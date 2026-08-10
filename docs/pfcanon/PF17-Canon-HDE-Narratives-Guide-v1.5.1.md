# 0\) Front Matter

## 0.1 Document Control

**Title:** PF17-Canon-HDE-Narratives-Guide  
**Version:** v1.5.1  
**Status:** Canon  
**Effective** **date**: 2026-08-10  
**Last Update Gate:** 0808 refresh 1  
**Invocation tag:** INV-f2ac55d77ce9aacc

---

## 0.2 Scope & Audience

**Scope.** This guide owns the narrative mechanics at the spec level. It defines, in names/behavioral terms (no byte dumps):

* **Deterministic composer contract.** Inputs, outputs, ranked whole-paragraph selection, suppression outcomes, shared symmetry, directional swap covariance, two-run identity, and hard lints. *(Tests/linters live in HDE-Mechanics Guide; acceptance wiring lives in the applicable phase document in the HDE-Build Checklist series — titles only.)*  
* **Narrative packs & identity linkage.** What exists and how it is referenced (**pack\_sha**, freeze-pack/manifest coupling), not byte-for-byte schemas. *(Schemas/manifest listing live in HDE-Schemas & Artifacts.)*  
* **Surfaces (policy level).** Reader v1 is narrative-free; Aux Narrative and CLI admin preview exist and are routed by title to their single homes (HDE-CLI-API-Vendor-Ref and HDE-Governance).  
* **Evidence/Doc-Delta hooks.** Names of acceptance markers and cross-doc requirements; **same-PR** human `docs/evidence/INDEX.json` \+ hash sentinel ↔ machine `artifacts/evidence_index.jsonl` parity, canonical JSONL, unknown-key rejection, ASCII field order, sort-before-write, **single mirror file**, mirror checksum, and **proof\_anchor** discipline are owned in HDE-Schemas & Artifacts and Epic-Process-Guide and referenced here by title.

**A7 proof surfaces.** A7 proofs run **only** on a **Catalog JSON success** route (Endpoint Catalog is internal-only and env-gated per entry); `/internal/version` is excluded. Evidence comprises:

* a **headers-only env-gate proof** (demonstrates non-prod entries are unreachable in prod), and  
* a **composite A7 proof JSON** (machine-checkable; schema lives in HDE-Schemas & Artifacts).  
  PF17 references these by **title only**; bytes live in HDE-CLI-API-Vendor-Ref; tokens/policy live in HDE-Governance.

**Out of scope.** This guide does **not** define:

* A7 transport rules & validators (e.g., strong ETag on 200, HEAD parity, 304 header omission, writers/errors no-store, rate-limits) → **HDE-Governance.** *(HDE-Governance also pins Aux “200 suppressed \= empty body; no ETag.”)*  
* Public payload bytes for Reader/CLI/Aux, endpoint shapes, and examples → **HDE-CLI-API-Vendor-Ref.**  
* Reader covenant & preimage/idempotence (bands-only success body) → **HDE-Math-Spec.**  
* Canonical JSON schemas, manifest listing, machine Evidence Index → **HDE-Schemas & Artifacts.**  
* Implementation tasks/tests & CI gates (lints, AB↔BA, two-run, acceptance) → **HDE-Mechanics Guide** and the applicable phase document in the **HDE-Build Checklist** series.  
* Architectural boundaries & single-emitter rule → **HDE Architecture.**

**Audience.** Engine implementers, adapter/presenter engineers, CLI maintainers, editorial/content ops, and reviewers. Editors follow titles-only routing and do **not** duplicate bytes owned by other PF documents.

**Supersession rule (HDE Build Notes addenda).** PF17 follows the latest active HDE Build Notes base version in full by applying every applicable, active, non-superseded addendum it contains. When that base version is a lettered set, every document in the set is equally authoritative. A higher-numbered addendum governs only overlapping scope or scope it explicitly supersedes; unrelated lower-numbered addenda and distinct, non-superseded scope within them remain authoritative. PF17 routes by title only (no version numbers).

---

## 0.3 Single Homes (titles-only routing)

This guide does not restate payload bytes, header matrices, or schemas that live elsewhere. It routes by document title to these single homes:

* **HDE-Governance.** A7 transport policy and validators (quoted strong ETag on 200; HEAD parity; 304 omits Content-Type and Content-Length; Vary: Authorization, Accept-Encoding; encoding-invariance), writers/errors no-store, `/internal/version` ops-only. Aux suppression: 200 with empty body, no ETag.  
    
* **HDE-CLI-API-Vendor-Ref.** Public/CLI/Aux route ownership and payload bytes; flags; stdout/sidecar guarantees. Endpoint Catalog (JSON success) is the A7 proof surface and is internal-only, env-gated; include a headers-only env-gate capture and the composite A7 proof JSON by title. The public Aux success query remains exactly `category`, `band`, and `perspective`.  
    
* **HDE-Schemas & Artifacts.** Canonical JSON constraints; freeze-pack manifest; `catalog/narratives/*` pack listing and `pack_sha` definition; human `docs/evidence/INDEX.json` and machine `artifacts/evidence_index.jsonl` (records-only) with same-PR parity, both hash sentinels where required, unknown-key rejection, ASCII field order, sort-before-write, single mirror file, and `proof_anchor` per record.  
    
  * Machine mirror discipline and registered tokens (single JSONL file; ASCII field order; sort-before-write; unknown-key reject; one LF; `proof_anchor`) are normative in their owning homes: `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
  * Header snapshots store **lower-case header names** (values verbatim). Acceptance: `SNAPSHOT_HEADER_LOWERCASE_OK`.


* **HDE-Math-Spec.** Reader covenant (bands-only public JSON), preimage and identity.  
    
* **HDE-Mechanics Guide.** Composer tasks/tests (hard lints; shared symmetry; directional swap covariance; two-run; suppression), integration with acceptance.  
    
* **Epic-Process-Guide.** PR-first; same-PR index \+ sentinel \+ mirror updates; governed locations only.  
    
* **HDE Architecture.** Engine Core, narrative-composer, Adapter, Presenter, and two-plane Loader/Exporter boundaries.  
    
* **HDE-Copy Tonality.** Editorial tone (bands-only; no em dashes), banned terms, symmetric shared copy, and directional personal views.  
    
* **Narratives authoring & storage authority (two-plane; titles-only).** In integrated mode, author in the database; an exporter snapshots to a manifest-pinned pack. Runtime loads and serves sealed files with no database read on the hot path. Ownership: HDE Architecture (two-plane wiring and Loader/Exporter boundaries), Glow Infrastructure (database names only), and HDE-Schemas & Artifacts (pack/manifest schema and release coupling). PF17 owns the narrative semantics and stays contract-free with respect to transport and schema bytes.

---

## 0.4 Acceptance & Evidence Pointers (names-only)

Names only; do not restate semantics. **Token ownership** lives in the HDE-Governance Acceptance Tokens registry; **evidence/index schema & parity** live in HDE-Schemas & Artifacts. A name not admitted by that registry or an applicable active HDE Build Notes addendum is a non-token proof label and must not be claimed as an acceptance token.

**Narratives packs:**  
`NARR_PACKS_IN_MANIFEST_OK`, `NARR_PACK_MANIFEST_OK`, `NARR_PACK_IDENTITY_OK`.

**Aux transport:**  
`NARR_200_TEXT_OK`, `NARR_SUPPRESSED_NO_ETAG_OK`, `NARR_VARY_AUTH_AE_OK`, `AUX_CANON_ALIAS_PARITY_OK`.

**Indices:**  
`EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

**Grace Gate (EPIC-010 pre-start):**  
`GRACE_DELIVERABLES_GATE_OK` *(dependency note only; not a PF17 home).*

**Owner:** HDE-Governance Acceptance Tokens registry.

---

# 1\) Purpose & Ground Rules

## 1.1 Purpose & Non-Goals

This guide defines the **what/why** of narrative composition; enforcement and tests live in **HDE-Mechanics Guide** and the applicable phase document in the **HDE-Build Checklist** series and are referenced here **by title only**.

### Purpose

Specify a **deterministic, LLM-free** layer that converts validated mechanics results and a validated narrative pack view into one short, human-readable paragraph for the **Aux narrative surface** and **CLI admin preview**, while leaving **Reader v1 unchanged and narrative-free**. The composer is a **pure function** with **two-run identity**, symmetric shared behavior, and directional swap covariance; its result is emitted through the **single shared presenter/emitter**. The concrete bytes/serializer contract is routed by title to **HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**, and **HDE Architecture**.

### Non-Goals

* **No change to Reader v1 public contract.** Reader success remains **bands-only (numeric-free)**; no narrative text appears on Reader v1. (Style/tone live in **HDE-Copy Tonality**.)  
    
* **No transport or payload bytes here.** A7 validators, ops posture, and rate-limits live in **HDE-Governance**; public and CLI/Aux endpoint shapes & payload bytes live in **HDE-CLI-API-Vendor-Ref**. Success proofs are **Catalog-driven** and run only on **Endpoint-Catalog (JSON-success)** routes; the Catalog is **internal-only** and **env-gated** (capture a **headers-only env-gate** proof). `/internal/version` is ops-only.  
    
* **No schema or manifest bytes.** Pack listings, canonical JSON rules, `pack_sha`, and the machine Evidence Index live in **HDE-Schemas & Artifacts**; this guide references them by title only.  
    
* **No randomness, time, I/O, or model calls.** Composition and `can_emit` are pure and receive an already loaded, validated, immutable pack view; required properties include **two-run identity**, shared symmetry, and directional swap covariance.  
    
* **No PII in examples/logs/artifacts.** Admin-only preview; examples use ids only (`fragment_ids`, `composition_id`, `pack_sha`, `release_id`); logs remain keys-only.  
    
* **No duplicated bytes across PF docs.** Follow the **single-home, titles-only** doctrine; keep payloads/bytes and schemas in **HDE-CLI-API-Vendor-Ref** and **HDE-Schemas & Artifacts** and transport/ops policy in **HDE-Governance**.  
    
* **No “pacing” gate here.** “Too early” is a **policy outcome** represented only by an applicable governed suppression rule; ineligible dyads are **not surfaced** (see **§2.4 can-emit**).  
    
* **No A7 proof details here.** PF17 does not own A7 bytes; it only notes that proofs require **env-gate headers** and a **composite A7 proof JSON** on a **cataloged success route**.

### 1.1.1 Non-Narrative Epic Boundary (historical; pattern for future epics)

For **EPIC-011 — Vendor Ingest & Data Durability (failed)**, Aux narratives were treated as **preservation surfaces**, not a feature surface. This pattern remains in force for any future epic whose scope is durability, ingest, infrastructure, provider rails, evidence coherence, or repo documentation rather than narrative content.

* **No new narrative semantics under non-narrative epics.**  
  Non-narrative epics may add durability structures, tests, headers-only evidence, rails/provider proofs, logs, evidence coherence artifacts, and indices around Aux narratives, but they **must not** change:  
  * the set of narrative packs and their IDs,  
  * pack text or composition,  
  * suppression rules,  
  * narrative router parity or narrative registry closure,  
  * which output surfaces exist (Aux API and CLI admin preview), or  
  * how packs are routed to those surfaces.  
* **HDE-EPIC031 boundary (SAFE rails Fermentation slice).**  
  HDE-EPIC031 evidence for SAFE rails open posture, keys-only observability, and governed evidence/indexing coherence does **not** close narrative router parity, narrative registry closure, DB bridge parity, HDAPI v2 runtime conformance, or any PF17 narrative acceptance gate. Its PR evidence and repo-docs sweep must not be cited as proof that any PF17 narrative semantics, pack contents, suppression rule, pack coverage, pack routing, Aux behavior, or CLI admin preview behavior changed.  
* **Pattern for future non-narrative epics.**  
  The same boundary applies to any future epic whose scope is durability, ingest, infrastructure, provider rails, evidence coherence, or repo documentation rather than content:  
  * narrative packs and semantics stay owned here in PF17;  
  * non-narrative epics may add tests, headers-only proofs, provider-rails proofs, logs, and indices around these surfaces;  
  * content changes (new or revised text, suppression rules, pack coverage/routing, new surfaces, or closure of narrative router parity/registry closure) must be owned by content or narrative epics, not by non-narrative provider, infrastructure, or evidence epics.  
* **Scope routing (titles-only).**  
  PF17 remains the single home for narrative semantics (packs, keys, suppression, and surfaces).  
  * **HDE-Phased Epics** is historical reference only and must not be used for planning or current acceptance rosters; current planning and acceptance use the applicable owning PF documents.  
  * Token semantics and acceptance-token admission live in **HDE-Governance**.  
    Any functional change to Aux narratives or CLI preview content **must** be planned and accepted through the applicable current owning PF documents; it remains out of scope for EPIC-011, HDE-EPIC031, and any purely durability-, provider-, infrastructure-, repo-docs-, or evidence-focused epic.

---

## 1.2 Principles \[Required-Now\]

These principles are **normative** for narrative composition; enforcement and tests live in **HDE-Mechanics Guide** and the applicable phase document in the **HDE-Build Checklist** series and are referenced here **by title only**.

**Deterministic, LLM-free composition.** The composer is a **pure function** with no randomness, time, external I/O, database access, filesystem access, or model calls. It receives pure request data and an already loaded, validated, immutable pack view. Identical inputs **must** yield identical bytes through the single shared presenter/emitter; bytes themselves are owned outside this guide.

**Two-run identity.** Repeatability is required: two executions with the same request and validated pack view produce **byte-for-byte identical** output. Determinism acceptance markers are owned outside PF17 (titles-only).

**Shared and directional coherence.** Shared evaluation is symmetric and fails closed for both viewers on any AB↔BA disagreement. Private evaluation is directional: swapping A and B maps `a_to_b` to `b_to_a` and preserves the corresponding result, but the two directional results need not be equal.

**Evidence parity (same-PR).** Every narrative change **must** update, **in the same PR**, every governed Human Evidence Index, hash sentinel, Machine Evidence Mirror, mirror checksum, and path-proof companion required by **HDE-Schemas & Artifacts**. Narrative evidence authority comes from its catalog, index, mirror, and path-proof binding; no path becomes authoritative by directory alone. Canonicalization and comparisons run with **`LC_ALL=C, LANG=C, TZ=UTC`**. *(Index/mirror schema and path-proof discipline: HDE-Schemas & Artifacts; PR-first workflow: Epic-Process-Guide — titles-only.)*

**Routing note (titles-only).** Enforcement and tests for these principles live in **HDE-Mechanics Guide** and the applicable phase document in the **HDE-Build Checklist** series; this guide lists PF17-owned rules and names-only hooks.

**Acceptance impact:** Names-only clarification; PF17 does not own pins or tokens. A proof-label name is not an acceptance token unless admitted by HDE-Governance or an applicable active HDE Build Notes addendum.

---

## 1.3 Terminology & Posture

This section defines terms and posture used in PF17. Transport and payload bytes are routed by title to **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**.

### Terms

**Category.** One of the ten compatibility categories governed by the keys registry. Candidate keys are recorded per `{category, band, perspective, slot}`.

**Narrative kind (derived; exactly two per category for one viewer)**

* **Shared Narrative** — a pair-level paragraph for both parties. Pack perspective: `shared`.  
* **Private Narrative** — a directional paragraph from one partner to the other. Pack perspective: `a_to_b` or `b_to_a`.

**Clarification.** `narrative_kind` is derived from `perspective` and is **not** a request field. `Shared ⇒ perspective=shared`; `Private ⇒ perspective∈{a_to_b,b_to_a}`. The stored pack perspective `personal` is retired because it collapses both directions. For a given viewer, the ten-category result still contains one shared key and that viewer’s directional private key per category.

### Text, Suppressed, and pre-composition error

* **Text.** Narrative is emitted when identity is valid, one whole-paragraph candidate is selected, policy allows it, and pack-time lints have passed. On Aux success, transport headers/bytes are owned by HDE-Governance and HDE-CLI-API-Vendor-Ref.  
* **Suppressed.** Deterministic outcome under valid identity when content is withheld because coverage is missing, an applicable governed `suppression_map` rule blocks every candidate, request validation fails outside identity, or the selected candidate is not lint-valid. Aux returns **200 with an empty body and no ETag**; a policy header may be present.  
* **Pre-composition identity error.** Missing, malformed, or mismatched `release_id` or `pack_sha` fails before the Text/Suppressed union as `ERR_NARRATIVE_IDENTITY_INVALID`. It does not fabricate or echo composer provenance.

**Public posture (numeric-free).** Reader v1 remains bands-only and narrative-free; narratives appear only via Aux and admin CLI preview.

**Byte discipline (route-only).** Narrative text must contain **no CR**; LF normalization is enforced by acceptance. Runtime hashing/ETag normalization is owned by HDE-Governance and HDE-CLI-API-Vendor-Ref; file artifacts remain LF-terminated. PF17 stays contract-free and routes specifics by title.

### Display Policy (per viewer)

* Everyone sees **Shared** only when the symmetric shared evaluation of `can_emit(request, pack_view)` passes for both AB and BA orientation.  
* A sees **Private-to-A** only through a request with `perspective=b_to_a`; B sees **Private-to-B** only through a request with `perspective=a_to_b`.  
* A private failure is local to that viewer’s private paragraph and does not suppress an otherwise valid Shared paragraph.  
* **Never** show a user the other party’s private paragraph.  
* Admin preview may show Shared \+ both private directions for QA only through its separately governed admin authorization.  
* **Visibility symmetry (AB↔BA).** Match-card visibility is symmetric at the **Top Category** and depends on the shared check. If shared evaluation fails or disagrees after governed AB-to-BA normalization, neither viewer sees the match for that Top Category. Narrative display then applies the per-viewer rules above.

### Spec Hook (names/fields used by this guide)

To avoid ambiguity across callers and evidence, PF17 uses these names consistently:

* `category` — Magic-10 id from the closed ten-category domain.  
* `band ∈ {Cool, Open, Warm, Glow}`.  
* `perspective ∈ {shared, a_to_b, b_to_a}`.  
* `families_fired` — a known, duplicate-free tuple already in strict ASCII order; it preserves upstream provenance but does not select prose.  
* `release_id` and `pack_sha` — lowercase 64-hex identities that must bind semantically to the explicitly supplied validated pack view.  
* `slot ∈ {1,2,3}` — pack-internal ranked candidate position; never a public request field.

### Transport Posture (route-only; titles-only)

* **A7 proof surface.** Success proofs run **only** on a **cataloged JSON success** route (Endpoint Catalog). The Catalog is **internal-only** and **env-gated**; non-prod entries must be **unreachable in prod** — capture a **headers-only env-gate proof**. `/internal/version` is ops-only and **not** A7-eligible.  
* **A7 invariants.** Success proofs must satisfy:  
  * **200:** **quoted strong ETag** over the LF-terminated canonical body and `Vary: Authorization, Accept-Encoding`.  
  * **HEAD 200:** validator parity with 200; **no body**; **`Content-Length = len(identity 200 body)`**; `Content-Type == GET`.  
  * **304:** only after prior 200; **omit both** `Content-Type` **and** `Content-Length`; **no body**.  
  * **Encoding-invariance:** identity (ETag) **and** effective `Content-Length` are stable across accepted encodings.  
  * *(Composite A7 proof JSON is required; schema lives in HDE-Schemas & Artifacts. All bytes/tests live in HDE-Governance, HDE-CLI-API-Vendor-Ref, and HDE-Mechanics Guide; PF17 remains contract-free.)*

**Routing (titles-only).** Transport validators live in **HDE-Governance**; concrete Aux/CLI payload bytes live in **HDE-CLI-API-Vendor-Ref**. PF17 defines **terms and posture** only.

---

# 2\) System Overview (contract-free)

## 2.1 Actors & Boundaries (Engine Core/Narrative Composer/Adapter/Presenter; single-emitter boundary) \[Canon\]

**Actors (responsibilities).**

* **Engine Core** — deterministic mechanics compute only; no time/network/I/O/randomness; returns normalized keys and structures, not narrative text.  
* **Narrative Composer** — a deterministic, pure function outside Engine Core. It consumes normalized mechanics results and an explicitly supplied, already loaded, validated, immutable narrative pack view. It selects one whole paragraph and returns a Text or Suppressed structure; it performs no I/O.  
* **Adapter** — single HTTP home; validates the public request, supplies governed internal identity and provenance inputs, calls the in-process boundaries, and **never hand-crafts public JSON**.  
* **Presenter (canonical emitter)** — the **one** emitter that serializes public bytes for all callers (HTTP and CLI). **Alternate serializers are forbidden** on public paths.

**Boundary guarantees (conceptual).**

* Engine Core produces **keys/structures only**. Narrative loading, composition, and preview remain isolated from Engine Core.  
* Loader and authoring/exporter I/O occur outside the pure composer call. The composer and `can_emit` receive the validated pack as pure data and do not access ambient loader state.  
* Adapter does **not** emit ad-hoc JSON. All public bytes come from the Presenter’s **single canonical emitter**.  
* **One emitter path for CLI and HTTP**; corresponding bytes are identical for the same inputs and surface contract. CLI text is LF-terminated.  
* Architecture remains **contract-free**; payload schemas and transport/header rules are owned elsewhere (titles-only routing).

**Routing (titles-only).**

* **HDE Architecture:** role boundaries, two-plane narrative architecture, single-emitter rule, contract-free stance.  
* **HDE-CLI-API-Vendor-Ref:** public/CLI/Aux route bytes and Endpoint Catalog ownership.  
* **HDE-Governance:** A7 transport policy, writers/errors posture, and Aux suppression policy.  
* **HDE-Schemas & Artifacts:** pack identity, manifest membership, composer response schema, and canonical JSON.

---

## 2.2 End-to-End Flow (CLI/HTTP call path; same bytes; LF discipline)

1. **Entry (CLI or HTTP → Adapter).** Adapter validates the public request and calls the in-process Engine and narrative boundaries; it never hand-crafts public JSON. The public Aux success query remains exactly `category`, `band`, and `perspective`.  
     
2. **Internal request assembly.** The Adapter or Presenter supplies the canonical `families_fired`, active `release_id`, requested `pack_sha`, and an already loaded, manifest-verified, immutable `ValidatedNarrativePackView`. These values are not added to the public success query.  
     
3. **Identity preflight.** Before routing, suppression, or composition identity creation, validate identity presence, lowercase 64-hex syntax, narrative-manifest digest equality, required narrative-member inclusion in the root freeze manifest, and release binding. Failure returns `ERR_NARRATIVE_IDENTITY_INVALID` outside the Text/Suppressed union.  
     
4. **Compute and select.** Engine Core supplies normalized mechanics results. The pure Narrative Composer evaluates the exact category, band, perspective, and strict slot order `1`, then `2`, then `3` against the validated pack view and selects at most one complete paragraph.  
     
5. **Emit (Presenter — single canonical emitter).** One emitter serializes public bytes for all callers; alternate serializers on public paths are forbidden. Composition remains deterministic and I/O-free.  
     
6. **Parity (same bytes for CLI and HTTP).** Adapter returns the **exact** Presenter bytes to HTTP; CLI writes the corresponding governed bytes to stdout with required **LF termination**. Parity applies only where the two surfaces own the same contract.  
     
7. **Aux specifics (routing only).** When suppressed under a valid identity, Aux returns **200 with an empty body and no ETag**; a policy header is optional. An identity error follows the governed typed-error path with no narrative provenance headers.  
     
8. **A7 proof surface (routing only).** Proofs run **only** on a **Catalog JSON success** route. The Catalog is **internal-only** and **env-gated**; capture a **headers-only env-gate** proof; `/internal/version` is excluded. The exact A7 rules and composite proof schema remain in their owning documents.  
     
9. **Authoring and runtime planes.** In integrated mode, narrative content is authored in the database and exported to a manifest-pinned pack. Runtime and standalone paths consume the same validated sealed pack bytes; no runtime hot-path database read is permitted. Admin authoring preview must be compared with the exported pack for source invariance rather than making the runtime Presenter read the authoring database.  
     
10. **LF discipline.** Output is LF-only; narrative text contains no `\r`. Acceptance checks live in HDE-Mechanics Guide and the applicable phase document in the HDE-Build Checklist series.

---

## 2.3 Data Hand-Off (keys-only registry & packs; bytes live elsewhere)

**Engine hand-off.** Normalized keys/structures only: `category`, `band`, `families_fired`, and `perspective`. The Engine Core remains deterministic and I/O-free. `families_fired` preserves governed mechanics provenance but does not rank or select prose.

**Presenter/Composer consumption.** Resolve candidates against governed content selected by **pack identity**:

* **Authoring → Export.** In integrated mode, the authoring source of truth **must be the DB**; the **Exporter must** snapshot to `catalog/narratives/*` and list members in the freeze manifest.  
    
* **Pack manifest — MUST.** `catalog/narratives/manifest.json` **MUST** exist and be listed **exactly once** in `catalog/manifest.json`. Each required narrative member is listed exactly once in the narrative manifest and root freeze manifest as governed by HDE-Schemas & Artifacts.  
    
* **Identity.** `pack_sha = sha256(canonical_bytes("catalog/narratives/manifest.json"))`, where the controlling canonical bytes include exactly one final LF. `pack_sha` is lowercase 64-hex.  
    
* **Candidate registry.** The normative key is `(category, band, perspective, slot) -> template_key`, with ten categories, four bands, perspectives `shared|a_to_b|b_to_a`, and slots `1|2|3`: 360 required candidate rows. The stored pack perspective `personal` is retired.  
    
* **Templates.** Each template value is one complete paragraph candidate. Numeric slots rank candidates in strict order; they are not paragraph positions and are never concatenated.  
    
* **Palettes.** `palettes.json` remains a required governed member whose bytes affect identity, but palette metadata is inert under the current composer contract.  
    
* **Suppression.** `suppression_map` may block a governed candidate. Missing or blocked candidates advance selection from slot 1 to 2 to 3; if none is eligible, the composer resolves to `missing_narrative_key` and suppresses under a valid identity.

**Per-viewer result.** For each of the ten categories, a viewer receives one shared key and that viewer’s directional private key. This preserves the ten-by-two viewer result without collapsing the three authored pair perspectives.

**Identity & traceability.** Pack selection couples to **`release_id`** via the root manifest. Valid Text and Suppressed results echo `pack_sha` and `composition_id`; an invalid-identity error echoes neither.

**Out of scope (titles-only routing).** Pack/schema bytes (HDE-Schemas & Artifacts); payload/CLI/Aux bytes (HDE-CLI-API-Vendor-Ref); A7 transport/header matrices (HDE-Governance).

## 2.4 Visibility Coupling (`can_emit` predicate; contract-free; titles-only) \[Canon\]

**Canonical request value.** The pure predicate receives this exact request:

```
CanEmitRequest {
  category: Magic10Id,
  band: Band,
  perspective: Perspective,
  families_fired: tuple[FamilyId, ...],
  release_id: LowerHex64,
  pack_sha: LowerHex64
}
```

The predicate is:

```
can_emit(request: CanEmitRequest,
         pack_view: ValidatedNarrativePackView) -> bool
```

This is one internal predicate, not a public API expansion. The Adapter or Presenter supplies `families_fired`, `release_id`, `pack_sha`, and the validated pack view from governed internal state. `pack_view` must already be loaded, manifest-verified, immutable for the call, and bound to the stated identities. The predicate performs no file access, database access, network access, clock read, randomness, model call, text rendering, or hidden-global lookup.

**Input and candidate rules.**

1. `category` must be one of the closed Magic-10 IDs. All ten categories remain independently supported; `harmony` is not a proxy for the other nine.  
2. `band` must be exactly one of `Cool`, `Open`, `Warm`, or `Glow`.  
3. `perspective` must be exactly one of `shared`, `a_to_b`, or `b_to_a`.  
4. `families_fired` must contain only known family IDs, contain no duplicates, and already be in strict ASCII order. The predicate does not sort, deduplicate, repair, or fabricate it. Empty `families_fired` is not rejected merely for being empty; upstream mechanics owns whether it is valid.  
5. `release_id` and `pack_sha` must be lowercase 64-hex and semantically bound to `pack_view`; format validity alone is insufficient. Identity preflight failure occurs before `can_emit`.  
6. The requested category, band, perspective, and at least one eligible whole-paragraph candidate must exist in the validated pack. Evaluate slots in strict order `1`, then `2`, then `3`.  
7. Applicable `suppression_map` rules must permit the selected candidate. A schema-owned family-sensitive guard may inspect `families_fired`; families do not otherwise choose prose.  
8. The selected whole paragraph must already have passed pack-time structural and editorial validation. `can_emit` consults immutable validation state and does not render or transform text.

**Shared and directional evaluation.** For category `C`, define:

```
shared_ab = can_emit(shared request in AB orientation)
shared_ba = can_emit(the same shared request after governed AB-to-BA normalization)
private_to_a = can_emit(perspective=b_to_a)
private_to_b = can_emit(perspective=a_to_b)
```

1. **Shared is symmetric.** `shared_ab` and `shared_ba` must be equal. Shared display is permitted only when both are true. A disagreement is an invariant failure and resolves to false for both viewers.  
2. **Top-category match visibility is symmetric.** A dyad may be surfaced for the Top Category only when the shared symmetric check passes. If it fails, neither viewer sees the match for that Top Category. Base Reader eligibility remains separately owned by HDE-Math-Spec. `can_emit` may withhold an otherwise eligible result but may never make an ineligible dyad visible.  
3. **Private is directional.** A sees only `b_to_a`; B sees only `a_to_b`. These booleans may differ.  
4. **Swap covariance, not forced equality, governs Private.** Swapping A and B maps `a_to_b` to `b_to_a` and preserves the corresponding result. It does not require identical directional prose or eligibility.  
5. **A private failure is local.** It withholds only that viewer’s private paragraph and does not expose the other viewer’s paragraph, suppress valid shared text, or change the Magic-10 score or band.  
6. **Privacy is absolute.** No caller may obtain the other person’s private paragraph through perspective relabeling. Admin preview may inspect all three perspectives only under separately governed admin authorization.

**Human Design boundary.** `can_emit` does not calculate a chart, score a category, change a band, reinterpret a Gate or Channel, or infer a family that canonical mechanics did not emit. It may only withhold text or visibility from an upstream all-ten-category mechanics result.

**Determinism pins.** Composer captures and checks run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`. The pure predicate itself does not read environment state.

**Acceptance hooks (titles-only).** Tests and CI gates live in HDE-Mechanics Guide; ship/no-ship gates live in the applicable phase document in the HDE-Build Checklist series; pack and suppression schemas live in HDE-Schemas & Artifacts. Any unregistered hook name is a non-token proof label.

**Routing (titles-only).**

* **HDE-Schemas & Artifacts:** pack/manifest and `suppression_map` definitions.  
* **HDE-CLI-API-Vendor-Ref:** list/detail routes and visibility endpoints.  
* **HDE-Governance:** transport policy; A7 proof surface and ops exclusion.  
* **HDE Architecture:** pure-data dependency and two-plane boundary.

---

# 3\) Composer Specification

## 3.1 Inputs Tuple (validated)

The composer accepts only a validated request and an explicitly supplied validated narrative pack view. Identity and request-domain validation occur before candidate selection. No invalid input is repaired or replaced with ambient state.

### Required Request Inputs (exact fields)

* **`category`** — Magic-10 id from the closed ten-category set.  
* **`band`** — one of `{"Cool","Open","Warm","Glow"}`.  
* **`families_fired`** — tuple of known family ids, already **ASCII-sorted** and **unique**. It may be empty when the owning upstream mechanics contract permits that result.  
* **`perspective`** — one of `{"shared","a_to_b","b_to_a"}`.  
* **`release_id`** — **lowercase 64-hex** id of the active freeze manifest.  
* **`pack_sha`** — **lowercase 64-hex** identity of the narrative pack in use.

The pure-data dependency is:

```
pack_view: ValidatedNarrativePackView
```

`pack_view` must already be loaded, manifest-verified, immutable for the call, and bound to the requested `pack_sha` and `release_id`. It is not a public request field.

**Public posture (routing).** The public Aux success route accepts exactly `category`, `band`, and `perspective`. `families_fired`, `release_id`, `pack_sha`, and `pack_view` are supplied from governed internal state. `slot` is not a public field.

**Notes.** Earlier inputs `uncertainty` and `pace_met` are retired. The request is **keys-only**; it contains **no free text** and introduces **no I/O**. The stored pack perspective `personal` is also retired; directional requests use `a_to_b` or `b_to_a`.

### Pre-Composition Validation (fail-closed)

Validation occurs before selection in this order:

1. **Identity preflight.** Require non-blank `release_id` and `pack_sha`; exact lowercase 64-hex syntax; `pack_sha` equality with the digest of the validated narrative manifest bytes; root freeze-manifest inclusion of the required narrative members; and equality between `release_id` and the active validated freeze identity binding that pack. Failure returns `ERR_NARRATIVE_IDENTITY_INVALID` outside the Text/Suppressed union.  
2. **Request-domain validation.** Require a canonical category, band, perspective, and known, duplicate-free, strictly ASCII-ordered family tuple. The composer receives this validated domain. A caller or transport that supplies a malformed field follows the typed input-error mapping in its owning contract; PF17 does not invent a token or a third composer variant.  
3. **Pack-view binding.** Require the explicit pack view to match the validated identities and to expose immutable validation state for all governed members. Do not substitute the loaded active pack for invalid caller identity.  
4. **Candidate eligibility.** Resolve the exact category, band, and perspective group and evaluate candidates in strict slot order `1`, `2`, `3`. Missing coverage or no eligible candidate produces a valid-identity Suppressed result.

The preflight performs no retries, repairs, sorting, deduplication, file access, database access, network access, clock read, randomness, model call, or text rendering.

---

## 3.2 Outputs (choose one after successful identity preflight)

After successful pre-composition identity and request validation, exactly one of the following PF12-owned response variants **MUST** be returned.

### Text Path

```json
{
  "composition_id": "<string>",
  "fragment_ids": ["<selected_template_key>"],
  "pack_sha": "<64-hex>",
  "text": "<string>"
}
```

**Constraints (names-only).** `text` is at most 300 characters and contains no `\r`; `composition_id` is 69 ASCII characters under the current recipe and remains within the PF12 `8..128` bound; `fragment_ids` contains exactly one selected template key; `pack_sha` is lowercase 64-hex.

### Suppressed Path

```json
{
  "composition_id": "<string>",
  "pack_sha": "<64-hex>",
  "policy_reason": "conflict",
  "suppressed": true
}
```

**Enum.** `policy_reason == "conflict"` only. Suppression applies only after identity and request-domain validation, when no whole-paragraph candidate is eligible because coverage is missing, all candidates are blocked by governed suppression, or all candidates fail pack-time schema or editorial validation. The Suppressed variant omits `text` and `fragment_ids`.

For this valid-identity no-candidate outcome, compute `composition_id` with the internal singleton `fragment_ids:["missing_narrative_key"]` preimage defined in §3.12. Do not expose that internal array in the Suppressed object.

### Pre-Composition Identity Error (outside the union)

The canonical typed condition is `ERR_NARRATIVE_IDENTITY_INVALID` with the non-secret public message:

```
narrative identity is missing, malformed, or not bound to the active release
```

This condition is not a Text or Suppressed object. `composition_id`, `fragment_ids`, `pack_sha`, narrative body, `X-Narrative-Pack-Sha`, and `X-Narrative-Composition` are absent, and the loaded active identity is not substituted. Internal diagnostics may contain only bounded `field` and `reason` keys, with `reason ∈ {missing, malformed, mismatch}`.

HDE-CLI-API-Vendor-Ref owns HTTP and CLI mapping. HTTP uses the governed `error_v1` path with `Cache-Control: no-store` and no ETag. CLI leaves stdout empty and emits the same canonical token on stderr; PF17 does not invent an exit code. The token and schema must be registered in their governed homes before implementation conformance is claimed.

### Semantics (contract-free summary; bytes live elsewhere)

* **Aux surface (titles-only).** When text is shown, Aux returns its PF05-owned 200 text representation. When **suppressed**, Aux returns **200 with an empty body and no ETag**; a generic policy header may be present. An identity error follows the typed-error path and emits no narrative provenance.  
* **CLI parity & evidence.** Admin CLI preview uses the corresponding governed emitter path. Narrative stdout is LF-terminated; sidecars, logs, and evidence contain ids only and no narrative text.

---

## 3.3 Lints (MUST)

The following lints are **normative** and **MUST** pass at pack validation for any candidate eligible for the Text path:

1. **Length cap:** Narrative text **≤ 300** UTF-8 characters.  
2. **Sentence count:** **2–4 sentences**.  
3. **Form:** **Single paragraph** (no blank lines).  
4. **Numeric-free:** **No numbers** in public text.  
5. **No em-dashes:** reject `—` (use periods or commas instead).  
6. **Line discipline:** **LF-only**; text **must not** contain `\r`.  
7. **Tone:** Inclusive, present-tense, felt-only wording; no advice, destiny language, blame, or Human Design jargon in public text. *(Titles-only pointer to HDE-Copy Tonality.)*

**Candidate handling (deterministic).** During strict slot evaluation, a schema-invalid or lint-invalid candidate is ineligible and selection advances to the next numeric slot. If no candidate passes, return the valid-identity Suppressed result. After a candidate is selected, do not retry another slot because a downstream transform, emitter, or transport step fails.

The checked-in restricted-character lint is repository behavior, not an additional PF17 requirement. Repository bytes alone do not authorize a new canonical character allow-list or acceptance token.

**Validation hooks (non-token labels unless admitted by HDE-Governance).**  
`NARR_LEN_≤300_OK` · `NARR_2TO4_SENTENCES_OK` · `NARR_SINGLE_PARAGRAPH_OK` · `NARR_NO_NUMERICS_OK` · `NARR_NO_EM_DASH_OK` · `NARR_LF_NORMALIZATION_OK` · `NARR_JARGON_FREE_OK` · `NARR_INCLUSIVE_TONE_OK`.

**Routing (titles-only).** Editorial rules: HDE-Copy Tonality; schema and pack validation: HDE-Schemas & Artifacts; public/CLI bytes: HDE-CLI-API-Vendor-Ref; transport: HDE-Governance; mechanics and fixtures: HDE-Mechanics Guide.

---

## 3.4 Determinism — pure function; no RNG/time/I/O; two-run identity; shared symmetry and directional swap covariance

The composer is a **closed, deterministic function**:

* **Pure, LLM-free function.** **No randomness, time, external I/O, database access, filesystem access, environment read, hidden global state, or model calls.** It receives the validated request and `ValidatedNarrativePackView` as pure data.  
* **Two-run identity.** Running the composer twice with identical request and pack-view inputs **MUST** yield **byte-for-byte identical** output.  
* **Shared symmetry.** Shared AB and normalized BA evaluations must select the same governed shared candidate and produce identical results. A disagreement fails closed for both viewers.  
* **Directional swap covariance.** Swapping A and B maps `a_to_b` to `b_to_a` and preserves the corresponding result. The two directions may select different governed paragraphs and need not be equal.  
* **Whole-template selection.** Numeric slots are ranked complete paragraphs. Exactly one eligible candidate is selected; no fragments are concatenated.  
* **Normalization.** Determinism is supported by pack-time text validation and PF12 canonical identity bytes.

**Environment pins (captures/checks).** Run composer captures, header/body snapshots, and canonicalization under **`LC_ALL=C, LANG=C, TZ=UTC`**. The pure composer does not read those variables at call time.

**Validation hooks (non-token labels unless admitted by HDE-Governance).**  
`NARR_DETERMINISM_OK` · `NARR_AB_BA_COHERENCE_OK` · `NARR_LF_NORMALIZATION_OK`.

**Repository posture.** The normative contract is not a conformance claim. At the pinned repository state, `compose_text` reads ambient `get_pack()` state and first use can load and mount filesystem content; shared and directional conformance are therefore not established by static inspection.

**Routing (titles-only).** Tests/fixtures: HDE-Mechanics Guide; ship/no-ship gates: applicable HDE-Build Checklist phase; transport/payload bytes: HDE-Governance and HDE-CLI-API-Vendor-Ref.

## 3.5 Suppression Policy — deterministic, conflict-only; pack rules allowed

**Status.** *Normative specification.* This policy specifies when the composer **must** return the **Suppressed** result. It is deterministic, has no heuristics or runtime retries, and applies only after identity and request-domain validation. Repository conformance is assessed separately.

**Triggers (exact).**

1. **Missing coverage.** No candidate group exists for the canonical `{category, band, perspective}` tuple.  
2. **No eligible numeric candidate.** In strict slot order `1`, `2`, `3`, every candidate is missing, schema-invalid, editorially lint-invalid, or blocked by an applicable governed `suppression_map` rule.  
3. **Perspective/key conflict.** The validated group or candidate does not match the exact `shared`, `a_to_b`, or `b_to_a` perspective.

Each trigger resolves to `missing_narrative_key` internally and returns the Suppressed variant with `policy_reason:"conflict"`. No alternate pack-defined public reason is allowed.

**Not suppression.** Missing, malformed, or mismatched identity returns `ERR_NARRATIVE_IDENTITY_INVALID` before this policy. Malformed public or internal request-domain inputs follow their owning typed input-error mapping and do not enter the composer union.

**Retired reasons.** Earlier drafts listed `uncertainty_high` and `pace_unmet`. Both remain retired from the spec and response enum. Suppression is conflict-based only.

**Surface behavior (titles-only).**

* **Aux narrative:** on suppression, return `200` with an empty body and **no `ETag`**. A policy header such as `X-Narrative-Policy: suppressed` **may** be present. *(HDE-Governance governs; this guide does not restate bytes.)*  
* **CLI preview:** mirrors the same no-text content outcome; bytes and flags live in HDE-CLI-API-Vendor-Ref.

**Can-emit coupling (no render needed).** Visibility uses the same explicit `CanEmitRequest`, immutable pack view, identity preflight, candidate eligibility, and governed suppression state as composition. It does not render or transform text.

**Reader posture.** Reader v1 remains numeric-free and carries no narrative text; base Reader eligibility remains separate from narrative visibility.

**Evidence & logging.** Logs are keys-only and never include narrative text. Valid-identity Suppressed results retain `composition_id` and `pack_sha`; invalid-identity errors retain neither. Governed evidence updates follow HDE-Schemas & Artifacts and Epic-Process-Guide.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `NARR_SUPPRESS_ON_CONFLICT_OK` · `CAN_EMIT_CONFLICT_FAILS_OK` · `CAN_EMIT_PACK_GUARD_FAILS_OK` · `AB_BA_VISIBILITY_PARITY_OK`.

**Routing (titles-only).** Packs, manifest, and `suppression_map` → HDE-Schemas & Artifacts; payload bytes and CLI routes → HDE-CLI-API-Vendor-Ref; transport → HDE-Governance.

---

## 3.6 Failure Modes & Fallbacks — fail closed; no relaxation paths

**Status.** *Normative specification.* The composer must fail closed and must never fix up inputs, relax validation, retry downstream failures with alternate content, or emit partial text. Repository conformance is assessed separately.

**Failure classes.**

1. **Identity failure.** The §3.1 identity preflight returns `ERR_NARRATIVE_IDENTITY_INVALID` outside the composer union, with no narrative body or provenance.  
2. **Request-domain failure.** Malformed category, band, perspective, or family provenance does not enter the composer union; the owning caller or transport applies its governed typed input-error mapping.  
3. **Valid-identity content conflict.** The exact triggers in §3.5 return the Suppressed variant.  
4. **Downstream failure after selection.** A runtime transform, emitter, or transport failure does not cause selection to retry slot 2 or 3; it follows the owning failure contract.

**Fallbacks (what we do not do).**

* **No relaxation paths.** Do not lower lint thresholds, concatenate candidates, randomize, apply a palette, or soften output to pass. Prefer suppression to fabricated prose.  
* **No auto-correction of inputs.** Do not sort or deduplicate `families_fired`, normalize an unknown enum into a known value, or replace an invalid identity with the active pack.  
* **No alternate emitters.** Public bytes come only from the single canonical emitter. If required parity cannot be established, do not emit the success representation.  
* **No hidden reads.** The composer and `can_emit` do not load files, read the authoring database, use environment state, or fetch a pack.

**Surface behavior (titles-only).** Valid-identity suppression returns the Aux policy outcome owned by HDE-Governance. Typed errors follow HDE-CLI-API-Vendor-Ref and HDE-Governance. PF17 does not define a parallel transport matrix.

**Evidence & logging posture.**

* Echo identities only for valid Text and Suppressed results.  
* Logs are keys-only, never narrative text, and preserve LF discipline.  
* Evidence authority and companion files follow HDE-Schemas & Artifacts.

**Routing (titles-only).** Packs/manifest/`suppression_map` → HDE-Schemas & Artifacts; public/CLI bytes → HDE-CLI-API-Vendor-Ref; transport → HDE-Governance.

---

## 3.7 Composer Mechanics — ranked whole-paragraph candidates

**Scope.** Select exactly one complete paragraph deterministically from governed pack candidates; **no model calls** and no fragment assembly.

**Candidate model.** The exact key is `(category, band, perspective, slot) -> template_key`, where `slot ∈ {1,2,3}` is a ranked whole-paragraph candidate position.

**Selection.**

1. Resolve the exact category, band, and perspective candidate group.  
2. Evaluate slots in strict order `1`, then `2`, then `3`.  
3. Select the first candidate that is present, schema-valid, editorially lint-valid, and not blocked by governed suppression.  
4. If no candidate is eligible, use the internal `missing_narrative_key` sentinel and return the valid-identity Suppressed variant.  
5. After selection, do not retry a later slot because a downstream transform, emitter, or transport step fails.

**Inputs (names-only).** `category`, `band`, `families_fired`, `perspective ∈ {shared,a_to_b,b_to_a}`, `pack_sha`, `release_id`, and `ValidatedNarrativePackView`. `families_fired` validates provenance or a schema-owned suppression guard but does not rank candidates.

**Retired current vocabularies.** `lead`, `bridge`, `close`, `opener`, `center`, `closer`, and `softener` are not current slots. Numeric candidates are not concatenated. A later multi-fragment composer requires a separately versioned pack schema, content migration, and provenance contract.

**Determinism.** No RNG, user-id hashing, wall time, process rotation, viewer preference, I/O, or hidden default affects selection.

**Routing (titles-only).** Pack schemas and candidate validation live in HDE-Schemas & Artifacts; surface bytes live in HDE-CLI-API-Vendor-Ref; mechanics and tests live in HDE-Mechanics Guide.

---

## 3.8 Key Resolution — registry and perspective paths

**Registry rule.** The required full candidate grid contains:

```
10 categories x 4 bands x 3 perspectives x 3 slots = 360 candidate rows
```

For an exact `{category, band, perspective}`, resolve up to three `template_key` values by numeric slot:

* `perspective=shared` → shared candidates.  
* `perspective=a_to_b` → A-to-B directional candidates.  
* `perspective=b_to_a` → B-to-A directional candidates.

For a given viewer, each category still yields two narrative keys: the shared key and that viewer’s directional private key. `personal` may remain a derived narrative-kind label but is not a request or pack-key perspective.

**Missing-key sentinel (fail-closed).** Missing group coverage or no eligible candidate resolves internally to `missing_narrative_key`. This sentinel is not a fallback template and never selects alternate prose. It supplies the valid-identity Suppressed `composition_id` preimage and is omitted from the public Suppressed object.

**No ambiguous tie.** Slot is the complete priority order. Duplicate tuples, duplicate slot identities, unsupported values, or partial required groups fail pack validation; ASCII title is not a runtime tie-breaker.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `COMPOSE_KEY_RESOLUTION_OK` · `COMPOSE_SLOT_ORDER_OK`.

---

## 3.9 Family Provenance Boundary

`families_fired` does **not** participate in current template selection, candidate ranking, or `composition_id` derivation.

It remains available only for:

* validation that the narrative request came from a complete, governed mechanics result; and  
* an explicitly schema-owned family-sensitive suppression rule, if one is present.

Do not convert family ids into prose through an undocumented priority table. Do not treat a numeric slot as a Gate, Channel, electromagnetic connection, compromise, dominance, or other Human Design mechanic. Any future family-sensitive narrative model requires a separately versioned semantic mapping and editorial corpus.

**Validation hook (non-token label unless admitted by HDE-Governance).** `COMPOSE_FAMILY_PROVENANCE_OK`.

---

## 3.10 Whole-Paragraph Validation — punctuation, casing, whitespace

Each governed template is one complete paragraph and passes these pack-time rules before it can be selected:

* Sentences end with `. ? !` only; **no em dash (—)**.  
* Spaces are normalized to one between words and one after sentence marks; no trailing spaces.  
* Sentence case; no all-caps beyond acronyms.  
* Quotes are straight `" "` (no smart quotes).  
* Final output is **one paragraph**, **2–4 sentences**, **≤300 characters**, **LF-only**, with no `\r`.

The runtime does not concatenate candidates or apply a text transform to make invalid content pass. A later-slot candidate may be selected only because it independently passed the same governed validation.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `NARR_NO_EM_DASH_OK` · `NARR_LF_NORMALIZATION_OK` · `NARR_LEN_≤300_OK` · `NARR_2TO4_SENTENCES_OK` · `NARR_SINGLE_PARAGRAPH_OK`.

## 3.11 Palettes and Variants \[Future-Promotion\]

**Current contract.** `catalog/narratives/palettes.json` remains a required governed pack member. Its exact bytes participate in `pack_sha` and, through the root freeze manifest, the coupled `release_id`.

**Inert metadata.** The current composer does not select a palette, apply synonym replacement, accept a palette identifier, or use an operator flag, public query parameter, environment variable, or hidden default to change narrative bytes. The current `default` palette metadata is inert; loader presence does not establish runtime adoption. `palette_id` is absent from `CanEmitRequest` and the current `composition_id` preimage.

**Determinism.** Whole paragraphs remain byte-stable. No claim may be made that a palette produced or modified current output bytes.

**Future promotion.** Any future palette that changes output requires a versioned pack and composer contract, explicit validated palette identity, inclusion in `composition_id`, identity and ETag updates, post-transform structural and tonality lints, fail-closed activation, and separately authorized public exposure if applicable. These are promotion prerequisites, not a current selection algorithm.

**Routing (titles-only).** Palette schema and pack identity live in HDE-Schemas & Artifacts; any future public or admin control lives in HDE-CLI-API-Vendor-Ref and HDE-Governance.

## 3.12 Composer Provenance — singleton ids and fixed derivation

**`fragment_ids` mapping.** For Text, emit exactly:

```
fragment_ids = [selected_template_key]
```

The selected whole paragraph is the single governed content unit. No `lead`, `bridge`, or `close` ids are fabricated. Suppressed omits `fragment_ids`.

**`composition_id` preimage.** Build exactly this logical object:

```json
{
  "band": "<canonical band>",
  "category": "<Magic-10 id>",
  "fragment_ids": ["<selected template key>"],
  "pack_sha": "<lowercase 64-hex>",
  "perspective": "<shared|a_to_b|b_to_a>",
  "release_id": "<lowercase 64-hex>"
}
```

Serialize it under HDE-Schemas & Artifacts canonical JSON rules: UTF-8, strict ASCII object-key order, compact separators, and exactly one final LF. Then compute:

```
composition_id = "comp_" + sha256(canonical_preimage_bytes).hexdigest()
```

The result is 69 ASCII characters. It changes when any material selector, selected key, pack, perspective, or release changes and is independently recomputable.

**Suppressed preimage.** For a valid-identity no-candidate outcome, use the internal singleton `fragment_ids:["missing_narrative_key"]`; do not return `fragment_ids` in the Suppressed object. Identity failure occurs before any preimage and produces no `composition_id`.

**Echo fields.** Valid Text and Suppressed results echo `pack_sha` and `composition_id`. Invalid-identity errors echo neither.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `COMPOSE_IDS_DETERMINISM_OK`, `COMPOSE_SLOT_MODEL_OK`.

**Routing (titles-only).** The canonical response schema and serialization constraints belong to HDE-Schemas & Artifacts; public payload and sidecar bytes belong to HDE-CLI-API-Vendor-Ref.

## 3.13 `suppression_map` Semantics — candidate-level blocking

**Current semantic boundary.** `suppression_map` is a governed pack member that can make a specific candidate ineligible. The exact map schema belongs to HDE-Schemas & Artifacts. PF17 does not invent an independent guard-field taxonomy.

**Precedence.**

1. Identity and request-domain validation complete before suppression evaluation.  
2. Resolve the exact category, band, and perspective group.  
3. Evaluate slots `1`, `2`, `3` in order. A candidate is eligible only if present, schema-valid, editorially lint-valid, and not blocked by an applicable map rule.  
4. Select the first eligible candidate.  
5. If none is eligible, resolve to `missing_narrative_key` and return the valid-identity Suppressed variant.

An absent candidate-level block does not itself block the candidate. A family-sensitive rule may inspect `families_fired` only when the governed schema explicitly owns that field. `families_fired` otherwise does not select or rank prose. Internal map reasons do not expand the public `policy_reason:"conflict"` enum.

**Validation hook (non-token label unless admitted by HDE-Governance).** `COMPOSE_SUPPRESSIONMAP_GUARDS_OK`.

**Routing (titles-only).** Guard schema belongs to HDE-Schemas & Artifacts; transport semantics of suppression live in HDE-Governance and HDE-CLI-API-Vendor-Ref.

## 3.14 Authoring Plane — DB-first; exporter snapshot

**Required source of truth (integrated mode).** Keys, templates, optional future palette authoring metadata, and `suppression_map` **must be authored and stored in the application database**.

**Exporter (release).** A release Exporter snapshots the governed authoring rows into a **manifest-pinned pack** under `catalog/narratives/*`, writes or updates `catalog/narratives/manifest.json` exactly once, and lists that manifest and every required member exactly once in `catalog/manifest.json`.

**Direction-aware preservation.** Export must preserve the complete 360-row `{category, band, perspective, slot}` candidate inventory. It must not collapse `a_to_b` and `b_to_a` into `personal`, split whole paragraphs, concatenate slots, or rewrite content implicitly.

**Preview parity.** Admin authoring preview may read the authoring plane. The exported pack for the same governed release **must** produce identical composer inputs and outputs in a source-invariance comparison. This does not authorize a runtime hot-path database read.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `AUTHORING_DB_EXPORTER_OK`, `NARR_SOURCE_INVARIANCE_OK`.

**Routing (titles-only).** Exporter/Loader architecture in HDE Architecture; database names in Glow Infrastructure; pack schemas and identity in HDE-Schemas & Artifacts.

## 3.15 Loader — verify, atomic activation, no hot-path DB

**Verify.** Fetch or locate the sealed pack outside the pure composer call. Verify the narrative manifest’s canonical bytes and digest, every governed member’s format/hash/size, required root-manifest inclusion, and binding to the active `release_id` before activation.

**Atomic activation.** Activate the new validated pack through an atomic pointer or equivalent old-or-new transition. Readers must observe either the complete previous validated pack or the complete new validated pack, never a partial mix. On any fetch, parse, canonicalization, manifest, member, identity, or activation failure, fail closed and keep the previous validated pack active.

**Hot path.** Runtime serves narratives from the sealed, immutable file-backed pack view, not the authoring database. The composer and `can_emit` receive that view as pure data.

**Rollback.** Restore or retain the prior validated pack through the manifest or activation pointer; rollback does not reinterpret pack bytes or invent identity.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `LOADER_ATOMIC_SWAP_OK`, `LOADER_VERIFY_IDENTITY_OK`.

**Repository posture.** Checked-in loader code verifies and mounts pack files, but it deletes an existing target before replacement and exposes no complete last-known-good rollback path. Static inspection does not establish this required activation guarantee.

**Routing (titles-only).** Loader architecture in HDE Architecture; pack identity and canonical bytes in HDE-Schemas & Artifacts.

## 3.16 Observability & Privacy — keys-only metrics

**Metrics families (examples).**

* `narr.compose_total`, `narr.compose_suppressed_total`, `narr.compose_latency_ms`.  
  **Labels (bounded).** `category`, `band`, `perspective`, `pack_sha_prefix`, `outcome ∈ {text,suppressed}`. Labels must be from **closed enums**; keep cardinality bounded.

**Identity errors.** If a separate error metric is governed, it may record only bounded field and reason labels; it must not copy raw untrusted identity values or narrative provenance headers.

**Privacy posture.** Keys-only logs; **no narrative text** in logs; no PII; redact secrets; follow the HDE-Governance logging allow-list. No payload echoes in metrics or logs.

**Validation hooks (non-token labels unless admitted by HDE-Governance).** `NARR_METRICS_KEYS_ONLY_OK`, `BG_PRIVACY_REDACTION_OK`.

**Routing (titles-only).** Logging/allow-lists live in HDE-Governance; evidence parity in HDE-Schemas & Artifacts and Epic-Process-Guide.

## 3.17 Rollout Phases & Gates — A→D

**A — Authoring \+ admin preview (DB).** Author in DB; admin preview renders narrative text, while logs, sidecars, and evidence remain ids-only.  
**B — Exporter \+ identity (release).** Export the complete direction-aware candidate grid to `catalog/narratives/*`; validate canonical manifest identity; include every required narrative member in the root freeze manifest; update governed evidence in the same PR.  
**C — Loader \+ sealed files (runtime).** Verify and atomically activate sealed packs on the hot path; preserve the last-known-good pack and rollback path.  
**D — Palette promotion \[Future-Promotion\].** Palette application and palette-selection controls are not part of the current composer contract. Any promotion requires the versioned identity, lint, and surface treatment in §3.11.

**Gates (titles-only).** Evidence follows the complete HDE-Schemas & Artifacts catalog, Human Index, hash sentinel, Machine Mirror, mirror checksum, and path-proof contract. PR workflow lives in Epic-Process-Guide. Acceptance-token claims use only names admitted by HDE-Governance or an applicable active HDE Build Notes addendum.

**Validation hook (non-token label unless admitted by HDE-Governance).** `ROLLOUT_PHASE_TAGS_OK`.

# 4\) Packs, Identity & Provenance (titles-only)

## 4.1 Pack Contents & Manifest Listing (templates, palettes, suppression\_map; sibling .sha256; LF; canonical JSON) \[Canon\]

**Scope.** Define what lives in a narrative pack and how it is listed and proven; exact schemas and bytes live in HDE-Schemas & Artifacts.

**Pack files (canonical JSON; LF-terminated).** Under `catalog/narratives/` maintain these governed members:

* `keys.json` — direction-aware candidate registry with exactly 360 required `{category, band, perspective, slot}` rows: ten categories × four bands × three perspectives × three slots. It is keys-only and contains no prose.  
* `templates.json` — maps each governed template key to one complete paragraph candidate. Numeric slots rank candidates; they are not fragments and are not concatenated.  
* `palettes.json` — required, identity-bound, inert metadata under the current contract.  
* `suppression_map.json` — candidate-level governed blocking data.  
* `manifest.json` — the narrative pack manifest binding every required member by canonical path, hash, and size.

Each current checked-in member and the narrative manifest has a sibling `.sha256` sidecar. Sidecar presence alone does not prove canonical bytes, correct digest, size, manifest completeness, root-manifest inclusion, release coupling, or conformance.

**Direction-aware preservation (MUST).**

* Pack perspectives are exactly `shared`, `a_to_b`, and `b_to_a`. Stored `personal` is retired because it collapses both directional views.  
* Slots are exactly integers `1`, `2`, and `3`, evaluated in that order.  
* Every template is a complete paragraph. Do not reinterpret current paragraphs as `lead`, `bridge`, `close`, `opener`, `center`, `closer`, or `softener`.  
* Export and migration must preserve source ids and copy deliberately; a 240-row collapsed pack does not prove preservation of the required 360-row corpus.

**Identity & manifest coupling (MUST).**

* Define `pack_sha` as the SHA-256 of the exact canonical bytes of `catalog/narratives/manifest.json`, including exactly one final LF.  
* The narrative manifest lists `keys.json`, `palettes.json`, `suppression_map.json`, and `templates.json` exactly once in strict ASCII path order with their exact canonical-byte hashes and sizes.  
* `catalog/manifest.json` lists the narrative manifest and all four required narrative members exactly once before the pack may be claimed as coupled to `release_id`.  
* Any governed byte change to a member or either manifest requires the applicable manifest update and changes the resulting identity. `palettes.json` participates even while palette application is deferred.

**Canonicalization discipline (MUST).** Files are UTF-8 JSON without BOM, compact, ASCII-key-ordered as governed, LF-terminated with exactly one final `\n`, and validated under the canonical JSON and set-order rules in HDE-Schemas & Artifacts. Hash the verified on-disk canonical bytes; do not parse and reserialize to manufacture different hash input.

**Evidence & indices (MUST).**

* Ship governed identity and validation evidence, including sidecars and logs where the owning artifact contract requires them.  
* Update the Human Evidence Index, its hash sentinel, the Machine Evidence Mirror, its required checksum, and every affected path-proof in the same PR as governed evidence changes.  
* Evidence authority comes from the HDE-Schemas & Artifacts catalog and complete ledger bindings; directory placement or sidecar presence alone does not confer authority.  
* Narrative evidence remains keys-only and provenance-only; do not place rendered narrative text in logs or evidence.

**Registered acceptance names (names-only).** `NARR_PACKS_IN_MANIFEST_OK` · `NARR_PACK_SHA_OK` · `NARR_PACKS_CANONICAL_JSON_OK` · `NARR_PACK_MANIFEST_OK` · `NARR_PACK_IDENTITY_OK`.

**Non-token validation labels unless separately admitted.** `NARR_KEYS_OK` · `NARR_TEMPLATES_OK`.

**Routing (titles-only).**

* HDE-Schemas & Artifacts: pack schema, manifest, canonical JSON, release identity, and evidence catalog.  
* HDE-CLI-API-Vendor-Ref: public/CLI payload bytes and routes.  
* HDE-Governance: transport policy and acceptance-token registry.  
* HDE-Mechanics Guide: loader, exporter, validators, evidence generators, and tests.

---

## 4.2 `pack_sha` & `release_id` Linkage (freeze coupling; echo in valid responses/sidecars) \[Canon\]

**Identity (`pack_sha`).** `pack_sha = sha256(exact canonical bytes of catalog/narratives/manifest.json)`. The controlling bytes include exactly one final LF. The manifest is the single pack-identity input.

**Freeze coupling (`release_id`).** The root freeze manifest must include the narrative manifest and all four required members. `release_id` is the lowercase 64-hex SHA-256 of the verified canonical bytes of `catalog/manifest.json`. A pack present in the repository but absent from that root manifest is not coupled to its release.

**Pre-composition binding.** Before routing or suppression, validate:

1. presence and non-blank form of both identities;  
2. exact lowercase 64-hex syntax;  
3. `pack_sha` equality with the validated narrative-manifest digest;  
4. root-manifest inclusion of all required narrative members; and  
5. `release_id` equality with the active validated freeze identity binding that pack.

Format validity alone is insufficient. A syntactically valid but wrong digest is an identity failure.

**Echo for provenance.** Valid Text and Suppressed composer results echo `pack_sha` and `composition_id`; CLI/admin sidecars may carry the same ids. Invalid identity returns `ERR_NARRATIVE_IDENTITY_INVALID` before the response union and emits no narrative body, `pack_sha`, `composition_id`, `fragment_ids`, `X-Narrative-Pack-Sha`, or `X-Narrative-Composition`.

**No placeholder release identity.** CLI, QA, and admin preview must use a validated `release_id` bound to the pack. An all-zero or other local placeholder is not a valid substitute and must not be recast as a Suppressed result. The authoritative runtime release identity derives from the packaged canonical root manifest; `/internal/version` is an ops inspection surface, not an alternate identity input.

**Evidence parity (names-only).** Governed identities and acceptance records follow the complete HDE-Schemas & Artifacts Human Index, hash sentinel, Machine Mirror, mirror checksum, and path-proof contract.

**Runtime (titles-only).** Sealed narrative packs are served from `/narratives/<pack_sha>/<PACK_MEMBER>`. Runtime loading and atomic activation are owned by HDE Architecture and HDE-Mechanics Guide; pack and release identity are owned by HDE-Schemas & Artifacts.

**Repository posture.** At the pinned commit, `catalog/manifest.json` omits the narrative manifest and all four required narrative members, while the loader derives a digest from reserialized manifest JSON without the governed final LF. The checked-in state therefore does not establish this required coupling or identity recipe.

**Routing (titles-only).**

* HDE-Schemas & Artifacts: pack and root manifest schemas, exact canonical bytes, and release identity.  
* HDE-CLI-API-Vendor-Ref: response, error, and sidecar byte contracts.  
* HDE-Governance: transport and typed-error policy.  
* HDE-Math-Spec: project-wide `release_id` definition.

---

## 4.3 Evidence Index (machine JSONL \+ human index) — same-PR parity requirement \[Canon\]

**Dual index (MUST).**

* **Machine mirror:** `artifacts/evidence_index.jsonl` — governed records-only JSONL. It is canonical, rejects unknown keys, uses strict field and record ordering, has exactly one final LF, maintains parity with the Human Index, and has its governed checksum and path-proof companions as required by HDE-Schemas & Artifacts.  
* **Human index:** `docs/evidence/INDEX.json` — records-only pointer and metadata ledger for governed artifacts, updated in the same PR as the Machine Mirror and guarded by `docs/evidence/INDEX.sha256`.

**Record contract (route by title).** HDE-Schemas & Artifacts owns the exact required and optional field set, ordering, self-record, timestamp, parity, checksum, and path-proof rules. PF17 does not maintain a competing schema. Narrative evidence records preserve the exact artifact key/path binding and every required hash, size, role, time, and proof anchor.

**Narrative evidence scope.**

* Narrative pack members and identities are frozen inputs. When promoted or cataloged as governed evidence, their evidence records and companions follow the owning catalog.  
* Registry-diff, router, pack-identity, source-invariance, loader, composer, parity, and validation evidence is indexed only when its owning artifact family catalogs it.  
* Examples and acceptance outputs remain keys-only and provenance-only; narrative text is not copied into logs or evidence merely to prove conformance.

**Evidence discipline (MUST).**

* **Canonicalization:** governed JSON and JSONL use the exact canonical-byte rules in HDE-Schemas & Artifacts.  
* **Keys-only logs:** logs and sidecars may include ids such as `pack_sha`, `composition_id`, and `release_id`, but no narrative text, PII, secrets, or raw untrusted identity values.  
* **Provenance echo:** only valid Text and Suppressed results echo composer provenance. Identity errors do not.  
* **Complete companions:** update the Human Index, Human Index hash sentinel, Machine Mirror, required Mirror checksum, and every affected path-proof in the same governed change.

**Registered acceptance names (names-only).** `EVIDENCE_INDEX_UPDATED_OK` · `EVIDENCE_INDEX_MIRROR_OK` · `EVIDENCE_INDEX_HASH_OK` · `MACHINE_MIRROR_UPDATED_OK` · `EVIDENCE_PATHS_VALIDATED_OK`.

**Non-token validation labels unless separately admitted.** `EVIDENCE_INDEX_CANONICAL_JSON_OK` · `EVIDENCE_INDEX_ONE_LF_OK`.

**Routing (titles-only).**

* HDE-Schemas & Artifacts: Evidence Catalog, Human Index, Machine Mirror, canonicalization, checksums, and path proofs.  
* Applicable HDE-Build Checklist phase: ship/no-ship task status and gate wiring.  
* Epic-Process-Guide: PR-first and same-PR process discipline.

---

## 4.4 Narratives Router Coverage and Evidence \[Canon\]

**Required current coverage.** Router and registry validation must cover the complete direction-aware candidate grid:

```
10 categories x 4 bands x 3 perspectives x 3 slots = 360 candidate rows
```

The coverage proof is keys-only and no-prose. It verifies:

* the closed ten-category roster and four canonical bands;  
* perspectives `shared`, `a_to_b`, and `b_to_a`;  
* slots `1`, `2`, and `3` for every supported group;  
* unique tuples and unique keys where required;  
* complete-paragraph template presence and pack-time validation state;  
* key-level suppression eligibility; and  
* `missing_narrative_key` for a valid-identity no-candidate result, without fallback prose.

For each viewer, the derived ten-by-two result contains one shared key and that viewer’s directional private key per category.

**Parity semantics.**

* Shared coverage and selection are symmetric under governed AB-to-BA normalization; disagreement fails closed for both viewers.  
* Directional coverage is swap-covariant: swapping A and B maps `a_to_b` to `b_to_a`. It does not require the two directions to be equal.  
* CLI/HTTP parity applies only where the compared surfaces own the same response contract.

**Historical HDE-EPIC032 evidence record.** The checked-in HDE-EPIC032 PR-01 artifacts remain historical evidence and are not rewritten:

* `audit/gates/narratives/keys_10x4.table.json` — historical 10-by-4 router coverage artifact. Its path and name do not prove the current 360-row direction-aware candidate contract.  
* `artifacts/narratives/router/parity_abba.log` — historical AB↔BA and two-run router log.  
* `artifacts/narratives/router/cli_http_parity.log` — historical CLI/HTTP router compare where parity was defined.

Those artifact bytes may support only the exact facts they record. They do not prove current 360-row registry closure, current runtime conformance, test passage, deployment, QA PASS, or acceptance.

**Acceptance posture (names-only).**

* `JSON_CANONICAL_CHECK_OK`, `CLI_READER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`, and `COMPOSITE_ABBA_IDENTITY_OK` may be claimed only where the governed evidence directly proves their registered semantics.  
* `NARR_REGISTRY_CLOSURE_OK` is not registered in the current HDE-Governance token roster and must not be claimed as an acceptance token. It may remain a non-token candidate label only until an owning source admits it.  
* Index, mirror, checksum, and path-proof tokens remain governed by their owning documents.

**Routing (titles-only).** Evidence cataloging and path-proof details live in HDE-Schemas & Artifacts; mechanics live in HDE-Mechanics Guide; task status lives in the applicable HDE-Build Checklist phase; token admission and semantics live in HDE-Governance.

## 4.5 Narrative Registry Diff and Pack Identity Evidence \[Canon\]

**Purpose.** Narrative registry diff and pack identity evidence prove that a narrative pack change is keys-only, deterministic, manifest-bound, direction-aware, and indexable without exposing narrative prose or inventing acceptance tokens. Generator implementation, pipeline mechanics, evidence schemas, and build-checklist task status live in their owning documents by title.

**Registry diff artifact (titles-only).**

* `audit/gates/narratives/registry.diff.json` is the historical canonical path used for keys-only registry diff evidence.  
* The artifact must remain no-prose: it may describe category, band, perspective, slot, key, manifest identity, and diff status, but must not embed rendered narrative text.  
* Current direction-aware evidence must distinguish `shared`, `a_to_b`, and `b_to_a`; it must not represent both directional views as stored `personal`.  
* If no prior baseline exists, the artifact may truthfully record a current-manifest-verified posture, but it must still fail closed on malformed, unsupported, duplicate, or incomplete state.

**Pack identity artifact (titles-only).**

* `audit/gates/narratives/pack_identity.txt` is the historical path for narrative pack identity evidence.  
* Pack identity evidence must bind `pack_sha` to the SHA-256 of the exact canonical narrative-manifest bytes, including the final LF, and record enough non-secret identity material to verify path, size, and two-run stability.  
* A complete current release-coupling proof also verifies root-manifest inclusion of the narrative manifest and all four required members and recomputes the bound `release_id`.  
* Identity evidence remains keys-only and provenance-only; it contains no narrative prose.

**Validation posture.** Registry diff evidence is valid only when validation fails closed for:

* missing or unexpected narrative-manifest paths;  
* unsupported category values;  
* unsupported band values;  
* unsupported perspective values, including collapsed stored `personal`;  
* unsupported slot values;  
* duplicate category-band-perspective-slot tuples;  
* duplicate keys where uniqueness is required;  
* missing supported category-band-perspective-slot tuples;  
* partial slot sets for supported groups;  
* missing or invalid complete-paragraph template bindings; and  
* pack identity or root-manifest release-coupling mismatch.

Missing, unsupported, duplicate, partial, or identity-invalid state must not be normalized into fallback prose. Invalid identity follows the pre-composition error boundary; a valid-identity no-candidate result uses `missing_narrative_key` and suppression.

**Historical Doc-Delta record.** The HDE-EPIC032 PR-02 artifact `audit/docdeltas/hde-epic032_doc_deltas.md` remains historical. Its presence does not make current candidate coverage, release coupling, implementation, QA, or acceptance conformant.

**Evidence binding.** Registry diff, pack identity, and any applicable Doc-Delta posture artifacts follow the complete governed evidence discipline in HDE-Schemas & Artifacts: Human Index, hash sentinel, Machine Mirror, required Mirror checksum, path-proof binding, and exact final-LF/canonical JSON checks where applicable.

**Pipeline ordering (titles-only).** For a PR that claims current registry-diff or pack-identity evidence, generation and validation of the source evidence must precede evidence-index update and validation. PF17 records this dependency only; the concrete pipeline, tests, and task status live in HDE-Mechanics Guide, HDE-Schemas & Artifacts, and the applicable HDE-Build Checklist phase.

**Acceptance posture (names-only).**

* Registry diff canonical JSON may support `JSON_CANONICAL_CHECK_OK` only when the governed bytes prove it.  
* Pack identity two-run stability may support `TWO_RUN_IDENTITY_OK` only when both runs bind the same exact manifest bytes.  
* A required Doc-Delta posture may support `DOC_DELTA_PRESENT_OK` only under its registered semantics.  
* `NARR_REGISTRY_CLOSURE_OK` remains a non-token label unless admitted by HDE-Governance or an applicable active HDE Build Notes addendum.

**Routing (titles-only).**

* HDE-Schemas & Artifacts owns schemas, canonical JSON, manifest listing, release identity, Evidence Catalog, Human Index, Machine Mirror, hash sentinels, and path-proof rules.  
* HDE-Mechanics Guide owns generator, validator, loader, and pipeline mechanics.  
* The applicable HDE-Build Checklist phase owns task status and gate wiring.  
* HDE-Governance owns token admission and token semantics.  
* Epic-Process-Guide owns same-PR evidence and Doc-Delta process discipline.

# **5\) Surfaces (titles-only)**

## **5.1 Reader v1 Posture — bands-only; narrative-free**

**Posture (unchanged).**  
 Reader v1 public JSON remains numeric-free (bands-only) and contains no narrative text. Narrative text appears only on the Aux narrative surface and in admin CLI preview.

This guide does not restate payload shapes or header matrices; it links by title only. Payload bytes live in **PF05 — CLI/API**; transport/A7 policy lives in **PF04 — Governance**; the bands-only Reader covenant is defined in **PF01 — Math Spec**.

**Implications.**  
 Reader v1 keeps its existing public contract (six-key, numeric-free success body). Any narrative-related exposure continues to route through Aux/CLI, not Reader v1.

**A7 proof surface (route-only).**  
 When Reader success routes are proven, proofs run only on a cataloged JSON success route (Endpoint Catalog, PF05). The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof. `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* PF05 — CLI/API: declare Reader v1 narrative-free and define Aux/CLI behaviors.

* PF04 — Governance: A7 (ETag/HEAD/304; writers/errors; ops exclusion).

* PF01 — Math Spec: bands-only Reader covenant.

---

## **5.2 Aux Narrative (text/plain) — 200 ok text; 200 suppressed empty body (no ETag) \[Canon\]**

**Route (titles-only).**  
 The Aux narrative endpoint and payload bytes are defined in **PF05 — CLI/API & Vendor Ref**. PF17 does not restate endpoint bytes.

**Bodies (posture).**

* **200 ok (text shown).** Narrative text is emitted when policy allows. Transport bytes live in PF05/PF04; PF17 stays contract-free.

* **200 suppressed (text withheld).** **Empty body, no `ETag`**, and **`Vary: Authorization, Accept-Encoding` present**. A policy header such as `X-Narrative-Policy: suppressed` **may** be present. *(Bytes in PF05; policy in PF04.)*

**A7 proof surface (route-only).**

* Catalog-only. Aux success proofs run only on a cataloged JSON success route (Endpoint Catalog in PF05).

* The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof.

* `/internal/version` is ops-only and not A7-eligible.

* **Aux HEAD and 304 are explicitly out of scope for EPIC-010; A7 proofs remain Catalog JSON-success only.**

**Invariants (bytes/tests live in PF04/PF05/PF14).**  
 On the cataloged route, proofs satisfy:

* Strong quoted ETag on 200 (identity over LF-terminated body; pre-compression).

* HEAD 200 validator parity (Content-Type \== GET; no body; Content-Length \== len(identity 200 body)).

* 304 after prior 200, omitting both Content-Type and Content-Length, validators mirror cached GET.

* `Vary: Authorization, Accept-Encoding` present.

* Encoding-invariance of identity (ETag) and effective Content-Length across accepted encodings.

**Reader posture (for clarity).**  
 Reader v1 remains bands-only and narrative-free; Aux/CLI are the narrative surfaces. (Routing: PF01/PF05.)

**Acceptance (names-only; enforcement lives in PF04/PF09/PF14).**

NARR\_200\_TEXT\_OK · NARR\_SUPPRESSED\_NO\_ETAG\_OK · A7\_GET\_QUOTED\_ETAG\_OK · A7\_HEAD\_PARITY\_OK · A7\_304\_OMITS\_CT\_CL\_OK · A7\_VARY\_AUTH\_AE\_OK · A7\_ENCODING\_INVARIANCE\_OK · ENDPOINTS\_CATALOG\_INTERNAL\_OK · A7\_TRANSPORT\_PROOF\_OK · **NARR\_VARY\_AUTH\_AE\_OK** · **AUX\_CANON\_ALIAS\_PARITY\_OK**

**Routing (titles-only).**

* PF05 — CLI/API: endpoint, payload bytes, stdout/sidecar guarantees, Endpoint Catalog.

* PF04 — Governance: A7 transport (ETag/HEAD/304; writers/errors). PF04 pins “200 suppressed \= empty body, no ETag.”

* PF12 — Schemas & Artifacts: composite success-proof JSON schema and evidence conventions (titles only).

* PF01 — Math Spec: bands-only Reader covenant (numeric-free).

**Evidence scope (EPIC-010).**  
 Aux evidence captures exactly **two** header snapshots: `aux_text_200.snap` and `aux_suppression_200.snap`; Aux HEAD/304 captures are out of scope (A7 is Catalog-only).

---

## **5.3 CLI Admin Preview — admin-only; stdout equals emitter; sidecar ids-only \[Canon\]**

**Behavior (posture).**

* **Exact bytes parity.** CLI preview must emit exactly the bytes the single Presenter/emitter produces for the same inputs; stdout is LF-terminated (no `\r`). This preserves single-emitter parity across HTTP and CLI.

* **Flags (titles-only).** Use a preview flag such as `--show-narrative` and an output option such as `--admin-out <path>` for sidecars. Names, shapes, and stdout/sidecar guarantees are defined in PF05 — CLI/API (not restated here).

* **Admin-only.** Access to narrative preview is restricted to authorized/admin contexts; public Reader v1 remains narrative-free. **Preview is enabled by default for admins across dev/stage/prod and uses the same emitter as Aux (bytes parity, LF-terminated).**

* **Suppression parity.** When the composer returns suppressed, the CLI preview mirrors suppression (no narrative text). Transport details remain governed in PF04/PF05.

**Sidecar (evidence).**

* **Ids-only, no prose.** Sidecar includes ids only: `composition_id`, `fragment_ids[]`, `pack_sha`, and (when available) `release_id`, to enable audit traceability without exposing text to logs.

**Same-PR indices and mirror hygiene.**

* Append a compact JSON object to the machine Evidence Index (`artifacts/evidence_index.jsonl`) in the same PR as the human Evidence Index update (`docs/evidence/INDEX.json`).

* The machine mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, one trailing LF), rejects unknown keys, and each record includes a `proof_anchor` to a path-proof stored alongside the artifact.

* Maintain LF discipline in all artifacts (no `\r`).

**Example (EPIC017 Aux admin preview, QA07 — informative).**  
 In EPIC017 QA, `hdctl aux-preview --admin-out` was run for a synthetic birth pair using the same compat JSON as Aux. The admin sidecar was a single JSON object containing:

* `composition_id` and `key` with a naming pattern of `category.band.perspective.slot` (for example, `heat.open.shared.1` for the Heat / Open / shared case and first slot in the pack).

* `pack_sha` as a 64-character lowercase hex digest that identifies the pinned narratives pack.

* `pair` with `a_person_uid` and `b_person_uid` values matching the `a.person_uid` and `b.person_uid` fields in the compat JSON for the same CLI-scoped people.

* `release_id` as a 64-character lowercase hex value that was all zeros in this CLI-only QA preview, reflecting a local preview identity rather than a specific production Engine release.

This example confirms that the Aux admin preview:

* selects a composition based on `{category, band, perspective, slot}` consistent with the pack and compat outcome,

* carries `pack_sha` so QA and ops can trace the narrative back to a specific narratives pack version, and

* ties the preview to the same CLI-scoped pair ids used by compat, with `release_id` allowed to be a non-prod value (such as all zeros) in CLI/QA, while `pack_sha` remains the primary identity for the narratives pack and the authoritative Engine identity stays `/internal/version` (PF05/PF04).

This subsection remains **informative**; byte contracts and schemas for the sidecar continue to live in PF05/PF12.

**Routing (titles-only).**

* PF05 — CLI/API: flag names, stdout/sidecar contracts, and any endpoint coupling.

* PF04 — Governance: A7 transport behavior mirrored in CLI proofs (e.g., HEAD/304 parity where applicable).

* PF12 — Schemas & Artifacts: Evidence Index JSONL conventions and canonicalization rules.

* PF06 — Epic-Process-Guide: PR-first; Doc-Delta \+ indices in the same PR.

**Acceptance (names-only; enforcement in PF14/PF09).**

CLI\_PREVIEW\_BYTES\_EQ\_EMITTER\_OK · CLI\_PREVIEW\_SUPPRESSION\_PARITY\_OK · CLI\_SIDECAR\_IDS\_ONLY\_OK · EVIDENCE\_INDEX\_UPDATED\_OK · MIRROR\_CANONICAL\_JSONL\_OK · MIRROR\_UNKNOWN\_KEYS\_REJECTED\_OK · LF\_NORMALIZATION\_OK · **CLI\_PREVIEW\_ENABLED\_OK** · **CLI\_PREVIEW\_INDEXED\_OK**

---

# **6\) Tests & Acceptance (names-only; enforcement in PF14/PF09/PF04)**

## **6.1 Determinism — NARR\_DETERMINISM\_OK · NARR\_AB\_BA\_COHERENCE\_OK · NARR\_LF\_NORMALIZATION\_OK \[Canon\]**

**Status.** Canon. This subsection lists determinism acceptance **names**; unit/property tests live in **PF14 — Mechanics**, and ship/no-ship gates live in **PF09 — Build Checklist** (titles-only).

**Markers (names-only).**

* **NARR\_DETERMINISM\_OK** — same validated inputs ⇒ byte-for-byte identical output.  
* **NARR\_AB\_BA\_COHERENCE\_OK** — perspectives coherent where symmetric (AB↔BA).  
* **NARR\_LF\_NORMALIZATION\_OK** — normalized line discipline (LF-only; no `\r`).

**Enforcement homes (titles-only).**

* **PF14 — Mechanics:** two-run identity, AB↔BA coherence, LF normalization tests.  
* **PF09 — Build Checklist:** determinism tokens are **blocking** gates for narratives.

**Notes.**

* PF17 lists **names only** to avoid duplicating test logic or payload bytes; payload/transport rules remain in **PF05/PF04**.  
  ---

  ## **6.2 Lints & Safety — NARR\_LEN\_≤300\_OK · NARR\_NO\_EM\_DASH\_OK · NARR\_BANNED\_TOKENS\_OK · NARR\_JARGON\_FREE\_OK \[Canon\]**

**Status.** Canon. This subsection lists lint/safety **names**; tests live in **PF14** and gates live in **PF09** (titles-only).

**Markers (names-only).**

* **NARR\_LEN\_≤300\_OK** — narrative text ≤ **300 UTF-8 chars** and within the spec’s length cap.  
* **NARR\_NO\_EM\_DASH\_OK** — no em-dash (—) characters present.  
* **NARR\_BANNED\_TOKENS\_OK** — text contains none of the banned tokens/phrases (thresholds live in **PF15**).  
* **NARR\_JARGON\_FREE\_OK** — text avoids HD/internal jargon in public copy per tone guide (thresholds live in **PF15**).

**Enforcement homes (titles-only).**

* **PF14 — Mechanics:** implement lint checks/fixtures for length, em-dash rejection, banned-tokens, jargon filters.  
* **PF09 — Build Checklist:** make these markers **blocking** in the narratives gate set.  
* **PF15 — Copy Tonality Guide:** single home for editorial thresholds (banned terms, tone).

**Notes.**

* Keep this section **names-only**; payload and transport remain in **PF05/PF04**.  
  ---

  ## **6.3 Transport Proofs (A7) — NARR\_200\_TEXT\_OK · NARR\_SUPPRESSED\_NO\_ETAG\_OK · A7\_HEAD\_PARITY\_OK · A7\_304\_OMITS\_CT\_CL\_OK · A7\_VARY\_AUTH\_AE\_OK · A7\_ENCODING\_INVARIANCE\_OK · A7\_429\_HEADERS\_OK · A7\_RETRY\_AFTER\_BOTH\_OK \[Canon\]**

**Status.** Canon. These are Aux transport acceptance **names**; authoritative A7 rules live in **PF04 — Governance**, endpoint bytes live in **PF05**, tests in **PF14**, and gates in **PF09** (titles-only). *Supersession:* a higher-numbered PF10 addendum governs only overlapping scope or scope it explicitly supersedes; unrelated lower-numbered addenda and distinct, non-superseded scope remain authoritative.

**Markers (names-only).**

* **NARR\_200\_TEXT\_OK** — 200 **text emitted** (Aux), success posture satisfied (bytes in PF05).  
* **NARR\_SUPPRESSED\_NO\_ETAG\_OK** — **200 suppressed**: **empty body, no ETag** (policy header optional; pinned in PF04).  
* **A7\_HEAD\_PARITY\_OK** — HEAD 200 mirrors GET validators; `Content-Type == GET`; no body; `Content-Length == len(identity 200 body)`.  
* **A7\_304\_OMITS\_CT\_CL\_OK** — conditional GET returns **304** only after prior 200, **no body**, **omit both `Content-Type` and `Content-Length`**; validators mirror cached GET.  
* **A7\_VARY\_AUTH\_AE\_OK** — `Vary: Authorization, Accept-Encoding` present.  
* **A7\_ENCODING\_INVARIANCE\_OK** — identity (**ETag**) and **effective `Content-Length`** are stable across accepted encodings (identity/gzip/br).  
* **A7\_429\_HEADERS\_OK** — rate-limit headers present/valid.  
* **A7\_RETRY\_AFTER\_BOTH\_OK** — `Retry-After` accepted in seconds **or** HTTP-date.

**Notes.**

* **Proof surface:** success proofs run **only on a cataloged JSON success** route (Endpoint Catalog, PF05). The Catalog is **internal-only** and **env-gated**; **non-prod entries must be unreachable in prod** — capture a headers-only **env-gate proof**. `/internal/version` is **ops-only** and not A7-eligible.  
* Bytes, header matrices, and examples are owned by **PF04/PF05**; PF17 lists **names only**.

**Enforcement homes (titles-only).**

* **PF14 — Mechanics:** implement A7 probes for Aux (GET/HEAD/304/429).  
* **PF09 — Build Checklist:** block on missing/failed A7 markers.  
* **PF04 — Governance:** authoritative A7 rules (ETag/HEAD/304/rate-limits/writers+errors).  
  ---

  ## **6.4 Provenance — NARR\_PACK\_SHA\_OK (echo & match) \[Canon\]**

**Status.** Canon. This lists the provenance **name** proving narrative outputs are traceable to a governed pack; tests live in **PF14**, gates in **PF09** (titles-only).

**Marker (names-only).**

* **NARR\_PACK\_SHA\_OK** — composer echoes the active `pack_sha` (Text and Suppressed) and it **matches** the pack identity derived from the **canonical pack manifest** that is **manifest-listed** for the same `release_id`.

**What we verify (conceptual).**

1. **Echo.** Responses include `pack_sha` alongside `composition_id` (both paths).  
2. **Match.** The echoed `pack_sha` equals the SHA derived from the **canonical manifest** for the same `release_id`.  
3. **Validity.** Ids are lowercase **64-hex**; non-conforming requests fail closed (suppressed/conflict).

**Evidence posture.**

* Sidecars/artifacts may include **ids only** (`pack_sha`, `composition_id`, optional `release_id`) for audit; update the **human Evidence Index** and append to the **machine JSONL mirror** **in the same PR**. The machine mirror is **records-only**, **canonical JSONL** (UTF-8, sorted keys, compact, **one LF**), **rejects unknown keys**, and each record includes a **`proof_anchor`** to a path-proof file stored alongside the artifact.

**Routing (titles-only).**

* **PF12 — Schemas & Artifacts:** pack schema/manifest and identity rules (canonical JSON, manifest listing).  
* **PF05 — CLI/API:** response/sidecar byte contracts (ids in outputs).  
* **PF14 / PF09:** tests and blocking gates for **NARR\_PACK\_SHA\_OK**.  
  ---

# 7\) Variety Without Randomness (titles-only; \[Speculative\]) — 

### **7.1 Variety objectives — no randomness**

**Goal.** Provide bounded micro-variety across repeated views **without** randomness or time dependence.

**Constraints.**

* Variety **never** alters acceptance outcomes or lints (text stays ≤300, 2–4 sentences, numeric-free).

* Variety **never** changes `pack_sha`, `composition_id`, or `fragment_ids` ordering rules.

* No external I/O; deterministic per `{category, band, perspective, pack_sha, release_id}`.

**Acceptance (names-only).** `VARIETY_OBJECTIVES_OK`  
 **Routing (titles-only).** Concrete mechanics pinned in **PF14**; any flags live in **PF05/PF04**.

### **7.2 Prime-Step Traversal (deterministic index) \[Speculative\]**

**Status.** Speculative. Deterministic traversal of eligible fragments; exact seeds/steps/windows are pinned in **PF14**.

**Intent.** Preserve strict determinism while allowing light variety across repeated views by walking the candidate set with a fixed prime step. No RNG, no timers, no external I/O.

**Definitions.**

* Let eligible fragments (post keys/guards/lints) form an ordered list **F** of length **N**.

* Choose a **prime step** `p` with `gcd(p, N) = 1`.

* Compute a deterministic **start index** `s` from a stable seed derived only from validated inputs/identities (e.g., hash of `{category, band, perspective, pack_sha, release_id}`), then `s = seed mod N`. *(Seed formula pinned in PF14.)*

**Traversal (normative on adoption).**

1. Initialize `i ← s`.

2. Test `F[i]` against all hard lints and coherence guards; also check **Cooling Window K** (if configured).

3. If `F[i]` passes, **select** it; else advance deterministically `i ← (i + p) mod N` and repeat **≤ N** probes.

4. If no candidate passes within **N** probes, **suppress** (conflict); **never** relax rules for variety.

**Determinism & identity.**

* For fixed inputs, `(N, p, s)` are fixed; the same traversal yields the same choice (**two-run identity**).

* `composition_id` **MUST** be derived deterministically from `{chosen_fragment_id, inputs, pack_sha}` (recipe pinned in PF14) so audits can reproduce selection.

**AB↔BA coherence.**  
 Seeds must be chosen so `A→B` and `B→A` outcomes are coherent by construction (either the same shared fragment or the correct directional pair).

**Open pins (PF14 to resolve).**  
 Seed recipe; allowed prime set/chooser; termination bound (≤ N); interaction with **K** and **R** (rings).

**Acceptance (names-only).** `VARIETY_PRIME_STEP_OK`, `PRIME_STEP_TRAVERSAL_OK`, `PRIME_STEP_TERMINATES_OK`, `PRIME_STEP_AB_BA_COHERENCE_OK`  
 **Routing (titles-only).** Any pack metadata for prime step lives in **PF12**.

### **7.3 Cooling Window K (release-scoped)**

Deterministic “recently-used” guard; values/plumbing pinned in **PF14**.

**Intent.** Avoid immediate repetition without randomness while preserving two-run identity and AB↔BA coherence.

**Definition.**

* `K` \= small integer count of recent `composition_id`s to avoid when selecting a new fragment.

* **Scope** \= release-scoped; the window resets when `release_id` changes. *(PF14 pins per-dyad vs per-dyad+perspective.)*

**Deterministic behavior.**

1. Build eligible set (post filters/lints/guards).

2. Apply **Prime-Step Traversal** (§7.2).

3. If the candidate’s `composition_id` is in **K**, advance one prime step and test next; repeat until found or **≤ N** probes.

4. If all candidates are blocked by lints/guards/window, **suppress** (conflict). No relaxation.

**State & plumbing (OPEN).**  
 Where state lives (caller-provided recent IDs vs deterministic ephemeral cache keyed by `{dyad, perspective, release_id}`), value of **K** (e.g., 2–4), and termination policy (≤ N probes).

**Determinism & parity.**  
 Including `release_id` guarantees repeatable resets; AB↔BA coherence must hold for whichever scope PF14 pins.

**Acceptance (names-only).** `VARIETY_COOLING_WINDOW_OK`, `COOLING_WINDOW_APPLIED_OK`, `COOLING_WINDOW_RELEASE_SCOPED_OK`, `COOLING_WINDOW_TERMINATES_OK`, `COOLING_WINDOW_AB_BA_COHERENCE_OK`  
 **Routing (titles-only).** **PF14** pins K/scope/state; **PF12** defines pack bytes if window metadata is stored (none by default).

### **7.4 Variety Rings R (optional grouping)** 

Curated alternates for common scenarios allowing light variation without randomness.

**Intent (deterministic variety).** Provide 4–6 pre-approved alternates for a `{category, band, narrative_kind, perspective}` case. Selection uses a stable **bucket** derived only from validated inputs/identities (e.g., `{category, band, families_fired, perspective, pack_sha, release_id}`), never RNG/time/I/O.

**Model (concept).**

* **Ring R**: ordered list of curated fragment IDs `(r0…rR−1)` defined in the pack for a case; ring contents are manifest-listed and SHA-pinned.

* **Bucket**: compute `b = f(inputs, identities) mod R`, where `f` is a deterministic hash (pinned in PF14). Candidate \= `r_b` **before** guards.

**Selection order (with other tools).**

1. Build eligible set (post filters/lints/guards).

2. If a ring exists, attempt `r_b` first; if it fails, advance deterministically using **Prime-Step Traversal** (§7.2).

3. Apply **Cooling Window K** (§7.3) if configured; if a candidate is in **K**, skip deterministically.

4. If all ring/prime-step candidates fail guards or K, **suppress** (no relaxation).

**Determinism & parity.**  
 Same validated inputs (incl. `pack_sha`, `release_id`) ⇒ same bucket and same outcome (text or suppression). Two-run identity holds. For symmetric perspectives, rings must preserve AB↔BA coherence (PF14 property tests).

**Open pins (PF14/PF12).**  
 Ring size **R** (e.g., 4–6) and pack schema field for rings (PF12); exact bucket function and interactions with prime-step/K; termination bound (≤ N).

**Acceptance (names-only).** `VARIETY_RINGS_OK`, `VARIETY_RING_BUCKET_OK`, `VARIETY_RING_REPLAY_OK`, `VARIETY_RING_TERMINATES_OK`, `VARIETY_RING_AB_BA_COHERENCE_OK`  
 **Routing (titles-only).** Bucket math & tests in **PF14**; any ring fields live in **PF12**.

### **7.5 OPEN Pins (K/R values, buckets, collision policy) \[Speculative\]**

Items that **MUST** be pinned in **PF14 — Mechanics** (and **PF12** if pack bytes are required) before implementation.

**To decide (and where to pin).**

* **K — Cooling window** size & scope; state location; termination policy (≤ N).

* **R — Ring size/placement** and the pack schema field where curated ring members live; rings manifest-listed and SHA-pinned (PF12).

* **Bucket function (rings)**: deterministic `b = f(inputs, identities) mod R`; exact inputs and hash choice.

* **Seed function (prime-step)**: exact seed recipe `s = seed mod N` and prime chooser with `gcd(p, N) = 1`.

* **Collision/termination policy**: max deterministic advances when guards/K/R exclude candidates; guarantee termination ≤ N probes; otherwise suppress.

* **AB↔BA coherence constraints**: how seeds/buckets/scopes ensure symmetric perspectives remain coherent; property tests.

* **Evidence & acceptance**: register acceptance names in PF14/PF09; add **same-PR** index entries for any new artifacts (human \+ machine mirror with canonical JSONL, unknown-key rejection, `proof_anchor`).

**Routing (titles-only).** **PF14** pins formulas, state, tests; **PF12** defines any ring/metadata fields and keeps manifest/identity rules.

---

## **8\) Security, Privacy & Ops (titles-only; \[Canon\])**

### **8.1 Access control & privacy — admin-only preview; no PII in artifacts \[Canon\]**

**Admin scope.** Narrative preview is **restricted to authorized/admin** contexts; public **Reader v1 remains narrative-free** (bands-only). Preview endpoints **must not** appear on public Reader surfaces.  
 **Ids-only artifacts.** Never include rendered narrative **text** or **PII** in logs, sidecars, evidence, or acceptance outputs. Preview artifacts **MUST** contain **ids only** (e.g., `composition_id`, `fragment_ids[]`, `pack_sha`, optional `release_id`) for audit traceability — **no user data**.  
 **Suppression parity.** If composition yields **suppressed**, **CLI preview mirrors suppression** (no text body). Aux/HTTP transport posture (200 empty, no ETag when suppressed) is governed in PF04/PF05.  
 **Acceptance (names-only).** `ADMIN_PREVIEW_GUARD_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`.

### **8.2 Logging posture — keys/ids only; include `correlation_id`, `release_id`, `pack_sha` \[Canon\]**

**Keys/ids only (MUST).** Logs and sidecars **MUST NOT** include rendered narrative text. Record **identifiers only**, e.g.:

* `policy_reason`, `composition_id`, `fragment_ids[]`, `pack_sha`, `release_id`, `correlation_id`.  
   **Line discipline.** All emitted text and logs are **LF-only**; narrative text **MUST NOT** contain `\r`. **No ANSI**, no trailing spaces.  
   **Evidence parity.** When logs/sidecars reflect emitted artifacts, update the **human index \+ hash sentinel \+ machine mirror in the same PR** (see §8.3).  
   **Routing (titles-only).** PF12 — Evidence Index/mirror conventions; PF04 — A7 transport & refusal/logging posture; PF05 — sidecar byte contracts and preview flows; PF15 — editorial safety/banned tokens (names-only).  
* **Acceptance (names‑only)**. \`OBS\_KEYS\_ONLY\_OK\`.

  ### **8.3 Ops & Evidence discipline — governed paths & mirror hygiene \[Canon\]**

**Governed locations only.** Evidence **must** live under `artifacts/**` or `docs/**`; **no** transient/generator paths.  
LC/TZ pins. All canonicalization and comparison steps must run with the environment set to **LC\_ALL=C, LANG=C, TZ=UTC**.

 **Same-PR parity (human ↔ machine).** When preview artifacts are written, update **in the same PR**:

* **Human** Evidence Index: `docs/evidence/INDEX.json`

* **Hash sentinel**: `docs/evidence/INDEX.sha256` (merge-gating; matches INDEX bytes)

* **Machine mirror**: `artifacts/evidence_index.jsonl`  
   **Mirror hygiene (records-only JSONL).** UTF-8, sorted keys, compact, **exactly one LF**; **unknown-keys rejected**; **ASCII field order**; **sort-before-write**; **single mirror file**. Each record includes `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a **`proof_anchor`** to a co-located path-proof.  
   **Acceptance (names-only).** `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`.  
* **Header snapshot normalization.** Stored snapshots use lower-case header names; values are verbatim (PF12; `SNAPSHOT_HEADER_LOWERCASE_OK`).

  ### **8.4 Routing (titles-only) \[Canon\]**

* **PF05 — CLI/API.** Admin flags/flows for preview; sidecar/output contracts.

* **PF04 — Governance.** A7 transport for Aux (ETag/HEAD/304/429; writers/errors); refusal/logging allow-lists; suppression posture.

* **PF12 — Schemas & Artifacts.** Evidence Index \+ mirror schema and canonicalization rules.

* **PF15 — Copy Tonality Guide.** Editorial safety rules (banned tokens/phrases); PF17 lists names only.


## **9\) Rollout & Gating (when adopted)**

### **9.1 Sequencing & Dependencies — plan-first, prove-as-you-go \[Canon\]**

**Order (must follow this sequence).**

1. **PF14 — Mechanics (implement & test).**  
    Build the deterministic composer; enforce lints; wire suppression; prove determinism (**two-run**, **AB↔BA**); implement any variety features (§7); add unit/property tests.

2. **PF05 / PF04 — Surfaces & transport (wire & prove).**  
    Expose Aux/CLI behaviors in **PF05** (routes, stdout/sidecar guarantees) and prove **A7 transport in PF04**:  
    – **200:** **strong quoted ETag**.  
    – **HEAD 200:** validator parity; **no body**; **Content-Length \= len(identity 200 body)**.  
    – **304:** only after prior 200; **omits both `Content-Type` and `Content-Length`**; no body.  
    – **Vary:** `Authorization, Accept-Encoding`.  
    – **Encoding invariance** of identity (ETag) and effective length.  
    – **Catalog-only** proof surface with **headers-only env-gate** proof; include the **composite success-proof JSON** (schema lives in PF12).

3. **PF09 — Build Checklist (gate & ship).**  
    Make narrative markers **blocking** (determinism, lints/safety, A7 proofs, provenance). **Ship only** when all narrative gates pass.

**Doc-in-PR rule (evidence parity).** Every code/test change that affects narratives **must update, in the same PR**:

* the **human Evidence Index** `docs/evidence/INDEX.json`,  
* the **hash sentinel** `docs/evidence/INDEX.sha256` (merge-gating; must match INDEX.json), and  
* the **machine mirror** `artifacts/evidence_index.jsonl` (**records-only** canonical JSONL: UTF-8, compact, **one LF**, **unknown-keys rejected**, **ASCII field order**, **sort-before-write**, **single mirror file**; each record includes `discovered_physical_path` and a **`proof_anchor`** to a co-located path-proof).  
   Run captures and CI under \*\*\`LC\_ALL=C, LANG=C, TZ=UTC\`\*\*. Governed locations only: artifacts live under \`artifacts/\*\*\` and \`docs/\*\*\`.

**Dependencies & handoffs.**

* **PF14** produces passing tests and artifacts (compose examples, acceptance logs) that **PF05/PF04** consume for parity/transport probes.  
* **PF05** declares payload/sidecar contracts; **PF04** pins A7 posture (including **200 suppressed \= empty body; no ETag**).  
* **PF09** reads the same artifacts/tokens and enforces ship/no-ship decisions via **blocking gates**.

**Acceptance (names-only).** `DOC_DELTA_RECORDED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`.

**Routing (titles-only).**  
 PF14 — Mechanics (implementation/tests) • PF05 — CLI/API & PF04 — Governance (surfaces \+ A7 proofs) • PF09 — Build Checklist (blocking narrative gates).

---

### **9.2 Narrative Acceptance Gate (CF-NARR) — close conditions & blocking tokens \[Canon\]**

**Scope (“touching narratives”).**  
 Composer changes (inputs/outputs, lints, suppression, determinism) • Surfaces/transport posture for Aux/CLI (A7 proofs by title) • Packs/identity/provenance (`catalog` listing, **`pack_sha` echo/match**).

**Close condition (all must pass).**

* **Determinism:** two-run identity and AB↔BA coherence proven on composer outputs.  
* **Lints & safety:** paragraph length/shape/tone enforced; suppression on failure.  
* **Provenance:** `pack_sha` echoed and matched against **release-pinned manifest**.  
* **A7 transport evidence present:** **Catalog snapshot**, **env-gate headers** proof, and **composite A7 proof JSON** (PF12 schema) for a cataloged JSON success route; `/internal/version` excluded.  
* **Doc-in-PR parity:** human index \+ sentinel \+ machine mirror updated **in the same PR**.

**Blocking token set (names-only; enforced elsewhere).**

* **Determinism:** `NARR_DETERMINISM_OK` · `NARR_AB_BA_COHERENCE_OK` · `NARR_LF_NORMALIZATION_OK`.  
* **Lints & safety:** `NARR_LEN_≤300_OK` · `NARR_NO_EM_DASH_OK` · `NARR_BANNED_TOKENS_OK` · `NARR_JARGON_FREE_OK` *(or `NARR_INCLUSIVE_TONE_OK` per PF15)*.  
* **Transport (Aux A7):**  
   `NARR_200_TEXT_OK` · `NARR_SUPPRESSED_NO_ETAG_OK` ·  
   `A7_GET_QUOTED_ETAG_OK` · `A7_HEAD_PARITY_OK` · `A7_304_OMITS_CT_CL_OK` · `A7_VARY_AUTH_AE_OK` · `A7_ENCODING_INVARIANCE_OK` ·  
   `ENDPOINTS_CATALOG_INTERNAL_OK` · `ENDPOINTS_CATALOG_ENV_GATE_OK` · `A7_TRANSPORT_PROOF_OK`  
   *(rate-limits as applicable: `A7_429_HEADERS_OK`, `A7_RETRY_AFTER_BOTH_OK`)*  
* **Provenance:** `NARR_PACK_SHA_OK` (echo & match against release-pinned manifest).

**Process rules.**

* **Single-homes routing.** Keep payload bytes in **PF05**, A7 transport in **PF04**, pack/schema bytes in **PF12** (this guide stays names-only).  
* **Doc-in-PR rule.** Update the human index \+ hash sentinel \+ machine mirror **in the same PR** (canonical JSONL; unknown-key rejection; `proof_anchor`, ASCII order, sort-before-write, single file).  
* **Blocking gates.** **PF09** treats the above tokens as **ship/no-ship** for any epic that touches narratives.

**Aggregated gate (names-only).** `NARR_GATE_ACCEPT_OK` (set **true** only when the entire CF-NARR set above is green).

**Routing (titles-only).**  
 PF14 — Mechanics: maintain tests for the CF-NARR token set • PF09 — Build Checklist: ensure all CF-NARR tokens are blocking • PF05/PF04/PF12: bytes/matrices live in their homes; this subsection does not duplicate them.

---

## **Appendix A) Minimal schema stubs (request/response; pack manifest) — route canonical homes to PF12 \[Informative stubs\]**

**Status.** Informative stubs only. These illustrate shapes for implementers and QA while **PF12 — HDE-Schemas & Artifacts** publishes and version-controls the **canonical schemas**. Canonicalization rules and the **machine Evidence Index** also live in **PF12** (titles-only routed here).

**Canonicalization posture (applies to all examples below).** UTF-8 JSON, **sorted keys**, **compact**, **exactly one trailing LF**; **no `\r`**. Final rules are owned by **PF12**.

### **A.1 `composer.request.v1.schema.json` (stub)**

Inputs reflect the current spec after retiring `uncertainty` and `pace_met`. **This stub is illustrative only; PF12 will publish the canonical schema.**

* {  
*   "$schema": "https://json-schema.org/draft/2020-12/schema",  
*   "title": "composer.request.v1 (stub)",  
*   "type": "object",  
*   "additionalProperties": false,  
*   "required": \["band", "families\_fired", "perspective", "release\_id", "pack\_sha"\],  
*   "properties": {  
*     "band": { "type": "string", "enum": \["Cool", "Open", "Warm", "Glow"\] },  
*     "families\_fired": { "type": "array", "items": { "type": "string" }, "uniqueItems": true, "description": "ASCII-sorted, unique family ids" },  
*     "perspective": { "type": "string", "enum": \["shared", "a\_to\_b", "b\_to\_a"\] },  
*     "release\_id": { "type": "string", "pattern": "^\[0-9a-f\]{64}$" },  
*     "pack\_sha": { "type": "string", "pattern": "^\[0-9a-f\]{64}$" }  
*   }  
* }


*Notes:* Validation is **fail-closed**; violations lead to a **suppressed** result (see A.2). See **PF12** for the canonical request schema once published.

### **A.2 `composer.response.v1.schema.json` (stub)**

Outcomes are **mutually exclusive**: **Text** or **Suppressed**. The only policy reason retained is `"conflict"`.

* {  
*   "$schema": "https://json-schema.org/draft/2020-12/schema",  
*   "title": "composer.response.v1 (stub)",  
*   "oneOf": \[  
*     {  
*       "type": "object",  
*       "additionalProperties": false,  
*       "required": \["text", "composition\_id", "fragment\_ids", "pack\_sha"\],  
*       "properties": {  
*         "text": { "type": "string", "maxLength": 300 },  
*         "composition\_id": { "type": "string", "minLength": 8, "maxLength": 128 },  
*         "fragment\_ids": { "type": "array", "minItems": 1, "items": { "type": "string" } },  
*         "pack\_sha": { "type": "string", "pattern": "^\[0-9a-f\]{64}$" }  
*       }  
*     },  
*     {  
*       "type": "object",  
*       "additionalProperties": false,  
*       "required": \["suppressed", "policy\_reason", "composition\_id", "pack\_sha"\],  
*       "properties": {  
*         "suppressed": { "const": true },  
*         "policy\_reason": { "type": "string", "enum": \["conflict"\] },  
*         "composition\_id": { "type": "string", "minLength": 8, "maxLength": 128 },  
*         "pack\_sha": { "type": "string", "pattern": "^\[0-9a-f\]{64}$" }  
*       }  
*     }  
*   \]  
* }


*Notes:* Both paths **echo `pack_sha`** for provenance; canonical response bytes/sidecar shapes live in **PF05**; **schema ownership** lives in **PF12**. Aux **“200 suppressed \= empty body, no `ETag`”** is pinned in **PF04**.

### **A.3 `narrative.pack.v1.schema.json` (stub)**

A pack describes governed content and guards the composer consults. File list and identities are **manifest-listed**; pack identity is **`pack_sha`**. **PF12** owns the real schema.

* {  
*   "$schema": "https://json-schema.org/draft/2020-12/schema",  
*   "title": "narrative.pack.v1 (stub)",  
*   "type": "object",  
*   "additionalProperties": false,  
*   "required": \["nodes"\],  
*   "properties": {  
*     "nodes": {  
*       "type": "array",  
*       "items": {  
*         "type": "object",  
*         "additionalProperties": false,  
*         "required": \["id", "slot", "band", "text"\],  
*         "properties": {  
*           "id": { "type": "string" },  
*           "slot": { "type": "string" },  
*           "band": { "type": "string", "enum": \["Cool", "Open", "Warm", "Glow"\] },  
*           "text": { "type": "string" },  
*           "constraints": { "type": "object", "additionalProperties": true }  
*         }  
*       }  
*     },  
*     "palettes": { "type": "object", "additionalProperties": true },  
*     "suppression\_map": { "type": "object", "additionalProperties": true }  
*   }  
* }


**Notes**

* Pack files (`keys.json`, `templates.json`, optional `palettes.json`, `suppression_map.json`) are **manifest-listed**; sibling `*.sha256` identities ship with artifacts; pack identity **couples to `release_id`**.  
* Suppression via `suppression_map` is the **content-level guard**; algorithmic behavior is in **PF17/PF14**, while **schema shape** is **PF12**’s remit.

**Evidence & machine mirror (reminder).** Whenever these stubs inform generated artifacts (examples, acceptance logs), **update the human Evidence Index \+ hash sentinel** and append one JSON line per artifact to `artifacts/evidence_index.jsonl` in the **same PR**. **PF12** governs mirror conventions (canonical JSONL, unknown-key rejection, `proof_anchor` to a path-proof).

---

## **Appendix B) Example artifacts (compose\_examples, identities, acceptance tokens file) — samples only \[Informative stubs\]**

**Status.** Informative stubs. These non-canonical examples illustrate artifact shapes for QA and implementers. Canonical schemas/canonicalization and the machine mirror live in **PF12 — Schemas & Artifacts**; payload/sidecar bytes live in **PF05 — CLI/API**. **Update the human Evidence Index \+ hash sentinel and machine JSONL in the same PR** when adding artifacts.

**Canonicalization posture for all files below.** UTF-8 JSON (or UTF-8 text), **sorted keys**, **compact**, and **exactly one trailing LF**; **no `\r`**.

### **B.1 `examples/compose_examples.json` (sample)**

* \[  
*   {  
*     "request": {  
*       "band": "Warm",  
*       "families\_fired": \["talk\_ladder","story"\],  
*       "perspective": "shared",  
*       "release\_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",  
*       "pack\_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"  
*     },  
*     "response": {  
*       "text": "You two find an easy rhythm together. Conversation opens doors and softens edges.",  
*       "composition\_id": "comp\_q1w2e3r4",  
*       "fragment\_ids": \["frag\_opener\_01","frag\_center\_17","frag\_closer\_03"\],  
*       "pack\_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"  
*     }  
*   }  
* \]


*Notes:* Request/response fields mirror the spec after retiring `uncertainty`/`pace_met`. Responses **echo `pack_sha`** and include `composition_id` & `fragment_ids` for provenance.

### **B.2 Identities alongside governed files (sample)**

Place **SHA identities** next to governed files under `catalog/narratives/`:

* catalog/narratives/keys.json  
* catalog/narratives/keys.json.sha256  
* catalog/narratives/templates.json  
* catalog/narratives/templates.json.sha256  
* catalog/narratives/palettes.json  
* catalog/narratives/palettes.json.sha256  
* catalog/narratives/suppression\_map.json  
* catalog/narratives/suppression\_map.json.sha256


*Notes:* Packs are **manifest-listed** and **SHA-pinned**; pack identity **couples to `release_id`**. Sibling `*.sha256` files **ship with artifacts**.

### **B.3 `acceptance/narratives_acceptance.txt` (names-only tokens)**

* NARR\_DETERMINISM\_OK  
* NARR\_AB\_BA\_COHERENCE\_OK  
* NARR\_LF\_NORMALIZATION\_OK  
* NARR\_LEN\_≤300\_OK  
* NARR\_NO\_EM\_DASH\_OK  
* NARR\_BANNED\_TOKENS\_OK  
* NARR\_JARGON\_FREE\_OK  
* NARR\_SUPPRESSED\_NO\_ETAG\_OK  
* A7\_GET\_QUOTED\_ETAG\_OK  
* A7\_HEAD\_PARITY\_OK  
* A7\_304\_OMITS\_CT\_CL\_OK  
* A7\_VARY\_AUTH\_AE\_OK  
* A7\_ENCODING\_INVARIANCE\_OK  
* NARR\_200\_TEXT\_OK  
* A7\_429\_HEADERS\_OK  
* A7\_RETRY\_AFTER\_BOTH\_OK  
* NARR\_PACK\_SHA\_OK


*Notes:* Names-only acceptance roster; gates/tests live in **PF09/PF14**; A7 details live in **PF04**. PF17 does **not** restate header matrices or payload bytes.

### **B.4 Machine Evidence Index (JSONL) — one line per artifact (sample)**

**File:** `artifacts/evidence_index.jsonl` *(append lines; same PR as the human Evidence Index \+ sentinel)*

* {"artifact\_key":"compose\_examples","role":"snapshot","sha256":"cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","size\_bytes":234,"produced\_at\_utc":"2025-11-06T12:00:00Z","discovered\_physical\_path":"examples/compose\_examples.json","proof\_anchor":"audit/examples/compose\_examples.stat.txt"}  
* {"artifact\_key":"narratives\_acceptance\_tokens","role":"log","sha256":"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd","size\_bytes":182,"produced\_at\_utc":"2025-11-06T12:00:00Z","discovered\_physical\_path":"acceptance/narratives\_acceptance.txt","proof\_anchor":"audit/acceptance/narratives\_acceptance.stat.txt","ids":{"pack\_sha":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","release\_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}}


*Notes:* **Canonical JSONL**; one object per line; **unknown keys rejected**; each record includes a `proof_anchor` (path-proof). **Never include narrative text** in logs/sidecars — **ids-only**.

### **B.5 CLI sidecar (ids-only) — sample**

**Path:** `preview/compose_sidecar.json`

* {  
*   "composition\_id": "comp\_q1w2e3r4",  
*   "fragment\_ids": \["frag\_opener\_01", "frag\_center\_17", "frag\_closer\_03"\],  
*   "pack\_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",  
*   "release\_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  
* }


**Notes.**

* **Ids only; no prose.** Sidecar echoes the same identifiers present in composer outputs for provenance (`composition_id`, `fragment_ids[]`, `pack_sha`) and may include `release_id` to tie to the freeze.  
* **Evidence parity.** When this file is produced/updated, append a line to `artifacts/evidence_index.jsonl` and update the **human Evidence Index \+ sentinel** in the **same PR**.  
* 

---

# **Appendix** C) Copywriter Templates

Here’s a **clean, copy-and-paste template pack** that can be used to request and then update deliverables from a copywriter session. It’s designed to be **unambiguous, lint-ready**, and easy for Codex/IA to act on. There are two parts:

1. **New Request (Intake)** — to kick off a session and gather fresh narratives

2. **Update (PATCH)** — to revise, add, or remove specific items after the session

I’m also including a **review checklist** and a **one-liner handoff** to Codex so your operator can move immediately without asking you follow-ups.

---

## C. 1 New Request — Copywriter Intake Template (NIB-style)

> Use this template to request a new batch. Paste it into the session/chat as-is and fill the blanks.

\>\>\>BEGIN NARRATIVES REQUEST  
REQUEST:  
  title: "\<short label for this batch\>"  
  owner: "\<your name/role\>"  
  due\_by: "\<YYYY-MM-DD or ASAP\>"  
  audience: "\<dating, friendship, collaborators, etc.\>"  
  voice\_tone: "\<e.g., warm, encouraging, inclusive\>"  
  constraints:  
    max\_chars: 300  
    sentences: "2-4"  
    single\_paragraph: true  
    no\_digits: true            \# no ASCII numerals 0–9  
    no\_emdash: true            \# no — em-dash  
    inclusive\_tone: true  
    no\_crlf: true              \# no carriage returns; text ends with one LF

SCOPE:  
  \# Choose any you want in this batch. You can start small (partial coverage).  
  categories: \["harmony","friction","growth","chemistry","timing","focus","support","play","depth","clarity"\]  
  bands: \["cool","open","warm","glow"\]  
  perspectives: \["shared","a\_to\_b","b\_to\_a"\]  
  slots: \["opener","center","closer","softener"\]  \# softener is optional

GUIDANCE:  
  user\_goal: "\<what the narrative should help the user feel/do\>"  
  avoid: \["jargon","advice/imperatives like 'should'","body/medical claims","numbers/dates"\]  
  examples (optional):  
    \- "A good 'shared/warm/opener' sounds like: \<1 short sample\>"  
    \- "But avoid: \<too technical / too long / salesy\>"

ROWS:  
  \# Add as many as you want. Use the id convention below.  
  \# id format: nar.\<category\>.\<band\>.\<perspective\>.\<slot\>.\<slug-\#\#\>  
  \# slug ends with \-01, \-02, ... to allow future revisions.

  \- category: harmony  
    band: warm  
    perspective: shared  
    slot: opener  
    id: nar.harmony.warm.shared.opener.glow-welcome-01  
    text: "\<≤300 chars; 2–4 sentences; one paragraph; inclusive; no digits/em-dash\>"

  \- category: harmony  
    band: warm  
    perspective: shared  
    slot: center  
    id: nar.harmony.warm.shared.center.glow-welcome-02  
    text: "\<…\>"

  \# (add more rows as needed)

SUPPRESSION (optional):  
  \# When to suppress a narrative so we’re honest (leave empty if none)  
  \- guard: "if profile=Reflector and authority=SoundingBoard"  
    action: "suppress"  
    ids: \["nar.harmony.warm.shared.opener.glow-welcome-01"\]

NOTES (optional):  
  \- "\<any editorial notes or nuance\>"  
\<\<\<END NARRATIVES REQUEST

---

## C.2 Update Request — Copywriter PATCH Template (targeted changes)

> Use this to fix specific lines or add/remove after a session. Keep it surgical.

\>\>\>BEGIN NARRATIVES UPDATE  
REQUEST:  
  title: "\<short label for patch\>"  
  owner: "\<your name/role\>"  
  reason: "\<typo fix|tone fix|add coverage|remove unsafe content\>"  
  due\_by: "\<YYYY-MM-DD or ASAP\>"

PATCH:  
  \# choose one op per entry: replace | add | remove

  \- op: replace  
    id: nar.harmony.warm.shared.opener.glow-welcome-01  
    text: "\<new text here; same constraints\>"

  \- op: add  
    row:  
      category: timing  
      band: cool  
      perspective: a\_to\_b  
      slot: closer  
      id: nar.timing.cool.a\_to\_b.closer.steady-signals-01  
      text: "\<≤300 chars; 2–4 sentences; one paragraph; no digits/em-dash\>"

  \- op: remove  
    id: nar.harmony.warm.shared.center.glow-welcome-02

SUPPRESSION (optional):  
  \- op: add  
    rule:  
      guard: "if category=harmony and band=warm and missing=true"  
      action: "suppress"  
      ids: \[\]

NOTES (optional):  
  \- "\<anything helpful for the fix\>"  
\<\<\<END NARRATIVES UPDATE

---

### C.2.1 Acceptance & lint gates (copy-review checklist)

Paste this under your request if you want the copywriter to self-check before handing back:

* **Length** ≤ 300 chars

* **Sentences** 2–4, one paragraph

* **Digits** none (no 0–9)

* **Em-dash** none (—)

* **Tone** inclusive, simple, human

* **No CR** (no `\r`), ends with one LF (`\n`)

* **ID matches the row** (category/band/perspective/slot align to id segments)

* **Directional**: `a_to_b` and `b_to_a` are allowed to differ; `shared` should read coherently for both

* **No claims** (medical/diagnostic/prescriptive)

* **Suppression** rules present if needed (honest no-output over filler)

---

### C.2.2 One-liner handoff for Codex (operator)

> Put this under the copywriter’s response so the operator can act without questions.

* **Intake**: “Ingest the above as **NIB-1.0**. Validate lints/IDs. Report any row-level errors with `error + field + hint`.”

* **Preview**: “Render preview via shared presenter. Confirm CLI \= HTTP bytes. If not equal, block and report.”

* **Publish** (only when requested): “Publish as a new pack; export canonical pack files, build `manifest.json`, compute `pack_sha`, upload to object storage; open one PR with human index \+ hash sentinel and machine mirror lines (records-only, ASCII key order, one LF, sorted, de-duped, path-proofs).”

* **PATCH**: “Apply `add|replace|remove` ops; re-lint; re-preview; publish/export only if requested.”

---

### C.2.3 Quick tips for the copywriter (keeps feedback cycles short)

**Do**

* Keep it **clear, kind, grounded** (“you two…”, “together you’ll notice…”).

* Use **short sentences**; neutral verbs (“notice”, “tend to”, “often”).

* Show **felt sense** (timing, ease, openness), not analysis.

**Don’t**

* Don’t instruct, fix, or prescribe (“you should”, “do this”).

* Don’t use numbers/dates or intensifiers (“always”, “never”).

* Don’t reveal private mechanics (no inner technical labels).

---

### C.2.4 Minimal “tiny” variant (if you need to drop a fast ask)

> For quick asks in a thread — Codex can still ingest this.

NEED:  
\- 4 lines for category=harmony, band=warm, perspective=shared  
\- slots: opener|center|closer|softener (softener optional)  
\- ≤300 chars; 2–4 sentences; one paragraph; no digits/em-dash

FORMAT (per row):  
id=nar.harmony.warm.shared.opener.glow-welcome-01  
text="\<your line\>"

id=nar.harmony.warm.shared.center.glow-welcome-02  
text="\<your line\>"

---

### C.2.5 FAQ — to prevent back-and-forth

**Q: What if I’m not sure about the exact ID?**  
 A: Fill the row fields and leave `id:` blank; Codex will mint a slug and return it to you for review. For replacements, **id is required**.

**Q: Can I ship partial coverage?**  
 A: Yes. We can publish category/band subsets; the renderer fails closed when a slot is missing.

**Q: Can I ask for “more poetic / more minimal” without specifics?**  
 A: Yes—add 1–2 micro examples under `GUIDANCE.examples`. It reduces rewrite cycles.

**Q: I need a softer/stronger tone for one category**  
 A: Add a `NOTES:` bullet for that category; we’ll pass it to the linter as a soft hint.

**Q: Can I request alternative variants?**  
 A: Add multiple rows with `slug-01`, `slug-02` and mark your preferred one in `NOTES:`. We’ll keep both offline and publish the preferred.

---

### C.2.6 Ready-to-send example (new request, small batch)

\>\>\>BEGIN NARRATIVES REQUEST  
REQUEST:  
  title: "Harmony Warm — shared intro"  
  owner: "Nathan"  
  due\_by: "2025-11-10"  
  audience: "romantic"  
  voice\_tone: "warm, honest, grounded"  
  constraints:  
    max\_chars: 300  
    sentences: "2-4"  
    single\_paragraph: true  
    no\_digits: true  
    no\_emdash: true  
    inclusive\_tone: true  
    no\_crlf: true

SCOPE:  
  categories: \["harmony"\]  
  bands: \["warm"\]  
  perspectives: \["shared"\]  
  slots: \["opener","center","closer"\]

GUIDANCE:  
  user\_goal: "Set a hopeful tone without promising outcomes; invite curiosity."  
  avoid: \["jargon","advice","medical/body claims"\]  
  examples:  
    \- "You find an easy rhythm together…"  
    \- "But avoid: 'always/never', directives like 'should'"

ROWS:  
  \- category: harmony  
    band: warm  
    perspective: shared  
    slot: opener  
    id: nar.harmony.warm.shared.opener.glow-welcome-01  
    text: "You two warm up quickly, with gentle clarity. It’s not loud; it’s steady. Each step feels natural and invites the next."

  \- category: harmony  
    band: warm  
    perspective: shared  
    slot: center  
    id: nar.harmony.warm.shared.center.glow-welcome-02  
    text: "It’s easy to fall into a shared pace. Small signals stand out—a glance, a pause—and you both tend to honor them."

  \- category: harmony  
    band: warm  
    perspective: shared  
    slot: closer  
    id: nar.harmony.warm.shared.closer.glow-welcome-03  
    text: "This is a place to keep tending. Keep listening for the subtle ‘yes’. You don’t need to rush; your rhythm emerges on its own."

NOTES:  
  \- "If any line feels borderline prescriptive, soften the verb."  
\<\<\<END NARRATIVES REQUEST

---

If you want, I can also emit these as **two Markdown files** (e.g., `templates/NARRATIVES_REQUEST.md` and `templates/NARRATIVES_UPDATE.md`) formatted for your repo, or as a **Google Docs friendly** version.

