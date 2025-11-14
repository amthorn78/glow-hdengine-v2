#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

from pathlib import Path

from scripts.db import _util

TARGET = "artifacts/db/migration_runner.log"
MIGRATIONS_DIR = Path("migrations")

paths = sorted(p for p in MIGRATIONS_DIR.glob("*.sql") if p.is_file())

log_lines: list[str] = []

db = _util.db_access()

db.exec(
    """
    CREATE TABLE IF NOT EXISTS schema_migrations (
        migration text PRIMARY KEY,
        applied_at timestamptz NOT NULL DEFAULT now()
    )
    """
)

for path in paths:
    name = path.name
    existing = db.query("SELECT 1 FROM schema_migrations WHERE migration = %s", (name,))
    if existing:
        continue

    sql = path.read_text(encoding="utf-8")
    log_lines.append(f"apply {name}")

    db.tx(
        [
            _util.Statement(sql=sql),
            _util.Statement(
                sql="INSERT INTO schema_migrations (migration) VALUES (%s)",
                params=(name,),
            ),
        ]
    )

if not log_lines:
    log_text = "no-op: no migrations to run\n"
else:
    log_text = "\n".join(log_lines) + "\n"

_util.write_text(TARGET, log_text)
