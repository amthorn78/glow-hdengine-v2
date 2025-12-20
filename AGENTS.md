# AGENTS.md — Glow HD Engine (agent rules)

## Scope and hierarchy
- This file governs all agents in the repo; PF-Canon remains the source of truth (see `docs/pfcanon/`, titles such as PF05 — CLI/API/Vendor Ref, PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, PF20 — Phased Epics). Where this file and PF-Canon diverge, PF-Canon wins.
- Governed evidence (INDEX/mirror/path proofs/orientation/manifest/close report/config acceptance map) must be produced only by the canonical tools. **Never hand-edit governed artifacts.**

## Agent roster (repo-facing)
- **Lead Dev / Product Owner:** approves epic scopes and evidence plans; owns acceptance maps/manifests and public/ops surface sign-off. Touches docs and governance bindings (acceptance maps, manifests, close reports).
- **Codex / dev agents:** implement features/docs/evidence under PO direction; run CLI guards and harnesses under closed rails; maintain the dev Reader helper (`scripts/dev_start_reader.sh`) and DEV_SAMPLER_URL wiring (dev/test/local only). Touch code, docs, and governed evidence generators.
- **Evidence harness:** runs `tools/generate_registry_report.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/orientation_demo.py`, `tools/evidence/run_sanity_pipeline.py`, epic-specific generators (including `tools/cli/generate_showcompat_artifacts.py` for EPIC022 D2), and keeps `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` aligned with `.path_proof.txt` siblings.
- **Config/bundle agents:** run `tools/config/generate_config_artifacts.py` and `tools/config/generate_bundles.py`; confirm `audit/EPIC-018_config_acceptance_map.json` stays consistent with generated artifacts and path proofs.
- **QA/Verifier:** executes the sanity pipeline, env-pins gate, EPIC020 deterministic suites (error envelope, presenter, `/internal/version`), the registry report generator, EPIC021 QA harness (`tools/qa/epic021_qa.py`), and EPIC022 acceptance scaffolding. Confirms tokens and evidence coverage in manifests/acceptance maps and updates Index/Mirror.
- **Doc agents:** refresh README/CHANGELOG/AGENTS/docs to reflect PF-Canon titles and epic outcomes; include rails/guardrails for determinism and evidence, dev vs public surfaces, and closed-rails posture for EPIC020–EPIC022.

## Operating workflow (closed rails, evidence discipline)
- Closed rails default: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` enforced by `engine.runtime.determinism_env.ensure_determinism_env` and checked via `ci/checks/check_env_pins.sh`. No network access for public/QA surfaces unless explicitly allowed for a governed harness.
- Read-first, then edit: inspect acceptance bindings, evidence indexes, and QA harness expectations before changing docs/code/evidence.
- Governed evidence rules:
  - Use only repo tools to regenerate governed artifacts. Examples: CLI guards (`python tools/cli/serializer_grep_guard.py`, `python tools/cli/emitter_symbol_proof.py`), registry report (`python tools/generate_registry_report.py`), showcompat D2 capture (`python tools/cli/generate_showcompat_artifacts.py`), orientation demo (`python tools/evidence/orientation_demo.py`), sanity pipeline (`python tools/evidence/run_sanity_pipeline.py`), Evidence Index updater (`python tools/evidence/update_evidence_index.py`), mirror schema check (`python ci/checks/check_mirror_schema.sh`).
  - Refresh Index/Mirror pairs (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`) and confirm `.path_proof.txt` siblings exist for every governed artifact. Run `update_evidence_index.py` (write) before `orientation_demo.py` (write), then their `--check` variants, and finish with the mirror schema check. Mirror path proofs include `mirror_body_sha256` for the self-record; do not hand-edit or drop the self-record row.
  - Verify acceptance bindings: EPIC018 manifest/close report under `audit/`; EPIC019/EPIC020/EPIC021/EPIC022 acceptance maps under `docs/`; token matrices under `audit/qa/hde-epic021/` and `audit/qa/hde-epic022/`.
- **No manual edits** to evidence indexes, path proofs, manifests, close reports, acceptance maps, or orientation artifacts.

## EPIC022 lessons (anti-drift)
- Deterministic scenarios first: parity/error envelopes and showcompat captures must run under pinned rails (no “environment roulette”) with stdout/stderr separation proven by tests and governed artifacts.
- Acceptance artifacts stay single-source: token matrices and acceptance maps must bind to concrete evidence/tests (no duplicate rows or placeholder evidence once concrete artifacts exist); showcompat D2 captures stay indexed with sha256 sidecars and path proofs; `/internal/version` D3 bundles and the close-pack (manifest + close report + sanity log) are present and must not be claimed as missing. PF05 exit-code taxonomy remains canonical even while repo tests pin showcompat vendor/engine errors to exit 1; PF20 D3 references a provenance note while implementation follows the PF10 posture (governed two-run/coupling log) — document the mismatch when relevant.
