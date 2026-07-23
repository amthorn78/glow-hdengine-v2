# Historical Adapter Architecture — Retired bridge provider selection

Status: historical retained design record, not current runtime or operator guidance. The flow below describes bridge-era behavior and must not be executed or restored.

## Connection Flow
1. Historical retained record, not current guidance: `DBAccess.for_current_env` once resolved `DATABASE_URL` and `DB_BRIDGE_URL`.
2. Historical retained record, not current guidance: the bridge-era adapter attempted psycopg first.
3. Historical retained record, not current guidance: `DB_FORCE_BRIDGE`, `BridgeProvider`, `DB_BRIDGE_URL`, bridge health I/O, and `artifacts/db_bridge/adapter_selection.snapshot.json` belonged to the retired fallback and must not be restored or executed.
4. Historical retained record, not current guidance: bridge operations once used a shared HTTP helper and keys-only logging; current DB access must not make bridge HTTP requests.

## Module Responsibilities
- Current: `engine/db/adapter.py` is the sole provider selector and permits direct psycopg only.
- Historical retained record, not current guidance: `engine/db/providers/bridge_provider.py` was the retired HTTPS client and must not exist as active source.
- Historical retained record, not current guidance: `engine/ops/http_log.py` recorded bridge-era keys-only metadata; it is not a bridge execution surface.
- Historical retained record, not current guidance: `scripts/db_bridge/capture_introspection.py` and related bridge harnesses must not be run or restored.

## Integration Points
- Current transport suites prove retired-key refusal and direct-only selection without fallback or external I/O.
- CLI (`hdctl`, `engine.cli`) reuses `DBAccess` so evidence harnesses and runtime commands share the same selection flow.
- Historical retained record, not current guidance: bridge-era captures were cataloged with governed companions. Historical primary bytes must not be refreshed or reclassified as current support by a runtime harness.

Historical bridge bytes remain auditable as history only. They do not prove current service availability, transport support, provider parity, or acceptance-token satisfaction.
