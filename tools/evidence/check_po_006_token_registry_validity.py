#!/usr/bin/env python3
"""Deterministic PO-006 token registry validity check."""
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
DEFAULT_REGISTRY_EXPORT = ROOT / "reports/qa_acceptance_tokens.json"
DEFAULT_TOKEN_SETS = (
    ROOT
    / "audit/qa/hde-epic024/remediation/s1_token_registry_discovery/token_sets.json"
)
DEFAULT_CHECK_DIR = ROOT / "audit/qa/hde-epic024/checks/po-006_token_registry_validity"
DEFAULT_REVIEW_DIR = (
    ROOT
    / "audit/qa/hde-epic024/remediation/s2_dev_acceptance_artifacts"
)

CHECK_REPORT_NAME = "token_registry_validity_report.json"
REVIEW_REPORT_NAME = "po_006_token_registry_validity_report.json"
REVIEW_SUMMARY_NAME = "po_006_token_registry_validity_summary.md"


@dataclass(frozen=True)
class TokenSets:
    canonical_tokens: set[str]
    deprecated_spellings: set[str]
    alias_map: dict[str, str]


@dataclass(frozen=True)
class TokenExtract:
    tokens: list[str]
    duplicates: list[str]


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _relative(path: Path) -> str:
    if path.is_relative_to(ROOT):
        return path.relative_to(ROOT).as_posix()
    return path.as_posix()


def _unique_sorted(items: Iterable[str]) -> list[str]:
    return sorted(set(items))


def load_token_sets(path: Path) -> TokenSets:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ValueError("token_sets must be a JSON object")
    alias_map = payload.get("alias_map")
    canonical_tokens = payload.get("canonical_tokens")
    deprecated_spellings = payload.get("deprecated_spellings")
    if not isinstance(alias_map, dict):
        raise ValueError("token_sets.alias_map must be an object")
    if not isinstance(canonical_tokens, list):
        raise ValueError("token_sets.canonical_tokens must be a list")
    if not isinstance(deprecated_spellings, list):
        raise ValueError("token_sets.deprecated_spellings must be a list")
    return TokenSets(
        canonical_tokens={str(token) for token in canonical_tokens if token},
        deprecated_spellings={str(token) for token in deprecated_spellings if token},
        alias_map={str(key): str(value) for key, value in alias_map.items()},
    )


def extract_acceptance_map_tokens(path: Path) -> TokenExtract:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ValueError("acceptance map must be a JSON object")
    entries = payload.get("tokens")
    if not isinstance(entries, list):
        raise ValueError("acceptance map tokens must be a list")
    tokens: list[str] = []
    duplicates: set[str] = set()
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()
        if name in seen:
            duplicates.add(name)
        seen.add(name)
        tokens.append(name)
    return TokenExtract(tokens=tokens, duplicates=sorted(duplicates))


def extract_registry_tokens(path: Path) -> TokenExtract:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ValueError("registry export must be a JSON object")
    entries = payload.get("tokens")
    if not isinstance(entries, list):
        raise ValueError("registry export tokens must be a list")
    tokens: list[str] = []
    duplicates: set[str] = set()
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()
        if name in seen:
            duplicates.add(name)
        seen.add(name)
        tokens.append(name)
    return TokenExtract(tokens=tokens, duplicates=sorted(duplicates))


def normalize_tokens(tokens: Iterable[str], alias_map: dict[str, str]) -> list[str]:
    return [alias_map.get(token, token) for token in tokens]


def build_report(
    *,
    acceptance_tokens: TokenExtract,
    registry_tokens: TokenExtract,
    token_sets: TokenSets,
    acceptance_map_path: Path,
    registry_export_path: Path,
    token_sets_path: Path,
    determinism_ok: bool,
    determinism_error: str | None,
) -> tuple[dict[str, object], str]:
    acceptance_unique = _unique_sorted(acceptance_tokens.tokens)
    registry_unique = _unique_sorted(registry_tokens.tokens)
    deprecated_used = sorted(
        token for token in acceptance_unique if token in token_sets.deprecated_spellings
    )
    alias_hits = {
        token: token_sets.alias_map[token]
        for token in acceptance_unique
        if token in token_sets.alias_map
    }
    normalized_acceptance = _unique_sorted(
        normalize_tokens(acceptance_tokens.tokens, token_sets.alias_map)
    )
    missing_in_registry = sorted(
        token for token in normalized_acceptance if token not in registry_unique
    )
    missing_in_canonical = sorted(
        token for token in normalized_acceptance if token not in token_sets.canonical_tokens
    )

    status = "PASS"
    if not determinism_ok:
        status = "TOOLING_BLOCKED"
    elif missing_in_registry or deprecated_used:
        status = "FAIL_BEHAVIOR"

    report: dict[str, object] = {
        "schema": "po-006.token_registry_validity.v1",
        "status": status,
        "inputs": {
            "acceptance_map": _relative(acceptance_map_path),
            "registry_export": _relative(registry_export_path),
            "token_sets": _relative(token_sets_path),
        },
        "determinism_env": {
            "ok": determinism_ok,
            "error": determinism_error,
        },
        "acceptance_map": {
            "token_count": len(acceptance_unique),
            "tokens": acceptance_unique,
            "duplicates": acceptance_tokens.duplicates,
        },
        "registry_export": {
            "token_count": len(registry_unique),
            "tokens": registry_unique,
            "duplicates": registry_tokens.duplicates,
        },
        "canonical_registry": {
            "token_count": len(token_sets.canonical_tokens),
            "tokens": sorted(token_sets.canonical_tokens),
            "deprecated_spellings": sorted(token_sets.deprecated_spellings),
            "alias_map": dict(sorted(token_sets.alias_map.items())),
        },
        "comparison": {
            "normalized_acceptance_tokens": normalized_acceptance,
            "missing_in_registry": missing_in_registry,
            "missing_in_canonical": missing_in_canonical,
            "deprecated_spellings_used": deprecated_used,
            "alias_hits": alias_hits,
            "extra_registry_tokens": sorted(
                token for token in registry_unique if token not in normalized_acceptance
            ),
        },
    }
    return report, status


def render_token_list(tokens: Sequence[str]) -> str:
    return "\n".join(tokens) + ("\n" if tokens else "")


def render_summary(report: dict[str, object]) -> str:
    acceptance = report["acceptance_map"]
    registry = report["registry_export"]
    comparison = report["comparison"]
    lines = [
        f"status: {report['status']}",
        f"acceptance_tokens: {acceptance['token_count']}",
        f"registry_tokens: {registry['token_count']}",
        f"missing_in_registry: {len(comparison['missing_in_registry'])}",
        f"deprecated_spellings_used: {len(comparison['deprecated_spellings_used'])}",
    ]
    if comparison["missing_in_registry"]:
        lines.append("missing_tokens:")
        lines.extend(f"- {token}" for token in comparison["missing_in_registry"])
    if comparison["deprecated_spellings_used"]:
        lines.append("deprecated_spellings:")
        lines.extend(
            f"- {token}" for token in comparison["deprecated_spellings_used"]
        )
    return "\n".join(lines) + "\n"


def _write_report(path: Path, report: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(report, sort_keys=True))


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _validate_output(path: Path, expected: str) -> list[str]:
    if not path.exists():
        return [f"missing_output:{path}"]
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        return [f"mismatch_output:{path}"]
    return []


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
        check_id="po-006_token_registry_validity",
        command=command,
        status=status,
        pf_refs=["PF10 Addendum 2.8", "PF19 §3.4.6"],
        intended_tokens=[],
        claimed_tokens=[],
    )
    header["exit_code"] = exit_code
    header["evidence_outputs"] = list(evidence_outputs)
    write_header(log_path, header)
    append_output(log_path, summary)
    append_output(
        log_path,
        "captures:\n- rg_acceptance_map_output.txt\n- rg_registry_output.txt\n- "
        f"{CHECK_REPORT_NAME}\n",
    )


def run_report_mode(args: argparse.Namespace) -> int:
    determinism_ok = True
    determinism_error = None
    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:
        determinism_ok = False
        determinism_error = str(exc)

    token_sets = load_token_sets(Path(args.token_sets))
    acceptance_tokens = extract_acceptance_map_tokens(Path(args.acceptance_map))
    registry_tokens = extract_registry_tokens(Path(args.registry_export))
    report, status = build_report(
        acceptance_tokens=acceptance_tokens,
        registry_tokens=registry_tokens,
        token_sets=token_sets,
        acceptance_map_path=Path(args.acceptance_map),
        registry_export_path=Path(args.registry_export),
        token_sets_path=Path(args.token_sets),
        determinism_ok=determinism_ok,
        determinism_error=determinism_error,
    )

    review_dir = Path(args.review_dir)
    _write_report(review_dir / REVIEW_REPORT_NAME, report)
    _write_text(review_dir / REVIEW_SUMMARY_NAME, render_summary(report))

    return 0 if status == "PASS" else (2 if status == "TOOLING_BLOCKED" else 1)


def run_check_mode(args: argparse.Namespace) -> int:
    determinism_ok = True
    determinism_error = None
    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:
        determinism_ok = False
        determinism_error = str(exc)

    acceptance_map_path = Path(args.acceptance_map)
    registry_export_path = Path(args.registry_export)
    token_sets_path = Path(args.token_sets)
    output_dir = Path(args.output_dir)

    if not acceptance_map_path.exists() or not registry_export_path.exists():
        status = "TOOLING_BLOCKED"
        summary = "missing_inputs\n"
        if args.check:
            return 2
        _write_primary_log(
            output_dir,
            status=status,
            command=args.command,
            exit_code=2,
            evidence_outputs=[],
            summary=summary,
        )
        return 2

    token_sets = load_token_sets(token_sets_path)
    acceptance_tokens = extract_acceptance_map_tokens(acceptance_map_path)
    registry_tokens = extract_registry_tokens(registry_export_path)

    report, status = build_report(
        acceptance_tokens=acceptance_tokens,
        registry_tokens=registry_tokens,
        token_sets=token_sets,
        acceptance_map_path=acceptance_map_path,
        registry_export_path=registry_export_path,
        token_sets_path=token_sets_path,
        determinism_ok=determinism_ok,
        determinism_error=determinism_error,
    )

    summary = render_summary(report)
    acceptance_capture = render_token_list(_unique_sorted(acceptance_tokens.tokens))
    registry_capture = render_token_list(_unique_sorted(registry_tokens.tokens))
    report_bytes = sercanon(report, sort_keys=True)

    capture_paths = [
        output_dir / "rg_acceptance_map_output.txt",
        output_dir / "rg_registry_output.txt",
        output_dir / CHECK_REPORT_NAME,
    ]

    issues: list[str] = []
    if args.check:
        issues.extend(_validate_output(capture_paths[0], acceptance_capture))
        issues.extend(_validate_output(capture_paths[1], registry_capture))
        issues.extend(_validate_report(capture_paths[2], report_bytes))
        if issues:
            status = "FAIL_BEHAVIOR"
        if not determinism_ok:
            status = "TOOLING_BLOCKED"
        return 0 if status == "PASS" else (2 if status == "TOOLING_BLOCKED" else 1)

    output_dir.mkdir(parents=True, exist_ok=True)
    _write_text(capture_paths[0], acceptance_capture)
    _write_text(capture_paths[1], registry_capture)
    _write_report(capture_paths[2], report)

    evidence_outputs = [
        _relative(path) for path in capture_paths
    ]

    exit_code = 0 if status == "PASS" else (2 if status == "TOOLING_BLOCKED" else 1)
    _write_primary_log(
        output_dir,
        status=status,
        command=args.command,
        exit_code=exit_code,
        evidence_outputs=evidence_outputs,
        summary=summary,
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic PO-006 token registry validity check."
    )
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers(dest="mode")

    check_parser = subparsers.add_parser("check", help="Run or validate PO-006 outputs")
    check_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    check_parser.add_argument("--registry-export", default=DEFAULT_REGISTRY_EXPORT)
    check_parser.add_argument("--token-sets", default=DEFAULT_TOKEN_SETS)
    check_parser.add_argument("--output-dir", default=DEFAULT_CHECK_DIR)
    check_parser.add_argument("--check", action="store_true", help="validate outputs only")
    check_parser.add_argument(
        "--command",
        default="python tools/evidence/check_po_006_token_registry_validity.py check",
    )
    check_parser.set_defaults(func=run_check_mode)

    report_parser = subparsers.add_parser(
        "report", help="Write remediation review artifacts"
    )
    report_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    report_parser.add_argument("--registry-export", default=DEFAULT_REGISTRY_EXPORT)
    report_parser.add_argument("--token-sets", default=DEFAULT_TOKEN_SETS)
    report_parser.add_argument("--review-dir", default=DEFAULT_REVIEW_DIR)
    report_parser.set_defaults(func=run_report_mode)

    args = parser.parse_args()
    if args.func is None:
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
