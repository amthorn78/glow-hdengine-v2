# STEP-0D Full Evidence Bundle (token_roster_validate)

## Overview
- Epic: HDE-EPIC022 (STEP-0D — token_roster_validate)
- Rails (all runs): SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=local, LC_ALL=C, LANG=C, TZ=UTC
- RUN_ID: run_20251226t181426z_e44b4cc (plan-faithful rerun); prior ad-hoc attempt recorded separately for traceability.

## Runs and Outcomes
- Plan-faithful rerun (Approved Plan block): status FAIL_TOOLING (exit_code=10) — validator executed; PF04 missing 5 EPIC022 tokens (CLOSE_PACK_FILES_PRESENT_OK, ERROR_JSON_CANON_OK, ERROR_TOKEN_MAP_OK, QA_POSTCOMMIT_CHECKLIST_OK, QA_PRECOMMIT_CHECKLIST_OK). Stdout contains mismatch details; stderr empty. EPIC_ID exported. Recorded in manifest.
  - Step log: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log)
  - Stdout: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt)
  - Stderr: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt)
  - Manifest entry: [audit/qa/hde-epic022/qa_step_logs_manifest.json](audit/qa/hde-epic022/qa_step_logs_manifest.json) (two STEP-0D rows: RC=1 export miss at 21:49:17Z; RC=10 mismatch at 21:49:52Z)
  - Consolidated rerun report: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate_report.md](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate_report.md)
  - Recorder tool (plan layout): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py)

- Ad-hoc attempt (non-plan layout, for traceability): status TOOLING_BLOCKED (validator missing) under run_20260102_211957_utc; evidence retained but superseded by plan-faithful rerun.
  - Full report: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md)
  - Step log: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/logs/step_0d_token_roster_validate.log](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/logs/step_0d_token_roster_validate.log)
  - Outcome JSON: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/outcome.json](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/outcome.json)
  - Stdout/stderr (empty): [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stdout/token_roster_validate.stdout.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stdout/token_roster_validate.stdout.txt), [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stderr/token_roster_validate.stderr.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stderr/token_roster_validate.stderr.txt)
  - PF match lists: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf04_matches.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf04_matches.txt), [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf20_matches.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf20_matches.txt)

## Validator output (plan-faithful rerun stdout)
```
{"epic_id": "HDE-EPIC022", "epic_tokens_ok": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK", "RELEASE_ID_FROM_MANIFEST_OK", "RELEASE_ID_RECOMPUTE_OK"], "epic_tokens_ok_count": 7, "missing_in_pf04": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK"], "missing_in_pf04_count": 5, "pf04_sha256": "c86f110e6bbde49d9f400bd1c90f22728eda16195241d238a3a2d7aabeafc3ff", "pf04_tokens_ok_count": 87, "pf20_sha256": "e7d5eeb5d0647265bbbce74dfbe4f76684649ca6a984e79b59b3973d129fb787"}
```

## Findings
- Plan-faithful rerun shows token roster mismatch: 5 EPIC022 OK tokens missing from PF04 registry; status set to FAIL_TOOLING (RC=10) per validator.
- Prior ad-hoc run was TOOLING_BLOCKED due to missing validator; retained for traceability but superseded.

## Next actions
- Align PF04 token registry with EPIC022 PF20 tokens (add or reconcile the 5 missing tokens), then rerun STEP-0D under the same RUN_ID (run_20251226t181426z_e44b4cc) using the plan block to seek PASS.
