from __future__ import annotations

import json
import os
import subprocess

import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACCEPTANCE_MAP = ROOT / "docs/acceptance_map_epic037.json"
TOKEN_MATRIX = ROOT / "audit/qa/hde-epic037/token_evidence_matrix.md"
OPS_ROOT = ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001"
MIRROR = ROOT / "artifacts/evidence_index.jsonl"
INDEX = ROOT / "docs/evidence/INDEX.json"

ALLOWED_TOKENS = {
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_INDEX_MIRROR_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "JSON_CANONICAL_CHECK_OK",
    "COMPOSITE_ABBA_IDENTITY_OK",
    "TWO_RUN_IDENTITY_OK",
    "NO_EXTERNAL_IO_ON_REFUSAL_OK",
    "ENV_RAILS_POLICY_OK",
}

EXPECTED_SUBTASKS = {
    "HDE-FERM008.7",
    "HDE-FERM008.8",
    "HDE-FERM008.9",
    "HDE-FERM008.10",
    "HDE-FERM008.11",
    "HDE-FERM008.12",
}

EXPECTED_INDEX_PATHS = {
    "docs/acceptance_map_epic037.json",
    "audit/qa/hde-epic037/token_evidence_matrix.md",
    "audit/qa/hde-epic037/acceptance_map_viability.log",
    "audit/qa/hde-epic037/parent_evidence_binding.log",
    "audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md",
    "audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md",
    "audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log",
    "audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json",
}


def _canonical_json(path: Path) -> object:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    payload = json.loads(raw)
    assert raw == (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return payload


def test_acceptance_map_binds_parent_evidence_and_nonclaims() -> None:
    payload = _canonical_json(ACCEPTANCE_MAP)
    assert payload["epic_id"] == "HDE-EPIC037"
    assert payload["pf09_task_id"] == "HDE-FERM008"
    assert payload["pf09_subtask_id"] == "HDE-FERM008.12"
    assert set(payload["pf09_subtasks_bound"]) == EXPECTED_SUBTASKS
    assert payload["parent_posture"] == "supportable_to_done"
    assert "later-drain support statement only" in payload["parent_posture_scope"]
    for nonclaim in [
        "QA PASS",
        "OPS completion by PR work",
        "PF09 status movement",
        "PF09 status drainage",
        "PF-Canon edit",
        "epic closeout",
        "production deployment",
        "public Reader change",
        "public route",
        "public flag",
        "new HTTP home",
        "app-side HumanDesignAPI ownership",
        "AI scope",
    ]:
        assert nonclaim in payload["nonclaims"]
    for family in [
        "pr01_hde_ferm008_7",
        "pr02_hde_ferm008_8",
        "pr03_hde_ferm008_9",
        "pr04_hde_ferm008_10",
        "ops01_hde_ferm008_11_po_produced",
        "pr05_hde_ferm008_12_parent_binding",
    ]:
        for rel in payload["evidence_families"][family]:
            assert (ROOT / rel).exists(), rel


def test_token_matrix_uses_registered_supported_subset() -> None:
    text = TOKEN_MATRIX.read_text(encoding="utf-8")
    claimed = {
        line.split("|", 3)[1].strip()
        for line in text.splitlines()
        if line.startswith("| ") and not line.startswith("| ---") and "Token" not in line.split("|", 3)[1]
    }
    assert claimed == ALLOWED_TOKENS
    assert "TESTS_PASS_OK" not in claimed
    assert "LOGS_KEYS_ONLY_OK" not in claimed
    assert "BG_PRIVACY_REDACTION_OK" not in claimed
    assert "VENDOR_NO_PAYLOAD_LOGGING_OK" not in claimed


def test_ops01_runtime_posture_is_secret_safe_before_registration() -> None:
    stdout = json.loads((OPS_ROOT / "stdout.log").read_text(encoding="utf-8"))
    assert stdout["status"] == "ok"
    assert stdout["adapter"] == {"code": "ADAPTER_MAPPED", "payload_family": "ChartResult", "status": "mapped"}
    request = stdout["resolver"]["request"]
    assert request["route"] == "vendor.hdapi.post:/charts"
    assert request["configured_base_url"] == "<redacted>"
    assert request["raw_body_emitted"] is False
    assert request["raw_response_body_emitted"] is False
    assert "bg_resolve_exit_code=0" in (OPS_ROOT / "exit_codes.txt").read_text(encoding="utf-8")
    result = json.loads((OPS_ROOT / "result_summary.json").read_text(encoding="utf-8"))
    assert result["runtime_conformance_supported_by_this_smoke"] is True
    adapter = json.loads((OPS_ROOT / "adapter_mapping_result_summary.json").read_text(encoding="utf-8"))
    assert adapter["raw_vendor_payload_recorded"] is False
    assert all(adapter["mapped_shape"][key] is True for key in ["resolved_bodygraph_present", "resolved_person_present", "cache_input_fingerprint_present"])
    compat = json.loads((OPS_ROOT / "compat_path_result_summary.json").read_text(encoding="utf-8"))
    assert compat["compat_path_status"] == "accepted"
    assert compat["category_count"] == 10
    request_summary = json.loads((OPS_ROOT / "request_summary.json").read_text(encoding="utf-8"))
    assert request_summary["secret_policy"]["plaintext_secret_recorded"] is False
    assert request_summary["secret_policy"]["raw_request_body_recorded"] is False
    assert request_summary["secret_policy"]["raw_response_body_recorded"] is False
    assert request_summary["secret_policy"]["uncontrolled_raw_vendor_payload_recorded"] is False
    failure = json.loads((OPS_ROOT / "failure_classification.json").read_text(encoding="utf-8"))
    assert failure["classification"] == "not_applicable_success"
    combined = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in [*OPS_ROOT.iterdir(), ROOT / "audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md"] if path.is_file())
    assert "Bearer <redacted>" in combined
    assert "HD-Geocode-Key: <redacted>" in combined
    assert "raw_response_body_emitted\":true" not in combined
    assert "raw_body_emitted\":true" not in combined


def test_pr05_and_ops01_records_are_indexed_mirrored_and_path_proofed() -> None:
    index_entries = json.loads(INDEX.read_text(encoding="utf-8"))
    index_paths = {entry["discovered_physical_path"] for entry in index_entries}
    mirror_records = [json.loads(line) for line in MIRROR.read_text(encoding="utf-8").splitlines()]
    mirror_by_path = {record["discovered_physical_path"]: record for record in mirror_records}
    for rel in EXPECTED_INDEX_PATHS:
        assert rel in index_paths
        record = mirror_by_path[rel]
        assert record["epic_id"] == "HDE-EPIC037"
        assert record["sha256"]
        assert record["size_bytes"] == (ROOT / rel).stat().st_size
        assert record["proof_anchor"] == f"{rel}.path_proof.txt"
        assert (ROOT / record["proof_anchor"]).exists()


def _review_base_ref() -> str | None:
    candidates = []
    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        candidates.extend([f"origin/{base_ref}", base_ref])
    candidates.extend(["origin/main", "main", "HEAD^"])
    for candidate in candidates:
        result = subprocess.run(
            ["git", "merge-base", "HEAD", candidate],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    return None


def test_pr05_did_not_edit_pfcanon() -> None:
    base = _review_base_ref()
    if base is None:
        pytest.skip("git review base unavailable in shallow checkout")
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD", "--", "docs/pfcanon"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        pytest.skip(f"git diff review base unavailable: {result.stderr.strip()}")
    assert result.stdout.strip() == ""


def test_parent_binding_generator_reproduces_governed_artifacts() -> None:
    result = subprocess.run(
        ["python", "tools/evidence/generate_hde_epic037_parent_binding.py", "--check"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    assert "checked HDE-EPIC037 PR-05 parent-binding artifacts" in result.stdout
