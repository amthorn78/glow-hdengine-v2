# RUN — Developer flight checks (HDE-EPIC026)

## Rails
- Pin determinism env: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` (or call `engine.runtime.determinism_env.ensure_determinism_env`).
- Disable auto-reload when capturing evidence. Reader harness binds to http://127.0.0.1:5000 when run locally (dev helper can override port via `PORT`).

## Quick checks
- Env pins: `python scripts/ensure_env.py` → expect `[ENV] OK` with rails above; CI mirrors this via `ci/checks/check_env_pins.sh`.
- Serializer parity: `pytest -q tests/test_sercanon.py` (runs under pinned locale/timezone).
- Registry report spot-check: `python tools/generate_registry_report.py --check` to validate catalog inputs and serializer wiring.
- Release input gate (closed rails): `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python scripts/release_id_recompute.py --check-manifest-only`. It validates canonical `catalog/manifest.json` and its declared file hashes without writing.
- Intentional release cut: `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python scripts/cut_release_manifest.py --version <semver> --built-at-utc <YYYY-MM-DDTHH:MM:SSZ>`. This updates only the manifest; commit that input once.
- Exact-head attestation: `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/build_release_attestation.py --output <external-empty-directory> --require-clean`. The tool uses an isolated tracked-file copy, validates a fixed point and the PR-A stage-14 stop, and emits `attestation.json`, its checksum, a names-only transcript, and generated evidence outside the Repo.

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
- Existing checked-in EPIC022 release outputs remain frozen capture-time evidence. Current release derivatives and the legacy closure are produced only inside the external attestation build; direct source-tree closure execution is refused.

## Config & bundles (D5/D6)
```bash
python tools/config/generate_config_artifacts.py
python tools/config/generate_bundles.py
python tools/evidence/update_evidence_index.py  # index generated artifacts under PF12 discipline
```
The config acceptance map lives at `audit/EPIC-018_config_acceptance_map.json` (governed). Sampler/core acceptance for EPIC019 is tracked in `docs/acceptance_map_epic019.json` with a path proof.

## HumanDesignAPI v2 BodyGraph-detail resolver posture (HDE-EPIC037)

- HDE-EPIC037 is the current Fermentation Pass 8 repo-evidence slice for HDE-FERM008.7 through HDE-FERM008.12. It distinguishes historical EPIC036 pre-adapter route-policy evidence from current scoped dry-run resolver behavior; it is still not a public Reader, public route, payload, transport, app-side credential, AI, QA PASS, production deployment, PO closeout, board update, epic closeout, or broad HumanDesignAPI v2 platform-conformance expansion.
- Historical EPIC036 evidence recorded configured v2 `hdctl bg:resolve --source vendor` as `unsupported_runtime_nonclaim` before any legacy `bodygraphs` request was built. Current EPIC037 resolver wiring supersedes that configured-v2 dry-run posture only for `bg:resolve --source vendor --dry-run`: configured v2 bases select the version-neutral `charts` route and deterministic v2 ChartResult adapter; non-v2 configured bases preserve explicit legacy BodyGraph fallback.
- Generic BodyGraph ingest remains guarded from raw v2 ChartResult persistence. HDE-EPIC038 PR-05 now provides a controlled configured-v2 mapped-cache path: `hdctl bg:resolve --source vendor --upsert --user <uuid> --birthdate <YYYY-MM-DD> --birthtime <HH:MM> --location <place>`. It requires explicit open rails, a configured v2 base and credentials, a non-production-like requested and process environment, and an available sanctioned database target. The resolver projects before writing to `hde.body_graphs` and verifies canonical read-back and idempotence; `--dry-run` remains database-free.
- The mapped-cache path is not production-write authorization. Missing `--upsert`, production-like environments, or failure to construct the sanctioned database target fail closed before the vendor request. OPS harnesses remain PO-only and must not be run as documentation or PR validation or treated as OPS completion.
- Governed evidence anchors include PR-01 through PR-04 artifacts under `artifacts/vendor/hdapi_v2/`, PR-05 parent binding at `docs/acceptance_map_epic037.json`, `audit/qa/hde-epic037/token_evidence_matrix.md`, `audit/qa/hde-epic037/acceptance_map_viability.log`, `audit/qa/hde-epic037/parent_evidence_binding.log`, and PO-produced OPS-01 evidence under `audit/ops/hde-epic037/ops-hde-epic037-001/`.
- Secret/config names are `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY`; document only names or redacted header shapes, never values. Current configured-v2 dry-run route evidence uses `Authorization: Bearer <redacted>` plus `HD-Geocode-Key: <redacted>` for `charts`, while legacy BodyGraph route metadata retains `HD-Api-Key: <redacted>` for non-v2 fallback.

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
