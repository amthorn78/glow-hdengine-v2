#!/usr/bin/env python3
"""Generate EPIC027 acceptance ledger and close-pack artifacts."""
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

EPIC_ID = "HDE-EPIC027"
EPIC_SLUG = "hde-epic027"
RUN_ID = "epic027-close"

ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic027.json"
TOKEN_MATRIX_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = ROOT / "audit" / "qa" / EPIC_SLUG / "acceptance_map_viability.log"
CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-027_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-027_MANIFEST.json"

TOKENS: list[dict[str, object]] = [
    {
        "name": "EVIDENCE_INDEX_UPDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "python tools/evidence/update_evidence_index.py",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_HASH_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.sha256",
            "python tools/evidence/update_evidence_index.py --check",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_MIRROR_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "ci/checks/check_mirror_schema.sh",
        ],
    },
    {
        "name": "EVIDENCE_PATHS_VALIDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
            "python tools/evidence/validate_evidence_paths.py",
        ],
    },
    {
        "name": "CI_CHECK_MIRROR_SCHEMA_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "ci/checks/check_mirror_schema.sh",
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "CI_CHECK_FINAL_LF_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "python tools/evidence/check_lf_endings.py --check",
            "audit/qa/hde-epic027/acceptance_map_viability.log",
        ],
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
    payload = {
        "epic_id": EPIC_ID,
        "tokens": TOKENS,
    }
    _write_json(ACCEPTANCE_MAP_PATH, payload)


def _write_token_matrix() -> None:
    rows = [
        "# HDE-EPIC027 Token ↔ Evidence Matrix",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| EVIDENCE_INDEX_UPDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | D4 global index/mirror refresh and hash sentinel update. |",
        "| EVIDENCE_INDEX_HASH_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.sha256 | python tools/evidence/update_evidence_index.py --check | acceptance_map_viability.log | Implemented | Hash sentinel refreshed with index update. |",
        "| EVIDENCE_INDEX_MIRROR_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | ci/checks/check_mirror_schema.sh | acceptance_map_viability.log | Implemented | Human index and machine mirror refreshed in one close slice. |",
        "| EVIDENCE_PATHS_VALIDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/validate_evidence_paths.py | acceptance_map_viability.log | Implemented | Path-proof coherence validated on governed outputs. |",
        "| CI_CHECK_MIRROR_SCHEMA_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/evidence_index.jsonl; docs/evidence/INDEX.json | ci/checks/check_mirror_schema.sh | acceptance_map_viability.log | Implemented | Mirror schema remains records-only and sorted. |",
        "| CI_CHECK_FINAL_LF_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/acceptance_map_epic027.json; audit/qa/hde-epic027/token_evidence_matrix.md | python tools/evidence/check_lf_endings.py --check | acceptance_map_viability.log | Implemented | Final-LF discipline enforced on new close-pack ledgers. |",
    ]
    _write_text(TOKEN_MATRIX_PATH, "\n".join(rows) + "\n")


def _write_close_report(produced_at: str) -> None:
    content = f"""# HDE-EPIC027 — Close Report

## Overview
HDE-CONJ009.2 closes EPIC027 at the global discipline layer by binding existing conjunction proof families into canonical acceptance ledgers and close-pack outputs.

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
Acceptance ledgers bind only canonical PF04 token names already present in the repository token registry; no non-registry token names are introduced.

## Index/Mirror coherence
This close slice refreshes and re-validates:
- `docs/evidence/INDEX.json`
- `docs/evidence/INDEX.sha256`
- `artifacts/evidence_index.jsonl`
- `artifacts/evidence_index.jsonl.sha256`
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str) -> None:
    payload = {
        "captured_at_utc": produced_at,
        "closeout_dir": "audit/qa/hde-epic027",
        "epic_id": EPIC_ID,
        "key_outputs": {
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
        },
        "qa_epic_root": "audit/qa/hde-epic027",
        "run_id": RUN_ID,
        "subtask_id": "HDE-CONJ009.2",
        "task_id": "HDE-CONJ009",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _ensure_required_paths() -> None:
    required = [
        ROOT / "artifacts/compat/identity_hash.txt",
        ROOT / "docs/ENDPOINTS_CATALOG.json",
        ROOT / "artifacts/proofs/success_get.txt",
        ROOT / "artifacts/proofs/success_head.txt",
        ROOT / "artifacts/proofs/success_304.txt",
        ROOT / "artifacts/writer/conjunction_write_readback.log",
        ROOT / "artifacts/writer/conjunction_writer_summary.json",
    ]
    missing = [p.relative_to(ROOT).as_posix() for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_PROOFS:{','.join(missing)}")


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        qa_root=VIABILITY_LOG_PATH.parent,
        acceptance_map_path=ACCEPTANCE_MAP_PATH,
        token_matrix_path=TOKEN_MATRIX_PATH,
        step_names=("acceptance_map_viability",),
    )
    qa_harness.generate_acceptance_map_viability(config, RUN_ID)
    print(f"WROTE {VIABILITY_LOG_PATH.relative_to(ROOT).as_posix()}")


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    produced_at = _utc_now()
    _ensure_required_paths()
    _write_acceptance_map()
    _write_token_matrix()
    _write_viability_log()
    _write_close_manifest(produced_at)
    _write_close_report(produced_at)

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
