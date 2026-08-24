# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF01-Canon-HDE-Math-Spec

**Version:** v1.3.7

**Status:** Canon

**Effective date:** 2026-08-25

**Last Update Gate:** BN 12.8.9

## **0.2 Change policy**

**Contract surface.** This spec is math-only. It does not define transport bytes, HTTP behavior, or operational policy. Those are referenced by title only:

* **HDE-CLI-API-Vendor-Ref:** CLI/Reader/vendor payloads, validators, header matrices, streams, and exit codes.  
* **HDE-Governance:** A7 transport, conditional delivery, caching and writers, SAFE rails, rate-limit and timeout acceptance. No duplicated bytes: if transport, ops, or policy details appear here, remove them and route by title to the owning document.

**Single-source math.** All normative math (algorithms, feature shapes, score formation) lives here. Any repository paths shown in examples are informative, never authoritative.

**Frozen inputs and release identity.** This specification requires its frozen math inputs to be represented in the pack manifest governed by **PF12-Canon-HDE-Schemas-and-Artifacts**. Repository conformance is assessed separately. The PF01-required frozen surface includes at least:

* **Feature-constants contract** (see §5.4.2): `limits.em_max`, `limits.throat_em_max`, `limits.centers_max`, `limits.motor_throat_max`, `limits.mind_throat_max`, and `limits.comp_max`; the current global score and band rules are governed separately at `math/thresholds.json`.  
* **Direct Motor→Throat set** (if catalogized in **PF12-Canon-HDE-Schemas-and-Artifacts**): governed four-channel set in canonical NN-NN; any change is frozen-input and bumps `release_id`.  
* **Magic-10 catalogs** (**PF12-Canon-HDE-Schemas-and-Artifacts**): `catalog/magic10.json` for the closed order and `catalog/magic10_caps.json` for category signal inputs and bounds.  
* **Topology catalogs** (**PF12-Canon-HDE-Schemas-and-Artifacts**): `catalog/gates_v1.json` and `catalog/channels_v1.json`; centers are derived from Gate rows and use canonical machine IDs.  
* **Seeds catalog** (when present): if Seeds are catalogized in **PF12-Canon-HDE-Schemas-and-Artifacts**, they are admin/test inputs and become frozen inputs that trigger a new `release_id` on change; Seeds are not public in v1.

**Frozen-input change ⇒ new `release_id`.** Any byte change to a frozen input or the manifest requires a Doc-Delta and a new `release_id` (**PF12-Canon-HDE-Schemas-and-Artifacts** §6: `release_id = sha256(canonical_bytes("catalog/manifest.json"))`).

**Canonical bytes** (**PF12-Canon-HDE-Schemas-and-Artifacts** §4). All governed JSON (including the manifest and any constants or catalog files) is serialized as UTF-8 without BOM, sorted keys, compact, with exactly one trailing LF; numbers are JSON numbers; arrays used as sets are deduplicated and ASCII-sorted. Hashing, parity, and equality checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. This spec references those rules and does not restate them.

**EPIC017 proof posture (informative).**  
EPIC017, as recorded in **HDE Phased Epics Map**, is associated with implementation and evidence intended to exercise the canonical-bytes and determinism rules defined in this spec. Static repository bytes do not establish execution, chronology, proof sufficiency, or acceptance. The recorded deliverables cover:

* canonical JSON (UTF-8, sorted keys, compact, one trailing LF)  
    
* arrays-as-sets (deduped and ASCII-sorted)  
    
* the `LC_ALL=C` / `LANG=C` / `TZ=UTC` posture for hashing and canonicalization  
    
* determinism evidence (AB↔BA identity, two-run identity, idempotence recompute)

The associated tests and evidence artifacts are owned by **HDE-Mechanics Guide** and **HDE-Build Checklist**. Their presence does not establish that they passed or that implementation is fully aligned. EPIC017 does **not** modify any math or canonical JSON semantics in this spec.

**Identifier and path policy** (**PF12-Canon-HDE-Schemas-and-Artifacts** §0.5 / §2.1). String IDs are ASCII and match `^[a-z0-9_]+$` (case-sensitive). Pack paths are POSIX (no `..`, no `//`, max 256 bytes). Centers are `snake_case` in outputs; Title Case is an ingestion alias.

**Process scope.** Build and CI flow, CodEx staging, and repo-docs updates live in **HDE-Build Notes** and **Epic-Process-Guide**. This spec remains contract-free for transport/ops and uses titles-only routing to those homes.

**Acceptance and evidence coupling.** Any change that touches frozen inputs or schema/identity must satisfy the applicable CI-token requirements and the Evidence Catalog contract owned by **PF12-Canon-HDE-Schemas-and-Artifacts**. This section retains only the applicable math acceptance-family names:

* **Pack/manifest and Evidence Catalog:** `RELEASE_ID_RECOMPUTE_OK`, `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Domains/catalogs:** `MAGIC10_DOMAIN_CLOSED_OK`, `M10_DEFS_OK`, `M10_SEEDS_OK` (when Seeds are catalogized), `CATALOG_ORIENTATION_CANON_OK`, `PREFS_KEYSET_10_OK`.  
* **Bands and rounding:** `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `ROUND_HALF_UP_OK`.  
* **Determinism:** `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.

**Token semantics.** Token semantics live in **HDE-Governance §2.0**; this document references token names only.

**Revision boundary.** PF01 states the current mathematical contract and does not maintain revision history or local workflow records. Changes to PF01-owned mathematics follow the current HDE-Governance controls. Governed artifact-byte changes follow the PF12 manifest and `release_id` rules.

---

## **0.3 Tagging convention (used throughout)**

* **\[Implemented\]** — Verified in the repo and exercised by surfaces/tests.  
    
* **\[Required-Now\]** — Required for current build goals; if missing in code, it is treated as a gap.  
    
* **\[Speculative\]** — Accepted future design; not yet wired. (Preserve math as-is; no public bytes until promoted.)

# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]

* **Public Reader v1 (bands-only, single “harmony”) — \[Required-Now\]**  
    
  * **Required contract.** The public envelope emits one category `{"id":"harmony","band": <Cool|Open|Warm|Glow>}` plus `eligible`, `meta:{engine_tag,invocation_tag}`, `release_id`, and `idempotence_hash`. Bytes are canonical JSON (UTF-8, sorted keys, compact, exactly one trailing `\n`). `idempotence_hash` is computed over the canonical preimage; **AB↔BA** and **two-run** identity are required (see §3.2 and §3.4).  
  * **Static implementation posture.** The pinned runtime emits the six-key envelope and computes the preimage hash, but it defaults `eligible` to `true`, retains the `harmony` item when `eligible == false`, and is not accepted by the checked-in success schema because that schema's category enum omits `harmony`. The schema and emitter also still permit `prompt`. These are implementation gaps; they do not weaken the public contract.  
  * **Evidence routing (titles-only).** Reader v1 emitter and canonical serializer; Reader/CLI sidecar parity; idempotence/preimage recompute. Evidence families and paths are owned by the Evidence Catalog in **PF12-Canon-HDE-Schemas-and-Artifacts**.  
  * **Scope note.** Transport/CLI specifics (headers, 304/HEAD, validators) live in **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles-only).


* **Determinism (LF, sorted keys, preimage hash, AB↔BA) — \[Required-Now\]**  
    
  * **Canonical JSON, one LF.** Public bytes are required to be emitted as UTF-8, sorted keys, compact separators, exactly one trailing `\n` (see **PF12-Canon-HDE-Schemas-and-Artifacts**). The pinned presenter and serializer statically implement this byte recipe; static inspection does not establish test passage.  
      
  * **Two-step idempotence.** Build the preimage (without `idempotence_hash`), compute `sha256(preimage_bytes)`, then re-emit with `idempotence_hash` inserted (see §3.2).  
      
  * **AB↔BA identity.** Pair inputs are normalized to a canonical order; order-neutral math is required so AB and BA produce byte-identical outputs (see §3.4).  
      
  * **Evidence (titles-only).** Reader/CLI sidecar schema and LF discipline, AB↔BA goldens, and idempotence recompute are governed evidence families in **PF12-Canon-HDE-Schemas-and-Artifacts**.  
      
  * **EPIC017 proof record (informative).**  
    EPIC017, as tracked in **HDE Phased Epics Map**, records deliverables intended to exercise the determinism invariants defined in this spec. Static repository bytes do not establish firstness, completeness, execution, or acceptance. The recorded deliverables cover:  
      
    * canonical JSON checks  
        
    * Reader↔CLI parity  
        
    * AB↔BA identity  
        
    * two-run identity  
        
    * idempotence-recompute harnesses

    

  * Acceptance tokens such as `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, and `COMPOSITE_ABBA_IDENTITY_OK` are mapped to evidence families owned by **PF12-Canon-HDE-Schemas-and-Artifacts** and acceptance semantics owned elsewhere. Their definitions do **not** introduce new math or an alternative determinism contract, and their presence does not establish a PASS.


* **Canonical Magic-10 (10 categories; scores→bands) — \[Required-Now\] (implementation gap; Reader projection remains harmony-only)**  
    
  * **Closed matrix.** Every eligible pair evaluation produces exactly one intrinsic integer score and band for each of the ten IDs in the frozen order governed by `catalog/magic10.json`; no partial, harmony-only, duplicate, defaulted, or eleventh result is conforming.  
  * **Human Design grounding.** Governed pair signals determine score magnitude. Person identifiers establish identity and canonical pair order only. Viewer preferences belong to sampler/ranker weighting and do not alter intrinsic compatibility scores or bands.  
  * **AB↔BA neutrality.** Validated normalized charts are ordered by ASCII `person_uid`; the canonical pair-signal map and deterministic reduction in §5.2 are order-neutral.  
  * **Deterministic scoring and banding.** Each category score is an integer in `0..100` produced by the half-unit reduction in §5.2, then mapped through the single global inclusive maxima `[24,49,74,100]` in §5.3.  
  * **Public projection.** Reader v1 exposes only the `harmony` band from the complete canonical matrix. It does not expose scores or the other nine categories.  
  * **Static implementation posture.** The pinned repository contains three noncanonical or transitional scorer surfaces and no complete ten-category implementation in `engine.core.core`; exact upstream mechanics for every governed pair signal are also not found. These are explicit implementation gaps.


* **Feature extractors (EM / Hanging Gates / Dominance–Compromise / Throat adjacency / …) — \[Required-Now\]**  
    
  * **Intent (one-liners).** Deterministic, pure signals for dyadic analysis (EM, HG, center balance, throat pathways, etc.), producing bounded enums/booleans for aggregation.  
  * **Common invariants.** Pure & deterministic (no time/network/random/file I/O); locale-neutral; AB↔BA symmetric; closed vocabularies; typed failures for unavailable states.  
  * **I/O shapes.** Inputs: normalized charts \+ frozen catalogs (titles-only). Outputs: small bounded maps (for example, `{ "em": true, "dominance": "g_identity", … }`); no narratives.  
  * **Acceptance requirement.** Unit goldens \+ property tests; catalog linkage; deterministic handoff to the §5.2 signal map; **no public surface in v1**. The pinned repository does not contain the complete required extractor and upstream signal-generation surface.


* **Presets & aggregation math — \[Speculative\]**  
    
  * **Posture.** Presets, alternative weights or scoring profiles, and the ungoverned advanced token-aggregation design are **Future-Promotion**. No current governed Presets catalog, Feature Registry, or token-aggregation contract exists.  
  * **Promotion boundary.** Promotion requires complete governed schemas and paths, fully populated fixed-point values, one fail-closed evaluation order, and pure-compute integration through the canonical Engine Core. No example identity, default, weight, cap, floor, correction, or stage is executable authority.  
  * **Current matrix unaffected.** Future-Promotion does not defer or narrow the Required-Now intrinsic ten-category matrix in §5.2 or its band mapping in §5.3. Viewer preferences remain sampler/ranker inputs.  
  * **Public rule.** A future preset must not silently widen Reader v1; the public projection remains numeric-free and harmony-only unless a separately authorized version change says otherwise.


* **Reader transport — proof surfaces & ops (titles-only routing)**  
    
  * **Endpoint Catalog (JSON success) — \[Required-Now\].** A7 success-endpoint evidence is an externally owned proof family. Its records, paths, Index/Mirror bindings, and production procedure are governed outside PF01; this section preserves only the titles-only routing boundary.  
  * **Dev harness — \[Required-Now\].** A dev/test capture surface exists, but the pinned code defaults a missing `APP_ENV` to `dev`; strict refusal outside explicit `APP_ENV=dev` remains an implementation gap. Transport details belong in **HDE-CLI-API-Vendor-Ref**.  
  * **/internal/version (ops endpoint) — \[Required-Now\].** Ops-only identity surface; acceptance in **HDE-Governance §10.5**.  
  * **Production public Reader endpoint — \[Speculative\].** Future public surface; conditional delivery/headers owned in **HDE-CLI-API-Vendor Ref**/**HDE-Governance**.


* **Serializer/emitter — single shared entrypoint — \[Required-Now\]**  
    
  * **One emitter for public bytes.** Reader and any CLI Reader-byte sidecar MUST call the same presenter/emitter; **no ad-hoc serializers**. Canonical JSON: UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets (dedupe \+ ASCII sort).  
  * **Determinism & parity.** A shared emitter is required for Reader-byte parity, AB↔BA identity, and two-run identity. In the pinned repository, `showcompat` stdout emits a distinct compat payload while `--dump-reader` writes the Reader envelope; stdout equality is not statically established.  
  * **Evidence.** Grep-guard, shared-emitter symbol proof, and Reader-sidecar parity fixtures are Evidence Catalog families owned by **PF12-Canon-HDE-Schemas-and-Artifacts**.


* **Vendor ingest (HDAPI) — \[Owned in HDE-CLI-API-Vendor Ref\]**  
    
  * **Request shaping — current static surface.** The pinned client contains a three-field `birthdate`/`birthtime`/`location` request builder for its supported route family and typed refusal for unsupported route posture. The owning transport canon controls the external contract.  
  * **Base-URL resolution — current static surface.** The pinned client accepts canonical `HD_API_BASE_URL` and the legacy `HDAPI_BASE_URL`, rejects conflicting values, and fails closed when required vendor configuration is absent.  
  * **Live HTTP gate — current static surface.** The default request function refuses network I/O unless `SAFE_MODE=0` and `ALLOW_NETWORK=1`. This static definition does not establish deployment or successful external calls.  
  * **Timeout and retry posture.** Pinned timeout, retry, and backoff profiles exist in code. Runtime enablement, rate-limit behavior, observability, and production authorization are not established by static bytes.


* **Retired contract: prompt and uncertainty — prohibited**  
    
  * **Scope.** Public Reader v1 is required to be narrative-free; `prompt` and `uncertainty` are prohibited by §§2.1–2.2 and Appendix D. Repository conformance must be established separately.  
  * **Acceptance requirement.** Success bodies MUST pass the governing schema without `prompt`; error bodies remain typed and LF-terminated; Reader-sidecar parity goldens remain bands-only. The pinned schema and emitter do not yet conform.

**Routing (no duplication).** Transport/CLI specifics are referenced by title in **HDE-CLI-API-Vendor Ref**; operational acceptance (A7, internal-ops exception, evidence policy) is in **HDE-Governance**. Canonical JSON & manifest/mirror rules live in **PF12-Canon-HDE-Schemas-and-Artifacts**.

---

# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]

## **2.1 Success payload (six keys; numeric-free) \[Required-Now\]**

**Normative rule.** The Reader v1 public success body is a numeric-free JSON object containing exactly six top-level keys. No additional public fields are allowed. All serialization uses canonical JSON (**PF12-Canon-HDE-Schemas-and-Artifacts** §4: UTF-8 without BOM, sorted keys, compact, exactly one trailing `\n`; arrays treated as sets are deduplicated and ASCII-sorted).

**Static implementation posture.** The pinned emitter constructs the six-key envelope and canonical preimage. The checked-in schema does not conform: its category enum omits `harmony`, it still permits `prompt`, and its success branch does not enforce the exact six-key field closure. This is an implementation gap; the normative covenant remains unchanged.

**Required keys (success) — exactly these six**

* **reader\_version :** `"v1"` — fixed string.  
* **eligible :** `<boolean>` — whether the pair is eligible for public evaluation.  
* **categories :** `[ { "id", "band" } … ]` — array of public category items (policy in §2.2).  
* **meta :** `{ "engine_tag", "invocation_tag" }` — engine build tag and invocation tag (both non-empty strings; invocation tag is the short form from **Invocation**; ownership and format per **HDE-Governance** / **PF12-Canon-HDE-Schemas-and-Artifacts** Identity, titles-only).  
* **release\_id :** `<hex64>` — lowercase 64-hex identifier of the frozen pack manifest in use (**PF12-Canon-HDE-Schemas-and-Artifacts** §6; see §3.1).  
* **idempotence\_hash :** `<hex64>` — lowercase 64-hex SHA-256 of the canonical five-key preimage (see §3.2).

**Public category policy (v1)**

* Each item in `categories` is exactly `{ "id": <string>, "band": "Cool" | "Open" | "Warm" | "Glow" }`.  
* Not permitted on the public surface: `prompt` (removed), `personal_key`, `shared_key`, or any numeric (e.g., score, percent).  
* Category identifiers are `snake_case` and come from the Magic-10 IDs set (**PF12-Canon-HDE-Schemas-and-Artifacts** §2.6). In v1, only the `"harmony"` public item may appear (see §2.2).

**Validation posture (success case)**

* **Shape:** object has exactly the six keys above; no extras.  
* **Patterns:** `release_id` and `idempotence_hash` match `^[0-9a-f]{64}$`.  
* **Categories:** must be numeric-free and obey §2.2 (band enum only; item shape exactly `{id,band}`).  
* **Transport/CLI behavior:** headers, conditional GET/HEAD, error envelopes, streams/exit codes are owned in **HDE-CLI-API-Vendor-Ref** / **HDE-Governance** and are referenced here by title only.

**Acceptance gates (titles-only)**

* `PREIMAGE_RECOMPUTE_OK`, `CLI_READER_EMITTER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`  
* `RELEASE_ID_FROM_MANIFEST_OK`, `MANIFEST_SHA256_HEX64_OK`  
* `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK` *(public band mapping proven elsewhere)*

*Tokens: see **HDE-Governance §2.0**.*

---

## **2.2 Category policy (v1) \[Required-Now\]**

### **v1 Alpha scope (public)**

* The public `categories` array in Reader v1 is **bands-only** and **numeric-free**.  
* If `eligible == true`: `categories` **MUST** contain **exactly one** item `{"id":"harmony","band":"Cool"|"Open"|"Warm"|"Glow"}`.  
* If `eligible == false`: `categories` **MUST** be `[]`.  
* No other public categories are allowed in v1. Exposure of the full Magic-10 set is a future, versioned change (PF-01 remains math-only; the public surface is constrained here).

### **Sorting & uniqueness**

* `categories` is treated as a **set**; duplicate `id` values are **forbidden**.  
* Arrays that represent sets are **deduped and ASCII-sorted** (bytewise) before hashing/compare (PF12-Canon-HDE-Schemas-and-Artifacts §4).  
* In v1 (single item), sorting is **vacuously satisfied**; **uniqueness still applies**.

### **Public shape constraints (reaffirmed)**

* Each item is **exactly** `{ "id": <string>, "band": "Cool" | "Open" | "Warm" | "Glow" }`.  
* `id` **must** come from the **Magic-10 closed set** (PF12-Canon-HDE-Schemas-and-Artifacts §2.6; PF-01 §5.1). *(v1 publicly exposes only `"harmony"`.)*  
* **Never permitted** on the public surface: `prompt`, `personal_key`, `shared_key`, `score`, or any numeric/free-text payloads.

### **Determinism coupling**

* `categories` contributes to the **idempotence preimage** (see §3.2; fields defined in PF-01).  
* **AB↔BA identity** and **two-run identity** MUST hold at the byte level after **canonical serialization** (PF12-Canon-HDE-Schemas-and-Artifacts §4; UTF-8 no BOM, sorted keys, compact, exactly one LF).

### **Acceptance gates (binary)**

1. **Exactly-one rule (eligible):** `eligible == true` ⇒ `len(categories) == 1` **and** `categories[0].id == "harmony"`.  
2. **Band enum:** `categories[0].band ∈ {"Cool","Open","Warm","Glow"}`.  
3. **Empty rule (ineligible):** `eligible == false` ⇒ `len(categories) == 0`.  
4. **No extras:** every `categories[*]` has **only** `id` and `band`.  
5. **Uniqueness:** **no duplicate `id` values** (trivial in v1).

**Static implementation posture.** The pinned runtime always constructs one `harmony` category even when the supplied `eligible` value is false. The required `eligible == false` ⇒ `categories: []` behavior is not implemented at the pinned commit.

## **2.3 Errors (shape/pointers) \[Required-Now\]**

### **Typed public error object (no PII; bounded numeric exception)**

* **Shape (minimum):** the public error body is a typed JSON object with:  
  * `ok: false`  
  * `code: "<token>"` — short, machine-readable error token  
  * `error: "<non-PII message>"` — human-readable, non-secret message  
* **Optional field (when applicable):**  
  * `retry_after_ms: <integer >= 0>` — present only when a rate-limit or backoff condition applies  
* **No additional public fields** (no narratives, no keys, no numerics beyond `retry_after_ms`).

### **Hygiene and guardrails**

* **No PII or secrets** in error messages; keep messages succinct and generic.  
* **Determinism:** error bodies are serialized by the same canonical path as success (**PF12-Canon-HDE-Schemas-and-Artifacts** §4): UTF-8, sorted keys, compact separators, exactly one trailing LF.

**Static implementation posture.** The pinned `error_envelope` also emits `schema` and can emit `details`; neither field is permitted by this Reader error contract. Repository conformance remains an implementation gap.

### **Pointers (transport & status live elsewhere)**

* **Transport ownership:** HTTP status mapping, headers, conditional delivery, caching, and streams/exit codes are owned by **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** and are referenced here by title only.

---

## **2.4 Ordering semantics (comparators) \[Required-Now\]**

**Purpose (normative).** Define the mathematical ordering rules that guarantee deterministic, stable outputs. Mechanics and tests live in **HDE-Mechanics Guide** (titles only).

**Comparators (math rules)**

* **IDs / centers / labels:** ASCII lexicographic (bytewise).  
* **Channels:** normalize to zero-padded `NN-NN` (min-first, ASCII hyphen `-`), then compare ASCII lexicographically.  
* **Categories:** primary order by the frozen Magic-10 rank (see **PF12-Canon-HDE-Schemas-and-Artifacts §2.6**), tie-break by `id` (ASCII).  
* **Stable-on-equality:** when primary keys compare equal, apply a canonical secondary key so the order is **total and stable** across runs.

**Set semantics (arrays-as-sets).** Any array that represents a set **MUST** be deduplicated and ASCII-sorted before hashing/compare (see **PF12-Canon-HDE-Schemas-and-Artifacts §4**). Non-canonical or duplicate elements **fail validation**.

**Channel rejection posture.** At the PF01 computation boundary, channel identifiers MUST already be canonical zero-padded `NN-NN` with the lower Gate first; reversed, duplicate, unknown, or unparsable stored values fail validation. An upstream ingestion surface may map a reversed alias such as `34-20` to `20-34` only when its owning contract explicitly authorizes that alias before the value reaches this boundary. Invalid tokens are not coerced here.

**Environment pins (determinism).** All comparisons and byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Routing (titles only).**

* Runnable helpers & tests (`dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`): **HDE-Mechanics Guide**.  
* Magic-10 rank (closed set & order): **PF12-Canon-HDE-Schemas-and-Artifacts §2.6**.

**Acceptance (tokens; titles only).** `TIEBREAK_TOTAL_ORDER_OK` *(supports `CATEGORY_FRAMEWORK_OK`)* — token names live in **HDE-Governance §2.0**.

**Evidence (records-only).** Property tests (antisymmetry / transitivity / totality), a channel-normalization corpus (canonical `NN-NN` plus rejected noncanonical values), and canonical before/after examples for set-normalized arrays are governed evidence families in **PF12-Canon-HDE-Schemas-and-Artifacts**. PF01 does not maintain a parallel path list.

**EPIC017 D4 proof (informative).**  
EPIC017’s “deterministic tie-break and total-order module” deliverable, as recorded in **HDE Phased Epics Map**, is associated with comparator code and evidence intended to cover IDs, channels, categories, arrays-as-sets, antisymmetry, transitivity, totality, AB↔BA identity, and two-run identity. Static repository inspection confirms comparator definitions but does not establish execution or PASS. EPIC017 does **not** alter the ordering rules or arrays-as-sets behavior in this spec. Any future change to comparator policy or set semantics remains a PF01 math change and must follow the usual release-id and evidence requirements.

---

# 3\. Identity & Determinism \[Required-Now\]

## **3.1 release\_id — freeze-pack identity (sha256) \[Required-Now\]**

**Definition (normative).** `release_id` is the lowercase 64-hex SHA-256 of the canonical bytes of `catalog/manifest.json`, the single release-identity input stored in Git. It is stable until those canonical manifest bytes change; neither a Git commit nor a change to a manifest-listed source file changes the value unless the manifest is intentionally cut and its canonical bytes change.

**What the freeze pack includes (by title).** The complete manifest membership and artifact paths are governed by **PF12-Canon-HDE-Schemas-and-Artifacts**. PF01 requires the following math inputs to participate in that governed release identity when represented as artifacts:

* **Topology catalogs:** `catalog/gates_v1.json` and `catalog/channels_v1.json` (canonical `NN-NN` channel identities; centers derive from Gate rows and use canonical machine IDs).  
* **Magic-10 catalog:** `catalog/magic10.json`, the closed, ordered ID set; input bounds live in `catalog/magic10_caps.json`, and global score/band thresholds live in `math/thresholds.json`.  
* **Feature-constants contract:** `limits.em_max`, `limits.throat_em_max`, `limits.centers_max`, `limits.motor_throat_max`, `limits.mind_throat_max`, and `limits.comp_max`; the current global score clamp, rounding mode, and band maxima are governed at `math/thresholds.json`.  
* **Direct Motor→Throat set (if catalogized):** governed four-channel set in canonical `NN-NN`; treated as a frozen input when listed in the manifest.  
* **Seeds catalog (when present):** if catalogized in **PF12-Canon-HDE-Schemas-and-Artifacts**, Seeds are admin/test inputs; any governed byte change requires a manifest cut and new `release_id`.  
  Transport and operational semantics are out of PF01 scope. Their bytes may nevertheless be manifest members when **PF12-Canon-HDE-Schemas-and-Artifacts** governs them as release inputs; PF01 does not redefine the complete manifest as math-only.

### **Construction (canonical)**

1. **Manifest.** Store the single release-identity input at `catalog/manifest.json`. Its top-level keys are exactly `root`, `version`, `built_at_utc`, and `files`, with shape:  
2. `{"root":"catalog/","version":"<semver>","built_at_utc":"YYYY-MM-DDThh:mm:ssZ","files":[{"path":"…","sha256":"<64hex>","size":<int>},…]}`. The manifest **MUST NOT** self-list. `files[].path` is repository-relative; `root` is identity metadata and is not a path-resolution base. `built_at_utc` MUST come from one deterministic, governed build input and MUST NOT be sampled during serialization.  
3. **Canonicalize.** Store the manifest using **PF12-Canon-HDE-Schemas-and-Artifacts** canonical JSON rules: UTF-8 (no BOM), ASCII-sorted object keys, compact separators, and exactly one trailing `\n`; arrays-as-sets are deduplicated and ASCII-sorted.  
4. **Hash.** `release_id = sha256(canonical_bytes("catalog/manifest.json"))` → 64-hex, lowercase. CI also requires the on-disk manifest to be canonical; non-canonical storage is a hard-fail even if the canonical hash would be unchanged.

**Casing & format**

* Exactly 64 lowercase hex: `^[0-9a-f]{64}$`.  
* No prefixes/suffixes; no whitespace.

**Change conditions**

* **MUST** cut a new canonical manifest and therefore a new `release_id` whenever the canonical bytes of a governed file change (topology catalogs, constants pack, Magic-10 catalog, direct Motor→Throat set if catalogized), or whenever the manifest’s canonical content or schema changes. A governed-file change alone does not alter `release_id`; the value changes only when the canonical manifest bytes change.  
* Pure formatting changes to the on-disk manifest do not change `release_id` after canonicalization, but still fail CI if the stored file is non-canonical.

**Scope & coupling**

* `release_id` is included in the Reader v1 success body and participates in acceptance checks (see §2, §3.4; Governance A-gates by title).  
* **Pins.** All recomputation runs with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Only the selected pack and its canonical manifest affect the value.  
* **Acyclic release graph.** The required dependency direction is `tracked source -> canonical manifest -> release_id -> external attestation`. No generated attestation may feed back into tracked source or become an input to `release_id`.

**Validation (binary)**

* **Pattern:** value matches `^[0-9a-f]{64}$`.  
* **Provenance:** evidence (titles/paths only) includes the canonical manifest artifact and the computed `release_id`.  
* **Determinism:** recomputing over the same pack yields the same `release_id` (two-run identity).

**Static implementation posture.** The pinned runtime validates and hashes the canonical packaged manifest. The pinned manifest has eight entries, omits required topology and complete Magic-10 narrative inputs named by the current PF12 minimum, and therefore does not establish manifest conformance or a PASS. Its inclusion of adapter and migration bytes is consistent with PF12 ownership of the complete release surface and disproves only the former PF01 math-only membership claim.

**Acceptance gates (titles-only)**  
`RELEASE_ID_FROM_MANIFEST_OK`, `RELEASE_ID_RECOMPUTE_OK`, `MANIFEST_SHA256_HEX64_OK`, `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`.

**Non-goals (routed by title only).** HTTP headers, conditional delivery, caching/writers, and CLI/Reader validators live in **HDE-CLI-API-Vendor Ref** and **HDE-Governance**.

## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**

**Definition (normative).** `idempotence_hash` is the lowercase 64-hex SHA-256 of the canonical preimage of the Reader v1 success envelope. It proves that the published bytes arise from a single, canonical representation.

### **Canonical preimage (success case)**

Build an object with exactly five keys (no others), each already normalized per this spec and **PF12-Canon-HDE-Schemas-and-Artifacts**:

1. `reader_version` : `"v1"`  
2. `eligible` : `<boolean>`  
3. `categories` : `[{"id","band"}]` — public policy per §2.2 (v1 exposes one item `{"id":"harmony","band":<Cool|Open|Warm|Glow>}` when `eligible == true`; `[]` when `eligible == false`; numeric-free)  
4. `meta` : `{"engine_tag","invocation_tag"}` — titles-only references to **PF12-Canon-HDE-Schemas-and-Artifacts** (invocation tag is the short form; no other fields in public `meta`)  
5. `release_id` : `<hex64>` — as defined in §3.1

Do not include `idempotence_hash` in the preimage.

**Separation from intrinsic Magic10 identity.** `idempotence_hash` is computed independently from `pair_key`. `pair_key` is neither a public field nor a member of the five-key Reader preimage, and no equality contract exists between the two digests. A valid self-pair produces no intrinsic `pair_key`. An eligible distinct-person equal-mask pair produces an intrinsic `pair_key`, but under the same `meta` and `release_id` its Reader preimage cannot equal the self-pair preimage because `eligible` and `categories` differ.

### **Canonical serialization (preimage & final)**

Use **PF12-Canon-HDE-Schemas-and-Artifacts** rules: UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays that represent sets are deduplicated and ASCII-sorted. All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **Emission algorithm (success)**

1. **Preimage.** Serialize the five-key object → `preimage_bytes` (LF-terminated, canonical).  
2. **Hash.** `digest = sha256(preimage_bytes)` (lowercase 64-hex).  
3. **Final.** Add `idempotence_hash : <digest>` and re-serialize canonically → public bytes.

### **Correctness properties**

* **Deterministic & stable.** Any preimage byte change (field value, order, band, `release_id`) changes `idempotence_hash`. Canonicalization removes non-semantic whitespace/key-order differences.  
* **AB↔BA identity.** Pair inputs are normalized (this spec’s composite rules; **PF12-Canon-HDE-Schemas-and-Artifacts** topology normalization), so AB and BA produce identical `preimage_bytes` and the same `idempotence_hash`.  
* **Two-run identity.** Re-emitting the same logical object yields byte-identical preimage and final bodies.  
* **Reader↔CLI parity.** For identical inputs and environment, a CLI Reader-byte sidecar and Reader MUST emit byte-identical success bodies and the same `idempotence_hash`. The general `showcompat` stdout payload is a different admin/compat surface and is not Reader bytes.

### **Validation (binary)**

* **Pattern.** Value matches `^[0-9a-f]{64}$`.  
* **Recompute check.** Remove `idempotence_hash` from the published body, re-serialize canonically, hash, and confirm equality with the published digest.

**Acceptance (tokens, titles-only).** `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`.  
**Non-goals / routing.** `idempotence_hash` is not an HTTP transport token; ETag/conditional semantics live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** (titles only).  
**Tokens:** see **HDE-Governance §2.0**.

**Static implementation posture.** The pinned presenter implements the five-key preimage, canonical hash, and final emission sequence. Complete public conformance remains blocked in code by the ineligible-category and `prompt` gaps identified in §§2.1–2.2; static inspection does not establish the acceptance tokens above.

---

## **3.3 invocation\_tag — deterministic, order-neutral \[Required-Now\]**

**Definition (normative).** `invocation_tag` is a **non-empty string** carried in `meta` that identifies the **logical invocation context** under which a public result is produced. It is part of the **success preimage** (see §3.2) and therefore participates in the `idempotence_hash`.

**Determinism & neutrality**

* **Order-neutral.** For the same pair and invocation context, **AB and BA MUST use the same `invocation_tag`**.  
* **Run-stable.** Retries of the same logical invocation **MUST** reuse the same `invocation_tag`; changing it will (by design) change the `idempotence_hash`.  
* **Two-run identity.** When all inputs (including `invocation_tag`) are identical, two serializations produce **byte-identical** outputs.

**Ownership & construction (routing)**

* The caller (CLI or Adapter) is responsible for **providing** `invocation_tag` consistently for a given invocation context.  
* Exact generation rules (e.g., environment resolution, defaults, substitution) **are not duplicated here**; they live in the transport/CLI reference and are referenced by title only.  
* This spec requires only that the caller’s recipe be **deterministic** and **order-neutral** with respect to pair normalization.

**Constraints**

* **String; non-empty.** Must be printable; **no PII/secrets**.  
* **Effect on identity.** Because `invocation_tag` is in the canonical preimage, changing it **changes `idempotence_hash`** (by design).

**Validation (binary)**

* **Presence:** `meta.invocation_tag` is present and non-empty.  
* **AB↔BA:** The same `invocation_tag` appears for AB and BA under the **same** invocation context.  
* **Recompute:** With `invocation_tag` held constant, preimage hash recomputation matches the published `idempotence_hash`.

**Non-goals / routing.** HTTP header behavior, conditional delivery, and CLI defaults for `invocation_tag` are owned by **PF-Canon-HDE-CLI-API-Vendor-Ref** and are not restated here.

---

## **3.4 Two-run identity & AB↔BA parity (public) \[Required-Now\]**

### **Definition (normative)**

* **Two-run identity.** Serializing the same logical success envelope twice (same inputs, same environment, same `invocation_tag`, same `release_id`) **MUST** produce byte-identical public bytes.  
* **AB↔BA parity.** For a given pair of **normalized** inputs, swapping input order (AB vs BA) **MUST** produce byte-identical public bytes.

### **How it is achieved (concept)**

* **Canonical preimage → hash → final** (see §3.2). Identical preimages yield identical `idempotence_hash` and final bytes.  
* **Pair normalization.** Inputs are normalized **before** any computation (see topology normalization in PF12-Canon-HDE-Schemas-and-Artifacts), guaranteeing order-neutrality for scores, bands, and envelope.  
* **Single emitter.** One canonical JSON emitter shared across Reader and CLI (UTF-8, sorted keys, compact, exactly one LF) eliminates serializer drift across surfaces.  
* **Environment pins.** All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **Evidence families (titles-only)**

* **Reader/CLI Reader-sidecar parity and LF discipline.**  
* **AB↔BA public-success goldens.**  
* **Two-run identity and idempotence recompute.**  
* **Canonical emitter identity.**  
* **Ownership.** Exact artifact families, paths, Index/Mirror records, and path proofs are governed by the Evidence Catalog in **PF12-Canon-HDE-Schemas-and-Artifacts**; PF01 does not maintain a parallel path list.

### **Byte-level acceptance (binary)**

* **Two-run identity.** For a fixed input set and environment, two serializations of the success envelope are exactly identical, including the single trailing LF; confirm by byte-compare and by recomputing `sha256(preimage_bytes)` to reproduce the published `idempotence_hash`.  
* **AB↔BA parity.** Given inputs A,B and B,A, the emitted bytes are bit-for-bit identical; confirm by byte-compare and equal `idempotence_hash`.  
* **Serializer invariants.** Outputs are UTF-8, sorted keys, compact separators, exactly one LF, no BOM/ANSI, and schema-valid in both success and error modes.

**Static implementation posture.** The pinned canonical serializer and Reader presenter are deterministic by inspection, and the CLI can write Reader bytes through `--dump-reader`. General `showcompat` stdout emits a different compat object; the checked-in Reader schema and ineligible behavior are nonconforming; and static files do not prove any test or acceptance PASS.

**Non-goals / routing.** Header matrices, conditional delivery, caching/writers policy, and CLI stream rules are not duplicated here; see **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles only).

---

# **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**

## 4.1 Definition (normative)

* **Eligibility** is a pure, mechanical pair-computability predicate indicating whether a validated normalized pair can be evaluated for public output.  
* Eligibility is not a sampler, ranking, viewer-preference, preset, moderation, consent, blocking, product-access, score, band, or relationship-state predicate.  
* Each evaluation-party record contains an exact lowercase, hyphenated RFC 4122 UUID as `canonical_person_id`, a complete normalized chart projection, an ascending unique Gate tuple, an unsigned 64-bit `gate_mask`, a sixteen-character lowercase `gate_mask_hex`, and the `chart_fingerprint` defined in §5.2.  
* Validate and resolve both complete party projections before classifying the pair.  
* Return `false` exactly when both records have the same `canonical_person_id` and byte-identical complete normalized projections. This valid self-pair is ineligible, not erroneous.  
* The same `canonical_person_id` with unequal complete normalized projections fails closed as `ERR_READER_INVALID_CHART`; it is not coerced to an ineligible success.  
* Return `true` exactly when the two validated records have distinct `canonical_person_id` values, including when their Gate masks are equal.  
* A valid distinct pair remains eligible when it has no electromagnetic Channel, a low compatibility band, or any Type combination.  
* Decide eligibility before Engine Core, intrinsic cache access, or `pair_key` construction. A valid self-pair produces no intrinsic signals, matrix, cache lookup or write, narrative route, or `pair_key`.  
* The result is a **boolean** (`eligible: true|false`) and carries no numerics or narrative content.

## 4.2 Inputs and catalogs (concept)

* **Raw Gate ingress.** The Gate normalizer accepts only a nonempty JSON array whose members are integers in `1..64` or canonical decimal strings from `"1"` through `"64"`. It rejects booleans, whitespace, leading zeroes, signs, decimals, missing or empty arrays, duplicates, malformed strings, and values outside `1..64`.  
* **Normalized Gate contract.** Normalization returns an ascending unique integer tuple, its unsigned 64-bit Gate mask with Gate `g` at bit `g-1`, a sixteen-character lowercase hexadecimal mask, and the §5.2 chart fingerprint.  
* **Gate closure.** Every normalized Gate MUST resolve exactly once in `catalog/gates_v1.json`.  
* **Channel coherence.** `catalog/channels_v1.json` MUST be closed and internally coherent for the active topology; every Channel endpoint used by downstream pair mechanics MUST resolve to the Gate Catalog.  
* **Release identity.** The active lowercase 64-hex `release_id` identifies the frozen inputs used for the evaluation. All lookups are deterministic and use that active frozen surface.  
* **Excluded inputs.** No score, band, viewer preference, preset, sampler setting, clock, environment variable, network result, moderation state, application relationship state, `prompt`, or `uncertainty` value is consulted.

## 4.3 Determinism & neutrality

* **Independent validation first.** Validate each normalized chart independently before self-pair classification, intrinsic ordering, or directional orientation.  
* **Eligibility first.** Apply the same-identity decision before Engine Core or intrinsic cache access.  
* **Canonical sets.** Canonicalize each `gates` array as ascending unique integers and derive its Gate mask deterministically.  
* **Intrinsic scoring order.** For an eligible pair, order the two Gate masks numerically as `member_lo` and `member_hi`. Equal masks remain two equal adjacent scoring members; identity does not affect Channel states, signals, scores, bands, chart fingerprints, or `pair_key`.  
* **Directional orientation order.** After eligibility succeeds, order evaluation parties by the total tuple `(gate_mask, canonical_person_id)`, using numeric Gate-mask order and then ASCII UUID order only when masks are equal. This orientation controls directional narrative keys only and never enters intrinsic mathematics or the intrinsic cache key.  
* **AB↔BA neutrality.** Reversing request order produces the same eligibility, intrinsic ordering, directional orientation, score result, and public projection.  
* **Two-run identity.** With the same complete inputs and freeze pack, recomputing eligibility yields the same boolean.  
* No time, network, random, environment, scoring, preference, or sampler source influences eligibility.

## 4.4 Public behavior

* **If `eligible == true`:** the public `categories` array **MUST** comply with §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
    
* **If `eligible == false`:** the public `categories` array **MUST** be `[]`. No numerics or narrative fields appear in either case.  
    
* Invalid or missing input does not produce a success envelope and MUST NOT be coerced to `eligible:false`.

## 4.5 Validation (binary)

* **Missing input.** An absent party, absent `person_uid`, absent `gates`, or absent active release identity fails closed as `ERR_READER_MISSING_PARAM`, with no Reader success envelope.  
    
* **Invalid input.** A malformed `person_uid`; malformed, duplicate, out-of-domain, or unresolved Gate; incoherent topology; or same-UID/different-projection conflict fails closed as `ERR_READER_INVALID_CHART`, with no Reader success envelope.  
    
* **Catalog closure:** every reference used by the gate resolves within the active frozen inputs.  
    
* **Determinism checks:** AB↔BA parity and two-run identity are satisfied for the eligibility boolean.  
    
* **Schema coupling:** the success envelope reflects eligibility as per §2.1; the value participates in the **preimage** for `idempotence_hash` (see §3.2).  
    
* **Minimum true fixture.** Two valid normalized charts with distinct valid UIDs, closed Gate membership, and the same active `release_id` produce `eligible:true`, including when no Channel is completed across the pair.  
    
* **Minimum false fixture.** The same valid normalized chart supplied twice with the same UID and byte-identical canonical projection produces `eligible:false` and `categories:[]`.  
    
* **Minimum invalid fixture.** A Gate `65`, duplicate Gate, or Gate absent from the active catalog produces `ERR_READER_INVALID_CHART` and no success envelope.

## 4.6 Non-goals / routing

* No transport policy, caching, HTTP status mapping, sampler eligibility, ranking, preference weighting, moderation, consent, blocking, or product-access policy is specified here; those concerns route to their owning documents by exact title.  
* `canonical_person_id` is the normalized application-boundary identity consumed by this predicate and by directional orientation only. A public or birth-facing caller need not construct it when an architecture-sanctioned resolver supplies the exact canonical identity and complete normalized projection before PF01 validation.

## 4.7 Emission rule (binary) \[Required-Now\]

* **Eligible ⇒** **emit categories** per §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
    
* **Ineligible ⇒** **`categories: []`** (empty array). No numerics, no narrative fields.

**Static implementation posture.** No Reader eligibility decision function implementing this contract was found in the pinned repository. `engine.runtime.public` accepts a caller-supplied boolean, defaults it to `true`, and emits `harmony` even when false. The sampler has a separate candidate-pool predicate and MUST NOT be reused as Reader pair-computability. This is an explicit implementation gap, not a change to the Required-Now contract.

# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]

## **5.1 Canonical IDs (closed set) \[Required-Now\]**

**Definition (normative).** The **Magic-10 category identifiers are a closed, ordered set** of ASCII-lowercase strings. **PF12-Canon-HDE-Schemas-and-Artifacts** and its governed `catalog/magic10.json` artifact are the single home for the set and order. This specification does not create a second catalog list; consumers MUST dereference the governed order.

**Use and exposure**

* **Canonical internal math:** the canonical Engine Core consumes the complete closed set for the intrinsic scoring and band matrix in §§5.2–5.3. Every eligible pair requires all ten results atomically.  
* **Public surface (v1):** Reader v1 is **bands-only & numeric-free** and projects only `{"id":"harmony","band":…}` from the complete canonical matrix (see **§2.2**). Public exposure of all ten categories remains a future, versioned change.

**Ordering and uniqueness**

* **Order is pinned** in **PF12-Canon-HDE-Schemas-and-Artifacts §2.6** and is the **normative iteration order** for any ordered consumer (comparators in **§2.4**).  
* Identifiers are **unique**; duplicates are **forbidden**.

**Format and validation**

* Identifiers are **ASCII-lowercase**; **validators MUST enforce exact membership** against PF12-Canon-HDE-Schemas-and-Artifacts §2.6. Pattern pre-filters (e.g., `^[a-z]+$`) are insufficient for acceptance; **exact set** membership is required.  
* Intrinsic score and band results MUST cover exactly this closed set, with no extras, omissions, or duplicates. Viewer preferences may use the same closed key set for sampler/ranker weighting, but they do not contribute to intrinsic score magnitude.  
* Catalogs/schemas (PF12-Canon-HDE-Schemas-and-Artifacts §2.6) **reject non-members**; stored JSON follows **PF12-Canon-HDE-Schemas-and-Artifacts §4** (UTF-8 no BOM, sorted keys, compact, **one LF**).

**Change control (freeze-pack coupling)**

* **No membership/order edits in this version.** Any change to **membership or order** is a **frozen-input change**; it **requires a new pack manifest** (PF12-Canon-HDE-Schemas-and-Artifacts §6) and therefore a **new `release_id`** (see **§3.1**).  
* Downstream governed artifacts (e.g., Magic-10 catalog, band maxima, presets) must reference **only these IDs**; changing them also **bumps `release_id`**.

**Determinism guarantees**

* Closed membership \+ fixed order, combined with **canonical serialization** and **preimage hashing** (see **§3.2**), ensures **AB↔BA identity** and **two-run identity**.  
* With identifiers immutable and order pinned, category iteration/aggregation is **byte-stable** across surfaces.

**Static implementation posture.** The pinned `catalog/magic10.json` and `engine.categories.registry` use the governed harmony-first order, while `engine.compat.categories.CATEGORIES_ORDER_V1` is heat-first. The compat order is a nonconforming admin/legacy implementation gap and does not change the governed order.

**Acceptance & CI (titles-only)**

* **MAGIC10\_DOMAIN\_CLOSED\_OK**, **MAGIC10\_NAMES\_FROZEN\_OK** (set & order frozen; change ⇒ new `release_id`)  
* **PREFS\_KEYSET\_10\_OK** (viewer-prefs keys \== this set)  
* **EVIDENCE\_INDEX\_UPDATED\_OK** (on any change to governed catalog)

---

## **5.2 Deterministic integer scoring model (caps; fixed-point rules)**

**Scope.** This section defines the Required-Now intrinsic Magic10 v1 computation from two eligible normalized Gate sets to one complete ordered ten-category score-and-band matrix. The computation classifies all 36 canonical Channels, produces exactly twenty internal signals in half-score units, reduces them into ten scores, and applies the global bands in §5.3. It is deterministic, AB↔BA neutral, identity-independent after eligibility, integer/fixed-point only, and complete-or-fail-closed.

The formula is Glow-authored Product synthesis grounded in Human Design composite Channel states. It does not assert empirical compatibility effect sizes, relationship quality, medical or psychological meaning, safety, destiny, ranking, or outcome prediction. Viewer preferences, caller-selected configurations, identifiers, request metadata, clocks, randomness, external I/O, and hidden mutable state do not affect intrinsic results.

### **5.2.1 Inputs and closure**

* **Eligible normalized pair.** Apply §4 before Engine Core or intrinsic cache access. A valid self-pair is not scored and produces no intrinsic result or `pair_key`.  
* **Gate representation.** Each member supplies an ascending unique nonempty Gate tuple, unsigned 64-bit `gate_mask`, and exactly sixteen lowercase hexadecimal digits as `gate_mask_hex`. Gate `g` occupies bit `g-1`.  
* **Topology closure.** Every Gate resolves exactly once in `catalog/gates_v1.json`; every scoring Channel resolves exactly once in the closed 36-row `catalog/channels_v1.json`; every Channel has two distinct ascending Gate endpoints.  
* **Mechanics configuration.** Use exactly one immutable active `magic10_mechanics_config.v1` bundle per release. The initial complete configuration is `m10-channel-state-v1.0.0`.  
* **Category closure.** `catalog/magic10.json` owns the exact ten-category order. `catalog/magic10_caps.json` owns each category's exact ordered two-signal input pair and integer score bounds.  
* **Threshold closure.** `math/thresholds.json` owns the `0..100` clamp, `ROUND_HALF_UP`, and inclusive maxima `[24,49,74,100]`.  
* **Complete-or-fail-closed.** Missing, extra, duplicate, malformed, out-of-domain, unresolved, stale, or configuration-incoherent input produces no successful intrinsic matrix.

  ### **5.2.2 Chart fingerprint, intrinsic pair identity, and cache identity**

For each normalized member, canonically serialize an object containing exactly:

* `schema = "magic10_chart_fingerprint.v1"`;  
* `gate_mask_hex = "<sixteen lowercase hexadecimal digits>"`.

Use the canonical JSON rules governed by **PF12-Canon-HDE-Schemas-and-Artifacts** and compute:

`chart_fingerprint = sha256(canonical_bytes(chart_fingerprint_preimage))`

For an eligible pair, order the two Gate masks numerically as `member_lo` and `member_hi`. Equal masks remain two equal adjacent members; identity does not break the tie and does not enter intrinsic mathematics.

Construct `magic10_pair_preimage.v1` as canonical JSON with exactly:

| Field | Exact value |
| ----- | ----- |
| `schema` | `magic10_pair_preimage.v1` |
| `members` | The two `chart_fingerprint` values ordered by numeric Gate masks as `member_lo`, `member_hi`; equal masks produce two equal adjacent values |
| `config_id` | Active immutable mechanics configuration ID |
| `release_id` | Active release identity |
| `result_schema` | `magic10_result.v1` |

Compute:

`pair_key = sha256(canonical_bytes(preimage))`

The intrinsic cache key is exactly:

`magic10:v1:<pair_key>`

A cached value is usable only when its embedded `pair_key`, `config_id`, `release_id`, and result-schema value match the current evaluation and release. A mismatch is stale, never a hit. If both valid Gate sets remain available, recompute under the active release; otherwise fail closed with `ERR_M10_STALE_RESULT`.

Names, account IDs, UUIDs, UIDs, request IDs, timestamps, relationship history, directional orientation, narrative keys, and viewer preferences are absent from the intrinsic preimage. `pair_key` is not public, is not a score operand, and has no equality contract with the Reader `idempotence_hash`.

### **5.2.3 Five-state input and response profiles**

Classify every canonical Channel exactly once under the closed five-state rule in §6.1. Only `dominance` and `compromise` carry the normalized full-Channel owner needed by the Balance ownership operation.

Ordinary signal responses use integer basis points in `0..10000`:

| Profile ID | none | companionship | dominance | compromise | electromagnetic | Required ordering |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| `coherence_bp_v1` | 0 | 10000 | 5000 | 2500 | 7500 | companionship \> electromagnetic \> dominance \> compromise \> none |
| `activation_bp_v1` | 0 | 5000 | 7500 | 2500 | 10000 | electromagnetic \> dominance \> companionship \> compromise \> none |
| `expression_bp_v1` | 0 | 7500 | 5000 | 2500 | 10000 | electromagnetic \> companionship \> dominance \> compromise \> none |

The exact stored values `0`, `2500`, `5000`, `7500`, and `10000` represent normalized responses `0.00`, `0.25`, `0.50`, `0.75`, and `1.00`. Human Design doctrine supports distinguishing the five states but does not supply these fractions.

### **5.2.4 Twenty-signal register and formulas**

All ordinary Channel weights default to `1`. The two Balance signals use their named operations rather than a response profile.

| Category | Signal ID | Exact construct | Operation or profile | Default Channel map |
| ----- | ----- | ----- | ----- | ----- |
| harmony | `rapport_delta` | Structural support through needs, values, care, communal bargains, and trusted transmission | `coherence_bp_v1` | `19-49`, `26-44`, `27-50`, `37-40` |
| harmony | `resonance_strength` | Attunement through rhythm, intimacy, mood-sensitive openness, and listening or witnessing | `coherence_bp_v1` | `05-15`, `06-59`, `12-22`, `13-33` |
| heat | `spark_intensity` | Relational charge through intimacy, shock, desire, and provocation or spirit | `activation_bp_v1` | `06-59`, `25-51`, `30-41`, `39-55` |
| heat | `momentum_flux` | Activated movement through mutation, deeds, commitment, and change or experience | `activation_bp_v1` | `03-60`, `20-34`, `29-46`, `35-36` |
| communication | `signal_clarity` | Capacity to formulate, organize, rationalize, or realize mental content | `expression_bp_v1` | `04-63`, `17-62`, `23-43`, `24-61`, `47-64` |
| communication | `exchange_density` | Capacity to exchange stories, emotional expression, witnessing, intuitive awareness, and transmission | `expression_bp_v1` | `11-56`, `12-22`, `13-33`, `20-57`, `26-44` |
| alignment | `vector_cohesion` | Coherence of direction, leadership, authentic presence, and action from conviction | `coherence_bp_v1` | `02-14`, `07-31`, `10-20`, `10-34` |
| alignment | `axis_agreement` | Coherence of principles, values, purpose, and continuity or ambition | `coherence_bp_v1` | `19-49`, `27-50`, `28-38`, `32-54` |
| comfort | `soothe_index` | Accessible intimacy, emotional openness, recognition of needs, and communal support | `coherence_bp_v1` | `06-59`, `12-22`, `19-49`, `37-40` |
| comfort | `buffer_resilience` | Embodied support through rhythm, survival awareness, preservation, and instinctive power | `coherence_bp_v1` | `05-15`, `10-57`, `27-50`, `34-57` |
| consistency | `pattern_integrity` | Repeatable rhythm, concentration, skill development, detail, and correction | `coherence_bp_v1` | `05-15`, `09-52`, `16-48`, `17-62`, `18-58` |
| consistency | `variance_stability` | Continuity through pulse, commitment, adaptation, and complete cycles | `coherence_bp_v1` | `03-60`, `29-46`, `32-54`, `42-53` |
| expansion | `growth_tendency` | Activation of mutation, improvement, transformation, and maturation | `activation_bp_v1` | `03-60`, `18-58`, `32-54`, `42-53` |
| expansion | `horizon_reach` | Activation through curiosity, meaningful risk, discovery, and new experience | `activation_bp_v1` | `11-56`, `28-38`, `29-46`, `35-36` |
| creativity | `novelty_factor` | Activation of contribution, mutation, unique insight, and initiation | `activation_bp_v1` | `01-08`, `03-60`, `23-43`, `25-51` |
| creativity | `expression_flow` | Expression through authentic presence, storytelling, emotion, talent, and experience | `expression_bp_v1` | `10-20`, `11-56`, `12-22`, `16-48`, `35-36` |
| drive | `willpower_current` | Activation of resources, material will, initiative, enterprise, and ambition | `activation_bp_v1` | `02-14`, `21-45`, `25-51`, `26-44`, `32-54` |
| drive | `focus_pressure` | Activation of concentration, improvement pressure, deeds, struggle, and cycle completion | `activation_bp_v1` | `09-52`, `18-58`, `20-34`, `28-38`, `42-53` |
| balance | `equilibrium_score` | Bilateral distribution of selected one-owner Channel mass | `twice_min_owner_mass_v1` | `02-14`, `07-31`, `21-45`, `26-44`, `32-54`, `37-40` |
| balance | `counterweight_ratio` | Share of selected Channel mass expressed through companionship or electromagnetic completion | `companionship_em_mass_v1` | `05-15`, `06-59`, `10-20`, `13-33`, `27-50`, `39-55` |

The default configuration contains exactly twenty signals, ten category pairs, and 90 Channel-to-signal rows. Every canonical Channel has at least one assigned Product use. No default map assigns one Channel to both signals of the same category.

#### **Ordinary signals: `weighted_state_sum_v1`**

For ordinary signal `s`:

* `C_s` is its configured Channel set;  
* `w(c,s)` is the configured positive integer Channel weight, default `1`;  
* `p_s` is its configured response profile;  
* `r(p_s,t_c)` is the integer basis-point response for Channel state `t_c`;  
* `W_s = sum(w(c,s))`;  
* `N_s = sum(w(c,s) * r(p_s,t_c))`.

The normalized signal is:

`x_s = N_s / (10000 * W_s)`

Represent the signal as an integer `q_s` in half-score units from `0..200`, where `1` means `0.5` score points:

`q_s = floor((N_s + 25 * W_s) / (50 * W_s))`

This is exactly `round_half_up(200 * x_s)`. Round once after the complete weighted signal sum. All `none` returns `0`; maximum response on every mapped Channel returns `200`.

#### **Balance signal: `equilibrium_score` through `twice_min_owner_mass_v1`**

Only `dominance` and `compromise` contribute. For each configured Channel, the full-Channel owner supplies `member_lo` or `member_hi`.

Define:

* `m_lo = sum(w_c)` for mapped dominance or compromise Channels owned by `member_lo`;  
* `m_hi = sum(w_c)` for mapped dominance or compromise Channels owned by `member_hi`;  
* `m = min(m_lo, m_hi)`;  
* `W = sum(w_c)` across all mapped Channels.

Then:

`x_equilibrium = 2 * m / W`

`q_equilibrium = floor((800 * m + W) / (2 * W))`

One-sided owner mass returns `0`. A perfectly split six-row default map returns `200`. Companionship, electromagnetic, and none do not contribute. This signal describes structural bilateral distribution, not fairness, reciprocity, equality, care, or relationship quality.

#### **Balance signal: `counterweight_ratio` through `companionship_em_mass_v1`**

Define:

* `M = sum(w_c)` for mapped Channels in `companionship` or `electromagnetic`;  
* `W = sum(w_c)` across all mapped Channels.

Then:

`x_counterweight = M / W`

`q_counterweight = floor((400 * M + W) / (2 * W))`

Dominance, compromise, and none contribute zero. This is a normalized selected-state ratio, not a relationship verdict.

### **5.2.5 Ten-category reduction, caps, rounding, and bands**

The canonical category order and exact caps-owned input pairs are:

| Order | Category | Signal 1 | Signal 2 | Default input weights |
| ----- | ----- | ----- | ----- | ----- |
| 1 | harmony | `rapport_delta` | `resonance_strength` | `1,1` |
| 2 | heat | `spark_intensity` | `momentum_flux` | `1,1` |
| 3 | communication | `signal_clarity` | `exchange_density` | `1,1` |
| 4 | alignment | `vector_cohesion` | `axis_agreement` | `1,1` |
| 5 | comfort | `soothe_index` | `buffer_resilience` | `1,1` |
| 6 | consistency | `pattern_integrity` | `variance_stability` | `1,1` |
| 7 | expansion | `growth_tendency` | `horizon_reach` | `1,1` |
| 8 | creativity | `novelty_factor` | `expression_flow` | `1,1` |
| 9 | drive | `willpower_current` | `focus_pressure` | `1,1` |
| 10 | balance | `equilibrium_score` | `counterweight_ratio` | `1,1` |

For category `k`, let `L_k` and `U_k` be its integer score-point bounds from `catalog/magic10_caps.json`. Cap each half-score-unit input before reduction:

`q_prime_i = min(2 * U_k, max(2 * L_k, q_i))`

The current bounds are `L_k = 0` and `U_k = 100`, so valid `q_i` values are unchanged.

Each category has exactly two capped inputs. Let:

* `b_i` be each positive integer category-input weight, default `1`;  
* `B_k = sum(b_i)`;  
* `Q_k = sum(b_i * q_prime_i)`.

Calculate:

`raw_score_k = floor((Q_k + B_k) / (2 * B_k))`

With two equal inputs:

`raw_score_k = floor((q_1 + q_2 + 2) / 4)`

Apply the defensive clamp exactly once:

`score_k = min(100, max(0, raw_score_k))`

This is one half-up round after the weighted signal mean, followed by the existing defensive clamp. Apply the global inclusive band maxima in §5.3 after the clamp. Do not use binary-floating-point intermediates.

No intrinsic preset, viewer preference, bonus, dampener, extra floor or cap, correction factor, UID value, category-specific hidden multiplier, or caller-selected configuration is applied.

### **5.2.6 Determinism and neutrality**

* **AB↔BA parity.** Reversing request order produces the same numeric Gate-mask order, five-state Channel vector, signal vector, category scores, bands, chart fingerprints, and `pair_key`.  
* **Identity independence.** Changing distinct eligible party identities without changing normalized Gate masks cannot change intrinsic content or `pair_key`.  
* **Equal-mask behavior.** Distinct eligible parties with equal masks retain two equal intrinsic members and compute the complete result. The transient UUID tie-break affects directional narrative orientation only.  
* **Two-run identity.** The same eligible Gate masks, active configuration, release identity, and frozen inputs produce the same complete ordered result.  
* **One evaluation.** Every Channel is classified once, every signal is produced once, and every category is reduced once in its canonical order.  
* **No hidden sources.** Intrinsic math performs no network or vendor call and consumes no wall clock, randomness, environment state, locale-dependent ordering, mutable remote configuration, identifiers as score seeds, viewer preference, or relationship history.

  ### **5.2.7 Validation and failure behavior**

* Validate complete closure among the 36-Channel catalog, three profiles, twenty ordered signal rows, ten caps-owned pairs, ten category-weight rows, thresholds, configuration source hashes, result schema, and active release identity.  
* Require exactly twenty unique signal IDs in flattened caps-input order and exactly ten unique category results in `catalog/magic10.json` order.  
* Require every ordinary signal to use one valid named profile and one through six unique canonical Channels. Require each Balance signal to use its exact named operation and one through six unique canonical Channels.  
* Require each ordinary Channel weight and category-input weight to be an integer in `1..3`; reject booleans, zero, negative, fractional, missing, or extra values.  
* Require every response to be an integer in `0..10000` and preserve each profile's required ordering.  
* Require every signal wire value to be an integer in `0..200`, every score to be an integer in `0..100`, and every band to derive only from §5.3.  
* Validate the exact deterministic fixtures in §9, including all-none, homogeneous companionship, Balance ownership, sparse Gate sets, identity independence, category boundaries, a valid self-pair, and distinct people with equal Gate masks.  
* AB and BA MUST yield identical intrinsic vectors and `pair_key`; two identical runs MUST yield identical intrinsic results.  
* If any required input, catalog row, mapping, profile, operation, source hash, configuration value, score, band, or cache identity is unavailable or invalid, emit no successful intrinsic matrix. Static definitions and checked-in tests do not establish a PASS.

  ### **5.2.8 Configuration, tuning, and change control**

The default active configuration is complete and shippable; tuning is not an implementation prerequisite.

| Knob | Default | Allowed configuration range | Change class |
| ----- | ----- | ----- | ----- |
| Ordinary Channel weight | `1` | integer `1..3` | Numeric tuning |
| State response | values in the three default tables | integer `0..10000` while profile ordering remains valid | Numeric tuning |
| Category-input weight | `1` | integer `1..3` | Numeric tuning |
| Channel membership in a signal | exact default map | valid unique canonical Channels, one through six per ordinary signal | Structural mechanics revision |
| Signal profile assignment | exact default assignment | one of the three ordinary profiles | Structural mechanics revision |
| Balance Channel membership | exact six-Channel maps | one through six valid unique canonical Channels | Structural mechanics revision |
| Band maxima | `[24,49,74,100]` | four increasing integer maxima ending in `100` | Public-contract tuning |

The five relationship states, twenty signal IDs, ten category IDs, two-signals-per-category structure, ordinary weighted-sum operation, two Balance operations, fixed-point scales, half-up reducers, `0..200` signal domain, and `0..100` score domain are fixed v1 invariants, not tuning knobs.

Any numeric tuning or referenced governed-source byte change requires a new immutable `config_id`, new canonical configuration bytes, a new manifest cut, a new `release_id`, regenerated deterministic goldens, and an explicit Product Owner adoption record. A structural mechanics revision additionally requires a PF01 Doc Delta naming every changed signal row and its rationale. A band change additionally requires review of affected public contracts before activation.

Callers cannot pass weights, profiles, bands, or a configuration ID. Production cannot blend configurations and selects exactly one active configuration per release. Rollback selects one complete prior release rather than mixing old code and new configuration.

### **5.2.8 Change control**

Any modification to the signal domain, pair preimage, pair-key version, category input lists or bounds, base formula, rounding order, score clamp, or active weighting posture is a PF01 math change. Any corresponding governed artifact-byte change requires a new manifest cut and `release_id` under **PF12-Canon-HDE-Schemas-and-Artifacts**. Presets and alternative profiles require separately authorized Future-Promotion.

### **5.2.9 Routing (no transport bytes here)**

Math only. Public presentation remains the §2 harmony-only, numeric-free projection; transport bytes live in their owning transport canon. `engine.core.core` is the canonical compatibility behavior home. The pinned `engine.compat.ts_v0` path is transitional, `engine.compat.compute` is admin-only, and `engine.magic10.calculators` is transitional. No pinned `engine.core.core` function implements this complete recipe; this is an explicit implementation gap.

## **5.3 Band mapping (global inclusive maxima)**

**Definition (normative).** Band mapping converts each intrinsic integer category score in `0..100` to exactly one of four bands using the single global inclusive-high maxima governed by `math/thresholds.json`: `[24,49,74,100]`.

* **Cool:** `0 ≤ score ≤ 24`  
* **Open:** `25 ≤ score ≤ 49`  
* **Warm:** `50 ≤ score ≤ 74`  
* **Glow:** `75 ≤ score ≤ 100`

No current preset-specific band maxima exist. Preset-specific maxima or an alternative band profile require separately authorized Future-Promotion and must not be inferred from legacy configuration or examples.

**Coupling to the freeze pack.** The score clamp, rounding mode, and global band maxima are governed at `math/thresholds.json` by **PF12-Canon-HDE-Schemas-and-Artifacts**. Any governed byte change requires a new manifest cut and `release_id` under §3.1.

### **5.3.1 Domain and monotonicity**

* **Score domain.** Input is the integer score `score_c` from §5.2 after exact mean integerization and global clamping.  
* **Monotone mapping.** If `s1 ≤ s2`, then `band(s1) ≤ band(s2)` in the total order `Cool < Open < Warm < Glow`.  
* **No gaps or overlaps.** Every integer in `0..100` maps to exactly one band; each listed maximum is inclusive.  
* **No score mutation.** Band selection does not round, clamp, weight, or otherwise change the score.

### **5.3.2 Boundary behavior (normative)**

* `24` → **Cool**; `25` → **Open**.  
* `49` → **Open**; `50` → **Warm**.  
* `74` → **Warm**; `75` → **Glow**.  
* `100` → **Glow**.

### **5.3.3 Determinism and neutrality**

* **AB↔BA identity.** The canonical score matrix is order-neutral; applying this pure integer comparison produces the same band matrix for AB and BA.  
* **Two-run identity.** The same scores and governed thresholds produce identical bands.  
* **No float dependence.** Mapping uses only integer comparisons; platform and locale cannot affect the result.

### **5.3.4 Validation (binary)**

* **Completeness:** every category score in `0..100` maps to exactly one of `Cool`, `Open`, `Warm`, or `Glow`.  
* **Boundary proofs:** governed cases cover `24/25`, `49/50`, `74/75`, `0`, and `100`.  
* **Matrix parity:** the complete AB and BA band vectors are identical; two identical runs yield identical vectors. Static test definitions or artifacts do not establish a PASS.

### **5.3.5 Change control**

* **Math change.** Adjusting a maximum, band label, band order, comparison posture, or score domain is a PF01 math change.  
* **Artifact coupling.** A corresponding change to `math/thresholds.json` or another governed artifact requires a new manifest cut and `release_id` under **PF12-Canon-HDE-Schemas-and-Artifacts**.  
* **Downstream lockstep.** Consumer schemas and governed acceptance families must remain consistent with the single mapping; acceptance-token semantics and Evidence Catalog paths stay in their owning canon.

### **5.3.6 Routing (no transport bytes here)**

Math only. CLI/Reader payloads, headers, validators, and evidence-path inventories remain in their canonical owners.

**Acceptance families (titles only)**  
`BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `INTRINSIC_SCORING_INT_OK`, `ROUND_HALF_UP_OK`,  
`COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`,  
`RELEASE_ID_RECOMPUTE_OK`, `EVIDENCE_INDEX_UPDATED_OK` when governed threshold bytes change.

## **5.4 Manifests and freeze-pack coupling (change ⇒ new `release_id`)**

**Purpose (normative).** This section identifies the PF01 math inputs that must participate in governed release identity and the PF01 rules that make their bytes release-significant. **PF12-Canon-HDE-Schemas-and-Artifacts** is the single home for complete manifest membership, artifact schemas and paths, canonical serialization, and `release_id` construction. PF01 does not redefine the complete manifest as math-only; manifest members may include non-math release inputs owned elsewhere. Transport and operational semantics remain out of PF01 scope.

### **5.4.1 What the freeze pack contains (math inputs required by PF01)**

At minimum, PF01 computation depends on these governed inputs:

* **Category order.** `catalog/magic10.json`, containing the closed Magic-10 identifier set and frozen order used by §§5.1–5.3.  
* **Category signal inputs and bounds.** `catalog/magic10_caps.json`, containing the exact ordered input list and integer bounds for every Magic-10 category.  
* **Global score and band rules.** `math/thresholds.json`, containing the `0..100` score clamp, `ROUND_HALF_UP`, and inclusive maxima `[24,49,74,100]`.  
* **Topology catalogs.** `catalog/gates_v1.json` and `catalog/channels_v1.json`, with canonical Gate membership, center IDs derived from Gate rows, and canonical `NN-NN` Channel identities.  
* **Feature constants.** The exact denominator and limit contract in §5.4.2 when consumed by PF01 feature math.  
* **Direct Motor→Throat set.** The governed four-Channel set in §5.4.2.1 when serialized for consumption.  
* **Seeds.** A governed Seeds catalog may be an admin/test release input, but Seeds do not enter the intrinsic §5.2 score formula.  
* **Active Magic10 mechanics configuration.** The Required-Now v1 formula uses one immutable release-bound configuration at `catalog/magic10_mechanics_v1.json`, initially identified by `config_id = "m10-channel-state-v1.0.0"`. Its governed bytes bind the §5.2 profiles, signal rows, Channel weights, category-input weights, operations, fixed-point scales, source hashes, and rounding declarations. **PF12-Canon-HDE-Schemas-and-Artifacts** owns its exact path, schema, canonical-byte contract, and manifest membership.  
* **Configuration release coupling.** Production selects exactly one active mechanics configuration per release; callers cannot select or blend configurations. Any governed configuration or referenced source-byte change requires a new immutable `config_id`, manifest cut, and `release_id`; a structural mechanics change also requires a PF01 Doc Delta.

**Future-Promotion boundary.** No current governed Presets catalog, Feature Registry, preset-specific threshold artifact, or advanced token-aggregation artifact exists. The active Magic10 mechanics configuration is the Required-Now production formula bundle, not a preset or alternative scoring profile. If a distinct preset or advanced aggregation artifact is later promoted, **PF12-Canon-HDE-Schemas-and-Artifacts** owns its exact path, schema, and manifest membership; PF01 owns only its fully authorized math.

**Non-content.** HTTP headers, caching and writer policy, CLI streams, validator matrices, evidence-path inventories, and operational procedures are not PF01 math.

### **5.4.2 Constants pack (frozen keys & schema) \[NEW\]**

**Purpose.** PF01 requires the following scalar and vector parameters to be governed before they are consumed by canonical feature math. The pinned repository contains corresponding Python constants, but current **PF12-Canon-HDE-Schemas-and-Artifacts** does not establish a separate governed constants-pack path or manifest entry. The schema below remains a Required-Now PF01 contract with an explicit artifact-implementation gap; no path may be invented.

**D1 — Frozen keys (normative)**

* `limits.em_max` *(int, \> 0\)*  
* `limits.throat_em_max` *(int, ≥ 0\)*  
* `limits.centers_max` *(int, \> 0\)*  
* `limits.mind_throat_max` *(int, ≥ 0\)*  
* `limits.motor_throat_max` *(int, ≥ 0\)*  
* `limits.comp_max` *(int, ≥ 0\)*  
* `bands.thresholds` — array of four integers `[cool, open, warm, 100]` with `0 ≤ cool ≤ open ≤ warm ≤ 99 < 100`; the current governed values are `[24,49,74,100]`.

**Note (v1).** XR windows, `alpha`, hysteresis, and other resonance diagnostics are not members of this constants contract. If later promoted and catalogized by **PF12-Canon-HDE-Schemas-and-Artifacts**, they become governed release inputs and any byte change requires a manifest cut and new `release_id`.

**D2 — JSON shape (normative)**

When this constants contract is represented as a governed JSON artifact, its payload is exactly:

```json
{
  "limits": {
    "em_max": <int>,
    "throat_em_max": <int>,
    "centers_max": <int>,
    "mind_throat_max": <int>,
    "motor_throat_max": <int>,
    "comp_max": <int>
  },
  "bands": { "thresholds": [ <int>, <int>, <int>, 100 ] }
}
```

The stored artifact MUST use the canonical JSON rules owned by **PF12-Canon-HDE-Schemas-and-Artifacts**. Any addition, removal, or value change to a consumed governed key is a frozen-input change and requires a new manifest cut and `release_id`.

**Evidence routing (titles-only).** Constants-domain, boundary, and release-recompute evidence families are governed by the Evidence Catalog in **PF12-Canon-HDE-Schemas-and-Artifacts**. Applicable token names include `JSON_CANONICAL_CHECK_OK`, `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `RELEASE_ID_RECOMPUTE_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, and `EVIDENCE_INDEX_UPDATED_OK`; PF01 does not define their semantics or paths.

#### **5.4.2.1 Direct Motor→Throat (v1) — governed set**

**Purpose (normative).** Define the direct-only Motor→Throat set used by denominator logic. The set MUST NOT include two-hop routes.

**Canonical definition**

* **Set (`NN-NN`, min-first; ASCII-sorted):** `["12-22","20-34","21-45","35-36"]`  
* **PF01 boundary.** Stored and computation-boundary values MUST already be zero-padded canonical `NN-NN` with the lower Gate first.  
* **Ingestion alias boundary.** An upstream ingestion surface may map a reversed alias such as `34-20` to `20-34` only when its owning contract explicitly authorizes that normalization before PF01 validation.  
* **Rejection posture.** Unknown, duplicate, unparsable, or noncanonical values at the PF01 boundary fail validation; no silent coercion occurs here.

**Storage and serialization**

* When governed as JSON, represent the set as an array of exactly the four strings above.  
* Apply the canonical array-as-set and JSON byte rules owned by **PF12-Canon-HDE-Schemas-and-Artifacts**.  
* The artifact is listed under the repository-relative path, hash, size, and manifest-root semantics governed by **PF12-Canon-HDE-Schemas-and-Artifacts**; PF01 does not restate those manifest fields.  
* Any addition, removal, or value change is a frozen-input change requiring a manifest cut and new `release_id`.  
* **Static implementation posture.** The pinned `engine/constants.py` contains the exact four-value tuple. No separate governed JSON artifact or manifest entry was found at the expected catalog/manifest loci, so artifact closure remains an implementation gap.

**Validation (binary)**

* **Set equality.** The governed value equals the four-element canonical list above.  
* **Canonical identity.** Every member is a known canonical Channel in `catalog/channels_v1.json`; the stored list is unique and ASCII-sorted.  
* **Manifest closure.** When the set is consumed as a governed artifact, its repository-relative path, canonical-byte hash, and size are present in the manifest.  
* **Evidence ownership.** Direct-Motor→Throat and release-identity evidence families route to **PF12-Canon-HDE-Schemas-and-Artifacts**.

**Acceptance names (titles-only).** `MOTOR_THROAT_DIRECT_ONLY_OK`, `RELEASE_ID_RECOMPUTE_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`.

### **5.4.3 Canonical manifest (construction rules)**

To produce `release_id`, use the single canonical manifest at `catalog/manifest.json` governed by **PF12-Canon-HDE-Schemas-and-Artifacts**:

1. **Normalization.** Serialize each governed JSON artifact with canonical UTF-8, no BOM, ASCII-sorted object keys, compact separators, and exactly one trailing LF; arrays used as sets are deduplicated and ASCII-sorted.  
2. **Entry list.** `files` is ASCII-sorted by `path`. Each entry contains:  
   * `path` — repository-relative POSIX path; no leading slash, backslash, NUL, `..` segment, self-listing, or path normalization difference.  
   * `sha256` — lowercase 64-hex SHA-256 of the governed bytes.  
   * `size` — integer byte length of those bytes.  
3. **Manifest metadata.** Top-level keys are exactly `root`, `version`, `built_at_utc`, and `files`. `root` is required identity metadata and not a path-resolution base. `built_at_utc` MUST be supplied by one deterministic governed build input and MUST NOT be sampled during serialization.  
4. **Hash.** `release_id = sha256(canonical_bytes("catalog/manifest.json"))` in lowercase hex.

For a governed non-JSON artifact, canonical bytes are its literal file bytes unless its owner defines another exact byte contract.

**Static implementation posture.** The pinned manifest is canonical and the runtime hashes it, but the manifest has eight entries and omits current PF12-required topology and complete Magic-10 narrative members. Its bytes and runtime definition do not establish complete manifest conformance, validation PASS, deployment, or acceptance.

### **5.4.4 Change policy (what forces a new `release_id`)**

A new manifest cut and `release_id` are required for any governed byte change affecting:

* **Category domain.** Magic-10 membership or order.  
* **Signal contract.** Category input lists, input bounds, or another governed §5.2 scoring input.  
* **Thresholds.** Global score clamp, rounding declaration, band maxima, or band mapping.  
* **Topology.** Gate or Channel catalog content used by PF01.  
* **Feature constants.** A consumed key or value from §5.4.2.  
* **Direct Motor→Throat set.** Any member, representation, or governed artifact byte.  
* **Promoted future artifacts.** A preset, alternative profile, registry, or aggregation artifact only after explicit promotion establishes it as governed.  
* **Serialization or manifest contract.** Canonical shape, order, metadata, membership, or another manifest byte.

Pure source reformatting that produces identical governed canonical bytes does not change `release_id`, but noncanonical stored bytes still fail their own validation contract.

### **5.4.5 Determinism and neutrality guarantees**

* **Two-run identity.** Building from identical governed sources and the same deterministic manifest metadata yields identical manifest bytes and `release_id`.  
* **AB↔BA neutrality.** Release identity is independent of pair order.  
* **Environment independence.** Pair-time transport configuration, headers, locale, network state, and viewer preferences do not enter release identity.

### **5.4.6 Validation (binary)**

* **Closure.** Every governed math input consumed by scoring or feature extraction resolves to a manifest member when its artifact contract requires manifest membership.  
* **Reproducibility.** Recomputing SHA-256 over the canonical stored manifest reproduces `release_id`.  
* **Member integrity.** Each manifest member's governed bytes match its recorded `sha256` and `size`.  
* **No self-listing and safe paths.** Manifest membership and paths satisfy the PF12 contract.  
* **Evidence boundary.** Evidence updates and acceptance claims are verified in their owning canon; static artifact presence alone does not establish PASS.  
* **Current gap.** The pinned manifest does not yet demonstrate required closure for PF01 topology, complete Magic-10, constants, and direct-Motor→Throat inputs.

### **5.4.7 Backwards-compatibility posture**

Changing governed pack bytes does not by itself change the Reader v1 public covenant. Reader v1 remains bands-only, numeric-free, and harmony-only unless a separately authorized public-contract version change widens it. Any future public exposure of the full ten-category matrix requires coordinated versioning without changing the current canonical calculation domain.

### **5.4.8 Routing (no transport bytes here)**

PF01 defines math input significance and release coupling. **PF12-Canon-HDE-Schemas-and-Artifacts** owns artifact schemas, paths, complete manifest membership, canonical bytes, and Evidence Catalog records. Architecture owns wiring. Transport headers, conditional delivery, caching and writer policy, CLI validators, evidence procedures, and acceptance semantics stay in their own canonical homes.

## **5.5 Privacy posture (no percent/numerics on public) \[Required-Now\]**

**Principle (normative).**  
The public Reader v1 surface is **numeric-free**. No scores, percentages, counters, or derived numeric indicators may appear in public success bodies. Public items are **exactly** `{id, band}` (see §2.2); all other quantitative signals remain **internal**.

### **5.5.1 Allowed vs. disallowed (public success)**

* **Allowed:**  
    
  * `categories[*]`: `{ "id": <Magic-10 id>, "band": "Cool"|"Open"|"Warm"|"Glow" }`  
      
  * `reader_version`, `eligible`, `meta{engine_tag,invocation_tag}`, `release_id`, `idempotence_hash`


* **Disallowed (examples):**  
    
  * `score`, `score_pct`, numeric ranks or counts, confidence/uncertainty values, thresholds, weights, or any numeric fields embedded in categories or at top level  
      
  * narrative or prompt text (see Appendix D — Retired)

### **5.5.2 Scope and containment**

* **Internal-only numerics.** All current per-category integers in `[0..100]` and intermediate pair signals remain inside the engine or authorized internal/admin surfaces. Any future-promoted preset arithmetic, cap, floor, dampener, or alternative profile is also internal unless a separately authorized public version change says otherwise.  
    
* **No leakage via metadata.** `meta` is strictly `{engine_tag, invocation_tag}` (non-PII strings); it must not encode numeric telemetry or user-specific counts.

### **5.5.3 Determinism & routing**

* This posture does **not** alter determinism: preimage rules, AB↔BA identity, and two-run identity still apply (see §3).  
    
* Transport/CLI behavior (e.g., admin streams, headers, or validators) is **not** restated here and is referenced **by title only** in PF-Canon-HDE-CLI-API-Vendor-Ref.

### **5.5.4 Validation (binary)**

* **Schema gate requirement:** the public success schema MUST reject any numeric fields beyond the six-key covenant (for example, `score` or `score_pct`). The pinned schema does not fully enforce the covenant and remains an implementation gap.  
    
* **Golden proof requirement:** governed public goldens and grep-guards cover `categories[*]` containing only `{id, band}` and top-level keys matching the six-key covenant. Static files alone do not establish PASS.  
    
* **Parity checks:** a CLI Reader-byte sidecar and Reader body MUST be byte-identical under this numeric-free policy. General `showcompat` stdout is an admin/compat payload and is not Reader bytes.

### **5.5.5 Change control**

* Introducing public numerics (e.g., exposing per-category scores or percentages) is a **versioned public-contract change** and requires an explicit Reader version bump and coordinated acceptance.  
    
* Until such a change is approved and versioned, the **numeric-free** public covenant stands.

>   
> Note: Internal math exists; public exposure of the full 10-item array is **Reader v2** (future).

## **5.6 Resonance posture (SR/XR; α; hysteresis) \[Required-Now\]**

**Purpose (normative).** Define the v1 resonance posture and its effect on public output. **Public output remains bands-only and numeric-free**; no SR/XR numerics are exposed (see §2).

This subsection does not add a second active scoring formula after §5.2. For the Required-Now intrinsic matrix, `SR_c` refers only to the current `score_c` produced by §5.2; no separate SR reducer, XR reducer, blend, or hysteresis stage is active in the current reduction contract.

**Normative/postponed behavior (v1).**

* **SR requirement, XR postponed.** `alpha = 1.0` declares an all-SR posture if the future blend surface is promoted; current intrinsic scoring remains the complete §5.2 v1 formula, with no separate SR reducer or XR blend.  
* **Hysteresis armed for future XR.** A one-point guard at the Open↔Warm boundary is defined for future use **only when `alpha < 1.0`**; with `alpha = 1.0` it is inert and not applied.  
* **Current formula boundary.** `resonance_strength` is the ordinary §5.2 signal produced from `05-15`, `06-59`, `12-22`, and `13-33` through `coherence_bp_v1`. No separate SR/XR blend, `alpha`, or hysteresis stage is active in the canonical v1 formula.

**Pack membership in v1 (governance rule).**

* **Not part of the constants pack.** Resonance parameters (α, hysteresis, XR windows/reducers) are **not** members of the frozen constants pack in v1 and **must not** appear in the freeze-pack manifest.  
* **Future catalogization.** If any resonance parameter is later catalogized in **PF12-Canon-HDE-Schemas-and-Artifacts** and listed in `catalog/manifest.json`, it becomes a **frozen input** and any value change **yields a new `release_id`** (see §3.1).

**Computation model (informative; deferred paths).**

* **SR (current mathematical meaning).** Integer `SR_c ∈ [0..100]` is the §5.2 intrinsic `score_c`; no additional rounding or transformation occurs.  
* **XR (deferred).** When separately promoted in a future version, XR is computed over governed windows and blended as `R* = α·SR + (1 − α)·XR`; integerize through a complete, separately authorized fixed-point contract consistent with §5.2.  
* **Hysteresis (only if α \< 1.0).** Apply a ±1 Schmitt-style guard at the Open/Warm boundary **before** §5.3 band mapping; other boundaries remain inclusive per §5.3.

**Determinism.**

* **AB↔BA identity.** Resonance uses the normalized composite (see **PF12-Canon-HDE-Schemas-and-Artifacts** topology normalization); identical inputs ⇒ identical outputs.  
* **Two-run identity.** Same inputs and catalogs/constants ⇒ identical results and banding (§5.3).  
* **Pins.** Run byte-checked evidence with `LC_ALL=C`, `TZ=UTC`.

**Validation & evidence (titles-only).**

* **No public numerics.** Reader/CLI success bodies remain bands-only; any SR/XR values, if computed internally, are not serialized.  
* **Provenance.** If a future version catalogizes resonance parameters, its governed artifact, release binding, and evidence family are registered under the Evidence Catalog in **PF12-Canon-HDE-Schemas-and-Artifacts**. PF01 does not maintain a parallel path list.

**Routing (no transport bytes here).** Headers, conditional delivery, caching, and validator matrices live in **HDE-CLI-API-Vendor Ref** / **HDE-Governance** (titles-only).

---

# **6\. Feature Extraction (engine-facing; deterministic) \[Required-Now\]**

## **6.1 Electromagnetics (EM): detection and throat flags**

### **Purpose (normative)**

Detect electromagnetic relationships between two normalized charts and produce bounded, deterministic feature outputs. Electromagnetism is the pair-level result of reciprocal opposite hanging Gates that complete the same cataloged Channel. Hanging-Gate records are derivation provenance and do not create a second feature contribution. EM detection is engine-internal; Reader v1 exposes neither EM nor HG records and remains numeric-free.

### **Inputs (closed and validated)**

* **Pair-normalized charts.** Canonicalize the two Gate sets before detection so that AB and BA resolve to the same normalized pair.  
* **Gate Catalog.** `catalog/gates_v1.json` supplies the closed Gate domain and the canonical center for each Gate.  
* **Channel Catalog.** `catalog/channels_v1.json` supplies the closed Channel domain, each Channel's two Gate endpoints, and its center adjacency. Each catalog must pass its owning PF12 validation contract before feature extraction.  
* **Catalog closure.** Every input Gate must exist in the Gate Catalog; every Channel endpoint must resolve to that catalog; and every derived `channel_id` must identify exactly one Channel row.

### **Invariants (applies to every EM computation)**

* **Deterministic and pure.** No time, network, randomness, environment access, or file I/O occurs during computation. Catalogs arrive as normalized inputs.  
* **AB↔BA symmetry.** EM outputs for AB equal those for BA after pair normalization.  
* **Closed vocabularies.** Outputs draw only from validated catalog IDs and bounded booleans or enums; no free text and no arbitrary keys.  
* **Numeric-free feature identity.** EM and HG emit no independent score, count, bonus, token, or category weight. Downstream logic may consume each EM Channel identity at most once.

  ### **Detection (normative rules)**

For each canonical Channel `c` with endpoint Gates `x` and `y`, define:

* `A_x`, `A_y`: whether member A owns each endpoint;  
* `B_x`, `B_y`: whether member B owns each endpoint;  
* `A_full = A_x and A_y`;  
* `B_full = B_x and B_y`;  
* `A_count = A_x + A_y`;  
* `B_count = B_x + B_y`.

Apply the first matching rule:

| Priority | State | Exact predicate | Owner field |
| ----- | ----- | ----- | ----- |
| 1 | `companionship` | `A_full and B_full` | absent |
| 2 | `compromise` | exactly one member is full and the other has exactly one endpoint | full-Channel owner |
| 3 | `dominance` | exactly one member is full and the other has zero endpoints | full-Channel owner |
| 4 | `electromagnetic` | neither is full and the members exclusively own opposite endpoints | absent |
| 5 | `none` | every other pattern | absent |

For `dominance` and `compromise`, normalize the owner as `member_lo` or `member_hi` after intrinsic numeric Gate-mask ordering. All other states omit the owner field.

An electromagnetic state requires exactly one of:

* `A_x and not A_y and not B_x and B_y`;  
* `not A_x and A_y and B_x and not B_y`.

The hanging-Gate process in §6.2 is a derived detection stage for the same classifier. It may join only reciprocal records for the same Channel with opposite present endpoints and must emit the same single electromagnetic Channel identity. It creates no independent contribution.

Unmatched hanging Gates, same-end hanging Gates, one unmatched half, and Gate repetition resolve to `none` unless a higher-priority full-Channel rule applies. A Channel is classified exactly once.

* **Gate-to-Channel resolution.** Every classified Channel must resolve to exactly one validated Channel row. Ambiguous or unmapped combinations fail closed with a typed error.  
* **De-duplication.** A canonical Channel contributes at most once to the five-state vector and at most once to any configured signal row.  
* **Canonical `channel_id`.** The Channel Catalog identity is `"<lowGate>-<highGate>"`, with numeric endpoints in ascending order and zero-padded to two digits (`01..64`). Example: Gates `{8,1}` resolve to `"01-08"`.  
* **Sorting.** Channel-state rows and the derived EM Channel list must be duplicate-free and ASCII-sorted by canonical `channel_id`.

### **Throat flags (normative)**

* **Throat involvement.** After the EM set is complete, set `throat_em = true` when any EM Channel's cataloged center set includes `throat`; otherwise set it to `false`.  
* **Throat-adjacent path.** If an externally governed catalog enum authorizes a throat-adjacent pathway, `throat_route` may carry that bounded enum; otherwise it is omitted or `null`.  
* **Closed values.** Flags are bounded booleans or externally governed enums.

### **Output (engine-facing; normative relationship)**

```json
{
  "em": {
    "channels": ["01-08", "10-20"],
    "present": true
  },
  "throat_em": true,
  "throat_route": null
}
```

* The `channels` array contains only canonical `channel_id` strings and is duplicate-free and ASCII-sorted.  
* `present` is true exactly when `channels` is non-empty.  
* HG provenance is nested under, or consumed while constructing, the corresponding internal EM record. It is not a peer aggregatable output.  
* The stable pair-level feature is the sorted unique EM Channel identity set. No score or count is part of that feature identity.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites are missing or invalid, including malformed Gates or incompatible chart normalization.  
* **CATALOG\_MISMATCH** — an input or derived identity references a Gate or Channel absent from the validated catalogs.  
* **AMBIGUOUS\_COMPLEMENT** — an endpoint pair resolves to more than one candidate Channel; the detector fails closed rather than guessing.

### **Determinism and acceptance (when wired)**

* **AB↔BA parity proof.** EM outputs are identical for AB and BA.  
* **Two-run identity.** Recomputing EM with the same normalized inputs and catalogs yields byte-identical internal feature records.  
* **Catalog coverage.** Governed tests must demonstrate positive and negative cases across representative throat-linked and non-throat Channels and every ownership classification.  
* **Fail-closed proofs.** Unmapped, ambiguous, or invalid combinations must yield typed failures and no partial EM items.  
* **Sorting and uniqueness.** Governed tests must verify ASCII order and per-Channel set semantics.  
* **Implementation posture.** EM/HG derivation is a current requirement with an implementation gap. Checked-in constants, toggles, tests, or evidence references do not by themselves prove a conforming extractor.

### **Change control**

Any change to the EM predicate, ownership classification, Channel identity, catalog topology, sorting rule, failure behavior, or externally governed flag enum is a governed math or catalog change and requires the applicable PF12 release and Doc-Delta treatment. Acceptance artifacts must be regenerated only through the separately authorized implementation and evidence workflow.

### **Public surface rule**

EM and HG remain engine-internal. Reader v1 stays numeric-free and emits only its approved `harmony` projection. No EM- or HG-derived numeric, record, or narrative is added to Reader v1.

### **Routing**

HDE-Math-Spec owns the EM/HG math. HDE-Schemas & Artifacts owns the Gate and Channel paths, schemas, validation, manifest treatment, and artifact contracts. HDE-Architecture owns component wiring. Transport and CLI behavior is owned by HDE-CLI-API-Vendor-Ref and is not restated here.

## **6.2 Hanging-gate derivation provenance \[Required-Now\]**

**Purpose (normative).**  
Identify each person's per-Channel half-channel state, preserve the present and missing endpoints as derivation provenance, and use reciprocal opposite records to derive the pair-level EM identity in §6.1. HG provenance is engine-internal, is not a peer aggregatable feature, and contributes zero independent score, count, bonus, token, or category weight.

### **Inputs (closed & validated)**

* **Pair-normalized charts.** Detection consumes the same normalized pair used by §6.1 while retaining which normalized person owns each Gate.  
* **Gate and Channel catalogs.** Use the validated `catalog/gates_v1.json` and `catalog/channels_v1.json` rows described in §6.1. Every endpoint and center assignment must resolve exactly.

### **Invariants (applies to every HG computation)**

* **Deterministic and pure.** No time, network, randomness, environment access, or file I/O occurs during computation.  
* **AB↔BA symmetry.** Pair-level EM output is invariant under input reversal; member provenance follows the normalized member identities.  
* **Closed vocabularies.** Only validated `channel_id` and Gate IDs may appear in required HG provenance. Any optional diagnostic field requires an externally owned schema.  
* **No independent contribution.** HG provenance is consumed only to construct EM and cannot be counted or weighted separately.

### **Detection (normative rules)**

1. **Per-person half-channel state.** For a person `P` and Channel `C={g1,g2}`, create one HG record exactly when `P=(1,0)` or `P=(0,1)`.  
2. **Required provenance.** Each record contains the canonical `channel_id`, the present Gate, and the missing harmonic Gate.  
3. **Reciprocal join.** Join only A/B HG records for the same Channel when their present endpoints are opposite. One reciprocal pair derives one deduplicated EM identity.  
4. **Same-person full Channel.** `P=(1,1)` is that person's defined Channel and produces no HG record for `P`; it is never EM by itself.  
5. **Unmatched and same-end halves.** A half with no complementary half and two people owning the same endpoint do not produce EM.  
6. **Catalog consistency.** Endpoint or center mismatches fail closed.  
7. **Derivation order.** Validate catalog closure; canonicalize both Gate sets; derive HG records per person; join reciprocal opposite records; emit one unique EM identity per Channel; ASCII-sort the EM set; then derive `throat_em` from Channel center adjacency.

### **Optional diagnostic provenance (externally schema-gated)**

A diagnostic surface may expose per-member HG provenance only when an externally owned schema authorizes its exact fields and values. Reader v1 exposes neither HG provenance nor EM records. Without that schema, HG records remain an internal derivation stage and are consumed while constructing EM.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — inputs are malformed or prerequisite data is missing.  
* **CATALOG\_MISMATCH** — a Gate, Channel, endpoint, or center assignment does not resolve in the validated catalogs.  
* **AMBIGUOUS\_COMPLEMENT** — the same endpoint pair resolves to multiple candidate Channels; the detector fails closed.

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** Reversing input order preserves the sorted pair-level EM identity set and normalized member provenance.  
* **Two-run identity.** Recomputing from the same normalized inputs and catalogs yields byte-identical internal derivation records.  
* **Catalog coverage.** Governed tests must cover reciprocal opposite halves, same-end halves, unmatched halves, same-person full Channels, dominance, compromise, companionship, throat adjacency, and non-throat Channels.  
* **Fail-closed proofs.** Ambiguous or unmapped endpoints must return typed failures and no partial EM or HG output.

### **Change control**

Any change to the half-channel predicate, required provenance, reciprocal join, ownership classification, catalog topology, or failure behavior is a governed math or catalog change and requires the applicable PF12 release and Doc-Delta treatment.

### **Public surface rule**

HG provenance and EM records remain engine-internal. Reader v1 exposes neither and remains numeric-free.

### **Routing**

HDE-Math-Spec owns HG/EM derivation math. HDE-Schemas & Artifacts owns catalog paths, schemas, and artifacts. HDE-Architecture owns wiring. Transport and CLI behavior is owned by HDE-CLI-API-Vendor-Ref and is not restated here.

## 6.3 Dominance / Compromise — center tagging \[Speculative\]

**Purpose (normative).**  
Produce **bounded, deterministic** center-level tags for a normalized pair indicating **dominance / compromise / neutral** relationships per center definitions in the freeze pack. These tags are **engine-internal**; Reader v1 remains numeric-free and bands-only (§2.2).

### Inputs (closed & validated)

* **Pair-normalized charts.** All computation consumes the **normalized** (order-neutral) pair.  
    
* **Frozen catalogs.** The freeze pack (see §5.4) defines, per center:  
    
  * Center **IDs** and **topology** (closed set).  
      
  * Center-level **definition rules** and any applicable complements.  
      
  * Allowed **enums** for dominance/compromise outcomes and optional sub-flags.  
    Any catalog change requires a new `release_id` (§3.1).

### Invariants (applies to every center tagging pass)

* **Deterministic & pure.** No time, network, randomness, or file I/O.  
    
* **AB↔BA symmetry.** Results for **AB** equal those for **BA** after normalization.  
    
* **Closed vocabularies.** Only cataloged center IDs and **fixed enums** may appear; no free text.  
    
* **Numeric-free outputs.** Tags are enums/booleans only; no counts, no scores.

### Tagging (conceptual rules)

1. **Per-center evaluation.** For each cataloged center, derive a **relationship outcome** from the two inputs and the center’s rules:  
     
   * **dominant** — one participant’s configuration at the center **preponderates** per catalog criteria.  
       
   * **compromise** — competing configurations **must resolve** to a cataloged compromise state.  
       
   * **neutral** — neither dominance nor compromise criteria are met.

   

2. **Decision closure.** Every evaluated center **must** yield exactly one of `{dominant, compromise, neutral}`; ambiguous cases **fail closed** (typed error).  
     
3. **No cross-center leakage.** A center’s tagging depends only on rules/material for that center; other centers may not modify its outcome except via cataloged cross-links (if any).

>   
> **Note:** The precise conditions that trigger **dominant** or **compromise** are pinned by the catalog schema; this spec constrains behavior (determinism, symmetry, closed enums), not rule text.

### Optional sub-flags (catalog-gated)

* **Actor indication.** If the catalog allows, a bounded field may indicate **which** participant is dominant (e.g., `dominant_actor: "min"|"max"` or equivalent, aligned to the normalized pair notion).  
    
* **Topology hints.** Catalog may define additional bounded hints (e.g., `compromise_mode: <enum>`).  
    
* **All sub-flags are optional**, strictly enumerated, and versioned with the catalog.

### Output (engine-facing; example shape)

```json
{
  "center_tags": [
    {"center": "<center_id>", "dominant_actor": "min", "tag": "dominant"},
    {"center": "<center_id>", "compromise_mode": "<enum>", "tag": "compromise"},
    {"center": "<center_id>", "tag": "neutral"}
  ]
}
```

* **Set semantics:** one entry per cataloged center; duplicates are forbidden.  
    
* **No numerics:** tags and optional bounded enums only.

### Typed failures

* **FEATURES\_UNAVAILABLE** — missing prerequisites or malformed inputs.  
    
* **CATALOG\_MISMATCH** — center rules/IDs not found in the active freeze pack.  
    
* **AMBIGUOUS\_CENTER\_TAG** — rules yield multiple outcomes for the same center; detector fails closed.

### Determinism & acceptance (when wired)

* **AB↔BA parity proof.** Tag arrays identical for AB and BA (after normalization).  
    
* **Two-run identity.** Re-running with the same inputs/catalog yields byte-identical outputs.  
    
* **Catalog coverage.** Golden tests cover representative centers for each outcome (`dominant`, `compromise`, `neutral`) and negative/edge cases.  
    
* **Fail-closed proofs.** Ambiguous or unmapped cases produce typed failures (no partial tags).

### Change control

* Any change to **center IDs**, **decision enums**, or **per-center rule schemas** is a math-catalog change and requires a **new `release_id`** (§3.1); regenerate acceptance evidence accordingly.

### Public surface rule

* Center tags are **internal-only**; Reader v1 **never** exposes dominance/compromise or related narratives (§2.2).

### Routing

* Transport/CLI validators, status/headers, or admin behavior are **not restated** here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **6.4 Throat adjacency — talk-ladder / narrative / direct-MT flags \[Speculative\]**

**Purpose (normative).**  
Detect **throat adjacency** features for a normalized pair and emit **bounded, deterministic** flags that inform internal weighting only. Three families of flags are considered: **talk-ladder**, **narrative**, and **direct-MT** (direct motor-to-throat), all defined by the freeze-pack catalogs. No public numerics or prose are produced; Reader v1 remains bands-only (§2.2).

### **Inputs (closed & validated)**

* **Pair-normalized charts.** All computation consumes the **normalized** (order-neutral) pair.  
    
* **Frozen catalogs.** The freeze pack (see §5.4) defines:  
    
  * **Center & channel topology** (including throat and motor centers).  
      
  * **Talk-ladder** adjacency rules (permitted routes and hops).  
      
  * **Narrative adjacency** rules (cataloged patterns only).  
      
  * **Direct-MT** definitions (allowed motor→throat pathways).  
      
  * **Closed enums** for all emitted flags.  
    Any change to these catalogs requires a new `release_id` (§3.1).

### **Invariants (applies to every throat-adjacency pass)**

* **Deterministic & pure.** No time, network, randomness, or file I/O.  
    
* **AB↔BA symmetry.** Outputs for **AB** equal those for **BA** after normalization.  
    
* **Closed vocabularies.** Only cataloged IDs/enums may appear; **no free text**.  
    
* **Numeric-free outputs.** Flags are booleans/enums; no counts, no scores.

### **Detection (conceptual rules)**

1. **Talk-ladder adjacency.**  
     
   * Evaluate whether the pair’s combined graph satisfies a **cataloged talk-ladder route** to throat (e.g., center-to-center hop constraints).  
       
   * If multiple routes qualify, reduce to the **highest-priority** catalog route (set semantics).

   

2. **Narrative adjacency (internal flag only).**  
     
   * If a cataloged, **non-textual** narrative adjacency pattern is satisfied (e.g., a specific throat-proximal motif), emit a bounded enum (e.g., `nar_adj: "<enum>"`).  
       
   * This **does not** authorize public narrative text; the flag is internal for weighting.

   

3. **Direct-MT (motor→throat) path.**  
     
   * Detect **direct motor-to-throat** adjacency when the pair’s combined graph forms an allowed **motor→throat** route per catalog.  
       
   * If both talk-ladder and direct-MT are true, **both** flags may be set; conflicts are resolved by catalog precedence.

   

4. **De-duplication & closure.**  
     
   * Emit at most **one** value per flag family (e.g., one `talk_ladder` enum).  
       
   * Ambiguities across aliases or overlapping patterns **fail closed** with a typed error.

### **Output (engine-facing; example shape)**

```json
{
  "throat_adj": {
    "direct_mt": true,
    "nar_adj": "<enum-or-none>",
    "talk_ladder": "<enum-or-none>"
  }
}
```

* Field names and allowed enums are **pinned by the catalog schema**; the example is illustrative.  
    
* **Set semantics:** absence of a condition may be encoded as `null`/omitted (per catalog), not as free-form text.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — missing prerequisites, invalid inputs, or unresolved IDs.  
    
* **CATALOG\_MISMATCH** — pattern references not present in the active freeze pack.  
    
* **AMBIGUOUS\_ROUTE** — multiple competing routes/enums match with no catalog precedence; detector fails closed.

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** Flags identical for AB and BA.  
    
* **Two-run identity.** Re-running with the same inputs/catalog yields byte-identical outputs.  
    
* **Catalog coverage.** Goldens demonstrate positive/negative cases for talk-ladder, narrative adjacency, and direct-MT, including tie-break precedence.  
    
* **Fail-closed proofs.** Ambiguity and catalog gaps return typed failures (no partial flag sets).

### **Change control**

* Any change to **center/channel topology**, **talk-ladder definitions**, **narrative adjacency enums**, or **direct-MT rules** is a math-catalog change and requires a **new `release_id`** (§3.1); regenerate acceptance artifacts accordingly.

### **Public surface rule**

* Throat-adjacency flags are **internal-only** and never appear on Reader v1 (bands-only). No narratives or prompt text are emitted on public surfaces.

### **Routing**

* Transport/CLI validators, status/headers, and admin behavior are **not restated** here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **6.5 Emotional timing & pacing (state \+ dampen flag) \[Speculative\]**

**Purpose (normative).**  
Detect a pair’s **emotional timing** posture and **pacing** condition from normalized charts and emit **bounded, deterministic** flags for internal weighting only. This detector can (a) report a **state enum** and (b) assert a **dampen** flag that instructs aggregation to **reduce** specific contributions when pacing criteria are unmet. No public numerics or narratives are produced; Reader v1 remains bands-only (§2.2).

### **Inputs (closed & validated)**

* **Pair-normalized charts.** All computation consumes the **normalized** (order-neutral) pair.  
    
* **Frozen catalogs.** The freeze pack (see §5.4) defines:  
    
  * Emotional topology and definitions (e.g., emotional center predicates, authority states, timing windows).  
      
  * **Allowed enums** for emotional timing state and dampening rationale.  
      
  * Any cross-links to other features (e.g., throat-EM interplay) declared by ID, not prose.  
    Any catalog change requires a new `release_id` (§3.1).

### **Invariants**

* **Deterministic & pure.** No time, network, randomness, or file I/O.  
    
* **AB↔BA symmetry.** Outputs are identical for **AB** and **BA** after normalization.  
    
* **Closed vocabularies.** Only cataloged enums/IDs may appear; **no free text**.  
    
* **Numeric-free outputs.** Booleans/enums only; no counts or scores.

### **Detection (conceptual rules)**

1. **Emotional timing state**  
     
   * Derive a **state enum** (e.g., `paced`, `not_paced`, or other cataloged states) from the pair’s combined emotional topology according to **catalog rules**.  
       
   * State selection must be **total** (one state chosen) and **deterministic**.

   

2. **Pacing & dampening**  
     
   * If the catalog indicates that **pacing is required** for particular contributions and the pair **is not** in a compliant state, set `dampen = true`.  
       
   * If pacing criteria are satisfied, set `dampen = false`.  
       
   * When asserted, `dampen` **reduces** only those internal contributions explicitly listed by the catalog (e.g., specific families or signals) and **never** introduces public numerics.

   

3. **Cross-feature coupling (catalog-gated)**  
     
   * Optional hints (e.g., “throat-EM eligible for bonus only when `paced`”) are expressed as **bounded enums/IDs** that downstream aggregation can interpret deterministically.  
       
   * No detector may alter another detector’s raw outputs; coupling is expressed via **aggregation rules** that read these flags.

### **Output (engine-facing; example shape)**

```json
{
  "em_timing": {
    "dampen": true,
    "reason": "<enum-or-none>",
    "state": "<enum>"
  }
}
```

* Field names and allowed enum values are **pinned by the catalog schema**; the example is illustrative only.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites missing/invalid; state cannot be derived deterministically.  
    
* **CATALOG\_MISMATCH** — referenced IDs/states not present in the active freeze pack.  
    
* **AMBIGUOUS\_STATE** — multiple states match with no catalog precedence; detector **fails closed** (no partial flags).

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** Identical `em_timing` for AB and BA.  
    
* **Two-run identity.** Re-running with the same inputs/catalog yields byte-identical outputs.  
    
* **Catalog coverage.** Golden tests show positive/negative edges for `state` and `dampen`, including precedence resolution.  
    
* **Fail-closed proofs.** Ambiguity and catalog gaps return typed failures.

### **Change control**

* Any change to **state enums**, **pacing criteria**, or **dampening scopes/rationales** is a math-catalog change and requires a **new `release_id`** (§3.1); regenerate acceptance artifacts accordingly.

### **Public surface rule**

* Emotional timing and dampening remain **internal-only**; no timing text, prompts, or numerics are emitted on Reader v1 (§2.2).

### **Routing**

* Transport/CLI behavior (headers, validators) and administrative streams are **not** restated here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **6.6 Families: G-identity, Tribal care, Rhythm, Story, Mind styles \[Speculative\]**

**Purpose (normative).**  
Detect **family-level signals** for a normalized pair and emit **bounded, deterministic** tags per family — **G-identity**, **Tribal care**, **Rhythm**, **Story**, **Mind styles** — for *internal* aggregation only. Families provide coarse structure for weighting/caps/floors in presets (§7) and aggregation (§8). Reader v1 remains numeric-free and bands-only (§2.2).

### **Inputs (closed & validated)**

* **Pair-normalized charts.** All computation consumes the **normalized** (order-neutral) pair.  
    
* **Frozen catalogs.** The freeze pack (§5.4) defines, for each family:  
    
  * The **family ID** (closed set) and **membership map** (what chart features/signals belong to the family).  
      
  * The **allowed enums** for family outcomes and any optional sub-flags.  
      
  * Any **cross-family constraints** or precedence rules the aggregation layer should observe.  
    Any catalog change requires a new `release_id` (§3.1).

### **Invariants (applies to every family)**

* **Deterministic & pure.** No time, network, randomness, or file I/O.  
    
* **AB↔BA symmetry.** Family tags for **AB** equal those for **BA** after normalization.  
    
* **Closed vocabularies.** Only cataloged family IDs and **fixed enums/booleans** may appear; **no free text**.  
    
* **Numeric-free outputs.** Families do **not** emit counts or scores to public surfaces.

### **Detection (conceptual rules)**

1. **Membership resolve.**  
     
   * Resolve chart features into family membership using the catalog map (e.g., all signals that belong to **G-identity**).  
       
   * Treat membership as **set semantics**; duplicates collapse.

   

2. **Family outcome (bounded).**  
     
   * For each family, derive a **bounded enum** (e.g., `"present"|"weak"|"absent"` or a catalog-specific outcome) from the resolved membership and the catalog rules.  
       
   * If multiple outcomes match, apply **catalog precedence**; otherwise fail closed (typed error).

   

3. **No cross-family leakage.**  
     
   * A family’s outcome depends only on the membership and rules declared for that family. Cross-family influences (e.g., “over-concentration” or “floor/cap” suggestions) are **signaled as flags** for the aggregation layer rather than mutating detection.

### **Optional sub-flags (catalog-gated)**

* **Over-concentration flag.** Signals that too many contributing features cluster within a single family (used by aggregation dampeners).  
    
* **Stability/consistency flags.** Bounded booleans or enums indicating cataloged stability conditions (e.g., “stable identity”).  
    
* **Coupling hints.** Catalog may define hints for aggregation (e.g., “prefer floor” for a family when certain conditions hold).

>   
> Names and allowed values are **pinned by the catalog schema**; this spec constrains behavior (determinism, symmetry, closure), not field lists.

### **Output (engine-facing; example shape)**

```json
{
  "families": [
    {"id": "g_identity", "over_concentration": false, "state": "<enum>"},
    {"id": "tribal_care", "state": "<enum>"},
    {"id": "rhythm", "state": "<enum>"},
    {"id": "story", "state": "<enum>"},
    {"id": "mind", "state": "<enum>"}
  ]
}
```

* **One entry per cataloged family**; duplicates are forbidden.  
    
* Enums/flags are **bounded** and versioned with the catalog; **no numerics**.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites missing/invalid; family membership cannot be derived deterministically.  
    
* **CATALOG\_MISMATCH** — family IDs or membership references not present in the active freeze pack.  
    
* **AMBIGUOUS\_FAMILY\_OUTCOME** — multiple outcomes match with no catalog precedence; detector **fails closed**.

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** Family arrays identical for AB and BA (after normalization).  
    
* **Two-run identity.** Re-running with the same inputs/catalog yields byte-identical outputs.  
    
* **Catalog coverage.** Golden tests cover representative positives/negatives per family, including over-concentration and precedence resolution.  
    
* **Fail-closed proofs.** Ambiguity and catalog gaps return typed failures (no partial family sets).

### **Change control**

* Any change to **family IDs**, **membership maps**, **outcome enums**, or **sub-flags** is a math-catalog change and requires a **new `release_id`** (§3.1); regenerate acceptance artifacts accordingly.

### **Public surface rule**

* Family outcomes and flags are **internal-only**; Reader v1 **never** exposes family tags, narratives, or counts (§2.2).

### **Routing**

* Transport/CLI validators, status/headers, and admin behavior are **not** restated here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **6.7 Planetary micro \[Future-Promotion\]**

**Purpose (future-promotion boundary).**  
Retain the planetary-micro detector concept without treating an invented preset identity, token mapping, cap, default, or aggregation stage as current authority. No governed planetary-micro catalog, preset gate, or token-aggregation contract exists in the current surface. Any implementation remains Future-Promotion under §7.

### **Promotion inputs (closed & validated)**

Promotion requires an exact governed micro catalog path and schema, a complete Human Design-grounded matching model, executable fail-closed validation, fully populated fixed-point values for any downstream contribution or cap, and normalized catalog inputs supplied to pure Engine Core computation. No `A`, `B`, “tiny cap,” example value, or hidden default is executable authority.

### **Invariant detector boundary**

* **Deterministic and pure.** No time, network, randomness, environment access, or file I/O may occur during computation.  
* **AB↔BA symmetry.** Outputs for AB and BA must be identical after pair normalization.  
* **Closed vocabulary.** Only governed micro IDs and bounded enums may appear; no free text or arbitrary keys.  
* **Set semantics.** Alias resolution must be governed, exact, and fail-closed; duplicate micro identities collapse.  
* **Numeric-free extractor output.** A promoted detector may emit only bounded IDs, booleans, or enums. It may not invent a score, count, magnitude, cap, preset gate, or category effect.  
* **No implicit aggregation.** Any future contribution, cap, or category interaction requires the complete §7 promotion prerequisites and one declared evaluation order.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites are missing or invalid.  
* **CATALOG\_MISMATCH** — a referenced micro ID or rule is absent from the promoted governed catalog.  
* **AMBIGUOUS\_MICRO** — multiple conflicting identities match without governed precedence; the detector fails closed.

### **Determinism & acceptance (after promotion)**

Any promoted implementation must prove AB↔BA parity, two-run identity, closed-catalog coverage, set semantics, and fail-closed behavior through the separately governed validation and evidence workflow. This statement does not claim present implementation or test passage.

### **Change control**

Promotion or any later change to micro IDs, matching rules, downstream effects, or cap posture requires PF01 math authority, PF12 schema/path/manifest and release treatment, PF02 wiring consistency, and the applicable Doc-Delta. No preset identity or numeric value may be inferred from this retained concept.

### **Public surface rule**

Planetary micro remains internal and Future-Promotion. Reader v1 does not expose micro records, numerics, or narratives.

### **Routing**

HDE-Math-Spec owns promoted detector and aggregation math; HDE-Schemas & Artifacts owns exact paths, schemas, manifest treatment, and artifact contracts; HDE-Architecture owns component wiring; transport behavior remains outside this section.

# **7\. Presets & Configuration (A/B) \[Speculative\]**

## **7.1 Future-Promotion posture**

The detailed preset, alternate-weight, and advanced token-aggregation design is **Future-Promotion**. No current governed Presets catalog, Feature Registry, or token-aggregation contract exists. The `A/B` wording is retained in this protected H1 identity; it does not establish preset IDs, defaults, active modes, or product behavior. The labels `A` and `B` have no standing authority.

Existing preset-oriented code, toggles, and tests are **LEGACY or orphan implementation surfaces**, not a governed Presets catalog and not authority for product math. No active `presets/` or `config/presets/` catalog is part of the inspected current repository surface. This static posture does not prove runtime, deployment, validation, or test state.

The Future-Promotion classification applies only to presets, alternative weights or scoring profiles, planetary-micro policy, and an advanced token-aggregation layer. It does not defer or narrow the Required-Now intrinsic Magic-10 contract: the canonical result contains scores and bands for exactly all ten frozen categories in frozen order, with Human Design grounding, per-category calculation, and the single §5.3 band mapping.

## **7.2 Promotion prerequisites**

Before any preset or advanced token-aggregation contract becomes current, one governed change must establish all of the following:

1. Product Owner approval of the business meaning and scope of presets, including whether a preset is an internal model version, an admin-only tuning profile, or a user-selectable product feature.  
2. For any advanced aggregation layer beyond the Required-Now intrinsic matrix, a complete and populated Human Design-grounded feature-to-category model in which every additional detector output, feature ID, family, category target, sign, magnitude, and precedence rule is defined exactly once.  
3. Exact governed paths and schemas for the Presets catalog and any Feature Registry, executable fail-closed validators, exact key closure, and explicit unknown-key behavior.  
4. Fully populated integer or fixed-point values for every weight, cap, floor, dampener, correction, and category distribution. Blank values and example defaults are invalid.  
5. One complete evaluation order covering de-duplication, priority or shadowing, signal reduction, corrections, floors, caps, `ROUND_HALF_UP`, clamp, and handoff to the single band mapping in §5.3.  
6. A decision on how presets interact with intrinsic scores and viewer preferences. Viewer preferences remain sampler or ranker inputs and do not alter intrinsic Magic-10 scores or bands.  
7. Pure-compute integration through the canonical Engine Core, with catalogs supplied as normalized inputs rather than loaded from files or environment during computation.  
8. PF12 promotion treatment for schema, manifest, release identity, migration, and governed artifact ownership, followed by an authorized public-contract version change only if a preset becomes externally selectable or changes Reader output.

Until all prerequisites are governed, no label, example, orphan file, empty cell, missing value, or implementation artifact creates a default or executable rule.

## **7.3 Invariants for any promoted design**

* **Closed identities and exact key closure.** Every preset, feature, family, category target, token, enum, and configuration key must belong to a governed closed domain. Unknown or extra keys fail closed.  
* **Deterministic pure computation.** Results depend only on normalized inputs and governed configuration. No time, network, randomness, environment access, file I/O, hidden state, or hidden default may affect computation.  
* **AB↔BA neutrality.** Neutral pair results must be identical after canonical pair normalization. Any directional value must be separately identified and governed.  
* **Fixed-point arithmetic.** All executable magnitudes, weights, corrections, floors, caps, and intermediate values must use the governed integer or fixed-point representation; binary floating point is forbidden.  
* **Rounding and clamp.** Apply `ROUND_HALF_UP` and the governed clamp at the single declared stages. Do not duplicate or reorder band mapping; final band assignment routes to §5.3.  
* **Complete evaluation order.** The promoted contract must declare every stage, precedence relation, de-duplication rule, reduction, correction, floor, cap, rounding point, clamp, and handoff exactly once.  
* **No hidden defaults.** Missing, blank, ambiguous, or ungoverned values fail closed. Examples are not defaults.  
* **No double counting.** A detector identity, including EM derived from HG provenance, may contribute only as its governed feature contract allows; derivation provenance cannot create an independent contribution.

## **7.4 Ownership and public boundary**

* **PF01 — HDE-Math-Spec.** Owns promoted preset semantics, mathematical transformations, exact evaluation order, and aggregation behavior.  
* **PF12 — HDE-Schemas & Artifacts.** Owns exact catalog and artifact paths, schemas or executable validation contracts, manifest membership, migration, release identity, and governed artifact contracts.  
* **PF02 — HDE-Architecture.** Owns component wiring, pure-compute boundaries, and single-home integration. It does not own formulas or artifact schemas.  
* **Engine Core boundary.** Any promoted computation runs through the canonical pure Engine Core with normalized configuration injected as input.  
* **Reader v1 boundary.** Reader v1 remains numeric-free and emits only `harmony`. That output is a projection from the complete canonical ten-category matrix; promotion cannot silently expose presets, scores, weights, tokens, other category bands, EM/HG records, or configuration details.

## **7.5 Promotion and change control**

Promoting presets, a Feature Registry, planetary-micro policy, or advanced token aggregation requires an authorized Doc-Delta that satisfies §7.2 and reconciles PF01 math, PF12 artifact ownership, and PF02 wiring in the same governed change. Any externally selectable preset or Reader-output change also requires the authorized public-contract version change owned outside this section.

This Future-Promotion boundary does not claim implementation completion, runtime success, test passage, deployment, QA, OPS, board, or approval state.

# **8\. Aggregation Algorithm (deterministic, fixed-point) \[Speculative\]**

## **8.1 Current posture and boundary \[Future-Promotion\]**

No current governed Presets catalog, Feature Registry, or advanced token-aggregation contract exists. The checked-in preset-oriented modules and toggles are legacy or orphan implementation surfaces; they do not define product math, active preset identities, defaults, or a governed catalog.

This Future-Promotion posture applies only to presets, alternative weights or scoring profiles, and an advanced token-aggregation layer. It does not defer or narrow the Required-Now intrinsic Magic-10 contract: for every eligible pair, the canonical mathematical result contains exactly one intrinsic integer score and one band for each of the ten closed Magic-10 category IDs, in the frozen order governed by the current catalog. `harmony` is one member of that matrix, not a substitute for the other nine.

The Required-Now intrinsic calculation uses the complete Human Design-grounded reduction defined in §5. It has no current preset-weight operand, category-level preset floor, category cap, family cap, global floor, throat-EM bonus, over-concentration factor, fast-intimacy correction, or family-distribution stage. No absent value or example may become an implicit default.

## **8.2 Future-Promotion prerequisites**

Promotion of presets or an advanced token-aggregation layer requires all of the following before any detailed algorithm becomes normative:

1. Product Owner approval of the business meaning and scope of presets, including whether a preset is an internal model version, an admin-only tuning profile, or a user-selectable product feature. The labels `A` and `B` have no standing authority.  
2. A complete, populated feature-to-category model grounded in Human Design mechanics, with every additional detector output, feature ID, family, category target, sign, magnitude, and precedence rule defined exactly once.  
3. Exact governed paths and schemas for the Presets catalog and any Feature Registry, executable fail-closed validators, and explicit unknown-key behavior.  
4. Fully populated integer or fixed-point values for every weight, cap, floor, dampener, correction, and category distribution. Blank values and example defaults are invalid authority.  
5. One complete evaluation order covering deduplication, priority or shadowing, signal reduction, corrections, floors, caps, `ROUND_HALF_UP`, clamp, and handoff to the single band mapping in §5.3.  
6. A decision on interaction with intrinsic scores and viewer preferences. Viewer preferences remain sampler/ranker inputs and do not alter intrinsic Magic-10 scores or bands.  
7. Pure-compute integration through the canonical Engine Core, with catalogs supplied as normalized input rather than loaded from files or environment at compute time.  
8. PF12 promotion treatment for schema, manifest, release identity, migration, and governed artifact ownership, followed by an authorized public-contract version change only if a preset becomes externally selectable or changes Reader output.

## **8.3 Promotion invariants**

Any promoted design must preserve these invariant-level requirements:

* **Closed identities and exact key closure.** Every detector output, feature, family, target, catalog row, and parameter resolves exactly once; unknown, missing, duplicate, or extra keys fail closed.  
* **Deterministic pure computation.** The result depends only on validated normalized inputs and governed frozen data. Time, network, locale, environment, randomness, and binary floating-point variability are prohibited.  
* **AB↔BA neutrality and two-run identity.** Pair normalization, set handling, reduction, tie-breaking, and iteration are order-independent; identical normalized inputs and governed data produce identical integer results on repeated runs.  
* **Fixed-point arithmetic.** Fractional operations use an explicitly governed integer or fixed-point recipe and `ROUND_HALF_UP`; final scores are clamped to `[0..100]` before the §5.3 handoff.  
* **One declared order and no hidden defaults.** Every stage, correction, floor, cap, rounding boundary, and tie-break is stated once. A missing value never enables a feature or supplies a magnitude.  
* **Atomic completeness.** A promoted layer either produces the complete governed result or fails closed. It must not return a partial matrix, a harmony-only substitute, or defaults for missing categories.

Changing a promoted fold, priority or shadowing rule, magnitude, sign, bonus, dampener, correction, distribution, floor, cap, application order, threshold, or other frozen math input is a math change and requires the governed release-identity and evidence treatment.

## **8.4 Ownership, handoff, and public boundary**

PF01 owns preset and aggregation mathematics if promoted. PF12 owns exact catalog paths, schemas, manifest membership, release-identity artifacts, and Evidence Catalog bindings. PF02 owns component wiring and the single-home boundary, not mathematical contracts.

Final category scores map to bands only through §5.3; this section does not define a second mapping or threshold table. Reader v1 remains numeric-free and emits only the `harmony` band as a projection from the complete canonical ten-category matrix. Promotion does not silently widen public output. Transport, HTTP, CLI stream, harness, and operational behavior remain in their owning documents.

# **9\. Validation**

**Scope.** This section defines the proofs required to accept PF01 math. Validation uses the active governed frozen inputs. Exact governed evidence-family names and physical paths are owned by the PF12 Evidence Catalog. No transport or HTTP proof lives here, and the presence of a checked-in definition or artifact does not establish that a check ran or passed.

## **9.1 Band edges (inclusive maxima)**

**Prove:**

* The single global inclusive-maxima rule in §5.3 maps every integer in `[0..100]` to exactly one band.  
* Equality falls to the lower band at each inclusive maximum.  
* `100` maps to `Glow`.  
* Cases cover each governed maximum, the next integer after each maximum, and `100`.

## **9.2 Rounding and clamping**

**Prove:**

* Rounding uses `round_half_up` at every pinned integerization stage.  
* The final clamp is `[0..100]`.  
* Cases cover midpoints and near-boundary values, including negative and above-maximum inputs where the owning formula admits them.

## **9.3 Electromagnetics (EM) extractor**

**Prove:**

* `channel_id` has the form `"<lowGate>-<highGate>"`, with gates zero-padded `01..64` and the lower gate first.  
* The `channels` array is ASCII-sorted by `channel_id` and contains unique entries.  
* AB and BA produce identical EM outputs after normalization.  
* Unmapped, malformed, or ambiguous inputs fail closed with typed errors.  
* Cases include at least one positive EM case with throat involvement, one negative case with no EM, and one fail-closed case.

## **9.4 Future-Promotion aggregation validation**

No current over-concentration factor, trigger, floor, cap, bonus, correction, or category-distribution recipe is governed. If the §8 Future-Promotion prerequisites are satisfied, validation must prove the complete promoted contract: exact key closure, one declared evaluation order, one application point for each correction, fully populated fixed-point values, `ROUND_HALF_UP` at each declared integerization boundary, `[0..100]` clamp, fail-closed unknown or missing inputs, and no hidden defaults. Boundary cases must exercise every declared stage and its disabled or inapplicable case.

## **9.5 Parity and two-run identity**

**Prove:**

* AB↔BA parity holds on the complete intrinsic ten-category scores and bands after pair normalization.  
* Two identical runs with the same normalized inputs and governed frozen data produce byte-identical internal results.  
* Reader/CLI public-byte parity is not proved here; the corresponding Reader-envelope requirement is governed in §10 and its owning interface canon.

### **Canonical Magic10 v1 goldens**

#### **M10-G001: no relationship Channels**

If all 36 Channel states are `none`:

* all twenty signal wire values are `0`;  
* all ten scores are `0`;  
* all ten bands are Cool.

#### **M10-G002: homogeneous companionship kernel fixture**

If every mapped state is `companionship`:

| Category | Score | Band |
| ----- | ----- | ----- |
| harmony | 100 | Glow |
| heat | 50 | Warm |
| communication | 75 | Glow |
| alignment | 100 | Glow |
| comfort | 100 | Glow |
| consistency | 100 | Glow |
| expansion | 50 | Warm |
| creativity | 63 | Warm |
| drive | 50 | Warm |
| balance | 50 | Warm |

Balance is `50` because `equilibrium_score` receives no one-owner mass while `counterweight_ratio` is `100`. This is a kernel fixture, not a claim that an all-Channel natal chart is lawful.

#### **M10-G003: Balance ownership split**

For the six equal-weight `equilibrium_score` Channels:

* three dominance or compromise Channels owned by `member_lo` and three owned by `member_hi` produce `q_equilibrium = 200`;  
* all six owned by one member produce `q_equilibrium = 0`;  
* swapping members cannot change either result.

#### **M10-G004: sparse end-to-end Gate sets**

Use:

* member A Gates: `{5,19,20,34,43,49}`;  
* member B Gates: `{9,12,15,22,23,52}`.

Expected Channel states:

* `05-15`: electromagnetic;  
* `09-52`: dominance by B;  
* `12-22`: dominance by B;  
* `19-49`: dominance by A;  
* `20-34`: dominance by A;  
* `23-43`: electromagnetic;  
* all other Channels: none.

Expected signal wire values:

| Signal | `q` half-score units |
| ----- | ----- |
| `rapport_delta` | 25 |
| `resonance_strength` | 63 |
| `spark_intensity` | 0 |
| `momentum_flux` | 38 |
| `signal_clarity` | 40 |
| `exchange_density` | 20 |
| `vector_cohesion` | 0 |
| `axis_agreement` | 25 |
| `soothe_index` | 50 |
| `buffer_resilience` | 38 |
| `pattern_integrity` | 50 |
| `variance_stability` | 0 |
| `growth_tendency` | 0 |
| `horizon_reach` | 0 |
| `novelty_factor` | 50 |
| `expression_flow` | 20 |
| `willpower_current` | 0 |
| `focus_pressure` | 60 |
| `equilibrium_score` | 0 |
| `counterweight_ratio` | 33 |

Expected category results:

| Category | Score | Band |
| ----- | ----- | ----- |
| harmony | 22 | Cool |
| heat | 10 | Cool |
| communication | 15 | Cool |
| alignment | 6 | Cool |
| comfort | 22 | Cool |
| consistency | 13 | Cool |
| expansion | 0 | Cool |
| creativity | 18 | Cool |
| drive | 15 | Cool |
| balance | 8 | Cool |

AB and BA must produce the same complete signal, score, and band vectors.

#### **M10-G005: identity independence**

Two eligible requests with identical normalized Gate masks and different user IDs must produce byte-identical intrinsic Magic10 content and the same `pair_key` under the same release. Pair IDs, request IDs, timestamps, and viewer preferences are excluded from the intrinsic preimage. This fixture does not assert that eligibility, directional narrative orientation, or public Reader bytes ignore identity.

#### **M10-G006: category boundary matrix**

At the category-reducer fixture layer, inject direct schema-valid `q` input pairs that produce integer scores `24`, `25`, `49`, `50`, `74`, `75`, and `100`. These pairs need not be reachable from Gate sets because this golden isolates reducer and band boundaries. Expected bands are respectively Cool, Open, Open, Warm, Warm, Glow, and Glow.

#### **M10-G007: valid self-pair boundary**

Use:

* `a_id = b_id = 00000000-0000-0000-0000-000000000001`;  
* both resolved normalized Gate sets are `{1}` and their complete normalized projections are byte-identical;  
* `release_id = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`;  
* `meta.engine_tag = m10-test`;  
* `meta.invocation_tag = m10-identity-boundary`.

Expected behavior:

* validation succeeds and `eligible == false`;  
* Engine Core, the intrinsic cache, and the narrative router are not called;  
* no `pair_key`, signal vector, category matrix, personal key, or shared key exists;  
* Reader categories are exactly `[]`;  
* canonical Reader preimage bytes hash to `8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15`;  
* two runs and the vacuous AB/BA reversal produce byte-identical Reader success bodies;  
* the condition is not converted into an error.

An internal same-UUID fixture with unequal complete normalized projections instead returns `ERR_READER_INVALID_CHART`, emits no success body, and creates no `pair_key`.

#### **M10-G008: distinct people with equal Gate masks**

Use:

* `a_id = 00000000-0000-0000-0000-000000000001`;  
* `b_id = 00000000-0000-0000-0000-000000000002`;  
* both normalized Gate sets are `{1}`;  
* the same `release_id` and `meta` values as M10-G007.

Expected intrinsic behavior:

* `eligible == true`;  
* `gate_mask_hex == 0000000000000001` for each member;  
* `chart_fingerprint == 7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b` for each member;  
* `pair_key == 8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501` under config `m10-channel-state-v1.0.0`;  
* every Channel state is `none`, every signal wire value is `0`, and every category score is `0` with band Cool.

Expected orientation and surface behavior:

* the first UUID is `lo` and the second is `hi` by the `(gate_mask, canonical_person_id)` tuple;  
* with a router stub returning `m10.test.personal.lo_to_hi`, `m10.test.personal.hi_to_lo`, and common shared key `m10.test.shared.equal_mask`, those values occupy `personal_lo_to_hi_key`, `personal_hi_to_lo_key`, and `shared_key` respectively;  
* reversing request order produces byte-identical `magic10_compat_result.v1` bytes and the same caller-to-key mapping;  
* Reader emits `eligible: true` and exactly `[{"id":"harmony","band":"Cool"}]`;  
* canonical Reader preimage bytes hash to `ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e`;  
* the Reader hash is independently computed and is not assigned from `pair_key`.

## **9.6 Pack closure and release identity**

**Prove:**

* Every identifier, table, formula input, topology row, and ordered set used by scoring and extractors resolves to the active governed frozen inputs.  
* Every required Magic-10 category is present exactly once in the frozen order; no extra or duplicate category is accepted.  
* Recomputed `sha256(canonical_manifest_bytes)` equals the recorded `release_id` under the owning manifest contract.  
* Missing, extra, duplicate, malformed, or unresolved governed inputs fail closed rather than producing a partial result or a default.

**Routing.** Public payload, serialization, emitter, transport, and CLI stream rules remain in their owning sections and documents. PF12 owns evidence paths and Evidence Index/Machine Mirror bindings.

# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]

## **10.1 Canonical serializer (UTF-8, sorted keys, compact, exactly one LF) \[Implemented\]**

**Purpose (normative).** Define the single JSON canonicalization used for the Reader body, the corresponding CLI Reader-envelope bytes, and the preimage used to compute `idempotence_hash` (§3.2). The serializer is BOM/ANSI-free, locale-neutral, and yields byte-identical output for identical logical inputs.

### **Canonical JSON rules**

* **Encoding:** UTF-8. No BOM.  
* **Key order:** `sort_keys = true` (lexicographic ASCII).  
* **Separators:** compact `','` and `':'` (no spaces).  
* **Escaping:** `ensure_ascii = false` (emit valid UTF-8 directly).  
* **Termination:** append exactly one trailing LF (`\n`) to the serialized document.  
* **No pretty print.** No indentation.  
* **No ANSI or non-JSON bytes.** No color codes, prompts, or trailing spaces.

### **Scope of use**

* **Success body:** serialize the five-key preimage without `idempotence_hash`, compute `sha256(preimage_bytes)`, then re-serialize the final six-key object (§3.2).  
* **Error body:** the same canonicalization rules apply to the typed error object, with one trailing LF.  
* **Arrays:** whenever arrays appear in public outputs, their order is deterministic and pinned by the owning contract before serialization.

### **Determinism properties**

* **Two-run identity:** canonicalizing the same logical object twice produces byte-identical bytes, including the single trailing LF.  
* **AB↔BA identity:** normalized inputs and deterministically ordered arrays and sets produce identical bytes for AB and BA (§3.4).  
* **Reader↔CLI parity requirement:** corresponding Reader-envelope bytes from both surfaces must be byte-equal for the same inputs; shared canonicalization alone does not establish logical-envelope or stream parity.  
* **Environment pins:** byte checks run with `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

### **Validation gates (binary)**

* **Encoding and termination:** output is UTF-8, BOM-free, and ends with one LF, neither zero nor two.  
* **Key order and separators:** local re-serialization with `sort_keys=true` and compact separators compares byte-equal; any mismatch is invalid.  
* **Preimage re-check:** remove `idempotence_hash`, re-serialize the preimage canonically, hash it, and reproduce the published digest (§3.2).

### **Hygiene requirements**

* **Single emitter only.** Public emission code must not use ad hoc `json.dumps` or alternate serializers; use the single canonical emitter (§10.2).  
* **Locale neutrality.** No locale-dependent collation, time, or formatting is permitted on the emission path.  
* **Numeric-free covenant.** The serializer emits what it receives; public success objects remain numeric-free except for identity fields already defined in §2.

**Routing note.** Transport and HTTP byte rules and CLI stream policy remain in **HDE-CLI-API-Vendor Ref**.

## **10.2 Unify emission entrypoint (CLI \+ Reader share the same emitter) \[Required-Now\]**

**Purpose (normative).** There is one public Reader-envelope emission entrypoint: the presenter emitter. The Reader Adapter and every designated CLI Reader-envelope surface must call this entrypoint. Normal compat/admin CLI stdout is not, merely by being stdout, the Reader envelope. No public surface may hand-craft JSON or call an ad hoc serializer. The unified emitter applies §10.1 canonicalization and the §3.2 preimage recipe.

### **10.2.1 Unified entrypoint (contract)**

* **Single emitter path.** Public Reader-envelope bytes must be produced by the presenter's canonical emission function.  
* **Caller responsibilities.** A Reader or CLI Reader-envelope caller must:  
  1. prepare the success preimage with the five keys defined in §3.2;  
  2. pass it to the unified emitter and receive LF-terminated canonical bytes; and  
  3. not mutate, re-encode, or re-serialize the returned bytes.  
* **Error bodies.** Typed public error objects use the same canonical public emitter and LF discipline, subject to the public shape constraints in §2.

### **10.2.2 Disallowed patterns (hard fail)**

* **No local serializers.** Module-local canonicalizers are forbidden on public emission paths.  
* **No ad hoc `json.dumps`.** Any direct `json.dumps(` on a public emission path is invalid, including “format then add LF.”  
* **No alternate emitters.** Do not duplicate the preimage recipe or `idempotence_hash` logic outside the unified Reader-envelope emitter.  
* **No test-only bypass.** Tests must not bypass the unified entrypoint.

### **10.2.3 Required refactor (action items)**

* **Route all Reader-envelope call sites.** Reader handlers and designated CLI Reader-envelope output must call the presenter emitter through the governed runtime path.  
* **Delete public-path duplicates.** Remove local public canonicalizers, hand-built Reader envelopes, and duplicate preimage or hash logic.  
* **Unify tests.** Reader and CLI Reader-envelope tests call the same emitter function without test shims.  
* **Grep-guard in CI.** Fail on public paths that contain:  
  * `\bjson\.dumps\(`;  
  * alternate emitter names not on the allowlist; or  
  * more than one canonicalizer symbol in a public module.

### **10.2.4 Acceptance and validation (binary)**

* **Reader↔CLI parity.** For identical inputs and environment, the Reader response body and corresponding CLI Reader-envelope bytes are byte-identical. Compat/admin stdout is a different surface and is not substituted for this proof.  
* **Idempotence re-check.** Remove `idempotence_hash`, re-serialize the preimage with the unified emitter, hash it, and reproduce the published digest (§3.2).  
* **LF discipline.** Both Reader-envelope surfaces produce exactly one trailing LF and no BOM or ANSI bytes.  
* **AB↔BA parity and two-run identity.** Public Reader-envelope bytes are bit-identical for AB versus BA and across two runs (§3).  
* **No extras.** Success bodies contain exactly the six keys; `categories[*]` are `{id,band}` only (§2).  
* **Pins and evidence.** Run byte checks with `LC_ALL=C`, `LANG=C`, and `TZ=UTC`. Register governed parity and idempotence evidence through the PF12 Evidence Catalog; path presence alone does not establish PASS.

### **10.2.5 Migration checklist (one-time)**

1. **Inventory.** Locate every Reader-envelope emission call site, including Reader handlers, designated CLI surfaces, legacy scripts, and test helpers.  
2. **Refactor.** Route each valid call site through the presenter emitter and remove local public serializers.  
3. **Purge.** Remove obsolete public helpers, hand-built envelopes, duplicate preimage logic, and direct `json.dumps` on public paths.  
4. **Re-run evidence.** Regenerate governed parity, idempotence, LF, schema, AB↔BA, and two-run evidence; update its PF12-governed bindings in the same change.  
5. **Enable grep-guard.** Add CI checks that prevent regression.

### **10.2.6 Non-goals and routing**

This section does not restate HTTP transport, conditional delivery, caching, or generic CLI stream policy. Those rules remain in **HDE-CLI-API-Vendor Ref**. Public output remains bound by the numeric-free covenant in §2. Acceptance-token semantics remain in their governance owner; PF12 owns evidence-family and path bindings.

## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**

**Purpose (normative).** Define the binary checks that must prove public bytes are serialized by the canonical emitter (§10.1), corresponding Reader and CLI Reader-envelope surfaces use the single entrypoint (§10.2), and the preimage recipe (§3.2) is applied correctly. This heading states a requirement; it does not claim that current repository evidence has passed.

### **10.3.1 Acceptance gates (must all pass)**

* **Canonical encoding.** Bytes are UTF-8, BOM/ANSI-free, use sorted keys and compact separators, and end with exactly one LF (`\n`).  
* **Six-key success.** Success bodies contain exactly the six top-level keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`) and no extras (§2.1).  
* **Public shape.** `categories[*]` are exactly `{id, band}` with `band ∈ {Cool,Open,Warm,Glow}`; no `prompt`, `personal_key`, `shared_key`, `score`, or other field is permitted (§§2.1–2.2).  
* **Preimage re-check.** Removing `idempotence_hash`, re-serializing the five-key preimage with the canonical emitter, and hashing reproduces the published digest (§3.2).  
* **Parity and identity:**  
  * corresponding Reader and CLI Reader-envelope bytes are identical for identical inputs and environment;  
  * AB and BA bytes are bit-identical after pair normalization; and  
  * two serializations with the same inputs are byte-identical (§3.4).

### **10.3.2 Governed evidence families**

Maintain reproducible, private-data-free proof for canonical schema and LF discipline, public AB↔BA goldens, idempotence coupling, single-emitter call-path inspection, corresponding Reader/CLI Reader-envelope parity, and two-run identity. PF12 is the single home for exact artifact-family names, physical paths, Human Index rows, Machine Mirror records, hashes, sizes, and path proofs; this section does not maintain a parallel path list.

The pinned repository contains serializer, presenter, schema, test, golden, script, and identity-related files, but the inspected bytes do not establish complete current acceptance: the named CLI schema/LF test is absent, the Reader goldens retain retired fields, the schema and presenter still permit `prompt`, and the checked-in identity marker is a historical or construction-time record rather than proof that the final required validation ran and passed.

### **10.3.3 CI hygiene (fail-fast)**

* **Grep-guards:** forbid ad hoc `json.dumps(` and local public canonicalizers; allow only the governed presenter emitter and its canonical serializer dependency.  
* **Single-LF check:** assert exactly one trailing LF on success and error bodies.  
* **Schema and shape:** validate the six-key success object, `{id,band}` items only, closed IDs and enums, and the prohibited-field set.  
* **Parity and identity:** compare AB/BA and two-run bytes and compare corresponding Reader and CLI Reader-envelope bytes.

### **10.3.4 Failure posture (binary)**

If any applicable gate fails—schema, shape, LF, preimage hash, parity, identity, or CI hygiene—the emission is invalid and must not be published. Transport failure behavior is not duplicated here and remains in **HDE-CLI-API-Vendor Ref**.

### **10.3.5 Determinism notes**

Evidence must demonstrate that the same governed Reader-envelope emitter produced both compared surfaces, that sorted keys, compact separators, and one LF are present, and that the preimage hash couples to the final bytes. All proofs are order-neutral and re-runnable. Static definitions and checked-in artifacts do not, by themselves, prove runtime success or test passage.

# **11\. Evidence**

**Scope.** Math-only evidence proves §9 Validation. Transport, HTTP, headers, caching, and generic CLI stream evidence do not live here. PF12's Evidence Catalog is the single home for exact governed artifact-family names, paths, record shapes, Human Index entries, Machine Mirror records, hashes, sizes, and path proofs. This section retains the local proof obligations without creating a parallel physical-path inventory.

JSON evidence governed for these proof families must use the canonical byte rules required by its owner. Evidence is generated from the applicable governed frozen inputs and a controlled harness. A file definition or checked-in artifact establishes only static bytes; it does not establish that generation, validation, or acceptance succeeded.

## **11.1 Band edges**

The band-edge proof family must cover the single global mapping in §5.3. It must include every inclusive maximum, the next integer after each maximum, and `100`, with the expected unique band. If a future preset-specific threshold table is promoted, it requires its own governed contract and evidence; no active preset-specific maxima are inferred here.

## **11.2 Rounding and clamping**

The rounding proof family must include `round_half_up` midpoint cases and clamp cases for `[0..100]`, with worked examples at every integerization boundary used by current PF01 math. Binary-float or away-from-zero behavior is not accepted as a substitute.

## **11.3 Electromagnetics (EM) extractor**

The EM proof family must include the active topology identity, at least one positive EM case with throat involvement, at least one negative case, and at least one fail-closed case. It must assert that:

* `channel_id` is `"NN-NN"`, with zero-padded gates `01..64` and the lower gate first;  
* `channels` is ASCII-sorted and duplicate-free; and  
* AB and BA outputs are identical after normalization.

## **11.4 Future-Promotion aggregation**

No current evidence claim is made for an over-concentration factor, trigger, bonus, correction, floor, cap, or distribution recipe because no such current governed aggregation contract exists. If §8 is promoted, its proof family must cover every populated stage, disabled case, boundary, precedence rule, integerization point, `ROUND_HALF_UP` operation, clamp, fail-closed condition, AB↔BA comparison, and two-run comparison. It must also prove that each stage is applied at exactly its declared point and never through an implicit default or loop.

## **11.5 Parity and two-run identity**

The math parity proof family must demonstrate byte-identical complete intrinsic ten-category scores and bands for AB versus BA after normalization and for two identical runs using the same governed inputs. Public Reader/CLI Reader-envelope parity remains a §10 and interface-owner proof; it is not substituted for complete internal-matrix parity.

## **11.6 Pack closure and release identity**

**Current release-bound requirement.** Current release provenance must bind the exact source commit, deterministic tracked-tree digest, canonical manifest and `release_id`, ASCII-sorted file inventory with hashes and sizes, and canonical checksums without introducing a cyclic identity dependency. Any external attestation remains outside tracked source and must not be used to regenerate tracked release derivatives or evidence indexes.

**Historical checked-in records.** Freeze-pack manifest copies, recorded release IDs, recomputation traces, checksum audits, and identity markers captured in tracked source remain historical records at their capture state. Their presence is not current release attestation, current validation, or proof of PASS. Do not regenerate, relabel, or refresh them merely because the current manifest or `release_id` changes.

**Must prove.** The canonical manifest has the exact required structure and bytes; its `files[]` entries are ASCII-sorted and unique; recorded hashes and sizes match their governed bytes; recomputation yields the manifest-derived `release_id`; and current provenance preserves the acyclic dependency from tracked source through the manifest and `release_id` to any external attestation. Exact evidence paths and bindings remain in PF12.

# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**

These pointers describe static repository state at the pinned validation snapshot. Normative rules remain in §§2–10. Static inspection does not establish runtime reachability, test passage, deployment, or acceptance.

* **Legacy public wrapper:** `engine/emit_public.py`  
    
  * Retained for harnesses; delegates to `engine.runtime.emit_reader_public_bytes` and contains no local serializer.


* **Current Reader runtime:** `engine/runtime/public.py`  
    
  * Builds the current single-`harmony` Reader envelope, computes that band separately through `engine/compat/ts_v0.py`, and calls `presenter/reader_v1/emitter.py`.  
  * The function defaults an externally supplied `eligible` value to true and constructs a `harmony` category even when `eligible` is false. Those bytes do not satisfy the complete eligibility and empty-category requirements merely because they are serializable.


* **Presenter and serializer chain:** `presenter/reader_v1/emitter.py` → `engine/presenter/emitter.py` → `engine/serializer/canon.py` → `engine/stable/sercanon.py`  
    
  * The chain constructs the canonical preimage, computes `sha256`, and emits the final LF-terminated object.  
  * `presenter/reader_v1/emitter.py` still carries through optional `prompt`; remove that carry-through so `categories[*]` are exactly `{id, band}` (§§2.1–2.2).


* **Ten-category compat internals:** `engine/compat/{compute,categories,thresholds,ordering}.py`  
    
  * This is a separate internal/admin hash-and-binary-float scoring path; it is not the source of the current public Reader `harmony` band and does not implement the canonical §5 Human Design-grounded matrix.  
  * `engine/compat/categories.py` maintains a heat-first order that differs from the harmony-first frozen order in `catalog/magic10.json`. Ordered consumers must use the governed order.  
  * Reader v1 still emits only the `harmony` projection; full public Magic-10 exposure requires an authorized versioned contract (§2.2).


* **Viewer preferences:** `engine/validation/viewer_prefs.py`  
    
  * It checks the exact Magic-10 key set and nominal integer range `0..100`, but Python booleans satisfy its current `isinstance(value, int)` test. The validator must reject booleans and other non-integer weights under the owning PF12 contract.  
  * Viewer preferences remain sampler/ranker inputs and must not alter intrinsic compatibility scores or bands.


* **Dev Reader harness:** `dev/reader_harness/app.py`  
    
  * Mounts the Reader blueprint under `/api`; the direct `adapter/http_reader.py` launch mounts the same blueprint at the root.  
  * The strict `APP_ENV=dev` refusal remains a requirement. A default that treats an unset environment as development is not fail-closed.  
  * Harness presence does not prove Reader/CLI byte parity or transport acceptance.


* **Public success schema:** `schemas/reader.v1.schema.json`  
    
  * The inspected schema permits optional `category.prompt` and lists legacy `*_leader` category IDs rather than the current `harmony` ID. Align it to the exact six-key success covenant and `{id,band}` item contract in §§2.1–2.2.  
  * Typed errors remain governed by §2.3 and use the canonical single-LF emitter.


* **CLI surfaces:** `engine/cli/main.py` and `scripts/hd_cli.py`  
    
  * `engine/cli/main.py` writes compat/admin bytes to ordinary stdout and produces corresponding Reader-envelope bytes only through its reader-dump surface. Parity claims must compare the Reader body with that corresponding Reader-envelope output, not with unrelated compat stdout.  
  * `scripts/hd_cli.py` hand-builds a legacy Reader-like envelope and bypasses the unified Reader-envelope path. Inventory and retire or route that alternate path under §10.2.


* **Evidence posture:**  
    
  * The expected CLI schema/LF test path is not present in the inspected repository. Existing Reader goldens contain retired fields, and the checked-in identity marker records a deterministic predicate rather than complete final validation.  
  * Scripts, tests, schemas, goldens, logs, and identity files establish only their checked-in contents. PF12 governs exact evidence-family and path bindings; executed PASS evidence is separate.


* **CI hygiene (required validation):**  
    
  * Grep-guard public paths against direct `json.dumps(`, hand-built Reader envelopes, and multiple public canonicalizers; allow only the governed presenter-emitter chain (§10.2).  
  * Validate AB↔BA bytes, two-run identity, single-LF discipline, schema and shape, frozen category order, idempotence coupling, and corresponding Reader/CLI Reader-envelope parity (§§3.4, 9, 10.3).

Transport, HTTP, conditional delivery, caching, writer behavior, and generic CLI stream policy are not restated here; they remain in their owning interface and governance documents.

# **Appendix A — Determinism & Ordering (reference) \[Required-Now\]**

## **A.1 Canonical comparators**

* **Key ordering (JSON objects).** Keys are serialized with **ASCII lexicographic** order (`sort_keys=true`). No locale-aware or natural (“1\<10”) sorts.  
    
* **String ordering (general).** When a comparator is needed (e.g., for array stabilization), use **byte-wise ASCII ascending** on the UTF-8 bytes of the string.  
    
* **Tuple/list ordering.** Compare element-wise under the same ASCII rules; the **shorter tuple is smaller** when all shared positions are equal.  
    
* **Category ordering.** When category arrays exist, sort by the frozen Magic-10 order defined in **PF12-Canon-HDE-Schemas-and-Artifacts**, then by `id` (ASCII ascending) as a deterministic tie-break.  
    
* **Stable tie-breaks (fail-closed on collision).** If two items share the same primary key, use a **secondary, deterministic** key (e.g., `id` then `band`) to avoid comparator drift. **If a collision remains after tie-break, treat it as a construction error (fail-closed); do not drop a duplicate arbitrarily.** (Aligns with §2.2 public `categories` rules and Appendix A.2 set-normalization.)

## **A.2 Set normalization**

* **Pair normalization (AB↔BA).** Before any computation, derive a **pair key** and reorder inputs to a canonical **(min, max)** by the **ASCII comparator**. All downstream math **MUST** consume the **normalized pair** only.  
    
* **Array → set semantics.** When an array represents a set (e.g., unique **category `id`s**, token IDs, channel IDs), **deduplicate by identity key**, then **sort deterministically (ASCII)** before use/serialization.  
    
* **Deterministic fold.** If the same token/ID appears more than once, apply the **commutative, associative fold** declared in the catalog (e.g., **max**, bounded sum) so evaluation order **cannot** affect the outcome.  
    
* **Fail-closed on conflict.** If two entries collide on an identity key but **disagree on value** (e.g., two different `band` values for the same `id`), treat this as a **construction error**—**do not** pick arbitrarily or drop a duplicate. (Aligns with §2.2 public `categories` rules.)

## **A.3 Locale pins**

* **Collation & formatting.** All comparisons and serializations are **locale-neutral**; treat strings as raw UTF-8 bytes for ordering.  
    
* **Numeric handling.** All arithmetic is **fixed-point integer** with **round half-up** where specified; never rely on float/locale formatting.  
    
* **Environment independence.** No dependence on process locale, timezone, or wall-clock. Results must be identical across environments and runs.

## **A.4 Two-run identity harness**

* **Goal.** Prove that **two serializations** of the same logical success envelope yield **byte-identical** output (including the single trailing LF), and that **AB** vs **BA** inputs produce byte-identical bytes.  
    
* **Harness recipe (success case).**  
    
  1. **Build preimage** with the five keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`).  
       
  2. **Canonicalize** (UTF-8, sorted keys, compact, **exactly one LF**).  
       
  3. **Hash** `sha256(preimage_bytes)` → `idempotence_hash` (lowercase 64-hex).  
       
  4. **Finalize**: add `idempotence_hash`, **re-serialize** canonically (one LF).  
       
  5. **AB↔BA check**: normalize `(A,B)` and `(B,A)`; run 1–4; **byte-compare** bodies (must match).  
       
  6. **Two-run check**: run 1–4 twice with identical inputs; **byte-compare** (must match).  
       
  7. **Recompute check**: remove `idempotence_hash` from the final body, re-serialize the five-key preimage canonically, `sha256` must equal the published hash.


* **CI hooks.** Add byte-compare jobs for AB/BA and two-run; single-LF and schema gates; block any ad-hoc `json.dumps` or non-presenter emitters on public paths.

# Appendix B — Evidence Index (titles/paths only) \[Required-Now\]

PF01 retains math proof-family names and local proof obligations only. The complete Evidence Catalog—including physical paths, Human Index and Machine Mirror records, hashes, sizes, and path proofs—is governed by **PF12-Canon-HDE-Schemas-and-Artifacts §§8.3 and 8.6**. This appendix does not maintain a parallel physical-path list.

**B.1 Parity (Reader↔CLI, AB↔BA)**

* PF01-owned complete-matrix AB↔BA parity and two-run identity are specified in §§9.5 and 11.5.  
* Reader↔CLI parity and its dev-harness proof surface are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §§5.4 and 10.3**.

**B.2 Newline & encoding discipline (LF; UTF-8; no BOM/ANSI)**

Canonical artifact bytes and their evidence bindings are governed by **PF12-Canon-HDE-Schemas-and-Artifacts**. Reader and CLI wire-byte requirements are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref**.

**B.3 Idempotence coupling (preimage → sha256 → final)**

PF01’s preimage and mathematical identity obligations are specified in §§3.2, 9.5, 10.3, and 11.5. Exact evidence records and paths are governed by the **PF12-Canon-HDE-Schemas-and-Artifacts** Evidence Catalog.

**B.4 Schema conformance (public success & errors)**

Public Reader and CLI schemas, validators, and wire-byte proofs are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref**. Their Evidence Catalog bindings are governed by **PF12-Canon-HDE-Schemas-and-Artifacts**.

**B.5 Identity evidence**

PF01’s pack-closure and release-identity proof obligations are specified in §§9.6 and 11.6. Manifest identity, artifact schemas, physical evidence paths, and index records are governed by **PF12-Canon-HDE-Schemas-and-Artifacts**; operational service identity is governed by **PF04-Canon-HDE-Governance**.

**Maintenance note.** Evidence-path and index maintenance is governed by **PF12-Canon-HDE-Schemas-and-Artifacts**. PF01 does not duplicate that catalog or its update procedure.

# **Appendix C — Dev Harness (Reader v1) \[Informative\]**

## **C.1 Purpose**

The complete dev Reader harness purpose and contract are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §§5.4 and 10.3**. PF01 defines no independent harness contract.

## **C.2 Gating & safety**

Dev-harness routing, environment gating, local-only containment, closed-rails posture, fixture use, and privacy requirements are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §§5.4 and 10.3** and **PF04-Canon-HDE-Governance §2.0**.

## **C.3 Parity with CLI (procedure)**

The Reader↔CLI parity procedure and corresponding dev-harness proof surface are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §5.4**. PF01’s mathematical AB↔BA and two-run obligations remain in §§9.5 and 11.5.

## C.4 Evidence produced (titles/paths only)

Proof-family and physical-path bindings are governed by the Evidence Catalog in **PF12-Canon-HDE-Schemas-and-Artifacts §§8.3 and 8.6**. PF01 does not maintain a second evidence inventory.

## **C.5 Operational constraints**

Harness emission, wire-byte, stream, schema, and public-envelope constraints are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §§5.4, 6, and 10.3**. Canonical artifact serialization is governed by **PF12-Canon-HDE-Schemas-and-Artifacts**.

## **C.6 Transport pointers (titles-only)**

Consult **PF05-Canon-HDE-CLI-API-Vendor-Ref** for CLI and Reader transport bytes and validators, and **PF04-Canon-HDE-Governance** for A7 transport acceptance and rails policy.

## **C.7 Non-goals**

The dev-harness architecture and non-goals are governed by **PF02-Canon-HDE-Architecture §3.3**. Harness transport and public-byte boundaries are governed by **PF05-Canon-HDE-CLI-API-Vendor-Ref §§5.4 and 10.3**, and schema/versioning change policy is governed by its §0.4. No separate persistence, production-routing, public-numeric, or schema-evolution contract is created here.

# **Appendix D — Retired Features (removed) \[Normative Notice\]**

## **D.1 Prompt**

The complete `prompt` retirement status, scope, administrative-surface rule, rationale, and effective-date record are governed by **PF04-Canon-HDE-Governance §14.1**. PF01 defines no separate retired-feature policy.

## **D.2 Uncertainty**

The complete uncertainty retirement status, scope, rationale, effective-date record, and operational-impact posture are governed by **PF04-Canon-HDE-Governance §14.2**. PF01 defines no separate retired-feature policy.

# **Appendix E — Composite fingerprint v1 (fixtures spec) \[Required-Now\]**

**Purpose (normative).** Provide a minimum-information, canonical, order-independent JSON artifact that witnesses composite determinism for CI and parity checks. This artifact is **not** a public API and **must not** include PII or narrative content. Serialization follows **PF12-Canon-HDE-Schemas-and-Artifacts §4**.

**Static implementation posture.** This four-key artifact remains a normative requirement with an implementation gap. At the pinned commit, `engine/compat/type_strategy_v0.py::compute_fingerprint` computes a gate-list digest rather than this shape, and the inspected Reader schema and runtime loci do not define a matching producer or schema.

## **E.1 Shape (keys, domains, ordering)**

The fingerprint object has **exactly four keys**, emitted in **ASCII key order**:

```json
{
  "centers_defined": ["ajna", "g", "root"],
  "channels_defined": ["07-31", "10-20", "29-46"],
  "channels_em": ["10-20"],
  "throat_em": true
}
```

**Domains & constraints (normative)**

* **centers\_defined** — Array of distinct center ids (strings), each in the closed set `{"head","ajna","throat","g","ego","spleen","sacral","solar_plexus","root"}`; ASCII-sorted.  
* **channels\_defined** — Array of distinct channel ids in canonical `NN-NN` form (two zero-padded gate ids, min-first), ASCII-sorted. Each element **MUST** match `^(?:0[1-9]|[1-5][0-9]|6[0-4])\-(?:0[1-9]|[1-5][0-9]|6[0-4])$` and be present in the Channel Catalog.  
* **channels\_em** — ASCII-sorted, duplicate-free subset of `channels_defined`. Each listed channel is completed by exclusive opposite endpoint ownership across the two normalized people. Same-person full, dominance, compromise, and companionship channels are excluded.  
* **throat\_em** — Boolean; `true` iff any `channels_em` element is incident to **throat**.

## **E.2 Construction procedure (success case)**

1. **Normalize inputs** `(A,B)` under **PF12-Canon-HDE-Schemas-and-Artifacts §2.1** ingestion rules; build the AB composite over `catalog/gates_v1.json` and `catalog/channels_v1.json`, deriving centers from Gate rows and using canonical `NN-NN` identities.  
2. **Derive sets from the composite (no partial inference):**  
   * `channels_defined` \= all catalog channels whose **both** gate endpoints are present.  
   * `centers_defined` \= all centers incident to `channels_defined`.  
   * `channels_em` \= the channels in `channels_defined` completed by exclusive opposite endpoint ownership across the two normalized people; exclude same-person full, dominance, compromise, and companionship channels.  
   * `throat_em` \= `true` iff any `channels_em` touches **throat**.  
3. **Canonicalize.** ASCII-sort each array; dedupe exact duplicates; emit the four keys in ASCII key order; serialize canonically under **PF12-Canon-HDE-Schemas-and-Artifacts §4** with one trailing LF.

## **E.3 Validation (binary)**

* **Keys:** exactly `{"centers_defined","channels_defined","channels_em","throat_em"}` (no extras).  
* **Arrays:** ASCII-sorted; no duplicates.  
* **Domains:** `channels_defined` entries match the `NN-NN` regex above; `centers_defined` entries are in the closed center set; `channels_em ⊆ channels_defined`.  
* **AB↔BA:** Fingerprints for `(A,B)` and `(B,A)` are **byte-identical** (after canonical serialization).  
* **Two-run identity:** Two runs on the same inputs/pack produce **byte-identical** fingerprints (checks with `LC_ALL=C`, `LANG=C`, `TZ=UTC`).

## **E.4 Change control**

The fingerprint’s keys, domains, and canonicalization rules are **frozen** for v1 CI. A shape, domain, or ordering change is a PF01 test-format change. **PF12-Canon-HDE-Schemas-and-Artifacts** owns schema, manifest, release-identity, physical-path, and Evidence Catalog treatment; acceptance-token semantics remain in **PF04-Canon-HDE-Governance**.

**Acceptance & CI (titles-only).**

* `COMPOSITE_ABBA_IDENTITY_OK` — AB/BA fingerprints are byte-identical.  
* `TOPOLOGY_COHERENCE_OK` / `XREF_MEMBERSHIP_OK` — `NN-NN` validity; center/channel closure.  
* `JSON_CANONICAL_CHECK_OK` — canonical JSON (UTF-8, sorted keys, deduped ASCII arrays, one LF).  
* `TWO_RUN_IDENTITY_OK` — repeatability on same inputs/pack.  
* `EVIDENCE_INDEX_UPDATED_OK` — fingerprint evidence is bound through the **PF12-Canon-HDE-Schemas-and-Artifacts** Evidence Catalog.

**Routing.** The fingerprint is **not** part of the Reader contract. Transport behavior is owned by **PF05-Canon-HDE-CLI-API-Vendor-Ref** and **PF04-Canon-HDE-Governance**. Evidence paths and index records are owned by **PF12-Canon-HDE-Schemas-and-Artifacts**.