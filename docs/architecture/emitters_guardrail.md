# Public emitter guardrails (EPIC020)

## Canonical requirements
- Public surfaces (CLI and Reader) must route through `engine/presenter/emitter.py` and `engine/serializer/canon.py`.
- Canonical serializer rules: UTF-8, `ensure_ascii=False`, sorted keys, compact separators, exactly one trailing LF, arrays-as-sets, normalized channel ids.
- AB↔BA and two-run identity proofs are required for public envelopes.

## Forbidden in governed paths
The CLI guard enforces these rules; acceptance fails if they appear in governed CLI scope:
```
json.dumps(
jsonify(
orjson
ujson
simplejson
```
Use the canonical serializer instead. Run `python tools/cli/serializer_grep_guard.py` under closed rails to produce `artifacts/cli/guards/serializer_grep_guard.log`.

## Emitter symbol proof
`python tools/cli/emitter_symbol_proof.py` inspects governed CLI handlers (`showcompat` and allow-listed presenter paths) and records which canonical emitters they call. Output: `artifacts/cli/guards/emitter_symbol_proof.txt`.

## Determinism helper
Both guard scripts invoke `engine.runtime.determinism_env.ensure_determinism_env`, which pins `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`. Do not bypass these rails.

## Evidence posture
Guard outputs are governed evidence: index them via `tools/evidence/update_evidence_index.py` and validate path proofs and mirrors with the orientation demo and sanity pipeline. No manual edits. EPIC020 evidence families include `ERROR_*`, `PRESENTER_*`, and `INTVER_*` artifacts.
