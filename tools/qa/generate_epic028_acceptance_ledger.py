#!/usr/bin/env python3
"""Thin, read-only-by-default EPIC028 acceptance-ledger adapter.

The checked-in EPIC028 acceptance and QA artifacts are historical.  This
module retains only the corrected locator relationships and an explicit
disjoint-repository adapter to the generic viability harness.  It does not
own acceptance-map, token-matrix, proof, index, receipt, or manifest writes.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC028"
EPIC_SLUG = "hde-epic028"


def _mapping(
    name: str,
    evidence_titles: tuple[str, ...],
    ci_tests_jobs: str,
) -> dict[str, object]:
    """Describe one retained locator relationship without claiming status."""

    return {
        "name": name,
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_titles": evidence_titles,
        "ci_tests_jobs": ci_tests_jobs,
        "qa_root_logs": "acceptance_map_viability.log",
    }


TOKEN_EVIDENCE_MAPPINGS: tuple[dict[str, object], ...] = (
    _mapping(
        "A7_GET_QUOTED_ETAG_OK",
        ("artifacts/proofs/success_get.txt",),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "A7_HEAD_PARITY_OK",
        (
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_get.txt",
        ),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "A7_304_OMITS_CT_CL_OK",
        ("artifacts/proofs/success_304.txt",),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "A7_VARY_AUTH_AE_OK",
        (
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
        ),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "A7_ENCODING_INVARIANCE_OK",
        ("artifacts/proofs/success_encoding_invariance.txt",),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "ENDPOINTS_CATALOG_OK",
        (
            "docs/ENDPOINTS_CATALOG.json",
            "docs/ENDPOINTS_CATALOG.json.sha256",
        ),
        "python -m pytest -q tests/http/test_endpoint_catalog.py",
    ),
    _mapping(
        "ENDPOINTS_CATALOG_ENV_GATE_OK",
        (
            "docs/ENDPOINTS_CATALOG.json",
            "artifacts/proofs/endpoints_env_gate_proof.log",
        ),
        (
            "python -m pytest -q tests/http/test_endpoint_catalog.py "
            "tests/http/test_reader_a7_transport.py"
        ),
    ),
    _mapping(
        "READER_200_CTYPE_JSON_UTF8_OK",
        ("artifacts/proofs/success_get.txt",),
        "python -m pytest -q tests/http/test_reader_a7_transport.py",
    ),
    _mapping(
        "PREFS_KEYSET_10_OK",
        (
            "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log",
            "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
        ),
        (
            "python -m pytest -q "
            "tests/unit/test_viewer_prefs_normalization.py::"
            "test_viewer_prefs_require_exact_magic10_weight_keys"
        ),
    ),
)


def viability_config(*, repo_root: Path | None = None) -> qa_harness.HarnessConfig:
    """Return generic viability configuration for an explicit isolated repo."""

    if repo_root is None:
        raise ValueError("EPIC028 viability requires an explicit isolated repo_root")
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


def main() -> int:
    """Verify frozen evidence without generating an acceptance ledger."""

    try:
        ensure_determinism_env()
        qa_harness.require_frozen_evidence(ROOT)
    except (DeterminismEnvError, OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
