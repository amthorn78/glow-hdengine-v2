# Test Plan — Bridge adapter & evidence

## Automated
- **Unit**: Adapter/provider tests inject success/failure stubs to assert fallback ordering, typed error codes, and JSON normalization for `introspect_*`.
- **HTTP logging**: `tests/ops/test_http_logging.py` validates the keys-only schema and rounding of `engine.ops.http_log.log_http_call`.
- **Evidence parity**: `tests/ops/test_evidence_index.py` ensures every governed artifact has matching `.path_proof.txt`, human index entry, machine mirror record, sha256, and size parity.
- **Adapter contracts**: `tests/db/test_adapter_contract.py` covers bridge version probe, search_path/grants/fingerprint normalization, and network error mapping.

## Manual / harness
- `python scripts/db_bridge/capture_introspection.py` — confirm bridge endpoints return canonical JSON and write to `artifacts/db_bridge/` + `artifacts/db/`.
- `python scripts/db_adapter/capture_adapter_introspection.py` — ensure adapter-level snapshots mirror bridge payloads without leaking secrets.
- `python scripts/ops/capture_rails_open_scope.py` — run after the above harnesses to verify only `db_bridge.*` routes were logged and that `vendor_call_count: 0`.
- Spot-check `artifacts/runtime/env_matrix.snapshot.json` / `env_matrix.diff.json` to confirm selection snapshots remain single-object, canonical JSON.

Exit criteria: automated suites green, harnesses refreshed under open rails, and all resulting artifacts indexed with up-to-date `.path_proof.txt`, `docs/evidence/INDEX.json`, and `artifacts/evidence_index.jsonl` entries.
