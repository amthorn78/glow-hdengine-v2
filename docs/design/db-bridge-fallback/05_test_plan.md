# Test Plan — DB Bridge Fallback

## Automated
- **Unit**: Inject connector stubs to simulate primary/bridge success and failure; assert typed errors and retry ordering.
- **Integration**: Run adapter CLI within `VERIFY.sh` using fabricated DSNs to verify canonical JSON and LF termination.
- **Transport**: Execute `tests/transport/test_internal_version_contract.py` and related suites to ensure headers stay unaffected.
- **Regression**: Extend `scripts/architecture_capture.sh` to record fallback artifacts and confirm idempotent replays.

## Manual
- Use `hdctl` against a dev Postgres instance with `DATABASE_URL` intentionally broken to observe bridge takeover.
- Validate `env-matrix` snapshots record fallback paths without altering refusal evidence layout.
- Review audit diffs to confirm ASCII-sorted keys and deduped arrays when fallback fires.

Exit criteria require all automated checks to pass and manual runs to capture refreshed evidence stored in `artifacts/db/` and indexed in `artifacts/evidence_index.jsonl`.
