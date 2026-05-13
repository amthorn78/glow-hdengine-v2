# HDE-EPIC031 — Fermentation Pass 2 — Action Report (PO-007 to PO-009)

Generated at (UTC): 2026-05-13T16:44:46Z

## Scope
This report captures execution, deliverables, and evidence outputs for:

- PO-007
- PO-008
- PO-009

Execution posture used:

- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Step PO-007 — Sensitive provider data absence from QA-visible diagnostics

### Commands executed
Preflight:

```bash
set -e
python --version
test -f audit/qa/hde-epic031/00_meta/live_qa_harness.py
test -f tools/evidence/generate_epic031_pr02_log_posture.py
test -f audit/qa/hde-epic031/pr-02/secret_redaction_scan.log
test -f audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt
```

Execution:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-007
```

### Deliverables
- audit/qa/hde-epic031/checks/po-007/primary.log
- audit/qa/hde-epic031/checks/po-007/result.json

### Evidence output
#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-007","check_name":"PO-007","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-007","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-007/primary.log","audit/qa/hde-epic031/checks/po-007/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T16:43:22Z"}
{
  "generator_check": {
    "cmd": [
      "/usr/local/bin/python",
      "tools/evidence/generate_epic031_pr02_log_posture.py",
      "--check"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": "EPIC031_PR02_LOG_POSTURE_OK\n"
  },
  "scan_has_title": true,
  "scan_present": true,
  "schema": "hde_epic031.po007.secret_absence.v1",
  "scope_live_forbidden": true,
  "status": "PASS"
}
```

#### result.json (full content)
```json
{
  "generator_check": {
    "cmd": [
      "/usr/local/bin/python",
      "tools/evidence/generate_epic031_pr02_log_posture.py",
      "--check"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": "EPIC031_PR02_LOG_POSTURE_OK\n"
  },
  "scan_has_title": true,
  "scan_present": true,
  "schema": "hde_epic031.po007.secret_absence.v1",
  "scope_live_forbidden": true,
  "status": "PASS"
}
```

### Outcome
PASS

## Step PO-008 — Governed human and machine evidence coherence

### Commands executed
Preflight:

```bash
set -e
python --version
test -f audit/qa/hde-epic031/00_meta/live_qa_harness.py
test -f tools/evidence/generate_epic031_pr03_evidence_coherence.py
test -f tools/evidence/update_evidence_index.py
test -f tools/evidence/validate_evidence_paths.py
test -f ci/checks/check_evidence_index_hash.sh
test -f ci/checks/check_mirror_schema.sh
test -f docs/evidence/INDEX.json
test -f artifacts/evidence_index.jsonl
```

Execution:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-008
```

### Deliverables
- audit/qa/hde-epic031/checks/po-008/primary.log
- audit/qa/hde-epic031/checks/po-008/result.json

### Evidence output
#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-008","check_name":"PO-008","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-008","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-008/primary.log","audit/qa/hde-epic031/checks/po-008/result.json"],"exit_code":1,"fail_status":"FAIL_BEHAVIOR","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"FAIL_BEHAVIOR","timestamp_utc":"2026-05-13T16:43:53Z"}
{
  "all_commands_green": false,
  "coherence_status": "PASS",
  "commands": [
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/generate_epic031_pr03_evidence_coherence.py",
        "--check"
      ],
      "returncode": 1,
      "stderr": "STALE:audit/qa/hde-epic031/pr-03/evidence_family_map.json\n",
      "stdout": ""
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/update_evidence_index.py",
        "--check"
      ],
      "returncode": 1,
      "stderr": "PROOF_MTIME_FUTURE:artifacts/compat/AB.json.path_proof.txt\n",
      "stdout": "[evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC\n"
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/validate_evidence_paths.py"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    },
    {
      "cmd": [
        "bash",
        "ci/checks/check_evidence_index_hash.sh"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "ci/checks/check_mirror_schema.sh"
      ],
      "returncode": 1,
      "stderr": "PROOF_MTIME:140:2026-04-23T17:40:37Z\nPROOF_MTIME:141:2026-04-23T17:40:37Z\nPROOF_MTIME:148:2026-05-10T21:33:32Z\nPROOF_MTIME:149:2026-05-10T21:33:32Z\nPROOF_MTIME:260:2026-05-10T21:33:32Z\nPROOF_MTIME:261:2026-05-10T21:33:32Z\nPROOF_MTIME:262:2026-05-10T21:33:32Z\nPROOF_MTIME:263:2026-05-10T21:33:32Z\nPROOF_MTIME:264:2026-05-10T21:33:32Z\nPROOF_MTIME:265:2026-05-10T21:33:32Z\nPROOF_MTIME:266:2026-05-10T21:33:32Z\nPROOF_MTIME:267:2026-05-10T21:33:32Z\nPROOF_MTIME:268:2026-05-10T21:33:32Z\n",
      "stdout": ""
    }
  ],
  "schema": "hde_epic031.po008.evidence_coherence.v1",
  "status": "FAIL_BEHAVIOR"
}
```

#### result.json (full content)
```json
{
  "all_commands_green": false,
  "coherence_status": "PASS",
  "commands": [
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/generate_epic031_pr03_evidence_coherence.py",
        "--check"
      ],
      "returncode": 1,
      "stderr": "STALE:audit/qa/hde-epic031/pr-03/evidence_family_map.json\n",
      "stdout": ""
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/update_evidence_index.py",
        "--check"
      ],
      "returncode": 1,
      "stderr": "PROOF_MTIME_FUTURE:artifacts/compat/AB.json.path_proof.txt\n",
      "stdout": "[evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC\n"
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/validate_evidence_paths.py"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    },
    {
      "cmd": [
        "bash",
        "ci/checks/check_evidence_index_hash.sh"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "ci/checks/check_mirror_schema.sh"
      ],
      "returncode": 1,
      "stderr": "PROOF_MTIME:140:2026-04-23T17:40:37Z\nPROOF_MTIME:141:2026-04-23T17:40:37Z\nPROOF_MTIME:148:2026-05-10T21:33:32Z\nPROOF_MTIME:149:2026-05-10T21:33:32Z\nPROOF_MTIME:260:2026-05-10T21:33:32Z\nPROOF_MTIME:261:2026-05-10T21:33:32Z\nPROOF_MTIME:262:2026-05-10T21:33:32Z\nPROOF_MTIME:263:2026-05-10T21:33:32Z\nPROOF_MTIME:264:2026-05-10T21:33:32Z\nPROOF_MTIME:265:2026-05-10T21:33:32Z\nPROOF_MTIME:266:2026-05-10T21:33:32Z\nPROOF_MTIME:267:2026-05-10T21:33:32Z\nPROOF_MTIME:268:2026-05-10T21:33:32Z\n",
      "stdout": ""
    }
  ],
  "schema": "hde_epic031.po008.evidence_coherence.v1",
  "status": "FAIL_BEHAVIOR"
}
```

### Outcome
FAIL_BEHAVIOR

### Notes
- `coherence_status` is `PASS`, but step status is `FAIL_BEHAVIOR` because nested commands are not all green.
- Plan “What to look for” includes `hash_sentinels_exist`; this field is not emitted by the current harness result schema.

## Step PO-009 — Machine mirror alignment and stale companion classification

### Commands executed
Preflight:

```bash
set -e
python --version
test -f audit/qa/hde-epic031/00_meta/live_qa_harness.py
test -f tools/evidence/generate_epic031_pr03_evidence_coherence.py
test -f ci/checks/check_mirror_schema.sh
test -f audit/qa/hde-epic031/pr-03/evidence_family_map.json
test -f artifacts/evidence_index.jsonl.path_proof.txt
test -f artifacts/evidence_index.jsonl.sha256
```

Execution:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-009
```

### Deliverables
- audit/qa/hde-epic031/checks/po-009/primary.log
- audit/qa/hde-epic031/checks/po-009/result.json

### Evidence output
#### primary.log (full content)
```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-009","check_name":"PO-009","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-009","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-009/primary.log","audit/qa/hde-epic031/checks/po-009/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T16:44:24Z"}
{
  "coherence_status": "PASS",
  "family_map_present": true,
  "family_map_type": "dict",
  "machine_mirror_present": true,
  "mirror_mentions_epic031": true,
  "schema": "hde_epic031.po009.mirror_alignment.v1",
  "status": "PASS"
}
```

#### result.json (full content)
```json
{
  "coherence_status": "PASS",
  "family_map_present": true,
  "family_map_type": "dict",
  "machine_mirror_present": true,
  "mirror_mentions_epic031": true,
  "schema": "hde_epic031.po009.mirror_alignment.v1",
  "status": "PASS"
}
```

### Outcome
PASS

### Notes
- Plan “What to look for” includes `mirror_path_proof_present` and nested command return codes; these fields are not emitted by the current harness result schema for PO-009.

## Summary
- PO-007: PASS
- PO-008: FAIL_BEHAVIOR
- PO-009: PASS
