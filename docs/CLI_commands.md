# docs/CLI_commands.md

**Title:** Glow CLI — `hdctl showcompat` (CORE-CLI-A3)  
**Version:** 1.2  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Card:** CORE-CLI-A3

## 1. Purpose
Define the canonical CLI surface for `hdctl showcompat`, the **public stdout** contract (keys, order, LF rule), idempotence preimage, strict sidecar gate, exit codes, determinism checks, and the **minimal** acceptance artifacts for A3.

## 2. Invocation (canonical)
```text
hdctl showcompat \
  --a <path-to-A.json> [--a-tz <IANA>] \
  --b <path-to-B.json> [--b-tz <IANA>] \
  [--showmath] [--admin] [--admin-out <path>]
```
Notes:
- Time zones are **per person** unless present in each chart file.
- Argument parser MUST use `allow_abbrev=False`.
- Acceptance runs SHOULD set `SAFE_MODE=1` (no network).

## 3. Public stdout contract (A3)
Public stdout is **numeric-free**, **bands-only**, and is the **only** thing written to stdout on success. It MUST be:
- UTF-8 JSON using the canonical serializer, **exactly one** trailing `\n`
- **BOM-free** and **ANSI-free**
- **Top-level keys (canonical set and order)**:  
  `["categories","eligible","idempotence_hash","meta","release_id"]`  
  This set is required. Order is induced by `sort_keys=True`.
- **Categories rule:** array with **exactly one** element whose **only** fields are `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`.

### 3.1 Canonical serializer
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```

## 4. Idempotence preimage rule
`idempotence_hash` couples the public bytes to their canonical preimage.
- Procedure: *remove* `idempotence_hash` → `sercanon(preimage)` → `sha256` (lowercase hex) → insert as `idempotence_hash` → `sercanon(final)`.
- Acceptance MUST recompute and assert equality.

Example recompute:
```python
import json, hashlib, pathlib
p = pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json")
o = json.loads(p.read_text(encoding="utf-8"))
pre = dict(o); pre.pop("idempotence_hash", None)
from json import dumps
canon = (dumps(pre, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n").encode("utf-8")
assert hashlib.sha256(canon).hexdigest() == o["idempotence_hash"]
print("PREIMAGE_OK")
```

## 5. Sidecar gate (TS-v0 minimal schema only)
The admin sidecar is **private** and **excluded** from the idempotence preimage. It is written **only** when the strict gate is satisfied.
- Gate MUST be: `--showmath` **and** `--admin-out <path>` **and** (`--admin` **or** `HD_ADMIN=1`).
- **Partial gate** MUST exit with code **2**, stdout empty, and no file created.
- Sidecar write MUST be **atomic**, **LF-terminated**, and file mode **0600**.
- TS-v0 **minimal** schema keys (no admin numerics in A3/A5):  
  `type, strategy, features, decision, pair_order, correlation_id, rule_version, timestamp, warning`
- Exact strategy strings:  
  Generator / Manifesting Generator → `Wait to respond`  
  Projector → `Wait for the invitation`  
  Manifestor → `Inform`  
  Reflector → `Wait a lunar cycle`
- Features: `strategy_match` (bool), `sacral_pair` (bool, **true only when both are Generator/MG**), `projector_to_generator` (bool).

## 6. Exit codes
- `0` — success
- `2` — **GATE_MISUSE** (strict sidecar gate not satisfied)
- `3` — missing or invalid **per-person** time zone (A or B)
- `4` — invalid path or missing required file
- `>4` — unexpected error

## 7. Determinism and parity
- **AB↔BA parity:** swapping A and B MUST NOT change public stdout bytes (`cmp -s` succeeds).
- **Two-run identity:** repeating the same run MUST produce **identical** bytes.

## 8. Minimal acceptance artifacts (A3)
Use **exactly** these paths; sidecar is optional and present only if the gate is exercised.
```
artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/release_id.txt
artifacts/cards/A3/IDENTITY_OK.txt
artifacts/cards/A3/validation.log
# Optional (only if gate used):
artifacts/cards/A3/admin/sidecar.json
```

## 9. Release identity
- `scripts/release_id.sh` MUST emit the **64-hex** sha256 of `release/manifest.sorted.json` to stdout, **LF-terminated**, nothing else.
- The same 64-hex MUST be recorded in `artifacts/cards/A3/release_id.txt` and MUST match the `release_id` in public stdout.

## 10. Run-This-Now (acceptance)
Shell with Python and `jq` available.

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

Stdout invariant, shape, and preimage:
```python
import re,json,pathlib,hashlib
p=pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b)

# presence of canonical keys (order induced by sort_keys):
assert list(sorted(o.keys()))==["categories","eligible","idempotence_hash","meta","release_id"]

c=o["categories"][0]; assert c.get("id")=="harmony" and c.get("band") in {"Cool","Open","Warm","Glow"}
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
assert hashlib.sha256(canon).hexdigest()==o["idempotence_hash"]
print("NO_BOM_STDOUT_OK"); print("NO_ANSI_OK"); print("PREIMAGE_OK"); print("SHAPE_OK")
```

Negative and positive sidecar gate:
```bash
# Negative gate → exit 2, stdout empty, no file
set +e
./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --admin-out "$SIDECAR" >/dev/null
code=$?; set -e
test "$code" -eq 2 && echo GATE_MISUSE_OK; test ! -f "$SIDECAR"

# Positive gate → 0600 and LF
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

## 11. Appendix — Pair fingerprint (when used in TS-v0)
When a pair fingerprint is required, the preimage object is **exactly**:
```json
{"gates":[<sorted unique integers>]}
```
Hash the **canonical bytes** of that object with the serializer above.

## 12. Governance note
Acceptance delivery is a **single revert-friendly commit to `main`** with the evidence bundle under `artifacts/cards/A3/`. No PRs for final approval; PO performs the closeout.
