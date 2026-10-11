#!/usr/bin/env bash
# Build completo del sitio: Nikola genera docs/ y Pagefind le agrega el
# indice del buscador en docs/pagefind/. Usar siempre esto en lugar de
# `nikola build` solo, si no el buscador queda desactualizado.
#
# Uso: ./build.sh
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
    uv venv
fi
uv pip install -q -r requirements.txt

uv run nikola build
uv run python -m pagefind --site docs
