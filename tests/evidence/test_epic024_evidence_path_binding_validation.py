from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import check_epic024_evidence_path_binding_validation as tool


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_evidence_path_binding_validation_passes_with_index_entries(tmp_path: Path) -> None:
    root = tmp_path
    acceptance_map = root / "docs/acceptance_map_epic024.json"
    matrix_path = root / "audit/qa/hde-epic024/token_evidence_matrix.md"
    index_path = root / "docs/evidence/INDEX.json"
    mirror_path = root / "artifacts/evidence_index.jsonl"
    evidence_path = root / "audit/qa/hde-epic024/viability.log"

    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_text("ok\n", encoding="utf-8")

    _write_json(
        acceptance_map,
        {
            "epic_id": "HDE-EPIC024",
            "tokens": [
                {
                    "name": "TOKEN_OK",
                    "status": "implemented",
                    "evidence_titles": ["audit/qa/hde-epic024/viability.log"],
                }
            ],
        },
    )
    matrix_path.parent.mkdir(parents=True, exist_ok=True)
    matrix_path.write_text(
        "\n".join(
            [
                "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
                "| --- | --- | --- | --- | --- | --- | --- |",
                "| TOKEN_OK | PF19 | audit/qa/hde-epic024/viability.log | pytest | acceptance_map_viability.log | Implemented | |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    _write_json(
        index_path,
        [
            {
                "artifact_key": "epic024.acceptance_map_viability",
                "discovered_physical_path": "audit/qa/hde-epic024/viability.log",
            }
        ],
    )
    mirror_path.parent.mkdir(parents=True, exist_ok=True)
    mirror_path.write_text(
        json.dumps(
            {
                "artifact_key": "epic024.acceptance_map_viability",
                "discovered_physical_path": "audit/qa/hde-epic024/viability.log",
                "proof_anchor": "sha256:deadbeef",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    report, status = tool.build_report(
        acceptance_map_path=acceptance_map,
        matrix_path=matrix_path,
        index_path=index_path,
        mirror_path=mirror_path,
        root=root,
        determinism_ok=True,
        determinism_error=None,
    )

    assert status == "PASS"
    assert report["issues"] == []
