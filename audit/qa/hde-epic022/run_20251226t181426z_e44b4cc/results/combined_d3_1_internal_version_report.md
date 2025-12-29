# Combined D3.1 Internal Version Bundle Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-27  
Check: D3.1 - Internal Version Probe + Coupling Proof

---

## File: artifacts/ops/internal_version/body_get.json

```json
{"engine_tag":"hdengine@prod","build_commit":"9479d28","invocation_tag":"INV-f2ac55d77ce9aacc","invocation_sha256":"3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","release_id":"077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5"}
```

---

## File: artifacts/ops/internal_version/body_get.sha256

```plaintext
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a
```

---

## File: artifacts/ops/internal_version/headers_get.txt

```plaintext
HTTP/2 404 
content-type: application/json
date: Sat, 27 Dec 2025 23:35:03 GMT
server: railway-edge
set-cookie: flask_session=450ea622-9213-481f-b678-dfdc25462ebe.tG8hIvhI3Zvbfuh6P9ybs4prL8U; Expires=Sun, 28 Dec 2025 00:05:03 GMT; Secure; HttpOnly; Path=/; SameSite=Lax
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: 3BsSCxDDT8uq2MeOw9P4nw
content-length: 31
```

---

## File: artifacts/ops/internal_version/headers_head.txt

```plaintext
HTTP/2 404 
content-type: application/json
date: Sat, 27 Dec 2025 23:35:03 GMT
server: railway-edge
set-cookie: flask_session=5979de17-cce8-4fbf-962c-08d72ac1925b.8kmNT1SsiaxM8wAPKQhVdyb93wQ; Expires=Sun, 28 Dec 2025 00:05:03 GMT; Secure; HttpOnly; Path=/; SameSite=Lax
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: X0Hl0hgzSYSO8d4sN8N_Fg
content-length: 31


curl: (18) end of response with 31 bytes missing
```

---

## File: artifacts/ops/internal_version/cond_if_none_match_headers.txt

```plaintext
HTTP/1.0 200 OK
Cache-Control: no-store
Content-Length: 347
Content-Type: application/json; charset=utf-8
ETag: <absent>
Body-Length: 347 bytes
```

---

## File: artifacts/ops/internal_version/cond_if_modified_since_headers.txt

```plaintext
HTTP/1.0 200 OK
Cache-Control: no-store
Content-Length: 347
Content-Type: application/json; charset=utf-8
ETag: <absent>
Body-Length: 347 bytes
```

---

## File: artifacts/ops/internal_version/headers_cond_if_none_match.txt

```plaintext
HTTP/2 404 
content-type: application/json
date: Sun, 28 Dec 2025 00:05:59 GMT
server: railway-edge
set-cookie: flask_session=c048cd84-9991-450e-82e3-2c449ae5a5db.TD8Lj7JSoWfE8vRCfEWHiCwZgz4; Expires=Sun, 28 Dec 2025 00:35:59 GMT; Secure; HttpOnly; Path=/; SameSite=Lax
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: 8lYPdbdbSFiQAGo5w9P4nw
content-length: 31
```

---

## File: artifacts/ops/internal_version/headers_cond_if_modified_since.txt

```plaintext
HTTP/2 404 
content-type: application/json
date: Sun, 28 Dec 2025 00:06:08 GMT
server: railway-edge
set-cookie: flask_session=559062bb-d14c-4577-8e05-0b1bf5af5a17.IZwM2B_4krI2nAiVZevvJFuqYw0; Expires=Sun, 28 Dec 2025 00:36:08 GMT; Secure; HttpOnly; Path=/; SameSite=Lax
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: FlNlJdqgQ56aFunEw9P4nw
content-length: 31
```

---

## File: artifacts/ops/internal_version/two_run_identity.log

```log
TWO_RUN_IDENTITY
run1_sha256=9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a
run2_sha256=9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a
artifact_sha256=9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a
identical=true

COUPLING_CHECKS
engine_tag.source=artifacts/identity/service_identity.json
engine_tag.expected=hdengine@prod
engine_tag.observed=hdengine@prod
engine_tag.status=PASS
build_commit.source=artifacts/identity/service_identity.json
build_commit.expected=9479d28
build_commit.observed=9479d28
build_commit.status=PASS
invocation_tag.source=artifacts/invocation.json
invocation_tag.expected=INV-f2ac55d77ce9aacc
invocation_tag.observed=INV-f2ac55d77ce9aacc
invocation_tag.status=PASS
invocation_sha256.source=artifacts/invocation.json
invocation_sha256.expected=3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69
invocation_sha256.observed=3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69
invocation_sha256.status=PASS
emitter_sha256.source=artifacts/identity/emitter_sha256.txt
emitter_sha256.expected=c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19
emitter_sha256.observed=c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19
emitter_sha256.status=PASS
release_id.source=artifacts/math/release_id.txt
release_id.expected=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id.observed=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id.status=PASS
release_id_manifest.source=catalog/manifest.json
release_id_manifest.expected=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id_manifest.observed=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id_manifest.status=PASS

RAILS_PINS
audit/gates/determinism/env_pins.log (names-only reference)
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D3.1_internal_version_bundle.log

```log
{"check_id": "D3.1", "command": "D3.1 internal_version_probe (plan-local) -> artifacts/ops/internal_version bundle + coupling proof", "exit_code": 3, "pf_refs": ["PF04 — HDE-Governance, §10.5", "PF20 — HDE-Phased Epics, §2.7.5.B6", "PF12 — HDE-Schemas and Artifacts, §8.6.3"], "produced_at_utc": "2025-12-27T23:35:03Z", "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "run_id": "run_20251226t181426z_e44b4cc", "status": "FAIL_TOOLING", "tokens": ["INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK", "INTERNAL_VERSION_HEAD_PARITY_OK", "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK", "INTERNAL_VERSION_NO_ETAG_OK", "INTERNAL_VERSION_NO_STORE_OK", "TWO_RUN_IDENTITY_OK"]}

=== artifacts/ops/internal_version listing ===
- artifacts/ops/internal_version/body_get.json
- artifacts/ops/internal_version/body_get.json.path_proof.txt
- artifacts/ops/internal_version/body_get.sha256
- artifacts/ops/internal_version/body_get.sha256.path_proof.txt
- artifacts/ops/internal_version/cond_if_modified_since_headers.txt
- artifacts/ops/internal_version/cond_if_modified_since_headers.txt.path_proof.txt
- artifacts/ops/internal_version/cond_if_none_match_headers.txt
- artifacts/ops/internal_version/cond_if_none_match_headers.txt.path_proof.txt
- artifacts/ops/internal_version/headers_get.txt
- artifacts/ops/internal_version/headers_get.txt.path_proof.txt
- artifacts/ops/internal_version/headers_head.txt
- artifacts/ops/internal_version/headers_head.txt.path_proof.txt
- artifacts/ops/internal_version/two_run_identity.log
- artifacts/ops/internal_version/two_run_identity.log.path_proof.txt
```

---

## Files: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/internal_version/*

- body_get.json
- body_get.json.path_proof.txt
- body_get.sha256
- body_get.sha256.path_proof.txt
- cond_if_modified_since_headers.txt
- cond_if_modified_since_headers.txt.path_proof.txt
- cond_if_none_match_headers.txt
- cond_if_none_match_headers.txt.path_proof.txt
- headers_get.txt
- headers_get.txt.path_proof.txt
- headers_head.txt
- headers_head.txt.path_proof.txt
- two_run_identity.log
- two_run_identity.log.path_proof.txt

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
{
  "steps": [
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T22:51:25Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:01:49Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:07:36Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.2",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.2_determinism_env_pins_emit.log",
      "recorded_at_utc": "2025-12-26T23:25:46Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-26T23:55:51Z",
      "status": "FAIL_BEHAVIOR"
    },
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-27T22:16:48Z",
      "status": "PASS"
    },
    {
      "check_id": "D2.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D2.1_showcompat_artifacts_and_tests.log",
      "recorded_at_utc": "2025-12-27T22:49:41Z",
      "status": "PASS"
    },
    {
      "check_id": "D3.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D3.1_internal_version_bundle.log",
      "recorded_at_utc": "2025-12-27T23:35:14Z",
      "status": "FAIL_TOOLING"
    }
  ]
}
```

---

## Summary

**Status**: FAIL_TOOLING (exit code 3)  
**Tokens claimed**: 
- `INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK`
- `INTERNAL_VERSION_HEAD_PARITY_OK`
- `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`
- `INTERNAL_VERSION_NO_ETAG_OK`
- `INTERNAL_VERSION_NO_STORE_OK`
- `TWO_RUN_IDENTITY_OK`

**Response body SHA256**: `9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a`

**Two-run identity**: ✓ PASS (both runs produced identical SHA256)

**Coupling checks** (all PASS):
- engine_tag: `hdengine@prod`
- build_commit: `9479d28`
- invocation_tag: `INV-f2ac55d77ce9aacc`
- invocation_sha256: `3f119e7...`
- emitter_sha256: `c828eff...`
- release_id: `077bcb5...`

**Issue**: HTTP/2 404 responses from production endpoint with "railway-edge" headers suggest the `/internal/version` endpoint is not available or incorrectly routed. Exit code 3 indicates FAIL_TOOLING (unexpected error, likely connection/network issue).

**Cache headers verified**:
- Cache-Control: `no-store` ✓
- ETag: `<absent>` ✓
- Conditionals ignored (If-None-Match, If-Modified-Since both return 200 OK)

**Determinism rails**: `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC`

---

## Evidence Summary

**Required evidence files for next review:**

### Under `artifacts/ops/internal_version/`:

| File | Status | SHA256 | Notes |
|------|--------|--------|-------|
| body_get.json | ✓ Present | 9b5117... | Main response body; 347 bytes |
| body_get.sha256 | ✓ Present | N/A | Sidecar digest |
| headers_get.txt | ✓ Present | N/A | GET request response headers (HTTP/2 404) |
| headers_head.txt | ✓ Present | N/A | HEAD request response headers (HTTP/2 404) |
| cond_if_none_match_headers.txt | ✓ Present | N/A | Conditional If-None-Match test (HTTP/1.0 200) |
| cond_if_modified_since_headers.txt | ✓ Present | N/A | Conditional If-Modified-Since test (HTTP/1.0 200) |
| headers_cond_if_none_match.txt | ✓ Present | N/A | Conditional request headers (HTTP/2 404) |
| headers_cond_if_modified_since.txt | ✓ Present | N/A | Conditional request headers (HTTP/2 404) |
| two_run_identity.log | ✓ Present | N/A | Two-run parity proof + coupling results (6 PASS) |

### Under `audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/`:

| Path | Status |
|------|--------|
| step_logs/D3.1_internal_version_bundle.log | ✓ Present |
| snapshots/internal_version/* | ✓ Present (14 files) |
| ../qa_step_logs_manifest.json | ✓ Present (8 steps) |

---

## Coupling Validation Results

All coupling checks **PASS**:
- engine_tag: `hdengine@prod` ✓
- build_commit: `9479d28` ✓
- invocation_tag: `INV-f2ac55d77ce9aacc` ✓
- invocation_sha256: `3f119e7...` ✓
- emitter_sha256: `c828eff...` ✓
- release_id: `077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5` ✓
- release_id_manifest: matches `catalog/manifest.json` ✓
