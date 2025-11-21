# 0 Front Matter

## 0.1 Document Control

**Title:** PF17-Review-HDE Narratives Guide  
**Version:** v1.4.1  
**Status:** Canon  
**Effective** date: 2025-11-17

**Last Update Gate:** BN 7.1 drain  
**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **0.2 Scope & Audience**

**Scope.** This guide owns the narrative mechanics at the spec level. It defines, in names/behavioral terms (no byte dumps):

* **Deterministic composer contract.** Inputs, outputs, tie-breaks, suppression outcomes, AB↔BA coherence, two-run identity, and hard lints. *(Tests/linters live in PF14; acceptance wiring lives in PF09 — titles only.)*  
* **Narrative packs & identity linkage.** What exists and how it is referenced (**pack\_sha**, freeze-pack/manifest coupling), not byte-for-byte schemas. *(Schemas/manifest listing live in PF12.)*  
* **Surfaces (policy level).** Reader v1 is narrative-free; Aux Narrative and CLI admin preview exist and are routed by title to their single homes (PF05/PF04).  
* **Evidence/Doc-Delta hooks.** Names of acceptance markers and cross-doc requirements; **same-PR** human `docs/evidence/INDEX.json` \+ hash sentinel ↔ machine `artifacts/evidence_index.jsonl` parity, canonical JSONL, unknown-key rejection, ASCII field order, sort-before-write, **single mirror file**, and **proof\_anchor** discipline are owned in PF12/PF06 and referenced here by title.

**A7 proof surfaces.** A7 proofs run **only** on a **Catalog JSON success** route (Endpoint Catalog is internal-only and env-gated per entry); `/internal/version` is excluded. Evidence comprises:

* a **headers-only env-gate proof** (demonstrates non-prod entries are unreachable in prod), and  
* a **composite A7 proof JSON** (machine-checkable; schema lives in PF12).  
   PF17 references these by **title only**; bytes live in PF05; tokens/policy live in PF04.

**Out of scope.** This guide does **not** define:

* A7 transport rules & validators (e.g., strong ETag on 200, HEAD parity, 304 header omission, writers/errors no-store, rate-limits) → **PF04 — HDE-Governance.** *(PF04 also pins Aux “200 suppressed \= empty body; no ETag.”)*  
* Public payload bytes for Reader/CLI/Aux, endpoint shapes, and examples → **PF05 — HDE-CLI-API-Vendor-Ref.**  
* Reader covenant & preimage/idempotence (bands-only success body) → **PF01 — HDE-Math-Spec.**  
* Canonical JSON schemas, manifest listing, machine Evidence Index → **PF12 — HDE-Schemas & Artifacts.**  
* Implementation tasks/tests & CI gates (lints, AB↔BA, two-run, acceptance) → **PF14 — HDE-Mechanics Guide** and **PF09 — HDE-Build Checklist.**  
* Architectural boundaries & single-emitter rule → **PF02 — HDE Architecture.**

**Audience.** Engine implementers, adapter/presenter engineers, CLI maintainers, editorial/content ops, and reviewers. Editors follow titles-only routing and do **not** duplicate bytes owned by other PF documents.

**Supersession rule (PF10 addenda).** PF10 addenda are **numbered**; when multiple addenda exist, the **later number governs**. PF17 follows the latest and routes by title only (no version numbers).

---

0.3 Single Homes (titles-only routing)

This guide does not restate payload bytes, header matrices, or schemas that live elsewhere. It routes by document title to these single homes:

* **HDE-Governance (PF04).** A7 transport policy and validators (quoted strong ETag on 200; HEAD parity; 304 omits Content-Type and Content-Length; Vary: Authorization, Accept-Encoding; encoding-invariance), writers/errors no-store, `/internal/version` ops-only. Aux suppression: 200 with empty body, no ETag.

* **HDE-CLI-API-Vendor-Ref (PF05).** Public/CLI/Aux route ownership and payload bytes; flags; stdout/sidecar guarantees. Endpoint Catalog (JSON success) is the A7 proof surface and is internal-only, env-gated; include a headers-only env-gate capture and the composite A7 proof JSON by title.

* **HDE-Schemas & Artifacts (PF12).** Canonical JSON constraints; freeze-pack manifest; `catalog/narratives/*` pack listing and `pack_sha` definition; human `docs/evidence/INDEX.json` and machine `artifacts/evidence_index.jsonl` (records-only) with same-PR parity, hash sentinel, unknown-key rejection, ASCII field order, sort-before-write, single mirror file, and `proof_anchor` per record.  
   • Machine mirror discipline and tokens (single JSONL file; ASCII field order; sort-before-write; unknown-key reject; one LF; `proof_anchor`) are normative (PF12/PF09): `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
   • Header snapshots store **lower-case header names** (values verbatim). Acceptance: `SNAPSHOT_HEADER_LOWERCASE_OK`.

* **HDE-Math-Spec (PF01).** Reader covenant (bands-only public JSON), preimage and identity.

* **HDE-Mechanics Guide (PF14).** Composer tasks/tests (hard lints; AB↔BA; two-run; suppression), integration with acceptance.

* **Epic-Process-Guide (PF06).** PR-first; same-PR index \+ sentinel \+ mirror updates; governed locations only.

* **HDE Architecture (PF02).** Single-emitter boundary; Loader/Exporter architecture (fetch/verify/atomic swap).

* **HDE-Copy Tonality (PF15).** Editorial tone (bands-only; no em dashes), banned tokens, copy review gates.

* **Narratives authoring & storage authority (DB-first; titles-only).** Author in DB; exporter snapshots to a manifest-pinned pack for runtime; loader serves sealed files (no DB on hot path). Ownership: PF02 (Loader/Exporter), PF07 (DB names only), PF12 (pack/manifest schema and release coupling). PF17 stays contract-free.

  ---

For §8.3 “Ops & Evidence discipline”, append this one line at the end of that section:

* 

---

## **0.4 Acceptance & Evidence pointers (names-only)**

Names only; do not restate semantics. **Token ownership** lives in **PF04 §2.0**; **evidence/index schema & parity** live in **PF12** (same-PR human index \+ sentinel \+ machine mirror; records-only canonical JSONL; unknown-keys rejected; ASCII field order; sort-before-write; single mirror file; `proof_anchor` present).

**Narratives packs:**  
 `NARR_PACKS_IN_MANIFEST_OK`, `NARR_PACK_MANIFEST_OK`, `NARR_PACK_IDENTITY_OK`.

**Aux transport:**  
 `AUX_A7_GET_QUOTED_ETAG_OK`, `AUX_A7_HEAD_PARITY_OK`, `AUX_A7_304_OMITS_CT_CL_OK`, `AUX_200_SUPPRESS_EMPTY_NO_ETAG_OK`.

**Indices:**  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

**Grace Gate (EPIC-010 pre-start):**  
 `GRACE_DELIVERABLES_GATE_OK` *(dependency note only; not a PF17 home).*

**Drivers:** PF10-K (Grace gate); PF04 §2.0 roster.

---

# **Part 1 — Purpose & Ground Rules** 

## **1.1 Purpose & Non-Goals**

This guide defines the **what/why** of narrative composition; enforcement and tests live in **PF14 (Mechanics)** and **PF09 (Build Checklist)** and are referenced here **by title only**.

### **Purpose**

Specify a **deterministic, LLM-free** layer that converts a set of keys into a short, human-readable paragraph for the **Aux narrative surface** and **CLI admin preview**, while leaving **Reader v1 unchanged and narrative-free**. The composer is a **pure function** with **two-run identity** and **AB↔BA coherence**; it emits **LF-terminated canonical JSON** (composer response) via the **single shared presenter/emitter**. The concrete bytes/serializer contract are routed by title to **PF05 (CLI/API)** and **PF02 (Architecture)**.

### **Non-Goals**

* **No change to Reader v1 public contract.** Reader success remains **bands-only (numeric-free)**; no narrative text appears on Reader v1. (Style/tone live in **PF15—Tonality**.)

* **No transport or payload bytes here.** A7 validators, ops posture, and rate-limits live in **PF04—Governance**; public and CLI/Aux endpoint shapes & payload bytes live in **PF05—CLI/API**. Success proofs are **Catalog-driven** and run only on **Endpoint-Catalog (JSON-success)** routes; the Catalog is **internal-only** and **env-gated** (capture a **headers-only env-gate** proof). `/internal/version` is ops-only.

* **No schema or manifest bytes.** Pack listings, canonical JSON rules, `pack_sha`, and the machine Evidence Index live in **PF12—Schemas & Artifacts**; this guide references them by title only.

* **No randomness, time, I/O, or model calls.** Composition is pure; required properties at adoption include **two-run identity** and **AB↔BA**.

* **No PII in examples/logs/artifacts.** Admin-only preview; examples use ids only (`composition_id`, `pack_sha`, `release_id`); logs remain keys-only.

* **No duplicated bytes across PF docs.** Follow the **single-home, titles-only** doctrine; keep payloads/bytes and schemas in **PF05/PF12** and transport/ops policy in **PF04**.

* **No “pacing” gate here.** “Too early” is a **policy outcome** (validation conflict or `suppression_map` guard); ineligible dyads are **not surfaced** (see **§2.4 can-emit**).

* **No A7 proof details here.** PF17 does not restate A7 bytes; it only notes that proofs require **env-gate headers** and a **composite A7 proof JSON** (PF12 schema) on a **cataloged success route**.

### **1.1.1 EPIC-011 preservation boundary (historical; pattern for future epics)**

For **EPIC-011 — Vendor Ingest & Data Durability (failed)**, Aux narratives were treated as **preservation surfaces**, not a feature surface. This pattern remains in force for any future “durability-only” epics:

* **No new narrative semantics under EPIC-011.**  
   EPIC-011 was allowed to add durability structures, tests, and headers-only evidence around Aux narratives, but it **must not** change:

  * the set of narrative packs and their IDs,

  * pack text or composition,

  * suppression rules, or

  * which output surfaces exist (Aux API and CLI admin preview) or how packs are routed to them.

* **Pattern for future durability-only epics.**  
   The same boundary applies to any future epic whose scope is durability, ingest, or infrastructure rather than content:

  * narrative packs and semantics stay owned here in PF17;

  * durability/infra epics may add tests, headers-only proofs, and indices around these surfaces;

  * content changes (new or revised text, suppression rules, pack coverage/routing, new surfaces) must be owned by **content epics**, not durability epics.

* **Scope routing (titles-only).**  
   PF17 remains the single home for narrative semantics (packs, keys, suppression, and surfaces).

  * Epic-level planning and acceptance rosters now live in **PF20 — Canon-HDE-Phased Epics**; **PF16 — HD Engine Epics Map** is historical only.

  * Token semantics and epic acceptance sets live in **HDE-Governance**.  
     Any functional change to Aux narratives or CLI preview content **must** be owned by a separate epic that explicitly claims those surfaces in PF20; it is out of scope for EPIC-011 and for any purely durability-focused epic.

---

## **1.2 Principles Required‑NowRequired‑NowRequired‑Now**

These principles are **normative** for narrative composition; enforcement and tests live in **PF14 (Mechanics)** and **PF09 (Build Checklist)** and are referenced here **by title only**.

**Deterministic, LLM-free composition.** The composer is a **pure function** with no randomness, time, or external I/O. Identical inputs **must** yield identical bytes (emitted via the single shared presenter/emitter; bytes themselves are owned outside this guide).

**Two-run identity.** Repeatability is required: two executions with the same inputs produce **byte-for-byte identical** output. Determinism acceptance markers are owned in PF14/PF09 (titles-only).

**AB↔BA coherence.** Where perspectives are symmetric, `A→B` and `B→A` must be coherent **by construction**; coherence is enforced via named acceptance markers in PF14/PF09 (titles-only).

**Evidence parity (same‑PR).** Every narrative change **must** update, **in the same PR**: the human Evidence Index `docs/evidence/INDEX.json` \+ hash sentinel and the machine mirror `artifacts/evidence_index.jsonl`. The mirror is **records‑only canonical JSONL** (UTF‑8, sorted keys, compact, **one trailing LF**), **rejects unknown keys**, uses **ASCII field order** and **sort‑before‑write**, is a **single mirror file**, and each record includes a `proof_anchor` to a path‑proof stored alongside the artifact. Evidence lives only under **governed paths** (`artifacts/**`, `docs/**`). All canonicalization and comparisons run with **`LC_ALL=C, LANG=C, TZ=UTC`**. *(Index/mirror schema: PF12; PR‑first workflow: PF06 — titles‑only.)*

**Routing note (titles-only).** Enforcement and tests for these principles live in **PF14 (Mechanics)** and **PF09 (Build Checklist)**; this guide lists principles and acceptance names only.

**Acceptance impact:** Names‑only clarification; PF17 does not own pins or tokens. (Pins requirement is consolidated in PF10 Addendum 9 and enforced via tokens owned in PF04/PF12.) 

---

## **1.3 Terminology & Posture**

This section defines terms and posture used in PF17. Transport and payload bytes are routed by title to **PF04** (Governance) and **PF05** (CLI/API Vendor-Ref).

### **Terms**

**Category.** One of the ten compatibility categories governed by the keys registry (see packs). Keys are recorded per `{category, band, personal_key, shared_key}`.

**Narrative kind (derived; exactly two per category)**

* **Shared Narrative** — a pair-level paragraph for both parties. Key source: `shared_key`. Perspective: `shared`.  
* **Private Narrative** — a directional paragraph from one partner to the other. Key source: `personal_key`. Perspective: `a_to_b` or `b_to_a`.

**Clarification.** `narrative_kind` is derived from `perspective` and is **not** a request field. `Shared ⇒ perspective=shared`; `Private ⇒ perspective∈{a_to_b,b_to_a}`.

### **Text vs suppressed (outcomes)**

* **Text.** Narrative is emitted when policy allows. On Aux success, transport headers/bytes are owned by PF04/PF05 (PF17 does not restate them).  
* **Suppressed.** Deterministic outcome when policy withholds text due to conflict (validation failure or `suppression_map` guard). Aux returns **200 with an empty body and no ETag** (a policy header may be present). *(Pinned in PF04; remove any prior “ETag on suppressed \= OPEN” language.)*

**Public posture (numeric-free).** Reader v1 remains bands-only and narrative-free; narratives appear only via Aux and admin CLI preview.

**Byte discipline (route-only).** Narrative text must contain **no CR**; LF normalization is enforced by acceptance. Runtime hashing/ETag normalization is owned by PF04/PF05; file artifacts remain LF-terminated. PF17 stays contract-free and routes specifics by title.

### **Display policy (per viewer)**

* Everyone sees **Shared** if `can_emit(shared)` passes (no suppression).  
* A sees **Private-to-A** (`perspective=b_to_a`) if `can_emit(b_to_a)` passes; B sees **Private-to-B** (`perspective=a_to_b`) if `can_emit(a_to_b)` passes.  
* **Never** show a user the other party’s private paragraph.  
* Admin preview may show Shared \+ both private directions for QA (admin-only).  
* **Visibility symmetry (AB↔BA).** Match-card visibility is symmetric at the **Top Category**; if either side fails the `can_emit` check there, neither side sees the match. Narrative display then applies the per-viewer rules above.

### **Spec hook (names/fields used by this guide)**

To avoid ambiguity across callers and evidence, PF17 uses these names consistently (names-only):

* `perspective ∈ {shared, a_to_b, b_to_a}` (required). Use `shared` for the Shared narrative; use `a_to_b`/`b_to_a` for the viewer’s Private narrative.  
* `category` (Magic-10 id) and `band` (public band) as usual inputs (keys registry governs mapping).

### **Transport posture (route-only; titles-only)**

* **A7 proof surface.** Success proofs run **only** on a **cataloged JSON success** route (Endpoint Catalog). The Catalog is **internal-only** and **env-gated**; non-prod entries must be **unreachable in prod** — capture a **headers-only env-gate proof**. `/internal/version` is ops-only and **not** A7-eligible.  
* **A7 invariants.** Success proofs must satisfy:  
  * **200:** **quoted strong ETag** over the LF-terminated canonical body and `Vary: Authorization, Accept-Encoding`.  
  * **HEAD 200:** validator parity with 200; **no body**; **`Content-Length = len(identity 200 body)`**; `Content-Type == GET`.  
  * **304:** only after prior 200; **omit both** `Content-Type` **and** `Content-Length`; **no body**.  
  * **Encoding-invariance:** identity (ETag) **and** effective `Content-Length` are stable across accepted encodings.  
  * *(Composite A7 proof JSON is required; schema lives in PF12. All bytes/tests live in PF04/PF05/PF14; PF17 remains contract-free.)*

**Routing (titles-only).** Transport validators live in **PF04 — Governance**; concrete Aux/CLI payload bytes live in **PF05 — CLI/API**. PF17 defines **terms and posture** only.

---

# **Part 2 — System Overview (contract-free)**

## **2.1 Actors & Boundaries (Engine/Adapter/Presenter; single-emitter boundary) \[Canon\]**

**Actors (responsibilities).**

* **Engine** — deterministic compute only; no time/network/I/O/randomness; returns normalized **keys/structures** (no narratives/free text).  
* **Adapter** — single HTTP home; light validation; calls the Engine in-proc; **never hand-crafts public JSON**.  
* **Presenter (canonical emitter)** — the **one** emitter that serializes public bytes for all callers (HTTP and CLI). **Alternate serializers are forbidden** on public paths.

**Boundary guarantees (conceptual).**

* Engine produces **keys/structures only** (no narrative text). Adapter does **not** emit ad-hoc JSON. All public bytes come from the Presenter’s **single canonical emitter**.  
* **One emitter path for CLI and HTTP**; bytes are identical for the same inputs (single-emitter parity; LF-terminated stdout).  
* Architecture remains **contract-free**; payload schemas and transport/header rules are owned elsewhere (titles-only routing).

**Routing (titles-only).**

* **HDE Architecture (PF02):** role boundaries, single-emitter rule, contract-free stance.  
* **HDE-CLI-API-Vendor-Ref (PF05):** public/CLI/Aux route bytes and Endpoint Catalog ownership.  
* **HDE-Governance (PF04):** A7 transport policy (strong ETag/200, HEAD parity, 304 header omissions), writers/errors posture.

---

## **2.2 End-to-End Flow (CLI/HTTP call path; same bytes; LF discipline) — REPLACE**

1. **Entry (CLI or HTTP → Adapter).** Adapter validates and calls the Engine in-proc; it never hand-crafts public JSON.

2. **Compute (Engine).** Deterministic compute only (no time/network/I/O/randomness); returns normalized keys/structures (no free text).

3. **Emit (Presenter — single canonical emitter).** One emitter serializes public bytes for all callers; alternate serializers on public paths are forbidden. The Presenter may invoke the composer deterministically; composition stays contract-free and I/O-free.

4. **Parity (same bytes for CLI and HTTP).** Adapter returns the **exact** Presenter bytes to HTTP; CLI writes the **same** bytes to stdout (**LF-terminated**).

5. **Aux specifics (routing only).** When suppressed, Aux returns **200 with an empty body and no ETag** (policy header optional). (PF04 pins transport; PF17 does not restate matrices.)

6. **A7 proof surface (routing only).** Proofs run **only** on a **Catalog JSON success** route (PF05). The Catalog is **internal-only** and **env-gated**; capture **headers-only env-gate** proof; `/internal/version` is excluded. Invariants required on the cataloged route:

   * **200:** **quoted strong ETag**; `Vary: Authorization, Accept-Encoding`.

   * **HEAD 200:** no body; validators mirror 200; **`Content-Length = len(identity 200 body)`**.

   * **304:** only after prior 200; **omit both `Content-Type` and `Content-Length`**; no body.

   * **Encoding-invariance:** identity (ETag) and effective length are stable across encodings.

   * **Composite A7 proof JSON** is required (schema lives in PF12).

7. **Integrated vs standalone read path.** In integrated mode the Presenter reads via Loader from the **DB authoring store**; in standalone it reads the **exported pack**. **Both paths must yield identical bytes** at the Presenter boundary (source-invariance proof lives in PF12/PF14).

8. **LF discipline.** Output is LF-only; narrative text contains no `\r`. Acceptance checks live in PF14/PF09.

---

## **2.3 Data Hand-Off (keys-only registry & packs; bytes live elsewhere)** 

**Engine hand-off.** Normalized keys/structures only (no narrative/free text): `category`, `band`, `families_fired`, and `perspective`. The Engine remains deterministic and I/O-free.

**Presenter/Composer consumption.** Resolve keys against governed content selected by **pack identity**:

* **Authoring → Export.** Authoring source of truth is the **DB**; the **Exporter** snapshots to `catalog/narratives/*` and lists members in the freeze manifest.

* **Pack manifest — MUST.** `catalog/narratives/manifest.json` **MUST** exist and be listed **exactly once** in `catalog/manifest.json`. Each member under `catalog/narratives/*` is listed **exactly once**.

* **Identity.** `pack_sha = sha256(canonical_bytes("catalog/narratives/manifest.json"))` (lowercase 64-hex).

* **Composer read path.** Composer reads the **pack manifest** semantics (nodes/slots/templates/constraints; optional palettes; `suppression_map`) and uses `{category, band}` \+ registry keys to select/gate output.

* **Keys registry.** Each `{category, band}` row carries `shared_key` and `personal_key` for Shared vs Private paths.

**Identity & traceability.** Pack selection couples to **`release_id`** via the manifest; responses **echo `pack_sha` and `composition_id`** for provenance.

**Out of scope (titles-only routing).** Pack/schema bytes (PF12); payload/CLI/Aux bytes (PF05); A7 transport/header matrices (PF04).

## **2.4 Visibility coupling (can-emit predicate; contract-free; titles-only) \[Canon\]**

**Release-pinned inputs.** Evaluate visibility against the **same pack identity and release** the composer would use: the narratives pack is **manifest-listed and SHA-pinned** (`pack_sha`) and coupled to `release_id`. No rendering, network, or model calls are performed.

**Definition — `can_emit(C)`.** For a given dyad and category **C**, compute `can_emit(C)` by running two deterministic checks against the **release-pinned** pack—without invoking the composer:

1. **Validation conflict.** The tuple for **C** must pass enum/format checks:  
    • valid `band`  
    • `families_fired` ASCII-sorted and **unique**  
    • identity fields are **64-hex** where required  
    If validation would fail, `can_emit(C) = false`.

2. **Pack guard.** The pack’s `suppression_map` for **C** **must not** block emission. If a guard would suppress, `can_emit(C) = false`; otherwise **true**.  
    *(If a category is not present in the pack’s suppression scope, treat it as **suppressed** rather than attempting a fallback.)*

**Visibility rule (match card).** A dyad is visible to a user in category **C** **only if** `can_emit(C) = true`. **No text rendering** is required to make this decision.

**Top-category gating (symmetric).** If a user’s **Top Category** fails `can_emit`, do **not** surface the dyad to that user (list/detail). Apply the same rule to any other surfaced categories. *(List/detail routes live in PF05.)*

**AB↔BA parity.** Visibility is **symmetric**: if either side fails the `can_emit` check for **C**, **neither** side sees the match in **C** (single-emitter / AB↔BA parity principle).

**Reader posture.** Reader public JSON remains **numeric-free** and contains **no narrative text**; gating is based on **eligibility** (would emission be allowed), not on the presence of text. (“Six-key” covenant per PF01.)

**Narrative display coupling (detail view; see §1.3).**

* Show **Shared** to both users if `can_emit(shared)` passes.

* Show the **viewer’s Private** (`a_to_b` or `b_to_a`) only if `can_emit(viewer-directed)` passes.

* **Never** show a user the other party’s private paragraph. *(Admin preview may show all for QA.)*

**Determinism pins.** `can_emit` is a pure, I/O-free check; it is order-neutral (AB↔BA) and produces the same result on every run with the same inputs. Run all checks with the environment set to:

LC\_ALL \= C, LANG \= C, TZ \= UTC.

**Acceptance hooks (titles-only).** Tests and CI gates for lints / AB↔BA / two-run live in **PF14**; ship/no-ship gates live in **PF09**; pack/suppression schemas live in **PF12**.

**Routing (titles-only).**

* **PF12 — Schemas & Artifacts:** pack/manifest and `suppression_map` definitions.

* **PF05 — CLI/API:** list/detail routes and visibility endpoints.

* **PF04 — Governance:** transport policy (ETag/HEAD/304, writers/errors); A7 proof surface and ops exclusion.

  ---


# **Part 3 — Composer Specification** 

Here’s the updated block with both deltas applied.

---

## **3.1 Inputs Tuple (validated)**

These inputs define the request tuple the composer accepts. On any validation failure the composer **fails closed** to a **suppressed** result (**no partial output**).

### **Required inputs (exact fields)**

* **`category`** — Magic-10 id (closed set).  
* **`band`** — one of `{"Cool","Open","Warm","Glow"}`.  
* **`families_fired`** — **ASCII-sorted** set of fired families; **unique**. *(Family ids come from the keys registry in packs.)*  
* **`perspective`** — one of `{"shared","a_to_b","b_to_a"}`. *(Shared \= pair-level; `a_to_b` / `b_to_a` \= private; see §1.3.)*  
* **`release_id`** — **lowercase 64-hex** id of the active freeze manifest.  
* **`pack_sha`** — **lowercase 64-hex** identity of the narrative pack in use.

**Public posture (routing):** the public Aux route accepts `category`, `band`, `perspective` only. **`slot` is not a public field** (pack-internal; QA override only). Bytes live in PF05; policy lives in PF04.

**Notes.** Earlier inputs `uncertainty` and `pace_met` are retired (see §1.3 and §2.4). The tuple is **keys-only**; it contains **no free text** and introduces **no I/O**.

### **Validation (fail-closed)**

Before any selection, the composer **MUST** validate the tuple. On any violation, **return a suppressed result** with `policy_reason:"conflict"` (**no retries, no partial text**):

* **Enum checks:** invalid `band` or `perspective` → **suppressed**.  
* **Families discipline:** `families_fired` not ASCII-sorted **or** contains duplicates → **suppressed**. *(Reject unknown family ids not present in the keys registry.)*  
* **Identity format:** `release_id` or `pack_sha` not valid **lowercase 64-hex** → **suppressed**.  
* **Presence:** missing/blank required fields → **suppressed**.

---

## **3.2 Outputs (choose one)**

Exactly one of the following objects **MUST** be returned.

### **Text path**

{

  "text": "\<string\>",

  "composition\_id": "\<string\>",

  "fragment\_ids": \["\<string\>", "..."\],

  "pack\_sha": "\<64-hex\>"

}

**Constraints (names-only):** `text ≤ 300` UTF-8 chars and **no `\r`**; `composition_id` length **8–128**; `fragment_ids` **minItems=1**; `pack_sha` **lowercase 64-hex**.

### **Suppressed path**

{

  "suppressed": true,

  "policy\_reason": "conflict",

  "composition\_id": "\<string\>",

  "pack\_sha": "\<64-hex\>"

}

**Enum:** `policy_reason == "conflict"` only (validation failure or pack guard).

### **Semantics (contract-free summary; bytes live elsewhere)**

* **Aux surface (titles-only).** When text is shown: `200` with `Content-Type: text/plain; charset=utf-8` and **ETag(text bytes)**. When **suppressed**: `200` **empty body** with **no `ETag`**; a policy header like `X-Narrative-Policy: suppressed` **may** be present. *(PF04 pins transport; PF17 does not restate matrices.)*  
* **CLI parity & evidence.** CLI preview equals internal composer bytes (**LF-terminated**); sidecar may include **ids only** (`fragment_ids`, `composition_id`, `pack_sha`) for admin evidence (no narrative text in evidence).

---

## **3.3 Lints (MUST)**

The following lints are **normative** and **MUST** pass for the Text path:

1. **Length cap:** Narrative text **≤ 300** UTF-8 characters.  
2. **Sentence count:** **2–4 sentences**.  
3. **Form:** **Single paragraph** (no blank lines).  
4. **Numeric-free:** **No numbers** in public text (Reader posture alignment).  
5. **No em-dashes:** reject `—` (use periods/commas instead).  
6. **Line discipline:** **LF-only**; text **must not** contain `\r`.  
7. **Tone:** Inclusive wording; avoid HD jargon in public text *(titles-only pointer to **PF15** for editorial specifics)*.

**Failure handling (deterministic).** Any lint failure **MUST** cause a **suppressed** result with `policy_reason:"conflict"` (**no partial output, no retries**).

**Acceptance names (names-only; enforcement in PF14/PF09):**  
 `NARR_LEN_≤300_OK` · `NARR_2TO4_SENTENCES_OK` · `NARR_SINGLE_PARAGRAPH_OK` · `NARR_NO_NUMERICS_OK` · `NARR_NO_EM_DASH_OK` · `NARR_LF_NORMALIZATION_OK` · `NARR_JARGON_FREE_OK` · `NARR_INCLUSIVE_TONE_OK`.

**Routing (titles-only).** Editorial thresholds: **PF15**; public/CLI bytes: **PF05**; transport/A7: **PF04**.

---

## **3.4 Determinism — pure function; no RNG/time/I/O; two-run identity; AB↔BA coherence**

The composer is a **closed, deterministic function**:

* **Pure, LLM-free function.** **No randomness, time, external I/O, or model calls.** Given the same **validated** inputs, it **MUST** produce the **same bytes**.  
* **Two-run identity.** Running the composer twice with identical inputs **MUST** yield **byte-for-byte identical** output.  
* **AB↔BA coherence.** Where perspective is symmetric, **A→B** and **B→A** results **MUST** be coherent by construction (no accidental asymmetry).  
* **Normalization.** Determinism is supported by **text-normalization** checks (**LF-only; no `\r`**), proven by `NARR_LF_NORMALIZATION_OK`. *(Detailed lint rules in §3.3.)*

**Environment pins (captures/checks).** Run composer captures, header/body snapshots, and canonicalization under **`LC_ALL=C, LANG=C, TZ=UTC`** (names-only; enforcement lives in PF12/PF09).

**Acceptance names (names-only; enforcement in PF14/PF09).**  
 `NARR_DETERMINISM_OK` · `NARR_AB_BA_COHERENCE_OK` · `NARR_LF_NORMALIZATION_OK`.

**Routing (titles-only).** Tests/fixtures: **PF14 — Mechanics**; ship/no-ship gates: **PF09 — Build Checklist**; transport/payload bytes: **PF04/PF05**.

## **3.5 Suppression Policy — deterministic, conflict-only; pack guards allowed**

**Status.** *Proposal only — nothing is implemented.* This policy specifies when the composer **must** return the **suppressed** result. It is **deterministic** (no heuristics, no retries) and evaluated **without rendering text**.

**Triggers (exact).**

1. **Validation conflict.** Any input-tuple violation (**bad enum** for band/perspective; `families_fired` not **ASCII-sorted** or not **unique**; invalid **lowercase 64-hex** for `release_id`/`pack_sha`; missing/blank required fields) ⇒ **suppressed** with `policy_reason:"conflict"`.  
2. **Pack guard.** A governed rule in the pack’s `suppression_map` for the target `{category, band}` forbids emission ⇒ **suppressed** with `policy_reason:"conflict"` (or a pack-defined code if PF12 later standardizes one).

**Retired reasons.** Earlier drafts listed `uncertainty_high` and `pace_unmet`. Both are **removed** from the spec (and from the response enum). Suppression is now **conflict-based only** (validation \+ pack guards).

**Surface behavior (titles-only).**

* **Aux narrative:** on suppression, \*\*return `200` with an empty body and \*\*no `ETag`\*\*\*\*. A policy header such as `X-Narrative-Policy: suppressed` **may** be present. *(PF04 governs; PF17 does not restate bytes.)*  
* **CLI preview:** mirrors the same suppressed outcome (no text); bytes/flags live in **PF05**.

**Can-emit coupling (no render needed).** Visibility can use a pure `can_emit` predicate: run the **same validation checks** and **pack guards** against **release-pinned** packs (`pack_sha`, `release_id`). If either would fail, **do not surface** the dyad for that category (see **§2.4**).

**Reader posture.** Reader v1 remains **numeric-free** and carries **no narrative text**; suppression affects Aux/CLI only.

**Evidence & logging.** Logs are **keys-only** (never narrative text). Suppressed responses still **echo identities** (`composition_id`, `pack_sha`) to keep audits complete; **update** the **human Evidence Index \+ hash sentinel** and the **machine JSONL mirror** in the **same PR** (mirror hygiene per **PF12/PF06**).

**Acceptance names (names-only; enforcement in PF14/PF09).** `NARR_SUPPRESS_ON_CONFLICT_OK` · `CAN_EMIT_CONFLICT_FAILS_OK` · `CAN_EMIT_PACK_GUARD_FAILS_OK` · `AB_BA_VISIBILITY_PARITY_OK`. *(Transport proofs remain under A7 acceptance in PF04.)*

**Routing (titles-only).** Packs/manifest/`suppression_map` → **PF12**; payload bytes & CLI routes → **PF05**; A7 transport/headers → **PF04**. No byte tables are duplicated here.

---

## **3.6 Failure Modes & Fallbacks — validation errors ⇒ suppression; no relaxation paths. Transport semantics live in PF04.**

**Status.** *Proposal only — nothing is implemented.* The composer **must fail closed** on any violation and return a **suppressed** result; it must **never** “fix up,” retry, or emit partial text.

**When to suppress (deterministic triggers):**

1. **Validation conflict.** Any input-tuple violation (**bad enum** for band/perspective; `families_fired` not **ASCII-sorted** or not **unique**; invalid **lowercase 64-hex** `release_id`/`pack_sha`; missing/blank required fields) ⇒ `policy_reason:"conflict"`.  
2. **Pack guard.** Governed rule in the pack’s `suppression_map` for the target `{category, band}` forbids emission ⇒ `policy_reason:"conflict"`.  
3. **Perspective/kind mismatch.** Request implies directional/private vs shared incorrectly (per keys registry) ⇒ treat as **conflict** ⇒ suppressed.  
4. **Lint failure.** Any narrative **lint** violation (≤300 chars; 2–4 sentences; single paragraph; **numeric-free**; **no em-dash**; **LF-only, no `\r`**) **forces suppression**.

**Fallbacks (what we do not do):**

* **No relaxation paths.** Do **not** lower lint thresholds, swap templates, randomize, or “soften” output to pass. **Always prefer suppression** to alteration.  
* **No auto-correction of inputs.** Do **not** sort/dedupe `families_fired` on behalf of caller; **reject instead**.  
* **No alternate emitters.** Public bytes come **only** from the **single canonical emitter**; if parity cannot be proven, **do not emit**.

**Surface behavior (titles-only).** On suppression, \*\*Aux returns `200` with an empty body and \*\*no `ETag`\*\*\*\*, and **may** include `X-Narrative-Policy: suppressed`. *(Transport/A7 details — ETag/HEAD/304/writers+errors — live in **PF04**.)*

**Evidence & logging posture.**

* **Echo identities** even when suppressed (`composition_id`, `pack_sha`) for traceability; **update** the human index **\+ hash sentinel** and the machine mirror in the **same PR**.  
* Logs are **keys-only** (never narrative text); maintain **LF discipline** (no `\r`).

**Routing (titles-only).** Packs/manifest/`suppression_map` → **PF12**; public/CLI bytes → **PF05**; transport/A7 → **PF04**.

---

## **3.7 Composer mechanics — slot model and selection**

**Scope.** Construct exactly one paragraph deterministically from pack-governed fragments; **no model calls**.

**Slot model.** Assemble **lead → bridge → close** in order. Each slot is optional per pack rules and lints, but the result **must** contain **2–4 sentences** (see §3.3).

**Inputs (names-only).** `category`, `band`, `families_fired` (ASCII-sorted, unique), `perspective ∈ {shared,a_to_b,b_to_a}`, `pack_sha`, `release_id`.

**Determinism.** No RNG/time/I/O; same inputs ⇒ same slot choices and bytes.

**Routing (titles-only).** Pack schemas and slot fragment fields live in **PF12**; surface bytes live in **PF05**.

---

## **3.8 Key resolution — registry and perspective paths**

**Registry rules.** For each `{category, band}`, the registry exposes **`shared_key`** and **`personal_key`**.

* `perspective=shared` → use `shared_key`.

* `perspective=a_to_b` or `b_to_a` → use `personal_key` (direction applied at render).  
   Missing key ⇒ **validation conflict** ⇒ suppression.  
   **Tie among candidates.** If multiple candidates exist for a key, choose by a **pack-pinned order**; if not present, pick the first by **ASCII title**. (Order metadata belongs in PF12.)

**Acceptance names (titles-only).** `COMPOSE_KEY_RESOLUTION_OK` · `COMPOSE_ASCII_TIEBREAK_OK`.

---

## **3.9 Priority ordering — families and tie-breakers**

**Primary selector.** Choose the **primary family** from `families_fired` using the pack’s **priority table**. Empty `families_fired` ⇒ **validation conflict** ⇒ suppression.

**Tie-breakers (deterministic).**

1. higher pack priority rank, then 2\) longer continuous match on `{category, band, perspective}`, then 3\) **ASCII** title.

**Acceptance (titles-only).** `COMPOSE_PRIORITY_TIEBREAK_OK`.

---

## **3.10 Fragment assembly — punctuation, casing, whitespace**

* Sentences end with `. ? !` only; **no em dash (—)**.

* Normalize spaces (single between words; one after sentence marks); strip trailing spaces.

* Sentence case; no all-caps beyond acronyms.

* Quotes are straight `" "` (no smart quotes).

* Final output: **one paragraph**, **2–4 sentences**, **≤300 chars**, **LF-only** (no `\r`).  
   **Acceptance (titles-only).** `NARR_NO_EM_DASH_OK` · `NARR_LF_NORMALIZATION_OK` · `NARR_LEN_≤300_OK` · `NARR_2TO4_SENTENCES_OK` · `NARR_SINGLE_PARAGRAPH_OK`.

## **3.11 Palettes and variants — optional, deterministic** 

**Optional palettes.** Packs MAY include `palettes.json` that define synonym/tone variants by **named palette**.

**Selection (no RNG).** A **fixed palette name** (from pack metadata or an operator flag) selects the variant set. There is **no runtime randomization**; the same inputs select the same palette.

**Application.** Palette replace rules are pure mapping tables applied after fragment selection and before assembly lints (see §3.10). If a referenced palette or mapping is missing, treat as **validation conflict** → suppression.

**Determinism.** Applying a palette is a pure function; same inputs → same bytes.

**Acceptance (names-only).** `COMPOSE_PALETTES_DETERMINISM_OK`, `COMPOSE_KEY_RESOLUTION_OK`.

**Routing (titles-only).** Palettes schema and palette selection metadata live in **PF12**; any palette selection flags live in **PF05/PF04**.

## **3.12 Composer provenance — ids and ordering**

**`composition_id` (deterministic).** A stable token (8–128 chars) derived from `{category, band, perspective, pack_sha, release_id}` using a **pack-defined recipe**. No randomness or time sources.

**`fragment_ids` ordering.** Emit `fragment_ids` in the **exact assembly order** `lead → bridge → close`. Omit empty slots.

**Echo fields.** Always echo `pack_sha` and `composition_id` in **both** Text and Suppressed outputs (see §3.2).

**Acceptance (names-only).** `COMPOSE_IDS_DETERMINISM_OK`, `COMPOSE_SLOT_MODEL_OK`.

**Routing (titles-only).** Provenance field recipes and constraints belong in **PF12**; public payload bytes in **PF05**.

## **3.13 `suppression_map` semantics — guards taxonomy** 

**Allowed guards (names/flags only).**

* `blocked: true` — unconditional block for the category.

* `min_band` / `max_band` — allowed band range.

* `disallow_perspective: ["a_to_b"|"b_to_a"|"shared", …]`.

* `families_disallow: [family_id…]` — any intersection with `families_fired` blocks.

**Precedence.**

1. **Validation conflict** (enum/format/key/missing) → suppressed.

2. If validation passes, evaluate guards; any guard **blocks** → suppressed.

3. If no guard is present for category **C**, treat **as blocked** rather than falling back.

**Acceptance (names-only).** `COMPOSE_SUPPRESSIONMAP_GUARDS_OK`.

**Routing (titles-only).** Guard schema belongs to **PF12**; transport semantics of suppression live in **PF04/PF05**.

## **3.14 Authoring plane — DB-first; exporter snapshot** 

**Source of truth (integrated mode).** Keys, templates, optional palettes, and `suppression_map` are **authored and stored in the application database**.

**Exporter (release).** A release Exporter snapshots DB rows into a **manifest-pinned pack** under `catalog/narratives/*`, writes/updates `catalog/narratives/manifest.json` (**MUST**, exactly once), and lists each member **exactly once** in `catalog/manifest.json`.

**Preview parity.** Admin preview reads from the DB authoring plane. The exported pack for the same release **must** produce **identical** composer inputs and outputs (source-invariance).

**Acceptance (names-only).** `AUTHORING_DB_EXPORTER_OK`, `NARR_SOURCE_INVARIANCE_OK`.

**Routing (titles-only).** Exporter/Loader architecture in **PF02**; DB names in **PF07** (names-only); pack schemas and identity in **PF12**.

## **3.15 Loader — verify, swap, no hot-path DB** 

**Verify & swap.** Verify `pack_sha` against the manifest; fetch files; perform an **atomic swap** into the runtime cache so readers observe either the old or new pack (never a partial mix).

**Hot path.** Serve narratives from **sealed files**, not DB, on the hot path.

**Rollback.** Swap back to the prior pack using the manifest pointer.

**Acceptance (names-only).** `LOADER_ATOMIC_SWAP_OK`, `LOADER_VERIFY_IDENTITY_OK`.

**Routing (titles-only).** Loader details in **PF02**; pack identity and indices in **PF12**.

## **3.16 Observability & privacy — keys-only metrics**

**Metrics families (examples).**

* `narr.compose_total`, `narr.compose_suppressed_total`, `narr.compose_latency_ms`.  
   **Labels (bounded).** `category`, `band`, `perspective`, `pack_sha_prefix`, `outcome ∈ {text,suppressed}`. Labels must be from **closed enums**; keep cardinality bounded.

**Privacy posture.** Keys-only logs; **no narrative text** in logs; no PII; redact secrets; follow PF04 logging allow-list (titles-only). No payload echoes in metrics or logs.

**Acceptance (names-only).** `NARR_METRICS_KEYS_ONLY_OK`, `BG_PRIVACY_REDACTION_OK`.

**Routing (titles-only).** Logging/allow-lists live in **PF04**; evidence parity in **PF12/PF06**.

## **3.17 Rollout phases & gates — A→D** 

**A — Authoring \+ admin preview (DB).** Author in DB; admin preview is keys-only and numeric-free.  
 **B — Exporter \+ identity (release).** Export to `catalog/narratives/*` with manifest/`pack_sha`; indices updated in the **same PR**.  
 **C — Loader \+ sealed files (runtime).** Verify/swap; serve sealed packs on hot path; rollback prepared.  
 **D — Optional palettes/admin flags.** Deterministic palette selection; flags pinned by title (no RNG).

**Gates (titles-only).** Evidence follows PF12 **same-PR** index \+ sentinel \+ mirror with `proof_anchor`. PR checklist tokens live in PF09.

**Acceptance (names-only).** `ROLLOUT_PHASE_TAGS_OK`.

# **Part 4 — Packs, Identity & Provenance (titles-only)**

## **4.1 Pack Contents & Manifest Listing (templates, palettes, suppression\_map; sibling .sha256; LF; canonical JSON) \[Canon\]**

**Scope.** Define what lives in a narrative pack and how it is listed and proven; exact schemas/bytes live elsewhere (titles-only routing).

**Pack files (canonical JSON; LF-terminated; sibling .sha256).**  
 Under `catalog/narratives/` we maintain governed files:

* `keys.json` — keys-only registry (10×4 category×band grid; no prose).

* `templates.json` — slot fragments (for example, opener | center | closer | softener) by band/tone.

* `palettes.json` — optional tone groupings.

* `suppression_map.json` — content-level guards that may forbid emission for specific slots.

**Identity & manifest coupling (MUST).**

* Define `pack_sha` as the SHA-256 of the canonical pack manifest bytes.

* List all pack files in the freeze manifest; any governed byte change (in a pack or its listing) bumps the release (`release_id`).

**Canonicalization discipline (MUST).**  
 Files are UTF-8 JSON, LF-terminated (exactly one trailing `\n`), with canonical key ordering. Schema-level constraints (for example, `additionalProperties:false`) are owned in PF12.

**Evidence & indices (MUST).**

* Ship sibling identities (for example, `*.sha256`) and acceptance logs/examples as required by title.

* Update the human Evidence Index `docs/evidence/INDEX.json`, the hash sentinel `docs/evidence/INDEX.sha256`, and the machine mirror `artifacts/evidence_index.jsonl` in the same PR.

* The mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, one trailing LF), rejects unknown keys, and each record includes `discovered_physical_path` and a `proof_anchor` to a path-proof stored alongside the artifact. (Mirror schema lives in PF12.)

**Acceptance (names-only; enforcement lives elsewhere).**  
 NARR\_KEYS\_OK · NARR\_TEMPLATES\_OK · NARR\_PACKS\_IN\_MANIFEST\_OK · NARR\_PACK\_SHA\_OK · EVIDENCE\_INDEX\_UPDATED\_OK.

**Routing (titles-only).**

* PF12 — Schemas & Artifacts: pack schema/manifest; evidence index/mirror conventions.

* PF05 — CLI/API: public/CLI payload bytes & routes (no duplication here).

* PF04 — Governance: transport policy (ETag/HEAD/304; writers/errors). PF17 does not restate header matrices.

  ---

  ## **4.2 pack\_sha & release\_id Linkage (freeze coupling; echo in responses/sidecars) \[Canon\]**

**Identity (`pack_sha`).**  
 Define `pack_sha = sha256(canonical pack manifest)`. Narrative pack files are manifest-listed; the manifest is the source of truth for `pack_sha`.

**Freeze coupling (`release_id`).**  
 Because packs are manifest-listed, any governed byte change (pack or listing) bumps the freeze `release_id` (lowercase 64-hex).

**Echo for provenance (responses/sidecars).**  
 Composer responses echo `pack_sha` (and `composition_id`) for both Text and Suppressed outcomes; CLI/admin sidecars may include the same identifiers for audit evidence. (Byte contracts live in PF05; PF17 remains contract-free.)

**Validation rules (names-only).**  
 `pack_sha` and `release_id` are lowercase 64-hex; inputs that do not match fail closed (suppressed/conflict).

**Evidence parity (names-only).**  
 Sibling identities and acceptance records ship with the change; update the human index \+ hash sentinel and machine mirror in the same PR (mirror hygiene per PF12/PF06).

**Routing (titles-only).**

* PF12 — Schemas & Artifacts: pack schema/manifest; evidence index conventions.

* PF05 — CLI/API: response/sidecar byte contracts (ids in outputs).

* PF04 — Governance: transport (ETag/HEAD/304; writers+errors).

**Runtime (titles-only).**  
 Sealed narratives packs are served from `/narratives/<pack_sha>/…`. Identity binding is to the canonical bytes of `catalog/narratives/manifest.json`. Loader/mount behavior is referenced here by title only (PF02/PF12).

---

## **4.3 Evidence Index (machine JSONL \+ human index) — same-PR parity requirement \[Canon\]**

**Dual index (MUST).**

* **Machine mirror:** `artifacts/evidence_index.jsonl` — one JSON object per line per shipped artifact (packs, identities, examples, acceptance logs); canonical JSONL (UTF-8, sorted keys, compact, one trailing LF); unknown keys rejected; each record includes `discovered_physical_path` and a `proof_anchor` to a path-proof file stored alongside the artifact.

* **Human index:** `docs/evidence/INDEX.json` — mirrors the same artifacts by title/path; updated in the same PR as the machine JSONL; guarded by `docs/evidence/INDEX.sha256` (merge-gating).

**Minimum JSONL record (route by title).**  
 PF12 owns the canonical field set. At minimum, the record includes artifact identity and provenance fields (for example, `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`). PF17 does not duplicate the schema; route to PF12.

**What must be indexed (non-exhaustive).**

* Pack files under `catalog/narratives/` (for example, `keys.json`, `templates.json`, `palettes.json`, `suppression_map.json`) and their sibling `*.sha256`.

* Examples and acceptance outputs (for example, sample compositions; acceptance logs).

**Evidence discipline (MUST).**

* **Canonicalization:** machine JSONL lines use canonical JSON; files are LF-only with exactly one trailing `\n`.

* **Keys-only logs:** never include narrative text; logs/sidecars may include ids (`pack_sha`, `composition_id`, `release_id`).

* **Provenance echo:** composer responses (text or suppressed) echo `pack_sha` (and `composition_id`) so artifacts can be traced back to packs/releases.

**Acceptance (names-only; enforcement lives elsewhere).**  
 EVIDENCE\_INDEX\_UPDATED\_OK · EVIDENCE\_INDEX\_CANONICAL\_JSON\_OK · EVIDENCE\_INDEX\_ONE\_LF\_OK (and mirror unknown-key/proof\_anchor checks per PF12/PF06).

**Routing (titles-only).**

* PF12 — Schemas & Artifacts: machine mirror schema, canonicalization, Evidence Index conventions.

* PF09 — Build Checklist: ship/no-ship gates for parity and JSONL conformance.

* PF06 — Epic-Process-Guide: PR-first; same-PR Doc-Delta \+ indices.

  ---

  ## **4.4 Narratives coverage (router) \[Canon\]**

**Artifact (titles-only).**  
 The router coverage artifact is locked to **10 categories × 4 bands**:  
 `audit/gates/narratives/keys_10x4.table.json`.

**Purpose.**  
 Names-only coverage proof for the keys registry (shared\_key and personal\_key present per row).

**Acceptance (names-only).**  
 `NARR_REGISTRY_CLOSURE_OK`.

**Routing (titles-only).**  
 Evidence listing and indexing live in PF12; gates live in PF09.

# **Part 5 — Surfaces (titles-only)**

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

**Routing (titles-only).**

* PF05 — CLI/API: flag names, stdout/sidecar contracts, and any endpoint coupling.

* PF04 — Governance: A7 transport behavior mirrored in CLI proofs (e.g., HEAD/304 parity where applicable).

* PF12 — Schemas & Artifacts: Evidence Index JSONL conventions and canonicalization rules.

* PF06 — Epic-Process-Guide: PR-first; Doc-Delta \+ indices in the same PR.

**Acceptance (names-only; enforcement in PF14/PF09).**

CLI\_PREVIEW\_BYTES\_EQ\_EMITTER\_OK · CLI\_PREVIEW\_SUPPRESSION\_PARITY\_OK · CLI\_SIDECAR\_IDS\_ONLY\_OK · EVIDENCE\_INDEX\_UPDATED\_OK · MIRROR\_CANONICAL\_JSONL\_OK · MIRROR\_UNKNOWN\_KEYS\_REJECTED\_OK · LF\_NORMALIZATION\_OK · **CLI\_PREVIEW\_ENABLED\_OK** · **CLI\_PREVIEW\_INDEXED\_OK**

---

# **Part 6 — Tests & Acceptance (names-only; enforcement in PF14/PF09/PF04)**

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

**Status.** Canon. These are Aux transport acceptance **names**; authoritative A7 rules live in **PF04 — Governance**, endpoint bytes live in **PF05**, tests in **PF14**, and gates in **PF09** (titles-only). *Supersession:* later PF10 addenda override earlier guidance.

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

  # Part 7 — Variety Without Randomness (titles-only; \[Speculative\]) — 

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

## **Part 8 — Security, Privacy & Ops (titles-only; \[Canon\]) — REPLACE WHOLE PART**

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


## **Part 9 — Rollout & Gating (when adopted)**

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

# **Appendices (informative; titles-only homes in PF12/PF05)**

## **A. Minimal schema stubs (request/response; pack manifest) — route canonical homes to PF12 \[Informative stubs\]**

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

## **B. Example artifacts (compose\_examples, identities, acceptance tokens file) — samples only \[Informative stubs\]**

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

# C. Copywriter Templates

Here’s a **clean, copy-and-paste template pack** that can be used to request and then update deliverables from a copywriter session. It’s designed to be **unambiguous, lint-ready**, and easy for Codex/IA to act on. There are two parts:

1. **New Request (Intake)** — to kick off a session and gather fresh narratives

2. **Update (PATCH)** — to revise, add, or remove specific items after the session

I’m also including a **review checklist** and a **one-liner handoff** to Codex so your operator can move immediately without asking you follow-ups.

---

## C. 1 New Request — Copywriter Intake Template (NIB-style)

Use this template to request a new batch. Paste it into the session/chat as-is and fill the blanks.

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

Use this to fix specific lines or add/remove after a session. Keep it surgical.

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

Put this under the copywriter’s response so the operator can act without questions.

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

For quick asks in a thread — Codex can still ingest this.

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

