# CHANGELOG

Unreleased — HDE-EPIC025: Repo Docs Sweep (README/CHANGELOG/AGENTS/docs/)

### Added
- Documented the EPIC025 compat contract and endpoint catalog posture (probe-only GET, POST-only internal admin surface, env-gate + catalog entry) alongside CLI stdout LF discipline and deterministic emitter coupling.
- Documented `/reader` A7 transport proofs and the proof artifacts emitted under `artifacts/proofs/` when `HDE_WRITE_A7_PROOFS=1`, plus the env-gate proof for `/reader`.
- Added EPIC025 QA evidence root and close-pack documentation: `audit/qa/hde-epic025/qa_step_logs_manifest.json`, per-check logs under `audit/qa/hde-epic025/checks/<check_id>/primary.log`, and close-pack outputs (`audit/EPIC-025_MANIFEST.json`, `audit/EPIC-025_close_report.md`, `audit/docdeltas/hde-epic025_doc_deltas.md`).
- Added documentation for the evidence-paths validation and LF-endings gates (`tools/evidence/validate_evidence_paths.py`, `tools/evidence/check_lf_endings.py`) and their QA logs in the EPIC025 root.

### Changed / Fixed
- README/AGENTS/docs refreshed to align EPIC025 evidence posture (compat contract, showcompat stdout rules, `/reader` A7 proofs, QA evidence root) and EPIC025 close-pack outputs.

2026-01-05 — HDE-EPIC022 Remediation 1 (Freeze-Pack identity contract hardening)

### Added
- Freeze-Pack manifest contract clarified: single SoT at `catalog/manifest.json` (top-level keys exactly `root`, `version`, `built_at_utc`, `files`, no self-listing) with canonical JSON bytes; `release_id = sha256(canonical_bytes(catalog/manifest.json))` (lowercase hex). Evidence copy is `artifacts/math/freeze_pack_manifest.json` (byte-identical), and evidence-only summaries (e.g., `manifest_snapshot.json`) are not identity inputs.
- Canonical recompute and evidence set: `python scripts/release_id_recompute.py --check` (fail-closed canonical recompute; writes recompute log/sha) and governed outputs `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`, `artifacts/math/manifest_snapshot.json`, `artifacts/proofs/env_pins.txt`.
- Fail-closed identity gate wired to closed rails: `python ci/checks/check_release_identity.sh` (Python entrypoint) validates schema/bytes/evidence and runs the recompute `--check`; the gate also runs inside `python tools/evidence/run_sanity_pipeline.py` alongside deterministic suites.
- Regression coverage retained: `tests/scripts/test_release_id_recompute.py` proves `--check` fails closed without rewriting freeze-pack inputs and that write-mode recovery produces the full evidence set in an isolated workspace.

### Changed / Fixed
- README/AGENTS/docs call out the release identity workflow (closed rails by default), canonical commands used in CI, and the governed evidence set/posture to prevent alternate manifest semantics or stale operator guidance.

2025-12-29 — EPIC-021: Calcination evidence pass (registry, sanity, QA harness)

### Added
- Serializer consolidation: canonical serializer and presenter remain the single source for Reader/CLI bytes; closed-rails pins documented for CLI suites.
- Evidence posture: `tools/generate_registry_report.py` emits `artifacts/registry/registry_report.json`; `tools/evidence/run_sanity_pipeline.py` captures `artifacts/sanity/sanity.log` with path proofs; `tools/evidence/update_evidence_index.py` refreshes Index/Mirror bindings for registry/sanity artifacts.
- QA harness: `tools/qa/epic021_qa.py` writes QA_ROOT logs under `audit/qa/hde-epic021/` (bootstrap log, per-step logs, QA step manifest, acceptance-map viability log) and references `docs/acceptance_map_epic021.json` plus `audit/qa/hde-epic021/token_evidence_matrix.md`.

### Changed / Fixed
- README/AGENTS/docs refreshed to align with EPIC021 deterministic rails, registry report governance, sanity pipeline, and QA harness workflows; PF-Canon titles are used for authoritative references.
- EPIC021 is a Calcination evidence pass; no breaking changes to the public Reader/CLI API, but QA artifacts and evidence indices were updated.

2025-12-22 — EPIC-020: Separation Pass 1 — Error & Identity Surfaces

### Added
- Canonical `error_v1` envelope with typed error tokens, CLI stdout/stderr separation, LF discipline, and usage-exit 64 handling; error parity harnesses and schema checks wired into governed evidence under `errors/*` and `parity/*`.
- Shared presenter/emitter across Reader HTTP and CLI with serializer guards; `showcompat` emits canonical JSON bytes with AB↔BA/two-run identity and preimage recompute proofs captured under `artifacts/presenter/*`.
- `/internal/version` internal identity surface returns fixed-order fields (`engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`) with GET/HEAD/conditional parity and identity artifacts under `artifacts/ops/internal_version/*` and `artifacts/math/*`.
- EPIC020 closed-rails CI job (SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC) plus EPIC020 QA checklist (`docs/QA_CHECKLIST_EPIC020.md`) covering deterministic suites, env-pin evidence, and scoped evidence-only expectations.

### Changed / Fixed
- README/AGENTS/docs now describe EPIC020 separation posture, presenter/emitter allow-listing, canonical error handling, and the `/internal/version` ops-only surface.
- Evidence and QA references updated to point to EPIC020 artifact families (`ERROR_*`, `PRESENTER_*`, `INTVER_*`) and acceptance map bindings.

2025-12-18 — EPIC-019: Remedial harnesses and evidence wiring (C1–C3)

### Added
- Dev Reader helper (`scripts/dev_start_reader.sh`) and infra-owned `DEV_SAMPLER_URL` binding documented for Codespaces/local dev; dev sampler healthcheck harness (`scripts/qa/dev_sampler_healthcheck.py`) captures APP_ENV gating under closed rails.
- Dev sampler Live QA harness (`scripts/qa/dev_sampler_live_qa.py`) produces governed D3 evidence (allowed/forbidden APP_ENV permutations) under `audit/qa/hde-epic019/dev_sampler_http/` and is indexed into acceptance map/manifest bindings.
- D6 open-rails Live Vendor QA harness (`scripts/qa/d6_live_vendor_qa.py`) with classified outcomes (`OK`, `FAIL_VENDOR`, `FAIL_TOOLING`) and governed logs/snapshots under `audit/qa/hde-epic019/d6-vendor-live-qa/`, mapped to D6 tokens.

### Changed / Fixed
- Dev Reader helper now tolerates empty/unset APP_ENV when invoked by harnesses; README/AGENTS/docs describe dev/admin-only posture and APP_ENV gating semantics without over-specifying edge cases.
- Evidence docs and acceptance roster updated to reflect EPIC019 remedial bindings (D3 Live QA + D6 vendor Live QA) and to reference PF-Canon titles for rails semantics.

2025-12-15 — EPIC-019: HD Dissolution Pass 2 close-out

### Added
- Sampler core (HDE-DISS003) completed with deterministic sampler harnesses (dev-only CLI `hdctl dev:sampler` and HTTP `/internal/dev/sampler`), seeded replay logs, diversity proofs, and governed evidence families indexed for sampler pool snapshots, ABBA parity, two-run identity, and seed replay.
- Engine Core (HDE-DISS004) completed with purity checks, JSON compare logs, ABBA parity, and two-run identity evidence; outputs are governed under `artifacts/core/` with schemas in `docs/schemas/core/`.
- Determinism/sanity pipeline now executes sampler and Engine Core evidence generators under closed rails, enforcing env pins and mirroring evidence to INDEX/Mirror with path proofs.
- Acceptance posture updated: EPIC019 sampler/core tokens are Green and mapped in `docs/acceptance_map_epic019.json` with manifest references in `docs/acceptance_maps.json`.

### Changed / Fixed
- Env-pins mismatch resolved: determinism helper enforcement is documented alongside `ci/checks/check_env_pins.sh` to gate SAFE_MODE/ALLOW_NETWORK/locale/timezone pins for docs and tests.
- Manifest token bindings corrected for EPIC019 acceptance, aligning sampler/core artifacts with the acceptance map and mirror records.
- `SANITY_PIPELINE_OK` manifest hash/size corrected to reflect the updated pipeline log and mirror entries.

2025-12-02 — EPIC-018: HD Calcination Pass 3 close-out

### Added
- Determinism rails (D1/D2) finalized with canonical JSON, AB↔BA/two-run identity proofs, and a determinism helper that pins locale/timezone and blocks network.
- CLI guard rails (D3): serializer grep guard and emitter symbol proof, both gated by the determinism helper and writing governed artifacts under `artifacts/cli/guards/`.
- Evidence skeleton and sanity pipeline (D4): orientation demo, sanity log capture, and governed index/mirror/path-proof discipline for all artifacts.
- Governed config artifacts and acceptance map (D5): config generators plus `audit/EPIC-018_config_acceptance_map.json` tying PF09 tasks to governed outputs.
- Typed FE/BE bundles (D6): bundle generator and schemas for frontend/backend parity with governed config and registry.
- Epic manifest and close report (D7): `audit/EPIC-018_MANIFEST.json` and `audit/EPIC-018_close_report.md` with path proofs.

### Changed
- README/AGENTS/docs now describe closed-rails posture, evidence harness workflow, config governance, and EPIC018 manifest/close-pack references.
- Deprecated guidance about manual evidence edits and open-rails runs removed; documentation now points to PF-Canon titles for transport and acceptance specifics.

2025-11-22 — EPIC-017: HD Calcination Pass 2 close-out

### Added
- EPIC017 manifest and close-out report under `audit/` plus PF doc-delta drafts for PF09/PF10/PF12/PF14/PF19/PF20/PF04.
- Acceptance map for EPIC017 foundations (`docs/acceptance_map_epic017.json`).

### Changed
- README/AGENTS/docs refreshed to describe the canonical emitter, registry loader, deterministic ordering layer, and the evidence ledger now backed by a machine mirror self-record.
- CHANGELOG now marks Calcination foundations as complete; vendor ingest (EPIC011) remains parked while matching foundations carry forward.

2025-11-14 — EPIC-011: Bridge adapter evidence (S2–S7)

### Added
- HTTPS pg-bridge coverage in `BridgeProvider`, including `/health`, `/`, `/query`, and `/introspect/{search_path,grants,fingerprint}` with typed error mapping and a version probe.
- Adapter-level introspection helpers (`DBAccess.introspect_version/search_path/grants/fingerprint`) and harness scripts:
  - `scripts/db_bridge/capture_introspection.py`
  - `scripts/db_adapter/capture_adapter_introspection.py`
  - `scripts/ops/capture_rails_open_scope.py`
- Keys-only HTTP logging via `engine.ops.http_log.log_http_call`, writing canonical JSONL to `artifacts/logs/keys_only.sample.jsonl`.
- Rails-open scope evidence at `artifacts/ops/rails_open_scope.txt` proving only bridge routes were exercised.
- Human and machine evidence indices updated with `.path_proof.txt` files for all S2–S7 artifacts (PF09 / PF12 discipline).

### Changed
- Updated documentation (README, AGENTS, docs/ADAPTER_DB.md, design package) to reflect the HTTPS bridge adapter workflow and evidence lifecycle.

2025-11-12 — EPIC-010: R7 remediation (docs & evidence pointers)

### Changed
- Confirmed the canonical Aux route `GET /api/aux/narrative?v=1` with `/aux/narrative?v=1` as the byte-identical BC alias.
- Documented the generic suppression posture (200 empty, no ETag, optional `X-Narrative-Policy: suppressed`).
- Captured provenance echoes on both outcomes (headers `X-Narrative-Pack-Sha`, `X-Narrative-Composition`).
- Recorded determinism under `LC_ALL=C`, `LANG=C`, `TZ=UTC` with two-run identity checks.
- Refreshed the Aux header snapshots and synchronized the human index plus single-file machine mirror (JSONL with proof anchors).

2025-11-11 — EPIC-010: Aux Narrative Surface (single PR)

### Added
- **Sealed narrative pack** under `catalog/narratives/{keys.json,templates.json,palettes.json,suppression_map.json,manifest.json}` with one `.sha256` sidecar per file; `pack_sha` = sha256 over canonical `manifest.json`.
- **Loader mount** at `/narratives/<pack_sha>/…` (verify → atomic swap; **no DB on hot path**).
- **Keys-only router & composer**: deterministic routing `(category, band, perspective, viewer_top, flags)` → `{personal_key, shared_key}`; tuple validation; **echo** `pack_sha` & `composition_id`.
- **Aux narrative surface**: `GET /aux/narrative` returns **200 text/plain** + quoted strong `ETag` on text; **200 empty/no-ETag** on suppression.
- **Evidence** (same PR): 10×4 coverage at `audit/gates/narratives/keys_10x4.table.json`; two Aux header snapshots at `tests/transport/headers/aux_text_200.snap` and `tests/transport/headers/aux_suppression_200.snap`; Human Index + Machine Mirror updated.

### Tokens (PASS)
JSON_CANONICAL_CHECK_OK · PACK_SHA256_SIDECARS_OK · PACKS_MANIFEST_OK · NARR_PACK_IDENTITY_OK ·
NARR_ROUTER_KEYS_ONLY_OK · NARR_DETERMINISM_OK · NARR_AB_BA_COHERENCE_OK · COMPOSE_IDS_DETERMINISM_OK ·
NARR_200_TEXT_OK · NARR_SUPPRESSED_NO_ETAG_OK · NARR_REGISTRY_CLOSURE_OK ·
EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · EVIDENCE_INDEX_MIRROR_OK · EVIDENCE_PATHS_VALIDATED_OK

2025-11-07 — EPIC-009: Ops Safety & DB Runtime Posture

### Added
- **SAFE rails refusal** at `/ops/rails/refusal` (GET/POST identical 503) with typed JSON body,
  `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, and **no ETag**.
- **Keys-only logging** for refusal using canonical keys `{at, route, status, duration_ms, idempotence_hash, release_id}`.
- **No-I/O guard** proving zero external I/O (HTTP/DNS/sockets/SDK) during refusal.
- **Env-matrix (selection-only)** evidence: success chooses `DATABASE_URL` or `DB_BRIDGE_URL` (redacted),
  failure is a frozen typed envelope; no connectivity in snapshots.
- **DB runtime posture** with connection-time fallback for scripts:
  try `DATABASE_URL`, on connection failure fall back to **Postgres-scheme** `DB_BRIDGE_URL`; fail if neither connects.
  Evidence includes exact `search_path = "hde, public"`, schema-qualified **grants** (ASCII sort; present-even-empty ADP),
  normalized **DDL fingerprint** (extensions/sequences/indexes/constraints/domains/functions; strips volatiles & ext versions),
  and **migration two-run identity** (`no-op` on second run).
- **PF12 parity**: updated **Human Evidence Index** + **Machine mirror JSONL** in the **same PR**;
  added **INDEX.sha256** sentinel (LF-terminated, lower-hex; not mirrored); path-proofs present.

### Tokens (PASS)
ENV_RAILS_POLICY_OK · ERROR_CACHECTL_NOSTORE_OK · ERROR_CTYPE_JSON_UTF8_OK · NO_CONTENT_ENCODING_OK
· NO_EXTERNAL_IO_ON_REFUSAL_OK · OBS_KEYS_ONLY_OK · PII_REDACTION_OK · DB_CONN_ENV_OK · DB_CONN_TYPED_ERROR_OK
· DB_RUNTIME_SEARCH_PATH_OK · DB_ROLE_OK · DB_SCHEMA_FINGERPRINT_OK · MIGRATION_RUNNER_OK · MIGRATION_LOGGED_OK
· MIGRATION_REPLAY_IDENTITY_OK · EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_MIRROR_OK · EVIDENCE_PATHS_VALIDATED_OK
· EVIDENCE_INDEX_HASH_OK · CI_CHECK_FINAL_LF_OK · CI_CHECK_MIRROR_SCHEMA_OK

2025-11-05 — EPIC-008: Writers & Auth

### Added
- Admin-only diagnostic writer endpoint to prove 2xx JSON rules.
- Deterministic writer transport: `Cache-Control: no-store`, **no ETag**, **never 304**, **no compression**; **HEAD→405** (no body) and **OPTIONS→204** (no body) with `Allow: POST, OPTIONS` and `Content-Length: 0`.
- Strict request validation for writer routes:
  - wrong/missing `Content-Type` → **415** (`invalid_content_type`)
  - malformed JSON/UTF-8/BOM → **400** (`invalid_json`)
  - unknown fields → **422** (`unknown_key`)
  - other schema violations → **422** (`invalid_input`)
  - payloads over **32 768 bytes** → **413** (`request_too_large`)
- Auth boundary for writers: `Authorization: Bearer`, **401** (with `WWW-Authenticate: Bearer`) vs **403**.
- Idempotent write path (preimage → sha256 digest → transactional persist) with **same-status** behavior on duplicates.
- Evidence updates: human index (`docs/evidence/INDEX.json`) and PF12 machine mirror (`artifacts/evidence_index.jsonl`) updated in the same commit; hash sentinel added.
- DB migration DDL: `migrations/008_writers_auth.sql` (creates `hde.idempotent_writes`).

### Changed
- `/api/compat/v1` success responses now explicitly set `Cache-Control: no-store`.

### Notes
- DB ops migration tooling/runbook is scheduled for a later ops epic; this release includes DDL only.

2025-10-31 — CLI file inputs and transport key-order fix
- CLI: add --pair-file / --a-file & --b-file plus --dump-reader/--dump-admin-dir; stdin and --a/--b preserved.
- Service: enforce internal/version key order and header invariants.
- Tests, QA admin dumps, and docs updated; Evidence Index entries added.

2025-10-31 — EPIC-006 Mechanics Foundations (closure)

**Highlights**
- Deterministic mechanics (comparators/helpers, arrays-as-sets, channel `NN-NN` min-first; stable-on-equal).
- Frozen denominators and direct Motor→Throat set.
- Category framework (harmony-first Magic-10), unknown-ID hard-fail; canonical registry report emitted.
- `/internal/version` posture: GET/HEAD 200, no-store, no ETag, conditionals ignored; headers-only proofs captured.
- Evidence Index (human + machine JSONL) updated in the same change.

**Acceptance tokens achieved (subset)**
- TIEBREAK_TOTAL_ORDER_OK, ORDER_STABLE_EQUAL_OK, CHANNEL_ID_FORMAT_OK, ARRAYS_AS_SETS_OK
- CONSTANTS_FROZEN_OK, MOTOR_THROAT_DIRECT_ONLY_OK
- CATEGORY_FRAMEWORK_OK, CATEGORY_CALC_PURE_OK, CONFIG_REPORT_CANON_OK
- LOCALE_TZ_INVAR_OK, LC_ALL_C_OK, TZ_UTC_DEFAULT_OK
- INTVER_200_CTYPE_JSON_UTF8_OK, INTVER_HEAD_PARITY_OK, INTVER_200_NO_ETAG_OK, INTVER_CONDITIONAL_IGNORED_OK
- EVIDENCE_INDEX_MIRROR_OK, CHANGE_AWARE_GATES_ON_OK

2025-10-16 — Repo docs consolidation (SoT + HTTP home)
• SoT clarified: Public body & determinism → “HD Engine — Math & Technical Spec”; Transport/caching acceptance → “Governance & Process (Acceptance)”.
• HTTP home: canonical adapter at adapter/http_reader.py; dev runner at dev/reader_harness/app.py (APP_ENV=dev). server/ is legacy (kept temporarily).
• Removed restatements of A7 tables from repo docs; link to Governance instead.
• Embedded evidence pointers in notes: tests/test_emitter_determinism.py, tests/test_reader_transport.py, tests/cli/*.

2025-10-02 — A7 alignment and contract centralization (v2.0 / v0.1.5)

[Env & Integration] Environment & Integration Plan v2.0

Canonical home for HTTP transport (A7): strong quoted ETag = sha256(final LF-terminated public bytes, pre-compression), Cache-Control: private, max-age=0, must-revalidate, Vary: Authorization, Accept-Encoding.

Conditional GET: CSV If-None-Match, weak tags ignored, strong compare only. 304 returns empty body; validators preserved; Content-Length: 0 or absent; Content-Type optional.

HEAD parity: validators identical to GET 200; no body; Content-Length == len(identity body).

Compression invariance: same ETag for identity, gzip, br.

Writers and errors: no ETag, Cache-Control: no-store.

Non-negotiables summarized: canonical serializer, idempotence preimage, single emitter, SAFE rails, security headers, logging and correlation.


[Reader] docs/server/reader_v1.md v2.0

Dev harness surface reaffirmed and gated to APP_ENV=dev; path policy under fixtures/charts/ with traversal and symlink denial.

Transport section links to Env v2.0; examples and acceptance markers added.

Bytes returned by Reader remain identical to CLI for the same inputs; one trailing LF.


[Contract] docs/contracts/reader_v1_public_bytes.md v1.0 (new)

Single canonical public body example (minified, sorted keys, UTF-8, one trailing LF).

Allowed enums and closed public set for Alpha: categories[0] = {"id":"harmony","band":"Cool|Open|Warm|Glow"}.

Idempotence preimage rule and a worked ETag over the final bytes.

De-duplicates schema examples across repo docs.


[Spec] Glow HD Engine — CLI, API & Vendor Ingest Spec v0.1.5

Front matter bumped; supersession map added: transport → Env v2.0, public body → Contract, Reader surface → reader_v1.md.

§2.1/2.2 tightened (serializer and regexes, including correlation id); §2.4 public categories clarified; §2.5 numeric policy clarified (Reader numeric-free; CLI --score gated).

§3.1 retitled to Idempotence (hash preimage); transport specifics moved to Env v2.0.

§18 acceptance updated to point to Env v2.0 for transport; markers kept prose-only.


[CLI] docs/CLI_commands.md v2.0

Purpose and scope clarified; stdout contract pinned (bands-only by default).

Numeric policy: top-level score_pct only with --score; half-up to 2dp; does not affect any other bytes.

Idempotence preimage coupling and strict sidecar gate restated; exit codes and acceptance evidence names listed.


[Emitters] docs/architecture/emitters.md v2.0

Single-emitter canon: CLI and Reader must import the same public emitter.

Serializer and idempotence rules centralized; AB↔BA and two-run identity required.

Provenance evidence names listed; no commands embedded.


[Alpha Acceptance] docs/alpha_acceptance.md v1.4

A3 and A5 acceptance tightened with evidence paths and PASS marker names.

Notes that A7 transport acceptance lives in Env v2.0; not restated here.


[Governance] Glow Governance & Process Handbook v1.1

Human/AI disclosure and access model restated: one human with agency; AI access via bundles only.

Source-of-truth map added; acceptance delivery policy (one revert-friendly commit with evidence) affirmed.


[Engine Tasks] HD Engine Tasks v10

Tracks updated to align with A7 and current canon.

F2: ETag and 304 discipline spelled out with Do and Accept.

I2: Rate limits clarified (Reader 120/480; Aux 30/120; 429 with Retry-After delta seconds or HTTP-date); evidence expectations listed.

Sources-of-truth pointers added to avoid duplicating transport or public body rules.


[Acceptance crib] docs/acceptance/reader_a7_crib.md (new)

One-page, command-free acceptance checklist names and artifact expectations for A7 transport, suitable for FE and QA rehearsals.



## 2025-10-30 — EPIC-010 (R7) Aux Narrative readiness
- Transport fixes: suppressed posture stays generic with no ETag.
- Vary confirmed on text and suppressed outcomes; canonical/alias routes remain byte-identical.
- CLI harness `hdctl aux-preview` shares the Aux emitter and its stdout + sidecar artifacts are indexed.
- Human and Machine evidence indices stay in parity with a single JSONL mirror and proof_anchor discipline.

---

2025-10-01 — Alpha docs/playbooks refresh (v1.2)

(unchanged from prior; retained here for history) 

[A3] CLI Alpha Public Invariant (docs/CLI_commands.md v1.2)

Public stdout pinned to canonical key set and order: ["categories","eligible","idempotence_hash","meta","release_id"] (sorted-keys JSON), one trailing LF, BOM-free, ANSI-free.

Categories rule clarified: single element with only {"id":"harmony","band":"Cool|Open|Warm|Glow"}.

Idempotence preimage rule affirmed (lowercase sha256 over canonical preimage).

Sidecar gate hardened: requires --showmath AND --admin-out AND (--admin OR HD_ADMIN=1); negative gate → exit 2, stdout empty, no file; positive gate → atomic, 0600, LF.

TS-v0 in A3/A5 remains minimal (no admin numerics).

Determinism: AB↔BA parity and two-run identity required.

Minimal artifacts standardized: cli_stdout_AB.json, cli_stdout_BA.json, release_id.txt, IDENTITY_OK.txt, validation.log (sidecar only if gate exercised).

Release identity discipline: scripts/release_id.sh prints a single 64-hex + LF (no args, no extra text).


[A5] Reader v1 Minimal API (docs/server/reader_v1.md v1.2)

Dev harness only: APP_ENV!=dev → 403 with {"error":"forbidden"}\n, no filesystem access.

Path policy: relative a/b resolved under fixtures/charts/; reject absolute paths, traversal, symlinks.

Transport: Content-Type: application/json; charset=utf-8 for success and errors; no ETag/Cache-Control, no 304 (A6 will add).

Public bytes equal CLI bytes for AB and BA; optional two-run identity.

Error bodies: single-line JSON + LF with tokens invalid_path|invalid_json|missing_tz_A|missing_tz_B.

Provenance: record EMITTER_SHA256=<64hex> for engine/emit_public.py.

Minimal artifacts standardized: reader_AB.json, reader_BA.json, headers_AB.txt, headers_BA.txt, validation.log.


[Emitters] Single Emitter Canon (docs/architecture/emitters.md v1.2)

Canonical module engine/emit_public.py required by both CLI and Reader.

Public envelope keys/order and preimage rule pinned; AB↔BA parity required.

Purity rules: no import-time I/O, no network, no file writes; keys-only logs.

Evidence: record EMITTER_SHA256 in A5 validation log.


[Alpha Acceptance] Consolidated Gate (docs/alpha_acceptance.md v1.2)

Aggregates A3/A5 invariants, minimal artifacts, and minimal validation markers.

Governance restated: single revert-friendly commit to main with evidence under artifacts/cards/<CARD>/; no PRs for final approval.

SAFE rails: acceptance runs with SAFE_MODE=1; network only if both SAFE_MODE=0 and ALLOW_NETWORK=1 are set.



---

Operator note
Repo docs are implementation playbooks. Canonical project documents (Environment & Integration Plan, Governance/Process, Engine Math/TS-v0, Spec) carry the authoritative rules and links.


## 2025-10-23 — HDE-EPIC004 Closed
### Added
- HTTP Transport Evidence goldens for Reader v1 (200, 304-after-200, HEAD, error & method posture, identity↔gzip invariance).
- Architecture snapshot `_arch/EPIC-004_<ts>/{homes.json,tree.txt}` proving single HTTP home.
### Changed
- Reader consolidated to **adapter/http_reader.py** as the only HTTP home.
- All public JSON now emitted via **engine/presenter/emitter.py** calling **engine/serializer/canon.py:sercanon**.
- Canonical start command pinned in docs: `python -m adapter.http_reader`.
### Removed/Deprecated
- “A7” wording in docs replaced by **HTTP Transport Evidence**.
