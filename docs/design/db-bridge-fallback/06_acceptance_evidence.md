# Acceptance Evidence — Bridge adapter (EPIC-011)

| Evidence | Description | Storage |
| --- | --- | --- |
| `artifacts/db_bridge/adapter_selection.snapshot.json` | Canonical JSON recording provider attempts (`psycopg`/`bridge`) and final selection. | `artifacts/db_bridge/` |
| `artifacts/db_bridge/{health.json,root.json,query_select_1.json}` | Bridge HTTP captures proving `/health`, `/`, and `/query` under rails-open. | `artifacts/db_bridge/` |
| `artifacts/db/introspect.{search_path,grants,fingerprint}.json` | Bridge introspection payloads (present-even-empty grants, canonical fingerprint). | `artifacts/db/` |
| `artifacts/engine/db_adapter.{version,search_path,fingerprint}.json` | Adapter-level introspection outputs normalized by `DBAccess`. | `artifacts/engine/` |
| `artifacts/logs/keys_only.sample.jsonl` | Keys-only HTTP log (`{at,route,status,duration_ms,idempotence_hash?,release_id?}`) for all bridge calls. | `artifacts/logs/` |
| `artifacts/ops/rails_open_scope.txt` | Summary confirming only bridge routes executed (`vendor_call_count: 0`). | `artifacts/ops/` |
| `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` | Indexed pointers + hash sentinel; every artifact has a `.path_proof.txt`. | `docs/evidence/`, `artifacts/` |

Acceptance is met when these artifacts are refreshed (canonical JSON, UTF-8, single trailing LF), `.path_proof.txt` files are updated, and both indices pass the mirror validation tests.
