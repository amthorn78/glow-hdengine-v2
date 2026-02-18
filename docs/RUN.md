# RUN — Developer flight checks (HDE-EPIC026)

## Rails
- Pin determinism env: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` (or call `engine.runtime.determinism_env.ensure_determinism_env`).
- Disable auto-reload when capturing evidence. Reader harness binds to http://127.0.0.1:5000 when run locally (dev helper can override port via `PORT`).

## Quick checks
- Env pins: `python scripts/ensure_env.py` → expect `[ENV] OK` with rails above; CI mirrors this via `ci/checks/check_env_pins.sh`.
- Serializer parity: `pytest -q tests/test_sercanon.py` (runs under pinned locale/timezone).
- Registry report spot-check: `python tools/generate_registry_report.py --check` to validate catalog inputs and serializer wiring.
- Release identity gate (closed rails): `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python scripts/release_id_recompute.py --check` (fail-closed canonical recompute) and `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python ci/checks/check_release_identity.sh` (Python entrypoint). Both commands run under the canonical manifest contract (`catalog/manifest.json` only; keys `{root,version,built_at_utc,files}`, no self-listing; canonical bytes rule). `--check` writes `artifacts/math/release_id_recompute.log` and its sha sidecar even on failure; use a clean workspace or discard local changes.

## Evidence and guard workflow
```bash
# CLI guards (D3)
python tools/cli/serializer_grep_guard.py
python tools/cli/emitter_symbol_proof.py

# Registry report (EPIC021)
python tools/generate_registry_report.py

# Sampler / Engine Core evidence (DISS003/DISS004)
python tools/evidence/generate_sampler_evidence.py
python tools/evidence/generate_engine_core_evidence.py

# Evidence skeleton updates (D4) and sanity pipeline (EPIC021 wiring)
python tools/evidence/update_evidence_index.py
python tools/evidence/orientation_demo.py
python tools/evidence/run_sanity_pipeline.py
```
Outputs are governed and require `.path_proof.txt` plus INDEX/mirror updates; the sanity pipeline runs under closed rails and mirrors registry_report/sanity artifacts into Index/Mirror when combined with the index updater.
- Release identity outputs (must exist and be non-empty under PF10/PF12 discipline): `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`, `artifacts/math/manifest_snapshot.json`, `artifacts/proofs/env_pins.txt`. `artifacts/math/freeze_pack_manifest.json` is the byte-identical evidence copy of `catalog/manifest.json`; `manifest_snapshot.json` is evidence-only and not an identity input. The identity gate is also wired into `python tools/evidence/run_sanity_pipeline.py`.

## Config & bundles (D5/D6)
```bash
python tools/config/generate_config_artifacts.py
python tools/config/generate_bundles.py
python tools/evidence/update_evidence_index.py  # index generated artifacts under PF12 discipline
```
The config acceptance map lives at `audit/EPIC-018_config_acceptance_map.json` (governed). Sampler/core acceptance for EPIC019 is tracked in `docs/acceptance_map_epic019.json` with a path proof.

## Dev-only conjunction endpoints (do not enable in production)

The conjunction preview routes `/dev/sampler/conjunction`, `/dev/reader/conjunction`, and `/dev/writer/conjunction` are dev-harness surfaces only. Runtime gating is enforced by `APP_ENV`: requests are allowed only when `APP_ENV` is `dev`, `test`, or `local`; all other values (including prod) are rejected with a forbidden writer-style envelope. Keep these endpoints limited to local/dev/test workflows under SAFE rails and never expose them on production surfaces.

For CLI conjunction flows, use `hdctl showcompat --conjunction` with either `--user-a/--user-b`, `--pair-file`, `--a-file/--b-file`, or stdin pair payload input. Provider acquisition for unresolved user inputs is closed by default and only opens when both `SAFE_MODE=0` and `ALLOW_NETWORK=1`; closed rails may emit explicit refusal codes (for example `PROVIDER_REFUSED`).

## Dev/admin harnesses

Closed rails unless noted; APP_ENV gating applies for `/internal/dev/sampler`.

```bash
# Start dev Reader helper (APP_ENV=dev by default; port override allowed)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh

# Dev sampler healthcheck (closed rails, uses DEV_SAMPLER_URL from environment)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev DEV_SAMPLER_URL="$DEV_SAMPLER_URL" scripts/qa/dev_sampler_healthcheck.py

# Dev sampler Live QA (closed rails; APP_ENV permutations logged)
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 DEV_SAMPLER_URL="$DEV_SAMPLER_URL" scripts/qa/dev_sampler_live_qa.py

# D6 vendor Live QA (open rails; vendor test identity, governed logs only)
ALLOW_NETWORK=1 scripts/qa/d6_live_vendor_qa.py

# EPIC021 QA harness (closed rails; optional EPIC021_QA_RUN_ID to group artifacts)
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/qa/epic021_qa.py
```

Logs:
- Dev sampler healthcheck → `notes/dev-sampler/dev_sampler_healthcheck.log`
- Dev sampler Live QA → `audit/qa/hde-epic019/dev_sampler_http/`
- D6 vendor Live QA → `audit/qa/hde-epic019/d6-vendor-live-qa/`
- EPIC021 QA harness → `audit/qa/hde-epic021/` (bootstrap log, step logs, acceptance-map viability, manifest)
