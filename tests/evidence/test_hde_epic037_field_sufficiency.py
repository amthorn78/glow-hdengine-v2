from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import generate_hde_epic037_field_sufficiency as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED = [
    VENDOR_DIR / "hde_epic037_field_sufficiency_proof.json",
    VENDOR_DIR / "hde_epic037_adapter_contract.snapshot.json",
    VENDOR_DIR / "hde_epic037_adapter_contract_nonclaims.json",
]


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    payload = json.loads(raw.decode("utf-8"))
    assert raw == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    return payload


def test_generator_outputs_are_canonical_epic037_scoped() -> None:
    outputs = generator.build_outputs("2026-07-04T00:00:00Z")
    for path in REQUIRED:
        assert path in outputs
    for body in (outputs[path] for path in REQUIRED):
        payload = json.loads(body.decode("utf-8"))
        assert payload["epic_id"] == "HDE-EPIC037"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.7"
        assert payload["generated_at_utc"] == "2026-07-04T00:00:00Z"
        assert body == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
        rendered = body.decode("utf-8")
        for forbidden in ["k_test", "api-key", "geo-key", "Bearer redacted", "HD-Api-Key: redacted"]:
            assert forbidden not in rendered


def test_field_sufficiency_records_typed_insufficient_fail_closed_result() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_field_sufficiency_proof.json")
    assert payload["selected_payload_family"] == "typed_insufficient_classification"
    assert payload["field_sufficiency_status"] == "INSUFFICIENT_FAIL_CLOSED"
    assert payload["v2_chart_data_feeds_existing_bodygraph_person_cache_compat_contract"] is False
    assert payload["adapter_compatibility_proof"]["runtime_adapter_implemented"] is False
    assert payload["adapter_compatibility_proof"]["resolver_rewired"] is False
    assert payload["adapter_compatibility_proof"]["compat_compute_ready"] is False
    assert payload["no_raw_vendor_payload_body_persisted_in_evidence"] is True
    assert payload["candidate_evaluations"]["ChartResult"]["compute_ready"] is False
    assert payload["candidate_evaluations"]["ChartSimpleResult"]["fail_closed"] is True


def test_adapter_contract_defines_internal_person_cache_compat_fields() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_adapter_contract.snapshot.json")
    fields = {(row["contract_area"], row["internal_field"]): row for row in payload["internal_contract"]}
    assert ("person", "person_uid") in fields
    assert ("cache", "hde.body_graphs.user_id") in fields
    assert ("cache", "hde.body_graphs.payload") in fields
    assert ("compat", "left.person_uid and right.person_uid") in fields
    assert fields[("person", "person_uid")]["status"] == "unsupported_vendor_field"
    assert fields[("cache", "hde.body_graphs.payload")]["status"] == "schema_change_or_adapter_required"
    assert payload["selected_payload_family"] == "typed_insufficient_classification"
    assert payload["schema_changes_required"]


def test_negative_fixtures_cover_missing_and_insufficient_vendor_fields() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_field_sufficiency_proof.json")
    fixtures = {item["fixture_id"]: item for item in payload["negative_fixtures"]}
    assert fixtures["chart_result_missing_person_uid"]["expected_classification"] == "FAIL_CLOSED_UNSUPPORTED_FIELD"
    assert "person_uid" in fixtures["chart_result_missing_person_uid"]["missing_internal_fields"]
    simple = fixtures["chart_simple_missing_person_uid_and_activations"]
    assert simple["expected_classification"] == "FAIL_CLOSED_INSUFFICIENT_SCHEMA"
    assert {"person_uid", "activations", "birthDateUtc"} <= set(simple["missing_internal_fields"])


def test_nonclaims_preserve_no_public_runtime_ai_or_vendor_claims() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_adapter_contract_nonclaims.json")
    no_claims = payload["no_claims"]
    assert no_claims["public_reader_change"] == "NONE"
    assert no_claims["new_http_home"] == "NONE"
    assert no_claims["app_side_humandesignapi_call_path"] == "NONE"
    assert no_claims["live_vendor_call"] == "NONE"
    assert no_claims["ai_llm_model_call_behavior"] == "NONE"
    assert no_claims["full_hdapi_v2_runtime_conformance"] == "NONE"
    assert payload["no_compatibility_by_inference"] is True


def test_evaluate_payload_family_fails_closed_for_unknown_family() -> None:
    result = generator.evaluate_payload_family("Unexpected", {"type"})
    assert result["classification"] == "UNSUPPORTED_PAYLOAD_FAMILY"
    assert result["field_sufficiency"] == "INSUFFICIENT"
    assert result["compute_ready"] is False
    assert result["fail_closed"] is True


def test_index_registration_does_not_claim_unproduced_log_or_privacy_tokens() -> None:
    from tools.evidence import update_evidence_index as updater

    nonclaims = next(
        entry
        for entry in updater.EPIC037_PR01_PRIMARY_ARTIFACTS
        if entry["artifact_key"] == "hdapi_v2.hde_epic037_adapter_contract_nonclaims"
    )
    assert "VENDOR_NO_PAYLOAD_LOGGING_OK" in nonclaims["tokens"]
    assert "LOGS_KEYS_ONLY_OK" not in nonclaims["tokens"]
    assert "BG_PRIVACY_REDACTION_OK" not in nonclaims["tokens"]
