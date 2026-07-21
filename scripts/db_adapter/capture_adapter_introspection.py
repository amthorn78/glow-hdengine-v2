"""Harness to capture direct PostgreSQL DB adapter introspection payloads."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db.adapter import DBAccess
from engine.db.errors import AdapterError

EXPECTED_SEARCH_PATH = "hde, public"
ROW_LIMIT = 1000
Artifact = tuple[
    str,
    Callable[[], Mapping[str, Any]],
    Callable[[Mapping[str, Any]], None],
]


def _write_artifact(name: str, payload: Mapping[str, Any]) -> None:
    output = Path("artifacts/engine") / name
    output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    output.write_text(text, encoding="utf-8")
    print(f"Wrote {output} ({len(text)} bytes)")


def _validate_status(payload: Mapping[str, Any], *, kind: str) -> None:
    if payload.get("status") != "ok":
        raise RuntimeError(f"{kind} status != ok")


def _validate_search_path(payload: Mapping[str, Any]) -> None:
    _validate_status(payload, kind="search_path")
    value = payload.get("search_path")
    if value != EXPECTED_SEARCH_PATH:
        raise RuntimeError("unexpected search_path value")
    print(f"search_path → status=ok, search_path={value}")


def _validate_fingerprint(payload: Mapping[str, Any]) -> None:
    _validate_status(payload, kind="fingerprint")
    objects = payload.get("objects")
    if not isinstance(objects, (list, Mapping)):
        raise RuntimeError("fingerprint payload missing objects collection")
    size = len(objects)
    if size > ROW_LIMIT:
        raise RuntimeError(f"fingerprint payload exceeded guard ({size} > {ROW_LIMIT})")
    print(f"fingerprint → status=ok, entries={size}")


def _validate_version(payload: Mapping[str, Any]) -> None:
    _validate_status(payload, kind="version")
    version = payload.get("version")
    if not isinstance(version, str) or not version:
        raise RuntimeError("version payload missing non-empty version string")
    print(f"version → status=ok, version={version}")


def _capture(
    db: DBAccess,
    label: str,
    call: Callable[[], Mapping[str, Any]],
    validate: Callable[[Mapping[str, Any]], None],
) -> None:
    del db
    payload = call()
    if not isinstance(payload, Mapping):
        raise RuntimeError(f"{label} payload is not a mapping")
    validate(payload)
    _write_artifact(label, payload)


def main() -> int:
    db = DBAccess.for_current_env()
    if db.provider_name != "psycopg":
        raise RuntimeError("direct PostgreSQL provider required")
    print("Adapter provider: psycopg")
    captures: tuple[Artifact, ...] = (
        ("db_adapter.version.json", db.introspect_version, _validate_version),
        ("db_adapter.search_path.json", db.introspect_search_path, _validate_search_path),
        ("db_adapter.fingerprint.json", db.introspect_fingerprint, _validate_fingerprint),
    )
    for name, call, validate in captures:
        _capture(db, name, call, validate)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AdapterError:
        print("ADAPTER ERROR: direct_db_unavailable")
        raise SystemExit(1)
    except Exception:
        print("ERROR: direct_introspection_failed")
        raise SystemExit(1)
