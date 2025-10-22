# ADAPTER 009 — Internal HTTP Adapter (health/ready/version)

## Overview
Internal-only WSGI adapter exposing:
- GET /internal/healthz — process up (no engine checks)
- GET /internal/readyz — resolver + catalogs/freeze + smoke ≤800 ms; sets X-Toggles-SHA on success
- GET /internal/version — engine/build metadata (prod requires Authorization: Bearer)

Bodies are minified JSON with stable key order and one trailing newline. All responses include the header set below.

## Environments
- dev/staging: open on localhost; bearer optional (accepted if present).
- prod: /internal/version requires Authorization: Bearer <ENGINE_SERVICE_TOKEN>.
- prod overrides: if config/runtime_overrides.json exists, /internal/readyz returns 503 (OverridesNotAllowedInProd).

## Required headers (all responses)
- Cache-Control: no-store
- Content-Type: application/json; charset=utf-8
- X-Correlation-Id: <echo or generated uuid4 hex>
- X-Engine-Tag: <engine_tag>
- X-Release-Id: <release_id>
- X-Adapter-Version: v1
- Security: X-Content-Type-Options: nosniff, Referrer-Policy: no-referrer, X-Frame-Options: DENY
- Prod only: Strict-Transport-Security: max-age=31536000; includeSubDomains
- Readyz only: X-Toggles-SHA: <64-hex>

## Error envelope (v1, strict)
{ "ok": false, "schema": "v1", "code": "<Enum>", "error": "<String>", "details": "<optional>" }

## Auth (prod)
- /internal/version:
  - Missing/invalid bearer → 401 with:
    {"ok":false,"schema":"v1","code":"Unauthorized","error":"InvalidOrMissingToken"}
  - Valid bearer (ENGINE_SERVICE_TOKEN) → 200

## Readiness rules
200 iff:
1) resolve_toggles() succeeds and (prod) no runtime overrides applied,
2) catalogs/freeze/toggles load,
3) a single compute_pair smoke completes in ≤800 ms.
Else 503 with typed code: OverridesNotAllowedInProd, DependencyFailure("resolver"|"catalogs"), or SmokeFailed("latency"|"exception").

## Env vars
ENGINE_ENV=dev|staging|prod (default dev), ENGINE_SERVICE_TOKEN (prod only).
Optional fixed meta: BUILD_COMMIT_SHORT, BUILD_TIMESTAMP_UTC, ENGINE_TAG, RELEASE_ID, TOGGLES_SHA.
