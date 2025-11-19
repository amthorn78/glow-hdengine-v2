#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f docs/evidence/INDEX.json || ! -f docs/evidence/INDEX.sha256 ]]; then
  echo "INDEX_FILES_MISSING" >&2
  exit 1
fi

expected=$(cut -d ' ' -f1 < docs/evidence/INDEX.sha256)
actual=$(sha256sum docs/evidence/INDEX.json | awk '{print $1}')

if [[ "$expected" != "$actual" ]]; then
  echo "INDEX_SHA_MISMATCH:${expected}!=$actual" >&2
  exit 1
fi
