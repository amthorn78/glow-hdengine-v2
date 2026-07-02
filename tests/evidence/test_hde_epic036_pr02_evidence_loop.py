from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACCEPTANCE = ROOT / "docs/acceptance_map_epic036.json"
MATRIX = ROOT / "audit/qa/hde-epic036/token_evidence_matrix.md"
VIABILITY = ROOT / "audit/qa/hde-epic036/acceptance_map_viability.log"
HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
MIRROR = ROOT / "artifacts/evidence_index.jsonl"

ALLOWED_TOKENS = {
    "TESTS_PASS_OK",
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "JSON_CANONICAL_CHECK_OK",
    "NO_EXTERNAL_IO_ON_REFUSAL_OK",
    "ENV_RAILS_POLICY_OK",
}
PR01_PATHS = {
    "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt",
    "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt",
    "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt",
    "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt",
    "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt",
    "audit/qa/hde-epic036/route_policy_decision.log",
    "audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt",
}
PR02_PATHS = {
    "docs/acceptance_map_epic036.json",
    "audit/qa/hde-epic036/token_evidence_matrix.md",
    "audit/qa/hde-epic036/acceptance_map_viability.log",
    "audit/docdeltas/hde-epic036_doc_deltas.md",
    "audit/qa/hde-epic036/00_meta/doc_deltas.md",
}
REQUIRED_NONCLAIMS = {
    "QA PASS",
    "OPS completion",
    "PF09 status movement",
    "HDE-FERM008 parent Done",
    "epic closeout",
    "full HumanDesignAPI v2 runtime conformance",
    "public Reader change",
    "public route",
    "public flag",
    "public payload or transport change",
    "new HTTP home",
    "app-side HumanDesignAPI credential ownership",
    "raw payload persistence",
    "AI scope",
}
FORBIDDEN_TEXT = [
    "qa_pass_claim=true",
    "ops_completion_claim=true",
    "pf09_status_movement_claim=true",
    "epic_closeout_claim=true",
    "full_runtime_conformance_claim=true",
    "public_reader_change_claim=true",
    "public_route_claim=true",
    "raw_payload_persistence_claim=true",
    "ai_scope_claim=true",
]


def _acceptance_payload() -> dict:
    raw = ACCEPTANCE.read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    assert raw == json.dumps(json.loads(raw), sort_keys=True, separators=(",", ":")).encode() + b"\n"
    return json.loads(raw)


def _mirror_rows() -> list[dict]:
    return [json.loads(line) for line in MIRROR.read_text(encoding="utf-8").splitlines() if line]


def test_acceptance_map_is_canonical_and_uses_approved_tokens_only() -> None:
    payload = _acceptance_payload()
    assert payload["epic_id"] == "HDE-EPIC036"
    assert payload["selected_route_policy_classification"] == "unsupported_runtime_nonclaim"
    names = {item["name"] for item in payload["tokens"]}
    assert names == ALLOWED_TOKENS
    joined = json.dumps(payload, sort_keys=True)
    assert "VENDOR_V2" not in joined
    assert "HDAPI_V2_OK" not in joined
    assert payload["vendor_v2_specific_acceptance_tokens"] == "NONE"
    assert REQUIRED_NONCLAIMS <= set(payload["nonclaims"])


def test_pr01_route_policy_evidence_is_referenced_and_exists() -> None:
    payload = _acceptance_payload()
    referenced = set(payload["referenced_evidence_paths"])
    assert PR01_PATHS <= referenced
    for rel in PR01_PATHS:
        assert (ROOT / rel).exists(), rel
    decision = (ROOT / "audit/qa/hde-epic036/route_policy_decision.log").read_text(encoding="utf-8")
    assert "selected_route_policy_classification=unsupported_runtime_nonclaim" in decision
    assert "OPS-01 not required by PR-01" in decision


def test_pr02_artifacts_are_indexed_mirrored_and_path_proven() -> None:
    index = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    rows = _mirror_rows()
    index_by_path = {entry["discovered_physical_path"]: entry for entry in index}
    mirror_by_path = {entry["discovered_physical_path"]: entry for entry in rows}
    assert PR02_PATHS <= set(index_by_path)
    assert PR02_PATHS <= set(mirror_by_path)
    for rel in PR02_PATHS:
        expected_sha = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert mirror_by_path[rel]["sha256"] == expected_sha
        proof = ROOT / f"{rel}.path_proof.txt"
        assert proof.exists()
        proof_text = proof.read_text(encoding="utf-8")
        assert f"path: {rel}" in proof_text
        assert f"sha256: {expected_sha}" in proof_text


def test_human_index_machine_mirror_parity_remains_coherent() -> None:
    index = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    mirror = _mirror_rows()
    assert len(index) == len(mirror)
    for human, machine in zip(index, mirror, strict=True):
        assert human["artifact_key"] == machine["artifact_key"]
        assert human["discovered_physical_path"] == machine["discovered_physical_path"]
        if "sha256" in human:
            assert human["sha256"] == machine["sha256"]


def test_ops01_not_claimed_without_actual_epic036_ops_evidence() -> None:
    payload = _acceptance_payload()
    ops_dir = ROOT / "audit/ops/hde-epic036/ops-01"
    ops_files = sorted(p for p in ops_dir.rglob("*") if p.is_file()) if ops_dir.exists() else []
    if not ops_files:
        assert payload["ops_01"]["executed_for_pr02"] is False
        assert payload["ops_01"]["actual_ops01_evidence_found"] is False
        text = MATRIX.read_text(encoding="utf-8") + VIABILITY.read_text(encoding="utf-8")
        assert "ops_01_executed_for_pr02=false" in text
        assert "ops_completion_claim=false" in text


def test_pr02_surfaces_preserve_no_claim_boundaries() -> None:
    text = "\n".join(
        (ROOT / rel).read_text(encoding="utf-8")
        for rel in PR02_PATHS
        if rel.endswith((".md", ".log", ".json"))
    )
    for forbidden in FORBIDDEN_TEXT:
        assert forbidden not in text
    assert "PF-Canon was not edited" in text
    assert "full HumanDesignAPI v2 runtime conformance" in text
    assert "raw payload persistence" in text
