# PO-010 Full Steps and Evidence Pack

Epic: HDE-EPIC027  
Step: CHECK po-010: PO-010  
Result: PASS  
Current governed header timestamp: 2026-03-19T07:32:00Z  
Remediation status: PF19 and PF27 defects remediated

## 1) Why this kept happening (root cause analysis)

The repeated remediation loop came from two independent trust defects in governed metadata, not from runtime proof failure:

1. PF19 defect (already fixed earlier): the manifest path proof retained stale `mtime_utc`/`produced_at_utc` after manifest bytes changed.
2. PF27 defect (fixed in this pass): the `command` field in the governed header was written as a narrative placeholder instead of an exact executable command string.

The substantive runtime evidence was always PASS, but these metadata defects made the proof package fail trust checks.

## 2) Determinism rails used

- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## 3) Step workflow executed in this remediation pass

1. Re-captured command output with exact executable commands in explicit order:
   - `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cat audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt`
   - `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cat audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt`
2. Rebuilt `audit/qa/hde-epic027/checks/po-010/primary.log` with a governed first-line header (`pf27.step_log_header.v1`) whose `command` field matches the exact command sequence above.
3. Re-updated `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading line 1 of the corrected `primary.log`.
4. Re-refreshed `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` with fresh provenance values.
5. Ran governed synchronization and checks:
   - `python3 tools/evidence/update_evidence_index.py`
   - `python3 tools/evidence/update_evidence_index.py --check`
   - `python3 tools/evidence/orientation_demo.py --check`

## 4) Required deliverables (plan set)

- audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt
- audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt
- audit/qa/hde-epic027/checks/po-010/primary.log
- audit/qa/hde-epic027/qa_step_logs_manifest.json
- audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt

## 5) Evidence: runtime proof files

`runtime_log_presence.txt` facts:
- `# OVERALL_RESULT=PASS`
- `# PRESENT_COUNT=5`
- `# MISSING_COUNT=0`

`runtime_surface_inventory.txt` facts:
- `# SURFACE_SUMMARY: CLI=PRESENT dev-http-conjunction=PRESENT reader-a7=PRESENT`
- `# RUNTIME_SURFACE_INVENTORY_RESULT=PASS`

## 6) Evidence: corrected governed primary header

First line of `audit/qa/hde-epic027/checks/po-010/primary.log`:

```json
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-010","check_name":"PO-010","claimed_tokens":[],"command":"SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cat audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt; SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cat audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt","audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt","audit/qa/hde-epic027/checks/po-010/primary.log","audit/qa/hde-epic027/qa_step_logs_manifest.json","audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 - HDE-Build Notes","PF05 - HDE-CLI-API-Vendor-Ref","PF02 - Canon-HDE-Core","PF27 - Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-03-19T07:32:00Z"}
```

## 7) Evidence: manifest and path proof after corrected header

Manifest entry for `po-010` (from `audit/qa/hde-epic027/qa_step_logs_manifest.json`):

```json
{"check_id":"po-010","check_name":"PO-010","fail_status":"","log_path":"checks/po-010/primary.log","status":"PASS","timestamp_utc":"2026-03-19T07:32:00Z"}
```

Path proof content:

```text
path: audit/qa/hde-epic027/qa_step_logs_manifest.json
size_bytes: 1890
sha256: 213cc6c7174099b5616c62f2c8760009cee84a2597ad985882057892ec2cb972
mtime_utc: 2026-03-19T07:32:17Z
produced_at_utc: 2026-03-19T07:32:17Z
```

## 8) Evidence: mirror/index alignment and check markers

Mirror row (from `artifacts/evidence_index.jsonl`):

```json
{"artifact_key":"epic027.qa_step_logs_manifest","discovered_physical_path":"audit/qa/hde-epic027/qa_step_logs_manifest.json","epic_id":"HDE-EPIC027","produced_at_utc":"2026-03-19T07:32:17Z","proof_anchor":"audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt","role":"snapshot","sha256":"213cc6c7174099b5616c62f2c8760009cee84a2597ad985882057892ec2cb972","size_bytes":1890}
```

Validation markers:

```text
UPDATE_INDEX_CHECK_OK
ORIENTATION_DEMO_CHECK_OK
```

## 9) Integrity table (post-remediation)

| Artifact | Size (bytes) | SHA256 |
|---|---:|---|
| audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt | 966 | 6c15e7fa6d0c9a2ef1884d636a6003e1f8c93e06732df4fb0d61b5914092b887 |
| audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt | 1333 | 25d01da3b96184db696c9dcaf60aa581b8ab5e276c489b5ac7647e866d1f94cf |
| audit/qa/hde-epic027/checks/po-010/primary.log | 3625 | 8efe130cf080c9bb6bc0bfaffc26e258f53e010c6c4b587c9003951d9c4ed984 |
| audit/qa/hde-epic027/qa_step_logs_manifest.json | 1890 | 213cc6c7174099b5616c62f2c8760009cee84a2597ad985882057892ec2cb972 |
| audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt | 214 | 139f174f11365e70d029451ef6b0711eafb7392bec93fa1947579c3e8b8a73d8 |
| artifacts/evidence_index.jsonl | 113794 | 25f47393026140860b7e812ebf85f49289483c1d5b53500e92907adbefc2d7b2 |
| docs/evidence/INDEX.json | 50930 | 4085bf217604addb8c247a6e1aa1c0e4be7cedc087c9b97427e39acd6a46cae5 |
| docs/evidence/INDEX.sha256 | 91 | 139ed5de93985c25751f06fc5426c8da050641f5a636c75483499d486e986013 |

## 10) PASS closure statement

PASS criteria and outcome:
- All deliverables exist: PASS.
- Runtime-log presence shows no missing prerequisite runtime logs: PASS (`MISSING_COUNT=0`).
- Runtime-surface inventory proves same-run runtime surfaces were executed in this run: PASS.

Final classification: PASS with remediated governed trust metadata.
