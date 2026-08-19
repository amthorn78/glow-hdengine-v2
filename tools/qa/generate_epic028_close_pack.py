#!/usr/bin/env python3
"""Thin, read-only-by-default EPIC028 close-manifest adapter.

The EPIC028 close pack, QA receipts, proofs, and OPS checksum family are
historical.  This module exposes only pure manifest-shape helpers and a frozen
evidence check.  It does not read those receipts, infer status from them, or
write any governed artifact.
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

CLOSE_KEY_OUTPUTS: dict[str, str] = {
    "acceptance_map": "docs/acceptance_map_epic028.json",
    "token_matrix": f"audit/qa/{EPIC_SLUG}/token_evidence_matrix.md",
    "acceptance_map_viability": (
        f"audit/qa/{EPIC_SLUG}/acceptance_map_viability.log"
    ),
    "qa_step_manifest": f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json",
    "qa_step_manifest_path_proof": (
        f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json.path_proof.txt"
    ),
    "po010_final_summary": (
        f"audit/qa/{EPIC_SLUG}/checks/po-010/final_summary.txt"
    ),
    "close_report": "audit/EPIC-028_close_report.md",
    "close_manifest": "audit/EPIC-028_MANIFEST.json",
    "ops_created_files_sha256": (
        f"audit/ops/{EPIC_SLUG}/ops-01/created_files_sha256.txt"
    ),
}


def close_manifest_payload(
    captured_at_utc: str,
    qa_manifest: dict[str, object],
) -> dict[str, object]:
    """Delegate run-free manifest construction to the generic harness."""

    return qa_harness.run_free_close_manifest_payload(
        EPIC_ID,
        captured_at_utc,
        CLOSE_KEY_OUTPUTS,
        qa_manifest=qa_manifest,
    )


def main() -> int:
    """Verify frozen evidence without generating a close pack."""

    try:
        ensure_determinism_env()
        qa_harness.require_frozen_evidence(ROOT)
    except (DeterminismEnvError, OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
