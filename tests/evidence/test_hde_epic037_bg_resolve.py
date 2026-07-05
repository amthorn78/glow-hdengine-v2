from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import generate_hde_epic037_bg_resolve as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED = [
    VENDOR_DIR / "hde_epic037_bg_resolve_v2_route_policy.snapshot.json",
    VENDOR_DIR / "hde_epic037_bg_resolve_request_shape.snapshot.json",
    VENDOR_DIR / "hde_epic037_bg_resolve_closed_rails_no_io.json",
    VENDOR_DIR / "hde_epic037_bg_resolve_legacy_fallback.snapshot.json",
]


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    payload = json.loads(raw.decode("utf-8"))
    assert raw == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    return payload


def test_generator_outputs_are_canonical_epic037_pr03_scoped() -> None:
    outputs = generator.build_outputs("2026-07-05T00:00:00Z")
    assert set(REQUIRED) <= set(outputs)
    for path in REQUIRED:
        payload = json.loads(outputs[path].decode("utf-8"))
        assert payload["epic_id"] == "HDE-EPIC037"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.9"
        assert outputs[path] == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"


def test_route_policy_evidence_selects_adapter_backed_v2_charts() -> None:
    payload = _assert_canonical_json(REQUIRED[0])
    policy = payload["route_policy"]
    assert policy["classification"] == "adapter_backed_v2_chart"
    assert policy["resource_path"] == "charts"
    assert policy["route_family"] == "recommended_v2_chart"
    assert policy["route_auth_posture"] == "Authorization: Bearer <redacted>"
    assert payload["resolver_adapter_code"] == "ADAPTER_MAPPED"
    assert payload["raw_vendor_payload_body_emitted"] is False


def test_request_shape_evidence_preserves_base_and_auth_boundaries() -> None:
    payload = _assert_canonical_json(REQUIRED[1])
    request = payload["request"]
    assert payload["version_owner"] == "HD_API_BASE_URL"
    assert request["url"] == "https://vendor.test/prefix/v2/charts"
    assert request["resource_path"] == "charts"
    assert request["no_double_version_prefix"] is True
    assert request["does_not_construct_legacy_bodygraphs_for_v2"] is True
    assert request["auth_header_posture"] == "Authorization: Bearer <redacted>"
    assert request["geocode_header_posture"] == "HD-Geocode-Key: <redacted>"
    assert payload["raw_request_body_emitted"] is False
    assert payload["raw_response_body_emitted"] is False


def test_closed_rails_no_io_and_legacy_fallback_evidence() -> None:
    closed = _assert_canonical_json(REQUIRED[2])
    assert closed["closed_rails_result"]["error"]["code"] == "PROVIDER_REFUSED"
    assert all(value is False for value in closed["no_io_before_refusal"].values())
    legacy = _assert_canonical_json(REQUIRED[3])
    assert legacy["legacy_policy"]["classification"] == "explicit_legacy_fallback"
    assert legacy["legacy_request"]["resource_path"] == "bodygraphs"
    assert legacy["legacy_request"]["auth_header_posture"] == "HD-Api-Key: <redacted>"
    assert legacy["v2_legacy_bodygraphs_request_supported"] is False


def test_index_registration_has_pr03_without_unsupported_privacy_tokens() -> None:
    from tools.evidence import update_evidence_index as updater

    keys = {entry["artifact_key"] for entry in updater.EPIC037_PR03_PRIMARY_ARTIFACTS}
    assert "hdapi_v2.hde_epic037_bg_resolve_v2_route_policy" in keys
    for entry in updater.EPIC037_PR03_PRIMARY_ARTIFACTS:
        assert "VENDOR_NO_PAYLOAD_LOGGING_OK" not in entry["tokens"]
        assert "LOGS_KEYS_ONLY_OK" not in entry["tokens"]
        assert "BG_PRIVACY_REDACTION_OK" not in entry["tokens"]
