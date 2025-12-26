# Missing Paths Resolution Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-26  
Scan: D0.1_required_paths_scan

---

## Summary

**Expected paths**: 3 missing  
**Resolution status**: All 3 have actual equivalents at different locations

---

## Path Mappings (Expected → Actual)

### 1. ENV_PINS Tool

**Expected (missing):**
```
tools/qa/emit_env_pins.sh
```

**Actual (exists):**
```
ci/checks/check_env_pins.sh
```

**Details:**
- The env pins check is in `ci/checks/` not `tools/qa/`
- Script invokes: `python -m engine.runtime.determinism_env`
- Writes to: `audit/gates/determinism/env_pins.log`
- Used in sanity pipeline and referenced in EPIC022 token evidence matrix

---

### 2. Machine Mirror Record Test

**Expected (missing):**
```
tests/ops/test_machine_mirror_record.py
```

**Actual (exists):**
```
tests/evidence/test_machine_mirror_self_proof.py
```

**Details:**
- Test is in `tests/evidence/` not `tests/ops/`
- Tests machine mirror self-proof and canonical digest matching
- Validates mirror path proof and rendered records
- Contains 47 lines with test function: `test_machine_mirror_self_proof_matches_canonical_digest()`

---

### 3. Mirror Schema Test

**Expected (missing):**
```
tests/ops/test_mirror_schema.py
```

**Actual (exists):**
```
ci/checks/check_mirror_schema.sh
```

**Details:**
- Check is in `ci/checks/` not `tests/ops/`
- Despite `.sh` extension, it's actually a Python script (shebang: `#!/usr/bin/env python3`)
- Contains 230 lines with schema validation logic
- Defines `REQUIRED_KEYS` and `OPTIONAL_KEYS` for mirror record validation
- References: `docs/acceptance_map_epic020.json`

---

## Additional Evidence Files (Related)

### Environment Pins Evidence
- `audit/gates/determinism/env_pins.log` (canonical output)
- `audit/gates/determinism/env_pins.log.path_proof.txt`
- `artifacts/identity/env_pins.txt`
- `artifacts/cli/env_pins_epic021.log`
- `tests/cli/test_cli_env_pins_epic021.py`

### Mirror/Evidence Infrastructure
- `tools/evidence/update_evidence_index.py` (mirror generator)
- `docs/evidence/INDEX.json` (human-readable evidence index)
- `artifacts/evidence_index.jsonl` (machine mirror)

---

## Root Cause Analysis

The `required_paths_scan.json` expected paths appear to be based on:
1. **Outdated path assumptions** - files were never at those locations
2. **Namespace reorganization** - tests moved from `ops/` to `evidence/`
3. **Tool categorization** - some tools placed in `ci/checks/` rather than `tools/qa/`

These are not missing files - they exist with different names/locations than the scan expected.

---

## Recommendation

Update `audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/tools/run_d0_1.sh` or the underlying required paths list to use the actual file paths:

```bash
# Replace expected paths with actual paths:
- tools/qa/emit_env_pins.sh              → ci/checks/check_env_pins.sh
- tests/ops/test_machine_mirror_record.py → tests/evidence/test_machine_mirror_self_proof.py  
- tests/ops/test_mirror_schema.py         → ci/checks/check_mirror_schema.sh
```
