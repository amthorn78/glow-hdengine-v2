from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import check_epic024_acceptance_map_viability as tool


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_acceptance_map_viability_flags_path_issues(tmp_path: Path) -> None:
    root = tmp_path
    acceptance_map = root / "docs/acceptance_map_epic024.json"
    token_sets_path = root / "audit/qa/hde-epic024/remediation/s1_token_registry_discovery/token_sets.json"
    evidence_path = root / "audit/qa/hde-epic024/viability.log"
    proof_path = root / "audit/qa/hde-epic024/viability.log.path_proof.txt"
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_text("ok\n", encoding="utf-8")
    proof_path.write_text("path: audit/qa/hde-epic024/viability.log\n", encoding="utf-8")

    _write_json(
        acceptance_map,
        {
            "epic_id": "HDE-EPIC024",
            "tokens": [
                {
                    "name": "TOKEN_OK",
                    "evidence_titles": [
                        "audit/qa/hde-epic024/viability.log",
                        "audit/qa/hde-epic024/viability.log.path_proof.txt",
                        "/abs/bad.log",
                        "../bad.log",
                    ],
                }
            ],
        },
    )
    _write_json(
        token_sets_path,
        {
            "canonical_tokens": ["TOKEN_OK"],
            "deprecated_spellings": [],
            "alias_map": {},
        },
    )

    report, status = tool.build_report(
        acceptance_map_path=acceptance_map,
        token_sets_path=token_sets_path,
        root=root,
        determinism_ok=True,
        determinism_error=None,
    )

    assert status == "FAIL_BEHAVIOR"
    assert "PATH_PROOF_USED:TOKEN_OK:audit/qa/hde-epic024/viability.log.path_proof.txt" in report["issues"]
    assert "ABSOLUTE_PATH:TOKEN_OK:/abs/bad.log" in report["issues"]
    assert "PARENT_PATH:TOKEN_OK:../bad.log" in report["issues"]


def test_acceptance_map_viability_flags_unknown_token(tmp_path: Path) -> None:
    root = tmp_path
    acceptance_map = root / "docs/acceptance_map_epic024.json"
    token_sets_path = root / "audit/qa/hde-epic024/remediation/s1_token_registry_discovery/token_sets.json"
    _write_json(
        acceptance_map,
        {
            "epic_id": "HDE-EPIC024",
            "tokens": [{"name": "QA_STEP_LOGS_CONSOLIDATED_OK"}],
        },
    )
    _write_json(
        token_sets_path,
        {
            "canonical_tokens": ["QA_HARNESS_DISCIPLINE_OK"],
            "deprecated_spellings": ["QA_STEP_LOGS_CONSOLIDATED_OK"],
            "alias_map": {"QA_STEP_LOGS_CONSOLIDATED_OK": "QA_HARNESS_DISCIPLINE_OK"},
        },
    )

    report, status = tool.build_report(
        acceptance_map_path=acceptance_map,
        token_sets_path=token_sets_path,
        root=root,
        determinism_ok=True,
        determinism_error=None,
    )

    assert status == "FAIL_BEHAVIOR"
    assert report["comparison"]["deprecated_spellings_used"] == [
        "QA_STEP_LOGS_CONSOLIDATED_OK"
    ]
