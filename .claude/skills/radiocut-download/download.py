#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Download a RadioCut audiocut as a single MP3 file.

RadioCut streams audio in 120-second chunks behind an obfuscated index
endpoint. This script reproduces the player's chunk-fetching logic, downloads
only the chunks that cover the cut, concatenates them, and trims to the exact
start/duration with ffmpeg. See SKILL.md for the protocol details.

Requires: ffmpeg in PATH.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/115.0"
RADIOCUT = "https://radiocut.fm"
INDEX_HOST = "https://chunkserver-do.radiocut.site"
SLOT_SIZE = 10_000  # seconds per slot (matches JS _seconds_to_slot)


def fetch(url: str, referer: str | None = None) -> bytes:
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        return r.read()


def slug_to_url(s: str) -> str:
    if s.startswith("http"):
        return s
    return f"{RADIOCUT}/audiocut/{s.strip('/')}/"


def parse_audio_jsonld(html: bytes) -> dict:
    text = html.decode("utf-8", errors="replace")
    m = re.search(
        r'<script type="application/ld\+json">\s*(\[.*?\])\s*</script>',
        text, re.DOTALL,
    )
    if not m:
        raise RuntimeError("No JSON-LD block found on the audiocut page")
    for item in json.loads(m.group(1)):
        if item.get("@type") == "AudioObject":
            return item
    raise RuntimeError("No AudioObject in JSON-LD")


def parse_content_url(url: str) -> tuple[str, float, float]:
    """Return (station, start_epoch, duration) from the JSON-LD contentUrl."""
    m = re.search(r"/get_unified_file/([^/]+)/([\d.]+)/([\d.]+)", url)
    if not m:
        raise RuntimeError(f"Cannot parse contentUrl: {url}")
    return m.group(1), float(m.group(2)), float(m.group(3))


def slot_index_url(station: str, slot: int) -> str:
    """Reproduce the JS _make_url_web obfuscation."""
    raw = f"dHn8{station}|{slot}oUac"
    enc = base64.b64encode(raw.encode()).decode()
    safe = enc.replace("=", "~").replace("+", "-").replace("/", "_")
    return f"{INDEX_HOST}/server/gec/app/{safe}/"


def find_chunks(start: float, duration: float, station: str) -> list[dict]:
    end = start + duration
    slots = sorted({int(start // SLOT_SIZE), int(end // SLOT_SIZE)})
    chunks: list[dict] = []
    for slot in slots:
        idx = json.loads(fetch(slot_index_url(station, slot)))
        bucket = idx.get(str(slot)) or {}
        base_default = bucket.get("baseURL", "")
        for c in bucket.get("chunks", []):
            cs = float(c["start"])
            ce = cs + float(c["length"])
            if ce > start and cs < end:
                base = (c.get("base_url") or base_default).replace("http:", "https:")
                chunks.append({
                    "url": f"{base}/{c['filename']}",
                    "start": cs,
                    "length": float(c["length"]),
                })
    if not chunks:
        raise RuntimeError(
            f"No chunks found for cut at {start} (duration {duration}s, station {station})"
        )
    return sorted(chunks, key=lambda c: c["start"])


def main() -> int:
    ap = argparse.ArgumentParser(description="Download a RadioCut audiocut as an MP3.")
    ap.add_argument("url_or_slug", help="Full RadioCut URL or audiocut slug.")
    ap.add_argument("-o", "--output", help="Output MP3 path. Default: ./<slug>.mp3")
    ap.add_argument("--bitrate", default="32k",
                    help="Re-encode bitrate (default 32k). Ignored with --keep-original-bitrate.")
    ap.add_argument("--keep-original-bitrate", action="store_true",
                    help="Don't re-encode; use stream copy. Faster, preserves source bitrate (~16 kbps).")
    args = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found in PATH. Install with: sudo apt install ffmpeg")

    page_url = slug_to_url(args.url_or_slug)
    slug = page_url.rstrip("/").rsplit("/", 1)[-1]
    print(f"Page:     {page_url}", file=sys.stderr)

    audio = parse_audio_jsonld(fetch(page_url))
    station, start, duration = parse_content_url(audio["contentUrl"])
    title = (audio.get("name") or slug).strip()
    description = (audio.get("description") or "").strip()
    upload = (audio.get("uploadDate") or "")[:10]
    radio = (audio.get("author") or {}).get("name", "")
    show = (audio.get("isPartOf") or {}).get("name", "")

    print(f"Title:    {title}", file=sys.stderr)
    print(f"Station:  {radio} ({station})  Show: {show}", file=sys.stderr)
    print(f"Cut:      start={start}  duration={duration:.1f}s", file=sys.stderr)

    chunks = find_chunks(start, duration, station)
    print(f"Chunks:   {len(chunks)}", file=sys.stderr)

    output = Path(args.output) if args.output else Path(f"{slug}.mp3")
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        combined = td_path / "combined.mp3"
        with combined.open("wb") as out:
            for i, c in enumerate(chunks, 1):
                print(f"  [{i}/{len(chunks)}] {c['url']}", file=sys.stderr)
                out.write(fetch(c["url"], referer=f"{RADIOCUT}/"))

        offset = start - chunks[0]["start"]
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-ss", f"{offset:.3f}", "-t", f"{duration:.3f}",
            "-i", str(combined),
            "-metadata", f"title={title}",
            "-metadata", f"artist={radio}",
            "-metadata", f"album={show}",
            "-metadata", f"date={upload}",
            "-metadata", f"comment=Source: {page_url}\n{description}".strip(),
        ]
        if args.keep_original_bitrate:
            cmd += ["-c:a", "copy"]
        else:
            cmd += ["-codec:a", "libmp3lame", "-b:a", args.bitrate, "-ac", "1"]
        cmd.append(str(output))
        subprocess.run(cmd, check=True)

    size_kb = output.stat().st_size / 1024
    print(f"\nSaved:    {output}  ({size_kb:.1f} KiB, {duration:.1f}s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
