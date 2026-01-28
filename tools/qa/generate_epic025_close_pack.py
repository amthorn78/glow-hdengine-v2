#!/usr/bin/env python3
"""Generate EPIC025 close-pack artifacts and QA step logs manifest."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

EPIC_ID = "HDE-EPIC025"
QA_ROOT = ROOT / "audit" / "qa" / "hde-epic025"
QA_CHECKS_ROOT = QA_ROOT / "checks"
DOC_DELTAS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic025_doc_deltas.md"
CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-025_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-025_MANIFEST.json"
QA_STEP_MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"

CHECK_IDS = (
    "preflight_e1_http_compat",
    "preflight_e2_endpoint_catalog",
    "preflight_e3_cli_entrypoint",
    "preflight_e4_json_emitter_coupling",
    "preflight_e5_a7_transport_invariants",
    "preflight_e6_evidence_index_mirror",
    "preflight_p3_token_roster",
    "preflight_p4_evidence_endpoints",
    "preflight_p6_rails_closure",
    "gate_canonical_json",
    "gate_evidence_index_update",
    "gate_evidence_paths_validation",
    "gate_mirror_schema",
    "gate_lf_endings",
)


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _required_paths() -> list[Path]:
    return [
        ROOT / "docs" / "ENDPOINTS_CATALOG.json",
        ROOT / "docs" / "ENDPOINTS_CATALOG.json.sha256",
        ROOT / "artifacts" / "proofs" / "endpoints_env_gate_proof.log",
        ROOT / "artifacts" / "proofs" / "success_get.txt",
        ROOT / "artifacts" / "proofs" / "success_head.txt",
        ROOT / "artifacts" / "proofs" / "success_304.txt",
        ROOT / "artifacts" / "proofs" / "success_writers_errors.txt",
        ROOT / "docs" / "evidence" / "INDEX.json",
        ROOT / "docs" / "evidence" / "INDEX.sha256",
        ROOT / "artifacts" / "evidence_index.jsonl",
        QA_STEP_MANIFEST_PATH,
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_check_log.ndjson",
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_compare_log.ndjson",
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_structured_record.json",
    ] + [QA_CHECKS_ROOT / check_id / "primary.log" for check_id in CHECK_IDS]


def _optional_paths() -> list[Path]:
    return [
        ROOT / "artifacts" / "proofs" / "encoding_invariance.txt",
        ROOT / "artifacts" / "cli" / "showcompat" / "stdout.json",
        ROOT / "artifacts" / "cli" / "showcompat" / "stdout.json.sha256",
        ROOT / "artifacts" / "cli" / "showcompat" / "args.json",
        ROOT / "artifacts" / "cli" / "guards" / "serializer_grep_guard.log",
    ]


def _ensure_paths(paths: Iterable[Path]) -> None:
    missing = [path.as_posix() for path in paths if not path.exists()]
    if missing:
        raise SystemExit(f"MISSING:{','.join(sorted(missing))}")


def write_step_manifest(produced_at: str) -> None:
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    QA_CHECKS_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        check_id: {
            "check_id": check_id,
            "log_path": f"checks/{check_id}/primary.log",
        }
        for check_id in CHECK_IDS
    }
    content = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    _write_text(QA_STEP_MANIFEST_PATH, content)
    rel = QA_STEP_MANIFEST_PATH.relative_to(ROOT).as_posix()
    stat = QA_STEP_MANIFEST_PATH.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256(QA_STEP_MANIFEST_PATH),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def write_doc_deltas() -> None:
    _write_text(DOC_DELTAS_PATH, "Doc Deltas: None\n")


def write_close_report() -> None:
    content = """# HDE-EPIC025 — Close Report

## Overview
PR-01 through PR-04 close the evidence discipline loop for audit endpoints and QA rails. Deliverables include the endpoint catalog refresh, A7 reader transport proofs, CLI/showcompat guardrails, and the EPIC025 close-pack with governed gate logs.

## PR summary
- PR-01: Endpoint catalog coverage and audit surface baseline.
- PR-02: Reader A7 transport invariants and proof artifacts.
- PR-03: CLI/showcompat guardrails and serializer coupling proofs.
- PR-04: Evidence discipline closure (QA step logs, canonical JSON gate, evidence index/mirror checks, and close pack).

## Deferrals
Dev HTTP Harness (single-home) and Writer Surfaces (API) are deferred to HDE-EPIC026. This epic makes no acceptance claims for those deferred surfaces.

## Key outputs
See the EPIC025 close manifest `key_outputs` for the governed evidence paths.
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _key_output_entries() -> dict[str, str]:
    outputs: dict[str, str] = {
        "endpoint_catalog": "docs/ENDPOINTS_CATALOG.json",
        "endpoint_catalog_sha256": "docs/ENDPOINTS_CATALOG.json.sha256",
        "endpoints_env_gate_proof": "artifacts/proofs/endpoints_env_gate_proof.log",
        "success_get": "artifacts/proofs/success_get.txt",
        "success_head": "artifacts/proofs/success_head.txt",
        "success_304": "artifacts/proofs/success_304.txt",
        "success_writers_errors": "artifacts/proofs/success_writers_errors.txt",
        "evidence_index": "docs/evidence/INDEX.json",
        "evidence_index_sha256": "docs/evidence/INDEX.sha256",
        "evidence_index_mirror": "artifacts/evidence_index.jsonl",
        "qa_step_manifest": "audit/qa/hde-epic025/qa_step_logs_manifest.json",
        "json_gate_check_log": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
        "json_gate_compare_log": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
        "json_gate_structured_record": "audit/gates/json_gate/canonical/json_gate_structured_record.json",
        "close_report": "audit/EPIC-025_close_report.md",
        "close_manifest": "audit/EPIC-025_MANIFEST.json",
        "doc_deltas": "audit/docdeltas/hde-epic025_doc_deltas.md",
    }
    for check_id in CHECK_IDS:
        outputs[f"qa_log_{check_id}"] = f"audit/qa/hde-epic025/checks/{check_id}/primary.log"

    optional_map = {
        "encoding_invariance": "artifacts/proofs/encoding_invariance.txt",
        "showcompat_stdout_json": "artifacts/cli/showcompat/stdout.json",
        "showcompat_stdout_sha256": "artifacts/cli/showcompat/stdout.json.sha256",
        "showcompat_args_json": "artifacts/cli/showcompat/args.json",
        "serializer_grep_guard_log": "artifacts/cli/guards/serializer_grep_guard.log",
    }
    for key, rel in optional_map.items():
        if (ROOT / rel).exists():
            outputs[key] = rel
    return outputs


def write_close_manifest(captured_at: str) -> None:
    payload = {
        "captured_at_utc": captured_at,
        "closeout_dir": "audit/qa/hde-epic025",
        "epic_id": EPIC_ID,
        "key_outputs": _key_output_entries(),
        "qa_epic_root": "audit/qa/hde-epic025",
        "qa_root": "audit/qa/hde-epic025",
        "qa_step_manifest_path": "audit/qa/hde-epic025/qa_step_logs_manifest.json",
        "run_id": "epic025-close",
    }
    content = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    _write_text(CLOSE_MANIFEST_PATH, content)


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    produced_at = _utc_now()
    write_step_manifest(produced_at)
    write_doc_deltas()
    write_close_report()
    _ensure_paths(_required_paths())
    write_close_manifest(produced_at)
    _ensure_paths(_required_paths())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
