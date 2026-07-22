#!/usr/bin/env python3
"""Authorization-bound direct PostgreSQL read-only OPS-03 capture runner."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
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
FAILURE_SCHEMA = ROOT / "schemas/hde_epic038_ops03_failure_receipt.v1.json"
RUN_ROOT = Path("/tmp/hde-epic038-ops03")
RUN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{15,63}$")

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
CHECKSUM_INPUTS = tuple(sorted((*PRIMARY_FILES, "validation_receipt.json")))
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
EXPECTED_VIEWS = ("hde.body_graphs_current", "public.hde_body_graphs_current")

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
        "SELECT rolsuper, rolcreatedb, rolcreaterole "
        "FROM pg_roles WHERE rolname = current_user",
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
        "is_trigger_updatable FROM information_schema.views "
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


def _read_json_noncanonical(path: Path) -> tuple[Any | None, bool]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw.decode("utf-8", "strict"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None, False
    return value, raw == canonical_bytes(value)


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
    from jsonschema import Draft202012Validator, FormatChecker

    validator = Draft202012Validator(_schema(AUTH_SCHEMA), format_checker=FormatChecker())
    if next(validator.iter_errors(auth), None) is not None:
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


def _git(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=False,
        capture_output=True,
        text=True,
        env={"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "GIT_OPTIONAL_LOCKS": "0"},
    )


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
    status = _git(("status", "--porcelain=v1", "--untracked-files=all"))
    if status.returncode or status.stdout:
        raise Ops03Error("pre_marker", "source_tree_not_pristine", consumed=False)
    worktree = _git(("diff", "--quiet", "--no-ext-diff", "--"))
    index = _git(("diff", "--cached", "--quiet", "--no-ext-diff", "--"))
    if worktree.returncode or index.returncode:
        raise Ops03Error("pre_marker", "source_manifest_mismatch", consumed=False)
    if any(ROOT.rglob("*.pyc")) or any(path.is_dir() for path in ROOT.rglob("__pycache__")):
        raise Ops03Error("pre_marker", "bytecode_residue_present", consumed=False)
    ignored_native = _git(("ls-files", "--others", "--ignored", "--exclude-standard", "--", "*.so", "*.pyd"))
    if ignored_native.returncode or ignored_native.stdout:
        raise Ops03Error("pre_marker", "ignored_native_module_present", consumed=False)



def _safe_child(path: Path, *, must_not_exist: bool = False) -> None:
    resolved_root = RUN_ROOT.resolve()
    try:
        if path.exists() or path.is_symlink():
            if must_not_exist or path.is_symlink():
                raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False)
            if not path.is_dir():
                raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False)
            resolved = path.resolve(strict=True)
            if resolved_root not in (resolved, *resolved.parents):
                raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False)
        else:
            parent = path.parent
            if parent.exists():
                parent_resolved = parent.resolve(strict=True)
                if parent_resolved != resolved_root and resolved_root not in parent_resolved.parents:
                    raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False)
    except OSError as exc:
        raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False) from exc


def _ensure_authorized_paths(base: Path, control: Path, candidate: Path, failure: Path, *, must_not_exist: bool) -> None:
    if base.parent.resolve() != RUN_ROOT.resolve():
        raise Ops03Error("pre_marker", "run_root_mismatch", consumed=False)
    for path in (base, control, candidate, failure):
        _safe_child(path, must_not_exist=must_not_exist and path == base)


def _safe_mkdir(path: Path, *, phase: str, consumed: bool) -> None:
    try:
        if path.exists() or path.is_symlink():
            raise Ops03Error(phase, "unsafe_or_stale_run_root", consumed=consumed)
        path.mkdir(parents=True, exist_ok=False)
        if path.is_symlink() or not path.is_dir():
            raise Ops03Error(phase, "unsafe_or_stale_run_root", consumed=consumed)
    except Ops03Error:
        raise
    except OSError as exc:
        raise Ops03Error(phase, "run_root_unwritable", consumed=consumed) from exc

def _clean_db_environment(auth: Mapping[str, Any], ambient: Mapping[str, str]) -> dict[str, str]:
    retired = tuple(sorted(name for name in RETIRED_DB_TRANSPORT_KEYS if name in ambient))
    if retired:
        raise Ops03Error("pre_provider", "retired_key_present", consumed=False)
    expected = {
        "APP_ENV": "dev",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "ALLOW_DB_WRITE": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }
    for name, value in expected.items():
        if ambient.get(name) != value:
            raise Ops03Error("pre_provider", f"environment_{name.lower()}_mismatch", consumed=False)
    database_url = ambient.get("DATABASE_URL")
    if not database_url or not database_url.strip():
        raise Ops03Error("pre_provider", "missing_database_url", consumed=False)
    if auth["rails"]["db_read_authorized"] is not True:
        raise Ops03Error("pre_provider", "db_read_not_authorized", consumed=False)
    allowed_names = {*expected, "DATABASE_URL"}
    unexpected_names = sorted(set(ambient) - allowed_names)
    if unexpected_names:
        raise Ops03Error("pre_provider", "environment_not_clean", consumed=False)
    if any(name.startswith("PYTHON") for name in ambient):
        raise Ops03Error("pre_provider", "python_environment_present", consumed=False)
    return {**expected, "DATABASE_URL": database_url}


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
                    "read_only": all(str(value).upper() == "NO" for value in row[2:5]),
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
            "all_expected_present": observed_partitions == list(EXPECTED_PARTITIONS) == verified_partitions,
        },
    }
    predicates = {
        "authorization_match": True,
        "direct_provider_only": db.provider_name == "psycopg" and list(db.attempts) == [{"provider": "psycopg", "status": "ok", "reason": None}],
        "read_only_transaction": read_only,
        "search_path_exact": search_path == ["hde", "public"],
        "least_privilege_role": role_flags == {"rolsuper": False, "rolcreatedb": False, "rolcreaterole": False},
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



def _capture_provider_child(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    candidate: Path,
    db_env: Mapping[str, str],
    provider_factory_builder: Callable[[Counters], Callable[[str], Any]],
) -> None:
    status_path = candidate.parent / "control" / "provider_child_status.json"
    pid = os.fork()
    if pid == 0:
        try:
            for name in tuple(os.environ):
                if name.startswith("PYTHON") or name == "DATABASE_URL":
                    os.environ.pop(name, None)
            os.environ.clear()
            os.environ.update(db_env)
            counters = Counters()
            provider_factory = provider_factory_builder(counters)
            DBAccess, _schema_name, _provider, _project, _validate = _repo_db_symbols()
            db = DBAccess.for_current_env(environ=dict(os.environ), psycopg_factory=provider_factory)
            results = db.readonly_tx(QUERY_STATEMENTS)
            posture = build_posture(auth, db, results, counters)
            _write_capture_files(auth, authorization_sha256, candidate, posture)
            status = {"pid": os.getpid(), "parent_pid": os.getppid(), "result": "PASS"}
            status_path.write_bytes(canonical_bytes(status))
            os._exit(0)
        except BaseException:
            try:
                status_path.write_bytes(canonical_bytes({"pid": os.getpid(), "parent_pid": os.getppid(), "result": "FAIL"}))
            except BaseException:
                pass
            os._exit(1)
    _, rc = os.waitpid(pid, 0)
    if rc != 0:
        raise Ops03Error("capture", "unexpected_failure", consumed=True)

def _write_capture_files(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    candidate: Path,
    posture: Mapping[str, Any],
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
    for name, payload in files.items():
        if _retained_text_is_unsafe(candidate / name, payload):
            raise Ops03Error("capture", "secret_scan_failed", consumed=True)
        (candidate / name).write_bytes(payload)


def write_checksums(candidate: Path) -> None:
    lines = [f"{sha256_path(candidate / name)}  {name}\n" for name in CHECKSUM_INPUTS]
    (candidate / "checksums.sha256").write_text("".join(lines), encoding="ascii")


def _run_validator(argv: Sequence[str]) -> None:
    completed = subprocess.run(
        list(argv),
        check=False,
        capture_output=True,
        env=_clean_validator_environment(),
    )
    if completed.returncode:
        raise Ops03Error(
            "receipt_validation" if "--emit-receipt" in argv else "final_validation",
            "independent_validator_failed",
            consumed=True,
        )


def _write_marker(control: Path, auth: Mapping[str, Any], authorization_sha256: str) -> None:
    _safe_mkdir(control, phase="pre_marker", consumed=False)
    try:
        (control / "launch.marker").write_bytes(b"launch_consumed=true\n")
    except OSError as exc:
        raise Ops03Error("pre_marker", "launch_marker_write_failed", consumed=False) from exc
    consumption = {
        "schema": "hde_epic038.ops03.authorization_consumption.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": authorization_sha256,
        "launch_consumed": True,
    }
    try:
        (control / "authorization_consumed.json").write_bytes(canonical_bytes(consumption))
    except OSError as exc:
        raise Ops03Error("pre_provider", "authorization_consumption_record_write_failed", consumed=True) from exc


def write_failure(
    auth: Mapping[str, Any],
    authorization_sha256: str,
    *,
    phase: str,
    code: str,
    consumed: bool,
) -> None:
    run_id = auth.get("run_id")
    if not isinstance(run_id, str) or RUN_ID_RE.fullmatch(run_id) is None:
        return
    _, _, _, failure = derived_paths(run_id)
    try:
        if failure.exists() and (failure.is_symlink() or not failure.is_dir()):
            return
        failure.mkdir(parents=True, exist_ok=True)
    except OSError:
        return
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
    from jsonschema import Draft202012Validator

    schema = _schema(FAILURE_SCHEMA)
    if next(Draft202012Validator(schema).iter_errors(receipt), None) is not None:
        return
    path = failure / "failure_receipt.json"
    if not path.exists():
        path.write_bytes(canonical_bytes(receipt))


def _discard_candidate(auth: Mapping[str, Any]) -> None:
    run_id = auth.get("run_id")
    if not isinstance(run_id, str) or RUN_ID_RE.fullmatch(run_id) is None:
        return
    _, _, candidate, _ = derived_paths(run_id)
    if candidate.parent.parent != RUN_ROOT or not candidate.exists():
        return
    try:
        shutil.rmtree(candidate)
    except OSError:
        pass


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
    auth: Mapping[str, Any] | None = None
    authorization_bytes = b""
    consumed = False
    try:
        auth, authorization_bytes = _read_canonical_json(auth_path)
        validate_authorization(auth, auth_path, now=now)
        if not _runtime_invocation_valid(actual_argv, auth["exact_argv"]["capture"]):
            raise Ops03Error("pre_marker", "capture_argv_mismatch", consumed=False)
        validate_source_identity(auth, enforce_repo=enforce_source)
        base, control, candidate, _ = derived_paths(str(auth["run_id"]))
        if base.is_symlink():
            raise Ops03Error("pre_marker", "unsafe_or_stale_run_root", consumed=False)
        if base.exists():
            raise Ops03Error("pre_marker", "authorization_already_consumed", consumed=False)
        _ensure_authorized_paths(base, control, candidate, base / "failure", must_not_exist=False)
        db_env = _clean_db_environment(auth, os.environ if ambient is None else ambient)
        DBAccess, _schema_name, _provider, _project, validate_readonly_statements = _repo_db_symbols()
        validate_readonly_statements(QUERY_STATEMENTS)
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("pre_marker", "authorization_bytes_changed", consumed=False)
        _safe_mkdir(base, phase="pre_marker", consumed=False)
        authorization_sha256 = sha256_bytes(authorization_bytes)
        _write_marker(control, auth, authorization_sha256)
        consumed = True
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("pre_provider", "authorization_bytes_changed", consumed=True)
        _safe_mkdir(candidate, phase="capture", consumed=True)
        _capture_provider_child(auth, authorization_sha256, candidate, db_env, provider_factory_builder)
        db_env = {}
        if not _authorization_is_stable(auth_path, authorization_bytes):
            raise Ops03Error("capture", "authorization_bytes_changed", consumed=True)
        validate_source_identity(auth, enforce_repo=enforce_source)
        if invoke_validators:
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("receipt_validation", "authorization_bytes_changed", consumed=True)
            _run_validator(auth["exact_argv"]["receipt"])
            write_checksums(candidate)
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("final_validation", "authorization_bytes_changed", consumed=True)
            _run_validator(auth["exact_argv"]["validate"])
            validate_source_identity(auth, enforce_repo=enforce_source)
            if not _authorization_is_stable(auth_path, authorization_bytes):
                raise Ops03Error("final_validation", "authorization_bytes_changed", consumed=True)
        return 0
    except Ops03Error as exc:
        if auth is None:
            parsed, _canonical = _read_json_noncanonical(auth_path)
            auth = parsed if isinstance(parsed, Mapping) else None
        if auth is not None:
            if consumed:
                _discard_candidate(auth)
            write_failure(
                auth,
                sha256_bytes(authorization_bytes),
                phase=exc.phase,
                code=exc.code,
                consumed=consumed or exc.consumed,
            )
        return 1
    except Exception:
        if auth is not None:
            if consumed:
                _discard_candidate(auth)
            write_failure(
                auth,
                sha256_bytes(authorization_bytes),
                phase="capture" if consumed else "pre_marker",
                code="unexpected_failure",
                consumed=consumed,
            )
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", required=True, type=Path)
    args = parser.parse_args(argv)
    actual_argv = list(sys.orig_argv) if argv is None else None
    return capture(args.authorization.resolve(), actual_argv=actual_argv)


if __name__ == "__main__":
    raise SystemExit(main())
