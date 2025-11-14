# Canon Deltas — Bridge adapter (EPIC-011)

| Area | Prior Canon | Delta | Notes |
| --- | --- | --- | --- |
| Connection precedence | Psycopg-only | Preserve psycopg first, then HTTPS `DB_BRIDGE_URL` via `BridgeProvider`; record attempts in adapter snapshot. | Matches `docs/ADAPTER_DB.md`; no third-party retries added. |
| Bridge validation | Allow Postgres DSN fallback | Require HTTPS pg-bridge endpoint; reject plaintext or missing URLs with typed `AdapterError`. | Prevents misuse and aligns with SAFE rails policy. |
| Introspection surface | Manual SQL probes | Provide adapter helpers (`introspect_{version,search_path,fingerprint}`) that delegate to bridge endpoints and normalize payloads. | Shapes mirror pg-bridge responses and stay canonical JSON. |
| Logging & telemetry | Route-specific logging only | Centralize keys-only HTTP logging via `engine.ops.http_log.log_http_call` (`{at,route,status,duration_ms,idempotence_hash?,release_id?}`). | Ensures no payloads/headers leak while preserving auditability. |
| Evidence discipline | Partial indexing | Mandate `.path_proof.txt` files and synchronized updates to `docs/evidence/INDEX.json` + `artifacts/evidence_index.jsonl` for every governed artifact. | Reinforces PF09 / PF12 acceptance tokens. |

Canon updates respect presenter requirements, keep refusal handling unchanged, and document bridge usage through deterministic, auditable artifacts.
