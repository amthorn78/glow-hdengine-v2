from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator
import os
from urllib.parse import urlparse

import psycopg


class MissingDbConfigError(RuntimeError):
    code = "missing_db_config"

    def __init__(self, message: str = "missing_db_config", *, attempts: list[str] | None = None):
        super().__init__(message)
        self.attempts = attempts or []


def _is_pg_dsn(value: str | None) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    scheme = parsed.scheme or value.split(":", 1)[0]
    return scheme in ("postgres", "postgresql")


def _env_allows_bridge_fallback() -> bool:
    env = (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "").strip().lower()
    if not env:
        return True
    return env in {"dev", "development", "test", "testing"}


def dsn_for_db_scripts() -> str:
    dsn1 = os.getenv("DATABASE_URL")
    dsn2 = os.getenv("DB_BRIDGE_URL")

    attempts: list[str] = []

    if dsn1:
        try:
            with psycopg.connect(dsn1, connect_timeout=5) as _conn:
                pass
            return dsn1
        except Exception:
            attempts.append("DATABASE_URL")

    allow_bridge = _env_allows_bridge_fallback()

    if _is_pg_dsn(dsn2) and (allow_bridge or not dsn1):
        try:
            with psycopg.connect(dsn2, connect_timeout=5) as _conn:
                pass
            return dsn2
        except Exception:
            attempts.append("DB_BRIDGE_URL")
    elif _is_pg_dsn(dsn2) and not allow_bridge:
        attempts.append("DB_BRIDGE_URL")

    raise MissingDbConfigError(attempts=attempts)


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
