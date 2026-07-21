"""Direct-only DB compatibility resolver."""
from __future__ import annotations

import os
from typing import Any, Dict

from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS, retired_db_transport_keys_present
from engine.db.errors import AdapterError, PrimaryUnavailable, RetiredBridgeConfiguration

MISSING_DB_CONFIG = {"schema":"hde.db.env_selection.v2","ok":False,"checks":[],"result":None,"error":{"class":"PrimaryUnavailable","code":"missing_database_url","retired_keys":[]}}

class DBStatus(dict):
    """Dictionary subtype describing an individual connection attempt."""


def _error_payload(exc: AdapterError) -> dict[str, Any]:
    return {"class": exc.__class__.__name__, "code": exc.code, "retired_keys": list(getattr(exc, "retired_keys", ())) }


def db_resolve(preference: str = "dsn") -> Dict[str, Any]:
    try:
        db = DBAccess.for_current_env()
    except AdapterError as exc:
        attempts = [] if isinstance(exc, RetiredBridgeConfiguration) else [{"provider":"psycopg","status":"skip" if exc.code == "missing_database_url" else "error","reason":exc.code}]
        return {"schema":"hde.db.resolve.v2","active":"none","attempts":attempts,"error":_error_payload(exc)}
    return {"schema":"hde.db.resolve.v2","active":"psycopg","attempts":list(db.attempts),"error":None}


def resolve_env_matrix() -> tuple[bool, Dict[str, Any]]:
    checks = [{"name":"DATABASE_URL","value_kind":"present_redacted" if "DATABASE_URL" in os.environ and (os.environ.get("DATABASE_URL") or "").strip() else "unset"}]
    checks.extend({"name":name,"value_kind":"present_retired" if name in os.environ else "unset"} for name in RETIRED_DB_TRANSPORT_KEYS)
    retired = retired_db_transport_keys_present(os.environ)
    if retired:
        payload={"schema":"hde.db.env_selection.v2","ok":False,"checks":checks,"result":None,"error":{"class":"RetiredBridgeConfiguration","code":"retired_bridge_configuration","retired_keys":list(retired)}}
        return False,payload
    if (os.environ.get("DATABASE_URL") or "").strip():
        return True,{"schema":"hde.db.env_selection.v2","ok":True,"checks":checks,"result":{"provider":"psycopg"},"error":None}
    return False,{"schema":"hde.db.env_selection.v2","ok":False,"checks":checks,"result":None,"error":{"class":"PrimaryUnavailable","code":"missing_database_url","retired_keys":[]}}


def db_rw_smoke(preference: str = "dsn") -> tuple[str, str]:
    if os.getenv("DB_REQUIRED", "0") != "1":
        return "skip", "DB_REQUIRED=0"
    resolved = db_resolve(preference)
    if resolved["active"] != "psycopg":
        return "skip", "no_working_path"
    try:
        import psycopg  # type: ignore
        dsn = os.environ["DATABASE_URL"]
        with psycopg.connect(dsn, connect_timeout=5) as conn, conn.cursor() as cur:  # type: ignore[attr-defined]
            try:
                cur.execute("SET LOCAL search_path TO hde, public")
            except Exception:
                cur.execute("SET search_path TO hde, public")
            cur.execute("INSERT INTO hde.public_results (id, release_id, payload) VALUES (gen_random_uuid(), 'qa_smoke', '{}'::jsonb) RETURNING id")
            cur.fetchone()
            cur.execute("DELETE FROM hde.public_results WHERE release_id=%s", ("qa_smoke",))
            return "ok", "db_rw_smoke_ok"
    except Exception:
        return "error", "db_rw_smoke_failed"
