from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from tools.qa import epic021_qa, qa_harness


def _inventory_payload(
    *,
    restore_files: dict[str, str],
    drift_files: dict[str, str],
    delete_paths: list[str],
    authorized_paths: list[str],
    transient_paths: list[str] | None = None,
    companion_paths: list[str] | None = None,
) -> dict[str, object]:
    transient_paths = [] if transient_paths is None else transient_paths
    companion_paths = [] if companion_paths is None else companion_paths
    net_paths = (
        len(restore_files)
        + len(drift_files)
        + len(delete_paths)
        + len(authorized_paths)
        + len(companion_paths)
    )
    return {
        "schema_version": "1.0",
        "purpose": "test fixture",
        "baseline_commit": "1" * 40,
        "reviewed_current_commit": "2" * 40,
        "classification_counts": {
            "lineage_artifact_paths": net_paths + len(transient_paths),
            "net_artifact_paths": net_paths,
            "frozen_historical_paths": (
                len(restore_files) + len(delete_paths) + len(transient_paths)
            ),
            "frozen_restore_files": len(restore_files),
            "frozen_delete_paths": len(delete_paths),
            "transient_absent_paths": len(transient_paths),
            "unrelated_drift_restore_files": len(drift_files),
            "authorized_current_state_paths": len(authorized_paths),
            "index_mirror_companion_paths": len(companion_paths),
        },
        "frozen_historical": {
            "restore_files": restore_files,
            "delete_paths": delete_paths,
            "transient_absent_paths": transient_paths,
        },
        "unrelated_drift": {"restore_files": drift_files},
        "authorized_current_state_paths": authorized_paths,
        "index_mirror_companion_paths": companion_paths,
    }


def _write_inventory(path: Path, payload: dict[str, object]) -> None:
    path.write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def _file_snapshot(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def test_disjoint_repository_guard_rejects_every_overlap_and_alias(
    tmp_path: Path,
) -> None:
    protected = tmp_path / "checkout"
    protected.mkdir()
    descendant = protected / "nested"
    descendant.mkdir()
    sibling = tmp_path / "fixture"
    sibling.mkdir()
    alias = tmp_path / "checkout-alias"
    alias.symlink_to(protected, target_is_directory=True)

    for candidate in (protected, descendant, tmp_path, alias):
        with pytest.raises(ValueError, match="repository disjoint"):
            qa_harness.require_disjoint_repository_root(
                candidate,
                protected_root=protected,
            )

    assert (
        qa_harness.require_disjoint_repository_root(
            sibling,
            protected_root=protected,
        )
        == sibling.resolve()
    )


def test_epic021_rejects_checkout_before_env_execution_or_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    protected = tmp_path / "checkout"
    protected.mkdir()
    monkeypatch.setattr(epic021_qa, "ROOT", protected)
    actions: list[str] = []

    def forbidden(name: str):
        def call(*_args, **_kwargs):
            actions.append(name)
            raise AssertionError(f"crossed {name} boundary")

        return call

    monkeypatch.setattr(
        epic021_qa,
        "ensure_determinism_env",
        forbidden("environment"),
    )
    monkeypatch.setattr(
        qa_harness,
        "run_pytest_check",
        forbidden("pytest"),
    )
    monkeypatch.setattr(qa_harness, "record_check", forbidden("publication"))
    monkeypatch.setattr(
        qa_harness,
        "generate_acceptance_map_viability",
        forbidden("viability"),
    )

    with pytest.raises(ValueError, match="repository disjoint"):
        epic021_qa.run_epic021_qa(repo_root=protected)
    assert actions == []


def test_epic021_requires_explicit_root_before_any_action(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    actions: list[str] = []
    monkeypatch.setattr(
        epic021_qa,
        "ensure_determinism_env",
        lambda: actions.append("environment"),
    )

    with pytest.raises(ValueError, match="explicit isolated repo_root"):
        epic021_qa.run_epic021_qa()
    assert actions == []


def test_epic021_delegates_only_bootstrap_and_viability_to_generic_harness(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    protected = tmp_path / "checkout"
    protected.mkdir()
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    monkeypatch.setattr(epic021_qa, "ROOT", protected)
    events: list[tuple[object, ...]] = []

    monkeypatch.setattr(
        epic021_qa,
        "ensure_determinism_env",
        lambda: events.append(("environment",)),
    )

    bootstrap = qa_harness.CheckResult(
        check_id=epic021_qa.BOOTSTRAP_CHECK_ID,
        status=qa_harness.Status.PASS,
    )

    def run_pytest(config, check_id, pytest_args, **kwargs):
        events.append(
            (
                "pytest",
                config.repo_root,
                config.qa_root,
                check_id,
                tuple(pytest_args),
                kwargs,
            )
        )
        return bootstrap

    bootstrap_log = (
        fixture
        / "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log"
    )
    manifest = fixture / "audit/qa/hde-epic021/qa_step_logs_manifest.json"

    def record_check(config, result, **kwargs):
        events.append(("record", config.repo_root, result, kwargs))
        return bootstrap_log, manifest

    ledger = fixture / "audit/qa/hde-epic021/acceptance_map_viability.log"
    viability = qa_harness.ViabilityResult(
        qa_harness.Status.PASS,
        "",
        fixture
        / "audit/qa/hde-epic021/checks/acceptance-map-viability/primary.log",
        manifest,
        ledger,
        {},
    )

    def generate(config, **kwargs):
        events.append(("viability", config.repo_root, kwargs))
        return viability

    def require(result, expected):
        events.append(("require", result, expected))
        return ledger

    monkeypatch.setattr(qa_harness, "run_pytest_check", run_pytest)
    monkeypatch.setattr(qa_harness, "record_check", record_check)
    monkeypatch.setattr(qa_harness, "generate_acceptance_map_viability", generate)
    monkeypatch.setattr(qa_harness, "require_governed_viability", require)

    result = epic021_qa.run_epic021_qa(repo_root=fixture)

    assert result == {
        "bootstrap": bootstrap,
        "bootstrap_log": bootstrap_log,
        "manifest": manifest,
        "viability": viability,
        "governed_ledger": ledger,
    }
    assert [event[0] for event in events] == [
        "environment",
        "pytest",
        "record",
        "viability",
        "require",
    ]
    pytest_event = events[1]
    assert pytest_event[1] == fixture.resolve()
    assert pytest_event[2] == fixture / "audit/qa/hde-epic021"
    assert pytest_event[3:5] == (
        "d00-bootstrap",
        ("-q", "tests/qa/test_epic021_scaffolding.py"),
    )
    assert events[2][3] == {
        "supersede_check_ids": ("D00_bootstrap",),
    }
    assert events[3][2] == {"publish_governed_ledger": True}
    assert {status.value for status in qa_harness.Status} == {
        "PASS",
        "FAIL_BEHAVIOR",
        "FAIL_TOOLING",
        "TOOLING_BLOCKED",
        "PARKED",
    }


def test_epic021_module_has_only_a_thin_non_live_qa_surface() -> None:
    source = Path(epic021_qa.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)

    assert {
        node.name for node in tree.body if isinstance(node, ast.FunctionDef)
    } == {"run_epic021_qa", "main"}
    assert not any(isinstance(node, ast.ClassDef) for node in tree.body)
    for forbidden in (
        "LIVE_QA_TESTS",
        "po-epic021-live-qa",
        "_live_qa_result",
        "_write_close_pack",
        "_write_graph",
        "subprocess",
        "orientation_demo",
        "update_evidence_index",
    ):
        assert forbidden not in source


def test_epic021_main_only_validates_env_and_frozen_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "checkout"
    root.mkdir()
    monkeypatch.setattr(epic021_qa, "ROOT", root)
    events: list[tuple[str, object]] = []
    monkeypatch.setattr(
        epic021_qa,
        "ensure_determinism_env",
        lambda: events.append(("environment", root)),
    )
    monkeypatch.setattr(
        qa_harness,
        "require_frozen_evidence",
        lambda candidate: events.append(("frozen", candidate)),
    )
    monkeypatch.setattr(
        epic021_qa,
        "run_epic021_qa",
        lambda **_kwargs: (_ for _ in ()).throw(
            AssertionError("main attempted QA execution")
        ),
    )

    assert epic021_qa.main() == 0
    assert events == [("environment", root), ("frozen", root)]


def test_frozen_evidence_guard_is_exact_read_only_and_causal(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    historical = root / "audit/historical.log"
    historical.parent.mkdir()
    historical.write_bytes(b"historical bytes\n")
    drift = root / "artifacts/drift.json"
    drift.parent.mkdir()
    drift.write_bytes(b"{}\n")
    inventory_path = tmp_path / "inventory.json"
    payload = _inventory_payload(
        restore_files={
            "audit/historical.log": qa_harness._git_blob_sha1(
                historical.read_bytes()
            )
        },
        drift_files={
            "artifacts/drift.json": qa_harness._git_blob_sha1(drift.read_bytes())
        },
        delete_paths=["audit/forbidden.log"],
        authorized_paths=["docs/current.json"],
    )
    _write_inventory(inventory_path, payload)
    before = _file_snapshot(root)

    assert (
        qa_harness.frozen_evidence_violations(
            root,
            inventory_path=inventory_path,
        )
        == ()
    )
    qa_harness.require_frozen_evidence(
        root,
        inventory_path=inventory_path,
    )
    assert _file_snapshot(root) == before

    historical.write_bytes(b"rewritten bytes\n")
    violations = qa_harness.frozen_evidence_violations(
        root,
        inventory_path=inventory_path,
    )
    assert len(violations) == 1
    assert violations[0].startswith("audit/historical.log: expected Git blob ")

    historical.write_bytes(b"historical bytes\n")
    forbidden = root / "audit/forbidden.log"
    forbidden.write_bytes(b"new output\n")
    violations = qa_harness.frozen_evidence_violations(
        root,
        inventory_path=inventory_path,
    )
    assert violations == ("audit/forbidden.log: baseline-absent path exists",)


def test_frozen_inventory_rejects_overlap_duplicates_and_count_drift(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    target = root / "audit/historical.log"
    target.parent.mkdir()
    target.write_bytes(b"bytes\n")
    inventory_path = tmp_path / "inventory.json"
    baseline = _inventory_payload(
        restore_files={
            "audit/historical.log": qa_harness._git_blob_sha1(target.read_bytes())
        },
        drift_files={},
        delete_paths=[],
        authorized_paths=[],
    )

    overlap = json.loads(json.dumps(baseline))
    overlap["authorized_current_state_paths"] = ["audit/historical.log"]
    overlap["classification_counts"]["authorized_current_state_paths"] = 1
    overlap["classification_counts"]["net_artifact_paths"] = 2
    overlap["classification_counts"]["lineage_artifact_paths"] = 2
    _write_inventory(inventory_path, overlap)
    with pytest.raises(ValueError, match="classifications overlap"):
        qa_harness.frozen_evidence_violations(
            root,
            inventory_path=inventory_path,
        )

    duplicate = json.loads(json.dumps(baseline))
    duplicate["frozen_historical"]["delete_paths"] = [
        "audit/absent.log",
        "audit/absent.log",
    ]
    duplicate["classification_counts"]["frozen_delete_paths"] = 2
    duplicate["classification_counts"]["frozen_historical_paths"] = 3
    duplicate["classification_counts"]["net_artifact_paths"] = 3
    duplicate["classification_counts"]["lineage_artifact_paths"] = 3
    _write_inventory(inventory_path, duplicate)
    with pytest.raises(ValueError, match="duplicate paths"):
        qa_harness.frozen_evidence_violations(
            root,
            inventory_path=inventory_path,
        )

    count_drift = json.loads(json.dumps(baseline))
    count_drift["classification_counts"]["frozen_restore_files"] = 2
    _write_inventory(inventory_path, count_drift)
    with pytest.raises(ValueError, match="classification counts disagree"):
        qa_harness.frozen_evidence_violations(
            root,
            inventory_path=inventory_path,
        )

    path_escape = json.loads(json.dumps(baseline))
    path_escape["frozen_historical"]["restore_files"] = {
        "audit/../outside.log": "0" * 40,
    }
    _write_inventory(inventory_path, path_escape)
    with pytest.raises(ValueError, match="invalid path"):
        qa_harness.frozen_evidence_violations(
            root,
            inventory_path=inventory_path,
        )


def test_checked_in_frozen_inventory_matches_exact_checkout_bytes() -> None:
    assert qa_harness.frozen_evidence_violations(epic021_qa.ROOT) == ()
