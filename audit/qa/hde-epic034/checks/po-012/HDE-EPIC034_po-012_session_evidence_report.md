# HDE-EPIC034 PO-012 Session Evidence Report

## Session Summary

Epic: HDE-EPIC034 / Fermentation Pass 5

Step: CHECK po-012 / PO-012

Local repo state observed during this session:

- Repo root: `/workspaces/glow-hdengine-v2`
- Branch: `main`
- Local HEAD: `daa21f40af2d235486c8784d9e66ba66b56ee02a`
- Note: the PO packet cited remote validation HEAD `e57ff83b9d903c1f8589c80605d209f5729289df`; this local workspace differed.

Work performed:

- Verified required secret-bearing environment variables were present without printing their values: `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY`.
- Verified `.venv/bin/python` was executable.
- Verified the OPS-02 procedure existed at `audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py`.
- Updated the existing QA-created harness at `audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py` to add `po-012` verification.
- Syntax-checked the updated harness with `python -m py_compile`.
- Ran the bounded open-rails OPS-02 smoke exactly once with `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`.
- Ran the closed-rails PO-012 verifier with `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`.
- Verified the PO-012 primary log header reported `status=PASS`, `exit_code=0`, and `check_id=po-012`.
- Verified the primary log sibling path proof points to `audit/qa/hde-epic034/checks/po-012/primary.log`.
- Verified the retained OPS-02 evidence remains bounded to `HDE-FERM008.2`, does not claim full v2 conformance, does not claim HDE-FERM008 parent completion, and remains secret-safe.
- Ran a raw secret scan over the requested deliverables using the current environment values; result: `secret_scan=PASS`.

Command outcomes:

- Bounded open-rails OPS-02 smoke: `PASS`, exit code `0`, `vendor_attempted=true`.
- Closed-rails PO-012 verifier: `PASS`, exit code `0`.

Scope note:

- No PF-Canon files were edited.
- No product code, public route, public Reader contract, acceptance token, manifest, close report, or evidence index/mirror file was intentionally edited.
- The OPS wrapper rewrote its retained OPS-02 evidence outputs as part of the authorized live run.

## Evidence Files Included

This report includes the full current contents of the evidence files produced, updated, or bound for this PO-012 session:

- `audit/qa/hde-epic034/checks/po-012/primary.log`
- `audit/qa/hde-epic034/checks/po-012/primary.log.path_proof.txt`
- `audit/ops/hde-epic034/ops-02/commands.txt`
- `audit/ops/hde-epic034/ops-02/env_presence_redacted.json`
- `audit/ops/hde-epic034/ops-02/exit_codes.txt`
- `audit/ops/hde-epic034/ops-02/files_sha256.txt`
- `audit/ops/hde-epic034/ops-02/request_summary.json`
- `audit/ops/hde-epic034/ops-02/result_summary.json`
- `audit/ops/hde-epic034/ops-02/stderr.log`
- `audit/ops/hde-epic034/ops-02/stdout.log`

## audit/qa/hde-epic034/checks/po-012/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T13:49:52Z", "check_id": "po-012", "check_name": "PO-012", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-012", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-012/primary.log", "audit/qa/hde-epic034/checks/po-012/primary.log.path_proof.txt", "audit/ops/hde-epic034/ops-02/commands.txt", "audit/ops/hde-epic034/ops-02/stdout.log", "audit/ops/hde-epic034/ops-02/files_sha256.txt", "audit/ops/hde-epic034/ops-02/env_presence_redacted.json", "audit/ops/hde-epic034/ops-02/request_summary.json", "audit/ops/hde-epic034/ops-02/result_summary.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-012
check_name=PO-012
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-012
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK audit/ops/hde-epic034/ops-02/commands.txt sha256=50b6b3ee7d8dfecb0a0155be9ed210008526165221710629cc0fa48c625ce739
FILE_OK audit/ops/hde-epic034/ops-02/stdout.log sha256=0f0cd5ab2c25fbc719546fc5aa8c870955f814b4f1b556befd72d1ab9910ab82
FILE_OK audit/ops/hde-epic034/ops-02/files_sha256.txt sha256=08dfbfdb14718e1584a1c4ba79c3ebcbffa1ae6fca5385aaaa33890618291c8b
FILE_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json sha256=566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5
FILE_OK audit/ops/hde-epic034/ops-02/request_summary.json sha256=40a29a73564be3945386134a231905c4daf99a77c5bde362aa4316eed8abb241
FILE_OK audit/ops/hde-epic034/ops-02/result_summary.json sha256=a8e41e93d4f9b2f1330b8bd13e692b65398033695b5fe0fc41bca413070a45ac
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: classification='PASS'
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: exit_code=0
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: vendor_attempted=True
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: full_v2_conformance_claim=False
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: hde_ferm008_parent_completion_claim=False
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: pf09_subtask_id='HDE-FERM008.2'
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: raw_secret_persisted=False
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: full_vendor_payload_persisted=False
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: resource_path='charts/coordinates'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: configured_base_url_key='HD_API_BASE_URL'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: auth_header_posture='Authorization: Bearer <redacted>'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: geocode_key_requirement='not needed'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: legacy_v2_auth_header_posture='HD-Api-Key not used for v2 chart routes'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: SAFE_MODE='0'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: ALLOW_NETWORK='1'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: HD_API_BASE_URL='SET'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: HD_API_KEY='SET'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: GEO_API_KEY='SET'
TEXT_OK audit/ops/hde-epic034/ops-02/commands.txt :: actual_pass_producing_command
```

## audit/qa/hde-epic034/checks/po-012/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-012/primary.log
size_bytes: 3751
sha256: b997d64b348737ced63f10fe1213147d4f54aa8a25c1e89acd5eeb5f23b3c34c
mtime_utc: 2026-06-26T13:49:52Z
produced_at_utc: 2026-06-26T13:49:52Z
```

## audit/ops/hde-epic034/ops-02/commands.txt

```text
# OPS-02 command transcript
work_item=HDE-EPIC034 OPS-02
operator_surface=Codex acting as PO tooling per user authorization
execution_class=bounded open-rails HumanDesignAPI v2 smoke wrapper
remediation_update_utc=2026-06-24T05:24:43Z
further_remediation_update_utc=2026-06-24T06:18:44Z
moon_loop_po_rerun_completed_at_utc=2026-06-24T06:28:13Z
route_resource_path=charts/coordinates
method=POST
rails=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
base_url_env=HD_API_BASE_URL
credential_env=HD_API_KEY
geocode_env=GEO_API_KEY not required for charts/coordinates
auth_header_shape=Authorization: Bearer <redacted>
no_legacy_v2_auth_header=HD-Api-Key not used for v2 chart routes
historical_placeholder_defect=initial packet recorded a placeholder wrapper command; the exact ephemeral wrapper path is not recoverable from repo evidence
reproducible_operator_procedure=audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
actual_pass_producing_command=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
procedure_status=repo-resident secret-safe procedure executed by Codex acting as PO tooling per user authorization; current PASS evidence was produced by this command
current_acceptance_status=PASS
command_to_output_provenance=PASS
rerun_transcript=audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt
required_next_step=bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance or HDE-FERM008 parent completion
activation_bridge_status=not required; .venv/bin/glow-codespaces-env is not repo-resident and .venv/bin/activate is not part of OPS-02 evidence
secret_policy=no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, uncontrolled production data, or full vendor payload bodies are persisted
```

## audit/ops/hde-epic034/ops-02/env_presence_redacted.json

```json
{"ALLOW_NETWORK":"1","APP_ENV":"dev","GEO_API_KEY":"SET","HDAPI_BASE_URL":"UNSET","HD_API_BASE_URL":"SET","HD_API_BASE_URL_expected_v2":true,"HD_API_KEY":"SET","LANG":"C","LC_ALL":"C","SAFE_MODE":"0","TZ":"UTC"}
```

## audit/ops/hde-epic034/ops-02/exit_codes.txt

```text
ops02_wrapper=0
```

## audit/ops/hde-epic034/ops-02/files_sha256.txt

```text
50b6b3ee7d8dfecb0a0155be9ed210008526165221710629cc0fa48c625ce739  audit/ops/hde-epic034/ops-02/commands.txt
566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5  audit/ops/hde-epic034/ops-02/env_presence_redacted.json
354a244d8b29b8086dcaa4b6a48457b06dd6b77ed375ed56bfdf2c077c52e22c  audit/ops/hde-epic034/ops-02/exit_codes.txt
407e1059596cdba51eed4b7f335ef28218f56a80df16148e19c0b7d95c5b4fca  audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
40a29a73564be3945386134a231905c4daf99a77c5bde362aa4316eed8abb241  audit/ops/hde-epic034/ops-02/request_summary.json
a8e41e93d4f9b2f1330b8bd13e692b65398033695b5fe0fc41bca413070a45ac  audit/ops/hde-epic034/ops-02/result_summary.json
01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b  audit/ops/hde-epic034/ops-02/stderr.log
0f0cd5ab2c25fbc719546fc5aa8c870955f814b4f1b556befd72d1ab9910ab82  audit/ops/hde-epic034/ops-02/stdout.log
```

## audit/ops/hde-epic034/ops-02/request_summary.json

```json
{"auth_header_posture":"Authorization: Bearer <redacted>","authorization_header_shape":"Authorization: Bearer <redacted>","body_sha256":"19fd61d354638d44a479dc68de92a62440d94dfc92d17c0e5c19c684621d1db0","configured_base_url_key":"HD_API_BASE_URL","endpoint_path_posture":"/v2/charts/coordinates via HD_API_BASE_URL plus version-neutral resource path","epic_id":"HDE-EPIC034","geocode_key_requirement":"not needed","hd_api_key_header_present":false,"hd_geocode_key_header_present":false,"header_names":["Accept","Authorization","Content-Type","User-Agent"],"input_fingerprint":"19fd61d354638d44a479dc68de92a62440d94dfc92d17c0e5c19c684621d1db0","input_tuple_posture":"synthetic non-PII coordinates tuple; full request body not persisted","legacy_v2_auth_header_posture":"HD-Api-Key not used for v2 chart routes","method":"POST","ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","rails_required":{"ALLOW_NETWORK":"1","SAFE_MODE":"0"},"request_fields":["birthdate","birthtime","lat","lng"],"request_url_posture":"redacted base URL; version-neutral resource path joined by HdApiClient","resource_path":"charts/coordinates"}
```

## audit/ops/hde-epic034/ops-02/result_summary.json

```json
{"classification":"PASS","epic_id":"HDE-EPIC034","exit_code":0,"follow_up":"bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance","full_v2_conformance_claim":false,"full_vendor_payload_persisted":false,"geocode_used":false,"hde_ferm008_3_4_5_completion_claim":false,"hde_ferm008_parent_completion_claim":false,"http_status_present":false,"legacy_hd_api_key_used_for_v2":false,"live_v2_success_claim":true,"ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","raw_secret_persisted":false,"v2_auth_posture":"Authorization: Bearer <redacted>","vendor_attempted":true}
```

## audit/ops/hde-epic034/ops-02/stderr.log

```text
```

## audit/ops/hde-epic034/ops-02/stdout.log

```json
{"attempts":1,"duration_ms_rounded":1867.58,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
```
