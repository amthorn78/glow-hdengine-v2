# HDE-EPIC026 — Detailed QA Report (po-006) [v2]

## Report scope

- Epic: HDE-EPIC026
- Check: `po-006`
- Check name: `CHECK po-006: Dev-only writer endpoint exists and gated`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-25
- Version note: `v2` adds canonical PF19 root-manifest provenance proof for `po-006`.

---

## Executive summary

CHECK `po-006` is **PASS** on final run.

Plan PASS conditions are satisfied:

- `route_proof.txt` shows `FOUND /dev/writer/conjunction`, and
- `pytest_rc.txt` is `0` for `tests/http/test_dev_conjunction_http.py`.

In addition, canonical provenance is now explicitly proven at the epic root manifest path (`audit/qa/hde-epic026/qa_step_logs_manifest.json`) with an updated root path proof.

---

## Detailed chronology (all steps taken)

### 1) Variable import and preflight

- Set and pinned the step inputs:
  - `EVIDENCE_ROOT=audit/qa/hde-epic026`
  - `SAFE_MODE=1`, `ALLOW_NETWORK=0`
  - `PYTHONHASHSEED=0`, `TZ=UTC`, `LC_ALL=C`
- Confirmed plan-named paths exist:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`
  - `adapter/http_reader.py`
  - `tests/http/test_dev_conjunction_http.py`

### 2) Initial attempt using plan block

- Attempted to run the provided command block exactly.
- Execution blocked by helper API drift: plan refers to helper functions `open_primary_log` and `record_step_end`, but these are not present in the active helper shim.

### 3) Helper-compatible adapted execution

- Ran a helper-compatible equivalent flow that preserves:
  - same deliverable files under `checks/po-006/`,
  - same proof obligations (`route_proof` + pytest rc),
  - same PASS/FAIL logic,
  - same closed rails and determinism posture.

### 4) Final determinism-pin alignment rerun

- Performed one additional rerun to ensure `LANG=C` appears in captured environment header, keeping artifacts strictly aligned with stated pins.

Final authoritative run is the latest `po-006` manifest row and current file set.

### 5) Canonical PF19 root-manifest remediation

- Verified the canonical epic-root manifest path exists:
  - `audit/qa/hde-epic026/qa_step_logs_manifest.json`
- Regenerated canonical close-pack artifacts using governed tooling:
  - `python tools/qa/generate_epic026_close_pack.py`
- Re-verified that the canonical root manifest now includes `po-006` with:
  - `log_path=checks/po-006/primary.log`
  - `sha256=50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5`
- Re-verified canonical root path proof for the manifest exists and is current:
  - `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt`

---

## PASS/FAIL criteria evaluation

Plan criteria:

- PASS if route proof shows FOUND for `/dev/writer/conjunction`, and pytest rc is `0`.

Observed in final run:

- route proof: `FOUND /dev/writer/conjunction`
- pytest rc: `0`

Decision: **PASS**.

---

## Required deliverables and full evidence contents

All expected outputs are present under `audit/qa/hde-epic026/checks/po-006/`:

- `primary.log`
- `route_proof.txt`
- `pytest_stdout.log`
- `pytest_stderr.log`
- `pytest_rc.txt`

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-006/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-25T05:20:02Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-006", "check_name": "CHECK po-006: Dev-only writer endpoint exists and gated", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": [{"cmd": "python - (route proof via adapter/http_reader.py)", "artifact": "route_proof.txt"}, {"cmd": "python -m pytest -q tests/http/test_dev_conjunction_http.py", "stdout": "pytest_stdout.log", "stderr": "pytest_stderr.log", "rc": "pytest_rc.txt"}], "artifacts": [{"path": "route_proof.txt", "desc": "route proof for /dev/writer/conjunction"}, {"path": "pytest_stdout.log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "desc": "pytest return code"}], "pf_refs": ["PF10 stable checks dir", "PF05 determinism pins", "PF02 closed rails"]}

###
route_proof=audit/qa/hde-epic026/checks/po-006/route_proof.txt
pytest_rc=0
pytest_stdout=audit/qa/hde-epic026/checks/po-006/pytest_stdout.log
pytest_stderr=audit/qa/hde-epic026/checks/po-006/pytest_stderr.log
```

### 2) `route_proof.txt`

Path: `audit/qa/hde-epic026/checks/po-006/route_proof.txt`

```text
FOUND /dev/writer/conjunction
```

### 3) `pytest_stdout.log`

Path: `audit/qa/hde-epic026/checks/po-006/pytest_stdout.log`

```log
....                                                                     [100%]
4 passed in 0.19s
```

### 4) `pytest_stderr.log`

Path: `audit/qa/hde-epic026/checks/po-006/pytest_stderr.log`

```text
(empty file)
```

### 5) `pytest_rc.txt`

Path: `audit/qa/hde-epic026/checks/po-006/pytest_rc.txt`

```text
0
```

---

## Manifest trail for po-006

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

- `2026-02-25T05:19:25Z` — `po-006` — `PASS` — `sha256=3f9c0ed4834b01d37cd097d3052f938ce6fefbb6fd17da1e72f1d4f20b1d47cc`
- `2026-02-25T05:20:03Z` — `po-006` — `PASS` — `sha256=50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5`

Latest entry corresponds to current `primary.log` and is the authoritative result.

---

## Canonical PF19 root-manifest provenance (remediation closure)

Canonical root manifest:

- Path: `audit/qa/hde-epic026/qa_step_logs_manifest.json`
- Contains `check_id=po-006`
- Contains `log_path=checks/po-006/primary.log`
- Contains `sha256=50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5`
- `generated_utc=2026-02-25T08:54:12Z`

Canonical root manifest path proof:

- Path: `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt`
- `path: audit/qa/hde-epic026/qa_step_logs_manifest.json`
- `sha256: f7910454a4139f2d5c3566cc101b93e1e07916b720a5ea0615c2076a90a147fc`
- `produced_at_utc: 2026-02-25T08:54:12Z`

Artifact integrity cross-check:

- Current `sha256(primary.log)` for `checks/po-006/primary.log` equals
  `50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5`,
  matching the canonical root manifest row for `po-006`.

Result: PF19 canonical-root provenance requirement for `po-006` is satisfied.

---

## Integrity snapshot (sha256)

- `primary.log`: `50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5`
- `route_proof.txt`: `6cb68e4d8fc340e25106c6d0fcf37cb0eb3d54f48fe43149d79c2c4c648f1b9c`
- `pytest_stdout.log`: `44091516c6f7d278c9900d796163d45f95d1ad1819370ffeeaf887bc704f2e38`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-006` is complete and PASS. Required artifacts exist at the expected check path, route proof is FOUND for the writer endpoint, pytest rc is 0, and the final primary log captures closed rails and determinism pins in the PF27 header.

Canonical PF19 provenance is now explicitly closed at the required epic-root manifest path, with matching path proof and hash linkage to `checks/po-006/primary.log`.
