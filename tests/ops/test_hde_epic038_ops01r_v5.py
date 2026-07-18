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

from tools.evidence.hde_epic038_ops01_v5 import (
    Ops01RDiscoveryAuthorizationExpectedIdentity,
    Ops01RPreflightExpectedIdentity,
    Ops01V5ExpectedIdentity,
    V5_PRIMARY_FILES,
    validate_ops01_v5_package,
    validate_ops01r_discovery_dispatch,
    validate_ops01r_discovery_result,
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


def test_runner_dormant_modes_do_not_run_external_ops():
    process = subprocess.run(
        [sys.executable, "scripts/ops/hde_epic038_ops01r.py", "--live-child"],
        capture_output=True,
        text=True,
    )
    assert process.returncode != 0
    assert "dormant" in process.stderr


def _candidate(tmp_path: Path) -> tuple[Path, Ops01V5ExpectedIdentity]:
    root = tmp_path / "candidate"
    root.mkdir()
    source_commit = "1" * 40
    source_manifest = "2" * 64
    pre_staging = "3" * 64
    post_staging = "4" * 64
    preflight_identity = "5" * 64
    runner_sha = "6" * 64
    validator_sha = "7" * 64
    projector_sha = "8" * 64
    staging_root = "/tmp/hde-epic038-ops01r/" + "a" * 32
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
    discovery = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_authorization_sha256": "9" * 64,
    }
    discovery["discovery_identity_sha256"] = _sha(_canon(discovery))
    authorization = {
        "schema": "hde_epic038.ops01r.authorization.v1",
        "source": {
            "commit": source_commit,
            "source_manifest_sha256": source_manifest,
        },
        "run": {"staging_root": staging_root},
        "runner": {"sha256": runner_sha},
        "validator": {"sha256": validator_sha},
        "projector": {"sha256": projector_sha},
        "preflight_identity_sha256": preflight_identity,
        "discovery": discovery,
        "expected_call_counts": counts,
        "write_contract": {"pre_staging_manifest_sha256": pre_staging},
    }
    commands = b"read-only observation\n"
    (root / "commands.txt").write_bytes(commands)
    (root / "stdout.log").write_text("PASS\n")
    (root / "stderr.log").write_text("none\n")
    (root / "exit_code.txt").write_text("0\n")
    for name in (
        "env_presence.json",
        "db_posture_summary.json",
        "bridge_consistency.result.json",
        "nonclaims.json",
    ):
        _write_json(root / name, {})
    _write_json(
        root / "provider_parity.proof.json",
        {
            "schema": "hde_epic038.ops01.provider_parity.v5",
            "status": "PASS",
            "selected": "psycopg",
            "environment": "dev",
            "rails_open": False,
            "full_ddl_semantic_parity_claimed": False,
        },
    )
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
    ledger = "\n".join(
        f"{_sha((root / name).read_bytes())}  {name}"
        for name in sorted(V5_PRIMARY_FILES)
        if name != "checksums.sha256"
    ) + "\n"
    (root / "checksums.sha256").write_text(ledger)
    expected = Ops01V5ExpectedIdentity(
        authorization_sha256=summary["authorization_sha256"],
        candidate_ledger_sha256=_sha(ledger.encode("ascii")),
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


def _discovery_pair(
    tmp_path: Path,
) -> tuple[Path, Path, Ops01RDiscoveryAuthorizationExpectedIdentity]:
    staging_root = tmp_path / ("b" * 32)
    control = staging_root / "control"
    control.mkdir(parents=True)
    source_manifest = "1" * 64
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
        "railway_cli": {"sha256": "5" * 64},
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
    manifest: list[object] = []
    result = {
        "schema": "hde_epic038.ops01r.discovery.v1",
        "status": "PASS",
        "discovery_authorization_sha256": authorization[
            "discovery_authorization_sha256"
        ],
        "command_manifest": manifest,
        "command_manifest_sha256": _sha(_canon(manifest)),
        "railway_cli": {"sha256": "5" * 64},
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
    source_manifest = "1" * 64
    record = {
        "schema": "hde_epic038.ops01r.preflight.v1",
        "status": "PASS",
        "run": {"staging_root": "/tmp/hde-epic038-ops01r/" + "a" * 32},
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
            "pre_staging_manifest_sha256": "8" * 64,
        },
    }
    record["preflight_identity_sha256"] = _sha(_canon(record))
    path = tmp_path / "preflight.json"
    _write_json(path, record)
    expected = Ops01RPreflightExpectedIdentity(
        source_commit="2" * 40,
        source_manifest_sha256=source_manifest,
        pre_staging_manifest_sha256="8" * 64,
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
