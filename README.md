# Glow HD Engine — deterministic compat and evidence rails

The Glow HD Engine is a deterministic Human Design–driven matching and insight engine. After **HDE-EPIC018 (Calcination Pass 3)** the public and CLI surfaces share a single canonical emitter and serializer, run only under closed rails, and ship governed evidence with path proofs, mirrors, and epic-level manifests/close reports.

## Quickstart (closed rails)

All commands assume the pinned environment used by the determinism helper: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

```bash
python -m pip install -e .
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python -m engine.cli --help
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file fixtures/charts/pair.sample.json
```

- CLI and module-run are interchangeable (`hdctl …` is exposed via `engine.cli.main:cli`).
- Evidence runs must use the determinism helper (`engine.runtime.determinism_env.ensure_determinism_env`) which enforces the rails above.

## Determinism & evidence posture (EPIC018)

- **D1 – Canonical JSON:** `engine/serializer/canon.py` emits UTF-8, sorted keys, compact separators, and exactly one trailing LF. AB↔BA runs and two-run identity are required for public bodies.
- **D2 – Closed rails:** Determinism helper pins locale/timezone and disables network. Use it in CLI guards, evidence harnesses, and tests.
- **D3 – CLI guards:**
  - `python tools/cli/serializer_grep_guard.py` scans governed CLI paths for forbidden serializers and writes `artifacts/cli/guards/serializer_grep_guard.log`.
  - `python tools/cli/emitter_symbol_proof.py` proves governed CLI handlers call the canonical emitter and writes `artifacts/cli/guards/emitter_symbol_proof.txt`.
- **D4 – Evidence skeleton & sanity pipeline:**
  - Governed artifacts carry `.path_proof.txt` siblings, human index entries (`docs/evidence/INDEX.json`), and machine mirror entries (`artifacts/evidence_index.jsonl`).
  - Orientation demo: `python tools/evidence/orientation_demo.py` checks mirror self-proof posture.
  - Sanity pipeline: `python tools/evidence/run_sanity_pipeline.py` performs serializer parity checks, orientation, and evidence hygiene under closed rails.
  - Use `python tools/evidence/update_evidence_index.py` to refresh governed evidence indexes; **never edit index, mirror, proofs, manifest, or close reports by hand**.
- **D5 – Governed config artifacts:** Config artifacts (e.g., `config/bands_4B60_v1.json`, `config/toggles_v1.json`) are generated via `python tools/config/generate_config_artifacts.py` and mapped to acceptance tokens in `audit/EPIC-018_config_acceptance_map.json`.
- **D6 – Typed FE/BE bundles:** `python tools/config/generate_bundles.py` emits typed frontend/backend bundles aligned with governed config and registry, using schemas in `docs/schemas/config_bundle_{fe,be}.json`.
- **D7 – Manifest & close report:** EPIC018 governance is summarized in `audit/EPIC-018_MANIFEST.json` and `audit/EPIC-018_close_report.md` (both governed with path proofs); see PF20 — Phased Epics for canon context.

See PF12 — Schemas & Artifacts and PF19 — QA Guide for canonical process details.

## Config & bundles (D5/D6)

- Run `python tools/config/generate_config_artifacts.py` under closed rails to regenerate governed config artifacts; outputs must be indexed and path-proofed by the evidence tools.
- Run `python tools/config/generate_bundles.py` to produce typed FE/BE bundles that mirror the governed configs and registry. Bundle schemas live in `docs/schemas/` and are referenced by PF14 — Mechanics.
- The acceptance map `audit/EPIC-018_config_acceptance_map.json` links PF09 tasks to config artifacts and registry tokens; treat it as governed evidence.

## Deterministic CLI & reader surfaces

- Compat CLI: `hdctl showcompat --pair-file <pair.json>` (or `--a-file/--b-file`) emits numeric-free public JSON using the canonical emitter/serializer (AB↔BA identity, LF-terminated).
- Reader harness mirrors CLI bytes for the same inputs; APP_ENV gating remains in `engine/http/compat_handler.py`.
- `hdctl showcompat` accepts `--dump-reader` and `--dump-admin-dir` for QA sidecars; governed evidence follows the PF12 indexing rules.

## Evidence harness workflow

1. Ensure determinism rails are set (`ensure_determinism_env`).
2. Generate or refresh governed artifacts with the provided tools (CLI guards, config generators, bundles).
3. Update evidence indexes with `tools/evidence/update_evidence_index.py` (human index + machine mirror + path proofs).
4. Run `tools/evidence/orientation_demo.py` to verify mirror self-proof posture.
5. Run `tools/evidence/run_sanity_pipeline.py` for serializer parity, guard verification, and sanity log capture.
6. Confirm manifest/close-pack references before merging (EPIC-018 manifest and close report live under `audit/`).

## Epic018 close-pack

The EPIC018 manifest and close report document the acceptance map, tokens, and governed evidence roster for Calcination Pass 3. They are read-only and referenced from PF20 — Phased Epics and PF19 — QA Guide. Use them to locate tokens and artifacts; do not hand-edit.
