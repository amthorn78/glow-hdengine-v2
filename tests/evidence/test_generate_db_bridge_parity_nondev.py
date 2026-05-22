from __future__ import annotations

import pytest

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


def test_provider_parity_payload_preserves_non_token_labels_and_unavailable_status() -> None:
    db = mod.DBAccess(mod.HarnessProvider("bridge"), attempts=[{"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"}, {"provider": "bridge", "status": "ok"}])
    payload = mod._provider_parity_payload(db)

    assert payload["live_provider_parity"]["parity_status"] == "unavailable"
    assert payload["live_provider_parity"]["direct_provider_rows"] == "unavailable"
    assert all(case["parity"] == "skip" for case in payload["capabilities"])
    labels = {row["name"]: row for row in payload["proof_labels"]}
    assert labels["DB_PROVIDER_PARITY_OK"]["type"] == "non_token"
    assert labels["DB_PROVIDER_PARITY_OK"]["status"] == "not_claimed"
    assert labels["DB_BRIDGE_CAPS_OK"]["type"] == "non_token"


def test_selection_order_contract_requires_structural_field_and_attempt_derivation() -> None:
    payload = {"attempts": [{"provider": "psycopg", "status": "error"}, {"provider": "bridge", "status": "ok"}]}
    out = mod._ensure_structural_selection_order(payload)
    assert out["selection_order"] == ["psycopg", "bridge"]

    with pytest.raises(SystemExit, match="SELECTION_ORDER_NOT_ARRAY"):
        mod._ensure_structural_selection_order({"attempts": payload["attempts"], "selection_order": "psycopg"})

    with pytest.raises(SystemExit, match="SELECTION_ORDER_MISMATCH"):
        mod._ensure_structural_selection_order({"attempts": payload["attempts"], "selection_order": ["bridge", "psycopg"]})
