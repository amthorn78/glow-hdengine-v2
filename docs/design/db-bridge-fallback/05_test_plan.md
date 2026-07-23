# Historical Test Plan — Retired bridge adapter and evidence

Status: historical retained design record, not a current test plan or runbook. The bridge-era tests and harness commands below must not be restored or executed.

## Automated
- **Unit**: Historical retained record, not current guidance: bridge-era tests asserted fallback ordering and bridge payload normalization.
- **HTTP logging**: `tests/ops/test_http_logging.py` validates the keys-only schema and rounding of `engine.ops.http_log.log_http_call`.
- **Evidence parity**: `tests/ops/test_evidence_index.py` ensures every governed artifact has matching `.path_proof.txt`, human index entry, machine mirror record, sha256, and size parity.
- **Adapter contracts**: Historical retained record, not current guidance: bridge-era tests covered bridge probes and network error mapping.

## Manual / harness
- Historical retained command, not current guidance: `python scripts/db_bridge/capture_introspection.py` wrote `artifacts/db_bridge/` captures and must not be run.
- Historical retained behavior, not current guidance: bridge-era revisions of `scripts/db_adapter/capture_adapter_introspection.py` and `scripts/ops/capture_rails_open_scope.py` mirrored bridge payloads and observed bridge routes; those revisions must not be restored or used to claim current support.
- Current direct-only behavior: `scripts/db_adapter/capture_adapter_introspection.py` delegates only to `DBAccess`/psycopg, and `scripts/ops/capture_rails_open_scope.py` invokes only that direct harness after retired-key refusal. PR-06R-A exercises their source and fixture tests only; it does not run a database or open-rails capture.
- Historical retained record, not current guidance: bridge-era env-matrix snapshots remain frozen inputs, not current selection proof.

Current exit criteria are owned by the direct-only PR-06R-A contract. They require static guidance scanning, direct-only selection/refusal coverage, and preservation of historical bytes; they do not permit bridge harness execution or refresh. Authorization-bound OPS-03 uses its separate runner after PR-06R-A, and PR-06R-B alone owns final evidence admission.
