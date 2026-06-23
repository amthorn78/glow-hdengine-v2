# HDE-EPIC034 OPS-02 Full Action Report and Evidence Output

generated_at_utc: 2026-06-23T22:00:05Z

## Scope

This report records the actions taken in this session for HDE-EPIC034 OPS-02, the PO-authorized open-rails HumanDesignAPI v2 smoke for PF09.5 HDE-FERM008.2.

The run was bounded to one HumanDesignAPI-only v2 chart smoke using the version-neutral resource path `charts/coordinates` under `HD_API_BASE_URL`. The coordinate route was selected because it is a governed v2 chart route and does not require geocoding.

This report does not claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, HDE-FERM008.3/.4/.5 completion, public Reader change, AI scope, or vendor payload persistence.

## Action Log

1. Read the provided OPS-02 context and repo-local PF/repo evidence requirements.
2. Inspected current repo state, PF09.5/PF05 constraints, EPIC034 implementation plan, OPS-01 facts, and PR-05 closed-rails evidence.
3. Verified current repo head: `main` at `1c20dc7847bd2eebd4bf26d1cf4281de5f5480b7`.
4. Confirmed PR-05 closed-rails prerequisite evidence existed and passed.
5. Treated Codex as PO tooling per user instruction and kept OPS-02 evidence secret-safe.
6. Diagnosed that the shell initially did not see `HD_API_KEY`.
7. Found Codespaces shared env files at `/workspaces/.codespaces/shared/`.
8. Added a venv activation bridge so `.venv/bin/activate` sources `.venv/bin/glow-codespaces-env`.
9. The env bridge imports valid entries from `/workspaces/.codespaces/shared/.env` and optionally `.venv/.glow-ops02.env`.
10. Verified the first Codespaces shared manifest had `HD_API_BASE_URL` and `GEO_API_KEY`, but not `HD_API_KEY`.
11. Ran an initial OPS-02 wrapper, which correctly classified `TOOLING_BLOCKED` and did not attempt a vendor call.
12. After the user added the missing Codespaces secret, re-sourced the venv and verified `HD_API_KEY=SET` by presence only.
13. Ran the bounded live HumanDesignAPI v2 smoke against `charts/coordinates`.
14. Captured only redacted environment posture, request metadata, response shape metadata, exit code, result summary, and checksums.
15. Verified checksum integrity, secret-safety scan, raw Bearer scan, and LF endings.

## Environment Persistence

`.venv/bin/activate` now includes:

```sh
# Glow HD Engine local Codespaces/OPS env bridge.
if [ -f "$VIRTUAL_ENV/bin/glow-codespaces-env" ] ; then
    . "$VIRTUAL_ENV/bin/glow-codespaces-env"
fi
```

The helper is secret-free and persists the Codespaces env bridge for future venv activations.

Final redacted activation probe:

```text
APP_ENV=dev
SAFE_MODE=0
ALLOW_NETWORK=1
HD_API_BASE_URL=SET
HDAPI_BASE_URL=UNSET
HD_API_KEY=SET
GEO_API_KEY=SET
LC_ALL=C
LANG=C
TZ=UTC
```

## Final Outcome

```text
OPS02_CLASSIFICATION=PASS
OPS02_EXIT_CODE=0
OPS02_VENDOR_ATTEMPTED=true
```

## Evidence Files

Primary OPS-02 evidence root:

```text
audit/ops/hde-epic034/ops-02/
```

Files produced:

```text
audit/ops/hde-epic034/ops-02/commands.txt
audit/ops/hde-epic034/ops-02/env_presence_redacted.json
audit/ops/hde-epic034/ops-02/exit_codes.txt
audit/ops/hde-epic034/ops-02/files_sha256.txt
audit/ops/hde-epic034/ops-02/request_summary.json
audit/ops/hde-epic034/ops-02/result_summary.json
audit/ops/hde-epic034/ops-02/stderr.log
audit/ops/hde-epic034/ops-02/stdout.log
```

## Evidence Output

### commands.txt

```text
# OPS-02 command transcript
work_item=HDE-EPIC034 OPS-02
operator_surface=Codex acting as PO tooling per user authorization
execution_class=bounded open-rails HumanDesignAPI v2 smoke wrapper
route_resource_path=charts/coordinates
method=POST
rails=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
base_url_env=HD_API_BASE_URL
credential_env=HD_API_KEY
geocode_env=GEO_API_KEY not required for charts/coordinates
auth_header_shape=Authorization: Bearer <redacted>
no_legacy_v2_auth_header=HD-Api-Key not used for v2 chart routes
command=. .venv/bin/activate && python <ops02_wrapper>
secret_policy=no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, uncontrolled production data, or full vendor payload bodies are persisted
```

### env_presence_redacted.json

```json
{"ALLOW_NETWORK":"1","APP_ENV":"dev","GEO_API_KEY":"SET","HDAPI_BASE_URL":"UNSET","HD_API_BASE_URL":"SET","HD_API_BASE_URL_expected_v2":true,"HD_API_KEY":"SET","LANG":"C","LC_ALL":"C","SAFE_MODE":"0","TZ":"UTC"}
```

### request_summary.json

```json
{"auth_header_posture":"Authorization: Bearer <redacted>","authorization_header_shape":"Authorization: Bearer <redacted>","body_sha256":"cb0005717a709aaeb3f4a652bafc33450f5e853d95fd60de034b2f805e49b0ff","configured_base_url_key":"HD_API_BASE_URL","endpoint_path_posture":"/v2/charts/coordinates via HD_API_BASE_URL plus version-neutral resource path","epic_id":"HDE-EPIC034","generated_at_utc":"2026-06-23T22:00:01Z","geocode_key_requirement":"not needed","hd_api_key_header_present":false,"hd_geocode_key_header_present":false,"header_names":["Accept","Authorization","Content-Type","User-Agent"],"input_fingerprint":"cb0005717a709aaeb3f4a652bafc33450f5e853d95fd60de034b2f805e49b0ff","input_tuple_posture":"synthetic non-PII coordinates tuple; full request body not persisted","legacy_v2_auth_header_posture":"HD-Api-Key not used for v2 chart routes","method":"POST","ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","rails_required":{"ALLOW_NETWORK":"1","SAFE_MODE":"0"},"request_fields":["birthdate","birthtime","lat","lng"],"request_url_posture":"redacted base URL; version-neutral resource path joined by HdApiClient","resource_path":"charts/coordinates"}
```

### stdout.log

```json
{"attempts":1,"duration_ms_rounded":4088.122,"response_shape":{"data_kind":"dict","errorCode_present":true,"success":true,"top_level_keys":["data","errorCode","message","success","timestamp","type"],"type":"ChartResult"},"status":"PASS","vendor_attempted":true}
```

### stderr.log

```text

```

### exit_codes.txt

```text
ops02_wrapper=0
```

### result_summary.json

```json
{"classification":"PASS","epic_id":"HDE-EPIC034","exit_code":0,"follow_up":"bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance","full_v2_conformance_claim":false,"full_vendor_payload_persisted":false,"generated_at_utc":"2026-06-23T22:00:05Z","geocode_used":false,"hde_ferm008_3_4_5_completion_claim":false,"hde_ferm008_parent_completion_claim":false,"http_status_present":false,"legacy_hd_api_key_used_for_v2":false,"live_v2_success_claim":true,"ops_task":"OPS-02","pf09_subtask_id":"HDE-FERM008.2","raw_secret_persisted":false,"v2_auth_posture":"Authorization: Bearer <redacted>","vendor_attempted":true}
```

### files_sha256.txt

```text
3e35bb55441ea6b79c3de38c74f3e86018c25e82d31a0b77872076267cb2acbd  audit/ops/hde-epic034/ops-02/commands.txt
566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5  audit/ops/hde-epic034/ops-02/env_presence_redacted.json
354a244d8b29b8086dcaa4b6a48457b06dd6b77ed375ed56bfdf2c077c52e22c  audit/ops/hde-epic034/ops-02/exit_codes.txt
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
audit/ops/hde-epic034/ops-02/request_summary.json: OK
audit/ops/hde-epic034/ops-02/result_summary.json: OK
audit/ops/hde-epic034/ops-02/stderr.log: OK
audit/ops/hde-epic034/ops-02/stdout.log: OK
```

Secret and Bearer scans:

```text
RAW_ENV_SECRET_SCAN=PASS
RAW_BEARER_SCAN=PASS
```

LF ending check:

```text
LF_ENDINGS=PASS
```

## Safety and Claim Boundaries

Confirmed:

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
```

Follow-up recorded in OPS evidence:

```text
bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance
```

## Workspace State After Session

```text
 M .venv/bin/activate
?? audit/ops/hde-epic034/ops-02/
```

Branch and commit:

```text
branch=main
head=1c20dc7847bd2eebd4bf26d1cf4281de5f5480b7
```
