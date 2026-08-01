#!/usr/bin/env bash
set -euo pipefail
fail=0

required_files=(
  docs/evidence/INDEX.json
  docs/evidence/INDEX.sha256
  artifacts/evidence_index.jsonl
  artifacts/runtime/env_matrix.snapshot.json
  artifacts/runtime/env_matrix.snapshot.json.path_proof.txt
  audit/qa/hde-epic038/token_evidence_matrix.md
  audit/qa/hde-epic038/token_evidence_matrix.md.path_proof.txt
)

planned_files=(
  audit/EPIC-038_close_report.md
  audit/EPIC-038_close_report.md.path_proof.txt
  audit/EPIC-038_MANIFEST.json
  audit/EPIC-038_MANIFEST.json.path_proof.txt
  docs/acceptance_map_epic038.json
  docs/acceptance_map_epic038.json.path_proof.txt
  audit/qa/hde-epic038/acceptance_map_viability.log
  audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt
  audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md
  audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt
  audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log
  audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log.path_proof.txt
  audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log
  audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log.path_proof.txt
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

for f in "${planned_files[@]}"; do
  if [[ -f "$f" ]]; then
    check_file "$f"
  fi
done

exit $fail
