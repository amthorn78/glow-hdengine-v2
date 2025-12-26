# Combined D0 Scan Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-26

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/required_paths_scan.json

```json
{
  "captured_at_utc": "2025-12-26T20:38:07Z",
  "missing_count": 3,
  "missing_paths": [
    "tools/qa/emit_env_pins.sh",
    "tests/ops/test_machine_mirror_record.py",
    "tests/ops/test_mirror_schema.py"
  ],
  "paths": [
    {
      "exists": true,
      "path": "docs/acceptance_map_epic022.json"
    },
    {
      "exists": true,
      "path": "audit/qa/hde-epic022/token_evidence_matrix.md"
    },
    {
      "exists": true,
      "path": "tools/evidence/update_evidence_index.py"
    },
    {
      "exists": true,
      "path": "tools/evidence/run_sanity_pipeline.py"
    },
    {
      "exists": false,
      "path": "tools/qa/emit_env_pins.sh"
    },
    {
      "exists": true,
      "path": "tools/cli/generate_showcompat_artifacts.py"
    },
    {
      "exists": true,
      "path": "tests/cli/test_errors_parity.py"
    },
    {
      "exists": true,
      "path": "tests/cli/test_cli_canonical_bytes.py"
    },
    {
      "exists": true,
      "path": "tests/cli/test_cli_usage_and_errors.py"
    },
    {
      "exists": true,
      "path": "tests/ops/test_evidence_index.py"
    },
    {
      "exists": false,
      "path": "tests/ops/test_machine_mirror_record.py"
    },
    {
      "exists": false,
      "path": "tests/ops/test_mirror_schema.py"
    },
    {
      "exists": true,
      "path": "ci/checks/check_mirror_schema.sh"
    },
    {
      "exists": true,
      "path": "artifacts/math/freeze_pack_manifest.json"
    },
    {
      "exists": true,
      "path": "artifacts/math/release_id.txt"
    },
    {
      "exists": true,
      "path": "artifacts/math/release_id_recompute.log"
    },
    {
      "exists": true,
      "path": "artifacts/identity/service_identity.json"
    },
    {
      "exists": true,
      "path": "artifacts/identity/emitter_sha256.txt"
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/d0_scan.md

**Status**: File not found (does not exist in repository)

---

## File: audit/qa/hde-epic022/d0_scan.md

**Status**: File not found (does not exist in repository)

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log

```log
check_id: D0.1
status: FAIL_BEHAVIOR
started_at_utc: 2025-12-26T20:38:07Z
ended_at_utc: 2025-12-26T20:38:07Z
rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
pf_refs: PF20 — HDE-Phased Epics, §2.7.5.A2
tokens:
command: bash 'audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/tools/run_d0_1.sh'
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
exit_code: 10
--- stdout ---

--- stderr ---

```

---

## File: audit/qa/hde-epic022/stepd0_1_deviations.md

**Status**: File not found (does not exist in repository)

---

## Summary

**Files found**: 2 of 5 requested files
- ✓ required_paths_scan.json (3 missing paths identified)
- ✗ closeout/d0_scan.md (not found)
- ✗ d0_scan.md (not found)
- ✓ step_logs/D0.1_required_paths_scan_and_d0_scan_md.log (FAIL_BEHAVIOR, exit code 10)
- ✗ stepd0_1_deviations.md (not found)

**Key findings**:
- Missing 3 required paths: emit_env_pins.sh, test_machine_mirror_record.py, test_mirror_schema.py
- D0.1 check status: FAIL_BEHAVIOR (exit code 10)
- Empty stdout/stderr in log file suggests the run_d0_1.sh script may have failed early
