"""Deterministic, current-state QA harness primitives."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shlex
import stat as stat_module
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path, PurePosixPath

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

EPIC_RE = re.compile(r"HDE-EPIC([0-9]{3})\Z")
CHECK_RE = re.compile(r"[a-z0-9][a-z0-9._-]*\Z")
LEGACY_CHECK_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
PF_TITLE_RE = re.compile(
    r"PF[0-9]{2}(?:\.[0-9]+)?-(?:Canon|Reference)-[A-Za-z0-9][A-Za-z0-9-]*\Z"
)
TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:[_-][A-Z0-9]+)+\b")
PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)(?![A-Za-z0-9_./-])"
)
EXACT_RELATIVE_PATH_RE = re.compile(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\Z")
PLACEHOLDER_RE = re.compile(r"(?:<[^>]+>|\{[^}]+\}|\bTBD\b|\be\.g\.)", re.IGNORECASE)
TOKEN_DECLARATION_RE = re.compile(
    r"^\s*(?:[*+-]\s+)?\*\*`?"
    r"(?P<name>[A-Z][A-Z0-9]*(?:(?:\\_|_|-)[A-Z0-9]+)+)"
    r"`?(?:(?:\*\*\s*[—–-])|(?:\s+[—–-].*\*\*))",
    re.VERBOSE,
)
UTC_TIMESTAMP_RE = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
ADMITTED_ENV_KEYS = frozenset((*DETERMINISM_ENV_PINS.keys(), "APP_ENV"))
NONCLAIM_EXPLANATION = "token_claim_posture: intended tokens are recorded but not claimed by this PR-03 receipt"


class Status(str, Enum):
    PASS = "PASS"
    FAIL_BEHAVIOR = "FAIL_BEHAVIOR"
    FAIL_TOOLING = "FAIL_TOOLING"
    TOOLING_BLOCKED = "TOOLING_BLOCKED"
    PARKED = "PARKED"


@dataclass(frozen=True)
class HarnessConfig:
    epic_id: str
    repo_root: Path | None = None
    step_names: Sequence[str] = ()

    def __post_init__(self) -> None:
        match = EPIC_RE.fullmatch(self.epic_id)
        if not match:
            raise ValueError("epic_id must match HDE-EPIC<NNN>")
        root = (self.repo_root or Path(__file__).resolve().parents[2]).resolve()
        if not root.is_dir():
            raise ValueError("repository root is unavailable")
        object.__setattr__(self, "repo_root", root)
        object.__setattr__(self, "epic_number", match.group(1))
        object.__setattr__(
            self, "qa_root", root / "audit" / "qa" / f"hde-epic{match.group(1)}"
        )
        object.__setattr__(
            self,
            "acceptance_map_path",
            root / "docs" / f"acceptance_map_epic{match.group(1)}.json",
        )
        object.__setattr__(
            self, "token_matrix_path", self.qa_root / "token_evidence_matrix.md"
        )
        object.__setattr__(
            self, "viability_ledger_path", self.qa_root / "acceptance_map_viability.log"
        )


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: Status
    status_reason: str = ""
    check_name: str = ""
    command: tuple[str, ...] | tuple[tuple[str, ...], ...] = ()
    command_provenance: str = "Not executed"
    exit_code: int | None = None
    output: str = ""
    evidence_artifacts: tuple[str, ...] = ()
    intended_tokens: tuple[str, ...] = ()
    pf_refs: tuple[str, ...] = ()
    captured_env: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        validate_check_id(self.check_id)
        if not isinstance(self.status, Status):
            raise ValueError("status must be a Status")  # noqa: TRY004
        _validate_command(self.command)
        if self.exit_code is not None and (
            not isinstance(self.exit_code, int) or isinstance(self.exit_code, bool)
        ):
            raise ValueError("exit_code must be an integer or None")
        if bool(self.command) != (self.exit_code is not None):
            raise ValueError("command execution and exit_code presence disagree")
        if any(
            not isinstance(reference, str) or not PF_TITLE_RE.fullmatch(reference)
            for reference in self.pf_refs
        ):
            raise ValueError("pf_refs must contain exact in-document PF titles")
        _validate_captured_env(self.captured_env)


@dataclass(frozen=True)
class AcceptanceTokenEntry:
    name: str
    owner_pf: str
    evidence_titles: tuple[str, ...]
    status: str | None


@dataclass(frozen=True)
class MatrixRow:
    token_name: str
    owner_pf: str
    evidence_artifacts: tuple[str, ...]
    ci_tests_jobs: tuple[str, ...]
    qa_root_logs: tuple[str, ...]
    status: str
    notes: str


@dataclass(frozen=True)
class PytestCollectionRequest:
    selectors: tuple[str, ...]
    options: tuple[str, ...]


@dataclass(frozen=True)
class ReferenceDiagnostic:
    token: str
    source_field: str
    item_index: int
    value: str
    status: Status
    reason: str = ""
    resolved_path: str | None = None

    def as_dict(self) -> dict[str, object]:
        return {
            "item_index": self.item_index,
            "reason": self.reason,
            "resolved_path": self.resolved_path,
            "source_field": self.source_field,
            "status": self.status.value,
            "token": self.token,
            "value": self.value,
        }


@dataclass(frozen=True)
class _EvidenceGraphRow:
    artifact_key: str
    declared_path: str
    payload: Mapping[str, object]
    raw_line: bytes | None = None


@dataclass(frozen=True)
class _EvidenceGraphSnapshot:
    status: Status
    reason: str
    human_by_path: Mapping[str, tuple[_EvidenceGraphRow, ...]]
    mirror_by_path: Mapping[str, tuple[_EvidenceGraphRow, ...]]
    mirror_rows: tuple[_EvidenceGraphRow, ...]
    human_bytes: bytes
    mirror_bytes: bytes
    self_proof_bytes: bytes


@dataclass(frozen=True)
class _RepositoryFileSnapshot:
    lexical_path: Path
    resolved_path: Path
    lexical_fingerprint: tuple[int, int, int, int, int]
    resolved_fingerprint: tuple[int, int, int, int, int]
    symlink_target: str | None
    payload: bytes


_MIRROR_REQUIRED_FIELDS = frozenset(
    {
        "artifact_key",
        "discovered_physical_path",
        "produced_at_utc",
        "proof_anchor",
        "role",
        "sha256",
        "size_bytes",
    }
)
_MIRROR_OPTIONAL_FIELDS = frozenset(
    {"epic_id", "notes", "record_type", "schema_version", "tokens"}
)
_HUMAN_INDEX_OPTIONAL_FIELDS = frozenset(
    {
        "epic_id",
        "notes",
        "produced_at_utc",
        "record_type",
        "role",
        "schema_version",
        "sha256",
        "size_bytes",
        "tokens",
    }
)

_STRING_METADATA_FIELDS = frozenset(
    {"epic_id", "notes", "record_type", "role", "schema_version"}
)
_ALLOWED_GOVERNED_PRIMARY_SYMLINKS = {
    "docs/ENDPOINTS_CATALOG.json": "../artifacts/audit/ENDPOINTS_CATALOG.json",
}
_MAX_SYMLINK_HOPS = 40
_SYMLINK_REPOSITORY_ESCAPE = "symlink target escapes repository"


def _stat_fingerprint(metadata: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def _repo_symlink_resolution_error(repo_root: Path, path: Path) -> str:
    """Detect unsafe in-repository symlink expansion without following links."""

    try:
        relative = path.relative_to(repo_root)
    except ValueError:
        return ""
    pending = list(relative.parts)
    current = repo_root
    visited: set[tuple[Path, tuple[str, ...]]] = set()
    hops = 0
    while pending:
        component = pending.pop(0)
        if component in {"", "."}:
            continue
        if component == "..":
            if current == repo_root:
                return "symlink target traverses above repository root"
            current = current.parent
            continue
        candidate = current / component
        try:
            candidate.relative_to(repo_root)
        except ValueError:
            return ""
        try:
            metadata = os.lstat(candidate)
        except (FileNotFoundError, NotADirectoryError):
            return ""
        except OSError as exc:
            return f"symlink path inspection failed: {exc}"
        if not stat_module.S_ISLNK(metadata.st_mode):
            current = candidate
            continue
        hops += 1
        resolution_state = (candidate, tuple(pending))
        if resolution_state in visited or hops > _MAX_SYMLINK_HOPS:
            return (
                "symlink loop detected at "
                f"{candidate.relative_to(repo_root).as_posix()}"
            )
        visited.add(resolution_state)
        try:
            target = Path(os.readlink(candidate))
        except OSError as exc:
            return f"symlink target inspection failed: {exc}"
        if target.is_absolute():
            try:
                target_relative = target.relative_to(repo_root)
            except ValueError:
                return _SYMLINK_REPOSITORY_ESCAPE
            current = repo_root
            pending[:0] = target_relative.parts
        else:
            pending[:0] = target.parts
    return ""


def _read_stable_repo_file_bytes(
    repo_root: Path,
    path: Path,
    *,
    subject: str,
) -> tuple[Status, str, bytes | None]:
    """Read a regular repo file without following any lexical-path symlink."""

    try:
        relative = path.relative_to(repo_root)
    except ValueError:
        return Status.FAIL_TOOLING, f"{subject} path escapes repository", None
    if not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        return Status.FAIL_TOOLING, f"{subject} path is not canonical", None
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    if not nofollow or not directory or os.open not in os.supports_dir_fd:
        return (
            Status.FAIL_TOOLING,
            f"{subject} cannot be opened with repository no-follow guarantees",
            None,
        )

    close_on_exec = getattr(os, "O_CLOEXEC", 0)
    nonblock = getattr(os, "O_NONBLOCK", 0)
    directory_flags = os.O_RDONLY | close_on_exec | directory | nofollow
    file_flags = os.O_RDONLY | close_on_exec | nonblock | nofollow
    descriptors: list[int] = []
    directory_edges: list[tuple[int, str, int]] = []
    try:
        root_descriptor = os.open(repo_root, directory_flags)
        descriptors.append(root_descriptor)
        parent_descriptor = root_descriptor
        for component in relative.parts[:-1]:
            child_descriptor = os.open(
                component,
                directory_flags,
                dir_fd=parent_descriptor,
            )
            descriptors.append(child_descriptor)
            child_metadata = os.fstat(child_descriptor)
            if not stat_module.S_ISDIR(child_metadata.st_mode):
                return (
                    Status.FAIL_TOOLING,
                    f"{subject} path contains a non-directory component",
                    None,
                )
            directory_edges.append(
                (parent_descriptor, component, child_descriptor)
            )
            parent_descriptor = child_descriptor

        final_component = relative.parts[-1]
        file_descriptor = os.open(
            final_component,
            file_flags,
            dir_fd=parent_descriptor,
        )
        descriptors.append(file_descriptor)
        before = os.fstat(file_descriptor)
        if not stat_module.S_ISREG(before.st_mode):
            return Status.FAIL_TOOLING, f"{subject} is not a regular file", None
        with os.fdopen(file_descriptor, "rb", closefd=False) as stream:
            payload = stream.read()
        after = os.fstat(file_descriptor)
        current = os.stat(
            final_component,
            dir_fd=parent_descriptor,
            follow_symlinks=False,
        )
        if (
            not stat_module.S_ISREG(current.st_mode)
            or _stat_fingerprint(before) != _stat_fingerprint(after)
            or _stat_fingerprint(after) != _stat_fingerprint(current)
            or len(payload) != after.st_size
        ):
            return (
                Status.FAIL_TOOLING,
                f"{subject} changed identity or bytes while being evaluated",
                None,
            )
        for parent_fd, component, child_fd in reversed(directory_edges):
            opened = os.fstat(child_fd)
            linked = os.stat(
                component,
                dir_fd=parent_fd,
                follow_symlinks=False,
            )
            if (
                not stat_module.S_ISDIR(linked.st_mode)
                or (opened.st_dev, opened.st_ino) != (linked.st_dev, linked.st_ino)
            ):
                return (
                    Status.FAIL_TOOLING,
                    f"{subject} path changed identity while being evaluated",
                    None,
                )
        opened_root = os.fstat(root_descriptor)
        linked_root = repo_root.stat()
        if (opened_root.st_dev, opened_root.st_ino) != (
            linked_root.st_dev,
            linked_root.st_ino,
        ):
            return (
                Status.FAIL_TOOLING,
                f"{subject} repository root changed identity while being evaluated",
                None,
            )
        return Status.PASS, "", payload
    except FileNotFoundError as exc:
        return Status.TOOLING_BLOCKED, f"{subject} is unavailable: {exc}", None
    except OSError as exc:
        return (
            Status.FAIL_TOOLING,
            f"{subject} could not be opened without following aliases: {exc}",
            None,
        )
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _read_stable_acceptance_file(
    repo_root: Path,
    path: Path,
    *,
    subject: str,
) -> tuple[Status, str, _RepositoryFileSnapshot | None]:
    """Capture one safe lexical artifact path, allowing a final in-repo symlink."""

    try:
        relative = path.relative_to(repo_root)
    except ValueError:
        return Status.FAIL_TOOLING, f"{subject} path escapes repository", None
    if not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        return Status.FAIL_TOOLING, f"{subject} path is not canonical", None

    current = path.parent
    while current != repo_root:
        try:
            if current.is_symlink():
                return (
                    Status.FAIL_TOOLING,
                    f"{subject} parent path is aliased: {current.relative_to(repo_root)}",
                    None,
                )
        except OSError as exc:
            return Status.FAIL_TOOLING, f"{subject} parent path is unsafe: {exc}", None
        if current == current.parent:  # pragma: no cover - defensive
            return Status.FAIL_TOOLING, f"{subject} parent path escapes repository", None
        current = current.parent

    try:
        lexical_before = path.lstat()
    except FileNotFoundError as exc:
        return Status.TOOLING_BLOCKED, f"{subject} is unavailable: {exc}", None
    except OSError as exc:
        return Status.FAIL_TOOLING, f"{subject} path is unsafe: {exc}", None
    symlink_target: str | None = None
    if stat_module.S_ISLNK(lexical_before.st_mode):
        try:
            symlink_target = os.readlink(path)
            allowed_target = _ALLOWED_GOVERNED_PRIMARY_SYMLINKS.get(
                relative.as_posix()
            )
            if allowed_target is None or symlink_target != allowed_target:
                return (
                    Status.FAIL_TOOLING,
                    f"{subject} is not an approved governed-primary symlink",
                    None,
                )
            # Preserve the one approved lexical hop.  Resolving the complete
            # chain here would hide a second symlink at the governed payload
            # path (or in one of its parents) from the no-follow reader below.
            resolved = Path(os.path.abspath(path.parent / symlink_target))
            resolved.relative_to(repo_root)
        except (OSError, ValueError) as exc:
            return Status.FAIL_TOOLING, f"{subject} symlink escapes repository: {exc}", None
    elif stat_module.S_ISREG(lexical_before.st_mode):
        resolved = path
    else:
        return Status.FAIL_TOOLING, f"{subject} is not a regular file", None

    try:
        resolved_before = resolved.lstat()
    except OSError as exc:
        return Status.FAIL_TOOLING, f"{subject} target is unsafe: {exc}", None
    if not stat_module.S_ISREG(resolved_before.st_mode):
        return Status.FAIL_TOOLING, f"{subject} target is not a regular file", None
    status, reason, payload = _read_stable_repo_file_bytes(
        repo_root,
        resolved,
        subject=subject,
    )
    if status is not Status.PASS or payload is None:
        return status, reason, None
    try:
        lexical_after = path.lstat()
        current_target = os.readlink(path) if symlink_target is not None else None
        current_resolved = (
            Path(os.path.abspath(path.parent / current_target))
            if current_target is not None
            else path
        )
        resolved_after = resolved.lstat()
    except (OSError, RuntimeError) as exc:
        return Status.FAIL_TOOLING, f"{subject} changed identity during evaluation: {exc}", None
    if (
        _stat_fingerprint(lexical_before) != _stat_fingerprint(lexical_after)
        or _stat_fingerprint(resolved_before) != _stat_fingerprint(resolved_after)
        or current_target != symlink_target
        or current_resolved != resolved
    ):
        return (
            Status.FAIL_TOOLING,
            f"{subject} changed identity during evaluation",
            None,
        )
    return (
        Status.PASS,
        "",
        _RepositoryFileSnapshot(
            lexical_path=path,
            resolved_path=resolved,
            lexical_fingerprint=_stat_fingerprint(lexical_after),
            resolved_fingerprint=_stat_fingerprint(resolved_after),
            symlink_target=symlink_target,
            payload=payload,
        ),
    )


def _aliased_repo_path_reason(repo_root: Path, path: Path) -> str:
    """Return why a lexical repository path is aliased or escapes, if any."""

    try:
        path.relative_to(repo_root)
    except ValueError:
        return "path escapes repository"
    current = path
    while current != repo_root:
        if current.is_symlink():
            return f"path is or contains a symlink: {current.relative_to(repo_root)}"
        if current == current.parent:  # pragma: no cover - defensive
            return "path parent chain does not reach repository root"
        current = current.parent
    try:
        path.resolve().relative_to(repo_root)
    except (OSError, RuntimeError, ValueError):
        return "path resolves outside repository or cannot be resolved safely"
    return ""


def _metadata_type_error(payload: Mapping[str, object], *, subject: str) -> str:
    for field in sorted(_STRING_METADATA_FIELDS & set(payload)):
        if not isinstance(payload[field], str):
            return f"{subject} {field} metadata must be a string"
    produced_at = payload.get("produced_at_utc")
    if "produced_at_utc" in payload and not _valid_graph_timestamp(produced_at):
        return f"{subject} produced_at_utc metadata is invalid"
    sha256 = payload.get("sha256")
    if "sha256" in payload and (
        not isinstance(sha256, str) or SHA256_RE.fullmatch(sha256) is None
    ):
        return f"{subject} sha256 metadata is invalid"
    size_bytes = payload.get("size_bytes")
    if "size_bytes" in payload and (
        not isinstance(size_bytes, int)
        or isinstance(size_bytes, bool)
        or size_bytes < 0
    ):
        return f"{subject} size_bytes metadata is invalid"
    tokens = payload.get("tokens")
    if "tokens" in payload and (
        not isinstance(tokens, list)
        or not tokens
        or any(not isinstance(token, str) or not token for token in tokens)
        or tokens != sorted(set(tokens))
    ):
        return f"{subject} tokens metadata is invalid"
    return ""


def _lexical_graph_path(config: HarnessConfig, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("ledger path is missing or non-string")
    if value.startswith(("/", "~")) or "\\" in value:
        raise ValueError("ledger path is not repository-relative")
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or not pure.parts
        or ".." in pure.parts
        or pure.as_posix() != value
    ):
        raise ValueError("ledger path is not a canonical lexical repository path")
    loop_reason = _repo_symlink_resolution_error(
        config.repo_root, config.repo_root / pure
    )
    if loop_reason:
        if loop_reason == _SYMLINK_REPOSITORY_ESCAPE:
            raise ValueError("ledger path escapes repository")
        raise ValueError(f"ledger path cannot be resolved safely: {loop_reason}")
    try:
        target = (config.repo_root / pure).resolve()
    except (OSError, RuntimeError) as exc:
        raise ValueError("ledger path cannot be resolved safely") from exc
    try:
        target.relative_to(config.repo_root)
    except ValueError as exc:
        raise ValueError("ledger path escapes repository") from exc
    return value


def _graph_rows_by_path(
    rows: Sequence[_EvidenceGraphRow],
) -> dict[str, tuple[_EvidenceGraphRow, ...]]:
    grouped: dict[str, list[_EvidenceGraphRow]] = {}
    for row in rows:
        grouped.setdefault(row.declared_path, []).append(row)
    return {path: tuple(items) for path, items in grouped.items()}


def _unavailable_graph_snapshot(reason: str) -> _EvidenceGraphSnapshot:
    return _EvidenceGraphSnapshot(
        Status.TOOLING_BLOCKED, reason, {}, {}, (), b"", b"", b""
    )


def _invalid_graph_snapshot(reason: str) -> _EvidenceGraphSnapshot:
    return _EvidenceGraphSnapshot(
        Status.FAIL_TOOLING, reason, {}, {}, (), b"", b"", b""
    )


def _mirror_record_error(payload: Mapping[str, object], declared_path: str) -> str:
    keys = set(payload)
    missing = _MIRROR_REQUIRED_FIELDS - keys
    unknown = keys - (_MIRROR_REQUIRED_FIELDS | _MIRROR_OPTIONAL_FIELDS)
    if missing or unknown:
        return (
            "Machine Mirror record has an invalid field set for "
            f"{declared_path}: missing={sorted(missing)!r}, "
            f"unknown={sorted(unknown)!r}"
        )
    proof_anchor = payload.get("proof_anchor")
    expected_proof = f"{declared_path}.path_proof.txt"
    if not isinstance(proof_anchor, str) or proof_anchor != expected_proof:
        return f"Machine Mirror proof_anchor does not name sibling proof: {expected_proof}"
    role = payload.get("role")
    if not isinstance(role, str) or not role:
        return "Machine Mirror role is invalid"
    produced_at = payload.get("produced_at_utc")
    if not _valid_graph_timestamp(produced_at):
        return "Machine Mirror produced_at_utc is invalid"
    sha256 = payload.get("sha256")
    if not isinstance(sha256, str) or SHA256_RE.fullmatch(sha256) is None:
        return "Machine Mirror sha256 is invalid"
    size_bytes = payload.get("size_bytes")
    if (
        not isinstance(size_bytes, int)
        or isinstance(size_bytes, bool)
        or size_bytes < 0
    ):
        return "Machine Mirror size_bytes is invalid"
    return _metadata_type_error(payload, subject="Machine Mirror")


def _parse_path_proof_bytes(
    payload: bytes,
) -> tuple[Status, str, dict[str, str] | None]:
    try:
        text = payload.decode("utf-8")
    except UnicodeError as exc:
        return Status.FAIL_TOOLING, f"sibling path proof is not UTF-8: {exc}", None
    proof: dict[str, str] = {}
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line:
            continue
        if ": " not in line:
            return (
                Status.FAIL_TOOLING,
                f"sibling path proof line {line_number} is malformed",
                None,
            )
        key, value = line.split(": ", 1)
        if not key or not value:
            return (
                Status.FAIL_TOOLING,
                f"sibling path proof line {line_number} has an empty field",
                None,
            )
        if key in proof:
            return (
                Status.FAIL_TOOLING,
                f"sibling path proof has duplicate field: {key}",
                None,
            )
        proof[key] = value
    required = {"path", "sha256", "size_bytes", "mtime_utc", "produced_at_utc"}
    missing = required - set(proof)
    if missing:
        return (
            Status.FAIL_TOOLING,
            f"sibling path proof is missing required fields: {sorted(missing)}",
            None,
        )
    return Status.PASS, "", proof


def _read_path_proof(
    config: HarnessConfig, proof_path: Path
) -> tuple[Status, str, dict[str, str] | None, bytes | None]:
    alias_reason = _aliased_repo_path_reason(config.repo_root, proof_path)
    if alias_reason:
        return (
            Status.FAIL_TOOLING,
            f"sibling path proof is not a regular repository file: {alias_reason}",
            None,
            None,
        )
    status, reason, payload = _read_stable_repo_file_bytes(
        config.repo_root,
        proof_path,
        subject="sibling path proof",
    )
    if status is not Status.PASS or payload is None:
        if status is Status.TOOLING_BLOCKED:
            reason = "sibling path proof is missing or empty"
        return status, reason, None, None
    if not payload:
        return (
            Status.TOOLING_BLOCKED,
            "sibling path proof is missing or empty",
            None,
            None,
        )
    proof_status, proof_reason, proof = _parse_path_proof_bytes(payload)
    return proof_status, proof_reason, proof, payload


def _path_proof_error(
    proof: Mapping[str, str],
    *,
    declared_path: str,
    require_mirror_body: bool,
) -> str:
    if proof.get("path") != declared_path:
        return "sibling path proof records the wrong artifact path"
    if SHA256_RE.fullmatch(proof.get("sha256", "")) is None:
        return "sibling path proof sha256 is invalid"
    if re.fullmatch(r"0|[1-9][0-9]*", proof.get("size_bytes", "")) is None:
        return "sibling path proof size_bytes is invalid"
    if not _valid_graph_timestamp(proof.get("mtime_utc")) or not _valid_graph_timestamp(
        proof.get("produced_at_utc")
    ):
        return "sibling path proof timestamp is invalid"
    body_sha = proof.get("mirror_body_sha256")
    if require_mirror_body:
        if body_sha is None or SHA256_RE.fullmatch(body_sha) is None:
            return "Machine Mirror path proof body hash is invalid"
    elif body_sha is not None:
        return "non-self path proof contains Machine Mirror self-record hash"
    return ""


def _load_evidence_graph(config: HarnessConfig) -> _EvidenceGraphSnapshot:
    human_path = config.repo_root / "docs/evidence/INDEX.json"
    mirror_path = config.repo_root / "artifacts/evidence_index.jsonl"
    graph_bytes: dict[str, bytes] = {}
    graph_failures: list[tuple[Status, str]] = []
    for label, path in (
        ("Human Evidence Index", human_path),
        ("Machine Evidence Mirror", mirror_path),
    ):
        status, reason, payload = _read_stable_repo_file_bytes(
            config.repo_root,
            path,
            subject=label,
        )
        if status is not Status.PASS or payload is None:
            graph_failures.append((status, reason))
        elif not payload:
            graph_failures.append((Status.TOOLING_BLOCKED, f"{label} is empty"))
        else:
            graph_bytes[label] = payload
    if graph_failures:
        reason = "; ".join(item[1] for item in graph_failures)
        if any(item[0] is Status.FAIL_TOOLING for item in graph_failures):
            return _invalid_graph_snapshot(reason)
        return _unavailable_graph_snapshot(reason)
    human_bytes = graph_bytes["Human Evidence Index"]
    mirror_bytes = graph_bytes["Machine Evidence Mirror"]

    try:
        human_payload = _loads_json_strict(human_bytes.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        return _invalid_graph_snapshot(f"Human Evidence Index is malformed: {exc}")
    if not isinstance(human_payload, list):
        return _invalid_graph_snapshot("Human Evidence Index must be a JSON list")
    if not human_payload:
        return _unavailable_graph_snapshot("Human Evidence Index is empty")
    canonical_human_bytes = (
        json.dumps(human_payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    if human_bytes != canonical_human_bytes:
        return _invalid_graph_snapshot(
            "Human Evidence Index is not canonical JSON with a final LF"
        )

    human_rows: list[_EvidenceGraphRow] = []
    human_pairs: set[tuple[str, str]] = set()
    for row_number, payload in enumerate(human_payload, start=1):
        if not isinstance(payload, dict):
            return _invalid_graph_snapshot(
                f"Human Evidence Index row {row_number} is not an object"
            )
        artifact_key = payload.get("artifact_key")
        if not isinstance(artifact_key, str) or not artifact_key:
            return _invalid_graph_snapshot(
                f"Human Evidence Index row {row_number} has an invalid artifact_key"
            )
        try:
            declared_path = _lexical_graph_path(
                config, payload.get("discovered_physical_path")
            )
        except ValueError as exc:
            return _invalid_graph_snapshot(
                f"Human Evidence Index row {row_number} has an invalid path: {exc}"
            )
        unknown = set(payload) - {
            "artifact_key",
            "discovered_physical_path",
            *_HUMAN_INDEX_OPTIONAL_FIELDS,
        }
        if unknown:
            return _invalid_graph_snapshot(
                f"Human Evidence Index row {row_number} has unknown fields: "
                f"{sorted(unknown)}"
            )
        metadata_error = _metadata_type_error(payload, subject="Human Index")
        if metadata_error:
            return _invalid_graph_snapshot(
                f"Human Evidence Index row {row_number} is invalid: {metadata_error}"
            )
        pair = (artifact_key, declared_path)
        if pair in human_pairs:
            return _invalid_graph_snapshot(
                f"Human Evidence Index has duplicate key/path pair: {pair!r}"
            )
        human_pairs.add(pair)
        human_rows.append(_EvidenceGraphRow(artifact_key, declared_path, payload))

    if [
        (row.artifact_key, row.declared_path) for row in human_rows
    ] != sorted((row.artifact_key, row.declared_path) for row in human_rows):
        return _invalid_graph_snapshot(
            "Human Evidence Index records are not sorted by key/path"
        )

    if not mirror_bytes.endswith(b"\n") or b"\r" in mirror_bytes:
        return _invalid_graph_snapshot(
            "Machine Evidence Mirror must use LF records with a final LF"
        )
    mirror_rows: list[_EvidenceGraphRow] = []
    mirror_pairs: set[tuple[str, str]] = set()
    for row_number, raw_line in enumerate(mirror_bytes.splitlines(keepends=True), start=1):
        if raw_line == b"\n":
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} is blank"
            )
        try:
            line = raw_line[:-1].decode("utf-8")
            payload = _loads_json_strict(line)
        except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} is malformed: {exc}"
            )
        if not isinstance(payload, dict):
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} is not an object"
            )
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        if line != canonical:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} is not canonical JSONL"
            )
        artifact_key = payload.get("artifact_key")
        if not isinstance(artifact_key, str) or not artifact_key:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} has an invalid artifact_key"
            )
        try:
            declared_path = _lexical_graph_path(
                config, payload.get("discovered_physical_path")
            )
        except ValueError as exc:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} has an invalid path: {exc}"
            )
        record_error = _mirror_record_error(payload, declared_path)
        if record_error:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror row {row_number} is invalid: {record_error}"
            )
        pair = (artifact_key, declared_path)
        if pair in mirror_pairs:
            return _invalid_graph_snapshot(
                f"Machine Evidence Mirror has duplicate key/path pair: {pair!r}"
            )
        mirror_pairs.add(pair)
        mirror_rows.append(
            _EvidenceGraphRow(artifact_key, declared_path, payload, raw_line)
        )
    if not mirror_rows:
        return _unavailable_graph_snapshot("Machine Evidence Mirror is empty")
    if [
        (row.artifact_key, row.declared_path) for row in mirror_rows
    ] != sorted((row.artifact_key, row.declared_path) for row in mirror_rows):
        return _invalid_graph_snapshot(
            "Machine Evidence Mirror records are not sorted by key/path"
        )

    if human_pairs != mirror_pairs:
        human_only = sorted(human_pairs - mirror_pairs)
        mirror_only = sorted(mirror_pairs - human_pairs)
        return _invalid_graph_snapshot(
            "Human Index and Machine Mirror key/path bindings disagree: "
            f"human_only={human_only!r}, mirror_only={mirror_only!r}"
        )

    mirror_rel = "artifacts/evidence_index.jsonl"
    self_candidates = [
        row
        for row in mirror_rows
        if row.artifact_key == "index.machine_mirror"
        or row.declared_path == mirror_rel
        or row.payload.get("role") == "self_record"
    ]
    if len(self_candidates) != 1:
        return _invalid_graph_snapshot(
            "Machine Mirror must contain exactly one canonical self-record"
        )
    self_row = self_candidates[0]
    if (
        self_row.artifact_key != "index.machine_mirror"
        or self_row.declared_path != mirror_rel
        or self_row.payload.get("role") != "self_record"
        or self_row.payload.get("proof_anchor")
        != "artifacts/evidence_index.jsonl.path_proof.txt"
    ):
        return _invalid_graph_snapshot("Machine Mirror self-record identity is invalid")

    self_proof_path = config.repo_root / "artifacts/evidence_index.jsonl.path_proof.txt"
    proof_status, proof_reason, self_proof, self_proof_bytes = _read_path_proof(
        config, self_proof_path
    )
    if (
        proof_status is not Status.PASS
        or self_proof is None
        or self_proof_bytes is None
    ):
        if proof_status is Status.TOOLING_BLOCKED:
            return _unavailable_graph_snapshot(
                f"Machine Mirror self-record proof is unavailable: {proof_reason}"
            )
        return _invalid_graph_snapshot(
            f"Machine Mirror self-record proof is invalid: {proof_reason}"
        )
    proof_error = _path_proof_error(
        self_proof, declared_path=mirror_rel, require_mirror_body=True
    )
    if proof_error:
        return _invalid_graph_snapshot(proof_error)

    body_bytes = b"".join(
        row.raw_line or b"" for row in mirror_rows if row is not self_row
    )
    body_sha = hashlib.sha256(body_bytes).hexdigest()
    full_sha = hashlib.sha256(mirror_bytes).hexdigest()
    if self_row.payload.get("sha256") != body_sha:
        return _invalid_graph_snapshot("Machine Mirror self-record body hash is invalid")
    if self_row.payload.get("size_bytes") != len(mirror_bytes):
        return _invalid_graph_snapshot("Machine Mirror self-record size is invalid")
    if (
        self_proof.get("sha256") != full_sha
        or int(self_proof["size_bytes"]) != len(mirror_bytes)
    ):
        return _invalid_graph_snapshot(
            "Machine Mirror self-record path proof hash/size is invalid"
        )
    if self_proof.get("mirror_body_sha256") != body_sha:
        return _invalid_graph_snapshot("Machine Mirror path proof body hash is invalid")
    if self_row.payload.get("produced_at_utc") != self_proof.get("produced_at_utc"):
        return _invalid_graph_snapshot(
            "Machine Mirror and sibling proof produced_at_utc disagree"
        )

    for human_row in human_rows:
        if human_row.declared_path != mirror_rel:
            continue
        human_sha = human_row.payload.get("sha256")
        human_size = human_row.payload.get("size_bytes")
        if human_sha is not None and human_sha != full_sha:
            return _invalid_graph_snapshot(
                "Human Index Machine Mirror sha256 does not match complete mirror bytes"
            )
        if human_size is not None and human_size != len(mirror_bytes):
            return _invalid_graph_snapshot(
                "Human Index Machine Mirror size_bytes does not match complete mirror bytes"
            )

    return _EvidenceGraphSnapshot(
        Status.PASS,
        "",
        _graph_rows_by_path(human_rows),
        _graph_rows_by_path(mirror_rows),
        tuple(mirror_rows),
        human_bytes,
        mirror_bytes,
        self_proof_bytes,
    )


def _valid_graph_timestamp(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        _validate_timestamp(value)
    except ValueError:
        return False
    return True


class _EvidenceGovernanceValidator:
    """Validate acceptance evidence against one immutable per-evaluation graph."""

    def __init__(self, config: HarnessConfig) -> None:
        self._config = config
        self._snapshot: _EvidenceGraphSnapshot | None = None
        self._artifact_snapshots: dict[str, _RepositoryFileSnapshot] = {}
        self._proof_snapshots: dict[Path, bytes] = {}
        self._input_snapshots: dict[Path, tuple[str, bytes]] = {}
        self._pf04_sources: tuple[Path, ...] | None = None

    def set_pf04_sources(self, sources: Sequence[Path]) -> None:
        self._pf04_sources = tuple(sources)

    def capture_input(
        self,
        path: Path,
        *,
        subject: str,
    ) -> tuple[Status, str, bytes | None]:
        status, reason, payload = _read_stable_repo_file_bytes(
            self._config.repo_root,
            path,
            subject=subject,
        )
        if status is not Status.PASS or payload is None:
            return status, reason, None
        observed = self._input_snapshots.get(path)
        if observed is not None and observed != (subject, payload):
            return (
                Status.FAIL_TOOLING,
                f"{subject} changed during acceptance evaluation",
                None,
            )
        self._input_snapshots.setdefault(path, (subject, payload))
        return Status.PASS, "", payload

    def validate(
        self,
        declared_path: str,
        target: Path,
        artifact_bytes: bytes | None = None,
        *,
        artifact_snapshot: _RepositoryFileSnapshot | None = None,
    ) -> tuple[Status, str]:
        if declared_path.endswith(".path_proof.txt"):
            return (
                Status.FAIL_TOOLING,
                "path-proof transcript cannot be primary acceptance evidence",
            )
        status, reason, current_snapshot = _read_stable_acceptance_file(
            self._config.repo_root,
            target,
            subject="acceptance evidence",
        )
        if status is not Status.PASS or current_snapshot is None:
            return status, reason
        if artifact_bytes is None:
            artifact_bytes = current_snapshot.payload
        elif artifact_bytes != current_snapshot.payload:
            return (
                Status.FAIL_TOOLING,
                "acceptance evidence changed bytes during evaluation",
            )
        if artifact_snapshot is not None and artifact_snapshot != current_snapshot:
            return (
                Status.FAIL_TOOLING,
                "acceptance evidence changed path identity or bytes during evaluation",
            )
        observed = self._artifact_snapshots.get(declared_path)
        if observed is not None and observed != current_snapshot:
            return (
                Status.FAIL_TOOLING,
                "acceptance evidence changed path identity or bytes during evaluation",
            )
        self._artifact_snapshots.setdefault(declared_path, current_snapshot)
        if self._snapshot is None:
            self._snapshot = _load_evidence_graph(self._config)
        if self._snapshot.status is not Status.PASS:
            return self._snapshot.status, self._snapshot.reason
        self_proof_path = (
            self._config.repo_root
            / "artifacts/evidence_index.jsonl.path_proof.txt"
        )
        observed_self_proof = self._proof_snapshots.get(self_proof_path)
        if (
            observed_self_proof is not None
            and observed_self_proof != self._snapshot.self_proof_bytes
        ):
            return Status.FAIL_TOOLING, "Machine Mirror self proof changed during evaluation"
        self._proof_snapshots.setdefault(
            self_proof_path, self._snapshot.self_proof_bytes
        )
        return self._validate_from_snapshot(
            declared_path, target, artifact_bytes, self._snapshot
        )

    def _validate_from_snapshot(
        self,
        declared_path: str,
        target: Path,
        artifact_bytes: bytes,
        snapshot: _EvidenceGraphSnapshot,
    ) -> tuple[Status, str]:
        human_rows = snapshot.human_by_path.get(declared_path, ())
        mirror_rows = snapshot.mirror_by_path.get(declared_path, ())
        if not human_rows and not mirror_rows:
            return (
                Status.TOOLING_BLOCKED,
                "acceptance evidence is absent from the Human Index and Machine Mirror",
            )
        if not human_rows:
            return Status.FAIL_TOOLING, "acceptance evidence is absent from the Human Index"
        if not mirror_rows:
            return Status.FAIL_TOOLING, "acceptance evidence is absent from the Machine Mirror"

        human_keys = {row.artifact_key for row in human_rows}
        mirror_keys = {row.artifact_key for row in mirror_rows}
        if human_keys != mirror_keys:
            return (
                Status.FAIL_TOOLING,
                (
                    "Human Index and Machine Mirror key/path bindings disagree for "
                    f"{declared_path}: human={sorted(human_keys)!r}, "
                    f"mirror={sorted(mirror_keys)!r}"
                ),
            )

        expected_proof = f"{declared_path}.path_proof.txt"
        proof_path = self._config.repo_root / PurePosixPath(expected_proof)
        if declared_path == "artifacts/evidence_index.jsonl":
            proof_bytes = snapshot.self_proof_bytes
            proof_status, proof_reason, proof = _parse_path_proof_bytes(proof_bytes)
        else:
            proof_status, proof_reason, proof, proof_bytes = _read_path_proof(
                self._config, proof_path
            )
        if (
            proof_status is not Status.PASS
            or proof is None
            or proof_bytes is None
        ):
            return proof_status, f"{declared_path}: {proof_reason}"
        observed_proof = self._proof_snapshots.get(proof_path)
        if observed_proof is not None and observed_proof != proof_bytes:
            return Status.FAIL_TOOLING, "sibling path proof changed during evaluation"
        self._proof_snapshots.setdefault(proof_path, proof_bytes)
        proof_error = _path_proof_error(
            proof,
            declared_path=declared_path,
            require_mirror_body=declared_path == "artifacts/evidence_index.jsonl",
        )
        if proof_error:
            return Status.FAIL_TOOLING, proof_error

        actual_sha = hashlib.sha256(artifact_bytes).hexdigest()
        actual_size = len(artifact_bytes)
        if proof["sha256"] != actual_sha or int(proof["size_bytes"]) != actual_size:
            return (
                Status.FAIL_TOOLING,
                "sibling path proof hash/size does not match acceptance evidence bytes",
            )

        for row in human_rows:
            payload = row.payload
            human_sha = payload.get("sha256")
            human_size = payload.get("size_bytes")
            if human_sha is not None and human_sha != actual_sha:
                return Status.FAIL_TOOLING, "Human Index sha256 does not match evidence bytes"
            if human_size is not None and (
                not isinstance(human_size, int)
                or isinstance(human_size, bool)
                or human_size != actual_size
            ):
                return Status.FAIL_TOOLING, "Human Index size_bytes does not match evidence bytes"

        if declared_path == "artifacts/evidence_index.jsonl":
            if artifact_bytes != snapshot.mirror_bytes or target != (
                self._config.repo_root / declared_path
            ):
                return Status.FAIL_TOOLING, "Machine Mirror bytes changed during evaluation"
        else:
            for row in mirror_rows:
                payload = row.payload
                if (
                    payload.get("role") == "self_record"
                    or row.artifact_key == "index.machine_mirror"
                ):
                    return Status.FAIL_TOOLING, "non-Mirror evidence uses self-record identity"
                if payload.get("sha256") != actual_sha:
                    return (
                        Status.FAIL_TOOLING,
                        "Machine Mirror sha256 does not match evidence bytes",
                    )
                size = payload.get("size_bytes")
                if (
                    not isinstance(size, int)
                    or isinstance(size, bool)
                    or size != actual_size
                ):
                    return (
                        Status.FAIL_TOOLING,
                        "Machine Mirror size_bytes does not match evidence bytes",
                    )

        for row in mirror_rows:
            if row.payload.get("produced_at_utc") != proof.get("produced_at_utc"):
                return (
                    Status.FAIL_TOOLING,
                    "Machine Mirror and sibling proof produced_at_utc disagree",
                )
        return Status.PASS, ""

    def verify_stability(self) -> tuple[Status, str]:
        """Re-read captured governance inputs before the evaluation can report PASS."""

        if self._pf04_sources is not None:
            current_pf04_sources = tuple(
                sorted(
                    (self._config.repo_root / "docs" / "pfcanon").glob(
                        "PF04-Canon-HDE-Governance-v*.md"
                    )
                )
            )
            if current_pf04_sources != self._pf04_sources:
                return (
                    Status.FAIL_TOOLING,
                    "PF04 Governance source set changed during acceptance evaluation",
                )
        for path, (subject, expected) in self._input_snapshots.items():
            status, reason, current = _read_stable_repo_file_bytes(
                self._config.repo_root,
                path,
                subject=subject,
            )
            if status is not Status.PASS or current is None or current != expected:
                return (
                    Status.FAIL_TOOLING,
                    reason or f"{subject} changed during acceptance evaluation",
                )
        if self._snapshot is None or self._snapshot.status is not Status.PASS:
            return Status.PASS, ""
        graph_inputs = (
            (
                self._config.repo_root / "docs/evidence/INDEX.json",
                self._snapshot.human_bytes,
                "Human Evidence Index",
            ),
            (
                self._config.repo_root / "artifacts/evidence_index.jsonl",
                self._snapshot.mirror_bytes,
                "Machine Evidence Mirror",
            ),
        )
        for path, expected, subject in graph_inputs:
            status, reason, current = _read_stable_repo_file_bytes(
                self._config.repo_root,
                path,
                subject=subject,
            )
            if status is not Status.PASS or current is None or current != expected:
                return (
                    Status.FAIL_TOOLING,
                    reason or f"{subject} changed during acceptance evaluation",
                )
        for declared_path, expected in self._artifact_snapshots.items():
            target = self._config.repo_root / PurePosixPath(declared_path)
            status, reason, current = _read_stable_acceptance_file(
                self._config.repo_root,
                target,
                subject=f"acceptance evidence {declared_path}",
            )
            if status is not Status.PASS or current is None or current != expected:
                return (
                    Status.FAIL_TOOLING,
                    reason or f"acceptance evidence changed during evaluation: {declared_path}",
                )
        for proof_path, expected in self._proof_snapshots.items():
            proof_status, proof_reason, _, current = _read_path_proof(
                self._config, proof_path
            )
            if (
                proof_status is not Status.PASS
                or current is None
                or current != expected
            ):
                return (
                    Status.FAIL_TOOLING,
                    proof_reason or "sibling path proof changed during evaluation",
                )
        return Status.PASS, ""


@dataclass(frozen=True)
class ViabilityResult:
    status: Status
    status_reason: str
    primary_log: Path | None
    manifest: Path | None
    governed_ledger: Path | None
    token_status: Mapping[str, str]


def validate_check_id(check_id: str) -> str:
    if (
        not isinstance(check_id, str)
        or not CHECK_RE.fullmatch(check_id)
        or check_id in {".", ".."}
    ):
        raise ValueError("check_id must be a lowercase ASCII safe path segment")
    return check_id


def _validate_legacy_check_id(check_id: str) -> str:
    """Validate a historical identity without admitting it for new publication."""
    if (
        not isinstance(check_id, str)
        or not LEGACY_CHECK_RE.fullmatch(check_id)
        or check_id in {".", ".."}
    ):
        raise ValueError("legacy check_id must be a safe single path segment")
    return check_id


def validate_env_pins(
    environ: MutableMapping[str, str] | None = None,
) -> dict[str, str]:
    return ensure_determinism_env(environ=environ)


def collect_env_for_logging(environ: Mapping[str, str] | None = None) -> dict[str, str]:
    source = os.environ if environ is None else environ
    keys = (*DETERMINISM_ENV_PINS.keys(), "APP_ENV")
    return {key: source[key] for key in keys if key in source}


def _validate_command(command: object) -> None:
    if command == ():
        return
    if not isinstance(command, tuple) or not command:
        raise ValueError(
            "command must be an argv tuple or an ordered tuple of argv tuples"
        )
    if all(isinstance(part, str) for part in command):
        if any(not part for part in command):
            raise ValueError("command argv cannot contain empty strings")
        return
    if all(isinstance(argv, tuple) for argv in command):
        if any(
            not argv or any(not isinstance(part, str) or not part for part in argv)
            for argv in command
        ):
            raise ValueError("every command argv must contain only non-empty strings")
        return
    raise ValueError("command cannot mix argv strings and nested argv tuples")


def _serialized_command(
    command: tuple[str, ...] | tuple[tuple[str, ...], ...],
) -> list[str] | list[list[str]]:
    _validate_command(command)
    if command and isinstance(command[0], tuple):
        return [list(argv) for argv in command]
    return list(command)


def _validate_captured_env(captured_env: object) -> None:
    if not isinstance(captured_env, tuple):
        raise TypeError("captured_env must be an immutable tuple of key/value pairs")
    seen: set[str] = set()
    for item in captured_env:
        if (
            not isinstance(item, tuple)
            or len(item) != 2
            or not all(isinstance(value, str) for value in item)
        ):
            raise ValueError("captured_env entries must be string key/value pairs")
        key, _ = item
        if key not in ADMITTED_ENV_KEYS or key in seen:
            raise ValueError("captured_env contains a duplicate or non-admitted key")
        seen.add(key)


def _captured_env(result: CheckResult) -> dict[str, str]:
    if result.captured_env:
        return dict(result.captured_env)
    return collect_env_for_logging()


def _validate_timestamp(value: str) -> str:
    if not isinstance(value, str) or not UTC_TIMESTAMP_RE.fullmatch(value):
        raise ValueError("captured_at_utc must use second-precision UTC Z form")
    try:
        parsed = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
    except ValueError as exc:
        raise ValueError("captured_at_utc is not a valid UTC timestamp") from exc
    if parsed.tzinfo != timezone.utc:
        raise ValueError("captured_at_utc must be UTC")
    return value


def _utc_now() -> str:
    return (
        datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    )


def summarize_checks(checks: Iterable[CheckResult]) -> Status:
    statuses = [check.status for check in checks]
    if not statuses:
        return Status.TOOLING_BLOCKED
    for status in (
        Status.FAIL_TOOLING,
        Status.TOOLING_BLOCKED,
        Status.FAIL_BEHAVIOR,
        Status.PARKED,
    ):
        if status in statuses:
            return status
    return Status.PASS


def _atomic_write(path: Path, content: str) -> None:
    if not content:
        raise ValueError("refusing to write empty QA evidence")
    _atomic_write_bytes(path, content.encode("utf-8"))


def _atomic_write_bytes(
    path: Path, content: bytes, *, allow_empty: bool = False
) -> None:
    if not content and not allow_empty:
        raise ValueError("refusing to write empty QA evidence")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        Path(temporary).replace(path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def _repo_relative(config: HarnessConfig, path: Path) -> str:
    return path.resolve().relative_to(config.repo_root).as_posix()


def _primary_log_content(
    config: HarnessConfig,
    result: CheckResult,
    *,
    captured_at_utc: str | None = None,
) -> tuple[Path, str]:
    validate_check_id(result.check_id)
    path = config.qa_root / "checks" / result.check_id / "primary.log"
    rel = _repo_relative(config, path)
    evidence = list(result.evidence_artifacts)
    if rel not in evidence:
        evidence.insert(0, rel)
    name = result.check_name or result.check_id
    reason = result.status_reason
    command_executed = bool(result.command)
    if command_executed != (result.exit_code is not None):
        raise ValueError("command execution and exit_code presence disagree")
    if result.status is Status.PASS and (
        result.exit_code != 0 or reason or not evidence
    ):
        raise ValueError(
            "PASS requires successful executed commands when present, no reason, and evidence"
        )
    if result.status is not Status.PASS and not reason:
        raise ValueError("non-PASS status requires a causal reason")
    if bool(result.command) == (result.command_provenance == "Not executed"):
        raise ValueError("command provenance is inconsistent")
    header = {
        "captured_env": _captured_env(result),
        "check_id": result.check_id,
        "check_name": name,
        "claimed_tokens": [],
        "command": _serialized_command(result.command),
        "command_provenance": result.command_provenance,
        "evidence_artifacts": evidence,
        "exit_code": result.exit_code,
        "intended_tokens": list(result.intended_tokens),
        "pf_refs": list(result.pf_refs),
        "schema_version": "pf27.step_log_header.v2",
        "status": result.status.value,
        "status_reason": reason,
        "timestamp_utc": _validate_timestamp(captured_at_utc or _utc_now()),
    }
    body = result.output.rstrip("\n")
    if (
        result.status is Status.PASS
        and result.intended_tokens
        and NONCLAIM_EXPLANATION not in body.splitlines()
    ):
        body = f"{body}\n{NONCLAIM_EXPLANATION}" if body else NONCLAIM_EXPLANATION
    content = json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n"
    if body:
        content += body + "\n"
    return path, content


def write_primary_log(config: HarnessConfig, result: CheckResult) -> Path:
    """Write one primary log; prefer ``record_check`` for coherent publication."""
    path, content = _primary_log_content(config, result)
    _publish_with_rollback(
        ((path, content),),
        lambda: _verify_written_primary(path, result.check_id, result.status),
        repo_root=config.repo_root,
    )
    return path


def _read_primary_header(
    path: Path, *, allow_legacy_check_id: bool
) -> dict[str, object]:
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("primary log is missing or empty")
    first = path.read_text(encoding="utf-8").splitlines()[0]
    data = _loads_json_strict(first)
    required = {
        "schema_version",
        "timestamp_utc",
        "check_id",
        "check_name",
        "status",
        "status_reason",
        "command",
        "command_provenance",
        "exit_code",
        "evidence_artifacts",
        "captured_env",
        "pf_refs",
        "intended_tokens",
        "claimed_tokens",
    }
    if (
        not isinstance(data, dict)
        or set(data) != required
        or data["schema_version"] != "pf27.step_log_header.v2"
    ):
        raise ValueError("malformed PF27 v2 header")
    check_id_validator = (
        _validate_legacy_check_id if allow_legacy_check_id else validate_check_id
    )
    check_id = check_id_validator(data["check_id"])
    if not isinstance(data["check_name"], str) or not data["check_name"]:
        raise ValueError("malformed PF27 v2 check_name")
    status = Status(data["status"])
    if not isinstance(data["status_reason"], str):
        raise ValueError("malformed PF27 v2 status_reason")  # noqa: TRY004
    command = data["command"]
    if not isinstance(command, list):
        raise ValueError("malformed PF27 v2 command")  # noqa: TRY004
    normalized_command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    if command and all(isinstance(part, list) for part in command):
        normalized_command = tuple(tuple(part) for part in command)
    else:
        normalized_command = tuple(command)
    _validate_command(normalized_command)
    if (
        not isinstance(data["command_provenance"], str)
        or not data["command_provenance"]
    ):
        raise ValueError("malformed PF27 v2 command_provenance")
    if bool(command) == (data["command_provenance"] == "Not executed"):
        raise ValueError("PF27 v2 command provenance is inconsistent")
    if data["exit_code"] is not None and (
        not isinstance(data["exit_code"], int) or isinstance(data["exit_code"], bool)
    ):
        raise ValueError("malformed PF27 v2 exit_code")
    if bool(command) != (data["exit_code"] is not None):
        raise ValueError("PF27 v2 command execution and exit_code presence disagree")
    for field in ("evidence_artifacts", "pf_refs", "intended_tokens", "claimed_tokens"):
        if not isinstance(data[field], list) or any(
            not isinstance(item, str) or not item for item in data[field]
        ):
            raise ValueError(f"malformed PF27 v2 {field}")
    if any(not PF_TITLE_RE.fullmatch(reference) for reference in data["pf_refs"]):
        raise ValueError("PF27 v2 pf_refs are not exact in-document PF titles")
    if not data["evidence_artifacts"]:
        raise ValueError("PF27 v2 evidence_artifacts cannot be empty")
    if not isinstance(data["captured_env"], dict) or any(
        key not in ADMITTED_ENV_KEYS or not isinstance(value, str)
        for key, value in data["captured_env"].items()
    ):
        raise ValueError("malformed PF27 v2 captured_env")
    _validate_timestamp(data["timestamp_utc"])
    if status is Status.PASS and (
        data["exit_code"] != 0 or data["status_reason"]
    ):
        raise ValueError("PF27 v2 PASS causality is malformed")
    if status is not Status.PASS and not data["status_reason"]:
        raise ValueError("PF27 v2 non-PASS status lacks a causal reason")
    if data["claimed_tokens"] != []:
        raise ValueError("PR-03 logs cannot claim tokens")
    if status is Status.PASS and data["intended_tokens"]:
        body_lines = path.read_text(encoding="utf-8").splitlines()[1:]
        if NONCLAIM_EXPLANATION not in body_lines:
            raise ValueError(
                "PF27 v2 PASS with intended tokens lacks an explicit nonclaim"
            )
    if data["check_id"] != check_id:
        raise ValueError("malformed PF27 v2 check_id")
    return data


def read_primary_header(path: Path) -> dict[str, object]:
    """Read a canonical current PF27 v2 header."""
    return _read_primary_header(path, allow_legacy_check_id=False)


def _verify_written_primary(path: Path, check_id: str, status: Status) -> None:
    parsed = read_primary_header(path)
    if parsed["check_id"] != check_id or parsed["status"] != status.value:
        raise RuntimeError("primary log verification failed")


def _read_supported_primary_header(
    path: Path, *, expected_check_id: str
) -> dict[str, object]:
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("primary log is missing or empty")
    first = path.read_text(encoding="utf-8").splitlines()[0]
    if first.startswith("["):
        raise ValueError(
            f"unsupported primary-log schema without governed status: {expected_check_id}"
        )
    try:
        data = _loads_json_strict(first)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(
            f"unsupported primary-log schema: {expected_check_id}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError(  # noqa: TRY004
            f"unsupported primary-log schema: {expected_check_id}"
        )
    schema = data.get("schema_version")
    if schema == "pf27.step_log_header.v2":
        data = _read_primary_header(path, allow_legacy_check_id=True)
    elif schema == "pf27.step_log_header.v1":
        if data.get("check_id") != expected_check_id:
            raise ValueError(
                "manifest key, entry, and primary header check identity disagree"
            )
        try:
            Status(data.get("status"))
        except (TypeError, ValueError) as exc:
            raise ValueError("PF27 v1 primary header has an invalid status") from exc
    else:
        raise ValueError(f"unsupported primary-log JSON schema: {schema!r}")
    if data.get("check_id") != expected_check_id:
        raise ValueError(
            "manifest key, entry, and primary header check identity disagree"
        )
    return data


def _require_v2_primary_self_binding(
    config: HarnessConfig,
    check_id: str,
    header: Mapping[str, object],
) -> None:
    if header.get("schema_version") != "pf27.step_log_header.v2":
        return
    expected = (
        config.qa_root / "checks" / check_id / "primary.log"
    ).relative_to(config.repo_root).as_posix()
    evidence_artifacts = header.get("evidence_artifacts")
    if not isinstance(evidence_artifacts, list) or expected not in evidence_artifacts:
        raise ValueError(
            "PF27 v2 evidence_artifacts omit the canonical own primary log"
        )


def _manifest_entry_log_path(
    config: HarnessConfig,
    check_id: str,
    entry: object,
    *,
    require_nonempty: bool = True,
) -> Path:
    _validate_legacy_check_id(check_id)
    if not isinstance(entry, dict) or entry.get("check_id") != check_id:
        raise ValueError("manifest key and entry check identity disagree")
    raw_path = entry.get("log_path")
    if not isinstance(raw_path, str) or not raw_path or "\\" in raw_path:
        raise ValueError("manifest log path is malformed")
    pure = PurePosixPath(raw_path)
    if pure.is_absolute() or ".." in pure.parts or "." in pure.parts:
        raise ValueError("manifest log path traverses or is absolute")
    expected = config.qa_root / "checks" / check_id / "primary.log"
    allowed = {
        PurePosixPath("checks") / check_id / "primary.log",
        PurePosixPath(_repo_relative(config, expected)),
    }
    if pure not in allowed:
        raise ValueError(
            "manifest log path is foreign, noncanonical, or check-mismatched"
        )
    if require_nonempty and (not expected.is_file() or expected.stat().st_size == 0):
        raise ValueError("manifest primary log is missing or empty")
    return expected


def _manifest_payload(
    config: HarnessConfig, *, captured_bytes: bytes | None = None
) -> object:
    path = config.qa_root / "qa_step_logs_manifest.json"
    try:
        text = (
            captured_bytes.decode("utf-8")
            if captured_bytes is not None
            else path.read_text(encoding="utf-8")
        )
        return _loads_json_strict(text)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"QA manifest is unreadable or malformed: {exc}") from exc


def _manifest_shape(
    config: HarnessConfig, payload: object
) -> tuple[str, Mapping[str, object]]:
    if not isinstance(payload, dict):
        raise ValueError("unknown QA manifest shape")  # noqa: TRY004
    if set(payload) == {"epic_id", "checks"}:
        if payload.get("epic_id") != config.epic_id or not isinstance(
            payload.get("checks"), dict
        ):
            raise ValueError("manifest epic identity or checks mapping is malformed")
        return "wrapped-checks", payload["checks"]
    if set(payload) == {"epic_id", "runs"}:
        if payload.get("epic_id") != config.epic_id or not isinstance(
            payload.get("runs"), list
        ):
            raise ValueError("historical manifest envelope is malformed")
        return "historical-runs", {}
    if not payload or (
        not ({"epic_id", "checks", "runs"} & set(payload))
        and all(
            isinstance(key, str)
            and LEGACY_CHECK_RE.fullmatch(key)
            and isinstance(value, dict)
            for key, value in payload.items()
        )
    ):
        return "flat-checks", payload
    raise ValueError("unknown QA manifest shape: mixed or unsupported structure")


def _normalize_manifest_checks(
    config: HarnessConfig,
    checks: Mapping[str, object],
) -> dict[str, dict[str, str]]:
    normalized: dict[str, dict[str, str]] = {}
    for check_id in sorted(checks):
        entry = checks[check_id]
        log = _manifest_entry_log_path(config, check_id, entry)
        header = _read_supported_primary_header(log, expected_check_id=check_id)
        _require_v2_primary_self_binding(config, check_id, header)
        assert isinstance(entry, dict)
        allowed_fields = {
            "check_id",
            "check_name",
            "fail_status",
            "log_path",
            "status",
            "timestamp_utc",
        }
        if not {"check_id", "log_path", "status"} <= set(entry) or not set(
            entry
        ) <= allowed_fields:
            raise ValueError("manifest entry has missing or unsupported fields")
        if any(
            not isinstance(entry[field], str)
            for field in set(entry) - {"check_id", "log_path"}
        ):
            raise ValueError("manifest entry metadata must be strings")
        if (
            header.get("schema_version") == "pf27.step_log_header.v2"
            and entry.get("status") != header.get("status")
        ):
            raise ValueError("canonical manifest status disagrees with primary header")
        normalized[check_id] = {
            "check_id": check_id,
            "log_path": _repo_relative(config, log),
            "status": Status(header["status"]).value,
        }
    return normalized


def _preflight_manifest(
    config: HarnessConfig, *, captured_bytes: bytes | None = None
) -> dict[str, dict[str, str]]:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if captured_bytes is None and not path.exists():
        return {}
    shape, checks = _manifest_shape(
        config, _manifest_payload(config, captured_bytes=captured_bytes)
    )
    if shape == "historical-runs":
        # Historical run records are recognized but never imported into
        # current-state correctness.
        return {}
    return _normalize_manifest_checks(config, checks)


def _preflight_legacy_family_replacement(
    config: HarnessConfig,
    expected_ids: set[str],
) -> None:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError(
            "complete-family replacement requires an existing legacy manifest"
        )
    shape, checks = _manifest_shape(config, _manifest_payload(config))
    if shape != "wrapped-checks" or set(checks) != expected_ids:
        raise ValueError(
            "legacy replacement manifest is partial, extra, or not the expected wrapper"
        )
    for check_id in sorted(expected_ids):
        # This bounded transition validates identity, path safety, and bytes,
        # but deliberately does not infer or trust a bracket log status.
        _manifest_entry_log_path(config, check_id, checks[check_id])


def _manifest_content(checks: Mapping[str, Mapping[str, str]]) -> str:
    for check_id in checks:
        validate_check_id(check_id)
    payload = {key: dict(checks[key]) for key in sorted(checks)}
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def update_manifest(config: HarnessConfig, log_path: Path) -> Path:
    header = _read_supported_primary_header(
        log_path,
        expected_check_id=validate_check_id(log_path.parent.name),
    )
    check_id = validate_check_id(str(header["check_id"]))
    expected = config.qa_root / "checks" / check_id / "primary.log"
    if log_path.resolve() != expected.resolve():
        raise ValueError("non-canonical primary log path")
    _require_v2_primary_self_binding(config, check_id, header)
    path = config.qa_root / "qa_step_logs_manifest.json"
    checks = _preflight_manifest(config)
    checks[check_id] = {
        "check_id": check_id,
        "log_path": _repo_relative(config, expected),
        "status": str(header["status"]),
    }
    expected_content = _manifest_content(checks)
    _publish_with_rollback(
        ((path, expected_content),),
        lambda: _verify_flat_manifest(config, checks),
        repo_root=config.repo_root,
    )
    return path


def verify_manifest_entry(config: HarnessConfig, check_id: str) -> dict[str, str]:
    validate_check_id(check_id)
    path = config.qa_root / "qa_step_logs_manifest.json"
    payload = _loads_json_strict(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or check_id not in payload:
        raise ValueError("canonical flat manifest entry is missing")
    entry = payload[check_id]
    log = config.repo_root / entry["log_path"]
    header = _read_supported_primary_header(log, expected_check_id=check_id)
    _require_v2_primary_self_binding(config, check_id, header)
    if entry != {
        "check_id": check_id,
        "log_path": _repo_relative(config, log),
        "status": header["status"],
    }:
        raise ValueError("manifest and primary log disagree")
    return entry


def _verify_flat_manifest(
    config: HarnessConfig,
    expected: Mapping[str, Mapping[str, str]],
) -> None:
    for check_id in expected:
        validate_check_id(check_id)
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("canonical flat manifest is missing or empty")
    payload = _loads_json_strict(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload != {
        key: dict(expected[key]) for key in sorted(expected)
    }:
        raise ValueError(
            "canonical flat manifest bytes or entries disagree with the staged family"
        )
    for check_id in sorted(expected):
        verify_manifest_entry(config, check_id)


def _parse_pytest_arguments(
    pytest_args: Sequence[str],
    *,
    subject: str,
) -> tuple[tuple[str, ...], tuple[str, ...], str]:
    """Partition the closed pytest grammar into selectors and exact options."""
    selectors: list[str] = []
    options: list[str] = []
    arguments = tuple(pytest_args)
    argument_index = 0
    while argument_index < len(arguments):
        argument = arguments[argument_index]
        if argument in {"-q", "--quiet", "--collect-only"}:
            options.append(argument)
            argument_index += 1
            continue
        if argument == "-p":
            if (
                argument_index + 1 >= len(arguments)
                or arguments[argument_index + 1] != "no:cacheprovider"
            ):
                return (), (), f"{subject} admits only -p no:cacheprovider"
            options.extend((argument, arguments[argument_index + 1]))
            argument_index += 2
            continue
        if argument in {"-k", "-m"}:
            if argument_index + 1 >= len(arguments):
                return (), (), f"{subject} option {argument} lacks its expression"
            options.extend((argument, arguments[argument_index + 1]))
            argument_index += 2
            continue
        if (argument.startswith("-k") or argument.startswith("-m")) and len(
            argument
        ) > 2:
            options.append(argument)
            argument_index += 1
            continue
        if argument.startswith("-"):
            return (), (), f"{subject} uses unsupported option: {argument}"
        selectors.append(argument)
        argument_index += 1
    return tuple(selectors), tuple(options), ""


def _normalize_pytest_collection_options(
    pytest_options: Sequence[str],
) -> tuple[str, ...]:
    """Remove collection controls already supplied by the canonical command."""
    normalized: list[str] = []
    option_index = 0
    options = tuple(pytest_options)
    while option_index < len(options):
        option = options[option_index]
        if option in {"-q", "--quiet", "--collect-only"}:
            option_index += 1
            continue
        if (
            option == "-p"
            and option_index + 1 < len(options)
            and options[option_index + 1] == "no:cacheprovider"
        ):
            option_index += 2
            continue
        normalized.append(option)
        option_index += 1
    return tuple(normalized)


def run_pytest_check(
    config: HarnessConfig,
    check_id: str,
    pytest_args: Sequence[str],
    *,
    check_name: str = "",
    intended_tokens: Sequence[str] = (),
) -> CheckResult:
    validate_check_id(check_id)
    command = (sys.executable, "-m", "pytest", *pytest_args)
    readiness_command = (sys.executable, "-m", "pytest", "--version")
    entrypoints, _, option_error = _parse_pytest_arguments(
        pytest_args,
        subject="pytest invocation",
    )
    if option_error:
        return CheckResult(
            check_id,
            Status.TOOLING_BLOCKED,
            option_error,
            check_name,
            (),
            "Not executed",
            None,
            intended_tokens=(),
        )
    missing = [
        arg
        for arg in entrypoints
        if not (config.repo_root / arg.split("::", 1)[0]).exists()
    ]
    if missing:
        return CheckResult(
            check_id,
            Status.TOOLING_BLOCKED,
            f"required pytest entrypoint unavailable: {missing[0]}",
            check_name,
            (),
            "Not executed",
            None,
            intended_tokens=(),
        )
    try:
        readiness = subprocess.run(
            readiness_command,
            cwd=config.repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return CheckResult(
            check_id,
            Status.FAIL_TOOLING,
            f"pytest readiness process malfunction: {exc}",
            check_name,
            (),
            "Not executed",
            None,
            intended_tokens=tuple(intended_tokens),
        )
    if readiness.returncode:
        return CheckResult(
            check_id,
            Status.TOOLING_BLOCKED,
            "pytest readiness check failed",
            check_name,
            readiness_command,
            "epic wrapper readiness command",
            readiness.returncode,
            readiness.stdout + readiness.stderr,
            intended_tokens=(),
        )
    try:
        completed = subprocess.run(
            command, cwd=config.repo_root, capture_output=True, text=True, check=False
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return CheckResult(
            check_id,
            Status.FAIL_TOOLING,
            f"pytest process malfunction: {exc}",
            check_name,
            readiness_command,
            "epic wrapper readiness completed; test command launch failed",
            readiness.returncode,
            intended_tokens=tuple(intended_tokens),
        )
    status = classify_pytest_returncode(completed.returncode)
    reason = (
        ""
        if status is Status.PASS
        else (
            "pytest collected no required tests"
            if status is Status.TOOLING_BLOCKED
            else (
                "pytest collection/tooling failed"
                if status is Status.FAIL_TOOLING
                else "pytest assertions contradicted required behavior"
            )
        )
    )
    return CheckResult(
        check_id,
        status,
        reason,
        check_name,
        (readiness_command, command),
        "epic wrapper readiness and test commands; exact ordered argv",
        completed.returncode,
        completed.stdout + completed.stderr,
        intended_tokens=(
            () if status is Status.TOOLING_BLOCKED else tuple(intended_tokens)
        ),
        pf_refs=(
            "PF14-Canon-HDE-Mechanics-Guide",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )


def classify_pytest_returncode(returncode: int) -> Status:
    """Map an actual pytest process result to the PF19 causal status."""
    if not isinstance(returncode, int) or isinstance(returncode, bool):
        raise ValueError("pytest returncode must be an integer")
    if returncode == 0:
        return Status.PASS
    if returncode == 5:
        return Status.TOOLING_BLOCKED
    if returncode in {2, 3, 4} or returncode < 0:
        return Status.FAIL_TOOLING
    return Status.FAIL_BEHAVIOR


def _publish_with_rollback(
    files: Sequence[tuple[Path, str]],
    verifier: Callable[[], None],
    *,
    repo_root: Path,
) -> None:
    """Publish and verify a related file family inside one rollback boundary."""
    if not files:
        raise ValueError("publication family cannot be empty")
    resolved_paths = [path.resolve() for path, _ in files]
    if len(resolved_paths) != len(set(resolved_paths)):
        raise ValueError("publication family contains duplicate output paths")
    for path, content in files:
        if path.is_symlink():
            raise ValueError("publication output cannot be a symlink")
        ancestor = path.parent
        while ancestor != repo_root:
            if ancestor.is_symlink():
                raise ValueError("publication output parent cannot be a symlink")
            if ancestor == ancestor.parent:
                break
            ancestor = ancestor.parent
        try:
            path.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise ValueError("publication output escapes repository") from exc
        if not content:
            raise ValueError("publication output cannot be empty")
    originals = {
        path: path.read_bytes() if path.exists() else None for path, _ in files
    }
    absent_parents: set[Path] = set()
    for path, _ in files:
        parent = path.parent
        while parent != repo_root and not parent.exists():
            absent_parents.add(parent)
            parent = parent.parent
    try:
        for path, content in files:
            _atomic_write(path, content)
        for path, content in files:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"published output is missing or empty: {path}")
            if path.read_bytes() != content.encode("utf-8"):
                raise RuntimeError(f"published output bytes disagree: {path}")
        verifier()
    except BaseException as publish_error:
        rollback_errors: list[BaseException] = []
        for path, _ in reversed(tuple(files)):
            try:
                original = originals[path]
                if original is None:
                    path.unlink(missing_ok=True)
                else:
                    _atomic_write_bytes(path, original, allow_empty=True)
            except BaseException as exc:  # noqa: BLE001  # pragma: no cover
                rollback_errors.append(exc)
        for parent in sorted(
            absent_parents, key=lambda item: len(item.parts), reverse=True
        ):
            try:
                parent.rmdir()
            except OSError:
                pass
        if rollback_errors:  # pragma: no cover - catastrophic filesystem failure
            raise RuntimeError(
                "publication failed and rollback was incomplete"
            ) from publish_error
        raise


def _publish_atomically(files: Sequence[tuple[Path, str]]) -> None:
    """Backward-compatible transactional writer without extra coherence checks."""
    if not files:
        raise ValueError("publication family cannot be empty")
    common = Path(os.path.commonpath([str(path.resolve()) for path, _ in files]))
    repo_root = common if common.is_dir() else common.parent
    _publish_with_rollback(files, lambda: None, repo_root=repo_root)


def record_check(
    config: HarnessConfig,
    result: CheckResult,
    *,
    additional_files: Sequence[tuple[Path, str]] = (),
) -> tuple[Path, Path]:
    """Preflight and coherently publish one primary log and the flat manifest."""
    logs, manifest = record_check_family(
        config,
        (result,),
        additional_files=additional_files,
    )
    return logs[0], manifest


def record_check_family(
    config: HarnessConfig,
    results: Sequence[CheckResult],
    *,
    additional_files: Sequence[tuple[Path, str]] = (),
    coherence_verifier: Callable[[], None] | None = None,
    replace_legacy_family_ids: Sequence[str] = (),
    admit_new_check_ids: Sequence[str] = (),
    captured_at_utc: str | None = None,
) -> tuple[tuple[Path, ...], Path]:
    """Publish a complete current-state family with all verification in-boundary."""
    staged_results = tuple(results)
    if not staged_results:
        raise ValueError("check family cannot be empty")
    # CheckResult validates at construction, and the publication boundary
    # revalidates so mutated/deserialized instances cannot create noncanonical
    # current paths before any family member is written.
    result_ids = [validate_check_id(result.check_id) for result in staged_results]
    checks_root = config.qa_root / "checks"
    for path, _ in additional_files:
        absolute_path = Path(os.path.abspath(path))
        try:
            relative = absolute_path.relative_to(checks_root)
        except ValueError:
            continue
        if relative.parts:
            validate_check_id(relative.parts[0])
    if len(result_ids) != len(set(result_ids)):
        raise ValueError("check family contains duplicate check IDs")
    replacement_ids = {
        _validate_legacy_check_id(check_id)
        for check_id in replace_legacy_family_ids
    }
    admitted_ids = {validate_check_id(check_id) for check_id in admit_new_check_ids}
    if replacement_ids & admitted_ids:
        raise ValueError("replacement and admitted check IDs must be disjoint")
    if replacement_ids:
        if set(result_ids) != replacement_ids | admitted_ids:
            raise ValueError(
                "fresh family is partial, extra, or missing an explicitly admitted check"
            )
        _preflight_legacy_family_replacement(config, replacement_ids)
        checks: dict[str, dict[str, str]] = {}
    else:
        if admitted_ids:
            raise ValueError(
                "admitted check IDs require a bounded legacy-family replacement"
            )
        checks = _preflight_manifest(config)
    family_timestamp = _validate_timestamp(captured_at_utc or _utc_now())
    rendered: list[tuple[Path, str]] = []
    logs: list[Path] = []
    for result in staged_results:
        log, content = _primary_log_content(
            config,
            result,
            captured_at_utc=family_timestamp,
        )
        logs.append(log)
        rendered.append((log, content))
        checks[result.check_id] = {
            "check_id": result.check_id,
            "log_path": _repo_relative(config, log),
            "status": result.status.value,
        }
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    staged_files = (
        *rendered,
        (manifest, _manifest_content(checks)),
        *tuple(additional_files),
    )

    def verify_family() -> None:
        for log, result in zip(logs, staged_results, strict=True):
            _verify_written_primary(log, result.check_id, result.status)
        _verify_flat_manifest(config, checks)
        if coherence_verifier is not None:
            coherence_verifier()

    _publish_with_rollback(
        staged_files,
        verify_family,
        repo_root=config.repo_root,
    )
    return tuple(logs), manifest


def _governance_tokens(
    config: HarnessConfig,
    *,
    captured_bytes: bytes | None = None,
) -> tuple[set[str] | None, str]:
    if captured_bytes is None:
        matches = sorted(
            (config.repo_root / "docs" / "pfcanon").glob(
                "PF04-Canon-HDE-Governance-v*.md"
            )
        )
        if len(matches) != 1:
            return None, "exactly one current PF04 Governance source is required"
        status, reason, captured_bytes = _read_stable_repo_file_bytes(
            config.repo_root,
            matches[0],
            subject="PF04 Governance source",
        )
        if status is not Status.PASS or captured_bytes is None:
            return None, reason
    try:
        text = captured_bytes.decode("utf-8")
    except UnicodeError as exc:
        return None, f"PF04 Governance source unreadable: {exc}"
    start = text.find("## **2.0 Acceptance Tokens")
    end = text.find("## **2.1 ", start)
    if start < 0 or end < 0:
        return None, "PF04 §2.0 token roster is incomplete"
    tokens: set[str] = set()
    for line in text[start:end].splitlines():
        declaration = TOKEN_DECLARATION_RE.match(line)
        if declaration:
            name = declaration.group("name").replace("\\_", "_")
            if TOKEN_RE.fullmatch(name):
                tokens.add(name)
    if not tokens:
        return None, "PF04 §2.0 token roster is empty"
    return tokens, ""


def _normalized_cell(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


COMPLETE_ACCEPTANCE_POSTURES = frozenset({"implemented", "covered", "satisfied"})
ACCEPTANCE_POSTURES = COMPLETE_ACCEPTANCE_POSTURES | frozenset(
    {"planned", "token_incomplete"}
)


def _normalized_acceptance_posture(value: object) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    stripped = value.strip()
    if not re.fullmatch(r"[A-Za-z]+(?:[ _-]+[A-Za-z]+)*", stripped):
        return None
    normalized = re.sub(r"[ _-]+", "_", stripped.lower())
    return normalized if normalized in ACCEPTANCE_POSTURES else None


def _is_matrix_header(cells: Sequence[str]) -> bool:
    if len(cells) != 7:
        return False
    normalized = [_normalized_cell(cell) for cell in cells]
    return (
        normalized[0] == "token_name"
        and "owner" in normalized[1]
        and normalized[2].startswith("evidence_artifacts")
        and "ci" in normalized[3]
        and ("test" in normalized[3] or "job" in normalized[3])
        and normalized[4].startswith("qa_root_logs")
        and normalized[5] == "status"
        and normalized[6] == "notes"
    )


def _split_reference_items(
    value: str, *, field: str, token_name: str
) -> tuple[str, ...]:
    items = tuple(item.strip() for item in value.split(";"))
    if not items or any(not item for item in items):
        raise ValueError(f"empty {field} reference in matrix token row: {token_name}")
    return items


def _matrix_rows(
    path: Path,
    *,
    captured_bytes: bytes | None = None,
) -> tuple[dict[str, MatrixRow], str]:
    rows: dict[str, MatrixRow] = {}
    try:
        payload = path.read_bytes() if captured_bytes is None else captured_bytes
        lines = payload.decode("utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return {}, str(exc)
    found_header = False
    for line in lines:
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if _is_matrix_header(cells):
            found_header = True
            continue
        if cells and set(cells[0]) <= {"-", ":"}:
            continue
        if not found_header:
            continue
        if len(cells) != 7:
            return {}, "token matrix row does not contain exactly seven columns"
        name = cells[0]
        if not TOKEN_RE.fullmatch(name) or name in rows:
            return {}, f"malformed or duplicate matrix token row: {name}"
        if any(not cells[index] for index in (1, 2, 3, 4, 6)):
            return {}, f"matrix token row has an empty required column: {name}"
        try:
            evidence = _split_reference_items(
                cells[2], field="evidence_artifacts", token_name=name
            )
            ci = _split_reference_items(
                cells[3], field="ci_tests_jobs", token_name=name
            )
            qa = _split_reference_items(cells[4], field="qa_root_logs", token_name=name)
        except ValueError as exc:
            return {}, str(exc)
        rows[name] = MatrixRow(name, cells[1], evidence, ci, qa, cells[5], cells[6])
    if not found_header:
        return {}, "matrix is missing the complete seven-column header"
    return rows, "" if rows else "matrix contains no token rows"


def _extract_reference_path(value: object) -> tuple[PurePosixPath | None, Status, str]:
    if not isinstance(value, str) or not value.strip():
        return None, Status.TOOLING_BLOCKED, "reference is missing or non-string"
    stripped = value.strip()
    if PLACEHOLDER_RE.search(stripped) or "*" in stripped:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "reference contains a wildcard or placeholder",
        )
    if stripped.startswith(("/", "~")) or "\\" in stripped:
        return (
            None,
            Status.FAIL_BEHAVIOR,
            "reference is absolute or uses a non-repository separator",
        )
    unwrapped = (
        stripped[1:-1].strip()
        if stripped.startswith("`") and stripped.endswith("`")
        else stripped
    )
    if EXACT_RELATIVE_PATH_RE.fullmatch(unwrapped):
        candidates = [unwrapped]
    else:
        candidates = [
            candidate.strip("`.,;:()[]") for candidate in PATH_RE.findall(stripped)
        ]
    candidates = list(dict.fromkeys(candidate for candidate in candidates if candidate))
    if not candidates:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "reference contains no supported repository-relative path",
        )
    if len(candidates) != 1:
        return (
            None,
            Status.FAIL_BEHAVIOR,
            "reference contains multiple ambiguous repository-relative paths",
        )
    candidate = candidates[0]
    pure = PurePosixPath(candidate)
    if (
        pure.is_absolute()
        or not pure.parts
        or ".." in pure.parts
        or pure.as_posix() != candidate
    ):
        return None, Status.FAIL_BEHAVIOR, "reference traverses or is absolute"
    return pure, Status.PASS, ""


def _repo_target(config: HarnessConfig, pure: PurePosixPath) -> Path:
    lexical = config.repo_root / pure
    loop_reason = _repo_symlink_resolution_error(config.repo_root, lexical)
    if loop_reason:
        if loop_reason == _SYMLINK_REPOSITORY_ESCAPE:
            raise ValueError("reference escapes repository")
        raise RuntimeError(loop_reason)
    target = lexical.resolve()
    try:
        target.relative_to(config.repo_root)
    except ValueError as exc:
        raise ValueError("reference escapes repository") from exc
    return target


def _planned_output_error(config: HarnessConfig, pure: PurePosixPath) -> str:
    lexical = config.repo_root / pure
    alias_reason = _aliased_repo_path_reason(config.repo_root, lexical)
    if alias_reason:
        return f"planned output is aliased or unsafe: {alias_reason}"
    if lexical.exists() and not lexical.is_file():
        return "planned output already exists as a non-regular file"
    return ""


def _validate_json_evidence_bytes(payload: bytes) -> None:
    try:
        parsed = _loads_json_strict(payload.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("required JSON evidence is malformed or partial") from exc
    if parsed in ({}, [], None):
        raise ValueError("required JSON evidence is malformed or partial")


def _reject_duplicate_json_keys(
    pairs: Sequence[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _loads_json_strict(text: str) -> object:
    return json.loads(text, object_pairs_hook=_reject_duplicate_json_keys)


def _file_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    source_field: str,
    item_index: int,
    value: object,
    planned_paths: set[str],
    referenced_manifests: set[str],
    require_governance: bool,
    governance_validator: _EvidenceGovernanceValidator | None,
    allow_planned_output: bool = False,
) -> ReferenceDiagnostic:
    pure, status, reason = _extract_reference_path(value)
    rendered = value if isinstance(value, str) else repr(value)
    if pure is None:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, status, reason
        )
    declared_path = pure.as_posix()
    matches_planned_path = declared_path in planned_paths
    if matches_planned_path:
        planned_error = _planned_output_error(config, pure)
        if planned_error:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_BEHAVIOR,
                planned_error,
                declared_path,
            )
    is_planned = allow_planned_output and matches_planned_path
    try:
        _repo_target(config, pure)
    except (OSError, RuntimeError) as exc:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.FAIL_TOOLING,
            f"reference cannot be resolved safely: {exc}",
        )
    except ValueError as exc:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, Status.FAIL_BEHAVIOR, str(exc)
        )
    target = config.repo_root / pure
    relative = declared_path
    manifest_path = config.qa_root / "qa_step_logs_manifest.json"
    manifest_declared_path = manifest_path.relative_to(config.repo_root).as_posix()
    if declared_path == manifest_declared_path:
        referenced_manifests.add(relative)
        artifact_bytes: bytes | None = None
        artifact_snapshot: _RepositoryFileSnapshot | None = None
        if target.exists():
            read_status, read_reason, artifact_snapshot = _read_stable_acceptance_file(
                config.repo_root,
                target,
                subject="referenced manifest",
            )
            if read_status is not Status.PASS or artifact_snapshot is None:
                return ReferenceDiagnostic(
                    token,
                    source_field,
                    item_index,
                    rendered,
                    read_status,
                    read_reason,
                    relative,
                )
            artifact_bytes = artifact_snapshot.payload
            try:
                _preflight_manifest(config, captured_bytes=artifact_bytes)
            except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
                return ReferenceDiagnostic(
                    token,
                    source_field,
                    item_index,
                    rendered,
                    Status.FAIL_TOOLING,
                    f"referenced manifest is untrustworthy: {exc}",
                    relative,
                )
        elif not is_planned:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "referenced manifest is missing",
                relative,
            )
        if is_planned or not require_governance:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.PASS,
                resolved_path=relative,
            )
        if governance_validator is None:  # pragma: no cover - defensive
            raise RuntimeError("governance validator is required")
        if artifact_bytes is None:  # pragma: no cover - guarded above
            raise RuntimeError("governed manifest bytes are required")
        governed_status, governed_reason = governance_validator.validate(
            declared_path,
            target,
            artifact_bytes,
            artifact_snapshot=artifact_snapshot,
        )
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            governed_status,
            governed_reason,
            relative,
        )
    if is_planned:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.PASS,
            resolved_path=relative,
        )
    read_status, read_reason, artifact_snapshot = _read_stable_acceptance_file(
        config.repo_root,
        target,
        subject="referenced file",
    )
    if read_status is not Status.PASS or artifact_snapshot is None:
        diagnostic_reason = (
            "referenced file is missing or empty"
            if read_status is Status.TOOLING_BLOCKED and not target.exists()
            else read_reason
        )
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            read_status,
            diagnostic_reason,
            relative,
        )
    artifact_bytes = artifact_snapshot.payload
    if not artifact_bytes:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.TOOLING_BLOCKED,
            "referenced file is missing or empty",
            relative,
        )
    if pure.suffix == ".json":
        try:
            _validate_json_evidence_bytes(artifact_bytes)
        except ValueError as exc:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_TOOLING,
                str(exc),
                relative,
            )
    if require_governance:
        if governance_validator is None:  # pragma: no cover - defensive
            raise RuntimeError("governance validator is required")
        governed_status, governed_reason = governance_validator.validate(
            declared_path,
            target,
            artifact_bytes,
            artifact_snapshot=artifact_snapshot,
        )
        if governed_status is not Status.PASS:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                governed_status,
                governed_reason,
                relative,
            )
    return ReferenceDiagnostic(
        token, source_field, item_index, rendered, Status.PASS, resolved_path=relative
    )


def _qa_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    item_index: int,
    value: object,
    planned_paths: set[str],
    referenced_manifests: set[str],
    require_governance: bool,
    governance_validator: _EvidenceGovernanceValidator | None,
) -> ReferenceDiagnostic:
    source_field = "matrix.qa_root_logs"
    pure, status, reason = _extract_reference_path(value)
    rendered = value if isinstance(value, str) else repr(value)
    if pure is None:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, status, reason
        )
    qa_prefix = PurePosixPath(config.qa_root.relative_to(config.repo_root).as_posix())
    if pure.parts[:2] == ("audit", "qa"):
        if pure.parts[: len(qa_prefix.parts)] != qa_prefix.parts:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_BEHAVIOR,
                "QA locator points to a foreign epic",
            )
        declared_path = pure
    else:
        declared_path = qa_prefix / pure
    try:
        target = _repo_target(config, declared_path)
    except (OSError, RuntimeError) as exc:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.FAIL_TOOLING,
            f"QA locator cannot be resolved safely: {exc}",
        )
    except ValueError as exc:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.FAIL_BEHAVIOR,
            str(exc),
        )
    try:
        target.relative_to(config.qa_root)
    except ValueError:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.FAIL_BEHAVIOR,
            "QA locator escapes the epic QA root",
        )
    return _file_diagnostic(
        config,
        token=token,
        source_field=source_field,
        item_index=item_index,
        value=declared_path.as_posix(),
        planned_paths=planned_paths,
        referenced_manifests=referenced_manifests,
        require_governance=require_governance,
        governance_validator=governance_validator,
        allow_planned_output=True,
    )


def _resolve_reference(config: HarnessConfig, value: object) -> tuple[Path | None, str]:
    diagnostic = _file_diagnostic(
        config,
        token="",
        source_field="evidence",
        item_index=1,
        value=value,
        planned_paths=set(),
        referenced_manifests=set(),
        require_governance=False,
        governance_validator=None,
    )
    if diagnostic.status is not Status.PASS or diagnostic.resolved_path is None:
        return None, diagnostic.reason
    return config.repo_root / diagnostic.resolved_path, ""


def _command_path(
    config: HarnessConfig,
    raw: str,
    *,
    require_executable: bool = False,
) -> tuple[Path | None, Status, str]:
    pure, status, reason = _extract_reference_path(raw)
    if pure is None:
        return None, status, reason
    try:
        target = _repo_target(config, pure)
    except (OSError, RuntimeError) as exc:
        return (
            None,
            Status.FAIL_TOOLING,
            f"command path cannot be resolved safely: {exc}",
        )
    except ValueError as exc:
        return None, Status.FAIL_BEHAVIOR, str(exc)
    if not target.is_file() or target.stat().st_size == 0:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "required script or test file is missing or empty",
        )
    if require_executable and not os.access(target, os.X_OK):
        return (
            None,
            Status.TOOLING_BLOCKED,
            "required bare script is not executable",
        )
    return target, Status.PASS, ""


def _ci_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    item_index: int,
    value: object,
) -> tuple[ReferenceDiagnostic, PytestCollectionRequest | None]:
    source_field = "matrix.ci_tests_jobs"
    rendered = value if isinstance(value, str) else repr(value)
    if not isinstance(value, str) or not value.strip():
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator is missing or non-string",
            ),
            None,
        )
    if PLACEHOLDER_RE.search(value) or "*" in value:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator contains a wildcard or placeholder",
            ),
            None,
        )
    try:
        argv = shlex.split(value)
    except ValueError as exc:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_TOOLING,
                f"CI/test locator parser failed: {exc}",
            ),
            None,
        )
    if not argv or any(part in {"&&", "||", "|", ">", ">>"} for part in argv):
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_BEHAVIOR,
                "CI/test locator contains an unsupported shell composition",
            ),
            None,
        )
    pytest_args: list[str] | None = None
    script_arg: str | None = None
    bare_script = False
    if argv[0] == "python" and len(argv) >= 3 and argv[1:3] == ["-m", "pytest"]:
        pytest_args = argv[3:]
    elif argv[0] == "pytest":
        pytest_args = argv[1:]
    elif argv[0] == "python" and len(argv) >= 2 and not argv[1].startswith("-"):
        script_arg = argv[1]
    elif "/" in argv[0] or argv[0].endswith((".py", ".sh")):
        script_arg = argv[0]
        bare_script = True
    else:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator is prose or uses an unsupported command form",
            ),
            None,
        )
    if script_arg is not None:
        script_position = argv.index(script_arg)
        if any(
            not argument.startswith("-") for argument in argv[script_position + 1 :]
        ):
            return (
                ReferenceDiagnostic(
                    token,
                    source_field,
                    item_index,
                    rendered,
                    Status.TOOLING_BLOCKED,
                    "script locator contains unsupported prose or positional arguments",
                ),
                None,
            )
        target, status, reason = _command_path(
            config, script_arg, require_executable=bare_script
        )
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                status,
                reason,
                _repo_relative(config, target) if target is not None else None,
            ),
            None,
        )
    selectors, options, option_error = _parse_pytest_arguments(
        tuple(pytest_args or ()),
        subject="pytest locator",
    )
    if not option_error and any(".py" not in selector for selector in selectors):
        option_error = "pytest locator contains unsupported positional prose"
    if option_error:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                option_error,
            ),
            None,
        )
    if not selectors:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "pytest locator does not name a repository test file or node",
            ),
            None,
        )
    for selector in selectors:
        base = selector.split("::", 1)[0]
        target, status, reason = _command_path(config, base)
        if target is None:
            return (
                ReferenceDiagnostic(
                    token, source_field, item_index, rendered, status, reason
                ),
                None,
            )
    first_target = config.repo_root / selectors[0].split("::", 1)[0]
    return (
        ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.PASS,
            resolved_path=_repo_relative(config, first_target),
        ),
        PytestCollectionRequest(
            selectors=selectors,
            options=_normalize_pytest_collection_options(options),
        ),
    )


def _collect_pytest_file(
    config: HarnessConfig,
    test_file: str,
    pytest_options: tuple[str, ...],
    temp_root: Path,
) -> tuple[
    Status,
    str,
    frozenset[str],
    tuple[str, ...] | None,
    int | None,
]:
    normalized_options = _normalize_pytest_collection_options(pytest_options)
    command = (
        sys.executable,
        "-m",
        "pytest",
        "--collect-only",
        "-q",
        "-p",
        "no:cacheprovider",
        f"--basetemp={temp_root}",
        *normalized_options,
        test_file,
    )
    source_env = os.environ
    runtime_bin = str(Path(sys.executable).parent)
    inherited_path = source_env.get("PATH", "")
    env = {
        **DETERMINISM_ENV_PINS,
        "PATH": runtime_bin
        + (os.pathsep + inherited_path if inherited_path else ""),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if "APP_ENV" in source_env:
        env["APP_ENV"] = source_env["APP_ENV"]
    try:
        completed = subprocess.run(
            command,
            cwd=config.repo_root,
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return (
            Status.FAIL_TOOLING,
            f"pytest collection process malfunction: {exc}",
            frozenset(),
            None,
            None,
        )
    output = f"{completed.stdout}\n{completed.stderr}"
    lowered = output.lower()
    if completed.returncode != 0:
        if (
            completed.returncode == 5
            or "not found:" in lowered
            or "no tests collected" in lowered
        ):
            return (
                Status.TOOLING_BLOCKED,
                f"pytest file is unavailable: {test_file}",
                frozenset(),
                command,
                completed.returncode,
            )
        if "no module named pytest" in lowered:
            return (
                Status.TOOLING_BLOCKED,
                "pytest collection prerequisite is unavailable",
                frozenset(),
                command,
                completed.returncode,
            )
        return (
            Status.FAIL_TOOLING,
            f"pytest collection/import failed for: {test_file}",
            frozenset(),
            command,
            completed.returncode,
        )
    node_lines = frozenset(
        line.strip() for line in completed.stdout.splitlines() if "::" in line
    )
    return Status.PASS, "", node_lines, command, completed.returncode


def _apply_pytest_collection(
    config: HarnessConfig,
    diagnostics: list[ReferenceDiagnostic],
    requests: Mapping[int, PytestCollectionRequest],
) -> tuple[tuple[tuple[str, ...], int], ...]:
    if not requests:
        return ()
    cache: dict[
        tuple[str, tuple[str, ...]],
        tuple[
            Status,
            str,
            frozenset[str],
            tuple[str, ...] | None,
            int | None,
        ],
    ] = {}
    receipts: list[tuple[tuple[str, ...], int]] = []
    try:
        temporary = tempfile.TemporaryDirectory(prefix="qa-harness-pytest-")
    except OSError as exc:
        for index in requests:
            diagnostics[index] = replace(
                diagnostics[index],
                status=Status.FAIL_TOOLING,
                reason=f"temporary pytest collection root failed: {exc}",
            )
        return ()
    request_items = tuple(requests.items())
    with temporary as root:
        for request_offset, (diagnostic_index, request) in enumerate(request_items):
            selector_results: list[tuple[Status, str]] = []
            for selector in request.selectors:
                test_file = selector.split("::", 1)[0]
                cache_key = (test_file, request.options)
                if cache_key not in cache:
                    cache[cache_key] = _collect_pytest_file(
                        config,
                        test_file,
                        request.options,
                        Path(root) / f"collection-{len(cache)}",
                    )
                    _, _, _, executed_command, exit_code = cache[cache_key]
                    if executed_command is not None and exit_code is not None:
                        receipts.append((executed_command, exit_code))
                status, selector_reason, nodes, _, _ = cache[cache_key]
                if (
                    status is Status.PASS
                    and "::" in selector
                    and not any(
                        node == selector
                        or node.startswith((f"{selector}[", f"{selector}::"))
                        for node in nodes
                    )
                ):
                    status = Status.TOOLING_BLOCKED
                    selector_reason = (
                        f"pytest node was not collected exactly: {selector}"
                    )
                selector_results.append((status, selector_reason))
                if status is not Status.PASS:
                    break
            statuses = [status for status, _ in selector_results]
            final = _status_rollup(statuses)
            if final is not Status.PASS:
                reason = next(
                    reason
                    for status, reason in selector_results
                    if status is final and reason
                )
                diagnostics[diagnostic_index] = replace(
                    diagnostics[diagnostic_index], status=final, reason=reason
                )
                blocked_reason = (
                    "pytest collection not executed after controlling "
                    f"{final.value}: {reason}"
                )
                for pending_index, _ in request_items[request_offset + 1 :]:
                    diagnostics[pending_index] = replace(
                        diagnostics[pending_index],
                        status=Status.TOOLING_BLOCKED,
                        reason=blocked_reason,
                    )
                break
    return tuple(receipts)


def _status_rollup(statuses: Iterable[Status]) -> Status:
    observed = tuple(statuses)
    for status in (
        Status.FAIL_TOOLING,
        Status.TOOLING_BLOCKED,
        Status.FAIL_BEHAVIOR,
        Status.PARKED,
    ):
        if status in observed:
            return status
    return Status.PASS


def _planned_qa_paths(
    config: HarnessConfig,
    check_id: str,
    *,
    planned_governed_ledger: bool,
) -> set[str]:
    planned_paths = {
        config.qa_root / "qa_step_logs_manifest.json",
        config.qa_root / "checks" / check_id / "primary.log",
    }
    if planned_governed_ledger:
        planned_paths.add(config.viability_ledger_path)
    for step_name in config.step_names:
        validate_check_id(step_name)
        planned_paths.add(config.qa_root / f"{step_name}.log")
        planned_paths.add(config.qa_root / "checks" / step_name / "primary.log")
        planned_paths.add(
            config.qa_root / "checks" / step_name.replace("_", "-") / "primary.log"
        )
    return {
        path.relative_to(config.repo_root).as_posix() for path in planned_paths
    }


def evaluate_acceptance_map_viability(
    config: HarnessConfig,
    check_id: str = "acceptance-map-viability",
    *,
    planned_governed_ledger: bool = False,
    proof_command: tuple[str, ...] | tuple[tuple[str, ...], ...] | None = None,
    proof_command_provenance: str = (
        "Current process invocation containing the approved in-process "
        "acceptance-map viability proof action"
    ),
) -> tuple[CheckResult, str]:
    """Evaluate every governed map/matrix reference without publishing files."""
    validate_check_id(check_id)
    issues: list[tuple[Status, str]] = []
    diagnostics: list[ReferenceDiagnostic] = []
    collection_requests: dict[int, PytestCollectionRequest] = {}
    referenced_manifests: set[str] = set()
    planned_paths = _planned_qa_paths(
        config,
        check_id,
        planned_governed_ledger=planned_governed_ledger,
    )
    entries: list[AcceptanceTokenEntry] = []
    acceptance_names: list[str] = []
    matrix: dict[str, MatrixRow] = {}
    token_integrity_disposition: dict[str, str] = {}
    governance_required_tokens: set[str] = set()
    acceptance_identity_is_valid = True
    governance_validator = _EvidenceGovernanceValidator(config)

    pf04_sources = tuple(
        sorted(
            (config.repo_root / "docs" / "pfcanon").glob(
                "PF04-Canon-HDE-Governance-v*.md"
            )
        )
    )
    governance_validator.set_pf04_sources(pf04_sources)
    if len(pf04_sources) != 1:
        registry: set[str] | None = None
        issues.append(
            (
                Status.TOOLING_BLOCKED,
                "exactly one current PF04 Governance source is required",
            )
        )
    else:
        registry_status, registry_reason, registry_bytes = (
            governance_validator.capture_input(
                pf04_sources[0],
                subject="PF04 Governance source",
            )
        )
        if registry_status is not Status.PASS or registry_bytes is None:
            registry = None
            issues.append((registry_status, registry_reason))
        else:
            registry, registry_error = _governance_tokens(
                config,
                captured_bytes=registry_bytes,
            )
            if registry is None:
                issues.append((Status.TOOLING_BLOCKED, registry_error))

    map_status, map_reason, map_bytes = governance_validator.capture_input(
        config.acceptance_map_path,
        subject="acceptance map",
    )
    if map_status is not Status.PASS or map_bytes is None:
        issues.append(
            (
                map_status,
                map_reason,
            )
        )
        data: object = None
    elif not map_bytes:
        issues.append(
            (
                Status.TOOLING_BLOCKED,
                f"required input unavailable: {_repo_relative(config, config.acceptance_map_path)}",
            )
        )
        data = None
    else:
        try:
            data = _loads_json_strict(map_bytes.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
            data = None
            issues.append((Status.FAIL_TOOLING, f"acceptance-map parser failed: {exc}"))
    if data is not None:
        if not isinstance(data, dict) or data.get("epic_id") != config.epic_id:
            issues.append(
                (
                    Status.FAIL_TOOLING,
                    "acceptance map epic identity is malformed or mismatched",
                )
            )
            acceptance_identity_is_valid = False
        tokens = data.get("tokens") if isinstance(data, dict) else None
        if not isinstance(tokens, list) or not tokens:
            issues.append(
                (Status.FAIL_TOOLING, "acceptance map tokens must be a non-empty list")
            )
        else:
            for token_index, item in enumerate(tokens, start=1):
                if not isinstance(item, dict):
                    issues.append(
                        (
                            Status.FAIL_TOOLING,
                            f"acceptance token entry {token_index} is not an object",
                        )
                    )
                    continue
                name = item.get("name")
                owner_pf = item.get("owner_pf")
                evidence_titles = item.get("evidence_titles")
                if not isinstance(name, str) or not TOKEN_RE.fullmatch(name):
                    issues.append(
                        (
                            Status.FAIL_TOOLING,
                            f"acceptance token entry {token_index} has an invalid name",
                        )
                    )
                    continue
                acceptance_names.append(name)
                posture = _normalized_acceptance_posture(item.get("status"))
                if posture is None:
                    issues.append(
                        (
                            Status.FAIL_TOOLING,
                            f"acceptance token {name} has a missing or invalid status",
                        )
                    )
                    token_integrity_disposition[name] = "INVALID_ACCEPTANCE_STATUS"
                if not isinstance(owner_pf, str) or not owner_pf.strip():
                    issues.append(
                        (
                            Status.FAIL_TOOLING,
                            f"acceptance token {name} has a missing or invalid owner_pf",
                        )
                    )
                    token_integrity_disposition.setdefault(
                        name, "INVALID_ACCEPTANCE_OWNER"
                    )
                    continue
                if (
                    not isinstance(evidence_titles, list)
                    or not evidence_titles
                    or any(
                        not isinstance(value, str) or not value.strip()
                        for value in evidence_titles
                    )
                ):
                    issues.append(
                        (
                            Status.FAIL_TOOLING,
                            f"acceptance token {name} has malformed or empty evidence_titles",
                        )
                    )
                    token_integrity_disposition.setdefault(
                        name, "INVALID_ACCEPTANCE_EVIDENCE_TITLES"
                    )
                    continue
                entries.append(
                    AcceptanceTokenEntry(
                        name,
                        owner_pf.strip(),
                        tuple(evidence_titles),
                        posture,
                    )
                )
            if len(acceptance_names) != len(set(acceptance_names)):
                issues.append(
                    (Status.FAIL_TOOLING, "acceptance map has duplicate token names")
                )
                for name in acceptance_names:
                    if acceptance_names.count(name) > 1:
                        token_integrity_disposition[name] = (
                            "DUPLICATE_ACCEPTANCE_TOKEN"
                        )
            if not acceptance_identity_is_valid:
                for name in acceptance_names:
                    token_integrity_disposition.setdefault(
                        name, "ACCEPTANCE_MAP_IDENTITY_MISMATCH"
                    )

    matrix_status, matrix_reason, matrix_bytes = governance_validator.capture_input(
        config.token_matrix_path,
        subject="token evidence matrix",
    )
    if matrix_status is not Status.PASS or matrix_bytes is None:
        issues.append(
            (
                matrix_status,
                matrix_reason,
            )
        )
    elif not matrix_bytes:
        issues.append(
            (
                Status.TOOLING_BLOCKED,
                f"required input unavailable: {_repo_relative(config, config.token_matrix_path)}",
            )
        )
    else:
        matrix, matrix_error = _matrix_rows(
            config.token_matrix_path,
            captured_bytes=matrix_bytes,
        )
        if matrix_error:
            issues.append((Status.FAIL_TOOLING, matrix_error))

    entry_names = set(acceptance_names)
    matrix_names = set(matrix)
    if entry_names and matrix and entry_names != matrix_names:
        issues.append(
            (Status.FAIL_TOOLING, "acceptance map and matrix token coverage differ")
        )
    for entry in entries:
        matrix_row = matrix.get(entry.name)
        if matrix_row is not None and entry.owner_pf != matrix_row.owner_pf:
            issues.append(
                (
                    Status.FAIL_TOOLING,
                    f"acceptance map and matrix owner_pf disagree for {entry.name}",
                )
            )
            token_integrity_disposition.setdefault(entry.name, "OWNER_MISMATCH")
        if matrix_row is None:
            continue
        matrix_posture = _normalized_acceptance_posture(matrix_row.status)
        if matrix_posture is None:
            issues.append(
                (
                    Status.FAIL_TOOLING,
                    f"matrix token {entry.name} has a missing or invalid status",
                )
            )
            token_integrity_disposition[entry.name] = "INVALID_MATRIX_STATUS"
        elif entry.status is None:
            pass
        elif entry.status != matrix_posture:
            issues.append(
                (
                    Status.FAIL_TOOLING,
                    "acceptance map and matrix status disagree for "
                    f"{entry.name}: {entry.status} != {matrix_posture}",
                )
            )
            token_integrity_disposition[entry.name] = "STATUS_MISMATCH"
        elif entry.status not in COMPLETE_ACCEPTANCE_POSTURES:
            issues.append(
                (
                    Status.TOOLING_BLOCKED,
                    f"acceptance token {entry.name} is not implemented: {entry.status}",
                )
            )
            token_integrity_disposition[entry.name] = entry.status.upper()
        else:
            governance_required_tokens.add(entry.name)
    if registry is not None:
        for name in sorted(entry_names - registry):
            issues.append(
                (
                    Status.FAIL_TOOLING,
                    f"acceptance map contains unregistered token: {name}",
                )
            )
            token_integrity_disposition.setdefault(name, "UNREGISTERED")

    for entry in entries:
        for item_index, value in enumerate(entry.evidence_titles, start=1):
            diagnostics.append(
                _file_diagnostic(
                    config,
                    token=entry.name,
                    source_field="acceptance_map.evidence_titles",
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                    require_governance=entry.name in governance_required_tokens,
                    governance_validator=governance_validator,
                )
            )
    for token_name in sorted(matrix):
        row = matrix[token_name]
        for item_index, value in enumerate(row.evidence_artifacts, start=1):
            diagnostics.append(
                _file_diagnostic(
                    config,
                    token=token_name,
                    source_field="matrix.evidence_artifacts",
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                    require_governance=token_name in governance_required_tokens,
                    governance_validator=governance_validator,
                )
            )
        for item_index, value in enumerate(row.ci_tests_jobs, start=1):
            diagnostic, collection_request = _ci_diagnostic(
                config,
                token=token_name,
                item_index=item_index,
                value=value,
            )
            diagnostic_index = len(diagnostics)
            diagnostics.append(diagnostic)
            if collection_request is not None and diagnostic.status is Status.PASS:
                collection_requests[diagnostic_index] = collection_request
        for item_index, value in enumerate(row.qa_root_logs, start=1):
            diagnostics.append(
                _qa_diagnostic(
                    config,
                    token=token_name,
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                    require_governance=token_name in governance_required_tokens,
                    governance_validator=governance_validator,
                )
            )
    collection_receipts = _apply_pytest_collection(
        config, diagnostics, collection_requests
    )
    stability_status, stability_reason = governance_validator.verify_stability()
    if stability_status is not Status.PASS:
        issues.append((stability_status, stability_reason))

    broken = [
        diagnostic for diagnostic in diagnostics if diagnostic.status is not Status.PASS
    ]
    all_statuses = [status for status, _ in issues] + [
        diagnostic.status for diagnostic in broken
    ]
    final_status = _status_rollup(all_statuses)
    final_reasons = [reason for status, reason in issues if status is final_status]
    final_reasons.extend(
        f"{diagnostic.token} {diagnostic.source_field}[{diagnostic.item_index}]: {diagnostic.reason}"
        for diagnostic in broken
        if diagnostic.status is final_status
    )
    reason = "; ".join(dict.fromkeys(final_reasons))

    token_status: dict[str, str] = {}
    for name in sorted(entry_names | matrix_names):
        if registry is not None and name not in registry:
            token_status[name] = "UNREGISTERED"
        elif name not in matrix_names:
            token_status[name] = "MISSING_MATRIX"
        elif name not in entry_names:
            token_status[name] = "ORPHAN_MATRIX"
        elif name in token_integrity_disposition:
            token_status[name] = token_integrity_disposition[name]
        else:
            token_diagnostics = [item.status for item in broken if item.token == name]
            token_status[name] = (
                _status_rollup(token_diagnostics).value
                if token_diagnostics
                else "VALID"
            )
    source_fields = (
        "acceptance_map.evidence_titles",
        "matrix.evidence_artifacts",
        "matrix.ci_tests_jobs",
        "matrix.qa_root_logs",
    )
    resolved_counts = {
        source_field: sum(
            diagnostic.status is Status.PASS and diagnostic.source_field == source_field
            for diagnostic in diagnostics
        )
        for source_field in source_fields
    }
    evaluation = {
        "acceptance_map_path": _repo_relative(config, config.acceptance_map_path),
        "broken_references": [diagnostic.as_dict() for diagnostic in broken],
        "epic_id": config.epic_id,
        "referenced_manifests": sorted(referenced_manifests),
        "resolved_reference_counts": resolved_counts,
        "status": final_status.value,
        "status_reason": reason,
        "token_reference_disposition": token_status,
        "token_status": token_status,
    }
    evaluation_content = (
        json.dumps(evaluation, sort_keys=True, separators=(",", ":")) + "\n"
    )
    executed_command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    exit_code: int | None
    command_provenance: str
    if len(collection_receipts) == 1:
        executed_command = collection_receipts[0][0]
        exit_code = collection_receipts[0][1]
        command_provenance = "Exact pytest collection argv executed by the viability walker"
    elif collection_receipts:
        executed_command = tuple(command for command, _ in collection_receipts)
        exit_code = collection_receipts[-1][1]
        command_provenance = (
            "Exact ordered pytest collection argv executed by the viability walker; "
            "collection stops at the first controlling non-PASS and exit_code is "
            "the last completed command result"
        )
    elif final_status is Status.PASS:
        executed_command = proof_command or (sys.executable, *sys.argv)
        _validate_command(executed_command)
        if not executed_command or not proof_command_provenance:
            raise ValueError(
                "PASS viability requires an exact command or approved proof action"
            )
        exit_code = 0
        command_provenance = proof_command_provenance
    else:
        executed_command = ()
        exit_code = None
        command_provenance = "Not executed"
    result = CheckResult(
        check_id=check_id,
        status=final_status,
        status_reason=reason,
        check_name="Acceptance-map viability",
        command=executed_command,
        command_provenance=command_provenance,
        exit_code=exit_code,
        output=evaluation_content,
        evidence_artifacts=(
            (_repo_relative(config, config.viability_ledger_path),)
            if planned_governed_ledger
            else ()
        ),
        intended_tokens=(),
        pf_refs=(
            "PF04-Canon-HDE-Governance",
            "PF14-Canon-HDE-Mechanics-Guide",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )
    return result, evaluation_content


def generate_acceptance_map_viability(
    config: HarnessConfig,
    check_id: str = "acceptance-map-viability",
    *,
    publish_governed_ledger: bool = False,
) -> ViabilityResult:
    """Evaluate and publish a current-state acceptance-map viability check."""
    result, evaluation_content = evaluate_acceptance_map_viability(
        config,
        check_id,
        planned_governed_ledger=publish_governed_ledger,
    )
    token_status = _loads_json_strict(evaluation_content)["token_status"]
    try:
        additional = (
            ((config.viability_ledger_path, evaluation_content),)
            if publish_governed_ledger
            else ()
        )
        log, manifest = record_check(config, result, additional_files=additional)
        verify_manifest_entry(config, check_id)
        governed_ledger = (
            config.viability_ledger_path if publish_governed_ledger else None
        )
        if (
            governed_ledger is not None
            and governed_ledger.read_text(encoding="utf-8") != evaluation_content
        ):
            raise RuntimeError("governed viability ledger verification failed")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        return ViabilityResult(
            Status.FAIL_TOOLING,
            f"viability evidence writer failed: {exc}",
            None,
            None,
            None,
            token_status,
        )
    return ViabilityResult(
        result.status,
        result.status_reason,
        log,
        manifest,
        governed_ledger,
        token_status,
    )


def require_governed_viability(result: ViabilityResult, expected_path: Path) -> Path:
    """Fail closed unless a generator received its verified PASS ledger."""
    ledger = result.governed_ledger
    if result.status is not Status.PASS:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_{result.status.value}:{result.status_reason}"
        )
    if ledger is None or ledger.resolve() != expected_path.resolve():
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    if not ledger.is_file() or ledger.stat().st_size == 0:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISSING")
    try:
        payload = _loads_json_strict(ledger.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"ACCEPTANCE_MAP_VIABILITY_LEDGER_MALFORMED:{exc}") from exc
    match = re.fullmatch(r"hde-epic([0-9]{3})", expected_path.parent.name)
    expected_epic = f"HDE-EPIC{match.group(1)}" if match else None
    if (
        payload.get("epic_id") != expected_epic
        or payload.get("status") != Status.PASS.value
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_STALE_OR_MISMATCHED")
    if expected_epic is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    config = HarnessConfig(expected_epic, repo_root=expected_path.parents[3])
    if result.primary_log is None or result.manifest is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_MISSING")
    if (
        result.primary_log.resolve()
        != (config.qa_root / "checks/acceptance-map-viability/primary.log").resolve()
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_PRIMARY_MISMATCH")
    if (
        result.manifest.resolve()
        != (config.qa_root / "qa_step_logs_manifest.json").resolve()
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_MANIFEST_MISMATCH")
    try:
        verify_manifest_entry(config, "acceptance-map-viability")
        primary_header = read_primary_header(result.primary_log)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_INVALID:{exc}"
        ) from exc
    ledger_reference = _repo_relative(config, ledger)
    if ledger_reference not in primary_header["evidence_artifacts"]:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_UNBOUND")
    return ledger
