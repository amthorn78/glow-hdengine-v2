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
        stat_mtime = _dt.datetime.fromtimestamp(Path(path).stat().st_mtime, tz=_dt.timezone.utc)
        # NEW CANON (EPIC017 WS-D4): refresh-time mtime is monotone vs. stat().
        assert parsed_mtime <= stat_mtime

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


def test_write_if_changed_check_mode_fails_closed_for_missing_target(tmp_path: Path):
    target = tmp_path / "missing.sha256"
    with pytest.raises(SystemExit, match=rf"^STALE:{target}$"):
        update_evidence_index._write_if_changed(target, b"abc\n", check=True)
    assert not target.exists()
