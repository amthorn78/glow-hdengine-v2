# Historical Change List — Retired bridge adapter and evidence

Status: historical retained design record, not a current change list or implementation guide. These bridge-era actions must not be replayed.

1. Historical retained record, not current guidance: bridge-era `DBAccess` attempted psycopg and then HTTPS bridge and wrote `artifacts/db_bridge/adapter_selection.snapshot.json`; current runtime must not do either bridge action.
2. Historical retained record, not current guidance: `DB_BRIDGE_URL` and bridge HTTP error codes belonged to the retired transport and must not be configured or restored.
3. Historical retained record, not current guidance: adapter introspection normalized bridge-era payloads.
4. Historical retained record, not current guidance: bridge HTTP requests emitted keys-only metadata; current DB access must not issue bridge HTTP requests.
5. Historical retained record, not current guidance: `scripts/db_bridge/capture_introspection.py` and related harnesses captured bridge bytes and must not be run or restored.
6. Historical retained record, not current guidance: the bridge-era change updated docs and governed companions together. Current historical primary bytes must not be rewritten.
