# Risks & Rollback — DB Bridge Fallback

## Key Risks
- **Misconfigured bridge DSN**: Non-Postgres URLs may slip through and cause runtime errors. *Mitigation*: strict prefix validation and unit tests covering HTTP/HTTPS rejection.
- **Divergent envelopes**: Fallback responses could deviate from canonical refusal format. *Mitigation*: reuse shared emitter and regression snapshots.
- **Silent data drift**: Bridge-hosted database may lag behind primary. *Mitigation*: capture schema/grant fingerprints and compare during audit reviews.
- **Operational ambiguity**: Operators might not know when fallback engaged. *Mitigation*: log keys-only events containing route, status, idempotence hash, release id.

## Rollback Strategy
1. Feature flag fallback helper behind configuration toggle defaulting to enabled; disable if incidents arise.
2. Revert posture scripts to primary-only connection by redeploying prior adapter build (tagged in release manifest).
3. Purge fallback-specific evidence entries while keeping baseline artifacts intact for traceability.
4. Notify audit trail maintainers via `docs/SYNC_LOG.md` entry summarizing the rollback window.

Rollback maintains canonical output expectations and preserves refusal capture workflow.
