import hashlib
import json
from pathlib import Path


def test_registry_report_index_entries_match_artifact() -> None:
    report_path = Path("artifacts/registry/registry_report.json")
    assert report_path.exists()
    sha = hashlib.sha256(report_path.read_bytes()).hexdigest()
    size = report_path.stat().st_size

    index = json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
    entries = [
        entry
        for entry in index
        if entry.get("discovered_physical_path") == "artifacts/registry/registry_report.json"
    ]
    assert entries, "registry_report missing from INDEX.json"
    artifact_key = entries[0]["artifact_key"]

    proof_path = Path("artifacts/registry/registry_report.json.path_proof.txt")
    assert proof_path.exists()
    proof_lines = {}
    for line in proof_path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        proof_lines[key.strip()] = value.strip()

    mirror_records = []
    for raw in Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        if obj.get("discovered_physical_path") == "artifacts/registry/registry_report.json":
            mirror_records.append(obj)

    assert mirror_records, "registry_report missing from evidence_index.jsonl"
    rec = mirror_records[0]
    assert rec["artifact_key"] == artifact_key
    assert rec["sha256"] == sha
    assert int(rec["size_bytes"]) == size
    assert rec.get("proof_anchor") == "artifacts/registry/registry_report.json.path_proof.txt"
    assert rec.get("produced_at_utc")
    assert set(rec) >= {
        "artifact_key",
        "discovered_physical_path",
        "produced_at_utc",
        "proof_anchor",
        "role",
        "sha256",
        "size_bytes",
    }
    assert proof_lines.get("sha256") == sha
    assert proof_lines.get("size_bytes") == str(size)

