#!/usr/bin/env python3
"""Update artifacts/evidence_index.jsonl with fresh metadata."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = ROOT / "artifacts/evidence_index.jsonl"

TARGETS: dict[str, dict[str, str]] = {
    "artifacts/runtime/env_matrix.snapshot.json": {},
    "artifacts/runtime/env_connectivity.snapshot.json": {"artifact_key": "runtime.env_connectivity"},
    "artifacts/db/check_schema.txt": {},
    "artifacts/db/ddl_fingerprint.json": {},
    "artifacts/db/grants.txt": {},
    "artifacts/db/partition_plan.txt": {},
    "artifacts/db/partition_verify.log": {},
    "artifacts/db/boundary_view.readonly.proof.txt": {},
    "artifacts/db/provider_parity/direct.json": {"artifact_key": "db.provider_parity.direct", "role": "runtime"},
    "artifacts/db/provider_parity/bridge.json": {"artifact_key": "db.provider_parity.bridge", "role": "runtime"},
    "artifacts/db/provider_parity/summary.json": {"artifact_key": "db.provider_parity.summary", "role": "runtime"},
    "artifacts/db_bridge/adapter_selection.snapshot.json": {},
    "artifacts/db_bridge/caps.snapshot.json": {},
    "artifacts/db_bridge/provider_parity.proof.json": {"artifact_key": "db_bridge.provider_parity"},
    "artifacts/bodygraph/source_selection.snapshot.json": {},
    "artifacts/presenter/json_canon_compare.log": {},
    "artifacts/bodygraph/metrics.snapshot.json": {},
    "artifacts/bodygraph/keys_only.logs.sample": {},
    "artifacts/proofs/ops_refusal_proof.txt": {"artifact_key": "ops.rails_refusal", "role": "proof"},
}


def _file_meta(rel: str) -> tuple[str, int, str]:
    path = ROOT / rel
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    size = len(data)
    mtime = _dt.datetime.fromtimestamp(path.stat().st_mtime, tz=_dt.timezone.utc).replace(microsecond=0)
    return sha, size, mtime.isoformat().replace("+00:00", "Z")


def _serialize(record: dict[str, object]) -> str:
    ordered = {
        "artifact_key": record["artifact_key"],
        "discovered_physical_path": record["discovered_physical_path"],
        "produced_at_utc": record["produced_at_utc"],
        "proof_anchor": record["proof_anchor"],
        "role": record["role"],
        "sha256": record["sha256"],
        "size_bytes": record["size_bytes"],
    }
    return json.dumps(ordered, separators=(",", ":"))


def main() -> None:
    records: list[dict[str, object]] = []
    seen_paths: set[str] = set()
    if INDEX_PATH.exists():
        for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            records.append(rec)
            seen_paths.add(rec["discovered_physical_path"])
    for rec in records:
        path = rec["discovered_physical_path"]
        if path not in TARGETS:
            continue
        sha, size, mtime = _file_meta(path)
        rec["sha256"] = sha
        rec["size_bytes"] = size
        rec["produced_at_utc"] = mtime
        rec["proof_anchor"] = f"{path}.path_proof.txt"
        override = TARGETS[path]
        if "artifact_key" in override:
            rec["artifact_key"] = override["artifact_key"]
        if "role" in override:
            rec["role"] = override["role"]
    for path, override in TARGETS.items():
        if path in seen_paths:
            continue
        sha, size, mtime = _file_meta(path)
        artifact_key = override.get("artifact_key")
        if not artifact_key:
            raise SystemExit(f"Missing artifact key for new path: {path}")
        role = override.get("role", "snapshot")
        records.append(
            {
                "artifact_key": artifact_key,
                "discovered_physical_path": path,
                "produced_at_utc": mtime,
                "proof_anchor": f"{path}.path_proof.txt",
                "role": role,
                "sha256": sha,
                "size_bytes": size,
            }
        )
        seen_paths.add(path)
    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))
    text = "\n".join(_serialize(rec) for rec in records) + "\n"
    INDEX_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
