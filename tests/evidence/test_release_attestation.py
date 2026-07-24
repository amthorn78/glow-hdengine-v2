from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

import pytest

from tools.evidence import build_release_attestation as builder
from tools.evidence import regenerate_identity_closure as closure
from tools.cli import generate_cli_conformance_artifacts as cli_conformance


def test_output_root_must_be_external_empty_directory(tmp_path):
    source = tmp_path / "source"
    source.mkdir()

    with pytest.raises(
        builder.AttestationBuildError,
        match="output_root_must_be_outside_source",
    ):
        builder._validate_output_root(source / "output", source)

    occupied = tmp_path / "occupied"
    occupied.mkdir()
    (occupied / "existing").write_text("preserve\n", encoding="utf-8")
    with pytest.raises(
        builder.AttestationBuildError,
        match="output_root_not_empty",
    ):
        builder._validate_output_root(occupied, source)
    assert (occupied / "existing").read_text(encoding="utf-8") == "preserve\n"


def test_output_root_refuses_symlink(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    external = tmp_path / "external"
    external.mkdir()
    output = tmp_path / "output-link"
    output.symlink_to(external, target_is_directory=True)

    with pytest.raises(
        builder.AttestationBuildError,
        match="output_root_symlink_refused",
    ):
        builder._validate_output_root(output, source)


def test_child_environment_is_closed_and_drops_sensitive_values(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://secret")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://retired.example")
    monkeypatch.setenv("HD_API_KEY", "secret")

    source = Path("/isolated/source")
    child = builder._clean_child_env(source)

    assert {name: child[name] for name in builder.CLOSED_RAILS} == builder.CLOSED_RAILS
    assert child["HDE_ISOLATED_RELEASE_BUILD"] == "1"
    assert child["HDE_ATTESTATION_BIN"] == str(source)
    assert "PYTHONPATH" not in child
    assert "VIRTUAL_ENV" not in child
    assert "DATABASE_URL" not in child
    assert "DB_BRIDGE_URL" not in child
    assert "HD_API_KEY" not in child


def test_success_transcript_is_names_only_and_runtime_independent(
    tmp_path,
    monkeypatch,
):
    outputs = iter(
        (
            subprocess.CompletedProcess(
                args=[], returncode=0, stdout="25 passed in 0.35s\n", stderr=""
            ),
            subprocess.CompletedProcess(
                args=[], returncode=0, stdout="25 passed in 0.31s\n", stderr=""
            ),
        )
    )
    monkeypatch.setattr(builder.subprocess, "run", lambda *_args, **_kwargs: next(outputs))
    monkeypatch.setattr(builder, "_clean_child_env", lambda _bin=None: {})
    first: list[str] = []
    second: list[str] = []

    bin_dir = tmp_path / "bin"
    builder._run_stage(
        tmp_path,
        "tests",
        ("python", "-m", "pytest"),
        first,
        attestation_bin=bin_dir,
    )
    builder._run_stage(
        tmp_path,
        "tests",
        ("python", "-m", "pytest"),
        second,
        attestation_bin=bin_dir,
    )

    assert first == second
    assert "0.35" not in "\n".join(first)
    assert "0.31" not in "\n".join(second)
    assert "stdout_recorded=false" in first


def test_isolated_console_entrypoint_is_installed_from_tracked_package(
    tmp_path,
    monkeypatch,
):
    package_source = tmp_path / "package-source"
    package_source.mkdir()
    calls: list[list[str]] = []

    def run(argv, **_kwargs):
        command = list(argv)
        calls.append(command)
        if command[1:4] == ["-m", "venv", "--system-site-packages"]:
            scripts = tmp_path / "venv" / ("Scripts" if builder.os.name == "nt" else "bin")
            scripts.mkdir(parents=True)
            python = scripts / ("python.exe" if builder.os.name == "nt" else "python")
            python.write_text("", encoding="utf-8")
        else:
            console = tmp_path / "venv" / (
                "Scripts/hdctl.exe" if builder.os.name == "nt" else "bin/hdctl"
            )
            console.write_text("#!/bin/sh\n", encoding="utf-8")
            console.chmod(0o755)
        return subprocess.CompletedProcess(args=command, returncode=0)

    monkeypatch.setattr(builder.subprocess, "run", run)
    transcript: list[str] = []
    scripts = builder._install_packaged_console_entrypoint(
        package_source,
        tmp_path,
        transcript,
    )

    assert len(calls) == 2
    assert calls[1][-1] == str(package_source)
    assert "--no-index" in calls[1]
    assert "--no-build-isolation" in calls[1]
    assert not (package_source / ".attestation-bin").exists()
    assert (scripts / ("hdctl.exe" if builder.os.name == "nt" else "hdctl")).is_file()
    assert transcript[0] == "stage=install_packaged_console_entrypoint"


def test_console_entrypoint_path_is_platform_correct_and_bin_constrained():
    env = {"HDE_ATTESTATION_BIN": "/isolated/venv/bin"}

    assert cli_conformance._console_entrypoint_path(
        env,
        windows=False,
    ) == Path("/isolated/venv/bin/hdctl")
    assert cli_conformance._console_entrypoint_path(
        env,
        windows=True,
    ) == Path("/isolated/venv/bin/hdctl.exe")


def test_source_tree_digest_is_order_independent_and_names_only():
    records = {
        "b": {"path": "b", "sha256": "b" * 64, "size": 2},
        "a": {"path": "a", "sha256": "a" * 64, "size": 1},
    }
    reverse = dict(reversed(list(records.items())))

    assert builder._source_tree_digest(records) == builder._source_tree_digest(reverse)


def test_tracked_source_inventory_refuses_virtual_environment(monkeypatch):
    monkeypatch.setattr(
        builder,
        "_run_git",
        lambda *_args: subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=b".venv/bin/python\0",
            stderr=b"",
        ),
    )
    with pytest.raises(
        builder.AttestationBuildError,
        match="tracked_source_ephemeral_path",
    ):
        builder._tracked_paths(Path("."))


def test_repository_does_not_track_local_virtual_environment():
    tracked = builder._tracked_paths(Path("."))
    assert not any(path.parts and path.parts[0] == ".venv" for path in tracked)


def test_isolated_write_boundary_allows_only_declared_outputs():
    assert builder._generated_path_allowed("artifacts/math/release_id.txt")
    assert builder._generated_path_allowed(
        "audit/gates/sanity_pipeline/sanity_pipeline.log"
    )
    assert builder._generated_path_allowed("docs/evidence/INDEX.json")
    assert builder._generated_path_allowed(
        "docs/ENDPOINTS_CATALOG.json.path_proof.txt"
    )
    assert builder._generated_path_allowed("docs/ENDPOINTS_CATALOG.json")
    assert not builder._generated_path_allowed("artifacts/unexpected.json")
    assert not builder._generated_path_allowed("audit/gates/unexpected.log")
    assert not builder._generated_path_allowed("docs/evidence/unexpected.json")
    assert not builder._generated_path_allowed("catalog/manifest.json")
    assert not builder._generated_path_allowed("engine/runtime/identity.py")
    assert not builder._generated_path_allowed(
        "audit/ops/hde-epic038/ops-03/result_summary.json"
    )
    assert not builder._generated_path_allowed(
        "artifacts/ops/hde-epic038/ops-03/result_summary.json"
    )
    assert not builder._generated_path_allowed(
        "artifacts/db_bridge/provider_parity.proof.json"
    )
    assert not builder._generated_path_allowed(
        "artifacts/runtime/env_connectivity.nondev_failure.json"
    )


def test_declared_output_roster_is_exact_owned_and_stable():
    assert len(closure.DECLARED_PRODUCER_OUTPUTS) == 101
    assert len(set(closure.DECLARED_PRODUCER_OUTPUTS)) == 101
    assert len(closure.ATTESTATION_PRIMARY_OUTPUTS) == 101
    assert len(closure.ATTESTATION_PATH_PROOF_TARGETS) == 92
    assert len(closure.ATTESTATION_GENERATED_OUTPUTS) == 193
    assert closure.ATTESTATION_GENERATED_OUTPUTS == tuple(
        sorted(set(closure.ATTESTATION_GENERATED_OUTPUTS))
    )
    assert all(step.outputs for step in closure.CLOSURE_STEPS)
    assert set(closure.ATTESTATION_PATH_PROOF_TARGETS).isdisjoint(
        closure.RELEASE_RECOMPUTE_OUTPUTS
    )
    assert set(closure.ATTESTATION_GENERATED_OUTPUTS) == {
        *closure.ATTESTATION_PRIMARY_OUTPUTS,
        *(
            f"{path}.path_proof.txt"
            for path in closure.ATTESTATION_PATH_PROOF_TARGETS
        ),
    }
    forbidden_prefixes = (
        "audit/ops/",
        "artifacts/ops/hde-epic038/ops-03/",
        "artifacts/db_bridge/",
        "schemas/",
    )
    assert not any(
        path.startswith(forbidden_prefixes)
        for path in closure.ATTESTATION_GENERATED_OUTPUTS
    )
    assert builder._DEREFERENCED_EVIDENCE_SYMLINKS == {
        "docs/ENDPOINTS_CATALOG.json"
    }
    assert builder._DEREFERENCED_EVIDENCE_SYMLINKS.issubset(
        closure.ATTESTATION_PRIMARY_OUTPUTS
    )


def test_failure_receipt_is_strict_and_secret_safe(tmp_path):
    exc = builder.AttestationBuildError(
        "isolated_stage_failed",
        stage="closure_fixed_point_check",
        returncode=7,
    )

    builder._write_failure(tmp_path, exc)

    payload = json.loads((tmp_path / "failure.json").read_bytes())
    assert payload == {
        "schema": "hde.release_attestation.failure.v1",
        "code": "isolated_stage_failed",
        "stage": "closure_fixed_point_check",
        "returncode": 7,
        "secret_values_recorded": False,
    }
    payload["unknown"] = True
    with pytest.raises(
        builder.AttestationBuildError,
        match="failure_receipt_contract_invalid",
    ):
        builder._validate_failure_payload(payload)


def test_failed_bundle_cleanup_emits_only_names_only_receipt(tmp_path):
    (tmp_path / "evidence").mkdir()
    (tmp_path / "evidence" / "partial").write_text(
        "Authorization: Bearer should-not-survive\n",
        encoding="utf-8",
    )
    (tmp_path / "build.log").write_text(
        "postgresql://should-not-survive\n",
        encoding="utf-8",
    )

    builder._reset_failed_output(tmp_path)
    builder._write_failure(
        tmp_path,
        builder.AttestationBuildError("isolated_stage_failed", stage="test"),
    )

    assert {path.name for path in tmp_path.iterdir()} == {"failure.json"}
    assert b"Bearer" not in (tmp_path / "failure.json").read_bytes()


def test_tracked_source_copy_rejects_symlink_escape(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()
    outside = tmp_path / "outside"
    outside.write_text("outside\n", encoding="utf-8")
    (source / "escape").symlink_to(outside)

    with pytest.raises(
        builder.AttestationBuildError,
        match="tracked_source_symlink_unsafe",
    ):
        builder._copy_tracked_source(
            source,
            destination,
            (Path("escape"),),
        )


def test_attestation_contract_rejects_unknown_keys_and_identity_mismatch(
    monkeypatch,
):
    record = {
        "path": "artifacts/test/proof.json",
        "sha256": "a" * 64,
        "size": 1,
    }
    transcript = {"path": "build.log", "sha256": "a" * 64, "size": 1}
    payload = {
        "schema": builder.SCHEMA,
        "source_commit": "b" * 40,
        "source_commit_exact": True,
        "source_tree_sha256": "c" * 64,
        "release_id": "d" * 64,
        "manifest_sha256": "d" * 64,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
        "rails": dict(builder.CLOSED_RAILS),
        "files": [record],
        "omitted_files": [],
        "transcript": transcript,
        "nonclaims": [
            "builder_executes_no_ops",
            "no_database_write",
            "no_deployment_or_migration",
            "no_qa_pass_or_acceptance",
            "no_pf09_status_movement",
        ],
    }
    monkeypatch.setattr(builder, "REQUIRED_EVIDENCE", (record["path"],))
    monkeypatch.setattr(builder, "ATTESTATION_GENERATED_OUTPUTS", ())
    builder._validate_payload(payload)

    payload["unknown"] = True
    with pytest.raises(builder.AttestationBuildError, match="attestation_contract_invalid"):
        builder._validate_payload(payload)
    payload.pop("unknown")
    payload["manifest_sha256"] = "e" * 64
    with pytest.raises(builder.AttestationBuildError, match="attestation_contract_invalid"):
        builder._validate_payload(payload)
    payload["manifest_sha256"] = payload["release_id"]
    payload["source_commit_exact"] = False
    with pytest.raises(builder.AttestationBuildError, match="attestation_contract_invalid"):
        builder._validate_payload(payload)


def test_final_attestation_build_refuses_dirty_source(tmp_path, monkeypatch):
    source = tmp_path / "source"
    source.mkdir()
    output = tmp_path / "output"
    monkeypatch.setattr(
        builder,
        "_git_identity",
        lambda _source: ("b" * 40, False),
    )

    with pytest.raises(
        builder.AttestationBuildError,
        match="source_tree_not_clean",
    ):
        builder.build_attestation(output, source=source)

    assert json.loads((output / "failure.json").read_text(encoding="utf-8"))[
        "code"
    ] == "source_tree_not_clean"


def _write_minimal_bundle(tmp_path, monkeypatch):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "x").write_bytes(b"bound\n")
    (tmp_path / "build.log").write_bytes(b"build\n")
    monkeypatch.setattr(builder, "REQUIRED_EVIDENCE", ("x",))
    monkeypatch.setattr(builder, "ATTESTATION_GENERATED_OUTPUTS", ())
    file_row = builder._file_record(evidence, Path("x"))
    transcript_row = builder._file_record(tmp_path, Path("build.log"))
    payload = {
        "schema": builder.SCHEMA,
        "source_commit": "b" * 40,
        "source_commit_exact": True,
        "source_tree_sha256": "c" * 64,
        "release_id": "d" * 64,
        "manifest_sha256": "d" * 64,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
        "rails": dict(builder.CLOSED_RAILS),
        "files": [file_row],
        "omitted_files": [],
        "transcript": transcript_row,
        "nonclaims": [
            "builder_executes_no_ops",
            "no_database_write",
            "no_deployment_or_migration",
            "no_qa_pass_or_acceptance",
            "no_pf09_status_movement",
        ],
    }
    raw = builder._canonical_bytes(payload)
    (tmp_path / "attestation.json").write_bytes(raw)
    (tmp_path / "attestation.json.sha256").write_text(
        f"{hashlib.sha256(raw).hexdigest()}  attestation.json\n",
        encoding="utf-8",
    )
    return evidence


def test_bundle_verifier_rejects_mutated_evidence(tmp_path, monkeypatch):
    evidence = _write_minimal_bundle(tmp_path, monkeypatch)

    monkeypatch.setattr(
        builder,
        "_git_identity",
        lambda _source: ("b" * 40, True),
    )
    monkeypatch.setattr(builder, "_tracked_paths", lambda _source: ())
    monkeypatch.setattr(builder, "_snapshot", lambda _root, _paths: {})
    monkeypatch.setattr(
        builder,
        "_source_tree_digest",
        lambda _records: "c" * 64,
    )
    builder.verify_attestation(tmp_path, require_exact=True)
    (evidence / "x").write_bytes(b"mutated\n")
    with pytest.raises(
        builder.AttestationBuildError,
        match="attestation_file_binding_invalid",
    ):
        builder.verify_attestation(tmp_path, require_exact=True)


def test_bundle_verifier_rejects_source_identity_mismatch(tmp_path, monkeypatch):
    _write_minimal_bundle(tmp_path, monkeypatch)
    monkeypatch.setattr(
        builder,
        "_git_identity",
        lambda _source: ("a" * 40, True),
    )
    monkeypatch.setattr(builder, "_tracked_paths", lambda _source: ())
    monkeypatch.setattr(builder, "_snapshot", lambda _root, _paths: {})
    monkeypatch.setattr(
        builder,
        "_source_tree_digest",
        lambda _records: "c" * 64,
    )
    with pytest.raises(
        builder.AttestationBuildError,
        match="attestation_source_not_exact",
    ):
        builder.verify_attestation(tmp_path, require_exact=True)


def test_bundle_verifier_rejects_symlinked_evidence_root(tmp_path, monkeypatch):
    real_root = tmp_path / "real"
    real_root.mkdir()
    _write_minimal_bundle(real_root, monkeypatch)
    evidence = real_root / "evidence"
    external = tmp_path / "external-evidence"
    evidence.rename(external)
    evidence.symlink_to(external, target_is_directory=True)

    with pytest.raises(
        builder.AttestationBuildError,
        match="attestation_root_inventory_invalid",
    ):
        builder.verify_attestation(real_root)


def test_workflow_publishes_external_attestation_without_source_closure_write():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "build_release_attestation.py" in workflow
    assert 'runner.temp }}/hde-release-attestation' in workflow
    assert "actions/upload-artifact@v4" in workflow
    assert "Run canonical JSON gate (closed rails)" in workflow
    assert '--verify "$RUNNER_TEMP/hde-release-attestation"' in workflow
    assert "regenerate_identity_closure.py --check" not in workflow
    assert "regenerate_identity_closure.py\n" not in workflow
    mirror_gate = Path("ci/checks/check_mirror_schema.sh").read_text(
        encoding="utf-8"
    )
    updater = Path("tools/evidence/update_evidence_index.py").read_text(
        encoding="utf-8"
    )
    assert "mtime later than filesystem stat" not in mirror_gate
    assert "PROOF_MTIME_FUTURE" not in updater


def test_direct_closure_cli_refuses_source_tree_execution(monkeypatch):
    from tools.evidence import regenerate_identity_closure as closure

    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    with pytest.raises(SystemExit, match="SOURCE_TREE_RELEASE_CLOSURE_REFUSED"):
        closure.main([])


def test_direct_release_evidence_write_cli_refuses_source_tree(monkeypatch):
    from scripts import release_id_recompute

    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    with pytest.raises(SystemExit):
        release_id_recompute.main([])


def test_catalog_manifest_is_packaged_from_its_single_source():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")

    assert '"catalog*"' in pyproject
    assert 'catalog = ["*.json"]' in pyproject
    assert Path("catalog/manifest.json").is_file()
    assert not Path("engine/runtime/catalog_manifest.json").exists()
