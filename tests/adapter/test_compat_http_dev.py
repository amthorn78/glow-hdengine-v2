import json

from adapter.http_reader import create_app


def _dev_client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_dev_compat_malformed_json_returns_compat_envelope():
    client = _dev_client()
    resp = client.post(
        "/api/compat/v1",
        data=b"{bad: json",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert 400 <= resp.status_code < 500
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"

    body_bytes = resp.data
    assert body_bytes.endswith(b"\n")

    payload = json.loads(body_bytes.decode("utf-8"))
    assert payload.get("ok") is False
    assert isinstance(payload.get("code"), str)
    assert isinstance(payload.get("error"), str)
    assert "<html" not in body_bytes.decode("utf-8").lower()
