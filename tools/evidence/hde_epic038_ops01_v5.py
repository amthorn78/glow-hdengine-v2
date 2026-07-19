#!/usr/bin/env python3
"""Dormant read-only HDE-EPIC038 OPS-01 v5 validators."""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import stat
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Type, TypeVar

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db.ddl_identity_projection import (
    DDL_IDENTITY_PROJECTION_FIELDS,
    DDL_IDENTITY_PROJECTION_SCHEMA,
    DDL_IDENTITY_UNEXAMINED_FIELDS,
    project_ddl_identity,
)
from tools.evidence.retained_evidence_safety import validate_retained_text_safety


@dataclass(frozen=True)
class Ops01V5ValidationResult:
    valid: bool
    errors: tuple[str, ...]


@dataclass(frozen=True)
class Ops01V5ExpectedIdentity:
    authorization_sha256: str
    candidate_ledger_sha256: str
    commands_sha256: str
    discovery_identity_sha256: str
    expected_call_counts_sha256: str
    literal_staging_root: str
    live_post_staging_manifest_sha256: str
    live_pre_staging_manifest_sha256: str
    preflight_identity_sha256: str
    projector_sha256: str
    runner_sha256: str
    source_commit: str
    source_manifest_sha256: str
    validator_sha256: str


@dataclass(frozen=True)
class Ops01RPreflightExpectedIdentity:
    source_commit: str
    source_manifest_sha256: str
    pre_staging_manifest_sha256: str
    literal_staging_root: str
    runner_sha256: str
    validator_sha256: str
    projector_sha256: str
    interpreter_sha256: str
    railway_executable_sha256: str
    preflight_identity_sha256: str


@dataclass(frozen=True)
class Ops01RDiscoveryAuthorizationExpectedIdentity:
    discovery_authorization_sha256: str
    discovery_entry_point_sha256: str
    literal_staging_root: str
    pre_staging_manifest_sha256: str
    preflight_identity_sha256: str
    railway_executable_sha256: str
    source_commit: str
    source_manifest_sha256: str


@dataclass(frozen=True)
class Ops01RLiveAuthorizationExpectedIdentity:
    authorization_sha256: str
    discovery_identity_sha256: str
    interpreter_sha256: str
    live_pre_staging_manifest_sha256: str
    literal_staging_root: str
    preflight_identity_sha256: str
    projector_sha256: str
    railway_executable_sha256: str
    runner_sha256: str
    source_commit: str
    source_manifest_sha256: str
    validator_sha256: str


V5_PRIMARY_FILES = (
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_code.txt",
    "env_presence.json",
    "db_posture_summary.json",
    "provider_parity.proof.json",
    "bridge_consistency.result.json",
    "nonclaims.json",
    "result_summary.json",
    "checksums.sha256",
)
CALL_COUNT_FIELDS = (
    "bodygraph_reads",
    "bridge_http_requests",
    "bridge_provider_selections",
    "direct_connection_attempts",
    "direct_provider_selections",
    "direct_sql_statements",
    "fallbacks",
    "logical_observations",
    "retries",
    "vendor_requests",
)
FIXED_COUNTS = {
    "logical_observations": 10,
    "bodygraph_reads": 2,
    "direct_connection_attempts": 8,
    "direct_sql_statements": 13,
    "bridge_http_requests": 6,
    "direct_provider_selections": 1,
    "bridge_provider_selections": 1,
    "vendor_requests": 0,
    "retries": 0,
    "fallbacks": 0,
}

PREFLIGHT_TOP_LEVEL_KEYS = {
    "actual_external_io_counts",
    "components",
    "expected_call_counts",
    "interpreter",
    "module_origins",
    "nonclaims",
    "orchestration",
    "preflight_identity_sha256",
    "railway_executable",
    "run",
    "schema",
    "source",
    "source_write_validation",
    "status",
}
PREFLIGHT_RUN_KEYS = {
    "control_root",
    "preflight_path",
    "run_id",
    "source_root",
    "staging_root",
    "working_directory",
}
PREFLIGHT_SOURCE_KEYS = {
    "checkout_state",
    "commit",
    "repository",
    "root",
    "source_manifest_sha256",
    "worktree_state",
}
PREFLIGHT_INTERPRETER_KEYS = {
    "bytecode_flag",
    "bytecode_write_control",
    "isolated_flag",
    "lexical_path",
    "preflight_argv",
    "preflight_validator_argv",
    "python_environment_names",
    "resolved_path",
    "sha256",
}
PREFLIGHT_ORCHESTRATION_KEYS = {
    "derived_call_counts",
    "deterministic",
    "identity_sha256",
    "runs",
    "schema",
}

DISCOVERY_RESULT_KEYS = {
    "schema",
    "status",
    "discovery_run_id",
    "discovery_authorization_sha256",
    "command_manifest",
    "command_manifest_sha256",
    "railway_cli",
    "target",
    "run_contract",
    "identity_contract",
    "counts",
    "nonclaims",
    "source_write_validation",
    "discovery_identity_sha256",
}
SOURCE_WRITE_KEYS = {
    "authorized_directory_metadata_paths",
    "authorized_exact_write_paths",
    "authorized_recursive_write_roots",
    "bytecode_write_control",
    "manifest_algorithm",
    "mode",
    "observed_staging_changes",
    "post_source_manifest_sha256",
    "post_staging_manifest_sha256",
    "pre_source_manifest_sha256",
    "pre_staging_manifest",
    "pre_staging_manifest_sha256",
    "prohibited_cache_paths",
    "python_argv",
    "python_environment_names",
    "self_bound_excluded_paths",
    "self_bound_excluded_recursive_roots",
    "source_root",
    "source_tree_unchanged",
    "staging_manifest_algorithm",
    "staging_write_set_valid",
    "status",
    "unauthorized_staging_paths",
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
PREFLIGHT_NONCLAIMS = (
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
)

DISCOVERY_AUTH_KEYS = {
    "discovery_authorization_sha256",
    "discovery_entry_point",
    "nonclaims",
    "output_contract",
    "policy",
    "preflight",
    "railway_cli",
    "requested_target",
    "run_id",
    "schema",
    "source",
    "working_directory",
    "write_contract",
}
DISCOVERY_POLICY_STAGE_KEYS = {"stage", "templates"}
DISCOVERY_POLICY_TEMPLATE_KEYS = {
    "argv",
    "required_help_tokens",
    "template_id",
    "version_regex",
}
DISCOVERY_POLICY_DESCRIPTOR_KINDS = {"literal", "prior_result", "python_child"}

DISCOVERY_STAGES = (
    "cli_version",
    "cli_help",
    "project_inventory",
    "environment_inventory",
    "service_inventory",
    "target_identity_probe",
)
SELECTOR = {
    "alias": "epic011-s10-invariance-1",
    "identity_source": "docs/run/EPIC011_TEST_IDENTITIES.md",
    "non_pii": True,
    "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afab",
}

RESULT_SUMMARY_KEYS = {
    "actual_call_counts",
    "authorization",
    "authorization_sha256",
    "checksum_policy",
    "corpus",
    "discovery_identity_sha256",
    "execution",
    "expected_call_counts",
    "full_ddl_semantic_parity_claimed",
    "literal_staging_root",
    "nonclaims",
    "observation",
    "preflight_identity_sha256",
    "remediation",
    "repository",
    "runner_sha256",
    "schema",
    "scope",
    "selector",
}

PROVIDER_PROOF_KEYS = {
    "active_parity_corpus",
    "attempts",
    "capabilities",
    "captured_at_utc",
    "environment",
    "full_ddl_semantic_parity_claimed",
    "live_provider_parity",
    "payload_posture",
    "provider_observations",
    "rails_open",
    "rails_posture",
    "remediation_marker",
    "schema",
    "selected",
    "status",
}
NONCLAIMS = (
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
)
EXPECTED_PRIVILEGES = (
    "DELETE",
    "INSERT",
    "REFERENCES",
    "SELECT",
    "TRIGGER",
    "TRUNCATE",
    "UPDATE",
)
T = TypeVar("T")


def _result(errors: set[str]) -> Ops01V5ValidationResult:
    return Ops01V5ValidationResult(not errors, tuple(sorted(errors)))


def _canon(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("ascii")


def _no_duplicate_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    if len({key for key, _ in pairs}) != len(pairs):
        raise ValueError("duplicate key")
    return dict(pairs)


def _read_json(path: Path) -> object:
    return json.loads(
        path.read_text("utf-8"),
        object_pairs_hook=_no_duplicate_object,
    )


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _tree_manifest(
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
    for excluded in (*excluded_exact, *excluded_roots):
        if root not in (excluded, *excluded.parents):
            raise ValueError("manifest exclusion escapes its root")

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
            raise ValueError("source or staging cache residue detected")
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
            payload = path.read_bytes()
            entry["kind"] = "regular_file"
            entry["sha256"] = _sha(payload)
            entry["size"] = len(payload)
        elif stat.S_ISLNK(metadata.st_mode):
            entry["kind"] = "symlink"
            entry["target"] = os.readlink(path)
        else:
            raise ValueError("unsupported filesystem kind")
        entries.append(entry)
        if entry["kind"] == "directory":
            for child in sorted(
                path.iterdir(), key=lambda item: item.name.encode("utf-8")
            ):
                visit(_lexical_absolute(child))

    visit(root)
    return {
        "schema": schema,
        "entries": sorted(
            entries, key=lambda item: str(item["path"]).encode("utf-8")
        ),
    }


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _has_exact_keys(value: object, keys: set[str]) -> bool:
    return isinstance(value, Mapping) and set(value) == keys


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _path_is_beneath(value: object, root: object) -> bool:
    if not isinstance(value, str) or not isinstance(root, str):
        return False
    path = _lexical_absolute(Path(value))
    parent = _lexical_absolute(Path(root))
    return parent in (path, *path.parents)


def _at(value: object, *keys: str) -> object:
    current = value
    for key in keys:
        current = _mapping(current).get(key)
    return current


def _self_hash(value: Mapping[str, object], field: str) -> str:
    return _sha(_canon({key: item for key, item in value.items() if key != field}))


def _all_expected_values_match(actual: Mapping[str, object], expected: object) -> bool:
    return all(
        actual.get(field.name) == getattr(expected, field.name)
        for field in dataclasses.fields(expected)
    )


def _candidate_expected_errors(
    actual: Mapping[str, object], expected: Ops01V5ExpectedIdentity
) -> set[str]:
    errors: set[str] = set()
    for field in dataclasses.fields(expected):
        if actual.get(field.name) != getattr(expected, field.name):
            errors.add(f"OPS01_V5_{field.name.upper()}_MISMATCH")
    return errors


def _parse_expected_stdin(cls: Type[T], error_code: str) -> T:
    try:
        descriptor = os.fstat(0)
        if os.isatty(0) or not stat.S_ISFIFO(descriptor.st_mode):
            raise ValueError("expected identity must arrive over an anonymous pipe")
        data = os.read(0, 16_385)
        if len(data) > 16_384 or os.read(0, 1) != b"":
            raise ValueError("expected identity input is oversized or has trailing data")
        if (
            data.startswith(b"\xef\xbb\xbf")
            or b"\r" in data
            or data.count(b"\n") != 1
            or not data.endswith(b"\n")
        ):
            raise ValueError("expected identity framing is invalid")
        text = data.decode("ascii")
        obj = json.loads(text, object_pairs_hook=_no_duplicate_object)
        keys = tuple(field.name for field in dataclasses.fields(cls))
        if (
            not isinstance(obj, dict)
            or set(obj) != set(keys)
            or any(not isinstance(obj[key], str) for key in keys)
        ):
            raise ValueError("expected identity roster is invalid")
        if _canon(obj) != data:
            raise ValueError("expected identity is not canonical")
        return cls(**obj)
    except Exception as exc:
        raise SystemExit(error_code) from exc


def _candidate_actual_identity(
    summary: Mapping[str, object], *, ledger_bytes: bytes, commands_bytes: bytes
) -> tuple[dict[str, object], set[str]]:
    errors: set[str] = set()
    authorization = _mapping(summary.get("authorization"))
    discovery = _mapping(authorization.get("discovery"))
    execution = _mapping(summary.get("execution"))
    source_write = _mapping(execution.get("source_write_validation"))

    authorization_sha256 = _sha(_canon(authorization))
    discovery_identity_sha256 = _self_hash(discovery, "discovery_identity_sha256")
    commands_sha256 = _sha(commands_bytes)
    candidate_ledger_sha256 = _sha(ledger_bytes)
    expected_call_counts = authorization.get("expected_call_counts")
    expected_call_counts_sha256 = _sha(_canon(expected_call_counts))

    actual: dict[str, object] = {
        "authorization_sha256": authorization_sha256,
        "candidate_ledger_sha256": candidate_ledger_sha256,
        "commands_sha256": commands_sha256,
        "discovery_identity_sha256": discovery_identity_sha256,
        "expected_call_counts_sha256": expected_call_counts_sha256,
        "literal_staging_root": _at(authorization, "run", "staging_root"),
        "live_post_staging_manifest_sha256": source_write.get(
            "post_staging_manifest_sha256"
        ),
        "live_pre_staging_manifest_sha256": _at(
            authorization, "write_contract", "pre_staging_manifest_sha256"
        ),
        "preflight_identity_sha256": authorization.get(
            "preflight_identity_sha256"
        ),
        "projector_sha256": _at(authorization, "projector", "sha256"),
        "runner_sha256": _at(authorization, "runner", "sha256"),
        "source_commit": _at(authorization, "source", "commit"),
        "source_manifest_sha256": _at(
            authorization, "source", "source_manifest_sha256"
        ),
        "validator_sha256": _at(authorization, "validator", "sha256"),
    }

    consistency_checks = (
        (summary.get("authorization_sha256"), authorization_sha256, "AUTHORIZATION_SHA256"),
        (_at(execution, "commands_sha256"), commands_sha256, "COMMANDS_SHA256"),
        (
            summary.get("discovery_identity_sha256"),
            discovery_identity_sha256,
            "DISCOVERY_IDENTITY_SHA256",
        ),
        (
            discovery.get("discovery_identity_sha256"),
            discovery_identity_sha256,
            "DISCOVERY_IDENTITY_SHA256",
        ),
        (
            summary.get("literal_staging_root"),
            actual["literal_staging_root"],
            "LITERAL_STAGING_ROOT",
        ),
        (
            summary.get("preflight_identity_sha256"),
            actual["preflight_identity_sha256"],
            "PREFLIGHT_IDENTITY_SHA256",
        ),
        (summary.get("runner_sha256"), actual["runner_sha256"], "RUNNER_SHA256"),
        (
            _at(summary, "repository", "head"),
            actual["source_commit"],
            "SOURCE_COMMIT",
        ),
        (
            source_write.get("pre_source_manifest_sha256"),
            actual["source_manifest_sha256"],
            "SOURCE_MANIFEST_SHA256",
        ),
        (
            source_write.get("post_source_manifest_sha256"),
            actual["source_manifest_sha256"],
            "SOURCE_MANIFEST_SHA256",
        ),
        (
            source_write.get("pre_staging_manifest_sha256"),
            actual["live_pre_staging_manifest_sha256"],
            "LIVE_PRE_STAGING_MANIFEST_SHA256",
        ),
        (
            summary.get("expected_call_counts"),
            expected_call_counts,
            "EXPECTED_CALL_COUNTS",
        ),
        (
            summary.get("actual_call_counts"),
            expected_call_counts,
            "ACTUAL_CALL_COUNTS",
        ),
    )
    for retained, recomputed, label in consistency_checks:
        if retained != recomputed:
            errors.add(f"OPS01_V5_{label}_MISMATCH")

    if "expected_call_counts_sha256" in summary or "expected_call_counts_sha256" in authorization:
        errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
    return actual, errors


def _provider_value(value: object) -> Mapping[str, object]:
    if not _has_exact_keys(value, {"status", "value"}):
        return {}
    row = _mapping(value)
    return row if row.get("status") == "ok" else {}


def _validate_selection_snapshot(
    value: object, *, side: str, staging_root: str
) -> bool:
    if not _has_exact_keys(value, {"content", "path", "sha256"}):
        return False
    snapshot = _mapping(value)
    content = snapshot.get("content")
    if not _has_exact_keys(
        content, {"attempts", "flags", "schema", "selected", "selection_order"}
    ):
        return False
    content = _mapping(content)
    provider = "psycopg" if side == "direct" else "bridge"
    expected_flags = {
        "allow_bridge_prod": False,
        "env": "dev",
        "force_bridge": side == "bridge",
        "force_pg": side == "direct",
    }
    return (
        content.get("schema") == "v1"
        and content.get("selected") == provider
        and content.get("attempts") == [{"provider": provider, "status": "ok"}]
        and content.get("selection_order") == [provider]
        and _has_exact_keys(content.get("flags"), set(expected_flags))
        and content.get("flags") == expected_flags
        and _path_is_beneath(snapshot.get("path"), staging_root)
        and snapshot.get("sha256") == _sha(_canon(content))
    )


def _provider_proof_valid(
    proof: Mapping[str, object], *, staging_root: str
) -> bool:
    if set(proof) != PROVIDER_PROOF_KEYS:
        return False
    active = proof.get("active_parity_corpus")
    if not _has_exact_keys(active, {"name", "ordered_rows", "selector"}):
        return False
    active = _mapping(active)
    ordered_rows = (
        "grants",
        "search_path",
        "select_one",
        "ddl_fingerprint",
        "bodygraph_payload_row",
    )
    if (
        proof.get("schema") != "hde_epic038.ops01.provider_parity.v5"
        or proof.get("status") != "PASS"
        or proof.get("selected") != "psycopg"
        or proof.get("environment") != "dev"
        or proof.get("rails_open") is not False
        or proof.get("full_ddl_semantic_parity_claimed") is not False
        or proof.get("remediation_marker")
        != "F-009_DDL_IDENTITY_PROJECTION_CONTRACT"
        or not isinstance(proof.get("captured_at_utc"), str)
        or not proof.get("captured_at_utc")
        or active.get("name")
        != "hde_epic038_ops01_live_bodygraph_parity_v4"
        or tuple(active.get("ordered_rows", ())) != ordered_rows
        or active.get("selector") != SELECTOR
        or proof.get("attempts") != [{"provider": "psycopg", "status": "ok"}]
        or proof.get("live_provider_parity")
        != {
            "bridge_provider_rows": "available",
            "claimed_row_count": 5,
            "direct_provider_rows": "available",
            "matched_row_count": 5,
            "parity_status": "pass",
        }
        or proof.get("payload_posture")
        != {
            "raw_bodygraph_payload_persisted": False,
            "raw_user_data_persisted": False,
            "secret_values_persisted": False,
        }
        or proof.get("provider_observations")
        != {"bridge": "ok", "direct": "ok"}
        or proof.get("rails_posture")
        != {
            "ALLOW_DB_WRITE": "0",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "SAFE_MODE": "1",
            "all_actions": "closed",
        }
    ):
        return False

    capabilities = proof.get("capabilities")
    if not isinstance(capabilities, list) or len(capabilities) != len(ordered_rows):
        return False
    for index, name in enumerate(ordered_rows[:3]):
        row = capabilities[index]
        if not _has_exact_keys(row, {"name", "direct", "bridge", "parity"}):
            return False
        row = _mapping(row)
        direct = _provider_value(row.get("direct"))
        bridge = _provider_value(row.get("bridge"))
        if (
            row.get("name") != name
            or row.get("parity") != "match"
            or not direct
            or not bridge
            or direct.get("value") != bridge.get("value")
        ):
            return False

    ddl = capabilities[3]
    if not _has_exact_keys(
        ddl, {"name", "direct", "bridge", "parity", "comparison_contract"}
    ):
        return False
    ddl = _mapping(ddl)
    direct_ddl = _provider_value(ddl.get("direct"))
    bridge_ddl = _provider_value(ddl.get("bridge"))
    comparison = ddl.get("comparison_contract")
    if not _has_exact_keys(
        comparison,
        {"schema", "mode", "included_fields", "unexamined_fields", "ordering"},
    ):
        return False
    comparison = _mapping(comparison)
    try:
        direct_projection = project_ddl_identity(direct_ddl.get("value"))
        bridge_projection = project_ddl_identity(bridge_ddl.get("value"))
    except (TypeError, ValueError):
        return False
    if (
        ddl.get("name") != "ddl_fingerprint"
        or ddl.get("parity") != "projection_match"
        or not direct_ddl
        or not bridge_ddl
        or direct_projection != bridge_projection
        or comparison.get("schema") != DDL_IDENTITY_PROJECTION_SCHEMA
        or comparison.get("mode") != "shared_identity_projection"
        or tuple(comparison.get("included_fields", ()))
        != DDL_IDENTITY_PROJECTION_FIELDS
        or tuple(comparison.get("unexamined_fields", ()))
        != DDL_IDENTITY_UNEXAMINED_FIELDS
        or comparison.get("ordering")
        != "objects_by_kind_name_columns_by_name_type"
    ):
        return False

    bodygraph = capabilities[4]
    if not _has_exact_keys(
        bodygraph,
        {
            "name",
            "direct",
            "bridge",
            "parity",
            "comparison",
            "payload_fetch_implementation",
            "read_surface",
            "selector",
        },
    ):
        return False
    bodygraph = _mapping(bodygraph)
    sides: dict[str, Mapping[str, object]] = {}
    for side, provider in (("direct", "psycopg"), ("bridge", "bridge")):
        side_value = bodygraph.get(side)
        if not _has_exact_keys(
            side_value,
            {
                "canonical_sha256",
                "provider",
                "raw_bodygraph_payload_recorded",
                "selection_snapshot",
                "staged_output",
                "status",
            },
        ):
            return False
        side_value = _mapping(side_value)
        if (
            side_value.get("provider") != provider
            or side_value.get("status") != "ok"
            or side_value.get("raw_bodygraph_payload_recorded") is not False
            or not _is_sha256(side_value.get("canonical_sha256"))
            or not _path_is_beneath(side_value.get("staged_output"), staging_root)
            or not _validate_selection_snapshot(
                side_value.get("selection_snapshot"),
                side=side,
                staging_root=staging_root,
            )
        ):
            return False
        sides[side] = side_value
    return (
        bodygraph.get("name") == "bodygraph_payload_row"
        and bodygraph.get("parity") == "match"
        and bodygraph.get("comparison") == "FILE_EQ_CANON_BYTES_OK"
        and bodygraph.get("payload_fetch_implementation")
        == "engine.cli.main:_fetch_db_bodygraph"
        and bodygraph.get("read_surface")
        == "hdctl showcompat --conjunction --source db"
        and bodygraph.get("selector") == SELECTOR
        and sides["direct"].get("canonical_sha256")
        == sides["bridge"].get("canonical_sha256")
    )


def _env_presence_valid(
    value: Mapping[str, object], *, authorization: Mapping[str, object]
) -> bool:
    rails = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "ALLOW_DB_WRITE": "0"}
    expected_environment = {
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
    expected_execution = {
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
    }
    repository = value.get("repository")
    target = value.get("target")
    return (
        _has_exact_keys(
            value,
            {
                "captured_at_utc",
                "environment_presence",
                "execution_rails",
                "operator_console",
                "repository",
                "schema",
                "secret_posture",
                "target",
            },
        )
        and value.get("schema") == "hde_epic038.ops01.env_presence.v3"
        and value.get("operator_console") == "github_codespaces"
        and value.get("secret_posture") == "presence_only"
        and value.get("environment_presence") == expected_environment
        and value.get("execution_rails") == expected_execution
        and _has_exact_keys(
            repository, {"branch", "head", "pre_execution_worktree", "root"}
        )
        and _mapping(repository).get("branch") == "DETACHED"
        and _mapping(repository).get("head") == _at(authorization, "source", "commit")
        and _mapping(repository).get("root") == _at(authorization, "source", "root")
        and _mapping(repository).get("pre_execution_worktree") == "clean"
        and _has_exact_keys(
            target, {"bridge_service", "db_instance", "db_schema", "project", "provider"}
        )
        and _mapping(target).get("bridge_service") == "pg-bridge"
        and _mapping(target).get("db_instance")
        == "ample-illumination/production/postgres"
        and _mapping(target).get("db_schema") == "hde"
        and _mapping(target).get("project") == "ample-illumination"
        and _mapping(target).get("provider") == "Railway"
    )


def _db_posture_valid(value: Mapping[str, object], *, staging_root: str) -> bool:
    objects = (
        {"kind": "table", "name": "hde.body_graphs"},
        {"kind": "view", "name": "hde.body_graphs_current"},
        {"kind": "view", "name": "public.hde_body_graphs_current"},
    )
    views = tuple(
        {
            "is_insertable_into": "NO",
            "is_trigger_updatable": "NO",
            "is_updatable": "NO",
            "name": name,
            "readonly": True,
        }
        for name in ("hde.body_graphs_current", "public.hde_body_graphs_current")
    )
    grants = tuple(
        {
            "grantees": ["postgres"],
            "object": item["name"],
            "privileges": list(EXPECTED_PRIVILEGES),
        }
        for item in objects
    )
    return (
        set(value)
        == {
            "bodygraph_unique_constraints",
            "boundary_views",
            "boundary_views_readonly",
            "captured_at_utc",
            "database_schema",
            "default_privileges",
            "fingerprint_objects",
            "grants",
            "observation_mode",
            "partition_plan",
            "partition_plan_status",
            "schema",
            "search_path",
            "search_path_exact",
            "source_capture_root",
            "status",
        }
        and value.get("schema") == "hde_epic038.ops01.db_posture_summary.v3"
        and value.get("database_schema") == "hde"
        and value.get("observation_mode") == "read_only"
        and value.get("search_path") == "hde, public"
        and value.get("search_path_exact") is True
        and value.get("boundary_views_readonly") is True
        and value.get("default_privileges") == "none_observed"
        and value.get("partition_plan_status") == "PASS"
        and value.get("status") == "PASS"
        and value.get("bodygraph_unique_constraints")
        == [
            {
                "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
                "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
            }
        ]
        and tuple(value.get("boundary_views", ())) == views
        and tuple(value.get("fingerprint_objects", ())) == objects
        and tuple(value.get("grants", ())) == grants
        and value.get("partition_plan")
        == [
            {"key": "(evaluated_at)", "strategy": "RANGE", "table": "hde.pair_evaluation"},
            {"key": "(created_at)", "strategy": "RANGE", "table": "hde.public_results"},
        ]
        and _path_is_beneath(value.get("source_capture_root"), staging_root)
    )


def _bridge_consistency_valid(
    value: Mapping[str, object],
    *,
    staging_root: str,
    candidate_root: Path,
    authorization: Mapping[str, object],
    provider_proof: Mapping[str, object],
) -> bool:
    if set(value) != {
        "bodygraph_comparator",
        "captured_at_utc",
        "command_exit_codes",
        "governed_checker",
        "predicates",
        "schema",
        "status",
    }:
        return False
    comparator = value.get("bodygraph_comparator")
    checker = value.get("governed_checker")
    if not _has_exact_keys(
        comparator,
        {
            "bridge_input",
            "canonical_sha256",
            "direct_input",
            "exit_code",
            "identity",
            "literal_invocation",
            "result",
        },
    ) or not _has_exact_keys(
        checker,
        {
            "exit_code",
            "inputs",
            "literal_invocation",
            "repo_identity",
            "repo_sha256",
            "result",
            "staged_executable",
            "staged_sha256",
        },
    ):
        return False
    comparator = _mapping(comparator)
    checker = _mapping(checker)
    pair_keys = {"path", "sha256"}
    comparator_inputs = (
        _mapping(comparator.get("direct_input")),
        _mapping(comparator.get("bridge_input")),
    )
    checker_inputs = _mapping(checker.get("inputs"))
    try:
        provider_proof_input = {
            "path": (
                Path(staging_root) / "candidate" / "provider_parity.proof.json"
            ).as_posix(),
            "sha256": _sha(
                (candidate_root / "provider_parity.proof.json").read_bytes()
            ),
        }
        env_presence_input = {
            "path": (
                Path(staging_root) / "candidate" / "env_presence.json"
            ).as_posix(),
            "sha256": _sha((candidate_root / "env_presence.json").read_bytes()),
        }
        source_root = _mapping(authorization.get("source")).get("root")
        if not isinstance(source_root, str):
            return False
        staged_checker = (
            Path(source_root) / "ci" / "checks" / "check_bridge_consistency.py"
        ).as_posix()
        staged_checker_path = Path(staged_checker)
        if staged_checker_path.is_symlink():
            return False
        checker_digest_path = staged_checker_path
        if not checker_digest_path.exists():
            checker_digest_path = ROOT / "ci" / "checks" / "check_bridge_consistency.py"
        if (
            checker_digest_path.is_symlink()
            or not checker_digest_path.is_file()
        ):
            return False
        checker_digest = _sha(checker_digest_path.read_bytes())
        bodygraph_row = next(
            _mapping(row)
            for row in provider_proof.get("capabilities", ())
            if isinstance(row, Mapping) and row.get("name") == "bodygraph_payload_row"
        )
        direct_bodygraph_sha = _mapping(bodygraph_row.get("direct")).get(
            "canonical_sha256"
        )
        bridge_bodygraph_sha = _mapping(bodygraph_row.get("bridge")).get(
            "canonical_sha256"
        )
    except (OSError, StopIteration, TypeError):
        return False
    all_paths = [item.get("path") for item in comparator_inputs]
    for name in ("adapter_selection", "env_connectivity", "provider_parity"):
        item = _mapping(checker_inputs.get(name))
        if not _has_exact_keys(item, pair_keys):
            return False
        all_paths.append(item.get("path"))
    expected_exit_names = {
        "bridge_bodygraph_read",
        "canonical_comparison",
        "db_posture_capture",
        "direct_bodygraph_read",
        "governed_checker",
    }
    expected_predicates = {
        "all_actions_closed_rails",
        "bodygraph_bridge_available",
        "bodygraph_direct_available",
        "bodygraph_provider_selection_provenance",
        "bodygraph_row_match",
        "bodygraph_selector_approved",
        "four_row_corpus_exact",
        "provider_selection_consistent",
        "search_path_exact",
    }
    return (
        value.get("schema") == "hde_epic038.ops01.bridge_consistency.v3"
        and value.get("status") == "PASS"
        and all(_has_exact_keys(item, pair_keys) for item in comparator_inputs)
        and comparator_inputs
        == (provider_proof_input, provider_proof_input)
        and all(_path_is_beneath(path, staging_root) for path in all_paths)
        and _path_is_beneath(checker.get("staged_executable"), staging_root)
        and all(_is_sha256(item.get("sha256")) for item in comparator_inputs)
        and comparator.get("identity") == "presenter.json_canon_compare"
        and comparator.get("exit_code") == 0
        and comparator.get("result") == "FILE_EQ_CANON_BYTES_OK"
        and comparator.get("canonical_sha256")
        == direct_bodygraph_sha
        == bridge_bodygraph_sha
        and set(_mapping(value.get("command_exit_codes"))) == expected_exit_names
        and all(type(item) is int and item == 0 for item in _mapping(value.get("command_exit_codes")).values())
        and set(_mapping(value.get("predicates"))) == expected_predicates
        and all(item is True for item in _mapping(value.get("predicates")).values())
        and _has_exact_keys(checker_inputs, {"adapter_selection", "env_connectivity", "provider_parity"})
        and checker_inputs
        == {
            "adapter_selection": provider_proof_input,
            "env_connectivity": env_presence_input,
            "provider_parity": provider_proof_input,
        }
        and checker.get("repo_identity") == "ci/checks/check_bridge_consistency.py"
        and checker.get("staged_executable") == staged_checker
        and checker.get("repo_sha256")
        == checker.get("staged_sha256")
        == checker_digest
        and checker.get("exit_code") == 0
        and checker.get("result") == "PASS"
    )


def _nonclaims_valid(value: Mapping[str, object]) -> bool:
    return (
        set(value) == {"captured_at_utc", "nonclaims", "pf09_posture", "schema"}
        and value.get("schema") == "hde_epic038.ops01.nonclaims.v3"
        and value.get("nonclaims") == list(NONCLAIMS)
        and value.get("pf09_posture")
        == {
            "HDE-DIST001": "Partial",
            "HDE-DIST001.4": "Partial",
            "HDE-DIST001.9": "Partial",
            "status_change": "none",
        }
    )


def _commands_match_authorization(
    commands_bytes: bytes, authorization: Mapping[str, object]
) -> bool:
    try:
        if b"\r" in commands_bytes or not commands_bytes.endswith(b"\n"):
            return False
        lines = commands_bytes.decode("utf-8").splitlines()
        if len(lines) != 1:
            return False
        rendered = json.loads(lines[0], object_pairs_hook=_no_duplicate_object)
        prefix = _at(authorization, "discovery", "run_contract", "argv_prefix")
        boundary = _at(
            authorization,
            "discovery",
            "run_contract",
            "child_argv_start_index",
        )
        child = _at(authorization, "run", "child_argv")
        expected_child = [
            _at(authorization, "interpreter", "path"),
            "-I",
            "-B",
            _at(authorization, "runner", "path"),
            "--live-child",
        ]
        return (
            isinstance(rendered, list)
            and all(isinstance(token, str) for token in rendered)
            and isinstance(prefix, list)
            and all(isinstance(token, str) for token in prefix)
            and type(boundary) is int
            and boundary == len(prefix)
            and child == expected_child
            and rendered == prefix + child
            and commands_bytes == _canon(rendered)
        )
    except (UnicodeError, ValueError, TypeError):
        return False


def validate_ops01_v5_package(
    root: Path, *, expected: Ops01V5ExpectedIdentity
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    try:
        entries = tuple(root.iterdir())
        files = tuple(path.name for path in entries)
        all_entries_are_regular_files = all(
            not path.is_symlink() and stat.S_ISREG(path.lstat().st_mode)
            for path in entries
        )
    except OSError:
        files = ()
        all_entries_are_regular_files = False
    if (
        root.is_symlink()
        or set(files) != set(V5_PRIMARY_FILES)
        or len(files) != len(V5_PRIMARY_FILES)
        or not all_entries_are_regular_files
    ):
        errors.add("OPS01_V5_WRITE_SET_MISMATCH")
        return _result(errors)

    for name in V5_PRIMARY_FILES:
        path = root / name
        if name != "checksums.sha256" and path.exists():
            try:
                errors.update(validate_retained_text_safety(path, path.read_bytes()))
            except OSError:
                errors.add("OPS01_V5_WRITE_SET_MISMATCH")

    ledger_bytes = b""
    commands_bytes = b""
    try:
        ledger_bytes = (root / "checksums.sha256").read_bytes()
        ledger = ledger_bytes.decode("ascii").splitlines()
        expected_lines = [
            f"{_sha((root / name).read_bytes())}  {name}"
            for name in sorted(V5_PRIMARY_FILES)
            if name != "checksums.sha256"
        ]
        if ledger != expected_lines:
            errors.add("OPS01_V5_WRITE_SET_MISMATCH")
        commands_bytes = (root / "commands.txt").read_bytes()
    except (OSError, UnicodeError):
        errors.add("OPS01_V5_WRITE_SET_MISMATCH")

    try:
        proof_path = root / "provider_parity.proof.json"
        proof_bytes = proof_path.read_bytes()
        proof = _mapping(_read_json(proof_path))
        if _canon(proof) != proof_bytes:
            errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")
        if not _provider_proof_valid(
            proof, staging_root=expected.literal_staging_root
        ):
            errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")
    except Exception:
        errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")

    try:
        summary_path = root / "result_summary.json"
        summary_bytes = summary_path.read_bytes()
        summary = _mapping(_read_json(summary_path))
        if _canon(summary) != summary_bytes:
            errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        if (
            set(summary) != RESULT_SUMMARY_KEYS
            or "status" in summary
            or summary.get("schema") != "hde_epic038.ops01.result_summary.v4"
            or summary.get("full_ddl_semantic_parity_claimed") is not False
            or _mapping(summary.get("scope")).get("default_release_sanity_admission") != "v4"
            or _mapping(summary.get("scope")).get("pr_c_integration") is not False
            or _mapping(summary.get("observation")).get("full_ddl_semantic_parity_claimed") is not False
            or summary.get("nonclaims") != list(NONCLAIMS)
            or _mapping(summary.get("corpus")).get("four_row_corpus_exact") is not True
            or _mapping(summary.get("corpus")).get("selector") != SELECTOR
            or summary.get("selector") != SELECTOR
            or _mapping(summary.get("checksum_policy")).get("algorithm") != "sha256"
            or _mapping(summary.get("checksum_policy")).get("terminal_files_checked") != ["exit_code.txt", "stderr.log", "stdout.log"]
            or _mapping(summary.get("remediation")).get("default_admission_remains_v4") is not True
            or _mapping(summary.get("remediation")).get("pf09_status_change") != "none"
            or _mapping(summary.get("remediation")).get("pr_c_ready_claimed") is not False
        ):
            errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        if (root / "exit_code.txt").read_bytes() != b"0\n":
            errors.add("OPS01_V5_EXIT_CODE_INVALID")
        if (root / "stdout.log").read_bytes() != b"PASS\n":
            errors.add("OPS01_V5_STDOUT_INVALID")
        if (root / "stderr.log").read_bytes() != b"none\n":
            errors.add("OPS01_V5_STDERR_INVALID")
        counts = _mapping(summary.get("actual_call_counts"))
        if set(counts) != set(CALL_COUNT_FIELDS) or any(
            type(counts[field]) is not int or counts[field] < 0
            for field in counts
        ):
            errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        if any(counts.get(field) != value for field, value in FIXED_COUNTS.items()):
            errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        actual, identity_errors = _candidate_actual_identity(
            summary,
            ledger_bytes=ledger_bytes,
            commands_bytes=commands_bytes,
        )
        errors.update(identity_errors)
        errors.update(_candidate_expected_errors(actual, expected))
        authorization = _mapping(summary.get("authorization"))
        if not _commands_match_authorization(commands_bytes, authorization):
            errors.add("OPS01_V5_COMMANDS_INVALID")

        primary_validators = (
            (
                "env_presence.json",
                lambda value: _env_presence_valid(
                    value, authorization=authorization
                ),
                "OPS01_V5_ENV_PRESENCE_INVALID",
            ),
            (
                "db_posture_summary.json",
                lambda value: _db_posture_valid(
                    value, staging_root=expected.literal_staging_root
                ),
                "OPS01_V5_DB_POSTURE_INVALID",
            ),
            (
                "bridge_consistency.result.json",
                lambda value: _bridge_consistency_valid(
                    value,
                    staging_root=expected.literal_staging_root,
                    candidate_root=root,
                    authorization=authorization,
                    provider_proof=proof,
                ),
                "OPS01_V5_BRIDGE_CONSISTENCY_INVALID",
            ),
            (
                "nonclaims.json",
                _nonclaims_valid,
                "OPS01_V5_NONCLAIMS_INVALID",
            ),
        )
        for name, validator, code in primary_validators:
            path = root / name
            raw_bytes = path.read_bytes()
            value = _mapping(_read_json(path))
            if _canon(value) != raw_bytes or not validator(value):
                errors.add(code)
    except Exception:
        errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")

    return _result(errors)


def _preflight_actual_identity(obj: Mapping[str, object]) -> dict[str, object]:
    source_write = _mapping(obj.get("source_write_validation"))
    return {
        "source_commit": _at(obj, "source", "commit"),
        "source_manifest_sha256": _at(
            obj, "source", "source_manifest_sha256"
        ),
        "pre_staging_manifest_sha256": source_write.get(
            "pre_staging_manifest_sha256"
        ),
        "literal_staging_root": _at(obj, "run", "staging_root"),
        "runner_sha256": _at(obj, "components", "runner", "sha256"),
        "validator_sha256": _at(obj, "components", "validator", "sha256"),
        "projector_sha256": _at(obj, "components", "projector", "sha256"),
        "interpreter_sha256": _at(obj, "interpreter", "sha256"),
        "railway_executable_sha256": _at(
            obj, "railway_executable", "sha256"
        ),
        "preflight_identity_sha256": _self_hash(
            obj, "preflight_identity_sha256"
        ),
    }


def _manifest_delta(
    before: list[object], after: list[object]
) -> list[dict[str, object]]:
    before_rows = {
        _mapping(row).get("path"): _mapping(row)
        for row in before
        if isinstance(_mapping(row).get("path"), str)
    }
    after_rows = {
        _mapping(row).get("path"): _mapping(row)
        for row in after
        if isinstance(_mapping(row).get("path"), str)
    }
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


def _preflight_live_tree_errors(
    path: Path,
    obj: Mapping[str, object],
    expected: Ops01RPreflightExpectedIdentity,
) -> set[str]:
    errors: set[str] = set()
    run = _mapping(obj.get("run"))
    source_write = _mapping(obj.get("source_write_validation"))
    source_root_value = run.get("source_root")
    staging_root_value = run.get("staging_root")
    preflight_path_value = run.get("preflight_path")
    if not all(
        isinstance(value, str)
        for value in (source_root_value, staging_root_value, preflight_path_value)
    ):
        return {"PREFLIGHT_SOURCE_MANIFEST_MISMATCH", "PREFLIGHT_WRITE_SET_INVALID"}
    source_root = _lexical_absolute(Path(source_root_value))
    staging_root = _lexical_absolute(Path(staging_root_value))
    preflight_path = _lexical_absolute(Path(preflight_path_value))
    if preflight_path != _lexical_absolute(path):
        errors.add("PREFLIGHT_WRITE_SET_INVALID")
    try:
        source_manifest = _tree_manifest(
            source_root, schema="hde_epic038.source_tree_manifest.v1"
        )
        source_sha = _sha(_canon(source_manifest))
        if (
            source_sha != expected.source_manifest_sha256
            or source_sha != _at(obj, "source", "source_manifest_sha256")
            or source_sha != source_write.get("pre_source_manifest_sha256")
            or source_sha != source_write.get("post_source_manifest_sha256")
        ):
            errors.add("PREFLIGHT_SOURCE_MANIFEST_MISMATCH")

        retained_pre = source_write.get("pre_staging_manifest")
        if not isinstance(retained_pre, list):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
            retained_pre = []
        retained_pre_manifest = {
            "schema": "hde_epic038.non_source_staging_manifest.v1",
            "entries": retained_pre,
        }
        retained_pre_sha = _sha(_canon(retained_pre_manifest))
        if (
            retained_pre_sha != expected.pre_staging_manifest_sha256
            or retained_pre_sha != source_write.get("pre_staging_manifest_sha256")
        ):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")

        recursive_exclusions: tuple[Path, ...] = ()
        if staging_root in (source_root, *source_root.parents):
            recursive_exclusions = (source_root,)
        post_manifest = _tree_manifest(
            staging_root,
            schema="hde_epic038.non_source_staging_manifest.v1",
            excluded_paths=(preflight_path,),
            excluded_recursive_roots=recursive_exclusions,
        )
        post_sha = _sha(_canon(post_manifest))
        if post_sha != source_write.get("post_staging_manifest_sha256"):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
        delta = _manifest_delta(retained_pre, post_manifest["entries"])
        if delta != source_write.get("observed_staging_changes"):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
        control_relative = _lexical_absolute(Path(run.get("control_root", ""))).relative_to(
            staging_root
        ).as_posix()
        if any(
            change.get("path") != control_relative
            or not set(change.get("change_kinds", ())) <= {"ctime_ns", "mtime_ns"}
            for change in delta
        ):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
        working = _lexical_absolute(Path(str(run.get("working_directory", ""))))
        if not working.is_dir() or any(working.iterdir()):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
    except (OSError, TypeError, ValueError):
        errors.add("PREFLIGHT_WRITE_SET_INVALID")
    return errors


def validate_ops01r_preflight(
    path: Path, *, expected: Ops01RPreflightExpectedIdentity
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    try:
        data = path.read_bytes()
        obj = _mapping(_read_json(path))
        if _canon(obj) != data:
            errors.add("PREFLIGHT_BYTES_NONCANONICAL")
        if set(obj) != PREFLIGHT_TOP_LEVEL_KEYS:
            errors.add("PREFLIGHT_ROSTER_INVALID")
        if set(_mapping(obj.get("run"))) != PREFLIGHT_RUN_KEYS:
            errors.add("PREFLIGHT_ROSTER_INVALID")
        if set(_mapping(obj.get("source"))) != PREFLIGHT_SOURCE_KEYS:
            errors.add("PREFLIGHT_ROSTER_INVALID")
        if set(_mapping(obj.get("interpreter"))) != PREFLIGHT_INTERPRETER_KEYS:
            errors.add("PREFLIGHT_ROSTER_INVALID")
        if set(_mapping(obj.get("components"))) != {"projector", "runner", "validator"}:
            errors.add("PREFLIGHT_ROSTER_INVALID")
        if set(_mapping(obj.get("source_write_validation"))) != SOURCE_WRITE_KEYS:
            errors.add("PREFLIGHT_SOURCE_WRITE_ROSTER_INVALID")
        orchestration = _mapping(obj.get("orchestration"))
        if set(orchestration) != PREFLIGHT_ORCHESTRATION_KEYS:
            errors.add("PREFLIGHT_ORCHESTRATION_INVALID")
        if obj.get("schema") != "hde_epic038.ops01r.preflight.v1":
            errors.add("PREFLIGHT_SCHEMA_INVALID")
        if obj.get("status") != "PASS":
            errors.add("PREFLIGHT_STATUS_INVALID")
        actual_io = _mapping(obj.get("actual_external_io_counts"))
        if set(actual_io) != set(PREFLIGHT_ZERO_IO_FIELDS) or any(
            type(actual_io[field]) is not int or actual_io[field] != 0
            for field in actual_io
        ):
            errors.add("PREFLIGHT_ACTUAL_IO_NONZERO")
        if obj.get("nonclaims") != list(PREFLIGHT_NONCLAIMS):
            errors.add("PREFLIGHT_NONCLAIMS_INVALID")
        expected_counts = _mapping(obj.get("expected_call_counts"))
        runs = orchestration.get("runs")
        derived_counts = _mapping(orchestration.get("derived_call_counts"))
        run_counts = []
        run_labels = []
        run_rows_valid = False
        if isinstance(runs, list) and len(runs) == 2:
            run_rows = [_mapping(row) for row in runs]
            run_rows_valid = all(set(row) == {"run_label", "call_counts"} for row in run_rows)
            run_labels = [row.get("run_label") for row in run_rows]
            run_counts = [row.get("call_counts") for row in run_rows]
        if (
            orchestration.get("schema")
            != "hde_epic038.ops01r.preflight.fake_boundary_two_run.v1"
            or orchestration.get("deterministic") is not True
            or len(run_counts) != 2
            or not run_rows_valid
            or run_labels != ["A", "B"]
            or any(_mapping(counts) != expected_counts for counts in run_counts)
            or derived_counts != expected_counts
            or orchestration.get("identity_sha256")
            != _sha(_canon([expected_counts, expected_counts]))
        ):
            errors.add("PREFLIGHT_ORCHESTRATION_INVALID")
        if set(expected_counts) != set(CALL_COUNT_FIELDS) or any(
            type(expected_counts[field]) is not int or expected_counts[field] < 0
            for field in expected_counts
        ) or any(
            expected_counts.get(field) != value
            for field, value in FIXED_COUNTS.items()
        ):
            errors.add("PREFLIGHT_EXPECTED_COUNTS_INVALID")
        actual = _preflight_actual_identity(obj)
        if obj.get("preflight_identity_sha256") != actual["preflight_identity_sha256"]:
            errors.add("PREFLIGHT_IDENTITY_MISMATCH")
        interpreter = _mapping(obj.get("interpreter"))
        source_write = _mapping(obj.get("source_write_validation"))
        producer_argv = interpreter.get("preflight_argv")
        if (
            not isinstance(producer_argv, list)
            or producer_argv != source_write.get("python_argv")
            or len(producer_argv) < 4
            or producer_argv[1:3] != ["-I", "-B"]
            or producer_argv[3] != _at(obj, "components", "runner", "lexical_path")
            or interpreter.get("python_environment_names") != []
            or source_write.get("python_environment_names") != []
            or interpreter.get("bytecode_flag") != "-B"
            or interpreter.get("isolated_flag") != "-I"
        ):
            errors.add("PREFLIGHT_ARGV_ENV_INVALID")
        run = _mapping(obj.get("run"))
        preflight_path_value = run.get("preflight_path")
        control_root_value = run.get("control_root")
        source_root_value = run.get("source_root")
        staging_root_value = run.get("staging_root")
        try:
            staging_root = _lexical_absolute(Path(str(staging_root_value)))
            control_root = _lexical_absolute(Path(str(control_root_value)))
            source_root = _lexical_absolute(Path(str(source_root_value)))
            preflight_path = _lexical_absolute(Path(str(preflight_path_value)))
            control_relative = control_root.relative_to(staging_root).as_posix()
            if (
                source_write.get("authorized_exact_write_paths")
                != [preflight_path.as_posix()]
                or source_write.get("authorized_recursive_write_roots") != []
                or source_write.get("authorized_directory_metadata_paths")
                != [control_relative]
                or source_write.get("self_bound_excluded_paths")
                != [preflight_path.as_posix()]
                or source_write.get("self_bound_excluded_recursive_roots")
                != [source_root.as_posix()]
            ):
                errors.add("PREFLIGHT_WRITE_SET_INVALID")
        except (OSError, TypeError, ValueError):
            errors.add("PREFLIGHT_WRITE_SET_INVALID")
        if (
            _at(obj, "source_write_validation", "pre_source_manifest_sha256")
            != actual["source_manifest_sha256"]
            or _at(obj, "source_write_validation", "post_source_manifest_sha256")
            != actual["source_manifest_sha256"]
            or source_write.get("source_tree_unchanged") is not True
            or source_write.get("prohibited_cache_paths") != []
            or source_write.get("unauthorized_staging_paths") != []
            or source_write.get("staging_write_set_valid") is not True
        ):
            errors.add("PREFLIGHT_SOURCE_MANIFEST_MISMATCH")
        if not _all_expected_values_match(actual, expected):
            errors.add("PREFLIGHT_EXPECTED_IDENTITY_MISMATCH")
        errors.update(_preflight_live_tree_errors(path, obj, expected))
    except OSError:
        errors.add("PREFLIGHT_FILE_UNREADABLE")
    except (UnicodeError, ValueError, TypeError):
        errors.add("PREFLIGHT_JSON_INVALID")
    return _result(errors)


def _discovery_staging_root(obj: Mapping[str, object]) -> object:
    output_path = _at(obj, "output_contract", "path")
    if isinstance(output_path, str) and output_path:
        return Path(output_path).parent.parent.as_posix()
    return None


def _discovery_authorization_actual_identity(
    obj: Mapping[str, object]
) -> dict[str, object]:
    return {
        "discovery_authorization_sha256": _self_hash(
            obj, "discovery_authorization_sha256"
        ),
        "discovery_entry_point_sha256": _at(
            obj, "discovery_entry_point", "sha256"
        ),
        "literal_staging_root": _discovery_staging_root(obj),
        "pre_staging_manifest_sha256": _at(
            obj, "write_contract", "pre_staging_manifest_sha256"
        ),
        "preflight_identity_sha256": _at(
            obj, "preflight", "preflight_identity_sha256"
        ),
        "railway_executable_sha256": _at(obj, "railway_cli", "sha256"),
        "source_commit": _at(obj, "source", "commit"),
        "source_manifest_sha256": _at(
            obj, "source", "source_manifest_sha256"
        ),
    }


def _validate_discovery_authorization_object(
    obj: Mapping[str, object],
    raw_bytes: bytes,
    expected: Ops01RDiscoveryAuthorizationExpectedIdentity,
) -> set[str]:
    errors: set[str] = set()
    actual = _discovery_authorization_actual_identity(obj)
    if _canon(obj) != raw_bytes:
        errors.add("DISCOVERY_AUTH_BYTES_NONCANONICAL")
    if obj.get("schema") != "hde_epic038.ops01r.discovery_authorization.v1":
        errors.add("DISCOVERY_AUTH_SCHEMA_INVALID")
    output_path = _at(obj, "output_contract", "path")
    if (
        not isinstance(output_path, str)
        or not output_path
        or Path(output_path).name != "discovery.json"
        or Path(output_path).parent.name != "control"
    ):
        errors.add("DISCOVERY_AUTH_OUTPUT_CONTRACT_INVALID")
    if (
        obj.get("discovery_authorization_sha256")
        != actual["discovery_authorization_sha256"]
    ):
        errors.add("DISCOVERY_AUTH_IDENTITY_MISMATCH")
    if not _all_expected_values_match(actual, expected):
        errors.add("DISCOVERY_AUTH_EXPECTED_IDENTITY_MISMATCH")
    if (
        _at(obj, "preflight", "source_manifest_sha256")
        != actual["source_manifest_sha256"]
    ):
        errors.add("DISCOVERY_AUTH_SOURCE_MANIFEST_MISMATCH")
    if set(obj) != DISCOVERY_AUTH_KEYS:
        errors.add("DISCOVERY_AUTH_ROSTER_INVALID")
    policy = _mapping(obj.get("policy"))
    stages = policy.get("stages")
    python_execution = _mapping(policy.get("python_execution"))
    target_probe_argv = python_execution.get("target_probe_argv")
    if (
        set(policy) != {"python_execution", "stages"}
        or set(python_execution) != {"target_probe_argv"}
        or not isinstance(target_probe_argv, list)
        or not all(isinstance(token, str) for token in target_probe_argv)
        or len(target_probe_argv) < 4
        or target_probe_argv[1:3] != ["-I", "-B"]
    ):
        errors.add("DISCOVERY_AUTH_POLICY_INVALID")
    if not isinstance(stages, list) or [
        _mapping(stage).get("stage") for stage in stages
    ] != list(DISCOVERY_STAGES):
        errors.add("DISCOVERY_AUTH_POLICY_INVALID")
    else:
        for stage_row in stages:
            stage_map = _mapping(stage_row)
            if set(stage_map) != DISCOVERY_POLICY_STAGE_KEYS:
                errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                continue
            templates = stage_map.get("templates")
            if not isinstance(templates, list) or len(templates) != 1:
                errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                continue
            template = _mapping(templates[0])
            if set(template) != DISCOVERY_POLICY_TEMPLATE_KEYS:
                errors.add("DISCOVERY_AUTH_POLICY_INVALID")
            argv = template.get("argv")
            if not isinstance(argv, list) or not argv:
                errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                continue
            for descriptor in argv:
                descriptor_map = _mapping(descriptor)
                if descriptor_map.get("kind") not in DISCOVERY_POLICY_DESCRIPTOR_KINDS:
                    errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                if descriptor_map.get("kind") == "literal" and set(descriptor_map) != {"kind", "value"}:
                    errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                if descriptor_map.get("kind") == "prior_result" and set(descriptor_map) != {"field", "kind", "source_stage"}:
                    errors.add("DISCOVERY_AUTH_POLICY_INVALID")
                if descriptor_map.get("kind") == "python_child" and set(descriptor_map) != {"kind"}:
                    errors.add("DISCOVERY_AUTH_POLICY_INVALID")
    working = _mapping(obj.get("working_directory"))
    if (
        set(working) != {"linked_context_required", "must_be_empty", "path"}
        or working.get("linked_context_required") is not False
        or working.get("must_be_empty") is not True
        or not isinstance(working.get("path"), str)
    ):
        errors.add("DISCOVERY_AUTH_WORKING_DIRECTORY_INVALID")
    write_contract = _mapping(obj.get("write_contract"))
    required_write = {
        "authorized_directory_metadata_paths",
        "authorized_exact_write_paths",
        "authorized_recursive_write_roots",
        "pre_staging_manifest",
        "pre_staging_manifest_sha256",
        "self_bound_excluded_paths",
        "self_bound_excluded_recursive_roots",
        "source_root_writes_authorized",
    }
    if set(write_contract) != required_write or write_contract.get("source_root_writes_authorized") is not False:
        errors.add("DISCOVERY_AUTH_WRITE_CONTRACT_INVALID")
    if obj.get("nonclaims") != [
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
    ]:
        errors.add("DISCOVERY_AUTH_NONCLAIMS_INVALID")
    return errors


def validate_ops01r_discovery_authorization(
    path: Path, *, expected: Ops01RDiscoveryAuthorizationExpectedIdentity
) -> Ops01V5ValidationResult:
    try:
        raw_bytes = path.read_bytes()
        obj = _mapping(_read_json(path))
        return _result(
            _validate_discovery_authorization_object(obj, raw_bytes, expected)
        )
    except OSError:
        return _result({"DISCOVERY_AUTH_FILE_UNREADABLE"})
    except (UnicodeError, ValueError, TypeError):
        return _result({"DISCOVERY_AUTH_JSON_INVALID"})


def validate_ops01r_discovery_dispatch(
    authorization_path: Path,
    *,
    stage: str,
    prior_results: object,
    rendered_argv: tuple[str, ...],
) -> Ops01V5ValidationResult:
    prohibited = {
        "add",
        "connect",
        "delete",
        "deploy",
        "disconnect",
        "down",
        "link",
        "logs",
        "redeploy",
        "remove",
        "restart",
        "set",
        "shell",
        "ssh",
        "unlink",
        "unset",
        "up",
        "variables",
    }
    if any(token.lstrip("-").casefold() in prohibited for token in rendered_argv):
        return _result({"DISCOVERY_AUTH_PROHIBITED_COMMAND"})
    try:
        authorization = _mapping(_read_json(authorization_path))
        if tuple(rendered_argv) not in _authorized_stage_vectors(
            authorization, stage=stage, prior_results=prior_results
        ):
            code = (
                "DISCOVERY_AUTH_PYTHON_ARGV_MISMATCH"
                if stage == "target_identity_probe"
                else "DISCOVERY_AUTH_PROHIBITED_COMMAND"
            )
            return _result({code})
    except (OSError, UnicodeError, ValueError, TypeError):
        return _result({"DISCOVERY_AUTH_PROHIBITED_COMMAND"})
    return _result(set())


def _prior_stage_value(
    prior_results: object, source_stage: object, field: object
) -> object:
    if not isinstance(source_stage, str) or not isinstance(field, str):
        return None
    stage_value = _mapping(_mapping(prior_results).get(source_stage))
    return stage_value.get(field)


def _authorized_stage_vectors(
    authorization: Mapping[str, object], *, stage: str, prior_results: object
) -> set[tuple[str, ...]]:
    policy = _mapping(authorization.get("policy"))
    stages = policy.get("stages")
    if not isinstance(stages, list):
        return set()
    matches = [row for row in stages if _mapping(row).get("stage") == stage]
    if len(matches) != 1:
        return set()
    templates = _mapping(matches[0]).get("templates")
    executable = _at(authorization, "railway_cli", "lexical_path")
    target_probe_argv = _at(policy, "python_execution", "target_probe_argv")
    if (
        not isinstance(templates, list)
        or not isinstance(executable, str)
        or not executable
    ):
        return set()
    vectors: set[tuple[str, ...]] = set()
    for template in templates:
        descriptors = _mapping(template).get("argv")
        if not isinstance(descriptors, list) or not descriptors:
            continue
        tokens = [executable]
        valid = True
        for index, descriptor in enumerate(descriptors):
            descriptor = _mapping(descriptor)
            kind = descriptor.get("kind")
            if kind == "literal" and set(descriptor) == {"kind", "value"}:
                value = descriptor.get("value")
            elif kind == "prior_result" and set(descriptor) == {
                "field",
                "kind",
                "source_stage",
            }:
                value = _prior_stage_value(
                    prior_results,
                    descriptor.get("source_stage"),
                    descriptor.get("field"),
                )
            elif (
                kind == "python_child"
                and set(descriptor) == {"kind"}
                and stage == "target_identity_probe"
                and index == len(descriptors) - 1
                and isinstance(target_probe_argv, list)
                and all(isinstance(token, str) for token in target_probe_argv)
            ):
                tokens.extend(target_probe_argv)
                continue
            else:
                valid = False
                break
            if (
                not isinstance(value, str)
                or not value
                or any(ord(character) < 32 or ord(character) == 127 for character in value)
            ):
                valid = False
                break
            tokens.append(value)
        if valid:
            vectors.add(tuple(tokens))
    return vectors


def _discovery_prior_results(obj: Mapping[str, object]) -> dict[str, object]:
    target = _mapping(obj.get("target"))
    return {
        "project_inventory": {
            "project_id": target.get("project_id"),
            "project_name": target.get("project_name"),
        },
        "environment_inventory": {
            "environment_id": target.get("environment_id"),
            "environment_name": target.get("environment_name"),
        },
        "service_inventory": {
            "service_id": target.get("service_id"),
            "service_name": target.get("service_name"),
        },
    }


def _safe_identity_string(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and not any(ord(character) < 32 or ord(character) == 127 for character in value)
    )


def _absolute_string_list(value: object) -> list[str] | None:
    if not isinstance(value, list) or any(
        not _safe_identity_string(item) or not Path(item).is_absolute()
        for item in value
    ):
        return None
    return value


def _discovery_write_set_errors(
    path: Path,
    authorization_path: Path,
    authorization: Mapping[str, object],
    result: Mapping[str, object],
    expected: Ops01RDiscoveryAuthorizationExpectedIdentity,
) -> set[str]:
    errors: set[str] = set()
    source_write = _mapping(result.get("source_write_validation"))
    write_contract = _mapping(authorization.get("write_contract"))
    source_root_value = _at(authorization, "source", "root")
    output_path_value = _at(authorization, "output_contract", "path")
    if not isinstance(source_root_value, str) or not isinstance(output_path_value, str):
        return {"DISCOVERY_RESULT_WRITE_SET_MISMATCH"}
    source_root = _lexical_absolute(Path(source_root_value))
    staging_root = _lexical_absolute(Path(expected.literal_staging_root))
    output_path = _lexical_absolute(Path(output_path_value))
    excluded_paths = _absolute_string_list(
        write_contract.get("self_bound_excluded_paths")
    )
    excluded_roots = _absolute_string_list(
        write_contract.get("self_bound_excluded_recursive_roots")
    )
    exact_paths = _absolute_string_list(
        write_contract.get("authorized_exact_write_paths")
    )
    recursive_roots = _absolute_string_list(
        write_contract.get("authorized_recursive_write_roots")
    )
    metadata_paths = _absolute_string_list(
        write_contract.get("authorized_directory_metadata_paths")
    )
    if any(
        value is None
        for value in (
            excluded_paths,
            excluded_roots,
            exact_paths,
            recursive_roots,
            metadata_paths,
        )
    ):
        return {"DISCOVERY_RESULT_WRITE_SET_MISMATCH"}
    assert excluded_paths is not None
    assert excluded_roots is not None
    assert exact_paths is not None
    assert recursive_roots is not None
    assert metadata_paths is not None
    expected_exclusions = sorted(
        (authorization_path.as_posix(), output_path.as_posix()),
        key=lambda value: value.encode("utf-8"),
    )
    if (
        source_root != staging_root / "source"
        or output_path != staging_root / "control" / "discovery.json"
        or _lexical_absolute(path) != output_path
        or excluded_paths != expected_exclusions
        or excluded_roots
        or exact_paths != [output_path.as_posix()]
        or recursive_roots
        or metadata_paths != [(staging_root / "control").as_posix()]
        or write_contract.get("source_root_writes_authorized") is not False
    ):
        errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")

    retained_entries = write_contract.get("pre_staging_manifest")
    retained_hash = write_contract.get("pre_staging_manifest_sha256")
    retained = {
        "schema": "hde_epic038.non_source_staging_manifest.v1",
        "entries": retained_entries,
    }
    if (
        not isinstance(retained_entries, list)
        or not isinstance(retained_hash, str)
        or _sha(_canon(retained)) != retained_hash
        or retained_hash != expected.pre_staging_manifest_sha256
    ):
        errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
        retained_entries = []
    try:
        source_manifest = _tree_manifest(
            source_root, schema="hde_epic038.source_tree_manifest.v1"
        )
        source_sha = _sha(_canon(source_manifest))
        if (
            source_sha != expected.source_manifest_sha256
            or source_sha != _at(authorization, "source", "source_manifest_sha256")
            or source_sha != source_write.get("pre_source_manifest_sha256")
            or source_sha != source_write.get("post_source_manifest_sha256")
        ):
            errors.add("DISCOVERY_RESULT_SOURCE_MANIFEST_MISMATCH")
        post_manifest = _tree_manifest(
            staging_root,
            schema="hde_epic038.non_source_staging_manifest.v1",
            excluded_paths=tuple(Path(item) for item in excluded_paths),
            excluded_recursive_roots=(
                source_root,
                *(Path(item) for item in excluded_roots),
            ),
        )
        post_hash = _sha(_canon(post_manifest))
        delta = _manifest_delta(retained_entries, post_manifest["entries"])
        if (
            post_hash != source_write.get("post_staging_manifest_sha256")
            or delta != source_write.get("observed_staging_changes")
        ):
            errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
        exact = {_lexical_absolute(Path(item)) for item in exact_paths}
        recursive = tuple(_lexical_absolute(Path(item)) for item in recursive_roots)
        metadata = {_lexical_absolute(Path(item)) for item in metadata_paths}
        for change in delta:
            relative = change.get("path")
            kinds = change.get("change_kinds")
            if not isinstance(relative, str) or not isinstance(kinds, list):
                errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
                continue
            changed = staging_root if relative == "." else staging_root / relative
            changed = _lexical_absolute(changed)
            if not (
                changed in exact
                or any(root in (changed, *changed.parents) for root in recursive)
                or (changed in metadata and set(kinds) <= {"ctime_ns", "mtime_ns"})
            ):
                errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
        working_path = _at(authorization, "working_directory", "path")
        if (
            not isinstance(working_path, str)
            or not Path(working_path).is_dir()
            or any(Path(working_path).iterdir())
        ):
            errors.add("DISCOVERY_RESULT_LINKED_CONTEXT_DETECTED")
    except (OSError, TypeError, ValueError):
        errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
    return errors


def validate_ops01r_discovery_result(
    path: Path,
    *,
    authorization_path: Path,
    expected: Ops01RDiscoveryAuthorizationExpectedIdentity,
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    try:
        authorization_bytes = authorization_path.read_bytes()
        authorization = _mapping(_read_json(authorization_path))
        auth_errors = _validate_discovery_authorization_object(
            authorization, authorization_bytes, expected
        )
        if auth_errors:
            errors.add("DISCOVERY_RESULT_AUTHORIZATION_MISMATCH")

        raw_bytes = path.read_bytes()
        obj = _mapping(_read_json(path))
        output_path = _at(authorization, "output_contract", "path")
        if (
            not isinstance(output_path, str)
            or _lexical_absolute(path) != _lexical_absolute(Path(output_path))
            or path.is_symlink()
        ):
            errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
        if _canon(obj) != raw_bytes:
            errors.add("DISCOVERY_RESULT_BYTES_NONCANONICAL")
        if obj.get("schema") != "hde_epic038.ops01r.discovery.v1":
            errors.add("DISCOVERY_RESULT_SCHEMA_INVALID")
        if set(obj) != DISCOVERY_RESULT_KEYS:
            errors.add("DISCOVERY_RESULT_UNKNOWN_KEY")
        if obj.get("status") != "PASS":
            errors.add("DISCOVERY_RESULT_STAGE_FAILED")
        if obj.get("discovery_run_id") != authorization.get("run_id"):
            errors.add("DISCOVERY_RESULT_IDENTITY_MISMATCH")

        target = _mapping(obj.get("target"))
        target_fields = {
            "project_id",
            "project_name",
            "environment_id",
            "environment_name",
            "service_id",
            "service_name",
        }
        if set(target) != target_fields or any(
            not isinstance(target.get(field), str)
            or not target[field]
            or target[field] != target[field].strip()
            or any(
                ord(character) < 32 or ord(character) == 127
                for character in target[field]
            )
            for field in target_fields
        ):
            errors.add("DISCOVERY_RESULT_TARGET_AMBIGUOUS")
        requested_target = _mapping(authorization.get("requested_target"))
        if (
            target.get("project_name") != requested_target.get("project_name")
            or target.get("environment_name")
            != requested_target.get("environment_name")
            or target.get("service_name") != requested_target.get("service_name")
        ):
            errors.add("DISCOVERY_RESULT_TARGET_AMBIGUOUS")

        authorization_identity = _self_hash(
            authorization, "discovery_authorization_sha256"
        )
        if (
            obj.get("discovery_authorization_sha256")
            != authorization_identity
            or authorization.get("discovery_authorization_sha256")
            != authorization_identity
            or authorization_identity != expected.discovery_authorization_sha256
        ):
            errors.add("DISCOVERY_RESULT_AUTHORIZATION_MISMATCH")

        result_identity = _self_hash(obj, "discovery_identity_sha256")
        if obj.get("discovery_identity_sha256") != result_identity:
            errors.add("DISCOVERY_RESULT_IDENTITY_MISMATCH")

        command_manifest = obj.get("command_manifest")
        if (
            obj.get("command_manifest_sha256")
            != _sha(_canon(command_manifest))
        ):
            errors.add("DISCOVERY_RESULT_IDENTITY_MISMATCH")
        if not isinstance(command_manifest, list) or len(command_manifest) != len(
            DISCOVERY_STAGES
        ):
            errors.add("DISCOVERY_RESULT_ARGV_MISMATCH")
        else:
            railway_path = _at(authorization, "railway_cli", "lexical_path")
            for index, rendered in enumerate(command_manifest):
                if (
                    not isinstance(rendered, list)
                    or not rendered
                    or any(not isinstance(token, str) for token in rendered)
                    or not isinstance(railway_path, str)
                    or rendered[0] != railway_path
                    or not validate_ops01r_discovery_dispatch(
                        authorization_path,
                        stage=DISCOVERY_STAGES[index],
                        prior_results=_discovery_prior_results(obj),
                        rendered_argv=tuple(rendered),
                    ).valid
                ):
                    errors.add("DISCOVERY_RESULT_ARGV_MISMATCH")

        python_execution = _at(authorization, "policy", "python_execution")
        target_probe_argv = _at(
            authorization, "policy", "python_execution", "target_probe_argv"
        )
        run_contract = _mapping(obj.get("run_contract"))
        prefix = run_contract.get("argv_prefix")
        boundary = run_contract.get("child_argv_start_index")
        child_environment = run_contract.get("child_environment_contract")
        if (
            set(run_contract)
            != {
                "argv_prefix",
                "child_argv_start_index",
                "child_environment_contract",
                "linked_context_required",
                "python_execution",
                "target_dimensions",
            }
            or not isinstance(prefix, list)
            or not prefix
            or any(not _safe_identity_string(token) for token in prefix)
            or type(boundary) is not int
            or boundary != len(prefix)
            or not isinstance(target_probe_argv, list)
            or not isinstance(command_manifest, list)
            or not command_manifest
            or command_manifest[-1] != prefix + target_probe_argv
            or run_contract.get("python_execution") != python_execution
            or run_contract.get("linked_context_required") is not False
            or run_contract.get("target_dimensions")
            != ["project", "environment", "service"]
            or not isinstance(child_environment, list)
            or child_environment
            != sorted(
                child_environment,
                key=lambda row: str(_mapping(row).get("name", "")).encode("utf-8"),
            )
            or any(
                not _has_exact_keys(row, {"name", "source", "value_policy"})
                or not _safe_identity_string(_mapping(row).get("name"))
                or not _safe_identity_string(_mapping(row).get("source"))
                or not _safe_identity_string(_mapping(row).get("value_policy"))
                or str(_mapping(row).get("name", "")).casefold().startswith("python")
                for row in child_environment
            )
            or len({_mapping(row).get("name") for row in child_environment})
            != len(child_environment)
        ):
            errors.add("DISCOVERY_RESULT_IDENTITY_CONTRACT_INVALID")

        identity_contract = obj.get("identity_contract")
        expected_by_dimension = {
            "project": target.get("project_id"),
            "environment": target.get("environment_id"),
            "service": target.get("service_id"),
        }
        if (
            not isinstance(identity_contract, list)
            or identity_contract
            != sorted(
                identity_contract,
                key=lambda row: str(_mapping(row).get("field_name", "")).encode(
                    "utf-8"
                ),
            )
            or len(identity_contract) != 3
            or any(
                not _has_exact_keys(
                    row,
                    {
                        "field_name",
                        "target_dimension",
                        "value_kind",
                        "expected_value",
                    },
                )
                or _mapping(row).get("value_kind") != "target_id"
                or _mapping(row).get("target_dimension") not in expected_by_dimension
                or _mapping(row).get("expected_value")
                != expected_by_dimension.get(_mapping(row).get("target_dimension"))
                or not _safe_identity_string(_mapping(row).get("field_name"))
                for row in identity_contract
            )
            or {
                _mapping(row).get("target_dimension") for row in identity_contract
            }
            != set(expected_by_dimension)
            or {
                _mapping(row).get("field_name") for row in identity_contract
            }
            - {_mapping(row).get("name") for row in child_environment}
            or len(
                {_mapping(row).get("field_name") for row in identity_contract}
            )
            != len(identity_contract)
        ):
            errors.add("DISCOVERY_RESULT_IDENTITY_CONTRACT_INVALID")
        else:
            environment_by_name = {
                _mapping(row).get("name"): _mapping(row)
                for row in child_environment
            }
            expected_child_environment = [
                {"name": "ALLOW_DB_WRITE", "source": "runner", "value_policy": "exact:0"},
                {"name": "ALLOW_NETWORK", "source": "runner", "value_policy": "exact:0"},
                {"name": "APP_ENV", "source": "runner", "value_policy": "exact:dev"},
                {"name": "DATABASE_URL", "source": "railway_service", "value_policy": "presence_only"},
                {"name": "DB_BRIDGE_URL", "source": "railway_service", "value_policy": "presence_only"},
                {"name": "LANG", "source": "runner", "value_policy": "exact:C"},
                {"name": "LC_ALL", "source": "runner", "value_policy": "exact:C"},
                {"name": "SAFE_MODE", "source": "runner", "value_policy": "exact:1"},
                {"name": "TZ", "source": "runner", "value_policy": "exact:UTC"},
                *[
                    {
                        "name": _mapping(row).get("field_name"),
                        "source": "railway_target_identity",
                        "value_policy": f"exact:{_mapping(row).get('expected_value')}",
                    }
                    for row in identity_contract
                ],
            ]
            expected_child_environment.sort(
                key=lambda row: str(row["name"]).encode("utf-8")
            )
            if any(
                _mapping(environment_by_name.get(_mapping(row).get("field_name"))).get(
                    "source"
                )
                != "railway_target_identity"
                or _mapping(
                    environment_by_name.get(_mapping(row).get("field_name"))
                ).get("value_policy")
                != f"exact:{_mapping(row).get('expected_value')}"
                for row in identity_contract
            ) or any(
                _mapping(environment_by_name.get(name)).get("value_policy")
                != "presence_only"
                for name in ("DATABASE_URL", "DB_BRIDGE_URL")
            ) or child_environment != expected_child_environment:
                errors.add("DISCOVERY_RESULT_IDENTITY_CONTRACT_INVALID")

        counts = _mapping(obj.get("counts"))
        expected_count_keys = {
            "command_manifest_entries",
            "discovery_subprocesses",
            "provider_constructions",
            "db_connections",
            "direct_sql_statements",
            "bridge_http_requests",
            "vendor_requests",
        }
        if (
            set(counts) != expected_count_keys
            or counts.get("command_manifest_entries") != len(DISCOVERY_STAGES)
            or counts.get("discovery_subprocesses") != len(DISCOVERY_STAGES)
            or any(
                counts.get(field) != 0
                for field in expected_count_keys
                - {"command_manifest_entries", "discovery_subprocesses"}
            )
        ):
            errors.add("DISCOVERY_RESULT_COUNT_MISMATCH")
        if obj.get("nonclaims") != authorization.get("nonclaims"):
            errors.add("DISCOVERY_RESULT_NONCLAIMS_INVALID")

        railway = _mapping(obj.get("railway_cli"))
        if (
            set(railway) != {"path", "resolved_path", "sha256", "version"}
            or railway.get("path") != _at(authorization, "railway_cli", "lexical_path")
            or railway.get("resolved_path")
            != _at(authorization, "railway_cli", "resolved_path")
            or railway.get("sha256") != expected.railway_executable_sha256
            or not _safe_identity_string(railway.get("version"))
        ):
            errors.add("DISCOVERY_RESULT_CLI_IDENTITY_MISMATCH")
        source_write = _mapping(obj.get("source_write_validation"))
        if (
            set(source_write) != SOURCE_WRITE_KEYS
            or source_write.get("mode") != "discovery"
            or source_write.get("status") != "PASS"
            or source_write.get("source_tree_unchanged") is not True
            or source_write.get("staging_write_set_valid") is not True
            or source_write.get("bytecode_write_control") != "python_flag_-B"
            or source_write.get("manifest_algorithm")
            != "hde_epic038.source_tree_manifest.v1"
            or source_write.get("staging_manifest_algorithm")
            != "hde_epic038.non_source_staging_manifest.v1"
            or source_write.get("python_environment_names") != []
            or source_write.get("prohibited_cache_paths") != []
            or source_write.get("unauthorized_staging_paths") != []
            or source_write.get("python_argv") != target_probe_argv
            or source_write.get("authorized_exact_write_paths")
            != _at(authorization, "write_contract", "authorized_exact_write_paths")
            or source_write.get("authorized_recursive_write_roots")
            != _at(
                authorization, "write_contract", "authorized_recursive_write_roots"
            )
            or source_write.get("authorized_directory_metadata_paths")
            != _at(
                authorization,
                "write_contract",
                "authorized_directory_metadata_paths",
            )
            or source_write.get("self_bound_excluded_paths")
            != _at(authorization, "write_contract", "self_bound_excluded_paths")
            or source_write.get("self_bound_excluded_recursive_roots")
            != _at(
                authorization,
                "write_contract",
                "self_bound_excluded_recursive_roots",
            )
            or source_write.get("pre_source_manifest_sha256")
            != expected.source_manifest_sha256
            or source_write.get("post_source_manifest_sha256")
            != expected.source_manifest_sha256
        ):
            errors.add("DISCOVERY_RESULT_SOURCE_MANIFEST_MISMATCH")
        if (
            source_write.get("pre_staging_manifest_sha256")
            != expected.pre_staging_manifest_sha256
            or source_write.get("pre_staging_manifest")
            != _at(authorization, "write_contract", "pre_staging_manifest")
        ):
            errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
        errors.update(
            _discovery_write_set_errors(
                path, authorization_path, authorization, obj, expected
            )
        )
    except OSError:
        errors.add("DISCOVERY_RESULT_FILE_UNREADABLE")
    except (UnicodeError, ValueError, TypeError):
        errors.add("DISCOVERY_RESULT_JSON_INVALID")
    return _result(errors)


def validate_ops01r_live_authorization(
    path: Path, *, expected: Ops01RLiveAuthorizationExpectedIdentity
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    try:
        raw_bytes = path.read_bytes()
        obj = _mapping(_read_json(path))
        canonical_bytes = _canon(obj)
        authorization_sha256 = _sha(canonical_bytes)
        if raw_bytes != canonical_bytes:
            errors.add("OPS01_AUTH_BYTES_NONCANONICAL")
        if obj.get("schema") != "hde_epic038.ops01r.authorization.v1":
            errors.add("OPS01_AUTH_SCHEMA_INVALID")
        if set(obj) != {
            "schema",
            "source",
            "run",
            "runner",
            "validator",
            "projector",
            "interpreter",
            "preflight_identity_sha256",
            "discovery",
            "launch_limit",
            "expected_call_counts",
            "tracked_writes_authorized",
            "write_contract",
        }:
            errors.add("OPS01_AUTH_UNKNOWN_KEY")
        counts = _mapping(obj.get("expected_call_counts"))
        if (
            set(counts) != set(CALL_COUNT_FIELDS)
            or any(
                type(counts[field]) is not int or counts[field] < 0
                for field in counts
            )
            or any(
                counts.get(field) != value for field, value in FIXED_COUNTS.items()
            )
            or obj.get("launch_limit") != 1
            or obj.get("tracked_writes_authorized") is not False
        ):
            errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
        source = _mapping(obj.get("source"))
        run = _mapping(obj.get("run"))
        runner = _mapping(obj.get("runner"))
        validator = _mapping(obj.get("validator"))
        projector = _mapping(obj.get("projector"))
        interpreter = _mapping(obj.get("interpreter"))
        write_contract = _mapping(obj.get("write_contract"))
        staging_root_value = run.get("staging_root")
        if not isinstance(staging_root_value, str):
            errors.add("OPS01_AUTH_WRITE_SET_INVALID")
            staging_root = Path("/")
        else:
            staging_root = _lexical_absolute(Path(staging_root_value))
        source_root = staging_root / "source"
        control_root = staging_root / "control"
        candidate_root = staging_root / "candidate"
        authorization_path = control_root / "live_authorization.json"
        failure_path = control_root / "failure.json"
        marker_path = control_root / "live_authority_consumed.json"
        expected_validator_argv = [
            interpreter.get("path"),
            "-I",
            "-B",
            validator.get("path"),
            "--validate-live-authorization",
            "--expected-identity-stdin",
            authorization_path.as_posix(),
        ]
        expected_launcher_argv = [
            interpreter.get("path"),
            "-I",
            "-B",
            runner.get("path"),
            "--live-launch",
            authorization_path.as_posix(),
        ]
        expected_capture_argv = [
            interpreter.get("path"),
            "-I",
            "-B",
            validator.get("path"),
            "--validate-live-capture",
            "--expected-identity-stdin",
            staging_root.as_posix(),
        ]
        if (
            set(source)
            != {"repository", "commit", "root", "source_manifest_sha256", "state"}
            or source.get("repository") != "amthorn78/glow-hdengine-v2"
            or source.get("root") != source_root.as_posix()
            or source.get("state") != "DETACHED"
            or set(run)
            != {
                "authorization_path",
                "candidate_root",
                "child_argv",
                "launcher_argv",
                "live_authorization_validator_argv",
                "live_capture_validator_argv",
                "run_id",
                "staging_root",
            }
            or run.get("authorization_path") != authorization_path.as_posix()
            or run.get("candidate_root") != candidate_root.as_posix()
            or run.get("launcher_argv") != expected_launcher_argv
            or run.get("live_authorization_validator_argv")
            != expected_validator_argv
            or run.get("live_capture_validator_argv") != expected_capture_argv
            or not _safe_identity_string(run.get("run_id"))
            or set(runner) != {"path", "sha256"}
            or set(validator) != {"path", "sha256"}
            or set(projector) != {"path", "sha256"}
            or set(interpreter)
            != {
                "bytecode_flag",
                "bytecode_write_control",
                "isolated_flag",
                "path",
                "python_environment_names",
                "resolved_path",
                "sha256",
            }
            or interpreter.get("isolated_flag") != "-I"
            or interpreter.get("bytecode_flag") != "-B"
            or interpreter.get("bytecode_write_control") != "python_flag_-B"
            or interpreter.get("python_environment_names") != []
        ):
            errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
        expected_child_argv = [
            _at(obj, "interpreter", "path"),
            "-I",
            "-B",
            _at(obj, "runner", "path"),
            "--live-child",
        ]
        prefix = _at(obj, "discovery", "run_contract", "argv_prefix")
        boundary = _at(
            obj, "discovery", "run_contract", "child_argv_start_index"
        )
        child_argv = _at(obj, "run", "child_argv")
        if (
            any(not isinstance(token, str) or not token for token in expected_child_argv)
            or not isinstance(prefix, list)
            or not prefix
            or any(not isinstance(token, str) or not token for token in prefix)
            or type(boundary) is not int
            or boundary != len(prefix)
            or child_argv != expected_child_argv
        ):
            errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
        discovery = _mapping(obj.get("discovery"))
        if (
            discovery.get("schema") != "hde_epic038.ops01r.discovery.v1"
            or discovery.get("status") != "PASS"
            or discovery.get("discovery_identity_sha256")
            != _self_hash(discovery, "discovery_identity_sha256")
            or discovery.get("discovery_identity_sha256")
            != expected.discovery_identity_sha256
        ):
            errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
        expected_write_keys = {
            "consumed_marker_path",
            "failure_authorized_directory_metadata_paths",
            "failure_authorized_exact_paths",
            "failure_authorized_recursive_write_roots",
            "failure_summary_path",
            "pre_staging_manifest",
            "pre_staging_manifest_sha256",
            "self_bound_excluded_paths",
            "self_bound_excluded_recursive_roots",
            "source_root_writes_authorized",
            "success_authorized_directory_metadata_paths",
            "success_authorized_exact_paths",
            "success_authorized_recursive_write_roots",
        }
        retained_entries = write_contract.get("pre_staging_manifest")
        retained_hash = write_contract.get("pre_staging_manifest_sha256")
        retained = {
            "schema": "hde_epic038.non_source_staging_manifest.v1",
            "entries": retained_entries,
        }
        expected_excluded_paths = sorted(
            (authorization_path.as_posix(), failure_path.as_posix()),
            key=lambda value: value.encode("utf-8"),
        )
        if (
            set(write_contract) != expected_write_keys
            or write_contract.get("consumed_marker_path") != marker_path.as_posix()
            or write_contract.get("failure_summary_path") != failure_path.as_posix()
            or write_contract.get("success_authorized_exact_paths")
            != [marker_path.as_posix()]
            or write_contract.get("success_authorized_recursive_write_roots")
            != [candidate_root.as_posix()]
            or write_contract.get("failure_authorized_exact_paths")
            != [marker_path.as_posix(), failure_path.as_posix()]
            or write_contract.get("failure_authorized_recursive_write_roots")
            != [candidate_root.as_posix()]
            or write_contract.get("success_authorized_directory_metadata_paths")
            != [control_root.as_posix()]
            or write_contract.get("failure_authorized_directory_metadata_paths")
            != [control_root.as_posix()]
            or write_contract.get("self_bound_excluded_paths")
            != expected_excluded_paths
            or write_contract.get("self_bound_excluded_recursive_roots")
            != [candidate_root.as_posix()]
            or write_contract.get("source_root_writes_authorized") is not False
            or not isinstance(retained_entries, list)
            or not isinstance(retained_hash, str)
            or _sha(_canon(retained)) != retained_hash
            or retained_hash != expected.live_pre_staging_manifest_sha256
        ):
            errors.add("OPS01_AUTH_WRITE_SET_INVALID")
        try:
            if (
                _lexical_absolute(path) != authorization_path
                or path.is_symlink()
                or source_root.is_symlink()
                or candidate_root.is_symlink()
                or not source_root.is_dir()
                or not candidate_root.is_dir()
                or any(candidate_root.iterdir())
                or marker_path.exists()
                or failure_path.exists()
            ):
                raise ValueError("live authorization path state invalid")
            source_manifest = _tree_manifest(
                source_root, schema="hde_epic038.source_tree_manifest.v1"
            )
            if _sha(_canon(source_manifest)) != expected.source_manifest_sha256:
                errors.add("OPS01_AUTH_SOURCE_MANIFEST_MISMATCH")
            post_staging = _tree_manifest(
                staging_root,
                schema="hde_epic038.non_source_staging_manifest.v1",
                excluded_paths=tuple(
                    Path(value)
                    for value in write_contract.get("self_bound_excluded_paths", [])
                ),
                excluded_recursive_roots=(
                    source_root,
                    *(Path(value) for value in write_contract.get("self_bound_excluded_recursive_roots", [])),
                ),
            )
            if post_staging != retained:
                errors.add("OPS01_AUTH_WRITE_SET_INVALID")
            for component, component_expected in (
                (runner, expected.runner_sha256),
                (validator, expected.validator_sha256),
                (projector, expected.projector_sha256),
            ):
                component_path = Path(str(component.get("path", "")))
                if (
                    component_path.is_symlink()
                    or not component_path.is_file()
                    or source_root
                    not in (
                        component_path.resolve(),
                        *component_path.resolve().parents,
                    )
                    or _sha(component_path.read_bytes()) != component_expected
                    or component.get("sha256") != component_expected
                ):
                    errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
            interpreter_path = Path(str(interpreter.get("path", "")))
            if (
                not interpreter_path.resolve().is_file()
                or interpreter_path.resolve().as_posix()
                != interpreter.get("resolved_path")
                or _sha(interpreter_path.resolve().read_bytes())
                != expected.interpreter_sha256
                or interpreter.get("sha256") != expected.interpreter_sha256
            ):
                errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
        except (OSError, TypeError, ValueError):
            errors.add("OPS01_AUTH_WRITE_SET_INVALID")
        actual = {
            "authorization_sha256": authorization_sha256,
            "discovery_identity_sha256": _at(
                obj, "discovery", "discovery_identity_sha256"
            ),
            "interpreter_sha256": _at(obj, "interpreter", "sha256"),
            "live_pre_staging_manifest_sha256": _at(
                obj, "write_contract", "pre_staging_manifest_sha256"
            ),
            "literal_staging_root": _at(obj, "run", "staging_root"),
            "preflight_identity_sha256": obj.get("preflight_identity_sha256"),
            "projector_sha256": _at(obj, "projector", "sha256"),
            "railway_executable_sha256": _at(
                obj, "discovery", "railway_cli", "sha256"
            ),
            "runner_sha256": _at(obj, "runner", "sha256"),
            "source_commit": _at(obj, "source", "commit"),
            "source_manifest_sha256": _at(
                obj, "source", "source_manifest_sha256"
            ),
            "validator_sha256": _at(obj, "validator", "sha256"),
        }
        if not _all_expected_values_match(actual, expected):
            errors.add("OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH")
    except (OSError, UnicodeError, ValueError, TypeError):
        errors.add("OPS01_AUTH_EXPECTED_INPUT_INVALID")
    return _result(errors)


def validate_ops01r_live_capture(
    staging_root: Path, *, expected: Ops01V5ExpectedIdentity
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    staging_root = _lexical_absolute(staging_root)
    candidate_root = staging_root / "candidate"
    candidate_result = validate_ops01_v5_package(candidate_root, expected=expected)
    errors.update(candidate_result.errors)
    try:
        if (
            staging_root.is_symlink()
            or not stat.S_ISDIR(staging_root.lstat().st_mode)
            or staging_root.as_posix() != expected.literal_staging_root
        ):
            raise ValueError("live staging root mismatch")

        summary = _mapping(_read_json(candidate_root / "result_summary.json"))
        authorization = _mapping(summary.get("authorization"))
        source_write = _mapping(
            _at(summary, "execution", "source_write_validation")
        )
        write_contract = _mapping(authorization.get("write_contract"))
        if (
            set(source_write) != SOURCE_WRITE_KEYS
            or source_write.get("mode") != "live"
            or source_write.get("status") != "PASS"
            or source_write.get("source_tree_unchanged") is not True
            or source_write.get("staging_write_set_valid") is not True
            or source_write.get("prohibited_cache_paths") != []
            or source_write.get("unauthorized_staging_paths") != []
            or source_write.get("python_environment_names") != []
            or source_write.get("python_argv")
            != _at(authorization, "run", "child_argv")
            or source_write.get("authorized_exact_write_paths")
            != write_contract.get("success_authorized_exact_paths")
            or source_write.get("authorized_recursive_write_roots")
            != write_contract.get("success_authorized_recursive_write_roots")
            or source_write.get("authorized_directory_metadata_paths")
            != write_contract.get("success_authorized_directory_metadata_paths")
        ):
            raise ValueError("live source/write result invalid")

        source_root_value = _at(authorization, "source", "root")
        if not isinstance(source_root_value, str):
            raise ValueError("live source root missing")
        source_root = _lexical_absolute(Path(source_root_value))
        if (
            source_root != staging_root / "source"
            or source_root.is_symlink()
            or not stat.S_ISDIR(source_root.lstat().st_mode)
            or source_write.get("source_root") != source_root.as_posix()
            or _at(authorization, "run", "candidate_root")
            != candidate_root.as_posix()
        ):
            raise ValueError("live source or candidate root mismatch")

        source_manifest = _tree_manifest(
            source_root,
            schema="hde_epic038.source_tree_manifest.v1",
        )
        if _sha(_canon(source_manifest)) != expected.source_manifest_sha256:
            errors.add("OPS01_V5_SOURCE_MANIFEST_MISMATCH")

        pre_staging_entries = source_write.get("pre_staging_manifest")
        if not isinstance(pre_staging_entries, list):
            errors.add("OPS01_V5_LIVE_PRE_STAGING_MANIFEST_MISMATCH")
        else:
            pre_staging_manifest = {
                "schema": "hde_epic038.non_source_staging_manifest.v1",
                "entries": pre_staging_entries,
            }
            if (
                _sha(_canon(pre_staging_manifest))
                != expected.live_pre_staging_manifest_sha256
                or pre_staging_entries
                != write_contract.get("pre_staging_manifest")
                or source_write.get("pre_staging_manifest_sha256")
                != write_contract.get("pre_staging_manifest_sha256")
            ):
                errors.add("OPS01_V5_LIVE_PRE_STAGING_MANIFEST_MISMATCH")

        exact_values = source_write.get("self_bound_excluded_paths", [])
        recursive_values = source_write.get(
            "self_bound_excluded_recursive_roots", []
        )
        authorization_path = _at(authorization, "run", "authorization_path")
        failure_summary_path = write_contract.get("failure_summary_path")
        expected_exact_values = (
            sorted(
                (authorization_path, failure_summary_path),
                key=lambda value: value.encode("utf-8"),
            )
            if isinstance(authorization_path, str)
            and isinstance(failure_summary_path, str)
            else None
        )
        if not (
            isinstance(exact_values, list)
            and all(isinstance(value, str) for value in exact_values)
            and isinstance(recursive_values, list)
            and all(isinstance(value, str) for value in recursive_values)
            and exact_values
            == write_contract.get("self_bound_excluded_paths", [])
            and recursive_values
            == write_contract.get("self_bound_excluded_recursive_roots", [])
            and exact_values == expected_exact_values
            and recursive_values == [candidate_root.as_posix()]
        ):
            raise ValueError("live staging exclusions mismatch")

        authorization_file = _lexical_absolute(Path(authorization_path))
        failure_summary_file = _lexical_absolute(Path(failure_summary_path))
        marker_path = write_contract.get("consumed_marker_path")
        if not isinstance(marker_path, str):
            raise ValueError("live marker path missing")
        marker_file = _lexical_absolute(Path(marker_path))
        expected_marker = {
            "authorization_sha256": expected.authorization_sha256,
            "run_id": _at(authorization, "run", "run_id"),
            "schema": "hde_epic038.ops01r.live_authority_consumed.v1",
        }
        authorization_bytes = authorization_file.read_bytes()
        if (
            authorization_file.is_symlink()
            or not stat.S_ISREG(authorization_file.lstat().st_mode)
            or authorization_bytes != _canon(authorization)
            or _sha(authorization_bytes) != expected.authorization_sha256
            or failure_summary_file.exists()
            or marker_file != staging_root / "control" / "live_authority_consumed.json"
            or marker_file.is_symlink()
            or not stat.S_ISREG(marker_file.lstat().st_mode)
            or marker_file.read_bytes() != _canon(expected_marker)
            or write_contract.get("success_authorized_exact_paths")
            != [marker_file.as_posix()]
            or write_contract.get("success_authorized_recursive_write_roots")
            != [candidate_root.as_posix()]
            or write_contract.get("success_authorized_directory_metadata_paths")
            != [(staging_root / "control").as_posix()]
        ):
            raise ValueError("live excluded control file mismatch")

        post_staging_manifest = _tree_manifest(
            staging_root,
            schema="hde_epic038.non_source_staging_manifest.v1",
            excluded_paths=tuple(Path(value) for value in exact_values),
            excluded_recursive_roots=(
                source_root,
                *(Path(value) for value in recursive_values),
            ),
        )
        if (
            _sha(_canon(post_staging_manifest))
            != expected.live_post_staging_manifest_sha256
            or source_write.get("post_staging_manifest_sha256")
            != expected.live_post_staging_manifest_sha256
        ):
            errors.add("OPS01_V5_LIVE_POST_STAGING_MANIFEST_MISMATCH")
        delta = _manifest_delta(
            pre_staging_entries if isinstance(pre_staging_entries, list) else [],
            post_staging_manifest["entries"],
        )
        if delta != source_write.get("observed_staging_changes"):
            errors.add("OPS01_V5_LIVE_POST_STAGING_MANIFEST_MISMATCH")
        exact_paths = {
            _lexical_absolute(Path(value))
            for value in source_write.get("authorized_exact_write_paths", [])
        }
        recursive_roots = tuple(
            _lexical_absolute(Path(value))
            for value in source_write.get("authorized_recursive_write_roots", [])
        )
        metadata_paths = {
            _lexical_absolute(Path(value))
            for value in source_write.get("authorized_directory_metadata_paths", [])
        }
        for change in delta:
            relative = change.get("path")
            kinds = change.get("change_kinds")
            if not isinstance(relative, str) or not isinstance(kinds, list):
                raise ValueError("live delta invalid")
            changed = staging_root if relative == "." else staging_root / relative
            changed = _lexical_absolute(changed)
            if not (
                changed in exact_paths
                or any(root in (changed, *changed.parents) for root in recursive_roots)
                or (
                    changed in metadata_paths
                    and set(kinds) <= {"ctime_ns", "mtime_ns"}
                )
            ):
                errors.add("OPS01_V5_LIVE_POST_STAGING_MANIFEST_MISMATCH")
    except OSError:
        errors.add("OPS01_V5_WRITE_SET_MISMATCH")
    except (TypeError, ValueError):
        errors.add("OPS01_V5_LIVE_CAPTURE_IDENTITY_MISMATCH")
    return _result(errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    modes = (
        "validate-preflight",
        "validate-discovery-authorization",
        "validate-discovery-result",
        "validate-live-authorization",
        "validate-live-capture",
        "validate-candidate",
    )
    for mode in modes:
        parser.add_argument(f"--{mode}", action="store_true")
    parser.add_argument("--expected-identity-stdin", action="store_true")
    parser.add_argument("path", type=Path)
    parser.add_argument("authorization_path", type=Path, nargs="?")
    args = parser.parse_args(argv)

    if sum(getattr(args, mode.replace("-", "_")) for mode in modes) != 1:
        return 2
    if not args.expected_identity_stdin:
        if args.validate_preflight:
            raise SystemExit("PREFLIGHT_EXPECTED_INPUT_INVALID")
        if args.validate_discovery_authorization:
            raise SystemExit("DISCOVERY_AUTH_EXPECTED_INPUT_INVALID")
        if args.validate_discovery_result:
            raise SystemExit("DISCOVERY_RESULT_EXPECTED_INPUT_INVALID")
        if args.validate_live_authorization:
            raise SystemExit("OPS01_AUTH_EXPECTED_INPUT_INVALID")
        raise SystemExit("OPS01_V5_EXPECTED_INPUT_INVALID")
    if args.validate_discovery_result != (args.authorization_path is not None):
        return 2

    if args.validate_preflight:
        result = validate_ops01r_preflight(
            args.path,
            expected=_parse_expected_stdin(
                Ops01RPreflightExpectedIdentity,
                "PREFLIGHT_EXPECTED_INPUT_INVALID",
            ),
        )
    elif args.validate_discovery_authorization:
        result = validate_ops01r_discovery_authorization(
            args.path,
            expected=_parse_expected_stdin(
                Ops01RDiscoveryAuthorizationExpectedIdentity,
                "DISCOVERY_AUTH_EXPECTED_INPUT_INVALID",
            ),
        )
    elif args.validate_discovery_result:
        result = validate_ops01r_discovery_result(
            args.path,
            authorization_path=args.authorization_path,
            expected=_parse_expected_stdin(
                Ops01RDiscoveryAuthorizationExpectedIdentity,
                "DISCOVERY_RESULT_EXPECTED_INPUT_INVALID",
            ),
        )
    elif args.validate_live_authorization:
        result = validate_ops01r_live_authorization(
            args.path,
            expected=_parse_expected_stdin(
                Ops01RLiveAuthorizationExpectedIdentity,
                "OPS01_AUTH_EXPECTED_INPUT_INVALID",
            ),
        )
    elif args.validate_live_capture:
        result = validate_ops01r_live_capture(
            args.path,
            expected=_parse_expected_stdin(
                Ops01V5ExpectedIdentity,
                "OPS01_V5_EXPECTED_INPUT_INVALID",
            ),
        )
    else:
        result = validate_ops01_v5_package(
            args.path,
            expected=_parse_expected_stdin(
                Ops01V5ExpectedIdentity,
                "OPS01_V5_EXPECTED_INPUT_INVALID",
            ),
        )

    print("PASS" if result.valid else "\n".join(result.errors))
    return 0 if result.valid else 1


def _require_source_loading_process_contract() -> None:
    if (
        sys.flags.isolated != 1
        or sys.flags.dont_write_bytecode != 1
        or Path(sys.argv[0]).resolve() != Path(__file__).resolve()
    ):
        raise SystemExit("OPS01_V5_PYTHON_ARGV_MISMATCH")
    if any(name.casefold().startswith("python") for name in os.environ):
        raise SystemExit("OPS01_V5_PYTHON_ENVIRONMENT_INVALID")


if __name__ == "__main__":
    _require_source_loading_process_contract()
    raise SystemExit(main())
