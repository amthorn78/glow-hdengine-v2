# Emitters (EPIC018)

## Public envelope
- Single canonical emitter: `engine/presenter/emitter.py` (`emit_public` / `emit_compact_json`).
- Canonical serializer: `engine/serializer/canon.py` (UTF-8, sorted keys, compact separators, one trailing LF, arrays-as-sets, channel normalization).
- Reader and CLI surfaces are required to share the emitter and serializer; AB↔BA and two-run identity proofs apply to all public bytes.

## Determinism rails
- Rails are enforced via `engine.runtime.determinism_env.ensure_determinism_env` (pins `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`). Use it in CLI guards, sanity pipeline, and evidence scripts.
- Emitter provenance is proven via CLI guard tools:
  - `tools/cli/serializer_grep_guard.py` (forbids ad-hoc JSON in governed CLI scope).
  - `tools/cli/emitter_symbol_proof.py` (proves governed CLI handlers call canonical emitters).

## Evidence coupling
- Governed artifacts using the emitter/serializer must carry `.path_proof.txt` files, human index entries, and machine mirror entries. Update with `tools/evidence/update_evidence_index.py` and validate with `tools/evidence/orientation_demo.py`.
- Sanity pipeline (`tools/evidence/run_sanity_pipeline.py`) asserts serializer parity, mirror posture, and LF termination for emitter outputs.

See PF12 — Schemas & Artifacts and PF05 — CLI/API/Vendor Ref for canonical rules (title references only).
