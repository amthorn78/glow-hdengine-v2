# Repo Architecture — Single Homes & Active Trees

> This document is the authoritative map of the HD Engine repo. It is kept in sync at the end of every epic.

## Single homes (authoritative)
- **engine/** — engine library
  - Compat: `engine/compat/{compute.py,ordering.py,thresholds.py,constants.py}`
  - Validation: `engine/validation/viewer_prefs.py`
  - Emission: `engine/presenter/emitter.py::emit_public(envelope, *, sort_keys=True) -> bytes`; `emit_compact_json(envelope, *, sort_keys=True) -> tuple[bytes, dict]` is a compatibility alias of `emit_public_with_envelope`
  - Serialization: `engine/serializer/canon.py::sercanon(obj, *, sort_keys=True) -> bytes` (UTF-8, sorted keys by default, compact, exactly one trailing LF); `dumps` is a compatibility alias
  - Errors: `engine/compat/errors.py::error_envelope` builds the governed `error_v1` envelope with keys `schema` (`"v1"`), `ok` (`false`), `code` and `error`, adding `details` only when a caller passes one (the Reader routes never do); the Reader error branches are `$defs.error` of `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json`.
  - HTTP handlers: `engine/http/*` (e.g., `compat_handler.py`)
  - Charts (pure): `engine/charts/pure.py` holds `validate_birth_inputs`, `normalize_chart` and `ChartInputError`; it does no time, randomness, environment, network, provider, logging or filesystem access, and the pinned ISO-3166 and IANA lists arrive as arguments
- **adapter/** — dev runner & route registration (the only app home)
  - Registers blueprints/routes and imports handlers from `engine/http/*`
  - Chart orchestration: `adapter/chart_orchestration.py::load_chart` is the non-HTTP chart entry; it owns the `SAFE_MODE` read for its log field, both clocks, the correlation id, the pinned-list reads, the fixture chart and one keys-only log line per call, and it registers no route and writes no file

## Providers
- Place reusable helpers under `engine/providers/*`. Do **not** import from legacy `adapters/` paths.

## Deprecated/archived trees
- `core/`, `server/`, `adapters/` — removed or archived by consolidation. Active code must not import these.

## Emitter/serializer discipline
- All service and CLI emission **must** call:
  - `engine.presenter.emitter.emit_public(envelope: dict, *, sort_keys: bool = True) -> bytes` (or `emit_public_with_envelope`, which returns `(bytes, envelope)`; `emit_compact_json` is its compatibility alias)
  - `engine.serializer.canon.sercanon(obj, *, sort_keys=True) -> bytes` (UTF-8, sorted keys by default, compact, exactly one trailing LF); `dumps` is a compatibility alias
- Forbidden in handlers/CLI: `json.dumps(` or `jsonify(`

## Routing and mounts
- Reader/Compat routes are registered from `adapter/`. Three app factories mount the same blueprints: the dev/internal blueprint at `/`, the production Reader blueprint under `/api` (`POST /api/reader`) and the compat blueprint at `/api/compat/v1`.
  - `adapter/factory.py::create_app` — the production app (`Procfile`, gunicorn)
  - `adapter/wsgi.py::create_app` — adds `/internal/healthz` and `/internal/readyz`
  - `adapter/http_reader.py::create_app` — the dev runner (`python -m adapter.http_reader`, started by `scripts/dev_start_reader.sh`)
- The route inventory is `docs/ENDPOINTS_CATALOG.json`, written by `tools/evidence/generate_a7_transport_proofs.py`
- In a production-like posture, the dev/internal blueprint serves no dev-harness handler and no canon-retired route: each dev-harness route answers its canonical refusal and each retired `/ops` route the governed not-found, before any handler runs (`adapter/http_reader.py::_mount_for_production`; S19-F03)
- Compat alpha endpoint (internal): `/api/compat/v1`
  - Success = **200 JSON**; errors include `Cache-Control: no-store`
  - GET answers **200** `{"ok":true,"schema":"v1"}`; a GET with a body answers **400** with `code` `ERR_COMPAT_INVALID_JSON`

## Architecture capture (every epic)
- At epic close, capture `_arch/<epic_id>_<ts>/` snapshots: routes, import scans (legacy trees), emitter/serializer guard, and a compact tree.
- Update this file as the human-readable view; store the mechanical map in artifacts for the epic.

## CI Guards (drift prevention)
- Fail if handlers/CLI contain `json.dumps(` or `jsonify(` (single emitter path rule)
- Fail on `from core|server|adapters` imports in active code
- Optional: CLI parity test (service bytes == CLI bytes for same request)

