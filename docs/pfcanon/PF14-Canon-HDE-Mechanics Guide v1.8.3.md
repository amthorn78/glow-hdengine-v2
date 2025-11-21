# PF14-Canon-HDE-Mechanics Guide

**Version:** v1.8.2  
 **Status:** Canon  
**Effective date:** 2025-11-21

**Last Update Gate:** HDE-EPIC017 planning r1

## **Purpose — Components & build tasks (Mechanics scope)**

Mechanics wires and **proves** the HD Engine for production. It does **not** restate Math formulas or public transport bytes.

**Public posture (Reader v1).** Bands-only, **numeric-free** public surface; resonance **SR-only** (α=1.0); **hysteresis \= 1** is armed for future XR and **not exposed**.

**Rules.**

* **Titles-only cross-refs** in body text (**no version numbers**).  
* **Single homes** (route by title; do not duplicate):  
   • **Public bytes:** PF-Canon-HDE-CLI-API-Vendor-Ref  
   • **Math:** PF-Canon-HDE-Math-Spec  
   • **Schemas/pack & canonical JSON:** PF-Canon-HDE-Schemas & Artifacts  
   • **Governance/acceptance & Evidence Index:** PF-Canon-HDE-Governance

**References (titles-only).**

* PF-Canon-HDE-Governance  
* PF-Canon-HDE-CLI-API-Vendor-Ref  
* PF-Canon-HDE-Math-Spec  
* PF-Canon-HDE Architecture  
* PF13 — Glow Development Philosophy  
* PF-Canon-HD Engine Epics Map  
* Glow HD Engine — Build Notes & Integration Addenda (Living)

**Provenance & deltas (informative).** Canonicalized from the REVIEW addenda and aligned with **PF10-HDE-Build Notes (Living)**. Rolled in previously-optional items (Server Cache; Reader conditional-GET helper). **Locked A7 transport posture**. Added the **/internal/version** ops posture (**no-store**, **no `ETag`**, **conditionals ignored**; **HEAD 200 with `Content-Type` parity**), clarified **optional `build_commit`**, and expanded Evidence Index captures with **same-PR updates**, **machine-mirror parity**, and **path-proofs**.

---

## **Preamble — Product scope**

**Viewer inputs & presets.** Presets are optional templates. Each user selects a top category and sets weights (`0..100`) across the ten Magic-10 IDs (closed set & order; titles-only to **HDE-Schemas and Artifacts §2.6** / **HDE-Math-Spec §5.1**). **Zero-weight rule:** if a viewer sets a category’s weight to `0`, candidates whose \#1 is that category are excluded.

**Engine outputs (internal/admin).** The engine computes per-category numbers (`0..100`) which map to bands (**Cool, Open, Warm, Glow**) using **inclusive-high** thresholds and `round_half_up` (titles-only to **HDE-Math-Spec §5.3**). The engine selects two narrative keys per category (personal, shared). The engine selects keys; it does not write copy. **Resonance posture (v1):** SR-only (`alpha=1.0`); XR is dormant and not part of public output.

**Public covenant (titles-only).** Public Reader payloads are **bands-only and numeric-free**; internal numbers remain admin-only. Public bytes & schemas live in **HDE-CLI-API-Vendor Ref** by title. **Canonical JSON** is required end-to-end: UTF-8 (no BOM), keys ASCII-sorted, compact separators, exactly one trailing LF; arrays used as sets are deduped & ASCII-sorted. **Determinism:** AB↔BA parity and two-run identity hold; Reader↔CLI parity is required; all checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Cross-doc references in this guide are **titles-only** (no version numbers), with math/transport/ops details routed to their single homes.

---

# **HD Engine — the plain story**

## **What it is**

The HD Engine computes per-category compatibility and drives which copy lines appear. It selects and routes copy via a deterministic system. It does not generate text.

## **What it is for**

* Power connection matching from user priorities and weights across ten categories.  
* Give explanations, not only scores: two short narrative lines per category (one personal, one shared) chosen by rules (no HD jargon in user copy).  
* Let admins tune numbers safely while user-visible results remain stable and understandable.

## **What it does**

* Compute pair results across ten categories

  * A number from 0 to 100 per category for admin/test.  
  * A band per category (Cool, Open, Warm, Glow) derived from the number.  
* Drive narrative output (no copywriting)

  * Produce narrative keys and selection signals for each category and perspective (personal/shared) using viewer intent and routing flags.  
  * Determinism and AB↔BA parity for pair views.  
* Respect user intent

  * User chooses \#1 category and weights; zero-weight rule enforced.  
* Return stable compact JSON

  * Admin/test JSON may include per-category numbers and bands with narrative keys and minimal meta.  
  * Public Reader remains bands-only; public payload bytes are defined in CLI/API.  
* Support the swipe/feed

  * Rank candidates by viewer weights and diversify results.

## **What it does not do**

* No copywriting; the engine selects keys only.  
* No public UI; the engine sits behind the app.  
* No direct Internet exposure.  
* No business policy beyond inputs; app controls product flow.

# **Components and tasks**

Numbering is stable. New inserts use letter suffixes to preserve references.

You’re right. I over-specified repo paths and target names. That invites drift. I’ve rewritten the section to be **capability-level and titles-only**, with no pinned paths or tool names.

---

## **1\) Repository & Tooling Skeleton (capabilities, not paths)**

**Scope (normative).** Mechanics requires a **set of capabilities** that enable determinism, transport acceptance, and evidence generation. The **concrete repository layout, file names, and tool targets are implementation-defined** and **must not be pinned** here. This section states *what must exist*, not *where or how*.

### **1.1 Capabilities the repo must provide**

* **Adapter surface (HTTP only).** Wires Reader routes and the ops endpoint; **does not define public bytes** (route by title to PF-Canon-HDE-CLI-API-Vendor-Ref).  
* **Mechanics core.** Pure orchestration for math, comparators, config loader, and public emitter wiring (route math to PF-Canon-HDE-Math-Spec).  
* **Schemas & validation.** JSON-Schema validation for governed inputs; AJV (or equivalent) CI step that fails on schema drift (route schema/canonical rules to PF-Canon-HDE-Schemas & Artifacts).  
* **Evidence indices.**  
  * **Human index** (titles/paths only) in this repo, **updated in the same PR** as artifacts.  
  * **Machine JSONL mirror** (records-only) owned by PF-Canon-HDE-Schemas & Artifacts; CI enforces **1:1 parity** and **path-proofs** for every record.  
* **Ops artifacts.** Start-command capture (bytes \+ hash), health/ready checks; no secrets in logs; SAFE rails defaults enforced per Governance.  
* **Scriptable pipeline.** A single **sanity pipeline** (name is implementation-defined) that runs, in order: formatting → lint/type → unit/prop tests → schema checks → goldens/evidence capture → **index & mirror parity \+ path-proof validation**.

### 1.2 Environment & secrets (names-only)

**Env allow-list.**  
 Defined by title (HDE-Schemas & Artifacts / HDE-Governance). CI **fails** on unknown or missing required keys; secrets are never printed (keys-only logs with redaction).

**Rails posture (derives from PF07).**  
 Rails defaults follow the **Env Deployment Inventory** (titles-only): **dev & stage OPEN**, **prod CLOSED**, **CI CLOSED**. This guide does not restate the table; it defers to Infrastructure.

**CI default CLOSED & evidence.**  
 CI pipelines run with rails **CLOSED by default**. Any pre-commit/CI job that **opens rails** must pin timeout/retry/backoff policy (closed domain) and attach governed evidence **in the same PR** (titles-only routing to Governance/Schemas & Artifacts).

**Determinism pins (all environments).**  
 Any canonicalization, hashing, header snapshotting, or governed evidence capture **MUST** run with:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

Acceptance (names-only): `ENV_LC_ALL_C_OK`.

### 1.3 Evidence & CI coupling \[Required-Now\]

**Scope (normative).** Mechanics must keep human and machine evidence in lockstep for every artifact this guide produces (math proofs, goldens, headers‑only snapshots, scripts). Transport bytes and ops surfaces are routed by title only to **HDE‑CLI‑API‑Vendor Ref** and **HDE‑Governance**.

**Single homes**  
 **Human index.** `docs/evidence/INDEX.json` — titles and paths only; no payload bytes. Must maintain **1:1 parity** with the machine mirror (see §8.3).  
 **Machine mirror (records‑only).** `artifacts/evidence_index.jsonl` — fixed path; one JSON object per line; canonical JSON (UTF‑8, no BOM; sorted keys; compact; exactly one trailing `\n`). This section surfaces the minimum shape used by implementers; the **normative mirror schema lives in PF12**.

**Mirror discipline (normative).** The machine mirror is **one and only one** file at `artifacts/evidence_index.jsonl`; **records‑only canonical JSONL** (UTF‑8; **ASCII‑sorted keys**; compact; **exactly one LF per record**); **unknown keys are rejected**; **sort‑before‑write** by (`artifact_key`,`discovered_physical_path`).  
 **Exact field order (per PF12/PF10):**  
 `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

**Join rule.** (`artifact_key`, `discovered_physical_path`) in the mirror equals (`title`, `path`) in the human Index (**1:1**).  
 **Unknown keys.** Rejected (**fail CI**).

**Path‑proofs (MUST).** Store a `path_proof.txt` (or equivalent) alongside each artifact with a stat transcript (size, mtime, sha). Reference it via `proof_anchor` in the mirror record.

**Update discipline (same PR).** Whenever any golden, snapshot, or script moves or changes, **update Appendix D and the machine mirror in the same commit/PR**. CI fails on mismatch.

**Environment pins (determinism).** All captures and comparisons run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Arrays that represent sets are deduped and ASCII‑sorted before hashing and compare.

**Pipeline coupling (minimum sequence).**

1. Build and normalize.

2. Run unit and property tests.

3. Produce artifacts (goldens, headers‑only snapshots, logs).

4. Write or refresh **human Index** entries.

5. Write **mirror** records with path‑proofs.

6. CI parity check: 1:1 human↔machine, schema‑valid, canonical JSONL.

7. Fail closed on any drift.

**Acceptance and CI (titles‑only; token names live in HDE‑Governance §2.0).**  
 `EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_MIRROR_OK · EVIDENCE_PATHS_VALIDATED_OK · JSON_CANONICAL_CHECK_OK · EVIDENCE_INDEX_HASH_OK · MACHINE_MIRROR_UPDATED_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK · ENV_LC_ALL_C_OK`. *(Schema & tokens routed by title to PF12/PF09; this guide does not restate the mirror schema.)*

**Header snapshot normalization:** stored snapshots use **lower‑case header names**; values verbatim. **Acceptance:** `SNAPSHOT_HEADER_LOWERCASE_OK`.

**Routing (titles‑only).** Manifest and release identity and the mirror schema ownership live in **HDE‑Schemas & Artifacts**. Transport A7 proofs and `/internal/version` evidence live in **HDE‑CLI‑API‑Vendor Ref** and **HDE‑Governance**.

**Governed locations (normative).** All QA/audit proofs **MUST** reside under governed paths: `artifacts/**`, `audit/**`, and `docs/evidence/**`. Files under transient generators (e.g., `codex/out/**`) **MUST NOT** be indexed. Human Index and machine mirror updates **MUST** occur in the **same PR**; mirror is **records‑only canonical JSONL** (UTF‑8, ASCII‑sorted keys, compact, exactly one LF), rejects **unknown keys**, and carries a `proof_anchor` to a path‑proof file in the same dir. Gate on `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and `EVIDENCE_INDEX_HASH_OK`. (Routing by title to **HDE‑Schemas & Artifacts / HDE‑Governance**.) 

---

### **1.4 Routing (single homes; no duplication)**

* **Public bytes:** PF-Canon-HDE-CLI-API-Vendor-Ref  
* **Math & preimage:** PF-Canon-HDE-Math-Spec  
* **Schemas, pack/manifest, canonical bytes, machine mirror:** PF-Canon-HDE-Schemas & Artifacts  
* **Governance (A7, ops posture, Evidence Index policy):** PF-Canon-HDE-Governance

### **1.5 Acceptance (tokens; titles-only)**

* **Evidence & indices:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`  
* **Determinism:** `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`  
* **Rails posture:** `ENV_RAILS_POLICY_OK`  
* **Ops start-command:** `SERVICE_START_CMD_CAPTURED_OK`, `GUNICORN_APP_FACTORY_OK`, `ENV_PORT_REQUIRED_OK`

  ## **2\) Canonical Enumerations Registry**

**Purpose.** Wire and prove the frozen domain registries (centers, gates, channels, categories) used by the engine. Mechanics validates and snapshots the domains; **HDE-Schemas and Artifacts** is the single home for authoritative catalogs and schemas. Developer notes in this repo are informative only (never authoritative).

**Single homes (titles-only).**

* **Domains & schemas:** HDE-Schemas and Artifacts (§2.1 Centers/Gates/Channels; §2.6 Magic-10).  
* **Canonical JSON & machine mirror:** HDE-Schemas and Artifacts (§4, §8).  
* **Math semantics (ordering/banding):** HDE-Math-Spec (§2.2, §2.4, §5.x).  
  ---

  ### **2.1 Domain invariants (normative)**

* **Centers:** closed set; `snake_case` identifiers; ASCII; unique.  
* **Gates:** closed domain; numeric identity per schema; unique; each attached to a single center by catalog.  
* **Channels:** closed set of edges; canonical `NN-NN` (zero-padded, min-first, ASCII hyphen); ASCII-sorted; unique; **no multi-hop encodings**.  
* **Categories (Magic-10):** closed ID set **with pinned order** (HDE-Schemas and Artifacts §2.6).  
* **Set semantics:** arrays that represent sets **MUST** be deduped and ASCII-sorted before hashing/compare (HDE-Schemas and Artifacts §4).  
* **Validation posture:** unknown IDs, duplicates, non-canonical channel forms, or schema mismatches **hard-fail** with typed errors.  
  ---

  ### **2.2 Validation & generation (mechanics)**

Mechanics provides a single **registry job** that:

1. **Load & validate** each domain against its HDE-Schemas and Artifacts JSON-Schema (titles-only).  
2. **Normalize channels** to `NN-NN` min-first and enforce ASCII sort \+ dedupe for set-arrays.  
3. **Prove closure & uniqueness** (no extras/omissions, no duplicates, no cross-catalog drift).  
4. **Emit a registry snapshot** (records-only metadata: domain name, item counts, canonical `sha256/size` of each governed artifact) and **index it** in the machine mirror at `artifacts/evidence_index.jsonl`.  
5. **Update the human Evidence Index** (Appendix D) **in the same change**; CI enforces human↔machine **1:1 parity** and **path-proofs** (`discovered_physical_path` \+ `proof_anchor`).  
6. **Pins (determinism).** All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`; JSON is canonical (UTF-8 no BOM, sorted keys, compact, one LF).

**Seeds (catalogized; admin/test).** If Seeds are present in HDE-Schemas and Artifacts, they are admin/test-only and treated as **frozen inputs**; any change **bumps `release_id`** (HDE-Schemas and Artifacts §6; HDE-Math-Spec §5.1.1). Seeds are **not public** in Reader v1.

---

### **2.3 Artifacts (records-only; path-agnostic; indexed via the machine mirror)**

List by **title/path** in Appendix D and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; one LF; canonical JSON).

* **`domain_snapshot`** — counts & identities (`sha256/size`) for centers/gates/channels/categories.  
* **`closure_report`** — proofs of domain closure & uniqueness; channel-normalization **reject corpus** (non-canonical inputs → errors).  
* **`registry_checksums`** — summarized checksums for governed artifacts (for quick diffing).  
  ---

  ### **2.4 Acceptance (tokens; titles-only)**

* **Domains closed & frozen:** `CATALOG_DOMAIN_CLOSED_OK`, `M10_DEFS_OK`, `MAGIC10_NAMES_FROZEN_OK`.  
* **Orientation & normalization:** `CATALOG_ORIENTATION_CANON_OK` (channels `NN-NN` min-first; ASCII-sorted; deduped).  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Seeds (when present):** `M10_SEEDS_OK`, `RELEASE_ID_RECOMPUTE_OK` (manifest bump on change).  
  ---

## **3\) Programmatic Configuration System**

**Purpose (normative).** Provide a **typed, deterministic configuration surface** for the engine and its clients. The system loads governed catalogs, **validates & normalizes** them, **fails on unknown/duplicate IDs**, and **emits typed artifacts** for FE/BE alongside a **registry report**. Concrete file names and directories are **implementation-defined** and **not pinned here**.

**Single homes (titles-only).**

* **Domains/schemas & canonical JSON rules:** PF-Canon-HDE-Schemas & Artifacts (§2, §4, §8).  
* **Math semantics (constants, ordering/banding):** PF-Canon-HDE-Math-Spec.  
* **Governance (evidence policy & tokens):** PF-Canon-HDE-Governance.

### **3.1 Loader behavior (normative)**

* **Unknown/duplicate IDs → fail build.** The loader **MUST** hard-fail (typed error) on any unknown identifier, duplicate entry, schema mismatch, or non-canonical channel form.  
* **Alias policy \= OFF (default).** No implicit aliases. If an allow-list is explicitly enabled, only **declared aliases** are recognized; all others **fail**.  
* **Normalization.** Channel IDs normalize to **zero-padded `NN–NN` (min-first)**; arrays that represent sets are **deduped & ASCII-sorted** before hashing/compare.  
* **Determinism.** Output is **order-neutral (AB↔BA)**, **locale-neutral** (`LC_ALL=C`), and **two-run identical**; canonical JSON is **UTF-8 (no BOM), sorted keys, compact, exactly one LF** (PF-12 §4).

### **3.2 Typed artifacts (codegen) — outputs, not paths**

* **FE typed constants bundle.** A generated artifact that exposes **closed enums/domains** and **read-only constants** needed by the FE client (e.g., category IDs, band labels), typed and **immutable**.  
* **BE enums & constants bundle.** A generated artifact that exposes the same **frozen domains** to backend code (enums, discriminated unions), typed and **immutable**.  
   *(The exact filenames/locations are implementation-defined; Mechanics only requires that both bundles exist and are **consistent, typed, and deterministic**.)*

### **3.3 Registry report (records-only; machine-readable)**

Emit a **registry report** documenting the **effective** configuration for this build.

* **Required fields (minimal):**  
   `version` (string), `generated_at_utc` (ISO-8601 “Z”),  
   `alias_policy` (`OFF` or `ON` \+ allow-list),  
   `enabled_features` (array; set-semantics),  
   `catalog_counts` (object with stable keys),  
   `rejects` (sorted array with reasons), `warnings` (sorted array).  
* **Serialization:** canonical JSON (PF-12 §4).  
* **Indexing:** appear as a **records-only** entry in the **PF-12 machine JSONL mirror** with `sha256`, `size_bytes`, `produced_at_utc`, **discovered `physical_path`**, and a **path-proof** (transcript anchor \+ on-disk stat). Update the **human Evidence Index** in the **same change**; CI enforces **1:1 parity**.

### **3.4 Validation (binary)**

1. **Schema & domain closure:** all catalogs validate; no unknown/duplicate IDs; channels canonicalized; categories match the **closed** Magic-10 set.  
2. **Alias policy:** `OFF` by default; if `ON`, only allow-listed aliases pass; all others fail.  
3. **Typed artifacts:** FE and BE bundles are **type-complete**, **immutable**, and **consistent** across runs (two-run identity).  
4. **Determinism:** re-running the loader yields identical bytes for codegen bundles and the registry report.  
5. **Evidence:** human Index and PF-12 mirror contain synchronized records with **path-proofs**; canonical JSON lints pass (UTF-8/no BOM, sorted keys, one LF).

### **3.5 Acceptance (tokens; titles-only)**

* **Config loader/report:** `CONFIG_GEN_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`.  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Domains closed/canonicalization (supporting):** `CATALOG_DOMAIN_CLOSED_OK`, `CATALOG_ORIENTATION_CANON_OK`, `M10_DEFS_OK`.

### **3.6 Routing (no duplication)**

* Canonical rules & mirror schema: **PF-Canon-HDE-Schemas & Artifacts**.  
* Math semantics & constants: **PF-Canon-HDE-Math-Spec**.  
* Evidence policy & governance tokens: **PF-Canon-HDE-Governance**.

## **4\) Canonical Serialization Package**

**One serializer and one emitter for all public bytes** (Reader, CLI, evidence artifacts).

### **4.1 Policy (normative)**

* **Single presenter/emitter.** All public JSON bytes **MUST** be produced by one presenter/emitter entrypoint symbol. Reader and CLI **MUST** call this exact symbol (titles-only allow-list; no alternates). See §10.2 for the unified entrypoint and §10.1 for canonicalization; the preimage recipe is in §3.2.  
* **Canonical JSON.** UTF-8 (no BOM); ASCII-sorted keys; compact separators (`,` and `:` only); exactly one trailing LF (`\n`). Arrays that function as sets are **deduplicated and ASCII-sorted** by identity.  
* **Single source of bytes.** The same canonical serializer is used for Reader responses, CLI stdout on parity surfaces, and machine-generated evidence artifacts.  
* **Determinism.** **AB↔BA parity** and **two-run identity** **MUST** hold for identical inputs/environment. Run all canonicalization and byte-compares with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Tests use the same path.** Test code **MUST NOT** bypass the shared presenter/emitter.

### **4.2 Prohibited (hard fail)**

* **No ad-hoc serialization on public paths.** No `json.dumps(`, no `jsonify(`, no templated/string-built JSON, no framework helpers that bypass the presenter, no pretty/indented output, **no test-only shims**.

### **4.3 Allow-list (code/CI owned)**

* Maintain an explicit **allow-list of presenter/emitter symbols**. Only allow-listed symbols may serialize public bytes (allow-list owned in code/CI; not pinned here).

### **4.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* **Symbol parity.** Reader & CLI resolve to the same emitter entrypoint → `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`.  
* **Canonical bytes.** Encoding, key order, compactness, single LF, arrays-as-sets proven by canonical re-serialization byte-compare → `JSON_CANONICAL_CHECK_OK`.  
* **Determinism.** `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`.  
* **Evidence discipline.** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

### **4.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

List by **title/path** in **Appendix D: Evidence Index** and add **1:1** records in `artifacts/evidence_index.jsonl` (each with `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF). Examples:

* **`grep_guard/serializer`** — proves no ad-hoc serializers on public paths (CI regex results).  
* **`emitter_symbol/proof`** — import-graph/reflection proof that Reader and CLI call the same presenter symbol.  
* **`canonical_json/check`** — policy check (UTF-8/no BOM, sorted keys, compact, one LF).  
* **`canonical_json/compare`** — byte-compare of public bytes vs canonical re-serialization (expected empty diff).

### **4.6 Routing (titles-only)**

Transport and HTTP behavior (headers, conditional delivery, caching) and CLI stream policy live in **HDE-CLI-API-Vendor Ref**; token roster in **HDE-Governance**.

---

## **5\) Deterministic Tie-Break & Total-Order Module \[Required-Now\]**

**Purpose.** Provide reusable comparators and helpers that impose a total, deterministic order over strings, numeric tuples, and domain identities the Engine uses. These utilities are called wherever ordering is consumed (selection, aggregation, snapshotting, evidence), ensuring **AB↔BA** neutrality and **two-run** identity. All byte-sensitive checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **5.1 Comparator policy (normative)**

* **Locale-free, bytewise order.** All string ordering is **ASCII byte order** (code-point ascending), case-sensitive, under `LC_ALL=C`. No locale collation; no Unicode normalization.  
* **Stable total order.** Comparators are **antisymmetric**, **transitive**, and **total** (every pair comparable). Equal inputs are **stable** (no reordering of equals).  
* **Arrays-as-sets discipline.** When an array is used as a set: **dedupe by identity**, then **ASCII-sort** with the appropriate comparator; never rely on map/set iteration order.  
* **No clocks/RNG.** Tie-breaks never consult time or randomness.

  ### **5.2 Domain comparators (exact)**

* **IDs (general strings).** `cmp_id(a,b)` → ASCII bytewise comparison.  
* **Magic-10 categories.** `cmp_category(a,b)` → compare by **frozen Magic-10 rank** (titles-only to **HDE-Schemas and Artifacts §2.6** / **HDE-Math-Spec §5.1**); if still equal (should not occur), fall back to `cmp_id`.  
* **Centers (snake\_case).** `cmp_center(a,b)` → `cmp_id(a,b)` over center IDs.  
* **Channels (NN-NN).** `cmp_channel(a,b)` → compare first the **left NN** (two-digit ASCII), then the **right NN**. Inputs **must already be canonical** `NN-NN` (min-first, zero-padded, ASCII hyphen `-`).  
* **Numeric then id (tuples).** For `(value, id)` (for example, equal-score ties):  
  1. sort **numeric ascending** (integers `0..100`),  
  2. break ties with `cmp_id` (stability preserved).  
      *Descending variants* use an explicit **descending numeric comparator** (do not negate and re-sort), then the same `cmp_id` tie-break.

  ### **5.3 Helpers (reusable)**

* **`dedupe_sort(set_like, cmp)`** → returns unique, ASCII-sorted array using `cmp`.  
* **`sort_pairs(pairs, key_cmp, val_cmp)`** → stable sort over `(key,val)` with `key_cmp` then `val_cmp`.  
* **`ensure_total_order(cmp, generator)`** → property-test harness asserting antisymmetry, transitivity, and totality for domain samples.  
* **`canonicalize_array(arr, cmp)`** → enforce set discipline (**dedupe \+ ASCII sort**) prior to canonical JSON emission.

  ### **5.4 Engine call-sites (must use)**

* **Composite surfaces.** Ordering of `channels_defined`, `channels_em`, `centers_defined` **must** use `cmp_channel` / `cmp_center` before emission/evidence (see **Appendix E — Composite fingerprint**).  
* **Category iteration.** All multi-category passes **must** iterate in the **frozen Magic-10 order** (titles-only **HDE-Schemas and Artifacts §2.6**); never rely on hash iteration.  
* **Presenter paths.** Before canonical serialization, arrays-as-sets **must** pass through `dedupe_sort` with the appropriate comparator.

  ### **5.5 Determinism & neutrality**

* **AB↔BA identity.** Using the same comparators on normalized `(A,B)` and `(B,A)` yields **identical** arrays/tuples.  
* **Two-run identity.** Re-running with the same inputs produces **byte-identical** sequences after canonicalization.  
* **Serializer coupling.** Canonical dumps use UTF-8 (no BOM), sorted keys, compact, exactly one LF (§4/§10.1), with arrays already **deduped & ASCII-sorted**.

  ### **5.6 Validation (binary & property tests)**

1. **Property tests:** for each domain comparator, prove **antisymmetry**, **transitivity**, **totality** over generated samples.  
2. **Set discipline:** `dedupe_sort` removes duplicates and preserves canonical order (idempotent on already-canonical arrays).  
3. **Channel ordering:** given mixed `NN-NN` arrays, verify strictly increasing `(left,right)` pairs and **min-first** orientation; reject non-canonical tokens.  
4. **Category loop:** verify the iteration order equals the **frozen Magic-10** index sequence (titles-only **HDE-Schemas and Artifacts §2.6**).  
5. **ABBA / two-run:** byte-compare outputs for `(A,B)` vs `(B,A)` and across two identical runs (must match).  
6. **Serializer cross-check:** canonical re-serialization byte-compare (UTF-8, no BOM, one LF).

   ### **5.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (**records-only JSONL**; UTF-8 no BOM; sorted keys; compact; exactly one LF). Each mirror record includes:  
 `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update human Index and mirror **in the same PR**; CI enforces 1:1 parity and **path-proofs**.

* **`order/props_total_order`** — property-tests pass (antisymmetry/transitivity/totality).  
* **`order/channels_sorted`** — channel identity ordering proof.  
* **`order/categories_iter`** — Magic-10 loop order proof.  
* **`order/abba_identity`** — AB↔BA byte-equality using these comparators.  
* **`canonical/json_compare`** — canonical dump compare (arrays deduped & ASCII-sorted).

**Routing (titles-only).**

* Frozen Magic-10 order & IDs: **HDE-Schemas and Artifacts §2.6**, **HDE-Math-Spec §5.1**.  
* Canonical JSON rules & fingerprint shape: **HDE-Schemas and Artifacts §4**, **HDE-Math-Spec Appendix E**.  
* Governance tokens roster: **HDE-Governance §2.0 Acceptance Tokens**.  
  ---

  ## **6\) Deterministic Engine Core \[Required-Now\]**

**Contract.** The Engine Core is **pure compute** (ops, scoring, aggregation). It performs **no I/O**, uses **no clocks**, reads **no globals/env**, and does **not** depend on system locale. All behavior is driven by **explicit inputs** and **frozen pack/preset constants** (titles-only to **PF-Canon-HDE-Schemas & Artifacts** / **PF-Canon-HDE-Math-Spec**).

### **6.1 Inputs & state (explicit only)**

* **Explicit parameters.** All data (composite, feature flags, constants, viewer\_prefs) is passed **by value** or via a **typed config object**.  
* **No hidden sources.** Do **not** read files, environment variables, or the clock; do **not** mutate module globals or singletons.  
* **Preconditions satisfied upstream.** Alias normalization, tz resolution, and ingestion occur **before** the core (titles-only to PF-Canon-HDE-Schemas & Artifacts §2.1 / PF-Canon-HDE-CLI-API-Vendor-Ref §3.2).

  ### **6.2 Determinism pins**

* **AB↔BA neutral.** Core results are **identical** when inputs `A,B` are swapped (AB \== BA after normalization).  
* **Two-run identity.** Two evaluations over the same inputs \+ constants produce **byte-identical** results.  
* **Stable iteration.** Do **not** rely on unspecified map/set iteration order: reduce over **ASCII-sorted keys**; arrays-as-sets are **deduped & ASCII-sorted**.  
* **Locale & serializer.** All canonicalization/compares run under **`LC_ALL=C`**. Any JSON the core emits for evidence uses the **canonical serializer** (UTF-8 no BOM, sorted keys, compact, **exactly one LF**).  
* **Numeric rules (titles-only).** Follow **PF-Canon-HDE-Math-Spec** for integerization and rounding (**round\_half\_up**); avoid floating-point accumulation for public-path numerics—use integer/fixed-point paths defined in **PF-01**.

  ### **6.3 Concurrency & parallelism**

* **Allowed if deterministic.** Parallel evaluation is permitted **only** when reductions/merges are **order-invariant** (commutative/associative) and the final ordering is **stabilized (ASCII sort)** before exposure.  
* **No race-driven clocks/RNG.** Do **not** consult time or RNG; if samplers/rankers require stochastic behavior, they **must be seeded and isolated** (see local policy section on stochastic samplers).

  ### **6.4 Errors & logging (internal only)**

* **Typed errors.** Fail fast with **typed, numeric-free** errors; do **not** include vendor payloads.  
* **No payload/secret logging.** Keys-only diagnostics; redact secrets; never echo request/response bodies.

  ### **6.5 Acceptance (binary)**

1. **Two-run identity:** run core twice on the same inputs → **byte-equal** outputs.  
2. **ABBA:** swap `A,B` → outputs (and any core-level artifacts) **byte-equal**.  
3. **Stable order:** arrays-as-sets are **deduped & ASCII-sorted**; reductions use **sorted keys**.  
4. **Serializer check** (if core emits JSON artifacts): canonical re-serialization byte-compare (UTF-8, no BOM, **one LF**).  
5. **No I/O/clocks/globals:** static/grep-guard \+ import-graph proof show **no file/env/time** access in core modules.

   ### **6.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* **artifact\_key:** `engine/tworun_identity` — two-run proof.  
* **artifact\_key:** `engine/abba_identity` — ABBA compare.  
* **artifact\_key:** `canonical_json/compare` — canonical re-serialization proof (if core emits JSON artifacts).  
* **artifact\_key:** `guards/no_io_no_clock` — static/grep proof of **no I/O/clocks/globals**.  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`. The **human Evidence Index** (Appendix D) is updated **in the same change**; CI enforces **human↔machine 1:1 parity** and **path-proofs**.

**Routing (titles-only).**

* Numeric rules & public rounding/banding: **PF-Canon-HDE-Math-Spec**.  
* Canonical JSON & pack/manifest: **PF-Canon-HDE-Schemas & Artifacts**.  
* Governance tokens: **PF-04 — §2.0 Acceptance Tokens**.

Acknowledged — I may reformat structure/wording only to conform to canon and improve readability, while preserving substance.

---

## 7\) Category Framework (internal) \[Required-Now\]

### 7.1 Closed list & scaffolds for per-category calculators

**Purpose.** Wire per-category **subtotal → band** calculators with precedence hooks; do **not** restate Math or public payload schemas.

**Frozen category set & order (titles-only).** All category logic addresses the ten **Magic-10** identifiers in their fixed canonical order. Iteration order is **normative** and **MUST** be enforced via the total-order utilities (ASCII / `cmp_category`; see §5 and **HDE-Schemas & Artifacts §2.6**, **HDE-Math-Spec §5.1**).

**Per-channel semantics (normative).** Calculators consume **channel-scoped** primitives: every “channel” reference is the canonical **NN-NN** edge (min-first, zero-padded), not a free-form string or unordered gate pair. Junction gates `{10,20,34,57}` may appear in multiple channels; treat each channel **independently**. Arrays of channels used as sets **MUST** be **deduped & ASCII-sorted** by canonical identity (see §5 comparators and canonicalization rules in §4; titles-only to **HDE-Schemas & Artifacts §2.1**).

**Public vs internal.** Category **subtotals** and **narrative keys** are internal/admin artifacts. The **public Reader** surface stays **bands-only, numeric-free** and is specified in **HDE-CLI-API-Vendor-Ref** (titles-only). Mechanics wires the allow-listed **presenter/emitter** (§4) and does **not** duplicate public JSON schema.

---

### 7.2 Compatibility Engine (pair) — contract

**Inputs (typed; titles-only).**

* `a, b` — each is either an **ID** or a **full person payload** (**HDE-CLI-API-Vendor-Ref** Reader schema). Do **not** mix ID and payload for the same party; mixed forms ⇒ typed `invalid_input` (**HDE-CLI-API-Vendor-Ref** error catalog, titles-only).

* `viewer_prefs` — `top_category ∈ Magic-10` and `weights` for **all ten** categories as integers `0..100` (key set **must equal** Magic-10). **Zero-weight rule:** if a viewer assigns `0` to a category, candidates whose \#1 equals that category are excluded. *(Titles-only: **HDE-Math-Spec §5.1**; **HDE-Schemas & Artifacts §2.6**; **HDE-CLI-API-Vendor-Ref**.)*

**Execution (internal math; titles-only).**

* **Subtotaling.** Compute per-category integer subtotals (`0..100`) via the Feature Framework and **pack-frozen constants** (**HDE-Math-Spec §5.4.2**; see channel semantics in §7.1; core is **I/O-free** per §6).

* **Banding.** Map each subtotal to a band using **inclusive-high** thresholds `(24/49/74/100)` with `round_half_up` (**HDE-Math-Spec §5.3**).

* **Narrative keys.** Select `{personal_key, shared_key}` per category from governed ledgers; if absent, flag `missing_narrative_key` (**no implicit fallback**).

**Outputs (admin/test surface only; titles-only).**  
 `categories[10]` in canonical Magic-10 order, each `{ id, score:int, band, personal_key, shared_key }`; plus `meta{ engine_tag, release_id }`.  
 **Public Reader** continues to emit **bands-only**. Contract bytes & schema are owned by **HDE-CLI-API-Vendor-Ref** and must be produced by the allow-listed **presenter/emitter** (§4). **Do not** embed JSON samples in this guide.

**Determinism & acceptance (binary).**

* **AB↔BA parity & two-run identity.** With identical inputs, **subtotals, bands, and any admin snapshots** are identical across `(A,B)` vs `(B,A)` and across runs; any emitted admin JSON is **canonical** (UTF-8/no-BOM, sorted keys, compact, one LF; arrays **deduped & ASCII-sorted**; `LC_ALL=C`).

* **Order.** Category arrays appear in the **frozen Magic-10 order**; tests assert this via §5 comparators.

* **Typed errors.** Mixed input forms ⇒ `invalid_input`; unknown IDs or malformed `viewer_prefs` ⇒ `invalid_input` (**HDE-CLI-API-Vendor-Ref** error catalog, titles-only).

**Tokens (titles-only).** `CATEGORY_FRAMEWORK_OK`, `M10_DEFS_OK`, `M10_MAPS_OK`, `M10_SYMMETRY_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.

**Evidence (records-only; path-agnostic).** ABBA fingerprint consumption (**HDE-Math-Spec Appendix E**), two-run logs, canonical-compare logs; **register mirror entries** and **update the human Evidence Index** in the same change (**HDE-Governance Appendix D: Evidence Index**; **HDE-Schemas & Artifacts** mirror).

---

### 7.3 Band thresholds & tuning (admin)

**Registry only (titles-only).** Mechanics maintains the authoring workflow for number→band thresholds (global or per-category) and the associated tooling; it does **not** restate numeric values.

**Normative sources.** Inclusive-high policy and `24/49/74/100` global edges: **HDE-Math-Spec §5.3**. Per-category overrides and the constants pack: **HDE-Schemas & Artifacts** (constants & manifest rules).

**Visibility & evidence.** Thresholds and scores are **admin/test-visible only**; the public surface remains **bands-only**. Mechanics provides helpers to dump/apply sets and captures: **edge-case fixtures** (`24/49/74/100`) and **identity/stability proofs** (e.g., `sha256` over canonical **compat** bytes, including the final LF). All tuning artifacts are listed in the **Evidence Index** (**HDE-Governance Appendix D**) and must be updated in the **same PR**.

---

## **8\) Public Presenter & Emitter \[Required-Now\]**

Transforms engine outputs into the Reader/CLI **public envelope** and emits **canonical JSON** via the **allow-listed** presenter–emitter.

### **Policy**

* **Single emitter.** Reader and CLI **MUST** call the **same presenter–emitter entrypoint symbol** to build the public body (CI maintains a **symbol allow-list**; no alternates).  
* **Canonical serializer.** The presenter **MUST** use the **Canonical Serialization Package** (§4): UTF-8 (no BOM), **ASCII-sorted keys**, **compact JSON**, **exactly one trailing LF**; arrays-as-sets **deduped & ASCII-sorted**; all byte checks under **`LC_ALL=C`**.  
* **Public shape (titles-only).** The public payload shape is owned by **PF-Canon-HDE-CLI-API-Vendor-Ref** and **PF-Canon-HDE-Math-Spec**. Mechanics **does not duplicate** those bytes here.

  ### **Idempotence**

* **Preimage (five keys).** Compute `idempotence_hash` over the **canonical preimage**: an object with **exactly** `reader_version, eligible, categories, meta, release_id` (**no** `idempotence_hash` yet). (Preimage fields are defined in **PF-01 §3**.)  
* **Finalize.** Insert `idempotence_hash` (**lowercase 64-hex**) and **re-emit canonically** to produce the public bytes (**LF-terminated**).  
* **Identity coupling.** `release_id` is taken from the **freeze-pack manifest** (**PF-12 §6**); `meta.invocation_tag` participates in the preimage (**PF-01 §3**).

  ### **Parity**

* **Reader↔CLI.** On parity surfaces, **CLI stdout** **MUST** be **byte-identical** to the **Reader 200** body.  
* **AB↔BA.** For pair-sensitive flows, **AB** and **BA** **MUST** produce **identical** bytes.  
* **Two-run identity.** With identical inputs/environment, **two serializations** **MUST** produce **bitwise-identical** public bytes.

  ### **Prohibited**

* **No ad-hoc serialization or templating** on public paths (`json.dumps(`, framework helpers, string-built JSON, pretty/indented output). **Only** the allow-listed emitter may serialize public bytes.

  ### **Acceptance (tokens; titles-only)**

* **Symbol parity:** Reader & CLI resolve to the **same emitter entrypoint** → **CLI\_READER\_EMITTER\_PARITY\_OK**, **CLI\_NO\_ALT\_JSON\_OK**.  
* **Parity proofs:** byte-compare **CLI vs Reader** outputs; **AB↔BA** parity; **two-run identity** → **TWO\_RUN\_IDENTITY\_OK**, **COMPOSITE\_ABBA\_IDENTITY\_OK**.  
* **Canonical compare:** canonical re-serialization byte-compare (encoding, key order, compactness, one LF, arrays-as-sets) → **JSON\_CANONICAL\_CHECK\_OK**.  
* **Evidence discipline:** **EVIDENCE\_INDEX\_UPDATED\_OK**, **EVIDENCE\_INDEX\_MIRROR\_OK**, **EVIDENCE\_PATHS\_VALIDATED\_OK** (same-PR update; human↔machine parity; path-proofs).

  ### **Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* **artifact\_key:** `parity/reader_cli` — Reader↔CLI byte equality (public surface).  
* **artifact\_key:** `parity/abba_identity` — AB↔BA byte equality.  
* **artifact\_key:** `parity/two_run_identity` — two-run identity digest/log.  
* **artifact\_key:** `emitter_symbol/proof` — import-graph/reflection proof of shared presenter symbol.  
* **artifact\_key:** `canonical_json/compare` — canonical re-serialization byte-compare of the public body.  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`; update the **human Evidence Index** in the **same change**; CI enforces **1:1 parity** and **path-proofs**.

**Routing (titles-only).**  
 Public payload & headers: **PF-Canon-HDE-CLI-API-Vendor-Ref**. Preimage/rounding/banding: **PF-Canon-HDE-Math-Spec**. Evidence policy & tokens: **PF-Canon-HDE-Governance**.

---

## **9\) Reader & Compat endpoints**

### **9.1 Endpoint Catalog (JSON success) \[Required-Now\]**

**Purpose (normative).** Name the Reader **JSON success** routes eligible for A7 proofs. Entries are **titles-only**; bytes/examples live elsewhere.

**Scope & rules**

* **Single home.** This Catalog is the only place that lists success endpoints eligible for A7 proofs.  
* **Posture.** Catalog is **internal-only** and **env-gated per entry**; entries not gated for prod are unreachable in production.  
* **Proof surface.** A7 proofs **must** run on a route listed in this Catalog.  
* **Exclusions.** All `/internal/*` routes are excluded; `/internal/version` is operator-only and not A7-eligible (see HDE-Governance §10.5).

**Invariants to prove (titles-only)**

* **200:** quoted, strong `ETag`; `Vary: Authorization, Accept-Encoding`; success cache headers.  
* **HEAD:** status 200; validators mirror 200 (including `Content-Type`); `Content-Length == len(identity 200 body)`.  
* **304:** only after prior 200-with-body; **omit** `Content-Type` and **omit** `Content-Length`; validators mirror cached 200\.  
* **Encoding invariance:** for the same canonical LF-terminated body, `ETag` identity and effective `Content-Length` are stable across accepted `Accept-Encoding` (identity/gzip/br).  
* **Writers/errors posture:** non-success writers and error routes carry `Cache-Control: no-store` (recorded as headers-only evidence).

**Catalog files (single home)**

* `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) — lists **JSON success routes only**, each with an env-gate; `/internal/` is excluded.  
* `docs/ENDPOINTS_CATALOG.json.sha256` — sidecar hash of the canonical bytes.

**Proof artifacts (headers-only; one LF each)**

* `artifacts/proofs/endpoints_env_gate_proof.log` — proves non-prod entries are unreachable in prod.  
* `artifacts/proofs/success_get.txt` — GET 200 proof (quoted strong ETag, Vary).  
* `artifacts/proofs/success_head.txt` — HEAD parity with GET 200\.  
* `artifacts/proofs/success_304.txt` — 304 omission proof (CT/CL omitted; validators mirror).  
* `artifacts/proofs/success_encoding_invariance.txt` — identity/gzip/br invariance proof.  
* `artifacts/proofs/success_writers_errors.txt` — writers/errors no-store posture.

**Indexing (human \+ machine, same PR)**

* Update the **human Evidence Index** and mirror 1:1 in `artifacts/evidence_index.jsonl`.  
* The machine mirror is **records-only canonical JSONL** (UTF-8; ASCII-sorted keys; compact; **one LF**); **unknown keys are rejected**.  
* Each record includes: `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a **`proof_anchor`** to a co-located path-proof file.

* **Mirror schema pins.** The machine mirror follows the **exact field order** and CI tokens defined in **§1.3** (PF12/PF10): `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`; **sort‑before‑write**, **unknown‑key reject**, **one LF**.

**Acceptance (titles-only; tokens live in HDE-Governance §2.0)**  
 `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

---

### **9.2 Reader (dev harness only) \[Implemented (dev-only)\]**

* **Route (dev-only).** `GET|POST /api/reader?v=1` is a **dev harness** enabled only when `APP_ENV=dev`; rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`; no vendor I/O).  
* **Emitter.** Uses the **allow-listed shared presenter/emitter** (see §4 / §10.2); tests must **not** bypass the shared emitter.  
* **Dev error posture.** `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, **no ETag**.  
* **A7 proofs boundary.** Harness may capture headers for **local evidence**, but authoritative A7 proofs run on a **Catalog JSON success** route; `/internal/version` remains an ops exception (see HDE-Governance §10.5).  
* **Pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Rails posture.** Rails defaults follow the **Env Deployment Inventory** (titles-only). The dev harness **does not perform vendor I/O**; tests may run with rails closed for evidence capture, but the default environment posture itself is owned by Infrastructure.

**Optional GET semantics (for local evidence only)**  
 If an optional **GET** is exposed in the harness, it **must** follow PF10 invariants for captures, **without** becoming the A7 proof surface:

* **200:** strong, quoted `ETag`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`; canonical JSON, one LF.  
* **HEAD:** status 200; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF-terminated, pre-compression).  
* **304:** only after prior 200-with-body; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror cached 200\.  
* **Encoding invariance (optional evidence):** for the same canonical body, **ETag identity** and **effective Content-Length** are stable across accepted encodings (identity/gzip/br).  
* **POST (dev harness):** non-conditional; never returns 304\.

**Acceptance (tokens; titles-only)**

* Core harness: `JSON_CANONICAL_CHECK_OK`, `CLI_READER_EMITTER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`.  
* If GET captures are taken (local-only, non-authoritative): `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK` *(captures here are supplemental; authoritative proofs remain on the Catalog route per §9.1).*  
* Evidence discipline: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

**Evidence (records-only; machine mirror; same-PR rule)**

* `reader/dev/parity` — harness vs CLI stdout byte-compare (expected empty).  
* `canonical_json/compare` — canonical re-serialization compare (one LF).  
* *(Optional, if GET exposed)* `transport/headers_200`, `transport/headers_head`, `transport/headers_304`, `transport/encoding_invariance`.  
   List titles/paths in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (canonical JSONL, one LF) with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update human Index and mirror **in the same PR**, with **path-proofs**.

**Routing (titles-only)**

* Transport matrices & A7 policy: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.  
* Ops endpoint posture: **HDE-Governance §10.5**.  
* Domains, catalogs, canonical JSON rules: **HDE-Schemas & Artifacts**.

---

### **9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]**

* **Route.** `POST /api/compat/v1` (pair) — internal/admin surface (**not public**).  
* **POST non-conditional.** POST carries no validators and never returns 304\.  
* **GET (health).** Any GET used for probing carries **no body**.  
* **Emitter.** Same shared presenter/emitter as Reader (§4 / §10.2). Public JSON is canonical: UTF-8 (no BOM), sorted keys, compact, **one LF**; arrays-as-sets deduped & ASCII-sorted; run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Determinism.** AB↔BA parity and two-run identity hold; category iteration follows the **frozen Magic-10 order**.

**Acceptance (tokens; titles-only).**  
 `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`.

**Evidence (records-only; machine mirror).**  
 `compat/parity/abba_identity`, `compat/parity/two_run_identity`, `canonical_json/compare`. Update human Index and mirror **in the same PR**, with **path-proofs**.

**Ownership (titles-only).** Production transport matrices and public payload bytes are owned by **HDE-CLI-API-Vendor Ref** and **HDE-Governance**. Mechanics enforces wiring/determinism (single emitter, canonical JSON, AB↔BA/two-run) and **does not duplicate** public schemas or bytes.

---

### **9.4 Internal ops: `/internal/version` (ops-only) \[Required-Now\]**

**Purpose (normative).** Operator surface for identity and provenance. **Not** a JSON success route and **not** A7-eligible (see HDE-Governance §10.5).

**Behavior (prod posture)**

* **GET 200\.** `Content-Type: application/json; charset=utf-8`; `Cache-Control: no-store`; **no ETag**; **Last-Modified absent**; `Vary` optional.  
* **HEAD 200 (parity).** Mirrors GET validators; **no body**; `Content-Length == len(identity GET body)`; `Content-Type == GET`.  
* **Conditionals ignored.** Requests with `If-None-Match` / `If-Modified-Since` are ignored; **never 304**.  
* **Pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Evidence (records-only; machine mirror)**

* `artifacts/ops/internal_version/headers_get.txt` — raw GET headers (proves no-store, no ETag, correct `Content-Type`).  
* `artifacts/ops/internal_version/headers_head.txt` — raw HEAD headers (HEAD 200; `Content-Type == GET`; `Content-Length ==` identity GET).  
* `artifacts/ops/internal_version/body_get.json` — exact LF-terminated GET body (six keys in frozen order) \+ `artifacts/ops/internal_version/body_get.sha256`.  
* `artifacts/ops/internal_version/cond_if_none_match_headers.txt` — GET with `If-None-Match` (still 200).  
* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt` — GET with `If-Modified-Since` (still 200).  
* `artifacts/ops/internal_version/two_run_identity.log` — two-run byte identity log.  
   List each artifact by title/path in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor`. Update human Index and mirror **in the same PR**.

**Acceptance (titles-only; token names live in HDE-Governance §2.0)**  
`INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`, **`INTVER_CACHECTL_NOSTORE_OK`**, plus Index/Mirror parity tokens. *(Tokens roster lives in Governance.)*

**Routing (titles-only).** Policy lives in **HDE-Governance §10.5**; transport matrices for success routes live in **HDE-CLI-API-Vendor Ref** (A7 not applicable here).

---

## **10\) Writer Surfaces (API)**

**Purpose.** Provide **minimal, idempotent** writer endpoints (e.g., **preferences**) with **strict schema validation** and **deterministic effects**. Mechanics wires determinism and validation; **public transport rules and error headers live in Governance/CLI-API** (titles-only).

### **10.1 Contract (normative)**

* **Idempotent semantics.** Repeating the **same request** produces the **same effect** and response semantics (no double-writes, no drift).  
* **Strict schema.** Requests **MUST** validate against the governing schema (titles-only to PF-Canon-HDE-Schemas & Artifacts). **Unknown or extra keys are rejected** (typed error).  
* **Normalization.** Where arrays represent sets, **dedupe & ASCII-sort**; category/channel IDs must be **canonical** (Magic-10 closed set; `NN-NN` min-first for channels).  
* **Explicit inputs only.** Writers **do not** read clocks/env/files and **do not** depend on locale.

  ### **10.2 Transport posture (titles-only; owned by Governance)**

**Routing only.** Transport behavior is governed in **HDE-Governance §10** and matrices live in **HDE-CLI-API-Vendor Ref**. This guide does not restate headers or validator details.

**Writers and errors**

* `Cache-Control: no-store`; **no `ETag`**.  
* Errors: `Content-Type: application/json; charset=utf-8`; typed, numeric-free error bodies (see **HDE-CLI-API-Vendor Ref** error model).  
* Writers have **no HEAD/304 semantics**.

**Success endpoints (A7 proofs)**

* Proofs run only on a cataloged **Endpoint Catalog (JSON success)** route (see **HDE-CLI-API-Vendor Ref §5.6 / Appendix A**).  
* Details such as 200 `ETag`, cache policy, `Vary`, 304 omission rules, and HEAD parity are referenced by title in Governance; do not duplicate here.

**Internal ops**

* `/internal/version` is operator-only, **not** A7-eligible; behavior is specified in **HDE-Governance §10.5**.

**Acceptance (titles-only; tokens live in HDE-Governance §2.0)**

* Writers/errors: `EVIDENCE_INDEX_UPDATED_OK` (evidence present), plus Governance A7 family excluded for writers.  
* Success routes (owned by Governance): `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `READER_VARY_ACCEPT_ENCODING_OK`, `READER_VARY_AUTHORIZATION_OK`.  
* Internal ops: `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`.  
  ---

### **10.3 Determinism & safety**

* **Two-run identity (effect).** Two identical writer invocations over the same state produce **identical post-state** and the same response semantics.  
* **Order stability.** Any JSON emission (if the writer returns a body) uses the **Canonical Serialization Package** (§4): UTF-8 no BOM, **sorted keys**, compact, **one LF**; arrays-as-sets **deduped & ASCII-sorted**; checks under **`LC_ALL=C`**.  
* **No RNG/time.** Writers do **not** consult clocks or randomness; no non-deterministic merges.

### **10.4 Errors & logging (internal)**

* **Typed errors only.** `invalid_input`, `invalid_json`, `unknown_key`, etc. (PF-05 titles-only); **no PII/secrets**.  
* **Keys-only logs.** Never log request/response bodies, header values, or secrets; redact references; bounded labels.

### **10.5 Validation (binary)**

1. **Schema pass:** request validates; **unknown/extra keys → fail** (typed error).  
2. **A7 writers posture:** responses carry **`no-store`**, **no `ETag`** (titles-only to Governance).  
3. **Idempotence:** re-issuing the same request leaves state unchanged; response semantics unchanged.  
4. **Canonical bytes (if body present):** canonical re-serialization byte-compare passes (UTF-8/no BOM, sorted keys, **one LF**, arrays-as-sets).  
5. **No locale/I/O:** static/grep checks show **no** file/env/time use in writer modules.

### **10.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* **artifact\_key:** `writers/no_store_headers` — header proof (`no-store`, no `ETag`).  
* **artifact\_key:** `writers/schema_validation` — JSON-Schema validation log (unknown/extra → typed error).  
* **artifact\_key:** `writers/two_run_idempotence` — two-run idempotence/effect proof.  
* **artifact\_key:** `canonical_json/compare` — canonical re-serialization compare (if a body is returned).  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`. Update the **human Evidence Index** in the **same change**; CI enforces **human↔machine parity** and **path-proofs**.

**Routing (titles-only).**

* **Transport rules & error headers:** **PF-Canon-HDE-Governance** (A7; writers/errors).  
* **Error shapes & public bytes:** **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* **Schemas & canonical JSON:** **PF-Canon-HDE-Schemas & Artifacts**.

---

## **11\) Input Normalization & Validation Layer** 

**Scope.** Normalize IDs and **validate payloads against schemas** (titles-only to **PF-Canon-HDE-Schemas & Artifacts**). Mechanics **wires** the checks; it **does not restate** schemas here.

### **11.1 Viewer prefs (normative)**

**Closed set & types**

* `top_category ∈` **Magic-10** (frozen IDs; fixed order).  
* `weights` contains **exactly ten keys**, one per Magic-10 ID; each value is an **int `0..100`**.  
* `preset` is **optional** and, when present, is drawn from a **declared preset catalog** (titles-only).

**Zero-weight rule**

* If a weight is **0** for category **X**, candidates whose **\#1 \== X** are **excluded** (enforced in the sampler/ranker, §11.3).

**Aliases & unknowns**

* **Default alias policy \= OFF.** Unknown IDs **reject** with a **typed input error**.  
* If input aliases are **explicitly enabled**, they **must** normalize via the **declared alias ledgers** (titles-only to PF-Canon-HDE-Schemas & Artifacts A1/A4/A5). Outputs remain **canonical**.

**Canonicalization (inputs)**

* Input JSON is normalized to **UTF-8 (no BOM)**, **ASCII-sorted keys**, **compact**, **exactly one LF**; arrays-as-sets are **deduped & ASCII-sorted**. All byte checks run under **`LC_ALL=C`**.

**AB↔BA neutrality**

* Normalization **MUST** produce **identical normalized forms** for `(A,B)` and `(B,A)`.  
  ---

  ### **11.2 Validation (binary)**

1. **Completeness.** `weights` includes **all ten** category keys; each value is **int `0..100`**.  
2. **Invalid shapes.** Malformed/missing keys or floats ⇒ **`invalid_prefs`** (typed error).  
3. **Schema pass.** Payloads validate against their owning schemas (titles-only to PF-Canon-HDE-Schemas & Artifacts).  
4. **Canonical bytes.** **Re-serialize canonically** and byte-compare (must match); **one LF**, **no BOM/ANSI**.  
5. **ABBA check.** Normalized forms for `(A,B)` vs `(B,A)` are **byte-identical**.

**Routing (titles-only).**

* Magic-10 IDs & order: **PF-Canon-HDE-Schemas & Artifacts §2.6**, **PF-Canon-HDE-Math-Spec §5.1**.  
* Public Reader contract: **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* Canonical JSON & pack: **PF-Canon-HDE-Schemas & Artifacts §4**.  
* Governance tokens: **PF-04 — §2.0 Acceptance Tokens**.  
  ---

  ### **11.3 Swipe Sampler & Ranker**

**Purpose.** Build a candidate pool that respects viewer weights (including the **zero-weight rule**) and then **rank deterministically**. Deterministic \= **order-neutral (AB↔BA)** and **seedable** (when used in **dev/admin** flows); **seeds never affect public bytes**.

#### **11.3.1 Sampling & exclusion**

* **Zero-weight rule.** Exclude any candidate whose **\#1** equals a viewer weight of **0**.  
* **Pool formation.** Apply viewer **eligibility filters** (titles-only), then enforce **diversity** (§11.3.3) **before** ranking.

  #### **11.3.2 Scoring & ranking (deterministic)**

* **Score function.** Deterministic **fixed-point** combination across the ten categories (integer path), consistent with **PF-01** rounding/banding (titles-only).  
* **\#1 influence.** The other party’s **\#1** may serve as a **stable tie-break** (integer/priority rule); the rule **must be pinned** and **stable**.  
* **Total order.** Sort by the specified **numeric** direction, then break ties by **ID comparator (ASCII)** to guarantee a **stable total order** (§5).  
* **Seedability.** Any stochastic element (if used in **non-public** flows) **must be seedable & isolated**; the seed does **not** alter public bytes.

  #### **11.3.3 Diversity acceptance (deterministic)**

* **Sliding window:** `K = 50`.  
* **Cardinality bound:** at most `N = 2` share the same **design fingerprint** within the window.  
* **No recent repeats:** none repeat from the last `R = 20`.  
* **Fingerprint.** A **deterministic** function (titles-only to PF-Math/PF-Spec) used **only** for diversity checks (**never exposed**).

  #### **11.3.4 Dev-only sampling endpoint (optional harness)**

* **Endpoint (dev-only).** `POST /api/sample/v1` with body containing `viewer_prefs{…}` and optional `seed:int`.  
* **Response.** List of **candidate IDs only**; the app hydrates details. If a seed was provided, **echo it in `meta`**.  
* **Determinism.** With the same inputs/seed, the output is **byte-identical**; **AB↔BA** has no effect on ordering.

  #### **11.3.5 Validation & evidence (binary; path-agnostic)**

* **Zero-weight exclusion** demonstrably enforced.  
* **Stable order:** ABBA and two-run proofs; **comparator laws** honored (see §5).  
* **Diversity checks:** window `K`, bound `N`, and recent `R` constraints verified.  
* **Seed replay:** identical inputs/seed → **identical outputs**; seed echoed in `meta` when used.  
* **Canonical bytes:** outputs are canonical JSON (UTF-8 no BOM, sorted keys, compact, **one LF**).  
* **Evidence Index:** append artifacts (sampler snapshots, seed replay logs) **in the same PR**; **PF-12 machine mirror** lines present with **path-proofs**.

**Routing (titles-only).**

* Scoring/banding/rounding rules: **PF-Canon-HDE-Math-Spec**.  
* Public contract & transport: **PF-Canon-HDE-CLI-API-Vendor-Ref**, **PF-Canon-HDE-Governance (A7)**.  
* Canonical JSON rules: **PF-Canon-HDE-Schemas & Artifacts §4**.  
  ---


  ## **12\) Error Envelope & Token Set \[Required-Now\]**

**Purpose.** Provide a **central formatter** for typed, numeric-free errors. Public error transport (writers/errors `no-store`, headers) lives in **PF-Canon-HDE-Governance** and **PF-Canon-HDE-CLI-API-Vendor-Ref** (titles-only). **Identity/Meta** content has been moved to **§13 (Identity & Provenance Module)** and **§14 (Internal Meta Surface)** to avoid duplication.

### **12.1 Error envelope (normative)**

* **Shape (exact):** `{"ok": false, "code": "<lower_snake_token>", "error": "<human message>"}` — **only** these keys.  
* **Canonical JSON:** UTF-8 (no BOM), **ASCII-sorted keys**, compact, **exactly one trailing LF**; checks under **`LC_ALL=C`**.  
* **Numeric-free & secret-free:** never include stack traces, payload excerpts, header values, or secrets; keys-only logs (redacted).  
* **Deterministic mapping:** the same condition always yields the same `{code,error}` pair; **byte-stable** across Reader and CLI.

  ### **12.2 Token set (lower\_snake; examples)**

**Tokens include (non-exhaustive):**

* `invalid_prefs` — malformed/missing/float/out-of-range weights.  
* `missing_narrative_key` — no mapping for `(category, band, personal|shared)`.  
* `invalid_json` — mixed id/payload for `a`/`b` (or schema violation at envelope root).

The canonical **token→message map** is tested and stored as evidence (titles-only). Add/retire tokens via Doc-Delta; message text is stable and versioned in the map.

### **12.3 Transport (titles-only)**

* **Writers & errors posture:** `Cache-Control: no-store`; **no `ETag`**; `Content-Type: application/json; charset=utf-8` (PF-04).  
* **A7 success rules** are **not** restated here (see PF-04/PF-05).

  ### **12.4 Acceptance (binary; tokens & evidence are titles-only)**

1. **Schema:** envelope has **exactly** `ok=false`, `code`, `error`; no extras; LF-terminated, canonical JSON.  
2. **Casing & map:** all tokens are **lower\_snake**; the **token→message** table matches the golden map (**exact bytes**).  
3. **Parity:** the same error emitted by **Reader and CLI** is **byte-identical**.  
4. **Two-run identity:** re-emitting the same error twice produces **bitwise-identical** bytes.  
5. **Transport coupling:** when the envelope appears in writers/errors, headers match PF-04 (no-store; no `ETag`).

**Gating tokens (titles-only):** `ERROR_TOKEN_MAP_OK`, `ERROR_JSON_CANON_OK`, `CLI_READER_EMITTER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

### **12.5 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* **artifact\_key:** `errors/token_map` — canonical token→message snapshot (golden).  
* **artifact\_key:** `errors/schema_check` — JSON-Schema check for the envelope.  
* **artifact\_key:** `errors/canonical_check` — encoding/key-order/compact/LF proof.  
* **artifact\_key:** `parity/errors_reader_cli` — byte-equality for the same error via Reader and CLI.  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`; update the **human Evidence Index** in the **same change**; CI enforces **1:1 parity** and **path-proofs**.

**Routing (titles-only).**

* Error shapes & code map ownership: **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* Writers/errors transport posture: **PF-Canon-HDE-Governance**.  
* Canonical JSON & mirror rules: **PF-Canon-HDE-Schemas & Artifacts §4/§8**.  
* Engine identity & `/internal/version`: **§13** and **§14** (this guide does not duplicate those bytes).  
  ---

  ## **13\) Identity & Provenance Module \[Required-Now\]**

**Purpose.** Single source of truth for **engine** and **release** identity. Values are **initialized once per cut** and are **read-only thereafter**; all public and operator surfaces **consume via helpers** (no direct env reads at emit time).

### **13.1 Fields (read-only after freeze; stable key order)**

Expose and persist **exactly** these fields; **no extras**:

1. `engine_tag` — opaque engine identity string pinned at build.  
2. `build_commit` — VCS short SHA for bundled repo head at cut time (**optional** on public/ops; may be unset).  
3. `invocation_tag` — canonical **short** tag for the current Invocation (public meta carries the **tag only**).  
4. `invocation_sha256` — **SHA-256** of the canonical Invocation text/bytes captured at cut (stable per cut; **evidence/admin** use; not added to public meta).  
5. `emitter_sha256` — SHA-256 over the **allow-listed presenter/emitter** source captured at cut (**evidence/admin**; not public).  
6. `release_id` — lowercase hex-64 of `sha256(canonical_bytes("catalog/manifest.json"))` computed at freeze-pack.

**Source of truth (titles-only):** `release_id` derives **only** from the PF-12 pack manifest; Invocation tag/bytes come from the Invocation registry; `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` are taken from the **build snapshot** at cut. No request-time hashing.

### **13.2 Accessors**

* **`identity_meta()` →** `{"engine_tag","invocation_tag"}` — inserted into the **public** envelope **before** idempotence hashing (**PF-01 §3.2**).  
* **`identity_admin()` →** `{"engine_tag","release_id","invocation_tag","invocation_sha256","build_commit","emitter_sha256"}` — for **internal/admin** surfaces (e.g., **/internal/version**, evidence capture).

  ### **13.3 Flow & constraints**

* **Fetch-only module.** Presenter (Reader) and CLI call this module’s helpers; **no direct env reads** at emit time; **no mutation** after freeze.  
* **Preimage coupling.** `identity_meta()` enters the **five-key preimage** (public path) **before** `idempotence_hash` is computed (PF-01 §3.2).  
* **Evidence coupling.** The same values flow into artifacts and audit evidence (titles-only); **do not duplicate** identity bytes in prose or ad-hoc files.

  ### **13.4 Prohibited**

* **No recomputation of `release_id`** during request handling.  
* **No mutation** of identity fields after freeze.  
* **No alternative sources** (env vars, flags) on public paths.  
* **No request-time hashing** for `emitter_sha256` or `invocation_sha256` — compute at **build only**.

  ### **13.5 Acceptance (binary; titles-only)**

1. **Two-run identity:** repeated emits with identical inputs yield **bitwise-identical** bytes (**one LF**).  
2. **`release_id` recompute:** equals **sha256(canonical manifest bytes)**; recompute job passes.  
3. **Reader↔CLI parity:** public bodies include `identity_meta()` and remain **byte-identical**.  
4. **Emitter/Invocation identities:** recorded `emitter_sha256` and `invocation_sha256` **match** their build-time evidence captures.

**Gating tokens:** `RELEASE_ID_RECOMPUTE_OK`, `TWO_RUN_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

### **13.6 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

**Scope (normative).** Identity artifacts are **records-only** and MUST be listed by title/path in **Appendix D: Evidence Index** and mirrored **1:1** in `artifacts/evidence_index.jsonl`. Mirror records are canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one trailing `\n`) and include: `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update the human Index and mirror **in the same commit/PR**; CI fails on mismatch or missing path-proofs. All captures run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Artifact keys (titles-only)**

* **`pack/manifest`** — canonical manifest bytes (freeze pack).  
* **`identity/release_id`** — frozen `release_id` (64-hex).  
* **`identity/release_id_recompute`** — recompute proof log (on-disk equals canonical; sha256 over canonical bytes).  
* **`identity/emitter_sha256`** — presenter/emitter source hash (proves single shared emitter).  
* **`identity/invocation_sha256`** — invocation canonical-bytes hash (admin provenance).  
* **`identity/service_identity`** — admin snapshot of identity fields (JSON; LF-terminated; numeric-free).  
* **`parity/two_run_identity`** — two-run identity digest/log (byte-equal outputs; LF-terminated).

**Mirror discipline (MUST)**

* One JSON object per line; reject unknown keys in mirror records.  
* `(artifact_key, discovered_physical_path)` in the mirror equals `(title, path)` in the human Index (strict 1:1 join).  
* A `path_proof.txt` (or equivalent) is stored alongside each artifact and referenced by `proof_anchor`.

**Routing (titles-only).**

* Pack/manifest & `release_id`: **HDE-Schemas and Artifacts §6**.  
* Invocation & preimage rules: **HDE-Math-Spec §3**.  
* Transport ops surface: **§14 Internal Meta Surface** (policy owned by **HDE-Governance**).  
  ---

## **14\) Internal Meta Surface \[Required-Now\]**

### **14.1 Purpose & scope (normative)**

Operator-only, side-effect-free endpoint exposing engine identity for diagnostics. **Single home:** `GET /internal/version`.

### **14.2 Payload (exact fields; frozen key order)**

Expose **exactly six** provenance fields — **no extras** — in this **frozen order**:

1. `engine_tag`  
2. `build_commit`  
3. `invocation_tag`  
4. `invocation_sha256`  
5. `emitter_sha256`  
6. `release_id`

**Source of truth.** Values originate from the Identity & Provenance Module (§13) and are read-only after freeze (see **HDE-Schemas & Artifacts** for release identity rules).

### **14.3 Transport (ops posture)**

* `Cache-Control: no-store`  
* **No ETag**; **Last-Modified absent**  
* `Content-Type: application/json; charset=utf-8`  
* **HEAD parity.** `HEAD /internal/version` returns **200** and mirrors 200 validators (incl. `Content-Type`); body is empty; `Content-Length == len(identity GET body)`  
* **Conditionals ignored.** `If-*` validators are ignored; this endpoint **never** serves 304  
* **Vary:** optional (MAY be present; not required for acceptance)  
   *(Policy owner: **HDE-Governance**; Mechanics reiterates here for ops wiring.)*

### **14.4 Posture**

* Operator-only; minimal payload; no secrets; no side effects.  
* Body is **canonical JSON** (UTF-8/no BOM, compact, **exactly one LF**).  
* **Key order is frozen as in §14.2** (do **not** re-sort keys for this endpoint).

### **14.5 Example (informative)**

**Request** `GET /internal/version`  
 **Response** `200 OK` `Cache-Control: no-store` `Content-Type: application/json; charset=utf-8`

{"engine\_tag":"hdengine-x.y.z","build\_commit":"\<shortsha\>","invocation\_tag":"INV-…","invocation\_sha256":"\<64hex\>","emitter\_sha256":"\<64hex\>","release\_id":"\<64hex\>"}

### **14.6 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* **Headers/behavior:** `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`  
* **Body shape:** six fields in frozen order; canonical JSON; numeric-free; exactly one LF  
* **Stability:** two consecutive GETs produce byte-identical bodies (**two-run identity proof recorded**)  
* **Index discipline:** **Evidence Index (human)** and **machine mirror** updated in the **same PR**; human↔machine **1:1 parity** enforced

### **14.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

* `intver/headers_get` — raw GET headers (proves **no-store**, **no ETag**, correct `Content-Type`)  
* `intver/headers_head` — raw HEAD headers (200; `Content-Type == GET`; `Content-Length ==` identity GET)  
* `intver/body_get` — exact LF-terminated GET body bytes \+ digest record  
* `intver/cond_if_none_match` — conditional GET (`If-None-Match` ignored → 200\)  
* `intver/cond_if_modified_since` — conditional GET (`If-Modified-Since` ignored → 200\)  
* `intver/two_run_identity` — two-run identity log (byte-equal bodies)  
* `intver/provenance_note` — operator note (`release_id`, `invocation_tag`, optional `build_commit`, capture timestamp)

Each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update the human Evidence Index in the **same change**; CI enforces **1:1 parity** and **path-proofs**.

### **14.8 Routing (titles-only)**

* **HDE-Governance §10.5** — `/internal/version` policy (no-store, no ETag, conditionals ignored, HEAD parity)  
* **HDE-Math-Spec §3** — identity/preimage rules (single home for idempotence & identity semantics)  
* **HDE-Schemas & Artifacts §6** — pack/manifest coupling for `release_id`  
  ---

## **15\) Narrative Selection Router (keys only)**

**Purpose**  
 Map viewer/context inputs to narrative keys without generating text.

**Inputs**

* `category`  
* `band`  
* `perspective` (exactly one of: `personal`, `shared`)  
* `viewer_top`  
* `flags`

**Output**

* `{ personal_key, shared_key }` — both drawn from the **Narrative Key Registry**.

**Rules**

* Deterministic; **no RNG**.  
* **Never** generates narrative text.  
* If a mapping is missing ⇒ return **`missing_narrative_key`** (no fallback).

**Routing & proofs (titles-only)**

* Authoring **DB plane** (intake, lints, preview) and runtime **file-backed pack** (sealed; no DB in hot path) live in the **Narratives Guide** / **Schemas & Artifacts**.  
* Mechanics proves **determinism** and **parity (CLI \= HTTP)**, and records **keys-only evidence** in the **same PR**.

## **16\) Narrative Key Registry and Manifests**

**Purpose**

* Versioned registry guarantees **exactly one key** per `(category, band, perspective)`.  
* Manifests are **diffable**; **no prose** is stored in the engine.  
* **Build guard:** fail the build if any mapping is **missing** or **ambiguous**.

**Pack identity (routing)**

* Identity is **manifest-driven**: `pack_sha = sha256(canonical manifest bytes)`.  
* Files are uploaded to immutable object storage at `/narratives/<pack_sha>/…`.  
* Exporter/loader procedures and coverage policy are **routed by title**; Mechanics **does not restate bytes** here.  
* CLI Tooling \[Required-Now\]

**Scope.**

* The CLI uses the shared engine and the allow-listed presenter/emitter to produce public bytes.

* All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Authoritative contract: the CLI must conform end-to-end to **PF05-Canon-HDE-CLI-API-Vendor-Ref** for commands/flags, payload shapes, error model, streams/exits, and help/version formatting (titles-only; PF05 governs).

* **Admin preview posture.** The narrative preview surface is enabled by default for admins across dev/stage/prod and uses the same emitter as Aux; bytes parity and LF discipline apply. (Bytes and route live in PF05 by title.)

  ---

  ### **16.1 Command catalog (titles-only; PF05 governs)**

**Single home for commands.**  
 The complete CLI command/flag catalog and their status live in PF05 (for example, “Commands (by status)”, “CLI Overview & Conventions”). This guide does not enumerate all commands.

**Conformance expectation.**  
 CLI help/usage, flags, and behavior must match PF05; any divergence is a defect until corrected.

**Examples (non‑exhaustive).**

* `hdctl showcompat …` — prints the **compat JSON payload** (admin/test surface) to `stdout` as canonical JSON (UTF‑8, sorted keys, compact, one LF) and, when invoked with `--dump-reader`, writes the exact Reader v1 public body (six keys) using the shared presenter/emitter. Reader↔CLI parity is defined between the Reader API and the `--dump-reader` output; CLI determinism (AB↔BA and two‑run identity) is merge‑blocking until the associated tokens are green.

* `hdctl sample …` — prints the same deterministic selection/ordering as the corresponding Reader surface documented in PF05.

* Additional commands (for example, `read singlebg`, `list people`, disabled `fetch *`) are defined and governed in PF05; this document only illustrates conformance expectations.

---

### **16.2 Streams & exits**

* **stdout (success):** public JSON body only, LF-terminated, no ANSI, no extra bytes.

* **stderr (failure):** typed JSON errors only; diagnostics without secrets/PII; success never writes to stderr.

* **Exit codes:** 0 success; 64 usage error; non-zero for other failures.

* **No mixed streams.** A run is either stdout-only success or stderr-only failure.

  ---

  ### **16.3 Determinism & parity**

* **Reader↔CLI parity.** CLI stdout is byte-identical to the Reader 200 body for mirrored surfaces (single emitter).

* **AB↔BA identity.** Pair order neutrality holds for pair-sensitive inputs.

* **Two-run identity.** Identical inputs ⇒ identical bytes (single LF).

* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact separators, one LF; arrays-as-sets deduped and ASCII-sorted (see §4/§10.1).

* **Merge-blocking status.** `showcompat` remains merge-blocking until the parity/determinism acceptance tokens in §16.7 pass.

  ---

  ### **16.4 Inputs & schemas (titles-only)**

* **IDs & catalogs.** Validate against **HDE-Schemas & Artifacts** (§2.1/§2.6).

* **Viewer prefs.** `--prefs` matches the closed 10-key weight map and `top_category ∈ Magic-10` (see **HDE-Math-Spec** §2.2/§5.x).

* **Rails.** Default SAFE rails; CLI must not open vendor rails unless explicitly configured (see §7.1/§7.3).

  ---

  ### **16.5 Installability & entrypoints**

* **Console script.** `pyproject` console-script `hdctl` present and installable.

* **Module-run.** `python -m engine.cli` parity proven with console script.

* **Packaging.** Build/install in a clean env succeeds; help/version behave as specified.

  ---

  ### **16.6 Environment pins (runtime)**

* **Pins.** `LC_ALL=C`, `LANG=C`, `TZ=UTC`; keys-only logs; no ANSI.

* **Allow-list.** CLI reads only documented env and fails-closed on unknowns (see §31.2).

  ---

  ### **16.7 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

**Entrypoints/install:**  
 `CLI_PYPROJECT_ENTRYPOINT_OK, CLI_MODULE_RUN_OK, CLI_INSTALL_OK, CLI_HELP_EXIT_0_OK, CLI_HELP_STDOUT_OK.`

**Streams/exits:**  
 `CLI_USAGE_ERR_EXIT64_OK, CLI_STDERR_ONLY_ON_ERROR_OK, CLI_STDOUT_LF_OK.`

**Parity/determinism:**  
 `CLI_READER_EMITTER_PARITY_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_AB_BA_PARITY_OK, JSON_CANONICAL_CHECK_OK, PREIMAGE_RECOMPUTE_OK, CLI_IMPLEMENTED_SET_OK.`

**Evidence discipline:**  
 `EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_PATHS_VALIDATED_OK.`

**Parity harness tokens:**  
 `CLI_INSTALL_OK, CLI_HELP_OK, CLI_SHOWCOMPAT_PRESENT, CLI_SHOWCOMPAT_CANON_OK, CLI_AB_BA_PARITY_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_READER_EMITTER_PARITY_OK.`  
 (Roster frozen in Governance.)

**Preview posture:**  
 `CLI_PREVIEW_ENABLED_OK · CLI_PREVIEW_INDEXED_OK.`

---

### **16.8 Evidence (records-only; machine mirror; same-PR rule)**

List by title/path in **Appendix D: Evidence Index** and mirror 1:1 in `artifacts/evidence_index.jsonl` (record fields as per §1.3). The machine mirror is canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF), rejects unknown keys, and each record includes a `proof_anchor` to a co-located path-proof file. Update the human Index and machine mirror in the same PR.

Required artifacts:

* `artifacts/cli/ab.json` — canonical output for AB inputs (LF-terminated)

* `artifacts/cli/ba.json` — canonical output for BA inputs (must be byte-identical to AB)

* `artifacts/cli/summary.json` — canonical JSON with attempted commands, sha256 of `ab.json` / `ba.json`, and `ab_ba_equal: true`

* `audit/gates/guards/emitter_symbol_proof.txt` — single-emitter guard (presenter symbol)

* `audit/gates/guards/serializer_grep_guard.log` — single-emitter guard (no ad-hoc serializers)

* `audit/gates/canonical/json_canonical_check.log` — canonical JSON checks

* `audit/gates/canonical/json_canon_compare.log` — canonical output comparisons

(Index human+machine in the same PR; mirror canonical JSONL; one LF; `proof_anchor` present.)

## **17 CLI Components**

### **17.1 Command catalog (titles‑only; PF05 governs)**

**Single home for commands.**  
 The complete CLI command/flag catalog and their status live in **PF05 — HDE‑CLI‑API‑Vendor‑Ref** (for example, “CLI Overview & Conventions”, “Commands (by status)”). PF14 does **not** enumerate or norm all commands; it records mechanical expectations and routes to PF05 by title.

**Conformance expectation.**  
 CLI help/usage, flags, and behavior **must** match PF05. Any divergence between `hdctl` behavior and PF05 is a defect until corrected (or PF05 is updated).

**Examples (non‑exhaustive).**

* \* \`hdctl showcompat …\` — canonical compat harness for comparing two users and driving Aux narrative preview. On success, its primary success payload is a single compat JSON document on stdout (admin/test surface), emitted via the shared presenter/emitter as canonical JSON (UTF‑8, ASCII-sorted keys, compact, one LF; no ANSI). When \`--dump-reader \<path\>\` is present, it also writes the six-key Reader v1 success envelope to \`\<path\>\` using the same emitter; those bytes must be byte-identical to the Reader 200 body for the same inputs/environment. The command remains merge-blocking until the compat JSON determinism and Reader↔CLI parity tokens are passing.  
* Additional commands (for example, `read singlebg`, `list people`, `bg:resolve`, and disabled `fetch` variants) are defined and governed in PF05, including whether they are **Required‑Now** or **Speculative**. Implement and test them according to PF05 without redefining schemas or bytes here.

---

### **17.2 Streams & exits**

* **stdout (success):** public JSON body only, LF‑terminated, no ANSI, no extra bytes.

* **stderr (failure):** typed JSON errors only; diagnostics without secrets or PII; successful runs never write to stderr.

* **Exit codes:**

  * `0` — success (canonical payload on stdout only).

  * `64` — usage error (bad flags/arguments; synopsis to stderr; stdout empty).

  * Other error codes are non‑zero and command‑specific as defined in PF05; in all cases stdout remains empty on failure.

* **No mixed streams.** A run is either **stdout‑only success** or **stderr‑only failure**; commands must not interleave diagnostics with public bytes.

---

### **17.3 Determinism & parity**

* **Reader↔CLI parity.** For each mirrored surface where the CLI emits Reader v1 bytes (stdout or via a reader-dump path, as defined in \*\*HDE-CLI-API-Vendor-Ref\*\*), those CLI bytes are byte-identical to the Reader 200 body for the same inputs/environment (single shared emitter, canonical JSON, exactly one LF). For \`hdctl showcompat\`, parity is defined between Reader HTTP and the \`--dump-reader\` sidecar file; stdout compat JSON is governed separately by determinism and canonical-JSON tokens.

* **AB↔BA identity.** For pair‑sensitive inputs, swapping the parties (A/B) yields identical outputs once normalized.

* **Two‑run identity.** Repeating the same command with identical inputs and environment yields byte‑identical stdout (single LF).

* **Canonical JSON.** All success payloads use canonical JSON: UTF‑8 (no BOM), ASCII‑sorted keys, compact separators, exactly one trailing LF. Arrays used as sets are deduped and ASCII‑sorted (see PF14 §4/§10.1).

* **Merge‑blocking status.** `hdctl showcompat` remains merge‑blocking until the parity/determinism acceptance tokens in §17.7 are passing.

---

### **17.4 Inputs & schemas (titles‑only)**

* **IDs & catalogs.** CLI commands that accept IDs or cataloged names validate them against **HDE‑Schemas & Artifacts** (§2.1/§2.6). This guide does not duplicate schema bytes.

* **Viewer prefs.** `--viewer-prefs-file` / `--prefs` flags must carry the closed 10‑key weight map with `top_category ∈ Magic‑10` and weights for all ten Magic‑10 categories (see **HDE‑Math‑Spec** §2.2/§5.x). PF05 owns the exact CLI flag shapes.

* **Rails.** CLI runs under SAFE rails by default and **must not** open vendor rails on its own. Any command that can reach vendor or external HTTP must honor the rails and override semantics defined in PF04/PF07/PF05 (§7.1/§7.3 here, and the rails sections in Governance/Infrastructure).

---

### **17.5 Installability & entrypoints**

* **Console script.** The `pyproject` console‑script entrypoint `hdctl` is present and installable.

* **Module‑run.** `python -m engine.cli` behaves identically to the console script; parity is required for help, version, and command invocation.

* **Packaging.** Building and installing the CLI in a clean environment succeeds. `hdctl --help` and `hdctl --version` behave as specified in PF05 (exit 0; output to stdout; no stderr noise).

---

### **17.6 Environment pins (runtime)**

* **Pins.** All CLI acceptance jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Logs are keys‑only, with no ANSI escapes.

* **Env allow‑list.** The CLI reads only documented environment variables and **fails closed** on unknown or malformed env that would affect behavior (see PF14 §31.2 and PF05 env/flags sections). Secrets are never echoed.

---

### **17.7 Acceptance (titles‑only; token names live in HDE‑Governance §2.0)**

**Entrypoints/install:**  
 `CLI_PYPROJECT_ENTRYPOINT_OK, CLI_MODULE_RUN_OK, CLI_INSTALL_OK, CLI_HELP_EXIT_0_OK, CLI_HELP_STDOUT_OK.`

**Streams/exits:**  
 `CLI_USAGE_ERR_EXIT64_OK, CLI_STDERR_ONLY_ON_ERROR_OK, CLI_STDOUT_LF_OK.`

**Parity/determinism:**  
 `CLI_READER_PARITY_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_TWO_RUN_IDENTITY_OK, PARITY_AB_BA_OK, JSON_CANONICAL_CHECK_OK, PREIMAGE_RECOMPUTE_OK, CLI_IMPLEMENTED_SET_OK.`

**Evidence discipline:**  
 `EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_PATHS_VALIDATED_OK.`

**Parity harness tokens (public CLI harness):**  
 `CLI_INSTALL_OK, CLI_HELP_OK, CLI_SHOWCOMPAT_PRESENT, CLI_SHOWCOMPAT_CANON_OK, CLI_AB_BA_PARITY_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_READER_EMITTER_PARITY_OK.`  
 (Parity‑harness roster is frozen in Governance/Epics; PF05 describes where these are proved.)

**Preview posture (Aux narrative preview):**  
 `CLI_PREVIEW_ENABLED_OK, CLI_PREVIEW_INDEXED_OK.`

---

### **17.8 Evidence (records‑only; machine mirror; same‑PR rule)**

Evidence listings are titles‑only here; PF12 is single home for schemas and indexing rules.

* **Indexing discipline.** List each CLI evidence artifact by title/path in **Appendix D: Evidence Index** and mirror it 1:1 in `artifacts/evidence_index.jsonl` (record fields as per PF12/§1.3). The machine mirror is canonical JSONL (UTF‑8; ASCII‑sorted keys; compact; one LF), rejects unknown keys, and each record includes a `proof_anchor` to a co‑located path‑proof file. Update the human Index and machine mirror in the same PR.

* **Required artifacts (CLI parity harness):**

  * `artifacts/cli/ab.json` — canonical output for AB inputs (LF‑terminated).

  * `artifacts/cli/ba.json` — canonical output for BA inputs (must be byte‑identical to AB).

  * `artifacts/cli/summary.json` — canonical JSON with attempted commands, sha256 of `ab.json`/`ba.json`, and `ab_ba_equal: true`.

* **Emitter and canonicalization guards:**

  * `audit/gates/guards/emitter_symbol_proof.txt` — single‑emitter guard (presenter symbol).

  * `audit/gates/guards/serializer_grep_guard.log` — grep‑guard proving there are no ad‑hoc serializers on public paths.

  * `audit/gates/canonical/json_canonical_check.log` — canonical JSON checks.

  * `audit/gates/canonical/json_canon_compare.log` — canonical output comparisons (including Reader↔CLI cases where defined in PF05).

All of the above must be indexed in both the Human Index and the machine mirror in the same PR, with canonical JSONL records and `proof_anchor` set.

---

## 

## **18\) CLI Serializer Coupling \[Required-Now\]**

**Scope.** Force all CLI public bytes through the **same allow-listed presenter/emitter** entrypoint used by Reader. Tests must not bypass the unified entrypoint.

### **18.1 Policy (normative)**

* **Single entrypoint.** CLI **MUST** route every public body through the shared presenter/emitter symbol (see §10.2).  
* **Canonical rules apply.** §4/§10.1 canonicalization (UTF-8; sorted keys; compact; one LF; arrays-as-sets) **MUST** hold for CLI stdout.  
* **Surface parity.**  
  * `/api/compat/v1`: CLI stdout is **byte-identical** to the Reader 200 body.  
  * `/api/sample/v1`: CLI stdout uses the **same deterministic selection \+ ordering** as Reader.

  ### **18.2 Prohibited (hard fail)**

* Any ad-hoc JSON on public paths: **no** `json.dumps(`, **no** `jsonify(`, **no** templating, **no** manual string building, **no** pretty/indented output.

  ### **18.3 Guards (CI)**

* **Symbol allow-list.** Maintain a code/CI allow-list of presenter/emitter symbols; only these may serialize public bytes.  
* **Grep-guard.** CI **fails** on public paths if ad-hoc serialization is detected (regex for `\bjson\.dumps\(` and known alternates).

  ### **18.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* **Coupling:** `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`.  
* **Surface parity:** `CLI_READER_EMITTER_PARITY_OK` (compat), ordering proof present (sample).  
* **Determinism:** `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

  ### **18.5 Evidence (records-only; machine mirror; same-PR rule)**

`artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`,  
 `audit/gates/guards/serializer_grep_guard.log`, `audit/gates/guards/emitter_symbol_proof.txt`,  
 `audit/gates/canonical/json_canonical_check.log`, `audit/gates/canonical/json_canon_compare.log`.

### **18.6 Routing (titles-only)**

* Canonical serializer & unified entrypoint: **§4** and **§10.2**.  
* Public payload/transport: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.  
* Domain catalogs & prefs schema: **HDE-Schemas and Artifacts** / **HDE-Math-Spec**.  
  ---

  


  ## **19\) Vendor Ingest Pipeline — source policy & proofs (normative)**

  ### **19.1 Policy (normative)**

**Policy (env-aware)**

* **Prod.** Source of truth is the database. Vendor APIs run only on explicit triggers or scheduled refresh; never inline on the request path.

* **Dev.** Direct vendor calls are allowed; on success, ingest MUST upsert the BodyGraph to DB for repeatability.

* **SAFE rails.** SAFE rails apply in all environments; rails posture and acceptance tokens are owned by HDE‑Governance (titles‑only).

**Per‑call selection (explicit)**

* Source is chosen **per call** on operator surfaces (CLI flag / ops param); there are no engine “modes.”

* Any unknown `ENGINE_*` env MUST fail fast with a typed error (no vendor I/O).

* When rails are closed, any request that sets `source=vendor` MUST return a typed refusal and MUST NOT perform outbound HTTP.

Routing and token semantics for per‑call selection are owned by HDE‑Governance and HDE‑CLI‑API‑Vendor‑Ref (titles‑only).

**Evidence (records‑only)**

* `artifacts/bodygraph/source_selection.snapshot.json` capturing at least:

  * `app_env`

  * `attempted` (requested source)

  * `selected` (actual source used)

  * `reason` (closed enum explaining selection/fallback)

  * `upserted` (boolean indicating DB upsert)

* Canonical JSON (UTF‑8, no BOM; sorted keys; compact; exactly one trailing `\n`); unknown keys are rejected.

**Source invariance (single presenter/emitter)**

For the same normalized inputs, DB‑sourced and vendor‑sourced bodies MUST be byte‑identical when emitted via the shared presenter/emitter.

Proofs live under `artifacts/bodygraph/source_invariance/` as at least:

* `ab.json` — DB body (reference side)

* `ba.json` — vendor body for the same inputs

* `summary.json` — summary (attempts, `sha256` digests, `ab_ba_equal: true` on success)

**Acceptance (titles‑only)**

* `BG_SOURCE_SELECTION_OK`

* `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`

* `BG_DEV_DIRECT_CALLS_UPSERT_OK`

* `BG_SOURCE_INVARIANCE_OK`

Index/mirror parity uses the existing index tokens:  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`.

Routing for artifact schemas and indexing lives in HDE‑Schemas & Artifacts; policy and tokens live in HDE‑Governance.

---

### **19.2 Refresh, TTL & SWR (out‑of‑band; normative)**

**Purpose.** Pin the invariants for the BodyGraph refresh worker (EPIC‑011), its policy, and the governed refresh policy snapshot. Mechanics, ADR values, and detailed schema live in the ADR, Build Notes, and HDE‑Schemas & Artifacts; this section states the mechanical invariants only.

#### **Guards (no inline vendor calls)**

A refresh worker MUST:

* Run **out‑of‑band**, off the hot Reader path; it MUST NOT perform inline vendor calls for request‑time reads.

* Respect all four guard classes:

  * **TTL**: when data becomes stale.

  * **SWR (stale‑while‑revalidate)**: when stale data may be served while a refresh runs.

  * **Rate‑limit**: how often refresh attempts may be made.

  * **Circuit‑breaker thresholds and cooldown**: behavior under sustained error conditions.

  #### **Policy snapshot (v1, titles‑only)**

The refresh policy is captured in the governed snapshot artifact:

* `artifacts/bodygraph/refresh_policy.snapshot.json`

HDE‑Schemas & Artifacts owns the path and JSON schema; PF14 references it by title only.

The snapshot uses a **v1 nested schema** pinned by ADR and tests:

* Top‑level TTL/SWR fields (for example, `ttl_s`, `swr_s`).

* Nested objects:

  * `rate_limit.{requests_per_window, window_s}`

  * `circuit_breaker.{fail_threshold, window_s, cooldown_s}`

A `sample_counts` block is attached to a copy of the policy, recording counters such as:

* `refresh_attempts`

* `refresh_successes`

* `refresh_failures`

* `breaker_tripped`

* `rate_limit_hits`

These values are enforced by governed evidence tests.

#### **Worker alignment rule (POLICY ↔ snapshot)**

The refresh worker implementation in `scripts/bodygraph/run_refresh_worker.py` MUST:

* Use a `POLICY` constant whose structure matches the v1 nested schema described above.

* Serialize that structure into `refresh_policy.snapshot.json` (plus `sample_counts`) using canonical JSON (UTF‑8, sorted keys, compact, exactly one LF).

The worker MUST NOT reintroduce the legacy flat layout (`rate_limit: 60`, `cb.{…}`) that predates the v1 schema. Any such regression would overwrite the governed snapshot with a schema that no longer matches the ADR and MUST be treated as out‑of‑policy.

Any future change to TTL/SWR, rate‑limit, or circuit‑breaker thresholds MUST:

1. Update the ADR and snapshot schema (HDE‑Mechanics, HDE‑CLI‑API‑Vendor‑Ref, HDE‑Build Notes) so they all describe the same v1‑compatible policy.

2. Update the refresh worker’s `POLICY` constant and its usages to match the updated schema and values.

Guard tests (for example `test_refresh_policy_snapshot_matches_adr`) MUST remain green; they enforce that the emitted snapshot matches the ADR‑pinned policy and that the worker reads from the same nested fields it writes.

#### **Determinism and environment**

The refresh worker runs under the same determinism pins and SAFE‑rails posture as other EPIC‑011 jobs:

* Determinism: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* SAFE rails and vendor shaping policy remain governed by HDE‑Governance and HDE‑CLI‑API‑Vendor‑Ref (titles‑only).

  ---

  ## **20\) Persistence Layer (DB posture, partition & bridge) \[Required‑Now\]**

**Scope (normative).** Database mechanics for schema identity, runtime posture, partition stance, and bridge parity. Artifact schemas and indexing live in HDE‑Schemas & Artifacts; governance tokens live in HDE‑Governance and the Build Notes. PF14 owns the mechanics that produce and prove the posture.

### **20.1 DB posture mechanics (build‑time identity)**

**Objective.** Capture the runtime DB schema, roles/grants, and boundary view posture in a deterministic way.

Mechanics MUST drive a posture harness that produces at least:

* `artifacts/db/ddl_fingerprint.json`

  * Normalized DDL snapshot of the runtime schema with stable ordering.

* `artifacts/db/grants.txt`

  * Baseline roles/grants listing.

* `artifacts/db/check_schema.txt`

  * Schema/search\_path echo and verification.

* `artifacts/db/check_constraints.txt`

  * Constraint checks (including FK, uniqueness, and any invariants called out in PF16).

* `boundary_view.readonly.proof`

  * Proof artifact (path named in HDE‑Schemas & Artifacts) that the boundary view is read‑only and does not permit writes outside the HDE schema.

Schema details for these artifacts live in HDE‑Schemas & Artifacts; PF14 requires only that the mechanics harness drive them.

All posture captures MUST:

* Run with determinism pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Produce canonical JSON/text where applicable (UTF‑8; sorted keys; compact; exactly one trailing LF).

* Remain secret‑free; logs and artifacts contain no credentials.

  ### **20.2 Partition mechanics (EPIC‑011)**

**Objective.** Enforce EPIC‑011’s non‑deferred partition stance under standard artifact paths.

The partition harness MUST produce:

* `artifacts/db/partition/partition_plan.txt`

  * Planned partition layout for HDE tables in scope.

* `artifacts/db/partition/partition_verify.log`

  * Verification output showing that the live DB matches the plan.

For EPIC‑011 there is **no** “defer partition” token: both a partition plan and verify log are required. Semantics of `PARTITION_PLAN_OK` remain defined in Governance/infra docs; PF14 owns the mechanics that generate these artifacts.

### **20.3 Bridge parity mechanics**

**Objective.** Prove parity between direct DB reads and bridge‑mediated reads and capture env connectivity posture.

Mechanics MUST:

* Drive a parity harness that emits (paths by title only):

  * `artifacts/bodygraph/vendor_upsert.<alias>.json` — vendor upsert transcript for a chosen alias.

  * `artifacts/bodygraph/db_resolve.<alias>.json` — DB resolve transcript for the same alias.

  * `artifacts/presenter/json_canon_compare.log` — canonical JSON compare proving structural equality of the two bodies.

* Ensure that, in the same change window as parity captures, an env connectivity snapshot is produced:

  * `artifacts/runtime/env_connectivity.snapshot.json` — dev‑only, names‑only snapshot showing how DB connectivity was resolved (schema in HDE‑Schemas & Artifacts).

Bridge parity and env connectivity artifacts are indexed via HDE‑Schemas & Artifacts; PF14 requires only that the mechanics jobs produce them.

**Acceptance impact.** No new tokens. This section makes explicit the mechanics expected by existing posture/partition/bridge tokens (`DB_SCHEMA_FINGERPRINT_OK`, `DB_ROLE_OK`, `PARTITION_PLAN_OK`, `DB_CONN_ENV_OK`, etc.), which remain defined in HDE‑Governance and infra docs.

---

## **21\) BodyGraph refresh worker (dev‑only; policy‑aligned) \[Required‑Now\]**

**Role.** `scripts/bodygraph/run_refresh_worker.py` is a dev‑only worker that refreshes BodyGraphs according to a governed policy. It is not wired into CI; policy and schema are governed by HDE‑Build Notes (ADR/Addenda 44–45) and HDE‑Schemas & Artifacts (snapshot schema).

### **21.1 Policy alignment (v1 schema)**

The worker uses a `POLICY` dict whose structure and values MUST match the ADR and the governed `refresh_policy.snapshot.json` v1 schema:

* `schema` — `"v1"`.

* `ttl_s` / `swr_s` — time‑to‑live and stale‑while‑revalidate windows (values as defined in ADR).

* `rate_limit` — nested object with `requests_per_window` and `window_s`.

* `circuit_breaker` — nested object with `fail_threshold`, `window_s`, `cooldown_s`.

PF14 does not restate specific numeric values; they live in HDE‑Build Notes/ADR and in the snapshot schema in HDE‑Schemas & Artifacts. The worker MUST treat `POLICY` as the single source of truth for its behavior.

### **21.2 Behavior and sample counts**

The worker:

* Uses `POLICY` to decide when to enqueue or skip refreshes (TTL/SWR), when to rate‑limit, and when to open/close the circuit breaker.

* Updates structured `sample_counts` for at least:

  * `refresh_failures`

  * `breaker_tripped`

  * `rate_limit_hits`

The exact metrics surface and aggregation are governed in infra/ops docs (PF07/PF19); PF14 records that these counts are produced and governed.

### **21.3 Schema stability and coordination**

Mechanics MUST ensure:

* Running the worker never mutates the schema of `refresh_policy.snapshot.json`; reads are allowed, but writes to the snapshot happen only via the governed snapshot path in HDE‑Schemas & Artifacts.

* Any change to the policy shape or thresholds is coordinated with:

  * HDE‑Build Notes addenda (ADR and bugfix PR‑7R), and

  * HDE‑Schemas & Artifacts snapshot schema and tests,

* so that worker `POLICY`, ADR, and `refresh_policy.snapshot.json` remain in lock‑step.

**Acceptance impact.** No new tokens. This section clarifies the behavior assumed by existing refresh‑policy evidence and tests described in HDE‑Build Notes and HDE‑Schemas & Artifacts; the worker remains dev‑only and is not an acceptance gate in CI.

---

## **22\) SAFE Rails and Provider Gate**

Refuse outbound/vendor work unless explicitly enabled. Provide open/close hooks for surfaces/providers and a posture sanity script.

* **Defaults.** Rails CLOSED for all tests and dev harness runs; vendor calls return typed refusals (numeric‑free).

* **Logging.** Keys‑only; no payloads, header values, or secrets.

* **Evidence.** Posture check log (rails closed) and at least one refusal fixture (typed, numeric‑free).

Policy, SAFE‑rails tokens, and vendor transport matrices remain single‑homed in HDE‑Governance and HDE‑CLI‑API‑Vendor‑Ref (titles‑only).

---

## **23\) Rate Limit and Backoff Component (429)**

**Closed policy (normative)**

* **Retry/backoff family:** one of `{none, fixed, exponential}` with **integer** parameters; **no jitter**.

* **Retryable conditions:** **only** `{network_error, 5xx}`; other `4xx` do **not** retry.

* **429 handling:** record typed `PROVIDER_RATE_LIMITED` (optionally `retry_after_ms` if provided); **no auto-success path in this epic** (titles-only: EPIC-012 owns the 429 success-route).

* **Envelope & logs:** typed, numeric-free error; keys-only diagnostics (no payload bodies or header values; secrets always redacted).

## **24\) Caching and Transport Wiring \[Required-Now\]**

### **24.1 Alpha posture (engine behind the app)**

* **Compat surfaces.** Return **`200 OK`** deterministic JSON only (no validators).  
* **No conditionals.** Do **not** implement **304** or **HEAD** in alpha; do **not** attach validators; skip CDN ceremony.  
* **Determinism.** Canonical JSON (UTF-8 no BOM, sorted keys, compact, exactly one LF); AB↔BA and two-run identity hold (see §10.1 / §4).

  ### **24.2 Production posture (Reader / Compat)**

**Scope (normative).** Mechanics wires and verifies runtime transport behavior for **JSON success routes** and companion surfaces. Full matrices live in **HDE-CLI-API-Vendor Ref (Appendix A)**; **A7 proofs run on a Catalog JSON success route** (not `/internal/version`).

* **200 (success).** `Content-Type: application/json; charset=utf-8`; include a **strong, quoted ETag** computed over the **LF-terminated** body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304 (conditional).** Only after a prior **200-with-body** for the same ETag; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror the cached 200; ETag present.  
* **HEAD parity.** **Status 200**; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF-terminated, pre-compression).  
* **Writers & errors.** `Cache-Control: no-store`; **no ETag**. Errors **must** include `Content-Type: application/json; charset=utf-8`.  
* **POST non-conditional.** Requests **do not** carry validators; responses **never** return 304 (ignore `If-*` conditionals).  
* **Encoding invariance.** For the same **canonical LF-terminated** body, **ETag identity** and the **effective `Content-Length`** are stable across accepted `Accept-Encoding` (identity/gzip/br). **Capture an encoding-invariance headers-only proof on a Catalog route.**

**Acceptance (titles-only; token names live in HDE-Governance §2.0).**  
 `A7_GET_QUOTED_ETAG_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`.

---

### **24.3 Proof surface & scope (titles-only routing)**

* **Success route proofs.** Run on a route listed in `docs/ENDPOINTS_CATALOG.json` (**not** `/internal/version`). Include **GET**, **HEAD parity**, **304 omission**, **writers/errors posture**, and **encoding-invariance** captures; **index human \+ machine** in the **same PR**.  
* **Ops exclusion.** `/internal/version` is operator-only and **not** A7-eligible (see §14 / HDE-Governance §10.5).  
* **Matrices & bytes.** Owned by **HDE-Governance** / **HDE-CLI-API-Vendor Ref** (titles-only). This guide enforces wiring and evidence.

  ### **24.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* **A7 success.** Governed by the **A7 token family** (200 `ETag`, HEAD parity, 304 omission, success cache/`Vary`).  
* **Writers/errors.** Governed by the **writers/error token family** (no-store, no `ETag`, error `Content-Type`).  
* **POST posture & invariance.** Governed by Governance tokens for **non-conditional POST** and **encoding/header invariance**.

  ### **24.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

* **Single home for titles/paths.** §36 **Documentation Artifacts and Registry** (“Reader success catalog & A7 proofs”).  
* **Indexing.** List titles/paths in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (canonical JSONL; one LF; each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`).  
* **Same-PR rule.** Update human Index and mirror **in the same commit/PR**; CI enforces parity and path-proofs.

  ### **24.6 Routing (titles-only)**

* **Transport matrices & header rules.** **HDE-Governance** / **HDE-CLI-API-Vendor Ref**.  
* **Evidence registry & mirror discipline.** §1.3 and §36.

---

## 25\) Gate Scripts and Evidence Harness \[Required-Now\]

### 25.1 Scope & pins (capability-level)

Dev/run scripts (or CI jobs) produce **binary acceptance** and **records-only evidence** for the Engine. Script names and locations are implementation-defined (not pinned here).

All byte checks run with:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

JSON is canonical:

* UTF-8, no BOM

* ASCII-sorted keys

* Compact (no pretty-print)

* Exactly one trailing LF

  ---

  ### 25.2 What the harness must prove

* **Determinism (math & emission)**

  * AB↔BA parity (pair neutrality)

  * Two-run identity

  * Canonical re-serialization byte-compare

  * Preimage → hash → final reproducibility

    

* **CI rails posture.** CI runs **CLOSED** by default. Any job that **opens rails** must pin retry/timeout/backoff policy and must index all governed evidence **in the same PR** (titles-only routing to Governance/Schemas & Artifacts).

* **Transport A7 (success endpoints)**

  * **Proof surface:** run on a **Catalog JSON success** route (see §9.1).

  * `/internal/version` is ops-only and **not** A7-eligible (see §9.4; HDE-Governance §10.5).

* **A7 must prove:**

  * 200 has a strong quoted ETag, success cache headers, and `Vary: Authorization, Accept-Encoding`.

  * HEAD mirrors 200 validators; no body; `Content-Type == GET`; `Content-Length ==` identity 200 body.

  * 304 is served only after 200; no body; omit `Content-Type` and omit `Content-Length`; validators mirror cached 200\.

  * POST is non-conditional (never 304).

  * Writers/errors: `Cache-Control: no-store`; no ETag; errors include `Content-Type: application/json; charset=utf-8`.

  * Encoding invariance: for the same canonical body, ETag identity and effective `Content-Length` are stable across accepted encodings (identity/gzip/br); capture a headers-only proof.

  * Env-gating: capture a headers-only env-gate proof demonstrating non-prod entries are unreachable in prod.

* **Band edges**

  * Inclusive-high thresholds

  * Snapshot edges and diffs for each preset (see §5.3)

* **Reader↔CLI parity**

  * Shared emitter

  * CLI stdout equals Reader 200 body for mirrored surfaces

* **Serializer path guards**

  * Grep-guard denies ad-hoc serializers

  * Symbol proof shows Reader/CLI resolve to the same presenter/emitter

* **Narratives & architecture (keys-only)**

  * Deterministic 10×2 key table `{id, band, personal_key, shared_key}`

  * Architecture snapshot (LF-validated, no secrets)

* **Aux evidence scope (EPIC-010)**

  * Capture exactly **two** headers-only snapshots:

    * `tests/transport/headers/aux_text_200.snap`

    * `tests/transport/headers/aux_suppression_200.snap`

  * Aux HEAD/304 captures are **out of scope**

  * A7 proofs remain **Catalog JSON-success only**

  * (Bytes/policy routed by title to PF05/PF04)

  ---

  ### 25.3 Orchestration & ordering

The harness can be invoked standalone or as part of the sanity pipeline (see §26.5).

**Minimum ordering:**

1. Format

2. Lint/type

3. Unit/property tests

4. Schema checks

5. Goldens

6. Capture artifacts

7. Index \+ mirror parity check

8. Fail-closed on drift

   ---

   ### 25.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **Determinism**

  * Governed by the determinism token family (AB↔BA, two-run, canonical compare)

* **Transport A7**

  * Governed by A7 tokens

  * Writers/errors posture governed by writers/error tokens

  * Encoding-invariance and Vary tokens required

  * Catalog posture (internal-only, env-gated) tokens required

* **Bands**

  * Governed by bands/edges tokens

* **CLI parity & serializer guards**

  * Governed by CLI/Emitter parity and no-alt-JSON tokens

* **Evidence discipline**

  * Governed by Index/Mirror tokens (human↔machine 1:1; canonical JSONL; path-proofs)

* **Aux/Narrative (EPIC-010)**

  * `NARR_200_TEXT_OK`

  * `NARR_SUPPRESSED_NO_ETAG_OK`

  * `NARR_VARY_AUTH_AE_OK`

  * `AUX_CANON_ALIAS_PARITY_OK`

  ---

  ### 25.5 Evidence & indexing (records-only; machine mirror; same-PR rule)

* **Single home for titles/paths**

  * §36 Documentation Artifacts and Registry

  * This guide does **not** pin file paths here

* **Indexing**

  * List artifact titles/paths in **Appendix D: Evidence Index**

  * Mirror 1:1 in `artifacts/evidence_index.jsonl` (canonical JSONL; exactly one LF)

* **Mirror record fields**

  * `artifact_key`

  * `sha256`

  * `size_bytes`

  * `produced_at_utc`

  * `discovered_physical_path`

  * `proof_anchor`

* **Parity gate**

  * Update human Index and mirror in the **same commit/PR**

  * CI fails on:

    * Mismatch

    * Non-canonical JSONL

    * Unknown keys

    * Missing path-proofs

* **Required titles to appear in Index \+ mirror** (examples, titles-only)

  * Endpoint Catalog snapshot

  * Env-gate proof

  * A7 headers (GET/HEAD/304/writers+errors)

  * Encoding-invariance proof

  * Reader↔CLI parity and canonical-compare artifacts

  * Band-edge snapshots

  * Serializer grep-guard and emitter-symbol proofs

  * `/internal/version` headers/body/two-run captures

* **Mirror field order note**

  * Mirror field order & CI tokens are pinned once in §1.3; this section routes by title only to PF12/PF10 for the exact order and gates.

  ---

  ### 25.6 Routing (titles-only)

* **Transport matrices & A7 policy**

  * HDE-CLI-API-Vendor-Ref

  * HDE-Governance

* **Domains & catalogs / canonical JSON rules**

  * HDE-Schemas & Artifacts

* **Math semantics (preimage, bands, comparators)**

  * HDE-Math-Spec

* **Ops endpoint posture**

  * HDE-Governance §10.5 (see §9.4 for PF14 ops block)

  ---

## **26\) Performance and Load Harness**

Load tests for Reader, Compat, and Narrative Selection Router (keys-only). Microbenchmarks: `compat()` core computation \+ narrative key lookups.  
 **Outputs:** non-PII bench reports (bounded histograms \+ percentiles), thresholds, and regression flags.  
 **Routing:** SLO targets and failure posture live in Governance (titles only).

## **27\) Release and Provenance Packaging**

**Purpose (normative).** Freeze the engine pack and prove that  
 `release_id = sha256(canonical_bytes("catalog/manifest.json"))`. Mechanics owns the **jobs and evidence**; manifest shape and canonical rules live in **HDE-Schemas and Artifacts** (titles only).

### **27.1 Manifest integrity checks**

* **Canonical bytes.** The on-disk `catalog/manifest.json` **equals** its canonical serialization (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing `\n`).  
* **`files[]` order.** Entries are **ASCII-ascending by `path`**; **no duplicates** by `path`.  
* **No self-listing.** `catalog/manifest.json` **MUST NOT** appear in `files[]`.  
* **Path constraints.** Each `path` is **relative to `root:"catalog/"`** (no `catalog/` prefix), POSIX, no `..` or `//`, length ≤ 256 bytes.  
* **Entry identity.** For every `{path, sha256, size}`: `sha256` is **lowercase 64-hex of the artifact’s canonical bytes** and `size` matches those canonical bytes.  
* **Pins.** All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **27.2 Recompute `release_id`**

1. Read `catalog/manifest.json` in **binary**.  
2. Re-serialize to **canonical bytes** (see **HDE-Schemas and Artifacts §4**).  
3. **Verify** on-disk bytes **equal** canonical bytes (fail closed if not).  
4. Compute SHA-256 over canonical bytes → 64-hex **lowercase**; record as `release_id`.

### **27.3 Evidence & mirror (records-only; same-PR rule)**

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF). Update human Index and mirror **in the same commit/PR**; CI fails on mismatch or missing path-proofs.

* `artifacts/math/freeze_pack_manifest.json` — evidence copy of `catalog/manifest.json`  
* `artifacts/math/release_id.txt` — recorded `release_id`  
* `artifacts/math/release_id_recompute.log` — recompute trace  
* `artifacts/math/checksums_audit.log` — per-entry verification (path/sha256/size)

* `artifacts/bodygraph/release_bindings.json` — `{release_id, data_source_policy, ttl_s, swr_s, snapshot_counts{fresh,swr,refresh_queued}}` (canonical JSON; one LF). *(Human+machine indices updated in the same PR.)*

### **27.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* `RELEASE_ID_RECOMPUTE_OK`  
* `MANIFEST_SHA256_HEX64_OK`  
* `PACK_MANIFEST_NO_SELF_LISTING_OK`  
* `MANIFEST_PATH_ASCII_SORT_OK`, `MANIFEST_NO_DUP_PATHS_OK`  
* `PACK_ROOT_PINNED_OK` *(if `root` present)*  
* `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`

**Routing (titles-only).** Manifest shape, canonical JSON rules, and mirror schema: **HDE-Schemas and Artifacts**. Public transport remains in **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.

Great question. The **sanity pipeline** is part of your release/provenance work, so the cleanest place is **inside §26 “Release and Provenance Packaging,” as a new numbered subsection right after 27.4**. That keeps all pack identity chores and the end-of-release checks together, and it complements the high-level pipeline note already in §1.3.

Here’s a paste-ready addition:

---

### **27.5 Sanity pipeline (release & provenance) \[Required-Now\]**

**Purpose (normative).** Provide a single, scriptable pipeline that verifies the release **end-to-end** and **fails closed** on any drift. It finishes by updating the human index and the machine mirror with **1:1 parity** and **path-proofs**.

**Ordered steps (minimal sequence)**

1. **Format** (code/docs)  
2. **Lint / type** checks  
3. **Unit \+ property tests** (determinism, comparators)  
4. **Schema validation** (domains, payloads as applicable)  
5. **Goldens** (AB↔BA, two-run, bands edges, canonical compare)  
6. **Capture artifacts** (this release):  
   * Pack identity: manifest evidence copy, `release_id` recompute, checksums audit (see 26.3)  
   * Transport proofs (A7) on a cataloged success route (see §9.1/§27.2)  
   * Internal-ops `/internal/version` snapshots (see §27.4/§14)  
   * DB posture artifacts (see §20/§27.5)  
7. **Index \+ mirror parity check**: update **Appendix D: Evidence Index** and write mirror records to `artifacts/evidence_index.jsonl` (**same commit/PR**), then verify:  
   * 1:1 join (title/path ↔ artifact\_key/discovered\_physical\_path)  
   * Canonical JSONL (UTF-8, sorted keys, compact, one LF)  
   * **Path-proofs** present and referenced by `proof_anchor`  
8. **Fail closed on drift** (non-canonical bytes, parity mismatch, missing path-proofs, changed digests, or schema violations)

**Evidence (records-only; machine mirror; same-PR rule)**

* `artifacts/proofs/sanity_pipeline.transcript.log` — pipeline transcript (ordered steps \+ pass/fail summary)  
* Existing artifacts produced in step 6 (see 26.3, §27, §20, §36) must also be indexed and mirrored **in this run**

**Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`  
* `JSON_CANONICAL_CHECK_OK` (mirror records and any JSON artifacts)  
* `RELEASE_ID_RECOMPUTE_OK` (pack identity verified)  
* Plus applicable transport/ops/DB tokens referenced by §9/§14/§20/§27

**Routing (titles-only).** Evidence and mirror schema: **HDE-Schemas and Artifacts**. Transport matrices and `/internal/version` policy: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**. Domain/pack rules: **HDE-Schemas and Artifacts**.

---

## **28\) Post-deploy Smoke**

**Purpose (normative).** Run a minimal, production-against-production verification immediately after deploy. Prove transport correctness on a **cataloged success route**, confirm **writers/errors** posture, verify **internal ops** surface, and spot-check **DB posture**. Mechanics captures artifacts and indexes them in the Evidence Index and machine mirror **in the same commit/PR**.

### **28.1 Scope & pins**

* **Environment pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Routing.** Transport matrices live in **HDE-CLI-API-Vendor Ref**; `/internal/version` policy in **HDE-Governance §10.5**; DB mechanics in **§20**.

### **28.2 Success route (A7) — transport smoke**

* **Surface.** Use a route listed in the **Endpoint Catalog (JSON success)** (see §9.1).  
* **Prove (headers-only):**  
  * **200:** strong **quoted `ETag`**, `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`.  
  * **HEAD parity:** no body; validators mirror 200; **`Content-Type == GET`**; **`Content-Length == identity 200 body`**.  
  * **304:** served **only after** a prior 200; **no body; omit `Content-Type` and `Content-Length`**; validators mirror cached 200\.

### **28.3 Writers & errors — posture smoke**

* **Writers/errors:** `Cache-Control: no-store`; **no `ETag`**.  
* **Errors:** `Content-Type: application/json; charset=utf-8`; typed, numeric-free error bodies (see Vendor Ref error model).

### **28.4 Internal ops `/internal/version` — ops-only smoke**

* **GET 200:** JSON UTF-8; `Cache-Control: no-store`; **no `ETag`**; `Last-Modified` absent; `Vary` optional.  
* **HEAD 200:** mirrors GET validators; **no body**; **`Content-Length == identity GET body`**; **`Content-Type == GET`**.  
* **Conditionals:** `If-None-Match` / `If-Modified-Since` **ignored**; **never 304**.  
* **A7:** **not** a success route; **exclude** from A7 proofs.

### **28.5 Database posture — live checks**

* **search\_path:** prove `hde, public` (unquoted, in that order).  
* **Roles/grants:** least-privilege at runtime (snapshot grants/constraints).  
* **Schema identity:** normalized DDL fingerprint captured (see §20.1).  
* **(Optional) RW smoke:** insert→delete round-trip against a scratch table (job-profile gated).

### **28.6 Evidence (records-only; machine mirror; same-PR rule)**

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record: `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF).

**Success route (A7) proofs**

* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`

**Internal ops**

* `artifacts/ops/internal_version/headers_get.txt`  
* `artifacts/ops/internal_version/headers_head.txt`  
* `artifacts/ops/internal_version/cond_if_none_match_headers.txt`  
* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`  
* `artifacts/ops/internal_version/body_get.json` \+ `artifacts/ops/internal_version/body_get.sha256`  
* `artifacts/ops/internal_version/provenance_note.md`

**DB posture**

* `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`, `artifacts/db/check_constraints.txt`  
* `artifacts/db/partition_plan.txt` *(if used)*  
* `artifacts/db/db_rw_smoke.log` *(optional)*

**Pins & harness**

* `artifacts/proofs/env_pins.txt`

  ### **28.7 Acceptance (titles-only; tokens live in HDE-Governance §2.0)**

* **Success route (A7).** Governed by the **A7 token family** in Governance (200 `ETag`, HEAD parity, 304 omission, success cache/`Vary`).  
* **Writers/errors.** Governed by the **writers/error token family** (no-store, no `ETag`, error `Content-Type`).  
* **Internal ops (`/internal/version`).** Governed by the **INTVER token family** (ops-only posture, HEAD parity, conditionals ignored).  
* **DB posture.** Governed by *DB\_ tokens*\* (connection/env, search\_path, roles, schema fingerprint; optional RW smoke if run).  
* **Evidence discipline.** Governed by **Index/Mirror tokens** (human↔machine 1:1; canonical JSONL; path-proofs).

This guide asserts capability-level conformance and **routes all token names to HDE-Governance §2.0**. Artifacts are captured per **§27.6** and indexed per **§1.3/§36**.

---

## **29\) Server Cache (Production) — rolled in**

**Purpose.** Optional, private, composite-key cache for **Reader** and **Compat** that preserves A7 transport rules and deterministic invalidation.

### **Key**

* **Composite key fields.** `{ viewer_id | person_id(s) }`, `design_fingerprint`, `thresholds_identity`, `release_id`.  
* **Pair normalization.** Normalize `{a,b}` to a stable order (**AB↔BA**) before keying.  
* **Viewer scope.** Include `viewer_id` **only** when output depends on viewer preferences.  
* **Determinism.** Key construction is pure and reproducible; no clock, no randomness.

  ### **Transport (A7-consistent)**

* **200 (success).** `Content-Type: application/json; charset=utf-8`; **strong, quoted ETag** over the **LF-terminated** body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304 (conditional).** Only after a prior **200-with-body** for the same ETag; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror the cached 200; ETag present.  
* **HEAD parity.** **Status 200**; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF, pre-compression).  
* **Writers & errors.** `Cache-Control: no-store`; **no ETag**; writers bypass cache.  
* **Encoding invariance.** For the same canonical body, **ETag identity** and **effective `Content-Length`** are stable across accepted `Accept-Encoding` (identity/gzip/br).  
* **Ops exception.** `/internal/version` is operator-only and **never cached**.

  ### **Invalidation (deterministic)**

* **Triggers.** Any change to **`release_id`**, **`thresholds_identity`**, **input payloads** (incl. `viewer_prefs`), or **`design_fingerprint`**.  
* **Effect.** Invalidation is **immediate**; **no stale bytes** are served after an invalidation event.

  ### **Controls**

* **Default OFF.** Enable via a runtime flag.  
* **Metrics.** Emit counters for **hits**, **misses**, **invalidations**.  
* **Diagnostics (optional).** A keyed, redaction-safe debug log of cache decisions for local analysis (titles-only in indices).

  ### **Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* **A7 transport preserved:** `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`.  
* **Correctness:** deterministic composite keys; **no stale bytes** after invalidation.  
* **Performance posture:** hit-ratio and latency guardrails met under load (titles-only; perf jobs live outside this guide).

*Proof surface reminder:* A7 proofs run on a **Catalog JSON success** route (see §9.1); caching must **not** change transport bytes or success/conditional behavior.

---

## **30\) Observability (Logs and Metrics)**

**Logging (keys-only)**

* Structured, **keys-only** logs with correlation IDs (non-PII, bounded).  
* Surfaces: Reader, Compat, cache layer, rate-limit decisions.  
* **Guards:** grep-guards prevent payload/secret logging; only allow-listed labels.

**Metrics**

* **Counters/Histograms:** request counts, latencies, cache hits/misses, rate-limit outcomes.  
* **Dashboards:** quick views for transport health, cache efficacy, and error rates.

**BodyGraph ingest signals**

* **Counters:** refresh successes/failures; rate-limit throttles; circuit-breaker trips.  
* **Histograms:** vendor latency.  
* **Gauges:** staleness percentage.  
* **Evidence:** `artifacts/bodygraph/metrics.snapshot.json` (keys-only, canonical JSON, single LF).

## **31\) Security Posture**

**Controls**

* Per-route rate limits  
* CSRF: rotate token and retry once on browser writers  
* Strict input validation  
* Writers: `Cache-Control: no-store`; typed errors; no `ETag`  
* Never log secrets or PII

**Packaging & Runtime**

* Dockerfile and process launch scripts  
* Health and readiness probes  
* Externalize only secrets/coordinates via environment variables  
* Generate typed config at build time

**Identity**

* `/internal/version` is operator-only; `Cache-Control: no-store`; no `ETag`  
* Provenance: `build_commit` is optional in production and may be unset/null

**Logs (ingest)**

* Keys-only logs; no raw birth data; no vendor payloads; secrets never logged  
* Provide a sanitized sample: `artifacts/bodygraph/keys_only.logs.sample`

## **32\) Packaging and Runtime \[Required-Now\]**

**Scope.** Container packaging and runtime posture for the HD Engine. Mechanics owns image/process hardening, config plumbing, health/ready behavior, and operational guardrails. Public bytes, schemas, and transport matrices are referenced by title only. All byte-sensitive checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### **32.1 Image & process posture**

* **Deterministic build.** Reproducible container image; pin base; lock package indexes; emit SBOM.  
* **Least privilege.** Run as non-root; drop Linux capabilities; prefer read-only root FS with writable tmp/cache only if required.  
* **Single binary & emitter.** Wire the **allow-listed presenter/emitter** (see §4, §10.2); forbid ad hoc serialization in entrypoints.  
* **Locale pins.** Export `LC_ALL=C`, `LANG=C`, `TZ=UTC` for all emit/compare paths to preserve byte identity.  
* **Resource limits.** Set CPU/memory limits and graceful shutdown (SIGTERM → drain → exit 0).

### **32.1A Start command & service factory \[Required-Now\]**

**Purpose (normative).** Capture the exact production start command and prove the app factory binds to **`$PORT`**.

* **Start-command capture (records-only).** Capture the exact launch command line used in production (no secrets). Store as canonical text (UTF-8; exactly one trailing `\n`). *(Evidence path listed in §36.)*  
* **Factory binding to `$PORT`.** Prove the service initializes via the factory `adapter.factory:create_app()` (titles only) and binds to **`$PORT`** from the environment (no hard-coded port).  
* **Runtime pins (minimal).** Record `PORT`, `APP_ENV`, and identity pins required for traceability as a keys-only text snapshot (UTF-8; one `\n`). *(Evidence path listed in §36.)*

### **32.2 Configuration & environment**

* **Typed config at build.** Generate a typed runtime config artifact at build (defaults, switches, A7 posture) and vendor it into the image.  
* **Env allow-list (secrets/coordinates only).** Only read whitelisted keys at startup: `SAFE_MODE`, `ALLOW_NETWORK`, `HDAPI_BASE_URL`, `HD_API_KEY` (secret), `GEO_API_KEY` (secret), `PORT`, and explicitly documented toggles.  
* **Fail-closed on unknowns.** Unknown env keys or malformed values fail fast; do not partially boot.  
* **Rails posture.** Rails defaults derive from the **Env Deployment Inventory** (titles-only): **dev & stage OPEN**, **prod CLOSED**, **CI CLOSED**. In CI, any job that opens rails must pin policy and index governed evidence **in the same PR**. Determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`) apply in **all** environments that produce governed bytes.

### **32.3 Health/ready & lifecycle**

* **HTTP probes.**  
   `/healthz`: liveness (process up, core initialized).  
   `/readyz`: readiness (emitter wired, pack loaded, manifest hashed, rails posture read).  
* **Probe bytes.** Minimal, numeric-free JSON; canonicalized (UTF-8/no BOM, sorted keys, compact, one LF).  
* **Graceful shutdown.** Stop accepting traffic on TERM; complete in-flight; emit final health with `status:"stopping"`; exit cleanly.

### **32.4 Security & observability**

* **Keys-only logs.** No payload or header values in logs; secrets always REDACTED; bounded labels (route, outcome, rails\_state, timeout\_profile, attempt\_idx).  
* **Metrics (bounded).** Counters/timers/histograms for engine/presenter latency and transport outcomes; no PII.  
* **Tracing.** Optional `correlation_id` (non-PII) with bounded cardinality.

### **32.5 Transport & identity (titles-only)**

* **Reader A7 (public).** See **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (ETag over LF-terminated body; `Vary` policy; 304 omits `Content-Type` and `Content-Length`; HEAD parity; POST non-conditional).  
* **Internal ops `/internal/version`.** Operator-only; `Cache-Control: no-store`; **no `ETag`**; HEAD parity; conditionals ignored; body includes `engine_tag`, `release_id`, `invocation_tag`, `emitter_sha256`, optional `build_commit` (see §14).  
* **Identity.** `release_id` from canonical manifest (**HDE-Schemas and Artifacts §6**); `invocation_tag` participates in preimage (**HDE-Math-Spec §3**); presenter uses canonical serializer (§4).

### **32.6 Acceptance (binary)**

* **Image & user.** SBOM produced; runs as non-root; read-only FS validated at runtime.  
* **Config discipline.** Only allow-listed env consumed; unknowns fail; typed config present; SAFE rails ON by default.  
* **Health/ready.** Probes return canonical JSON; liveness/readiness reflect emitter/pack state; graceful shutdown proven.  
* **Ops posture.** `/internal/version` headers/body match §14; **no-store**, **no `ETag`**, conditionals **ignored**, one LF; HEAD 200 parity.  
* **Start command & factory.** Start command captured; factory proven; **binds `$PORT`**.  
* **Determinism.** `LC_ALL=C`, `LANG=C`, `TZ=UTC` enforced; canonical re-serialization byte-compare passes for all public/ops surfaces emitted from this process.

**Acceptance tokens (titles-only; token names live in HDE-Governance §2.0)**  
 `SERVICE_START_CMD_CAPTURED_OK`, `GUNICORN_APP_FACTORY_OK`, `ENV_PORT_REQUIRED_OK`,  
 `DB_CONN_ENV_OK` *(if DB env validated here)*,  
 plus any applicable transport/ops tokens referenced by §14 and §9.

### **32.7 Evidence (titles/paths only)**

**Single home for artifact titles/paths.** Do **not** pin file paths here. The authoritative registry of artifacts and their titles/paths lives in **§36 Documentation Artifacts and Registry**. Mechanics **MUST**:

* List artifacts by **title/path** in **Appendix D: Evidence Index** (human).  
* Write **records-only** mirror entries to `artifacts/evidence_index.jsonl` in the **same commit/PR** (machine).  
* Ensure each mirror record is canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one LF) and includes:  
   `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`.  
* Maintain strict **1:1 parity** between human Index and machine mirror; CI fails on mismatch or missing **path-proofs**.

**Routing (titles-only).** A7 and ops policies: **HDE-Governance**. Public bytes & preimage: **HDE-CLI-API-Vendor Ref** / **HDE-Math-Spec**. Pack/manifest: **HDE-Schemas and Artifacts**. Evidence registry/mirror discipline: **§1.3** and **§36**.

---

## **33\) SDKs (Client Libraries) — rolled in**

Client libraries use the allow-listed presenter-emitter and enforce transport rules.

**TypeScript SDK (required)**

* `readPerson(id | payload)` — calls Reader; returns the exact public body bytes (LF-terminated). `await .json()` is available as a convenience parser.  
* `compat(a, b, prefs)` — calls `/api/compat/v1` with `POST` and `Content-Type: application/json`; returns the exact body bytes; `await .json()` available.  
* `sample(viewer_prefs, seed?)` — calls `/api/sample/v1` with `POST`; returns the exact body bytes; ordering matches service; `await .json()` available.

**conditionalGetHelper (Reader; production)**

* Implements conditional GET with `If-None-Match`.  
* On `200`: returns `{status:200, etag, body_bytes}`, updates cache.  
* On `304`: returns `{status:304, etag, body_bytes}` using cached bytes; server `304` has no body, omits `Content-Type`, and has `Content-Length 0` or absent.  
* Helpers surface the strong, quoted `ETag` for callers.

**Python SDK (ops/automation)**

* Mirrors `readPerson`, `compat`, `sample`; returns body bytes with optional `.json()` convenience.  
* Includes byte/order parity tests against the service.

**Policy**

* All SDK calls **MUST** preserve canonical JSON bytes (UTF-8, sorted keys, compact separators, exactly one trailing LF).  
* Application teams **SHOULD** use the SDK to guarantee byte/order parity with the single emitter and correct A7 transport behavior.

**Acceptance**

* TypeScript `compat()` and `sample()` bytes are bitwise-equal to service `200` bodies; `sample()` ordering matches.  
* `conditionalGetHelper` sends `If-None-Match` and handles `304` semantics exactly (no body, omit `Content-Type`, `Content-Length 0/absent`).  
* Python SDK parity tests pass for bytes and ordering across all three calls.

## **34\) Dev HTTP Harness (single home)**

Dev-only; bound to `127.0.0.1`; not public; CORS disabled; `APP_ENV=dev`; debug reloader **off** during captures. Emits canonical JSON via the allow-listed presenter-emitter (§4/§8).

**Routes**

* `GET|POST /api/reader` (person)  
* `GET|POST /api/compat/v1` (pair; ids-only `GET`)  
* `POST /api/sample/v1`

**Method posture**

* `GET` **MUST NOT** include a body.  
* `POST` is **non-conditional** (no validators; never returns `304`).

**Dev error posture (Reader & Compat)**

* `Content-Type: application/json; charset=utf-8`  
* `Cache-Control: no-store`  
* **No `ETag`**

**Runner**

* Start locally with the canonical runner:  
   `python -m adapter.http_reader --bind 127.0.0.1:5000`

**Quick start (curl)**

export APP\_ENV=dev

\# Pair (POST)

curl \-s http://127.0.0.1:5000/api/compat/v1 \-H 'Content-Type: application/json' \\

  \-X POST \-d '{"a":{…},"b":{…},"viewer\_prefs":{…}}' | jq .

\# Reader (POST body form)

curl \-s http://127.0.0.1:5000/api/reader \-H 'Content-Type: application/json' \\

  \-X POST \-d '{"id":"…"}' | jq .

\# Sample with seed (POST)

curl \-s http://127.0.0.1:5000/api/sample/v1 \-H 'Content-Type: application/json' \\

  \-X POST \-d '{"viewer\_prefs":{…},"seed":12345}' | jq .

## **35\) Runbooks (Operations)**

Runbooks for elevated 5xx, slow Reader/Compat, stuck queue, DB lag. Fast rollback \+ data safety notes.  
 **Pointers:** rollback uses pointer-flip to last known-good `release_id` (titles only).

## **36\) Dashboards and Alerts**

Dashboards for Reader, Compat, Narrative Router, and Server Cache latencies, error rates, hit/miss, and rate-limits. Actionable alerts for error spikes and budget breaches.  
 **Notes:** include A7 headers health and cache hit ratio panels.

---

## 37\) Documentation Artifacts and Registry \[Required-Now\]

### Purpose

Registry for small, deterministic documentation artifacts and gate evidence. Titles-only cross-refs; bytes live in files. Mechanics keeps the human index and the machine mirror in lockstep (same-PR rule).

### Governance note

Governed paths only; transient generator paths (for example, `codex/out/**`) are not authoritative and **MUST NOT** be indexed.

### Homes

* `/artifacts` — public documentation snapshots and pack/identity evidence.

* `/audit/gates` — gate evidence produced by §24 scripts (bands / canonical / props / etc.).

* Human Index (single home): `docs/evidence/INDEX.json` (titles/paths only; no bytes).

* Machine Mirror (single home): `artifacts/evidence_index.jsonl` (records-only JSONL; one LF).

### Conventions

* Deterministic filenames (lowercase, stable tokens).

* Extensions: `.json`, `.log`, `.txt`, `.bytes`.

* Text artifacts end with exactly one trailing LF (`\n`).

* JSON is canonical (UTF-8, no BOM, ASCII-sorted keys, compact, one LF).

* `.bytes` files mirror the exact body bytes (including the body’s own trailing LF, if present).

* Header snapshots follow §4.3 normalization (lower-cased keys, compact, one LF).

### Mirror (records-only)

Every artifact listed here must have a 1:1 record in `artifacts/evidence_index.jsonl` (canonical JSONL; one LF) with:

* `artifact_key`

* `role`

* `sha256`

* `size_bytes`

* `produced_at_utc`

* `discovered_physical_path`

* `proof_anchor` (path-proof transcript)

Unknown keys are rejected. Update the Human Index and the machine mirror in the same commit/PR.

**Exact field order (normative).** Mirror records use:

* `artifact_key`

* `discovered_physical_path`

* `produced_at_utc`

* `proof_anchor`

* `role`

* `sha256`

* `size_bytes`

with:

* sort-before-write

* unknown-key reject

* one LF per record

**Acceptance:** `MACHINE_MIRROR_UPDATED_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK` (plus index parity tokens already listed).

### Required captures (titles/paths only)

#### Reader success catalog & A7 proofs

* Catalog: `docs/ENDPOINTS_CATALOG.json` (+ `docs/ENDPOINTS_CATALOG.json.sha256`)

* Env-gate proof: `artifacts/proofs/endpoints_env_gate_proof.log` (proves non-prod entries are unreachable in prod)

* Success GET proof: `artifacts/proofs/success_get.txt`

* Success HEAD parity proof: `artifacts/proofs/success_head.txt`

* Success 304 omission proof: `artifacts/proofs/success_304.txt` (omits Content-Type and Content-Length)

* Writers/Errors posture proof: `artifacts/proofs/success_writers_errors.txt`

* (Optional) Encoding-invariance proof: `artifacts/proofs/encoding_invariance.txt`

#### Serializer / Emitter guards

* Grep guard (no ad-hoc serializers on public paths): `audit/gates/guards/serializer_grep_guard.log`

* Shared presenter/emitter symbol proof: `audit/gates/guards/emitter_symbol_proof.txt`

#### CLI parity & determinism (public bytes)

* AB ↔ BA goldens:

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json`  
     (LF-terminated, canonical JSON; BA must be byte-identical to AB)

* Parity summary: `artifacts/cli/summary.json` (attempted commands, sha256 of AB/BA, `ab_ba_equal: true`)

* Two-run marker: `artifacts/cards/A3/IDENTITY_OK.txt`

* Canonical compare: `audit/gates/canonical/json_canon_compare.log`

#### CLI Admin Preview (narrative)

* `artifacts/cli/narrative/stdout.txt` — LF-terminated text (no ANSI)

* `artifacts/cli/narrative/sidecar.json` — ids-only canonical JSON (no prose)

Index both in the human index and the machine mirror in the same PR.

#### Canonical JSON checks

* Policy check: `audit/gates/canonical/json_canonical_check.log`

* Canonical re-serialization compare: `audit/gates/canonical/json_canon_compare.log`

#### Bands edges (inclusive-high)

* Edges snapshot: `audit/gates/bands/edges.snapshot.json`

* Edges diff: `audit/gates/bands/edges.diff.json`

#### Pack identity & provenance

* Evidence copy of manifest: `artifacts/math/freeze_pack_manifest.json`

* Recomputed `release_id`: `artifacts/math/release_id.txt`

* Recompute log: `artifacts/math/release_id_recompute.log`

* Checksums audit: `artifacts/math/checksums_audit.log`

* (Optional) SBOM (CycloneDX) \+ hash:

  * `sbom/cyclonedx.json`

  * `sbom/cyclonedx.json.sha256`

#### Identity & Math

* Service identity (admin JSON): `artifacts/identity/service_identity.json`

* Emitter SHA-256: `artifacts/identity/emitter_sha256.txt`

#### Internal-ops `/internal/version` snapshots

* GET headers: `artifacts/ops/internal_version/headers_get.txt`

* HEAD headers: `artifacts/ops/internal_version/headers_head.txt`

* Cond: If-None-Match: `artifacts/ops/internal_version/cond_if_none_match_headers.txt`

* Cond: If-Modified-Since: `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

* Body (JSON): `artifacts/ops/internal_version/body_get.json`

* Body SHA-256: `artifacts/ops/internal_version/body_get.sha256`

* Provenance note: `artifacts/ops/internal_version/provenance_note.md`

#### Database proofs & ops pins

* DDL snapshot: `artifacts/db/ddl_fingerprint.json`

* Grants/constraints checks:

  * `artifacts/db/grants.txt`

  * `artifacts/db/check_constraints.txt`

* Schema check: `artifacts/db/check_schema.txt`

* Partition plan: `artifacts/db/partition_plan.txt`

* Start command capture: `artifacts/proofs/start_command_capture.txt`

* Environment pins: `artifacts/proofs/env_pins.txt`

#### BodyGraph proofs

* Source selection snapshot: `artifacts/bodygraph/source_selection.snapshot.json`

* Source invariance:

  * `artifacts/bodygraph/source_invariance/ab.json`

  * `artifacts/bodygraph/source_invariance/ba.json`

  * `artifacts/bodygraph/source_invariance/summary.json`

* Refresh policy: `artifacts/bodygraph/refresh_policy.snapshot.json`

* Metrics: `artifacts/bodygraph/metrics.snapshot.json`

* Sanitized logs sample: `artifacts/bodygraph/keys_only.logs.sample`

* Release bindings: `artifacts/bodygraph/release_bindings.json`

#### Narratives 

* Narratives coverage (router):  
   `audit/gates/narratives/keys_10x4.table.json` (10 categories × 4 bands)

* Aux (EPIC-010 scope; headers-only):

  * `tests/transport/headers/aux_text_200.snap`

  * `tests/transport/headers/aux_suppression_200.snap`  
     (No Aux HEAD/304 captures in EPIC-010; A7 remains Catalog-only.)

#### Architecture capture

* Snapshot path root: `audit/gates/arch/_arch/<epic>_<ts>/…`

## **Index and synchronization**

* Human index: `docs/evidence/INDEX.json` (titles/paths only).

* Machine mirror: `artifacts/evidence_index.jsonl` (records-only JSONL).

* Same-PR rule: Any addition, removal, or relocation here must update both indices in the same commit/PR. CI enforces human↔machine 1:1 parity, canonical JSONL, unknown-key rejection, and path-proofs.

