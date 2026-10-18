import io
import json
from pathlib import Path

import pytest
from werkzeug.test import EnvironBuilder

from adapter import http_reader
from adapter.http_reader import app
from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS

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
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)
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


# --- HDE-CRD-0002 WU-PR-05 (S19-F01, S19-F04): the writer JSON helper refuses JSON nested past the
# parser's recursion limit, and bounds the read itself when Content-Length is absent ------------------

def test_s19_writer_json_helper_refuses_deeply_nested_json(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    resp = http_reader.create_app().test_client().post(
        "/internal/dev/sampler", data=b"[" * 32_768, headers={"Content-Type": "application/json; charset=utf-8"}
    )
    assert resp.status_code == 400
    assert resp.headers["Cache-Control"] == "no-store"
    assert json.loads(resp.data)["code"] == "ERR_WRITER_INVALID_JSON"


class _S19CountingStream(io.BytesIO):
    def __init__(self, data: bytes) -> None:
        super().__init__(data)
        self.consumed = 0

    def read(self, size=-1):
        chunk = super().read(size)
        self.consumed += len(chunk)
        return chunk


def test_s19_writer_json_read_is_bounded_when_content_length_is_absent(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    stream = _S19CountingStream(b"{" + b" " * (4 * http_reader._MAX_WRITER_BYTES) + b"}")
    environ = EnvironBuilder(path="/internal/dev/sampler", method="POST", content_type="application/json; charset=utf-8").get_environ()
    environ.pop("CONTENT_LENGTH", None)
    environ["wsgi.input"] = stream
    environ["wsgi.input_terminated"] = True  # a chunked request, as gunicorn presents it
    with http_reader.create_app().request_context(environ):
        payload, error = http_reader._read_writer_json(allow_empty_body=False, allowed_keys={"viewer_id"})
    assert payload is None and error.status_code == 413
    assert json.loads(error.get_data())["code"] == "ERR_WRITER_REQUEST_TOO_LARGE"
    assert stream.consumed <= http_reader._MAX_WRITER_BYTES + 1
