# HDE-EPIC031 — Fermentation Pass 2 — Action Report (Version 2)

Generated at (UTC): 2026-05-13T13:44:58Z
Source baseline: audit/qa/hde-epic031/checks/po-004-po-006_action_report.md

## Scope

This versioned report provides full current evidence output in one file for:

- PO-004
- PO-005
- PO-006

Closed-rails execution posture:

- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Step PO-004

### Deliverables

- audit/qa/hde-epic031/checks/po-004/primary.log
- audit/qa/hde-epic031/checks/po-004/result.json

### Full Evidence Output

#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-004","check_name":"PO-004","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-004","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-004/primary.log","audit/qa/hde-epic031/checks/po-004/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T13:13:43Z"}
{
  "non_success_classification_present": true,
  "pinned_attempts_present": true,
  "pytest": {
    "cmd": [
      "/usr/bin/python3",
      "-m",
      "pytest",
      "tests/bodygraph/test_vendor_client.py",
      "-q"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": ".............                                                            [100%]\n13 passed in 0.19s\n"
  },
  "retry_backoff_artifact_present": true,
  "schema": "hde_epic031.po004.retry_backoff.v1",
  "status": "PASS"
}
```

#### result.json (full content)
```json
{
  "non_success_classification_present": true,
  "pinned_attempts_present": true,
  "pytest": {
    "cmd": [
      "/usr/bin/python3",
      "-m",
      "pytest",
      "tests/bodygraph/test_vendor_client.py",
      "-q"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": ".............                                                            [100%]\n13 passed in 0.19s\n"
  },
  "retry_backoff_artifact_present": true,
  "schema": "hde_epic031.po004.retry_backoff.v1",
  "status": "PASS"
}
```

## Step PO-005

### Deliverables

- audit/qa/hde-epic031/checks/po-005/primary.log
- audit/qa/hde-epic031/checks/po-005/result.json

### Full Evidence Output

#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-005","check_name":"PO-005","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-005","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-005/primary.log","audit/qa/hde-epic031/checks/po-005/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T13:14:28Z"}
{
  "retry_after_delta_parsed": true,
  "schema": "hde_epic031.po005.rate_limit.v1",
  "source_maps_429": true,
  "status": "PASS",
  "typed_429_evidence_present": true
}
```

#### result.json (full content)
```json
{
  "retry_after_delta_parsed": true,
  "schema": "hde_epic031.po005.rate_limit.v1",
  "source_maps_429": true,
  "status": "PASS",
  "typed_429_evidence_present": true
}
```

## Step PO-006

### Deliverables

- audit/qa/hde-epic031/checks/po-006/primary.log
- audit/qa/hde-epic031/checks/po-006/result.json

### Full Evidence Output

#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-006","check_name":"PO-006","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-006","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-006/primary.log","audit/qa/hde-epic031/checks/po-006/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T13:19:05Z"}
{
  "allowed_keys_present": true,
  "generator_check": {
    "cmd": [
      "/usr/bin/python3",
      "tools/evidence/generate_epic031_pr02_log_posture.py",
      "--check"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": "EPIC031_PR02_LOG_POSTURE_OK\n"
  },
  "payload_body_absent": true,
  "plaintext_secret_absent": true,
  "raw_secret_header_absent": true,
  "schema": "hde_epic031.po006.keys_only.v1",
  "status": "PASS"
}
```

#### result.json (full content)
```json
{
  "allowed_keys_present": true,
  "generator_check": {
    "cmd": [
      "/usr/bin/python3",
      "tools/evidence/generate_epic031_pr02_log_posture.py",
      "--check"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": "EPIC031_PR02_LOG_POSTURE_OK\n"
  },
  "payload_body_absent": true,
  "plaintext_secret_absent": true,
  "raw_secret_header_absent": true,
  "schema": "hde_epic031.po006.keys_only.v1",
  "status": "PASS"
}
```

## Moon Loop Provenance (PO-006)

- audit/qa/hde-epic031/remediation/moon_loop/patch.diff
- audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt
- audit/qa/hde-epic031/00_meta/doc_deltas.md

## Final Status

- PO-004: PASS
- PO-005: PASS
- PO-006: PASS
