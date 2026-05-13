# HDE-EPIC031 — Fermentation Pass 2 — Action Report (PO-007 to PO-009, Version 2)

Generated at (UTC): 2026-05-13T16:59:48Z
Source baseline: audit/qa/hde-epic031/checks/po-007-po-009_action_report.md

## Scope
This report captures final current-state evidence after Moon Loop remediation for:

- PO-007
- PO-008
- PO-009

Closed-rails posture:

- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Step PO-007

### Deliverables
- audit/qa/hde-epic031/checks/po-007/primary.log
- audit/qa/hde-epic031/checks/po-007/result.json

### Full evidence output
#### primary.log
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

#### result.json
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

## Step PO-008 (Moon Loop Remediated)

### Deliverables
- audit/qa/hde-epic031/checks/po-008/primary.log
- audit/qa/hde-epic031/checks/po-008/result.json

### Full evidence output
#### primary.log (includes in-session Moon Loop evidence stream)
```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-008","check_name":"PO-008","claimed_tokens":[],"command":"python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-008","command_provenance":"Copy/paste from plan","evidence_artifacts":["audit/qa/hde-epic031/checks/po-008/primary.log","audit/qa/hde-epic031/checks/po-008/result.json"],"exit_code":0,"fail_status":"","intended_tokens":[],"pf_refs":["PF10 \u2014 HDE-Build Notes","PF19 \u2014 Glow QA Guide","PF27 \u2014 Canon Plan Templates","PF06 \u2014 Epic Process Guide"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-05-13T16:53:30Z"}
{
  "all_commands_green": true,
  "coherence_status": "PASS",
  "commands": [
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/generate_epic031_pr03_evidence_coherence.py",
        "--check"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": "EPIC031_PR03_EVIDENCE_COHERENCE_OK\n"
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/update_evidence_index.py",
        "--check"
      ],
      "returncode": 0,
      "stderr": "",
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
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    }
  ],
  "schema": "hde_epic031.po008.evidence_coherence.v1",
  "status": "PASS"
}

MOON_LOOP_EVIDENCE_STREAM_BEGIN
failure_signature_excerpt: {"check_id":"po-008","status":"FAIL_BEHAVIOR","exit_code":1,"timestamp_utc":"2026-05-13T16:43:53Z","all_commands_green":false,"coherence_status":"PASS","failures":["STALE:audit/qa/hde-epic031/pr-03/evidence_family_map.json","PROOF_MTIME_FUTURE:artifacts/compat/AB.json.path_proof.txt","PROOF_MTIME:ci/checks/check_mirror_schema.sh"]}
remediation_note: refreshed governed coherence/index artifacts under closed rails via tools/evidence/generate_epic031_pr03_evidence_coherence.py and tools/evidence/update_evidence_index.py, and normalized artifacts/compat/AB.json + artifacts/compat/BA.json filesystem mtimes (bytes unchanged) to clear PROOF_MTIME_FUTURE blockers.
rerun_pass_excerpt: {"check_id":"po-008","status":"PASS","exit_code":0,"timestamp_utc":"2026-05-13T16:53:30Z","all_commands_green":true,"coherence_status":"PASS","commands_all_returncode_zero":true}
MOON_LOOP_EVIDENCE_STREAM_END
```

#### result.json
```json
{
  "all_commands_green": true,
  "coherence_status": "PASS",
  "commands": [
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/generate_epic031_pr03_evidence_coherence.py",
        "--check"
      ],
      "returncode": 0,
      "stderr": "",
      "stdout": "EPIC031_PR03_EVIDENCE_COHERENCE_OK\n"
    },
    {
      "cmd": [
        "/usr/local/bin/python",
        "tools/evidence/update_evidence_index.py",
        "--check"
      ],
      "returncode": 0,
      "stderr": "",
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
      "returncode": 0,
      "stderr": "",
      "stdout": ""
    }
  ],
  "schema": "hde_epic031.po008.evidence_coherence.v1",
  "status": "PASS"
}
```

### Outcome
PASS

## Step PO-009

### Deliverables
- audit/qa/hde-epic031/checks/po-009/primary.log
- audit/qa/hde-epic031/checks/po-009/result.json

### Full evidence output
#### primary.log
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

#### result.json
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

## Moon Loop Provenance (PO-008)

### Delta artifact paths
- audit/qa/hde-epic031/remediation/moon_loop/patch.diff
- audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt
- audit/qa/hde-epic031/00_meta/doc_deltas.md

### changed_files.txt (PO-008 section)
```text
# PO-008 moon loop remediation
# generated_at_utc: 2026-05-13T16:58:45Z
audit/qa/hde-epic031/checks/po-008/primary.log 19cb7bc40b14d9778fbb28398898db394f5c36a92f3c8e0ddc85a4043ef5e474
audit/qa/hde-epic031/checks/po-008/result.json 354865705e127cad3480a09155fc67a75f357add17b757453117659f8c63de2c
audit/qa/hde-epic031/pr-03/evidence_family_map.json d71ef9a543d43be1822e270ec7c912039c8c90b8f058d665c222f0353dc28df6
audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json a62fc187d5aa69cbe493a61b0c5ccff11582353c0d96b63e421290849ba82c33
audit/qa/hde-epic031/pr-03/evidence_refresh.log 0be1d384e1ac7b0a249606256f86236fce0a45d84920a2cfc0053993addc2000
docs/evidence/INDEX.json 7c3888fd4a5d9a8f2e5c36ef62a40adf811a0507bb0e194a5164eed10a5a270d
docs/evidence/INDEX.sha256 94c5648876afb7192f92e7043abde0f4783a0492338da7ea0add6c870ca7535d
artifacts/evidence_index.jsonl 537e8b0b27858131aed581460dd074fa002965216ce19987d0cc3c325db45017
artifacts/evidence_index.jsonl.sha256 1a94aad5e2607e6e81bf13ee985c472fd186368a70b99e05d186d8f7d3751dc8
artifacts/evidence_index.jsonl.path_proof.txt 67ee0166133a10d3ef1f4c73dcdab17a3b2af7c87302b2eb4e67bde0666687b3
artifacts/compat/AB.json f4616998ad4ce55dc7c716388709f767718a4d3056d866f9c2f73fa4f4703ed7
artifacts/compat/BA.json f4616998ad4ce55dc7c716388709f767718a4d3056d866f9c2f73fa4f4703ed7
```

## Final status

- PO-007: PASS
- PO-008: PASS (after Moon Loop remediation)
- PO-009: PASS
