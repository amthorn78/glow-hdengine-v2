#!/usr/bin/env python3
import json
import sys
import hashlib
from pathlib import Path

REQUIRED_KEYS = [
    "artifact_key",
    "discovered_physical_path",
    "produced_at_utc",
    "proof_anchor",
    "role",
    "sha256",
    "size_bytes",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_proof(path: Path):
    data = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main():
    ok = True
    prev = None
    index_path = Path("artifacts/evidence_index.jsonl")
    if not index_path.exists():
        print("MISSING:artifacts/evidence_index.jsonl", file=sys.stderr)
        return 1

    for i, raw in enumerate(index_path.read_text().splitlines(), 1):
        if not raw:
            print(f"EMPTY:{i}", file=sys.stderr)
            ok = False
            continue
        try:
            obj = json.loads(raw)
        except Exception as exc:  # noqa: BLE001
            print(f"JSON:{i}:{exc}", file=sys.stderr)
            ok = False
            continue

        key_set = set(obj.keys())
        if key_set != set(REQUIRED_KEYS):
            print(f"KEYS:{i}:{sorted(key_set)}", file=sys.stderr)
            ok = False

        if prev and (obj["artifact_key"], obj["discovered_physical_path"]) < prev:
            print(f"SORT:{i}:{(obj['artifact_key'], obj['discovered_physical_path'])} < {prev}", file=sys.stderr)
            ok = False
        prev = (obj["artifact_key"], obj["discovered_physical_path"])

        artifact_path = Path(obj["discovered_physical_path"])
        proof_path = Path(obj["proof_anchor"])

        if not proof_path.as_posix().endswith(".path_proof.txt"):
            print(f"PROOF_SUFFIX:{i}:{proof_path}", file=sys.stderr)
            ok = False
        if not proof_path.exists():
            print(f"PROOF_MISSING:{i}:{proof_path}", file=sys.stderr)
            ok = False
            continue

        if not artifact_path.exists():
            print(f"ARTIFACT_MISSING:{i}:{artifact_path}", file=sys.stderr)
            ok = False
            continue

        proof_data = load_proof(proof_path)
        if proof_data.get("path") != artifact_path.as_posix():
            print(f"PROOF_PATH:{i}:{proof_data.get('path')}!={artifact_path.as_posix()}", file=sys.stderr)
            ok = False

        actual_sha = sha256(artifact_path)
        actual_size = artifact_path.stat().st_size

        if obj.get("sha256") != actual_sha:
            print(f"SHA_MISMATCH:{i}:{obj.get('sha256')}!={actual_sha}", file=sys.stderr)
            ok = False
        if obj.get("size_bytes") != actual_size:
            print(f"SIZE_MISMATCH:{i}:{obj.get('size_bytes')}!={actual_size}", file=sys.stderr)
            ok = False

        if proof_data.get("sha256") != actual_sha:
            print(f"PROOF_SHA:{i}:{proof_data.get('sha256')}!={actual_sha}", file=sys.stderr)
            ok = False
        proof_size_val = proof_data.get("size_bytes")
        if proof_size_val is None or int(proof_size_val) != actual_size:
            print(f"PROOF_SIZE:{i}:{proof_size_val}!={actual_size}", file=sys.stderr)
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
