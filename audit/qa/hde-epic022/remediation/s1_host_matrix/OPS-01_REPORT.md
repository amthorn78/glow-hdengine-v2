# OPS-01 Report: Host Reachability Matrix for /internal/version

**Task ID:** OPS-01  
**Epic:** HDE-EPIC022 Remediation 2  
**Execution Date:** 2025-12-29  
**Status:** ✅ COMPLETE

## Executive Summary

Successfully discovered and validated a reachable production host for `GET /internal/version`. The selected host (`prod_railway`) returned HTTP 200 without authentication and provides a stable base URL for downstream remediation steps.

**Selected Host:** `prod_railway`  
**Selected Base URL:** `https://glow-hdengine-v2-production.up.railway.app`  
**Authentication Required:** No (unauthenticated probe succeeded with HTTP 200)

---

## Deliverables

### D1: Host Reachability Matrix

**File:** `host_matrix.md`

```markdown
]633;E;echo "| host_label | base_url | reachable | http_status | notes | selected |";89b3a77a-c414-40f6-af47-032135216c73]633;C| host_label | base_url | reachable | http_status | notes | selected |
| --- | --- | --- | --- | --- | --- |
| prod_railway | https://glow-hdengine-v2-production.up.railway.app | Y | 200 | status_line: HTTP/2 200 ; auth_used=N | SELECTED |
```

**Analysis:**
- Total candidates probed: 1
- Reachable hosts: 1
- Hosts returning HTTP 200: 1
- Selected host: `prod_railway` (SELECTED marker present)

---

### D2: Selected Base URL

**File:** `selected_base_url.txt`

```
https://glow-hdengine-v2-production.up.railway.app
```

---

### D3: Selected Host Label

**File:** `selected_host_label.txt`

```
prod_railway
```

---

### D4: Raw HTTP Headers

**File:** `headers_raw_SELECTED.txt`

```
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Mon, 29 Dec 2025 20:35:07 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: k_a98rgYQCWSLMIeYqdHTg
content-length: 347

```

**Key Observations:**
- Protocol: HTTP/2
- Status: 200 OK
- Cache-Control: no-store (appropriate for ops endpoints)
- Content-Type: application/json; charset=utf-8
- Server: railway-edge
- Content-Length: 347 bytes

---

### D5: Curl Stderr Capture

**File:** `curl_stderr_SELECTED.txt`

```
(empty - curl succeeded without errors)
```

---

### D6: Structured Headers (JSON)

**File:** `headers_internal_version_sample.json`

```json
{"headers":{"cache-control":"no-store","content-length":"347","content-type":"application/json; charset=utf-8","date":"Mon, 29 Dec 2025 20:35:07 GMT","server":"railway-edge","x-railway-edge":"railway/europe-west4-drams3a","x-railway-request-id":"k_a98rgYQCWSLMIeYqdHTg"},"status_line":"HTTP/2 200"}
```

**Schema Validation:** ✅ PASS
- Contains `status_line` (string): `"HTTP/2 200"`
- Contains `headers` (object): 7 header fields, all lower-case keys
- Newline-terminated: Yes
- Valid JSON: Yes

---

## Verification Results

All success criteria satisfied:

- [x] **D1:** Exactly one SELECTED row present with reachable=Y and http_status=200
- [x] **D2:** Base URL matches SELECTED row exactly (copied, not retyped)
- [x] **D3:** Host label matches SELECTED row exactly (copied, not retyped)
- [x] **D4:** Raw headers non-empty, includes HTTP status line
- [x] **D5:** File exists (empty indicates success)
- [x] **D6:** Valid JSON with required keys, lower-case header names

Verification command output:
```
OPS-01 verification: OK
```

---

## Environment Context

**Discovery Source:**
- Production base URL from PF07 — Glow Infrastructure, §2.2
- No additional base URLs discovered from environment variables

**Authentication Posture:**
- Unauthenticated probe succeeded
- No Authorization header required for HTTP 200 response
- AUTH_HEADER_VALUE not used

**Determinism Environment:**
- LC_ALL=C
- LANG=C
- TZ=UTC

---

## Next Steps (Out of Scope for OPS-01)

The selected base URL (`https://glow-hdengine-v2-production.up.railway.app`) is now available for downstream HDE-EPIC022 Remediation 2 steps:

1. Full response body capture for `/internal/version`
2. Schema validation against expected structure
3. Evidence artifact generation for acceptance mapping

**Critical Constraint:** Downstream steps MUST reuse the exact base_url string from `selected_base_url.txt` verbatim. Do not retype or reconstruct the URL.

---

## File Manifest

```
audit/qa/hde-epic022/remediation/s1_host_matrix/
 OPS-01_REPORT.md                           (this file)
 host_matrix.md                              (D1: reachability matrix)
 selected_base_url.txt                       (D2: selected base URL)
 selected_host_label.txt                     (D3: selected host label)
 headers_raw_SELECTED.txt                    (D4: raw HTTP headers)
 curl_stderr_SELECTED.txt                    (D5: curl stderr, empty)
 headers_internal_version_sample.json        (D6: structured headers JSON)
```

**Total Artifacts:** 7 files (6 deliverables + 1 report)

---

**Report Generated:** 2025-12-29  
**OPS-01 Status:** ✅ COMPLETE
