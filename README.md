# Glow HD Engine — Calcination evidence pass (EPIC021)

The Glow HD Engine is a deterministic Human Design engine and CLI that emits governed, canonically serialized bytes. After **HDE-EPIC021 — Calcination evidence pass**, the public stack keeps the EPIC020 separation surfaces and adds refreshed evidence posture: consolidated serializer/Reader parity, registry report governance, sanity pipeline wiring, and an EPIC021 QA harness with QA_ROOT logging. PF-Canon (titles only: PF05 — CLI/API/Vendor Ref, PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, PF20 — Phased Epics) remains authoritative.

## Overview

- Public Reader v1 and CLI share the canonical emitter and serializer for all success bytes; EPIC021 preserves AB↔BA and two-run identity proofs.
- Error responses use the canonical `error_v1` envelope with typed error tokens and JSON discipline.
- `/internal/version` remains an ops-only identity surface with a fixed six-field body and transport invariants; it is not a public API.
- Evidence posture includes a governed registry report, sanity pipeline outputs, Evidence Index/Mirror pairing, and EPIC021 QA_ROOT artifacts.

## Features

- **Compat/Reader outputs:** Public Reader v1 and CLI (`hdctl`) emit canonical JSON (UTF-8, sorted keys, compact separators, one trailing LF) using the shared presenter/emitter. AB↔BA and two-run identity proofs apply to public bytes; preimage recompute is preserved for identity parity.
- **CLI commands:**
  - `hdctl showcompat` (or `python -m engine.cli showcompat`) reads compat inputs from a pair file, separate `--a-file/--b-file`, or stdin. Successful runs print LF-terminated canonical JSON to stdout; errors print to stderr only and set exit codes (0 success, 2 typed failure, 64 argparse usage). Sidecar flags `--dump-reader` and `--dump-admin-dir` persist governed bytes.
  - `hdctl aux-preview` previews Aux narrative ids and optional text for a compat tuple using the sealed narrative pack.
  - `hdctl bg:resolve` provides a Phase S8a stub for BodyGraph resolution with vendor/db selection under closed rails.
  - Dev/admin sampler CLI remains available for QA-only flows (APP_ENV=dev) but is outside public scope.
- **Error handling:** Canonical `error_v1` envelopes with typed error tokens, LF discipline, and stdout/stderr separation for CLI. Error parity harnesses and schema checks are wired into governed evidence (`errors/*`, `parity/*`).
- **Presenter/emitter:** A single allow-listed emitter serves Reader HTTP and CLI, protecting canonical JSON bytes and LF termination. Presenter artifacts cover two-run and AB↔BA identity proofs plus preimage recompute under `artifacts/presenter/*`.
- **Internal identity:** `/internal/version` returns a fixed-order body `{engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id}` with GET/HEAD parity and conditional handling per PF14. Identity artifacts live under `artifacts/ops/internal_version/*` and `artifacts/math/*`.
- **Evidence posture:**
  - Registry report generator: `tools/generate_registry_report.py` emits `artifacts/registry/registry_report.json` with canonical serializer wiring.
  - Evidence Index (`docs/evidence/INDEX.json`) and machine Mirror (`artifacts/evidence_index.jsonl`) track governed artifacts with `.path_proof.txt` siblings; EPIC021 adds registry_report, sanity pipeline, and QA harness entries.
  - Sanity pipeline: `tools/evidence/run_sanity_pipeline.py` writes `artifacts/sanity/sanity.log` plus `.path_proof.txt`.
  - Evidence index updater: `tools/evidence/update_evidence_index.py` refreshes Index/Mirror bindings for new artifacts.
  - EPIC021 QA harness: `tools/qa/epic021_qa.py` writes QA_ROOT logs under `audit/qa/hde-epic021/` including bootstrap, step logs, and an acceptance-map viability check.

## Installation & requirements

Closed rails are the default for determinism, QA, and evidence:

```bash
python -m pip install -e .

# Closed rails pins (apply to commands below)
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
```

Use the determinism helper (`engine.runtime.determinism_env.ensure_determinism_env`) and `ci/checks/check_env_pins.sh` to verify pins when running CI or local suites.

## Quickstart

```bash
# CLI help
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python -m engine.cli --help

# Compat output via showcompat (stdout on success; stderr on errors)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file fixtures/charts/pair.sample.json

# Aux narrative preview for a compat tuple
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl aux-preview --pair-file artifacts/presenter/showcompat_identity_summary.json --category undefined --band Cool --perspective shared --show-narrative

# `/internal/version` identity probe (ops/internal only; mirrors evidence artifacts)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev curl -sSf http://localhost:8000/internal/version
```

- Dev Reader helper (`scripts/dev_start_reader.sh`) remains available for dev/test/local harnessing; APP_ENV gating applies.
- For in-depth behavior and schema details, refer to PF-Canon titles (PF05/PF12/PF14/PF19/PF20) and the non-canon docs under `docs/` (e.g., `docs/CLI_commands.md`, `docs/architecture/emitters.md`).

## QA & evidence

- **Evidence rails:** Governed artifacts require `.path_proof.txt` siblings plus entries in the Evidence Index/Mirror; avoid manual edits. Orientation demo (`tools/evidence/orientation_demo.py`) and sanity pipeline (`tools/evidence/run_sanity_pipeline.py`) validate mirror/posture and env pins.
- **Registry report:** `tools/generate_registry_report.py` emits `artifacts/registry/registry_report.json`; Evidence Index entries cover the report and its path proof.
- **Sanity pipeline:** `tools/evidence/run_sanity_pipeline.py` writes `artifacts/sanity/sanity.log` and `artifacts/sanity/sanity.log.path_proof.txt` under closed rails.
- **Evidence index and mirror:** `tools/evidence/update_evidence_index.py` refreshes `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`.
- **QA harness (EPIC021):** `tools/qa/epic021_qa.py` records QA_ROOT logs under `audit/qa/hde-epic021/` (bootstrap log, per-step logs, QA step manifest, acceptance-map viability log). Run under closed rails; set `EPIC021_QA_RUN_ID` to group artifacts.
- **Acceptance tracking:** EPIC021 acceptance map (`docs/acceptance_map_epic021.json`) and token evidence matrix (`audit/qa/hde-epic021/token_evidence_matrix.md`) summarize coverage; earlier epic acceptance maps remain available under `docs/acceptance_map_epic020.json`, `docs/acceptance_map_epic019.json`, and `docs/acceptance_map_epic017.json`.

## Notes and references

- Public surfaces remain limited to Reader v1 and CLI; dev/admin harnesses (e.g., sampler CLI, QA scripts) stay restricted to dev/test/local contexts.
- PF-Canon remains authoritative for mechanics, transport, and governance. Repo docs summarize behavior and point to canonical titles rather than duplicating specs.
