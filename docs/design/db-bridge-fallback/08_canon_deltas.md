# Historical Canon Delta Record — Retired bridge adapter (EPIC-011)

Status: historical retained design record, not current canon or implementation guidance. The bridge-era delta is superseded on the exact transport topic by the approved direct-only decision.

| Area | Prior Canon | Delta | Notes |
| --- | --- | --- | --- |
| Connection precedence | Psycopg-only | Historical retained record, not current guidance: psycopg once preceded `DB_BRIDGE_URL` through `BridgeProvider`; that fallback must not be restored. | Historical design only; no current transport support. |
| Bridge validation | Historical fallback | Historical retained record, not current guidance: the retired bridge once required HTTPS and typed errors. | Superseded for current execution. |
| Introspection surface | Manual SQL probes | Historical retained record, not current guidance: adapter helpers once delegated to bridge endpoints. | Historical shapes only. |
| Logging and telemetry | Route-specific logging only | Historical retained record, not current guidance: bridge-era HTTP logging was keys-only. | Historical secret-safety posture remains descriptive only. |
| Evidence discipline | Partial indexing | Mandate `.path_proof.txt` files and synchronized updates to `docs/evidence/INDEX.json` + `artifacts/evidence_index.jsonl` for every governed artifact. | Reinforces PF09 / PF12 acceptance tokens. |

Current execution is direct-only through psycopg. Historical bridge bytes stay deterministic and auditable but do not prove current service availability, provider parity, acceptance, QA, PF09 movement, deployment, or closeout.
