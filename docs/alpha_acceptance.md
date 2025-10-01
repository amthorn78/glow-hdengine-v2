# docs/alpha_acceptance.md

**Title:** Glow Alpha Acceptance — A3 (CLI) and A5 (Reader v1 dev harness)  
**Version:** 1.2  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Cards:** CORE-CLI-A3, CORE-READER-A5

## 1. Purpose
Provide a single, prescriptive acceptance gate for Alpha. This verifies public stdout invariants, AB↔BA byte identity, idempotence preimage coupling, strict sidecar gating (A3), and byte-equivalence between Reader v1 and CLI (A5). It also defines **minimal artifacts** and **minimal validation markers** required for PO signoff.

## 2. Governance
- Work on `main`. Deliver **one** revert-friendly commit with the evidence bundle under `artifacts/cards/<CARD>/`. PO performs acceptance. **No PRs** for final approval.
- Acceptance runs with `SAFE_MODE=1`; no network calls unless **both** `SAFE_MODE=0` and `ALLOW_NETWORK=1` are set.

## 3. Canon pins
### 3.1 Canonical serializer
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```
### 3.2 Idempotence preimage (public stdout)
```
idempotence_hash = sha256( sercanon(preimage_without_hash) ).hexdigest()  # lowercase hex
```
### 3.3 Release identity
`scripts/release_id.sh` prints a single **64-hex + LF** for `release/manifest.sorted.json`. No arguments; no extra text.

### 3.4 Public envelope keys and order
Public stdout uses the canonical serializer and MUST contain exactly these top-level keys (sorted by key name):  
`["categories","eligible","idempotence_hash","meta","release_id"]`  
`categories` is an array with exactly one element and that element has **only** `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`. Public payload is **numeric-free** and ends with **exactly one `\n`** (BOM-free, ANSI-free).

---

## 4. A3 — CLI acceptance

### 4.1 Command surface (canonical)
```text
hdctl showcompat \
  --a <path-to-A.json> [--a-tz <IANA>] \
  --b <path-to-B.json> [--b-tz <IANA>] \
  [--showmath] [--admin] [--admin-out <path>]
```
Notes: per-person time zones are required unless contained in each chart; parser uses `allow_abbrev=False`.

### 4.2 Sidecar gate (TS-v0 minimal schema only)
- Gate MUST be: `--showmath` **and** `--admin-out <path>` **and** (`--admin` **or** `HD_ADMIN=1`).  
- Negative gate → exit **2**, stdout empty, no file.  
- Positive gate → atomic write, mode **0600**, LF-terminated.  
- TS-v0 minimal keys only: `type, strategy, features, decision, pair_order, correlation_id, rule_version, timestamp, warning` (**no admin numerics in A3/A5**).  
- Strategy strings: Generator/MG `Wait to respond`; Projector `Wait for the invitation`; Manifestor `Inform`; Reflector `Wait a lunar cycle`.

### 4.3 Acceptance checklist (binary)
- Public stdout: one LF, BOM-free, ANSI-free, exact key set and categories rule.  
- AB↔BA byte identity holds.  
- Preimage recompute equals embedded `idempotence_hash`.  
- Negative gate exits 2 with empty stdout and no sidecar file.  
- Positive gate produces LF + 0600 sidecar.  
- `release_id.txt` contains a single 64-hex line from helper, matching `release_id` in stdout.  
- `validation.log` contains minimal markers (below).

### 4.4 Run this now
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

# Release ID (64-hex + LF)
scripts/release_id.sh > "$OUT/release_id.txt"

# AB and BA
./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo > "$OUT/cli_stdout_AB.json"
./scripts/hdctl.py showcompat --a "$B" --a-tz Africa/Cairo --b "$A" --b-tz Africa/Cairo > "$OUT/cli_stdout_BA.json"
cmp -s "$OUT/cli_stdout_AB.json" "$OUT/cli_stdout_BA.json" && echo "CLI_AB_BA_IDENTITY: OK" | tee "$OUT/IDENTITY_OK.txt"
```

Stdout invariant, shape, preimage:
```python
import re,json,pathlib,hashlib
p=pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)
# enforce presence of canonical keys (order is by sort_keys):
assert list(sorted(o.keys()))==["categories","eligible","idempotence_hash","meta","release_id"]
c=o["categories"][0]; assert c.get("id")=="harmony" and c.get("band") in {"Cool","Open","Warm","Glow"}
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("NO_BOM_STDOUT_OK"); print("NO_ANSI_OK"); print("PREIMAGE_OK"); print("SHAPE_OK")
```

Sidecar gate checks:
```bash
# Negative → exit 2, stdout empty, no file
set +e
./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --admin-out "$SIDECAR" >/dev/null
code=$?; set -e
test "$code" -eq 2 && echo GATE_MISUSE_OK; test ! -f "$SIDECAR"

# Positive → 0600 and LF
HD_ADMIN=1 ./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --showmath --admin-out "$SIDECAR" >/dev/null
stat -c '%a %n' "$SIDECAR" | grep '^600 ' && echo SIDECAR_MODE_0600_OK
python - <<'PY'
b=open("artifacts/cards/A3/admin/sidecar.json","rb").read()
assert b.endswith(b"\n"); print("SIDECAR_LF_OK")
PY
```

Validation log (minimal markers):
```bash
printf "%s\n%s\n%s\n%s\nMETA_INVOCATION_TAG=%s\n" \
  NO_BOM_STDOUT_OK NO_BOM_SIDECAR_OK NO_ANSI_OK NO_REL_DEV_OK "$PRODUCT_INVOCATION_TAG" \
  > "$OUT/validation.log"

python - <<'PY'
h=open("artifacts/cards/A3/release_id.txt").read().strip()
with open("artifacts/cards/A3/validation.log","a") as f:
  f.write("RELEASE_ID_STDOUT="+h+"\n")
  f.write("RELEASE_ID_HELPER="+h+"\n")
print("VALIDATION_LOG_OK")
PY
```

### 4.5 Minimal artifacts (A3)
```
artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/release_id.txt
artifacts/cards/A3/IDENTITY_OK.txt
artifacts/cards/A3/validation.log
# Optional (only if gate used):
artifacts/cards/A3/admin/sidecar.json
```

---

## 5. A5 — Reader v1 acceptance (dev harness)

### 5.1 Scope
Reader v1 is dev-only. It returns bytes identical to the CLI for the same inputs. It is not production traffic. Use for acceptance, smoke, reproducible testing.

### 5.2 Endpoint surface
- `GET /health` → `ok\n`  
- `GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>` → LF-terminated JSON identical to CLI

**Parameter policy**
- `v=1` only.  
- `a`, `b` are **relative** paths resolved under `fixtures/charts/` (reject absolute paths).  
- `a_tz`, `b_tz` required if not present in charts.

### 5.3 Gating and path safety
- If `APP_ENV != dev` → return **403** and do not access filesystem. Body: `{"error":"forbidden"}\n`.  
- If `APP_ENV == dev` → allow only under `fixtures/charts/*`, deny traversal and symlinks.

### 5.4 Transport policy (A5 only)
- `Content-Type: application/json; charset=utf-8` for success and error bodies.  
- **No** `ETag` or `Cache-Control`; no conditional 304. These are introduced in A6.

### 5.5 Acceptance checklist (binary)
- Reader AB body equals CLI AB; Reader BA equals CLI BA.  
- Optional two-run identity on Reader.  
- Preimage recompute equals embedded `idempotence_hash` for Reader AB.  
- Headers: Content-Type correct; no ETag/Cache-Control.  
- APP_ENV gating and path-safety enforced.  
- Validation logs include `EMITTER_SHA256` for provenance.

### 5.6 Run this now
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

# Compare to CLI
cmp -s "$RART/reader_AB.json" "$CART/cli_stdout_AB.json" && echo READER_EQ_CLI_AB_OK > "$RART/stdout_cmp_AB.ok"
cmp -s "$RART/reader_BA.json" "$CART/cli_stdout_BA.json" && echo READER_EQ_CLI_BA_OK > "$RART/stdout_cmp_BA.ok"
```

Reader invariants and preimage:
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

Header checks and provenance:
```bash
grep -i '^content-type: application/json; charset=utf-8' "$RART/headers_AB.txt" && echo CONTENT_TYPE_OK >> "$RART/validation.log"
! grep -i '^etag:' "$RART/headers_AB.txt" && echo NO_ETAG_OK >> "$RART/validation.log"
! grep -i '^cache-control:' "$RART/headers_AB.txt" && echo NO_CACHECTL_OK >> "$RART/validation.log"
sha256sum engine/emit_public.py | awk '{print $1}' | sed 's/^/EMITTER_SHA256=/' >> "$RART/validation.log"
```

### 5.7 Minimal artifacts (A5)
```
artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/validation.log
```

### 5.8 Minimal markers (acceptance will grep these)
**A3:** `NO_BOM_STDOUT_OK`, `NO_BOM_SIDECAR_OK`, `NO_ANSI_OK`, `NO_REL_DEV_OK`, `META_INVOCATION_TAG=…`, `RELEASE_ID_STDOUT=…`, `RELEASE_ID_HELPER=…`, `CLI_AB_BA_IDENTITY: OK`  
**A5:** `READER_EQ_CLI_AB_OK`, `READER_EQ_CLI_BA_OK`, `READER_PREIMAGE_OK`, `CONTENT_TYPE_OK`, `NO_ETAG_OK`, `NO_CACHECTL_OK`, `EMITTER_SHA256=…`

---

## 6. Signoff template (paste in PO closeout)
```
[ALPHA ACCEPTANCE — PO SIGNOFF]
Cards: CORE-CLI-A3, CORE-READER-A5
Result: ACCEPTED
Release ID (64-hex): <value from artifacts/cards/A3/release_id.txt>
Verifier: Full Stack Guru 7
PO: Nathan
Date: <ISO8601>
Notes: CLI and Reader bytes, preimage, invariants, sidecar gate, and minimal evidence verified on main.
```

## 7. Rollback
Revert the single acceptance commit on `main`. No migrations or global edits. Re-run the checks to confirm a clean state.

## 8. Appendix
- Invocation tag regex: `^INV-[0-9A-F]{16,64}$`  
- LF rule: file must end with exactly one `\n`  
- Parser: `allow_abbrev=False` for CLI arguments
