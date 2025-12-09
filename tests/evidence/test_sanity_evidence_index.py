import hashlib
import json
from pathlib import Path


def test_sanity_log_mirror_and_proof_are_consistent() -> None:
    log_path = Path("artifacts/sanity/sanity.log")
    assert log_path.exists()
    sha = hashlib.sha256(log_path.read_bytes()).hexdigest()
    size = log_path.stat().st_size

    index_entries = [
        entry
        for entry in json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
        if entry.get("discovered_physical_path") == "artifacts/sanity/sanity.log"
    ]
    assert index_entries, "sanity log missing from INDEX.json"

    proof_path = Path("artifacts/sanity/sanity.log.path_proof.txt")
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
        if obj.get("discovered_physical_path") == "artifacts/sanity/sanity.log":
            mirror_records.append(obj)

    assert mirror_records, "sanity log missing from machine mirror"
    mirror = mirror_records[0]
    assert mirror.get("proof_anchor") == "artifacts/sanity/sanity.log.path_proof.txt"
    assert mirror.get("sha256") == sha
    assert int(mirror.get("size_bytes", 0)) == size
    assert proof_fields.get("sha256") == sha
    assert proof_fields.get("size_bytes") == str(size)
    assert mirror.get("produced_at_utc")
