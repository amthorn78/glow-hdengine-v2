# STEP-0D Full Report and Evidence Dump (RUN_ID: run_20251226t181426z_e44b4cc)

## Summary
- Epic/Step: HDE-EPIC022 / STEP-0D (token_roster_validate)
- Status (plan-faithful rerun): FAIL_TOOLING (exit_code=10)
- Root cause: PF04 missing 5 EPIC022 tokens — CLOSE_PACK_FILES_PRESENT_OK, ERROR_JSON_CANON_OK, ERROR_TOKEN_MAP_OK, QA_POSTCOMMIT_CHECKLIST_OK, QA_PRECOMMIT_CHECKLIST_OK.
- Rails: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=local, LC_ALL=C, LANG=C, TZ=UTC.
- PF docs resolved: docs/pfcanon/PF04-Canon-HDE-Governance-v1.7.7.md; docs/pfcanon/PF20-Canon-HDE-Phased-Epics-v1.7.1.md.
- Evidence layout: QA_ROOT=audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc with manifest updated per Approved Plan.

## Evidence Files
- Step log (PF19 header + stdout/stderr body): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log)
- Stdout: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt)
- Stderr (empty): [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stderr/STEP-0D_token_roster_validate.stderr.txt)
- Manifest (updated; two STEP-0D records, latest RC=10): [audit/qa/hde-epic022/qa_step_logs_manifest.json](audit/qa/hde-epic022/qa_step_logs_manifest.json)
- Validator tool: [tools/qa/token_roster_validate.py](tools/qa/token_roster_validate.py)
- Recorder used: [audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/tools/qa_record_step.py)
- Earlier blocked attempt (traceability): [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md)

## Log Header (authoritative run)
From [STEP-0D_token_roster_validate.log](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log):
```
{"epic_id": "HDE-EPIC022", "run_id": "run_20251226t181426z_e44b4cc", "check_id": "STEP-0D", "step_name": "token_roster_validate", "command": "set -euo pipefail\n\nresolve_pf_doc() {\n  local pattern=\"$1\"\n  shopt -s nullglob\n  local matches=( ${pattern} )\n  shopt -u nullglob\n  if [ \"${#matches[@]}\" -ne 1 ]; then\n    echo \"[STEP-0D] PF doc resolution failed: pattern='${pattern}' matches=${#matches[@]} (expected 1)\" >&2\n    if [ \"${#matches[@]}\" -gt 0 ]; then\n      printf '%s\\n' \"${matches[@]}\" >&2\n    fi\n    return 1\n  fi\n  echo \"${matches[0]}\"\n}\n\nPF04_PATH=\"$(resolve_pf_doc docs/pfcanon/PF04-Canon-HDE-Governance-*.md)\" || exit 20\nPF20_PATH=\"$(resolve_pf_doc docs/pfcanon/PF20-Canon-HDE-Phased-Epics-*.md)\" || exit 20\n\npython tools/qa/token_roster_validate.py --epic \"${EPIC_ID}\" --pf04 \"${PF04_PATH}\" --pf20 \"${PF20_PATH}\"", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "local", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=local LC_ALL=C LANG=C TZ=UTC", "pf_refs": ["PF04", "PF19", "PF20"], "intended_tokens": [], "claimed_tokens": [], "status": "FAIL_TOOLING", "exit_code": 10, "started_at_utc": "2026-01-02T21:49:52Z", "ended_at_utc": "2026-01-02T21:49:53Z", "stdout_sha256": "27dc14a3339ce324579f09c513223bf729cd508a683306c594dfd68984018c32", "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
```

## Validator Output (stdout)
From [STEP-0D_token_roster_validate.stdout.txt](audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/stdout/STEP-0D_token_roster_validate.stdout.txt):
```
{"epic_id": "HDE-EPIC022", "epic_tokens_ok": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK", "RELEASE_ID_FROM_MANIFEST_OK", "RELEASE_ID_RECOMPUTE_OK"], "epic_tokens_ok_count": 7, "missing_in_pf04": ["CLOSE_PACK_FILES_PRESENT_OK", "ERROR_JSON_CANON_OK", "ERROR_TOKEN_MAP_OK", "QA_POSTCOMMIT_CHECKLIST_OK", "QA_PRECOMMIT_CHECKLIST_OK"], "missing_in_pf04_count": 5, "pf04_sha256": "c86f110e6bbde49d9f400bd1c90f22728eda16195241d238a3a2d7aabeafc3ff", "pf04_tokens_ok_count": 87, "pf20_sha256": "e7d5eeb5d0647265bbbce74dfbe4f76684649ca6a984e79b59b3973d129fb787"}
```

## Manifest Entries (excerpt)
From [qa_step_logs_manifest.json](audit/qa/hde-epic022/qa_step_logs_manifest.json): latest two STEP-0D rows for this RUN_ID:
```
{
  "check_id": "STEP-0D",
  "step_name": "token_roster_validate",
  "run_id": "run_20251226t181426z_e44b4cc",
  "log_path": "audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log",
  "status": "FAIL_TOOLING",
  "recorded_at_utc": "2026-01-02T21:49:17Z",
  "exit_code": 1
},
{
  "check_id": "STEP-0D",
  "step_name": "token_roster_validate",
  "run_id": "run_20251226t181426z_e44b4cc",
  "log_path": "audit/qa/hde-epic022/runs/run_20251226t181426z_e44b4cc/step_logs/STEP-0D_token_roster_validate.log",
  "status": "FAIL_TOOLING",
  "recorded_at_utc": "2026-01-02T21:49:53Z",
  "exit_code": 10
}
```
(Note: first entry reflects EPIC_ID export miss (RC=1); second is authoritative validator run (RC=10).)

## Earlier Blocked Attempt (traceability)
- Full report: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/step_0d_full_report.md)
- Status there: TOOLING_BLOCKED (missing validator) with exit_code=0; superseded by plan-faithful rerun above.

## Next Step Recommendations
1) Reconcile PF04 vs PF20 for EPIC022: add the 5 missing OK tokens to PF04 (or adjust PF20 token list if PF04 is correct), ensuring hashes will change accordingly.
2) Rerun STEP-0D under the same RUN_ID (run_20251226t181426z_e44b4cc) using the Approved Plan block; expect PASS (RC=0) once tokens align.
3) Verify manifest updates: confirm qa_step_logs_manifest.json gains a new STEP-0D entry with PASS and exit_code=0 after rerun.
