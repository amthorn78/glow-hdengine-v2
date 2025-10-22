# Repo Architecture — Single Homes & Active Trees

> This document is the authoritative map of the HD Engine repo. It is kept in sync at the end of every epic.

## Single homes (authoritative)
- **engine/** — engine library
  - Compat: `engine/compat/{compute.py,ordering.py,thresholds.py,constants.py}`
  - Validation: `engine/validation/viewer_prefs.py`
  - Emission: `engine/presenter/emitter.py::emit_compact_json(payload)`
  - Serialization: `engine/serializer/canon.py::dumps(obj)->bytes` (UTF-8, sort_keys, compact, one trailing LF)
  - Errors: `engine/errors/envelope.py` (`{ok,false,code,error}`)
  - HTTP handlers: `engine/http/*` (e.g., `compat_handler.py`)
- **adapter/** — dev runner & route registration (the only app home)
  - Registers blueprints/routes and imports handlers from `engine/http/*`

## Providers
- Place reusable helpers under `engine/providers/*`. Do **not** import from legacy `adapters/` paths.

## Deprecated/archived trees
- `core/`, `server/`, `adapters/` — removed or archived by consolidation. Active code must not import these.

## Emitter/serializer discipline
- All service and CLI emission **must** call:
  - `engine.presenter.emitter.emit_compact_json(payload: dict) -> bytes`
  - `engine.serializer.canon.dumps(obj) -> bytes` (UTF-8, sort_keys=True, compact, exactly one trailing LF)
- Forbidden in handlers/CLI: `json.dumps(` or `jsonify(`

## Routing (dev only)
- Reader/Compat routes are registered from `adapter/`
- Compat alpha endpoint (internal): `/api/compat/v1`
  - Success = **200 JSON**; errors include `Cache-Control: no-store`
  - GET **ids-only** (`a_id`,`b_id`); any JSON body → **400**

## Architecture capture (every epic)
- At epic close, capture `_arch/<epic_id>_<ts>/` snapshots: routes, import scans (legacy trees), emitter/serializer guard, and a compact tree.
- Update this file as the human-readable view; store the mechanical map in artifacts for the epic.

## CI Guards (drift prevention)
- Fail if handlers/CLI contain `json.dumps(` or `jsonify(` (single emitter path rule)
- Fail on `from core|server|adapters` imports in active code
- Optional: CLI parity test (service bytes == CLI bytes for same request)

