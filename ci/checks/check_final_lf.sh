#!/usr/bin/env bash
set -euo pipefail; fail=0
files=(
  artifacts/evidence_index.jsonl
  artifacts/evidence_index.jsonl.path_proof.txt
  artifacts/runtime/env_matrix.snapshot.json
  artifacts/runtime/env_matrix.snapshot.json.path_proof.txt
  docs/evidence/INDEX.json
  docs/evidence/INDEX.sha256
)
for f in "${files[@]}"; do
  [ -s "$f" ] || continue
  tail -c1 "$f" | od -An -t o1 | grep -q '012' || { echo "MISSING_FINAL_LF: $f" >&2; fail=1; }
  LC_ALL=C tr -d '\n' <"$f" | grep -q $'\r' && { echo "CR_FOUND: $f" >&2; fail=1; }
done; exit $fail
