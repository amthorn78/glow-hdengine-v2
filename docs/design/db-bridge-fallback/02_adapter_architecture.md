# Adapter Architecture — DB Bridge Fallback

## Connection Flow
1. Configuration loader resolves `DATABASE_URL` and `DB_BRIDGE_URL` from process environment using existing adapter config helpers.
2. Posture script invokes psycopg connector with `DATABASE_URL` first.
3. On connection failure, validator confirms `DB_BRIDGE_URL` begins with `postgres://` or `postgresql://`; HTTP bridges are rejected up front.
4. Successful connection is passed to the migration runner and data exporters; failures surface as typed errors routed through the shared emitter.

## Module Responsibilities
- `adapter/http_reader.py`: entrypoint for CLI-invoked posture runs; ensures presenter/emitter wiring remains canonical.
- `engine/mech/helpers.py`: provides array-as-set normalization for schema diffs before serialization.
- `artifacts/db/*`: receives LF-terminated canonical artifacts keyed by posture id.
- `docs/ADAPTER_DB.md`: authoritative policy; this design expands on its fallback sequence and rejection rules.

## Integration Points
- Transport harnesses (`tests/transport`) assert headers and refusal structure remain unchanged when fallback activates.
- CLI (`hdctl`, `engine.cli`) reuses the same fallback helper to ensure parity across user interfaces.
- Audit snapshots (`audit/docs_snapshot_r7/`) continue to snapshot posture outputs without DB availability.

The architecture treats fallback as a thin retry wrapper around existing Postgres flows; it does not introduce new protocols or bypass the adapter’s lifecycle hooks.
