# Canon Deltas — DB Bridge Fallback

| Area | Current Canon | Delta | Notes |
| --- | --- | --- | --- |
| Connection precedence | Primary DSN only | Introduce two-step attempt (`DATABASE_URL` → `DB_BRIDGE_URL`) before failing. | Aligns with `docs/ADAPTER_DB.md` guidance; no other retry layers added. |
| URL validation | Minimal schema checks | Require Postgres scheme for bridge DSN; reject HTTP/HTTPS. | Prevents psycopg misuse and aligns with repo invariants. |
| Error taxonomy | Generic connection failures | Normalize to typed `missing_db_config` when both DSNs unusable. | Ensures refusal evidence remains machine-parseable. |
| Evidence catalog | Primary-only artifacts | Add fallback success/failure captures to `artifacts/db/` and index updates. | Maintain LF-termination and ASCII sorting. |
| Documentation | High-level policy | New design docs under `docs/design/db-bridge-fallback/` referenced by audit snapshots. | Keeps change traceable without touching runbooks outside scope. |

Canon updates respect presenter requirements and avoid modifying transport/writer contracts.
