# HDE-EPIC026 — Detailed QA Report (po-009)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-009`
- Check name: `PO-009 — CLI rails: closed refusal, open success`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Date (UTC): 2026-02-26
- Evidence root: `audit/qa/hde-epic026`

---

## Executive summary

`po-009` was executed and ended in **BLOCKED_MISSING_INPUTS** posture.

Per current product/run constraints provided by PO, `USER_A_ID` and `USER_B_ID` are not available as valid inputs at this time and should not be expected for this run. The check is deferred until valid IDs are available.

---

## Actions taken

1. Loaded deterministic environment and rails defaults for QA execution:
   - `LANG=C`, `LC_ALL=C`, `TZ=UTC`
   - Closed rails defaults applied in captured env (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`).
2. Verified prerequisite helper exists and sourced:
   - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`
3. Started `po-009` step execution under stable checks-only path:
   - `audit/qa/hde-epic026/checks/po-009/`
4. Evaluated required input precondition from approved plan:
   - Missing/invalid `USER_A_ID` / `USER_B_ID` triggered blocked path.
5. Wrote blocked evidence artifacts and appended manifest entry.
6. Recorded explicit input-availability constraint log for this step:
   - `po-009_input_constraint.log`

---

## Outcome classification

- `pass_fail`: `FAIL`
- `fail_status`: `BLOCKED_MISSING_INPUTS`
- Run type: precondition block (not a behavioral defect run)

Rationale: The approved plan requires real `USER_A_ID`/`USER_B_ID` to exercise closed/open/close-back rails behavior. Those IDs are not available as valid product inputs at this time.

---

## Evidence artifacts

### 1) Primary step log

Path: `audit/qa/hde-epic026/checks/po-009/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-26T05:46:40Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-009", "check_name": "PO-009 — CLI rails: closed refusal, open success", "pass_fail": "FAIL", "fail_status": "BLOCKED_MISSING_INPUTS", "intended_tokens": [], "claimed_tokens": [], "commands": [], "artifacts": [{"path": "open_rails_note.txt", "type": "text", "desc": "missing USER_A_ID/USER_B_ID"}], "pf_refs": ["PF27 §Step-log header schema expectations (minimum; required)"]}

###
```

### 2) Block note

Path: `audit/qa/hde-epic026/checks/po-009/open_rails_note.txt`

```text
BLOCKED: USER_A_ID/USER_B_ID are not valid at this time.
Run deferred until valid IDs are available.
```

### 3) Input constraint log (new)

Path: `audit/qa/hde-epic026/checks/po-009/po-009_input_constraint.log`

```text
timestamp_utc=2026-02-26T05:46:41Z
check_id=po-009
status=BLOCKED_MISSING_INPUTS
statement=USER_A_ID/USER_B_ID are not available as valid product inputs at this time and should not be expected for this run.
action=po-009 execution deferred until valid IDs are available.
evidence_primary_log=audit/qa/hde-epic026/checks/po-009/primary.log
evidence_note=audit/qa/hde-epic026/checks/po-009/open_rails_note.txt
```

---

## Manifest linkage

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

Recorded row:

- `timestamp_utc`: `2026-02-26T05:46:41Z`
- `check_id`: `po-009`
- `status`: `FAIL`
- `log_path`: `checks/po-009/primary.log`
- `sha256`: `4ee70c9c5063af0a97c846edaeb04c7dc2f350770b4296a440b56d14b3e26c8b`

---

## Next-step condition

Re-run `po-009` when valid product `USER_A_ID` and `USER_B_ID` become available.
At that time, expected additional deliverables are the full rails-run artifact set (`closed_*`, `open_*`, and close-back artifacts) per the approved plan.
