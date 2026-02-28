# HDE-EPIC026 — Detailed QA Report (po-003, v2)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-003`
- Check name: `PO-003 — Local-first acquisition semantics preserved`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Report version: `v2` (captures PF19/PF27 `captured_env` remediation)
- Date (UTC): 2026-02-24

---

## Executive summary

`po-003` required two rounds of remediation:

1. **Selector remediation**: initial plan selector matched zero tests (`rc=5`), then corrected selector produced PASS (`rc=0`).
2. **Header trust remediation**: PF-required `captured_env` was missing from `primary.log`; helper was updated and check rerun to emit canonical rails/env capture.

Final authoritative state: **PASS with `captured_env` present**.

---

## All steps taken (complete chronology)

### Step 1 — Initial po-003 run (plan selector)

- Preconditions validated:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh` exists
  - `tests/http/test_compat_endpoint_contract.py` exists
  - `python -m pytest --version` works
- Executed plan selector:

```bash
python -m pytest tests/http/test_compat_endpoint_contract.py \
  -k "test_local_first_semantics or test_rails_gate_semantics"
```

- Outcome: FAIL (`pytest_rc=5`, 0 tests selected).

### Step 2 — Selector mismatch analysis

- Inspected test locus and confirmed selector names were absent.
- Chosen valid selector covering local-first + rails semantics:
  - `close_back_uses_local_without_provider`
  - `open_rails_acquires_and_persists`
  - `closed_rails_missing_refuses_without_provider`

### Step 3 — Remediation run (selector fix)

- Re-ran po-003 under closed rails and determinism pins with corrected selector:

```bash
python -m pytest tests/http/test_compat_endpoint_contract.py \
  -k "close_back_uses_local_without_provider or open_rails_acquires_and_persists or closed_rails_missing_refuses_without_provider"
```

- Outcome: PASS (`pytest_rc=0`, 3 selected tests passed).

### Step 4 — Review finding: trust blocker (`captured_env` missing)

- External review flagged PF19/PF27 trust requirement not met because `primary.log` header lacked `captured_env`.

### Step 5 — Header-emitter remediation

- Updated helper used by plan execution to include canonical captured environment fields:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`
  - `audit/qa/hde-epic026/00_meta/qa_helpers.sh`
- Added `captured_env` object with keys:
  - `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`

### Step 6 — Re-execution after captured_env fix

- Re-ran po-003 again in the same stable directory (`checks/po-003`) with:
  - `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
  - `LC_ALL=C`, `LANG=C`, `TZ=UTC`
- Outcome: PASS (`pytest_rc=0`) and `primary.log` now includes `captured_env`.

---

## PASS/FAIL criteria (plan language) and final decision

Plan rule:

- PASS if pytest exit code is `0`.
- FAIL if pytest exit code is non-zero.

Latest run result:

- `pytest_rc.txt` = `0`
- `primary.log` = `pass_fail=PASS`
- `captured_env` = present and populated with rails/env pins

Final decision: **PASS (accepted as QA proof after remediation)**.

---

## Required deliverables and full evidence contents (latest run)

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-003/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-24T20:58:49Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-003", "check_name": "PO-003 — Local-first acquisition semantics preserved", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": ["python -m pytest tests/http/test_compat_endpoint_contract.py -k close_back_uses_local_without_provider or open_rails_acquires_and_persists or closed_rails_missing_refuses_without_provider", "bash wrapper emits logs and rc"], "artifacts": [{"path": "pytest_stdout.log", "type": "log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "type": "log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "type": "text", "desc": "pytest exit code"}], "pf_refs": ["PF05 §6.2", "PF02 §3.4", "PF10 §2.16", "PF19 captured_env requirement", "PF27 captured_env schema"]}

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

======================= 3 passed, 9 deselected in 0.58s ========================
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

## Manifest history for po-003 (audit trail)

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

- `2026-02-24T19:55:53Z` — `po-003` — `FAIL` — `sha256=38b6867a7e1703a8b1343b101166385142eff68e9212fdb634b5cbc3cdef9f7b`
- `2026-02-24T19:59:41Z` — `po-003` — `PASS` — `sha256=c981ceb7f84d41c928b35aaae4a48a14dad7886dc62fd684322d937050f06e12`
- `2026-02-24T20:58:49Z` — `po-003` — `PASS` — `sha256=9fc6188660f8f6bd92e861953d234899d23aac287748f7c076f2dafafb700888` (captured_env-compliant rerun)

Interpretation: the latest manifest entry is PASS and aligns with the current `primary.log` hash.

---

## Integrity snapshot (latest deliverables)

- `primary.log`: `9fc6188660f8f6bd92e861953d234899d23aac287748f7c076f2dafafb700888`
- `pytest_stdout.log`: `b7ed776bf17b2a63341bab117752fc0e6ef401da8934585d92aa7ad8d107f90a`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-003` is now fully remediated for both behavioral proof and evidence-trust requirements: selected tests pass (`rc=0`) and `primary.log` includes PF-required `captured_env` rails/env capture. This v2 report supersedes the previous report for acceptance review.