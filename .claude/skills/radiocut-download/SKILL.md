---
name: radiocut-download
description: Download an audiocut from radiocut.fm as a single MP3 file (used when the user wants to save/backup a RadioCut clip locally, since RadioCut no longer exposes a direct MP3 URL).
---

# RadioCut downloader

RadioCut.fm streams audio in 120-second chunks served from Backblaze and indexed by an obfuscated endpoint at `chunkserver-do.radiocut.site`. There's no direct "Download MP3" link. This skill reproduces the player's chunk-fetching logic, reassembles only the chunks that cover the cut, and trims to the exact duration with ffmpeg.

## When to use

Whenever the user wants to save, archive, or back up an audio clip from `radiocut.fm`. Examples: *"baja este audio de RadioCut"*, *"necesito guardar esta columna localmente"*, *"vamos a archivarlo por si el sitio cae"*.

## Usage

```bash
./.claude/skills/radiocut-download/download.py <url-or-slug> [-o output.mp3] [--bitrate 32k]
```

Examples:

```bash
# By full URL
./.claude/skills/radiocut-download/download.py \
  https://radiocut.fm/audiocut/en-nuestra-columna-de-open-data-andres-vazquez/

# By slug only, custom output
./.claude/skills/radiocut-download/download.py en-nuestra-columna-de-open-data-andres-vazquez \
  -o custom-statics/audio/odc/columna-genfm-2017-07-03.mp3

# Skip re-encoding (faster, preserves original 16 kbps)
./.claude/skills/radiocut-download/download.py <slug> --keep-original-bitrate
```

The script writes ID3 metadata (title, artist=radiostation, album=show, date, comment with source URL + description) extracted from the page's JSON-LD.

## Requirements

- Python 3.10+ (uses `uv run --script` via PEP 723 inline metadata, no extra deps).
- `ffmpeg` in PATH for trimming and re-encoding. Install with `apt install ffmpeg`.

## How it works (for future maintenance)

If RadioCut changes their player and the script breaks, here's the trail:

1. **JSON-LD on the audiocut page** has `contentUrl: ".../get_unified_file/<station>/<start>/<duration>"`. That endpoint returns 404 (deprecated), but the timestamp + duration + station are what we need.
2. **Slot index endpoint:** `chunkserver-do.radiocut.site/server/gec/app/<obfuscated>/`. Slot is `floor(start_epoch / 10000)`. The `<obfuscated>` part is `base64("dHn8" + station + "|" + slot + "oUac")` with URL-safe replacements (`=→~`, `+→-`, `/→_`). The obfuscation lives in `_make_url_web` inside `static.radiocut.com.ar/js/embed_master.<hash>.js` — a small array shuffle (`["replace","dHn8","toString"]` rotated 166 times → 1 shift mod 3).
3. **Chunks JSON** lists 120-second MP3 chunks with `start`, `length`, `filename`, and `baseURL` pointing to a Backblaze bucket (`b2-f000.radiocut.com.ar/file/...`). Filter by overlap with `[cut_start, cut_start+duration]`.
4. **Chunk download:** must use HTTPS (the JS does `.replace("http:", "https:")`) and send `Referer: https://radiocut.fm/`, otherwise B2 returns 521.
5. **Reassembly:** concat with `cat` (CBR MP3, byte-level concat is fine), then `ffmpeg -ss <offset> -t <duration>` to trim. Offset = `cut_start - first_chunk_start`.

If the slot index endpoint changes shape (new path or new obfuscation), reverse-engineer `embed_master.js` again — search for `_make_url_web` and `audio_base_url+"/server/`.
