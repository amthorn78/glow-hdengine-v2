# Adapter Architecture — Bridge provider selection

## Connection Flow
1. `DBAccess.for_current_env` resolves `DATABASE_URL` and `DB_BRIDGE_URL` from the environment.
2. The adapter attempts psycopg via `DATABASE_URL` first, running a health check before returning the provider.
3. If the primary is unavailable (or `DB_FORCE_BRIDGE=1`), the adapter instantiates `BridgeProvider` with HTTPS `DB_BRIDGE_URL`, calls `GET /health`, and records the attempt in `artifacts/db_bridge/adapter_selection.snapshot.json`.
4. Bridge operations (`query`, `introspect_*`, `tx`) use the shared `_json_request` helper, which wraps network failures as typed adapter errors and logs keys-only metadata.

## Module Responsibilities
- `engine/db/adapter.py`: provider selection, typed attempts, and adapter-level introspection helpers.
- `engine/db/providers/bridge_provider.py`: HTTPS client (`/health`, `/`, `/query`, `/introspect/{search_path,grants,fingerprint}`, version probe) with keys-only logging and typed error mapping.
- `engine/ops/http_log.py`: append-only JSONL sink for `{at,route,status,duration_ms,idempotence_hash?,release_id?}`.
- `scripts/db_bridge/capture_introspection.py`, `scripts/db_adapter/capture_adapter_introspection.py`, `scripts/ops/capture_rails_open_scope.py`: harnesses that exercise the bridge and adapter surfaces.

## Integration Points
- Transport suites ensure refusal surfaces remain unchanged while the adapter selects bridge fallback.
- CLI (`hdctl`, `engine.cli`) reuses `DBAccess` so evidence harnesses and runtime commands share the same selection flow.
- Evidence indices (`docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`) and `.path_proof.txt` files are updated in the same PR as harness captures (PF09 / PF12 discipline).

The architecture keeps fallback deterministic and observable: selection snapshots, keys-only logs, and canonical JSON artifacts make bridge usage auditable without exposing payload bodies or secrets.
