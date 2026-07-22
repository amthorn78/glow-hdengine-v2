# Secrets and environment variables

## Active database secret

- `DATABASE_URL` - Direct PostgreSQL DSN used by the current HDE DB adapter. Treat the value as secret; diagnostics may record only presence or `SET_REDACTED`.

## Vendor and geocoding secrets

- `HD_API_KEY` - Vendor API credential. Logs and evidence may record only `SET`/`UNSET` or `REDACTED`.
- `GEO_API_KEY` - Geocoding credential. Logs and evidence may record only `SET`/`UNSET` or `REDACTED`.
- `HD_API_BASE_URL` and compatibility-only `HDAPI_BASE_URL` are endpoint configuration. Treat concrete base URLs as sensitive operational configuration in step logs; record `SET`/`UNSET` or `REDACTED`, not the value.

## Rails and application posture

- Closed rails default to `SAFE_MODE=1` and `ALLOW_NETWORK=0`.
- Open rails require explicit task authorization and must keep secrets redacted in logs.
- `APP_ENV` controls dev/test/local versus non-dev behavior and should be recorded as a non-secret environment label when needed.
- Port variables and local app URLs are operational configuration; avoid persisting private hostnames or tunnel URLs in governed evidence.

## Locale, timezone, and identity posture

- Deterministic checks run with `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.
- Release and service identity values are governed evidence; do not hand-edit identity artifacts, manifests, checksums, or path proofs.
- If identity drift appears during a source-only remediation, stop and report it rather than refreshing identity evidence.

## Redaction discipline

- Step logs must not include secrets, tokens, DSNs, bearer values, raw vendor headers, raw request/response payloads, or birth-input values.
- Environment probes should record secrets and base URLs only as `REDACTED`, `SET`, or `UNSET`.
- Keys-only logs must retain names/status only and must not persist raw values.

## Retired database transport keys

The following names are retired and are refusal-only current configuration: `DB_ALLOW_BRIDGE_IN_PROD`, `DB_BRIDGE_URL`, and `DB_FORCE_BRIDGE`. Their presence, even with empty or whitespace values, fails DB provider selection before provider construction or external I/O. Do not configure them for current HDE runtime behavior.

Historical evidence may still mention bridge-era names as immutable history; that does not make them active configuration.
