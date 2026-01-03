# STEP-0D rerun report — token_roster_validate (RUN_ID: run_20251226t181426z_e44b4cc)

## Summary
- Status: FAIL_TOOLING (exit_code=10) — validator ran and found missing tokens in PF04 for EPIC HDE-EPIC022.
- Rails: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=local, LC_ALL=C, LANG=C, TZ=UTC.
- PF docs resolved: docs/pfcanon/PF04-Canon-HDE-Governance-v1.7.7.md; docs/pfcanon/PF20-Canon-HDE-Phased-Epics-v1.7.1.md.
- Validator gaps: missing_in_pf04 = {CLOSE_PACK_FILES_PRESENT_OK, ERROR_JSON_CANON_OK, ERROR_TOKEN_MAP_OK, QA_POSTCOMMIT_CHECKLIST_OK, QA_PRECOMMIT_CHECKLIST_OK}; epic token count=7, PF04 tokens present=87.
- Tooling added: tools/qa/token_roster_validate.py (new); audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py (new recorder to align with Approved Plan).
- Note: A prior rerun attempt (21:49:17Z) failed with EPIC_ID unset in the subshell (recorded as FAIL_TOOLING exit_code=1); final attempt at 21:49:52Z is the authoritative execution.

## Evidence paths
- Step log (PF19 header + stdout/stderr body): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log)
- Stdout: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt)
- Stderr (empty): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt)
- Manifest (updated): [audit/qa/hde-epic022/qa_step_logs_manifest.json](audit/qa/hde-epic022/qa_step_logs_manifest.json)
- Validator tool: [tools/qa/token_roster_validate.py](tools/qa/token_roster_validate.py)
- Recorder tool (QA_ROOT): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py)

## Validator output (stdout)
```
{"epic_id": "HDE-EPIC022", "epic_tokens_ok": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK", "RELEASE_ID_FROM_MANIFEST_OK", "RELEASE_ID_RECOMPUTE_OK"], "epic_tokens_ok_count": 7, "missing_in_pf04": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK"], "missing_in_pf04_count": 5, "pf04_sha256": "c86f110e6bbde49d9f400bd1c90f22728eda16195241d238a3a2d7aabeafc3ff", "pf04_tokens_ok_count": 87, "pf20_sha256": "e7d5eeb5d0647265bbbce74dfbe4f76684649ca6a984e79b59b3973d129fb787"}
```

## Notes
- Manifest now contains two STEP-0D records for this RUN_ID: the first (21:49:17Z) captures the EPIC_ID export miss (RC=1), and the second (21:49:52Z) captures the validator execution (RC=10, FAIL_TOOLING).
- No new RUN_ID was created; outputs live under QA_ROOT=audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc per the Approved Plan block.
