from __future__ import annotations

import json

from engine.ops import http_log


def test_log_http_call_keys_only(tmp_path, monkeypatch):
    log_path = tmp_path / "sample.jsonl"
    monkeypatch.setattr(http_log, "LOG_PATH", log_path)

    http_log.log_http_call(
        route="db_bridge.get:/health",
        status=200,
        duration_ms=12.3456,
        release_id="rel-123",
        idempotence_hash="idh-456",
    )

    raw = log_path.read_text(encoding="utf-8").splitlines()
    assert len(raw) == 1
    record = json.loads(raw[0])
    assert record["route"] == "db_bridge.get:/health"
    assert record["status"] == 200
    assert set(record) <= {"at", "route", "status", "duration_ms", "release_id", "idempotence_hash"}
    assert isinstance(record["duration_ms"], float)
    assert record["duration_ms"] == round(record["duration_ms"], 3)
