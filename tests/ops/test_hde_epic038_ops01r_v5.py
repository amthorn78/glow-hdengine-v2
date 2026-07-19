from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, replace
from pathlib import Path

import pytest

from engine.db.ddl_identity_projection import (
    DDL_IDENTITY_PROJECTION_FIELDS,
    DDL_IDENTITY_PROJECTION_SCHEMA,
    DDL_IDENTITY_UNEXAMINED_FIELDS,
)
from tools.evidence.hde_epic038_ops01_v5 import (
    Ops01RDiscoveryAuthorizationExpectedIdentity,
    Ops01RLiveAuthorizationExpectedIdentity,
    Ops01RPreflightExpectedIdentity,
    Ops01V5ExpectedIdentity,
    DISCOVERY_STAGES,
    PREFLIGHT_NONCLAIMS,
    PREFLIGHT_ZERO_IO_FIELDS,
    NONCLAIMS,
    RESULT_SUMMARY_KEYS,
    V5_PRIMARY_FILES,
    _manifest_delta,
    _tree_manifest,
    validate_ops01_v5_package,
    validate_ops01r_discovery_authorization,
    validate_ops01r_discovery_dispatch,
    validate_ops01r_discovery_result,
    validate_ops01r_live_capture,
    validate_ops01r_live_authorization,
    validate_ops01r_preflight,
)


def _canon(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("ascii")


def _sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _write_json(path: Path, value: object) -> None:
    path.write_bytes(_canon(value))


def _rewrite_candidate_ledger(root: Path) -> bytes:
    ledger = (
        "\n".join(
            f"{_sha((root / name).read_bytes())}  {name}"
            for name in sorted(V5_PRIMARY_FILES)
            if name != "checksums.sha256"
        )
        + "\n"
    ).encode("ascii")
    (root / "checksums.sha256").write_bytes(ledger)
    return ledger


def test_discovery_dispatch_rejects_mutating_tokens(tmp_path):
    result = validate_ops01r_discovery_dispatch(
        tmp_path / "authorization.json",
        stage="cli_version",
        prior_results={},
        rendered_argv=("railway", "deploy"),
    )
    assert not result.valid
    assert "DISCOVERY_AUTH_PROHIBITED_COMMAND" in result.errors


def test_expected_identity_requires_pipe(tmp_path):
    path = tmp_path / "preflight.json"
    path.write_text("{}\n")
    expected = Ops01RPreflightExpectedIdentity(*(["x"] * 10))
    data = _canon(asdict(expected))
    process = subprocess.run(
        [
            sys.executable,
            "tools/evidence/hde_epic038_ops01_v5.py",
            "--validate-preflight",
            "--expected-identity-stdin",
            str(path),
        ],
        input=data,
        capture_output=True,
    )
    assert process.returncode != 0


def test_validator_cli_imports_from_outside_the_repo(tmp_path):
    validator = Path("tools/evidence/hde_epic038_ops01_v5.py").resolve()
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }

    process = subprocess.run(
        [sys.executable, "-I", "-B", str(validator), "--help"],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
    )

    assert process.returncode == 0, process.stderr


def test_unauthorized_live_child_does_not_run_external_ops():
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }
    process = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "scripts/ops/hde_epic038_ops01r.py",
            "--live-child",
        ],
        env=environment,
        capture_output=True,
        text=True,
    )
    assert process.returncode != 0
    assert "OPS01R_LIVE_AUTH_INVALID" in process.stderr


@pytest.mark.parametrize(
    "script,mode,flags",
    [
        ("scripts/ops/hde_epic038_ops01r.py", "--target-identity-probe", []),
        ("scripts/ops/hde_epic038_ops01r.py", "--target-identity-probe", ["-I"]),
        ("scripts/ops/hde_epic038_ops01r.py", "--target-identity-probe", ["-B"]),
        ("tools/evidence/hde_epic038_ops01_v5.py", "--help", []),
        ("tools/evidence/hde_epic038_ops01_v5.py", "--help", ["-I"]),
        ("tools/evidence/hde_epic038_ops01_v5.py", "--help", ["-B"]),
    ],
)
def test_source_loading_entry_points_require_isolated_no_bytecode_python(
    script, mode, flags
):
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }

    process = subprocess.run(
        [sys.executable, *flags, script, mode],
        env=environment,
        capture_output=True,
        text=True,
    )

    assert process.returncode != 0
    assert "OPS01_V5_PYTHON_ARGV_MISMATCH" in process.stderr


def test_target_identity_probe_rejects_python_environment():
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }
    environment["PythonPath"] = "/tmp/unauthorized-python-path"

    process = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "scripts/ops/hde_epic038_ops01r.py",
            "--target-identity-probe",
        ],
        env=environment,
        capture_output=True,
        text=True,
    )

    assert process.returncode != 0
    assert "OPS01_V5_PYTHON_ENVIRONMENT_INVALID" in process.stderr


def test_target_identity_probe_emits_names_and_presence_only():
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }
    environment.update(
        {
            "DATABASE_URL": "postgresql://not-retained",
            "DB_BRIDGE_URL": "https://not-retained.invalid",
            "RAILWAY_ENVIRONMENT_ID": "env-id",
            "RAILWAY_PROJECT_ID": "project-id",
            "RAILWAY_SERVICE_ID": "service-id",
        }
    )

    process = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "scripts/ops/hde_epic038_ops01r.py",
            "--target-identity-probe",
        ],
        env=environment,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(process.stdout)

    assert payload["endpoint_presence"] == {
        "DATABASE_URL": True,
        "DB_BRIDGE_URL": True,
    }
    assert payload["identity_fields"] == [
        {"name": "RAILWAY_ENVIRONMENT_ID", "value": "env-id"},
        {"name": "RAILWAY_PROJECT_ID", "value": "project-id"},
        {"name": "RAILWAY_SERVICE_ID", "value": "service-id"},
    ]
    assert "not-retained" not in process.stdout


def _candidate(
    tmp_path: Path,
    *,
    counts: dict[str, int] | None = None,
    ddl_parity: str = "projection_match",
    include_capabilities: bool = True,
    include_projection_contract: bool = True,
    literal_staging_root: str | None = None,
) -> tuple[Path, Ops01V5ExpectedIdentity]:
    root = tmp_path / "candidate"
    root.mkdir(exist_ok=True)
    source_commit = "1" * 40
    source_manifest = "2" * 64
    pre_staging = "3" * 64
    post_staging = "4" * 64
    preflight_identity = "5" * 64
    runner_sha = "6" * 64
    validator_sha = "7" * 64
    projector_sha = "8" * 64
    staging_root = literal_staging_root or tmp_path.as_posix()
    if counts is None:
        counts = {
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
    source_root = f"{staging_root}/source"
    checker_path = Path(source_root) / "ci/checks/check_bridge_consistency.py"
    checker_path.parent.mkdir(parents=True, exist_ok=True)
    if not checker_path.exists():
        checker_path.write_text("fixture checker\n")
    checker_sha = _sha(checker_path.read_bytes())
    runner_path = f"{source_root}/scripts/ops/hde_epic038_ops01r.py"
    validator_path = f"{source_root}/tools/evidence/hde_epic038_ops01_v5.py"
    projector_path = f"{source_root}/engine/db/ddl_identity_projection.py"
    interpreter_path = "/usr/bin/python3"
    argv_prefix = ["railway", "run", "--service", "glow-hdengine-v2", "--"]
    child_argv = [
        interpreter_path,
        "-I",
        "-B",
        runner_path,
        "--live-child",
    ]
    discovery = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_authorization_sha256": "9" * 64,
        "run_contract": {
            "argv_prefix": argv_prefix,
            "child_argv_start_index": len(argv_prefix),
        },
    }
    discovery["discovery_identity_sha256"] = _sha(_canon(discovery))
    authorization = {
        "schema": "hde_epic038.ops01r.authorization.v1",
        "source": {
            "commit": source_commit,
            "root": source_root,
            "source_manifest_sha256": source_manifest,
        },
        "run": {
            "candidate_root": root.as_posix(),
            "child_argv": child_argv,
            "staging_root": staging_root,
        },
        "runner": {"path": runner_path, "sha256": runner_sha},
        "validator": {"path": validator_path, "sha256": validator_sha},
        "projector": {"path": projector_path, "sha256": projector_sha},
        "interpreter": {"path": interpreter_path},
        "preflight_identity_sha256": preflight_identity,
        "discovery": discovery,
        "expected_call_counts": counts,
        "write_contract": {
            "pre_staging_manifest_sha256": pre_staging,
            "success_authorized_directory_metadata_paths": [f"{staging_root}/control"],
            "success_authorized_exact_paths": [f"{staging_root}/control/live_authority_consumed.json"],
            "success_authorized_recursive_write_roots": [root.as_posix()],
            "self_bound_excluded_paths": [
                f"{staging_root}/control/failure.json",
                f"{staging_root}/control/live_authorization.json",
            ],
            "self_bound_excluded_recursive_roots": [root.as_posix()],
        },
    }
    commands = _canon(argv_prefix + child_argv)
    (root / "commands.txt").write_bytes(commands)
    (root / "stdout.log").write_text("PASS\n")
    (root / "stderr.log").write_text("none\n")
    (root / "exit_code.txt").write_text("0\n")
    captured_at = "2026-07-18T00:00:00Z"
    selector = {
        "alias": "epic011-s10-invariance-1",
        "identity_source": "docs/run/EPIC011_TEST_IDENTITIES.md",
        "non_pii": True,
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afab",
    }
    rails = {"ALLOW_DB_WRITE": "0", "ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
    _write_json(
        root / "env_presence.json",
        {
            "captured_at_utc": captured_at,
            "environment_presence": {
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
            },
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
                "head": source_commit,
                "pre_execution_worktree": "clean",
                "root": source_root,
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
        },
    )
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
    _write_json(
        root / "db_posture_summary.json",
        {
            "bodygraph_unique_constraints": [
                {
                    "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
                    "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
                }
            ],
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
                    "object": item["name"],
                    "privileges": privileges,
                }
                for item in objects
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
            "source_capture_root": f"{staging_root}/capture",
            "status": "PASS",
        },
    )
    canonical_sha = "a" * 64
    input_pair = lambda name: {
        "path": f"{staging_root}/{name}.json",
        "sha256": canonical_sha,
    }
    _write_json(
        root / "bridge_consistency.result.json",
        {
            "bodygraph_comparator": {
                "bridge_input": input_pair("bodygraph.bridge"),
                "canonical_sha256": canonical_sha,
                "direct_input": input_pair("bodygraph.direct"),
                "exit_code": 0,
                "identity": "presenter.json_canon_compare",
                "literal_invocation": "sanitized canonical comparison",
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
                    "adapter_selection": input_pair("adapter-selection"),
                    "env_connectivity": input_pair("env-connectivity"),
                    "provider_parity": input_pair("provider-parity"),
                },
                "literal_invocation": "sanitized governed checker",
                "repo_identity": "ci/checks/check_bridge_consistency.py",
                "repo_sha256": checker_sha,
                "result": "PASS",
                "staged_executable": f"{staging_root}/checker/check_bridge_consistency.py",
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
        },
    )
    _write_json(
        root / "nonclaims.json",
        {
            "captured_at_utc": captured_at,
            "nonclaims": [
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
            ],
            "pf09_posture": {
                "HDE-DIST001": "Partial",
                "HDE-DIST001.4": "Partial",
                "HDE-DIST001.9": "Partial",
                "status_change": "none",
            },
            "schema": "hde_epic038.ops01.nonclaims.v3",
        },
    )
    provider_proof: dict[str, object] = {
        "schema": "hde_epic038.ops01.provider_parity.v5",
        "status": "PASS",
        "selected": "psycopg",
        "environment": "dev",
        "rails_open": False,
        "full_ddl_semantic_parity_claimed": False,
        "active_parity_corpus": {
            "name": "hde_epic038_ops01_live_bodygraph_parity_v4",
            "ordered_rows": [
                "grants",
                "search_path",
                "select_one",
                "ddl_fingerprint",
                "bodygraph_payload_row",
            ],
            "selector": selector,
        },
        "attempts": [{"provider": "psycopg", "status": "ok"}],
        "captured_at_utc": captured_at,
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
        "rails_posture": {
            "ALLOW_DB_WRITE": "0",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "SAFE_MODE": "1",
            "all_actions": "closed",
        },
        "remediation_marker": "F-009_DDL_IDENTITY_PROJECTION_CONTRACT",
    }
    direct_ddl = [
        {
            "columns": [{"data_type": "uuid", "name": "user_id"}],
            "kind": "table",
            "name": "hde.body_graphs",
        },
        {"kind": "view", "name": "hde.body_graphs_current"},
    ]
    bridge_ddl = [
        {
            "columns": [{"name": "user_id", "type": "uuid"}],
            "kind": "table",
            "name": "hde.body_graphs",
        },
        {"kind": "view", "name": "hde.body_graphs_current"},
    ]
    ddl_row: dict[str, object] = {
        "name": "ddl_fingerprint",
        "direct": {"status": "ok", "value": direct_ddl},
        "bridge": {"status": "ok", "value": bridge_ddl},
        "parity": ddl_parity,
    }
    if include_projection_contract:
        ddl_row["comparison_contract"] = {
            "schema": DDL_IDENTITY_PROJECTION_SCHEMA,
            "mode": "shared_identity_projection",
            "included_fields": list(DDL_IDENTITY_PROJECTION_FIELDS),
            "unexamined_fields": list(DDL_IDENTITY_UNEXAMINED_FIELDS),
            "ordering": "objects_by_kind_name_columns_by_name_type",
        }
    if include_capabilities:
        def bodygraph_side(side: str) -> dict[str, object]:
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
                "canonical_sha256": canonical_sha,
                "provider": provider,
                "raw_bodygraph_payload_recorded": False,
                "selection_snapshot": {
                    "content": content,
                    "path": f"{staging_root}/{side}/adapter_selection.snapshot.json",
                    "sha256": _sha(_canon(content)),
                },
                "staged_output": f"{staging_root}/bodygraph.{side}.json",
                "status": "ok",
            }
        provider_proof["capabilities"] = [
            {
                "name": "grants",
                "direct": {"status": "ok", "value": ["grant"]},
                "bridge": {"status": "ok", "value": ["grant"]},
                "parity": "match",
            },
            {
                "name": "search_path",
                "direct": {"status": "ok", "value": "hde, public"},
                "bridge": {"status": "ok", "value": "hde, public"},
                "parity": "match",
            },
            {
                "name": "select_one",
                "direct": {"status": "ok", "value": 1},
                "bridge": {"status": "ok", "value": 1},
                "parity": "match",
            },
            ddl_row,
            {
                "name": "bodygraph_payload_row",
                "direct": bodygraph_side("direct"),
                "bridge": bodygraph_side("bridge"),
                "parity": "match",
                "comparison": "FILE_EQ_CANON_BYTES_OK",
                "payload_fetch_implementation": "engine.cli.main:_fetch_db_bodygraph",
                "read_surface": "hdctl showcompat --conjunction --source db",
                "selector": selector,
            },
        ]
    _write_json(root / "provider_parity.proof.json", provider_proof)
    provider_proof_input = {
        "path": f"{staging_root}/candidate/provider_parity.proof.json",
        "sha256": _sha((root / "provider_parity.proof.json").read_bytes()),
    }
    env_presence_input = {
        "path": f"{staging_root}/candidate/env_presence.json",
        "sha256": _sha((root / "env_presence.json").read_bytes()),
    }
    bridge_consistency_path = root / "bridge_consistency.result.json"
    bridge_consistency = json.loads(bridge_consistency_path.read_text())
    bridge_consistency["bodygraph_comparator"]["direct_input"] = dict(
        provider_proof_input
    )
    bridge_consistency["bodygraph_comparator"]["bridge_input"] = dict(
        provider_proof_input
    )
    bridge_consistency["governed_checker"]["inputs"] = {
        "adapter_selection": dict(provider_proof_input),
        "env_connectivity": dict(env_presence_input),
        "provider_parity": dict(provider_proof_input),
    }
    bridge_consistency["governed_checker"]["staged_executable"] = (
        f"{source_root}/ci/checks/check_bridge_consistency.py"
    )
    _write_json(bridge_consistency_path, bridge_consistency)
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
        "actual_call_counts": counts,
        "authorization": authorization,
        "authorization_sha256": _sha(_canon(authorization)),
        "bodygraph_selector": selector,
        "captured_at_utc": captured_at,
        "checksum_policy": {"algorithm": "sha256", "ledger_excludes_itself": True},
        "discovery_identity_sha256": discovery["discovery_identity_sha256"],
        "epic_closeout": "NOT_CLAIMED",
        "execution": {
            "candidate_validator_argv": [
                interpreter_path,
                "-I",
                "-B",
                validator_path,
                "--validate-candidate",
                "--expected-identity-stdin",
                root.as_posix(),
            ],
            "commands_sha256": _sha(commands),
            "launch_executions": 1,
            "source_checkout_state": "DETACHED",
            "source_write_validation": {
                "authorized_directory_metadata_paths": [f"{staging_root}/control"],
                "authorized_exact_write_paths": [f"{staging_root}/control/live_authority_consumed.json"],
                "authorized_recursive_write_roots": [root.as_posix()],
                "bytecode_write_control": "python_flag_-B",
                "manifest_algorithm": "hde_epic038.source_tree_manifest.v1",
                "mode": "live",
                "observed_staging_changes": [],
                "post_source_manifest_sha256": source_manifest,
                "post_staging_manifest_sha256": post_staging,
                "pre_source_manifest_sha256": source_manifest,
                "pre_staging_manifest": [],
                "pre_staging_manifest_sha256": pre_staging,
                "prohibited_cache_paths": [],
                "python_argv": child_argv,
                "python_environment_names": [],
                "self_bound_excluded_paths": authorization["write_contract"]["self_bound_excluded_paths"],
                "self_bound_excluded_recursive_roots": [root.as_posix()],
                "source_root": source_root,
                "source_tree_unchanged": True,
                "staging_manifest_algorithm": "hde_epic038.non_source_staging_manifest.v1",
                "staging_write_set_valid": True,
                "status": "PASS",
                "unauthorized_staging_paths": [],
            },
        },
        "expected_call_counts": counts,
        "full_ddl_semantic_parity_claimed": False,
        "literal_staging_root": staging_root,
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
        "preflight_identity_sha256": preflight_identity,
        "qa_status": "NOT_CLAIMED",
        "remediation_findings_resolved": [
            "F-004_LITERAL_COMMANDS",
            "F-005_RAW_STREAM_AND_CHECKER_BINDING",
            "F-006_BODYGRAPH_ROW_PARITY",
            "F-007_OPS01_SCOPE",
            "F-008_BODYGRAPH_PROVIDER_SELECTION_PROVENANCE",
            "F-009_DDL_IDENTITY_PROJECTION_CONTRACT",
        ],
        "runner_sha256": runner_sha,
        "repository": {
            "branch": "DETACHED",
            "head": source_commit,
            "post_execution_worktree": "clean",
            "pre_execution_worktree": "clean",
            "root": source_root,
        },
        "schema": "hde_epic038.ops01.result_summary.v4",
        "scope": "bounded_read_only_db_posture_and_direct_bridge_bodygraph_row_parity",
    }
    _write_json(root / "result_summary.json", summary)
    ledger = _rewrite_candidate_ledger(root)
    expected = Ops01V5ExpectedIdentity(
        authorization_sha256=summary["authorization_sha256"],
        candidate_ledger_sha256=_sha(ledger),
        commands_sha256=_sha(commands),
        discovery_identity_sha256=discovery["discovery_identity_sha256"],
        expected_call_counts_sha256=_sha(_canon(counts)),
        literal_staging_root=staging_root,
        live_post_staging_manifest_sha256=post_staging,
        live_pre_staging_manifest_sha256=pre_staging,
        preflight_identity_sha256=preflight_identity,
        projector_sha256=projector_sha,
        runner_sha256=runner_sha,
        source_commit=source_commit,
        source_manifest_sha256=source_manifest,
        validator_sha256=validator_sha,
    )
    return root, expected


def test_candidate_is_bound_to_all_externally_reviewed_identity_fields(tmp_path):
    root, expected = _candidate(tmp_path)
    assert validate_ops01_v5_package(root, expected=expected).valid
    for field in asdict(expected):
        wrong = replace(expected, **{field: "f" * 64})
        result = validate_ops01_v5_package(root, expected=wrong)
        assert not result.valid, field
        assert f"OPS01_V5_{field.upper()}_MISMATCH" in result.errors


def test_candidate_rejects_nested_non_file_entries(tmp_path):
    root, expected = _candidate(tmp_path)
    extra = root / "extra"
    extra.mkdir()
    (extra / "raw.json").write_text('{"raw_request_body":{"secret":"x"}}\n')

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_WRITE_SET_MISMATCH" in result.errors


def test_candidate_rejects_symlinked_primary_files(tmp_path):
    root, expected = _candidate(tmp_path)
    external = tmp_path / "external.log"
    external.write_text("PASS\n")
    (root / "stdout.log").unlink()
    (root / "stdout.log").symlink_to(external)

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_WRITE_SET_MISMATCH" in result.errors


def test_candidate_requires_exact_fixed_call_counts(tmp_path):
    missing_case = tmp_path / "missing-count"
    missing_case.mkdir()
    missing_counts = {
        "bodygraph_reads": 2,
        "bridge_http_requests": 6,
        "bridge_provider_selections": 1,
        "direct_connection_attempts": 8,
        "direct_provider_selections": 1,
        "direct_sql_statements": 13,
        "fallbacks": 0,
        "logical_observations": 10,
        "retries": 0,
    }
    root, expected = _candidate(missing_case, counts=missing_counts)
    result = validate_ops01_v5_package(root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_RESULT_SUMMARY_INVALID" in result.errors

    nonzero_case = tmp_path / "nonzero-fixed-count"
    nonzero_case.mkdir()
    nonzero_counts = dict(missing_counts, vendor_requests=0, retries=1)
    root, expected = _candidate(nonzero_case, counts=nonzero_counts)
    result = validate_ops01_v5_package(root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_RESULT_SUMMARY_INVALID" in result.errors


def test_candidate_requires_ddl_projection_contract(tmp_path):
    root, expected = _candidate(tmp_path, include_projection_contract=False)

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_PROVIDER_PROOF_INVALID" in result.errors


def test_candidate_requires_active_projection_match_row(tmp_path):
    missing_case = tmp_path / "missing-capabilities"
    missing_case.mkdir()
    root, expected = _candidate(missing_case, include_capabilities=False)
    result = validate_ops01_v5_package(root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_PROVIDER_PROOF_INVALID" in result.errors


def test_candidate_rejects_semantically_invalid_primary_proofs(tmp_path):
    cases = (
        ("env_presence.json", "OPS01_V5_ENV_PRESENCE_INVALID"),
        ("db_posture_summary.json", "OPS01_V5_DB_POSTURE_INVALID"),
        (
            "bridge_consistency.result.json",
            "OPS01_V5_BRIDGE_CONSISTENCY_INVALID",
        ),
        ("nonclaims.json", "OPS01_V5_NONCLAIMS_INVALID"),
    )
    for name, code in cases:
        case_root = tmp_path / name.replace(".", "-")
        case_root.mkdir()
        root, expected = _candidate(case_root)
        _write_json(root / name, {})
        ledger = _rewrite_candidate_ledger(root)
        expected = replace(expected, candidate_ledger_sha256=_sha(ledger))

        result = validate_ops01_v5_package(root, expected=expected)

        assert not result.valid
        assert code in result.errors


@pytest.mark.parametrize(
    "mutation",
    [
        "missing_input",
        "wrong_digest",
        "missing_checker",
        "wrong_checker_digest",
        "broken_checker_symlink",
    ],
)
def test_bridge_consistency_rejects_unretained_or_unbound_inputs(
    tmp_path, monkeypatch, mutation
):
    root, expected = _candidate(tmp_path)
    path = root / "bridge_consistency.result.json"
    value = json.loads(path.read_text())
    if mutation == "missing_input":
        value["bodygraph_comparator"]["direct_input"]["path"] = (
            f"{expected.literal_staging_root}/bodygraph.direct.compat.json"
        )
    elif mutation == "wrong_digest":
        value["governed_checker"]["inputs"]["env_connectivity"]["sha256"] = (
            "f" * 64
        )
    elif mutation == "missing_checker":
        value["governed_checker"]["staged_executable"] = (
            f"{expected.literal_staging_root}/candidate/check_bridge_consistency.py"
        )
    elif mutation == "wrong_checker_digest":
        value["governed_checker"]["repo_sha256"] = "f" * 64
        value["governed_checker"]["staged_sha256"] = "f" * 64
    else:
        import tools.evidence.hde_epic038_ops01_v5 as validator_module

        staged_checker = Path(value["governed_checker"]["staged_executable"])
        staged_checker.unlink()
        staged_checker.symlink_to(staged_checker.with_name("missing-checker.py"))
        fallback_root = tmp_path / "fallback-repo"
        fallback_checker = (
            fallback_root / "ci/checks/check_bridge_consistency.py"
        )
        fallback_checker.parent.mkdir(parents=True)
        fallback_checker.write_text("fallback checker\n")
        fallback_sha = _sha(fallback_checker.read_bytes())
        value["governed_checker"]["repo_sha256"] = fallback_sha
        value["governed_checker"]["staged_sha256"] = fallback_sha
        monkeypatch.setattr(validator_module, "ROOT", fallback_root)
    _write_json(path, value)
    ledger = _rewrite_candidate_ledger(root)
    expected = replace(expected, candidate_ledger_sha256=_sha(ledger))

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_BRIDGE_CONSISTENCY_INVALID" in result.errors


def test_candidate_requires_full_provider_proof_roster(tmp_path):
    root, expected = _candidate(tmp_path)
    proof_path = root / "provider_parity.proof.json"
    proof = json.loads(proof_path.read_text())
    del proof["remediation_marker"]
    _write_json(proof_path, proof)
    ledger = _rewrite_candidate_ledger(root)
    expected = replace(expected, candidate_ledger_sha256=_sha(ledger))

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_PROVIDER_PROOF_INVALID" in result.errors


def test_candidate_reconstructs_the_authorized_live_command(tmp_path):
    root, expected = _candidate(tmp_path)
    commands = _canon(["railway", "run", "--", "python", "--live-child"])
    (root / "commands.txt").write_bytes(commands)
    summary_path = root / "result_summary.json"
    summary = json.loads(summary_path.read_text())
    summary["execution"]["commands_sha256"] = _sha(commands)
    _write_json(summary_path, summary)
    ledger = _rewrite_candidate_ledger(root)
    expected = replace(
        expected,
        candidate_ledger_sha256=_sha(ledger),
        commands_sha256=_sha(commands),
    )

    result = validate_ops01_v5_package(root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_COMMANDS_INVALID" in result.errors

    legacy_case = tmp_path / "legacy-match"
    legacy_case.mkdir()
    root, expected = _candidate(legacy_case, ddl_parity="match")
    result = validate_ops01_v5_package(root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_PROVIDER_PROOF_INVALID" in result.errors


def _live_capture(
    tmp_path: Path,
) -> tuple[Path, Path, Ops01V5ExpectedIdentity]:
    staging_root = tmp_path / "run"
    source_root = staging_root / "source"
    source_root.mkdir(parents=True)
    (source_root / "tracked.py").write_text("VALUE = 1\n")
    candidate_root, expected = _candidate(
        staging_root, literal_staging_root=staging_root.as_posix()
    )
    control_root = staging_root / "control"
    control_root.mkdir()
    authorization_path = control_root / "live_authorization.json"
    authorization_path.touch()
    failure_summary_path = control_root / "failure.json"
    consumed_marker_path = control_root / "live_authority_consumed.json"
    summary_path = candidate_root / "result_summary.json"
    summary = json.loads(summary_path.read_text())
    authorization = summary["authorization"]
    source_write = summary["execution"]["source_write_validation"]

    source_manifest = _tree_manifest(
        source_root,
        schema="hde_epic038.source_tree_manifest.v1",
    )
    source_manifest_sha256 = _sha(_canon(source_manifest))
    staging_manifest = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(authorization_path, failure_summary_path),
        excluded_recursive_roots=(source_root, candidate_root),
    )
    staging_manifest_sha256 = _sha(_canon(staging_manifest))

    authorization["source"]["root"] = source_root.as_posix()
    authorization["source"]["source_manifest_sha256"] = source_manifest_sha256
    authorization["run"] = {
        "authorization_path": authorization_path.as_posix(),
        "candidate_root": candidate_root.as_posix(),
        "child_argv": authorization["run"]["child_argv"],
        "run_id": "fixture-live-run",
        "staging_root": staging_root.as_posix(),
    }
    excluded_paths = sorted(
        (authorization_path.as_posix(), failure_summary_path.as_posix()),
        key=lambda value: value.encode("utf-8"),
    )
    recursive_roots = [candidate_root.as_posix()]
    metadata_paths = [control_root.as_posix()]
    authorization["write_contract"] = {
        "consumed_marker_path": consumed_marker_path.as_posix(),
        "failure_authorized_directory_metadata_paths": metadata_paths,
        "failure_authorized_exact_paths": [
            consumed_marker_path.as_posix(),
            failure_summary_path.as_posix(),
        ],
        "failure_authorized_recursive_write_roots": recursive_roots,
        "failure_summary_path": failure_summary_path.as_posix(),
        "pre_staging_manifest": staging_manifest["entries"],
        "pre_staging_manifest_sha256": staging_manifest_sha256,
        "self_bound_excluded_paths": excluded_paths,
        "self_bound_excluded_recursive_roots": recursive_roots,
        "source_root_writes_authorized": False,
        "success_authorized_directory_metadata_paths": metadata_paths,
        "success_authorized_exact_paths": [consumed_marker_path.as_posix()],
        "success_authorized_recursive_write_roots": recursive_roots,
    }
    summary["authorization_sha256"] = _sha(_canon(authorization))
    summary["literal_staging_root"] = staging_root.as_posix()
    _write_json(authorization_path, authorization)
    _write_json(
        consumed_marker_path,
        {
            "authorization_sha256": summary["authorization_sha256"],
            "run_id": authorization["run"]["run_id"],
            "schema": "hde_epic038.ops01r.live_authority_consumed.v1",
        },
    )
    post_staging_manifest = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(authorization_path, failure_summary_path),
        excluded_recursive_roots=(source_root, candidate_root),
    )
    post_staging_manifest_sha256 = _sha(_canon(post_staging_manifest))
    source_write.clear()
    source_write.update(
        {
            "authorized_directory_metadata_paths": metadata_paths,
            "authorized_exact_write_paths": [consumed_marker_path.as_posix()],
            "authorized_recursive_write_roots": recursive_roots,
            "bytecode_write_control": "python_flag_-B",
            "manifest_algorithm": "hde_epic038.source_tree_manifest.v1",
            "mode": "live",
            "observed_staging_changes": _manifest_delta(
                staging_manifest["entries"], post_staging_manifest["entries"]
            ),
            "post_source_manifest_sha256": source_manifest_sha256,
            "post_staging_manifest_sha256": post_staging_manifest_sha256,
            "pre_source_manifest_sha256": source_manifest_sha256,
            "pre_staging_manifest": staging_manifest["entries"],
            "pre_staging_manifest_sha256": staging_manifest_sha256,
            "prohibited_cache_paths": [],
            "python_argv": authorization["run"]["child_argv"],
            "python_environment_names": [],
            "self_bound_excluded_paths": excluded_paths,
            "self_bound_excluded_recursive_roots": recursive_roots,
            "source_root": source_root.as_posix(),
            "source_tree_unchanged": True,
            "staging_manifest_algorithm": "hde_epic038.non_source_staging_manifest.v1",
            "staging_write_set_valid": True,
            "status": "PASS",
            "unauthorized_staging_paths": [],
        }
    )
    _write_json(summary_path, summary)
    ledger = _rewrite_candidate_ledger(candidate_root)
    expected = replace(
        expected,
        authorization_sha256=summary["authorization_sha256"],
        candidate_ledger_sha256=_sha(ledger),
        literal_staging_root=staging_root.as_posix(),
        live_post_staging_manifest_sha256=post_staging_manifest_sha256,
        live_pre_staging_manifest_sha256=staging_manifest_sha256,
        source_manifest_sha256=source_manifest_sha256,
    )
    return staging_root, source_root, expected


def test_live_capture_recomputes_source_and_non_candidate_staging(tmp_path):
    staging_root, source_root, expected = _live_capture(tmp_path)
    assert validate_ops01r_live_capture(staging_root, expected=expected).valid

    (staging_root / "unauthorized.txt").write_text("not authorized\n")
    result = validate_ops01r_live_capture(staging_root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_LIVE_POST_STAGING_MANIFEST_MISMATCH" in result.errors

    (source_root / "tracked.py").write_text("VALUE = 2\n")
    result = validate_ops01r_live_capture(staging_root, expected=expected)
    assert not result.valid
    assert "OPS01_V5_SOURCE_MANIFEST_MISMATCH" in result.errors


def test_live_capture_rejects_result_claimed_write_set_expansion(tmp_path):
    staging_root, source_root, expected = _live_capture(tmp_path)
    candidate_root = staging_root / "candidate"
    summary_path = candidate_root / "result_summary.json"
    summary = json.loads(summary_path.read_text())
    source_write = summary["execution"]["source_write_validation"]
    unauthorized = staging_root / "unauthorized.txt"
    unauthorized.write_text("not authorized\n")
    post_staging = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=tuple(
            Path(value) for value in source_write["self_bound_excluded_paths"]
        ),
        excluded_recursive_roots=(source_root, candidate_root),
    )
    post_staging_sha = _sha(_canon(post_staging))
    source_write["authorized_exact_write_paths"].append(unauthorized.as_posix())
    source_write["authorized_directory_metadata_paths"].append(
        staging_root.as_posix()
    )
    source_write["observed_staging_changes"] = _manifest_delta(
        source_write["pre_staging_manifest"], post_staging["entries"]
    )
    source_write["post_staging_manifest_sha256"] = post_staging_sha
    _write_json(summary_path, summary)
    ledger = _rewrite_candidate_ledger(candidate_root)
    expected = replace(
        expected,
        candidate_ledger_sha256=_sha(ledger),
        live_post_staging_manifest_sha256=post_staging_sha,
    )

    result = validate_ops01r_live_capture(staging_root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_LIVE_CAPTURE_IDENTITY_MISMATCH" in result.errors


def test_live_capture_revalidates_excluded_authorization(tmp_path):
    staging_root, _, expected = _live_capture(tmp_path)
    authorization_path = staging_root / "control" / "live_authorization.json"
    authorization_path.write_bytes(authorization_path.read_bytes() + b" ")

    result = validate_ops01r_live_capture(staging_root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_LIVE_CAPTURE_IDENTITY_MISMATCH" in result.errors


def _discovery_pair(
    tmp_path: Path,
    *,
    produce_result: bool = True,
) -> tuple[Path, Path, Ops01RDiscoveryAuthorizationExpectedIdentity]:
    run_id = hashlib.sha256(tmp_path.as_posix().encode()).hexdigest()[:32]
    staging_root = Path("/tmp/hde-epic038-ops01r") / run_id
    shutil.rmtree(staging_root, ignore_errors=True)
    control = staging_root / "control"
    control.mkdir(parents=True)
    source_root = staging_root / "source"
    source_root.mkdir()
    (source_root / "tracked.py").write_text("VALUE = 1\n")
    runner_path = source_root / "scripts/ops/hde_epic038_ops01r.py"
    validator_path = source_root / "tools/evidence/hde_epic038_ops01_v5.py"
    for component_path, content in (
        (runner_path, "RUNNER = 1\n"),
        (validator_path, "VALIDATOR = 1\n"),
    ):
        component_path.parent.mkdir(parents=True, exist_ok=True)
        component_path.write_text(content)
    railway_path = staging_root / "bin/railway"
    railway_path.parent.mkdir()
    railway_path.write_bytes(b"#!/bin/sh\nexit 0\n")
    railway_path.chmod(0o755)
    working_directory = staging_root / "discovery-work"
    working_directory.mkdir()
    source_manifest_object = _tree_manifest(
        source_root, schema="hde_epic038.source_tree_manifest.v1"
    )
    source_manifest = _sha(_canon(source_manifest_object))
    authorization_path = control / "discovery_authorization.json"
    result_path = control / "discovery.json"
    preflight_path = control / "preflight.json"

    def file_identity(path: Path) -> dict[str, str]:
        return {
            "lexical_path": path.as_posix(),
            "resolved_path": path.resolve().as_posix(),
            "sha256": _sha(path.resolve().read_bytes()),
        }

    runner_identity = file_identity(runner_path)
    validator_identity = file_identity(validator_path)
    railway_identity = file_identity(railway_path)
    interpreter_path = Path(sys.executable)
    interpreter_identity = file_identity(interpreter_path)
    preflight = {
        "components": {
            "runner": runner_identity,
            "validator": validator_identity,
        },
        "interpreter": interpreter_identity,
        "railway_executable": railway_identity,
        "run": {
            "run_id": run_id,
            "source_root": source_root.as_posix(),
            "staging_root": staging_root.as_posix(),
        },
        "schema": "hde_epic038.ops01r.preflight.v1",
        "source": {
            "checkout_state": "DETACHED",
            "commit": "2" * 40,
            "repository": "amthorn78/glow-hdengine-v2",
            "root": source_root.as_posix(),
            "source_manifest_sha256": source_manifest,
        },
        "status": "PASS",
    }
    preflight["preflight_identity_sha256"] = _sha(_canon(preflight))
    _write_json(preflight_path, preflight)
    authorization_path.touch()
    pre_staging_object = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(authorization_path, result_path),
        excluded_recursive_roots=(source_root,),
    )
    pre_staging_sha = _sha(_canon(pre_staging_object))
    python_prefix = [
        interpreter_path.as_posix(),
        "-I",
        "-B",
    ]
    target_probe_argv = [
        *python_prefix,
        runner_path.as_posix(),
        "--target-identity-probe",
    ]
    stage_descriptors = {
        "cli_version": [
            {"kind": "literal", "value": "--version"},
        ],
        "cli_help": [
            {"kind": "literal", "value": "help"},
        ],
        "project_inventory": [
            {"kind": "literal", "value": "project"},
            {"kind": "literal", "value": "list"},
        ],
        "environment_inventory": [
            {"kind": "literal", "value": "environment"},
            {"kind": "literal", "value": "list"},
            {"kind": "literal", "value": "--project"},
            {
                "field": "project_id",
                "kind": "prior_result",
                "source_stage": "project_inventory",
            },
        ],
        "service_inventory": [
            {"kind": "literal", "value": "service"},
            {"kind": "literal", "value": "list"},
            {"kind": "literal", "value": "--project"},
            {
                "field": "project_id",
                "kind": "prior_result",
                "source_stage": "project_inventory",
            },
            {"kind": "literal", "value": "--environment"},
            {
                "field": "environment_id",
                "kind": "prior_result",
                "source_stage": "environment_inventory",
            },
        ],
        "target_identity_probe": [
            {"kind": "literal", "value": "run"},
            {"kind": "literal", "value": "--project"},
            {
                "field": "project_id",
                "kind": "prior_result",
                "source_stage": "project_inventory",
            },
            {"kind": "literal", "value": "--environment"},
            {
                "field": "environment_id",
                "kind": "prior_result",
                "source_stage": "environment_inventory",
            },
            {"kind": "literal", "value": "--service"},
            {
                "field": "service_id",
                "kind": "prior_result",
                "source_stage": "service_inventory",
            },
            {"kind": "literal", "value": "--"},
            {"kind": "python_child"},
        ],
    }
    selection_modes = {
        "cli_version": "single",
        "cli_help": "version",
        "project_inventory": "version_and_help",
        "environment_inventory": "version_and_help",
        "service_inventory": "version_and_help",
        "target_identity_probe": "version_and_help",
    }
    policy_stages = []
    for ordinal, stage in enumerate(DISCOVERY_STAGES, start=1):
        policy_stages.append(
            {
                "max_invocations": 1,
                "ordinal": ordinal,
                "predecessors": list(DISCOVERY_STAGES[: ordinal - 1]),
                "selection_mode": selection_modes[stage],
                "stage": stage,
                "templates": [
                    {
                        "argv": stage_descriptors[stage],
                        "required_help_tokens": (
                            ["[COMMAND]"]
                            if selection_modes[stage] == "version_and_help"
                            else []
                        ),
                        "template_id": f"{stage}-v1",
                        "version_regex": (
                            "" if stage == "cli_version" else r"railway 4\.0\.0"
                        ),
                    }
                ],
            }
        )
    authorization = {
        "schema": "hde_epic038.ops01r.discovery_authorization.v1",
        "source": {
            "commit": "2" * 40,
            "repository": "amthorn78/glow-hdengine-v2",
            "root": source_root.as_posix(),
            "source_manifest_sha256": source_manifest,
            "state": "DETACHED",
        },
        "discovery_entry_point": runner_identity,
        "preflight": {
            "path": preflight_path.as_posix(),
            "preflight_identity_sha256": preflight[
                "preflight_identity_sha256"
            ],
            "source_manifest_sha256": source_manifest,
        },
        "railway_cli": railway_identity,
        "policy": {
            "argv_rules": {
                "allow_control_characters": False,
                "allow_empty_tokens": False,
                "allow_endpoint_or_secret_values": False,
                "allow_shell": False,
                "executable_token_source": "authorized_railway_cli_lexical_path",
                "forbidden_casefolded_tokens": [
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
                ],
            },
            "permitted_command_families": list(DISCOVERY_STAGES),
            "prohibited_command_families": [
                "arbitrary_child_execution",
                "database_connect",
                "deployment",
                "environment_mutation",
                "linked_context_change",
                "log_stream",
                "project_mutation",
                "redeployment",
                "remote_shell",
                "restart",
                "selection_change",
                "service_mutation",
                "variable_read",
                "variable_write",
            ],
            "python_execution": {
                "authorization_validator_argv": [
                    *python_prefix,
                    validator_path.as_posix(),
                    "--validate-discovery-authorization",
                    "--expected-identity-stdin",
                    authorization_path.as_posix(),
                ],
                "bytecode_flag": "-B",
                "bytecode_write_control": "python_flag_-B",
                "discovery_producer_argv": [
                    *python_prefix,
                    runner_path.as_posix(),
                    "--discovery",
                    authorization_path.as_posix(),
                ],
                "environment_name_rule": "no_casefolded_python_prefix",
                "interpreter_argv_prefix": python_prefix,
                "python_environment_names": [],
                "result_validator_argv": [
                    *python_prefix,
                    validator_path.as_posix(),
                    "--validate-discovery-result",
                    "--expected-identity-stdin",
                    result_path.as_posix(),
                    authorization_path.as_posix(),
                ],
                "target_probe_argv": target_probe_argv,
            },
            "sanitization": {
                "allowed_value_classes": [
                    "boolean",
                    "cli_version",
                    "identity_field_name",
                    "integer_count",
                    "sanitized_argv",
                    "schema_literal",
                    "sha256",
                    "target_id",
                    "target_name",
                ],
                "endpoint_values_retained": False,
                "forbidden_field_name_regex": r"(?i)(secret|token|password|passwd|api[_-]?key|database_url|db_bridge_url|authorization|cookie)",
                "raw_stderr_retained": False,
                "raw_stdout_retained": False,
                "secret_like_output_action": "fail",
            },
            "schema": "hde_epic038.ops01r.discovery_policy.v1",
            "stages": policy_stages,
            "template_selection": {
                "cardinality": "exactly_one",
                "help_match": "every_required_help_token_present_as_case_sensitive_exact_token",
                "tie_break": "none_fail_on_zero_or_multiple",
                "version_match": "python_re_fullmatch_on_normalized_version",
            },
        },
        "output_contract": {
            "canonical_json": True,
            "path": result_path.as_posix(),
            "raw_cli_output_retained": False,
            "schema": "hde_epic038.ops01r.discovery.v1",
            "trailing_lf": True,
        },
        "run_id": run_id,
        "requested_target": {
            "project_name": "ample-illumination",
            "environment_name": "production",
            "service_name": "glow-hdengine-v2",
        },
        "nonclaims": [
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
        ],
        "subprocess_limit": 6,
        "working_directory": {
            "linked_context_required": False,
            "must_be_empty": True,
            "path": working_directory.as_posix(),
        },
        "write_contract": {
            "authorized_directory_metadata_paths": [control.as_posix()],
            "authorized_exact_write_paths": [result_path.as_posix()],
            "authorized_recursive_write_roots": [],
            "pre_staging_manifest": pre_staging_object["entries"],
            "pre_staging_manifest_sha256": pre_staging_sha,
            "self_bound_excluded_paths": sorted(
                (authorization_path.as_posix(), result_path.as_posix()),
                key=lambda value: value.encode("utf-8"),
            ),
            "self_bound_excluded_recursive_roots": [],
            "source_root_writes_authorized": False,
        },
    }
    authorization["discovery_authorization_sha256"] = _sha(_canon(authorization))
    _write_json(authorization_path, authorization)
    assert _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(authorization_path, result_path),
        excluded_recursive_roots=(source_root,),
    )["entries"] == pre_staging_object["entries"]
    expected = Ops01RDiscoveryAuthorizationExpectedIdentity(
        discovery_authorization_sha256=authorization[
            "discovery_authorization_sha256"
        ],
        discovery_entry_point_sha256=runner_identity["sha256"],
        literal_staging_root=staging_root.as_posix(),
        pre_staging_manifest_sha256=pre_staging_sha,
        preflight_identity_sha256=preflight["preflight_identity_sha256"],
        railway_executable_sha256=railway_identity["sha256"],
        source_commit="2" * 40,
        source_manifest_sha256=source_manifest,
    )
    railway_lexical = railway_path.as_posix()
    manifest: list[object] = [
        [railway_lexical, "--version"],
        [railway_lexical, "help"],
        [railway_lexical, "project", "list"],
        [
            railway_lexical,
            "environment",
            "list",
            "--project",
            "project-id",
        ],
        [
            railway_lexical,
            "service",
            "list",
            "--project",
            "project-id",
            "--environment",
            "environment-id",
        ],
        [
            railway_lexical,
            "run",
            "--project",
            "project-id",
            "--environment",
            "environment-id",
            "--service",
            "service-id",
            "--",
            *target_probe_argv,
        ],
    ]
    if not produce_result:
        return result_path, authorization_path, expected
    prefix = manifest[-1][: -len(target_probe_argv)]
    identity_contract = [
        {
            "expected_value": "environment-id",
            "field_name": "RAILWAY_ENVIRONMENT_ID",
            "target_dimension": "environment",
            "value_kind": "target_id",
        },
        {
            "expected_value": "project-id",
            "field_name": "RAILWAY_PROJECT_ID",
            "target_dimension": "project",
            "value_kind": "target_id",
        },
        {
            "expected_value": "service-id",
            "field_name": "RAILWAY_SERVICE_ID",
            "target_dimension": "service",
            "value_kind": "target_id",
        },
    ]
    child_environment_contract = sorted(
        [
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
                    "name": row["field_name"],
                    "source": "railway_target_identity",
                    "value_policy": f"exact:{row['expected_value']}",
                }
                for row in identity_contract
            ],
        ],
        key=lambda row: row["name"].encode("utf-8"),
    )
    result_path.touch()
    post_staging_object = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(authorization_path, result_path),
        excluded_recursive_roots=(source_root,),
    )
    observed_delta = _manifest_delta(
        pre_staging_object["entries"], post_staging_object["entries"]
    )
    result = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_run_id": run_id,
        "discovery_authorization_sha256": authorization[
            "discovery_authorization_sha256"
        ],
        "command_manifest": manifest,
        "command_manifest_sha256": _sha(_canon(manifest)),
        "railway_cli": {
            "path": railway_identity["lexical_path"],
            "resolved_path": railway_identity["resolved_path"],
            "sha256": railway_identity["sha256"],
            "version": "railway 4.0.0",
        },
        "target": {
            "project_id": "project-id",
            "project_name": "ample-illumination",
            "environment_id": "environment-id",
            "environment_name": "production",
            "service_id": "service-id",
            "service_name": "glow-hdengine-v2",
        },
        "run_contract": {
            "argv_prefix": prefix,
            "child_argv_start_index": len(prefix),
            "child_environment_contract": child_environment_contract,
            "linked_context_required": False,
            "python_execution": authorization["policy"]["python_execution"],
            "target_dimensions": ["project", "environment", "service"],
        },
        "identity_contract": identity_contract,
        "counts": {
            "command_manifest_entries": 6,
            "discovery_subprocesses": 6,
            "provider_constructions": 0,
            "db_connections": 0,
            "direct_sql_statements": 0,
            "bridge_http_requests": 0,
            "vendor_requests": 0,
        },
        "nonclaims": authorization["nonclaims"],
        "source_write_validation": {
            "authorized_directory_metadata_paths": [control.as_posix()],
            "authorized_exact_write_paths": [result_path.as_posix()],
            "authorized_recursive_write_roots": [],
            "bytecode_write_control": "python_flag_-B",
            "manifest_algorithm": "hde_epic038.source_tree_manifest.v1",
            "mode": "discovery",
            "observed_staging_changes": observed_delta,
            "pre_source_manifest_sha256": source_manifest,
            "post_source_manifest_sha256": source_manifest,
            "pre_staging_manifest": pre_staging_object["entries"],
            "pre_staging_manifest_sha256": pre_staging_sha,
            "post_staging_manifest_sha256": _sha(_canon(post_staging_object)),
            "prohibited_cache_paths": [],
            "python_argv": target_probe_argv,
            "python_environment_names": [],
            "self_bound_excluded_paths": authorization["write_contract"]["self_bound_excluded_paths"],
            "self_bound_excluded_recursive_roots": [],
            "source_root": source_root.as_posix(),
            "source_tree_unchanged": True,
            "staging_manifest_algorithm": "hde_epic038.non_source_staging_manifest.v1",
            "staging_write_set_valid": True,
            "status": "PASS",
            "unauthorized_staging_paths": [],
        },
    }
    result["discovery_identity_sha256"] = _sha(_canon(result))
    _write_json(result_path, result)
    return result_path, authorization_path, expected


def _rewrite_discovery_authorization(
    authorization_path: Path,
    expected: Ops01RDiscoveryAuthorizationExpectedIdentity,
    mutation,
) -> Ops01RDiscoveryAuthorizationExpectedIdentity:
    authorization = json.loads(authorization_path.read_text())
    mutation(authorization)
    authorization["discovery_authorization_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in authorization.items()
                if key != "discovery_authorization_sha256"
            }
        )
    )
    _write_json(authorization_path, authorization)
    return replace(
        expected,
        discovery_authorization_sha256=authorization[
            "discovery_authorization_sha256"
        ],
    )


def test_discovery_result_is_bound_to_reviewed_authorization(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    assert validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    ).valid

    wrong_expected = replace(expected, source_commit="f" * 40)
    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=wrong_expected,
    )
    assert not result.valid
    assert "DISCOVERY_RESULT_AUTHORIZATION_MISMATCH" in result.errors


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    [
        (
            lambda authorization: authorization["policy"].update(
                {"unreviewed_policy": True}
            ),
            "DISCOVERY_AUTH_UNKNOWN_KEY",
        ),
        (
            lambda authorization: authorization["policy"]["stages"][2][
                "templates"
            ][0].update({"unreviewed_template": True}),
            "DISCOVERY_AUTH_UNKNOWN_KEY",
        ),
        (
            lambda authorization: authorization["policy"]["python_execution"][
                "discovery_producer_argv"
            ].append("--alternate"),
            "DISCOVERY_AUTH_PYTHON_ARGV_MISMATCH",
        ),
    ],
)
def test_discovery_authorization_recursively_closes_policy(
    tmp_path, mutation, expected_code
):
    _, authorization_path, expected = _discovery_pair(
        tmp_path, produce_result=False
    )
    expected = _rewrite_discovery_authorization(
        authorization_path, expected, mutation
    )

    result = validate_ops01r_discovery_authorization(
        authorization_path, expected=expected
    )

    assert not result.valid
    assert expected_code in result.errors


def test_runner_rejects_rehashed_policy_expansion_before_subprocess(
    tmp_path, monkeypatch
):
    import scripts.ops.hde_epic038_ops01r as runner
    import tools.evidence.hde_epic038_ops01_v5 as validator

    _, authorization_path, expected = _discovery_pair(
        tmp_path, produce_result=False
    )
    original_dispatch = validator.validate_ops01r_discovery_dispatch
    subprocess_calls = []

    def mutate_after_dispatch(*args, **kwargs):
        result = original_dispatch(*args, **kwargs)
        _rewrite_discovery_authorization(
            authorization_path,
            expected,
            lambda authorization: authorization["policy"]["stages"][1][
                "templates"
            ][0]["argv"].append({"kind": "literal", "value": "status"}),
        )
        return result

    def fail_if_called(*args, **kwargs):
        subprocess_calls.append(args)
        raise AssertionError("subprocess crossed the mutated authorization boundary")

    monkeypatch.setattr(
        validator,
        "validate_ops01r_discovery_dispatch",
        mutate_after_dispatch,
    )
    monkeypatch.setattr(runner.subprocess, "run", fail_if_called)

    with pytest.raises(SystemExit, match="OPS01R_DISCOVERY_AUTH_INVALID"):
        runner.discovery(authorization_path, expected=expected)
    assert subprocess_calls == []


def test_discovery_result_replays_command_policy(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    payload["command_manifest"][0] = [
        payload["railway_cli"]["path"],
        "deploy",
    ]
    payload["command_manifest_sha256"] = _sha(_canon(payload["command_manifest"]))
    payload["discovery_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in payload.items()
                if key != "discovery_identity_sha256"
            }
        )
    )
    _write_json(result_path, payload)

    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    )

    assert not result.valid
    assert "DISCOVERY_RESULT_ARGV_MISMATCH" in result.errors


def test_discovery_result_requires_all_six_stages(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    payload["command_manifest"] = payload["command_manifest"][:-1]
    payload["command_manifest_sha256"] = _sha(_canon(payload["command_manifest"]))
    payload["discovery_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in payload.items()
                if key != "discovery_identity_sha256"
            }
        )
    )
    _write_json(result_path, payload)

    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    )

    assert not result.valid
    assert "DISCOVERY_RESULT_STAGE_COUNT_INVALID" in result.errors


def test_discovery_dispatch_requires_exact_authorized_stage_argv(tmp_path):
    _, authorization_path, _ = _discovery_pair(tmp_path, produce_result=False)
    authorization = json.loads(authorization_path.read_text())
    railway_path = authorization["railway_cli"]["lexical_path"]
    assert validate_ops01r_discovery_dispatch(
        authorization_path,
        stage="cli_version",
        prior_results={},
        rendered_argv=(railway_path, "--version"),
    ).valid

    result = validate_ops01r_discovery_dispatch(
        authorization_path,
        stage="cli_version",
        prior_results={},
        rendered_argv=(railway_path, "run", "python", "-c", "print('unsafe')"),
    )

    assert not result.valid
    assert "DISCOVERY_AUTH_PROHIBITED_COMMAND" in result.errors


def test_discovery_result_requires_authorized_output_path(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    copied_path = tmp_path / "copied-discovery.json"
    copied_path.write_bytes(result_path.read_bytes())

    result = validate_ops01r_discovery_result(
        copied_path,
        authorization_path=authorization_path,
        expected=expected,
    )

    assert not result.valid
    assert "DISCOVERY_RESULT_WRITE_SET_MISMATCH" in result.errors


def test_discovery_authorization_requires_output_path(tmp_path):
    _, authorization_path, expected = _discovery_pair(tmp_path)
    authorization = json.loads(authorization_path.read_text())
    authorization["output_contract"] = {}
    authorization["discovery_authorization_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in authorization.items()
                if key != "discovery_authorization_sha256"
            }
        )
    )
    _write_json(authorization_path, authorization)
    expected = replace(
        expected,
        discovery_authorization_sha256=authorization[
            "discovery_authorization_sha256"
        ],
    )

    result = validate_ops01r_discovery_authorization(
        authorization_path, expected=expected
    )

    assert not result.valid
    assert "DISCOVERY_AUTH_OUTPUT_CONTRACT_INVALID" in result.errors


def test_discovery_result_rejects_tampered_authorization_hash(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    payload["discovery_authorization_sha256"] = "e" * 64
    payload["discovery_identity_sha256"] = _sha(
        _canon({key: value for key, value in payload.items() if key != "discovery_identity_sha256"})
    )
    _write_json(result_path, payload)
    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    )
    assert not result.valid
    assert "DISCOVERY_RESULT_AUTHORIZATION_MISMATCH" in result.errors


@pytest.mark.parametrize(
    "payload",
    [
        "not json",
        _canon({"project_name": "ample-illumination"}).decode("ascii"),
        _canon(
            {
                "project_id": "",
                "project_name": "ample-illumination",
            }
        ).decode("ascii"),
        _canon(
            {
                "project_id": "project-id",
                "project_name": " ample-illumination",
            }
        ).decode("ascii"),
    ],
)
def test_runner_discovery_parser_rejects_missing_or_invalid_target_identity(payload):
    import scripts.ops.hde_epic038_ops01r as runner

    with pytest.raises(SystemExit, match="OPS01R_DISCOVERY_TARGET_AMBIGUOUS"):
        runner._parse_stage("project_inventory", payload)


def test_runner_discovery_parser_does_not_treat_version_or_help_as_target_json():
    import scripts.ops.hde_epic038_ops01r as runner

    assert runner._parse_stage("cli_version", "railway 4.0.0\n") == {
        "version": "railway 4.0.0"
    }
    assert runner._parse_stage("cli_help", "Usage: railway [COMMAND]\n") == {
        "help_tokens": ["Usage:", "railway", "[COMMAND]"]
    }


def test_runner_discovery_parser_requires_exact_no_write_target_probe_result():
    import scripts.ops.hde_epic038_ops01r as runner

    valid = _canon(
        {
            "endpoint_presence": {
                "DATABASE_URL": True,
                "DB_BRIDGE_URL": True,
            },
            "identity_fields": [
                {"name": "RAILWAY_PROJECT_ID", "value": "project-id"}
            ],
            "schema": "hde_epic038.ops01r.target_identity_probe.v1",
            "writes": 0,
        }
    ).decode("ascii")
    assert runner._parse_stage("target_identity_probe", valid) == json.loads(valid)

    with pytest.raises(SystemExit, match="OPS01R_DISCOVERY_TARGET_AMBIGUOUS"):
        runner._parse_stage(
            "target_identity_probe",
            _canon(
                {
                    "endpoint_presence": {
                        "DATABASE_URL": True,
                        "DB_BRIDGE_URL": True,
                    },
                    "identity_fields": [],
                    "schema": "hde_epic038.ops01r.target_identity_probe.v1",
                    "writes": 1,
                }
            ).decode("ascii"),
        )


def test_discovery_result_rejects_incomplete_target_identity(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    del payload["target"]["service_id"]
    payload["discovery_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in payload.items()
                if key != "discovery_identity_sha256"
            }
        )
    )
    _write_json(result_path, payload)

    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    )

    assert not result.valid
    assert "DISCOVERY_RESULT_TARGET_AMBIGUOUS" in result.errors


def test_discovery_result_rejects_unlisted_child_environment(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    payload["run_contract"]["child_environment_contract"].append(
        {
            "name": "HD_API_KEY",
            "source": "railway_service",
            "value_policy": "presence_only",
        }
    )
    payload["run_contract"]["child_environment_contract"].sort(
        key=lambda row: row["name"].encode("utf-8")
    )
    payload["discovery_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in payload.items()
                if key != "discovery_identity_sha256"
            }
        )
    )
    _write_json(result_path, payload)

    result = validate_ops01r_discovery_result(
        result_path,
        authorization_path=authorization_path,
        expected=expected,
    )

    assert not result.valid
    assert "DISCOVERY_RESULT_IDENTITY_CONTRACT_INVALID" in result.errors


def _discovery_stage_outputs() -> dict[str, str]:
    return {
        "cli_version": "railway 4.0.0\n",
        "cli_help": "Usage: railway [COMMAND]\n",
        "project_inventory": _canon(
            {"project_id": "project-id", "project_name": "ample-illumination"}
        ).decode("ascii"),
        "environment_inventory": _canon(
            {
                "environment_id": "environment-id",
                "environment_name": "production",
            }
        ).decode("ascii"),
        "service_inventory": _canon(
            {"service_id": "service-id", "service_name": "glow-hdengine-v2"}
        ).decode("ascii"),
        "target_identity_probe": _canon(
            {
                "endpoint_presence": {
                    "DATABASE_URL": True,
                    "DB_BRIDGE_URL": True,
                },
                "identity_fields": [
                    {"name": "RAILWAY_PROJECT_ID", "value": "project-id"},
                    {
                        "name": "RAILWAY_ENVIRONMENT_ID",
                        "value": "environment-id",
                    },
                    {"name": "RAILWAY_SERVICE_ID", "value": "service-id"},
                ],
                "schema": "hde_epic038.ops01r.target_identity_probe.v1",
                "writes": 0,
            }
        ).decode("ascii"),
    }


def test_runner_discovery_emits_bound_run_contract(tmp_path, monkeypatch):
    import scripts.ops.hde_epic038_ops01r as runner

    result_path, authorization_path, expected = _discovery_pair(
        tmp_path, produce_result=False
    )
    outputs = _discovery_stage_outputs()
    calls = []

    def fake_run(argv, **kwargs):
        stage = DISCOVERY_STAGES[len(calls)]
        calls.append((tuple(argv), kwargs))
        return subprocess.CompletedProcess(argv, 0, outputs[stage], "")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)

    assert runner.discovery(authorization_path, expected=expected) == 0
    payload = json.loads(result_path.read_text())
    probe_argv = json.loads(authorization_path.read_text())["policy"][
        "python_execution"
    ]["target_probe_argv"]
    expected_prefix = payload["command_manifest"][-1][: -len(probe_argv)]
    assert payload["run_contract"]["argv_prefix"] == expected_prefix
    assert payload["run_contract"]["child_argv_start_index"] == len(
        expected_prefix
    )
    assert payload["command_manifest"][-1] == [
        *payload["run_contract"]["argv_prefix"],
        *probe_argv,
    ]
    assert {
        row["target_dimension"] for row in payload["identity_contract"]
    } == {"project", "environment", "service"}
    assert len(calls) == len(DISCOVERY_STAGES)
    assert all(call[1]["cwd"].name == "discovery-work" for call in calls)
    assert validate_ops01r_discovery_result(
        result_path, authorization_path=authorization_path, expected=expected
    ).valid


def test_runner_discovery_rejects_post_subprocess_staging_write(
    tmp_path, monkeypatch
):
    import scripts.ops.hde_epic038_ops01r as runner

    _, authorization_path, expected = _discovery_pair(
        tmp_path, produce_result=False
    )
    outputs = _discovery_stage_outputs()
    calls = []

    def fake_run(argv, **kwargs):
        stage = DISCOVERY_STAGES[len(calls)]
        calls.append(stage)
        if stage == "service_inventory":
            authorization_path.parent.parent.joinpath("unauthorized.txt").write_text(
                "unauthorized\n"
            )
        return subprocess.CompletedProcess(argv, 0, outputs[stage], "")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)

    with pytest.raises(SystemExit, match="OPS01R_DISCOVERY_WRITE_SET_MISMATCH"):
        runner.discovery(authorization_path, expected=expected)
    assert calls == list(DISCOVERY_STAGES[:-1])


def test_preflight_uses_canonical_nested_identity_fields(tmp_path):
    run_id = hashlib.sha256(tmp_path.as_posix().encode()).hexdigest()[:32]
    staging_root = Path("/tmp/hde-epic038-ops01r") / run_id
    shutil.rmtree(staging_root, ignore_errors=True)
    source_root = staging_root / "source"
    control_root = staging_root / "control"
    working_directory = staging_root / "preflight-work"
    source_root.mkdir(parents=True)
    control_root.mkdir()
    working_directory.mkdir()
    component_contents = {
        "engine/db/ddl_identity_projection.py": b"PROJECTOR = 1\n",
        "scripts/db/capture_epic011_posture.py": b"CAPTURE = 1\n",
        "scripts/ops/hde_epic038_ops01r.py": b"RUNNER = 1\n",
        "tools/evidence/hde_epic038_ops01_v5.py": b"VALIDATOR = 1\n",
    }
    for relative, content in component_contents.items():
        component_path = source_root / relative
        component_path.parent.mkdir(parents=True, exist_ok=True)
        component_path.write_bytes(content)
    railway_path = staging_root / "bin/railway"
    railway_path.parent.mkdir()
    railway_path.write_bytes(b"#!/bin/sh\nexit 0\n")
    railway_path.chmod(0o755)
    path = control_root / "preflight.json"
    source_manifest_object = _tree_manifest(
        source_root, schema="hde_epic038.source_tree_manifest.v1"
    )
    source_manifest = _sha(_canon(source_manifest_object))
    pre_staging_object = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(path,),
        excluded_recursive_roots=(source_root,),
    )
    pre_staging = _sha(_canon(pre_staging_object))
    path.touch()
    post_staging_object = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(path,),
        excluded_recursive_roots=(source_root,),
    )
    counts = {
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
    producer_argv = [
        sys.executable,
        "-I",
        "-B",
        (source_root / "scripts/ops/hde_epic038_ops01r.py").as_posix(),
        "--preflight",
    ]
    zero_io = {name: 0 for name in PREFLIGHT_ZERO_IO_FIELDS}
    orchestration = {
        "fake_boundary_mode": "count_before_fail_on_touch_delegate",
        "run_1": {
            "actual_external_io_counts": zero_io,
            "expected_call_counts": counts,
        },
        "run_2": {
            "actual_external_io_counts": zero_io,
            "expected_call_counts": counts,
        },
        "run_count": 2,
        "vectors_equal": True,
    }
    record = {
        "schema": "hde_epic038.ops01r.preflight.v1",
        "status": "PASS",
        "actual_external_io_counts": zero_io,
        "expected_call_counts": counts,
        "nonclaims": list(PREFLIGHT_NONCLAIMS),
        "run": {
            "control_root": control_root.as_posix(),
            "preflight_path": path.as_posix(),
            "run_id": run_id,
            "source_root": source_root.as_posix(),
            "staging_root": staging_root.as_posix(),
            "working_directory": working_directory.as_posix(),
        },
        "source": {
            "checkout_state": "DETACHED",
            "commit": "2" * 40,
            "repository": "amthorn78/glow-hdengine-v2",
            "root": source_root.as_posix(),
            "source_manifest_sha256": source_manifest,
            "worktree_state": "clean",
        },
        "components": {
            "runner": {"lexical_path": producer_argv[3], "resolved_path": producer_argv[3], "sha256": _sha(component_contents["scripts/ops/hde_epic038_ops01r.py"])},
            "validator": {"lexical_path": (source_root / "tools/evidence/hde_epic038_ops01_v5.py").as_posix(), "resolved_path": (source_root / "tools/evidence/hde_epic038_ops01_v5.py").as_posix(), "sha256": _sha(component_contents["tools/evidence/hde_epic038_ops01_v5.py"])},
            "projector": {"lexical_path": (source_root / "engine/db/ddl_identity_projection.py").as_posix(), "resolved_path": (source_root / "engine/db/ddl_identity_projection.py").as_posix(), "sha256": _sha(component_contents["engine/db/ddl_identity_projection.py"])},
        },
        "interpreter": {
            "bytecode_flag": "-B",
            "bytecode_write_control": "python_flag_-B",
            "isolated_flag": "-I",
            "lexical_path": sys.executable,
            "preflight_argv": producer_argv,
            "preflight_validator_argv": [sys.executable, "-I", "-B", (source_root / "tools/evidence/hde_epic038_ops01_v5.py").as_posix(), "--validate-preflight", "--expected-identity-stdin", path.as_posix()],
            "python_environment_names": [],
            "resolved_path": Path(sys.executable).resolve().as_posix(),
            "sha256": _sha(Path(sys.executable).resolve().read_bytes()),
        },
        "module_origins": [
            {
                "lexical_origin": (source_root / relative).as_posix(),
                "module": module,
                "resolved_origin": (source_root / relative).as_posix(),
                "sha256": _sha(component_contents[relative]),
            }
            for module, relative in sorted(
                {
                    "engine.db.ddl_identity_projection": "engine/db/ddl_identity_projection.py",
                    "scripts.db.capture_epic011_posture": "scripts/db/capture_epic011_posture.py",
                    "scripts.ops.hde_epic038_ops01r": "scripts/ops/hde_epic038_ops01r.py",
                    "tools.evidence.hde_epic038_ops01_v5": "tools/evidence/hde_epic038_ops01_v5.py",
                }.items()
            )
        ],
        "orchestration": orchestration,
        "railway_executable": {
            "lexical_path": railway_path.as_posix(),
            "resolved_path": railway_path.as_posix(),
            "sha256": _sha(railway_path.read_bytes()),
        },
        "source_write_validation": {
            "authorized_directory_metadata_paths": [control_root.as_posix()],
            "authorized_exact_write_paths": [path.as_posix()],
            "authorized_recursive_write_roots": [],
            "bytecode_write_control": "python_flag_-B",
            "manifest_algorithm": "hde_epic038.source_tree_manifest.v1",
            "mode": "preflight",
            "observed_staging_changes": _manifest_delta(pre_staging_object["entries"], post_staging_object["entries"]),
            "post_source_manifest_sha256": source_manifest,
            "post_staging_manifest_sha256": _sha(_canon(post_staging_object)),
            "pre_source_manifest_sha256": source_manifest,
            "pre_staging_manifest": pre_staging_object["entries"],
            "pre_staging_manifest_sha256": pre_staging,
            "prohibited_cache_paths": [],
            "python_argv": producer_argv,
            "python_environment_names": [],
            "self_bound_excluded_paths": [path.as_posix()],
            "self_bound_excluded_recursive_roots": [],
            "source_root": source_root.as_posix(),
            "source_tree_unchanged": True,
            "staging_manifest_algorithm": "hde_epic038.non_source_staging_manifest.v1",
            "staging_write_set_valid": True,
            "status": "PASS",
            "unauthorized_staging_paths": [],
        },
    }
    record["preflight_identity_sha256"] = _sha(_canon(record))
    _write_json(path, record)
    expected = Ops01RPreflightExpectedIdentity(
        source_commit="2" * 40,
        source_manifest_sha256=source_manifest,
        pre_staging_manifest_sha256=pre_staging,
        literal_staging_root=record["run"]["staging_root"],
        runner_sha256=_sha(component_contents["scripts/ops/hde_epic038_ops01r.py"]),
        validator_sha256=_sha(component_contents["tools/evidence/hde_epic038_ops01_v5.py"]),
        projector_sha256=_sha(component_contents["engine/db/ddl_identity_projection.py"]),
        interpreter_sha256=_sha(Path(sys.executable).resolve().read_bytes()),
        railway_executable_sha256=_sha(railway_path.read_bytes()),
        preflight_identity_sha256=record["preflight_identity_sha256"],
    )
    assert validate_ops01r_preflight(path, expected=expected).valid

    for key, bad_value in (
        ("authorized_exact_write_paths", [path.with_name("other.json").as_posix()]),
        ("authorized_recursive_write_roots", [staging_root.as_posix()]),
        ("authorized_directory_metadata_paths", [staging_root.as_posix()]),
        ("self_bound_excluded_paths", []),
        ("self_bound_excluded_recursive_roots", [source_root.as_posix()]),
    ):
        mutated = json.loads(json.dumps(record))
        mutated["source_write_validation"][key] = bad_value
        mutated["preflight_identity_sha256"] = _sha(
            _canon({k: v for k, v in mutated.items() if k != "preflight_identity_sha256"})
        )
        _write_json(path, mutated)
        result = validate_ops01r_preflight(
            path,
            expected=replace(
                expected,
                preflight_identity_sha256=mutated["preflight_identity_sha256"],
            ),
        )
        assert not result.valid, key
        assert "PREFLIGHT_WRITE_SET_MISMATCH" in result.errors

    for key, value in (
        ("run_count", 1),
        ("vectors_equal", False),
        ("fake_boundary_mode", "copied_constants"),
    ):
        mutated = json.loads(json.dumps(record))
        mutated["orchestration"][key] = value
        mutated["preflight_identity_sha256"] = _sha(
            _canon({k: v for k, v in mutated.items() if k != "preflight_identity_sha256"})
        )
        _write_json(path, mutated)
        result = validate_ops01r_preflight(
            path,
            expected=replace(
                expected,
                preflight_identity_sha256=mutated["preflight_identity_sha256"],
            ),
        )
        assert not result.valid, key
        assert "PREFLIGHT_ORCHESTRATION_MISMATCH" in result.errors

    for field, bad_vector in (
        ("preflight_argv", ["/tmp/not-python", "-I", "-B", producer_argv[3], "--preflight"]),
        ("preflight_argv", [*producer_argv, "--extra"]),
        (
            "preflight_validator_argv",
            [sys.executable, "-I", "-B", record["components"]["validator"]["lexical_path"], "--validate-preflight", path.as_posix()],
        ),
    ):
        mutated = json.loads(json.dumps(record))
        mutated["interpreter"][field] = bad_vector
        if field == "preflight_argv":
            mutated["source_write_validation"]["python_argv"] = bad_vector
        mutated["preflight_identity_sha256"] = _sha(
            _canon({k: v for k, v in mutated.items() if k != "preflight_identity_sha256"})
        )
        _write_json(path, mutated)
        result = validate_ops01r_preflight(
            path,
            expected=replace(
                expected,
                preflight_identity_sha256=mutated["preflight_identity_sha256"],
            ),
        )
        assert not result.valid, field
        assert "PREFLIGHT_PYTHON_ARGV_MISMATCH" in result.errors

    _write_json(path, record)
    assert not validate_ops01r_preflight(
        path,
        expected=replace(expected, runner_sha256="f" * 64),
    ).valid

    record["actual_external_io_counts"]["railway_subprocesses"] = 1
    record["preflight_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in record.items()
                if key != "preflight_identity_sha256"
            }
        )
    )
    _write_json(path, record)
    result = validate_ops01r_preflight(
        path,
        expected=replace(
            expected,
            preflight_identity_sha256=record["preflight_identity_sha256"],
        ),
    )
    assert not result.valid
    assert "PREFLIGHT_ACTUAL_IO_NONZERO" in result.errors

    record["actual_external_io_counts"]["railway_subprocesses"] = 0
    del record["nonclaims"]
    record["preflight_identity_sha256"] = _sha(
        _canon(
            {
                key: value
                for key, value in record.items()
                if key != "preflight_identity_sha256"
            }
        )
    )
    _write_json(path, record)
    result = validate_ops01r_preflight(
        path,
        expected=replace(
            expected,
            preflight_identity_sha256=record["preflight_identity_sha256"],
        ),
    )
    assert not result.valid
    assert "PREFLIGHT_NONCLAIMS_INVALID" in result.errors

    (source_root / "tracked.py").write_text("VALUE = 2\n")
    (staging_root / "unauthorized.txt").write_text("not authorized\n")
    result = validate_ops01r_preflight(
        path,
        expected=replace(
            expected,
            preflight_identity_sha256=record["preflight_identity_sha256"],
        ),
    )
    assert not result.valid
    assert "PREFLIGHT_SOURCE_MANIFEST_MISMATCH" in result.errors
    assert "PREFLIGHT_WRITE_SET_MISMATCH" in result.errors
    shutil.rmtree(staging_root, ignore_errors=True)


def _live_authorization_pair(
    tmp_path: Path,
) -> tuple[Path, dict[str, object], Ops01RLiveAuthorizationExpectedIdentity]:
    counts = {
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
    staging_root = tmp_path / ("a" * 32)
    source_root = staging_root / "source"
    control_root = staging_root / "control"
    candidate_root = staging_root / "candidate"
    source_root.mkdir(parents=True)
    control_root.mkdir()
    candidate_root.mkdir()
    runner_path = source_root / "scripts/ops/hde_epic038_ops01r.py"
    validator_path = source_root / "tools/evidence/hde_epic038_ops01_v5.py"
    projector_path = source_root / "engine/db/ddl_identity_projection.py"
    for path_value, content in (
        (runner_path, "RUNNER = 1\n"),
        (validator_path, "VALIDATOR = 1\n"),
        (projector_path, "PROJECTOR = 1\n"),
    ):
        path_value.parent.mkdir(parents=True, exist_ok=True)
        path_value.write_text(content)
    source_manifest_object = _tree_manifest(
        source_root, schema="hde_epic038.source_tree_manifest.v1"
    )
    source_manifest = _sha(_canon(source_manifest_object))
    path = control_root / "live_authorization.json"
    failure_path = control_root / "failure.json"
    marker_path = control_root / "live_authority_consumed.json"
    path.touch()
    pre_staging_object = _tree_manifest(
        staging_root,
        schema="hde_epic038.non_source_staging_manifest.v1",
        excluded_paths=(path, failure_path),
        excluded_recursive_roots=(source_root, candidate_root),
    )
    pre_staging_sha = _sha(_canon(pre_staging_object))
    interpreter_path = Path(sys.executable).resolve()
    child = [
        interpreter_path.as_posix(),
        "-I",
        "-B",
        runner_path.as_posix(),
        "--live-child",
    ]
    prefix = ["railway", "run", "--service", "glow-hdengine-v2", "--"]
    discovery: dict[str, object] = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "railway_cli": {"sha256": "9" * 64},
        "target": {
            "project_id": "project-id",
            "project_name": "ample-illumination",
            "environment_id": "environment-id",
            "environment_name": "production",
            "service_id": "service-id",
            "service_name": "glow-hdengine-v2",
        },
        "identity_contract": [
            {
                "expected_value": "project-id",
                "field_name": "RAILWAY_PROJECT_ID",
                "target_dimension": "project",
                "value_kind": "target_id",
            }
        ],
        "run_contract": {
            "argv_prefix": prefix,
            "child_argv_start_index": len(prefix),
            "child_environment_contract": [
                {"name": "DATABASE_URL", "source": "railway_service", "value_policy": "presence_only"},
                {"name": "DB_BRIDGE_URL", "source": "railway_service", "value_policy": "presence_only"},
                {"name": "RAILWAY_PROJECT_ID", "source": "railway_target_identity", "value_policy": "exact:project-id"},
            ],
        },
    }
    discovery["discovery_identity_sha256"] = _sha(_canon(discovery))
    authorization: dict[str, object] = {
        "schema": "hde_epic038.ops01r.authorization.v1",
        "source": {
            "repository": "amthorn78/glow-hdengine-v2",
            "commit": "1" * 40,
            "root": source_root.as_posix(),
            "source_manifest_sha256": source_manifest,
            "state": "DETACHED",
        },
        "run": {
            "authorization_path": path.as_posix(),
            "candidate_root": candidate_root.as_posix(),
            "child_argv": child,
            "launcher_argv": [
                interpreter_path.as_posix(),
                "-I",
                "-B",
                runner_path.as_posix(),
                "--live-launch",
                path.as_posix(),
            ],
            "live_authorization_validator_argv": [
                interpreter_path.as_posix(),
                "-I",
                "-B",
                validator_path.as_posix(),
                "--validate-live-authorization",
                "--expected-identity-stdin",
                path.as_posix(),
            ],
            "live_capture_validator_argv": [
                interpreter_path.as_posix(),
                "-I",
                "-B",
                validator_path.as_posix(),
                "--validate-live-capture",
                "--expected-identity-stdin",
                staging_root.as_posix(),
            ],
            "run_id": "a" * 32,
            "staging_root": staging_root.as_posix(),
        },
        "runner": {
            "path": runner_path.as_posix(),
            "sha256": _sha(runner_path.read_bytes()),
        },
        "validator": {
            "path": validator_path.as_posix(),
            "sha256": _sha(validator_path.read_bytes()),
        },
        "projector": {
            "path": projector_path.as_posix(),
            "sha256": _sha(projector_path.read_bytes()),
        },
        "interpreter": {
            "bytecode_flag": "-B",
            "bytecode_write_control": "python_flag_-B",
            "isolated_flag": "-I",
            "path": interpreter_path.as_posix(),
            "python_environment_names": [],
            "resolved_path": interpreter_path.as_posix(),
            "sha256": _sha(interpreter_path.read_bytes()),
        },
        "preflight_identity_sha256": "7" * 64,
        "discovery": discovery,
        "launch_limit": 1,
        "expected_call_counts": counts,
        "tracked_writes_authorized": False,
        "write_contract": {
            "consumed_marker_path": marker_path.as_posix(),
            "failure_authorized_directory_metadata_paths": [control_root.as_posix()],
            "failure_authorized_exact_paths": [marker_path.as_posix(), failure_path.as_posix()],
            "failure_authorized_recursive_write_roots": [candidate_root.as_posix()],
            "failure_summary_path": failure_path.as_posix(),
            "pre_staging_manifest": pre_staging_object["entries"],
            "pre_staging_manifest_sha256": pre_staging_sha,
            "self_bound_excluded_paths": sorted(
                (path.as_posix(), failure_path.as_posix()),
                key=lambda value: value.encode("utf-8"),
            ),
            "self_bound_excluded_recursive_roots": [candidate_root.as_posix()],
            "source_root_writes_authorized": False,
            "success_authorized_directory_metadata_paths": [control_root.as_posix()],
            "success_authorized_exact_paths": [marker_path.as_posix()],
            "success_authorized_recursive_write_roots": [candidate_root.as_posix()],
        },
    }
    _write_json(path, authorization)
    expected = Ops01RLiveAuthorizationExpectedIdentity(
        authorization_sha256=_sha(_canon(authorization)),
        discovery_identity_sha256=discovery["discovery_identity_sha256"],
        interpreter_sha256=authorization["interpreter"]["sha256"],
        live_pre_staging_manifest_sha256=pre_staging_sha,
        literal_staging_root=authorization["run"]["staging_root"],
        preflight_identity_sha256="7" * 64,
        projector_sha256=authorization["projector"]["sha256"],
        railway_executable_sha256="9" * 64,
        runner_sha256=authorization["runner"]["sha256"],
        source_commit="1" * 40,
        source_manifest_sha256=source_manifest,
        validator_sha256=authorization["validator"]["sha256"],
    )
    return path, authorization, expected


def test_live_authorization_requires_canonical_schema_closed_bytes(tmp_path):
    path, authorization, expected = _live_authorization_pair(tmp_path)
    assert validate_ops01r_live_authorization(path, expected=expected).valid

    path.write_text(json.dumps(authorization, indent=2) + "\n")
    result = validate_ops01r_live_authorization(path, expected=expected)
    assert not result.valid
    assert "OPS01_AUTH_BYTES_NONCANONICAL" in result.errors

    authorization["schema"] = "wrong.schema"
    _write_json(path, authorization)
    result = validate_ops01r_live_authorization(
        path,
        expected=replace(
            expected,
            authorization_sha256=_sha(_canon(authorization)),
        ),
    )
    assert not result.valid
    assert "OPS01_AUTH_SCHEMA_INVALID" in result.errors


@pytest.mark.parametrize("tampered_field", ["interpreter", "runner"])
def test_live_authorization_rejects_unbound_child_vector(tmp_path, tampered_field):
    path, authorization, expected = _live_authorization_pair(tmp_path)
    index = 0 if tampered_field == "interpreter" else 3
    authorization["run"]["child_argv"][index] += ".tampered"
    _write_json(path, authorization)

    result = validate_ops01r_live_authorization(
        path,
        expected=replace(
            expected,
            authorization_sha256=_sha(_canon(authorization)),
        ),
    )

    assert not result.valid
    assert "OPS01_AUTH_EXPECTED_IDENTITY_MISMATCH" in result.errors


def _stage_runner_source(tmp_path: Path) -> Path:
    source = tmp_path / "source"
    required_files = (
        "engine/db/ddl_identity_projection.py",
        "scripts/db/capture_epic011_posture.py",
        "scripts/ops/hde_epic038_ops01r.py",
        "tools/evidence/hde_epic038_ops01_v5.py",
        "tools/evidence/retained_evidence_safety.py",
    )
    for relative in required_files:
        destination = source / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(relative, destination)
    return source


def test_runner_preflight_round_trips_through_independent_validator(tmp_path):
    source = _stage_runner_source(tmp_path)
    railway_bin = tmp_path / "bin"
    railway_bin.mkdir()
    railway = railway_bin / "railway"
    railway.write_text("#!/bin/sh\nexit 0\n")
    railway.chmod(0o755)
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }
    environment["PATH"] = railway_bin.as_posix()
    process = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            str(source / "scripts/ops/hde_epic038_ops01r.py"),
            "--preflight",
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=True,
    )
    path = Path(process.stdout.strip())
    record = json.loads(path.read_text())
    expected = Ops01RPreflightExpectedIdentity(
        source_commit=record["source"]["commit"],
        source_manifest_sha256=record["source"]["source_manifest_sha256"],
        pre_staging_manifest_sha256=record["source_write_validation"][
            "pre_staging_manifest_sha256"
        ],
        literal_staging_root=record["run"]["staging_root"],
        runner_sha256=record["components"]["runner"]["sha256"],
        validator_sha256=record["components"]["validator"]["sha256"],
        projector_sha256=record["components"]["projector"]["sha256"],
        interpreter_sha256=record["interpreter"]["sha256"],
        railway_executable_sha256=record["railway_executable"]["sha256"],
        preflight_identity_sha256=record["preflight_identity_sha256"],
    )
    assert validate_ops01r_preflight(path, expected=expected).valid


def test_preflight_binds_components_and_modules_to_materialized_source(
    tmp_path, monkeypatch
):
    import scripts.ops.hde_epic038_ops01r as runner

    for name in tuple(os.environ):
        if name.casefold().startswith("python"):
            monkeypatch.delenv(name)

    run_id = hashlib.sha256(tmp_path.as_posix().encode()).hexdigest()[:32]
    staging_root = Path("/tmp/hde-epic038-ops01r") / run_id
    shutil.rmtree(staging_root, ignore_errors=True)
    files = {
        "engine/db/ddl_identity_projection.py": Path("engine/db/ddl_identity_projection.py").read_bytes(),
        "scripts/db/capture_epic011_posture.py": Path("scripts/db/capture_epic011_posture.py").read_bytes(),
        "scripts/ops/hde_epic038_ops01r.py": Path("scripts/ops/hde_epic038_ops01r.py").read_bytes(),
        "tools/evidence/hde_epic038_ops01_v5.py": Path("tools/evidence/hde_epic038_ops01_v5.py").read_bytes(),
    }

    def materialize(source_root, commit):
        for relative, content in files.items():
            path = source_root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

    railway_bin = tmp_path / "bin"
    railway_bin.mkdir()
    railway = railway_bin / "railway"
    railway.write_text("#!/bin/sh\necho railway 4.0.0\n")
    railway.chmod(0o755)
    monkeypatch.setenv("PATH", railway_bin.as_posix())

    monkeypatch.setattr(runner, "materialize_source_worktree", materialize)
    monkeypatch.setattr(runner, "_git_commit", lambda root: "1" * 40)
    try:
        assert runner.preflight(run_id=run_id) == 0
        record = json.loads((staging_root / "control/preflight.json").read_text())
        source_root = staging_root / "source"
        for name, relative in (
            ("runner", "scripts/ops/hde_epic038_ops01r.py"),
            ("validator", "tools/evidence/hde_epic038_ops01_v5.py"),
            ("projector", "engine/db/ddl_identity_projection.py"),
        ):
            identity = record["components"][name]
            expected_path = (source_root / relative).as_posix()
            assert identity["lexical_path"] == expected_path
            assert identity["resolved_path"] == expected_path
            assert identity["sha256"] == _sha(files[relative])

        expected_origins = {
            "engine.db.ddl_identity_projection": "engine/db/ddl_identity_projection.py",
            "scripts.db.capture_epic011_posture": "scripts/db/capture_epic011_posture.py",
            "scripts.ops.hde_epic038_ops01r": "scripts/ops/hde_epic038_ops01r.py",
            "tools.evidence.hde_epic038_ops01_v5": "tools/evidence/hde_epic038_ops01_v5.py",
        }
        for origin in record["module_origins"]:
            relative = expected_origins[origin["module"]]
            expected_path = (source_root / relative).as_posix()
            assert origin["lexical_origin"] == expected_path
            assert origin["resolved_origin"] == expected_path
            assert origin["sha256"] == _sha(files[relative])
        assert record["interpreter"]["preflight_argv"][3] == (
            source_root / "scripts/ops/hde_epic038_ops01r.py"
        ).as_posix()
        assert record["interpreter"]["preflight_validator_argv"][3] == (
            source_root / "tools/evidence/hde_epic038_ops01_v5.py"
        ).as_posix()
        assert record["railway_executable"]["lexical_path"] == railway.as_posix()
        assert record["railway_executable"]["resolved_path"] == railway.as_posix()
        assert record["railway_executable"]["sha256"] == _sha(railway.read_bytes())
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)


def test_runner_preflight_rejects_python_environment(tmp_path):
    source = _stage_runner_source(tmp_path)
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.casefold().startswith("python")
    }
    environment["PYTHONPATH"] = "/tmp/unauthorized-python-path"

    process = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            str(source / "scripts/ops/hde_epic038_ops01r.py"),
            "--preflight",
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
    )

    assert process.returncode != 0
    assert "OPS01_V5_PYTHON_ENVIRONMENT_INVALID" in process.stderr


def test_runner_rejects_invalid_discovery_authorization_before_subprocess(tmp_path, monkeypatch):
    import scripts.ops.hde_epic038_ops01r as runner

    authorization = tmp_path / "discovery_authorization.json"
    _write_json(authorization, {"schema": "invalid"})
    calls = []
    monkeypatch.setattr(
        runner.subprocess,
        "run",
        lambda *a, **k: calls.append((a, k))
        or pytest.fail("external subprocess invoked"),
    )

    with pytest.raises(SystemExit, match="OPS01R_DISCOVERY_AUTH_INVALID"):
        runner.discovery(
            authorization,
            expected=Ops01RDiscoveryAuthorizationExpectedIdentity(*(["x"] * 8)),
        )
    assert calls == []


def test_runner_rejects_invalid_live_authorization_before_consumption_or_subprocess(
    tmp_path, monkeypatch
):
    import scripts.ops.hde_epic038_ops01r as runner

    control = tmp_path / "control"
    control.mkdir()
    authorization = control / "live_authorization.json"
    _write_json(authorization, {"schema": "invalid"})
    calls = []
    monkeypatch.setattr(
        runner.subprocess,
        "run",
        lambda *a, **k: calls.append((a, k))
        or pytest.fail("external subprocess invoked"),
    )

    with pytest.raises(SystemExit, match="OPS01R_LIVE_AUTH_INVALID"):
        runner.live_launch(
            authorization,
            expected=Ops01RLiveAuthorizationExpectedIdentity(*(["x"] * 12)),
        )
    assert calls == []
    assert not (control / "live_authority_consumed.json").exists()


def test_live_launch_uses_discovery_bound_railway_prefix_and_live_child_suffix(
    tmp_path, monkeypatch
):
    import scripts.ops.hde_epic038_ops01r as runner

    path, authorization, expected = _live_authorization_pair(tmp_path)
    child = authorization["run"]["child_argv"]
    prefix = authorization["discovery"]["run_contract"]["argv_prefix"]
    calls = []

    def fake_run(argv, **kwargs):
        calls.append((tuple(argv), kwargs))
        (Path(authorization["run"]["candidate_root"]) / "produced.txt").write_text(
            "produced\n"
        )
        return subprocess.CompletedProcess(argv, 0, "", "")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)

    assert runner.live_launch(path, expected=expected) == 0
    assert len(calls) == 1
    assert calls[0][0] == tuple(prefix + child)
    assert calls[0][1]["shell"] is False
    for name, value in {
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "ALLOW_DB_WRITE": "0",
        "APP_ENV": "dev",
    }.items():
        assert calls[0][1]["env"][name] == value
    assert not any(
        name.casefold().startswith("python") for name in calls[0][1]["env"]
    )
    marker = Path(authorization["write_contract"]["consumed_marker_path"])
    assert marker.exists()
    marker_payload = json.loads(marker.read_text())
    assert marker_payload["authorization_sha256"] == expected.authorization_sha256
    assert marker_payload["run_id"] == authorization["run"]["run_id"]


@pytest.mark.parametrize("tampered_index", [0, 3, 4])
def test_live_launch_rejects_unbound_child_vector_before_consumption(
    tmp_path, monkeypatch, tampered_index
):
    import scripts.ops.hde_epic038_ops01r as runner

    path, authorization, expected = _live_authorization_pair(tmp_path)
    authorization["run"]["child_argv"][tampered_index] += ".tampered"
    authorization["discovery"]["run_contract"] = {
        "argv_prefix": ["railway", "run", "--"],
        "child_argv_start_index": 3,
    }
    _write_json(path, authorization)
    expected = replace(
        expected,
        authorization_sha256=_sha(_canon(authorization)),
    )
    calls = []
    monkeypatch.setattr(
        runner.subprocess,
        "run",
        lambda *a, **k: calls.append((a, k))
        or pytest.fail("external subprocess invoked"),
    )

    with pytest.raises(SystemExit, match="OPS01R_LIVE_AUTH_INVALID"):
        runner.live_launch(path, expected=expected)
    assert calls == []
    assert not Path(
        authorization["write_contract"]["consumed_marker_path"]
    ).exists()


def test_live_child_executes_authorized_capture_pipeline(tmp_path, monkeypatch):
    import scripts.ops.hde_epic038_ops01r as runner

    authorization = {
        "expected_call_counts": dict(runner.EXPECTED_CALL_COUNTS),
        "source": {"root": (tmp_path / "source").as_posix()},
        "run": {"staging_root": tmp_path.as_posix()},
    }
    events = []

    monkeypatch.setattr(
        runner,
        "_live_runtime_authorization",
        lambda: (
            tmp_path / "control/live_authorization.json",
            authorization,
            "a" * 64,
        ),
    )
    monkeypatch.setattr(
        runner,
        "_close_live_environment",
        lambda value: events.append("environment") or {},
    )

    def fake_capture(value, budget):
        events.append("capture")
        budget.actual = dict(budget.expected)
        return {"observed": True}

    monkeypatch.setattr(runner, "_capture_live_observations", fake_capture)
    monkeypatch.setattr(
        runner,
        "_live_source_write_validation",
        lambda *args: events.append("source-write") or {"status": "PASS"},
    )
    monkeypatch.setattr(
        runner,
        "_write_candidate",
        lambda *args: events.append("candidate"),
    )

    assert runner.main(["--live-child"]) == 0
    assert events == ["environment", "capture", "source-write", "candidate"]


def _install_bridge_response_stub(monkeypatch):
    providers_module = type(sys)("engine.db.providers")
    bridge_module = type(sys)("engine.db.providers.bridge_provider")

    class BridgeResponse:
        def __init__(self, *, status, body, headers):
            self.status = status
            self.body = body
            self.headers = headers

    bridge_module.BridgeResponse = BridgeResponse
    monkeypatch.setitem(sys.modules, "engine.db.providers", providers_module)
    monkeypatch.setitem(
        sys.modules, "engine.db.providers.bridge_provider", bridge_module
    )


def test_bridge_request_allows_only_governed_read_only_gets(monkeypatch):
    import scripts.ops.hde_epic038_ops01r as runner

    _install_bridge_response_stub(monkeypatch)
    calls = []

    class Response:
        status = 200
        headers = {}

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def getcode(self):
            return self.status

        def read(self):
            return b'{"status":"ok"}'

    class Opener:
        def open(self, request, timeout):
            calls.append((request.full_url, request.method, request.data, timeout))
            return Response()

    monkeypatch.setattr(
        runner.urllib.request, "build_opener", lambda *handlers: Opener()
    )
    budget = runner._CallBudget.from_authorization(
        {"expected_call_counts": dict(runner.EXPECTED_CALL_COUNTS)}
    )
    request = runner._bridge_request(budget)

    for path in (
        "/health",
        "/introspect/grants",
        "/introspect/search_path",
        "/introspect/fingerprint",
    ):
        response = request(f"https://bridge.invalid{path}", "GET", None, {})
        assert response.status == 200

    assert [entry[0] for entry in calls] == [
        "https://bridge.invalid/health",
        "https://bridge.invalid/introspect/grants",
        "https://bridge.invalid/introspect/search_path",
        "https://bridge.invalid/introspect/fingerprint",
    ]


@pytest.mark.parametrize(
    "url",
    [
        "https://bridge.invalid/introspect/version",
        "https://bridge.invalid/unlisted/health",
    ],
)
def test_bridge_request_rejects_unlisted_gets_before_io(monkeypatch, url):
    import scripts.ops.hde_epic038_ops01r as runner

    _install_bridge_response_stub(monkeypatch)

    class Opener:
        def open(self, *args, **kwargs):
            pytest.fail("external bridge I/O attempted")

    monkeypatch.setattr(
        runner.urllib.request,
        "build_opener",
        lambda *handlers: Opener(),
    )
    budget = runner._CallBudget.from_authorization(
        {"expected_call_counts": dict(runner.EXPECTED_CALL_COUNTS)}
    )
    request = runner._bridge_request(budget)

    with pytest.raises(RuntimeError, match="OPS01R_LIVE_BRIDGE_REQUEST_INVALID"):
        request(url, "GET", None, {})


def test_live_child_validates_target_before_reading_db_endpoints(monkeypatch):
    import scripts.ops.hde_epic038_ops01r as runner

    class TrackingEnvironment(dict):
        def __init__(self, values):
            super().__init__(values)
            self.value_reads = []

        def get(self, name, default=None):
            self.value_reads.append(name)
            return super().get(name, default)

    environment = TrackingEnvironment(
        {
            "ALLOW_DB_WRITE": "0",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "DATABASE_URL": "postgresql://credential",
            "DB_BRIDGE_URL": "https://bridge.invalid",
            "LANG": "C",
            "LC_ALL": "C",
            "RAILWAY_SERVICE_ID": "wrong-service",
            "SAFE_MODE": "1",
            "TZ": "UTC",
        }
    )
    contract = [
        {"name": name, "source": source, "value_policy": policy}
        for name, source, policy in (
            ("DATABASE_URL", "railway_service", "presence_only"),
            ("DB_BRIDGE_URL", "railway_service", "presence_only"),
            ("ALLOW_DB_WRITE", "runner", "exact:0"),
            ("ALLOW_NETWORK", "runner", "exact:0"),
            ("APP_ENV", "runner", "exact:dev"),
            ("LANG", "runner", "exact:C"),
            ("LC_ALL", "runner", "exact:C"),
            (
                "RAILWAY_SERVICE_ID",
                "railway_target_identity",
                "exact:wrong-service",
            ),
            ("SAFE_MODE", "runner", "exact:1"),
            ("TZ", "runner", "exact:UTC"),
        )
    ]
    authorization = {
        "discovery": {
            "identity_contract": [
                {
                    "expected_value": "authorized-service",
                    "field_name": "RAILWAY_SERVICE_ID",
                    "target_dimension": "service",
                    "value_kind": "target_id",
                }
            ],
            "run_contract": {"child_environment_contract": contract},
        }
    }
    monkeypatch.setattr(runner.os, "environ", environment)

    with pytest.raises(SystemExit, match="OPS01R_LIVE_TARGET_IDENTITY_INVALID"):
        runner._close_live_environment(authorization)

    assert "DATABASE_URL" not in environment.value_reads
    assert "DB_BRIDGE_URL" not in environment.value_reads
