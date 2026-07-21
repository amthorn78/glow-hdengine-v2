# DB adapter current behavior

Current HDE database access is direct-only. Call `DBAccess.for_current_env(...)` to select the sole active provider: Glow-owned `psycopg` using `DATABASE_URL`.

Retired bridge configuration keys are refusal-only: `DB_ALLOW_BRIDGE_IN_PROD`, `DB_BRIDGE_URL`, and `DB_FORCE_BRIDGE`. If any of those names are present in the process environment, selection raises a typed retired-configuration error before reading `DATABASE_URL`, constructing a provider, or performing external I/O. Values are never serialized.

`DATABASE_URL` remains secret material and must be recorded only as present/absent or redacted. Missing or unavailable direct PostgreSQL fails closed; there is no active bridge fallback or alternate database transport.
