# HDE-EPIC026 — CHECK po-009 All-in-One Log Bundle

## Scope

- Epic: HDE-EPIC026
- Check: po-009
- Plan: r11 Live QA Plan HDE-EPIC026.md
- Date: 2026-02-26
- Evidence root: audit/qa/hde-epic026

---

## Final status

- Outcome: BLOCKED_MISSING_INPUTS
- pass_fail: FAIL
- fail_status: BLOCKED_MISSING_INPUTS

### Input availability statement (authoritative for this run)

USER_A_ID and USER_B_ID are not available as valid product inputs at this time and should not be expected for this run.

---

## Actions taken

1. Loaded deterministic environment posture (`LANG=C`, `LC_ALL=C`, `TZ=UTC`).
2. Loaded QA helper from `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`.
3. Started po-009 in stable checks-only path `audit/qa/hde-epic026/checks/po-009/`.
4. Hit required-input precondition gate for USER_A_ID/USER_B_ID.
5. Wrote blocked evidence (`primary.log`, `open_rails_note.txt`).
6. Appended manifest entry under `checks/po-000/qa_step_logs_manifest.json`.
7. Wrote dedicated input-constraint log for traceability.

---

## Evidence index (this bundle)

- audit/qa/hde-epic026/checks/po-009/primary.log
- audit/qa/hde-epic026/checks/po-009/open_rails_note.txt
- audit/qa/hde-epic026/checks/po-009/po-009_input_constraint.log
- audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json (po-009 row)

---

## Manifest linkage

Recorded row for po-009:

- timestamp_utc: 2026-02-26T05:46:41Z
- check_id: po-009
- status: FAIL
- log_path: checks/po-009/primary.log
- sha256: 4ee70c9c5063af0a97c846edaeb04c7dc2f350770b4296a440b56d14b3e26c8b

---

## Raw evidence appendix

### A) primary.log

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-26T05:46:40Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-009", "check_name": "PO-009 — CLI rails: closed refusal, open success", "pass_fail": "FAIL", "fail_status": "BLOCKED_MISSING_INPUTS", "intended_tokens": [], "claimed_tokens": [], "commands": [], "artifacts": [{"path": "open_rails_note.txt", "type": "text", "desc": "missing USER_A_ID/USER_B_ID"}], "pf_refs": ["PF27 §Step-log header schema expectations (minimum; required)"]}

###
```

### B) open_rails_note.txt

```text
BLOCKED: USER_A_ID/USER_B_ID are not valid at this time.
Run deferred until valid IDs are available.
```

### C) po-009_input_constraint.log

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

## Re-run condition

Re-run po-009 only when valid product USER_A_ID and USER_B_ID become available.
Until then, this blocked result is expected and should be treated as an input-availability gate, not a behavior defect.
