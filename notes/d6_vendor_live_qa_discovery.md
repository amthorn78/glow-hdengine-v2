# D6 vendor live QA discovery (read-only pass)

## Vendor-facing surfaces (PF05/PF07/PF14 scope)
- **engine.cli bg:resolve --source vendor / showcompat vendor** via `scripts/ops/admin_vendor_qa.py`
  - Vendor: HDAPI (BodyGraph resolve/upsert) using Engine CLI.
  - Env: `SAFE_MODE`, `ALLOW_NETWORK`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`; rails summary printed and audit JSONL appended at `artifacts/ops/admin_vendor_calls.jsonl`.
  - QA doc footprint: admin parity checks, not explicitly tied to EPIC019.
- **Vendor ingest harness** via `scripts/ingest/run_vendor_ingest.py`
  - Vendor: HDAPI ingest path through `engine.bodygraph.ingest`.
  - Env: `SAFE_MODE`, `ALLOW_NETWORK`, locale pins, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HDE_BASE_URL`, DB URLs; captures `artifacts/runtime/env_matrix.snapshot.json` plus ingest logs.
  - QA docs: produces ingest evidence (idempotency, retry trace) referenced in evidence index but not in EPIC019 acceptance map.
- **Sampler dev live QA** via `scripts/qa/dev_sampler_live_qa.py`
  - Surface: sampler HTTP POST (local reader) not vendor transport; included for context (rails pinning + audit logs under `audit/qa/hde-epic019/dev_sampler_http`).
- **Provider shapers** (`engine/providers/vendor_http_hdapi.py`, `engine/bodygraph/vendor_client.py`)
  - Vendor: HDAPI request shaping, env keys `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`; defaults to HTTPS requirement in client, legacy default base in provider shim.
  - QA docs: leveraged by ingest/CLI; no live QA harness specific to D6 found.
- **Ops helper** `scripts/ops/admin_vendor_qa.py` logs rails, calls vendor and DB flows, writes artifacts under `artifacts/bodygraph` and `artifacts/compat`.

## Open-rails CI jobs
- `.github/workflows/ci.yml` pins closed rails globally (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) for all jobs; no open-rails vendor jobs found.
- `ci/checks/*` are closed-rails determinism/evidence guards; none set `ALLOW_NETWORK=1`.
- No dedicated Live Vendor QA CI job identified; EPIC019 acceptance map currently does not reference any open-rails job.

## D6 tokens & acceptance artifacts
- `docs/acceptance_map_epic019.json` currently defines foundations D1–D5 only; **no D6 foundation or tokens present**. Tokens like `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, `DISCOVERY_BASELINE_OK` are not defined or bound.
- `docs/acceptance_maps.json` lists EPIC017 and EPIC019 only (no D6 specifics).
- `audit/EPIC019_MANIFEST.json` mirrors the D1–D5 tokens only; no manifest entries for D6/vendor transport evidence.
- `docs/evidence/INDEX.json` contains vendor-related artifact keys (e.g., `ingest.vendor.*`, `ops.admin_vendor_calls`, retry/backoff proofs) but none are wired to EPIC019 acceptance map.

## Observations / gaps
- No existing D6-specific live vendor QA harness; closest is `scripts/ops/admin_vendor_qa.py` (admin parity) and ingest harness (idempotency) but neither logs D6 open-rails posture or failure classification per PF19.
- No rails snapshot or open-rails documentation for vendor QA within EPIC019 scope.
- CI does not exercise vendor network calls; any D6 evidence must be run manually/open-rails with `ALLOW_NETWORK=1` and logged explicitly.
