# Coverage Matrix — DB Bridge Fallback

| Scenario | DATABASE_URL | DB_BRIDGE_URL | Expected Result | Verification |
| --- | --- | --- | --- | --- |
| Primary succeeds | Valid Postgres DSN | Optional | Use `DATABASE_URL`; do not touch bridge. | Posture smoke run in `VERIFY.sh`.|
| Primary fails, bridge succeeds | Invalid/timeout | Valid Postgres DSN | Connect via bridge; emit success artifacts with fallback note. | Targeted harness run in `scripts/architecture_capture.sh`.|
| Both fail | Invalid | Missing/invalid | Emit `missing_db_config` failure envelope; no partial writes. | Unit test asserts typed error and refusal format.|
| Bridge non-Postgres | Valid primary | HTTP/empty | Skip bridge attempt; rely on primary; warn during validation. | Static config validator in CLI smoke test.|
| Env-matrix selection | Unset | Postgres DSN | Snapshot run chooses bridge path; envelopes frozen for review. | `env-matrix` capture log + audit diff.| 

Coverage ensures fallback behavior remains deterministic across CLI, adapter server, and automated snapshots. All evidence is LF-terminated and cataloged under `artifacts/db/`.
