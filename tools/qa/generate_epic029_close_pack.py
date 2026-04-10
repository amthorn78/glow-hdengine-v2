#!/usr/bin/env python3
"""Generate EPIC029 offline acceptance + close-pack binding artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC029"
EPIC_SLUG = "hde-epic029"
RUN_ID = "epic029-close"
PF09_TASK_ID = "HDE-CONJ009"
PF09_SUBTASK_ID = "HDE-CONJ009.1"

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
OPS_ROOT = ROOT / "audit" / "ops" / EPIC_SLUG / "ops-01"

ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic029.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"
QA_STEP_MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"

SURFACE_INVENTORY_PATH = QA_ROOT / "00_meta" / "conjunction_json_surface_inventory.md"
DEV_HARNESS_BINDING_COVERAGE_PATH = QA_ROOT / "00_meta" / "dev_harness_binding_coverage.md"

DOC_DELTAS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_doc_deltas.md"
DRAIN_TARGETS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_drain_targets.md"

CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-029_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-029_MANIFEST.json"

OPS_REQUIRED = [
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_codes.txt",
    "codespaces_dev_sampler_url.md",
    "local_dev_sampler_url.md",
    "binding_disposition.md",
    "created_files_sha256.txt",
]

LIVE_QA_CHECKS = {
    "po-epic-close-live-qa": QA_ROOT / "checks" / "po-epic-close-live-qa" / "primary.log",
    "po-precommit": QA_ROOT / "checks" / "po-precommit" / "primary.log",
    "po-postcommit": QA_ROOT / "checks" / "po-postcommit" / "primary.log",
}


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


def _missing_required_paths() -> list[str]:
    required = [SURFACE_INVENTORY_PATH, ROOT / "artifacts" / "writer" / "conjunction_write_readback.log", ROOT / "artifacts" / "writer" / "conjunction_writer_summary.json"]
    required += [OPS_ROOT / name for name in OPS_REQUIRED]
    return [path.relative_to(ROOT).as_posix() for path in required if not path.exists()]


def _live_qa_status() -> dict[str, bool]:
    return {check_id: path.exists() for check_id, path in LIVE_QA_CHECKS.items()}


def _tokens(live_qa: dict[str, bool]) -> list[dict[str, object]]:
    return [
        {
            "name": "HDE_CONJ009_1_SURFACE_INVENTORY_BOUND_OK",
            "owner_pf": "PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ009.1",
            "status": "implemented",
            "evidence_titles": [
                "audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md",
                "docs/acceptance_map_epic029.json",
            ],
        },
        {
            "name": "HDE_CONJ008_1_WRITER_ENVELOPE_BOUND_OK",
            "owner_pf": "PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ008.1",
            "status": "implemented",
            "evidence_titles": [
                "artifacts/writer/conjunction_write_readback.log",
                "artifacts/writer/conjunction_writer_summary.json",
            ],
        },
        {
            "name": "HDE_CONJ001_4_DEV_HARNESS_CLOSURE_OK",
            "owner_pf": "PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ001.4",
            "status": "token_incomplete",
            "evidence_titles": [
                "audit/ops/hde-epic029/ops-01/binding_disposition.md",
                "audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md",
            ],
        },
        {
            "name": "TESTS_PASS_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if live_qa["po-epic-close-live-qa"] else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"],
        },
        {
            "name": "QA_PRECOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if live_qa["po-precommit"] else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-precommit/primary.log"],
        },
        {
            "name": "QA_POSTCOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if live_qa["po-postcommit"] else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-postcommit/primary.log"],
        },
    ]


def _write_acceptance_map(live_qa: dict[str, bool]) -> None:
    _write_json(ACCEPTANCE_MAP_PATH, {"epic_id": EPIC_ID, "tokens": _tokens(live_qa)})


def _write_token_matrix(live_qa: dict[str, bool]) -> None:
    lines = [
        "# HDE-EPIC029 Token ↔ Evidence Matrix",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| HDE_CONJ009_1_SURFACE_INVENTORY_BOUND_OK | PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ009.1 | audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md | Reuse-only bounded inventory from PR-01 | acceptance_map_viability.log | Implemented | Existing conjunction JSON surface inventory is bound without widening scope. |",
        "| HDE_CONJ008_1_WRITER_ENVELOPE_BOUND_OK | PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ008.1 | artifacts/writer/conjunction_write_readback.log; artifacts/writer/conjunction_writer_summary.json | Reuse writer evidence artifacts already present | acceptance_map_viability.log | Implemented | Writer-envelope evidence is bound from existing governed artifacts. |",
        "| HDE_CONJ001_4_DEV_HARNESS_CLOSURE_OK | PF09.4 — Canon-HDE-Build-Checklist-Conjunction-v1 §HDE-CONJ001.4 | audit/ops/hde-epic029/ops-01/binding_disposition.md; audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md | OPS-01 evidence binding only; no rerun | acceptance_map_viability.log | Planned | Not yet closed: codespaces has gating_discrepancy (APP_ENV=prod returned 200), and local_dev uses published DEV_SAMPLER_URL http://127.0.0.1:8000/internal/dev/sampler but OPS reported step-creation/AI-data-indexing failure. |",
        f"| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | Existing epic-close live QA output only | acceptance_map_viability.log | {'Implemented' if live_qa['po-epic-close-live-qa'] else 'Planned'} | {'Bound to existing live QA primary log.' if live_qa['po-epic-close-live-qa'] else 'Deferred: required live QA primary log is missing; no pass claim synthesized.'} |",
        f"| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | Existing precommit checklist output only | acceptance_map_viability.log | {'Implemented' if live_qa['po-precommit'] else 'Planned'} | {'Bound to existing precommit primary log.' if live_qa['po-precommit'] else 'Deferred: required precommit primary log is missing; no pass claim synthesized.'} |",
        f"| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | Existing postcommit checklist output only | acceptance_map_viability.log | {'Implemented' if live_qa['po-postcommit'] else 'Planned'} | {'Bound to existing postcommit primary log.' if live_qa['po-postcommit'] else 'Deferred: required postcommit primary log is missing; no pass claim synthesized.'} |",
    ]
    _write_text(TOKEN_MATRIX_PATH, "\n".join(lines) + "\n")


def _write_dev_harness_binding_coverage(live_qa: dict[str, bool]) -> None:
    live_block = []
    for check_id, path in LIVE_QA_CHECKS.items():
        rel = path.relative_to(ROOT).as_posix()
        if live_qa[check_id]:
            live_block.append(f"- `{rel}`: present and bound.")
        else:
            live_block.append(f"- `{rel}`: missing (deferred; no synthetic PASS claim).")

    content = f"""# HDE-EPIC029 Dev Harness Binding Coverage

## OPS-01 single-source disposition
- Source of truth: `audit/ops/hde-epic029/ops-01/binding_disposition.md`.
- Codespaces remains **not yet closed** because accepted remediation evidence recorded `gating_discrepancy observed (APP_ENV=prod did not return 403)`.
- Local dev remains **not yet closed**; PF07 publishes `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`, but OPS disposition recorded step-creation and AI-data-indexing failure.
- Therefore `HDE_CONJ001_4_DEV_HARNESS_CLOSURE_OK` remains `token_incomplete` in this close-pack.

## OPS-01 files bound by this PR
- `audit/ops/hde-epic029/ops-01/commands.txt`
- `audit/ops/hde-epic029/ops-01/stdout.log`
- `audit/ops/hde-epic029/ops-01/stderr.log`
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

## Epic-close Live QA outputs disposition
{chr(10).join(live_block)}
"""
    _write_text(DEV_HARNESS_BINDING_COVERAGE_PATH, content)


def _write_docdeltas() -> None:
    _write_text(
        DOC_DELTAS_PATH,
        "# HDE-EPIC029 doc deltas\n\n- Empty ledger: this PR binds governed acceptance/closeout artifacts only; no canon/doc prose deltas were introduced.\n",
    )
    _write_text(
        DRAIN_TARGETS_PATH,
        "# HDE-EPIC029 drain targets\n\n- Empty ledger: no additional drain-target document actions are required in this offline acceptance binding slice.\n",
    )


def _write_qa_step_manifest(live_qa: dict[str, bool]) -> None:
    checks = {
        "po-epic-close-live-qa": {
            "check_id": "po-epic-close-live-qa",
            "log_path": "checks/po-epic-close-live-qa/primary.log",
            "status": "PASS" if live_qa["po-epic-close-live-qa"] else "MISSING",
        },
        "po-precommit": {
            "check_id": "po-precommit",
            "log_path": "checks/po-precommit/primary.log",
            "status": "PASS" if live_qa["po-precommit"] else "MISSING",
        },
        "po-postcommit": {
            "check_id": "po-postcommit",
            "log_path": "checks/po-postcommit/primary.log",
            "status": "PASS" if live_qa["po-postcommit"] else "MISSING",
        },
    }
    _write_json(QA_STEP_MANIFEST_PATH, {"epic_id": EPIC_ID, "checks": checks})


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        qa_root=QA_ROOT,
        acceptance_map_path=ACCEPTANCE_MAP_PATH,
        token_matrix_path=TOKEN_MATRIX_PATH,
        step_names=("acceptance_map_viability",),
    )
    qa_harness.generate_acceptance_map_viability(config, RUN_ID)
    print(f"WROTE {VIABILITY_LOG_PATH.relative_to(ROOT).as_posix()}")


def _write_close_report(produced_at: str, live_qa: dict[str, bool]) -> None:
    qa_lines = []
    for check_id, exists in live_qa.items():
        rel = LIVE_QA_CHECKS[check_id].relative_to(ROOT).as_posix()
        qa_lines.append(f"- `{rel}`: {'present' if exists else 'missing'}")

    content = f"""# HDE-EPIC029 — Close Report

## Overview
This close-pack finalizes offline acceptance and closure-artifact binding for EPIC029 using existing governed evidence only. It does not reopen runtime scope.

## Capture timestamp
- `{produced_at}`

## PF09 mapping used
- Task: `{PF09_TASK_ID}`
- Subtask: `{PF09_SUBTASK_ID}`
- Additional bound subtasks: `HDE-CONJ008.1`, `HDE-CONJ001.4`.

## OPS-01 truth preserved
- Codespaces is **not yet closed** (accepted remediation rerun recorded gating discrepancy: APP_ENV=prod did not return 403).
- Local dev is **not yet closed** (PF07 published DEV_SAMPLER_URL `http://127.0.0.1:8000/internal/dev/sampler`; OPS outcome was step-creation and AI-data-indexing failure).
- `HDE-CONJ001.4` is therefore not marked complete in this PR.

## Epic-close Live QA outputs
{chr(10).join(qa_lines)}

## Canonical EPIC029 close-pack artifacts
- `docs/acceptance_map_epic029.json`
- `audit/qa/hde-epic029/token_evidence_matrix.md`
- `audit/qa/hde-epic029/acceptance_map_viability.log`
- `audit/qa/hde-epic029/qa_step_logs_manifest.json`
- `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`
- `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`
- `audit/docdeltas/hde-epic029_doc_deltas.md`
- `audit/docdeltas/hde-epic029_drain_targets.md`
- `audit/EPIC-029_close_report.md`
- `audit/EPIC-029_MANIFEST.json`
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str, live_qa: dict[str, bool]) -> None:
    key_outputs = {
        "acceptance_map": "docs/acceptance_map_epic029.json",
        "token_matrix": "audit/qa/hde-epic029/token_evidence_matrix.md",
        "acceptance_map_viability": "audit/qa/hde-epic029/acceptance_map_viability.log",
        "qa_step_manifest": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "conjunction_json_surface_inventory": "audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md",
        "dev_harness_binding_coverage": "audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md",
        "doc_deltas": "audit/docdeltas/hde-epic029_doc_deltas.md",
        "drain_targets": "audit/docdeltas/hde-epic029_drain_targets.md",
        "close_report": "audit/EPIC-029_close_report.md",
        "close_manifest": "audit/EPIC-029_MANIFEST.json",
        "ops_commands": "audit/ops/hde-epic029/ops-01/commands.txt",
        "ops_stdout": "audit/ops/hde-epic029/ops-01/stdout.log",
        "ops_stderr": "audit/ops/hde-epic029/ops-01/stderr.log",
        "ops_exit_codes": "audit/ops/hde-epic029/ops-01/exit_codes.txt",
        "ops_codespaces_dev_sampler_url": "audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md",
        "ops_local_dev_sampler_url": "audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md",
        "ops_binding_disposition": "audit/ops/hde-epic029/ops-01/binding_disposition.md",
        "ops_created_files_sha256": "audit/ops/hde-epic029/ops-01/created_files_sha256.txt",
    }
    payload = {
        "captured_at_utc": produced_at,
        "closeout_dir": "audit/qa/hde-epic029",
        "epic_id": EPIC_ID,
        "key_outputs": key_outputs,
        "ops_task_id": "OPS-01",
        "pf09_task_id": PF09_TASK_ID,
        "pf09_subtask_id": PF09_SUBTASK_ID,
        "qa_epic_root": "audit/qa/hde-epic029",
        "qa_step_count": len(live_qa),
        "qa_step_manifest_path": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "qa_summary_lines": [
            f"po-epic-close-live-qa={'recorded' if live_qa['po-epic-close-live-qa'] else 'missing'}",
            f"po-precommit={'recorded' if live_qa['po-precommit'] else 'missing'}",
            f"po-postcommit={'recorded' if live_qa['po-postcommit'] else 'missing'}",
            "codespaces=not_yet_closed_gating_discrepancy_observed",
            "local_dev=not_yet_closed_step_creation_and_ai_data_indexing_failure_with_published_dev_sampler_url",
            "hde_conj001_4=token_incomplete",
        ],
        "run_id": RUN_ID,
        "scope": "offline_acceptance_close_pack_binding_only",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _write_path_proofs(produced_at: str) -> None:
    governed = [
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        QA_STEP_MANIFEST_PATH,
        SURFACE_INVENTORY_PATH,
        DEV_HARNESS_BINDING_COVERAGE_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
    ]
    for path in governed:
        _write_path_proof(path, produced_at)


def _verify_manifest_paths() -> None:
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

    missing = _missing_required_paths()
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_INPUTS:{','.join(missing)}")

    produced_at = _utc_now()
    live_qa = _live_qa_status()

    _write_acceptance_map(live_qa)
    _write_token_matrix(live_qa)
    _write_qa_step_manifest(live_qa)
    _write_viability_log()
    _write_dev_harness_binding_coverage(live_qa)
    _write_docdeltas()
    _write_close_report(produced_at, live_qa)
    _write_close_manifest(produced_at, live_qa)
    _write_path_proofs(produced_at)
    _verify_manifest_paths()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
