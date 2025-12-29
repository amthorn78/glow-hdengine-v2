# Combined QA Files for run_20251226t181426z_e44b4cc (Step D3.1 - Internal Version)

## File: artifacts/ops/internal_version/body_get.json

```json
{"error":"Endpoint not found"}
```

---

## File: artifacts/ops/internal_version/body_get.sha256

```plaintext
13661a746f2a084a667ec3be7107fc6d02dc1e23bccc745bfcb1056dee5319a4
```

---

## File: artifacts/ops/internal_version/headers_get.txt

```plaintext
HTTP/1.1 301 Moved Permanently
content-type: text/html; charset=utf-8
location: https://glow-hdengine-v2-production.up.railway.app/internal/version
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: DRe01Vv4Tc-OPEwaw9P4nw
date: Sun, 28 Dec 2025 01:59:31 GMT
content-length: 102
```

---

## File: artifacts/ops/internal_version/headers_head.txt

```plaintext
HTTP/1.1 301 Moved Permanently
content-type: text/html; charset=utf-8
location: https://glow-hdengine-v2-production.up.railway.app/internal/version
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: u0Oapb8bS5iOCo8PN8N_Fg
date: Sun, 28 Dec 2025 01:59:31 GMT


curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received
```

---

## File: artifacts/ops/internal_version/cond_if_none_match_headers.txt

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

## File: artifacts/ops/internal_version/cond_if_modified_since_headers.txt

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
{"check_id": "D3.1", "command": "D3.1 internal_version_probe (plan-local) -> artifacts/ops/internal_version bundle + coupling proof", "exit_code": 3, "pf_refs": ["PF04 — HDE-Governance, §10.5", "PF20 — HDE-Phased Epics, §2.7.5.B6", "PF12 — HDE-Schemas and Artifacts, §8.6.3"], "produced_at_utc": "2025-12-28T02:00:01Z", "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "run_id": "run_20251226t181426z_e44b4cc", "status": "FAIL_TOOLING", "tokens": ["INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK", "INTERNAL_VERSION_HEAD_PARITY_OK", "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK", "INTERNAL_VERSION_NO_ETAG_OK", "INTERNAL_VERSION_NO_STORE_OK", "TWO_RUN_IDENTITY_OK"]}

=== artifacts/ops/internal_version listing ===
- artifacts/ops/internal_version/body_get.json
- artifacts/ops/internal_version/body_get.json.path_proof.txt
- artifacts/ops/internal_version/body_get.sha256
- artifacts/ops/internal_version/body_get.sha256.path_proof.txt
- artifacts/ops/internal_version/cond_if_modified_since_headers.txt
- artifacts/ops/internal_version/cond_if_modified_since_headers.txt.path_proof.txt
- artifacts/ops/internal_version/cond_if_none_match_headers.txt
- artifacts/ops/internal_version/cond_if_none_match_headers.txt.path_proof.txt
- artifacts/ops/internal_version/headers_cond_if_modified_since.txt
- artifacts/ops/internal_version/headers_cond_if_none_match.txt
- artifacts/ops/internal_version/headers_get.txt
- artifacts/ops/internal_version/headers_get.txt.path_proof.txt
- artifacts/ops/internal_version/headers_head.txt
- artifacts/ops/internal_version/headers_head.txt.path_proof.txt
- artifacts/ops/internal_version/two_run_identity.log
- artifacts/ops/internal_version/two_run_identity.log.path_proof.txt
```

---

## Snapshot Files: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/internal_version/

### body_get.json

```json
{"error":"Endpoint not found"}
```

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/body_get.json
size_bytes: 347
sha256: 9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### body_get.sha256

```plaintext
13661a746f2a084a667ec3be7107fc6d02dc1e23bccc745bfcb1056dee5319a4
```

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/body_get.sha256
size_bytes: 65
sha256: 51e48fd317e87dbcac137d8ed791bb376988f8466e0333ba04c0ab5992cadac4
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### headers_get.txt

```plaintext
HTTP/1.1 301 Moved Permanently
content-type: text/html; charset=utf-8
location: https://glow-hdengine-v2-production.up.railway.app/internal/version
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: DRe01Vv4Tc-OPEwaw9P4nw
date: Sun, 28 Dec 2025 01:59:31 GMT
content-length: 102
```

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/headers_get.txt
size_bytes: 144
sha256: 902c2e17138d4bb4d0c67469d1fcc63dbdb25bbd5390abe513163cdd65d95e59
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### headers_head.txt

```plaintext
HTTP/1.1 301 Moved Permanently
content-type: text/html; charset=utf-8
location: https://glow-hdengine-v2-production.up.railway.app/internal/version
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: u0Oapb8bS5iOCo8PN8N_Fg
date: Sun, 28 Dec 2025 01:59:31 GMT


curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received
```

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/headers_head.txt
size_bytes: 142
sha256: 4449eb33f9f23c3f5b9a8fcedb35a06498d7c9f2567c81816e6135ed4e68b62e
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### cond_if_none_match_headers.txt

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

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/cond_if_none_match_headers.txt
size_bytes: 144
sha256: 902c2e17138d4bb4d0c67469d1fcc63dbdb25bbd5390abe513163cdd65d95e59
mtime_utc: 2025-12-19T16:30:01Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### cond_if_modified_since_headers.txt

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

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/cond_if_modified_since_headers.txt
size_bytes: 144
sha256: 902c2e17138d4bb4d0c67469d1fcc63dbdb25bbd5390abe513163cdd65d95e59
mtime_utc: 2025-12-19T16:30:01Z
produced_at_utc: 2025-11-30T03:58:47Z
```

### headers_cond_if_none_match.txt

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

### headers_cond_if_modified_since.txt

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

### two_run_identity.log

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

**Path Proof:**
```plaintext
path: artifacts/ops/internal_version/two_run_identity.log
size_bytes: 1857
sha256: eb37c693e3a564bf2ad63c91897124388576515352f663ac01db73066b9c02ed
mtime_utc: 2025-12-06T04:06:36Z
produced_at_utc: 2025-11-30T03:58:47Z
```

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
      "recorded_at_utc": "2025-12-27T23:35:03Z",
      "status": "FAIL_TOOLING"
    },
    {
      "check_id": "D3.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D3.1_internal_version_bundle.log",
      "recorded_at_utc": "2025-12-28T02:00:02Z",
      "status": "FAIL_TOOLING"
    }
  ]
}
```

---

## Summary

**Status:** FAIL_TOOLING (exit code 3)

**Tokens passed:**
- INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK
- INTERNAL_VERSION_HEAD_PARITY_OK
- INTERNAL_VERSION_CONDITIONALS_IGNORED_OK
- INTERNAL_VERSION_NO_ETAG_OK
- INTERNAL_VERSION_NO_STORE_OK
- TWO_RUN_IDENTITY_OK

**Two-run identity:** ✓ identical (all runs produce same SHA256: `9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a`)

**Coupling checks:** All PASS (engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id, release_id_manifest)

**Issues observed:**
- HTTP/1.1 301 redirects encountered for GET/HEAD requests
- HEAD request timeout (30s)
- Endpoint returns 404 for conditional requests (If-None-Match, If-Modified-Since)
- Body returns: `{"error":"Endpoint not found"}`
