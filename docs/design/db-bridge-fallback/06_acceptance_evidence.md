# Historical Evidence Inventory — Retired bridge adapter (EPIC-011)

Status: historical retained evidence inventory, not current acceptance guidance. The listed bridge-era bytes retain their original provenance and must not be refreshed, reinterpreted as current support, or used to claim token satisfaction.

| Evidence | Description | Storage |
| --- | --- | --- |
| Historical retained evidence, not current support: `artifacts/db_bridge/adapter_selection.snapshot.json` | Bridge-era provider attempts and final selection; must not be recomputed. | Historical retained `artifacts/db_bridge/`, not a current output home. |
| Historical retained evidence, not current support: `artifacts/db_bridge/{health.json,root.json,query_select_1.json}` | Bridge-era HTTP captures; must not be treated as current service availability. | Historical retained `artifacts/db_bridge/`, not a current output home. |
| Historical retained evidence, not current support: `artifacts/db/introspect.{search_path,grants,fingerprint}.json` | Bridge-era introspection payloads. | `artifacts/db/` |
| Historical retained evidence, not current support: `artifacts/engine/db_adapter.{version,search_path,fingerprint}.json` | Bridge-era adapter-normalized outputs. | `artifacts/engine/` |
| Historical retained evidence, not current support: `artifacts/logs/keys_only.sample.jsonl` | Bridge-era keys-only HTTP log; it must not be interpreted as current bridge activity. | `artifacts/logs/` |
| Historical retained evidence, not current support: `artifacts/ops/rails_open_scope.txt` | Bridge-era route summary; it must not be rerun or treated as current support. | `artifacts/ops/` |
| `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` | Indexed pointers + hash sentinel; every artifact has a `.path_proof.txt`. | `docs/evidence/`, `artifacts/` |

Historical integrity is preserved by byte/checksum, readability, provenance, secret-safety, and historical-nonclaim checks only. This inventory makes no current provider-parity, service-availability, QA, token, deployment, PF09, or closeout claim.
