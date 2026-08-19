#!/usr/bin/env python3
"""Generate EPIC028 Reader-side acceptance ledger artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import stat as _stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC028"
EPIC_SLUG = "hde-epic028"
FINAL_MIRROR_SCHEMA_COMMAND = (
    "ci/checks/check_mirror_schema.sh",
    "artifacts/evidence_index.jsonl",
)

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic028.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"


def _path_proof_path(path: Path) -> Path:
    return path.with_name(f"{path.name}.path_proof.txt")


def _updater_graph_paths() -> tuple[Path, ...]:
    primaries = (
        ROOT / "docs/evidence/INDEX.json",
        ROOT / "docs/evidence/INDEX.sha256",
        ROOT / "artifacts/evidence_index.jsonl",
        ROOT / "artifacts/evidence_index.jsonl.sha256",
        ROOT / "audit/gates/topology/orientation_demo.txt",
    )
    registered_proofs: tuple[Path, ...] = ()
    if update_evidence_index.ROOT.absolute() == ROOT.absolute():
        registered_proofs = tuple(
            ROOT / f"{entry['discovered_physical_path']}.path_proof.txt"
            for entry in update_evidence_index._load_human_index()
        )
    return (
        *primaries,
        *(_path_proof_path(path) for path in primaries),
        *registered_proofs,
    )


def _wrapper_write_paths() -> tuple[Path, ...]:
    manifest = QA_ROOT / "qa_step_logs_manifest.json"
    viability_primary = QA_ROOT / "checks/acceptance-map-viability/primary.log"
    governed = (
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        manifest,
        viability_primary,
    )
    paths = {
        *governed,
        *(_path_proof_path(path) for path in governed),
        *_updater_graph_paths(),
    }
    return tuple(sorted(paths, key=lambda path: path.as_posix()))


class _WrapperWriteTransaction:
    """Restore the complete wrapper-owned family after any failed finalization."""

    def __init__(self) -> None:
        self._preimages: dict[Path, tuple[bytes, int] | None] = {}
        self._new_directories: set[Path] = set()

    @staticmethod
    def _relative(path: Path) -> None:
        try:
            path.absolute().relative_to(ROOT.absolute())
        except ValueError as exc:
            raise RuntimeError(f"WRAPPER_TRANSACTION_PATH_OUTSIDE_ROOT:{path}") from exc

    def _inspect_parent_chain(self, path: Path) -> None:
        parents: list[Path] = []
        parent = path.parent
        while parent != ROOT:
            self._relative(parent)
            parents.append(parent)
            parent = parent.parent
        for candidate in reversed(parents):
            if candidate.is_symlink():
                raise RuntimeError(
                    f"WRAPPER_TRANSACTION_PARENT_SYMLINK:{candidate}"
                )
            if candidate.exists():
                if not candidate.is_dir():
                    raise RuntimeError(
                        f"WRAPPER_TRANSACTION_PARENT_NOT_DIRECTORY:{candidate}"
                    )
            else:
                self._new_directories.add(candidate)

    def __enter__(self) -> "_WrapperWriteTransaction":
        if ROOT.is_symlink() or not ROOT.is_dir():
            raise RuntimeError("WRAPPER_TRANSACTION_ROOT_INVALID")
        for path in _wrapper_write_paths():
            self._relative(path)
            self._inspect_parent_chain(path)
            if path.is_symlink():
                raise RuntimeError(f"WRAPPER_TRANSACTION_TARGET_SYMLINK:{path}")
            if path.exists():
                if not path.is_file():
                    raise RuntimeError(
                        f"WRAPPER_TRANSACTION_TARGET_NOT_REGULAR:{path}"
                    )
                self._preimages[path] = (
                    path.read_bytes(),
                    _stat.S_IMODE(path.stat().st_mode),
                )
            else:
                self._preimages[path] = None
        return self

    @staticmethod
    def _restore_file(path: Path, content: bytes, mode: int) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.rollback.", dir=path.parent
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(temporary, mode)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)

    @staticmethod
    def _remove_new_target(path: Path) -> None:
        if path.is_symlink() or path.is_file():
            path.unlink(missing_ok=True)
        elif path.exists():
            path.rmdir()

    def _rollback(self) -> None:
        for path, preimage in self._preimages.items():
            if preimage is None:
                self._remove_new_target(path)
                continue
            if path.is_symlink():
                path.unlink()
            elif path.exists() and not path.is_file():
                path.rmdir()
            content, mode = preimage
            self._restore_file(path, content, mode)
        for directory in sorted(
            self._new_directories,
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            if directory.is_symlink():
                directory.unlink()
            elif directory.exists():
                directory.rmdir()

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_value is None:
            return False
        try:
            self._rollback()
        except BaseException as rollback_error:  # noqa: BLE001
            raise RuntimeError("EPIC028_WRAPPER_ROLLBACK_FAILED") from rollback_error
        return False

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
        "evidence_titles": ["artifacts/proofs/success_get.txt"],
    },
    {
        "name": "PREFS_KEYSET_10_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log",
            "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
        ],
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
        "evidence_artifacts": "artifacts/proofs/success_get.txt",
        "ci_tests_jobs": "python -m pytest -q tests/http/test_reader_a7_transport.py",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Reader 200 contract asserts six-key envelope and JSON UTF-8 content-type.",
    },
    {
        "token_name": "PREFS_KEYSET_10_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "evidence_artifacts": "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log; audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
        "ci_tests_jobs": "python -m pytest -q tests/unit/test_viewer_prefs_normalization.py::test_viewer_prefs_require_exact_magic10_weight_keys",
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "Viewer prefs exact-keyset behavior is bound to normalization evidence and a missing/extra-key validator.",
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


def _write_viability_log() -> qa_harness.ViabilityResult:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    result = qa_harness.generate_acceptance_map_viability(config, publish_governed_ledger=True)
    qa_harness.require_governed_viability(result, VIABILITY_LOG_PATH)
    return result


def _refresh_governed_bindings(
    result: qa_harness.ViabilityResult,
    produced_at: str,
) -> None:
    if result.status is not qa_harness.Status.PASS:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_{result.status.value}:{result.status_reason}"
        )
    if result.primary_log is None or result.manifest is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_MISSING")

    for path in [
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        result.primary_log,
        result.manifest,
    ]:
        _write_path_proof(path, produced_at)

    update_evidence_index.main([])
    update_evidence_index.main(["--check"])
    _run_final_mirror_schema_check()


def _run_final_mirror_schema_check() -> None:
    try:
        proc = subprocess.run(
            FINAL_MIRROR_SCHEMA_COMMAND,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise SystemExit(f"FINAL_MIRROR_SCHEMA_FAIL_TOOLING:{exc}") from exc
    if proc.returncode != 0:
        raise SystemExit(f"FINAL_MIRROR_SCHEMA_FAILED:{proc.returncode}")


def _ensure_required_paths() -> None:
    required = {
        ROOT / "docs" / "ENDPOINTS_CATALOG.json",
        ROOT / "docs" / "ENDPOINTS_CATALOG.json.sha256",
        ROOT / "artifacts" / "proofs" / "success_get.txt",
        ROOT / "artifacts" / "proofs" / "success_head.txt",
        ROOT / "artifacts" / "proofs" / "success_304.txt",
        ROOT / "artifacts" / "proofs" / "success_encoding_invariance.txt",
        ROOT / "artifacts" / "proofs" / "endpoints_env_gate_proof.log",
        ROOT / "audit" / "qa" / "hde-epic030" / "pr-01" / "invalid_viewer_prefs.log",
        ROOT / "audit" / "qa" / "hde-epic030" / "pr-01" / "zero_weight_handoff.json",
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

    with _WrapperWriteTransaction():
        _write_acceptance_map()
        _write_token_matrix()
        result = _write_viability_log()
        _refresh_governed_bindings(result, produced_at)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
