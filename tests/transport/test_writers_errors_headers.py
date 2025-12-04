import json
from pathlib import Path

import pytest

from adapter.http_reader import app

pytestmark = pytest.mark.epic020

SNAP_PATH = Path("tests/transport/headers/no_store_writers_errors.snap")


def _load_snapshot() -> dict[str, dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None
    label = None
    for raw in SNAP_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            label = line.strip("[]")
            current = {}
            sections[label] = current
            continue
        if current is None:
            raise AssertionError("snapshot missing section header")
        key, value = line.split(":", 1)
        current[key.lower()] = value.strip()
    return sections


def _headers(resp):
    headers = {k.lower(): v for k, v in resp.headers.items()}
    for forbidden in ("etag",):
        assert forbidden not in headers
    return headers


def test_writers_errors_headers(monkeypatch):
    for key, value in {
        "APP_ENV": "dev",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "HDE_TEST_TOKEN_ADMIN": "adm",
        "HDE_TEST_TOKEN_NONE": "none",
    }.items():
        monkeypatch.setenv(key, value)

    snapshot = _load_snapshot()
    client = app.test_client()

    ok_resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer adm",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={},
    )
    ok_headers = _headers(ok_resp)
    assert ok_resp.status_code == int(snapshot["success"]["status"])
    for key, value in snapshot["success"].items():
        if key == "status":
            continue
        assert ok_headers.get(key) == value

    err_resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer wrong",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={},
    )
    err_headers = _headers(err_resp)
    assert err_resp.status_code == int(snapshot["error"]["status"])
    for key, value in snapshot["error"].items():
        if key == "status":
            continue
        assert err_headers.get(key) == value
