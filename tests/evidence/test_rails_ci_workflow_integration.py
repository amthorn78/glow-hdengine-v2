from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from ci.checks import classify_ci_changes as classifier
from ci.checks import run_rails_job_definitions as runner
from tools.evidence import build_release_attestation as attestation
from tools.evidence import generate_rails_gate_evidence as producer
from tools.evidence import regenerate_identity_closure as release_closure
from tools.evidence import run_sanity_pipeline as release_sanity

ROOT = Path(__file__).resolve().parents[2]
DEFS = [
    ROOT / "ci/jobs/rails_closed_refusal.yml",
    ROOT / "ci/jobs/rails_open_conformance.yml",
    ROOT / "ci/jobs/logs_keys_only_redaction.yml",
]


def _repo_state() -> tuple[str, str]:
    diff = subprocess.run(["git", "diff", "--exit-code"], cwd=ROOT, text=True, capture_output=True)
    status = subprocess.run(["git", "status", "--porcelain=v1", "--untracked-files=all"], cwd=ROOT, text=True, capture_output=True, check=True)
    return (str(diff.returncode), status.stdout)


def _materialize_test_targets(repo: Path, targets: tuple[str, ...]) -> None:
    for target in targets:
        path = repo / target
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("def test_placeholder(): pass\n", encoding="utf-8")


def test_workflow_contains_one_conditional_closed_default_rails_lane() -> None:
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "  rails-policy-gates:" not in text
    assert "  sanity-pipeline:" not in text
    assert "id: rails_lane" in text
    assert "if: ${{ steps.classify.outputs.rails == 'true' }}" in text
    assert text.count("python ci/checks/run_rails_job_definitions.py") == 1
    start = text.index("      - name: Run rails policy and secret-safety lane")
    end = text.index("      - name: Run governed evidence integrity lane", start)
    lane = text[start:end]
    for definition in (
        "ci/jobs/rails_closed_refusal.yml",
        "ci/jobs/rails_open_conformance.yml",
        "ci/jobs/logs_keys_only_redaction.yml",
    ):
        assert lane.count(definition) == 1
    for needle in ["LC_ALL: C", "LANG: C", "TZ: UTC", 'SAFE_MODE: "1"', 'ALLOW_NETWORK: "0"']:
        assert needle in text
    assert "secrets:" not in lane
    assert "${{ secrets." not in lane.lower()


def test_workflow_has_one_truthful_exact_head_summary_topology() -> None:
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    exact_head = "${{ github.event.pull_request.head.sha || github.sha }}"

    assert "  pull_request:" in text
    assert "  push:\n    branches:\n      - main" in text
    assert "permissions:\n  contents: read" in text
    assert "cancel-in-progress: ${{ github.event_name == 'pull_request' }}" in text
    assert "group: ci-${{ github.workflow }}-${{ github.event.pull_request.number || github.run_id }}" in text
    assert text.count("\n    runs-on:") == 1
    assert "\n  test:\n" in text
    assert "needs:" not in text
    assert text.count("actions/checkout@v4") == 1
    assert text.count("persist-credentials: false") == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count("actions/setup-python@v5") == 1
    assert text.count("python -m pip install") == 1
    assert text.count("python -m pytest --version") == 1
    assert f"ref: {exact_head}" in text
    assert "BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}" in text
    assert "HEAD_SHA: ${{ github.event.pull_request.head.sha || github.sha }}" in text
    assert '--event-name "${{ github.event_name }}"' in text
    assert "actions/upload-artifact" not in text
    assert "actions/download-artifact" not in text
    assert "ALLOW_NETWORK=1" not in text
    assert "tools.evidence.epic020_bundle" not in text
    assert "test_epic020_bundle_index_integration.py" not in text
    assert "tools/evidence/update_evidence_index.py --epic-id" not in text
    assert "tools/evidence/update_evidence_index.py --check" in text
    assert (
        'python tools/cli/serializer_grep_guard.py --output '
        '"$RUNNER_TEMP/serializer_grep_guard.log"'
    ) in text
    assert (
        'python tools/cli/emitter_symbol_proof.py --output '
        '"$RUNNER_TEMP/emitter_symbol_proof.txt"'
    ) in text
    assert "generate_hde_" + "epic038_closeout" not in text
    assert "check_hde_epic038_" + "qa_current_state" not in text
    assert "EPIC038_" + "CLOSEOUT" not in text
    assert "tests/evidence/test_architecture_snapshot.py" in text
    assert "tests/ops/test_hde_epic038_ops03.py" not in text
    for step_id in (
        "classify",
        "pytest_readiness",
        "changed_tests",
        "product_lane",
        "compat_lane",
        "db_lane",
        "rails_lane",
        "evidence_lane",
        "qa_lane",
        "release_lane",
        "final_audit",
    ):
        assert f"id: {step_id}" in text
    assert "if: ${{ always() }}" in text
    assert "APPLICABLE_CI_LANE_NOT_SUCCESSFUL" in text
    assert "CI_APPLICABILITY_AND_EXACT_HEAD_OK" in text
    assert '--changed-tests-output "$RUNNER_TEMP/ci-changed-test-targets.txt"' in text
    assert "if: ${{ steps.classify.outputs.changed_tests == 'true' }}" in text
    assert 'changed_test_source="$RUNNER_TEMP/hde-changed-test-source"' in text
    assert (
        'python -m pytest -q -p no:cacheprovider -- "${changed_test_targets[@]}"'
        in text
    )
    changed_test_step = text[
        text.index("      - name: Run affected behavioral tests in isolation") :
        text.index("      - name: Run product mechanics and ordering lane")
    ]
    assert "git diff --exit-code" in changed_test_step
    assert 'git status --short --untracked-files=all' in changed_test_step
    qa_step = text[
        text.index("      - name: Run approved generic QA subsystem lane in isolation") :
        text.index("      - name: Build and verify exact-source release attestation")
    ]
    release_step = text[
        text.index("      - name: Build and verify exact-source release attestation") :
        text.index("      - name: Verify truthful applicability and clean candidate tree")
    ]
    for isolated_step in (qa_step, release_step):
        assert "git diff --exit-code" in isolated_step
        assert 'git status --short --untracked-files=all' in isolated_step
    assert 'require_outcome "$NEEDS_PYTHON" "$PYTEST_READINESS_OUTCOME" pytest-readiness' in text
    assert 'require_outcome "$CHANGED_TESTS" "$CHANGED_TESTS_OUTCOME" changed-tests' in text

    install = text.index("      - name: Install applicable validation dependencies")
    readiness = text.index("      - name: Verify pytest readiness")
    changed_tests = text.index("      - name: Run affected behavioral tests in isolation")
    lanes = text.index("      - name: Run product mechanics and ordering lane")
    assert install < readiness < changed_tests < lanes

    workflow_targets = set(re.findall(r"tests/[A-Za-z0-9_./-]+", text))
    fixed_targets = set(classifier._FIXED_LANE_TEST_DIRECTORIES) | set(
        classifier._FIXED_LANE_TEST_PROVIDERS
    )
    assert workflow_targets == fixed_targets


@pytest.mark.parametrize(
    ("paths", "expected_lanes", "expected_reason"),
    [
        (["README.md"], set(), "documentation_only"),
        (["docs/plans/hde-epic038.md"], set(), "documentation_only"),
        (["docs/adr/hde/body_graphs_adr.md"], {"evidence"}, "selected_lanes"),
        (["docs/run/EPIC011_TEST_IDENTITIES.md"], {"evidence"}, "selected_lanes"),
        (["docs/run/PROD_ENDPOINTS.json"], {"evidence"}, "selected_lanes"),
        (["notes/d6_vendor_live_qa_discovery.md"], {"evidence"}, "selected_lanes"),
        (["audit/history/closed-run.json"], {"evidence"}, "selected_lanes"),
        (["audit/ops/hde-epic038/ops-03/result.json"], {"evidence"}, "selected_lanes"),
        (["artifacts/architecture/architecture_snapshot.keys_only.json"], {"evidence"}, "selected_lanes"),
        (["artifacts/epic020/bundles/capture.json"], {"evidence"}, "selected_lanes"),
        (["artifacts/runs/closed-run.json"], {"evidence"}, "selected_lanes"),
        (["artifacts/db_bridge/health.json"], {"evidence"}, "selected_lanes"),
        (["audit/qa/hde-epic039/00_meta/doc_deltas.md"], {"evidence"}, "selected_lanes"),
        (["catalog/manifest.json"], {"release"}, "selected_lanes"),
        (["engine/narratives/router.py"], {"product", "release"}, "selected_lanes"),
        (["engine/db/adapter.py"], {"product", "db", "release"}, "selected_lanes"),
        (["adapter/http_reader.py"], {"product", "compat", "release"}, "selected_lanes"),
        (["engine/bodygraph/vendor_client.py"], {"product", "rails", "release"}, "selected_lanes"),
        (["tools/qa/qa_harness.py"], {"evidence", "qa"}, "selected_lanes"),
        (["tools/qa/run_hde_epic024_harness.py"], {"evidence", "qa"}, "selected_lanes"),
        (["tools/evidence/run_sanity_pipeline.py"], {"evidence", "release"}, "selected_lanes"),
        (["tools/evidence/update_evidence_index.py"], {"evidence", "release"}, "selected_lanes"),
        (["tools/evidence/generate_architecture_snapshot.py"], {"evidence", "product"}, "selected_lanes"),
        (["tests/evidence/test_architecture_snapshot.py"], {"evidence", "product"}, "selected_lanes"),
        (["ci/checks/run_rails_job_definitions.py"], {"rails", "release"}, "selected_lanes"),
        (["tests/adapter/test_env_guard_prod_variants.py"], {"product", "compat", "release"}, "selected_lanes"),
        (["engine/canon/__init__.py.REMOVED.md"], set(), "documentation_only"),
        (["engine/config/provider_loader.bak2"], {"evidence"}, "selected_lanes"),
        (["engine/serializer/canon.py.bak.20251022212047"], {"evidence"}, "selected_lanes"),
        (["scripts/card_close.sh.bak"], {"evidence"}, "selected_lanes"),
        (["scripts/hdctl.backup.py"], {"evidence"}, "selected_lanes"),
        (["catalog/manifest.json.path_proof.txt"], {"evidence"}, "selected_lanes"),
        (["schemas/hde_release_attestation.v1.json"], {"release"}, "selected_lanes"),
        (["schemas/architecture_snapshot.keys_only.v1.json"], {"evidence"}, "selected_lanes"),
        (["schemas/hde_epic038_direct_db_selection.v1.json"], {"db", "evidence", "release"}, "selected_lanes"),
        (["schemas/hde_epic038_ops03_result_summary.v1.json"], {"evidence"}, "selected_lanes"),
        (["audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt"], {"evidence", "release"}, "selected_lanes"),
        (["tests/transport/headers/aux_text_200.snap.path_proof.txt"], {"evidence"}, "selected_lanes"),
        (["tests/README.md"], set(), "documentation_only"),
        ([".github/workflows/ci.yml"], set(classifier.LANES), "selected_lanes"),
        (["ci/checks/classify_ci_changes.py"], set(classifier.LANES), "selected_lanes"),
    ],
)
def test_change_classifier_selects_expected_execution_scenarios(
    paths: list[str], expected_lanes: set[str], expected_reason: str
) -> None:
    result = classifier.classify_paths(paths)
    enabled = {lane for lane in classifier.LANES if result.flags[lane]}
    assert enabled == expected_lanes
    assert result.flags["needs_python"] is bool(expected_lanes)
    assert result.reason == expected_reason
    assert result.path_count == len(paths)


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def test_change_classifier_builds_safe_direct_test_targets(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    adapter = repo / "tests/adapter"
    unit = repo / "tests/unit"
    adapter.mkdir(parents=True)
    unit.mkdir(parents=True)
    (adapter / "test_env_guard_prod_variants.py").write_text(
        "def test_guard(): pass\n",
        encoding="utf-8",
    )
    (unit / "conftest.py").write_text("VALUE = 1\n", encoding="utf-8")
    (unit / "test_unit.py").write_text(
        "def test_unit(): pass\n",
        encoding="utf-8",
    )

    direct_targets = classifier.changed_test_targets(
        repo,
        (
            "tests/adapter/test_env_guard_prod_variants.py",
            "tests/unit/test_unit.py",
        ),
    )

    assert direct_targets == (
        "tests/adapter/test_env_guard_prod_variants.py",
        "tests/unit/test_unit.py",
    )

    fixture = adapter / "fixtures/input.json"
    fixture.parent.mkdir()
    fixture.write_text("{}\n", encoding="utf-8")
    symlink = adapter / "test_link.py"
    symlink.symlink_to(adapter / "test_env_guard_prod_variants.py")

    for ambiguous_path in (
        "tests/adapter/fixtures/input.json",
        "tests/adapter/test_link.py",
    ):
        with pytest.raises(ValueError, match="CI_TEST_SUPPORT_OWNER_MISSING"):
            classifier.changed_test_targets(repo, (ambiguous_path,))
    with pytest.raises(ValueError, match="CI_TEST_SUPPORT_OWNER_MISSING"):
        classifier.changed_test_targets(ROOT, ("tests/unit/helpers.py",))
    with pytest.raises(ValueError, match="CI_TEST_SUPPORT_OWNER_MISSING"):
        classifier.changed_test_targets(repo, ("tests/deleted/helpers.py",))
    assert classifier.changed_test_targets(
        repo,
        ("tests/deleted/test_removed.py",),
    ) == ()
    with pytest.raises(ValueError, match="CI_REGISTERED_OWNER_TEST_DELETED"):
        classifier.changed_test_targets(
            repo,
            ("tests/unit/test_narratives_router.py",),
        )


def test_product_source_owner_policy_is_explicit_and_fail_closed() -> None:
    active_suffixes = {".json", ".py", ".sh", ".sql"}
    blocked: set[str] = set()
    handled: set[str] = set()
    for prefix in classifier._PRODUCT_PREFIXES:
        root = ROOT / prefix
        if not root.exists():
            continue
        for candidate in root.rglob("*"):
            if (
                not candidate.is_file()
                or candidate.is_symlink()
                or candidate.suffix.lower() not in active_suffixes
            ):
                continue
            rel = candidate.relative_to(ROOT).as_posix()
            try:
                classifier._product_owner_targets(ROOT, rel)
            except ValueError as exc:
                assert str(exc).startswith("CI_PRODUCT_OWNER_TEST_MISSING:"), rel
                blocked.add(rel)
            else:
                handled.add(rel)
    assert handled
    assert blocked
    assert "adapter/http_reader.py" in handled
    assert "engine/bodygraph/vendor_client.py" in handled
    assert "engine/serializer/canon.py" in handled
    assert "engine/errors/__init__.py" in blocked
    assert "adapter/cache_keys.py" in blocked

    assert classifier._EVIDENCE_GENERATOR_TEST_OWNERS
    for rel in sorted(classifier._EVIDENCE_GENERATOR_TEST_OWNERS):
        assert (ROOT / rel).is_file()
        classifier._evidence_generator_owner_targets(ROOT, rel)


def test_http_reader_owner_registry_covers_active_direct_consumers() -> None:
    direct_consumers: set[str] = set()
    for candidate in (ROOT / "tests").rglob("test_*.py"):
        if not candidate.is_file() or candidate.is_symlink():
            continue
        tree = ast.parse(candidate.read_text(encoding="utf-8"))
        imports_reader = any(
            (
                isinstance(node, ast.Import)
                and any(
                    alias.name == "adapter.http_reader" for alias in node.names
                )
            )
            or (
                isinstance(node, ast.ImportFrom)
                and (
                    node.module == "adapter.http_reader"
                    or (
                        node.module == "adapter"
                        and any(alias.name == "http_reader" for alias in node.names)
                    )
                )
            )
            or (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "import_module"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and node.args[0].value == "adapter.http_reader"
            )
            for node in ast.walk(tree)
        )
        if imports_reader:
            direct_consumers.add(candidate.relative_to(ROOT).as_posix())

    owners = set(classifier._HTTP_READER_TEST_OWNERS)
    assert direct_consumers
    assert direct_consumers <= owners
    assert {
        "tests/adapter/test_diagnostic_writer.py",
        "tests/http/test_reader_a7_transport.py",
    } <= owners
    for owner in owners:
        path = ROOT / owner
        assert path.is_file(), owner
        assert not path.is_symlink(), owner

    expected_direct = tuple(
        sorted(
            owner
            for owner in owners
            if not classifier._fixed_lane_covers_test_target(
                "adapter/http_reader.py", owner
            )
        )
    )
    assert classifier.changed_test_targets(
        ROOT, ("adapter/http_reader.py",)
    ) == expected_direct


def test_qa_tool_owner_policy_is_exhaustive_and_deduplicated(
    tmp_path: Path,
) -> None:
    tracked = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "tools/qa").rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix.lower() == ".py"
    }
    assert (
        set(classifier._QA_TOOL_TEST_OWNERS)
        | classifier._QA_TOOLS_REQUIRING_OWNER
    ) == tracked
    assert not (
        set(classifier._QA_TOOL_TEST_OWNERS)
        & classifier._QA_TOOLS_REQUIRING_OWNER
    )
    assert all(
        classifier._QA_TOOL_OWNERSHIP_TEST in owners
        for owners in classifier._QA_TOOL_TEST_OWNERS.values()
    )

    for source, owners in sorted(classifier._QA_TOOL_TEST_OWNERS.items()):
        assert owners, source
        for owner in owners:
            assert (ROOT / owner).is_file(), (source, owner)
            assert not (ROOT / owner).is_symlink(), (source, owner)
        expected = tuple(
            owner
            for owner in owners
            if not classifier._fixed_lane_covers_test_target(source, owner)
        )
        assert classifier._qa_tool_owner_targets(ROOT, source) == expected

    assert classifier.changed_test_targets(
        ROOT, ("tools/qa/run_hde_epic024_harness.py",)
    ) == (
        "tests/qa/test_epic024_bootstrap_status.py",
        classifier._QA_TOOL_OWNERSHIP_TEST,
    )
    assert classifier.changed_test_targets(
        ROOT, ("tools/qa/token_roster_validate.py",)
    ) == (
        "tests/qa/test_epic023_acceptance_alignment.py",
        classifier._QA_TOOL_OWNERSHIP_TEST,
    )
    for source in sorted(classifier._QA_TOOLS_REQUIRING_OWNER):
        with pytest.raises(ValueError, match="CI_QA_OWNER_TEST_MISSING"):
            classifier.changed_test_targets(ROOT, (source,))
    assert classifier.changed_test_targets(
        ROOT, ("tools/qa/qa_harness.py",)
    ) == (classifier._QA_TOOL_OWNERSHIP_TEST,)

    unowned = tmp_path / "repo/tools/qa/new_harness.py"
    unowned.parent.mkdir(parents=True)
    unowned.write_text("VALUE = 1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="CI_QA_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            tmp_path / "repo", ("tools/qa/new_harness.py",)
        )
    unowned_upper = unowned.with_suffix(".PY")
    unowned_upper.write_text("VALUE = 1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="CI_QA_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            tmp_path / "repo", ("tools/qa/new_harness.PY",)
        )

    with pytest.raises(ValueError, match="CI_REGISTERED_OWNER_TEST_DELETED"):
        classifier.changed_test_targets(
            tmp_path / "repo", ("tests/qa/test_epic024_bootstrap_status.py",)
        )


def test_qa_tool_git_change_selects_its_exact_behavioral_owner(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    source = repo / "tools/qa/run_hde_epic024_harness.py"
    owner = repo / "tests/qa/test_epic024_bootstrap_status.py"
    ownership_guard = repo / classifier._QA_TOOL_OWNERSHIP_TEST
    source.parent.mkdir(parents=True)
    owner.parent.mkdir(parents=True)
    source.write_text("VALUE = 1\n", encoding="utf-8")
    owner.write_text("def test_owner(): pass\n", encoding="utf-8")
    ownership_guard.write_text("def test_registry(): pass\n", encoding="utf-8")
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "base")
    base = _git(repo, "rev-parse", "HEAD")

    source.write_text("VALUE = 2\n", encoding="utf-8")
    _git(repo, "add", source.relative_to(repo).as_posix())
    _git(repo, "commit", "-m", "change EPIC024 harness")
    head = _git(repo, "rev-parse", "HEAD")

    result = classifier.classify_git_change(
        repo, base, head, event_name="push"
    )
    assert {lane for lane in classifier.LANES if result.flags[lane]} == {
        "evidence",
        "qa",
    }
    assert result.test_targets == (
        "tests/qa/test_epic024_bootstrap_status.py",
        classifier._QA_TOOL_OWNERSHIP_TEST,
    )


def test_behavioral_owner_examples_cover_router_and_epic037_generator(
    tmp_path: Path,
) -> None:
    assert classifier.changed_test_targets(
        ROOT, ("engine/narratives/router.py",)
    ) == tuple(sorted(classifier._NARRATIVE_TEST_OWNERS))
    assert classifier.changed_test_targets(
        ROOT, ("tools/evidence/generate_hde_epic037_v2_adapter.py",)
    ) == ("tests/evidence/test_hde_epic037_v2_adapter.py",)
    with pytest.raises(ValueError, match="CI_PRODUCT_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(ROOT, ("engine/new_surface/module.py",))

    repo = tmp_path / "repo"
    generator = repo / "tools/evidence/generate_unowned_surface.py"
    generator.parent.mkdir(parents=True)
    generator.write_text("VALUE = 1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="CI_EVIDENCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            repo, ("tools/evidence/generate_unowned_surface.py",)
        )
    generator.unlink()
    with pytest.raises(ValueError, match="CI_EVIDENCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            repo, ("tools/evidence/generate_unowned_surface.py",)
        )
    removed_generator = "tools/evidence/generate_retired_subsystem.py"
    removed_owner = "tests/evidence/test_retired_subsystem.py"
    assert classifier.changed_test_targets(
        repo, (removed_generator, removed_owner)
    ) == ()
    with pytest.raises(ValueError, match="CI_EVIDENCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(repo, (removed_generator,))
    with pytest.raises(ValueError, match="CI_EVIDENCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            repo, ("tools/evidence/nested/generate_unowned_surface.py",)
        )
    with pytest.raises(ValueError, match="CI_EVIDENCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            ROOT, ("tools/evidence/generate_epic023_orientation_artifacts.py",)
        )
    with pytest.raises(ValueError, match="CI_SOURCE_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(ROOT, ("server/new_runtime.py",))
    with pytest.raises(ValueError, match="CI_PRODUCT_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(ROOT, ("engine/errors/runtime.py",))
    assert classifier.changed_test_targets(
        ROOT, ("scripts/probe_internal_version.py",)
    ) == ("tests/transport/test_internal_version_contract.py",)
    assert classifier.changed_test_targets(
        ROOT, ("tests/ops/test_http_logging.py",)
    ) == ("tests/ops/test_http_logging.py",)
    assert classifier.changed_test_targets(
        ROOT, ("engine/serializer/canon.py",)
    ) == ()
    assert classifier.changed_test_targets(
        ROOT, ("catalog/manifest.json",)
    ) == ()
    assert all(
        classifier._FIXED_LANE_TEST_PROVIDERS[target] == "release"
        for target in classifier._PRODUCT_TEST_OWNER_PATHS["catalog/manifest.json"]
    )
    with pytest.raises(ValueError, match="CI_PRODUCT_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            ROOT, ("scripts/db/verify_backup_restore.py",)
        )
    with pytest.raises(ValueError, match="CI_PRODUCT_OWNER_TEST_MISSING"):
        classifier.changed_test_targets(
            ROOT, ("engine/runtime/worker.backup.py",)
        )
    assert classifier.changed_test_targets(
        ROOT,
        (
            "engine/canon/__init__.py.REMOVED.md",
            "engine/config/provider_loader.bak2",
            "scripts/hdctl.backup.py",
            "catalog/manifest.json.path_proof.txt",
            "tests/transport/headers/aux_text_200.snap.path_proof.txt",
            "tests/README.md",
        ),
    ) == ()
    with pytest.raises(ValueError, match="CI_CHANGE_SURFACE_UNCLASSIFIED"):
        classifier.classify_paths(("new-surface.bin",))


def test_non_generator_evidence_helpers_have_exact_fail_closed_owners(
    tmp_path: Path,
) -> None:
    assert classifier.changed_test_targets(
        ROOT, ("tools/evidence/strict_json_schema.py",)
    ) == (
        classifier._EVIDENCE_HELPER_OWNERSHIP_TEST,
        "tests/ops/test_hde_epic038_ops03.py",
    )
    assert classifier.changed_test_targets(
        ROOT, ("tools/evidence/run_sanity_pipeline.py",)
    ) == (classifier._EVIDENCE_HELPER_OWNERSHIP_TEST,)

    for source in sorted(classifier._EVIDENCE_HELPERS_REQUIRING_OWNER):
        with pytest.raises(
            ValueError, match="CI_EVIDENCE_HELPER_OWNER_MISSING"
        ):
            classifier.changed_test_targets(ROOT, (source,))

    repo = tmp_path / "repo"
    helper = repo / "tools/evidence/new_helper.py"
    helper.parent.mkdir(parents=True)
    helper.write_text("VALUE = 1\n", encoding="utf-8")
    for path in (
        "tools/evidence/new_helper.py",
        "tools/evidence/new_helper.PY",
        "tools/evidence/Generate_unowned.py",
    ):
        with pytest.raises(
            ValueError,
            match="CI_EVIDENCE_(?:OWNER_TEST|HELPER_OWNER)_MISSING",
        ):
            classifier.changed_test_targets(repo, (path,))

    removed_helper = "tools/evidence/check_retired_surface.py"
    removed_owner = "tests/evidence/test_check_retired_surface.py"
    assert classifier.changed_test_targets(
        repo, (removed_helper, removed_owner)
    ) == ()
    with pytest.raises(ValueError, match="CI_EVIDENCE_HELPER_OWNER_MISSING"):
        classifier.changed_test_targets(repo, (removed_helper,))

    with pytest.raises(ValueError, match="CI_EVIDENCE_HELPER_OWNER_INVALID"):
        classifier.changed_test_targets(
            repo, ("tools/evidence/strict_json_schema.py",)
        )


def test_fail_safe_full_validation_runs_the_supplemental_behavioral_gap() -> None:
    expected = tuple(sorted(classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS))
    empty = classifier.classify_paths(())
    assert all(empty.flags[lane] for lane in classifier.LANES)
    assert empty.test_targets == expected

    known_full = classifier.classify_paths((".github/workflows/ci.yml",))
    assert all(known_full.flags[lane] for lane in classifier.LANES)
    assert known_full.test_targets == ()
    assert classifier.changed_test_targets(
        ROOT, (".github/workflows/ci.yml",)
    ) == expected


def test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
        timeout=120,
    )
    configured = {
        line.split("::", 1)[0]
        for line in result.stdout.splitlines()
        if line.startswith("tests/") and "::" in line
    }
    fixed = {
        path
        for path in configured
        if path in classifier._FIXED_LANE_TEST_PROVIDERS
        or any(
            path == directory or path.startswith(f"{directory}/")
            for directory in classifier._FIXED_LANE_TEST_DIRECTORIES
        )
    }
    supplemental = set(classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS)
    inactive = classifier._FULL_VALIDATION_INACTIVE_TESTS

    assert configured
    assert not fixed & supplemental
    assert not fixed & inactive
    assert not supplemental & inactive
    assert configured == fixed | supplemental | inactive
    for path in supplemental | inactive:
        candidate = ROOT / path
        assert candidate.is_file(), path
        assert not candidate.is_symlink(), path


def test_full_validation_inputs_run_the_supplemental_behavioral_gap() -> None:
    expected = tuple(sorted(classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS))
    full_paths = set(classifier._FULL_VALIDATION_PATHS) | {
        ".github/workflows/ci.yml"
    }
    for path in sorted(full_paths):
        result = classifier.classify_paths((path,))
        assert all(result.flags[lane] for lane in classifier.LANES), path
        assert classifier.changed_test_targets(ROOT, (path,)) == expected

    direct_test = "tests/adapter/test_env_guard_prod_variants.py"
    assert classifier.changed_test_targets(
        ROOT, ("requirements.txt", direct_test)
    ) == tuple(sorted(set(expected) | {direct_test}))

    for path in sorted(classifier._FULL_VALIDATION_INACTIVE_TESTS):
        with pytest.raises(
            ValueError, match="CI_INACTIVE_TEST_REQUIRES_DISPOSITION"
        ):
            classifier.changed_test_targets(ROOT, (path,))


def test_every_current_governed_primary_selects_evidence() -> None:
    governed = classifier._load_governed_primary_paths(ROOT)
    assert {
        "docs/adr/hde/body_graphs_adr.md",
        "docs/run/EPIC011_TEST_IDENTITIES.md",
        "docs/run/PROD_ENDPOINTS.json",
        "notes/d6_vendor_live_qa_discovery.md",
    } <= governed
    for path in governed:
        result = classifier.classify_paths((path,), governed_paths=governed)
        assert result.flags["evidence"], path

    ordinary_doc = classifier.classify_paths(
        ("docs/run/RUN_PROD_QA.md",),
        governed_paths=governed,
    )
    assert not any(ordinary_doc.flags[lane] for lane in classifier.LANES)
    assert ordinary_doc.reason == "documentation_only"


def test_governed_document_git_change_selects_evidence(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    primary = repo / "docs/run/PROD_ENDPOINTS.json"
    index = repo / "docs/evidence/INDEX.json"
    index.parent.mkdir(parents=True)
    primary.parent.mkdir(parents=True, exist_ok=True)
    primary.write_text("{}\n", encoding="utf-8")
    index.write_text(
        '[{"artifact_key":"run.prod_endpoints",'
        '"discovered_physical_path":"docs/run/PROD_ENDPOINTS.json"}]\n',
        encoding="utf-8",
    )
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "base")
    base = _git(repo, "rev-parse", "HEAD")

    primary.write_text('{"updated":true}\n', encoding="utf-8")
    _git(repo, "add", "docs/run/PROD_ENDPOINTS.json")
    _git(repo, "commit", "-m", "update governed run input")
    head = _git(repo, "rev-parse", "HEAD")

    result = classifier.classify_git_change(
        repo, base, head, event_name="push"
    )
    assert {lane for lane in classifier.LANES if result.flags[lane]} == {
        "evidence"
    }
    assert result.test_targets == ()


def test_manifest_only_git_change_selects_release_owners(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    for relative in classifier._PRODUCT_TEST_OWNER_PATHS["catalog/manifest.json"]:
        owner = repo / relative
        owner.parent.mkdir(parents=True, exist_ok=True)
        owner.write_text("def test_owner(): pass\n", encoding="utf-8")
    (repo / "README.md").write_text("base\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "base")
    base = _git(repo, "rev-parse", "HEAD")

    manifest = repo / "catalog/manifest.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text("{}\n", encoding="utf-8")
    _git(repo, "add", "catalog/manifest.json")
    _git(repo, "commit", "-m", "release cut")
    head = _git(repo, "rev-parse", "HEAD")

    result = classifier.classify_git_change(
        repo, base, head, event_name="push"
    )
    assert {lane for lane in classifier.LANES if result.flags[lane]} == {"release"}
    assert result.test_targets == ()
    assert {
        lane
        for lane in classifier.LANES
        if classifier.classify_paths(
            ("catalog/manifest.json", "catalog/manifest.json.path_proof.txt")
        ).flags[lane]
    } == {"evidence", "release"}


def test_change_classifier_writes_changed_test_execution_contract(
    tmp_path: Path,
) -> None:
    github_output = tmp_path / "github-output"
    changed_tests = tmp_path / "changed-tests"
    result = classifier.Classification(
        flags=classifier._empty_flags(),
        reason="selected_lanes",
        path_count=1,
        test_targets=("tests/adapter/test_env_guard_prod_variants.py",),
    )

    classifier.write_github_output(github_output, result)
    classifier.write_changed_test_targets(changed_tests, result.test_targets)

    assert "changed_tests=true\n" in github_output.read_text(encoding="utf-8")
    assert changed_tests.read_text(encoding="utf-8") == (
        "tests/adapter/test_env_guard_prod_variants.py\n"
    )


def test_change_classifier_executes_against_exact_git_refs(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    (repo / "README.md").write_text("first\n", encoding="utf-8")
    _materialize_test_targets(
        repo, classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS
    )
    _git(repo, "add", "README.md")
    _git(repo, "add", "tests")
    _git(repo, "commit", "-m", "base")
    base = _git(repo, "rev-parse", "HEAD")

    (repo / "README.md").write_text("second\n", encoding="utf-8")
    _git(repo, "add", "README.md")
    _git(repo, "commit", "-m", "docs")
    docs_head = _git(repo, "rev-parse", "HEAD")
    docs = classifier.classify_git_change(
        repo, base, docs_head, event_name="push"
    )
    assert not any(docs.flags[lane] for lane in classifier.LANES)
    assert docs.reason == "documentation_only"
    with pytest.raises(RuntimeError, match="CI_CHANGE_BASE_UNAVAILABLE"):
        classifier.classify_git_change(
            repo, "0" * 40, docs_head, event_name="push"
        )
    identical = classifier.classify_git_change(
        repo, docs_head, docs_head, event_name="push"
    )
    assert all(identical.flags[lane] for lane in classifier.LANES)
    assert identical.reason == "identical_refs_full_validation"
    assert identical.test_targets == tuple(
        sorted(classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS)
    )

    workflow = repo / ".github/workflows/ci.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text("name: ci\n", encoding="utf-8")
    _git(repo, "add", workflow.relative_to(repo).as_posix())
    _git(repo, "commit", "-m", "change CI topology")
    workflow_head = _git(repo, "rev-parse", "HEAD")
    workflow_change = classifier.classify_git_change(
        repo, docs_head, workflow_head, event_name="push"
    )
    assert all(workflow_change.flags[lane] for lane in classifier.LANES)
    assert workflow_change.reason == "selected_lanes"
    assert workflow_change.test_targets == tuple(
        sorted(classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS)
    )

    source = repo / "engine/db/adapter.py"
    source.parent.mkdir(parents=True)
    (repo / "tests/db").mkdir(parents=True)
    (repo / "tests/db/test_adapter.py").write_text(
        "def test_adapter(): pass\n", encoding="utf-8"
    )
    source.write_text("VALUE = 1\n", encoding="utf-8")
    _git(repo, "add", source.relative_to(repo).as_posix(), "tests/db/test_adapter.py")
    _git(repo, "commit", "-m", "database")
    product_head = _git(repo, "rev-parse", "HEAD")
    product = classifier.classify_git_change(
        repo, workflow_head, product_head, event_name="push"
    )
    assert {lane for lane in classifier.LANES if product.flags[lane]} == {
        "product",
        "db",
        "release",
    }
    assert product.test_targets == ()

    changed_test = repo / "tests/adapter/test_env_guard_prod_variants.py"
    changed_test.parent.mkdir(parents=True)
    changed_test.write_text("def test_guard(): pass\n", encoding="utf-8")
    _git(repo, "add", changed_test.relative_to(repo).as_posix())
    _git(repo, "commit", "-m", "add unlisted adapter regression")
    test_head = _git(repo, "rev-parse", "HEAD")
    changed_test_result = classifier.classify_git_change(
        repo,
        product_head,
        test_head,
        event_name="push",
    )
    assert {
        lane for lane in classifier.LANES if changed_test_result.flags[lane]
    } == {"product", "compat", "release"}
    assert changed_test_result.test_targets == (
        "tests/adapter/test_env_guard_prod_variants.py",
    )

    changed_test.unlink()
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "remove standalone adapter regression")
    deleted_test_head = _git(repo, "rev-parse", "HEAD")
    deleted_test_result = classifier.classify_git_change(
        repo,
        test_head,
        deleted_test_head,
        event_name="push",
    )
    assert {
        lane for lane in classifier.LANES if deleted_test_result.flags[lane]
    } == {"product", "compat", "release"}
    assert deleted_test_result.test_targets == ()

    renamed = repo / "docs/adapter.md"
    renamed.parent.mkdir(exist_ok=True)
    _git(repo, "mv", source.relative_to(repo).as_posix(), renamed.relative_to(repo).as_posix())
    _git(repo, "commit", "-m", "rename source into docs")
    rename_head = _git(repo, "rev-parse", "HEAD")
    rename = classifier.classify_git_change(
        repo, deleted_test_head, rename_head, event_name="push"
    )
    assert {lane for lane in classifier.LANES if rename.flags[lane]} == {
        "product",
        "db",
        "release",
    }
    assert rename.test_targets == ()


def test_pull_request_classification_uses_merge_base_not_base_tip(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    (repo / "README.md").write_text("root\n", encoding="utf-8")
    _git(repo, "add", "README.md")
    _git(repo, "commit", "-m", "root")
    root = _git(repo, "rev-parse", "HEAD")

    _git(repo, "checkout", "-b", "feature")
    feature_doc = repo / "docs/run/feature.md"
    feature_doc.parent.mkdir(parents=True)
    feature_doc.write_text("feature\n", encoding="utf-8")
    _git(repo, "add", "docs/run/feature.md")
    _git(repo, "commit", "-m", "feature docs")
    feature_head = _git(repo, "rev-parse", "HEAD")

    _git(repo, "checkout", "-b", "advanced-main", root)
    base_only = repo / "engine/new_on_main.py"
    base_only.parent.mkdir(parents=True)
    base_only.write_text("VALUE = 1\n", encoding="utf-8")
    _git(repo, "add", "engine/new_on_main.py")
    _git(repo, "commit", "-m", "advance main")
    base_tip = _git(repo, "rev-parse", "HEAD")
    _git(repo, "checkout", "feature")

    pull_request = classifier.classify_git_change(
        repo,
        base_tip,
        feature_head,
        event_name="pull_request",
    )
    assert pull_request.reason == "documentation_only"
    assert not any(pull_request.flags[lane] for lane in classifier.LANES)
    assert pull_request.test_targets == ()

    with pytest.raises(ValueError, match="CI_PRODUCT_OWNER_TEST_MISSING"):
        classifier.classify_git_change(
            repo,
            base_tip,
            feature_head,
            event_name="push",
        )
    with pytest.raises(ValueError, match="CI_CHANGE_EVENT_UNSUPPORTED"):
        classifier.classify_git_change(
            repo,
            root,
            feature_head,
            event_name="workflow_dispatch",
        )


def test_classifier_main_forwards_event_name(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    observed: dict[str, str] = {}

    def fake_classify(repo_root, base, head, *, event_name):
        observed.update(
            repo_root=str(repo_root),
            base=base,
            head=head,
            event_name=event_name,
        )
        return classifier.Classification(
            flags=classifier._empty_flags(),
            reason="documentation_only",
            path_count=1,
        )

    monkeypatch.setattr(classifier, "classify_git_change", fake_classify)
    github_output = tmp_path / "github-output"
    changed_tests = tmp_path / "changed-tests"
    assert classifier.main(
        [
            "--base",
            "1" * 40,
            "--head",
            "2" * 40,
            "--event-name",
            "pull_request",
            "--repo-root",
            str(tmp_path),
            "--github-output",
            str(github_output),
            "--changed-tests-output",
            str(changed_tests),
        ]
    ) == 0
    assert observed == {
        "repo_root": str(tmp_path.resolve()),
        "base": "1" * 40,
        "head": "2" * 40,
        "event_name": "pull_request",
    }


def test_pull_request_classification_fails_without_a_merge_base(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "ci-classifier@example.invalid")
    _git(repo, "config", "user.name", "CI classifier test")
    (repo / "README.md").write_text("first root\n", encoding="utf-8")
    _git(repo, "add", "README.md")
    _git(repo, "commit", "-m", "first root")
    first = _git(repo, "rev-parse", "HEAD")

    _git(repo, "switch", "--orphan", "unrelated")
    (repo / "README.md").unlink(missing_ok=True)
    (repo / "OTHER.md").write_text("second root\n", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "second root")
    second = _git(repo, "rev-parse", "HEAD")

    with pytest.raises(RuntimeError, match="CI_CHANGE_MERGE_BASE_UNAVAILABLE"):
        classifier.classify_git_change(
            repo,
            first,
            second,
            event_name="pull_request",
        )


def test_change_classifier_covers_release_chain_sources_and_outputs() -> None:
    for path in sorted(classifier._RELEASE_IMPLEMENTATION_PATHS):
        assert classifier.classify_paths([path]).flags["release"], path

    commands = [
        command
        for step in release_closure.CLOSURE_STEPS
        for command in (step.write, step.check)
    ] + [
        command
        for step in release_sanity.default_steps()
        for command in step.commands
    ]
    command_paths = {
        argument
        for command in commands
        for argument in command
        if not Path(argument).is_absolute()
        and (ROOT / argument).is_file()
    }
    assert command_paths
    for path in sorted(command_paths):
        assert classifier.classify_paths([path]).flags["release"], path

    consumed = set(attestation.REQUIRED_EVIDENCE) | set(
        release_closure.ATTESTATION_GENERATED_OUTPUTS
    )
    assert consumed
    for path in sorted(consumed):
        assert classifier.classify_paths([path]).flags["release"], path


def test_every_active_workflow_command_input_has_an_applicable_lane() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    command_paths = {
        match
        for match in re.findall(
            r"(?:ci|scripts|tools)/[A-Za-z0-9_./-]+\.(?:py|sh|yml)",
            workflow,
        )
        if (ROOT / match).is_file()
    }
    assert command_paths
    for path in sorted(command_paths):
        result = classifier.classify_paths((path,))
        assert any(result.flags[lane] for lane in classifier.LANES), path


def test_job_definitions_are_reusable_secret_free_and_live_forbidden() -> None:
    expected = ["rails_closed_refusal", "rails_open_conformance", "logs_keys_only_redaction"]
    for path, name in zip(DEFS, expected):
        assert path.exists()
        job = runner.validate(path)
        assert job["name"] == name
        assert "hde-epic031" not in job["scope"].lower()
        assert job["live_vendor_calls"] == "forbidden"
        text = path.read_text(encoding="utf-8").lower()
        assert "${{ secrets." not in text
    open_job = runner.validate(DEFS[1])
    assert "fixture-backed" in open_job["scope"] and "non-live" in open_job["scope"]


def _write_def(path: Path, name: str, safe: str, allow: str, command: str, scope: str = "reusable-fixture-backed-mocked-non-live") -> None:
    path.write_text(
        f'''name: {name}\nrails:\n  SAFE_MODE: "{safe}"\n  ALLOW_NETWORK: "{allow}"\n  LC_ALL: C\n  LANG: C\n  TZ: UTC\nscope: {scope}\nlive_vendor_calls: forbidden\nsteps:\n  - command: {command}\n    proves:\n      - local proof\n''',
        encoding="utf-8",
    )


def test_runner_orders_steps_and_isolates_open_environment(tmp_path: Path) -> None:
    probe = tmp_path / "probe.py"
    out = tmp_path / "out.txt"
    probe.write_text(
        "import os,sys,pathlib\npathlib.Path(sys.argv[1]).open('a').write(sys.argv[2]+':' + os.environ['SAFE_MODE'] + ':' + os.environ['ALLOW_NETWORK'] + '\\n')\n",
        encoding="utf-8",
    )
    a, b, c = tmp_path / "a.yml", tmp_path / "b.yml", tmp_path / "c.yml"
    _write_def(a, "rails_closed_refusal", "1", "0", f"{sys.executable} {probe} {out} closed", "reusable-closed")
    _write_def(b, "rails_open_conformance", "0", "1", f"{sys.executable} {probe} {out} open")
    _write_def(c, "logs_keys_only_redaction", "1", "0", f"{sys.executable} {probe} {out} logs", "reusable-logs")
    old = runner.ALLOWED_ARGV
    try:
        runner.ALLOWED_ARGV = {
            "rails_closed_refusal": (("python", str(probe), str(out), "closed"),),
            "rails_open_conformance": (("python", str(probe), str(out), "open"),),
            "logs_keys_only_redaction": (("python", str(probe), str(out), "logs"),),
        }
        assert runner.main([str(a), str(b), str(c)]) == 0
    finally:
        runner.ALLOWED_ARGV = old
    assert out.read_text(encoding="utf-8").splitlines() == ["closed:1:0", "open:0:1", "logs:1:0"]
    assert os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1"


def test_runner_scrubs_ambient_vendor_credentials_from_child_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for key in runner.CREDENTIAL_ENV_NAMES:
        monkeypatch.setenv(key, f"ambient-{key.lower()}")
    probe = tmp_path / "probe.py"
    out = tmp_path / "out.txt"
    probe.write_text(
        "import os,sys,pathlib\nkeys=sys.argv[2:]\npathlib.Path(sys.argv[1]).write_text('\\n'.join(k for k in keys if os.environ.get(k))+'\\n', encoding='utf-8')\n",
        encoding="utf-8",
    )
    job = {
        "name": "rails_open_conformance",
        "rails": {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"},
        "steps": [{"command": f"{sys.executable} {probe} {out} " + " ".join(sorted(runner.CREDENTIAL_ENV_NAMES))}],
    }

    old = runner.ALLOWED_ARGV
    try:
        runner.ALLOWED_ARGV = {"rails_open_conformance": (("python", str(probe), str(out), *sorted(runner.CREDENTIAL_ENV_NAMES)),)}
        assert runner.run_job(job) == 0
    finally:
        runner.ALLOWED_ARGV = old
    assert out.read_text(encoding="utf-8") == "\n"
    for key in runner.CREDENTIAL_ENV_NAMES:
        assert os.environ[key] == f"ambient-{key.lower()}"


@pytest.mark.parametrize(
    "mutate, expected",
    [
        (lambda s: s.replace("rails_closed_refusal", "unknown_identity"), "unknown"),
        (lambda s: s.replace("reusable-closed", "hde-epic031-pr-01"), "EPIC031"),
        (lambda s: s.replace("live_vendor_calls: forbidden", "live_vendor_calls: allowed"), "live_vendor_calls"),
        (lambda s: s + "secrets:\n  HD_API_KEY: value\n", "credential"),
        (lambda s: s.replace("local proof", "${{ secrets.HD_API_KEY }}"), "secrets"),
        (lambda s: s.replace("steps:\n  - command:", "steps:\n  - nope:"), "step"),
    ],
)
def test_runner_rejects_invalid_definitions(tmp_path: Path, mutate, expected: str) -> None:
    good = '''name: rails_closed_refusal\nrails:\n  SAFE_MODE: "1"\n  ALLOW_NETWORK: "0"\n  LC_ALL: C\n  LANG: C\n  TZ: UTC\nscope: reusable-closed\nlive_vendor_calls: forbidden\nsteps:\n  - command: python -c 'print("ok")'\n    proves:\n      - local proof\n'''
    bad = tmp_path / "bad.yml"
    bad.write_text(mutate(good), encoding="utf-8")
    with pytest.raises(Exception) as excinfo:
        runner.validate(bad)
    assert expected.lower() in str(excinfo.value).lower()


def test_runner_rejects_duplicate_and_stops_on_failure(tmp_path: Path) -> None:
    a, b = tmp_path / "a.yml", tmp_path / "b.yml"
    _write_def(a, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'raise SystemExit(3)'", "reusable-closed")
    _write_def(b, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'print(1)'", "reusable-closed")
    old = runner.ALLOWED_ARGV
    try:
        runner.ALLOWED_ARGV = {"rails_closed_refusal": (("python", "-c", "raise SystemExit(3)"), ("python", "-c", "print(1)"))}
        assert runner.main([str(a), str(b)]) == 2
        c, d = tmp_path / "c.yml", tmp_path / "d.yml"
        _write_def(c, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'raise SystemExit(3)'", "reusable-closed")
        _write_def(d, "rails_open_conformance", "0", "1", f"{sys.executable} -c 'print(1)'")
        assert runner.run_job(runner.validate(c)) == 3
    finally:
        runner.ALLOWED_ARGV = old


def test_producer_check_mode_does_not_modify_files_or_repo_paths() -> None:
    paths = [ROOT / producer.OPS_REFUSAL_REL, ROOT / producer.RETRY_AFTER_REL, ROOT / producer.KEYS_ONLY_REL]
    before = {p: p.read_bytes() for p in paths if p.exists()}
    state_before = _repo_state()
    producer.generate(check=True)
    after = {p: p.read_bytes() for p in paths if p.exists()}
    state_after = _repo_state()
    assert before == after
    assert state_before == state_after
    assert not (ROOT / ".rails_gate_keys_only.tmp").exists()


def test_producer_validation_failure_leaves_existing_output_unchanged(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    target = tmp_path / "sample.txt"
    target.write_text("original\n", encoding="utf-8")
    monkeypatch.setattr(producer, "KEYS_ONLY_REL", str(target.relative_to(ROOT)) if target.is_relative_to(ROOT) else producer.KEYS_ONLY_REL)
    monkeypatch.setattr(producer, "expected_outputs", lambda: (_ for _ in ()).throw(SystemExit("boom")))
    with pytest.raises(SystemExit):
        producer.generate(check=False)
    assert target.read_text(encoding="utf-8") == "original\n"


def test_refusal_proof_forces_closed_env_without_leaking(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    text = producer.build_ops_refusal()
    assert "x-rails-mode: closed" in text
    assert "rails remain closed" in text
    assert os.environ["SAFE_MODE"] == "0"
    assert os.environ["ALLOW_NETWORK"] == "1"


def test_rails_keys_only_uses_dedicated_vendor_artifact_path() -> None:
    assert producer.KEYS_ONLY_REL == "artifacts/vendor/rails_gate_keys_only.logs.sample"
    assert producer.KEYS_ONLY_REL != "artifacts/bodygraph/keys_only.logs.sample"
    assert (ROOT / "scripts/bodygraph/run_refresh_worker.py").read_text(encoding="utf-8").find("artifacts/bodygraph/keys_only.logs.sample") > -1


def test_fixture_backed_open_rails_tests_do_not_reach_real_network() -> None:
    child_env = os.environ.copy()
    for key in runner.CREDENTIAL_ENV_NAMES:
        child_env.pop(key, None)
    child_env.update(
        {
            "SAFE_MODE": "0",
            "ALLOW_NETWORK": "1",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        }
    )
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/bodygraph/test_vendor_client.py", "-q"],
        cwd=ROOT,
        env=child_env,
        text=True,
        capture_output=True,
        timeout=120,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_runner_rejects_credential_bearing_command_forms(tmp_path: Path) -> None:
    bad_forms = [
        "HD_API_KEY=value python -m pytest tests/bodygraph/test_vendor_client.py -q",
        "env HD_API_KEY=value python -m pytest tests/bodygraph/test_vendor_client.py -q",
        "python -m pytest tests/bodygraph/test_vendor_client.py -q --hd-api-key value",
        "python -m pytest tests/bodygraph/test_vendor_client.py -q --HD_API_BASE_URL=https://example.invalid",
        "python -m pytest tests/bodygraph/test_vendor_client.py -q TOKEN=value",
    ]
    for idx, command in enumerate(bad_forms):
        path = tmp_path / f"bad{idx}.yml"
        _write_def(path, "rails_open_conformance", "0", "1", command)
        with pytest.raises(Exception) as excinfo:
            runner.validate(path)
        assert "credential" in str(excinfo.value).lower() or "env wrapper" in str(excinfo.value).lower()


def test_runner_rejects_non_allowlisted_command_vectors(tmp_path: Path) -> None:
    path = tmp_path / "bad.yml"
    _write_def(path, "rails_open_conformance", "0", "1", "python -c 'print(1)'")
    with pytest.raises(Exception) as excinfo:
        runner.validate(path)
    assert "allowlisted" in str(excinfo.value).lower()


def test_runner_accepts_exact_current_allowlist() -> None:
    for path in DEFS:
        job = runner.validate(path)
        for step in job["steps"]:
            argv = runner.shlex.split(step["command"])
            runner._validate_allowed_argv(job["name"], argv)


def test_feature_producers_do_not_reference_path_proof_writer() -> None:
    rails_text = (ROOT / "tools/evidence/generate_rails_gate_evidence.py").read_text(encoding="utf-8")
    open_text = (ROOT / "tools/evidence/generate_open_rails_abba_proof.py").read_text(encoding="utf-8")
    for text in (rails_text, open_text):
        assert "_write_path_proof" not in text
        assert "INDEX.sha256" not in text
        assert "evidence_index.jsonl" not in text


def test_open_rails_producer_check_mode_has_no_repo_residue() -> None:
    from tools.evidence import generate_open_rails_abba_proof as open_proof

    state_before = _repo_state()
    assert open_proof.main(["--check-current"]) == 0
    state_after = _repo_state()
    assert state_before == state_after
