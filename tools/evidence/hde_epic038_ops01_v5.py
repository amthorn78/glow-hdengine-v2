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

from engine.db.ddl_identity_projection import (
    DDL_IDENTITY_PROJECTION_FIELDS,
    DDL_IDENTITY_PROJECTION_SCHEMA,
    DDL_IDENTITY_UNEXAMINED_FIELDS,
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
    "direct_provider_selections": 1,
    "bridge_provider_selections": 1,
    "vendor_requests": 0,
    "retries": 0,
    "fallbacks": 0,
}
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


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


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
        proof = _mapping(_read_json(root / "provider_parity.proof.json"))
        if proof.get("schema") != "hde_epic038.ops01.provider_parity.v5":
            errors.add("OPS01_V5_SCHEMA_INVALID")
        if (
            proof.get("status") != "PASS"
            or proof.get("selected") != "psycopg"
            or proof.get("environment") != "dev"
            or proof.get("rails_open") is not False
            or proof.get("full_ddl_semantic_parity_claimed") is not False
        ):
            errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")
        comparison = _mapping(
            proof.get("comparison_contract")
            or proof.get("ddl_identity_projection_contract")
        )
        if comparison and (
            comparison.get("schema") != DDL_IDENTITY_PROJECTION_SCHEMA
            or tuple(comparison.get("included_fields", ()))
            != DDL_IDENTITY_PROJECTION_FIELDS
            or tuple(comparison.get("unexamined_fields", ()))
            != DDL_IDENTITY_UNEXAMINED_FIELDS
        ):
            errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")
    except Exception:
        errors.add("OPS01_V5_PROVIDER_PROOF_INVALID")

    try:
        summary = _mapping(_read_json(root / "result_summary.json"))
        if (
            summary.get("schema") != "hde_epic038.ops01.result_summary.v4"
            or summary.get("full_ddl_semantic_parity_claimed") is not False
        ):
            errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        counts = _mapping(summary.get("actual_call_counts"))
        for field, value in counts.items():
            if field in CALL_COUNT_FIELDS and (type(value) is not int or value < 0):
                errors.add("OPS01_V5_RESULT_SUMMARY_INVALID")
        actual, identity_errors = _candidate_actual_identity(
            summary,
            ledger_bytes=ledger_bytes,
            commands_bytes=commands_bytes,
        )
        errors.update(identity_errors)
        errors.update(_candidate_expected_errors(actual, expected))
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


def validate_ops01r_preflight(
    path: Path, *, expected: Ops01RPreflightExpectedIdentity
) -> Ops01V5ValidationResult:
    errors: set[str] = set()
    try:
        data = path.read_bytes()
        obj = _mapping(_read_json(path))
        if _canon(obj) != data:
            errors.add("PREFLIGHT_BYTES_NONCANONICAL")
        if obj.get("schema") != "hde_epic038.ops01r.preflight.v1":
            errors.add("PREFLIGHT_SCHEMA_INVALID")
        if obj.get("status") != "PASS":
            errors.add("PREFLIGHT_STATUS_INVALID")
        actual = _preflight_actual_identity(obj)
        if obj.get("preflight_identity_sha256") != actual["preflight_identity_sha256"]:
            errors.add("PREFLIGHT_IDENTITY_MISMATCH")
        if (
            _at(obj, "source_write_validation", "pre_source_manifest_sha256")
            != actual["source_manifest_sha256"]
            or _at(obj, "source_write_validation", "post_source_manifest_sha256")
            != actual["source_manifest_sha256"]
        ):
            errors.add("PREFLIGHT_SOURCE_MANIFEST_MISMATCH")
        if not _all_expected_values_match(actual, expected):
            errors.add("PREFLIGHT_EXPECTED_IDENTITY_MISMATCH")
    except OSError:
        errors.add("PREFLIGHT_FILE_UNREADABLE")
    except (UnicodeError, ValueError, TypeError):
        errors.add("PREFLIGHT_JSON_INVALID")
    return _result(errors)


def _discovery_staging_root(obj: Mapping[str, object]) -> object:
    output_path = _at(obj, "output_contract", "path")
    if isinstance(output_path, str) and output_path:
        return Path(output_path).parent.parent.as_posix()
    source_root = _at(obj, "source", "root")
    if isinstance(source_root, str) and source_root:
        return Path(source_root).parent.as_posix()
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
    del authorization_path, stage, prior_results
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
    return _result(set())


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
        if _canon(obj) != raw_bytes:
            errors.add("DISCOVERY_RESULT_BYTES_NONCANONICAL")
        if obj.get("schema") != "hde_epic038.ops01r.discovery.v1":
            errors.add("DISCOVERY_RESULT_SCHEMA_INVALID")
        if obj.get("status") != "PASS":
            errors.add("DISCOVERY_RESULT_STAGE_FAILED")

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

        if _at(obj, "railway_cli", "sha256") != expected.railway_executable_sha256:
            errors.add("DISCOVERY_RESULT_CLI_IDENTITY_MISMATCH")
        source_write = _mapping(obj.get("source_write_validation"))
        if (
            source_write.get("pre_source_manifest_sha256")
            != expected.source_manifest_sha256
            or source_write.get("post_source_manifest_sha256")
            != expected.source_manifest_sha256
        ):
            errors.add("DISCOVERY_RESULT_SOURCE_MANIFEST_MISMATCH")
        if (
            source_write.get("pre_staging_manifest_sha256")
            != expected.pre_staging_manifest_sha256
        ):
            errors.add("DISCOVERY_RESULT_WRITE_SET_MISMATCH")
    except OSError:
        errors.add("DISCOVERY_RESULT_FILE_UNREADABLE")
    except (UnicodeError, ValueError, TypeError):
        errors.add("DISCOVERY_RESULT_JSON_INVALID")
    return _result(errors)


def validate_ops01r_live_authorization(
    path: Path, *, expected: Ops01RLiveAuthorizationExpectedIdentity
) -> Ops01V5ValidationResult:
    try:
        obj = _mapping(_read_json(path))
        authorization_sha256 = _sha(_canon(obj))
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
            return _result({"OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH"})
        return _result(set())
    except Exception:
        return _result({"OPS01_AUTH_EXPECTED_INPUT_INVALID"})


def validate_ops01r_live_capture(
    staging_root: Path, *, expected: Ops01V5ExpectedIdentity
) -> Ops01V5ValidationResult:
    candidate_root = staging_root / "candidate"
    if not candidate_root.is_dir() and (staging_root / "result_summary.json").is_file():
        candidate_root = staging_root
    return validate_ops01_v5_package(candidate_root, expected=expected)


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


if __name__ == "__main__":
    raise SystemExit(main())
