# Secrets and environment variables

## Active database secret

- `DATABASE_URL` - Direct PostgreSQL DSN used by the current HDE DB adapter. Treat the value as secret; diagnostics may record only presence or `SET_REDACTED`.

## Retired database transport keys

The following names are retired and are refusal-only current configuration: `DB_ALLOW_BRIDGE_IN_PROD`, `DB_BRIDGE_URL`, and `DB_FORCE_BRIDGE`. Their presence, even with empty or whitespace values, fails DB provider selection before provider construction or external I/O. Do not configure them for current HDE runtime behavior.

Historical evidence may still mention bridge-era names as immutable history; that does not make them active configuration.
