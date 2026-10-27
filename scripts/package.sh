#!/usr/bin/env bash
# Build the reproducible Initial Skill Package (Round 1 ZIP).
#
# Steps:
#   1. stage skill/ -> build/story-reel/ (directory name must equal skill name)
#   2. run the official Uliya checker on the staged directory (must exit 0)
#   3. zip the staged directory with SKILL.md at the ZIP root
#   4. enforce the 10 MB ZIP and uncompressed limits
#   5. unzip into a temp dir, re-run the checker there, print the file list
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT="$ROOT/tooling/uliya-skill-kit"
STAGE="$ROOT/build/story-reel"
ZIP="$ROOT/pre-test-skill-package.zip"
MAX_BYTES=$((10 * 1024 * 1024))

rm -rf "$STAGE" "$ROOT/build/unpacked" "$ZIP"
mkdir -p "$STAGE"
cp -R "$ROOT/skill/." "$STAGE/"
# Normalize mtimes so repeated builds produce a byte-identical ZIP.
find "$STAGE" -exec touch -t 202601010000.00 {} +

echo "== 1/5 stage =="
echo "staged: $STAGE"
find "$STAGE" -type f | sed "s#^$ROOT/##" | sort

echo
echo "== 2/5 official checker on staged skill =="
node "$KIT/scripts/check-skill.mjs" "$STAGE" | tee "$ROOT/build/check-staged.json"
# checker exits 0 only when uploadable (no errors)
node -e '
const r = require(process.argv[1]);
console.log("checker status:", r.status, "| errors:", r.summary.errors, "| warnings:", r.summary.warnings, "| info:", r.summary.info);
if (r.status === "not-uploadable") process.exit(1);
' "$ROOT/build/check-staged.json"

echo
echo "== 3/5 build zip =="
(cd "$STAGE" && zip -q -X -r "$ZIP" .)
echo "zip: $ZIP"

echo
echo "== 4/5 size limits =="
ZIP_BYTES=$(wc -c < "$ZIP" | tr -d ' ')
UNCOMPRESSED=$(find "$STAGE" -type f -exec wc -c {} + | tail -1 | awk '{print $1}')
FILE_COUNT=$(find "$STAGE" -type f | wc -l | tr -d ' ')
MAX_FILE=$(find "$STAGE" -type f -exec wc -c {} + | sed '$d' | awk '{print $1}' | sort -n | tail -1)
echo "zip bytes: $ZIP_BYTES (limit $MAX_BYTES)"
echo "uncompressed bytes: $UNCOMPRESSED (limit $MAX_BYTES)"
echo "files: $FILE_COUNT (limit 100), largest file: $MAX_FILE bytes (limit 1048576)"
test "$ZIP_BYTES" -le "$MAX_BYTES"
test "$UNCOMPRESSED" -le "$MAX_BYTES"
test "$FILE_COUNT" -le 100
test "$MAX_FILE" -le 1048576

echo
echo "== 5/5 verify unpacked package =="
# Unzip into a directory named exactly `story-reel`: the official checker derives
# the expected skill name from the directory basename.
UNPACKED="$ROOT/build/unpacked/story-reel"
rm -rf "$ROOT/build/unpacked"
mkdir -p "$UNPACKED"
unzip -q "$ZIP" -d "$UNPACKED"
test -f "$UNPACKED/SKILL.md"
echo "files in zip:"
unzip -l "$ZIP"
echo
node "$KIT/scripts/check-skill.mjs" "$UNPACKED" | tee "$ROOT/build/check-unpacked.json"
node -e '
const r = require(process.argv[1]);
console.log("unpacked checker status:", r.status, "| errors:", r.summary.errors, "| warnings:", r.summary.warnings);
if (r.status === "not-uploadable") process.exit(1);
' "$ROOT/build/check-unpacked.json"

echo
echo "PASS: package built, checked, and verified at $ZIP"
