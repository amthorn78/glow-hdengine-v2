"""Verify a restored Railway backup using the Engine DB adapter."""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from engine.db.adapter import DBAccess
from engine.db.errors import AdapterError, IntrospectionError, SqlExecError


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _db_alias() -> str:
    alias = (
        os.getenv("RESTORE_DB_ALIAS")
        or os.getenv("DB_ALIAS")
        or os.getenv("DATABASE_ALIAS")
        or os.getenv("APP_DB_ALIAS")
        or "restored-db"
    )
    value = alias.strip()
    return value or "restored-db"


def _print(line: str) -> None:
    sys.stdout.write(line + "\n")


def _body_graphs_exists(db: DBAccess) -> bool:
    rows = db.query("select to_regclass('hde.body_graphs') is not null")
    if not rows:
        return False
    return bool(rows[0][0])


def _body_graphs_count(db: DBAccess) -> int:
    rows = db.query("select count(*) from hde.body_graphs")
    if not rows:
        return 0
    return int(rows[0][0])


def main(argv: list[str] | None = None) -> int:
    del argv  # unused
    now = _utc_now()
    _print(f"{now} - backup restore verification")

    db_alias = _db_alias()
    provider_name = "unknown"
    search_path_status = "FAIL"
    search_path_value = ""
    table_status = "FAIL"
    row_count = 0
    result_status = "OK"
    error_detail: str | None = None

    try:
        db = DBAccess.for_current_env()
        provider_name = db.provider_name or "unknown"

        search_payload = db.introspect_search_path()
        search_path_value = str(search_payload.get("search_path", "")).strip()
        search_path_status = "OK" if search_path_value == "hde, public" else "FAIL"

        table_status = "OK" if _body_graphs_exists(db) else "FAIL"
        row_count = _body_graphs_count(db)

        if search_path_status != "OK" or table_status != "OK":
            result_status = "FAILED"
    except (AdapterError, IntrospectionError, SqlExecError) as exc:
        result_status = "FAILED"
        error_detail = f"adapter_error:{getattr(exc, 'code', 'unknown')}"
    except Exception as exc:  # pragma: no cover - defensive logging
        result_status = "FAILED"
        error_detail = f"unexpected_error:{exc.__class__.__name__}"

    _print(f"db_alias: {db_alias}")
    _print(f"provider: {provider_name}")
    _print(f"check_search_path: {search_path_status} (value='{search_path_value}')")
    _print(f"body_graphs_exists: {table_status}")
    _print(f"rows_in_body_graphs: {row_count}")

    if error_detail:
        _print(f"error: {error_detail}")

    _print(f"result: {result_status}")

    return 0 if result_status == "OK" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
