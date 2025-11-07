#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

targets = [
    "artifacts/db/check_constraints.txt",
    "artifacts/db/check_schema.txt",
    "artifacts/db/ddl_fingerprint.json",
    "artifacts/db/grants.txt",
    "artifacts/db/migration_runner.log",
    "artifacts/db/partition_plan.txt",
    "artifacts/ops/no_io_guard.txt",
    "artifacts/ops/rails_refusal_proof.txt",
    "artifacts/ops/restart_capability.txt",
    "artifacts/ops/restart_probe_after.json",
    "artifacts/ops/restart_probe_before.json",
    "artifacts/runtime/env_matrix.failure.json",
    "artifacts/runtime/env_matrix.snapshot.json",
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.sha256",
    "artifacts/evidence_index.jsonl",
]

failed = False

for name in targets:
    path = Path(name)
    if not path.is_file():
        continue
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        print(f"missing final newline: {name}", file=sys.stderr)
        failed = True
    if b"\r" in data:
        print(f"carriage return detected: {name}", file=sys.stderr)
        failed = True

if failed:
    sys.exit(1)
PY
