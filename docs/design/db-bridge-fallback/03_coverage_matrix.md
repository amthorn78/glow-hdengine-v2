# Historical Coverage Matrix — Retired bridge provider and evidence

Status: historical retained design record, not current test or operator guidance. These cases describe bridge-era coverage and must not be rerun as current transport proof.

| Scenario | Direct endpoint | Retired endpoint | Historical result | Historical verification |
| --- | --- | --- | --- | --- |
| Primary succeeded | Reachable psycopg DSN | Historical retained record, not current guidance: `DB_BRIDGE_URL` was optional. | Adapter returned psycopg. | Historical adapter snapshot. |
| Primary failed, bridge succeeded | Invalid/timeout | Historical retired pg-bridge URL | Historical retained record, not current guidance: the adapter selected the bridge; this fallback must not be restored. | Historical retained record, not current guidance: `scripts/db_bridge/capture_introspection.py` and adapter snapshots. |
| Both failed | Invalid | Missing/invalid | Historical typed bridge-era failure. | Historical tests only; not current support. |
| Rails-open scope | Any | Historical retired pg-bridge URL | Historical keys-only bridge routes. | Historical scope summary only; it must not be rerun. |
| Env-matrix selection | Unset | Historical retired pg-bridge URL | Historical retained record, not current guidance: fallback ordering. | Historical env-matrix baseline only. |

Historical retained evidence, not current guidance: `artifacts/db_bridge/` bytes remain frozen and auditable with their existing governed companions. Current tests prove direct-only selection, refusal-before-I/O, one attempt, and no alternate provider.
