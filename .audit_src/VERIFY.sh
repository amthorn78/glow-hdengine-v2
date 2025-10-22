#!/usr/bin/env bash
set -euo pipefail

export APP_ENV=${APP_ENV:-dev}

say() { printf "%s\n" "$*"; }

# --- 0) Serializer + emitter determinism ---
python - <<'PY'
import os, json, hashlib, sys
from engine.stable.sercanon import serialize
from engine.emit_public import emit_public_envelope

def tok(name, ok): print(f"{name}_{'OK' if ok else 'FAIL'}")

# serializer one LF + sorted keys
b = serialize({"b":1,"a":2})
tok("SERIALIZER_ONE_LF", b.endswith(b"\n") and not b[:-1].endswith(b"\n") and b.decode().startswith('{"a":2,"b":1}'))

# inputs
with open("fixtures/charts/alice.json","r",encoding="utf-8") as f: A=json.load(f)
with open("fixtures/charts/bob.json","r",encoding="utf-8")   as f: B=json.load(f)
et=os.environ.get("ENGINE_TAG","hdengine-alpha")
it=os.environ.get("PRODUCT_INVOCATION_TAG","INV-UNKNOWN")
rid=os.environ.get("RELEASE_ID","0"*64)

AB1 = emit_public_envelope(A,B,et,it,rid)
AB2 = emit_public_envelope(A,B,et,it,rid)
BA  = emit_public_envelope(B,A,et,it,rid)

o=json.loads(AB1); pre=dict(o); pre.pop("idempotence_hash",None)
idh = hashlib.sha256(serialize(pre)).hexdigest()
tok("PREIMAGE", idh==o["idempotence_hash"])
tok("TWO_RUN_IDENTITY", AB1==AB2)
tok("AB_BA", AB1==BA)
PY

# --- 1) Start runner (adapter blueprint) ---
# free port 5000 if needed
{ command -v fuser >/dev/null && fuser -k 5000/tcp; } >/dev/null 2>&1 || true
{ command -v lsof  >/dev/null && lsof -ti tcp:5000 | xargs -r kill -9; } >/dev/null 2>&1 || true

python -u - <<'PY' > .verify_runner.log 2>&1 &
from dev.reader_harness.app import app
app.run(host="127.0.0.1", port=5000, debug=False)
PY
PID=$!
sleep 1
if ! ps -p "$PID" >/dev/null 2>&1; then
  echo "RUNNER_FAIL"; sed -n '1,120p' .verify_runner.log; exit 1
fi

URL='http://127.0.0.1:5000/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo'

# --- 2) GET 200: headers + ETag over identity bytes ---
curl -sS -H 'Accept-Encoding: identity' -D .h200.txt "$URL" -o .body200.json >/dev/null

python - <<'PY'
import hashlib, re, os
hdr = open(".h200.txt","rb").read().decode("latin-1")
bod = open(".body200.json","rb").read()
def tok(n, ok): print(f"{n}_{'OK' if ok else 'FAIL'}")
ct  = re.search(r'(?im)^content-type:\s*application/json;\s*charset=utf-8\s*$', hdr) is not None
cc  = re.search(r'(?im)^cache-control:\s*private,\s*max-age=0,\s*must-revalidate\s*$', hdr) is not None
vary= re.search(r'(?im)^vary:\s*authorization,\s*accept-encoding\s*$', hdr) is not None
tok("READER_200_HEADERS", ct and cc and vary)
m = re.search(r'(?im)^etag:\s*("?[0-9a-f]{64}"?)\s*$', hdr)
tok("READER_200_ETAG_PRESENT", bool(m))
tok("READER_200_ETAG_MATCH", bool(m) and m.group(1).strip()=='"%s"'%hashlib.sha256(bod).hexdigest())
PY

# --- 3) 304 empty body + HEAD CL parity ---
ETAG=$(awk 'BEGIN{IGNORECASE=1}/^etag:/{print $2}' .h200.txt | tr -d '\r')
curl -sS -D .h304.txt -H "If-None-Match: $ETAG" "$URL" -o /dev/null -w '%{http_code}\n' > .code304.txt

python - <<'PY'
import re, pathlib
hdr  = pathlib.Path(".h304.txt").read_text(encoding="latin-1")
code = pathlib.Path(".code304.txt").read_text().strip()
def tok(n, ok): print(f"{n}_{'OK' if ok else 'FAIL'}")
tok("READER_304_STATUS", code=="304")
m = re.search(r'(?im)^content-length:\s*(\d+)\s*$', hdr)
tok("READER_304_EMPTY_BODY", (m is None) or (m and m.group(1)=="0"))
PY

curl -sS -I -D .hhead.txt "$URL" -o /dev/null >/dev/null
python - <<'PY'
import os, re, pathlib
len_body = os.path.getsize(".body200.json")
hdr = pathlib.Path(".hhead.txt").read_text(encoding="latin-1")
m = re.search(r'(?im)^content-length:\s*(\d+)\s*$', hdr)
print("READER_HEAD_CL_MATCH_OK" if (m and int(m.group(1))==len_body) else "READER_HEAD_CL_MATCH_FAIL")
PY

# --- 4) ETag invariance (identity vs gzip) ---
curl -sS -H 'Accept-Encoding: identity' -D .h_id.txt "$URL" -o /dev/null
curl -sS --compressed                 -D .h_gz.txt "$URL" -o /dev/null
awk 'BEGIN{IGNORECASE=1}/^etag:/{print $2}' .h_id.txt | tr -d '\r' > .et_id.txt
awk 'BEGIN{IGNORECASE=1}/^etag:/{print $2}' .h_gz.txt | tr -d '\r' > .et_gz.txt
diff -q .et_id.txt .et_gz.txt >/dev/null && echo "ETAG_INVARIANCE_OK" || echo "ETAG_INVARIANCE_FAIL"

# --- 5) Stop runner ---
kill "$PID" >/dev/null 2>&1 || true

# --- 6) Exit 1 if any FAIL printed ---
if grep -q "_FAIL" <(grep -E '(_OK|_FAIL)$' <<<"$(cat .h200.txt .h304.txt .hhead.txt 2>/dev/null; true)"; \
                    printf "%s\n" "$(cat .verify_runner.log 2>/dev/null)"; \
                    true) || \
   grep -q "_FAIL" <(grep -E '(_OK|_FAIL)$' <<<"$(cat)"); then
  exit 1
fi
