#!/usr/bin/env bash
set -euo pipefail

# Every check below verifies the dev Reader success path, which serves only an
# explicit APP_ENV=dev.  Like the start helper it runs, this script never
# defaults APP_ENV (HDE Mechanics Guide §5.6): the caller supplies it.
if [[ "${APP_ENV-}" != "dev" ]]; then
  echo "VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: ${APP_ENV-<UNSET>})" >&2
  exit 2
fi
export APP_ENV
PORT="${VERIFY_PORT:-5000}"
WORK="$(mktemp -d)"
TOKENS="$WORK/tokens.txt"
: > "$TOKENS"
PID=""
cleanup() {
  if [[ -n "$PID" ]]; then kill "$PID" >/dev/null 2>&1 || true; wait "$PID" 2>/dev/null || true; fi
  rm -rf "$WORK"
}
trap cleanup EXIT

say() { printf "%s\n" "$*"; }

# --- 0) Serializer + emitter determinism ---
python - <<'PY' | tee -a "$TOKENS"
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

# --- 1) Start the canonical dev runner (scripts/dev_start_reader.sh) ---
# free the port if needed
{ command -v fuser >/dev/null && fuser -k "$PORT/tcp"; } >/dev/null 2>&1 || true
{ command -v lsof  >/dev/null && lsof -ti "tcp:$PORT" | xargs -r kill -9; } >/dev/null 2>&1 || true

PORT="$PORT" scripts/dev_start_reader.sh > "$WORK/runner.log" 2>&1 &
PID=$!

URL="http://127.0.0.1:$PORT/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo"

ready=0
for _ in $(seq 1 60); do
  if ! kill -0 "$PID" >/dev/null 2>&1; then break; fi
  if curl -sS -o /dev/null "$URL" >/dev/null 2>&1; then ready=1; break; fi
  sleep 0.5
done
if [[ "$ready" != 1 ]]; then
  echo "RUNNER_FAIL"; sed -n '1,120p' "$WORK/runner.log"; exit 1
fi

# --- 2) GET 200: headers + ETag over identity bytes ---
curl -sS -H 'Accept-Encoding: identity' -D "$WORK/h200.txt" "$URL" -o "$WORK/body200.json" >/dev/null

WORK="$WORK" python - <<'PY' | tee -a "$TOKENS"
import hashlib, re, os
w = os.environ["WORK"]
hdr = open(os.path.join(w, "h200.txt"),"rb").read().decode("latin-1")
bod = open(os.path.join(w, "body200.json"),"rb").read()
def tok(n, ok): print(f"{n}_{'OK' if ok else 'FAIL'}")
tok("READER_200_STATUS", re.match(r'HTTP/\S+\s+200\b', hdr) is not None)
ct  = re.search(r'(?im)^content-type:\s*application/json;\s*charset=utf-8\s*$', hdr) is not None
cc  = re.search(r'(?im)^cache-control:\s*private,\s*max-age=0,\s*must-revalidate\s*$', hdr) is not None
vary= re.search(r'(?im)^vary:\s*authorization,\s*accept-encoding\s*$', hdr) is not None
tok("READER_200_HEADERS", ct and cc and vary)
m = re.search(r'(?im)^etag:\s*("?[0-9a-f]{64}"?)\s*$', hdr)
tok("READER_200_ETAG_PRESENT", bool(m))
tok("READER_200_ETAG_MATCH", bool(m) and m.group(1).strip()=='"%s"'%hashlib.sha256(bod).hexdigest())
PY

# --- 3) 304 empty body + HEAD CL parity ---
ETAG=$(awk 'tolower($1)=="etag:"{print $2}' "$WORK/h200.txt" | tr -d '\r')
curl -sS -D "$WORK/h304.txt" -H "If-None-Match: $ETAG" "$URL" -o /dev/null -w '%{http_code}\n' > "$WORK/code304.txt"

WORK="$WORK" python - <<'PY' | tee -a "$TOKENS"
import os, re, pathlib
w = pathlib.Path(os.environ["WORK"])
hdr  = (w / "h304.txt").read_text(encoding="latin-1")
code = (w / "code304.txt").read_text().strip()
def tok(n, ok): print(f"{n}_{'OK' if ok else 'FAIL'}")
tok("READER_304_STATUS", code=="304")
m = re.search(r'(?im)^content-length:\s*(\d+)\s*$', hdr)
tok("READER_304_EMPTY_BODY", (m is None) or (m and m.group(1)=="0"))
PY

curl -sS -I -D "$WORK/hhead.txt" "$URL" -o /dev/null >/dev/null
WORK="$WORK" python - <<'PY' | tee -a "$TOKENS"
import os, re, pathlib
w = pathlib.Path(os.environ["WORK"])
len_body = (w / "body200.json").stat().st_size
hdr = (w / "hhead.txt").read_text(encoding="latin-1")
m = re.search(r'(?im)^content-length:\s*(\d+)\s*$', hdr)
print("READER_HEAD_CL_MATCH_OK" if (m and int(m.group(1))==len_body) else "READER_HEAD_CL_MATCH_FAIL")
PY

# --- 4) ETag invariance (identity vs gzip) ---
curl -sS -H 'Accept-Encoding: identity' -D "$WORK/h_id.txt" "$URL" -o /dev/null
curl -sS --compressed                 -D "$WORK/h_gz.txt" "$URL" -o /dev/null
awk 'tolower($1)=="etag:"{print $2}' "$WORK/h_id.txt" | tr -d '\r' > "$WORK/et_id.txt"
awk 'tolower($1)=="etag:"{print $2}' "$WORK/h_gz.txt" | tr -d '\r' > "$WORK/et_gz.txt"
{ test -s "$WORK/et_id.txt" && diff -q "$WORK/et_id.txt" "$WORK/et_gz.txt" >/dev/null && echo "ETAG_INVARIANCE_OK" || echo "ETAG_INVARIANCE_FAIL"; } | tee -a "$TOKENS"

# --- 5) Exit 1 if any token failed ---
if grep -q '_FAIL$' "$TOKENS"; then
  exit 1
fi
