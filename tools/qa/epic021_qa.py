"""Thin HDE-EPIC021 wrapper over the current-state QA harness."""

from __future__ import annotations

import sys
from pathlib import Path

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa.qa_harness import (
    HarnessConfig,
    Status,
    generate_acceptance_map_viability,
    record_check,
    run_pytest_check,
)

EPIC_ID = "HDE-EPIC021"
BOOTSTRAP_CHECK_ID = "D00_bootstrap"
BOOTSTRAP_TEST = "tests/qa/test_epic021_scaffolding.py"


def run_epic021_qa(*, repo_root: Path | None = None) -> dict[str, object]:
    """Execute only EPIC021's concrete bootstrap and viability definitions."""
    config = HarnessConfig(EPIC_ID, repo_root=repo_root)
    bootstrap = run_pytest_check(
        config,
        BOOTSTRAP_CHECK_ID,
        ("-q", BOOTSTRAP_TEST),
        check_name="EPIC021 tooling bootstrap",
    )
    bootstrap_log, manifest = record_check(config, bootstrap)
    viability = generate_acceptance_map_viability(config)
    return {
        "bootstrap": bootstrap,
        "bootstrap_log": bootstrap_log,
        "manifest": manifest,
        "viability": viability,
    }


def main() -> int:
    try:
        ensure_determinism_env()
        results = run_epic021_qa()
    except (DeterminismEnvError, OSError, ValueError, RuntimeError) as exc:
        sys.stderr.write(f"EPIC021_QA_TOOLING_ERROR: {exc}\n")
        return 1
    return 0 if results["bootstrap"].status is Status.PASS and results["viability"].status is Status.PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
