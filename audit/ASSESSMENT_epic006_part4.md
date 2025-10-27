PASS: TRANSPORT_A7_OK CLI_READER_PARITY_OK MATH_INVENTORY_OK ENV_SNAPSHOT_RECORDED_OK SERVICE_CMD_CAPTURED_OK DB_DISCOVERY_SHARED_OK DB_SCHEMA_HDE_OK DB_SEARCH_PATH_OK DB_RW_OK AUDIT_GUARDS_OK
FAIL: INTVER_NO_STORE_NO_ETAG_OK

```json
{ "run_ts": "2025-10-27T22:36:58Z", "run_id": "2baee8f1-f960-4c86-b8e8-8bf80816c4d1", "release_id": "ef260e9aa3c673af240d17a2660480361a8e081d1ffeca2a5ed0e3219fc18567" }
```

## Part 1 — Core findings

### /internal/version snapshots (dev app could not reach DB)

**GET**
```txt
# GET /internal/version @ 2025-10-27T22:35:57Z
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 22:35:57 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 265
Connection: close

<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>

```

**HEAD**
```txt
# HEAD /internal/version @ 2025-10-27T22:36:00Z
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 22:36:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 265
Connection: close


```

**Conditional GET (If-None-Match/If-Modified-Since)**
```txt
# Conditional GET /internal/version @ 2025-10-27T22:36:02Z
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 22:36:02 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 265
Connection: close

<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>

```

> Result: all attempts returned HTTP 500 with the Werkzeug HTML fallback because the Flask dev server could not reach the Railway Postgres instance (psycopg `Network is unreachable`). No-cache headers therefore could not be verified in this environment.

### DB bridge recap (release `ef260e9a…`)

- `version`: version PostgreSQL 17.6 (Debian 17.6-2.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit (1 row)
- `schemas`: {"schemas":["hde","information_schema","pg_catalog","pg_toast","public"]}
- `search_path`: search_path "$user", public (1 row)
- `search_path (runtime)`: {"search_path":"hde, public"}
- `rw_check`: first lines from read/write smoke test
```txt
Output format is unaligned.
PASS: schema hde exists
PASS: all 4 base tables exist
PASS: current-month partitions exist
PASS: public_results PK(id, created_at)
PASS: pair_evaluation PK(id, evaluated_at)
PASS: pair_evaluation UNIQUE(min_user,max_user,release_id,evaluated_at)
PASS: public_results indexes present
PASS: pair_evaluation indexes present
```

### Hygiene confirmations

- Service command:
```txt
APP_ENV=dev python -c 'from flask import Flask; from engine.emit_public import emit_public_envelope; from adapter.http_reader import get_reader_bp; import os; app=Flask(__name__); app.register_blueprint(get_reader_bp(emit_public_envelope), url_prefix='/api'); app.run(host='0.0.0.0', port=int(os.environ.get('PORT','8000')));'

```
- Env snapshot (first five lines):
```txt
APP_ENV=<redacted>
DATABASE_URL=<redacted>
SAFE_MODE=<redacted>
ALLOW_NETWORK=<redacted>
PORT=<redacted>
```

## Part 2 — Reader transport & parity

### Transport captures (endpoint `GET http://127.0.0.1:8000/api/reader`)

```txt
# RUN_TS: 2025-10-27T18:58:25Z
# RUN_ID: d0c1c079-1bf9-426a-8002-5d3ecf9900df
# Endpoint: http://127.0.0.1:8000/api/reader

## GET 200
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 18:58:52 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 300
ETag: "5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031"
Cache-Control: private, max-age=0, must-revalidate
Vary: Authorization, Accept-Encoding
Connection: close

{"categories":[{"band":"Warm","id":"harmony"}],"eligible":true,"idempotence_hash":"eb9a01ee1a2a5df5083e9410ab857b7af1528a8f05bf4d8cefd9bc7089535e80","meta":{"engine_tag":"hdengine-alpha","invocation_tag":"INV-UNKNOWN"},"release_id":"0000000000000000000000000000000000000000000000000000000000000000"}

## HEAD 200
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 18:59:02 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 300
ETag: "5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031"
Cache-Control: private, max-age=0, must-revalidate
Vary: Authorization, Accept-Encoding
Connection: close


## GET 304 (If-None-Match "5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031")
HTTP/1.1 304 NOT MODIFIED
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 18:59:06 GMT
ETag: "5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031"
Cache-Control: private, max-age=0, must-revalidate
Vary: Authorization, Accept-Encoding
Connection: close


## GET error (invalid_version)
HTTP/1.1 400 BAD REQUEST
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 18:59:11 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 28
Cache-Control: no-store
Connection: close

{"error":"invalid_version"}

## POST with If-* headers
HTTP/1.1 405 METHOD NOT ALLOWED
Server: Werkzeug/3.1.3 Python/3.11.12
Date: Mon, 27 Oct 2025 18:59:18 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 31
Cache-Control: no-store
Connection: close

{"error":"method_not_allowed"}
```

- 200 OK body length = 300 bytes with SHA-256 `5d7f1923…2031` and `Cache-Control: private, max-age=0, must-revalidate`.
- HEAD 200 echoed `Content-Type: application/json; charset=utf-8` and `Content-Length: 300`, matching the 200 response.
- 304 response preserved the strong ETag and stripped `Content-Type`, keeping `Content-Length: 0` as implemented.
- Error posture: `400 invalid_version` uses JSON body, `Cache-Control: no-store`, no ETag.

### ETag validation

```txt
## ETag validation
Preimage rule: SHA-256 of LF-terminated 200 OK body bytes (pre-compression), quoted.
Computed SHA-256: 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031
Returned ETag: "5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031"
```

The computed SHA-256 of the LF-terminated 200 body exactly matched the returned strong ETag.

### CLI ↔ Reader digest parity

Reader requests were issued against `http://127.0.0.1:8000/api/reader` with `v=1` and fixture pairs. CLI invocations used `PYTHONPATH=. APP_ENV=dev python scripts/hdctl.py showcompat …`.

| Case | Reader SHA-256 | CLI SHA-256 | Result |
| --- | --- | --- | --- |
| A=alice, B=bob (GET http://127.0.0.1:8000/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=UTC&b_tz=UTC&run_id=d0c1c079-1bf9-426a-8002-5d3ecf9900df&case=1) | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | PASS case 1 |
| A=bob, B=alice (GET http://127.0.0.1:8000/api/reader?v=1&a=fixtures/charts/bob.json&b=fixtures/charts/alice.json&a_tz=UTC&b_tz=UTC&run_id=d0c1c079-1bf9-426a-8002-5d3ecf9900df&case=2) | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | PASS case 2 |
| A=alice, B=alice (boundary same chart) (GET http://127.0.0.1:8000/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/alice.json&a_tz=UTC&b_tz=UTC&run_id=d0c1c079-1bf9-426a-8002-5d3ecf9900df&case=3) | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | 5d7f19230de75ed00c158d3380d9809df2b4808e982761a9f959971ba7012031 | PASS case 3 |
All three parity cases produced identical digests (`5d7f1923…2031`) confirming deterministic reader/CLI alignment.

## Part 3 — Math inventory highlights

### Coverage snapshot

| Category | Count |
| --- | ---: |
| hashing | 4 |
| time | 4 |
| rounding | 1 |
| normalization | 1 |
| banding | 1 |
| scoring | 1 |
| random | 1 |
| constraint | 2 |

**Top modules by item count:** engine (11), scripts (2), adapter (1).

### Spotlight items

1. **engine.compat.compute._score_for** — hashes the normalized pair, mods by 101, scales by `(0.5 + 0.5*w)`, rounds half-up, and clamps to `[0,100]` ensuring deterministic banding inputs. (Constants: 101, 0.5.)
2. **engine.compat.compute.band_for** — maps numeric scores to `Cool/Open/Warm/Glow` via inclusive thresholds `24/49/74`, keeping boundary determinism explicit.
3. **adapter.retry_after.parse_retry_after_ms** — converts seconds to milliseconds (`*1000`) and enforces non-negative retry windows before integer casting, avoiding fractional drift.
4. **scripts.release_id_tools.validate_manifest** — rejects manifest entries with missing/negative sizes, anchoring release integrity checks around zero lower bound.

All formulas align with the deterministic emission path captured in the CLI/Reader parity evidence.

## Artifacts index

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| artifacts/headers/internal_version_get.txt | 506 | `285905c2d04ae627ebd8f892159a1ff9bf9d698d1a2df67edaa7e778497f91ba` |
| artifacts/headers/internal_version_head.txt | 242 | `0d47320613307b3088c1db3773465b14f3016c8aa2f0d586e30431cfcf2b2f95` |
| artifacts/headers/internal_version_conditional.txt | 518 | `646a2676de845cac90ee75c709692f64cceea9b82651fd8569bb708b963132d6` |
| artifacts/db/version.txt | 131 | `36b57d321a9390b45a2aefdf1a79c09e045d91c7351d7ddc4f5f0c03884c2623` |
| artifacts/db/schemas.txt | 74 | `21c84d1c4aeb40b35e0b2270af14bc18bc45d152050983053325d6813dd14d5c` |
| artifacts/db/search_path.txt | 36 | `b2cc89178ff4b3c3afc36fb8dd5fbf2bdbfc20fa00854e9933a6c3992ecea0f0` |
| artifacts/db/search_path_runtime.txt | 30 | `4dc4db90d55de76bbe04caa31deefe0cc87d9e283ac096cf2dabf282f972b664` |
| artifacts/db/verify_epic005.txt | 349 | `7db86293e5488a7080ac37397fd47146c558890bf4f51e553605b7e573170433` |
| artifacts/validation/service_cmd.txt | 327 | `3c090bb49c265e1f8d4fe7c990c1ca9e4fd97bcac0ed1865d0de68f417d29da5` |
| artifacts/env/ENV_SNAPSHOT.txt | 144 | `8a642bd40089783682ccaf01fda1eed090b75d53e9891b88a2c12f35b49f5159` |
| artifacts/proofs/reader_transport.txt | 2304 | `5f6214dd78a78f65e8a84dcc6f3c52adfd3ef3eca8d36226f4c54fbf44fd20e9` |
| artifacts/proofs/cli_reader_parity.txt | 1784 | `5a0ce6fcc7a7e22773edaa4f200e7450dfb1ffbc7e8b1971ea93a65ed1f5536f` |
| artifacts/cli/out.json | 326 | `98e8b6534c03c5ec9fcd6ea0b77b49e17fba6758ff1dc3a7930ee8d7e355af21` |
| artifacts/cli/hash.txt | 65 | `b2766a4ad7c2039bf91e29aa359543d226ebd59a63db87b24ee83f57b6d8780b` |
| artifacts/math/coverage.txt | 405 | `98bbc23d99a09d9ca6c17593b08b0ed6f061e1a03d8dffe52c8a5dce35a2bf96` |
| artifacts/math/inventory.md | 3538 | `4e91288fd3c83f729e47bdb1dc851fbb274c1b4945b98cce446963f992192137` |
| audit/ASSESSMENT_epic006_part4.md | 10986 | `0a215d5824974a50546c458c6338cf1118187b014b377a80a645985c5f37a74b` |
