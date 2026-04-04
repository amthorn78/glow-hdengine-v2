# HDE-EPIC028 PO-006 Full Action Log

## Manifest Header
- HDE-EPIC: HDE-EPIC028 / Conjunction Pass 4
- Step: PO-006 - Governed public success surface transport posture
- Approved QA Plan File: r9 Live QA Plan HDE-EPIC028.md
- Approval Doc File: none
- Previous Step Report File: report - po-005 QA HDE-EPIC028.md
- PF-Canon consulted: PF10 (current) + PF05 + PF02
- Generated at (UTC): 2026-04-03T14:14:37Z

## Outcome
- Final status: PASS
- Fail status: (empty)
- Branch policy: Run Reader transport proof only after governed proof-surface resolution from PO-005

## Rails and Repo State
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC
- git HEAD: e5703d58447f38394f25cbcd113eebf6883366b5
- git status (po-006 scope):

?? audit/qa/hde-epic028/checks/po-006/

## Executed Actions
1. Confirmed D0, PO-005 primary artifact, and Reader transport test locus exist at approved paths.
2. Copied PO-005 primary artifact into po-006/po_005_lookup.txt as the deciding lookup for this step.
3. Evaluated lookup resolution and wrote branch_note/blocked_reason into blocked_note.txt.
4. Executed Reader transport test only on resolved branch and captured stdout/stderr/rc artifacts.
5. Wrote po-006 primary.log with the correct status lane and decision note.

## Commands Used
- set -euo pipefail
- export LC_ALL=C
- export LANG=C
- export TZ=UTC
- export SAFE_MODE=1
- export ALLOW_NETWORK=0
- export APP_ENV=dev
- mkdir -p audit/qa/hde-epic028/checks/po-006
- test -f audit/qa/hde-epic028/checks/d0/primary.log
- test -f audit/qa/hde-epic028/checks/po-005/primary.log
- test -f tests/http/test_reader_a7_transport.py
- python: copy po-005 primary.log -> po-006/po_005_lookup.txt
- python: derive resolved branch note -> po-006/blocked_note.txt
- python: run pytest only if resolved -> pytest_stdout.log, pytest_stderr.log, pytest_rc.txt
- python: write po-006/primary.log using PASS/FAIL_BEHAVIOR/TOOLING_BLOCKED branch

## Evidence Outputs (Metadata)
- audit/qa/hde-epic028/checks/po-006/primary.log
  - sha256: d09a6446799515a44fbedd069e7dd267e787fc84d6fba3d2799743c0ac728bc4
  - size_bytes: 3211
  - mtime_epoch: 1775225565
- audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt
  - sha256: 2543c344201eb8839738633ccc32da6eea8cb1505e76c492497e47e3d1ee3a40
  - size_bytes: 2015
  - mtime_epoch: 1775225562
- audit/qa/hde-epic028/checks/po-006/blocked_note.txt
  - sha256: 4e96b7eb6c4b272b60e765f797ac118ecdf6a0e0a03282498c9d1cc7949901fb
  - size_bytes: 148
  - mtime_epoch: 1775225562
- audit/qa/hde-epic028/checks/po-006/pytest_stdout.log
  - sha256: b336bfbb42d8a55315e2f7350d4a6528e0fd95453f81c1e21f96f9ae7c5d2932
  - size_bytes: 98
  - mtime_epoch: 1775225565
- audit/qa/hde-epic028/checks/po-006/pytest_stderr.log
  - sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  - size_bytes: 0
  - mtime_epoch: 1775225565
- audit/qa/hde-epic028/checks/po-006/pytest_rc.txt
  - sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
  - size_bytes: 2
  - mtime_epoch: 1775225565

## Evidence Outputs (Full Verbatim Content)
### audit/qa/hde-epic028/checks/po-006/primary.log

{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-006","check_name":"Governed public success surface transport posture","claimed_tokens":[],"command":"python - <<'PY'\\nfrom pathlib import Path\\nsrc = Path(\"audit/qa/hde-epic028/checks/po-005/primary.log\")\\ndst = Path(\"audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt\")\\ndst.write_text(src.read_text(encoding=\"utf-8\"), encoding=\"utf-8\")\\nPY; python - <<'PY'\\nfrom pathlib import Path\\nlookup = Path(\"audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt\").read_text(encoding=\"utf-8\")\\nresolved = ('\\\"status\\\":\\\"PASS\\\"' in lookup and '/reader is the governed Reader success-proof surface' in lookup and 'APP_ENV=dev gating' in lookup and 'a7_eligible:true' in lookup)\\nnote = (\"branch_note: po-005 lookup confirms /reader as the governed Reader success-proof surface for the current HDE-EPIC028 scope under PF10 addendum 2.14\\\\n\" if resolved else \"blocked_reason: po-005 did not prove one governed Reader success-proof surface\\\\n\")\\nPath(\"audit/qa/hde-epic028/checks/po-006/blocked_note.txt\").write_text(note, encoding=\"utf-8\")\\nPY; python - <<'PY'\\nfrom pathlib import Path\\nimport subprocess\\nlookup = Path(\"audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt\").read_text(encoding=\"utf-8\")\\nresolved = ('\\\"status\\\":\\\"PASS\\\"' in lookup and '/reader is the governed Reader success-proof surface' in lookup and 'APP_ENV=dev gating' in lookup and 'a7_eligible:true' in lookup)\\nstdout_path = Path(\"audit/qa/hde-epic028/checks/po-006/pytest_stdout.log\")\\nstderr_path = Path(\"audit/qa/hde-epic028/checks/po-006/pytest_stderr.log\")\\nrc_path = Path(\"audit/qa/hde-epic028/checks/po-006/pytest_rc.txt\")\\nif not resolved:\\n    stdout_path.write_text(\"\", encoding=\"utf-8\")\\n    stderr_path.write_text(\"\", encoding=\"utf-8\")\\n    rc_path.write_text(\"NOT_RUN\\\\n\", encoding=\"utf-8\")\\nelse:\\n    r = subprocess.run([\"python\", \"-m\", \"pytest\", \"-q\", \"tests/http/test_reader_a7_transport.py\"], capture_output=True, text=True)\\n    stdout_path.write_text(r.stdout, encoding=\"utf-8\")\\n    stderr_path.write_text(r.stderr, encoding=\"utf-8\")\\n    rc_path.write_text(f\"{r.returncode}\\\\n\", encoding=\"utf-8\")\\nPY","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-006/primary.log","audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt","audit/qa/hde-epic028/checks/po-006/blocked_note.txt","audit/qa/hde-epic028/checks/po-006/pytest_stdout.log","audit/qa/hde-epic028/checks/po-006/pytest_stderr.log","audit/qa/hde-epic028/checks/po-006/pytest_rc.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 — HDE-Build Notes","PF05 — HDE-CLI-API-Vendor-Ref","PF02 — HDE-Architecture","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-03T14:12:45Z"}
planned_step: run Reader transport proof only after the governed proof-surface designation is resolved
decision_note: po-005 lookup confirmed /reader as the governed Reader success-proof surface and the Reader transport test exited 0

### audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt

{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-005","check_name":"Governed Reader proof-surface designation","claimed_tokens":[],"command":"python -c \"from pathlib import Path; src=Path('docs/ENDPOINTS_CATALOG.json').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt').write_text('\\\\n'.join(src[:40])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('adapter/http_reader.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt').write_text('\\\\n'.join(src[:180])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; Path('audit/qa/hde-epic028/checks/po-005/blocked_note.txt').write_text('lookup_note: /reader remains the current Reader route under review; success_endpoints is empty while /reader is marked a7_eligible:true, and PF10 addendum 2.14 treats that missing explicit designation as downstream canon drift rather than a reason to invent a second proof-surface mechanism for this step\\\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-005/primary.log","audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt","audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt","audit/qa/hde-epic028/checks/po-005/blocked_note.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 — HDE-Build Notes","PF05 — HDE-CLI-API-Vendor-Ref","PF02 — HDE-Architecture","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-02T22:00:49Z"}
planned_step: capture the current Reader catalog row and route ownership proof
decision_note: under PF10 addendum 2.14, /reader is the governed Reader success-proof surface for the current HDE-EPIC028 scope when the approved lookup artifact shows route existence, APP_ENV=dev gating, and a7_eligible:true

### audit/qa/hde-epic028/checks/po-006/blocked_note.txt

branch_note: po-005 lookup confirms /reader as the governed Reader success-proof surface for the current HDE-EPIC028 scope under PF10 addendum 2.14

### audit/qa/hde-epic028/checks/po-006/pytest_stdout.log

.                                                                        [100%]
1 passed in 0.49s

### audit/qa/hde-epic028/checks/po-006/pytest_stderr.log

[empty file]

### audit/qa/hde-epic028/checks/po-006/pytest_rc.txt

0
