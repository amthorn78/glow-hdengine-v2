# Glow HD Engine — Separation Pass 1 (EPIC020) surfaces

The Glow HD Engine is a deterministic Human Design engine and CLI that emits governed, canonically serialized bytes. After **HDE-EPIC020 — Separation Pass 1 (Error & Identity Surfaces)**, the public stack exposes a separation-grade surface area: canonical error envelopes and tokens, a single allow-listed presenter/emitter, and an internal identity endpoint with fixed-order fields. Evidence remains governed through PF-Canon rails (see PF05 — CLI/API/Vendor Ref, PF12 — Schemas & Artifacts, PF14 — Mechanics Guide, PF19 — QA Guide, PF20 — Phased Epics; titles only).

## Overview

- Public Reader v1 and CLI share the canonical emitter and serializer for all success bytes.
- Error responses use the canonical `error_v1` envelope with typed error tokens and JSON discipline.
- `/internal/version` is an ops-only identity surface with a fixed six-field body and transport invariants; it is not a public API.
- Determinism and evidence posture are enforced through closed rails, governed artifacts, and Evidence Index/Mirror pairing.

## Features

- **Compat/Reader outputs:** Public Reader v1 and CLI (`hdctl`) emit canonical JSON (UTF-8, sorted keys, compact separators, one trailing LF) using the shared presenter/emitter. AB↔BA and two-run identity proofs apply to public bytes; preimage recompute is preserved for identity parity.
- **CLI commands:**
  - `hdctl showcompat` (or `python -m engine.cli showcompat`) reads compat inputs from a pair file, separate `--a-file/--b-file`, or stdin. Successful runs print LF-terminated canonical JSON to stdout; errors print to stderr only and set exit codes (0 success, 2 typed failure, 64 argparse usage).
  - Dev/admin sampler CLI remains available for QA-only flows (APP_ENV=dev) but is outside public scope.
- **Error handling:** Canonical `error_v1` envelopes with typed error tokens, LF discipline, and stdout/stderr separation for CLI. Error parity harnesses and schema checks are wired into governed evidence (`errors/*`, `parity/*`).
- **Presenter/emitter:** A single allow-listed emitter serves Reader HTTP and CLI, protecting canonical JSON bytes and LF termination. Presenter artifacts cover two-run and AB↔BA identity proofs plus preimage recompute under `artifacts/presenter/*`.
- **Internal identity:** `/internal/version` returns a fixed-order body `{engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id}` with GET/HEAD parity and conditional handling per PF14. Identity artifacts live under `artifacts/ops/internal_version/*` and `artifacts/math/*`.
- **Evidence posture:** Evidence Index (`docs/evidence/INDEX.json`) and machine Mirror (`artifacts/evidence_index.jsonl`) track governed artifacts (with `.path_proof.txt` siblings). Artifact families for EPIC020 include `ERROR_*`, `PRESENTER_*`, `INTVER_*`, and env-pin logs.

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

# `/internal/version` identity probe (ops/internal only; mirrors evidence artifacts)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev curl -sSf http://localhost:8000/internal/version
```

- Dev Reader helper (`scripts/dev_start_reader.sh`) remains available for dev/test/local harnessing; APP_ENV gating applies.
- For in-depth behavior and schema details, refer to PF-Canon titles (PF05/PF12/PF14/PF19/PF20) and the non-canon docs under `docs/` (e.g., `docs/CLI_commands.md`, `docs/architecture/emitters.md`).

## QA & evidence

- **Evidence rails:** Governed artifacts require `.path_proof.txt` siblings plus entries in the Evidence Index/Mirror; avoid manual edits. Orientation demo (`tools/evidence/orientation_demo.py`) and sanity pipeline (`tools/evidence/run_sanity_pipeline.py`) validate mirror/posture.
- **EPIC020 artifacts:** Error envelopes, presenter identity proofs, and `/internal/version` identity runs are recorded under `errors/*`, `parity/*`, `artifacts/presenter/*`, and `artifacts/ops/internal_version/*`, mirrored into the Evidence Index.
- **QA checklist:** See `docs/QA_CHECKLIST_EPIC020.md` for the deterministic suites and env-pin expectations; CI includes an EPIC020 closed-rails job.
- **Acceptance tracking:** EPIC020 acceptance map/manifest entries tie tokens to evidence; earlier epic acceptance maps remain available under `docs/acceptance_map_epic019.json` and `docs/acceptance_map_epic017.json`.

## Notes and references

- Public surfaces remain limited to Reader v1 and CLI; dev/admin harnesses (e.g., sampler CLI, QA scripts) stay restricted to dev/test/local contexts.
- PF-Canon remains authoritative for mechanics, transport, and governance. Repo docs summarize behavior and point to canonical titles rather than duplicating specs.
