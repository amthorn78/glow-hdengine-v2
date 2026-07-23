# ADR — BodyGraph Durability Home & DB Runtime Posture

## Status
Accepted for the BodyGraph durability, schema, search-path, and role decisions below. The bridge transport clauses are a historical retained record and are superseded for current execution; they are not current guidance.

## Context
- BodyGraph ingest & durability belong to HDE-EPIC011.
- Canon sets the durability home in schema `hde` with a `hde.body_graphs` table and `hde.body_graphs_current` view.
- A read-only integration view in `public` will expose `hde.body_graphs_current` as `public.hde_body_graphs_current`.
- Historical retained record, not current guidance: EPIC-011 DB clients could see either `DATABASE_URL` or `DB_BRIDGE_URL`, and its posture scripts implemented connection-time fallback.
- Current direct-only overlay: `DATABASE_URL` is the sole active endpoint; `DB_BRIDGE_URL` is retired and must not be configured or used, and no transport fallback is permitted.

## Decision
- Durability home: schema `hde`.
- Objects:
  - Table: `hde.body_graphs`
  - View (durability): `hde.body_graphs_current`
  - View (boundary): `public.hde_body_graphs_current` (read-only)
- Runtime search_path MUST be `hde, public` for engine workloads.
- Current DB scripts use the shared `engine.db.adapter.DBAccess` selector and direct psycopg only.
- Missing or unavailable direct access fails closed with a typed, names-only error; no retry or alternate provider is attempted.
- Historical retained record, not current guidance: the accepted EPIC-011 decision once preferred direct access and then allowed dev fallback to `DB_BRIDGE_URL`; that fallback is retired and must not be restored.
- Roles (names only, no grants in this ADR):
  - Migrator role (DDL owner for `hde.*`)
  - App role (CRUD on `hde.body_graphs`, SELECT on views)
  - Backend role (SELECT on `public.hde_body_graphs_current` only)
- Partition plan is non-deferred: durability storage will have a defined partition strategy (details in DDL ADR addenda).
- Retention policy will be applied at the table level (values TBD in a follow-up ADR or addendum).

## Consequences
- All future migrations for BodyGraph durability MUST target `hde` and respect the search_path and role model described here.
- Public code may only read from `public.hde_body_graphs_current` and MUST NOT write into `hde` directly.
- DB posture scripts MUST use the shared direct-only selector and MUST NOT implement fallback or a second transport policy.

## Acceptance Tokens (for EPIC-011)
- DB_SCHEMA_FINGERPRINT_OK
- DB_RUNTIME_SEARCH_PATH_OK
- DB_ROLE_GRANTS_OK
- DB_BOUNDARY_VIEW_OK
- DB_WRITERS_ISOLATED_OK
- MIGRATE_ROLLBACK_OK
- PARTITION_PLAN_OK
