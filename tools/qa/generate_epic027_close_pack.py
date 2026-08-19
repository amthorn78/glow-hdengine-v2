#!/usr/bin/env python3
"""Thin, read-only-by-default EPIC027 adapter.

The checked-in EPIC027 evidence family is historical. This module retains
only locator configuration, a pure run-free close-manifest payload, and an
explicit disjoint-repository adapter to the generic viability harness. It
does not execute gates or own any evidence writer, proof writer, index update,
QA receipt, close-report, or manifest publication.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC027"
EPIC_SLUG = "hde-epic027"


def _mapping(
    name: str,
    evidence_titles: tuple[str, ...],
    ci_tests_jobs: str,
    qa_root_logs: str,
) -> dict[str, object]:
    """Describe one retained locator relationship without making a status claim."""

    return {
        "name": name,
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_titles": evidence_titles,
        "ci_tests_jobs": ci_tests_jobs,
        "qa_root_logs": qa_root_logs,
    }


TOKEN_EVIDENCE_MAPPINGS: tuple[dict[str, object], ...] = (
    _mapping(
        "COMPOSITE_ABBA_IDENTITY_OK",
        (
            "artifacts/compat/identity_hash.txt",
            "artifacts/compat/AB.json",
            "artifacts/compat/BA.json",
        ),
        "python tools/evidence/generate_conjunction_writer_evidence.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "TWO_RUN_IDENTITY_OK",
        (
            "artifacts/audit/cli/two_run_identity.log",
            "artifacts/writer/conjunction_write_readback.log",
            "artifacts/writer/conjunction_writer_summary.json",
        ),
        "python tools/evidence/generate_conjunction_writer_evidence.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "CLI_READER_PARITY_OK",
        (
            "artifacts/cli/reader_dump.json",
            "artifacts/cli/reader_cli_parity.bytes",
        ),
        "python -m pytest tests/http/test_reader_a7_transport.py::test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "A7_GET_QUOTED_ETAG_OK",
        ("artifacts/proofs/success_get.txt",),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "A7_HEAD_PARITY_OK",
        (
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_get.txt",
        ),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "A7_304_OMITS_CT_CL_OK",
        ("artifacts/proofs/success_304.txt",),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "A7_VARY_AUTH_AE_OK",
        (
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
        ),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "A7_ENCODING_INVARIANCE_OK",
        (
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_304.txt",
            "artifacts/proofs/success_encoding_invariance.txt",
        ),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "ENDPOINTS_CATALOG_OK",
        (
            "docs/ENDPOINTS_CATALOG.json",
            "docs/ENDPOINTS_CATALOG.json.sha256",
        ),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "ENDPOINTS_CATALOG_ENV_GATE_OK",
        (
            "docs/ENDPOINTS_CATALOG.json",
            "artifacts/proofs/endpoints_env_gate_proof.log",
        ),
        "python tools/qa/generate_epic027_close_pack.py",
        "acceptance_map_viability.log",
    ),
    _mapping(
        "ENV_RAILS_POLICY_OK",
        ("audit/gates/determinism/env_pins.log",),
        "ci/checks/check_env_pins.sh",
        "checks/gate_mirror_schema/primary.log",
    ),
    _mapping(
        "EVIDENCE_INDEX_UPDATED_OK",
        ("docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"),
        "python tools/evidence/update_evidence_index.py",
        "checks/gate_update_evidence_index_write/primary.log",
    ),
    _mapping(
        "EVIDENCE_INDEX_HASH_OK",
        ("docs/evidence/INDEX.sha256",),
        "python tools/evidence/update_evidence_index.py --check",
        "checks/gate_update_evidence_index_check/primary.log",
    ),
    _mapping(
        "EVIDENCE_INDEX_MIRROR_OK",
        ("docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"),
        "ci/checks/check_mirror_schema.sh",
        "checks/gate_mirror_schema/primary.log",
    ),
    _mapping(
        "EVIDENCE_PATHS_VALIDATED_OK",
        ("docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"),
        "python tools/evidence/validate_evidence_paths.py",
        "checks/gate_evidence_paths_validation/primary.log",
    ),
    _mapping(
        "CI_CHECK_MIRROR_SCHEMA_OK",
        ("docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"),
        "ci/checks/check_mirror_schema.sh",
        "checks/gate_mirror_schema/primary.log",
    ),
    _mapping(
        "CI_CHECK_FINAL_LF_OK",
        (
            "docs/acceptance_map_epic027.json",
            "audit/qa/hde-epic027/token_evidence_matrix.md",
        ),
        "python tools/evidence/check_lf_endings.py",
        "checks/gate_lf_endings/primary.log",
    ),
)

HISTORICAL_GATE_RECEIPTS: tuple[str, ...] = tuple(
    f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log"
    for check_id in (
        "gate_update_evidence_index_write",
        "gate_orientation_demo_write",
        "gate_update_evidence_index_check",
        "gate_orientation_demo_check",
        "gate_evidence_paths_validation",
        "gate_lf_endings",
        "gate_mirror_schema",
    )
)

CLOSE_KEY_OUTPUTS: dict[str, str] = {
    "acceptance_map": "docs/acceptance_map_epic027.json",
    "token_matrix": "audit/qa/hde-epic027/token_evidence_matrix.md",
    "acceptance_viability": "audit/qa/hde-epic027/acceptance_map_viability.log",
    "step_logs_manifest": "audit/qa/hde-epic027/qa_step_logs_manifest.json",
    "doc_deltas": "audit/qa/hde-epic027/00_meta/doc_deltas.md",
    "close_report": "audit/EPIC-027_close_report.md",
    "close_manifest": "audit/EPIC-027_MANIFEST.json",
    "d1_compat_identity_hash": "artifacts/compat/identity_hash.txt",
    "d3_endpoints_catalog": "docs/ENDPOINTS_CATALOG.json",
    "d3_success_get": "artifacts/proofs/success_get.txt",
    "d3_success_head": "artifacts/proofs/success_head.txt",
    "d3_success_304": "artifacts/proofs/success_304.txt",
    "d4_writer_readback": "artifacts/writer/conjunction_write_readback.log",
    "d4_writer_summary": "artifacts/writer/conjunction_writer_summary.json",
    "index_human": "docs/evidence/INDEX.json",
    "index_human_sha256": "docs/evidence/INDEX.sha256",
    "index_mirror": "artifacts/evidence_index.jsonl",
    "index_mirror_sha256": "artifacts/evidence_index.jsonl.sha256",
    **{
        f"qa_log_{Path(receipt).parent.name}": receipt
        for receipt in HISTORICAL_GATE_RECEIPTS
    },
}


def viability_config(*, repo_root: Path | None = None) -> qa_harness.HarnessConfig:
    """Return generic viability configuration for an explicit isolated repository."""

    if repo_root is None:
        raise ValueError("EPIC027 viability requires an explicit isolated repo_root")
    config = qa_harness.HarnessConfig(EPIC_ID, repo_root=repo_root)
    qa_harness.require_disjoint_repository_root(
        config.repo_root,
        protected_root=ROOT,
    )
    return config


def run_viability(*, repo_root: Path | None = None) -> qa_harness.ViabilityResult:
    """Delegate isolated viability publication to the generic harness."""

    config = viability_config(repo_root=repo_root)
    ensure_determinism_env()
    result = qa_harness.generate_acceptance_map_viability(
        config,
        publish_governed_ledger=True,
    )
    qa_harness.require_governed_viability(result, config.viability_ledger_path)
    return result


def close_manifest_payload(captured_at_utc: str) -> dict[str, object]:
    """Delegate run-free manifest construction to the generic harness."""

    return qa_harness.run_free_close_manifest_payload(
        EPIC_ID,
        captured_at_utc,
        CLOSE_KEY_OUTPUTS,
    )


def main() -> int:
    """Verify frozen evidence without executing QA or publishing artifacts."""

    try:
        ensure_determinism_env()
        qa_harness.require_frozen_evidence(ROOT)
    except (DeterminismEnvError, OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
