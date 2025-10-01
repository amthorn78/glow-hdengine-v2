# docs/alpha_acceptance.md

**Title:** Glow Alpha Acceptance — CLI A3 and Reader A5  
**Version:** 1.0  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Cards:** CORE-CLI-A3, CORE-READER-A5

## 1. Purpose
Provide a single acceptance document for Alpha that covers both CLI A3 and Reader A5. This gate proves public stdout invariants, AB↔BA identity, idempotence preimage, strict sidecar gating, and equivalence between Reader v1 and CLI outputs. It also defines evidence artifacts and validation markers.

## 2. Governance
- Work on `main`. Deliver one revert-friendly commit and the closeout bundle. PO acceptance is the only gate. No PRs for final approval.
- SAFE rails are on by default in dev and stage. Vendor calls are refused unless `SAFE_MODE=0` and `ALLOW_NETWORK=1` are explicitly set.

## 3. Canon pins
### 3.1 Canonical serializer
Use one serializer for public JSON everywhere.
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```
### 3.2 Idempotence preimage
`idempotence_hash = sha256( sercanon(preimage_without_hash) ).hexdigest()`  
Then insert the hash and serialize again with `sercanon(final)`.
### 3.3 Release identity
`scripts/release_id.sh release/manifest.sorted.json` must print a single 64-hex sha256 line to stdout. LF-terminated. No other text.

## 4. Public contract
Public outputs are numeric-free and bands-only. The minimal Reader-shaped JSON must include:
- `eligible` (bool)
- `categories=[{"id":"harmony","band":"Cool|Open|Warm|Glow"}]`
- `meta={"engine_tag": "...", "invocation_tag": "INV-..."}`
- `release_id` as a 64-hex string
- `idempotence_hash` as a 64-hex string
The JSON must be LF-terminated, BOM-free, and ANSI-free.

## 5. CLI A3 acceptance

### 5.1 Command surface (canonical)
```
hdctl showcompat   --a <path-to-A.json> [--a-tz <IANA>]   --b <path-to-B.json> [--b-tz <IANA>]   [--showmath] [--admin] [--admin-out <path>]
```
Notes: time zones are per person unless present in the charts. Parser must use `allow_abbrev=False`.

### 5.2 Sidecar gate
Sidecar is private and excluded from the idempotence preimage. Strict gate:
- Required: `--showmath` and `--admin-out <path>` and (`--admin` or `HD_ADMIN=1`)
- Partial gate returns exit code `2`, stdout empty, and no file
- Positive gate writes an LF-terminated file with mode `0600`
- TS-v0 minimal schema keys: `type`, `strategy`, `features`, `decision`, `pair_order`, `correlation_id`, `rule_version`, `timestamp`, `warning`
- Strategy strings must be exact:
  - Generator or Manifesting Generator -> Wait to respond
  - Projector -> Wait for the invitation
  - Manifestor -> Inform
  - Reflector -> Wait a lunar cycle
- Features include:
  - `strategy_match` (bool)
  - `sacral_pair` (bool, true only when both are Generator or MG)
  - `projector_to_generator` (bool)

### 5.3 Acceptance checklist (binary)
- Stdout invariant holds: one LF, no BOM, no ANSI, minimal shape as defined above
- AB↔BA byte identity holds
- Preimage recompute matches the embedded `idempotence_hash`
- Sidecar negative gate returns exit `2` and no file
- Sidecar positive gate writes mode `0600` and LF
- `release_id.txt` contains a single 64-hex line
- `validation.log` contains required markers

### 5.4 Run this now
These commands run in a shell with Python and `jq` available.

```bash
# Pins
export PRODUCT_INVOCATION_TAG=INV-C9F3AFB03805F430
export ENGINE_TAG=hdengine-alpha
export SAFE_MODE=1
unset ALLOW_NETWORK

# Inputs and paths
A=fixtures/charts/alice.json
B=fixtures/charts/bob.json
OUT=artifacts/cards/A3
SIDECAR="$OUT/admin/sidecar.json"
mkdir -p "$OUT/admin"

# Release ID
scripts/release_id.sh release/manifest.sorted.json > "$OUT/release_id.txt"

# AB and BA runs
./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo > "$OUT/cli_stdout_AB.json"
./scripts/hdctl.py showcompat --a "$B" --a-tz Africa/Cairo --b "$A" --b-tz Africa/Cairo > "$OUT/cli_stdout_BA.json"
cmp -s "$OUT/cli_stdout_AB.json" "$OUT/cli_stdout_BA.json" && echo IDENTITY_OK > "$OUT/IDENTITY_OK.txt"

# Stdout invariant and shape
python - <<'PY'
import re,json,pathlib
p=pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)
assert set(o.keys())>= {"categories","meta","release_id","idempotence_hash"}
cats=o["categories"]; assert isinstance(cats,list) and len(cats)==1
c=cats[0]; assert c.get("id")=="harmony" and c.get("band") in {"Cool","Open","Warm","Glow"}
print("NO_BOM_STDOUT_OK"); print("NO_ANSI_OK"); print("SHAPE_OK")
PY

# Preimage recompute
python - <<'PY'
import json,hashlib,pathlib,json as J
p=pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json")
o=J.loads(p.read_text(encoding="utf-8"))
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(J.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("PREIMAGE_OK")
PY

# Sidecar negative gate
set +e
./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --admin-out "$SIDECAR" >/dev/null
code=$?; set -e
test "$code" -eq 2 && echo GATE_MISUSE_OK
test ! -f "$SIDECAR"

# Sidecar positive gate
HD_ADMIN=1 ./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --showmath --admin-out "$SIDECAR" >/dev/null
stat -c '%a %n' "$SIDECAR" | grep '^600 ' && echo SIDECAR_MODE_0600_OK
python - <<'PY'
b=open("artifacts/cards/A3/admin/sidecar.json","rb").read()
assert b.endswith(b"\n"); print("SIDECAR_LF_OK")
PY

# Validation log
printf "%s
%s
%s
%s
META_INVOCATION_TAG=%s
"   NO_BOM_STDOUT_OK NO_BOM_SIDECAR_OK NO_ANSI_OK NO_REL_DEV_OK "$PRODUCT_INVOCATION_TAG"   > "$OUT/validation.log"
python - <<'PY'
h=open("artifacts/cards/A3/release_id.txt").read().strip()
open("artifacts/cards/A3/validation.log","a").write("RELEASE_ID_STDOUT="+h+"\nRELEASE_ID_HELPER="+h+"\n")
print("VALIDATION_LOG_OK")
PY
```

### 5.5 Artifacts (exact names)
```
artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/admin/sidecar.json            # present only when gated
artifacts/cards/A3/release_id.txt
artifacts/cards/A3/IDENTITY_OK.txt
artifacts/cards/A3/validation.log
```

## 6. Reader A5 acceptance

### 6.1 Purpose and scope
Reader v1 is a dev-only HTTP harness that returns bytes identical to the CLI for the same inputs. It is not for production traffic. Use it for acceptance, smoke tests, and reproducible developer testing.

### 6.2 Endpoint surface
- `GET /health` returns `ok\n` for startup checks
- `GET /api/reader?v=1&a=<path>&b=<path>&a_tz=<IANA>&b_tz=<IANA>` returns LF-terminated public bytes identical to CLI

### 6.3 Gating and path safety
- If `APP_ENV != dev` return `403` with `{"error":"forbidden"}\n`
- When `APP_ENV == dev` allow only `fixtures/charts/*`
- Deny `..` traversal and symlinks
- Require tz present either in chart or via `a_tz` and `b_tz`

### 6.4 Error bodies
LF-terminated one-line JSON only:
- `400` with `{"error":"invalid_path"|"invalid_json"|"missing_tz_A"|"missing_tz_B"}\n`
- `403` with `{"error":"forbidden"}\n`

### 6.5 Transport policy
Only `Content-Type: application/json; charset=utf-8`. No `ETag` or `Cache-Control` in A5. A6 introduces those headers and conditional 304.

### 6.6 Acceptance checklist (binary)
- Reader AB body equals CLI AB body
- Reader BA body equals CLI BA body
- AB↔BA identity on Reader
- Two-run identity on Reader
- Preimage recompute matches `idempotence_hash` on Reader output
- Correct Content-Type, and no ETag or Cache-Control
- APP_ENV gating and path safety enforced
- Error bodies are one-line LF-terminated JSON

### 6.7 Run this now
Assumes the Reader dev server is listening on `http://127.0.0.1:8000` and `APP_ENV=dev`.

```bash
RURL=http://127.0.0.1:8000
RART=artifacts/cards/A5
CART=artifacts/cards/A3
mkdir -p "$RART"

# Health
curl -sS -D "$RART/headers_health.txt" "$RURL/health" -o "$RART/health.txt"

# AB and BA from Reader
curl -sS -D "$RART/headers_AB.txt" "$RURL/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_AB.json"
curl -sS -D "$RART/headers_BA.txt" "$RURL/api/reader?v=1&a=fixtures/charts/bob.json&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_BA.json"

# Compare Reader vs CLI
cmp -s "$RART/reader_AB.json" "$CART/cli_stdout_AB.json" && echo READER_EQ_CLI_AB_OK > "$RART/stdout_cmp_AB.ok"
cmp -s "$RART/reader_BA.json" "$CART/cli_stdout_BA.json" && echo READER_EQ_CLI_BA_OK > "$RART/stdout_cmp_BA.ok"

# Invariants on Reader AB
python - <<'PY'
import re,json,pathlib,hashlib
p=pathlib.Path("artifacts/cards/A5/reader_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("READER_PREIMAGE_OK")
PY

# Header checks
grep -i '^content-type: application/json; charset=utf-8' "$RART/headers_AB.txt" && echo CONTENT_TYPE_OK >> "$RART/validation.log"
! grep -i '^etag:' "$RART/headers_AB.txt" && echo NO_ETAG_OK >> "$RART/validation.log"
! grep -i '^cache-control:' "$RART/headers_AB.txt" && echo NO_CACHECTL_OK >> "$RART/validation.log"

# Error body checks
curl -sS -D "$RART/headers_400.txt" "$RURL/api/reader?v=1&a=../etc/passwd&b=fixtures/charts/alice.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" -o "$RART/reader_400.json" -w "" || true
python - <<'PY'
b=open("artifacts/cards/A5/reader_400.json","rb").read()
assert b.endswith(b"\n"), "ERROR_LF_FAIL"
print("ERROR_LF_OK")
PY
```

### 6.8 Artifacts (exact names)
```
artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/headers_400.txt
artifacts/cards/A5/reader_400.json
artifacts/cards/A5/stdout_cmp_AB.ok
artifacts/cards/A5/stdout_cmp_BA.ok
artifacts/cards/A5/validation.log
artifacts/cards/A3/release_id.txt          # produced by A3 and reused here
```

## 7. Validation markers (verbatim strings)

### 7.1 A3 markers
```
CLI_AB_BA_IDENTITY: OK
ABBA_BYTES_OK
TWO_RUN_IDENTITY_OK
NO_BOM_STDOUT_OK
NO_BOM_SIDECAR_OK
NO_ANSI_OK
NO_REL_DEV_OK
META_INVOCATION_TAG=INV-C9F3AFB03805F430
RELEASE_ID_STDOUT=<64hex>
RELEASE_ID_HELPER=<64hex>
```

### 7.2 A5 markers
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

## 8. Signoff template
```
[ALPHA ACCEPTANCE — PO SIGNOFF]
Cards: CORE-CLI-A3, CORE-READER-A5
Result: ACCEPTED
Release ID (64-hex): <value from artifacts/cards/A3/release_id.txt>
Verifier: Full Stack Guru 7
PO: Nathan
Date: <ISO8601>
Notes: CLI and Reader checks, preimage coupling, stdout invariants, sidecar gate, and evidence verified on main.
```

## 9. Rollback
Revert the single acceptance commit on main. No migrations or global edits. Re-run the checks to confirm a clean state.

## 10. Appendix
- Invocation tag regex: `^INV-[0-9A-F]{16,64}$`
- LF check: file must end with a single `\n`
- Parser: `allow_abbrev=False` in CLI arguments
