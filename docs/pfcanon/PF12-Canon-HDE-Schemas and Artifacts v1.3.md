# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF12-Canon-HDE-Schemas and Artifacts

**Version:** v1.3

**Status:** Canon

**Effective date:** 2025-11-20  
**Last Update Gate:** BN 7.5 Drain 

## **0.2 Scope (single home)**

**Supersession (PF10 addenda).** PF10 is living; when multiple numbered addenda exist, the later number supersedes earlier guidance. PF12 integrates the latest addenda and routes by title only to single homes (no version numbers).

**Ownership.** This document is the single home for engine catalogs, the freeze-pack manifest at `catalog/manifest.json`, and checksum sidecars (`*.sha256`). It defines closed enumerations and canonical artifact rules (manifest → `release_id`). `CANON_CHECKSUMS.json` is deprecated; the manifest at `catalog/manifest.json` is authoritative.

**Human Evidence Index (single home).** Path: `docs/evidence/INDEX.json`. Canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF). Titles and paths only; no payload bytes. Must maintain 1:1 parity with the machine mirror (see §8.3). Acceptance sentinel: `EVIDENCE_INDEX_HASH_OK` (merge-gating).

**Machine Evidence Mirror (governed here).** The JSONL mirror at `artifacts/evidence_index.jsonl` is a governed artifact (records-only); its content and schema are owned here (see §8.3). CI enforces 1:1 parity with the Human Evidence Index. Each record MUST include fields sufficient for proof and reproducibility (`sha256`, `size_bytes`, `produced_at_utc`, a `discovered_physical_path`, and a `proof_anchor` to a transcript plus on-disk stat). Path-proofs are stored alongside each artifact. Bytes are produced by build steps and validated in CI per §8; determinism follows §4; all comparisons run with `LC_ALL=C`, `TZ=UTC`, canonical JSON (UTF-8, sorted keys, compact, exactly one LF). CI hygiene (pointer; detailed rules in §8.3): mirror is canonical JSONL; unknown-key rejection is enforced; ASCII field order and sort-before-write are required; exactly one mirror file must exist. Governed locations only: evidence must live under governed repo paths (for example, `artifacts/**`, `docs/**`); transient generator paths are disallowed (details §8.3 and §8.6). Governed evidence families include Endpoint Catalog proofs, CLI parity set, `/internal/version` ops proof, DB posture snapshots, and BodyGraph artifacts enumerated in §8.6.

**Routing by title only.** Math arithmetic (scoring, thresholds, preimage recipe) and transport bytes (Reader, CLI, vendor) are routed by title only to their owning documents — HDE-Math-Spec, HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Architecture — and are not duplicated here.

**Token Registry and acceptance hints (names-only).** HDE-Governance owns the Token Registry and the semantics of all acceptance tokens. PF12 binds those tokens to concrete artifact shapes and Evidence Index / Machine Mirror records via “Acceptance hints (names-only)” lists in later sections; it does not redefine semantics. PF09-Canon-HDE-Build-Checklist is a consumer-only view: its token rosters must be a subset of the Token Registry / PF12 names and may not introduce new token names.

**Process and PR workflow.** The “update repo docs and Evidence Index in the same PR” rule lives in Epic-Process-Guide (titles only).

**Catalogized seeds (admin-only).** The Magic-10 seeds catalog at `catalog/magic10_seeds.json` is governed here (see §2.7). Changes are frozen-input changes and require `release_id` recomputation per §6.

## **0.3 Tagging**

Each section is labeled to indicate implementation status:

* **\[Implemented\]** — verified in the repository and enforced by CI and tests.  
* **\[Required-Now\]** — required for the current build and release discipline; must be satisfied before promotion.  
* **\[Speculative\]** — accepted future design; not yet wired.  
* **\[OPEN\]** — unresolved items or toggles pending a Doc-Delta.

  ## **0.4 Change policy \[Required-Now\]**

**Single homes.** This document owns catalogs (`catalog/`), the freeze-pack manifest at `catalog/manifest.json`, and checksum sidecars (`*.sha256`). Bytes owned by PF01 (scoring, thresholds, deterministic preimage and idempotence), PF02 (boundaries, single homes), PF05 (transport and vendor shaping), and PF04 (A-gates, Reader transport) are referenced by title only and are not restated here.

**Doc-Delta discipline (normative edits only).** A Doc-Delta is required for any change to:

* a catalog’s closed domain (IDs, enums, order);  
* a catalog’s schema;  
* canonical JSON serialization rules;  
* the freeze-pack manifest shape or entries (`catalog/manifest.json`);  
* frozen math inputs under `catalog/` (for example `catalog/magic10.json` IDs or inclusive maxima, `catalog/channels.json` contents);  
* the Machine Evidence Mirror path or record schema (`artifacts/evidence_index.jsonl`) or its parity rule with the Human Evidence Index (§8.3);  
* governed records-only artifacts in §8 (format or path), including:  
  * Endpoint Catalog file: `docs/ENDPOINTS_CATALOG.json` and `docs/ENDPOINTS_CATALOG.json.sha256`;  
  * Reader A7 composite proof JSON: `artifacts/proofs/reader_success_get_head_304.json`;  
  * Dev connectivity snapshot: `artifacts/runtime/env_connectivity.snapshot.json`;  
  * CLI and SDK parity JSONs: `artifacts/cli/{ab.json,ba.json,summary.json}`;  
  * `/internal/version` ops proof: `proofs/internal_version/get_head.json`;  
  * Registry report, DB fingerprint, start-command capture, environment inventories and validator outputs (names as in §8.6);  
  * **BodyGraph release bindings:** `artifacts/bodygraph/release_bindings.json`;  
  * **BodyGraph refresh policy snapshot:** `artifacts/bodygraph/refresh_policy.snapshot.json`;  
  * **BodyGraph metrics snapshot (keys-only):** `artifacts/bodygraph/metrics.snapshot.json`;  
  * **BodyGraph keys-only logs sample (sanitized):** `artifacts/bodygraph/keys_only.logs.sample`.

The Doc-Delta must state scope, targets, acceptance impact, evidence updates, and whether a new `release_id` is required.

**Evidence Index updates (same PR).** Whenever any golden, artifact, snapshot, or script path changes, update this document’s human Evidence Index (titles and paths only), the Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`), and the machine JSONL mirror at `artifacts/evidence_index.jsonl` in the same PR or commit; add a matching entry to the Change Log and Doc-Delta hooks (PF06 owns the process).

**Release identity (freeze-pack).** Any byte-level change to frozen inputs enumerated by the manifest, or to the canonical bytes of `catalog/manifest.json`, MUST produce a new `release_id` and record it in the Doc-Delta. Changes to `catalog/magic10_seeds.json` are frozen-input changes and require `release_id` recomputation. For narratives, frozen inputs include the narratives pack manifest at `catalog/narratives/manifest.json` and the pack members under `catalog/narratives/*` per §2.8.

**Editorial vs. normative.** Pure editorial rearrangements that do not change catalogs, schemas, or canonical bytes do not require a Doc-Delta. All normative changes do.

**CI enforcement (merge-blocking).** CI fails if any of the following are true:

* catalogs fail schema or closed-domain checks;  
* artifact files violate canonical JSON rules (UTF-8, sorted keys, compact separators, exactly one LF, no BOM);  
* the human Evidence Index or machine JSONL mirror is not updated alongside changed paths, or parity between them is broken;  
* the JSONL mirror is non-deterministic (not one object per line, unsorted keys, missing trailing LF), has unknown keys, is missing path-proofs, violates ASCII field order or sort-before-write, or more than one `artifacts/evidence_index.jsonl` exists;  
* required checksum sidecars for governed files are missing;  
* the Evidence Index hash sentinel does not match `INDEX.json` bytes.  
* the **Environment Matrix Snapshot** artifact — `artifacts/runtime/env_matrix.snapshot.json` (**schema v3**; **singleton** semantics); any change to its schema or path requires a Doc‑Delta and same‑PR index/mirror updates.

* **Acceptance impact:** None; clarifies Doc‑Delta scope already enforced by `EVIDENCE_INDEX_UPDATED_OK` and `EVIDENCE_INDEX_HASH_OK`.

## **0.5 Open decisions \[Tracking\]**

This section records unresolved items that require confirmation. Each remains **\[OPEN\]** until the named owner confirms. Changes that affect frozen inputs, schemas, closed domains, or canonical bytes must land with a Doc-Delta.

**CH-PRIMARY**  
 **Status:** RESOLVED  
 **Decision:** canonical Channels catalog path is `catalog/channels.json`.  
 **Owner:** Isis  
 **Severity:** critical  
 **Affects:** §§2.1, 3.2.1, 5, 6  
 **Next:** update all references; retire other channel files to Historical.

**CHANNEL-IDENTITY**  
 **Status:** RESOLVED  
 **Decision:** `channel_id = "NN-NN"` with gates zero-padded `01..64`, min-first; arrays-as-sets sort ASCII by `channel_id`.  
 **Owner:** Isis  
 **Severity:** high  
 **Affects:** §§3.2.1, 4.2  
 **Next:** enforce in schemas and CI; fail on duplicates or wrong order.

**CHECKSUMS-NAMING**  
 **Status:** RESOLVED  
 **Decision:** the freeze-pack manifest file is `catalog/manifest.json`. Any prior `CANON_CHECKSUMS.json` name is deprecated and must not be used.  
 **Owner:** Isis  
 **Severity:** high  
 **Affects:** §§5.1–5.3, 6.1–6.4  
 **Next:** rename references and stubs; ensure sidecars `*.sha256` exist for governed files.

**MAGIC10-HOME**  
 **Status:** RESOLVED  
 **Decision:** Magic-10 IDs and inclusive maxima live in `catalog/magic10.json` (not embedded in presets).  
 **Owner:** Isis  
 **Severity:** high  
 **Affects:** §§2.5–2.6, 6.1  
 **Next:** point presets to this catalog; Doc-Delta on any byte change.

**PACK-ROOT**  
 **Status:** RESOLVED  
 **Decision:** pack root is `catalog/` (used to resolve relative paths in the manifest).  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §5.1, §6.1  
 **Next:** pin in text and examples; changing it bumps `release_id`.

**SELF-LISTING**  
 **Status:** RESOLVED  
 **Decision:** NO self-listing for `catalog/manifest.json`.  
 **Owner:** Isis  
 **Severity:** low  
 **Affects:** §§5.2, 6.1  
 **Next:** keep manifest entries for governed files only; validate manifest like any other governed artifact.

**AUTH-PROFILES-USAGE**  
 **Status:** OPEN  
 **Current:** whether Authorities and Profiles catalogs are consumed in v1.  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §2.2 (and CI inclusion)  
 **Next:** confirm usage; include or exclude from CI scope accordingly.

**ID-CHARSET**  
 **Status:** RESOLVED  
 **Decision:** catalog ID charset/case policy is `^[a-z0-9_]+$`, case-sensitive.  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §3.3 and owning schemas  
 **Next:** reflect in schemas and validation text.

**PATH-CHARSET**  
 **Status:** RESOLVED  
 **Decision:** POSIX paths, no `..`, no `//`, max 256 bytes.  
 **Owner:** Isis  
 **Severity:** low  
 **Affects:** §5.1  
 **Next:** pin constraints; add to §5.1 validation rules.

**SCHEMA-DRAFT**  
 **Status:** RESOLVED  
 **Decision:** JSON Schema 2020-12; `$id` is a stable title-path.  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §3.1 and schema files  
 **Next:** ensure existing schemas declare `$schema`/`$id` accordingly.

**ALIASES-POLICY**  
 **Status:** RESOLVED  
 **Decision:** input-only aliases in request handling; outputs remain canonical (centers/planets/lines).  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §3.3 and request rules in **HDE-CLI-API-Vendor Ref**  
 **Next:** add the corresponding note here and rules in the request spec (titles only).

**SERIALIZATION-SCOPE**  
 **Status:** RESOLVED  
 **Decision:** Canonical JSON rules apply to JSON evidence artifacts; operational logs remain keys-only (not necessarily canonical JSON).  
 **Owner:** Isis  
 **Severity:** low  
 **Affects:** §4, §5  
 **Next:** none; already reflected in §4.

**EVIDENCE-PATHS**  
 **Status:** RESOLVED *(updated)*  
 **Decision:** fix the machine mirror path to `artifacts/evidence_index.jsonl` (records-only). Require 1:1 parity with the human Evidence Index, path-proofs, canonical JSONL (UTF-8, sorted keys, compact, single trailing LF).  
 **Owner:** audit  
 **Severity:** low  
 **Affects:** §8.3, §4  
 **Next:** enforce in CI; fail on mismatch.

**MIRROR-RECORD-SCHEMA**  
 **Status:** RESOLVED *(updated)*  
 **Decision:** minimum mirror record keys are  
 `{"artifact_key","role","sha256","size_bytes","produced_at_utc","discovered_physical_path","proof_anchor"}`; reject unknown keys.  
 **Owner:** audit  
 **Severity:** low  
 **Affects:** §8.3  
 **Next:** validate against schema; reject unknown keys; ensure join with human Index `(title,path)`.

**SEEDS-CATALOGIZE**  
 **Status:** RESOLVED  
 **Decision:** catalogize Magic-10 seeds at `catalog/magic10_seeds.json` (admin-only; exactly 10 entries).  
 **Owner:** Isis  
 **Severity:** medium  
 **Affects:** §2.7 (new), §3, §6  
 **Next:** add catalog \+ schema; include in manifest; any byte change recomputes `release_id`.

---

# **1\. Purpose & Single-Home Rule \[Required-Now\]**

## **1.1 What lives here**

This document is the single home for the engine’s **pack inputs** and **pack artifacts**.

* **Closed catalogs (IDs, enums).** Canonical lists and enums used by the engine (e.g., centers, gates, channels, Magic-10 category IDs, viewer-preference keys). Catalogs **MUST** be schema-validated, closed-domain, and locale-neutral.

* **Artifact serialization policy.** Canonical JSON for all pack files: **UTF-8**, **ASCII-sorted keys**, **compact separators** (`,`/`:`), **exactly one LF**, **no BOM/ANSI**. Arrays treated as sets are **deduped then ASCII-sorted**; value conflicts **fail-closed**.

* **Freeze-Pack Manifest (single home).** The authoritative manifest lives at **`catalog/manifest.json`**.

  * **Entry shape (normative):** each item is exactly `{ "path": <string>, "sha256": <hex64>, "size": <int> }`, where `sha256` is computed over the file’s **canonical bytes** (per policy above) and is **lowercase hex**.  
  * **Sidecars:** governed files carry `*.sha256` checksum sidecars.  
  * **Release identity:** `release_id = sha256(canonical_manifest_bytes)` (lowercase 64-hex). **Any byte change** to frozen inputs or to the manifest’s canonical bytes **requires a new `release_id`**.  
  * **Deprecation note:** `CANON_CHECKSUMS.json` is deprecated; use `catalog/manifest.json`.

By design, **math arithmetic** (scoring, thresholds, preimage recipe) and **transport bytes** (Reader/CLI/vendor) are **not duplicated here** and are referenced **by title only** in their owning documents.

---

## **1.2 Titles-only routing \[Required-Now\]**

**Rule.** References are by **title only**. Do **not** include version numbers in prose. Do **not** restate bytes owned by other specs.

* **Math** — scoring/thresholds; deterministic preimage (idempotence) recipe.  
   *Referenced by title only in* **HDE-Math-Spec**; no arithmetic or preimage bytes are restated here.

* **Governance / CLI** — Reader transport (headers, conditional delivery, error model), writers/errors posture, and vendor request shaping \+ typed mapping.  
   *Referenced by title only in* **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**; no transport or vendor bytes are restated here.

* **Architecture** — component boundaries (engine, adapter, presenter) and single-homes/single-emitter boundary.  
   *Referenced by title only in* **HDE-Architecture**; no architectural prose is duplicated here.

**Narratives routing reminder.** Narratives transport and example payload bytes are out of scope for this document and are routed by title to **HDE-Governance** (A7) and **HDE-CLI-API-Vendor-Ref**.

---

**2\. Catalogs Index (titles/paths only) \[Required-Now\]**

Master list of every catalog consumed by the engine with a pointer to its JSON Schema. No payload bytes in this doc.

## **2.1 Human Design topology catalogs \[Required-Now\]**

Master list items only. Titles and paths only. No payload bytes in this doc.

* **Centers** (closed set; IDs; optional attributes)

  * catalog path: `catalog/centers.json`  
  * JSON Schema path: `schemas/ums.center.v1.json`  
* **Gates** (IDs; center affiliation)

  * catalog path: `catalog/gates.json`  
  * JSON Schema path: `schemas/ums.gate.v1.json`  
* **Channels** (pairs of gate IDs; center↔channel consistency) **\[RESOLVED\]\[CRITICAL\]**

  * catalog path: `catalog/channels.json` (**canonical**)

  * **identity rule (normative):** `channel_id = "<lowGate>-<highGate>"` with gates **zero-padded `01..64`**, **min-first**; arrays-as-sets **ASCII sort** by `channel_id`

  * JSON Schema path: `schemas/ums.channel.v1.json`

  * **deprecations:** retire `catalog/channels_v1.json` and `catalog/channels_catalog_v1.json` to **Historical**; update all references accordingly

  * **validation notes:** enforce **center↔channel** consistency against Centers and Gates catalogs; **duplicates** or malformed identities **fail closed**

  * **integration (junction) gates (normative):** **only** gates **10, 20, 34, 57** form the Integration cluster; they produce **six** channels (complete graph): `10-20`, `20-34`, `20-57`, `10-34`, `10-57`, `34-57` (IDs follow the identity rule above)

  * **machine list note:** `catalog/channels.json` governs the **36 canonical channel IDs** (**IDs only**; any human-readable labels are non-normative and live outside this document)

  * **circuit attribution:** **circuit is a property of the channel**, not the individual gate (semantics are routed by title to Math/Mechanics)

  * **graph invariants:** degree/multiplicity checks are specified in **§3.2 Graph coherence checks** (titles-only); loaders must fail closed on violations

    ---

    ## **2.2 Identity & profile catalogs \[Required-Now\]**

Master list items only. Titles and paths only. No payload bytes in this doc.

* **Authorities** (closed enum, if used) \[OPEN\]

  * catalog path: \[OPEN\] confirm final repo path  
  * JSON Schema path: \[OPEN\] confirm schema path  
  * usage status: \[OPEN\] confirm whether the engine consumes this catalog in v1  
  * ID charset and case policy: \[OPEN\] confirm allowed characters and case sensitivity  
  * enum order normative: \[OPEN\] confirm whether order is normative for any consumer  
  * note: if used, treat as a **closed set** with **stable IDs**; any change to membership, IDs, or normative order **requires a `release_id` bump**  
* **Profiles** (closed enum, if used) \[OPEN\]

  * catalog path: \[OPEN\] confirm final repo path  
  * JSON Schema path: \[OPEN\] confirm schema path  
  * usage status: \[OPEN\] confirm whether the engine consumes this catalog in v1  
  * ID charset and case policy: \[OPEN\] confirm allowed characters and case sensitivity  
  * enum order normative: \[OPEN\] confirm whether order is normative for any consumer  
  * note: if used, treat as a **closed set** with **stable IDs**; any change to membership, IDs, or normative order **requires a `release_id` bump**

  

  ## **2.3 Magic-10 categories (ID list only) \[Required-Now\]**

Closed list \+ normative order (IDs only; thresholds live in Math).

* heat  
* harmony  
* communication  
* alignment  
* comfort  
* consistency  
* expansion  
* creativity  
* drive  
* balance

  ## **2.4 Viewer preferences keys \[Required-Now\]**

Exactly the 10 category keys; values are ints 0..100 (detailed validation anchored here).

**Key set**  
 The preferences object MUST contain exactly the following 10 keys, matching the Magic-10 list **and order** from §2.3:

1. heat  
2. harmony  
3. communication  
4. alignment  
5. comfort  
6. consistency  
7. expansion  
8. creativity  
9. drive  
10. balance

**Validation rules (normative)**

* Type is **JSON object**.  
* The key set **MUST equal** the list above. No keys may be missing. **No additional keys** are allowed.  
* Each value MUST be an **integer** in the inclusive range **0..100**.  
* Floats are invalid. Strings are invalid. `null` is invalid. Booleans are invalid.  
* Values MUST NOT be negative; values **\>100** are invalid.  
* **Empty objects** are invalid.

**Acceptance & CI**

* Tokens: `PREFS_KEYSET_10_OK`, `MAGIC10_DOMAIN_CLOSED_OK`.  
* Execute validations under **LC\_ALL=C**; artifacts follow the **canonical JSON** policy (UTF-8, sorted keys, compact, exactly one trailing LF).

  

  ## **2.5 Preset catalog (schema only) \[Required-Now\]**

Preset entry schema (field names and closed enums). Arithmetic and precedence live in **PF-Canon-HDE-Math-Spec** (titles only).

**Catalog pointers**

* catalog path: `catalog/presets.json`  
* JSON Schema path: `schemas/catalog.presets.v1.json`  
* Maxima live in **Magic-10**. Band maxima are **not** embedded in presets; they live in `catalog/magic10.json` alongside the Magic-10 IDs and their **inclusive maxima** (see §2.6). Any change to that file is a frozen-input change and requires a Doc-Delta \+ new `release_id`.

**Preset entry object (required fields)**

* `id` — string. Stable preset identifier; lower\_snake ASCII is required (regex `^[a-z0-9_]+$`). Must be **non-empty** and **unique** within the catalog (see §0.5).  
* `name` — string. Human-readable label.  
* `prefs` — object. **Exactly** the 10 keys from §2.4 (`heat, harmony, communication, alignment, comfort, consistency, expansion, creativity, drive, balance`). Each value is an **integer 0..100**. **No extra keys.**

**Preset entry object (enumerated fields; closed sets)**

* `scope` — enum: `viewer`, `pair`  
* `visibility` — enum: `public`, `internal`  
* `lifecycle` — enum: `active`, `retired`

**Optional fields**

* `description` — string. Short explanatory text.  
* `notes` — string. Internal notes (non-UI).

**Validation rules (normative)**

* Type is **JSON object**. Required fields: `id`, `name`, `prefs`.  
* `id` obeys charset/case policy `^[a-z0-9_]+$`, case-sensitive; **unique** within the catalog.  
* `prefs` must satisfy §2.4 **exactly** (10 keys; values are **ints 0..100**). Floats invalid. Strings invalid. `null` invalid. Booleans invalid.  
* Enumerated fields use only values from their **closed sets**; adding a new value requires a Doc-Delta **and** a schema update.  
* **No additional properties** beyond the fields listed here.

**Change control**

* Changing the `prefs` key set or any closed enum requires a **Doc-Delta** and yields a new `release_id` (frozen-input surface).  
* Changes to `catalog/magic10.json` maxima are frozen-input changes (see §2.6, §6.1) and also require a new `release_id`.

**Acceptance & CI (titles-only)**

* Tokens: `PRESET_SCHEMA_OK`, `PRESET_ENUMS_CLOSED_OK`, `PRESET_ID_CHARSET_OK`, `PREFS_KEYSET_10_OK`, `MAGIC10_DOMAIN_CLOSED_OK`.  
* Canonical JSON policy applies to the catalog file (UTF-8, **sorted keys**, **compact**, exactly **one** trailing LF).

  ## **2.6 Magic-10 catalog (IDs, caps, inclusive maxima) \[Required-Now\]**

Single home for Magic-10 identifiers, their normative order, and preset-specific inclusive maxima. Arithmetic remains in **PF-Canon-HDE-Math-Spec** (titles only).

**Catalog pointers**

* catalog path: `catalog/magic10.json`  
* JSON Schema path: `schemas/catalog.magic10.v1.json`

**Object shape — required fields**

* `ids` — array of **10** strings. Exactly the Magic-10 identifiers in normative order (see **PF-Canon-HDE-Math-Spec**, titles only). Each item is ASCII lowercase matching regex `^[a-z]+$`. All **unique**.  
* `maxima` — object keyed by **preset id**. **Required keys:** `"A"`, `"B"`.  
  * Each preset value is an object with keys `"cool"`, `"open"`, `"warm"` as **integers**; these are **inclusive-high** maxima for band mapping (Glow is the else case).

**Object shape — optional fields**

* `caps` — object (if used in v1; otherwise omit). If present, list only Magic-10 keys with **integer** values.  
* `notes` — string. Short internal comments.

**Validation rules (normative)**

* `ids` contains **exactly** the 10 Magic-10 IDs in the **pinned order**; duplicates are invalid.  
* `maxima` **must** contain `"A"` and `"B"`. For each preset:  
  * required keys `"cool"`, `"open"`, `"warm"` are **integers**;  
  * **monotonicity:** `cool ≤ open ≤ warm`;  
  * values are validated as **frozen math inputs** (any change ⇒ new `release_id`).  
* If `caps` is present, it must use only Magic-10 keys with **integer** values.  
* **No additional top-level properties** beyond the fields listed here.

**Change control**

* Any byte change to `catalog/magic10.json` (IDs, order, maxima values, caps, or structure) requires a **Doc-Delta** and yields a new `release_id`.  
* Adding or removing a preset entry in `maxima` also requires a new `release_id`.

**Routing**

* Band mapping arithmetic and behavior remain in **PF-Canon-HDE-Math-Spec** (titles only). Transport, headers, and validators live in **PF-Canon-HDE-CLI-API-Vendor-Ref** (titles only).

**Acceptance & CI (titles-only)**

* Tokens: `MAGIC10_DOMAIN_CLOSED_OK`, `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`, `PREFS_KEYSET_10_OK`.

## **2.7 Magic-10 seeds (admin-only, frozen) \[Required-Now\]**

Admin-only seed templates for narrative/category scaffolding (IDs only; not surfaced publicly; bytes live in the repo).

Catalog path: catalog/magic10\_seeds.json  
 JSON Schema path: schemas/catalog.magic10\_seeds.v1.json

Shape (minimum): object keyed by id with fields {id, template\_id, seed\_version, updated\_at\_utc, checksum\_sha256, admin\_only}.  
 Cardinality: exactly 10 entries (one per Magic-10 category).

Governance: listed in the pack manifest; any byte change requires a Doc-Delta and a new release\_id (see §6).  
 Validation: closed domain enforced in §3; admin\_only must be true; checksum\_sha256 must match the canonical serialized seed body; checks run under LC\_ALL=C.

Acknowledged — I may reformat structure/wording only to conform to canon and improve readability, while preserving substance.

---

Acknowledged — applying the plan exactly (append-only edits; canon \+ readability).

---

### **2.8 Narratives pack (keys/templates/palettes/suppression\_map) \[Required‑Now\]**

**Catalog paths.**

* `catalog/narratives/keys.json`  
* `catalog/narratives/templates.json`  
* `catalog/narratives/palettes.json` *(optional)*  
* `catalog/narratives/suppression_map.json`

**JSON Schema paths.**

* `schemas/catalog.narratives.keys.v1.json`  
* `schemas/catalog.narratives.templates.v1.json`  
* `schemas/catalog.narratives.palettes.v1.json`  
* `schemas/catalog.narratives.suppression_map.v1.json`

**Pack manifest (narratives) & identity.**  
 A **narratives pack manifest** **MUST** exist at `catalog/narratives/manifest.json`.  
 `pack_sha = sha256(canonical_bytes("catalog/narratives/manifest.json"))` (lowercase 64‑hex).  
 The narratives pack manifest **MUST** be included in `catalog/manifest.json` and carry a `*.sha256` sidecar.

**Governance (normative).**  
 All four pack files **and** the narratives pack manifest are governed inputs and **MUST** be listed in `catalog/manifest.json` with `*.sha256` sidecars. **Canonical JSON** policy applies everywhere (UTF‑8, sorted keys, compact, exactly one LF; arrays‑as‑sets deduped & ASCII‑sorted). **Any byte change** to any of the four files **or** the narratives pack manifest is a frozen‑input change and requires a Doc‑Delta and a new `release_id` (§6).

**Routing (titles‑only).**  
 Catalog membership & schemas: PF12 (this document).  
 Aux transport/suppression semantics & endpoint bytes: PF04/PF05 (titles‑only).

**Acceptance & CI (titles‑only).**  
 `NARR_PACKS_IN_MANIFEST_OK`, `NARR_PACK_MANIFEST_OK`, `NARR_PACK_IDENTITY_OK`, `NARR_PACKS_CANONICAL_JSON_OK`. *(Tokens live in Governance.)*

---

# **3\. Catalog Validation & Integrity \[Required-Now\]**

## **3.1 JSON Schema validation**

Every catalog file MUST pass its owning JSON Schema. No extra keys. No missing required fields.

Scope

* “Catalog file” means any JSON artifact that enumerates a closed or structured domain used by the engine.  
* “Owning JSON Schema” is the single schema that defines the structure, types, and constraints for that catalog. Reference it by title and path only.

Normative rules

* Each catalog MUST validate against its owning schema with no errors.  
* All required properties defined by the schema MUST be present. None may be omitted.  
* No additional properties are allowed unless the schema explicitly permits them at that object level.  
* Property types MUST match exactly (e.g., integer ≠ number; strings are not numeric).  
* All enums define closed sets. Values outside the set are invalid.  
* Arrays that represent sets MUST contain no duplicates. If uniqueness cannot be expressed in JSON Schema, a companion check MUST enforce it.  
* For arrays of objects used as sets, the schema MUST declare an identity key for deduplication and ordering. If an object-array is declared a set without an identity rule, that is a schema error; enforce via a companion check until the schema is corrected.  
* String identifier fields such as id MUST be non-empty. Charset and maximum length are governed in §0.5; until formally pinned, use the default guidance ^\[a-z0-9\_\]+$ (case-sensitive).  
* Numeric ranges, if present, MUST be enforced exactly as defined in the schema.  
* Schema validation concerns data shape and values. Serialization rules (canonical JSON, key ordering, single trailing LF) are handled by the Artifact Serialization Policy (§4).  
* Identity-code constraints: where IDs must be normalized (e.g., channel identity), the schema SHOULD encode the constraint (min→max, zero-padded NN-NN, ASCII). Example (informative): channel\_id matches the min-first zero-padded pattern and domain 01..64-01..64; arrays-as-sets are ASCII-sorted by channel\_id.  
* Seeds checksum (catalog/magic10\_seeds.json): checksum\_sha256 MUST equal the sha256 of the seed’s canonical serialized body; enforce via a companion check (see §2.7, §4).

Schema hygiene

* Each schema MUST include $schema and SHOULD include $id.  
* Draft: 2020-12; $schema MUST be [https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema). $id MUST be a stable repo title-path for the catalog (e.g., schemas/ums.channel.v1.json) — not an external URL.  
* Schemas SHOULD set additionalProperties: false at closed object levels, and allow additional properties only where intended.  
* Cross-catalog references that a schema cannot express (e.g., membership in another catalog’s closed set, degree/multiplicity invariants) MUST be enforced by companion checks (see §3.2–§3.3 and Integrity CI in §8.2).  
* Where identity codes are constrained by format (e.g., zero-padded numeric identifiers and min-first orientation), the schema SHOULD encode that constraint (pattern/range); otherwise a companion check MUST enforce it.

CI enforcement

* Validation MUST run for every catalog locally and in CI. Any failure is a hard stop.  
* When a catalog or its schema changes, validation MUST re-run and succeed in the same change.  
* Uniqueness, cross-reference, ordering, and arrays-as-sets rules that exceed JSON Schema’s native capabilities MUST be enforced by companion checks.  
* Run checks under LC\_ALL=C per §4.3.

Acceptance hints

* CATALOG\_SCHEMA\_OK  
* CATALOG\_NO\_ADDITIONAL\_PROPS\_OK  
* CATALOG\_ENUM\_DOMAIN\_CLOSED\_OK  
* ARR\_SET\_NO\_DUPLICATES\_OK  
* ARR\_SET\_IDENTITY\_DECLARED\_OK (when arrays of objects are used as sets)  
* SCHEMA\_HYGIENE\_OK  
* SCHEMA\_ID\_STABLE\_OK (repo title-path in $id)

  ## **3.2 Graph coherence checks (topology)**

Topology-level integrity rules across Centers, Gates, and Channels.

Scope

* Inputs. The Centers catalog, Gates catalog, and Channels catalog from §2.1.  
* Derived maps used by checks.  
  * center\_of\_gate\[g\] from the Gates catalog (each gate’s center)  
  * gates\_of\_channel\[ch\] \= \[g\_a, g\_b\] from the Channels catalog  
  * centers\_of\_channel\_derived\[ch\] \= { center\_of\_gate\[g\_a\], center\_of\_gate\[g\_b\] }

  ### **3.2.1 Channel degree and identity (channel ↔ exactly two gates)**

Cardinality

* Each channel MUST reference exactly two gate IDs.  
* The two gate IDs MUST be present in the Gates catalog and MUST be distinct. A channel MUST NOT list the same gate twice.

Identity and uniqueness \[RESOLVED\]

* Canonical identity. A channel’s identity is the ASCII-ascending, zero-padded gate pair encoded as "-", where lowGate/highGate are the two referenced gate IDs normalized to two digits (01..64) and ordered lexicographically as strings (see §2.1, Channels). (Schema pattern reference: ^(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])$.)  
* Uniqueness. No two channels may share the same canonical identity. If the same identity appears with different element bytes, fail closed.

Arrays-as-sets coupling

* Any array that lists channels as a set (for example, a top-level channels list) MUST be deduplicated by the canonical identity above and MUST be ASCII-sorted by that identity (see §4.2). Any duplicate identity or out-of-order identity is a validation error.

CI acceptance hints

* TOPOLOGY\_CHANNEL\_DEGREE\_2\_OK  
* ARR\_SET\_NO\_CONFLICTS\_OK  
* ARR\_SET\_ASCII\_SORT\_OK  
* CATALOG\_ORIENTATION\_CANON\_OK  
* TOPOLOGY\_COHERENCE\_OK

  ### **3.2.2 Gate↔center and channel↔center consistency**

* Every gate MUST reference exactly one valid center ID from the Centers catalog (domain closure).  
* For each channel, compute centers\_of\_channel\_derived\[ch\] \= { center\_of\_gate\[g\_a\], center\_of\_gate\[g\_b\] }.  
* If the Channels catalog stores an explicit center field (or fields), those values MUST equal centers\_of\_channel\_derived\[ch\].  
* There is no inherent requirement that the two centers of a channel differ; enforce distinctness only if a separate rule in this document or the owning schema declares it.

CI acceptance hints

* TOPOLOGY\_CENTER\_CONSISTENCY\_OK  
* TOPOLOGY\_DOMAIN\_CLOSED\_OK  
* XREF\_MEMBERSHIP\_OK

  ### **3.2.3 No orphans: every referenced ID exists**

* Every center ID referenced by any gate MUST exist in the Centers catalog.  
* Every gate ID referenced by any channel MUST exist in the Gates catalog.  
* There MUST be zero dangling references across all three catalogs. Any missing target is a hard validation error.

CI acceptance hints

* TOPOLOGY\_NO\_ORPHANS\_OK

  ### **3.2.4 Degree vectors (optional)**

Optional invariants that assert expected degree counts; enforce only when explicitly declared by the owning spec or a referenced proof artifact.

Scope

* Inputs: Centers, Gates, Channels catalogs from §2.1.  
* Graph model: gate\_degree\[g\] \= count of channels that reference gate g.  
* Source of truth. If degree expectations are provided (e.g., in a field in the Gates schema or a separate declared artifact listed in the pack), they govern the checks below; otherwise this subsection is not applicable.

Normative rules (apply only when expectations are declared)

* Build the observed vector: for each gate g, compute gate\_degree\[g\].  
* Compare to the declared expected vector.  
* Every gate that appears in the expected vector MUST appear in the observed vector with the same integer value.  
* If the expected vector declares a closed key set, the observed vector MUST have exactly that key set.  
* All degree values MUST be non-negative integers. Any mismatch is a validation error.

Notes

* You may declare only a subset of gates; in that case, enforce equality only for the declared subset.  
* Encode any special-case adjustments (e.g., temporary exclusions) in the declared artifact rather than prose.

CI enforcement

* Run this check whenever Centers, Gates, Channels, or the declared degree-vector artifact changes. Fail on first mismatch.

Acceptance hints

* DEGREE\_VECTORS\_DECLARED\_OK  
* DEGREE\_VECTORS\_MATCH\_OK  
* DEGREE\_VECTORS\_NONNEG\_INT\_OK

  ### **3.2.5 Distinguished sets (optional)**

Optional invariants that declare named, frozen subsets of channels or gates. Enforce only when a set is declared.

Scope

* Inputs: Centers, Gates, Channels catalogs from §2.1.  
* “Distinguished set” means a named subset, e.g., Talk Ladder, Narrative Throat, or Direct Motor→Throat.  
* Source of truth. The set definition MUST be provided by a declared source (e.g., a dedicated catalog, a section in a proof artifact, or a field in a governed catalog) and referenced by title/path in §8.3.

Declaration requirements — each distinguished set MUST declare:

* name (string)  
* type with value "channels" or "gates"  
* members (array treated as a set per §4.2)  
* optional metadata (e.g., rationale, provenance), if needed

Identity

* For type: "gates", identity is the gate ID.  
* For type: "channels", identity is the canonical channel identity "-" (§3.2.1).

Normative rules (apply only when a set is declared)

* Domain closure: every member MUST belong to the relevant closed domain (see §3.3).  
* No duplicates: members MUST be deduplicated by identity; if the same identity appears with different element bytes, fail closed.  
* Ordering: members MUST be ASCII-ascending by identity (arrays-as-sets, §4.2).  
* Cross-consistency:  
  * For type: "channels", both gate IDs MUST resolve to valid gates; derived centers MUST be consistent with §3.2.2.  
* Closed vs partial sets: If a set is declared closed, the members list is authoritative and MUST be complete; otherwise, validate membership and set semantics only.

CI enforcement

* Validate domain closure, deduplication, ordering, and topology cross-checks for every declared set; fail on the first violation.

Acceptance hints

* DISTINGUISHED\_DECLARED\_OK  
* DISTINGUISHED\_DOMAIN\_CLOSED\_OK  
* DISTINGUISHED\_NO\_CONFLICTS\_OK  
* DISTINGUISHED\_ASCII\_SORT\_OK  
* DISTINGUISHED\_TOPOLOGY\_CONSISTENT\_OK

  ### **3.2.6 Integration & multiplicity invariants (loader checks) \[NEW | NORMATIVE\]**

Scope

* Inputs: Centers, Gates, Channels catalogs from §2.1; the graph model defined at the top of §3.2.

Normative rules

* Integration degree test (gate graph). Only gates 10, 20, 34, 57 have degree \= 3 (each participates in three distinct channels). All other gates have degree \= 1\. Fail closed if violated.  
* Center-pair multiplicity. When channels are reduced to unordered center pairs, the per-pair counts MUST sum to 36 across the wheel. The expected multiplicities MUST be encoded in a governed artifact or inlined as a closed list in catalog/channels.json and listed in the Evidence Index/machine mirror. Fail closed on mismatch.  
* Simple vs multigraph. At channel level, the graph is simple (no duplicate edges after canonical NN-NN normalization). At center level, it is a multigraph (parallel edges allowed) and is used for analytics only; mechanics remain per channel.

Evidence hooks (titles/paths only)

* audit/gates/topology/degree\_check.log — observed degree map and pass/fail  
* audit/gates/topology/multiplicity\_vector.log — observed center-pair multiplicities and pass/fail

CI acceptance hints

* TOPOLOGY\_INTEGRATION\_DEGREE\_OK  
* TOPOLOGY\_CENTER\_MULTIPLICITY\_OK  
* TOPOLOGY\_SIMPLE\_GRAPH\_OK

  ## **3.3 Domain closure & enums**

All IDs and enum values MUST come from the catalog’s closed domain. Unknowns are rejected.

Scope

* Applies to all closed-domain catalogs in §2 (for example, Centers, Gates, Channels, Authorities, Profiles) and to any artifact that references them (for example, presets, invariants).  
* Also applies to the Magic-10 category IDs and the viewer preferences key set from §§2.3–2.4.

Normative rules

* Closed domain per release. For a given release, each catalog defines the complete set of valid IDs or enum values.  
* Exact membership. Every referenced ID or enum value MUST be a member of the owning catalog’s set. Any value not present is invalid.  
* No coercion. Do not coerce, normalize, or substitute unknown values. Treat them as hard validation errors.  
* Case & charset (RESOLVED). IDs are case-sensitive, ASCII, and MUST match the regex ^\[a-z0-9\_\]+$ (no spaces).  
* Aliases policy (RESOLVED). Input-only aliases may be accepted at ingestion (per alias catalogs); all outputs are canonical. Alias catalogs, when present, live separately and are validated independently.  
* Append/retire policy. Renames and deletions are discouraged; additions require explicit review and may require a release\_id bump and catalog version note.  
* Normative order. When order is consumed, it is defined by the owning catalog. Otherwise, treat sets as unordered; programmatic lists MUST sort in ASCII ascending for reproducibility.

Specific applications

* Magic-10 categories (§2.3). Only the ten category IDs listed are valid. If any consumer treats order as normative, do not reorder without a Doc-Delta.  
* Viewer preferences (§2.4). The preferences object key set MUST equal the ten category IDs. Unknown keys are invalid.  
* Magic-10 seeds (§2.7). Exactly ten entries (one per category); key set MUST match the ten category IDs; `admin_only` MUST be true for all entries; `checksum_sha256` MUST match the canonical serialized seed body (see §3.1); any change is a frozen-input change and may require a release\_id bump (see §6).  
* Topology catalogs (§2.1).  
  * Centers. Closed set: head, ajna, throat, g\_center, ego, spleen, solar\_plexus, sacral, root.  
  * Gates. A gate’s center MUST be a member of the Centers set.  
  * Channels. Each channel MUST reference two gate IDs from Gates and use the canonical identity NN-NN (zero-padded, min-first). Any other format is invalid.

Validation mechanics

* Prefer JSON Schema enum for explicit closed sets where feasible.  
* When values are references to another catalog, implement a cross-reference check that builds the owner set and validates membership for every reference.  
* Where JSON Schema cannot express the constraint, add a companion validation step that fails on the first unknown.

CI enforcement

* Run domain-closure checks on every change to a catalog or any artifact that references it.  
* Treat any unknown ID or enum value as a hard failure.  
* When a closed set changes, re-run all dependent validations in the same change.  
* Execute under LC\_ALL=C per §4.3.

Acceptance hints

* CATALOG\_DOMAIN\_CLOSED\_OK  
* CATALOG\_NO\_UNKNOWN\_IDS\_OK  
* PREFS\_KEYSET\_10\_OK  
* MAGIC10\_DOMAIN\_CLOSED\_OK  
* XREF\_MEMBERSHIP\_OK  
* ALIASES\_INPUT\_ONLY\_OK  
* ID\_CHARSET\_POLICY\_OK

Acknowledged — I may reformat structure/wording only to conform to canon and improve readability, while preserving substance.

---

### **3.4 Narratives composer response schema \[Required‑Now\]**

**Schema path.** `schemas/narratives.composer.response.v1.json`

**Valid shapes (reject unknown keys).**

* **Text variant**  
   `composition_id` (ASCII, 8..128)  
   `fragment_ids` (array, **minItems: 1**)  
   `pack_sha` (lowercase 64‑hex)  
   `policy_reason` (enum: `"conflict"`)  
   `text` (string, **maxLength: 300**, **MUST NOT** contain `"\r"`)

* **Suppressed variant**  
   Same as Text variant **without** `text` (suppression \= missing body text)

**Serialization & validation.**  
 Canonical JSON applies to any stored artifacts (UTF‑8, sorted keys, compact, exactly one LF; no BOM). The schema **must reject** any fields not listed above and any CR characters (`"\r"`) inside `text`.

**Routing (titles‑only).**  
 Transport headers, A7 rules, and suppression policy semantics: PF04/PF05.

**Persistence profile (titles‑only).**  
 Any admin persistence of narrative text **MUST** honor the ≤300/no‑CR limits and identity fields (`composition_id, fragment_ids, pack_sha, release_id`). Storage/retention is routed to Glow Infrastructure (names‑only). Logging/privacy posture (keys‑only; never log text) is routed to PF04.

# **4\. Artifact Serialization Policy**

Canonical bytes for all pack files and for the manifest.

### **Scope**

* Applies to all pack files listed in this document and to the pack manifest.  
* The rules below define the exact byte form used for hashing and equality checks.  
* These rules also apply to JSON evidence artifacts listed in Appendix D (so evidence is reproducibly comparable). Operational logs are out of scope for canonicalization; they must remain keys-only per Governance §7.1 and are not required to be canonical JSON.

### **Non-goals**

* This section does not restate any schema content, arithmetic, or transport behavior. It only defines how valid JSON is serialized to bytes.

### **Canonical JSON rules (normative)**

* Encoding: UTF-8 without BOM.  
* Whitespace: compact (no pretty/indent), no trailing spaces, exactly one trailing newline LF (`\n`) at end of file.  
* Objects: keys are emitted in ASCII ascending order at every object level.  
* Numbers: encoded as JSON numbers (not strings). NaN/Infinity disallowed.  
* Booleans/null: lowercase JSON literals.  
* Arrays:  
  * If the array represents a set, it **MUST** be de-duplicated and ASCII-sorted by its identity rule (see §3.2/§3.3).  
  * If the array is ordered by spec, preserve the schema-declared order; do not re-sort.  
* JSONL artifacts (records-only): one canonical JSON object per line; no blank lines; each line obeys all canonical JSON rules above (sorted keys, compact); the file ends with exactly one trailing LF.  
* Escapes: JSON string escaping per RFC 8259; no non-canonical escape variants.  
* **Locale:** all canonicalization and comparisons run under **`LC_ALL=C, LANG=C, TZ=UTC`**.  
* **Capture env pins:** header/body snapshot jobs and canonicalization checks **MUST** run with the same env pins: **`LC_ALL=C, LANG=C, TZ=UTC`**.

### **Determinism & hashing**

* All governed pack files’ `sha256` values in the manifest are computed over their canonical bytes.  
* The `release_id` is the `sha256` of the canonical bytes of `catalog/manifest.json` (see §6.1).  
* Any byte that violates the rules above invalidates the stored digest and **must fail** checks.

### **CI enforcement**

* Canonicalization check must re-serialize each governed JSON and byte-compare to the on-disk file.  
* Two-run identity: two consecutive canonical dumps of the same object graph must produce identical bytes.  
* Fail closed on: unsorted keys, missing LF, extra whitespace, BOM, duplicated set entries, locale drift, or number/string mismatches.

### **Acceptance hints (titles-only)**

* DET\_SERIALIZER\_OK  
* TWO\_RUN\_IDENTITY\_OK  
* JSON\_CANONICAL\_CHECK\_OK  
* MANIFEST\_FILE\_EQ\_CANON\_OK  
* JSONL\_RECORDS\_CANON\_OK  
* **ENV\_LC\_ALL\_C\_OK**

§§5–8 reference this policy without redefining it.

---

## **4.1 Canonical JSON rules**

All artifacts covered by §4 **MUST** be encoded as canonical JSON. The same semantic content **MUST** always yield identical bytes.

### **Encoding and file boundary**

* Text encoding: UTF-8.  
* No BOM.  
* File terminator: exactly one line feed at end of file (LF, byte `0x0A`).  
* No carriage returns (`0x0D`) and no trailing spaces or tabs.

### **Object key ordering**

* For every JSON object, keys **MUST** be emitted in strict ASCII ascending order.  
* Ordering is recursive: apply the same rule to all nested objects.  
* Arrays preserve their input order; only object member order is canonicalized.

### **Whitespace and separators**

* Compact form only. No pretty printing.  
* Object member separator is a comma `,` with no surrounding spaces.  
* Name–value separator is a colon `:` with no surrounding spaces.

Example shape:  
 {"a":1,"b":\[true,false\],"c":{"d":2}}

* 

### **Strings**

* Delimiter: double quotes.  
* Content **MUST** be valid UTF-8.  
* Escape only what JSON requires: `"`, `\`, and control characters `U+0000..U+001F` (use the shortest legal escape such as `\n`, `\t`, or `\u00XX`).  
* Do not escape non-ASCII letters; emit them as UTF-8.  
* Disallow unpaired surrogates; strings **MUST** be well-formed Unicode.

### **Numbers**

* Follow the owning schema’s types.  
* Integers: base-10, no leading zeros, no plus sign, no decimal point, no exponent.  
* Non-integers: not permitted in pack artifacts. If a future schema requires non-integer quantities, they **MUST** be represented as exact strings (or exact integer encodings) with a Math-defined rounding/precision policy (see §4.3).

### **Booleans and null**

* Booleans are `true` or `false` (lowercase).  
* `null` only where explicitly allowed by the schema.

### **Field names**

* Field names follow the schema. If unspecified, prefer `lower_snake` ASCII for new fields to keep key ordering unambiguous.

### **Determinism checks (normative)**

* Re-serializing the same in-memory value **MUST** produce byte-for-byte identical output.  
* Canonicalization **MUST NOT** reorder arrays or change values.  
* Any byte that violates the rules above invalidates the artifact.

### **JSONL artifacts (records-only)**

* Structure: exactly one JSON object per line; no array wrapper.  
* Line canon: each line is canonical JSON (sorted keys, compact separators).  
* File boundary: end with exactly one LF; no blank lines before EOF.  
* Purpose: used by the machine Evidence Index and other records-only evidence; see §8.

### **Acceptance hints**

* CANON\_JSON\_UTF8\_OK  
* CANON\_JSON\_SORTED\_KEYS\_OK  
* CANON\_JSON\_COMPACT\_OK  
* CANON\_JSON\_SINGLE\_LF\_OK  
* CANON\_JSON\_NO\_BOM\_OK  
* CANON\_JSON\_IDENTITY\_OK

---

## **4.2 Arrays-as-sets discipline**

Deduplicate by identity. Sort ASCII. On value conflict, fail closed.

### **When this applies**

* Any array that a schema defines as a set rather than an ordered list.  
* Typical cases include top-level catalog entries, lists of IDs, and composite references declared as sets.  
* The owning schema **MUST** explicitly mark which arrays are treated as sets (and, where possible, encode the identity rule).

### **Identity**

* Scalars: identity is the scalar value itself.  
* Objects: identity is the value of the field the schema designates as the identity key (for example `id`).  
* Composite identities: if identity is a tuple, the schema **MUST** define a canonical projection to a single string (e.g., normalize field order and join with a fixed delimiter).  
* If no identity rule is defined for an object array that is treated as a set, that is a schema error to resolve (enforce via a companion check until corrected).

### **Normalization pins (identity projection)**

* The projected identity string **MUST** be canonical and exactly match on-disk bytes for comparison/sort (no trimming, case changes, or locale transforms).  
* Where the schema mandates a normalized representation, the catalog **MUST** store that form.  
  * Example (channels): `channel_id = "<a>-<b>"` with zero-padded `01..64`, min-first (e.g., `31-07`, `57-20/57-34/10-57`).

### **Deduplication**

* Build a map `identity → element`.  
* If the same identity appears multiple times with byte-identical elements, keep a single instance.  
* If the same identity appears with different element values, that is a conflict → fail closed (companion check should point to the first divergent field).

### **Ordering**

* After deduplication, arrays-as-sets **MUST** be ASCII ascending by the identity string (byte-wise, case-sensitive, locale-independent; treat `LC_ALL=C` as the reference).  
* Producers **MUST** write arrays in this order; validators reject out-of-order sets.

### **Acceptance hints**

* ARR\_SET\_IDENTITY\_DECLARED\_OK  
* ARR\_SET\_NO\_DUPLICATES\_OK  
* ARR\_SET\_NO\_CONFLICTS\_OK  
* ARR\_SET\_ASCII\_SORT\_OK  
* ARR\_SET\_PROJECTION\_CANON\_OK

---

## **4.3 Locale & determinism pins**

`LC_ALL=C`. No wall clock. No randomness. No floats in artifact generation.

### **Scope**

* Applies to every step that produces canonical pack files or the pack manifest.

### **Locale and environment**

* Set `LC_ALL=C` for all generation and verification steps.  
* Recommended pins: `LANG=C` and `TZ=UTC` to avoid host variance.  
* Any collation, case-folding, or string comparison used during generation **MUST** be performed under this locale.

### **Time sources**

* Artifact generation **MUST NOT** read the wall clock.  
* No timestamps, date strings, or time-derived fields may be computed during generation.  
* If a timestamp appears in surrounding evidence, it **MUST** come from release metadata or CI context and **MUST NOT** influence artifact bytes.

### **Randomness and process nondeterminism**

* No calls to RNGs or seed-dependent libraries.  
* Do not depend on memory addresses, iteration order of non-deterministic structures, or any nondeterministic API.  
* Hash-order or interpreter randomization **MUST NOT** affect outputs; canonical JSON ordering applies.

### **Floating point prohibition**

* Artifact generation **MUST NOT** use floating-point arithmetic.  
* Outputs **MUST NOT** contain floating-point numbers.  
* If a future schema requires non-integer quantities, represent them as exact integers or exact strings with a Math-defined encoding and rounding policy.

### **Determinism requirements**

* Two runs over the same inputs and code **MUST** produce byte-for-byte identical artifacts.  
* Generation **MUST** be pure with respect to inputs declared by this document and the owning schemas.

### **CI enforcement**

* Assert `LC_ALL=C` in the environment at generation and at checks.  
* Run a two-run identity check over the full pack and manifest.  
* Grep/audit for wall-clock calls, RNG usage, and float emission in the generation path. Any hit is a hard failure.

### **Acceptance hints**

* ENV\_LC\_ALL\_C\_OK  
* NO\_WALL\_CLOCK\_OK  
* NO\_RANDOMNESS\_OK  
* NO\_FLOATS\_IN\_GEN\_OK  
* TWO\_RUN\_IDENTITY\_OK

---

# **5\. Freeze-Pack Manifest (catalog/manifest.json) \[Required-Now\]**

Got it. Here’s a single, paste-ready merged section that keeps everything from your **ORIGINAL** and the **NEW** refinement, without duplication or drift.

---

## **5.1 Manifest file shape \[Required-Now\]**

**Purpose.** Canonical JSON document that lists **every frozen input** with `{path, sha256, size}` and top-level metadata. The canonical bytes of this file determine `release_id` (see §6).

### **Top-level object (no extras)**

* `root` — string. **Fixed:** `"catalog/"`.  
* `version` — string. Semver for the catalog pack (not app version).  
* `built_at_utc` — string. UTC ISO-8601 timestamp (`YYYY-MM-DDThh:mm:ssZ`).  
* `files` — array of entry objects.

No other top-level members are allowed. **Self-exclusion:** the root manifest **MUST NOT** list itself (`catalog/manifest.json`). Listing `catalog/narratives/manifest.json` is **required** (see “Frozen inputs completeness” and §2.8).

### **Files\[\] as a set (arrays-as-sets policy)**

Treat `files` as a **set keyed by `path`**. **Deduplicate by `path`**, **ASCII-sort** by `path` (byte-wise, locale-independent), and **fail closed** on conflicting duplicates. Producers **MUST** emit `files` in ASCII ascending path order. Canonical JSON applies everywhere (UTF-8, no BOM; **sorted keys**; compact separators; **exactly one trailing LF**).

### **Frozen inputs completeness (normative)**

`files[]` **MUST enumerate all frozen inputs** for the release. This includes, at minimum, the four narratives pack members under `catalog/narratives/*` **and** the narratives pack manifest at `catalog/narratives/manifest.json` (see §2.8 Narratives pack). Missing any required narratives entry is an **error**.

### **Entry object (exactly three fields)**

* `path` — string. POSIX path **relative to** the pack root (`root == "catalog/"`).  
  * Do **not** include the `"catalog/"` prefix.  
  * **No** absolute paths; **no** `..`; **no** `//`.  
  * Case-sensitive. Path charset/length limits per §0.5 (default: `^[a-z0-9_./-]+$`, max 256 bytes).  
* `sha256` — string. **64-char lowercase hex** of the file’s **canonical bytes** (per §4 policy).  
* `size` — integer. Byte length of the same canonical bytes (non-negative; fits in signed 64-bit).

**Additional properties.** Not allowed. Each entry **MUST** contain **exactly** `path`, `sha256`, `size`.

### **Ordering (producer requirement)**

`files[]` **MUST** be ASCII ascending by `path` (**byte-wise; locale-independent**). Producers **MUST** emit in this order.

### **Validation rules (summary)**

* Every listed `path` **MUST** resolve to an existing file under the pack root (`catalog/`).  
* For each entry, **recompute** SHA-256 over the file’s **canonical bytes**; it **must match** `sha256`.  
* **Recompute** byte length; it **must match** `size`.  
* Unknown fields or missing required fields are **errors**.  
* Duplicate `path` values with differing `sha256` or `size` are **conflicts → error**.  
* **Narratives completeness:** `catalog/narratives/manifest.json` **and** the four narratives members under `catalog/narratives/*` **MUST** be present (see §2.8); omission is an **error**.  
* The manifest itself **MUST** be canonical JSON on disk (UTF-8, sorted keys, compact, exactly one LF).

### **Example (illustrative only)**

{

  "root": "catalog/",

  "version": "1.0.0",

  "built\_at\_utc": "2025-10-28T00:00:00Z",

  "files": \[

    { "path": "centers.json",

      "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",

      "size": 1234 },

    { "path": "gates.json",

      "sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789",

      "size": 5678 },

    { "path": "narratives/manifest.json",

      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",

      "size": 321 },

    { "path": "narratives/templates.json",

      "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",

      "size": 654 }

  \]

}

*(The example is non-normative and abbreviated; real catalogs will contain additional governed files.)*

### **CI enforcement (minimum)**

* `PACK_ROOT_PINNED_OK`  
* `MANIFEST_TOP_LEVEL_OBJECT_OK`  
* `MANIFEST_FILES_ARRAY_OK`  
* `MANIFEST_ENTRY_FIELDS_OK`  
* `MANIFEST_SHA256_HEX64_OK`  
* `MANIFEST_SIZE_MATCH_OK`  
* `MANIFEST_PATH_ASCII_SORT_OK`  
* `MANIFEST_NO_DUP_PATHS_OK`  
* `MANIFEST_FILE_EXISTS_OK`  
* `MANIFEST_CANON_JSON_OK`  
* `PACK_MANIFEST_NO_SELF_LISTING_OK`

*(Narratives pack-specific acceptance lives in §2.8: `NARR_PACKS_IN_MANIFEST_OK`, `NARR_PACK_MANIFEST_OK`, `NARR_PACK_IDENTITY_OK`, and `NARR_PACKS_CANONICAL_JSON_OK`.)*

---

## **5.2 Hash input**

Canonical bytes of the artifact (per §4), not raw editor formatting.

Normative rule

* Compute sha256 over the artifact’s canonical bytes as defined in §4 (UTF-8, sorted keys, compact, exactly one LF, no BOM). Do not hash whatever an editor wrote if it is non-canonical.

Required procedure (JSON artifacts)

1. Read the file in binary mode.  
2. Parse as JSON and re-serialize with the canonical JSON rules from §4 to obtain canonical\_bytes.  
3. Compare canonical\_bytes to the on-disk bytes. They MUST match exactly.  
   * If they differ (pretty print, CRLF, extra spaces, unsorted keys, missing LF, BOM), fail closed. Do not “fix up” during hashing.  
4. Compute SHA-256 over canonical\_bytes.  
5. Encode the digest as 64 lowercase hex; record it as sha256.  
6. Set size to the byte length of canonical\_bytes.

What not to hash

* Not compressed or transport encodings (no gzip, no br).  
* Not editor or IDE previews with altered line endings or encodings.  
* Not a “normalized-only-for-hashing” variant while leaving a non-canonical file on disk. The file itself must already be canonical.

Arrays-as-sets interaction

* If an array is declared a set (§4), the file must already be deduplicated and ASCII-sorted by identity.  
* Any duplicate-with-different-value or out-of-order identity makes the artifact non-canonical → fail closed.

Locale and environment

* Run under LC\_ALL=C (§4). Do not allow locale or timezone to affect bytes or hashing.

Self-listing

* RESOLVED: the manifest does not self-list. If this policy changes, compute any self-entry after the file is finalized and canonical, then validate it like any other entry (avoid recursion by hashing the canonical bytes as they exist on disk at that moment).

Acceptance hints

* HASH\_INPUT\_CANON\_BYTES\_OK  
* HASH\_SHA256\_HEX64\_OK  
* HASH\_SIZE\_MATCH\_OK  
* HASH\_FILE\_EQ\_CANON\_OK  
* HASH\_ENV\_LC\_ALL\_C\_OK

## **5.3 Validation**

Hex64 lowercase; size matches canonical bytes; every referenced artifact appears exactly once.

Procedure (normative)

1. Schema pass. Validate catalog/manifest.json against its owning schema (top-level object with root, version, built\_at\_utc, and a single files: \[ … \] array of {path, sha256, size}, no additional top-level members or entry fields).  
2. Entry fields. For each files entry:  
   * sha256 matches regex ^\[0-9a-f\]{64}$ (lowercase hex).  
   * size is an integer ≥ 0 (fits in 64-bit signed).  
   * path is a relative POSIX path (no absolute paths, no .., no //).  
3. File presence. Each path resolves to an existing file under the pack root (root="catalog/"). Missing files are errors.  
4. Canonical bytes check. For each path:  
   * Read in binary, parse JSON, re-serialize with §4 canonical rules to obtain canonical\_bytes.  
   * The on-disk bytes MUST equal canonical\_bytes. If not, fail closed (do not “fix up” during hashing).  
5. Digest and length. Recompute SHA-256 over canonical\_bytes; compare to sha256. Recompute byte length; compare to size. Both MUST match.  
6. Uniqueness & order. Treat files as a set keyed by path:  
   * No duplicate path entries.  
   * ASCII-ascending order by path. Any out-of-order pair is an error.  
7. Completeness. The set of entries MUST include every frozen input exactly once. No missing entries. No extraneous entries for non-inputs.  
8. Arrays-as-sets interaction. Where any governed artifact contains arrays treated as sets (§4), that artifact MUST already be deduplicated and ASCII-sorted by identity. Any conflict/out-of-order identity makes the artifact non-canonical → error.  
9. Locale & purity. Perform validation under LC\_ALL=C (§4); no wall clock, randomness, or floats in any step.  
10. Self-listing. Not used. If re-enabled by policy, verify the computed self-entry like any other entry.

CI enforcement (minimum checks)

* MANIFEST\_TOP\_LEVEL\_OBJECT\_OK  
* MANIFEST\_FILES\_ARRAY\_OK  
* MANIFEST\_ENTRY\_FIELDS\_OK  
* MANIFEST\_SHA256\_HEX64\_OK  
* MANIFEST\_SIZE\_MATCH\_OK  
* MANIFEST\_NO\_DUP\_PATHS\_OK  
* MANIFEST\_PATH\_ASCII\_SORT\_OK  
* MANIFEST\_FILE\_EXISTS\_OK  
* MANIFEST\_FILE\_EQ\_CANON\_OK  
* MANIFEST\_LISTS\_ALL\_INPUTS\_OK  
* MANIFEST\_CANON\_JSON\_OK  
* ENV\_LC\_ALL\_C\_OK  
* PACK\_ROOT\_PINNED\_OK  
* PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK

  # **6\. Freeze-Pack Manifest → release\_id \[Required-Now\]**

## **6.1 Manifest construction**

**Purpose.** Canonical JSON document listing every frozen input (path, sha256, size) with top-level metadata. This file’s canonical bytes are the exact bytes hashed to derive `release_id` and it captures a closed set of frozen inputs for the release.

### **Single home**

* The Freeze-Pack Manifest file is `catalog/manifest.json` — the single source of truth for the input list.  
* Any prior name (for example, `CANON_CHECKSUMS.json`) is deprecated.

### **Top-level shape (normative)**

The manifest is a JSON object with the following properties (no others allowed):

* `root` — string. Pack root, fixed to `"catalog/"`.  
* `version` — string. Semver for the catalog pack (not the app version).  
* `built_at_utc` — string. UTC ISO-8601 timestamp (`YYYY-MM-DDThh:mm:ssZ`).  
* `files` — array of entry objects.

**Self-exclusion.** The root manifest **MUST NOT** list itself (`catalog/manifest.json`). Listing `catalog/narratives/manifest.json` is required (see **Content requirements** and §2.8).

### **Entry objects (see §5.1)**

Exactly:

{"path": "\<string\>", "sha256": "\<lowercase 64-hex\>", "size": \<non-negative integer\>}

* `path` values are relative to the pack root (`root == "catalog/"`). Do not include the `"catalog/"` prefix.  
* **Path constraints:** repo-relative POSIX; no `..`, no `//`; maximum 256 bytes. Case-sensitive. (Default path charset guidance `^[a-z0-9_./-]+$`.)

### **Arrays-as-sets policy**

`files` is treated as a set keyed by `path`. Apply §4 arrays-as-sets rules: dedupe by identity (`path`), ASCII-sort by `path`, fail closed on conflicts.

### **Canonical bytes**

Apply §4 canonical JSON rules to the entire file: UTF-8 (no BOM); sorted keys (ASCII) for every object; compact separators; exactly one trailing LF.

### **Content requirements**

* Include every catalog/artifact consumed as a frozen input in this document’s scope (for example: `centers.json`, `gates.json`, `channels.json`, `presets.json`, `magic10.json`, `magic10_seeds.json` when present, and other denominators where applicable).  
* Include narratives pack members under `catalog/narratives/*` (`keys.json`, `templates.json`, optional `palettes.json`, `suppression_map.json`) and the narratives pack manifest at `catalog/narratives/manifest.json` (see §2.8).  
* Do not include logs, evidence reports, JSONL mirrors, or other non-inputs.  
* **Narratives completeness check:** the items above must be present exactly once; omission is an error.

**Runtime (titles-only).** Sealed narratives packs are served from **`/narratives/<pack_sha>/…`**. Identity binding is to the canonical bytes of `catalog/narratives/manifest.json` (see **pack\_sha** rule above). Loader/mount behavior is referenced here **by title only**; detailed runtime policy lives outside this document.

### **Ordering & duplicates**

* `files` entries **MUST** be ASCII ascending by `path`.  
* No duplicate `path`. Conflicting duplicates (same `path`, different `sha256/size`) ⇒ error.

### **Example (illustrative only)**

{

  "root": "catalog/",

  "version": "1.0.0",

  "built\_at\_utc": "2025-10-28T00:00:00Z",

  "files": \[

    { "path": "centers.json",

      "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",

      "size": 1234 },

    { "path": "gates.json",

      "sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789",

      "size": 5678 },

    { "path": "narratives/manifest.json",

      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",

      "size": 321 },

    { "path": "narratives/templates.json",

      "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",

      "size": 654 }

  \]

}

### **CI enforcement (minimum)**

`MANIFEST_TOP_LEVEL_OBJECT_OK`, `MANIFEST_FILES_ARRAY_OK`, `MANIFEST_ENTRY_FIELDS_OK`, `MANIFEST_SHA256_HEX64_OK`, `MANIFEST_SIZE_MATCH_OK`, `MANIFEST_PATH_ASCII_SORT_OK`, `MANIFEST_NO_DUP_PATHS_OK`, `MANIFEST_FILE_EXISTS_OK`, `MANIFEST_CANON_JSON_OK`, `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`.

## **6.2 `release_id` computation**

`release_id = sha256(canonical_manifest_bytes)` where the digest is **lowercase 64-hex**.

### **Normative rule**

* Compute `release_id` by hashing the **canonical bytes** of the Freeze-Pack Manifest defined in §6.1.  
* Canonical bytes follow §4: UTF-8, **sorted keys (ASCII)**, compact, **exactly one** LF, no BOM.  
* Output is a **64-character lowercase hex** SHA-256 string. No prefixes, no uppercase.

### **Procedure**

1. Read the finalized manifest **in binary**.  
2. Parse JSON and **re-serialize** using §4 rules to obtain `canonical_manifest_bytes`.  
3. **Verify** on-disk bytes equal `canonical_manifest_bytes`. If not, **fail closed**.  
4. Compute **SHA-256** over `canonical_manifest_bytes`.  
5. Encode as **64 lowercase hex**; record as `release_id`.

### **Determinism pins**

* Run with `LC_ALL=C`, `LANG=C`, `TZ=UTC` (§4).  
* **No** wall clock, **no** randomness, **no** floats.  
* **Two runs** over identical inputs **MUST** produce identical `release_id`.

### **Validation**

* To validate a claimed `release_id`, recompute from the on-disk manifest as above and compare for **exact equality**.  
* If the manifest is **non-canonical**, do not compute. Treat as an error until canonicalization is fixed.

### **Acceptance hints (titles only; tokens live in HDE-Governance §2.0)**

`RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`,  
 `JSON_CANONICAL_CHECK_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`.

## **6.3 Change ⇒ new `release_id`**

Any **byte change** to a **frozen input** or to the **manifest** produces a **new `release_id`**.

### **Scope**

* “Frozen input” means any file **listed** in the Freeze-Pack Manifest (§6.1).  
* “Manifest structure” means the set of entries and their canonical JSON form in `catalog/manifest.json`.

### **Normative rules**

* If any listed artifact’s **canonical bytes** change, the entry (`sha256`, `size`) changes ⇒ manifest bytes change ⇒ **new `release_id`**.  
* If the manifest’s entries set changes in **any** way, manifest bytes change ⇒ **new `release_id`**:  
  * Adding/removing an entry.  
  * Renaming a path.  
  * Introducing or resolving a duplicate path.  
  * Reordering so `files` is **not ASCII-ascending** by `path`.  
  * Changing any field value (`path`, `sha256`, `size`).  
* If an artifact violates canonical rules and is then **corrected** to canonical, the artifact bytes change ⇒ **new `release_id`**.  
* **Non-canonical** manifest: do **not** compute (see §6.2 **Validation**). Fix canonicalization first; then compute.

### **Examples that produce a new `release_id`**

* Edit to `catalog/gates.json` that changes any value.  
* Fixing key order or line endings in `catalog/centers.json` to meet §4.  
* Adding `catalog/presets.json` to the pack.  
* Adding `catalog/magic10_seeds.json` to the pack (when introduced).  
* Adding `catalog/narratives/manifest.json` to the pack.  
* Adding any `catalog/narratives/*` member (`keys/templates/palettes/suppression_map`) to the pack.  
* Renaming a path in the manifest.  
* Correcting an out-of-order `files` array to ASCII order.

### **Examples that do not produce a new `release_id`**

* Editor settings that do **not** alter canonical bytes.  
* Changes to logs, evidence reports, JSONL mirrors, or files **not listed** in the manifest.  
* Runtime or transport settings outside the pack (for example, gzip delivery).

### **CI enforcement**

* Recompute `release_id` from the finalized manifest and compare to the recorded value.  
* **Fail** the build if any listed artifact’s recomputed `sha256` or `size` differs from the manifest.  
* **Fail** the build if the manifest is **not canonical JSON** or **not ASCII-sorted** by `path`.

### **Acceptance hints (titles only; tokens live in HDE-Governance §2.0)**

`RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`,  
 `MANIFEST_PATH_ASCII_SORT_OK`, `MANIFEST_NO_DUP_PATHS_OK`, `MANIFEST_FILE_EXISTS_OK`,  
 `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`.

## **6.4 Evidence and CI hooks**

**Purpose.** Prove the manifest is **canonical**, that each entry’s digest and size match the artifact’s **canonical bytes**, and that the `release_id` equals the SHA-256 of the **canonical** manifest bytes.

### **Required artifacts**

* **Recompute script** — reads the finalized manifest, verifies canonical form, recomputes `release_id`, exits non-zero on any mismatch.  
  * path: `scripts/release_id_recompute.py`  
  * recompute log (evidence): `artifacts/math/release_id_recompute.log`  
* **Checksum verification report** — per-entry results for `path`, recomputed `sha256`, `size`, and any failures.  
  * path: `artifacts/math/checksums_audit.log`  
* **Manifest snapshot** — small JSON with `release_id`, manifest file path, manifest `sha256`, entry count, CI timestamp. Evidence only, not an input.  
  * path: `artifacts/math/manifest_snapshot.json`  
* **Environment pins** — text file recording `LC_ALL=C`, `LANG=C`, `TZ=UTC` used during checks.  
  * path: `artifacts/proofs/env_pins.txt`

### **Normative behavior**

1. **Recompute `release_id`.**

   * Read `catalog/manifest.json` in binary; parse; re-serialize with §4 rules to canonical bytes; **verify on-disk file equals canonical**.  
   * Compute SHA-256 over canonical bytes; compare to the recorded `release_id` (**must match**).  
   * Assert manifest is UTF-8 (no BOM), **sorted keys**, compact, **exactly one LF**; `files[]` is ASCII-sorted by `path`, has **no duplicates**, and **does not** list the manifest itself.  
2. **Verify checksums.**

   * For each entry `{path, sha256, size}`: open the file; compute canonical bytes; verify on-disk equals canonical; recompute `sha256` and `size`; both **must match** the manifest.  
   * **Fail** if any entry path is not repo-relative POSIX or any hash is not lowercase 64-hex.  
3. **Completeness.**

   * The manifest lists **every frozen input exactly once** (closed sets, denominators, catalogs, constants, thresholds, seeds if catalogized). **No extras** for non-inputs.  
   * **Narratives completeness:** `catalog/narratives/manifest.json` **and** the four `catalog/narratives/*` members **must** be present **exactly once** (see §2.8).  
4. **Locale and determinism.**

   * Run under `LC_ALL=C`, `LANG=C`, `TZ=UTC` with **no** wall-clock dependence, **no** randomness, and **no** floating-point nondeterminism (§4).  
   * Prove **two-run identity** of the recompute step (same inputs → identical outputs).

### **CI hooks (minimum)**

* **Pre-merge job** runs the recompute script and checksum verification; any failure is a **hard stop**.  
* **Manifest-change gate** requires updating, in the **same commit/PR**:  
  * the **human Evidence Index**: `docs/evidence/INDEX.json`,  
  * the **Evidence Index hash sentinel**: `docs/evidence/INDEX.sha256`, and  
  * the **machine mirror**: `artifacts/evidence_index.jsonl`.  
* **Two-run identity job** ensures stable bytes across two executions on the same inputs.  
* **Sentinel check:** CI fails if `docs/evidence/INDEX.sha256` does **not** match the current `INDEX.json` bytes.

### **Evidence Index entries (titles and paths only)**

* Freeze-Pack Manifest (bytes copied for evidence) — `artifacts/math/freeze_pack_manifest.json`  
* Recompute `release_id` script — `scripts/release_id_recompute.py`  
* Recompute `release_id` log — `artifacts/math/release_id_recompute.log`  
* Checksum verification report — `artifacts/math/checksums_audit.log`  
* Manifest snapshot (release\_id, manifest sha256, count) — `artifacts/math/manifest_snapshot.json`  
* Environment pins (LC\_ALL, LANG, TZ) — `artifacts/proofs/env_pins.txt`  
* Evidence Index hash sentinel — `docs/evidence/INDEX.sha256`

### **Acceptance hints (titles only; token names live in HDE-Governance §2.0)**

`RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`,  
 `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `TWO_RUN_IDENTITY_OK`.

#  **7\. Interfaces to Other Specs (titles-only) \[Required-Now\]**

This document routes by **title only**. Do not restate or duplicate content from other specs. Do not include version numbers in prose.

## **7.1 Math (by title)**

**Reference**: **PF-Canon-HDE-Math-Spec**

**Defers to Math for**

* Scoring and thresholds  
* Deterministic preimage and idempotence recipe  
* Any arithmetic, weighting, tie-break, or precedence logic

  ## **7.2 Governance/CLI (by title)**

**References**: **PF-Canon-HDE-Governance**; **PF-Canon-HDE-CLI-API-Vendor-Ref**

**Defers to Governance/CLI for**

* Public success and error shapes  
* Headers and conditional delivery behavior  
* Vendor request shaping and typed field mapping

  ## **7.3 Architecture (by title)**

**Reference**: **PF-Canon-HDE-Architecture**

**Defers to Architecture for**

* System boundaries and single-homes  
* Contract-free overview of components and responsibility lines  
* CI & Evidence \[Required-Now\]

  # **8\. CI & Evidence \[Required-Now\]**

## **8.1 Catalog schema CI**

 Jobs to validate all catalogs against their schemas. Fail on unknown keys or IDs. These jobs enforce §§3–6; they do not redefine rules.

**Purpose**  
 Prove that every catalog conforms to its owning JSON Schema and that all referenced IDs belong to closed domains.

**Scope**  
 Catalogs from §2: Centers, Gates, Channels, Presets, Magic-10 (`catalog/magic10.json`), Magic-10 seeds (`catalog/magic10_seeds.json`), Authorities \[OPEN\], Profiles \[OPEN\].  
 Validation rules from §3.1 (schema), §3.2 (topology), §3.3 (domain closure), and serialization pins from §4.

**Inputs**  
 Catalog file list from §2 with titles and paths only. Paths that are not yet confirmed remain \[OPEN\] and must be wired before CI runs.

**Normative jobs**

* **catalog\_schema\_validate**  
  * Validate each catalog against its owning JSON Schema.  
  * Reject additional properties unless the schema allows them at that object level.  
  * Reject missing required fields and wrong types.  
  * Arrays declared as sets must declare identity rules or be flagged \[OPEN\] to fix in schema.  
* **catalog\_domain\_closure**  
  * Build owner sets for each closed domain.  
  * Check all references for membership in the owner set.  
  * Fail on any unknown ID or enum value. No coercion. No aliases in v1.  
* **catalog\_topology\_coherence**  
  * Apply graph checks from §3.2 across Centers, Gates, Channels.  
  * Channel has exactly two distinct gate IDs.  
  * Gate references exactly one valid center.  
  * Channel center derivation matches any stored center fields.  
  * No orphaned references.  
* **catalog\_arrays\_as\_sets**  
  * For arrays that function as sets, verify deduplication by identity, no conflicts on identical identities, and ASCII ascending order by identity, per §4.2.  
* **catalog\_canonical\_json**  
  * Verify each catalog is already in canonical JSON form per §4.  
  * Check UTF-8, sorted keys, compact separators, exactly one trailing LF, no BOM.  
  * Do not auto-rewrite. Treat non-canonical bytes as an error.

**Failure policy**  
 Any schema error, unknown key, unknown ID, orphan, set-order violation, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

**Artifacts (titles and paths only)**

* Catalog Schema Validation Report — `artifacts/catalog/catalog_schema_validation.log`  
* Domain Closure Report — `artifacts/catalog/domain_closure_report.log`  
* Topology Coherence Report — `artifacts/topology/topology_coherence_report.log`  
* Canonical JSON Check Report — `audit/gates/canonical_json/json_canonical_check.log`

**Indexing**  
 Add the above to Appendix D (human) and append records to `artifacts/evidence_index.jsonl` (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a `proof_anchor` to a path-proof stored alongside the artifact).

**Environment and determinism**  
 Run with `LC_ALL=C, LANG=C, TZ=UTC` per §4.3.  
 No wall clock, no randomness, no floats.

**Acceptance hints (names-only)**  
 `UMS_AJV_PASS`, `CATALOG_SCHEMA_OK`, `CATALOG_NO_ADDITIONAL_PROPS_OK`, `CATALOG_NO_UNKNOWN_KEYS_OK`, `CATALOG_DOMAIN_CLOSED_OK`, `CATALOG_TOPOLOGY_OK`, `ARR_SET_IDENTITY_DECLARED_OK`, `ARR_SET_NO_DUPLICATES_OK`, `ARR_SET_ASCII_SORT_OK`, `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`.

---

## **8.2 Integrity CI**  Degree-vector and orphan checks. Arrays-as-sets enforcement. Canonicalization compare.

**Purpose**  
 Assert pack-level integrity beyond schema shape: graph soundness, set semantics, and byte determinism.

**Scope**  
 Applies to all catalogs in §2 that participate in topology or set semantics (Centers, Gates, Channels, Presets, Magic-10, Magic-10 seeds, Authorities \[OPEN\], Profiles \[OPEN\]).  
 Uses rules from §3.2 (topology), §3.3 (domain closure), §4 (canonical JSON and arrays-as-sets).

**Normative jobs**

* **integrity\_topology**  
  * Orphans. Every referenced ID exists (gate→center, channel→gates). Zero dangling references.  
  * Channel degree. Each channel references exactly two distinct gate IDs.  
  * Gate↔center consistency. Each gate references exactly one valid center; any stored center fields on channels must match the set derived from member gates.  
  * Degree vectors (optional). If catalogs declare expected degree counts (for centers or gates), compute observed degrees from the graph and assert equality. If undeclared, skip with PASS; if declared, mismatches are errors. (Confirm degree-vector home in §3; leave \[OPEN\] only if not declared in schemas.)  
* **integrity\_arrays\_as\_sets**  
  * For arrays designated as sets in their schemas, enforce §4.2:  
    * Identity declared & computable (\[OPEN\] where missing in schema).  
    * No duplicate identities with different element values (conflict).  
    * After deduplication, ASCII ascending order by identity.  
  * Fail closed on any conflict or ordering violation.  
* **integrity\_canonicalization\_compare**  
  * For each catalog: parse JSON, re-serialize with §4 canonical rules, and compare bytes to the on-disk file.  
  * Files must already be canonical (UTF-8, sorted keys, compact, one LF, no BOM).  
  * Do not auto-rewrite. Any difference is an error.

**Failure policy**  
 Any orphan, degree violation, set conflict, out-of-order identity, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

**Artifacts (titles and paths only)**

* Topology Integrity Report — `artifacts/topology/topology_coherence_report.log`  
* Arrays-as-Sets Report — `artifacts/canonical/arrays_as_sets_report.log`  
* Canonicalization Compare Report — `audit/gates/canonical_json/json_canon_compare.log`

**Indexing**  
 Add these to Appendix D (human) and append records to `artifacts/evidence_index.jsonl` (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a `proof_anchor` to a path-proof stored alongside the artifact).

**Environment and determinism**  
 Run with `LC_ALL=C, LANG=C, TZ=UTC` per §4.3.  
 No wall clock, no randomness, no floats.

**Acceptance hints (names-only)**  
 `TOPOLOGY_NO_ORPHANS_OK`, `TOPOLOGY_CHANNEL_DEGREE_2_OK`, `TOPOLOGY_GATE_CENTER_OK`, `DEGREE_VECTORS_MATCH_OK` (when declared), `ARR_SET_IDENTITY_DECLARED_OK`, `ARR_SET_NO_CONFLICTS_OK`, `ARR_SET_ASCII_SORT_OK`, `FILE_EQ_CANON_BYTES_OK`, `ENV_LC_ALL_C_OK`.

## ---

## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**

**Single home and path**

* **Path (fixed).** `artifacts/evidence_index.jsonl` (there must be exactly one mirror file in the repo).

* **Governed locations only.** Every evidence file referenced by the mirror MUST live under governed repo paths (for example, `artifacts/**`, `docs/**`). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI.

* **Tracked files (no `.gitignore` for governed artifacts).** Governed evidence artifacts and their `artifacts/path_proofs/...` files MUST NOT be ignored by `.gitignore`. Governed locations are expected to be tracked; using `.gitignore` to hide governed artifacts or path-proofs is invalid and should be treated as a QA failure.

**Format (canonical JSONL)**

* One JSON object per line.

* Canonical JSON per §4 for each line:

  * UTF-8 (no BOM).

  * Sorted keys.

  * Compact separators.

  * Exactly one trailing `\n` per line.

  * No blank lines; no trailing spaces.

* Unknown keys are rejected (CI-blocking).

**Minimum record schema (reject unknown keys)**

Each line in the mirror uses at least the following schema; unknown keys are rejected:

{  
 "artifact\_key": "",  
 "role": "\<proof|golden|snapshot|script|log\>",  
 "sha256": "\<lowercase 64-hex\>",  
 "size\_bytes": ,  
 "produced\_at\_utc": "",  
 "discovered\_physical\_path": "",  
 "proof\_anchor": ""  
 }

**Field order and write discipline (merge-blocking)**

* ASCII field order (exact):

   `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

* Sort-before-write by the tuple `(artifact_key, discovered_physical_path)`.

* Uniqueness: the pair `(artifact_key, discovered_physical_path)` is unique; duplicates fail CI.

* Single mirror file: only one `artifacts/evidence_index.jsonl` may exist in the repo.

**Produced\_at\_utc vs mtime\_utc**

* `produced_at_utc` records when the evidence was **logically produced** (the event time). It is part of the mirror record and is used to reason about when posture snapshots and QA runs occurred.

* `mtime_utc` is recorded in the per-artifact path-proof (`artifacts/path_proofs/...`) as the filesystem modification time for the artifact.

* Differences between `produced_at_utc` and `mtime_utc` are allowed but must be truthful — no “backdating” or forward-dating to distort ordering. QA may rely on `produced_at_utc` as the primary ordering key for evidence; disagreements should be rare and explainable in the PR.

**Acceptance hints (titles-only; tokens live in HDE-Governance §2.0)**

Names-only list of tokens that gate the mirror and its parity with the human index:

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `JSON_CANONICAL_CHECK_OK`

* `EVIDENCE_PATH_PROOFS_OK`

**Join to the human index (parity, proofs, same-PR rule)**

* **1:1 parity.** Every §8.6 Evidence Index entry has exactly one mirror record, and every mirror record has a corresponding human entry:

  * `artifact_key` equals the Human Index title.

  * `discovered_physical_path` equals the Human Index path.

* **Path-proofs.** Each artifact’s directory contains a stored path-proof (for example, `path_proof.txt` with a stat transcript). The mirror record’s `proof_anchor` must exactly match the stored path-proof for that artifact.

* **Same-PR rule.** For every governed artifact in §8.6, any change to the artifact **MUST** update, in the same PR:

  * The artifact bytes on disk under a governed path.

  * Its `artifacts/path_proofs/...` path-proof file (`proof_anchor` target).

  * The corresponding machine mirror record in `artifacts/evidence_index.jsonl`.

  * The Human Evidence Index entry in `docs/evidence/INDEX.json` and its hash sentinel `docs/evidence/INDEX.sha256`.

* Mirror or index entries that refer to non-existent artifacts or stale path-proofs are invalid and must be corrected, not ignored.

**Determinism**

* All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* JSONL records are canonical and LF-terminated (exactly one `\n` per record).

**Header snapshots in artifacts (normative)**

* For artifacts that capture headers, header names MUST be lower-case and values MUST be verbatim; exact checks apply to values.

* Wire casing may differ and is validated by transport owners.

* Acceptance hint (names-only): `SNAPSHOT_HEADER_LOWERCASE_OK`.

**Refusal proofs (policy note)**

* Refusal proofs are error/ops evidence (not JSON success). They must:

  * Not set `ETag`, `Vary`, or compression headers.

  * Use `Content-Type: application/json; charset=utf-8`.

* The refusal log allow-list for JSON body fields is exactly:

   `{at, route, status, duration_ms, idempotence_hash, release_id}`

* Records with any additional fields fail policy checks.

* Rate-limit (429) evidence uses a different allow-list and is governed by HDE-Governance. Do not mix refusal and 429 fields in the mirror.

**Role usage notes (non-normative examples)**

* `proof` → `artifacts/db/ddl_fingerprint.json`, `artifacts/proofs/endpoints_env_gate_proof.log`, `artifacts/bodygraph/source_invariance/ab.json`, `/ba.json`, `/summary.json`

* `golden` → `catalog/manifest.json`, `catalog/schemas/*.json`

* `snapshot` → `artifacts/runtime/env_matrix.snapshot.json`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/bodygraph/refresh_policy.snapshot.json`, `artifacts/bodygraph/metrics.snapshot.json`

* `script` → `scripts/card_close.sh`, `scripts/migration_runner.sh`

* `log` → `artifacts/db/migration_runner.log`, `artifacts/proofs/headers_probe.log`, `artifacts/bodygraph/keys_only.logs.sample` (sanitized; keys-only, no PII per Governance)

### **8.3.1 Refusal proof (single-file canonical) \[Required-Now\]**

**Path (fixed)**

* `artifacts/proofs/ops_refusal_proof.txt` — single-file refusal:

  * Header block.

  * One blank line.

  * LF-terminated JSON body.

* Index this file in both `docs/evidence/INDEX.json` (human) and `artifacts/evidence_index.jsonl` (machine) in the same PR.

* Include a co-located `path_proof.txt` and reference it via `proof_anchor` in the mirror.

* Policy and tokens live in HDE-Governance (titles only).

**Purpose**

* Capture a refusal response verbatim (headers \+ JSON body) for ops/evidence.

* This is not a JSON success route.

**File format (exact)**

* The file consists of:

  * A header block.

  * Exactly one blank line.

  * A JSON body.

* The file ends with exactly one `\n`.

**Header block**

* One header per line, format: `<lowercase-name>: <value>`.

* Required header:

   `content-type: application/json; charset=utf-8`

* Forbidden headers: `etag`, `vary`, `content-encoding`.

* Other headers may appear as governed elsewhere (for example, `date`).

* Header names are lower-case; values are verbatim. Order is preserved as captured.

**Separator**

* Exactly one blank line (a single `\n`) between headers and body.

**Body (JSON, single line)**

* Canonical JSON per §4:

  * UTF-8.

  * Sorted keys.

  * Compact separators.

  * One trailing `\n`.

* Fields must conform to the refusal allow-list:

   `{at, route, status, duration_ms, idempotence_hash, release_id}`

* Unknown keys fail policy checks.

**Mirror linkage**

* The mirror record uses `role:"log"` and must point to this file via `discovered_physical_path`.

* The artifact directory also contains a `path_proof.txt` stat transcript; the mirror `proof_anchor` must exactly match that path-proof entry.

**Validation checks (CI)**

* File ends with exactly one `\n`.

* Headers lower-case; required header present; forbidden headers absent.

* Exactly one blank line between headers and body.

* Body is single-line canonical JSON with the refusal allow-list only.

* Determinism: checks run with `LC_ALL=C`, `TZ=UTC`.

**Example (illustrative)**

content-type: application/json; charset=utf-8  
 date: 2025-11-07T21:00:00Z

{"at":"2025-11-07T21:00:00Z","route":"/ops/rails/refusal","status":503,"duration\_ms":12,"idempotence\_hash":"\<64-hex\>","release\_id":"\<64-hex\>"}

**Acceptance hints (titles-only; tokens live in HDE-Governance)**

* `OPS_REFUSAL_FILE_FORMAT_OK`

* `OPS_REFUSAL_HEADERS_OK`

* `OPS_REFUSAL_BODY_OK`

* `OPS_REFUSAL_MIRROR_LINK_OK`

### **8.3.2 Environment matrix snapshot (singleton, v3) \[Required-Now\]**

**Path (fixed)**

* `artifacts/runtime/env_matrix.snapshot.json` — one file per repo (singleton).

**Purpose**

* Record the default rails posture and determinism pins across environments, as captured by the build/test harness.

* HDE-Governance owns policy and tokens; Glow-Infrastructure lists names-only env inventory; PF12 owns this artifact’s schema and indexing.

**Schema (v3; reject unknown keys)**

* Canonical JSON per §4 (UTF-8; sorted keys; compact; exactly one LF).

Minimum fields:

{  
 "schema\_version": 3,  
 "default\_rails": {  
 "dev": {"SAFE\_MODE": 0, "ALLOW\_NETWORK": 1},  
 "stage": {"SAFE\_MODE": 0, "ALLOW\_NETWORK": 1},  
 "prod": {"SAFE\_MODE": 1, "ALLOW\_NETWORK": 0},  
 "CI": {"SAFE\_MODE": 1, "ALLOW\_NETWORK": 0}  
 },  
 "determinism\_pins": {"LC\_ALL": "C", "LANG": "C", "TZ": "UTC"},  
 "presence": {  
 "DATABASE\_URL": {"present": true},  
 "DB\_BRIDGE\_URL": {"present": false},  
 "db\_allow\_bridge\_in\_prod": {"present": false}  
 },  
 "notes": \[\]  
 }

**Field rules**

* Uppercase rails keys (`SAFE_MODE`, `ALLOW_NETWORK`) and env names as shown.

* `schema_version` MUST equal `3`.

* `presence.*.present` are booleans indicating whether the variable (or prod guard) is set at capture time; do not record secrets or values.

* `notes` is optional (short strings; no secrets).

**Indexing (both indices; same PR)**

* Add a titles/paths entry in §8.6 and a mirror record (`role:"snapshot"`) in `artifacts/evidence_index.jsonl` with `proof_anchor` to a co-located `path_proof.txt` (stat transcript).

* Mirror schema and “single mirror file” rule are per §8.3.

**Acceptance hints (names-only; tokens live in HDE-Governance)**

* `ENV_RAILS_POLICY_OK`

* `ENV_LC_ALL_C_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `CI_CHECK_FINAL_LF_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

**Routing (titles-only)**

* Policy and refusal semantics → HDE-Governance.

* Env inventory → Glow-Infrastructure.

## **8.4 Human Evidence Index (titles/paths only)**

**Single home and format**

* Path: `docs/evidence/INDEX.json`.

* Canonical JSON per §4 (titles/paths only; no payload bytes).

* Used for human review; must maintain 1:1 parity with the machine JSONL mirror in §8.3.

**Update rule**

* When an artifact is added, moved, or removed, update in the same PR/commit:

  * `docs/evidence/INDEX.json` (Human Index).

  * `docs/evidence/INDEX.sha256` (hash sentinel).

  * `artifacts/evidence_index.jsonl` (machine mirror).

* Parity rules and same-PR discipline are defined in §8.3.

**Acceptance hints (titles-only; tokens live in HDE-Governance)**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

## **8.5 Registry report (records-only)**

**Purpose and format**

* Names-only, records-only indicator that the configuration registry was generated for this cut; no secrets or payload values.

* Canonical JSON object (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Intended for automated consumption (for example, CI, auditors), not for human-readable narrative.

**Path (single home)**

* `artifacts/registry/registry_report.json` (fixed).

**Content (minimum shape; reject unknown keys)**

* `generated_at_utc` — ISO-8601 UTC timestamp of the registry build.

* `inputs` — names-only list of upstream sources consulted (for example, `["env:LC_ALL","env:LANG","env:TZ","catalog/*.json","…"]`).

* `artifacts` — names-only list of emitted registry artifacts (titles only, for example, `"artifacts/registry/registry_report.json"`).

* `notes` — optional short array of strings (free text; no secrets).

* This artifact is not a substitute for the Human Evidence Index; it is a machine-oriented summary.

**Indexing (titles/paths only)**

* **Machine mirror.** Append a records-only entry to `artifacts/evidence_index.jsonl` in the same PR:

  * `artifact_key` (title),

  * `role:"snapshot"`,

  * `discovered_physical_path`,

  * `sha256`,

  * `size_bytes`,

  * `produced_at_utc`,

  * `proof_anchor` (path to `path_proof.txt` stored alongside the file).

* **Human index (optional).** Add a titles/paths-only entry in §8.6 (no payload bytes).

* Mirror records must follow §8.3 (canonical JSONL; one LF; sorted keys; unknown-key rejection; path-proof; single mirror file).

**Acceptance hints (titles-only; tokens live in HDE-Governance §2.0)**

* `REGISTRY_REPORT_OK` (registry report present, canonical, and indexed).

* `EVIDENCE_INDEX_UPDATED_OK` (human/machine parity in the same PR).

* `EVIDENCE_PATHS_VALIDATED_OK` (mirror record has `proof_anchor` for on-disk path-proof).

## **8.6 Evidence Index entries (titles/paths only) \[Required-Now\]**

**Discipline**

* Update both the Human Index (`docs/evidence/INDEX.json`) and the machine mirror (`artifacts/evidence_index.jsonl`) in the same PR.

* Records-only; canonical JSONL; one LF; unknown-key rejection; ASCII field order; sort-before-write; single mirror file; `proof_anchor` present.

* Process is defined in Epic-Process-Guide; acceptance sentinel gating per PF12 front-matter.

**Parity rule (MUST)**

Update all of the following in the same PR:

* `docs/evidence/INDEX.json` (Human Index).

* `docs/evidence/INDEX.sha256` (hash sentinel).

* `artifacts/evidence_index.jsonl` (machine mirror).

Assert the mirror/index tokens named in §8.3 on every change.

**Entries (authoritative list; titles/paths only)**

*Freeze-pack and math*

* `artifacts/math/freeze_pack_manifest.json`

* `artifacts/math/release_id.txt`

* `artifacts/math/release_id_recompute.log`

* `artifacts/math/checksums_audit.log`

* `artifacts/math/manifest_snapshot.json`

*Canonical JSON and topology*

* `artifacts/canonical/arrays_as_sets_report.log`

* `audit/gates/canonical_json/json_canon_compare.log`

* `artifacts/topology/topology_coherence.log`

*Endpoint Catalog and A7 proofs*

* `artifacts/reader/endpoints_snapshot.json`

* `artifacts/proofs/endpoints_env_gate_proof.log`

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_writers_errors.txt`

* `artifacts/proofs/encoding_invariance.txt` (optional)

* `artifacts/proofs/reader_success_get_head_304.json` (composite proof; schema in §8.12)

*Aux Narrative (text) — header snapshots*

* `tests/transport/headers/aux_text_200.snap`

* `tests/transport/headers/aux_suppression_200.snap`

*CLI Admin Preview (narrative) — evidence*

* `artifacts/cli/narrative/stdout.txt` (LF-terminated narrative text; no ANSI)

* `artifacts/cli/narrative/sidecar.json` (ids-only: `composition_id`, `fragment_ids[]`, `pack_sha`, optional `release_id`; canonical JSON)

*Narratives coverage (router)*

* `audit/gates/narratives/keys_10x4.table.json`

*Rails proofs (ops)*

* `artifacts/proofs/ops_refusal_proof.txt` — single-file refusal (headers → blank line → LF-terminated JSON). (Record type: `ops_refusal_proof`; policy/tokens by title in Governance.)

* `ci/jobs/logs_keys_only_redaction.yml`

* `ci/jobs/rails_open_conformance.yml`

*DB posture and runtime*

* `artifacts/db/ddl_fingerprint.json`

* `artifacts/db/grants.txt`

* `artifacts/db/check_schema.txt`

* `artifacts/db/check_constraints.txt`

* `artifacts/db/partition_plan.txt`

* `artifacts/db/db_rw_smoke.log` (optional)

*Runtime / env*

* `artifacts/runtime/env_matrix.snapshot.json` — singleton snapshot (`schema_version` 3); default rails and determinism pins; presence booleans for DB/bridge/guard. (Schema in §8.3.2; tokens by title in Governance.)

* `artifacts/runtime/env_connectivity.snapshot.json` — dev resolver snapshot (records attempts and selected source on fallback).

*Ops / refusal (closed-rails)*

* `artifacts/proofs/ops_refusal_proof.txt` — single-file refusal (headers → blank line → LF-terminated JSON). (Policy and tokens by title in Governance.)

*Internal-ops surface*

* `/internal/version` headers/body proofs (titles/paths per HDE-Governance appendix for internal ops).

*CLI parity and determinism*

* `artifacts/cli/showcompat/stdout.json`

* `artifacts/cli/showcompat/two_run_identity.log`

* `artifacts/cli/showcompat/abba.diff`

* `artifacts/cli/showcompat/reader_cli_parity.diff`

*SBOM*

* `sbom/cyclonedx.json`

* `sbom/cyclonedx.json.sha256`

*Registry/reporting*

* `artifacts/registry/registry_report.json`

*BodyGraph adapter data-source and invariance*

* `artifacts/bodygraph/source_selection.snapshot.json`

* `artifacts/bodygraph/source_invariance/ab.json`

* `artifacts/bodygraph/source_invariance/ba.json`

* `artifacts/bodygraph/source_invariance/summary.json`

* `artifacts/bodygraph/release_bindings.json`

* `artifacts/bodygraph/refresh_policy.snapshot.json`

* `artifacts/bodygraph/metrics.snapshot.json`

* `artifacts/bodygraph/keys_only.logs.sample`

*Lifecycle (backup/restore/retention) — OPS-managed captures*

* `artifacts/db/backup_manifest.json`

* `artifacts/db/restore_verify.log`

* `artifacts/db/retention_run.log`

*Admin QA and runbooks*

* `docs/run/PROD_ENDPOINTS.json`

* `docs/run/RUN_PROD_QA.md`

* `docs/run/EPIC011_TEST_IDENTITIES.md`

* `artifacts/ops/admin_vendor_calls.jsonl`

Human Index entries are titles/paths only; mirror records include `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor`.

**Discipline reminder**

* Every entry above must have exactly one Human Index entry and one mirror record.

* Mirrors must follow §8.3 (canonical JSONL, single file, sorted, LF-terminated, unknown-key reject, `proof_anchor` to a stored `path_proof.txt`).

**Acceptance impact**

* None new; this section remains a names-only catalog.

* Enforcement is via existing mirror/index tokens (`EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, etc.).

## **8.7 DB fingerprint & smoke artifacts \[Required-Now\]**

**Purpose.** Capture database posture and minimal activity proofs as records-only governed evidence for EPIC-011 and future epics.

**Artifacts (titles and paths only)**

* **DB fingerprint — normalized DDL \+ sha256.**  
   `artifacts/db/ddl_fingerprint.json`

* **Roles/grants snapshot.**  
   `artifacts/db/grants.txt`

* **Schema/search\_path echo.**  
   `artifacts/db/check_schema.txt`

* **Constraints check.**  
   `artifacts/db/check_constraints.txt`

* **Partition plan (summary).**  
   `artifacts/db/partition_plan.txt`

* **RW smoke (optional).**  
   `artifacts/db/db_rw_smoke.log`

* **Connection env selection (dev-only snapshot).**  
   `artifacts/runtime/env_connectivity.snapshot.json`

* **Env posture (names-only).**  
   `artifacts/runtime/env_matrix.snapshot.json`

**Indexing.**  
 List each artifact in `docs/evidence/INDEX.json` and update `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl` in the same PR, with a matching `*.path_proof.txt` for every governed artifact. The machine mirror is canonical JSONL (UTF-8; sorted keys; compact; one LF per record), enforces unknown-key rejection, and is sorted by `(artifact_key, discovered_physical_path)`. See §8.3 for mirror schema, sort order, and path-proof rules.

### **Primary key posture (current EPIC-011 reality)**

The canonical fingerprint schema for EPIC-011 includes a `primary_key` array and `constraints` list for each table. In the current captured posture for `hde.body_graphs`, both `primary_key` and `constraints` are empty; this accurately reflects the production database at the time of capture (no primary key is defined on `hde.body_graphs`).

For EPIC-011, tokens such as `DB_SCHEMA_FINGERPRINT_OK` and `DB_ROLE_OK` are defined as “posture is captured and indexed as-is,” so this no-PK state is sufficient for those tokens once fingerprint, grants, mirror, and path-proofs are in sync. The missing PK on `hde.body_graphs` is recorded technical debt: a future DB/infra migration epic must introduce and enforce an appropriate primary key on `(user_id, vendor, vendor_version, input_fingerprint)`, re-capture `ddl_fingerprint.json` and `grants.txt`, and update PF12 and PF10 accordingly. Until that epic lands, PF12’s role is to document the current posture truthfully, not to prescribe the eventual PK.

**Acceptance (titles-only; tokens live in HDE-Governance).**  
 `DB_SCHEMA_FINGERPRINT_OK`, `DB_ROLE_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_CONN_ENV_OK`, `DEV_DB_BRIDGE_FALLBACK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`. Interpretation of `DB_ROLE_OK` and related posture tokens under EPIC-011 follows the governance rules in HDE-Governance and the BN 7.6.6 drain plan.

---

## 8.8 Reader JSON Success Endpoint Catalog snapshot (records-only)

**Purpose.** Support Governance proofs for success routes (A7) beyond `/internal/version`. A7 proofs run only on cataloged JSON success routes; `/internal/version` is ops-only and excluded. The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod (pair with an env-gate proof artifact).

**Path.** `artifacts/reader/endpoints_snapshot.json` (fixed).

**Content (titles only).** Canonical JSON snapshot that lists success endpoints by title and the names of response envelope keys. No URLs, no example payloads, no bytes beyond names.

**Format.** Records-only, canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF). An empty `endpoints` array is allowed until a route ships.

**Suggested minimal schema (example)**

{

  "generated\_at\_utc": "YYYY-MM-DDThh:mm:ssZ",

  "endpoints": \["\<title-1\>", "\<title-2\>"\],

  "envelope\_keys": \["reader\_version","eligible","categories","meta","release\_id","idempotence\_hash"\]

}

**Related governed files (titles only).** The authoritative Catalog file lives at `docs/ENDPOINTS_CATALOG.json` with checksum sidecar `docs/ENDPOINTS_CATALOG.json.sha256` and **MUST** be indexed like other records-only artifacts (see §8.6, Appendix C).

**Indexing.**  
 Human Index: add a titles/paths-only entry in `docs/evidence/INDEX.json` and update the hash sentinel `docs/evidence/INDEX.sha256` in the same PR.  
 Machine mirror: add a matching records-only line to `artifacts/evidence_index.jsonl` (see §8.3). The mirror record **MUST** include: `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a `path_proof.txt` stored alongside the artifact.  
 Mirror hygiene (merge-blocking): canonical JSONL, unknown-key rejection, ASCII field order and sort-before-write as pinned in §8.3; exactly one mirror file in the repo.  
 Env-gate pairing: pair this entry with `artifacts/proofs/endpoints_env_gate_proof.log` to prove env-gating (headers-only, LF-terminated; header names lower-case, values verbatim).

**Acceptance hints (titles only; tokens live in HDE-Governance §2.0)**  
 `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_TRANSPORT_PROOF_OK`.

---

## 8.9 Start-command capture (records-only)

**Content:** effective start command as bytes with sha256; path discovered post-emission.

**Indexing:** list in machine mirror and human index (titles/paths only).

**Acceptance hints**  
 `START_COMMAND_CAPTURE_OK`.

---

## 8.10 Environment inventories & validator outputs (names-only)

**Inventories:** canonical JSON listing of environment variables consulted by the service; unknown keys flagged.  
 **Validator outputs:** records-only outputs to prove config sanity.

**Indexing:** list in machine mirror and human index (titles/paths only).

**Acceptance hints**  
 `ENV_INVENTORY_OK`, `VALIDATOR_OUTPUTS_OK`.

---

## 8.11 SBOM (records-only) \[Optional\]

**Purpose.** Provide a build-time Software Bill of Materials to support provenance, audit, and supply-chain review. This artifact is records-only and does not change `release_id` or the Freeze-Pack manifest contents.

**Artifacts (titles/paths only)**

* SBOM (CycloneDX JSON): `sbom/cyclonedx.json`  
* SBOM hash (sha256): `sbom/cyclonedx.json.sha256`

**Format & scope**  
 Format: CycloneDX JSON (v1.x). Titles-only here; bytes live at the path above.  
 Scope: Enumerates runtime/package components for the shipped artifact; no secrets/tokens, no PII.  
 Stability: Generated from the finalized dependency graph of the release build; the tool version/preset is pinned in CI (names-only).

**Indexing (required)**  
 Appendix D (human index): add a titles/paths-only entry for `sbom/cyclonedx.json` and `sbom/cyclonedx.json.sha256` in the same PR that adds/changes them.  
 Machine mirror (`artifacts/evidence_index.jsonl`): add one record per artifact with: `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`.  
 Mirror hygiene (merge-blocking): canonical JSONL (one LF), unknown-key rejection, ASCII field order, sort-before-write (see §8.3); exactly one mirror file in the repo.  
 Path-proof: store a path\_proof (stat transcript) alongside each SBOM artifact and reference it via `proof_anchor` in the mirror record.

**Determinism & environment**  
 Generate and verify under `LC_ALL=C, LANG=C, TZ=UTC`.  
 SBOM bytes are canonical JSON (UTF-8, no BOM; sorted keys where the tool allows; compact; exactly one trailing LF).

**Retention & release identity**  
 SBOM is not part of `catalog/manifest.json` and does not affect `release_id`.  
 Ship under `sbom/` in the release bundle; treat as a governed, records-only artifact.

**Acceptance hints (titles only; tokens live in HDE-Governance §2.0)**  
 `SBOM_PRESENT_OK` — `sbom/cyclonedx.json` exists and is indexed (human \+ machine).  
 `SBOM_HASH_OK` — `sbom/cyclonedx.json.sha256` matches computed digest and is indexed with path-proofs.  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_FINAL_LF_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`.

**Routing (titles-only)**  
 Provenance policy & release workflow: Epic-Process-Guide; HDE-Governance §2.0 tokens and evidence rules.

---

## 8.12 Reader A7 composite proof — schema & validation (records-only) \[Required-Now\]

**Purpose.** Provide a single, machine-checkable JSON artifact that proves the A7 suite on a cataloged JSON success route (GET/HEAD/304; quoted strong ETag; Vary; encoding-invariance). The `/internal/version` ops surface is excluded.

**Schema (single home).**  
 Schema path: `schemas/proofs.reader_success.v1.json` (owned by PF12).  
 Artifact (example): `artifacts/proofs/reader_success_get_head_304.json` (records-only).  
 Routing: Tokens live in Governance; transport bytes live in Vendor Ref. This section governs only the artifact’s shape and validation. Always pair this artifact with the Catalog snapshot and the env-gate proof (see Indexing).

**Minimum required fields (reject unknown keys)**

{

  "route\_path": "\<Catalog title or identifier of the success route\>",

  "env\_gate": {

    "proof\_path": "artifacts/proofs/endpoints\_env\_gate\_proof.log",

    "gated\_ok": true

  },

  "get\_200": {

    "content\_type": "application/json; charset=utf-8",

    "etag": "\\"\<strong-etag\>\\"",

    "body\_sha256": "\<64-hex\>",

    "captured\_at\_utc": "YYYY-MM-DDThh:mm:ssZ"

  },

  "head\_200": {

    "content\_type\_equals\_get": true,

    "content\_length\_equals\_identity": true,

    "no\_body": true

  },

  "after\_304": {

    "seen\_after\_prior\_get": true,

    "no\_body": true,

    "omits\_content\_type": true,

    "omits\_content\_length": true

  },

  "vary\_flags": {

    "authorization": true,

    "accept\_encoding": true

  },

  "etag": {

    "identity\_etag": "\\"\<strong-etag\>\\"",

    "encoding\_invariance\_ok": true,

    "tested\_encodings": \["identity", "gzip", "br"\]

  }

}

**Field notes (normative):**

* `route_path` references the Catalog route by title (no URL).  
* `env_gate.proof_path` points to the headers-only env-gate artifact; `gated_ok: true` asserts non-prod entries are unreachable in prod.  
* `get_200.body_sha256` is the SHA-256 of the LF-terminated canonical body used for identity.  
* `head_200.content_length_equals_identity` compares to the GET identity body length (pre-compression).  
* `after_304.*` proves the 304 invariants (only after prior 200; omits both Content-Type and Content-Length; no body).  
* `vary_flags` must assert both authorization and accept\_encoding.  
* `etag.encoding_invariance_ok: true` affirms identity (ETag) and effective length are stable across accepted encodings.

**Validation & CI (merge-blocking)**

* The proof JSON **MUST** validate against `schemas/proofs.reader_success.v1.json` before indexing.  
* Unknown keys are rejected (mirror enforces).  
* Canonical JSON: UTF-8 (no BOM), sorted keys, compact, exactly one trailing `\n`.  
* Determinism: all captures/derivations run with `LC_ALL=C, TZ=UTC`.  
* Governed locations only: artifact under `artifacts/**`; schema under `schemas/**`.

**Indexing (titles/paths only)**

* **Human Index:** add a titles/paths entry in `docs/evidence/INDEX.json` and update `docs/evidence/INDEX.sha256` in the same PR.  
* **Machine mirror:** add a records-only line to `artifacts/evidence_index.jsonl` (see §8.3) with `artifact_key`, `role:"proof"`, `discovered_physical_path`, `sha256`, `size_bytes`, `produced_at_utc`, and a `proof_anchor` to a `path_proof.txt` stored alongside the JSON file.  
* **Pair with:**  
  * `artifacts/reader/endpoints_snapshot.json` (Catalog snapshot)  
  * `artifacts/proofs/endpoints_env_gate_proof.log` (env-gate headers)

**Acceptance hints (titles-only; tokens live in HDE-Governance §2.0)**  
 `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`, `A7_TRANSPORT_PROOF_OK`,  
 `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`,  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`.

# **9\) Change Log & Doc-Delta Hooks \[Required-Now\]**

## **9.1 What requires a Doc-Delta**

A **Doc-Delta is required** whenever a change affects **frozen inputs**, **closed domains**, **validation rules**, or **canonical bytes**. The Doc-Delta **must accompany** the change that introduces the effect, and the **Evidence Index must be updated in the same PR/commit**.

**Changes that require a Doc-Delta (normative)**

* **Catalog set changes**

  * Adding a new catalog file  
  * Removing a catalog file  
  * Renaming or moving a catalog file path  
* **Schema and validation changes**

  * Any edit to an owning JSON Schema  
  * Any change to arrays-as-sets identity or ordering rules  
  * Any change to topology or cross-reference constraints  
  * Pinning or changing JSON Schema draft / `$schema` / `$id` conventions (pin to **JSON Schema 2020-12**)  
  * Introducing or revising companion checks for constraints that exceed JSON Schema’s native power (uniqueness, cross-catalog membership, ASCII sort)  
* **Closed domain changes**

  * Adding, removing, or renaming IDs in a closed enum (Centers, Gates, Channels, Authorities, Profiles, Magic-10)  
  * Reordering IDs where order is normative  
* **Frozen math inputs changes**

  * Any byte change to `catalog/magic10.json` (Magic-10 IDs, preset-specific inclusive maxima, caps)  
  * Adding or removing a preset entry inside `magic10.maxima`  
  * Changing the prefs key set in the Preset catalog  
* **Manifest and checksums changes**

  * Any edit that changes `catalog/manifest.json` entries, ordering, or content  
  * Adding or removing governed files in the manifest  
  * Changing **canonical bytes** of any governed file (content, key order, whitespace, line endings, encoding)  
  * Introducing or changing required checksum sidecars (`*.sha256`)  
  * Toggling manifest self-listing policy  
* **Machine Evidence Mirror & parity**

  * Changing the **Machine Evidence Mirror** path or **record schema** (`artifacts/evidence_index.jsonl`) or its parity rule with the human Evidence Index (§8.3)  
  * Changing **mirror field order** or **sort-before-write** rules; altering the **single-mirror-file** posture  
  * Changing the **human-index hash sentinel** posture or acceptance (merge-gating)  
* **Governed records-only artifacts in §8**

  * Endpoint-Catalog snapshot and **env-gate proof**  
  * Registry report  
  * DB fingerprint / grants / schema / constraints / partition plan / RW smoke  
  * Start-command capture and Environment inventories/validator outputs  
  * Runtime environment matrix capture

**What the Doc-Delta must include**

* Short **summary** of the change and its rationale  
* **Titles and paths** of affected catalogs and schemas  
* Statement of **impact on `release_id`** with the new value if it changes  
* **Evidence Index updates** (reports, recompute logs, snapshots) updated in the same PR/commit  
* Any **new or updated acceptance tokens** relevant to the change  
* *(Optional but recommended)* PR link and commit hash for traceability

**CI coupling**

* The Doc-Delta must land with **passing** schema, topology, domain-closure, arrays-as-sets, canonicalization, and manifest checks.  
* **Recompute `release_id`** and update snapshots and reports in the same change (enforced by tokens such as **EVIDENCE\_INDEX\_UPDATED\_OK**).  
* **Mirror hygiene** must pass: canonical JSONL, **unknown-key rejection**, **ASCII field order**, **sort-before-write**, **one mirror file**, **path-proofs** present and joined correctly.

  ---

  ## **9.2 Doc-Delta template**

ID/date/scope/targets; summary; acceptance impact; evidence updates; freeze-pack impact; routing (titles-only).

**How to use**

* Fill the template below and attach it to the same change that introduces the edits.  
* Reference other specs by title only (no version numbers in prose).  
* Update §8.6 Evidence Index entries where you add or move evidence.  
* Keep human Appendix D and the machine mirror in §8.3 in the same PR.

**Fill-in template (paste and complete)**

* doc\_delta:  
*   id: "DOCDELTA-YYYYMMDD-\<slug\>"  
*   date: "YYYY-MM-DD"  
*   author: "\<name\>"  
*   
*   scope:  
*     catalogs: \[true|false\]  
*     schemas: \[true|false\]  
*     manifest\_checksums: \[true|false\]  
*     ci\_jobs: \[true|false\]  
*     evidence\_index: \[true|false\]  
*     routing\_only: \[true|false\]  
*   
*   targets:        \# titles and paths only  
*     catalogs\_changed:  
*       \- title: "Centers"           \# §2 reference title  
*         path: "\<relative/path\>"  
*       \- title: "Gates"  
*         path: "\<relative/path\>"  
*     schemas\_changed:  
*       \- title: "Centers Schema"  
*         path: "\<relative/path\>"  
*     other\_artifacts\_changed:  
*       \- title: "catalog/manifest.json"  
*         path: "catalog/manifest.json"  
*       \- title: "Endpoint Catalog env-gate proof"  
*         path: "artifacts/proofs/endpoints\_env\_gate\_proof.log"  
*       \- title: "Registry report"  
*         path: "artifacts/registry/registry\_report.json"  
*       \- title: "EPIC close-pack report"  
*         path: "audit/EPIC-009\_close\_report.md"  
*       \- title: "EPIC close-pack manifest"  
*         path: "audit/EPIC-009\_MANIFEST.json"  
*       \- title: "Evidence Index hash sentinel"  
*         path: "docs/evidence/INDEX.sha256"  
*   
*   summary: |  
*     \<short description of what changed and why, one or two paragraphs\>  
*   
*   acceptance\_impact:            \# list tokens that matter  
*     tokens\_added: \["\<TOKEN\_A\>", "\<TOKEN\_B\>"\]  
*     tokens\_removed: \[\]  
*     tokens\_unchanged:  
*       \- "JSON\_CANONICAL\_CHECK\_OK"  
*       \- "UMS\_AJV\_PASS"  
*       \- "CATALOG\_DOMAIN\_CLOSED\_OK"  
*       \- "TOPOLOGY\_NO\_ORPHANS\_OK"  
*       \- "ARR\_SET\_ASCII\_SORT\_OK"  
*       \- "EVIDENCE\_INDEX\_MIRROR\_OK"  
*       \- "EVIDENCE\_INDEX\_UPDATED\_OK"  
*       \- "EVIDENCE\_INDEX\_HASH\_OK"  
*       \- "CI\_CHECK\_MIRROR\_SCHEMA\_OK"  
*       \- "CI\_CHECK\_FINAL\_LF\_OK"  
*   
*   freeze\_pack\_impact:  
*     manifest\_changed: \[true|false\]  
*     release\_id\_expected\_change: \[true|false\]  
*     computed\_release\_id: "\[OPEN\]"          \# fill after recompute  
*   
*   notes: |  
*     routing\_titles\_only:  
*       math: "HDE-Math-Spec"  
*       governance: "HDE-Governance"  
*       cli\_api\_vendor: "HDE-CLI-API-Vendor-Ref"  
*       architecture: "HDE Architecture"  
*   
*   open\_decisions:  
*     \- id: "OPEN-CH-PRIMARY"  
*       description: "Choose canonical Channels catalog"  
*       owner: "Isis"  
*       status: "open"  
*   
*   ci\_status:                     \# pass/fail at time of landing  
*     catalog\_schema: "pass|fail"  
*     domain\_closure: "pass|fail"  
*     topology: "pass|fail"  
*     arrays\_as\_sets: "pass|fail"  
*     canonical\_json: "pass|fail"  
*     manifest: "pass|fail"  
*     recompute\_release\_id: "pass|fail"  
*     mirror\_schema: "pass|fail"   \# CI\_CHECK\_MIRROR\_SCHEMA\_OK  
*     final\_lf: "pass|fail"        \# CI\_CHECK\_FINAL\_LF\_OK  
*     env\_pins: "pass|fail"        \# LC\_ALL=C, LANG=C, TZ=UTC  
*   
*   evidence\_updates:              \# titles and paths only  
*     \- title: "Checksum Verification Report"  
*       path: "artifacts/math/checksums\_audit.log"  
*     \- title: "Manifest Snapshot"  
*       path: "artifacts/math/manifest\_snapshot.json"  
*     \- title: "Recompute release\_id log"  
*       path: "artifacts/math/release\_id\_recompute.log"  
*     \- title: "Environment Pins"  
*       path: "artifacts/proofs/env\_pins.txt"  
*     \- title: "EPIC close-pack report"  
*       path: "audit/EPIC-009\_close\_report.md"  
*     \- title: "EPIC close-pack manifest"  
*       path: "audit/EPIC-009\_MANIFEST.json"  
*     \- title: "Evidence Index (human)"  
*       path: "docs/evidence/INDEX.json"  
*     \- title: "Evidence Index hash sentinel"  
*       path: "docs/evidence/INDEX.sha256"  
*   
*   change\_log\_entry: |  
*     \<one paragraph for §9 Change Log summarizing the change, listing affected catalogs/schemas by title, stating release\_id impact, and confirming human/machine index parity \+ hash sentinel status\>


**Submission checklist**

* All targets listed by title and path  
* Update §8.6 Evidence Index and §8.3 machine mirror  
* CI jobs pass with updated artifacts  
* `release_id` recomputed if the manifest changed  
* Any unresolved items marked `[OPEN]` with owner and next step  
* Close-pack artifacts listed when applicable  
* Evidence Index hash sentinel updated alongside the human index

  ---

  ## **9.3 Acceptance to land**

All catalog and schema CI **green**. **Evidence Index updated** in the same change. New `release_id` recorded if the pack changed.

**Preconditions (normative)**

* **CI status:** All jobs required by §§8.1–8.2 pass on the same change set:

  * `catalog_schema_validate`  
  * `catalog_domain_closure`  
  * `catalog_topology_coherence`  
  * `catalog_arrays_as_sets`  
  * `catalog_canonical_json`  
  * `integrity_topology`  
  * `integrity_arrays_as_sets`  
  * `integrity_canonicalization_compare`  
* **Manifest integrity:** §6 checks pass in the same change:

  * `MANIFEST_FILE_EQ_CANON_OK`  
  * `MANIFEST_PATH_ASCII_SORT_OK`, `MANIFEST_NO_DUP_PATHS_OK`  
  * `RELEASE_ID_FROM_MANIFEST_OK`  
* **Evidence Index:** Update **§8.6 (human)** and **§8.3 (machine)** in the **same PR**; mirror record has **`proof_anchor`** and obeys field-order/sort rules.

* **Doc-Delta:** If any condition in §9.1 applies, a completed **§9.2 Doc-Delta** is included in the same change.

**Release handling (normative)**

* If any **frozen input** or the **manifest** changed, recompute `release_id` per §6.2 and record it:

  * In the **Manifest Snapshot** evidence file.  
  * In the **Change Log** entry for this change.  
* If **no** frozen input or manifest bytes changed, confirm that the **prior `release_id`** remains valid and record that fact in the Change Log entry.

**Environment and determinism**

* All generation and checks run with **LC\_ALL=C, LANG=C, TZ=UTC** per §4.3.  
* **Two-run identity** proof over the pack and manifest passes on the same inputs.

**Failure policy**

* Any **CI failure**, missing Evidence Index entry, **missing required Doc-Delta**, or **inconsistent `release_id`** blocks the change from landing.

**Acceptance tokens (minimum)**

* `UMS_AJV_PASS`  
* `CATALOG_DOMAIN_CLOSED_OK`  
* `CATALOG_TOPOLOGY_OK`  
* `ARR_SET_ASCII_SORT_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `MANIFEST_FILE_EQ_CANON_OK`  
* `RELEASE_ID_FROM_MANIFEST_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `DOC_DELTA_PRESENT_OK`  
* `ENV_LC_ALL_C_OK`  
* `TWO_RUN_IDENTITY_OK`  
* **`CI_CHECK_FINAL_LF_OK`**  
* **`CI_CHECK_MIRROR_SCHEMA_OK`**  
* **`EVIDENCE_INDEX_HASH_OK`**


  ---

# Appendix A: UMS Schemas

## Ums.catalog.channels

{"meta":{"built\_at\_utc":"2025-10-28T18:04:04.331512Z","sources":\["PF08-Reference-Human Design System.md","PF11-Reference-The Rave I Ching.md"\],"assumptions":\["Channel circuits set only when explicitly confirmed by PF11 gate headers; others use well-known stream inference or marked 'Tribal/Ego' where PF08 text implies Ego/Tribal circuitry.","Astrologic spans copied where visible on PF11 headers; no extrapolation performed for missing gates."\]},"channels":\[{"id":"02-14","name":"The Beat","keynote":"A design of being the keeper of keys","from\_center":"g\_center","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"03-60","name":"Mutation","keynote":"Energy which fluctuates and initiates, pulse","from\_center":"sacral","to\_center":"root","circuit":"Knowing","notes":null},{"id":"08-01","name":"Inspiration","keynote":"The creative role model","from\_center":"throat","to\_center":"g\_center","circuit":"Knowing","notes":null},{"id":"09-52","name":"Concentration","keynote":"A design of determination, focused","from\_center":"sacral","to\_center":"root","circuit":"Understanding","notes":null},{"id":"10-34","name":"Exploration","keynote":"A design of following one's convictions","from\_center":"g\_center","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"10-57","name":"Perfected Form","keynote":"A design of survival","from\_center":"g\_center","to\_center":"spleen","circuit":"Knowing","notes":null},{"id":"11-56","name":"Curiosity","keynote":"A design of a searcher","from\_center":"ajna","to\_center":"throat","circuit":"Sensing","notes":null},{"id":"12-22","name":"Openness","keynote":"A design of a social being","from\_center":"throat","to\_center":"solar\_plexus","circuit":"Sensing","notes":null},{"id":"15-05","name":"Rhythm","keynote":"A design of being in the flow","from\_center":"g\_center","to\_center":"sacral","circuit":"Understanding","notes":null},{"id":"16-48","name":"The Wave Length","keynote":"A design of talent","from\_center":"throat","to\_center":"spleen","circuit":"Understanding","notes":null},{"id":"17-62","name":"Acceptance","keynote":"A design of an organizational being","from\_center":"ajna","to\_center":"throat","circuit":"Understanding","notes":null},{"id":"18-58","name":"Judgment","keynote":"A design of insatiability","from\_center":"spleen","to\_center":"root","circuit":"Understanding","notes":null},{"id":"20-10","name":"Awakening","keynote":"A design of commitment to higher principles","from\_center":"throat","to\_center":"g\_center","circuit":"Knowing","notes":null},{"id":"20-34","name":"Charisma","keynote":"A design where thoughts must become deeds","from\_center":"throat","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"20-57","name":"The Brain Wave","keynote":"A design of penetrating awareness","from\_center":"throat","to\_center":"spleen","circuit":"Knowing","notes":null},{"id":"25-51","name":"Initiation","keynote":"A design of needing to be first","from\_center":"g\_center","to\_center":"ego\_heart","circuit":"Tribal/Ego","notes":null},{"id":"26-44","name":"Surrender","keynote":"A design of a transmitter","from\_center":"ego\_heart","to\_center":"spleen","circuit":"Tribal/Ego","notes":null},{"id":"28-38","name":"Struggle","keynote":"A design of stubbornness","from\_center":"spleen","to\_center":"root","circuit":"Knowing","notes":null},{"id":"30-41","name":"Recognition","keynote":"A design of focused energy","from\_center":"solar\_plexus","to\_center":"root","circuit":null,"notes":null},{"id":"31-07","name":"The Alpha","keynote":"For 'good' or 'bad', a design of leadership","from\_center":"throat","to\_center":"g\_center","circuit":"Understanding","notes":null},{"id":"32-54","name":"Transformation","keynote":"A design of being driven","from\_center":"spleen","to\_center":"root","circuit":"Tribal/Ego","notes":null},{"id":"33-13","name":"The Prodigal","keynote":"The design of the witness","from\_center":"throat","to\_center":"g\_center","circuit":"Sensing","notes":null},{"id":"35-36","name":"Transitoriness","keynote":"A design of a 'Jack of all Trades'","from\_center":"throat","to\_center":"solar\_plexus","circuit":"Sensing","notes":null},{"id":"40-37","name":"Community","keynote":"A design of being a part, seeking a whole","from\_center":"ego\_heart","to\_center":"solar\_plexus","circuit":"Tribal/Ego","notes":null},{"id":"42-53","name":"Maturation","keynote":"A design of balanced development, cyclical","from\_center":"sacral","to\_center":"root","circuit":"Sensing","notes":null},{"id":"43-23","name":"Structuring","keynote":"A design of individuality","from\_center":"ajna","to\_center":"throat","circuit":"Knowing","notes":null},{"id":"45-21","name":"Money","keynote":"A design of a materialist","from\_center":"throat","to\_center":"ego\_heart","circuit":"Tribal/Ego","notes":null},{"id":"46-29","name":"Discovery","keynote":"A design of succeeding where others fail","from\_center":"g\_center","to\_center":"sacral","circuit":"Sensing","notes":null},{"id":"49-19","name":"Synthesis","keynote":"A design of being sensitive","from\_center":"solar\_plexus","to\_center":"root","circuit":"Tribal/Ego","notes":null},{"id":"50-27","name":"Preservation","keynote":"A design of custodianship","from\_center":"spleen","to\_center":"sacral","circuit":"Tribal/Ego","notes":null},{"id":"55-39","name":"Emoting","keynote":"A design of moodiness","from\_center":"solar\_plexus","to\_center":"root","circuit":null,"notes":null},{"id":"57-34","name":"Power","keynote":"A design of an archetype","from\_center":"spleen","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"59-06","name":"Mating","keynote":"A design focused on reproduction","from\_center":"sacral","to\_center":"solar\_plexus","circuit":"Defense","notes":null},{"id":"61-24","name":"Awareness","keynote":"A design of a thinker","from\_center":"head","to\_center":"ajna","circuit":"Knowing","notes":null},{"id":"63-04","name":"Logic","keynote":"A design of mental ease mixed with doubt","from\_center":"head","to\_center":"ajna","circuit":"Understanding","notes":null},{"id":"64-47","name":"Abstraction","keynote":"A design of mental activity and clarity","from\_center":"head","to\_center":"ajna","circuit":null,"notes":null}\],"count":36}

## Ums.catalog.gates.json

{  
  "meta": {  
    "built\_at\_utc": "2025-10-28T18:04:04.331512Z",  
    "sources": \[  
      "PF08-Reference-Human Design System.md",  
      "PF11-Reference-The Rave I Ching.md"  
    \],  
    "assumptions": \[  
      "Channel circuits set only when explicitly confirmed by PF11 gate headers; others use well-known stream inference or marked 'Tribal/Ego' where PF08 text implies Ego/Tribal circuitry.",  
      "Astrologic spans copied where visible on PF11 headers; no extrapolation performed for missing gates."  
    \]  
  },  
  "gates": \[  
    {  
      "gate": 1,  
      "rave\_title": "The Gate of Self-Expression",  
      "i\_ching\_name": "The Creative",  
      "channel\_id": "01-08",  
      "harmonic\_gate": 8,  
      "center": "g\_center",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Scorpio", "deg": 13, "min": 15, "sec": 0 },  
        "end": { "sign": "Scorpio", "deg": 18, "min": 52, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 2,  
      "rave\_title": "The Gate of the Direction of the Self",  
      "i\_ching\_name": "The Receptive",  
      "channel\_id": "02-14",  
      "harmonic\_gate": 14,  
      "center": "g\_center",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Taurus", "deg": 13, "min": 15, "sec": 0 },  
        "end": { "sign": "Taurus", "deg": 18, "min": 52, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 3,  
      "rave\_title": "The Gate of Ordering",  
      "i\_ching\_name": "Difficulty at the Beginning",  
      "channel\_id": "03-60",  
      "harmonic\_gate": 60,  
      "center": "sacral",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Aries", "deg": 26, "min": 22, "sec": 30 },  
        "end": { "sign": "Taurus", "deg": 2, "min": 0, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 4,  
      "rave\_title": "The Gate of Formulization",  
      "i\_ching\_name": "Youthful Folly",  
      "channel\_id": "04-63",  
      "harmonic\_gate": 63,  
      "center": "ajna",  
      "circuit": "Understanding",  
      "astro\_span": {  
        "start": { "sign": "Leo", "deg": 18, "min": 52, "sec": 30 },  
        "end": { "sign": "Leo", "deg": 24, "min": 30, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 5,  
      "rave\_title": "The Gate of Fixed Rhythms",  
      "i\_ching\_name": "Waiting",  
      "channel\_id": "05-15",  
      "harmonic\_gate": 15,  
      "center": "sacral",  
      "circuit": "Understanding",  
      "astro\_span": {  
        "start": { "sign": "Sagittarius", "deg": 11, "min": 22, "sec": 30 },  
        "end": { "sign": "Sagittarius", "deg": 17, "min": 0, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 6,  
      "rave\_title": "The Gate of Friction",  
      "i\_ching\_name": "Conflict",  
      "channel\_id": "06-59",  
      "harmonic\_gate": 59,  
      "center": "solar\_plexus",  
      "circuit": "Defense",  
      "astro\_span": {  
        "start": { "sign": "Virgo", "deg": 22, "min": 37, "sec": 30 },  
        "end": { "sign": "Virgo", "deg": 28, "min": 15, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 7,  
      "rave\_title": "The Gate of the Role of the Self",  
      "i\_ching\_name": "The Army",  
      "channel\_id": "07-31",  
      "harmonic\_gate": 31,  
      "center": "g\_center",  
      "circuit": "Understanding",  
      "astro\_span": {  
        "start": { "sign": "Leo", "deg": 13, "min": 15, "sec": 0 },  
        "end": { "sign": "Leo", "deg": 18, "min": 52, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 8,  
      "rave\_title": "The Gate of Contribution",  
      "i\_ching\_name": "Holding Together",  
      "channel\_id": "01-08",  
      "harmonic\_gate": 1,  
      "center": "throat",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Capricorn", "deg": 24, "min": 30, "sec": 0 },  
        "end": { "sign": "Aquarius", "deg": 0, "min": 7, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 9, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 10, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 11,  
      "rave\_title": "The Gate of Ideas",  
      "i\_ching\_name": "Peace",  
      "channel\_id": "11-56",  
      "harmonic\_gate": 56,  
      "center": "ajna",  
      "circuit": "Sensing",  
      "astro\_span": {  
        "start": { "sign": "Sagittarius", "deg": 22, "min": 37, "sec": 30 },  
        "end": { "sign": "Sagittarius", "deg": 28, "min": 15, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 12, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 13, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 14,  
      "rave\_title": "The Gate of Power Skills",  
      "i\_ching\_name": "Possession in Great Measure",  
      "channel\_id": "02-14",  
      "harmonic\_gate": 2,  
      "center": "sacral",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Scorpio", "deg": 24, "min": 30, "sec": 0 },  
        "end": { "sign": "Sagittarius", "deg": 0, "min": 7, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 15,  
      "rave\_title": "The Gate of Extremes",  
      "i\_ching\_name": "Modesty",  
      "channel\_id": "05-15",  
      "harmonic\_gate": 5,  
      "center": "g\_center",  
      "circuit": "Understanding",  
      "astro\_span": {  
        "start": { "sign": "Gemini", "deg": 28, "min": 15, "sec": 0 },  
        "end": { "sign": "Cancer", "deg": 3, "min": 52, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 16, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 17, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 18, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 19,  
      "rave\_title": "The Gate of Wanting",  
      "i\_ching\_name": "Approach",  
      "channel\_id": "19-49",  
      "harmonic\_gate": 49,  
      "center": "root",  
      "circuit": "Tribal/Ego",  
      "astro\_span": {  
        "start": { "sign": "Aquarius", "deg": 7, "min": 37, "sec": 30 },  
        "end": { "sign": "Aquarius", "deg": 13, "min": 15, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 20, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 21, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 22, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 23,  
      "rave\_title": "The Gate of Assimilation",  
      "i\_ching\_name": "Splitting Apart",  
      "channel\_id": "23-43",  
      "harmonic\_gate": 43,  
      "center": "throat",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Taurus", "deg": 18, "min": 52, "sec": 30 },  
        "end": { "sign": "Taurus", "deg": 24, "min": 30, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 24, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 25, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 26, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 27, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 28, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 29,  
      "rave\_title": "The Gate of Saying Yes",  
      "i\_ching\_name": "The Abysmal",  
      "channel\_id": "29-46",  
      "harmonic\_gate": 46,  
      "center": "sacral",  
      "circuit": "Sensing",  
      "astro\_span": {  
        "start": { "sign": "Leo", "deg": 24, "min": 30, "sec": 0 },  
        "end": { "sign": "Virgo", "deg": 0, "min": 7, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 30, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 31,  
      "rave\_title": "The Gate of Leading",  
      "i\_ching\_name": "Influence",  
      "channel\_id": "07-31",  
      "harmonic\_gate": 7,  
      "center": "throat",  
      "circuit": "Understanding",  
      "astro\_span": {  
        "start": { "sign": "Leo", "deg": 2, "min": 0, "sec": 0 },  
        "end": { "sign": "Leo", "deg": 7, "min": 37, "sec": 30 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 32, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 33, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 34, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 35, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 36, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 37, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 38, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 39, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 40, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 41, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 42, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 43,  
      "rave\_title": "The Gate of Insight",  
      "i\_ching\_name": "Breakthrough",  
      "channel\_id": "23-43",  
      "harmonic\_gate": 23,  
      "center": "ajna",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Scorpio", "deg": 18, "min": 52, "sec": 30 },  
        "end": { "sign": "Scorpio", "deg": 24, "min": 30, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    { "gate": 44, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 45, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 46, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 47, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 48, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 49, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 50, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 51, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 52, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 53, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 54, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 55, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    {  
      "gate": 56,  
      "rave\_title": "The Gate of Stimulation",  
      "i\_ching\_name": "The Wanderer",  
      "channel\_id": "11-56",  
      "harmonic\_gate": 11,  
      "center": "throat",  
      "circuit": "Sensing",  
      "astro\_span": {  
        "start": { "sign": "Aquarius", "deg": 26, "min": 22, "sec": 30 },  
        "end": { "sign": "Pisces", "deg": 2, "min": 0, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": null  
    },  
    {  
      "gate": 57,  
      "rave\_title": "The Gate of Intuitive Insight",  
      "i\_ching\_name": "The Gentle",  
      "channel\_id": "10-57/20-57/34-57",  
      "harmonic\_gate": null,  
      "center": "spleen",  
      "circuit": "Knowing",  
      "astro\_span": {  
        "start": { "sign": "Libra", "deg": 15, "min": 7, "sec": 30 },  
        "end": { "sign": "Libra", "deg": 20, "min": 45, "sec": 0 }  
      },  
      "crosses": \[\],  
      "notes": "Gate 57 participates in three channels: 10-57, 20-57, 34-57."  
    },  
    { "gate": 58, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 59, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 60, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 61, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 62, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 63, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
    { "gate": 64, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." }  
  \],  
  "count": 64  
}

## Ums.schema.channel.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.channel.v1.json","title":"UMS Channel (v1)","type":"object","additionalProperties":false,"required":\["id","name","keynote","from\_center","to\_center"\],"properties":{"id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:\\/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))\*$","description":"Gate-pair identifier (zero-padded NN-NN), e.g. '31-07'. Multiple pairs allowed with '/': '20-57/34-57/10-57'."},"name":{"type":"string","minLength":1},"keynote":{"type":"string","minLength":1},"from\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"to\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"notes":{"type":\["string","null"\]}}}

## Ums.schema.gate.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.gate.v1.json","title":"UMS Gate (v1)","oneOf":\[{"type":"object","additionalProperties":false,"required":\["gate","status"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"status":{"type":"string","const":"TODO"},"notes":{"type":"string"}}},{"type":"object","additionalProperties":false,"required":\["gate","rave\_title","i\_ching\_name","center","astro\_span"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"rave\_title":{"type":"string","minLength":1},"i\_ching\_name":{"type":"string","minLength":1},"channel\_id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:\\/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))\*$","description":"Primary channel id(s) for the gate; hyphenated, zero-padded NN-NN; multiple allowed when a gate participates in multiple channels."},"harmonic\_gate":{"description":"Harmonic partner gate; null or string allowed when multiple partners exist.","oneOf":\[{"type":"integer","minimum":1,"maximum":64},{"type":"string"},{"type":"null"}\]},"center":{"description":"Center label (snake\_case canonical).","type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"astro\_span":{"type":"object","additionalProperties":false,"required":\["start","end"\],"properties":{"start":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}},"end":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}}}},"crosses":{"type":"array","items":{"type":"string"},"uniqueItems":true},"notes":{"type":\["string","null"\]}}}\]}

## **ums.schema.ums.json**

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.v1.json","title":"Unified Master Schema (UMS v1)","type":"object","additionalProperties":false,"required":\["version","wheel","gates","channels"\],"properties":{"version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+(-\[A-Za-z0-9.\_-\]+)?$"},"wheel":{"type":"object","additionalProperties":false,"required":\["zodiac","hexagrams"\],"properties":{"zodiac":{"type":"object","additionalProperties":false,"required":\["segments","segment\_size\_deg"\],"properties":{"segments":{"const":12},"segment\_size\_deg":{"const":30}}},"hexagrams":{"type":"object","additionalProperties":false,"required":\["segments","segment\_size\_deg"\],"properties":{"segments":{"const":64},"segment\_size\_deg":{"const":5.625}}}}},"gates":{"type":"array","minItems":64,"maxItems":64,"items":{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.gate.v1.json","title":"UMS Gate (v1)","oneOf":\[{"type":"object","additionalProperties":false,"required":\["gate","status"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"status":{"type":"string","const":"TODO"},"notes":{"type":"string"}}},{"type":"object","additionalProperties":false,"required":\["gate","rave\_title","i\_ching\_name","center","astro\_span"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"rave\_title":{"type":"string","minLength":1},"i\_ching\_name":{"type":"string","minLength":1},"channel\_id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:\\/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))*$","description":"Primary channel id(s) for the gate; hyphenated, zero-padded NN-NN; multiple allowed when a gate participates in multiple channels."},"harmonic\_gate":{"description":"Harmonic partner gate; null or string allowed when multiple partners exist.","oneOf":\[{"type":"integer","minimum":1,"maximum":64},{"type":"string"},{"type":"null"}\]},"center":{"description":"Center label (snake\_case canonical).","type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"astro\_span":{"type":"object","additionalProperties":false,"required":\["start","end"\],"properties":{"start":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}},"end":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}}}},"crosses":{"type":"array","items":{"type":"string"},"uniqueItems":true},"notes":{"type":\["string","null"\]}}}\]}},"channels":{"type":"array","minItems":36,"maxItems":36,"items":{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.channel.v1.json","title":"UMS Channel (v1)","type":"object","additionalProperties":false,"required":\["id","name","keynote","from\_center","to\_center"\],"properties":{"id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:\\/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))*$","description":"Gate-pair identifier, e.g. '31-07'. Multiple pairs allowed with '/': '20-57/34-57/10-57'."},"name":{"type":"string","minLength":1},"keynote":{"type":"string","minLength":1},"from\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"to\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"notes":{"type":\["string","null"\]}}}},"centers":{"type":"array","items":{"type":"object","additionalProperties":false,"required":\["id"\],"properties":{"id":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"color":{"type":"string"}}}}}}

## ums.schemas.README

## UMS JSON Schemas (JSON Schema 2020-12)

Artifacts:

* `ums.schema.channel.json` — schema for channel catalog entries  
* `ums.schema.gate.json` — schema for gate catalog entries (supports full header and TODO placeholder variants)  
* `ums.schema.ums.json` — umbrella schema for a full UMS bundle (gates \+ channels \+ wheel)

Schema hygiene:

* Each schema sets **`$schema`: `https://json-schema.org/draft/2020-12/schema`** and a **stable `$id`** URL.  
* Title/IDs are aligned to the artifact’s role (e.g., `ums.channel.v1.json`, `ums.gate.v1.json`, `ums.v1.json`).

Validation notes:

* **Zero-padded channel IDs.** `id` (and gate `channel_id`) require **two-digit gate numbers `01..64`** in `NN-NN` form; multiple pairs are allowed with `/`, e.g., `57-20/57-34/10-57`.  
* Angles are modeled inside a sign; **deg `0–29`**, **min/sec `0–59`**.  
* Circuits permit both spellings **`Defense/Defence`** and the tribal label **`Tribal/Ego`** (also `Ego/Tribal`) as seen in the sources.

Reference math (grounded by the books you provided):

* 64 equal hexagrams tile 360° → **5° 37′ 30″** per gate; 6 lines per gate → **56′ 15″** per line.  
* Wheel constants appear in `ums.schema.ums.json` as:  
   `{"zodiac":{"segments":12,"segment_size_deg":30},"hexagrams":{"segments":64,"segment_size_deg":5.625}}`.

How to use (AJV example):

ajv \-s ums.schema.gate.json \-d ums.catalog.gates.json  
ajv \-s ums.schema.channel.json \-d ums.catalog.channels.json

— Generated: 2025-10-28T18:38:46.050554Z

# Appendix B — Channel ID normalization (informative)

**Purpose.** QA aid for catalog builders and vendor normalization tests. This appendix illustrates the **identity rule** and sorting discipline for channel IDs. The **normative home** for channel identity is **§2.1** (Channels), and topology invariants are defined in **§3.2**. No schemas or payload bytes live here.

**Rule (titles-only restatement)**

* Channels are **unordered edges** between two gates.  
* Store the ID in **min→max**, **zero-padded** `NN-NN` form with gates in `01..64`.  
* Arrays treated as sets **MUST** be **deduplicated** and **ASCII-sorted** by `channel_id`.

## B.1 Before → After (normalization examples)

| Input (as received) | Normalized `channel_id` |
| ----- | ----- |
| `57-20` | `20-57` |
| `8-1` | `01-08` |
| `34-10` | `10-34` |
| `43-23` | `23-43` |
| `3-60` | `03-60` |
| `12-22` | `12-22` *(already canonical)* |
| `10-10` | **invalid** *(same gate twice is not a channel)* |

## B.2 Sorting examples (arrays-as-sets)

**Before (unordered, duplicates possible):**

\["57-20","01-08","10-34","23-43","10-34"\]

**Normalize \+ dedupe \+ ASCII-sort → After:**

\["01-08","10-34","20-57","23-43"\]

**Notes**

* Normalization is performed **before** any catalog or evidence emission.  
* **Duplicates or malformed identities fail closed** (see §3.1 JSON Schema validation and §3.2 Graph coherence checks).

## B.3 Evidence hooks (Index titles/paths only)

Register the following artifacts in the Evidence Index (Governance, Appendix D) to demonstrate orientation and topology invariants:

* `audit/gates/topology/orientation_demo.txt` — before/after normalization examples  
* `audit/gates/topology/degree_check.log` — observed gate degrees \+ pass/fail  
* `audit/gates/topology/multiplicity_vector.log` — observed center-pair multiplicities \+ pass/fail

---

# **Appendix C — Governed artifact record types (records-only)**

Titles and paths only. One-line purpose each. Bytes live outside PF12; this appendix governs names and paths only.

* manifest — Freeze-Pack manifest; frozen inputs (path, sha256, size); sole source for release identity. (path: `catalog/manifest.json`)

* freeze\_pack\_manifest — Evidence copy of the Freeze-Pack manifest for audits. (path: `artifacts/math/freeze_pack_manifest.json`)

* release\_id — Canonical release\_id derived from manifest bytes. (path: `artifacts/math/release_id.txt`)

* release\_id\_recompute — Recompute log proving sha256(canonical\_manifest\_bytes) equals release\_id. (path: `artifacts/math/release_id_recompute.log`)

* checksums\_audit — Per-entry sha256/size/presence verification report. (path: `artifacts/math/checksums_audit.log`)

* manifest\_snapshot — Names-only snapshot (release\_id, manifest sha256, entry count, CI timestamp). (path: `artifacts/math/manifest_snapshot.json`)

* human\_index — Human Evidence Index; titles/paths only; 1:1 with machine mirror. (path: `docs/evidence/INDEX.json`)

* human\_index\_hash — Hash sentinel for the Human Evidence Index (sha256 of INDEX.json). (path: `docs/evidence/INDEX.sha256`)

* mirror\_jsonl — Machine Evidence Index; JSONL; 1:1 parity with the human index. (path: `artifacts/evidence_index.jsonl`)

* seeds — Magic-10 seeds catalog; admin-only; exactly 10 entries; manifest-listed frozen input. (path: `catalog/magic10_seeds.json`)

* db\_fingerprint — Normalized database DDL snapshot with sha256; proves schema identity. (path: `artifacts/db/ddl_fingerprint.json`)

* db\_grants\_snapshot — Least-privilege grants snapshot for runtime principal. (path: `artifacts/db/grants.txt`)

* db\_schema\_check — Search\_path/schema echo (names-only posture). (path: `artifacts/db/check_schema.txt`)

* db\_constraints\_check — Constraints posture snapshot. (path: `artifacts/db/check_constraints.txt`)

* db\_partition\_plan — Partition plan definition/proof. (path: `artifacts/db/partition_plan.txt`)

* db\_conn\_env\_selection — Connection env selection order proof. (path: `artifacts/db/conn_env_selection.log`)

* db\_rw\_smoke\_log (optional) — Minimal read/write smoke probe. (path: `artifacts/db/db_rw_smoke.log`)

* registry\_report — Names-only configuration registry proof (no secrets). (path: `artifacts/registry/registry_report.json`)

* endpoint\_catalog\_file — Authoritative Endpoint Catalog (records-only) plus checksum. (paths: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`)

* endpoint\_catalog\_snapshot — Reader JSON success-endpoints snapshot; proves success envelopes. (path: `artifacts/reader/endpoints_snapshot.json`)

* endpoint\_env\_gate\_proof — Env-gating proof (headers-only); shows non-prod entries unreachable in prod. (path: `artifacts/proofs/endpoints_env_gate_proof.log`)

* a7\_headers\_get — A7 GET (200) headers snapshot (headers-only). (path: `artifacts/proofs/success_get.txt`)

* a7\_headers\_head — A7 HEAD (200) headers snapshot (headers-only). (path: `artifacts/proofs/success_head.txt`)

* a7\_headers\_304 — A7 304 headers snapshot (headers-only; omits Content-Type and Content-Length). (path: `artifacts/proofs/success_304.txt`)

* a7\_headers\_writers\_errors — Writers/errors posture headers snapshot (no-store, no ETag). (path: `artifacts/proofs/success_writers_errors.txt`)

* reader\_success\_proof — Composite proof JSON for GET/HEAD/304 on Catalog route. (path: `artifacts/proofs/reader_success_get_head_304.json`)

* ops\_refusal\_proof — Single-file refusal proof (headers block, one blank line, LF-terminated JSON body). (path: `[OPEN: confirm final path; recommended artifacts/proofs/ops_refusal_proof.txt]`)

* encoding\_invariance\_probe — Proof that identity (ETag) and effective length are stable across Accept-Encoding. (path: `artifacts/proofs/encoding_invariance.txt`)

* start\_command\_capture — Effective start command captured as bytes \+ sha256. (path: `artifacts/proofs/start_command_capture.txt`)

* env\_inventory — Environment inventory (names-only) proving consulted keys. (path: `artifacts/proofs/env_inventory.json`)

* env\_pins — Environment pins used for runs (LC\_ALL, LANG, TZ). (path: `artifacts/proofs/env_pins.txt`)

* validator\_outputs — Validator outputs proving config sanity. (path: `artifacts/proofs/validator_outputs.json`)

* internal\_version\_get\_head — /internal/version ops identity proof (headers/body/conditionals). (path: `artifacts/proofs/internal_version_get_head.json`)

* cli\_showcompat\_stdout — Exact showcompat stdout (LF-terminated; non-empty) \+ sha256. (path: `artifacts/cli/showcompat/stdout.json`)

* cli\_showcompat\_two\_run — Two-run identity log for showcompat. (path: `artifacts/cli/showcompat/two_run_identity.log`)

* cli\_showcompat\_abba — AB↔BA byte-diff for showcompat (expected empty). (path: `artifacts/cli/showcompat/abba.diff`)

* reader\_cli\_parity\_diff — Reader vs CLI parity diff (expected empty). (path: `artifacts/cli/showcompat/reader_cli_parity.diff`)

* preimage\_recompute — Log proving sha256(preimage\_bytes) equals idempotence\_hash. (path: `artifacts/cli/showcompat/preimage_recompute.log`)

* cli\_parity\_ab — CLI/SDK parity artifact (A→B). (path: `artifacts/cli/ab.json`)

* cli\_parity\_ba — CLI/SDK parity artifact (B→A). (path: `artifacts/cli/ba.json`)

* cli\_parity\_summary — CLI/SDK parity summary. (path: `artifacts/cli/summary.json`)

* catalog\_schema\_validation — Catalog schema validation report. (path: `artifacts/catalog/catalog_schema_validation.log`)

* domain\_closure\_report — Domain closure report. (path: `artifacts/catalog/domain_closure_report.log`)

* topology\_coherence\_report — Topology coherence report. (path: `artifacts/topology/topology_coherence_report.log`)

* arrays\_as\_sets\_report — Arrays-as-sets canonicalization report. (path: `artifacts/canonical/arrays_as_sets_report.log`)

* canonical\_json\_check — Canonical JSON check report. (path: `audit/gates/canonical_json/json_canonical_check.log`)

* canonicalization\_compare — Canonicalization compare report. (path: `audit/gates/canonical_json/json_canon_compare.log`)

* env\_matrix\_snapshot — Runtime environment matrix (names-only; capture). (path: `artifacts/runtime/env_matrix.snapshot.json`)

* env\_matrix\_failure — Runtime environment matrix failure envelope (frozen failure). (path: `artifacts/runtime/env_matrix.failure.json`)

* env\_connectivity\_snapshot — Dev-only resolver connectivity snapshot. (path: `artifacts/runtime/env_connectivity.snapshot.json`)

* bodygraph\_source\_selection — Source selection snapshot (names-only; no PII). (path: `artifacts/bodygraph/source_selection.snapshot.json`)

* bodygraph\_invariance\_ab — Provider/source invariance proof (A→B). (path: `artifacts/bodygraph/source_invariance/ab.json`)

* bodygraph\_invariance\_ba — Provider/source invariance proof (B→A). (path: `artifacts/bodygraph/source_invariance/ba.json`)

* bodygraph\_invariance\_summary — Summary of invariance checks. (path: `artifacts/bodygraph/source_invariance/summary.json`)

* close\_pack\_report — EPIC close-out report (scope, tokens PASS roster, merged SHAs). (path: `audit/EPIC-009_close_report.md`)

* close\_pack\_manifest — Close-pack manifest (artifact keys, sha256, size). (path: `audit/EPIC-009_MANIFEST.json`)

* sbom\_cyclonedx (optional) — Software Bill of Materials (CycloneDX) with hash. (paths: `sbom/cyclonedx.json`, `sbom/cyclonedx.json.sha256`)

* cli\_preview\_stdout — Admin preview stdout (LF-terminated narrative text; no ANSI). (path: `artifacts/cli/narrative/stdout.txt`)

* cli\_preview\_sidecar — Admin preview sidecar (ids-only; canonical JSON; no prose). (path: `artifacts/cli/narrative/sidecar.json`)

* narratives\_coverage\_10x4 — Router coverage table (10 categories × 4 bands). (path: `audit/gates/narratives/keys_10x4.table.json`)

