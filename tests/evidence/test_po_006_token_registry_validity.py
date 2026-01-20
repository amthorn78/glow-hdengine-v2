from __future__ import annotations

import json
from pathlib import Path

from tools.evidence.check_po_006_token_registry_validity import (
    TokenExtract,
    TokenSets,
    build_report,
    extract_acceptance_map_tokens,
    extract_registry_tokens,
    run_report_mode,
)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_report_detects_deprecated_spellings(tmp_path: Path) -> None:
    token_sets_path = tmp_path / "token_sets.json"
    acceptance_map_path = tmp_path / "acceptance_map.json"
    registry_path = tmp_path / "registry.json"

    _write_json(
        token_sets_path,
        {
            "canonical_tokens": ["QA_HARNESS_DISCIPLINE_OK", "TESTS_PASS_OK"],
            "deprecated_spellings": ["QA_STEP_LOGS_CONSOLIDATED_OK"],
            "alias_map": {
                "QA_STEP_LOGS_CONSOLIDATED_OK": "QA_HARNESS_DISCIPLINE_OK"
            },
        },
    )
    _write_json(
        acceptance_map_path,
        {
            "epic_id": "HDE-EPIC024",
            "tokens": [
                {"name": "QA_STEP_LOGS_CONSOLIDATED_OK"},
                {"name": "TESTS_PASS_OK"},
            ],
        },
    )
    _write_json(
        registry_path,
        {
            "tokens": [
                {"name": "QA_HARNESS_DISCIPLINE_OK"},
                {"name": "TESTS_PASS_OK"},
            ]
        },
    )

    token_sets = TokenSets(
        canonical_tokens={"QA_HARNESS_DISCIPLINE_OK", "TESTS_PASS_OK"},
        deprecated_spellings={"QA_STEP_LOGS_CONSOLIDATED_OK"},
        alias_map={"QA_STEP_LOGS_CONSOLIDATED_OK": "QA_HARNESS_DISCIPLINE_OK"},
    )
    acceptance_tokens = extract_acceptance_map_tokens(acceptance_map_path)
    registry_tokens = extract_registry_tokens(registry_path)

    report, status = build_report(
        acceptance_tokens=acceptance_tokens,
        registry_tokens=registry_tokens,
        token_sets=token_sets,
        acceptance_map_path=acceptance_map_path,
        registry_export_path=registry_path,
        token_sets_path=token_sets_path,
        determinism_ok=True,
        determinism_error=None,
    )

    comparison = report["comparison"]
    assert status == "FAIL_BEHAVIOR"
    assert comparison["missing_in_registry"] == []
    assert comparison["deprecated_spellings_used"] == ["QA_STEP_LOGS_CONSOLIDATED_OK"]
    assert comparison["alias_hits"] == {
        "QA_STEP_LOGS_CONSOLIDATED_OK": "QA_HARNESS_DISCIPLINE_OK"
    }


def test_report_detects_missing_registry_tokens(tmp_path: Path) -> None:
    acceptance_map_path = tmp_path / "acceptance_map.json"
    registry_path = tmp_path / "registry.json"

    _write_json(
        acceptance_map_path,
        {
            "epic_id": "HDE-EPIC024",
            "tokens": [{"name": "MISSING_OK"}],
        },
    )
    _write_json(registry_path, {"tokens": []})

    token_sets = TokenSets(
        canonical_tokens={"MISSING_OK"},
        deprecated_spellings=set(),
        alias_map={},
    )
    acceptance_tokens = TokenExtract(tokens=["MISSING_OK"], duplicates=[])
    registry_tokens = TokenExtract(tokens=[], duplicates=[])

    report, status = build_report(
        acceptance_tokens=acceptance_tokens,
        registry_tokens=registry_tokens,
        token_sets=token_sets,
        acceptance_map_path=acceptance_map_path,
        registry_export_path=registry_path,
        token_sets_path=tmp_path / "token_sets.json",
        determinism_ok=True,
        determinism_error=None,
    )

    comparison = report["comparison"]
    assert status == "FAIL_BEHAVIOR"
    assert comparison["missing_in_registry"] == ["MISSING_OK"]


def test_report_mode_skips_outputs_when_determinism_open(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    review_dir = tmp_path / "review"
    args = type(
        "Args",
        (),
        {
            "acceptance_map": tmp_path / "missing_map.json",
            "registry_export": tmp_path / "missing_registry.json",
            "token_sets": tmp_path / "missing_token_sets.json",
            "review_dir": review_dir,
        },
    )
    exit_code = run_report_mode(args)
    assert exit_code == 2
    assert not (review_dir / "po_006_token_registry_validity_report.json").exists()
    assert not (review_dir / "po_006_token_registry_validity_summary.md").exists()
