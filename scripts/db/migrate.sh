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

with _util.connect() as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                migration text PRIMARY KEY,
                applied_at timestamptz NOT NULL DEFAULT now()
            )
            """
        )
    conn.commit()

    for path in paths:
        name = path.name
        with conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM schema_migrations WHERE migration = %s",
                (name,),
            )
            if cur.fetchone():
                continue

        sql = path.read_text(encoding="utf-8")
        log_lines.append(f"apply {name}")

        with conn.cursor() as cur:
            cur.execute(sql)
            cur.execute(
                "INSERT INTO schema_migrations (migration) VALUES (%s)",
                (name,),
            )
        conn.commit()

if not log_lines:
    log_text = "no-op: no migrations to run\n"
else:
    log_text = "\n".join(log_lines) + "\n"

_util.write_text(TARGET, log_text)
PY
