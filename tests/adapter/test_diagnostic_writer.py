import hashlib
import json

import pytest

from adapter.http_reader import create_app, _MAX_WRITER_BYTES
from adapter.logging_filter import install as install_logging_filter
from engine.serializer import canon


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setenv("HDE_TEST_TOKEN_ADMIN", "admin-token")
    monkeypatch.setenv("HDE_TEST_TOKEN_NONE", "none-token")
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


@pytest.fixture()
def client_with_sink(monkeypatch):
    monkeypatch.setenv("HDE_TEST_TOKEN_ADMIN", "admin-token")
    monkeypatch.setenv("HDE_TEST_TOKEN_NONE", "none-token")
    app = create_app()
    install_logging_filter(app)
    sink: list[str] = []
    app.config.update(TESTING=True, LOG_SINK=sink)
    return app.test_client(), app, sink


def test_diagnostic_writer_success(client):
    resp = client.post("/ops/writer/diagnostic", headers={"Authorization": "Bearer admin-token"})
    assert resp.status_code == 200
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert "Content-Encoding" not in resp.headers
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert resp.data.endswith(b"\n")
    assert resp.data == b'{"message":"diagnostic","ok":true}\n'


def test_diagnostic_writer_requires_bearer(client):
    resp = client.post("/ops/writer/diagnostic")
    assert resp.status_code == 401
    assert resp.headers.get("WWW-Authenticate") == "Bearer"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.data == b'{"code":"unauthorized","error":"authorization required","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_forbids_insufficient_scope(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={"Authorization": "Bearer none-token"},
    )
    assert resp.status_code == 403
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.data == b'{"code":"forbidden","error":"insufficient scope","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_rejects_unknown_token(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={"Authorization": "Bearer nope"},
    )
    assert resp.status_code == 401
    assert resp.headers.get("WWW-Authenticate") == "Bearer"
    assert resp.data == b'{"code":"unauthorized","error":"authorization required","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_head_405(client):
    resp = client.head("/ops/writer/diagnostic")
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "POST, OPTIONS"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Length") == "0"
    assert resp.data == b""


def test_diagnostic_writer_options_204(client):
    resp = client.open("/ops/writer/diagnostic", method="OPTIONS")
    assert resp.status_code == 204
    assert resp.headers.get("Allow") == "POST, OPTIONS"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Length") == "0"
    assert resp.data == b""


def test_diagnostic_writer_idempotence_logged(client_with_sink):
    client, app, sink = client_with_sink
    resp = client.post("/ops/writer/diagnostic", headers={"Authorization": "Bearer admin-token"})
    assert resp.status_code == 200
    assert sink, "expected log entries for diagnostic writer"
    entry = json.loads(sink[-1])
    assert entry["route"] in {"diagnostic_writer", "reader_v1"}
    canonical_body = canon.sercanon({}, sort_keys=True)
    preimage = canon.sercanon(
        {
            "canonical_request_body": canonical_body.decode("utf-8"),
            "method": "POST",
            "writer_route_id": "ops.writer.diagnostic.v1",
        },
        sort_keys=True,
    )
    expected_hash = hashlib.sha256(preimage).hexdigest()
    assert entry["idempotence_hash"] == expected_hash


def test_diagnostic_writer_duplicate_same_status(client_with_sink):
    client, app, sink = client_with_sink
    resp_one = client.post("/ops/writer/diagnostic", headers={"Authorization": "Bearer admin-token"})
    resp_two = client.post("/ops/writer/diagnostic", headers={"Authorization": "Bearer admin-token"})
    assert resp_one.status_code == resp_two.status_code == 200
    hashes = [json.loads(line)["idempotence_hash"] for line in sink if json.loads(line)["idempotence_hash"]]
    assert len(hashes) >= 2
    assert hashes[-1] == hashes[-2]


def test_diagnostic_writer_ignores_conditionals(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "If-None-Match": '"abc"',
            "If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT",
        },
    )
    assert resp.status_code == 200


def test_diagnostic_writer_rejects_wrong_content_type(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "Content-Type": "text/plain",
        },
        data="hello",
    )
    assert resp.status_code == 415
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.data == b'{"code":"invalid_content_type","error":"expected application/json; charset=utf-8","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_rejects_malformed_json(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "Content-Type": "application/json; charset=utf-8",
        },
        data=b"{\n",
    )
    assert resp.status_code == 400
    assert resp.data == b'{"code":"invalid_json","error":"malformed JSON request","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_rejects_unknown_keys(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={"extra": True},
    )
    assert resp.status_code == 422
    assert resp.data == b'{"code":"unknown_key","error":"unknown request key","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_enforces_size_cap(client):
    big_body = b"{" + b"a" * (_MAX_WRITER_BYTES + 1) + b"}"
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "Content-Type": "application/json; charset=utf-8",
        },
        data=big_body,
    )
    assert resp.status_code == 413
    assert resp.data == b'{"code":"request_too_large","error":"request body exceeds 32 KiB","ok":false,"schema":"v1"}\n'


def test_diagnostic_writer_rejects_non_object(client):
    resp = client.post(
        "/ops/writer/diagnostic",
        headers={
            "Authorization": "Bearer admin-token",
            "Content-Type": "application/json; charset=utf-8",
        },
        data="[]",
    )
    assert resp.status_code == 422
    assert resp.data == b'{"code":"invalid_input","error":"schema validation failed","ok":false,"schema":"v1"}\n'
