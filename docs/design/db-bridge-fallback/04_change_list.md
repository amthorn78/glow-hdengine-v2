# Change List — DB Bridge Fallback

1. Extract fallback helper to shared adapter utility invoked by CLI and adapter server.
2. Enforce Postgres-only guard on `DB_BRIDGE_URL` with descriptive validation errors.
3. Update posture scripts to surface `missing_db_config` through shared emitter, preserving refusal logging format.
4. Extend architecture capture script to exercise fallback path and deposit artifacts under `artifacts/db/`.
5. Document operator runbook entries in `docs/ADAPTER_DB.md` referencing new fallback expectations.
6. Refresh audit snapshots to include fallback success and failure envelopes with ASCII-sorted keys.
