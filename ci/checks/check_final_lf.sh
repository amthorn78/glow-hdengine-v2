#!/usr/bin/env bash
set -euo pipefail; fail=0
list=$(git ls-files 'artifacts/**' 'docs/evidence/INDEX.json' 'artifacts/evidence_index.jsonl')
for f in $list; do
  [ -s "$f" ] || continue
  tail -c1 "$f" | od -An -t o1 | grep -q '012' || { echo "MISSING_FINAL_LF: $f" >&2; fail=1; }
  LC_ALL=C tr -d '\n' <"$f" | grep -q $'\r' && { echo "CR_FOUND: $f" >&2; fail=1; }
done; exit $fail
