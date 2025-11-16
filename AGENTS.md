# AGENTS.md — Glow HD Engine (agent rules)

## Repository scope & invariants
- Public Reader v1 responses stay bands-only (numeric-free); see docs/server/reader_v1.md **(dev harness; deprecated)** if present.
- Emit public success bytes through engine.presenter.emitter.emit_public to share the canonical presenter/emitter path.
- Canonical JSON is UTF-8, sort_keys=True, compact separators (",",":"), with exactly one trailing LF per engine/serializer/canon.py.
- Treat arrays-as-sets by deduping and ASCII-sorting (engine/mech/helpers.py); normalize channel ids to NN-NN with the lower value first (engine/mech/compare.py).

## Environment & configuration
- Smoke base URL variable: HDE_BASE_URL (dev default: http://127.0.0.1:5000 in scripts/architecture_capture.sh). **Set explicitly for staging/prod.**

## Service entrypoints & commands
- Local adapter server: python -m adapter.http_reader (dev runner in adapter/http_reader.py).
- CLI setup and help: python -m pip -q install -e ., then hdctl --help and python -m engine.cli --help (pyproject.toml exposes hdctl via engine.cli.main:cli).
- python -m engine.cli --help must exit 0 (parity with hdctl --help).

## QA / acceptance (repo-only)
- /internal/version must serve GET and HEAD as application/json; charset=utf-8 with Cache-Control: no-store, no ETag, HEAD Content-Length equal to the GET body, and conditional GET remaining 200 (adapter/http_reader.py; tests/transport/test_internal_version_contract.py; artifacts/proofs/internal_version_headers.json).
- CLI `showcompat` must emit non-empty canonical JSON (one LF) and pass two-run identity and AB↔BA parity on a fabricated pair.
- A7 JSON success check: **Dev harness example (APP_ENV=dev)** GET "${HDE_BASE_URL:-http://127.0.0.1:5000}/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" expecting Content-Type application/json (from VERIFY.sh). For staging/production, use a cataloged JSON success endpoint if present; otherwise record a documentation gap and skip A7.
- Writers (EPIC-008):  
  - Transport: HEAD→405 and OPTIONS→204 (no body), `Cache-Control: no-store`, no ETag, no compression; never 304 (conditionals ignored).  
  - Validation: strict `Content-Type` (diagnostic empty-body exempt); 400 invalid JSON; 422 unknown_key / invalid_input; 413 ≥ 32 768 bytes.  
  - Auth: `Authorization: Bearer` with `admin:write` (401/403 split).  
  - Idempotence: preimage `{method, writer_route_id, canonical_request_body}`; sha256 lowercase hex; duplicate returns same status.
- **Aux (EPIC-010) checklist:**
  - Route & alias: `GET /api/aux/narrative?v=1` (canonical) and `/aux/narrative?v=1` (BC alias).
  - Posture names: Text → 200 text/plain with quoted strong ETag, LF body, Vary; Suppressed → 200 empty, no ETag, optional generic policy header.
  - Provenance headers: `X-Narrative-Pack-Sha`, `X-Narrative-Composition` on both outcomes.
  - Evidence pointers: `tests/transport/headers/aux_text_200.snap`, `tests/transport/headers/aux_suppression_200.snap`, `audit/gates/narratives/keys_10x4.table.json`.
  - Guard: no Aux HEAD/304 captures in this epic; Catalog/A7 proofs live elsewhere.

## DB bridge / adapter evidence (EPIC-011)
- Bridge provider must use HTTPS `DB_BRIDGE_URL`; surface `/health`, `/`, `/query`, and `/introspect/{search_path,grants,fingerprint}` plus the adapter’s version probe. Wrap network failures as typed adapter errors (no raw `urllib` tracebacks).
- Harness sequence (rails open, SAFE logging):
  - `python scripts/db_bridge/capture_introspection.py`
  - `python scripts/db_adapter/capture_adapter_introspection.py`
  - `python scripts/ops/capture_rails_open_scope.py`
- Keys-only HTTP logs live at `artifacts/logs/keys_only.sample.jsonl` via `engine.ops.http_log.log_http_call`; only `{at, route, status, duration_ms, idempotence_hash?, release_id?}` are recorded.
- `artifacts/ops/rails_open_scope.txt` must report `vendor_call_count: 0` for EPIC-011 harness runs.

## Evidence & artifact paths
- Machine mirror index: artifacts/evidence_index.jsonl (PF12 keys; one JSON object per line).
- Proof artifacts live under artifacts/proofs/; QA captures under artifacts/qa/.
- Every governed artifact needs a sibling `.path_proof.txt` plus entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in the same PR (see HDE-Build Checklist, HDE-Schemas & Artifacts).

## EPIC011 – Source invariance test chart (S10)

Use this synthetic chart for vendor ingest, refresh posture, and DB-only invariance checks (no real user system required):

- user_id: `epic011-s10-invariance-1`
- birthdate: `1990-01-01`
- birthtime: `12:00`
- location: `Amsterdam, Netherlands`

These pins drive the S9/S10/S11 harnesses and must remain stable so the ingest path, parity proofs, and refresh worker share the same BodyGraph row.

## Do / Don’t
- Do use engine.presenter.emitter for public bytes, keep JSON canonical and LF-terminated, dedupe+sort arrays-as-sets, and normalize channel ids to NN-NN.
- Don’t add new env vars, bypass the shared emitter, alter transport rules, or stash specs in Build Notes.
- Do keep logs keys-only with exactly: {at, route, status, duration_ms, idempotence_hash, release_id}.
- Do label the refusal route with the symbolic route name **"ops.rails.refusal"**.
- Do capture refusal evidence as a single file: lower-case header names → one blank line → frozen body (LF).
- Do treat **env-matrix** as **selection-only** (no DB connectivity); snapshots choose `DATABASE_URL` or `DB_BRIDGE_URL` and freeze the failure envelope.
- Do implement **connection-time fallback** for DB posture scripts: try `DATABASE_URL`, then fall back to HTTPS `DB_BRIDGE_URL` through `BridgeProvider`; fail fast if both are unusable.
- Do ensure compat/admin preview reuses the shared presenter/emitter when text output is required; ids-only preview is allowed for suppressed outcomes.
- Don’t log request/response bodies or headers; redact emails/UUIDs/≥32-hex except allow-list {release_id, idempotence_hash, invocation_tag}.

Referenced repo paths
- docs/server/reader_v1.md
- engine/presenter/emitter.py
- engine/serializer/canon.py
- engine/mech/helpers.py
- engine/mech/compare.py
- scripts/architecture_capture.sh
- VERIFY.sh
- adapter/http_reader.py
- pyproject.toml
- tests/transport/test_internal_version_contract.py
- artifacts/proofs/internal_version_headers.json
- artifacts/evidence_index.jsonl
- artifacts/proofs/
- artifacts/qa/
