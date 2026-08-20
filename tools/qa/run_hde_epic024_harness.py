#!/usr/bin/env python3
"""HDE-EPIC024 QA harness entrypoint (closed rails)."""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
import argparse
import copy
from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env
from tools.qa.step_log_header import append_output, create_header, write_header

QA_ROOT = ROOT / "audit/qa/hde-epic024"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
DOC_DELTAS_ROOT = ROOT / "audit/docdeltas"
ACCEPTANCE_MAP_PATH = ROOT / "docs/acceptance_map_epic024.json"

RUN_ID = "epic024-close"

TOKEN_ROSTER = [
    "TESTS_PASS_OK",
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "QA_PRECOMMIT_CHECKLIST_OK",
    "QA_POSTCOMMIT_CHECKLIST_OK",
    "QA_LIVE_QA_RUN_OK",
    "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
    "QA_BOOTSTRAP_OK",
    "QA_BOOTSTRAP_TOOLING_FAIL",
    "QA_HARNESS_DISCIPLINE_OK",
    "CLI_READER_PARITY_OK",
    "CLI_NO_ALT_JSON_OK",
    "CLI_STDOUT_LF_OK",
    "JSON_CANONICAL_CHECK_OK",
    "ENV_LC_ALL_C_OK",
    "DETERMINISM_ENV_PINS_OK",
    "SANITY_PIPELINE_OK",
    "EVIDENCE_INDEX_MIRROR_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "CI_CHECK_MIRROR_SCHEMA_OK",
    "CI_CHECK_FINAL_LF_OK",
    "TWO_RUN_IDENTITY_OK",
]


@dataclass(frozen=True)
class CheckSpec:
    check_id: str
    command: Sequence[str] | None
    description: str
    evidence_outputs: Sequence[str]


def _canonical_json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _text_bytes(content: str) -> bytes:
    if not content.endswith("\n"):
        content += "\n"
    return content.encode("utf-8")

def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(_text_bytes(content))


def _write_canonical_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(_canonical_json_bytes(payload))


def _env_for_subprocess() -> dict[str, str]:
    env = os.environ.copy()
    for key, value in DETERMINISM_ENV_PINS.items():
        env[key] = value
    env["APP_ENV"] = "dev"
    return env


def _command_to_str(command: Sequence[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def _status_from_exit(exit_code: int) -> str:
    if exit_code == 0:
        return "PASS"
    if exit_code == 1:
        return "FAIL_BEHAVIOR"
    if exit_code == 2:
        return "TOOLING_BLOCKED"
    if exit_code == 3:
        return "FAIL_BEHAVIOR"
    return "FAIL_TOOLING"


def _is_missing_pytest(stderr: str) -> bool:
    lowered = stderr.lower()
    if "no module named" in lowered and "pytest" in lowered:
        return True
    if "modulenotfounderror" in lowered and "pytest" in lowered:
        return True
    return False


def _status_from_bootstrap(exit_code: int, stderr: str) -> str:
    if exit_code != 0 and _is_missing_pytest(stderr):
        return "FAIL_TOOLING"
    return _status_from_exit(exit_code)


def _write_primary_log(
    *,
    check_id: str,
    command: str,
    status: str,
    exit_code: int,
    evidence_outputs: Sequence[str],
    stdout: str,
    stderr: str,
) -> Path:
    log_path = QA_ROOT / "checks" / check_id / "primary.log"
    header = create_header(check_id=check_id, command=command, status=status)
    header["exit_code"] = exit_code
    header["evidence_outputs"] = list(evidence_outputs)
    write_header(log_path, header)
    content = "\n".join(
        [
            "== STDOUT ==",
            stdout.rstrip(),
            "",
            "== STDERR ==",
            stderr.rstrip(),
            "",
            "== RC ==",
            str(exit_code),
        ]
    )
    append_output(log_path, content)
    return log_path


def _run_command(check: CheckSpec, env: Mapping[str, str]) -> tuple[str, int, Path]:
    command_str = _command_to_str(check.command or [])
    if check.command is None:
        return "PASS", 0, _write_primary_log(
            check_id=check.check_id,
            command=check.description,
            status="PASS",
            exit_code=0,
            evidence_outputs=check.evidence_outputs,
            stdout="",
            stderr="",
        )

    proc = subprocess.run(
        list(check.command),
        capture_output=True,
        text=True,
        env=dict(env),
    )
    if check.check_id == "D00_bootstrap_pytest":
        status = _status_from_bootstrap(proc.returncode, proc.stderr)
    else:
        status = _status_from_exit(proc.returncode)
    log_path = _write_primary_log(
        check_id=check.check_id,
        command=command_str,
        status=status,
        exit_code=proc.returncode,
        evidence_outputs=check.evidence_outputs,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )
    return status, proc.returncode, log_path


def _qa_manifest_payload(checks: Iterable[CheckSpec]) -> dict[str, dict[str, str]]:
    return {
        check.check_id: {
            "check_id": check.check_id,
            "log_path": f"checks/{check.check_id}/primary.log",
        }
        for check in checks
    }


def _write_step_logs_manifest(checks: Iterable[CheckSpec]) -> Path:
    manifest_path = QA_ROOT / "qa_step_logs_manifest.json"
    _write_canonical_json(manifest_path, _qa_manifest_payload(checks))
    return manifest_path


def _write_doc_deltas() -> tuple[Path, Path]:
    captured_at = _utc_now()
    qa_doc = QA_ROOT / "00_meta/doc_deltas.md"
    root_doc = DOC_DELTAS_ROOT / "hde-epic024_doc_deltas.md"
    qa_body = "\n".join(
        [
            "# HDE-EPIC024 QA Doc Delta",
            "",
            "## EPIC024 QA root updates",
            "- Added EPIC024 QA root with step logs, token matrix, acceptance-map viability log, and manifest.",
            "- Captured EPIC024 close-pack and acceptance-map artifacts for governed QA closure.",
        ]
    )
    root_body = "\n".join(
        [
            "# HDE-EPIC024 Doc Delta Draft (PR-04)",
            "",
            f"captured_at_utc: {captured_at}",
            "",
            "## EPIC024 scaffolds introduced",
            "",
            "- Added EPIC024 acceptance map, token↔evidence matrix, and QA step-log manifest.",
            "- Recorded EPIC024 close-pack artifacts and doc-delta surfaces under audit/.",
        ]
    )
    _write_text(qa_doc, qa_body)
    _write_text(root_doc, root_body)
    return qa_doc, root_doc


def _write_close_pack() -> tuple[Path, Path]:
    close_report = ROOT / "audit/EPIC-024_close_report.md"
    close_manifest = ROOT / "audit/EPIC-024_MANIFEST.json"
    close_report_body = "\n".join(
        [
            "# HDE-EPIC024 — Close Report",
            "",
            "## Overview",
            "EPIC024 completes the QA root close-surface capture, anchoring the governed acceptance map, token matrix, and close-pack artifacts for deterministic closure.",
            "",
            "## Final token roster",
            *(f"- {token}" for token in TOKEN_ROSTER),
            "",
            "## Acceptance and evidence pointers",
            "- docs/acceptance_map_epic024.json",
            "- audit/qa/hde-epic024/token_evidence_matrix.md",
            "- audit/qa/hde-epic024/acceptance_map_viability.log",
            "- audit/docdeltas/hde-epic024_doc_deltas.md",
            "- audit/qa/hde-epic024/qa_step_logs_manifest.json",
            "",
            "## Canonical close-pack files",
            "- Close report: audit/EPIC-024_close_report.md",
            "- Close manifest: audit/EPIC-024_MANIFEST.json",
            "",
            "## QA Rails — Open/Close (Final PR)",
            "- Default posture: closed rails (SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC).",
            "- Any temporary rail opening must be explicitly scoped, evidenced, and closed immediately after use.",
            "",
            "## Live QA requirement",
            "- Live QA runs must follow the closed-rails posture and be recorded via governed QA logs before any acceptance claims.",
        ]
    )
    _write_text(close_report, close_report_body)

    close_payload = {
        "captured_at_utc": _utc_now(),
        "closeout_dir": "audit/qa/hde-epic024",
        "epic_id": "HDE-EPIC024",
        "key_outputs": {
            "acceptance_map": "docs/acceptance_map_epic024.json",
            "token_matrix": "audit/qa/hde-epic024/token_evidence_matrix.md",
            "acceptance_map_viability": "audit/qa/hde-epic024/acceptance_map_viability.log",
            "doc_deltas": "audit/docdeltas/hde-epic024_doc_deltas.md",
            "qa_step_manifest": "audit/qa/hde-epic024/qa_step_logs_manifest.json",
            "close_report": "audit/EPIC-024_close_report.md",
            "close_manifest": "audit/EPIC-024_MANIFEST.json",
        },
        "qa_epic_root": "audit/qa/hde-epic024",
        "qa_root": "audit/qa/hde-epic024",
        "qa_step_manifest_path": "audit/qa/hde-epic024/qa_step_logs_manifest.json",
        "run_id": RUN_ID,
    }
    _write_canonical_json(close_manifest, close_payload)
    return close_report, close_manifest


def _render_token_matrix(*, bootstrap_status: str) -> bytes:
    matrix_path = TOKEN_MATRIX_PATH
    bootstrap_ok = bootstrap_status == "PASS"
    bootstrap_tooling_fail = bootstrap_status in {"FAIL_TOOLING", "TOOLING_BLOCKED"}
    rows = [
        {
            "token_name": "TESTS_PASS_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "evidence": "audit/qa/hde-epic024/checks/D06_tests_pass/primary.log",
            "ci": "python -m pytest tests/evidence tests/ops/test_evidence_index.py",
            "qa_logs": "checks/D06_tests_pass/primary.log",
            "status": "Implemented",
            "notes": "checks: D06_tests_pass",
        },
        {
            "token_name": "DOC_DELTA_PRESENT_OK",
            "owner_pf": "PF10 — HDE-Build Notes §2.5",
            "evidence": "audit/docdeltas/hde-epic024_doc_deltas.md; audit/qa/hde-epic024/00_meta/doc_deltas.md",
            "ci": "PF10 doc-delta review",
            "qa_logs": "00_meta/doc_deltas.md",
            "status": "Implemented",
            "notes": "checks: D15_doc_deltas",
        },
        {
            "token_name": "EVIDENCE_INDEX_UPDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Index",
            "evidence": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
            "ci": "python tools/evidence/update_evidence_index.py",
            "qa_logs": "checks/D08_update_evidence_index/primary.log",
            "status": "Implemented",
            "notes": "checks: D08_update_evidence_index",
        },
        {
            "token_name": "MACHINE_MIRROR_UPDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "evidence": "artifacts/evidence_index.jsonl",
            "ci": "ci/checks/check_mirror_schema.sh",
            "qa_logs": "checks/D11_check_mirror_schema/primary.log",
            "status": "Implemented",
            "notes": "checks: D11_check_mirror_schema",
        },
        {
            "token_name": "EVIDENCE_INDEX_HASH_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Hashing",
            "evidence": "docs/evidence/INDEX.sha256",
            "ci": "ci/checks/check_evidence_index_hash.sh",
            "qa_logs": "checks/D10_check_evidence_index_hash/primary.log",
            "status": "Implemented",
            "notes": "checks: D10_check_evidence_index_hash",
        },
        {
            "token_name": "QA_PRECOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "evidence": "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log; audit/gates/determinism/env_pins.log",
            "ci": "python -m pytest --version; ci/checks/check_env_pins.sh",
            "qa_logs": "checks/D00_bootstrap_pytest/primary.log",
            "status": "Implemented",
            "notes": "checks: D00_bootstrap_pytest, D01_env_pins_gate",
        },
        {
            "token_name": "QA_POSTCOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "evidence": "audit/qa/hde-epic024/qa_step_logs_manifest.json; audit/qa/hde-epic024/acceptance_map_viability.log",
            "ci": "python tools/qa/run_hde_epic024_harness.py",
            "qa_logs": "acceptance_map_viability.log",
            "status": "Implemented",
            "notes": "checks: D13_acceptance_map_viability",
        },
        {
            "token_name": "QA_LIVE_QA_RUN_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.2",
            "evidence": "artifacts/sampler/seed_replay/cli_http_seed_replay.json; artifacts/sampler/two_run/identity.json",
            "ci": "python tools/evidence/generate_sampler_evidence.py",
            "qa_logs": "checks/D04_sampler_evidence/primary.log",
            "status": "Implemented",
            "notes": "checks: D04_sampler_evidence",
        },
        {
            "token_name": "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.3",
            "evidence": "audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log",
            "ci": "python tools/qa/run_hde_epic024_harness.py",
            "qa_logs": "checks/D14_harness_selftest/primary.log",
            "status": "Implemented",
            "notes": "checks: D14_harness_selftest",
        },
        {
            "token_name": "QA_BOOTSTRAP_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.1",
            "evidence": "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log",
            "ci": "python -m pytest --version",
            "qa_logs": "checks/D00_bootstrap_pytest/primary.log",
            "status": "Implemented" if bootstrap_ok else "Token-incomplete",
            "notes": "checks: D00_bootstrap_pytest" if bootstrap_ok else "Not observed; bootstrap did not succeed.",
        },
        {
            "token_name": "QA_BOOTSTRAP_TOOLING_FAIL",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.1",
            "evidence": "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log",
            "ci": "python -m pytest --version",
            "qa_logs": "checks/D00_bootstrap_pytest/primary.log",
            "status": "Implemented" if bootstrap_tooling_fail else "Token-incomplete",
            "notes": "Observed tooling failure during bootstrap." if bootstrap_tooling_fail else "Not observed; bootstrap succeeded under closed rails (checks: D00_bootstrap_pytest).",
        },
        {
            "token_name": "QA_HARNESS_DISCIPLINE_OK",
            "owner_pf": "PF19 — Glow QA Guide §4.4.4",
            "evidence": "audit/qa/hde-epic024/qa_step_logs_manifest.json; audit/qa/hde-epic024/acceptance_map_viability.log",
            "ci": "python tools/qa/run_hde_epic024_harness.py",
            "qa_logs": "qa_step_logs_manifest.json",
            "status": "Implemented",
            "notes": "checks: D13_acceptance_map_viability",
        },
        {
            "token_name": "CLI_READER_PARITY_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA002.5)",
            "evidence": "artifacts/cli/reader_cli_parity.bytes; artifacts/cli/reader_dump.json",
            "ci": "python tools/cli/generate_showcompat_artifacts.py",
            "qa_logs": "checks/D03_showcompat_artifacts/primary.log",
            "status": "Implemented",
            "notes": "checks: D03_showcompat_artifacts",
        },
        {
            "token_name": "CLI_NO_ALT_JSON_OK",
            "owner_pf": "PF05 — CLI/API/Vendor Ref §6",
            "evidence": "artifacts/cli/showcompat/stdout.json; artifacts/cli/showcompat/args.json",
            "ci": "python tools/cli/generate_showcompat_artifacts.py",
            "qa_logs": "checks/D03_showcompat_artifacts/primary.log",
            "status": "Implemented",
            "notes": "checks: D03_showcompat_artifacts",
        },
        {
            "token_name": "CLI_STDOUT_LF_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA003.3)",
            "evidence": "artifacts/cli/showcompat/stdout.json; artifacts/cli/showcompat/stdout.json.sha256",
            "ci": "python tools/cli/generate_showcompat_artifacts.py",
            "qa_logs": "checks/D03_showcompat_artifacts/primary.log",
            "status": "Implemented",
            "notes": "checks: D03_showcompat_artifacts",
        },
        {
            "token_name": "JSON_CANONICAL_CHECK_OK",
            "owner_pf": "PF04 — Canon-HDE-Governance §Canonical JSON",
            "evidence": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson; audit/gates/json_gate/canonical/json_gate_compare_log.ndjson; audit/gates/json_gate/canonical/json_gate_structured_record.json",
            "ci": "python tools/evidence/run_canonical_json_gate.py",
            "qa_logs": "checks/D02_canonical_json_gate/primary.log",
            "status": "Implemented",
            "notes": "checks: D02_canonical_json_gate",
        },
        {
            "token_name": "ENV_LC_ALL_C_OK",
            "owner_pf": "PF19 — Glow QA Guide §Env Pins",
            "evidence": "audit/gates/determinism/env_pins.log",
            "ci": "ci/checks/check_env_pins.sh",
            "qa_logs": "checks/D01_env_pins_gate/primary.log",
            "status": "Implemented",
            "notes": "checks: D01_env_pins_gate",
        },
        {
            "token_name": "DETERMINISM_ENV_PINS_OK",
            "owner_pf": "PF19 — Glow QA Guide §Env Pins",
            "evidence": "audit/gates/determinism/env_pins.log",
            "ci": "ci/checks/check_env_pins.sh",
            "qa_logs": "checks/D01_env_pins_gate/primary.log",
            "status": "Implemented",
            "notes": "checks: D01_env_pins_gate",
        },
        {
            "token_name": "SANITY_PIPELINE_OK",
            "owner_pf": "PF19 — Glow QA Guide §Sanity Pipeline",
            "evidence": "audit/gates/sanity_pipeline/sanity_pipeline.log",
            "ci": "python tools/evidence/run_sanity_pipeline.py",
            "qa_logs": "checks/D07_sanity_pipeline/primary.log",
            "status": "Implemented",
            "notes": "checks: D07_sanity_pipeline",
        },
        {
            "token_name": "EVIDENCE_INDEX_MIRROR_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "evidence": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
            "ci": "ci/checks/check_mirror_schema.sh",
            "qa_logs": "checks/D11_check_mirror_schema/primary.log",
            "status": "Implemented",
            "notes": "checks: D11_check_mirror_schema",
        },
        {
            "token_name": "EVIDENCE_PATHS_VALIDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path Proofs",
            "evidence": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
            "ci": "python tools/evidence/update_evidence_index.py --check",
            "qa_logs": "checks/D08_update_evidence_index/primary.log",
            "status": "Implemented",
            "notes": "checks: D08_update_evidence_index",
        },
        {
            "token_name": "EVIDENCE_PATH_PROOFS_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path Proofs",
            "evidence": "audit/qa/hde-epic024/checks/D08_update_evidence_index/primary.log",
            "ci": "python tools/evidence/update_evidence_index.py --check",
            "qa_logs": "checks/D08_update_evidence_index/primary.log",
            "status": "Implemented",
            "notes": "checks: D08_update_evidence_index",
        },
        {
            "token_name": "CI_CHECK_MIRROR_SCHEMA_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "evidence": "audit/qa/hde-epic024/checks/D11_check_mirror_schema/primary.log",
            "ci": "ci/checks/check_mirror_schema.sh",
            "qa_logs": "checks/D11_check_mirror_schema/primary.log",
            "status": "Implemented",
            "notes": "checks: D11_check_mirror_schema",
        },
        {
            "token_name": "CI_CHECK_FINAL_LF_OK",
            "owner_pf": "PF09 — HDE-Build Checklist §Final LF",
            "evidence": "audit/qa/hde-epic024/checks/D12_check_final_lf/primary.log",
            "ci": "ci/checks/check_final_lf.sh",
            "qa_logs": "checks/D12_check_final_lf/primary.log",
            "status": "Implemented",
            "notes": "checks: D12_check_final_lf",
        },
        {
            "token_name": "TWO_RUN_IDENTITY_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA002.5; HDE-SEPA004.4)",
            "evidence": "artifacts/ops/internal_version/two_run_identity.log; artifacts/ops/internal_version/request_chain_manifest.json",
            "ci": "python tools/evidence/run_sanity_pipeline.py",
            "qa_logs": "checks/D07_sanity_pipeline/primary.log",
            "status": "Implemented",
            "notes": "checks: D07_sanity_pipeline",
        },
    ]

    ordered = {row["token_name"]: row for row in rows}
    lines = [
        "# HDE-EPIC024 Token ↔ Evidence Matrix",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for token in TOKEN_ROSTER:
        row = ordered[token]
        lines.append(
            "| {token} | {owner} | {evidence} | {ci} | {qa} | {status} | {notes} |".format(
                token=row["token_name"],
                owner=row["owner_pf"],
                evidence=row["evidence"],
                ci=row["ci"],
                qa=row["qa_logs"],
                status=row["status"],
                notes=row["notes"],
            )
        )
    return _text_bytes("\n".join(lines))


def _write_token_matrix(*, bootstrap_status: str) -> Path:
    TOKEN_MATRIX_PATH.parent.mkdir(parents=True, exist_ok=True)
    TOKEN_MATRIX_PATH.write_bytes(_render_token_matrix(bootstrap_status=bootstrap_status))
    return TOKEN_MATRIX_PATH


def _render_acceptance_map(*, bootstrap_status: str) -> bytes:
    bootstrap_ok = bootstrap_status == "PASS"
    bootstrap_tooling_fail = bootstrap_status in {"FAIL_TOOLING", "TOOLING_BLOCKED"}
    tokens = [
        {
            "name": "TESTS_PASS_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D06_tests_pass/primary.log",
            ],
        },
        {
            "name": "DOC_DELTA_PRESENT_OK",
            "owner_pf": "PF10 — HDE-Build Notes §2.5",
            "status": "implemented",
            "evidence_titles": [
                "audit/docdeltas/hde-epic024_doc_deltas.md",
                "audit/qa/hde-epic024/00_meta/doc_deltas.md",
            ],
        },
        {
            "name": "EVIDENCE_INDEX_UPDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Index",
            "status": "implemented",
            "evidence_titles": [
                "docs/evidence/INDEX.json",
                "artifacts/evidence_index.jsonl",
            ],
        },
        {
            "name": "MACHINE_MIRROR_UPDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/evidence_index.jsonl",
            ],
        },
        {
            "name": "EVIDENCE_INDEX_HASH_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Hashing",
            "status": "implemented",
            "evidence_titles": [
                "docs/evidence/INDEX.sha256",
            ],
        },
        {
            "name": "QA_PRECOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log",
                "audit/gates/determinism/env_pins.log",
            ],
        },
        {
            "name": "QA_POSTCOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/qa_step_logs_manifest.json",
                "audit/qa/hde-epic024/acceptance_map_viability.log",
            ],
        },
        {
            "name": "QA_LIVE_QA_RUN_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.2",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/sampler/seed_replay/cli_http_seed_replay.json",
                "artifacts/sampler/two_run/identity.json",
            ],
        },
        {
            "name": "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.3",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log",
            ],
        },
        {
            "name": "QA_BOOTSTRAP_OK",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.1",
            "status": "implemented" if bootstrap_ok else "token_incomplete",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log",
            ],
        },
        {
            "name": "QA_BOOTSTRAP_TOOLING_FAIL",
            "owner_pf": "PF14 — HDE-Mechanics Guide §1.6.1",
            "status": "implemented" if bootstrap_tooling_fail else "token_incomplete",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log",
            ],
        },
        {
            "name": "QA_HARNESS_DISCIPLINE_OK",
            "owner_pf": "PF19 — Glow QA Guide §4.4.4",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/qa_step_logs_manifest.json",
                "audit/qa/hde-epic024/acceptance_map_viability.log",
            ],
        },
        {
            "name": "CLI_READER_PARITY_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA002.5)",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/cli/reader_cli_parity.bytes",
                "artifacts/cli/reader_dump.json",
            ],
        },
        {
            "name": "CLI_NO_ALT_JSON_OK",
            "owner_pf": "PF05 — CLI/API/Vendor Ref §6",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/cli/showcompat/stdout.json",
                "artifacts/cli/showcompat/args.json",
            ],
        },
        {
            "name": "CLI_STDOUT_LF_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA003.3)",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/cli/showcompat/stdout.json",
                "artifacts/cli/showcompat/stdout.json.sha256",
            ],
        },
        {
            "name": "JSON_CANONICAL_CHECK_OK",
            "owner_pf": "PF04 — Canon-HDE-Governance §Canonical JSON",
            "status": "implemented",
            "evidence_titles": [
                "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
                "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
                "audit/gates/json_gate/canonical/json_gate_structured_record.json",
            ],
        },
        {
            "name": "ENV_LC_ALL_C_OK",
            "owner_pf": "PF19 — Glow QA Guide §Env Pins",
            "status": "implemented",
            "evidence_titles": [
                "audit/gates/determinism/env_pins.log",
            ],
        },
        {
            "name": "DETERMINISM_ENV_PINS_OK",
            "owner_pf": "PF19 — Glow QA Guide §Env Pins",
            "status": "implemented",
            "evidence_titles": [
                "audit/gates/determinism/env_pins.log",
            ],
        },
        {
            "name": "SANITY_PIPELINE_OK",
            "owner_pf": "PF19 — Glow QA Guide §Sanity Pipeline",
            "status": "implemented",
            "evidence_titles": [
                "audit/gates/sanity_pipeline/sanity_pipeline.log",
            ],
        },
        {
            "name": "EVIDENCE_INDEX_MIRROR_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "status": "implemented",
            "evidence_titles": [
                "docs/evidence/INDEX.json",
                "artifacts/evidence_index.jsonl",
            ],
        },
        {
            "name": "EVIDENCE_PATHS_VALIDATED_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path Proofs",
            "status": "implemented",
            "evidence_titles": [
                "docs/evidence/INDEX.json",
                "artifacts/evidence_index.jsonl",
            ],
        },
        {
            "name": "EVIDENCE_PATH_PROOFS_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path Proofs",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D08_update_evidence_index/primary.log",
            ],
        },
        {
            "name": "CI_CHECK_MIRROR_SCHEMA_OK",
            "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D11_check_mirror_schema/primary.log",
            ],
        },
        {
            "name": "CI_CHECK_FINAL_LF_OK",
            "owner_pf": "PF09 — HDE-Build Checklist §Final LF",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic024/checks/D12_check_final_lf/primary.log",
            ],
        },
        {
            "name": "TWO_RUN_IDENTITY_OK",
            "owner_pf": "PF20 — HDE-Phased Epics (HDE-SEPA002.5; HDE-SEPA004.4)",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/ops/internal_version/two_run_identity.log",
                "artifacts/ops/internal_version/request_chain_manifest.json",
            ],
        },
    ]
    payload = {"epic_id": "HDE-EPIC024", "tokens": tokens}
    return _canonical_json_bytes(payload)


def _write_acceptance_map(*, bootstrap_status: str) -> Path:
    ACCEPTANCE_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACCEPTANCE_MAP_PATH.write_bytes(_render_acceptance_map(bootstrap_status=bootstrap_status))
    return ACCEPTANCE_MAP_PATH


def _status_rows_from_matrix(text: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("| ") or line.startswith("| ---") or "token_name" in line:
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 7:
            continue
        token, status = parts[0], parts[5]
        if token in rows:
            raise ValueError(f"duplicate token matrix row: {token}")
        rows[token] = status
    return rows


def _derive_retained_bootstrap_status(acceptance_map: object, token_matrix: str) -> str:
    if not isinstance(acceptance_map, dict) or not isinstance(acceptance_map.get("tokens"), list):
        raise ValueError("acceptance map malformed")
    map_rows: dict[str, str] = {}
    for row in acceptance_map["tokens"]:
        if not isinstance(row, dict) or not isinstance(row.get("name"), str) or not isinstance(row.get("status"), str):
            continue
        name = row["name"]
        if name in map_rows:
            raise ValueError(f"duplicate acceptance token: {name}")
        map_rows[name] = row["status"]
    matrix_rows = _status_rows_from_matrix(token_matrix)
    pair = (map_rows.get("QA_BOOTSTRAP_OK"), map_rows.get("QA_BOOTSTRAP_TOOLING_FAIL"), matrix_rows.get("QA_BOOTSTRAP_OK"), matrix_rows.get("QA_BOOTSTRAP_TOOLING_FAIL"))
    if pair == ("implemented", "token_incomplete", "Implemented", "Token-incomplete"):
        return "PASS"
    if pair == ("token_incomplete", "implemented", "Token-incomplete", "Implemented"):
        return "TOOLING_BLOCKED"
    raise ValueError("conflicting retained bootstrap status")


def _one_path_diff_ok(old: bytes, new: bytes) -> bool:
    return old.replace(b"artifacts/sanity/sanity.log", b"audit/gates/sanity_pipeline/sanity_pipeline.log") == new and old.count(b"artifacts/sanity/sanity.log") == 1 and new.count(b"audit/gates/sanity_pipeline/sanity_pipeline.log") == 1


def _selective_acceptance_bindings(*, write: bool) -> int:
    old_map_b = ACCEPTANCE_MAP_PATH.read_bytes()
    old_matrix_b = TOKEN_MATRIX_PATH.read_bytes()
    status = _derive_retained_bootstrap_status(json.loads(old_map_b.decode("utf-8")), old_matrix_b.decode("utf-8"))
    new_map_b = _render_acceptance_map(bootstrap_status=status)
    new_matrix_b = _render_token_matrix(bootstrap_status=status)
    if old_map_b == new_map_b and old_matrix_b == new_matrix_b:
        return 0
    if not (_one_path_diff_ok(old_map_b, new_map_b) and _one_path_diff_ok(old_matrix_b, new_matrix_b)):
        raise ValueError("selective acceptance binding diff is not exactly the approved sanity path update")
    if write:
        ACCEPTANCE_MAP_PATH.write_bytes(new_map_b)
        TOKEN_MATRIX_PATH.write_bytes(new_matrix_b)
        return 0
    return 1


def _write_acceptance_map_viability() -> tuple[Path, List[str]]:
    log_path = QA_ROOT / "acceptance_map_viability.log"
    issues: List[str] = []
    if not ACCEPTANCE_MAP_PATH.exists():
        issues.append("MISSING_ACCEPTANCE_MAP")
        _write_text(log_path, "acceptance_map: MISSING\nsummary: FAIL")
        return log_path, issues

    try:
        payload = json.loads(ACCEPTANCE_MAP_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"JSON_ERROR:{exc.msg}")
        _write_text(log_path, f"acceptance_map: INVALID_JSON\nsummary: FAIL\n{exc.msg}")
        return log_path, issues

    rel_map = ACCEPTANCE_MAP_PATH.relative_to(ROOT).as_posix()
    lines = [f"run:{RUN_ID}", f"acceptance_map: {rel_map}"]
    for token in payload.get("tokens", []):
        name = token.get("name", "<unknown>")
        for evidence in token.get("evidence_titles", []):
            if evidence.endswith(".path_proof.txt"):
                issues.append(f"PATH_PROOF_USED:{name}:{evidence}")
            if evidence.startswith("/"):
                issues.append(f"ABSOLUTE_PATH:{name}:{evidence}")
            if ".." in Path(evidence).parts:
                issues.append(f"PARENT_PATH:{name}:{evidence}")
            if not (ROOT / evidence).exists():
                issues.append(f"MISSING_EVIDENCE:{name}:{evidence}")
    if issues:
        lines.append("summary: FAIL")
        lines.extend(sorted(set(issues)))
    else:
        lines.append("summary: PASS")
    _write_text(log_path, "\n".join(lines))
    return log_path, issues


def _write_harness_selftest_log(evidence_paths: Sequence[Path]) -> tuple[Path, List[str]]:
    missing = [path.as_posix() for path in evidence_paths if not path.exists()]
    log_path = QA_ROOT / "checks/D14_harness_selftest/primary.log"
    status = "PASS" if not missing else "FAIL_BEHAVIOR"
    header = create_header(
        check_id="D14_harness_selftest",
        command="python (embedded) validate EPIC024 harness outputs",
        status=status,
    )
    header["exit_code"] = 0 if status == "PASS" else 3
    header["evidence_outputs"] = [path.as_posix() for path in evidence_paths]
    write_header(log_path, header)
    body = "PASS: harness outputs present." if not missing else "FAIL_BEHAVIOR: missing outputs\n" + "\n".join(missing)
    append_output(log_path, body)
    return log_path, missing


def _write_acceptance_map_check_log() -> Path:
    log_path = QA_ROOT / "checks/D18_acceptance_map/primary.log"
    header = create_header(
        check_id="D18_acceptance_map",
        command="python (embedded) write docs/acceptance_map_epic024.json",
        status="PASS",
    )
    header["exit_code"] = 0
    header["evidence_outputs"] = ["docs/acceptance_map_epic024.json"]
    write_header(log_path, header)
    append_output(log_path, "PASS: acceptance map generated.")
    return log_path


def _write_token_matrix_check_log() -> Path:
    log_path = QA_ROOT / "checks/D17_token_matrix/primary.log"
    header = create_header(
        check_id="D17_token_matrix",
        command="python (embedded) write audit/qa/hde-epic024/token_evidence_matrix.md",
        status="PASS",
    )
    header["exit_code"] = 0
    header["evidence_outputs"] = ["audit/qa/hde-epic024/token_evidence_matrix.md"]
    write_header(log_path, header)
    append_output(log_path, "PASS: token matrix generated.")
    return log_path


def _write_doc_deltas_check_log() -> Path:
    log_path = QA_ROOT / "checks/D15_doc_deltas/primary.log"
    header = create_header(
        check_id="D15_doc_deltas",
        command="python (embedded) write EPIC024 doc deltas",
        status="PASS",
    )
    header["exit_code"] = 0
    header["evidence_outputs"] = [
        "audit/docdeltas/hde-epic024_doc_deltas.md",
        "audit/qa/hde-epic024/00_meta/doc_deltas.md",
    ]
    write_header(log_path, header)
    append_output(log_path, "PASS: doc deltas generated.")
    return log_path


def _write_close_pack_check_log() -> Path:
    log_path = QA_ROOT / "checks/D16_close_pack/primary.log"
    header = create_header(
        check_id="D16_close_pack",
        command="python (embedded) write EPIC024 close report and manifest",
        status="PASS",
    )
    header["exit_code"] = 0
    header["evidence_outputs"] = [
        "audit/EPIC-024_close_report.md",
        "audit/EPIC-024_MANIFEST.json",
    ]
    write_header(log_path, header)
    append_output(log_path, "PASS: close pack generated.")
    return log_path


def _write_acceptance_map_viability_check_log(*, status: str, exit_code: int, issues: Sequence[str]) -> Path:
    log_path = QA_ROOT / "checks/D13_acceptance_map_viability/primary.log"
    header = create_header(
        check_id="D13_acceptance_map_viability",
        command="python (embedded) validate acceptance map evidence paths",
        status=status,
    )
    header["exit_code"] = exit_code
    header["evidence_outputs"] = [
        "audit/qa/hde-epic024/acceptance_map_viability.log",
    ]
    write_header(log_path, header)
    if status == "PASS":
        append_output(log_path, "PASS: acceptance map viability log generated.")
    else:
        append_output(log_path, "FAIL_BEHAVIOR: acceptance map viability issues detected.\n" + "\n".join(issues))
    return log_path


def _write_manifest_check_log() -> Path:
    log_path = QA_ROOT / "checks/D19_step_logs_manifest/primary.log"
    header = create_header(
        check_id="D19_step_logs_manifest",
        command="python (embedded) write qa_step_logs_manifest.json",
        status="PASS",
    )
    header["exit_code"] = 0
    header["evidence_outputs"] = [
        "audit/qa/hde-epic024/qa_step_logs_manifest.json",
    ]
    write_header(log_path, header)
    append_output(log_path, "PASS: step logs manifest written.")
    return log_path


def _check_specs() -> list[CheckSpec]:
    return [
        CheckSpec(
            check_id="D00_bootstrap_pytest",
            command=["python", "-m", "pytest", "--version"],
            description="python -m pytest --version",
            evidence_outputs=[],
        ),
        CheckSpec(
            check_id="D01_env_pins_gate",
            command=["ci/checks/check_env_pins.sh"],
            description="ci/checks/check_env_pins.sh",
            evidence_outputs=["audit/gates/determinism/env_pins.log"],
        ),
        CheckSpec(
            check_id="D02_canonical_json_gate",
            command=["python", "tools/evidence/run_canonical_json_gate.py"],
            description="python tools/evidence/run_canonical_json_gate.py",
            evidence_outputs=[
                "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
                "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
                "audit/gates/json_gate/canonical/json_gate_structured_record.json",
            ],
        ),
        CheckSpec(
            check_id="D03_showcompat_artifacts",
            command=["python", "tools/cli/generate_showcompat_artifacts.py"],
            description="python tools/cli/generate_showcompat_artifacts.py",
            evidence_outputs=[
                "artifacts/cli/showcompat/stdout.json",
                "artifacts/cli/showcompat/stdout.json.sha256",
                "artifacts/cli/showcompat/args.json",
            ],
        ),
        CheckSpec(
            check_id="D04_sampler_evidence",
            command=["python", "tools/evidence/generate_sampler_evidence.py"],
            description="python tools/evidence/generate_sampler_evidence.py",
            evidence_outputs=[
                "artifacts/sampler/seed_replay/cli_http_seed_replay.json",
                "artifacts/sampler/two_run/identity.json",
                "artifacts/sampler/abba/ab_ba_parity.json",
                "artifacts/sampler/pool_snapshots/baseline.json",
                "artifacts/sampler/diversity/diversity_requirements.json",
            ],
        ),
        CheckSpec(
            check_id="D05_arrays_as_sets",
            command=["python", "-m", "pytest", "tests/compare/test_arrays_as_sets.py"],
            description="python -m pytest tests/compare/test_arrays_as_sets.py",
            evidence_outputs=[],
        ),
        CheckSpec(
            check_id="D06_tests_pass",
            command=["python", "-m", "pytest", "tests/evidence", "tests/ops/test_evidence_index.py"],
            description="python -m pytest tests/evidence tests/ops/test_evidence_index.py",
            evidence_outputs=[],
        ),
        CheckSpec(
            check_id="D07_sanity_pipeline",
            command=["python", "tools/evidence/run_sanity_pipeline.py"],
            description="python tools/evidence/run_sanity_pipeline.py",
            evidence_outputs=["audit/gates/sanity_pipeline/sanity_pipeline.log"],
        ),
        CheckSpec(
            check_id="D08_update_evidence_index",
            command=["python", "tools/evidence/update_evidence_index.py"],
            description="python tools/evidence/update_evidence_index.py",
            evidence_outputs=[
                "docs/evidence/INDEX.json",
                "docs/evidence/INDEX.sha256",
                "artifacts/evidence_index.jsonl",
            ],
        ),
        CheckSpec(
            check_id="D09_generate_evidence_index_snapshot",
            command=["python", "tools/evidence/generate_evidence_index_snapshot.py"],
            description="python tools/evidence/generate_evidence_index_snapshot.py",
            evidence_outputs=["audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"],
        ),
        CheckSpec(
            check_id="D10_check_evidence_index_hash",
            command=["ci/checks/check_evidence_index_hash.sh"],
            description="ci/checks/check_evidence_index_hash.sh",
            evidence_outputs=["docs/evidence/INDEX.sha256"],
        ),
        CheckSpec(
            check_id="D11_check_mirror_schema",
            command=["ci/checks/check_mirror_schema.sh"],
            description="ci/checks/check_mirror_schema.sh",
            evidence_outputs=["artifacts/evidence_index.jsonl"],
        ),
        CheckSpec(
            check_id="D12_check_final_lf",
            command=["ci/checks/check_final_lf.sh"],
            description="ci/checks/check_final_lf.sh",
            evidence_outputs=[],
        ),
        CheckSpec(
            check_id="D17_token_matrix",
            command=None,
            description="python (embedded) write audit/qa/hde-epic024/token_evidence_matrix.md",
            evidence_outputs=["audit/qa/hde-epic024/token_evidence_matrix.md"],
        ),
        CheckSpec(
            check_id="D18_acceptance_map",
            command=None,
            description="python (embedded) write docs/acceptance_map_epic024.json",
            evidence_outputs=["docs/acceptance_map_epic024.json"],
        ),
        CheckSpec(
            check_id="D15_doc_deltas",
            command=None,
            description="python (embedded) write EPIC024 doc deltas",
            evidence_outputs=[
                "audit/docdeltas/hde-epic024_doc_deltas.md",
                "audit/qa/hde-epic024/00_meta/doc_deltas.md",
            ],
        ),
        CheckSpec(
            check_id="D16_close_pack",
            command=None,
            description="python (embedded) write EPIC024 close pack",
            evidence_outputs=[
                "audit/EPIC-024_close_report.md",
                "audit/EPIC-024_MANIFEST.json",
            ],
        ),
        CheckSpec(
            check_id="D19_step_logs_manifest",
            command=None,
            description="python (embedded) write qa_step_logs_manifest.json",
            evidence_outputs=["audit/qa/hde-epic024/qa_step_logs_manifest.json"],
        ),
        CheckSpec(
            check_id="D13_acceptance_map_viability",
            command=None,
            description="python (embedded) validate acceptance map evidence paths",
            evidence_outputs=["audit/qa/hde-epic024/acceptance_map_viability.log"],
        ),
        CheckSpec(
            check_id="D14_harness_selftest",
            command=None,
            description="python (embedded) validate EPIC024 harness outputs",
            evidence_outputs=[
                "audit/qa/hde-epic024/token_evidence_matrix.md",
                "docs/acceptance_map_epic024.json",
                "audit/qa/hde-epic024/acceptance_map_viability.log",
                "audit/docdeltas/hde-epic024_doc_deltas.md",
                "audit/EPIC-024_close_report.md",
                "audit/EPIC-024_MANIFEST.json",
            ],
        ),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh-acceptance-bindings-only", action="store_true")
    parser.add_argument("--check-acceptance-bindings", action="store_true")
    args = parser.parse_args()
    ensure_determinism_env(apply=True)
    if args.refresh_acceptance_bindings_only or args.check_acceptance_bindings:
        return _selective_acceptance_bindings(write=args.refresh_acceptance_bindings_only)
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    env = _env_for_subprocess()

    checks = _check_specs()
    _write_step_logs_manifest(checks)

    status_by_check: dict[str, str] = {}

    bootstrap_status = "UNKNOWN"
    for check in checks:
        if check.check_id == "D17_token_matrix":
            _write_token_matrix(bootstrap_status=bootstrap_status)
            _write_token_matrix_check_log()
            status_by_check[check.check_id] = "PASS"
            continue
        if check.check_id == "D18_acceptance_map":
            _write_acceptance_map(bootstrap_status=bootstrap_status)
            _write_acceptance_map_check_log()
            status_by_check[check.check_id] = "PASS"
            continue
        if check.check_id == "D15_doc_deltas":
            _write_doc_deltas()
            _write_doc_deltas_check_log()
            status_by_check[check.check_id] = "PASS"
            continue
        if check.check_id == "D16_close_pack":
            _write_close_pack()
            _write_close_pack_check_log()
            status_by_check[check.check_id] = "PASS"
            continue
        if check.check_id == "D13_acceptance_map_viability":
            _, issues = _write_acceptance_map_viability()
            status = "PASS" if not issues else "FAIL_BEHAVIOR"
            exit_code = 0 if not issues else 3
            _write_acceptance_map_viability_check_log(status=status, exit_code=exit_code, issues=issues)
            status_by_check[check.check_id] = status
            continue
        if check.check_id == "D14_harness_selftest":
            required = [
                QA_ROOT / "token_evidence_matrix.md",
                ACCEPTANCE_MAP_PATH,
                QA_ROOT / "acceptance_map_viability.log",
                DOC_DELTAS_ROOT / "hde-epic024_doc_deltas.md",
                ROOT / "audit/EPIC-024_close_report.md",
                ROOT / "audit/EPIC-024_MANIFEST.json",
            ]
            _, missing = _write_harness_selftest_log(required)
            status_by_check[check.check_id] = "PASS" if not missing else "FAIL_BEHAVIOR"
            continue
        if check.check_id == "D19_step_logs_manifest":
            _write_step_logs_manifest(checks)
            _write_manifest_check_log()
            status_by_check[check.check_id] = "PASS"
            continue

        status, _, _ = _run_command(check, env)
        status_by_check[check.check_id] = status
        if check.check_id == "D00_bootstrap_pytest":
            bootstrap_status = status

    failures = [name for name, status in status_by_check.items() if status != "PASS"]
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
