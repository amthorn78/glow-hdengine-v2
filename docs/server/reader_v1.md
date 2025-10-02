docs/server/reader_v1.md

Title: Reader v1 — Dev Harness that Mirrors CLI
Version: 2.0
Owner: Cyrano (Tech Writer)
Status: Canon (A7 scope)
Cards: CORE-READER-A5 (body invariants), A7 transport

1. Purpose and scope

Reader v1 is a developer-only HTTP harness. It returns bytes identical to the CLI public stdout for the same inputs. It is not for production traffic. Use it for acceptance, smoke tests, and reproducible developer testing of the public envelope.

> A7 transport: Reader now implements strong ETag, caching validators, conditional GET, and HEAD parity. Body semantics remain frozen by the Spec.



2. Endpoint surface

GET /health → returns 200 and body ok\n.

GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA> → returns LF-terminated public bytes identical to CLI for the same inputs.


Parameter policy

v=1 only.

a, b are relative paths that the server resolves under fixtures/charts/. Absolute paths are rejected.

a_tz, b_tz are required if the respective chart files do not include a time zone.


3. Gating and path safety

If APP_ENV != dev → return 403 and do not read from the filesystem. Body: {"error":"forbidden"}\n.

If APP_ENV == dev → allow reads only from fixtures/charts/*; deny .. traversal and symlinks.


4. Transport policy (A7)

Success (200 OK)

Content-Type: application/json; charset=utf-8

Cache-Control: private, max-age=0, must-revalidate

Vary: Authorization, Accept-Encoding

ETag: "<sha256(final LF-terminated body bytes)>" (strong, quoted; computed over the pre-compression entity)

ETag is invariant across identity, gzip, and br.


Conditional GET (304 Not Modified)

Triggered by a strong If-None-Match match. Accept comma-separated lists; ignore weak W/ tokens; ignore *.

Return 304 with no body. Include ETag, Vary, Cache-Control. Content-Length: 0 or absent. Content-Type optional.


HEAD parity

Same validators as GET 200. No body.

Content-Length == len(identity GET body).


Errors (4xx/5xx)

One-line JSON + LF. Content-Type: application/json; charset=utf-8.

No ETag. Cache-Control: no-store.


Framework controls

Disable any auto-ETag and auto-cache features.


5. Public contract and equivalence to CLI

Public JSON is numeric-free and bands-only for SPA use.

Canonical serializer: UTF-8, sort_keys=True, separators=(',',':'), ensure_ascii=False, exactly one trailing \n.

Top-level keys (canonical set; order induced by sort_keys): ["categories","eligible","idempotence_hash","meta","release_id"].

Categories rule: array with exactly one element whose only fields are {"id":"harmony","band":"Cool|Open|Warm|Glow"}.

Output MUST end with exactly one \n, be BOM-free and ANSI-free.

AB↔BA parity and two-run identity MUST hold.

Reader v1 MUST call the single emitter engine/emit_public.py to produce the bytes (no duplicate serializer logic).


6. Error responses

Error bodies are single-line JSON with a trailing LF.

400: {"error":"invalid_path"} | {"error":"invalid_json"} | {"error":"missing_tz_A"} | {"error":"missing_tz_B"} followed by \n

403: {"error":"forbidden"}\n


7. A7 acceptance — Run this now

These steps prove transport behavior and CLI equivalence. Assumes Reader listens on http://127.0.0.1:8000 and APP_ENV=dev.

# Paths
RURL=http://127.0.0.1:8000
RART=artifacts/cards/A7
CART=artifacts/cards/A3
mkdir -p "$RART"

7.1 Health

curl -sS -D "$RART/headers_health.txt" "$RURL/health" -o "$RART/health.txt"
grep -q '^ok$' "$RART/health.txt" && echo READER_HEALTH_OK >> "$RART/validation.log"

7.2 AB and BA from Reader (identity body for hashing)

curl -sS -H 'Accept-Encoding: identity' -D "$RART/headers_AB.txt" \
  "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" \
  -o "$RART/reader_AB.json"

curl -sS -H 'Accept-Encoding: identity' -D "$RART/headers_BA.txt" \
  "$RURL/api/reader?v=1&a=fixtures/charts/bob.json&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" \
  -o "$RART/reader_BA.json"

7.3 Reader equals CLI

cmp -s "$RART/reader_AB.json" "$CART/cli_stdout_AB.json" && echo READER_EQ_CLI_AB_OK >> "$RART/validation.log"
cmp -s "$RART/reader_BA.json" "$CART/cli_stdout_BA.json" && echo READER_EQ_CLI_BA_OK >> "$RART/validation.log"

7.4 Preimage and idempotence on Reader

import re,json,pathlib,hashlib
p=pathlib.Path("artifacts/cards/A7/reader_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("READER_PREIMAGE_OK")

7.5 Header checks (200/304/HEAD) and compression invariance

# 200 identity
grep -i '^content-type: application/json; charset=utf-8' "$RART/headers_AB.txt" && echo READER_200_CT_OK >> "$RART/validation.log"
grep -i '^cache-control: private, max-age=0, must-revalidate' "$RART/headers_AB.txt" && echo READER_200_CACHECTL_OK >> "$RART/validation.log"
grep -i '^vary: authorization, accept-encoding' "$RART/headers_AB.txt" && echo READER_200_VARY_OK >> "$RART/validation.log"
ETAG=$(grep -i '^etag:' "$RART/headers_AB.txt" | awk '{print $2}' | tr -d '\r')
echo "READER_200_ETAG_PRESENT=${ETAG}" >> "$RART/validation.log"

# recompute ETag from identity body
python - <<'PY'
import hashlib,sys
b=open("artifacts/cards/A7/reader_AB.json","rb").read()
print("READER_200_ETAG_MATCH="+('OK' if '"%s"'%hashlib.sha256(b).hexdigest()==open("artifacts/cards/A7/headers_AB.txt").read().splitlines()[-1].split(': ',1)[1] else 'FAIL'))
PY >> "$RART/validation.log"

# 200 gzip and br must keep same ETag
curl -sS --compressed -D "$RART/headers_AB_gzip.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o /dev/null
grep -qi "^etag: $(echo $ETAG)" "$RART/headers_AB_gzip.txt" && echo READER_200_GZIP_ETAG_SAME=OK >> "$RART/validation.log"

curl -sS -H 'Accept-Encoding: br' -D "$RART/headers_AB_br.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o /dev/null
grep -qi "^etag: $(echo $ETAG)" "$RART/headers_AB_br.txt" && echo READER_200_BR_ETAG_SAME=OK >> "$RART/validation.log"

# 304 from If-None-Match
curl -sS -D "$RART/headers_304.txt" -H "If-None-Match: $ETAG" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o /dev/null -w '%{http_code}\n' | grep -q '^304$' && echo READER_304_STATUS_OK >> "$RART/validation.log"
! grep -qi '^content-length: [1-9]' "$RART/headers_304.txt" && echo READER_304_EMPTY_BODY_OK >> "$RART/validation.log"

# HEAD parity
curl -sS -I -D "$RART/headers_head.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o /dev/null
grep -qi '^etag: ' "$RART/headers_head.txt" && echo READER_HEAD_ETAG_OK >> "$RART/validation.log"
LEN=$(wc -c < "$RART/reader_AB.json")
grep -qi "^content-length: $LEN$" "$RART/headers_head.txt" && echo READER_HEAD_CL_MATCH_OK >> "$RART/validation.log"

7.6 Errors and auto-headers

# error posture
curl -sS -D "$RART/headers_err.txt" "$RURL/api/reader?v=1&a=/etc/passwd&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/error.json" -w '%{http_code}\n' | grep -q '^400$' && echo READER_400_STATUS_OK >> "$RART/validation.log"
! grep -qi '^etag:' "$RART/headers_err.txt" && echo READER_400_NO_ETAG_OK >> "$RART/validation.log"
grep -qi '^cache-control: no-store' "$RART/headers_err.txt" && echo READER_400_NOSTORE_OK >> "$RART/validation.log"
grep -qi '^content-type: application/json; charset=utf-8' "$RART/headers_err.txt" && echo READER_400_CT_OK >> "$RART/validation.log"

# auto-ETag disabled
! grep -qi '^etag:' "$RART/headers_health.txt" && echo READER_AUTOTAG_DISABLED_OK >> "$RART/validation.log"

8. Minimal required artifacts (A7)

artifacts/cards/A7/reader_AB.json
artifacts/cards/A7/headers_AB.txt
artifacts/cards/A7/headers_AB_gzip.txt
artifacts/cards/A7/headers_AB_br.txt
artifacts/cards/A7/headers_304.txt
artifacts/cards/A7/headers_head.txt
artifacts/cards/A7/headers_health.txt
artifacts/cards/A7/error.json
artifacts/cards/A7/headers_err.txt
artifacts/cards/A7/validation.log

9. Minimal validation markers (acceptance will grep these)

READER_HEALTH_OK
READER_EQ_CLI_AB_OK
READER_EQ_CLI_BA_OK
READER_PREIMAGE_OK
READER_200_CT_OK
READER_200_CACHECTL_OK
READER_200_VARY_OK
READER_200_ETAG_PRESENT="<etag>"
READER_200_ETAG_MATCH=OK
READER_200_GZIP_ETAG_SAME=OK
READER_200_BR_ETAG_SAME=OK
READER_304_STATUS_OK
READER_304_EMPTY_BODY_OK
READER_HEAD_ETAG_OK
READER_HEAD_CL_MATCH_OK
READER_400_STATUS_OK
READER_400_NO_ETAG_OK
READER_400_NOSTORE_OK
READER_400_CT_OK
READER_AUTOTAG_DISABLED_OK

10. Appendix

Query parameter rules

a and b MUST be relative and resolved beneath fixtures/charts/. Reject absolute paths, traversal, and symlinks.

a_tz and b_tz MUST be valid IANA names if tz is not present in the chart files.


Parser and serializer

Use the same sercanon and preimage rule as the CLI. Do not introduce a second serializer or alternate idempotence code path.


Updated from v1.3 (A5) to v2.0 (A7 transport and acceptance). 