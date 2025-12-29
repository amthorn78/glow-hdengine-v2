# Ops Discovery Bundle — EPIC022 /internal/version

**Discovery ID:** `opsdisc_20251228t020126z`  
**Captured:** 2025-12-28T02:01:26Z  
**Target:** `https://glow-hdengine-v2-production.up.railway.app`

---

## Environment Context

### Base URL
```
https://glow-hdengine-v2-production.up.railway.app
```

### Auth Header Presence
```json
{
  "header_name": "Authorization",
  "present": true
}
```

### Rails Posture
- `SAFE_MODE=0`
- `ALLOW_NETWORK=1`
- `APP_ENV=prod`
- `LC_ALL=C`
- `LANG=C`
- `TZ=UTC`

---

## Discovery Summary

```json
{
  "probes": [
    {
      "body_bytes": 207,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/root.get.noauth.headers",
      "label": "root.get.noauth",
      "rc": 0,
      "status_line": "HTTP/2 404",
      "stderr_tail": null
    },
    {
      "body_bytes": null,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/root.head.noauth.headers",
      "label": "root.head.noauth",
      "rc": 18,
      "status_line": "HTTP/2 404",
      "stderr_tail": "curl: (18) end of response with 347 bytes missing"
    },
    {
      "body_bytes": 347,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.get.noauth.headers",
      "label": "internal_version.get.noauth",
      "rc": 0,
      "status_line": "HTTP/2 200",
      "stderr_tail": null
    },
    {
      "body_bytes": null,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.head.noauth.headers",
      "label": "internal_version.head.noauth",
      "rc": 18,
      "status_line": "HTTP/2 200",
      "stderr_tail": "curl: (18) end of response with 347 bytes missing"
    },
    {
      "body_bytes": 347,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.get.auth.headers",
      "label": "internal_version.get.auth",
      "rc": 0,
      "status_line": "HTTP/2 200",
      "stderr_tail": null
    },
    {
      "body_bytes": null,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.head.auth.headers",
      "label": "internal_version.head.auth",
      "rc": 18,
      "status_line": "HTTP/2 200",
      "stderr_tail": "curl: (18) end of response with 347 bytes missing"
    },
    {
      "body_bytes": 347,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.cond_inm.noauth.headers",
      "label": "internal_version.cond_inm.noauth",
      "rc": 0,
      "status_line": "HTTP/2 200",
      "stderr_tail": null
    },
    {
      "body_bytes": 347,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.cond_ims.noauth.headers",
      "label": "internal_version.cond_ims.noauth",
      "rc": 0,
      "status_line": "HTTP/2 200",
      "stderr_tail": null
    },
    {
      "body_bytes": 347,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.get.noauth.http1.headers",
      "label": "internal_version.get.noauth.http1",
      "rc": 0,
      "status_line": "HTTP/1.1 200 OK",
      "stderr_tail": null
    },
    {
      "body_bytes": null,
      "headers_path": "audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version/internal_version.head.noauth.http1.headers",
      "label": "internal_version.head.noauth.http1",
      "rc": 28,
      "status_line": "HTTP/1.1 200 OK",
      "stderr_tail": "curl: (28) Operation timed out after 30002 milliseconds with 0 out of 347 bytes received"
    }
  ]
}
```

---

## Sample Response Body

**Endpoint:** `/internal/version` (GET, no auth)

```json
{"engine_tag":"hdengine@prod","build_commit":"9479d28","invocation_tag":"INV-f2ac55d77ce9aacc","invocation_sha256":"3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","release_id":"077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5"}
```

**Headers:**
```
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sun, 28 Dec 2025 02:01:26 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: abldWOR7Tai3adedjUJq2g
content-length: 347
```

---

## Integrity Checksums

```
ac4797257da28a764ca4c7ba1a71890a95ada61230dea1cbd6408c527d54cb6c  auth_header_presence.json
f5c74feb560bc046cb71655f5dc79429c33d21dbb548b165864460ead2ea3e1b  captured_at_utc.txt
5695da8506eb159dbad3802306c78ce454185d1e637fa2a343910ca19e00b273  curl_version.txt
290024e64d5c99ce676eac09302e790d87f40dc1e7ededfedcc57ae8ea098d49  hde_base_url.txt
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a  internal_version.cond_ims.noauth.body
f90b806a91b0bf3973475cc7e9ecc8cb4fbde8b343f4f9f37a49924432a46b50  internal_version.cond_ims.noauth.headers
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  internal_version.cond_ims.noauth.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  internal_version.cond_ims.noauth.stderr
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a  internal_version.cond_inm.noauth.body
0f1d24b2196362caa4410c1f00f0dc3b3dc3fa0c4e3097921fd48ddb51a7266c  internal_version.cond_inm.noauth.headers
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  internal_version.cond_inm.noauth.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  internal_version.cond_inm.noauth.stderr
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a  internal_version.get.auth.body
e8a4b9014382dd7d527cd74571a3f715f07181ecec2ea007ce5b91ef8362c090  internal_version.get.auth.headers
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  internal_version.get.auth.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  internal_version.get.auth.stderr
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a  internal_version.get.noauth.body
ae384f137ce1b69787db50f0c97aa3f4ad20e62c2a249412a9b8ca1082dfe178  internal_version.get.noauth.headers
9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a  internal_version.get.noauth.http1.body
dff32a17dbf3c6545d54ea5f8161cba959264c6619b2e478802e6faf3944d3f4  internal_version.get.noauth.http1.headers
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  internal_version.get.noauth.http1.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  internal_version.get.noauth.http1.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  internal_version.get.noauth.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  internal_version.get.noauth.stderr
34991b728184b51cc3d6fba4eacdaaeb9daca50054af5089286ab8aa5f6f6b09  internal_version.head.auth.headers
7ee29791fc17e986b97128845622b077fb45e349fdb80523fac9dba879b4ad60  internal_version.head.auth.rc
ad657ca265fa5ed18f3684c9602dff5a6830b8d4e9cc76418aac1fbc7443b629  internal_version.head.auth.stderr
758100a7181626e676ba1044a272858bbf2d18e2dc4a746452b6a5d8eb5c4293  internal_version.head.noauth.headers
afd772e4a1e2ac23fc3623178cd208d3d0592b9bde78f80f7cabe9d36b228d2b  internal_version.head.noauth.http1.headers
9961d158a7e0e2f990765971a9e490af826c0743b7d603020f34cc8944319fcb  internal_version.head.noauth.http1.rc
a7ed23522616d91183552fe94a41668d16e9beca191e3020d7b21409f405adce  internal_version.head.noauth.http1.stderr
7ee29791fc17e986b97128845622b077fb45e349fdb80523fac9dba879b4ad60  internal_version.head.noauth.rc
ad657ca265fa5ed18f3684c9602dff5a6830b8d4e9cc76418aac1fbc7443b629  internal_version.head.noauth.stderr
2a90b292184970c71e8ab2873802279d6e090012e45cf432c7297c2544cddd8c  ops_discovery_summary.json
8fa6fee68fb4ca8eda41d4db888f6a2a6b039d072f18375fa9df13d8912037d7  python_version.txt
e9639e3c4681ce85f852fbac48e2eeee5ba51296dbfec57c200d59b76237ab80  root.get.noauth.body
b379eaea6b7ee5a1473ffaf331193d4bb419e599a4a5a5a18b60ecc5548f7a6b  root.get.noauth.headers
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  root.get.noauth.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  root.get.noauth.stderr
b12f5c10240202ec130c961e1c717aaded0b32ecc54f9270eadff1fd4f017a04  root.head.noauth.headers
7ee29791fc17e986b97128845622b077fb45e349fdb80523fac9dba879b4ad60  root.head.noauth.rc
9ed657348f3185046fee1ef34a87ada3ce1622d9e46d0101b8bd51ef0228b88d  root.head.noauth.stderr
```

---

## Operational Observations

1. **GET success:** `/internal/version` returns HTTP 200 with 347-byte JSON response (both with and without Authorization header)

2. **HEAD failures:** All HTTP/2 HEAD requests fail with curl rc=18 ("end of response with X bytes missing"), suggesting Railway edge proxy issue with HEAD method over HTTP/2

3. **HTTP/1.1 HEAD timeout:** HEAD request over HTTP/1.1 times out (rc=28, 30+ seconds), indicating HEAD method not working in production environment

4. **No conditional response:** Conditional requests (If-None-Match, If-Modified-Since) return HTTP 200 with full body instead of 304 Not Modified, indicating ETag/Last-Modified caching is not implemented

5. **Auth not enforced:** Authorization header present in environment but endpoint returns 200 regardless of auth presence (no 401/403 enforcement detected in production)

---

**Output Directory:** `audit/qa/hde-epic022/opsdisc_20251228t020126z/results/ops_discovery_internal_version`
