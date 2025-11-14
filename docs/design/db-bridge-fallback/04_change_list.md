# Change List — Bridge adapter & evidence

1. Keep `DBAccess` as the single entry point for provider selection (psycopg → HTTPS bridge) and persist attempts to `artifacts/db_bridge/adapter_selection.snapshot.json`.
2. Require HTTPS `DB_BRIDGE_URL` and wrap network/HTTP errors as typed `AdapterError` codes (`bridge_requires_https`, `bridge_network_error`, etc.).
3. Add adapter-level introspection helpers and normalize payloads for version, search_path, grants, and fingerprint results.
4. Introduce keys-only HTTP logging via `engine.ops.http_log.log_http_call` and ensure bridge requests emit `{at,route,status,duration_ms,idempotence_hash?,release_id?}` only.
5. Ship harness scripts (`scripts/db_bridge/capture_introspection.py`, `scripts/db_adapter/capture_adapter_introspection.py`, `scripts/ops/capture_rails_open_scope.py`) to capture canonical JSON artifacts and scope reports.
6. Update docs (`README.md`, `AGENTS.md`, `docs/ADAPTER_DB.md`, this design package) plus Evidence Index and machine mirror entries (with `.path_proof.txt`) in the same PR.
