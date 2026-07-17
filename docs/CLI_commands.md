# CLI commands — Compat v1 and conjunction/dev harnesses (HDE-EPIC027)

The CLI shares the canonical presenter/emitter and serializer with the Reader harness. Run public commands under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`), enforced by `engine.runtime.determinism_env.ensure_determinism_env`.

## Usage
- `hdctl showcompat --pair-file <pair.json>`
- `hdctl showcompat --a-file <A.json> --b-file <B.json>`
- `hdctl showcompat` (reads one pair from stdin)
- Conjunction compatibility check:
  - `hdctl showcompat --conjunction --pair-file <pair.json>`
  - `hdctl showcompat --conjunction --a-file <A.json> --b-file <B.json>`
  - `hdctl showcompat --conjunction --user-a <user_a> --user-b <user_b> [--source db|vendor|auto]`
  - `hdctl showcompat --conjunction` (reads one conjunction pair payload from stdin)
- `hdctl aux-preview --pair-file <compat.json> --category <slug> --band <band> --perspective <perspective> [--show-narrative] [--admin-out <ids.json>]`
- `hdctl bg:resolve --user <user> [--source auto|db|vendor] [--upsert] [--dry-run] [--birthdate YYYY-MM-DD --birthtime HH:MM --location <place>]`
  - Closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) refuse vendor resolution before route-policy classification, client construction, request construction, fetch, ingest, DB, DNS, socket, or HTTP.
  - Under explicitly open rails, configured v2 bases use the governed, version-neutral `charts` route plus the deterministic v2 ChartResult adapter. `--dry-run` maps without constructing a database target. A non-dry-run configured-v2 write requires explicit `--upsert`, a non-production-like requested and process environment, and an available sanctioned `DBAccess.for_current_env(snapshot_path=None)` target. The resolver persists only the projected mapped-cache payload to `hde.body_graphs`, then verifies canonical read-back and idempotence.
  - Missing `--upsert`, production-like environments, and failure to construct the sanctioned database target fail closed before the vendor request. This controlled path is not production-write authorization. Non-v2 configured bases preserve explicit legacy BodyGraph fallback.
- Dev-only sampler CLI (APP_ENV in `dev|test|local`, QA only): `hdctl dev:sampler --viewer <viewer_id> --candidates-file <candidates.json> [--seed <seed>]`
- Flags for QA sidecars: `--dump-reader <out.json> --dump-admin-dir <dir>`

`showcompat --conjunction` emits canonical JSON to stdout. Side effects depend on input mode and rails: payload-based invocation (`--pair-file`, `--a-file` + `--b-file`, or stdin with `left`/`right`) is computation-only, while unresolved `--user-a/--user-b` inputs can trigger bodygraph resolution and vendor ingest under open rails (for example with `--source vendor`), which may persist resolved records. Required conjunction inputs must be present for both parties, either through `--user-a/--user-b` or through payload input. Single-party file input (only `--a-file` or only `--b-file`), mixed file modes, or unresolved auto source paths fail with CLI usage errors; `--dump-reader`/`--dump-admin-dir` are not supported with `--conjunction`.

Exit codes: 0 success; 64 for usage/validation/IO errors surfaced via `CliError`; showcompat vendor/engine failures return exit 1 as enforced by the CLI error-path tests; other non-zero codes are command-specific. PF05 (CLI/API/Vendor Ref) is the canonical home for the exit-code taxonomy; the current vendor/engine mapping is documented here until implementation aligns (known mismatch until PF05 parity). Success bytes are LF-terminated canonical JSON printed to stdout; stdout must end with exactly one LF and CRLF is rejected with `STDOUT_MISSING_LF` / `STDOUT_CRLF`. Showcompat stdout is the canonical emitter output for compat or conjunction payloads and may include numeric scores/weights as captured in governed evidence. Reader v1 bytes are emitted via `--dump-reader` sidecar files (shared `emit_reader_public_envelope` path) and align with the Reader harness. CLI errors are emitted as stderr code strings (not JSON envelopes). Aux preview emits ids-only JSON unless `--show-narrative` is set.

## Guards
- Serializer grep guard: `python tools/cli/serializer_grep_guard.py` → `artifacts/cli/guards/serializer_grep_guard.log`
- Emitter symbol proof: `python tools/cli/emitter_symbol_proof.py` → `artifacts/cli/guards/emitter_symbol_proof.txt`
Both guards fail fast if determinism rails are not pinned and protect the allow-listed presenter/emitter.


## HumanDesignAPI v2 BodyGraph-detail resolver evidence posture (HDE-EPIC037)

- EPIC037 PR-01 through PR-05 complete the current repo-evidence chain for HDE-FERM008.7 through HDE-FERM008.12: field sufficiency, pure deterministic v2 ChartResult adapter mapping, configured-v2 `bg:resolve --source vendor --dry-run` charts-route wiring, mapped v2-to-compat proof, PO-produced OPS-01 smoke binding, and parent evidence binding.
- For configured v2 bases, `hdctl bg:resolve --source vendor --dry-run` selects `charts` with `Authorization: Bearer <redacted>` plus `HD-Geocode-Key: <redacted>` and maps through the deterministic v2 ChartResult adapter. Legacy BodyGraph route metadata retains `HD-Api-Key: <redacted>` posture for non-v2 fallback. Generic BodyGraph ingest remains guarded from raw v2 ChartResult persistence. HDE-EPIC038 PR-05 adds only the controlled projected mapped-cache path described above for explicit `--upsert`; production-like writes remain refused.
- PR-04 evidence proves mapped v2 ChartResult adapter output can feed `engine.compat.compute.conjunction_public` with two-run and AB/BA identity posture, while preserving public Reader no-change and admin/public boundaries.
- OPS-01 evidence under `audit/ops/hde-epic037/ops-hde-epic037-001/` is PO-produced bounded open-rails smoke evidence only: it records `vendor.hdapi.post:/charts`, adapter status `ADAPTER_MAPPED`, payload family `ChartResult`, compatibility path accepted, exit code 0, and redacted secret-safe posture for HDE-FERM008.11 later-drain support. PR-05 binds that evidence without rerunning OPS or making a live vendor call.
- EPIC037 parent binding records `parent_posture=supportable_to_done` as supportable for later PF09 drainage from repo evidence only. It does not claim QA PASS, OPS completion by PR work, PF09 status movement/drainage, PO closeout, board update, production deployment, epic closeout, broad HumanDesignAPI v2 platform conformance, public Reader change, new public route/flag/payload/transport, new HTTP home, app-side HumanDesignAPI ownership, raw secret/request/response/vendor payload persistence, or AI scope.

## Historical HumanDesignAPI v2 route-policy evidence posture (HDE-EPIC036)

- PR-01 route-policy evidence for HDE-FERM008.6 is governed at `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`, `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`, `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`, `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`, `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`, and `audit/qa/hde-epic036/route_policy_decision.log`.
- PR-02 evidence-loop binding is recorded at `docs/acceptance_map_epic036.json`, `audit/qa/hde-epic036/token_evidence_matrix.md`, `audit/qa/hde-epic036/acceptance_map_viability.log`, `audit/docdeltas/hde-epic036_doc_deltas.md`, and `audit/qa/hde-epic036/00_meta/doc_deltas.md`; Human Evidence Index and Machine Mirror rows remain the canonical evidence bindings.
- EPIC036 records historical pre-adapter route-policy evidence: configured v2 bases were classified as `unsupported_runtime_nonclaim` before constructing a legacy `bodygraphs` request, and explicit legacy fallback was preserved only for non-v2 configured bases. Current EPIC037 dry-run resolver wiring supersedes that configured-v2 runtime posture only for scoped dry-run use.

## Evidence discipline
- Conjunction evidence artifacts: `artifacts/audit/cli/pair.json`, `artifacts/audit/cli/pair_ba.json`, `artifacts/audit/cli/showcompat_ab.json`, `artifacts/audit/cli/showcompat_ba.json`, compare logs under `artifacts/audit/cli/`, and ABBA sidecar artifacts under `artifacts/cli/abba_sidecar.json` (with `.sha256` + `.path_proof.txt`).
- Guard outputs, QA dumps, and other governed artifacts must have `.path_proof.txt` siblings plus entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`. Use `python tools/evidence/update_evidence_index.py` to refresh.
- Registry report: `python tools/generate_registry_report.py` writes `artifacts/registry/registry_report.json` (canonical serializer) with a `.path_proof.txt` sidecar.
- Orientation and sanity checks: `python tools/evidence/orientation_demo.py` and `python tools/evidence/run_sanity_pipeline.py` (canonical output: `audit/gates/sanity_pipeline/sanity_pipeline.log` under closed rails). `artifacts/sanity/sanity.log` is an updater-owned, byte-identical compatibility mirror for historical bindings; it is not the indexed authority. Run `ci/checks/check_mirror_schema.sh` to validate mirror schema/self-record/path-proof discipline.
- Canonical JSON gate (closed rails): `python tools/evidence/run_canonical_json_gate.py` (CI step “Run canonical JSON gate (closed rails)”) writes `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and `audit/gates/json_gate/canonical/json_gate_structured_record.json` with `.path_proof.txt` siblings (`--check-only` available for read-only validation). The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log`.
- Showcompat deterministic capture (EPIC022 D2): `python tools/cli/generate_showcompat_artifacts.py` records `artifacts/cli/showcompat/stdout.json`, `artifacts/cli/showcompat/stdout.json.sha256`, and `artifacts/cli/showcompat/args.json` with env-pin metadata; governed via `.path_proof.txt` siblings and the Evidence Index/Mirror.
- CLI installability/help/version conformance artifacts: `python tools/cli/generate_cli_conformance_artifacts.py` writes `artifacts/cli/install/installability_summary.json`, `artifacts/cli/install/entrypoints.txt`, `artifacts/cli/help/hdctl_help.txt`, and `artifacts/cli/help/showcompat_help.txt`.
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
