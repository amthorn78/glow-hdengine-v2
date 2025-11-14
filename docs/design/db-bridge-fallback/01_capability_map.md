# Capability Map — Bridge adapter evidence

| Capability | Owning Surface | Description | Evidence Hooks |
| --- | --- | --- | --- |
| Connection-time fallback | Adapter posture scripts, CLI runners | Attempt `DATABASE_URL`, then HTTPS `DB_BRIDGE_URL` through `BridgeProvider`; fail with typed `AdapterError` when both unusable. | `docs/ADAPTER_DB.md`, `artifacts/db_bridge/adapter_selection.snapshot.json` |
| Deterministic posture envelopes | `env-matrix` snapshots, transport harness | Selection-only env matrix records provider ordering without touching the DB. | `AGENTS.md` env-matrix rule, `artifacts/runtime/env_matrix.*.json` |
| Bridge introspection | `scripts/db_bridge/capture_introspection.py`, `scripts/db_adapter/capture_adapter_introspection.py` | Exercise `/health`, `/`, `/query`, `/introspect/{search_path,grants,fingerprint}`, and adapter helpers to capture canonical JSON. | `artifacts/db_bridge/*.json`, `artifacts/db/*.json`, `artifacts/engine/*.json` |
| Keys-only telemetry | `engine/ops/http_log.py`, rails-open harness | Record `{at,route,status,duration_ms,idempotence_hash?,release_id?}` for every bridge HTTP call; summarize scope under open rails. | `artifacts/logs/keys_only.sample.jsonl`, `artifacts/ops/rails_open_scope.txt` |
| Evidence cataloging | Docs + mirror | `.path_proof.txt`, human index, and machine mirror entries update in the same PR. | `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` |

Each capability preserves the repo invariants: canonical JSON, deduped set representations, and refusal logging discipline. The fallback surface must never bypass the presenter or alter transport/auth baselines.
