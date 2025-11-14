"""Harness to capture bridge introspection endpoints."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib import error, request

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.ops.http_log import log_http_call

EXPECTED_SEARCH_PATH = "hde, public"
ROW_LIMIT = 1000  # Defensive upper bound when counting list payloads

ENDPOINTS = {
    "introspect.search_path.json": "/introspect/search_path",
    "introspect.grants.json": "/introspect/grants",
    "introspect.fingerprint.json": "/introspect/fingerprint",
}


def _bridge_base_url() -> str:
    value = (os.environ.get("DB_BRIDGE_URL") or "").strip()
    if not value:
        raise SystemExit("DB_BRIDGE_URL is not set")
    return value.rstrip("/")


def _fetch_json(base: str, path: str) -> Any:
    url = f"{base}{path}"
    req = request.Request(url, method="GET", headers={"Content-Type": "application/json"})
    start = time.monotonic()
    status: int | str = "error"
    try:
        with request.urlopen(req, timeout=10.0) as resp:
            status = getattr(resp, "status", resp.getcode())
            body = resp.read()
    except error.HTTPError as exc:  # pragma: no cover - network behavior
        status = exc.code
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{url} returned status {exc.code}: {detail}") from None
    except Exception as exc:  # pragma: no cover - network behavior
        raise RuntimeError(f"Request to {url} failed: {exc}") from None
    if status != 200:
        raise RuntimeError(f"{url} returned status {status}")
    try:
        return json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as exc:  # pragma: no cover - invalid JSON
        raise RuntimeError(f"Failed to parse JSON from {url}: {exc}") from None
    finally:
        duration = (time.monotonic() - start) * 1000.0
        log_http_call(route=f"db_bridge.get:{path}", status=status, duration_ms=duration)


def _validate_search_path(payload: Any) -> None:
    if not isinstance(payload, dict):
        raise RuntimeError("/introspect/search_path response is not an object")
    status = payload.get("status")
    if status != "ok":
        raise RuntimeError(f"/introspect/search_path status != ok: {status}")
    value = payload.get("search_path")
    if not isinstance(value, str):
        raise RuntimeError("/introspect/search_path missing string search_path")
    if value != EXPECTED_SEARCH_PATH:
        raise RuntimeError(f"unexpected search_path value: {value!r}")
    print(f"/introspect/search_path → status=ok, search_path={value}")


def _validate_grants(payload: Any) -> None:
    if not isinstance(payload, dict):
        raise RuntimeError("/introspect/grants response is not an object")
    status = payload.get("status")
    if status != "ok":
        raise RuntimeError(f"/introspect/grants status != ok: {status}")
    grants = payload.get("grants")
    if not isinstance(grants, (list, dict)):
        raise RuntimeError("/introspect/grants payload missing grants list or dict")
    size = len(grants)
    if size > ROW_LIMIT:
        raise RuntimeError(f"/introspect/grants returned {size} entries (> {ROW_LIMIT})")
    emptiness = "empty" if size == 0 else "non-empty"
    print(f"/introspect/grants → status=ok, grants={emptiness}, entries={size}")


def _validate_fingerprint(payload: Any) -> None:
    if not isinstance(payload, dict):
        raise RuntimeError("/introspect/fingerprint response is not an object")
    status = payload.get("status")
    if status != "ok":
        raise RuntimeError(f"/introspect/fingerprint status != ok: {status}")
    objects = payload.get("objects")
    if not isinstance(objects, (list, dict)):
        raise RuntimeError("/introspect/fingerprint payload missing objects list or dict")
    size = len(objects)
    if size > ROW_LIMIT:
        raise RuntimeError(f"/introspect/fingerprint returned {size} entries (> {ROW_LIMIT})")
    print(f"/introspect/fingerprint → status=ok, entries={size}")


def _write_artifact(name: str, payload: Any) -> None:
    out_path = Path("artifacts/db") / name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path} ({len(text)} bytes)")


def main() -> int:
    base = _bridge_base_url()
    artifacts: dict[str, Any] = {}

    search_payload = _fetch_json(base, ENDPOINTS["introspect.search_path.json"])
    _validate_search_path(search_payload)
    artifacts["introspect.search_path.json"] = search_payload

    grants_payload = _fetch_json(base, ENDPOINTS["introspect.grants.json"])
    _validate_grants(grants_payload)
    artifacts["introspect.grants.json"] = grants_payload

    fingerprint_payload = _fetch_json(base, ENDPOINTS["introspect.fingerprint.json"])
    _validate_fingerprint(fingerprint_payload)
    artifacts["introspect.fingerprint.json"] = fingerprint_payload

    for name, payload in artifacts.items():
        _write_artifact(name, payload)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
