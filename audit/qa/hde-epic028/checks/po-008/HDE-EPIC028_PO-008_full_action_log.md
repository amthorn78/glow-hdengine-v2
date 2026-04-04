# HDE-EPIC028 PO-008 Full Action Log

## Manifest Header
- HDE-EPIC: HDE-EPIC028 / Conjunction Pass 4
- Step: PO-008 - Same-change coherence across changed governed evidence families
- Approved QA Plan File: r9 Live QA Plan HDE-EPIC028.md
- Approval Doc File: none
- Previous Step Report File: report - po-007 QA HDE-EPIC028.md
- PF-Canon consulted: PF10 (current) + PF05 + PF02 (+ PF12 + PF19 for one execution gap)
- Generated at (UTC): 2026-04-03T17:12:36Z

## Outcome
- Final status: PASS
- Fail status: (empty)
- Coherence set validated together: audit/gates/json_gate/canonical + audit/gates/canonical_json

## Rails and Repo State
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC
- git HEAD: e5703d58447f38394f25cbcd113eebf6883366b5
- git status (po-008 scope):

?? audit/qa/hde-epic028/checks/po-008/

## Executed Actions
1. Created stable check-scoped root under audit/qa/hde-epic028/checks/po-008.
2. Recorded D0 presence flag and captured complete before file lists for both governed families.
3. Ran canonical gate writer exactly once and captured stdout, stderr, and return code.
4. Captured complete after file lists for both governed families.
5. Evaluated same-change coherence as a single set and wrote primary.log with final lane.

## Commands Used
- set -euo pipefail
- export LC_ALL=C
- export LANG=C
- export TZ=UTC
- export SAFE_MODE=1
- export ALLOW_NETWORK=0
- export APP_ENV=dev
- mkdir -p audit/qa/hde-epic028/checks/po-008
- capture json_gate_family_before.txt from audit/gates/json_gate/canonical
- capture canonical_json_family_before.txt from audit/gates/canonical_json
- run tools/evidence/run_canonical_json_gate.py once, capture stdout/stderr/rc
- capture json_gate_family_after.txt from audit/gates/json_gate/canonical
- capture canonical_json_family_after.txt from audit/gates/canonical_json
- write primary.log with PASS/FAIL_TOOLING decision based on coherence set checks

## Evidence Outputs (Metadata)
- audit/qa/hde-epic028/checks/po-008/primary.log
  - sha256: 6575e7bc7f15f1a5af283685e75c762c0755689fd0f7e3fac1a202443135f990
  - size_bytes: 2688
  - mtime_epoch: 1775236130
- audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt
  - sha256: ea70e2d78be4838ee68b9d8968f5d87fa8afc945b397d4853254d9ba77da20e8
  - size_bytes: 415
  - mtime_epoch: 1775236129
- audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt
  - sha256: 0a32c64f6a15769ca4639f5aa5f2f119561fdd5cada16566dc91401f5393ac82
  - size_bytes: 456
  - mtime_epoch: 1775236129
- audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log
  - sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  - size_bytes: 0
  - mtime_epoch: 1775236129
- audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log
  - sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  - size_bytes: 0
  - mtime_epoch: 1775236129
- audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt
  - sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
  - size_bytes: 2
  - mtime_epoch: 1775236130
- audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt
  - sha256: ea70e2d78be4838ee68b9d8968f5d87fa8afc945b397d4853254d9ba77da20e8
  - size_bytes: 415
  - mtime_epoch: 1775236130
- audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt
  - sha256: 0a32c64f6a15769ca4639f5aa5f2f119561fdd5cada16566dc91401f5393ac82
  - size_bytes: 456
  - mtime_epoch: 1775236130

## Evidence Outputs (Full Verbatim Content)
### audit/qa/hde-epic028/checks/po-008/primary.log

{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-008","check_name":"Same-change coherence across changed governed evidence families","claimed_tokens":[],"command":"python -c \"from pathlib import Path; files=sorted(p.as_posix() for p in Path('audit/gates/json_gate/canonical').rglob('*') if p.is_file()); Path('audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt').write_text('\\\\n'.join(files)+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; files=sorted(p.as_posix() for p in Path('audit/gates/canonical_json').rglob('*') if p.is_file()); Path('audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt').write_text('\\\\n'.join(files)+'\\\\n', encoding='utf-8')\"; python tools/evidence/run_canonical_json_gate.py > audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log 2> audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log; python -c \"from pathlib import Path; files=sorted(p.as_posix() for p in Path('audit/gates/json_gate/canonical').rglob('*') if p.is_file()); Path('audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt').write_text('\\\\n'.join(files)+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; files=sorted(p.as_posix() for p in Path('audit/gates/canonical_json').rglob('*') if p.is_file()); Path('audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt').write_text('\\\\n'.join(files)+'\\\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-008/primary.log","audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt","audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt","audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log","audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log","audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt","audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt","audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-03T17:08:50Z"}
planned_step: capture both canonical JSON gate families and run the canonical gate writer
coherence_set: audit/gates/json_gate/canonical + audit/gates/canonical_json
d0_present: yes
run_canonical_json_gate_rc: 0
json_gate_family_before_present: yes
canonical_json_family_before_present: yes
json_gate_family_after_present: yes
canonical_json_family_after_present: yes

### audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt

audit/gates/json_gate/canonical/json_gate_check_log.ndjson
audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt
audit/gates/json_gate/canonical/json_gate_compare_log.ndjson
audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt
audit/gates/json_gate/canonical/json_gate_structured_record.json
audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt

### audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt

audit/gates/canonical_json/canonical_json.gate.json
audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt
audit/gates/canonical_json/cli_surfaces.log
audit/gates/canonical_json/cli_surfaces.log.path_proof.txt
audit/gates/canonical_json/json_canon_compare.log
audit/gates/canonical_json/json_canon_compare.log.path_proof.txt
audit/gates/canonical_json/json_canonical_check.log
audit/gates/canonical_json/json_canonical_check.log.path_proof.txt

### audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log

[empty file]

### audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log

[empty file]

### audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt

0

### audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt

audit/gates/json_gate/canonical/json_gate_check_log.ndjson
audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt
audit/gates/json_gate/canonical/json_gate_compare_log.ndjson
audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt
audit/gates/json_gate/canonical/json_gate_structured_record.json
audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt

### audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt

audit/gates/canonical_json/canonical_json.gate.json
audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt
audit/gates/canonical_json/cli_surfaces.log
audit/gates/canonical_json/cli_surfaces.log.path_proof.txt
audit/gates/canonical_json/json_canon_compare.log
audit/gates/canonical_json/json_canon_compare.log.path_proof.txt
audit/gates/canonical_json/json_canonical_check.log
audit/gates/canonical_json/json_canonical_check.log.path_proof.txt
