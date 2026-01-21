#!/usr/bin/env python3
"""Deterministic evidence index snapshot contract checker (D23)."""
from __future__ import annotations

import argparse
import json
import sys
import datetime as _dt
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence import generate_evidence_index_snapshot as snapshot
from tools.evidence import update_evidence_index
from tools.qa.step_log_header import append_output, create_header, write_header

DEFAULT_SNAPSHOT = ROOT / "audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"
DEFAULT_HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
DEFAULT_MIRROR = ROOT / "artifacts/evidence_index.jsonl"
DEFAULT_CHECK_DIR = (
    ROOT / "audit/qa/hde-epic024/checks/d23_evidence_index_snapshot_contract"
)
REPORT_NAME = "evidence_index_snapshot_contract_report.json"


def _relative(path: Path, root: Path) -> str:
    if path.is_relative_to(root):
        return path.relative_to(root).as_posix()
    return path.as_posix()


def _unique_sorted(items: Iterable[str]) -> list[str]:
    return sorted(set(items))


def _load_snapshot(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _write_path_proof(path: Path, *, produced_at: str, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=snapshot._sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime)
        if not check
        else None,
        produced_at=produced_at if not check else None,
        default_produced_at=produced_at,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def _looks_like_repo_path(value: str) -> bool:
    if not value or value.startswith("/") or value.startswith("~"):
        return False
    if " " in value or "::" in value:
        return False
    return True


def build_report(
    *,
    root: Path,
    snapshot_path: Path,
    human_index_path: Path,
    mirror_path: Path,
    determinism_ok: bool,
    determinism_error: str | None,
    check_path_proof: bool = True,
) -> tuple[dict[str, object], str]:
    issues: list[str] = []
    if not snapshot_path.exists():
        issues.append("MISSING_SNAPSHOT")
        status = "TOOLING_BLOCKED" if determinism_ok else "TOOLING_BLOCKED"
        report = {
            "schema": "epic024.evidence_index_snapshot_contract.v1",
            "status": status,
            "inputs": {
                "snapshot_path": _relative(snapshot_path, root),
                "human_index_path": _relative(human_index_path, root),
                "mirror_path": _relative(mirror_path, root),
            },
            "determinism_env": {
                "ok": determinism_ok,
                "error": determinism_error,
            },
            "issues": issues,
        }
        return report, status

    payload = _load_snapshot(snapshot_path)
    if not isinstance(payload, dict):
        issues.append("SNAPSHOT_NOT_OBJECT")
        payload = {}

    if payload.get("schema_version") != "1":
        issues.append("SCHEMA_VERSION")

    generated_at = payload.get("generated_at_utc")
    if not isinstance(generated_at, str):
        issues.append("GENERATED_AT")
    else:
        try:
            snapshot.update_evidence_index._parse_utc_iso8601(generated_at)
        except ValueError:
            issues.append("GENERATED_AT_FORMAT")

    inputs = payload.get("inputs")
    if not isinstance(inputs, dict):
        issues.append("INPUTS")
        inputs = {}

    human_path = inputs.get("human_index_path")
    mirror_path_value = inputs.get("machine_mirror_path")
    if human_path != snapshot.HUMAN_INDEX_REL:
        issues.append("HUMAN_PATH_MISMATCH")
    if mirror_path_value != snapshot.MIRROR_REL:
        issues.append("MIRROR_PATH_MISMATCH")

    if not _looks_like_repo_path(human_path or ""):
        issues.append("HUMAN_PATH_INVALID")
    if not _looks_like_repo_path(mirror_path_value or ""):
        issues.append("MIRROR_PATH_INVALID")

    if not human_index_path.exists():
        issues.append("MISSING_HUMAN_INDEX")
    if not mirror_path.exists():
        issues.append("MISSING_MIRROR_INDEX")

    if human_index_path.exists():
        expected_human_sha = snapshot._sha256_path(human_index_path)
        if inputs.get("human_index_sha256") != expected_human_sha:
            issues.append("HUMAN_SHA_MISMATCH")
    if mirror_path.exists():
        expected_mirror_sha = snapshot._sha256_path(mirror_path)
        if inputs.get("machine_mirror_sha256") != expected_mirror_sha:
            issues.append("MIRROR_SHA_MISMATCH")

    try:
        parity_expected = (
            snapshot._load_human_keys(human_index_path)
            == snapshot._load_mirror_keys(mirror_path)
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        issues.append(f"PARITY_READ_ERROR:{exc.__class__.__name__}")
        parity_expected = None

    parity = payload.get("parity")
    if not isinstance(parity, dict):
        issues.append("PARITY_OBJECT")
        parity = {}
    parity_value = parity.get("artifact_keys_match")
    if parity_value is not True:
        issues.append("PARITY_FALSE")
    if parity_expected is not None and parity_value != parity_expected:
        issues.append("PARITY_MISMATCH")

    if snapshot_path.read_bytes() != sercanon(payload, sort_keys=True):
        issues.append("NON_CANONICAL_JSON")

    if check_path_proof:
        proof_path = snapshot_path.with_suffix(snapshot_path.suffix + ".path_proof.txt")
        if not proof_path.exists():
            issues.append("MISSING_PATH_PROOF")

    status = "PASS"
    if not determinism_ok:
        status = "TOOLING_BLOCKED"
    elif issues:
        status = "FAIL_BEHAVIOR"

    report = {
        "schema": "epic024.evidence_index_snapshot_contract.v1",
        "status": status,
        "inputs": {
            "snapshot_path": _relative(snapshot_path, root),
            "human_index_path": _relative(human_index_path, root),
            "mirror_path": _relative(mirror_path, root),
        },
        "determinism_env": {
            "ok": determinism_ok,
            "error": determinism_error,
        },
        "issues": _unique_sorted(issues),
    }
    return report, status


def _write_report(path: Path, report: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(report, sort_keys=True))


def _validate_report(path: Path, expected: bytes) -> list[str]:
    if not path.exists():
        return [f"missing_output:{path}"]
    if path.read_bytes() != expected:
        return [f"mismatch_output:{path}"]
    return []


def _write_primary_log(
    output_dir: Path,
    *,
    status: str,
    command: str,
    exit_code: int,
    evidence_outputs: Sequence[str],
    summary: str,
) -> None:
    log_path = output_dir / "primary.log"
    header = create_header(
        check_id="d23_evidence_index_snapshot_contract",
        command=command,
        status=status,
        pf_refs=["PF12 §Evidence Index"],
        intended_tokens=[],
        claimed_tokens=[],
    )
    header["exit_code"] = exit_code
    header["evidence_outputs"] = list(evidence_outputs)
    write_header(log_path, header)
    append_output(log_path, summary)


def _status_exit_code(status: str) -> int:
    if status == "PASS":
        return 0
    if status == "TOOLING_BLOCKED":
        return 2
    return 1


def run_check_mode(args: argparse.Namespace) -> int:
    determinism_ok = True
    determinism_error = None
    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:
        determinism_ok = False
        determinism_error = str(exc)

    if not determinism_ok:
        return 2

    snapshot_path = Path(args.snapshot)
    human_index_path = Path(args.human_index)
    mirror_path = Path(args.mirror)
    report, status = build_report(
        root=ROOT,
        snapshot_path=snapshot_path,
        human_index_path=human_index_path,
        mirror_path=mirror_path,
        determinism_ok=determinism_ok,
        determinism_error=determinism_error,
        check_path_proof=False,
    )
    if status == "FAIL_BEHAVIOR" and not args.check:
        inputs = snapshot.Inputs(
            human_path=human_index_path,
            mirror_path=mirror_path,
            snapshot_path=snapshot_path,
        )
        snapshot.run_snapshot(inputs, check_only=False)
        report, status = build_report(
            root=ROOT,
            snapshot_path=snapshot_path,
            human_index_path=human_index_path,
            mirror_path=mirror_path,
            determinism_ok=determinism_ok,
            determinism_error=determinism_error,
            check_path_proof=False,
        )

    if snapshot_path.exists():
        produced_at = _utc_now()
        try:
            _write_path_proof(snapshot_path, produced_at=produced_at, check=args.check)
        except SystemExit as exc:
            report["issues"] = _unique_sorted([*report["issues"], f"PATH_PROOF:{exc}"])
            status = "FAIL_BEHAVIOR"
            report["status"] = status

    report_bytes = sercanon(report, sort_keys=True)
    report_path = Path(args.output_dir) / REPORT_NAME

    if args.check:
        issues = _validate_report(report_path, report_bytes)
        if issues:
            status = "FAIL_BEHAVIOR"
        return _status_exit_code(status)

    _write_report(report_path, report)
    evidence_outputs = [_relative(report_path, ROOT)]
    summary = f"status: {status}\nissues: {len(report['issues'])}\n"
    exit_code = _status_exit_code(status)
    _write_primary_log(
        report_path.parent,
        status=status,
        command=args.command,
        exit_code=exit_code,
        evidence_outputs=evidence_outputs,
        summary=summary,
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic evidence index snapshot contract checker."
    )
    parser.add_argument("--snapshot", default=DEFAULT_SNAPSHOT)
    parser.add_argument("--human-index", default=DEFAULT_HUMAN_INDEX)
    parser.add_argument("--mirror", default=DEFAULT_MIRROR)
    parser.add_argument("--output-dir", default=DEFAULT_CHECK_DIR)
    parser.add_argument("--check", action="store_true", help="validate outputs only")
    parser.add_argument(
        "--command",
        default="python tools/evidence/check_d23_evidence_index_snapshot_contract.py",
    )
    args = parser.parse_args()
    return run_check_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
