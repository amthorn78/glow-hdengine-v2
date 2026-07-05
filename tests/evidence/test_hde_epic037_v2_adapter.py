from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import generate_hde_epic037_v2_adapter as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED = [
    VENDOR_DIR / "hde_epic037_adapter_mapping.snapshot.json",
    VENDOR_DIR / "hde_epic037_adapter_negative_fixtures.json",
    VENDOR_DIR / "hde_epic037_public_reader_no_change.json",
    VENDOR_DIR / "hde_epic037_no_raw_payload_persistence.json",
]


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    payload = json.loads(raw.decode("utf-8"))
    assert raw == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    return payload


def test_generator_outputs_are_canonical_epic037_pr02_scoped() -> None:
    outputs = generator.build_outputs("2026-07-05T00:00:00Z")
    assert set(REQUIRED) <= set(outputs)
    for path in REQUIRED:
        payload = json.loads(outputs[path].decode("utf-8"))
        assert payload["epic_id"] == "HDE-EPIC037"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.8"
        assert outputs[path] == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"


def test_adapter_mapping_evidence_is_context_backed_and_non_wired() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_adapter_mapping.snapshot.json")
    assert payload["mapping_result"]["status"] == "mapped"
    assert payload["mapping_result"]["resolved"]["person_uid"] == "person-epic037-pr02"
    assert payload["mapping_result"]["cache"]["payload_posture"] == "adapter_mapped_no_raw_vendor_payload"
    assert "resolver wiring" in payload["nonclaims"]
    assert payload["adapter_purity"] == {"database_io": False, "environment_reads": False, "file_io": False, "network_io": False, "randomness": False, "time_reads": False, "vendor_fetch": False}


def test_negative_fixtures_cover_fail_closed_cases() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_adapter_negative_fixtures.json")
    fixtures = {row["fixture_id"]: row["result"] for row in payload["fixtures"]}
    expected = {"missing_internal_identity_context", "missing_vendor_detail_fields", "chart_simple_result_detail_insufficient", "malformed_payload", "missing_data", "unsupported_payload_family", "wrong_route_family", "wrong_route"}
    assert expected <= set(fixtures)
    assert all(row["status"] == "unsupported" for row in fixtures.values())
    assert fixtures["missing_internal_identity_context"]["code"] == "ADAPTER_CONTEXT_INSUFFICIENT"
    assert fixtures["chart_simple_result_detail_insufficient"]["code"] == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"


def test_public_reader_and_runtime_nonclaims_preserved() -> None:
    public = _assert_canonical_json(VENDOR_DIR / "hde_epic037_public_reader_no_change.json")
    assert public["public_reader_change_claim"] == "NONE"
    assert public["new_http_home_claim"] == "NONE"
    no_raw = _assert_canonical_json(VENDOR_DIR / "hde_epic037_no_raw_payload_persistence.json")
    assert no_raw["adapter_calls_ingest_vendor_bodygraph"] is False
    assert no_raw["adapter_persists_raw_vendor_payload"] is False
    for token in ["VENDOR_NO_PAYLOAD_LOGGING_OK", "LOGS_KEYS_ONLY_OK", "BG_PRIVACY_REDACTION_OK"]:
        assert token in no_raw["tokens_not_claimed"]


def test_index_registration_has_pr02_without_unsupported_privacy_tokens() -> None:
    from tools.evidence import update_evidence_index as updater

    keys = {entry["artifact_key"] for entry in updater.EPIC037_PR02_PRIMARY_ARTIFACTS}
    assert "hdapi_v2.hde_epic037_adapter_mapping" in keys
    for entry in updater.EPIC037_PR02_PRIMARY_ARTIFACTS:
        assert "VENDOR_NO_PAYLOAD_LOGGING_OK" not in entry["tokens"]
        assert "LOGS_KEYS_ONLY_OK" not in entry["tokens"]
        assert "BG_PRIVACY_REDACTION_OK" not in entry["tokens"]
