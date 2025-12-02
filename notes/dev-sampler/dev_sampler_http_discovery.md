# Dev sampler HTTP harness discovery (EPIC019 Card C1)

## Handler and routing
- Route defined in `adapter/http_reader.py` as `@bp.route("/internal/dev/sampler", methods=["POST"], provide_automatic_options=False)`.
- APP_ENV gate `_dev_admin_gate()` allows only `dev`, `test`, or `local`; any other, missing, or empty value returns a writer-style `forbidden` error (HTTP 403) without invoking the sampler core.
- Request body is parsed via `_read_writer_json` permitting keys `viewer_id`, `candidate_ids`, `seed`; empty body or validation error returns the corresponding writer error.
- Validation requires `viewer_id` non-empty string, `candidate_ids` non-empty list of non-empty strings; optional `seed` echoed via `meta.seed` (stringified or null) but does not affect ranking. Extra or malformed input yields `invalid_input` (422).
- Response built from sampler core `sample_and_rank` output and emitted via `emit_compact_json` with `Content-Type: application/json; charset=utf-8` and `Cache-Control: no-store` and no `ETag`; HTTP status 200 on success.

## Reader start commands observed
- The adapter includes a dev runner at the bottom of `adapter/http_reader.py` invoked with `python -m adapter.http_reader`, binding to host `0.0.0.0` and port from `PORT` env (default 8000).
- Documentation hints align with this runner (`README.md` and `docs/ADAPTER_009.md` mention `python -m adapter.http_reader`; PF10 notes observe it responding on `http://127.0.0.1:8000/internal/dev/sampler`).
- A legacy dev harness exists at `dev/reader_harness/app.py` (Flask app under `/api`) but not wired as the canonical start command; no Make targets or devcontainer tasks currently start the Reader automatically.

## DEV_SAMPLER_URL findings
- No repository-wide environment binding currently sets `DEV_SAMPLER_URL`; `.devcontainer/devcontainer.json` only pins locale/timezone and PATH.
- Prior exploratory notes propose `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` (e.g., `notes/dev-sampler/DEV_SAMPLER_URL.decided` and PF10 build notes addendum), but there is no single authoritative config value checked into infra.
- QA/audit logs reference both port 8000 and 2000, so a canonical source of truth is still needed.
