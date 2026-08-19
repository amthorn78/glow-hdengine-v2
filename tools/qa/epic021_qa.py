"""Thin HDE-EPIC021 adapter over the generic current-state QA harness.

The checked-in EPIC021 evidence family is historical and read-only.  The
callable adapter therefore requires an explicit, disjoint temporary repository;
the command-line entry point performs only frozen-evidence verification.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC021"
BOOTSTRAP_CHECK_ID = "d00-bootstrap"
LEGACY_BOOTSTRAP_CHECK_ID = "D00_bootstrap"
BOOTSTRAP_TEST = "tests/qa/test_epic021_scaffolding.py"


def run_epic021_qa(*, repo_root: Path | None = None) -> dict[str, object]:
    """Run the thin adapter only inside an explicit isolated repository."""

    if repo_root is None:
        raise ValueError("EPIC021 QA requires an explicit isolated repo_root")
    config = qa_harness.HarnessConfig(
        EPIC_ID,
        repo_root=repo_root,
        step_names=(BOOTSTRAP_CHECK_ID,),
    )
    qa_harness.require_disjoint_repository_root(
        config.repo_root,
        protected_root=ROOT,
    )
    ensure_determinism_env()
    bootstrap = qa_harness.run_pytest_check(
        config,
        BOOTSTRAP_CHECK_ID,
        ("-q", BOOTSTRAP_TEST),
        check_name="EPIC021 tooling bootstrap",
    )
    bootstrap_log, manifest = qa_harness.record_check(
        config,
        bootstrap,
        supersede_check_ids=(LEGACY_BOOTSTRAP_CHECK_ID,),
    )
    viability = qa_harness.generate_acceptance_map_viability(
        config,
        publish_governed_ledger=True,
    )
    governed_ledger = qa_harness.require_governed_viability(
        viability,
        config.viability_ledger_path,
    )
    return {
        "bootstrap": bootstrap,
        "bootstrap_log": bootstrap_log,
        "manifest": manifest,
        "viability": viability,
        "governed_ledger": governed_ledger,
    }


def main() -> int:
    """Verify the frozen family without executing QA or publishing evidence."""

    try:
        ensure_determinism_env()
        qa_harness.require_frozen_evidence(ROOT)
    except (DeterminismEnvError, OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
