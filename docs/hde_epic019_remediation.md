# HDE-EPIC019 remedial rails (Cards C1–C3)

This repo carries infra-owned wiring for the dev-only sampler HTTP harness (`POST /internal/dev/sampler`), Live QA harnesses for D3/D6, and evidence bindings that close the loop on EPIC019 without changing PF-Canon semantics.

## Canonical dev Reader start command

```bash
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 \
  scripts/dev_start_reader.sh
```

Notes:
- Uses `python -m adapter.http_reader` (binds to `0.0.0.0:<PORT>`, default 8000) and keeps rails closed.
- APP_ENV remains dev/admin-only; production runs must not use this harness.
- Harness tolerates empty/unset APP_ENV when invoked by QA scripts; APP_ENV gating remains enforced by the Reader handler.

## DEV_SAMPLER_URL source of truth
- Codespaces devcontainer exports `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` via `.devcontainer/devcontainer.json`.
- Scripts and docs should consume this env binding rather than guessing host/port. Update the value only when the Reader binding changes.

## Dev sampler healthcheck / gating diagnostic (closed rails)

Run the Engine-owned harness to exercise the dev HTTP sampler and record gating posture:

```bash
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
DEV_SAMPLER_URL="$DEV_SAMPLER_URL" \
scripts/qa/dev_sampler_healthcheck.py
```

Behavior:
- Starts the Reader for APP_ENV=dev, posts a minimal payload, and expects HTTP/1.1 200 with canonical JSON.
- Re-runs under APP_ENV=prod to record the current gate behavior (403 expected; mismatches are logged for follow-up).
- Logs live under `notes/dev-sampler/dev_sampler_healthcheck.log` alongside Reader stdout/stderr captures for each mode.

This harness is QA/diagnostic-only; it does not alter APP_ENV semantics or promote evidence.

## Dev sampler Live QA (D3 evidence, closed rails)

- Harness: `scripts/qa/dev_sampler_live_qa.py`
- Behavior: runs the dev Reader helper under APP_ENV permutations (dev/prod/empty) with closed rails, posts a seeded payload, and records governed JSONL and reader logs under `audit/qa/hde-epic019/dev_sampler_http/`.
- Evidence: wired into the EPIC019 acceptance map/manifest bindings; mirrors to Evidence Index/Mirror with path proofs.

## D6 open-rails vendor Live QA harness

- Harness: `scripts/qa/d6_live_vendor_qa.py`
- Rails: allows `ALLOW_NETWORK=1` (SAFE_MODE may be 0/1) for controlled vendor test identity only; not a CI determinism job.
- Outcomes: classified (`OK`, `FAIL_VENDOR`, `FAIL_TOOLING`) with governed logs and rails snapshot under `audit/qa/hde-epic019/d6-vendor-live-qa/`.
- Evidence: mapped to D6 tokens in the EPIC019 acceptance map and mirrored into Index/Mirror with path proofs.
