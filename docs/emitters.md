# docs/architecture/emitters.md

**Title:** Single Emitter Canon — public JSON emission for CLI and Reader  
**Version:** 1.0  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Cards:** CORE-CLI-A3, CORE-READER-A5

## 1. Purpose
Define one canonical emitter used by both the CLI and the Reader dev harness. This prevents drift, locks the serializer and idempotence rules, and guarantees that the same inputs produce the same public bytes across tools.

## 2. Canonical module
- **Path:** `engine/emit_public.py`  
- **Signature:** `emit_public_envelope(a_chart, b_chart, engine_tag, invocation_tag, release_id) -> bytes`  
- **Contract:** Returns LF-terminated UTF-8 bytes produced by the canonical serializer over the minimal public JSON envelope.

### 2.1 Public envelope shape
The emitter must construct the same minimal Reader-shaped JSON that the CLI and Reader serve.
- Top-level fields:
  - `eligible` — boolean
  - `categories` — array with exactly one item: `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`
  - `meta` — object with `engine_tag` and `invocation_tag`
  - `release_id` — 64-hex string from `scripts/release_id.sh` applied to `release/manifest.sorted.json`
  - `idempotence_hash` — 64-hex string as defined below
- Output must end with exactly one `\n`. No BOM. No ANSI. Numeric-free and bands-only.

## 3. Canonical serializer
Use one serializer everywhere that produces public bytes.
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```

## 4. Idempotence preimage rule
The emitter is responsible for coupling the bytes to a deterministic preimage.
1) Build the envelope fields except `idempotence_hash`.  
2) Compute `idempotence_hash = sha256( sercanon(preimage_without_hash) ).hexdigest()` as lowercase hex.  
3) Insert `idempotence_hash` into the object.  
4) Serialize with `sercanon(final)` and return the bytes.

## 5. AB and BA parity
The emitter must produce public bytes that are identical when the two inputs are swapped. The CLI and Reader rely on this property for acceptance.

## 6. Purity and safety rules
- No import-time I/O. The module must not read files or environment variables at import time.  
- No network access. The emitter is pure with respect to inputs.  
- Logs are keys-only when present. Never include secrets.  
- The emitter must not write files. Only return bytes to the caller.

## 7. Reader and CLI usage
Both tools must import and use this module. Do not reimplement serializer or idempotence logic anywhere else.
- **CLI:** `hdctl showcompat` uses `emit_public_envelope(...)` for stdout.  
- **Reader v1:** the HTTP handler calls the same function then writes headers and the bytes to the response body.

### 7.1 Example usage
```python
from engine.emit_public import emit_public_envelope

# a_chart and b_chart are already validated and normalized dicts
public_bytes = emit_public_envelope(
    a_chart=a_chart,
    b_chart=b_chart,
    engine_tag="hdengine-alpha",
    invocation_tag="INV-C9F3AFB03805F430",
    release_id=open("artifacts/cards/A3/release_id.txt").read().strip()
)
# CLI: write to stdout; Reader: write to HTTP response
```

## 8. Provenance and evidence
Acceptance must record the emitter source hash to prove single-source usage.
```bash
sha256sum engine/emit_public.py | awk '{print $1}' | sed 's/^/EMITTER_SHA256=/' >> artifacts/cards/A5/validation.log
```
Recommended markers:
```
NO_DUPLICATE_SERIALIZER_OK
EMITTER_IMPORT_OK
EMITTER_SHA256=<64hex>
```

## 9. Unit tests and golden checks
- Two-run identity on the same inputs.  
- AB to BA byte identity.  
- Preimage recompute equals embedded `idempotence_hash`.  
- Final text is LF-terminated and BOM-free.  
- Minimal shape is present and numeric-free.  
- Reader equals CLI for the same charts and time zones.

## 10. Change control
- Do not change public fields in Alpha. Any change requires a coordinated card and acceptance refresh.  
- New internal fields belong in the admin sidecar, not in the public envelope.  
- When the emitter changes, update the provenance marker and rerun acceptance for A3 and A5.

## 11. Appendix
**Invocation tag regex:** `^INV-[0-9A-F]{16,64}$`  
**LF rule:** return value must end with a single `\n`  
**Serializer reminders:** `sort_keys=True`, `separators=(',',':')`, `ensure_ascii=False`
