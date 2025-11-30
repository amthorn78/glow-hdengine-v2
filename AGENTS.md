# AGENTS.md — Glow HD Engine (agent rules)

## Scope and hierarchy
- This file governs all agents in the repo; PF-Canon remains the source of truth (see `docs/pfcanon/`, titles such as PF12 — Schemas & Artifacts, PF19 — QA Guide, PF20 — Phased Epics). Where this file and PF-Canon diverge, PF-Canon wins.
- Governed evidence (INDEX/mirror/path proofs/orientation/manifest/close report/config acceptance map) must be produced only by the canonical tools. **Never hand-edit governed artifacts.**

## Roles and responsibilities
- **Lead Dev:** approves implementation/evidence plans, keeps acceptance maps/manifests coherent, and signs off on sampler + Engine Core scope (EPIC019) before close.
- **Codex / dev agents:** implement features/docs/evidence under PO direction, run CLI guards and sampler/core harnesses under closed rails, and ensure determinism helper + env pins are honored.
- **Evidence harness:** runs `tools/evidence/update_evidence_index.py`, `tools/evidence/orientation_demo.py`, `tools/evidence/run_sanity_pipeline.py`, `tools/evidence/generate_sampler_evidence.py`, and `tools/evidence/generate_engine_core_evidence.py`; keeps `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in sync with path proofs and EPIC019 acceptance bindings.
- **Config/bundle agents:** run `tools/config/generate_config_artifacts.py` and `tools/config/generate_bundles.py`; confirm `audit/EPIC-018_config_acceptance_map.json` remains consistent with generated artifacts.
- **QA/Verifier:** executes the sanity pipeline, env-pins gate, and sampler/core harness tests; confirms tokens and evidence coverage in manifests/acceptance maps and updates Index/Mirror as needed.
- **Doc agents:** refresh README/CHANGELOG/AGENTS/docs to reflect PF-Canon titles and EPIC outcomes; include rails and guardrails for determinism and evidence, especially sampler/core families and env-pin posture.

## Rails (EPIC019 closed posture)
- Environment pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` (enforced by `engine.runtime.determinism_env.ensure_determinism_env` and checked via `ci/checks/check_env_pins.sh`).
- Use the canonical emitter and serializer (`engine/presenter/emitter.py`, `engine/serializer/canon.py`) for all public bytes; CLI, Reader, sampler harnesses, and Engine Core outputs must remain byte-identical (AB↔BA, two-run identity).
- CLI guard tools:
  - `python tools/cli/serializer_grep_guard.py` → `artifacts/cli/guards/serializer_grep_guard.log`
  - `python tools/cli/emitter_symbol_proof.py` → `artifacts/cli/guards/emitter_symbol_proof.txt`
- Sampler/core evidence tools:
  - `python tools/evidence/generate_sampler_evidence.py` (dev-only sampler CLI/HTTP harness runs, diversity + seed replay evidence)
  - `python tools/evidence/generate_engine_core_evidence.py` (Engine Core purity/identity/ABBA evidence)
- Evidence tools: orientation demo, sanity pipeline (includes sampler/core runs), and evidence index updater listed above. Rails are closed for all runs.

## Workflows
- **Before merging governed changes (code, config, or docs touching evidence):**
  1) Pin environment (rails above) and run CLI guards.
  2) Regenerate governed artifacts (config, bundles, sampler/core evidence, guard logs) with the provided tools.
  3) Refresh indexes with `tools/evidence/update_evidence_index.py` and confirm `.path_proof.txt` siblings are present.
  4) Run `tools/evidence/orientation_demo.py` and `tools/evidence/run_sanity_pipeline.py`; review `sanity.log` and env-pin results.
  5) Verify manifest/acceptance map references (EPIC-018 manifest/close report under `audit/`; EPIC019 acceptance map under `docs/`).
- **No manual edits** to: evidence indexes, path proofs, manifest/close reports, acceptance maps, orientation artifacts, or config acceptance map.

## Entrypoints and references
- CLI help: `python -m engine.cli --help` or `hdctl --help` (same entrypoint).
- Reader harness: `adapter/http_reader.py` (APP_ENV gating applies).
- Determinism helper: `engine/runtime/determinism_env.py` (pins locale/timezone/network posture).
- Config artifacts: generated into `config/`; bundle schemas live in `docs/schemas/`.

## Ownership reminders
- Epic-level governance is captured in the EPIC018 manifest and close report; do not change ordering or evidence semantics without a new epic.
- PF-Canon titles remain the authoritative process references; repo docs are supplements only.
