# Historical Risks and Current Rollback Boundary — Retired bridge adapter

Status: historical retained design record plus a current non-restoration boundary; it is not a bridge operations runbook.

## Key Risks
- **Historical invalid-URL risk**: Historical retained record, not current guidance: `DB_BRIDGE_URL` and `BridgeProvider` once enforced bridge URL policy; both are retired and must not be restored.
- **Historical payload drift**: Historical retained record, not current guidance: bridge-era captures used canonical JSON and normalized fields.
- **Historical logging leakage**: Historical retained record, not current guidance: bridge-era HTTP logging was keys-only.
- **Historical silent external access**: Historical retained record, not current guidance: a bridge-era rails-open harness counted routes; it must not be rerun as current proof.

## Rollback Strategy
1. Current rollback must not restore bridge selection, retired keys, HTTP calls, harnesses, or provider parity.
2. If direct-only DB entrypoints are unsafe, block them or revert to a known direct-only commit; never revert to bridge-enabled source.
3. Preserve historical bridge primaries and their checksum/provenance records byte-for-byte; do not prune or refresh them during runtime rollback.

Rollback remains fail closed, preserves public bytes and historical evidence truth, and does not authorize OPS, DB writes, deployment, or PF09 movement.
