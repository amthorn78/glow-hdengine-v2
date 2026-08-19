#!/usr/bin/env python3
"""Generate EPIC027 acceptance ledger and close-pack artifacts."""
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
DOC_DELTA_PATH = QA_ROOT / "00_meta" / "doc_deltas.md"

FINAL_MIRROR_SCHEMA_COMMAND = (
    "ci/checks/check_mirror_schema.sh",
    "artifacts/evidence_index.jsonl",
)

GATE_COMMANDS: list[tuple[str, list[str]]] = [
    ("gate_update_evidence_index_write", ["python", "tools/evidence/update_evidence_index.py"]),
    ("gate_orientation_demo_write", ["python", "tools/evidence/orientation_demo.py"]),
    ("gate_update_evidence_index_check", ["python", "tools/evidence/update_evidence_index.py", "--check"]),
    ("gate_orientation_demo_check", ["python", "tools/evidence/orientation_demo.py", "--check"]),
    ("gate_evidence_paths_validation", ["python", "tools/evidence/validate_evidence_paths.py"]),
    ("gate_lf_endings", ["python", "tools/evidence/check_lf_endings.py"]),
    ("gate_mirror_schema", list(FINAL_MIRROR_SCHEMA_COMMAND)),
]
GATE_CHECK_IDS = tuple(check_id for check_id, _ in GATE_COMMANDS)
GRAPH_SEAL_COMMANDS = tuple(
    tuple(command)
    for _, command in GATE_COMMANDS
)


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


def _gate_output_paths() -> tuple[Path, ...]:
    names = ("command_used.txt", "stdout.log", "stderr.log", "rc.txt", "primary.log")
    return tuple(
        QA_CHECKS_ROOT / check_id / name
        for check_id in GATE_CHECK_IDS
        for name in names
    )


def _wrapper_write_paths() -> tuple[Path, ...]:
    manifest = QA_ROOT / "qa_step_logs_manifest.json"
    viability_primary = QA_ROOT / "checks/acceptance-map-viability/primary.log"
    gate_outputs = _gate_output_paths()
    governed = (
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        manifest,
        viability_primary,
        DOC_DELTA_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
    )
    proved = (*governed, *(path for path in gate_outputs if path.name == "primary.log"))
    paths = {
        *governed,
        *gate_outputs,
        *(_path_proof_path(path) for path in proved),
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
            raise RuntimeError("EPIC027_WRAPPER_ROLLBACK_FAILED") from rollback_error
        return False

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
            "artifacts/cli/reader_dump.json",
            "artifacts/cli/reader_cli_parity.bytes",
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
            "artifacts/proofs/success_encoding_invariance.txt",
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
        ],
    },
    {
        "name": "EVIDENCE_INDEX_UPDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_HASH_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.sha256",
        ],
    },
    {
        "name": "EVIDENCE_INDEX_MIRROR_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "EVIDENCE_PATHS_VALIDATED_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "CI_CHECK_MIRROR_SCHEMA_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/evidence/INDEX.json",
            "artifacts/evidence_index.jsonl",
        ],
    },
    {
        "name": "CI_CHECK_FINAL_LF_OK",
        "owner_pf": "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "status": "implemented",
        "evidence_titles": [
            "docs/acceptance_map_epic027.json",
            "audit/qa/hde-epic027/token_evidence_matrix.md",
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
        "evidence_artifacts": "artifacts/cli/reader_dump.json; artifacts/cli/reader_cli_parity.bytes",
        "ci_tests_jobs": (
            "python -m pytest "
            "tests/http/test_reader_a7_transport.py::"
            "test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair"
        ),
        "qa_root_logs": "acceptance_map_viability.log",
        "status": "Implemented",
        "notes": "D1 parity family bound to governed artifacts and an exact current CLI/HTTP byte-parity test.",
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
        "evidence_artifacts": "artifacts/proofs/success_get.txt; artifacts/proofs/success_head.txt; artifacts/proofs/success_304.txt; artifacts/proofs/success_encoding_invariance.txt",
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
        "evidence_artifacts": "audit/gates/determinism/env_pins.log",
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
        "evidence_artifacts": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
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


def _gate_evidence_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _run_gate_command(check_id: str, command: list[str]) -> qa_harness.CheckResult:
    check_dir = QA_CHECKS_ROOT / check_id
    check_dir.mkdir(parents=True, exist_ok=True)
    cmd_text = " ".join(command)
    command_path = check_dir / "command_used.txt"
    stdout_path = check_dir / "stdout.log"
    stderr_path = check_dir / "stderr.log"
    rc_path = check_dir / "rc.txt"
    _write_text(command_path, cmd_text + "\n")
    evidence = [_gate_evidence_path(command_path)]

    try:
        proc = subprocess.run(
            tuple(command),
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        failure = f"gate command process failed: {exc}"
        _write_text(stderr_path, failure + "\n")
        evidence.append(_gate_evidence_path(stderr_path))
        return qa_harness.CheckResult(
            check_id=check_id,
            status=qa_harness.Status.FAIL_TOOLING,
            status_reason=failure,
            check_name=f"EPIC027 governed gate: {check_id}",
            command=(),
            command_provenance="Not executed",
            exit_code=None,
            output=failure,
            evidence_artifacts=tuple(evidence),
            pf_refs=(
                "PF19-Canon-Glow-QA-Guide",
                "PF27-Canon-Plan-Templates",
            ),
        )

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    _write_text(stdout_path, stdout)
    _write_text(stderr_path, stderr)
    _write_text(rc_path, f"{proc.returncode}\n")
    evidence.append(_gate_evidence_path(rc_path))
    if stdout:
        evidence.append(_gate_evidence_path(stdout_path))
    if stderr:
        evidence.append(_gate_evidence_path(stderr_path))

    status = (
        qa_harness.Status.PASS
        if proc.returncode == 0
        else qa_harness.Status.FAIL_TOOLING
    )
    reason = (
        ""
        if status is qa_harness.Status.PASS
        else f"gate command exited with status {proc.returncode}"
    )
    return qa_harness.CheckResult(
        check_id=check_id,
        status=status,
        status_reason=reason,
        check_name=f"EPIC027 governed gate: {check_id}",
        command=tuple(command),
        command_provenance=(
            "Executed exact non-shell argv; exit code returned by subprocess"
        ),
        exit_code=proc.returncode,
        output="\n".join(
            (
                f"command_capture:{_gate_evidence_path(command_path)}",
                f"stdout_capture:{_gate_evidence_path(stdout_path)}",
                f"stderr_capture:{_gate_evidence_path(stderr_path)}",
                f"exit_code_capture:{_gate_evidence_path(rc_path)}",
            )
        ),
        evidence_artifacts=tuple(evidence),
        pf_refs=(
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )


def _prepare_gate_receipt_manifest(config: qa_harness.HarnessConfig) -> Path:
    checks = qa_harness._preflight_manifest(config)
    for check_id in (*GATE_CHECK_IDS, "acceptance-map-viability"):
        checks.pop(check_id, None)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    content = qa_harness._manifest_content(checks)
    qa_harness._publish_with_rollback(
        ((manifest, content),),
        lambda: qa_harness._verify_flat_manifest(config, checks),
        repo_root=config.repo_root,
    )
    return manifest


def _run_governed_gates() -> tuple[Path, ...]:
    config = qa_harness.HarnessConfig(epic_id=EPIC_ID, repo_root=ROOT)
    _prepare_gate_receipt_manifest(config)
    results: list[qa_harness.CheckResult] = []
    for check_id, command in GATE_COMMANDS:
        result = _run_gate_command(check_id, command)
        results.append(result)
        if result.status is not qa_harness.Status.PASS:
            break

    try:
        primary_logs, _ = qa_harness.record_check_family(config, tuple(results))
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        failed_check_id = results[-1].check_id
        raise SystemExit(
            f"GATE_RECEIPT_PUBLICATION_FAILED:{failed_check_id}:{exc}"
        ) from exc
    for primary in primary_logs:
        print(f"WROTE {_gate_evidence_path(primary)}")

    final_result = results[-1]
    if final_result.status is not qa_harness.Status.PASS:
        raise SystemExit(
            "GATE_"
            f"{final_result.status.value}:{final_result.check_id}:"
            f"{final_result.status_reason}"
        )
    return primary_logs


def _seal_governed_gate_receipts() -> None:
    """Seal freshly published gate receipts before unplanned viability reads."""

    for command in GRAPH_SEAL_COMMANDS:
        try:
            proc = subprocess.run(
                command,
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
                shell=False,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            raise SystemExit(
                f"GATE_RECEIPT_GRAPH_SEAL_FAIL_TOOLING:{command[1]}:{exc}"
            ) from exc
        if proc.returncode != 0:
            raise SystemExit(
                f"GATE_RECEIPT_GRAPH_SEAL_FAILED:{command[1]}:"
                f"{proc.returncode}"
            )


def _preflight_acceptance_map_viability() -> None:
    update_evidence_index.main([])
    update_evidence_index.main(["--check"])
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=GATE_CHECK_IDS,
    )
    result, _ = qa_harness.evaluate_acceptance_map_viability(
        config,
        planned_governed_ledger=True,
    )
    if result.status is not qa_harness.Status.PASS:
        raise SystemExit(
            "ACCEPTANCE_MAP_VIABILITY_PREFLIGHT_"
            f"{result.status.value}:{result.status_reason}"
        )


def _invalidate_close_pair() -> None:
    try:
        for path in (CLOSE_REPORT_PATH, CLOSE_MANIFEST_PATH):
            path.unlink(missing_ok=True)
    except OSError as exc:
        raise SystemExit(f"CLOSE_PAIR_INVALIDATION_FAILED:{exc}") from exc
    if CLOSE_REPORT_PATH.exists() or CLOSE_MANIFEST_PATH.exists():
        raise SystemExit("CLOSE_PAIR_INVALIDATION_FAILED:stale close output remains")


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
- `audit/qa/hde-epic027/qa_step_logs_manifest.json`
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
        "acceptance_viability": "audit/qa/hde-epic027/acceptance_map_viability.log",
        "step_logs_manifest": "audit/qa/hde-epic027/qa_step_logs_manifest.json",
        "doc_deltas": "audit/qa/hde-epic027/00_meta/doc_deltas.md",
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
        ROOT / "artifacts/cli/reader_dump.json",
        ROOT / "artifacts/cli/reader_cli_parity.bytes",
        ROOT / "docs/ENDPOINTS_CATALOG.json",
        ROOT / "docs/ENDPOINTS_CATALOG.json.sha256",
        ROOT / "artifacts/proofs/endpoints_env_gate_proof.log",
        ROOT / "artifacts/proofs/success_get.txt",
        ROOT / "artifacts/proofs/success_head.txt",
        ROOT / "artifacts/proofs/success_304.txt",
        ROOT / "artifacts/proofs/success_encoding_invariance.txt",
        ROOT / "artifacts/writer/conjunction_write_readback.log",
        ROOT / "artifacts/writer/conjunction_writer_summary.json",
        ROOT / "artifacts/audit/cli/two_run_identity.log",
        ROOT / "audit/gates/determinism/env_pins.log",
        DOC_DELTA_PATH,
    ]
    missing = [p.relative_to(ROOT).as_posix() for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_PROOFS:{','.join(missing)}")


def _write_viability_log() -> qa_harness.ViabilityResult:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
    )
    result = qa_harness.generate_acceptance_map_viability(
        config,
        publish_governed_ledger=True,
    )
    ledger = qa_harness.require_governed_viability(result, VIABILITY_LOG_PATH)
    print(f"WROTE {ledger.relative_to(ROOT).as_posix()}")
    return result


def _refresh_governed_bindings(
    result: qa_harness.ViabilityResult,
    gate_primary_logs: tuple[Path, ...],
    produced_at: str,
) -> None:
    if result.status is not qa_harness.Status.PASS:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_{result.status.value}:{result.status_reason}"
        )
    if result.primary_log is None or result.manifest is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_MISSING")
    if len(gate_primary_logs) != len(GATE_CHECK_IDS):
        raise SystemExit("EPIC027_GATE_RECEIPT_FAMILY_INCOMPLETE")
    if tuple(path.parent.name for path in gate_primary_logs) != GATE_CHECK_IDS:
        raise SystemExit("EPIC027_GATE_RECEIPT_ORDER_MISMATCH")

    for path in [
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        *gate_primary_logs,
        result.primary_log,
        result.manifest,
        DOC_DELTA_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
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

    with _WrapperWriteTransaction():
        QA_ROOT.mkdir(parents=True, exist_ok=True)
        _write_acceptance_map()
        _write_token_matrix()
        _preflight_acceptance_map_viability()
        gate_primary_logs = _run_governed_gates()
        _seal_governed_gate_receipts()
        _invalidate_close_pair()
        result = _write_viability_log()
        _write_close_manifest(produced_at)
        _write_close_report(produced_at)

        _manifest_outputs_exist()
        _refresh_governed_bindings(result, gate_primary_logs, produced_at)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
