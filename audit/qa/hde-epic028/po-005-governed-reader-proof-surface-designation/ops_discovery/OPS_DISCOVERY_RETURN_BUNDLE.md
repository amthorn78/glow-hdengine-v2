EPIC_ID: HDE-EPIC028
STEP_NAME: Governed Reader proof-surface designation
STEP_SLUG: po-005-governed-reader-proof-surface-designation
OUTPUT_DIR: audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery

Commands run (verbatim):
1) EPIC_ID=hde-epic028
   STEP_SLUG=po-005-governed-reader-proof-surface-designation
   OUTPUT_DIR=audit/qa/${EPIC_ID}/${STEP_SLUG}/ops_discovery
   mkdir -p "${OUTPUT_DIR}"
2) pwd > "${OUTPUT_DIR}/repo_root.txt"
3) git rev-parse HEAD > "${OUTPUT_DIR}/repo_head.txt"
4) git status --porcelain > "${OUTPUT_DIR}/git_status_porcelain.txt"
5) for p in
   audit/qa/hde-epic028/checks/d0/primary.log
   audit/qa/hde-epic028/checks/d0/runtime_context.txt
   audit/qa/hde-epic028/checks/d0/cli_health.txt
   audit/qa/hde-epic028/checks/d0/services_surfaces.txt
   audit/qa/hde-epic028/qa_step_logs_manifest.json
   audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt
   audit/qa/hde-epic028/checks/po-005/primary.log
   audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt
   audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt
   audit/qa/hde-epic028/checks/po-005/blocked_note.txt
   docs/ENDPOINTS_CATALOG.json
   adapter/http_reader.py
   do
   if [ -e "$p" ]; then
   printf 'PRESENT %s\n' "$p"
   sha256sum "$p"
   stat -c 'mtime_epoch=%Y size_bytes=%s path=%n' "$p"
   else
   printf 'MISSING %s\n' "$p"
   fi
   done > "${OUTPUT_DIR}/presence_hash_mtime.txt"
6) python block: copy D0 and PO-005 artifacts verbatim into ops_discovery
7) python block: extract first JSON header line from D0 and PO-005 primary logs
8) python block: capture current source excerpts from docs/ENDPOINTS_CATALOG.json (first 40 lines) and adapter/http_reader.py (first 180 lines)
9) python block: generate unified diffs (snapshot vs current excerpts)
10) printf 'additional_repo_local_artifacts_used=none\n' > "${OUTPUT_DIR}/additional_loci_used.txt"

Key outputs (short excerpts, with filenames):
- repo_head.txt:
  410fb7ecb229d5a453c34ab4835876c846ad2a6b
- git_status_porcelain.txt:
  ?? audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/
- d0_primary_header.json:
  status=PASS
  timestamp_utc=2026-04-01T16:50:25Z
  command=<full D0 exact command sequence captured>
- po005_primary_header.json:
  status=TOOLING_BLOCKED
  fail_status=NO_EXPLICIT_GOVERNED_SUCCESS_PROOF_DESIGNATION
  command="capture catalog row and route ownership proof for /reader; classify explicit governed Reader success-proof surface designation"
- po005_primary.log:
  reader_row_count=1 reader_a7_eligible_count=1
  success_endpoints_designates_reader=False
  reader_has_explicit_designation=False
- po005_catalog_vs_current.diff:
  snapshot file is a derived 6-line analysis record, while current excerpt contains compact JSON (single-line file body)
- po005_http_reader_vs_current.diff:
  snapshot file is a derived locator summary (line references + alias check), while current excerpt is raw source top-180 lines
- additional_loci_used.txt:
  additional_repo_local_artifacts_used=none

Evidence files produced (full paths + sha256 for each):
See evidence_files_sha256.txt for the full inventory. Key entries:
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/repo_root.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/repo_head.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/git_status_porcelain.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/presence_hash_mtime.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_primary.log
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_runtime_context.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_cli_health.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_services_surfaces.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_qa_step_logs_manifest.json
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_qa_step_logs_manifest.json.path_proof.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_primary.log
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_catalog_snapshot.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_http_reader_snapshot.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_blocked_note.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/d0_primary_header.json
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_primary_header.json
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/current_ENDPOINTS_CATALOG_excerpt.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/current_http_reader_excerpt.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_catalog_vs_current.diff
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/po005_http_reader_vs_current.diff
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/additional_loci_used.txt
- audit/qa/hde-epic028/po-005-governed-reader-proof-surface-designation/ops_discovery/evidence_files_sha256.txt

Notes (only deviations from Doc B, if any):
- No deviation in required discovery outputs.
- One hygiene remediation was applied after initial capture: presence_hash_mtime.txt was regenerated in a deterministic Python pass to avoid terminal-control escape bytes in redirected output.
