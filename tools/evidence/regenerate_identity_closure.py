#!/usr/bin/env python3
"""Regenerate and verify the complete identity and release evidence closure."""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

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


def _env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(CLOSED_RAILS)
    return env


def _run(*args: str) -> None:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=_env(),
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"CLOSURE_STEP_FAILED:{' '.join(args)}:{proc.returncode}")


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
    _run("scripts/release_id_recompute.py", "--refresh-manifest")
    _refresh_cut_time_identity()
    _run("scripts/release_id_recompute.py", "--check")
    _run("tools/evidence/generate_env_matrix_snapshot.py")
    _run("tools/evidence/generate_identity_provenance.py")
    _run("tools/evidence/generate_release_bindings.py")
    _run("tools/cli/generate_showcompat_artifacts.py")
    _run("tools/cli/generate_cli_conformance_artifacts.py")
    _run("tools/evidence/generate_epic032_pr01_router_evidence.py")
    _run("tools/evidence/run_canonical_json_gate.py")
    _run(
        "-m",
        "pytest",
        "tests/transport/test_internal_version_contract.py",
        "-q",
    )
    _run("tools/evidence/update_evidence_index.py")
    _run("tools/evidence/orientation_demo.py")


def _check_closure() -> None:
    _verify_cut_time_identity()
    _run("scripts/release_id_recompute.py", "--check")
    _run("tools/evidence/generate_identity_provenance.py", "--check")
    _run("tools/evidence/generate_release_bindings.py", "--check")
    _run("tools/evidence/generate_env_matrix_snapshot.py", "--check")
    _run("tools/cli/generate_showcompat_artifacts.py", "--check")
    _run("tools/cli/generate_cli_conformance_artifacts.py", "--check")
    _run("tools/evidence/generate_epic032_pr01_router_evidence.py", "--check")
    _run("tools/evidence/run_canonical_json_gate.py", "--check-only")
    _run("tools/evidence/update_evidence_index.py", "--check")
    _run("tools/evidence/orientation_demo.py", "--check")
    _run(
        "-m",
        "pytest",
        "tests/evidence/test_internal_version_manifest_captures.py",
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
