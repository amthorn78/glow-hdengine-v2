# docs/CLI_commands.md

**Title:** Glow CLI — `hdctl showcompat` (CORE-CLI-A3)  
**Version:** 1.0  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Card:** CORE-CLI-A3

## 1. Purpose
Define the canonical CLI surface for `hdctl showcompat`, the public stdout contract, idempotence preimage rule, sidecar gate, exit codes, and required acceptance artifacts. This page is authoritative for implementers and QA.

## 2. Invocation (canonical)
```
hdctl showcompat   --a <path-to-A.json> [--a-tz <IANA>]   --b <path-to-B.json> [--b-tz <IANA>]   [--showmath] [--admin] [--admin-out <path>]
```
Notes:
- Per-person time zones are required unless present in each chart file.
- Parser must use `allow_abbrev=False`.

## 3. Public stdout contract
Public stdout is a minimal Reader-shaped JSON that is numeric-free, LF-terminated, BOM-free, and ANSI-free.
- Top-level fields:
  - `eligible` — boolean
  - `categories` — array with exactly one item: `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`
  - `meta` — object containing at least `engine_tag` and `invocation_tag`
  - `release_id` — string, 64-hex, the sha256 of `release/manifest.sorted.json`
  - `idempotence_hash` — string, 64-hex
- Exactly one trailing `\n`. No additional whitespace. No BOM. No ANSI.

## 4. Canonical serializer
Use a single canonical serializer in all components that produce public JSON.
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```

## 5. Idempotence preimage rule
`idempotence_hash` couples the bytes to their canonical preimage.
- Procedure: remove `idempotence_hash` → `sercanon(preimage)` → sha256 (lowercase hex) → insert as `idempotence_hash` → `sercanon(final)`.
- Acceptance must recompute and assert equality.

Example recompute snippet:
```python
import json, hashlib, sys, pathlib
p = pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json")
o = json.loads(p.read_text(encoding="utf-8"))
pre = dict(o); pre.pop("idempotence_hash", None)
canon = sercanon(pre).encode("utf-8")
assert hashlib.sha256(canon).hexdigest() == o["idempotence_hash"]
print("PREIMAGE_OK")
```

## 6. Sidecar gate and TS-v0
The admin sidecar is private and excluded from the idempotence preimage. It is written only when the strict gate is satisfied.
- Gate must be: `--showmath` and `--admin-out <path>` and (`--admin` or `HD_ADMIN=1`).
- Partial gate must exit with code `2`, stdout empty, and no file created.
- Sidecar write must be atomic and file mode must be `0600`. Sidecar must be LF-terminated.
- TS-v0 minimal schema keys: `type`, `strategy`, `features`, `decision`, `pair_order`, `correlation_id`, `rule_version`, `timestamp`, `warning`.
- Strategy strings must be exact:
  - Generator or Manifesting Generator → `Wait to respond`
  - Projector → `Wait for the invitation`
  - Manifestor → `Inform`
  - Reflector → `Wait a lunar cycle`
- Features must include: `strategy_match` (bool), `sacral_pair` (bool, true only when both are Generator/MG), `projector_to_generator` (bool).

## 7. Exit codes
- `0` — success
- `2` — GATE_MISUSE (strict sidecar gate not satisfied)
- `3` — missing or invalid per-person time zone for A or B
- `4` — invalid path or missing required file
- `>4` — unexpected error

## 8. Determinism and parity
- AB↔BA parity: swapping A and B must not change public stdout bytes. `cmp -s AB.json BA.json` must succeed.
- Two-run identity: repeating the same run must produce identical bytes.
- Public output is numeric-free and bands-only.

## 9. Acceptance artifacts (A3) — required names
All acceptance outputs must use these exact paths:
```
artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/admin/sidecar.json            # only when gated
artifacts/cards/A3/stdout.sha256
artifacts/cards/A3/sidecar.sha256
artifacts/cards/A3/lastline_stdout.hex
artifacts/cards/A3/lastline_sidecar.hex
artifacts/cards/A3/IDENTITY_OK.txt
artifacts/cards/A3/validation.log
```

## 10. Release identity
- `scripts/release_id.sh` must emit the 64-hex sha256 of `release/manifest.sorted.json` to stdout, LF-terminated, nothing else.
- The 64-hex value must be recorded as the `release_id` in public output and written to `artifacts/cards/A3/release_id.txt` during acceptance.

## 11. Quick acceptance checks
These examples run in a fresh shell with Python and `jq` available.

AB and BA runs:
```bash
A=fixtures/charts/alice.json
B=fixtures/charts/bob.json
OUT=artifacts/cards/A3
mkdir -p "$OUT/admin"

./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo > "$OUT/cli_stdout_AB.json"
./scripts/hdctl.py showcompat --a "$B" --b "$A" --a-tz Africa/Cairo --b-tz Africa/Cairo > "$OUT/cli_stdout_BA.json"
cmp -s "$OUT/cli_stdout_AB.json" "$OUT/cli_stdout_BA.json" && echo IDENTITY_OK > "$OUT/IDENTITY_OK.txt"
```

Stdout invariant and shape:
```python
import re,json,pathlib
p=pathlib.Path("artifacts/cards/A3/cli_stdout_AB.json"); b=p.read_bytes()
assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
o=json.loads(b); assert "categories" in o and isinstance(o["categories"], list) and len(o["categories"])==1
c=o["categories"][0]; assert c.get("id")=="harmony" and c.get("band") in {"Cool","Open","Warm","Glow"}
print("NO_BOM_STDOUT_OK"); print("NO_ANSI_OK"); print("SHAPE_OK")
```

Negative and positive sidecar gate:
```bash
SIDECAR=artifacts/cards/A3/admin/sidecar.json
set +e; ./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --admin-out "$SIDECAR" >/dev/null; code=$?; set -e
test "$code" -eq 2 && echo GATE_MISUSE_OK; test ! -f "$SIDECAR"
HD_ADMIN=1 ./scripts/hdctl.py showcompat --a "$A" --a-tz Africa/Cairo --b "$B" --b-tz Africa/Cairo --showmath --admin-out "$SIDECAR" >/dev/null
stat -c '%a %n' "$SIDECAR" | grep '^600 ' && echo SIDECAR_MODE_0600_OK
python - <<'PY'
b=open("artifacts/cards/A3/admin/sidecar.json","rb").read()
assert b.endswith(b"\n")
print("SIDECAR_LF_OK")
PY
```

Preimage recompute:
```python
import json,hashlib,pathlib
from pathlib import Path
from sys import exit
o=json.loads(Path("artifacts/cards/A3/cli_stdout_AB.json").read_text(encoding="utf-8"))
pre=dict(o); pre.pop("idempotence_hash",None)
from json import dumps
canon=(dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
print("PREIMAGE_OK" if hashlib.sha256(canon).hexdigest()==o["idempotence_hash"] else "PREIMAGE_FAIL")
```

## 12. Appendix — Pair fingerprint rule
When a pair fingerprint is required in TS-v0:
- Compute `sha256( sercanon({"gates":[sorted unique ints]}) )` as lowercase hex.

## 13. Governance note
Acceptance delivery is a single revert-friendly commit to main with the evidence bundle under `artifacts/cards/A3`. No PRs for final acceptance. The PO performs the closeout.
