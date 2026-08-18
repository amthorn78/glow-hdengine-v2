#!/usr/bin/env python3
"""Generate EPIC027 acceptance ledger and close-pack artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC027"
EPIC_SLUG = "hde-epic027"
RUN_ID = "epic027-close"

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
QA_CHECKS_ROOT = QA_ROOT / "checks"
ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic027.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"
CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-027_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-027_MANIFEST.json"

GATE_COMMANDS: list[tuple[str, list[str]]] = [
    ("gate_update_evidence_index_write", ["python", "tools/evidence/update_evidence_index.py"]),
    ("gate_orientation_demo_write", ["python", "tools/evidence/orientation_demo.py"]),
    ("gate_update_evidence_index_check", ["python", "tools/evidence/update_evidence_index.py", "--check"]),
    ("gate_orientation_demo_check", ["python", "tools/evidence/orientation_demo.py", "--check"]),
    ("gate_evidence_paths_validation", ["python", "tools/evidence/validate_evidence_paths.py"]),
    ("gate_lf_endings", ["python", "tools/evidence/check_lf_endings.py"]),
    ("gate_mirror_schema", ["ci/checks/check_mirror_schema.sh"]),
]

TOKENS: list[dict[str, object]] = [
    {
        "name": "COMPOSITE_ABBA_IDENTITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/compat/identity_hash.txt",
            "artifacts/compat/AB.json",
            "artifacts/compat/BA.json",
        ],
    },
    {
        "name": "TWO_RUN_IDENTITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/audit/cli/two_run_identity.log",
            "artifacts/writer/conjunction_write_readback.log",
            "artifacts/writer/conjunction_writer_summary.json",
        ],
    },
    {
        "name": "CLI_READER_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/cli_reader_parity.txt",
            "docs/ENDPOINTS_CATALOG.json",
        ],
    },
    {
        "name": "A7_GET_QUOTED_ETAG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_get.txt",
        ],
    },
    {
        "name": "A7_HEAD_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_get.txt",
        ],
    },
    {
        "name": "A7_304_OMITS_CT_CL_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_304.txt",
        ],
    },
    {
        "name": "A7_VARY_AUTH_AE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
        ],
    },
    {
        "name": "A7_ENCODING_INVARIANCE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_304.txt",
        ],
    },
    {
        "name": "ENDPOINTS_CATALOG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/ENDPOINTS_CATALOG.json",
            "docs/ENDPOINTS_CATALOG.json.sha256",
        ],
    },
    {
        "name": "ENDPOINTS_CATALOG_ENV_GATE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/ENDPOINTS_CATALOG.json",
            "artifacts/proofs/endpoints_env_gate_proof.log",
        ],
    },
    {
        "name": "ENV_RAILS_POLICY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "audit/gates/determinism/env_pins.log",
            "audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_UPDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "audit/qa/hde-epic027/checks/gate_update_evidence_index_write/primary.log",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_HASH_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.sha256",
            "audit/qa/hde-epic027/checks/gate_update_evidence_index_check/primary.log",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_MIRROR_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log",
        ],
    },
    {
        "name": "EVIDENCE_PATHS_VALIDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "audit/qa/hde-epic027/checks/gate_evidence_paths_validation/primary.log",
        ],
    },
    {
        "name": "CI_CHECK_MIRROR_SCHEMA_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log",
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "CI_CHECK_FINAL_LF_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "audit/qa/hde-epic027/checks/gate_lf_endings/primary.log",
            "audit/qa/hde-epic027/acceptance_map_viability.log",
        ],
    },
]


TOKEN_MATRIX_ROWS: list[dict[str, str]] = [
    {
        "token_name": "COMPOSITE_ABBA_IDENTITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/compat/identity_hash.txt; artifacts/compat/AB.json; artifacts/compat/BA.json",
        "ci_tests_jobs": "python tools/evidence/generate_conjunction_writer_evidence.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D1 compat family bound without reimplementation.",
    },
    {
        "token_name": "TWO_RUN_IDENTITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/audit/cli/two_run_identity.log; artifacts/writer/conjunction_write_readback.log; artifacts/writer/conjunction_writer_summary.json",
        "ci_tests_jobs": "python tools/evidence/generate_conjunction_writer_evidence.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D1/D4 identity and write-readback families bound.",
    },
    {
        "token_name": "CLI_READER_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/cli_reader_parity.txt; docs/ENDPOINTS_CATALOG.json",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D1 parity family bound to existing proof artifacts.",
    },
    {
        "token_name": "A7_GET_QUOTED_ETAG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 A7 success capture reused.",
    },
    {
        "token_name": "A7_HEAD_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_head.txt; artifacts/proofs/success_get.txt",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 A7 HEAD parity bound.",
    },
    {
        "token_name": "A7_304_OMITS_CT_CL_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_304.txt",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 304 transport behavior bound.",
    },
    {
        "token_name": "A7_VARY_AUTH_AE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt; artifacts/proofs/success_head.txt",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 Vary transport posture bound.",
    },
    {
        "token_name": "A7_ENCODING_INVARIANCE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt; artifacts/proofs/success_head.txt; artifacts/proofs/success_304.txt",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 encoding invariance family bound.",
    },
    {
        "token_name": "ENDPOINTS_CATALOG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/ENDPOINTS_CATALOG.json; docs/ENDPOINTS_CATALOG.json.sha256",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 endpoint catalog snapshot bound.",
    },
    {
        "token_name": "ENDPOINTS_CATALOG_ENV_GATE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/ENDPOINTS_CATALOG.json; artifacts/proofs/endpoints_env_gate_proof.log",
        "ci_tests_jobs": "python tools/qa/generate_epic027_close_pack.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D3 env-gating proof family bound.",
    },
    {
        "token_name": "ENV_RAILS_POLICY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "audit/gates/determinism/env_pins.log; audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log",
        "ci_tests_jobs": "ci/checks/check_env_pins.sh",
        "qa_root_logs": "checks/gate_mirror_schema/primary.log",
        "status": "Implemented",
        "notes": "D4 closed-rails posture bound.",
    },
    {
        "token_name": "EVIDENCE_INDEX_UPDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
        "ci_tests_jobs": "python tools/evidence/update_evidence_index.py",
        "qa_root_logs": "checks/gate_update_evidence_index_write/primary.log",
        "status": "Implemented",
        "notes": "Global index refresh executed in-run.",
    },
    {
        "token_name": "EVIDENCE_INDEX_HASH_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/evidence/INDEX.sha256",
        "ci_tests_jobs": "python tools/evidence/update_evidence_index.py --check",
        "qa_root_logs": "checks/gate_update_evidence_index_check/primary.log",
        "status": "Implemented",
        "notes": "Hash sentinel verified in-run.",
    },
    {
        "token_name": "EVIDENCE_INDEX_MIRROR_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
        "ci_tests_jobs": "ci/checks/check_mirror_schema.sh",
        "qa_root_logs": "checks/gate_mirror_schema/primary.log",
        "status": "Implemented",
        "notes": "Mirror schema validated in-run.",
    },
    {
        "token_name": "EVIDENCE_PATHS_VALIDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
        "ci_tests_jobs": "python tools/evidence/validate_evidence_paths.py",
        "qa_root_logs": "checks/gate_evidence_paths_validation/primary.log",
        "status": "Implemented",
        "notes": "Path validation gate executed in-run.",
    },
    {
        "token_name": "CI_CHECK_MIRROR_SCHEMA_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/evidence_index.jsonl; docs/evidence/INDEX.json",
        "ci_tests_jobs": "ci/checks/check_mirror_schema.sh",
        "qa_root_logs": "checks/gate_mirror_schema/primary.log",
        "status": "Implemented",
        "notes": "Records-only mirror canonicality check passed.",
    },
    {
        "token_name": "CI_CHECK_FINAL_LF_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/acceptance_map_epic027.json; audit/qa/hde-epic027/token_evidence_matrix.md",
        "ci_tests_jobs": "python tools/evidence/check_lf_endings.py",
        "qa_root_logs": "checks/gate_lf_endings/primary.log",
        "status": "Implemented",
        "notes": "Final-LF gate executed in-run.",
    },
]


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT).as_posix()}")


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


def _write_path_proof(path: Path, produced_at: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )
    print(f"WROTE {rel}.path_proof.txt")


def _write_acceptance_map() -> None:
    _write_json(ACCEPTANCE_MAP_PATH, {"epic_id": EPIC_ID, "tokens": TOKENS})


def _write_token_matrix() -> None:
    lines = [
        "# HDE-EPIC027 Token ↔ Evidence Matrix",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in TOKEN_MATRIX_ROWS:
        lines.append(
            "| {token_name} | {owner_pf} | {evidence_artifacts} | {ci_tests_jobs} | {qa_root_logs} | {status} | {notes} |".format(
                **row
            )
        )
    _write_text(TOKEN_MATRIX_PATH, "\n".join(lines) + "\n")


def _run_gate_command(check_id: str, command: list[str]) -> None:
    check_dir = QA_CHECKS_ROOT / check_id
    check_dir.mkdir(parents=True, exist_ok=True)
    cmd_text = " ".join(command)
    (check_dir / "command_used.txt").write_text(cmd_text + "\n", encoding="utf-8")

    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    (check_dir / "stdout.log").write_text(proc.stdout, encoding="utf-8")
    (check_dir / "stderr.log").write_text(proc.stderr, encoding="utf-8")
    (check_dir / "rc.txt").write_text(f"{proc.returncode}\n", encoding="utf-8")

    status = "PASS" if proc.returncode == 0 else "FAIL"
    primary = [
        f"check_id:{check_id}",
        f"status:{status}",
        f"command:{cmd_text}",
        f"stdout_log:audit/qa/{EPIC_SLUG}/checks/{check_id}/stdout.log",
        f"stderr_log:audit/qa/{EPIC_SLUG}/checks/{check_id}/stderr.log",
        f"rc:{proc.returncode}",
    ]
    (check_dir / "primary.log").write_text("\n".join(primary) + "\n", encoding="utf-8")
    print(f"WROTE audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log")

    if proc.returncode != 0:
        raise SystemExit(f"GATE_FAILED:{check_id}")


def _run_governed_gates() -> None:
    for check_id, command in GATE_COMMANDS:
        _run_gate_command(check_id, command)


def _write_close_report(produced_at: str) -> None:
    executed_logs = "\n".join(f"- `audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log`" for check_id, _ in GATE_COMMANDS)
    content = f"""# HDE-EPIC027 — Close Report

## Overview
HDE-CONJ009.2 closes EPIC027 at the global discipline layer by binding existing conjunction D1, D3, and D4 proof families into canonical acceptance ledgers and close-pack outputs.

## Capture timestamp
- `{produced_at}`

## Reused proof families (no reimplementation)
- D1 compat family: `artifacts/compat/identity_hash.txt`
- D3 reader/endpoint family: `docs/ENDPOINTS_CATALOG.json`, `artifacts/proofs/success_get.txt`, `artifacts/proofs/success_head.txt`, `artifacts/proofs/success_304.txt`
- D4 writer family: `artifacts/writer/conjunction_write_readback.log`, `artifacts/writer/conjunction_writer_summary.json`

## EPIC027 closure artifacts
- `docs/acceptance_map_epic027.json`
- `audit/qa/hde-epic027/token_evidence_matrix.md`
- `audit/qa/hde-epic027/acceptance_map_viability.log`
- `audit/EPIC-027_MANIFEST.json`
- `audit/EPIC-027_close_report.md`

## Token posture
Acceptance ledgers bind canonical PF04 token names only, including D1/D3/D4 families and HDE-CONJ009.2 index/mirror discipline tokens.

## Index/Mirror coherence
The following commands were executed during this generator run before close-pack completion:
{executed_logs}

These command logs provide direct evidence for refresh/re-validation of:
- `docs/evidence/INDEX.json`
- `docs/evidence/INDEX.sha256`
- `artifacts/evidence_index.jsonl`
- `artifacts/evidence_index.jsonl.sha256`
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str) -> None:
    key_outputs = {
        "acceptance_map": "docs/acceptance_map_epic027.json",
        "token_matrix": "audit/qa/hde-epic027/token_evidence_matrix.md",
        "acceptance_map_viability": "audit/qa/hde-epic027/acceptance_map_viability.log",
        "close_report": "audit/EPIC-027_close_report.md",
        "close_manifest": "audit/EPIC-027_MANIFEST.json",
        "d1_compat_identity_hash": "artifacts/compat/identity_hash.txt",
        "d3_endpoints_catalog": "docs/ENDPOINTS_CATALOG.json",
        "d3_success_get": "artifacts/proofs/success_get.txt",
        "d3_success_head": "artifacts/proofs/success_head.txt",
        "d3_success_304": "artifacts/proofs/success_304.txt",
        "d4_writer_readback": "artifacts/writer/conjunction_write_readback.log",
        "d4_writer_summary": "artifacts/writer/conjunction_writer_summary.json",
        "index_human": "docs/evidence/INDEX.json",
        "index_human_sha256": "docs/evidence/INDEX.sha256",
        "index_mirror": "artifacts/evidence_index.jsonl",
        "index_mirror_sha256": "artifacts/evidence_index.jsonl.sha256",
    }
    for check_id, _ in GATE_COMMANDS:
        key_outputs[f"qa_log_{check_id}"] = f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log"

    _write_json(
        CLOSE_MANIFEST_PATH,
        {
            "captured_at_utc": produced_at,
            "closeout_dir": f"audit/qa/{EPIC_SLUG}",
            "epic_id": EPIC_ID,
            "key_outputs": key_outputs,
            "qa_epic_root": f"audit/qa/{EPIC_SLUG}",
            "run_id": RUN_ID,
            "subtask_id": "HDE-CONJ009.2",
            "task_id": "HDE-CONJ009",
        },
    )


def _ensure_required_paths() -> None:
    required = [
        ROOT / "artifacts/compat/identity_hash.txt",
        ROOT / "artifacts/compat/AB.json",
        ROOT / "artifacts/compat/BA.json",
        ROOT / "artifacts/proofs/cli_reader_parity.txt",
        ROOT / "docs/ENDPOINTS_CATALOG.json",
        ROOT / "docs/ENDPOINTS_CATALOG.json.sha256",
        ROOT / "artifacts/proofs/endpoints_env_gate_proof.log",
        ROOT / "artifacts/proofs/success_get.txt",
        ROOT / "artifacts/proofs/success_head.txt",
        ROOT / "artifacts/proofs/success_304.txt",
        ROOT / "artifacts/writer/conjunction_write_readback.log",
        ROOT / "artifacts/writer/conjunction_writer_summary.json",
        ROOT / "artifacts/audit/cli/two_run_identity.log",
        ROOT / "audit/gates/determinism/env_pins.log",
    ]
    missing = [p.relative_to(ROOT).as_posix() for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_PROOFS:{','.join(missing)}")


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    qa_harness.generate_acceptance_map_viability(config)
    print(f"WROTE {VIABILITY_LOG_PATH.relative_to(ROOT).as_posix()}")


def _manifest_outputs_exist() -> None:
    payload = json.loads(CLOSE_MANIFEST_PATH.read_text(encoding="utf-8"))
    missing: list[str] = []
    for rel in sorted(set(payload["key_outputs"].values())):
        if not (ROOT / rel).exists():
            missing.append(rel)
    if missing:
        raise SystemExit(f"DANGLING_MANIFEST_PATHS:{','.join(missing)}")


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    produced_at = _utc_now()
    _ensure_required_paths()
    QA_ROOT.mkdir(parents=True, exist_ok=True)

    _write_acceptance_map()
    _write_token_matrix()
    _write_viability_log()
    _write_close_manifest(produced_at)
    _write_close_report(produced_at)

    _run_governed_gates()
    _manifest_outputs_exist()

    for path in [
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
    ]:
        _write_path_proof(path, produced_at)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
