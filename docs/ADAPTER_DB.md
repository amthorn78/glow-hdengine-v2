# DB Connectivity — Connection-time fallback (EPIC-009)

Scripts that connect to Postgres MUST:

1. Try `DATABASE_URL` (if present).
2. If connection fails, fall back to **`DB_BRIDGE_URL` only when it is a Postgres DSN** (`postgres://` or `postgresql://`).
   Skip HTTP/HTTPS bridges for psycopg usage.
3. If neither option succeeds, exit with a typed `missing_db_config` error.

Dev: fallback may be exercised locally; log success/failure (keys-only).
Prod/staging: use the configured DSN; do **not** attempt HTTP bridges.

Evidence expectations:
- `artifacts/db/check_schema.txt` (exact `hde, public`).
- `artifacts/db/grants.txt` (schema-qualified; ASCII sort; present-even-empty ADP).
- `artifacts/db/ddl_fingerprint.json` (normalized; compact; LF-terminated).
- `artifacts/db/migration_runner.log` (second run reports "no-op").
