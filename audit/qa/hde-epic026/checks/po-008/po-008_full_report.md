# HDE-EPIC026 — Detailed QA Report (po-008)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-008`
- Check name: `PO-008 — CLI conjunction mode + canonical JSON + modifier rejection`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-26

---

## Executive summary

CHECK `po-008` is **PASS**.

PASS criteria from the approved plan are satisfied:

- `hdctl --help` succeeded (`rc=0`),
- `hdctl showcompat --help` succeeded (`rc=0`),
- non-json conjunction modifier rejection failed fast (`reject_nonjson_rc=64`, non-zero), and
- optional real conjunction run was **not executed** because `USER_A_ID` / `USER_B_ID` were empty (allowed by plan posture).

---

## Detailed chronology (all steps run)

### 1) Variable import and rails/determinism pins

- Set step environment under stable epic QA root:
  - `EVIDENCE_ROOT=audit/qa/hde-epic026`
  - `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
  - `LANG=C`, `LC_ALL=C`, `TZ=UTC`
  - `USER_A_ID=""`, `USER_B_ID=""` (optional conjunction output run intentionally skipped)

### 2) Setup and helper load

- Confirmed evidence root posture under `audit/qa/` and not `docs/`.
- Loaded helper file at:
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`

### 3) CLI help surface capture

- Captured `hdctl --help` to `cli_help.txt` with `rc=0`.
- Captured `hdctl showcompat --help` to `showcompat_help.txt` with `rc=0`.

### 4) Modifier rejection negative test

- Ran non-json conjunction invocation:
  - `hdctl showcompat --conjunction --user-a foo --user-b bar --format yaml`
- Result:
  - `reject_nonjson_rc=64` (non-zero expected)
  - stderr contains: `unrecognized arguments: --format yaml`

### 5) Optional conjunction output run branch

- Since `USER_A_ID` and `USER_B_ID` were empty, optional real conjunction JSON run and canonical key-order/trailing-LF check were skipped per plan-allowed optional path.

### 6) Finalization and manifest append

- Wrote `primary.log` PF27 header + body summary.
- Added manifest entry under:
  - `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`
  - `check_id=po-008`, `status=PASS`, `log_path=checks/po-008/primary.log`

---

## PASS/FAIL criteria evaluation

Plan criteria:

- PASS if:
  - `hdctl --help` and `hdctl showcompat --help` succeed,
  - non-json modifier rejection returns non-zero exit,
  - if conjunction output run is executed, it succeeds and passes canonical key-order check.

Observed:

- `hdctl_help_rc=0`
- `showcompat_help_rc=0`
- `reject_nonjson_rc=64` (non-zero)
- optional conjunction run skipped due to empty user IDs

Decision: **PASS**.

---

## Required deliverables and evidence contents

All expected outputs are present under `audit/qa/hde-epic026/checks/po-008/`:

- `primary.log`
- `cli_help.txt`
- `showcompat_help.txt`
- `reject_nonjson_stdout.log`
- `reject_nonjson_stderr.log`
- `reject_nonjson_rc.txt`

Optional outputs (`cli_conjunction.json`, `cli_conjunction_rc.txt`, `canonical_keyorder_check.txt`) were not generated because IDs were intentionally not provided.

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-008/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-26T02:21:43Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-008", "check_name": "PO-008 — CLI conjunction mode + canonical JSON + modifier rejection", "pass_fail": "PASS", "fail_status": "", "intended_tokens": ["A3"], "claimed_tokens": [], "commands": ["hdctl --help", "hdctl showcompat --help", "hdctl showcompat --conjunction --user-a foo --user-b bar --format yaml", "hdctl showcompat --conjunction --user-a $USER_A_ID --user-b $USER_B_ID --format json (optional)"], "artifacts": [{"path": "cli_help.txt", "type": "text", "desc": "hdctl help"}, {"path": "showcompat_help.txt", "type": "text", "desc": "showcompat help"}, {"path": "reject_nonjson_stdout.log", "type": "log", "desc": "stdout for non-json rejection"}, {"path": "reject_nonjson_stderr.log", "type": "log", "desc": "stderr for non-json rejection"}, {"path": "reject_nonjson_rc.txt", "type": "text", "desc": "exit code for non-json rejection"}], "pf_refs": ["PF10 §2.17-§2.18", "PF05 §6.1 Canonical JSON", "PF02 §3.3 Rails and determinism"]}

###
hdctl_help_rc=0
showcompat_help_rc=0
reject_nonjson_rc=64
conjunction_run=SKIPPED_NO_USER_IDS
pass_fail=PASS
```

### 2) `cli_help.txt`

Path: `audit/qa/hde-epic026/checks/po-008/cli_help.txt`

```text
usage: hdctl [-h] {showcompat,aux-preview,bg:resolve,dev:sampler} ...

Glow HD Engine compatibility CLI

positional arguments:
  {showcompat,aux-preview,bg:resolve,dev:sampler}
    showcompat          Emit canonical Reader v1 bytes from vendor JSON (stdin
                        or files)
    aux-preview         Preview Aux narrative text for a public tuple
    bg:resolve          Resolve BodyGraphs from db/vendor sources (Phase S8a
                        stub)
    dev:sampler         DEV/ADMIN ONLY: deterministic sampler harness
                        (seedable)

options:
  -h, --help            show this help message and exit
```

### 3) `showcompat_help.txt`

Path: `audit/qa/hde-epic026/checks/po-008/showcompat_help.txt`

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

### 4) `reject_nonjson_stdout.log`

Path: `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stdout.log`

```text
(empty file)
```

### 5) `reject_nonjson_stderr.log`

Path: `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stderr.log`

```log
usage: hdctl [-h] {showcompat,aux-preview,bg:resolve,dev:sampler} ...
hdctl: error: unrecognized arguments: --format yaml
```

### 6) `reject_nonjson_rc.txt`

Path: `audit/qa/hde-epic026/checks/po-008/reject_nonjson_rc.txt`

```text
64
```

---

## Manifest trail for po-008

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

- `2026-02-26T02:21:43Z` — `po-008` — `PASS` — `sha256=ee5da4fb490ac1f651811ce0024efc60aef6707035ce0e014f9b0bed752eca57`

---

## Integrity snapshot (sha256)

- `primary.log`: `ee5da4fb490ac1f651811ce0024efc60aef6707035ce0e014f9b0bed752eca57`
- `cli_help.txt`: `07a8d7cfccf832a24f81af0a569885c9a4449b487ccef7d3d3edc474dd16516d`
- `showcompat_help.txt`: `f9cdc8861dee7e3fb5f34c244e56a66f4660f679f29e6cd0badf28690ea82035`
- `reject_nonjson_stdout.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `reject_nonjson_stderr.log`: `145dc3617d18f80b3dbc70f87c37f65b4e87314976b0fb3d28ecbd219a413bc3`
- `reject_nonjson_rc.txt`: `913f5d1da2feaf4deeccc9e55cbb350a20f12b3f507e87be85dbb77fdd3cb9bc`

---

## Conclusion

`po-008` is complete and PASS. CLI help surfaces are available, non-json conjunction modifier rejection behaves correctly (non-zero failure), and the step evidence is captured under the stable checks-only epic QA layout.
