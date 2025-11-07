#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

import json
import re
from datetime import datetime
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

ROLE_SET = {"proof", "snapshot", "log"}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

mirror_path = Path("artifacts/evidence_index.jsonl")

if not mirror_path.exists():
    raise SystemExit("machine mirror not found: artifacts/evidence_index.jsonl")

primary_seen: set[tuple[str, str]] = set()
secondary_seen: set[tuple[str, str]] = set()
tuples: list[tuple[str, str]] = []

with mirror_path.open("r", encoding="utf-8") as fh:
    for idx, raw in enumerate(fh, 1):
        raw = raw.rstrip("\n")
        if not raw:
            raise SystemExit(f"blank line at {idx} in mirror")
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON on line {idx}: {exc}") from exc

        if list(obj.keys()) != REQUIRED_KEYS:
            raise SystemExit(f"unexpected key order on line {idx}")

        artifact_key = obj["artifact_key"]
        discovered_path = obj["discovered_physical_path"]
        produced_at = obj["produced_at_utc"]
        proof_anchor = obj["proof_anchor"]
        role = obj["role"]
        sha256 = obj["sha256"]
        size_bytes = obj["size_bytes"]

        if not isinstance(artifact_key, str) or not artifact_key:
            raise SystemExit(f"invalid artifact_key on line {idx}")
        if not isinstance(discovered_path, str) or ".." in discovered_path or discovered_path.startswith("./"):
            raise SystemExit(f"invalid discovered_physical_path on line {idx}")
        if proof_anchor != discovered_path:
            raise SystemExit(f"proof_anchor mismatch on line {idx}")
        if role not in ROLE_SET:
            raise SystemExit(f"invalid role on line {idx}")
        if not isinstance(produced_at, str):
            raise SystemExit(f"produced_at_utc must be string on line {idx}")
        try:
            datetime.strptime(produced_at, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError as exc:
            raise SystemExit(f"produced_at_utc must be whole-second RFC3339 on line {idx}") from exc
        if not isinstance(sha256, str) or not SHA_RE.match(sha256):
            raise SystemExit(f"invalid sha256 on line {idx}")
        if not isinstance(size_bytes, int) or size_bytes < 0:
            raise SystemExit(f"invalid size_bytes on line {idx}")

        primary = (artifact_key, discovered_path)
        if primary in primary_seen:
            raise SystemExit(f"duplicate artifact/discovered pair on line {idx}")
        primary_seen.add(primary)

        secondary = (proof_anchor, sha256)
        if secondary in secondary_seen:
            raise SystemExit(f"duplicate proof/sha pair on line {idx}")
        secondary_seen.add(secondary)

        tuples.append(primary)

if tuples != sorted(tuples):
    raise SystemExit("mirror must be sorted by artifact_key, discovered_physical_path")
PY
