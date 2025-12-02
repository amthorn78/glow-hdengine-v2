# Glow HD Engine — deterministic sampler + Engine Core rails

The Glow HD Engine is a deterministic Human Design–driven matching and insight engine. After **HDE-EPIC019 (Dissolution Pass 2)** the engine layers now include a deterministic sampler core (HDE-DISS003) and Engine Core (HDE-DISS004) alongside the established compat stack. Public surfaces and dev/admin harnesses share the canonical emitter/serializer, run only under closed rails, and ship governed evidence with path proofs, mirrors, and epic-level manifests/close reports.

## Quickstart (closed rails)

All commands assume the pinned environment used by the determinism helper: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

```bash
python -m pip install -e .
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python -m engine.cli --help
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file fixtures/charts/pair.sample.json

# Dev/admin-only sampler harnesses (do not use in production):
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev hdctl dev:sampler --viewer viewer-001 --candidates-file path/to/candidates.json --seed seed-1
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh  # exposes /internal/dev/sampler
```

- CLI and module-run are interchangeable (`hdctl …` is exposed via `engine.cli.main:cli`).
- Evidence runs must use the determinism helper (`engine.runtime.determinism_env.ensure_determinism_env`) which enforces the rails above.
- Dev/admin sampler flows (CLI + HTTP) are gated to APP_ENV=dev and exist for QA only; production surfaces remain compat Reader v1.

## Determinism & evidence posture (EPIC019)

- **D1 – Canonical JSON:** `engine/serializer/canon.py` emits UTF-8, sorted keys, compact separators, and exactly one trailing LF. AB↔BA runs and two-run identity are required for public bodies, sampler outputs, and Engine Core results.
- **D2 – Closed rails + env pins:** Determinism helper pins locale/timezone and disables network. The env-pins gate (`ci/checks/check_env_pins.sh`) guards docs/tests for `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.
- **D3 – CLI guards:**
  - `python tools/cli/serializer_grep_guard.py` scans governed CLI paths for forbidden serializers and writes `artifacts/cli/guards/serializer_grep_guard.log`.
  - `python tools/cli/emitter_symbol_proof.py` proves governed CLI handlers call the canonical emitter and writes `artifacts/cli/guards/emitter_symbol_proof.txt`.
- **D4 – Evidence skeleton & sanity pipeline:**
  - Governed artifacts carry `.path_proof.txt` siblings, human index entries (`docs/evidence/INDEX.json`), and machine mirror entries (`artifacts/evidence_index.jsonl`).
  - Orientation demo: `python tools/evidence/orientation_demo.py` checks mirror self-proof posture.
  - Sanity pipeline: `python tools/evidence/run_sanity_pipeline.py` performs serializer parity checks, sampler/core harness runs, orientation, and evidence hygiene under closed rails.
  - Use `python tools/evidence/update_evidence_index.py` to refresh governed evidence indexes; **never edit index, mirror, proofs, manifest, or acceptance maps by hand**.
- **Sampler evidence (HDE-DISS003):** `python tools/evidence/generate_sampler_evidence.py` exercises sampler core plus dev CLI/HTTP harnesses (seeded runs, diversity checks, ABBA/two-run identity) and writes governed artifacts under `artifacts/sampler/` with schemas in `docs/schemas/sampler/`.
- **Engine Core evidence (HDE-DISS004):** `python tools/evidence/generate_engine_core_evidence.py` exercises pure-compute core parity (purity, two-run identity, ABBA, JSON compare) with governed outputs under `artifacts/core/` and schemas in `docs/schemas/core/`.
- **D5 – Governed config artifacts:** Config artifacts (e.g., `config/bands_4B60_v1.json`, `config/toggles_v1.json`) are generated via `python tools/config/generate_config_artifacts.py` and mapped to acceptance tokens in `audit/EPIC-018_config_acceptance_map.json`.
- **D6 – Typed FE/BE bundles:** `python tools/config/generate_bundles.py` emits typed frontend/backend bundles aligned with governed config and registry, using schemas in `docs/schemas/config_bundle_{fe,be}.json`.
- **Epic manifests & acceptance maps:** EPIC018 governance remains in `audit/EPIC-018_MANIFEST.json` / `audit/EPIC-018_close_report.md`. EPIC019 adds sampler/core acceptance mapping in `docs/acceptance_map_epic019.json` (with path proof) and closes tokens in `docs/acceptance_maps.json`; see PF20 — Phased Epics for canon context.

See PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, and PF20 — Phased Epics for canonical process details.

## Config & bundles (D5/D6)

- Run `python tools/config/generate_config_artifacts.py` under closed rails to regenerate governed config artifacts; outputs must be indexed and path-proofed by the evidence tools.
- Run `python tools/config/generate_bundles.py` to produce typed FE/BE bundles that mirror the governed configs and registry. Bundle schemas live in `docs/schemas/` and are referenced by PF14 — Mechanics.
- The acceptance map `audit/EPIC-018_config_acceptance_map.json` links PF09 tasks to config artifacts and registry tokens; treat it as governed evidence.

## Deterministic CLI & reader surfaces

- Compat CLI: `hdctl showcompat --pair-file <pair.json>` (or `--a-file/--b-file`) emits numeric-free public JSON using the canonical emitter/serializer (AB↔BA identity, LF-terminated).
- Dev-only sampler CLI: `APP_ENV=dev hdctl dev:sampler --viewer <viewer_id> --candidates-file <candidates.json> [--seed <seed>]` emits deterministic sampler JSON under closed rails for QA only.
- Reader harness mirrors CLI bytes for the same inputs; APP_ENV gating remains in `engine/http/compat_handler.py`. A dev-only sampler endpoint lives at `/internal/dev/sampler` (APP_ENV=dev) for QA parity with the sampler CLI.

### Dev sampler HTTP harness (dev/admin-only)

- Canonical dev Reader start command: `APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev_start_reader.sh` (binds to port 8000; uses `python -m adapter.http_reader`).
- Infra-owned URL binding: `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` (exported in `.devcontainer/devcontainer.json`).
- Healthcheck/diagnostic harness: `scripts/qa/dev_sampler_healthcheck.py` starts the Reader, posts a minimal payload under APP_ENV=dev (expects 200), then records the APP_ENV=prod gate result for follow-up (logs in `notes/dev-sampler/dev_sampler_healthcheck.log`).
- `hdctl showcompat` accepts `--dump-reader` and `--dump-admin-dir` for QA sidecars; governed evidence follows the PF12 indexing rules.

## Evidence harness workflow

1. Ensure determinism rails are set (`ensure_determinism_env`).
2. Generate or refresh governed artifacts:
   - CLI guards (`tools/cli/serializer_grep_guard.py`, `tools/cli/emitter_symbol_proof.py`).
   - Config/bundle generators (`tools/config/generate_config_artifacts.py`, `tools/config/generate_bundles.py`).
   - Sampler evidence (`tools/evidence/generate_sampler_evidence.py`) and Engine Core evidence (`tools/evidence/generate_engine_core_evidence.py`).
3. Update evidence indexes with `tools/evidence/update_evidence_index.py` (human index + machine mirror + path proofs).
4. Run `tools/evidence/orientation_demo.py` to verify mirror self-proof posture.
5. Run `tools/evidence/run_sanity_pipeline.py` for serializer parity, sampler/core harness checks, env-pin validation, and sanity log capture.
6. Confirm manifest/acceptance map references before merging (EPIC-018 manifest, EPIC019 acceptance map, and EPIC-018 close report live under `audit/` and `docs/`).

## Epic acceptance references

- EPIC018: manifest and close report document Calcination Pass 3; read-only governed artifacts under `audit/`.
- EPIC019: sampler/core acceptance is captured in `docs/acceptance_map_epic019.json` with a path proof and is summarized in `docs/acceptance_maps.json`. Tokens are green with indexed evidence for sampler/core families.

See PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, and PF20 — Phased Epics for canonical process details.
