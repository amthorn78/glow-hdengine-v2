# DB Connectivity — Bridge adapter & evidence (EPIC-011)

Scripts that need database posture must go through the adapter (`engine.db.adapter.DBAccess`):

1. Call `DBAccess.for_current_env(...)`. The helper attempts `DATABASE_URL` first (psycopg), then HTTPS `DB_BRIDGE_URL` via `BridgeProvider` when rails are open or bridge-forced.
2. Fallback selection is recorded automatically in `artifacts/db_bridge/adapter_selection.snapshot.json` (canonical JSON, LF-terminated) with attempts and the chosen provider.
3. If neither provider is usable, the adapter raises a typed `AdapterError` (`missing_database_url`, `missing_bridge_url`, `bridge_guard_blocked`, etc.). Do **not** bypass the adapter or open raw sockets.

Bridge requirements:
- `DB_BRIDGE_URL` must be HTTPS and point at the pg-bridge service root.
- Bridge endpoints used by the engine: `GET /health`, `GET /`, `POST /query`, `GET /introspect/search_path`, `GET /introspect/grants`, `GET /introspect/fingerprint`, and the adapter’s version probe (`SELECT current_setting('server_version')`).
- All HTTP activity is logged via `engine.ops.http_log.log_http_call` into `artifacts/logs/keys_only.sample.jsonl` (keys-only, no payloads or headers).

Harness scripts (rails open):
- `python scripts/db_bridge/capture_introspection.py` — exercises the bridge directly and writes canonical snapshots under `artifacts/db_bridge/` and `artifacts/db/`.
- `python scripts/db_adapter/capture_adapter_introspection.py` — calls `DBAccess.introspect_{version,search_path,grants,fingerprint}` and captures adapter-normalized results under `artifacts/engine/`.
- `python scripts/ops/capture_rails_open_scope.py` — reruns both harnesses, summarizes HTTP routes in `artifacts/ops/rails_open_scope.txt`, and asserts `vendor_call_count: 0`.

Evidence expectations (PF09 / PF12):
- Every governed artifact listed above has a sibling `.path_proof.txt`, a human index entry (`docs/evidence/INDEX.json`), and a machine mirror record (`artifacts/evidence_index.jsonl`).
- Introspection payloads are canonical JSON, UTF-8, sorted keys, compact, and end with exactly one newline.
- Logs and scope reports remain keys-only and must never expose DSNs, headers, or SQL bodies.
