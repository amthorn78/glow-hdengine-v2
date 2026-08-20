#!/usr/bin/env python3
"""Generate or check one feedback-free epic closeout candidate pair.

The candidate source, schema, plan, and evidence inputs are exact tracked files
at the current Git HEAD.  Write mode is the sole publication path for the two
derived candidate files.  Check mode is deliberately read-only.
"""
from __future__ import annotations

import argparse
import ctypes
import errno
import hashlib
import json
import os
import re
import secrets
import shutil
import stat
import struct
import subprocess
import sys
import zlib
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

sys.dont_write_bytecode = True

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ModuleNotFoundError:  # pragma: no cover - exercised by dependency readiness
    Draft202012Validator = None  # type: ignore[assignment]
    SchemaError = ValueError  # type: ignore[assignment,misc]


SCHEMA_REL = "schemas/epic_close_candidate_source.v1.json"
SOURCE_SCHEMA_VERSION = "epic_close_candidate_source.v1"
MANIFEST_SCHEMA_VERSION = "epic_close_candidate_manifest.v1"
EPIC_RE = re.compile(r"HDE-EPIC(?P<number>[0-9]{3})\Z")
RELATIVE_PATH_RE = re.compile(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\Z")
SHA_RE = re.compile(r"[0-9a-f]{40,64}\Z")
FEEDBACK_DEPENDENCY_RE = re.compile(
    r"(?:(?<![a-z0-9])(?:run[^a-z0-9\r\n]*id|receipt|attestation|"
    r"hosted[^a-z0-9\r\n]*result|later[^a-z0-9\r\n]*commit|"
    r"source[^a-z0-9\r\n]*commit|release[^a-z0-9\r\n]*id)(?![a-z0-9]))",
    re.IGNORECASE,
)
REGULAR_GIT_MODES = frozenset({"100644", "100755"})
OUTPUT_MODE = 0o644
RENAME_NOREPLACE = 1
RENAME_EXCHANGE = 2
MAX_GIT_OBJECT_BYTES = 128 * 1024 * 1024
MAX_GIT_PACK_BYTES = 512 * 1024 * 1024
MAX_GIT_PACK_COUNT = 64
MAX_GIT_PACK_OBJECTS = 2_000_000
MAX_GIT_REFERENCE_DEPTH = 16
MAX_GIT_TREE_DEPTH = 128
MAX_GIT_TREE_ENTRIES = 2_000_000
MAX_WORKTREE_FILE_BYTES = 128 * 1024 * 1024
MAX_CAUSAL_INPUT_BYTES = 128 * 1024 * 1024
MAX_OUTPUT_BYTES = 16 * 1024 * 1024
RESERVED_HEADINGS = frozenset(
    {"source bindings", "output bindings", "explicit nonclaims"}
)
REPORT_HEADING_RE = re.compile(
    r"(?!.*(?:^|[^A-Za-z0-9])_)(?!.*_(?:[^A-Za-z0-9]|$))"
    r"[A-Za-z0-9](?:[A-Za-z0-9 _.,:;()/+'-]*[A-Za-z0-9)])?\Z"
)
# Body lines are intentionally not a general CommonMark surface.  H1/H2,
# containers, fences, reference definitions, and raw HTML belong outside the
# closed custom-section body grammar so the generated section topology is unique.
REPORT_BODY_PROHIBITED_RE = re.compile(
    r"(?:"
    r"[\x00-\x1f\x7f-\x9f\u00ad\u061c\u180e\u200b-\u200f"
    r"\u2028-\u202e\u2060-\u206f\ud800-\udfff\ufeff\ufff9-\ufffb]|"
    r"^[ \t]*#{1,2}(?:[ \t]+|$)|"
    r"^[ \t]*(?:`{3,}|~{3,})|"
    r"^[ \t]*(?:=+|-+)[ \t]*$|"
    r"^[ \t]*(?:>|[-+*][ \t]+|[0-9]{1,9}[.)][ \t]+)|"
    r"^[ \t]*\[[^\]\r\n]+\]:|"
    r"[<>]"
    r")",
    re.IGNORECASE,
)
CLOSED_RAILS = {
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
NONCLAIM_TEXT = {
    "no_epic_closeout_or_pf09_movement": (
        "No PF09 movement, Product Owner closeout, or epic closeout is claimed."
    ),
    "no_hosted_feedback_or_external_attestation": (
        "No run ID, hosted result, receipt, later-commit result, release ID, "
        "or current external attestation is claimed or used as candidate feedback."
    ),
    "no_ops_live_qa_deployment_or_release": (
        "No OPS, Live QA, deployment, release, or migration is claimed."
    ),
    "no_public_contract_runtime_or_data_change": (
        "No public contract, runtime behavior, database, or persistent-data change "
        "is claimed."
    ),
    "no_qa_acceptance_or_token_satisfaction": (
        "No QA PASS, acceptance, or token satisfaction is claimed."
    ),
}


class ClosePackError(RuntimeError):
    """One deterministic fail-closed lifecycle refusal."""


@dataclass(frozen=True)
class GitTreeEntry:
    mode: str
    object_type: str
    object_id: str


@dataclass(frozen=True)
class GitIndexEntry:
    mode: str
    object_id: str
    ctime_seconds: int
    ctime_nanoseconds: int
    mtime_seconds: int
    mtime_nanoseconds: int
    device: int
    inode: int
    uid: int
    gid: int
    size: int


@dataclass(frozen=True)
class FileSnapshot:
    rel: str
    object_id: str
    payload: bytes
    fingerprint: tuple[int, int, int, int, int, int]


@dataclass(frozen=True)
class GitMarkerSnapshot:
    kind: str
    fingerprint: tuple[int, int, int, int, int, int]
    payload: bytes | None


@dataclass(frozen=True)
class GitContext:
    root: Path
    git_dir: Path
    common_dir: Path
    root_identity: tuple[int, int]
    git_dir_identity: tuple[int, int]
    common_dir_identity: tuple[int, int]
    marker: GitMarkerSnapshot
    commondir_marker: GitMarkerSnapshot | None
    gitdir_marker: GitMarkerSnapshot | None


@dataclass(frozen=True)
class GitObject:
    object_type: str
    payload: bytes


@dataclass(frozen=True)
class GitPack:
    name: str
    payload: bytes
    object_offsets: Mapping[str, int]
    offset_objects: Mapping[int, str]
    entry_crcs: Mapping[int, int]
    entry_ends: Mapping[int, int]


@dataclass(frozen=True)
class CandidateModel:
    source: Mapping[str, Any]
    source_path: str
    source_input: FileSnapshot
    schema_input: FileSnapshot
    plan_input: FileSnapshot
    evidence_inputs: tuple[tuple[str, FileSnapshot], ...]
    report_path: str
    manifest_path: str


@dataclass(frozen=True)
class OutputPreimage:
    existed: bool
    payload: bytes
    mode: int
    atime_ns: int
    mtime_ns: int
    fingerprint: tuple[int, int, int, int, int, int] | None


@dataclass(frozen=True)
class OutputAnchor:
    rel: str
    parent_path: Path
    parent_fd: int
    parent_device: int
    parent_inode: int
    name: str
    preimage: OutputPreimage


@dataclass(frozen=True)
class InstalledOutput:
    anchor: OutputAnchor
    payload: bytes
    fingerprint: tuple[int, int, int, int, int, int]
    atime_ns: int
    backup_name: str | None


def _fail(code: str) -> ClosePackError:
    return ClosePackError(code)


def _normalized_absolute_path(base: Path, raw: str) -> Path:
    if not raw or "\x00" in raw or "\\" in raw or not base.is_absolute():
        raise _fail("GIT_CONTEXT_CHANGED")
    absolute = raw.startswith(os.path.sep)
    components = [] if absolute else list(base.parts[1:])
    saw_raw_component = False
    for component in raw.split(os.path.sep):
        if not component or component == ".":
            continue
        if component == "..":
            # Git's linked-worktree ``commondir`` convention uses a leading
            # ``../..``.  A parent segment after another raw component would
            # require resolving that component first; reject that ambiguous
            # form rather than lexically erasing a possible symlink.
            if saw_raw_component or not components:
                raise _fail("GIT_CONTEXT_CHANGED")
            components.pop()
            continue
        saw_raw_component = True
        components.append(component)
    if not components:
        raise _fail("GIT_CONTEXT_CHANGED")
    return Path(os.path.sep, *components)


def _path_without_symlink_components(
    path: Path, *, final_directory: bool, code: str
) -> tuple[Path, tuple[int, int]]:
    """Validate an absolute path without following or reading any symlink."""

    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    path_only = getattr(os, "O_PATH", 0)
    cloexec = getattr(os, "O_CLOEXEC", 0)
    if not path.is_absolute() or not nofollow or not directory or not path_only:
        raise _fail(code)
    parts = path.parts[1:]
    descriptors: list[int] = []
    try:
        current_fd = os.open(
            os.path.sep, path_only | directory | nofollow | cloexec
        )
        descriptors.append(current_fd)
        final_metadata = os.fstat(current_fd)
        for index, part in enumerate(parts):
            if part in {"", ".", ".."}:
                raise _fail(code)
            final = index == len(parts) - 1
            if final and not final_directory:
                metadata = os.stat(part, dir_fd=current_fd, follow_symlinks=False)
                if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(
                    metadata.st_mode
                ):
                    raise _fail(code)
                final_metadata = metadata
                break
            child_fd = os.open(
                part,
                path_only | directory | nofollow | cloexec,
                dir_fd=current_fd,
            )
            descriptors.append(child_fd)
            metadata = os.fstat(child_fd)
            if not stat.S_ISDIR(metadata.st_mode):
                raise _fail(code)
            final_metadata = metadata
            current_fd = child_fd
        if not parts and not final_directory:
            raise _fail(code)
        return path, (final_metadata.st_dev, final_metadata.st_ino)
    except ClosePackError:
        raise
    except OSError as exc:
        raise _fail(code) from exc
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _resolved_marker_target(base: Path, raw: str) -> tuple[Path, tuple[int, int]]:
    return _path_without_symlink_components(
        _normalized_absolute_path(base, raw),
        final_directory=True,
        code="GIT_CONTEXT_CHANGED",
    )


def _resolved_backlink_target(raw: str) -> tuple[Path, tuple[int, int]]:
    return _path_without_symlink_components(
        _normalized_absolute_path(Path(os.path.sep), raw),
        final_directory=False,
        code="GIT_CONTEXT_CHANGED",
    )


def _verify_git_context(context: GitContext) -> None:
    try:
        root_metadata = context.root.lstat()
        git_dir_metadata = context.git_dir.lstat()
        common_dir_metadata = context.common_dir.lstat()
        marker_metadata = (context.root / ".git").lstat()
    except OSError as exc:
        raise _fail("GIT_CONTEXT_CHANGED") from exc
    if (
        not stat.S_ISDIR(root_metadata.st_mode)
        or stat.S_ISLNK(root_metadata.st_mode)
        or (root_metadata.st_dev, root_metadata.st_ino) != context.root_identity
        or not stat.S_ISDIR(git_dir_metadata.st_mode)
        or stat.S_ISLNK(git_dir_metadata.st_mode)
        or (git_dir_metadata.st_dev, git_dir_metadata.st_ino)
        != context.git_dir_identity
        or not stat.S_ISDIR(common_dir_metadata.st_mode)
        or stat.S_ISLNK(common_dir_metadata.st_mode)
        or (common_dir_metadata.st_dev, common_dir_metadata.st_ino)
        != context.common_dir_identity
        or _fingerprint(marker_metadata) != context.marker.fingerprint
    ):
        raise _fail("GIT_CONTEXT_CHANGED")
    if context.marker.kind == "directory":
        if not stat.S_ISDIR(marker_metadata.st_mode) or stat.S_ISLNK(
            marker_metadata.st_mode
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
        if context.marker.payload is not None:
            raise _fail("GIT_CONTEXT_CHANGED")
        resolved_git_dir, resolved_git_dir_identity = (
            _path_without_symlink_components(
                context.root / ".git",
                final_directory=True,
                code="GIT_CONTEXT_CHANGED",
            )
        )
        if (
            resolved_git_dir != context.git_dir
            or resolved_git_dir_identity != context.git_dir_identity
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
    else:
        if (
            context.marker.kind != "file"
            or not stat.S_ISREG(marker_metadata.st_mode)
            or stat.S_ISLNK(marker_metadata.st_mode)
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
        payload, stable = _stable_absolute_read(context.root / ".git")
        if (
            payload != context.marker.payload
            or _fingerprint(stable) != context.marker.fingerprint
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            lines = payload.decode("utf-8").splitlines()
        except UnicodeDecodeError as exc:
            raise _fail("GIT_CONTEXT_CHANGED") from exc
        if len(lines) != 1 or not lines[0].startswith("gitdir: "):
            raise _fail("GIT_CONTEXT_CHANGED")
        resolved_git_dir, resolved_git_dir_identity = _resolved_marker_target(
            context.root, lines[0][8:]
        )
        if (
            resolved_git_dir != context.git_dir
            or resolved_git_dir_identity != context.git_dir_identity
        ):
            raise _fail("GIT_CONTEXT_CHANGED")

    commondir_path = context.git_dir / "commondir"
    try:
        commondir_metadata = commondir_path.lstat()
    except FileNotFoundError:
        if context.commondir_marker is not None:
            raise _fail("GIT_CONTEXT_CHANGED")
    except OSError as exc:
        raise _fail("GIT_CONTEXT_CHANGED") from exc
    else:
        marker = context.commondir_marker
        if (
            marker is None
            or marker.kind != "file"
            or not stat.S_ISREG(commondir_metadata.st_mode)
            or stat.S_ISLNK(commondir_metadata.st_mode)
            or _fingerprint(commondir_metadata) != marker.fingerprint
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
        payload, stable = _stable_absolute_read(commondir_path)
        if payload != marker.payload or _fingerprint(stable) != marker.fingerprint:
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            lines = payload.decode("utf-8").splitlines()
        except UnicodeDecodeError as exc:
            raise _fail("GIT_CONTEXT_CHANGED") from exc
        if len(lines) != 1 or not lines[0]:
            raise _fail("GIT_CONTEXT_CHANGED")
        resolved_common_dir, resolved_common_dir_identity = _resolved_marker_target(
            context.git_dir, lines[0]
        )
        if (
            resolved_common_dir != context.common_dir
            or resolved_common_dir_identity != context.common_dir_identity
        ):
            raise _fail("GIT_CONTEXT_CHANGED")

    gitdir_path = context.git_dir / "gitdir"
    try:
        gitdir_metadata = gitdir_path.lstat()
    except FileNotFoundError:
        if context.gitdir_marker is not None:
            raise _fail("GIT_CONTEXT_CHANGED")
    except OSError as exc:
        raise _fail("GIT_CONTEXT_CHANGED") from exc
    else:
        marker = context.gitdir_marker
        if (
            marker is None
            or marker.kind != "file"
            or not stat.S_ISREG(gitdir_metadata.st_mode)
            or stat.S_ISLNK(gitdir_metadata.st_mode)
            or _fingerprint(gitdir_metadata) != marker.fingerprint
        ):
            raise _fail("GIT_CONTEXT_CHANGED")
        payload, stable = _stable_absolute_read(gitdir_path)
        if payload != marker.payload or _fingerprint(stable) != marker.fingerprint:
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            lines = payload.decode("utf-8").splitlines()
        except (UnicodeDecodeError, IndexError) as exc:
            raise _fail("GIT_CONTEXT_CHANGED") from exc
        if len(lines) != 1 or not Path(lines[0]).is_absolute():
            raise _fail("GIT_CONTEXT_CHANGED")
        resolved_backlink, resolved_backlink_identity = _resolved_backlink_target(
            lines[0]
        )
        if (
            resolved_backlink != context.root / ".git"
            or resolved_backlink_identity
            != (context.marker.fingerprint[0], context.marker.fingerprint[1])
        ):
            raise _fail("GIT_CONTEXT_CHANGED")


def _run_git(location: Path | GitContext, *args: str) -> bytes:
    candidate = shutil.which("git", path=os.defpath)
    if candidate is None:
        raise _fail("GIT_UNAVAILABLE")
    try:
        executable = Path(candidate).resolve(strict=True)
    except OSError as exc:
        raise _fail("GIT_UNAVAILABLE") from exc
    if not executable.is_file() or not os.access(executable, os.X_OK):
        raise _fail("GIT_UNAVAILABLE")
    environment = {
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_OPTIONAL_LOCKS": "0",
        "GIT_NO_LAZY_FETCH": "1",
        "GIT_NO_REPLACE_OBJECTS": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": os.defpath,
        "TZ": "UTC",
    }
    context = location if isinstance(location, GitContext) else None
    if context is not None:
        _verify_git_context(context)
        repository_args = (
            f"--git-dir={context.git_dir}",
            f"--work-tree={context.root}",
        )
    else:
        repository_args = ("-C", str(location))
    try:
        completed = subprocess.run(
            (
                str(executable),
                "-c",
                "core.fsmonitor=false",
                "-c",
                "core.hooksPath=/dev/null",
                "-c",
                "core.untrackedCache=false",
                *repository_args,
                *args,
            ),
            capture_output=True,
            check=False,
            env=environment,
            shell=False,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise _fail("GIT_UNAVAILABLE") from exc
    if context is not None:
        _verify_git_context(context)
    if completed.returncode != 0:
        raise _fail("GIT_COMMAND_FAILED")
    return completed.stdout


def _repository_root() -> Path:
    try:
        cwd = Path.cwd().resolve(strict=True)
    except OSError as exc:
        raise _fail("GIT_ROOT_INVALID") from exc
    for candidate in (cwd, *cwd.parents):
        marker = candidate / ".git"
        try:
            metadata = marker.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise _fail("GIT_ROOT_INVALID") from exc
        if stat.S_ISLNK(metadata.st_mode) or not (
            stat.S_ISDIR(metadata.st_mode) or stat.S_ISREG(metadata.st_mode)
        ):
            raise _fail("GIT_ROOT_INVALID")
        return candidate
    raise _fail("GIT_WORKTREE_UNAVAILABLE")


def _establish_git_context(root: Path) -> GitContext:
    try:
        root_metadata = root.lstat()
        marker_path = root / ".git"
        marker_metadata = marker_path.lstat()
    except OSError as exc:
        raise _fail("GIT_CONTEXT_INVALID") from exc
    if not stat.S_ISDIR(root_metadata.st_mode) or stat.S_ISLNK(root_metadata.st_mode):
        raise _fail("GIT_CONTEXT_INVALID")

    marker_payload: bytes | None
    if stat.S_ISDIR(marker_metadata.st_mode) and not stat.S_ISLNK(
        marker_metadata.st_mode
    ):
        git_dir, opened_git_dir_identity = _path_without_symlink_components(
            marker_path, final_directory=True, code="GIT_CONTEXT_INVALID"
        )
        marker_kind = "directory"
        marker_payload = None
    elif stat.S_ISREG(marker_metadata.st_mode) and not stat.S_ISLNK(
        marker_metadata.st_mode
    ):
        marker_payload, stable = _stable_absolute_read(marker_path)
        if _fingerprint(stable) != _fingerprint(marker_metadata):
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            marker_text = marker_payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise _fail("GIT_CONTEXT_INVALID") from exc
        marker_lines = marker_text.splitlines()
        if len(marker_lines) != 1 or not marker_lines[0].startswith("gitdir: "):
            raise _fail("GIT_CONTEXT_INVALID")
        try:
            git_dir, opened_git_dir_identity = _path_without_symlink_components(
                _normalized_absolute_path(root, marker_lines[0][8:]),
                final_directory=True,
                code="GIT_CONTEXT_INVALID",
            )
        except ClosePackError as exc:
            raise _fail("GIT_CONTEXT_INVALID") from exc
        marker_kind = "file"
    else:
        raise _fail("GIT_CONTEXT_INVALID")

    commondir_path = git_dir / "commondir"
    try:
        commondir_metadata = commondir_path.lstat()
    except FileNotFoundError:
        common_dir = git_dir
        commondir_marker = None
    except OSError as exc:
        raise _fail("GIT_CONTEXT_INVALID") from exc
    else:
        if not stat.S_ISREG(commondir_metadata.st_mode) or stat.S_ISLNK(
            commondir_metadata.st_mode
        ):
            raise _fail("GIT_CONTEXT_INVALID")
        commondir_payload, stable = _stable_absolute_read(commondir_path)
        if _fingerprint(stable) != _fingerprint(commondir_metadata):
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            commondir_text = commondir_payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise _fail("GIT_CONTEXT_INVALID") from exc
        commondir_lines = commondir_text.splitlines()
        if len(commondir_lines) != 1 or not commondir_lines[0]:
            raise _fail("GIT_CONTEXT_INVALID")
        try:
            common_dir, opened_common_dir_identity = _path_without_symlink_components(
                _normalized_absolute_path(git_dir, commondir_lines[0]),
                final_directory=True,
                code="GIT_CONTEXT_INVALID",
            )
        except ClosePackError as exc:
            raise _fail("GIT_CONTEXT_INVALID") from exc
        commondir_marker = GitMarkerSnapshot(
            "file",
            _fingerprint(commondir_metadata),
            commondir_payload,
        )
    if commondir_marker is None:
        opened_common_dir_identity = opened_git_dir_identity

    try:
        git_dir_metadata = git_dir.lstat()
        common_dir_metadata = common_dir.lstat()
    except OSError as exc:
        raise _fail("GIT_CONTEXT_INVALID") from exc
    if (
        not stat.S_ISDIR(git_dir_metadata.st_mode)
        or stat.S_ISLNK(git_dir_metadata.st_mode)
        or not stat.S_ISDIR(common_dir_metadata.st_mode)
        or stat.S_ISLNK(common_dir_metadata.st_mode)
        or (git_dir_metadata.st_dev, git_dir_metadata.st_ino)
        != opened_git_dir_identity
        or (common_dir_metadata.st_dev, common_dir_metadata.st_ino)
        != opened_common_dir_identity
    ):
        raise _fail("GIT_CONTEXT_INVALID")

    gitdir_backlink = git_dir / "gitdir"
    try:
        gitdir_backlink_metadata = gitdir_backlink.lstat()
    except FileNotFoundError:
        if marker_kind == "file":
            raise _fail("GIT_CONTEXT_INVALID")
        gitdir_marker = None
    except OSError as exc:
        raise _fail("GIT_CONTEXT_INVALID") from exc
    else:
        if (
            marker_kind != "file"
            or not stat.S_ISREG(gitdir_backlink_metadata.st_mode)
            or stat.S_ISLNK(gitdir_backlink_metadata.st_mode)
        ):
            raise _fail("GIT_CONTEXT_INVALID")
        gitdir_backlink_payload, stable = _stable_absolute_read(gitdir_backlink)
        if _fingerprint(stable) != _fingerprint(gitdir_backlink_metadata):
            raise _fail("GIT_CONTEXT_CHANGED")
        try:
            backlink_lines = gitdir_backlink_payload.decode("utf-8").splitlines()
            backlink_path = Path(backlink_lines[0])
        except (UnicodeDecodeError, IndexError) as exc:
            raise _fail("GIT_CONTEXT_INVALID") from exc
        resolved_backlink, resolved_backlink_identity = _resolved_backlink_target(
            backlink_lines[0]
        )
        if (
            len(backlink_lines) != 1
            or not backlink_path.is_absolute()
            or resolved_backlink != marker_path
            or resolved_backlink_identity
            != (marker_metadata.st_dev, marker_metadata.st_ino)
        ):
            raise _fail("GIT_CONTEXT_INVALID")
        gitdir_marker = GitMarkerSnapshot(
            "file",
            _fingerprint(gitdir_backlink_metadata),
            gitdir_backlink_payload,
        )

    context = GitContext(
        root=root,
        git_dir=git_dir,
        common_dir=common_dir,
        root_identity=(root_metadata.st_dev, root_metadata.st_ino),
        git_dir_identity=(git_dir_metadata.st_dev, git_dir_metadata.st_ino),
        common_dir_identity=(common_dir_metadata.st_dev, common_dir_metadata.st_ino),
        marker=GitMarkerSnapshot(
            marker_kind,
            _fingerprint(marker_metadata),
            marker_payload,
        ),
        commondir_marker=commondir_marker,
        gitdir_marker=gitdir_marker,
    )
    _verify_git_context(context)
    return context


def _verify_git_repository(context: GitContext) -> None:
    try:
        inside = _run_git(context, "rev-parse", "--is-inside-work-tree")
        root = Path(
            _run_git(context, "rev-parse", "--show-toplevel")
            .decode("utf-8")
            .strip()
        ).resolve(strict=True)
        git_dir = Path(
            _run_git(context, "rev-parse", "--absolute-git-dir")
            .decode("utf-8")
            .strip()
        ).resolve(strict=True)
        common_dir = Path(
            _run_git(context, "rev-parse", "--path-format=absolute", "--git-common-dir")
            .decode("utf-8")
            .strip()
        ).resolve(strict=True)
    except (ClosePackError, OSError, UnicodeDecodeError) as exc:
        raise _fail("GIT_WORKTREE_UNAVAILABLE") from exc
    if (
        inside != b"true\n"
        or root != context.root
        or git_dir != context.git_dir
        or common_dir != context.common_dir
    ):
        raise _fail("GIT_CONTEXT_INVALID")


def _head(context: GitContext, store: _GitObjectStore | None = None) -> str:
    object_id = _resolve_head_oid(context)
    _validate_repository_config(context, _object_algorithm(object_id))
    reader = store or _GitObjectStore(context)
    return _peel_head_commit(reader, object_id)


def _require_clean(root: Path, context: GitContext) -> None:
    if _worktree_changes(root, context):
        raise _fail("DIRTY_TREE")


def _canonical_relative_path(raw: object, *, code: str = "PATH_INVALID") -> str:
    if (
        not isinstance(raw, str)
        or not raw
        or "\\" in raw
        or "\x00" in raw
        or RELATIVE_PATH_RE.fullmatch(raw) is None
    ):
        raise _fail(code)
    pure = PurePosixPath(raw)
    if (
        pure.is_absolute()
        or any(part in {"", ".", ".."} for part in pure.parts)
        or pure.as_posix() != raw
    ):
        raise _fail(code)
    return raw


def _tree_entries(
    context: GitContext, store: _GitObjectStore | None = None
) -> dict[str, GitTreeEntry]:
    return _tree_entries_from_store(context, store or _GitObjectStore(context))


def _require_tracked_regular(
    tree: Mapping[str, GitTreeEntry], rel: str
) -> GitTreeEntry:
    entry = tree.get(rel)
    if entry is None:
        raise _fail("INPUT_UNTRACKED")
    aliases = [path for path in tree if path.casefold() == rel.casefold()]
    if aliases != [rel]:
        raise _fail("INPUT_CASE_AMBIGUOUS")
    if entry.object_type != "blob" or entry.mode not in REGULAR_GIT_MODES:
        raise _fail("INPUT_NOT_REGULAR")
    return entry


def _fingerprint(metadata: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def _stable_read(
    root: Path, rel: str, *, max_bytes: int | None = None
) -> tuple[bytes, tuple[int, int, int, int, int, int]]:
    parts = PurePosixPath(rel).parts
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if (
        not nofollow
        or not directory
        or not noatime
        or os.open not in os.supports_dir_fd
    ):
        raise _fail("NOFOLLOW_UNAVAILABLE")
    descriptors: list[int] = []
    edges: list[tuple[int, str, int]] = []
    try:
        root_fd = os.open(root, os.O_RDONLY | directory | nofollow | noatime)
        descriptors.append(root_fd)
        parent_fd = root_fd
        for part in parts[:-1]:
            child_fd = os.open(
                part,
                os.O_RDONLY | directory | nofollow | noatime,
                dir_fd=parent_fd,
            )
            descriptors.append(child_fd)
            child_stat = os.fstat(child_fd)
            if not stat.S_ISDIR(child_stat.st_mode):
                raise _fail("INPUT_NOT_REGULAR")
            edges.append((parent_fd, part, child_fd))
            parent_fd = child_fd
        file_fd = os.open(
            parts[-1],
            os.O_RDONLY | nofollow | noatime | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        descriptors.append(file_fd)
        before = os.fstat(file_fd)
        if not stat.S_ISREG(before.st_mode):
            raise _fail("INPUT_NOT_REGULAR")
        if max_bytes is not None and before.st_size > max_bytes:
            raise _fail("INPUT_TOO_LARGE")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(file_fd, 1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if max_bytes is not None and total > max_bytes:
                raise _fail("INPUT_TOO_LARGE")
            chunks.append(chunk)
        payload = b"".join(chunks)
        after = os.fstat(file_fd)
        linked = os.stat(parts[-1], dir_fd=parent_fd, follow_symlinks=False)
        if (
            not stat.S_ISREG(linked.st_mode)
            or _fingerprint(before) != _fingerprint(after)
            or _fingerprint(after) != _fingerprint(linked)
            or len(payload) != after.st_size
        ):
            raise _fail("INPUT_CHANGED")
        for ancestor_fd, part, child_fd in reversed(edges):
            opened = os.fstat(child_fd)
            current = os.stat(part, dir_fd=ancestor_fd, follow_symlinks=False)
            if (
                not stat.S_ISDIR(current.st_mode)
                or (opened.st_dev, opened.st_ino)
                != (current.st_dev, current.st_ino)
            ):
                raise _fail("INPUT_CHANGED")
        current_root = root.stat()
        opened_root = os.fstat(root_fd)
        if (opened_root.st_dev, opened_root.st_ino) != (
            current_root.st_dev,
            current_root.st_ino,
        ):
            raise _fail("INPUT_CHANGED")
        return payload, _fingerprint(after)
    except ClosePackError:
        raise
    except (FileNotFoundError, NotADirectoryError) as exc:
        raise _fail("INPUT_MISSING") from exc
    except OSError as exc:
        raise _fail("INPUT_ALIAS_OR_UNAVAILABLE") from exc
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _stable_symlink_read(root: Path, rel: str) -> bytes:
    """Read exact symlink bytes under the sole approved atime exemption.

    ``readlink`` has no no-atime flag.  The kernel may therefore advance only
    the tracked symlink inode's atime.  This function never attempts to restore
    that timestamp and rejects every content, identity, mtime, or ctime change.
    """

    parts = PurePosixPath(rel).parts
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if (
        not nofollow
        or not directory
        or not noatime
        or os.readlink not in os.supports_dir_fd
    ):
        raise _fail("NOFOLLOW_UNAVAILABLE")
    descriptors: list[int] = []
    edges: list[tuple[int, str, int]] = []
    try:
        root_fd = os.open(root, os.O_RDONLY | directory | nofollow | noatime)
        descriptors.append(root_fd)
        parent_fd = root_fd
        for part in parts[:-1]:
            child_fd = os.open(
                part,
                os.O_RDONLY | directory | nofollow | noatime,
                dir_fd=parent_fd,
            )
            descriptors.append(child_fd)
            child_stat = os.fstat(child_fd)
            if not stat.S_ISDIR(child_stat.st_mode):
                raise _fail("SYMLINK_PATH_INVALID")
            edges.append((parent_fd, part, child_fd))
            parent_fd = child_fd
        before = os.stat(parts[-1], dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISLNK(before.st_mode):
            raise _fail("SYMLINK_PATH_INVALID")
        target = os.readlink(parts[-1], dir_fd=parent_fd)
        after = os.stat(parts[-1], dir_fd=parent_fd, follow_symlinks=False)
        if (
            not stat.S_ISLNK(after.st_mode)
            or _fingerprint(before) != _fingerprint(after)
        ):
            raise _fail("SYMLINK_CHANGED")
        for ancestor_fd, part, child_fd in reversed(edges):
            opened = os.fstat(child_fd)
            current = os.stat(part, dir_fd=ancestor_fd, follow_symlinks=False)
            if (
                not stat.S_ISDIR(current.st_mode)
                or (opened.st_dev, opened.st_ino)
                != (current.st_dev, current.st_ino)
            ):
                raise _fail("SYMLINK_CHANGED")
        current_root = root.stat()
        opened_root = os.fstat(root_fd)
        if (opened_root.st_dev, opened_root.st_ino) != (
            current_root.st_dev,
            current_root.st_ino,
        ):
            raise _fail("SYMLINK_CHANGED")
        return os.fsencode(target)
    except ClosePackError:
        raise
    except (FileNotFoundError, NotADirectoryError) as exc:
        raise _fail("SYMLINK_MISSING") from exc
    except OSError as exc:
        raise _fail("SYMLINK_READ_UNAVAILABLE") from exc
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _stable_directory_names(
    root: Path, rel: str, *, missing_ok: bool = False
) -> tuple[str, ...]:
    parts = PurePosixPath(rel).parts
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if not nofollow or not directory or not noatime:
        raise _fail("NOFOLLOW_UNAVAILABLE")
    descriptors: list[int] = []
    edges: list[tuple[int, str, int]] = []
    try:
        root_fd = os.open(root, os.O_RDONLY | directory | nofollow | noatime)
        descriptors.append(root_fd)
        parent_fd = root_fd
        for part in parts:
            child_fd = os.open(
                part,
                os.O_RDONLY | directory | nofollow | noatime,
                dir_fd=parent_fd,
            )
            descriptors.append(child_fd)
            child_stat = os.fstat(child_fd)
            if not stat.S_ISDIR(child_stat.st_mode):
                raise _fail("GIT_OBJECT_STORE_INVALID")
            edges.append((parent_fd, part, child_fd))
            parent_fd = child_fd
        names = tuple(sorted(os.listdir(parent_fd)))
        for ancestor_fd, part, child_fd in reversed(edges):
            opened = os.fstat(child_fd)
            current = os.stat(part, dir_fd=ancestor_fd, follow_symlinks=False)
            if (
                not stat.S_ISDIR(current.st_mode)
                or (opened.st_dev, opened.st_ino)
                != (current.st_dev, current.st_ino)
            ):
                raise _fail("GIT_OBJECT_STORE_CHANGED")
        current_root = root.stat()
        opened_root = os.fstat(root_fd)
        if (opened_root.st_dev, opened_root.st_ino) != (
            current_root.st_dev,
            current_root.st_ino,
        ):
            raise _fail("GIT_OBJECT_STORE_CHANGED")
        return names
    except FileNotFoundError as exc:
        if missing_ok:
            return ()
        raise _fail("GIT_OBJECT_STORE_UNAVAILABLE") from exc
    except ClosePackError:
        raise
    except OSError as exc:
        raise _fail("GIT_OBJECT_STORE_UNAVAILABLE") from exc
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _object_algorithm(object_id: str) -> str:
    if len(object_id) == 40 and SHA_RE.fullmatch(object_id) is not None:
        return "sha1"
    if len(object_id) == 64 and SHA_RE.fullmatch(object_id) is not None:
        return "sha256"
    raise _fail("GIT_OBJECT_ID_INVALID")


def _hash_git_object(object_type: str, payload: bytes, algorithm: str) -> str:
    try:
        digest = hashlib.new(algorithm)
    except ValueError as exc:
        raise _fail("GIT_OBJECT_FORMAT_UNSUPPORTED") from exc
    digest.update(f"{object_type} {len(payload)}\0".encode("ascii"))
    digest.update(payload)
    return digest.hexdigest()


def _parse_git_object(raw: bytes, object_id: str) -> GitObject:
    algorithm = _object_algorithm(object_id)
    if hashlib.new(algorithm, raw).hexdigest() != object_id:
        raise _fail("GIT_OBJECT_INVALID")
    try:
        header, payload = raw.split(b"\0", 1)
        object_type_bytes, size_bytes = header.split(b" ", 1)
        object_type = object_type_bytes.decode("ascii")
        size = int(size_bytes.decode("ascii"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise _fail("GIT_OBJECT_INVALID") from exc
    if (
        object_type not in {"blob", "commit", "tag", "tree"}
        or size != len(payload)
        or header != f"{object_type} {len(payload)}".encode("ascii")
    ):
        raise _fail("GIT_OBJECT_INVALID")
    return GitObject(object_type, payload)


def _decode_delta_integer(payload: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if offset >= len(payload) or shift > 63:
            raise _fail("GIT_PACK_INVALID")
        byte = payload[offset]
        offset += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, offset
        shift += 7


def _apply_git_delta(base: bytes, delta: bytes) -> bytes:
    base_size, offset = _decode_delta_integer(delta, 0)
    result_size, offset = _decode_delta_integer(delta, offset)
    if (
        base_size != len(base)
        or base_size > MAX_GIT_OBJECT_BYTES
        or result_size > MAX_GIT_OBJECT_BYTES
    ):
        raise _fail("GIT_PACK_INVALID")
    result = bytearray()
    while offset < len(delta):
        opcode = delta[offset]
        offset += 1
        if opcode & 0x80:
            copy_offset = 0
            copy_size = 0
            for bit, shift in ((0x01, 0), (0x02, 8), (0x04, 16), (0x08, 24)):
                if opcode & bit:
                    if offset >= len(delta):
                        raise _fail("GIT_PACK_INVALID")
                    copy_offset |= delta[offset] << shift
                    offset += 1
            for bit, shift in ((0x10, 0), (0x20, 8), (0x40, 16)):
                if opcode & bit:
                    if offset >= len(delta):
                        raise _fail("GIT_PACK_INVALID")
                    copy_size |= delta[offset] << shift
                    offset += 1
            if copy_size == 0:
                copy_size = 0x10000
            end = copy_offset + copy_size
            if end > len(base):
                raise _fail("GIT_PACK_INVALID")
            result.extend(base[copy_offset:end])
        elif opcode:
            end = offset + opcode
            if end > len(delta):
                raise _fail("GIT_PACK_INVALID")
            result.extend(delta[offset:end])
            offset = end
        else:
            raise _fail("GIT_PACK_INVALID")
        if len(result) > result_size:
            raise _fail("GIT_PACK_INVALID")
    if len(result) != result_size:
        raise _fail("GIT_PACK_INVALID")
    return bytes(result)


class _GitObjectStore:
    def __init__(self, context: GitContext) -> None:
        self.context = context
        self.algorithm: str | None = None
        self.objects: dict[str, GitObject] = {}
        self.pack_objects: dict[tuple[str, int], GitObject] = {}
        self.packs: tuple[GitPack, ...] | None = None
        _verify_git_context(context)
        for rel in ("objects/info/alternates", "objects/info/http-alternates"):
            try:
                metadata = (context.common_dir / rel).lstat()
            except FileNotFoundError:
                continue
            except OSError as exc:
                raise _fail("GIT_OBJECT_STORE_UNAVAILABLE") from exc
            if stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
                raise _fail("GIT_OBJECT_STORE_EXTERNAL")
            raise _fail("GIT_OBJECT_STORE_INVALID")

    def read(self, object_id: str, stack: tuple[str, ...] = ()) -> GitObject:
        object_id = object_id.lower()
        algorithm = _object_algorithm(object_id)
        if self.algorithm is None:
            self.algorithm = algorithm
        elif algorithm != self.algorithm:
            raise _fail("GIT_OBJECT_FORMAT_MISMATCH")
        if object_id in stack or len(stack) >= 64:
            raise _fail("GIT_OBJECT_CYCLE")
        cached = self.objects.get(object_id)
        if cached is not None:
            return cached
        loose = self._read_loose(object_id)
        if loose is not None:
            self.objects[object_id] = loose
            return loose
        for pack in self._load_packs(algorithm):
            offset = pack.object_offsets.get(object_id)
            if offset is None:
                continue
            value = self._read_pack_entry(pack, offset, (*stack, object_id))
            if _hash_git_object(
                value.object_type,
                value.payload,
                algorithm,
            ) != object_id:
                raise _fail("GIT_OBJECT_INVALID")
            self.objects[object_id] = value
            return value
        raise _fail("GIT_OBJECT_MISSING")

    def _read_loose(self, object_id: str) -> GitObject | None:
        rel = f"objects/{object_id[:2]}/{object_id[2:]}"
        try:
            compressed, _ = _stable_read(
                self.context.common_dir,
                rel,
                max_bytes=MAX_GIT_OBJECT_BYTES,
            )
        except ClosePackError as exc:
            if str(exc) == "INPUT_MISSING":
                return None
            raise _fail("GIT_OBJECT_STORE_UNAVAILABLE") from exc
        try:
            inflater = zlib.decompressobj()
            raw = inflater.decompress(compressed, MAX_GIT_OBJECT_BYTES + 1)
        except zlib.error as exc:
            raise _fail("GIT_OBJECT_INVALID") from exc
        if (
            len(raw) > MAX_GIT_OBJECT_BYTES
            or not inflater.eof
            or inflater.unused_data
            or inflater.unconsumed_tail
        ):
            raise _fail("GIT_OBJECT_INVALID")
        raw += inflater.flush()
        return _parse_git_object(raw, object_id)

    def _load_packs(self, algorithm: str) -> tuple[GitPack, ...]:
        if self.packs is not None:
            return self.packs
        names = _stable_directory_names(
            self.context.common_dir, "objects/pack", missing_ok=True
        )
        digest_size = hashlib.new(algorithm).digest_size
        packs: list[GitPack] = []
        cumulative_bytes = 0
        cumulative_objects = 0
        for name in names:
            match = re.fullmatch(r"pack-([0-9a-f]{40}|[0-9a-f]{64})\.idx", name)
            if match is None or len(match.group(1)) != digest_size * 2:
                continue
            pack_name = name[:-4] + ".pack"
            if pack_name not in names:
                raise _fail("GIT_PACK_INVALID")
            if len(packs) >= MAX_GIT_PACK_COUNT:
                raise _fail("GIT_PACK_STORE_TOO_LARGE")
            try:
                index_size = (self.context.common_dir / "objects/pack" / name).lstat()
                pack_size = (
                    self.context.common_dir / "objects/pack" / pack_name
                ).lstat()
            except OSError as exc:
                raise _fail("GIT_PACK_UNAVAILABLE") from exc
            if (
                not stat.S_ISREG(index_size.st_mode)
                or stat.S_ISLNK(index_size.st_mode)
                or not stat.S_ISREG(pack_size.st_mode)
                or stat.S_ISLNK(pack_size.st_mode)
                or cumulative_bytes + index_size.st_size + pack_size.st_size
                > MAX_GIT_PACK_BYTES
            ):
                raise _fail("GIT_PACK_STORE_TOO_LARGE")
            try:
                index_payload, _ = _stable_read(
                    self.context.common_dir,
                    f"objects/pack/{name}",
                    max_bytes=MAX_GIT_PACK_BYTES,
                )
                pack_payload, _ = _stable_read(
                    self.context.common_dir,
                    f"objects/pack/{pack_name}",
                    max_bytes=MAX_GIT_PACK_BYTES,
                )
            except ClosePackError as exc:
                raise _fail("GIT_PACK_UNAVAILABLE") from exc
            offsets, entry_crcs = self._parse_pack_index(index_payload, algorithm)
            cumulative_bytes += len(index_payload) + len(pack_payload)
            cumulative_objects += len(offsets)
            if (
                len(pack_payload) < 12 + digest_size
                or pack_payload[:4] != b"PACK"
                or int.from_bytes(pack_payload[4:8], "big") not in {2, 3}
                or int.from_bytes(pack_payload[8:12], "big") != len(offsets)
                or len(offsets) > MAX_GIT_PACK_OBJECTS
                or cumulative_bytes > MAX_GIT_PACK_BYTES
                or cumulative_objects > MAX_GIT_PACK_OBJECTS
                or (offsets and min(offsets.values()) != 12)
                or any(
                    offset >= len(pack_payload) - digest_size
                    for offset in offsets.values()
                )
            ):
                raise _fail("GIT_PACK_INVALID")
            ordered_offsets = sorted(offsets.values())
            entry_ends = {
                offset: (
                    ordered_offsets[index + 1]
                    if index + 1 < len(ordered_offsets)
                    else len(pack_payload) - digest_size
                )
                for index, offset in enumerate(ordered_offsets)
            }
            pack_checksum = index_payload[-2 * digest_size : -digest_size]
            if (
                pack_payload[-digest_size:] != pack_checksum
                or hashlib.new(algorithm, pack_payload[:-digest_size]).digest()
                != pack_checksum
            ):
                raise _fail("GIT_PACK_INVALID")
            packs.append(
                GitPack(
                    pack_name,
                    pack_payload,
                    offsets,
                    {offset: oid for oid, offset in offsets.items()},
                    entry_crcs,
                    entry_ends,
                )
            )
        self.packs = tuple(packs)
        return self.packs

    @staticmethod
    def _parse_pack_index(
        payload: bytes, algorithm: str
    ) -> tuple[dict[str, int], dict[int, int]]:
        digest_size = hashlib.new(algorithm).digest_size
        fanout_end = 8 + 256 * 4
        if (
            len(payload) < fanout_end + 2 * digest_size
            or payload[:4] != b"\xfftOc"
            or int.from_bytes(payload[4:8], "big") != 2
            or hashlib.new(algorithm, payload[:-digest_size]).digest()
            != payload[-digest_size:]
        ):
            raise _fail("GIT_PACK_INDEX_INVALID")
        fanout = [
            int.from_bytes(payload[offset : offset + 4], "big")
            for offset in range(8, fanout_end, 4)
        ]
        if any(left > right for left, right in zip(fanout, fanout[1:])):
            raise _fail("GIT_PACK_INDEX_INVALID")
        count = fanout[-1]
        if count > MAX_GIT_PACK_OBJECTS:
            raise _fail("GIT_PACK_INDEX_INVALID")
        object_ids_start = fanout_end
        crc_start = object_ids_start + count * digest_size
        offsets_start = crc_start + count * 4
        large_start = offsets_start + count * 4
        if large_start + 2 * digest_size > len(payload):
            raise _fail("GIT_PACK_INDEX_INVALID")
        offset_words = [
            int.from_bytes(payload[position : position + 4], "big")
            for position in range(offsets_start, large_start, 4)
        ]
        large_count = sum(bool(word & 0x80000000) for word in offset_words)
        if large_start + large_count * 8 + 2 * digest_size != len(payload):
            raise _fail("GIT_PACK_INDEX_INVALID")
        large_offsets = [
            int.from_bytes(payload[position : position + 8], "big")
            for position in range(large_start, large_start + large_count * 8, 8)
        ]
        result: dict[str, int] = {}
        crc_values = [
            int.from_bytes(payload[position : position + 4], "big")
            for position in range(crc_start, offsets_start, 4)
        ]
        large_indices = [
            word & 0x7FFFFFFF for word in offset_words if word & 0x80000000
        ]
        if sorted(large_indices) != list(range(large_count)):
            raise _fail("GIT_PACK_INDEX_INVALID")
        previous = ""
        bucket_counts = [0] * 256
        offset_crcs: dict[int, int] = {}
        for index, word in enumerate(offset_words):
            oid_start = object_ids_start + index * digest_size
            object_id = payload[oid_start : oid_start + digest_size].hex()
            if object_id <= previous:
                raise _fail("GIT_PACK_INDEX_INVALID")
            previous = object_id
            bucket_counts[int(object_id[:2], 16)] += 1
            if word & 0x80000000:
                large_index = word & 0x7FFFFFFF
                if large_index >= len(large_offsets):
                    raise _fail("GIT_PACK_INDEX_INVALID")
                offset = large_offsets[large_index]
            else:
                offset = word
            if offset < 12 or object_id in result or offset in offset_crcs:
                raise _fail("GIT_PACK_INDEX_INVALID")
            result[object_id] = offset
            offset_crcs[offset] = crc_values[index]
        running = 0
        expected_fanout: list[int] = []
        for value in bucket_counts:
            running += value
            expected_fanout.append(running)
        if fanout != expected_fanout:
            raise _fail("GIT_PACK_INDEX_INVALID")
        return result, offset_crcs

    def _read_pack_entry(
        self, pack: GitPack, entry_offset: int, stack: tuple[str, ...]
    ) -> GitObject:
        cache_key = (pack.name, entry_offset)
        cached = self.pack_objects.get(cache_key)
        if cached is not None:
            return cached
        if len(stack) >= 64:
            raise _fail("GIT_OBJECT_CYCLE")
        algorithm = _object_algorithm(next(iter(pack.object_offsets)))
        digest_size = hashlib.new(algorithm).digest_size
        limit = len(pack.payload) - digest_size
        if entry_offset < 12 or entry_offset >= limit:
            raise _fail("GIT_PACK_INVALID")
        position = entry_offset
        first = pack.payload[position]
        position += 1
        object_type_id = (first >> 4) & 0x07
        declared_size = first & 0x0F
        shift = 4
        current = first
        while current & 0x80:
            if position >= limit or shift > 63:
                raise _fail("GIT_PACK_INVALID")
            current = pack.payload[position]
            position += 1
            declared_size |= (current & 0x7F) << shift
            shift += 7
        if declared_size > MAX_GIT_OBJECT_BYTES:
            raise _fail("GIT_PACK_INVALID")

        base_offset: int | None = None
        base_object_id: str | None = None
        if object_type_id == 6:
            if position >= limit:
                raise _fail("GIT_PACK_INVALID")
            current = pack.payload[position]
            position += 1
            distance = current & 0x7F
            distance_bytes = 1
            while current & 0x80:
                if position >= limit or distance_bytes >= 10:
                    raise _fail("GIT_PACK_INVALID")
                current = pack.payload[position]
                position += 1
                distance_bytes += 1
                distance = ((distance + 1) << 7) | (current & 0x7F)
                if distance > entry_offset - 12:
                    raise _fail("GIT_PACK_INVALID")
            base_offset = entry_offset - distance
            if base_offset < 12 or base_offset not in pack.offset_objects:
                raise _fail("GIT_PACK_INVALID")
        elif object_type_id == 7:
            if position + digest_size > limit:
                raise _fail("GIT_PACK_INVALID")
            base_object_id = pack.payload[position : position + digest_size].hex()
            position += digest_size

        expected_end = pack.entry_ends.get(entry_offset)
        if expected_end is None or not position < expected_end <= limit:
            raise _fail("GIT_PACK_INVALID")
        try:
            inflater = zlib.decompressobj()
            compressed = memoryview(pack.payload)[position:expected_end]
            inflated = inflater.decompress(compressed, MAX_GIT_OBJECT_BYTES + 1)
        except zlib.error as exc:
            raise _fail("GIT_PACK_INVALID") from exc
        if (
            len(inflated) > MAX_GIT_OBJECT_BYTES
            or not inflater.eof
            or inflater.unconsumed_tail
            or inflater.unused_data
            or len(inflated) != declared_size
        ):
            raise _fail("GIT_PACK_INVALID")
        inflated += inflater.flush()
        if (
            zlib.crc32(memoryview(pack.payload)[entry_offset:expected_end])
            != pack.entry_crcs.get(entry_offset)
        ):
            raise _fail("GIT_PACK_INVALID")

        object_types = {1: "commit", 2: "tree", 3: "blob", 4: "tag"}
        if object_type_id in object_types:
            value = GitObject(object_types[object_type_id], inflated)
        elif base_offset is not None:
            base = self._read_pack_entry(pack, base_offset, (*stack, str(entry_offset)))
            value = GitObject(base.object_type, _apply_git_delta(base.payload, inflated))
        elif base_object_id is not None:
            base_entry_offset = pack.object_offsets.get(base_object_id)
            if base_entry_offset is None:
                raise _fail("GIT_PACK_THIN")
            base = self._read_pack_entry(
                pack, base_entry_offset, (*stack, str(entry_offset))
            )
            value = GitObject(base.object_type, _apply_git_delta(base.payload, inflated))
        else:
            raise _fail("GIT_PACK_INVALID")

        expected = pack.offset_objects.get(entry_offset)
        if expected is not None and _hash_git_object(
            value.object_type, value.payload, algorithm
        ) != expected:
            raise _fail("GIT_OBJECT_INVALID")
        self.pack_objects[cache_key] = value
        return value


def _read_optional_repository_file(root: Path, rel: str) -> bytes | None:
    try:
        payload, _ = _stable_read(root, rel, max_bytes=16 * 1024 * 1024)
        return payload
    except ClosePackError as exc:
        if str(exc) == "INPUT_MISSING":
            return None
        raise _fail("GIT_CONTROL_STATE_UNAVAILABLE") from exc


def _is_per_worktree_ref(ref: str) -> bool:
    return ref.startswith(("refs/bisect/", "refs/rewritten/", "refs/worktree/"))


def _canonical_git_ref(raw: str) -> str:
    try:
        encoded = raw.encode("ascii")
    except UnicodeEncodeError as exc:
        raise _fail("GIT_HEAD_UNAVAILABLE") from exc
    forbidden = b" ~^:?*[\\"
    components = raw.split("/")
    if (
        not raw.startswith("refs/")
        or raw == "@"
        or raw.endswith(("/", "."))
        or b"@{" in encoded
        or b".." in encoded
        or any(byte < 0x20 or byte == 0x7F or byte in forbidden for byte in encoded)
        or any(
            not component
            or component.startswith(".")
            or component.endswith(".lock")
            for component in components
        )
    ):
        raise _fail("GIT_HEAD_UNAVAILABLE")
    return raw


def _packed_ref_oid(context: GitContext, ref: str) -> str:
    packed = _read_optional_repository_file(context.common_dir, "packed-refs")
    if packed is None:
        raise _fail("GIT_HEAD_UNAVAILABLE")
    matches: list[str] = []
    seen_refs: set[str] = set()
    expected_algorithm: str | None = None
    previous_ref: str | None = None
    previous_entry_ref: str | None = None
    previous_was_peeled = False
    advertised_sorted = False
    try:
        for line_number, line in enumerate(packed.decode("ascii").splitlines()):
            if not line:
                continue
            if line.startswith("#"):
                if line_number == 0 and line.startswith("# pack-refs with:"):
                    features = set(line.partition(":")[2].split())
                    if features - {"peeled", "fully-peeled", "sorted"}:
                        raise _fail("GIT_HEAD_UNAVAILABLE")
                    advertised_sorted = "sorted" in features
                continue
            if line.startswith("^"):
                peeled = line[1:].lower()
                algorithm = _object_algorithm(peeled)
                if (
                    previous_entry_ref is None
                    or previous_was_peeled
                    or (expected_algorithm is not None and algorithm != expected_algorithm)
                ):
                    raise _fail("GIT_HEAD_UNAVAILABLE")
                expected_algorithm = algorithm
                previous_was_peeled = True
                continue
            object_id, packed_ref = line.split(" ", 1)
            packed_ref = _canonical_git_ref(packed_ref)
            object_id = object_id.lower()
            algorithm = _object_algorithm(object_id)
            if (
                packed_ref in seen_refs
                or _is_per_worktree_ref(packed_ref)
                or (expected_algorithm is not None and algorithm != expected_algorithm)
                or (
                    advertised_sorted
                    and previous_ref is not None
                    and packed_ref.encode("ascii") <= previous_ref.encode("ascii")
                )
            ):
                raise _fail("GIT_HEAD_UNAVAILABLE")
            expected_algorithm = algorithm
            seen_refs.add(packed_ref)
            previous_ref = packed_ref
            previous_entry_ref = packed_ref
            previous_was_peeled = False
            if packed_ref == ref:
                matches.append(object_id)
    except (ClosePackError, UnicodeDecodeError, ValueError) as exc:
        raise _fail("GIT_HEAD_UNAVAILABLE") from exc
    if len(matches) != 1:
        raise _fail("GIT_HEAD_UNAVAILABLE")
    return matches[0]


def _resolve_head_oid(
    context: GitContext, observed_paths: set[Path] | None = None
) -> str:
    try:
        payload, _ = _stable_absolute_read(
            context.git_dir / "HEAD", max_bytes=1024 * 1024
        )
        lines = payload.decode("ascii").splitlines()
    except (ClosePackError, UnicodeDecodeError) as exc:
        raise _fail("GIT_HEAD_UNAVAILABLE") from exc
    if len(lines) != 1 or not lines[0]:
        raise _fail("GIT_HEAD_UNAVAILABLE")
    value = lines[0]
    seen: set[str] = set()
    for _ in range(MAX_GIT_REFERENCE_DEPTH):
        if not value.startswith("ref: "):
            break
        ref = _canonical_git_ref(value[5:])
        if ref in seen:
            raise _fail("GIT_HEAD_UNAVAILABLE")
        seen.add(ref)
        per_worktree = _is_per_worktree_ref(ref)
        ref_root = context.git_dir if per_worktree else context.common_dir
        if observed_paths is not None:
            observed_paths.add(ref_root / ref)
        loose = _read_optional_repository_file(ref_root, ref)
        if loose is not None:
            try:
                ref_lines = loose.decode("ascii").splitlines()
            except UnicodeDecodeError as exc:
                raise _fail("GIT_HEAD_UNAVAILABLE") from exc
            if len(ref_lines) != 1:
                raise _fail("GIT_HEAD_UNAVAILABLE")
            value = ref_lines[0]
        else:
            if per_worktree:
                raise _fail("GIT_HEAD_UNAVAILABLE")
            if observed_paths is not None:
                observed_paths.add(context.common_dir / "packed-refs")
            value = _packed_ref_oid(context, ref)
    else:
        raise _fail("GIT_HEAD_UNAVAILABLE")
    value = value.lower()
    _object_algorithm(value)
    return value


def _validate_repository_config(context: GitContext, algorithm: str) -> None:
    try:
        payload, _ = _stable_absolute_read(
            context.common_dir / "config", max_bytes=16 * 1024 * 1024
        )
        if any(byte < 0x20 and byte not in {0x09, 0x0A} for byte in payload) or any(
            byte == 0x7F for byte in payload
        ):
            raise _fail("GIT_CONFIG_UNSUPPORTED")
        text = payload.decode("utf-8")
    except (ClosePackError, UnicodeDecodeError) as exc:
        raise _fail("GIT_CONFIG_INVALID") from exc
    section = ""
    repository_format: str | None = None
    extensions: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", ";")):
            continue
        if line.endswith("\\"):
            raise _fail("GIT_CONFIG_UNSUPPORTED")
        if line.startswith("["):
            if not line.endswith("]"):
                raise _fail("GIT_CONFIG_INVALID")
            declaration = line[1:-1].strip()
            if "\\" in declaration:
                raise _fail("GIT_CONFIG_UNSUPPORTED")
            match = re.fullmatch(
                r'([A-Za-z0-9.-]+)(?:\s+"([^"\\]*)")?', declaration
            )
            if match is None:
                raise _fail("GIT_CONFIG_UNSUPPORTED")
            section = match.group(1).casefold()
            subsection = match.group(2)
            if section in {"include", "includeif"}:
                raise _fail("GIT_CONFIG_EXTERNAL_INCLUDE")
            if section.startswith(("extensions.", "core.")) or (
                section in {"extensions", "core"} and subsection is not None
            ):
                raise _fail("GIT_CONFIG_UNSUPPORTED")
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9-]*)(?:\s*=\s*(.*))?", line)
        if match is None or not section:
            raise _fail("GIT_CONFIG_INVALID")
        key = match.group(1).casefold()
        value = (match.group(2) if match.group(2) is not None else "true").strip()
        if any(character in value for character in ('"', "'", "\\", "#", ";")):
            raise _fail("GIT_CONFIG_UNSUPPORTED")
        if section == "core" and key == "repositoryformatversion":
            if repository_format is not None:
                raise _fail("GIT_CONFIG_INVALID")
            repository_format = value
        elif section == "core" and key == "bare" and value.casefold() not in {
            "false",
            "no",
            "off",
            "0",
        }:
            raise _fail("GIT_CONFIG_INVALID")
        elif section == "core" and key == "worktree":
            raise _fail("GIT_CONFIG_EXTERNAL_WORKTREE")
        elif section == "extensions":
            if key in extensions:
                raise _fail("GIT_CONFIG_INVALID")
            extensions[key] = value.casefold()
    if repository_format not in {"0", "1"}:
        raise _fail("GIT_CONFIG_UNSUPPORTED")
    if set(extensions) - {"objectformat"}:
        raise _fail("GIT_CONFIG_UNSUPPORTED")
    configured_algorithm = extensions.get("objectformat", "sha1")
    if configured_algorithm not in {"sha1", "sha256"}:
        raise _fail("GIT_CONFIG_UNSUPPORTED")
    if repository_format == "0" and extensions:
        raise _fail("GIT_CONFIG_UNSUPPORTED")
    if configured_algorithm != algorithm:
        raise _fail("GIT_OBJECT_FORMAT_MISMATCH")


def _peel_head_commit(store: _GitObjectStore, object_id: str) -> str:
    seen: set[str] = set()
    expected_type: str | None = None
    for _ in range(MAX_GIT_REFERENCE_DEPTH):
        if object_id in seen:
            raise _fail("GIT_HEAD_UNAVAILABLE")
        seen.add(object_id)
        value = store.read(object_id)
        if expected_type is not None and value.object_type != expected_type:
            raise _fail("GIT_HEAD_UNAVAILABLE")
        if value.object_type == "commit":
            return object_id
        if value.object_type != "tag":
            raise _fail("GIT_HEAD_UNAVAILABLE")
        header, separator, _message = value.payload.partition(b"\n\n")
        header_lines = header.split(b"\n")
        try:
            object_prefix, target = header_lines[0].split(b" ", 1)
            type_prefix, tagged_type = header_lines[1].split(b" ", 1)
            tag_prefix, tag_name = header_lines[2].split(b" ", 1)
            object_id = target.decode("ascii").lower()
            expected_type = tagged_type.decode("ascii")
        except (IndexError, UnicodeDecodeError, ValueError) as exc:
            raise _fail("GIT_HEAD_UNAVAILABLE") from exc
        if (
            not separator
            or object_prefix != b"object"
            or type_prefix != b"type"
            or tag_prefix != b"tag"
            or expected_type not in {"commit", "tag"}
            or not tag_name
            or any(not line for line in header_lines[:3])
        ):
            raise _fail("GIT_HEAD_UNAVAILABLE")
        if (
            store.algorithm is not None
            and _object_algorithm(object_id) != store.algorithm
        ):
            raise _fail("GIT_OBJECT_FORMAT_MISMATCH")
    raise _fail("GIT_HEAD_UNAVAILABLE")


def _git_blob_payload(
    context: GitContext, object_id: str, store: _GitObjectStore | None = None
) -> bytes:
    reader = store or _GitObjectStore(context)
    value = reader.read(object_id)
    if value.object_type != "blob":
        raise _fail("GIT_OBJECT_TYPE_INVALID")
    return value.payload


def _tree_entries_from_store(
    context: GitContext, store: _GitObjectStore
) -> dict[str, GitTreeEntry]:
    head = _head(context, store)
    commit = store.read(head)
    if commit.object_type != "commit":
        raise _fail("GIT_HEAD_UNAVAILABLE")
    first_line = commit.payload.split(b"\n", 1)[0]
    try:
        prefix, tree_id_bytes = first_line.split(b" ", 1)
        tree_id = tree_id_bytes.decode("ascii")
    except (UnicodeDecodeError, ValueError) as exc:
        raise _fail("GIT_TREE_INVALID") from exc
    if prefix != b"tree" or len(tree_id) != len(head):
        raise _fail("GIT_TREE_INVALID")

    entries: dict[str, GitTreeEntry] = {}
    visiting: set[str] = set()
    parsed_entries = 0

    def visit(object_id: str, parent: PurePosixPath, depth: int) -> None:
        nonlocal parsed_entries
        if object_id in visiting or depth > MAX_GIT_TREE_DEPTH:
            raise _fail("GIT_TREE_INVALID")
        visiting.add(object_id)
        value = store.read(object_id)
        if value.object_type != "tree":
            raise _fail("GIT_TREE_INVALID")
        offset = 0
        digest_size = hashlib.new(_object_algorithm(object_id)).digest_size
        names: set[bytes] = set()
        previous_sort_key: bytes | None = None
        while offset < len(value.payload):
            parsed_entries += 1
            if parsed_entries > MAX_GIT_TREE_ENTRIES:
                raise _fail("GIT_TREE_INVALID")
            separator = value.payload.find(b" ", offset)
            terminator = value.payload.find(b"\0", separator + 1)
            if separator < 0 or terminator < 0 or terminator + 1 + digest_size > len(
                value.payload
            ):
                raise _fail("GIT_TREE_INVALID")
            try:
                mode = value.payload[offset:separator].decode("ascii")
                name_bytes = value.payload[separator + 1 : terminator]
                name = os.fsdecode(name_bytes)
            except UnicodeDecodeError as exc:
                raise _fail("GIT_TREE_INVALID") from exc
            child_id = value.payload[
                terminator + 1 : terminator + 1 + digest_size
            ].hex()
            offset = terminator + 1 + digest_size
            if (
                not name
                or "/" in name
                or name in {".", ".."}
                or name_bytes in names
            ):
                raise _fail("GIT_TREE_INVALID")
            names.add(name_bytes)
            is_tree = mode == "40000"
            sort_key = name_bytes + (b"/" if is_tree else b"\0")
            if previous_sort_key is not None and sort_key <= previous_sort_key:
                raise _fail("GIT_TREE_INVALID")
            previous_sort_key = sort_key
            path = (parent / name).as_posix()
            if len(os.fsencode(path)) > 4096:
                raise _fail("GIT_TREE_INVALID")
            if mode == "40000":
                visit(child_id, PurePosixPath(path), depth + 1)
            else:
                if mode in {"100644", "100755", "120000"}:
                    object_type = "blob"
                elif mode == "160000":
                    object_type = "commit"
                else:
                    raise _fail("GIT_TREE_INVALID")
                if path in entries:
                    raise _fail("GIT_TREE_AMBIGUOUS")
                entries[path] = GitTreeEntry(mode, object_type, child_id)
        visiting.remove(object_id)

    visit(tree_id, PurePosixPath(), 0)
    return entries


def _capture_input(
    root: Path,
    context: GitContext,
    store: _GitObjectStore,
    tree: Mapping[str, GitTreeEntry],
    rel: str,
    *,
    max_bytes: int = MAX_WORKTREE_FILE_BYTES,
) -> FileSnapshot:
    entry = _require_tracked_regular(tree, rel)
    payload, fingerprint = _stable_read(root, rel, max_bytes=max_bytes)
    if not payload:
        raise _fail("INPUT_EMPTY")
    head_payload = _git_blob_payload(context, entry.object_id, store)
    if payload != head_payload:
        raise _fail("INPUT_HEAD_MISMATCH")
    return FileSnapshot(rel, entry.object_id, payload, fingerprint)


def _strict_json(payload: bytes, *, code: str) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise _fail(code)
            result[key] = value
        return result

    try:
        text = payload.decode("utf-8")
        if text.startswith("\ufeff"):
            raise _fail(code)
        return json.loads(text, object_pairs_hook=reject_duplicates)
    except ClosePackError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise _fail(code) from exc


def _validate_schema(schema: Any) -> Mapping[str, Any]:
    if Draft202012Validator is None:
        raise _fail("JSONSCHEMA_DEPENDENCY_UNAVAILABLE")
    if not isinstance(schema, dict):
        raise _fail("SCHEMA_INVALID")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise _fail("SCHEMA_INVALID")
    if schema.get("$id") != SCHEMA_REL:
        raise _fail("SCHEMA_INVALID")
    references: list[str] = []
    pending: list[tuple[Any, bool]] = [(schema, True)]
    while pending:
        node, is_root = pending.pop()
        if isinstance(node, dict):
            if not is_root and "$id" in node:
                raise _fail("SCHEMA_INVALID")
            for keyword in ("$ref", "$dynamicRef", "$recursiveRef"):
                if keyword not in node:
                    continue
                reference = node[keyword]
                if (
                    not isinstance(reference, str)
                    or not reference.startswith("#/$defs/")
                ):
                    raise _fail("SCHEMA_INVALID")
                references.append(reference)
            pending.extend((value, False) for value in node.values())
        elif isinstance(node, list):
            pending.extend((value, False) for value in node)
    for reference in references:
        target: Any = schema
        try:
            for encoded in reference[2:].split("/"):
                token = encoded.replace("~1", "/").replace("~0", "~")
                if not isinstance(target, dict) or token not in target:
                    raise KeyError(token)
                target = target[token]
        except (KeyError, TypeError) as exc:
            raise _fail("SCHEMA_INVALID") from exc
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise _fail("SCHEMA_INVALID") from exc
    return schema


def _validate_source(source: Any, schema: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(source, dict):
        raise _fail("SOURCE_SCHEMA_INVALID")
    try:
        errors = sorted(
            Draft202012Validator(schema).iter_errors(source),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
    except Exception as exc:
        raise _fail("SOURCE_SCHEMA_INVALID") from exc
    if errors:
        raise _fail("SOURCE_SCHEMA_INVALID")
    return source


def _require_feedback_free_source(
    source: Mapping[str, Any], source_rel: str, head: str
) -> None:
    causal_values = [source_rel, str(source["plan_path"])]
    for item in source["evidence_inputs"]:
        causal_values.extend((str(item["binding"]), str(item["path"])))
    for section in source["report_sections"]:
        causal_values.append(str(section["heading"]))
        causal_values.extend(str(line) for line in section["body_lines"])
    for value in causal_values:
        if (
            value.casefold().startswith("catalog/manifest.json")
            or head.casefold() in value.casefold()
            or FEEDBACK_DEPENDENCY_RE.search(value) is not None
        ):
            raise _fail("FEEDBACK_DEPENDENCY_PROHIBITED")


def _normalized_report_heading(value: str) -> str:
    return re.sub(r"[ \t]+", " ", value.strip(" \t")).casefold()


def _report_body_structure_is_ambiguous(lines: Sequence[str]) -> bool:
    return any(REPORT_BODY_PROHIBITED_RE.search(line) is not None for line in lines)


def _require_report_structure(source: Mapping[str, Any]) -> None:
    raw_headings = [str(section["heading"]) for section in source["report_sections"]]
    headings = [
        _normalized_report_heading(heading) for heading in raw_headings
    ]
    ambiguous_body_structure = any(
        _report_body_structure_is_ambiguous(
            [str(line) for line in section["body_lines"]]
        )
        for section in source["report_sections"]
    )
    if (
        len(headings) != len(set(headings))
        or any(heading in RESERVED_HEADINGS for heading in headings)
        or any(REPORT_HEADING_RE.fullmatch(heading) is None for heading in raw_headings)
        or ambiguous_body_structure
    ):
        raise _fail("REPORT_SECTION_AMBIGUOUS")


def _derived_paths(epic_id: str) -> tuple[str, str]:
    match = EPIC_RE.fullmatch(epic_id)
    if match is None:
        raise _fail("EPIC_ID_INVALID")
    number = match.group("number")
    return (
        f"audit/EPIC-{number}_close_report.md",
        f"audit/EPIC-{number}_MANIFEST.json",
    )


def _load_model(
    root: Path,
    context: GitContext,
    head: str,
    source_rel: str,
) -> tuple[CandidateModel, tuple[FileSnapshot, ...]]:
    store = _GitObjectStore(context)
    tree = _tree_entries(context, store)
    remaining_input_bytes = MAX_CAUSAL_INPUT_BYTES
    schema_input = _capture_input(
        root, context, store, tree, SCHEMA_REL, max_bytes=remaining_input_bytes
    )
    remaining_input_bytes -= len(schema_input.payload)
    source_input = _capture_input(
        root, context, store, tree, source_rel, max_bytes=remaining_input_bytes
    )
    remaining_input_bytes -= len(source_input.payload)
    schema = _validate_schema(_strict_json(schema_input.payload, code="SCHEMA_JSON_INVALID"))
    source = _validate_source(
        _strict_json(source_input.payload, code="SOURCE_JSON_INVALID"), schema
    )
    if source.get("schema_version") != SOURCE_SCHEMA_VERSION:
        raise _fail("SOURCE_SCHEMA_INVALID")
    _require_feedback_free_source(source, source_rel, head)
    if set(source["nonclaims"]) != set(NONCLAIM_TEXT):
        raise _fail("SOURCE_SCHEMA_INVALID")

    report_path, manifest_path = _derived_paths(str(source["epic_id"]))
    outputs = source["key_outputs"]
    if outputs != {
        "close_manifest": manifest_path,
        "close_report": report_path,
    }:
        raise _fail("OUTPUT_BINDING_MISMATCH")

    _require_report_structure(source)

    plan_rel = _canonical_relative_path(source["plan_path"])
    plan_input = _capture_input(
        root, context, store, tree, plan_rel, max_bytes=remaining_input_bytes
    )
    remaining_input_bytes -= len(plan_input.payload)
    evidence: list[tuple[str, FileSnapshot]] = []
    bindings: set[str] = set()
    evidence_paths: set[str] = set()
    for item in source["evidence_inputs"]:
        binding = item["binding"]
        rel = _canonical_relative_path(item["path"])
        if binding in bindings or rel in evidence_paths:
            raise _fail("EVIDENCE_BINDING_AMBIGUOUS")
        bindings.add(binding)
        evidence_paths.add(rel)
        snapshot = _capture_input(
            root, context, store, tree, rel, max_bytes=remaining_input_bytes
        )
        remaining_input_bytes -= len(snapshot.payload)
        evidence.append((binding, snapshot))

    causal_paths = {
        SCHEMA_REL,
        source_rel,
        plan_rel,
        *(snapshot.rel for _, snapshot in evidence),
    }
    if len(causal_paths) != 3 + len(evidence):
        raise _fail("INPUT_COLLISION")
    if report_path in causal_paths or manifest_path in causal_paths:
        raise _fail("OUTPUT_COLLISION")
    if report_path == manifest_path:
        raise _fail("OUTPUT_COLLISION")

    if _head(context, store) != head:
        raise _fail("GIT_HEAD_CHANGED")
    model = CandidateModel(
        source=source,
        source_path=source_rel,
        source_input=source_input,
        schema_input=schema_input,
        plan_input=plan_input,
        evidence_inputs=tuple(sorted(evidence, key=lambda item: (item[0], item[1].rel))),
        report_path=report_path,
        manifest_path=manifest_path,
    )
    snapshots = (
        schema_input,
        source_input,
        plan_input,
        *(snapshot for _, snapshot in model.evidence_inputs),
    )
    return model, snapshots


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _binding(snapshot: FileSnapshot) -> dict[str, object]:
    return {
        "path": snapshot.rel,
        "sha256": _sha256(snapshot.payload),
        "size_bytes": len(snapshot.payload),
    }


def _canonical_json(payload: object) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")


def _render_candidate(model: CandidateModel) -> dict[str, bytes]:
    source = model.source
    lines = [
        f"# {source['epic_id']} Close Candidate",
        "",
        "This deterministic candidate is derived only from exact tracked repository inputs.",
        "",
        "## Source bindings",
        "",
    ]
    named_inputs = [
        ("Candidate source", model.source_input),
        ("Candidate-source schema", model.schema_input),
        ("Plan", model.plan_input),
    ]
    for label, snapshot in named_inputs:
        lines.append(
            f"- {label}: `{snapshot.rel}` "
            f"(`sha256={_sha256(snapshot.payload)}`, `size_bytes={len(snapshot.payload)}`)"
        )
    for binding, snapshot in model.evidence_inputs:
        lines.append(
            f"- Evidence `{binding}`: `{snapshot.rel}` "
            f"(`sha256={_sha256(snapshot.payload)}`, `size_bytes={len(snapshot.payload)}`)"
        )

    for section in source["report_sections"]:
        lines.extend(("", f"## {section['heading']}", ""))
        lines.extend(section["body_lines"])

    lines.extend(
        (
            "",
            "## Output bindings",
            "",
            f"- Close report: `{model.report_path}`",
            f"- Close manifest: `{model.manifest_path}`",
            "",
            "## Explicit nonclaims",
            "",
        )
    )
    nonclaim_codes = sorted(source["nonclaims"])
    lines.extend(f"- {NONCLAIM_TEXT[code]}" for code in nonclaim_codes)
    report = ("\n".join(lines) + "\n").encode("utf-8")

    manifest = {
        "candidate_posture": "candidate_only",
        "epic_id": source["epic_id"],
        "inputs": {
            "candidate_source": _binding(model.source_input),
            "evidence": [
                {"binding": binding, **_binding(snapshot)}
                for binding, snapshot in model.evidence_inputs
            ],
            "plan": _binding(model.plan_input),
            "schema": _binding(model.schema_input),
        },
        "nonclaims": [
            {"code": code, "statement": NONCLAIM_TEXT[code]}
            for code in nonclaim_codes
        ],
        "outputs": {
            "close_manifest": {"path": model.manifest_path},
            "close_report": {
                "path": model.report_path,
                "sha256": _sha256(report),
                "size_bytes": len(report),
            },
        },
        "schema_version": MANIFEST_SCHEMA_VERSION,
    }
    return {
        model.manifest_path: _canonical_json(manifest),
        model.report_path: report,
    }


def _verify_snapshots(
    root: Path,
    context: GitContext,
    head: str,
    snapshots: Sequence[FileSnapshot],
) -> None:
    store = _GitObjectStore(context)
    if _head(context, store) != head:
        raise _fail("GIT_HEAD_CHANGED")
    tree = _tree_entries(context, store)
    for snapshot in snapshots:
        entry = _require_tracked_regular(tree, snapshot.rel)
        payload, fingerprint = _stable_read(
            root, snapshot.rel, max_bytes=MAX_WORKTREE_FILE_BYTES
        )
        if (
            entry.object_id != snapshot.object_id
            or payload != snapshot.payload
            or fingerprint != snapshot.fingerprint
        ):
            raise _fail("INPUT_CHANGED")
        if payload != _git_blob_payload(context, entry.object_id, store):
            raise _fail("INPUT_HEAD_MISMATCH")
    if _head(context, store) != head:
        raise _fail("GIT_HEAD_CHANGED")


def _repository_metadata(
    root: Path,
) -> dict[str, tuple[int, int, int, int, int, int, int]]:
    result: dict[str, tuple[int, int, int, int, int, int, int]] = {}

    def record(rel: str, metadata: os.stat_result) -> None:
        result[rel] = (
            metadata.st_mode,
            metadata.st_size,
            metadata.st_atime_ns,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
            metadata.st_dev,
            metadata.st_ino,
        )

    def walk(directory: Path, prefix: PurePosixPath) -> None:
        nofollow = getattr(os, "O_NOFOLLOW", 0)
        directory_flag = getattr(os, "O_DIRECTORY", 0)
        noatime = getattr(os, "O_NOATIME", 0)
        if not nofollow or not directory_flag or not noatime:
            raise _fail("NOFOLLOW_UNAVAILABLE")
        try:
            directory_fd = os.open(
                directory,
                os.O_RDONLY | directory_flag | nofollow | noatime,
            )
        except OSError as exc:
            raise _fail("REPOSITORY_METADATA_UNAVAILABLE") from exc
        try:
            entries = sorted(
                (
                    (
                        name,
                        os.stat(name, dir_fd=directory_fd, follow_symlinks=False),
                    )
                    for name in os.listdir(directory_fd)
                ),
                key=lambda item: item[0],
            )
        except OSError as exc:
            raise _fail("REPOSITORY_METADATA_UNAVAILABLE") from exc
        finally:
            os.close(directory_fd)
        for name, metadata in entries:
            if not prefix.parts and name == ".git":
                continue
            rel = prefix / name
            record(rel.as_posix(), metadata)
            if stat.S_ISDIR(metadata.st_mode):
                walk(directory / name, rel)

    record(".", root.stat())
    walk(root, PurePosixPath())
    return result


def _metadata_matches_with_symlink_atime_exemption(
    before: Mapping[str, tuple[int, int, int, int, int, int, int]],
    after: Mapping[str, tuple[int, int, int, int, int, int, int]],
    tree: Mapping[str, GitTreeEntry],
) -> bool:
    if set(before) != set(after):
        return False
    for rel, prior in before.items():
        current = after[rel]
        if current == prior:
            continue
        entry = tree.get(rel)
        if (
            entry is None
            or entry.mode != "120000"
            or current[2] < prior[2]
            or prior[:2] + prior[3:] != current[:2] + current[3:]
        ):
            return False
    return True


def _git_blob_id(payload: bytes, algorithm: str) -> str:
    try:
        digest = hashlib.new(algorithm)
    except ValueError as exc:
        raise _fail("GIT_OBJECT_FORMAT_UNSUPPORTED") from exc
    digest.update(f"blob {len(payload)}\0".encode("ascii"))
    digest.update(payload)
    return digest.hexdigest()


def _index_entries(context: GitContext, algorithm: str) -> dict[str, GitIndexEntry]:
    index_path = context.git_dir / "index"
    payload, _ = _stable_absolute_read(index_path, max_bytes=MAX_GIT_PACK_BYTES)
    digest_size = hashlib.new(algorithm).digest_size
    if len(payload) < 12 + digest_size or payload[:4] != b"DIRC":
        raise _fail("GIT_INDEX_INVALID")
    content, checksum = payload[:-digest_size], payload[-digest_size:]
    if hashlib.new(algorithm, content).digest() != checksum:
        raise _fail("GIT_INDEX_INVALID")
    version, count = struct.unpack(">II", content[4:12])
    if version not in {2, 3}:
        raise _fail("GIT_INDEX_UNSUPPORTED")

    entries: dict[str, GitIndexEntry] = {}
    offset = 12
    previous_path_bytes: bytes | None = None
    try:
        for _ in range(count):
            start = offset
            fixed_size = 40 + digest_size + 2
            if offset + fixed_size > len(content):
                raise _fail("GIT_INDEX_INVALID")
            cached = struct.unpack(">10I", content[offset : offset + 40])
            offset += 40
            object_id = content[offset : offset + digest_size].hex()
            offset += digest_size
            flags = struct.unpack(">H", content[offset : offset + 2])[0]
            offset += 2
            if flags & 0x3000 or flags & 0x8000:
                raise _fail("GIT_INDEX_DIRTY")
            if flags & 0x4000:
                if version < 3 or offset + 2 > len(content):
                    raise _fail("GIT_INDEX_INVALID")
                extended_flags = struct.unpack(">H", content[offset : offset + 2])[0]
                offset += 2
                if extended_flags:
                    raise _fail("GIT_INDEX_DIRTY")
            declared_length = flags & 0x0FFF
            terminator = content.find(b"\0", offset)
            if terminator < 0:
                raise _fail("GIT_INDEX_INVALID")
            path_bytes = content[offset:terminator]
            if declared_length != min(len(path_bytes), 0x0FFF):
                raise _fail("GIT_INDEX_INVALID")
            if previous_path_bytes is not None and path_bytes <= previous_path_bytes:
                raise _fail("GIT_INDEX_INVALID")
            previous_path_bytes = path_bytes
            path = os.fsdecode(path_bytes)
            entry_end = terminator + 1
            padding = (8 - ((entry_end - start) % 8)) % 8
            if any(content[entry_end : entry_end + padding]):
                raise _fail("GIT_INDEX_INVALID")
            offset = entry_end + padding
            if path in entries or not path:
                raise _fail("GIT_INDEX_INVALID")
            mode = f"{cached[6]:o}"
            entries[path] = GitIndexEntry(
                mode=mode,
                object_id=object_id,
                ctime_seconds=cached[0],
                ctime_nanoseconds=cached[1],
                mtime_seconds=cached[2],
                mtime_nanoseconds=cached[3],
                device=cached[4],
                inode=cached[5],
                uid=cached[7],
                gid=cached[8],
                size=cached[9],
            )
    except (UnicodeDecodeError, struct.error, ValueError) as exc:
        raise _fail("GIT_INDEX_INVALID") from exc
    while offset < len(content):
        if offset + 8 > len(content):
            raise _fail("GIT_INDEX_INVALID")
        signature = content[offset : offset + 4]
        extension_size = int.from_bytes(content[offset + 4 : offset + 8], "big")
        offset += 8
        extension_end = offset + extension_size
        if (
            extension_end > len(content)
            or len(signature) != 4
            or not 65 <= signature[0] <= 90
        ):
            raise _fail("GIT_INDEX_UNSUPPORTED")
        offset = extension_end
    if offset != len(content):
        raise _fail("GIT_INDEX_INVALID")
    return entries


def _worktree_changes(root: Path, context: GitContext) -> set[str]:
    store = _GitObjectStore(context)
    head = _head(context, store)
    tree = _tree_entries(context, store)
    try:
        algorithm = _object_algorithm(head)
        index = _index_entries(context, algorithm)
    except ClosePackError as exc:
        raise _fail("GIT_CLEAN_STATE_UNAVAILABLE") from exc
    if algorithm not in {"sha1", "sha256"}:
        raise _fail("GIT_OBJECT_FORMAT_UNSUPPORTED")

    metadata = _repository_metadata(root)
    file_paths = {
        rel
        for rel, values in metadata.items()
        if rel != "." and not stat.S_ISDIR(values[0])
    }
    directory_paths = {
        rel
        for rel, values in metadata.items()
        if rel != "." and stat.S_ISDIR(values[0])
    }
    tracked_directories = {
        PurePosixPath(path).parents[index].as_posix()
        for path in tree
        for index in range(len(PurePosixPath(path).parents) - 1)
    }
    tree_paths = set(tree)
    index_paths = set(index)
    changes = tree_paths ^ index_paths
    for rel in tree_paths & index_paths:
        entry = tree[rel]
        if (index[rel].mode, index[rel].object_id) != (entry.mode, entry.object_id):
            changes.add(rel)
    changes.update(file_paths - set(tree))
    changes.update(directory_paths - tracked_directories)
    for rel, entry in tree.items():
        values = metadata.get(rel)
        if values is None:
            changes.add(rel)
            continue
        mode = values[0]
        try:
            if entry.object_type != "blob":
                changes.add(rel)
            elif entry.mode in REGULAR_GIT_MODES and stat.S_ISREG(mode):
                payload, _ = _stable_read(
                    root, rel, max_bytes=MAX_WORKTREE_FILE_BYTES
                )
                worktree_mode = "100755" if stat.S_IMODE(mode) & 0o111 else "100644"
                if (
                    worktree_mode != entry.mode
                    or _git_blob_id(payload, algorithm) != entry.object_id
                ):
                    changes.add(rel)
            elif entry.mode == "120000" and stat.S_ISLNK(mode):
                target = _stable_symlink_read(root, rel)
                if _git_blob_id(target, algorithm) != entry.object_id:
                    changes.add(rel)
            else:
                changes.add(rel)
        except (ClosePackError, OSError):
            raise
    return changes


def _git_control_paths(context: GitContext) -> tuple[Path, ...]:
    _verify_git_context(context)
    git_dir = context.git_dir
    common_dir = context.common_dir
    paths = {
        git_dir / "HEAD",
        git_dir / "commondir",
        git_dir / "gitdir",
        git_dir / "index",
        git_dir / "logs/HEAD",
        common_dir / "config",
        common_dir / "packed-refs",
    }
    try:
        _resolve_head_oid(context, paths)
    except ClosePackError as exc:
        raise _fail("GIT_CONTROL_STATE_UNAVAILABLE") from exc
    return tuple(sorted(paths))


def _stable_absolute_read(
    path: Path, *, max_bytes: int | None = None
) -> tuple[bytes, os.stat_result]:
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if not nofollow or not noatime:
        raise _fail("NONWRITING_READ_UNAVAILABLE")
    try:
        descriptor = os.open(path, os.O_RDONLY | nofollow | noatime)
    except OSError as exc:
        raise _fail("GIT_CONTROL_STATE_UNAVAILABLE") from exc
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise _fail("GIT_CONTROL_STATE_UNAVAILABLE")
        if max_bytes is not None and before.st_size > max_bytes:
            raise _fail("GIT_CONTROL_STATE_UNAVAILABLE")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if max_bytes is not None and total > max_bytes:
                raise _fail("GIT_CONTROL_STATE_UNAVAILABLE")
            chunks.append(chunk)
        payload = b"".join(chunks)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    try:
        linked = path.lstat()
    except OSError as exc:
        raise _fail("GIT_CONTROL_STATE_UNAVAILABLE") from exc
    if (
        not stat.S_ISREG(linked.st_mode)
        or _fingerprint(before) != _fingerprint(after)
        or _fingerprint(after) != _fingerprint(linked)
        or len(payload) != after.st_size
    ):
        raise _fail("GIT_CONTROL_STATE_CHANGED")
    return payload, after


def _git_control_state(
    paths: Sequence[Path],
) -> dict[str, tuple[int, int, int, int, int, int, int, str] | None]:
    result: dict[str, tuple[int, int, int, int, int, int, int, str] | None] = {}
    for path in paths:
        try:
            metadata = path.lstat()
        except FileNotFoundError:
            result[str(path)] = None
            continue
        except OSError as exc:
            raise _fail("GIT_CONTROL_STATE_UNAVAILABLE") from exc
        if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
            raise _fail("GIT_CONTROL_STATE_UNAVAILABLE")
        payload, stable = _stable_absolute_read(path)
        result[str(path)] = (
            stable.st_mode,
            stable.st_size,
            stable.st_atime_ns,
            stable.st_mtime_ns,
            stable.st_ctime_ns,
            stable.st_dev,
            stable.st_ino,
            _sha256(payload),
        )
    return result


def _require_output_case_unambiguous(
    tree: Mapping[str, GitTreeEntry], rel: str
) -> None:
    aliases = [path for path in tree if path.casefold() == rel.casefold()]
    if any(path != rel for path in aliases):
        raise _fail("OUTPUT_CASE_AMBIGUOUS")


def _validate_output_target(root: Path, rel: str) -> OutputPreimage:
    _canonical_relative_path(rel, code="OUTPUT_PATH_INVALID")
    target = root / rel
    current = target.parent
    while current != root:
        try:
            metadata = current.lstat()
        except OSError as exc:
            raise _fail("OUTPUT_PARENT_UNAVAILABLE") from exc
        if not stat.S_ISDIR(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
            raise _fail("OUTPUT_PARENT_ALIASED")
        current = current.parent
    try:
        metadata = target.lstat()
    except FileNotFoundError:
        return OutputPreimage(False, b"", OUTPUT_MODE, 0, 0, None)
    except OSError as exc:
        raise _fail("OUTPUT_TARGET_UNAVAILABLE") from exc
    if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
        raise _fail("OUTPUT_TARGET_NOT_REGULAR")
    payload, fingerprint = _stable_read(root, rel, max_bytes=MAX_OUTPUT_BYTES)
    return OutputPreimage(
        True,
        payload,
        stat.S_IMODE(metadata.st_mode),
        metadata.st_atime_ns,
        metadata.st_mtime_ns,
        fingerprint,
    )


def _directory_case_matches(parent_fd: int, expected: str) -> list[str]:
    try:
        return sorted(
            name for name in os.listdir(parent_fd) if name.casefold() == expected.casefold()
        )
    except OSError as exc:
        raise _fail("OUTPUT_PARENT_UNAVAILABLE") from exc


def _stable_anchored_read(
    parent_fd: int, name: str, *, max_bytes: int = MAX_OUTPUT_BYTES
) -> tuple[bytes, os.stat_result]:
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if not nofollow or not noatime or os.open not in os.supports_dir_fd:
        raise _fail("NONWRITING_READ_UNAVAILABLE")
    try:
        descriptor = os.open(
            name,
            os.O_RDONLY | nofollow | noatime | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
    except OSError as exc:
        raise _fail("OUTPUT_TARGET_UNAVAILABLE") from exc
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise _fail("OUTPUT_TARGET_NOT_REGULAR")
        if before.st_size > max_bytes:
            raise _fail("OUTPUT_TOO_LARGE")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > max_bytes:
                raise _fail("OUTPUT_TOO_LARGE")
            chunks.append(chunk)
        payload = b"".join(chunks)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    try:
        linked = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as exc:
        raise _fail("OUTPUT_TARGET_UNAVAILABLE") from exc
    if (
        not stat.S_ISREG(linked.st_mode)
        or _fingerprint(before) != _fingerprint(after)
        or _fingerprint(after) != _fingerprint(linked)
        or len(payload) != after.st_size
    ):
        raise _fail("OUTPUT_TARGET_CHANGED")
    return payload, after


def _open_output_anchor(root: Path, rel: str) -> OutputAnchor:
    _canonical_relative_path(rel, code="OUTPUT_PATH_INVALID")
    parts = PurePosixPath(rel).parts
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory = getattr(os, "O_DIRECTORY", 0)
    noatime = getattr(os, "O_NOATIME", 0)
    if (
        not nofollow
        or not directory
        or not noatime
        or os.open not in os.supports_dir_fd
    ):
        raise _fail("NONWRITING_READ_UNAVAILABLE")
    descriptors: list[int] = []
    try:
        root_fd = os.open(root, os.O_RDONLY | directory | nofollow | noatime)
        descriptors.append(root_fd)
        parent_fd = root_fd
        for part in parts[:-1]:
            matches = _directory_case_matches(parent_fd, part)
            if matches != [part]:
                code = "OUTPUT_PARENT_UNAVAILABLE" if not matches else "OUTPUT_CASE_AMBIGUOUS"
                raise _fail(code)
            child_fd = os.open(
                part,
                os.O_RDONLY | directory | nofollow | noatime,
                dir_fd=parent_fd,
            )
            descriptors.append(child_fd)
            metadata = os.fstat(child_fd)
            if not stat.S_ISDIR(metadata.st_mode):
                raise _fail("OUTPUT_PARENT_ALIASED")
            parent_fd = child_fd

        name = parts[-1]
        target_matches = _directory_case_matches(parent_fd, name)
        if target_matches not in ([], [name]):
            raise _fail("OUTPUT_CASE_AMBIGUOUS")
        if target_matches:
            metadata = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
            if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
                raise _fail("OUTPUT_TARGET_NOT_REGULAR")
            payload, stable = _stable_anchored_read(parent_fd, name)
            preimage = OutputPreimage(
                True,
                payload,
                stat.S_IMODE(stable.st_mode),
                stable.st_atime_ns,
                stable.st_mtime_ns,
                _fingerprint(stable),
            )
        else:
            preimage = OutputPreimage(False, b"", OUTPUT_MODE, 0, 0, None)

        parent_metadata = os.fstat(parent_fd)
        retained_fd = os.dup(parent_fd)
        anchor = OutputAnchor(
            rel=rel,
            parent_path=root.joinpath(*parts[:-1]),
            parent_fd=retained_fd,
            parent_device=parent_metadata.st_dev,
            parent_inode=parent_metadata.st_ino,
            name=name,
            preimage=preimage,
        )
    except ClosePackError:
        raise
    except OSError as exc:
        raise _fail("OUTPUT_PARENT_UNAVAILABLE") from exc
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)
    return anchor


def _verify_anchor_parent(anchor: OutputAnchor) -> None:
    try:
        opened = os.fstat(anchor.parent_fd)
        current = anchor.parent_path.lstat()
    except OSError as exc:
        raise _fail("OUTPUT_PARENT_CHANGED") from exc
    if (
        not stat.S_ISDIR(opened.st_mode)
        or not stat.S_ISDIR(current.st_mode)
        or stat.S_ISLNK(current.st_mode)
        or (opened.st_dev, opened.st_ino)
        != (anchor.parent_device, anchor.parent_inode)
        or (current.st_dev, current.st_ino)
        != (anchor.parent_device, anchor.parent_inode)
    ):
        raise _fail("OUTPUT_PARENT_CHANGED")


def _require_anchor_preimage(anchor: OutputAnchor) -> None:
    _verify_anchor_parent(anchor)
    matches = _directory_case_matches(anchor.parent_fd, anchor.name)
    if not anchor.preimage.existed:
        if matches:
            raise _fail("OUTPUT_TARGET_CHANGED")
        return
    if matches != [anchor.name]:
        raise _fail("OUTPUT_TARGET_CHANGED")
    payload, metadata = _stable_anchored_read(anchor.parent_fd, anchor.name)
    if (
        payload != anchor.preimage.payload
        or _fingerprint(metadata) != anchor.preimage.fingerprint
        or metadata.st_atime_ns != anchor.preimage.atime_ns
    ):
        raise _fail("OUTPUT_TARGET_CHANGED")


def _write_temp(anchor: OutputAnchor, payload: bytes, mode: int) -> str:
    _verify_anchor_parent(anchor)
    descriptor: int | None = None
    temp_name = ""
    for _ in range(128):
        temp_name = f".{anchor.name}.epic-close-pack.{secrets.token_hex(16)}"
        try:
            descriptor = os.open(
                temp_name,
                os.O_WRONLY
                | os.O_CREAT
                | os.O_EXCL
                | getattr(os, "O_NOFOLLOW", 0),
                mode,
                dir_fd=anchor.parent_fd,
            )
            break
        except FileExistsError:
            continue
        except OSError as exc:
            raise _fail("OUTPUT_TEMP_UNAVAILABLE") from exc
    if descriptor is None:
        raise _fail("OUTPUT_TEMP_UNAVAILABLE")
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = None
            stream.write(payload)
            stream.flush()
            os.fchmod(stream.fileno(), mode)
            os.fsync(stream.fileno())
    except BaseException:
        try:
            os.unlink(temp_name, dir_fd=anchor.parent_fd)
        except FileNotFoundError:
            pass
        raise
    finally:
        if descriptor is not None:
            os.close(descriptor)
    return temp_name


def _rename_with_flags(
    source: str,
    target: str,
    parent_fd: int,
    flags: int,
) -> None:
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        renameat2 = libc.renameat2
    except (OSError, AttributeError) as exc:
        raise _fail("ATOMIC_RENAME_UNAVAILABLE") from exc
    renameat2.argtypes = (
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    )
    renameat2.restype = ctypes.c_int
    result = renameat2(
        parent_fd,
        os.fsencode(source),
        parent_fd,
        os.fsencode(target),
        flags,
    )
    if result != 0:
        error_number = ctypes.get_errno()
        if error_number in {errno.ENOSYS, errno.EINVAL, errno.ENOTSUP}:
            raise _fail("ATOMIC_RENAME_UNAVAILABLE")
        raise OSError(error_number, os.strerror(error_number), target)


def _unlink_anchored(anchor: OutputAnchor, name: str) -> None:
    try:
        os.unlink(name, dir_fd=anchor.parent_fd)
    except FileNotFoundError:
        pass


def _capture_staged_output(
    anchor: OutputAnchor,
    staged_name: str,
    expected: bytes,
    backup_name: str | None,
) -> InstalledOutput:
    _verify_anchor_parent(anchor)
    if _directory_case_matches(anchor.parent_fd, staged_name) != [staged_name]:
        raise _fail("OUTPUT_TARGET_CHANGED")
    payload, metadata = _stable_anchored_read(anchor.parent_fd, staged_name)
    if payload != expected or stat.S_IMODE(metadata.st_mode) != OUTPUT_MODE:
        raise _fail("OUTPUT_TARGET_CHANGED")
    return InstalledOutput(
        anchor=anchor,
        payload=payload,
        fingerprint=_fingerprint(metadata),
        atime_ns=metadata.st_atime_ns,
        backup_name=backup_name,
    )


def _require_named_state(
    anchor: OutputAnchor,
    name: str,
    payload_expected: bytes,
    fingerprint_expected: tuple[int, int, int, int, int, int],
    atime_ns_expected: int,
) -> None:
    payload, metadata = _stable_anchored_read(anchor.parent_fd, name)
    if (
        payload != payload_expected
        or _fingerprint(metadata)[:-1] != fingerprint_expected[:-1]
        or metadata.st_atime_ns != atime_ns_expected
    ):
        raise _fail("OUTPUT_TARGET_CHANGED")


def _install_staged_output(
    anchor: OutputAnchor,
    staged_name: str,
    expected: bytes,
    installed: list[InstalledOutput],
) -> None:
    _verify_anchor_parent(anchor)
    staged_output = _capture_staged_output(
        anchor,
        staged_name,
        expected,
        staged_name if anchor.preimage.existed else None,
    )
    if anchor.preimage.existed:
        _rename_with_flags(staged_name, anchor.name, anchor.parent_fd, RENAME_EXCHANGE)
        installed.append(staged_output)
        if anchor.preimage.fingerprint is None:
            raise _fail("OUTPUT_TARGET_CHANGED")
        _require_named_state(
            anchor,
            staged_name,
            anchor.preimage.payload,
            anchor.preimage.fingerprint,
            anchor.preimage.atime_ns,
        )
        return

    _rename_with_flags(staged_name, anchor.name, anchor.parent_fd, RENAME_NOREPLACE)
    installed.append(staged_output)


def _rollback_installed_output(installed: InstalledOutput, staged_name: str) -> None:
    anchor = installed.anchor
    _verify_anchor_parent(anchor)
    if installed.backup_name is not None:
        _rename_with_flags(
            installed.backup_name,
            anchor.name,
            anchor.parent_fd,
            RENAME_EXCHANGE,
        )
        try:
            _require_named_state(
                anchor,
                installed.backup_name,
                installed.payload,
                installed.fingerprint,
                installed.atime_ns,
            )
        except BaseException:
            _rename_with_flags(
                installed.backup_name,
                anchor.name,
                anchor.parent_fd,
                RENAME_EXCHANGE,
            )
            raise
        return

    _rename_with_flags(
        anchor.name,
        staged_name,
        anchor.parent_fd,
        RENAME_NOREPLACE,
    )
    try:
        _require_named_state(
            anchor,
            staged_name,
            installed.payload,
            installed.fingerprint,
            installed.atime_ns,
        )
    except BaseException:
        _rename_with_flags(
            staged_name,
            anchor.name,
            anchor.parent_fd,
            RENAME_NOREPLACE,
        )
        raise


def _publish_pair(
    root: Path,
    outputs: Mapping[str, bytes],
    verifier: Callable[[], None],
) -> None:
    if len(outputs) != 2:
        raise _fail("OUTPUT_SET_INCOMPLETE")
    rels = sorted(outputs)
    if len(set(rels)) != 2:
        raise _fail("OUTPUT_COLLISION")
    anchors: dict[str, OutputAnchor] = {}
    staged: dict[str, str] = {}
    installed: list[InstalledOutput] = []
    try:
        for rel in rels:
            anchors[rel] = _open_output_anchor(root, rel)
        for rel in rels:
            staged[rel] = _write_temp(anchors[rel], outputs[rel], OUTPUT_MODE)
        for rel in rels:
            anchor = anchors[rel]
            _require_anchor_preimage(anchor)
            _install_staged_output(
                anchor,
                staged[rel],
                outputs[rel],
                installed,
            )
        synced: set[tuple[int, int]] = set()
        for rel in rels:
            anchor = anchors[rel]
            identity = (anchor.parent_device, anchor.parent_inode)
            if identity in synced:
                continue
            synced.add(identity)
            try:
                os.fsync(anchor.parent_fd)
            except OSError as exc:
                raise _fail("PUBLICATION_VERIFY_FAILED") from exc
        for rel in rels:
            anchor = anchors[rel]
            _verify_anchor_parent(anchor)
            if _directory_case_matches(anchor.parent_fd, anchor.name) != [anchor.name]:
                raise _fail("OUTPUT_CASE_AMBIGUOUS")
            actual, _ = _stable_anchored_read(anchor.parent_fd, anchor.name)
            metadata = os.stat(
                anchor.name,
                dir_fd=anchor.parent_fd,
                follow_symlinks=False,
            )
            if actual != outputs[rel] or stat.S_IMODE(metadata.st_mode) != OUTPUT_MODE:
                raise _fail("PUBLICATION_VERIFY_FAILED")
        verifier()
        for rel, temp_name in staged.items():
            _unlink_anchored(anchors[rel], temp_name)
    except BaseException as publish_error:
        rollback_errors: list[BaseException] = []
        for installed_output in reversed(installed):
            try:
                _rollback_installed_output(
                    installed_output,
                    staged[installed_output.anchor.rel],
                )
            except BaseException as exc:  # pragma: no cover - catastrophic filesystem failure
                rollback_errors.append(exc)
        for rel, temp_name in staged.items():
            try:
                _unlink_anchored(anchors[rel], temp_name)
            except BaseException as exc:
                rollback_errors.append(exc)
        if rollback_errors:
            raise _fail("PUBLICATION_ROLLBACK_INCOMPLETE") from publish_error
        raise
    finally:
        for rel, temp_name in staged.items():
            try:
                _unlink_anchored(anchors[rel], temp_name)
            except BaseException:
                pass
        for anchor in anchors.values():
            os.close(anchor.parent_fd)


def _allowed_write_status(
    root: Path, context: GitContext, outputs: set[str]
) -> None:
    if not _worktree_changes(root, context).issubset(outputs):
        raise _fail("UNEXPECTED_WRITE_RESIDUE")


def _require_output_bytes(root: Path, rel: str, expected: bytes) -> None:
    try:
        metadata = (root / rel).lstat()
    except FileNotFoundError as exc:
        raise _fail("OUTPUT_MISSING") from exc
    if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
        raise _fail("OUTPUT_NOT_REGULAR")
    actual, _ = _stable_read(root, rel, max_bytes=MAX_OUTPUT_BYTES)
    if actual != expected:
        raise _fail("OUTPUT_BYTES_MISMATCH")
    if stat.S_IMODE(metadata.st_mode) != OUTPUT_MODE:
        raise _fail("OUTPUT_MODE_MISMATCH")


def _render_twice(model: CandidateModel) -> dict[str, bytes]:
    first = _render_candidate(model)
    second = _render_candidate(model)
    if first != second or set(first) != {model.report_path, model.manifest_path}:
        raise _fail("NONDETERMINISTIC_RENDER")
    if any(not payload or not payload.endswith(b"\n") for payload in first.values()):
        raise _fail("OUTPUT_BYTES_INVALID")
    if any(len(payload) > MAX_OUTPUT_BYTES for payload in first.values()):
        raise _fail("OUTPUT_TOO_LARGE")
    return first


def _run_write(
    root: Path, context: GitContext, head: str, source_rel: str
) -> tuple[str, str]:
    _require_clean(root, context)
    model, snapshots = _load_model(root, context, head, source_rel)
    outputs = _render_twice(model)
    _verify_snapshots(root, context, head, snapshots)
    _require_clean(root, context)
    tree = _tree_entries(context)
    for rel in outputs:
        _require_output_case_unambiguous(tree, rel)
        _validate_output_target(root, rel)

    unchanged = True
    for rel, expected in outputs.items():
        try:
            _require_output_bytes(root, rel, expected)
        except ClosePackError:
            unchanged = False
            break
    if not unchanged:
        output_paths = set(outputs)

        def verify_publication() -> None:
            _verify_snapshots(root, context, head, snapshots)
            _allowed_write_status(root, context, output_paths)
            for rel, expected in outputs.items():
                _require_output_bytes(root, rel, expected)

        _publish_pair(root, outputs, verify_publication)

    _verify_snapshots(root, context, head, snapshots)
    _allowed_write_status(root, context, set(outputs))
    for rel, expected in outputs.items():
        _require_output_bytes(root, rel, expected)
    return model.report_path, model.manifest_path


def _run_check(
    root: Path,
    context: GitContext,
    head: str,
    source_rel: str,
    metadata_before: Mapping[str, tuple[int, int, int, int, int, int, int]],
    git_control_paths: Sequence[Path],
    git_control_before: Mapping[
        str, tuple[int, int, int, int, int, int, int, str] | None
    ],
) -> tuple[str, str]:
    _require_clean(root, context)
    primary_error: BaseException | None = None
    try:
        model, snapshots = _load_model(root, context, head, source_rel)
        outputs = _render_twice(model)
        _verify_snapshots(root, context, head, snapshots)
        store = _GitObjectStore(context)
        tree = _tree_entries(context, store)
        for rel, expected in outputs.items():
            entry = _require_tracked_regular(tree, rel)
            if entry.mode != "100644":
                raise _fail("OUTPUT_MODE_MISMATCH")
            _require_output_bytes(root, rel, expected)
            if _git_blob_payload(context, entry.object_id, store) != expected:
                raise _fail("OUTPUT_HEAD_MISMATCH")
        _verify_snapshots(root, context, head, snapshots)
        _require_clean(root, context)
        if _head(context) != head:
            raise _fail("GIT_HEAD_CHANGED")
        return model.report_path, model.manifest_path
    except BaseException as exc:
        primary_error = exc
        raise
    finally:
        try:
            metadata_after = _repository_metadata(root)
            changes_after = _worktree_changes(root, context)
            head_after = _head(context)
            tree_after = _tree_entries(context)
            git_control_after = _git_control_state(git_control_paths)
            if (
                not _metadata_matches_with_symlink_atime_exemption(
                    metadata_before, metadata_after, tree_after
                )
                or git_control_after != git_control_before
                or changes_after
                or head_after != head
            ):
                raise _fail("CHECK_MODE_MUTATION")
        except BaseException as final_error:
            if primary_error is None:
                raise
            raise final_error from primary_error


def _require_closed_rails() -> None:
    if any(os.environ.get(key) != value for key, value in CLOSED_RAILS.items()):
        raise _fail("CLOSED_RAILS_REQUIRED")


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    arguments = list(argv) if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Generate or check one tracked-input epic closeout candidate pair"
    )
    parser.add_argument(
        "--source",
        required=True,
        help="tracked repository-relative candidate source",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="atomically publish the candidate pair")
    mode.add_argument(
        "--check",
        action="store_true",
        help="validate the exact committed pair without writing",
    )
    if sum(
        argument == "--source" or argument.startswith("--source=")
        for argument in arguments
    ) != 1:
        parser.error("exactly one --source is required")
    if sum(argument in {"--write", "--check"} for argument in arguments) != 1:
        parser.error("exactly one mode is required")
    return parser.parse_args(arguments)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        _require_closed_rails()
        source_rel = _canonical_relative_path(args.source, code="SOURCE_PATH_INVALID")
        root = _repository_root()
        context = _establish_git_context(root)
        if args.write:
            _verify_git_repository(context)
            head = _head(context)
            paths = _run_write(root, context, head, source_rel)
        else:
            git_control_paths = _git_control_paths(context)
            metadata_before = _repository_metadata(root)
            git_control_before = _git_control_state(git_control_paths)
            _verify_git_context(context)
            head = _head(context)
            paths = _run_check(
                root,
                context,
                head,
                source_rel,
                metadata_before,
                git_control_paths,
                git_control_before,
            )
    except (ClosePackError, OSError, ValueError) as exc:
        code = str(exc) if isinstance(exc, ClosePackError) else "UNSAFE_STATE"
        print(f"EPIC_CLOSE_PACK_ERROR:{code}", file=sys.stderr)
        return 1
    mode = "WRITE" if args.write else "CHECK"
    print(f"EPIC_CLOSE_PACK_{mode}_OK:{paths[0]}:{paths[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
