# Combined QA Files for run_20251226t181426z_e44b4cc (Step 0B)

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/00_meta/doc_deltas.md

```markdown
# Doc Delta Capture — HDE-EPIC022

run_id: run_20251226t181426z_e44b4cc
captured_at_utc: 2025-12-26T18:41:55Z

## Known items (from plan review; must be reconciled)

- Token registry drift posture applies (PF10 — HDE-Build Notes, §2.7). Step 0D records concrete PF04 validation results.
- /internal/version conditional headers filename conflict exists across canon homes; see ADR-001 in this resubmission.
- showcompat checksum sidecar normalization for EPIC022 applies (PF10 — HDE-Build Notes, §2.5).

## No other deltas captured at this step.
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0B_doc_delta_capture.log

```log
check_id: 0B
status: PASS
started_at_utc: 2025-12-26T18:41:55Z
ended_at_utc: 2025-12-26T18:41:55Z
rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
pf_refs: PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.7
tokens: DOC_DELTA_PRESENT_OK
command: set -euo pipefail
    OUT="audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/00_meta/doc_deltas.md"
    {
      echo "# Doc Delta Capture — HDE-EPIC022"
      echo
      echo "run_id: run_20251226t181426z_e44b4cc"
      echo "captured_at_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
      echo
      echo "## Known items (from plan review; must be reconciled)"
      echo
      echo "- Token registry drift posture applies (PF10 — HDE-Build Notes, §2.7). Step 0D records concrete PF04 validation results."
      echo "- /internal/version conditional headers filename conflict exists across canon homes; see ADR-001 in this resubmission."
      echo "- showcompat checksum sidecar normalization for EPIC022 applies (PF10 — HDE-Build Notes, §2.5)."
      echo
      echo "## No other deltas captured at this step."
    } > "${OUT}"
  
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
exit_code: 0
--- stdout ---

--- stderr ---

```

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
[
  {
    "check_id": "0A",
    "ended_at_utc": "2025-12-26T18:16:15Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0A_bootstrap_and_codespaces_snapshot.log",
    "pf_refs": "PF19 — Glow QA Guide, §14.4.3; PF27 — Plan Templates, §4.2",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:16:15Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "0710287ebdc583a08974ea6b7205269a34d81b0c4edfb69fdf3d471cda1d4b98",
    "tokens": []
  },
  {
    "check_id": "0B",
    "ended_at_utc": "2025-12-26T18:41:55Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0B_doc_delta_capture.log",
    "pf_refs": "PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.7",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:41:55Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": [
      "DOC_DELTA_PRESENT_OK"
    ]
  }
]
```

---

## File: audit/qa/hde-epic022/step0b_deviations.md

*File not found*
