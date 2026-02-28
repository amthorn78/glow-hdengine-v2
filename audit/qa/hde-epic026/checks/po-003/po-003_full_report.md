# HDE-EPIC026 — Detailed QA Report (po-003)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-003`
- Check name: `PO-003 — Local-first acquisition semantics preserved`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-24

---

## Executive summary

This check was executed twice:

1. **Initial run** produced a FAIL outcome (`pytest_rc=5`) because the original `-k` selector matched no tests.
2. **Remediation run** updated the selector to existing local-first/rails test names and produced a PASS outcome (`pytest_rc=0`).

Final status for `po-003`: **PASS (after remediation)**.

---

## Preconditions and controls applied

- Stable check-scoped evidence directory used: `audit/qa/hde-epic026/checks/po-003/` (no run-id folders)
- Determinism pins used during execution: `LC_ALL=C`, `LANG=C`, `TZ=UTC`
- Rails posture used during execution: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
- Required helper dependency used: `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`

---

## Detailed chronology (all steps taken)

### 1) Preflight and first execution (plan-provided selector)

- Confirmed required files existed:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`
  - `tests/http/test_compat_endpoint_contract.py`
- Confirmed pytest availability with `python -m pytest --version`.
- Ran the plan-provided selector:

```bash
python -m pytest tests/http/test_compat_endpoint_contract.py \
  -k "test_local_first_semantics or test_rails_gate_semantics"
```

- Result observed at runtime:
  - `pytest_rc=5`
  - `collected 12 items / 12 deselected / 0 selected`
- Manifest recorded this as a FAIL entry for `po-003`.

### 2) Root-cause analysis and remediation design

- Inspected `tests/http/test_compat_endpoint_contract.py` and verified the selector names from the plan were not present.
- Identified existing tests that validate local-first and rails semantics:
  - `test_conjunction_resolved_closed_rails_missing_refuses_without_provider`
  - `test_conjunction_resolved_open_rails_acquires_and_persists`
  - `test_conjunction_resolved_close_back_uses_local_without_provider`
- Remediation selector chosen to match those tests.

### 3) Remediation execution (corrected selector)

- Re-ran `po-003` in the same check directory with corrected selector and complete header exports (`CHECK_ID`, `CHECK_NAME`):

```bash
python -m pytest tests/http/test_compat_endpoint_contract.py \
  -k "close_back_uses_local_without_provider or open_rails_acquires_and_persists or closed_rails_missing_refuses_without_provider"
```

- Result:
  - `pytest_rc=0`
  - `3 passed, 9 deselected`
- Manifest appended a second `po-003` entry with PASS status.

---

## Plan PASS/FAIL criteria evaluation

Plan rule for this step:

- PASS if pytest exit code is `0`.
- FAIL if pytest exit code is non-zero.

Evaluation:

- Initial run: `pytest_rc=5` → FAIL
- Remediation run: `pytest_rc=0` → PASS

Final disposition: **PASS (remediated run)**

---

## Required deliverables and full evidence contents

All required deliverables exist under `audit/qa/hde-epic026/checks/po-003/`.

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-003/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-24T19:59:41Z", "check_id": "po-003", "check_name": "PO-003 — Local-first acquisition semantics preserved", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": ["python -m pytest tests/http/test_compat_endpoint_contract.py -k close_back_uses_local_without_provider or open_rails_acquires_and_persists or closed_rails_missing_refuses_without_provider", "bash wrapper emits logs and rc"], "artifacts": [{"path": "pytest_stdout.log", "type": "log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "type": "log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "type": "text", "desc": "pytest exit code"}], "pf_refs": ["PF05 §6.2", "PF02 §3.4", "PF10 §2.16"]}

###
pytest_rc=0
pass_fail=PASS
```

### 2) `pytest_stdout.log`

Path: `audit/qa/hde-epic026/checks/po-003/pytest_stdout.log`

```log
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
rootdir: /workspaces/glow-hdengine-v2
configfile: pytest.ini
collected 12 items / 9 deselected / 3 selected

tests/http/test_compat_endpoint_contract.py ...                          [100%]

======================= 3 passed, 9 deselected in 0.18s ========================
```

### 3) `pytest_stderr.log`

Path: `audit/qa/hde-epic026/checks/po-003/pytest_stderr.log`

```text
(empty file)
```

### 4) `pytest_rc.txt`

Path: `audit/qa/hde-epic026/checks/po-003/pytest_rc.txt`

```text
0
```

---

## Manifest history for po-003 (shows all runs)

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

Relevant entries:

- `2026-02-24T19:55:53Z` — `po-003` — `FAIL` — sha256 `38b6867a7e1703a8b1343b101166385142eff68e9212fdb634b5cbc3cdef9f7b`
- `2026-02-24T19:59:41Z` — `po-003` — `PASS` — sha256 `c981ceb7f84d41c928b35aaae4a48a14dad7886dc62fd684322d937050f06e12`

Interpretation: The step was rerun and remediated; latest entry is PASS.

---

## Artifact integrity snapshot (sha256)

- `primary.log`: `c981ceb7f84d41c928b35aaae4a48a14dad7886dc62fd684322d937050f06e12`
- `pytest_stdout.log`: `192fab28b40ccb8435ca859965bb7b9a5137c0928fbce963018f3265911c234f`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-003` initially failed due to a selector/test-name mismatch, then passed after remediation with a selector that maps to existing local-first and rails-gating tests. All required deliverables are present, and final plan-based status is PASS.