#!/usr/bin/env python3
"""Generate EPIC028 close-pack baseline artifacts under canonical audit paths."""
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

EPIC_ID = "HDE-EPIC028"
EPIC_SLUG = "hde-epic028"
RUN_ID = "epic028-close"
PF09_TASK_ID = "HDE-COAG007"
PF09_SUBTASK_ID = "HDE-COAG007.3"

ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic028.json"
TOKEN_MATRIX_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "acceptance_map_viability.log"
QA_STEP_MANIFEST_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "qa_step_logs_manifest.json"
PO010_SUMMARY_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "checks" / "po-010" / "final_summary.txt"

CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-028_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-028_MANIFEST.json"
OPS_SHA256_PATH = ROOT / "audit" / "ops" / EPIC_SLUG / "ops-01" / "created_files_sha256.txt"


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


def _ensure_required_paths() -> None:
    required = [
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        QA_STEP_MANIFEST_PATH,
        QA_STEP_MANIFEST_PATH.with_suffix(".json.path_proof.txt"),
        PO010_SUMMARY_PATH,
    ]
    missing = [p.relative_to(ROOT).as_posix() for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_INPUTS:{','.join(missing)}")


def _read_po010_lines() -> list[str]:
    lines = [line.strip() for line in PO010_SUMMARY_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    return lines


def _read_step_manifest() -> dict[str, object]:
    payload = json.loads(QA_STEP_MANIFEST_PATH.read_text(encoding="utf-8"))
    checks = payload.get("checks", {})
    if not isinstance(checks, dict):
        raise SystemExit("INVALID_QA_STEP_MANIFEST:checks_must_be_object")
    return payload


def _write_close_report(produced_at: str, qa_manifest: dict[str, object], po010_lines: list[str]) -> None:
    checks = qa_manifest.get("checks", {})
    ordered_check_ids = sorted(str(check_id) for check_id in checks.keys())
    check_lines = "\n".join(f"- `audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log`" for check_id in ordered_check_ids)
    po010_block = "\n".join(f"- `{line}`" for line in po010_lines)

    content = f"""# HDE-EPIC028 — Close Report

## Overview
This close-pack is a packaging and evidence-surfacing baseline only. It does not re-open implementation scope, does not modify QA verdicts, and does not assert merge provenance.

## Capture timestamp
- `{produced_at}`

## PF09 mapping used
- Task: `{PF09_TASK_ID}`
- Subtask: `{PF09_SUBTASK_ID}`
- Basis: PF09 row generalizes close-pack adjacency for `audit/EPIC-<NNN>_close_report.md` and `audit/EPIC-<NNN>_MANIFEST.json`.

## Canonical EPIC028 close-pack artifacts
- `audit/EPIC-028_close_report.md`
- `audit/EPIC-028_MANIFEST.json`
- `audit/EPIC-028_close_report.md.path_proof.txt`
- `audit/EPIC-028_MANIFEST.json.path_proof.txt`

## QA evidence posture (reused; unchanged)
- `docs/acceptance_map_epic028.json`
- `audit/qa/hde-epic028/token_evidence_matrix.md`
- `audit/qa/hde-epic028/acceptance_map_viability.log`
- `audit/qa/hde-epic028/qa_step_logs_manifest.json`
- `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`

## QA RCA summary (embedded)
- PO-010 final summary confirms repo-supported completion only and no formal close-pack claim by the QA step.
{po010_block}

## Step-log inventory referenced from qa_step_logs_manifest.json
{check_lines}
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str, qa_manifest: dict[str, object], po010_lines: list[str]) -> None:
    key_outputs = {
        "acceptance_map": "docs/acceptance_map_epic028.json",
        "token_matrix": f"audit/qa/{EPIC_SLUG}/token_evidence_matrix.md",
        "acceptance_map_viability": f"audit/qa/{EPIC_SLUG}/acceptance_map_viability.log",
        "qa_step_manifest": f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json",
        "qa_step_manifest_path_proof": f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json.path_proof.txt",
        "po010_final_summary": f"audit/qa/{EPIC_SLUG}/checks/po-010/final_summary.txt",
        "close_report": "audit/EPIC-028_close_report.md",
        "close_manifest": "audit/EPIC-028_MANIFEST.json",
        "ops_created_files_sha256": f"audit/ops/{EPIC_SLUG}/ops-01/created_files_sha256.txt",
    }
    payload = {
        "captured_at_utc": produced_at,
        "closeout_dir": f"audit/qa/{EPIC_SLUG}",
        "epic_id": EPIC_ID,
        "key_outputs": key_outputs,
        "ops_task_id": "OPS-01",
        "pf09_subtask_id": PF09_SUBTASK_ID,
        "pf09_task_id": PF09_TASK_ID,
        "qa_epic_root": f"audit/qa/{EPIC_SLUG}",
        "qa_step_count": len(qa_manifest.get("checks", {})),
        "qa_step_manifest_path": f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json",
        "qa_summary_lines": po010_lines,
        "run_id": RUN_ID,
        "scope": "packaging_and_evidence_surfacing_only",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _write_ops_checksums() -> None:
    targets = [
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
        CLOSE_REPORT_PATH.with_suffix(CLOSE_REPORT_PATH.suffix + ".path_proof.txt"),
        CLOSE_MANIFEST_PATH.with_suffix(CLOSE_MANIFEST_PATH.suffix + ".path_proof.txt"),
    ]
    lines = []
    for path in targets:
        rel = path.relative_to(ROOT).as_posix()
        lines.append(f"{_sha256(path)}  {rel}")
    _write_text(OPS_SHA256_PATH, "\n".join(sorted(lines)) + "\n")


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

    qa_manifest = _read_step_manifest()
    po010_lines = _read_po010_lines()

    _write_close_report(produced_at, qa_manifest, po010_lines)
    _write_close_manifest(produced_at, qa_manifest, po010_lines)
    _write_path_proof(CLOSE_REPORT_PATH, produced_at)
    _write_path_proof(CLOSE_MANIFEST_PATH, produced_at)
    _write_ops_checksums()
    _manifest_outputs_exist()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
