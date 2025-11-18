# EPIC011 Production QA Runbook — Rails Window + Ingest/Parity Proofs

## Purpose & Scope
This runbook defines the exact operator choreography for **EPIC011 — Vendor Ingest & Data Durability** in production. It is the only approved procedure for capturing the evidence that a single consented test user can be ingested from the vendor, persisted in prod, resolved from the DB-first hot path, proven byte-identical against the vendor payload, and refused when rails are closed. Follow these instructions only when performing the scheduled QA dry-run; do **not** call production outside the documented rails-open window.

## Preconditions
- **Rails default**: Production rails are closed (SAFE_MODE=1 and/or ALLOW_NETWORK=0). No vendor calls may run until the temporary window is opened in Step 2.
- **Consented UUID**: The PO supplies one prod-safe, consented test user UUID that will be used for every call in this runbook.
- **Vendor credentials**: HDAPI_BASE_URL, HD_API_KEY, and related env vars are already configured on the prod Engine host, but rails stay closed until Step 2.
- **System of Truth endpoints**: The PROD_ENDPOINTS SoT file (`docs/run/PROD_ENDPOINTS.json`) is available; operators derive the base URL and ops routes from it at runtime. This runbook references the file by name and does not re-list any URLs.
- **Operator roles**: Ops owns SAFE_MODE/ALLOW_NETWORK toggles; QA owns CLI/HTTP captures. Both acknowledge the scheduled window start/end in writing before Step 2.

## Step 1 — Capture Pre-window Refusal (Rails Closed)
1. Confirm that either SAFE_MODE=1 or ALLOW_NETWORK=0 (or both). Rails must be closed.
2. Call the ops resolve route (`_ops/bodygraph/resolve`) or `python -m engine.cli bg:resolve --user <UUID> --source vendor --upsert true` with the consented UUID, while rails are closed. This call must target `source="vendor"` with `upsert=true` so the Engine refuses it.
3. Save headers and body to temporary files exactly as received. Normalize header names to lower-case and ensure `cache-control: no-store` is present. The refusal response must not include `etag`, `vary`, or compression headers.
4. Combine headers + body into `artifacts/proofs/ops_refusal_proof.txt` under a clearly labeled section `# PRE-WINDOW`. Each section must render as:
   ```
   # PRE-WINDOW
   header-name: value
   cache-control: no-store
   ...

   {"error":"...","status":"refused"}
   ```
   - Headers stay lower-case.
   - Exactly one blank line separates headers from body.
   - The JSON body is numeric-free (no codes embedded in strings) and LF-terminated.
   - No fabricated timestamps; record exactly what prod returned.

## Step 2 — Open Rails (Temporary Ops Window)
1. Ops sets `SAFE_MODE=0` **and** `ALLOW_NETWORK=1` for the Engine process (per host-specific procedure). Document the window start/end in ops notes.
2. No vendor calls may occur outside this window. Keep the window as short as possible—just long enough to finish Steps 3–5.

## Step 3 — Vendor Upsert Ingest (Rails Open)
1. Run the explicit vendor resolve/upsert call for the consented UUID, e.g.:
   ```bash
   python -m engine.cli bg:resolve --user <UUID> --source vendor --upsert true --emit-json
   ```
   or invoke the HTTP route derived from `docs/run/PROD_ENDPOINTS.json` with the same parameters.
2. Confirm the response shows a successful vendor hit (the CLI prints `source":"vendor"` in the JSON) and that the Engine persisted the BodyGraph row.
3. Save the full JSON response (no redactions) to `artifacts/bodygraph/vendor_upsert.<UUID>.json`. Ensure the file is canonical JSON with one trailing LF.

## Step 4 — DB Resolve (DB-first Hot Path)
1. Immediately resolve the same UUID through the DB-only source:
   ```bash
   python -m engine.cli bg:resolve --user <UUID> --source db --emit-json
   ```
   (or the equivalent HTTP call with `source=db` and no `upsert` flag).
2. Save the JSON response to `artifacts/bodygraph/db_resolve.<UUID>.json`. This file should reflect the persisted BodyGraph without any vendor network access.
3. Confirm the CLI/HTTP output shows `source":"db"` so the run proves the prod default is DB-first even when rails are open.

## Step 5 — Byte-level Parity Check
1. Use the shared presenter/emitter parity helper (e.g., `python -m presenter.json_canon_compare artifacts/bodygraph/vendor_upsert.<UUID>.json artifacts/bodygraph/db_resolve.<UUID>.json`) or the ops script that canonicalizes both payloads with the same emitter.
2. Record the parity outcome to `artifacts/presenter/json_canon_compare.log` using the structure:
   ```
   compare: FILE_EQ_CANON_BYTES_OK   # or compare: DIFF
   ab_sha256: <sha256 of vendor_upsert file>
   ba_sha256: <sha256 of db_resolve file>
   ```
   - Use canonical JSON bytes for hashing.
   - Do not insert actual hashes in this repo; the operator will fill them in during the live run.
3. If the comparison reports `DIFF`, note the discrepancy in the log and coordinate with engineering before proceeding.

## Step 6 — Close Rails and Capture Post-window Refusal
1. Ops restores the default posture: `SAFE_MODE=1` and/or `ALLOW_NETWORK=0` (rails closed).
2. Repeat the refusal capture from Step 1, again calling `source="vendor"` with `upsert=true` so prod rejects it.
3. Append a new section `# POST-WINDOW` to `artifacts/proofs/ops_refusal_proof.txt` using the same formatting requirements (lower-case headers, `cache-control: no-store`, no `etag/vary/compression`, exactly one blank line before the numeric-free JSON body). The file now contains both pre- and post-window refusal envelopes.

## Evidence Table & Acceptance Tokens
| Artifact | Purpose | Acceptance Tokens Satisfied |
| --- | --- | --- |
| `artifacts/proofs/ops_refusal_proof.txt` | Demonstrates rails are closed outside the window, both before and after, with canonical refusal formatting. | SNAPSHOT_HEADER_LOWERCASE_OK, BG_VENDOR_CALLS_DISABLED_IN_PROD_OK |
| `artifacts/bodygraph/vendor_upsert.<UUID>.json` | Captures the successful vendor ingest while rails are open. | INGEST_OK |
| `artifacts/bodygraph/db_resolve.<UUID>.json` | Shows DB-first resolution for the same user without re-hitting the vendor. | INGEST_IDEMPOTENT_OK, BG_SOURCE_SELECTION_OK |
| `artifacts/presenter/json_canon_compare.log` | Proves byte-level parity between vendor ingest and DB resolve outputs. | BG_SOURCE_INVARIANCE_OK |

This runbook is preparatory; the actual QA execution will populate the governed artifacts and update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in a follow-up PR.

## Operator Inputs (Supplied at Runtime)
- Consented prod test user UUID (single value reused in all steps).
- Scheduled start/end timestamps for the rails-open window, approved by ops + PO.
- Confirmation that vendor credentials are configured before Step 3.

## Post-run Expectations
- No prod code paths change; only artifacts under `artifacts/proofs/`, `artifacts/bodygraph/`, and `artifacts/presenter/` are produced during QA.
- Refusal proofs remain deterministic and numeric-free.
- Vendor ingest happens only inside the documented window.
- All evidence files will later be indexed by path-proof + hash according to the EPIC011 evidence governance process.
