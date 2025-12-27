# Combined QA Files for run_20251226t181426z_e44b4cc (Step D0.1)

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/required_paths_scan.json

```json
{
  "captured_at_utc": "2025-12-26T23:07:02Z",
  "missing_count": 0,
  "missing_paths": [],
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
      "exists": true,
      "path": "ci/checks/check_mirror_schema.sh"
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/d0_scan.md

```markdown
# D0 Scan - EPIC022 required paths

run_id: run_20251226t181426z_e44b4cc
captured_at_utc: 2025-12-26T23:07:12Z

missing_count: 0

## Missing (none)

## Full scan
- [x] docs/acceptance_map_epic022.json
- [x] audit/qa/hde-epic022/token_evidence_matrix.md
- [x] tools/evidence/update_evidence_index.py
- [x] tools/evidence/run_sanity_pipeline.py
- [x] tools/cli/generate_showcompat_artifacts.py
- [x] tests/cli/test_errors_parity.py
- [x] tests/cli/test_cli_canonical_bytes.py
- [x] tests/cli/test_cli_usage_and_errors.py
- [x] tests/ops/test_evidence_index.py
- [x] ci/checks/check_mirror_schema.sh
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/d0_scan.md

```markdown
# D0 Scan - EPIC022 required paths

run_id: run_20251226t181426z_e44b4cc
captured_at_utc: 2025-12-26T23:07:12Z

missing_count: 0

## Missing (none)

## Full scan
- [x] docs/acceptance_map_epic022.json
- [x] audit/qa/hde-epic022/token_evidence_matrix.md
- [x] tools/evidence/update_evidence_index.py
- [x] tools/evidence/run_sanity_pipeline.py
- [x] tools/cli/generate_showcompat_artifacts.py
- [x] tests/cli/test_errors_parity.py
- [x] tests/cli/test_cli_canonical_bytes.py
- [x] tests/cli/test_cli_usage_and_errors.py
- [x] tests/ops/test_evidence_index.py
- [x] ci/checks/check_mirror_schema.sh
```

---

## File: audit/qa/hde-epic022/stepd0_1_deviations.md

```markdown
# STEP D0.1 deviations

None. Step executed via inline commands (no wrapper script).
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/closeout/stepd0_1_deviations.md

```markdown
# STEP D0.1 deviations

None. Step executed via inline commands (no wrapper script).
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log

```log
{"check_id": "D0.1", "command": "D0.1 inline required-path scan + d0_scan renderer (codespaces-safe; no exit)", "exit_code": 0, "pf_refs": [], "produced_at_utc": "2025-12-26T23:07:27Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "status": "PASS", "tokens": []}

=== required_paths_scan.json ===
{
  "captured_at_utc": "2025-12-26T23:07:02Z",
  "missing_count": 0,
  "missing_paths": [],
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
      "exists": true,
      "path": "ci/checks/check_mirror_schema.sh"
    }
  ]
}


=== d0_scan_md (stable path) ===
audit/qa/hde-epic022/d0_scan.md

=== deviations (stable path) ===
# STEP D0.1 deviations

None. Step executed via inline commands (no wrapper script).
```

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
{
  "steps": [
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T22:51:25Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:01:49Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:07:36Z",
      "status": "PASS"
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/d0_1_verdict.txt

```plaintext
PASS
```
