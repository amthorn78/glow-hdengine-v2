1. Repo map
- `engine/` — Present. Core compute modules (sampler, core logic), runtime emitters, CLI, bodygraph resolver/ingest, presenter/serializer, etc.
- `adapter/` — Present. Flask adapter surfaces including Reader, aux narrative, internal ops, and dev sampler endpoints, plus app factory and guards.
- `presenter/` — Present. Reader v1 emitter and JSON canon comparison helpers reused by runtime/public surfaces.
- `docs/` — Present. Acceptance maps and governed evidence index files for artifacts and QA.
- `artifacts/` — Present. Evidence index JSONL and generated artifacts (ingest logs, catalogs, etc.).
- `catalog/` — Present. Catalog JSON describing channels, gates, manifests, and narrative packs used by the engine surfaces.
- `scripts/` — Present. Operational, QA, and release helper scripts (CLI wrappers, sanity gates, ingest helpers).
- Other notable roots: `adapter` (HTTP), `engine` (core), `presenter`, `docs`, `artifacts`, `catalog`, `scripts`, `tests/` (pytest suite), `schemas/` (data schemas), `migrations/` (DB migrations), `audit/` (QA logs).

Expected layout status:
- `engine/` — Present. Houses deterministic sampler/core plus compat and runtime emitters.
- `adapter/` — Present. Flask HTTP surfaces and guards.
- `presenter/` — Present under `engine/presenter/` and shared `presenter/reader_v1/` emitters.
- CLI package — Present at `engine/cli/` with `hdctl` entrypoint defined in `pyproject.toml`.
- `docs/` — Present with acceptance maps and evidence index.
- `artifacts/` — Present with evidence index JSONL and generated artifacts.
- `scripts/` — Present with QA/dev/release utilities.
- `audit/qa/` — Present within `audit/` containing QA gates (see evidence index entries).

2. Engine modules
- Sampler (`engine/sampler/core.py`): Defines frozen dataclasses for viewer/candidate/config, builds eligible candidate pools, ranks deterministically via weight/compat/band/ID comparators, and provides `sample_and_rank` helper.
- Engine Core (`engine/core/core.py`): Pure-compute functions and dataclasses for participant state, config, perspective breakdown, and `compute_core` that enforces AB/BA ordering, neutral scores, band ordering, and shared trait canonicalization.
- No duplicate sampler/core modules observed; each has a single primary implementation.

3. Adapter / HTTP surfaces
- Flask blueprint in `adapter/http_reader.py`:
  - `/reader` GET/HEAD dev-only Reader harness loading charts from local fixtures and emitting canonical Reader bytes with ETag handling.
  - `/api/aux/narrative` and `/aux/narrative` emit public aux narratives with ETags when not suppressed.
  - `/internal/dev/sampler` POST provides dev/admin sampler harness calling sampler core directly with writer-style envelopes on error.
  - Ops/admin endpoints include `/ops/rails/refusal`, `/ops/probe/env`, and `/ops/writer/diagnostic`, plus `/internal/version` for identity metadata.
- Additional compatibility writer blueprint under `engine/http/compat_handler.py` exposes `/api/compat/v1` GET/POST/HEAD/OPTIONS producing compat JSON with writer-style envelopes.

4. Presenter / emitter
- Canonical JSON emitter `engine/presenter/emitter.py` centralizes `emit_compact_json` and `emit_public` for LF-terminated canonical bytes using serializer canon.
- Serializer `engine/serializer/canon.py` wraps stable serializer for canonical JSON used by all surfaces.
- Reader-specific emitter `presenter/reader_v1/emitter.py` builds preimage, computes idempotence hash, and emits final Reader v1 envelope via canonical emitter; used by runtime public helper.
- Single emitter stack appears shared across HTTP (Reader/aux) and CLI outputs via `emit_public`/runtime helpers.

5. CLI surfaces
- Entry point `hdctl` (`engine/cli/main.py` via `pyproject.toml`) with subcommands:
  - `showcompat` builds or resolves BodyGraphs (file/db/vendor), computes compat payload, emits Reader bytes, and optional admin dumps.
  - `aux-preview` previews aux narratives for compat payloads (uses same emitters; not shown but adjacent).
  - `bg:resolve` returns BodyGraph resolution envelope using resolver logic without real IO under closed rails.
  - `dev:sampler` dev/admin sampler harness loading candidates from file and emitting ranked list via serializer.
- Command dispatch handled by `cli()` parsing args and invoking handlers with error mapping.

6. Vendor seam & BodyGraph storage
- Vendor HTTP client `engine/bodygraph/vendor_client.py` constructs HTTPS requests with API keys and geo key, pinned retries/timeouts, and typed errors; `build_request` normalizes birth data and fingerprints payloads.
- Ingest pipeline `engine/bodygraph/ingest.py` enforces SAFE/ALLOW rails, builds vendor request via client, emits canonical payload, persists to DB (when not dry-run), logs parity, and computes idempotency key; includes DB helper functions and synthetic ID normalization.
- Resolver control flow `engine/bodygraph/resolver.py` decides source (auto/db/vendor), enforces rails, gathers inputs (env or args), normalizes IDs, invokes ingest (dry-run for CLI), and wraps result in status envelope.
- DB access layer referenced via `engine.db` within ingest (not detailed here); adapter HTTP surfaces avoid direct vendor/DB calls.

7. Evidence & catalogs
- Evidence index present at `docs/evidence/INDEX.json` (single-line governed index) with SHA sidecars; artifacts mirror stored in `artifacts/evidence_index.jsonl` with keys, paths, hashes, roles, and sizes.
- Catalog files under `catalog/` include manifest and channel/gate listings for runtime/reference use.
- Endpoint catalog file not found; no `ENDPOINTS_CATALOG` observed.

8. Flows & call chains
- Reader success (dev harness): HTTP GET `/reader` (`adapter/http_reader.py:reader_v1`) loads local charts, enforces version/env, then calls `emit_reader_public_bytes` default from `engine/runtime/public.py`, which computes band via compat TS and emits Reader v1 envelope through `presenter/reader_v1/emitter.emit_reader_v1` using canonical emitter/serializer before returning HTTP response with ETag.
- CLI compatibility flow: `hdctl showcompat` (`engine/cli/main.py`) loads parties (file/db/vendor), computes TS features, calls `compat_public` for compat payload, emits public compat bytes via `emitter.emit_public`, and also emits Reader bytes via `emit_reader_public_envelope`, with optional dumps for admin proofs.
- Vendor ingest flow: CLI vendor path builds `VendorInputs` and calls `ingest_vendor_bodygraph` (dry-run unless configured), which constructs vendor request via `HdApiClient`, fetches payload, fingerprints and logs, optionally persists to DB, and returns outcome; resolver wraps this in status envelope for CLI output.

9. Reality vs Expectations (drift summary)
- Engine/adapter/presenter split: Aligned — deterministic engine modules separated from Flask adapter and shared canonical emitter/serializer stack.
- Single emitter for surfaces: Aligned — both HTTP and CLI use `engine.presenter.emitter` and runtime Reader helpers feeding `presenter/reader_v1` emitter.
- Vendor seam outside engine core: Partial — vendor client/ingest live under `engine/bodygraph` (inside engine package) but remain separate from sampler/core; they perform network/DB IO guarded by rails.
- Evidence layout: Aligned — governed evidence index and artifact mirror present under `docs/evidence` and `artifacts/`.
- Adapter exposure: Aligned for Reader/aux/internal dev harness via Flask; compatibility writer also exists under `engine/http`.
- Surprises: IO-heavy vendor ingest code resides inside `engine/bodygraph` package (not a separate adapter layer), and Reader public surface gated to dev with fixture-based charts rather than external inputs.

Testing
- Not run (read-only architecture audit).
