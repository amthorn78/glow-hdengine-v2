# Evidence posture — EPIC018/EPIC019

## Skeleton (PF12 — Schemas & Artifacts)
- Governed artifacts require: payload + `.path_proof.txt` + entries in `docs/evidence/INDEX.json` (human) and `artifacts/evidence_index.jsonl` (machine mirror).
- Machine mirror entries include self-records; orientation demo verifies mirror self-proof and path proof discipline.
- EPIC019 sampler and Engine Core artifacts follow the same PF12 discipline with schemas under `docs/schemas/sampler/` and `docs/schemas/core/`.

## Orientation demo
- Command: `python tools/evidence/orientation_demo.py`
- Checks: mirror body hash, path proof presence, and mirror self-record coherence. `status: ok` indicates orientation parity; mismatches/drift fail acceptance.

## Sanity pipeline
- Command: `python tools/evidence/run_sanity_pipeline.py`
- Runs determinism env check, serializer parity, sampler evidence generator, Engine Core evidence generator, guard verification, orientation demo, and writes `sanity.log` under governed rails.

## Evidence updates
- Command: `python tools/evidence/update_evidence_index.py`
- Purpose: updates human index and machine mirror with new governed artifacts; refuses to run without determinism rails.
- Manual edits to indexes, mirrors, path proofs, manifest, or close reports are forbidden.
- Sampler evidence generator: `python tools/evidence/generate_sampler_evidence.py` (dev sampler CLI/HTTP harness, diversity/seed replay/ABBA/two-run identity).
- Engine Core evidence generator: `python tools/evidence/generate_engine_core_evidence.py` (purity, JSON compare, ABBA/two-run identity).

## Tokens and acceptance
- EPIC018 tokens and artifact roster are cataloged in `audit/EPIC-018_MANIFEST.json` and `audit/EPIC-018_close_report.md` (path-proofed). Use these to map tokens to artifacts; do not modify them directly.
- EPIC019 sampler/core tokens are recorded in `docs/acceptance_map_epic019.json` with a path proof and summarized in `docs/acceptance_maps.json`; tokens are Green with INDEX/Mirror coverage for sampler/core families.

## Rails
- All evidence commands run under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` via `engine.runtime.determinism_env.ensure_determinism_env`; env pins are also checked in CI via `ci/checks/check_env_pins.sh`.

See PF19 — QA Guide for the governing QA process (title reference only).
