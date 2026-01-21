from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import check_d23_evidence_index_snapshot_contract as tool
from tools.evidence import generate_evidence_index_snapshot as snapshot


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_snapshot_contract_report_passes(tmp_path: Path) -> None:
    root = tmp_path
    human_index = root / "docs/evidence/INDEX.json"
    mirror = root / "artifacts/evidence_index.jsonl"
    snapshot_path = root / "audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"

    _write_json(
        human_index,
        [
            {
                "artifact_key": "token.A",
                "discovered_physical_path": "artifacts/example.txt",
            }
        ],
    )
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_text(
        json.dumps(
            {
                "artifact_key": "token.A",
                "discovered_physical_path": "artifacts/example.txt",
                "proof_anchor": "sha256:deadbeef",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_payload = {
        "generated_at_utc": "2026-01-19T08:49:41Z",
        "inputs": {
            "human_index_path": snapshot.HUMAN_INDEX_REL,
            "human_index_sha256": snapshot._sha256_path(human_index),
            "machine_mirror_path": snapshot.MIRROR_REL,
            "machine_mirror_sha256": snapshot._sha256_path(mirror),
        },
        "parity": {"artifact_keys_match": True},
        "schema_version": "1",
    }
    snapshot_path.write_bytes(snapshot._render_snapshot(snapshot_payload))

    report, status = tool.build_report(
        root=root,
        snapshot_path=snapshot_path,
        human_index_path=human_index,
        mirror_path=mirror,
        determinism_ok=True,
        determinism_error=None,
        check_path_proof=False,
    )

    assert status == "PASS"
    assert report["issues"] == []


def test_missing_snapshot_is_tooling_blocked(tmp_path: Path) -> None:
    root = tmp_path
    human_index = root / "docs/evidence/INDEX.json"
    mirror = root / "artifacts/evidence_index.jsonl"
    snapshot_path = root / "audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"

    report, status = tool.build_report(
        root=root,
        snapshot_path=snapshot_path,
        human_index_path=human_index,
        mirror_path=mirror,
        determinism_ok=True,
        determinism_error=None,
        check_path_proof=False,
    )

    assert status == "TOOLING_BLOCKED"
    assert "MISSING_SNAPSHOT" in report["issues"]
    assert tool._status_exit_code(status) == 2


def test_extract_generated_at_from_snapshot(tmp_path: Path) -> None:
    snapshot_path = tmp_path / "audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_payload = {
        "generated_at_utc": "2026-01-19T08:49:41Z",
        "inputs": {
            "human_index_path": snapshot.HUMAN_INDEX_REL,
            "human_index_sha256": "deadbeef",
            "machine_mirror_path": snapshot.MIRROR_REL,
            "machine_mirror_sha256": "beadfeed",
        },
        "parity": {"artifact_keys_match": True},
        "schema_version": "1",
    }
    snapshot_path.write_bytes(snapshot._render_snapshot(snapshot_payload))

    assert tool._extract_generated_at(snapshot_path) == "2026-01-19T08:49:41Z"
