#!/usr/bin/env bash
set -euo pipefail
if [ $# -ne 1 ] || [ ! -f "$1" ]; then
  echo "usage: release_id.sh <manifest.json>" >&2
  exit 64
fi
MANIFEST="$1"

# Prefer sha256sum; fallback to Python if unavailable
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$MANIFEST" | awk '{print $1}'
else
  python - <<'PY'
import sys,hashlib,Pathlib
from pathlib import Path
p=Path(sys.argv[1]).read_bytes()
print(hashlib.sha256(p).hexdigest())
PY
fi
