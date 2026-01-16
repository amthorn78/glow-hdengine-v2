# CLI commands — Compat v1 and dev/admin harnesses (post-EPIC022)

The CLI shares the canonical presenter/emitter and serializer with the Reader harness. Run public commands under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`), enforced by `engine.runtime.determinism_env.ensure_determinism_env`.

## Usage
- `hdctl showcompat --pair-file <pair.json>`
- `hdctl showcompat --a-file <A.json> --b-file <B.json>`
- `hdctl showcompat` (reads one pair from stdin)
- `hdctl aux-preview --pair-file <compat.json> --category <slug> --band <band> --perspective <perspective> [--show-narrative] [--admin-out <ids.json>]`
- `hdctl bg:resolve --user <user> [--source auto|db|vendor] [--birthdate YYYY-MM-DD --birthtime HH:MM --location <place>]`
- Dev-only sampler CLI (APP_ENV=dev, QA only): `hdctl dev:sampler --viewer <viewer_id> --candidates-file <candidates.json> [--seed <seed>]`
- Flags for QA sidecars: `--dump-reader <out.json> --dump-admin-dir <dir>`

Exit codes: 0 success; 64 for usage/validation/IO errors surfaced via `CliError`; showcompat vendor/engine failures return exit 1 as enforced by the CLI error-path tests; other non-zero codes are command-specific. PF05 (CLI/API/Vendor Ref) is the canonical home for the exit-code taxonomy; the current vendor/engine mapping is documented here until implementation aligns (known mismatch until PF05 parity). Success bytes are LF-terminated canonical JSON printed to stdout. Showcompat stdout is the canonical emitter output for the compat payload (AB↔BA identity, two-run identity, preimage recompute preserved) and may include numeric scores/weights as captured in the EPIC022 D2 evidence. Reader v1 bytes are emitted via `--dump-reader` sidecar files and align with the Reader harness. Error envelopes use `error_v1` with typed tokens, are numeric-free, and are printed to stderr only (LF-terminated JSON). Aux preview emits ids-only JSON unless `--show-narrative` is set.

## Guards
- Serializer grep guard: `python tools/cli/serializer_grep_guard.py` → `artifacts/cli/guards/serializer_grep_guard.log`
- Emitter symbol proof: `python tools/cli/emitter_symbol_proof.py` → `artifacts/cli/guards/emitter_symbol_proof.txt`
Both guards fail fast if determinism rails are not pinned and protect the allow-listed presenter/emitter.

## Evidence discipline
- Guard outputs, QA dumps, and other governed artifacts must have `.path_proof.txt` siblings plus entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`. Use `python tools/evidence/update_evidence_index.py` to refresh.
- Registry report: `python tools/generate_registry_report.py` writes `artifacts/registry/registry_report.json` (canonical serializer) with a `.path_proof.txt` sidecar.
- Orientation and sanity checks: `python tools/evidence/orientation_demo.py` and `python tools/evidence/run_sanity_pipeline.py` (pipeline emits `artifacts/sanity/sanity.log` under closed rails). Run `ci/checks/check_mirror_schema.sh` to validate mirror schema/self-record/path-proof discipline.
- Canonical JSON gate (closed rails): `python tools/evidence/run_canonical_json_gate.py` (CI step “Run canonical JSON gate (closed rails)”) writes `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and `audit/gates/json_gate/canonical/json_gate_structured_record.json` with `.path_proof.txt` siblings (`--check-only` available for read-only validation). The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log`.
- Showcompat deterministic capture (EPIC022 D2): `python tools/cli/generate_showcompat_artifacts.py` records `artifacts/cli/showcompat/stdout.json`, `artifacts/cli/showcompat/stdout.json.sha256`, and `artifacts/cli/showcompat/args.json` with env-pin metadata; governed via `.path_proof.txt` siblings and the Evidence Index/Mirror.
- Sampler evidence harness: `python tools/evidence/generate_sampler_evidence.py` runs dev sampler CLI + HTTP harnesses and captures seed replay, diversity, ABBA, and two-run identity logs.
- Engine Core evidence harness: `python tools/evidence/generate_engine_core_evidence.py` captures purity, JSON compare, ABBA, and two-run identity logs.
- Evidence index updater: `python tools/evidence/update_evidence_index.py` mirrors registry_report, sanity, showcompat captures, and other governed artifacts into Index/Mirror (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`). Update the skeleton in the same PR when governed bytes change, and follow the refresh order: update_evidence_index (write) → orientation_demo (write) → `--check` variants → `ci/checks/check_mirror_schema.sh`.
- Release identity (closed rails): Freeze-Pack SoT is `catalog/manifest.json` (keys `{root,version,built_at_utc,files}`, no self-listing); `release_id = sha256(canonical_bytes(catalog/manifest.json))`. Evidence copy is `artifacts/math/freeze_pack_manifest.json` (byte-identical to the SoT); `manifest_snapshot.json` is evidence-only. Validation commands: `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python scripts/release_id_recompute.py --check` and `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python ci/checks/check_release_identity.sh` (Python entrypoint; also run via `python tools/evidence/run_sanity_pipeline.py`). Evidence set must exist and be non-empty: `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`, `artifacts/math/manifest_snapshot.json`, `artifacts/proofs/env_pins.txt`. `--check` writes the recompute log/sha; use a clean workspace for governed artifacts.

## Dev/admin harnesses (dev/test/local only)

- Dev Reader helper: `APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev_start_reader.sh`
- Dev sampler healthcheck (closed rails): `APP_ENV=dev DEV_SAMPLER_URL="$DEV_SAMPLER_URL" SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC scripts/qa/dev_sampler_healthcheck.py`
- Dev sampler Live QA (closed rails; APP_ENV permutations): `DEV_SAMPLER_URL="$DEV_SAMPLER_URL" SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC scripts/qa/dev_sampler_live_qa.py`
- D6 vendor Live QA (open rails vendor harness, governed): `scripts/qa/d6_live_vendor_qa.py` (allows `ALLOW_NETWORK=1`; SAFE_MODE may be 0/1; runs under controlled vendor test identity only).
- EPIC021 QA harness (closed rails): `python tools/qa/epic021_qa.py` writes QA_ROOT logs under `audit/qa/hde-epic021/` (bootstrap, step logs, acceptance-map viability, manifest).

See PF05 — CLI/API/Vendor Ref and PF12 — Schemas & Artifacts for canonical rules (title references only).
