# ADAPTER 009 — Internal HTTP Adapter (health/ready/version)

## Overview
Internal-only WSGI adapter exposing:
- GET /internal/healthz — process up (no engine checks)
- GET /internal/readyz — always 200 `{"ok":true,"schema":"v1"}`; no dependency check, no smoke (see Readiness rules)
- GET /internal/version — engine/build metadata; served by every app factory, with no authorization check

Bodies are minified JSON with stable key order and one trailing newline. Responses of `adapter.wsgi` include the header set below.

### `/internal/version` invariants (enforced)
- GET and HEAD both return **200** with header parity.
- **Cache-Control: no-store** and no ETag on this route.
- Conditional validators are ignored; conditional GET still returns 200.
- Body keys remain ordered: `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id` (pinned by `tests/transport/test_internal_version_contract.py`). `release_id` is the canonical release identity.
- Route stays DB-decoupled and renders without external dependencies.

## Environments
- Every environment: /internal/version answers without authorization; an `Authorization` header is ignored, and no code reads `ENGINE_SERVICE_TOKEN`. A request carrying `X-Identity-Override` returns 400 (`no-store`, no ETag). Local captures use `http://127.0.0.1:8000` (see "Deterministic run posture").
- prod overrides: /internal/readyz performs no override check; config/runtime_overrides.json does not change its response.

## Required headers (all responses of `adapter.wsgi`)
- Applied by `adapter.wsgi:create_app()` (`adapter.app:app`) only. The production app (`adapter.factory`) and the dev Reader do not add this set; their `/internal/version` response carries `Cache-Control: no-store`, `Content-Type` and `Content-Length`.
- Cache-Control: no-store
- Content-Type: application/json; charset=utf-8
- X-Correlation-Id: <echo or generated uuid4 hex>
- X-Engine-Tag: the app's `ENGINE_TAG` configuration value, default `Isis6`
- X-Release-Id: the app's `RELEASE_ID` configuration value, default `rel_dev`; not the canonical `release_id`, which the `/internal/version` body reports
- X-Adapter-Version: v1
- Security: X-Content-Type-Options: nosniff, Referrer-Policy: no-referrer, X-Frame-Options: DENY
- Prod only: Strict-Transport-Security: max-age=31536000; includeSubDomains
- /internal/readyz adds no header of its own (no X-Toggles-SHA).

## Error envelope (v1, strict)
{ "ok": false, "schema": "v1", "code": "<Enum>", "error": "<String>", "details": "<optional>" }

## Auth
- /internal/version has no authorization check in any environment: it returns no 401, and an `Authorization` header changes nothing.

*Note (EPIC-005): proofs captured in repo artifacts do not use Bearer.*

## Readiness rules
/internal/readyz is registered only by `adapter.wsgi:create_app()`, exposed as `adapter.app:app` for `flask --app adapter.app run`. The production app (`adapter.factory:create_app()`, started by `Procfile`) and the dev Reader (`python -m adapter.http_reader`) do not register it and answer 404.
It returns 200 with `{"ok":true,"schema":"v1"}` and the header set above, unconditionally. It checks no dependency, runs no smoke and performs no override check, so a 200 shows only that the process answers.

## Env vars
`APP_ENV` selects the environment. `adapter/wsgi.py` (for the production-only `Strict-Transport-Security` header) and `adapter/env_guard.py` read `ENGINE_ENV` only when `APP_ENV` is blank.
No code reads `ENGINE_SERVICE_TOKEN`, `TOGGLES_SHA`, `BUILD_COMMIT_SHORT` or `BUILD_TIMESTAMP_UTC`. The HTTP adapter reads neither `ENGINE_TAG` nor `RELEASE_ID` from the environment (`adapter/wsgi.py` sets them as app configuration defaults, `Isis6` and `rel_dev`, for its `X-Engine-Tag` and `X-Release-Id` headers and its log lines), but the vendor client (`engine/bodygraph/vendor_client.py`) reads `RELEASE_ID` from the environment for its `User-Agent: GlowHDEngine/<release_id>` header when no release identity is passed.

# Appendix-D — Evidence Index (EPIC-005)

**Transport — `/internal/version`**

* `artifacts/headers/internal_version_200.txt`
* `artifacts/headers/internal_version_head.txt`
* `artifacts/headers/internal_version_if_none_match.txt`
* `artifacts/headers/internal_version_override_denied.txt`

**Identity & Math**

* `artifacts/identity/service_identity.json`
* `artifacts/math/release_id.txt`
* `artifacts/math/release_id_recompute.log`
* `artifacts/identity/emitter_sha256.txt`

**Database**

* `artifacts/db/ddl_applied.sql`
* `artifacts/db/check_schema.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/grants.txt` *(deferred to HDE-EPIC-006)*

**Ops pins**

* `artifacts/validation/service_cmd.txt` *(deferred to HDE-EPIC-006)*
* `artifacts/prod/exposure_note.md`


# HD Engine Repo Docs — Index (SoT pointers)

This repo contains implementation docs. Canon (spec/process) lives in PF documents; reference **titles only**:

- Mechanics Guide to the HD Engine (Build Guide)
- HD Engine Build Checklist (Components & Tasks)
- HD Engine Math & Technical Spec
- HD Engine — CLI, API & Vendor Ingest Spec
- Governance & Process Handbook

### Local map
- **ARCHITECTURE.md** — single homes (engine/, adapter/), guards, providers
- Architecture snapshots: `_arch/<epic_id>_<timestamp>/` (routes/imports/tree)

### Developer quick-links
- Emitter: `engine/presenter/emitter.py::emit_compact_json`
- Serializer: `engine/serializer/canon.py::dumps` (UTF-8; sort_keys; one LF)
- Compat handler (alpha): `engine/http/compat_handler.py`

### Acceptance crib
- Reader (EPIC-004): `docs/acceptance/reader_a7_crib.md`
- Internal Ops (EPIC-005): `docs/acceptance/http_transport_evidence.md`

### Evidence Index (EPIC-005)
- `docs/EVIDENCE_INDEX.md`

- Pins: `python scripts/ensure_env.py` → `[ENV] OK`
- Tests: `pytest -q tests/infra/test_sercanon_bytes.py`
<!-- EPIC-004 PATCH: RUN posture -->
### Deterministic run posture (Reader)
```bash
python -m adapter.http_reader
```

Bind target for captures: http://127.0.0.1:8000 — the runner binds loopback (127.0.0.1) only, on `$PORT` when set (default 8000).

Environment for reproducible bytes/headers (same shell):
```
APP_ENV=dev
SAFE_MODE=1
ALLOW_NETWORK=0
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONUTF8=1
```

Auto-reload: **off** when capturing evidence.

<!-- EPIC-004 RUN posture -->
```bash
python -m adapter.http_reader
```
Bind: http://127.0.0.1:8000 (`$PORT` when set)  ·  Env: APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONUTF8=1  ·  Auto-reload: off

---

## RUN — Production start (repository `Procfile`)

The repository's start command is the `Procfile` line:

```bash
/app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30
```

This states the repository's start command only, not the live service's settings.

Evidence: `artifacts/validation/service_cmd.txt` *(deferred to HDE-EPIC-006 if not yet captured)*

# Reader — HTTP Transport Evidence (Acceptance)

**Scope:** Reader v1 transport; public payload remains numeric-free, bands-only.

<a id="tokens-must-be-pass"></a>

## Required transport predicates and evidence

All predicates below remain required within this document's stated scope. The retained identifiers are optional historical/evidence lookup labels with their original meanings; new-work acceptance does not require token issuance or token PASS. A label alone proves no HTTP behavior. Any current acceptance claim must be established from applicable native source, tests and captured transport evidence for that predicate and candidate. This framing update does not attest current conformance or reconcile differences in retained technical wording; assess discrepancies against the actual owning sources.

- `HTTP_200_HEADERS_OK` — JSON Content-Type; Cache-Control `private, max-age=0, must-revalidate`;
  `Vary: Authorization, Accept-Encoding` (exact order, single comma+space);
  **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- `HTTP_ETAG_INVARIANCE_IDENTITY_GZIP_OK` — identity ↔ gzip ETag identical (Brotli optional via `.note.json`).
- `HTTP_304_OMIT_CONTENT_TYPE_OK` — 304 omits `Content-Type`; **no body** (Content-Length 0 or absent).
- `HTTP_304_VALIDATORS_REPEAT_OK` — 304 repeats ETag / Vary / Cache-Control identically to the prior 200.
- `HTTP_HEAD_CL_AND_CT_OK` — HEAD includes Content-Type; **no body**; `Content-Length == len(identity bytes)`;
  validators equal 200.
- `HTTP_ERRORS_NOSTORE_NOETAG_OK` — Errors/writers are JSON, **no-store**, **no ETag**.
- `HTTP_POST_METHOD_POSTURE_OK` — Reader POST ⇒ 405 typed JSON (`no-store`, no ETag); Compat POST ⇒ 200 non-conditional.
- `COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 error_v1 envelope built from the `invalid_json` alias (emitted `code`: `ERR_COMPAT_INVALID_JSON`), `no-store`, no ETag.

Current routes (HDE-EPIC040): the 200, 304 and HEAD predicates above apply to the dev Reader `GET /reader`, the route the A7 transport proofs select from `docs/ENDPOINTS_CATALOG.json`. `HTTP_POST_METHOD_POSTURE_OK` keeps its original meaning, which now holds for the unprefixed `POST /reader`: it returns the governed 405 (`ERR_NOT_FOUND`, `Allow: GET, HEAD`, `no-store`, no ETag). The production Reader is `POST /api/reader?v=1` or `?v=2`: a success is 200, non-conditional and carries no ETag; its errors are `no-store` without ETag; every other method on `/api/reader` returns 405 with `Allow: POST`. See `docs/contracts/reader_v2_public_bytes.md`.

## Evidence shape
Header goldens are canonical JSON: **lowercased keys**, sorted, compact, **exactly one trailing LF**.
Bytes are LF-terminated; Reader↔CLI parity is defined via the CLI `--dump-reader` sidecar (not `showcompat` stdout), as in `docs/acceptance/http_transport_evidence.md`.

<!-- EPIC-004 PATCH: _arch naming compatibility note -->
### Snapshot directory naming (compatibility)
- **New snapshots (recommended):** `_arch/EPIC-004_<timestamp>/…`
- **Historic snapshots (valid):** `_arch/EPIC004_<timestamp>/…`

Both forms are accepted by our docs and tools. **Do not rename** existing `_arch` folders.
# Internal Ops — HTTP Transport Evidence (EPIC-005)

**Endpoint:** `GET /internal/version` (+ `HEAD`)

**Body (200):** exactly the six keys `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`, in that order.
LF-terminated JSON; no extra fields.

**Headers (200):**

* `Content-Type: application/json; charset=utf-8`
* `Cache-Control: no-store`
* **No** `ETag`

**HEAD (200):**

* same validators as 200
* **no body**
* `Content-Length ==` 200 body bytes

**Conditionals:** `If-None-Match` ignored — still **200** (no 304)

**Override:** `X-Identity-Override` ⇒ **400** JSON in every environment; `no-store`; **no `ETag`**

**Evidence (repo-relative):**

* `artifacts/headers/internal_version_200.txt`
* `artifacts/headers/internal_version_head.txt`
* `artifacts/headers/internal_version_if_none_match.txt`
* `artifacts/headers/internal_version_override_denied.txt`
* `artifacts/identity/service_identity.json`

### EPIC-006 — `/internal/version` posture
- GET and HEAD both return **200** with header parity.
- **Cache-Control: no-store**; **no ETag** on this route.
- Conditional validators are **ignored** (conditional GET still returns 200).
- Body is compact JSON with keys in order: `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`.
- This route must be **DB-decoupled** and always render without external dependencies.

### `/internal/version` invariants (enforced)
GET/HEAD 200 with header parity; Cache-Control: no-store; no ETag; conditional GET ignored; body key order:
`engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`.

