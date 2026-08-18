#!/usr/bin/env python3
"""Generate EPIC028 Reader-side acceptance ledger artifacts."""
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

EPIC_ID = "HDE-EPIC028"
EPIC_SLUG = "hde-epic028"
RUN_ID = "epic028-reader-ledger"

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic028.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"

TOKENS: list[dict[str, object]] = [
    {
        "name": "A7_GET_QUOTED_ETAG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["artifacts/proofs/success_get.txt"],
    },
    {
        "name": "A7_HEAD_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["artifacts/proofs/success_head.txt", "artifacts/proofs/success_get.txt"],
    },
    {
        "name": "A7_304_OMITS_CT_CL_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["artifacts/proofs/success_304.txt"],
    },
    {
        "name": "A7_VARY_AUTH_AE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["artifacts/proofs/success_get.txt", "artifacts/proofs/success_head.txt"],
    },
    {
        "name": "A7_ENCODING_INVARIANCE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "artifacts/proofs/success_encoding_invariance.txt",
        ],
    },
    {
        "name": "ENDPOINTS_CATALOG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["docs/ENDPOINTS_CATALOG.json", "docs/ENDPOINTS_CATALOG.json.sha256"],
    },
    {
        "name": "ENDPOINTS_CATALOG_ENV_GATE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["docs/ENDPOINTS_CATALOG.json", "artifacts/proofs/endpoints_env_gate_proof.log"],
    },
    {
        "name": "READER_200_CTYPE_JSON_UTF8_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["artifacts/proofs/success_get.txt", "tests/http/test_reader_a7_transport.py"],
    },
    {
        "name": "MAGIC10_DOMAIN_CLOSED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["catalog/magic10.json", "tests/categories/test_registry_and_purity.py"],
    },
    {
        "name": "PREFS_KEYSET_10_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": ["tests/http/test_compat_endpoint_contract.py", "engine/compat/categories.py"],
    },
]

TOKEN_MATRIX_ROWS: list[dict[str, str]] = [
    {
        "token_name": "A7_GET_QUOTED_ETAG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Reader A7 GET proof bound on cataloged /reader success route.",
    },
    {
        "token_name": "A7_HEAD_PARITY_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_head.txt; artifacts/proofs/success_get.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "HEAD parity proof reuses existing governed captures.",
    },
    {
        "token_name": "A7_304_OMITS_CT_CL_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_304.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "304 omission of Content-Type/Content-Length is preserved.",
    },
    {
        "token_name": "A7_VARY_AUTH_AE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt; artifacts/proofs/success_head.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Vary header parity remains Authorization, Accept-Encoding.",
    },
    {
        "token_name": "A7_ENCODING_INVARIANCE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_encoding_invariance.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Encoding invariance capture is retained under governed proof path.",
    },
    {
        "token_name": "ENDPOINTS_CATALOG_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/ENDPOINTS_CATALOG.json; docs/ENDPOINTS_CATALOG.json.sha256",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_endpoint_catalog.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Endpoint catalog single-home inventory is validated.",
    },
    {
        "token_name": "ENDPOINTS_CATALOG_ENV_GATE_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "docs/ENDPOINTS_CATALOG.json; artifacts/proofs/endpoints_env_gate_proof.log",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_endpoint_catalog.py tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Catalog env-gate representation and blocked-call proof are both present.",
    },
    {
        "token_name": "READER_200_CTYPE_JSON_UTF8_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "artifacts/proofs/success_get.txt; tests/http/test_reader_a7_transport.py",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Reader 200 contract asserts six-key envelope and JSON UTF-8 content-type.",
    },
    {
        "token_name": "MAGIC10_DOMAIN_CLOSED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "catalog/magic10.json; tests/categories/test_registry_and_purity.py",
        "ci_tests_jobs": "python -m pytest -q tests/categories/test_registry_and_purity.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Magic10 registry/domain closure proof reused from existing category tests.",
    },
    {
        "token_name": "PREFS_KEYSET_10_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "engine/compat/categories.py; tests/http/test_compat_endpoint_contract.py",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_compat_endpoint_contract.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Viewer prefs keyset contract is bound to compat endpoint contract tests.",
    },
]


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


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


def _write_acceptance_map() -> None:
    _write_json(ACCEPTANCE_MAP_PATH, {"epic_id": EPIC_ID, "tokens": TOKENS})


def _write_token_matrix() -> None:
    lines = [
        "# HDE-EPIC028 Token ↔ Evidence Matrix",
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


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    result = qa_harness.generate_acceptance_map_viability(config, publish_governed_ledger=True)
    qa_harness.require_governed_viability(result, VIABILITY_LOG_PATH)


def _ensure_required_paths() -> None:
    required = {
        ROOT / "docs" / "ENDPOINTS_CATALOG.json",
        ROOT / "docs" / "ENDPOINTS_CATALOG.json.sha256",
        ROOT / "artifacts" / "proofs" / "success_get.txt",
        ROOT / "artifacts" / "proofs" / "success_head.txt",
        ROOT / "artifacts" / "proofs" / "success_304.txt",
        ROOT / "artifacts" / "proofs" / "success_encoding_invariance.txt",
        ROOT / "artifacts" / "proofs" / "endpoints_env_gate_proof.log",
        ROOT / "catalog" / "magic10.json",
        ROOT / "engine" / "compat" / "categories.py",
        ROOT / "tests" / "http" / "test_reader_a7_transport.py",
        ROOT / "tests" / "http" / "test_compat_endpoint_contract.py",
        ROOT / "tests" / "categories" / "test_registry_and_purity.py",
    }
    missing = [path.relative_to(ROOT).as_posix() for path in sorted(required) if not path.exists()]
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_PROOFS:{','.join(missing)}")


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

    for path in [ACCEPTANCE_MAP_PATH, TOKEN_MATRIX_PATH, VIABILITY_LOG_PATH]:
        _write_path_proof(path, produced_at)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
