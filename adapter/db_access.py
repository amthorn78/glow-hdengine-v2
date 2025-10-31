"""DB connectivity resolver that attempts both DSN and Bridge paths."""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict


class DBStatus(dict):
    """Dictionary subtype describing an individual connection attempt."""


def _rails_open() -> bool:
    return os.getenv("SAFE_MODE", "1") == "0" and os.getenv("ALLOW_NETWORK", "0") == "1"


def _try_dsn() -> DBStatus:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        return DBStatus(path="dsn", status="skip", reason="no_dsn")
    try:
        import psycopg  # type: ignore

        with psycopg.connect(dsn, connect_timeout=5) as conn, conn.cursor() as cur:  # type: ignore[attr-defined]
            try:
                cur.execute("SET LOCAL search_path TO hde, public")
            except Exception:
                cur.execute("SET search_path TO hde, public")
            cur.execute("SHOW server_version")
            ver = cur.fetchone()[0]
            cur.execute("SHOW search_path")
            sp = cur.fetchone()[0]
            cur.execute("SELECT current_user")
            role = cur.fetchone()[0]
        return DBStatus(path="dsn", status="ok", server_version=ver, search_path=sp, role=role)
    except Exception as exc:  # pragma: no cover - depends on env
        return DBStatus(path="dsn", status="unreachable", reason=str(exc))


def _try_bridge() -> DBStatus:
    url = os.environ.get("DB_BRIDGE_URL")
    if not url:
        return DBStatus(path="bridge", status="skip", reason="no_bridge_url")
    if not _rails_open():
        return DBStatus(path="bridge", status="skip", reason="rails_closed")
    try:
        req = urllib.request.Request(url.rstrip("/") + "/meta", method="GET")
        with urllib.request.urlopen(req, timeout=10) as resp:
            meta = json.loads(resp.read().decode("utf-8"))
        return DBStatus(
            path="bridge",
            status="ok",
            server_version=meta.get("server_version", ""),
            search_path=meta.get("search_path", ""),
            role=meta.get("role", ""),
        )
    except Exception as exc:  # pragma: no cover - depends on env
        return DBStatus(path="bridge", status="unreachable", reason=str(exc))


def db_resolve(preference: str = "dsn") -> Dict[str, Any]:
    """Attempt both DSN and Bridge and pick the first success by preference."""

    dsn = _try_dsn()
    bridge = _try_bridge()
    ordered = [dsn, bridge] if preference == "dsn" else [bridge, dsn]
    active = "none"
    for candidate in ordered:
        if candidate.get("status") == "ok":
            active = candidate["path"]
            break
    return {"active": active, "dsn": dsn, "bridge": bridge}


def db_rw_smoke(preference: str = "dsn") -> tuple[str, str]:
    """Perform a read/write smoke test using the active path if required."""

    if os.getenv("DB_REQUIRED", "0") != "1":
        return "skip", "DB_REQUIRED=0"

    resolved = db_resolve(preference)
    if resolved["active"] == "dsn":
        try:
            import psycopg  # type: ignore

            dsn = os.environ["DATABASE_URL"]
            with psycopg.connect(dsn, connect_timeout=5) as conn, conn.cursor() as cur:  # type: ignore[attr-defined]
                try:
                    cur.execute("SET LOCAL search_path TO hde, public")
                except Exception:
                    cur.execute("SET search_path TO hde, public")
                cur.execute(
                    "INSERT INTO hde.public_results (id, release_id, payload) "
                    "VALUES (gen_random_uuid(), 'qa_smoke', '{}'::jsonb) RETURNING id"
                )
                rid = cur.fetchone()[0]
                cur.execute("DELETE FROM hde.public_results WHERE id=%s", (rid,))
                return "ok", f"id={rid}"
        except Exception as exc:  # pragma: no cover - env dependent
            return "error", str(exc)
    elif resolved["active"] == "bridge":
        try:
            req = urllib.request.Request(
                os.environ["DB_BRIDGE_URL"].rstrip("/") + "/rw-smoke",
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                return "ok", resp.read().decode("utf-8")[:200]
        except Exception:  # pragma: no cover - depends on env
            return "skip", "bridge_smoke_not_implemented"
    return "skip", "no_working_path"

