# Reader v1 — A7 Acceptance Crib
# Command-only checklist: run in Codespace with APP_ENV=dev and Reader at http://127.0.0.1:8000

RURL=http://127.0.0.1:8000
RART=artifacts/cards/A7
mkdir -p "$RART"

# 1) Health
curl -sS -D "$RART/headers_health.txt" "$RURL/health" -o "$RART/health.txt"
grep -q '^ok$' "$RART/health.txt" && echo READER_HEALTH_OK >> "$RART/validation.log"

# 2) Identity GET (Accept-Encoding: identity)
curl -sS -H 'Accept-Encoding: identity' -D "$RART/headers_AB.txt" \
  "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" \
  -o "$RART/reader_AB.json"

# 3) Compression variants (gzip & br) must preserve ETag
curl -sS --compressed -D "$RART/headers_AB_gzip.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json" -o /dev/null
curl -sS -H 'Accept-Encoding: br' -D "$RART/headers_AB_br.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json" -o /dev/null

# 4) Recompute ETag from identity body (pre-compression)
python - <<'PY' > "$RART/preimage_check.log"
import hashlib
b=open("artifacts/cards/A7/reader_AB.json","rb").read()
print("ETAG_RECOMPUTED="+hashlib.sha256(b).hexdigest())
PY
python - <<'PY' >> "$RART/validation.log"
import hashlib,re
h=open("artifacts/cards/A7/preimage_check.log").read().strip().split('=',1)[1]
hdr=open("artifacts/cards/A7/headers_AB.txt").read()
m=re.search(r'(?mi)^etag:\s*"?([a-f0-9]{64})"?',hdr)
print("READER_200_ETAG_MATCH="+("OK" if m and m.group(1)==h else "FAIL"))
PY

# 5) Conditional GET → 304
ETAG=$(grep -i '^etag:' "$RART/headers_AB.txt" | awk '{print $2}' | tr -d '\r')
curl -sS -D "$RART/headers_304.txt" -H "If-None-Match: $ETAG" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json" -o /dev/null -w '%{http_code}\n' | grep -q '^304$' && echo READER_304_STATUS_OK >> "$RART/validation.log"
! grep -qi '^content-length: [1-9]' "$RART/headers_304.txt" && echo READER_304_EMPTY_BODY_OK >> "$RART/validation.log"

# 6) HEAD parity
curl -sS -I -D "$RART/headers_head.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json" -o /dev/null
grep -qi '^etag:' "$RART/headers_head.txt" && echo READER_HEAD_ETAG_OK >> "$RART/validation.log"
LEN=$(wc -c < "$RART/reader_AB.json")
grep -qi "^content-length: $LEN$" "$RART/headers_head.txt" && echo READER_HEAD_CL_MATCH_OK >> "$RART/validation.log"

# 7) Error posture (invalid path)
curl -sS -D "$RART/headers_err.txt" "$RURL/api/reader?v=1&a=/etc/passwd&b=fixtures/charts/bob.json" -o "$RART/error.json" -w '%{http_code}\n' | grep -q '^400$' && echo READER_400_STATUS_OK >> "$RART/validation.log"
! grep -qi '^etag:' "$RART/headers_err.txt" && echo READER_400_NO_ETAG_OK >> "$RART/validation.log"
grep -qi '^cache-control: no-store' "$RART/headers_err.txt" && echo READER_400_NOSTORE_OK >> "$RART/validation.log"

# 8) Final artifact checklist (exists)
for f in reader_AB.json headers_AB.txt headers_AB_gzip.txt headers_AB_br.txt headers_304.txt headers_head.txt headers_health.txt error.json headers_err.txt validation.log; do
  [ -f "$RART/$f" ] && echo "ARTIFACT_OK $f" >> "$RART/validation.log" || echo "MISSING $f" >> "$RART/validation.log"
done