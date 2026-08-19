import importlib
import json
from pathlib import Path

import pytest

from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, ViabilityResult, record_check


MODULES = (
    "tools.qa.generate_epic027_close_pack",
    "tools.qa.generate_epic028_acceptance_ledger",
    "tools.qa.generate_epic029_close_pack",
)


def _write_fixture_paths(root: Path, relative_paths: set[str]) -> None:
    for relative_path in relative_paths:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n", encoding="utf-8")


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_binds_verified_returned_ledger(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        json.dumps({"epic_id": module.EPIC_ID, "status": "PASS", "status_reason": "", "token_status": {}}) + "\n",
        encoding="utf-8",
    )
    config = HarnessConfig(module.EPIC_ID, repo_root=tmp_path)
    primary, manifest = record_check(
        config,
        CheckResult(
            "acceptance-map-viability",
            Status.PASS,
            command=("fixture-check",),
            command_provenance="Explicitly created",
            exit_code=0,
            evidence_artifacts=(
                f"audit/qa/hde-epic{number}/acceptance_map_viability.log",
            ),
        ),
    )
    result = ViabilityResult(Status.PASS, "", primary, manifest, ledger, {})
    calls = []
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: calls.append((config, kwargs)) or result,
    )
    module._write_viability_log()
    assert calls[0][1] == {"publish_governed_ledger": True}


@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize("status", [Status.FAIL_BEHAVIOR, Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.PARKED])
def test_generator_wrapper_stops_on_every_non_pass(
    module_name: str, status: Status, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(status, "blocked", None, None, None, {}),
    )
    with pytest.raises(SystemExit, match=f"ACCEPTANCE_MAP_VIABILITY_{status.value}"):
        module._write_viability_log()


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_rejects_stale_or_mismatched_ledger(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(json.dumps({"epic_id": "HDE-EPIC999", "status": "PASS"}) + "\n", encoding="utf-8")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(Status.PASS, "", tmp_path / "primary", tmp_path / "manifest", ledger, {}),
    )
    with pytest.raises(SystemExit, match="STALE_OR_MISMATCHED"):
        module._write_viability_log()


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_rejects_missing_pass_outputs(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(Status.PASS, "", None, None, None, {}),
    )
    with pytest.raises(SystemExit, match="LEDGER_MISMATCH"):
        module._write_viability_log()


def _epic028_result(tmp_path: Path) -> ViabilityResult:
    qa_root = tmp_path / "audit/qa/hde-epic028"
    return ViabilityResult(
        Status.PASS,
        "",
        qa_root / "checks/acceptance-map-viability/primary.log",
        qa_root / "qa_step_logs_manifest.json",
        qa_root / "acceptance_map_viability.log",
        {},
    )


def _configure_epic028_publication_paths(module, tmp_path: Path, monkeypatch) -> None:
    qa_root = tmp_path / "audit/qa/hde-epic028"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "QA_ROOT", qa_root)
    monkeypatch.setattr(
        module,
        "ACCEPTANCE_MAP_PATH",
        tmp_path / "docs/acceptance_map_epic028.json",
    )
    monkeypatch.setattr(
        module,
        "TOKEN_MATRIX_PATH",
        qa_root / "token_evidence_matrix.md",
    )
    monkeypatch.setattr(
        module,
        "VIABILITY_LOG_PATH",
        qa_root / "acceptance_map_viability.log",
    )


def test_epic028_refreshes_all_proofs_before_index_write_and_check(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    _configure_epic028_publication_paths(module, tmp_path, monkeypatch)
    result = _epic028_result(tmp_path)
    events = []

    monkeypatch.setattr(
        module,
        "_write_path_proof",
        lambda path, produced_at: events.append(("proof", path, produced_at)),
    )
    monkeypatch.setattr(
        module.update_evidence_index,
        "main",
        lambda argv: events.append(("updater", tuple(argv))),
    )
    monkeypatch.setattr(
        module,
        "_run_final_mirror_schema_check",
        lambda: events.append(("mirror-schema", module.FINAL_MIRROR_SCHEMA_COMMAND)),
    )

    module._refresh_governed_bindings(result, "2026-08-18T00:00:00Z")

    assert events == [
        ("proof", module.ACCEPTANCE_MAP_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.TOKEN_MATRIX_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.VIABILITY_LOG_PATH, "2026-08-18T00:00:00Z"),
        ("proof", result.primary_log, "2026-08-18T00:00:00Z"),
        ("proof", result.manifest, "2026-08-18T00:00:00Z"),
        ("updater", ()),
        ("updater", ("--check",)),
        ("mirror-schema", module.FINAL_MIRROR_SCHEMA_COMMAND),
    ]


def test_epic028_stale_index_check_cannot_report_success(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    _configure_epic028_publication_paths(module, tmp_path, monkeypatch)
    result = _epic028_result(tmp_path)
    updater_calls = []
    mirror_calls = []
    monkeypatch.setattr(module, "_write_path_proof", lambda path, produced_at: None)
    monkeypatch.setattr(
        module,
        "_run_final_mirror_schema_check",
        lambda: mirror_calls.append(module.FINAL_MIRROR_SCHEMA_COMMAND),
    )

    def stale_check(argv):
        updater_calls.append(tuple(argv))
        if argv == ["--check"]:
            raise SystemExit("STALE:artifacts/evidence_index.jsonl")

    monkeypatch.setattr(module.update_evidence_index, "main", stale_check)

    with pytest.raises(SystemExit, match="STALE:artifacts/evidence_index.jsonl"):
        module._refresh_governed_bindings(result, "2026-08-18T00:00:00Z")

    assert updater_calls == [(), ("--check",)]
    assert mirror_calls == []


def test_epic028_final_mirror_schema_uses_exact_non_shell_argv(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    calls = []

    def run(command, **kwargs):
        calls.append((command, kwargs))
        return module.subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(module.subprocess, "run", run)

    module._run_final_mirror_schema_check()

    assert calls == [
        (
            (
                "ci/checks/check_mirror_schema.sh",
                "artifacts/evidence_index.jsonl",
            ),
            {
                "cwd": tmp_path,
                "text": True,
                "capture_output": True,
                "check": False,
                "shell": False,
            },
        )
    ]


def test_epic028_final_mirror_schema_failure_is_fatal(
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda command, **kwargs: module.subprocess.CompletedProcess(
            command, 1, "", "invalid mirror"
        ),
    )

    with pytest.raises(SystemExit, match="FINAL_MIRROR_SCHEMA_FAILED:1"):
        module._run_final_mirror_schema_check()


@pytest.mark.parametrize(
    "status",
    [Status.FAIL_BEHAVIOR, Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.PARKED],
)
def test_epic028_main_stops_before_proof_or_index_work_on_non_pass(
    status: Status,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    _configure_epic028_publication_paths(module, tmp_path, monkeypatch)
    downstream_calls = []
    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(
            status,
            "blocked",
            None,
            None,
            None,
            {},
        ),
    )
    monkeypatch.setattr(
        module,
        "_write_path_proof",
        lambda path, produced_at: downstream_calls.append(("proof", path)),
    )
    monkeypatch.setattr(
        module.update_evidence_index,
        "main",
        lambda argv: downstream_calls.append(("updater", tuple(argv))),
    )
    monkeypatch.setattr(
        module,
        "_run_final_mirror_schema_check",
        lambda: downstream_calls.append(("mirror-schema",)),
    )

    with pytest.raises(SystemExit, match=f"ACCEPTANCE_MAP_VIABILITY_{status.value}"):
        module.main()

    assert downstream_calls == []


def _epic027_result(tmp_path: Path) -> ViabilityResult:
    qa_root = tmp_path / "audit/qa/hde-epic027"
    return ViabilityResult(
        Status.PASS,
        "",
        qa_root / "checks/acceptance-map-viability/primary.log",
        qa_root / "qa_step_logs_manifest.json",
        qa_root / "acceptance_map_viability.log",
        {},
    )


def _epic027_gate_primaries(tmp_path: Path) -> tuple[Path, ...]:
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    qa_root = tmp_path / "audit/qa/hde-epic027/checks"
    return tuple(qa_root / check_id / "primary.log" for check_id in module.GATE_CHECK_IDS)


def _configure_epic027_publication_paths(module, tmp_path: Path, monkeypatch) -> None:
    qa_root = tmp_path / "audit/qa/hde-epic027"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "QA_ROOT", qa_root)
    monkeypatch.setattr(module, "QA_CHECKS_ROOT", qa_root / "checks")
    monkeypatch.setattr(
        module,
        "ACCEPTANCE_MAP_PATH",
        tmp_path / "docs/acceptance_map_epic027.json",
    )
    monkeypatch.setattr(module, "TOKEN_MATRIX_PATH", qa_root / "token_evidence_matrix.md")
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", qa_root / "acceptance_map_viability.log")
    monkeypatch.setattr(
        module,
        "CLOSE_REPORT_PATH",
        tmp_path / "audit/EPIC-027_close_report.md",
    )
    monkeypatch.setattr(
        module,
        "CLOSE_MANIFEST_PATH",
        tmp_path / "audit/EPIC-027_MANIFEST.json",
    )
    monkeypatch.setattr(
        module,
        "DOC_DELTA_PATH",
        qa_root / "00_meta/doc_deltas.md",
    )


def test_epic027_viability_has_no_planned_gate_exemptions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    ledger = tmp_path / "audit/qa/hde-epic027/acceptance_map_viability.log"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        json.dumps(
            {
                "epic_id": module.EPIC_ID,
                "status": "PASS",
                "status_reason": "",
                "token_status": {},
            }
        )
        + "\n",
        encoding="utf-8",
    )
    config = HarnessConfig(module.EPIC_ID, repo_root=tmp_path)
    primary, manifest = record_check(
        config,
        CheckResult(
            "acceptance-map-viability",
            Status.PASS,
            command=("fixture-check",),
            command_provenance="Explicitly created",
            exit_code=0,
            evidence_artifacts=(
                "audit/qa/hde-epic027/acceptance_map_viability.log",
            ),
        ),
    )
    result = ViabilityResult(
        Status.PASS,
        "",
        primary,
        manifest,
        ledger,
        {},
    )
    observed = []
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: observed.append((config, kwargs)) or result,
    )

    returned = module._write_viability_log()

    assert returned is result
    assert tuple(observed[0][0].step_names) == ()
    assert set(module.GATE_CHECK_IDS) == {
        check_id for check_id, _ in module.GATE_COMMANDS
    }


def test_epic027_preflight_admits_only_planned_gate_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    events = []
    result = CheckResult("acceptance-map-viability", Status.PASS)
    monkeypatch.setattr(
        module.update_evidence_index,
        "main",
        lambda argv: events.append(("updater", tuple(argv))),
    )
    monkeypatch.setattr(
        module.qa_harness,
        "evaluate_acceptance_map_viability",
        lambda config, **kwargs: events.append(("viability", config, kwargs))
        or (result, "{}\n"),
    )

    module._preflight_acceptance_map_viability()

    assert [event[0] for event in events] == ["updater", "updater", "viability"]
    assert events[:2] == [("updater", ()), ("updater", ("--check",))]
    _, config, kwargs = events[2]
    assert tuple(config.step_names) == module.GATE_CHECK_IDS
    assert kwargs == {"planned_governed_ledger": True}


@pytest.mark.parametrize(
    "status",
    [Status.FAIL_BEHAVIOR, Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.PARKED],
)
def test_epic027_preflight_requires_pass(
    status: Status,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    monkeypatch.setattr(module.update_evidence_index, "main", lambda argv: None)
    monkeypatch.setattr(
        module.qa_harness,
        "evaluate_acceptance_map_viability",
        lambda config, **kwargs: (
            CheckResult(
                "acceptance-map-viability",
                status,
                status_reason="blocked",
            ),
            "{}\n",
        ),
    )

    with pytest.raises(
        SystemExit,
        match=f"ACCEPTANCE_MAP_VIABILITY_PREFLIGHT_{status.value}:blocked",
    ):
        module._preflight_acceptance_map_viability()


def test_epic027_preflight_stops_before_viability_when_seal_check_is_stale(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    events = []

    def stale_check(argv):
        events.append(("updater", tuple(argv)))
        if argv == ["--check"]:
            raise SystemExit("STALE:docs/evidence/INDEX.json")

    monkeypatch.setattr(module.update_evidence_index, "main", stale_check)
    monkeypatch.setattr(
        module.qa_harness,
        "evaluate_acceptance_map_viability",
        lambda config, **kwargs: events.append(("viability", config, kwargs)),
    )

    with pytest.raises(SystemExit, match="STALE:docs/evidence/INDEX.json"):
        module._preflight_acceptance_map_viability()

    assert events == [("updater", ()), ("updater", ("--check",))]


def test_epic027_evidence_uses_indexed_artifacts_and_separate_gate_receipts():
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    tokens = {token["name"]: token for token in module.TOKENS}
    rows = {row["token_name"]: row for row in module.TOKEN_MATRIX_ROWS}

    assert tokens["CLI_READER_PARITY_OK"]["evidence_titles"] == [
        "artifacts/cli/reader_dump.json",
        "artifacts/cli/reader_cli_parity.bytes",
    ]
    assert rows["CLI_READER_PARITY_OK"]["evidence_artifacts"] == (
        "artifacts/cli/reader_dump.json; artifacts/cli/reader_cli_parity.bytes"
    )
    assert rows["CLI_READER_PARITY_OK"]["ci_tests_jobs"] == (
        "python -m pytest "
        "tests/http/test_reader_a7_transport.py::"
        "test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair"
    )
    assert tokens["A7_ENCODING_INVARIANCE_OK"]["evidence_titles"][-1] == (
        "artifacts/proofs/success_encoding_invariance.txt"
    )
    assert tokens["CI_CHECK_FINAL_LF_OK"]["evidence_titles"] == [
        "docs/acceptance_map_epic027.json",
        "audit/qa/hde-epic027/token_evidence_matrix.md",
    ]

    gate_evidence_prefix = "audit/qa/hde-epic027/checks/gate_"
    assert all(
        not any(
            path.startswith(gate_evidence_prefix) and path.endswith("/primary.log")
            for path in token["evidence_titles"]
        )
        for token in module.TOKENS
    )
    assert all(
        gate_evidence_prefix not in row["evidence_artifacts"]
        for row in module.TOKEN_MATRIX_ROWS
    )

    expected_receipts = {
        "ENV_RAILS_POLICY_OK": "checks/gate_mirror_schema/primary.log",
        "EVIDENCE_INDEX_UPDATED_OK": (
            "checks/gate_update_evidence_index_write/primary.log"
        ),
        "EVIDENCE_INDEX_HASH_OK": (
            "checks/gate_update_evidence_index_check/primary.log"
        ),
        "EVIDENCE_INDEX_MIRROR_OK": "checks/gate_mirror_schema/primary.log",
        "EVIDENCE_PATHS_VALIDATED_OK": (
            "checks/gate_evidence_paths_validation/primary.log"
        ),
        "CI_CHECK_MIRROR_SCHEMA_OK": "checks/gate_mirror_schema/primary.log",
        "CI_CHECK_FINAL_LF_OK": "checks/gate_lf_endings/primary.log",
    }
    assert {
        name: rows[name]["qa_root_logs"] for name in expected_receipts
    } == expected_receipts


def test_epic027_cli_reader_parity_cannot_regress_to_stored_file_gate_only():
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    row = next(
        row
        for row in module.TOKEN_MATRIX_ROWS
        if row["token_name"] == "CLI_READER_PARITY_OK"
    )

    assert row["evidence_artifacts"] == (
        "artifacts/cli/reader_dump.json; artifacts/cli/reader_cli_parity.bytes"
    )
    assert "run_canonical_json_gate.py" not in row["ci_tests_jobs"]
    assert row["ci_tests_jobs"].endswith(
        "tests/http/test_reader_a7_transport.py::"
        "test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair"
    )


def test_epic028_evidence_uses_governed_artifacts_and_keeps_tests_as_jobs():
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    tokens = {token["name"]: token for token in module.TOKENS}
    rows = {row["token_name"]: row for row in module.TOKEN_MATRIX_ROWS}

    expected = {
        "READER_200_CTYPE_JSON_UTF8_OK": [
            "artifacts/proofs/success_get.txt",
        ],
        "PREFS_KEYSET_10_OK": [
            "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log",
            "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
        ],
    }
    for name, evidence in expected.items():
        assert tokens[name]["evidence_titles"] == evidence
        assert rows[name]["evidence_artifacts"] == "; ".join(evidence)

    forbidden_evidence = {
        "catalog/magic10.json",
        "engine/compat/categories.py",
        "tests/categories/test_registry_and_purity.py",
        "tests/http/test_compat_endpoint_contract.py",
        "tests/http/test_reader_a7_transport.py",
    }
    assert all(
        forbidden_evidence.isdisjoint(token["evidence_titles"])
        for token in module.TOKENS
    )
    assert all(
        forbidden_evidence.isdisjoint(row["evidence_artifacts"].split("; "))
        for row in module.TOKEN_MATRIX_ROWS
    )
    assert rows["READER_200_CTYPE_JSON_UTF8_OK"]["ci_tests_jobs"] == (
        "python -m pytest -q tests/http/test_reader_a7_transport.py"
    )
    assert rows["PREFS_KEYSET_10_OK"]["ci_tests_jobs"] == (
        "python -m pytest -q tests/unit/test_viewer_prefs_normalization.py::"
        "test_viewer_prefs_require_exact_magic10_weight_keys"
    )


def test_epic028_executable_roster_excludes_historical_unclaimed_magic10():
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    token_names = {token["name"] for token in module.TOKENS}
    matrix_names = {row["token_name"] for row in module.TOKEN_MATRIX_ROWS}

    # PF09.4 assigns no EPIC028 implementation row to this token.  PF20 records
    # it as plan-era history and also records that the actual PF10 result never
    # claimed it.  Keep that history intact without promoting it in the current
    # executable Reader-side ledger.
    assert "MAGIC10_DOMAIN_CLOSED_OK" not in token_names
    assert "MAGIC10_DOMAIN_CLOSED_OK" not in matrix_names
    assert len(token_names) == 9
    assert token_names == matrix_names


@pytest.mark.parametrize(
    "module_name",
    (
        "tools.qa.generate_epic027_close_pack",
        "tools.qa.generate_epic028_acceptance_ledger",
    ),
)
def test_acceptance_map_and_matrix_evidence_bindings_are_exactly_aligned(
    module_name: str,
):
    module = importlib.import_module(module_name)
    tokens = {token["name"]: token for token in module.TOKENS}
    rows = {row["token_name"]: row for row in module.TOKEN_MATRIX_ROWS}

    assert set(tokens) == set(rows)
    for name, token in tokens.items():
        assert token["evidence_titles"] == rows[name]["evidence_artifacts"].split(
            "; "
        )


@pytest.mark.parametrize(
    "module_name",
    (
        "tools.qa.generate_epic027_close_pack",
        "tools.qa.generate_epic028_acceptance_ledger",
    ),
)
def test_acceptance_evidence_has_human_mirror_and_proof_bindings(module_name: str):
    module = importlib.import_module(module_name)
    human_rows = json.loads(
        (module.ROOT / "docs/evidence/INDEX.json").read_text(encoding="utf-8")
    )
    mirror_rows = [
        json.loads(line)
        for line in (
            module.ROOT / "artifacts/evidence_index.jsonl"
        ).read_text(encoding="utf-8").splitlines()
        if line
    ]
    evidence_paths = {
        path
        for token in module.TOKENS
        for path in token["evidence_titles"]
    }

    for relative_path in evidence_paths:
        human_keys = {
            row["artifact_key"]
            for row in human_rows
            if row["discovered_physical_path"] == relative_path
        }
        matching_mirror = [
            row
            for row in mirror_rows
            if row["discovered_physical_path"] == relative_path
        ]
        mirror_keys = {row["artifact_key"] for row in matching_mirror}
        expected_proof = f"{relative_path}.path_proof.txt"

        assert human_keys
        assert human_keys == mirror_keys
        assert all(row["proof_anchor"] == expected_proof for row in matching_mirror)
        assert (module.ROOT / expected_proof).is_file()


def test_epic028_prefs_keyset_evidence_matches_exact_magic10_validation():
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    from engine.compat.categories import CATEGORIES_ORDER_V1
    from engine.validation.viewer_prefs import validate_viewer_prefs

    weights = {category: 1 for category in CATEGORIES_ORDER_V1}
    valid = {"top_category": CATEGORIES_ORDER_V1[0], "weights": weights}
    missing = {
        "top_category": CATEGORIES_ORDER_V1[0],
        "weights": dict(tuple(weights.items())[:-1]),
    }
    extra = {
        "top_category": CATEGORIES_ORDER_V1[0],
        "weights": {**weights, "not-a-magic10-category": 1},
    }

    assert validate_viewer_prefs(valid) is None
    assert validate_viewer_prefs(missing) is not None
    assert validate_viewer_prefs(extra) is not None

    invalid_log = (
        module.ROOT
        / "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log"
    ).read_text(encoding="utf-8")
    assert "missing_weights: PASS\n" in invalid_log
    normalized = json.loads(
        (
            module.ROOT
            / "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json"
        ).read_text(encoding="utf-8")
    )["viewer_prefs_normalized"]
    assert set(normalized["weights"]) == set(CATEGORIES_ORDER_V1)


def test_epic027_required_paths_use_canonical_cli_parity(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    canonical_cli_artifacts = {
        "artifacts/cli/reader_dump.json",
        "artifacts/cli/reader_cli_parity.bytes",
    }
    _write_fixture_paths(
        tmp_path,
        {
            "artifacts/compat/identity_hash.txt",
            "artifacts/compat/AB.json",
            "artifacts/compat/BA.json",
            "docs/ENDPOINTS_CATALOG.json",
            "docs/ENDPOINTS_CATALOG.json.sha256",
            "artifacts/proofs/endpoints_env_gate_proof.log",
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_304.txt",
            "artifacts/proofs/success_encoding_invariance.txt",
            "artifacts/writer/conjunction_write_readback.log",
            "artifacts/writer/conjunction_writer_summary.json",
            "artifacts/audit/cli/two_run_identity.log",
            "audit/gates/determinism/env_pins.log",
            "audit/qa/hde-epic027/00_meta/doc_deltas.md",
        },
    )

    with pytest.raises(SystemExit, match="artifacts/cli/reader_cli_parity.bytes"):
        module._ensure_required_paths()

    _write_fixture_paths(tmp_path, canonical_cli_artifacts)
    module._ensure_required_paths()
    assert not (tmp_path / "artifacts/proofs/cli_reader_parity.txt").exists()


def test_epic028_required_paths_use_governed_prefs_artifacts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    _configure_epic028_publication_paths(module, tmp_path, monkeypatch)
    governed_prefs_artifacts = {
        "audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log",
        "audit/qa/hde-epic030/pr-01/zero_weight_handoff.json",
    }
    _write_fixture_paths(
        tmp_path,
        {
            "docs/ENDPOINTS_CATALOG.json",
            "docs/ENDPOINTS_CATALOG.json.sha256",
            "artifacts/proofs/success_get.txt",
            "artifacts/proofs/success_head.txt",
            "artifacts/proofs/success_304.txt",
            "artifacts/proofs/success_encoding_invariance.txt",
            "artifacts/proofs/endpoints_env_gate_proof.log",
        },
    )

    with pytest.raises(SystemExit) as exc_info:
        module._ensure_required_paths()
    assert governed_prefs_artifacts == set(
        str(exc_info.value).removeprefix("MISSING_REQUIRED_PROOFS:").split(",")
    )

    _write_fixture_paths(tmp_path, governed_prefs_artifacts)
    module._ensure_required_paths()
    assert not (tmp_path / "catalog/magic10.json").exists()
    assert not (tmp_path / "artifacts/thresholds/magic10_config.json").exists()
    assert not (
        tmp_path / "artifacts/engine/order/categories_iter.snapshot.json"
    ).exists()
    assert not (tmp_path / "engine/compat/categories.py").exists()
    assert not (tmp_path / "tests/http/test_reader_a7_transport.py").exists()


def test_epic027_close_manifest_binds_current_qa_manifest(
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    captured = []
    monkeypatch.setattr(
        module,
        "_write_json",
        lambda path, payload: captured.append((path, payload)),
    )

    module._write_close_manifest("2026-08-18T00:00:00Z")

    assert captured[0][1]["key_outputs"]["step_logs_manifest"] == (
        "audit/qa/hde-epic027/qa_step_logs_manifest.json"
    )
    assert captured[0][1]["key_outputs"]["acceptance_viability"] == (
        "audit/qa/hde-epic027/acceptance_map_viability.log"
    )
    assert captured[0][1]["key_outputs"]["doc_deltas"] == (
        "audit/qa/hde-epic027/00_meta/doc_deltas.md"
    )


def test_epic027_gate_receipts_are_pf27_v2_and_manifest_bound(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    calls = []

    def pass_gate(command, **kwargs):
        calls.append((command, kwargs))
        return module.subprocess.CompletedProcess(command, 0, "gate passed\n", "")

    monkeypatch.setattr(module.subprocess, "run", pass_gate)
    record_family = module.qa_harness.record_check_family
    family_calls = []

    def record_family_spy(config, results, **kwargs):
        family_calls.append(tuple(result.check_id for result in results))
        return record_family(config, results, **kwargs)

    monkeypatch.setattr(
        module.qa_harness,
        "record_check_family",
        record_family_spy,
    )

    primary_logs = module._run_governed_gates()

    assert primary_logs == _epic027_gate_primaries(tmp_path)
    assert family_calls == [module.GATE_CHECK_IDS]
    manifest = json.loads(
        (module.QA_ROOT / "qa_step_logs_manifest.json").read_text(encoding="utf-8")
    )
    assert tuple(manifest) == tuple(sorted(module.GATE_CHECK_IDS))
    for check_id, primary in zip(module.GATE_CHECK_IDS, primary_logs, strict=True):
        header = module.qa_harness.read_primary_header(primary)
        assert header["schema_version"] == "pf27.step_log_header.v2"
        assert header["check_id"] == check_id
        assert header["status"] == "PASS"
        assert header["command"] == dict(module.GATE_COMMANDS)[check_id]
        assert header["exit_code"] == 0
        assert header["command_provenance"] == (
            "Executed exact non-shell argv; exit code returned by subprocess"
        )
        assert header["pf_refs"] == [
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ]
        assert manifest[check_id] == {
            "check_id": check_id,
            "log_path": primary.relative_to(tmp_path).as_posix(),
            "status": "PASS",
        }
        assert not primary.read_text(encoding="utf-8").startswith("check_id:")
    assert [command for command, _ in calls] == [
        tuple(command) for _, command in module.GATE_COMMANDS
    ]
    assert all(kwargs["shell"] is False for _, kwargs in calls)


def test_epic027_fresh_gate_receipts_are_sealed_before_unplanned_viability(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    events = []

    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda command, **kwargs: module.subprocess.CompletedProcess(
            command,
            0,
            "gate passed\n",
            "",
        ),
    )
    gate_primary_logs = module._run_governed_gates()
    assert gate_primary_logs == _epic027_gate_primaries(tmp_path)
    assert all(path.is_file() for path in gate_primary_logs)
    registered = {
        entry["discovered_physical_path"]
        for entry in module.update_evidence_index.EPIC027_PRIMARY_ARTIFACTS
    }
    assert {
        path.relative_to(tmp_path).as_posix()
        for path in gate_primary_logs
    } <= registered

    def run(command, **kwargs):
        events.append(("seal", command, kwargs))
        return module.subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(module.subprocess, "run", run)
    module._seal_governed_gate_receipts()

    assert [event[1] for event in events] == list(module.GRAPH_SEAL_COMMANDS)
    assert all(event[2]["cwd"] == tmp_path for event in events)
    assert all(event[2]["shell"] is False for event in events)

    def publish_viability(config, **kwargs):
        events.append(("viability", tuple(config.step_names), kwargs))
        return ViabilityResult(Status.PASS, "", None, None, None, {})

    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        publish_viability,
    )
    monkeypatch.setattr(
        module.qa_harness,
        "require_governed_viability",
        lambda result, ledger: ledger,
    )
    module._write_viability_log()

    assert events[-1] == (
        "viability",
        (),
        {"publish_governed_ledger": True},
    )


@pytest.mark.parametrize(
    "check_id",
    [
        "gate_update_evidence_index_write",
        "gate_evidence_paths_validation",
    ],
)
def test_epic027_completed_gate_nonzero_is_causal_tooling_failure(
    check_id: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    command = dict(module.GATE_COMMANDS)[check_id]
    observed = []

    def fail(command_argv, **kwargs):
        observed.append((command_argv, kwargs))
        return module.subprocess.CompletedProcess(command_argv, 7, "", "failed\n")

    monkeypatch.setattr(module.subprocess, "run", fail)

    result = module._run_gate_command(check_id, command)

    assert result.status is Status.FAIL_TOOLING
    assert result.command == tuple(command)
    assert result.exit_code == 7
    assert result.command_provenance == (
        "Executed exact non-shell argv; exit code returned by subprocess"
    )
    assert result.pf_refs == (
        "PF19-Canon-Glow-QA-Guide",
        "PF27-Canon-Plan-Templates",
    )
    assert observed == [
        (
            tuple(command),
            {
                "cwd": tmp_path,
                "text": True,
                "capture_output": True,
                "check": False,
                "shell": False,
            },
        )
    ]


def test_epic027_final_viability_preserves_gate_receipts_in_flat_manifest(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda command, **kwargs: module.subprocess.CompletedProcess(
            command,
            0,
            "gate passed\n",
            "",
        ),
    )
    gate_primary_logs = module._run_governed_gates()

    def publish_viability(config, **kwargs):
        assert tuple(config.step_names) == ()
        assert kwargs == {"publish_governed_ledger": True}
        ledger_content = (
            json.dumps(
                {
                    "epic_id": module.EPIC_ID,
                    "status": "PASS",
                    "status_reason": "",
                    "token_status": {},
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
        )
        primary, manifest = module.qa_harness.record_check(
            config,
            CheckResult(
                "acceptance-map-viability",
                Status.PASS,
                command=("fixture-check",),
                command_provenance="Explicitly created",
                exit_code=0,
                evidence_artifacts=(
                    "audit/qa/hde-epic027/acceptance_map_viability.log",
                ),
            ),
            additional_files=((config.viability_ledger_path, ledger_content),),
        )
        return ViabilityResult(
            Status.PASS,
            "",
            primary,
            manifest,
            config.viability_ledger_path,
            {},
        )

    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        publish_viability,
    )

    result = module._write_viability_log()

    manifest = json.loads(result.manifest.read_text(encoding="utf-8"))
    expected_ids = {*module.GATE_CHECK_IDS, "acceptance-map-viability"}
    assert set(manifest) == expected_ids
    for check_id, entry in manifest.items():
        primary = tmp_path / entry["log_path"]
        header = module.qa_harness.read_primary_header(primary)
        assert header["check_id"] == check_id
        assert header["status"] == entry["status"]
    assert tuple(gate_primary_logs) == _epic027_gate_primaries(tmp_path)


def test_epic027_failed_gate_replaces_stale_family_and_stops_later_gates(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    config = HarnessConfig(module.EPIC_ID, repo_root=tmp_path)
    stale_results = [
        CheckResult(
            check_id,
            Status.PASS,
            command=("fixture-check", check_id),
            command_provenance="Explicitly created",
            exit_code=0,
        )
        for check_id in (*module.GATE_CHECK_IDS, "acceptance-map-viability")
    ]
    module.qa_harness.record_check_family(config, stale_results)
    calls = []

    def fail_second_gate(command, **kwargs):
        calls.append(command)
        return module.subprocess.CompletedProcess(
            command,
            0 if len(calls) == 1 else 1,
            "first gate passed\n" if len(calls) == 1 else "",
            "second gate failed\n" if len(calls) == 2 else "",
        )

    monkeypatch.setattr(module.subprocess, "run", fail_second_gate)

    with pytest.raises(
        SystemExit,
        match=f"GATE_FAIL_TOOLING:{module.GATE_CHECK_IDS[1]}",
    ):
        module._run_governed_gates()

    manifest = json.loads(
        (module.QA_ROOT / "qa_step_logs_manifest.json").read_text(encoding="utf-8")
    )
    assert set(manifest) == set(module.GATE_CHECK_IDS[:2])
    assert manifest[module.GATE_CHECK_IDS[0]]["status"] == "PASS"
    assert manifest[module.GATE_CHECK_IDS[1]]["status"] == "FAIL_TOOLING"
    failed_primary = (
        module.QA_CHECKS_ROOT / module.GATE_CHECK_IDS[1] / "primary.log"
    )
    failed_header = module.qa_harness.read_primary_header(failed_primary)
    assert failed_header["status"] == "FAIL_TOOLING"
    assert len(calls) == 2
    assert not module.CLOSE_REPORT_PATH.exists()
    assert not module.CLOSE_MANIFEST_PATH.exists()


def test_epic027_gate_launch_failure_publishes_truthful_tooling_receipt(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda command, **kwargs: (_ for _ in ()).throw(OSError("not executable")),
    )

    with pytest.raises(
        SystemExit,
        match=f"GATE_FAIL_TOOLING:{module.GATE_CHECK_IDS[0]}",
    ):
        module._run_governed_gates()

    manifest = json.loads(
        (module.QA_ROOT / "qa_step_logs_manifest.json").read_text(encoding="utf-8")
    )
    assert tuple(manifest) == (module.GATE_CHECK_IDS[0],)
    primary = module.QA_CHECKS_ROOT / module.GATE_CHECK_IDS[0] / "primary.log"
    header = module.qa_harness.read_primary_header(primary)
    assert header["status"] == "FAIL_TOOLING"
    assert header["command"] == []
    assert header["exit_code"] is None


def test_epic027_refreshes_canonical_proofs_before_index_write_and_check(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    result = _epic027_result(tmp_path)
    gate_primary_logs = _epic027_gate_primaries(tmp_path)
    events = []
    monkeypatch.setattr(
        module,
        "_write_path_proof",
        lambda path, produced_at: events.append(("proof", path, produced_at)),
    )
    monkeypatch.setattr(
        module.update_evidence_index,
        "main",
        lambda argv: events.append(("updater", tuple(argv))),
    )
    monkeypatch.setattr(
        module,
        "_run_final_mirror_schema_check",
        lambda: events.append(("mirror-schema", module.FINAL_MIRROR_SCHEMA_COMMAND)),
    )

    module._refresh_governed_bindings(
        result,
        gate_primary_logs,
        "2026-08-18T00:00:00Z",
    )

    assert events == [
        ("proof", module.ACCEPTANCE_MAP_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.TOKEN_MATRIX_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.VIABILITY_LOG_PATH, "2026-08-18T00:00:00Z"),
        *[
            ("proof", path, "2026-08-18T00:00:00Z")
            for path in gate_primary_logs
        ],
        ("proof", result.primary_log, "2026-08-18T00:00:00Z"),
        ("proof", result.manifest, "2026-08-18T00:00:00Z"),
        ("proof", module.DOC_DELTA_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.CLOSE_REPORT_PATH, "2026-08-18T00:00:00Z"),
        ("proof", module.CLOSE_MANIFEST_PATH, "2026-08-18T00:00:00Z"),
        ("updater", ()),
        ("updater", ("--check",)),
        ("mirror-schema", module.FINAL_MIRROR_SCHEMA_COMMAND),
    ]


def test_epic027_main_finalizes_only_after_gate_and_output_verification(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    result = _epic027_result(tmp_path)
    gate_primary_logs = _epic027_gate_primaries(tmp_path)
    events = []
    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_utc_now", lambda: "2026-08-18T00:00:00Z")
    for name in (
        "_ensure_required_paths",
        "_invalidate_close_pair",
        "_write_acceptance_map",
        "_write_token_matrix",
        "_preflight_acceptance_map_viability",
        "_write_close_manifest",
        "_write_close_report",
        "_manifest_outputs_exist",
    ):
        monkeypatch.setattr(
            module,
            name,
            lambda *args, _name=name, **kwargs: events.append(_name),
        )
    monkeypatch.setattr(
        module,
        "_run_governed_gates",
        lambda: events.append("_run_governed_gates") or gate_primary_logs,
    )
    monkeypatch.setattr(
        module,
        "_seal_governed_gate_receipts",
        lambda: events.append("_seal_governed_gate_receipts"),
    )
    monkeypatch.setattr(
        module,
        "_write_viability_log",
        lambda: events.append("_write_viability_log") or result,
    )
    monkeypatch.setattr(
        module,
        "_refresh_governed_bindings",
        lambda viability, gates, produced_at: events.append(
            ("_refresh_governed_bindings", viability, gates, produced_at)
        ),
    )

    assert module.main() == 0
    assert events == [
        "_ensure_required_paths",
        "_write_acceptance_map",
        "_write_token_matrix",
        "_preflight_acceptance_map_viability",
        "_run_governed_gates",
        "_seal_governed_gate_receipts",
        "_invalidate_close_pair",
        "_write_viability_log",
        "_write_close_manifest",
        "_write_close_report",
        "_manifest_outputs_exist",
        (
            "_refresh_governed_bindings",
            result,
            gate_primary_logs,
            "2026-08-18T00:00:00Z",
        ),
    ]


def test_epic027_stale_index_check_cannot_report_success(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    result = _epic027_result(tmp_path)
    gate_primary_logs = _epic027_gate_primaries(tmp_path)
    updater_calls = []
    mirror_calls = []
    monkeypatch.setattr(module, "_write_path_proof", lambda path, produced_at: None)
    monkeypatch.setattr(
        module,
        "_run_final_mirror_schema_check",
        lambda: mirror_calls.append(module.FINAL_MIRROR_SCHEMA_COMMAND),
    )

    def stale_check(argv):
        updater_calls.append(tuple(argv))
        if argv == ["--check"]:
            raise SystemExit("STALE:docs/evidence/INDEX.json")

    monkeypatch.setattr(module.update_evidence_index, "main", stale_check)

    with pytest.raises(SystemExit, match="STALE:docs/evidence/INDEX.json"):
        module._refresh_governed_bindings(
            result,
            gate_primary_logs,
            "2026-08-18T00:00:00Z",
        )

    assert updater_calls == [(), ("--check",)]
    assert mirror_calls == []


def test_epic027_final_mirror_schema_uses_exact_non_shell_argv(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    calls = []

    def run(command, **kwargs):
        calls.append((command, kwargs))
        return module.subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(module.subprocess, "run", run)

    module._run_final_mirror_schema_check()

    assert calls == [
        (
            (
                "ci/checks/check_mirror_schema.sh",
                "artifacts/evidence_index.jsonl",
            ),
            {
                "cwd": tmp_path,
                "text": True,
                "capture_output": True,
                "check": False,
                "shell": False,
            },
        )
    ]


def test_epic027_gate_failure_halts_main_before_viability_and_close_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    events = []
    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(
        module,
        "_preflight_acceptance_map_viability",
        lambda: events.append("preflight"),
    )
    module.CLOSE_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    module.CLOSE_REPORT_PATH.write_text("stale close report\n", encoding="utf-8")
    module.CLOSE_MANIFEST_PATH.write_text("{}\n", encoding="utf-8")

    def fail_gates():
        assert module.CLOSE_REPORT_PATH.read_text(encoding="utf-8") == (
            "stale close report\n"
        )
        assert module.CLOSE_MANIFEST_PATH.read_text(encoding="utf-8") == "{}\n"
        events.append("gates")
        raise SystemExit("GATE_FAIL_TOOLING:gate_update_evidence_index_write")

    monkeypatch.setattr(module, "_run_governed_gates", fail_gates)
    for name in (
        "_write_viability_log",
        "_write_close_manifest",
        "_write_close_report",
        "_manifest_outputs_exist",
        "_refresh_governed_bindings",
    ):
        monkeypatch.setattr(
            module,
            name,
            lambda *args, _name=name, **kwargs: events.append(_name),
        )

    with pytest.raises(SystemExit, match="GATE_FAIL_TOOLING"):
        module.main()

    assert events == ["preflight", "gates"]
    assert module.CLOSE_REPORT_PATH.read_text(encoding="utf-8") == (
        "stale close report\n"
    )
    assert module.CLOSE_MANIFEST_PATH.read_text(encoding="utf-8") == "{}\n"


def test_epic027_preflight_failure_halts_main_before_gates_and_close_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    events = []
    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(
        module,
        "_preflight_acceptance_map_viability",
        lambda: (_ for _ in ()).throw(
            SystemExit("ACCEPTANCE_MAP_VIABILITY_PREFLIGHT_FAIL_TOOLING:blocked")
        ),
    )
    monkeypatch.setattr(
        module,
        "_run_governed_gates",
        lambda: events.append("gates"),
    )
    for name in (
        "_write_viability_log",
        "_write_close_manifest",
        "_write_close_report",
        "_manifest_outputs_exist",
        "_refresh_governed_bindings",
    ):
        monkeypatch.setattr(
            module,
            name,
            lambda *args, _name=name, **kwargs: events.append(_name),
        )

    with pytest.raises(SystemExit, match="ACCEPTANCE_MAP_VIABILITY_PREFLIGHT"):
        module.main()

    assert events == []
    assert not module.CLOSE_REPORT_PATH.exists()
    assert not module.CLOSE_MANIFEST_PATH.exists()


@pytest.mark.parametrize(
    "status",
    [Status.FAIL_BEHAVIOR, Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.PARKED],
)
def test_epic027_main_stops_after_gates_before_close_pair_on_viability_non_pass(
    status: Status,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    gate_primary_logs = _epic027_gate_primaries(tmp_path)
    downstream_calls = []
    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(
        module,
        "_preflight_acceptance_map_viability",
        lambda: downstream_calls.append("_preflight_acceptance_map_viability"),
    )
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(
            status,
            "blocked",
            None,
            None,
            None,
            {},
        ),
    )
    for name in (
        "_write_close_manifest",
        "_write_close_report",
        "_manifest_outputs_exist",
        "_refresh_governed_bindings",
    ):
        monkeypatch.setattr(
            module,
            name,
            lambda *args, _name=name, **kwargs: downstream_calls.append(_name),
        )
    monkeypatch.setattr(
        module,
        "_run_governed_gates",
        lambda: downstream_calls.append("_run_governed_gates")
        or gate_primary_logs,
    )
    monkeypatch.setattr(
        module,
        "_seal_governed_gate_receipts",
        lambda: downstream_calls.append("_seal_governed_gate_receipts"),
    )

    with pytest.raises(SystemExit, match=f"ACCEPTANCE_MAP_VIABILITY_{status.value}"):
        module.main()

    assert downstream_calls == [
        "_preflight_acceptance_map_viability",
        "_run_governed_gates",
        "_seal_governed_gate_receipts",
    ]


def _seed_wrapper_write_family(module):
    paths = module._wrapper_write_paths()
    for index, path in enumerate(paths):
        is_new_leaf_family = "/checks/acceptance-map-viability/" in (
            path.as_posix()
        )
        if index % 2 or is_new_leaf_family:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(f"preimage:{index}:{path.name}\n".encode())
        path.chmod(0o640 if index % 4 == 0 else 0o750)
    preimages = {
        path: (
            (path.read_bytes(), path.stat().st_mode & 0o7777)
            if path.exists()
            else None
        )
        for path in paths
    }
    directories = {
        path
        for path in module.ROOT.rglob("*")
        if path.is_dir() and not path.is_symlink()
    }
    return paths, preimages, directories


def _mutate_wrapper_write_family(paths) -> None:
    for index, path in enumerate(paths):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(f"mutated:{index}:{path.name}\n".encode())
        path.chmod(0o600)


def _assert_wrapper_write_family_restored(module, preimages, directories) -> None:
    for path, preimage in preimages.items():
        if preimage is None:
            assert not path.exists()
            assert not path.is_symlink()
            continue
        content, mode = preimage
        assert path.read_bytes() == content
        assert path.stat().st_mode & 0o7777 == mode
    assert {
        path
        for path in module.ROOT.rglob("*")
        if path.is_dir() and not path.is_symlink()
    } == directories


@pytest.mark.parametrize(
    "phase",
    ["gate", "seal", "viability", "updater", "schema"],
)
def test_epic027_outer_transaction_rolls_back_complete_family_at_each_phase(
    phase: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic027_close_pack")
    _configure_epic027_publication_paths(module, tmp_path, monkeypatch)
    monkeypatch.setattr(module.update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setattr(
        module.update_evidence_index,
        "_load_human_index",
        lambda: [
            {
                "artifact_key": "fixture.registered",
                "discovered_physical_path": "artifacts/registered/source.txt",
            }
        ],
    )
    paths, preimages, directories = _seed_wrapper_write_family(module)
    result = _epic027_result(tmp_path)
    gate_primaries = _epic027_gate_primaries(tmp_path)

    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_utc_now", lambda: "2026-08-18T00:00:00Z")
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(module, "_preflight_acceptance_map_viability", lambda: None)
    monkeypatch.setattr(module, "_write_close_manifest", lambda produced_at: None)
    monkeypatch.setattr(module, "_write_close_report", lambda produced_at: None)
    monkeypatch.setattr(module, "_manifest_outputs_exist", lambda: None)
    monkeypatch.setattr(module, "_write_path_proof", lambda path, produced_at: None)

    def gates():
        if phase == "gate":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_GATE")
        return gate_primaries

    def viability():
        if phase == "viability":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_VIABILITY")
        return result

    def seal():
        if phase == "seal":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_SEAL")

    def updater(argv):
        if phase == "updater":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_UPDATER")

    def schema():
        if phase == "schema":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_SCHEMA")

    monkeypatch.setattr(module, "_run_governed_gates", gates)
    monkeypatch.setattr(module, "_seal_governed_gate_receipts", seal)
    monkeypatch.setattr(module, "_write_viability_log", viability)
    monkeypatch.setattr(module.update_evidence_index, "main", updater)
    monkeypatch.setattr(module, "_run_final_mirror_schema_check", schema)

    with pytest.raises(SystemExit, match=f"INJECTED_{phase.upper()}"):
        module.main()

    _assert_wrapper_write_family_restored(module, preimages, directories)


@pytest.mark.parametrize("phase", ["viability", "updater", "schema"])
def test_epic028_outer_transaction_rolls_back_complete_family_at_each_phase(
    phase: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    _configure_epic028_publication_paths(module, tmp_path, monkeypatch)
    monkeypatch.setattr(module.update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setattr(
        module.update_evidence_index,
        "_load_human_index",
        lambda: [
            {
                "artifact_key": "fixture.registered",
                "discovered_physical_path": "artifacts/registered/source.txt",
            }
        ],
    )
    paths, preimages, directories = _seed_wrapper_write_family(module)
    result = _epic028_result(tmp_path)

    monkeypatch.setattr(module, "ensure_determinism_env", lambda **kwargs: None)
    monkeypatch.setattr(module, "_ensure_required_paths", lambda: None)
    monkeypatch.setattr(module, "_utc_now", lambda: "2026-08-18T00:00:00Z")
    monkeypatch.setattr(module, "_write_acceptance_map", lambda: None)
    monkeypatch.setattr(module, "_write_token_matrix", lambda: None)
    monkeypatch.setattr(module, "_write_path_proof", lambda path, produced_at: None)

    def viability():
        if phase == "viability":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_VIABILITY")
        return result

    def updater(argv):
        if phase == "updater":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_UPDATER")

    def schema():
        if phase == "schema":
            _mutate_wrapper_write_family(paths)
            raise SystemExit("INJECTED_SCHEMA")

    monkeypatch.setattr(module, "_write_viability_log", viability)
    monkeypatch.setattr(module.update_evidence_index, "main", updater)
    monkeypatch.setattr(module, "_run_final_mirror_schema_check", schema)

    with pytest.raises(SystemExit, match=f"INJECTED_{phase.upper()}"):
        module.main()

    _assert_wrapper_write_family_restored(module, preimages, directories)


@pytest.mark.parametrize(
    "module_name,configure",
    [
        (
            "tools.qa.generate_epic027_close_pack",
            _configure_epic027_publication_paths,
        ),
        (
            "tools.qa.generate_epic028_acceptance_ledger",
            _configure_epic028_publication_paths,
        ),
    ],
)
@pytest.mark.parametrize("target_kind", ["symlink", "directory"])
def test_wrapper_transaction_rejects_aliased_or_nonregular_targets(
    module_name: str,
    configure,
    target_kind: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module(module_name)
    configure(module, tmp_path, monkeypatch)
    target = module.ACCEPTANCE_MAP_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    if target_kind == "symlink":
        backing = tmp_path / "backing.txt"
        backing.write_text("untouched\n", encoding="utf-8")
        target.symlink_to(backing)
        expected = "WRAPPER_TRANSACTION_TARGET_SYMLINK"
    else:
        target.mkdir()
        expected = "WRAPPER_TRANSACTION_TARGET_NOT_REGULAR"

    with pytest.raises(RuntimeError, match=expected):
        with module._WrapperWriteTransaction():
            raise AssertionError("transaction should not open")


@pytest.mark.parametrize(
    "module_name,configure",
    [
        (
            "tools.qa.generate_epic027_close_pack",
            _configure_epic027_publication_paths,
        ),
        (
            "tools.qa.generate_epic028_acceptance_ledger",
            _configure_epic028_publication_paths,
        ),
    ],
)
def test_wrapper_transaction_includes_every_updater_registered_proof(
    module_name: str,
    configure,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    module = importlib.import_module(module_name)
    configure(module, tmp_path, monkeypatch)
    monkeypatch.setattr(module.update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setattr(
        module.update_evidence_index,
        "_load_human_index",
        lambda: [
            {
                "artifact_key": "fixture.registered",
                "discovered_physical_path": "artifacts/registered/source.txt",
            }
        ],
    )

    assert (
        tmp_path / "artifacts/registered/source.txt.path_proof.txt"
        in module._wrapper_write_paths()
    )


@pytest.mark.parametrize(
    ("module_name", "args"),
    (
        ("tools.qa.generate_epic027_close_pack", ("2026-08-19T00:00:00Z",)),
        (
            "tools.qa.generate_epic028_close_pack",
            ("2026-08-19T00:00:00Z", {"checks": {}}, []),
        ),
        (
            "tools.qa.generate_epic029_close_pack",
            (
                "2026-08-19T00:00:00Z",
                {
                    "po-epic-close-live-qa": True,
                    "po-precommit": True,
                    "po-postcommit": True,
                },
                {
                    "codespaces": "closed",
                    "local_dev": "closed",
                    "closure_mode": "binding-equivalence",
                    "row_closure_status": {"HDE-CONJ001.4": "closed"},
                },
            ),
        ),
    ),
)
def test_active_close_manifest_generators_have_no_run_identity(
    module_name: str, args: tuple[object, ...], monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    captured: list[object] = []
    monkeypatch.setattr(module, "_write_json", lambda _path, payload: captured.append(payload))

    module._write_close_manifest(*args)

    rendered = json.dumps(captured[0], sort_keys=True)
    assert "run_id" not in rendered
    assert not hasattr(module, "RUN_ID")


def test_active_acceptance_ledger_has_no_run_identity_constant():
    module = importlib.import_module("tools.qa.generate_epic028_acceptance_ledger")
    assert not hasattr(module, "RUN_ID")


@pytest.mark.parametrize("number", ("027", "028", "029"))
def test_checked_in_current_close_manifests_have_no_run_identity(number: str):
    payload = json.loads(Path(f"audit/EPIC-{number}_MANIFEST.json").read_text(encoding="utf-8"))
    assert "run_id" not in payload
    assert "RUN_ID" not in json.dumps(payload, sort_keys=True)


def test_epic028_close_pack_counts_canonical_flat_manifest(monkeypatch: pytest.MonkeyPatch):
    module = importlib.import_module("tools.qa.generate_epic028_close_pack")
    flat = {
        "acceptance-map-viability": {"status": "PASS"},
        "d0": {"status": "PASS"},
        "po-001": {"status": "PASS"},
    }
    captured: list[object] = []
    monkeypatch.setattr(module, "_write_json", lambda _path, payload: captured.append(payload))

    module._write_close_manifest("2026-08-19T00:00:00Z", flat, [])

    assert captured[0]["qa_step_count"] == 3
    assert module._manifest_checks(flat) is flat
