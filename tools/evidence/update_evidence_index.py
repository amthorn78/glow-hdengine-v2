#!/usr/bin/env python3
"""Harden the evidence index, hash sentinel, and machine mirror.

Discovery summary (PR2 — EPIC017):
- INDEX + sentinel already existed under docs/evidence with loose schema (title/path/proof).
- The machine mirror lived at artifacts/evidence_index.jsonl with the required keys already,
  enforced partially by ci/checks/check_mirror_schema.sh.
- Path-proofs were scattered as ``*.path_proof.txt`` files with path/sha/size/mtime lines
  written by helpers such as tools/evidence/generate_rails_closed_phase1.py.
- No topology orientation demo artifact existed yet; CI only checked the sentinel hash and
  mirror schema ordering.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import hashlib
import json
import os
import stat as _stat
import sys
import tempfile
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
HASH_SENTINEL = ROOT / "docs/evidence/INDEX.sha256"
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"
MIRROR_REL = MIRROR_PATH.relative_to(ROOT).as_posix()
MIRROR_SHA_PATH = ROOT / "artifacts/evidence_index.jsonl.sha256"
ORIENTATION_PATH = ROOT / "audit/gates/topology/orientation_demo.txt"
SANITY_LOG_REL = "audit/gates/sanity_pipeline/sanity_pipeline.log"
SANITY_LOG_KEY = ("sanity.pipeline.log", SANITY_LOG_REL)
EPIC020_BUNDLE_DIR = ROOT / "artifacts" / "epic020" / "bundles"
EPIC020_ACCEPTANCE_MAP = ROOT / "docs" / "acceptance_map_epic020.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import (  # noqa: E402
    DETERMINISM_ENV_PINS,
    ensure_determinism_env,
)


class _WriteTransaction:
    """Restore every updater-owned write when convergence or validation fails."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.files: dict[Path, tuple[bytes, int, int, int] | None] = {}
        self.directories: dict[Path, tuple[int, int, int] | None] = {}

    def __enter__(self) -> "_WriteTransaction":
        global _ACTIVE_WRITE_TRANSACTION
        if _ACTIVE_WRITE_TRANSACTION is not None:
            raise RuntimeError("nested evidence-index write transaction")
        _ACTIVE_WRITE_TRANSACTION = self
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        global _ACTIVE_WRITE_TRANSACTION
        _ACTIVE_WRITE_TRANSACTION = None
        if exc_value is None:
            return False
        try:
            self.rollback()
        except BaseException as rollback_error:  # noqa: BLE001
            failure = RuntimeError("EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED")
            failure.add_note(f"rollback error: {rollback_error}")
            raise failure from exc_value
        return False

    def _assert_scoped(self, path: Path) -> None:
        try:
            relative = path.relative_to(self.root)
        except ValueError as exc:
            raise RuntimeError(f"transaction path escapes repository: {path}") from exc
        if ".." in relative.parts:
            raise RuntimeError(f"transaction path escapes repository: {path}")

    def _capture_directory_chain(self, path: Path) -> None:
        chain: list[Path] = []
        current = path.parent
        while True:
            self._assert_scoped(current)
            chain.append(current)
            if current == self.root:
                break
            current = current.parent
        for directory in reversed(chain):
            if directory in self.directories:
                continue
            if directory.is_symlink():
                raise SystemExit(f"ALIASED_TRANSACTION_DIRECTORY:{directory}")
            if not directory.exists():
                self.directories[directory] = None
                continue
            if not directory.is_dir():
                raise SystemExit(f"NON_DIRECTORY_TRANSACTION_PARENT:{directory}")
            metadata = directory.stat()
            self.directories[directory] = (
                _stat.S_IMODE(metadata.st_mode),
                metadata.st_atime_ns,
                metadata.st_mtime_ns,
            )

    def capture(self, path: Path) -> None:
        self._assert_scoped(path)
        if path in self.files:
            return
        self._capture_directory_chain(path)
        if path.is_symlink():
            raise SystemExit(f"ALIASED_TRANSACTION_FILE:{path}")
        if not path.exists():
            self.files[path] = None
            return
        if not path.is_file():
            raise SystemExit(f"NON_FILE_TRANSACTION_TARGET:{path}")
        metadata = path.stat()
        self.files[path] = (
            path.read_bytes(),
            _stat.S_IMODE(metadata.st_mode),
            metadata.st_atime_ns,
            metadata.st_mtime_ns,
        )

    def rollback(self) -> None:
        for path, preimage in self.files.items():
            if preimage is None:
                if path.is_symlink() or path.is_file():
                    path.unlink()
                elif path.exists():
                    raise RuntimeError(f"transaction target became non-file: {path}")
                continue
            body, mode, atime_ns, mtime_ns = preimage
            if path.is_symlink() or (path.exists() and not path.is_file()):
                raise RuntimeError(f"transaction target changed type: {path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            os.chmod(path, mode, follow_symlinks=False)
            os.utime(
                path,
                ns=(atime_ns, mtime_ns),
                follow_symlinks=False,
            )

        missing_directories = sorted(
            (
                path
                for path, preimage in self.directories.items()
                if preimage is None
            ),
            key=lambda path: len(path.parts),
            reverse=True,
        )
        for directory in missing_directories:
            if directory.exists():
                directory.rmdir()

        existing_directories = sorted(
            (
                (path, preimage)
                for path, preimage in self.directories.items()
                if preimage is not None
            ),
            key=lambda item: len(item[0].parts),
            reverse=True,
        )
        for directory, preimage in existing_directories:
            assert preimage is not None
            mode, atime_ns, mtime_ns = preimage
            os.chmod(directory, mode, follow_symlinks=False)
            os.utime(
                directory,
                ns=(atime_ns, mtime_ns),
                follow_symlinks=False,
            )


_ACTIVE_WRITE_TRANSACTION: _WriteTransaction | None = None


class _StagedDeletion:
    """Explicit final-model marker for a path that must be absent."""


_STAGED_DELETION = _StagedDeletion()


@dataclasses.dataclass
class _StagedView:
    """Coherent read/write view of the updater's final, unpublished model."""

    root: Path
    produced_default: str
    changes: dict[Path, bytes | _StagedDeletion] = dataclasses.field(
        default_factory=dict
    )

    def _assert_scoped(self, path: Path) -> None:
        try:
            path.relative_to(self.root)
        except ValueError as exc:
            raise RuntimeError(f"staged path escapes repository: {path}") from exc

    def exists(self, path: Path) -> bool:
        self._assert_scoped(path)
        staged = self.changes.get(path)
        if staged is _STAGED_DELETION:
            return False
        if isinstance(staged, bytes):
            return True
        return path.exists()

    def read_bytes(self, path: Path) -> bytes:
        self._assert_scoped(path)
        staged = self.changes.get(path)
        if staged is _STAGED_DELETION:
            raise FileNotFoundError(f"staged deletion has no bytes: {path}")
        if isinstance(staged, bytes):
            return staged
        return path.read_bytes()

    def size_bytes(self, path: Path) -> int:
        return len(self.read_bytes(path))

    def proof_mtime(self, path: Path) -> float:
        """Return stable provenance without requiring an inode for additions."""

        self._assert_scoped(path)
        if path.exists():
            return path.stat().st_mtime
        if self.exists(path):
            return _parse_utc_iso8601(self.produced_default).timestamp()
        raise FileNotFoundError(path)

    def stage_bytes(self, path: Path, content: bytes) -> None:
        self._assert_scoped(path)
        self.changes[path] = content

    def stage_deletion(self, path: Path) -> None:
        self._assert_scoped(path)
        self.changes[path] = _STAGED_DELETION


_STAGED_VIEW: _StagedView | None = None


def _read_bytes(path: Path) -> bytes:
    if _STAGED_VIEW is not None:
        return _STAGED_VIEW.read_bytes(path)
    return path.read_bytes()


def _path_exists(path: Path) -> bool:
    if _STAGED_VIEW is not None:
        return _STAGED_VIEW.exists(path)
    return path.exists()


def _size_bytes(path: Path) -> int:
    if _STAGED_VIEW is not None:
        return _STAGED_VIEW.size_bytes(path)
    return path.stat().st_size


def _proof_mtime(path: Path, *, default_produced_at: str) -> float:
    if _STAGED_VIEW is not None:
        return _STAGED_VIEW.proof_mtime(path)
    if path.exists():
        return path.stat().st_mtime
    return _parse_utc_iso8601(default_produced_at).timestamp()


def _capture_transaction_preimage(path: Path) -> None:
    if _ACTIVE_WRITE_TRANSACTION is not None:
        _ACTIVE_WRITE_TRANSACTION.capture(path)


def _assert_unaliased_write_path(path: Path) -> None:
    """Reject aliased updater outputs before any unchanged-byte fast path."""

    if _STAGED_VIEW is not None:
        root = _STAGED_VIEW.root
    elif _ACTIVE_WRITE_TRANSACTION is not None:
        root = _ACTIVE_WRITE_TRANSACTION.root
    else:
        root = ROOT
        if path.is_absolute() and not path.is_relative_to(root):
            # Standalone helper tests and callers may use an absolute scratch
            # path without an active repository transaction. Preserve that
            # behavior while still checking its complete lexical parent chain.
            root = Path(path.anchor)
    scoped_path = path if path.is_absolute() else root / path
    try:
        relative = scoped_path.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"transaction path escapes repository: {path}") from exc
    if ".." in relative.parts:
        raise RuntimeError(f"transaction path escapes repository: {path}")
    if scoped_path == root:
        raise RuntimeError(f"transaction path names repository root: {path}")
    if scoped_path.is_symlink():
        raise SystemExit(f"ALIASED_TRANSACTION_FILE:{scoped_path}")
    current = scoped_path.parent
    while True:
        if current.is_symlink():
            raise SystemExit(f"ALIASED_TRANSACTION_DIRECTORY:{current}")
        if current == root:
            break
        current = current.parent


BASELINE_ENTRIES: list[dict[str, object]] = [
    {
        "artifact_key": "registry.registry_report",
        "discovered_physical_path": "artifacts/registry/registry_report.json",
        "record_type": "registry_report",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "sanity.pipeline.log",
        "discovered_physical_path": "audit/gates/sanity_pipeline/sanity_pipeline.log",
        "record_type": "sanity_log",
        "schema_version": "1.0",
    },
]
EPIC022_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic022.close_report",
        "discovered_physical_path": "audit/EPIC-022_close_report.md",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.manifest",
        "discovered_physical_path": "audit/EPIC-022_MANIFEST.json",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic022/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic022.json",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "audit.cli.two_run_identity",
        "discovered_physical_path": "artifacts/audit/cli/two_run_identity.log",
        "record_type": "audit_cli_log",
    },
]
EPIC024_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic024.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic024.json",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic024/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic024/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic024/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic024/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic024_doc_deltas.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.close_report",
        "discovered_physical_path": "audit/EPIC-024_close_report.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.manifest",
        "discovered_physical_path": "audit/EPIC-024_MANIFEST.json",
        "epic_id": "HDE-EPIC024",
    },
]

EPIC027_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic027.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic027.json",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic027/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic027/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic027/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.close_report",
        "discovered_physical_path": "audit/EPIC-027_close_report.md",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.manifest",
        "discovered_physical_path": "audit/EPIC-027_MANIFEST.json",
        "epic_id": "HDE-EPIC027",
    },
]

EPIC028_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic028.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic028.json",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic028/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic028/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic028/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.close_report",
        "discovered_physical_path": "audit/EPIC-028_close_report.md",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.manifest",
        "discovered_physical_path": "audit/EPIC-028_MANIFEST.json",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.ops01.created_files_sha256",
        "discovered_physical_path": "audit/ops/hde-epic028/ops-01/created_files_sha256.txt",
        "epic_id": "HDE-EPIC028",
    },
]



EPIC031_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic031.pr01.policies_pinned",
        "discovered_physical_path": "artifacts/vendor/policies_pinned.md",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr01_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T15:38:37Z",
        "notes": "EPIC031 PR-01 pinned SAFE rails provider policy evidence",
    },
    {
        "artifact_key": "vendor.retry_after_parse",
        "discovered_physical_path": "artifacts/vendor/retry_after_parse.log",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr01_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T15:38:37Z",
        "notes": "EPIC031 PR-01 Retry-After deterministic parse evidence",
    },
    {
        "artifact_key": "epic031.pr01.open_rails_policy_proof",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr01_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T15:38:37Z",
        "notes": "EPIC031 PR-01 open rails policy proof",
    },
    {
        "artifact_key": "epic031.pr01.retry_backoff_429_proof",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr01_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T15:38:37Z",
        "notes": "EPIC031 PR-01 retry, backoff, and 429 typed proof",
    },
    {
        "artifact_key": "epic031.pr01.closed_default_open_exception_rails",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr01_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T15:38:37Z",
        "notes": "EPIC031 PR-01 closed default and open exception rails proof",
    },
]

EPIC031_PR02_SUPERSEDED_INDEX_KEYS = {
    ("epic031.pr02.keys_only_sample", "artifacts/logs/keys_only.sample.jsonl"),
    ("epic031.pr02.rails_open_scope", "artifacts/ops/rails_open_scope.txt"),
}

EPIC031_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic031.pr02.vendor_keys_only_sample",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr02_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T16:20:00Z",
        "notes": "EPIC031 PR-02 SAFE rails keys-only vendor log sample",
        "tokens": ["VENDOR_NO_PAYLOAD_LOGGING_OK", "ENV_RAILS_POLICY_OK"],
    },
    {
        "artifact_key": "epic031.pr02.vendor_rails_scope",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr02_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T16:20:00Z",
        "notes": "EPIC031 PR-02 local deterministic vendor rails scope for log posture",
        "tokens": ["ENV_RAILS_POLICY_OK"],
    },
    {
        "artifact_key": "epic031.pr02.keys_only_log_redaction",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr02_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T16:20:00Z",
        "notes": "EPIC031 PR-02 keys-only payload and secret redaction proof",
        "tokens": ["VENDOR_NO_PAYLOAD_LOGGING_OK"],
    },
    {
        "artifact_key": "epic031.pr02.bounded_label_observability",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-02/bounded_label_observability.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr02_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T16:20:00Z",
        "notes": "EPIC031 PR-02 bounded label observability proof",
        "tokens": ["VENDOR_NO_PAYLOAD_LOGGING_OK", "ENV_RAILS_POLICY_OK"],
    },
    {
        "artifact_key": "epic031.pr02.secret_redaction_scan",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-02/secret_redaction_scan.log",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr02_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T16:20:00Z",
        "notes": "EPIC031 PR-02 deterministic redaction scan log",
        "tokens": ["VENDOR_NO_PAYLOAD_LOGGING_OK", "TESTS_PASS_OK"],
    },
]

EPIC031_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic031.pr03.evidence_family_map",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-03/evidence_family_map.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr03_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T17:05:00Z",
        "notes": "EPIC031 PR-03 SAFE rails evidence family map for governed index coherence",
    },
    {
        "artifact_key": "epic031.pr03.safe_rails_evidence_coherence",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr03_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T17:05:00Z",
        "notes": "EPIC031 PR-03 SAFE rails Human Index, Machine Mirror, hash, and path-proof coherence evidence",
    },
    {
        "artifact_key": "epic031.pr03.evidence_refresh_log",
        "discovered_physical_path": "audit/qa/hde-epic031/pr-03/evidence_refresh.log",
        "epic_id": "HDE-EPIC031",
        "record_type": "epic031_pr03_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-05-10T17:05:00Z",
        "notes": "EPIC031 PR-03 evidence refresh log with generator outcomes and validation command roster",
    },
]

EPIC030_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic030.pr02.dev_sampler_http_headers",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr02_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-02 dev sampler harness HTTP headers evidence",
    },
    {
        "artifact_key": "epic030.pr02.dev_sampler_http_body",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr02_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-02 dev sampler harness HTTP body evidence",
    },
    {
        "artifact_key": "epic030.pr02.dev_sampler_two_run_identity",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr02_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-02 dev sampler two-run identity evidence",
    },
    {
        "artifact_key": "epic030.pr02.dev_sampler_seed_only",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr02_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-02 dev sampler seed-only metadata evidence",
    },
]

EPIC030_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic030.pr03.compat_parity_binding",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-03/compat_parity_binding.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr03_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-03 compat AB↔BA parity binding evidence for HDE-DISS002.6",
    },
    {
        "artifact_key": "epic030.pr03.compat_identity_binding",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-03/compat_identity_binding.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr03_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-03 compat identity-hash binding evidence for HDE-DISS002.6",
    },
    {
        "artifact_key": "epic030.pr03.category_order_binding",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-03/category_order_binding.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr03_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-03 category-order and narrative key-table binding evidence for HDE-DISS002.6",
    },
]

EPIC030_PR04_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic030.pr04.band_thresholds_diff",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_thresholds_diff.json",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr04_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-04 compact threshold diffs for HDE-DISS005.3",
    },
    {
        "artifact_key": "epic030.pr04.band_thresholds_identity_hash",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr04_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-04 LF-terminated compat identity hashes for tuning runs (HDE-DISS005.3)",
    },
    {
        "artifact_key": "epic030.pr04.band_edges_binding",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_edges_binding.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr04_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-04 constants-pack band-edge binding evidence for HDE-DISS005.2",
    },
]

EPIC030_PR05_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic030.pr05.category_framework_binding",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-05/category_framework_binding.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr05_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-05 category-framework binding evidence for HDE-DISS006.3/.4/.5",
    },
    {
        "artifact_key": "epic030.pr05.per_channel_mechanics",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-05/per_channel_mechanics.json",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr05_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-05 per-channel mechanics evidence for canonical NN-NN and circuit scope (HDE-DISS006.3)",
    },
    {
        "artifact_key": "epic030.pr05.category_canonical_compare",
        "discovered_physical_path": "audit/qa/hde-epic030/pr-05/category_canonical_compare.log",
        "epic_id": "HDE-EPIC030",
        "record_type": "epic030_pr05_evidence",
        "schema_version": "1.0",
        "notes": "EPIC030 PR-05 canonical JSON compare evidence for category framework (HDE-DISS006.4)",
    },
]

EPIC032_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic032.pr01.router_key_table_10x4",
        "discovered_physical_path": "audit/gates/narratives/keys_10x4.table.json",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr01_evidence",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC032 PR-01 canonical narrative router 10x4 coverage table for HDE-FERM002.2",
    },
    {
        "artifact_key": "epic032.pr01.router_parity_abba",
        "discovered_physical_path": "artifacts/narratives/router/parity_abba.log",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr01_evidence",
        "schema_version": "1.0",
        "tokens": ["TWO_RUN_IDENTITY_OK", "COMPOSITE_ABBA_IDENTITY_OK"],
        "notes": "EPIC032 PR-01 keys-only router two-run identity and AB↔BA coherence log for HDE-FERM002.2",
    },
    {
        "artifact_key": "epic032.pr01.router_cli_http_parity",
        "discovered_physical_path": "artifacts/narratives/router/cli_http_parity.log",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr01_evidence",
        "schema_version": "1.0",
        "tokens": ["CLI_READER_PARITY_OK"],
        "notes": "EPIC032 PR-01 keys-only aux-preview CLI admin output to aux HTTP header parity log for HDE-FERM002.2",
    },
]

EPIC032_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic032.pr02.registry_diff",
        "discovered_physical_path": "audit/gates/narratives/registry.diff.json",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr02_evidence",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC032 PR-02 canonical narrative registry diff evidence for HDE-FERM003.2",
    },
    {
        "artifact_key": "epic032.pr02.pack_identity",
        "discovered_physical_path": "audit/gates/narratives/pack_identity.txt",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr02_evidence",
        "schema_version": "1.0",
        "tokens": ["TWO_RUN_IDENTITY_OK"],
        "notes": "EPIC032 PR-02 pack identity evidence from canonical manifest bytes for HDE-FERM003.2",
    },
    {
        "artifact_key": "epic032.pr02.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic032_doc_deltas.md",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr02_evidence",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC032 PR-02 Doc-Delta posture record for HDE-FERM003.2",
    },
]

EPIC032_PR03_SUPERSEDED_INDEX_KEYS = {
    ("epic032.pr03.adapter_selection", "artifacts/db_bridge/adapter_selection.snapshot.json"),
}

EPIC034_PR01_SUPERSEDED_INDEX_KEYS = {
    ("epic034.pr01.source_selection_snapshot", "artifacts/vendor/hdapi_v2/source_selection.snapshot.json"),
    ("epic034.pr01.v1_legacy_guard", "artifacts/vendor/hdapi_v2/v1_legacy_guard.log"),
    ("epic034.pr01.doc_deltas", "audit/docdeltas/hde-epic034_doc_deltas.md"),
    ("epic034.pr01.qa_meta_doc_deltas", "audit/qa/hde-epic034/00_meta/doc_deltas.md"),
}

EPIC034_PR02_SUPERSEDED_INDEX_KEYS = {
    ("hdapi_v2.request_shaping", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"),
    ("epic034.pr02.request_shaping_check", "audit/qa/hde-epic034/pr-02/request_shaping_check.log"),
}

EPIC034_PR03_SUPERSEDED_INDEX_KEYS = {
    ("hdapi_v2.response_mapping", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"),
    ("epic034.pr03.response_mapping_check", "audit/qa/hde-epic034/pr-03/response_mapping_check.log"),
    ("epic034.pr03.doc_deltas", "audit/docdeltas/hde-epic034_doc_deltas.md"),
    ("epic034.pr03.qa_meta_doc_deltas", "audit/qa/hde-epic034/00_meta/doc_deltas.md"),
}

EPIC034_PR04_SUPERSEDED_INDEX_KEYS = {
    ("hdapi_v2.adapter_boundary_proof", "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"),
    ("epic034.pr04.boundary_check", "audit/qa/hde-epic034/pr-04/boundary_check.log"),
    ("epic034.pr04.doc_deltas", "audit/docdeltas/hde-epic034_doc_deltas.md"),
    ("epic034.pr04.qa_meta_doc_deltas", "audit/qa/hde-epic034/00_meta/doc_deltas.md"),
    ("epic034.pr04.w005_final_validation_log", "audit/qa/hde-epic034/pr-04/w-005_final_validation.log"),
    ("epic034.pr04.w005_final_validation_report", "audit/qa/hde-epic034/pr-04/w-005_final_validation_report.md"),
}

EPIC034_PR06_SUPERSEDED_INDEX_KEYS = {
    ("epic034.pr04.doc_deltas", "audit/docdeltas/hde-epic034_doc_deltas.md"),
    ("epic034.pr04.qa_meta_doc_deltas", "audit/qa/hde-epic034/00_meta/doc_deltas.md"),
}

EPIC037_PR05_SUPERSEDED_INDEX_KEYS = {
    ("epic037.pr05.doc_deltas", "audit/docdeltas/hde-epic037_doc_deltas.md"),
    ("epic037.pr05.qa_meta_doc_deltas", "audit/qa/hde-epic037/00_meta/doc_deltas.md"),
}

EPIC032_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "db_bridge.adapter_selection.snapshot",
        "discovered_physical_path": "artifacts/db_bridge/adapter_selection.snapshot.json",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr03_evidence",
        "schema_version": "1.0",
        "tokens": ["DB_CONN_ENV_OK"],
        "notes": "EPIC032 PR-03 DBAccess provider selection and guarded bridge fallback evidence for HDE-FERM004.2",
    },
]


EPIC032_PR04_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic032.pr04.env_connectivity_nondev_failure",
        "discovered_physical_path": "artifacts/runtime/env_connectivity.nondev_failure.json",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr04_evidence",
        "schema_version": "1.0",
        "tokens": ["DB_CONN_ENV_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC032 PR-04 non-dev total-failure typed-error and numeric-free posture evidence for HDE-FERM004.3/.4",
    },
    {
        "artifact_key": "epic032.pr04.ops01.provider_parity_closure_decision",
        "discovered_physical_path": "audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json",
        "epic_id": "HDE-EPIC032",
        "record_type": "epic032_pr04_ops_evidence",
        "schema_version": "1.0",
        "notes": "EPIC032 PR-04 OPS-01 provider parity closure decision bound as OPS evidence only (non-claiming)",
    },
]


RUNTIME_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "runtime.env_connectivity",
        "discovered_physical_path": "artifacts/runtime/env_connectivity.snapshot.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "runtime_env_connectivity",
        "schema_version": "2",
        "tokens": ["DEV_DB_BRIDGE_FALLBACK_OK"],
        "notes": "Canonical runtime environment connectivity snapshot carrying the PF04 dev DB bridge fallback acceptance token; duplicate PR-specific current keys are retired.",
    },
]


EPIC033_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.source_inventory_json",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/source_inventory.json",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC033 PR-01 HDAPI v2 and legacy v1 public documentation source inventory for HDE-FERM006.1",
    },
    {
        "artifact_key": "hdapi_v2.source_inventory_md",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/source_inventory.md",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 human-readable HDAPI v2 source inventory summary and AI-boundary classification",
    },
    {
        "artifact_key": "hdapi_v2.openapi_validation",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/openapi_validation.log",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 validation and quarantine posture for v2-routes.yaml, v1-routes.yaml, and suspect OpenAPI artifacts",
    },
    {
        "artifact_key": "hdapi_v2.known_anomalies",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/known_anomalies.md",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 quarantine ledger for suspect api-reference/openapi.json and no-claim boundaries",
    },
    {
        "artifact_key": "hdapi_v2.endpoint_reference",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/endpoint_reference.csv",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 endpoint reference distinguishing recommended v2 chart routes from legacy v1 BodyGraph routes for HDE-FERM006.3",
    },
    {
        "artifact_key": "hdapi_v2.contract_map",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/contract_map.json",
        "epic_id": "HDE-EPIC033",
        "record_type": "hdapi_v2_contract_inventory",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC033 PR-01 canonical contract map binding validated route specs to v2 and legacy v1 route families",
    },
    {
        "artifact_key": "epic033.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic033.json",
        "epic_id": "HDE-EPIC033",
        "record_type": "epic033_baseline_pointer",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC033 PR-01 acceptance baseline map using existing registry-valid tokens only",
    },
    {
        "artifact_key": "epic033.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic033/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC033",
        "record_type": "epic033_baseline_pointer",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 token evidence matrix with no vendor-v2-specific token",
    },
    {
        "artifact_key": "epic033.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic033/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC033",
        "record_type": "epic033_baseline_pointer",
        "schema_version": "1.0",
        "notes": "EPIC033 PR-01 acceptance-map viability baseline for existing-token posture",
    },
    {
        "artifact_key": "epic033.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic033_doc_deltas.md",
        "epic_id": "HDE-EPIC033",
        "record_type": "epic033_baseline_pointer",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC033 PR-01 doc-delta baseline pointer",
    },
    {
        "artifact_key": "epic033.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic033/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC033",
        "record_type": "epic033_baseline_pointer",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC033 PR-01 QA meta doc-delta baseline pointer",
    },
]



def _load_epic033_entries() -> list[dict[str, object]]:
    produced_at = None
    source_inventory = ROOT / "artifacts/vendor/hdapi_v2/source_inventory.json"
    if source_inventory.exists():
        try:
            payload = json.loads(source_inventory.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit("INVALID_EPIC033_SOURCE_INVENTORY") from exc
        produced = payload.get("generated_at_utc")
        if isinstance(produced, str) and produced:
            produced_at = produced
    entries: list[dict[str, object]] = []
    for entry in EPIC033_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if produced_at is not None:
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries
EPIC034_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.source_selection",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr01_source_selection",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory",
    },
    {
        "artifact_key": "hdapi_v2.v1_legacy_guard",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/v1_legacy_guard.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr01_source_selection",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-01 LF-terminated legacy v1 BodyGraph guard proving v1 routes do not silently collapse into recommended v2 chart routes",
    },
    {
        "artifact_key": "epic034.pr01.source_selection_check",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-01/source_selection_check.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr01_source_selection",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-01 source-selection check log for route-family distinction and v1 legacy isolation",
    },
]


def _load_epic034_pr01_entries() -> list[dict[str, object]]:
    produced_at = None
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/source_selection.snapshot.json"
    if snapshot.exists():
        try:
            payload = json.loads(snapshot.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit("INVALID_EPIC034_SOURCE_SELECTION_SNAPSHOT") from exc
        produced = payload.get("generated_at_utc")
        if isinstance(produced, str) and produced:
            produced_at = produced
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR01_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if produced_at is not None and normalized.get("record_type") != "epic034_pr01_doc_delta":
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries

EPIC034_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.request_shaping",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr02_request_shaping",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary",
    },
    {
        "artifact_key": "epic034.pr02.request_shaping_check",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-02/request_shaping_check.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr02_request_shaping",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-02 LF-terminated request-shaping posture check log for v2 Bearer, v1 HD-Api-Key, geocode, base URL alias, and secret-safety posture",
    },
]


def _load_epic034_pr02_entries() -> list[dict[str, object]]:
    produced_at = None
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"
    check_log = ROOT / "audit/qa/hde-epic034/pr-02/request_shaping_check.log"
    if not snapshot.exists() or not check_log.exists():
        return []
    try:
        payload = json.loads(snapshot.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC034_REQUEST_SHAPING_SNAPSHOT") from exc
    produced = payload.get("generated_at_utc")
    if isinstance(produced, str) and produced:
        produced_at = produced
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR02_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if produced_at is not None:
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries


EPIC034_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.response_mapping",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr03_response_mapping",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim",
    },
    {
        "artifact_key": "epic034.pr03.response_mapping_check",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-03/response_mapping_check.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr03_response_mapping",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-03 LF-terminated response-mapping posture check log for envelope field preservation, schema gaps, secret safety, and non-claims",
    },
    {
        "artifact_key": "epic034.pr03.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic034_doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr03_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-03 current-epic draft/staging doc-delta surface for HDE-FERM007.3 response-mapping evidence",
    },
    {
        "artifact_key": "epic034.pr03.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic034/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr03_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-03 epic-scoped QA meta doc-delta capture for HDE-FERM007.3 response-mapping evidence",
    },
]


def _load_epic034_pr03_entries() -> list[dict[str, object]]:
    produced_at = None
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    check_log = ROOT / "audit/qa/hde-epic034/pr-03/response_mapping_check.log"
    if not snapshot.exists() or not check_log.exists():
        return []
    try:
        payload = json.loads(snapshot.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC034_RESPONSE_MAPPING_SNAPSHOT") from exc
    shared_snapshot_promoted = payload.get("epic_id") == "HDE-EPIC035" and payload.get("pf09_subtask_id") == "HDE-FERM008.4"
    produced = payload.get("generated_at_utc")
    if isinstance(produced, str) and produced:
        produced_at = produced
    pr04_doc_delta_active = (
        (ROOT / "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log").exists()
        and (ROOT / "audit/qa/hde-epic034/pr-04/boundary_check.log").exists()
    )
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR03_PRIMARY_ARTIFACTS:
        if shared_snapshot_promoted and entry.get("discovered_physical_path") == snapshot.relative_to(ROOT).as_posix():
            continue
        if pr04_doc_delta_active and entry.get("record_type") == "epic034_pr03_doc_delta":
            continue
        normalized = dict(entry)
        if produced_at is not None and normalized.get("record_type") != "epic034_pr03_doc_delta":
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries

EPIC034_PR04_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.adapter_boundary_proof",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_adapter_boundary",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim",
    },
    {
        "artifact_key": "epic034.pr04.boundary_check",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-04/boundary_check.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_adapter_boundary",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-04 boundary check log for adapter HTTP home, presenter boundary, serializer, pure-compute, and prior-family binding posture",
    },
    {
        "artifact_key": "epic034.pr04.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic034_doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-04 current-epic doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof",
    },
    {
        "artifact_key": "epic034.pr04.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic034/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-04 QA meta doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof",
    },
    {
        "artifact_key": "epic034.pr04.w005_final_validation_log",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-04/w-005_final_validation.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_w005_validation",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK", "EVIDENCE_INDEX_HASH_OK"],
        "notes": "EPIC034 PR-04 W-005 machine-readable final validation log for HDE-FERM007.4 boundary-proof remediation",
    },
    {
        "artifact_key": "epic034.pr04.w005_final_validation_report",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-04/w-005_final_validation_report.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr04_w005_validation",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK", "EVIDENCE_INDEX_HASH_OK"],
        "notes": "EPIC034 PR-04 W-005 human-readable final validation report for HDE-FERM007.4 later PF09.5 status-action support",
    },
]


def _load_epic034_pr04_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"
    check_log = ROOT / "audit/qa/hde-epic034/pr-04/boundary_check.log"
    if not proof.exists() or not check_log.exists():
        return []
    produced_at = None
    for line in proof.read_text(encoding="utf-8").splitlines():
        if line.startswith("generated_at_utc="):
            produced_at = line.split("=", 1)[1]
            break
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR04_PRIMARY_ARTIFACTS:
        artifact_path = ROOT / str(entry["discovered_physical_path"])
        if not artifact_path.exists():
            continue
        normalized = dict(entry)
        if normalized.get("record_type") == "epic034_pr04_w005_validation":
            for line in artifact_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("produced_at_utc="):
                    normalized["produced_at_utc"] = line.split("=", 1)[1]
                    break
        elif produced_at is not None and normalized.get("record_type") != "epic034_pr04_doc_delta":
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries

EPIC034_PR05_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.closed_rails_refusal",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/closed_rails_refusal.txt",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr05_closed_rails_refusal",
        "schema_version": "1.0",
        "tokens": ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "TWO_RUN_IDENTITY_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-05 LF-terminated closed-rails refusal proof for HDE-FERM007.5 and HDE-FERM008.1 covering deterministic v2 route shaping, PF10 header projection, typed refusal, and no external I/O; no open-rails, live conformance, public Reader, or AI scope claim",
    },
    {
        "artifact_key": "epic034.pr05.closed_rails_check",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-05/closed_rails_check.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr05_closed_rails_refusal",
        "schema_version": "1.0",
        "tokens": ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "TWO_RUN_IDENTITY_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-05 validation log with PASS predicates for source-selection, request-shaping, response-mapping, boundary proof, closed rails, v2/v1 auth posture, base URL conflict refusal, typed refusal, two-run identity, and no-claim posture",
    },
]


def _load_epic034_pr05_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/closed_rails_refusal.txt"
    check_log = ROOT / "audit/qa/hde-epic034/pr-05/closed_rails_check.log"
    if not proof.exists() or not check_log.exists():
        return []
    produced_at = None
    for line in proof.read_text(encoding="utf-8").splitlines():
        if line.startswith("generated_at_utc="):
            produced_at = line.split("=", 1)[1]
            break
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR05_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if produced_at is not None:
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries




EPIC035_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.error_mapping",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr01_provider_outcome_mapping",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK", "PF04_LOG_ALLOWLIST_009_OK", "ERROR_TOKEN_MAP_OK"],
        "notes": "EPIC035 PR-01 canonical provider error, retry, malformed-response, redirect, network-error, and secret-safe observability mapping evidence for HDE-FERM008.3; no live vendor call or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "hdapi_v2.rate_limit_headers",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr01_provider_outcome_mapping",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK", "ERROR_TOKEN_MAP_OK"],
        "notes": "EPIC035 PR-01 canonical Retry-After delta-seconds, HTTP-date, invalid, and overflow omission evidence for HDE-FERM008.3; 429 remains non-retryable",
    },
]


def _load_epic035_pr01_entries() -> list[dict[str, object]]:
    produced_at = None
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json"
    rate_limit = ROOT / "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json"
    if not snapshot.exists() or not rate_limit.exists():
        return []
    try:
        payload = json.loads(snapshot.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC035_ERROR_MAPPING_SNAPSHOT") from exc
    produced = payload.get("generated_at_utc")
    if isinstance(produced, str) and produced:
        produced_at = produced
    entries: list[dict[str, object]] = []
    for entry in EPIC035_PR01_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if produced_at is not None:
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries

EPIC035_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.response_mapping_pr02",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr02_response_normalization_gap",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-02 canonical HDE-FERM008.4 response-normalization evidence recording exact ChartResult/ChartSimpleResult adapter/schema gap; no compatibility by inference, live vendor call, public Reader change, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "hdapi_v2.release_binding",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr02_release_binding",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-02 release binding linking already-landed HDE-FERM008.3 provider outcome evidence to HDE-FERM008.4 exact adapter/schema gap evidence without claiming HDE-FERM008.5 closure or full v2 runtime conformance",
    },
]


def _load_epic035_pr02_entries() -> list[dict[str, object]]:
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    release = ROOT / "artifacts/vendor/hdapi_v2/release_binding.snapshot.json"
    if not snapshot.exists() or not release.exists():
        return []
    try:
        payload = json.loads(snapshot.read_text(encoding="utf-8"))
        release_payload = json.loads(release.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC035_PR02_SNAPSHOT") from exc
    if (
        payload.get("artifact_kind") != "hdapi_v2_response_normalization_gap"
        or payload.get("epic_id") != "HDE-EPIC035"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.4"
        or payload.get("response_normalization_posture") != "EXACT_SCHEMA_ADAPTER_GAP_RECORDED"
        or payload.get("schema_gap_status") != "GAP_RECORDED"
    ):
        raise SystemExit("INVALID_EPIC035_RESPONSE_MAPPING_IDENTITY")
    binding = (
        release_payload.get("pr_evidence_bindings", {})
        .get("pr02_hde_ferm008_4_response_normalization", {})
    )
    artifacts = binding.get("artifacts")
    expected_path = snapshot.relative_to(ROOT).as_posix()
    actual_sha = hashlib.sha256(snapshot.read_bytes()).hexdigest()
    if (
        release_payload.get("artifact_kind") != "hdapi_v2_release_binding"
        or release_payload.get("epic_id") != "HDE-EPIC035"
        or release_payload.get("pf09_task_id") != "HDE-FERM008"
        or binding.get("subtask_id") != "HDE-FERM008.4"
        or not isinstance(artifacts, list)
        or {item.get("path"): item.get("sha256") for item in artifacts if isinstance(item, dict)}.get(expected_path) != actual_sha
    ):
        raise SystemExit("INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC035_PR02_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


EPIC036_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.bg_resolve_route_policy",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 canonical bg:resolve route-policy classification for HDE-FERM008.6 selecting unsupported-runtime nonclaim for configured v2 BodyGraph-detail resolution; no live vendor call, public Reader change, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "hdapi_v2.bg_resolve_bodygraph_detail_proof",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 BodyGraph-detail sufficiency nonclaim proof for bg:resolve configured-v2 route policy; records no v2 ChartResult/ChartSimpleResult adapter sufficiency claim",
    },
    {
        "artifact_key": "hdapi_v2.bg_resolve_runtime_nonclaims",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 runtime nonclaims for bg:resolve route policy, including no public route, no app-side vendor credential ownership, no raw payload persistence, no AI scope, and no full v2 runtime conformance claim",
    },
    {
        "artifact_key": "hdapi_v2.bg_resolve_request_shape",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 request-shape evidence proving configured-v2 bg:resolve does not build a legacy bodygraphs request and preserves explicit legacy fallback only for non-v2 configured bases",
    },
    {
        "artifact_key": "hdapi_v2.bg_resolve_policy_binding",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 policy-binding snapshot for HDE-FERM008.6 route-policy classification; PR-02 ledger binding remains follow-up",
    },
    {
        "artifact_key": "epic036.pr01.route_policy_decision",
        "discovered_physical_path": "audit/qa/hde-epic036/route_policy_decision.log",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr01_bg_resolve_route_policy",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-01 LF-terminated route-policy decision log recording unsupported-runtime nonclaim, explicit legacy fallback boundary, and OPS-01 not required by PR-01",
    },
]


EPIC036_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic036.pr02.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic036.json",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr02_evidence_loop_binding",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK", "DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC036 PR-02 acceptance map binding already-landed bg:resolve route-policy evidence into HDE-FERM008.6 evidence-loop surfaces; no OPS execution, PF09 status movement, epic closeout, public Reader change, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic036.pr02.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic036/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr02_evidence_loop_binding",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC036 PR-02 token/evidence matrix mapping approved tokens to concrete PR-01 and PR-02 evidence paths without vendor-v2-specific tokens or QA PASS claim",
    },
    {
        "artifact_key": "epic036.pr02.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic036/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr02_evidence_loop_binding",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-02 viability log recording acceptance-map coherence with unsupported-runtime nonclaim route-policy evidence and no OPS execution",
    },
    {
        "artifact_key": "epic036.pr02.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic036_doc_deltas.md",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr02_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-02 doc-delta candidate surface for HDE-FERM008.6 evidence-loop supportability; PF-Canon not edited and PF09 status movement remains separate",
    },
    {
        "artifact_key": "epic036.pr02.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic036/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC036",
        "record_type": "epic036_pr02_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC036 PR-02 QA-meta doc-delta candidate mirror for HDE-FERM008.6 evidence-loop supportability; no PF-Canon edit, OPS completion, or full v2 runtime conformance claim",
    },
]


def _load_epic036_pr01_entries() -> list[dict[str, object]]:
    snapshot = ROOT / "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
    if not snapshot.exists():
        return []
    try:
        payload = json.loads(snapshot.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC036_PR01_ROUTE_POLICY_SNAPSHOT") from exc
    if (
        payload.get("artifact_kind") != "bg_resolve_route_policy"
        or payload.get("epic_id") != "HDE-EPIC036"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.6"
        or payload.get("selected_posture") != "unsupported_runtime_nonclaim"
    ):
        raise SystemExit("INVALID_EPIC036_ROUTE_POLICY_IDENTITY")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC036_PR01_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC036_PR01_ARTIFACT:{rel}")
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


def _load_epic036_pr02_entries() -> list[dict[str, object]]:
    acceptance = ROOT / "docs/acceptance_map_epic036.json"
    if not acceptance.exists():
        return []
    try:
        raw = acceptance.read_bytes()
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC036_PR02_ACCEPTANCE_MAP") from exc
    if raw != json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8") + b"\n":
        raise SystemExit("NONCANONICAL_EPIC036_PR02_ACCEPTANCE_MAP")
    allowed = {
        "TESTS_PASS_OK",
        "DOC_DELTA_PRESENT_OK",
        "EVIDENCE_INDEX_UPDATED_OK",
        "MACHINE_MIRROR_UPDATED_OK",
        "EVIDENCE_INDEX_HASH_OK",
        "EVIDENCE_PATHS_VALIDATED_OK",
        "EVIDENCE_PATH_PROOFS_OK",
        "JSON_CANONICAL_CHECK_OK",
        "NO_EXTERNAL_IO_ON_REFUSAL_OK",
        "ENV_RAILS_POLICY_OK",
    }
    token_names = {item.get("name") for item in payload.get("tokens", []) if isinstance(item, dict)}
    if (
        payload.get("epic_id") != "HDE-EPIC036"
        or payload.get("selected_route_policy_classification") != "unsupported_runtime_nonclaim"
        or token_names != allowed
    ):
        raise SystemExit("INVALID_EPIC036_PR02_ACCEPTANCE_IDENTITY")
    required_nonclaims = {
        "QA PASS",
        "OPS completion",
        "PF09 status movement",
        "HDE-FERM008 parent Done",
        "epic closeout",
        "full HumanDesignAPI v2 runtime conformance",
        "public Reader change",
        "public route",
        "public flag",
        "public payload or transport change",
        "new HTTP home",
        "app-side HumanDesignAPI credential ownership",
        "raw payload persistence",
        "AI scope",
    }
    if not required_nonclaims <= set(payload.get("nonclaims", [])):
        raise SystemExit("INVALID_EPIC036_PR02_NONCLAIMS")
    if payload.get("ops_01", {}).get("executed_for_pr02") is not False:
        raise SystemExit("INVALID_EPIC036_PR02_OPS01_POSTURE")
    entries: list[dict[str, object]] = []
    for entry in EPIC036_PR02_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC036_PR02_ARTIFACT:{rel}")
        entries.append(dict(entry))
    return entries


EPIC037_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.hde_epic037_field_sufficiency_proof",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr01_field_sufficiency",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-01 machine-checkable v2 BodyGraph-detail field-sufficiency proof for HDE-FERM008.7; records typed insufficient classification without runtime conformance claim",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_adapter_contract",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr01_field_sufficiency",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-01 internal HDE BodyGraph/person/cache/compat adapter contract snapshot for v2 ChartResult and ChartSimpleResult readiness",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_adapter_contract_nonclaims",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr01_field_sufficiency",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-01 explicit nonclaims for unsupported vendor fields and unsupported HDE paths; no public Reader, route, flag, payload, app-side call path, live vendor call, raw payload persistence, AI behavior, QA PASS, OPS, or closeout claim",
    },
    {
        "artifact_key": "epic037.pr01.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic037_doc_deltas.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr01_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-01 doc-delta candidate for HDE-FERM008.7 field-sufficiency evidence; PF-Canon not edited",
    },
    {
        "artifact_key": "epic037.pr01.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic037/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr01_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-01 QA-meta doc-delta mirror for HDE-FERM008.7 evidence; no PF09 status movement or runtime conformance claim",
    },
]


def _load_epic037_pr01_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json"
    if not proof.exists():
        return []
    try:
        payload = json.loads(proof.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC037_PR01_FIELD_SUFFICIENCY_PROOF") from exc
    if (
        payload.get("artifact_kind") != "hde_epic037_field_sufficiency_proof"
        or payload.get("epic_id") != "HDE-EPIC037"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.7"
        or payload.get("selected_payload_family") != "typed_insufficient_classification"
        or payload.get("field_sufficiency_status") != "INSUFFICIENT_FAIL_CLOSED"
        or payload.get("v2_chart_data_feeds_existing_bodygraph_person_cache_compat_contract") is not False
    ):
        raise SystemExit("INVALID_EPIC037_FIELD_SUFFICIENCY_IDENTITY")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC037_PR01_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_PR01_ARTIFACT:{rel}")
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


EPIC037_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.hde_epic037_adapter_mapping",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr02_v2_adapter",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-02 deterministic pure v2 ChartResult adapter mapping proof for HDE-FERM008.8; context-backed only and not resolver wiring",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_adapter_negative_fixtures",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr02_v2_adapter",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-02 negative fixture evidence for missing context, missing detail fields, malformed data, unsupported payloads, and wrong route failures",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_public_reader_no_change",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr02_v2_adapter",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-02 public Reader no-change evidence; no public route, flag, payload, transport, or HTTP home claim",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_no_raw_payload_persistence",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr02_v2_adapter",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-02 scoped adapter no-raw-payload-persistence posture; does not claim generic log/privacy tokens",
    },
]


def _load_epic037_pr02_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json"
    if not proof.exists():
        return []
    try:
        payload = json.loads(proof.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC037_PR02_ADAPTER_MAPPING") from exc
    if (
        payload.get("artifact_kind") != "hde_epic037_adapter_mapping_snapshot"
        or payload.get("epic_id") != "HDE-EPIC037"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.8"
        or payload.get("mapping_result", {}).get("status") != "mapped"
        or payload.get("mapping_result", {}).get("code") != "ADAPTER_MAPPED"
    ):
        raise SystemExit("INVALID_EPIC037_PR02_ADAPTER_IDENTITY")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC037_PR02_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_PR02_ARTIFACT:{rel}")
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


EPIC037_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.hde_epic037_bg_resolve_v2_route_policy",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr03_bg_resolve_v2_adapter_wiring",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-03 configured-v2 bg:resolve route policy selects adapter-backed version-neutral charts route for HDE-FERM008.9",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_bg_resolve_request_shape",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr03_bg_resolve_v2_adapter_wiring",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-03 request-shape proof for version-neutral charts construction, v2 Bearer auth posture, geocode posture, and no v2 legacy bodygraphs request",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_bg_resolve_closed_rails_no_io",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr03_bg_resolve_v2_adapter_wiring",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-03 closed-rails no-I/O resolver refusal proof before route policy, client construction, request construction, fetch, ingest, DB, DNS, socket, or HTTP",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_bg_resolve_legacy_fallback",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr03_bg_resolve_v2_adapter_wiring",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-03 explicit non-v2 legacy BodyGraph fallback proof with distinct HD-Api-Key posture",
    },
]


def _load_epic037_pr03_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json"
    if not proof.exists():
        return []
    try:
        payload = json.loads(proof.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC037_PR03_BG_RESOLVE_ROUTE_POLICY") from exc
    policy = payload.get("route_policy", {})
    if (
        payload.get("artifact_kind") != "hde_epic037_bg_resolve_v2_route_policy"
        or payload.get("epic_id") != "HDE-EPIC037"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.9"
        or policy.get("classification") != "adapter_backed_v2_chart"
        or policy.get("route_family") != "recommended_v2_chart"
        or policy.get("resource_path") != "charts"
        or payload.get("resolver_output_proof", {}).get("adapter", {}).get("code") != "ADAPTER_MAPPED"
    ):
        raise SystemExit("INVALID_EPIC037_PR03_BG_RESOLVE_IDENTITY")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC037_PR03_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_PR03_ARTIFACT:{rel}")
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


EPIC037_PR04_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "hdapi_v2.hde_epic037_v2_to_compat_proof",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr04_v2_to_compat",
        "role": "proof",
        "schema_version": "1.0",
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-04 proof that mapped v2 ChartResult adapter output is shape-sufficient for existing compatibility computation for HDE-FERM008.10",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_v2_to_compat_two_run",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr04_v2_to_compat",
        "role": "proof",
        "schema_version": "1.0",
        "tokens": ["TWO_RUN_IDENTITY_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-04 two-run canonical identity proof for the closed-rails v2 adapter-to-compat fixture path",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_v2_to_compat_pair_order",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr04_v2_to_compat",
        "role": "proof",
        "schema_version": "1.0",
        "tokens": ["COMPOSITE_ABBA_IDENTITY_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-04 AB/BA normalized pair-order identity proof for mapped v2 resolved parties entering compatibility computation",
    },
    {
        "artifact_key": "hdapi_v2.hde_epic037_admin_public_boundary",
        "discovered_physical_path": "artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr04_v2_to_compat",
        "role": "proof",
        "schema_version": "1.0",
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-04 public Reader no-change and admin/public boundary preservation proof; numeric, cache, adapter, and vendor internals remain out of public Reader bytes",
    },
]


def _load_epic037_pr04_entries() -> list[dict[str, object]]:
    proof = ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json"
    if not proof.exists():
        return []
    try:
        payload = json.loads(proof.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC037_PR04_V2_TO_COMPAT_PROOF") from exc
    if (
        payload.get("artifact_kind") != "hde_epic037_v2_to_compat_proof"
        or payload.get("epic_id") != "HDE-EPIC037"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.10"
        or payload.get("compat_acceptance", {}).get("accepted_mapped_resolved_parties") is not True
        or payload.get("fixture_count") != 2
    ):
        raise SystemExit("INVALID_EPIC037_PR04_V2_TO_COMPAT_IDENTITY")
    produced = payload.get("generated_at_utc")
    entries: list[dict[str, object]] = []
    for entry in EPIC037_PR04_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"MISSING_EPIC037_PR04_ARTIFACT:{rel}")
        normalized = dict(entry)
        if isinstance(produced, str) and produced:
            normalized["produced_at_utc"] = produced
        entries.append(normalized)
    return entries


EPIC037_OPS01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic037.ops01.commands",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "ENV_RAILS_POLICY_OK"],
        "notes": "EPIC037 OPS-01 PO-produced open-rails v2 chart-backed bg:resolve dry-run command transcript; bound by PR-05 without rerunning OPS or making a live vendor call",
    },
    {
        "artifact_key": "epic037.ops01.stdout",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 stdout JSON records status ok, ADAPTER_MAPPED ChartResult, vendor.hdapi.post:/charts, and redacted request posture",
    },
    {
        "artifact_key": "epic037.ops01.stderr",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/stderr.log",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 OPS-01 stderr log is empty for successful PO-produced smoke",
    },
    {
        "artifact_key": "epic037.ops01.exit_codes",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 OPS-01 exit-code evidence records bg_resolve_exit_code=0",
    },
    {
        "artifact_key": "epic037.ops01.env_presence_redacted",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK", "ENV_RAILS_POLICY_OK"],
        "notes": "EPIC037 OPS-01 presence-only environment proof; no plaintext HD_API_KEY or GEO_API_KEY value recorded",
    },
    {
        "artifact_key": "epic037.ops01.request_summary",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 request summary records charts resource, recommended v2 chart route family, ChartResult payload family, redacted base URL, and no raw body emission",
    },
    {
        "artifact_key": "epic037.ops01.result_summary",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 result summary supports bounded runtime conformance for this smoke only and records no ingest rows written",
    },
    {
        "artifact_key": "epic037.ops01.adapter_mapping_result_summary",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 adapter mapping summary records mapped resolved BodyGraph/person/cache shape presence without raw vendor payload recording",
    },
    {
        "artifact_key": "epic037.ops01.compat_path_result_summary",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 compatibility-path summary records accepted compat path and category_count=10",
    },
    {
        "artifact_key": "epic037.ops01.failure_classification",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"],
        "notes": "EPIC037 OPS-01 failure classification records not_applicable_success with stdout JSON parse ok",
    },
    {
        "artifact_key": "epic037.ops01.files_sha256",
        "discovered_physical_path": "audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "manifest",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 OPS-01 checksum ledger covering OPS evidence files and QA pointer",
    },
    {
        "artifact_key": "epic037.ops01.ops_evidence_pointer",
        "discovered_physical_path": "audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_ops01_po_produced_runtime_smoke",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 OPS-01 QA pointer to PO-produced OPS evidence root; PR-05 binds it without rerunning OPS",
    },
]

EPIC037_PR05_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic037.pr05.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic037.json",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_parent_evidence_binding",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK", "DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC037 PR-05 parent acceptance map binds HDE-FERM008.7 through HDE-FERM008.12 and records supportable_to_done as later-drain support only",
    },
    {
        "artifact_key": "epic037.pr05.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic037/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_parent_evidence_binding",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC037 PR-05 token/evidence matrix maps registered tokens to current concrete evidence without QA PASS or PF09 status movement claim",
    },
    {
        "artifact_key": "epic037.pr05.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic037/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_parent_evidence_binding",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-05 acceptance-map viability log records parseability, path/proof/index/mirror posture, supported tokens, and parent posture supportability",
    },
    {
        "artifact_key": "epic037.pr05.parent_evidence_binding",
        "discovered_physical_path": "audit/qa/hde-epic037/parent_evidence_binding.log",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_parent_evidence_binding",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-05 parent evidence binding log lists HDE-FERM008.7 through HDE-FERM008.12 evidence families, index/mirror/hash/path-proof posture, nonclaims, and final supportable_to_done posture",
    },
    {
        "artifact_key": "epic037.pr05.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-05 doc-delta candidate surface for parent evidence binding; PF-Canon not edited",
    },
    {
        "artifact_key": "epic037.pr05.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md",
        "epic_id": "HDE-EPIC037",
        "record_type": "epic037_pr05_doc_delta_candidate",
        "role": "audit",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC037 PR-05 QA-meta doc-delta mirror for parent evidence binding; no PF09 status movement, OPS rerun, QA PASS, or closeout claim",
    },
]


def _load_epic037_ops01_entries() -> list[dict[str, object]]:
    stdout_path = ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log"
    if not stdout_path.exists():
        return []
    commands_text = (ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt").read_text(encoding="utf-8")
    required_command_rails = (
        "HD_API_BASE_URL=<redacted-v2-base>",
        "SAFE_MODE=0",
        "ALLOW_NETWORK=1",
        "APP_ENV=dev",
        "LC_ALL=C",
        "LANG=C",
        "TZ=UTC",
    )
    if "https://" in commands_text or "http://" in commands_text or any(token not in commands_text for token in required_command_rails):
        raise SystemExit("INVALID_EPIC037_OPS01_COMMAND_REDACTION")
    ops_root = ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001"

    def _load_canonical_ops_json(filename: str) -> object:
        path = ops_root / filename
        raw = path.read_bytes()
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit("INVALID_EPIC037_OPS01_JSON") from exc
        canonical = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8") + b"\n"
        if raw != canonical:
            raise SystemExit(f"NONCANONICAL_EPIC037_OPS01_JSON:{path.relative_to(ROOT).as_posix()}")
        return payload

    stdout_payload = _load_canonical_ops_json("stdout.log")
    request_summary = _load_canonical_ops_json("request_summary.json")
    env_presence = _load_canonical_ops_json("env_presence_redacted.json")
    result_summary = _load_canonical_ops_json("result_summary.json")
    adapter_summary = _load_canonical_ops_json("adapter_mapping_result_summary.json")
    compat_summary = _load_canonical_ops_json("compat_path_result_summary.json")
    failure = _load_canonical_ops_json("failure_classification.json")
    request = stdout_payload.get("resolver", {}).get("request", {})
    request_summary_request = request_summary.get("request", {})
    request_summary_policy = request_summary.get("route_policy", {})
    env_rails = env_presence.get("rails", {})
    env_secret_policy = env_presence.get("secret_policy", {})
    env_base_url_posture = env_presence.get("base_url_posture", {})
    env_locale = env_presence.get("locale", {})
    adapter = stdout_payload.get("adapter", {})
    expected_header_posture = ["Authorization: Bearer <redacted>", "HD-Geocode-Key: <redacted>"]
    expected_auth_posture = "Authorization: Bearer <redacted>"
    if (
        stdout_payload.get("status") != "ok"
        or adapter.get("status") != "mapped"
        or adapter.get("code") != "ADAPTER_MAPPED"
        or adapter.get("payload_family") != "ChartResult"
        or request.get("route") != "vendor.hdapi.post:/charts"
        or request.get("configured_base_url") != "<redacted>"
        or request.get("raw_body_emitted") is not False
        or request.get("raw_response_body_emitted") is not False
        or request.get("route_auth_posture") != expected_auth_posture
        or request.get("header_posture") != expected_header_posture
        or request_summary_request.get("route") != "vendor.hdapi.post:/charts"
        or request_summary_request.get("configured_base_url") != "<redacted>"
        or request_summary_request.get("resource_path") != "charts"
        or request_summary_request.get("raw_body_emitted") is not False
        or request_summary_request.get("raw_response_body_emitted") is not False
        or request_summary_request.get("route_auth_posture") != expected_auth_posture
        or request_summary_request.get("header_posture") != expected_header_posture
        or request_summary_policy.get("route_family") != "recommended_v2_chart"
        or request_summary_policy.get("resource_path") != "charts"
        or request_summary_policy.get("payload_family") != "ChartResult"
        or request_summary_policy.get("supported") is not True
        or request_summary_policy.get("route_auth_posture") != expected_auth_posture
        or request_summary_policy.get("geocode_required") is not True
        or result_summary.get("runtime_conformance_supported_by_this_smoke") is not True
        or adapter_summary.get("mapped_shape", {}).get("resolved_bodygraph_present") is not True
        or adapter_summary.get("mapped_shape", {}).get("resolved_person_present") is not True
        or adapter_summary.get("mapped_shape", {}).get("cache_input_fingerprint_present") is not True
        or adapter_summary.get("raw_vendor_payload_recorded") is not False
        or compat_summary.get("compat_path_status") != "accepted"
        or compat_summary.get("category_count") != 10
        or failure.get("classification") != "not_applicable_success"
        or env_presence.get("artifact_kind") != "hde_epic037_ops01_env_presence_redacted"
        or env_presence.get("epic_id") != "HDE-EPIC037"
        or env_presence.get("pf09_task_id") != "HDE-FERM008"
        or env_presence.get("pf09_subtask_id") != "HDE-FERM008.11"
        or env_presence.get("missing") != []
        or env_presence.get("errors") != []
        or env_rails.get("safe_mode") != "0"
        or env_rails.get("allow_network") != "1"
        or env_rails.get("app_env") != "dev"
        or env_locale.get("lc_all") != "C"
        or env_locale.get("lang") != "C"
        or env_locale.get("tz") != "UTC"
        or env_base_url_posture.get("hd_api_base_url_present") is not True
        or env_base_url_posture.get("hd_api_base_url_expected_v2_value") is not True
        or env_base_url_posture.get("hd_api_base_url_value_recorded") is not False
        or env_base_url_posture.get("hdapi_base_url_alias_present") is not False
        or env_secret_policy.get("hd_api_key_value_recorded") is not False
        or env_secret_policy.get("geo_api_key_value_recorded") is not False
        or env_secret_policy.get("plaintext_secrets_allowed_in_evidence") is not False
    ):
        raise SystemExit("INVALID_EPIC037_OPS01_RUNTIME_OR_ENV_POSTURE")
    exit_code_lines = (
        ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt"
    ).read_text(encoding="utf-8").splitlines()
    if exit_code_lines != ["bg_resolve_exit_code=0"]:
        raise SystemExit("INVALID_EPIC037_OPS01_EXIT_CODE")
    ledger_lines = (ROOT / "audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt").read_text(encoding="utf-8").splitlines()
    ledger = {line.split()[1]: line.split()[0] for line in ledger_lines if line.strip()}
    entries: list[dict[str, object]] = []
    for entry in EPIC037_OPS01_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"MISSING_EPIC037_OPS01_ARTIFACT:{rel}")
        if rel != "audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt" and ledger.get(rel) != _sha256_path(path):
            raise SystemExit(f"INVALID_EPIC037_OPS01_LEDGER:{rel}")
        normalized = dict(entry)
        normalized["produced_at_utc"] = "2026-07-06T00:00:00Z"
        entries.append(normalized)
    secret_policy = request_summary.get("secret_policy", {})
    if (
        secret_policy.get("plaintext_secret_recorded") is not False
        or secret_policy.get("raw_request_body_recorded") is not False
        or secret_policy.get("raw_response_body_recorded") is not False
        or secret_policy.get("uncontrolled_raw_vendor_payload_recorded") is not False
    ):
        raise SystemExit("INVALID_EPIC037_OPS01_SECRET_OR_RAW_PAYLOAD_POSTURE")
    return entries


def _load_epic037_pr05_entries() -> list[dict[str, object]]:
    acceptance_map = ROOT / "docs/acceptance_map_epic037.json"
    if not acceptance_map.exists():
        return []
    try:
        payload = json.loads(acceptance_map.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC037_PR05_ACCEPTANCE_MAP") from exc
    if (
        payload.get("epic_id") != "HDE-EPIC037"
        or payload.get("pf09_task_id") != "HDE-FERM008"
        or payload.get("pf09_subtask_id") != "HDE-FERM008.12"
        or payload.get("parent_posture") != "supportable_to_done"
        or set(payload.get("pf09_subtasks_bound", [])) != {"HDE-FERM008.7", "HDE-FERM008.8", "HDE-FERM008.9", "HDE-FERM008.10", "HDE-FERM008.11", "HDE-FERM008.12"}
        or "PF09 status movement" not in payload.get("nonclaims", [])
        or "QA PASS" not in payload.get("nonclaims", [])
    ):
        raise SystemExit("INVALID_EPIC037_PR05_ACCEPTANCE_IDENTITY")
    entries: list[dict[str, object]] = []
    for entry in EPIC037_PR05_PRIMARY_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_PR05_ARTIFACT:{rel}")
        normalized = dict(entry)
        normalized["produced_at_utc"] = str(payload.get("generated_at_utc") or "2026-07-06T00:00:00Z")
        entries.append(normalized)
    return entries


EPIC035_PR03_OPS01_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic035.ops01.ops_evidence_manifest",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "manifest",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 retained OPS-01 evidence manifest mapping planned deliverables to repo-retained paths; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.files_sha256",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/files_sha256.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 retained OPS-01 checksum ledger; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.final_classification",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 final classification separating v2 charts/simple geokey success from bg:resolve runtime gap; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.v2_charts_simple_commands",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 v2 charts/simple command transcript retained from OPS-01; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.v2_charts_simple_stdout",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 v2 charts/simple stdout proving redacted Bearer and HD-Geocode-Key header posture with legacy HD-Api-Key absent; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.v2_charts_simple_stderr",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 v2 charts/simple stderr retained from OPS-01; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.v2_charts_simple_result_summary",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 v2 charts/simple result summary retained from OPS-01; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.request_summary",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 OPS-01 request summary; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.result_summary",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 OPS-01 result summary; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.stdout",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 bg:resolve stdout retained as provider-error/runtime-gap evidence, not success; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.stderr",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 bg:resolve stderr retained as provider-error/runtime-gap evidence; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.exit_codes",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 OPS-01 exit-code evidence; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.vendor_bodygraph_dry_run",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 bg:resolve dry-run provider-error/runtime-gap evidence; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.ops01.vendor_bodygraph_dry_run_no_version",
        "discovered_physical_path": "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_ops01_retained_evidence",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC035 PR-03 bg:resolve dry-run no-version provider-error/runtime-gap evidence; bound without rerunning OPS or making live vendor calls",
    },
    {
        "artifact_key": "epic035.pr03.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic035.json",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_acceptance_map",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ['JSON_CANONICAL_CHECK_OK', 'EVIDENCE_PATH_PROOFS_OK', 'DOC_DELTA_PRESENT_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic035.pr03.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic035/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_acceptance_boundary",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ['EVIDENCE_PATH_PROOFS_OK', 'DOC_DELTA_PRESENT_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic035.pr03.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic035/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_acceptance_boundary",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ['EVIDENCE_PATH_PROOFS_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic035.pr03.ops_evidence_binding",
        "discovered_physical_path": "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_ops01_binding",
        "role": "log",
        "schema_version": "1.0",
        "tokens": ['EVIDENCE_PATH_PROOFS_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic035.pr03.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic035_doc_deltas.md",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_doc_delta",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ['DOC_DELTA_PRESENT_OK', 'EVIDENCE_PATH_PROOFS_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
    {
        "artifact_key": "epic035.pr03.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic035/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC035",
        "record_type": "epic035_pr03_doc_delta",
        "role": "snapshot",
        "schema_version": "1.0",
        "tokens": ['DOC_DELTA_PRESENT_OK', 'EVIDENCE_PATH_PROOFS_OK'],
        "notes": "EPIC035 PR-03 acceptance-boundary artifact for HDE-FERM008.5 evidence-loop closure; no QA PASS, OPS completion, PF09 status movement, parent Done, epic closeout, or full v2 runtime conformance claim",
    },
]


def _epic035_ops01_v2_stdout_is_valid(stdout_payload: Mapping[str, object]) -> bool:
    return (
        stdout_payload.get("authorization_header_shape") == "Authorization: Bearer <redacted>"
        and stdout_payload.get("hd_geocode_key_header_shape") == "HD-Geocode-Key: <redacted>"
        and stdout_payload.get("has_authorization") is True
        and stdout_payload.get("has_hd_geocode_key") is True
        and stdout_payload.get("legacy_hd_api_key_on_v2_path") is False
        and stdout_payload.get("has_hd_api_key") is False
    )


def _load_epic035_ops01_checksum_ledger(ledger_path: Path) -> dict[str, str]:
    ledger: dict[str, str] = {}
    for line_number, raw_line in enumerate(ledger_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        parts = raw_line.split(maxsplit=1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise SystemExit(f"INVALID_EPIC035_OPS01_CHECKSUM_LEDGER_LINE:{line_number}")
        sha, rel = parts
        if any(char not in "0123456789abcdef" for char in sha):
            raise SystemExit(f"INVALID_EPIC035_OPS01_CHECKSUM_LEDGER_SHA:{line_number}")
        ledger[rel.strip()] = sha
    return ledger


def _validate_epic035_ops01_checksums() -> None:
    ledger_path = ROOT / "audit/ops/hde-epic035/ops-01/files_sha256.txt"
    if not ledger_path.exists():
        raise SystemExit("MISSING_EPIC035_OPS01_CHECKSUM_LEDGER")
    ledger = _load_epic035_ops01_checksum_ledger(ledger_path)
    for entry in EPIC035_PR03_OPS01_ARTIFACTS:
        rel = str(entry["discovered_physical_path"])
        if not rel.startswith("audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/"):
            continue
        expected_sha = ledger.get(rel)
        if expected_sha is None:
            raise SystemExit(f"MISSING_EPIC035_OPS01_LEDGER_ENTRY:{rel}")
        actual_sha = _sha256_path(ROOT / rel)
        if actual_sha != expected_sha:
            raise SystemExit(f"MISMATCH_EPIC035_OPS01_LEDGER_SHA:{rel}")

def _load_epic035_pr03_entries() -> list[dict[str, object]]:
    acceptance = ROOT / "docs/acceptance_map_epic035.json"
    binding = ROOT / "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"
    final_classification = ROOT / "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt"
    stdout = ROOT / "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log"
    if not acceptance.exists() or not binding.exists():
        return []
    try:
        payload = json.loads(acceptance.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC035_PR03_ACCEPTANCE_MAP") from exc
    token_names = {item.get("name") for item in payload.get("tokens", []) if isinstance(item, dict)}
    allowed = {"DOC_DELTA_PRESENT_OK", "EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_INDEX_HASH_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK", "TESTS_PASS_OK"}
    if payload.get("epic_id") != "HDE-EPIC035" or not token_names <= allowed:
        raise SystemExit("INVALID_EPIC035_PR03_ACCEPTANCE_TOKENS")
    nonclaims = set(payload.get("nonclaims", []))
    required_nonclaims = {"QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout", "full HumanDesignAPI v2 runtime conformance"}
    if not required_nonclaims <= nonclaims:
        raise SystemExit("INVALID_EPIC035_PR03_NONCLAIMS")
    if final_classification.exists():
        text = final_classification.read_text(encoding="utf-8")
        if "v2_charts_simple=success" not in text or "bg_resolve_http_status=404" not in text or "runtime_gap=" not in text:
            raise SystemExit("INVALID_EPIC035_OPS01_FINAL_CLASSIFICATION")
    if stdout.exists():
        text = stdout.read_text(encoding="utf-8")
        try:
            stdout_payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise SystemExit("INVALID_EPIC035_OPS01_V2_STDOUT_JSON") from exc
        if not _epic035_ops01_v2_stdout_is_valid(stdout_payload):
            raise SystemExit("INVALID_EPIC035_OPS01_V2_STDOUT")
    _validate_epic035_ops01_checksums()
    entries = []
    for entry in EPIC035_PR03_OPS01_ARTIFACTS:
        if not (ROOT / str(entry["discovered_physical_path"])).exists():
            raise SystemExit(f"MISSING_EPIC035_PR03_ARTIFACT:{entry['discovered_physical_path']}")
        normalized = dict(entry)
        entries.append(normalized)
    return entries

EPIC034_PR06_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic034.ops02.commands",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/commands.txt",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 retained command transcript for HDE-FERM008.2 open-rails smoke evidence; PR-06 binds without rerunning the smoke",
    },
    {
        "artifact_key": "epic034.ops02.env_presence_redacted",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/env_presence_redacted.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 redacted environment-presence evidence for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.exit_codes",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/exit_codes.txt",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 wrapper exit-code evidence for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.files_sha256",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/files_sha256.txt",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 retained-file checksum manifest for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.moon_loop_rerun_transcript",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 Moon Loop rerun transcript preserving command-to-output provenance for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.full_action_log",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/ops02_full_action_log_and_evidence_output.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 full action log and evidence output for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.smoke_procedure",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 repo-retained smoke procedure; PR-06 governs the file without executing it",
    },
    {
        "artifact_key": "epic034.ops02.request_summary",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/request_summary.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 request summary proving version-neutral charts/coordinates and redacted Bearer auth posture for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.result_summary",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/result_summary.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 result summary supporting HDE-FERM008.2 only with no parent-completion or full-v2-conformance claim",
    },
    {
        "artifact_key": "epic034.ops02.stderr",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/stderr.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 stderr capture for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.ops02.stdout",
        "discovered_physical_path": "audit/ops/hde-epic034/ops-02/stdout.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_ops02_smoke_evidence",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 OPS-02 stdout capture recording PASS and vendor_attempted=true for HDE-FERM008.2",
    },
    {
        "artifact_key": "epic034.pr06.ops_smoke_evidence_binding",
        "discovered_physical_path": "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr06_ops02_binding",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-06 LF-terminated binding log for already-produced OPS-02 open-rails smoke evidence supporting HDE-FERM008.2 only; no full v2 runtime conformance, HDE-FERM008 parent completion, public Reader, or AI scope claim",
    },
    {
        "artifact_key": "epic034.pr06.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic034.json",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr06_acceptance_map",
        "schema_version": "1.0",
        "tokens": ["EVIDENCE_PATH_PROOFS_OK", "DOC_DELTA_PRESENT_OK"],
        "notes": "EPIC034 PR-06 acceptance map using existing baseline tokens only and binding PR-06 to HDE-FERM008.2 only",
    },
    {
        "artifact_key": "epic034.pr06.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic034_doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr06_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-06 current-epic doc-delta surface records OPS-02 support for HDE-FERM008.2 only and no PF-Canon edit",
    },
    {
        "artifact_key": "epic034.pr06.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic034/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC034",
        "record_type": "epic034_pr06_doc_delta",
        "schema_version": "1.0",
        "tokens": ["DOC_DELTA_PRESENT_OK", "EVIDENCE_PATH_PROOFS_OK"],
        "notes": "EPIC034 PR-06 QA meta doc-delta surface records OPS-02 support for HDE-FERM008.2 only and no PF-Canon edit",
    },
]


def _load_epic034_pr06_entries() -> list[dict[str, object]]:
    binding_log = ROOT / "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"
    acceptance_map = ROOT / "docs/acceptance_map_epic034.json"
    if not binding_log.exists() or not acceptance_map.exists():
        return []
    produced_at = None
    for line in binding_log.read_text(encoding="utf-8").splitlines():
        if line.startswith("ops02_result_hde_ferm008_2_evidence_ready=true"):
            produced_at = "2026-06-24T06:28:13Z"
            break
    entries: list[dict[str, object]] = []
    for entry in EPIC034_PR06_PRIMARY_ARTIFACTS:
        artifact_path = ROOT / str(entry["discovered_physical_path"])
        if not artifact_path.exists():
            continue
        normalized = dict(entry)
        if produced_at is not None and normalized.get("record_type") in {
            "epic034_ops02_smoke_evidence",
            "epic034_pr06_ops02_binding",
        }:
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries


EPIC038_QA_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic038.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic038_doc_deltas.md",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_doc_delta",
        "schema_version": "1.0",
        "notes": "Primary draft/staging binding for DOC_DELTA_PRESENT_OK; governed presence is nonclaiming",
    },
    {
        "artifact_key": "epic038.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic038/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_doc_delta_capture",
        "schema_version": "1.0",
        "notes": "Supporting QA capture for the HDE-EPIC038 doc-delta pair; not the primary token surface and not a token claim",
    },
    {
        "artifact_key": "epic038.release.catalog_manifest",
        "discovered_physical_path": "catalog/manifest.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_release_identity_source",
        "schema_version": "1.0",
        "notes": "Canonical current release source input; exact-head derived attestation remains an external CI artifact and this record makes no token claim",
    },
    {
        "artifact_key": "epic038.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic038/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_token_matrix",
        "schema_version": "1.0",
        "notes": "Deterministic DEV-01 nonclaiming token binding matrix; independent Gate B review required",
    },
    {
        "artifact_key": "epic038.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic038/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_qa_step_logs_manifest",
        "schema_version": "1.0",
        "notes": "HDE-EPIC038 current-state QA step-log manifest; tokenless coverage index only, not acceptance or closeout",
    },
]

EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "epic038.close_report", "discovered_physical_path": "audit/EPIC-038_close_report.md", "epic_id": "HDE-EPIC038", "record_type": "epic038_close_report", "schema_version": "1.0", "tokens": ["TESTS_PASS_OK"]},
    {"artifact_key": "epic038.manifest", "discovered_physical_path": "audit/EPIC-038_MANIFEST.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_close_manifest", "schema_version": "1.0"},
    {"artifact_key": "epic038.acceptance_map", "discovered_physical_path": "docs/acceptance_map_epic038.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_acceptance_map", "schema_version": "1.0"},
    {"artifact_key": "epic038.acceptance_map_viability", "discovered_physical_path": "audit/qa/hde-epic038/acceptance_map_viability.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_acceptance_map_viability", "schema_version": "1.0"},
    {"artifact_key": "epic038.closeout_remediation_ledger", "discovered_physical_path": "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md", "epic_id": "HDE-EPIC038", "record_type": "epic038_closeout_remediation_ledger", "schema_version": "1.0"},
    {"artifact_key": "epic038.qa_precommit_checklist", "discovered_physical_path": "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_qa_precommit_checklist", "schema_version": "1.0", "tokens": ["QA_PRECOMMIT_CHECKLIST_OK"]},
    {"artifact_key": "epic038.qa_postcommit_checklist", "discovered_physical_path": "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_qa_postcommit_checklist", "schema_version": "1.0", "tokens": ["QA_POSTCOMMIT_CHECKLIST_OK"]},
]

EPIC038_CLOSEOUT_KEY_OUTPUTS = {
    "acceptance_map": "docs/acceptance_map_epic038.json",
    "acceptance_map_viability": "audit/qa/hde-epic038/acceptance_map_viability.log",
    "close_manifest": "audit/EPIC-038_MANIFEST.json",
    "close_report": "audit/EPIC-038_close_report.md",
    "closeout_remediation_ledger": "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
    "qa_postcommit_checklist": "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log",
    "qa_precommit_checklist": "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log",
    "token_matrix": "audit/qa/hde-epic038/token_evidence_matrix.md",
}

EPIC038_CLOSEOUT_FAMILY_KEYS = frozenset(
    str(entry["artifact_key"]) for entry in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS
)
EPIC038_CLOSEOUT_FAMILY_PATHS = frozenset(
    str(entry["discovered_physical_path"])
    for entry in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS
)


def _load_epic038_json(path: Path, *, label: str) -> dict[str, object]:
    def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    try:
        payload = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"INVALID_EPIC038_{label}") from exc
    if not isinstance(payload, dict):
        raise SystemExit(f"INVALID_EPIC038_{label}")
    return payload


def _epic038_closeout_package_bytes() -> dict[str, bytes]:
    from tools.evidence import generate_hde_epic038_closeout as closeout

    if dict(closeout.KEY_OUTPUTS) != EPIC038_CLOSEOUT_KEY_OUTPUTS:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_KEY_OUTPUT_CONTRACT")
    package: dict[str, bytes] = {}
    try:
        for package_path in closeout.PACKAGE_PATHS:
            relative = (
                package_path.as_posix()
                if isinstance(package_path, Path)
                else str(package_path)
            )
            package[relative] = (ROOT / relative).read_bytes()
    except OSError as exc:
        raise SystemExit("INCOMPLETE_EPIC038_CLOSEOUT_PACKAGE") from exc
    return package


def _validate_epic038_closeout_bindings() -> None:
    manifest = _load_epic038_json(
        ROOT / "audit/EPIC-038_MANIFEST.json", label="CLOSE_MANIFEST"
    )
    acceptance_map = _load_epic038_json(
        ROOT / "docs/acceptance_map_epic038.json", label="ACCEPTANCE_MAP"
    )
    if (
        manifest.get("epic_id") != "HDE-EPIC038"
        or manifest.get("schema_version") != "1.0"
        or manifest.get("key_outputs") != EPIC038_CLOSEOUT_KEY_OUTPUTS
    ):
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_BINDINGS")
    if (
        acceptance_map.get("artifact_key") != "epic038.acceptance_map"
        or acceptance_map.get("epic_id") != "HDE-EPIC038"
        or acceptance_map.get("schema_version") != "1.0"
    ):
        raise SystemExit("INVALID_EPIC038_ACCEPTANCE_MAP_BINDINGS")

    decision = manifest.get("decision")
    if decision not in {"SATISFIED", "NOT SATISFIED"}:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_DECISION")
    if acceptance_map.get("decision") != decision:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_DECISION_COHERENCE")

    roster = manifest.get("token_roster")
    token_status = manifest.get("token_status")
    records = acceptance_map.get("records")
    if (
        not isinstance(roster, list)
        or not roster
        or any(not isinstance(token, str) or not token for token in roster)
        or len(roster) != len(set(roster))
        or not isinstance(token_status, dict)
        or set(token_status) != set(roster)
        or not isinstance(records, list)
        or [record.get("token") for record in records if isinstance(record, dict)]
        != roster
        or any(not isinstance(record, dict) for record in records)
        or any(
            record.get("status") != token_status.get(record.get("token"))
            for record in records
            if isinstance(record, dict)
        )
        or acceptance_map.get("minimum_follow_up")
        != manifest.get("minimum_follow_up")
    ):
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_ROSTER_COHERENCE")

    for output_path in EPIC038_CLOSEOUT_KEY_OUTPUTS.values():
        if not (ROOT / output_path).is_file():
            raise SystemExit(f"MISSING_EPIC038_CLOSEOUT_OUTPUT:{output_path}")

    try:
        report = (ROOT / "audit/EPIC-038_close_report.md").read_text(
            encoding="utf-8"
        )
        viability = (
            ROOT / "audit/qa/hde-epic038/acceptance_map_viability.log"
        ).read_text(encoding="utf-8")
        ledger = (
            ROOT
            / "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md"
        ).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_TEXT_ARTIFACT") from exc
    if (
        f"Final decision: {decision}" not in report
        or f"DECISION: {decision}" not in viability
    ):
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_DECISION_COHERENCE")

    ledger_prefix = "# HDE-EPIC038 Closeout Remediation Ledger\n\n```json\n"
    ledger_suffix = "\n```\n"
    if not ledger.startswith(ledger_prefix) or not ledger.endswith(ledger_suffix):
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_LEDGER")
    try:
        ledger_payload = json.loads(
            ledger[len(ledger_prefix) : -len(ledger_suffix)]
        )
    except json.JSONDecodeError as exc:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_LEDGER") from exc
    if (
        not isinstance(ledger_payload, dict)
        or ledger_payload.get("artifact_key")
        != "epic038.closeout_remediation_ledger"
        or ledger_payload.get("epic_id") != "HDE-EPIC038"
        or ledger_payload.get("schema")
        != "hde.epic038.closeout_remediation_ledger.v1"
        or not isinstance(ledger_payload.get("entries"), list)
    ):
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_LEDGER")

    # Keep the updater and producer on one exact package-surface contract.
    # Full current-byte validation runs after updater-owned proofs and indexes
    # have been refreshed; doing it here would prevent canonical self-repair.
    from tools.evidence import generate_hde_epic038_closeout as closeout

    previous_root = closeout.ROOT
    closeout.ROOT = ROOT
    try:
        closeout.validate_package_structure(_epic038_closeout_package_bytes())
    except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_PACKAGE_STRUCTURE") from exc
    finally:
        closeout.ROOT = previous_root


def _validate_epic038_closeout_package() -> None:
    """Validate the complete package after canonical updater convergence work."""
    activation_paths = [
        ROOT / str(entry["discovered_physical_path"])
        for entry in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS
    ]
    if not any(path.is_file() or path.is_symlink() for path in activation_paths):
        return

    from tools.evidence import generate_hde_epic038_closeout as closeout

    previous_root = closeout.ROOT
    closeout.ROOT = ROOT
    try:
        closeout._validate_package_for_canonical_updater(
            _epic038_closeout_package_bytes()
        )
    except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
        raise SystemExit("INVALID_EPIC038_CLOSEOUT_PACKAGE") from exc
    finally:
        closeout.ROOT = previous_root


def _load_epic038_closeout_entries() -> list[dict[str, object]]:
    """Activate the DEV-03 family as a unit; a partial family is never valid."""
    paths = [ROOT / str(e["discovered_physical_path"]) for e in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS]
    present = [path.is_file() for path in paths]
    proof_paths = [
        ROOT / f"{entry['discovered_physical_path']}.path_proof.txt"
        for entry in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS
    ]
    aliased = [
        path.relative_to(ROOT).as_posix()
        for path in (*paths, *proof_paths)
        if path.is_symlink()
    ]
    if aliased:
        raise SystemExit("ALIASED_EPIC038_CLOSEOUT_FAMILY:" + ",".join(aliased))
    proof_present = [path.is_file() for path in proof_paths]
    if not any(present) and not any(proof_present):
        return []
    if not all(present):
        missing = [str(e["discovered_physical_path"]) for e, exists in zip(EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS, present) if not exists]
        raise SystemExit("INCOMPLETE_EPIC038_CLOSEOUT_FAMILY:" + ",".join(missing))
    if any(proof_present) and not all(proof_present):
        missing_proofs = [
            path.relative_to(ROOT).as_posix()
            for path, exists in zip(proof_paths, proof_present)
            if not exists
        ]
        raise SystemExit(
            "INCOMPLETE_EPIC038_CLOSEOUT_PROOF_FAMILY:"
            + ",".join(missing_proofs)
        )
    _validate_epic038_closeout_bindings()
    return [dict(entry) for entry in EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS]


EPIC038_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "epic038.pr01.identity_release_id", "discovered_physical_path": "artifacts/identity/release_id.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.identity_release_id_recompute", "discovered_physical_path": "artifacts/identity/release_id_recompute.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.two_run_identity", "discovered_physical_path": "artifacts/parity/two_run_identity.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.service_identity", "discovered_physical_path": "artifacts/identity/service_identity.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.emitter_sha256", "discovered_physical_path": "artifacts/identity/emitter_sha256.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.invocation_sha256", "discovered_physical_path": "artifacts/identity/invocation_sha256.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.bodygraph_release_bindings", "discovered_physical_path": "artifacts/bodygraph/release_bindings.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr01.env_matrix_snapshot_v3", "discovered_physical_path": "artifacts/runtime/env_matrix.snapshot.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr01_evidence", "schema_version": "3"},
]

EPIC038_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "epic038.pr02.reader_cli_ab", "discovered_physical_path": "audit/gates/parity/reader_cli/ab.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0", "notes": "Reader-to-CLI AB deterministic byte proof; predicate evidence only, no acceptance token satisfaction claim"},
    {"artifact_key": "epic038.pr02.reader_cli_ba", "discovered_physical_path": "audit/gates/parity/reader_cli/ba.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.reader_cli_summary", "discovered_physical_path": "audit/gates/parity/reader_cli/summary.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.abba_bytes", "discovered_physical_path": "audit/gates/determinism/abba.bytes", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.tworun_identity", "discovered_physical_path": "audit/gates/determinism/tworun_identity.sha256", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a3_identity_ok", "discovered_physical_path": "artifacts/cards/a3/IDENTITY_OK.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.endpoint_catalog", "discovered_physical_path": "docs/ENDPOINTS_CATALOG.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_catalog_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.endpoint_catalog_sha256", "discovered_physical_path": "docs/ENDPOINTS_CATALOG.json.sha256", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_catalog_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.endpoint_catalog_audit", "discovered_physical_path": "artifacts/audit/ENDPOINTS_CATALOG.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_catalog_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.endpoint_catalog_audit_sha256", "discovered_physical_path": "artifacts/audit/ENDPOINTS_CATALOG.json.sha256", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_catalog_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.endpoints_snapshot", "discovered_physical_path": "artifacts/reader/endpoints_snapshot.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_catalog_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_env_gate", "discovered_physical_path": "artifacts/proofs/endpoints_env_gate_proof.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_success_get", "discovered_physical_path": "artifacts/proofs/success_get.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_success_head", "discovered_physical_path": "artifacts/proofs/success_head.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_success_304", "discovered_physical_path": "artifacts/proofs/success_304.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_success_writers_errors", "discovered_physical_path": "artifacts/proofs/success_writers_errors.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.a7_reader_success_composite", "discovered_physical_path": "artifacts/proofs/reader_success_get_head_304.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_a7_predicate_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr02.reader_success_schema", "discovered_physical_path": "schemas/proofs.reader_success.v1.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr02_schema", "schema_version": "1.0"},
]

EPIC038_PR02_SUPERSEDED_INDEX_KEYS: set[tuple[str, str]] = set()

EPIC038_PR06_SUPERSEDED_INDEX_KEYS = {
    ("sanity.pipeline.log", "artifacts/sanity/sanity.log"),
}

EPIC038_PR04_SUPERSEDED_INDEX_KEYS = {
    ("epic038.pr04.db_ddl_fingerprint", "artifacts/db/ddl_fingerprint.json"),
    ("epic038.pr04.db_grants", "artifacts/db/grants.txt"),
    ("epic038.pr04.db_check_schema", "artifacts/db/check_schema.txt"),
    ("epic038.pr04.db_boundary_view_readonly", "artifacts/db/boundary_view.readonly.proof.txt"),
    ("epic038.pr04.env_connectivity", "artifacts/runtime/env_connectivity.snapshot.json"),
    ("epic032.pr03.env_connectivity", "artifacts/runtime/env_connectivity.snapshot.json"),
    ("epic038.pr04.env_nondev_failure", "artifacts/runtime/env_connectivity.nondev_failure.json"),
    ("epic038.pr04.db_bridge_adapter_selection", "artifacts/db_bridge/adapter_selection.snapshot.json"),
    ("epic038.pr04.db_bridge_provider_parity", "artifacts/db_bridge/provider_parity.proof.json"),
    ("epic032.pr03.provider_parity", "artifacts/db_bridge/provider_parity.proof.json"),
    ("epic038.pr04.bodygraph_source_selection", "artifacts/bodygraph/source_selection.snapshot.json"),
    ("epic038.pr04.bodygraph_source_invariance_ab", "artifacts/bodygraph/source_invariance/ab.json"),
    ("epic038.pr04.bodygraph_source_invariance_ba", "artifacts/bodygraph/source_invariance/ba.json"),
    ("epic038.pr04.bodygraph_source_invariance_summary", "artifacts/bodygraph/source_invariance/summary.json"),
    ("epic038.pr04.bodygraph_refresh_policy", "artifacts/bodygraph/refresh_policy.snapshot.json"),
    ("epic038.pr04.bodygraph_metrics", "artifacts/bodygraph/metrics.snapshot.json"),
    ("epic038.pr04.bodygraph_keys_only_logs", "artifacts/bodygraph/keys_only.logs.sample"),
    ("epic038.pr04.presenter_json_canon_compare", "artifacts/presenter/json_canon_compare.log"),
    ("ops.refusal_proof", "artifacts/proofs/ops_refusal_proof.txt"),
}

EPIC038_PR03_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "rails_gate.keys_only_logs",
        "discovered_physical_path": "artifacts/vendor/rails_gate_keys_only.logs.sample",
        "epic_id": "HDE-EPIC038",
        "record_type": "rails_gate_evidence",
        "schema_version": "1.0",
        "produced_at_utc": "2026-07-13T00:00:00Z",
        "notes": "Reusable HDE rails-gate fixture-backed keys-only vendor log sample",
    },
    {
        "artifact_key": "epic038.pr03.open_rails_abba",
        "discovered_physical_path": "audit/gates/determinism/open_rails_abba.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_pr03_open_rails_abba_proof",
        "schema_version": "1.0",
        "produced_at_utc": "2026-07-14T00:00:00Z",
        "notes": "Fixture-backed open-rails ABBA determinism proof; live vendor calls forbidden and acceptance_token_satisfied=false",
    },
    {
        "artifact_key": "epic038.pr03.open_rails_vendor_abba",
        "discovered_physical_path": "audit/gates/determinism/open_rails_vendor_abba.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_pr03_open_rails_vendor_abba_proof",
        "schema_version": "1.0",
        "notes": "Event-bound PO-authorized live vendor ABBA proof for the exact canonical target with at most two requests; acceptance_token_satisfied=false and no recurring authority",
    },
]


def _load_epic038_pr03_entries() -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for entry in EPIC038_PR03_PRIMARY_ARTIFACTS:
        normalized = dict(entry)
        if normalized["artifact_key"] == "epic038.pr03.open_rails_vendor_abba":
            rel = str(normalized["discovered_physical_path"])
            path = ROOT / rel
            if not path.exists():
                # The live proof is conditional on a fresh PO-authorized event.
                # Repositories and isolated test roots without that event must
                # not acquire a synthetic or dangling index entry.
                continue
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                produced_at = payload["generated_at_utc"]
                if not isinstance(produced_at, str):
                    raise TypeError("generated_at_utc must be a string")
                parsed = _parse_utc_iso8601(produced_at)
            except (
                OSError,
                UnicodeError,
                json.JSONDecodeError,
                KeyError,
                TypeError,
                ValueError,
            ) as exc:
                raise SystemExit("INVALID_EPIC038_PR03_LIVE_PROOF_TIMESTAMP") from exc
            if (
                _isoformat(parsed) != produced_at
                or payload.get("artifact_kind")
                != "hde_epic038_pr03_open_rails_vendor_abba_proof"
                or payload.get("top_level_pass") is not True
                or payload.get("result") != "pass"
                or payload.get("acceptance_token_satisfied") is not False
            ):
                raise SystemExit("INVALID_EPIC038_PR03_LIVE_PROOF_POSTURE")
            normalized["produced_at_utc"] = produced_at
        entries.append(normalized)
    return entries


EPIC038_PR04_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "epic038.pr04.db_check_constraints", "discovered_physical_path": "artifacts/db/check_constraints.txt", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_db_runtime_posture", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr04.bodygraph_vendor_upsert_synthetic", "discovered_physical_path": "artifacts/bodygraph/vendor_upsert.epic038_synthetic.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_synthetic_pair", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr04.bodygraph_db_resolve_synthetic", "discovered_physical_path": "artifacts/bodygraph/db_resolve.epic038_synthetic.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_synthetic_pair", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr04.presenter_db_bridge_compare", "discovered_physical_path": "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_presenter_compare", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr04.presenter_db_bridge_compare_schema", "discovered_physical_path": "schemas/presenter_db_bridge_compare.v1.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_schema", "schema_version": "1.0"},
    {"artifact_key": "bodygraph.source_invariance.schema.run.v2", "discovered_physical_path": "schemas/bodygraph_source_invariance.run.v2.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_schema", "schema_version": "2.0"},
    {"artifact_key": "bodygraph.source_invariance.schema.summary.v2", "discovered_physical_path": "schemas/bodygraph_source_invariance.summary.v2.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_schema", "schema_version": "2.0"},
    {"artifact_key": "epic038.pr04.architecture_snapshot", "discovered_physical_path": "artifacts/architecture/architecture_snapshot.keys_only.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_architecture_snapshot", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr04.architecture_schema", "discovered_physical_path": "schemas/architecture_snapshot.keys_only.v1.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr04_schema", "schema_version": "1.0"},
]

EPIC038_PR05_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "epic038.pr05.v2_mapped_cache.write_transcript", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/write_transcript.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.read_back_transcript", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.canonical_parity", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/canonical_parity.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.no_raw_vendor_payload", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.idempotence", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/idempotence.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.closed_rails_refusal", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.legacy_fallback", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.manifest", "discovered_physical_path": "artifacts/bodygraph/v2_mapped_cache/manifest.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_mapped_cache_evidence", "schema_version": "1.0", "notes": "Predicate-derived PR evidence manifest; no acceptance-token satisfaction claim"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.transcript_schema", "discovered_physical_path": "schemas/bodygraph_v2_mapped_cache_transcript.v1.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_schema", "schema_version": "1.0"},
    {"artifact_key": "epic038.pr05.v2_mapped_cache.manifest_schema", "discovered_physical_path": "schemas/bodygraph_v2_mapped_cache_manifest.v1.json", "epic_id": "HDE-EPIC038", "record_type": "epic038_pr05_schema", "schema_version": "1.0"},
]

HISTORICAL_BRIDGE_NOTES = (
    "Historical bridge/OPS-01 evidence retained for integrity, provenance, readability, "
    "secret safety, and historical nonclaims only; does not prove current service "
    "availability, runtime support, provider parity, fallback, consistency, a current "
    "OPS PASS, or token satisfaction."
)
HISTORICAL_BRIDGE_PRIMARY_PATHS = frozenset(
    {
        "artifacts/db_bridge/adapter_selection.snapshot.json",
        "artifacts/db_bridge/caps.snapshot.json",
        "artifacts/db_bridge/health.json",
        "artifacts/db_bridge/provider_parity.proof.json",
        "artifacts/db_bridge/query_select_1.json",
        "artifacts/db_bridge/root.json",
        "artifacts/db/provider_parity/bridge.json",
        "artifacts/db/provider_parity/direct.json",
        "artifacts/db/provider_parity/summary.json",
        "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json",
        "artifacts/runtime/env_connectivity.nondev_failure.json",
        "artifacts/runtime/env_connectivity.snapshot.json",
        "schemas/presenter_db_bridge_compare.v1.json",
    }
)
EPIC038_OPS03_PRIMARY_BINDINGS = {
    "commands.txt": ("epic038.ops03.commands", "epic038_ops03_text"),
    "stdout.log": ("epic038.ops03.stdout", "epic038_ops03_log"),
    "stderr.log": ("epic038.ops03.stderr", "epic038_ops03_log"),
    "exit_code.txt": ("epic038.ops03.exit_code", "epic038_ops03_text"),
    "env_presence.json": ("epic038.ops03.env_presence", "epic038_ops03_env_presence"),
    "db_posture_summary.json": ("epic038.ops03.db_posture_summary", "epic038_ops03_db_posture"),
    "nonclaims.json": ("epic038.ops03.nonclaims", "epic038_ops03_nonclaims"),
    "result_summary.json": ("epic038.ops03.result_summary", "epic038_ops03_result"),
    "validation_receipt.json": ("epic038.ops03.validation_receipt", "epic038_ops03_validation"),
    "checksums.sha256": ("epic038.ops03.checksums", "epic038_ops03_checksum"),
}
EPIC038_OPS03_SCHEMA_FILES = (
    "hde_epic038_ops03_authorization.v1.json",
    "hde_epic038_ops03_env_presence.v1.json",
    "hde_epic038_ops03_db_posture_summary.v1.json",
    "hde_epic038_ops03_nonclaims.v1.json",
    "hde_epic038_ops03_result_summary.v1.json",
    "hde_epic038_ops03_validation_receipt.v1.json",
    "hde_epic038_ops03_failure_receipt.v1.json",
)
EPIC038_PR06_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic038.pr06r.direct_db_selection",
        "discovered_physical_path": "artifacts/runtime/direct_db_selection.snapshot.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_pr06r_direct_db_selection",
        "schema_version": "1.0",
        "notes": "Deterministic local direct-selection primary; no external I/O, OPS, QA, acceptance-token, PF09, deployment, or closeout claim",
    },
    {
        "artifact_key": "epic038.pr06r.direct_db_selection_schema",
        "discovered_physical_path": "schemas/hde_epic038_direct_db_selection.v1.json",
        "epic_id": "HDE-EPIC038",
        "record_type": "epic038_pr06r_schema",
        "schema_version": "1.0",
    },
    *[
        {
            "artifact_key": f"epic038.pr06.{package.replace('-', '')}.{name.replace('.', '_')}",
            "discovered_physical_path": f"audit/ops/hde-epic038/{package}/{name}",
            "epic_id": "HDE-EPIC038",
            "record_type": "historical_bridge_evidence" if package == "ops-01" else "epic038_pr06_ops_evidence",
            "schema_version": "1.0",
            "notes": HISTORICAL_BRIDGE_NOTES if package == "ops-01" else "Retained OPS-02 mapped-cache evidence bound read-only; no QA, acceptance-token, PF09, deployment, or closeout claim",
        }
        for package, names in {
            "ops-01": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "db_posture_summary.json", "provider_parity.proof.json", "bridge_consistency.result.json", "nonclaims.json", "result_summary.json", "checksums.sha256"),
            "ops-02": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "request_summary.json", "mapped_output_summary.json", "read_back_summary.json", "canonical_parity.log", "idempotence.log", "no_raw_vendor_payload_persistence.log", "legacy_fallback_preservation.log", "nonclaims.json", "result_summary.json", "checksums.sha256"),
        }.items() for name in names
    ],
    *[
        {
            "artifact_key": key,
            "discovered_physical_path": f"audit/ops/hde-epic038/ops-03/{name}",
            "epic_id": "HDE-EPIC038",
            "record_type": record_type,
            "schema_version": "1.0",
            "notes": "Accepted OPS-03 direct DB posture packet primary admitted read-only; no OPS rerun, QA, acceptance-token, PF09, deployment, or closeout claim",
        }
        for name, (key, record_type) in EPIC038_OPS03_PRIMARY_BINDINGS.items()
    ],
    *[
        {
            "artifact_key": f"epic038.ops03.schema.{name[:-5]}",
            "discovered_physical_path": f"schemas/{name}",
            "epic_id": "HDE-EPIC038",
            "record_type": "epic038_ops03_schema",
            "schema_version": "1.0",
        }
        for name in EPIC038_OPS03_SCHEMA_FILES
    ],
]
A7_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "a7.success_encoding_invariance",
        "discovered_physical_path": "artifacts/proofs/success_encoding_invariance.txt",
    },
]

EPIC039_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": f"epic039.pr01.{key}",
        "discovered_physical_path": path,
        "epic_id": "HDE-EPIC039",
        "record_type": "epic039_pr01_canonical_json_evidence",
        "role": role,
        "schema_version": "1.0",
        "tokens": tokens,
        "notes": "Bounded Calcination PR-01 implementation evidence; no QA, acceptance-token, PF09, OPS, or closeout claim",
    }
    for key, path, role, tokens in (
        ("arrays_as_sets_report", "artifacts/canonical/arrays_as_sets_report.log", "report", ["CANONICAL_JSON_GATE_UPDATED_OK"]),
        ("canonical_check", "audit/gates/json_gate/canonical/json_gate_check_log.ndjson", "log", ["JSON_CANONICAL_CHECK_OK"]),
        ("canonical_compare", "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson", "log", ["CANONICAL_JSON_GATE_PASSED_OK"]),
        ("canonical_record", "audit/gates/json_gate/canonical/json_gate_structured_record.json", "summary", ["CANONICAL_JSON_GATE_UPDATED_OK", "CANONICAL_JSON_GATE_PASSED_OK"]),
        ("doc_delta", "audit/docdeltas/hde-epic039_doc_deltas.md", "doc_delta", []),
        ("doc_delta_mirror", "audit/qa/hde-epic039/00_meta/doc_deltas.md", "doc_delta", []),
    )
]
for _epic039_entry in EPIC039_PR01_PRIMARY_ARTIFACTS:
    if not _epic039_entry["tokens"]:
        del _epic039_entry["tokens"]

CLI_CONFORMANCE_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "cli.help.hdctl", "discovered_physical_path": "artifacts/cli/help/hdctl_help.txt"},
    {"artifact_key": "cli.help.showcompat", "discovered_physical_path": "artifacts/cli/help/showcompat_help.txt"},
    {"artifact_key": "cli.help.reject_nonjson", "discovered_physical_path": "artifacts/cli/help/reject_nonjson.txt"},
    {"artifact_key": "cli.install.entrypoints", "discovered_physical_path": "artifacts/cli/install/entrypoints.txt"},
    {"artifact_key": "cli.install.installability_summary", "discovered_physical_path": "artifacts/cli/install/installability_summary.json"},
    {"artifact_key": "cli.showcompat.ab", "discovered_physical_path": "artifacts/cli/ab.json"},
    {"artifact_key": "cli.showcompat.ba", "discovered_physical_path": "artifacts/cli/ba.json"},
    {"artifact_key": "cli.showcompat.summary", "discovered_physical_path": "artifacts/cli/summary.json"},
]

COMPAT_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "compat.conjunction.ab",
        "discovered_physical_path": "artifacts/compat/AB.json",
        "record_type": "compat_parity_payload",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "compat.conjunction.ba",
        "discovered_physical_path": "artifacts/compat/BA.json",
        "record_type": "compat_parity_payload",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "compat.conjunction.identity_hash",
        "discovered_physical_path": "artifacts/compat/identity_hash.txt",
        "record_type": "compat_identity_hash",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "compat.narratives.key_table_10x2",
        "discovered_physical_path": "artifacts/narratives/key_table_10x2.snapshot.json",
        "record_type": "compat_narrative_key_table",
        "schema_version": "1.0",
    }
]

CONJUNCTION_WRITER_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "conjunction.writer.write_readback",
        "discovered_physical_path": "artifacts/writer/conjunction_write_readback.log",
        "record_type": "writer_log",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "conjunction.writer.summary",
        "discovered_physical_path": "artifacts/writer/conjunction_writer_summary.json",
        "record_type": "writer_summary",
        "schema_version": "1.0",
    },
]

LEGACY_NON_BACKDATED_ARTIFACT_RELS: set[str] = {
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.sha256",
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.sha256",
    "audit/gates/topology/orientation_demo.txt",
    "docs/ENDPOINTS_CATALOG.json",
    "docs/ENDPOINTS_CATALOG.json.sha256",
    "artifacts/audit/ENDPOINTS_CATALOG.json",
    "artifacts/audit/ENDPOINTS_CATALOG.json.sha256",
    "artifacts/reader/endpoints_snapshot.json",
    "artifacts/proofs/endpoints_env_gate_proof.log",
    "artifacts/proofs/success_get.txt",
    "artifacts/proofs/success_head.txt",
    "artifacts/proofs/success_304.txt",
    "artifacts/proofs/success_writers_errors.txt",
    "artifacts/proofs/success_encoding_invariance.txt",
    "artifacts/proofs/reader_success_get_head_304.json",
}
EPIC035_PR01_ARTIFACT_RELS: set[str] = {
    "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json",
    "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json",
}
EPIC035_PR02_ARTIFACT_RELS: set[str] = {
    "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
    "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
}
EPIC036_PR01_ARTIFACT_RELS: set[str] = {
    "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
    "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
    "audit/qa/hde-epic036/route_policy_decision.log",
}
NON_BACKDATED_PROOF_RELS: set[str] = {
    *EPIC035_PR01_ARTIFACT_RELS,
    *EPIC035_PR02_ARTIFACT_RELS,
    *EPIC036_PR01_ARTIFACT_RELS,
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.sha256",
    *LEGACY_NON_BACKDATED_ARTIFACT_RELS,
}


def _validate_epic038_pr02_semantics() -> None:
    from tools.evidence import generate_a7_transport_proofs as a7

    summary_path = ROOT / "audit/gates/parity/reader_cli/summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        gate = summary.get("canonical_gate")
        if summary.get("top_level_pass") is not True or not isinstance(gate, dict) or gate.get("passed") is not True or "command" not in gate:
            raise SystemExit("EPIC038_PR02_DETERMINISM_CANON_GATE_INVALID")

    cat = json.loads((ROOT / "docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))
    a7.validate_catalog(cat)
    snap = json.loads((ROOT / "artifacts/reader/endpoints_snapshot.json").read_text(encoding="utf-8"))
    if set(snap) != {"generated_at_utc", "endpoints", "envelope_keys"}:
        raise SystemExit("EPIC038_PR02_ENDPOINT_SNAPSHOT_SHAPE")
    if snap["endpoints"] != ["GET /reader"]:
        raise SystemExit("EPIC038_PR02_ENDPOINT_SNAPSHOT_TARGETS")
    comp = json.loads((ROOT / "artifacts/proofs/reader_success_get_head_304.json").read_text(encoding="utf-8"))
    a7.validate_composite(comp)
    enc = (ROOT / "artifacts/proofs/success_encoding_invariance.txt").read_text(encoding="utf-8")
    for token in ("identity_etag=", "gzip_etag=", "br_etag=", "identity_head_identity_length=", "gzip_head_identity_length=", "br_head_identity_length=", "pass=true"):
        if token not in enc:
            raise SystemExit("EPIC038_PR02_ENCODING_PROOF_INSUFFICIENT")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_path(path: Path) -> str:
    return _sha256_bytes(_read_bytes(path))


def _render_env_pins() -> str:
    ordered = [f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)]
    return ",".join(ordered)


def _isoformat(dt: _dt.datetime) -> str:
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _isoformat_from_timestamp(ts: float) -> str:
    return _isoformat(_dt.datetime.fromtimestamp(ts, tz=_dt.timezone.utc))


def _parse_utc_iso8601(raw: str) -> _dt.datetime:
    dt = _dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo != _dt.timezone.utc:
        raise ValueError("expected UTC tzinfo")
    if dt.microsecond:
        raise ValueError("expected zero microseconds")
    return dt


def _isolated_release_timestamp() -> str | None:
    """Return the immutable cut timestamp for isolated release generation."""

    if os.environ.get("HDE_ISOLATED_RELEASE_BUILD") != "1":
        return None
    try:
        payload = json.loads(
            (ROOT / "catalog/manifest.json").read_text(encoding="utf-8")
        )
        value = payload["built_at_utc"]
        if not isinstance(value, str):
            raise TypeError
        _parse_utc_iso8601(value)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise SystemExit("ISOLATED_RELEASE_TIMESTAMP_INVALID") from exc
    return value


def _load_mirror_roles() -> dict[tuple[str, str], str]:
    roles: dict[tuple[str, str], str] = {}
    if not _path_exists(MIRROR_PATH):
        return roles
    for raw in _read_bytes(MIRROR_PATH).decode("utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        roles[(obj["artifact_key"], obj["discovered_physical_path"])] = obj.get("role", "snapshot")
    return roles


def _load_existing_proof(proof_path: Path) -> dict[str, str]:
    _assert_unaliased_write_path(proof_path)
    if not _path_exists(proof_path):
        return {}
    data: dict[str, str] = {}
    for line in _read_bytes(proof_path).decode("utf-8").splitlines():
        if not line:
            continue
        if ": " not in line:
            raise SystemExit(f"PROOF_FORMAT:{proof_path}")
        key, value = line.split(": ", 1)
        if not key or not value:
            raise SystemExit(f"PROOF_FIELD_EMPTY:{proof_path}:{key}")
        if key in data:
            raise SystemExit(f"PROOF_DUPLICATE_FIELD:{proof_path}:{key}")
        data[key] = value
    return data


def _write_path_proof(
    rel: str,
    *,
    sha256: str,
    size_bytes: int,
    mtime_utc: str | None,
    produced_at: str | None,
    default_produced_at: str,
    check: bool,
    stat_mtime: float,
    extra_fields: Mapping[str, str] | None = None,
) -> tuple[str, str]:
    """Write or validate a path-proof for the given relative path.

    mtime_utc captures provenance at evidence refresh time. Git does not
    preserve that metadata, so later checks validate its UTC shape while
    integrity remains bound by path, sha256, size, and declared extra fields.
    Clone-local stat() values are never evidence inputs.
    """

    proof_rel = f"{rel}.path_proof.txt"
    proof_path = ROOT / proof_rel

    def _normalize_utc(raw: str | None) -> str | None:
        if not raw:
            return None
        try:
            _parse_utc_iso8601(raw)
        except Exception:  # noqa: BLE001
            return None
        return raw

    stat_mtime_iso = _isoformat_from_timestamp(stat_mtime)
    extra_fields = dict(extra_fields or {})
    expected_field_names = {
        "path",
        "size_bytes",
        "sha256",
        "mtime_utc",
        "produced_at_utc",
        *extra_fields,
    }
    existing = _load_existing_proof(proof_path)
    existing_produced = _normalize_utc(existing.get("produced_at_utc"))
    existing_mtime = _normalize_utc(existing.get("mtime_utc"))
    requested_produced = _normalize_utc(produced_at)
    requested_mtime = _normalize_utc(mtime_utc)
    isolated_timestamp = _isolated_release_timestamp()
    if isolated_timestamp is not None:
        requested_produced = isolated_timestamp
        requested_mtime = isolated_timestamp
    if not check and existing:
        try:
            existing_size_matches = int(existing.get("size_bytes", "")) == size_bytes
        except ValueError:
            existing_size_matches = False
        existing_fields_match = (
            set(existing) == expected_field_names
            and all(existing.get(key) == value for key, value in extra_fields.items())
        )
        explicit_produced_matches = (
            isolated_timestamp is not None
            or requested_produced is None
            or existing_produced == requested_produced
        )
        if (
            existing.get("path") == rel
            and existing.get("sha256") == sha256
            and existing_size_matches
            and existing_fields_match
            and explicit_produced_matches
            and existing_mtime is not None
            and existing_produced is not None
        ):
            return proof_rel, existing_produced
    if requested_produced and existing_mtime:
        try:
            if _parse_utc_iso8601(existing_mtime) < _parse_utc_iso8601(requested_produced):
                existing_mtime = None
        except Exception:  # noqa: BLE001
            existing_mtime = None
    produced = requested_produced or existing_produced or default_produced_at
    mtime_floor = requested_mtime or existing_mtime or stat_mtime_iso
    if rel in NON_BACKDATED_PROOF_RELS:
        try:
            if _parse_utc_iso8601(produced) < _parse_utc_iso8601(mtime_floor):
                produced = mtime_floor
        except Exception:  # noqa: BLE001
            produced = default_produced_at
    if check:
        if not _path_exists(proof_path):
            raise SystemExit(f"MISSING_PROOF:{proof_rel}")
        proof = existing
        if set(proof) != expected_field_names:
            raise SystemExit(f"PROOF_FIELDS:{proof_rel}")
        if proof.get("path") != rel:
            raise SystemExit(f"PROOF_PATH:{proof_rel}")
        if proof.get("sha256") != sha256:
            raise SystemExit(f"PROOF_SHA:{proof_rel}")
        try:
            recorded_size = int(proof.get("size_bytes", ""))
        except ValueError as exc:  # pragma: no cover - defensive
            raise SystemExit(f"PROOF_SIZE:{proof_rel}") from exc
        if recorded_size != size_bytes:
            raise SystemExit(f"PROOF_SIZE:{proof_rel}")
        for key, value in extra_fields.items():
            if proof.get(key) != value:
                raise SystemExit(f"PROOF_FIELD:{proof_rel}:{key}")

        mtime_raw = proof.get("mtime_utc")
        produced_raw = proof.get("produced_at_utc")
        if not mtime_raw or not produced_raw:
            raise SystemExit(f"PROOF_FIELDS:{proof_rel}")
        try:
            mtime_parsed = _parse_utc_iso8601(mtime_raw)
            produced_parsed = _parse_utc_iso8601(produced_raw)
        except Exception as exc:  # noqa: BLE001
            raise SystemExit(f"PROOF_MTIME:{proof_rel}") from exc
        if rel in NON_BACKDATED_PROOF_RELS and produced_parsed < mtime_parsed:
            raise SystemExit(f"PROOF_PRODUCED_BACKDATED:{proof_rel}")

        return proof_rel, produced_raw

    mtime = mtime_floor
    proof_lines = [
        f"path: {rel}",
        f"size_bytes: {size_bytes}",
        f"sha256: {sha256}",
    ]
    for key, value in extra_fields.items():
        proof_lines.append(f"{key}: {value}")
    proof_lines.extend(
        [
        f"mtime_utc: {mtime}",
        f"produced_at_utc: {produced}",
        "",
        ]
    )
    proof_text = "\n".join(proof_lines)
    if _path_exists(proof_path):
        existing_text = _read_bytes(proof_path).decode("utf-8")
        if existing_text == proof_text:
            return proof_rel, produced
    _write_if_changed(proof_path, proof_text.encode("utf-8"), check=False)
    return proof_rel, produced


_ALLOWED_INDEX_FIELDS = {
    "artifact_key",
    "discovered_physical_path",
    "epic_id",
    "record_type",
    "role",
    "schema_version",
    "tokens",
    "notes",
    "produced_at_utc",
    "sha256",
    "size_bytes",
}


def _normalize_index_entry(entry: Mapping[str, object]) -> dict[str, object]:
    key = entry.get("artifact_key") or entry.get("title")
    path = entry.get("discovered_physical_path") or entry.get("path")
    if not isinstance(key, str) or not isinstance(path, str):
        raise ValueError(f"Invalid entry: {entry!r}")
    candidate_path = Path(path)
    if candidate_path.is_absolute() or ".." in candidate_path.parts:
        raise ValueError(f"Invalid discovered_physical_path for {key}: {path!r}")

    if "audit/qa/hde-epic024/checks/" in path:
        parts = path.split("/")
        normalized_parts = []
        for part in parts:
            if part.startswith("D") and len(part) > 1 and part[1].isdigit():
                normalized_parts.append(part.lower())
            else:
                normalized_parts.append(part)
        path = "/".join(normalized_parts)

    normalized: dict[str, object] = {
        "artifact_key": key,
        "discovered_physical_path": path,
    }

    for field in _ALLOWED_INDEX_FIELDS:
        if field in {"artifact_key", "discovered_physical_path"}:
            continue
        if field in entry:
            value = entry[field]
            if field == "tokens":
                if not isinstance(value, (list, tuple)):
                    raise ValueError(f"Invalid tokens for {key}: {value!r}")
                if not all(isinstance(token, str) and token for token in value):
                    raise ValueError(f"Invalid tokens for {key}: {value!r}")
                value = sorted(set(value))
            normalized[field] = value
    if path in HISTORICAL_BRIDGE_PRIMARY_PATHS:
        normalized["record_type"] = "historical_bridge_evidence"
        normalized["notes"] = HISTORICAL_BRIDGE_NOTES
        normalized.pop("tokens", None)
    return normalized


def _dedupe_entries(entries: Iterable[Mapping[str, object]]) -> list[dict[str, object]]:
    deduped: dict[tuple[str, str], dict[str, object]] = {}
    for entry in entries:
        normalized = _normalize_index_entry(entry)
        deduped[(normalized["artifact_key"], normalized["discovered_physical_path"])] = normalized
    return sorted(deduped.values(), key=lambda item: (item["artifact_key"], item["discovered_physical_path"]))


def _load_human_index() -> list[dict[str, object]]:
    payload = json.loads(_read_bytes(HUMAN_INDEX).decode("utf-8"))
    payload = [
        entry
        for entry in payload
        if entry.get("artifact_key") not in EPIC038_CLOSEOUT_FAMILY_KEYS
        and entry.get("discovered_physical_path")
        not in EPIC038_CLOSEOUT_FAMILY_PATHS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC031_PR02_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC032_PR03_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC034_PR01_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC034_PR02_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC034_PR03_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC034_PR04_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC034_PR06_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC037_PR05_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC038_PR02_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC038_PR04_SUPERSEDED_INDEX_KEYS
        and (entry.get("artifact_key"), entry.get("discovered_physical_path"))
        not in EPIC038_PR06_SUPERSEDED_INDEX_KEYS
    ]
    return _dedupe_entries(
        [
            *payload,
            *BASELINE_ENTRIES,
            *EPIC022_PRIMARY_ARTIFACTS,
            *EPIC024_PRIMARY_ARTIFACTS,
            *EPIC027_PRIMARY_ARTIFACTS,
            *EPIC028_PRIMARY_ARTIFACTS,
            *EPIC030_PR02_PRIMARY_ARTIFACTS,
            *EPIC031_PR01_PRIMARY_ARTIFACTS,
            *EPIC031_PR02_PRIMARY_ARTIFACTS,
            *EPIC031_PR03_PRIMARY_ARTIFACTS,
            *EPIC030_PR03_PRIMARY_ARTIFACTS,
            *EPIC030_PR04_PRIMARY_ARTIFACTS,
            *EPIC030_PR05_PRIMARY_ARTIFACTS,
            *EPIC032_PR01_PRIMARY_ARTIFACTS,
            *EPIC032_PR02_PRIMARY_ARTIFACTS,
            *EPIC032_PR03_PRIMARY_ARTIFACTS,
            *EPIC032_PR04_PRIMARY_ARTIFACTS,
            *RUNTIME_PRIMARY_ARTIFACTS,
            *_load_epic033_entries(),
            *_load_epic034_pr01_entries(),
            *_load_epic034_pr02_entries(),
            *_load_epic034_pr03_entries(),
            *_load_epic034_pr04_entries(),
            *_load_epic034_pr05_entries(),
            *_load_epic034_pr06_entries(),
            *_load_epic035_pr01_entries(),
            *_load_epic035_pr02_entries(),
            *_load_epic035_pr03_entries(),
            *_load_epic036_pr01_entries(),
            *_load_epic036_pr02_entries(),
            *_load_epic037_pr01_entries(),
            *_load_epic037_pr02_entries(),
            *_load_epic037_pr03_entries(),
            *_load_epic037_pr04_entries(),
            *_load_epic037_ops01_entries(),
            *_load_epic037_pr05_entries(),
            *_load_epic038_closeout_entries(),
            *EPIC038_QA_PRIMARY_ARTIFACTS,
            *EPIC038_PR01_PRIMARY_ARTIFACTS,
            *EPIC038_PR02_PRIMARY_ARTIFACTS,
            *_load_epic038_pr03_entries(),
            *EPIC038_PR04_PRIMARY_ARTIFACTS,
            *EPIC038_PR05_PRIMARY_ARTIFACTS,
            *EPIC038_PR06_PRIMARY_ARTIFACTS,
            *EPIC039_PR01_PRIMARY_ARTIFACTS,
            *A7_PRIMARY_ARTIFACTS,
            *COMPAT_PRIMARY_ARTIFACTS,
            *CLI_CONFORMANCE_ARTIFACTS,
            *CONJUNCTION_WRITER_ARTIFACTS,
        ]
    )


def _render_human_index(entries: Iterable[Mapping[str, object]]) -> bytes:
    normalized = _dedupe_entries(entries)
    return (json.dumps(normalized, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def _role_for(entry: Mapping[str, str], roles: Mapping[tuple[str, str], str]) -> str:
    declared_role = entry.get("role")
    if isinstance(declared_role, str) and declared_role:
        return declared_role
    key = (entry["artifact_key"], entry["discovered_physical_path"])
    if key in roles:
        return roles[key]
    path = entry["discovered_physical_path"]
    if "/proofs/" in path or path.endswith(".proof.txt"):
        return "proof"
    if path.endswith(".log"):
        return "log"
    if "/audit/" in path:
        return "audit"
    return "snapshot"


def _load_epic020_tokens(epic_id: str) -> set[str]:
    if epic_id != "HDE-EPIC020":
        return set()
    if not EPIC020_ACCEPTANCE_MAP.exists():
        raise SystemExit("MISSING:docs/acceptance_map_epic020.json")
    data = json.loads(EPIC020_ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    if data.get("epic_id") != epic_id:
        raise SystemExit(f"EPIC_MISMATCH:{EPIC020_ACCEPTANCE_MAP}")
    tokens = set(data.get("token_status", {}))
    if not tokens:
        raise SystemExit("CANON_GAP:EPIC020_TOKENS")
    return tokens


def _load_epic020_bundle_entries(epic_id: str, allowed_tokens: Sequence[str]) -> list[dict[str, object]]:
    manifests = sorted(EPIC020_BUNDLE_DIR.glob("*.manifest.json"))
    if not manifests:
        raise SystemExit("MISSING_EPIC020_BUNDLES")

    allowed = set(allowed_tokens)
    if not allowed:
        raise SystemExit("CANON_GAP:EPIC020_TOKENS")

    entries: list[dict[str, object]] = []
    for manifest_path in manifests:
        manifest_rel = manifest_path.relative_to(ROOT).as_posix()
        manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        bundle_key = manifest_payload.get("artifact_key")
        bundle_path_rel = manifest_payload.get("bundle_path")
        produced_at = manifest_payload.get("produced_at_utc")
        schema_version = manifest_payload.get("schema_version", "1.0")

        if not bundle_key or not bundle_path_rel:
            raise SystemExit(f"INVALID_MANIFEST:{manifest_rel}")
        if produced_at is None:
            raise SystemExit(f"MISSING_PRODUCED_AT:{manifest_rel}")
        if bundle_key not in allowed:
            raise SystemExit(f"CANON_GAP:{bundle_key}")

        bundle_path = ROOT / bundle_path_rel
        if not bundle_path.exists():
            raise SystemExit(f"MISSING_BUNDLE:{bundle_path_rel}")

        bundle_sha = _sha256_path(bundle_path)
        bundle_size = bundle_path.stat().st_size
        manifest_sha = _sha256_path(manifest_path)
        manifest_size = manifest_path.stat().st_size

        notes = f"EPIC020 Candidate 1 bundle for {bundle_key}"
        tokens = [bundle_key]

        entries.append(
            {
                "artifact_key": bundle_key,
                "discovered_physical_path": bundle_path_rel,
                "epic_id": epic_id,
                "record_type": "epic020_bundle",
                "schema_version": schema_version,
                "produced_at_utc": produced_at,
                "sha256": bundle_sha,
                "size_bytes": bundle_size,
                "tokens": tokens,
                "notes": notes,
            }
        )

        entries.append(
            {
                "artifact_key": bundle_key,
                "discovered_physical_path": manifest_rel,
                "epic_id": epic_id,
                "record_type": "epic020_bundle_manifest",
                "schema_version": schema_version,
                "produced_at_utc": produced_at,
                "sha256": manifest_sha,
                "size_bytes": manifest_size,
                "tokens": tokens,
                "notes": f"EPIC020 Candidate 1 manifest for {bundle_key}",
            }
        )

    return _dedupe_entries(entries)


def _render_mirror(
    entries: Iterable[Mapping[str, str]], *, produced_default: str, check: bool
) -> tuple[bytes, dict[str, object]]:
    """Render the machine mirror with a deterministic self-record.

    The self-record is derived only from the rendered body; it does not depend on
    any on-disk mirror or path-proof state so that a write pass followed by
    `--check` is idempotent when artifacts are unchanged.
    """

    raise_on_duplicate: set[tuple[str, str]] = set()
    records: list[dict[str, object]] = []
    roles = _load_mirror_roles()

    for entry in entries:
        path = entry["discovered_physical_path"]
        rel_path = ROOT / path
        key = (entry["artifact_key"], path)
        if key in raise_on_duplicate:
            raise SystemExit(f"DUPLICATE_MIRROR_KEY:{key}")
        raise_on_duplicate.add(key)

        record: dict[str, object] = dict(entry)
        record.setdefault("artifact_key", entry["artifact_key"])
        record.setdefault("discovered_physical_path", path)
        record.setdefault("produced_at_utc", None)
        record.setdefault("proof_anchor", f"{path}.path_proof.txt")
        record.setdefault("role", _role_for(entry, roles))
        record.setdefault("sha256", None)
        record.setdefault("size_bytes", None)

        if rel_path == MIRROR_PATH:
            record["role"] = "self_record"
            records.append(record)
            continue

        sha = _sha256_bytes(_read_bytes(rel_path))
        proof_anchor, produced_at = _write_path_proof(
            path,
            sha256=sha,
            size_bytes=_size_bytes(rel_path),
            mtime_utc=None,
            produced_at=str(entry.get("produced_at_utc")) if entry.get("produced_at_utc") else None,
            default_produced_at=produced_default,
            check=check,
            stat_mtime=_proof_mtime(
                rel_path, default_produced_at=produced_default
            ),
        )
        record.update({
            "sha256": sha,
            "size_bytes": _size_bytes(rel_path),
            "produced_at_utc": produced_at,
            "proof_anchor": proof_anchor,
        })
        records.append(record)

    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))

    try:
        mirror_key = next(
            i
            for i, rec in enumerate(records)
            if rec["artifact_key"] == "index.machine_mirror"
            and rec["discovered_physical_path"] == MIRROR_REL
        )
    except StopIteration as exc:  # pragma: no cover - defensive
        raise SystemExit("MISSING_SELF_RECORD") from exc

    rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
    body_lines = [line for i, line in enumerate(rendered_lines) if i != mirror_key]
    body_text = "\n".join(body_lines) + ("\n" if body_lines else "")

    mirror_rec = records[mirror_key]
    mirror_rec["produced_at_utc"] = produced_default
    mirror_rec["sha256"] = _sha256_bytes(body_text.encode("utf-8"))

    while True:
        rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
        text = "\n".join(rendered_lines) + "\n"
        size = len(text.encode("utf-8"))
        if size == mirror_rec.get("size_bytes"):
            break
        mirror_rec["size_bytes"] = size

    return ("\n".join(rendered_lines) + "\n").encode("utf-8"), mirror_rec


def _render_orientation(
    entries: Iterable[Mapping[str, object]],
) -> bytes:
    """Render the orientation summary from the final ordered ledger model."""

    human_keys = [
        (str(entry["artifact_key"]), str(entry["discovered_physical_path"]))
        for entry in _dedupe_entries(entries)
    ]
    return (
        "orientation demo (evidence skeleton)\n"
        f"total_artifacts: {len(human_keys)}\n"
        "status: ok\n"
        "sample: INDEX and mirror entries are coherent\n"
    ).encode("utf-8")


def _publish_staged(staged: Mapping[Path, bytes | _StagedDeletion]) -> None:
    """Replace the complete staged model under the active rollback boundary."""

    for path in sorted(staged, key=lambda item: item.as_posix()):
        _assert_unaliased_write_path(path)
        content = staged[path]
        if content is _STAGED_DELETION:
            if path.exists():
                _capture_transaction_preimage(path)
                path.unlink()
            continue
        if path.exists() and path.read_bytes() == content:
            continue
        _capture_transaction_preimage(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        temporary = Path(temporary_name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            if path.exists():
                os.chmod(temporary, _stat.S_IMODE(path.stat().st_mode))
            else:
                os.chmod(temporary, 0o644)
            os.replace(temporary, path)
        finally:
            if temporary.exists():
                temporary.unlink()


def _write_if_changed(path: Path, content: bytes, *, check: bool) -> None:
    _assert_unaliased_write_path(path)
    if _path_exists(path):
        existing = _read_bytes(path)
        if existing == content:
            return
        if check:
            raise SystemExit(f"STALE:{path}")
    elif check:
        raise SystemExit(f"STALE:{path}")
    if _STAGED_VIEW is not None:
        _STAGED_VIEW.stage_bytes(path, content)
        return
    _capture_transaction_preimage(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def _refresh_path_proof(path: Path, *, default_produced_at: str, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    proof_existing = _load_existing_proof(ROOT / f"{rel}.path_proof.txt")
    _write_path_proof(
        rel,
        sha256=_sha256_path(path),
        size_bytes=_size_bytes(path),
        mtime_utc=proof_existing.get("mtime_utc"),
        produced_at=proof_existing.get("produced_at_utc"),
        default_produced_at=default_produced_at,
        check=check,
        stat_mtime=_proof_mtime(path, default_produced_at=default_produced_at),
    )


def _rebind_sanity_log_only(*, produced_default: str, check: bool) -> None:
    """Rebind the canonical sanity log without changing evidence membership."""
    for updater_input in (HUMAN_INDEX, HASH_SENTINEL, MIRROR_PATH):
        _assert_unaliased_write_path(updater_input)
    try:
        human_payload = json.loads(_read_bytes(HUMAN_INDEX).decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit("SANITY_REBIND_HUMAN_INDEX_INVALID") from exc
    if not isinstance(human_payload, list):
        raise SystemExit("SANITY_REBIND_HUMAN_INDEX_INVALID")

    human_keys: list[tuple[str, str]] = []
    for entry in human_payload:
        if not isinstance(entry, dict):
            raise SystemExit("SANITY_REBIND_HUMAN_INDEX_INVALID")
        normalized = _normalize_index_entry(entry)
        human_keys.append(
            (
                str(normalized["artifact_key"]),
                str(normalized["discovered_physical_path"]),
            )
        )
    if human_keys != sorted(human_keys) or len(human_keys) != len(set(human_keys)):
        raise SystemExit("SANITY_REBIND_HUMAN_INDEX_TOPOLOGY_INVALID")

    expected_sentinel = (
        f"{_sha256_path(HUMAN_INDEX)}  docs/evidence/INDEX.json\n"
    ).encode("utf-8")
    try:
        current_sentinel = _read_bytes(HASH_SENTINEL)
    except OSError as exc:
        raise SystemExit("SANITY_REBIND_HUMAN_INDEX_SENTINEL_INVALID") from exc
    if current_sentinel != expected_sentinel:
        raise SystemExit("SANITY_REBIND_HUMAN_INDEX_SENTINEL_INVALID")

    records: list[dict[str, object]] = []
    try:
        mirror_lines = _read_bytes(MIRROR_PATH).decode("utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise SystemExit("SANITY_REBIND_MIRROR_INVALID") from exc
    for raw in mirror_lines:
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit("SANITY_REBIND_MIRROR_INVALID") from exc
        if not isinstance(record, dict):
            raise SystemExit("SANITY_REBIND_MIRROR_INVALID")
        records.append(record)
    try:
        mirror_keys = [
            (str(record["artifact_key"]), str(record["discovered_physical_path"]))
            for record in records
        ]
    except KeyError as exc:
        raise SystemExit("SANITY_REBIND_MIRROR_INVALID") from exc
    if mirror_keys != human_keys:
        raise SystemExit("SANITY_REBIND_TOPOLOGY_DRIFT")

    by_key = {
        (str(record["artifact_key"]), str(record["discovered_physical_path"])): record
        for record in records
    }
    mirror_key = ("index.machine_mirror", MIRROR_REL)
    if SANITY_LOG_KEY not in by_key or mirror_key not in by_key:
        raise SystemExit("SANITY_REBIND_REQUIRED_ROW_MISSING")

    sanity_path = ROOT / SANITY_LOG_REL
    _assert_unaliased_write_path(sanity_path)
    try:
        sanity_bytes = _read_bytes(sanity_path)
    except OSError as exc:
        raise SystemExit("SANITY_REBIND_LOG_MISSING") from exc
    if not sanity_bytes:
        raise SystemExit("SANITY_REBIND_LOG_EMPTY")
    if not sanity_bytes.endswith(b"summary:FAIL\n"):
        raise SystemExit("SANITY_REBIND_LOG_NOT_FAIL")

    sanity_mtime = _proof_mtime(
        sanity_path, default_produced_at=produced_default
    )
    sanity_proof = _load_existing_proof(ROOT / f"{SANITY_LOG_REL}.path_proof.txt")
    proof_anchor, sanity_produced = _write_path_proof(
        SANITY_LOG_REL,
        sha256=_sha256_bytes(sanity_bytes),
        size_bytes=len(sanity_bytes),
        mtime_utc=sanity_proof.get("mtime_utc"),
        produced_at=produced_default,
        default_produced_at=produced_default,
        check=check,
        stat_mtime=sanity_mtime,
    )
    by_key[SANITY_LOG_KEY].update(
        {
            "produced_at_utc": sanity_produced,
            "proof_anchor": proof_anchor,
            "sha256": _sha256_bytes(sanity_bytes),
            "size_bytes": len(sanity_bytes),
        }
    )

    mirror_record = by_key[mirror_key]
    mirror_record["produced_at_utc"] = produced_default
    mirror_record["proof_anchor"] = f"{MIRROR_REL}.path_proof.txt"
    mirror_record["role"] = "self_record"

    self_index = mirror_keys.index(mirror_key)
    rendered = [json.dumps(record, separators=(",", ":"), sort_keys=True) for record in records]
    body_lines = [line for index, line in enumerate(rendered) if index != self_index]
    body_text = "\n".join(body_lines) + ("\n" if body_lines else "")
    mirror_record["sha256"] = _sha256_bytes(body_text.encode("utf-8"))
    while True:
        rendered = [json.dumps(record, separators=(",", ":"), sort_keys=True) for record in records]
        mirror_bytes = ("\n".join(rendered) + "\n").encode("utf-8")
        if mirror_record.get("size_bytes") == len(mirror_bytes):
            break
        mirror_record["size_bytes"] = len(mirror_bytes)
    _write_if_changed(MIRROR_PATH, mirror_bytes, check=check)

    mirror_size = _size_bytes(MIRROR_PATH)
    mirror_mtime = _proof_mtime(
        MIRROR_PATH, default_produced_at=produced_default
    )
    mirror_file_sha = _sha256_path(MIRROR_PATH)
    mirror_sha_bytes = f"{mirror_file_sha}  {MIRROR_REL}\n".encode("utf-8")
    _write_if_changed(MIRROR_SHA_PATH, mirror_sha_bytes, check=check)
    _refresh_path_proof(
        MIRROR_SHA_PATH, default_produced_at=produced_default, check=check
    )
    mirror_proof = _load_existing_proof(ROOT / f"{MIRROR_REL}.path_proof.txt")
    _write_path_proof(
        MIRROR_REL,
        sha256=mirror_file_sha,
        size_bytes=mirror_size,
        mtime_utc=mirror_proof.get("mtime_utc"),
        produced_at=produced_default,
        default_produced_at=produced_default,
        check=check,
        stat_mtime=mirror_mtime,
        extra_fields={"mirror_body_sha256": str(mirror_record["sha256"])},
    )

    _write_path_proof(
        SANITY_LOG_REL,
        sha256=_sha256_bytes(sanity_bytes),
        size_bytes=len(sanity_bytes),
        mtime_utc=None,
        produced_at=None,
        default_produced_at=produced_default,
        check=True,
        stat_mtime=sanity_mtime,
    )
    _refresh_path_proof(
        MIRROR_SHA_PATH, default_produced_at=produced_default, check=True
    )
    _write_path_proof(
        MIRROR_REL,
        sha256=mirror_file_sha,
        size_bytes=mirror_size,
        mtime_utc=None,
        produced_at=None,
        default_produced_at=produced_default,
        check=True,
        stat_mtime=mirror_mtime,
        extra_fields={"mirror_body_sha256": str(mirror_record["sha256"])},
    )


def _run_sanity_log_rebind_transaction() -> None:
    """Publish the failure-log rebind through the atomic ledger boundary."""

    global _STAGED_VIEW
    produced_default = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
    try:
        with _WriteTransaction(ROOT):
            _STAGED_VIEW = _StagedView(ROOT, produced_default)
            _rebind_sanity_log_only(
                produced_default=produced_default, check=False
            )
            _rebind_sanity_log_only(
                produced_default=produced_default, check=True
            )
            staged = dict(_STAGED_VIEW.changes)
            _STAGED_VIEW = None
            _publish_staged(staged)
            _rebind_sanity_log_only(
                produced_default=produced_default, check=True
            )
    finally:
        _STAGED_VIEW = None


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Maintain the evidence index and mirror")
    parser.add_argument("--check", action="store_true", help="Fail if files would change")
    parser.add_argument(
        "--rebind-sanity-log",
        action="store_true",
        help="Rebind only the canonical sanity log after a failed pipeline run",
    )
    parser.add_argument(
        "--epic-id",
        action="append",
        default=[],
        help="Integrate epic-specific governed artifacts (e.g. HDE-EPIC020)",
    )
    args = parser.parse_args(argv)

    ensure_determinism_env()
    print(f"[evidence-index] env pins: {_render_env_pins()}")

    if args.rebind_sanity_log:
        if args.check or args.epic_id:
            parser.error("--rebind-sanity-log cannot be combined with --check or --epic-id")
        _run_sanity_log_rebind_transaction()
        return

    epic_ids = set(args.epic_id)

    def _run_once(*, check: bool) -> None:
        _validate_epic038_pr02_semantics()
        isolated_timestamp = _isolated_release_timestamp()
        produced_default = isolated_timestamp or _isoformat(
            _dt.datetime.now(tz=_dt.timezone.utc)
        )
        mirror_proof_path = MIRROR_PATH.with_suffix(".jsonl.path_proof.txt")
        mirror_proof_existing = _load_existing_proof(mirror_proof_path)
        mirror_produced = mirror_proof_existing.get("produced_at_utc")
        if mirror_produced:
            try:
                _parse_utc_iso8601(mirror_produced)
            except Exception:  # noqa: BLE001
                mirror_produced = None
        if mirror_produced and isolated_timestamp is None:
            produced_default = mirror_produced
        entries = _load_human_index()
        if "HDE-EPIC020" in epic_ids:
            epic020_tokens = _load_epic020_tokens("HDE-EPIC020")
            entries = _dedupe_entries(entries + _load_epic020_bundle_entries("HDE-EPIC020", epic020_tokens))

        index_bytes = _render_human_index(entries)
        _write_if_changed(HUMAN_INDEX, index_bytes, check=check)
        hash_line = f"{_sha256_bytes(index_bytes)}  docs/evidence/INDEX.json\n".encode("utf-8")
        _write_if_changed(HASH_SENTINEL, hash_line, check=check)
        _refresh_path_proof(HUMAN_INDEX, default_produced_at=produced_default, check=check)
        _refresh_path_proof(HASH_SENTINEL, default_produced_at=produced_default, check=check)

        orientation_bytes = _render_orientation(entries)
        _write_if_changed(ORIENTATION_PATH, orientation_bytes, check=check)

        mirror_bytes, mirror_rec = _render_mirror(entries, produced_default=produced_default, check=check)
        mirror_size = len(mirror_bytes)
        mirror_rec["size_bytes"] = mirror_size
        _write_if_changed(MIRROR_PATH, mirror_bytes, check=check)

        mirror_file_sha = _sha256_path(MIRROR_PATH)
        mirror_sha_line = f"{mirror_file_sha}  {MIRROR_REL}\n".encode("utf-8")
        _write_if_changed(MIRROR_SHA_PATH, mirror_sha_line, check=check)
        _refresh_path_proof(MIRROR_SHA_PATH, default_produced_at=produced_default, check=check)

        mirror_body_sha = str(mirror_rec["sha256"])
        proof_anchor, produced_at = _write_path_proof(
            MIRROR_REL,
            sha256=mirror_file_sha,
            size_bytes=_size_bytes(MIRROR_PATH),
            mtime_utc=mirror_proof_existing.get("mtime_utc"),
            produced_at=str(mirror_rec.get("produced_at_utc")),
            default_produced_at=produced_default,
            check=check,
            stat_mtime=_proof_mtime(
                MIRROR_PATH, default_produced_at=produced_default
            ),
            extra_fields={"mirror_body_sha256": mirror_body_sha},
        )
        if proof_anchor != mirror_rec["proof_anchor"]:
            mirror_rec["proof_anchor"] = proof_anchor
            if check:
                raise SystemExit(f"STALE_PROOF:{proof_anchor}")
        if produced_at != mirror_rec["produced_at_utc"]:
            mirror_rec["produced_at_utc"] = produced_at
            if check:
                raise SystemExit(f"STALE_PRODUCED_AT:{MIRROR_REL}")
        if _size_bytes(MIRROR_PATH) != int(mirror_rec["size_bytes"]):
            if check:
                raise SystemExit(f"STALE_SIZE:{MIRROR_REL}")
            mirror_rec["size_bytes"] = _size_bytes(MIRROR_PATH)

    if args.check:
        _run_once(check=True)
        _validate_epic038_closeout_package()
        return

    # Converge in one invocation with a bounded fixed-point loop.
    # Mirror rendering depends on artifacts written by this same updater
    # (notably artifacts/evidence_index.jsonl.sha256 and related path proofs),
    # so a single rewrite is not always sufficient.
    global _STAGED_VIEW
    try:
        with _WriteTransaction(ROOT):
            initial_produced = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
            existing_mirror_proof = _load_existing_proof(
                MIRROR_PATH.with_suffix(".jsonl.path_proof.txt")
            )
            staged_produced = existing_mirror_proof.get(
                "produced_at_utc", initial_produced
            )
            try:
                _parse_utc_iso8601(staged_produced)
            except (TypeError, ValueError):
                staged_produced = initial_produced
            _STAGED_VIEW = _StagedView(ROOT, staged_produced)
            max_passes = 6
            last_error: SystemExit | None = None
            for _ in range(max_passes):
                _run_once(check=False)
                try:
                    _run_once(check=True)
                    last_error = None
                    break
                except SystemExit as exc:
                    last_error = exc

            if last_error is not None:
                raise SystemExit(f"MIRROR_CONVERGENCE_FAILED:{last_error}")
            staged = dict(_STAGED_VIEW.changes)
            _STAGED_VIEW = None
            _publish_staged(staged)
            _run_once(check=True)
            # The legacy closeout validator reads its registered companions
            # directly from the filesystem. Validate only after publication,
            # while the rollback transaction is still active, so it observes
            # one coherent ledger without gaining a second staged-read model.
            _validate_epic038_closeout_package()
    finally:
        _STAGED_VIEW = None


if __name__ == "__main__":
    main()
