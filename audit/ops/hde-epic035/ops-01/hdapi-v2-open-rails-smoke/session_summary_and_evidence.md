# HDE-EPIC035 OPS-01 Session Summary And Evidence

## Scope

This file consolidates the Codex session evidence for HDE-EPIC035 OPS-01. It records the bounded open-rails HumanDesignAPI checks performed during the session, the correction from the earlier `bg:resolve` drift, and the final observed state.

No raw secrets, bearer tokens, API keys, geocode keys, raw request bodies, raw response bodies, raw vendor payload bodies, production PII, or private payload bodies are recorded here.

No PF-canon files, Human Evidence Index, Machine Mirror, hash sentinels, path proofs, acceptance maps, or PF09 status were updated in this session.

## Repo Preflight

Initial repo preflight:

```text
pwd=/workspaces/glow-hdengine-v2
git_root=/workspaces/glow-hdengine-v2
branch=main
HEAD=7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d
initial_git_status_short=<empty>
```

## Confirmed Configuration

The active configured vendor base URL was confirmed from `HD_API_BASE_URL` only:

```text
HD_API_BASE_URL=https://api.humandesignapi.nl/v2/
```

Presence-only config posture observed in the operator shell:

```text
HD_API_BASE_URL=present_redacted
HD_API_KEY=present_redacted
GEO_API_KEY=present_redacted
SAFE_MODE=present_redacted
ALLOW_NETWORK=present_redacted
LC_ALL=present_redacted
LANG=present_redacted
TZ=present_redacted
```

## Production Target Inputs

```text
production_app_system_entrypoint_label=production_hd_engine_railway_service
production_app_system_url=https://glow-hdengine-v2-production.up.railway.app
scope_note=HD Engine production service, not Glow app product UI
po_approved_test_record_label=qa-user
pii_posture=no_pii_synthetic_test_record
sanitized_input=user=qa-user; birthdate=1990-01-01; birthtime=12:00; location=Paris, FR
```

## Initial Incorrect Path

The first live command used `hdctl bg:resolve`:

```bash
SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate 1990-01-01 --birthtime 12:00 --location "Paris, FR" --dry-run
```

It failed with:

```json
{"error":{"code":"PROVIDER_NOT_FOUND","details":{"status":404},"message":"vendor_error"},"resolver":{"allow_network":true,"dry_run":true,"requested_source":"vendor","resolved_source":"vendor","safe_mode":false,"upsert":false,"user_id":"qa-user"},"status":"error"}
```

The important request-shape finding was:

```text
url_path_suffix=/v2/bodygraphs
route=vendor.hdapi.post:/bodygraphs
has_authorization=False
has_hd_geocode_key=True
has_hd_api_key=True
```

Interpretation: `bg:resolve` is still wired to the legacy BodyGraph resource/header posture. With the configured v2 base, it builds `/v2/bodygraphs`, uses `HD-Api-Key`, includes `HD-Geocode-Key`, and does not use `Authorization: Bearer`.

## Artificial No-Version Rerun

A no-version rerun was attempted during diagnosis:

```bash
HD_API_BASE_URL=https://api.humandesignapi.nl SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate 1990-01-01 --birthtime 12:00 --location "Paris, FR" --dry-run
```

It also failed with:

```text
exit_code=1
status=error
error_code=PROVIDER_NOT_FOUND
http_status=404
```

Its request shape was:

```text
url_path_suffix=/bodygraphs
route=vendor.hdapi.post:/bodygraphs
has_HD_Api_Key=True
has_HD_Geocode_Key=True
has_Authorization=False
```

This rerun is diagnostic only. It does not represent the configured production posture because `HD_API_BASE_URL` is supposed to include the v2 base value.

## Correct V2 Provider Check

After confirming `HD_API_BASE_URL=https://api.humandesignapi.nl/v2/`, the correct v2 geocode-required chart path was checked with the repo `HdApiClient` using `charts/simple`.

Secret-safe observed summary:

```text
configured_base_url_key=HD_API_BASE_URL
url_path_suffix=/v2/charts/simple
route=vendor.hdapi.post:/charts/simple
has_authorization=True
has_hd_geocode_key=True
has_hd_api_key=False
provider_responding=yes
classification=success
attempts=1
response_success=True
response_type=ChartSimpleResult
response_keys=data,errorCode,message,success,timestamp,type
```

Interpretation: the provider is responding successfully on the correct v2 geocode-required chart route. The v2 path uses `Authorization: Bearer <redacted>` and `HD-Geocode-Key: <redacted>`, and it does not use legacy `HD-Api-Key`.

## Final bg:resolve Recheck

After the successful v2 provider check, `bg:resolve` was run again with the configured `HD_API_BASE_URL` unchanged:

```bash
SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate 1990-01-01 --birthtime 12:00 --location "Paris, FR" --dry-run
```

It still failed:

```text
exit_code=1
status=error
error_code=PROVIDER_NOT_FOUND
http_status=404
```

Emitted safe JSON:

```json
{"error":{"code":"PROVIDER_NOT_FOUND","details":{"status":404},"message":"vendor_error"},"resolver":{"allow_network":true,"dry_run":true,"requested_source":"vendor","resolved_source":"vendor","safe_mode":false,"upsert":false,"user_id":"qa-user"},"status":"error"}
```

Final request-shape proof:

```text
url_path_suffix=/v2/bodygraphs
route=vendor.hdapi.post:/bodygraphs
has_authorization=False
has_hd_geocode_key=True
has_hd_api_key=True
```

## Central Finding

The provider is up and responding on the correct v2 chart/geocode route.

`bg:resolve` is the failing path. It still constructs the legacy BodyGraph route against the v2 configured base:

```text
/v2/bodygraphs
```

and uses legacy auth posture:

```text
HD-Api-Key present
Authorization absent
HD-Geocode-Key present
```

The `bg:resolve` failure is therefore not evidence that the provider is unavailable. It is evidence that `bg:resolve` is not using the current v2 chart/geocode request-shaping path.

## Retry Log Evidence

`hdctl bg:resolve` appended keys-only retry observations to `artifacts/ingest/retry_trace.log`.

Relevant records observed:

```json
{"at":"2026-06-28T12:33:06Z","attempt":1,"backoff_ms":0,"duration_ms":637.724,"error_class":"4xx","error_code":"PROVIDER_NOT_FOUND","outcome":"failure","profile":"exponential","rails_state":"open_exception","route":"vendor.hdapi.post:/bodygraphs","status":404,"timeout_profile":"connect=2000;read=5000;total=10000"}
{"at":"2026-06-28T12:37:43Z","attempt":1,"backoff_ms":0,"duration_ms":338.255,"error_class":"4xx","error_code":"PROVIDER_NOT_FOUND","outcome":"failure","profile":"exponential","rails_state":"open_exception","route":"vendor.hdapi.post:/bodygraphs","status":404,"timeout_profile":"connect=2000;read=5000;total=10000"}
{"at":"2026-06-28T12:45:19Z","attempt":1,"backoff_ms":0,"duration_ms":328.677,"error_class":"4xx","error_code":"PROVIDER_NOT_FOUND","outcome":"failure","profile":"exponential","rails_state":"open_exception","route":"vendor.hdapi.post:/bodygraphs","status":404,"timeout_profile":"connect=2000;read=5000;total=10000"}
```

## Evidence Files Touched Or Created

Evidence root:

```text
audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/
```

Files present:

```text
commands.txt
exit_codes.txt
redacted_env_presence.json
request_summary.txt
result_summary.md
session_summary_and_evidence.md
stderr.log
stdout.log
vendor_bodygraph_dry_run.json
vendor_bodygraph_dry_run.stderr
vendor_bodygraph_dry_run_no_version.json
vendor_bodygraph_dry_run_no_version.stderr
```

Additional side-effect file:

```text
artifacts/ingest/retry_trace.log
```

## Final Classification

```text
provider_v2_chart_simple=success
bg_resolve=vendor_error_class_observed
bg_resolve_error_code=PROVIDER_NOT_FOUND
bg_resolve_http_status=404
root_cause_summary=bg:resolve still uses legacy BodyGraph route/header posture against the configured v2 base
```

## Nonclaims

- no QA PASS
- no PF09 status movement
- no epic closeout
- no full HumanDesignAPI v2 runtime conformance
- no public Reader change
- no new public route
- no app-side vendor credential ownership
- no raw payload persistence
- no AI scope
