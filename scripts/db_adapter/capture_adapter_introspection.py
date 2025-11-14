"""Harness to capture DB adapter introspection payloads via the bridge."""
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

Artifact = tuple[str, Callable[[], Mapping[str, Any]], Callable[[Mapping[str, Any]], None]]


def _write_artifact(name: str, payload: Mapping[str, Any]) -> None:
    out_path = Path("artifacts/engine") / name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path} ({len(text)} bytes)")


def _validate_status(payload: Mapping[str, Any], *, kind: str) -> None:
    status = payload.get("status")
    if status != "ok":
        raise RuntimeError(f"{kind} status != ok: {status!r}")


def _validate_search_path(payload: Mapping[str, Any]) -> None:
    _validate_status(payload, kind="search_path")
    value = payload.get("search_path")
    if not isinstance(value, str):
        raise RuntimeError("search_path payload missing string search_path")
    if value != EXPECTED_SEARCH_PATH:
        raise RuntimeError(f"unexpected search_path value: {value!r}")
    print(f"search_path → status=ok, search_path={value}")


def _validate_fingerprint(payload: Mapping[str, Any]) -> None:
    _validate_status(payload, kind="fingerprint")
    objects = payload.get("objects")
    if not isinstance(objects, list):
        raise RuntimeError("fingerprint payload missing objects list")
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


def _capture(db: DBAccess, label: str, call: Callable[[], Mapping[str, Any]], validator: Callable[[Mapping[str, Any]], None]) -> None:
    payload = call()
    if not isinstance(payload, Mapping):
        raise RuntimeError(f"{label} payload is not a mapping: {type(payload)!r}")
    validator(payload)
    _write_artifact(label, payload)


def main() -> int:
    db = DBAccess.for_current_env()
    print(f"Adapter provider: {db.provider_name}")

    captures: tuple[Artifact, ...] = (
        ("db_adapter.version.json", db.introspect_version, _validate_version),
        ("db_adapter.search_path.json", db.introspect_search_path, _validate_search_path),
        ("db_adapter.fingerprint.json", db.introspect_fingerprint, _validate_fingerprint),
    )

    for name, func, validator in captures:
        _capture(db, name, func, validator)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AdapterError as exc:
        print(f"ADAPTER ERROR: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
