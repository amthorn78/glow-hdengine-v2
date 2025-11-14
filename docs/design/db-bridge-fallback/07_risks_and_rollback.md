# Risks & Rollback — Bridge adapter (EPIC-011)

## Key Risks
- **Invalid bridge URL**: Non-HTTPS URLs or missing `DB_BRIDGE_URL` block fallback. *Mitigation*: `BridgeProvider` enforces HTTPS and raises `bridge_requires_https` / `missing_bridge_url` early; adapter tests cover these paths.
- **Payload drift**: Bridge responses could add unexpected fields. *Mitigation*: harness scripts write canonical JSON checked into the Evidence Index; adapter normalization ensures search_path, grants, fingerprint, and version stay typed.
- **Logging leakage**: Mistakes could log bodies or headers. *Mitigation*: `engine.ops.http_log.log_http_call` only records keys `{at,route,status,duration_ms,idempotence_hash?,release_id?}`; tests guard the schema.
- **Silent vendor access**: Rails-open runs might hit vendor HTTP. *Mitigation*: `scripts/ops/capture_rails_open_scope.py` computes per-route counts and fails if any `vendor.*` entry appears.

## Rollback Strategy
1. Disable bridge usage by setting `DB_FORCE_PG=1` (or removing `DB_BRIDGE_URL`) while leaving harness scripts intact for parity checks.
2. Revert the adapter/bridge modules to the prior release tag and prune bridge artifacts from the Evidence Index (documenting removals in `docs/SYNC_LOG.md`).
3. Retain `artifacts/logs/keys_only.sample.jsonl` and scope reports for the rollback window to show vendor HTTP stayed disabled.

Rollback preserves canonical outputs and refuses to bypass the shared emitter; evidence remains auditable throughout the transition.
