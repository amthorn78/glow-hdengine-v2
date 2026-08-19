#!/usr/bin/env bash
set -euo pipefail
fail=0

required_files=(
  docs/evidence/INDEX.json
  docs/evidence/INDEX.sha256
  artifacts/evidence_index.jsonl
  docs/evidence/INDEX.json.path_proof.txt
  docs/evidence/INDEX.sha256.path_proof.txt
  artifacts/evidence_index.jsonl.path_proof.txt
  artifacts/evidence_index.jsonl.sha256
  artifacts/evidence_index.jsonl.sha256.path_proof.txt
  audit/gates/topology/orientation_demo.txt
  audit/gates/topology/orientation_demo.txt.path_proof.txt
  artifacts/runtime/env_matrix.snapshot.json
  artifacts/runtime/env_matrix.snapshot.json.path_proof.txt
)

check_file() {
  local f=$1
  if [[ ! -f "$f" ]]; then
    echo "FILE_MISSING:$f" >&2
    fail=1
    return
  fi
  if [[ ! -s "$f" ]]; then
    echo "FILE_EMPTY:$f" >&2
    fail=1
    return
  fi
  tail -c1 "$f" | od -An -t o1 | grep -q '012' || { echo "MISSING_FINAL_LF: $f" >&2; fail=1; }
  LC_ALL=C tr -d '\n' <"$f" | grep -q $'\r' && { echo "CR_FOUND: $f" >&2; fail=1; }
  return 0
}

for f in "${required_files[@]}"; do
  check_file "$f"
done

exit $fail
