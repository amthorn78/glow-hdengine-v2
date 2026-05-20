from __future__ import annotations

from tools.evidence import generate_db_bridge_parity as mod


def test_nondev_failure_payload_uses_stage_and_records_attempt_order() -> None:
    payload = mod._nondev_total_failure_payload()

    assert payload["environment"] == "stage"
    assert payload["selection_order"] == ["psycopg", "bridge"]
    assert payload["selection_attempts"] == [
        {"provider": "psycopg", "status": "skip", "reason": "missing_database_url"},
        {"provider": "bridge", "status": "skip", "reason": "missing_bridge_url"},
    ]
    assert payload["total_failure"]["typed_error"] == {
        "class": "BridgeUnavailable",
        "code": "missing_bridge_url",
    }
