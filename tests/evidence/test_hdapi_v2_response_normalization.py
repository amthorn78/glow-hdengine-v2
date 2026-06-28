from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from tools.evidence import generate_hdapi_v2_response_normalization as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED = [
    VENDOR_DIR / "response_mapping.snapshot.json",
    VENDOR_DIR / "release_binding.snapshot.json",
]


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    assert not raw.startswith(b"\xef\xbb\xbf")
    payload = json.loads(raw.decode("utf-8"))
    assert raw == json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    return payload


def _load_path_proof(path: Path) -> dict[str, str]:
    proof = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            proof[key] = value
    return proof


def _parse_utc(raw: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    assert parsed.tzinfo == dt.timezone.utc
    assert parsed.microsecond == 0
    return parsed


def test_pr02_generator_outputs_are_canonical_hde035_ferm0084_gap_scoped() -> None:
    outputs = generator.render_outputs(produced_at="2026-06-28T09:00:00Z")
    assert set(outputs) == set(REQUIRED)
    for body in outputs.values():
        assert body.endswith(b"\n")
        assert not body.endswith(b"\n\n")
        payload = json.loads(body.decode("utf-8"))
        assert payload["epic_id"] == "HDE-EPIC035"
        assert payload["pf09_document"] == "PF09.5 — HDE Build Checklist Fermentation"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["generated_at_utc"] == "2026-06-28T09:00:00Z"
        rendered = body.decode("utf-8")
        for forbidden in ["Bearer redacted", "HD-Api-Key: redacted", "k_test", "api-key", "geo-key"]:
            assert forbidden not in rendered


def test_response_mapping_records_exact_schema_adapter_gap_without_inference() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    assert payload["pf09_subtask_id"] == "HDE-FERM008.4"
    assert payload["artifact_kind"] == "hdapi_v2_response_normalization_gap"
    assert payload["response_normalization_posture"] == "EXACT_SCHEMA_ADAPTER_GAP_RECORDED"
    assert payload["schema_gap_status"] == "GAP_RECORDED"
    assert payload["normalized_data_path_proof_claim"] == "NONE"
    assert payload["no_compatibility_by_inference"] is True
    assert payload["data_payload_body_emitted"] is False
    gap = payload["adapter_schema_gap"]
    assert "no ChartResult/ChartSimpleResult-to-BodyGraph adapter" in gap["bodygraph_boundary"]
    assert "person_uid" in gap["compat_boundary"]
    assert "not proven" in gap["cache_boundary"]
    assert payload["no_claims"]["full_hdapi_v2_runtime_conformance"] == "NONE"
    assert payload["no_claims"]["public_reader_change"] == "NONE"
    assert payload["no_claims"]["app_side_humandesignapi_call_path"] == "NONE"
    assert payload["no_claims"]["raw_vendor_payload_persisted"] == "NONE"
    assert payload["no_claims"]["hde_ferm008_5_closure"] == "NONE"
    assert payload["live_vendor_call_claim"] == "NONE"
    assert "no AI interpretation" in payload["no_ai_transformation_posture"]


def test_response_mapping_preserves_route_family_identity_and_secret_safe_auth_posture() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    routes = payload["route_family_identity"]
    assert routes["version_neutral_runtime_resource_paths"] == ["bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates"]
    assert {row["resource_path"] for row in routes["legacy_v1_bodygraph_routes"]} == {"bodygraphs", "bodygraphs/simple"}
    assert {row["auth_header_posture"] for row in routes["legacy_v1_bodygraph_routes"]} == {"HD-Api-Key: <redacted>"}
    by_path = {row["endpoint_path"]: row for row in routes["v2_chart_routes"]}
    assert by_path["/v2/charts"]["data_schema"] == "ChartResult"
    assert by_path["/v2/charts/simple"]["data_schema"] == "ChartSimpleResult"
    assert by_path["/v2/charts/coordinates"]["data_schema"] == "ChartResult"
    assert {row["auth_header_posture"] for row in by_path.values()} == {"Authorization: Bearer <redacted>"}


def test_release_binding_distinguishes_pr01_pr02_and_follow_up_without_overclaiming() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "release_binding.snapshot.json")
    bindings = payload["pr_evidence_bindings"]
    assert bindings["pr01_hde_ferm008_3_provider_outcome"]["subtask_id"] == "HDE-FERM008.3"
    assert bindings["pr02_hde_ferm008_4_response_normalization"]["subtask_id"] == "HDE-FERM008.4"
    assert bindings["follow_up_hde_ferm008_5_evidence_loop_closure"]["posture"] == "FOLLOW_UP_NOT_CLAIMED_BY_PR02"
    assert bindings["pr02_hde_ferm008_4_response_normalization"]["schema_gap_status"] == "GAP_RECORDED"
    assert bindings["pr02_hde_ferm008_4_response_normalization"]["normalized_data_path_proof_claim"] == "NONE"
    assert payload["no_claims"]["full_hdapi_v2_runtime_conformance"] == "NONE"
    assert payload["no_claims"]["new_http_home"] == "NONE"
    assert payload["no_claims"]["public_route_flag_payload_or_transport_change"] == "NONE"
    assert "without claiming full HumanDesignAPI v2 runtime conformance" in payload["release_binding_posture"]


def test_pr02_index_mirror_path_proof_bindings_when_promoted() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    mirror = [json.loads(line) for line in (ROOT / "artifacts" / "evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    index_by_path = {entry["discovered_physical_path"]: entry for entry in index}
    mirror_by_path = {entry["discovered_physical_path"]: entry for entry in mirror}
    for path in REQUIRED:
        rel = path.relative_to(ROOT).as_posix()
        assert rel in index_by_path
        assert rel in mirror_by_path
        assert index_by_path[rel]["epic_id"] == "HDE-EPIC035"
        assert mirror_by_path[rel]["epic_id"] == "HDE-EPIC035"
        proof = ROOT / f"{rel}.path_proof.txt"
        assert proof.exists()
        proof_data = _load_path_proof(proof)
        assert proof_data["path"] == rel
        assert len(proof_data["sha256"]) == 64
        assert _parse_utc(proof_data["produced_at_utc"]) >= _parse_utc(proof_data["mtime_utc"])


def test_pr02_index_mirror_do_not_retain_conflicting_epic034_response_mapping_row() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    mirror = [json.loads(line) for line in (ROOT / "artifacts" / "evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    conflicting = {
        (entry.get("artifact_key"), entry.get("discovered_physical_path"), entry.get("epic_id"))
        for entry in [*index, *mirror]
        if entry.get("discovered_physical_path") == "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    }
    assert ("hdapi_v2.response_mapping", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json", "HDE-EPIC034") not in conflicting
    assert ("hdapi_v2.response_mapping_pr02", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json", "HDE-EPIC035") in conflicting


def test_route_rows_fail_closed_on_required_schema_drift() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    drifted = json.loads(json.dumps(contract))
    for route in drifted["route_families"]:
        if route.get("path") == "/v2/charts/coordinates":
            route["success_envelope"] = "StandardResponse with type=Unexpected and data=Unexpected"
    try:
        generator._route_rows(drifted)
    except ValueError as exc:
        assert "HDAPI_V2_RESPONSE_NORMALIZATION_ENVELOPE_DRIFT:/v2/charts/coordinates" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("route schema drift did not fail closed")


def test_index_retains_epic034_pr03_check_log_when_pr02_snapshot_is_promoted() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    by_path = {entry["discovered_physical_path"]: entry for entry in index}
    entry = by_path["audit/qa/hde-epic034/pr-03/response_mapping_check.log"]
    assert entry["artifact_key"] == "epic034.pr03.response_mapping_check"
    assert entry["epic_id"] == "HDE-EPIC034"


def test_pr02_loader_fails_closed_on_release_binding_sha_drift(tmp_path, monkeypatch) -> None:
    from tools.evidence import update_evidence_index as updater

    vendor = tmp_path / "artifacts" / "vendor" / "hdapi_v2"
    vendor.mkdir(parents=True)
    snapshot = vendor / "response_mapping.snapshot.json"
    snapshot_payload = {
        "artifact_kind": "hdapi_v2_response_normalization_gap",
        "epic_id": "HDE-EPIC035",
        "generated_at_utc": "2026-06-28T09:00:00Z",
        "pf09_task_id": "HDE-FERM008",
        "pf09_subtask_id": "HDE-FERM008.4",
        "response_normalization_posture": "EXACT_SCHEMA_ADAPTER_GAP_RECORDED",
        "schema_gap_status": "GAP_RECORDED",
    }
    snapshot.write_text(json.dumps(snapshot_payload, sort_keys=True) + "\n", encoding="utf-8")
    release = vendor / "release_binding.snapshot.json"
    release.write_text(json.dumps({
        "artifact_kind": "hdapi_v2_release_binding",
        "epic_id": "HDE-EPIC035",
        "pf09_task_id": "HDE-FERM008",
        "pr_evidence_bindings": {
            "pr02_hde_ferm008_4_response_normalization": {
                "artifacts": [{"path": "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json", "sha256": "0" * 64}],
                "subtask_id": "HDE-FERM008.4",
            }
        },
    }, sort_keys=True) + "\n", encoding="utf-8")
    monkeypatch.setattr(updater, "ROOT", tmp_path)
    try:
        updater._load_epic035_pr02_entries()
    except SystemExit as exc:
        assert str(exc) == "INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE"
    else:  # pragma: no cover
        raise AssertionError("release binding SHA drift did not fail closed")
