# Coverage Matrix — Bridge provider & evidence

| Scenario | DATABASE_URL | DB_BRIDGE_URL | Expected Result | Verification |
| --- | --- | --- | --- | --- |
| Primary succeeds | Reachable psycopg DSN | Optional | Adapter returns psycopg provider; bridge attempts marked `skip`. | Unit tests + adapter selection snapshot (`provider="psycopg"`). |
| Primary fails, bridge succeeds | Invalid/timeout | HTTPS pg-bridge | Adapter selects `bridge`; harness captures `/health`, `/`, `/query`, `/introspect/*` payloads. | `scripts/db_bridge/capture_introspection.py`, adapter snapshot JSON. |
| Both fail | Invalid | Missing/invalid | Adapter raises typed `AdapterError` (`missing_database_url`, `missing_bridge_url`, or `bridge_guard_blocked`). | Unit tests covering error codes + refusal envelope parity. |
| Rails-open scope | Any | HTTPS pg-bridge | Keys-only log shows only `db_bridge.*` routes; `vendor_call_count: 0`. | `scripts/ops/capture_rails_open_scope.py` summary + JSONL log inspection. |
| Env-matrix selection | Unset | HTTPS pg-bridge | Snapshot records the fallback order without attempting connectivity. | `artifacts/runtime/env_matrix.snapshot.json` + diff/prev baselines. |

Coverage keeps fallback deterministic, auditable, and LF-terminated; all governed artifacts land under `artifacts/db_bridge/`, `artifacts/db/`, `artifacts/engine/`, `artifacts/logs/`, or `artifacts/ops/` with matching `.path_proof.txt` files and Evidence Index entries.
