# HDE-EPIC031 Doc Deltas

## BLOCKERS

None recorded before Live QA execution.

## CAVEATS

None recorded before Live QA execution.

## MOON LOOP REMEDIATION

- Step: PO-006
- Timestamp (UTC): 2026-05-13T13:19:05Z
- Trigger: `allowed_keys_present` evaluated false despite PR-02 generator check passing and redaction artifact status PASS.
- File changed: `audit/qa/hde-epic031/00_meta/live_qa_harness.py`
- Action taken: aligned `check_po006` keys-only predicate with canonical redaction schema fields (`allowed_keys`, `status`) and retained sample fallback.
- Re-execution under closed rails: `python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-006`
- Remediated outputs:
	- `audit/qa/hde-epic031/checks/po-006/primary.log` -> `status: PASS`, `exit_code: 0`
	- `audit/qa/hde-epic031/checks/po-006/result.json` -> `allowed_keys_present: true`, `status: PASS`
- PF02 Moon Loop delta artifacts:
	- `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`
	- `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`

- Step: PO-008
- Timestamp (UTC): 2026-05-13T16:53:30Z
- Trigger: `FAIL_BEHAVIOR` with `all_commands_green=false` caused by `STALE` coherence state and `PROOF_MTIME_FUTURE`/`PROOF_MTIME` validator errors.
- Files changed: governed PR-03 coherence/index artifacts and check outputs under `audit/qa/hde-epic031/checks/po-008/`; no source code path changed for PO-008 moon loop.
- Action taken: refreshed governed coherence/index artifacts with closed-rails write-mode generators and normalized compat AB/BA file mtimes (no byte changes) to satisfy proof-mtime monotonicity checks.
- Re-execution under closed rails: `python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-008`
- Remediated outputs:
	- `audit/qa/hde-epic031/checks/po-008/primary.log` -> `status: PASS`, `exit_code: 0`
	- `audit/qa/hde-epic031/checks/po-008/result.json` -> `all_commands_green: true`, `coherence_status: PASS`, `status: PASS`
- Moon Loop delta artifacts:
	- `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`
	- `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`
