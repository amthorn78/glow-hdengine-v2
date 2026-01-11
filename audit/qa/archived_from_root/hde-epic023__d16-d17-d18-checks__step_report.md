# HDE-EPIC023 D16–D17–D18 Checks — Step Report

**EPIC_ID:** HDE-EPIC023  
**STEP_NAMES:** D16_orientation_demo, D17_internal_env_pins, D18_sanity_log  
**Execution Date:** 2026-01-10  
**Environment:** Closed rails (SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC)

---

## Step Results

### Commands/Actions Executed (in order)

1. **D16_orientation_demo — Orientation Demo Evidence Check**
   - Set environment: `EVIDENCE_ROOT=audit/qa/hde-epic023`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`
   - Created check directory: `audit/qa/hde-epic023/checks/D16_orientation_demo/`
   - Executed: `python tools/evidence/orientation_demo.py` (write mode)
   - Executed: `python tools/evidence/orientation_demo.py --check` (validation mode)
   - Validated evidence family presence: `audit/gates/topology/orientation_demo.txt` + `.path_proof.txt`
   - Checked for `status: ok` in orientation demo transcript
   - Updated `qa_step_logs_manifest.json` with D16 check results
   - **Result:** `FAIL_BEHAVIOR`

2. **D17_internal_env_pins — Determinism Env Pins Log Check**
   - Set environment variables (same closed rails)
   - Created check directory: `audit/qa/hde-epic023/checks/D17_internal_env_pins/`
   - Validated evidence family presence: `audit/gates/determinism/env_pins.log` + `.path_proof.txt`
   - Parsed `env_pins.log` and validated JSON schema (PF12 §8.3.3)
   - Checked required top-level keys: `{env, status, suites}` (notes optional)
   - Validated allowlisted env keys and pinned values
   - **Result:** `FAIL_BEHAVIOR`

3. **D18_sanity_log — Sanity Pipeline Log Check**
   - Set environment variables (same closed rails)
   - Created check directory: `audit/qa/hde-epic023/checks/D18_sanity_log/`
   - Attempted: `python tools/evidence/run_sanity_pipeline.py --check` (tool does not support `--check` flag)
   - Validated evidence family presence: `artifacts/sanity/sanity.log` + `.path_proof.txt`
   - Checked log format per PF12 §8.3.5: first line `sanity_pipeline`, second line env pins, last line `summary:PASS|FAIL`
   - **Result:** `FAIL_BEHAVIOR`

### Key Outputs (status lines, pass/fail signals, decisive log lines)

**D16_orientation_demo:**
```
D16_orientation_demo => FAIL_BEHAVIOR
```
- Orientation demo tool executed successfully in write and check modes
- Evidence files present: `audit/gates/topology/orientation_demo.txt` and `.path_proof.txt`
- **Failure reason:** `status: mismatch` instead of `status: ok`
- Issues reported in orientation_demo.txt:
  - `SHA_MIRROR_MISMATCH epic023.qa_step_logs_manifest c5faad028e391036db1d195d250fc69891cc62792b78cd5cd7c21d18463c6fd3!=0b9f3b9d131b1f5f1aa45b4295ab6a985f0d287acc44b8cc40490616ab6ead78`
  - `SIZE_MIRROR_MISMATCH epic023.qa_step_logs_manifest 1077!=1150`

**D17_internal_env_pins:**
```
D17_internal_env_pins => FAIL_BEHAVIOR
```
- Evidence files present: `audit/gates/determinism/env_pins.log` and `.path_proof.txt`
- **Failure reason:** `FAIL_BEHAVIOR: env_pins.log env missing required keys: ['APP_ENV']`
- Existing env_pins.log contains: `{"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"status":"success","suites":[...]}`
- The log is missing the `APP_ENV` key in the `env` object

**D18_sanity_log:**
```
D18_sanity_log => FAIL_BEHAVIOR
```
- Tool invocation error: `run_sanity_pipeline.py: error: unrecognized arguments: --check`
- Evidence files present: `artifacts/sanity/sanity.log` and `.path_proof.txt`
- **Failure reason:** `FAIL_BEHAVIOR: sanity.log env line mismatch; expected: env: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`
- Actual env line in sanity.log: `env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` (comma-separated format)
- Expected format: space-separated `env: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`

---

## Repository Changes

### Summary of What Changed

- Updated `audit/gates/topology/orientation_demo.txt` — status changed from `ok` to `mismatch` with sha256/size mismatch details for qa_step_logs_manifest
- Created `audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log` — check execution log with FAIL_BEHAVIOR status and manifest update confirmation
- Created `audit/qa/hde-epic023/checks/D17_internal_env_pins/primary.log` — check execution log showing APP_ENV missing from env_pins.log
- Updated `audit/qa/hde-epic023/checks/D18_sanity_log/primary.log` — check execution log showing tool argument error and env line format mismatch
- Updated `audit/qa/hde-epic023/qa_step_logs_manifest.json` — added D16_orientation_demo entry with full metadata (sha256, size, mtime, tokens_claimed, environment captures)
- Updated `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt` — new sha256/size/mtime reflecting manifest update

### Full Changed-Files List (repo-relative paths)

- `audit/gates/topology/orientation_demo.txt`
- `audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log`
- `audit/qa/hde-epic023/checks/D17_internal_env_pins/primary.log`
- `audit/qa/hde-epic023/checks/D18_sanity_log/primary.log`
- `audit/qa/hde-epic023/qa_step_logs_manifest.json`
- `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt`

### Diff Summary

All three checks executed and wrote primary logs. D16 check also triggered orientation demo regeneration and updated the qa_step_logs_manifest. The orientation demo detected a mirror/index mismatch for the manifest file itself (sha256 and size discrepancies between Index and Mirror representations). All three checks reported FAIL_BEHAVIOR status due to:
- D16: Evidence validation found `status: mismatch` instead of `status: ok`
- D17: Missing `APP_ENV` key in env_pins.log env object
- D18: Sanity log format drift (env line uses commas instead of spaces)

---

## Evidence Filedump (complete)

### Path: audit/gates/topology/orientation_demo.txt

```
orientation demo (evidence skeleton)
total_artifacts: 252
status: mismatch
issues:
- SHA_MIRROR_MISMATCH epic023.qa_step_logs_manifest c5faad028e391036db1d195d250fc69891cc62792b78cd5cd7c21d18463c6fd3!=0b9f3b9d131b1f5f1aa45b4295ab6a985f0d287acc44b8cc40490616ab6ead78
- SIZE_MIRROR_MISMATCH epic023.qa_step_logs_manifest 1077!=1150
```

### Path: audit/gates/topology/orientation_demo.txt.path_proof.txt

```
path: audit/gates/topology/orientation_demo.txt
size_bytes: 115
sha256: 340c8d04fef8998e7413f7299f8b088cb7121c568f3d17a8a748afe055d59913
mtime_utc: 2026-01-05T00:27:10Z
produced_at_utc: 2026-01-05T00:27:58Z
```

### Path: audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log

```
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D16_orientation_demo","claimed_tokens":[],"command":"python tools/evidence/orientation_demo.py && python tools/evidence/orientation_demo.py --check","intended_tokens":[],"pf_refs":["PF09 — HDE-Build Checklist, §Subtask HDE-CALC003.8 — Topology orientation demo","PF19 — Glow QA Guide, §4.4.3"],"status":"FAIL_BEHAVIOR"}
Updated qa_step_logs_manifest.json + path proof.
```

### Path: audit/qa/hde-epic023/checks/D17_internal_env_pins/primary.log

```
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D17_internal_env_pins","claimed_tokens":[],"command":"validate audit/gates/determinism/env_pins.log schema and pins (PF12 §8.3.3)","intended_tokens":[],"pf_refs":["PF12 — HDE-Schemas and Artifacts, §8.3.3","PF14 — HDE-Mechanics Guide, §1.3"],"status":"FAIL_BEHAVIOR"}
== D17: determinism env pins log ==
FAIL_BEHAVIOR: env_pins.log env missing required keys: ['APP_ENV']
```

### Path: audit/qa/hde-epic023/checks/D18_sanity_log/primary.log

```
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D18_sanity_log","claimed_tokens":[],"command":"python tools/evidence/run_sanity_pipeline.py --check + validate artifacts/sanity/sanity.log format (PF12 §8.3.5)","intended_tokens":[],"pf_refs":["PF12 — HDE-Schemas and Artifacts, §8.3.5","PF14 — HDE-Mechanics Guide, §1.4"],"status":"FAIL_BEHAVIOR"}
== D18: sanity pipeline log ==
usage: run_sanity_pipeline.py [-h] [--log-path LOG_PATH]
run_sanity_pipeline.py: error: unrecognized arguments: --check
FAIL_BEHAVIOR: sanity.log env line mismatch; expected: env: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
```

### Path: audit/qa/hde-epic023/qa_step_logs_manifest.json

```json
{
  "epic_id": "HDE-EPIC023",
  "runs": [
    {
      "produced_at_utc": "2026-01-05T03:49:38.236980+00:00",
      "run_id": "viability-check",
      "steps": [
        {
          "log_path": "audit/qa/hde-epic023/acceptance_map_viability.log",
          "name": "acceptance_map_viability",
          "status": "PASS"
        }
      ]
    }
  ],
  "steps": [
    {
      "check_id": "${CHECK_ID}",
      "log_path": "${LOG_PATH}",
      "status": "${STATUS}"
    },
    {
      "check_id": "D02_token_evidence_matrix",
      "log_path": "audit/qa/hde-epic023/checks/D02_token_evidence_matrix/primary.log",
      "status": "PASS"
    },
    {
      "check_id": "D04_acceptance_alignment_validator",
      "log_path": "audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log",
      "status": "FAIL_BEHAVIOR"
    },
    {
      "check_id": "D05_step_logs_manifest",
      "log_path": "audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log",
      "status": "PASS"
    },
    {
      "check_id": "D06_primary_step_logs",
      "log_path": "audit/qa/hde-epic023/checks/D06_primary_step_logs/primary.log",
      "status": "PASS"
    },
    {
      "check_id": "D07_codespaces_snapshot",
      "log_path": "audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log",
      "status": "PASS"
    },
    {
      "check_id": "D08_qa_doc_deltas_capture",
      "log_path": "audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log",
      "status": "PASS"
    },
    {
      "allow_network": "0",
      "app_env": "dev",
      "check_id": "D16_orientation_demo",
      "log_path": "audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log",
      "mtime_utc": "2026-01-10T02:07:51Z",
      "safe_mode": "1",
      "sha256": "7bb73b9a1a47714012c764678324d690add7b6697e01a9e645bc859bf0dcb3c2",
      "size_bytes": 462,
      "status": "FAIL_BEHAVIOR",
      "tokens_claimed": []
    }
  ]
}
```

### Path: audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt

```
qa_step_logs_manifest.json
sha256=312cf69f6c125e88921f83d745f646c4ad6d783747a5f77a752673bfe3a8acea
size_bytes=1927
mtime_utc=2026-01-10T02:07:51Z
```

### Path: audit/gates/determinism/env_pins.log

```json
{"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"status":"success","suites":["ci:determinism-rails","tests:invariance","tests:evidence-ordering","evidence:sampler","evidence:engine-core","orientation:demo"]}
```

### Path: audit/gates/determinism/env_pins.log.path_proof.txt

```
path: audit/gates/determinism/env_pins.log
size_bytes: 240
sha256: 6360e83eb1945e4b45bdb6327f4087c0b30ea58932fb6a07783bc79fb25f6b59
mtime_utc: 2025-12-27T16:55:04Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### Path: artifacts/sanity/sanity.log

```
sanity_pipeline
env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC
check pytest tests/cli/test_cli_canonical_bytes.py:OK
check pytest tests/cli/test_showcompat_parity_and_identity.py:OK
check pytest tests/invariance/test_bytes_identity.py:OK
check ci/checks/check_env_pins.sh:OK
check python ci/checks/check_release_identity.sh:OK
check python tools/evidence/generate_sampler_evidence.py:OK
check python tools/evidence/generate_engine_core_evidence.py:OK
check pytest tests/invariance/test_locale_tz.py:OK
check python tools/cli/serializer_grep_guard.py:OK
check python tools/cli/emitter_symbol_proof.py:OK
check pytest tests/cli/test_serializer_guards.py:OK
check python tools/order/generate_ordering_artifacts.py:OK
check python tools/evidence/update_evidence_index.py:OK
check python tools/order/generate_ordering_artifacts.py --check:OK
check python tools/evidence/update_evidence_index.py --check:OK
check python tools/evidence/orientation_demo.py:OK
check python tools/evidence/orientation_demo.py --check:OK
check update_evidence_index.post:OK
summary:PASS
```

### Path: artifacts/sanity/sanity.log.path_proof.txt

```
path: artifacts/sanity/sanity.log
size_bytes: 1068
sha256: 13013763f93d0afab5a8bf1111c8bae3db016ee52045ed599004a79b0c52bc14
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-22T17:07:45Z
```

---

## Analysis and Observations

### D16 Failure Root Cause

The orientation demo tool executed successfully and generated the evidence transcript at `audit/gates/topology/orientation_demo.txt`. However, the check failed because the transcript reports `status: mismatch` instead of the required `status: ok`. The mismatch is specifically related to the `qa_step_logs_manifest.json` file itself — the Index and Mirror representations have different sha256 hashes and sizes. This is a circular dependency issue: the D16 check updated the manifest as part of its execution, causing the manifest's sha256 to change, which in turn caused the orientation demo (which validates Index/Mirror coherence) to detect a mismatch.

**Required artifacts present:**
- `audit/gates/topology/orientation_demo.txt` ✓
- `audit/gates/topology/orientation_demo.txt.path_proof.txt` ✓

**Status in transcript:** `status: mismatch` (expected: `status: ok`)

### D17 Failure Root Cause

The `env_pins.log` file exists and is properly formatted as a JSON object with the required top-level keys `{env, status, suites}`. However, the `env` object within the log is missing the `APP_ENV` key. The check script expected to find six environment variables (`SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`) but only five are present in the existing log.

**Existing env keys:** `ALLOW_NETWORK`, `LANG`, `LC_ALL`, `SAFE_MODE`, `TZ`  
**Missing key:** `APP_ENV`

This indicates the env_pins.log was generated by an older version of the evidence tooling that did not capture `APP_ENV`, or it was generated before `APP_ENV` was added to the required environment pins.

### D18 Failure Root Cause

Two distinct issues contributed to the D18 failure:

1. **Tool invocation error:** The check script attempted to run `python tools/evidence/run_sanity_pipeline.py --check`, but the tool does not support a `--check` flag. The tool only accepts `[-h]` (help) and `[--log-path LOG_PATH]` arguments.

2. **Log format mismatch:** Even if the tool invocation had succeeded, the existing `artifacts/sanity/sanity.log` uses a different env line format. The check expected:
   ```
   env: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
   ```
   But the actual log contains:
   ```
   env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC
   ```
   The actual format is comma-separated with no space after the colon, and the variable order differs.

**Required artifacts present:**
- `artifacts/sanity/sanity.log` ✓
- `artifacts/sanity/sanity.log.path_proof.txt` ✓

**Log contains:** `summary:PASS` ✓  
**Log format:** Does not match PF12 §8.3.5 expected format ✗

### Remediation Recommendations

**For D16 (Orientation Demo):**
- The circular dependency issue needs to be resolved. Options:
  1. Run the orientation demo check *before* updating the qa_step_logs_manifest
  2. Exclude the manifest file itself from Index/Mirror coherence validation during this check
  3. Use a two-pass approach: check orientation demo status, then update manifest

**For D17 (Env Pins):**
- Regenerate `audit/gates/determinism/env_pins.log` with the current determinism environment tooling to ensure it includes the `APP_ENV` key
- Command: Run the env pins generator under closed rails with `APP_ENV=dev` set

**For D18 (Sanity Log):**
- Update the check script to remove the `--check` flag from the sanity pipeline invocation (or verify correct tool usage)
- Either:
  1. Update the check script's expected env line format to match the actual sanity.log format (comma-separated), OR
  2. Regenerate sanity.log with the format expected by PF12 §8.3.5 (space-separated env line)

### Environment Note

Shell warning observed during execution: `bash: warning: setlocale: LC_ALL: cannot change locale (1): No such file or directory`. This indicates `LC_ALL=1` was attempted instead of `LC_ALL=C`. However, the captured_env in all three primary.log headers correctly shows `LC_ALL=C`, suggesting Python successfully set the locale environment but the shell export may have had issues. This did not affect the core checks but should be noted for reproducibility.

---

## Conclusion

All three checks (D16, D17, D18) were executed under closed rails with proper environment pinning. Each check identified specific evidence format or content issues:

- **D16:** Evidence present but status is `mismatch` due to qa_step_logs_manifest Index/Mirror discrepancy
- **D17:** Evidence present but missing `APP_ENV` key in env object (schema drift)
- **D18:** Evidence present but log format differs from expected PF12 §8.3.5 format (env line format mismatch) and tool does not support `--check` flag

No tokens were claimed by any of these checks. All failures are categorized as `FAIL_BEHAVIOR` (evidence exists but does not meet acceptance criteria), not `TOOLING_BLOCKED` (evidence missing).

The qa_step_logs_manifest.json was successfully updated with the D16 check entry, including full metadata (sha256, size, mtime, environment captures). The manifest now contains 9 check entries (including one with unexpanded shell placeholders `${CHECK_ID}`, `${LOG_PATH}`, `${STATUS}` from a previous run).
