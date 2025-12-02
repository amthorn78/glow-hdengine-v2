# HDE-EPIC019 remedial rails (Card C1)

This repo now carries infra-owned wiring for the dev-only sampler HTTP harness (`POST /internal/dev/sampler`). The goal is to make the harness reproducible in Codespaces/local dev without changing PF-Canon semantics.

## Canonical dev Reader start command

```bash
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 \
  scripts/dev_start_reader.sh
```

Notes:
- Uses `python -m adapter.http_reader` (binds to `0.0.0.0:<PORT>`, default 8000) and keeps rails closed.
- APP_ENV remains dev/admin-only; production runs must not use this harness.

## DEV_SAMPLER_URL source of truth
- Codespaces devcontainer now exports `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` via `.devcontainer/devcontainer.json`.
- Scripts and docs should consume this env binding rather than guessing host/port. Update the value only when the Reader binding changes.

## Dev sampler healthcheck / gating diagnostic

Run the Engine-owned harness to exercise the dev HTTP sampler and record gating posture:

```bash
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler \
scripts/qa/dev_sampler_healthcheck.py
```

Behavior:
- Starts the Reader for APP_ENV=dev, posts a minimal payload, and expects HTTP/1.1 200 with canonical JSON.
- Re-runs under APP_ENV=prod to record the current gate behavior (403 expected; mismatches are logged for follow-up).
- Logs live under `notes/dev-sampler/dev_sampler_healthcheck.log` alongside Reader stdout/stderr captures for each mode.

This harness is QA/diagnostic-only; it does not alter APP_ENV semantics or promote evidence.
