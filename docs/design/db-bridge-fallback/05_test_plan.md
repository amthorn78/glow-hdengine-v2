# Historical Test Plan — Retired bridge adapter and evidence

Status: historical retained design record, not a current test plan or runbook. The bridge-era tests and harness commands below must not be restored or executed.

## Automated
- **Unit**: Historical retained record, not current guidance: bridge-era tests asserted fallback ordering and bridge payload normalization.
- **HTTP logging**: `tests/ops/test_http_logging.py` validates the keys-only schema and rounding of `engine.ops.http_log.log_http_call`.
- **Evidence parity**: `tests/ops/test_evidence_index.py` ensures every governed artifact has matching `.path_proof.txt`, human index entry, machine mirror record, sha256, and size parity.
- **Adapter contracts**: Historical retained record, not current guidance: bridge-era tests covered bridge probes and network error mapping.

## Manual / harness
- Historical retained command, not current guidance: `python scripts/db_bridge/capture_introspection.py` wrote `artifacts/db_bridge/` captures and must not be run.
- Historical retained command, not current guidance: the adapter introspection harness mirrored bridge payloads and must not be used to claim current support.
- Historical retained command, not current guidance: the rails-open scope harness observed bridge routes and must not be rerun for this retirement.
- Historical retained record, not current guidance: bridge-era env-matrix snapshots remain frozen inputs, not current selection proof.

Current exit criteria are owned by the direct-only PR-06R-A contract. They require static guidance scanning, direct-only selection/refusal coverage, and preservation of historical bytes; they do not permit bridge harness execution or refresh.
