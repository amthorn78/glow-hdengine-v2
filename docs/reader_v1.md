# docs/server/reader_v1.md

**Title:** Reader v1 — Dev Harness that Mirrors CLI (CORE-READER-A5)  
**Version:** 1.0  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Card:** CORE-READER-A5

## 1. Purpose and scope
Reader v1 is a minimal developer-only HTTP harness. It returns bytes that are identical to the CLI public stdout for the same inputs. It is not for production traffic. Use it for acceptance, smoke tests, and reproducible developer testing of the public envelope.

## 2. Endpoint surface
- `GET /health` returns `200` and body `ok\n`.
- `GET /api/reader?v=1&a=<path>&b=<path>&a_tz=<IANA>&b_tz=<IANA>` returns LF-terminated public bytes identical to CLI for the same inputs.

**Query parameters**
- `v` required. Only `v=1` is allowed.
- `a`, `b` required. Paths to charts under `fixtures/charts/`.
- `a_tz`, `b_tz` required if the respective chart files do not include a time zone.

## 3. Gating and path safety
- If `APP_ENV != dev` the server must return `403` and **must not** read from the filesystem.
- If `APP_ENV == dev` allow reads only from `fixtures/charts/*`. Deny `..` traversal and symlinks.
- For each person, require a valid IANA time zone either in the chart or via `a_tz` and `b_tz`.

## 4. Transport policy for A5
- `Content-Type: application/json; charset=utf-8` only.
- No `ETag` or `Cache-Control` headers in A5. These are added in A6 along with conditional 304.
- Response body is LF-terminated, BOM-free, and ANSI-free.

## 5. Public contract and equivalence to CLI
- Public JSON is numeric-free and bands-only.
- Minimal shape must include:
  - `eligible` (bool)
  - `categories=[{"id":"harmony","band":"Cool|Open|Warm|Glow"}]`
  - `meta={"engine_tag":"...","invocation_tag":"INV-..."}`
  - `release_id` as a 64-hex string (sha256 of `release/manifest.sorted.json`)
  - `idempotence_hash` as a 64-hex string
- Output must end with exactly one `\n`, with no BOM and no ANSI codes.
- AB↔BA parity and two-run identity must hold.
- Reader v1 **must** use the single canonical emitter `engine/emit_public.py` to produce public bytes. Do not duplicate the serializer or idempotence preimage logic.

## 6. Error responses
Error bodies are single-line JSON with a trailing LF. Examples:
- `400`: `{"error":"invalid_path"}` or `{"error":"invalid_json"}` or `{"error":"missing_tz_A"}` or `{"error":"missing_tz_B"}` followed by `\n`
- `403`: `{"error":"forbidden"}\n`

## 7. Determinism and acceptance checks
The steps below prove that Reader equals CLI and respects invariants. These commands assume the dev server listens on `http://127.0.0.1:8000` and `APP_ENV=dev`.

```bash
# Pins and paths
RURL=http://127.0.0.1:8000
RART=artifacts/cards/A5
CART=artifacts/cards/A3
mkdir -p "$RART"
```

### 7.1 Health
```bash
curl -sS -D "$RART/headers_health.txt" "$RURL/health" -o "$RART/health.txt"
```

### 7.2 AB and BA from Reader
```bash
curl -sS -D "$RART/headers_AB.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_AB.json"
curl -sS -D "$RART/headers_BA.txt" "$RURL/api/reader?v=1&a=fixtures/charts/bob.json&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_BA.json"
# Optional second AB for two-run identity
curl -sS "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_AB_2.json"
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

### 7.5 Header checks for A5
```bash
grep -i '^content-type: application/json; charset=utf-8' "$RART/headers_AB.txt" && echo CONTENT_TYPE_OK >> "$RART/validation.log"
! grep -i '^etag:' "$RART/headers_AB.txt" && echo NO_ETAG_OK >> "$RART/validation.log"
! grep -i '^cache-control:' "$RART/headers_AB.txt" && echo NO_CACHECTL_OK >> "$RART/validation.log"
```

### 7.6 Error body checks
```bash
curl -sS -D "$RART/headers_400.txt" "$RURL/api/reader?v=1&a=../etc/passwd&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_400.json" -w "" || true
python - <<'PY'
b=open("artifacts/cards/A5/reader_400.json","rb").read()
assert b.endswith(b"\n"), "ERROR_LF_FAIL"
print("ERROR_LF_OK")
PY
```

### 7.7 Provenance pins
Record the emitter hash in validation logs to prove single-emitter usage.
```bash
sha256sum engine/emit_public.py | awk '{print $1}' | sed 's/^/EMITTER_SHA256=/' >> "$RART/validation.log"
```

## 8. Required artifacts (A5)
```
artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_AB_2.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/headers_400.txt
artifacts/cards/A5/reader_400.json
artifacts/cards/A5/stdout_cmp_AB.ok
artifacts/cards/A5/stdout_cmp_BA.ok
artifacts/cards/A5/validation.log
artifacts/cards/A3/cli_stdout_AB.json      # from A3, used for equality check
artifacts/cards/A3/cli_stdout_BA.json      # from A3, used for equality check
artifacts/cards/A3/release_id.txt          # 64-hex release id from A3
```

## 9. Validation markers (verbatim examples)
```
READER_EQ_CLI_AB_OK
READER_EQ_CLI_BA_OK
READER_ABBA_BYTES_OK
READER_TWO_RUN_IDENTITY_OK
READER_PREIMAGE_OK
CONTENT_TYPE_OK
NO_ETAG_OK
NO_CACHECTL_OK
APP_ENV_GATING_OK
ERROR_ONE_LINE_OK
ERROR_LF_OK
NO_DUPLICATE_SERIALIZER_OK
EMITTER_SHA256=<64hex>
```

## 10. Appendix
**Query parameter rules**
- `a` and `b` must be absolute paths beneath `fixtures/charts/` or server must resolve them against that root. Do not allow `..` or symlinks.
- `a_tz` and `b_tz` must be valid IANA names if tz is not present in the chart files.

**Parser and serializer**
- Use the same sercanon and preimage rule as the CLI. Do not introduce a second serializer.
