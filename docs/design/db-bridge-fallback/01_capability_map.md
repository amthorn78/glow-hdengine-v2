# Historical Capability Map — Retired bridge adapter evidence

Status: historical retained design record, not current runtime or operator guidance. The rows describe bridge-era behavior at capture time and must not be used to restore, execute, or refresh the retired transport.

| Capability | Owning Surface | Description | Evidence Hooks |
| --- | --- | --- | --- |
| Connection-time fallback | Adapter posture scripts, CLI runners | Historical retained record, not current guidance: attempted `DATABASE_URL`, then HTTPS `DB_BRIDGE_URL` through `BridgeProvider`; this fallback is retired and must not be restored. | Historical retained evidence, not current support: `docs/ADAPTER_DB.md`, `artifacts/db_bridge/adapter_selection.snapshot.json` |
| Deterministic posture envelopes | Historical env-matrix snapshots | Historical retained record, not current guidance: the bridge-era matrix recorded provider ordering without DB I/O. | Historical env-matrix baselines only. |
| Bridge introspection | Historical harnesses | Historical retained record, not current guidance: `scripts/db_bridge/capture_introspection.py` and the adapter harness exercised bridge endpoints; they must not be run. | Historical retained evidence, not current support: `artifacts/db_bridge/*.json`, `artifacts/db/*.json`, `artifacts/engine/*.json` |
| Keys-only telemetry | Historical rails-open harness | Historical retained record, not current guidance: bridge HTTP calls emitted keys-only metadata. No current bridge HTTP call is allowed. | `artifacts/logs/keys_only.sample.jsonl`, `artifacts/ops/rails_open_scope.txt` |
| Evidence cataloging | Docs + mirror | Historical retained record, not current guidance: bridge-era artifacts were cataloged with governed companions. | Current updater ownership remains unchanged. |

Current posture is direct-only through `engine.db.adapter.DBAccess` and psycopg. Retired configuration is refused before provider construction; there is no fallback surface or alternate transport.
