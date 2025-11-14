# ADR — BodyGraph Durability Home & DB Runtime Posture

## Status
Accepted

## Context
- BodyGraph ingest & durability belong to HDE-EPIC011.
- Canon sets the durability home in schema `hde` with a `hde.body_graphs` table and `hde.body_graphs_current` view.
- A read-only integration view in `public` will expose `hde.body_graphs_current` as `public.hde_body_graphs_current`.
- DB clients may see either DATABASE_URL or DB_BRIDGE_URL; DB posture scripts must implement connection-time fallback.

## Decision
- Durability home: schema `hde`.
- Objects:
  - Table: `hde.body_graphs`
  - View (durability): `hde.body_graphs_current`
  - View (boundary): `public.hde_body_graphs_current` (read-only)
- Runtime search_path MUST be `hde, public` for engine workloads.
- Connection-time fallback for DB scripts:
  - Prefer `DATABASE_URL` when usable.
  - In dev, if `DATABASE_URL` is present but unusable, fall back to `DB_BRIDGE_URL`.
  - If neither works, fail fast with a typed error.
- Roles (names only, no grants in this ADR):
  - Migrator role (DDL owner for `hde.*`)
  - App role (CRUD on `hde.body_graphs`, SELECT on views)
  - Backend role (SELECT on `public.hde_body_graphs_current` only)
- Partition plan is non-deferred: durability storage will have a defined partition strategy (details in DDL ADR addenda).
- Retention policy will be applied at the table level (values TBD in a follow-up ADR or addendum).

## Consequences
- All future migrations for BodyGraph durability MUST target `hde` and respect the search_path and role model described here.
- Public code may only read from `public.hde_body_graphs_current` and MUST NOT write into `hde` directly.
- DB posture scripts MUST use the shared resolver and fallback rules when connecting.

## Acceptance Tokens (for EPIC-011)
- DB_SCHEMA_FINGERPRINT_OK
- DB_RUNTIME_SEARCH_PATH_OK
- DB_ROLE_GRANTS_OK
- DB_BOUNDARY_VIEW_OK
- DB_WRITERS_ISOLATED_OK
- MIGRATE_ROLLBACK_OK
- PARTITION_PLAN_OK
