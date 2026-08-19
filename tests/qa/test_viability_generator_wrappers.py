"""Regression guards for the thin, read-only EPIC027/028/029 wrappers."""

from __future__ import annotations

import ast
from collections.abc import Iterator
from copy import deepcopy
from pathlib import Path

import pytest

from tools.qa import qa_harness
from tools.qa import generate_epic027_close_pack as epic027
from tools.qa import generate_epic028_acceptance_ledger as epic028_ledger
from tools.qa import generate_epic028_close_pack as epic028_close
from tools.qa import generate_epic029_close_pack as epic029

ADAPTERS = (epic027, epic028_ledger, epic028_close, epic029)
VIABILITY_ADAPTERS = (epic027, epic028_ledger, epic029)

FORBIDDEN_IMPORT_ROOTS = frozenset(
    {
        "subprocess",
        "tempfile",
        "tools.evidence",
    }
)
FORBIDDEN_IO_CALLS = frozenset(
    {
        "mkdir",
        "open",
        "read_bytes",
        "read_text",
        "rename",
        "replace",
        "rmdir",
        "touch",
        "unlink",
        "write_bytes",
        "write_text",
    }
)
ALLOWED_HARNESS_CALLS = frozenset(
    {
        "HarnessConfig",
        "generate_acceptance_map_viability",
        "require_disjoint_repository_root",
        "require_frozen_evidence",
        "require_governed_viability",
        "run_free_close_manifest_payload",
    }
)
FORBIDDEN_MANIFEST_KEYS = frozenset(
    {
        "ops_task_id",
        "pf09_scope",
        "pf09_subtask_id",
        "pf09_task_id",
        "qa_summary_lines",
        "run_id",
        "status",
    }
)


def _source_tree(module: object) -> ast.Module:
    path = Path(module.__file__)
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _mapping_by_name(module: object) -> dict[str, dict[str, object]]:
    return {row["name"]: row for row in module.TOKEN_EVIDENCE_MAPPINGS}


def _nested_keys(value: object) -> Iterator[str]:
    if isinstance(value, dict):
        for key, nested in value.items():
            yield str(key)
            yield from _nested_keys(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            yield from _nested_keys(nested)


@pytest.mark.parametrize("module", ADAPTERS, ids=lambda module: module.EPIC_ID)
def test_adapters_do_not_own_execution_or_publication(module: object) -> None:
    tree = _source_tree(module)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported = {alias.name for alias in node.names}
            assert not any(
                name == root or name.startswith(f"{root}.")
                for name in imported
                for root in FORBIDDEN_IMPORT_ROOTS
            )
        elif isinstance(node, ast.ImportFrom):
            imported_from = node.module or ""
            assert not any(
                imported_from == root or imported_from.startswith(f"{root}.")
                for root in FORBIDDEN_IMPORT_ROOTS
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            assert not node.name.startswith(("_execute", "_publish", "_write"))
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                assert node.func.id not in FORBIDDEN_IO_CALLS
            elif isinstance(node.func, ast.Attribute):
                assert node.func.attr not in FORBIDDEN_IO_CALLS
                if (
                    isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "qa_harness"
                ):
                    assert node.func.attr in ALLOWED_HARNESS_CALLS


@pytest.mark.parametrize("module", ADAPTERS, ids=lambda module: module.EPIC_ID)
def test_default_entrypoints_only_verify_frozen_evidence(
    monkeypatch: pytest.MonkeyPatch,
    module: object,
) -> None:
    calls: list[tuple[str, object]] = []

    monkeypatch.setattr(
        module,
        "ensure_determinism_env",
        lambda: calls.append(("determinism", None)),
    )
    monkeypatch.setattr(
        module.qa_harness,
        "require_frozen_evidence",
        lambda root: calls.append(("frozen", root)),
    )
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda *args, **kwargs: pytest.fail("default entrypoint executed viability"),
    )

    assert module.main() == 0
    assert calls == [("determinism", None), ("frozen", module.ROOT)]


@pytest.mark.parametrize(
    "module,number",
    ((epic027, "027"), (epic028_ledger, "028"), (epic029, "029")),
    ids=lambda value: getattr(value, "EPIC_ID", str(value)),
)
def test_viability_requires_explicit_disjoint_repository(
    tmp_path: Path,
    module: object,
    number: str,
) -> None:
    with pytest.raises(ValueError, match="explicit isolated repo_root"):
        module.viability_config()
    with pytest.raises(ValueError, match="disjoint"):
        module.viability_config(repo_root=module.ROOT)

    config = module.viability_config(repo_root=tmp_path)
    assert config.repo_root == tmp_path.resolve()
    assert config.qa_root == tmp_path / "audit" / "qa" / f"hde-epic{number}"
    assert config.acceptance_map_path == (
        tmp_path / "docs" / f"acceptance_map_epic{number}.json"
    )


@pytest.mark.parametrize("module", VIABILITY_ADAPTERS, ids=lambda module: module.EPIC_ID)
def test_viability_rejects_invalid_root_before_env_execution_or_publication(
    monkeypatch: pytest.MonkeyPatch,
    module: object,
) -> None:
    actions: list[str] = []

    def forbidden(name: str):
        def call(*_args, **_kwargs):
            actions.append(name)
            raise AssertionError(f"crossed {name} boundary")

        return call

    monkeypatch.setattr(module, "ensure_determinism_env", forbidden("environment"))
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        forbidden("viability"),
    )
    monkeypatch.setattr(
        module.qa_harness,
        "require_governed_viability",
        forbidden("publication"),
    )

    with pytest.raises(ValueError, match="explicit isolated repo_root"):
        module.run_viability()
    with pytest.raises(ValueError, match="repository disjoint"):
        module.run_viability(repo_root=module.ROOT)
    assert actions == []


@pytest.mark.parametrize("module", VIABILITY_ADAPTERS, ids=lambda module: module.EPIC_ID)
def test_viability_is_only_a_generic_harness_delegation(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    module: object,
) -> None:
    marker = object()
    calls: list[tuple[str, object]] = []

    monkeypatch.setattr(
        module,
        "ensure_determinism_env",
        lambda: calls.append(("determinism", None)),
    )

    def generate(config: object, *, publish_governed_ledger: bool) -> object:
        assert config.repo_root == tmp_path.resolve()
        assert publish_governed_ledger is True
        calls.append(("generate", config))
        return marker

    def require(result: object, path: Path) -> object:
        assert result is marker
        assert path == (
            tmp_path
            / "audit"
            / "qa"
            / module.EPIC_SLUG
            / "acceptance_map_viability.log"
        )
        calls.append(("require", path))
        return path

    monkeypatch.setattr(module.qa_harness, "generate_acceptance_map_viability", generate)
    monkeypatch.setattr(module.qa_harness, "require_governed_viability", require)

    assert module.run_viability(repo_root=tmp_path) is marker
    assert [name for name, _ in calls] == ["determinism", "generate", "require"]


@pytest.mark.parametrize(
    "module",
    (epic027, epic028_ledger, epic029),
    ids=lambda module: module.EPIC_ID,
)
def test_locator_mappings_make_no_status_claims(module: object) -> None:
    for row in module.TOKEN_EVIDENCE_MAPPINGS:
        assert set(row) == {
            "ci_tests_jobs",
            "evidence_titles",
            "name",
            "owner_pf",
            "qa_root_logs",
        }
        assert not (set(_nested_keys(row)) & FORBIDDEN_MANIFEST_KEYS)


def test_corrected_locator_mappings_are_retained() -> None:
    epic027_rows = _mapping_by_name(epic027)
    assert epic027_rows["CLI_READER_PARITY_OK"]["evidence_titles"] == (
        "artifacts/cli/reader_dump.json",
        "artifacts/cli/reader_cli_parity.bytes",
    )

    epic028_rows = _mapping_by_name(epic028_ledger)
    assert epic028_rows["PREFS_KEYSET_10_OK"]["evidence_titles"] == (
        "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log",
        "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
    )
    assert "test_viewer_prefs_require_exact_magic10_weight_keys" in str(
        epic028_rows["PREFS_KEYSET_10_OK"]["ci_tests_jobs"]
    )

    epic029_rows = _mapping_by_name(epic029)
    assert epic029_rows["TESTS_PASS_OK"]["evidence_titles"] == (
        "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log",
    )
    assert epic029_rows["TESTS_PASS_OK"]["ci_tests_jobs"] == (
        "read-only historical receipt; no execution"
    )


def test_run_free_close_manifest_payloads_make_no_status_or_pf09_claims() -> None:
    timestamp = "2026-08-19T00:00:00Z"
    flat_manifest = {
        "a-check": {
            "check_id": "a-check",
            "log_path": "checks/a-check/primary.log",
            "status": "PASS",
        }
    }
    original = deepcopy(flat_manifest)
    payloads = (
        epic027.close_manifest_payload(timestamp),
        epic028_close.close_manifest_payload(timestamp, flat_manifest),
        epic029.close_manifest_payload(timestamp),
    )

    assert flat_manifest == original
    for payload in payloads:
        assert payload["captured_at_utc"] == timestamp
        assert payload["scope"] == "read_only_reference_only"
        assert not (set(_nested_keys(payload)) & FORBIDDEN_MANIFEST_KEYS)


@pytest.mark.parametrize(
    "module",
    (epic027, epic028_close, epic029),
    ids=lambda module: module.EPIC_ID,
)
def test_close_manifest_construction_is_one_generic_delegation(
    module: object,
) -> None:
    tree = _source_tree(module)
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "close_manifest_payload"
    )
    calls = [node for node in ast.walk(function) if isinstance(node, ast.Call)]
    assert len(calls) == 1
    call = calls[0]
    assert isinstance(call.func, ast.Attribute)
    assert isinstance(call.func.value, ast.Name)
    assert call.func.value.id == "qa_harness"
    assert call.func.attr == "run_free_close_manifest_payload"


def test_epic028_manifest_helper_preserves_flat_check_keying() -> None:
    checks = {
        "a-check": {
            "check_id": "a-check",
            "log_path": "checks/a-check/primary.log",
            "status": "PASS",
        },
        "b-check": {
            "check_id": "b-check",
            "log_path": "checks/b-check/primary.log",
            "status": "PASS",
        },
    }
    assert qa_harness.close_manifest_checks(checks) is checks
    assert epic028_close.close_manifest_payload("2026-08-19T00:00:00Z", checks)[
        "qa_step_count"
    ] == 2
    with pytest.raises(ValueError, match="QA_STEP_MANIFEST_CHECKS_INVALID"):
        qa_harness.close_manifest_checks({"checks": []})
    with pytest.raises(ValueError, match="QA_STEP_MANIFEST_CHECKS_INVALID"):
        qa_harness.close_manifest_checks({"checks": checks})


def test_run_free_close_manifest_rejects_impossible_timestamp() -> None:
    with pytest.raises(ValueError, match="valid UTC timestamp"):
        qa_harness.run_free_close_manifest_payload(
            epic027.EPIC_ID,
            "2026-99-99T99:99:99Z",
            epic027.CLOSE_KEY_OUTPUTS,
        )
