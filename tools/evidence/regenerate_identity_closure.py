#!/usr/bin/env python3
"""Regenerate and verify the complete identity and release evidence closure."""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[2]
IDENTITY_SOURCE = ROOT / "engine/runtime/identity.py"
RELEASE_ID_PATH = ROOT / "artifacts/math/release_id.txt"
_RELEASE_LINE = re.compile(r'(?m)^    "release_id": "([0-9a-f]{64})",$')

CLOSED_RAILS = {
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "PIP_NO_INDEX": "1",
}


@dataclass(frozen=True)
class ClosureStep:
    """One deterministic producer and its residue-free validation command."""

    name: str
    write: tuple[str, ...]
    check: tuple[str, ...]
    write_env: tuple[tuple[str, str], ...] = ()


# This is the single declared write/check graph for deterministic local release
# artifacts that must exist before OPS-03.  The release pipeline consumes these
# bytes in check mode; it must never discover and repair stale primaries itself.
CLOSURE_STEPS = (
    ClosureStep(
        "config_artifacts",
        ("tools/config/generate_config_artifacts.py",),
        ("tools/config/generate_config_artifacts.py", "--check"),
    ),
    ClosureStep(
        "config_bundles",
        ("tools/config/generate_bundles.py",),
        ("tools/config/generate_bundles.py", "--check"),
    ),
    ClosureStep(
        "env_matrix",
        ("tools/evidence/generate_env_matrix_snapshot.py",),
        ("tools/evidence/generate_env_matrix_snapshot.py", "--check"),
    ),
    ClosureStep(
        "identity_provenance",
        ("tools/evidence/generate_identity_provenance.py",),
        ("tools/evidence/generate_identity_provenance.py", "--check"),
    ),
    ClosureStep(
        "release_bindings",
        ("tools/evidence/generate_release_bindings.py",),
        ("tools/evidence/generate_release_bindings.py", "--check"),
    ),
    ClosureStep(
        "showcompat",
        ("tools/cli/generate_showcompat_artifacts.py",),
        ("tools/cli/generate_showcompat_artifacts.py", "--check"),
    ),
    ClosureStep(
        "cli_conformance",
        ("tools/cli/generate_cli_conformance_artifacts.py",),
        ("tools/cli/generate_cli_conformance_artifacts.py", "--check"),
    ),
    ClosureStep(
        "epic032_router",
        ("tools/evidence/generate_epic032_pr01_router_evidence.py",),
        ("tools/evidence/generate_epic032_pr01_router_evidence.py", "--check"),
    ),
    ClosureStep(
        "canonical_json",
        ("tools/evidence/run_canonical_json_gate.py",),
        ("tools/evidence/run_canonical_json_gate.py", "--check-only"),
    ),
    ClosureStep(
        "reader_cli_determinism",
        ("tools/evidence/generate_determinism_gate_proofs.py",),
        ("tools/evidence/generate_determinism_gate_proofs.py", "--check"),
    ),
    ClosureStep(
        "fixture_open_rails_abba",
        ("tools/evidence/generate_open_rails_abba_proof.py",),
        ("tools/evidence/generate_open_rails_abba_proof.py", "--check"),
    ),
    ClosureStep(
        "a7_transport",
        ("tools/evidence/generate_a7_transport_proofs.py",),
        ("tools/evidence/generate_a7_transport_proofs.py", "--check"),
        (("HDE_WRITE_A7_PROOFS", "1"),),
    ),
    ClosureStep(
        "rails_gate",
        ("tools/evidence/generate_rails_gate_evidence.py",),
        ("tools/evidence/generate_rails_gate_evidence.py", "--check"),
    ),
    ClosureStep(
        "db_runtime_posture",
        ("tools/evidence/generate_db_runtime_posture.py",),
        ("tools/evidence/generate_db_runtime_posture.py", "--check"),
    ),
    ClosureStep(
        "bodygraph_policy",
        ("tools/evidence/generate_bodygraph_policy_proofs.py",),
        ("tools/evidence/generate_bodygraph_policy_proofs.py", "--check"),
    ),
    ClosureStep(
        "architecture_snapshot",
        ("tools/evidence/generate_architecture_snapshot.py",),
        ("tools/evidence/generate_architecture_snapshot.py", "--check"),
    ),
    ClosureStep(
        "mapped_cache",
        ("tools/evidence/generate_v2_mapped_cache_evidence.py",),
        ("tools/evidence/generate_v2_mapped_cache_evidence.py", "--check"),
    ),
    ClosureStep(
        "internal_version",
        (
            "-m",
            "pytest",
            "tests/transport/test_internal_version_contract.py",
            "-q",
        ),
        (
            "-m",
            "pytest",
            "tests/evidence/test_internal_version_manifest_captures.py",
            "-q",
        ),
    ),
    ClosureStep(
        "evidence_index",
        ("tools/evidence/update_evidence_index.py",),
        ("tools/evidence/update_evidence_index.py", "--check"),
    ),
    ClosureStep(
        "orientation",
        ("tools/evidence/orientation_demo.py",),
        ("tools/evidence/orientation_demo.py", "--check"),
    ),
)


def _env(overrides: Mapping[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    env.update(CLOSED_RAILS)
    env.update(overrides or {})
    return env


def _run(*args: str, env_overrides: Mapping[str, str] | None = None) -> None:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=_env(env_overrides),
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"CLOSURE_STEP_FAILED:{' '.join(args)}:{proc.returncode}")


def _is_current(*args: str, env_overrides: Mapping[str, str] | None = None) -> bool:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=_env(env_overrides),
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0


def _ensure_step(step: ClosureStep) -> None:
    if _is_current(*step.check):
        return
    _run(*step.write, env_overrides=dict(step.write_env))
    _run(*step.check)


def _source_release_id(source: str) -> str:
    match = _RELEASE_LINE.search(source)
    if match is None:
        raise ValueError("cut_time_release_id_missing")
    return match.group(1)


def _replace_cut_time_release_id(source: str, release_id: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{64}", release_id):
        raise ValueError("release_id_invalid")
    current = _source_release_id(source)
    if current == release_id:
        return source
    updated, count = _RELEASE_LINE.subn(
        f'    "release_id": "{release_id}",',
        source,
        count=1,
    )
    if count != 1:
        raise ValueError("cut_time_release_id_update_failed")
    return updated


def _refresh_cut_time_identity() -> None:
    release_id = RELEASE_ID_PATH.read_text(encoding="utf-8").strip()
    source = IDENTITY_SOURCE.read_text(encoding="utf-8")
    updated = _replace_cut_time_release_id(source, release_id)
    if updated != source:
        IDENTITY_SOURCE.write_text(updated, encoding="utf-8")


def _verify_cut_time_identity() -> None:
    expected = RELEASE_ID_PATH.read_text(encoding="utf-8").strip()
    actual = _source_release_id(IDENTITY_SOURCE.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit("CUT_TIME_RELEASE_ID_MISMATCH")


def _write_closure() -> None:
    if not _is_current("scripts/release_id_recompute.py", "--check"):
        _run("scripts/release_id_recompute.py", "--refresh-manifest")
    _refresh_cut_time_identity()
    _run("scripts/release_id_recompute.py", "--check")
    for step in CLOSURE_STEPS:
        _ensure_step(step)


def _check_closure() -> None:
    _verify_cut_time_identity()
    _run("scripts/release_id_recompute.py", "--check")
    for step in CLOSURE_STEPS:
        _run(*step.check)
    _run("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check")
    _run(
        "-m",
        "pytest",
        "tests/evidence/test_aux_preview_identity_parity.py",
        "tests/evidence/test_release_manifest_content_binding.py",
        "tests/qa/test_epic022_acceptance_scaffold.py",
        "tests/qa/test_epic022_close_pack_ready.py",
        "-q",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if args.check:
        _check_closure()
    else:
        _write_closure()
        _check_closure()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
