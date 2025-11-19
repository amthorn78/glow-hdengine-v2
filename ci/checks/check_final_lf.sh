#!/usr/bin/env bash
set -euo pipefail
fail=0

files=(
  docs/evidence/INDEX.json
  docs/evidence/INDEX.sha256
  artifacts/evidence_index.jsonl
  artifacts/runtime/env_matrix.snapshot.json
  artifacts/runtime/env_matrix.snapshot.json.path_proof.txt
)

for f in "${files[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "FILE_MISSING:$f" >&2
    fail=1
    continue
  fi
  if [[ ! -s "$f" ]]; then
    echo "FILE_EMPTY:$f" >&2
    fail=1
    continue
  fi
  tail -c1 "$f" | od -An -t o1 | grep -q '012' || { echo "MISSING_FINAL_LF: $f" >&2; fail=1; }
  LC_ALL=C tr -d '\n' <"$f" | grep -q $'\r' && { echo "CR_FOUND: $f" >&2; fail=1; }
done

exit $fail
