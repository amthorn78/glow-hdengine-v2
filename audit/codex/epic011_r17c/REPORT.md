# HDE-EPIC011 Audit r17c

| Check | Status | Key Evidence | Notes |
| --- | --- | --- | --- |
| A1 – CLI help & parity | **FAIL** | `pyproject.toml`, `audit/codex/epic011_r17c/cli/help.txt` | `hdctl` console script is absent from PATH, so help capture begins with `bash: command not found: hdctl`; only `python -m engine.cli` exposes the `bg:resolve` command today. |
| A2 – bg:resolve (rails closed) | **FAIL** | `audit/codex/epic011_r17c/cli/bg_resolve.closed.db.json`, `audit/codex/epic011_r17c/cli/bg_resolve.closed.vendor.txt`, `engine/bodygraph/resolver.py` | DB invocation emits canonical JSON, but the vendor refusal envelope is printed to stdout while stderr is empty, so PF05 refusal proofing cannot rely on stderr capture. |
| A3 – Source selection snapshot | **PASS** | `audit/codex/epic011_r17c/bodygraph/source_selection.snap.json` | Snapshot shows SAFE rails refusing vendor without silently switching providers. |
| B1 – Vendor request shape | **PASS** | `engine/bodygraph/vendor_client.py`, `engine/providers/vendor_http_hdapi.py`, `audit/codex/epic011_r17c/vendor/request_shape.static.json` | Client shapes POST `/bodygraphs` with Accept + Content-Type + HD-Api-Key + HD-Geocode-Key + User-Agent and the `{birthdate,birthtime,location}` body. |
| B2 – Vendor env scan | **PASS** | `audit/codex/epic011_r17c/vendor/ingest_env_scan.json` | HD_API_KEY, GEO_API_KEY, and HDAPI_BASE_URL are referenced throughout provider code, tests, docs, and scripts. |
| B3 – Retry-After handling | **FAIL** | `engine/bodygraph/vendor_client.py`, `audit/codex/epic011_r17c/vendor/retry_after_parse.log` | `_retry_after_ms` only handles numeric strings; HTTP-date inputs return `None`, so 429 backoff posture is incomplete. |
| B4 – Rails-open vendor run | **ABSENT** | `audit/codex/epic011_r17c/cli/bg_resolve.open.vendor.json` | No stubbed vendor harness/cassette exists, so SAFE rails cannot be opened for a functional ingest capture. |
| C – DB posture | **PASS** | `artifacts/db/introspect.*.json`, `artifacts/db/boundary_view.readonly.proof.txt`, `audit/codex/epic011_r17c/db/posture.json` | Existing artifacts confirm search_path `hde, public`, grants inventory (165 entries), fingerprint objects, and read-only boundary views. |
| D – Adapter selection & bridge | **DRIFT** | `engine/db/adapter.py`, `engine/db/providers/bridge_provider.py`, `audit/codex/epic011_r17c/bridge/*.json` | Snapshot shows psycopg failure and bridge selection, but caps snapshot is derived from source declarations and no SELECT-parity proof ran. |
| E – Evidence hygiene | **PASS** | `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `audit/codex/epic011_r17c/evidence/mirror_check.json` | Human index, sha sentinel, and machine mirror all exist with canonical JSONL records + proof anchors. |
| F – Rails refusal proof | **PASS** | `audit/codex/epic011_r17c/rails/refusal_proof.txt` | Lower-case headers → blank line → canonical JSON body captured per PF05/PF12 guidance. |
| G – BodyGraph invariance | **ABSENT** | `fixtures/`, `audit/codex/epic011_r17c/bodygraph/invariance.summary.json` | No fixtures/bodygraph samples exist, so two-run and AB↔BA identities could not be executed. |
| H – Catalog presence | **ABSENT** | `audit/codex/epic011_r17c/docs/catalog_presence.json` | `docs/ENDPOINTS_CATALOG.json` and `.sha256` are missing. |

See `summary.json`, `locations.json`, `drift.json`, and `pfcanon/xref.json` for machine-readable status, references, and canon anchors.
