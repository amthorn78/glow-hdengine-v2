# PO-016 Remediation Recommendation

**Issue:** CHECK D07_sanity_pipeline: PO-016 — FAILED  
**Root Cause:** pytest module not installed in Python environment  
**Date:** 2026-01-21  

---

## Problem Summary

The sanity pipeline failed on its first check:
```
check pytest tests/cli/test_cli_canonical_bytes.py:FAIL
```

Investigation reveals that `pytest` is not installed in the Python environment. When attempting to run pytest, the error message is:
```
/usr/local/bin/python: No module named pytest
```

---

## Root Cause Analysis

### Missing Dependencies

The repository has test infrastructure configured (pytest.ini exists with test markers and paths), but the required testing packages are not installed in the current environment:

**Missing packages:**
- `pytest` (test framework)
- Potentially other test dependencies

**Evidence:**
1. `pytest.ini` exists and defines test markers for multiple EPICs
2. `requirements-dev.txt` exists but only lists `jsonschema==4.23.0`
3. `pip list | grep pytest` returns no results
4. Running `python -m pytest` produces "No module named pytest"

### Why This Wasn't Caught Earlier

Previous QA steps (D01, D03, D04, D08) did not require pytest execution. The sanity pipeline (D07) is the first step that attempts to run pytest-based tests, revealing this missing dependency.

---

## Recommended Remediation

### Option 1: Install pytest (Quick Fix) ⭐ RECOMMENDED

**Action:**
```bash
pip install pytest
```

**Why recommended:**
- Fastest solution (under 1 minute)
- Addresses immediate blocker
- Standard testing tool, widely used
- No side effects

**Steps:**
1. Install pytest:
   ```bash
   cd /workspaces/glow-hdengine-v2
   pip install pytest
   ```

2. Re-run the sanity pipeline:
   ```bash
   python tools/evidence/run_sanity_pipeline_gate.py
   ```

3. Verify PASS status:
   ```bash
   cat audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log | head -1 | grep PASS
   ```

**Expected outcome:**
- Sanity pipeline completes all 17 checks
- D07 primary.log shows `"status":"PASS"`
- PO-016 acceptance criteria met

---

### Option 2: Install Complete Dev Dependencies

**Action:**
```bash
pip install pytest pytest-cov pytest-mock
```

**Why this option:**
- Installs pytest with common plugins
- Better for long-term development
- Prepares environment for future test runs

**Steps:**
1. Install pytest and common plugins:
   ```bash
   cd /workspaces/glow-hdengine-v2
   pip install pytest pytest-cov pytest-mock
   ```

2. Re-run sanity pipeline (same as Option 1 steps 2-3)

---

### Option 3: Create/Update requirements-dev.txt (Long-term Fix)

**Action:** Document the testing dependencies properly

**Steps:**
1. Update `requirements-dev.txt`:
   ```bash
   cat >> requirements-dev.txt << 'EOF'
   # Testing framework
   pytest>=7.4,<9.0
   pytest-cov>=4.1,<5.0
   pytest-mock>=3.12,<4.0
   EOF
   ```

2. Install from updated requirements:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Re-run sanity pipeline (same as Option 1 steps 2-3)

4. Commit the updated requirements-dev.txt:
   ```bash
   git add requirements-dev.txt
   git commit -m "Add pytest dependencies to requirements-dev.txt"
   ```

**Why this option:**
- Proper documentation of dev dependencies
- Reproducible environment setup
- Aligns with best practices
- Prevents this issue in future environments

---

## Detailed Remediation Steps (Option 1 - Recommended)

### Step 1: Install pytest
```bash
cd /workspaces/glow-hdengine-v2
pip install pytest
```

**Expected output:**
```
Collecting pytest
  Downloading pytest-X.Y.Z-py3-none-any.whl
...
Successfully installed pytest-X.Y.Z ...
```

### Step 2: Verify installation
```bash
python -m pytest --version
```

**Expected output:**
```
pytest X.Y.Z
```

### Step 3: Test the failing check independently
```bash
python -m pytest tests/cli/test_cli_canonical_bytes.py -v
```

**Expected output:**
```
tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical PASSED
tests/cli/test_cli_canonical_bytes.py::test_reader_dump_and_admin_sidecars_are_canonical PASSED
...
```

### Step 4: Re-run the full sanity pipeline
```bash
python tools/evidence/run_sanity_pipeline_gate.py
```

**Expected outcome:**
- Exit code: 0
- All 17 checks pass
- Gate log shows `summary:PASS`

### Step 5: Verify PO-016 PASS criteria
```bash
# Check exit code from previous command
echo $?  # Should be 0

# Check gate log exists
ls -la audit/gates/sanity_pipeline/sanity_pipeline.log

# Check primary log status
grep '"status":"PASS"' audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log
```

---

## Verification Checklist

After remediation, verify:

- [ ] `python -m pytest --version` works
- [ ] `python -m pytest tests/cli/test_cli_canonical_bytes.py -v` passes
- [ ] Sanity pipeline exits with code 0
- [ ] `audit/gates/sanity_pipeline/sanity_pipeline.log` contains `summary:PASS`
- [ ] `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log` contains `"status":"PASS"`
- [ ] All 17 sanity checks show `:OK` status

---

## Additional Considerations

### Other Potentially Missing Dependencies

The sanity pipeline runs 17 checks. After installing pytest, the following dependencies may also be required:

1. **Flask** (for generate_sampler_evidence.py):
   ```bash
   pip install Flask>=2.3,<3.0
   ```

2. **psycopg** (for database tests):
   ```bash
   pip install 'psycopg[binary]>=3.1,<3.3'
   ```

3. **gunicorn** (for server tests):
   ```bash
   pip install 'gunicorn>=21,<22'
   ```

**Recommendation:** Install from requirements.txt:
```bash
pip install -r requirements.txt
```

### Environment Setup Best Practice

For future consistency, consider adding a setup script or documentation:

**Create `scripts/setup_dev_env.sh`:**
```bash
#!/bin/bash
set -e
pip install -r requirements.txt
pip install -r requirements-dev.txt
echo "✅ Development environment setup complete"
```

---

## Timeline Estimate

**Option 1 (Quick Fix):**
- Install pytest: 30 seconds
- Re-run sanity pipeline: 2-5 minutes
- Verification: 30 seconds
- **Total: ~5 minutes**

**Option 3 (Long-term Fix):**
- Update requirements-dev.txt: 2 minutes
- Install dependencies: 1 minute
- Re-run sanity pipeline: 2-5 minutes
- Verification: 30 seconds
- **Total: ~8 minutes**

---

## Recommended Action Plan

**Immediate (to unblock PO-016):**
1. Run: `pip install pytest`
2. Run: `python tools/evidence/run_sanity_pipeline_gate.py`
3. Verify PASS status

**Follow-up (for long-term stability):**
1. Update `requirements-dev.txt` with pytest dependencies
2. Install from `requirements.txt` for runtime dependencies
3. Document environment setup procedure
4. Add to EPIC024 close-pack notes

---

## Success Criteria

PO-016 will PASS when:
1. ✅ Sanity pipeline exits with code 0
2. ✅ Gate log shows `summary:PASS`
3. ✅ D07 primary.log contains `"status":"PASS"`
4. ✅ All 17 sanity checks complete successfully

---

## Contact/Escalation

If the remediation does not resolve the issue:
- Check for additional missing dependencies in sanity pipeline output
- Review individual test failures for root causes
- Consider environment compatibility issues (Python version, OS dependencies)

---

*Remediation plan prepared: 2026-01-21*  
*Issue: PO-016 sanity pipeline FAIL*  
*Priority: HIGH (blocks EPIC024 progression)*
