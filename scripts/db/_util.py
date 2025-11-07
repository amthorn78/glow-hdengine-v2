from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator
import os
from urllib.parse import urlparse

import psycopg


def _is_pg_dsn(value: str | None) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    scheme = parsed.scheme or value.split(":", 1)[0]
    return scheme in ("postgres", "postgresql")


def dsn_for_db_scripts() -> str:
    dsn1 = os.getenv("DATABASE_URL")
    dsn2 = os.getenv("DB_BRIDGE_URL")

    if dsn1:
        try:
            with psycopg.connect(dsn1, connect_timeout=5) as _conn:
                pass
            return dsn1
        except Exception:
            pass

    if _is_pg_dsn(dsn2):
        with psycopg.connect(dsn2, connect_timeout=5) as _conn:
            pass
        return dsn2

    raise RuntimeError("missing_db_config")


@contextmanager
def connect() -> Iterator["psycopg.Connection"]:
    dsn = dsn_for_db_scripts()
    conn = psycopg.connect(dsn, connect_timeout=5)
    try:
        with conn:
            yield conn
    finally:
        conn.close()


def ensure_artifact(path: str) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def write_text(path: str, content: str) -> None:
    target = ensure_artifact(path)
    target.write_text(content, encoding="utf-8")
