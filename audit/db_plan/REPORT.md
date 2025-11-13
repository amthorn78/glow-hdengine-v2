# HDE-EPIC011 Database Planning Audit

## Overview
- **Discovery source:** `artifacts/db_discovery/20251113`
- **Schema dump:** `artifacts/db_discovery/20251113/postgres_schema_only.sql`
- **Database engine:** PostgreSQL 17.6 (dumped with pg_dump 17.7)
- **Search path:** `hde, public`
- **Schemas analyzed:** `hde` (engine/internal) and `public` (application/user data)

## Schemas & naming conventions
- `hde` stores engine telemetry and published artifacts. Tables follow strict `snake_case` with UUID/text identifiers and partitioned history (`*_pcur` tables attached to the primary partitioned tables).
- `public` holds core product data. Table names use `snake_case`, often prefixed with `user_` for per-user state. Columns typically use `snake_case` with `_id` suffixes for integer identifiers and `_at` for timestamps.
- No additional custom schemas or bodygraph-specific namespaces were present. Privileges grant `hde_rw` usage on `hde`, indicating a read/write service role boundary.

## User / core tables
- **public.users** — integer surrogate PK (`id`) with email uniqueness and admin flag defaults; referenced by nearly every other user-facing table.
- **public.user_profiles** — PK `id`, unique `user_id`, optional profile details; references `users` via FK, aligning with the `user_id` naming convention.
- **public.birth_data** — PK & FK on `user_id`, extensive birth time/location fields, defaults for `location_source` (`'manual'`) and `location_verified` (`false`).
- **public.human_design_data** — PK/FK on `user_id`; stores `chart_data`, `energy_type`, `strategy`, `authority`, `profile`, API payload, and calculation timestamp.
- **public.compatibility_matrix** — composite PK (`user_a_id`, `user_b_id`) with dual FKs to `users`, modelling pairwise relationships.
- **Session & preference tables** (`user_sessions`, `user_preferences`, `user_priorities`, `user_resonance_*`) — all keyed by `user_id` and FK-constrained to `users`, providing structured per-user preferences and resonance signals.
- **Administrative tables** (`admin_action_log`, `email_notifications`) — log-like data referencing `users` via nullable foreign keys.

## Existing BodyGraph-related structures
- No tables/views include “bodygraph” or `bg_` in their names. However, `public.human_design_data` already stores per-user Human Design chart attributes and API responses, and `public.user_resonance_signals_private` tracks Human Design-derived signals (bridges, decision modes, etc.). These are the closest existing structures for BodyGraph durability.

## Key dependencies and hotspots
- `public.users` is the central hub with 13 inbound FKs, covering admin logs, compatibility, birth data, design data, preferences, priorities, resonance metrics, sessions, and notifications. Any new durability table should expect to reference `users` for ownership.
- `hde` tables are partitioned event stores (`pair_evaluation` and `public_results` with current (`_pcur`) partitions). No foreign keys connect `hde` to `public`, reinforcing separation between engine telemetry and application data.

## Index and constraint posture
- All tables have primary keys, often implemented as unique btree indexes. User-centric tables rely on single-column integer PKs (`users`, `user_profiles`, `user_sessions`) or composite keys for pairwise data (`compatibility_matrix`).
- Secondary indexes exist on lookup fields (e.g., `ix_users_email`, `ix_user_sessions_session_token`, location indexes on `birth_data`). Partitioned tables in `hde` include mirrored indexes on the attached `_pcur` partitions.
- Check constraints enforce hash formatting on `hde.pair_evaluation` and `hde.public_results` (`release_id` & `idempotence_hash`), and on `hde.meta`’s `invocation_tag`.

## Implications for HDE-EPIC011 (BodyGraph durability)
- **Schema placement:** `public` is the natural home for a durability table tied to user records. The existing `human_design_data` table suggests either augmenting it or introducing a sibling (e.g., `user_bodygraph_snapshots`) keyed by `user_id` with FK to `users`.
- **Naming alignment:** Follow `snake_case` with `user_` prefix if the table is user-scoped. Column names should use `_id`, `_at`, and `_json` suffixes to match existing patterns (`chart_json`, `computed_at`).
- **Key choices:** Use integer `user_id` referencing `public.users(id)`; consider composite keys (`user_id`, `computed_at`) if multiple durability snapshots must be stored. Defaults like `now()` for timestamps and JSON/JSONB payloads align with current design data storage.
- **Collision avoidance:** No current tables named `bodygraph`, but `human_design_data` already claims the general concept. If a new table is introduced, coordinate naming to avoid confusion (e.g., `human_design_bodygraph_history`).
- **Engine boundary:** Keep durability data in `public`; avoid coupling to partitioned `hde` telemetry unless there is a specific engine processing requirement.

## Risks and open questions
- **Data overlap:** Clarify whether the new durability table should supersede or extend `public.human_design_data`. Requirements should specify retention vs. snapshot history to avoid redundant storage.
- **Partitioning & retention:** If long-term durability implies high-volume history, confirm whether range partitioning (similar to `hde` tables) or archival strategy is needed.
- **API provenance:** `human_design_data.api_response` is raw text; determine whether new durability records must capture external payloads, derived metrics, or normalized structures.
- **Permissions/RLS:** Dump lacks role/row-level security info beyond basic grants. Confirm whether RLS policies exist elsewhere or need to be considered for new tables.
- **Sequence usage:** Several tables rely on sequences (`users_id_seq`, `user_profiles_id_seq`, etc.). Confirm whether durability records should adopt integer sequences or reuse natural keys.
- **Testing data bridges:** No foreign keys connect `hde` → `public`; verify that any durability ingestion path does not require cross-schema FK constraints, or plan for application-level integrity enforcement.
- **Terminology alignment:** Coordinate with product/DBA on preferred naming (`bodygraph`, `design`, `chart`) to prevent mismatched semantics.

