#!/usr/bin/env python3
"""Invoke and strictly validate the canonical HDE-EPIC038 sanity pipeline."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log"
PINS = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}


def _valid_log() -> bool:
    try:
        data = LOG.read_bytes()
        text = data.decode("utf-8")
    except (OSError, UnicodeError):
        return False
    stages = [line for line in text.splitlines() if line.startswith("check ")]
    return (data.endswith(b"\n") and not data.endswith(b"\n\n") and len(stages) == 18
            and text.startswith("run:sanity-pipeline\n")
            and "\nenv:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC\n" in text
            and all(line.endswith(":OK") for line in stages[:-1])
            and stages[-1] == "check 18 PR-A nonfinal gate:FAIL"
            and "pr_a_state:nonfinal_fail_closed\n" in text
            and "final_readiness_blocked:pr_a_nonfinal_ops03_pr_b_binding_required\n" in text
            and "first_failed_stage:18 PR-A nonfinal gate\nsummary:FAIL\n" in text
            and "ops_evidence:retained_integrity_provenance_secret_safe_only;historical_nonclaim=true;not_rerun=true\n" in text)


def _log_version() -> tuple[int, int, int, int, int] | None:
    """Return filesystem generation metadata for the canonical sanity receipt."""
    try:
        stat = LOG.stat()
    except OSError:
        return None
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


def main() -> int:
    env = os.environ.copy()
    env.update(PINS)
    prior_log_version = _log_version()
    result = subprocess.run([sys.executable, "tools/evidence/run_sanity_pipeline.py"], cwd=ROOT, env=env)
    current_log_version = _log_version()
    if (
        result.returncode == 1
        and current_log_version is not None
        and current_log_version != prior_log_version
        and _valid_log()
    ):
        return 0
    return result.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
