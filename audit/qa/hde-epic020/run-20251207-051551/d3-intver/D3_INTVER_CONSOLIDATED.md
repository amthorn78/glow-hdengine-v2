# EPIC020 D3 — Internal Version QA Consolidated Artifacts

**Run timestamp:** 2025-12-07T05:39:46Z

**Source directory:** `/audit/qa/hde-epic020/run-20251207-051551/d3-intver/`

---

## Summary

Internal version endpoint (`/internal/version`) QA under closed rails (SAFE_MODE=1, ALLOW_NETWORK=0).

| Check | Status |
|-------|--------|
| HTTP 200 response | ✓ OK |
| Content-Type application/json | ✓ OK |
| Two-run identity (GET1 vs GET2) | ✓ OK |
| HEAD request parity | ✓ OK |

---

## File: internal_version_get1.headers

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:03 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close
```

---

## File: internal_version_get1.body

```json
{"engine_tag":"hdengine@prod","build_commit":"9479d28","invocation_tag":"INV-f2ac55d77ce9aacc","invocation_sha256":"3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","release_id":"6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925"}
```

---

## File: internal_version_get1.curl.stderr

(Empty — no errors)

---

## File: internal_version_get2.headers

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:12 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close
```

---

## File: internal_version_get2.body

```json
{"engine_tag":"hdengine@prod","build_commit":"9479d28","invocation_tag":"INV-f2ac55d77ce9aacc","invocation_sha256":"3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","release_id":"6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925"}
```

---

## File: internal_version_get2.curl.stderr

(Empty — no errors)

---

## File: internal_version_head.headers

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:46 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close
```

---

## File: internal_version_head.curl.stderr

(Empty — no errors)

---

## File: step4_internal_version.log

```
check_id=EPIC020_D3_INTERNAL_VERSION
command=curl GET/HEAD http://127.0.0.1:8000/internal/version (two GETs + one HEAD)
rails=APP_ENV=dev;LC_ALL=C;LANG=C;TZ=UTC;SAFE_MODE=1;ALLOW_NETWORK=0
pf_refs=PF20 EPIC020 D3;PF14 internal ops;PF09 internal checklist;PF10 EPIC020 D3 addenda;PF19 §4.4
tokens=INTVER_200_CTYPE_JSON_UTF8_OK,INTVER_HEAD_PARITY_OK
status=PENDING

--- internal_version_get1.headers ---
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:03 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close


--- internal_version_get2.headers ---
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:12 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close


--- internal_version_head.headers ---
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Sun, 07 Dec 2025 05:39:46 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 347
Cache-Control: no-store
Connection: close
```

---

## Analysis

### Two-Run Identity (GET1 vs GET2)

Both requests returned identical JSON bodies:
- Same `engine_tag`, `build_commit`, `invocation_tag`
- Identical `invocation_sha256` and `emitter_sha256`
- Same `release_id`

**Result: PASS** — Deterministic endpoint behavior confirmed.

### HEAD Request Parity

HEAD request (internal_version_head.headers) returned identical status and Content-Type as both GET requests:
- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Content-Length: 347

**Result: PASS** — HEAD/GET header parity confirmed.

### Response Format

All responses:
- Status: **200 OK** ✓
- Content-Type: **application/json; charset=utf-8** ✓
- Server: **Werkzeug/3.1.4 Python/3.11.14**
- Cache-Control: **no-store** (correct for internal endpoints)

### Rails Configuration

Tests ran under closed rails:
- `SAFE_MODE=1` — Determinism enforced
- `ALLOW_NETWORK=0` — No external network
- `LC_ALL=C`, `LANG=C`, `TZ=UTC` — Locale locked for reproducibility

### Tokens Earned

- `INTVER_200_CTYPE_JSON_UTF8_OK` — Status 200 + JSON UTF-8 content type
- `INTVER_HEAD_PARITY_OK` — HEAD and GET request parity confirmed

---

End of EPIC020 D3 Internal Version QA Consolidated Artifacts.
