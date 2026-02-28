# HDE-EPIC026 — Detailed QA Report (po-005)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-005`
- Check name: `CHECK po-005: Dev-only sampler and reader endpoints exist and gated`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-25

---

## Executive summary

CHECK `po-005` is **PASS** on final run. Both static route proof targets are `FOUND` and pytest for `tests/http/test_dev_conjunction_http.py` returned `0`.

The step required remediation attempts before final PASS because the initial static proof pattern was too strict for the actual decorator alias in the repo. The final static proof matcher correctly verifies the presence of dev endpoints without changing PASS/FAIL criteria.

---

## Detailed chronology (all steps run)

### 1) Preflight

- Set `EVIDENCE_ROOT=audit/qa/hde-epic026`.
- Confirmed required loci exist:
  - `adapter/http_reader.py`
  - `tests/http/test_dev_conjunction_http.py`
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`

### 2) Helper/API compatibility check

- The plan command block references helper functions not present in the current helper shim (`qa_emit_kv`, `qa_emit_step_log_footer`, and others).
- Executed a helper-compatible adapted flow that preserved:
  - identical deliverable files/paths,
  - same route-proof + pytest proof obligations,
  - same PASS/FAIL criteria,
  - closed rails + determinism pinning,
  - manifest append behavior.

### 3) Run history and remediation

- **Attempt 1:** FAIL (`route_proof` false negative, pytest rc `0`).
- **Attempt 2:** FAIL (regex still over-escaped; route proof false negative, pytest rc `0`).
- **Attempt 3 (final):** PASS (`route_proof` FOUND for both endpoints, pytest rc `0`).

Final authoritative status is latest manifest entry for `po-005`: PASS.

---

## PASS/FAIL criteria evaluation

Plan criteria:

- PASS if route proof shows FOUND for both dev endpoints and pytest rc is 0.
- FAIL if either route proof has NOT_FOUND or pytest fails.

Final run evidence:

- `/dev/sampler/conjunction` → FOUND
- `/dev/reader/conjunction` → FOUND
- `pytest_rc.txt` → `0`

Decision: **PASS**.

---

## Required deliverables and full evidence contents

All expected outputs are present under `audit/qa/hde-epic026/checks/po-005/`:

- `primary.log`
- `pytest_stdout.log`
- `pytest_stderr.log`
- `pytest_rc.txt`
- `route_proof.txt`

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-005/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-25T02:35:22Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-005", "check_name": "CHECK po-005: Dev-only sampler and reader endpoints exist and gated", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": [{"cmd": "python - (route proof via adapter/http_reader.py)", "artifact": "route_proof.txt"}, {"cmd": "python -m pytest -q tests/http/test_dev_conjunction_http.py", "stdout": "pytest_stdout.log", "stderr": "pytest_stderr.log", "rc": "pytest_rc.txt"}], "artifacts": [{"path": "route_proof.txt", "desc": "route decorator proof for dev endpoints"}, {"path": "pytest_stdout.log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "desc": "pytest return code"}], "pf_refs": [{"pf": "PF19", "why": "QA evidence trust posture; tooling failures vs behavior failures"}, {"pf": "PF27", "why": "Plan templates + step log schema"}]}

###
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
determinism=LC_ALL=C LANG=C TZ=UTC
route_proof=audit/qa/hde-epic026/checks/po-005/route_proof.txt
pytest_rc=0
pytest_stdout=audit/qa/hde-epic026/checks/po-005/pytest_stdout.log
pytest_stderr=audit/qa/hde-epic026/checks/po-005/pytest_stderr.log
```

### 2) `route_proof.txt`

Path: `audit/qa/hde-epic026/checks/po-005/route_proof.txt`

```text
/dev/sampler/conjunction FOUND
/dev/reader/conjunction FOUND
```

### 3) `pytest_stdout.log`

Path: `audit/qa/hde-epic026/checks/po-005/pytest_stdout.log`

```log
....                                                                     [100%]
4 passed in 0.23s
```

### 4) `pytest_stderr.log`

Path: `audit/qa/hde-epic026/checks/po-005/pytest_stderr.log`

```text
(empty file)
```

### 5) `pytest_rc.txt`

Path: `audit/qa/hde-epic026/checks/po-005/pytest_rc.txt`

```text
0
```

---

## Manifest trail for po-005

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

- `2026-02-25T02:22:15Z` — `po-005` — `FAIL` — `sha256=e4ff67f6978740f1776d72415e0da1414ea422f9ddbed37f930255e677e97467`
- `2026-02-25T02:26:29Z` — `po-005` — `FAIL` — `sha256=517e4a03409ee94fef722a332f0aa115db059c55f287ca36e50ca9ff176a5dbc`
- `2026-02-25T02:35:23Z` — `po-005` — `PASS` — `sha256=b1a9d07d48fd33674034a39aee9c3f81aed2f04015a917fb89065de603e6dd29`

Latest entry is PASS and corresponds to the current `primary.log`.

---

## Integrity snapshot (sha256)

- `primary.log`: `b1a9d07d48fd33674034a39aee9c3f81aed2f04015a917fb89065de603e6dd29`
- `route_proof.txt`: `224fb18694acd576fa1b5411373b6909884b9379af8e6ce1de7fce9fa1a89693`
- `pytest_stdout.log`: `2132f781fd09c4d032290bbe2ac096ba7335a9eb5ac19ffde8bd10a3ae2045f5`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-005` is complete and PASS on final run. The dev-only sampler and reader endpoints are statically proven present, dev-only endpoint pytest coverage passes, and all required deliverables are present under the stable checks path.