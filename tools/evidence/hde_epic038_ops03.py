#!/usr/bin/env python3
"""Independent, read-only validator for the HDE-EPIC038 OPS-03 packet."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RUNNER = (ROOT / "scripts/ops/hde_epic038_ops03.py").resolve()
VALIDATOR = Path(__file__).resolve()
SCHEMA_ROOT = ROOT / "schemas"
RUN_ROOT = Path("/tmp/hde-epic038-ops03")

SCHEMA_RECEIPT = "hde_epic038.ops03.validation_receipt.v1"
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


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _read_json(path: Path) -> tuple[Any | None, bool]:
    value, canonical, _ = _read_json_with_raw(path)
    return value, canonical


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
        from jsonschema import Draft202012Validator, FormatChecker

        validator = Draft202012Validator(_schema(name), format_checker=FormatChecker())
        return next(validator.iter_errors(value), None) is None
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


def _git(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=False,
        capture_output=True,
        text=True,
        env={"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "GIT_OPTIONAL_LOCKS": "0"},
    )


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
    status = _git(("status", "--porcelain=v1", "--untracked-files=all"))
    if status.returncode or status.stdout:
        errors.add("source_tree_not_pristine")
    worktree = _git(("diff", "--quiet", "--no-ext-diff", "--"))
    index = _git(("diff", "--cached", "--quiet", "--no-ext-diff", "--"))
    if worktree.returncode or index.returncode:
        errors.add("source_manifest_mismatch")
    if any(ROOT.rglob("*.pyc")) or any(path.is_dir() for path in ROOT.rglob("__pycache__")):
        errors.add("bytecode_residue_present")
    ignored_native = _git(("ls-files", "--others", "--ignored", "--exclude-standard", "--", "*.so", "*.pyd"))
    if ignored_native.returncode or ignored_native.stdout:
        errors.add("ignored_native_module_present")
    return tuple(sorted(errors))


def _load_candidate_json(candidate: Path) -> tuple[dict[str, Any], bool]:
    values: dict[str, Any] = {}
    canonical = True
    for name in ("db_posture_summary.json", "env_presence.json", "nonclaims.json", "result_summary.json"):
        value, is_canonical = _read_json(candidate / name)
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
    candidate: Path,
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
            (candidate / "commands.txt").read_text(encoding="utf-8") == commands
            and (candidate / "stdout.log").read_text(encoding="utf-8") == "OPS03_CAPTURE_PASS\n"
            and (candidate / "stderr.log").read_bytes() == b""
            and (candidate / "exit_code.txt").read_bytes() == b"0\n"
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
            and observations["runtime_role_flags"] == {"rolsuper": False, "rolcreatedb": False, "rolcreaterole": False}
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


def _secret_scan_valid(candidate: Path, names: Sequence[str]) -> bool:
    for name in names:
        path = candidate / name
        try:
            payload = path.read_bytes()
        except OSError:
            return False
        from tools.evidence.retained_evidence_safety import validate_retained_text_safety

        if validate_retained_text_safety(path, payload):
            return False
    return True


def _checksums_valid(candidate: Path) -> bool:
    try:
        lines = (candidate / CHECKSUM_FILE).read_text(encoding="ascii").splitlines()
    except (OSError, UnicodeDecodeError):
        return False
    expected = [f"{sha256_path(candidate / name)}  {name}" for name in CHECKSUM_INPUTS]
    return lines == expected


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


def validate_packet(
    auth_path: Path,
    candidate: Path,
    *,
    final: bool,
    enforce_source: bool = True,
    now: dt.datetime | None = None,
    actual_argv: Sequence[str] | None = None,
    mode: str | None = None,
) -> dict[str, Any]:
    auth_value, auth_canonical, authorization_bytes = _read_json_with_raw(auth_path)
    authorization_sha256 = sha256_bytes(authorization_bytes)
    auth = dict(auth_value) if isinstance(auth_value, Mapping) else {}
    auth_errors = authorization_errors(auth, auth_path, now=now) if auth else ("authorization_invalid",)
    if not auth_errors:
        _, _, authorized_candidate, _ = derived_paths(str(auth["run_id"]))
        try:
            candidate_matches = candidate.resolve() == authorized_candidate.resolve()
        except OSError:
            candidate_matches = False
        if not candidate_matches:
            auth_errors = ("candidate_path_mismatch",)
    failure_state_present = False
    if not auth_errors:
        _, _, _authorized_candidate, failure = derived_paths(str(auth["run_id"]))
        failure_state_present = (failure / "failure_receipt.json").exists()
        if failure_state_present:
            auth_errors = ("failure_state_present",)
    if not auth_errors and not _invocation_valid(auth, actual_argv, mode):
        auth_errors = ("validator_invocation_mismatch",)
    source_errors = source_identity_errors(auth, enforce_repo=enforce_source) if not auth_errors else ("source_not_checked",)
    expected_names = FINAL_FILES if final else tuple(sorted(PRIMARY_FILES))
    try:
        entries = list(candidate.iterdir())
        actual_names = tuple(sorted(path.name for path in entries))
        entries_are_regular = all(path.is_file() and not path.is_symlink() for path in entries)
    except OSError:
        actual_names = ()
        entries_are_regular = False
    inventory_exact = actual_names == expected_names and entries_are_regular
    values, core_canonical = _load_candidate_json(candidate)
    schemas_valid = _core_schema_valid(values)
    content_valid, counts_valid = (
        _content_valid(auth, authorization_sha256, candidate, values)
        if not auth_errors
        else (False, False)
    )
    canonical_valid = auth_canonical and core_canonical
    secret_names = list(PRIMARY_FILES)
    if final:
        receipt_value, receipt_canonical = _read_json(candidate / RECEIPT_FILE)
        canonical_valid = canonical_valid and receipt_canonical
        schemas_valid = schemas_valid and receipt_value is not None and _schema_valid(receipt_value, JSON_SCHEMAS[RECEIPT_FILE])
        secret_names.append(RECEIPT_FILE)
    predicates = {
        "authorization_valid": not auth_errors and auth_canonical,
        "source_identity_valid": not source_errors,
        "schemas_valid": schemas_valid,
        "canonical_bytes_valid": canonical_valid,
        "inventory_valid": inventory_exact and content_valid,
        "counts_valid": counts_valid,
        "secret_scan_valid": _secret_scan_valid(candidate, secret_names),
        "nonclaims_valid": values.get("nonclaims.json") == {"schema": "hde_epic038.ops03.nonclaims.v1", "run_id": auth.get("run_id"), "nonclaims": list(NONCLAIMS)},
    }
    try:
        authorization_stable = auth_path.read_bytes() == authorization_bytes
    except OSError:
        authorization_stable = False
    predicates["authorization_valid"] = predicates["authorization_valid"] and authorization_stable
    receipt = _receipt(auth, authorization_sha256, predicates)
    if final:
        stored, _ = _read_json(candidate / RECEIPT_FILE)
        predicates["inventory_valid"] = predicates["inventory_valid"] and stored == receipt and _checksums_valid(candidate)
        receipt = _receipt(auth, authorization_sha256, predicates)
    return receipt


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
    receipt = validate_packet(
        args.authorization.resolve(),
        args.candidate.resolve(),
        final=args.validate,
        actual_argv=actual_argv,
        mode=mode_name,
    )
    if receipt["result"] != "PASS":
        return 1
    if args.emit_receipt:
        (args.candidate / RECEIPT_FILE).write_bytes(canonical_bytes(receipt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
