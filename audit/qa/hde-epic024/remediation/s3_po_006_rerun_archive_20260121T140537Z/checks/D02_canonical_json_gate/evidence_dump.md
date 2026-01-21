# HDE-EPIC024 — CHECK D02_canonical_json_gate: PO-001 — Evidence Dump

**Generated:** 2026-01-19 (UTC)  
**Epic:** HDE-EPIC024  
**Step:** CHECK D02_canonical_json_gate: PO-001  
**Purpose:** Complete content capture of all canonical JSON gate evidence artifacts  

---

## Evidence Artifact Index

This dump contains the full content of each evidence artifact verified and generated during the D02 canonical JSON gate check:

1. `tools/evidence/run_canonical_json_gate.py` (Command entrypoint - not dumped, script file)
2. `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (Canonical gate log - FULL CONTENT)
3. `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log` (D02 primary log - FULL CONTENT)

---

## Evidence Artifact 1: Command Entrypoint

**File Path:** `tools/evidence/run_canonical_json_gate.py`  
**Type:** Python script (command entrypoint)  
**Status:** Executed successfully  
**Exit Code:** 0  

### Execution Details
- **Working Directory:** `/workspaces/glow-hdengine-v2`
- **Command:** `python tools/evidence/run_canonical_json_gate.py`
- **STDOUT:** (empty)
- **STDERR:** (empty)
- **Exit Code:** 0

**Note:** Script content not included in evidence dump (Python source file).

---

## Evidence Artifact 2: Canonical JSON Gate Check Log

**File Path:** `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
**Classification:** Governed log (NDJSON)  
**Format:** Newline-delimited JSON  
**Line Count:** 6 records  
**Verified:** 2026-01-19  

### Full Content

```jsonl
{"artifact":"cli_ab_stdout","canonical_sha256":"daf6660a2ee8c6a24717712e834a9c7e900c1e25dff29f3bdfa72817400c0ed9","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/ab.json","schema":"canonical_json.check.v1","sha256":"daf6660a2ee8c6a24717712e834a9c7e900c1e25dff29f3bdfa72817400c0ed9","size_bytes":1895,"status":"pass","trailing_lf":true}
{"artifact":"cli_ba_stdout","canonical_sha256":"daf6660a2ee8c6a24717712e834a9c7e900c1e25dff29f3bdfa72817400c0ed9","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/ba.json","schema":"canonical_json.check.v1","sha256":"daf6660a2ee8c6a24717712e834a9c7e900c1e25dff29f3bdfa72817400c0ed9","size_bytes":1895,"status":"pass","trailing_lf":true}
{"artifact":"cli_reader_dump","canonical_sha256":"1c8009b23095fb556225864f04136839ac4433b656465055379235db604fef42","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/reader_dump.json","schema":"canonical_json.check.v1","sha256":"1c8009b23095fb556225864f04136839ac4433b656465055379235db604fef42","size_bytes":320,"status":"pass","trailing_lf":true}
{"artifact":"cli_showcompat_args","canonical_sha256":"fc4a57cad8a099a3b7a3c947fd66d0b47b56145e6e1d90eba5743d5c2704a8c0","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/showcompat/args.json","schema":"canonical_json.check.v1","sha256":"fc4a57cad8a099a3b7a3c947fd66d0b47b56145e6e1d90eba5743d5c2704a8c0","size_bytes":800,"status":"pass","trailing_lf":true}
{"artifact":"cli_showcompat_stdout","canonical_sha256":"affb9ce0b9cb1d69932287ac7913ac243562005b10e7ba8cade9b0d27d26232f","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/showcompat/stdout.json","schema":"canonical_json.check.v1","sha256":"affb9ce0b9cb1d69932287ac7913ac243562005b10e7ba8cade9b0d27d26232f","size_bytes":1901,"status":"pass","trailing_lf":true}
{"artifact":"cli_summary","canonical_sha256":"f9b98777b3b62fe2818d8038f84249c286fe0cb3e72523f38868fab69b54277c","checked_at_utc":"2026-01-05T01:22:11Z","issues":[],"match":true,"path":"artifacts/cli/summary.json","schema":"canonical_json.check.v1","sha256":"f9b98777b3b62fe2818d8038f84249c286fe0cb3e72523f38868fab69b54277c","size_bytes":548,"status":"pass","trailing_lf":true}
```

### Summary Statistics
- **Total artifacts checked:** 6
- **Schema version:** canonical_json.check.v1
- **Check timestamp:** 2026-01-05T01:22:11Z
- **All status:** pass (100%)
- **All match:** true (100%)
- **All trailing_lf:** true (100%)
- **No issues:** 0 issues across all artifacts

### Artifacts Validated
1. `cli_ab_stdout` → `artifacts/cli/ab.json` (1895 bytes, sha256: daf6660a...)
2. `cli_ba_stdout` → `artifacts/cli/ba.json` (1895 bytes, sha256: daf6660a...)
3. `cli_reader_dump` → `artifacts/cli/reader_dump.json` (320 bytes, sha256: 1c8009b2...)
4. `cli_showcompat_args` → `artifacts/cli/showcompat/args.json` (800 bytes, sha256: fc4a57ca...)
5. `cli_showcompat_stdout` → `artifacts/cli/showcompat/stdout.json` (1901 bytes, sha256: affb9ce0...)
6. `cli_summary` → `artifacts/cli/summary.json` (548 bytes, sha256: f9b98777...)

---

## Evidence Artifact 3: D02 Primary Log

**File Path:** `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`  
**Classification:** QA check log  
**Format:** JSON header + structured sections  
**Verified:** 2026-01-19  

### Full Content

```log
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D02_canonical_json_gate","claimed_tokens":[],"command":"python tools/evidence/run_canonical_json_gate.py","evidence_outputs":["audit/gates/json_gate/canonical/json_gate_check_log.ndjson","audit/gates/json_gate/canonical/json_gate_compare_log.ndjson","audit/gates/json_gate/canonical/json_gate_structured_record.json"],"exit_code":0,"intended_tokens":[],"pf_refs":[],"status":"PASS"}
== STDOUT ==


== STDERR ==


== RC ==
0

```

### Header Analysis (JSON)

```json
{
  "captured_env": {
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC"
  },
  "check_id": "D02_canonical_json_gate",
  "claimed_tokens": [],
  "command": "python tools/evidence/run_canonical_json_gate.py",
  "evidence_outputs": [
    "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_structured_record.json"
  ],
  "exit_code": 0,
  "intended_tokens": [],
  "pf_refs": [],
  "status": "PASS"
}
```

### Key Fields
- **status:** PASS ✅ (pass criterion satisfied)
- **exit_code:** 0 (command succeeded)
- **check_id:** D02_canonical_json_gate
- **command:** python tools/evidence/run_canonical_json_gate.py
- **evidence_outputs:** 3 artifacts listed
  1. json_gate_check_log.ndjson
  2. json_gate_compare_log.ndjson
  3. json_gate_structured_record.json
- **claimed_tokens:** [] (empty)
- **intended_tokens:** [] (empty)
- **pf_refs:** [] (empty)

### Environment Pins (Closed Rails)
- `ALLOW_NETWORK`: 0 ✅
- `APP_ENV`: dev
- `LANG`: C ✅
- `LC_ALL`: C ✅
- `SAFE_MODE`: 1 ✅
- `TZ`: UTC ✅

**Determinism Environment:** All required pins present and correct.

### Output Sections
- **STDOUT:** Empty (no output)
- **STDERR:** Empty (no errors)
- **RC:** 0 (success)

---

## Cross-Reference Validation

### Gate Log ↔ Primary Log Consistency
- **Gate log check timestamp:** 2026-01-05T01:22:11Z
- **Primary log captured_env:** Closed rails confirmed
- **All gate log records:** status=pass, match=true, issues=[]
- **Primary log status:** PASS
- **Primary log exit_code:** 0

**Consistency Check:** ✅ Gate log shows all artifacts passing canonical checks; primary log confirms overall PASS status and successful execution.

### Evidence Outputs Declared vs. Actual
Primary log declares 3 evidence outputs:
1. ✅ `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (confirmed exists)
2. ⚠️  `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` (not verified in this step)
3. ⚠️  `audit/gates/json_gate/canonical/json_gate_structured_record.json` (not verified in this step)

**Note:** Only `json_gate_check_log.ndjson` was required by Approved Plan for Step D02. Other declared outputs not verified as part of this QA step's scope.

---

## Governance Notes

1. **Read-Only Status:** All canonical JSON gate artifacts are governed and should not be manually edited.
2. **Evidence Chain:** These artifacts support EPIC024 acceptance-map validation and token matrix evidence requirements.
3. **Schema Version:** All gate log records use `canonical_json.check.v1` schema.
4. **Timestamp Preservation:** Gate log records include explicit UTC check timestamps.
5. **Determinism Confirmed:** Closed rails environment pins verified in primary log header.

---

## Conclusion

All three evidence artifacts exist and contain valid data. The canonical JSON gate executed successfully with exit code 0, produced a 6-record gate log showing all artifacts passed canonical format validation, and the D02 primary log header confirms PASS status.

**Step D02 Evidence:** Complete and consistent ✅

---

**Evidence Dump End**
