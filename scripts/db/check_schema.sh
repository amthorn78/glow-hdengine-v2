#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from scripts.db import _util

TARGET = "artifacts/db/check_schema.txt"

with _util.connect() as conn:
    with conn.cursor() as cur:
        cur.execute("SHOW search_path")
        value = (cur.fetchone() or [""])[0].strip()

if value != "hde, public":
    raise SystemExit(f"unexpected search_path: {value!r}")

_util.write_text(TARGET, value + "\n")
PY
