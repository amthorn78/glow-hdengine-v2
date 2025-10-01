# docs/architecture/emitters.md

**Title:** Single Emitter Canon — public JSON emission for CLI and Reader  
**Version:** 1.2  
**Owner:** Cyrano (Tech Writer)  
**Status:** Canon  
**Cards:** CORE-CLI-A3, CORE-READER-A5

## 1. Purpose
Define one canonical emitter used by both the CLI and the Reader dev harness. This prevents drift, locks the serializer and idempotence rules, and guarantees that the same inputs produce the same public bytes across tools.

## 2. Canonical module
- **Path:** `engine/emit_public.py`  
- **Signature:** `emit_public_envelope(a_chart, b_chart, engine_tag, invocation_tag, release_id) -> bytes`  
- **Contract:** Returns LF-terminated UTF-8 bytes produced by the canonical serializer over the minimal public JSON envelope.

### 2.1 Public envelope (A3/A5)
The emitter MUST construct the minimal public JSON used by CLI and Reader.
- Top-level keys (canonical set and order for byte tests):  
  `["categories","eligible","idempotence_hash","meta","release_id"]`
- `categories` is an array with **exactly one** element whose **only** fields are `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`.
- Output MUST end with exactly one `\n`. No BOM. No ANSI. Numeric-free and bands-only.

## 3. Canonical serializer
Use one serializer everywhere that produces public bytes.
```python
import json
def sercanon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"
```

## 4. Idempotence preimage
The emitter is responsible for coupling the bytes to a deterministic preimage:
1) Build the envelope except `idempotence_hash`.  
2) Compute `idempotence_hash = sha256( sercanon(preimage_without_hash) ).hexdigest()` (lowercase hex).  
3) Insert `idempotence_hash`.  
4) Serialize with `sercanon(final)` and return bytes.

## 5. AB↔BA parity
Swapping inputs MUST NOT change the public bytes. CLI and Reader acceptance depend on this property.

## 6. Purity and safety
- No import-time I/O. No environment reads at import.  
- No network access. Pure function of inputs.  
- No file writes. Only return bytes to caller.  
- Logs (if any) MUST be keys-only and NOT contain secrets.

## 7. Tooling usage
- **CLI (`hdctl showcompat`)** MUST call `emit_public_envelope(...)` to produce stdout bytes.  
- **Reader v1** MUST call the same function and write headers plus these bytes to the HTTP response body.

### 7.1 Example usage
```python
from engine.emit_public import emit_public_envelope

# a_chart and b_chart are validated and normalized dicts
public_bytes = emit_public_envelope(
    a_chart=a_chart,
    b_chart=b_chart,
    engine_tag="hdengine-alpha",
    invocation_tag="INV-C9F3AFB03805F430",
    release_id=open("artifacts/cards/A3/release_id.txt").read().strip()
)
# CLI: write to stdout; Reader: write to HTTP response
```

## 8. Provenance (acceptance evidence)
Record the emitter source hash to prove single-source usage:
```bash
sha256sum engine/emit_public.py | awk '{print $1}' | sed 's/^/EMITTER_SHA256=/' >> artifacts/cards/A5/validation.log
```
Markers:
```
NO_DUPLICATE_SERIALIZER_OK
EMITTER_IMPORT_OK
EMITTER_SHA256=<64hex>
```

## 9. Unit tests and goldens
- Two-run identity on same inputs.  
- AB↔BA byte identity.  
- Preimage recompute equals embedded `idempotence_hash`.  
- Final text ends with a single LF and is BOM-free.  
- Minimal envelope shape present and numeric-free.  
- Reader bytes == CLI bytes for identical inputs.

## 10. Change control
- Public envelope is **frozen for A3/A5**. Any change requires a card and refreshed acceptance evidence.  
- New internal fields belong in the admin sidecar, not in the public envelope.  
- When the emitter changes, update provenance markers and re-run A3 and A5 acceptance.

## 11. Appendix
**Invocation tag regex:** `^INV-[0-9A-F]{16,64}$`  
**LF rule:** returned bytes MUST end with exactly one `\n`.  
**Serializer:** `sort_keys=True`, `separators=(',',':')`, `ensure_ascii=False`
