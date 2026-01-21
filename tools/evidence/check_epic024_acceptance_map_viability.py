#!/usr/bin/env python3
"""Deterministic EPIC024 acceptance map viability checker."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.qa.step_log_header import append_output, create_header, write_header

DEFAULT_ACCEPTANCE_MAP = ROOT / "docs/acceptance_map_epic024.json"
DEFAULT_CHECK_DIR = ROOT / "audit/qa/hde-epic024/checks/epic024_acceptance_map_viability"
DEFAULT_REVIEW_DIR = (
    ROOT / "audit/qa/hde-epic024/remediation/s2_dev_acceptance_artifacts"
)
REPORT_NAME = "acceptance_map_viability.json"
SUMMARY_NAME = "acceptance_map_viability_summary.md"


@dataclass(frozen=True)
class TokenIssue:
    name: str
    issues: Sequence[str]


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _relative(path: Path, root: Path) -> str:
    if path.is_relative_to(root):
        return path.relative_to(root).as_posix()
    return path.as_posix()


def _unique_sorted(items: Iterable[str]) -> list[str]:
    return sorted(set(items))


def _looks_relative(path: str) -> bool:
    if path.startswith("/") or path.startswith("~"):
        return False
    if ".." in Path(path).parts:
        return False
    return True


def _collect_token_issues(
    token_name: str, evidence_titles: Iterable[str], *, root: Path
) -> list[str]:
    issues: set[str] = set()
    for evidence in evidence_titles:
        if not isinstance(evidence, str) or not evidence.strip():
            continue
        if evidence.endswith(".path_proof.txt"):
            issues.add(f"PATH_PROOF_USED:{token_name}:{evidence}")
        if not _looks_relative(evidence):
            if evidence.startswith("/") or evidence.startswith("~"):
                issues.add(f"ABSOLUTE_PATH:{token_name}:{evidence}")
            if ".." in Path(evidence).parts:
                issues.add(f"PARENT_PATH:{token_name}:{evidence}")
            continue
        if not (root / evidence).exists():
            issues.add(f"MISSING_EVIDENCE:{token_name}:{evidence}")
    return sorted(issues)


def build_report(
    *,
    acceptance_map_path: Path,
    root: Path,
    determinism_ok: bool,
    determinism_error: str | None,
) -> tuple[dict[str, object], str]:
    payload = _read_json(acceptance_map_path)
    if not isinstance(payload, dict):
        raise ValueError("acceptance map payload must be a JSON object")

    tokens = payload.get("tokens")
    if not isinstance(tokens, list):
        raise ValueError("acceptance map tokens must be a list")

    issues: list[str] = []
    duplicates: set[str] = set()
    seen: set[str] = set()
    token_entries: list[TokenIssue] = []
    evidence_count = 0

    for entry in tokens:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()
        if name in seen:
            duplicates.add(name)
        seen.add(name)
        evidence_titles = entry.get("evidence_titles") or []
        if isinstance(evidence_titles, list):
            evidence_count += len([item for item in evidence_titles if isinstance(item, str)])
        token_issues = (
            _collect_token_issues(name, evidence_titles, root=root)
            if isinstance(evidence_titles, list)
            else [f"EVIDENCE_TITLES_INVALID:{name}"]
        )
        issues.extend(token_issues)
        token_entries.append(TokenIssue(name=name, issues=token_issues))

    for duplicate in sorted(duplicates):
        issues.append(f"DUPLICATE_TOKEN:{duplicate}")

    status = "PASS"
    if not determinism_ok:
        status = "TOOLING_BLOCKED"
    elif issues:
        status = "FAIL_BEHAVIOR"

    report = {
        "schema": "epic024.acceptance_map_viability.v1",
        "status": status,
        "inputs": {
            "acceptance_map": _relative(acceptance_map_path, root),
        },
        "determinism_env": {
            "ok": determinism_ok,
            "error": determinism_error,
        },
        "summary": {
            "token_count": len(seen),
            "evidence_title_count": evidence_count,
            "issue_count": len(_unique_sorted(issues)),
            "duplicate_tokens": sorted(duplicates),
        },
        "token_issues": {
            entry.name: list(entry.issues)
            for entry in token_entries
            if entry.issues
        },
        "issues": _unique_sorted(issues),
    }
    return report, status


def _write_report(path: Path, report: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(report, sort_keys=True))


def _write_summary(path: Path, report: dict[str, object], status: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    summary = f"status: {status}\nissues: {len(report['issues'])}\n"
    path.write_text(summary, encoding="utf-8")


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
        check_id="epic024_acceptance_map_viability",
        command=command,
        status=status,
        pf_refs=["PF19 §4.4.4"],
        intended_tokens=[],
        claimed_tokens=[],
    )
    header["exit_code"] = exit_code
    header["evidence_outputs"] = list(evidence_outputs)
    write_header(log_path, header)
    append_output(log_path, summary)


def run_report_mode(args: argparse.Namespace) -> int:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        return 2

    report, status = build_report(
        acceptance_map_path=Path(args.acceptance_map),
        root=ROOT,
        determinism_ok=True,
        determinism_error=None,
    )
    review_dir = Path(args.review_dir)
    _write_report(review_dir / REPORT_NAME, report)
    _write_summary(review_dir / SUMMARY_NAME, report, status)
    return 0 if status == "PASS" else 1


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

    acceptance_map_path = Path(args.acceptance_map)
    if not acceptance_map_path.exists():
        return 2

    report, status = build_report(
        acceptance_map_path=acceptance_map_path,
        root=ROOT,
        determinism_ok=determinism_ok,
        determinism_error=determinism_error,
    )
    report_bytes = sercanon(report, sort_keys=True)
    report_path = Path(args.output_dir) / REPORT_NAME

    if args.check:
        issues = _validate_report(report_path, report_bytes)
        if issues:
            status = "FAIL_BEHAVIOR"
        return 0 if status == "PASS" else 1

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_bytes(report_bytes)
    evidence_outputs = [_relative(report_path, ROOT)]
    summary = f"status: {status}\nissues: {len(report['issues'])}\n"
    exit_code = 0 if status == "PASS" else 1
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
        description="Deterministic EPIC024 acceptance map viability checker."
    )
    subparsers = parser.add_subparsers(dest="mode")

    check_parser = subparsers.add_parser("check", help="Run or validate check outputs")
    check_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    check_parser.add_argument("--output-dir", default=DEFAULT_CHECK_DIR)
    check_parser.add_argument("--check", action="store_true", help="validate outputs only")
    check_parser.add_argument(
        "--command",
        default="python tools/evidence/check_epic024_acceptance_map_viability.py check",
    )
    check_parser.set_defaults(func=run_check_mode)

    report_parser = subparsers.add_parser(
        "report", help="Write remediation review artifacts"
    )
    report_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    report_parser.add_argument("--review-dir", default=DEFAULT_REVIEW_DIR)
    report_parser.set_defaults(func=run_report_mode)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
