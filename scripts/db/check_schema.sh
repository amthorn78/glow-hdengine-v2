#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from scripts.db import _util

import sys

TARGET = "artifacts/db/check_schema.txt"

try:
    with _util.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SHOW search_path")
            value = (cur.fetchone() or [""])[0].strip()
except _util.MissingDbConfigError:
    value = "(missing_db_config)"
    print(
        "WARNING: database connection unavailable; recorded search_path as '(missing_db_config)'",
        file=sys.stderr,
    )

if value != "hde, public":
    print(f"WARNING: expected 'hde, public' search_path, observed {value!r}", file=sys.stderr)

_util.write_text(TARGET, value + "\n")
PY
