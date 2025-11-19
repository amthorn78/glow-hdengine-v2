# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF04-Canon-HDE-Governance

**Version:** v1.4

**Status:** Canon

**Effective date:** 2025-11-17  
**Last Update Gate:** BN 7.1 Drain

## **0.2 Scope \[Required-Now\]**

This document defines governance, validation, and operational policy for the Glow HD Engine. It owns the acceptance gates (A3 / A4 / A7), evidence and release discipline, SAFE-rails posture, logging & privacy requirements, and the public resonance posture (Reader v1 is bands-only, numeric-free; SR-only alpha=1.0; hysteresis=1 is armed for future XR and not exposed).

Supersession (PF10 addenda). PF10 is living; when multiple numbered addenda exist, the later number supersedes earlier guidance. This document integrates the latest addenda and routes by title only to single homes (no version numbers).

Ownership boundaries (titles-only routing). • Transport & ops policy live here. A7 invariants, cache & writers policy, conditional rules, parity requirements, refusal posture, the Aux-suppression carve-out, and the /internal/version ops surface are governed in this document. Exact wire bytes / presenter / CLI flows live in HDE-CLI-API-Vendor-Ref. • Math & algorithms (composite, scoring, bands, primitives) live in HDE-Math-Spec. • Schemas & pack/manifest/canonical JSON live in HDE-Schemas & Artifacts — includes catalog/manifest.json for release\_id, canonical JSON rules (UTF-8 no BOM, ASCII-sorted keys, compact, one trailing LF; arrays-as-sets deduped & ASCII-sorted), and the machine-mirror schema & ordering. Run all byte checks under LC\_ALL=C, TZ=UTC. • Architecture references live in HDE Architecture. • Endpoint Catalog (JSON success) — single proof surface for A7. The Catalog is internal-only and env-gated per entry; entries not gated for prod are unreachable in production. A7 transport proofs must run on a Catalog JSON success route (titles-only; path-agnostic). The /internal/version ops surface is excluded and governed in §10.5. A headers-only env-gate proof is required to demonstrate non-prod entries are unreachable in prod. **For EPIC-010, Aux HEAD and 304 are explicitly out of scope; A7 proofs remain Catalog JSON success only.**

Single homes. • Token roster. All governance tokens are listed once in §2.0 Acceptance Tokens; other sections reference §2.0 and do not restate token lists. • Evidence Index (PF12 single home). PF12 §8.6 is the single home for evidence titles/paths, the human Evidence Index (docs/evidence/INDEX.json) and its hash sentinel, and the machine JSONL mirror (artifacts/evidence\_index.jsonl). Updates must land in the same PR as artifact changes. PF12 governs: records-only JSONL, one trailing LF, unknown-key rejection, ASCII field order, sort-before-write, single mirror file, and required proof\_anchor path-proofs. (PF04 Appendix D may list required titles only; PF12 remains the single home for the index and mirror.)

## **0.3 Tagging convention**

Each section is tagged to show implementation status:

* \[Implemented\] — verified in repo and enforced by tests.  
* \[Required-Now\] — required for the current build or acceptance gates.  
* \[Speculative\] — design accepted for future release; not yet wired.  
* \[OPEN\] — unresolved or gated pending Doc-Delta review.

  ## **0.4 Change policy**

* Single homes; no duplication. Math and Architecture bytes are not restated here; transport bytes remain in CLI/API/Vendor-Ref; artifacts & mirror are owned by PF12.  
* **Governed paths only.** Evidence must live under governed repo paths (artifacts/**, docs/**); transient generator paths are disallowed; mirror entries pointing to non-governed paths **fail CI**.  
* Determinism first. Any change that affects byte identity (serializer path, schema keys, A7 headers) must include updated parity and idempotence evidence.  
* Doc-Delta discipline. All normative edits (math/public/acceptance/rails) require a Doc-Delta entry: scope, affected sections, acceptance impact, evidence updates, and freeze-pack effect.  
* Evidence synchronization (PR-first). When any golden or artifact path changes, Appendix D — Evidence Index must be updated in the same PR/commit that changes those items, with a matching entry in §9 Change Management — Doc-Delta Hooks. Process ownership for this requirement lives in PF06-Canon-Epic-Process-Guide.  
* Mirror hygiene (merge-blocking). The machine mirror must be canonical JSONL (one trailing LF, unknown-keys rejected); each record must include a proof\_anchor pointing to a path-proof stored alongside the artifact. (Field order and sort/join details live in PF12; this doc references policy only.)

**Editorial vs normative.** Stylistic or non-functional rewordings need not be logged; any change that modifies bytes, tests, or acceptance criteria must be logged.

---

# **1\. Purpose & Single-Home Governance \[Required-Now\]**

## **1.1 Purpose \[Required-Now\]**

This governance document defines how the HD Engine is built, validated, and released under explicit Epic gates. Each Epic functions as a governance gate: a bounded set of features and acceptance tests that must be fully implemented, validated, and evidenced before the next Epic begins. Governance, validation, and operations are inseparable—an Epic closes only when its governance and evidence gates pass. **Supersession rule:** where lettered addenda conflict, the later addendum supersedes the earlier; this document integrates the latest positions.

**This document owns**

* **Acceptance gates (A-gates and Epic gates).**

  * **A3 / A4 / A7** enforce determinism, Reader↔CLI parity, and transport correctness.  
  * Every Epic applies the same internal criteria: **AB↔BA parity**, **two-run identity**, **canonical JSON** discipline, and **A7 transport** compliance.  
  * Governance and testing during an Epic use the **same binary proofs** required for release acceptance.  
* **Reader transport and A7 policy.** Governs public transport behavior (headers, conditional delivery, caching). **Single proof surface:** A7 proofs run on a **Catalog JSON success** route (see Endpoint Catalog in PF05); the Catalog is **internal-only** and **env-gated** per entry, and entries not gated for prod are **unreachable in production**. `/internal/version` is **ops-only and excluded**. Required posture includes:

  * strong **quoted ETag** on 200;  
  * `Vary: Authorization, Accept-Encoding`;  
  * `HEAD 200` with validator parity and `Content-Length == len(identity 200 body)`;  
  * **304 only after 200**, with **no body**, and **omit `Content-Type` and `Content-Length`**;  
  * writers/errors `Cache-Control: no-store` and **no ETag**;  
  * **POST non-conditional**;  
  * **encoding invariance** (identity stable across accepted `Accept-Encoding`).  
* **Rails and environments (vendor posture).** **SAFE-rails** model for vendor HTTP: default **closed**, explicit open conditions, deterministic refusal semantics, and non-PII observability.

* **Public resonance posture (Reader v1).** Public surface is **bands-only, numeric-free**; resonance is **SR-only** (`alpha=1.0`); **`hysteresis=1`** is armed for future XR and is not exposed. Any XR diagnostics, if supported, are **CLI-only** behind an admin guard (never on Reader 200).

* **Operations and evidence.** Required evidence classes (parity, idempotence, transport, rails, band-edge, constants), CI hygiene (grep-guards, LF/encoding checks), SLO posture, and the **Evidence Index single-home rule**. Index updates must land **in the same PR** as the artifacts.

* **Release discipline.** Manages freeze-pack identity (`release_id`), pointer-flip and rollback, drift checks. **Any frozen-math or manifest canonical-bytes change yields a new `release_id`** (pack manifest is canonical JSON with `root:"catalog/"`, `version`, `built_at_utc`, and `files:[{path,sha256,size}]`).

* **Security and privacy.** Enforces the **numeric-free public covenant**, keys-only logging, and **no secrets/PII in logs**; labels and correlation IDs remain bounded and deterministic.

* **Change management.** Defines the **Doc-Delta** workflow (scope, targets, acceptance, evidence, freeze-pack impact) and mandates that every normative change updates the **Evidence Index** in the same commit.

**Single-home routing (titles-only)**

* Mathematical rules (composite, scoring, banding, preimage), pack constants, and category catalogs: **HDE-Math-Spec** and **HDE-Schemas & Artifacts**.  
* Architectural boundaries: **HDE Architecture**.  
* Operational governance and Epic acceptance gates: **here**. Exact wire bytes / presenter / CLI flows: **HDE-CLI-API-Vendor-Ref**. **No duplication** of math or serializer bytes in this document.  
  ---

  ## **1.2 Single homes & routing \[Required-Now\]**

* **Ownership (this doc).** Governance owns operational and transport bytes for the HD Engine: A-gates (acceptance policy), Reader transport (headers, conditional delivery, caching), rails posture (enable/disable vendor HTTP), logging/privacy, bench/SLO, release/pointer-flip, and evidence/CI hygiene.

* **Titles-only routing (no duplication).** Mathematical rules (e.g., scoring, thresholds, fixed-point/rounding, preimage definition) and architectural boundaries (engine/adapter/presenter responsibilities) are referenced by title only from **HDE-Math-Spec** and **HDE Architecture**; they are not restated here.

* **Aux Narrative routing note.** Aux Narrative payload and route bytes (examples, endpoint bytes, CLI admin flags) are documented in **HDE-CLI-API-Vendor-Ref**; this document owns the acceptance matrices and policy carve-outs only (e.g., suppression posture).

* **Single homes, single emitter.** Transport bytes and governance processes live here; the canonical serializer/emitter rules and public payload schema are owned in their respective homes and referenced by title only.

* **Change discipline.** If a change touches Math or Architecture, it must be made in that home and routed here via Doc-Delta; if a change alters transport/ops, it lands here with updated evidence and pointers, never by duplicating content across documents.

* **Auditability.** All references to external homes are titles/anchors only; proofs (goldens, scripts, snapshots) are indexed under **Appendix D: Evidence Index** and kept in sync with repo changes.

  ---

# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**

---

## 2.0 Acceptance Tokens (single-home roster) \[Required-Now\] 

Single home for governance tokens. This roster centralizes token semantics; the bytes and tests live elsewhere and are referenced by title only. Other sections must reference §2.0 and must not restate token lists. Supersession: PF10 uses numbered addenda; the later number governs. Case-sensitive.

### **2.0.1 Determinism & identity**

* TWO\_RUN\_IDENTITY\_OK — Two serializations of the same inputs produce identical bytes. (Owned: HDE Math Spec; Mechanics Guide; Evidence & Artifacts)  
* COMPOSITE\_ABBA\_IDENTITY\_OK — AB↔BA fingerprint byte-equality (no vendor flags in composite). (Owned: HDE Math Spec; Evidence & Artifacts)  
* JSON\_CANONICAL\_CHECK\_OK — Canonical JSON everywhere: UTF-8 (no BOM), sorted keys, compact, exactly one trailing LF; arrays-as-sets. (Owned: Mechanics Guide; Evidence & Artifacts)  
* PREIMAGE\_RECOMPUTE\_OK — Strip idempotence\_hash, canonicalize preimage, sha256 matches published. (Owned: HDE Math Spec; Evidence & Artifacts)

### **2.0.2 Internal-ops identity (/internal/version)**

* INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK — GET 200 uses application/json; charset=utf-8. (Owned: Governance; Mechanics Guide)  
* INTERNAL\_VERSION\_HEAD\_PARITY\_OK — HEAD 200 mirrors GET validators (no body). (Owned: Governance; Mechanics Guide)  
* INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK — If-None-Match / If-Modified-Since ignored → 200 (never 304). (Owned: Governance; Mechanics Guide)  
* INTERNAL\_VERSION\_NO\_ETAG\_OK — No ETag on GET/HEAD. (Owned: Governance; Build Notes — Prod QA)  
* INTERNAL\_VERSION\_NO\_STORE\_OK — Cache-Control: no-store on GET/HEAD. (Owned: Governance; Build Notes — Prod QA)

Naming cleanup: The INTVER\_\* aliases are deprecated in favor of INTERNAL\_VERSION\_\*. Use only the canonical names above going forward.

### **2.0.3 Reader A7 (Catalog JSON success; prove on the Endpoint Catalog)**

* ENDPOINTS\_CATALOG\_OK — Catalog of JSON success routes is present (titles-only in CLI/API Vendor Ref). (Owned: CLI/API Vendor Ref)  
* ENDPOINTS\_CATALOG\_INTERNAL\_OK — Catalog is internal-only; not a client contract. (Owned: Governance; CLI/API Vendor Ref)  
* ENDPOINTS\_CATALOG\_ENV\_GATE\_OK — Each entry declares an env gate; non-prod entries are unreachable in prod. (Owned: Governance; CLI/API Vendor Ref)  
* A7\_GET\_QUOTED\_ETAG\_OK — GET 200 has strong, quoted ETag (identity over LF-terminated body; pre-compression). (Owned: Governance; CLI/API Vendor Ref)  
* A7\_HEAD\_PARITY\_OK — HEAD 200 mirrors 200 validators (no body). (Owned: Governance; CLI/API Vendor Ref)  
* A7\_304\_OMITS\_CT\_CL\_OK — 304 only after prior 200; omit both Content-Type and Content-Length. (Owned: Governance; CLI/API Vendor Ref)  
* A7\_ENCODING\_INVARIANCE\_OK — For the same canonical body, identity (ETag) and effective Content-Length are stable across accepted encodings. (Owned: Governance; CLI/API Vendor Ref)  
* A7\_VARY\_AUTH\_AE\_OK — Vary: Authorization, Accept-Encoding present. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_200\_CTYPE\_JSON\_UTF8\_OK — application/json; charset=utf-8 on 200\. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_200\_CACHECTL\_OK — Cache-Control on 200/HEAD is policy-compliant. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_VARY\_ACCEPT\_ENCODING\_OK — Vary includes Accept-Encoding. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_VARY\_AUTHORIZATION\_OK — Vary includes Authorization. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_304\_NO\_CL\_OK — 304 omits Content-Length. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_304\_NO\_CTYPE\_OK — 304 omits Content-Type. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_HEAD\_ETAG\_MATCH\_OK — HEAD validators (incl. ETag) match GET. (Owned: Governance; CLI/API Vendor Ref)  
* READER\_HEAD\_CL\_MATCH\_OK — HEAD Content-Length equals identity 200 body length. (Owned: Governance; CLI/API Vendor Ref)  
* A7\_TRANSPORT\_PROOF\_OK — Capture one full A7 proof set for a cataloged route. (Owned: CLI/API Vendor Ref; Evidence & Artifacts)

#### Equivalence notes (titles-only).

* A7\_304\_OMITS\_CT\_CL\_OK ≡ (READER\_304\_NO\_CTYPE\_OK ∧ READER\_304\_NO\_CL\_OK)  
* A7\_VARY\_AUTH\_AE\_OK ≡ (READER\_VARY\_AUTHORIZATION\_OK ∧ READER\_VARY\_ACCEPT\_ENCODING\_OK)

### **2.0.4 Aux Narrative transport (success \+ suppression; prove on Endpoint Catalog)**

* Tokens (Aux surface; names-only)  
  * NARR\_200\_TEXT\_OK  
  * NARR\_SUPPRESSED\_NO\_ETAG\_OK  
  * NARR\_VARY\_AUTH\_AE\_OK  
  * AUX\_CANON\_ALIAS\_PARITY\_OK

  * (Notes: these replace legacy AUX\_\* names; one-release grace for AUX\_\* may be handled in PF09. Aux HEAD/304 tokens are out-of-scope for EPIC-010; A7 remains Catalog-only.)

### **2.0.5 Writers / refusal & ops posture (rails)**

* WRITERS\_OPTIONS\_204\_NO\_BODY\_OK — Writers’ OPTIONS returns 204 (no body). Never emit body/ETag/Vary/compression; HEAD 405 remains strict with Content-Length: 0\. (Owned: Governance)  
* ERROR\_CTYPE\_JSON\_UTF8\_OK — Refusal responses use application/json; charset=utf-8. (Owned: Governance)  
* NO\_CONTENT\_ENCODING\_OK — No Content-Encoding on refusal. (Owned: Governance)  
* NO\_EXTERNAL\_IO\_ON\_REFUSAL\_OK — Refusal path performs no external I/O. (Owned: Governance)  
* PF04\_LOG\_ALLOWLIST\_009\_OK — Refusal logs are keys-only with the allow-list {at, route, status, duration\_ms, idempotence\_hash, release\_id}. (Owned: Governance)  
* REFUSAL\_ROUTE\_PINNED\_OK — Canonical refusal probe route is /ops/rails/refusal (GET/POST equivalent; OPTIONS/HEAD per matrix). (Owned: Governance)

## **Refusal proof artifact (shape & linkage)**

* OPS\_REFUSAL\_FILE\_FORMAT\_OK  
* OPS\_REFUSAL\_HEADERS\_OK  
* OPS\_REFUSAL\_BODY\_OK  
* OPS\_REFUSAL\_MIRROR\_LINK\_OK

### **2.0.6 Evidence & indexing**

* EVIDENCE\_INDEX\_UPDATED\_OK — Human Evidence Index updated in the same change as artifacts. (Owned: Governance; Evidence & Artifacts)  
* EVIDENCE\_INDEX\_MIRROR\_OK — Machine JSONL mirror (records-only; sorted keys; one LF) present and valid. (Owned: Evidence & Artifacts)  
* EVIDENCE\_PATHS\_VALIDATED\_OK — Each record has a discovered path plus path-proof; human↔machine parity is 1:1. (Owned: Governance; Evidence & Artifacts)  
* EVIDENCE\_PATH\_PROOFS\_OK — Path-proofs present and linked. (Owned: Evidence & Artifacts)  
* CI\_CHECK\_FINAL\_LF\_OK — All evidence artifacts & mirror lines are LF-terminated (exactly one). (Owned: Evidence & Artifacts; Build Notes)  
* CI\_CHECK\_MIRROR\_SCHEMA\_OK — Mirror records pass schema/role/field-order checks (unknown-key rejection). (Owned: Evidence & Artifacts; Build Notes)  
* EVIDENCE\_INDEX\_HASH\_OK — Human index hash sentinel present and gating merges. (Owned: Governance; Evidence & Artifacts)  
* \+SNAPSHOT\_HEADER\_LOWERCASE\_OK (Normative header-name lowercasing for stored snapshots; PF12 owns the rule and schema.)

### **2.0.7 Freeze-Pack & manifest**

* PACK\_ROOT\_PINNED\_OK — root: "catalog/" pinned. (Owned: Evidence & Artifacts — Manifest)  
* PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK — Root manifest does not list itself or sidecars. (Owned: Evidence & Artifacts — Manifest)  
* MANIFEST\_SHA256\_HEX64\_OK — Each entry sha256 is lowercase 64-hex of canonical bytes. (Owned: Evidence & Artifacts — Manifest)  
* MANIFEST\_FILE\_EXISTS\_OK — Each listed file exists at the path. (Owned: Evidence & Artifacts — Manifest)  
* MANIFEST\_PATH\_ASCII\_SORT\_OK — files\[\] ASCII-sorted by path. (Owned: Evidence & Artifacts — Manifest)  
* RELEASE\_ID\_FROM\_MANIFEST\_OK — release\_id derives only from the manifest. (Owned: Evidence & Artifacts — Manifest)  
* RELEASE\_ID\_RECOMPUTE\_OK — sha256(canonical\_manifest\_bytes) matches recompute. (Owned: Evidence & Artifacts — Manifest)  
* TWO\_RUN\_IDENTITY\_OK — Two-run identity of the recompute step. (Owned: Evidence & Artifacts — Manifest)

### **2.0.8 CLI/SDK parity harness**

* \- CLI\_READER\_EMITTER\_PARITY\_OK  
* \+ CLI\_READER\_PARITY\_OK  
* \+ CLI\_PREVIEW\_ENABLED\_OK  
* \+ CLI\_PREVIEW\_INDEXED\_OK

(CLI admin preview is enabled for admins and uses the same emitter as Aux; evidence is required and indexed.)

### 2.0.9 Database posture

DB\_CONN\_ENV\_OK — Selection order `DATABASE_URL → DB_BRIDGE_URL → typed error`. (Owned: Glow Infrastructure; Mechanics Guide)  
 DB\_RUNTIME\_SEARCH\_PATH\_OK — Runtime `search_path = hde, public` (in that order). (Owned: Glow Infrastructure; Mechanics Guide; Evidence & Artifacts)  
 DB\_ROLE\_OK — Least-privilege runtime grants. (Owned: Glow Infrastructure; Evidence & Artifacts)  
 DB\_SCHEMA\_FINGERPRINT\_OK — Canonical DDL fingerprint captured. (Owned: Evidence & Artifacts)  
 DB\_BOUNDARY\_VIEW\_OK — Boundary view (`public.hde_body_graphs_current`) is read-only; no rules/triggers allow writes outside the `hde` schema. (Owned: Governance; Glow Infrastructure; Evidence & Artifacts)  
 DB\_WRITERS\_ISOLATED\_OK — Only Engine roles can mutate `hde.*`; backend roles and other consumers have no DML rights on `hde` data (write isolation enforced). (Owned: Governance; Glow Infrastructure; Evidence & Artifacts)  
 DEV\_DB\_BRIDGE\_FALLBACK\_OK — In dev, when `DATABASE_URL` is unusable, fall back to `DB_BRIDGE_URL`; dev connectivity snapshot present; keys-only diagnostics; no secrets. (Owned: Governance; Glow Infrastructure; Evidence & Artifacts)  
 PROD\_CONN\_SINGLE\_SOURCE\_OK — In prod, connection source is single and explicit (no bridge fallback). (Owned: Governance; Glow Infrastructure)

### 2.0.10 Env / rails / infra

ENV\_PORT\_REQUIRED\_OK — Runtime `PORT` is present and bound. (Owned: Glow Infrastructure)  
 SERVICE\_START\_CMD\_CAPTURED\_OK — Production start command captured (bytes \+ sha256). (Owned: Glow Infrastructure; Evidence & Artifacts)  
 GUNICORN\_APP\_FACTORY\_OK — Adapter entry `adapter.factory:create_app()` binds `$PORT`. (Owned: Glow Infrastructure; Evidence & Artifacts)  
 ENV\_RAILS\_POLICY\_OK — Dev/QA may be open; Prod must not depend on rails-open settings; CI/test harness runs default to closed rails. (Owned: Mechanics Guide; Governance)  
 ENV\_LC\_ALL\_C\_OK — All determinism and evidence jobs run with canonical pins `LC_ALL=C`, `LANG=C`, `TZ=UTC` for HDE services and CI (env pins present and enforced). (Owned: Governance; Build Checklist; Mechanics Guide)  
 OBS\_KEYS\_ONLY\_OK — Operational logs are keys-only and secret-free (no payload bodies or header values; secrets redacted), in accordance with Governance logging policy. (Owned: Governance)

### **2.0.11 Catalog hygiene (where applicable)**

* CATALOG\_ORIENTATION\_CANON\_OK — Channel IDs canonical NN-NN (zero-padded, min-first); ASCII ordered. (Owned: Evidence & Artifacts — Catalogs)  
* CATALOG\_DENOMINATORS\_FROZEN\_OK — Pack denominators are present and frozen; no runtime overrides. (Owned: HDE Math Spec; Evidence & Artifacts)  
* FEATURE\_NULL\_DEFAULT\_OK — Default null → 0 unless D3 explicitly overrides. (Owned: HDE Math Spec)  
* BAND\_MAX\_INCLUSIVE\_OK — Bands use inclusive-high thresholds. (Owned: HDE Math Spec)  
* BAND\_EDGE\_GOLDENS\_OK — Goldens at 24/49/74/100 pass. (Owned: HDE Math Spec; Evidence & Artifacts)  
* PREFS\_KEYSET\_10\_OK — Preference keyset is the canonical 10\. (Owned: HDE Math Spec; Governance)

### **2.0.12 Narratives — packs & gate**

* NARR\_PACKS\_IN\_MANIFEST\_OK  
* NARR\_PACK\_SHA\_OK  
* NARR\_PACKS\_CANONICAL\_JSON\_OK  
* NARR\_PACK\_MANIFEST\_OK  
* NARR\_PACK\_IDENTITY\_OK  
* GRACE\_DELIVERABLES\_GATE\_OK

*Naming cleanup:* `CLI_READER_EMITTER_PARITY_OK` is deprecated in favor of `CLI_READER_PARITY_OK`. Keep the legacy token only for historical boards.\*

## **2.1 A3 — Determinism gates \[Required-Now\]**

**Canonical serializer.** All public JSON MUST be emitted by the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact separators (,/:), exactly one trailing LF. Arrays that function as sets MUST be deduplicated and ASCII-sorted.

**Two-step idempotence (preimage recipe).** Build the five-key preimage object (reader\_version, eligible, categories, meta, release\_id) without `idempotence_hash`; serialize canonically to `preimage_bytes`; compute `idempotence_hash = sha256(preimage_bytes)` (lowercase 64-hex); add it; re-serialize canonically for the final bytes.

**Pattern constraints.** `release_id` and `idempotence_hash` MUST match lowercase 64-hex: `^[0-9a-f]{64}$`.

**AB↔BA parity.** Inputs are pair-normalized; for any pair AB and BA, both the Appendix-E composite fingerprint and the final public bytes MUST be byte-identical (including the single LF). Integration channel cases (10/20/34/57 combinations, for example 20-34 vs 20-57) MUST be covered.

**Two-run identity.** Two serializations of the same logical success envelope (same inputs/environment) MUST produce byte-identical output.

**Locale discipline.** All canonicalization and comparisons run under `LC_ALL=C`.

**On-disk equality.** Public outputs MUST match their canonical re-serialization byte-for-byte (no drift between emitted bytes and canonical dumps).

### **Validation gates (binary)**

* Preimage re-check: recompute `sha256(preimage_bytes)` and match the published `idempotence_hash`.  
* AB↔BA compare: byte-compare Appendix-E fingerprints and public outputs for AB vs BA (both must match; include Integration cases).  
* Two-run compare: byte-compare two runs with identical inputs (must match).  
* Serializer hygiene: UTF-8; sorted keys; compact; one LF; no BOM; arrays-as-sets deduped and ASCII-sorted.  
* Pattern check: `release_id`, `idempotence_hash` each match `^[0-9a-f]{64}$`.  
* Canonical re-serialization: emitted bytes equal canonical dumps (file-equals-canon).

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---

## **2.2 A4 — Reader↔CLI parity \[Required-Now\]**

* **Single presenter/emitter.** Reader and CLI MUST call the same emitter to produce success and error bodies; no ad-hoc dumps or parallel “mini-emitters.”  
* **Byte equality.** For identical inputs/environment, CLI stdout and Reader body MUST be byte-identical (including the single LF).  
* **Canonical JSON.** Public bytes are serialized with the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. All checks run under `LC_ALL=C`.  
* **Public resonance posture (v1).** No SR/XR numerics appear on Reader 200\. v1 ships SR-only (alpha \= 1.0); hysteresis \= 1 is armed for future XR and not exposed.

**Schema/shape gates**

1. Success: exactly the six keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*]` are exactly `{ "id", "band" }` (numeric-free; `band ∈ {"Cool","Open","Warm","Glow"}`).  
2. Errors: typed, numeric-free JSON; LF-terminated; no PII.

**Validation gates (binary)**

1. Reader↔CLI compare: byte-compare outputs (must match).  
2. Shape checks: enforce success/error schemas above (reject extras, numerics, or missing fields).  
3. Emitter proof: CI/allowlist shows both surfaces invoke the same emitter symbol.

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---

## **2.3 A7 — Transport tokens \[Required-Now\]**

**Scope.** These rules apply to Reader success endpoints. Proofs MUST be run on an Endpoint Catalog (success JSON) route in **HDE-CLI-API-Vendor-Ref**. Internal-ops `/internal/version` is excluded and governed by §10.5.

* **ETag on 200 (identity of body bytes).** Reader 200 MUST include a strong, quoted ETag. Identity is computed over the final LF-terminated body (canonical JSON per PF-Schemas & Artifacts). Compression does not change the ETag (encoding-invariant).  
* **Cache headers on 200 and HEAD.** `Cache-Control: private, max-age=0, must-revalidate` MUST be present on 200 and HEAD.  
* **304 only after a 200-with-body.** 304 MAY be sent only after a successful 200 has established an ETag. 304 carries no body, omits `Content-Type` and `Content-Length`, and repeats validators from the cached 200\.  
* **HEAD parity.** HEAD returns the same validators as 200 and no body. `Content-Length` equals the identity 200 body length (canonical LF-terminated bytes). `Content-Type` on HEAD equals GET.  
* **Writers and errors: no-store; no ETag.** All writer and error responses MUST include `Cache-Control: no-store` and MUST NOT include an ETag. Error responses MUST include `Content-Type: application/json; charset=utf-8`.  
* **Content-Type on 200\.** Success 200 MUST include `Content-Type: application/json; charset=utf-8`.  
* **Vary policy.** Reader responses MUST set `Vary: Accept-Encoding, Authorization` to prevent cache mixing and prove encoding-invariance separately.  
* **POST is non-conditional.** POST MUST NOT honor conditional validators; treat as non-conditional write/compute.

**Validation gates (binary; prove on a cataloged success endpoint)**

1. 200: strong quoted ETag present; `Cache-Control: private, max-age=0, must-revalidate` present; `Content-Type: application/json; charset=utf-8` present; encoding-invariance proven (same ETag across accepted `Accept-Encoding`).  
2. 304: only after a prior 200; no body; validators mirror 200; omit `Content-Type` and `Content-Length`.  
3. HEAD: validators mirror 200; no body; `Content-Length` matches identity 200 body; `Cache-Control: private, max-age=0, must-revalidate` present; `Content-Type` equals GET.  
4. Writers and errors: `Cache-Control: no-store` present; no ETag; errors include `Content-Type: application/json; charset=utf-8`.  
5. POST: treated as non-conditional (ignore `If-*` conditionals).

*Tokens: see §2.0 Acceptance Tokens (A-gates roster; Reader A7 and READER\_* tokens).\*

# 3\) Rails & Environments (Vendor posture) \[Required-Now\]

## **3.1 SAFE rails default ON \[Required-Now\]**

Default posture by environment.  
 In **development** and **stage** environments, rails are **OPEN by default** (`SAFE_MODE=0`, `ALLOW_NETWORK=1`); vendor HTTP is allowed in these environments unless rails are explicitly closed. In **production**, rails are **CLOSED by default** (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); vendor HTTP is refused unless rails are explicitly opened by ops.

Two-gate rule (both required).  
 Live HTTP is allowed only when **both** `SAFE_MODE=0` **and** `ALLOW_NETWORK=1`. If either gate is not satisfied, vendor HTTP is treated as closed-rails and refused.

No implicit overrides.  
 Reader/CLI **MUST NOT** toggle rails; opening rails is an **operational (env/config) decision**, not a runtime flag. Jobs or sessions that open rails for vendor ingest must do so explicitly via configuration and meet the evidence requirements in this document and in the Epic-Process-Guide.

Determinism while closed.  
 With rails closed, provider code may shape requests (for diagnostics) but **MUST NOT** perform any network I/O (no sockets, DNS, HTTP). It returns a typed refusal (numeric-free JSON; canonical: UTF-8 no BOM, sorted keys, compact, exactly one LF) and logs no secrets. Run checks under `LC_ALL=C`, `TZ=UTC`.

CI/test posture.  
 Rails remain **CLOSED by default** in CI and test harness runs (`SAFE_MODE=1`, `ALLOW_NETWORK=0`). Any CI job that opens rails must pin timeout/retry/backoff policy, remain keys-only in diagnostics, and attach required evidence (including env snapshot and path-proofs) in the same change, as governed by this document and by the Epic-Process-Guide.

---

## **3.2 Refusal semantics (rails closed) \[Required-Now\]**

When rails are closed (i.e., `SAFE_MODE≠0` or `ALLOW_NETWORK≠1`), vendor paths **MUST NOT** open sockets, resolve DNS, or attempt HTTP (no external I/O). This applies to **all** vendor invocations, including manual or CLI requests that explicitly set `source="vendor"`; such attempts **MUST** produce a deterministic typed refusal and **MUST NOT** perform any upstream call.

Headers (ops/error surface).  
 Cache-Control: `no-store` **MUST** be present.  
 Content-Type: `application/json; charset=utf-8` **MUST** be used for the refusal body.  
 No `ETag`, no `Vary`, no `Content-Encoding`.  
 Exactly one blank line between headers and body (see PF12 §8.3.1 for the refusal proof format).

Body (typed, numeric-free).  
 Return a typed error explaining that vendor access is disabled (numeric-free JSON; LF-terminated). Do not echo provider payloads or headers.

Logs (keys-only; no secrets).  
 Logs **MUST NOT** contain API keys/tokens, request/response bodies, or header values.  
 If keys are referenced, they **MUST** be redacted (e.g., `HD-Api-Key: REDACTED`).  
 Labels remain bounded (e.g., `route`, `outcome`, `rails_state`); no PII.

Refusal log allow-list (frozen).  
 Refusal logs are limited to the six-key set: `{ at, route, status, duration_ms, idempotence_hash, release_id }`.  
 (Do not include `retry_after_ms` here; that belongs to 429 evidence only.)

Deterministic shaping (optional).  
 Request shapes (endpoint, headers, body schema) may be computed without sending the request; shaping must be deterministic and order-neutral (AB↔BA).

Canonical probe route.  
 Expose a single refusal probe at `/ops/rails/refusal`:

* `GET`/`POST` → 503 single-file capture (headers → blank line → LF-terminated JSON),

* `OPTIONS` → 204 no body,

* `HEAD` → 405 with `Content-Length: 0`,

* no ETag/Vary/compression.

(Evidence artifact shape lives in PF12 §8.3.1.)

CI posture (must).  
 CI must prove:

* No network I/O occurs under closed rails.

* The typed refusal is produced with the required headers/body.

* Logs are keys-only and secret-free (no payloads/headers).

Tokens (titles-only; see §2.0).  
 `NO_EXTERNAL_IO_ON_REFUSAL_OK` · `ERROR_CTYPE_JSON_UTF8_OK` · `NO_CONTENT_ENCODING_OK` · `PF04_LOG_ALLOWLIST_009_OK` · `REFUSAL_ROUTE_PINNED_OK` · `OPS_REFUSAL_FILE_FORMAT_OK` · `OPS_REFUSAL_HEADERS_OK` · `OPS_REFUSAL_BODY_OK` · `OPS_REFUSAL_MIRROR_LINK_OK`

Routing (titles-only).  
 Transport matrix & writers posture: §10 of this document.  
 Evidence/mirror hygiene (same-PR, canonical JSONL, unknown-key reject, `proof_anchor`): **HDE-Schemas & Artifacts** / **Epic-Process-Guide**.  
 Infrastructure names for admin credentials/rails: **Glow Infrastructure** (names-only).

* 

---

## 3.3 Secrets & env validation \[Required-Now\]

* **Validate against PF12 (names-only allow-list).** Before any vendor action, validate required keys from the PF12 canonical env table (names-only; secrets not printed). Unknown keys **must** be flagged in CI; missing required **must** fail at prod start.  
   **Required (examples):** `HDAPI_BASE_URL` (vendor base URL), `HD_API_KEY` (secret), `GEO_API_KEY` (secret).  
   **Failure posture:** if rails are **open** but any required key is invalid/missing, the provider **MUST refuse** with a typed error; **do not** attempt partial requests or fallbacks.  
* **Redaction rules (keys-only logs).** Never log secrets, request/response bodies, or header values. When secrets are referenced, print **redacted placeholders only** (e.g., `HD-Api-Key: REDACTED`). Labels remain bounded; **no PII**, **no free-text** payloads.  
* **Deterministic diagnostics.** Configuration checks and refusal messages **MUST** be deterministic and order-neutral; **no** locale/time/random dependencies (run under `LC_ALL=C`).  
* **CI checks.** Add tests that (a) **fail fast** on missing/empty env, (b) assert refusal posture with **no network I/O**, and (c) **grep-guard** logs to ensure no secrets or payload bodies appear.

---

## 3.4 Open rails (controlled) \[Required-Now\]

* **Explicit enablement only.** Opening rails is **explicit** (env/config). Reader/CLI behavior and canonical bytes remain **unchanged** (same presenter/emitter; public payload numeric-free).  
* **Pinned network policy (by title).** When open, live calls follow **pinned timeouts, retries, and backoff**; vendor error mapping is **deterministic** and **typed**; **no** payloads/secrets in logs.  
* **Parity & idempotence remain intact.** Enabling rails **must not** change Reader↔CLI parity, **A7 conformance**, or **idempotence** proofs.  
* **Evidence.** Provide **records-only** machine-mirror entries for:  
   (a) **closed-rails refusal** proof,  
   (b) **open-rails conformance** run (with redaction checks), and  
   (c) **env-validator outputs** per environment.  
   *(PF12 single home; same-PR updates apply.)*

**Tokens:** see **§2.0 Acceptance Tokens** (A-gates roster).

---

# **4\) Evidence & Artifacts \[Required-Now\]**

## **4.1 Classes of evidence \[Required-Now\]**

What must be proved for every cut (**binary gates; no partial**). Index all artifacts in **Appendix D: Evidence Index** and keep it synchronized with repo changes. All byte-comparisons and hashes run with **LC\_ALL=C, TZ=UTC**, and **canonical JSON** (UTF-8 no BOM, ASCII-sorted keys, compact, **exactly one LF**; arrays-as-sets are deduped and ASCII-sorted).

### **4.1.1 Parity — Reader↔CLI, AB↔BA, two-run**

* **Reader↔CLI byte identity.** For identical inputs and environment, Reader body and CLI stdout are bit-identical (single presenter/emitter; same `idempotence_hash`; one trailing LF).  
* **AB↔BA identity.** Swapping pair order yields bit-identical bytes (pair normalization in effect). Include AB/BA composite fingerprint cases and a byte-compare log; cover integration channel examples.  
* **Two-run identity.** Two serializations of the same logical invocation produce bit-identical bytes.  
* **Evidence.** Parity runs and goldens; AB/BA and two-run logs; CI byte-diff jobs; **machine-mirror** records (records-only) for each capture.  
* **Tokens.** `CLI_READER_EMITTER_PARITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`.

### **4.1.2 Idempotence recompute — preimage → sha256 → final**

* **Preimage check.** Remove `idempotence_hash`; canonicalize the defined preimage fields (see **HDE Math Spec**); verify `sha256(preimage_bytes) == idempotence_hash`.  
* **Evidence.** Recompute logs and script; env pins recorded (**LC\_ALL=C, TZ=UTC**); mirror records with sha256 and proof.  
* **Tokens.** `PREIMAGE_RECOMPUTE_OK`, `JSON_CANONICAL_CHECK_OK`.

### **4.1.3 A7 transport — validators and conditional delivery**

**Proof surface.** Prove on a **CLI/API/Vendor Ref Endpoint Catalog JSON success** route (titles-only). **/internal/version is excluded.** The Catalog is **internal-only** and **env-gated**; non-prod entries **must be unreachable in prod** (capture a headers-only **env-gate proof**).

* **200\.** Strong, quoted ETag over the LF-terminated body (**encoding-invariant**).  
* **200/HEAD.** `Cache-Control: private, max-age=0, must-revalidate` present.  
* **304\.** Only after a prior 200; **no body**; **omit both `Content-Type` and `Content-Length`**; validators mirror cached 200\.  
* **HEAD.** Validators mirror 200; no body; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
* **Writers/errors.** `Cache-Control: no-store`; **no ETag**; errors include `Content-Type: application/json; charset=utf-8`.  
* **Evidence.** Header snapshots for 200, HEAD, and 304; conditional sequences; **encoding-invariance** check; **Endpoint-Catalog snapshot** and **env-gate proof**; all indexed as records-only in the machine mirror.  
* **Tokens.** `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_ENCODING_INVARIANCE_OK`, `A7_VARY_AUTH_AE_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `READER_HEAD_ETAG_MATCH_OK`, `READER_HEAD_CL_MATCH_OK`, `A7_TRANSPORT_PROOF_OK`.

**Equivalence (titles-only).** `A7_304_OMITS_CT_CL_OK` ≡ (`READER_304_NO_CTYPE_OK` ∧ `READER_304_NO_CL_OK`); `A7_VARY_AUTH_AE_OK` ≡ (`READER_VARY_AUTHORIZATION_OK` ∧ `READER_VARY_ACCEPT_ENCODING_OK`).

### **4.1.4 Rails posture — closed refusal; open conformance**

* **Closed rails (default).** No network I/O; typed, numeric-free refusal; keys-only logs with secrets redacted.  
* **Open rails (controlled).** Pinned timeouts/retries/backoff; deterministic vendor error mapping; logs contain no payloads or secrets; Reader↔CLI parity and idempotence unaffected.  
* **Evidence.** CI job proving closed-rails refusal; integration job proving open-rails conformance; redaction/observability fixtures (records-only).  
* **Tokens.** `ENV_RAILS_POLICY_OK`.

### **4.1.5 Bands — inclusive-high thresholds (by preset)**

* **Boundaries.** Proof goldens at **24/49/74/100**; show \+1 transitions (see **HDE Math Spec**); 100 → Glow.  
* **Evidence.** Band-edge snapshots and diffs; mirror records.  
* **Tokens.** `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`.

### **4.1.6 Pack constants and release identity**

* **Constants pack.** Snapshot of frozen keys (limits, thresholds, resonance inputs as applicable) and hashes.  
* **Manifest and `release_id`.** Canonical manifest capture; recompute log proving `release_id = sha256(canonical_manifest_bytes)`.  
* **Evidence.** Constants snapshot with `.sha256`; manifest and recompute log; mirror records.  
* **Tokens.** `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`.

### **4.1.7 Topology loader — orientation and graph invariants**

* **Orientation.** Channel IDs are min→max, zero-padded **NN-NN**; arrays-as-sets deduped and ASCII-sorted.  
* **Integration invariants.** Only gates **10/20/34/57** have degree \= 3; all others \= 1\. Center-pair multiplicities sum to **36**; fail closed on mismatch.  
* **Evidence.** Orientation demo; degree and multiplicity logs; machine-mirror entries.  
* **Tokens.** `CATALOG_ORIENTATION_CANON_OK` (and related topology tokens in Evidence & Artifacts).

**Pass criteria.** All classes pass (parity, idempotence, A7, rails, bands, pack constants/manifest, topology) with evidence listed in **Appendix D: Evidence Index** and CI gates enabled (grep-guards for ad hoc emitters; LF/encoding checks; A7 cache header and ETag/no-ETag checks).

---

## **4.2 Evidence index rule \[Required-Now\]**

### **4.2.1 Synchronized updates (MUST)**

Whenever any golden, artifact, or script changes, **Appendix D: Evidence Index (human)** and the **machine JSONL mirror** **must** be updated in the **same change**; the Change Log / Doc-Delta must reference the updated items.

### **4.2.2 Single homes and format**

* **Human Index (this doc).** Lives in **Appendix D: Evidence Index**. Canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, **exactly one LF**; arrays-as-sets deduped & ASCII-sorted. Allowed fields per entry: `title` (string), `path` (repo-relative POSIX), optional `sha256` (lowercase 64-hex), optional `size` (bytes). Constraints: `{title, path}` pair is unique; path must be repo-relative, must not be absolute, must not contain `..` segments or duplicate slashes, and must not end with a slash.  
* **Machine mirror (single home in Evidence & Artifacts).** Fixed repo path **`artifacts/evidence_index.jsonl`** with a **records-only JSONL** schema. Each record includes: `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor` (transcript reference \+ on-disk stat). Records are canonical JSON objects (sorted keys, compact), **one per line**, **LF-terminated**.

**Mirror discipline (merge-blocking).**

* **Unknown-key rejection**: CI fails on unknown/missing fields.  
* **ASCII field order** in each record: `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.  
* **Sort-before-write** by (`artifact_key`, `discovered_physical_path`).  
* **Join rule:** `artifact_key` \== human Index title; `discovered_physical_path` \== human Index path.  
* **Path-proof equality:** `proof_anchor` **must equal** the discovered path proof stored alongside the artifact (per-dir `path_proof.txt`).  
* **Single mirror file:** exactly one `artifacts/evidence_index.jsonl` must exist.

### **4.2.3 Parity rule (CI-enforced)**

Human ↔ machine entries **must be 1:1**. CI fails on count or content mismatch, missing files, stale `sha256/size` (when present), or schema violations.

### **4.2.4 Titles and paths only (human index)**

The human Index lists **titles and repository paths only**; no payload bytes or inline data.

### **4.2.5 Single source of truth**

**Appendix D** is the authoritative map for parity, idempotence, A7, rails, bands, topology, and pack/evidence artifacts. CI reads the Index \+ mirror to locate fixtures and scripts and fails if required entries are missing or stale.

### **4.2.6 Tokens**

See **§2.0 Acceptance Tokens**: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, **`CI_CHECK_FINAL_LF_OK`**, **`CI_CHECK_MIRROR_SCHEMA_OK`**, **`EVIDENCE_INDEX_HASH_OK`**.

---

## **4.3 CI hygiene \[Required-Now\]**

### **4.3.1 Grep guards (fail fast)**

* **No ad-hoc dumps/emitters.** Fail any public path containing `json.dumps(` (or equivalent) or a non-presenter emitter; allow-list the single presenter/emitter symbol.  
* **No payload/secret logging.** Fail on patterns that indicate request/response bodies, header values, or keys in logs; secrets must be redacted.

### **4.3.2 Encoding and termination checks**

* **UTF-8 only**, BOM/ANSI-free.  
* **Exactly one LF** at end of all success and error bodies.  
* **Header snapshot normalization.** JSON with **lower-cased header names**, compact separators, **one LF**; **values remain verbatim**.  
  * Acceptance (titles-only): SNAPSHOT\_HEADER\_LOWERCASE\_OK  
* **Canonical re-serialization compare.** Enforce sorted keys and compact separators by comparing to canonical dumps.  
* **Arrays-as-sets.** Where arrays represent sets, dedupe and ASCII-sort before hashing/compare.

### **4.3.3 Schema and shape gates**

* **Success.** Six keys exactly; `categories[*]` are `{id, band}` only (numeric-free).  
* **Errors.** Typed, numeric-free JSON (no PII), LF-terminated.

### **4.3.4 Parity and identity jobs**

* Reader↔CLI byte equality for identical inputs/environment (single presenter).  
* AB↔BA byte equality (pair normalization) — include integration channel cases.  
* Two-run identity (repeat run produces identical bytes).  
* Idempotence re-check. Recompute `sha256(preimage_bytes)` (preimage fields per HDE Math Spec) equals published `idempotence_hash`.

### **4.3.5 A7 transport checks (Catalog success endpoint)**

* **200\.** Strong, quoted ETag present; `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304\.** Only after a prior 200-with-body; **no body**; validators mirror 200; **omit both `Content-Type` and `Content-Length`**.  
* **HEAD parity.** Validators mirror 200; no body; `Content-Length` matches identity 200 body; `Content-Type` equals GET.  
* **Writers and errors.** `Cache-Control: no-store`; **no ETag**; errors include `Content-Type: application/json; charset=utf-8`.  
* **Encoding invariance.** For the same body, identity (ETag) is stable across Accept-Encoding.  
* **POST non-conditional.** Ignore If-\* conditionals for POST.  
* **Env-gate proof.** Capture a headers-only proof that non-prod entries are unreachable in prod on the Endpoint Catalog route.

### **4.3.6 Rails posture jobs**

* **Closed rails (default).** Prove no network I/O, typed refusal, keys-only logs with secrets redacted.  
* **Open rails (integration profile).** Prove pinned timeouts/retries/backoff and deterministic vendor error mapping; logs contain no payloads or secrets; public bytes unchanged (parity/idempotence intact).

### **4.3.7 Topology integrity jobs**

* ID normalization demo. Verify high→low normalized to min→max **NN-NN** in orientation demo.  
* Integration degree check. Gates **10/20/34/57** ⇒ degree 3; all other gates ⇒ degree 1\.  
* Center-pair multiplicity. Unordered center-pair counts sum to **36**.

### **4.3.8 Environment pins**

Record **LC\_ALL=C, LANG=C, TZ=UTC** for all jobs; **fail if missing**.

### **4.3.9 Evidence Index enforcement**

* **Same-change updates (MUST).** Fail the pipeline if **Appendix D** (human) and the **machine JSONL mirror** are not updated in the **same commit/PR** when any golden/artifact/script changes.  
* **Human↔machine parity.** Require **1:1 membership**; fail on mismatch.  
* **Path-proofs.** Every mirror record must include a discovered physical path and a proof (transcript anchor \+ on-disk stat); **fail if absent**.  
* **Single mirror file.** Fail if more than one `artifacts/evidence_index.jsonl` exists or if any record is non-canonical (unsorted keys, wrong line ending, **unknown keys**, missing/unequal `proof_anchor`).

**Tokens:** see **§2.0**.

---

# **5\) Release & Freeze-Pack Discipline \[Required-Now\]**

## **5.1 Release identity (manifest → release\_id) \[Required-Now\]**

**Definition (normative).** `release_id` is the lowercase 64-hex SHA-256 of the canonical freeze-pack manifest. It identifies exactly which frozen math inputs produced the public bytes for a release.

**Canonical manifest (construction)**

* **Top-level fields (required).** A single JSON object with:  
   `root: "catalog/"`, `version` (pack semver), `built_at_utc` (UTC ISO-8601 with `Z`), and  
   `files: [{path, sha256, size}]`. Do not self-list the manifest.  
* **Enumerate frozen math inputs (titles and paths only).** List every governed math artifact used by the engine: closed category set and order, band maxima (inclusive-high), topology catalogs (centers, gates, channels), **Motor→Throat sets** (and other denominators where applicable), preset catalog (if used), constants pack (limits, thresholds, resonance inputs as applicable), and any other normative math tables referenced by this governance. Transport and ops bytes are not part of the pack.  
* **Per-entry identity.** For each entry compute `sha256(canonical_bytes(entry))` and record:  
   `path` (repo-relative POSIX path under `catalog/`), `sha256` (lowercase 64-hex), `size` (integer byte length of the same canonical bytes).  
* **Canonical storage and hashing.** The manifest itself is stored canonically (see **Evidence & Artifacts**): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. Compute  
   `release_id = sha256(canonical_bytes("catalog/manifest.json"))`. All jobs run with `LC_ALL=C` and `TZ=UTC`.

**Change ⇒ new `release_id`**

* Any byte-level change to a frozen input (content, bounds, divisors or weights, thresholds, catalogs, seeds if catalogized), its schema or membership or order, or the manifest content or shape or order **MUST** produce a new `release_id`.  
* **Explicit rule.** Any change to constants, **Motor→Throat sets**, thresholds, or catalog membership or order **requires a manifest update in Evidence & Artifacts and yields a new `release_id`**.

**Determinism and scope**

* **Two-run identity.** Building the pack twice from identical sources yields the same `release_id`.  
* **Order-neutral.** `release_id` is independent of AB↔BA pairing and of presentation order in public bytes, as long as the pack is identical.  
* **Transport-independent.** HTTP headers, caching, and Reader or CLI mechanics do not enter the pack.

**Validation (binary)**

* **Pattern.** `release_id` matches `^[0-9a-f]{64}$`.  
* **Recompute.** Recompute `sha256(canonical_bytes(manifest))` and match the published `release_id`.  
* **Canonical file check.** The on-disk manifest equals the canonical serialization (UTF-8 no BOM, sorted keys, compact, one LF).  
* **Closure.** Every math input referenced at runtime resolves to an entry in `files[]`. No missing or ad hoc sources.  
* **No self-listing.** The manifest does not list itself.

**Tokens:** see §2.0: `RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `PACK_ROOT_PINNED_OK`, `JSON_CANONICAL_CHECK_OK`.

---

## **5.2 Pointer-flip and rollback \[Required-Now\]**

**Purpose (normative).** Provide a deterministic, auditable procedure to promote a frozen math pack to production and to revert safely if acceptance signals fail. **Promotion is a pointer change** in configuration, not a code edit. The active pack is identified **solely** by its `release_id` (§5.1).

### **5.2.1 Promotion (pointer-flip) — required steps**

1. **Freeze and tag.**  
    • Build the **canonical manifest**; compute and record the `release_id` (64-hex).  
    • Attach the manifest and `release_id` to the Change Log / Doc-Delta (titles & repo-relative paths only).

2. **Staging verification (A-gates).**  
    • Prove **A3 determinism** (preimage re-check per **PF-01**, AB↔BA, two-run).  
    • Prove **A4 Reader↔CLI parity** on staging fixtures (single presenter).  
    • Prove **A7 transport** on a **PF-05 Endpoint Catalog (success JSON)** route: **ETag on 200**, **HEAD parity including `Content-Type`**, **304 omits `Content-Type`**.  
    • Record artifacts in the **human Index** and **machine JSONL mirror** (records-only, path-agnostic, with path-proofs).

3. **Canary (optional, recommended).**  
    • Flip the pack pointer to the new `release_id` for a **bounded, time-boxed** canary.  
    • Monitor keys-only metrics for regressions in **parity**, **preimage pass rate**, **A7 invariants**, and **typed error mix**.

4. **Production flip.**  
    • Update the **single pointer** selecting the active pack to the new `release_id`.  
    • Do **not** modify code, schemas, or runtime knobs during the flip; only the **pack pointer** changes.

5. **Post-flip evidence.**  
    • On live traffic or representative fixtures, **re-prove A3, A4, A7** and capture header snapshots (titles only).  
    • Update **Appendix D** and the **machine mirror** **in the same change**.

### **5.2.2 Rollback — required steps**

1. **Trigger conditions (any one is sufficient).**  
    • Parity failure (Reader↔CLI mismatch), **AB↔BA** or **two-run** failure, or **preimage/idempotence** mismatch.  
    • **A7 violation** (missing/incorrect `ETag`, 304 without prior 200, **HEAD parity mismatch**, **304 with `Content-Type`**).  
    • Elevated **typed failures** attributable to the pack.

2. **Immediate action.**  
    • Flip the pack pointer back to the **previous `release_id`** (last known good).  
    • Do **not** change code or hot-patch the emitter; only revert the pointer.

3. **Drift checks.**  
    • Confirm that **public bodies and validators** now match the last known good (A3, A4, A7 **pass**).  
    • Verify caches reflect the rollback: identity bytes and therefore `ETag`s revert to prior values.

4. **Evidence and follow-up.**  
    • Record the rollback in the Change Log (one-line reason, time, `release_id→release_id`).  
    • Open an investigation item with links to failing evidence; **do not** re-promote until fixed.

### **5.2.3 Guardrails (normative)**

* **Immutability.** A published pack is **immutable**. Any math or input change produces a new `release_id` (§5.1). No in-place edits.  
* **Single source of identity.** The active pack in any environment is identified **only** by the pointer’s `release_id`. Do not infer from tags or branches.  
* **No mixed packs.** Never serve mixed results from multiple packs in the same environment. Canaries must be scoped and time-boxed.  
* **Keys-only ops.** Release, canary, and rollback logs contain **no payloads or secrets**. Labels are bounded (route, outcome, `rails_state`).  
* **Evidence first.** A promotion or rollback is **incomplete** until the **human Index \+ machine mirror** are updated **in the same change** and CI gates pass (parity, idempotence, A7 tokens, **mirror parity & path-proof validation**).

### **5.2.4 Binary acceptance (pass or fail)**

A pointer-flip or rollback is **Accepted** only if, after the change:

* **A3, A4, A7** gates **pass** on the active environment (staging then production).  
* The **Evidence Index (human) and machine mirror** are updated and CI passes (**parity, preimage re-check, A7 tokens, grep-guards, mirror parity & path proofs**).

Otherwise, the change is **Rejected** and must be rolled back to the **last known-good `release_id`**.

# **6\. Operations & SLOs \[Required-Now\]**

## **6.1 Bench harness (non-PII) \[Required-Now\]**

**Purpose (normative).** Provide a repeatable, deterministic harness for measuring engine performance and transport behavior without exposing PII or payload bytes. Bench results inform SLOs, release decisions, and regressions; they do not change the public contract.

### **6.1.1 Deterministic runs**

* **Inputs and seeds.** Use a fixed set of fixture pairs (titles and paths only), stable environment, and pinned config (serializer and emitter, rails posture). No wall-clock–dependent logic; no randomness.  
* **Warm-up and windowing.** Perform a fixed warm-up that is discarded, then a fixed measurement window; run counts are constant across cuts.  
* **Isolation.** Disable vendor calls (rails **closed**) for math and transport benches. When measuring **open rails** profiles, pin timeout, backoff, and retry enums and run them in a separate profile.

  ### **6.1.2 Report set (bounded, non-PII)**

* **Latency histograms (bounded).**  
  * `engine.latency_ms` and `presenter.latency_ms`: bucketed histograms with fixed bucket edges, plus p50, p95, p99 derived in harness (not logged per request).  
  * `reader.latency_ms` (dev harness only) with the same buckets.  
* **Outcome counters (bounded labels).**  
  * `reader.req_total`, `reader.req_ok`, `reader.req_error_{class}` where class ∈ {`usage`,`typed`,`transport`}.  
  * `cli.stdout_ok`, `cli.stderr_typed`.  
  * `transport.etag_ok`, `transport.cond_304`, `transport.head_parity_ok`, `transport.no_store_ok`.  
* **Label set (bounded).** `route`, `outcome ∈ {ok,usage,typed,transport}`, `rails_state ∈ {open,closed}`, `profile ∈ {default,small,long}`, `attempt_idx` when measuring retries.  
* **No payloads and no secrets.** Logs must not include request/response bodies, header values, or keys. Secrets are always redacted.

  ### **6.1.3 Procedure (normative)**

1. **Prepare profiles.**  
   * **Math/transport profile:** rails **closed**; run fixture pairs through CLI and dev Reader; capture latency and parity/idempotence checks.  
   * **Vendor profile (optional):** rails **open**; run pinned timeouts, retries, and backoff; capture typed mapping behavior with no payloads.  
2. **Execute runs.** Fixed iteration counts per profile; capture metrics and byte-level assertions for AB↔BA, two-run identity, and Reader↔CLI parity.  
3. **Summarize.** Produce a bench report artifact (titles and paths only) with histograms and counters. No raw payloads or secrets.

   ### **6.1.4 Acceptance (binary)**

* **Determinism.** Re-running the same profile yields statistically identical histograms and identical parity and idempotence outcomes.  
* **Parity and identity.** All A3 and A4 byte-level gates pass during the bench (AB↔BA, two-run, Reader↔CLI).  
* **A7 spot checks.** In the dev harness, validators for **200 with ETag**, **304**, **HEAD parity**, and **no-store** on writers/errors pass.  
* **Rails posture.** Closed-rails benches show no network I/O. Open-rails benches show pinned behavior and redacted logs only.

  ### **6.1.5 Evidence and SLO coupling**

* **Artifacts.** Commit the bench report and metric snapshots under the Evidence Index (Appendix D; titles and paths only).  
* **SLO link.** Compare p95 and p99 to the SLO targets (see §6.2). A violation triggers rollback or investigation per §5.2.  
  ---

## 6.2 SLO targets and failure posture \[Required‑Now\]

### Scope (policy‑level). 

Define service‑level objectives for Reader success routes and ops surfaces. Targets are numeric‑free here; concrete values and dashboards live in operator configuration. All captures and compares run with `LC_ALL=C`, `TZ=UTC`. (Evidence and mirror hygiene live in PF12; tokens live in §2.0.)

### Bench harness (evidence, titles‑only). 

Bench outputs are evidence artifacts without payload bodies or PII; index them in the human Evidence Index and the machine mirror in the same PR (PF12 single home).

### Failure posture. 

If a governed SLO is breached for a success route or ops surface, initiate the operator rollback or mitigation policy, capture an evidence snapshot of the failure envelope, and update the human index \+ hash sentinel and machine mirror in the same PR. (Mirror: records‑only canonical JSONL; one LF; ASCII field order; unknown‑keys rejected; single mirror file; `proof_anchor` present.)

### Acceptance tokens (names‑only; rostered in §2.0). 

Register SLO/bench tokens as they are introduced; they are merge‑gating and must obey PF12 index/mirror discipline.

### Routing (titles‑only).

Evidence/index shapes and merge‑gating sentinel: PF12. Process/PR flow: Epic‑Process‑Guide. Transport bytes and success matrices: §10 / Appendix A of this document.

## 6.3 Database runtime posture (prod & dev) \[Required-Now\]

 **Purpose (normative).** Pin connection-source policy and acceptance tokens for production and development, without duplicating schema/bytes. Evidence lives in **PF12**; infra names live in **Glow Infrastructure**.

### **6.3.1 Production (policy)**

* **Single source (presence-only; no probe).** Connection selection is **`DATABASE_URL → typed error`**. The **bridge is not used** in production.  
* **Search path.** Runtime `search_path` is exactly **`hde, public`** (in that order).  
* **Dev-only artifacts absent.** The dev connectivity snapshot (**`artifacts/runtime/env_connectivity.snapshot.json`**) **must not** be present in production evidence.

**Acceptance (titles-only).** `PROD_CONN_SINGLE_SOURCE_OK`, `DB_CONN_ENV_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`.  
 **Evidence (titles-only; PF12 single home).**

* `artifacts/db/check_schema.txt` (search\_path)  
* `artifacts/db/grants.txt` (least-privilege grants)  
* `artifacts/db/ddl_fingerprint.json` (DDL fingerprint)  
* `artifacts/db/conn_env_selection.log` (selection proof; keys-only, no secrets)  
   See **Appendix D: D.11**.

### 6.3.2 Development (PF10-A) — bridge fallback with evidence

Fallback rule (dev-only).  
 If `APP_ENV=dev` and `DATABASE_URL` is present but not usable, fall back to `DB_BRIDGE_URL`; refuse (typed error) if neither is usable.

Diagnostics.  
 Keys-only logs; no secrets, no payloads.

Error handling (bridge failures).  
 Any network-level error from the HTTPS bridge is caught and surfaced as a **typed internal adapter error** (for example `BridgeUnavailable` with a coded reason), not as a raw exception. This preserves SAFE-rails and logging posture: no low-level stack traces or unredacted messages leak into logs or outputs, and error bodies follow the standard typed, numeric-free envelope.

Search path.  
 Runtime `search_path` remains `hde, public`.

Acceptance (titles-only).  
 `DEV_DB_BRIDGE_FALLBACK_OK`, `DB_CONN_ENV_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`.

Evidence (titles-only; PF12 single home).  
 `artifacts/runtime/env_connectivity.snapshot.json` (dev resolver snapshot), plus the D.11 DB posture set. See **Appendix D: D.12**.

### 6.3.3 Routing (titles-only)

Tokens: §2.0 Acceptance Tokens.  
 Evidence & mirror hygiene: **PF12 — HDE-Schemas & Artifacts** (human `INDEX.json` \+ hash sentinel \+ machine mirror updated in the same PR).  
 Infra names/ownership: **Glow Infrastructure** (names-only).

---

### 6.4 QA branches (evidence-only) \[Required-Now\]

**Scope (cross-reference).** In QA branches, changes are **evidence-only** and CI is **diff-scoped to governed files**; do not modify application/presenter bytes, schemas, or runtime config outside an approved release epic. Permitted changes are limited to **updating the Human Evidence Index** (`docs/evidence/INDEX.json`), its **hash sentinel** (`docs/evidence/INDEX.sha256`), the **machine mirror** (`artifacts/evidence_index.jsonl`, records-only, canonical JSONL, one LF, unknown-key rejection, ASCII field order, sort-before-write, single file, each with a `proof_anchor` to a co-located path-proof), and **proof artifacts under `artifacts/**` (e.g., A7 headers & composite JSON on Catalog success routes, rails refusal/conformance probes, DB posture & env-connectivity snapshots, start-command/env-pins, SBOM)**—all indexed in **PF12 §8.6** in the **same PR** per PF06. For process, **do not restate procedure here**: see **Epic-Process-Guide** (QA PR template, PR-first, same-PR evidence rule) and **PF06 §0.7** (QA branches are evidence-only; CI is **diff-scoped**). *Tokens:* see **§2.0** (`QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`). *Evidence hygiene:* mirror parity and hash-sentinel gating per **PF12 §8.3/§8.6**.

---

# 7\) Logging & Observability \[Required-Now\]

### **7.1 Keys-only logging \[Required-Now\]**

**Principle (normative).** Operational logs **MUST** be keys-only: no request/response payloads, no header values, and no secrets or PII. Messages use bounded labels and deterministic formats suitable for automated analysis.

#### **7.1.1 Prohibitions**

* **No payload bodies.** Never log Reader or CLI JSON bodies, vendor requests, or vendor responses.  
* **No header values.** Never emit concrete header contents (e.g., `Authorization`, `HD-Api-Key`, `HD-Geocode-Key`, `Set-Cookie`, ETag payload).  
* **No secrets or PII.** API keys, tokens, user identifiers, free-text inputs, or locations are not logged.

  #### **7.1.2 Redaction and safe fields**

* **Secrets redacted.** If a secret key name must be mentioned, print a placeholder only (e.g., `HD-Api-Key: REDACTED`).  
* **Error objects.** Typed errors are logged as numeric-free `{code, message}` tuples; never echo vendor or body text.

  #### **7.1.3 Bounded label set (examples)**

Use a small, fixed set of labels. Values come from closed enums.

* `route` (e.g., `reader_v1`, `vendor_hdapi`)  
* `outcome ∈ {ok, usage, typed, transport, network_error, 4xx, 5xx, 429}`  
* `rails_state ∈ {open, closed}`  
* `timeout_profile ∈ {small, default, long}` (when rails are open)  
* `attempt_idx` — retry attempt as a small integer  
* `correlation_id` — non-PII, bounded format

  #### **7.1.4 Determinism and formatting**

* **Deterministic structure.** Emissions are stable key/value objects (JSON or equivalent), locale-neutral, and free of ANSI/BOM.  
* **No free text.** Avoid narrative strings; prefer tokens and enums.  
* **Time fields.** If present, use UTC ISO-8601/RFC timestamps. Never log wall-clock deltas derived from payload contents. Run checks under `LC_ALL=C`, `TZ=UTC`.

  #### **7.1.5 CI and enforcement**

* **Grep guards.** Fail the pipeline on patterns that indicate payload/body dumps, header value logging, or raw secrets.  
* **Allow-list.** Maintain an allow-list of safe labels. New labels require a Doc-Delta and tests.  
* **Spot checks.** Include redaction fixtures and log-shape tests in the Evidence Index. Verify no payloads or values appear in logs.

**Refusal vs 429 (keys-only) — scope note.**

* **Refusal (rails closed):** refusal logs are limited to the six-key allow-list `{at, route, status, duration_ms, idempotence_hash, release_id}`.  
* **429:** when rate-limited, logs may include `retry_after_ms` in addition to the allow-listed keys; never echo payload or header values.

**Tokens (titles-only; see §2.0).** `PF04_LOG_ALLOWLIST_009_OK`, `ERROR_CTYPE_JSON_UTF8_OK`, `NO_CONTENT_ENCODING_OK`, `NO_EXTERNAL_IO_ON_REFUSAL_OK`.

#### 7.1.6 Privacy (BodyGraph/vendor inputs) \[Required-Now\]

* **No birth data.** Never log birth details or any BodyGraph input fields.  
* **No payload echo.** Do not log vendor request/response bodies or derived payload content.  
* **Secrets never logged.** API keys/tokens/credentials must not appear; if referenced, use redacted placeholders (e.g., `HD-Api-Key: REDACTED`).  
* **Bounded metrics families only.** Use fixed, low-cardinality metric families and labels; do not encode payload content or PII in labels.  
   *(Examples of bounded labels: `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`, `correlation_id`.)*

### **7.2 Correlation ID \[Required-Now\]**

**Principle (normative).** A non-PII correlation identifier ties together logs and traces across CLI, Reader, and (when rails are open) vendor calls. It is transport/ops-only, **never** part of the public payload, deterministic per invocation, and order-neutral with respect to pair normalization.

#### **7.2.1 Requirements**

* **Non-PII and secret-free.** The value **MUST NOT** encode personal data, tokens, or payload content.  
* **Stable propagation.** A single correlation ID **MUST** be generated/selected at entry and propagated unchanged through all downstream calls/logs for that invocation.  
* **Order-neutral.** For `(A,B)` and `(B,A)` of the same logical invocation, the correlation ID **MUST** be identical.  
* **Payload-free.** The correlation ID **MUST NOT** appear in the Reader public body (success or error). It does not affect `idempotence_hash` or `ETag`.

  #### **7.2.2 Format and bounds**

* **Charset/length.** ASCII opaque token from a bounded alphabet (e.g., `[A-Z0-9-]`) with a fixed maximum length (e.g., ≤ 64).  
* **Deterministic generation.** Caller (CLI or Adapter) supplies the ID when available; otherwise generate at the adapter boundary using a deterministic, time-independent recipe. If a time-safe recipe must be used, treat the value as transport-only.  
* **Bounded cardinality.** Use correlation ID as a field, not a high-cardinality label in metrics; if used as a label, sample/partition to protect observability systems.

  #### **7.2.3 Propagation (transport and logging)**

* **Transport.** Propagate via a single, pinned transport carrier owned by the CLI/Reader transport spec (titles-only routing).  
* **Logging.** Include the correlation ID in keys-only logs. Redact nothing except to enforce format/length bounds. **Do not** log header values.  
* **Vendor calls (rails open).** If a vendor call is made, forward the correlation ID as metadata only. Never echo vendor bodies or header values to logs.

  #### **7.2.4 Validation (binary)**

* **Presence & format.** When required, the correlation ID **MUST** be present and match the pinned format bounds; otherwise refuse or downgrade to a typed error per transport policy.  
* **AB↔BA and two-run neutrality.** Correlation ID is identical for AB versus BA and stable across two runs of the same invocation. It does not change public bytes, `idempotence_hash`, or `ETag`.  
* **CI checks.** Tests assert presence/format, no appearance in public payloads, and keys-only logging with no secrets or payloads.

  #### **7.2.5 Routing (titles-only)**

Carrier name, precise header casing, and where/when it is set are defined in **HDE-CLI-API-Vendor-Ref** (transport section). Governance does not duplicate transport bytes.

### **7.3 Narratives persistence logging (admin-only) \[Required-Now\]**

**Rule.** Do **not** log narrative text or fragment content. Logs must be keys-only and numeric-free.

**Allowed fields in logs (keys-only).** `composition_id`, `fragment_ids.length`, `pack_sha`, `release_id`, `dyad_id`, `request_id`, `writer`, `timestamps`, `correlation_id`.

**Prohibited logging.**

* The narrative text itself.  
* Any raw `fragment_ids` values or fragment content.  
* Payload echoes, secrets, or headers with credentials.

**Redaction and shaping.**

* Redact secret-bearing headers and payloads.  
* If a fragment list is present in an internal trace, record only `fragment_ids.length`.  
* Keep labels bounded and consistent to preserve cardinality discipline.

**Evidence (titles/paths only).**

* `ci/jobs/logs_keys_only_redaction.yml` — CI proof that logs contain no narrative text and only the allowed keys.  
* Optional audit sample demonstrating absence of text in logs.

**Acceptance (titles-only).** Governed by logging/redaction tokens listed in §2.0 and the Evidence Index parity tokens (human ↔ machine, same PR).

**Routing (titles-only).**

* Field/length constraints for narratives: **HDE-Schemas & Artifacts** (composer response).  
* Storage locations and DB names: **Glow Infrastructure** (names-only).  
* Transport and A7 policy: **HDE-Governance** (this document) and **HDE-CLI-API-Vendor-Ref** for endpoint bytes.

---

# **8\. Security & Privacy \[Required-Now\]**

## **8.1 Numeric-free public covenant \[Required-Now\]**

**Principle (normative).** All public-facing **Reader v1** responses are **numeric-free** and **narrative-free**. Public payloads disclose **only** categorical results in the shape `{ "id", "band" }`. **No** scores, percentages, prompt text, or other numerics may appear on the public surface.

### **8.1.1 Scope**

* **Applies to:** all public responses from the Reader v1 surface (**HTTP 200 success** and all **typed errors**) and all **CLI stdout** outputs intended to mirror public bytes.  
* **Does not apply to:** internal compatibility math, presets, or bench diagnostics stored as **private artifacts or logs**. These remain internal only and **redacted** in public.

### **8.1.2 Requirements**

* **Categories array (public shape & domain).**

  * Each item in `categories[*]` **MUST** be exactly `{ "id": <string>, "band": <enum> }`.  
  * `band ∈ {"Cool","Open","Warm","Glow"}`.  
  * `id` **MUST** be a **Magic-10 identifier** from the **closed set and order** (see PF-Canon-HDE-Schemas and Artifacts §2.6 / PF-01 §5.1).  
  * **v1 exposure rule:** if `eligible == true`, the array **MUST** contain **exactly one** item, `{"id":"harmony","band":…}` (PF-01 §2.2). If `eligible == false`, the array **MAY** be empty.  
  * **No numeric fields** are permitted (e.g., `score`, `score_pct`, `index`, `rank`).  
* **Top-level structure (success).** The success body contains **exactly six keys**:  
   `reader_version, eligible, categories, meta, release_id, idempotence_hash`.  
   No additional top-level fields may be introduced without a **versioned Reader contract** update.

* **Typed errors (numeric-free).**

  * Error objects are numeric-free; only `{ ok:false, code, error }` are allowed.  
  * Optional `retry_after_ms` is the **sole integer** field, used **only** under controlled vendor retry policies (see **PF-Canon-HDE-CLI-API-Vendor-Ref**, titles-only).  
* **Narratives and prompts.** Public payloads **MUST NOT** include prompt text, narratives, or user-facing messages generated by internal modules. These are **retired**.

* **Resonance posture (public).** Public payloads **MUST NOT** expose SR/XR numerics. v1 ships **SR-only** (`alpha=1.0`); **hysteresis \= 1** is armed for future XR and **not exposed**.

### **8.1.3 Validation (binary)**

* **Schema gate.** Verify success has **exactly six keys** and that `categories[*]` items are **only** `{id, band}`.  
* **Closed-set check.** `id` values must belong to the **Magic-10** closed set (PF-12 §2.6 / PF-01 §5.1); **no extras/omissions**.  
* **Numeric-free grep-guard.** CI blocks any numeric fields or prompt text in public payloads.  
* **Canonical JSON.** Public bytes are serialized as **UTF-8 (no BOM)**, **sorted keys**, **compact**, **exactly one trailing LF**; arrays used as sets are **deduped and ASCII-sorted** (PF-12 §4).  
* **Parity enforcement.** **Reader↔CLI** parity gates confirm **identical numeric-free** payloads for the same inputs and environment, under **`LC_ALL=C`**.

### **8.1.4 Routing (titles-only)**

Math and scoring details are defined in **PF-Canon-HDE-Math-Spec**. The public emission policy **lives here** and governs the Reader and CLI surfaces. Resonance constants and pack/manifest rules live in **PF-Canon-HDE-Schemas and Artifacts**.

**Acceptance & CI (titles-only)**  
 `RESONANCE_PUBLIC_POSTURE_OK`, `CLI_READER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `PREFS_KEYSET_10_OK`, `MAGIC10_DOMAIN_CLOSED_OK`

## **8.2 No PII or secrets in logs \[Required-Now\]**

**Principle (normative).** Operational logs MUST NOT contain PII or secrets under any circumstance. Logs are keys only and use bounded, deterministic labels (see §7.1).

### **8.2.1 Redaction rules**

* **Secrets.** Do not write API keys, tokens, session IDs, or header values. If a key name must appear, render as `REDACTED` (for example, `HD-Api-Key: REDACTED`).  
* **PII.** Do not emit names, birth data, locations, or free text copied from payloads.  
* **Bodies.** Never log Reader, CLI, or vendored request or response bodies.  
* **Typed errors.** Emit only numeric free code and message tuples. Never echo vendor text or payload fragments.

### **8.2.2 Safe fields and bounded labels**

* Allowed labels are a fixed allowlist (for example, `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`, `correlation_id`) with closed value domains. No high cardinality user identifiers.  
* `correlation_id` is non PII, bounded in length and charset, and used for stitching only (see §7.2).

### **8.2.3 Audit hooks (prove and enforce)**

* **CI grep guards.** Fail on patterns indicating payload or body dumps, header value logging, or raw secrets.  
* **Structured log shape tests.** Verify logs are JSON or equivalent, BOM or ANSI free, and contain only allowlisted fields.  
* **Redaction fixtures.** Keep example log lines with redacted secrets under the Evidence Index (titles and paths only).  
* **Periodic review.** Run scheduled audits to confirm no PII or secrets. File a Doc-Delta if new labels are needed.

### **8.2.4 Incident posture**

* **Immediate containment.** If PII or secret leakage is detected, halt affected jobs, rotate credentials if applicable, and purge offending logs per policy.  
* **Evidence and follow up.** Record the incident (titles and paths only), add tests and guards to prevent recurrence, and document the fix in the Change Log or Doc-Delta.

**Routing.** This section governs ops logging only. Public payload rules remain in §8.1. Transport specifics and vendor behaviors are referenced by title only in the **PF-Canon-HDE-CLI-API-Vendor-Ref**.

# 9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]

 **Purpose.** Define the repo-level rules that keep governance, evidence, and code in lock-step. **PF12** remains the single home for index/mirror schemas and canonical JSON rules; this section pins the **policy and gates** (names-only routing to PF12 for bytes).

---

## 9.1 Single-home doctrine (routing by title) 

* **Transport & ops policy live here (PF04).** A7 invariants, conditional rules, refusal posture, Aux suppression carve-out, and `/internal/version` ops semantics are governed in PF04.  
* **CLI/Reader wire bytes live in PF05.**  
* **Pack/manifest/mirror schemas live in PF12.**  
   Use **titles-only** cross-references; **do not duplicate bytes** across documents.

---

## 9.2 What requires a Doc-Delta \[Required-Now\]

A Doc-Delta is **mandatory** for any normative change that can affect **identity, acceptance, or operations**. Open a Doc-Delta **before** making any of the following changes, and land it **only with updated evidence** (see §4) and a synchronized **Evidence Index** entry.

* **Math change (freeze-pack impact).** Any change to frozen math inputs or their canonicalization: category membership or order, band maxima, vocab tokens, fold or priority rules, dampener recipes, floors or caps, preset catalog or schema, or any manifest bytes that would yield a new `release_id` (§5.1). The Doc-Delta **MUST** include the new manifest digest and `release_id`.  
* **Public contract (Reader or CLI).** Any change to the public success or error shape, adding fields, changing categories policy, or altering the numeric-free covenant; any transport-visible behavior that modifies public bytes.  
* **Serializer or emitter path.** Any change to the single presenter emitter or its canonicalization rules (UTF-8, sorted keys, compact, one LF), or introducing/removing emitters on public paths.  
* **Schema gates.** Tightening or loosening public schemas (success or typed errors), changing allowed enums, or modifying validation that could alter acceptance outcomes.  
* **Transport policy (A7).** Changes to ETag identity, conditional delivery for 304 or HEAD, Cache-Control rules, or any header matrices that affect acceptance.  
* **Rails enablement (vendor posture).** Opening rails for live HTTP, changing timeouts, retries, backoff, or 429 policies; adding/changing typed vendor error mapping; any modification to redaction/observability that impacts acceptance.  
* **Security and logging.** Adjustments to keys-only logging, redaction rules, correlation propagation, or bounded label sets that alter operational guarantees.

**Landing conditions (binary).** A Doc-Delta is **Accepted** only when: (a) implicated A-gates pass (A3 or A4 or A7 as applicable), (b) **evidence is added/updated** and **Appendix D** is revised **in the same change**, and (c) **freeze-pack** impact is recorded if present. Otherwise it is **Rejected** and must not ship.

---

## 9.3 Doc-Delta entries (what to record for any normative change) 

Every normative change **MUST** add a short “Doc-Delta” entry in this document’s **Change Log** with:

* **Scope** (one line): what changed, at a glance.  
* **Targets** (anchors/sections by title).  
* **Acceptance impact:** which tokens are affected (names-only; token roster lives in §2.0).  
* **Evidence impact:** which artifacts/paths were added/rotated/removed (titles only).  
* **Freeze-pack impact:** whether `release_id` changed (PF12 owns bytes).

*Rationale:* PF10 addenda are living; later addenda **supersede** earlier guidance, so the Doc-Delta ties **decision → bytes → evidence** in a single PR.

---

## 9.4 Doc-Delta template \[Required-Now\]

Use this template for every normative change. Keep entries concise and action-oriented. All affected **binary gates** must pass (§4), and **Appendix D — Evidence Index** must be updated in the same change.

DOC-DELTA-ID: GOV-YYYYMMDD-\<shortslug\>

Date / Author: \<YYYY-MM-DD\> / \<name\>

Scope: Math | Public Contract/Transport | Serializer/Emitter | Vendor Ingest | Schema | Acceptance/Evidence | Security/Logging | Rails Enablement

Targets (section anchors): e.g., §2.3 A7, §5.1 release\_id, Appendix D

Summary (≤ 5 bullets):

1\) \<Action verb \+ concrete change\>

2\) ...

Acceptance impact (binary gates to update or verify):

\- A3 Determinism. Preimage → sha256 → final; AB↔BA; two-run.

\- A4 Reader↔CLI parity. Single emitter; byte equality; schema and shape gates.

\- A7 Transport. ETag, 304, HEAD; no-store on writers and errors.

\- Rails posture. Refusal closed; conformance open (timeouts, retries, backoff, 429).

Evidence updates (titles and paths only):

\- Goldens or scripts added or refreshed (AB↔BA, two-run, LF and encoding, preimage recompute).

\- Header snapshots and transport sequences (A7).

\- CI jobs or grep guards adjusted (no ad-hoc dumps or emitters; keys-only logs).

\- Appendix D entries updated (MUST).

Freeze-pack impact: Yes/No

\- If Yes: attach canonical manifest digest and new release\_id (§5.1); list affected pack entries by title and path.

Routing (titles only confirmations):

\- Math and Architecture rules are referenced by title only.

\- Transport and ops bytes remain governed here.

Rollout plan:

\- Staging gates → optional canary (scope and duration) → production pointer flip (§5.2).

\- Backout or rollback plan (pointer to last known-good release\_id).

\- Monitoring focus (bounded labels; no payloads or secrets).

Change Log entry (one line): vX.Y — \<concise action\>: \<targets\>; evidence updated; freeze-pack impact: \<Yes/No\>.

---

## 9.5 Same-PR indexing (human ↔ machine parity)

When any golden/evidence path changes, update **in the same PR**:

* **Human Index:** `docs/evidence/INDEX.json`  
* **Hash sentinel:** `docs/evidence/INDEX.sha256` (merge-gating; must match `INDEX.json` bytes)  
* **Machine mirror:** `artifacts/evidence_index.jsonl` (**records-only** canonical JSONL; one LF; ASCII field order; sort-before-write; **unknown-key reject**; **single mirror file**; each record includes **`proof_anchor`** to a stored path-proof)

**Acceptance tokens (names-only).** `EVIDENCE_INDEX_UPDATED_OK` · `EVIDENCE_INDEX_HASH_OK` · `EVIDENCE_INDEX_MIRROR_OK` · `EVIDENCE_PATHS_VALIDATED_OK`. *(Roster lives in §2.0.)*

---

## 9.6 Pairing proofs with the A7 surface 

A7 transport proofs **must** run on a **Catalog JSON success** route (not `/internal/version`). Pair the **composite A7 proof JSON** (PF12 schema) with:

* **Catalog snapshot** (titles-only)  
* **Headers-only env-gate** capture proving non-prod entries are

# 10\. Transport Governance (Reader) \[Required-Now\]

## 10.1 Success (200) matrix \[Required-Now\]

 **Purpose (normative).** Govern the required headers and body properties for a **200 OK** Reader response on a **Catalog JSON success** route. These are governance rules; transport bytes and concrete route lists live by title in **HDE-CLI-API-Vendor-Ref** and are validated via **A7** acceptance tokens (§2.0). **A7 proofs run on a Catalog JSON success route; `/internal/version` is excluded.**

### Headers — required

* **Content-Type: application/json; charset=utf-8** — UTF-8 JSON; BOM/ANSI-free.  
* **ETag: "\<strong, quoted\>"** — identity over the **final LF-terminated canonical JSON** body (pre-compression); encoding-invariant.  
* **Vary: Authorization, Accept-Encoding** — required; additional Vary members allowed.  
* **Cache-Control: private, max-age=0, must-revalidate** — required on 200 success.

### Body — success covenant

* **Six keys exactly.** Top-level object contains only: **reader\_version, eligible, categories, meta, release\_id, idempotence\_hash**.  
* **Categories policy (v1).** `categories[*]` are exactly **{ id, band }** (numeric-free). If `eligible == true` in v1 Alpha, a single `{"id":"harmony","band":…}`; if `eligible == false`, `[]`.  
* **Serialization.** Canonical emitter: UTF-8, **sorted keys**, compact separators, **exactly one trailing LF** (`\n`).  
* **Idempotence coupling.** `idempotence_hash = sha256(preimage_bytes)` where the preimage fields are defined in **HDE-Math-Spec** (do not restate here). **Re-serialize canonically after insertion.**

**Acceptance (binary gates)**

1. **Headers present and correct.** `Content-Type`, **quoted strong** `ETag`, `Vary: Authorization, Accept-Encoding`, and `Cache-Control: private, max-age=0, must-revalidate` are present.  
2. **Body covenant.** Six keys only; `categories[*] == { id, band }`; LF-terminated; canonical serialization.  
3. **Idempotence re-check.** Remove `idempotence_hash`, canonicalize the **HDE-Math-Spec** preimage, and verify `sha256(preimage_bytes)` equals the published hash.  
4. **Encoding invariance.** Identity (`ETag`) is unchanged by `Accept-Encoding` selection for the same body.  
5. **No `no-store` on success.** Confirm `Cache-Control: no-store` is **absent** on 200 success (reserved for writers/errors).  
6. **Tokens:** see §2.0 **Reader A7** and **READER\_\*** tokens.

## 10.2 Conditional delivery \[Required-Now\]

 **Purpose (normative).** Define when and how conditional responses are served on a **Catalog JSON success** route. Governance rules live here; transport bytes live by title in **HDE-CLI-API-Vendor-Ref**. **A7 proofs run on a Catalog JSON success route; `/internal/version` is excluded.**

### **304 Not Modified — only after a prior 200-with-body**

* **Precondition.** A prior 200 success with a **strong, quoted ETag** exists, and the request presents a matching `If-None-Match`.  
* **Body.** None.  
* **Headers.**  
  * `ETag` present (matches the cached 200\)  
  * Mirror 200 validators (`Cache-Control`, `Vary`)  
  * **Omit `Content-Type`**  
  * **Omit `Content-Length`**  
* **No writers/errors.** 304 is **never** used for writer or error responses (writers/errors use `Cache-Control: no-store` and carry **no `ETag`**).

### **HEAD parity — headers mirror 200; no body**

* **Header parity.** HEAD returns the same validators as GET for the same resource (**strong quoted ETag**, `Vary`, `Cache-Control: private, max-age=0, must-revalidate`, and `Content-Type` identical to GET).  
* **Body/length.** No body; **`Content-Length == len(identity 200 body)`** (canonical LF-terminated bytes, pre-compression).  
* **Encoding invariance.** Choice of `Accept-Encoding` does not change identity (`ETag`) for the same body.

### **Acceptance (binary gates)**

1. **304-after-200.** Server returns 304 only when a prior 200-with-body exists and `If-None-Match` matches the strong, quoted `ETag`; 304 carries **no body**, mirrors validators, and **omits** `Content-Type` **and** `Content-Length`.  
2. **HEAD parity.** Headers mirror 200; **no body**; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
3. **Invariant identity.** `ETag` is stable across encodings for the same body.  
4. **No misuse.** 304 is **never** used for writers/errors; those responses are governed by `no-store` and **no `ETag`**.

**Tokens:** see §2.0 **Reader A7** tokens.

Got it — here’s your **§10.3 Writers and errors** cleaned up for clarity and consistency, without changing any substance.

---

## 10.3 Writers and errors \[Required-Now\]

 **Purpose (normative).** Govern headers and body shape for writer and error responses. Governance rules live here; transport bytes live by title in **HDE-CLI-API-Vendor-Ref**. Writers/errors are **no-store** and **not** part of A7 success proofs.

### **Headers — required**

* **Writers and errors:** `Cache-Control: no-store` (**MUST**).  
* **Errors only:** `Content-Type: application/json; charset=utf-8`.  
* **Writers and errors:** **no `ETag`** (identity caching does not apply).

### **Body — typed error shape (errors only)**

* **Shape.** Typed, numeric-free error object (see CLI/Reader error model):  
   `{"ok": false, "code": "<TOKEN>", "error": "<non-PII message>"}`.  
   Optional `retry_after_ms` (integer ≥ 0\) only under a pinned vendor rate-limit policy.  
* **Serialization.** Canonical emitter (UTF-8, sorted keys, compact separators), **exactly one trailing LF**.  
* **No payload echo.** Do **not** include vendor payloads, header values, or secrets.

### **Writers (success-without-body semantics)**

* **No body required.** Writers commonly return **204 No Content**. If a body is emitted for diagnostics, it must remain **typed, minimal, numeric-free,** and **canonically serialized**.  
* **Always no-store.** Caching must be disabled. **Never** send an `ETag`.

### **Writers — OPTIONS/HEAD semantics (normative)**

* **OPTIONS → 204 (no body).** Writers’ OPTIONS responses **must** return 204 with no body; **forbid** `ETag`/`Vary`/compression. Under HTTP/2, `Content-Length: 0` may be omitted.  
* **HEAD 405 (strict).** Writers’ HEAD on non-HEAD writers is **405**; when emitted, include `Content-Length: 0`.

### **Acceptance (binary gates)**

1. **Headers.** `Cache-Control: no-store` present on writers and errors; **no `ETag`**; errors include `Content-Type: application/json; charset=utf-8`.  
2. **Errors.** Body is a typed, numeric-free error object; canonical emission; one LF; **no secrets/PII**.  
3. **Writers.** If body is absent, transport is compliant. If present, it honors the numeric-free covenant and canonical emission.  
4. **No misuse of 304\.** Writer and error responses **must not** use 304; conditional delivery applies **only** to cached 200s (see §10.2 and §2.0).  
5. **OPTIONS (writers).** 204, no body; under HTTP/2 `Content-Length: 0` may be omitted; **no** `ETag`/`Vary`/compression.  
6. **HEAD (writers).** Non-HEAD writers return 405 with `Content-Length: 0`.

**Tokens:** see §2.0 **Writer/Error & rails** tokens, including `WRITERS_OPTIONS_204_NO_BODY_OK`.

---

## 10.4 Aux Narrative suppression (carve-out) — Reader scope note

 **Purpose (normative).** Define the suppression behavior for the **Aux Narrative** surface **without changing** the Reader matrices.

**Behavior.**  When text is present: 200 text/plain; charset=utf-8 with a strong, quoted ETag and Vary: Authorization, Accept-Encoding. When suppressed: 200 with an empty body and no ETag; Vary: Authorization, Accept-Encoding is still present. A policy header may be present as a generic signal (X-Narrative-Policy: suppressed). This carve-out applies only to Aux Narrative. Reader transport rules in §10.1–§10.3 remain unchanged and are fully governed by A7 (success on Catalog routes only). Aux HEAD and 304 are out of scope for EPIC-010.

**Acceptance (binary)**

1. **Suppression case.** Header snapshot shows `200`, **no body**, **no `ETag`**.  
2. **Non-suppressed cases.** Reader responses continue to meet **§10.1–§10.3**.

**Evidence (titles-only).** Add a **suppression header snapshot** entry in PF12 (update **human** `docs/evidence/INDEX.json` \+ **hash sentinel** and **machine** `artifacts/evidence_index.jsonl` **in the same PR**).

**Tokens (titles-only).** `AUX_A7_GET_QUOTED_ETAG_OK` · `AUX_A7_HEAD_PARITY_OK` · `AUX_A7_304_OMITS_CT_CL_OK` · `AUX_200_SUPPRESS_EMPTY_NO_ETAG_OK`.

---

## 10.5 Internal-ops surface: /internal/version

 **Intent and scope.** **Internal-only** identity/version surface for operators. **Not** a public Reader success route; **A7 does not apply**.

**Methods and status**

* Supports **GET** and **HEAD**.  
* **Content-Type on 200:** `application/json; charset=utf-8`.  
* **HEAD parity:** HEAD returns **200**, mirrors GET validators, **empty body**; `Content-Length == len(identity GET body)` (LF-terminated bytes); `Content-Type == GET`.  
* Always returns **200** on success. *(Production override ⇒ `400` JSON with `Cache-Control: no-store`, no `ETag`, when an override is explicitly denied.)*

**Caching and validators**

* **Cache-Control: `no-store`** on **all** responses.  
* **No `ETag`** and **no `Last-Modified`** on this surface.  
* Conditional request headers are **ignored**; **never 304** on this surface.  
* `Vary` is **optional** (may be present; not required for acceptance).

**Payload (frozen minimal identity).** Expose **exactly six** provenance fields; **no extra fields**:

1. `engine_tag`  
2. `build_commit`  
3. `invocation_tag`  
4. `invocation_sha256`  
5. `emitter_sha256`  
6. `release_id`  
    Canonical JSON; UTF-8; compact separators; **exactly one trailing LF**.

**Acceptance (binary gates)**

1. **INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK.** GET 200 includes `Content-Type: application/json; charset=utf-8`.  
2. **INTERNAL\_VERSION\_HEAD\_PARITY\_OK.** HEAD returns 200; mirrors GET validators; empty body; `Content-Length == len(identity GET)`; `Content-Type == GET`.  
3. **INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK.** `If-None-Match` / `If-Modified-Since` ignored; always 200 (**never 304**).  
4. **INTERNAL\_VERSION\_NO\_ETAG\_OK.** No `ETag` on GET/HEAD.  
5. **INTERNAL\_VERSION\_NO\_STORE\_OK.** `Cache-Control: no-store` present on GET/HEAD.

**Evidence (records-only; titles-only; indexed via PF12)**

* **intver/headers\_get** — raw GET response headers (proves `no-store`, no `ETag`, correct `Content-Type`).  
* **intver/headers\_head** — raw HEAD response headers (HEAD 200, `Content-Type` parity, `Content-Length ==` identity GET).  
* **intver/body\_get** — exact GET body bytes (LF-terminated; six keys; stable order) \+ sha256 record.  
* **intver/cond\_if\_none\_match** — GET with `If-None-Match` (still 200).  
* **intver/cond\_if\_modified\_since** — GET with `If-Modified-Since` (still 200).  
* **intver/two\_run\_identity** — two-run byte identity log.  
   *(Mirror records include: `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a co-located path-proof. Update the PF12 human index \+ hash sentinel and the machine mirror **in the same PR**.)*

**Routing (titles-only)**

* Contract bytes (examples/schema) for **GET /internal/version** live in **HDE-CLI-API-Vendor-Ref**.  
* Operational policy and runbooks live in **HDE-Governance** (this document).

**Prod QA note.** In production, `/internal/version` returns `application/json; charset=utf-8` with **`Cache-Control: no-store`**, **no `ETag`**, ignores conditional request headers (**never 304**), and **HEAD 200** mirrors GET validators with `Content-Length == GET` and `Content-Type == GET`. This surface is operator-only and is **not** a JSON success route.

# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**

## **11.1 Request shaping (owned here) \[Required-Now\]**

**Scope (normative).** This section pins the bytes used to construct HDAPI requests and to remap provider outcomes into typed, numeric-free errors. Rails posture (open/closed) is governed in §3; live-call behavior (timeouts/retries/backoff) is in §11.2.

### **11.1.1 Endpoint & method**

* **Primary endpoint:** `POST /v1/bodygraphs` (JSON).  
* **Alternate (optional):** `POST /v1/bodygraphs/simple` (feature-flagged; same headers/body).  
* **Base URL resolution:** `${HDAPI_BASE_URL}` (must be present & non-empty; see §3.3).  
* **Determinism:** URL construction is order-neutral (AB↔BA) and locale-neutral.

  ### **11.1.2 Canonical headers (dash-/case-exact)**

Send these verbatim; do not add others unless explicitly pinned here:

* `Accept: application/json`  
* `Content-Type: application/json; charset=utf-8`  
* `HD-Api-Key: <secret>`  
* `HD-Geocode-Key: <secret>`  
* `User-Agent: GlowHDEngine/<release_id>` (release\_id from §5.1)

**Redaction:** Never log header values; secrets **MUST** be redacted in diagnostics (keys-only posture; §7.1, §8.2).

### **11.1.3 Request body schema (exact three keys) \[Required-Now\]**

**Normative rule.** The request **MUST** contain exactly three top-level fields—no others—and they **MUST** be formatted as follows:

1. {"birthdate":"DD-MMM-YYYY","birthtime":"HH:MM","location":"City, Country"}  
     
* **birthdate** — English month abbreviations `Jan..Dec`; day zero-padded (`01..31`); four-digit year. Examples: `03-Jan-1980`, `21-Sep-1995`.  
* **birthtime** — 24-hour `HH:MM`; zero-padded hour and minute (`00..23`, `00..59`). Examples: `00:00`, `09:30`, `23:59`.  
* **location** — ASCII English `"City, Country"`; a **single** comma \+ space separator; no leading/trailing spaces. Examples: `Paris, France`, `New York, USA`.

**Do not send `tz`.** The vendor derives timezone from location via geocoding; any `tz` field **MUST NOT** be present.  
 **Determinism.** Body construction is order-neutral (AB↔BA) and locale-neutral; no floats, wall-clock, or platform-dependent formatting.

**Validation & failure posture.**

* If any field is missing, extra, or malformed, the client **MUST** fail locally with a **typed, numeric-free error** (LF-terminated) and **MUST NOT** attempt network I/O.  
* Whitespace and casing rules above are normative; violations are treated as schema errors.

  ### **11.1.4 Typed error mapping (provider → CLI/Reader)**

Provider outcomes **MUST** be remapped to these typed, numeric-free errors (no vendor payload echo):

* **401 → `PROVIDER_UNAUTHORIZED`**  
* **403 → `PROVIDER_FORBIDDEN`**  
* **404 → `PROVIDER_NOT_FOUND`**  
* **429 → `PROVIDER_RATE_LIMITED`**  
  * If a valid `Retry-After` header is present, deterministically parse (delta-seconds or RFC-date) to integer `retry_after_ms`; on invalid/unsupported header, omit the field.  
* **5xx → `PROVIDER_UNAVAILABLE`**  
* **Malformed / bad JSON → `PROVIDER_BAD_RESPONSE`** (schema/mapping failure)

**Emission.** Error objects are serialized by the **single presenter emitter** and LF-terminated (see A-gates and transport rules).

### **11.1.5 Rails coupling (pointer)**

* **Rails closed (default; §3.1):** perform **no network I/O**; it is permissible to compute deterministic shaping (URL/headers/body) for diagnostics, but return a **typed refusal** and keep logs secret-free (keys-only).  
* **Rails open:** request shaping remains identical; live-call policy is pinned in §11.2.

  ### **11.1.6 Acceptance (binary)**

To pass governance:

1. **Shaping is canonical:** endpoint, headers, and body exactly match §§11.1.1–11.1.3; order-/locale-neutral construction.  
2. **Typed mapping proven:** provider statuses remap only to the tokens above; optional `retry_after_ms` is parsed deterministically.  
3. **Logging hygiene:** no payloads or header values; secrets redacted; labels bounded (per §7.1/§8.2).  
4. **A-gates unaffected:** Reader↔CLI parity and idempotence (A3/A4) remain unchanged by vendor paths.  
5. **Evidence:** index redacted examples/mapping tests in Appendix D (titles/paths only); keep synchronized with repo changes.  
   ---

## **11.2 Live call policy \[Speculative\]**

**Scope (normative, draft).** This section defines the closed, deterministic policy for live vendor calls made **only** when rails are open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`). It pins enum domains and governance rules; exact numeric selections are chosen before enablement and recorded via Doc-Delta.

### **11.2.1 Prerequisites & posture**

* **Rails open:** both gates satisfied (see §3.1); required env present/non-empty (see §3.3).  
* **Shaping fixed:** endpoint, headers, and body exactly as in §11.1.  
* **Determinism first:** no locale/time/random dependencies in policy selection; no payload/secret logging (keys-only).

### **11.2.2 Timeouts (closed integers; pick one profile)**

* **Profiles (enum):** `timeout_profile ∈ {small, default, long}`.  
* **Domains (ms):**  
  * `connect_timeout_ms ∈ {1000, 2000, 5000}`  
  * `read_timeout_ms ∈ {2000, 5000, 10000}`  
  * `total_timeout_ms ∈ {5000, 10000, 15000, 30000}`  
* **Rule:** pick **one** profile per environment; no per-request adaptation. Respect `total_timeout_ms` for all scheduling.

### **11.2.3 Retries & backoff (closed, no jitter)**

* **Retries:** `max_attempts ∈ {0,1,2,3}` (includes the first try). Retry classes: `{network_error, 5xx, 429}` only.  
* **Backoff enum:** `backoff ∈ {none, fixed, exponential}`.  
* **Backoff params (ms):**  
  * `fixed_delay_ms ∈ {250, 500, 1000}`  
  * `exp_base_ms ∈ {250, 500}`, `exp_factor = 2`, `exp_ceiling_ms ∈ {1000, 2000, 4000}`  
* **Schedule:**  
  * `none → 0 ms`; `fixed →` repeat `fixed_delay_ms`;  
  * `exponential → min(exp_base_ms * 2^(n-1), exp_ceiling_ms)` for attempt `n ≥ 2`.  
* **Budget:** never exceed `total_timeout_ms`; **no jitter**.

### **11.2.4 429 handling (deterministic)**

* **Typed error:** map to `PROVIDER_RATE_LIMITED` (see §11.1.4); no payload echo.  
* **Retry-After parse:** if present, deterministically parse delta-seconds or HTTP-date → `retry_after_ms` (integer); invalid header → omit the field.  
* **Optional retry on 429:** enabled only when policy pins `retry_on_429=true`; then apply the same backoff and respect `max_attempts` and the total time budget.

### **11.2.5 Observability (non-PII; bounded labels)**

* **Counters/timers/histograms (examples):** `vendor.req_total`, `vendor.req_success`, `vendor.req_error_{class}`, `vendor.retry_attempts`, `vendor.latency_ms` (bounded buckets).  
* **Labels (bounded):** `route`, `outcome ∈ {ok, network_error, 4xx, 5xx, 429}`, `rails_state ∈ {open,closed}`, `timeout_profile`, `attempt_idx`.  
* **Keys-only logs:** never log request/response bodies or header values; secrets always redacted (see §7.1, §8.2).

### **11.2.6 Acceptance to flip rails (controlled integration)**

Before enabling live calls in any environment, a Doc-Delta **MUST** pin the selections and evidence must pass:

1. **Policy pinning:** choose one timeout profile, `max_attempts`, backoff, and 429 handling.  
2. **Redaction tests:** prove logs contain no secrets/payloads; only bounded labels.  
3. **Refusal proof:** with rails closed, show deterministic refusal and correct shaping (no I/O).  
4. **Open-rails conformance:** with rails open, prove success, retry, and 429 paths follow pinned policy; parity/idempotence (A3/A4) unaffected.  
5. **Evidence index:** update Appendix D (titles/paths only) and add a Change Log entry for the pinned selections.

### **11.2.7 Change control**

Any change to selected timeouts/retries/backoff/429 settings, observability labels, or logging posture is a **normative** change and **requires a Doc-Delta**; if the math pack is unaffected, no new `release_id` is needed, but evidence must be refreshed.

# **12\. Gate Suites (Governance Gates) \[Required-Now\]**

## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**

**Anchors.** Use these exact IDs in evidence and Doc-Delta targets: `GATE:CORE-CANON`, `GATE:CORE-DET`, `GATE:CORE-READER`, `GATE:CORE-MATCH`.  
 All gates inherit the serializer and locale pins: UTF-8, sorted keys, compact separators (`,` and `:`), exactly one LF, `LC_ALL=C`, `TZ=UTC`. Any historic prompt or uncertainty checks are retired.

### **GATE:CORE-CANON — Canonical emission and comparators \[Required-Now\]**

**Scope.** Canonical serializer and ordering rules across Reader and CLI. **Pass when (binary):**

* Public bytes are produced by the single presenter/emitter; no ad hoc `json.dumps(`, `jsonify(`, or alternate emitters on public paths.  
* **Objects:** keys ASCII-sorted; compact separators; UTF-8; BOM/ANSI-free; exactly one LF.  
* **Arrays as sets:** dedupe by identity, then ASCII-sort; on value conflict, fail closed.  
* **Environment pins:** `LC_ALL=C`, `TZ=UTC`.  
   **Evidence.** Canonical re-serialize comparison; grep-guards (no `json.dumps` on public paths); LF/encoding checks.

### **GATE:CORE-DET — Determinism and identity \[Required-Now\]**

**Scope.** Idempotence, AB↔BA, two-run identity. **Pass when (binary):**

* **Preimage recipe:** build the preimage (without `idempotence_hash`), canonicalize, verify `sha256(preimage_bytes) == idempotence_hash`; then re-serialize canonically.  
* **AB↔BA identity** (pair normalization) and **two-run identity** hold byte-for-byte.  
* No nondeterminism on public paths from time, locale, randomness, or floating-point behavior.  
   **Evidence.** Preimage recompute logs; AB/BA and two-run byte-compare goldens.

### **GATE:CORE-READER — Public covenant and transport hooks \[Required-Now\]**

**Scope.** Reader v1 public body and A7 transport validators. **Pass when (binary):**

* **Success body:** six keys exactly (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*] == {id, band}` only (numeric-free).  
* **Errors:** typed, numeric-free JSON; canonical emission; one LF; no PII.  
* **Reader↔CLI parity:** bytes equal for identical inputs/environment (same emitter).  
* **A7 hooks present:**  
  * 200 has strong, quoted `ETag`; **Cache-Control: private, max-age=0, must-revalidate**; **Vary: Authorization, Accept-Encoding**.  
  * 304 only after a prior 200-with-body; **no body; omit `Content-Type` and `Content-Length`; validators mirror** the cached 200\.  
  * HEAD mirrors 200 validators; **no body; `Content-Length` equals identity 200; `Content-Type` equals GET**.  
  * Writers/errors: **Cache-Control: no-store** and **no `ETag`**; errors include `Content-Type: application/json; charset=utf-8`.  
  * **POST is non-conditional** (ignore `If-*` conditionals).  
     **Evidence.** Schema/shape tests; Reader↔CLI parity runs; A7 header snapshots.

### **GATE:CORE-MATCH — Compat math posture \[Required-Now\]**

**Scope.** Engine math visible at governance level (design in **HDE Math Spec**, titles only). **Pass when (binary):**

* **Closed sets:** Magic-10 category IDs and order fixed; band thresholds are inclusive maxima.  
* **Validation:** `viewer_prefs.weights` covers all 10 IDs with integers `0..100`; invalid shapes ⇒ typed failure.  
* **Determinism:** AB↔BA and two-run identity hold for internal scoring; fixed-point arithmetic with round away-from-zero and clamp to `[0..100]`.  
* **Public boundary:** no public numerics; Reader v1 remains `{id, band}` only (compat internals do not leak).  
   **Evidence.** Validator tests; fixed-point boundary goldens; proofs of “no public numerics” in success bodies.

**Note.** Any previously listed gate checks for prompt or uncertainty are removed from governance. Those features are retired and must not appear in public payloads or acceptance criteria.

## **12.2 Evidence links (titles-only) \[Required-Now\]**

**Titles and paths only; no payload bytes.** Keep this list synchronized with **Appendix D: Evidence Index** (that index remains the single source of truth). Update both in the same commit/PR when any golden or script path moves.

### **GATE:CORE-CANON — Canonical emission and comparators**

* Tests: `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`  
* Grep-guards and allowlist: `ci/grep-guards/canonical_emitter.allowlist`, `ci/grep-guards/no_json_dumps_public.regex`  
* Schema (success and error shapes): `schemas/reader.v1.schema.json`

### **GATE:CORE-DET — Determinism and identity**

* Goldens (AB↔BA, two-run): `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Idempotence recompute and parity scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Identity marker (preimage → sha256 → final): `artifacts/cards/A3/IDENTITY_OK.txt`

### **GATE:CORE-READER — Public covenant and transport hooks**

* Schema and shape (six-key success; `{id, band}` only): `schemas/reader.v1.schema.json`  
* Reader↔CLI parity (dev harness and tests): `adapter/http_reader.py` (dev-only harness), `tests/reader_v1/test_emitter.py`, `tests/cli/test_cli_stdout_schema_and_lf.py`  
* A7 transport snapshots (validators):  
   `tests/transport/headers/etag_200.snap`,  
   `tests/transport/headers/cond_304.snap`,  
   `tests/transport/headers/head_parity.snap`,  
   `tests/transport/headers/no_store_writers_errors.snap`  
* For internal-ops transport evidence of `/internal/version`, see **Appendix D: D.8** (titles only).

### **GATE:CORE-MATCH — Compat math posture**

* Validation (viewer prefs, closed sets): `tests/validation/viewer_prefs/*`  
* Fixed-point boundary and rounding (away-from-zero; clamp): `tests/compat/fixed_point/*`  
* Band thresholds (inclusive maxima): `tests/compat/bands_thresholds/*`  
* Public numeric ban (no scores on success): `ci/grep-guards/public_numeric_ban.regex`

**Maintenance rule.** Whenever a golden, snapshot, or script path changes, **Appendix D: Evidence Index** **MUST** be updated in the same commit/PR, and add a one-line entry to **§9 Change Management: Doc-Delta Hooks**.

---

* 

# **13\. Versioning & Compatibility \[Required-Now\]**

## **13.1 Reader versioning (v1) \[Required-Now\]**

**Principle (normative).**  
 **Reader v1** is a **strict** public contract. Success bodies contain **exactly six** top-level keys and a **bands-only** `categories` array. Any change that alters this public shape or its semantics is a **versioned change** (Reader v2+).

### **13.1.1 v1 success contract (strict)**

* **Six keys exactly:** `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`.  
* **`categories` items:** **exactly** `{ "id": <string>, "band": <"Cool"|"Open"|"Warm"|"Glow"> }` (numeric-free).  
* **Serialization:** canonical emitter (UTF-8, sorted keys, compact separators), **exactly one** trailing LF; `idempotence_hash` computed over the **five-key** preimage.  
* **v1 Alpha policy:** when `eligible==true`, public `categories` has **one** item with `id:"harmony"`; when `eligible==false`, `categories` **may** be empty.

### **13.1.2 Error contract (typed)**

* **Typed, numeric-free error:** `{ "ok": false, "code": "<token>", "error": "<non-PII message>" }` (+ optional `retry_after_ms` under pinned vendor policy).  
* **Same emitter rules:** canonical JSON; **one** trailing LF; **no** PII/secrets or payload echo.

### **13.1.3 What requires a Reader version bump (v2+)**

* Adding, renaming, or removing **any** top-level success key (beyond the six).  
* Adding **any** field to `categories[*]` (e.g., `score`, `prompt`, keys).  
* Changing the **allowed enum** for `band` or the **public** category exposure policy (e.g., exposing full Magic-10).  
* Changing the **canonical serialization** rules (UTF-8, sorted keys, compact, **one** LF) or the **preimage recipe**.  
* Changing the **typed error** public shape.

### **13.1.4 What does not require a Reader version bump (governed elsewhere)**

* Changing **math internals** (scores, presets, thresholds) while keeping the public v1 payload numeric-free and schema-conformant (may change `release_id`).  
* Changing **transport policy** within A7 (headers/conditional delivery as defined in §10) with no change to public body bytes.  
* Changing **rails** policy for vendor ingest (enablement, timeouts/retries/backoff) with no change to public body bytes.

These changes still require a **Doc-Delta** and updated evidence; if they alter frozen math, they produce a new **`release_id`** (§5.1).

### **13.1.5 Compatibility & validation (binary)**

* **Schema gate:** v1 success bodies validate the six-key schema; `categories[*] == {id,band}` only.  
* **Parity/identity:** A3/A4 gates pass (AB↔BA, two-run, Reader↔CLI byte equality; preimage re-check).  
* **A7 transport:** v1 responses follow §10 (ETag on 200; 304-after-200; HEAD parity; `no-store` & no ETag on writers/errors).  
* **Evidence:** goldens and scripts indexed in **Appendix D — Evidence Index** (titles/paths only).

### **13.1.6 Change control**

* **Public shape change ⇒ version bump.** Any proposal to alter the v1 contract **MUST** define a **Reader v2** (or higher) with updated schema, acceptance, and migration notes; land via Doc-Delta with full evidence.  
* **No silent drift.** Adding “optional” public fields under v1 is **prohibited**; clients and CI validate **strict equality** to the v1 schema.

## **13.2 Presets/evolution policy \[Required-Now\]**

**Governance stance (normative).**  
 Presets are a **frozen, cataloged control surface** for internal scoring/aggregation. They **MUST NOT** change the public Reader v1 covenant (numeric-free; `{id, band}` only) and are promoted via the **freeze-pack** process. Arithmetic and schema details are **owned by Math** and are referenced here **by title only**.

### **13.2.1 Ownership & routing**

* **This document (Governance) owns:** enable/disable posture, promotion/rollback rules, evidence requirements, and Doc-Delta/process gates.  
* **Math (titles-only) owns:** preset **schema**, arithmetic (weights, caps/floors, dampeners, cross-family corrections, micro posture), and the closed vocab domains used by presets. No arithmetic is duplicated here.

### **13.2.2 Change control (freeze-pack impact)**

* **Preset changes ⇒ new `release_id`.** Adding/removing a preset, or changing preset **weights**, **caps/floors**, **dampeners**, **cross-family** hints, **micro** posture, or the preset **schema** is a **math change** and **MUST** be captured in the freeze-pack; promotion requires a **new `release_id`** (see §5.1).  
* **Precedence policy.** If presets co-exist with viewer weights, the **deterministic precedence policy** must be **pinned by title** (Math/CLI reference). Changing that policy requires a **Doc-Delta** and updated evidence.  
* **No public drift.** Preset evolution **MUST NOT** introduce public numerics or new public fields under Reader v1 (see §13.1).

  ### **13.2.3 Acceptance to land (binary)**

* Schema validation (titles-only). Every preset validates against the Math-owned schema (exact Magic-10 keys; integers 0..100; closed enums for caps/dampeners).  
* Determinism. Fixed-point arithmetic with **round away-from-zero**; AB↔BA and two-run identity hold under the selected preset(s).  
* Public covenant. Reader v1 success remains {id, band} only; no changes to six-key shape or error model.  
* Evidence. Update Appendix D — Evidence Index with preset schema passes, fixed-point boundary goldens, and parity/identity runs; add a Doc-Delta entry in §9.

### **13.2.4 Versioning posture**

* **No Reader version bump** is required for preset changes that keep the v1 public covenant intact (they still yield a new `release_id`).  
* **Reader version bump (v2+)** is required **only** if preset behavior would change the **public** contract (e.g., exposing additional public categories or public numerics). Such proposals must define the new version and land via Doc-Delta with full evidence (see §13.1).

  # **14\. Retired Features \[Normative Notice\]**

  ## **14.1 Prompt \[Required-Now\]**

* **Status:** Removed from the public contract.  
* **Scope of removal:** The `prompt` field is **disallowed** in all public payloads and **must not** be preserved or injected by the Presenter. Any prior optional `categories[*].prompt` schema property is **deleted**; public items remain exactly `{id, band}`.  
* **Administrative surfaces:** `prompt` **must not** appear on admin/dev payloads either (keep parity with public).  
* **Rationale (one line):** Reader v1 is numeric-free and narrative-free; `prompt` risks drift without advancing the math contract.  
* **Effective date:** **2025-10-19**; first removed in the **Math & Technical Spec** (review) and retained through subsequent cuts (titles-only reference).

  ## **14.2 Uncertainty \[Required-Now\]**

* **Status:** Never shipped; any references are **excised** from this governance and related specs.  
* **Scope:** No uncertainty fields, tokens, or narratives are defined or permitted on public or admin surfaces.  
* **Rationale (one line):** Uncertainty signaling is out of scope for Reader v1 and introduces non-deterministic interpretations inconsistent with the fixed math contract.  
* **Effective date:** **2025-10-19**; scrub completed across **Review** documents. No operational impact on the current public contract.

# **15\. Open Toggles & Questions \[Open\]**

## **15.1 Feature toggles (default OFF)**

* **Default posture.** All feature toggles are **OFF by default** in all environments.  
* **Activation requirements (binary).** A toggle may be turned **ON** only with:  
  1. an **approved Doc-Delta** that pins scope and affected sections,  
  2. **new/updated goldens** and CI jobs for the implicated gates (A3/A4/A7/rails), and  
  3. updated **Evidence Index** entries (Appendix D) in the **same change**.  
* **Rollout guardrails.** Prefer **staged canary** with time-boxed scope; do **not** change public bytes or schemas under Reader v1; use **pointer-flip** rollback if acceptance fails (§5.2).

## **15.2 Open issues list**

Keep this list short and actionable. Each item has an **owner**, a **next step**, and a **target Doc-Delta** or **deadline**.

* **OI-001 — Reader v2 planning (full Magic-10 exposure).**

  * *Owner:* Architecture \+ Math leads  
  * *Next step:* Draft v2 public schema \+ acceptance; define migration plan; Doc-Delta proposal  
  * *Status:* OPEN  
* **OI-002 — Preset precedence vs viewer weights (pinning).**

  * *Owner:* Math \+ CLI  
  * *Next step:* Route final policy by title (CLI/Math); add tests; Doc-Delta  
  * *Status:* OPEN  
* **OI-003 — Vendor open-rails pilot (timeouts/retries/backoff/429).**

  * *Owner:* Transport  
  * *Next step:* Pin profile enums; add integration job; Doc-Delta to flip rails; redaction proof  
  * *Status:* OPEN  
* **OI-004 — Serializer unification proof in CI (symbol allowlist).**

  * *Owner:* Platform  
  * *Next step:* Add symbol-level emitter check; extend grep-guards; refresh parity/idempotence goldens  
  * *Status:* OPEN  
* **OI-005 — A7 HEAD `Content-Length` verification on large bodies.**

  * *Owner:* Transport  
  * *Next step:* Add header snapshot test for edge cases; Doc-Delta if matrix changes  
  * *Status:* OPEN

Update this list as items close; each closure should cite the Doc-Delta ID and the Evidence Index entries that were updated in the same change.

# **Appendices \[Informative / Reference\]**

## **Appendix A — Transport Matrices (Reader) \[Required-Now\]**

**Governance.** This appendix defines the required headers and conditional rules for Reader responses. Transport **bytes and examples** live by title in **HDE-CLI-API-Vendor-Ref**; this section governs policy only. No payload bytes appear in this document.

### **A.1 Success (200) — required headers**

* **Content-Type:** `application/json; charset=utf-8` — UTF-8 JSON; BOM/ANSI-free.  
* **ETag:** `"strong, quoted"` — identity over the final LF-terminated body (canonical JSON per HDE-Schemas & Artifacts, pre-compression); encoding-invariant.  
* **Vary:** `Authorization, Accept-Encoding` — at minimum.  
* **Cache-Control:** `private, max-age=0, must-revalidate` — required on 200 (and mirrored on HEAD; see A.4).

### **A.2 Success (200) — body covenant**

* **Six keys exactly:** `reader_version, eligible, categories, meta, release_id, idempotence_hash`.  
* **Categories policy (v1):** `categories[*] == { id, band }` only (numeric-free); v1 Alpha: single `{"id":"harmony","band":…}` when `eligible == true`.  
* **Canonical emission:** UTF-8, sorted keys, compact separators, exactly one LF.  
* **Idempotence:** `idempotence_hash = sha256(preimage_bytes)` where the preimage fields are defined in HDE-Math-Spec (no local restatement here).

### **A.3 304 Not Modified (conditional GET)**

* **Precondition (strong ETag).** A prior 200 OK with a strong, quoted `ETag` **MUST** exist for the same resource, and the request **MUST** present a matching `If-None-Match`.  
* **Shape.** **No body; omit both `Content-Type` and `Content-Length`.**  
* **Validators.** Repeat the validators from the cached 200 (for example, `ETag`, `Vary`, `Cache-Control`).  
* **Writers/errors excluded.** Never use 304 for writers or error responses; those responses **MUST** send `Cache-Control: no-store` and **MUST NOT** send `ETag`.

### **A.4 HEAD parity**

* **Headers mirror 200** (strong quoted `ETag`; `Vary: Authorization, Accept-Encoding`; `Cache-Control: private, max-age=0, must-revalidate`; `Content-Type: application/json; charset=utf-8`).  
* **No body;** `Content-Length == len(identity 200 body)` (canonical LF-terminated bytes, pre-compression).  
* **Encoding invariance.** Identity (`ETag`) is unchanged by accepted `Accept-Encoding` selections.

### **A.5 Writers & errors**

* `Cache-Control: no-store` on **all** writers and **all** error responses.  
* **No `ETag`** on writers/errors.  
* **Errors.** `Content-Type: application/json; charset=utf-8`; typed errors only (numeric-free code/message object), LF-terminated; no PII; no vendor payload echo.  
* **Writers (success-without-body).** Typically `204 No Content`; if a body is emitted for diagnostics, it **MUST** be typed, minimal, numeric-free, and canonically serialized (LF-terminated).  
* **POST is non-conditional.** Ignore `If-*` conditionals for POST; writers/errors never return 304\.

**Writers — OPTIONS/HEAD semantics (normative).**

* **OPTIONS → 204 (no body).** For writer resources, OPTIONS **MUST** return 204 with no body; no `ETag`/`Vary`/compression. Under HTTP/2, `Content-Length: 0` may be omitted.  
* **HEAD 405 (strict).** Writers’ HEAD on non-HEAD writer routes returns 405; include `Content-Length: 0`.

### **A.6 Examples (titles-only; no payload bytes)**

* Success \+ ETag (200) — Transport: Success 200 headers (cataloged endpoint)  
* Conditional GET (304) — Transport: Conditional 304 headers (cataloged endpoint)  
* HEAD parity — Transport: HEAD-vs-200 parity headers  
* Writers/errors — Transport: no-store \+ no-ETag headers  
   *(Keep these titles synchronized with Appendix D: Evidence Index and the machine JSONL mirror; update both in the same change when snapshots move.)*

### **A.7 Acceptance checklist (binary)**

1. **200:** strong, quoted `ETag`; body meets six-key covenant; LF/encoding OK; `Cache-Control: private, max-age=0, must-revalidate` present; `Vary` present; encoding-invariant `ETag`.  
2. **304:** served only **after 200**; **no body**; validators mirror 200; **`Content-Type` omitted; `Content-Length` omitted.**  
3. **HEAD:** mirrors all 200 validators (including `Content-Type`); no body; `Content-Length` matches identity 200\.  
4. **Writers/errors:** send `no-store` and no `ETag`; typed error shape and LF present.  
5. **Evidence:** snapshots exist and are indexed in Appendix D (titles/records only) and mirrored in the machine JSONL **with path-proofs**.  
6. **POST non-conditional:** POST responses never return 304 and do not honor request validators.  
7. **Proof endpoint:** A7 proofs are run on an **HDE-CLI-API-Vendor-Ref** Endpoint Catalog (success JSON) route (titles-only reference).

---

## **Appendix B — Acceptance Gate Details \[Required-Now\]**

Titles and paths only; no payload bytes. This appendix lists gate checklists and CI jobs that enforce them. Keep it synchronized with **Appendix D — Evidence Index** and CI config in the same change.

### **B.1 GATE:CORE-CANON — Canonical emission and comparators**

* **Checklist (binary):** single presenter/emitter; UTF-8; sorted keys; compact separators; one LF; arrays-as-sets deduped and ASCII-sorted; conflict ⇒ fail-closed; `LC_ALL=C`.  
* **CI jobs (titles-only):**  
  * `ci/jobs/canonical_emitter_symbol_check.yml`  
  * `ci/jobs/no_json_dumps_public_guard.yml`  
  * `ci/jobs/lf_and_encoding_check.yml`

### **B.2 GATE:CORE-DET — Determinism and identity**

* **Checklist (binary):** preimage (five-key) → `sha256` → final; AB↔BA byte-equality; two-run identity.  
* **CI jobs (titles-only):**  
  * `ci/jobs/preimage_recompute_and_compare.yml`  
  * `ci/jobs/ab_ba_parity_bytecompare.yml`  
  * `ci/jobs/two_run_identity_bytecompare.yml`

### **B.3 GATE:CORE-READER — Public covenant and transport hooks**

* **Checklist (binary):** success \= six keys; `categories[*] == {id, band}` (numeric-free); typed error shape; Reader↔CLI byte-equality; A7 hooks present.  
* **CI jobs (titles-only):**  
  * `ci/jobs/schema_shape_success.yml`  
  * `ci/jobs/schema_shape_error.yml`  
  * `ci/jobs/reader_cli_parity.yml`

### **B.4 A7 — Transport tokens (200 / 304 / HEAD / writers+errors)**

**Proof surface.** A7 proofs run on a **Catalog JSON success** route listed in PF05 §5.6 (titles-only); **not** on `/internal/version`.

* **Checklist (binary):**  
  * **200:** strong, quoted ETag present; `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
  * **304:** only after a prior 200-with-body; no body; validators mirror 200; **omit** `Content-Type`; **omit** `Content-Length`; ETag present.  
  * **HEAD:** validators mirror 200; no body; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
  * **Writers/Errors:** `Cache-Control: no-store`; no ETag; errors include `Content-Type: application/json; charset=utf-8`.  
  * **Encoding invariance:** for the same canonical body, identity (ETag) and effective length are stable across accepted `Accept-Encoding`.  
* **CI jobs (titles-only):**  
  * `ci/jobs/transport_etag_200.yml`  
  * `ci/jobs/transport_conditional_304.yml`  
  * `ci/jobs/transport_head_parity.yml`  
  * `ci/jobs/transport_no_store_writers_errors.yml`

### **B.5 Rails posture — Closed refusal / Open conformance**

* **Checklist (binary):** closed ⇒ no network I/O, typed refusal, keys-only logs; open ⇒ pinned timeouts/retries/backoff/429, deterministic mapping, no payload/secret logging; parity/idempotence unaffected.  
* **CI jobs (titles-only):**  
  * `ci/jobs/rails_closed_refusal.yml`  
  * `ci/jobs/rails_open_conformance.yml`  
  * `ci/jobs/logs_keys_only_redaction.yml`

### **B.6 GATE:CORE-MATCH — Compat math posture (titles-only; math owned in spec)**

* **Checklist (binary):** closed Magic-10 IDs/order; inclusive maxima thresholds; viewer prefs ints `0..100`; fixed-point with round away-from-zero and clamp `[0..100]`; no public numerics.  
* **CI jobs (titles-only):**  
  * `ci/jobs/validation_viewer_prefs.yml`  
  * `ci/jobs/fixed_point_rounding_and_clamp.yml`  
  * `ci/jobs/band_thresholds_inclusive.yml`  
  * `ci/jobs/public_numeric_ban_guard.yml`

**Maintenance rule (MUST).** When a gate’s golden/snapshot/script path changes, update **Appendix D — Evidence Index** and the corresponding CI job references here **in the same change**, and add a one-line entry in **§9 Change Management — Doc-Delta Hooks**.

---

## **Appendix C — Bench & Ops Runbook \[Required-Now\]**

Titles/paths only — no payload bytes. This runbook defines how to run the bench harness and verify SLOs. Keep references synchronized with **Appendix D — Evidence Index** and CI config in the same change.

### **C.1 Purpose & scope**

* Prove determinism (A3), Reader↔CLI parity (A4), and transport invariants (A7) under load, without PII or payload logging.  
* Produce bounded latency histograms and percentile summaries (p95/p99).  
* Support promotion/rollback decisions (see §5.2).

  ### **C.2 Bench profiles (titles-only)**

* **Math/transport profile (rails closed).** Deterministic engine \+ presenter; no network I/O.  
* **Vendor profile (rails open).** Timeouts/retries/backoff per §11.2; typed mapping; keys-only logs. Pin profile names/arguments in repo scripts (see Appendix D).

  ### **C.3 Usage recipe (deterministic runs)**

1. **Prepare fixtures & env.** Fixed fixture set, pinned env; do not vary counts/data between cuts.  
2. **Warm-up then measure.** Discard warm-up; collect metrics during a fixed measurement window.  
3. **Collect checks.**  
   * Parity & identity: AB↔BA, two-run, Reader↔CLI byte-compare; preimage → sha256 → final.  
   * A7 spot checks (dev harness): ETag on 200; 304-after-200; HEAD parity; no-store on writers/errors.  
4. **Capture histograms/counters.** Engine/presenter/reader latency buckets; outcome counters with bounded labels.  
5. **Write artifacts (titles/paths only).** Bench report (percentiles \+ histogram snapshot), parity/identity logs, A7 header snapshots.

   ### **C.4 SLO verification (binary)**

* **Inputs:** bench report for current cut; pinned SLO targets (§6.2).  
* **Pass when:** (1) p95/p99 thresholds met by profile/metric; (2) A3/A4 pass in the same runs; (3) A7 spot checks pass; (4) rails posture honored.  
* **Fail posture:** stop canary or rollback via pointer-flip (§5.2); open investigation.

  ### **C.5 Reporting & evidence (titles-only)**

* **Bench report:** `artifacts/bench/bench_report_{release_id}.json`  
* **Parity/identity logs:** `artifacts/bench/parity_identity_{release_id}.log`  
* **Transport snapshots:** `artifacts/bench/transport_headers_{release_id}/…`  
* **Indexing:** update **Appendix D — Evidence Index** in the same change.

  ### **C.6 CI hooks (titles-only)**

* **Jobs:** `ci/jobs/bench_math_transport.yml` (rails closed) `ci/jobs/bench_vendor_open.yml` (rails open; policy pinned) `ci/jobs/slo_verify.yml` (compare report vs targets)  
* **Guards:** enforce keys-only logging; fail on payload/body/header-value patterns; assert one LF and canonical encoding on emitted JSON.

  ### **C.7 Ops notes**

* **No schema drift.** Bench harness must not alter public bytes or schemas.  
* **Keys-only logs.** Never log payloads or header values; secrets always redacted (see §7.1, §8.2).  
* **Pointer discipline.** Promotions/rollbacks are pointer flips to `release_id`; record outcomes in the Change Log and update Appendix D.  
  ---

Absolutely—here’s a clean, merged, and *logically ordered* **Appendix D** that applies your deltas to the current version. I’ve:

* Kept your existing intent and language style.  
* Applied the delta structure (D.0 → D.11), with your prior content merged where appropriate.  
* Removed duplicates (e.g., DB posture split across two places; refusal/A7 items repeated).  
* Preserved extra evidence families you already had (Bands/Pack/Topology) by moving them after the new D.11, so nothing is lost.

Paste this over your current Appendix D.

---

## **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**

**Single-home rule.** PF12 governs the **human Evidence Index** (`docs/evidence/INDEX.json`), the **hash sentinel** (`docs/evidence/INDEX.sha256`), and the **machine JSONL mirror** (`artifacts/evidence_index.jsonl`). **Update all three in the same PR** when any governed artifact changes. The mirror is **one file**, **records-only canonical JSONL** (UTF-8; sorted keys; compact; **one LF**); **ASCII field order**; **sort-before-write**; **unknown-keys rejected**; each record includes a **`proof_anchor`** to a co-located path-proof.

**Governed locations only.** Store proofs under `artifacts/**` or `docs/**`; ephemeral generator paths are **not** authoritative.

---

### **D.0 Close-pack & release manifests (admin)**

* `audit/EPIC-009_close_report.md`  
* `audit/EPIC-009_MANIFEST.json`

---

### **D.1 Parity (Reader↔CLI, AB↔BA, two-run)**

* Goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Harness/tests: `tests/reader_v1/test_emitter.py`, `tests/cli/test_cli_stdout_schema_and_lf.py`  
* Byte-compare scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Composite fingerprint: `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`  
* Integration set: `fixtures/composite/integration_abba/*.json`, `audit/gates/determinism/abba_compare_integration.log`

---

### **D.2 LF & encoding discipline (UTF-8; one LF; no BOM/ANSI)**

* Checks/tests: `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`  
* CI guards: `ci/jobs/lf_and_encoding_check.yml`, `ci/grep-guards/no_ansi_no_bom.regex`

---

### **D.3 Idempotence coupling (preimage → sha256 → final)**

* Identity marker/logs: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Recompute scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Schema (success, six keys): `schemas/reader.v1.schema.json`

---

### **D.4 Endpoint Catalog & transport proofs (Reader A7)**

**Proof surface & posture (titles-only).**

* A7 proofs run **only** on a **cataloged JSON success** route (Endpoint Catalog; titles-only in CLI/API Vendor Ref).  
* The Catalog is **internal-only** and **env-gated**; **non-prod entries must be unreachable in prod** — capture a **headers-only env-gate** proof.  
* The `/internal/version` ops surface is **excluded** from A7.  
* Artifacts below are **records-only**; index each in the machine mirror; LF-terminated; header names **lower-case**; values **verbatim**.

**Catalog/A7 artifacts.**

* Catalog snapshot — `artifacts/reader/endpoints_snapshot.json`  
* Env-gate proof (headers-only; one LF) — `artifacts/proofs/endpoints_env_gate_proof.log`  
* Composite success proof (records-only JSON) — `artifacts/proofs/reader_success_get_head_304.json` *(PF12 schema; presence required)*  
* Optional encoding-invariance proof — `artifacts/proofs/encoding_invariance.txt`

**Aux Narrative (text) snapshots (headers-only).**

* `tests/transport/headers/aux_text_200.snap`  
* `tests/transport/headers/aux_head.snap`  
* `tests/transport/headers/aux_304.snap`  
* `tests/transport/headers/aux_suppression.snap`

**Catalog example (informative; titles-only).**

* `docs/ENDPOINTS_CATALOG.json`

**Writer/error posture (headers-only).**

* `tests/transport/headers/error_headers_utf8.snap`  
* `tests/transport/headers/no_store_writers_errors.snap`

**CI jobs (titles-only).**

* `ci/jobs/transport_etag_200.yml`  
* `ci/jobs/transport_conditional_304.yml`  
* `ci/jobs/transport_head_parity.yml`  
* `ci/jobs/transport_no_store_writers_errors.yml`

---

### **D.5 Rails posture (refusal & open conformance)**

* **Closed-rails refusal proof** (single-file canonical; headers → blank line → body): `artifacts/proofs/refusal_run.txt` *(format rules in PF12 §8.3.1)*  
* **Shaping correctness (closed rails):** `ci/jobs/logs_keys_only_redaction.yml`  
* **Open-rails conformance** (timeouts/retries/backoff profile): `ci/jobs/rails_open_conformance.yml`

---

### **D.6 Internal-ops surface: `/internal/version`**

* GET/HEAD headers/body capture — `artifacts/proofs/internal_version/get_head.json` *(or equivalent titles-only proof; ops-only, `no-store`, no `ETag`; conditionals ignored — **never 304**; HEAD mirrors GET with no body and equal identity length).*

---

### D.7 Database runtime posture (prod & dev)

Env snapshot — `artifacts/runtime/env_matrix.snapshot.json` (singleton; one file representing the default rails settings across environments, using the canonical v3 schema with uppercase rails keys such as `SAFE_MODE` and `ALLOW_NETWORK` and labeled policy fields; governed by `ENV_RAILS_POLICY_OK` and `ENV_LC_ALL_C_OK`).  
 Dev connectivity snapshot — `artifacts/runtime/env_connectivity.snapshot.json`  
 DDL/search\_path/grants set — `artifacts/db/check_schema.txt` (search\_path), `artifacts/db/grants.txt` (least-privilege), `artifacts/db/ddl_fingerprint.json` (normalized fingerprint), `artifacts/db/conn_env_selection.log` (selection proof)

(Tokens & policy live in §2.0 / §6.3.)

---

### **D.8 QA artifacts namespace (transient captures)**

* Namespace (titles-only): `artifacts/qa/` *(transient test-only; governed by PF12)*

---

### **D.9 BodyGraph adapter data-source & invariance (PF10-AA)**

* Source selection snapshot — `artifacts/bodygraph/source_selection.snapshot.json`  
* Source invariance (A→B) — `artifacts/bodygraph/source_invariance/ab.json`  
* Source invariance (B→A) — `artifacts/bodygraph/source_invariance/ba.json`  
* Summary — `artifacts/bodygraph/source_invariance/summary.json`  
* Release bindings — `artifacts/bodygraph/release_bindings.json`  
* Refresh/TTL/SWR policy snapshot — `artifacts/bodygraph/refresh_policy.snapshot.json`  
* Metrics snapshot (keys-only) — `artifacts/bodygraph/metrics.snapshot.json`  
* Keys-only logs sample (sanitized) — `artifacts/bodygraph/keys_only.logs.sample`

*(Narratives adapter/data-source policy is routed by title; evidence only.)*

---

### **D.10 Bands and thresholds (inclusive-high)**

* Edge proofs: `audit/gates/bands/edges.snapshot.json`, `audit/gates/bands/edges.diff.json` (boundaries at 24/49/74/100; see HDE Math Spec)  
* CI jobs: `ci/jobs/bands_edges_snapshot.yml`, `ci/jobs/bands_edges_diff.yml`

---

### **D.11 Pack constants and release identity**

* Constants pack (evidence snapshot): `artifacts/math/constants.json`, `artifacts/math/constants.json.sha256`  
* Manifest and release\_id: `catalog/manifest.json`, `artifacts/math/release_id_recompute.log`

---

### **D.12 Topology loader: orientation and graph invariants**

* Orientation demo: `audit/gates/topology/orientation_demo.txt` (before/after high–low → min→max NN-NN; arrays-as-sets deduped and ASCII-sorted)  
* Integration degree check: `audit/gates/topology/degree_check.log` (verifies 10/20/34/57 ⇒ degree 3; all other gates ⇒ degree 1\)  
* Center-pair multiplicity: `audit/gates/topology/multiplicity_vector.log` (unordered center-pair counts sum to 36\)

---

**Indexing discipline (reminder).** Every artifact listed in this appendix **must** be added to the **human** index and mirrored in `artifacts/evidence_index.jsonl` **in the same PR**, with a `proof_anchor` pointing to a path-proof stored alongside the artifact.

