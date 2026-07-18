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


def test_runner_dormant_modes_do_not_run_external_ops():
    process = subprocess.run(
        [sys.executable, "scripts/ops/hde_epic038_ops01r.py", "--live-child"],
        capture_output=True,
        text=True,
    )
    assert process.returncode != 0
    assert "dormant" in process.stderr


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
    staging_root = literal_staging_root or (
        "/tmp/hde-epic038-ops01r/" + "a" * 32
    )
    if counts is None:
        counts = {
            "bodygraph_reads": 2,
            "bridge_http_requests": 0,
            "bridge_provider_selections": 1,
            "direct_connection_attempts": 0,
            "direct_provider_selections": 1,
            "direct_sql_statements": 0,
            "fallbacks": 0,
            "logical_observations": 10,
            "retries": 0,
            "vendor_requests": 0,
        }
    source_root = f"{staging_root}/source"
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
        "run": {"child_argv": child_argv, "staging_root": staging_root},
        "runner": {"path": runner_path, "sha256": runner_sha},
        "validator": {"path": validator_path, "sha256": validator_sha},
        "projector": {"path": projector_path, "sha256": projector_sha},
        "interpreter": {"path": interpreter_path},
        "preflight_identity_sha256": preflight_identity,
        "discovery": discovery,
        "expected_call_counts": counts,
        "write_contract": {"pre_staging_manifest_sha256": pre_staging},
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
    checker_sha = "b" * 64
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
    summary = {
        "schema": "hde_epic038.ops01.result_summary.v4",
        "full_ddl_semantic_parity_claimed": False,
        "authorization": authorization,
        "authorization_sha256": _sha(_canon(authorization)),
        "discovery_identity_sha256": discovery["discovery_identity_sha256"],
        "literal_staging_root": staging_root,
        "preflight_identity_sha256": preflight_identity,
        "runner_sha256": runner_sha,
        "repository": {"head": source_commit},
        "expected_call_counts": counts,
        "actual_call_counts": counts,
        "execution": {
            "commands_sha256": _sha(commands),
            "source_write_validation": {
                "pre_source_manifest_sha256": source_manifest,
                "post_source_manifest_sha256": source_manifest,
                "pre_staging_manifest_sha256": pre_staging,
                "post_staging_manifest_sha256": post_staging,
            },
        },
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
        "bridge_http_requests": 0,
        "bridge_provider_selections": 1,
        "direct_connection_attempts": 0,
        "direct_provider_selections": 1,
        "direct_sql_statements": 0,
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
        "staging_root": staging_root.as_posix(),
    }
    authorization["write_contract"].update(
        {
            "pre_staging_manifest_sha256": staging_manifest_sha256,
            "failure_summary_path": failure_summary_path.as_posix(),
            "self_bound_excluded_paths": sorted(
                (
                    authorization_path.as_posix(),
                    failure_summary_path.as_posix(),
                ),
                key=lambda value: value.encode("utf-8"),
            ),
            "self_bound_excluded_recursive_roots": [candidate_root.as_posix()],
        }
    )
    source_write.update(
        {
            "post_source_manifest_sha256": source_manifest_sha256,
            "post_staging_manifest_sha256": staging_manifest_sha256,
            "pre_source_manifest_sha256": source_manifest_sha256,
            "pre_staging_manifest": staging_manifest["entries"],
            "pre_staging_manifest_sha256": staging_manifest_sha256,
            "self_bound_excluded_paths": authorization["write_contract"][
                "self_bound_excluded_paths"
            ],
            "self_bound_excluded_recursive_roots": [candidate_root.as_posix()],
            "source_root": source_root.as_posix(),
        }
    )
    summary["authorization_sha256"] = _sha(_canon(authorization))
    summary["literal_staging_root"] = staging_root.as_posix()
    _write_json(authorization_path, authorization)
    _write_json(summary_path, summary)
    ledger = _rewrite_candidate_ledger(candidate_root)
    expected = replace(
        expected,
        authorization_sha256=summary["authorization_sha256"],
        candidate_ledger_sha256=_sha(ledger),
        literal_staging_root=staging_root.as_posix(),
        live_post_staging_manifest_sha256=staging_manifest_sha256,
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


def test_live_capture_revalidates_excluded_authorization(tmp_path):
    staging_root, _, expected = _live_capture(tmp_path)
    authorization_path = staging_root / "control" / "live_authorization.json"
    authorization_path.write_bytes(authorization_path.read_bytes() + b" ")

    result = validate_ops01r_live_capture(staging_root, expected=expected)

    assert not result.valid
    assert "OPS01_V5_LIVE_CAPTURE_IDENTITY_MISMATCH" in result.errors


def _discovery_pair(
    tmp_path: Path,
) -> tuple[Path, Path, Ops01RDiscoveryAuthorizationExpectedIdentity]:
    staging_root = tmp_path / ("b" * 32)
    control = staging_root / "control"
    control.mkdir(parents=True)
    source_manifest = "1" * 64
    target_probe_argv = [
        "/usr/bin/python3",
        "-I",
        "-B",
        (staging_root / "source/scripts/ops/hde_epic038_ops01r.py").as_posix(),
        "--target-identity-probe",
    ]
    stage_commands = {
        "cli_version": ["--version"],
        "cli_help": ["help"],
        "project_inventory": ["project", "list"],
        "environment_inventory": ["environment", "list"],
        "service_inventory": ["service", "list"],
    }
    policy_stages = []
    for ordinal, stage in enumerate(DISCOVERY_STAGES, start=1):
        descriptors = (
            [{"kind": "literal", "value": token} for token in stage_commands[stage]]
            if stage != "target_identity_probe"
            else [
                {"kind": "literal", "value": "run"},
                {"kind": "literal", "value": "--"},
                {"kind": "python_child"},
            ]
        )
        policy_stages.append(
            {
                "stage": stage,
                "templates": [
                    {
                        "argv": descriptors,
                        "required_help_tokens": [],
                        "template_id": f"{stage}-v1",
                        "version_regex": "",
                    }
                ],
            }
        )
    authorization = {
        "schema": "hde_epic038.ops01r.discovery_authorization.v1",
        "source": {
            "commit": "2" * 40,
            "root": (staging_root / "source").as_posix(),
            "source_manifest_sha256": source_manifest,
        },
        "discovery_entry_point": {"sha256": "3" * 64},
        "preflight": {
            "preflight_identity_sha256": "4" * 64,
            "source_manifest_sha256": source_manifest,
        },
        "railway_cli": {"lexical_path": "railway", "sha256": "5" * 64},
        "policy": {
            "python_execution": {"target_probe_argv": target_probe_argv},
            "stages": policy_stages,
        },
        "output_contract": {"path": (control / "discovery.json").as_posix()},
        "write_contract": {"pre_staging_manifest_sha256": "6" * 64},
    }
    authorization["discovery_authorization_sha256"] = _sha(_canon(authorization))
    authorization_path = control / "discovery_authorization.json"
    _write_json(authorization_path, authorization)
    expected = Ops01RDiscoveryAuthorizationExpectedIdentity(
        discovery_authorization_sha256=authorization[
            "discovery_authorization_sha256"
        ],
        discovery_entry_point_sha256="3" * 64,
        literal_staging_root=staging_root.as_posix(),
        pre_staging_manifest_sha256="6" * 64,
        preflight_identity_sha256="4" * 64,
        railway_executable_sha256="5" * 64,
        source_commit="2" * 40,
        source_manifest_sha256=source_manifest,
    )
    manifest: list[object] = [
        ["railway", "--version"],
        ["railway", "help"],
        ["railway", "project", "list"],
        ["railway", "environment", "list"],
        ["railway", "service", "list"],
        ["railway", "run", "--", *target_probe_argv],
    ]
    result = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_authorization_sha256": authorization[
            "discovery_authorization_sha256"
        ],
        "command_manifest": manifest,
        "command_manifest_sha256": _sha(_canon(manifest)),
        "railway_cli": {"sha256": "5" * 64},
        "target": {
            "project_id": "project-id",
            "project_name": "ample-illumination",
            "environment_id": "environment-id",
            "environment_name": "production",
            "service_id": "service-id",
            "service_name": "glow-hdengine-v2",
        },
        "source_write_validation": {
            "pre_source_manifest_sha256": source_manifest,
            "post_source_manifest_sha256": source_manifest,
            "pre_staging_manifest_sha256": "6" * 64,
        },
    }
    result["discovery_identity_sha256"] = _sha(_canon(result))
    result_path = control / "discovery.json"
    _write_json(result_path, result)
    return result_path, authorization_path, expected


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


def test_discovery_result_replays_command_policy(tmp_path):
    result_path, authorization_path, expected = _discovery_pair(tmp_path)
    payload = json.loads(result_path.read_text())
    payload["command_manifest"] = [["railway", "deploy"]]
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
    assert "DISCOVERY_RESULT_ARGV_MISMATCH" in result.errors


def test_discovery_dispatch_requires_exact_authorized_stage_argv(tmp_path):
    _, authorization_path, _ = _discovery_pair(tmp_path)
    assert validate_ops01r_discovery_dispatch(
        authorization_path,
        stage="cli_version",
        prior_results={},
        rendered_argv=("railway", "--version"),
    ).valid

    result = validate_ops01r_discovery_dispatch(
        authorization_path,
        stage="cli_version",
        prior_results={},
        rendered_argv=("railway", "run", "python", "-c", "print('unsafe')"),
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


def test_preflight_uses_canonical_nested_identity_fields(tmp_path):
    staging_root = tmp_path / "run"
    source_root = staging_root / "source"
    control_root = staging_root / "control"
    working_directory = staging_root / "preflight-work"
    source_root.mkdir(parents=True)
    control_root.mkdir()
    working_directory.mkdir()
    (source_root / "tracked.py").write_text("VALUE = 1\n")
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
    record = {
        "schema": "hde_epic038.ops01r.preflight.v1",
        "status": "PASS",
        "actual_external_io_counts": {
            name: 0 for name in PREFLIGHT_ZERO_IO_FIELDS
        },
        "expected_call_counts": {
            "bodygraph_reads": 2,
            "bridge_http_requests": 0,
            "bridge_provider_selections": 1,
            "direct_connection_attempts": 0,
            "direct_provider_selections": 1,
            "direct_sql_statements": 0,
            "fallbacks": 0,
            "logical_observations": 10,
            "retries": 0,
            "vendor_requests": 0,
        },
        "nonclaims": list(PREFLIGHT_NONCLAIMS),
        "run": {
            "control_root": control_root.as_posix(),
            "preflight_path": path.as_posix(),
            "source_root": source_root.as_posix(),
            "staging_root": staging_root.as_posix(),
            "working_directory": working_directory.as_posix(),
        },
        "source": {
            "commit": "2" * 40,
            "source_manifest_sha256": source_manifest,
        },
        "components": {
            "runner": {"sha256": "3" * 64},
            "validator": {"sha256": "4" * 64},
            "projector": {"sha256": "5" * 64},
        },
        "interpreter": {"sha256": "6" * 64},
        "railway_executable": {"sha256": "7" * 64},
        "source_write_validation": {
            "pre_source_manifest_sha256": source_manifest,
            "post_source_manifest_sha256": source_manifest,
            "pre_staging_manifest": pre_staging_object["entries"],
            "pre_staging_manifest_sha256": pre_staging,
            "post_staging_manifest_sha256": _sha(_canon(post_staging_object)),
            "observed_staging_changes": _manifest_delta(
                pre_staging_object["entries"], post_staging_object["entries"]
            ),
        },
    }
    record["preflight_identity_sha256"] = _sha(_canon(record))
    _write_json(path, record)
    expected = Ops01RPreflightExpectedIdentity(
        source_commit="2" * 40,
        source_manifest_sha256=source_manifest,
        pre_staging_manifest_sha256=pre_staging,
        literal_staging_root=record["run"]["staging_root"],
        runner_sha256="3" * 64,
        validator_sha256="4" * 64,
        projector_sha256="5" * 64,
        interpreter_sha256="6" * 64,
        railway_executable_sha256="7" * 64,
        preflight_identity_sha256=record["preflight_identity_sha256"],
    )
    assert validate_ops01r_preflight(path, expected=expected).valid
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
    assert "PREFLIGHT_WRITE_SET_INVALID" in result.errors


def _live_authorization_pair(
    tmp_path: Path,
) -> tuple[Path, dict[str, object], Ops01RLiveAuthorizationExpectedIdentity]:
    counts = {
        "bodygraph_reads": 2,
        "bridge_http_requests": 0,
        "bridge_provider_selections": 1,
        "direct_connection_attempts": 0,
        "direct_provider_selections": 1,
        "direct_sql_statements": 0,
        "fallbacks": 0,
        "logical_observations": 10,
        "retries": 0,
        "vendor_requests": 0,
    }
    authorization: dict[str, object] = {
        "schema": "hde_epic038.ops01r.authorization.v1",
        "source": {
            "commit": "1" * 40,
            "source_manifest_sha256": "2" * 64,
        },
        "run": {"staging_root": "/tmp/hde-epic038-ops01r/" + "a" * 32},
        "runner": {"sha256": "3" * 64},
        "validator": {"sha256": "4" * 64},
        "projector": {"sha256": "5" * 64},
        "interpreter": {"sha256": "6" * 64},
        "preflight_identity_sha256": "7" * 64,
        "discovery": {
            "discovery_identity_sha256": "8" * 64,
            "railway_cli": {"sha256": "9" * 64},
        },
        "launch_limit": 1,
        "expected_call_counts": counts,
        "tracked_writes_authorized": False,
        "write_contract": {"pre_staging_manifest_sha256": "a" * 64},
    }
    path = tmp_path / "live_authorization.json"
    _write_json(path, authorization)
    expected = Ops01RLiveAuthorizationExpectedIdentity(
        authorization_sha256=_sha(_canon(authorization)),
        discovery_identity_sha256="8" * 64,
        interpreter_sha256="6" * 64,
        live_pre_staging_manifest_sha256="a" * 64,
        literal_staging_root=authorization["run"]["staging_root"],
        preflight_identity_sha256="7" * 64,
        projector_sha256="5" * 64,
        railway_executable_sha256="9" * 64,
        runner_sha256="3" * 64,
        source_commit="1" * 40,
        source_manifest_sha256="2" * 64,
        validator_sha256="4" * 64,
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
