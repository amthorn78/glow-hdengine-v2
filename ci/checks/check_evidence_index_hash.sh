#!/usr/bin/env bash
set -euo pipefail
calc=$(sha256sum docs/evidence/INDEX.json | awk '{print $1}')
stored=$(cat docs/evidence/INDEX.sha256)
if [[ "$calc" != "$stored" ]]; then
  echo "INDEX_SHA_MISMATCH:${stored}:${calc}" >&2
  exit 1
fi
