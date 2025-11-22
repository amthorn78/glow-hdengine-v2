from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.evidence import update_evidence_index


def test_index_canonical_and_hash_matches(tmp_path):
    entries = update_evidence_index._load_human_index()
    rendered = update_evidence_index._render_human_index(entries)
    assert rendered.endswith(b"\n")

    expected_hash = hashlib.sha256(rendered).hexdigest()
    sentinel_line = Path("docs/evidence/INDEX.sha256").read_text(encoding="utf-8").strip()
    assert sentinel_line == f"{expected_hash}  docs/evidence/INDEX.json"

    on_disk = Path("docs/evidence/INDEX.json").read_bytes()
    assert on_disk == rendered


def test_mirror_schema_and_parity():
    entries = update_evidence_index._load_human_index()
    mirror = Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines(True)

    seen = set()
    prev = None
    for line in mirror:
        assert line.endswith("\n")
        rec = json.loads(line)
        assert set(rec.keys()) == {
            "artifact_key",
            "discovered_physical_path",
            "produced_at_utc",
            "proof_anchor",
            "role",
            "sha256",
            "size_bytes",
        }
        key = (rec["artifact_key"], rec["discovered_physical_path"])
        assert key not in seen
        seen.add(key)
        if prev:
            assert key >= prev
        prev = key

        proof_path = Path(rec["proof_anchor"])
        assert proof_path.exists()
        proof = update_evidence_index._load_existing_proof(proof_path)
        assert proof.get("path") == rec["discovered_physical_path"]
        assert proof.get("sha256") == rec["sha256"]
        assert int(proof.get("size_bytes")) == rec["size_bytes"]

    expected_keys = {
        (entry["artifact_key"], entry["discovered_physical_path"]) for entry in entries
    }
    assert expected_keys == seen
