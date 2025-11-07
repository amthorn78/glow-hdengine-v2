from __future__ import annotations

import json

from adapter.wsgi import create_app


def _build_app(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.delenv("ALLOW_NETWORK", raising=False)
    app = create_app()
    app.config.update(TESTING=True, LOG_SINK=[])
    return app


def test_ops_rails_refusal_get(monkeypatch):
    app = _build_app(monkeypatch)
    client = app.test_client()

    resp = client.get("/ops/rails/refusal")

    assert resp.status_code == 503
    assert resp.data.decode("utf-8") == (
        '{"schema":"v1","ok":false,"code":"rails_closed","error":"rails are closed"}\n'
    )
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    assert resp.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp.headers
    assert "Content-Encoding" not in resp.headers
    assert "Vary" not in resp.headers

    assert len(app.config["LOG_SINK"]) == 1
    log_line = json.loads(app.config["LOG_SINK"][0])
    assert log_line["route"] == "ops.rails.refusal"
    assert log_line["rails_state"] == "closed"
    assert log_line["status"] == 503
    assert set(log_line.keys()) == {"at", "route", "status", "duration_ms", "rails_state"}


def test_ops_rails_refusal_post(monkeypatch):
    app = _build_app(monkeypatch)
    client = app.test_client()

    resp = client.post("/ops/rails/refusal")

    assert resp.status_code == 503
    assert resp.data.decode("utf-8") == (
        '{"schema":"v1","ok":false,"code":"rails_closed","error":"rails are closed"}\n'
    )
    assert len(app.config["LOG_SINK"]) == 1
    log_line = json.loads(app.config["LOG_SINK"][0])
    assert log_line["route"] == "ops.rails.refusal"
    assert log_line["rails_state"] == "closed"
