# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF01-Canon-HDE-Math-Spec

**Version:** v1.2.9

**Status:** Canon

**Effective date:** 2025-12-03

**Last Update Gate:** 2025-12-03 Audit

## **0.2 Change policy**

**Contract surface.** This spec is math-only. It does not define transport bytes, HTTP behavior, or operational policy. Those are referenced by title only:

* **HDE-CLI-API-Vendor-Ref:** CLI/Reader/vendor payloads, validators, header matrices, streams, and exit codes.  
* **HDE-Governance:** A7 transport, conditional delivery, caching and writers, SAFE rails, rate-limit and timeout acceptance. No duplicated bytes: if transport, ops, or policy details appear here, remove them and route by title to the owning document.

**Single-source math.** All normative math (algorithms, feature shapes, score formation) lives here. Any repository paths shown in examples are informative, never authoritative.

**Frozen inputs and release identity (HDE-Schemas & Artifacts §§2, 4, 5-6).** This spec is realized by frozen inputs enumerated in the pack manifest (`catalog/manifest.json`). The frozen surface includes at least:

* **Constants pack** (see §5.4.2): `limits.em_max`, `limits.throat_em_max`, `limits.centers_max`, `limits.motor_throat_max`, `limits.mind_throat_max`, `limits.comp_max`, and `bands.thresholds` (inclusive-high maxima).  
* **Direct Motor→Throat set** (if catalogized in **HDE-Schemas & Artifacts**): governed four-channel set in canonical NN-NN; any change is frozen-input and bumps `release_id`.  
* **Magic-10 catalog** (**HDE-Schemas & Artifacts** §2.6): closed, ordered ID set; pinned order is the single home there (this spec references by title). *(Thresholds remain in the constants pack.)*  
* **Topology catalogs** (**HDE-Schemas & Artifacts** §2.1): `centers.json`, `gates.json`, `channels.json` (canonical NN-NN channel identities; centers in `snake_case`).  
* **Seeds catalog** (when present): if Seeds are catalogized in **HDE-Schemas & Artifacts**, they are admin/test inputs and become frozen inputs that trigger a new `release_id` on change; Seeds are not public in v1.

**Frozen-input change ⇒ new `release_id`.** Any byte change to a frozen input or the manifest requires a Doc-Delta and a new `release_id` (**HDE-Schemas & Artifacts** §6: `release_id = sha256(canonical_bytes("catalog/manifest.json"))`).

**Canonical bytes** (**HDE-Schemas & Artifacts** §4). All governed JSON (including the manifest and any constants or catalog files) is serialized as UTF-8 without BOM, sorted keys, compact, with exactly one trailing LF; numbers are JSON numbers; arrays used as sets are deduplicated and ASCII-sorted. Hashing, parity, and equality checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. This spec references those rules and does not restate them.

**EPIC017 proof posture (informative).**  
 EPIC017, as recorded in **HDE Phased Epics Map**, is the first epic that fully proves the canonical-bytes and determinism rules defined in this spec. Its deliverables exercise:

* canonical JSON (UTF-8, sorted keys, compact, one trailing LF)

* arrays-as-sets (deduped and ASCII-sorted)

* the `LC_ALL=C` / `LANG=C` / `TZ=UTC` posture for hashing and canonicalization

* determinism evidence (AB↔BA identity, two-run identity, idempotence recompute)

These proofs are implemented through tests and evidence artifacts owned by **HDE-Mechanics Guide** and **HDE-Build Checklist**. EPIC017 does **not** modify any math or canonical JSON semantics in this spec; it brings implementation and evidence into full alignment with the existing contract.

**Identifier and path policy** (**HDE-Schemas & Artifacts** §0.5 / §2.1). String IDs are ASCII and match `^[a-z0-9_]+$` (case-sensitive). Pack paths are POSIX (no `..`, no `//`, max 256 bytes). Centers are `snake_case` in outputs; Title Case is an ingestion alias.

**Process scope.** Build and CI flow, CodEx staging, and repo-docs updates live in **HDE-Build Notes** and **Epic-Process-Guide**. This spec remains contract-free for transport/ops and uses titles-only routing to those homes.

**Acceptance and evidence coupling** (**HDE-Schemas & Artifacts** §8; **HDE-Governance** A-gates). Any change that touches frozen inputs or schema/identity must ship with CI tokens and Evidence Index updates, including as applicable:

* **Pack/manifest and mirror:** `RELEASE_ID_RECOMPUTE_OK`, `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`. The machine mirror lives at `artifacts/evidence_index.jsonl` and must be kept 1:1 with the human Evidence Index in **HDE-Governance** (records-only with path-proofs).  
* **Domains/catalogs:** `MAGIC10_DOMAIN_CLOSED_OK`, `M10_DEFS_OK`, `M10_SEEDS_OK` (when Seeds are catalogized), `CATALOG_ORIENTATION_CANON_OK`, `PREFS_KEYSET_10_OK`.  
* **Bands and rounding:** `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `ROUND_HALF_UP_OK`.  
* **Determinism:** `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.

**Token semantics.** Token semantics live in **HDE-Governance §2.0**; this document references token names only.

---

## 

## **0.3 Tagging convention (used throughout)**

* **\[Implemented\]** — Verified in the repo and exercised by surfaces/tests.

* **\[Required-Now\]** — Required for current build goals; if missing in code, it is treated as a gap.

* **\[Speculative\]** — Accepted future design; not yet wired. (Preserve math as-is; no public bytes until promoted.)

# **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**

* **Public Reader v1 (bands-only, single “harmony”) — \[Implemented\] (with CLI parity target)**

  * **What’s live.** The public envelope emits one category `{"id":"harmony","band": <Cool|Open|Warm|Glow>}` plus `eligible`, `meta:{engine_tag,invocation_tag}`, `release_id`, and `idempotence_hash`. Bytes are canonical JSON (UTF-8, sorted keys, compact, exactly one trailing `\n`). `idempotence_hash` is computed over the canonical preimage; **AB↔BA** and **two-run** identity hold (see §3.2 and §3.4).  
  * **Where it’s proved (titles-only).** • Reader v1 emitter & canonical serializer (public envelope rules) • Reader↔CLI parity harness (byte equality for identical inputs) • Idempotence/preimage recompute (preimage → hash → final).  
     All artifacts are indexed via the machine mirror at `artifacts/evidence_index.jsonl`; titles appear in **Appendix D: Evidence Index**.  
  * **Scope note.** Transport/CLI specifics (headers, 304/HEAD, validators) live in **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles-only).  
* **Determinism (LF, sorted keys, preimage hash, AB↔BA) — \[Implemented\]**

  * **Canonical JSON, one LF.** Public bytes are emitted as UTF-8, sorted keys, compact separators, exactly one trailing `\n` (see **HDE-Schemas and Artifacts §4**; enforced by emitter and tests).  
  * **Two-step idempotence.** Build the preimage (without `idempotence_hash`), compute `sha256(preimage_bytes)`, then re-emit with `idempotence_hash` inserted (see §3.2).  
  * **AB↔BA identity.** Pair inputs are normalized to a canonical order; the same pair key drives downstream math so AB and BA produce byte-identical outputs (see §3.4).  
  * **Evidence (titles-only).** Reader/CLI schema & LF discipline, AB↔BA goldens, idempotence recompute logs; all entries mirrored 1:1 in the machine mirror.  
  * **EPIC017 proof record (informative).**  
     EPIC017, as tracked in **HDE Phased Epics Map**, is the first complete implementation of the determinism invariants defined in this spec. Its deliverables exercise:

    * canonical JSON checks

    * Reader↔CLI parity

    * AB↔BA identity

    * two-run identity

    * idempotence-recompute harnesses

  * Acceptance tokens such as `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, and `COMPOSITE_ABBA_IDENTITY_OK` are mapped to evidence artifacts owned by **HDE-Mechanics Guide** and **HDE-Build Checklist**. These proofs demonstrate that implementation conforms to the rules defined here; they do **not** introduce any new math or any alternative determinism contract.

* **Compat Magic-10 (10 categories; scores→bands) — \[Speculative\] (internal math present; not public)**

  * **Closed set & order.** Magic-10 IDs and their pinned order are defined in **HDE-Schemas and Artifacts §2.6** (this spec is math-only; public exposure is constrained in §2.2).  
  * **Viewer prefs (shape & bounds).** Inputs validate against a closed 10-key weight map (0..100 integers) and a `top_category ∈ Magic-10`; deviations yield typed invalid-prefs (titles-only).  
  * **AB↔BA neutrality.** Pair normalization yields order-neutral inputs; a stable pair key drives deterministic internal scoring.  
  * **Deterministic scoring & banding.** Per-category scores are integers 0..100 by pinned arithmetic; bands map via inclusive maxima 24/49/74/100 with round\_half\_up (see §2.2 \+ §5.3).  
  * **Internal result shape (not public).** Internal outputs may include `{id, score, band, personal_key, shared_key}`; Reader v1 exposes only the single harmony band.  
  * **Doc posture.** Keep full Magic-10 math here as authoritative (IDs/order, banding semantics); public transport bytes remain in **HDE-CLI-API-Vendor Ref** (titles-only).  
* **Feature extractors (EM / Hanging Gates / Dominance–Compromise / Throat adjacency / …) — \[Speculative\]**

  * **Intent (one-liners).** Deterministic, pure signals for dyadic analysis (EM, HG, center balance, throat pathways, etc.), producing bounded enums/booleans for aggregation.  
  * **Common invariants.** Pure & deterministic (no time/network/random/file I/O); locale-neutral; AB↔BA symmetric; closed vocabularies; typed failures for unavailable states.  
  * **I/O shapes.** Inputs: normalized charts \+ frozen catalogs (titles-only). Outputs: small bounded maps (for example, `{ "em": true, "dominance": "g_identity", … }`); no narratives.  
  * **Acceptance (when wired).** Unit goldens \+ property tests; catalog linkage; aggregation contract to presets; **no public surface in v1**.  
* **Presets & aggregation math — \[Speculative\]**

  * **Intent.** Catalog-driven, deterministic combination of feature signals to integer category scores 0..100, then bands via inclusive maxima 24/49/74/100 (see §2.2/§5.3).  
  * **Preset catalog (frozen).** Named/versioned; any change to weights/caps/floors/corrections bumps the freeze pack and `release_id` (**HDE-Schemas and Artifacts**).  
  * **Validation.** Preset name resolves to exactly one catalog entry; viewer prefs validated independently; all decisions AB↔BA neutral.  
  * **Public rule.** Presets affect internal scores only; Reader v1 stays bands-only with single harmony.  
* **Reader transport — proof surfaces & ops (titles-only routing)**

  * **Endpoint Catalog (JSON success) — \[Required-Now\].** Single proof surface for A7 on success endpoints **(see HDE-CLI-API-Vendor Ref §5.6 and Appendix A)**. Catalog is titles-only/path-agnostic; publish a records-only snapshot and mirror it 1:1.  
  * **Dev harness — \[Implemented (dev-only)\].** Dev/test capture for schema/LF and parity **(see HDE-CLI-API-Vendor Ref)**; rails closed; no vendor I/O.  
  * **/internal/version (ops endpoint) — \[Required-Now\].** Ops-only identity surface; acceptance in **HDE-Governance §10.5**.  
  * **Production public Reader endpoint — \[Speculative\].** Future public surface; conditional delivery/headers owned in **HDE-CLI-API-Vendor Ref**/**HDE-Governance**.  
* **Serializer/emitter — single shared entrypoint — \[Required-Now\]**

  * **One emitter for public bytes.** Reader and CLI call the same presenter/emitter; **no ad-hoc serializers**. Canonical JSON: UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets (dedupe \+ ASCII sort).  
  * **Determinism & parity.** Single emitter guarantees Reader↔CLI byte equality, AB↔BA, and two-run identity.  
  * **Evidence.** Grep-guard (no alt serializers), symbol proof (shared emitter), parity fixtures — all titles/paths only and mirrored 1:1.  
* **Vendor ingest (HDAPI) — \[Owned in HDE-CLI-API-Vendor Ref\]**

  * **Request shaping — \[Implemented\].** Endpoint/method, canonical headers, and three-key body (`birthdate`,`birthtime`,`location`).  
  * **Base-URL resolution — \[Required-Now\].** `HDAPI_BASE_URL` required (env); no literal default. Missing/empty ⇒ typed failure (no network I/O).  
  * **Live HTTP gated by SAFE rails — \[Required-Now\].** Vendor calls only when `SAFE_MODE=0` and `ALLOW_NETWORK=1`; default closed for dev/CI.  
  * **Production calls — \[Speculative\].** Timeouts/retries/backoff/rate-limits/observability pinned before enabling.  
* **Retired: prompt, uncertainty — removed**

  * **Scope.** Public Reader v1 is narrative-free; any mention of prompt/“uncertainty” is out of scope and removed from schema and emitter.  
  * **Acceptance.** Success bodies pass schema without prompt; error bodies unchanged (typed, LF-terminated). Goldens for Reader/CLI parity remain bands-only.

**Routing (no duplication).** Transport/CLI specifics are referenced by title in **HDE-CLI-API-Vendor Ref**; operational acceptance (A7, internal-ops exception, evidence policy) is in **HDE-Governance**. Canonical JSON & manifest/mirror rules live in **HDE-Schemas and Artifacts**.

---

# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]

## **2.1 Success payload (six keys; numeric-free) \[Implemented\]**

**Normative rule.** The Reader v1 public success body is a numeric-free JSON object containing exactly six top-level keys. No additional public fields are allowed. All serialization uses canonical JSON (**HDE-Schemas & Artifacts** §4: UTF-8 without BOM, sorted keys, compact, exactly one trailing `\n`; arrays treated as sets are deduplicated and ASCII-sorted).

**Required keys (success) — exactly these six**

* **reader\_version :** `"v1"` — fixed string.  
* **eligible :** `<boolean>` — whether the pair is eligible for public evaluation.  
* **categories :** `[ { "id", "band" } … ]` — array of public category items (policy in §2.2).  
* **meta :** `{ "engine_tag", "invocation_tag" }` — engine build tag and invocation tag (both non-empty strings; invocation tag is the short form from **Invocation**; ownership and format per **HDE-Governance** / **HDE-Schemas & Artifacts** Identity, titles-only).  
* **release\_id :** `<hex64>` — lowercase 64-hex identifier of the frozen pack manifest in use (**HDE-Schemas & Artifacts** §6; see §3.1).  
* **idempotence\_hash :** `<hex64>` — lowercase 64-hex SHA-256 of the canonical five-key preimage (see §3.2).

**Public category policy (v1)**

* Each item in `categories` is exactly `{ "id": <string>, "band": "Cool" | "Open" | "Warm" | "Glow" }`.  
* Not permitted on the public surface: `prompt` (removed), `personal_key`, `shared_key`, or any numeric (e.g., score, percent).  
* Category identifiers are `snake_case` and come from the Magic-10 IDs set (**HDE-Schemas & Artifacts** §2.6). In v1, only the `"harmony"` public item may appear (see §2.2).

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
* Arrays that represent sets are **deduped and ASCII-sorted** (bytewise) before hashing/compare (PF-12 §4).  
* In v1 (single item), sorting is **vacuously satisfied**; **uniqueness still applies**.

  ### **Public shape constraints (reaffirmed)**

* Each item is **exactly** `{ "id": <string>, "band": "Cool" | "Open" | "Warm" | "Glow" }`.  
* `id` **must** come from the **Magic-10 closed set** (PF-12 §2.6; PF-01 §5.1). *(v1 publicly exposes only `"harmony"`.)*  
* **Never permitted** on the public surface: `prompt`, `personal_key`, `shared_key`, `score`, or any numeric/free-text payloads.

  ### **Determinism coupling**

* `categories` contributes to the **idempotence preimage** (see §3.2; fields defined in PF-01).  
* **AB↔BA identity** and **two-run identity** MUST hold at the byte level after **canonical serialization** (PF-12 §4; UTF-8 no BOM, sorted keys, compact, exactly one LF).

  ### **Acceptance gates (binary)**

1. **Exactly-one rule (eligible):** `eligible == true` ⇒ `len(categories) == 1` **and** `categories[0].id == "harmony"`.  
2. **Band enum:** `categories[0].band ∈ {"Cool","Open","Warm","Glow"}`.  
3. **Empty rule (ineligible):** `eligible == false` ⇒ `len(categories) == 0`.  
4. **No extras:** every `categories[*]` has **only** `id` and `band`.  
5. **Uniqueness:** **no duplicate `id` values** (trivial in v1).

   ## **2.3 Errors (shape/pointers) \[Required-Now\]**

   ### **Typed public error object (numeric-free, no PII)**

* **Shape (minimum):** the public error body is a typed JSON object with:  
  * `ok: false`  
  * `code: "<token>"` — short, machine-readable error token  
  * `error: "<non-PII message>"` — human-readable, non-secret message  
* **Optional field (when applicable):**  
  * `retry_after_ms: <integer >= 0>` — present only when a rate-limit or backoff condition applies  
* **No additional public fields** (no narratives, no keys, no numerics beyond `retry_after_ms`).

  ### **Hygiene and guardrails**

* **No PII or secrets** in error messages; keep messages succinct and generic.  
* **Determinism:** error bodies are serialized by the same canonical path as success (**HDE-Schemas & Artifacts** §4): UTF-8, sorted keys, compact separators, exactly one trailing LF.

  ### **Pointers (transport & status live elsewhere)**

* **Transport ownership:** HTTP status mapping, headers, conditional delivery, caching, and streams/exit codes are owned by **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** and are referenced here by title only.

---

## **2.4 Ordering semantics (comparators) \[Required-Now\]**

**Purpose (normative).** Define the mathematical ordering rules that guarantee deterministic, stable outputs. Mechanics and tests live in **HDE-Mechanics Guide** (titles only).

**Comparators (math rules)**

* **IDs / centers / labels:** ASCII lexicographic (bytewise).  
* **Channels:** normalize to zero-padded `NN-NN` (min-first, ASCII hyphen `-`), then compare ASCII lexicographically.  
* **Categories:** primary order by the frozen Magic-10 rank (see **HDE-Schemas and Artifacts §2.6**), tie-break by `id` (ASCII).  
* **Stable-on-equality:** when primary keys compare equal, apply a canonical secondary key so the order is **total and stable** across runs.

**Set semantics (arrays-as-sets).** Any array that represents a set **MUST** be deduplicated and ASCII-sorted before hashing/compare (see **HDE-Schemas and Artifacts §4**). Non-canonical or duplicate elements **fail validation**.

**Channel rejection posture.** Reversed or unparsable channel tokens **hard-fail** (typed error). Reversal (e.g., `34-20`) **normalizes to** `20-34` before compare; invalid tokens are **not** coerced.

**Environment pins (determinism).** All comparisons and byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Routing (titles only).**

* Runnable helpers & tests (`dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`): **HDE-Mechanics Guide**.  
* Magic-10 rank (closed set & order): **HDE-Schemas and Artifacts §2.6**.

**Acceptance (tokens; titles only).** `TIEBREAK_TOTAL_ORDER_OK` *(supports `CATEGORY_FRAMEWORK_OK`)* — token names live in **HDE-Governance §2.0**.

**Evidence (records-only; indexed via the machine mirror).** Property tests (antisymmetry / transitivity / totality), a channel-normalization corpus (input → canonical `NN-NN`, rejects for non-canonical), and canonical before/after examples for set-normalized arrays. List by title/path in **Appendix D: Evidence Index** and mirror 1:1 in `artifacts/evidence_index.jsonl` with path-proofs.

**EPIC017 D4 proof (informative).**  
 EPIC017’s “deterministic tie-break and total-order module” deliverable, as recorded in **HDE Phased Epics Map**, implements comparators for IDs, channels, categories, and arrays-as-sets exactly as specified in this section. It proves antisymmetry, transitivity, totality, AB↔BA identity, and two-run identity using ordering artifacts and tests defined in **HDE-Mechanics Guide** and **HDE-Schemas & Artifacts**. These proofs confirm the semantics defined here; EPIC017 does **not** alter the ordering rules or arrays-as-sets behavior in this spec. Any future change to comparator policy or set semantics remains a PF01 math change and must follow the usual release-id and evidence requirements.

---

# 3\. Identity & Determinism \[Required-Now\]

## **3.1 release\_id — freeze-pack identity (sha256) \[Implemented\]**

**Definition (normative).** `release_id` is the lowercase 64-hex SHA-256 of the **canonical** freeze-pack manifest. It is stable for a given pack and changes only when a frozen input or the manifest’s canonical bytes change.

**What the freeze pack includes (by title).** The pack is the set of frozen math inputs enumerated in the pack manifest (single home: **HDE-Schemas and Artifacts**), including at minimum:

* **Topology catalogs:** `centers.json`, `gates.json`, `channels.json` (canonical `NN-NN` channel identities; centers in `snake_case`).  
* **Magic-10 catalog:** the closed, ordered ID set (IDs only; thresholds live in the constants pack).  
* **Constants pack:** `limits.em_max`, `limits.throat_em_max`, `limits.centers_max`, `limits.motor_throat_max`, `limits.mind_throat_max`, `limits.comp_max`, and `bands.thresholds` (inclusive-high maxima).  
* **Direct Motor→Throat set (if catalogized):** governed four-channel set in canonical `NN-NN`; treated as a frozen input when listed in the manifest.  
* **Seeds catalog (when present):** if catalogized in **HDE-Schemas and Artifacts**, Seeds are admin/test inputs; any byte change triggers a new `release_id`.  
   Transport/ops bytes are out of scope and **not** part of this identity.

### **Construction (canonical)**

1. **Manifest.** Build the pack manifest at `catalog/manifest.json` with shape:  
    `{"root":"catalog/","version":"<semver>","built_at_utc":"YYYY-MM-DDThh:mm:ssZ","files":[{"path":"…","sha256":"<64hex>","size":<int>},…]}`. The manifest **MUST NOT** self-list.  
2. **Canonicalize.** Serialize the manifest using **HDE-Schemas and Artifacts** canonical JSON rules: UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing `\n`; arrays-as-sets deduped and ASCII-sorted.  
3. **Hash.** `release_id = sha256(canonical_bytes("catalog/manifest.json"))` → 64-hex, lowercase. CI also requires the on-disk manifest to be canonical; non-canonical storage is a hard-fail even if the canonical hash would be unchanged.

**Casing & format**

* Exactly 64 lowercase hex: `^[0-9a-f]{64}$`.  
* No prefixes/suffixes; no whitespace.

**Change conditions**

* **MUST** change on any byte change to a governed file (topology catalogs, constants pack, Magic-10 catalog, direct Motor→Throat set if catalogized), or to the manifest’s `files[]` entries, or to the manifest’s shape/ordering.  
* Pure formatting changes to the on-disk manifest do not change `release_id` after canonicalization, but still fail CI if the stored file is non-canonical.

**Scope & coupling**

* `release_id` is included in the Reader v1 success body and participates in acceptance checks (see §2, §3.4; Governance A-gates by title).  
* **Pins.** All recomputation runs with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Only the selected pack and its canonical manifest affect the value.

**Validation (binary)**

* **Pattern:** value matches `^[0-9a-f]{64}$`.  
* **Provenance:** evidence (titles/paths only) includes the canonical manifest artifact and the computed `release_id`.  
* **Determinism:** recomputing over the same pack yields the same `release_id` (two-run identity).

**Acceptance gates (titles-only)**  
 `RELEASE_ID_FROM_MANIFEST_OK`, `RELEASE_ID_RECOMPUTE_OK`, `MANIFEST_SHA256_HEX64_OK`, `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`.

**Non-goals (routed by title only).** HTTP headers, conditional delivery, caching/writers, and CLI/Reader validators live in **HDE-CLI-API-Vendor Ref** and **HDE-Governance**.

## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Implemented\]**

**Definition (normative).** `idempotence_hash` is the lowercase 64-hex SHA-256 of the canonical preimage of the Reader v1 success envelope. It proves that the published bytes arise from a single, canonical representation.

### **Canonical preimage (success case)**

Build an object with exactly five keys (no others), each already normalized per this spec and **HDE-Schemas & Artifacts**:

1. `reader_version` : `"v1"`  
2. `eligible` : `<boolean>`  
3. `categories` : `[{"id","band"}]` — public policy per §2.2 (v1 exposes one item `{"id":"harmony","band":<Cool|Open|Warm|Glow>}` when `eligible == true`; `[]` when `eligible == false`; numeric-free)  
4. `meta` : `{"engine_tag","invocation_tag"}` — titles-only references to **HDE-Schemas & Artifacts** (invocation tag is the short form; no other fields in public `meta`)  
5. `release_id` : `<hex64>` — as defined in §3.1

Do not include `idempotence_hash` in the preimage.

### **Canonical serialization (preimage & final)**

Use **HDE-Schemas & Artifacts** rules: UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays that represent sets are deduplicated and ASCII-sorted. All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **Emission algorithm (success)**

1. **Preimage.** Serialize the five-key object → `preimage_bytes` (LF-terminated, canonical).  
2. **Hash.** `digest = sha256(preimage_bytes)` (lowercase 64-hex).  
3. **Final.** Add `idempotence_hash : <digest>` and re-serialize canonically → public bytes.

### **Correctness properties**

* **Deterministic & stable.** Any preimage byte change (field value, order, band, `release_id`) changes `idempotence_hash`. Canonicalization removes non-semantic whitespace/key-order differences.  
* **AB↔BA identity.** Pair inputs are normalized (this spec’s composite rules; **HDE-Schemas & Artifacts** topology normalization), so AB and BA produce identical `preimage_bytes` and the same `idempotence_hash`.  
* **Two-run identity.** Re-emitting the same logical object yields byte-identical preimage and final bodies.  
* **Reader↔CLI parity.** For identical inputs/environment, CLI stdout and Reader emit byte-identical success bodies (and thus the same `idempotence_hash`).

### **Validation (binary)**

* **Pattern.** Value matches `^[0-9a-f]{64}$`.  
* **Recompute check.** Remove `idempotence_hash` from the published body, re-serialize canonically, hash, and confirm equality with the published digest.

**Acceptance (tokens, titles-only).** `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`.  
 **Non-goals / routing.** `idempotence_hash` is not an HTTP transport token; ETag/conditional semantics live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** (titles only).  
 **Tokens:** see **HDE-Governance §2.0**.

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

## **3.4 Two-run identity & AB↔BA parity (public) \[Implemented\]**

### **Definition (normative)**

* **Two-run identity.** Serializing the same logical success envelope twice (same inputs, same environment, same `invocation_tag`, same `release_id`) **MUST** produce byte-identical public bytes.  
* **AB↔BA parity.** For a given pair of **normalized** inputs, swapping input order (AB vs BA) **MUST** produce byte-identical public bytes.

### **How it is achieved (concept)**

* **Canonical preimage → hash → final** (see §3.2). Identical preimages yield identical `idempotence_hash` and final bytes.  
* **Pair normalization.** Inputs are normalized **before** any computation (see topology normalization in HDE-Schemas and Artifacts), guaranteeing order-neutrality for scores, bands, and envelope.  
* **Single emitter.** One canonical JSON emitter shared across Reader and CLI (UTF-8, sorted keys, compact, exactly one LF) eliminates serializer drift across surfaces.  
* **Environment pins.** All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **Evidence & goldens (titles/paths only)**

* **Reader/CLI parity & LF discipline** (schema \+ byte checks): `tests/reader_v1/`, `tests/cli/`, `schemas/reader.v1.schema.json`.  
* **AB↔BA golden proofs (public success parity):**  
   `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`.  
* **Identity markers & scripts:** `artifacts/cards/A3/IDENTITY_OK.txt`, `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`.  
* **Emitter identity:** canonical emitter SHA-256 (see **Appendix B — Evidence Index**, titles only).  
* **Index & mirror rule:** Every item above is listed by title/path in the human Evidence Index and mirrored 1:1 in `artifacts/evidence_index.jsonl` with path-proofs (see HDE-Schemas and Artifacts).

### **Byte-level acceptance (binary)**

* **Two-run identity.** For a fixed input set and environment, two serializations of the success envelope are exactly identical, including the single trailing LF; confirm by byte-compare and by recomputing `sha256(preimage_bytes)` to reproduce the published `idempotence_hash`.  
* **AB↔BA parity.** Given inputs A,B and B,A, the emitted bytes are bit-for-bit identical; confirm by byte-compare and equal `idempotence_hash`.  
* **Serializer invariants.** Outputs are UTF-8, sorted keys, compact separators, exactly one LF, no BOM/ANSI, and schema-valid in both success and error modes.

**Non-goals / routing.** Header matrices, conditional delivery, caching/writers policy, and CLI stream rules are not duplicated here; see **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles only).

---

#  **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**

## 4.1 Definition (normative)

* **Eligibility** is a **mechanical, catalog-driven gate** indicating whether a pair can be evaluated for public output.

* The result is a **boolean** (`eligible: true|false`) and **does not carry numerics** or narrative content.

## 4.2 Inputs and catalogs (concept)

* The decision references only **frozen catalogs/manifests** and normalized inputs defined by this spec.

* All lookups are **deterministic** and performed against the **freeze pack** associated with the current `release_id`.

* Eligibility logic is **independent of any “prompt” or “uncertainty” concepts** (both are removed from this spec).

## 4.3 Determinism & neutrality

* **Order-neutral:** After canonical pair normalization, the eligibility outcome for **AB** equals that for **BA**.

* **Two-run identity:** With the same inputs and freeze pack, recomputing eligibility yields the same boolean.

* No time, network, or random sources influence eligibility.

## 4.4 Public behavior

* **If `eligible == true`:** the public `categories` array **MUST** comply with §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).

* **If `eligible == false`:** the public `categories` array **MAY** be empty. No numerics or narrative fields appear in either case.

## 4.5 Validation (binary)

* **Catalog closure:** every reference used by the gate must resolve within the freeze pack.

* **Determinism checks:** AB↔BA parity and two-run identity are satisfied for the eligibility boolean.

* **Schema coupling:** the success envelope reflects eligibility as per §2.1; the value participates in the **preimage** for `idempotence_hash` (see §3.2).

## 4.6 Non-goals / routing

* No transport policy, caching, or HTTP status mapping is specified here; such details are referenced **by title only** in the transport/CLI and governance documents.

## 4.7 Emission rule (binary) \[Required-Now\]

* **Eligible ⇒** **emit categories** per §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).

* **Ineligible ⇒** **`categories: []`** (empty array). No numerics, no narrative fields.

## 

# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Speculative\]

## **5.1 Canonical IDs (closed set) \[Required-Now\]**

**Definition (normative).** The **Magic-10 category identifiers are a closed, ordered set** of ASCII-lowercase strings. **PF-Canon-HDE-Schemas & Artifacts §2.6** is the **single home** for this set **and its order**. This specification **does not restate** the list; any consumer must dereference it **by title**.

**Use and exposure**

* **Internal math:** the compat layer consumes this closed set for scoring → band mapping (see **§5.2**, **§5.3**).  
* **Public surface (v1):** Reader v1 is **bands-only & numeric-free**; it exposes only `{"id":"harmony","band":…}` (see **§2.2**). Exposure of all ten categories is a **future, versioned** change.

**Ordering and uniqueness**

* **Order is pinned** in **PF-12 §2.6** and is the **normative iteration order** for any ordered consumer (comparators in **§2.4**).  
* Identifiers are **unique**; duplicates are **forbidden**.

**Format and validation**

* Identifiers are **ASCII-lowercase**; **validators MUST enforce exact membership** against PF-12 §2.6. Pattern pre-filters (e.g., `^[a-z]+$`) are insufficient for acceptance; **exact set** membership is required.  
* Inputs that reference categories (e.g., viewer weights) **must cover exactly this closed set**; **no extras or omissions**.  
* Catalogs/schemas (PF-12 §2.6) **reject non-members**; stored JSON follows **PF-12 §4** (UTF-8 no BOM, sorted keys, compact, **one LF**).

**Change control (freeze-pack coupling)**

* **No membership/order edits in this version.** Any change to **membership or order** is a **frozen-input change**; it **requires a new pack manifest** (PF-12 §6) and therefore a **new `release_id`** (see **§3.1**).  
* Downstream governed artifacts (e.g., Magic-10 catalog, band maxima, presets) must reference **only these IDs**; changing them also **bumps `release_id`**.

**Determinism guarantees**

* Closed membership \+ fixed order, combined with **canonical serialization** and **preimage hashing** (see **§3.2**), ensures **AB↔BA identity** and **two-run identity**.  
* With identifiers immutable and order pinned, category iteration/aggregation is **byte-stable** across surfaces.

**Acceptance & CI (titles-only)**

* **MAGIC10\_DOMAIN\_CLOSED\_OK**, **MAGIC10\_NAMES\_FROZEN\_OK** (set & order frozen; change ⇒ new `release_id`)  
* **PREFS\_KEYSET\_10\_OK** (viewer-prefs keys \== this set)  
* **EVIDENCE\_INDEX\_UPDATED\_OK** (on any change to governed catalog)

---

## **5.2 Deterministic integer scoring model (caps; fixed-point rules)**

**Scope.** Defines the **per-category scoring model** that converts normalized inputs (and, optionally, viewer weights or presets) into **integer scores in \[0..100\]**, prior to band mapping (**§5.3**). Deterministic, **order-neutral (AB↔BA)**, and **fixed-point** (no persisted floats).

### **5.2.1 Inputs (closed and validated)**

* **Category universe:** **exactly** the Magic-10 IDs from **§5.1** (closed set; fixed order).  
* **Pair normalization:** inputs are canonically ordered **before any scoring**; all downstream steps consume the **normalized** pair.  
* **Viewer weights (optional):** if present, **every category** must have an **integer weight in \[0..100\]**; missing/extra keys are **invalid**.

### **5.2.2 Deterministic base (order-neutral seed)**

Each category’s score begins from a **stable, order-neutral base** derived from `(pair_key, category_id)` with these properties:

* **Pure function** of `(pair_key, category_id)`; **no time/network/randomness**.  
* Produces a bounded **integer in \[0..100\]**.  
* Changes only when inputs or the category ID change (freeze-pack changes are reflected via **§3.1 `release_id`**).

*Baseline (informative).* A stable hash of `"pair_key:category"` modulo 101 yields a base integer in **\[0..100\]**.

### **5.2.3 Weight application (fixed-point)**

If viewer or preset weights are provided, they influence scores without floating-point drift:

* **Weight domain:** normalize `w_cat ∈ {0..100}` to a **fixed-point factor in \[0..1\]** (half-unit arithmetic; **no persisted floats**).  
* **Monotone lifting:** apply a deterministic monotone function that never decreases the base when weights increase and **never exceeds 100**.  
* **Fixed-point arithmetic:** any fractional intermediate is represented in **half-units** and converted by the pinned **rounding rule** (**§5.2.5**) to an integer before clamping.

*Baseline (informative).* `val = base * (0.5 + 0.5 * w_cat/100)`; then **round\_half\_up** and **clamp to \[0..100\]**.

### **5.2.4 Caps and floors (deterministic bounds)**

* **Per-category clamp:** final category score **MUST** be **clamped to \[0..100\]**.  
* **Optional floors/caps:** if specified (e.g., by preset), apply **deterministically** and record them in the **freeze pack**; changing them **requires a new `release_id`** (see **§3.1**).

### **5.2.5 Rounding rule (pinned)**

Whenever rounding is required, use **round\_half\_up** to the nearest integer. This mode is **normative and global** for scoring steps. Changing it is a math change that **requires a new freeze pack** (and `release_id` bump).

### **5.2.6 Determinism and neutrality**

* **AB↔BA parity:** scoring consumes the **normalized** pair; scores for AB and BA are **identical**.  
* **Two-run identity:** same inputs, catalogs, presets/weights ⇒ **bit-identical** integer scores.  
* **No hidden sources:** scoring never uses wall-clock, randomness, external I/O, locale-dependent collation, or platform-dependent float accumulations.

### **5.2.7 Validation (binary)**

* **Category coverage:** a score is computed for **every Magic-10 ID**; **no extras**.  
* **Weight coverage:** when weights are present, the key set equals the Magic-10 set and **all values ∈ \[0..100\]** (integers).  
* **Clamp & rounding proof:** goldens demonstrate correct **round\_half\_up** and final **\[0..100\]** clamping at boundaries (0, 100, midpoints).  
* **Parity proof:** AB vs BA yields **identical** score vectors; **two identical runs** produce identical vectors.

### **5.2.8 Change control**

Any modification to the **base function**, **weight function**, **caps/floors**, or **rounding rules** is a **math change** and **MUST** be captured in the freeze pack; recomputing the canonical manifest **must yield a new `release_id`** (§3.1).

### **5.2.9 Routing (no transport bytes here)**

Math only. No HTTP/CLI payloads, status/header matrices, or validator bytes are restated here; those live in **PF-Canon-HDE-CLI-API-Vendor-Ref** (titles-only).

* 

## **5.3 Band mapping (preset-specific inclusive maxima)**

**Definition (normative).** Band mapping converts each integer category score in `[0..100]` to one of four public bands using the preset’s **inclusive-high** maxima. For an active preset *P* with maxima `M_cool(P) ≤ M_open(P) ≤ M_warm(P)` (all integers):

* **Cool:** `score ≤ M_cool(P)`  
* **Open:** `score ≤ M_open(P)`  
* **Warm:** `score ≤ M_warm(P)`  
* **Glow:** otherwise (`score > M_warm(P)`; **100 always maps to Glow**)

**Coupling to the freeze-pack.** In v1, the band maxima are stored in the **constants pack** as `bands.thresholds` (see §5.4.2; **HDE-Schemas and Artifacts**). Any change to any maximum is a frozen-input change and **requires a new `release_id`** (see §3.1).  
 *Forward note:* if a future version introduces **preset-specific** maxima, those values MUST be catalogized in **HDE-Schemas and Artifacts** (titles only) and will likewise be frozen-inputs that bump `release_id`.

### **5.3.1 Domain and monotonicity**

* **Score domain.** Inputs to band mapping are integers `0..100` (see §5.2). If any upstream step produces fixed-point, integerize via §5.2 `round_half_up` first.  
* **Monotone mapping.** If `s1 ≤ s2` then `band(s1) ≤ band(s2)` in the total order `Cool < Open < Warm < Glow`.  
* **No gaps or overlaps.** Every integer in `0..100` maps to exactly one band; thresholds are **inclusive** at each maximum.  
* **Maxima domain.** To preserve `100 → Glow`, presets **MUST** satisfy `0 ≤ M_cool(P) ≤ M_open(P) ≤ M_warm(P) ≤ 99`.

### **5.3.2 Boundary behavior (normative)**

* `M_cool(P)` → **Cool**, `M_cool(P)+1` → **Open**  
* `M_open(P)` → **Open**, `M_open(P)+1` → **Warm**  
* `M_warm(P)` → **Warm**, `M_warm(P)+1 … 100` → **Glow**  
* `100 → Glow` (even if `M_warm(P) = 99`)

### **5.3.3 Determinism and neutrality**

* **AB↔BA identity.** Scores are computed from the **normalized composite** (see §5.2; **HDE-Schemas and Artifacts §2.1**); band mapping yields identical results for AB and BA.  
* **Two-run identity.** With the same inputs, catalogs, constants, and preset, repeated evaluation produces identical band arrays.  
* **No float dependence.** Mapping uses only integer comparisons; platform/locale cannot affect outcomes. Run checks with `LC_ALL=C`, `LANG=C`, `TZ=UTC` (**HDE-Schemas and Artifacts §4**).

### **5.3.4 Validation (binary)**

* **Completeness:** every produced score in `0..100` maps to one of the four bands.  
* **Boundary proofs:** goldens cover each preset’s edges: `M_cool(P)/M_cool(P)+1`, `M_open(P)/M_open(P)+1`, `M_warm(P)/M_warm(P)+1`, and `100`.  
* **Parity proofs:** AB vs BA yield identical band arrays; two identical runs yield identical arrays (byte-level after canonical JSON per **HDE-Schemas and Artifacts §4**).

### **5.3.5 Change control**

* **Breaking change.** Adjusting any preset maximum or the band order is a math change; it **MUST** be recorded in the pack manifest (**HDE-Schemas and Artifacts §6**) and yields a new `release_id` (see §3.1).  
* **Downstream lockstep.** Consumer schemas and acceptance must be kept in lockstep when maxima change (titles only), for example: `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`.

### **5.3.6 Routing (no transport bytes here)**

Math only. Any CLI/Reader payload examples, header rules, or validator matrices remain in **HDE-CLI-API-Vendor Ref** (titles only).

**Acceptance & CI (titles only)**  
 `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `INTRINSIC_SCORING_INT_OK`, `ROUND_HALF_UP_OK`,  
 `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`,  
 `RELEASE_ID_RECOMPUTE_OK`, `EVIDENCE_INDEX_UPDATED_OK` *(when maxima change)*

---

## **5.4 Manifests and freeze-pack coupling (change ⇒ new `release_id`)**

**Purpose (normative).** This section defines **what constitutes the frozen math pack**, how its contents are canonically manifested, and **why any change requires a new `release_id`** (see §3.1). **Transport/ops bytes are out of scope** and are referenced by title to their owners (PF-Canon-HDE-CLI-API-Vendor-Ref, PF-Canon-HDE-Governance).

### **5.4.1 What the freeze pack contains (math only)**

The freeze pack is the authoritative set of **math inputs** required to compute public outputs. It excludes transport and ops bytes. At minimum it includes:

* **Category manifest.** Closed **Magic-10 identifier set and pinned order** (see §5.1; PF-12 §2.6).  
* **Band-maxima manifest.** **Preset-specific inclusive-high maxima** for **Cool/Open/Warm/Glow** (see §5.3; PF-12 §2.6).  
* **Topology catalogs.** Fixed **Centers/Gates/Channels** catalogs (PF-12 §2.1; canonical **NN-NN** channel identity, snake\_case centers) and any math-relevant vocabularies used by extractors (e.g., channel→center adjacency) when serialized as governed artifacts.  
* **Preset catalog (if used).** Named, versioned presets (e.g., A, B) carrying deterministic arithmetic knobs (e.g., per-category weights, optional caps/floors/feature switches).  
* **Constants pack** (see §5.4.2). **Frozen denominators/limits** and **band thresholds** required by this spec.

*Non-content:* HTTP headers, caching/writers policy, CLI streams, and validator matrices are **not** part of the pack and are routed by title to PF-CLI-API / PF-Governance.

### **5.4.2 Constants pack (frozen keys & schema) \[NEW\]**

**Purpose.** Govern the frozen scalar/vector parameters invoked by this spec. The constants pack is a JSON artifact whose file name and path are recorded in the pack manifest (see **HDE-Schemas and Artifacts §6**). Changes to any frozen value are frozen-input changes and **require a new `release_id`** (see §3.1).

**D1 — Frozen keys (normative)**

* `limits.em_max` *(int, ≥ 0\)*  
* `limits.throat_em_max` *(int, ≥ 0\)*  
* `limits.centers_max` *(int, \> 0\)*  
* `limits.mind_throat_max` *(int, ≥ 0\)*  
* `limits.motor_throat_max` *(int, ≥ 0\)*  
* `limits.comp_max` *(int, ≥ 0\)*  
* `bands.thresholds` — array of 4 ints `[cool, open, warm, 100]` with `0 ≤ cool ≤ open ≤ warm ≤ 99 < 100` *(inclusive-high; see §5.3 for semantics and rounding)*

**Note (v1).** Resonance/diagnostic inputs (for example, XR windows, α, hysteresis) are **admin/test-only** and **not** part of the frozen constants pack. If later catalogized in **HDE-Schemas and Artifacts**, they become frozen inputs and any change **yields a new `release_id`**.

**D2 — JSON shape (normative)**  
 A single JSON object with **canonical JSON** serialization (see **HDE-Schemas and Artifacts §4**):

{

  "limits": {

    "em\_max": \<int\>,

    "throat\_em\_max": \<int\>,

    "centers\_max": \<int\>,

    "mind\_throat\_max": \<int\>,

    "motor\_throat\_max": \<int\>,

    "comp\_max": \<int\>

  },

  "bands": { "thresholds": \[ \<int\>, \<int\>, \<int\>, 100 \] }

}

**Change ⇒ new `release_id`.** Any addition/removal or value change to the keys above is a frozen-input change and **requires** a new `release_id` (see §3.1; **HDE-Schemas and Artifacts §6**).

**Indexing & evidence (titles-only).** List the constants artifact in **Appendix D: Evidence Index** and mirror it 1:1 in `artifacts/evidence_index.jsonl` with path-proofs.

**Acceptance & CI (titles-only).**  
 `JSON_CANONICAL_CHECK_OK`, `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`,  
 `RELEASE_ID_RECOMPUTE_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `EVIDENCE_INDEX_UPDATED_OK`  
 *(token names live in HDE-Governance §2.0)*

#### **5.4.2.1 Direct Motor→Throat (v1) — governed set**

**Purpose (normative).** Define the **direct-only** Motor→Throat set that participates in denominator logic. This set is a governed artifact in the freeze-pack and **must not** include 2-hop routes.

**Canonical definition**

* **Set (`NN-NN`, min-first; ASCII-sorted):** `["12-22","20-34","21-45","35-36"]`  
* **Normalization rule.** Channel identifiers are normalized to zero-padded `NN-NN` with the lower gate first. Reversed forms (for example, `34-20`) normalize to `20-34`.  
* **Rejection posture.** Unparsable tokens or non-canonical forms hard-fail validation (typed error); no silent coercion.

**Storage & serialization (pack entry)**

* Represented as a JSON **array of strings** (the four canonical `NN-NN` pairs).  
* **Canonical JSON** (see **HDE-Schemas and Artifacts §4**): UTF-8 (no BOM), sorted keys/values (ASCII), compact, exactly one trailing LF; arrays treated as sets (dedupe \+ ASCII-sort).  
* **Manifest coupling.** Listed in the pack manifest (**HDE-Schemas and Artifacts §6**) with its **repo-relative path (relative to `root: "catalog/"`, no `catalog/` prefix)**, `sha256` (lowercase 64-hex of canonical bytes), and `size`.  
* **Change ⇒ new `release_id`.** Any addition/removal/value change triggers a manifest recompute and a new `release_id`.

**Validation (binary)**

* **Set equality.** The governed artifact equals the four-element canonical list above (after ASCII-sort).  
* **Normalization.** A test corpus proves min-first ordering and `NN-NN` padding; reversed/non-canonical items are rejected.  
* **Manifest closure.** The artifact appears in `files[]` and its recorded `sha256` matches canonical bytes.  
* **Index & mirror.** Add a titles/paths entry to **Appendix D: Evidence Index** and a 1:1 records-only line in `artifacts/evidence_index.jsonl` (with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`).

**Acceptance (titles-only).**  
 `MOTOR_THROAT_DIRECT_ONLY_OK`, `RELEASE_ID_RECOMPUTE_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK` *(token names live in HDE-Governance §2.0).*

---

### **5.4.3 Canonical manifest (construction rules)**

To produce `release_id`, summarize the pack as a single canonical manifest at `catalog/manifest.json` (PF-12 §6.1–§6.2):

1. **Normalization.** Serialize every governed JSON artifact with PF-12 §4 rules: **UTF-8 no BOM, sorted keys, compact, one trailing `\n`; arrays-as-sets are deduped & ASCII-sorted**.  
2. **Entry list.** The manifest contains **files** (ASCII-sorted by `path`), each entry:  
   * `path` — **repo-relative POSIX path** (stable; no `..`, no `//`, ASCII, ≤256 bytes)  
   * `sha256` — **lowercase 64-hex** of the artifact’s **canonical bytes**  
   * `size` — integer byte length of those canonical bytes  
      *(Manifest fields `root:"catalog/"`, `version` (semver), `built_at_utc` are required per PF-12 §6.1; **no self-listing**.)*  
3. **Hash.** `release_id = sha256(canonical_bytes("catalog/manifest.json"))` (lowercase 64-hex).

If a **non-JSON** artifact is governed, its canonical bytes are its **literal file bytes**; any change to those bytes changes its `sha256` and thus the `release_id`.

### **5.4.4 Change policy (what forces a new `release_id`)**

A new `release_id` is required for any of the following:

* **Membership change.** Adding, removing, or renaming a category; altering the Magic-10 order (PF-12 §2.6).  
* **Maxima change.** Changing any **preset band maximum** value (PF-12 §2.6; §5.3).  
* **Catalog change.** Adding/removing/updating topology catalogs or math vocabularies that feed extractors (PF-12 §2.1).  
* **Preset change.** Adding/removing a preset or changing any preset arithmetic knob (e.g., per-category weights, caps/floors, feature switches).  
* **Constants change.** Changing any **constants pack** key or value (see §5.4.2 D1/D2).  
* **Serialization change.** Any change in canonical content/shape/order of a governed artifact that affects its canonical bytes.

*Pure re-formatting* that still serializes to **identical canonical bytes** does **not** change `release_id`, but **non-canonical storage fails CI**.

### **5.4.5 Determinism and neutrality guarantees**

* **Two-run identity.** Building the pack twice from identical sources yields the **same** canonical manifest and `release_id`.  
* **AB↔BA parity.** Because the pack contains only math inputs (independent of pair order), `release_id` is **order-neutral**.  
* **Environment independence.** `release_id` is unaffected by transport configuration, runtime headers, or locale; recomputation runs under **`LC_ALL=C`**.

### **5.4.6 Validation (binary)**

* **Closure.** **Every** math reference used by scoring/aggregation/extractors resolves to a governed entry in the manifest.  
* **Reproducibility.** Recomputing `sha256(canonical_manifest_bytes)` reproduces the `release_id`.  
* **Drift checks.** Any pack change is accompanied by updated **acceptance evidence** (titles/records only) that cites the new `release_id`.

### **5.4.7 Backwards-compatibility posture**

Changing the pack **does not** change the **Reader v1 public covenant** (bands-only; single *harmony*) unless this spec explicitly version-bumps the public contract. If public exposure of the full Magic-10 set is introduced later (e.g., Reader v2), the category and band-maxima manifests become **public-contract inputs** and require coordinated versioning and acceptance updates.

### **5.4.8 Routing (no transport bytes here)**

This section defines **math pack identity only**. Transport headers, conditional delivery, caching/writers policy, and CLI validators live in **PF-Canon-HDE-CLI-API-Vendor-Ref** and **PF-Canon-HDE-Governance** (titles-only).

---

## **5.5 Privacy posture (no percent/numerics on public) \[Speculative\]**

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

* **Internal-only numerics.** All per-category integers in `[0..100]`, intermediate subtotals, caps/floors, dampeners, and preset arithmetic remain **inside the engine** and/or internal compat responses (not public).

* **No leakage via metadata.** `meta` is strictly `{engine_tag, invocation_tag}` (non-PII strings); it must not encode numeric telemetry or user-specific counts.

### **5.5.3 Determinism & routing**

* This posture does **not** alter determinism: preimage rules, AB↔BA identity, and two-run identity still apply (see §3).

* Transport/CLI behavior (e.g., admin streams, headers, or validators) is **not** restated here and is referenced **by title only** in PF-Canon-HDE-CLI-API-Vendor-Ref.

### **5.5.4 Validation (binary)**

* **Schema gate:** the public success schema rejects any numeric fields beyond those already defined for identity/determinism (e.g., no `score`, no `score_pct`).

* **Golden proofs:** public goldens and grep-guards confirm that `categories[*]` contain only `{id, band}` and that top-level keys match the six-key covenant.

* **Parity checks:** CLI stdout and Reader bodies remain byte-identical under this numeric-free policy.

### **5.5.5 Change control**

* Introducing public numerics (e.g., exposing per-category scores or percentages) is a **versioned public-contract change** and requires an explicit Reader version bump and coordinated acceptance.

* Until such a change is approved and versioned, the **numeric-free** public covenant stands.

Note: Internal math exists; public exposure of the full 10-item array is **Reader v2** (future).

## **5.6 Resonance posture (SR/XR; α; hysteresis) \[Required-Now\]**

**Purpose (normative).** Define the v1 resonance posture and its effect on public output. **Public output remains bands-only and numeric-free**; no SR/XR numerics are exposed (see §2).

**Active/postponed behavior (v1).**

* **SR active, XR postponed.** `alpha = 1.0` (blend is all-SR).  
* **Hysteresis armed for future XR.** A one-point guard at the Open↔Warm boundary is defined for future use **only when `alpha < 1.0`**; with `alpha = 1.0` it is inert and not applied.

**Pack membership in v1 (governance rule).**

* **Not part of the constants pack.** Resonance parameters (α, hysteresis, XR windows/reducers) are **not** members of the frozen constants pack in v1 and **must not** appear in the freeze-pack manifest.  
* **Future catalogization.** If any resonance parameter is later catalogized in **HDE-Schemas & Artifacts** and listed in `catalog/manifest.json`, it becomes a **frozen input** and any value change **yields a new `release_id`** (see §6).

**Computation model (informative; deferred paths).**

* **SR (in use).** Integer score `SR_c ∈ [0..100]` per §5.2 (rounding per that section).  
* **XR (deferred).** When enabled in a future version, XR is computed over preset windows and blended as `R* = (1 − α)·SR + α·XR`; integerize per §5.2.  
* **Hysteresis (only if α \< 1.0).** Apply a ±1 Schmitt-style guard at the Open/Warm boundary **before** §5.3 band mapping; other boundaries remain inclusive per §5.3.

**Determinism.**

* **AB↔BA identity.** Resonance uses the normalized composite (see **HDE-Schemas & Artifacts** topology normalization); identical inputs ⇒ identical outputs.  
* **Two-run identity.** Same inputs and catalogs/constants ⇒ identical results and banding (§5.3).  
* **Pins.** Run byte-checked evidence with `LC_ALL=C`, `TZ=UTC`.

**Validation & evidence (titles-only).**

* **No public numerics.** Reader/CLI success bodies remain bands-only; any SR/XR values, if computed internally, are not serialized.  
* **Provenance.** If a future version catalogizes resonance parameters, list the artifact and `release_id` in **Appendix D: Evidence Index** and mirror it in `artifacts/evidence_index.jsonl` (see **HDE-Schemas & Artifacts**).

**Routing (no transport bytes here).** Headers, conditional delivery, caching, and validator matrices live in **HDE-CLI-API-Vendor Ref** / **HDE-Governance** (titles-only).

---

# **6\. Feature Extraction (engine-facing; deterministic) \[Speculative\]**

## **6.1 Electromagnetics (EM): detection and throat flags**

### **Purpose (normative)**

Detect electromagnetic relationships between two normalized charts and produce bounded, deterministic feature outputs for aggregation. EM detection is internal-only; no public numerics or narratives appear on Reader v1.

### **Inputs (closed and validated)**

* **Normalized charts (pair-normalized).** Inputs are canonicalized (AB↔BA neutral) before any detection.  
* **Frozen catalogs.** A freeze-pack catalog (see §5.4) defines the channel map (gate→channel pairs), center topology (including throat), and any aliases. Catalog changes require a new `release_id` (§3.1).

  ### **Invariants (applies to every EM computation)**

* **Deterministic and pure.** No time, network, randomness, or file I/O.  
* **AB↔BA symmetry.** EM outputs for AB equal those for BA after pair normalization.  
* **Closed vocabularies.** Outputs draw only from frozen enums and IDs; no free text and no arbitrary keys.  
* **Numeric-free outputs.** EM does not emit scores or counts to public surfaces; internal aggregation consumes only bounded keys, enums, and booleans.

  ### **Detection (normative rules)**

* **Channel completion.** Electromagnetics are present when complementary gates (from different persons) complete a cataloged channel.  
* **Gate→channel resolution.** Each detected EM MUST resolve to a single catalog channel via the freeze-pack mapping; ambiguous or unmapped combinations fail closed (typed error).  
* **De-duplication (set semantics).** Multiple contributing gates that resolve to the same catalog channel produce one EM entry.  
* **Canonical channel\_id.** For each EM, compute `channel_id = "<lowGate>-<highGate>"` where `<lowGate>` and `<highGate>` are the numeric gates in ascending order, **zero-padded to two digits** (`01..64`). Example: gates `{8, 1}` ⇒ `channel_id = "01-08"`.  
* **Sorting.** The EM channels list MUST be sorted in ascending ASCII order by `channel_id`. Zero-padding guarantees ASCII and numeric orders coincide.

  ### **Throat flags (normative)**

* **Throat involvement.** If any detected EM touches the throat center (per center topology), set `throat_em = true`; otherwise `false`.  
* **Throat-adjacent path.** If the catalog indicates a throat-adjacent pathway (for example, a talk-ladder route), set `throat_route` to the catalog enum value; otherwise omit or set `null`.  
* **Closed enums.** Flags are strictly bounded booleans or enums defined in the catalog.

Note: Final field names and enums are pinned by the catalog schema in the freeze pack; this spec constrains behavior (determinism, symmetry, closure) rather than publicizing field lists.

### **Output (engine-facing; normative shape)**

* {  
*   "em": {  
*     "present": true|false,  
*     "channels": \["\<channel\_id\>", ...\]   // sorted, unique, e.g., \["01-08","10-20"\]  
*   },  
*   "throat\_em": true|false,  
*   "throat\_route": "\<enum\>" | null  
* }  
    
* The `channels` array contains **only** canonical `channel_id` strings, unique and sorted.  
* No counts or scores are required for EM; aggregation may reference only presence and catalog IDs/enums.

  ### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites missing or invalid (for example, malformed gates, unresolved catalog IDs, incompatible chart normalization).  
* **CATALOG\_MISMATCH** — an input references gates or channels absent from the active freeze pack.

  ### **Determinism and acceptance (when wired)**

* **AB↔BA parity proof.** EM outputs are identical for AB and BA.  
* **Two-run identity.** Recomputing EM with the same inputs and catalog yields byte-identical internal feature records.  
* **Catalog coverage.** Golden tests demonstrate correct detection across representative channels, including throat-linked and non-throat paths.  
* **Fail-closed proofs.** Goldens show that unmapped or invalid combinations yield typed failures (no partial EM items).  
* **Sorting and uniqueness.** Goldens prove sorted `channels` and set semantics (no duplicates).

  ### **Change control**

Any change to channel maps, center topology, `channel_id` construction rules, sorting policy, or flag enums is a math-catalog change and requires a new `release_id` (§3.1). Downstream acceptance artifacts must be regenerated.

### **Public surface rule**

EM outputs remain internal-only. Reader v1 stays bands-only with a single `harmony` item (see §2.2). No EM-derived numerics or narratives appear on the public surface.

### **Routing**

Transport and CLI behavior (headers, validators) is not restated here and is referenced by title only in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **6.2 Hanging-gate complements \[Speculative\]**

**Purpose (normative).**  
 Identify **complementary half-channels** across two normalized charts (A,B) and emit **bounded, deterministic** feature outputs that downstream aggregation can consume. Hanging-gate (HG) detection is **engine-internal**; Reader v1 remains numeric-free and bands-only (§2.2).

### **Inputs (closed & validated)**

* **Pair-normalized charts.** All detection consumes the **normalized** (order-neutral) pair.

* **Frozen catalogs.** A freeze-pack catalog (see §5.4) defines:

  * **Gate → channel** mappings (each channel lists its two gates and owning centers).

  * **Center topology** (including channel membership and aliases, if any).

  * **Allowed enums/IDs** for feature fields.  
     Catalog changes require a new `release_id` (§3.1).

### **Invariants (applies to every HG computation)**

* **Deterministic & pure.** No time, network, randomness, or file I/O.

* **AB↔BA symmetry.** Outputs for **AB** equal those for **BA** after normalization.

* **Closed vocabularies.** Only cataloged channel/gate IDs and fixed enums may appear; no free text.

* **Numeric-free outputs.** HG does **not** emit scores or counts to public surfaces.

### **Detection (conceptual rules)**

1. **Complement formation (cross-person).**

   * If **A** contributes gate *g₁* and **B** contributes gate *g₂*, and `{g₁,g₂}` exactly matches a cataloged channel *C*, then **one** HG complement is detected for *C*.

   * Two gates **from the same person** do **not** form an HG complement (that is a defined channel, not HG).

2. **Per-channel set semantics.**

   * Multiple occurrences that resolve to the **same** channel *C* produce a **single** HG item.

3. **Center consistency.**

   * Detected complements must respect the catalog’s center assignments; mismatches **fail closed**.

4. **Ambiguity guard.**

   * If catalogs/aliases yield multiple candidate channels for the same `{g₁,g₂}`, the detector returns a typed failure (see **Typed failures**) rather than guessing.

### **Optional sub-flags (catalog-gated)**

* **Center flags.** Catalog may define optional center tags (e.g., “G-identity HG present”) that the detector may set as **booleans/enums**.

* **Topology hints.** If the catalog declares a special topology hint relevant to HG (e.g., “bridge to throat present”), the detector may set a **bounded enum**.

Names and allowed values for any sub-flags are pinned by the catalog schema; this spec constrains behavior (determinism, symmetry, closure), not field lists.

### **Output (engine-facing; example shape)**

{

  "hg": {

    "present": true,

    "channels": \["\<catalog\_channel\_id\>", "..."\],

    "centers": \["\<center\_id\>", "..."\]   // optional, if catalog-gated

  }

}

* **No counts/scores** are required for HG; aggregation may reference only **presence** and **catalog IDs/enums**.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — inputs malformed or prerequisite data missing (e.g., unknown gate code, invalid normalization).

* **CATALOG\_MISMATCH** — gates reference channels not present in the active freeze pack.

* **AMBIGUOUS\_COMPLEMENT** — `{g₁,g₂}` maps to more than one catalog channel due to aliasing; detector fails closed.

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** HG outputs identical for AB and BA.

* **Two-run identity.** Recomputing HG with the same inputs/catalog yields byte-identical feature records.

* **Catalog coverage.** Goldens demonstrate detection across representative channels and centers (including negative/edge cases).

* **Fail-closed proofs.** Goldens show that ambiguous/unmapped pairs return typed failures (no partial HG items).

### **Change control**

* Any change to **gate→channel maps**, **center topology**, or **HG flag enums** is a math-catalog change and requires a **new `release_id`** (§3.1); regenerate acceptance artifacts accordingly.

### **Public surface rule**

* HG outputs remain **internal-only**; Reader v1 exposes **no** HG-derived numerics or narratives (§2.2).

### **Routing**

* Transport/CLI validators, status/headers, and admin behaviors are **not** restated here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

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

**Note:** The precise conditions that trigger **dominant** or **compromise** are pinned by the catalog schema; this spec constrains behavior (determinism, symmetry, closed enums), not rule text.

### Optional sub-flags (catalog-gated)

* **Actor indication.** If the catalog allows, a bounded field may indicate **which** participant is dominant (e.g., `dominant_actor: "min"|"max"` or equivalent, aligned to the normalized pair notion).

* **Topology hints.** Catalog may define additional bounded hints (e.g., `compromise_mode: <enum>`).

* **All sub-flags are optional**, strictly enumerated, and versioned with the catalog.

### Output (engine-facing; example shape)

{

  "center\_tags": \[

    { "center": "\<center\_id\>", "tag": "dominant",   "dominant\_actor": "min" },

    { "center": "\<center\_id\>", "tag": "compromise", "compromise\_mode": "\<enum\>" },

    { "center": "\<center\_id\>", "tag": "neutral" }

  \]

}

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

{

  "throat\_adj": {

    "talk\_ladder": "\<enum-or-none\>",

    "nar\_adj": "\<enum-or-none\>",

    "direct\_mt": true

  }

}

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

{

  "em\_timing": {

    "state": "\<enum\>",          // e.g., "paced" | "not\_paced" | \<catalog\_state\>

    "dampen": true,             // boolean; instructs aggregation to reduce certain contributions

    "reason": "\<enum-or-none\>"  // optional, catalog-bounded rationale for dampening

  }

}

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

Names and allowed values are **pinned by the catalog schema**; this spec constrains behavior (determinism, symmetry, closure), not field lists.

### **Output (engine-facing; example shape)**

{

  "families": \[

    { "id": "g\_identity", "state": "\<enum\>", "over\_concentration": false },

    { "id": "tribal\_care", "state": "\<enum\>" },

    { "id": "rhythm",      "state": "\<enum\>" },

    { "id": "story",       "state": "\<enum\>" },

    { "id": "mind",        "state": "\<enum\>" }

  \]

}

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

## **6.7 Planetary micro (B-only, tiny cap) \[Speculative\]**

**Purpose (normative).**  
 Detect **planetary micro** signals for a normalized pair and emit **bounded, deterministic** feature flags for *internal* aggregation. Planetary micro is **preset-gated (B-only)** and subject to a **tiny cap** defined in the freeze-pack catalogs/presets. Reader v1 remains numeric-free and bands-only (§2.2).

### **Inputs (closed & validated)**

* **Pair-normalized charts.** All detection consumes the **normalized** (order-neutral) pair.

* **Frozen catalogs & presets.** The freeze pack (§5.4) defines:

  * A **micro catalog** (closed IDs/enums) and matching rules.

  * The **B-preset** gating (micro considered only when preset B is active).

  * The **tiny cap policy** (catalog/preset directive limiting how many micro tokens the aggregation layer may consider).  
     Any change requires a new `release_id` (§3.1).

### **Invariants**

* **Deterministic & pure.** No time, network, randomness, or file I/O.

* **AB↔BA symmetry.** Outputs identical for AB and BA after normalization.

* **Closed vocabularies.** Only cataloged micro IDs/enums; **no free text**.

* **Numeric-free extractor output.** The detector emits **booleans/enums only**; any cap application occurs in aggregation (§7–§8).

### **Detection (conceptual rules)**

1. **Preset gate (B-only).**

   * If the active preset is not **B**, **no micro output** is produced.

2. **Micro token resolution.**

   * Apply catalog rules to derive a **set** of micro tokens (closed IDs/enums).

   * Resolve aliases strictly to catalog IDs; duplicates collapse (set semantics).

3. **Tiny cap semantics (aggregation-facing).**

   * The detector **does not count** or trim numerically; it can set an **advisory enum/flag** indicating that micro is *cap-eligible*.

   * The **cap** is enforced by aggregation (e.g., “consider at most *N* micro tokens”), never by emitting numeric counts here.

### **Output (engine-facing; example shape)**

{

  "planetary\_micro": {

    "present": true,

    "tokens": \["\<micro\_id\>", "..."\],   // closed IDs; set semantics

    "cap\_eligible": true,              // indicates that preset B’s tiny-cap rule applies

    "preset\_gate": "B"                 // optional, catalog-bounded enum

  }

}

* Field names and enums are **pinned by the catalog schema**; the example is illustrative.

* No numeric counts are emitted by this detector.

### **Typed failures**

* **FEATURES\_UNAVAILABLE** — prerequisites missing/invalid; micro cannot be resolved deterministically.

* **CATALOG\_MISMATCH** — referenced micro IDs or rules not present in the active freeze pack.

* **AMBIGUOUS\_MICRO** — multiple conflicting tokens without catalog precedence; detector **fails closed**.

### **Determinism & acceptance (when wired)**

* **AB↔BA parity proof.** Identical `planetary_micro` for AB and BA.

* **Two-run identity.** Re-running with the same inputs/catalog yields byte-identical outputs.

* **Catalog coverage.** Goldens demonstrate positive/negative micro resolution across representative cases.

* **Cap adherence (aggregation tests).** Aggregation goldens verify that, when `cap_eligible` and preset B are active, **no more than the tiny-cap limit** contributes to scoring (cap value owned by preset/catalog).

### **Change control**

* Any change to **micro IDs/enums**, **resolution rules**, or **cap posture** (including the “B-only” gate) is a math-catalog/preset change and requires a **new `release_id`** (§3.1); regenerate acceptance evidence accordingly.

### **Public surface rule**

* Planetary micro is **internal-only**. No micro-derived numerics or narratives appear on Reader v1 (§2.2).

### **Routing**

* Transport/CLI validators, status/headers, and admin streams are **not restated** here and are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

# **7\. Presets & Configuration (A/B) \[Speculative\]**

## **7.1 Preset catalog (validated; freeze-pack member) \[Speculative\]**

**Purpose (normative).**  
 Define a **frozen, validated catalog** of presets that parameterize internal scoring/aggregation without changing the public Reader covenant (numeric-free; bands-only). The preset catalog is a **member of the freeze pack** (§5.4); any change requires a new `release_id` (§3.1).

### **7.1.1 Catalog membership & keys (closed)**

* **Entries:** each preset is an object with a **stable `id`** (ASCII lowercase, `^[a-z0-9._-]{1,32}$`) that is **unique** within the catalog.

* **A/B scope:** at minimum, the catalog may contain **A** and **B** families; additional presets are allowed but must follow the same schema.

* **No aliases:** a preset `id` maps to **exactly one** entry; aliasing is forbidden.

### **7.1.2 Schema (validation rules)**

Each preset **MUST** validate against a canonical JSON schema (part of the freeze pack) with, at minimum, the following fields:

* **`id`** *(string)* — unique key, stable across releases unless intentionally versioned.

* **`description`** *(string, optional)* — short, non-normative note; no functional effect.

* **`weights`** *(object)* — **exact** Magic-10 keys (§5.1), each an **integer 0..100**. Missing/extra keys are invalid.

* **`caps` / `floors`** *(object, optional)* — bounded integers or closed enums controlling per-family/category capping/flooring; keys must be from closed vocabularies.

* **`dampeners`** *(object, optional)* — closed enums or booleans specifying over-concentration guards and other reduction rules (no free text, no floats).

* **`cross_family`** *(object, optional)* — closed-enum hints for cross-family corrections (e.g., small penalties) interpreted deterministically by aggregation (§8).

* **`micro`** *(object, optional)* — planetary-micro posture (e.g., `gate: "B"`, `cap_eligible: true`) using only closed enums/booleans.

* **`rounding`** *(string, optional)* — if present, **must** be `"half_up"` to align with fixed-point rules (§5.2.5).

* **`enabled`** *(boolean, default `true`)* — preset availability flag for runtime selection.

**Validation is binary:** failure of any rule rejects the entire catalog build and therefore blocks the freeze pack.

### **7.1.3 Determinism & neutrality**

* **AB↔BA identity:** presets **must not** depend on person order; applying a preset to AB and BA yields identical per-category integer scores prior to band mapping (§5.3).

* **Two-run identity:** with the same inputs and freeze pack, recomputation under a given preset yields **bit-identical** integer scores.

* **No floats:** presets may not introduce floating-point sensitivity; all arithmetic resolves via fixed-point rules and **round half-up** (§5.2.5).

  ### 7.1.4 Selection & precedence (concept)

* **Selection.** The caller (CLI/adapter) selects **exactly one** preset (or none) for a computation; default behavior (when omitted) is defined **outside** this section.

* **Viewer weights coexistence.** When both **viewer weights** and a **preset** are provided, a **deterministic precedence policy** **MUST** govern how they combine (e.g., “preset base weights, viewer deltas,” or “viewer overrides”). This spec requires **one pinned policy** and **does not restate it here**.  
   **Routing (titles-only):** the precedence policy is owned in **PF-Canon-HDE-CLI-API-Vendor-Ref** (see “Preset vs Viewer Weights”). 

### **7.1.5 Change control (new `release_id`)**

Any of the following **requires** a new `release_id` (§3.1):

* Adding/removing a preset or changing any preset field (`weights`, `caps/floors`, `dampeners`, `cross_family`, `micro`, `rounding`, `enabled`).

* Modifying the preset JSON schema such that canonical bytes change.

* Changing Magic-10 IDs (§5.1) or thresholds (§5.3) referenced by presets.

### **7.1.6 Acceptance (binary)**

* **Schema validation:** every entry passes the canonical JSON schema; **exact** Magic-10 coverage in `weights`.

* **Determinism proofs:** AB↔BA parity and two-run identity hold for representative inputs under each preset.

* **Clamp/rounding proofs:** boundary fixtures demonstrate half-up rounding and clamp to `[0..100]` (§5.2.4–§5.2.5).

* **Catalog closure:** all referenced IDs/enums (families, micro, dampeners) resolve within the same freeze pack.

* **No public drift:** public Reader bodies remain numeric-free; presets affect **internal** scores only.

### **7.1.7 Routing (no transport bytes)**

* HTTP headers, CLI flags/defaults, and validator streams are **not** restated here; they are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **7.2 Closed vocab (magnitude map; sign policy) \[Speculative\]**

**Purpose (normative).**  
 Define a **closed vocabulary** that links detector outputs (e.g., EM/HG/family flags) to **bounded, deterministic** arithmetic knobs used by presets and aggregation. The vocabulary is split into two parts: a **magnitude map** (how much a token can contribute) and a **sign policy** (whether a token’s contribution is additive or subtractive). This catalog is part of the **freeze pack** (§5.4); any change requires a new `release_id` (§3.1).

### **7.2.1 Vocabulary membership (closed)**

* **Token IDs.** Each arithmetic token (e.g., a feature flag, family hint, or coupling hint) has a **stable ASCII ID** (`^[a-z0-9._-]{1,32}$`), unique within the vocab.

* **No aliases.** A token ID maps to **one** semantic meaning; aliasing is forbidden.

* **Scopes.** Tokens may be grouped by scope (e.g., `em.*`, `hg.*`, `family.*`) for validation only; scopes carry no arithmetic semantics.

### **7.2.2 Magnitude map (deterministic, bounded)**

* **Definition.** The magnitude map assigns each token ID a **bounded magnitude** chosen from a **closed set** pinned in the catalog (e.g., an enum or a small integer domain).

* **Fixed-point only.** Magnitudes are encoded as **integers** or **closed enums**; no floats.

* **Monotonicity.** If a preset increases the magnitude for a token, downstream scoring **MUST NOT** produce a smaller contribution for that token, all else equal.

* **Fold rule (set semantics).** When multiple detections yield the **same token**, the catalog declares a **commutative, associative** fold operator (e.g., **max** or **bounded sum**) so that AB↔BA and two-run identity hold. The fold operator is part of the vocab definition.

* **Caps/floors.** Any caps/floors that constrain magnitudes across a set of tokens are specified in the **preset** (see §7.1) or the **aggregation** layer (see §8), not here; the vocab only declares token-level magnitudes.

### **7.2.3 Sign policy (closed)**

* **Definition.** Each token maps to a **sign** from a closed enum (e.g., `pos | neg | neutral`), indicating how aggregation interprets the token’s effect.

* **No dynamic signs.** Sign is **cataloged**, not computed at runtime. If a token needs contextual inversion, the catalog must use **distinct IDs** for the inverted case.

* **Neutral tokens.** Tokens marked `neutral` may be used as **gates** (e.g., enabling bonuses elsewhere) without direct arithmetic weight.

### **7.2.4 Selector/priority rules (conflict resolution)**

* **Priority.** If two tokens are **mutually exclusive** by design, the catalog declares a **priority order**; the lower-priority token is ignored when both appear.

* **Shadowing.** A high-priority token may **shadow** a set of lower-priority tokens; shadowed tokens are dropped **before** folding.

* **Canonicalization.** Priority/shadowing rules are **order-independent** and **deterministic** (commutative, associative), ensuring AB↔BA identity.

### **7.2.5 Validation (binary)**

* **Closure.** Every token referenced by detectors, presets, or aggregation **MUST** be present in the vocab; unknown tokens are invalid.

* **Deterministic fold.** The fold operator for duplicate tokens **MUST** be declared and proven commutative/associative in acceptance (see §11).

* **Sign/magnitude coherence.** Each token **MUST** have exactly one sign and one magnitude (or enum equivalent).

* **Domain bounds.** Magnitudes and signs **MUST** be drawn from their closed domains; out-of-range values fail validation.

### **7.2.6 Determinism & neutrality**

* **AB↔BA identity.** Because token formation (detectors) and token folding (vocab rules) are order-invariant, AB and BA yield identical token-to-weight outcomes.

* **Two-run identity.** Re-running with the same inputs and freeze pack yields byte-identical token sets and folded magnitudes.

* **No floats / locale.** No floating-point or locale-sensitive operations are permitted in vocab interpretation.

### **7.2.7 Change control (new `release_id`)**

* Adding/removing a token, changing a token’s **magnitude**, **sign**, **fold operator**, or **priority/shadowing** rules, or altering domain enums is a **math change** and **requires** a new `release_id` (§3.1).

* Any downstream preset or aggregation that references vocab entries **must** be updated in lockstep (schema validation enforces closure).

### **7.2.8 Routing (no transport bytes)**

* This section defines **math vocab** only. Transport/CLI behavior (flags/defaults, validators, headers) is referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

**Implementation note (informative).** Vocab resolution occurs **before** preset arithmetic in §7 and **before** aggregation folds in §8; the vocab establishes the **deterministic, bounded** building blocks (token → magnitude, sign) that those layers consume.

## **7.3 Caps & floors; dampeners (halve-penalty; over-concentration) \[Speculative\]**

**Purpose (normative).**  
 Provide **bounded, deterministic** controls that shape internal scores **without** introducing public numerics. Controls are of three kinds:

1. **Caps** — upper bounds on intermediate or final per-category contributions.

2. **Floors** — lower bounds that prevent collapse of a contribution.

3. **Dampeners** — reductions applied under cataloged conditions (e.g., **over-concentration**), including a **halve-penalty** effect.

All knobs are defined by **closed enums/integers** in the **preset catalog** (§7.1) and/or the **closed vocab** (§7.2), and are part of the **freeze pack** (§5.4). Any change requires a new `release_id` (§3.1).

---

### **7.3.1 Deterministic application order (fixed)**

For any category’s internal contribution, the engine **MUST** apply controls in the following **canonical order**:

1. **Token fold** (set semantics from §7.2; commutative/associative)

2. **Magnitude \+ sign** (from the closed vocab in §7.2)

3. **Dampeners** (e.g., halve-penalty, oc-guard)

4. **Floors**

5. **Caps**

6. **Clamp to `[0..100]`** and **round half-up** where required (see §5.2.5)

This order is **normative** and must be used everywhere such controls are evaluated to guarantee AB↔BA identity and two-run identity.

---

### **7.3.2 Caps (upper bounds)**

* **Definition.** A **cap** is a preset-declared upper bound that limits a **category** (or a **family subtotal** if explicitly declared) after dampeners/floors are applied.

* **Domain.** Caps are **integers** or **closed enum levels** (e.g., `low|mid|high → {n₁,n₂,n₃}`), never floats.

* **Effect.** `val' = min(val, CAP)`; then clamp to `[0..100]`.

* **Scope.** Caps **must** name an unambiguous target (category or family); ambiguous or overlapping caps are invalid at validation time.

---

### **7.3.3 Floors (lower bounds)**

* **Definition.** A **floor** is a preset-declared lower bound that prevents a contribution from collapsing below a cataloged minimum **after** dampeners.

* **Domain.** Floors are **integers** or **closed enum levels**; never floats.

* **Effect.** `val' = max(val, FLOOR)`; then clamp to `[0..100]`.

* **Coherence.** If `FLOOR > CAP`, validation **fails** (catalog/preset must be coherent).

---

### **7.3.4 Dampeners (including halve-penalty)**

* **Definition.** A **dampener** reduces a contribution under cataloged conditions (e.g., **over-concentration** within a family, pacing not satisfied; see §6.5).

* **Domain.** Dampeners are **closed enums** with pinned effects; at minimum:

  * `none` — no reduction

  * `halve` — **halve-penalty**

  * (optional) additional bounded modes, e.g., `reduce_25`, `reduce_33`, etc., **only** if declared in the freeze pack

* **Effect (fixed-point).** If mode is `halve`:

  * `val' = round_half_up(val * 0.5)`; then clamp to `[0..100]`.

  * Other modes (if present) use **integer** fixed-point recipes pinned by the catalog (e.g., `val * 3 / 4` with round half-up).

* **Triggering.** Dampeners are **not** inferred at runtime; they are triggered strictly by **closed conditions** (e.g., a family’s **over-concentration** flag, or `em_timing.dampen==true`), both defined by detectors/presets and validated in the freeze pack.

---

### **7.3.5 Over-concentration guard (oc-guard)**

* **Intent.** Prevent a single family or narrow signal cluster from dominating totals.  
* **Trigger.** The oc-guard applies when the **family record count \> 3** for the named family/scope, computed **after de-duplication/folding** (set semantics) and validation against the active freeze pack. If the count ≤ 3, the guard does not apply.  
* **Effect (normative).** Multiply that family’s subtotal by **0.75** using half-unit fixed-point arithmetic and **round away-from-zero**, then proceed to floors and caps (see §8.2 for the canonical order). **Apply at most once per family per computation.**  
* **No counts.** The guard is modeled as a flag, not a numeric quota; caps/floors enforce bounds without emitting counts.

**Change control.** Any change to the oc-guard factor, its **trigger threshold**, or its scope is a math change and requires a new `release_id` (see §5.4).

---

### **7.3.6 Validation (binary)**

* **Closure.** Every cap/floor/dampener **MUST** reference a **known** category/family and a **declared** mode/value.

* **Coherence.** For each scoped target, `0 ≤ FLOOR ≤ CAP ≤ 100`; otherwise the catalog **fails** validation.

* **Determinism.** The same inputs and preset produce **bit-identical** integers after applying dampeners, floors, and caps; AB↔BA identity holds.

* **Rounding proof.** Goldens cover half-up rounding at key boundaries (e.g., 0.5, 12.5, 87.5) and demonstrate clamp to `[0..100]`.

---

### **7.3.7 Change control (new `release_id`)**

Any of the following is a **math change** requiring a new `release_id` (§3.1):

* Adding/removing/updating any **cap**, **floor**, or **dampener** declaration.

* Changing the **fixed-point recipe** for a dampener mode (e.g., redefining `halve`).

* Altering the **application order** or scope mapping.  
   All affected acceptance artifacts must be regenerated.

---

### **7.3.8 Non-goals / routing**

* No HTTP/CLI payloads, headers, or validator streams are restated here; such details are referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**.

* This section defines **math controls** only; public Reader v1 remains numeric-free and bands-only (§2.2).

## **7.4 Planetary micro policy (B only; cap\_total=+3) \[Speculative\]**

**Purpose (normative).**  
 Constrain how **planetary micro** contributes to **internal** totals under **Preset B**. Public Reader v1 remains **numeric-free** and **bands-only** (§2.2); micro never appears on the public surface.

### **7.4.1 Gating & scope**

* **Preset gate (B-only).** Planetary micro is **considered only** when the active preset is **B**. If the active preset ≠ B, planetary micro contributes **nothing** (regardless of detector outputs).

* **Detector → aggregation boundary.** The detector emits **tokens** and a boolean/enum posture (e.g., `cap_eligible`) **without counts** (§6.7). All **counting and capping** occurs **only** in aggregation (this section).

### **7.4.2 Tiny cap on total contribution**

* **Cap constant.** `cap_total = +3` micro tokens maximum **may contribute** to aggregation when preset **B** is active.

* **No public numerics.** The cap is an **internal rule**; it never appears in public payloads.

* **Deterministic selection.** If more than three micro tokens are available, choose the contributing set **deterministically** using the closed, order-independent priority rules from the vocab (§7.2.4) and/or preset schema (§7.1):

  1. **Priority/shadowing:** apply shadowing first (higher-priority tokens keep, shadowed tokens drop).

  2. **Magnitude tie-break:** if still \>3, pick the three with highest cataloged **magnitude**; if magnitudes tie, fall back to the **stable token ID order** (ASCII ascending).  
      These rules are **normative** and must yield the same selection for AB and BA (commutative/associative).

### **7.4.3 Integration with aggregation pipeline**

* **Where applied.** The cap is enforced **after** token fold and sign/magnitude resolution (§7.2) and **before** preset caps/floors (§7.3).

* **Effect.** At most three micro tokens advance to the subsequent steps; all others are **ignored** for that computation. No partial weighting is applied to the ignored tokens.

* **Fixed-point arithmetic.** Any contribution from the selected tokens remains integer/fixed-point per §5.2; round **half-up** and clamp to `[0..100]` as required.

### **7.4.4 Determinism & neutrality**

* **AB↔BA identity.** Because selection uses order-independent priority/shadow rules, the same three tokens (or fewer) are chosen for **AB** and **BA**.

* **Two-run identity.** With the same inputs, catalogs, and preset, recomputation yields identical selected tokens and identical integer contributions.

* **No floats / locale.** No floating-point or locale-sensitive operations are permitted.

### **7.4.5 Validation (binary)**

* **Closure:** all selected tokens **must** exist in the micro vocab (§6.7) and closed vocab (§7.2).

* **Cap proof:** acceptance fixtures show that when \>3 micro tokens are available under preset **B**, exactly three are selected via the deterministic rules; when ≤3 exist, all are selected.

* **Parity proof:** AB vs BA selection and totals are identical; two identical runs produce identical selections and totals.

### **7.4.6 Change control**

* Any change to **cap\_total** (e.g., from `+3` to another value), to the **selection priority**, or to the **gating preset** is a math/preset change and **requires** a new `release_id` (§3.1). Re-generate acceptance artifacts accordingly.

### **7.4.7 Public surface rule**

* Planetary micro remains **internal-only**. Reader v1 exposes **no** micro-derived fields or numerics; presets influence **internal** totals only.

  ## **7.5 Feature primitives (v1) & loader invariants \[Required-Now\]**

**Purpose (normative).** Define the v1 feature primitives consumed by category scoring (§5.2) and the loader invariants that guarantee deterministic, pack-driven, channel-scoped extraction. These are **math inputs**; public output remains **numeric-free** (bands only). Transport/ops are out of scope (titles-only to **HDE-CLI-API-Vendor Ref** / **HDE-Governance**).

### **7.5.1 Source of truth & inputs (titles-only)**

* **Topology & vocabularies.** `centers.json`, `gates.json`, `channels.json` (see **HDE-Schemas and Artifacts §2.1**). Channel identity is canonical `NN-NN` (min→max, zero-padded); centers are `snake_case`; Title Case is an ingestion alias only.  
* **Constants pack.** `limits.*` and `bands.thresholds` (see §5.4.2; **HDE-Schemas and Artifacts §6**) — these are **frozen** and used as divisors and parameters.  
   *Note:* Resonance/diagnostic inputs are not in the v1 constants pack (see §5.6).  
* **Composite.** All primitives are computed on the **normalized AB composite** (see **HDE-Schemas and Artifacts §2.1**) so that **AB \= BA** (see §7.5.4).  
* **Channel-level scope & classification (normative).**  
  * **Per-channel semantics.** “Channel” means the channel **edge** (canonical `NN-NN`), not “gate-pair” or a center. Junction gates (10, 20, 34, 57\) can appear in multiple channels; each channel is evaluated independently.  
  * **Classification set (pairwise-disjoint).** For each channel, compatibility class is **exactly one of** `{ companion, compromise(A→B), compromise(B→A), EM, null }`. The compromise direction is part of the class.  
  * **Arrays-as-sets.** When aggregating over channels, treat inputs as a set of canonical identities (dedupe by `NN-NN`; ASCII-sort for determinism; see §4.2). EM/Compromise are counted **per-channel** (e.g., `20-34` and `20-57` are distinct).

  ### **7.5.2 Normalization & null-handling (normative)**

* **Raw → normalized.** Unless stated otherwise, each primitive’s raw value is mapped to a unit interval by a **pack-frozen divisor** `D > 0`, producing `F = clamp(raw, 0, D) / D ∈ [0,1]`. Where a primitive uses a named divisor from the constants pack (e.g., `limits.em_max`), that divisor is **normative and frozen**.  
* **Null default.** If a raw component is missing/unknown, apply **null → 0** unless the feature’s **Feature Registry** row declares a different `null_handling` (`"ignore"` or `"floor"`) (registry lives in **HDE-Schemas and Artifacts**, titles-only).  
* **Integerization boundary.** Category aggregation and banding use §5.2 (`round_half_up`) **after** weighting; primitives themselves stay in `[0,1]` (or `{0,1}` for booleans).  
* **Channel set discipline.** Any intermediate/output array of channel IDs used as a **set** MUST be deduplicated and ASCII-sorted by canonical `NN-NN` (§4.2). EM/compromise counts are **per-channel**, never per-gate.

  ### **7.5.3 Primitive definitions (v1, no public numerics)**

Each item is identified by its feature id `F.<snake_case>`, with raw definition, normalization, and constraints.

1. **F.EM\_TOTAL — total cross-person electromagnetics (completed A–B channels)**

   * **Raw:** `raw = |{ ch : ch connects two centers AND is completed by opposite ownership across A/B }|`. Count **per channel** (canonical `NN-NN`); do **not** merge distinct channels that share a gate (e.g., `20-34` vs `20-57`).  
   * **Normalizer:** `D = limits.em_max` *(pack-frozen)*.  
   * **Normalized:** `F = min(raw, D) / D ∈ [0,1]`.  
   * **Notes:** “Completed” means both endpoints present in the composite and owned by opposite members.  
2. **F.HAS\_THROAT\_EM — any A–B EM touching throat**

   * **Raw:** indicator: `1` if ∃ completed `ch` with `throat ∈ endpoints(ch)`, else `0`.  
   * **Normalized:** `F = raw ∈ {0,1}` (boolean).  
   * **Scope:** EM detected **per channel**; a single EM on `20-57` satisfies the indicator independent of `20-34`.  
3. **F.CENTERS\_CO\_DEFINED — centers simultaneously defined by both A and B**

   * **Raw:** `raw = |{ c ∈ Centers : c ∈ Defined(A) ∧ c ∈ Defined(B) }|`.  
   * **Normalizer:** `D = limits.centers_max` *(pack-frozen; typically 9\)*.  
   * **Normalized:** `F = raw / D ∈ [0,1]`.  
4. **F.MIND\_TO\_THROAT — direct Mind→Throat completions**

   * **Mind set:** `{head, ajna}`; **Throat:** `throat`.  
   * **Raw:** number of **direct completed** composite channels whose endpoints are `(head|ajna) ↔ throat`.  
   * **Normalizer:** `D = limits.mind_throat_max` *(pack-frozen, ≥ 0\)*.  
   * **Normalized:** `F = (D == 0) ? 0 : min(raw, D) / D`.  
   * **Notes:** **Direct-only** (no 2-hop paths); per-channel counting; channel IDs are canonical `NN-NN`.  
5. **F.MOTOR\_TO\_THROAT — direct Motor→Throat completions (v1 direct-only)**

   * **Motor set:** `{ego, sacral, solar_plexus, root}`; **Throat:** `throat`.  
   * **Raw:** number of **direct completed** composite channels whose endpoints are `(motor) ↔ throat`.  
   * **Normalizer:** `D = limits.motor_throat_max` *(pack-frozen, ≥ 0\)*.  
   * **Normalized:** `F = (D == 0) ? 0 : min(raw, D) / D`.  
   * **Notes:** **Direct-only** in v1 (see §5.4.2.1); do **not** count 2-hop routes; per-channel counting.  
6. **F.COMP\_WHOLLY\_OWNED\_PENALTY (aka F.COMPROMISE\_PENALTY) — penalize “wholly one-sided” full channels**

   * **Raw:** `comp = |{ ch : ch completed in composite AND both gates from the same member }|` (per channel).  
   * **Parameter:** `limits.comp_max` *(pack-frozen)* caps the count in normalization.  
   * **Normalized:** `F = 1 − min(comp, limits.comp_max) / limits.comp_max` *(if `limits.comp_max == 0`, define `F = 1`)*.  
   * **Range:** `[0,1]`, where `1` \= no one-sided completions; lower values indicate “more compromise”.

**Registration in the Feature Registry (titles-only).** Each `F.*` appears in the **Feature Registry** (in **HDE-Schemas and Artifacts**) with fields `{ feature_id, normalizer_divisor, lower_bound, upper_bound, null_handling, notes }`. For channel-scoped features, the registry key MUST be the canonical `NN-NN` `channel_id`; junction gates may yield multiple rows (one per channel). For `F.MIND_TO_THROAT` and `F.MOTOR_TO_THROAT`, set `normalizer_divisor` to `limits.mind_throat_max` / `limits.motor_throat_max`. Default `null_handling: "zero"` unless otherwise frozen.

### **7.5.4 Determinism & identity (normative)**

* **AB↔BA identity.** Primitives are computed **after** composite normalization; swapping A/B does not change any raw or `F`.  
* **Two-run identity.** Identical inputs \+ identical pack ⇒ identical primitives and downstream scores/bands (see **HDE-Schemas and Artifacts §4**; run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`).  
* **No transport dependence.** Primitives depend only on governed math inputs; transport headers/cache/timeouts are irrelevant.

  ### **7.5.5 Validation & CI (titles-only)**

* **Binary/value domains.**  
  * Booleans: `{0,1}`; normalized features: `F ∈ [0,1]`.  
  * **Divisors equal the pack-frozen constants; no runtime overrides.**  
  * `null_handling` obeys the Feature Registry.  
  * Channel collections are sets (dedupe \+ ASCII-sort by `NN-NN`); EM/compromise counted **per channel**.  
* **Acceptance tokens:**  
   `CATALOG_DENOMINATORS_FROZEN_OK`, `FEATURE_NULL_DEFAULT_OK`,  
   `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`.  
   *(Token names live in HDE-Governance §2.0.)*

  ### **7.5.6 Routing (no transport bytes here)**

All HTTP/CLI concerns (headers, streams, validators, error envelopes) are owned by **HDE-CLI-API-Vendor Ref** / **HDE-Governance** and are referenced by title only.

---

## **7.6 Magic-10 feature registry (D3/D3b shapes & “overrides only”) \[Required-Now\]**

**Purpose (normative).** Pin the data shapes and loading semantics for the per-feature constants that drive category scoring (§5.2). These are **math inputs** serialized in the pack (see **HDE-Schemas and Artifacts §2.6, §6**). The pack stores **overrides only**; any “resolved” tables shown in this spec are non-normative views derived from the pack.

**Frozen-input coupling.** Any change to populated divisors / bounds / weights, or to these shapes, is a frozen-input change and **requires a new `release_id`** (see **HDE-Schemas and Artifacts §6**; §3.1).

### **7.6.1 D3 — Divisors & bounds (shape; overrides only)**

Each category may override the default normalization of any feature. Omitted features inherit the base/default from the pack; if no base is present, the engine treats the divisor as required by the feature’s definition (or as `1` only where explicitly allowed by §7.5).

**Shape (JSON, canonical; comments shown here in prose):**

{

  "magic10": {

    "divisors": {

      "\<category\_key\>": {

        "\<feature\_id\>": \<number\>

      }

    },

    "bounds": {

      "\<category\_key\>": {

        "\<feature\_id\>": {

          "min":  \<number or null\>,

          "max":  \<number or null\>,

          "null": "zero" | "ignore" | "floor"

        }

      }

    }

  }

}

**Rules (normative)**

* **Divisors** are positive and finite; when a primitive specifies a pack key (for example, `limits.em_max`), the override **must** reference that pack-frozen divisor (§7.5).  
* If both `min` and `max` are present, then `min ≤ max`.  
* **Null handling** defaults to `zero` unless overridden:  
   `zero` → substitute `0` before normalization;  
   `ignore` → exclude the feature from category aggregation for that item;  
   `floor` → substitute `min` before normalization.  
* Pack JSON is **canonical** (see **HDE-Schemas and Artifacts §4**): UTF-8 (no BOM), sorted keys, compact, one trailing `\n`.

### **7.6.2 D3b — Weight vectors `W_c` (shape; AWAITING VALUES)**

Per category, the pack contains **only non-zero overrides**; missing features implicitly take weight `0` unless a template (T1–T5) supplies an editorial seed. Templates are **not** normative; the frozen weights in the pack are.

**Shape (JSON, canonical):**

{

  "magic10": {

    "weights": {

      "\<category\_key\>": {

        "\<feature\_id\>": \<number\>

      }

    }

  }

}

**Notes (v1)**

* **No auto-normalization.** Weights are used exactly as frozen; the engine does **not** renormalize sums to `1`.  
* **Templates (T1–T5).** May guide authoring; the pack’s concrete weights are the **only** normative source.  
* **Status.** `weights` content is **AWAITING VALUES**; when populated and manifested, it becomes frozen and bumps `release_id`.

### **7.6.3 Registration & linkage to primitives**

For every feature `F.<…>` consumed by any category (§7.5), the registry **must** provide a D3/D3b row wherever that feature participates:

* **Divisor linkage.** If a primitive’s normalization is defined against a pack key (for example, `limits.em_max`, `limits.mind_throat_max`, `limits.motor_throat_max`, `limits.centers_max`, `limits.comp_max`), the D3 `divisors` entry **must** match that key’s value when overridden.  
* **Bounds & null policy.** If a primitive requires clamping or non-zero floor/ignore semantics, encode them in D3 `bounds` for each category that differs from the base/default.  
* **Keys & IDs.** Use `snake_case` identifiers for `<category_key>` and `<feature_id>`. Category keys **must** come from the frozen Magic-10 IDs (see **HDE-Schemas and Artifacts §2.6**; §5.1). Feature IDs **must** match §7.5.  
* **Channel-scoped features.** When a primitive is channel-scoped (§7.5), D3/D3b still keys by `<feature_id>` at the **category** row; channel identity (`NN-NN`) is carried by extraction and set-handling rules in §7.5. (Divisors/bounds/weights typically remain category-level.)

### **7.6.4 Determinism & identity**

* **AB↔BA identity.** Features are extracted from the **normalized composite** (see **HDE-Schemas and Artifacts §2.1**); swapping A/B does not change feature values.  
* **Two-run identity.** Given identical inputs and identical pack contents, two runs produce byte-identical category inputs and downstream aggregates (§5.2).  
* **Environment pins.** All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC` (see **HDE-Schemas and Artifacts §4**).

### **7.6.5 Validation & CI (titles-only)**

* **Schema/shape:** `JSON_CANONICAL_CHECK_OK`  
* **Limits coupling:** `CATALOG_DENOMINATORS_FROZEN_OK` (divisors referencing `limits.*` match pack)  
* **Population (when filled):** `EVIDENCE_INDEX_UPDATED_OK`, `RELEASE_ID_RECOMPUTE_OK`  
* **Determinism:** `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`

### **7.6.6 Routing (no transport bytes here)**

All transport/ops concerns (headers, validators, streams) are owned by **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (referenced by title only).

* 

# **8\. Aggregation Algorithm (deterministic, fixed-point) \[Speculative\]**

## **8.1 Per-signal scoring (magnitude×sign; throat-EM bonus; halve-penalty) \[Speculative\]**

**Purpose (normative).**  
 Convert detector outputs (tokens) into **integer contributions** per category using a deterministic, fixed-point pipeline. Each token contributes according to a **closed magnitude** and **sign** (§7.2), optional **bonus gates** (e.g., throat-EM), and **dampeners** (e.g., halve-penalty) (§7.3). All arithmetic is **order-neutral (AB↔BA)**, **two-run identical**, and **numeric-free on public surfaces** (§2.2).

### **8.1.1 Inputs (closed & validated)**

* **Token set:** deduplicated, cataloged tokens from feature detectors (§6.\*) resolved via the closed vocab (§7.2), after **priority/shadowing** and **fold** per vocab rules.

* **Magnitude & sign:** for every token `t`, `mag(t)` and `sign(t) ∈ {pos, neg, neutral}` from the vocab (§7.2.2–§7.2.3).

* **Preset controls (optional):** caps/floors/dampeners directives declared in the active preset (§7.1, §7.3).

* **Gates:** boolean/enum gates emitted by detectors (e.g., `throat_em`, `em_timing.dampen`) (§6.1, §6.5).

### **8.1.2 Canonical evaluation order (fixed)**

For each category being aggregated, apply the following **normative sequence**:

1. **Token fold** (vocab): resolve duplicates with the declared **commutative, associative** operator (§7.2.2).

2. **Magnitude × sign:** compute the signed base effect for each surviving token.

3. **Bonus gates** (e.g., throat-EM): apply cataloged, boolean/enum-controlled **additive** bonus only when the gate condition is true.

4. **Dampeners** (e.g., halve-penalty): apply catalog/preset reductions (fixed-point) (§7.3.4–§7.3.5).

5. **Floor, then Cap:** enforce preset floors, then caps (§7.3.2–§7.3.3).

6. **Round & Clamp:** **round half-up** where required; **clamp to `[0..100]`** (§5.2.4–§5.2.5).

This order is **normative** and guarantees AB↔BA identity and two-run identity.

### **8.1.3 Magnitude × sign (fixed-point, integer output)**

* **Signed contribution.** For each token `t`, form a provisional value  
   `v_t = mag(t)` if `sign(t)=pos`, `v_t = −mag(t)` if `sign(t)=neg`, `v_t = 0` if `sign(t)=neutral`.

* **Combine tokens.** Sum contributions with **commutative/associative** integer accumulation (or the cataloged fold if not simple sum) to produce a category subtotal `S`.

* **No floats.** Intermediate scales are expressed as integer recipes or closed enums; whenever a fractional step is unavoidable (e.g., a multiplicative reduction), apply **round half-up** immediately and continue with integers.

  ### **8.1.4 Throat-EM bonus (gate-controlled, additive)**

* **Enable.** `talk_ladder.throat_em_bonus ∈ {0,1}` in the active preset or freeze pack. Default is `1` for presets A and B; if the key is missing, treat it as `0` (disabled).  
* **Gate.** Apply only when `throat_em == true` (§6.1) **and** `pace_honored == true` (for example, `em_timing.state == "paced"`; §6.5). If either condition fails or the enable flag is `0`, no bonus is applied.  
* **Recipe and order.** The bonus is a closed enum→integer mapping (for example, `+B_THROAT_EM`), never a float. Add the bonus to **S** **after** magnitude×sign and **before** dampeners and floors/caps (see §7.3 and §8.2). Arithmetic remains integer (fixed-point where relevant).  
* **Single application.** Apply the bonus **at most once per detected EM**. If several routes could target the same EM, use the catalog’s priority or shadowing rules (§7.2.4). Different EM channels may each receive their single bonus.

**Determinism.** Same gates produce the same bonus; AB and BA yield the same result.

### **8.1.5 Dampeners (e.g., halve-penalty; over-concentration)**

* **Trigger.** If a declared dampener condition is true (e.g., **over-concentration** in a family, or `em_timing.dampen == true`), apply the preset’s **dampener mode** (§7.3.4–§7.3.5).

* **Halve-penalty.** For `mode = "halve"`: `S ← round_half_up(S * 0.5)`.

* **Other modes.** Any additional modes use integer recipes pinned in the freeze pack (e.g., `S ← round_half_up(S * 3 / 4)`).

* **Proceed to floors/caps** afterward; do not re-apply dampeners unless explicitly declared (no implicit loops).

### **8.1.6 Floors, Caps, Round, Clamp**

* **Floor then Cap.** Enforce preset **floor**, then **cap** for the category (§7.3.2–§7.3.3).

* **Round half-up** any fractional intermediate once, then **clamp** final category score to `[0..100]`.

* **Global invariants.** Integer domain and rounding rule are **uniform** across categories and runs.

### **8.1.7 Determinism & neutrality**

* **AB↔BA identity.** Because token formation, fold, gates, dampeners, and caps/floors are defined with **order-independent** rules, AB and BA produce **identical** category scores.

* **Two-run identity.** With identical inputs, catalogs, and preset, the pipeline yields **bit-identical** integer results.

* **No hidden sources.** No time/network/locale/floating-point variability is permitted.

### **8.1.8 Validation (binary)**

* **Vocab closure.** Every token used has declared `mag`, `sign`, fold, and (if relevant) priority/shadowing (§7.2).

* **Gate proofs.** Goldens show positive/negative cases for throat-EM and any other bonus gates, including precedence.

* **Dampener proofs.** Goldens demonstrate halve-penalty and other modes at boundary values, with round half-up behavior.

* **Floor/Cap coherence.** For each category, presets satisfy `0 ≤ FLOOR ≤ CAP ≤ 100`; violations fail validation (§7.3.6).

* **Parity proofs.** AB vs BA results and two identical runs produce identical integers.

### **8.1.9 Change control**

* Changing any of: **fold operator**, **priority/shadowing**, **bonus recipe**, **dampener recipes**, or **application order** is a **math change** requiring a new **`release_id`** (§3.1) and regenerated acceptance evidence.

### **8.1.10 Routing (no transport bytes here)**

* This section defines **math** only. Transport/CLI behavior (headers, validators, streams) is referenced **by title only** and is not duplicated here. Public output remains **bands-only** per §2.2.

## **8.2 Family subtotal (cap; over-concentration 0.75) \[Speculative\]**

**Purpose (normative).**  
 Combine per-signal contributions that belong to the **same family** (see §6.6) into a **deterministic, fixed-point family subtotal**, then apply an **over-concentration guard** and **family caps/floors** before handing totals to the next stage. Public Reader v1 remains numeric-free (§2.2).

### **8.2.1 Inputs (closed & validated)**

* **Family membership map** (from the freeze pack): each token is assigned to **exactly one** family (e.g., `g_identity`, `tribal_care`, `rhythm`, `story`, `mind`).

* **Per-signal effects**: the signed, fixed-point contributions produced in §8.1 **after** magnitude×sign, bonus gates, and dampeners for each token.

* **Over-concentration flag** (optional): `over_concentration == true|false` per family (from detectors/presets; see §6.6, §7.3.5).

* **Family caps/floors** (optional): preset-declared integers or closed enums (see §7.3.2–§7.3.3).

### **8.2.2 Canonical evaluation order (fixed)**

For **each family** `F`, compute the subtotal using this **normative** sequence:

1. **Collect & sum** all signed per-signal contributions assigned to `F` → `S₀` (commutative/associative integer sum; no floats).

2. **Over-concentration guard (0.75)**:

   * If `over_concentration(F) == true`, apply the fixed reduction  
      `S₁ = round_half_up(S₀ × 0.75)`; otherwise `S₁ = S₀`.

3. **Floor then Cap** (if declared):

   * `S₂ = max(S₁, FLOOR_F)` (if present), then `S₃ = min(S₂, CAP_F)` (if present).

4. **Clamp to `[0..100]`** and **round half-up** where required (see §5.2.4–§5.2.5).

5. **Emit family subtotal** `S_F = S₃` for downstream use.

This order is **normative** and must be used everywhere family subtotals are computed to preserve AB↔BA identity and two-run identity.

### **8.2.3 Distribution to categories (concept)**

* If a preset **distributes** family subtotals into category lanes, the distribution is a **closed, integer recipe** pinned in the preset (e.g., integer weights per family→category).

* Any split that yields fractional integers **must** apply **round half-up** at each step and remain **order-independent** (stable tie-breakers such as ASCII ascending on category id).

* Distribution rules belong to the **freeze pack**; changing them requires a new `release_id` (§3.1).

### **8.2.4 Determinism & neutrality**

* **AB↔BA identity:** family membership, over-concentration, floors/caps, and distribution are **order-independent**; subtotals for AB and BA are identical.

* **Two-run identity:** identical inputs, catalogs, and preset produce **bit-identical** family subtotals and downstream splits.

* **No floats / locale:** all math is fixed-point; no locale-dependent operations.

### **8.2.5 Validation (binary)**

* **Closure:** every token contributing to `S₀` must reference a known family; every applied floor/cap must be declared for that family.

* **OC 0.75 proof:** goldens show `over_concentration==true` reduces by **exactly 25%** with **round half-up** (e.g., 5→4, 3→2).

* **Floor/Cap coherence:** for each family, `0 ≤ FLOOR_F ≤ CAP_F ≤ 100` or validation fails.

* **Parity proofs:** AB vs BA subtotals and two identical runs are byte-identical.

* **Distribution proofs (if used):** integer splits match preset weights with pinned tie-breakers.

### **8.2.6 Change control**

* Any change to the **OC factor** (0.75), **family floors/caps**, or **distribution recipe** is a math/preset change and **requires** a new `release_id` (§3.1); regenerate acceptance artifacts accordingly.

### **8.2.7 Routing (no transport bytes here)**

* This section defines **math aggregation** only. Transport/CLI behavior (headers, validators, streams) is referenced **by title only** in **PF-Canon-HDE-CLI-API-Vendor-Ref**. Public output remains **bands-only** per §2.2.


  ## **8.3 Cross-family correction (fast intimacy penalty) \[Speculative\]**

**Purpose (normative).** Apply a small, deterministic **integer** correction when a **cataloged** fast-intimacy pattern is present, to temper early “stacking” of signals across families. The correction is **order-neutral (AB↔BA)**, uses **fixed-point integers only**, and is **internal-only** — **Reader v1 remains numeric-free** (§2.2). Transport/CLI behavior is out of scope (titles-only to PF-Canon-HDE-CLI-API-Vendor-Ref / PF-Canon-HDE-Governance).

**Gating & freeze-pack coupling.** This feature is **disabled by default** in v1. It may be enabled only by **frozen pack/preset** settings (PF-12 §6), using **closed enums/ids**. Any change to on/off, magnitude classes, or target mappings is a **frozen-input change** and **requires a new `release_id`** (§3.1).

### **8.3.1 Inputs (closed & validated)**

* **Family subtotals `S_F`** from §8.2 **after** over-concentration guard and family floors/caps.  
* **Enabling tokens** from catalogs/preset that **explicitly** permit this correction (closed ids/enums only; PF-12 §2).  
* **Preset posture (if used).** Preset may enable/disable the correction and fix **magnitude class** and **targets** (all encoded as **integers/enums**; no floats).

  ### **8.3.2 When it applies (binary gate)**

The correction **MUST NOT** be inferred. It applies **only** if **all** hold:

1. A **cataloged** token/id explicitly marks a fast-intimacy condition (schema closure).  
2. The active **pack/preset** **enables** this correction.  
3. All referenced families/targets are members of the **current frozen set** (PF-12 §2, §6).

If any condition fails, **no correction** is applied.

### **8.3.3 Canonical evaluation order (fixed)**

Apply immediately **after** §8.2 (family subtotals ready) and **before** §8.4 (global floor / hand-off to category mapping):

1. **Select magnitude class `P`.**  
    `P ∈ ℕ₀` from a **closed enum** (e.g., `none|small|med|large`) with a pack/preset-frozen map to **non-negative integers**. No floats.

2. **Select targets (order-independent).**  
    A pack/preset-frozen rule chooses targets deterministically:

   * **Family-level:** a fixed set `{F₁,…}` of families; or  
   * **Category-level:** a frozen map from families to categories (integer split weights), with **stable tie-break** in **ASCII order of target id**.  
      *(Routing: tie-break definitions live in the preset/catalog; titles-only here.)*  
3. **Apply correction (integer subtraction).**

   * **Single target:** `T' = max(0, T − P)`.  
   * **Multiple targets:** split `P` by the frozen integer rule; at each step apply **round\_half\_up** (as in §5.2.5); break ties by **ASCII order** of target id; subtract from each target: `T_i' = max(0, T_i − p_i)`.  
4. **Clamp.** After subtraction and rounding, clamp each adjusted value to **`[0..100]`**.

5. **Proceed.** Continue with §8.4 (global floor, then category mapping).

This sequence is **normative** and guarantees **AB↔BA** and **two-run** identity.

### **8.3.4 Determinism & neutrality**

* **AB↔BA identity.** Target selection, magnitude mapping, and splits are defined as **commutative/order-independent** by the frozen spec; swapping A/B yields identical results.  
* **Two-run identity.** With identical inputs, catalogs, constants, and preset, recomputation yields **bit-identical** integers.  
* **No floats / locale.** All math is integer/fixed-point; run under **`LC_ALL=C`**; no time- or locale-dependent behavior.

  ### **8.3.5 Validation (binary)**

* **Closure.** Every token/id and every target referenced by the correction exists in the **active pack/preset** (PF-12 §2, §6).  
* **Magnitude mapping.** Enum→integer map for `P` is declared and frozen; values must be **non-negative integers** and within pack-specified bounds.  
* **Split proofs.** Goldens cover multi-target splits, including tie cases and **round\_half\_up** at each step.  
* **Parity.** `(A,B)` vs `(B,A)` produce identical corrected values; two identical runs produce identical results.

  ### **8.3.6 Change control**

Changing **magnitude classes**, **target selection rules**, **split/tie-break recipe**, or the **application point** is a **math change**; update the pack/preset and **regenerate acceptance evidence**; **bump `release_id`** (§3.1).

### **8.3.7 Routing (no transport bytes)**

This section defines **math only**. Any CLI/Reader behavior (headers, validators) is referenced by title only in **PF-Canon-HDE-CLI-API-Vendor-Ref**. Public output remains **bands-only** (§2.2).

**Acceptance & CI (titles-only)**

* `FAST_INTIMACY_CORRECTION_ENABLED_OK` (gate honored; default off)  
* `FAST_INTIMACY_CLOSURE_OK` (all ids/enums from pack/preset)  
* `FIXED_POINT_INTEGER_ONLY_OK` (no floating arithmetic)  
* `SPLIT_TIEBREAK_ASCII_OK` (deterministic split/tie-break)  
* `CROSS_FAMILY_CORRECTION_ABBA_OK`, `TWO_RUN_IDENTITY_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`, `RELEASE_ID_RECOMPUTE_OK` (on any frozen-input change)


## **8.4 Global floor; handoff to category mapping \[Speculative\]**

**Purpose (normative).**  
 Finalize **per-category integer scores** after aggregation by applying an optional **global floor**, then **handoff** each category to **band mapping** (§5.3). All math remains **fixed-point**, **order-neutral (AB↔BA)**, and **internal-only**; Reader v1 stays numeric-free (§2.2).

### **8.4.1 Inputs (closed & validated)**

* **Per-category integers** `S_cat ∈ [0..100]` produced by §8.1–§8.3.

* **Global floor** (optional): a closed-enum or integer declared in the **preset** and/or **freeze pack** (e.g., a uniform floor or a per-category floor map).

* **Cap coherence:** any **category cap** previously declared (§7.3.2) remains in force.

### **8.4.2 Canonical evaluation order (fixed)**

For **each category** `c`:

1. **Select floor** `F_c`

   * If a **per-category** floor is declared, use that; otherwise, if a **uniform** floor is declared, use it for all categories; else **no floor**.

2. **Apply floor**

   * `S'_c = max(S_c, F_c)` (if no floor, `S'_c = S_c`).

3. **Cap coherence & clamp**

   * If a cap `CAP_c` exists, validation must guarantee `F_c ≤ CAP_c` (§7.3.6).

   * Clamp final integer to `[0..100]` (values are already integers; rounding is not required here).

4. **Handoff to band mapping**

   * Feed `S'_c` into **§5.3 band mapping** (inclusive maxima) to obtain `band_c ∈ {Cool,Open,Warm,Glow}`.

   * Internal pipelines may retain `S'_c` for diagnostics; **public** surfaces use **bands-only** (§2.2).

The sequence above is **normative** and must be used everywhere to preserve AB↔BA identity and two-run identity.

### **8.4.3 Determinism & neutrality**

* **AB↔BA identity.** Because floors and clamps are per-category and order-independent, AB and BA yield identical `S'_cat` and band outcomes.

* **Two-run identity.** With identical inputs, catalogs, and presets, recomputation produces **bit-identical** `S'_cat` and band arrays.

* **No floats / locale.** Only integer comparison and min/max are used; locale and platform cannot change outcomes.

### **8.4.4 Validation (binary)**

* **Domain bounds:** for any declared floor, `0 ≤ F_c ≤ 100`.

* **Cap coherence:** if both `F_c` and `CAP_c` are present, enforce `F_c ≤ CAP_c`; otherwise the catalog/preset **fails** validation (§7.3.6).

* **Completeness:** every category present after §8.3 either applies a floor or skips it; no category is dropped.

* **Parity proofs:** AB vs BA results and two identical runs produce identical integers and bands.

### **8.4.5 Change control**

* Changing the **global floor value**, its **scope** (uniform vs per-category), or its **application order** is a math/preset change and **requires** a new `release_id` (§3.1); regenerate acceptance artifacts.

### **8.4.6 Routing (no transport bytes here)**

* This section defines **math** only. Transport/CLI behavior (headers, validators, streams) is referenced **by title only** in PF-Canon-HDE-CLI-API-Vendor-Ref. Public output remains **bands-only** per §2.2.


  ## **8.5 Category mapping to bands (inclusive maxima) \[Speculative\]**

**Purpose (normative).**  
 Convert each **per-category integer** score `S'_c ∈ [0..100]` (after §8.4) to a **band** using the **inclusive maxima** rules in §5.3. This step is deterministic, order-neutral (AB↔BA), and produces **internal** band labels that the Presenter will expose on the public surface as **bands-only** (§2.2).

### **8.5.1 Inputs (closed & validated)**

* **Final integers per category** `S'_c` from §8.4 (already floor/cap-conformant and clamped to `[0..100]`).

* **Band thresholds** from the freeze pack (§5.3), with inclusive maxima for `Cool ≤ …`, `Open ≤ …`, `Warm ≤ …`, else `Glow`.

  ### **8.5.2 Canonical mapping (fixed)**

For each category `c`, apply **exactly** this mapping:

1. **Compare `S'_c` to inclusive maxima** per §5.3 in ascending order of bands.

2. **Select the first matching band** (no ties due to inclusivity); if none match, assign **Glow**.

3. **Record** `(c, band_c)` for downstream Presenter use.

The thresholds and their order live in §5.3; this section **does not** restate numeric values.

### **8.5.3 Determinism & neutrality**

* **AB↔BA identity.** Because `S'_c` is AB-neutral (see §8.4), `band_c` is identical for AB and BA.

* **Two-run identity.** With identical inputs, catalogs, and presets, recomputation yields byte-identical band arrays.

* **No floats / locale.** Only integer comparisons are used.

  ### **8.5.4 Validation (binary)**

* **Completeness:** every `S'_c ∈ [0..100]` maps to **exactly one** band.

* **Boundary proofs:** goldens cover all threshold edges (e.g., Cool/Open, Open/Warm, Warm/Glow, and `100 → Glow`) as specified in §5.3.

* **Parity proofs:** AB vs BA produce identical band arrays; two identical runs produce identical results.

  ### **8.5.5 Change control**

* Changing **any** band threshold or their evaluation order is a **math change**; it must be captured in the freeze-pack manifest and results in a **new `release_id`** (§3.1). Downstream acceptance must be updated in lockstep.

  ### **8.5.6 Routing (no transport bytes here)**

* This section defines **math mapping** only. Presenter/Reader behavior (payload shape, schema, headers) is referenced **by title only** elsewhere; public output remains **bands-only** per §2.2.


  

  ## **9 Validation**

**Scope.** This section lists the proofs required to accept the math. Tests must use the active freeze pack and produce artifacts referenced in §11 Evidence. No transport or HTTP proofs live here.

### **9.1 Band edges (inclusive maxima)**

**Prove:**

* For each active preset `P`, the inclusive maxima map integers in \[0..100\] to exactly one band.  
* Equality falls to the lower band at each maximum.  
* `100` always maps to `Glow`.  
   **Cases to cover:** `M_cool(P)`, `M_cool(P)+1`, `M_open(P)`, `M_open(P)+1`, `M_warm(P)`, `M_warm(P)+1`, `100`.  
   **Artifacts:** see §11.1.

  ### **9.2 Rounding and clamping**

**Prove:**

* Rounding is **away-from-zero** at pinned stages.  
* Final clamp is \[0..100\].  
   **Cases to cover:** midpoints and near extremes such as `-0.6, -0.5, -0.4, 0.4, 0.5, 0.6, 99.4, 99.5, 101.2`.  
   **Artifacts:** see §11.2.

  ### **9.3 Electromagnetics (EM) extractor**

**Prove:**

* `channel_id` format is `"<lowGate>-<highGate>"` with gates zero-padded `01..64`.  
* `channels` array is sorted ASCII by `channel_id` and contains unique entries.  
* AB and BA produce identical EM outputs after normalization.  
* Unmapped or ambiguous inputs fail closed with typed errors.  
   **Cases to cover:** at least one positive EM case with throat involvement, one negative case with no EM, and one fail-closed case.  
   **Artifacts:** see §11.3.

  ### **9.4 Over-concentration guard**

**Prove:**

* Trigger applies when the family record count is `> 3` after de-duplication.  
* Factor `× 0.75` applies once per family, then rounding is away-from-zero, then floors and caps in the canonical order.  
   **Cases to cover:** family counts `3` and `4` with a worked subtotal example.  
   **Artifacts:** see §11.4.

  ### **9.5 Parity and two-run identity**

**Prove:**

* AB↔BA parity holds on the complete internal totals before band mapping.  
* Two identical runs with the same inputs and pack produce byte-identical results.  
   **Artifacts:** see §11.5.

  ### **9.6 Pack closure and release identity**

**Prove:**

* Every identifier and table used by scoring, aggregation, and extractors resolves to an entry in the freeze pack.  
* Recomputed `sha256(canonical_manifest_bytes)` equals the recorded `release_id`.  
   **Artifacts:** see §11.6.

**Routing.** Public payload, serialization, and emitter rules live in **PF-Canon-HDE-CLI-API-Vendor-Ref** (titles-only). 

## 

### 

## 

## 

# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]

## **10.1 Canonical serializer (UTF-8, sorted keys, compact, exactly one LF) \[Implemented\]**

**Purpose (normative).** Define the single JSON canonicalization used for all public bytes (Reader body and CLI stdout) and for the preimage used to compute `idempotence_hash` (§3.2). The serializer is BOM/ANSI-free, locale-neutral, and yields byte-identical output for identical inputs.

### **Canonical JSON rules**

* **Encoding:** UTF-8. No BOM.  
* **Key order:** `sort_keys = true` (lexicographic ASCII).  
* **Separators:** compact `','` and `':'` (no spaces).  
* **Escaping:** `ensure_ascii = false` (emit valid UTF-8 directly).  
* **Termination:** append exactly one trailing LF (`\n`) to the serialized document.  
* **No pretty print.** No indentation.  
* **No ANSI or non-JSON bytes.** No color codes, prompts, or trailing spaces.

### **Scope of use**

* **Success body:** serialize the five-key preimage (without `idempotence_hash`), compute `sha256(preimage_bytes)`, then re-serialize the final six-key object (§3.2).  
* **Error body:** the same canonicalization rules apply to the typed error object (LF-terminated).  
* **Arrays:** whenever arrays appear in public outputs, their order is deterministic and pinned by this spec (for example, sort by `id`) before serialization.

### **Determinism properties**

* **Two-run identity:** canonicalizing the same logical object twice produces byte-identical bytes, including the single trailing LF.  
* **AB↔BA identity:** because inputs are normalized and arrays/sets are deterministically ordered before emission, AB and BA produce identical bytes (§3.4).  
* **Reader↔CLI parity:** both surfaces call this canonicalization and therefore emit byte-equal bodies for the same inputs.  
* **Environment pins:** all checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **Validation gates (binary)**

* **Encoding/termination:** output is UTF-8, BOM-free, and ends with one LF (neither zero nor two).  
* **Key order and separators:** a local re-serialization with `sort_keys=true` and compact separators compares byte-equal; any mismatch is invalid.  
* **Preimage re-check:** remove `idempotence_hash`, re-serialize the preimage canonically, hash, and reproduce the published digest (§3.2).

### **Hygiene requirements**

* **Single emitter only.** Public emission code **must not** use ad hoc `json.dumps` or alternate serializers; use the single canonical emitter (§10.2).  
* **Locale neutrality.** No locale-dependent collation, time, or formatting anywhere on the emission path.  
* **Numeric-free covenant.** The serializer emits what it is given; public success objects remain numeric-free except for identity fields already defined (§2).

**Routing note.** Transport and HTTP byte rules (headers, conditional delivery, caching) and CLI stream policy are referenced by title only in **HDE-CLI-API-Vendor Ref**.

---

## **10.2 Unify emission entrypoint (CLI \+ Reader share the same emitter) \[Required-Now\]**

**Purpose (normative).** There is one public emission entrypoint for Reader v1 and CLI stdout: the stable presenter emitter. Both the Adapter (Reader) and CLI must call this entrypoint. No surface may hand-craft JSON or call an ad hoc serializer. Replace any local helpers with the presenter serializer import and forbid `json.dumps` on public paths. The unified emitter applies §10.1 canonicalization and the §3.2 preimage recipe.

### **10.2.1 Unified entrypoint (contract)**

* **Single emitter path.** Public bytes MUST be produced by the presenter’s canonical emission function.  
* **Caller responsibilities (Reader and CLI).**  
  1. Prepare the success preimage (five keys; see §3.2).  
  2. Pass it to the unified emitter; receive LF-terminated canonical bytes for transport/stdout.  
  3. Do not mutate, re-encode, or re-serialize the returned bytes.  
* **Error bodies.** Call the same unified emitter for typed error objects (LF-terminated; public shape constraints in §2).

### **10.2.2 Disallowed patterns (hard fail)**

* **No local serializers.** Remove or forbid any module-local canonicalizers on public paths.  
* **No ad hoc `json.dumps`.** Any direct `json.dumps(` on public emission paths is invalid (including “format then add LF”).  
* **No alternate emitters.** Do not duplicate the preimage recipe or `idempotence_hash` logic outside the unified emitter.  
* **No test-only bypass.** Tests must not bypass the unified entrypoint.

### **10.2.3 Required refactor (action items)**

* **Replace local helper.** Import and use the presenter’s emitter for:  
  * preimage serialization (five keys)  
  * `idempotence_hash` computation and insertion  
  * final LF-terminated body emission  
* **Delete duplicates.** Remove any local “sercanon” or equivalent from public emission modules.  
* **Unify tests.** Ensure Reader and CLI tests call the same emitter function (no test shims).  
* **Grep-guard in CI.** Fail on public paths that contain:  
  * `\bjson\.dumps\(`  
  * alternate emitter names not on the allowlist  
  * more than one canonicalizer symbol in a public module

### **10.2.4 Acceptance and validation (binary)**

* **Reader↔CLI parity.** For identical inputs/environment, Reader response bytes and CLI stdout are byte-identical.  
* **Idempotence re-check.** Remove `idempotence_hash`, re-serialize the preimage with the unified emitter, hash, and reproduce the published digest (§3.2).  
* **LF discipline.** Both surfaces produce exactly one trailing LF; no BOM/ANSI.  
* **AB↔BA parity; two-run identity.** Public bytes are bit-identical for AB vs BA and across two runs (see §3).  
* **No extras.** Success bodies contain exactly the six keys; `categories[*]` are `{id,band}` only (§2).  
* **Pins and evidence.** Run byte checks with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Index parity/idempotence artifacts in **Appendix D: Evidence Index** and mirror them 1:1 in `artifacts/evidence_index.jsonl`.

### **10.2.5 Migration checklist (one-time)**

1. **Inventory.** Locate all public emission call sites (Reader handlers, CLI command).  
2. **Refactor.** Import the presenter’s emitter; remove local serializers and re-wire calls.  
3. **Purge.** Delete obsolete helpers; replace any `json.dumps` on public paths.  
4. **Re-run evidence.** Regenerate parity/idempotence/LF goldens; confirm byte equality across Reader and CLI; update the human index and machine mirror in the same commit.  
5. **Enable grep-guard.** Add CI checks to prevent regressions.

### **10.2.6 Non-goals and routing**

This section does not restate HTTP transport (headers, conditional delivery, caching) or CLI stream policy; those are referenced by title only in **HDE-CLI-API-Vendor-Ref**. Public output remains bound by the numeric-free covenant (§2).

*Tokens: see **HDE-Governance §2.0**.*

---

## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Implemented\]**

**Purpose (normative).**  
 Define the **binary checks** and **evidence artifacts** that prove public bytes are serialized by the **canonical emitter** (§10.1), that **Reader and CLI** share the **single entrypoint** (§10.2), and that the **preimage recipe** (§3.2) is correctly applied.

### **10.3.1 Acceptance gates (must all pass)**

* **Canonical encoding.** Bytes are UTF-8, **BOM/ANSI-free**, with **sorted keys** and **compact separators**; output ends with **exactly one** LF (`\n`).

* **Six-key success.** Success bodies contain **exactly** the six top-level keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`) and **no extras** (§9.2).

* **Public shape.** `categories[*]` are **exactly** `{id, band}` with `band ∈ {Cool,Open,Warm,Glow}`; **no** `prompt`, `personal_key`, `shared_key`, `score`, or other fields (§§2.1–2.2, §9.1).

* **Preimage re-check.** Removing `idempotence_hash`, re-serializing the **five-key preimage** with the canonical emitter, and hashing **reproduces** the published digest (§9.3.3).

* **Parity & identity.**

  * **Reader ↔ CLI:** bytes are **identical** for identical inputs/environment.

  * **AB ↔ BA:** bytes are **bit-identical** for swapped inputs (pair normalization).

  * **Two-run:** two serializations with the same inputs produce **byte-identical** output (§3.4).

### **10.3.2 Evidence set (titles/paths only)**

Maintain reproducible proof in the repo (no private data), for example:

* **Schema & LF discipline:** `schemas/reader.v1.schema.json`, `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`.

* **AB↔BA goldens (public success):** `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`.

* **Idempotence coupling:** `artifacts/cards/A3/IDENTITY_OK.txt`, recompute logs showing **preimage → sha256 → final** (§3.2).

* **Parity harness/scripts:** `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`.

* **Reader/CLI parity runs:** \* evidence that the Reader 200 body and the corresponding CLI Reader-envelope bytes (stdout or reader-dump surface as defined in \*\*HDE-CLI-API-Vendor-Ref\*\*) are byte-equal for the same inputs (§9.2).

Exact locations are indexed in **Appendix B — Evidence Index**; transport/HTTP acceptance is routed **by title only** to PF-Canon-HDE-CLI-API-Vendor-Ref.

### **10.3.3 CI hygiene (fail-fast)**

* **Grep-guards (public paths):**

  * Forbid ad-hoc `json.dumps(` and local canonicalizers; only the **presenter emitter** may be used (§10.2).

  * Flag multiple canonicalizers defined in public modules.

* **Single-LF check:** assert **one** trailing LF on success and error bodies.

* **Schema & shape:** validate six-key success, `{id,band}` items only, and enums.

* **Parity & identity:** automated AB/BA and two-run byte-compare jobs; Reader↔CLI parity job.

### **10.3.4 Failure posture (binary)**

If **any** gate fails (schema, shape, LF, preimage hash, parity/identity, or CI hygiene), the emission is **invalid** and must **not** be published. Transport behavior on failure (status, headers) is **not duplicated here** and is referenced **by title only** in PF-Canon-HDE-CLI-API-Vendor-Ref.

### **10.3.5 Determinism notes**

* Evidence must demonstrate that the **same emitter** produced both Reader and CLI bytes; that **sorted keys \+ compact separators \+ one LF** are present; and that the **preimage hash couples** to the final bytes.

* All proofs are **order-neutral** (AB↔BA) and **re-runnable** (two-run identity).

Yes. Keep §11 in the Math Spec, but make it **math-only evidence**. Any transport or header evidence (ETag, 304, Cache-Control, CLI stdout parity) belongs in **CLI/API/Vendor** or **Governance A7**. Here’s the **final §11** to paste in:

---

## **11\. Evidence**

**Scope.** Math-only evidence that proves §9 Validation. All artifacts are generated from the active freeze pack and test harness. **Do not include transport/HTTP evidence here.**  
 **Index & mirror (MUST).** List every artifact below (titles/paths only) in **Appendix D: Evidence Index** and add a matching records-only line to the machine mirror at `artifacts/evidence_index.jsonl` (with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`).  
 **Formatting (JSON artifacts).** UTF-8, BOM-free, sorted keys, compact separators, exactly one trailing `\n`. Provide a sibling `.sha256` when noted; otherwise the mirror supplies the digest. Place artifacts under `artifacts/` (for example, `artifacts/math/`, `artifacts/topology/`, `audit/gates/...`). Record environment pins once at `artifacts/proofs/env_pins.txt` (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

### **11.1 Band edges**

**Files (consolidated, per pack):**

* `audit/gates/bands/edges.snapshot.json`  
* `audit/gates/bands/edges.diff.json`

**Must include:** for each active preset, the three inclusive maxima and proof cases at `M_cool`, `M_cool+1`, `M_open`, `M_open+1`, `M_warm`, `M_warm+1`, and `100` with expected bands. `edges.diff.json` shows deltas vs prior snapshot.

### **11.2 Rounding and clamping**

**Files:**

* `artifacts/compat/rounding_cases.json` (+ optional `.sha256`)

**Must include:** away-from-zero midpoint proofs and clamp proofs to `[0..100]` with worked examples around boundaries.

### **11.3 Electromagnetics (EM) extractor**

**Files:**

* `artifacts/features/em_golden_cases.json` (+ optional `.sha256`)

**Must include:** `catalog_sha256`, ≥1 positive EM case with throat involvement, ≥1 negative case, ≥1 fail-closed case, and assertions that:

* `channel_id` is `"NN-NN"` with zero-padded gates `01..64` and min-first,  
* `channels` is ASCII-sorted and unique,  
* AB and BA outputs are identical after normalization.

### **11.4 Over-concentration guard**

**Files:**

* `artifacts/features/over_concentration_cases.json` (+ optional `.sha256`)

**Must show:** trigger at family record count `> 3` (after de-dup), **single** application of factor `× 0.75`, rounding away-from-zero, then floors and caps in canonical order, with worked examples for counts 3 and 4\.

### **11.5 Parity and two-run identity (public bytes)**

**Files (titles/paths only):**

* AB↔BA goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Two-run marker: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`

**Must prove:** AB bytes equal BA bytes for the same inputs and pack; two identical runs produce byte-identical results (LF-terminated), consistent with §3.2/§3.4.

### **11.6 Pack closure and release identity**

**Files:**

* `artifacts/math/freeze_pack_manifest.json` (+ `.sha256`) — evidence copy of `catalog/manifest.json`  
* `artifacts/math/release_id.txt` — `sha256(canonical_manifest_bytes)`  
* `artifacts/math/release_id_recompute.log` — recomputation trace (must match `release_id`)  
* `artifacts/math/checksums_audit.log` — per-entry path/sha256/size verification

**Must prove:** manifest equals canonical bytes; `files[]` ASCII-sorted and unique; recorded digests/sizes match; recompute hash equals published `release_id`.

**Routing.** Transport/HTTP evidence (status, headers, conditional delivery, caching, Reader↔CLI stream parity) lives in **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles only).

# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**

Pointers are **informative** for engineers. The **normative** rules live in §§2–10.

* **Public envelope:** `engine/emit_public.py`

  * Current minimal path that builds the Reader v1 envelope.

  * **Refactor:** import and use the **stable presenter emitter** (§10.2) in place of any local `sercanon`; remove ad-hoc `json.dumps`.

  * Re-run parity/idempotence/LF goldens after refactor.

* **Presenter (stable):** `presenter/reader_v1/emitter.py`

  * Canonical preimage → `sha256` → final, **LF-terminated** emission (§§3.2, 10.1).

  * **Action:** drop any `prompt` carry-through so `categories[*]` are **exactly** `{id, band}` (§§2.1–2.2, 9.1, 9.4).

* **Compat internals:** `engine/compat/{compute,categories,thresholds,ordering}.py`

  * Internal 10-category scoring → thresholds → bands; AB↔BA via `normalize_pair` (§§5.1–5.3, 8.\*).

  * Public Reader v1 still emits **single** `harmony` item; full Magic-10 exposure is **future** (versioned) (§2.2).

* **Validation:** `engine/validation/viewer_prefs.py`

  * Enforces **exact** Magic-10 keys and integer weights `0..100`; `invalid_prefs` on any mismatch (§5.1, §5.2).

* **Dev Reader harness (parity evidence):** `adapter/http_reader.py`

  * Dev-only `/api/reader?v=1` surface; uses unified emitter and A7-style conditional GET/HEAD for parity proofs.

  * Not a production surface; use for **Reader↔CLI byte-equality** and LF/schema checks (§§9–10).

* **Schema (public success):** `schemas/reader.v1.schema.json`

  * **Action:** remove optional `category.prompt`; keep `additionalProperties:false`, `required:["id","band"]`.

  * Success objects are **six-key** covenant; errors follow typed shape with single LF (§§2.1–2.3, 9.2, 9.4).

* **CI hygiene (suggested):**

  * Grep-guard: forbid `json.dumps(` and multiple canonicalizers on public paths; allow only the presenter emitter (§10.2).

  * Jobs: AB↔BA byte-compare, two-run identity, single-LF checks, schema/shape gates, idempotence re-check (§§3.4, 9.3, 10.3).

Transport/HTTP behavior (status, headers, conditional delivery, caching/writers) and CLI stream policy are **not** restated here; they are referenced **by title only** in PF-Canon-HDE-CLI-API-Vendor-Ref.

# **13\. Change Log & Doc-Delta Hooks \[Required-Now\]**

## **13.1 Change Log (concise, normative)**

* **v0.3.** Remove **`prompt`** across schema/emitter; clarify **uncertainty** retired; unify to a **single emitter/serializer path**; tag sections as **\[Implemented\] / \[Required-Now\] / \[Speculative\]**; **preserve math** (no loss of normative content).

**Style rule for future entries:** keep items **short, action-oriented**, and limited to **normative deltas** that affect **math**, the **public contract**, or **acceptance**. Purely editorial rearrangements without normative effect **need not be listed** here. 

## **13.2 Doc-Delta Hooks (how to record & ship changes)**

**Purpose.** Provide a uniform, auditable method to propose, review, and land changes without drifting from single-home ownership or duplicating bytes. Titles-only cross-references to transport/CLI and ops remain mandatory.

### **13.2.1 When to open a Doc-Delta**

Open a Doc-Delta **before** any of the following:

* **Math changes**: category membership/order, thresholds, vocab tokens, fold/priority rules, dampener recipes, floors/caps, fast-intimacy correction, preset schema/entries. (These require a new `release_id`.)

* **Public contract changes**: anything that would alter Reader v1 bytes (e.g., exposing more than `harmony`).

* **Serializer/emitter** flow alterations that could affect byte identity.

* **Schema gates**: tightening/loosening public success/error schema.

  ### **13.2.2 Doc-Delta content (minimal but complete)**

Each Doc-Delta record **MUST** include:

* **Delta ID / Date / Author.**

* **Scope:** *Math* | *Public Contract* | *Serializer/Emitter* | *Schema* | *Editorial*.

* **Targets (titles-only):** section anchors (e.g., “§5.2 Deterministic integer scoring model”).

* **Change summary (≤5 bullets):** action verbs (“Add preset B cap\_total=+3”, “Replace local `sercanon` with presenter emitter”).

* **Acceptance impact:** which gates/goldens to add/update (AB↔BA, two-run, LF, schema, idempotence re-check).

* **Freeze-pack impact:** *Yes/No*. If *Yes*, attach the new canonical manifest digest (**new `release_id`**) and list affected artifacts by title/path (Appendix B).

* **Routing:** confirm that transport/CLI/ops bytes remain referenced **by title only** (no duplication).

  ### **13.2.3 Landing a Doc-Delta (binary outcome)**

A Doc-Delta is **Accepted** only when:

* All **acceptance gates** implicated by the change **pass** (schema/public-shape, LF discipline, idempotence re-check, AB↔BA parity, two-run identity).

* Evidence artifacts are written and indexed in **Appendix B** (titles/paths only).

* If the change touches frozen math, the **new `release_id`** is present and recorded.

Otherwise, it is **Rejected** (no partial merges).

### **13.2.4 Guardrails**

* **No duplicated bytes.** Transport/headers/validators remain in **PF-Canon-HDE-CLI-API-Vendor-Ref**; ops/A7 in **PF-Canon-HDE-Governance** (titles-only pointers).

* **Single emitter.** Reader and CLI MUST share the same presenter emitter; forbid ad-hoc `json.dumps` on public paths.

* **Numeric-free public.** Reader v1 stays bands-only with a single `harmony` item unless a versioned contract says otherwise.

* **AB↔BA / Two-run first-class.** Any delta that can disturb order-neutrality or determinism **must** add/update parity goldens.

  ### **13.2.5 Filing & trace**

* Append the **one-line** change summary to §13.1 upon acceptance.

* Add/update entries in **Appendix B — Evidence Index** pointing to new/updated goldens, schema files, recompute logs, and freeze-pack manifests.

* If a feature is removed (like `prompt`), place a single-line notice in **Appendix D — Retired Features** (no prose duplication).

This hook keeps the spec stable, auditable, and easy to evolve while preserving single-homes and byte-level determinism. 

## 

## 

## 

# **Appendix A — Determinism & Ordering (reference) \[Required-Now\]**

## **A.1 Canonical comparators**

* **Key ordering (JSON objects).** Keys are serialized with **ASCII lexicographic** order (`sort_keys=true`). No locale-aware or natural (“1\<10”) sorts.

* **String ordering (general).** When a comparator is needed (e.g., for array stabilization), use **byte-wise ASCII ascending** on the UTF-8 bytes of the string.

* **Tuple/list ordering.** Compare element-wise under the same ASCII rules; the **shorter tuple is smaller** when all shared positions are equal.

* **Category ordering.** When category arrays exist (current/future), **sort by `id` (ASCII ascending)**.

* **Stable tie-breaks (fail-closed on collision).** If two items share the same primary key, use a **secondary, deterministic** key (e.g., `id` then `band`) to avoid comparator drift. **If a collision remains after tie-break, treat it as a construction error (fail-closed); do not drop a duplicate arbitrarily.** (Aligns with §9.1 public `categories` rules and Appendix A.2 set-normalization.) 

  ## **A.2 Set normalization**

* **Pair normalization (AB↔BA).** Before any computation, derive a **pair key** and reorder inputs to a canonical **(min, max)** by the **ASCII comparator**. All downstream math **MUST** consume the **normalized pair** only.

* **Array → set semantics.** When an array represents a set (e.g., unique **category `id`s**, token IDs, channel IDs), **deduplicate by identity key**, then **sort deterministically (ASCII)** before use/serialization.

* **Deterministic fold.** If the same token/ID appears more than once, apply the **commutative, associative fold** declared in the catalog (e.g., **max**, bounded sum) so evaluation order **cannot** affect the outcome.

* **Fail-closed on conflict.** If two entries collide on an identity key but **disagree on value** (e.g., two different `band` values for the same `id`), treat this as a **construction error**—**do not** pick arbitrarily or drop a duplicate. (Aligns with §9.1 public `categories` rules.) 

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

 Index of goldens, tests, and artifacts used to prove parity, newline discipline, idempotence coupling, and schema conformance. Paths are illustrative; keep them current in the repo. Titles/paths only—no payload bytes here.

**B.1 Parity (Reader↔CLI, AB↔BA)**

* AB↔BA goldens (public success): `goldens/reader/v1/g02_ab_ba_parity_A.jsonl` `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Reader↔CLI parity harness/scripts: `scripts/make_reader_v1_goldens.py` `adapter/http_reader.py` (dev harness; parity evidence) `engine/emit_public.py` (public envelope; unified emitter callsite)  
* Parity tests: `tests/reader_v1/test_emitter.py` `tests/cli/test_cli_stdout_schema_and_lf.py`

**B.2 Newline & encoding discipline (LF; UTF-8; no BOM/ANSI)**

* LF \+ schema tests: `tests/cli/test_cli_stdout_schema_and_lf.py` `tests/reader_v1/test_emitter.py`  
* Emitter canonicalization reference: `presenter/reader_v1/emitter.py` (single emitter; canonical rules)

**B.3 Idempotence coupling (preimage → sha256 → final)**

* Identity markers & logs: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Preimage/hash recompute scripts: `scripts/make_reader_v1_goldens.py` `scripts/make_compat_determinism_artifacts.py`  
* Success schema (preimage fields source of truth): `schemas/reader.v1.schema.json`

**B.4 Schema conformance (public success & errors)**

* Public success schema (six keys; `{id,band}` only): `schemas/reader.v1.schema.json`  
* Reader/CLI schema tests: `tests/reader_v1/test_emitter.py` `tests/cli/test_cli_stdout_schema_and_lf.py`  
* Dev harness (validation runs; titles-only reference): `adapter/http_reader.py`

**B.5 Identity evidence**

* Emitter SHA-256 (canonical): `artifacts/identity/emitter_sha256.txt`  
* Service identity (ops; names-only payload): `artifacts/identity/service_identity.json` *(owned by Governance; see Governance Appendix D for transport/ops evidence)*

**Maintenance note.** When goldens or acceptance artifacts change, update this index and the corresponding entries in §13 (Change Log & Doc-Delta hooks). Titles/paths only; no duplication of transport/HTTP bytes.

# **Appendix C — Dev Harness (Reader v1) \[Informative\]**

## **C.1 Purpose**

Provide a **local, non-production** harness for exercising Reader v1 with fixture inputs and proving **byte parity** with the CLI. It exists to generate acceptance evidence (schema/LF, AB↔BA, two-run identity, Reader↔CLI parity) while keeping the **public contract** numeric-free and bands-only.

## **C.2 Gating & safety**

* **Environment gate:** the harness **MUST** run only when `APP_ENV=dev`. Any other value **must exit/refuse**.

* **No PII / no vendors:** load only local fixtures; never call vendor APIs; do not emit PII.

* **Non-production surface:** the harness is not a public endpoint and must not be mounted in production builds.

## **C.3 Parity with CLI (procedure)**

To prove Reader↔CLI byte-equality for the same logical invocation:

1. **Prepare inputs:** normalized pair (or fixture chart paths) and required flags (e.g., time-zone overrides) as permitted by the harness.

2. **Emit via Reader:** call the dev harness; capture the **LF-terminated** success body.

3. **Emit via CLI:** run the CLI surface that emits the Reader v1 success envelope for the same inputs (for example, the reader-dump path defined in the CLI/API reference) and capture those envelope bytes (stdout or file, depending on the command).

4. **Byte-compare:** bodies must be **identical** (including the single trailing LF).

5. **Idempotence re-check:** strip `idempotence_hash`, re-serialize the five-key preimage canonically, hash, and confirm equality with the published digest.

6. **AB↔BA:** repeat 2–5 with the pair order swapped; bytes must remain identical.

## C.4 Evidence produced (titles/paths only)

* Parity harness and scripts: dev harness, parity test modules, CLI parity scripts.

* AB↔BA goldens: paired outputs for A,B and B,A.

* Schema and LF tests: Reader and CLI schema checks with single-LF guards.

* Idempotence logs: preimage → sha256 → final recompute traces.

* Emitter identity: canonical emitter SHA-256 — see Appendix B.

* Service identity (ops): minimal internal identity payload — see Appendix B; transport/ops ownership in Governance (Appendix D, titles only).

See Appendix B (Evidence Index) for titles and paths.

## **C.5 Operational constraints**

* **Single emitter:** the harness **must** call the same presenter emitter as CLI (§10); no local serializers or ad-hoc `json.dumps`.

* **Canonical output:** UTF-8, sorted keys, compact separators, **exactly one LF**; success body has **exactly six keys** (§9.2).

* **Numeric-free public shape:** `categories[*]` are `{id, band}` only; v1 Alpha exposes **exactly one** `{"id":"harmony",…}` when `eligible==true` (§2.2).

## **C.6 Transport pointers (titles-only)**

Transport/HTTP behavior (e.g., conditional GET/HEAD, caching, headers, status semantics) and CLI stream policy are **not duplicated** here. They are referenced **by title only** in:

* **PF-Canon-HDE-CLI-API-Vendor-Ref** — CLI/Reader transport & validators.

* **PF-Canon-HDE-Governance** — A7 transport acceptance (conditional delivery, caching/writers).

## **C.7 Non-goals**

* No persistence or production routing.

* No public exposure of internal numerics or keys.

* No schema evolution outside the spec’s versioned process. 

## 

  

  # **Appendix D — Retired Features (removed) \[Normative Notice\]**

  ## **D.1 Prompt**

* **Status:** **Removed** from this specification.

* **Scope of removal:** The `prompt` field is **disallowed** in all **public** payloads and **must not** be preserved or injected by the Presenter. Any prior optional `categories[*].prompt` schema property is **deleted**; public items remain **exactly** `{id, band}`.

* **Administrative surfaces:** `prompt` **must not** appear in any admin/diagnostic/public narratives or envelopes going forward.

* **Rationale (one line):** Public Reader v1 is numeric-free and narrative-free; `prompt` risks drift and policy violations without advancing the math contract.

* **Effective date:** **2025-10-19** (first removed in PF-Review-HDE-Math-Spec v0.3 and retained in later versions).

  ## **D.2 Uncertainty**

* **Status:** **Never shipped**; any references are **excised** from this spec.

* **Scope of removal:** No uncertainty fields, tokens, or narratives are defined or permitted on public or admin surfaces.

* **Rationale (one line):** Uncertainty signaling is out of scope for Reader v1 and introduces non-deterministic interpretations inconsistent with the fixed math contract.

* **Effective date:** **2025-10-19** (document scrub complete in PF-Review-HDE-Math-Spec v0.3+).

**Operational impact:** None. The **public contract** remains unchanged (six-key success; bands-only; single `harmony` in v1 Alpha; canonical serialization and idempotence). No transport bytes are altered by these retirements. 

# **Appendix E — Composite fingerprint v1 (fixtures spec) \[Required-Now\]**

**Purpose (normative).** Provide a minimum-information, canonical, order-independent JSON artifact that witnesses composite determinism for CI and parity checks. This artifact is **derived** (not part of the public Reader contract) but its shape is **normative** for validation. All serialization uses canonical JSON (see **HDE-Schemas and Artifacts §4**: UTF-8 no BOM, object keys ASCII-sorted, arrays ASCII-sorted and deduplicated, exactly one trailing `\n`).

## **E.1 Shape (keys, domains, ordering)**

The fingerprint object has **exactly four keys**, emitted in **ASCII key order**:

{

  "centers\_defined": \["ajna", "g\_center", "root"\],

  "channels\_defined": \["07-31", "10-20", "29-46"\],

  "channels\_em": \["10-20"\],

  "throat\_em": true

}

**Domains & constraints (normative)**

* **centers\_defined** — Array of distinct center ids (strings), each in the closed set  
   `{"head","ajna","throat","g_center","ego","spleen","sacral","solar_plexus","root"}`; ASCII-sorted.  
* **channels\_defined** — Array of distinct channel ids in canonical `NN-NN` form (two zero-padded gate ids, min-first), ASCII-sorted. Each element **MUST** match  
   `^(?:0[1-9]|[1-5][0-9]|6[0-4])-(?:0[1-9]|[1-5][0-9]|6[0-4])$` (see **HDE-Schemas and Artifacts §2.1**).  
* **channels\_em** — Array of distinct channel ids, ASCII-sorted, and **subset of** `channels_defined`; each id is a canonical `NN-NN` whose endpoints are both defined in the composite and owned by **opposite** members (A/B).  
* **throat\_em** — Boolean; `true` iff any `channels_em` element is incident to **throat**.

## **E.2 Construction procedure (success case)**

1. **Normalize inputs** `(A,B)` per **HDE-Schemas and Artifacts §2.1** (apply declared ingestion aliases; build the AB composite over `centers.json`/`gates.json`/`channels.json` using canonical `NN-NN` identities).  
2. **Derive sets from the composite (no partial inference):**  
   * `channels_defined` \= all catalog channels whose **both** gate endpoints are present.  
   * `centers_defined` \= all centers incident to `channels_defined`.  
   * `channels_em` \= those `channels_defined` completed by **opposite** ownership across A/B.  
   * `throat_em` \= `true` iff any `channels_em` touches **throat**.  
3. **Canonicalize.** ASCII-sort each array; dedupe exact duplicates; emit the four keys in ASCII key order; serialize canonically (**HDE-Schemas and Artifacts §4**) with one trailing `\n`.  
    **Pins.** Run byte checks with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

## **E.3 Validation (binary)**

* **Keys:** exactly `{"centers_defined","channels_defined","channels_em","throat_em"}` (no extras).  
* **Arrays:** ASCII-sorted; no duplicates.  
* **Domains:** `channels_defined` entries match the `NN-NN` regex above; `centers_defined` entries are in the closed center set; `channels_em ⊆ channels_defined`.  
* **AB↔BA:** Fingerprints for `(A,B)` and `(B,A)` are **byte-identical** (after canonical serialization).  
* **Two-run identity:** Two runs on the same inputs/pack produce **byte-identical** fingerprints (checks with `LC_ALL=C`, `LANG=C`, `TZ=UTC`).

## **E.4 Change control**

The fingerprint’s keys, domains, and canonicalization rules are **frozen** for v1 CI. Any change to this shape or ordering is a **test-format** change and must update CI and evidence via Doc-Delta (see **HDE-Governance**).

**Acceptance & CI (titles-only).**

* `COMPOSITE_ABBA_IDENTITY_OK` — AB/BA fingerprints are byte-identical.  
* `TOPOLOGY_COHERENCE_OK` / `XREF_MEMBERSHIP_OK` — `NN-NN` validity; center/channel closure.  
* `JSON_CANONICAL_CHECK_OK` — canonical JSON (UTF-8, sorted keys, deduped ASCII arrays, one LF).  
* `TWO_RUN_IDENTITY_OK` — repeatability on same inputs/pack.  
* `EVIDENCE_INDEX_UPDATED_OK` — fingerprint files and compare logs registered in the Index (and mirrored 1:1 in `artifacts/evidence_index.jsonl` with path-proofs).

**Routing.** The fingerprint is **not** part of the Reader contract. Transport behavior (headers, conditionals) is owned by **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (titles only).

---

