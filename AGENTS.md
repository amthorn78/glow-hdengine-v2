# AGENTS.md — Glow HD Engine (agent rules)

## Scope and hierarchy
- This file governs all agents in the repo; PF-Canon remains the source of truth (see `docs/pfcanon/`, titles such as PF05 — CLI/API/Vendor Ref, PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, PF20 — Phased Epics). Where this file and PF-Canon diverge, PF-Canon wins.
- Governed evidence (INDEX/mirror/path proofs/orientation/manifest/close report/config acceptance map) must be produced only by the canonical tools. **Never hand-edit governed artifacts.**

## Roles and responsibilities
- **Lead Dev / Product Owner:** approves epic scopes and evidence plans, keeps acceptance maps/manifests coherent, and signs off on public/ops surfaces before close. EPIC021 close-out references acceptance artifacts under `docs/acceptance_map_epic021.json` and `audit/qa/hde-epic021/`.
- **Codex / dev agents:** implement features/docs/evidence under PO direction, run CLI guards and harnesses under closed rails, and ensure determinism helper + env pins are honored; own the dev Reader helper (`scripts/dev_start_reader.sh`) and DEV_SAMPLER_URL wiring for dev/test/local only.
- **Evidence harness:** runs `tools/generate_registry_report.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/orientation_demo.py`, `tools/evidence/run_sanity_pipeline.py`, and epic-specific generators; keeps `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in sync with path proofs and current acceptance bindings (EPIC021 registry_report/sanity entries plus EPIC020 error/presenter/internal-version families under `errors/`, `parity/`, `artifacts/presenter/`, `artifacts/ops/internal_version/`).
- **Config/bundle agents:** run `tools/config/generate_config_artifacts.py` and `tools/config/generate_bundles.py`; confirm `audit/EPIC-018_config_acceptance_map.json` remains consistent with generated artifacts.
- **QA/Verifier:** executes the sanity pipeline, env-pins gate, EPIC020 deterministic suites (error envelope, presenter, `/internal/version`), the registry report generator, and EPIC021 QA harness (`tools/qa/epic021_qa.py`); confirms tokens and evidence coverage in manifests/acceptance maps and updates Index/Mirror as needed.
- **Doc agents:** refresh README/CHANGELOG/AGENTS/docs to reflect PF-Canon titles and epic outcomes; include rails/guardrails for determinism and evidence, dev vs public surfaces, and closed-rails posture for EPIC020/EPIC021 (no new open-rails scopes).

## Rails (closed posture)
- Environment pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` (enforced by `engine.runtime.determinism_env.ensure_determinism_env` and checked via `ci/checks/check_env_pins.sh`). EPIC020 CI runs under these pins.
- Use the canonical emitter and serializer (`engine/presenter/emitter.py`, `engine/serializer/canon.py`) for all public bytes; CLI and Reader share the presenter/emitter (including `showcompat` canonical JSON). AB↔BA and two-run identity proofs remain required.
- CLI guard tools:
  - `python tools/cli/serializer_grep_guard.py` → `artifacts/cli/guards/serializer_grep_guard.log`
  - `python tools/cli/emitter_symbol_proof.py` → `artifacts/cli/guards/emitter_symbol_proof.txt`
- Evidence tools: orientation demo, registry report generator, sanity pipeline, and evidence index updater listed above. Rails are closed for all runs; EPIC020-specific artifacts cover error envelopes, presenter identity proofs, and `/internal/version` identity runs; EPIC021 artifacts cover registry_report, sanity pipeline, and QA harness outputs.

## Workflows
- **Before merging governed changes (code, config, or docs touching evidence):**
  1) Pin environment (rails above) and run CLI guards.
  2) Regenerate governed artifacts (config, bundles, sampler/core evidence, guard logs, registry_report, sanity pipeline, QA harness outputs) with the provided tools.
  3) Refresh indexes with `tools/evidence/update_evidence_index.py` and confirm `.path_proof.txt` siblings are present.
  4) Run `tools/evidence/orientation_demo.py` and `tools/evidence/run_sanity_pipeline.py`; review `sanity.log` and env-pin results.
  5) Verify manifest/acceptance map references (EPIC-018 manifest/close report under `audit/`; EPIC019/EPIC020/EPIC021 acceptance maps under `docs/`; EPIC021 token matrix under `audit/qa/hde-epic021/`).
- **No manual edits** to: evidence indexes, path proofs, manifest/close reports, acceptance maps, orientation artifacts, or config acceptance map.

## Entrypoints and references
- CLI help: `python -m engine.cli --help` or `hdctl --help` (same entrypoint).
- Reader harness: `adapter/http_reader.py` (APP_ENV gating applies).
- Determinism helper: `engine/runtime/determinism_env.py` (pins locale/timezone/network posture).
- Config artifacts: generated into `config/`; bundle schemas live in `docs/schemas/`.

## Ownership reminders
- Epic-level governance is captured in the EPIC018 manifest and close report; do not change ordering or evidence semantics without a new epic.
- PF-Canon titles remain the authoritative process references; repo docs are supplements only.
