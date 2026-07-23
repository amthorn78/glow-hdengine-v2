#!/usr/bin/env python3
"""Authorization-bound direct PostgreSQL read-only OPS-03 capture runner."""
from __future__ import annotations

import argparse
import datetime as dt
import errno
import hashlib
import json
import os
import re
import select
import signal
import stat
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RETIRED_DB_TRANSPORT_KEYS = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)


@dataclass(frozen=True)
class Statement:
    sql: str
    fetch: bool = False


RUNNER = Path(__file__).resolve()
VALIDATOR = (ROOT / "tools/evidence/hde_epic038_ops03.py").resolve()
AUTH_SCHEMA = ROOT / "schemas/hde_epic038_ops03_authorization.v1.json"
RUN_ROOT = Path("/tmp/hde-epic038-ops03")
RUN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{15,63}$")
GIT_TIMEOUT_SECONDS = 10.0

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
PENDING_FILE = ".capture.pending"
FAILURE_LATCH_FILE = ".capture.failed"
COMMITTED_FILE = ".capture.committed"
FAILED_COMMIT_FILE = ".capture.commit_failed"
CHECKSUM_INPUTS = tuple(sorted((*PRIMARY_FILES, "validation_receipt.json")))
FINAL_FILES = tuple(sorted((*PRIMARY_FILES, "validation_receipt.json", "checksums.sha256")))
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
EXPECTED_PARTITIONS = ("hde.pair_evaluation", "hde.public_results")
EXPECTED_PARTITION_DEFINITIONS = {
    "hde.pair_evaluation": ("r", "RANGE (evaluated_at)"),
    "hde.public_results": ("r", "RANGE (created_at)"),
}
EXPECTED_VIEWS = ("hde.body_graphs_current", "public.hde_body_graphs_current")
CHILD_READY_TIMEOUT_SECONDS = 10.0
PROVIDER_CHILD_TIMEOUT_SECONDS = 60.0
PROVIDER_REAP_TIMEOUT_SECONDS = 2.0
VALIDATOR_TIMEOUT_SECONDS = 60.0

QUERY_STATEMENTS = (
    Statement("SET TRANSACTION READ ONLY"),
    Statement("SET LOCAL search_path TO hde, public"),
    Statement(
        "SELECT current_database() IS NOT NULL, current_user IS NOT NULL, "
        "current_setting('transaction_read_only') = 'on'",
        fetch=True,
    ),
    Statement("SHOW search_path", fetch=True),
    Statement(
        "SELECT role.rolsuper, role.rolcreatedb, role.rolcreaterole, "
        "role.rolreplication, role.rolbypassrls, "
        "EXISTS (SELECT 1 FROM pg_namespace nsp "
        "WHERE nsp.nspname IN ('hde', 'public') "
        "AND (pg_has_role(current_user, nsp.nspowner, 'USAGE') "
        "OR EXISTS (SELECT 1 FROM aclexplode(COALESCE(nsp.nspacl, "
        "acldefault('n', nsp.nspowner))) acl "
        "WHERE acl.privilege_type <> 'USAGE' "
        "AND (acl.grantee = 0 OR pg_has_role(current_user, acl.grantee, 'USAGE'))))), "
        "EXISTS (SELECT 1 FROM information_schema.table_privileges priv "
        "LEFT JOIN pg_roles grantee ON grantee.rolname = priv.grantee "
        "WHERE priv.table_schema IN ('hde', 'public') "
        "AND priv.privilege_type <> 'SELECT' "
        "AND (priv.grantee = 'PUBLIC' OR (grantee.oid IS NOT NULL "
        "AND pg_has_role(current_user, grantee.oid, 'USAGE')))) "
        "OR EXISTS (SELECT 1 FROM information_schema.column_privileges priv "
        "LEFT JOIN pg_roles grantee ON grantee.rolname = priv.grantee "
        "WHERE priv.table_schema IN ('hde', 'public') "
        "AND priv.privilege_type <> 'SELECT' "
        "AND (priv.grantee = 'PUBLIC' OR (grantee.oid IS NOT NULL "
        "AND pg_has_role(current_user, grantee.oid, 'USAGE')))) "
        # PostgreSQL omits its nonstandard sequence UPDATE grant from
        # information_schema.usage_privileges, so inspect the effective ACL and
        # treat every sequence privilege except SELECT as write-capable.
        "OR EXISTS (SELECT 1 FROM pg_class seq "
        "JOIN pg_namespace nsp ON nsp.oid = seq.relnamespace "
        "CROSS JOIN LATERAL aclexplode(COALESCE(seq.relacl, "
        "acldefault('s', seq.relowner))) seq_acl "
        "WHERE nsp.nspname IN ('hde', 'public') AND seq.relkind = 'S' "
        "AND seq_acl.privilege_type <> 'SELECT' "
        "AND (seq_acl.grantee = 0 OR "
        "pg_has_role(current_user, seq_acl.grantee, 'USAGE'))) "
        "OR EXISTS (SELECT 1 FROM pg_class cls "
        "JOIN pg_namespace nsp ON nsp.oid = cls.relnamespace "
        "WHERE nsp.nspname IN ('hde', 'public') "
        "AND pg_has_role(current_user, cls.relowner, 'USAGE')) "
        "FROM pg_roles role WHERE role.rolname = current_user",
        fetch=True,
    ),
    Statement(
        "SELECT column_name, data_type, is_nullable, column_default "
        "FROM information_schema.columns "
        "WHERE table_schema = 'hde' AND table_name = 'body_graphs' "
        "ORDER BY ordinal_position",
        fetch=True,
    ),
    Statement(
        "SELECT con.conname, pg_get_constraintdef(con.oid, true) "
        "FROM pg_constraint con "
        "JOIN pg_class cls ON cls.oid = con.conrelid "
        "JOIN pg_namespace nsp ON nsp.oid = con.connamespace "
        "WHERE nsp.nspname = 'hde' AND cls.relname = 'body_graphs' "
        "ORDER BY con.conname",
        fetch=True,
    ),
    Statement(
        "SELECT table_schema, table_name, is_updatable, is_insertable_into, "
        "is_trigger_updatable, is_trigger_deletable, is_trigger_insertable_into "
        "FROM information_schema.views "
        "WHERE (table_schema = 'hde' AND table_name = 'body_graphs_current') "
        "OR (table_schema = 'public' AND table_name = 'hde_body_graphs_current') "
        "ORDER BY table_schema, table_name",
        fetch=True,
    ),
    Statement(
        "SELECT ns.nspname || '.' || cls.relname, part.partstrat, "
        "pg_get_partkeydef(part.partrelid) "
        "FROM pg_partitioned_table part "
        "JOIN pg_class cls ON cls.oid = part.partrelid "
        "JOIN pg_namespace ns ON ns.oid = cls.relnamespace "
        "WHERE ns.nspname = 'hde' AND cls.relname IN ('pair_evaluation','public_results') "
        "ORDER BY ns.nspname, cls.relname",
        fetch=True,
    ),
    Statement(
        "SELECT ns.nspname || '.' || cls.relname, cls.relkind = 'p' "
        "FROM pg_class cls JOIN pg_namespace ns ON ns.oid = cls.relnamespace "
        "WHERE ns.nspname = 'hde' AND cls.relname IN ('pair_evaluation','public_results') "
        "ORDER BY ns.nspname, cls.relname",
        fetch=True,
    ),
)


class Ops03Error(RuntimeError):
    def __init__(self, phase: str, code: str, *, consumed: bool):
        super().__init__(code)
        self.phase = phase
        self.code = code
        self.consumed = consumed


_DIR_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
_FILE_READ_FLAGS = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
_FILE_WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
_SAFE_PHASES = frozenset(("pre_marker", "pre_provider", "capture", "receipt_validation", "final_validation"))
_SAFE_CODE_RE = re.compile(r"^[a-z0-9_]{3,80}$")


@dataclass
class RunContext:
    run_id: str
    tmp_fd: int
    root_fd: int
    base_fd: int
    control_fd: int | None = None
    candidate_fd: int | None = None
    failure_fd: int | None = None
    launch_consumed: bool = False
    commit_transition_durable: bool = False
    failure_transition_durable: bool = False

    def close(self) -> None:
        for name in ("failure_fd", "candidate_fd", "control_fd", "base_fd", "root_fd", "tmp_fd"):
            fd = getattr(self, name)
            if fd is None:
                continue
            try:
                os.close(fd)
            except BaseException:
                pass
            setattr(self, name, None)


@dataclass(frozen=True)
class EnvironmentShape:
    names: frozenset[str]
    values: Mapping[str, str | None]
    database_url_present: bool


@dataclass
class ProviderChild:
    pid: int
    ready_fd: int
    launch_fd: int
    status_fd: int
    completed: bool = False


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


def _secure_mkdir_open(parent_fd: int, name: str) -> int:
    os.mkdir(name, mode=0o700, dir_fd=parent_fd)
    fd = _secure_open_dir(parent_fd, name)
    try:
        os.fsync(parent_fd)
        return fd
    except BaseException:
        os.close(fd)
        raise


def _open_run_root(*, create: bool) -> tuple[int, int]:
    if RUN_ROOT.parent != Path("/tmp") or RUN_ROOT.name != "hde-epic038-ops03":
        raise OSError("run_root_contract_mismatch")
    tmp_fd = os.open("/tmp", _DIR_FLAGS)
    try:
        try:
            root_fd = _secure_open_dir(tmp_fd, RUN_ROOT.name)
        except FileNotFoundError:
            if not create:
                raise
            root_fd = _secure_mkdir_open(tmp_fd, RUN_ROOT.name)
        root_stat = os.fstat(root_fd)
        if root_stat.st_uid != os.geteuid() or stat.S_IMODE(root_stat.st_mode) & 0o077:
            os.close(root_fd)
            raise OSError("unsafe_run_root_permissions")
        return tmp_fd, root_fd
    except BaseException:
        os.close(tmp_fd)
        raise


def _open_run_context(run_id: str, *, create_base: bool, allow_existing: bool = False) -> RunContext:
    if RUN_ID_RE.fullmatch(run_id) is None:
        raise Ops03Error("pre_marker", "authorization_schema_invalid", consumed=False)
    try:
        tmp_fd, root_fd = _open_run_root(create=True)
        try:
            try:
                base_fd = _secure_open_dir(root_fd, run_id)
                if not allow_existing:
                    os.close(base_fd)
                    raise Ops03Error("pre_marker", "authorization_already_consumed", consumed=False)
            except FileNotFoundError:
                if not create_base:
                    raise
                base_fd = _secure_mkdir_open(root_fd, run_id)
            if not _private_directory(base_fd):
                os.close(base_fd)
                raise OSError("unsafe_run_base_permissions")
            return RunContext(run_id, tmp_fd, root_fd, base_fd)
        except BaseException:
            os.close(root_fd)
            os.close(tmp_fd)
            raise
    except Ops03Error:
        raise
    except OSError as exc:
        raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False) from exc


def _private_directory(fd: int) -> bool:
    value = os.fstat(fd)
    return (
        stat.S_ISDIR(value.st_mode)
        and value.st_uid == os.geteuid()
        and stat.S_IMODE(value.st_mode) == 0o700
    )


def _assert_run_base_live(
    context: RunContext,
    *,
    phase: str = "capture",
    consumed: bool = True,
) -> None:
    if not all(
        (
            _entry_matches(context.tmp_fd, RUN_ROOT.name, context.root_fd),
            _entry_matches(context.root_fd, context.run_id, context.base_fd),
            _private_directory(context.root_fd),
            _private_directory(context.base_fd),
        )
    ):
        raise Ops03Error(phase, "run_root_generation_changed", consumed=consumed)


def _assert_context_live(
    context: RunContext,
    *,
    phase: str = "capture",
    consumed: bool = True,
) -> None:
    _assert_run_base_live(context, phase=phase, consumed=consumed)
    checks = [
        True,
    ]
    if context.control_fd is not None:
        checks.append(
            _entry_matches(context.base_fd, "control", context.control_fd)
            and _private_directory(context.control_fd)
        )
    if context.candidate_fd is not None:
        checks.append(
            _entry_matches(context.base_fd, "candidate", context.candidate_fd)
            and _private_directory(context.candidate_fd)
        )
    if context.failure_fd is not None:
        checks.append(
            _entry_matches(context.base_fd, "failure", context.failure_fd)
            and _private_directory(context.failure_fd)
        )
    if not all(checks):
        raise Ops03Error(phase, "run_root_generation_changed", consumed=consumed)


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("short_write")
        view = view[written:]


def _close_unneeded_child_fds(keep: set[int]) -> None:
    try:
        names = os.listdir("/proc/self/fd")
    except OSError as exc:
        raise OSError("child_fd_inventory_unavailable") from exc
    for name in names:
        try:
            fd = int(name)
        except ValueError:
            continue
        if fd in keep:
            continue
        try:
            os.close(fd)
        except OSError as exc:
            if exc.errno != errno.EBADF:
                raise OSError("child_fd_close_failed") from exc


def _write_new_file(dir_fd: int, name: str, payload: bytes) -> None:
    if not name or "/" in name or name in {".", ".."}:
        raise OSError("invalid_file_name")
    fd = os.open(name, _FILE_WRITE_FLAGS, 0o600, dir_fd=dir_fd)
    try:
        _write_all(fd, payload)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.fsync(dir_fd)


def _replace_file(dir_fd: int, name: str, payload: bytes) -> None:
    if not name or "/" in name or name in {".", ".."}:
        raise OSError("invalid_file_name")
    temporary = f".{name}.next"
    _write_new_file(dir_fd, temporary, payload)
    try:
        os.replace(
            temporary,
            name,
            src_dir_fd=dir_fd,
            dst_dir_fd=dir_fd,
        )
        os.fsync(dir_fd)
    except BaseException:
        try:
            os.unlink(temporary, dir_fd=dir_fd)
            os.fsync(dir_fd)
        except BaseException:
            pass
        raise


def _read_file(dir_fd: int, name: str) -> bytes:
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
                before_generation = (
                    before.st_dev,
                    before.st_ino,
                    before.st_size,
                    before.st_mtime_ns,
                    before.st_ctime_ns,
                )
                after_generation = (
                    after.st_dev,
                    after.st_ino,
                    after.st_size,
                    after.st_mtime_ns,
                    after.st_ctime_ns,
                )
                if (
                    before_generation != after_generation
                    or (linked_after.st_dev, linked_after.st_ino) != (after.st_dev, after.st_ino)
                    or stat.S_IFMT(linked_after.st_mode) != stat.S_IFREG
                    or len(payload) != after.st_size
                ):
                    raise OSError("file_generation_changed")
                return payload
            chunks.append(chunk)
    finally:
        os.close(fd)


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def derived_paths(run_id: str) -> tuple[Path, Path, Path, Path]:
    base = RUN_ROOT / run_id
    return base, base / "control", base / "candidate", base / "failure"


def _read_canonical_json(path: Path) -> tuple[Mapping[str, Any], bytes]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw.decode("utf-8", "strict"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Ops03Error("pre_marker", "authorization_unreadable", consumed=False) from exc
    if not isinstance(value, Mapping) or raw != canonical_bytes(value):
        raise Ops03Error("pre_marker", "authorization_not_canonical", consumed=False)
    return value, raw


def _read_json_noncanonical(path: Path) -> tuple[Any | None, bool, bytes]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw.decode("utf-8", "strict"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None, False, b""
    return value, raw == canonical_bytes(value), raw


def _authorization_is_stable(path: Path, expected: bytes) -> bool:
    try:
        return path.read_bytes() == expected
    except OSError:
        return False


def _runtime_invocation_valid(actual_argv: Sequence[str] | None, expected: Sequence[str]) -> bool:
    if actual_argv is None:
        return True
    return (
        list(actual_argv) == list(expected)
        and bool(sys.flags.isolated)
        and bool(sys.dont_write_bytecode)
    )


def _schema(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError("schema_not_mapping")
    return value


def _parse_utc(value: object) -> dt.datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.tzinfo == dt.timezone.utc else None


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


def validate_authorization(
    auth: Mapping[str, Any],
    auth_path: Path,
    *,
    now: dt.datetime | None = None,
) -> None:
    from tools.evidence.strict_json_schema import is_valid as schema_is_valid

    if not schema_is_valid(auth, _schema(AUTH_SCHEMA)):
        raise Ops03Error("pre_marker", "authorization_schema_invalid", consumed=False)
    run_id = str(auth["run_id"])
    _, _, candidate, _ = derived_paths(run_id)
    exact_values = (
        (auth["candidate_root"], candidate.as_posix() + "/", "candidate_root_mismatch"),
        (auth["retired_keys_required_absent"], list(RETIRED_DB_TRANSPORT_KEYS), "retired_key_roster_mismatch"),
        (auth["ordered_query_ids"], list(ORDERED_QUERY_IDS), "query_roster_mismatch"),
        (auth["expected_counts"], EXPECTED_COUNTS, "expected_counts_mismatch"),
        (auth["target"], {"app_env": "dev", "database_schema": "hde", "search_path": ["hde", "public"]}, "target_mismatch"),
        (auth["rails"], {"safe_mode": "1", "allow_network": "0", "allow_db_write": "0", "db_read_authorized": True}, "rails_mismatch"),
        (auth["exact_argv"], expected_argv(auth, auth_path, candidate), "argv_mismatch"),
    )
    for actual, expected, code in exact_values:
        if actual != expected:
            raise Ops03Error("pre_marker", code, consumed=False)
    authorized = _parse_utc(auth["authorized_at_utc"])
    expires = _parse_utc(auth["expires_at_utc"])
    current = now or dt.datetime.now(dt.timezone.utc)
    if authorized is None or expires is None or not (authorized < expires):
        raise Ops03Error("pre_marker", "authorization_window_invalid", consumed=False)
    if not (authorized <= current < expires):
        raise Ops03Error("pre_marker", "authorization_expired_or_not_active", consumed=False)


def _bootstrap_authorization_valid(auth: Any) -> bool:
    if not isinstance(auth, Mapping):
        return False
    run_id = auth.get("run_id")
    interpreter = auth.get("interpreter")
    return bool(
        isinstance(run_id, str)
        and RUN_ID_RE.fullmatch(run_id)
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
            parents.append((cursor, _stat_generation(info)))
        path = ROOT / relative_path
        before = path.lstat()
        if not stat.S_ISREG(before.st_mode):
            return None
        payload = path.read_bytes()
        after = path.lstat()
        if _stat_generation(before) != _stat_generation(after) or len(payload) != after.st_size:
            return None
        for parent, expected in parents:
            if _stat_generation(parent.lstat()) != expected:
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


def validate_source_identity(auth: Mapping[str, Any], *, enforce_repo: bool = True) -> None:
    interpreter = Path(sys.executable).resolve()
    checks = (
        (interpreter == Path(auth["interpreter"]["resolved_path"]).resolve(), "interpreter_path_mismatch"),
        (sha256_path(interpreter) == auth["interpreter"]["sha256"], "interpreter_hash_mismatch"),
        (sha256_path(RUNNER) == auth["runner_sha256"], "runner_hash_mismatch"),
        (sha256_path(VALIDATOR) == auth["validator_sha256"], "validator_hash_mismatch"),
    )
    for ok, code in checks:
        if not ok:
            raise Ops03Error("pre_marker", code, consumed=False)
    if not enforce_repo:
        return
    head = _git(("rev-parse", "HEAD"))
    if head.returncode or head.stdout.strip() != auth["source_commit"]:
        raise Ops03Error("pre_marker", "source_commit_mismatch", consumed=False)
    auxiliary_error = _source_manifest_auxiliary_error()
    if auxiliary_error is not None:
        raise Ops03Error("pre_marker", auxiliary_error, consumed=False)
    if any(ROOT.rglob("*.pyc")) or any(path.is_dir() for path in ROOT.rglob("__pycache__")):
        raise Ops03Error("pre_marker", "bytecode_residue_present", consumed=False)
    ignored_importable = _git(
        ("ls-files", "--others", "--ignored", "--exclude-standard", "--", "*.py", "*.pyw", "*.so", "*.pyd")
    )
    if ignored_importable.returncode or ignored_importable.stdout:
        raise Ops03Error("pre_marker", "ignored_native_module_present", consumed=False)



_EXPECTED_ENVIRONMENT = {
    "APP_ENV": "dev",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "ALLOW_DB_WRITE": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}


def _environment_shape(ambient: Mapping[str, str]) -> EnvironmentShape:
    names = frozenset(str(name) for name in ambient)
    values = {name: ambient.get(name) for name in _EXPECTED_ENVIRONMENT}
    return EnvironmentShape(names, values, "DATABASE_URL" in names)


def _validate_parent_environment(auth: Mapping[str, Any], shape: EnvironmentShape) -> None:
    retired = tuple(sorted(name for name in RETIRED_DB_TRANSPORT_KEYS if name in shape.names))
    if retired:
        raise Ops03Error("pre_marker", "retired_key_present", consumed=False)
    for name, value in _EXPECTED_ENVIRONMENT.items():
        if shape.values.get(name) != value:
            raise Ops03Error("pre_marker", f"environment_{name.lower()}_mismatch", consumed=False)
    if not shape.database_url_present:
        raise Ops03Error("pre_marker", "missing_database_url", consumed=False)
    if auth["rails"]["db_read_authorized"] is not True:
        raise Ops03Error("pre_marker", "db_read_not_authorized", consumed=False)
    allowed_names = {*_EXPECTED_ENVIRONMENT, "DATABASE_URL"}
    unexpected_names = sorted(shape.names - allowed_names)
    if unexpected_names:
        raise Ops03Error("pre_marker", "environment_not_clean", consumed=False)
    if any(name.startswith("PYTHON") for name in shape.names):
        raise Ops03Error("pre_marker", "python_environment_present", consumed=False)


def _child_db_environment(ambient: Mapping[str, str]) -> dict[str, str]:
    shape = _environment_shape(ambient)
    retired = tuple(sorted(name for name in RETIRED_DB_TRANSPORT_KEYS if name in shape.names))
    if retired:
        raise Ops03Error("pre_marker", "retired_key_present", consumed=False)
    for name, value in _EXPECTED_ENVIRONMENT.items():
        if shape.values.get(name) != value:
            raise Ops03Error("pre_marker", f"environment_{name.lower()}_mismatch", consumed=False)
    if sorted(shape.names - {*_EXPECTED_ENVIRONMENT, "DATABASE_URL"}):
        raise Ops03Error("pre_marker", "environment_not_clean", consumed=False)
    if any(name.startswith("PYTHON") for name in shape.names):
        raise Ops03Error("pre_marker", "python_environment_present", consumed=False)
    database_url = ambient.get("DATABASE_URL")
    if not isinstance(database_url, str) or not database_url.strip():
        raise Ops03Error("pre_marker", "missing_database_url", consumed=False)
    return {
        **_EXPECTED_ENVIRONMENT,
        "DATABASE_URL": database_url,
    }


def _clean_validator_environment() -> dict[str, str]:
    return {
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "ALLOW_DB_WRITE": "0",
    }


@dataclass
class Counters:
    provider_selections: int = 0
    health_connections: int = 0
    health_sql_statements: int = 0
    posture_transactions: int = 0
    posture_sql_statements: int = 0
    direct_connections: int = 0
    sql_statements: int = 0
    sql_writes: int = 0
    retries: int = 0
    alternate_provider_attempts: int = 0

    def as_dict(self) -> dict[str, int]:
        return {name: int(getattr(self, name)) for name in EXPECTED_COUNTS}


class CountingProvider:
    name = "psycopg"

    def __init__(self, inner: Any, counters: Counters, *, count_connections_by_call: bool):
        self._inner = inner
        self._counters = counters
        self._count_connections_by_call = count_connections_by_call

    def health(self) -> None:
        self._counters.health_connections += 1
        self._counters.health_sql_statements += 1
        self._counters.sql_statements += 1
        if self._count_connections_by_call:
            self._counters.direct_connections += 1
        self._inner.health()

    def readonly_tx(self, statements: Sequence[Statement]):
        self._counters.posture_transactions += 1
        self._counters.posture_sql_statements += len(statements)
        self._counters.sql_statements += len(statements)
        if self._count_connections_by_call:
            self._counters.direct_connections += 1
        return self._inner.readonly_tx(statements)

    def query(self, *args: Any, **kwargs: Any):
        return self._inner.query(*args, **kwargs)

    def exec(self, *args: Any, **kwargs: Any):
        return self._inner.exec(*args, **kwargs)

    def tx(self, *args: Any, **kwargs: Any):
        return self._inner.tx(*args, **kwargs)

    def introspect(self, *args: Any, **kwargs: Any):
        return self._inner.introspect(*args, **kwargs)


def _repo_db_symbols():
    from engine.db.adapter import DBAccess
    from engine.db.ddl_identity_projection import DDL_IDENTITY_PROJECTION_SCHEMA, project_ddl_identity
    from engine.db.providers.psycopg_provider import PsycopgProvider, validate_readonly_statements

    return DBAccess, DDL_IDENTITY_PROJECTION_SCHEMA, PsycopgProvider, project_ddl_identity, validate_readonly_statements


def _retained_text_is_unsafe(path: Path, payload: bytes) -> bool:
    from tools.evidence.retained_evidence_safety import validate_retained_text_safety

    return bool(validate_retained_text_safety(path, payload))


def live_provider_factory(counters: Counters) -> Callable[[str], CountingProvider]:
    def factory(dsn: str) -> CountingProvider:
        counters.provider_selections += 1

        def connect(value: str):
            import psycopg  # type: ignore

            counters.direct_connections += 1
            return psycopg.connect(value, connect_timeout=5)  # type: ignore[attr-defined]

        return CountingProvider(
            _repo_db_symbols()[2](dsn, connection_factory=connect),
            counters,
            count_connections_by_call=False,
        )

    return factory


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_json_safe(item) for item in value]
    return str(value)


def _rows(result: Sequence[Any] | None) -> list[list[Any]]:
    if result is None:
        return []
    return [_json_safe(list(row) if isinstance(row, Sequence) and not isinstance(row, str) else [row]) for row in result]


def _normalize_search_path(value: object) -> list[str]:
    return [part.strip() for part in str(value).split(",") if part.strip()]


def build_posture(
    auth: Mapping[str, Any],
    db: DBAccess,
    results: Sequence[Sequence[Any] | None],
    counters: Counters,
) -> dict[str, Any]:
    if len(results) != len(ORDERED_QUERY_IDS):
        raise Ops03Error("capture", "query_result_count_mismatch", consumed=True)
    rows = [_rows(result) for result in results]
    query_results = [
        {
            "query_id": query_id,
            "status": "ok",
            "row_count": len(value),
            "canonical_sha256": sha256_bytes(canonical_bytes(value)),
        }
        for query_id, value in zip(ORDERED_QUERY_IDS, rows)
    ]
    try:
        identity_row = rows[2][0]
        connection_identity_presence = bool(identity_row[0]) and bool(identity_row[1])
        read_only = bool(identity_row[2])
        search_path = _normalize_search_path(rows[3][0][0])
        role = rows[4][0]
        role_flags = {
            "rolsuper": bool(role[0]),
            "rolcreatedb": bool(role[1]),
            "rolcreaterole": bool(role[2]),
            "rolreplication": bool(role[3]),
            "rolbypassrls": bool(role[4]),
            "schema_create": bool(role[5]),
            "relation_write": bool(role[6]),
        }
        columns = [
            {
                "name": str(row[0]),
                "data_type": str(row[1]),
                "nullable": str(row[2]) == "YES",
                "default": " ".join(str(row[3] or "").split()),
            }
            for row in rows[5]
        ]
        boundaries = sorted(
            [
                {
                    "name": f"{row[0]}.{row[1]}",
                    "read_only": all(str(value).upper() == "NO" for value in row[2:7]),
                }
                for row in rows[7]
            ],
            key=lambda item: item["name"],
        )
        projection_input = [
            {"kind": "table", "name": "hde.body_graphs", "columns": columns},
            *({"kind": "view", "name": name} for name in EXPECTED_VIEWS),
        ]
        _DBAccess, DDL_IDENTITY_PROJECTION_SCHEMA, _PsycopgProvider, project_ddl_identity, _validate = _repo_db_symbols()
        projection = project_ddl_identity(projection_input)
        observed_partitions = sorted(str(row[0]) for row in rows[8])
        partition_definitions_exact = (
            len(rows[8]) == len(EXPECTED_PARTITION_DEFINITIONS)
            and all(
                len(row) == 3
                and str(row[0]) in EXPECTED_PARTITION_DEFINITIONS
                and (
                    str(row[1]).lower(),
                    " ".join(str(row[2]).split()),
                )
                == EXPECTED_PARTITION_DEFINITIONS[str(row[0])]
                for row in rows[8]
            )
        )
        verified_partitions = sorted(str(row[0]) for row in rows[9] if bool(row[1]))
    except (IndexError, TypeError, ValueError) as exc:
        raise Ops03Error("capture", "observation_shape_invalid", consumed=True) from exc
    observations = {
        "connection_identity_presence": connection_identity_presence,
        "search_path": search_path,
        "runtime_role_flags": role_flags,
        "ddl_identity": {
            "schema": DDL_IDENTITY_PROJECTION_SCHEMA,
            "canonical_sha256": sha256_bytes(canonical_bytes(projection)),
        },
        "constraint_count": len(rows[6]),
        "boundary_views": boundaries,
        "partition_posture": {
            "expected_tables": list(EXPECTED_PARTITIONS),
            "observed_tables": observed_partitions,
            "all_expected_present": (
                partition_definitions_exact
                and observed_partitions
                == list(EXPECTED_PARTITIONS)
                == verified_partitions
            ),
        },
    }
    predicates = {
        "authorization_match": True,
        "direct_provider_only": db.provider_name == "psycopg" and list(db.attempts) == [{"provider": "psycopg", "status": "ok", "reason": None}],
        "read_only_transaction": read_only,
        "search_path_exact": search_path == ["hde", "public"],
        "least_privilege_role": role_flags == {
            "rolsuper": False,
            "rolcreatedb": False,
            "rolcreaterole": False,
            "rolreplication": False,
            "rolbypassrls": False,
            "schema_create": False,
            "relation_write": False,
        },
        "ddl_identity_valid": bool(projection),
        "constraints_observed": len(rows[6]) >= 1,
        "boundary_views_readonly": boundaries == [{"name": "hde.body_graphs_current", "read_only": True}, {"name": "public.hde_body_graphs_current", "read_only": True}],
        "partition_posture_observed": observations["partition_posture"]["all_expected_present"],
        "counts_exact": counters.as_dict() == EXPECTED_COUNTS,
        "secret_values_absent": True,
    }
    if set(predicates) != set(POSTURE_PREDICATES) or not all(predicates.values()):
        raise Ops03Error("capture", "posture_predicate_failed", consumed=True)
    return {
        "schema": "hde_epic038.ops03.db_posture_summary.v1",
        "run_id": auth["run_id"],
        "source_commit": auth["source_commit"],
        "provider": "psycopg",
        "selection_attempts": list(db.attempts),
        "ordered_query_ids": list(ORDERED_QUERY_IDS),
        "query_results": query_results,
        "observations": observations,
        "counts": counters.as_dict(),
        "predicates": predicates,
        "result": "PASS",
    }



def _read_pipe(
    fd: int,
    *,
    limit: int = 4096,
    timeout_seconds: float | None = None,
) -> bytes:
    chunks: list[bytes] = []
    total = 0
    deadline = (
        None
        if timeout_seconds is None
        else time.monotonic() + max(0.0, timeout_seconds)
    )
    while True:
        if deadline is not None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("pipe_read_timeout")
            try:
                readable, _writable, _exceptional = select.select(
                    [fd],
                    [],
                    [],
                    remaining,
                )
            except InterruptedError:
                continue
            if not readable:
                raise TimeoutError("pipe_read_timeout")
        chunk = os.read(fd, 4096)
        if not chunk:
            return b"".join(chunks)
        total += len(chunk)
        if total > limit:
            raise OSError("pipe_payload_too_large")
        chunks.append(chunk)


def _failure_status(phase: str, code: str, *, consumed: bool) -> dict[str, Any]:
    return {
        "pid": os.getpid(),
        "parent_pid": os.getppid(),
        "result": "FAIL",
        "phase": phase,
        "code": code,
        "consumed": consumed,
    }


def _candidate_commit_record(
    files: Mapping[str, bytes],
    *,
    sealed: bool,
    finalized: bool,
    committed_payload: bytes | None = None,
) -> dict[str, Any]:
    names = FINAL_FILES if sealed else tuple(sorted(PRIMARY_FILES))
    record = {
        "schema": "hde_epic038.ops03.candidate_commit.v1",
        "sealed": sealed,
        "finalized": finalized,
        "files": {name: sha256_bytes(files[name]) for name in names},
    }
    if committed_payload is not None:
        record["committed_marker_sha256"] = sha256_bytes(committed_payload)
    return record


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


def _write_child_status(fd: int, status: Mapping[str, Any]) -> None:
    try:
        _write_all(fd, canonical_bytes(status))
    except BaseException:
        pass
    try:
        os.close(fd)
    except OSError:
        pass


def _runner_control_state_valid(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    candidate_commit: Mapping[str, Any] | None = None,
    committed_payload: bytes | None = None,
) -> bool:
    if context.control_fd is None:
        return False
    try:
        _assert_run_base_live(context, phase="pre_provider", consumed=True)
        if (
            not _entry_matches(context.base_fd, "control", context.control_fd)
            or not _private_directory(context.control_fd)
            or (context.candidate_fd is not None and not _candidate_entry_live(context, "candidate"))
            or tuple(sorted(os.listdir(context.base_fd))) != ("candidate", "control")
        ):
            return False
        control_names = (
            (COMMITTED_FILE, "authorization_consumed.json", "launch.marker")
            if committed_payload is not None
            else ("authorization_consumed.json", "launch.marker")
        )
        if tuple(sorted(os.listdir(context.control_fd))) != control_names:
            return False
        if _read_file(context.control_fd, "launch.marker") != b"launch_consumed=true\n":
            return False
        if committed_payload is not None and _read_file(
            context.control_fd,
            COMMITTED_FILE,
        ) != committed_payload:
            return False
        expected = _authorization_consumption(
            auth,
            authorization_sha256,
            candidate_commit=candidate_commit,
        )
        consumption_valid = _read_file(
            context.control_fd,
            "authorization_consumed.json",
        ) == canonical_bytes(expected)
        _assert_run_base_live(context, phase="pre_provider", consumed=True)
        if (
            not _entry_matches(context.base_fd, "control", context.control_fd)
            or not _private_directory(context.control_fd)
            or (context.candidate_fd is not None and not _candidate_entry_live(context, "candidate"))
            or tuple(sorted(os.listdir(context.base_fd))) != ("candidate", "control")
        ):
            return False
        return (
            consumption_valid
            and tuple(sorted(os.listdir(context.control_fd))) == control_names
        )
    except (OSError, Ops03Error, KeyError, TypeError):
        return False


def _provider_child_entry(
    auth_path: Path,
    ambient: Mapping[str, str],
    provider_factory_builder: Callable[[Counters], Callable[[str], Any]],
    now: dt.datetime | None,
    ready_fd: int,
    launch_fd: int,
    status_fd: int,
) -> None:
    context: RunContext | None = None
    ready_sent = False
    try:
        db_env = _child_db_environment(ambient)
        ambient = {}
        os.environ.clear()
        os.environ.update(db_env)
        _close_unneeded_child_fds({0, 1, 2, ready_fd, launch_fd, status_fd})
        _write_all(
            ready_fd,
            canonical_bytes({"pid": os.getpid(), "parent_pid": os.getppid(), "result": "READY"}),
        )
        os.close(ready_fd)
        ready_sent = True
        launch_raw = _read_pipe(launch_fd, limit=1024)
        os.close(launch_fd)
        if not launch_raw:
            os.close(status_fd)
            os._exit(0)
        launch = json.loads(launch_raw.decode("utf-8", "strict"))
        if not isinstance(launch, Mapping) or launch_raw != canonical_bytes(launch):
            raise Ops03Error("pre_provider", "provider_launch_token_invalid", consumed=True)
        auth, authorization_bytes = _read_canonical_json(auth_path)
        if not _bootstrap_authorization_valid(auth):
            raise Ops03Error("pre_provider", "authorization_schema_invalid", consumed=True)
        try:
            validate_source_identity(auth, enforce_repo=bool(launch.get("enforce_source")))
            validate_authorization(auth, auth_path, now=now)
        except Ops03Error as exc:
            raise Ops03Error("pre_provider", exc.code, consumed=True) from exc
        authorization_sha256 = sha256_bytes(authorization_bytes)
        expected_launch = {
            "run_id": auth["run_id"],
            "authorization_sha256": authorization_sha256,
            "parent_pid": os.getppid(),
            "enforce_source": bool(launch.get("enforce_source")),
        }
        if launch != expected_launch or not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("pre_provider", "provider_launch_token_invalid", consumed=True)
        _base, _control, candidate, _failure = derived_paths(str(auth["run_id"]))
        context = _open_run_context(str(auth["run_id"]), create_base=False, allow_existing=True)
        try:
            context.control_fd = _secure_open_dir(context.base_fd, "control")
            context.candidate_fd = _secure_open_dir(context.base_fd, "candidate")
        except OSError as exc:
            raise Ops03Error("pre_provider", "provider_context_invalid", consumed=True) from exc
        _assert_context_live(context)
        if not _runner_control_state_valid(context, auth, authorization_sha256):
            raise Ops03Error("pre_provider", "control_state_invalid", consumed=True)
        counters = Counters()
        provider_factory = provider_factory_builder(counters)
        DBAccess, _schema_name, _provider, _project, validate_readonly_statements = _repo_db_symbols()
        validate_readonly_statements(QUERY_STATEMENTS)
        db = DBAccess.for_current_env(environ=dict(os.environ), psycopg_factory=provider_factory)
        results = db.readonly_tx(QUERY_STATEMENTS)
        posture = build_posture(auth, db, results, counters)
        _write_capture_files(auth, authorization_sha256, candidate, posture, context)
        _write_child_status(
            status_fd,
            {"pid": os.getpid(), "parent_pid": os.getppid(), "result": "PASS"},
        )
        os._exit(0)
    except Ops03Error as exc:
        phase = "pre_marker" if not ready_sent else (exc.phase if exc.phase != "pre_marker" else "pre_provider")
        consumed = False if not ready_sent else True
        _write_child_status(
            status_fd if ready_sent else ready_fd,
            _failure_status(phase, exc.code, consumed=consumed),
        )
        os._exit(1)
    except BaseException:
        _write_child_status(
            status_fd if ready_sent else ready_fd,
            _failure_status(
                "capture" if ready_sent else "pre_marker",
                "unexpected_failure",
                consumed=ready_sent,
            ),
        )
        os._exit(1)
    finally:
        if context is not None:
            context.close()


def _parse_child_message(raw: bytes, pid: int) -> Mapping[str, Any]:
    try:
        value = json.loads(raw.decode("utf-8", "strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False) from exc
    if (
        not isinstance(value, Mapping)
        or raw != canonical_bytes(value)
        or value.get("pid") != pid
        or value.get("parent_pid") != os.getpid()
    ):
        raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False)
    return value


def _scrub_parent_database_url(*, required: bool = False) -> bool:
    try:
        del os.environ["DATABASE_URL"]
    except KeyError:
        pass
    except BaseException as exc:
        if required:
            raise Ops03Error(
                "pre_marker",
                "parent_database_url_scrub_failed",
                consumed=False,
            ) from exc
        return False
    try:
        present = any(str(name) == "DATABASE_URL" for name in os.environ.keys())
    except BaseException as exc:
        if required:
            raise Ops03Error(
                "pre_marker",
                "parent_database_url_scrub_failed",
                consumed=False,
            ) from exc
        return False
    if present and required:
        raise Ops03Error(
            "pre_marker",
            "parent_database_url_scrub_failed",
            consumed=False,
        )
    return not present


def _close_fd_quiet(fd: int) -> None:
    if fd < 0:
        return
    try:
        os.close(fd)
    except BaseException:
        pass


def _wait_for_child(pid: int, *, grace_seconds: float) -> bool:
    deadline = time.monotonic() + max(0.0, grace_seconds)
    while True:
        try:
            waited, _status = os.waitpid(pid, os.WNOHANG)
        except ChildProcessError:
            return True
        except InterruptedError:
            continue
        except BaseException:
            return False
        if waited == pid:
            return True
        if time.monotonic() >= deadline:
            return False
        time.sleep(0.01)


def _wait_for_child_status(pid: int, *, grace_seconds: float) -> int | None:
    deadline = time.monotonic() + max(0.0, grace_seconds)
    while True:
        try:
            waited, status = os.waitpid(pid, os.WNOHANG)
        except InterruptedError:
            continue
        except BaseException:
            return None
        if waited == pid:
            return status
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.01)


def _terminate_and_reap(pid: int, *, grace_seconds: float = 0.25) -> bool:
    if _wait_for_child(pid, grace_seconds=grace_seconds):
        return True
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return _wait_for_child(pid, grace_seconds=grace_seconds)
    except BaseException:
        pass
    if _wait_for_child(pid, grace_seconds=grace_seconds):
        return True
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        return _wait_for_child(pid, grace_seconds=grace_seconds)
    except BaseException:
        pass
    return _wait_for_child(pid, grace_seconds=grace_seconds)


def _spawn_provider_child(
    auth_path: Path,
    ambient: Mapping[str, str],
    provider_factory_builder: Callable[[Counters], Callable[[str], Any]],
    now: dt.datetime | None,
) -> tuple[ProviderChild, EnvironmentShape]:
    shape = _environment_shape(ambient)
    owned_fds: set[int] = set()
    pid: int | None = None
    try:
        ready_read, ready_write = os.pipe()
        owned_fds.update((ready_read, ready_write))
        launch_read, launch_write = os.pipe()
        owned_fds.update((launch_read, launch_write))
        status_read, status_write = os.pipe()
        owned_fds.update((status_read, status_write))
        pid = os.fork()
        if pid == 0:
            try:
                os.close(ready_read)
                os.close(launch_write)
                os.close(status_read)
            except BaseException:
                _write_child_status(
                    ready_write,
                    _failure_status("pre_marker", "provider_child_setup_failed", consumed=False),
                )
                os._exit(1)
            _provider_child_entry(
                auth_path,
                ambient,
                provider_factory_builder,
                now,
                ready_write,
                launch_read,
                status_write,
            )
            os._exit(1)

        for fd in (ready_write, launch_read, status_write):
            os.close(fd)
            owned_fds.discard(fd)
        child = ProviderChild(pid, ready_read, launch_write, status_read)
        _scrub_parent_database_url(required=True)
        ambient = {}
        owned_fds.clear()
        return child, shape
    except BaseException as exc:
        _scrub_parent_database_url()
        for fd in owned_fds:
            _close_fd_quiet(fd)
        if pid is not None and pid > 0:
            _terminate_and_reap(pid, grace_seconds=0.05)
        if isinstance(exc, Ops03Error):
            raise
        raise Ops03Error("pre_marker", "provider_child_setup_failed", consumed=False) from exc


def _await_provider_child_ready(child: ProviderChild) -> None:
    try:
        raw = _read_pipe(
            child.ready_fd,
            timeout_seconds=CHILD_READY_TIMEOUT_SECONDS,
        )
    except TimeoutError as exc:
        _abort_provider_child(child)
        raise Ops03Error(
            "pre_marker",
            "provider_child_ready_timeout",
            consumed=False,
        ) from exc
    except OSError as exc:
        _abort_provider_child(child)
        raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False) from exc
    finally:
        try:
            os.close(child.ready_fd)
        except OSError:
            pass
        child.ready_fd = -1
    try:
        message = _parse_child_message(raw, child.pid)
    except Ops03Error:
        _abort_provider_child(child)
        raise
    if message.get("result") == "READY" and set(message) == {"pid", "parent_pid", "result"}:
        return
    _abort_provider_child(child)
    code = message.get("code")
    if (
        message.get("result") == "FAIL"
        and message.get("phase") == "pre_marker"
        and message.get("consumed") is False
        and isinstance(code, str)
        and _SAFE_CODE_RE.fullmatch(code)
    ):
        raise Ops03Error("pre_marker", code, consumed=False)
    raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False)


def _abort_provider_child(child: ProviderChild) -> None:
    if child.completed:
        return
    for name in ("ready_fd", "launch_fd", "status_fd"):
        fd = getattr(child, name)
        if fd < 0:
            continue
        _close_fd_quiet(fd)
        setattr(child, name, -1)
    try:
        _terminate_and_reap(child.pid)
    except BaseException:
        pass
    finally:
        child.completed = True


def _launch_provider_child(
    child: ProviderChild,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    enforce_source: bool,
) -> None:
    token = {
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "parent_pid": os.getpid(),
        "enforce_source": enforce_source,
    }
    try:
        _write_all(child.launch_fd, canonical_bytes(token))
    except OSError as exc:
        raise Ops03Error("pre_provider", "provider_child_launch_failed", consumed=True) from exc
    finally:
        try:
            os.close(child.launch_fd)
        except OSError:
            pass
        child.launch_fd = -1
    try:
        raw = _read_pipe(
            child.status_fd,
            timeout_seconds=PROVIDER_CHILD_TIMEOUT_SECONDS,
        )
    except TimeoutError as exc:
        _abort_provider_child(child)
        raise Ops03Error(
            "capture",
            "provider_child_timeout",
            consumed=True,
        ) from exc
    except OSError as exc:
        raise Ops03Error("capture", "provider_child_status_invalid", consumed=True) from exc
    finally:
        try:
            os.close(child.status_fd)
        except OSError:
            pass
        child.status_fd = -1
    wait_status = _wait_for_child_status(
        child.pid,
        grace_seconds=PROVIDER_REAP_TIMEOUT_SECONDS,
    )
    if wait_status is None:
        _abort_provider_child(child)
        raise Ops03Error(
            "capture",
            "provider_child_reap_timeout",
            consumed=True,
        )
    child.completed = True
    exit_code = os.waitstatus_to_exitcode(wait_status)
    try:
        message = _parse_child_message(raw, child.pid)
    except Ops03Error as exc:
        raise Ops03Error("capture", exc.code, consumed=True) from exc
    if exit_code == 0 and message == {"pid": child.pid, "parent_pid": os.getpid(), "result": "PASS"}:
        return
    code = message.get("code")
    phase = message.get("phase")
    if (
        exit_code != 0
        and message.get("result") == "FAIL"
        and phase in {"pre_provider", "capture", "receipt_validation", "final_validation"}
        and isinstance(code, str)
        and _SAFE_CODE_RE.fullmatch(code)
        and message.get("consumed") is True
    ):
        raise Ops03Error(str(phase), code, consumed=True)
    raise Ops03Error("capture", "provider_child_status_invalid", consumed=True)

def _write_capture_files(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    candidate: Path,
    posture: Mapping[str, Any],
    context: RunContext,
) -> None:
    env = {
        "schema": "hde_epic038.ops03.env_presence.v1",
        "run_id": auth["run_id"],
        "app_env": "dev",
        "rails": auth["rails"],
        "database_url_presence": "SET_REDACTED",
        "retired_key_presence": {name: "UNSET" for name in RETIRED_DB_TRANSPORT_KEYS},
        "determinism_pins": {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
    }
    nonclaims = {"schema": "hde_epic038.ops03.nonclaims.v1", "run_id": auth["run_id"], "nonclaims": list(NONCLAIMS)}
    summary = {
        "schema": "hde_epic038.ops03.result_summary.v1",
        "run_id": auth["run_id"],
        "source_commit": auth["source_commit"],
        "authorization_sha256": authorization_sha256,
        "capture_result": "PASS",
        "decisive_predicates": posture["predicates"],
        "primary_files": list(PRIMARY_FILES),
        "nonclaims_ref": "nonclaims.json",
    }
    commands = "".join(
        f"{name}_argv={json.dumps(auth['exact_argv'][name], sort_keys=True, separators=(',', ':'))}\n"
        for name in ("capture", "receipt", "validate")
    )
    files: dict[str, bytes] = {
        "commands.txt": commands.encode("utf-8"),
        "db_posture_summary.json": canonical_bytes(posture),
        "env_presence.json": canonical_bytes(env),
        "exit_code.txt": b"0\n",
        "nonclaims.json": canonical_bytes(nonclaims),
        "result_summary.json": canonical_bytes(summary),
        "stderr.log": b"",
        "stdout.log": b"OPS03_CAPTURE_PASS\n",
    }
    if tuple(sorted(files)) != tuple(sorted(PRIMARY_FILES)):
        raise Ops03Error("capture", "primary_inventory_internal_error", consumed=True)
    if context.candidate_fd is None:
        raise Ops03Error("capture", "candidate_root_unavailable", consumed=True)
    for name, payload in files.items():
        if _retained_text_is_unsafe(candidate / name, payload):
            raise Ops03Error("capture", "secret_scan_failed", consumed=True)
        _assert_context_live(context)
        try:
            _write_new_file(context.candidate_fd, name, payload)
        except OSError as exc:
            raise Ops03Error("capture", "candidate_write_failed", consumed=True) from exc
        _assert_context_live(context)


def _context_for_candidate(candidate: Path) -> RunContext:
    absolute = Path(os.path.abspath(candidate))
    run_id = absolute.parent.name
    if absolute != RUN_ROOT / run_id / "candidate":
        raise Ops03Error("final_validation", "candidate_root_mismatch", consumed=True)
    context = _open_run_context(run_id, create_base=False, allow_existing=True)
    try:
        context.control_fd = _secure_open_dir(context.base_fd, "control")
        context.candidate_fd = _secure_open_dir(context.base_fd, "candidate")
        _assert_context_live(context)
        return context
    except BaseException:
        context.close()
        raise


def write_checksums(candidate: Path, *, context: RunContext | None = None) -> None:
    owned = context is None
    active = _context_for_candidate(candidate) if owned else context
    if active is None or active.candidate_fd is None:
        raise Ops03Error("final_validation", "candidate_root_unavailable", consumed=True)
    try:
        _assert_context_live(active)
        lines = [f"{sha256_bytes(_read_file(active.candidate_fd, name))}  {name}\n" for name in CHECKSUM_INPUTS]
        try:
            os.unlink("checksums.sha256", dir_fd=active.candidate_fd)
        except FileNotFoundError:
            pass
        _write_new_file(active.candidate_fd, "checksums.sha256", "".join(lines).encode("ascii"))
        _assert_context_live(active)
    except OSError as exc:
        raise Ops03Error("final_validation", "checksum_write_failed", consumed=True) from exc
    finally:
        if owned:
            active.close()


def _run_validator(
    argv: Sequence[str],
    *,
    pending_token: bytes,
) -> Mapping[str, Any] | None:
    phase = "receipt_validation" if "--emit-receipt" in argv else "final_validation"
    try:
        completed = subprocess.run(
            list(argv),
            check=False,
            capture_output=True,
            env=_clean_validator_environment(),
            input=pending_token,
            timeout=VALIDATOR_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise Ops03Error(
            phase,
            "independent_validator_timeout",
            consumed=True,
        ) from exc
    if completed.returncode:
        raise Ops03Error(
            phase,
            "independent_validator_failed",
            consumed=True,
        )
    if "--validate" not in argv:
        if completed.stdout:
            raise Ops03Error(
                "receipt_validation",
                "independent_validator_output_invalid",
                consumed=True,
            )
        return None
    try:
        attestation = json.loads(completed.stdout.decode("utf-8", "strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Ops03Error(
            "final_validation",
            "independent_validator_output_invalid",
            consumed=True,
        ) from exc
    if not isinstance(attestation, Mapping) or completed.stdout != canonical_bytes(attestation):
        raise Ops03Error(
            "final_validation",
            "independent_validator_output_invalid",
            consumed=True,
        )
    return attestation


def _write_marker(context: RunContext, auth: Mapping[str, Any], authorization_sha256: str) -> None:
    try:
        context.control_fd = _secure_mkdir_open(context.base_fd, "control")
    except OSError as exc:
        raise Ops03Error("pre_marker", "control_root_unwritable", consumed=False) from exc
    _assert_context_live(context, phase="pre_marker", consumed=False)
    marker_persisted = False
    marker_payload = b"launch_consumed=true\n"
    try:
        _write_new_file(context.control_fd, "launch.marker", marker_payload)
        marker_persisted = True
        context.launch_consumed = True
    except BaseException as exc:
        try:
            marker_persisted = _read_file(context.control_fd, "launch.marker") == marker_payload
        except FileNotFoundError:
            marker_persisted = False
        except BaseException:
            marker_persisted = True
        if not marker_persisted:
            try:
                try:
                    os.unlink("launch.marker", dir_fd=context.control_fd)
                except FileNotFoundError:
                    pass
                os.fsync(context.control_fd)
                try:
                    os.stat("launch.marker", dir_fd=context.control_fd, follow_symlinks=False)
                except FileNotFoundError:
                    marker_persisted = False
                else:
                    marker_persisted = True
            except BaseException:
                marker_persisted = True
        context.launch_consumed = marker_persisted
        raise Ops03Error(
            "pre_provider" if marker_persisted else "pre_marker",
            "launch_marker_write_failed",
            consumed=marker_persisted,
        ) from exc
    consumption = _authorization_consumption(auth, authorization_sha256)
    try:
        _write_new_file(context.control_fd, "authorization_consumed.json", canonical_bytes(consumption))
    except OSError as exc:
        raise Ops03Error("pre_provider", "authorization_consumption_record_write_failed", consumed=True) from exc
    try:
        control_inventory = tuple(sorted(os.listdir(context.control_fd)))
    except OSError as exc:
        raise Ops03Error("pre_provider", "control_inventory_unreadable", consumed=True) from exc
    if control_inventory != ("authorization_consumed.json", "launch.marker"):
        raise Ops03Error("pre_provider", "control_inventory_invalid", consumed=True)
    _assert_context_live(context, phase="pre_provider", consumed=True)


def write_failure(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    phase: str,
    code: str,
    consumed: bool,
    context: RunContext | None = None,
) -> bool:
    run_id = auth.get("run_id")
    if (
        not isinstance(run_id, str)
        or RUN_ID_RE.fullmatch(run_id) is None
        or not re.fullmatch(r"[0-9a-f]{64}", authorization_sha256)
        or phase not in _SAFE_PHASES
        or _SAFE_CODE_RE.fullmatch(code) is None
    ):
        return False
    receipt = {
        "schema": "hde_epic038.ops03.failure_receipt.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "phase": phase,
        "code": code,
        "launch_consumed": consumed,
        "candidate_admissible": False,
        "nonclaims": list(NONCLAIMS),
    }
    for attempt in range(2):
        try:
            active = _open_run_context(
                run_id,
                create_base=context is None and attempt == 0,
                allow_existing=context is not None or attempt > 0,
            )
        except (Ops03Error, OSError):
            return False
        try:
            _assert_run_base_live(active, phase=phase, consumed=consumed)
            try:
                active.failure_fd = _secure_mkdir_open(active.base_fd, "failure")
            except FileExistsError:
                return False
            _assert_context_live(active, phase=phase, consumed=consumed)
            _write_new_file(active.failure_fd, "failure_receipt.json", canonical_bytes(receipt))
            _assert_context_live(active, phase=phase, consumed=consumed)
            return True
        except (OSError, Ops03Error):
            try:
                os.stat("failure", dir_fd=active.base_fd, follow_symlinks=False)
                return False
            except FileNotFoundError:
                if attempt:
                    return False
            except OSError:
                return False
        finally:
            active.close()
    return False


def _pending_payload(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    pending_token: bytes,
) -> bytes:
    if len(pending_token) != 32:
        raise OSError("pending_token_invalid")
    return canonical_bytes(
        {
            "schema": "hde_epic038.ops03.capture_pending.v1",
            "run_id": auth["run_id"],
            "authorization_sha256": authorization_sha256,
            "runner_pid": os.getpid(),
            "runner_token_sha256": sha256_bytes(pending_token),
        }
    )


def _create_pending_latch(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    pending_token: bytes,
) -> None:
    if context.candidate_fd is None:
        raise Ops03Error("capture", "candidate_root_unavailable", consumed=True)
    try:
        _assert_context_live(context)
        _write_new_file(
            context.candidate_fd,
            PENDING_FILE,
            _pending_payload(auth, authorization_sha256, pending_token),
        )
        _assert_context_live(context)
        context.failure_transition_durable = True
    except OSError as exc:
        raise Ops03Error("capture", "candidate_pending_latch_failed", consumed=True) from exc


def _stat_generation(value: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


def _candidate_entry_live(context: RunContext, name: str) -> bool:
    return bool(
        context.candidate_fd is not None
        and _entry_matches(context.base_fd, name, context.candidate_fd)
        and _private_directory(context.candidate_fd)
    )


def _snapshot_candidate_files(
    context: RunContext,
) -> dict[str, bytes]:
    if context.candidate_fd is None:
        raise OSError("candidate_root_unavailable")
    _assert_run_base_live(context)
    if not _candidate_entry_live(context, "candidate"):
        raise OSError("candidate_generation_changed")
    initial_names = tuple(sorted(os.listdir(context.candidate_fd)))
    files: dict[str, bytes] = {}
    generations: dict[str, tuple[int, int, int, int, int, int]] = {}
    for name in initial_names:
        info = os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode):
            raise OSError("candidate_entry_not_regular")
        files[name] = _read_file(context.candidate_fd, name)
        generations[name] = _stat_generation(
            os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)
        )
    if tuple(sorted(os.listdir(context.candidate_fd))) != initial_names:
        raise OSError("candidate_inventory_changed")
    for name, expected in generations.items():
        if _stat_generation(os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)) != expected:
            raise OSError("candidate_file_generation_changed")
    _assert_run_base_live(context)
    if not _candidate_entry_live(context, "candidate"):
        raise OSError("candidate_generation_changed")
    return files


def _candidate_attestation(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    files: Mapping[str, bytes],
) -> dict[str, Any]:
    return {
        "schema": "hde_epic038.ops03.candidate_attestation.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "files": {name: sha256_bytes(files[name]) for name in FINAL_FILES},
    }


def _runner_failure_state_present(context: RunContext) -> bool:
    try:
        os.stat("failure", dir_fd=context.base_fd, follow_symlinks=False)
        return True
    except FileNotFoundError:
        return False
    except OSError:
        return True


def _run_base_inventory_valid(context: RunContext) -> bool:
    try:
        _assert_context_live(context, phase="final_validation", consumed=True)
        return tuple(sorted(os.listdir(context.base_fd))) == ("candidate", "control")
    except (OSError, Ops03Error):
        return False


def _write_candidate_commit_control(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    candidate_commit: Mapping[str, Any],
) -> None:
    if context.control_fd is None:
        raise Ops03Error(
            "final_validation",
            "candidate_commit_control_unavailable",
            consumed=True,
        )
    try:
        _replace_file(
            context.control_fd,
            "authorization_consumed.json",
            canonical_bytes(
                _authorization_consumption(
                    auth,
                    authorization_sha256,
                    candidate_commit=candidate_commit,
                )
            ),
        )
    except BaseException as exc:
        raise Ops03Error(
            "final_validation",
            "candidate_commit_control_write_failed",
            consumed=True,
        ) from exc


def _invalidate_candidate_commit_control(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
) -> bool:
    if context.control_fd is None:
        return False
    try:
        _replace_file(
            context.control_fd,
            "authorization_consumed.json",
            canonical_bytes(_authorization_consumption(auth, authorization_sha256)),
        )
        context.commit_transition_durable = False
        context.failure_transition_durable = True
        return _runner_control_state_valid(
            context,
            auth,
            authorization_sha256,
        )
    except BaseException:
        return False


def _committed_candidate_visible(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
    attestation: Mapping[str, Any] | None,
    committed_payload: bytes,
    *,
    sealed: bool,
) -> bool:
    retained_names = FINAL_FILES if sealed else tuple(sorted(PRIMARY_FILES))
    try:
        if (
            not _run_base_inventory_valid(context)
            or _runner_failure_state_present(context)
        ):
            return False
        files = _snapshot_candidate_files(context)
        if tuple(sorted(files)) != tuple(sorted(retained_names)):
            return False
        if sealed and attestation != _candidate_attestation(
            auth,
            authorization_sha256,
            files,
        ):
            return False
        commit_record = _candidate_commit_record(
            files,
            sealed=sealed,
            finalized=True,
            committed_payload=committed_payload,
        )
        return _runner_control_state_valid(
            context,
            auth,
            authorization_sha256,
            candidate_commit=commit_record,
            committed_payload=committed_payload,
        )
    except BaseException:
        return False


def _terminal_success_visible(
    context: RunContext,
    auth: Mapping[str, Any],
    auth_path: Path,
    authorization_bytes: bytes,
    authorization_sha256: str,
    attestation: Mapping[str, Any] | None,
    committed_payload: bytes,
    *,
    sealed: bool,
    enforce_source: bool,
) -> bool:
    try:
        if not _committed_candidate_visible(
            context,
            auth,
            authorization_sha256,
            attestation,
            committed_payload,
            sealed=sealed,
        ):
            return False
        if not _authorization_is_stable(auth_path, authorization_bytes):
            return False
        validate_source_identity(auth, enforce_repo=enforce_source)
        return (
            _authorization_is_stable(auth_path, authorization_bytes)
            and _committed_candidate_visible(
                context,
                auth,
                authorization_sha256,
                attestation,
                committed_payload,
                sealed=sealed,
            )
        )
    except BaseException:
        return False


def _finalization_ready_visible(
    context: RunContext,
    auth: Mapping[str, Any],
    auth_path: Path,
    authorization_bytes: bytes,
    authorization_sha256: str,
    pending_payload: bytes,
    retained: Mapping[str, bytes],
    *,
    sealed: bool,
    enforce_source: bool,
) -> bool:
    expected_files = {**retained, PENDING_FILE: pending_payload}
    finalized_commit = _candidate_commit_record(
        retained,
        sealed=sealed,
        finalized=True,
        committed_payload=pending_payload,
    )

    def state_visible() -> bool:
        return bool(
            _run_base_inventory_valid(context)
            and not _runner_failure_state_present(context)
            and _snapshot_candidate_files(context) == expected_files
            and _runner_control_state_valid(
                context,
                auth,
                authorization_sha256,
                candidate_commit=finalized_commit,
            )
        )

    try:
        if not state_visible() or not _authorization_is_stable(
            auth_path,
            authorization_bytes,
        ):
            return False
        validate_source_identity(auth, enforce_repo=enforce_source)
        return (
            _authorization_is_stable(auth_path, authorization_bytes)
            and state_visible()
        )
    except BaseException:
        return False


def _transition_entry_state(
    context: RunContext,
    pending_payload: bytes,
    *,
    committed: bool,
) -> bool:
    if context.candidate_fd is None or context.control_fd is None:
        return False
    try:
        pending_value: bytes | None
        committed_value: bytes | None
        try:
            pending_value = _read_file(context.candidate_fd, PENDING_FILE)
        except FileNotFoundError:
            pending_value = None
        try:
            committed_value = _read_file(context.control_fd, COMMITTED_FILE)
        except FileNotFoundError:
            committed_value = None
        if committed:
            return pending_value is None and committed_value == pending_payload
        return pending_value == pending_payload and committed_value is None
    except BaseException:
        return False


def _rename_result_visible(
    source_fd: int,
    source_name: str,
    destination_fd: int,
    destination_name: str,
    source_stat: os.stat_result,
) -> bool:
    try:
        os.stat(source_name, dir_fd=source_fd, follow_symlinks=False)
        return False
    except FileNotFoundError:
        pass
    except BaseException:
        return False
    try:
        destination_stat = os.stat(
            destination_name,
            dir_fd=destination_fd,
            follow_symlinks=False,
        )
    except BaseException:
        return False
    return (destination_stat.st_dev, destination_stat.st_ino) == (
        source_stat.st_dev,
        source_stat.st_ino,
    )


def _sync_directory_fds(*fds: int) -> bool:
    unique_fds = tuple(dict.fromkeys(fds))

    def sync_each() -> bool:
        durable = True
        for fd in unique_fds:
            try:
                os.fsync(fd)
            except BaseException:
                durable = False
        return durable

    if sync_each():
        return True
    # A process-wide sync cannot attest persistence for these directory entries.
    # Retry each exact descriptor once and fail closed unless every retry succeeds.
    return sync_each()


def _control_failure_transition_visible(
    context: RunContext,
    pending_payload: bytes,
) -> bool:
    if context.control_fd is None:
        return False
    try:
        return _read_file(
            context.control_fd,
            FAILED_COMMIT_FILE,
        ) == pending_payload
    except BaseException:
        return False


def _move_committed_to_failure(
    context: RunContext,
    pending_payload: bytes,
    source_stat: os.stat_result,
) -> bool:
    if context.control_fd is None:
        return False
    try:
        os.rename(
            COMMITTED_FILE,
            FAILED_COMMIT_FILE,
            src_dir_fd=context.control_fd,
            dst_dir_fd=context.control_fd,
        )
    except BaseException:
        moved = _rename_result_visible(
            context.control_fd,
            COMMITTED_FILE,
            context.control_fd,
            FAILED_COMMIT_FILE,
            source_stat,
        ) or _control_failure_transition_visible(context, pending_payload)
        if not moved:
            return False
    durable = _sync_directory_fds(context.control_fd)
    if durable:
        context.commit_transition_durable = False
        context.failure_transition_durable = True
    return durable


def _move_pending_to_failure(
    context: RunContext,
    pending_payload: bytes,
) -> bool:
    if context.candidate_fd is None or context.control_fd is None:
        return False
    try:
        source_stat = os.stat(
            PENDING_FILE,
            dir_fd=context.candidate_fd,
            follow_symlinks=False,
        )
    except BaseException:
        visible = _control_failure_transition_visible(context, pending_payload)
        durable = visible and _sync_directory_fds(context.control_fd)
        if durable:
            context.commit_transition_durable = False
            context.failure_transition_durable = True
        return durable
    try:
        os.rename(
            PENDING_FILE,
            FAILED_COMMIT_FILE,
            src_dir_fd=context.candidate_fd,
            dst_dir_fd=context.control_fd,
        )
    except BaseException:
        moved = _rename_result_visible(
            context.candidate_fd,
            PENDING_FILE,
            context.control_fd,
            FAILED_COMMIT_FILE,
            source_stat,
        ) or _control_failure_transition_visible(context, pending_payload)
        if not moved:
            return False
    durable = _sync_directory_fds(context.candidate_fd, context.control_fd)
    if durable:
        context.commit_transition_durable = False
        context.failure_transition_durable = True
    return durable


def _move_pending_to_committed(
    context: RunContext,
    pending_payload: bytes,
) -> None:
    if context.candidate_fd is None or context.control_fd is None:
        raise Ops03Error(
            "final_validation",
            "candidate_commit_control_unavailable",
            consumed=True,
        )
    try:
        source_stat = os.stat(
            PENDING_FILE,
            dir_fd=context.candidate_fd,
            follow_symlinks=False,
        )
    except BaseException as exc:
        raise Ops03Error(
            "final_validation",
            "candidate_commit_failed",
            consumed=True,
        ) from exc
    try:
        os.rename(
            PENDING_FILE,
            COMMITTED_FILE,
            src_dir_fd=context.candidate_fd,
            dst_dir_fd=context.control_fd,
        )
    except BaseException as exc:
        if not (
            _rename_result_visible(
                context.candidate_fd,
                PENDING_FILE,
                context.control_fd,
                COMMITTED_FILE,
                source_stat,
            )
            or _transition_entry_state(context, pending_payload, committed=True)
        ):
            if _transition_entry_state(context, pending_payload, committed=False):
                raise Ops03Error(
                    "final_validation",
                    "candidate_commit_failed",
                    consumed=True,
                ) from exc
            raise Ops03Error(
                "final_validation",
                "candidate_commit_failed",
                consumed=True,
            ) from exc
    if not _sync_directory_fds(context.candidate_fd, context.control_fd):
        _move_committed_to_pending(context, pending_payload)
        raise Ops03Error(
            "final_validation",
            "candidate_commit_failed",
            consumed=True,
        )
    context.commit_transition_durable = True
    context.failure_transition_durable = False


def _move_committed_to_pending(
    context: RunContext,
    pending_payload: bytes,
) -> bool:
    if context.candidate_fd is None or context.control_fd is None:
        return False
    try:
        source_stat = os.stat(
            COMMITTED_FILE,
            dir_fd=context.control_fd,
            follow_symlinks=False,
        )
    except BaseException:
        visible = _control_failure_transition_visible(context, pending_payload)
        durable = visible and _sync_directory_fds(context.control_fd)
        if durable:
            context.commit_transition_durable = False
            context.failure_transition_durable = True
        return durable
    try:
        os.rename(
            COMMITTED_FILE,
            PENDING_FILE,
            src_dir_fd=context.control_fd,
            dst_dir_fd=context.candidate_fd,
        )
    except BaseException:
        restored = _rename_result_visible(
            context.control_fd,
            COMMITTED_FILE,
            context.candidate_fd,
            PENDING_FILE,
            source_stat,
        ) or _transition_entry_state(context, pending_payload, committed=False)
        if not restored:
            return _move_committed_to_failure(
                context,
                pending_payload,
                source_stat,
            )
    durable = _sync_directory_fds(context.control_fd, context.candidate_fd)
    if not durable:
        return _move_pending_to_failure(context, pending_payload)
    context.commit_transition_durable = False
    context.failure_transition_durable = True
    return True


def _commit_candidate(
    context: RunContext,
    auth: Mapping[str, Any],
    auth_path: Path,
    authorization_bytes: bytes,
    authorization_sha256: str,
    pending_token: bytes,
    attestation: Mapping[str, Any] | None,
    *,
    sealed: bool,
    enforce_source: bool,
) -> None:
    if context.candidate_fd is None:
        raise Ops03Error("final_validation", "candidate_root_unavailable", consumed=True)
    retained_names = FINAL_FILES if sealed else tuple(sorted(PRIMARY_FILES))
    expected_names = tuple(sorted((*retained_names, PENDING_FILE)))
    expected_pending = _pending_payload(auth, authorization_sha256, pending_token)
    try:
        _assert_context_live(context, phase="final_validation", consumed=True)
        if (
            not _run_base_inventory_valid(context)
            or _runner_failure_state_present(context)
            or not _runner_control_state_valid(context, auth, authorization_sha256)
        ):
            raise Ops03Error("final_validation", "candidate_commit_pre_state_invalid", consumed=True)
        files = _snapshot_candidate_files(context)
        if tuple(sorted(files)) != expected_names or files.get(PENDING_FILE) != expected_pending:
            raise Ops03Error("final_validation", "candidate_commit_inventory_invalid", consumed=True)
        retained = {name: files[name] for name in retained_names}
        if sealed and attestation != _candidate_attestation(auth, authorization_sha256, retained):
            raise Ops03Error("final_validation", "candidate_attestation_mismatch", consumed=True)
        final_files = _snapshot_candidate_files(context)
        if final_files != files:
            raise Ops03Error("final_validation", "candidate_commit_snapshot_changed", consumed=True)
        if (
            not _run_base_inventory_valid(context)
            or _runner_failure_state_present(context)
            or not _runner_control_state_valid(context, auth, authorization_sha256)
        ):
            raise Ops03Error("final_validation", "candidate_commit_final_state_invalid", consumed=True)
        pending_commit_record = _candidate_commit_record(
            retained,
            sealed=sealed,
            finalized=False,
        )
        _write_candidate_commit_control(
            context,
            auth,
            authorization_sha256,
            pending_commit_record,
        )
        if (
            _snapshot_candidate_files(context) != files
            or not _run_base_inventory_valid(context)
            or _runner_failure_state_present(context)
            or not _runner_control_state_valid(
                context,
                auth,
                authorization_sha256,
                candidate_commit=pending_commit_record,
            )
        ):
            raise Ops03Error(
                "final_validation",
                "candidate_commit_manifest_state_invalid",
                consumed=True,
            )
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error(
                "final_validation",
                "authorization_bytes_changed",
                consumed=True,
            )
        try:
            validate_source_identity(auth, enforce_repo=enforce_source)
        except Ops03Error as exc:
            raise Ops03Error("final_validation", exc.code, consumed=True) from exc
        finalized_commit_record = _candidate_commit_record(
            retained,
            sealed=sealed,
            finalized=True,
            committed_payload=expected_pending,
        )
        _write_candidate_commit_control(
            context,
            auth,
            authorization_sha256,
            finalized_commit_record,
        )
        if not _finalization_ready_visible(
            context,
            auth,
            auth_path,
            authorization_bytes,
            authorization_sha256,
            expected_pending,
            retained,
            sealed=sealed,
            enforce_source=enforce_source,
        ):
            raise Ops03Error(
                "final_validation",
                "candidate_commit_finalized_state_invalid",
                consumed=True,
            )
        _move_pending_to_committed(context, expected_pending)
        if not _terminal_success_visible(
            context,
            auth,
            auth_path,
            authorization_bytes,
            authorization_sha256,
            attestation,
            expected_pending,
            sealed=sealed,
            enforce_source=enforce_source,
        ):
            context.commit_transition_durable = False
            _move_committed_to_pending(context, expected_pending)
            raise Ops03Error(
                "final_validation",
                "candidate_commit_finalized_state_invalid",
                consumed=True,
            )
        return
    except Ops03Error:
        raise
    except BaseException as exc:
        raise Ops03Error("final_validation", "candidate_commit_failed", consumed=True) from exc


def _discard_candidate(context: RunContext) -> bool:
    if context.candidate_fd is None:
        return True
    try:
        _assert_context_live(context)
        names = sorted(
            os.listdir(context.candidate_fd),
            key=lambda name: (name == PENDING_FILE, name),
        )
        for name in names:
            entry = os.stat(name, dir_fd=context.candidate_fd, follow_symlinks=False)
            if stat.S_ISDIR(entry.st_mode):
                return False
            os.unlink(name, dir_fd=context.candidate_fd)
        os.fsync(context.candidate_fd)
        context.commit_transition_durable = False
        context.failure_transition_durable = True
        os.close(context.candidate_fd)
        context.candidate_fd = None
        os.rmdir("candidate", dir_fd=context.base_fd)
        os.fsync(context.base_fd)
        context.commit_transition_durable = False
        context.failure_transition_durable = True
        return True
    except OSError:
        return False
    except Ops03Error:
        return False


def _retain_candidate_failure_latch(
    context: RunContext,
    auth: Mapping[str, Any],
    authorization_sha256: str,
) -> bool:
    if context.candidate_fd is None:
        return True
    payload = canonical_bytes(
        {
            "schema": "hde_epic038.ops03.candidate_failure.v1",
            "run_id": auth["run_id"],
            "authorization_sha256": authorization_sha256,
            "launch_consumed": True,
            "candidate_admissible": False,
        }
    )
    try:
        _assert_context_live(context, phase="final_validation", consumed=True)
        try:
            _write_new_file(context.candidate_fd, FAILURE_LATCH_FILE, payload)
        except FileExistsError:
            pass
        _assert_context_live(context, phase="final_validation", consumed=True)
        retained = _read_file(context.candidate_fd, FAILURE_LATCH_FILE) == payload
        if retained:
            context.commit_transition_durable = False
            context.failure_transition_durable = True
        return retained
    except BaseException:
        return False


def _capture_impl(
    auth_path: Path,
    *,
    ambient: Mapping[str, str] | None = None,
    provider_factory_builder: Callable[[Counters], Callable[[str], Any]] = live_provider_factory,
    enforce_source: bool = True,
    invoke_validators: bool = True,
    now: dt.datetime | None = None,
    actual_argv: Sequence[str] | None = None,
) -> int:
    auth: Mapping[str, Any] | None = None
    authorization_bytes = b""
    consumed = False
    context: RunContext | None = None
    provider_child: ProviderChild | None = None
    environment_shape: EnvironmentShape | None = None
    pending_token: bytes | None = None
    final_attestation: Mapping[str, Any] | None = None
    source_env: Mapping[str, str] = os.environ if ambient is None else ambient
    try:
        try:
            provider_child, environment_shape = _spawn_provider_child(
                auth_path,
                source_env,
                provider_factory_builder,
                now,
            )
        finally:
            ambient = None
            source_env = {}
        if provider_child is None:
            raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False)
        _await_provider_child_ready(provider_child)
        auth, authorization_bytes = _read_canonical_json(auth_path)
        if not _bootstrap_authorization_valid(auth):
            raise Ops03Error("pre_marker", "authorization_schema_invalid", consumed=False)
        validate_source_identity(auth, enforce_repo=enforce_source)
        validate_authorization(auth, auth_path, now=now)
        if not _runtime_invocation_valid(actual_argv, auth["exact_argv"]["capture"]):
            raise Ops03Error("pre_marker", "capture_argv_mismatch", consumed=False)
        if environment_shape is None:
            raise Ops03Error("pre_marker", "provider_child_status_invalid", consumed=False)
        _validate_parent_environment(auth, environment_shape)
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("pre_marker", "authorization_bytes_changed", consumed=False)
        _base, _control, candidate, _failure = derived_paths(str(auth["run_id"]))
        context = _open_run_context(str(auth["run_id"]), create_base=True, allow_existing=False)
        authorization_sha256 = sha256_bytes(authorization_bytes)
        _write_marker(context, auth, authorization_sha256)
        consumed = True
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("pre_provider", "authorization_bytes_changed", consumed=True)
        try:
            context.candidate_fd = _secure_mkdir_open(context.base_fd, "candidate")
        except OSError as exc:
            raise Ops03Error("capture", "candidate_root_unwritable", consumed=True) from exc
        _assert_context_live(context)
        pending_token = os.urandom(32)
        _create_pending_latch(context, auth, authorization_sha256, pending_token)
        if provider_child is None:
            raise Ops03Error("pre_provider", "provider_child_status_invalid", consumed=True)
        _launch_provider_child(
            provider_child,
            auth,
            authorization_sha256,
            enforce_source=enforce_source,
        )
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("capture", "authorization_bytes_changed", consumed=True)
        try:
            validate_source_identity(auth, enforce_repo=enforce_source)
        except Ops03Error as exc:
            raise Ops03Error("capture", exc.code, consumed=True) from exc
        if invoke_validators:
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("receipt_validation", "authorization_bytes_changed", consumed=True)
            _run_validator(auth["exact_argv"]["receipt"], pending_token=pending_token)
            write_checksums(candidate, context=context)
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("final_validation", "authorization_bytes_changed", consumed=True)
            final_attestation = _run_validator(
                auth["exact_argv"]["validate"],
                pending_token=pending_token,
            )
            if final_attestation is None:
                raise Ops03Error(
                    "final_validation",
                    "independent_validator_output_invalid",
                    consumed=True,
                )
            try:
                validate_source_identity(auth, enforce_repo=enforce_source)
            except Ops03Error as exc:
                raise Ops03Error("final_validation", exc.code, consumed=True) from exc
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("final_validation", "authorization_bytes_changed", consumed=True)
        _assert_context_live(context, phase="final_validation", consumed=True)
        if pending_token is None:
            raise Ops03Error(
                "final_validation",
                "candidate_pending_token_unavailable",
                consumed=True,
            )
        _commit_candidate(
            context,
            auth,
            auth_path,
            authorization_bytes,
            authorization_sha256,
            pending_token,
            final_attestation,
            sealed=invoke_validators,
            enforce_source=enforce_source,
        )
        return 0
    except Ops03Error as exc:
        if (
            auth is not None
            and context is not None
            and pending_token is not None
            and context.commit_transition_durable
            and not context.failure_transition_durable
            and _terminal_success_visible(
                context,
                auth,
                auth_path,
                authorization_bytes,
                sha256_bytes(authorization_bytes),
                final_attestation,
                _pending_payload(
                    auth,
                    sha256_bytes(authorization_bytes),
                    pending_token,
                ),
                sealed=invoke_validators,
                enforce_source=enforce_source,
            )
        ):
            return 0
        if auth is None:
            parsed, _canonical, recovered_bytes = _read_json_noncanonical(auth_path)
            auth = parsed if isinstance(parsed, Mapping) else None
            if recovered_bytes:
                authorization_bytes = recovered_bytes
        if auth is not None:
            effective_consumed = consumed or exc.consumed or bool(context and context.launch_consumed)
            failure_phase = "pre_provider" if effective_consumed and exc.phase == "pre_marker" else exc.phase
            if effective_consumed and context is not None:
                _invalidate_candidate_commit_control(
                    context,
                    auth,
                    sha256_bytes(authorization_bytes),
                )
            failure_written = False
            try:
                failure_written = write_failure(
                    auth,
                    sha256_bytes(authorization_bytes),
                    phase=failure_phase,
                    code=exc.code,
                    consumed=effective_consumed,
                    context=context,
                )
            except BaseException:
                pass
            if failure_written and context is not None:
                context.commit_transition_durable = False
                context.failure_transition_durable = True
            if effective_consumed and context is not None:
                discarded = False
                try:
                    discarded = _discard_candidate(context)
                except BaseException:
                    pass
                if not discarded:
                    _retain_candidate_failure_latch(
                        context,
                        auth,
                        sha256_bytes(authorization_bytes),
                    )
        return 1
    except BaseException:
        if (
            auth is not None
            and context is not None
            and pending_token is not None
            and context.commit_transition_durable
            and not context.failure_transition_durable
            and _terminal_success_visible(
                context,
                auth,
                auth_path,
                authorization_bytes,
                sha256_bytes(authorization_bytes),
                final_attestation,
                _pending_payload(
                    auth,
                    sha256_bytes(authorization_bytes),
                    pending_token,
                ),
                sealed=invoke_validators,
                enforce_source=enforce_source,
            )
        ):
            return 0
        if auth is not None:
            effective_consumed = consumed or bool(context and context.launch_consumed)
            if effective_consumed and context is not None:
                _invalidate_candidate_commit_control(
                    context,
                    auth,
                    sha256_bytes(authorization_bytes),
                )
            failure_written = False
            try:
                failure_written = write_failure(
                    auth,
                    sha256_bytes(authorization_bytes),
                    phase="capture" if consumed else ("pre_provider" if effective_consumed else "pre_marker"),
                    code="unexpected_failure",
                    consumed=effective_consumed,
                    context=context,
                )
            except BaseException:
                pass
            if failure_written and context is not None:
                context.commit_transition_durable = False
                context.failure_transition_durable = True
            if effective_consumed and context is not None:
                discarded = False
                try:
                    discarded = _discard_candidate(context)
                except BaseException:
                    pass
                if not discarded:
                    _retain_candidate_failure_latch(
                        context,
                        auth,
                        sha256_bytes(authorization_bytes),
                    )
        return 1
    finally:
        _scrub_parent_database_url()
        if provider_child is not None:
            _abort_provider_child(provider_child)
        if context is not None:
            context.close()


def capture(
    auth_path: Path,
    *,
    ambient: Mapping[str, str] | None = None,
    provider_factory_builder: Callable[[Counters], Callable[[str], Any]] = live_provider_factory,
    enforce_source: bool = True,
    invoke_validators: bool = True,
    now: dt.datetime | None = None,
    actual_argv: Sequence[str] | None = None,
) -> int:
    try:
        return _capture_impl(
            auth_path,
            ambient=ambient,
            provider_factory_builder=provider_factory_builder,
            enforce_source=enforce_source,
            invoke_validators=invoke_validators,
            now=now,
            actual_argv=actual_argv,
        )
    except BaseException:
        _scrub_parent_database_url()
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", required=True, type=Path)
    args = parser.parse_args(argv)
    actual_argv = list(sys.orig_argv) if argv is None else None
    return capture(args.authorization.resolve(), actual_argv=actual_argv)


if __name__ == "__main__":
    raise SystemExit(main())
