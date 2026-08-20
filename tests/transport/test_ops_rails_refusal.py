from __future__ import annotations

import json

import pytest

from adapter.wsgi import create_app


def _build_app(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.delenv("ALLOW_NETWORK", raising=False)
    monkeypatch.setenv("APP_ENV", "dev")
    app = create_app()
    app.config.update(TESTING=True, LOG_SINK=[])
    return app


def test_ops_rails_refusal_get(monkeypatch):
    app = _build_app(monkeypatch)
    client = app.test_client()

    resp = client.get("/ops/rails/refusal")

    assert resp.status_code == 503
    assert resp.data.decode("utf-8") == (
        '{"schema":"v1","ok":false,"code":"ERR_WRITER_RAILS_CLOSED","error":"rails are closed"}\n'
    )
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    assert resp.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp.headers
    assert "Content-Encoding" not in resp.headers
    assert "Vary" not in resp.headers

    assert len(app.config["LOG_SINK"]) == 1
    log_line = json.loads(app.config["LOG_SINK"][0])
    assert log_line["route"] == "ops.rails.refusal"
    assert log_line["status"] == 503
    # Canonical keys-only schema:
    assert set(log_line.keys()) == {
        "at",
        "route",
        "status",
        "duration_ms",
        "idempotence_hash",
        "release_id",
    }


def test_ops_rails_refusal_post(monkeypatch):
    app = _build_app(monkeypatch)
    client = app.test_client()

    resp = client.post("/ops/rails/refusal")

    assert resp.status_code == 503
    assert resp.data.decode("utf-8") == (
        '{"schema":"v1","ok":false,"code":"ERR_WRITER_RAILS_CLOSED","error":"rails are closed"}\n'
    )
    assert len(app.config["LOG_SINK"]) == 1
    log_line = json.loads(app.config["LOG_SINK"][0])
    assert log_line["route"] == "ops.rails.refusal"


@pytest.mark.parametrize(
    ("probe_token", "expected_present"),
    ((None, False), ("probe-token-must-not-leak", True)),
)
def test_ops_probe_env_reports_closed_process_posture(
    monkeypatch, probe_token, expected_present
):
    if probe_token is None:
        monkeypatch.delenv("RESTART_PROBE_TOKEN", raising=False)
    else:
        monkeypatch.setenv("RESTART_PROBE_TOKEN", probe_token)
    app = _build_app(monkeypatch)
    client = app.test_client()

    response = client.get("/ops/probe/env")

    assert response.status_code == 200
    payload = json.loads(response.data)
    assert set(payload) == {
        "pid",
        "started_at_utc",
        "rails_state",
        "probe_token_present",
    }
    assert isinstance(payload["pid"], int)
    assert payload["pid"] > 0
    assert payload["started_at_utc"].endswith("Z")
    assert payload["rails_state"] == {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "unset",
        "APP_ENV": "dev",
    }
    assert payload["probe_token_present"] is expected_present
    assert response.headers["Cache-Control"] == "no-store"
    assert "ETag" not in response.headers

    assert len(app.config["LOG_SINK"]) == 1
    log_line = json.loads(app.config["LOG_SINK"][0])
    assert log_line["route"] == "ops.probe.env"
    assert log_line["status"] == 200
    if probe_token is not None:
        assert probe_token.encode("utf-8") not in response.data
        assert probe_token not in "".join(app.config["LOG_SINK"])
