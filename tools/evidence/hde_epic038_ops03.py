#!/usr/bin/env python3
"""Independent, read-only validator for the HDE-EPIC038 OPS-03 packet."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RUNNER = (ROOT / "scripts/ops/hde_epic038_ops03.py").resolve()
VALIDATOR = Path(__file__).resolve()
SCHEMA_ROOT = ROOT / "schemas"
RUN_ROOT = Path("/tmp/hde-epic038-ops03")
GIT_TIMEOUT_SECONDS = 10.0

SCHEMA_RECEIPT = "hde_epic038.ops03.validation_receipt.v1"
SCHEMA_ATTESTATION = "hde_epic038.ops03.candidate_attestation.v1"
PRIMARY_FILES = (
    "commands.txt",
    "db_posture_summary.json",
    "env_presence.json",
    "exit_code.txt",
    "nonclaims.json",
    "result_summary.json",
    "stderr.log",
    "stdout.log",
)
RECEIPT_FILE = "validation_receipt.json"
CHECKSUM_FILE = "checksums.sha256"
PENDING_FILE = ".capture.pending"
COMMITTED_FILE = ".capture.committed"
FINAL_FILES = tuple(sorted((*PRIMARY_FILES, RECEIPT_FILE, CHECKSUM_FILE)))
CHECKSUM_INPUTS = tuple(sorted((*PRIMARY_FILES, RECEIPT_FILE)))
ORDERED_QUERY_IDS = (
    "set_transaction_read_only",
    "set_search_path",
    "connection_identity",
    "search_path",
    "runtime_role_grants",
    "ddl_columns",
    "ddl_constraints",
    "boundary_views",
    "partition_inventory",
    "partition_verify",
)
EXPECTED_COUNTS = {
    "provider_selections": 1,
    "health_connections": 1,
    "health_sql_statements": 1,
    "posture_transactions": 1,
    "posture_sql_statements": 10,
    "direct_connections": 2,
    "sql_statements": 11,
    "sql_writes": 0,
    "retries": 0,
    "alternate_provider_attempts": 0,
}
RETIRED_KEYS = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)
NONCLAIMS = (
    "acceptance_token_satisfaction",
    "deployment",
    "epic_closeout",
    "migration",
    "pf09_status_movement",
    "production_write_authorization",
    "qa_pass",
    "railway_inventory_proof",
    "retired_transport_availability",
)
POSTURE_PREDICATES = (
    "authorization_match",
    "direct_provider_only",
    "read_only_transaction",
    "search_path_exact",
    "least_privilege_role",
    "ddl_identity_valid",
    "constraints_observed",
    "boundary_views_readonly",
    "partition_posture_observed",
    "counts_exact",
    "secret_values_absent",
)
RECEIPT_PREDICATES = (
    "authorization_valid",
    "source_identity_valid",
    "schemas_valid",
    "canonical_bytes_valid",
    "inventory_valid",
    "counts_valid",
    "secret_scan_valid",
    "nonclaims_valid",
)
JSON_SCHEMAS = {
    "db_posture_summary.json": "hde_epic038_ops03_db_posture_summary.v1.json",
    "env_presence.json": "hde_epic038_ops03_env_presence.v1.json",
    "nonclaims.json": "hde_epic038_ops03_nonclaims.v1.json",
    "result_summary.json": "hde_epic038_ops03_result_summary.v1.json",
    RECEIPT_FILE: "hde_epic038_ops03_validation_receipt.v1.json",
}
VALIDATOR_ENV = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "ALLOW_DB_WRITE": "0",
}

_DIR_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
_FILE_READ_FLAGS = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
_FILE_WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
_RUN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{15,63}$")


@dataclass
class PacketContext:
    run_id: str
    tmp_fd: int
    root_fd: int
    base_fd: int
    control_fd: int
    candidate_fd: int

    def close(self) -> None:
        for name in ("candidate_fd", "control_fd", "base_fd", "root_fd", "tmp_fd"):
            fd = getattr(self, name)
            if fd is None:
                continue
            try:
                os.close(fd)
            except BaseException:
                pass
            setattr(self, name, None)


def _entry_matches(parent_fd: int, name: str, child_fd: int) -> bool:
    try:
        linked = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        opened = os.fstat(child_fd)
    except OSError:
        return False
    return stat.S_ISDIR(linked.st_mode) and (linked.st_dev, linked.st_ino) == (opened.st_dev, opened.st_ino)


def _secure_open_dir(parent_fd: int, name: str) -> int:
    if not name or "/" in name or name in {".", ".."}:
        raise OSError("invalid_directory_name")
    fd = os.open(name, _DIR_FLAGS, dir_fd=parent_fd)
    if not _entry_matches(parent_fd, name, fd):
        os.close(fd)
        raise OSError("directory_generation_changed")
    return fd


def _assert_packet_context(context: PacketContext) -> None:
    if not all(
        (
            _entry_matches(context.tmp_fd, RUN_ROOT.name, context.root_fd),
            _entry_matches(context.root_fd, context.run_id, context.base_fd),
            _entry_matches(context.base_fd, "control", context.control_fd),
            _entry_matches(context.base_fd, "candidate", context.candidate_fd),
            tuple(sorted(os.listdir(context.base_fd))) == ("candidate", "control"),
            _private_directory(context.root_fd),
            _private_directory(context.base_fd),
            _private_directory(context.control_fd),
            _private_directory(context.candidate_fd),
        )
    ):
        raise OSError("packet_generation_changed")


def _private_directory(fd: int) -> bool:
    value = os.fstat(fd)
    return (
        stat.S_ISDIR(value.st_mode)
        and value.st_uid == os.geteuid()
        and stat.S_IMODE(value.st_mode) == 0o700
    )


def _open_packet_context(run_id: str, candidate: Path) -> PacketContext:
    if _RUN_ID_RE.fullmatch(run_id) is None:
        raise OSError("invalid_run_id")
    absolute_candidate = Path(os.path.abspath(candidate))
    if absolute_candidate != RUN_ROOT / run_id / "candidate":
        raise OSError("candidate_path_mismatch")
    tmp_fd = os.open("/tmp", _DIR_FLAGS)
    try:
        root_fd = _secure_open_dir(tmp_fd, RUN_ROOT.name)
        root_stat = os.fstat(root_fd)
        if root_stat.st_uid != os.geteuid() or stat.S_IMODE(root_stat.st_mode) & 0o077:
            os.close(root_fd)
            raise OSError("unsafe_run_root_permissions")
        try:
            base_fd = _secure_open_dir(root_fd, run_id)
            try:
                control_fd = _secure_open_dir(base_fd, "control")
                try:
                    candidate_fd = _secure_open_dir(base_fd, "candidate")
                except BaseException:
                    os.close(control_fd)
                    raise
            except BaseException:
                os.close(base_fd)
                raise
        except BaseException:
            os.close(root_fd)
            raise
        context = PacketContext(run_id, tmp_fd, root_fd, base_fd, control_fd, candidate_fd)
        try:
            _assert_packet_context(context)
            return context
        except BaseException:
            context.close()
            raise
    except BaseException:
        try:
            os.close(tmp_fd)
        except OSError:
            pass
        raise


def _generation(value: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


def _read_bound_file(dir_fd: int, name: str) -> tuple[bytes, tuple[int, int, int, int, int, int]]:
    fd = os.open(name, _FILE_READ_FLAGS, dir_fd=dir_fd)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode):
            raise OSError("not_regular_file")
        linked_before = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
        if not stat.S_ISREG(linked_before.st_mode) or (linked_before.st_dev, linked_before.st_ino) != (before.st_dev, before.st_ino):
            raise OSError("file_entry_generation_changed")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 65536)
            if not chunk:
                payload = b"".join(chunks)
                after = os.fstat(fd)
                linked_after = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                before_generation = _generation(before)
                after_generation = _generation(after)
                if (
                    before_generation != after_generation
                    or _generation(linked_after) != after_generation
                    or len(payload) != after.st_size
                ):
                    raise OSError("file_generation_changed")
                return payload, after_generation
            chunks.append(chunk)
    finally:
        os.close(fd)


def _read_file(dir_fd: int, name: str) -> bytes:
    return _read_bound_file(dir_fd, name)[0]


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("short_write")
        view = view[written:]


def _write_new_file(dir_fd: int, name: str, payload: bytes) -> None:
    fd = os.open(name, _FILE_WRITE_FLAGS, 0o600, dir_fd=dir_fd)
    try:
        _write_all(fd, payload)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.fsync(dir_fd)


def _snapshot_candidate(context: PacketContext) -> tuple[dict[str, bytes], bool]:
    _assert_packet_context(context)
    files: dict[str, bytes] = {}
    generations: dict[str, tuple[int, int, int, int, int, int]] = {}
    regular = True
    initial_names = tuple(sorted(os.listdir(context.candidate_fd)))
    for name in initial_names:
        try:
            info = os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)
            if not stat.S_ISREG(info.st_mode):
                regular = False
                continue
            files[name], generations[name] = _read_bound_file(context.candidate_fd, name)
        except OSError:
            regular = False
    final_names = tuple(sorted(os.listdir(context.candidate_fd)))
    if final_names != initial_names:
        regular = False
    for name, expected in generations.items():
        try:
            if _generation(os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)) != expected:
                regular = False
        except OSError:
            regular = False
    _assert_packet_context(context)
    return files, regular


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _read_json_with_raw(path: Path) -> tuple[Any | None, bool, bytes]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw.decode("utf-8", "strict"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None, False, b""
    return value, raw == canonical_bytes(value), raw


def _schema(name: str) -> Mapping[str, Any]:
    try:
        value = json.loads((SCHEMA_ROOT / name).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("invalid_schema_source") from exc
    if not isinstance(value, Mapping):
        raise ValueError("invalid_schema_source")
    return value


def _schema_valid(value: Any, name: str) -> bool:
    try:
        from tools.evidence.strict_json_schema import is_valid as schema_is_valid

        return schema_is_valid(value, _schema(name))
    except (OSError, ValueError, json.JSONDecodeError):
        return False


def _parse_utc(value: object) -> dt.datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.tzinfo == dt.timezone.utc else None


def derived_paths(run_id: str) -> tuple[Path, Path, Path, Path]:
    base = RUN_ROOT / run_id
    return base, base / "control", base / "candidate", base / "failure"


def expected_argv(auth: Mapping[str, Any], auth_path: Path, candidate: Path) -> dict[str, list[str]]:
    interpreter = str(Path(auth["interpreter"]["resolved_path"]).resolve())
    common = [interpreter, "-I", "-B"]
    authorization = str(auth_path.resolve())
    candidate_arg = str(candidate.resolve())
    return {
        "capture": [*common, str(RUNNER), "--authorization", authorization],
        "receipt": [*common, str(VALIDATOR), "--emit-receipt", "--authorization", authorization, "--candidate", candidate_arg],
        "validate": [*common, str(VALIDATOR), "--validate", "--authorization", authorization, "--candidate", candidate_arg],
    }


def _invocation_valid(
    auth: Mapping[str, Any],
    actual_argv: Sequence[str] | None,
    mode: str | None,
) -> bool:
    if actual_argv is None:
        return True
    if mode not in {"receipt", "validate"}:
        return False
    return (
        list(actual_argv) == auth["exact_argv"][mode]
        and bool(sys.flags.isolated)
        and bool(sys.dont_write_bytecode)
        and dict(os.environ) == VALIDATOR_ENV
    )


def authorization_errors(
    auth: Any,
    auth_path: Path,
    *,
    now: dt.datetime | None = None,
) -> tuple[str, ...]:
    errors: set[str] = set()
    if not isinstance(auth, Mapping) or not _schema_valid(auth, "hde_epic038_ops03_authorization.v1.json"):
        return ("authorization_schema_invalid",)
    run_id = str(auth["run_id"])
    _, _, candidate, _ = derived_paths(run_id)
    if auth.get("candidate_root") != candidate.as_posix() + "/":
        errors.add("candidate_root_mismatch")
    if auth.get("retired_keys_required_absent") != list(RETIRED_KEYS):
        errors.add("retired_key_roster_mismatch")
    if auth.get("ordered_query_ids") != list(ORDERED_QUERY_IDS):
        errors.add("query_roster_mismatch")
    if auth.get("expected_counts") != EXPECTED_COUNTS:
        errors.add("expected_counts_mismatch")
    if auth.get("target") != {"app_env": "dev", "database_schema": "hde", "search_path": ["hde", "public"]}:
        errors.add("target_mismatch")
    if auth.get("rails") != {"safe_mode": "1", "allow_network": "0", "allow_db_write": "0", "db_read_authorized": True}:
        errors.add("rails_mismatch")
    if auth.get("exact_argv") != expected_argv(auth, auth_path, candidate):
        errors.add("argv_mismatch")
    authorized = _parse_utc(auth.get("authorized_at_utc"))
    expires = _parse_utc(auth.get("expires_at_utc"))
    current = now or dt.datetime.now(dt.timezone.utc)
    if authorized is None or expires is None or not (authorized < expires):
        errors.add("authorization_window_invalid")
    elif not (authorized <= current < expires):
        errors.add("authorization_expired_or_not_active")
    return tuple(sorted(errors))


def _bootstrap_authorization_valid(auth: Any) -> bool:
    if not isinstance(auth, Mapping):
        return False
    run_id = auth.get("run_id")
    interpreter = auth.get("interpreter")
    return bool(
        isinstance(run_id, str)
        and _RUN_ID_RE.fullmatch(run_id)
        and isinstance(auth.get("source_commit"), str)
        and re.fullmatch(r"[0-9a-f]{40}", str(auth.get("source_commit")))
        and isinstance(auth.get("runner_sha256"), str)
        and re.fullmatch(r"[0-9a-f]{64}", str(auth.get("runner_sha256")))
        and isinstance(auth.get("validator_sha256"), str)
        and re.fullmatch(r"[0-9a-f]{64}", str(auth.get("validator_sha256")))
        and isinstance(interpreter, Mapping)
        and isinstance(interpreter.get("resolved_path"), str)
        and str(interpreter.get("resolved_path")).startswith("/")
        and "\x00" not in str(interpreter.get("resolved_path"))
        and isinstance(interpreter.get("sha256"), str)
        and re.fullmatch(r"[0-9a-f]{64}", str(interpreter.get("sha256")))
    )


def _git(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    command = [
        "git",
        "-c",
        "core.fsmonitor=false",
        "-c",
        "core.untrackedCache=false",
        "-C",
        str(ROOT),
        "--work-tree",
        str(ROOT),
        *args,
    ]
    try:
        return subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=GIT_TIMEOUT_SECONDS,
            env={
                "LC_ALL": "C",
                "LANG": "C",
                "TZ": "UTC",
                "GIT_CONFIG_GLOBAL": "/dev/null",
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_NO_REPLACE_OBJECTS": "1",
                "GIT_OPTIONAL_LOCKS": "0",
                "GIT_WORK_TREE": str(ROOT),
            },
        )
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(
            command,
            returncode=124,
            stdout="",
            stderr="git_timeout",
        )


def _manifest_entries(raw: str, *, index: bool) -> dict[str, tuple[str, str]] | None:
    entries: dict[str, tuple[str, str]] = {}
    for entry in raw.split("\0"):
        if not entry:
            continue
        try:
            metadata, relative = entry.split("\t", 1)
            fields = metadata.split()
            if index:
                mode, object_id, stage = fields
                if stage != "0":
                    return None
            else:
                mode, kind, object_id = fields
                if kind != "blob":
                    return None
        except ValueError:
            return None
        if relative in entries:
            return None
        entries[relative] = (mode, object_id)
    return entries


def _raw_worktree_entry(relative: str) -> tuple[bytes, str] | None:
    relative_path = Path(relative)
    if relative_path.is_absolute() or not relative_path.parts or ".." in relative_path.parts:
        return None
    parents: list[tuple[Path, tuple[int, int, int, int, int, int]]] = []
    cursor = ROOT
    try:
        for part in relative_path.parts[:-1]:
            cursor = cursor / part
            info = cursor.lstat()
            if not stat.S_ISDIR(info.st_mode):
                return None
            parents.append((cursor, _generation(info)))
        path = ROOT / relative_path
        before = path.lstat()
        if not stat.S_ISREG(before.st_mode):
            return None
        payload = path.read_bytes()
        after = path.lstat()
        if _generation(before) != _generation(after) or len(payload) != after.st_size:
            return None
        for parent, expected in parents:
            if _generation(parent.lstat()) != expected:
                return None
    except OSError:
        return None
    mode = "100755" if stat.S_IMODE(after.st_mode) & 0o111 else "100644"
    return payload, mode


def _source_manifest_auxiliary_error() -> str | None:
    toplevel = _git(("rev-parse", "--show-toplevel"))
    if toplevel.returncode or Path(toplevel.stdout.strip()).resolve() != ROOT:
        return "source_worktree_mismatch"
    replacements = _git(("for-each-ref", "--format=%(refname)", "refs/replace/"))
    if replacements.returncode or replacements.stdout:
        return "source_replacement_ref_present"
    flags = _git(("ls-files", "-v", "-z"))
    if flags.returncode:
        return "source_index_flags_unreadable"
    if any(entry and not entry.startswith("H ") for entry in flags.stdout.split("\0")):
        return "source_index_flags_unsafe"
    index_result = _git(("ls-files", "-s", "-z"))
    head_result = _git(("ls-tree", "-r", "-z", "--full-tree", "HEAD"))
    if index_result.returncode or head_result.returncode:
        return "source_index_manifest_unreadable"
    index_entries = _manifest_entries(index_result.stdout, index=True)
    head_entries = _manifest_entries(head_result.stdout, index=False)
    if index_entries is None or head_entries is None:
        return "source_index_manifest_invalid"
    if index_entries != head_entries:
        return "source_manifest_mismatch"
    for relative, (mode, object_id) in head_entries.items():
        if mode == "120000":
            return "tracked_source_symlink_present"
        if mode not in {"100644", "100755"}:
            return "tracked_source_type_invalid"
        worktree = _raw_worktree_entry(relative)
        if worktree is None:
            return "source_manifest_mismatch"
        payload, worktree_mode = worktree
        blob = hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()
        if worktree_mode != mode or blob != object_id:
            return "source_manifest_mismatch"
    untracked = _git(("ls-files", "--others", "--exclude-standard", "-z"))
    if untracked.returncode or untracked.stdout:
        return "source_tree_not_pristine"
    ignored = _git(("ls-files", "--others", "--ignored", "--exclude-standard", "-z"))
    if ignored.returncode:
        return "ignored_source_manifest_unreadable"
    for relative in ignored.stdout.split("\0"):
        if relative and (ROOT / relative).is_symlink():
            return "ignored_source_symlink_present"
    return None


def source_identity_errors(auth: Mapping[str, Any], *, enforce_repo: bool = True) -> tuple[str, ...]:
    errors: set[str] = set()
    interpreter = Path(sys.executable).resolve()
    expected_interpreter = Path(auth["interpreter"]["resolved_path"]).resolve()
    if interpreter != expected_interpreter:
        errors.add("interpreter_path_mismatch")
    for path, expected, code in (
        (RUNNER, auth.get("runner_sha256"), "runner_hash_mismatch"),
        (VALIDATOR, auth.get("validator_sha256"), "validator_hash_mismatch"),
        (interpreter, auth["interpreter"].get("sha256"), "interpreter_hash_mismatch"),
    ):
        try:
            if sha256_path(path) != expected:
                errors.add(code)
        except OSError:
            errors.add(code)
    if not enforce_repo:
        return tuple(sorted(errors))
    head = _git(("rev-parse", "HEAD"))
    if head.returncode or head.stdout.strip() != auth.get("source_commit"):
        errors.add("source_commit_mismatch")
    auxiliary_error = _source_manifest_auxiliary_error()
    if auxiliary_error is not None:
        errors.add(auxiliary_error)
    if any(ROOT.rglob("*.pyc")) or any(path.is_dir() for path in ROOT.rglob("__pycache__")):
        errors.add("bytecode_residue_present")
    ignored_importable = _git(
        ("ls-files", "--others", "--ignored", "--exclude-standard", "--", "*.py", "*.pyw", "*.so", "*.pyd")
    )
    if ignored_importable.returncode or ignored_importable.stdout:
        errors.add("ignored_native_module_present")
    return tuple(sorted(errors))


def _json_from_bytes(raw: bytes) -> tuple[Any | None, bool]:
    try:
        value = json.loads(raw.decode("utf-8", "strict"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None, False
    return value, raw == canonical_bytes(value)


def _load_candidate_json(files: Mapping[str, bytes]) -> tuple[dict[str, Any], bool]:
    values: dict[str, Any] = {}
    canonical = True
    for name in ("db_posture_summary.json", "env_presence.json", "nonclaims.json", "result_summary.json"):
        value, is_canonical = _json_from_bytes(files.get(name, b""))
        if value is None:
            canonical = False
        else:
            values[name] = value
        canonical = canonical and is_canonical
    return values, canonical


def _core_schema_valid(values: Mapping[str, Any]) -> bool:
    return all(
        name in values and _schema_valid(values[name], JSON_SCHEMAS[name])
        for name in ("db_posture_summary.json", "env_presence.json", "nonclaims.json", "result_summary.json")
    )


def _content_valid(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    files: Mapping[str, bytes],
    values: Mapping[str, Any],
) -> tuple[bool, bool]:
    try:
        posture = values["db_posture_summary.json"]
        env = values["env_presence.json"]
        nonclaims = values["nonclaims.json"]
        summary = values["result_summary.json"]
        commands = "".join(
            f"{name}_argv={json.dumps(auth['exact_argv'][name], sort_keys=True, separators=(',', ':'))}\n"
            for name in ("capture", "receipt", "validate")
        )
        inventory_ok = (
            files.get("commands.txt", b"").decode("utf-8", "strict") == commands
            and files.get("stdout.log") == b"OPS03_CAPTURE_PASS\n"
            and files.get("stderr.log") == b""
            and files.get("exit_code.txt") == b"0\n"
            and env == {
                "schema": "hde_epic038.ops03.env_presence.v1",
                "run_id": auth["run_id"],
                "app_env": "dev",
                "rails": auth["rails"],
                "database_url_presence": "SET_REDACTED",
                "retired_key_presence": {name: "UNSET" for name in RETIRED_KEYS},
                "determinism_pins": {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
            }
            and nonclaims == {"schema": "hde_epic038.ops03.nonclaims.v1", "run_id": auth["run_id"], "nonclaims": list(NONCLAIMS)}
            and summary["run_id"] == auth["run_id"]
            and summary["source_commit"] == auth["source_commit"]
            and summary["authorization_sha256"] == authorization_sha256
            and summary["capture_result"] == "PASS"
            and summary["decisive_predicates"] == posture["predicates"]
            and summary["primary_files"] == list(PRIMARY_FILES)
            and summary["nonclaims_ref"] == "nonclaims.json"
        )
        observations = posture["observations"]
        boundaries = observations["boundary_views"]
        partition = observations["partition_posture"]
        counts_ok = (
            posture["run_id"] == auth["run_id"]
            and posture["source_commit"] == auth["source_commit"]
            and posture["provider"] == "psycopg"
            and posture["selection_attempts"] == [{"provider": "psycopg", "status": "ok", "reason": None}]
            and posture["ordered_query_ids"] == list(ORDERED_QUERY_IDS)
            and [row["query_id"] for row in posture["query_results"]] == list(ORDERED_QUERY_IDS)
            and posture["counts"] == auth["expected_counts"] == EXPECTED_COUNTS
            and set(posture["predicates"]) == set(POSTURE_PREDICATES)
            and all(posture["predicates"].values())
            and posture["result"] == "PASS"
            and observations["connection_identity_presence"] is True
            and observations["search_path"] == ["hde", "public"]
            and observations["runtime_role_flags"] == {
                "rolsuper": False,
                "rolcreatedb": False,
                "rolcreaterole": False,
                "rolreplication": False,
                "rolbypassrls": False,
                "schema_create": False,
                "relation_write": False,
            }
            and observations["ddl_identity"]["schema"] == "hde.ddl_identity_projection.v1"
            and observations["constraint_count"] >= 1
            and sorted(boundaries, key=lambda row: row["name"]) == [
                {"name": "hde.body_graphs_current", "read_only": True},
                {"name": "public.hde_body_graphs_current", "read_only": True},
            ]
            and partition == {
                "expected_tables": ["hde.pair_evaluation", "hde.public_results"],
                "observed_tables": ["hde.pair_evaluation", "hde.public_results"],
                "all_expected_present": True,
            }
        )
        return inventory_ok, counts_ok
    except (KeyError, TypeError, ValueError, OSError, UnicodeDecodeError):
        return False, False


def _secret_scan_valid(candidate: Path, files: Mapping[str, bytes], names: Sequence[str]) -> bool:
    for name in names:
        path = candidate / name
        payload = files.get(name)
        if payload is None:
            return False
        from tools.evidence.retained_evidence_safety import validate_retained_text_safety

        if validate_retained_text_safety(path, payload):
            return False
    return True


def _checksums_valid(files: Mapping[str, bytes]) -> bool:
    try:
        lines = files[CHECKSUM_FILE].decode("ascii", "strict").splitlines()
    except (KeyError, UnicodeDecodeError):
        return False
    try:
        expected = [f"{sha256_bytes(files[name])}  {name}" for name in CHECKSUM_INPUTS]
    except KeyError:
        return False
    return lines == expected


def _candidate_attestation(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    files: Mapping[str, bytes],
) -> dict[str, Any]:
    return {
        "schema": SCHEMA_ATTESTATION,
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "files": {name: sha256_bytes(files[name]) for name in FINAL_FILES},
    }


def _candidate_commit_record(
    files: Mapping[str, bytes],
    *,
    sealed: bool,
    finalized: bool,
) -> dict[str, Any]:
    names = FINAL_FILES if sealed else tuple(sorted(PRIMARY_FILES))
    return {
        "schema": "hde_epic038.ops03.candidate_commit.v1",
        "sealed": sealed,
        "finalized": finalized,
        "files": {name: sha256_bytes(files[name]) for name in names},
    }


def _authorization_consumption(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    candidate_commit: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    value = {
        "schema": "hde_epic038.ops03.authorization_consumption.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "launch_consumed": True,
    }
    if candidate_commit is not None:
        value["candidate_commit"] = dict(candidate_commit)
    return value


def _committed_marker_valid(
    raw: bytes,
    auth: Mapping[str, Any],
    authorization_sha256: str,
) -> bool:
    value, canonical = _json_from_bytes(raw)
    if not canonical or not isinstance(value, Mapping):
        return False
    runner_pid = value.get("runner_pid")
    token_sha256 = value.get("runner_token_sha256")
    return bool(
        set(value)
        == {
            "schema",
            "run_id",
            "authorization_sha256",
            "runner_pid",
            "runner_token_sha256",
        }
        and value.get("schema") == "hde_epic038.ops03.capture_pending.v1"
        and value.get("run_id") == auth.get("run_id")
        and value.get("authorization_sha256") == authorization_sha256
        and isinstance(runner_pid, int)
        and not isinstance(runner_pid, bool)
        and runner_pid > 0
        and isinstance(token_sha256, str)
        and re.fullmatch(r"[0-9a-f]{64}", token_sha256)
    )


def _receipt(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    predicates: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "schema": SCHEMA_RECEIPT,
        "run_id": auth.get("run_id", "invalid-authorization"),
        "authorization_sha256": authorization_sha256,
        "validated_files": list(PRIMARY_FILES),
        "predicates": {name: bool(predicates[name]) for name in RECEIPT_PREDICATES},
        "result": "PASS" if all(predicates.values()) else "FAIL",
    }


def _control_state_valid(
    context: PacketContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    candidate_commit: Mapping[str, Any] | None = None,
) -> bool:
    try:
        _assert_packet_context(context)
        committed_required = bool(
            candidate_commit is not None
            and candidate_commit.get("finalized") is True
        )
        control_names = (
            (COMMITTED_FILE, "authorization_consumed.json", "launch.marker")
            if committed_required
            else ("authorization_consumed.json", "launch.marker")
        )
        if tuple(sorted(os.listdir(context.control_fd))) != control_names:
            return False
        if _read_file(context.control_fd, "launch.marker") != b"launch_consumed=true\n":
            return False
        expected_candidate_commit = candidate_commit
        if committed_required:
            committed_payload = _read_file(context.control_fd, COMMITTED_FILE)
            if not _committed_marker_valid(
                committed_payload,
                auth,
                authorization_sha256,
            ):
                return False
            expected_candidate_commit = {
                **candidate_commit,
                "committed_marker_sha256": sha256_bytes(committed_payload),
            }
        expected = _authorization_consumption(
            auth,
            authorization_sha256,
            candidate_commit=expected_candidate_commit,
        )
        consumption_valid = _read_file(
            context.control_fd,
            "authorization_consumed.json",
        ) == canonical_bytes(expected)
        _assert_packet_context(context)
        return (
            consumption_valid
            and tuple(sorted(os.listdir(context.control_fd))) == control_names
        )
    except (OSError, KeyError, TypeError):
        return False


def _failure_state_present(context: PacketContext) -> bool:
    try:
        os.stat("failure", dir_fd=context.base_fd, follow_symlinks=False)
        return True
    except FileNotFoundError:
        return False
    except OSError:
        return True


def _pending_latch_authorized(
    raw: bytes,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    actual_argv: Sequence[str] | None,
    mode: str | None,
    pending_token: bytes | None,
) -> bool:
    if (
        actual_argv is None
        or mode not in {"receipt", "validate"}
        or pending_token is None
        or len(pending_token) != 32
    ):
        return False
    value, canonical = _json_from_bytes(raw)
    expected = {
        "schema": "hde_epic038.ops03.capture_pending.v1",
        "run_id": auth.get("run_id"),
        "authorization_sha256": authorization_sha256,
        "runner_pid": os.getppid(),
        "runner_token_sha256": sha256_bytes(pending_token),
    }
    return canonical and value == expected


def _admission_state_stable(
    context: PacketContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    expected_files: Mapping[str, bytes],
    *,
    candidate_commit: Mapping[str, Any] | None = None,
    infer_candidate_commit: bool = True,
) -> bool:
    try:
        _assert_packet_context(context)
        if infer_candidate_commit:
            if PENDING_FILE in expected_files:
                candidate_commit = None
            else:
                names = tuple(sorted(expected_files))
                if names == FINAL_FILES:
                    sealed = True
                elif names == tuple(sorted(PRIMARY_FILES)):
                    sealed = False
                else:
                    return False
                candidate_commit = _candidate_commit_record(
                    expected_files,
                    sealed=sealed,
                    finalized=True,
                )
        if _failure_state_present(context) or not _control_state_valid(
            context,
            auth,
            authorization_sha256,
            candidate_commit=candidate_commit,
        ):
            return False
        current_files, regular = _snapshot_candidate(context)
        if not regular or current_files != expected_files:
            return False
        if not _control_state_valid(
            context,
            auth,
            authorization_sha256,
            candidate_commit=candidate_commit,
        ):
            return False
        _assert_packet_context(context)
        return not _failure_state_present(context)
    except OSError:
        return False


def validate_packet(
    auth_path: Path,
    candidate: Path,
    *,
    final: bool,
    enforce_source: bool = True,
    now: dt.datetime | None = None,
    actual_argv: Sequence[str] | None = None,
    mode: str | None = None,
    emit_receipt: bool = False,
    pending_token: bytes | None = None,
    attestation_out: dict[str, Any] | None = None,
) -> dict[str, Any]:
    auth_value, auth_canonical, authorization_bytes = _read_json_with_raw(auth_path)
    authorization_sha256 = sha256_bytes(authorization_bytes)
    auth = dict(auth_value) if isinstance(auth_value, Mapping) else {}
    bootstrap_valid = _bootstrap_authorization_valid(auth)
    source_errors = (
        source_identity_errors(auth, enforce_repo=enforce_source)
        if bootstrap_valid
        else ("source_not_checked",)
    )
    auth_errors = (
        authorization_errors(auth, auth_path, now=now)
        if bootstrap_valid and not source_errors
        else (("authorization_invalid",) if not bootstrap_valid else ("source_identity_invalid",))
    )
    context: PacketContext | None = None
    snapshot_files: dict[str, bytes] = {}
    files: dict[str, bytes] = {}
    entries_are_regular = False
    terminal_snapshot: Mapping[str, bytes] = {}
    terminal_control_commit: Mapping[str, Any] | None = None
    infer_terminal_control = True
    try:
        if not auth_errors:
            try:
                context = _open_packet_context(str(auth["run_id"]), candidate)
                if _failure_state_present(context):
                    auth_errors = ("failure_state_present",)
                elif not _invocation_valid(auth, actual_argv, mode):
                    auth_errors = ("validator_invocation_mismatch",)
                else:
                    snapshot_files, entries_are_regular = _snapshot_candidate(context)
                    terminal_snapshot = snapshot_files
                    files = dict(snapshot_files)
                    pending = files.get(PENDING_FILE)
                    if pending is not None:
                        if not _control_state_valid(
                            context,
                            auth,
                            authorization_sha256,
                        ):
                            auth_errors = ("consumed_failure_state_present",)
                        elif _pending_latch_authorized(
                            pending,
                            auth,
                            authorization_sha256,
                            actual_argv,
                            mode,
                            pending_token,
                        ):
                            del files[PENDING_FILE]
                    else:
                        names = tuple(sorted(files))
                        if names == FINAL_FILES:
                            sealed = True
                        elif names == tuple(sorted(PRIMARY_FILES)):
                            sealed = False
                        else:
                            sealed = None
                        if sealed is None or not _control_state_valid(
                            context,
                            auth,
                            authorization_sha256,
                            candidate_commit=(
                                _candidate_commit_record(
                                    files,
                                    sealed=sealed,
                                    finalized=True,
                                )
                                if sealed is not None
                                else None
                            ),
                        ):
                            auth_errors = ("consumed_failure_state_present",)
            except OSError:
                auth_errors = ("candidate_path_or_generation_invalid",)

        expected_names = FINAL_FILES if final else tuple(sorted(PRIMARY_FILES))
        actual_names = tuple(sorted(files))
        inventory_exact = actual_names == expected_names and entries_are_regular
        values, core_canonical = _load_candidate_json(files)
        schemas_valid = not source_errors and _core_schema_valid(values)
        content_valid, counts_valid = (
            _content_valid(auth, authorization_sha256, files, values)
            if not auth_errors
            else (False, False)
        )
        canonical_valid = auth_canonical and core_canonical
        secret_names = list(PRIMARY_FILES)
        receipt_value: Any | None = None
        if final:
            receipt_value, receipt_canonical = _json_from_bytes(files.get(RECEIPT_FILE, b""))
            canonical_valid = canonical_valid and receipt_canonical
            schemas_valid = (
                schemas_valid
                and receipt_value is not None
                and _schema_valid(receipt_value, JSON_SCHEMAS[RECEIPT_FILE])
            )
            secret_names.append(RECEIPT_FILE)
        predicates = {
            "authorization_valid": not auth_errors and auth_canonical,
            "source_identity_valid": not source_errors,
            "schemas_valid": schemas_valid,
            "canonical_bytes_valid": canonical_valid,
            "inventory_valid": inventory_exact and content_valid,
            "counts_valid": counts_valid,
            "secret_scan_valid": not source_errors
            and _secret_scan_valid(candidate, files, secret_names),
            "nonclaims_valid": values.get("nonclaims.json") == {
                "schema": "hde_epic038.ops03.nonclaims.v1",
                "run_id": auth.get("run_id"),
                "nonclaims": list(NONCLAIMS),
            },
        }
        try:
            authorization_stable = auth_path.read_bytes() == authorization_bytes
        except OSError:
            authorization_stable = False
        predicates["authorization_valid"] = predicates["authorization_valid"] and authorization_stable
        receipt = _receipt(auth, authorization_sha256, predicates)
        if final:
            predicates["inventory_valid"] = (
                predicates["inventory_valid"]
                and receipt_value == receipt
                and _checksums_valid(files)
            )
            receipt = _receipt(auth, authorization_sha256, predicates)
        if receipt["result"] == "PASS" and context is not None:
            if not _admission_state_stable(context, auth, authorization_sha256, snapshot_files):
                predicates["authorization_valid"] = False
                receipt = _receipt(auth, authorization_sha256, predicates)
        if emit_receipt and receipt["result"] == "PASS":
            if context is None or final:
                predicates["inventory_valid"] = False
                receipt = _receipt(auth, authorization_sha256, predicates)
            else:
                try:
                    _assert_packet_context(context)
                    _write_new_file(context.candidate_fd, RECEIPT_FILE, canonical_bytes(receipt))
                    _assert_packet_context(context)
                    emitted_files = {**snapshot_files, RECEIPT_FILE: canonical_bytes(receipt)}
                    emitted_control_commit = None
                    infer_emitted_control = True
                    if tuple(sorted(snapshot_files)) == tuple(sorted(PRIMARY_FILES)):
                        emitted_control_commit = _candidate_commit_record(
                            snapshot_files,
                            sealed=False,
                            finalized=True,
                        )
                        infer_emitted_control = False
                    if not _admission_state_stable(
                        context,
                        auth,
                        authorization_sha256,
                        emitted_files,
                        candidate_commit=emitted_control_commit,
                        infer_candidate_commit=infer_emitted_control,
                    ):
                        try:
                            os.unlink(RECEIPT_FILE, dir_fd=context.candidate_fd)
                            os.fsync(context.candidate_fd)
                        except OSError:
                            pass
                        raise OSError("post_emit_admission_state_changed")
                    terminal_snapshot = emitted_files
                    terminal_control_commit = emitted_control_commit
                    infer_terminal_control = infer_emitted_control
                except OSError:
                    predicates["inventory_valid"] = False
                    receipt = _receipt(auth, authorization_sha256, predicates)
        if receipt["result"] == "PASS" and context is not None:
            if not _admission_state_stable(
                context,
                auth,
                authorization_sha256,
                terminal_snapshot,
                candidate_commit=terminal_control_commit,
                infer_candidate_commit=infer_terminal_control,
            ):
                predicates["authorization_valid"] = False
                receipt = _receipt(auth, authorization_sha256, predicates)
        if receipt["result"] == "PASS":
            try:
                terminal_authorization_stable = (
                    auth_path.read_bytes() == authorization_bytes
                )
            except OSError:
                terminal_authorization_stable = False
            terminal_source_errors = source_identity_errors(
                auth,
                enforce_repo=enforce_source,
            )
            try:
                terminal_authorization_stable = (
                    terminal_authorization_stable
                    and auth_path.read_bytes() == authorization_bytes
                )
            except OSError:
                terminal_authorization_stable = False
            if terminal_source_errors:
                predicates["source_identity_valid"] = False
            if not terminal_authorization_stable:
                predicates["authorization_valid"] = False
            receipt = _receipt(auth, authorization_sha256, predicates)
        if receipt["result"] == "PASS" and context is not None:
            if not _admission_state_stable(
                context,
                auth,
                authorization_sha256,
                terminal_snapshot,
                candidate_commit=terminal_control_commit,
                infer_candidate_commit=infer_terminal_control,
            ):
                predicates["authorization_valid"] = False
                receipt = _receipt(auth, authorization_sha256, predicates)
        if final and receipt["result"] == "PASS" and attestation_out is not None:
            attestation_out.update(_candidate_attestation(auth, authorization_sha256, files))
        return receipt
    finally:
        if context is not None:
            context.close()


def _read_pending_token() -> bytes | None:
    try:
        if os.isatty(sys.stdin.fileno()):
            return None
        raw = os.read(sys.stdin.fileno(), 33)
    except (OSError, ValueError):
        return None
    return raw if len(raw) == 32 else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--emit-receipt", action="store_true")
    mode.add_argument("--validate", action="store_true")
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    args = parser.parse_args(argv)
    mode_name = "validate" if args.validate else "receipt"
    actual_argv = list(sys.orig_argv) if argv is None else None
    attestation: dict[str, Any] = {}
    receipt = validate_packet(
        args.authorization.resolve(),
        Path(os.path.abspath(args.candidate)),
        final=args.validate,
        actual_argv=actual_argv,
        mode=mode_name,
        emit_receipt=args.emit_receipt,
        pending_token=_read_pending_token(),
        attestation_out=attestation if args.validate else None,
    )
    if receipt["result"] != "PASS":
        sys.stderr.buffer.write(canonical_bytes(receipt))
        return 1
    if args.validate:
        sys.stdout.buffer.write(canonical_bytes(attestation))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
