import hashlib
import json
from pathlib import Path


def test_sanity_log_mirror_and_proof_are_consistent() -> None:
    relative_log = "audit/gates/sanity_pipeline/sanity_pipeline.log"
    log_path = Path(relative_log)
    assert log_path.exists()
    sha = hashlib.sha256(log_path.read_bytes()).hexdigest()
    size = log_path.stat().st_size

    index_entries = [
        entry
        for entry in json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
        if entry.get("artifact_key") == "sanity.pipeline.log"
    ]
    assert index_entries, "sanity log missing from INDEX.json"

    proof_path = Path(f"{relative_log}.path_proof.txt")
    assert proof_path.exists()
    proof_fields: dict[str, str] = {}
    for line in proof_path.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            proof_fields[key.strip()] = value.strip()

    mirror_records = []
    for raw in Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        if obj.get("artifact_key") == "sanity.pipeline.log":
            mirror_records.append(obj)

    assert mirror_records, "sanity log missing from machine mirror"
    mirror = mirror_records[0]
    assert mirror.get("discovered_physical_path") == relative_log
    assert mirror.get("proof_anchor") == f"{relative_log}.path_proof.txt"
    assert mirror.get("sha256") == sha
    assert int(mirror.get("size_bytes", 0)) == size
    assert proof_fields.get("sha256") == sha
    assert proof_fields.get("size_bytes") == str(size)
    assert mirror.get("produced_at_utc")

    assert {entry.get("discovered_physical_path") for entry in index_entries} == {
        relative_log
    }
    assert {record.get("discovered_physical_path") for record in mirror_records} == {
        relative_log
    }

    legacy_log = Path("artifacts/sanity/sanity.log")
    legacy_proof = Path("artifacts/sanity/sanity.log.path_proof.txt")
    assert legacy_log.read_bytes() == log_path.read_bytes()
    legacy_fields: dict[str, str] = {}
    for line in legacy_proof.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            legacy_fields[key.strip()] = value.strip()
    assert legacy_fields.get("path") == legacy_log.as_posix()
    assert legacy_fields.get("sha256") == sha
    assert legacy_fields.get("size_bytes") == str(size)
