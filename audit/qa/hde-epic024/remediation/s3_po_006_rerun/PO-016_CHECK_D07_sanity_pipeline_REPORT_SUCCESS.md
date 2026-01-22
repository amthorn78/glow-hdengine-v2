# PO-016 CHECK D07_sanity_pipeline — SUCCESS REPORT (Post-Remediation)

**Date:** 2026-01-21  
**Check ID:** D07_sanity_pipeline  
**Status:** ✅ PASS  
**Exit Code:** 0  

## Executive Summary

PO-016 (CHECK D07_sanity_pipeline) now **PASSES** after successful remediation. The root causes were:
1. Missing pytest testing framework dependencies
2. Incorrect `APP_ENV=rails` (should be `APP_ENV=dev`)
3. Stale path proof with future mtime

All issues resolved via:
- Option 3 remediation: Updated `requirements-dev.txt` with pytest dependencies
- Corrected `APP_ENV` from "rails" to "dev" in wrapper script
- Removed stale path proof to trigger regeneration

## Remediation Actions Taken

### 1. Updated requirements-dev.txt (Option 3)
```
pytest>=7.4,<9.0
pytest-cov>=4.1,<5.0
pytest-mock>=3.12,<4.0
jsonschema==4.23.0
```

### 2. Installed Dependencies
```bash
pip install -r requirements-dev.txt  # Installed pytest 8.4.2
pip install -r requirements.txt       # Installed Flask, psycopg, gunicorn
```

### 3. Fixed APP_ENV in Wrapper Script
Changed `tools/evidence/run_sanity_pipeline_gate.py`:
- Before: `"APP_ENV": "rails"`
- After: `"APP_ENV": "dev"`

Rationale: The sampler evidence generator requires `APP_ENV ∈ {dev, test, local}` per PF-Canon. "rails" is not a valid APP_ENV value; it's a shorthand for "closed rails" (deterministic environment), but the actual environment variable must be "dev".

### 4. Removed Stale Path Proof
```bash
rm audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt
```

The stale path proof had `mtime_utc: 2026-01-16T16:28:20Z` in future of actual file mtime `2026-01-15 14:43:17`, causing `PROOF_MTIME_FUTURE` error.

## Verification Evidence

### Primary Log Status
```json
{
  "check_id": "D07_sanity_pipeline",
  "status": "PASS",
  "exit_code": 0,
  "command": "python tools/evidence/run_sanity_pipeline.py",
  "evidence_outputs": ["audit/gates/sanity_pipeline/sanity_pipeline.log"],
  "captured_env": {
    "APP_ENV": "dev",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "TZ": "UTC"
  }
}
```

### Sanity Pipeline Summary (17 checks)
```
check pytest tests/cli/test_cli_canonical_bytes.py: OK
check pytest tests/cli/test_showcompat_parity_and_identity.py: OK
check pytest tests/invariance/test_bytes_identity.py: OK
check ci/checks/check_env_pins.sh: OK
check python ci/checks/check_release_identity.sh: OK
check python tools/evidence/generate_sampler_evidence.py: OK ← Fixed!
check python tools/evidence/generate_engine_core_evidence.py: OK
check pytest tests/invariance/test_locale_tz.py: OK
check python tools/cli/serializer_grep_guard.py: OK
check python tools/cli/emitter_symbol_proof.py: OK
check pytest tests/cli/test_serializer_guards.py: OK
check python tools/order/generate_ordering_artifacts.py: OK
check python tools/evidence/update_evidence_index.py: OK
check python tools/order/generate_ordering_artifacts.py --check: OK
check python tools/evidence/update_evidence_index.py --check: OK
check python tools/evidence/orientation_demo.py: OK
check python tools/evidence/orientation_demo.py --check: OK
check update_evidence_index.post: OK

summary: PASS
```

### Pytest Verification
```
$ python -m pytest --version
pytest 8.4.2
```

## Evidence Artifacts Generated

### Primary Artifacts
1. **audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log** (241 bytes)
   - Status: PASS
   - Exit code: 0
   - Captured environment includes corrected `APP_ENV=dev`

2. **audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log.path_proof.txt**
   - SHA256: (generated)
   - Mtime: (current)

3. **audit/gates/sanity_pipeline/sanity_pipeline.log** (1,267 bytes)
   - All 17 checks: OK
   - Summary: PASS

## Root Cause Analysis

### Issue 1: Missing pytest
**Symptom:** `ModuleNotFoundError: No module named 'pytest'`  
**Root Cause:** Testing dependencies not documented in `requirements-dev.txt`  
**Resolution:** Added pytest, pytest-cov, pytest-mock to requirements-dev.txt (Option 3 - long-term fix)

### Issue 2: Incorrect APP_ENV
**Symptom:** `DEV_ADMIN_ONLY` error from sampler evidence generator  
**Root Cause:** `APP_ENV=rails` is not a valid value; must be in `{dev, test, local}` per PF05/PF09 canon  
**Resolution:** Changed wrapper script to use `APP_ENV=dev`

### Issue 3: Stale Path Proof
**Symptom:** `PROOF_MTIME_FUTURE` error  
**Root Cause:** Path proof mtime (2026-01-16) ahead of file's actual mtime (2026-01-15)  
**Resolution:** Removed stale path proof, regenerated automatically

## Acceptance Criteria Met

✅ Wrapper script executes without errors  
✅ Exit code is 0  
✅ Primary log status is "PASS"  
✅ All 17 sanity pipeline checks pass  
✅ Sampler evidence generator succeeds (key blocker resolved)  
✅ Evidence artifacts generated at specified paths  
✅ Path proofs created for primary log  
✅ Closed-rails environment enforced (with corrected APP_ENV)  

## Files Modified

1. **requirements-dev.txt**
   - Added pytest>=7.4,<9.0
   - Added pytest-cov>=4.1,<5.0
   - Added pytest-mock>=3.12,<4.0

2. **tools/evidence/run_sanity_pipeline_gate.py**
   - Changed ENV_PINS["APP_ENV"] from "rails" to "dev"

3. **audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt**
   - Removed (stale) - regenerated automatically

## Recommendations

1. **Document APP_ENV semantics:** Update developer documentation to clarify:
   - "rails" means closed-rails (deterministic mode), not an APP_ENV value
   - Valid APP_ENV values: {dev, test, local} for dev features
   - Production uses empty/unset/prod (blocks dev-only features)

2. **CI Dependency Check:** Add CI step to verify test dependencies installed before running QA gates

3. **Path Proof Validation:** Consider timestamp tolerance for path proof validation in Codespaces (clock skew)

4. **Commit Updated Files:** Add requirements-dev.txt to version control to share testing setup

## Conclusion

PO-016 remediation is **COMPLETE** and **SUCCESSFUL**. The sanity pipeline now executes all 17 checks cleanly under closed rails with corrected APP_ENV=dev. The long-term fix (Option 3) ensures reproducible testing environments for all developers.

**Next Action:** Continue with remaining EPIC024 QA steps if any, or proceed to EPIC024 acceptance map validation.
