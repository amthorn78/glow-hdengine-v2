from __future__ import annotations

import hashlib
import datetime as _dt
import json

import pytest
from pathlib import Path

from tools.evidence import update_evidence_index


COMPAT_TARGETS = [
    ("compat.conjunction.identity_hash", "artifacts/compat/identity_hash.txt"),
]

REPO_TARGETS = [
    ("db_bridge.adapter_selection.snapshot", "artifacts/db_bridge/adapter_selection.snapshot.json"),
    ("db_bridge.health", "artifacts/db_bridge/health.json"),
    ("db_bridge.root", "artifacts/db_bridge/root.json"),
    ("db_bridge.query_select_1", "artifacts/db_bridge/query_select_1.json"),
    ("db.introspect.search_path", "artifacts/db/introspect.search_path.json"),
    ("db.introspect.grants", "artifacts/db/introspect.grants.json"),
    ("db.introspect.fingerprint", "artifacts/db/introspect.fingerprint.json"),
    ("engine.db_adapter.version", "artifacts/engine/db_adapter.version.json"),
    ("engine.db_adapter.search_path", "artifacts/engine/db_adapter.search_path.json"),
    ("engine.db_adapter.fingerprint", "artifacts/engine/db_adapter.fingerprint.json"),
    ("logs.keys_only.sample", "artifacts/logs/keys_only.sample.jsonl"),
    ("ops.rails_open_scope", "artifacts/ops/rails_open_scope.txt"),
    ("cli.showcompat.ab", "artifacts/cli/ab.json"),
    ("cli.showcompat.ba", "artifacts/cli/ba.json"),
    ("cli.showcompat.summary", "artifacts/cli/summary.json"),
    ("cli.help.hdctl", "artifacts/cli/help/hdctl_help.txt"),
    ("cli.help.showcompat", "artifacts/cli/help/showcompat_help.txt"),
    ("cli.help.reject_nonjson", "artifacts/cli/help/reject_nonjson.txt"),
    ("cli.install.entrypoints", "artifacts/cli/install/entrypoints.txt"),
    ("cli.install.installability_summary", "artifacts/cli/install/installability_summary.json"),
    ("cli.guard.serializer_grep", "artifacts/cli/guards/serializer_grep_guard.log"),
    ("cli.guard.emitter_symbol_proof", "artifacts/cli/guards/emitter_symbol_proof.txt"),
    ("cli.showcompat.reader_cli_parity", "artifacts/cli/reader_cli_parity.bytes"),
]


def _assert_targets_present(targets):
    idx_path = Path("docs/evidence/INDEX.json")
    idx_entries = json.loads(idx_path.read_text(encoding="utf-8"))
    assert isinstance(idx_entries, list)

    entries_by_path = {entry["discovered_physical_path"]: entry for entry in idx_entries}

    for key, path in targets:
        assert path in entries_by_path, f"missing {path} in INDEX.json"
        entry = entries_by_path[path]
        assert entry.get("artifact_key") == key
        expected_proof = Path(f"{path}.path_proof.txt")
        assert expected_proof.exists()
        proof_data = update_evidence_index._load_existing_proof(expected_proof)
        assert proof_data.get("path") == path
        assert "mtime_utc" in proof_data
        assert "produced_at_utc" in proof_data
        parsed_mtime = _dt.datetime.fromisoformat(proof_data["mtime_utc"].replace("Z", "+00:00"))
        assert parsed_mtime.tzinfo == _dt.timezone.utc
        assert parsed_mtime.microsecond == 0
        parsed_produced = _dt.datetime.fromisoformat(
            proof_data["produced_at_utc"].replace("Z", "+00:00")
        )
        assert parsed_produced.tzinfo == _dt.timezone.utc
        assert parsed_produced.microsecond == 0

    mirror_path = Path("artifacts/evidence_index.jsonl")
    records = {}
    for line in mirror_path.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        records[(rec["artifact_key"], rec["discovered_physical_path"])] = rec

    for key, path in targets:
        assert (key, path) in records, f"missing {key} in evidence_index.jsonl"
        rec = records[(key, path)]
        expected_proof = f"{path}.path_proof.txt"
        assert rec.get("proof_anchor") == expected_proof
        sha = hashlib.sha256(Path(path).read_bytes()).hexdigest()
        assert rec.get("sha256") == sha
        assert rec.get("size_bytes") == Path(path).stat().st_size


def test_evidence_index_has_required_compat_artifacts():
    _assert_targets_present(COMPAT_TARGETS)


def test_evidence_index_has_required_repo_artifacts():
    _assert_targets_present(REPO_TARGETS)


def test_historical_bridge_inventory_is_nonclaiming_in_both_indexes():
    expected_paths = update_evidence_index.HISTORICAL_BRIDGE_PRIMARY_PATHS
    human = json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
    mirror = [
        json.loads(line)
        for line in Path("artifacts/evidence_index.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]

    for records in (human, mirror):
        selected = [
            record
            for record in records
            if record.get("discovered_physical_path") in expected_paths
        ]
        assert {record["discovered_physical_path"] for record in selected} == expected_paths
        assert len(selected) == len(expected_paths)
        for record in selected:
            assert record["record_type"] == "historical_bridge_evidence"
            assert record["notes"] == update_evidence_index.HISTORICAL_BRIDGE_NOTES
            assert "tokens" not in record


def test_historical_bridge_normalization_strips_current_claims():
    normalized = update_evidence_index._normalize_index_entry(
        {
            "artifact_key": "bridge",
            "discovered_physical_path": next(
                iter(update_evidence_index.HISTORICAL_BRIDGE_PRIMARY_PATHS)
            ),
            "record_type": "current_bridge",
            "tokens": ["CURRENT_BRIDGE_OK"],
            "notes": "current provider fallback",
        }
    )

    assert normalized["record_type"] == "historical_bridge_evidence"
    assert normalized["notes"] == update_evidence_index.HISTORICAL_BRIDGE_NOTES
    assert "tokens" not in normalized


def _write_epic038_live_proof(
    root: Path,
    *,
    generated_at_utc: object = "2026-07-27T23:38:12Z",
    top_level_pass: bool = True,
) -> None:
    path = root / "audit/gates/determinism/open_rails_vendor_abba.json"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {
                "acceptance_token_satisfied": False,
                "artifact_kind": "hde_epic038_pr03_open_rails_vendor_abba_proof",
                "generated_at_utc": generated_at_utc,
                "result": "pass",
                "top_level_pass": top_level_pass,
            }
        )
        + "\n",
        encoding="utf-8",
    )


def test_epic038_live_index_entry_uses_current_artifact_timestamp(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    _write_epic038_live_proof(tmp_path)
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    entries = update_evidence_index._load_epic038_pr03_entries()
    by_key = {entry["artifact_key"]: entry for entry in entries}

    assert by_key["epic038.pr03.open_rails_vendor_abba"]["produced_at_utc"] == "2026-07-27T23:38:12Z"
    assert by_key["epic038.pr03.open_rails_abba"]["produced_at_utc"] == "2026-07-14T00:00:00Z"


def test_epic038_live_index_entry_is_omitted_when_conditional_artifact_absent(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    entries = update_evidence_index._load_epic038_pr03_entries()

    assert "epic038.pr03.open_rails_vendor_abba" not in {
        entry["artifact_key"] for entry in entries
    }


@pytest.mark.parametrize(
    "generated_at_utc,top_level_pass,expected",
    [
        ("2026-07-27", True, "INVALID_EPIC038_PR03_LIVE_PROOF_TIMESTAMP"),
        ("2026-07-27T23:38:12Z", False, "INVALID_EPIC038_PR03_LIVE_PROOF_POSTURE"),
    ],
)
def test_epic038_live_index_entry_rejects_invalid_provenance(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    generated_at_utc: object,
    top_level_pass: bool,
    expected: str,
) -> None:
    _write_epic038_live_proof(
        tmp_path,
        generated_at_utc=generated_at_utc,
        top_level_pass=top_level_pass,
    )
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    with pytest.raises(SystemExit, match=expected):
        update_evidence_index._load_epic038_pr03_entries()


def test_write_if_changed_check_mode_fails_closed_for_missing_target(tmp_path: Path):
    target = tmp_path / "missing.sha256"
    with pytest.raises(SystemExit, match=rf"^STALE:{target}$"):
        update_evidence_index._write_if_changed(target, b"abc\n", check=True)
    assert not target.exists()
