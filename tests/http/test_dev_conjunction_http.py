import json

from adapter.http_reader import create_app


def _client(monkeypatch, app_env: str):
    monkeypatch.setenv("APP_ENV", app_env)
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_dev_conjunction_endpoints_gate_in_prod(monkeypatch):
    client = _client(monkeypatch, "prod")

    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction"):
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

    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction"):
        resp = client.get(route, query_string={"a_user_id": "left", "b_user_id": "right"})
        assert resp.status_code == 503
        payload = json.loads(resp.data)
        assert payload["code"] == "ERR_WRITER_RAILS_CLOSED"
        assert payload["details"]["rails"] == {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}


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
    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction"):
        resp = client.get(route, query_string=query)
        assert resp.status_code == 200
        payload = json.loads(resp.data)
        assert "conjunction" in payload
        assert payload["conjunction"]["left"]["person_uid"]
        assert payload["conjunction"]["right"]["person_uid"]
