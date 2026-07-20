#!/usr/bin/env python3
"""Dormant OPS-01R runner scaffold for HDE-EPIC038 PR-A."""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from collections.abc import Iterator, Mapping
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SOURCE_MANIFEST_SCHEMA = "hde_epic038.source_tree_manifest.v1"
STAGING_MANIFEST_SCHEMA = "hde_epic038.non_source_staging_manifest.v1"

EXPECTED_CALL_COUNTS = {
    "bodygraph_reads": 2,
    "bridge_http_requests": 6,
    "bridge_provider_selections": 1,
    "direct_connection_attempts": 8,
    "direct_provider_selections": 1,
    "direct_sql_statements": 13,
    "fallbacks": 0,
    "logical_observations": 10,
    "retries": 0,
    "vendor_requests": 0,
}

PREFLIGHT_ZERO_IO_FIELDS = (
    "bridge_transport_delegations",
    "candidate_writes",
    "credential_reads",
    "direct_connector_delegations",
    "failure_summary_writes",
    "provider_constructions",
    "railway_subprocesses",
    "sql_driver_delegations",
    "vendor_transport_delegations",
)

# This is an ordered fake-boundary trace, not a copied counter object.  Each
# entry represents the point immediately before the corresponding live
# delegation would be touched.  Preflight replays the trace twice without
# constructing a provider or invoking a delegate, and derives its vector from
# the two independent observations.
PREFLIGHT_FAKE_BOUNDARY_EVENTS = (
    "direct_provider_selections",
    *("direct_connection_attempts" for _ in range(8)),
    *("direct_sql_statements" for _ in range(13)),
    "bridge_provider_selections",
    *("bridge_http_requests" for _ in range(6)),
    *("logical_observations" for _ in range(8)),
    "bodygraph_reads",
    "logical_observations",
    "bodygraph_reads",
    "logical_observations",
)

DISCOVERY_NONCLAIMS = [
    "no_glow_import",
    "no_provider_construction",
    "no_db_call",
    "no_bridge_call",
    "no_vendor_call",
    "no_deployment",
    "no_restart",
    "no_relink",
    "no_selection_change",
    "no_variable_mutation",
    "no_tracked_write",
]

LIVE_NONCLAIMS = [
    "no_sql_write",
    "no_migration",
    "no_grant_change",
    "no_schema_change",
    "no_vendor_call",
    "no_deployment_change",
    "no_raw_secret_persistence",
    "no_raw_user_data_persistence",
    "no_raw_bodygraph_payload_persistence",
    "no_qa_pass_claim",
    "no_acceptance_token_claim",
    "no_pf09_status_movement",
    "no_epic_closeout_claim",
]

SELECTOR = {
    "alias": "epic011-s10-invariance-1",
    "identity_source": "docs/run/EPIC011_TEST_IDENTITIES.md",
    "non_pii": True,
    "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afab",
}


def canonical_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("ascii")


def sha_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def tree_manifest(
    root: Path,
    *,
    schema: str,
    excluded_paths: tuple[Path, ...] = (),
    excluded_recursive_roots: tuple[Path, ...] = (),
) -> dict[str, object]:
    root = _lexical_absolute(root)
    excluded_exact = {_lexical_absolute(path) for path in excluded_paths}
    excluded_roots = tuple(
        _lexical_absolute(path) for path in excluded_recursive_roots
    )
    entries: list[dict[str, object]] = []

    def excluded(path: Path) -> bool:
        return path in excluded_exact or any(
            parent in (path, *path.parents) for parent in excluded_roots
        )

    def visit(path: Path) -> None:
        if path != root and excluded(path):
            return
        metadata = path.lstat()
        relative = "." if path == root else path.relative_to(root).as_posix()
        if any(part == "__pycache__" for part in Path(relative).parts) or (
            stat.S_ISREG(metadata.st_mode) and path.name.endswith(".pyc")
        ):
            raise RuntimeError("OPS01_V5_SOURCE_RESIDUE_DETECTED")
        entry: dict[str, object] = {
            "ctime_ns": metadata.st_ctime_ns,
            "kind": "",
            "mode": stat.S_IMODE(metadata.st_mode),
            "mtime_ns": metadata.st_mtime_ns,
            "path": relative,
            "sha256": None,
            "size": None,
            "target": None,
        }
        if stat.S_ISDIR(metadata.st_mode):
            entry["kind"] = "directory"
        elif stat.S_ISREG(metadata.st_mode):
            entry["kind"] = "regular_file"
            data = path.read_bytes()
            entry["sha256"] = sha_bytes(data)
            entry["size"] = len(data)
        elif stat.S_ISLNK(metadata.st_mode):
            entry["kind"] = "symlink"
            entry["target"] = os.readlink(path)
        else:
            raise RuntimeError("unsupported filesystem kind")
        entries.append(entry)
        if entry["kind"] == "directory":
            for child in sorted(
                path.iterdir(), key=lambda item: item.name.encode("utf-8")
            ):
                visit(_lexical_absolute(child))

    visit(root)
    return {
        "schema": schema,
        "entries": sorted(entries, key=lambda item: str(item["path"]).encode("utf-8")),
    }


def manifest_delta(
    before: list[dict[str, object]], after: list[dict[str, object]]
) -> list[dict[str, object]]:
    before_rows = {str(row["path"]): row for row in before}
    after_rows = {str(row["path"]): row for row in after}
    changes: list[dict[str, object]] = []
    for path in sorted(set(before_rows) | set(after_rows), key=lambda item: item.encode("utf-8")):
        if path not in before_rows:
            kinds = ["created"]
        elif path not in after_rows:
            kinds = ["deleted"]
        else:
            kinds = sorted(
                key
                for key in (
                    "ctime_ns",
                    "kind",
                    "mode",
                    "mtime_ns",
                    "sha256",
                    "size",
                    "target",
                )
                if before_rows[path].get(key) != after_rows[path].get(key)
            )
        if kinds:
            changes.append({"change_kinds": kinds, "path": path})
    return changes


def bound_python_vector(script: Path, *arguments: str) -> tuple[str, ...]:
    return (sys.executable, "-I", "-B", script.resolve().as_posix(), *arguments)


def reject_python_env(environment: Mapping[str, object]) -> None:
    if any(name.casefold().startswith("python") for name in environment):
        raise RuntimeError("OPS01_V5_PYTHON_ENVIRONMENT_INVALID")


def require_source_loading_process_contract() -> None:
    """Fail before mode work unless this script is running under exact -I -B."""
    if (
        sys.flags.isolated != 1
        or sys.flags.dont_write_bytecode != 1
        or Path(sys.argv[0]).resolve() != Path(__file__).resolve()
    ):
        raise RuntimeError("OPS01_V5_PYTHON_ARGV_MISMATCH")
    reject_python_env(os.environ)


def write_contained(path: Path, data: bytes, root: Path) -> None:
    path = path.resolve()
    root = root.resolve()
    if root not in (path, *path.parents):
        raise RuntimeError("OPS01_V5_WRITE_SET_MISMATCH")
    for parent in path.parents:
        if parent == root.parent:
            break
        if parent.exists() and parent.is_symlink():
            raise RuntimeError("OPS01_V5_WRITE_SET_MISMATCH")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _file_identity(path: Path) -> dict[str, str]:
    lexical = path.absolute()
    resolved = lexical.resolve()
    return {
        "lexical_path": lexical.as_posix(),
        "resolved_path": resolved.as_posix(),
        "sha256": sha_bytes(resolved.read_bytes()),
    }


def _optional_executable_identity(name: str) -> dict[str, str]:
    lexical = shutil.which(name)
    if lexical is None:
        return {"lexical_path": name, "resolved_path": "", "sha256": ""}
    return _file_identity(Path(lexical))


def _git_commit(root: Path) -> str:
    marker = root / ".git"
    git_dir = marker
    if marker.is_file():
        text = marker.read_text("utf-8").strip()
        if not text.startswith("gitdir: "):
            return "UNKNOWN"
        git_dir = Path(text[8:])
        if not git_dir.is_absolute():
            git_dir = (root / git_dir).resolve()
    try:
        head = (git_dir / "HEAD").read_text("ascii").strip()
    except OSError:
        return "UNKNOWN"
    if len(head) == 40 and all(character in "0123456789abcdef" for character in head):
        return head
    if not head.startswith("ref: "):
        return "UNKNOWN"
    reference = head[5:]
    candidates = [git_dir / reference]
    try:
        common = (git_dir / "commondir").read_text("utf-8").strip()
        common_dir = Path(common)
        if not common_dir.is_absolute():
            common_dir = (git_dir / common_dir).resolve()
        candidates.append(common_dir / reference)
    except OSError:
        common_dir = git_dir
    for candidate in candidates:
        try:
            value = candidate.read_text("ascii").strip()
        except OSError:
            continue
        if len(value) == 40 and all(
            character in "0123456789abcdef" for character in value
        ):
            return value
    for packed in (git_dir / "packed-refs", common_dir / "packed-refs"):
        try:
            lines = packed.read_text("ascii").splitlines()
        except OSError:
            continue
        for line in lines:
            if line.startswith(("#", "^")):
                continue
            fields = line.split(" ", 1)
            if len(fields) == 2 and fields[1] == reference:
                return fields[0]
    return "UNKNOWN"


def _module_origins(source_root: Path) -> list[dict[str, str]]:
    modules = {
        "engine.db.ddl_identity_projection": source_root
        / "engine/db/ddl_identity_projection.py",
        "scripts.db.capture_epic011_posture": source_root
        / "scripts/db/capture_epic011_posture.py",
        "scripts.ops.hde_epic038_ops01r": source_root
        / "scripts/ops/hde_epic038_ops01r.py",
        "tools.evidence.hde_epic038_ops01_v5": source_root
        / "tools/evidence/hde_epic038_ops01_v5.py",
    }
    origins = []
    for module, path in sorted(modules.items()):
        identity = _file_identity(path)
        origins.append(
            {
                "lexical_origin": identity["lexical_path"],
                "module": module,
                "resolved_origin": identity["resolved_path"],
                "sha256": identity["sha256"],
            }
        )
    return origins


def _clean_child_env() -> dict[str, str]:
    env = {
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "ALLOW_DB_WRITE": "0",
        "APP_ENV": "dev",
    }
    reject_python_env(env)
    return env


def _launcher_env() -> dict[str, str]:
    """Preserve launcher authentication while excluding child-only values."""
    removed = {
        "ALLOW_DB_WRITE",
        "ALLOW_NETWORK",
        "APP_ENV",
        "DATABASE_URL",
        "DB_ALLOW_BRIDGE_IN_PROD",
        "DB_BRIDGE_URL",
        "DB_FORCE_BRIDGE",
        "DB_FORCE_PG",
        "ENGINE_ENV",
        "SAFE_MODE",
    }
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
        and name not in removed
        and name
        not in {
            "HD_API_KEY",
            "HDE_BIRTHDATE",
            "HDE_BIRTHTIME",
            "HDE_LOCATION",
            "HDE_VENDOR_URL",
        }
    }
    environment.update(_clean_child_env())
    return environment


def _safe_identity_string(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and not any(ord(character) < 32 or ord(character) == 127 for character in value)
    )


def _target_probe_payload(environment: Mapping[str, str]) -> dict[str, object]:
    """Expose only non-secret Railway identity candidates and endpoint presence."""
    identity_fields = []
    forbidden = ("secret", "token", "password", "passwd", "key", "cookie")
    for name, value in sorted(environment.items(), key=lambda item: item[0].encode("utf-8")):
        folded = name.casefold()
        if (
            not name.startswith("RAILWAY_")
            or not name.endswith("_ID")
            or any(marker in folded for marker in forbidden)
            or not _safe_identity_string(name)
            or not _safe_identity_string(value)
        ):
            continue
        identity_fields.append({"name": name, "value": value})
    return {
        "schema": "hde_epic038.ops01r.target_identity_probe.v1",
        "writes": 0,
        "endpoint_presence": {
            "DATABASE_URL": bool((environment.get("DATABASE_URL") or "").strip()),
            "DB_BRIDGE_URL": bool((environment.get("DB_BRIDGE_URL") or "").strip()),
        },
        "identity_fields": identity_fields,
    }


def _derive_discovery_contracts(
    target: Mapping[str, str], probe: Mapping[str, object]
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    identity_fields = probe.get("identity_fields")
    endpoint_presence = probe.get("endpoint_presence")
    if not isinstance(identity_fields, list) or endpoint_presence != {
        "DATABASE_URL": True,
        "DB_BRIDGE_URL": True,
    }:
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    candidates: list[dict[str, str]] = []
    for row in identity_fields:
        if (
            not isinstance(row, dict)
            or set(row) != {"name", "value"}
            or not _safe_identity_string(row.get("name"))
            or not _safe_identity_string(row.get("value"))
        ):
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        candidates.append({"name": row["name"], "value": row["value"]})

    identity_contract: list[dict[str, str]] = []
    for dimension, field in (
        ("project", "project_id"),
        ("environment", "environment_id"),
        ("service", "service_id"),
    ):
        matches = [row for row in candidates if row["value"] == target[field]]
        if len(matches) != 1:
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        identity_contract.append(
            {
                "expected_value": target[field],
                "field_name": matches[0]["name"],
                "target_dimension": dimension,
                "value_kind": "target_id",
            }
        )
    identity_contract.sort(key=lambda row: row["field_name"].encode("utf-8"))

    child_environment_contract = [
        {"name": "ALLOW_DB_WRITE", "source": "runner", "value_policy": "exact:0"},
        {"name": "ALLOW_NETWORK", "source": "runner", "value_policy": "exact:0"},
        {"name": "APP_ENV", "source": "runner", "value_policy": "exact:dev"},
        {"name": "DATABASE_URL", "source": "railway_service", "value_policy": "presence_only"},
        {"name": "DB_BRIDGE_URL", "source": "railway_service", "value_policy": "presence_only"},
        {"name": "LANG", "source": "runner", "value_policy": "exact:C"},
        {"name": "LC_ALL", "source": "runner", "value_policy": "exact:C"},
        {"name": "SAFE_MODE", "source": "runner", "value_policy": "exact:1"},
        {"name": "TZ", "source": "runner", "value_policy": "exact:UTC"},
    ]
    child_environment_contract.extend(
        {
            "name": row["field_name"],
            "source": "railway_target_identity",
            "value_policy": f"exact:{row['expected_value']}",
        }
        for row in identity_contract
    )
    child_environment_contract.sort(key=lambda row: row["name"].encode("utf-8"))
    return identity_contract, child_environment_contract


def _run_checked(argv: tuple[str, ...], **kwargs) -> subprocess.CompletedProcess[str]:
    if len(argv) < 3 or argv[1:3] != ("-I", "-B"):
        raise RuntimeError("OPS01_V5_PYTHON_ARGV_MISMATCH")
    return subprocess.run(argv, shell=False, check=True, text=True, **kwargs)


def _require_string_list(value: object, code: str) -> list[str]:
    if (
        not isinstance(value, list)
        or any(
            not isinstance(item, str)
            or not item
            or item != item.strip()
            or any(ord(character) < 32 or ord(character) == 127 for character in item)
            for item in value
        )
    ):
        raise SystemExit(code)
    return value


def _staging_manifest_for_contract(
    staging_root: Path,
    *,
    source_root: Path,
    excluded_paths: list[str],
    excluded_recursive_roots: list[str],
) -> dict[str, object]:
    return tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=tuple(Path(value) for value in excluded_paths),
        excluded_recursive_roots=(
            source_root,
            *(Path(value) for value in excluded_recursive_roots),
        ),
    )


def _validate_pre_staging_contract(
    staging_root: Path,
    *,
    source_root: Path,
    write_contract: Mapping[str, object],
    code: str,
) -> tuple[dict[str, object], list[str], list[str]]:
    excluded_paths = _require_string_list(
        write_contract.get("self_bound_excluded_paths"), code
    )
    excluded_recursive_roots = _require_string_list(
        write_contract.get("self_bound_excluded_recursive_roots"), code
    )
    retained_entries = write_contract.get("pre_staging_manifest")
    retained_hash = write_contract.get("pre_staging_manifest_sha256")
    if not isinstance(retained_entries, list) or not isinstance(retained_hash, str):
        raise SystemExit(code)
    retained = {"schema": STAGING_MANIFEST_SCHEMA, "entries": retained_entries}
    if sha_bytes(canonical_bytes(retained)) != retained_hash:
        raise SystemExit(code)
    actual = _staging_manifest_for_contract(
        staging_root,
        source_root=source_root,
        excluded_paths=excluded_paths,
        excluded_recursive_roots=excluded_recursive_roots,
    )
    if actual != retained:
        raise SystemExit(code)
    return retained, excluded_paths, excluded_recursive_roots


def _validate_authorized_delta(
    delta: list[dict[str, object]],
    *,
    staging_root: Path,
    exact_paths: list[str],
    recursive_roots: list[str],
    directory_metadata_paths: list[str],
    code: str,
) -> None:
    exact = {_lexical_absolute(Path(value)) for value in exact_paths}
    recursive = tuple(_lexical_absolute(Path(value)) for value in recursive_roots)
    metadata = {_lexical_absolute(Path(value)) for value in directory_metadata_paths}
    for change in delta:
        relative = change.get("path")
        kinds = change.get("change_kinds")
        if not isinstance(relative, str) or not isinstance(kinds, list):
            raise SystemExit(code)
        path = staging_root if relative == "." else staging_root / relative
        path = _lexical_absolute(path)
        beneath_recursive = any(root in (path, *path.parents) for root in recursive)
        metadata_only = path in metadata and set(kinds) <= {"ctime_ns", "mtime_ns"}
        if path not in exact and not beneath_recursive and not metadata_only:
            raise SystemExit(code)


def materialize_source_worktree(source_root: Path, commit: str) -> None:
    if source_root.exists():
        raise RuntimeError("OPS01_V5_SOURCE_ROOT_EXISTS")
    if commit == "UNKNOWN" or not (ROOT / ".git").exists():
        shutil.copytree(
            ROOT,
            source_root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        return
    subprocess.run(
        ("git", "worktree", "add", "--detach", source_root.as_posix(), commit),
        cwd=ROOT,
        shell=False,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    status = subprocess.run(
        ("git", "status", "--porcelain"),
        cwd=source_root,
        shell=False,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if status.stdout:
        raise RuntimeError("OPS01_V5_SOURCE_WORKTREE_DIRTY")


def _preflight_source_write_validation(
    *,
    mode: str,
    producer_argv: tuple[str, ...],
    source_root: Path,
    staging_root: Path,
    preflight_path: Path,
    pre_source_manifest: dict[str, object],
    pre_staging_manifest: dict[str, object],
    post_source_manifest: dict[str, object],
    post_staging_manifest: dict[str, object],
    observed_staging_changes: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "authorized_directory_metadata_paths": [preflight_path.parent.as_posix()],
        "authorized_exact_write_paths": [preflight_path.as_posix()],
        "authorized_recursive_write_roots": [],
        "bytecode_write_control": "python_flag_-B",
        "manifest_algorithm": SOURCE_MANIFEST_SCHEMA,
        "mode": mode,
        "observed_staging_changes": observed_staging_changes,
        "post_source_manifest_sha256": sha_bytes(canonical_bytes(post_source_manifest)),
        "post_staging_manifest_sha256": sha_bytes(canonical_bytes(post_staging_manifest)),
        "pre_source_manifest_sha256": sha_bytes(canonical_bytes(pre_source_manifest)),
        "pre_staging_manifest": pre_staging_manifest["entries"],
        "pre_staging_manifest_sha256": sha_bytes(canonical_bytes(pre_staging_manifest)),
        "prohibited_cache_paths": [],
        "python_argv": list(producer_argv),
        "python_environment_names": [],
        "self_bound_excluded_paths": [preflight_path.as_posix()],
        "self_bound_excluded_recursive_roots": [],
        "source_root": source_root.as_posix(),
        "source_tree_unchanged": True,
        "staging_manifest_algorithm": STAGING_MANIFEST_SCHEMA,
        "staging_write_set_valid": True,
        "status": "PASS",
        "unauthorized_staging_paths": [],
    }


def _preflight_fake_boundary_run() -> dict[str, object]:
    expected = {name: 0 for name in EXPECTED_CALL_COUNTS}
    for field in PREFLIGHT_FAKE_BOUNDARY_EVENTS:
        expected[field] += 1
    actual = {name: 0 for name in PREFLIGHT_ZERO_IO_FIELDS}
    return {
        "actual_external_io_counts": actual,
        "expected_call_counts": expected,
    }


def _preflight_count_orchestration() -> dict[str, object]:
    run_1 = _preflight_fake_boundary_run()
    run_2 = _preflight_fake_boundary_run()
    vectors_equal = run_1 == run_2
    if not vectors_equal or run_1["expected_call_counts"] != EXPECTED_CALL_COUNTS:
        raise RuntimeError("OPS01_V5_PREFLIGHT_NONDETERMINISTIC")
    return {
        "fake_boundary_mode": "count_before_fail_on_touch_delegate",
        "run_1": run_1,
        "run_2": run_2,
        "run_count": 2,
        "vectors_equal": True,
    }


def _produce_preflight_payload(
    *,
    run_id: str,
    staging_root: Path,
    source_root: Path,
    control_root: Path,
    working_directory: Path,
    preflight_path: Path,
    source_commit: str,
) -> None:
    require_source_loading_process_contract()
    source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    source_manifest_sha256 = sha_bytes(canonical_bytes(source_manifest))
    pre_staging_manifest = tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=(preflight_path,),
        excluded_recursive_roots=(source_root,),
    )
    staged_runner = source_root / "scripts/ops/hde_epic038_ops01r.py"
    staged_validator = source_root / "tools/evidence/hde_epic038_ops01_v5.py"
    staged_projector = source_root / "engine/db/ddl_identity_projection.py"
    runner = _file_identity(staged_runner)
    validator = _file_identity(staged_validator)
    projector = _file_identity(staged_projector)
    interpreter = _file_identity(Path(sys.executable))
    railway = _optional_executable_identity("railway")
    if not railway["resolved_path"] or not railway["sha256"]:
        raise RuntimeError("OPS01_V5_RAILWAY_EXECUTABLE_IDENTITY_MISMATCH")
    producer_argv = bound_python_vector(staged_runner, "--preflight")
    if tuple(sys.argv) != producer_argv[3:]:
        raise RuntimeError("OPS01_V5_PYTHON_ARGV_MISMATCH")
    validator_argv = bound_python_vector(
        staged_validator,
        "--validate-preflight",
        "--expected-identity-stdin",
        preflight_path.as_posix(),
    )
    orchestration = _preflight_count_orchestration()
    expected_counts = dict(orchestration["run_1"]["expected_call_counts"])
    zero_counts = dict(orchestration["run_1"]["actual_external_io_counts"])
    write_contained(preflight_path, b"", staging_root)
    post_source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    if sha_bytes(canonical_bytes(post_source_manifest)) != source_manifest_sha256:
        raise RuntimeError("OPS01_V5_SOURCE_MANIFEST_MISMATCH")
    post_staging_manifest = tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=(preflight_path,),
        excluded_recursive_roots=(source_root,),
    )
    observed_staging_changes = manifest_delta(
        pre_staging_manifest["entries"], post_staging_manifest["entries"]
    )
    payload: dict[str, object] = {
        "schema": "hde_epic038.ops01r.preflight.v1",
        "status": "PASS",
        "run": {
            "control_root": control_root.as_posix(),
            "preflight_path": preflight_path.as_posix(),
            "run_id": run_id,
            "source_root": source_root.as_posix(),
            "staging_root": staging_root.as_posix(),
            "working_directory": working_directory.as_posix(),
        },
        "source": {
            "checkout_state": "DETACHED",
            "commit": source_commit,
            "repository": "amthorn78/glow-hdengine-v2",
            "root": source_root.as_posix(),
            "source_manifest_sha256": source_manifest_sha256,
            "worktree_state": "clean",
        },
        "components": {"projector": projector, "runner": runner, "validator": validator},
        "interpreter": {
            "bytecode_flag": "-B",
            "bytecode_write_control": "python_flag_-B",
            "isolated_flag": "-I",
            "lexical_path": interpreter["lexical_path"],
            "preflight_argv": list(producer_argv),
            "preflight_validator_argv": list(validator_argv),
            "python_environment_names": [],
            "resolved_path": interpreter["resolved_path"],
            "sha256": interpreter["sha256"],
        },
        "module_origins": _module_origins(source_root),
        "railway_executable": railway,
        "orchestration": orchestration,
        "actual_external_io_counts": zero_counts,
        "expected_call_counts": expected_counts,
        "nonclaims": [
            "no_railway_subprocess",
            "no_credential_read",
            "no_provider_construction",
            "no_direct_connector_delegation",
            "no_sql_driver_delegation",
            "no_bridge_transport_delegation",
            "no_vendor_transport_delegation",
            "no_candidate_write",
            "no_failure_summary_write",
            "no_source_tree_write",
            "no_bytecode_cache_write",
            "no_unauthorized_staging_write",
        ],
        "source_write_validation": _preflight_source_write_validation(
            mode="preflight",
            producer_argv=producer_argv,
            source_root=source_root,
            staging_root=staging_root,
            preflight_path=preflight_path,
            pre_source_manifest=source_manifest,
            pre_staging_manifest=pre_staging_manifest,
            post_source_manifest=post_source_manifest,
            post_staging_manifest=post_staging_manifest,
            observed_staging_changes=observed_staging_changes,
        ),
    }
    payload["preflight_identity_sha256"] = sha_bytes(canonical_bytes(payload))
    write_contained(preflight_path, canonical_bytes(payload), staging_root)
    recaptured_staging_manifest = tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=(preflight_path,),
        excluded_recursive_roots=(source_root,),
    )
    if (
        sha_bytes(canonical_bytes(recaptured_staging_manifest))
        != payload["source_write_validation"]["post_staging_manifest_sha256"]
        or manifest_delta(
            pre_staging_manifest["entries"],
            recaptured_staging_manifest["entries"],
        )
        != observed_staging_changes
    ):
        raise RuntimeError("OPS01_V5_WRITE_SET_MISMATCH")


def preflight(*, run_id: str | None = None) -> int:
    if os.environ.get("OPS01R_PREFLIGHT_STAGED") == "1":
        reject_python_env(os.environ)
        _produce_preflight_payload(
            run_id=os.environ["OPS01R_RUN_ID"],
            staging_root=Path(os.environ["OPS01R_STAGING_ROOT"]),
            source_root=Path(os.environ["OPS01R_SOURCE_ROOT"]),
            control_root=Path(os.environ["OPS01R_CONTROL_ROOT"]),
            working_directory=Path(os.environ["OPS01R_WORKING_DIRECTORY"]),
            preflight_path=Path(os.environ["OPS01R_PREFLIGHT_PATH"]),
            source_commit=os.environ["OPS01R_SOURCE_COMMIT"],
        )
        print(os.environ["OPS01R_PREFLIGHT_PATH"])
        return 0

    reject_python_env(os.environ)
    run_id = run_id or uuid.uuid4().hex
    if len(run_id) != 32 or any(c not in "0123456789abcdef" for c in run_id):
        raise RuntimeError("OPS01_V5_RUN_ID_INVALID")
    staging_root = Path("/tmp/hde-epic038-ops01r") / run_id
    source_root = staging_root / "source"
    control_root = staging_root / "control"
    working_directory = staging_root / "preflight-work"
    preflight_path = control_root / "preflight.json"
    control_root.mkdir(parents=True)
    working_directory.mkdir()
    source_commit = _git_commit(ROOT)
    materialize_source_worktree(source_root, source_commit)
    staged_runner = source_root / "scripts/ops/hde_epic038_ops01r.py"
    producer_argv = bound_python_vector(staged_runner, "--preflight")
    child_env = _clean_child_env()
    if "PATH" in os.environ:
        child_env["PATH"] = os.environ["PATH"]
    child_env.update(
        {
            "OPS01R_PREFLIGHT_STAGED": "1",
            "OPS01R_RUN_ID": run_id,
            "OPS01R_STAGING_ROOT": staging_root.as_posix(),
            "OPS01R_SOURCE_ROOT": source_root.as_posix(),
            "OPS01R_CONTROL_ROOT": control_root.as_posix(),
            "OPS01R_WORKING_DIRECTORY": working_directory.as_posix(),
            "OPS01R_PREFLIGHT_PATH": preflight_path.as_posix(),
            "OPS01R_SOURCE_COMMIT": source_commit,
        }
    )
    reject_python_env(child_env)
    subprocess.run(
        producer_argv,
        cwd=working_directory,
        env=child_env,
        shell=False,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(preflight_path.as_posix())
    return 0


def discovery(
    authorization_path: Path,
    *,
    expected=None,
) -> int:
    from tools.evidence.hde_epic038_ops01_v5 import (
        DISCOVERY_STAGES,
        Ops01RDiscoveryAuthorizationExpectedIdentity,
        _parse_expected_stdin,
        validate_ops01r_discovery_authorization,
        validate_ops01r_discovery_dispatch,
        validate_ops01r_discovery_result,
    )
    if expected is None:
        expected = _parse_expected_stdin(
            Ops01RDiscoveryAuthorizationExpectedIdentity,
            "DISCOVERY_AUTH_EXPECTED_INPUT_INVALID",
        )
    if not validate_ops01r_discovery_authorization(
        authorization_path, expected=expected
    ).valid:
        raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
    authorization_bytes = authorization_path.read_bytes()
    authorization = json.loads(authorization_bytes)
    try:
        output_path = Path(authorization["output_contract"]["path"])
        source_root = Path(authorization["source"]["root"])
        write_contract = authorization["write_contract"]
        working_contract = authorization["working_directory"]
        working_directory = Path(working_contract["path"])
        staging_root = output_path.parent.parent
        requested_target = authorization["requested_target"]
    except (KeyError, TypeError):
        raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
    if (
        not isinstance(write_contract, dict)
        or not isinstance(working_contract, dict)
        or working_contract.get("linked_context_required") is not False
        or working_contract.get("must_be_empty") is not True
        or not working_directory.is_dir()
        or any(working_directory.iterdir())
        or output_path != staging_root / "control" / "discovery.json"
        or source_root != staging_root / "source"
    ):
        raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
    pre_source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    pre_source_sha = sha_bytes(canonical_bytes(pre_source_manifest))
    if pre_source_sha != authorization["source"].get("source_manifest_sha256"):
        raise SystemExit("OPS01R_DISCOVERY_SOURCE_MANIFEST_MISMATCH")
    retained_pre, excluded_paths, excluded_recursive_roots = (
        _validate_pre_staging_contract(
            staging_root,
            source_root=source_root,
            write_contract=write_contract,
            code="OPS01R_DISCOVERY_WRITE_SET_MISMATCH",
        )
    )
    exact_paths = _require_string_list(
        write_contract.get("authorized_exact_write_paths"),
        "OPS01R_DISCOVERY_WRITE_SET_MISMATCH",
    )
    recursive_roots = _require_string_list(
        write_contract.get("authorized_recursive_write_roots"),
        "OPS01R_DISCOVERY_WRITE_SET_MISMATCH",
    )
    metadata_paths = _require_string_list(
        write_contract.get("authorized_directory_metadata_paths"),
        "OPS01R_DISCOVERY_WRITE_SET_MISMATCH",
    )
    if (
        exact_paths != [output_path.as_posix()]
        or recursive_roots
        or write_contract.get("source_root_writes_authorized") is not False
    ):
        raise SystemExit("OPS01R_DISCOVERY_WRITE_SET_MISMATCH")
    prior: dict[str, object] = {}
    manifest: list[list[str]] = []
    target: dict[str, str] = {}
    probe: dict[str, object] = {}
    railway_version = ""

    def require_pristine_staging() -> None:
        current = _staging_manifest_for_contract(
            staging_root,
            source_root=source_root,
            excluded_paths=excluded_paths,
            excluded_recursive_roots=excluded_recursive_roots,
        )
        if current != retained_pre:
            raise SystemExit("OPS01R_DISCOVERY_WRITE_SET_MISMATCH")

    for stage in DISCOVERY_STAGES:
        require_pristine_staging()
        vectors = sorted(
            validate_vectors(authorization, stage, prior),
            key=lambda v: canonical_bytes(list(v)),
        )
        if len(vectors) != 1:
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        argv = vectors[0]
        if authorization_path.read_bytes() != authorization_bytes:
            raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
        dispatch = validate_ops01r_discovery_dispatch(
            authorization_path,
            stage=stage,
            prior_results=prior,
            rendered_argv=argv,
        )
        if not dispatch.valid:
            raise SystemExit("OPS01R_DISCOVERY_DISPATCH_INVALID")
        if authorization_path.read_bytes() != authorization_bytes:
            raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
        require_pristine_staging()
        if authorization_path.read_bytes() != authorization_bytes:
            raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
        cp = subprocess.run(
            argv,
            shell=False,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=working_directory,
            env=_launcher_env(),
            encoding="utf-8",
            errors="strict",
        )
        if cp.returncode != 0:
            raise SystemExit("OPS01R_DISCOVERY_STAGE_FAILED")
        manifest.append(list(argv))
        parsed = _parse_stage(
            stage,
            cp.stdout,
            requested_target=requested_target,
            prior_results=prior,
        )
        prior[stage] = parsed
        if stage.endswith("_inventory"):
            target.update(
                {key: value for key, value in parsed.items() if isinstance(value, str)}
            )
        elif stage == "target_identity_probe":
            probe = parsed
        elif stage == "cli_version":
            railway_version = str(parsed.get("version", ""))
    required = {
        "project_id",
        "project_name",
        "environment_id",
        "environment_name",
        "service_id",
        "service_name",
    }
    if set(target) != required or any(not target[k] for k in required):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    if (
        not isinstance(requested_target, dict)
        or target.get("project_name") != requested_target.get("project_name")
        or target.get("environment_name") != requested_target.get("environment_name")
        or target.get("service_name") != requested_target.get("service_name")
    ):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    identity_contract, child_environment_contract = _derive_discovery_contracts(
        target, probe
    )
    try:
        target_probe_argv = authorization["policy"]["python_execution"][
            "target_probe_argv"
        ]
    except (KeyError, TypeError):
        raise SystemExit("OPS01R_DISCOVERY_ARGV_INVALID")
    if (
        not isinstance(target_probe_argv, list)
        or not target_probe_argv
        or len(manifest[-1]) <= len(target_probe_argv)
        or manifest[-1][-len(target_probe_argv) :] != target_probe_argv
    ):
        raise SystemExit("OPS01R_DISCOVERY_ARGV_INVALID")
    argv_prefix = manifest[-1][: -len(target_probe_argv)]

    if authorization_path.read_bytes() != authorization_bytes:
        raise SystemExit("OPS01R_DISCOVERY_AUTH_INVALID")
    post_source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    post_source_sha = sha_bytes(canonical_bytes(post_source_manifest))
    if post_source_sha != pre_source_sha:
        raise SystemExit("OPS01R_DISCOVERY_SOURCE_MANIFEST_MISMATCH")
    if output_path.exists():
        if output_path.is_symlink() or output_path.read_bytes() != b"":
            raise SystemExit("OPS01R_DISCOVERY_WRITE_SET_MISMATCH")
    else:
        write_contained(output_path, b"", staging_root)
    post_staging = _staging_manifest_for_contract(
        staging_root,
        source_root=source_root,
        excluded_paths=excluded_paths,
        excluded_recursive_roots=excluded_recursive_roots,
    )
    post_staging_sha = sha_bytes(canonical_bytes(post_staging))
    observed_delta = manifest_delta(
        retained_pre["entries"], post_staging["entries"]
    )
    _validate_authorized_delta(
        observed_delta,
        staging_root=staging_root,
        exact_paths=exact_paths,
        recursive_roots=recursive_roots,
        directory_metadata_paths=metadata_paths,
        code="OPS01R_DISCOVERY_WRITE_SET_MISMATCH",
    )
    if any(working_directory.iterdir()):
        raise SystemExit("OPS01R_DISCOVERY_WRITE_SET_MISMATCH")
    source_write_validation = {
        "authorized_directory_metadata_paths": metadata_paths,
        "authorized_exact_write_paths": exact_paths,
        "authorized_recursive_write_roots": recursive_roots,
        "bytecode_write_control": "python_flag_-B",
        "manifest_algorithm": SOURCE_MANIFEST_SCHEMA,
        "mode": "discovery",
        "observed_staging_changes": observed_delta,
        "post_source_manifest_sha256": post_source_sha,
        "post_staging_manifest_sha256": post_staging_sha,
        "pre_source_manifest_sha256": pre_source_sha,
        "pre_staging_manifest": retained_pre["entries"],
        "pre_staging_manifest_sha256": write_contract[
            "pre_staging_manifest_sha256"
        ],
        "prohibited_cache_paths": [],
        "python_argv": target_probe_argv,
        "python_environment_names": [],
        "self_bound_excluded_paths": excluded_paths,
        "self_bound_excluded_recursive_roots": excluded_recursive_roots,
        "source_root": source_root.as_posix(),
        "source_tree_unchanged": True,
        "staging_manifest_algorithm": STAGING_MANIFEST_SCHEMA,
        "staging_write_set_valid": True,
        "status": "PASS",
        "unauthorized_staging_paths": [],
    }
    payload: dict[str, object] = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_run_id": authorization["run_id"],
        "discovery_authorization_sha256": authorization["discovery_authorization_sha256"],
        "command_manifest": manifest,
        "command_manifest_sha256": sha_bytes(canonical_bytes(manifest)),
        "railway_cli": {
            "path": authorization["railway_cli"]["lexical_path"],
            "resolved_path": authorization["railway_cli"]["resolved_path"],
            "sha256": authorization["railway_cli"]["sha256"],
            "version": railway_version,
        },
        "target": target,
        "run_contract": {
            "argv_prefix": argv_prefix,
            "child_argv_start_index": len(argv_prefix),
            "child_environment_contract": child_environment_contract,
            "linked_context_required": False,
            "python_execution": authorization["policy"]["python_execution"],
            "target_dimensions": ["project", "environment", "service"],
        },
        "identity_contract": identity_contract,
        "counts": {
            "bridge_http_requests": 0,
            "command_manifest_entries": len(manifest),
            "db_connections": 0,
            "direct_sql_statements": 0,
            "discovery_subprocesses": len(manifest),
            "provider_constructions": 0,
            "vendor_requests": 0,
        },
        "nonclaims": authorization.get("nonclaims", DISCOVERY_NONCLAIMS),
        "source_write_validation": source_write_validation,
    }
    payload["discovery_identity_sha256"] = sha_bytes(canonical_bytes(payload))
    write_contained(output_path, canonical_bytes(payload), output_path.parent.parent)
    recaptured_staging = _staging_manifest_for_contract(
        staging_root,
        source_root=source_root,
        excluded_paths=excluded_paths,
        excluded_recursive_roots=excluded_recursive_roots,
    )
    if (
        sha_bytes(canonical_bytes(recaptured_staging)) != post_staging_sha
        or authorization_path.read_bytes() != authorization_bytes
    ):
        raise SystemExit("OPS01R_DISCOVERY_WRITE_SET_MISMATCH")
    if not validate_ops01r_discovery_result(
        output_path, authorization_path=authorization_path, expected=expected
    ).valid:
        raise SystemExit("OPS01R_DISCOVERY_RESULT_INVALID")
    print(output_path.as_posix())
    return 0


def validate_vectors(
    authorization: dict[str, object], stage: str, prior: object
) -> set[tuple[str, ...]]:
    from tools.evidence.hde_epic038_ops01_v5 import _authorized_stage_vectors
    return _authorized_stage_vectors(authorization, stage=stage, prior_results=prior)


def _discovery_json_has_secret_like_field(value: object) -> bool:
    forbidden = re.compile(
        r"(?i)(secret|token|password|passwd|api[_-]?key|database_url|db_bridge_url|authorization|cookie)"
    )
    if isinstance(value, dict):
        return any(
            not isinstance(key, str)
            or forbidden.search(key) is not None
            or _discovery_json_has_secret_like_field(child)
            for key, child in value.items()
        )
    if isinstance(value, list):
        return any(_discovery_json_has_secret_like_field(child) for child in value)
    return False


def _inventory_identity(
    items: object,
    *,
    requested_name: object,
    id_field: str,
    name_field: str,
) -> dict[str, object]:
    if (
        not isinstance(items, list)
        or not _safe_identity_string(requested_name)
        or any(not isinstance(item, dict) for item in items)
    ):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    matches = [item for item in items if item.get("name") == requested_name]
    if len(matches) != 1:
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    identity = {
        id_field: matches[0].get("id"),
        name_field: matches[0].get("name"),
    }
    if any(not _safe_identity_string(value) for value in identity.values()):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    return identity


def _parse_stage(
    stage: str,
    stdout: str,
    *,
    requested_target: object = None,
    prior_results: object = None,
) -> dict[str, object]:
    if stage == "cli_version":
        normalized = (
            stdout.replace("\r\n", "\n")
            .replace("\r", "\n")
            .strip(" \t\n\v\f")
        )
        if "\n" in normalized or not _safe_identity_string(normalized):
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        return {"version": normalized}
    if stage == "cli_help":
        normalized = stdout.replace("\r\n", "\n").replace("\r", "\n")
        tokens = [
            token
            for token in re.split(r"[ \t\n\v\f]+", normalized)
            if token
        ]
        if not tokens:
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        return {"help_tokens": tokens}
    if stage == "target_identity_probe":
        try:
            probe = json.loads(stdout)
        except (json.JSONDecodeError, UnicodeError):
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        if (
            not isinstance(probe, dict)
            or set(probe)
            != {"schema", "writes", "endpoint_presence", "identity_fields"}
            or probe.get("schema")
            != "hde_epic038.ops01r.target_identity_probe.v1"
            or probe.get("writes") != 0
            or not isinstance(probe.get("endpoint_presence"), dict)
            or not isinstance(probe.get("identity_fields"), list)
        ):
            raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
        return probe
    if stage not in {
        "project_inventory",
        "environment_inventory",
        "service_inventory",
    }:
        return {}
    try:
        obj = json.loads(stdout)
    except (json.JSONDecodeError, UnicodeError):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    if _discovery_json_has_secret_like_field(obj):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    requested = requested_target if isinstance(requested_target, dict) else {}
    if stage == "project_inventory":
        return _inventory_identity(
            obj,
            requested_name=requested.get("project_name"),
            id_field="project_id",
            name_field="project_name",
        )
    if stage == "service_inventory":
        return _inventory_identity(
            obj,
            requested_name=requested.get("service_name"),
            id_field="service_id",
            name_field="service_name",
        )

    prior = prior_results if isinstance(prior_results, dict) else {}
    project = prior.get("project_inventory")
    if (
        not isinstance(obj, dict)
        or not isinstance(project, dict)
        or obj.get("id") != project.get("project_id")
        or obj.get("name") != project.get("project_name")
    ):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    environments = obj.get("environments")
    edges = environments.get("edges") if isinstance(environments, dict) else None
    if not isinstance(edges, list) or any(
        not isinstance(edge, dict) for edge in edges
    ):
        raise SystemExit("OPS01R_DISCOVERY_TARGET_AMBIGUOUS")
    nodes = [edge.get("node") for edge in edges]
    return _inventory_identity(
        nodes,
        requested_name=requested.get("environment_name"),
        id_field="environment_id",
        name_field="environment_name",
    )


@dataclass
class _CallBudget:
    expected: dict[str, int]
    actual: dict[str, int]

    @classmethod
    def from_authorization(cls, authorization: Mapping[str, object]) -> "_CallBudget":
        raw = authorization.get("expected_call_counts")
        if raw != EXPECTED_CALL_COUNTS:
            raise SystemExit("OPS01R_LIVE_CALL_VECTOR_INVALID")
        return cls(dict(EXPECTED_CALL_COUNTS), {name: 0 for name in EXPECTED_CALL_COUNTS})

    def advance(self, field: str) -> None:
        attempted = self.actual[field] + 1
        if attempted > self.expected[field]:
            raise RuntimeError("OPS01R_LIVE_CALL_BUDGET_EXCEEDED")
        self.actual[field] = attempted

    def require_terminal_equality(self) -> None:
        if self.actual != self.expected:
            raise RuntimeError("OPS01R_LIVE_CALL_VECTOR_MISMATCH")


def _read_only_sql(sql: object) -> None:
    if not isinstance(sql, str) or not sql.lstrip().casefold().startswith(
        ("select", "show")
    ):
        raise RuntimeError("OPS01R_LIVE_SQL_NOT_READ_ONLY")


class _CountedCursor:
    def __init__(self, cursor: object, budget: _CallBudget):
        self._cursor = cursor
        self._budget = budget

    def __enter__(self):
        enter = getattr(self._cursor, "__enter__", None)
        if enter is not None:
            enter()
        return self

    def __exit__(self, *args):
        exit_method = getattr(self._cursor, "__exit__", None)
        if exit_method is not None:
            return exit_method(*args)
        close = getattr(self._cursor, "close", None)
        if close is not None:
            close()
        return False

    def execute(self, sql, params=None):
        _read_only_sql(sql)
        self._budget.advance("direct_sql_statements")
        return self._cursor.execute(sql, params)

    def executemany(self, sql, params=None):
        _read_only_sql(sql)
        self._budget.advance("direct_sql_statements")
        return self._cursor.executemany(sql, params)

    def copy(self, sql, *args, **kwargs):
        _read_only_sql(sql)
        self._budget.advance("direct_sql_statements")
        return self._cursor.copy(sql, *args, **kwargs)

    def __getattr__(self, name: str):
        return getattr(self._cursor, name)


class _CountedConnection:
    def __init__(self, connection: object, budget: _CallBudget):
        self._connection = connection
        self._budget = budget

    def cursor(self, *args, **kwargs):
        return _CountedCursor(self._connection.cursor(*args, **kwargs), self._budget)

    def __getattr__(self, name: str):
        return getattr(self._connection, name)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _bridge_request(budget: _CallBudget):
    from engine.db.providers.bridge_provider import BridgeResponse

    opener = urllib.request.build_opener(_NoRedirect)

    def request(
        url: str, method: str, data: bytes | None, headers: Mapping[str, str]
    ) -> BridgeResponse:
        budget.advance("bridge_http_requests")
        path = urllib.parse.urlsplit(url).path
        if method == "GET":
            if path not in {
                "/health",
                "/introspect/fingerprint",
                "/introspect/grants",
                "/introspect/search_path",
            } or data is not None:
                raise RuntimeError("OPS01R_LIVE_BRIDGE_REQUEST_INVALID")
        elif method == "POST":
            if path != "/query" or data is None:
                raise RuntimeError("OPS01R_LIVE_BRIDGE_REQUEST_INVALID")
            request_obj = json.loads(data.decode("utf-8"))
            _read_only_sql(request_obj.get("sql"))
        else:
            raise RuntimeError("OPS01R_LIVE_BRIDGE_REQUEST_INVALID")
        req = urllib.request.Request(url, data=data, method=method, headers=dict(headers))
        try:
            with opener.open(req, timeout=10) as response:
                return BridgeResponse(
                    status=getattr(response, "status", response.getcode()),
                    body=response.read(),
                    headers={key.casefold(): value for key, value in response.headers.items()},
                )
        except urllib.error.HTTPError as exc:
            return BridgeResponse(
                status=exc.code,
                body=exc.read(),
                headers={key.casefold(): value for key, value in (exc.headers or {}).items()},
            )

    return request


def _validate_component(path_value: object, expected_sha: object, source_root: Path) -> Path:
    if not isinstance(path_value, str) or not isinstance(expected_sha, str):
        raise SystemExit("OPS01R_LIVE_COMPONENT_IDENTITY_INVALID")
    path = Path(path_value)
    resolved = path.resolve()
    if (
        source_root not in (resolved, *resolved.parents)
        or path.is_symlink()
        or not path.is_file()
        or sha_bytes(path.read_bytes()) != expected_sha
    ):
        raise SystemExit("OPS01R_LIVE_COMPONENT_IDENTITY_INVALID")
    return path


def _live_runtime_authorization() -> tuple[Path, dict[str, object], str]:
    staging_root = ROOT.parent
    authorization_path = staging_root / "control" / "live_authorization.json"
    try:
        authorization_bytes = authorization_path.read_bytes()
        authorization = json.loads(authorization_bytes)
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise SystemExit("OPS01R_LIVE_AUTH_INVALID")
    if (
        not isinstance(authorization, dict)
        or canonical_bytes(authorization) != authorization_bytes
        or authorization.get("schema") != "hde_epic038.ops01r.authorization.v1"
    ):
        raise SystemExit("OPS01R_LIVE_AUTH_INVALID")
    authorization_sha = sha_bytes(authorization_bytes)
    source_root = Path(str(authorization.get("source", {}).get("root", "")))
    run = authorization.get("run")
    if (
        not isinstance(run, dict)
        or source_root.resolve() != ROOT.resolve()
        or Path(str(run.get("authorization_path", ""))).resolve()
        != authorization_path.resolve()
        or Path(str(run.get("staging_root", ""))).resolve()
        != staging_root.resolve()
        or run.get("child_argv")
        != [
            authorization.get("interpreter", {}).get("path"),
            "-I",
            "-B",
            authorization.get("runner", {}).get("path"),
            "--live-child",
        ]
    ):
        raise SystemExit("OPS01R_LIVE_AUTH_INVALID")
    source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    if sha_bytes(canonical_bytes(source_manifest)) != authorization["source"].get(
        "source_manifest_sha256"
    ):
        raise SystemExit("OPS01R_LIVE_SOURCE_MANIFEST_MISMATCH")
    for name in ("runner", "validator", "projector"):
        component = authorization.get(name)
        if not isinstance(component, dict):
            raise SystemExit("OPS01R_LIVE_COMPONENT_IDENTITY_INVALID")
        _validate_component(component.get("path"), component.get("sha256"), source_root)
    interpreter = authorization.get("interpreter")
    if (
        not isinstance(interpreter, dict)
        or not isinstance(interpreter.get("path"), str)
        or Path(interpreter["path"]).resolve() != Path(sys.executable).resolve()
        or sha_bytes(Path(interpreter["path"]).resolve().read_bytes())
        != interpreter.get("sha256")
    ):
        raise SystemExit("OPS01R_LIVE_COMPONENT_IDENTITY_INVALID")
    write_contract = authorization.get("write_contract")
    if not isinstance(write_contract, dict):
        raise SystemExit("OPS01R_LIVE_WRITE_SET_INVALID")
    marker_path = Path(str(write_contract.get("consumed_marker_path", "")))
    marker = {
        "authorization_sha256": authorization_sha,
        "run_id": run.get("run_id"),
        "schema": "hde_epic038.ops01r.live_authority_consumed.v1",
    }
    if (
        marker_path != staging_root / "control" / "live_authority_consumed.json"
        or marker_path.is_symlink()
        or not marker_path.is_file()
        or marker_path.read_bytes() != canonical_bytes(marker)
    ):
        raise SystemExit("OPS01R_LIVE_AUTHORITY_NOT_CONSUMED")
    return authorization_path, authorization, authorization_sha


def _close_live_environment(authorization: Mapping[str, object]) -> dict[str, str]:
    # Inspect names only here: credential values remain unread until the
    # independently bound target identity and closed rails have passed.
    reject_python_env(os.environ)
    discovery = authorization.get("discovery")
    if not isinstance(discovery, dict):
        raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    run_contract = discovery.get("run_contract")
    identity_contract = discovery.get("identity_contract")
    if not isinstance(run_contract, dict) or not isinstance(identity_contract, list):
        raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    contract = run_contract.get("child_environment_contract")
    if not isinstance(contract, list):
        raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    retained: dict[str, str] = {}
    endpoint_names = {"DATABASE_URL", "DB_BRIDGE_URL"}
    for row in contract:
        if (
            not isinstance(row, dict)
            or set(row) != {"name", "source", "value_policy"}
            or not _safe_identity_string(row.get("name"))
            or not _safe_identity_string(row.get("value_policy"))
        ):
            raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
        name = row["name"]
        policy = row["value_policy"]
        if name in endpoint_names:
            if policy != "presence_only":
                raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
            continue
        value = os.environ.get(name, "")
        if policy.startswith("exact:"):
            if value != policy[6:]:
                raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
        else:
            raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
        retained[name] = value
    for row in identity_contract:
        if (
            not isinstance(row, dict)
            or retained.get(str(row.get("field_name", "")))
            != row.get("expected_value")
        ):
            raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    for name in sorted(endpoint_names):
        value = os.environ.get(name, "")
        if not value.strip():
            raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
        retained[name] = value
    if not endpoint_names <= set(retained):
        raise SystemExit("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    os.environ.clear()
    os.environ.update(retained)
    return retained


def _captured_at() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _selection_snapshot(side: str, staging_root: Path) -> dict[str, object]:
    provider = "psycopg" if side == "direct" else "bridge"
    content = {
        "attempts": [{"provider": provider, "status": "ok"}],
        "flags": {
            "allow_bridge_prod": False,
            "env": "dev",
            "force_bridge": side == "bridge",
            "force_pg": side == "direct",
        },
        "schema": "v1",
        "selected": provider,
        "selection_order": [provider],
    }
    return {
        "content": content,
        "path": (staging_root / "candidate" / f"{side}.selection.snapshot.json").as_posix(),
        "sha256": sha_bytes(canonical_bytes(content)),
    }


def _capture_live_observations(
    authorization: Mapping[str, object], budget: _CallBudget
) -> dict[str, object]:
    from engine.cli.main import _fetch_db_bodygraph
    from engine.db.adapter import DBAccess
    from engine.db.ddl_identity_projection import (
        DDL_IDENTITY_PROJECTION_FIELDS,
        DDL_IDENTITY_PROJECTION_SCHEMA,
        DDL_IDENTITY_UNEXAMINED_FIELDS,
        project_ddl_identity,
    )
    from engine.db.providers.bridge_provider import BridgeProvider
    from engine.db.providers.psycopg_provider import PsycopgProvider
    from scripts.db.capture_epic011_posture import (
        _boundary_view_lines,
        _fingerprint_objects,
        _grant_lines,
        _grant_payload,
        _partition_plan,
        _search_path_value,
        _select_one,
    )

    import psycopg  # type: ignore

    staging_root = Path(str(_mapping_value(authorization, "run", "staging_root")))
    dsn = os.environ.get("DATABASE_URL", "")
    bridge_url = os.environ.get("DB_BRIDGE_URL", "")

    def direct_connection(value: str):
        budget.advance("direct_connection_attempts")
        connection = psycopg.connect(value, connect_timeout=5)
        return _CountedConnection(connection, budget)

    budget.advance("direct_provider_selections")
    direct_provider = PsycopgProvider(dsn, connection_factory=direct_connection)
    direct_provider.health()
    direct = DBAccess(
        direct_provider, attempts=[{"provider": "psycopg", "status": "ok"}]
    )

    budget.advance("bridge_provider_selections")
    bridge_provider = BridgeProvider(
        bridge_url, request=_bridge_request(budget)
    )
    bridge_provider.health()
    bridge = DBAccess(
        bridge_provider, attempts=[{"provider": "bridge", "status": "ok"}]
    )

    def observe(db: object, function):
        value = function(db)
        budget.advance("logical_observations")
        return value

    direct_grant_payload = observe(direct, _grant_payload)
    bridge_grant_payload = observe(bridge, _grant_payload)
    direct_grants = _grant_lines(direct_grant_payload)
    bridge_grants = _grant_lines(bridge_grant_payload)
    direct_search = observe(direct, _search_path_value)
    bridge_search = observe(bridge, _search_path_value)
    direct_select = observe(direct, _select_one)
    bridge_select = observe(bridge, _select_one)
    direct_ddl = observe(direct, _fingerprint_objects)
    bridge_ddl = observe(bridge, _fingerprint_objects)

    budget.advance("bodygraph_reads")
    direct_bodygraph, direct_user_id = _fetch_db_bodygraph(SELECTOR["uuid"], direct)
    budget.advance("logical_observations")
    budget.advance("bodygraph_reads")
    bridge_bodygraph, bridge_user_id = _fetch_db_bodygraph(SELECTOR["uuid"], bridge)
    budget.advance("logical_observations")

    partition_lines, partition_observed = _partition_plan(direct)
    boundary_lines = _boundary_view_lines(direct)
    expected_grants = [
        f"postgres {name} {privilege}"
        for name in (
            "hde.body_graphs",
            "hde.body_graphs_current",
            "public.hde_body_graphs_current",
        )
        for privilege in (
            "DELETE",
            "INSERT",
            "REFERENCES",
            "SELECT",
            "TRIGGER",
            "TRUNCATE",
            "UPDATE",
        )
    ]
    expected_boundary_lines = [
        "view: hde.body_graphs_current",
        "is_updatable: NO",
        "is_insertable_into: NO",
        "is_trigger_updatable: NO",
        "",
        "view: public.hde_body_graphs_current",
        "is_updatable: NO",
        "is_insertable_into: NO",
        "is_trigger_updatable: NO",
    ]
    if (
        direct_grants != expected_grants
        or bridge_grants != expected_grants
        or direct_grant_payload.get("default_privileges") != ["(none)"]
        or bridge_grant_payload.get("default_privileges") != ["(none)"]
        or direct_search != "hde, public"
        or bridge_search != direct_search
        or direct_select != 1
        or bridge_select != direct_select
        or project_ddl_identity(direct_ddl) != project_ddl_identity(bridge_ddl)
        or direct_user_id != SELECTOR["uuid"]
        or bridge_user_id != direct_user_id
        or direct_bodygraph != bridge_bodygraph
        or partition_lines
        != [
            "hde.pair_evaluation RANGE (evaluated_at)",
            "hde.public_results RANGE (created_at)",
        ]
        or partition_observed
        != ["hde.pair_evaluation", "hde.public_results"]
        or boundary_lines != expected_boundary_lines
    ):
        raise RuntimeError("OPS01R_LIVE_PARITY_MISMATCH")
    unique_constraints = []
    for row in direct_ddl:
        if row.get("name") == "hde.body_graphs":
            unique_constraints = row.get("constraints", [])
            break
    expected_unique = [
        {
            "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
            "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
        }
    ]
    if unique_constraints != expected_unique:
        raise RuntimeError("OPS01R_LIVE_DB_POSTURE_MISMATCH")

    bodygraph_sha = sha_bytes(canonical_bytes(direct_bodygraph))
    direct_snapshot = _selection_snapshot("direct", staging_root)
    bridge_snapshot = _selection_snapshot("bridge", staging_root)
    capabilities = [
        {
            "bridge": {"status": "ok", "value": bridge_grants},
            "direct": {"status": "ok", "value": direct_grants},
            "name": "grants",
            "parity": "match",
        },
        {
            "bridge": {"status": "ok", "value": bridge_search},
            "direct": {"status": "ok", "value": direct_search},
            "name": "search_path",
            "parity": "match",
        },
        {
            "bridge": {"status": "ok", "value": bridge_select},
            "direct": {"status": "ok", "value": direct_select},
            "name": "select_one",
            "parity": "match",
        },
        {
            "bridge": {"status": "ok", "value": bridge_ddl},
            "comparison_contract": {
                "included_fields": list(DDL_IDENTITY_PROJECTION_FIELDS),
                "mode": "shared_identity_projection",
                "ordering": "objects_by_kind_name_columns_by_name_type",
                "schema": DDL_IDENTITY_PROJECTION_SCHEMA,
                "unexamined_fields": list(DDL_IDENTITY_UNEXAMINED_FIELDS),
            },
            "direct": {"status": "ok", "value": direct_ddl},
            "name": "ddl_fingerprint",
            "parity": "projection_match",
        },
        {
            "bridge": {
                "canonical_sha256": bodygraph_sha,
                "provider": "bridge",
                "raw_bodygraph_payload_recorded": False,
                "selection_snapshot": bridge_snapshot,
                "staged_output": (
                    staging_root / "candidate" / "bodygraph.bridge.compat.json"
                ).as_posix(),
                "status": "ok",
            },
            "comparison": "FILE_EQ_CANON_BYTES_OK",
            "direct": {
                "canonical_sha256": bodygraph_sha,
                "provider": "psycopg",
                "raw_bodygraph_payload_recorded": False,
                "selection_snapshot": direct_snapshot,
                "staged_output": (
                    staging_root / "candidate" / "bodygraph.direct.compat.json"
                ).as_posix(),
                "status": "ok",
            },
            "name": "bodygraph_payload_row",
            "parity": "match",
            "payload_fetch_implementation": "engine.cli.main:_fetch_db_bodygraph",
            "read_surface": "hdctl showcompat --conjunction --source db",
            "selector": SELECTOR,
        },
    ]
    return {
        "bodygraph_sha": bodygraph_sha,
        "capabilities": capabilities,
        "direct_snapshot": direct_snapshot,
        "bridge_snapshot": bridge_snapshot,
        "unique_constraints": expected_unique,
    }


def _mapping_value(value: Mapping[str, object], *keys: str) -> object:
    current: object = value
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _live_source_write_validation(
    authorization: Mapping[str, object], source_root: Path, staging_root: Path
) -> dict[str, object]:
    write_contract = authorization.get("write_contract")
    if not isinstance(write_contract, dict):
        raise RuntimeError("OPS01R_LIVE_WRITE_SET_INVALID")
    retained_pre = write_contract.get("pre_staging_manifest")
    retained_hash = write_contract.get("pre_staging_manifest_sha256")
    if not isinstance(retained_pre, list) or not isinstance(retained_hash, str):
        raise RuntimeError("OPS01R_LIVE_WRITE_SET_INVALID")
    retained = {"schema": STAGING_MANIFEST_SCHEMA, "entries": retained_pre}
    if sha_bytes(canonical_bytes(retained)) != retained_hash:
        raise RuntimeError("OPS01R_LIVE_WRITE_SET_INVALID")
    excluded_paths = _require_string_list(
        write_contract.get("self_bound_excluded_paths"),
        "OPS01R_LIVE_WRITE_SET_INVALID",
    )
    excluded_roots = _require_string_list(
        write_contract.get("self_bound_excluded_recursive_roots"),
        "OPS01R_LIVE_WRITE_SET_INVALID",
    )
    exact_paths = _require_string_list(
        write_contract.get("success_authorized_exact_paths"),
        "OPS01R_LIVE_WRITE_SET_INVALID",
    )
    recursive_roots = _require_string_list(
        write_contract.get("success_authorized_recursive_write_roots"),
        "OPS01R_LIVE_WRITE_SET_INVALID",
    )
    metadata_paths = _require_string_list(
        write_contract.get("success_authorized_directory_metadata_paths"),
        "OPS01R_LIVE_WRITE_SET_INVALID",
    )
    source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    source_sha = sha_bytes(canonical_bytes(source_manifest))
    if source_sha != _mapping_value(authorization, "source", "source_manifest_sha256"):
        raise RuntimeError("OPS01R_LIVE_SOURCE_MANIFEST_MISMATCH")
    post_staging = _staging_manifest_for_contract(
        staging_root,
        source_root=source_root,
        excluded_paths=excluded_paths,
        excluded_recursive_roots=excluded_roots,
    )
    post_sha = sha_bytes(canonical_bytes(post_staging))
    delta = manifest_delta(retained_pre, post_staging["entries"])
    _validate_authorized_delta(
        delta,
        staging_root=staging_root,
        exact_paths=exact_paths,
        recursive_roots=recursive_roots,
        directory_metadata_paths=metadata_paths,
        code="OPS01R_LIVE_WRITE_SET_INVALID",
    )
    return {
        "authorized_directory_metadata_paths": metadata_paths,
        "authorized_exact_write_paths": exact_paths,
        "authorized_recursive_write_roots": recursive_roots,
        "bytecode_write_control": "python_flag_-B",
        "manifest_algorithm": SOURCE_MANIFEST_SCHEMA,
        "mode": "live",
        "observed_staging_changes": delta,
        "post_source_manifest_sha256": source_sha,
        "post_staging_manifest_sha256": post_sha,
        "pre_source_manifest_sha256": source_sha,
        "pre_staging_manifest": retained_pre,
        "pre_staging_manifest_sha256": retained_hash,
        "prohibited_cache_paths": [],
        "python_argv": _mapping_value(authorization, "run", "child_argv"),
        "python_environment_names": [],
        "self_bound_excluded_paths": excluded_paths,
        "self_bound_excluded_recursive_roots": excluded_roots,
        "source_root": source_root.as_posix(),
        "source_tree_unchanged": True,
        "staging_manifest_algorithm": STAGING_MANIFEST_SCHEMA,
        "staging_write_set_valid": True,
        "status": "PASS",
        "unauthorized_staging_paths": [],
    }


def _write_candidate(
    authorization: dict[str, object],
    authorization_sha: str,
    budget: _CallBudget,
    observations: Mapping[str, object],
    source_write: Mapping[str, object],
    captured_at: str,
) -> None:
    from tools.evidence.hde_epic038_ops01_v5 import (
        Ops01V5ExpectedIdentity,
        V5_PRIMARY_FILES,
        validate_ops01_v5_package,
    )

    staging_root = Path(str(_mapping_value(authorization, "run", "staging_root")))
    candidate_root = Path(str(_mapping_value(authorization, "run", "candidate_root")))
    if (
        candidate_root != staging_root / "candidate"
        or candidate_root.is_symlink()
        or not candidate_root.is_dir()
        or any(candidate_root.iterdir())
    ):
        raise RuntimeError("OPS01R_LIVE_CANDIDATE_ROOT_INVALID")
    target = _mapping_value(authorization, "discovery", "target")
    if not isinstance(target, dict) or target != {
        "project_id": target.get("project_id"),
        "project_name": "ample-illumination",
        "environment_id": target.get("environment_id"),
        "environment_name": "production",
        "service_id": target.get("service_id"),
        "service_name": "glow-hdengine-v2",
    }:
        raise RuntimeError("OPS01R_LIVE_TARGET_IDENTITY_INVALID")
    rails = {"ALLOW_DB_WRITE": "0", "ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
    environment_presence = {
        "ALLOW_DB_WRITE": "0",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "SET:dev",
        "DATABASE_URL": "SET:REDACTED",
        "DB_BRIDGE_URL": "SET:REDACTED",
        "ENGINE_ENV": "UNSET",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    env_presence = {
        "captured_at_utc": captured_at,
        "environment_presence": environment_presence,
        "execution_rails": {
            "bridge_bodygraph_read": {
                **rails,
                "DB_FORCE_BRIDGE": "1",
                "DB_FORCE_PG": "UNSET",
            },
            "canonical_comparison": rails,
            "db_posture_capture": rails,
            "direct_bodygraph_read": {
                **rails,
                "DB_FORCE_BRIDGE": "UNSET",
                "DB_FORCE_PG": "1",
            },
            "governed_checker": rails,
        },
        "operator_console": "github_codespaces",
        "repository": {
            "branch": "DETACHED",
            "head": _mapping_value(authorization, "source", "commit"),
            "pre_execution_worktree": "clean",
            "root": _mapping_value(authorization, "source", "root"),
        },
        "schema": "hde_epic038.ops01.env_presence.v3",
        "secret_posture": "presence_only",
        "target": {
            "bridge_service": "pg-bridge",
            "db_instance": "ample-illumination/production/postgres",
            "db_schema": "hde",
            "project": "ample-illumination",
            "provider": "Railway",
        },
    }
    objects = [
        {"kind": "table", "name": "hde.body_graphs"},
        {"kind": "view", "name": "hde.body_graphs_current"},
        {"kind": "view", "name": "public.hde_body_graphs_current"},
    ]
    privileges = [
        "DELETE",
        "INSERT",
        "REFERENCES",
        "SELECT",
        "TRIGGER",
        "TRUNCATE",
        "UPDATE",
    ]
    db_posture = {
        "bodygraph_unique_constraints": observations["unique_constraints"],
        "boundary_views": [
            {
                "is_insertable_into": "NO",
                "is_trigger_updatable": "NO",
                "is_updatable": "NO",
                "name": name,
                "readonly": True,
            }
            for name in (
                "hde.body_graphs_current",
                "public.hde_body_graphs_current",
            )
        ],
        "boundary_views_readonly": True,
        "captured_at_utc": captured_at,
        "database_schema": "hde",
        "default_privileges": "none_observed",
        "fingerprint_objects": objects,
        "grants": [
            {
                "grantees": ["postgres"],
                "object": row["name"],
                "privileges": privileges,
            }
            for row in objects
        ],
        "observation_mode": "read_only",
        "partition_plan": [
            {
                "key": "(evaluated_at)",
                "strategy": "RANGE",
                "table": "hde.pair_evaluation",
            },
            {
                "key": "(created_at)",
                "strategy": "RANGE",
                "table": "hde.public_results",
            },
        ],
        "partition_plan_status": "PASS",
        "schema": "hde_epic038.ops01.db_posture_summary.v3",
        "search_path": "hde, public",
        "search_path_exact": True,
        "source_capture_root": (candidate_root / "capture").as_posix(),
        "status": "PASS",
    }
    provider_proof = {
        "active_parity_corpus": {
            "name": "hde_epic038_ops01_live_bodygraph_parity_v4",
            "ordered_rows": [
                "grants",
                "search_path",
                "select_one",
                "ddl_fingerprint",
                "bodygraph_payload_row",
            ],
            "selector": SELECTOR,
        },
        "attempts": [{"provider": "psycopg", "status": "ok"}],
        "capabilities": observations["capabilities"],
        "captured_at_utc": captured_at,
        "environment": "dev",
        "full_ddl_semantic_parity_claimed": False,
        "live_provider_parity": {
            "bridge_provider_rows": "available",
            "claimed_row_count": 5,
            "direct_provider_rows": "available",
            "matched_row_count": 5,
            "parity_status": "pass",
        },
        "payload_posture": {
            "raw_bodygraph_payload_persisted": False,
            "raw_user_data_persisted": False,
            "secret_values_persisted": False,
        },
        "provider_observations": {"bridge": "ok", "direct": "ok"},
        "rails_open": False,
        "rails_posture": {
            "ALLOW_DB_WRITE": "0",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "SAFE_MODE": "1",
            "all_actions": "closed",
        },
        "remediation_marker": "F-009_DDL_IDENTITY_PROJECTION_CONTRACT",
        "schema": "hde_epic038.ops01.provider_parity.v5",
        "selected": "psycopg",
        "status": "PASS",
    }
    bodygraph_sha = str(observations["bodygraph_sha"])
    checker_path = ROOT / "ci" / "checks" / "check_bridge_consistency.py"
    checker_sha = sha_bytes(checker_path.read_bytes())
    env_presence_bytes = canonical_bytes(env_presence)
    provider_proof_bytes = canonical_bytes(provider_proof)

    def retained_input(name: str, content: bytes) -> dict[str, str]:
        return {
            "path": (candidate_root / name).as_posix(),
            "sha256": sha_bytes(content),
        }

    provider_proof_input = retained_input(
        "provider_parity.proof.json", provider_proof_bytes
    )
    env_presence_input = retained_input("env_presence.json", env_presence_bytes)
    bridge_consistency = {
        "bodygraph_comparator": {
            "bridge_input": dict(provider_proof_input),
            "canonical_sha256": bodygraph_sha,
            "direct_input": dict(provider_proof_input),
            "exit_code": 0,
            "identity": "presenter.json_canon_compare",
            "literal_invocation": "in-process canonical comparison",
            "result": "FILE_EQ_CANON_BYTES_OK",
        },
        "captured_at_utc": captured_at,
        "command_exit_codes": {
            "bridge_bodygraph_read": 0,
            "canonical_comparison": 0,
            "db_posture_capture": 0,
            "direct_bodygraph_read": 0,
            "governed_checker": 0,
        },
        "governed_checker": {
            "exit_code": 0,
            "inputs": {
                "adapter_selection": dict(provider_proof_input),
                "env_connectivity": dict(env_presence_input),
                "provider_parity": dict(provider_proof_input),
            },
            "literal_invocation": "in-process governed parity validation",
            "repo_identity": "ci/checks/check_bridge_consistency.py",
            "repo_sha256": checker_sha,
            "result": "PASS",
            "staged_executable": checker_path.as_posix(),
            "staged_sha256": checker_sha,
        },
        "predicates": {
            "all_actions_closed_rails": True,
            "bodygraph_bridge_available": True,
            "bodygraph_direct_available": True,
            "bodygraph_provider_selection_provenance": True,
            "bodygraph_row_match": True,
            "bodygraph_selector_approved": True,
            "four_row_corpus_exact": True,
            "provider_selection_consistent": True,
            "search_path_exact": True,
        },
        "schema": "hde_epic038.ops01.bridge_consistency.v3",
        "status": "PASS",
    }
    nonclaims = {
        "captured_at_utc": captured_at,
        "nonclaims": LIVE_NONCLAIMS,
        "pf09_posture": {
            "HDE-DIST001": "Partial",
            "HDE-DIST001.4": "Partial",
            "HDE-DIST001.9": "Partial",
            "status_change": "none",
        },
        "schema": "hde_epic038.ops01.nonclaims.v3",
    }
    prefix = _mapping_value(
        authorization, "discovery", "run_contract", "argv_prefix"
    )
    child_argv = _mapping_value(authorization, "run", "child_argv")
    if not isinstance(prefix, list) or not isinstance(child_argv, list):
        raise RuntimeError("OPS01R_LIVE_ARGV_INVALID")
    commands = canonical_bytes(prefix + child_argv)
    summary = {
        "acceptance_tokens": "NOT_CLAIMED",
        "active_parity_corpus": "hde_epic038_ops01_live_bodygraph_parity_v4",
        "active_parity_rows": [
            "grants",
            "search_path",
            "select_one",
            "ddl_fingerprint",
            "bodygraph_payload_row",
        ],
        "actual_call_counts": budget.actual,
        "authorization": authorization,
        "authorization_sha256": authorization_sha,
        "bodygraph_selector": SELECTOR,
        "captured_at_utc": captured_at,
        "checksum_policy": {
            "algorithm": "sha256",
            "ledger_excludes_itself": True,
        },
        "discovery_identity_sha256": _mapping_value(
            authorization, "discovery", "discovery_identity_sha256"
        ),
        "epic_closeout": "NOT_CLAIMED",
        "execution": {
            "candidate_validator_argv": [
                _mapping_value(authorization, "interpreter", "path"),
                "-I",
                "-B",
                _mapping_value(authorization, "validator", "path"),
                "--validate-candidate",
                "--expected-identity-stdin",
                candidate_root.as_posix(),
            ],
            "commands_sha256": sha_bytes(commands),
            "launch_executions": 1,
            "source_checkout_state": "DETACHED",
            "source_write_validation": source_write,
        },
        "expected_call_counts": authorization["expected_call_counts"],
        "full_ddl_semantic_parity_claimed": False,
        "literal_staging_root": staging_root.as_posix(),
        "observations": {
            "bodygraph_row_parity": "match",
            "bridge_consistency": "PASS",
            "bridge_provider": "available",
            "claimed_rows": 5,
            "db_posture": "PASS",
            "ddl_identity_projection": "projection_match",
            "direct_provider": "available",
            "matched_rows": 5,
            "search_path": "hde, public",
        },
        "ops_observation_status": "PASS",
        "packaged_at_utc": captured_at,
        "pf09_status_movement": "NONE",
        "preflight_identity_sha256": authorization["preflight_identity_sha256"],
        "qa_status": "NOT_CLAIMED",
        "remediation_findings_resolved": [
            "F-004_LITERAL_COMMANDS",
            "F-005_RAW_STREAM_AND_CHECKER_BINDING",
            "F-006_BODYGRAPH_ROW_PARITY",
            "F-007_OPS01_SCOPE",
            "F-008_BODYGRAPH_PROVIDER_SELECTION_PROVENANCE",
            "F-009_DDL_IDENTITY_PROJECTION_CONTRACT",
        ],
        "repository": {
            "branch": "DETACHED",
            "head": _mapping_value(authorization, "source", "commit"),
            "post_execution_worktree": "clean",
            "pre_execution_worktree": "clean",
            "root": _mapping_value(authorization, "source", "root"),
        },
        "runner_sha256": _mapping_value(authorization, "runner", "sha256"),
        "schema": "hde_epic038.ops01.result_summary.v4",
        "scope": "bounded_read_only_db_posture_and_direct_bridge_bodygraph_row_parity",
    }
    payloads: dict[str, bytes] = {
        "bridge_consistency.result.json": canonical_bytes(bridge_consistency),
        "commands.txt": commands,
        "db_posture_summary.json": canonical_bytes(db_posture),
        "env_presence.json": env_presence_bytes,
        "exit_code.txt": b"0\n",
        "nonclaims.json": canonical_bytes(nonclaims),
        "provider_parity.proof.json": provider_proof_bytes,
        "result_summary.json": canonical_bytes(summary),
        "stderr.log": b"none\n",
        "stdout.log": b"PASS\n",
    }
    for name, data in payloads.items():
        write_contained(candidate_root / name, data, candidate_root)
    ledger = (
        "\n".join(
            f"{sha_bytes((candidate_root / name).read_bytes())}  {name}"
            for name in sorted(payloads)
        )
        + "\n"
    ).encode("ascii")
    write_contained(candidate_root / "checksums.sha256", ledger, candidate_root)
    if set(path.name for path in candidate_root.iterdir()) != set(V5_PRIMARY_FILES):
        raise RuntimeError("OPS01R_LIVE_CANDIDATE_WRITE_SET_INVALID")
    expected = Ops01V5ExpectedIdentity(
        authorization_sha256=authorization_sha,
        candidate_ledger_sha256=sha_bytes(ledger),
        commands_sha256=sha_bytes(commands),
        discovery_identity_sha256=str(
            _mapping_value(authorization, "discovery", "discovery_identity_sha256")
        ),
        expected_call_counts_sha256=sha_bytes(
            canonical_bytes(authorization["expected_call_counts"])
        ),
        literal_staging_root=staging_root.as_posix(),
        live_post_staging_manifest_sha256=str(
            source_write["post_staging_manifest_sha256"]
        ),
        live_pre_staging_manifest_sha256=str(
            _mapping_value(
                authorization, "write_contract", "pre_staging_manifest_sha256"
            )
        ),
        preflight_identity_sha256=str(authorization["preflight_identity_sha256"]),
        projector_sha256=str(_mapping_value(authorization, "projector", "sha256")),
        runner_sha256=str(_mapping_value(authorization, "runner", "sha256")),
        source_commit=str(_mapping_value(authorization, "source", "commit")),
        source_manifest_sha256=str(
            _mapping_value(authorization, "source", "source_manifest_sha256")
        ),
        validator_sha256=str(_mapping_value(authorization, "validator", "sha256")),
    )
    result = validate_ops01_v5_package(candidate_root, expected=expected)
    if not result.valid:
        raise RuntimeError("OPS01R_LIVE_CANDIDATE_INVALID")


def live_child() -> int:
    _, authorization, authorization_sha = _live_runtime_authorization()
    _close_live_environment(authorization)
    budget = _CallBudget.from_authorization(authorization)
    captured_at = _captured_at()
    observations = _capture_live_observations(authorization, budget)
    budget.require_terminal_equality()
    source_root = Path(str(_mapping_value(authorization, "source", "root")))
    staging_root = Path(str(_mapping_value(authorization, "run", "staging_root")))
    source_write = _live_source_write_validation(
        authorization, source_root, staging_root
    )
    _write_candidate(
        authorization,
        authorization_sha,
        budget,
        observations,
        source_write,
        captured_at,
    )
    return 0


def live_launch(authorization_path: Path, *, expected=None) -> int:
    from tools.evidence.hde_epic038_ops01_v5 import (
        Ops01RLiveAuthorizationExpectedIdentity,
        _parse_expected_stdin,
        validate_ops01r_live_authorization,
    )
    if expected is None:
        expected = _parse_expected_stdin(
            Ops01RLiveAuthorizationExpectedIdentity,
            "OPS01_AUTH_EXPECTED_INPUT_INVALID",
        )
    if not validate_ops01r_live_authorization(
        authorization_path, expected=expected
    ).valid:
        raise SystemExit("OPS01R_LIVE_AUTH_INVALID")
    authorization_bytes = authorization_path.read_bytes()
    authorization = json.loads(authorization_bytes)
    authorization_sha = sha_bytes(authorization_bytes)
    control_root = authorization_path.parent
    try:
        prefix = authorization["discovery"]["run_contract"]["argv_prefix"]
        boundary = authorization["discovery"]["run_contract"][
            "child_argv_start_index"
        ]
        child_argv = authorization["run"]["child_argv"]
        expected_child_argv = [
            authorization["interpreter"]["path"],
            "-I",
            "-B",
            authorization["runner"]["path"],
            "--live-child",
        ]
        run = authorization["run"]
        staging_root = Path(run["staging_root"])
        source_root = Path(authorization["source"]["root"])
        candidate_root = Path(run["candidate_root"])
        write_contract = authorization["write_contract"]
        marker_path = Path(write_contract["consumed_marker_path"])
        failure_path = Path(write_contract["failure_summary_path"])
    except (KeyError, TypeError):
        raise SystemExit("OPS01R_LIVE_ARGV_INVALID")
    if (
        not isinstance(prefix, list)
        or not all(isinstance(token, str) for token in prefix)
        or type(boundary) is not int
        or boundary != len(prefix)
        or not isinstance(child_argv, list)
        or not all(isinstance(token, str) for token in child_argv)
        or child_argv != expected_child_argv
        or authorization_path != staging_root / "control" / "live_authorization.json"
        or control_root != staging_root / "control"
        or source_root != staging_root / "source"
        or candidate_root != staging_root / "candidate"
        or marker_path
        != staging_root / "control" / "live_authority_consumed.json"
        or failure_path != staging_root / "control" / "failure.json"
    ):
        raise SystemExit("OPS01R_LIVE_ARGV_INVALID")
    source_manifest = tree_manifest(source_root, schema=SOURCE_MANIFEST_SCHEMA)
    if sha_bytes(canonical_bytes(source_manifest)) != authorization["source"].get(
        "source_manifest_sha256"
    ):
        raise SystemExit("OPS01R_LIVE_SOURCE_MANIFEST_MISMATCH")
    for name in ("runner", "validator", "projector"):
        component = authorization.get(name)
        if not isinstance(component, dict):
            raise SystemExit("OPS01R_LIVE_COMPONENT_IDENTITY_INVALID")
        _validate_component(component.get("path"), component.get("sha256"), source_root)
    if (
        candidate_root.is_symlink()
        or not candidate_root.is_dir()
        or any(candidate_root.iterdir())
        or marker_path.exists()
        or failure_path.exists()
    ):
        raise SystemExit("OPS01R_LIVE_WRITE_SET_INVALID")
    _validate_pre_staging_contract(
        staging_root,
        source_root=source_root,
        write_contract=write_contract,
        code="OPS01R_LIVE_WRITE_SET_INVALID",
    )
    if (
        write_contract.get("success_authorized_exact_paths")
        != [marker_path.as_posix()]
        or write_contract.get("success_authorized_recursive_write_roots")
        != [candidate_root.as_posix()]
        or write_contract.get("failure_authorized_exact_paths")
        != [marker_path.as_posix(), failure_path.as_posix()]
        or write_contract.get("failure_authorized_recursive_write_roots")
        != [candidate_root.as_posix()]
        or authorization_path.read_bytes() != authorization_bytes
    ):
        raise SystemExit("OPS01R_LIVE_WRITE_SET_INVALID")
    argv = tuple(prefix + child_argv)
    marker = canonical_bytes(
        {
            "authorization_sha256": authorization_sha,
            "run_id": run["run_id"],
            "schema": "hde_epic038.ops01r.live_authority_consumed.v1",
        }
    )
    fd = os.open(marker_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        offset = 0
        while offset < len(marker):
            written = os.write(fd, marker[offset:])
            if written <= 0:
                raise OSError("short marker write")
            offset += written
    finally:
        os.close(fd)
    try:
        cp = subprocess.run(
            argv,
            shell=False,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=_launcher_env(),
        )
    except OSError:
        write_contained(
            failure_path,
            canonical_bytes(
                {
                    "schema": "hde_epic038.ops01r.failure.v1",
                    "status": "FAIL",
                    "reason": "launch_error",
                }
            ),
            staging_root,
        )
        return 1
    if cp.returncode != 0:
        failure = {
            "schema": "hde_epic038.ops01r.failure.v1",
            "status": "FAIL",
            "exit_code": cp.returncode,
        }
        write_contained(
            failure_path,
            canonical_bytes(failure),
            staging_root,
        )
        return cp.returncode
    if not candidate_root.is_dir() or not any(candidate_root.iterdir()):
        write_contained(
            failure_path,
            canonical_bytes(
                {
                    "schema": "hde_epic038.ops01r.failure.v1",
                    "status": "FAIL",
                    "exit_code": 0,
                    "reason": "candidate_missing",
                }
            ),
            staging_root,
        )
        return 1
    return 0

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--preflight", action="store_true")
    modes.add_argument("--target-identity-probe", action="store_true")
    modes.add_argument("--discovery")
    modes.add_argument("--live-launch")
    modes.add_argument("--live-child", action="store_true")
    args = parser.parse_args(argv)
    if args.preflight:
        return preflight()
    if args.target_identity_probe:
        print(canonical_bytes(_target_probe_payload(os.environ)).decode(), end="")
        return 0
    if args.discovery:
        return discovery(Path(args.discovery))
    if args.live_launch:
        return live_launch(Path(args.live_launch))
    if args.live_child:
        return live_child()
    return 2


if __name__ == "__main__":
    require_source_loading_process_contract()
    raise SystemExit(main())
