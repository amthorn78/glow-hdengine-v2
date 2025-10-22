Glow HD Engine — README

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
