from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

import pytest

from tools.evidence import build_release_attestation as builder
from tools.evidence import regenerate_identity_closure as closure
from tools.cli import generate_cli_conformance_artifacts as cli_conformance


def test_attestation_ci_lane_is_bound_to_exact_candidate_head():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")
    exact_head = "${{ github.event.pull_request.head.sha || github.sha }}"
    lane_start = workflow.index(
        "      - name: Build and verify exact-source release attestation"
    )
    lane_end = workflow.index(
        "      - name: Verify truthful applicability and clean candidate tree",
        lane_start,
    )
    lane = workflow[lane_start:lane_end]

    assert f"ref: {exact_head}" in workflow
    assert "id: release_lane" in lane
    assert "if: ${{ steps.classify.outputs.release == 'true' }}" in lane
    assert 'release_test_source="$RUNNER_TEMP/hde-release-regression-tests"' in lane
    assert 'git worktree add --detach "$release_test_source"' in lane
    assert 'export PYTHONPATH="$release_test_source"' in lane
    assert 'git worktree remove --force "$release_test_source"' in lane
    # The detached test source, pre-build candidate, and post-build candidate
    # must each remain clean.
    assert lane.count('test -z "$(git status --short --untracked-files=all)"') == 3
    assert '--output "$attestation_root"' in lane
    assert '--verify "$attestation_root"' in lane
    assert "actions/upload-artifact" not in workflow
    assert "actions/download-artifact" not in workflow


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
        if command[1:4] == ["-m", "pip", "wheel"]:
            wheelhouse = Path(command[command.index("--wheel-dir") + 1])
            wheelhouse.mkdir(parents=True, exist_ok=True)
            (wheelhouse / "glow_hdengine-0.0.0-py3-none-any.whl").write_bytes(b"wheel")
        elif command[1:3] == ["-m", "venv"]:
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

    monkeypatch.setattr(builder, "_distribution_layout_compat_required", lambda env, cwd: False)
    monkeypatch.setattr(builder.subprocess, "run", run)
    transcript: list[str] = []
    scripts = builder._install_packaged_console_entrypoint(
        package_source,
        tmp_path,
        transcript,
    )

    assert len(calls) == 3
    assert calls[0][-1] == str(package_source)
    assert "--no-cache-dir" in calls[0]
    assert "--no-index" in calls[0]
    assert "--no-build-isolation" in calls[0]
    assert "--system-site-packages" not in calls[1]
    assert calls[2][-1].endswith(".whl")
    assert "--no-cache-dir" in calls[2]
    assert "--no-index" in calls[2]
    assert not (package_source / ".attestation-bin").exists()
    assert (scripts / ("hdctl.exe" if builder.os.name == "nt" else "hdctl")).is_file()
    assert transcript[0] == "stage=build_packaged_wheel"
    assert "stage=install_packaged_console_entrypoint" in transcript


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
    assert len(closure.DECLARED_PRODUCER_OUTPUTS) == 97
    assert len(set(closure.DECLARED_PRODUCER_OUTPUTS)) == 97
    assert len(closure.ATTESTATION_PRIMARY_OUTPUTS) == 97
    assert len(closure.ATTESTATION_PATH_PROOF_TARGETS) == 88
    assert len(closure.ATTESTATION_GENERATED_OUTPUTS) == 185
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


def test_tracked_source_copy_must_match_recorded_snapshot(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()
    tracked = (Path("tracked.txt"),)
    (source / "tracked.txt").write_text("original\n", encoding="utf-8")
    snapshot = builder._snapshot(source, tracked)

    builder._copy_tracked_source(source, destination, tracked)
    builder._require_exact_source_copy(destination, tracked, snapshot)

    (destination / "tracked.txt").write_text("changed\n", encoding="utf-8")
    with pytest.raises(
        builder.AttestationBuildError,
        match="tracked_source_copy_not_exact",
    ):
        builder._require_exact_source_copy(destination, tracked, snapshot)


def test_v1_schema_preserves_the_pf12_wire_contract():
    schema = json.loads(builder.SCHEMA_PATH.read_text(encoding="utf-8"))
    nonclaims = schema["properties"]["nonclaims"]

    assert schema["$id"] == builder.SCHEMA == "hde.release_attestation.v1"
    assert schema["properties"]["release_admission"] == {
        "const": "PR06R_B_FINAL_PASS"
    }
    assert [item["const"] for item in nonclaims["prefixItems"]] == [
        "builder_executes_no_ops",
        "no_database_write",
        "no_deployment_or_migration",
        "no_qa_pass_or_acceptance",
        "no_pf09_status_movement",
    ]
    assert nonclaims["minItems"] == nonclaims["maxItems"] == 5


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


def test_workflow_validates_external_attestation_without_source_closure_write():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "build_release_attestation.py" in workflow
    assert 'attestation_root="$RUNNER_TEMP/hde-release-attestation"' in workflow
    assert '--output "$attestation_root"' in workflow
    assert '--verify "$attestation_root"' in workflow
    assert "actions/upload-artifact" not in workflow
    assert "actions/download-artifact" not in workflow
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


def test_release_closure_does_not_currentize_frozen_architecture_snapshot():
    assert "architecture_snapshot" not in {step.name for step in closure.CLOSURE_STEPS}
    assert (
        "artifacts/architecture/architecture_snapshot.keys_only.json"
        not in closure.ATTESTATION_GENERATED_OUTPUTS
    )


def test_release_closure_does_not_run_epic_closeout_assertions():
    source = Path("tools/evidence/regenerate_identity_closure.py").read_text(
        encoding="utf-8"
    )
    assert "tests/qa/test_epic022_acceptance_scaffold.py" not in source
    assert "tests/qa/test_epic022_close_pack_ready.py" not in source


def test_direct_release_evidence_write_cli_refuses_source_tree(monkeypatch):
    from scripts import release_id_recompute

    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    with pytest.raises(SystemExit):
        release_id_recompute.main([])


def test_catalog_manifest_is_packaged_from_its_single_source():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")

    assert '"catalog*"' in pyproject
    assert 'catalog = ["*.json"]' in pyproject


def test_magic10_thresholds_are_available_to_the_installed_console():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")

    assert '"math*"' in pyproject
    assert 'math = ["*.json"]' in pyproject
    assert Path("catalog/manifest.json").is_file()
    assert not Path("engine/runtime/catalog_manifest.json").exists()


def _fake_setuptools(root: Path, install_lib_source: str) -> SimpleNamespace:
    package = root / "setuptools"
    (package / "command").mkdir(parents=True)
    (package / "__init__.py").write_text("", encoding="utf-8")
    (package / "command" / "install_lib.py").write_text(install_lib_source, encoding="utf-8")
    return SimpleNamespace(origin=str(package / "__init__.py"))


@pytest.mark.parametrize(
    "system_mod,install_lib,expected",
    [
        (True, "self.set_undefined_options('install',('install_layout','install_layout'))\n", False),
        (False, "self.set_undefined_options('install',('install_layout','install_layout'))\n", True),
        (False, "class install_lib: pass\n", False),
        (False, None, False),
    ],
    ids=["system-mod-present", "patched-backend", "unpatched-backend", "no-setuptools"],
)
def test_wheel_layout_compat_is_required_only_for_a_distribution_patched_backend(
    tmp_path, monkeypatch, capsys, system_mod, install_lib, expected
):
    setuptools_spec = None if install_lib is None else _fake_setuptools(tmp_path, install_lib)

    def find_spec(name):
        if name == "_distutils_system_mod":
            return object() if system_mod else None
        assert name == "setuptools"
        return setuptools_spec

    monkeypatch.setattr(importlib.util, "find_spec", find_spec)
    exec(compile(builder._LAYOUT_COMPAT_PROBE, "layout-compat-probe", "exec"), {"__name__": "probe"})
    assert capsys.readouterr().out == ("required\n" if expected else "not-required\n")


@pytest.mark.parametrize(
    "returncode,stdout,expected",
    [(0, "required\n", True), (0, "not-required\n", False), (1, "required\n", False), (0, "", False)],
    ids=["required", "not-required", "probe-failed", "no-answer"],
)
def test_layout_compat_probe_runs_in_the_wheel_child_interpreter_and_environment(
    tmp_path, monkeypatch, returncode, stdout, expected
):
    monkeypatch.setenv("PYTHONPATH", "/ambient/unpatched/setuptools")
    monkeypatch.setenv("PYTHONUSERBASE", "/ambient/user/base")
    calls: list[tuple[list[str], dict[str, object]]] = []

    def run(argv, **kwargs):
        calls.append((list(argv), kwargs))
        return subprocess.CompletedProcess(args=argv, returncode=returncode, stdout=stdout)

    monkeypatch.setattr(builder.subprocess, "run", run)
    child_env = builder._clean_child_env()
    assert builder._distribution_layout_compat_required(child_env, tmp_path) is expected
    (argv, kwargs), = calls
    assert argv == [sys.executable, "-c", builder._LAYOUT_COMPAT_PROBE]
    assert kwargs["env"] == child_env and kwargs["cwd"] == tmp_path
    assert not {"PYTHONPATH", "PYTHONUSERBASE"} & set(kwargs["env"])


def test_wheel_build_env_adds_only_the_builder_owned_compat_path(tmp_path, monkeypatch):
    monkeypatch.setenv("PYTHONPATH", "/ambient/should/not/leak")
    probed: list[tuple[dict[str, str], Path]] = []

    def not_required(env, cwd):
        probed.append((dict(env), cwd))
        return False

    monkeypatch.setattr(builder, "_distribution_layout_compat_required", not_required)
    env, applied = builder._wheel_build_env(tmp_path)
    assert applied is False and env == builder._clean_child_env()
    assert probed == [(builder._clean_child_env(), tmp_path)]
    assert not (tmp_path / "build-backend-compat").exists()

    monkeypatch.setattr(builder, "_distribution_layout_compat_required", lambda env, cwd: True)
    env, applied = builder._wheel_build_env(tmp_path)
    compat = tmp_path / "build-backend-compat"
    assert applied is True
    assert env == {**builder._clean_child_env(), "PYTHONPATH": str(compat)}
    assert sorted(path.name for path in compat.iterdir()) == ["_distutils_system_mod.py"]
    compile((compat / "_distutils_system_mod.py").read_text(encoding="utf-8"), "shim", "exec")


def test_wheel_layout_compat_supplies_neutral_install_options(tmp_path, monkeypatch):
    monkeypatch.setattr(builder, "_distribution_layout_compat_required", lambda env, cwd: True)
    env, _ = builder._wheel_build_env(tmp_path)
    probe = (
        "import setuptools, _distutils_system_mod\n"
        "from distutils.dist import Distribution\n"
        "import distutils.command.install as install\n"
        "command = install.install(Distribution())\n"
        "assert command.install_layout is None and command.prefix_option is None\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", probe], cwd=tmp_path, env=env, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr


def test_wheel_stage_records_and_scopes_the_layout_compat(tmp_path, monkeypatch):
    package_source = tmp_path / "package-source"
    package_source.mkdir()
    envs: list[dict[str, str]] = []

    def run(argv, **kwargs):
        command = list(argv)
        envs.append(dict(kwargs["env"]))
        if command[1:4] == ["-m", "pip", "wheel"]:
            wheelhouse = Path(command[command.index("--wheel-dir") + 1])
            (wheelhouse / "glow_hdengine-0.0.0-py3-none-any.whl").write_bytes(b"wheel")
        elif command[1:3] == ["-m", "venv"]:
            scripts = tmp_path / "venv" / ("Scripts" if builder.os.name == "nt" else "bin")
            scripts.mkdir(parents=True)
            (scripts / ("python.exe" if builder.os.name == "nt" else "python")).write_text("")
        else:
            console = tmp_path / "venv" / ("Scripts/hdctl.exe" if builder.os.name == "nt" else "bin/hdctl")
            console.write_text("#!/bin/sh\n")
            console.chmod(0o755)
        return subprocess.CompletedProcess(args=command, returncode=0)

    monkeypatch.setattr(builder, "_distribution_layout_compat_required", lambda env, cwd: True)
    monkeypatch.setattr(builder.subprocess, "run", run)
    transcript: list[str] = []
    builder._install_packaged_console_entrypoint(package_source, tmp_path, transcript)

    assert envs[0]["PYTHONPATH"] == str(tmp_path / "build-backend-compat")
    assert all("PYTHONPATH" not in env for env in envs[1:])
    assert transcript[:3] == [
        "stage=build_packaged_wheel",
        "source=tracked_source_copy",
        "build_backend_compat=distribution_install_layout",
    ]
    assert not any(package_source.iterdir())


_STUB_LOADER = """
class SchemaValidationError(Exception):
    def __init__(self, code, message=""):
        super().__init__(message)
        self.code = code


def load_active_mechanics_bundle():
    {body}
"""
_REFUSES = 'raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "stub")'
_ADMITS = "return object()"


def _stub_engine(root: Path, body: str) -> None:
    config = root / "engine" / "config"
    config.mkdir(parents=True)
    (root / "engine" / "__init__.py").write_text("", encoding="utf-8")
    (config / "__init__.py").write_text("", encoding="utf-8")
    (config / "registry_loader.py").write_text(_STUB_LOADER.format(body=body), encoding="utf-8")


def _isolated_copy(tmp_path: Path, body: str) -> Path:
    copy = tmp_path / "copy"
    (copy / "tools" / "evidence").mkdir(parents=True)
    (copy / "tools" / "evidence" / "regenerate_identity_closure.py").write_bytes(
        Path("tools/evidence/regenerate_identity_closure.py").read_bytes()
    )
    _stub_engine(copy, body)
    return copy / "tools" / "evidence" / "regenerate_identity_closure.py"


_PROBE = (
    "import runpy, sys\n"
    "{preimport}"
    "ns = runpy.run_path(sys.argv[1], run_name='probe')\n"
    "print(ns['release_not_admitted_observed']())\n"
)


def _probe(script: Path, cwd: Path, *, ambient: Path | None = None, preimport: str = ""):
    env = {"PATH": "/usr/bin:/bin", "HDE_ISOLATED_RELEASE_BUILD": "1"}
    if ambient is not None:
        env["PYTHONPATH"] = str(ambient)
    return subprocess.run(
        [sys.executable, "-S", "-c", _PROBE.format(preimport=preimport), str(script)],
        cwd=cwd, env=env, capture_output=True, text=True, check=False,
    )


def test_closure_probe_follows_the_isolated_copy_with_no_ambient_engine(tmp_path):
    script = _isolated_copy(tmp_path, _REFUSES)
    neutral = tmp_path / "neutral"
    neutral.mkdir()
    result = subprocess.run(
        [sys.executable, "-I", "-S", str(script), "--in-place-isolated"],
        cwd=neutral, env={"PATH": "/usr/bin:/bin", "HDE_ISOLATED_RELEASE_BUILD": "1"},
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == closure.RELEASE_NOT_ADMITTED_EXIT_CODE, result.stderr
    assert result.stdout == closure.NOT_ADMITTED_LINE + "\n"


@pytest.mark.parametrize(
    "copy_body,ambient_body,expected",
    [(_REFUSES, _ADMITS, "True"), (_ADMITS, _REFUSES, "False")],
    ids=["copy-refuses-ambient-admits", "copy-admits-ambient-refuses"],
)
def test_closure_probe_ignores_a_different_ambient_engine(tmp_path, copy_body, ambient_body, expected):
    script = _isolated_copy(tmp_path, copy_body)
    ambient = tmp_path / "ambient"
    _stub_engine(ambient, ambient_body)
    neutral = tmp_path / "neutral"
    neutral.mkdir()
    result = _probe(script, neutral, ambient=ambient)
    assert result.returncode == 0, result.stderr
    assert result.stdout == expected + "\n"


def test_closure_probe_fails_closed_when_engine_was_imported_from_elsewhere(tmp_path):
    script = _isolated_copy(tmp_path, _REFUSES)
    ambient = tmp_path / "ambient"
    _stub_engine(ambient, _ADMITS)
    neutral = tmp_path / "neutral"
    neutral.mkdir()
    result = _probe(script, neutral, ambient=ambient, preimport="import engine.config.registry_loader\n")
    assert result.returncode != 0
    assert "IDENTITY_CLOSURE:ADMISSION_PROBE_NOT_ROOT_BOUND" in result.stderr
