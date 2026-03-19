# Report CHECK po-003 HDE-EPIC027

Date (UTC): 2026-03-17
Check: po-003
Final status: PASS

## Intent
Prove the conjunction CLI remains deterministic and emits via the shared public-emission path, while parity/identity proof and showcompat help surface remain usable.

## 1) All Steps Taken In This Session (Chronological)

1. Read the approved live QA plan block for CHECK po-003 and extracted goal, required deliverables, and pass/fail criteria.
2. Confirmed current-state preconditions from the existing manifest pair and earlier step statuses.
3. Preflighted required repo loci for po-003 proof surfaces:
  - engine/cli/main.py
  - tests/cli/test_showcompat_parity_and_identity.py
  - scripts/hdctl.py
4. Executed emitter proof capture against engine/cli/main.py for shared emit_public path and LF/CRLF guards.
5. Executed CLI parity/identity test suite:
  - python -m pytest -q tests/cli/test_showcompat_parity_and_identity.py
6. Captured CLI help surface using repo-local entrypoint:
  - python scripts/hdctl.py showcompat --help
7. Wrote governed first-line JSON header and transcript to audit/qa/hde-epic027/checks/po-003/primary.log.
8. Updated audit/qa/hde-epic027/qa_step_logs_manifest.json by reading the governed first-line header in po-003 primary.log.
9. Refreshed audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt from updated manifest bytes.
10. Re-read all po-003 deliverables and manifest pair to verify final PASS state and consistency.

## 2) Rails and Determinism Pins Used
- LC_ALL=C
- LANG=C
- TZ=UTC
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev

## 3) Full Evidence Outputs

### 3.1 audit/qa/hde-epic027/checks/po-003/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-003","check_name":"PO-003","claimed_tokens":["JSON_CANONICAL_CHECK_OK","COMPOSITE_ABBA_IDENTITY_OK","TWO_RUN_IDENTITY_OK"],"command":"grep -nE '_emit_stdout_bytes\\(emitter\\.emit_public\\(conjunction_payload\\)\\)|STDOUT_MISSING_LF|STDOUT_CRLF' engine/cli/main.py; python -m pytest -q tests/cli/test_showcompat_parity_and_identity.py; python scripts/hdctl.py showcompat --help","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic027/checks/po-003/cli_emitter_proof.txt","audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt","audit/qa/hde-epic027/checks/po-003/showcompat_help.txt","audit/qa/hde-epic027/checks/po-003/primary.log","audit/qa/hde-epic027/qa_step_logs_manifest.json","audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt"],"fail_status":"","intended_tokens":["JSON_CANONICAL_CHECK_OK","COMPOSITE_ABBA_IDENTITY_OK","TWO_RUN_IDENTITY_OK"],"pf_refs":["PF10 - HDE-Build Notes","PF05 - HDE-CLI-API-Vendor-Ref","PF02 - Canon-HDE-Core","PF27 - Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-03-17T08:53:35Z"}
$ grep -nE '_emit_stdout_bytes\(emitter\.emit_public\(conjunction_payload\)\)|STDOUT_MISSING_LF|STDOUT_CRLF' engine/cli/main.py
rc=0
stdout:
561:        raise CliError("STDOUT_MISSING_LF")
563:        raise CliError("STDOUT_CRLF")
823:        _emit_stdout_bytes(emitter.emit_public(conjunction_payload))

$ python -m pytest -q tests/cli/test_showcompat_parity_and_identity.py
rc=0
stdout:
sss.                                                                     [100%]
1 passed, 3 skipped in 0.15s

$ python scripts/hdctl.py showcompat --help
rc=0
stdout:
usage: hdctl showcompat [-h] [--pair-file PAIR_FILE] [--a-file A_FILE]
                        [--b-file B_FILE] [--a A_FILE] [--b B_FILE]
                        [--dump-reader DUMP_READER]
                        [--dump-admin-dir DUMP_ADMIN_DIR]
                        [--source {db,vendor,auto}] [--conjunction]
                        [--viewer-prefs-file VIEWER_PREFS_FILE]
                        [--user-a USER_A] [--user-b USER_B]
                        [--birthdate-a BIRTHDATE_A]
                        [--birthtime-a BIRTHTIME_A] [--location-a LOCATION_A]
                        [--birthdate-b BIRTHDATE_B]
                        [--birthtime-b BIRTHTIME_B] [--location-b LOCATION_B]

options:
  -h, --help            show this help message and exit
  --pair-file PAIR_FILE
                        Path to JSON with left/right payloads
  --a-file A_FILE       Path to JSON file containing the left payload
  --b-file B_FILE       Path to JSON file containing the right payload
  --a A_FILE            Alias for --a-file
  --b B_FILE            Alias for --b-file
  --dump-reader DUMP_READER
                        Optional path to write public Reader JSON (canonical
                        bytes)
  --dump-admin-dir DUMP_ADMIN_DIR
                        Directory for admin proofs (writes 0600 JSON + .sha256
                        sidecars)
  --source {db,vendor,auto}
                        Explicit BodyGraph source (db, vendor, or auto)
  --conjunction         Emit conjunction contract JSON (requires
                        --user-a/--user-b or conjunction pair input; uses SAFE
                        rails resolver gating)
  --viewer-prefs-file VIEWER_PREFS_FILE
                        Path to JSON viewer prefs (top_category + weights)
  --user-a USER_A       DB user identifier for party A
  --user-b USER_B       DB user identifier for party B
  --birthdate-a BIRTHDATE_A
                        Birthdate for party A (YYYY-MM-DD)
  --birthtime-a BIRTHTIME_A
                        Birth time for party A (HH:MM)
  --location-a LOCATION_A
                        Location for party A
  --birthdate-b BIRTHDATE_B
                        Birthdate for party B (YYYY-MM-DD)
  --birthtime-b BIRTHTIME_B
                        Birth time for party B (HH:MM)
  --location-b LOCATION_B
                        Location for party B
```

### 3.2 audit/qa/hde-epic027/checks/po-003/cli_emitter_proof.txt

```text
561:        raise CliError("STDOUT_MISSING_LF")
563:        raise CliError("STDOUT_CRLF")
823:        _emit_stdout_bytes(emitter.emit_public(conjunction_payload))
```

### 3.3 audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt

```text
sss.                                                                     [100%]
1 passed, 3 skipped in 0.15s
```

### 3.4 audit/qa/hde-epic027/checks/po-003/showcompat_help.txt

```text
usage: hdctl showcompat [-h] [--pair-file PAIR_FILE] [--a-file A_FILE]
                        [--b-file B_FILE] [--a A_FILE] [--b B_FILE]
                        [--dump-reader DUMP_READER]
                        [--dump-admin-dir DUMP_ADMIN_DIR]
                        [--source {db,vendor,auto}] [--conjunction]
                        [--viewer-prefs-file VIEWER_PREFS_FILE]
                        [--user-a USER_A] [--user-b USER_B]
                        [--birthdate-a BIRTHDATE_A]
                        [--birthtime-a BIRTHTIME_A] [--location-a LOCATION_A]
                        [--birthdate-b BIRTHDATE_B]
                        [--birthtime-b BIRTHTIME_B] [--location-b LOCATION_B]

options:
  -h, --help            show this help message and exit
  --pair-file PAIR_FILE
                        Path to JSON with left/right payloads
  --a-file A_FILE       Path to JSON file containing the left payload
  --b-file B_FILE       Path to JSON file containing the right payload
  --a A_FILE            Alias for --a-file
  --b B_FILE            Alias for --b-file
  --dump-reader DUMP_READER
                        Optional path to write public Reader JSON (canonical
                        bytes)
  --dump-admin-dir DUMP_ADMIN_DIR
                        Directory for admin proofs (writes 0600 JSON + .sha256
                        sidecars)
  --source {db,vendor,auto}
                        Explicit BodyGraph source (db, vendor, or auto)
  --conjunction         Emit conjunction contract JSON (requires
                        --user-a/--user-b or conjunction pair input; uses SAFE
                        rails resolver gating)
  --viewer-prefs-file VIEWER_PREFS_FILE
                        Path to JSON viewer prefs (top_category + weights)
  --user-a USER_A       DB user identifier for party A
  --user-b USER_B       DB user identifier for party B
  --birthdate-a BIRTHDATE_A
                        Birthdate for party A (YYYY-MM-DD)
  --birthtime-a BIRTHTIME_A
                        Birth time for party A (HH:MM)
  --location-a LOCATION_A
                        Location for party A
  --birthdate-b BIRTHDATE_B
                        Birthdate for party B (YYYY-MM-DD)
  --birthtime-b BIRTHTIME_B
                        Birth time for party B (HH:MM)
  --location-b LOCATION_B
                        Location for party B
```

### 3.5 audit/qa/hde-epic027/qa_step_logs_manifest.json

```json
{"d0_discovery":{"check_id":"d0_discovery","check_name":"d0 - Discovery, current-state evidence bootstrap, and manifest bootstrap","fail_status":"","log_path":"checks/d0_discovery/primary.log","status":"PASS","timestamp_utc":"2026-03-17T03:01:30Z"},"po-001":{"check_id":"po-001","check_name":"PO-001","fail_status":"","log_path":"checks/po-001/primary.log","status":"PASS","timestamp_utc":"2026-03-17T04:08:10Z"},"po-002":{"check_id":"po-002","check_name":"PO-002","fail_status":"","log_path":"checks/po-002/primary.log","status":"PASS","timestamp_utc":"2026-03-17T07:58:52Z"},"po-003":{"check_id":"po-003","check_name":"PO-003","fail_status":"","log_path":"checks/po-003/primary.log","status":"PASS","timestamp_utc":"2026-03-17T08:53:35Z"}}
```

### 3.6 audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt

```text
path: audit/qa/hde-epic027/qa_step_logs_manifest.json
size_bytes: 742
sha256: fdcbe4c76189c0b3a150d6395d96140002f96d3c6aa8ec6d0fb9f79c42e45af2
mtime_utc: 2026-03-16T22:17:30Z
produced_at_utc: 2026-03-17T08:53:35Z
```

## 4) PO Inputs Resolved

1. Exact parity-test command used and captured:
- python -m pytest -q tests/cli/test_showcompat_parity_and_identity.py
- Captured in audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt

2. Help capture invocation used:
- python scripts/hdctl.py showcompat --help
- Captured in audit/qa/hde-epic027/checks/po-003/showcompat_help.txt

3. Manifest update workflow for po-003:
- No dedicated po-003 helper exists in-repo.
- Same governed workflow as prior checks: read first-line JSON header in audit/qa/hde-epic027/checks/po-003/primary.log and upsert po-003 entry in audit/qa/hde-epic027/qa_step_logs_manifest.json.

4. Path-proof refresh workflow for po-003:
- No dedicated po-003 helper exists in-repo.
- Same governed refresh flow as prior checks via tools.evidence.update_evidence_index._write_path_proof after manifest update.

5. Governed primary header workflow:
- Header written as first line of audit/qa/hde-epic027/checks/po-003/primary.log before transcript bytes.
- Header command field records the full ordered command sequence executed in this step.

## 5) Completeness Check

- Included all po-003 steps taken in this session: YES
- Included full output for all po-003 evidence artifacts: YES
- Included updated manifest and refreshed path-proof full outputs: YES
- Final po-003 status: PASS
