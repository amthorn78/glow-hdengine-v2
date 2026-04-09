import json

from adapter.http_reader import create_app


def _client(monkeypatch, app_env: str):
    monkeypatch.setenv("APP_ENV", app_env)
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_dev_conjunction_endpoints_gate_in_prod(monkeypatch):
    client = _client(monkeypatch, "prod")

    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string={"a_user_id": "left", "b_user_id": "right"})
        assert resp.status_code == 403
        assert json.loads(resp.data) == {
            "schema": "v1",
            "ok": False,
            "code": "ERR_WRITER_FORBIDDEN",
            "error": "insufficient scope",
        }


def test_dev_conjunction_endpoints_closed_rails_refusal(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    client = _client(monkeypatch, "dev")

    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string={"a_user_id": "left", "b_user_id": "right"})
        assert resp.status_code == 503
        payload = json.loads(resp.data)
        assert payload["code"] == "ERR_WRITER_RAILS_CLOSED"
        assert payload["details"]["rails"] == {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
        if route == "/dev/writer/conjunction":
            assert payload["type"] == "dev.writer.conjunction.error.v1"


def test_dev_conjunction_endpoints_open_rails_success(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    client = _client(monkeypatch, "dev")

    query = {
        "a_user_id": "left",
        "b_user_id": "right",
        "a_birthdate": "1990-01-01",
        "a_birthtime": "08:30",
        "a_location": "Amsterdam",
        "b_birthdate": "1991-02-02",
        "b_birthtime": "09:45",
        "b_location": "Berlin",
    }
    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string=query)
        assert resp.status_code == 200
        payload = json.loads(resp.data)
        conjunction_payload = payload.get("result", payload)
        assert "conjunction" in conjunction_payload
        assert conjunction_payload["conjunction"]["left"]["person_uid"]
        assert conjunction_payload["conjunction"]["right"]["person_uid"]


def test_dev_writer_conjunction_is_idempotent_bytes(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    client = _client(monkeypatch, "dev")

    query = {
        "a_user_id": "left",
        "b_user_id": "right",
        "a_birthdate": "1990-01-01",
        "a_birthtime": "08:30",
        "a_location": "Amsterdam",
        "b_birthdate": "1991-02-02",
        "b_birthtime": "09:45",
        "b_location": "Berlin",
    }

    resp_one = client.get("/dev/writer/conjunction", query_string=query)
    resp_two = client.get("/dev/writer/conjunction", query_string=query)

    assert resp_one.status_code == 200
    assert resp_two.status_code == 200
    assert resp_one.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp_one.headers
    assert resp_one.data == resp_two.data

    payload_one = json.loads(resp_one.data)
    payload_two = json.loads(resp_two.data)
    assert payload_one["schema"] == "v1"
    assert payload_one["type"] == "dev.writer.conjunction.success.v1"
    assert payload_one["writer"] == payload_two["writer"]
    assert payload_one["writer"]["writer_route_id"] == "dev.writer.conjunction.v1"
    assert payload_one["writer"]["idempotence_hash"]


def test_dev_writer_conjunction_invalid_input_uses_typed_error(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    client = _client(monkeypatch, "dev")

    resp = client.get("/dev/writer/conjunction", query_string={"a_user_id": "left"})
    assert resp.status_code == 422
    assert resp.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp.headers
    payload = json.loads(resp.data)
    assert payload["schema"] == "v1"
    assert payload["ok"] is False
    assert payload["code"] == "ERR_WRITER_INVALID_INPUT"
    assert payload["type"] == "dev.writer.conjunction.error.v1"
