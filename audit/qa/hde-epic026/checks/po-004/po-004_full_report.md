# HDE-EPIC026 — Detailed QA Report (po-004)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-004`
- Check name: `PO-004 — Cached vendor-shaped payload regression fixed`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-24

---

## Executive summary

CHECK `po-004` completed with final status **PASS** (`pytest_rc=0`) and produced all required deliverables under `audit/qa/hde-epic026/checks/po-004/`.

Important execution note: the exact plan command block references helper functions that are not present in the active helper shim (`qa_log_context`, `qa_capture_route_bytes`, `qa_emit_outcome`). The run was completed using an adapted block that preserves the plan’s required deliverables, deterministic pins, closed rails posture, and manifest append behavior.

---

## Detailed chronology (all steps run)

### 1) Variable import + setup checks

- Set `EVIDENCE_ROOT=audit/qa/hde-epic026` and validated non-empty.
- Confirmed helper prerequisite exists:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`
- Confirmed repo test locus exists:
  - `tests/http/test_compat_endpoint_contract.py`

Preflight marker observed: `po004_preflight_ok`.

### 2) Attempted plan command block

- The plan-provided procedure was invoked, but helper/API mismatch prevented completion because referenced helper functions are absent in current helper shim.

### 3) Adapted execution (plan-aligned)

- Executed deterministic closed-rails pytest run with required output files:

```bash
python -m pytest -q tests/http/test_compat_endpoint_contract.py 1>"$stdout_log" 2>"$stderr_log"
```

- Rails and determinism posture captured in run environment:
  - `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
  - `LC_ALL=C`, `LANG=C`, `TZ=UTC`
  - `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, `SOURCE_DATE_EPOCH=1700000000`, `PYTHONWARNINGS=ignore`

- Emitted `primary.log` via `qa_emit_step_log_header`, appended rc/pass-fail lines, and appended manifest row via `qa_append_manifest`.

---

## PASS/FAIL evaluation

Plan language:

- PASS if pytest exit code is `0`.
- FAIL if pytest exit code is non-zero.

Observed:

- `pytest_rc.txt` contains `0`.

Decision: **PASS**.

---

## Deliverables and full evidence contents

All authoritative deliverables exist:

- `audit/qa/hde-epic026/checks/po-004/primary.log`
- `audit/qa/hde-epic026/checks/po-004/pytest_stdout.log`
- `audit/qa/hde-epic026/checks/po-004/pytest_stderr.log`
- `audit/qa/hde-epic026/checks/po-004/pytest_rc.txt`

### 1) primary.log

Path: `audit/qa/hde-epic026/checks/po-004/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-24T22:06:54Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-004", "check_name": "PO-004 — Cached vendor-shaped payload regression fixed", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": ["python -m pytest -q tests/http/test_compat_endpoint_contract.py"], "artifacts": [{"path": "pytest_stdout.log", "type": "log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "type": "log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "type": "text", "desc": "pytest exit code"}], "pf_refs": ["PF10 stable checks dirs", "PF05 deterministic closed rails", "PF02 rails posture"]}

###
pytest_rc=0
pass_fail=PASS
```

### 2) pytest_stdout.log

Path: `audit/qa/hde-epic026/checks/po-004/pytest_stdout.log`

```log
............                                                             [100%]
12 passed in 0.22s
```

### 3) pytest_stderr.log

Path: `audit/qa/hde-epic026/checks/po-004/pytest_stderr.log`

```text
(empty file)
```

### 4) pytest_rc.txt

Path: `audit/qa/hde-epic026/checks/po-004/pytest_rc.txt`

```text
0
```

---

## Manifest linkage

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

`po-004` manifest row:

- `timestamp_utc`: `2026-02-24T22:06:54Z`
- `check_id`: `po-004`
- `status`: `PASS`
- `log_path`: `checks/po-004/primary.log`
- `sha256`: `cf545563f658a1c33e4adae763264212158e4b9d8667e9669c7241ef64a80542`

---

## Integrity snapshot (sha256)

- `primary.log`: `cf545563f658a1c33e4adae763264212158e4b9d8667e9669c7241ef64a80542`
- `pytest_stdout.log`: `c3acbaab2306c0dae714d40da745b876663bee5998bb7d04a92961f01cca2cec`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-004` is complete with required deliverables present and PASS by plan rule (`pytest_rc=0`). Evidence is stored under the stable check directory and includes canonical `captured_env` rails/env pins in `primary.log`.