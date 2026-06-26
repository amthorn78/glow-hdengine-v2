# HDE-EPIC034 po-004 through po-008 Session Report

## Scope

This report covers the Codex session work for HDE-EPIC034 / Fermentation Pass 5 selected checks:

- po-004
- po-005
- po-006
- po-007
- po-008

## Work Completed

The QA-created harness at `audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py` was extended in place to support checks `po-004` through `po-008` while preserving the existing `step-0b-doc-delta-capture`, `po-001`, `po-002`, and `po-003` checks.

The following closed-rails commands were run:

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-004
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-005
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-006
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-007
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-008
```

All five checks returned `status=PASS` and `exit_code=0`.

Verification performed after generation:

- Confirmed each primary log header reports `status=PASS` and `exit_code=0`.
- Confirmed each header lists its sibling `.path_proof.txt` path.
- Confirmed each path proof points to the expected `primary.log`.
- Ran `python -m py_compile audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py` successfully.

## Evidence Files Produced

The following evidence files were produced in this session:

- `audit/qa/hde-epic034/checks/po-004/primary.log`
- `audit/qa/hde-epic034/checks/po-004/primary.log.path_proof.txt`
- `audit/qa/hde-epic034/checks/po-005/primary.log`
- `audit/qa/hde-epic034/checks/po-005/primary.log.path_proof.txt`
- `audit/qa/hde-epic034/checks/po-006/primary.log`
- `audit/qa/hde-epic034/checks/po-006/primary.log.path_proof.txt`
- `audit/qa/hde-epic034/checks/po-007/primary.log`
- `audit/qa/hde-epic034/checks/po-007/primary.log.path_proof.txt`
- `audit/qa/hde-epic034/checks/po-008/primary.log`
- `audit/qa/hde-epic034/checks/po-008/primary.log.path_proof.txt`

## Full Evidence Contents

### audit/qa/hde-epic034/checks/po-004/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T11:01:23Z", "check_id": "po-004", "check_name": "PO-004", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-004", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-004/primary.log", "audit/qa/hde-epic034/checks/po-004/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-004
check_name=PO-004
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-004
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json sha256=d789bcf5aa1d3db6bbcd7673f901f1152ae49eceb6550922586c30f8fff2ebba
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "v2_auth_header_posture":"Authorization: Bearer <redacted>"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "v1_legacy_auth_header_posture":"HD-Api-Key: <redacted>"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "credential_env_var":"HD_API_KEY"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: <redacted>
```

### audit/qa/hde-epic034/checks/po-004/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-004/primary.log
size_bytes: 1554
sha256: 7689cf2b549fc3be6a5b93c8aa60d7b5da41057595f01befdf01ffe3fd0e6667
mtime_utc: 2026-06-26T11:01:23Z
produced_at_utc: 2026-06-26T11:01:23Z
```

### audit/qa/hde-epic034/checks/po-005/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T11:01:23Z", "check_id": "po-005", "check_name": "PO-005", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-005", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-005/primary.log", "audit/qa/hde-epic034/checks/po-005/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-005
check_name=PO-005
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-005
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json sha256=d789bcf5aa1d3db6bbcd7673f901f1152ae49eceb6550922586c30f8fff2ebba
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "geocode_env_var":"GEO_API_KEY"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "geocode_header_posture":"HD-Geocode-Key: <redacted>"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "geocode_key_requirement":"required"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "geocode_key_requirement":"not needed"
TEXT_OK artifacts/vendor/hdapi_v2/request_shaping.snapshot.json :: "geocode_env_var":"not applicable"
```

### audit/qa/hde-epic034/checks/po-005/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-005/primary.log
size_bytes: 1656
sha256: 8ef5e20ce40afbbd76629d005a0982c98ba379c949c446b9ea84779494a57658
mtime_utc: 2026-06-26T11:01:23Z
produced_at_utc: 2026-06-26T11:01:23Z
```

### audit/qa/hde-epic034/checks/po-006/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T11:01:23Z", "check_id": "po-006", "check_name": "PO-006", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-006", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-006/primary.log", "audit/qa/hde-epic034/checks/po-006/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-006
check_name=PO-006
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-006
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json sha256=0425b010ad22ddaee335fe98b3a276d9673ae3fbf41268f16f1f1158885f3db3
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "response_envelope_fields":["timestamp","success","message","errorCode","type","data"]
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "success_status_handling"
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "errorCode_handling"
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "data_payload_body_emitted":false
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "route_variant":"coordinates_chart"
```

### audit/qa/hde-epic034/checks/po-006/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-006/primary.log
size_bytes: 1670
sha256: 1a48e0d5b465f670978df42e66272e9ea03e5564f0af355dfc46baec88991fcb
mtime_utc: 2026-06-26T11:01:23Z
produced_at_utc: 2026-06-26T11:01:23Z
```

### audit/qa/hde-epic034/checks/po-007/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T11:01:23Z", "check_id": "po-007", "check_name": "PO-007", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-007", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-007/primary.log", "audit/qa/hde-epic034/checks/po-007/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-007
check_name=PO-007
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-007
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json sha256=0425b010ad22ddaee335fe98b3a276d9673ae3fbf41268f16f1f1158885f3db3
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "schema_gap_status":"GAP_RECORDED"
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "no_compatibility_by_inference":true
TEXT_OK artifacts/vendor/hdapi_v2/response_mapping.snapshot.json :: "normalized_data_path_proof_claim":"NONE"
```

### audit/qa/hde-epic034/checks/po-007/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-007/primary.log
size_bytes: 1444
sha256: 6785d0121c1c2915bb340bae015d4f94edb104ae1cd9f9ded9c17cc5bd0c98e2
mtime_utc: 2026-06-26T11:01:23Z
produced_at_utc: 2026-06-26T11:01:23Z
```

### audit/qa/hde-epic034/checks/po-008/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T11:01:23Z", "check_id": "po-008", "check_name": "PO-008", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-008", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-008/primary.log", "audit/qa/hde-epic034/checks/po-008/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-008
check_name=PO-008
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-008
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK artifacts/vendor/hdapi_v2/adapter_boundary_proof.log sha256=aeae687678351afc698acbd2ddaa0ca507b545714df05ca0a51e7b6f6d3181a6
TEXT_OK artifacts/vendor/hdapi_v2/adapter_boundary_proof.log :: adapter/presenter boundary taxonomy proof
TEXT_OK artifacts/vendor/hdapi_v2/adapter_boundary_proof.log :: adapter routes resolve to sanctioned presenter/emitter calls
TEXT_OK artifacts/vendor/hdapi_v2/adapter_boundary_proof.log :: bounded_static_grammar_posture
```

### audit/qa/hde-epic034/checks/po-008/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-008/primary.log
size_bytes: 1444
sha256: 816c21348998c397889f3f57a07324d94ca98c8db2761cb0756ed2eb3e2af453
mtime_utc: 2026-06-26T11:01:23Z
produced_at_utc: 2026-06-26T11:01:23Z
```
