# HDE-EPIC034 OPS-02 Full Action Log and Evidence Output

generated_at_utc: 2026-06-24T05:43:32Z

repo_root: `/workspaces/glow-hdengine-v2`

branch: `main`

current_head: `8f4d0b837f0e1ad2bce4ea77237a2a4656818d68`

primary_evidence_root: `audit/ops/hde-epic034/ops-02/`

## Scope

This packet records the remediated OPS-02 evidence posture for HDE-EPIC034, the PO-authorized open-rails HumanDesignAPI v2 smoke for PF09.5 HDE-FERM008.2.

The original live smoke evidence remains bounded to one HumanDesignAPI-only v2 chart smoke using the version-neutral resource path `charts/coordinates` under `HD_API_BASE_URL`. The coordinate route does not require geocoding. This packet does not re-execute the vendor call.

This packet does not claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, HDE-FERM008.3/.4/.5 completion, public Reader change, AI scope, or vendor payload persistence.

## Action Log

1. Read the OPS-02 final review/remediation request and existing repo-resident evidence under `audit/ops/hde-epic034/ops-02/`.
2. Confirmed the review blockers: `commands.txt` had used a placeholder wrapper command, and the prior action report claimed a virtualenv helper that was not repo-resident.
3. Inspected EPIC034 plan posture, OPS-02 packet contents, HDAPI v2 request-shaping evidence, and `engine.bodygraph.vendor_client.HdApiClient`.
4. Removed the tracked `.venv/bin/activate` hook that sourced `.venv/bin/glow-codespaces-env`.
5. Persisted a concrete repo-resident, secret-safe operator procedure at `audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py`.
6. Updated `commands.txt` with an exact command using `.venv/bin/python` and the persisted procedure.
7. Recorded the original placeholder command as a defect without retaining the placeholder token.
8. Updated `ops02_full_action_report.md` to document the remediation and to remove the unresolved environment-bridge claim.
9. Refreshed `files_sha256.txt` for the primary OPS-02 evidence set.
10. Verified checksums, JSON parsing, syntax-only compile, LF endings, placeholder absence, activation-hook absence, and raw-secret scans.

## Remediation Outcome

```text
OPS02_REMEDIATION_CLASSIFICATION=PASS
OPS02_VENDOR_RERUN=false
OPS02_PLACEHOLDER_COMMAND_REMEDIATED=true
OPS02_ENV_BRIDGE_CONTRADICTION_REMEDIATED=true
OPS02_PRIMARY_CHECKSUMS_OK=true
```

## Evidence Files

```text
audit/ops/hde-epic034/ops-02/commands.txt
audit/ops/hde-epic034/ops-02/env_presence_redacted.json
audit/ops/hde-epic034/ops-02/exit_codes.txt
audit/ops/hde-epic034/ops-02/files_sha256.txt
audit/ops/hde-epic034/ops-02/ops02_full_action_report.md
audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
audit/ops/hde-epic034/ops-02/request_summary.json
audit/ops/hde-epic034/ops-02/result_summary.json
audit/ops/hde-epic034/ops-02/stderr.log
audit/ops/hde-epic034/ops-02/stdout.log
```

## Command Transcript

```text
# OPS-02 command transcript
work_item=HDE-EPIC034 OPS-02
operator_surface=Codex acting as PO tooling per user authorization
execution_class=bounded open-rails HumanDesignAPI v2 smoke wrapper
remediation_update_utc=2026-06-24T05:24:43Z
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
command=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
procedure_status=repo-resident secret-safe procedure for a bounded charts/coordinates smoke; remediation did not re-execute the vendor call
activation_bridge_status=not required; .venv/bin/glow-codespaces-env is not repo-resident and .venv/bin/activate is not part of OPS-02 evidence
secret_policy=no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, uncontrolled production data, or full vendor payload bodies are persisted
```

## Redacted Environment Evidence

```json
{"ALLOW_NETWORK":"1","APP_ENV":"dev","GEO_API_KEY":"SET","HDAPI_BASE_URL":"UNSET","HD_API_BASE_URL":"SET","HD_API_BASE_URL_expected_v2":true,"HD_API_KEY":"SET","LANG":"C","LC_ALL":"C","SAFE_MODE":"0","TZ":"UTC"}
```

## Request Summary Evidence

```json
{"auth_header_posture":"Authorization: Bearer <redacted>","authorization_header_shape":"Authorization: Bearer <redacted>","body_sha256":"cb0005717a709aaeb3f4a652bafc33450f5e853d95fd60de034b2f805e49b0ff","configured_base_url_key":"HD_API_BASE_URL","endpoint_path_posture":"/v2/charts/coordinates via HD_API_BASE_URL plus version-neutral resource path","epic_id":"HDE-EPIC034","generated_at_utc":"2026-06-23T22:00:01Z","geocode_key_requirement":"not needed","hd_api_key_header_present":false,"hd_geocode_key_header_present":false,"header_names":["Accept","Authorization","Content-Type","User-Agent"],"input_fingerprint":"cb0005717a709aaeb3f4a652bafc33450f5e853d95fd60de034b2f805e49b0ff","input_tuple_posture":"synthetic non-PII coordinates tuple; full request body not persisted","legacy_v2_auth_header_posture":"HD-Api-Key not used for v2 chart routes","method":"POST","ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","rails_required":{"ALLOW_NETWORK":"1","SAFE_MODE":"0"},"request_fields":["birthdate","birthtime","lat","lng"],"request_url_posture":"redacted base URL; version-neutral resource path joined by HdApiClient","resource_path":"charts/coordinates"}
```

## Stdout Evidence

```json
{"attempts":1,"duration_ms_rounded":4088.122,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
```

## Stderr Evidence

```text

```

## Exit Code Evidence

```text
ops02_wrapper=0
```

## Result Summary Evidence

```json
{"classification":"PASS","epic_id":"HDE-EPIC034","exit_code":0,"follow_up":"bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance","full_v2_conformance_claim":false,"full_vendor_payload_persisted":false,"generated_at_utc":"2026-06-23T22:00:05Z","geocode_used":false,"hde_ferm008_3_4_5_completion_claim":false,"hde_ferm008_parent_completion_claim":false,"http_status_present":false,"legacy_hd_api_key_used_for_v2":false,"live_v2_success_claim":true,"ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","raw_secret_persisted":false,"v2_auth_posture":"Authorization: Bearer <redacted>","vendor_attempted":true}
```

## Checksum Evidence

```text
3346efd8375fc6b4e5a50550a22e97c6fe6bf32b43e4f71aff5fc14dd346864d  audit/ops/hde-epic034/ops-02/commands.txt
566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5  audit/ops/hde-epic034/ops-02/env_presence_redacted.json
354a244d8b29b8086dcaa4b6a48457b06dd6b77ed375ed56bfdf2c077c52e22c  audit/ops/hde-epic034/ops-02/exit_codes.txt
407e1059596cdba51eed4b7f335ef28218f56a80df16148e19c0b7d95c5b4fca  audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
e3caed458f4046b00bda819fac0e3fd16e569a885f88268253f4f49fb934ce87  audit/ops/hde-epic034/ops-02/request_summary.json
128534056106a5e5e6184f5e89ec741a059d701a85de77b264a6db1ce65e4802  audit/ops/hde-epic034/ops-02/result_summary.json
01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b  audit/ops/hde-epic034/ops-02/stderr.log
4fb99caba19981a03fc086760418c21ea515345657575d6420baeaf0dc88365c  audit/ops/hde-epic034/ops-02/stdout.log
```

## Verification Output

Checksum verification:

```text
audit/ops/hde-epic034/ops-02/commands.txt: OK
audit/ops/hde-epic034/ops-02/env_presence_redacted.json: OK
audit/ops/hde-epic034/ops-02/exit_codes.txt: OK
audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py: OK
audit/ops/hde-epic034/ops-02/request_summary.json: OK
audit/ops/hde-epic034/ops-02/result_summary.json: OK
audit/ops/hde-epic034/ops-02/stderr.log: OK
audit/ops/hde-epic034/ops-02/stdout.log: OK
```

Additional verification:

```text
JSON_PARSE_OK
PY_COMPILE_NO_WRITE_OK
CONCRETE_COMMAND_OK
LF_ENDINGS_OK
PLACEHOLDER_SCAN_OK
ACTIVATION_HOOK_SCAN_OK
RAW_ENV_SECRET_SCAN=PASS
RAW_BEARER_SCAN=PASS
```

## Claim Boundaries

Confirmed supported claims:

```text
classification=PASS
vendor_attempted=true
exit_code=0
live_v2_success_claim=true
v2_auth_posture=Authorization: Bearer <redacted>
legacy_hd_api_key_used_for_v2=false
geocode_used=false
raw_secret_persisted=false
full_vendor_payload_persisted=false
```

Explicit non-claims:

```text
full_v2_conformance_claim=false
hde_ferm008_parent_completion_claim=false
hde_ferm008_3_4_5_completion_claim=false
public_reader_change_claim=false
ai_scope_claim=false
vendor_payload_persistence_claim=false
vendor_rerun_by_remediation=false
```

## Workspace State

Current remediated OPS-02 changes:

```text
 M .venv/bin/activate
 M audit/ops/hde-epic034/ops-02/commands.txt
 M audit/ops/hde-epic034/ops-02/files_sha256.txt
 M audit/ops/hde-epic034/ops-02/ops02_full_action_report.md
?? audit/ops/hde-epic034/ops-02/ops02_full_action_log_and_evidence_output.md
?? audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
```

Unrelated pre-existing local change preserved:

```text
 M .devcontainer/scripts/codespaces-extension-doctor.sh
```

