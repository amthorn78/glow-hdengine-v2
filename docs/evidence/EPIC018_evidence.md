# Evidence posture — EPIC018

## Skeleton (PF12 — Schemas & Artifacts)
- Governed artifacts require: payload + `.path_proof.txt` + entries in `docs/evidence/INDEX.json` (human) and `artifacts/evidence_index.jsonl` (machine mirror).
- Machine mirror entries include self-records; orientation demo verifies mirror self-proof and path proof discipline.

## Orientation demo
- Command: `python tools/evidence/orientation_demo.py`
- Checks: mirror body hash, path proof presence, and mirror self-record coherence. `status: ok` indicates orientation parity; mismatches/drift fail acceptance.

## Sanity pipeline
- Command: `python tools/evidence/run_sanity_pipeline.py`
- Runs determinism env check, serializer parity, guard verification, orientation demo, and writes `sanity.log` under governed rails.

## Evidence updates
- Command: `python tools/evidence/update_evidence_index.py`
- Purpose: updates human index and machine mirror with new governed artifacts; refuses to run without determinism rails.
- Manual edits to indexes, mirrors, path proofs, manifest, or close reports are forbidden.

## Tokens and acceptance
- EPIC018 tokens and artifact roster are cataloged in `audit/EPIC-018_MANIFEST.json` and `audit/EPIC-018_close_report.md` (path-proofed). Use these to map tokens to artifacts; do not modify them directly.

## Rails
- All evidence commands run under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` via `engine.runtime.determinism_env.ensure_determinism_env`.

See PF19 — QA Guide for the governing QA process (title reference only).
