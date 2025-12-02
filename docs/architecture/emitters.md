# Emitters (EPIC019)

## Public envelope
- Single canonical emitter: `engine/presenter/emitter.py` (`emit_public` / `emit_compact_json`).
- Canonical serializer: `engine/serializer/canon.py` (UTF-8, sorted keys, compact separators, one trailing LF, arrays-as-sets, channel normalization).
- Reader, CLI, dev sampler harnesses, and Engine Core evidence generation share the emitter/serializer; AB↔BA and two-run identity proofs apply to all public bytes and sampler/core outputs.

## Determinism rails
- Rails are enforced via `engine.runtime.determinism_env.ensure_determinism_env` (pins `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`). Use it in CLI guards, sampler/core harnesses, sanity pipeline, and evidence scripts (env pins also gated by `ci/checks/check_env_pins.sh`).
- Emitter provenance is proven via CLI guard tools:
  - `tools/cli/serializer_grep_guard.py` (forbids ad-hoc JSON in governed CLI scope).
  - `tools/cli/emitter_symbol_proof.py` (proves governed CLI handlers call canonical emitters).

## Sampler and harness layering (EPIC019)
- Public surfaces: Reader v1 endpoints and `hdctl showcompat` share the emitter/serializer and remain the only public APIs.
- Dev/admin sampler surfaces: `hdctl dev:sampler` (APP_ENV=dev) and `/internal/dev/sampler` (APP_ENV=dev via `scripts/dev_start_reader.sh`) mirror public bytes for QA only.
- QA harnesses: closed-rails healthcheck and Live QA (`scripts/qa/dev_sampler_healthcheck.py`, `scripts/qa/dev_sampler_live_qa.py`) plus open-rails vendor Live QA (`scripts/qa/d6_live_vendor_qa.py`, controlled vendor identity). Outputs are governed evidence under `audit/qa/hde-epic019/` and are indexed into EPIC019 acceptance artifacts.


## Evidence coupling
- Governed artifacts using the emitter/serializer must carry `.path_proof.txt` files, human index entries, and machine mirror entries. Update with `tools/evidence/update_evidence_index.py` and validate with `tools/evidence/orientation_demo.py`.
- Sanity pipeline (`tools/evidence/run_sanity_pipeline.py`) asserts serializer parity, sampler/core harness outputs, mirror posture, and LF termination for emitter outputs.

See PF12 — Schemas & Artifacts and PF05 — CLI/API/Vendor Ref for canonical rules (title references only).
