# Z0 Close Pack Generate — Evidence Bundle (2025-12-30)

## Posture
- Closed rails: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0.
- RUN_ID: run_20251226t181426z_e44b4cc.
- Step folder: audit/qa/hde-epic022/hde_epic022_qa_step_z0/run_20251226t181426z_e44b4cc.

## Results
### results/status_rc.txt
```
status=PASS
rc=0
```

### results/verdict.txt
```
PASS
```

### results/z0_close_pack_generate.stdout.log (empty after rerun; prior traceback cleared)
```

```

## Step Log
### step_logs/z0_close_pack_generate.log
```
{"check_id": "Z0", "command": "Z0 inline close pack generator (canonical close report + manifest + qa closeout summaries)", "exit_code": 0, "pf_refs": ["PF20 — HDE-Phased Epics, §2.7.6"], "produced_at_utc": "2025-12-30T06:19:00Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "run_id": "run_20251226t181426z_e44b4cc", "status": "PASS", "tokens": []}

=== outputs presence (governed + working) ===
- close_report_exists=True
- close_manifest_exists=True
- qa_run_summary_exists=True
- qa_rca_doc_delta_summary_exists=True
- qa_manifest_exists=True
```

## Snapshots (governed outputs copies)
### snapshots/epic_022_close_report.copy.md
```
# EPIC-022 Close Report

captured_at_utc: 2025-12-30T06:17:57Z
run_id: run_20251226t181426z_e44b4cc

## Evidence roots
- qa_epic_root: audit/qa/hde-epic022
- qa_root: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc

## Canonical close-pack files
- close_report: audit/EPIC-022_close_report.md
- close_manifest: audit/EPIC-022_MANIFEST.json

## QA RCA + Doc Delta Summary
- audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_rca_doc_delta_summary.md

## Step manifest
- audit/qa/hde-epic022/qa_step_logs_manifest.json exists=True

## D0 scan
- audit/qa/hde-epic022/d0_scan.md exists=True

## Status
This file is mechanically generated. See qa_run_summary.json for step status.
```

### snapshots/epic_022_manifest.copy.json
```
{
  "captured_at_utc": "2025-12-30T06:17:57Z",
  "closeout_dir": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout",
  "epic_id": "hde-epic022",
  "key_outputs": {
    "close_manifest": "audit/EPIC-022_MANIFEST.json",
    "close_report": "audit/EPIC-022_close_report.md",
    "d0_scan": "audit/qa/hde-epic022/d0_scan.md",
    "d0_scan_exists": true,
    "qa_rca_doc_delta_summary": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_rca_doc_delta_summary.md",
    "qa_run_summary": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_run_summary.json"
  },
  "qa_epic_root": "audit/qa/hde-epic022",
  "qa_root": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc",
  "qa_step_manifest_path": "audit/qa/hde-epic022/qa_step_logs_manifest.json",
  "run_id": "run_20251226t181426z_e44b4cc"
}
```

### snapshots/qa_run_summary.copy.json
```
{
  "captured_at_utc": "2025-12-30T06:17:57Z",
  "epic_id": "hde-epic022",
  "failing_steps": [
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-26T23:55:51Z",
      "status": "FAIL_BEHAVIOR"
    },
    {
      "check_id": "D3.3",
      "log_path": "audit/qa/hde-epic022/hde_epic022_qa_stepd3.3/run_20251226t181426z_e44b4cc/step_logs/d3_3_sanity_pipeline.log",
      "recorded_at_utc": "2025-12-30T05:07:47Z",
      "status": "FAIL_BEHAVIOR"
    }
  ],
  "qa_epic_root": "audit/qa/hde-epic022",
  "qa_root": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc",
  "qa_step_manifest_path": "audit/qa/hde-epic022/qa_step_logs_manifest.json",
  "run_id": "run_20251226t181426z_e44b4cc"
}
```

### snapshots/qa_rca_doc_delta_summary.copy.md
```
# QA RCA + Doc Delta Summary — EPIC022

captured_at_utc: 2025-12-30T06:17:57Z
run_id: run_20251226t181426z_e44b4cc

## Inputs (presence only)
- doc_deltas_path: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/00_meta/doc_deltas.md exists=True
- token_roster_validation_path: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_registry_validation.summary.md exists=True

## Failing / blocked steps (from qa_step_logs_manifest.json)
- D0.3: FAIL_BEHAVIOR log=audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log
- D3.3: FAIL_BEHAVIOR log=audit/qa/hde-epic022/hde_epic022_qa_stepd3.3/run_20251226t181426z_e44b4cc/step_logs/d3_3_sanity_pipeline.log

## Notes
- This file is mechanically generated.
- See qa_run_summary.json for full failing-step details.
```

### snapshots/qa_step_logs_manifest.copy.json
```
{
  "steps": [
    {"check_id": "D0.1", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log", "recorded_at_utc": "2025-12-26T22:51:25Z", "status": "PASS"},
    {"check_id": "D0.1", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log", "recorded_at_utc": "2025-12-26T23:01:49Z", "status": "PASS"},
    {"check_id": "D0.1", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log", "recorded_at_utc": "2025-12-26T23:07:36Z", "status": "PASS"},
    {"check_id": "D0.2", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.2_determinism_env_pins_emit.log", "recorded_at_utc": "2025-12-26T23:25:46Z", "status": "PASS"},
    {"check_id": "D0.3", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log", "recorded_at_utc": "2025-12-26T23:55:51Z", "status": "FAIL_BEHAVIOR"},
    {"check_id": "D0.3", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log", "recorded_at_utc": "2025-12-27T22:16:48Z", "status": "PASS"},
    {"check_id": "D2.1", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D2.1_showcompat_artifacts_and_tests.log", "recorded_at_utc": "2025-12-27T22:49:41Z", "status": "PASS"},
    {"check_id": "D3.1", "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D3.1_internal_version_bundle.log", "recorded_at_utc": "2025-12-30T02:32:42Z", "status": "PASS"},
    {"check_id": "D3.2", "log_path": "audit/qa/hde-epic022/hde_epic022_qa_step_d3.2/run_20251226t181426z_e44b4cc/step_logs/d3.2_evidence_index_update_and_validate.log", "recorded_at_utc": "2025-12-30T04:27:36Z", "status": "PASS"},
    {"check_id": "D3.3", "log_path": "audit/qa/hde-epic022/hde_epic022_qa_stepd3.3/run_20251226t181426z_e44b4cc/step_logs/d3_3_sanity_pipeline.log", "recorded_at_utc": "2025-12-30T05:07:47Z", "status": "FAIL_BEHAVIOR"},
    {"check_id": "D3.3", "log_path": "audit/qa/hde-epic022/hde_epic022_qa_stepd3.3/run_20251230t051330z_5d9b453/step_logs/d3_3_sanity_pipeline.log", "recorded_at_utc": "2025-12-30T05:16:54Z", "status": "PASS"},
    {"check_id": "Z0", "log_path": "audit/qa/hde-epic022/hde_epic022_qa_step_z0/run_20251226t181426z_e44b4cc/step_logs/z0_close_pack_generate.log", "recorded_at_utc": "2025-12-30T06:16:22Z", "status": "PASS"},
    {"check_id": "Z0", "log_path": "audit/qa/hde-epic022/hde_epic022_qa_step_z0/run_20251226t181426z_e44b4cc/step_logs/z0_close_pack_generate.log", "recorded_at_utc": "2025-12-30T06:19:15Z", "status": "PASS"}
  ]
}
```

## Canonical Outputs (governed locations)
### audit/EPIC-022_close_report.md
```
# EPIC-022 Close Report

captured_at_utc: 2025-12-30T06:14:42Z
run_id: run_20251226t181426z_e44b4cc

## Evidence roots
- qa_epic_root: audit/qa/hde-epic022
- qa_root: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc

## Canonical close-pack files
- close_report: audit/EPIC-022_close_report.md
- close_manifest: audit/EPIC-022_MANIFEST.json

## QA RCA + Doc Delta Summary
- audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_rca_doc_delta_summary.md

## Step manifest
- audit/qa/hde-epic022/qa_step_logs_manifest.json exists=True

## D0 scan
- audit/qa/hde-epic022/d0_scan.md exists=True

## Status
This file is mechanically generated. See qa_run_summary.json for step status.
```

### audit/EPIC-022_MANIFEST.json
```
{
  "captured_at_utc": "2025-12-30T06:14:42Z",
  "closeout_dir": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout",
  "epic_id": "hde-epic022",
  "key_outputs": {
    "close_manifest": "audit/EPIC-022_MANIFEST.json",
    "close_report": "audit/EPIC-022_close_report.md",
    "d0_scan": "audit/qa/hde-epic022/d0_scan.md",
    "d0_scan_exists": true,
    "qa_rca_doc_delta_summary": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_rca_doc_delta_summary.md",
    "qa_run_summary": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/qa_run_summary.json"
  },
  "qa_epic_root": "audit/qa/hde-epic022",
  "qa_root": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc",
  "qa_step_manifest_path": "audit/qa/hde-epic022/qa_step_logs_manifest.json",
  "run_id": "run_20251226t181426z_e44b4cc"
}
```

## Notes
- Z0 executed under closed rails; canonical close-pack files and closeout summaries generated and copied into the step folder.
- QA step manifest now includes Z0 entries (see snapshots/qa_step_logs_manifest.copy.json).
