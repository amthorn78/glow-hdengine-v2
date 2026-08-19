#!/usr/bin/env python3
"""Thin, read-only-by-default EPIC029 close-pack adapter.

The checked-in EPIC029 QA, closeout, proof, and OPS families are historical.
This module retains only status-free locator configuration, a pure run-free
manifest payload, and an explicit disjoint-repository adapter to the generic
viability harness.  It never parses historical receipts as current results,
executes Live QA, recommends PF09 movement, or publishes evidence.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC029"
EPIC_SLUG = "hde-epic029"


def _mapping(
    name: str,
    owner_pf: str,
    evidence_titles: tuple[str, ...],
    ci_tests_jobs: str,
) -> dict[str, object]:
    """Describe one retained locator relationship without claiming status."""

    return {
        "name": name,
        "owner_pf": owner_pf,
        "evidence_titles": evidence_titles,
        "ci_tests_jobs": ci_tests_jobs,
        "qa_root_logs": "acceptance_map_viability.log",
    }


TOKEN_EVIDENCE_MAPPINGS: tuple[dict[str, object], ...] = (
    _mapping(
        "DOC_DELTA_PRESENT_OK",
        "PF04 — HDE Governance §2.0.0",
        (
            "audit/docdeltas/hde-epic029_doc_deltas.md",
            "audit/docdeltas/hde-epic029_drain_targets.md",
        ),
        "read-only historical evidence",
    ),
    _mapping(
        "EVIDENCE_INDEX_UPDATED_OK",
        "PF12 — Schemas & Artifacts §Evidence Index",
        ("docs/evidence/INDEX.json",),
        "python tools/evidence/update_evidence_index.py --check",
    ),
    _mapping(
        "MACHINE_MIRROR_UPDATED_OK",
        "PF12 — Schemas & Artifacts §Evidence Mirror",
        ("artifacts/evidence_index.jsonl",),
        "ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl",
    ),
    _mapping(
        "EVIDENCE_INDEX_HASH_OK",
        "PF12 — Schemas & Artifacts §Evidence Hash Discipline",
        (
            "docs/evidence/INDEX.sha256",
            "artifacts/evidence_index.jsonl",
        ),
        "python tools/evidence/update_evidence_index.py --check",
    ),
    _mapping(
        "ENV_RAILS_POLICY_OK",
        "PF10 — HDE Build Notes §Closed Rails",
        ("audit/gates/determinism/env_pins.log",),
        "ci/checks/check_env_pins.sh",
    ),
    _mapping(
        "JSON_CANONICAL_CHECK_OK",
        "PF10 — HDE Build Notes §Canonical JSON Gate",
        (
            "audit/gates/json_gate/canonical/json_gate_structured_record.json",
            "audit/gates/canonical_json/json_canonical_check.log",
        ),
        "python tools/evidence/run_canonical_json_gate.py --check-only",
    ),
    _mapping(
        "TESTS_PASS_OK",
        "PF19 — Glow QA Guide §QA Rails",
        (
            "audit/qa/hde-epic029/checks/"
            "po-epic-close-live-qa/primary.log",
        ),
        "read-only historical receipt; no execution",
    ),
    _mapping(
        "QA_PRECOMMIT_CHECKLIST_OK",
        "PF19 — Glow QA Guide §QA Rails",
        ("audit/qa/hde-epic029/checks/po-precommit/primary.log",),
        "read-only historical receipt; no execution",
    ),
    _mapping(
        "QA_POSTCOMMIT_CHECKLIST_OK",
        "PF19 — Glow QA Guide §QA Rails",
        ("audit/qa/hde-epic029/checks/po-postcommit/primary.log",),
        "read-only historical receipt; no execution",
    ),
)

HISTORICAL_QA_RECEIPTS: dict[str, str] = {
    "po-epic-close-live-qa": (
        f"audit/qa/{EPIC_SLUG}/checks/po-epic-close-live-qa/primary.log"
    ),
    "po-precommit": f"audit/qa/{EPIC_SLUG}/checks/po-precommit/primary.log",
    "po-postcommit": f"audit/qa/{EPIC_SLUG}/checks/po-postcommit/primary.log",
}

CLOSE_KEY_OUTPUTS: dict[str, str] = {
    "acceptance_map": "docs/acceptance_map_epic029.json",
    "token_matrix": f"audit/qa/{EPIC_SLUG}/token_evidence_matrix.md",
    "acceptance_viability": (
        f"audit/qa/{EPIC_SLUG}/acceptance_map_viability.log"
    ),
    "step_logs_manifest": f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json",
    "conjunction_json_surface_inventory": (
        f"audit/qa/{EPIC_SLUG}/00_meta/conjunction_json_surface_inventory.md"
    ),
    "dev_harness_binding_coverage": (
        f"audit/qa/{EPIC_SLUG}/00_meta/dev_harness_binding_coverage.md"
    ),
    "doc_deltas": "audit/docdeltas/hde-epic029_doc_deltas.md",
    "drain_targets": "audit/docdeltas/hde-epic029_drain_targets.md",
    "close_report": "audit/EPIC-029_close_report.md",
    "close_manifest": "audit/EPIC-029_MANIFEST.json",
    "ops_commands": f"audit/ops/{EPIC_SLUG}/ops-01/commands.txt",
    "ops_stdout": f"audit/ops/{EPIC_SLUG}/ops-01/stdout.log",
    "ops_stderr": f"audit/ops/{EPIC_SLUG}/ops-01/stderr.log",
    "ops_exit_codes": f"audit/ops/{EPIC_SLUG}/ops-01/exit_codes.txt",
    "ops_codespaces_dev_sampler_url": (
        f"audit/ops/{EPIC_SLUG}/ops-01/codespaces_dev_sampler_url.md"
    ),
    "ops_local_dev_sampler_url": (
        f"audit/ops/{EPIC_SLUG}/ops-01/local_dev_sampler_url.md"
    ),
    "ops_binding_disposition": (
        f"audit/ops/{EPIC_SLUG}/ops-01/binding_disposition.md"
    ),
    "ops_created_files_sha256": (
        f"audit/ops/{EPIC_SLUG}/ops-01/created_files_sha256.txt"
    ),
    **{
        f"historical_qa_receipt_{check_id}": path
        for check_id, path in HISTORICAL_QA_RECEIPTS.items()
    },
}


def viability_config(*, repo_root: Path | None = None) -> qa_harness.HarnessConfig:
    """Return generic viability configuration for an explicit isolated repo."""

    if repo_root is None:
        raise ValueError("EPIC029 viability requires an explicit isolated repo_root")
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
    """Verify frozen evidence without executing QA or generating a close pack."""

    try:
        ensure_determinism_env()
        qa_harness.require_frozen_evidence(ROOT)
    except (DeterminismEnvError, OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
