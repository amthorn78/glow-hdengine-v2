# PF05 exact redlines from v2.5.2

Run identity: gtwpe-20261009-pf10-v13-5/T-PF05/from-v2.5.2

Originating preparer: Codex in Nathan’s original T-PF05 document session, /root; no external platform session ID is asserted.

Original: docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md at e7265a090ad0cc8de5f36de2f19481216aa3d073; v2.5.2; raw UTF-8 SHA-256 a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e.

Pinned role: TW-DRAIN-10 100926.1. This file is content redlines only; Apply reserves the native header fields.

Preparation outcome: READY after complete producer validation; save completeness is recorded by the verified companion proof log. Package revision: preparation r1.

Literal framing: each fenced payload has one framing LF immediately before its closing fence; that framing LF is not payload. Every preceding character and LF, including leading/trailing blank lines, is literal payload. No normalization or unescaping is permitted. Each location is the exact original heading hierarchy. Offsets/counts are independently checked against the unchanged original in the companion proof log.

## Redline RL-001

Operation: REPLACE

Original heading path:
># **0\. Document Control \[Required-Now\]**
>## **0.2 Scope \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
* **Supersession (PF10 addenda).** Consult the complete latest active PF10 base version, whether it is one unlettered document or a complete verified lettered set, and treat every document in a lettered set as an equally authoritative container of independently scoped addenda. Apply every applicable, active, non-superseded addendum to its own scope. A later document letter supersedes nothing by itself; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and lower-numbered guidance remains authoritative for distinct scope. PF10 governs PF05 only where such an addendum explicitly addresses a PF05-owned topic; when the complete active PF10 version is silent on that topic, PF05 governs. PF05 integrates applicable PF10 guidance and routes **by title only** to single homes (no version numbers). Build Notes reference posture: cite PF10 by **addendum number \+ addendum title**; do not use PF10 version strings, document letters, or PF10 section numbers as durable anchors.  

`````

Replacement text:
`````text
* **Supersession (PF10 addenda).** Consult the complete latest active PF10 base version, whether it is one unlettered document or a complete verified lettered set, and treat every document in a lettered set as an equally authoritative container of independently scoped addenda. Apply every applicable, active, non-superseded addendum to its own scope. A later document letter supersedes nothing by itself; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and lower-numbered guidance remains authoritative for distinct scope. PF10 governs PF05 only where such an addendum explicitly addresses a PF05-owned topic; when the complete active PF10 version is silent on that topic, PF05 governs. PF05 integrates applicable PF10 guidance and routes **by title only** to single homes (no version numbers). Reference **HDE Build Notes** by title only; do not cite its addendum numbers, sections, headings, paragraphs, versions, document letters, or other internal locators. Search the current source by topic to establish applicable scope.  

`````

## Redline RL-002

Operation: REPLACE

Original heading path:
># **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**
>  ## **Reader transport**

Expected occurrences: 1

Old text:
`````text
* **Dev harness — Implemented (dev-only).** `/reader?v=1` is the canonical dev Reader surface for schema/LF checks, AB↔BA and two-run identity, and Reader↔CLI reader-dump parity. `/api/reader?v=1` is an alias only when the Reader blueprint is actually mounted under `/api`. Rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); harness proofs are supplemental and do not replace Endpoint Catalog A7 proofs. See §5.4.  

`````

Replacement text:
`````text
* **Dev harness — Implemented (dev-only).** `GET /reader?v=1` is the canonical dev Reader surface for schema/LF checks, AB↔BA and two-run identity, and Reader v1 CLI reader-dump parity. It remains at the root mount. The separate production `POST /api/reader` serves `v=1` and `v=2`; it is not a GET alias. Rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); harness proofs are supplemental and do not replace Endpoint Catalog A7 proofs. See §5.4.  

`````

## Redline RL-003

Operation: REPLACE

Original heading path:
># **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**
>  ## **Reader transport**

Expected occurrences: 1

Old text:
`````text
* **Production Reader surface — Required-Now.** `POST /api/reader?v=1` is the adopted production application route. It accepts only the closed two-UUID request in §5.1, resolves BodyGraphs read-only, and projects either the one-band eligible Reader v1 success or the empty ineligible self-pair success. The existing file-path GET Reader remains development-only and non-authoritative.  

`````

Replacement text:
`````text
* **Production Reader surface — Required-Now; implemented in the repository.** `POST /api/reader` selects Reader v1 with exactly one `v=1`, or Reader v2 with exactly one `v=2`. Both accept the closed two-UUID request in §5.1 and resolve complete BodyGraphs read-only. An eligible v1 pair projects only `harmony`; an eligible v2 pair projects all ten categories in governed order. An ineligible self-pair projects `[]` in either version. The file-path GET Reader remains development-only. Repository implementation does not establish deployment or live current-row success; see §5.1.7.  

`````

## Redline RL-004

Operation: REPLACE

Original heading path:
># **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**
>  ## **Vendor ingest (HDAPI)**

Expected occurrences: 1

Old text:
`````text
* **Live HTTP gated by SAFE rails — Required-Now.** Vendor calls are permitted only when rails are explicitly open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); default posture for dev/CI is closed. Closed-rails refusal behavior, admin override, and rails evidence live in §7.1. HumanDesignAPI v2 open-rails smoke, when required, remains PO-only and evidence-backed.  

`````

Replacement text:
`````text
* **Live HTTP gated by SAFE rails — Required-Now.** Vendor calls are permitted only when rails are explicitly open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); default posture for dev/CI is closed. Closed-rails refusal behavior, the unimplemented production override requirement, and rails evidence live in §7.1. A Product Owner-directed agent may execute a bounded vendor smoke with the same controls and required evidence as a human executor; the direction is task-specific and creates no standing vendor authority.  

`````

## Redline RL-005

Operation: REPLACE

Original heading path:
># **3\) CLI Overview & Conventions \[Required-Now\]**
>## **3.7 Interim “no-user” QA mode (pre-Glow prod)**

Expected occurrences: 1

Old text:
`````text
* A controlled vendor-backed no-user smoke, when used as PF05 `showcompat` implementation-validation evidence, MUST be PO-only and IA-guided. Automated agents MUST NOT run the vendor call, and no command may be modified by guesswork to force a PASS.  

`````

Replacement text:
`````text
* A controlled vendor-backed no-user smoke, when used as PF05 `showcompat` implementation-validation evidence, MUST be Product Owner-authorized and IA-guided. A directed automated session agent executes the identified task on the Product Owner’s direction and produces its evidence. “PO-only” names the authorizing and accountable principal, not a required physical executor. The agent follows the same exact commands, scope, request limit, rails, stop checks, synthetic inputs, secret scan/quarantine, redaction and evidence contract as a human executor. No command may be modified by guesswork to force a PASS, and no completion may be claimed without the required evidence.

`````

## Redline RL-006

Operation: REPLACE

Original heading path:
># **3\) CLI Overview & Conventions \[Required-Now\]**
>## **3.7 Interim “no-user” QA mode (pre-Glow prod)**

Expected occurrences: 1

Old text:
`````text
* For this CLI vendor smoke, the target is the HD Engine CLI running in the PO-controlled execution context. Required target facts are `hdctl showcompat`, `--source vendor`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when required by the command path, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and `APP_ENV=dev`.  

`````

Replacement text:
`````text
* For this CLI vendor smoke, the target is the HD Engine CLI running in the PO-controlled execution context. Required target facts are `hdctl showcompat`, `--source vendor`, the two credential names `HD_API_KEY` and `GEO_API_KEY`, the canonical base-URL name `HD_API_BASE_URL` (or deprecated `HDAPI_BASE_URL` only when the canonical value is absent), `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and `APP_ENV=dev`. The base URL is configuration, not an API key. Resolve conflicting normalized base-URL values by failing closed; never silently choose one. Use the configuration held in the execution environment, record only `SET` or `UNSET`, keep values off argument lists and out of conversation, logs and artifacts, and scan captured output before using it as evidence. A rails posture MUST NOT remove the only configured base URL. Missing required configuration prevents the call; record missing names by presence only and classify a begun step as `TOOLING_BLOCKED`. Do not substitute manual entry of vendor values.

`````

## Redline RL-007

Operation: REPLACE

Original heading path:
># 4\. Commands (by status)
>## 4.1 hdctl showcompat \[Partially Implemented; Required‑Now\]
>### 4.1.6 Implementation status (audit v1)

Expected occurrences: 1

Old text:
`````text
### 4.1.6 Implementation status (audit v1)

* **Implementation status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c`:** Registered but partially implemented.  
* **Statically confirmed:** the packaged `hdctl` entrypoint and `showcompat` parser exist; compat stdout, Reader dump, and admin-dump paths are wired; compat stdout and Reader dump use the canonical presenter.  
* **Required gaps:** category scores are derived from a stable pair/category hash rather than full BodyGraph mechanics; file/stdin mode does not retain full BodyGraph topology; stdout `a`/`b` are not resolved BodyGraphs; the adopted explicit stdin/user flag spellings, file canonical-byte/schema gates, and stdin schema/shape validation are absent; `auto` can select vendor from birth inputs; conjunction passes viewer preferences despite the ignore rule; admin sidecars bypass the presenter; and help describes Reader bytes rather than compat stdout.  
* **Evidence posture:** checked-in tests and artifacts record intended canonical/parity behavior, but their presence is not a runtime PASS or acceptance-token attestation.


`````

Replacement text:
`````text
### 4.1.6 Implementation status (bounded repository inspection)

* **Repository snapshot:** `main@e7265a090ad0cc8de5f36de2f19481216aa3d073`, inspected read-only on 2026-10-09. The packaged `hdctl` parser and `showcompat` entrypoint exist. Eligible stdout is the complete canonical `magic10_compat_result.v1`; the optional `--dump-reader` path remains Reader v1 only. Both delegate byte emission to the shared presenter.
* **Delivered integration:** complete-chart resolution feeds the admitted Gate-based mechanics path, eligibility precedes evaluation, `auto` is DB-only, file/stdin resolution is local, and admin dumps use the presenter. The earlier stable-hash scorer, missing-topology behavior and automatic birth-based vendor fallback are not the current `showcompat` path. HDE Build Notes records accepted PR04 integration and the later complete-release and Reader deliveries; historical non-admitted interim states remain historical.
* **Remaining CLI limitations:** the adopted explicit stdin/user flag spellings and file canonical-byte/schema gates are not established by this inspection; the parser still describes Reader v1 bytes rather than compat stdout. `--dump-reader` does not emit Reader v2. The separate stateless run-bundle capability in §4.1.7 remains a gap. The legacy `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure is recorded in HDE Build Notes and is not corrected or rerun here.
* **Proof boundary:** this is bounded static inspection. Historical exact-head CI, accepted implementation and QA evidence retain their original attribution; none is a new runtime PASS, deployment, production availability or acceptance-token attestation for this documentation revision.


`````

## Redline RL-008

Operation: FIND_AND_REPLACE

Original heading path:
>WHOLE PF

Expected occurrences: 2

Scope: whole PF

FIND literal:
`````text
Build Notes (Addendum 11)
`````

REPLACE literal:
`````text
**HDE Build Notes**
`````

## Redline RL-009

Operation: DELETE

Original heading path:
># 4\. Commands (by status)
>## 4.2 hdctl read singlebg \[Speculative\]

Expected occurrences: 1

Old text:
`````text
*(Unchanged in spirit; shown here only for completeness with minor wording aligned to Option B. No new semantics were invented.)*


`````

## Redline RL-010

Operation: REPLACE

Original heading path:
># 4\. Commands (by status)
>## 4.2 hdctl read singlebg \[Speculative\]

Expected occurrences: 1

Old text:
`````text
**Purpose (normative, draft).**
`````

Replacement text:
`````text
**Purpose (normative).**
`````

## Redline RL-011

Operation: REPLACE

Original heading path:
># 4\. Commands (by status)
>## 4.3 hdctl list people \[Speculative\]

Expected occurrences: 1

Old text:
`````text
## 4.3 hdctl list people \[Speculative\]

Needs development.

---


`````

Replacement text:
`````text
## 4.3 hdctl list people \[Speculative\]

Implementation gap. No invocable contract is adopted; the command remains Speculative.

---


`````

## Redline RL-012

Operation: REPLACE

Original heading path:
># 4\. Commands (by status)
>## 4.4 Fetch commands (person/batch) \[Speculative\]

Expected occurrences: 1

Old text:
`````text
## 4.4 Fetch commands (person/batch) \[Speculative\]

Needs development.

---


`````

Replacement text:
`````text
## 4.4 Fetch commands (person/batch) \[Speculative\]

Implementation gap. No invocable contract is adopted; the command remains Speculative.

---


`````

## Redline RL-013

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]

Expected occurrences: 1

Old text:
`````text
The Reader v1 success body contains exactly these six top‑level keys — no extras:

`````

Replacement text:
`````text
The Reader success body contains exactly these six top-level keys — no extras. Reader v1 and Reader v2 use the same closed envelope with their version-specific projection:

`````

## Redline RL-014

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]

Expected occurrences: 1

Old text:
`````text
* `reader_version` — fixed string `"v1"`.  

`````

Replacement text:
`````text
* `reader_version` — fixed string `"v1"` for Reader v1 or `"v2"` for Reader v2.  

`````

## Redline RL-015

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]
>### **5.1.0 Production POST request and resolution (normative)**

Expected occurrences: 1

Old text:
`````text
### **5.1.0 Production POST request and resolution (normative)**

`POST /api/reader?v=1` accepts one JSON object with exactly `a_id` and `b_id`. Each value must be an exact lowercase canonical hyphenated RFC 4122 UUID. Unknown keys and inline charts, Gates, weights, profiles, bands, configuration IDs, and viewer preferences are prohibited.

The application resolves each UUID read-only through `public.hde_body_graphs_current` with `user_id` equal to the canonical UUID and `vendor = 'hdapi'`, selecting the current `user_id`, `vendor`, `vendor_version`, `input_fingerprint`, and `payload`. Reader resolution performs no write, request-time vendor call, arbitrary-string UUID5 conversion, or silent fallback. A resolved Gate array must be present, nonempty, unique, canonical, and within `1..64` before Engine Core is called.

Eligibility is decided after both complete projections resolve and before Engine Core, narrative routing, or intrinsic cache access. The same canonical UUID with byte-identical normalized projections is a valid ineligible self-pair. The same canonical UUID with unequal complete normalized projections fails closed. For distinct parties, directional narrative order is `(gate_mask, canonical_person_id)`; ASCII canonical UUID order is used only to break an equal Gate-mask tie. Request order never controls narrative orientation.


`````

Replacement text:
`````text
### **5.1.0 Production POST request and resolution (normative)**

The production route is `POST /api/reader`. The query MUST carry exactly one `v` whose decoded value is exactly `1` (Reader v1) or `2` (Reader v2). No defaulting, trimming, numeric parsing or version inference is allowed. Missing, empty, repeated (even identical), malformed or unsupported values return status `400` with `ERR_READER_INVALID_VERSION` before body reading or lookup.

Both versions accept one JSON object with exactly `a_id` and `b_id`. Each value must be an exact lowercase canonical hyphenated RFC 4122 UUID. The body is nonempty UTF-8 JSON without a BOM and at most `32,768` bytes, including when `Content-Length` is absent. Invalid JSON, wrong shape, extra or missing keys, invalid UUID spelling and an oversize body return `422 ERR_READER_INVALID_INPUT`. Inline charts, Gates, weights, profiles, bands, configuration IDs and viewer preferences are prohibited.

The application resolves each distinct UUID by one read-only lookup through `public.hde_body_graphs_current` with `user_id` equal to the canonical UUID and `vendor = 'hdapi'`, selecting the current `user_id`, `vendor`, `vendor_version`, `input_fingerprint`, and `payload`. Reader resolution performs no write, request-time vendor call, arbitrary-string UUID5 conversion, or silent fallback. A missing row returns `404 ERR_M10_PERSON_UNRESOLVED`; unavailable or ambiguous resolution or an invalid current-view row contract returns `503 ERR_M10_RESOLVER_UNAVAILABLE`. A resolved Gate array must be present, nonempty, unique, canonical, and within `1..64` before Engine Core is called; incomplete stored Gate data returns `503 ERR_M10_BODYGRAPH_INCOMPLETE`.

Eligibility is decided after both complete projections resolve and before Engine Core, narrative routing, or intrinsic cache access. The same canonical UUID with byte-identical normalized projections is a valid ineligible self-pair. The same canonical UUID with unequal complete normalized projections fails closed. For distinct parties, directional narrative order is `(gate_mask, canonical_person_id)`; ASCII canonical UUID order is used only to break an equal Gate-mask tie. Request order never controls narrative orientation.

Every method other than `POST` at `/api/reader`, including `HEAD`, `OPTIONS` and extension methods, returns the governed `405 ERR_NOT_FOUND` response with `Allow: POST`, `Cache-Control: no-store`, no `ETag` and no `Content-Encoding`; HTTP HEAD suppresses the body. Production POST ignores `If-*` conditionals and never returns `304`. Success is `200` with `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate` and `Vary: Authorization, Accept-Encoding`, with no `ETag`. Errors follow §5.2. Unknown descendant paths are distinct from this exact-route method contract; the factory-specific HTML 404 limitation is retained in §5.1.7.


`````

## Redline RL-016

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]
>### 5.1.1 CLI and admin compatibility surfaces (normative)

Expected occurrences: 1

Old text:
`````text
* The Reader v1 success envelope above is the **only** public compat payload exposed by the Reader API. It remains six‑key and numeric‑free.  

`````

Replacement text:
`````text
* The versioned Reader success envelopes above are the public compat payloads exposed by the Reader API: v1 is single-harmony; v2 is the ordered full Magic-10 projection. Both remain six-key, bands-only and numeric-free.  

`````

## Redline RL-017

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]
>### 5.1.1 CLI and admin compatibility surfaces (normative)

Expected occurrences: 1

Old text:
`````text
* The compat engine produces the pure `magic10_result.v1` and the symmetric complete `magic10_compat_result.v1` defined in §4.1.3. Neither is the Reader v1 envelope.

`````

Replacement text:
`````text
* The compat engine produces the pure `magic10_result.v1` and the symmetric complete `magic10_compat_result.v1` defined in §4.1.3. Neither is a public Reader envelope.  

`````

## Redline RL-018

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]
>### 5.1.3 Emission algorithm (success case; titles‑only)

Expected occurrences: 1

Old text:
`````text
The Reader v1 success emission algorithm is:

`````

Replacement text:
`````text
The Reader v1 and Reader v2 success emission algorithm is the same; `reader_version` and category projection are selected before constructing the preimage:

`````

## Redline RL-019

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## 5.1 Success envelope \[Required‑Now\]
>### 5.1.4 Public covenant and determinism

Expected occurrences: 1

Old text:
`````text
### 5.1.4 Public covenant and determinism

**Public covenant.**

* The Reader v1 success body is **numeric‑free**.  
    
* Fields such as `score`, `prompt`, `uncertainty`, or any narrative keys/diagnostics **MUST NOT** appear in the Reader v1 envelope.  
    
* Numeric scores and narrative keys exist only in compat/admin JSON (e.g., `showcompat` stdout compat JSON and Aux preview inputs), never in the public Reader response.

**Determinism and parity.**

* **AB vs BA.** Normalization at the compat layer guarantees identical preimages and identical final Reader v1 envelope bytes for `{a,b}` and `{b,a}`.  
    
* **Two‑run identity.** Two serializations with the same inputs produce byte‑identical Reader envelope bytes.  
    
* **Reader vs CLI.**  
    
  * When the CLI produces Reader v1 bytes via `--dump-reader`, those bytes **MUST** be identical to the Reader 200 success body for the same inputs and environment.  
      
  * CLI compat JSON (admin/test) is canonical and deterministic, but it is a **distinct envelope** from the Reader v1 public envelope.

**Routing (titles‑only).**

* Canonical JSON & pack/manifest rules: **HDE‑Schemas & Artifacts**.  
    
* Magic‑10 IDs, scoring, and band selection: **HDE‑Math‑Spec** and **HDE‑Mechanics Guide**.  
    
* Transport status & headers (A7 matrices): **HDE‑Governance** §10 and this document’s §5.3.  
    
* Preimage/idempotence details: **HDE‑Math‑Spec** §3.  
    
* CLI compat JSON schema and admin/test evidence surfaces: this document (later CLI/compat sections) and **HDE‑Mechanics Guide** (titles‑only).


`````

Replacement text:
`````text
### 5.1.4 Public covenant and determinism

**Public covenant.**

* Reader v1 and Reader v2 success bodies are **numeric‑free**.  
    
* Fields such as `score`, `prompt`, `uncertainty`, or any narrative keys/diagnostics **MUST NOT** appear in either public Reader envelope.  
    
* Numeric scores and narrative keys exist only in compat/admin JSON (e.g., `showcompat` stdout compat JSON and Aux preview inputs), never in the public Reader response.

**Determinism and parity.**

* **AB vs BA.** Normalization at the compat layer guarantees identical preimages and identical final version-selected Reader envelope bytes for `{a,b}` and `{b,a}`.  
    
* **Two‑run identity.** Two serializations with the same inputs produce byte‑identical Reader envelope bytes.  
    
* **Reader vs CLI (v1 only).**  
    
  * When the CLI produces Reader v1 bytes via `--dump-reader`, those bytes **MUST** be identical to the Reader v1 200 success body for the same inputs and environment.  
      
  * No CLI flag emits Reader v2; v2 has its own ordered goldens and AB↔BA/two-run checks.
      
  * CLI compat JSON (admin/test) is canonical and deterministic, but it is a **distinct envelope** from the Reader v1 public envelope.

**Routing (titles‑only).**

* Canonical JSON & pack/manifest rules: **HDE‑Schemas & Artifacts**.  
    
* Magic‑10 IDs, scoring, and band selection: **HDE‑Math‑Spec** and **HDE‑Mechanics Guide**.  
    
* Transport status & headers (A7 matrices): **HDE‑Governance** §10 and this document’s §5.3.  
    
* Preimage/idempotence details: **HDE‑Math‑Spec** §3.  
    
* CLI compat JSON schema and admin/test evidence surfaces: this document (later CLI/compat sections) and **HDE‑Mechanics Guide** (titles‑only).


`````

## Redline RL-020

Operation: INSERT

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

BEFORE anchor:
`````text
This QA step validates a single well-formed envelope instance in the CLI QA environment; it does not, by itself, satisfy the broader parity and determinism acceptance tokens.

---


`````

AFTER anchor:
`````text
## **5.2 Errors \[Required-Now\]**

`````

Inserted text:
`````text
### 5.1.6 Reader v2 ordered projection and examples (normative)

Reader v2 is selected by `POST /api/reader?v=2`. It inherits §5.1.0 request, read-only resolution, eligibility, error and transport behavior. `reader_version` is exactly `"v2"`. Its success schema is `schemas/reader.v2.schema.json` and its owned goldens are under `goldens/reader/v2/`.

For an eligible pair, `categories` MUST contain exactly ten items, each exactly `{ "id", "band" }`, in this governed order from `catalog/magic10.json`:

1. `harmony`
2. `heat`
3. `communication`
4. `alignment`
5. `comfort`
6. `consistency`
7. `expansion`
8. `creativity`
9. `drive`
10. `balance`

Each band is that category’s band in the complete canonical intrinsic Magic-10 result and is exactly `Cool`, `Open`, `Warm` or `Glow`. This is an ordered array, not a set-sorted array. No category may be omitted, duplicated, default-filled, substituted by harmony, or altered by viewer preferences. For an ineligible pair, `categories` MUST be `[]`; Engine Core, intrinsic cache and narrative routing are not called.

The five-key preimage contains `reader_version:"v2"`, `eligible`, the ordered `categories`, the closed `meta` object and `release_id`. Hash the canonical LF-terminated preimage, add `idempotence_hash`, and re-emit through the same shared byte-authoritative emitter. AB↔BA and two-run byte identity apply. No public numeric, score, prompt, narrative key, UUID, Gate data, configuration or internal diagnostic is added.

Reader v1 remains unchanged: exactly one harmony item when eligible, otherwise `[]`, `reader_version:"v1"`, the same six-key closure and its existing byte covenant. `schemas/reader.v1.schema.json` now represents that covenant: harmony only, no prompt, closed success topology. Its error branch is the four-key envelope in §5.2, corrected by PR06b. Retired `*_leader` identities are not Reader contracts. `scripts/hd_cli.py` is a retained legacy stub, not a Reader surface.

These complete synthetic examples are the named repository goldens displayed without their final LF. Wire bytes include exactly one final LF. The 64-character `a` release value and `Isis5` / `INV-000000` metadata are fixture identities, not the current production release or observed live responses. The quoted digits in tags and hashes are strings; the bodies contain no JSON number.

Eligible pair — `goldens/reader/v2/g03_eligible_ten_in_order.json`:

```json
{"categories":[{"band":"Cool","id":"harmony"},{"band":"Open","id":"heat"},{"band":"Warm","id":"communication"},{"band":"Glow","id":"alignment"},{"band":"Cool","id":"comfort"},{"band":"Open","id":"consistency"},{"band":"Warm","id":"expansion"},{"band":"Glow","id":"creativity"},{"band":"Cool","id":"drive"},{"band":"Open","id":"balance"}],"eligible":true,"idempotence_hash":"9e51c57b9e613d9c0f52486979c3c247c265c568a690240ff4e5a11ac445dea4","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Ineligible pair — `goldens/reader/v2/g01_ineligible.json`:

```json
{"categories":[],"eligible":false,"idempotence_hash":"a2cca383ec8f8542d1d4cd04841d5ee389d38fa0ad38b41b4ca7f49b3ff1e23b","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Governed Reader error — `goldens/reader/v1/g06_error_invalid_input.json` (same error envelope for Reader v1 and v2):

```json
{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}
```

The error’s `schema:"v1"` identifies `error_v1`, not the selected Reader success version. No CLI flag emits Reader v2; `hdctl showcompat --dump-reader` and Reader↔CLI dump parity remain v1 only.

### 5.1.7 Delivered scope and proof limits (informative)

At `main@e7265a090ad0cc8de5f36de2f19481216aa3d073`, bounded read-only inspection finds the production Reader blueprint mounted under `/api` in `adapter/factory.py`, `adapter/http_reader.py` and `adapter/wsgi.py`. The dev GET blueprint stays at the root. Reader v1 and v2 share the production handler, read-only current-row resolver and byte-authoritative emitter. The production route’s POST Catalog row is present; query versions select contracts within that one route/method record.

HDE Build Notes records PR06a delivery of PR04’s F03 production-route, F05 v1 success-schema and F07 dev-conjunction capture deferrals. PR06b subsequently delivered C040-08 v1 error-schema conformance. These earlier deferrals are resolved in that delivered lineage, not open route/schema obligations. The admitted roster is 45 members at release version `1.3.0`; `schemas/reader.v2.schema.json` is a member. Release admission and deployment remain distinct.

The recorded HDE-EPIC040 QA verdict is PASS for its tested source and stated proof classes, not a new run here. Reader v1/v2 success used injected rows in-process; loopback HTTP covered refusals. Live Gate readiness and live DB Reader success over live HTTP remained blocked by environment and deferred to a future epic with the App user model. The bounded live-vendor check proved CLI-local acquisition, canonical compat stdout and a Reader v1 dump, not Reader v2 over HTTP, mapped-cache persistence, broad provider conformance or a deployed service.

Known limits remain: unknown non-compat paths, including Reader descendant paths, receive framework HTML 404 from `adapter/factory.py` and `adapter/http_reader.py`; `adapter/wsgi.py` supplies JSON `ERR_NOT_FOUND`. This does not weaken the normative error contract, and the transport owner retains the gap. Other recorded limitations, including the legacy CLI proof failure, wheel-install admission limitation, stale showcompat help and carried implementation/evidence findings, retain their owners; their historical outcomes are not rerun here. This documentation revision runs no product QA, deploys nothing and proves no live availability.

The closure record for HDE-EPIC040 is `CLOSE / CHANGE_CLOSED` by Product Owner-authorized exceptional closure. It resolves the earlier evidence-landing and QA50-F01 indexing gaps. It establishes neither ordinary Close Gate completion nor a close pack, PF09 movement, phase exit, deployment or release activation. It supports later documentation drainage without turning this revision into a closure or acceptance decision.


`````

## Redline RL-021

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
2. Optional fields are defined in the schema owned by **HDE-Schemas & Artifacts** (titles-only). Today this includes:  

`````

Replacement text:
`````text
2. Outside the closed Reader contracts, optional fields are defined in the schema owned by **HDE-Schemas & Artifacts** (titles-only). Reader v1 and Reader v2 errors have exactly the four required keys in §5.2.3, with no `retry_after_ms` or `details`. Other governed surfaces may include only their own schema-permitted fields:  

`````

## Redline RL-022

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
   1. For Reader v1, the standard error envelope has exactly `schema`, `ok`, `code`, and `error`; `schema` is `v1`, `ok` is `false`, and `code` and `error` are the governed pair below. Public Reader invokes `engine.compat.errors.error_envelope()` without `details`. No stack, path, UUID, Gate list, configuration contents, database detail, or internal diagnostic detail appears.

`````

Replacement text:
`````text
   1. For Reader v1 and Reader v2, the standard error envelope has exactly `schema`, `ok`, `code`, and `error`; `schema` is `"v1"` (the `error_v1` version), `ok` is `false`, and `code` and `error` are a governed pair. The Reader invokes `engine.compat.errors.error_envelope()` without `details`. No retry field, stack, path, UUID, Gate list, configuration contents, database detail, or internal diagnostic appears.

`````

## Redline RL-023

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
| `ERR_READER_INVALID_CHART` | `invalid Reader chart` |
`````

Replacement text:
`````text
| `ERR_READER_INVALID_CHART` | `invalid reader payload` |
`````

## Redline RL-024

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
   3. The error branch of `schemas/reader.v1.schema.json` MUST enforce this exact closed topology and the governed token/message pairs. Every new token MUST be registered in `engine/compat/error_tokens.py` and regenerated into `errors/token_map/token_map.json` through `tools/errors/generate_error_artifacts.py`. `adapter/schemas/error_v1.schema.json` remains unchanged unless its parity check proves a mismatch.

`````

Replacement text:
`````text
   3. `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json` enforce closed Reader error objects and the exact governed token/message pairs. The v1 error branch corrected by PR06b requires `schema:"v1"`, `ok:false`, `code` and `error` and rejects an absent or wrong schema, an ungoverned pair, and every extra key. Reader v1 additionally admits its existing dev-fixture refusal tokens. The two internal/CLI Gate-data tokens in the table above are not public Reader error branches; stored Gate defects project as `ERR_M10_BODYGRAPH_INCOMPLETE`. Every new token MUST be registered in `engine/compat/error_tokens.py` and regenerated into `errors/token_map/token_map.json` through `tools/errors/generate_error_artifacts.py`. `adapter/schemas/error_v1.schema.json` remains the separate generic envelope schema.

`````

## Redline RL-025

Operation: INSERT

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.2 Errors \[Required-Now\]**

Expected occurrences: 1

BEFORE anchor:
`````text
4. **Canonical error token map (`ERR_*`) and aliases.**  
     

`````

AFTER anchor:
`````text
   1. Canonical error tokens are defined in a governed **error token map** (for example `ERROR_TOKEN_MAP` in the engine) and are emitted as **UPPER\_SNAKE** strings in the `code` field, such as:  

`````

Inserted text:
`````text
   Reader version refusal is `400 ERR_READER_INVALID_VERSION` with message `unsupported reader version`. Every non-POST method at `/api/reader` is `405 ERR_NOT_FOUND` with message `not found` and `Allow: POST`. Dev GET `/reader` retains `ERR_READER_FORBIDDEN` (`reader endpoint disabled`), `ERR_READER_MISSING_PARAM` (`missing required reader parameters`), `ERR_READER_INVALID_PATH` (`invalid chart path`), `ERR_READER_MISSING_TZ_A` (`missing tz for party A`) and `ERR_READER_MISSING_TZ_B` (`missing tz for party B`). These pairs are schema-admitted; the dev tokens do not create v2 GET support.
     

`````

## Redline RL-026

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.4 Dev harness routing and guard (dev-only) \[Implemented\]**
>### **Route and gate (must)**

Expected occurrences: 1

Old text:
`````text
* **Version selection.** Reader v1 is selected via query parameter `v=1` on the Reader route, without changing the route path.  

`````

Replacement text:
`````text
* **Version selection.** Dev `GET /reader` requires exactly one query `v=1`. It does not serve Reader v2; missing, empty, repeated or other values return `400 ERR_READER_INVALID_VERSION`.  

`````

## Redline RL-027

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.4 Dev harness routing and guard (dev-only) \[Implemented\]**
>### **Route and gate (must)**

Expected occurrences: 1

Old text:
`````text
* **API-mount alias posture.** When the Reader blueprint is mounted under an `/api` prefix in a runtime configuration, `/api/reader` (and `/api/reader?v=1`) is an alias of the same Reader surface as `/reader` (and `/reader?v=1`). It is not a distinct contract or a separate proof surface.  

`````

Replacement text:
`````text
* **Production mount.** The separate production Reader blueprint is mounted under `/api` and serves `POST /api/reader?v=1` and `POST /api/reader?v=2`. It is not an alias of the dev GET surface. `/api/reader` rejects every non-POST method with the governed `405`, and unprefixed `POST /reader` is a `405` stub. Do not move the dev/internal blueprint or conflate its GET/HEAD A7 proofs with production POST.  

`````

## Redline RL-028

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.4 Dev harness routing and guard (dev-only) \[Implemented\]**
>### **Evidence (records-only; titles-only; indexed via PF12)**

Expected occurrences: 1

Old text:
`````text
* `parity/harness_vs_cli` — harness `GET` or `POST` vs CLI stdout byte-compare (**expected empty diff**).  

`````

Replacement text:
`````text
* `parity/harness_vs_cli` — dev harness GET vs CLI Reader v1 reader-dump byte-compare (**expected empty diff**); ordinary compat stdout is not a Reader-envelope parity input.  

`````

## Redline RL-029

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>## **5.6 Endpoint Catalog (JSON success) \[Required−Now\]**

Expected occurrences: 1

Old text:
`````text
| `/api/reader` | `POST` | production application Reader v1; closed two-UUID request; read-only current-`hdapi` BodyGraph resolution | not eligible |
`````

Replacement text:
`````text
| `/api/reader` | `POST` | production application Reader v1 (`v=1`) and Reader v2 (`v=2`); closed two-UUID request; read-only current-`hdapi` BodyGraph resolution; no GET alias or POST validator | not eligible |
`````

## Redline RL-030

Operation: REPLACE

Original heading path:
># 5\. Reader Transport (public bytes) \[Required‑Now\]
>  ## **5.12 Dev conjunction endpoints \[Implemented (dev-only)\]**

Expected occurrences: 1

Old text:
`````text
  ## **5.12 Dev conjunction endpoints \[Implemented (dev-only)\]**

* **Purpose.** Provide dev-only HTTP routes for conjunction preview and harness evaluation without coupling to the internal sampler harness.  
    
* **Environment gating (normative).**  
    
  * These routes MUST be gated by `APP_ENV` in `{dev, test, local}` and MUST NOT be available in production.  
  * If env-gating fails, requests to these routes MUST be forbidden using the Writer-style error envelope in §5.2 with `code: "ERR_WRITER_FORBIDDEN"` (not a raw HTTP 403 payload).  
  * These routes are not eligible for A7 proof selection; they MUST be registered with `a7_eligible=false` in the Endpoint Catalog.


* **Input contract (normative).**  
    
  * Inputs are supplied as query-string keys in the `a_*` and `b_*` namespace.  
  * At minimum, `a_id` and `b_id` MUST be accepted as pair identifiers.  
  * Request validation MUST fail closed for missing or malformed required identifiers, and MUST use canonical typed error mapping (no ad-hoc string errors).


* Resolver acquisition and SAFE rails posture (normative).  
    
  * Provider acquisition MUST be performed through resolver acquisition (not raw cache reads), so cache hits are normalized into a resolved shape and resolved detection remains correct even when a cached record is vendor-shaped.  
  * SAFE rails posture is closed by default. When an explicit environment configuration enables open-rails acquisition, acquisition MAY open rails only long enough to acquire missing data and MUST close back before compute and emission.  
  * Any governed writer-evidence run that exercises `GET /dev/writer/conjunction` MUST require explicit caller-provided open rails and MUST NOT silently force `SAFE_MODE=0` or `ALLOW_NETWORK=1` on behalf of the caller.  
  * Such writer-evidence runs do not widen the route contract and do not move this endpoint into the A7 proof family.


* Output canon (normative).  
    
  * Any success payload emitted by these routes MUST be serialized by the canonical public emitter, producing deterministic JSON bytes with ASCII-sorted keys and exactly one trailing LF.  
  * AB↔BA parity MUST hold for conjunction evaluation: swapping A and B MUST NOT change emitted bytes after canonical emission.  
  * `GET /dev/writer/conjunction` MUST emit typed, numeric-free writer-style success and error envelopes.  
  * The success envelope type MUST be `dev.writer.conjunction.success.v1`.  
  * The error envelope type MUST be `dev.writer.conjunction.error.v1`.  
  * Writer-style success and error outcomes on `GET /dev/writer/conjunction` MUST remain `Cache-Control: no-store`, MUST NOT emit `ETag`, and MUST be treated as non-conditional.


* Endpoints (dev-only).  
    
  * GET /dev/sampler/conjunction  
    * Dev-only conjunction preview route for sampler evaluation.  
  * GET /dev/reader/conjunction  
    * Dev-only conjunction preview route for Reader-style response emission and VendorError mapping.  
  * GET /dev/writer/conjunction  
    * Dev-only conjunction preview route returning an idempotent writer-style envelope (not the public Reader v1 envelope).  
    * The Endpoint Catalog route id for this endpoint is `dev.writer.conjunction.v1`.  
    * The `/dev/*/conjunction` family notation is bounded to the currently canonized conjunction-family surfaces listed in this subsection.  
    * It does **not** create a reusable wildcard or standing rule that any future dev route matched by a `/dev/*/` pattern is automatically valid, dev-harness, or outside the formal proof family.  
    * Any future non-conjunction dev route requires explicit canon classification before it is treated as valid, dev-harness, or outside the formal proof family.


  ---


`````

Replacement text:
`````text
  ## **5.12 Dev conjunction endpoints \[Implemented (dev-only)\]**

* **Purpose.** Provide dev-only HTTP routes for conjunction preview and harness evaluation without coupling to the internal sampler harness.  
    
* **Environment gating (normative).**  
    
  * These routes MUST be gated by `APP_ENV` in `{dev, test, local}` and MUST NOT be available in production.  
  * If env-gating fails, requests to these routes MUST be forbidden using the Writer-style error envelope in §5.2 with `code: "ERR_WRITER_FORBIDDEN"` (not a raw HTTP 403 payload).  
  * These routes are not eligible for A7 proof selection; they MUST be registered with `a7_eligible=false` in the Endpoint Catalog.


* **Input contract (normative).**  
    
  * Inputs are supplied as query-string keys in the `a_*` and `b_*` namespace.  
  * At minimum, `a_id` and `b_id` MUST be accepted as pair identifiers.  
  * Request validation MUST fail closed for missing or malformed required identifiers, and MUST use canonical typed error mapping (no ad-hoc string errors).


* Resolver acquisition and SAFE rails posture (normative).  
    
  * Provider acquisition MUST be performed through resolver acquisition (not raw cache reads), so cache hits are normalized into a resolved shape and resolved detection remains correct even when a cached record is vendor-shaped.  
  * SAFE rails posture is closed by default. When an explicit environment configuration enables open-rails acquisition, acquisition MAY open rails only long enough to acquire missing data and MUST close back before compute and emission.  
  * The owned deterministic conjunction writer-evidence capture runs with explicit closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) and a dev-only `DEV_CONJUNCTION_LOCAL_LOOKUP` of complete deterministic mapped rows. That app-config key is absent by default and is not used by the production Reader. The capture does not acquire vendor data, invent app users or bypass real release admission. A distinct live vendor step, when authorized, requires explicit caller-provided open rails and the vendor controls in §7; the generator MUST NOT silently open rails.  
  * Such writer-evidence runs do not widen the route contract and do not move this endpoint into the A7 proof family.


* Output canon (normative).  
    
  * Any success payload emitted by these routes MUST be serialized by the canonical public emitter, producing deterministic JSON bytes with ASCII-sorted keys and exactly one trailing LF.  
  * AB↔BA parity MUST hold for conjunction evaluation: swapping A and B MUST NOT change emitted bytes after canonical emission.  
  * `GET /dev/writer/conjunction` MUST emit typed, numeric-free writer-style success and error envelopes.  
  * The success envelope type MUST be `dev.writer.conjunction.success.v1`.  
  * The error envelope type MUST be `dev.writer.conjunction.error.v1`.  
  * Writer-style success and error outcomes on `GET /dev/writer/conjunction` MUST remain `Cache-Control: no-store`, MUST NOT emit `ETag`, and MUST be treated as non-conditional.


* **Identity and F07 delivery.** The dev conjunction routes consume the real admitted release identity, with no `dev_compat_identity()` stamp. PR06a restored the dev-only resolver seam, generator assertions and owned writer artifacts, and registered `tools/evidence/generate_conjunction_writer_evidence.py` with `_EVIDENCE_GENERATOR_TEST_OWNERS` for `tests/evidence/test_dev_conjunction_identity.py`. Those are delivered repository definitions and attributed historical evidence, not a new run or proof of live vendor/database behavior. The prior PR04 F07 deferral is resolved in that lineage.

* Endpoints (dev-only).  
    
  * GET /dev/sampler/conjunction  
    * Dev-only conjunction preview route for sampler evaluation.  
  * GET /dev/reader/conjunction  
    * Dev-only conjunction preview route for Reader-style response emission and VendorError mapping.  
  * GET /dev/writer/conjunction  
    * Dev-only conjunction preview route returning an idempotent writer-style envelope (not the public Reader v1 envelope).  
    * The Endpoint Catalog route id for this endpoint is `dev.writer.conjunction.v1`.  
    * The `/dev/*/conjunction` family notation is bounded to the currently canonized conjunction-family surfaces listed in this subsection.  
    * It does **not** create a reusable wildcard or standing rule that any future dev route matched by a `/dev/*/` pattern is automatically valid, dev-harness, or outside the formal proof family.  
    * Any future non-conjunction dev route requires explicit canon classification before it is treated as valid, dev-harness, or outside the formal proof family.


  ---


`````

## Redline RL-031

Operation: REPLACE

Original heading path:
># 6\. Serializer Canon & Single Emitter \[Required-Now\]
>## 6.1 Canonical JSON (UTF-8, sorted keys, compact, one LF) \[Implemented\]

Expected occurrences: 1

Old text:
`````text
* **Arrays-as-sets.** Any array that functions as a set **MUST** be deduplicated and ASCII-sorted by its identity rule (see **HDE-Schemas & Artifacts §4**).  

`````

Replacement text:
`````text
* **Arrays-as-sets.** Any array that functions as a set **MUST** be deduplicated and ASCII-sorted by its identity rule (see **HDE-Schemas & Artifacts §4**). Ordered arrays preserve their governing order. Reader v2 `categories` follows §5.1.6 and MUST NOT be set-sorted or repaired by deduplication/default filling.  

`````

## Redline RL-032

Operation: REPLACE

Original heading path:
># 6\. Serializer Canon & Single Emitter \[Required-Now\]
>## **6.2 Unify entrypoint (single presenter/emitter) \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
* **Determinism & parity.** A single byte-authoritative emitter ensures Reader↔CLI **byte equality**, **AB↔BA parity**, and **two-run identity** for identical inputs and environment.

`````

Replacement text:
`````text
* **Determinism & parity.** A single byte-authoritative emitter supplies canonical bytes for both Reader versions, **AB↔BA parity** and **two-run identity** for identical inputs/environment. Reader↔CLI byte-equality applies to Reader v1 and its CLI reader-dump; no CLI Reader v2 carrier is introduced.  

`````

## Redline RL-033

Operation: REPLACE

Original heading path:
># 6\. Serializer Canon & Single Emitter \[Required-Now\]
>## 6.3 Idempotence preimage recipe (Reader/CLI parity) \[Required-Now\]

Expected occurrences: 1

Old text:
`````text
  * `reader_version`: `"v1"`  

`````

Replacement text:
`````text
  * `reader_version`: `"v1"` or `"v2"`, matching the selected Reader contract  

`````

## Redline RL-034

Operation: REPLACE

Original heading path:
># 6\. Serializer Canon & Single Emitter \[Required-Now\]
>## 6.3 Idempotence preimage recipe (Reader/CLI parity) \[Required-Now\]

Expected occurrences: 1

Old text:
`````text
  * `categories`: `[ { "id","band" } … ]` — numeric-free and constrained by **§5.1** *(v1: when eligible: exactly one `{ "id":"harmony","band":… }`)*  

`````

Replacement text:
`````text
  * `categories`: `[ { "id","band" } ]` — numeric-free and constrained by **§5.1**: eligible v1 has exactly one harmony item; eligible v2 has exactly ten items in governed order; ineligible v1/v2 has `[]`. Reader v2 order is preserved through hashing.  

`````

## Redline RL-035

Operation: REPLACE

Original heading path:
># 6\. Serializer Canon & Single Emitter \[Required-Now\]
>## 6.3 Idempotence preimage recipe (Reader/CLI parity) \[Required-Now\]

Expected occurrences: 1

Old text:
`````text
* **Parity & determinism.** The `preimage_bytes` and final public bytes produced by Reader and CLI **MUST** be **byte-identical** for identical inputs/environment. Preimage and final bytes **MUST** also be identical for **AB vs BA** normalized inputs, and across **two runs** with the same inputs.

`````

Replacement text:
`````text
* **Parity & determinism.** Reader v1 preimage and final bytes MUST equal its CLI reader-dump for identical inputs/environment. Reader v1 and Reader v2 preimage and final bytes MUST independently be identical for **AB vs BA** normalized inputs and across **two runs**. No CLI v2 dump is defined.  

`````

## Redline RL-036

Operation: REPLACE

Original heading path:
># **7\) Vendor Ingest (HDAPI) \[Required-Now\]**
>## **7.1 Rails & Environment \[Required-Now\]**
>### **7.1.4 Environment variables (must be present and non-empty; names-only)**

Expected occurrences: 1

Old text:
`````text
* `GEO_API_KEY` (when needed)

`````

Replacement text:
`````text
* `GEO_API_KEY`

`````

## Redline RL-037

Operation: INSERT

Original heading path:
># **7\) Vendor Ingest (HDAPI) \[Required-Now\]**
>## **7.1 Rails & Environment \[Required-Now\]**
>### **7.1.5 Determinism and shaping (closed rails)**

Expected occurrences: 1

BEFORE anchor:
`````text
Missing or empty env values **MUST** produce a typed failure **without** I/O.


`````

AFTER anchor:
`````text
### **7.1.5 Determinism and shaping (closed rails)**

`````

Inserted text:
`````text
Execution uses the vendor configuration already held in the environment. The Product Owner is not required to type, paste or re-enter values. Presence preflight records only names and `SET`/`UNSET`; the base URL is configuration, not a third API key. Passing the environment to the product process is not plaintext-secret handling. Values MUST stay out of process argument lists, conversation, logs, artifacts and commits; scan captured output before admitting evidence. A rails posture MUST NOT remove the only configured base URL. If required configuration is missing, make no call and classify a begun step as `TOOLING_BLOCKED`, identifying missing names by presence only. `.env.example` omitting `GEO_API_KEY` remains an implementation-lane documentation gap; it does not waive this requirement.


`````

## Redline RL-038

Operation: REPLACE

Original heading path:
># **7\) Vendor Ingest (HDAPI) \[Required-Now\]**
>## **7.1 Rails & Environment \[Required-Now\]**
>### **7.1.8 Acceptance (titles-only; tokens live in Governance)**
>#### 7.1.8a OPS discovery, open-rails testing, and repo-reality observations (vendor ingest)

Expected occurrences: 1

Old text:
`````text
If the missing fact is safely discoverable, the work MUST route through a bounded OPS discovery task or bounded OPS open-rails task instead of guessing, silently deferring, or treating the unknown as out of scope. OPS discovery and open-rails execution remain PO-only, IA-guided, secret-safe, and evidence-recorded. Automated agents MUST NOT perform live external vendor actions, expose secret values, simulate external state changes, or claim OPS completion.

`````

Replacement text:
`````text
If the missing fact is safely discoverable, the work MUST route through a bounded OPS discovery task or bounded OPS open-rails task instead of guessing, silently deferring, or treating the unknown as out of scope. Execution remains Product Owner-authorized, IA-guided, secret-safe and evidence-recorded. The Product Owner may direct an automated session agent to execute the identified live-vendor task with the same commands and controls as a human executor; the agent is the executor and evidence producer, not an independent approver. “PO-only” identifies the authorizing and accountable principal. No agent may expose secret values, simulate external state changes, or claim OPS completion without required evidence. No standing authority is created.

`````

## Redline RL-039

Operation: INSERT

Original heading path:
># **7\) Vendor Ingest (HDAPI) \[Required-Now\]**
>## **7.1 Rails & Environment \[Required-Now\]**
>### **7.1.11 SAFE rails and production vendor override**

Expected occurrences: 1

BEFORE anchor:
`````text
### **7.1.11 SAFE rails and production vendor override**


`````

AFTER anchor:
`````text
Vendor HTTP remains subject to the generic SAFE rails in **HDE-Governance**. Closed SAFE or network rails refuse before every vendor decision and perform no credential loading, DNS, socket, or HTTP activity. The production override is an additional admin gate; it never opens either generic rail and never permits public Reader or Aux traffic to call the vendor.

`````

Inserted text:
`````text
**Required-Now implementation gap (DD-04; held).** The following production override contract is a requirement, not an available CLI facility. At `main@e7265a090ad0cc8de5f36de2f19481216aa3d073`, bounded parser/resolver inspection finds no `--allow-prod-vendor` implementation or corresponding authenticated override/audit gate. HDE Build Notes records DD-04 / QA50-B01 outside HDE-EPIC040, retained by the PF05 and CLI owners through change control. Neither the Reader deliveries, exceptional closure nor the directed-agent vendor rule implements or waives this contract. Preserve its required flag, authentication, rails and audit predicates; do not invoke or describe the flag as operational.


`````

## Redline RL-040

Operation: REPLACE

Original heading path:
># **7\) Vendor Ingest (HDAPI) \[Required-Now\]**
>## **7.4 Adapter data-source policy (PF10-AA) \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
## **7.4 Adapter data-source policy (PF10-AA) \[Required-Now\]**
`````

Replacement text:
`````text
## **7.4 Adapter data-source policy \[Required-Now\]**
`````

## Redline RL-041

Operation: REPLACE

Original heading path:
># **8\. Error Model & Exit Codes \[Required-Now\]**
>## 8.1 Typed public error object (numeric-free) \[Required−Now\]

Expected occurrences: 1

Old text:
`````text
Optional fields are schema-owned and must remain numeric-free (for example `retry_after_ms` integer ≥ 0 when transport policy explicitly permits it, and optional `details` object when permitted by the error\_v1 schema).

`````

Replacement text:
`````text
Reader v1 and Reader v2 use exactly these four keys, with no `retry_after_ms` or `details`; `schema:"v1"` versions the error envelope. Only other surfaces whose own schemas and transport policies permit them may emit optional fields. Their optional fields remain subject to the owning numeric and secret-safety constraints.

`````

## Redline RL-042

Operation: REPLACE

Original heading path:
># 9\. Acceptance & Evidence \[Required-Now\]
>## 9.1 Parity (binary)

Expected occurrences: 1

Old text:
`````text
* **Reader↔CLI byte-equality.** For identical inputs and environment, Reader response bytes and Reader-v1 bytes written by `hdctl showcompat --dump-reader <path>` MUST be byte-identical, including the single trailing LF. Ordinary `showcompat` stdout remains the distinct compat JSON envelope.  

`````

Replacement text:
`````text
* **Reader↔CLI byte-equality (v1).** For identical inputs and environment, Reader v1 response bytes and Reader v1 bytes written by `hdctl showcompat --dump-reader <path>` MUST be byte-identical, including the single trailing LF. Ordinary `showcompat` stdout remains the distinct compat JSON envelope. Reader v2 has no CLI dump flag; it retains its own AB↔BA, two-run, schema and preimage checks.  

`````

## Redline RL-043

Operation: REPLACE

Original heading path:
># **Appendix C — CLI Parity Harness (usage recipes for AB↔BA, two-run) \[Required-Now\]**

Expected occurrences: 1

Old text:
`````text
**Purpose.** Repeatable recipes to prove **Reader↔CLI byte parity**, **AB↔BA identity**, and **two-run identity**, without exposing vendor calls. The harness is **dev-only** (`APP_ENV=dev`).
`````

Replacement text:
`````text
**Purpose.** Repeatable recipes to prove **Reader v1↔CLI reader-dump byte parity**, **AB↔BA identity**, and **two-run identity**, without exposing vendor calls. The harness is **dev-only** (`APP_ENV=dev`). Reader v2 uses its ordered projection and goldens in §5.1.6; no CLI v2 carrier is introduced.
`````

## Redline RL-044

Operation: INSERT

Original heading path:
># **11\. Change Log & Doc-Delta Hooks \[Required-Now\]**
>## **11.1 Change Log (concise, normative)**

Expected occurrences: 1

BEFORE anchor:
`````text
* v2.4.9 — Define the PF12-owned `public_aux` Catalog alias model, reject undocumented Aux query controls, require exactly one `v=1`, and normalize the §6.2 status tag in §§5–6. Sentinel updated: NO.  

`````

AFTER anchor:
`````text
* **Where to put links.** Governed artifact identities and paths are indexed through the Evidence Catalog in **HDE-Schemas & Artifacts**; do not paste payload or transport bytes here. If the Human Evidence Index changes, record “Sentinel updated: YES” only after recomputing `docs/evidence/INDEX.sha256`; the sentinel is the SHA-256 digest of the canonical bytes of `docs/evidence/INDEX.json` and is not mirrored.

`````

Inserted text:
`````text
* v2.5.3 — Admit production Reader v1/v2 on the distinct POST mount; define ordered v2 projection/examples and inherited transport; correct v1 success/error schema references and resolve PR04 F03/F05/F07 deferrals; conform directed-agent vendor execution and environment/base-URL alias facts; retain held DD-04 and proof/availability limits in §§0.2, 1, 3.7, 4.1, 5.1–5.6, 5.12, 6, 7.1, 7.4, 8.1, 9.1 and Appendix C. Sentinel updated: NO.

`````

## Redline RL-045

Operation: REPLACE

Original heading path:
># **0\. Document Control \[Required-Now\]**
>  ## **0.4 Change policy**

Expected occurrences: 1

Old text:
`````text
* **Process ownership.** Use the evidence-only PR template and follow the “update in same PR” workflow defined in **Epic-Process-Guide** (titles only). **Build Notes** are WIP only; drained guidance must land in canon.  

`````

Replacement text:
`````text
* **Process ownership.** Use the evidence-only PR template and follow the “update in same PR” workflow defined in **Epic-Process-Guide** (titles only). **HDE Build Notes** is the canonical override and amendment mechanism; an applicable active addendum governs conflicting earlier canon for its scope until later drainage.  

`````

## Redline RL-046

Operation: REPLACE

Original heading path:
># **3\) CLI Overview & Conventions \[Required-Now\]**
>  ## **3.6 Determinism expectations for stdout**
>### **Dependent reconciliation outside this selection**

Expected occurrences: 1

Old text:
`````text
### **Dependent reconciliation outside this selection**

The §3.1.1 carrier set controls globally, but the unselected `bg:export-json` wording in §4.8 still permits empty stdout or a human synopsis for file success, and the unselected `admin-bundle` wording in §4.9 still permits a human file-success synopsis. Those command sections remain unchanged in this selection and require later in-owner reconciliation: each file-only success MUST emit a command-owned canonical JSON receipt after all required writes complete.


`````

Replacement text:
`````text
### **Command-carrier reconciliation gap**

The §3.1.1 carrier set controls globally, but the `bg:export-json` wording in §4.8 still permits empty stdout or a human synopsis for file success, and the `admin-bundle` wording in §4.9 still permits a human file-success synopsis. The command-specific wording requires reconciliation by its owner with the global carrier rule: each file-only success MUST emit a command-owned canonical JSON receipt after all required writes complete.


`````

END OF REDLINES
