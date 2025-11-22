from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.evidence import update_evidence_index


TARGETS = [
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


def test_evidence_index_has_required_artifacts():
    idx_path = Path("docs/evidence/INDEX.json")
    idx_entries = json.loads(idx_path.read_text(encoding="utf-8"))
    assert isinstance(idx_entries, list)

    entries_by_path = {entry["discovered_physical_path"]: entry for entry in idx_entries}

    for key, path in TARGETS:
        assert path in entries_by_path, f"missing {path} in INDEX.json"
        entry = entries_by_path[path]
        assert entry.get("artifact_key") == key
        expected_proof = Path(f"{path}.path_proof.txt")
        assert expected_proof.exists()
        proof_data = update_evidence_index._load_existing_proof(expected_proof)
        assert proof_data.get("path") == path

    mirror_path = Path("artifacts/evidence_index.jsonl")
    records = {}
    for line in mirror_path.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        records[(rec["artifact_key"], rec["discovered_physical_path"])] = rec

    for key, path in TARGETS:
        assert (key, path) in records, f"missing {key} in evidence_index.jsonl"
        rec = records[(key, path)]
        expected_proof = f"{path}.path_proof.txt"
        assert rec.get("proof_anchor") == expected_proof
        sha = hashlib.sha256(Path(path).read_bytes()).hexdigest()
        assert rec.get("sha256") == sha
        assert rec.get("size_bytes") == Path(path).stat().st_size
