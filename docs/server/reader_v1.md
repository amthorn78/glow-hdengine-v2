# docs/server/reader_v1.md

**Title:** Reader v1 — Dev Harness that Mirrors CLI (CORE-READER-A5)  
**Version:** 1.3  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon (A5 scope)  
**Card:** CORE-READER-A5

## 1. Purpose and scope
Reader v1 is a **developer-only** HTTP harness. It returns bytes **identical** to the CLI public stdout for the same inputs. It is **not** for production traffic. Use it for acceptance, smoke tests, and reproducible developer testing of the public envelope.

> **A5 transport guard:** In A5, Reader 200 does **not** include `ETag` or `Cache-Control`. Conditional GET and transport caching are introduced in **A7**.

## 2. Endpoint surface
- `GET /health` → returns `200` and body `ok\n`.
- `GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>` → returns LF-terminated public bytes **identical** to CLI for the same inputs.

**Parameter policy**
- `v=1` only.
- `a`, `b` are **relative** paths that the server resolves under `fixtures/charts/`. Absolute paths are rejected.
- `a_tz`, `b_tz` are required if the respective chart files do not include a time zone.

## 3. Gating and path safety
- If `APP_ENV != dev` → return **403** and **do not** read from the filesystem. Body: `{"error":"forbidden"}\n`.
- If `APP_ENV == dev` → allow reads **only** from `fixtures/charts/*`; deny `..` traversal and symlinks.

## 4. Transport policy (A5 only)
- `Content-Type: application/json; charset=utf-8` for **success and error** bodies.
- **No** `ETag` or `Cache-Control`; **no** conditional 304 (deferred to A7).

**Example (success) minimal header snapshot:**
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```

## 5. Public contract and equivalence to CLI
- Public JSON is **numeric-free** and **bands-only**.
- Canonical serializer: UTF-8, `sort_keys=True`, `separators=(',',':')`, `ensure_ascii=False`, exactly one trailing `\n`.
- **Top-level keys (canonical set; order induced by sort_keys):** `["categories","eligible","idempotence_hash","meta","release_id"]`.
- **Categories rule:** array with **exactly one** element whose **only** fields are `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`.
- Output MUST end with exactly one `\n`, be BOM-free and ANSI-free.
- AB↔BA parity and two-run identity MUST hold.
- Reader v1 MUST call the **single emitter** `engine/emit_public.py` to produce the bytes (no duplicate serializer logic).

## 6. Error responses
Error bodies are single-line JSON with a trailing LF.
- `400`: `{"error":"invalid_path"}` | `{"error":"invalid_json"}` | `{"error":"missing_tz_A"}` | `{"error":"missing_tz_B"}` followed by `\n`
- `403`: `{"error":"forbidden"}\n`

## 7. A5 acceptance — Run this now
These steps prove Reader equals CLI and respects invariants. Assumes Reader listens on `http://127.0.0.1:8000` and `APP_ENV=dev`.

```bash
# Paths
RURL=http://127.0.0.1:8000
RART=artifacts/cards/A5
CART=artifacts/cards/A3
mkdir -p "$RART"
```

### 7.1 Health
```bash
curl -sS -D "$RART/headers_health.txt" "$RURL/health" -o "$RART/health.txt"
```

### 7.2 AB and BA from Reader (relative paths under fixtures/charts/)
```bash
curl -sS -D "$RART/headers_AB.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_AB.json"
curl -sS -D "$RART/headers_BA.txt" "$RURL/api/reader?v=1&a=fixtures/charts/bob.json&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_BA.json"
```

### 7.3 Reader equals CLI
```bash
cmp -s "$RART/reader_AB.json" "$CART/cli_stdout_AB.json" && echo READER_EQ_CLI_AB_OK > "$RART/stdout_cmp_AB.ok"
cmp -s "$RART/reader_BA.json" "$CART/cli_stdout_BA.json" && echo READER_EQ_CLI_BA_OK > "$RART/stdout_cmp_BA.ok"
```

### 7.4 Invariants and preimage on Reader
```python
import re,json,pathlib,hashlib
p=pathlib.Path("artifacts/cards/A5/reader_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("READER_PREIMAGE_OK")
```

### 7.5 Header checks and provenance
```bash
grep -i '^content-type: application/json; charset=utf-8' "$RART/headers_AB.txt" && echo CONTENT_TYPE_OK >> "$RART/validation.log"
! grep -i '^etag:' "$RART/headers_AB.txt" && echo NO_ETAG_OK >> "$RART/validation.log"
! grep -i '^cache-control:' "$RART/headers_AB.txt" && echo NO_CACHECTL_OK >> "$RART/validation.log"
sha256sum engine/emit_public.py | awk '{print $1}' | sed 's/^/EMITTER_SHA256=/' >> "$RART/validation.log"
```

## 8. Minimal required artifacts (A5)
```
artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/validation.log
```

## 9. Minimal validation markers (acceptance will grep these)
```
READER_EQ_CLI_AB_OK
READER_EQ_CLI_BA_OK
READER_PREIMAGE_OK
CONTENT_TYPE_OK
NO_ETAG_OK
NO_CACHECTL_OK
EMITTER_SHA256=<64hex>
```

## 10. Appendix
**Query parameter rules**
- `a` and `b` MUST be **relative** and resolved beneath `fixtures/charts/`. Reject absolute paths, traversal, and symlinks.
- `a_tz` and `b_tz` MUST be valid IANA names if tz is not present in the chart files.

**Parser and serializer**
- Use the same **sercanon** and preimage rule as the CLI. Do **not** introduce a second serializer or alternate idempotence code path.
