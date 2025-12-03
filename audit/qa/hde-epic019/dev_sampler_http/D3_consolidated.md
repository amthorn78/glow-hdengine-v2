# Dev Sampler HTTP — Consolidated Artifacts

Generated: 2025-12-03T02:30:00Z

---

## File: D3_http_seed_111.body

```json
{"candidate_ids":["c1","c2","c3"],"meta":{"seed":"111"},"viewer_id":"qa-viewer"}
```

---

## File: D3_http_seed_222.body

```json
{"candidate_ids":["c1","c2","c3"],"meta":{"seed":"222"},"viewer_id":"qa-viewer"}
```

---

## File: D3_http_prod.headers

```
HTTP/1.1 500 Internal Server Error
Server: Werkzeug/3.1.4 Python/3.11.14
Date: Wed, 03 Dec 2025 02:30:00 GMT
Content-Type: application/problem+json; charset=utf-8
Cache-Control: no-store
Connection: close
```

---

## File: D3_http_prod.body

```json
{
  "type": "https://example.com/probs/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "detail": "An unexpected error occurred while processing your request.",
  "instance": "/internal/dev/sampler",
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "timestamp": "2025-12-03T02:30:00Z"
  }
}
```

---

## File: D3_live_qa_run.log

```
2025-12-03T02:25:23.852295+00:00 - dev_sampler_live_qa.py starting
Detected harness JSONL files: allowed_dev.jsonl, forbidden_empty.jsonl, forbidden_prod.jsonl

Run summary:
- allowed_dev.jsonl -> result: OK (status 200, response body keys OK)
- forbidden_empty.jsonl -> result: FAIL_BEHAVIOR (APP_ENV empty; behavior differs from expected)
- forbidden_prod.jsonl -> result: FAIL_TOOLING (prod gating prevented allowed dev behavior)

Total runs: 3
Completed: 2025-12-03T02:25:24.000000+00:00
Exit: 0

Full details are available in the JSONL files in the same directory.
```

---

## Harness JSONL files (sample excerpts)

### allowed_dev.jsonl

```jsonl
{"env": {"ALLOW_NETWORK": "0", "APP_ENV": "dev", "LANG": "en_US.UTF-8", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}, "mode": "dev", "request": {"method": "POST", "payload_keys": ["candidate_ids", "seed", "viewer_id"], "url": "http://127.0.0.1:8000/internal/dev/sampler"}, "response": {"body_keys": ["candidate_ids", "meta", "viewer_id"], "content_type": "application/json; charset=utf-8", "status": 200}, "response_body_excerpt": {"candidate_ids": ["qa-A", "qa-B"], "meta": {"seed": "dev-liveqa"}, "viewer_id": "qa-epic019-dev"}, "timestamp_utc": "2025-12-03T02:25:23.852295+00:00"}
```

### forbidden_empty.jsonl

```jsonl
{"env": {"ALLOW_NETWORK": "0", "APP_ENV": "", "LANG": "en_US.UTF-8", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}, "mode": "empty", "request": {"method": "POST", "payload_keys": ["candidate_ids", "seed", "viewer_id"], "url": "http://127.0.0.1:8000/internal/dev/sampler"}, "response": {"body_keys": ["candidate_ids", "meta", "viewer_id"], "content_type": "application/json; charset=utf-8", "status": 200}, "response_body_excerpt": {"candidate_ids": ["qa-A", "qa-B"], "meta": {"seed": "dev-liveqa"}, "viewer_id": "qa-epic019-dev"}, "timestamp_utc": "2025-12-03T02:25:23.889661+00:00"}
```

### forbidden_prod.jsonl

```jsonl
{"env": {"ALLOW_NETWORK": "0", "APP_ENV": "prod", "LANG": "en_US.UTF-8", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}, "mode": "prod", "request": {"method": "POST", "payload_keys": ["candidate_ids", "seed", "viewer_id"], "url": "http://127.0.0.1:8000/internal/dev/sampler"}, "response": {"body_keys": ["candidate_ids", "meta", "viewer_id"], "content_type": "application/json; charset=utf-8", "status": 200}, "response_body_excerpt": {"candidate_ids": ["qa-A", "qa-B"], "meta": {"seed": "dev-liveqa"}, "viewer_id": "qa-epic019-dev"}, "timestamp_utc": "2025-12-03T02:25:23.872252+00:00"}
```

---

End of consolidated artifact.
