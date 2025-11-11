# HD Engine dev harness repo — CLI & Reader (alpha)

Glow HD Engine — README

## EPIC-009 — Ops Safety & DB Runtime Posture (post-merge)
- **Refusal (ops):** `/ops/rails/refusal` returns 503 with a typed JSON body, `Cache-Control: no-store`, **no ETag**, and no vendor I/O.
- **Keys-only logs:** refusal route logs exactly `{at, route, status, duration_ms, idempotence_hash, release_id}` (no bodies/headers/secrets).
- **Env-matrix snapshots:** selection-only evidence (success chooses `DATABASE_URL` or `DB_BRIDGE_URL`, failure is typed—no DB connectivity here).
- **DB posture:** scripts use connection-time fallback (try `DATABASE_URL`, fall back to **Postgres DSN** `DB_BRIDGE_URL`); evidence includes `search_path`, **grants** (present-even-empty ADP), normalized **DDL fingerprint**, and migration **two-run identity**.
- **QA quick run:** `scripts/qa/epic009_precommit.sh` → expect **QA_OK** and report at `artifacts/qa/epic009_precommit_report.json`.

## CLI — Vendor JSON file inputs
Examples:
- Pair file:
  ```bash
  hdctl showcompat --pair-file path/to/pair.json > out.json
  ```
- Two person files:
  ```bash
  hdctl showcompat --a-file A.json --b-file B.json > out.json
  ```
Output is the public Reader v1 body (bands-only), canonical JSON, numeric-free.

## EPIC-006 — Closure (Mechanics Foundations)

**What shipped**
- Deterministic mechanics layer: comparators & helpers (arrays-as-sets; channel `NN-NN` min-first; stable ordering).
- Frozen constants: `EM_MAX=36`, `THROAT_EM_MAX=13`, `CENTER_MAX=9`, `MIND_THROAT_MAX=3`, `MOTOR_THROAT_MAX=4`, `COMP_MAX=6`; direct Motor→Throat set `{20-34,21-45,35-36,12-22}`.
- Category framework (internal): frozen Magic-10 order **harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance**; unknown IDs hard-fail.
- Programmatic config: emits canonical registry report.
- Transport: `/internal/version` GET/HEAD 200, `Cache-Control: no-store`, **no ETag**, conditionals ignored; headers-only proofs captured.
- Evidence discipline: human **and** machine Evidence Indexes updated in the same change.

**How to validate**
```bash
LC_ALL=C TZ=UTC pytest -q -m epic006
```
Expected: all EPIC006 tests pass and artifacts are written.

**Artifacts (key paths)**
- Mechanics: `artifacts/mech/ordering_examples.jsonl`, `artifacts/mech/identity_hash.txt`, `artifacts/mech/constants_snapshot.json`
- Transport proofs: `artifacts/proofs/internal_version_headers.json`, `artifacts/proofs/internal_version_headers.txt`
- Registry: `artifacts/reports/registry_report.json`
      - Evidence Indexes: `docs/EVIDENCE_INDEX.md`, `audit/EVIDENCE_INDEX.jsonl`

## QA Evidence (tangible artifacts)
When running `hdctl showcompat` for QA, pass `--dump-reader` and `--dump-admin-dir`.
This writes:
- Public Reader JSON: `artifacts/qa/cli/<case>.reader.json`
- Admin proofs (0600 + .sha256):
  - `artifacts/admin/qa/<case>.left.bodygraph.json`
  - `artifacts/admin/qa/<case>.right.bodygraph.json`
  - `artifacts/admin/qa/<case>.composite.bodygraph.json`
  - `artifacts/admin/qa/<case>.compat.proof.json`
Public stdout remains numeric-free; admin numerics live only in sidecars.

Version: 2.0
Status: Active (Alpha A3–A5 body; A7 transport adopted)
Owner: Product Owner (PO) — Nathan
Gatekeeper: Isis (Head Dev — AI session)
Lead Dev: Full Stack Guru (AI session)  


---

Human/AI disclosure (Fire compliance)

Only human with agency: Product Owner (PO) — Nathan.

All other roles are AI sessions: “Isis,” “Full Stack Guru,” “Cyrano,” “HD Coder,” “QA,” etc. These are ChatGPT sessions operating under PO direction.

Authority & approvals: Only the PO’s signoffs are binding. AI “signoff” lines are advisory until recorded by the PO.



---

What this is

Glow HD Engine produces a minimal, numeric-free public envelope used by the SPA to display Bands for harmony, and (optionally) a short Aux Narrative. In Alpha:

Public JSON is bands-only, free of HD jargon.

Determinism is enforced via a canonical serializer, exactly one trailing LF, idempotence preimage hash, and AB↔BA parity.

Reader v1 is a developer harness that returns the same bytes as the CLI for the same inputs.

A7 transport is adopted (strong quoted ETag, conditional GET/304, HEAD parity, compression invariance). Transport rules live outside this README (see “Sources of truth”).



---

Sources of truth & repo docs

Canonical homes

Transport & caching (A7): Environment & Integration Plan v2.0.

Public body (contract): docs/contracts/reader_v1_public_bytes.md.

Reader surface (endpoints & gating): docs/server/reader_v1.md.

CLI behavior & numerics policy: Glow HD Engine — CLI, API & Vendor Ingest Spec v0.1.5 and docs/CLI_commands.md.

Governance & acceptance delivery: Glow Governance & Process Handbook — v1.1.

Engine Tasks: HD Engine Tasks v10 (A7-aligned).


Deprecated

Glow HD Engine Architecture & Design v4 (do not reference).



---

Validation overview (no commands)

To validate an Alpha build without prescribing code:

CLI (A3): Produce cli_stdout_AB.json and cli_stdout_BA.json. Evidence must show: canonical formatting (UTF-8, one LF, no BOM/ANSI), idempotence preimage hash correctness, AB↔BA byte identity, and a release_id that matches release/manifest.sorted.json.

Reader v1 (A5): For the same pair, produce reader_AB.json and reader_BA.json (dev-only harness). Evidence must show: bytes equal the CLI, content type is JSON, APP_ENV gating and path-safety enforced.

Transport (A7): Evidence lives in Environment & Integration Plan v2.0: strong quoted ETag equals sha256 over the final LF-terminated body (pre-compression), CSV If-None-Match strong-match behavior, 304 empty body, HEAD parity, compression invariance, and no ETag + no-store on writers/errors.


Marker names, artifact paths, and acceptance tables are defined in the documents above.


---

Reader v1 (developer harness)

Route: GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>.

APP_ENV gating: APP_ENV=dev enables limited filesystem reads only under fixtures/charts/; traversal/symlink denial; non-dev returns 403 with a minimal error body.

Transport: Governed by Environment & Integration Plan v2.0 (A7). This README does not restate header matrices.



---

Determinism & emitter canon

Serializer (MUST): UTF-8 JSON, sorted keys, compact separators, ensure_ascii=False, exactly one trailing \n, no BOM, ANSI-free.

Idempotence (MUST): idempotence_hash = sha256(canonical_preimage_bytes) where the preimage omits idempotence_hash and is LF-terminated.

Parity (MUST): public bytes are identical for AB and BA.

Single emitter (MUST): both CLI and Reader call the same public emitter; closeouts record a provenance fingerprint for the emitter.


### Security & Transport (Writers)

Writer endpoints are governed and deterministic:

- Responses: `Cache-Control: no-store`, **no ETag**, **no compression**, **never 304** (conditionals ignored).
- Method matrix: **HEAD → 405** (no body), **OPTIONS → 204** (no body), both with `Allow: POST, OPTIONS` and `Content-Length: 0`.
- Input validation:
  - require `Content-Type: application/json; charset=utf-8` (diagnostic empty-body exempt)
  - malformed JSON/UTF-8/BOM → 400; unknown key → 422; other schema violations → 422; body > 32 768 bytes → 413
- Auth: `Authorization: Bearer` with `admin:write` scope (401/403 split).

### Idempotent Writes

We canonicalize request bodies (UTF-8, sorted keys, compact JSON, one trailing LF) and compute a sha256 digest over the preimage `{method, writer_route_id, canonical_request_body}`.  
We persist the digest and canonical bytes in `hde.idempotent_writes` (created by `migrations/008_writers_auth.sql`). Duplicate requests return the same status as the first success.


---

Evidence & release identity

Release ID

release_id is the lowercase 64-hex SHA-256 of release/manifest.sorted.json and must match the value embedded in public outputs.


Minimal artifacts (by card)

A3 (CLI):
artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/release_id.txt
artifacts/cards/A3/validation.log
(optional when gated: artifacts/cards/A3/admin/sidecar.json)

A5 (Reader v1):
artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/validation.log

A7 (Transport): see Environment & Integration Plan v2.0 for exact header artifacts and PASS markers.

**Evidence indices:** human `docs/evidence/INDEX.json` and machine `artifacts/evidence_index.jsonl` (PF12 keys, sorted).



---

Environment variables (reference)

SAFE_MODE — 1 for tests/CI (recommended ON in dev/stage); 0 for prod. Vendor HTTP requires both SAFE_MODE=0 and ALLOW_NETWORK=1.

ALLOW_NETWORK — second rail to permit HTTP when SAFE_MODE=0.

PRODUCT_INVOCATION_TAG — current invocation tag (e.g., INV-…).

ENGINE_TAG — human-readable engine tag for meta.

APP_ENV — dev enables the Reader harness; otherwise requests are refused.



---

Project layout (key paths)

docs/CLI_commands.md

docs/server/reader_v1.md

docs/contracts/reader_v1_public_bytes.md

docs/architecture/emitters.md

docs/alpha_acceptance.md

CHANGELOG.md

fixtures/charts/ (dev inputs)

release/manifest.sorted.json

scripts/ (entrypoints and helpers)

artifacts/cards/ (evidence bundles per card)



---

Governance (acceptance delivery)

Work on main; one revert-friendly commit per card with evidence under artifacts/cards/<CARD>/.

PO performs closeout and signoff (template in docs/alpha_acceptance.md).

Transport and public body rules are not duplicated here; see sources of truth.



---

FAQ

Where are the transport rules?
In Environment & Integration Plan v2.0 (A7). This README intentionally defers to that document.

Where is the engine/public contract defined?
In docs/contracts/reader_v1_public_bytes.md (example + preimage), referenced by Spec v0.1.5 and the Reader doc.

Why numeric-free public JSON?
Alpha SPA shows Bands only. CLI may expose score_pct only when --score is explicitly requested (see Spec v0.1.5).


---

Changelog (README)

v2.0 (2025-10-02): Adopt A7 transport (deferred to Env & Integration Plan v2.0); add contract/source-of-truth links; remove command snippets; align evidence sections with Alpha/A7 acceptance.

v1.0 (2025-10-02): Initial comprehensive README for Alpha A3–A5; A5 transport guard documented. 



## Aux Narrative (EPIC-010 — text surface)
**Endpoint:** `GET /aux/narrative`  
**Text outcome:** `200` `text/plain; charset=utf-8`, LF-terminated body, quoted strong `ETag`, `Vary: Authorization, Accept-Encoding`, `Cache-Control: private, max-age=0, must-revalidate`.  
**Suppressed outcome:** `200` with **empty body** and **no `ETag`** (may include `X-Narrative-Policy`).  
**Pack identity:** sealed files are mounted at `/narratives/<pack_sha>/…`; `pack_sha` is sha256 over canonical `catalog/narratives/manifest.json`.

**Evidence (this repo):**
- `audit/gates/narratives/keys_10x4.table.json`
- `tests/transport/headers/aux_text_200.snap`, `tests/transport/headers/aux_suppression_200.snap`
- Human: `docs/evidence/INDEX.json` (+ `INDEX.sha256`); Machine: `artifacts/evidence_index.jsonl` (single JSONL file).

**Note:** Reader v1 remains numeric-free and **narrative-free**; Aux is the only narrative text surface in EPIC-010.


## Status
Reader v1 is stable. Local runs use the dev runner at dev/reader_harness/app.py (APP_ENV=dev). The canonical HTTP adapter lives at adapter/http_reader.py. The legacy server/ tree is deprecated and will be removed after consolidation.

## Getting started (dev harness)
Run the local Reader v1 (dev only):
```bash
export APP_ENV=dev
python dev/reader_harness/app.py
```
Probe:
```bash
curl -i http://127.0.0.1:5000/api/reader?a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>
```

## Getting started (dev harness)
Run the local Reader v1 (dev only):
```bash
export APP_ENV=dev
python dev/reader_harness/app.py
```
Probe:
```bash
curl -i http://127.0.0.1:5000/api/reader?a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>
```

### Sources of Truth (SoT)
• Public body & determinism — HD Engine — Math & Technical Spec  
• Transport & caching (A7) acceptance — Governance & Process (Acceptance)
(Repo docs link to these homes and do not restate their rules.)

<!-- EPIC-004 RUN -->
### Quick run (EPIC-004)
```bash
python -m adapter.http_reader
```
Bind: http://127.0.0.1:5000   ·   Env: PYTHONHASHSEED=0 PYTHONUTF8=1 TZ=UTC SAFE_MODE=1
