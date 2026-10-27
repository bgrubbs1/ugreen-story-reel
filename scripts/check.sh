#!/usr/bin/env bash
# Static-check the story-reel skill with the official Uliya checker.
#
# The official checker derives the expected skill name from the directory
# basename (`story-reel`). The canonical source lives in `skill/`, so this
# script stages a byte-identical copy into `build/story-reel/` and checks it.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT="$ROOT/tooling/uliya-skill-kit"
STAGE="$ROOT/build/story-reel"

rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -R "$ROOT/skill/." "$STAGE/"

exec node "$KIT/scripts/check-skill.mjs" "$STAGE"
