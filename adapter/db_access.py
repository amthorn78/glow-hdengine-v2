"""Direct-only DB compatibility resolver."""
from __future__ import annotations

import os
from typing import Any, Dict

from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import AdapterError, PrimaryUnavailable, RetiredBridgeConfiguration


class _EnvMatrixProvider:
    name = "psycopg"

    def health(self) -> None:
        return None


MISSING_DB_CONFIG = {"schema":"hde.db.env_selection.v2","ok":False,"checks":[],"result":None,"error":{"class":"PrimaryUnavailable","code":"missing_database_url","retired_keys":[]}}

class DBStatus(dict):
    """Dictionary subtype describing an individual connection attempt."""


def _error_payload(exc: AdapterError) -> dict[str, Any]:
    return {"class": exc.__class__.__name__, "code": exc.code, "retired_keys": list(getattr(exc, "retired_keys", ())) }


def _attempts_for_error(exc: AdapterError) -> list[dict[str, Any]]:
    attempts = getattr(exc, "attempt_rows", None)
    if attempts is not None:
        return [dict(row) for row in attempts]
    if isinstance(exc, RetiredBridgeConfiguration):
        return []
    status = "skip" if exc.code == "missing_database_url" else "error"
    return [{"provider": "psycopg", "status": status, "reason": exc.code}]


def db_resolve(preference: str = "dsn") -> Dict[str, Any]:
    """Return the legacy resolver shape using DBAccess as the only selector."""
    try:
        db = DBAccess.for_current_env()
    except AdapterError as exc:
        return {"schema":"hde.db.resolve.v2","active":"none","attempts":_attempts_for_error(exc),"error":_error_payload(exc)}
    return {"schema":"hde.db.resolve.v2","active":getattr(db, "provider_name", "psycopg"),"attempts":list(getattr(db, "attempts", ())),"error":None}


def _checks_from_case(case: dict[str, Any]) -> list[dict[str, str]]:
    checks = [{"name":"DATABASE_URL","value_kind":case.get("database_url_presence", "unset")}]
    retired = set(case.get("retired_keys_present") or [])
    checks.extend(
        {"name": name, "value_kind": "present_retired" if name in retired else "unset"}
        for name in RETIRED_DB_TRANSPORT_KEYS
    )
    return checks


def resolve_env_matrix() -> tuple[bool, Dict[str, Any]]:
    """Return legacy env matrix formatting from DBAccess selection evidence only."""
    try:
        db = DBAccess.for_current_env(psycopg_factory=lambda _dsn: _EnvMatrixProvider())
        case = dict(db.selection_evidence())
        payload = {"schema":"hde.db.env_selection.v2","ok":True,"checks":_checks_from_case(case),"result":{"provider":getattr(db, "provider_name", "psycopg")},"error":None}
        return True, payload
    except AdapterError as exc:
        case = DBAccess.selection_failure_evidence(exc)
        payload = {"schema":"hde.db.env_selection.v2","ok":False,"checks":_checks_from_case(case),"result":None,"error":_error_payload(exc)}
        return False, payload


def db_rw_smoke(preference: str = "dsn") -> tuple[str, str]:
    """Run the legacy write/delete smoke through the selected DBAccess facade."""
    if os.getenv("DB_REQUIRED", "0") != "1":
        return "skip", "DB_REQUIRED=0"
    try:
        db = DBAccess.for_current_env()
        db.exec("SET search_path TO hde, public")
        rows = db.query("INSERT INTO hde.public_results (id, release_id, payload) VALUES (gen_random_uuid(), 'qa_smoke', '{}'::jsonb) RETURNING id")
        if not rows or not rows[0]:
            raise RuntimeError("smoke_insert_missing_id")
        db.exec("DELETE FROM hde.public_results WHERE id=%s", (rows[0][0],))
        return "ok", "db_rw_smoke_ok"
    except PrimaryUnavailable:
        return "skip", "no_working_path"
    except RetiredBridgeConfiguration:
        return "skip", "no_working_path"
    except Exception:
        return "error", "db_rw_smoke_failed"
