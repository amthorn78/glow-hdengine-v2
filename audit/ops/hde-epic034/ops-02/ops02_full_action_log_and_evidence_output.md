# HDE-EPIC034 OPS-02 Full Action Log and Evidence Output

generated_at_utc: `2026-06-24T06:28:13Z`

repo_root: `/workspaces/glow-hdengine-v2`

branch: `main`

current_head: `20c96073dfbcb6f25a9c1f3cb38267dde7472dec`

primary_evidence_root: `audit/ops/hde-epic034/ops-02/`

## Final Classification

```text
OPS02_CLASSIFICATION=PASS
COMMAND_TO_OUTPUT_PROVENANCE=PASS
VENDOR_RERUN_BY_MOON_LOOP=true
OPS02_EXIT_CODE=0
OPS02_VENDOR_ATTEMPTED=true
OPS02_LIVE_V2_SUCCESS_SHAPE=true
```

This packet is the current OPS-02 evidence output for the HDE-EPIC034 PR-06 open-rails HumanDesignAPI v2 smoke supporting the narrow PF09.5 HDE-FERM008.2 vendor-POST slice.

The prior blocker was provenance-only: the evidence had a PASS-shaped vendor result, but the exact PASS-producing command was not bound to the current output. The Moon Loop remediation executed the repo-resident smoke procedure as PO tooling under the user's authorization and replaced the historical/provenance-blocked state with a concrete command-to-output chain.

## Directory Cleanup

Removed stale or redundant standalone reports from `audit/ops/hde-epic034/ops-02/` after folding their useful content into this single current packet:

```text
audit/ops/hde-epic034/ops-02/ops02_full_action_report.md
audit/ops/hde-epic034/ops-02/ops02_moon_loop_action_log_and_evidence_output.md
audit/ops/hde-epic034/ops-02/revalidation_report.txt
```

Retained files are either primary evidence, checksum coverage, the repo-resident smoke procedure, the rerun transcript, or this active full output.

## Scope

OPS-02 is bounded to one HumanDesignAPI-only v2 chart smoke using the version-neutral resource path `charts/coordinates` under `HD_API_BASE_URL`. The coordinate route does not require geocoding.

This packet does not claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, HDE-FERM008.3/.4/.5 completion, public Reader change, AI scope, raw vendor payload persistence, or any public contract change.

## Action Log

1. Read the OPS-02 remediation record and repo-local evidence requirements.
2. Identified that the placeholder command and missing activation-helper claims had already been remediated, but current PASS acceptance was still blocked by command-to-output provenance.
3. Confirmed the user instruction authorizing Codex to act as PO tooling for the rerun: "you are acting as PO here so the rerun is your task".
4. Verified open-rails environment presence using redacted values only: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, `HD_API_BASE_URL=SET`, `HD_API_KEY=SET`, `GEO_API_KEY=SET`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
5. Executed the repo-resident procedure at `audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py`.
6. Captured the actual stdout, stderr, exit code, redacted environment posture, request summary, result summary, and rerun transcript.
7. Reclassified OPS-02 from `TOOLING_BLOCKED` to `PASS` because the current PASS output is now produced by a concrete, recorded command.
8. Removed stale standalone reports from the OPS-02 directory and kept this file as the distinct current action log and evidence output.
9. Refreshed the checksum ledger for retained primary evidence files.
10. Re-ran integrity, syntax, parser, LF-ending, stale-placeholder, activation-hook, and secret-pattern scans.

## Exact PASS-Producing Command

```bash
SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
```

## Observed Runtime Result

Exit code:

```text
0
```

stdout:

```json
{"attempts":1,"duration_ms_rounded":2008.51,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
```

stderr:

```text
empty
```

## Retained Evidence Files

```text
audit/ops/hde-epic034/ops-02/commands.txt
audit/ops/hde-epic034/ops-02/env_presence_redacted.json
audit/ops/hde-epic034/ops-02/exit_codes.txt
audit/ops/hde-epic034/ops-02/files_sha256.txt
audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt
audit/ops/hde-epic034/ops-02/ops02_full_action_log_and_evidence_output.md
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

## Rerun Transcript

```text
HDE-EPIC034 OPS-02 MOON LOOP RERUN TRANSCRIPT
started_at_utc=2026-06-24T06:28:13Z
completed_at_utc=2026-06-24T06:28:13Z
operator_surface=Codex acting as PO tooling per user authorization
command=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
exit_code=0
stdout={"attempts":1,"duration_ms_rounded":2008.51,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
stderr=
secret_policy=no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, uncontrolled production data, or full vendor payload bodies persisted
```

## Redacted Environment Evidence

```json
{"ALLOW_NETWORK":"1","APP_ENV":"dev","GEO_API_KEY":"SET","HDAPI_BASE_URL":"UNSET","HD_API_BASE_URL":"SET","HD_API_BASE_URL_expected_v2":true,"HD_API_KEY":"SET","LANG":"C","LC_ALL":"C","SAFE_MODE":"0","TZ":"UTC"}
```

## Request Summary Evidence

```json
{"auth_header_posture":"Authorization: Bearer <redacted>","authorization_header_shape":"Authorization: Bearer <redacted>","body_sha256":"19fd61d354638d44a479dc68de92a62440d94dfc92d17c0e5c19c684621d1db0","command_to_output_provenance":"PASS","configured_base_url_key":"HD_API_BASE_URL","endpoint_path_posture":"/v2/charts/coordinates via HD_API_BASE_URL plus version-neutral resource path","epic_id":"HDE-EPIC034","generated_at_utc":"2026-06-24T06:28:13Z","geocode_key_requirement":"not needed","hd_api_key_header_present":false,"hd_geocode_key_header_present":false,"header_names":["Accept","Authorization","Content-Type","User-Agent"],"input_fingerprint":"19fd61d354638d44a479dc68de92a62440d94dfc92d17c0e5c19c684621d1db0","input_tuple_posture":"synthetic non-PII coordinates tuple; full request body not persisted","legacy_v2_auth_header_posture":"HD-Api-Key not used for v2 chart routes","method":"POST","ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","rails_required":{"ALLOW_NETWORK":"1","SAFE_MODE":"0"},"request_fields":["birthdate","birthtime","lat","lng"],"request_url_posture":"redacted base URL; version-neutral resource path joined by HdApiClient","resource_path":"charts/coordinates","vendor_rerun_by_moon_loop":true}
```

## Stdout Evidence

```json
{"attempts":1,"duration_ms_rounded":2008.51,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
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
{"classification":"PASS","command_to_output_provenance":"PASS","epic_id":"HDE-EPIC034","exit_code":0,"follow_up":"bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance or HDE-FERM008 parent completion","full_v2_conformance_claim":false,"full_vendor_payload_persisted":false,"generated_at_utc":"2026-06-24T06:28:13Z","geocode_used":false,"hde_ferm008_2_ops02_evidence_ready":true,"hde_ferm008_3_4_5_completion_claim":false,"hde_ferm008_parent_completion_claim":false,"http_status_present":false,"legacy_hd_api_key_used_for_v2":false,"live_v2_success_claim":true,"ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","raw_secret_persisted":false,"v2_auth_posture":"Authorization: Bearer <redacted>","vendor_attempted":true,"vendor_rerun_by_moon_loop":true}
```

## Checksum Evidence

`files_sha256.txt` covers retained primary evidence files and intentionally excludes this narrative report and the checksum file itself to avoid self-reference.

```text
50b6b3ee7d8dfecb0a0155be9ed210008526165221710629cc0fa48c625ce739  audit/ops/hde-epic034/ops-02/commands.txt
566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5  audit/ops/hde-epic034/ops-02/env_presence_redacted.json
354a244d8b29b8086dcaa4b6a48457b06dd6b77ed375ed56bfdf2c077c52e22c  audit/ops/hde-epic034/ops-02/exit_codes.txt
0dd29a95519e069eb6beeff275fe58ac48c78830e7964b055fcd4200572e613a  audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt
407e1059596cdba51eed4b7f335ef28218f56a80df16148e19c0b7d95c5b4fca  audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py
8bdf35464322008b5a3c3368eeab6c4ae9eb6ea1b0d23c489b949cb92035be65  audit/ops/hde-epic034/ops-02/request_summary.json
a1f3b1d7bc0130bb02d6ac78999f3da8f4178d1c67c8f1903f66904211abaeb3  audit/ops/hde-epic034/ops-02/result_summary.json
01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b  audit/ops/hde-epic034/ops-02/stderr.log
c852d3a83ae19f1aec00a71196b76b5408bd26816e4901522aaf028617b18a25  audit/ops/hde-epic034/ops-02/stdout.log
```

## Verification Output

Checksum verification:

```text
audit/ops/hde-epic034/ops-02/commands.txt: OK
audit/ops/hde-epic034/ops-02/env_presence_redacted.json: OK
audit/ops/hde-epic034/ops-02/exit_codes.txt: OK
audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt: OK
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
LF_ENDINGS_OK
PLACEHOLDER_SCAN_OK
ACTIVATION_HOOK_SCAN_OK
RAW_ENV_SECRET_SCAN=PASS
RAW_BEARER_SCAN=PASS
STALE_REPORTS_REMOVED=PASS
```

## Claim Boundaries

Supported narrow claims:

```text
classification=PASS
command_to_output_provenance=PASS
vendor_rerun_by_moon_loop=true
vendor_attempted=true
exit_code=0
live_v2_success_claim=true
v2_auth_posture=Authorization: Bearer <redacted>
legacy_hd_api_key_used_for_v2=false
geocode_used=false
raw_secret_persisted=false
full_vendor_payload_persisted=false
```

Explicit nonclaims:

```text
full_v2_conformance_claim=false
hde_ferm008_parent_completion_claim=false
hde_ferm008_3_4_5_completion_claim=false
public_reader_change_claim=false
ai_scope_claim=false
vendor_payload_persistence_claim=false
raw_request_payload_persistence_claim=false
raw_response_payload_persistence_claim=false
```

## PR-06 Binding Posture

OPS-02 is ready to bind as PR-06 evidence for the narrow open-rails HDE-FERM008.2 vendor-POST smoke. Broader runtime conformance, public Reader changes, and HDE-FERM008 parent completion remain out of scope until separately proven by governed evidence.
