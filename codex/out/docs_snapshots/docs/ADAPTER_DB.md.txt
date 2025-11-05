# DB Connectivity - Attempt-Both Resolver

- Default preference: attempt DSN then Bridge. The first successful path becomes active.
- Bridge requests require `SAFE_MODE=0` and `ALLOW_NETWORK=1` before any outbound calls.
- DSN path enforces `search_path` `hde, public` with a 5s connect timeout.
- `/internal/version` stays DB-decoupled and does not import the resolver.
- Evidence artifacts: `artifacts/db/attempts.json`, `artifacts/db/rw_smoke.txt` (both LF-terminated, compact JSON where applicable).
