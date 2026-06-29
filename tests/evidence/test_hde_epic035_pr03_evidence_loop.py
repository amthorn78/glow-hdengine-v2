from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.evidence.update_evidence_index import (
    ROOT as INDEX_ROOT,
    _epic035_ops01_v2_stdout_is_valid,
    _load_epic035_ops01_checksum_ledger,
    _validate_epic035_ops01_checksums,
)

ROOT = Path(__file__).resolve().parents[2]
ACCEPTANCE = ROOT / "docs/acceptance_map_epic035.json"
MATRIX = ROOT / "audit/qa/hde-epic035/token_evidence_matrix.md"
VIABILITY = ROOT / "audit/qa/hde-epic035/acceptance_map_viability.log"
BINDING = ROOT / "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"
HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
MIRROR = ROOT / "artifacts/evidence_index.jsonl"

ALLOWED_TOKENS = {
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "JSON_CANONICAL_CHECK_OK",
    "TESTS_PASS_OK",
}
REQUIRED_OPS_PATHS = [
    "audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt",
    "audit/ops/hde-epic035/ops-01/files_sha256.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json",
    "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json",
]


def _acceptance_payload() -> dict:
    raw = ACCEPTANCE.read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    assert raw == json.dumps(json.loads(raw), sort_keys=True, separators=(",", ":")).encode() + b"\n"
    return json.loads(raw)


def _mirror_rows() -> list[dict]:
    return [json.loads(line) for line in MIRROR.read_text(encoding="utf-8").splitlines() if line]


def test_acceptance_map_uses_only_allowed_tokens_and_nonclaims() -> None:
    payload = _acceptance_payload()
    assert payload["epic_id"] == "HDE-EPIC035"
    names = {item["name"] for item in payload["tokens"]}
    assert names <= ALLOWED_TOKENS
    joined = json.dumps(payload, sort_keys=True)
    assert "VENDOR_V2" not in joined and "HDAPI_V2_OK" not in joined
    for nonclaim in [
        "QA PASS",
        "OPS completion",
        "PF09 status movement",
        "HDE-FERM008 parent Done",
        "epic closeout",
        "full HumanDesignAPI v2 runtime conformance",
        "public Reader change",
        "raw payload persistence",
        "AI scope",
    ]:
        assert nonclaim in payload["nonclaims"]


def test_ops01_paths_and_binding_preserve_success_gap_distinction() -> None:
    payload = _acceptance_payload()
    for rel in REQUIRED_OPS_PATHS:
        assert rel in payload["referenced_evidence_paths"]
        assert (ROOT / rel).exists()
    stdout = (ROOT / "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log").read_text()
    stdout_payload = json.loads(stdout)
    assert stdout_payload["authorization_header_shape"] == "Authorization: Bearer <redacted>"
    assert stdout_payload["hd_geocode_key_header_shape"] == "HD-Geocode-Key: <redacted>"
    assert stdout_payload["has_authorization"] is True
    assert stdout_payload["has_hd_geocode_key"] is True
    assert stdout_payload["legacy_hd_api_key_on_v2_path"] is False
    assert stdout_payload["has_hd_api_key"] is False
    assert stdout_payload["raw_request_body_persisted"] is False
    assert stdout_payload["raw_response_body_persisted"] is False
    assert stdout_payload["raw_secret_persisted"] is False
    assert stdout_payload["raw_vendor_payload_persisted"] is False
    final = (ROOT / "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt").read_text()
    assert "v2_charts_simple=success" in final
    assert "bg_resolve_http_status=404" in final
    assert "runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base" in final
    binding = BINDING.read_text(encoding="utf-8")
    assert "bg_resolve_runtime_gap=" in binding
    assert "ops_completion_claim=false" in binding


def test_epic035_rows_are_indexed_mirrored_and_path_proven() -> None:
    index = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    rows = _mirror_rows()
    index_by_path = {entry["discovered_physical_path"]: entry for entry in index}
    mirror_by_path = {entry["discovered_physical_path"]: entry for entry in rows}
    required = {
        "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json",
        "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
        "docs/acceptance_map_epic035.json",
        "audit/qa/hde-epic035/token_evidence_matrix.md",
        "audit/qa/hde-epic035/acceptance_map_viability.log",
        "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log",
        *REQUIRED_OPS_PATHS,
    }
    assert required <= set(index_by_path)
    assert required <= set(mirror_by_path)
    for rel in required:
        expected_sha = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert mirror_by_path[rel]["sha256"] == expected_sha
        proof = ROOT / f"{rel}.path_proof.txt"
        assert proof.exists()
        proof_text = proof.read_text(encoding="utf-8")
        assert f"path: {rel}" in proof_text
        assert f"sha256: {expected_sha}" in proof_text


def test_human_index_machine_mirror_parity_for_epic035() -> None:
    index = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    mirror = _mirror_rows()
    assert len(index) == len(mirror)
    for human, machine in zip(index, mirror, strict=True):
        assert human["artifact_key"] == machine["artifact_key"]
        assert human["discovered_physical_path"] == machine["discovered_physical_path"]
        if "sha256" in human:
            assert human["sha256"] == machine["sha256"]


def test_boundary_logs_are_not_closeout_or_runbooks() -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for path in [MATRIX, VIABILITY, BINDING])
    assert "Live QA runbook" in text or "live_qa_runbook=false" in text
    assert "closeout_review=false" in text
    assert "ops_completion_claim=false" in text
    assert "pf09_status_movement_claim=false" in text
    assert "full_runtime_conformance_claim=false" in text


def test_epic035_stdout_guard_rejects_legacy_hd_api_key_regression() -> None:
    payload = json.loads((ROOT / "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log").read_text())
    assert _epic035_ops01_v2_stdout_is_valid(payload) is True
    payload["legacy_hd_api_key_on_v2_path"] = True
    assert _epic035_ops01_v2_stdout_is_valid(payload) is False
    payload["legacy_hd_api_key_on_v2_path"] = False
    payload["has_hd_api_key"] = True
    assert _epic035_ops01_v2_stdout_is_valid(payload) is False


def test_epic035_ops01_checksum_ledger_matches_promoted_retained_files() -> None:
    ledger_path = ROOT / "audit/ops/hde-epic035/ops-01/files_sha256.txt"
    ledger = _load_epic035_ops01_checksum_ledger(ledger_path)
    for rel in REQUIRED_OPS_PATHS:
        if not rel.startswith("audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/"):
            continue
        assert rel in ledger
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == ledger[rel]
    assert INDEX_ROOT == ROOT
    _validate_epic035_ops01_checksums()
