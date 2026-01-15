# 0\. Document Control \[Required-Now\]

## 0.1 Header

**Title:** PF12-Canon-HDE-Schemas-and-Artifacts

**Version:** v1.8.7

**Status:** Canon

**Effective date:** 2026-01-12

**Last Update Gate:** BN 9.3.4 Drain 54-57

**Invocation tag:** INV-f2ac55d77ce9aacc

## **0.2 Scope & single homes \[Required-Now\]**

### **Supersession (PF10 addenda)**

PF10 — Glow HD Engine Build Notes is living. Where multiple numbered addenda exist, later addenda supersede earlier guidance. PF12 integrates the latest addenda and routes by titles only to other PF documents (no version numbers).

---

### **Ownership**

This document is the single home for:

* Engine catalogs (under `catalog/`).  
* The freeze-pack manifest at `catalog/manifest.json`.  
* Checksum sidecars (`*.sha256`) for governed files.  
* Closed enumerations and canonical artifact rules (manifest → `release_id`).  
* Engine QA export artifacts for stateless/no-DB modes — canonical JSON schemas and Evidence Catalog families for BodyGraph export JSON, compat export JSON, and optional “run bundle” aggregates produced directly from birth data or vendor JSON without relying on database user records (see §1.1 and §8.x).

`CANON_CHECKSUMS.json` is deprecated; the manifest at `catalog/manifest.json` is authoritative for frozen inputs and pack identity.

---

### **Human Evidence Index (single home)**

**Path:** `docs/evidence/INDEX.json`

* Canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF).  
* Titles and paths only; no payload bytes.  
* Must maintain 1:1 parity with the Machine Evidence Mirror (see §8.3).  
* Hash sentinel `docs/evidence/INDEX.sha256` is computed over the canonical bytes of INDEX.json (merge-gating; token semantics live in HDE-Governance).  
  ---

### **Machine Evidence Mirror (governed here)**

**Path:** `artifacts/evidence_index.jsonl`

* Governed artifact; records-only JSONL.  
* Content and schema are owned in §8.3.  
* CI enforces 1:1 parity with the Human Evidence Index.  
* Each record MUST include fields sufficient for proof and reproducibility (`artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`).  
* Path-proofs are stored alongside each artifact; `proof_anchor` must point to the matching transcript.

**Mirror discipline (detailed in §8.3):**

* Canonical JSONL (UTF-8; ASCII-sorted keys; compact; exactly one LF per record).  
* Unknown-key rejection is enforced.  
* Fixed ASCII field order and sort-before-write by (`artifact_key`, `discovered_physical_path`).  
* Exactly one mirror file must exist at `artifacts/evidence_index.jsonl`.

  #### **Mirror self-record semantics (implementation checklist) \[Required-Now\]**

The Machine Evidence Mirror is itself a governed artifact at:

* `artifacts/evidence_index.jsonl`

In addition to the per-record rules in §8.3, implementations and validators **MUST** observe the checklist below to prevent recurring CI drift and “proof SHA” mismatches.

1. **Exactly one self-record is required**

* The mirror **MUST** contain exactly one record whose `discovered_physical_path` equals `artifacts/evidence_index.jsonl` (the mirror self-record).

* The self-record’s `proof_anchor` **MUST** point to the mirror’s own sibling path-proof transcript:  
   `artifacts/evidence_index.jsonl.path_proof.txt`

2. **Excluded-from-hash rule (self-record only)**

* To avoid self-referential hashing, the self-record’s `sha256` and `size_bytes` **MUST** be computed over the mirror file’s canonical bytes **with the self-record line excluded**.

* All other records continue to use `sha256` and `size_bytes` computed from the canonical bytes of their target artifacts.

3. **Proof transcript expectations**

* The mirror’s sibling path-proof transcript (`artifacts/evidence_index.jsonl.path_proof.txt`) **MUST** remain coherent with the self-record semantics above and **MUST** satisfy the general path-proof schema described in §8.3.

* Validators **MUST** treat a mismatch between the self-record and its `proof_anchor` transcript as a merge-blocking error.

4. **Regression test coverage (merge-blocking)**

* Any PR that changes evidence tooling or mirror generation **MUST** update or confirm a dedicated regression test for mirror self-record semantics (for example: `tests/evidence/test_machine_mirror_self_proof.py`).

* This test **MUST** remain merge-blocking so that the producer and validator cannot silently diverge.

5. **Single mirror file (no alternates)**

* `artifacts/evidence_index.jsonl` is the **only** canonical Machine Evidence Mirror path.

* Any file resembling a mirror under `docs/evidence/**` (for example, `docs/evidence/INDEX.machine_mirror.jsonl`) is **non-canonical** unless and until a Doc-Delta in PF12 explicitly introduces it and defines its purpose, schema, and indexing posture.

  #### **Schema validation tooling dependency posture (evidence validators) \[Required-Now\]**

Some evidence tooling validates governed JSON artifacts against JSON Schemas. To avoid CI-only failures caused by missing optional dependencies:

* Evidence schema validation tooling **MUST** either:

  * (A) declare its dependencies as **required for CI** and ensure CI installs them, or

  * (B) behave as **optional** and skip cleanly (with an explicit skip reason) when dependencies are absent.

* Tests that invoke schema validation **MUST** reflect the chosen posture and **MUST NOT** hard-fail solely due to missing optional dependencies unless PF-Canon explicitly mandates them as required.  
  ---

### **Governed locations only**

Evidence must live under governed repo paths (for example, `artifacts/**`, `docs/**`, `audit/**`). Transient generator paths (e.g. `codex/out/**`) are not authoritative and MUST NOT be indexed.

---

### **Directory naming (lower-case ASCII)**

All directory names in the repository and application codebase MUST use lower-case ASCII.

* Under governed roots (including `artifacts/**`, `docs/**`, `audit/**`, `catalog/**`, `schemas/**`), introducing any mixed-case or upper-case directory name is non-conforming and is treated as a QA failure.  
* If any directory renames are required to normalize legacy mixed-case drift, those renames MUST be accompanied by same-PR updates to the Human Evidence Index (`docs/evidence/INDEX.json`), its hash sentinel (`docs/evidence/INDEX.sha256`), the Machine Evidence Mirror (`artifacts/evidence_index.jsonl`), and the affected path-proofs, per §8.6 and §8.3.

Governed evidence families include, at minimum, the Endpoint Catalog proofs, CLI parity set, `/internal/version` ops proofs, DB posture snapshots, BodyGraph artifacts, stateless QA export artifacts (BodyGraph export JSON, compat export JSON, run bundles), and other families enumerated in §8.6.

---

### **Evidence bundles & manifests (ledger-centric evidence)**

PF12 assumes a ledger-centric, text-based evidence posture for the HD Engine:

* Certain governed evidence families MAY be represented as evidence bundles instead of many small files. An evidence bundle is a textual artifact (typically JSON or JSONL) under `artifacts/**` or `docs/evidence/**` that aggregates multiple logical evidence members into a single file.  
* Each bundle MUST have a companion bundle manifest (also textual JSON/JSONL under governed paths) that, for each logical member, records at least:  
  * a member or logical `artifact_key`,  
  * a sha256 hash (lowercase 64-hex) of the member’s canonical bytes, and  
  * `size_bytes` for that member,  
    plus any additional descriptors owned by local schemas and tests.  
* For bundle-based families, PF12 treats the bundle file and its manifest as the governed artifacts. They are indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` under the standard Evidence Index / Machine Evidence Mirror discipline (§8.3). Individual members inside the bundle MAY, but need not, appear as separate rows in the Human Index or Machine Mirror.  
* Baseline HD Engine evidence that supports PF19 QA tokens and PF23 reality audits MUST remain per-PR inspectable via text artifacts: Human Index, Machine Mirror, bundle manifests, and key QA logs. Binary or compressed artifacts (for example, archives) MAY exist as supplementary files but MUST NOT be the sole governed evidence for any acceptance token that Codex/ChatGPT-class agents are expected to reason about.

In the rest of this document, the term artifact includes both single-file artifacts (for example, a single log or JSON snapshot) and bundle artifacts (bundle file \+ manifest) unless otherwise specified. The Evidence Catalog in §8.6 enumerates which families use bundles and which remain single-file artifacts.

---

### **Candidate 1 bundle behavior (EPIC020 transitional rules)**

During the EPIC020 Candidate 1 migration, PF12 adopts the following transitional, EPIC-scoped constraints for the EPIC020 evidence bundle generator.

#### **Mixed artifact entry forms (acceptance map compatibility)**

The EPIC020 bundle/manifest generator MUST be able to consume both:

* structured artifact entries (objects with `artifact_key` / `bundle_artifact_key` / `path` or `discovered_physical_path`), and  
* legacy string entries (where an artifact is named only by its path string)

in `docs/acceptance_map_epic020.json` without requiring the acceptance map to be rewritten.

For string entries, the generator MAY infer a logical `artifact_key` and `bundle_artifact_key` from the token and path (for example, using the token name as `bundle_artifact_key` and the path as `artifact_key`), but this inference is transitional and EPIC020-only: canonical artifact and bundle keys remain governed by PF-Canon and may be pinned explicitly in future Doc-Deltas. PF12 continues to treat acceptance maps as sources of paths and tokens, not as canonical homes for bundle key naming.

#### **No self-referential bundling**

Evidence bundles and their manifests are themselves governed artifacts with their own Index/Mirror records. They MUST NOT be treated as bundle members, even if they appear as governed artifacts for tokens in acceptance maps.

Bundle generators MUST restrict membership to the underlying evidence files (for example, compat logs, JSON snapshots, headers, QA checklists) and MUST skip any acceptance-map entries whose discovered physical path points at their own outputs (for example `artifacts/epic020/bundles/*.bundle.json` or `*.manifest.json` for EPIC020).

This rule prevents self-referential bundles that cannot pass check-mode invariants and aligns with Candidate 1’s design: bundles/manifests are logical families over existing EPIC020 evidence, not members of themselves or other bundles.

#### **Scope**

These behaviors are transitional and scoped to EPIC020 Candidate 1\. They do not change the general Evidence Catalog model: PF12 still expects acceptance maps and manifests to remain names-only inputs, with canonical bundle key naming and membership semantics owned by PF12/PF14/PF19/PF20 via future Doc-Deltas.

---

### **Evidence Catalog (single home)**

PF12 §8.x and §8.6 together form the Evidence Catalog: the single home for governed evidence artifact families and their titles/paths. Other PF documents (PF04/PF05/PF09/PF14/PF20) must refer to these families by name and must not maintain parallel path lists.

**Non-citation rule (MUST).** PF20 MUST NOT be cited to define evidence surface paths, evidence shapes, or remediation predicate targets. For evidence paths/shapes and predicate target surfaces, cite PF12 (this document’s Evidence Catalog: §8.3 schemas and §8.6 entries).

---

### **Routing by title only**

Math arithmetic (scoring, thresholds, preimage recipe) and transport bytes (Reader, CLI, vendor) are not defined here; they are referenced by title only from:

* HDE-Math-Spec  
* HDE-Governance  
* HDE-CLI-API-Vendor-Ref  
* HDE Architecture  
  ---

### **Tokens & acceptance hints (names-only)**

HDE-Governance owns the Token Registry and all acceptance token semantics.

* PF12 binds those tokens to concrete artifact shapes and Evidence Index / Machine Mirror records via “Acceptance hints (names-only)” lists in later sections; it does not redefine semantics.  
* HDE-Build Checklist (PF09) is a consumer-only view: its token references must be a subset of PF04/PF12 names and may not introduce new token names.  
  ---

### **Process and PR workflow**

The “update repo docs and Evidence Index in the same PR” rule and other PR workflow details live in Epic-Process-Guide (PF06). PF12 describes what must be kept in sync (catalogs, manifest, Index/Mirror, stateless QA export families), not how PRs are managed.

---

### **Catalogized seeds (admin-only)**

The Magic-10 seeds catalog at `catalog/magic10_seeds.json` is governed here (see §2.7).

Changes to this catalog are frozen-input changes and require `release_id` recomputation per §6.

## 0.3 Tagging

Each section is labeled to indicate implementation status:

* \[Implemented\] — verified in the repository and enforced by CI and tests.

* \[Required-Now\] — required for the current build and release discipline; must be satisfied before promotion.

* \[Speculative\] — accepted future design; not yet wired.

* \[OPEN\] — unresolved items or toggles pending a Doc-Delta.

## 0.4 Change policy \[Required-Now\]

**Single homes.**

* This document owns:

  * Catalogs under `catalog/`.

  * The freeze-pack manifest at `catalog/manifest.json`.

  * Checksum sidecars (`*.sha256`) for governed files.

* Bytes owned by other PF documents are referenced by title only and are not restated here:

  * PF01 — scoring, thresholds, deterministic preimage and idempotence.

  * PF02 — architectural boundaries and single-home routing.

  * PF05 — transport and vendor shaping.

  * PF04 — acceptance gates and Reader transport policy.

**Doc-Delta discipline (normative edits only).**  
 A Doc-Delta is required for any change to:

* A catalog’s closed domain (IDs, enums, order).

* A catalog’s schema.

* Canonical JSON serialization rules.

* The freeze-pack manifest shape or entries (`catalog/manifest.json`).

* Frozen math inputs under `catalog/` (for example, `catalog/magic10.json` IDs or inclusive maxima, `catalog/channels.json` contents).

* The Machine Evidence Mirror path or record schema (`artifacts/evidence_index.jsonl`) or its parity rule with the Human Evidence Index (§8.3).

* Governed records-only artifacts in §8, including (titles/paths only):

  * Endpoint Catalog file and checksum: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`.

  * Reader A7 composite proof JSON: `artifacts/proofs/reader_success_get_head_304.json`.

  * Dev connectivity snapshot: `artifacts/runtime/env_connectivity.snapshot.json`.

  * CLI parity artifacts: `artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`.

  * `/internal/version` ops proofs (headers/body snapshots) as enumerated in §8.6.

  * Registry report, DB fingerprint, start-command capture, environment inventories and validator outputs (names as in §8.6).

  * BodyGraph release bindings: `artifacts/bodygraph/release_bindings.json`.

  * BodyGraph refresh policy snapshot: `artifacts/bodygraph/refresh_policy.snapshot.json`.

  * BodyGraph metrics snapshot (keys-only): `artifacts/bodygraph/metrics.snapshot.json`.

  * BodyGraph keys-only logs sample (sanitized): `artifacts/bodygraph/keys_only.logs.sample`.

Each Doc-Delta **must** state scope, targets, acceptance impact, evidence updates, and whether a new `release_id` is required.

**Evidence Index updates (same PR).**

* Whenever any golden, artifact, snapshot, or script path changes, update in the **same PR/commit**:

  * The Human Evidence Index (`docs/evidence/INDEX.json`),

  * The Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`),

  * The Machine Evidence Mirror (`artifacts/evidence_index.jsonl`).

* Add a matching entry to the Change Log and Doc-Delta hooks (process ownership lives in PF06 — Epic-Process-Guide).

**Release identity (freeze-pack).**

* Any byte-level change to frozen inputs enumerated by the manifest, or to the canonical bytes of `catalog/manifest.json`, **MUST** produce a new `release_id` and record it in the Doc-Delta.

* Changes to `catalog/magic10_seeds.json` are frozen-input changes and require `release_id` recomputation.

* For narratives, frozen inputs include the narratives pack manifest at `catalog/narratives/manifest.json` and the pack members under `catalog/narratives/*` per §2.8.

**Editorial vs normative.**

* Pure editorial rearrangements that do not change catalogs, schemas, or canonical bytes do **not** require a Doc-Delta.

* All normative changes do.

**CI enforcement (merge-blocking).**  
 CI must fail if any of the following are true:

* Catalogs fail schema or closed-domain checks.

* Artifact files violate canonical JSON rules (UTF-8, sorted keys, compact separators, exactly one LF, no BOM).

* The Human Evidence Index or Machine Evidence Mirror is not updated alongside changed paths, or parity between them is broken.

* The JSONL Mirror is non-deterministic (not one object per line, unsorted keys, missing trailing LF), has unknown keys, is missing path-proofs, violates ASCII field order or sort-before-write, or more than one `artifacts/evidence_index.jsonl` exists.

* Required checksum sidecars for governed files are missing.

* The Evidence Index hash sentinel does not match `INDEX.json` bytes.

* The Environment Matrix Snapshot artifact — `artifacts/runtime/env_matrix.snapshot.json` (schema v3; singleton semantics) — is missing or invalid; any change to its schema or path requires a Doc-Delta and same-PR Index/Mirror updates.

## 0.5 Open decisions \[Tracking\]

This section records unresolved items that require confirmation. Each remains \[OPEN\] until the named owner confirms. Changes that affect frozen inputs, schemas, closed domains, or canonical bytes must land with a Doc-Delta.

* **CH-PRIMARY**  
   Status: RESOLVED  
   Decision: canonical Channels catalog path is `catalog/channels.json`.  
   Owner: Isis  
   Severity: critical  
   Affects: §§2.1, 3.2.1, 5, 6  
   Next: update all references; retire other channel files to Historical.

* **CHANNEL-IDENTITY**  
   Status: RESOLVED  
   Decision: `channel_id = "NN-NN"` with gates zero-padded `01..64`, min-first; arrays-as-sets sort ASCII by `channel_id`.  
   Owner: Isis  
   Severity: high  
   Affects: §§3.2.1, 4.2  
   Next: enforce in schemas and CI; fail on duplicates or wrong order.

* **CHECKSUMS-NAMING**  
   Status: RESOLVED  
   Decision: the freeze-pack manifest file is `catalog/manifest.json`. Any prior `CANON_CHECKSUMS.json` name is deprecated and must not be used.  
   Owner: Isis  
   Severity: high  
   Affects: §§5.1–5.3, 6.1–6.4  
   Next: rename references and stubs; ensure `*.sha256` sidecars exist for governed files.

* **MAGIC10-HOME**  
   Status: RESOLVED  
   Decision: Magic-10 IDs and inclusive maxima live in `catalog/magic10.json` (not embedded in presets).  
   Owner: Isis  
   Severity: high  
   Affects: §§2.5–2.6, 6.1  
   Next: point presets to this catalog; Doc-Delta on any byte change.

* **PACK-ROOT**  
   Status: RESOLVED  
   Decision: pack root is `catalog/` (used to resolve relative paths in the manifest).  
   Owner: Isis  
   Severity: medium  
   Affects: §5.1, §6.1  
   Next: pin in text and examples; changing it bumps `release_id`.

* **SELF-LISTING**  
   Status: RESOLVED  
   Decision: **no** self-listing for `catalog/manifest.json`.  
   Owner: Isis  
   Severity: low  
   Affects: §§5.2, 6.1  
   Next: keep manifest entries for governed files only; validate manifest like any other governed artifact.

* **AUTH-PROFILES-USAGE**  
   Status: OPEN  
   Current: whether Authorities and Profiles catalogs are consumed in v1.  
   Owner: Isis  
   Severity: medium  
   Affects: §2.2 (and CI inclusion)  
   Next: confirm usage; include or exclude from CI scope accordingly.

* **ID-CHARSET**  
   Status: RESOLVED  
   Decision: catalog ID charset/case policy is `^[a-z0-9_]+$`, case-sensitive.  
   Owner: Isis  
   Severity: medium  
   Affects: §3.3 and owning schemas  
   Next: reflect in schemas and validation text.

* **PATH-CHARSET**  
   Status: RESOLVED  
   Decision: POSIX paths, no `..`, no `//`, max 256 bytes.  
   Owner: Isis  
   Severity: low  
   Affects: §5.1  
   Next: pin constraints; add to §5.1 validation rules.

* **SCHEMA-DRAFT**  
   Status: RESOLVED  
   Decision: JSON Schema 2020-12; `$id` is a stable title-path.  
   Owner: Isis  
   Severity: medium  
   Affects: §3.1 and schema files  
   Next: ensure existing schemas declare `$schema` / `$id` accordingly.

* **ALIASES-POLICY**  
   Status: RESOLVED  
   Decision: input-only aliases in request handling; outputs remain canonical (centers/planets/lines).  
   Owner: Isis  
   Severity: medium  
   Affects: §3.3 and request rules in HDE-CLI-API-Vendor-Ref  
   Next: add the corresponding note here and rules in the request spec (titles only).

* **SERIALIZATION-SCOPE**  
   Status: RESOLVED  
   Decision: Canonical JSON rules apply to JSON evidence artifacts; operational logs remain keys-only (not necessarily canonical JSON).  
   Owner: Isis  
   Severity: low  
   Affects: §4, §5  
   Next: none; already reflected in §4.

* **EVIDENCE-PATHS**  
   Status: RESOLVED (updated)  
   Decision: fix the Machine Mirror path to `artifacts/evidence_index.jsonl` (records-only). Require 1:1 parity with the Human Evidence Index, path-proofs, and canonical JSONL (UTF-8, sorted keys, compact, single trailing LF).  
   Owner: audit  
   Severity: low  
   Affects: §8.3, §4  
   Next: enforce in CI; fail on mismatch.


* **MTIME-UTC-SEMANTICS**  
   Status: RESOLVED  
   Decision: `mtime_utc` in governed path-proof transcripts is the **refresh-time mtime** of the artifact: a UTC ISO-8601 timestamp captured when the evidence job refreshed that artifact, truncated to whole seconds with **microsecond \== 0**, and **not later than** the artifact’s current filesystem `stat().st_mtime` at the time of capture or check (monotone semantics). It is **not** required to stay equal to future `stat()` values across clones or reruns on other machines. `produced_at_utc` remains the logical evidence refresh timestamp (when the evidence job ran) and is also a UTC ISO-8601 string; it may be updated on each refresh or carried forward when `mtime_utc` is unchanged. Integrity gates continue to rely primarily on `sha256` and `size_bytes` equality between the artifact, its mirror record, and its path-proof; `mtime_utc` and `produced_at_utc` provide temporal context and are validated for format and monotonicity.  
   Owner: Isis  
   Severity: medium  
   Affects: §8.3 (path-proof transcript schema), PF19 (QA checks), PF10 (evidence addenda)  
   Next: Treat the refresh-time, monotone `mtime_utc` semantics as **canon** for all governed path-proofs. Any future change to these semantics MUST land with a Doc-Delta and synchronized updates to PF19, evidence tools (`tools/evidence/update_evidence_index.py`, `ci/checks/check_mirror_schema.sh`), and the relevant tests before being considered accepted. 

* **MIRROR-RECORD-SCHEMA**  
   Status: RESOLVED (updated)  
   Decision: minimum mirror record keys are  
   `{"artifact_key","role","sha256","size_bytes","produced_at_utc","discovered_physical_path","proof_anchor"}`; reject unknown keys.  
   Owner: audit  
   Severity: low  
   Affects: §8.3  
   Next: validate against schema; reject unknown keys; ensure join with Human Index (title,path).

* **SEEDS-CATALOGIZE**  
   Status: RESOLVED  
   Decision: catalogize Magic-10 seeds at `catalog/magic10_seeds.json` (admin-only; exactly 10 entries).  
   Owner: Isis  
   Severity: medium  
   Affects: §2.7 (new), §3, §6  
   Next: add catalog \+ schema; include in manifest; any byte change recomputes `release_id`.

* **EVIDENCE-BUNDLES-HASH-MODELS**

  Status: OPEN

  Decision: Candidate 1 (“Evidence Bundles with Manifests”) is adopted as the baseline evidence architecture: evidence MAY be grouped into textual bundles with textual manifests, and the bundle \+ manifest are treated as governed artifacts under the existing Evidence Index / Machine Mirror discipline. Current canon still expects **per-artifact path proofs**, where “artifact” may be a single file or a bundle artifact/manifest file; no hash-only or index-only families are permitted yet. Any future move to hash-only or index-only evidence (no on-disk member payloads) MUST land with a Doc-Delta that reconciles §8.3 path-proof semantics and Mirror schema, and must be coordinated with HDE-Mechanics Guide, HDE-Build Checklist, Glow QA Guide, and Reality Audits before implementation.

  Owner: audit

Severity: medium

Affects: §8.3 (Machine Evidence Mirror and bundle semantics), PF14 evidence tooling, PF09 evidence gates, PF19 QA tokens, PF23 Reality Audits

Next: Design and agree a hash-only/index-only model (Candidate 4\) and update PF12 \+ dependent PF docs via Doc-Delta before any such evidence families appear in the repo.

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

**Stateless QA export artifacts (no-DB mode).**  
 PF12 also governs the schemas and Evidence Catalog families for **stateless QA exports** produced directly by the engine and CLI from birth data or vendor JSON, without requiring database user records:

* **BodyGraph export JSON** — a canonical JSON object that records:

  * raw birth inputs used for the computation (date, time, location as normalized fields),

  * the resolved BodyGraph topology (centers, gates, channels, profile, authority, definition, type) as IDs and structures only, and

  * any internal registry IDs required for downstream compat or narratives.  
     It MUST NOT embed app-level user identifiers or database primary keys. It is a pure engine result over frozen catalogs and math inputs (titles-only to HDE-Math-Spec and HDE-Schemas & Artifacts).

* **Compat export JSON (stateless mode)** — a canonical JSON object that records compat results computed either from two BodyGraph export files or two birth tuples:

  * the pair of inputs (referenced by birth data and/or BodyGraph export identity),

  * the internal compat result (closed Magic-10 IDs and bands only; numbers remain admin/internal), and

  * the Reader v1 public envelope (six-key object per PF01/PF05) as a nested structure for parity checks.  
     This artifact is a QA/admin surface only; it remains numeric-free at the public Reader layer.

* **Optional “run bundle” JSON** — a composite QA artifact that aggregates, for a single compat run:

  * the originating birth inputs or vendor JSON,

  * the resulting BodyGraph export JSON for each chart, and

  * the compat export JSON for the pair.  
     It exists to support reproducible QA runs and audits; concrete schema and usage live under §8.x Evidence Catalog.

All three stateless QA artifact types MUST follow the canonical JSON policy defined in this document (UTF-8, sorted keys, compact separators, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted) and MUST be admissible to the Evidence Index/Mirror under governed paths (`artifacts/**`, `audit/**`) when used as part of QA. They are **not** public app payloads; transport bytes and CLI flags live in HDE-CLI-API-Vendor-Ref and HDE-Governance (titles-only).

By design, **math arithmetic** (scoring, thresholds, preimage recipe) and **transport bytes** (Reader/CLI/vendor) are **not duplicated here** and are referenced **by title only** in their owning documents.

---

## **1.2 Titles-only routing \[Required-Now\]**

### **Artifact binding rules (paths-of-record; normative)**

PF12 is the single home for governed artifact families and their canonical paths-of-record. Plans and acceptance artifacts MUST bind to these canonical surfaces and MUST NOT invent alternates.

### **Guard proofs are evidence-only by default (promotion discipline)**

Guard proof artifacts MAY be required deliverables, but they do not create new acceptance token obligations.

If a guard proof artifact is used for closure wiring (for example referenced by an acceptance map, token↔evidence matrix, or close-pack), it MUST be treated as governed evidence like other PF12 families:

* stable path under governed roots,  
* updated in the Human Evidence Index and Machine Evidence Mirror in the same PR when bytes change, and  
* sibling `*.path_proof.txt` transcripts when required by the Evidence Catalog posture.

### **Canonical JSON gate artifacts (single family; no dual-home)**

Canonical JSON gate artifacts MUST use the canonical family under: `audit/gates/json_gate/canonical/`

At minimum, the canonical family includes:

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (required)  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` (required)  
* `audit/gates/json_gate/canonical/json_gate_structured_record.json` (optional by default; may be required by an explicit plan)

…plus their corresponding path proofs as defined by the owning canon.

The Implementation Plan path family:

* `audit/gates/canonical_json/canonical_json.gate.json`  
* `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`

…is treated as non-authoritative legacy naming and MUST NOT be required by new plans or acceptance binding unless canon explicitly reinstates it (via PF12).

Acceptance artifacts MUST NOT dual-home bindings across `audit/gates/json_gate/canonical/` and any legacy families (including `audit/gates/canonical_json/` and `audit/gates/canonical/`).

### **Evidence index snapshot artifacts (single home; remove EPIC-local variant)**

Canonical evidence index snapshot artifacts MUST use the gate-family path:

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

The EPIC-local variant under `audit/qa/hde-epic<NNN>/…/evidence_index_snapshot.json` is non-authoritative and is not a closure-required canonical surface. Plans and acceptance artifacts MUST NOT bind to EPIC-local variants when the PF12 canonical gate-family surface exists.

### **Canonical compare artifacts (no epic-local compare paths)**

Canonical compare evidence for canonical JSON gate checks MUST reuse the canon-defined surface under `audit/gates/json_gate/canonical/` (see `json_gate_compare_log.ndjson` above).

Epics MUST NOT introduce new compare artifact paths as “the canonical compare proof” without an explicit canon change routed through a Doc-Delta and drained into the owning PF-Canon homes.

### **Close-pack artifacts (deterministic path-of-record; baseline artifacts)**

The close-pack pair MUST be located under `audit/` using the `EPIC-###` pattern (3 digits):

* `audit/EPIC-###_close_report.md`  
* `audit/EPIC-###_MANIFEST.json`

These are baseline closure artifacts (required artifacts), not acceptance tokens by default. They MUST NOT be relocated into alternate directory trees (for example `audit/qa/**` or `artifacts/**`) without an explicit canon change.

### **Close-pack manifest `key_outputs` (named binding map; normative)**

The close-pack manifest (`audit/EPIC-###_MANIFEST.json`) MUST include `key_outputs` as a JSON object (map) where:

* each key is a stable pointer name (string),  
* each value is a repo-relative artifact path (string), and  
* `key_outputs` MUST NOT be a list.

### **EPIC023 required bindings (normative)**

For EPIC023, `key_outputs` MUST include these keys and exact values:

* `acceptance_map`: `docs/acceptance_map_epic023.json`  
* `token_matrix`: `audit/qa/hde-epic023/token_evidence_matrix.md`  
* `acceptance_map_viability`: `audit/qa/hde-epic023/acceptance_map_viability.log`  
* `qa_step_manifest`: `audit/qa/hde-epic023/qa_step_logs_manifest.json`  
* `doc_deltas`: `audit/docdeltas/hde-epic023_doc_deltas.md`  
* `close_report`: `audit/EPIC-023_close_report.md`  
* `close_manifest`: `audit/EPIC-023_MANIFEST.json`

Additional `key_outputs` entries are allowed, but these bindings are the closure minimum.

### **Titles-only routing rule**

**Rule.** References are by title only. Do not include version numbers in prose. Do not restate bytes owned by other specs.

* **Math:** scoring and thresholds; deterministic preimage (idempotence) recipe.  
  Referenced by title only in HDE-Math-Spec. No arithmetic or preimage bytes are restated here.  
* **Governance / CLI:** Reader transport (headers, conditional delivery, error model), writers and errors posture, and vendor request shaping plus typed mapping.  
  Referenced by title only in HDE-Governance and HDE-CLI-API-Vendor-Ref. No transport or vendor bytes are restated here.  
* **Architecture:** component boundaries (engine, adapter, presenter) and single-homes/single-emitter boundary.  
  Referenced by title only in HDE-Architecture. No architectural prose is duplicated here.  
* **Narratives routing reminder:** narratives transport and example payload bytes are out of scope for this document and are routed by title to HDE-Governance (A7) and HDE-CLI-API-Vendor-Ref.

---

#  **2\. Catalogs Index (titles/paths only) \[Required-Now\]**

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

## 2.8 Narratives pack (keys/templates/palettes/suppression\_map) \[Required‑Now\]

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

---

## 3.4 Narratives composer response schema \[Required‑Now\]

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

* **Freeze-Pack Manifest evidence copy (no alternate semantics)**

  * path: `artifacts/math/freeze_pack_manifest.json`

  * MUST be a **byte-identical copy** of the canonical on-disk `catalog/manifest.json` (identity is on canonical bytes; no derived schemas or alternate contracts).

  * MUST NOT be repurposed for any other manifest-like payload (see “no branching semantics” posture in Build Notes by title only).

* **Recompute script** — reads the finalized manifest, verifies canonical form, recomputes `release_id`, and proves the freeze-pack identity surfaces are coherent.

  * path: `scripts/release_id_recompute.py`

  * recompute log (evidence): `artifacts/math/release_id_recompute.log`

  * **Mode semantics (normative):**

    * `--check` MUST be fail-closed (non-zero on any mismatch) and MUST NOT “self-heal” or rewrite governed artifacts.

    * Non-`--check` mode MAY rewrite governed artifacts to the canonical state and MUST exit 0 when the post-write state is clean.

    * A regression test MUST cover both modes using an isolated temp workspace (so the repo working tree is not mutated).

* **Release ID file (canonical)** — one-line `release_id` \+ LF; must be treated as the canonical recorded value for tooling and closeout wiring.

  * path: `artifacts/math/release_id.txt`

  * `audit/gates/release/release_id.txt` is deprecated and MUST NOT be used.

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

* **Release identity gate (fail-closed, closed rails)** — CI MUST run the dedicated identity gate entrypoint:  
  * path: `ci/checks/check_release_identity.sh`  
  * invocation posture (names-only): invoke as a Python entrypoint (for example `python ci/checks/check_release_identity.sh`).  
  * minimum behavior (normative):  
    * enforce closed rails,  
    * run `python scripts/release_id_recompute.py --check`,  
      assert manifest schema \+ canonical bytes posture,  
    * assert byte-equality between `catalog/manifest.json` (canonical bytes) and `artifacts/math/freeze_pack_manifest.json`, and  
    * assert the governed recompute evidence outputs exist and are non-empty.  
  * operator note (non-blocking): running the gate may rewrite `artifacts/math/release_id_recompute.log` even in `--check` mode in ephemeral CI workspaces; local operators MUST treat this as tool-driven churn and avoid committing unintended log rewrites.  
* **Pre-merge job** runs the recompute script and checksum verification; any failure is a **hard stop**.  
* **Manifest-change gate** requires updating, in the **same commit/PR**:  
  * the **human Evidence Index**: `docs/evidence/INDEX.json`,  
  * the **Evidence Index hash sentinel**: `docs/evidence/INDEX.sha256`, and  
  * the **machine mirror**: `artifacts/evidence_index.jsonl`.  
* **Two-run identity job** ensures stable bytes across two executions on the same inputs.  
* **Sentinel check:** CI fails if `docs/evidence/INDEX.sha256` does **not** match the current `INDEX.json` bytes.

### **Evidence Index entries (titles and paths only)**

* Freeze-Pack Manifest (bytes copied for evidence) — `artifacts/math/freeze_pack_manifest.json`  
* Release ID file (canonical) — `artifacts/math/release_id.txt`  
* Recompute `release_id` script — `scripts/release_id_recompute.py`  
  Recompute `release_id` log — `artifacts/math/release_id_recompute.log`  
* Checksum verification report — `artifacts/math/checksums_audit.log`  
* Manifest snapshot (release\_id, manifest sha256, count) — `artifacts/math/manifest_snapshot.json`  
* Environment pins (LC\_ALL, LANG, TZ) — `artifacts/proofs/env_pins.txt`  
* Evidence Index hash sentinel — `docs/evidence/INDEX.sha256`

### **Acceptance hints (titles only; acceptance token names live in PF04; semantics in HDE-Governance)**

`RELEASE_ID_RECOMPUTE_OK`, `RELEASE_ID_FROM_MANIFEST_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`,  
 `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `TWO_RUN_IDENTITY_OK`.

**7\. Interfaces to Other Specs (titles-only) \[Required-Now\]**

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
* Canonical JSON Gate Compare Log — `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`

**Indexing**  
 Add these to Appendix D (human) and append records to `artifacts/evidence_index.jsonl` (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a `proof_anchor` to a path-proof stored alongside the artifact).

**Environment and determinism**  
 Run with `LC_ALL=C, LANG=C, TZ=UTC` per §4.3.  
 No wall clock, no randomness, no floats.

**Acceptance hints (names-only)**  
 `TOPOLOGY_NO_ORPHANS_OK`, `TOPOLOGY_CHANNEL_DEGREE_2_OK`, `TOPOLOGY_GATE_CENTER_OK`, `DEGREE_VECTORS_MATCH_OK` (when declared), `ARR_SET_IDENTITY_DECLARED_OK`, `ARR_SET_NO_CONFLICTS_OK`, `ARR_SET_ASCII_SORT_OK`, `FILE_EQ_CANON_BYTES_OK`, `ENV_LC_ALL_C_OK`.

## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**

### **Single home and path**

**Path (fixed).**  
artifacts/evidence\_index.jsonl (there must be exactly one mirror file in the repo).

**Governed locations only.**  
Every evidence file referenced by the mirror MUST live under governed repo paths (for example, artifacts/**, docs/**). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI.

**Tracked files (no .gitignore for governed artifacts).**  
Governed evidence artifacts and their sibling path-proof transcripts (`<artifact>.path_proof.txt`) MUST NOT be ignored by .gitignore. Governed locations are expected to be tracked; using .gitignore to hide governed artifacts or their path-proofs is invalid and should be treated as a QA failure.

---

### **Format (canonical JSONL)**

**One JSON object per line.**

**Canonical JSON per §4 for each line:**

* UTF-8 (no BOM).  
* Sorted keys.  
* Compact separators.  
* Exactly one trailing \\n per line.  
* No blank lines; no trailing spaces.  
* Unknown keys are rejected (CI-blocking).

---

### **Minimum record schema (reject unknown keys)**

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

---

### **Bundle-aware extension (evidence bundles, manifests, and epic metadata)**

The minimum record schema above remains normative for all Mirror records. This section extends it to cover bundle artifacts, their manifests, and per-epic metadata without changing the core field set or canonical JSONL discipline.

#### **Allowed top-level keys and unknown-key rejection**

The Mirror still rejects unknown keys. The only allowed top-level keys for any record are:

**Core keys (required for every record):**

* artifact\_key  
* role  
* sha256  
* size\_bytes  
* produced\_at\_utc  
* discovered\_physical\_path  
* proof\_anchor

**Metadata keys (optional; may appear on any record):**

* epic\_id — a short identifier for the owning epic (for example, "HDE-EPIC020"); semantics live in HDE-Phased Epics and Glow QA Guide (titles-only).  
* record\_type — a short type label for this record (for example, "epic020\_bundle" or "epic020\_bundle\_manifest"); names are governed by local schemas and tests.  
* schema\_version — a version string for the record schema (for example, "1.0").  
* notes — free-form, names-only commentary to aid audits; contents are out of scope for PF12 beyond canonical JSON constraints.  
* `tokens` — an array-as-set of acceptance token names (strings) associated with this record; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide. Arrays treated as sets MUST be deduped and ASCII-sorted.  
* `tokens` is a non-empty array of token names tied to the EPIC020 acceptance roster; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide.

**Bundle-specific keys (optional; bundle rows only):**

* bundle\_key — a stable logical identifier for the bundle’s member family (for example, "ordering\_evidence", "sampler\_pool\_snapshots", "config\_bundles", or an epic-specific family such as "epic020\_bundles"); names are governed by local schemas and tests, not by PF12.  
* bundle\_manifest\_path — the repo-relative path to the bundle’s manifest JSON/JSONL file if the current record represents the bundle file (the manifest itself is a separate governed artifact with its own Mirror record).  
* bundle\_member\_count — an integer counting the number of logical members recorded in the manifest for this bundle.

**Non-bundle artifacts (most rows) MUST NOT include any bundle-specific keys.**  
For those rows, the allowed key set is exactly the core keys plus any applicable metadata keys above; the minimum record schema from the preceding block applies unchanged.

#### **Bundle artifacts and manifests**

A bundle artifact is a textual file (JSON/JSONL) that groups multiple logical evidence members. Its Mirror record’s artifact\_key identifies the governed bundle family (for example, "config\_bundle.fe" or a future bundle family defined in §8.6), and discovered\_physical\_path points to the bundle file under artifacts/\*\* or docs/evidence/\*\*.

A bundle manifest is a textual file (JSON/JSONL) that enumerates the bundle’s members (logical artifact\_key, member sha256, size\_bytes, and optional descriptors) and is treated as a separate governed artifact. The manifest has its own Mirror record with its own artifact\_key and discovered\_physical\_path; it MAY use bundle\_key to associate itself with the corresponding bundle artifact.

For selected bundle-based families (as defined in §8.6 and in their per-family subsections), the Human Evidence Index and Machine Evidence Mirror track the bundle file and its manifest as the governed artifacts instead of listing every internal member file as a separate row. Internal member content is addressed by the manifest, not directly by additional Mirror rows.

#### **EPIC-scale example (EPIC020 Candidate 1 bundles)**

EPIC020 Candidate 1 evidence bundles follow this pattern:

* Each EPIC020 bundle and manifest has a Mirror record whose artifact\_key is the relevant EPIC020 token (for example, "EPIC020.D1.HTTP\_COMPAT\_MALFORMED\_JSON" or CLI\_SHOWCOMPAT\_CANON\_OK).  
* record\_type is "epic020\_bundle" for bundle artifacts and "epic020\_bundle\_manifest" for manifests.  
* epic\_id is "HDE-EPIC020".  
* tokens is a non-empty array of token names tied to the EPIC020 acceptance roster; schema and ownership of token names live in HDE-Governance and Glow QA Guide.

Other epics may introduce similar patterns with different record\_type and epic\_id values; PF12 remains the single home for the allowed key set and canonical JSONL constraints, while per-epic meaning is defined by PF04/PF19/PF20.

#### **Path-proof semantics for bundles**

Each bundle artifact and its manifest MUST have governed sibling path-proof transcripts (`<bundle_file>.path_proof.txt` and `<manifest_file>.path_proof.txt`) stored alongside each file, whose `path`, `sha256`, and `size_bytes` match the bundle/manifest file and the corresponding Mirror record values.

For bundle-based families, “per-artifact path proofs” in PF12 are interpreted as “per governed artifact,” where a governed artifact may be either:

* a single artifact file (e.g., a log or JSON snapshot), or  
* a bundle artifact or bundle manifest file.

This extension does not introduce hash-only or index-only families. Any future move toward hash-only evidence (no on-disk member payloads) remains out of scope here and requires an explicit reconciliation Doc-Delta (tracked as an OPEN decision in §0.5).

All other Mirror rules remain unchanged: canonical JSONL per §4, single mirror file at artifacts/evidence\_index.jsonl, sort-before-write by (artifact\_key, discovered\_physical\_path), uniqueness of that pair, strict governed-paths rule, and 1:1 parity with the Human Evidence Index.

---

### **Self-record semantics (index.machine\_mirror)**

The mirror MAY include a single record whose artifact\_key identifies the Machine Evidence Mirror itself (for example, "index.machine\_mirror"). This is the self-record for artifacts/evidence\_index.jsonl.

For this self-record:

* sha256 MUST equal the SHA-256 digest of the mirror’s canonical JSONL body excluding the self-record line.  
* size\_bytes MUST equal the byte length of the complete artifacts/evidence\_index.jsonl file including the self-record line.  
* The associated path-proof transcript for artifacts/evidence\_index.jsonl MUST contain exactly one sha256/size\_bytes pair and those values MUST match the self-record’s sha256 and size\_bytes.

All other mirror records (non self-records) follow the normal mirror discipline: sha256 and size\_bytes are for the referenced artifact at discovered\_physical\_path, and their path-proof transcripts must match those values (see “Path-proof transcript schema”).

---

### **Field order and write discipline (merge-blocking)**

**ASCII field order (exact):**  
artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes.

**Sort-before-write** by the tuple (artifact\_key, discovered\_physical\_path).

**Uniqueness:** the pair (artifact\_key, discovered\_physical\_path) is unique; duplicates fail CI.

**Single mirror file:** only one artifacts/evidence\_index.jsonl may exist in the repo.

---

### **produced\_at\_utc vs mtime\_utc**

produced\_at\_utc records when the evidence was logically produced (the event time). It is part of the mirror record and is used to reason about when posture snapshots and QA runs occurred.

mtime\_utc is recorded in the per-artifact sibling path-proof transcript (`<artifact>.path_proof.txt`) as the filesystem modification time for the artifact.

Differences between produced\_at\_utc and mtime\_utc are allowed but must be truthful — no “backdating” or forward-dating to distort ordering. QA may rely on produced\_at\_utc as the primary ordering key for evidence; disagreements should be rare and explainable in the PR.

---

### **Path-proof transcript schema (governed artifacts)**

**Naming (MUST).** The sibling path-proof transcript for a governed artifact MUST be named `<artifact>.path\_proof.txt`, where `<artifact>` includes the artifact’s full filename including extension. Example: `audit/gates/determinism/env\_pins.log` → `audit/gates/determinism/env\_pins.log.path\_proof.txt` (not `env\_pins.path\_proof.txt`).

For every governed artifact in §8.6, the path-proof transcript MUST be a co-located sibling file named `<artifact>.path_proof.txt`. It MUST describe exactly one artifact and follow a stable, line-oriented schema.

#### **Required fields (exactly one record per file)**

Each path-proof MUST contain exactly one record for the artifact it describes, with the following required fields:

* path — repo-relative path to the artifact (for example artifacts/engine/order/channels\_sorted.snapshot.json).  
* sha256 — lowercase 64-hex SHA-256 digest of the artifact’s canonical bytes.  
* size\_bytes — non-negative integer byte length of the artifact’s canonical bytes.  
* mtime\_utc — UTC ISO-8601 timestamp (e.g. YYYY-MM-DDThh:mm:ssZ) representing the artifact’s refresh-time mtime (see “mtime\_utc semantics” below).  
* produced\_at\_utc — UTC ISO-8601 time when the evidence for this artifact was logically produced.

These fields MUST appear exactly once per file; path-proofs MUST NOT contain multiple or conflicting sha256/size\_bytes pairs, nor multiple mtime\_utc or produced\_at\_utc values for the same artifact.

#### **Optional fields**

Path-proof transcripts MAY include additional informational fields beyond the required set above, but those fields:

* MUST NOT change acceptance semantics, and  
* MUST NOT conflict with the required record for path, sha256, size\_bytes, mtime\_utc, or produced\_at\_utc.

The authoritative truth remains the match between:

* the artifact’s canonical bytes,  
* the mirror record’s sha256 and size\_bytes, and  
* the path-proof’s single sha256/size\_bytes triple for that artifact.

#### **Relationship to proof\_anchor**

Each mirror record’s proof\_anchor field MUST equal the path to the corresponding .path\_proof.txt for that artifact.

CI MUST verify that:

* the file referenced by proof\_anchor exists under governed paths,  
* its path matches the mirror’s discovered\_physical\_path,  
* its sha256/size\_bytes match the mirror record’s sha256/size\_bytes, and  
* there are no duplicate or conflicting sha256/size\_bytes entries within the path-proof.

Failure of any of these conditions is a hard error under the mirror/index tokens declared in §8.3 and §0.2.

---

### **mtime\_utc semantics (normative)**

#### **Refresh-time mtime**

mtime\_utc records the artifact’s refresh-time mtime: the filesystem modification time observed when the evidence job refreshed that artifact, encoded as a UTC ISO-8601 timestamp (YYYY-MM-DDThh:mm:ssZ) with no fractional seconds (microsecond component MUST be zero).

#### **Monotone vs filesystem stat()**

On any run that writes or checks a path-proof, the evidence tooling MUST verify that mtime\_utc parses as UTC (with microsecond \== 0\) and that parsed\_mtime \<= current\_fs\_mtime, where current\_fs\_mtime is the artifact’s stat().st\_mtime observed at check time.

mtime\_utc is not required to be exactly equal to stat().st\_mtime; it is permitted to be earlier (for example, when a proof is refreshed without the underlying file changing) but MUST NOT lie in the future relative to the current filesystem mtime.

#### **Interaction with produced\_at\_utc**

produced\_at\_utc captures when the evidence for the artifact was logically produced (the evidence refresh event). It is also a UTC ISO-8601 timestamp and may be updated on each refresh or left unchanged when appropriate.

It is expected, but not strictly required, that produced\_at\_utc be greater than or equal to prior produced\_at\_utc values for the same artifact; any non-monotone behavior should be rare and explained in the PR.

#### **Integrity semantics**

The primary integrity check for governed evidence remains the equality of sha256 and size\_bytes between:

* the artifact’s canonical bytes on disk,  
* the Machine Mirror record (§8.3), and  
* the single record in the path-proof transcript.

mtime\_utc and produced\_at\_utc provide temporal context and are enforced for format and monotone constraints as described above; they do not replace the sha/size equality as the core integrity proof.

#### **Alignment with tools and QA**

Evidence tooling (tools/evidence/update\_evidence\_index.py) and CI checks (ci/checks/check\_mirror\_schema.sh) MUST implement these semantics:

* when writing path-proofs, always recompute size\_bytes and sha256 from the artifact’s canonical bytes;  
* set or carry forward mtime\_utc as the refresh-time mtime, and validate that it is a UTC ISO timestamp with microsecond \== 0 and mtime\_utc \<= current\_fs\_mtime;  
* set or carry forward produced\_at\_utc as the evidence refresh time.

Evidence tests (for example, tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py) MUST assert these same semantics (format \+ monotone \<= stat\_mtime) and MUST be kept in sync with this section.

#### **Change control**

Any change to the definition or validation of mtime\_utc or produced\_at\_utc semantics is a normative change and requires:

* a PF12 Doc-Delta (§9),  
* synchronized updates to PF19 (Glow QA Guide) and PF10 Build Notes, and  
* updates to the evidence tooling and tests that enforce these semantics.

---

### **Join to the human index (parity, proofs, same-PR rule)**

**1:1 parity.**  
Every §8.6 Evidence Index entry has exactly one mirror record, and every mirror record has a corresponding human entry:

* artifact\_key equals the Human Index title.  
* discovered\_physical\_path equals the Human Index path.

**Path-proofs.**  
Each artifact’s directory contains a stored path-proof (for example, path\_proof.txt with a stat transcript). The mirror record’s proof\_anchor must exactly match the stored path-proof for that artifact.

**Same-PR rule.**  
For every governed artifact in §8.6, any change to the artifact MUST update, in the same PR:

* The artifact bytes on disk under a governed path.  
* Its sibling `<artifact>.path_proof.txt` path-proof transcript (the `proof_anchor` target).  
* The corresponding machine mirror record in artifacts/evidence\_index.jsonl.  
* The Human Evidence Index entry in docs/evidence/INDEX.json and its hash sentinel docs/evidence/INDEX.sha256.

Mirror or index entries that refer to non-existent artifacts or stale path-proofs are invalid and must be corrected, not ignored.

**Troubleshooting (common failure mode): governed artifact drift**

A governed artifact is considered **drifted** when any of the following disagree:

* the artifact’s on-disk bytes,

* its sibling `*.path_proof.txt` (`sha256` and `size_bytes`), and

* the corresponding Machine Mirror record (`sha256` and `size_bytes` for the same `discovered_physical_path`).

This is a hard evidence integrity failure. Do not hand-edit proofs or mirror records to “make the check pass”.

**Correct remediation (single writer):**

Re-generate the evidence skeleton using the canonical evidence tooling so all three surfaces realign:

1. Ensure `docs/evidence/INDEX.json` reflects the intended titles and paths.

2. Run `tools/evidence/update_evidence_index.py` in write mode to regenerate:

   * `docs/evidence/INDEX.sha256`,

   * `artifacts/evidence_index.jsonl`, and

   * all governed `*.path_proof.txt` transcripts.

3. Re-run the tool in `--check` mode and fix any remaining mismatches before merge.

---

### **Determinism**

All checks run with LC\_ALL=C, LANG=C, TZ=UTC.

JSONL records are canonical and LF-terminated (exactly one \\n per record).

---

### **Header snapshots in artifacts (normative)**

For artifacts that capture headers, header names MUST be lower-case and values MUST be verbatim; exact checks apply to values.

**Capture hygiene (normative).**

* Header snapshot artifacts MUST contain header lines only.

* Tool warnings or stderr output (for example, curl warnings) MUST NOT be mixed into header snapshot bytes.

* If the capture command can emit warnings, capture stderr separately (for example, to a sibling `*.stderr.txt` or a step log) or filter non-header lines before writing the governed artifact.

Wire casing may differ and is validated by transport owners.

Acceptance hint (names-only): SNAPSHOT\_HEADER\_LOWERCASE\_OK.

---

### **Refusal proofs (policy note)**

Refusal proofs are error/ops evidence (not JSON success). They must:

* Not set ETag, Vary, or compression headers.  
* Use Content-Type: application/json; charset=utf-8.

The refusal log allow-list for JSON body fields is exactly:  
{at, route, status, duration\_ms, idempotence\_hash, release\_id}

Records with any additional fields fail policy checks.

Rate-limit (429) evidence uses a different allow-list and is governed by HDE-Governance. Do not mix refusal and 429 fields in the mirror.

---

### **Refresh sequence (normative)**

When governed evidence artifacts change, the canonical refresh sequence is:

* Update docs/evidence/INDEX.json with the new or changed titles and paths.

* Run python tools/evidence/update\_evidence\_index.py in write mode to regenerate docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, and all governed \*.path\_proof.txt transcripts.

* Run the mirror schema/shape check job (canonical CI invocation: `ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`) and fix any discrepancies before merge.

**Operator note (invocation; avoid bash drift).**  
 `ci/checks/check_mirror_schema.sh` is a **Python entrypoint** (script file with a Python shebang) and CI invokes it directly. When an acceptance artifact or runbook needs an explicit command, the canonical invocation is:

* `ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

Acceptance artifacts may list either:

* the script path (`ci/checks/check_mirror_schema.sh`) as a **tool reference**, or

* the explicit direct command above as an **invocation**,

but `bash ci/checks/check_mirror_schema.sh` is invalid and MUST NOT appear in approved acceptance artifacts or operator instructions.

Process and PR workflow (who runs which command and when) remains single-homed in Epic-Process-Guide; this section pins file-level ordering and artifacts that MUST be updated together.

---

### **Role usage notes (non-normative examples)**

* proof → artifacts/db/ddl\_fingerprint.json, artifacts/proofs/endpoints\_env\_gate\_proof.log, artifacts/bodygraph/source\_invariance/ab.json, /ba.json, /summary.json  
* golden → catalog/manifest.json, catalog/schemas/\*.json  
* snapshot → artifacts/runtime/env\_matrix.snapshot.json, artifacts/reader/endpoints\_snapshot.json, artifacts/bodygraph/refresh\_policy.snapshot.json, artifacts/bodygraph/metrics.snapshot.json  
* script → scripts/card\_close.sh, scripts/migration\_runner.sh  
* log → artifacts/db/migration\_runner.log, artifacts/proofs/headers\_probe.log, artifacts/bodygraph/keys\_only.logs.sample (sanitized; keys-only, no PII per Governance)

---

### **Artifacts with generated\_at\_utc (provenance discipline, including sampler and Engine Core evidence)**

Some governed artifacts (for example, sampler evidence artifacts under artifacts/sampler/\*\* and Engine Core evidence artifacts under artifacts/core/\*\*) include a generated\_at\_utc field in their own JSON payloads. For these artifact families, provenance discipline tightens the relationship between the payload timestamp and the evidence timestamps recorded in the Machine Mirror and path-proofs.

#### **Normative rules (in addition to the general rules in this section)**

When an artifact carries a generated\_at\_utc field in its payload, the evidence tooling MUST treat that field as the artifact’s self-reported generation time for the current refresh and enforce all of the following:

* produced\_at\_utc in the Machine Evidence Mirror record for that artifact MUST NOT be earlier than the artifact’s generated\_at\_utc value. Backdating Mirror produced\_at\_utc relative to generated\_at\_utc is not allowed.  
* produced\_at\_utc in the Machine Evidence Mirror record and produced\_at\_utc in the artifact’s path-proof transcript MUST be identical strings (same UTC ISO-8601 representation). Mirror and path-proof timestamps MUST stay in lockstep for a given artifact.  
* mtime\_utc in the path-proof remains the refresh-time filesystem mtime (see “mtime\_utc semantics” above) and MUST NOT be later than the artifact’s current filesystem stat().st\_mtime at check time. mtime\_utc may be earlier than generated\_at\_utc (for example, when an artifact’s content has not changed between runs but evidence is refreshed), but sha256 and size\_bytes MUST still match.

For governed families that include both generated\_at\_utc and produced\_at\_utc (including the sampler families registered in §8.6.3 and the Engine Core families engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, and engine\_core\_json\_compare\_logs), provenance correctness for a given refresh requires:

* the artifact’s payload generated\_at\_utc and the Mirror produced\_at\_utc to describe the same refresh window (produced\_at\_utc ≥ generated\_at\_utc in UTC time), and  
* the path-proof produced\_at\_utc to match the Mirror produced\_at\_utc exactly.

Integrity gates for these artifacts continue to rely primarily on sha256 and size\_bytes equality across artifact, Mirror record, and path-proof. Timestamp checks are additive: format, monotonicity (per “mtime\_utc semantics”), and the non-backdating rule relative to payload generated\_at\_utc are enforced in addition to the existing sha/size equality rules.

#### **Example — sampler and Engine Core evidence fixes (HDE-EPIC019)**

In earlier EPIC019 work, sampler Mirror records and path-proofs for sampler\_pool\_snapshots, sampler\_two\_run\_logs, sampler\_abba\_logs, sampler\_diversity\_artifacts, and sampler\_seed\_replay\_logs carried produced\_at\_utc values copied from an older skeleton baseline even after the artifacts themselves were regenerated with later generated\_at\_utc timestamps. Engine Core evidence families added in PR7 (engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, engine\_core\_json\_compare\_logs) were wired with generated\_at\_utc and closed-rails env metadata from the start.

The EPIC019 bugfix refreshed Mirror records and path-proofs so that:

* sampler artifacts under artifacts/sampler/\*\* and Engine Core artifacts under artifacts/core/\*\* retain canonical bytes (sha256 and size\_bytes unchanged when content is unchanged),  
* their payload generated\_at\_utc values reflect the actual regeneration time for the latest evidence run, and  
* produced\_at\_utc in both Mirror and path-proofs is updated to the later refresh time, satisfying the non-backdating rule above and restoring consistency between payload generation timestamps and evidence timestamps for all families that carry generated\_at\_utc.

#### **Tools and tests**

Evidence tooling (for example, tools/evidence/update\_evidence\_index.py and any Engine Core/sampler-specific generators) and Mirror schema checks MUST implement these provenance rules whenever an artifact family introduces a payload-level generated\_at\_utc field.

Tests that exercise those families (for example, sampler evidence tests under tests/evidence/ and Engine Core evidence tests under tests/evidence/test\_engine\_core\_evidence.py) SHOULD assert that:

* produced\_at\_utc in Mirror and path-proofs matches for each artifact instance, and  
* where generated\_at\_utc is present, Mirror produced\_at\_utc is not earlier than payload generated\_at\_utc.

#### **Change control**

Any change to the relationship between payload generated\_at\_utc and evidence produced\_at\_utc semantics is a normative change and MUST land with:

* a PF12 Doc-Delta (§9),  
* synchronized updates to the relevant Mechanics/QA specs that describe Engine Core and sampler evidence behavior, and  
* synchronized changes to the evidence tools and tests that enforce these semantics before the change is considered accepted.

---

## **8.3.1 Refusal proof (single-file canonical) \[Required-Now\]**

### **Path (fixed)**

artifacts/proofs/ops\_refusal\_proof.txt — single-file refusal:

* Header block.  
* One blank line.  
* LF-terminated JSON body.

Index this file in both docs/evidence/INDEX.json (human) and artifacts/evidence\_index.jsonl (machine) in the same PR.

Include a co-located path\_proof.txt and reference it via proof\_anchor in the mirror.

Policy and tokens live in HDE-Governance (titles only).

### **Purpose**

Capture a refusal response verbatim (headers \+ JSON body) for ops/evidence.

This is not a JSON success route.

### **File format (exact)**

The file consists of:

* A header block.  
* Exactly one blank line.  
* A JSON body.

The file ends with exactly one \\n.

#### **Header block**

One header per line, format: : .

Required header:

* content-type: application/json; charset=utf-8

Forbidden headers: etag, vary, content-encoding.

Other headers may appear as governed elsewhere (for example, date).

Header names are lower-case; values are verbatim. Order is preserved as captured.

#### **Separator**

Exactly one blank line (a single \\n) between headers and body.

#### **Body (JSON, single line)**

Canonical JSON per §4:

* UTF-8.  
* Sorted keys.  
* Compact separators.  
* One trailing \\n.

Fields must conform to the refusal allow-list:  
{at, route, status, duration\_ms, idempotence\_hash, release\_id}

Unknown keys fail policy checks.

### **Mirror linkage**

The mirror record uses role:"log" and must point to this file via discovered\_physical\_path.

The artifact directory also contains a path\_proof.txt stat transcript; the mirror proof\_anchor must exactly match that path-proof entry.

### **Validation checks (CI)**

* File ends with exactly one \\n.  
* Headers lower-case; required header present; forbidden headers absent.  
* Exactly one blank line between headers and body.  
* Body is single-line canonical JSON with the refusal allow-list only.  
* Determinism: checks run with LC\_ALL=C, TZ=UTC.

### **Example (illustrative)**

content-type: application/json; charset=utf-8

date: 2025-11-07T21:00:00Z

{"at":"2025-11-07T21:00:00Z","route":"/ops/rails/refusal","status":503,"duration\_ms":12,"idempotence\_hash":"\<64-hex\>","release\_id":"\<64-hex\>"}

### **Acceptance hints (titles-only; tokens live in HDE-Governance)**

OPS\_REFUSAL\_FILE\_FORMAT\_OK  
OPS\_REFUSAL\_HEADERS\_OK  
OPS\_REFUSAL\_BODY\_OK  
OPS\_REFUSAL\_MIRROR\_LINK\_OK

---

## **8.3.2 Environment matrix snapshot (singleton, v3) \[Required-Now\]**

### **Path (fixed)**

artifacts/runtime/env\_matrix.snapshot.json — one file per repo (singleton).

### **Purpose**

Record the default rails posture and determinism pins across environments, as captured by the build/test harness.

HDE-Governance owns policy and tokens; Glow-Infrastructure lists names-only env inventory; PF12 owns this artifact’s schema and indexing.

### **Schema (v3; reject unknown keys)**

Canonical JSON per §4 (UTF-8; sorted keys; compact; exactly one LF).

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

### **Field rules**

* Uppercase rails keys (SAFE\_MODE, ALLOW\_NETWORK) and env names as shown.  
* schema\_version MUST equal 3\.  
* presence.\*.present are booleans indicating whether the variable (or prod guard) is set at capture time; do not record secrets or values.  
* notes is optional (short strings; no secrets).

### **Indexing (both indices; same PR)**

Add a titles/paths entry in §8.6 and a mirror record (role:"snapshot") in artifacts/evidence\_index.jsonl with proof\_anchor to a co-located path\_proof.txt (stat transcript).

Mirror schema and “single mirror file” rule are per §8.3.

### **Acceptance hints (names-only; tokens live in HDE-Governance)**

ENV\_RAILS\_POLICY\_OK  
ENV\_LC\_ALL\_C\_OK  
EVIDENCE\_INDEX\_UPDATED\_OK  
CI\_CHECK\_FINAL\_LF\_OK  
CI\_CHECK\_MIRROR\_SCHEMA\_OK

### **Routing (titles-only)**

Policy and refusal semantics → HDE-Governance.  
Env inventory → Glow-Infrastructure.

---

## **8.3.3 Determinism env\_pins log (audit.determinism.env\_pins) Required-Now**

### **Purpose**

This log is the canonical record of determinism-related environment rails/pins that govern evidence production and verification. It MUST capture the exact “closed rails” posture values (LC\_ALL/LANG/TZ/SAFE\_MODE/ALLOW\_NETWORK) used during the run.

### **Canonical path (single home)**

audit/gates/determinism/env\_pins.log

### **Role and artifact\_key**

* Role: determinism pins proof surface (governed)

* artifact\_key: audit.determinism.env\_pins

### **File format**

The file MUST be a single-line canonical JSON object with exactly the top-level keys `schema`, `rails`, `status`, `suites`, `notes`. Unknown keys are rejected.

* `schema` MUST be the string `"determinism_env_pins.v1"`. Unknown schema values are rejected.

* `rails` MUST be a JSON object.

* `status` MUST be a string (recommended values: `success`, `fail`).

* `suites` MUST be a non-empty array of suite names (strings).

* `notes` MUST be an array of strings; it MAY be empty.

The `rails` object:

* MUST be a JSON object of pinned values.

* At minimum, the `rails` object MUST include:

  * `LC_ALL` (string)

  * `LANG` (string)

  * `TZ` (string)

  * `SAFE_MODE` (integer 0 or 1\)

  * `ALLOW_NETWORK` (integer 0 or 1\)

* The values MUST match the expected determinism pins and closed-rails posture. Specifically:

  * `LC_ALL` MUST be `"C"`

  * `LANG` MUST be `"C"`

  * `TZ` MUST be `"UTC"`

  * `SAFE_MODE` MUST be `1`

  * `ALLOW_NETWORK` MUST be `0`

* `SAFE_MODE` and `ALLOW_NETWORK` MUST be numeric JSON integers (0/1), not strings.

The file MUST end with exactly one trailing LF. It MUST NOT include a BOM.

### **Environment and determinism**

Generation and checks for downstream governed artifacts MUST run under the determinism pins asserted in the log’s `rails` object:

* LC\_ALL=C

* LANG=C

* TZ=UTC

* SAFE\_MODE=1

* ALLOW\_NETWORK=0

### **Indexing and proof anchoring**

This file is a governed surface and MUST be indexed and mirrored:

* Evidence Index entry MUST point to `audit/gates/determinism/env_pins.log`.

* A proof anchor MUST be written to the Machine Evidence Mirror record in `artifacts/evidence/machine_mirror.json`, with a `proof_anchor` pointing to `audit/gates/determinism/env_pins.log.path_proof.json` and a stable `sha256` reflecting bytes.

### **Acceptance hints**

* Token hint: `DETERMINISM_ENV_PINS_OK` is satisfied when:

  * `audit/gates/determinism/env_pins.log` exists and is valid canonical JSON,

  * `schema` is `"determinism_env_pins.v1"`,

  * `rails` includes the determinism pins and matches closed-rails posture (LC\_ALL/LANG/TZ as strings; SAFE\_MODE/ALLOW\_NETWORK as integer 0/1),

  * and the Evidence Index \+ Machine Evidence Mirror reflect the same bytes with a path-proof sibling.

---

## **8.3.4 Sanity pipeline log (sanity.pipeline.log) \[Required−Now\]**

### **Purpose**

This is the canonical output of the sanity pipeline that validates deterministic serialization and core invariants for governed artifacts. It provides a stable, minimal, line-oriented PASS/FAIL summary suitable for indexing and closure proofs.

### **Canonical path (single home)**

artifacts/sanity/sanity.log

### **Role and artifact\_key**

* Role: deterministic sanity proof surface (governed)

* artifact\_key: sanity.pipeline.log

### **File format**

The file MUST be a UTF-8 text file with LF line endings. It MUST contain only ASCII characters and the following exact structure:

1. **Header line** (exact):  
    `run:sanity-pipeline`

2. **Environment pins reference line** (exact):  
    `env_pins: audit/gates/determinism/env_pins.log`

3. **Step lines** (zero or more):  
    `check <name>:(OK|FAIL)`  
    Where `<name>` MUST be an ASCII token (recommended: `[a-z0-9_]+`).

4. **Summary line** (exact prefix):  
    `summary:(PASS|FAIL)`

Additional format rules:

* The log MUST be non-empty.

* The header line and env\_pins reference line MUST appear exactly once each.

* The summary line MUST appear exactly once and MUST be the final line in the file.

* If any step line is `FAIL`, the summary MUST be `summary:FAIL`.

* If the summary is `summary:PASS`, all step lines (if any) MUST be `OK`.

* The log MUST NOT embed timestamps, UUIDs, hostnames, or other nondeterministic values.

* The log MUST NOT embed environment pin values inline; determinism pins are proven via the referenced `audit/gates/determinism/env_pins.log`.

Example (minimal conformant):

`run:sanity-pipeline`

`env_pins: audit/gates/determinism/env_pins.log`

`summary:PASS`

Example (with steps):

`run:sanity-pipeline`

`env_pins: audit/gates/determinism/env_pins.log`

`check serializer:OK`

`check canonical_json:OK`

`summary:PASS`

### **Environment and determinism**

Generation and checks for `artifacts/sanity/sanity.log` MUST run under the determinism pins proven by `audit/gates/determinism/env_pins.log` (and referenced by the required `env_pins:` line in this log).

### **Indexing and proof anchoring**

This file is a governed surface and MUST be indexed and mirrored:

* Evidence Index entry MUST point to `artifacts/sanity/sanity.log`.

* A proof anchor MUST be written to the Machine Evidence Mirror record in `artifacts/evidence/machine_mirror.json`, with a `proof_anchor` pointing to `artifacts/sanity/sanity.log.path_proof.json` and a stable `sha256` reflecting bytes.

### **Acceptance hints**

* Token hint: `SANITY_PIPELINE_OK` is satisfied when:

  * `artifacts/sanity/sanity.log` exists and matches the required structure (including `run:sanity-pipeline`, `env_pins: audit/gates/determinism/env_pins.log`, and `summary:PASS`),

  * and the Evidence Index \+ Machine Evidence Mirror reflect the same bytes with a path-proof sibling.

## **8.4 Human Evidence Index (titles/paths only)**

**Single home and format**

* Path: `docs/evidence/INDEX.json`.

* Canonical JSON per §4 (titles/paths only; no payload bytes).

* Used for human review; must maintain 1:1 parity with the machine JSONL mirror in §8.3.

**Shape and normalization.**  
 `INDEX.json` stores an array of `{artifact_key, discovered_physical_path}` objects. Before render, duplicate `(artifact_key, discovered_physical_path)` pairs **MUST** be deduplicated, and the array **MUST** be ASCII-ascending first by `artifact_key` and then by `discovered_physical_path` (byte-wise, locale-independent). The hash sentinel `docs/evidence/INDEX.sha256` is computed over the canonical bytes of `INDEX.json` and **is not** mirrored into `artifacts/evidence_index.jsonl`; it is a Human Index–only guard.

Both `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` have required co-located governed path-proof transcripts (`*.path_proof.txt`) that MUST be refreshed whenever their bytes change (same PR). See §8.4.

### **Governed path-proofs (Index and hash sentinel)**

`docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` are **governed artifacts** even though they are not listed as entries inside `docs/evidence/INDEX.json` and are not represented as ordinary mirror records.

**Required path-proof transcripts (co-located):**

* `docs/evidence/INDEX.json.path_proof.txt` — MUST exist and MUST match the exact on-disk bytes of `docs/evidence/INDEX.json` (sha256 and size\_bytes), using the path-proof schema and timestamp semantics defined in §8.3.

* `docs/evidence/INDEX.sha256.path_proof.txt` — MUST exist and MUST match the exact on-disk bytes of `docs/evidence/INDEX.sha256` (sha256 and size\_bytes), using the same path-proof schema and timestamp semantics defined in §8.3.

**Refresh rule (same PR, non-optional):**

Whenever either `docs/evidence/INDEX.json` or `docs/evidence/INDEX.sha256` changes bytes, its corresponding `*.path_proof.txt` MUST be refreshed in the **same PR**. Stale proofs for `INDEX.json` or `INDEX.sha256` are treated as evidence integrity failures.

**Tooling expectation (single writer):**

The canonical evidence tool (`tools/evidence/update_evidence_index.py`) is expected to refresh these two path-proofs during normal runs and MUST fail in check mode if either proof is missing or stale.

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

**Purpose.** Names-only, records-only summary of the configuration registry for a given cut. This artifact is used by CI and auditors to prove that the registry catalogs and manifest are internally consistent, and that alias policy is enforced as configured. It contains **no secrets** and **no raw payload values**.

**Path (single home).**  
 `artifacts/registry/registry_report.json` (fixed).

**Canonical JSON & schema.**

* Canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Top-level object **MUST** use at least the following keys; unknown top-level keys are rejected:

  * `schema` — string, **MUST** equal `"registry_report.v1"`.

  * `generated_at_utc` — string. UTC ISO-8601 timestamp (`YYYY-MM-DDThh:mm:ssZ`).

  * `inputs` — object. Names-only descriptions of upstream sources (titles and paths for catalogs, manifest, and environment inputs).

  * `artifacts` — object. Contains at least one member `registry` (see below).

  * `notes` — array of strings (optional; short internal comments only, no secrets).

**Generated-at stability.**

* `generated_at_utc` is intended to be **stable across two runs** unless the environment explicitly opts into new timestamps (for example, via `SOURCE_DATE_EPOCH` or an equivalent mechanism).

* Tools **SHOULD** reuse the existing `generated_at_utc` from a prior report when regenerating in a determinism-pinned environment and no inputs have changed.

**`artifacts.registry` shape (names-only summary).**

`artifacts.registry` **MUST** be present and is a names-only summary of registry state. At minimum, it **MUST** contain:

* `channel_ids` — array of strings. Canonical channel IDs (`NN-NN`) drawn from the Channels catalog; arrays-as-sets discipline from §4.2 applies (deduped, ASCII-sorted).

* `gate_centers` — object mapping gate IDs (1..64 as strings) to center IDs (`head, ajna, throat, g_center, ego, spleen, sacral, solar_plexus, root`). Names-only; values must match the topology catalogs.

* `centers` — array of center IDs (closed domain from §2.1).

* `domains` — array of domain/category labels used by the registry (names-only).

* `domain_counts` — object mapping domain labels to **non-negative integers** (counts of channels per domain).

* `magic10` — object summarizing Magic-10 registry state:

  * `order` — array of the ten Magic-10 category IDs (normative order, names-only).

  * `seeds` — names-only summary keyed by category ID; may include `seed_version` or other admin-only identifiers.

  * `caps` — object keyed by category ID with integer caps, when present (names-only; values must match `catalog/magic10.json` and any related caps catalog).

* `alias_policy` — object describing alias behavior:

  * `mode` — string, one of `"off"` or `"allow_list"`. `"off"` means alias entries are not accepted; `"allow_list"` means they are accepted only when explicitly configured.

  * `aliases` — object mapping alias IDs (strings) to canonical channel IDs (strings) when `mode:"allow_list"`; keys and values are names-only; any alias included here **must** correspond to validated catalog entries.

Implementation details (how these fields are computed, or where the aliases ledger lives) are out of scope for this document; they live in Mechanics and QA. PF12 only governs the **shape**, **names-only content**, and canonical JSON requirements.

**Indexing (titles/paths only).**

* **Machine mirror.** Every registry\_report instance **MUST** have a corresponding record in `artifacts/evidence_index.jsonl` with:

  * `artifact_key` (for example `"registry.registry_report"`),

  * `role:"snapshot"`,

  * `discovered_physical_path:"artifacts/registry/registry_report.json"`,

  * `sha256`,

  * `size_bytes`,

  * `produced_at_utc`,

  * `proof_anchor` (path to `artifacts/registry/registry_report.json.path_proof.txt` stored alongside the JSON file).

* **Human index.** Add a titles/paths-only entry in `docs/evidence/INDEX.json` with the same artifact\_key/title and path. Update `docs/evidence/INDEX.sha256` in the **same PR**.

Mirror records **MUST** obey §8.3 (canonical JSONL; one LF; unknown-key rejection; ASCII field order; sort-before-write; single mirror file; governed paths only; path-proofs present).

**Acceptance hints (titles-only; tokens live in HDE-Governance §2.0).**

* `REGISTRY_REPORT_OK` — registry\_report present, canonical JSON, and indexed.

* `EVIDENCE_INDEX_UPDATED_OK` — human/machine parity updated in the same PR.

* `EVIDENCE_INDEX_HASH_OK` — human index hash sentinel matches `INDEX.json` bytes.

* `EVIDENCE_PATHS_VALIDATED_OK` — mirror record has `proof_anchor` to a matching path-proof.

* `EVIDENCE_INDEX_MIRROR_OK` — mirror schema and self-record semantics are satisfied per §8.3 and §0.2.

**Generation & env rails.**  
 `registry_report.v1` is generated by the typed loader (tools/generate\_registry\_report.py) under the closed-rails profile used for evidence jobs (`SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC`). The report is names-only and **MUST NOT** contain secrets or raw payload values.

**ID and alias semantics.**  
 During generation, unknown IDs and enum values from the catalogs fail closed: the loader **MUST** reject any ID or enum value that is not a member of the closed domains defined in §3.3. Where alias catalogs are present, aliases are resolved to canonical IDs **before** validation and emission, and the report records only canonical IDs. Aliases remain input-only; all outputs are canonical, per §3.3.

**Determinism tests.**  
 Registry report generation participates in the global determinism contract: two successive runs over the same inputs **MUST** produce byte-identical `registry_report.v1` documents. CI tests **MUST** assert both canonical JSON (§4) and two-run identity for this artifact; failures are hard errors and block merge.

## **8.6 Evidence Index entries (titles/paths only) \[Required-Now\]**

### **8.6.1 Discipline**

* Update both the Human Index and the Machine Mirror **in the same PR**:

  * Human Index: `docs/evidence/INDEX.json`

  * Machine Mirror: `artifacts/evidence_index.jsonl`

* Machine Mirror discipline:

  * Records-only JSONL

  * Canonical JSONL

  * Exactly one LF per record

  * Unknown-key rejection

  * ASCII field order

  * Sort-before-write

  * Single mirror file

  * `proof_anchor` present and valid for every record

* Process and CI posture:

  * Detailed PR/workflow process is defined in **Epic-Process-Guide** (titles-only).

  * Acceptance sentinel gating behavior is defined in PF12 front-matter and **Governance** (titles-only).

**Canonical evidence-path binding validation (MUST).**

When any acceptance token is claimed as satisfied (in an Epic Plan, acceptance map/manifest, or token\_evidence\_matrix), every token→evidence binding **MUST** be validated against PF12’s Evidence Catalog and any fixed canonical paths it defines.

* If the Evidence Catalog defines a fixed canonical path for a token’s evidence surface, then the Plan/matrix/acceptance artifacts **MUST** bind to that exact path.

* Any binding to a non-canonical path is a **mechanical blocker** and **MUST** be corrected before approval/merge. If a non-canonical path is truly required, it MUST be routed via an explicit decision process and drained into the correct canonical home; do not silently substitute paths.

**Primary evidence vs path-proof transcripts (clarification).**

Acceptance artifacts (Epic Plans, acceptance maps/manifests, token/evidence matrices) MUST bind tokens to the primary governed artifact paths listed in the Evidence Catalog.

* `*.path_proof.txt` files are required integrity transcripts. They MUST exist and stay in sync, but they are not primary evidence targets.  
* Therefore, acceptance artifacts MUST NOT bind tokens directly to `*.path_proof.txt` as their evidence surface. The only approved linkage to a path-proof is via the Machine Mirror `proof_anchor` for the primary artifact.

**Minimum required artifacts that MUST agree when a token is claimed**

For every claimed token, the following **MUST** be mutually consistent (same `artifact_key` / same `discovered_physical_path`, and the same bytes-hash and size at the Index/Mirror/proof level):

* The Epic Plan’s required-evidence list entry (titles/paths only, per deliverable).

* The token\_evidence\_matrix row for the token.

* The Human Evidence Index entry in `docs/evidence/INDEX.json`.

* The Machine Evidence Mirror record in `artifacts/evidence_index.jsonl` for the same `(artifact_key, discovered_physical_path)`.

* The governed path-proof referenced by the mirror record’s `proof_anchor`.

**Shared/global evidence dependencies (do not assume implicit).**

Some governed evidence surfaces are shared across many deliverables and may live outside a deliverable’s “local bundle” directory. When a deliverable’s acceptance depends on shared/global evidence surfaces, they must be **explicitly listed and bound by canonical path** rather than assumed to be “implicitly available.” PF12’s role is to define canonical paths and evidence families; workflow enforcement and review gates are routed by title to the Epic-Process-Guide and Glow QA Guide.

**Remediation-only artifacts (MUST).**

Remediation-only diagnostics and manifests MUST NOT be introduced under governed Evidence Index / Machine Mirror surfaces unless explicitly adopted via a PF12 Doc-Delta into the Evidence Catalog. Default posture: remediation-only artifacts live under remediation audit paths (for example, `audit/qa/.../remediation/...`) and do not enter the Human Evidence Index or Machine Evidence Mirror.

**Index and mirror fixed filenames (for plans/tasks that touch governed indices/mirrors).**

Evidence index (human-readable):

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `docs/evidence/INDEX.json.path_proof.txt`

* `docs/evidence/INDEX.sha256.path_proof.txt`

Evidence index mirror (machine-readable):

* `artifacts/evidence_index.jsonl`

* `artifacts/evidence_index.jsonl.path_proof.txt`

Plans and tasks that touch any file above MUST treat the sibling `.path_proof.txt` as a first-class deliverable. If a plan proposes a new file under governed roots, it MUST state whether the file is intended to appear in the indices/mirror; absence of that statement is a mechanical blocker.

**Acceptance map — token identity and shape (clarification).**

This section clarifies how acceptance tokens are identified inside acceptance-map artifacts. This prevents token identity drift when acceptance maps are rendered as tables.

**Rule (normative).**

In acceptance maps, tokens are identified by the `tokens[].name` field (case-sensitive, exact-match), not by any display label or table header text.

* Acceptance-map artifacts MUST include a top-level `tokens` array.

* Each `tokens[]` entry MUST be an object.

* Each `tokens[]` entry MUST include a `name` field whose value is a non-empty string.

* `tokens[].token_name` MAY be present as an alias/display label for compatibility, but it is non-authoritative; downstream validators MUST NOT require `token_name` and MUST NOT use it as the token’s identity.

**Implications for QA validators and plans.**

* QA plans and validators MUST derive token identity from `tokens[].name`.

* QA plans and validators MUST NOT guess field keys or treat matrix/table header labels (for example `token_name`) as tokens.

### **8.6.2 Parity rule (MUST)**

In any PR that changes governed evidence artifacts or their indexing, you **MUST** update all of the following together:

* `docs/evidence/INDEX.json` (Human Index)

* `docs/evidence/INDEX.sha256` (hash sentinel)

* `artifacts/evidence_index.jsonl` (Machine Evidence Mirror)

And you **MUST** assert the mirror/index tokens named in §8.3 (for example, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, etc.) on every change.

### **8.6.3 Entries (authoritative list; titles/paths only)**

Human Index entries are titles/paths only. Machine Mirror records include at least artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, and proof\_anchor. Every artifact listed below MUST have exactly one Human Index entry and one Machine Mirror record, plus exactly one governed \*.path\_proof.txt transcript, all kept in lockstep.

#### **Freeze-pack and math**

* artifacts/math/freeze\_pack\_manifest.json  
* artifacts/math/release\_id.txt  
* artifacts/math/release\_id\_recompute.log  
* artifacts/math/checksums\_audit.log  
* artifacts/math/manifest\_snapshot.json

#### **Canonical JSON and topology**

* artifacts/canonical/arrays\_as\_sets\_report.log

* audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson

* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

* audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json (optional)

* artifacts/topology/topology\_coherence.log

#### **Evidence Index snapshot (gate family)**

* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json

#### **Topology orientation demo**

* audit/gates/topology/orientation\_demo.txt  
* audit/gates/topology/degree\_check.log  
* audit/gates/topology/multiplicity\_vector.log

Each artifact above MUST have a co-located sibling path-proof transcript named `<artifact>.path\_proof.txt` (example: `audit/gates/topology/orientation\_demo.txt.path\_proof.txt`).

Canonical predicate targets (D16) are `audit/gates/topology/orientation\_demo.txt` and `audit/gates/topology/orientation\_demo.txt.path\_proof.txt`.

These artifacts form the topology.orientation\_demo family and serve as the exemplar for path-proof validation and topology invariants; each MUST be indexed in both the Human Evidence Index and the Machine Evidence Mirror with matching path-proofs.

#### **Deterministic order & comparators \[Required-Now\]**

* artifacts/engine/order/props\_total\_order.log  
  Log of ordering properties and invariants (antisymmetry, transitivity, totality) for the canonical comparators.  
* artifacts/engine/order/channels\_sorted.snapshot.json  
  Canonical JSON snapshot of channels in comparator order.  
* artifacts/engine/order/categories\_iter.snapshot.json  
  Canonical JSON snapshot of categories in comparator order.  
* artifacts/engine/order/abba\_identity.bytes  
  Binary AB↔BA identity sample for comparator behavior, governed by the same Mirror and path-proof discipline (abba\_identity.bytes.path\_proof.txt) as other artifacts in this section.

#### **Endpoint Catalog and A7 proofs**

* artifacts/reader/endpoints\_snapshot.json  
* artifacts/proofs/endpoints\_env\_gate\_proof.log  
* artifacts/proofs/success\_get.txt  
* artifacts/proofs/success\_head.txt  
* artifacts/proofs/success\_304.txt  
* artifacts/proofs/success\_writers\_errors.txt  
* artifacts/proofs/encoding\_invariance.txt (optional)  
* artifacts/proofs/reader\_success\_get\_head\_304.json  
  Composite proof; schema owned by the Endpoint Catalog evidence section (§8.12).

#### **Aux Narrative (text) — header snapshots**

* tests/transport/headers/aux\_text\_200.snap  
* tests/transport/headers/aux\_suppression\_200.snap

#### **CLI Admin Preview (narrative) — evidence**

* artifacts/cli/narrative/stdout.txt  
  LF-terminated narrative text; no ANSI.  
* artifacts/cli/narrative/sidecar.json  
  IDs-only: composition\_id, fragment\_ids\[\], pack\_sha, optional release\_id; canonical JSON.

#### **CLI showcompat (deterministic capture) — evidence (EPIC022 D2)**

* #### `artifacts/cli/showcompat/stdout.json`    Deterministic capture of `hdctl showcompat` stdout bytes (LF-terminated; success has empty stderr; emitted via canonical serializer as required by CLI evidence posture).

* #### `artifacts/cli/showcompat/stdout.json.sha256`    SHA-256 sidecar for `stdout.json` capture bytes.

* #### `artifacts/cli/showcompat/stdout.sha256` — allowed legacy alias of `stdout.json.sha256` (EPIC022 D2). Evidence wiring MUST normalize this alias to `stdout.json.sha256`; new producers MUST NOT emit `stdout.sha256`. If both are present they MUST match.

* #### `artifacts/cli/showcompat/args.json`    Names-only arguments/env snapshot used for deterministic capture (no secrets; canonical JSON).

* #### `tools/cli/generate_showcompat_artifacts.py`    Deterministic producer tool used to generate the EPIC022 D2 showcompat capture artifacts under closed rails.

#### **Narratives coverage (router)**

* audit/gates/narratives/keys\_10x4.table.json

#### **Rails proofs (ops)**

* artifacts/proofs/ops\_refusal\_proof.txt  
  Single-file refusal (headers → blank line → LF-terminated JSON).  
  Record type: ops\_refusal\_proof; policy and tokens are owned by HDE-Governance (titles-only).  
* ci/jobs/logs\_keys\_only\_redaction.yml  
* ci/jobs/rails\_open\_conformance.yml

#### **DB posture and runtime**

* artifacts/db/ddl\_fingerprint.json  
* artifacts/db/grants.txt  
* artifacts/db/check\_schema.txt  
* artifacts/db/check\_constraints.txt  
* artifacts/db/partition\_plan.txt  
* artifacts/db/db\_rw\_smoke.log (optional)

#### **Runtime / env**

* artifacts/runtime/env\_matrix.snapshot.json  
  Singleton snapshot (schema\_version: 3); default rails and determinism pins; presence booleans for DB/bridge/guard. Schema owned by §8.3.2; tokens by title in Governance.  
* artifacts/runtime/env\_connectivity.snapshot.json  
  Dev resolver snapshot; records attempts and selected source on fallback.

#### **Ops / refusal (closed-rails)**

* artifacts/proofs/ops\_refusal\_proof.txt  
  Same governed artifact as above, viewed here specifically as the closed-rails refusal proof (headers → blank line → LF-terminated JSON). Policy and tokens by title in Governance.

---

#### **Internal-ops surface — /internal/version identity artifacts (INTVER\_\*)**

These entries register the /internal/version identity artifacts required by Governance as governed Evidence Catalog families. /internal/version is an ops-only identity surface (non-A7); PF12 records its evidence artifacts, artifact\_keys, and Index/Mirror discipline, while transport bytes and token semantics remain in HDE-Governance and HDE-CLI-API-Vendor-Ref by title.

##### **Auth posture (not canonized; discovery evidence required)**

PF-Canon defines the `/internal/version` transport/content contract and its governed identity artifacts, but **does not canonize** the auth posture (public vs operator-network gated vs auth-header required) or the expected failure mode when access is missing/invalid.

* Until canonized, remediation guides and operational tooling MUST NOT state auth requirements for `/internal/version` as canon. Any statement about auth posture MUST be explicitly labeled as **Observed Evidence (non-PF)**.

* Until an auth-gated posture is both implemented and canonized, runbooks MUST NOT require an auth header for `/internal/version`. If an auth header is used in a probe, it MUST be treated as optional and recorded as presence-only (never the raw value) in any associated request-chain or run logs.

* Canonization of auth posture requires OPS discovery evidence that captures **status line and headers** for the canonical deployment context(s) under two conditions:

  * with **no auth header**, and

  * with the expected auth header **present** (value redacted or presence-only noted).

* This discovery evidence MUST be secret-free and stored in-repo under a lowercase audit path (titles-only: HDE-Build Notes OPS posture). PF12 governs only that any such evidence, when promoted, must live under governed roots and follow the Evidence Index/Mirror discipline.

Checksum sidecars in this family (INTVER\_\*\_SHA256\_\*) are optional unless explicitly required by an acceptance roster; if present, each checksum file MUST be the sha256 hex \+ LF of the corresponding artifact bytes.

##### **/internal/version invariant checklist (minimum set; MUST be explicit)**

##### Any remediation guide, QA step, or probe tool that produces governed `/internal/version` evidence artifacts (INTVER\_\*) MUST explicitly enumerate and verify the canon-critical invariants below. It is not acceptable to imply these checks by referencing PF sections only.

##### **A. Transport**

* ##### GET MUST return 200\. 

* ##### HEAD MUST return 200 and satisfy parity expectations. 

* ##### Conditional requests (If-None-Match, If-Modified-Since) MUST NOT yield 304\. They MUST return 200\. 

##### **B. Headers**

* ##### Cache-Control: no-store MUST be present.

* ##### Content-Type: application/json; charset=utf-8 MUST be present.

* ##### ETag MUST be absent.

* ##### Absence is literal: the captured header set MUST NOT contain an `ETag:` header line at all (do not emit placeholder lines such as `ETag: <absent>`).

* ##### Last-Modified MUST be absent. 

##### **C. Body (identity payload)**

* ##### Body MUST be fixed-schema JSON with exactly these keys (no extras): `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`. 

* ##### Body bytes MUST satisfy the canon identity bytes posture where applicable: canonical JSON per §4, including LF termination. 

##### **D. Coupling and fail-closed behavior**

* ##### Verification MUST be performed against the same captured bytes that are written as governed artifacts for that run (headers snapshots, body snapshot, and any two-run identity digest/log). 

* ##### If coupling cannot be established (mixed target or redirect drift) or verification cannot be completed (tooling failure), the run MUST fail closed for evidence purposes and MUST NOT be recorded as satisfying the corresponding invariants. 

##### This checklist does not canonize auth posture. Auth posture remains not canonized until OPS discovery evidence is captured (see the Auth posture subsection above).

##### **INTVER\_BODY\_GET\_V1 — GET body snapshot**

* Artifact path (example): artifacts/ops/internal\_version/body\_get.json — canonical JSON body for a successful GET /internal/version (six provenance fields, no extras, LF-terminated).  
* Schema path: a JSON Schema under docs/schemas/\*\* that captures the frozen six-field identity envelope for /internal/version.  
* Mirror: records use artifact\_key:"INTVER\_BODY\_GET\_V1" and role:"snapshot"; Human Index entries use the same artifact\_key and the body\_get.json path as discovered\_physical\_path.

##### **INTVER\_BODY\_GET\_SHA256\_V1 — GET body hash record**

* Artifact path (example): artifacts/ops/internal\_version/body\_get.sha256 — small JSON or text artifact recording the sha256 and size of body\_get.json as governed in Governance.  
* Mirror: records use artifact\_key:"INTVER\_BODY\_GET\_SHA256\_V1" and role:"snapshot"; Human Index entries use the same artifact\_key and the hash file path.

##### **INTVER\_HEADERS\_GET\_V1 — GET headers snapshot**

* Artifact path (example): artifacts/ops/internal\_version/headers\_get.txt — raw GET /internal/version response headers (proving Cache-Control: no-store, absence of ETag/Last-Modified, correct Content-Type).  
* Mirror: records use artifact\_key:"INTVER\_HEADERS\_GET\_V1" and role:"snapshot"; Human Index entries use the same artifact\_key and headers file path.

##### INTVER\_HEADERS\_COND\_IF\_NONE\_MATCH\_V1 — conditional headers snapshot (If-None-Match)

* Artifact path (canonical): `artifacts/ops/internal_version/headers_cond_if_none_match.txt` — raw response headers captured from a conditional request to `/internal/version` with `If-None-Match` present.  
   Purpose: provide governed evidence that `/internal/version` ignores conditional delivery for its ops-only identity contract (names-only; no body bytes in this artifact).

* Mirror: records use `artifact_key:"INTVER_HEADERS_COND_IF_NONE_MATCH_V1"` and `role:"snapshot"`; Human Index entries use the same `artifact_key` and the conditional headers file path.

  ##### **INTVER\_HEADERS\_COND\_IF\_MODIFIED\_SINCE\_V1 — conditional headers snapshot (If-Modified-Since)**

* Artifact path (canonical): `artifacts/ops/internal_version/headers_cond_if_modified_since.txt` — raw response headers captured from a conditional request to `/internal/version` with `If-Modified-Since` present.  
   Purpose: provide governed evidence that `/internal/version` ignores conditional delivery for its ops-only identity contract (names-only; no body bytes in this artifact).

* Mirror: records use `artifact_key:"INTVER_HEADERS_COND_IF_MODIFIED_SINCE_V1"` and `role:"snapshot"`; Human Index entries use the same `artifact_key` and the conditional headers file path.

  ##### **Conditional artifact key posture (normative)**

* Conditional header capture artifacts for `/internal/version` **MUST** use dedicated `INTVER_HEADERS_COND_*` artifact keys as listed above. They **MUST NOT** be indexed under `INTVER_HEADERS_GET_V1` or `INTVER_HEADERS_HEAD_V1`.

* Evidence Index and Machine Mirror entries for these files **MUST** be consistent with this dedicated-key posture.

##### **INTVER\_HEADERS\_HEAD\_V1 — HEAD headers snapshot**

* Artifact path (example): artifacts/ops/internal\_version/headers\_head.txt — raw HEAD /internal/version response headers (200, Content-Length \== len(identity GET body), Content-Type \== GET, no body).  
* Mirror: records use artifact\_key:"INTVER\_HEADERS\_HEAD\_V1" and role:"snapshot"; Human Index entries use the same artifact\_key and headers file path.

##### **INTVER\_TWO\_RUN\_IDENTITY\_V1 — coupling and two-run identity log (single governed proof)**

* Artifact path (example): artifacts/ops/internal\_version/two\_run\_identity.log — single governed log proving /internal/version coupling and two-run identity under closed rails.  
* Minimum required content (names-only; no secrets):  
  * Two-run identity result: explicit pass/fail that two consecutive GET /internal/version captures are byte-identical, including recorded digests or byte identifiers for both runs.  
  * Coupling verification result: explicit pass/fail that the six /internal/version fields match their governing identity sources (record the governing artifact paths by name and the check outcome, including release\_id coupling).  
  * Rails posture reference: names-only reference to closed-rails posture and the determinism pins evidence surface (audit/gates/determinism/env\_pins.log).  
* Mirror: records use artifact\_key:"INTVER\_TWO\_RUN\_IDENTITY\_V1" and role:"log"; Human Index entries use the same artifact\_key and log path.

##### **INTVER\_REQUEST\_CHAIN\_MANIFEST\_V1 — request-chain manifest (deterministic)**

* ##### Artifact path (canonical): `artifacts/ops/internal_version/request_chain_manifest.json`    Deterministic request-chain manifest associated with `/internal/version` evidence capture runs.

* ##### Requirements (normative):

  * ##### MUST be secret-free. If an auth header is used by a probe or harness, the manifest MUST NOT record the raw value (presence-only or redacted placeholder only).

  * ##### MUST have a co-located sibling path-proof transcript:     `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`

* ##### Mirror/Index linkage (names-only):

  * ##### Mirror: records use `artifact_key:"INTVER_REQUEST_CHAIN_MANIFEST_V1"` and `role:"snapshot"`.

  * ##### Human Index: entries use the same `artifact_key` and the manifest path as `discovered_physical_path`.

  * ##### `proof_anchor` MUST point to `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`.

##### 

##### **Indexing and Mirror discipline**

For each INTVER\_\* family above, the Human Evidence Index (docs/evidence/INDEX.json) MUST contain at least one entry with the appropriate artifact\_key and a discovered\_physical\_path pointing to the governed artifact under artifacts/ops/internal\_version/\*\*; docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any /internal/version artifact. The Machine Evidence Mirror (artifacts/evidence\_index.jsonl) MUST contain canonical JSONL records for each governed /internal/version artifact and schema, using the artifact\_key names exactly as above and the minimum Mirror record schema in §8.3 (artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor).

##### **Acceptance hints (names-only)**

These INTVER\_\* families are the governed surfaces for the /internal/version identity token titles defined in PF04 (and the relevant EPIC acceptance roster), e.g.: INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK, INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_NOTOK, INTERNAL\_VERSION\_200\_CTYPE\_HTML\_NOTOK, INTERNAL\_VERSION\_404\_NOTOK.

---

#### **Presenter evidence (EPIC020 D2 — presenter/emitter identity)**

These entries register the presenter evidence families introduced by HDE-EPIC020 D2 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section (UTF-8, sorted keys, compact separators, exactly one trailing LF for JSON artifacts; governed paths only; path-proofs and Index/Mirror parity per §8.3–§8.6). PF12 binds these families to D2 tokens by artifact\_key and path only; token semantics remain in HDE-Governance and Glow QA Guide by title.

##### **Presenter identity summary — canonical JSON summary for showcompat identity**

* Example path: a JSON file under artifacts/presenter/ (for example, artifacts/presenter/showcompat\_identity\_summary.json); schema owned by an engine/presenter presenter evidence schema in docs/schemas/\*\*.  
* Family name: PRESENTER\_IDENTITY\_SUMMARY\_V1 — Machine Mirror records for this family use artifact\_key:"PRESENTER\_IDENTITY\_SUMMARY\_V1" and a role such as "snapshot"; Human Index entries use the same artifact\_key as the title and the concrete summary file path as discovered\_physical\_path.

##### **Presenter preimage recompute log — preimage recompute evidence for presenter/Reader envelopes**

* Example path: a log file under artifacts/presenter/ (for example, artifacts/presenter/preimage\_recompute.log).  
* Family name: PRESENTER\_PREIMAGE\_RECOMPUTE\_V1 — Mirror records use artifact\_key:"PRESENTER\_PREIMAGE\_RECOMPUTE\_V1" and role:"log"; Human Index entries use that artifact\_key and the log path as discovered\_physical\_path.

##### **Presenter Reader/CLI parity bytes — Reader vs CLI presenter parity sample**

* Example path: a bytes or JSON artifact under artifacts/presenter/ capturing a presenter-level Reader/CLI parity proof (for example, artifacts/presenter/reader\_cli\_parity.bytes).  
* Family name: PRESENTER\_READER\_CLI\_PARITY\_V1 — Mirror records use artifact\_key:"PRESENTER\_READER\_CLI\_PARITY\_V1" and role:"snapshot" (or "log" depending on implementation); Human Index entries use the same artifact\_key and the parity artifact path.

##### **Presenter AB/BA identity bytes — showcompat AB/BA presenter bytes**

* Example paths: bytes artifacts under artifacts/presenter/ capturing AB and BA showcompat presenter bytes (for example, artifacts/presenter/showcompat\_ab.bytes and artifacts/presenter/showcompat\_ba.bytes).  
* Family names: PRESENTER\_SHOWCOMPAT\_AB\_BYTES\_V1 and PRESENTER\_SHOWCOMPAT\_BA\_BYTES\_V1 — Mirror records use these artifact\_keys and role:"snapshot"; Human Index entries use the same artifact\_keys and their corresponding AB/BA presenter byte paths as discovered\_physical\_path values.

##### **Indexing and Mirror discipline**

For each of the presenter families above, the Human Evidence Index (docs/evidence/INDEX.json) MUST contain at least one entry per artifact\_key (for example, "PRESENTER\_IDENTITY\_SUMMARY\_V1") with a discovered\_physical\_path pointing to the governed artifact path under artifacts/presenter/\*\*; docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any presenter artifact. The Machine Evidence Mirror (artifacts/evidence\_index.jsonl) MUST contain canonical JSONL records for each governed presenter artifact and schema, using the artifact\_key names exactly as above and the minimum Mirror record schema in §8.3 (artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor).

##### **Acceptance hints (names-only)**

These families support the EPIC020 D2 presenter tokens (for example, CLI\_SHOWCOMPAT\_CANON\_OK, TWO\_RUN\_IDENTITY\_OK, COMPOSITE\_ABBA\_IDENTITY\_OK, PREIMAGE\_RECOMPUTE\_OK) by providing governed artifacts and Index/Mirror records; PF12 binds tokens to artifacts by name and path only and does not redefine token semantics.

---

#### **Error evidence (EPIC020 D1 — Reader/CLI parity, schema, token map)**

These entries register the error evidence families introduced by HDE-EPIC020 D1 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section (UTF-8, sorted keys, compact separators, exactly one trailing LF where JSON is used; governed paths only; path-proofs and Index/Mirror parity per §8.3–§8.6).

##### **ERRORS\_READER\_CLI\_PARITY\_V1 — Reader↔CLI parity artifacts**

* parity/errors\_reader\_cli.\*.http.json  
* parity/errors\_reader\_cli.\*.cli.txt

Closed-rails error parity artifacts for EPIC020 D1. Each scenario captures a typed error envelope from the HTTP surface and a matching CLI stderr/text log, used together to prove Reader↔CLI parity for error codes and messages under closed rails. These files form the ERRORS\_READER\_CLI\_PARITY\_V1 evidence family. Machine Mirror records for this family use artifact\_key:"ERRORS\_READER\_CLI\_PARITY\_V1" and role:"log"; Human Index entries use the same artifact\_key as the title and the concrete parity file paths as discovered\_physical\_path values. Token semantics (for example, CLI\_READER\_PARITY\_OK and related parity tokens) remain owned by HDE-Governance and Glow QA Guide; PF12 binds them to this family by name and path only.

##### **ERROR\_SCHEMA\_CHECK\_V1 — error-envelope schema-check logs**

* errors/schema\_check/error\_envelope\_\*.log

Error-envelope schema-check logs for selected error-envelope scenarios (for example, invalid\_json, invalid\_viewer\_prefs, db\_unavailable, vendor\_attempt\_closed\_rails). Each log records at minimum the scenario name, HTTP status, canonical error code, and schema validation result under the governed error envelope schema. These files form the ERROR\_SCHEMA\_CHECK\_V1 evidence family. Machine Mirror records use artifact\_key:"ERROR\_SCHEMA\_CHECK\_V1" and role:"log"; Human Index entries use the same artifact\_key and the concrete log paths under errors/schema\_check/. These artifacts support error-envelope schema tokens such as ERROR\_JSON\_CANON\_OK and JSON\_CANONICAL\_CHECK\_OK (names-only; semantics live in Governance).

##### **ERROR\_TOKEN\_MAP\_V1 — token-map snapshot**

* errors/token\_map/token\_map.json

Canonical JSON snapshot of the typed error token map, listing each error code with its aliases and message text for the current error envelope set. This file forms the ERROR\_TOKEN\_MAP\_V1 evidence family. Machine Mirror records use artifact\_key:"ERROR\_TOKEN\_MAP\_V1" and role:"snapshot"; the Human Index entry uses the same artifact\_key and discovered\_physical\_path:"errors/token\_map/token\_map.json". This artifact underpins the ERROR\_TOKEN\_MAP\_OK token (names-only), ensuring that the runtime error token map matches the governed snapshot used in tests and CLI/HTTP error behavior.

##### **Indexing and path-proofs**

All three error evidence families MUST participate in the standard Evidence Index/Mirror discipline:

Human Index (docs/evidence/INDEX.json):

* For every concrete parity artifact (parity/errors\_reader\_cli.*.http.json or parity/errors\_reader\_cli.*.cli.txt), there MUST be an entry whose artifact\_key is "ERRORS\_READER\_CLI\_PARITY\_V1" and whose discovered\_physical\_path equals that file’s repo-relative path.  
* For every schema-check log under `errors/schema_check/error_envelope_*.log`, there **MUST** be an entry whose `artifact_key` is `"ERROR_SCHEMA_CHECK_V1"` and whose `discovered_physical_path` equals that log’s path.  
* For the token-map snapshot, there MUST be an entry with artifact\_key:"ERROR\_TOKEN\_MAP\_V1" and discovered\_physical\_path:"errors/token\_map/token\_map.json".  
* docs/evidence/INDEX.sha256 MUST be updated in the same PR as any change to these artifacts or their indexing.

Machine mirror (artifacts/evidence\_index.jsonl):

* MUST contain canonical JSONL records for each governed error artifact above with:  
  * artifact\_key set to "ERRORS\_READER\_CLI\_PARITY\_V1", "ERROR\_SCHEMA\_CHECK\_V1", or "ERROR\_TOKEN\_MAP\_V1" as appropriate,  
  * role set to "log" for parity and schema-check artifacts and "snapshot" for the token map,  
  * discovered\_physical\_path equal to the path recorded in the Human Index,  
  * sha256 and size\_bytes matching the artifact’s canonical bytes,  
  * produced\_at\_utc reflecting the evidence refresh time, and  
  * proof\_anchor pointing to the matching .path\_proof.txt transcript alongside each artifact.  
* Mirror records MUST obey all §8.3 rules (field set, ASCII field order, sort-before-write, single mirror file, unknown-key rejection).

Path-proofs:

* Each concrete parity artifact and schema-check log MUST have a sibling path-proof transcript (`<file>.path_proof.txt`) stored alongside the artifact, whose `path`, `sha256`, `size_bytes`, `mtime_utc`, and `produced_at_utc` match the artifact’s canonical bytes and its Mirror record.  
* errors/token\_map/token\_map.json MUST have a sibling errors/token\_map/token\_map.json.path\_proof.txt transcript with the same constraints.

Acceptance hints for these families are names-only and include error/parity and schema tokens such as CLI\_READER\_PARITY\_OK (and its legacy alias CLI\_READER\_EMITTER\_PARITY\_OK), ERROR\_JSON\_CANON\_OK, JSON\_CANONICAL\_CHECK\_OK, and ERROR\_TOKEN\_MAP\_OK. PF12 does not change token semantics; it binds these tokens to the governed error evidence families by artifact\_key and path so that Governance, QA, and PF09 can route by title only.

---

#### **Sampler evidence (D4 — HDE-EPIC019)**

These entries register the sampler/ranker evidence families introduced by HDE-EPIC019 D4 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section (UTF-8, sorted keys, compact, exactly one LF; governed paths only; path-proofs and Index/Mirror parity per §8.3–§8.6).

##### **sampler\_pool\_snapshots — sampler pool/eligibility snapshots**

Purpose. Canonical JSON snapshots of sampler candidate pools, including viewer ID, candidate IDs, bands, compat scores, weights, and eligibility flags, used to prove sampler pool composition and eligibility filters (D1 core behavior).  
Artifact path (example). artifacts/sampler/pool\_snapshots/baseline.json (and siblings under artifacts/sampler/pool\_snapshots/).  
Schema path. docs/schemas/sampler/pool\_snapshots.schema.json (JSON Schema 2020-12, titles-only here).  
PII posture. Artifacts omit PII beyond IDs, bands, compat labels, and QA-necessary metadata; no app-level user identifiers or raw personal data are permitted.

##### **sampler\_two\_run\_logs — sampler two-run identity logs**

Purpose. Logs demonstrating two-run identity for sampler output (same inputs ⇒ identical ordering), used to prove sampler determinism under closed rails.  
Artifact path. artifacts/sampler/two\_run/identity.json.  
Schema path. docs/schemas/sampler/two\_run\_logs.schema.json.  
Notes. Canonical JSON; array fields that represent sets follow arrays-as-sets rules (§4.2).

##### **sampler\_abba\_logs — AB/BA/ABBA parity logs**

Purpose. AB/BA/ABBA sampler runs for parity checks (A→B, B→A, ABBA), used to show that sampler ranking is invariant under label order when inputs are normalized.  
Artifact path. artifacts/sampler/abba/ab\_ba\_parity.json.  
Schema path. docs/schemas/sampler/abba\_logs.schema.json.

##### **sampler\_diversity\_artifacts — diversity/window evidence**

Purpose. Evidence for diversity, window, and “recent selection” constraints in the sampler, used to show that the sampler respects configured spread and recency rules.  
Artifact path. artifacts/sampler/diversity/diversity\_requirements.json.  
Schema path. docs/schemas/sampler/diversity\_artifacts.schema.json.

##### **sampler\_seed\_replay\_logs — seed replay logs (CLI/HTTP harnesses)**

Purpose. Seed replay logs from dev sampler CLI/HTTP harnesses, capturing repeated seeded runs and proving seed-echo semantics and candidate-set stability across surfaces.  
Artifact path. artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json.  
Schema path. docs/schemas/sampler/seed\_replay\_logs.schema.json.

##### **Canonical JSON policy and governed locations (sampler)**

All sampler artifacts listed above MUST use the canonical JSON emitter governed by §4 (UTF-8, ASCII-sorted keys, compact separators, exactly one trailing LF; arrays treated as sets are deduped and ASCII-sorted by identity).  
All sampler artifacts and schemas MUST live under governed locations:

* artifacts/sampler/\*\*  
* docs/schemas/sampler/\*\*

Transient generator paths (for example, codex/out/\*\*, temp directories) MUST NOT be indexed or mirrored.

##### **Evidence Index/Mirror and path-proofs (sampler)**

For each sampler family, the Human Evidence Index (docs/evidence/INDEX.json) MUST contain an entry with the appropriate artifact\_key (for example, "sampler\_pool\_snapshots") and discovered\_physical\_path pointing to the governed artifact path; docs/evidence/INDEX.sha256 MUST be updated in the same PR.  
The Machine Evidence Mirror (artifacts/evidence\_index.jsonl) MUST contain a canonical JSONL record for each governed sampler artifact and schema, using artifact\_key names exactly as above and the minimum Mirror record schema in §8.3 (artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor).  
Each sampler artifact and schema MUST have a sibling path-proof transcript (for example, artifacts/sampler/pool\_snapshots/baseline.json.path\_proof.txt, docs/schemas/sampler/pool\_snapshots.schema.json.path\_proof.txt) that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via proof\_anchor.

##### **Acceptance hints (names-only; sampler)**

Sampler evidence families participate in the existing mirror/index tokens referenced in §0.2 and §8.3 (for example, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, JSON\_CANONICAL\_CHECK\_OK). PF12 binds these tokens to sampler artifacts by name and path only; token semantics remain owned by Governance and Glow QA Guide.

---

#### **Engine Core evidence (DISS003/DISS004 — HDE-EPIC019)**

These entries register the Engine Core evidence families introduced by HDE-EPIC019 PR7 as governed members of the Evidence Catalog. They mirror the sampler evidence pattern: canonical JSON artifacts under artifacts/core/**, schemas under docs/schemas/core/**, and full Index/Mirror \+ path-proof discipline under §8.3–§8.6.

##### **engine\_core\_purity\_report — Engine Core purity report**

Purpose. Canonical JSON report that summarizes Engine Core “purity” checks over compute\_core scenarios (for example, invariants that must hold for all core calls under closed rails). Each report instance is produced under closed rails and records env posture and provenance alongside result data.  
Artifact path. artifacts/core/purity/purity\_report.json (and siblings under artifacts/core/purity/ if multiple purity reports are captured).  
Schema path. docs/schemas/core/engine\_core\_purity\_report.schema.json (JSON Schema 2020-12, titles-only here).  
Generated-at and env metadata. Each artifact MUST include a payload-level generated\_at\_utc field (UTC ISO-8601) and closed-rails env metadata sufficient to reconstruct the determinism posture used for the run; provenance semantics and timestamp constraints follow §8.3 (“Artifacts with generated\_at\_utc”) for all Engine Core families.

##### **engine\_core\_two\_run\_logs — Engine Core two-run identity logs**

Purpose. Canonical JSON logs demonstrating two-run identity for Engine Core output (same inputs ⇒ identical outputs) under closed rails. These logs are used to prove TWO\_RUN\_IDENTITY\_OK and related determinism tokens for the core engine.  
Artifact path. artifacts/core/two\_run/identity.json.  
Schema path. docs/schemas/core/engine\_core\_two\_run\_logs.schema.json.  
Notes. Arrays that function as sets (for example, lists of tested scenarios) MUST follow arrays-as-sets rules in §4.2 (deduped by identity, ASCII-sorted).

##### **engine\_core\_abba\_logs — Engine Core AB/BA/ABBA parity logs**

Purpose. Canonical JSON logs for AB/BA/ABBA runs over Engine Core (for example, swapping label order where appropriate), used to demonstrate that core behavior is invariant under symmetry-preserving input permutations after normalization.  
Artifact path. artifacts/core/abba/ab\_ba\_parity.json.  
Schema path. docs/schemas/core/engine\_core\_abba\_logs.schema.json.  
Notes. These logs complement engine\_core\_two\_run\_logs by proving parity properties; the same canonical JSON and path-proof discipline applies.

##### **engine\_core\_json\_compare\_logs — Engine Core JSON-compare logs**

Purpose. Canonical JSON logs produced by comparing Engine Core result JSON across two runs or two surfaces (for example, CLI vs internal harness) and recording equality/inequality at the structured JSON level. These artifacts are used to support JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK, and related core evidence tokens.  
Artifact path. artifacts/core/json\_compare/core\_result\_json\_compare.json.  
Schema path. docs/schemas/core/engine\_core\_json\_compare\_logs.schema.json.  
Notes. Logs MUST NOT include raw payloads beyond what the schema requires for comparison; they remain names-only and structural, and rely on canonical JSON for reproducible diffs.

##### **Canonical JSON policy and governed locations (Engine Core)**

All Engine Core artifacts listed above MUST use the canonical JSON emitter governed by §4 (UTF-8, ASCII-sorted keys, compact separators, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted by identity).  
All Engine Core artifacts and schemas MUST live under governed locations:

* artifacts: artifacts/core/\*\*  
* schemas: docs/schemas/core/\*\*

Transient generator paths (for example, scratch or codex/out/\*\*) MUST NOT be indexed or mirrored.

##### **Evidence Index/Mirror and path-proofs (Engine Core)**

For each Engine Core family, the Human Evidence Index (docs/evidence/INDEX.json) MUST contain at least one entry with the appropriate artifact\_key (for example, "engine\_core\_purity\_report") and a discovered\_physical\_path pointing to the governed artifact path; docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any Engine Core artifact.  
The Machine Evidence Mirror (artifacts/evidence\_index.jsonl) MUST contain canonical JSONL records for each governed Engine Core artifact and schema, using artifact\_key names exactly as above and the minimum Mirror record schema in §8.3 (artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor).  
Each Engine Core artifact and schema MUST have a sibling path-proof transcript (for example, artifacts/core/purity/purity\_report.json.path\_proof.txt, docs/schemas/core/engine\_core\_purity\_report.schema.json.path\_proof.txt) that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via proof\_anchor. Path-proof sha256 and size\_bytes MUST match both the artifact’s canonical bytes and the Mirror record values.

##### **Acceptance hints (names-only; Engine Core skeleton)**

Engine Core evidence families participate in the existing Mirror/Index tokens referenced in §0.2 and §8.3 (for example, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK). Together with the sampler evidence families, they form the governed Engine Core/sampler evidence skeleton for DISS003/DISS004; PF12 binds these tokens to Engine Core artifacts by name and path only. Token semantics remain owned by Governance and Glow QA Guide.

---

#### **SBOM**

* sbom/cyclonedx.json  
* sbom/cyclonedx.json.sha256

#### **Registry/reporting & config**

* artifacts/registry/registry\_report.json  
* config.magic10 — Magic-10 configuration snapshot (names-only summary of Magic-10 order, caps, and seed metadata; canonical JSON).  
  * Path: artifacts/thresholds/magic10\_config.json  
  * Path-proof: artifacts/thresholds/magic10\_config.json.path\_proof.txt  
  * Mirror record: artifact\_key:"config.magic10", role:"snapshot", discovered\_physical\_path:"artifacts/thresholds/magic10\_config.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.1.  
* config.band\_edges — Band-edges configuration snapshot (names-only summary of band names, edges, clamp, rounding mode, and version linked to math/thresholds.json; canonical JSON).  
  * Path: artifacts/thresholds/band\_edges.json  
  * Path-proof: artifacts/thresholds/band\_edges.json.path\_proof.txt  
  * Mirror record: artifact\_key:"config.band\_edges", role:"snapshot", discovered\_physical\_path:"artifacts/thresholds/band\_edges.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.2.  
* epic018.config.acceptance\_map — HDE-EPIC018 config acceptance map (PF09-style mapping from config tasks → artifact keys → tokens/tests; canonical JSON).  
  * Path: audit/EPIC-018\_config\_acceptance\_map.json  
  * Path-proof: audit/EPIC-018\_config\_acceptance\_map.json.path\_proof.txt  
  * Mirror record: artifact\_key:"epic018.config.acceptance\_map", role:"snapshot", discovered\_physical\_path:"audit/EPIC-018\_config\_acceptance\_map.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.3.  
* config\_bundle.fe — Typed frontend config bundle (names-only projection of governed Magic-10 config, band-edges config, and registry topology/alias policy for client consumption; canonical JSON; includes a sources block keyed to the underlying config artifacts and registry report).  
  * Path: JSON file under artifacts/config\_bundles/ (exact filename pinned by the bundle generator and tests).  
  * Path-proof: sibling .path\_proof.txt transcript under artifacts/path\_proofs/... for the same path.  
  * Mirror record: artifact\_key:"config\_bundle.fe", role:"snapshot", discovered\_physical\_path equal to the bundle path, with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the bundle’s canonical bytes and path-proof as required by §8.3 and §8.15.  
* config\_bundle.be — Typed backend config bundle (names-only projection of governed Magic-10 config, band-edges config, full channels/centers/domains/alias policy, and registry-derived topology for engine/internal use; canonical JSON; includes a sources block keyed to the underlying config artifacts and registry report).  
  * Path: JSON file under artifacts/config\_bundles/ (exact filename pinned by the bundle generator and tests).  
  * Path-proof: a sibling `<bundle_file>.path_proof.txt` transcript stored alongside the bundle file (same directory).  
  * Mirror record: artifact\_key:"config\_bundle.be", role:"snapshot", discovered\_physical\_path equal to the bundle path, with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the bundle’s canonical bytes and path-proof as required by §8.3 and §8.15.

#### **BodyGraph adapter data-source and invariance**

* artifacts/bodygraph/source\_selection.snapshot.json  
* artifacts/bodygraph/source\_invariance/ab.json  
* artifacts/bodygraph/source\_invariance/ba.json  
* artifacts/bodygraph/source\_invariance/summary.json  
* artifacts/bodygraph/release\_bindings.json  
* artifacts/bodygraph/refresh\_policy.snapshot.json  
* artifacts/bodygraph/metrics.snapshot.json  
* artifacts/bodygraph/keys\_only.logs.sample

#### **Lifecycle (backup/restore/retention) — OPS-managed captures**

* artifacts/db/backup\_manifest.json  
* artifacts/db/restore\_verify.log  
* artifacts/db/retention\_run.log

#### **Admin QA and runbooks**

* docs/run/PROD\_ENDPOINTS.json  
* docs/run/RUN\_PROD\_QA.md  
* docs/run/EPIC011\_TEST\_IDENTITIES.md  
* artifacts/ops/admin\_vendor\_calls.jsonl

---

### **Epic QA harness ledger artifacts (per-epic; names-only; current-state)**

These entries register QA harness ledger files that summarize Live QA results **as current-state evidence**, while keeping per-run retention optional and non-canon unless explicitly promoted. The invariant required outputs for a Live QA run are the per-check primary log and the step-logs manifest; additional ledger artifacts may exist but MUST NOT be required for closure by default.

**Canonical epic QA root**  
 `audit/qa/<epic-id>/`

**Invariant required outputs (current-state; canonical paths):**

* `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
   Per-epic manifest acting as a **current-state index keyed by check\_id**, pointing to (at minimum) each check’s status and the canonical path to its primary log. Records-only canonical JSON (UTF-8, ASCII-sorted keys, compact, exactly one trailing LF).

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
   Per-check primary log (one per check\_id) containing the authoritative run output and verdict context for that check. LF-terminated, non-empty text. This file is referenced by `qa_step_logs_manifest.json`.

**Optional ledger artifacts (non-required for closure; current-state if present):**

* `audit/qa/<epic-id>/acceptance_map_viability.log`  
   Per-epic text log summarizing acceptance-map viability results for the current-state (and optionally noting any retained history). LF-terminated text.

* `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`  
   Optional Step-0 Codespaces environment snapshot (tool versions, rails pins, presence-only env context). Canonical JSON; schema and indexing posture are defined in §8.17.5. Live QA Plans MUST NOT require this artifact for closure by default.

* `audit/docdeltas/<epic-id>_doc_deltas.md`  
* Mechanically produced doc delta draft/capture (names-only; no secrets). If no deltas exist, the artifact MUST explicitly say so (produced output, not an instruction). This artifact may be referenced by QA ledger artifacts and/or close-pack `key_outputs` pointers, but it is not required to live under the epic QA root.

**Optional per-run retention (non-canon; allowed):**  
 A retained copy MAY exist under `audit/qa/<epic-id>/runs/<run_id>/…` (including run-scoped copies of check logs, snapshots, or debugging outputs). If present, run copies MUST NOT be required for closure, and MUST NOT be used for manifest keying. They may be indexed only if explicitly promoted as governed evidence by acceptance wiring.

**Indexing discipline (governed artifacts):**  
 Indexing follows the standard §8.6 rule set: exactly one Human Evidence Index entry per concrete file path, exactly one Machine Evidence Mirror record per concrete file path, and exactly one governed path-proof transcript per concrete file path, kept in lockstep.

---

### **Epic token/evidence matrix (per-epic QA ledger; current-state)**

These entries register per-epic Token/Evidence Matrix artifacts as governed members of the Evidence Catalog. Each matrix provides a single, reviewable ledger mapping QA tokens to evidence and execution surfaces for one epic.

#### **Family description**

Each epic MAY define exactly one Token/Evidence Matrix artifact under its epic QA root. The matrix is current-state; it is updated in place as the epic’s closure posture evolves.

#### **Path pattern (single home per epic; choose exactly one format per epic)**

* Markdown: `audit/qa/<epic-id>/token_evidence_matrix.md`  
* JSON: `audit/qa/<epic-id>/token_evidence_matrix.json`  
* JSONL: `audit/qa/<epic-id>/token_evidence_matrix.jsonl`

`<epic-id>` is the canonical epic identifier used in §8.17 (lower-case ASCII, hyphenated; for example `hde-epic021`). If a semantic epic identifier differs (for example `HDE-EPIC021`), it MAY be recorded in Machine Mirror metadata via `epic_id` (see §8.3 allowed metadata keys).

The matrix is a textual artifact (Markdown or JSON/JSONL) intended to be read by humans and QA agents; it must carry no secrets.

#### **Row set (binding discipline; names-only)**

Matrix rows are reserved for the set of QA tokens that this epic explicitly claims as in-scope.

Tokens explicitly deferred or out of scope for this epic MUST NOT appear as matrix rows.

#### **Minimum content (names-only)**

For each token row in the matrix, the artifact MUST record at least:

* `token_name` — the QA token’s canonical name, as defined in HDE-Governance and/or Glow QA Guide or an approved doc delta (titles-only).  
* `owner_pf` — the PF document (and optionally section) that owns the token’s semantics (titles-only).  
* `evidence_artifacts` — one or more governed artifacts associated with the token (artifact\_keys and/or discovered\_physical\_path entries), drawn from families listed in §8.6 and other PF12 sections.  
* `qa_root_logs` — QA log paths under `audit/qa/<epic-id>/…` that demonstrate QA harness runs relevant to this token (current-state preferred; retained history optional).  
* `ci_tests_jobs` — CI test modules and/or jobs that enforce this token under closed rails (names only).

Additional columns such as Status or Notes MAY be present for human use; their contents are not governed by PF12 beyond canonical text formatting and governed-path rules.

#### **Canonical format**

When the matrix is Markdown, it MUST remain plain UTF-8 text with LF line endings and no ANSI sequences.

When JSON/JSONL is used instead of Markdown, canonical JSON rules from §4 apply (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted when treated as sets).

#### **Indexing (titles/paths only)**

Let MATRIX\_PATH be the chosen single-home Token/Evidence Matrix path for this epic (one of the three paths listed above).

**Human Evidence Index (docs/evidence/INDEX.json).**  
For each epic that defines a Token/Evidence Matrix, there MUST be exactly one Index entry with:

* `artifact_key` set to a stable, epic-scoped key (for example `epic021.token_matrix`), and  
* `discovered_physical_path` pointing to MATRIX\_PATH.

`docs/evidence/INDEX.sha256` MUST be updated in the same change-set whenever a new epic matrix is added or its path changes.

**Machine Evidence Mirror (artifacts/evidence\_index.jsonl).**  
Each epic Token/Evidence Matrix MUST have a corresponding Mirror record with:

* `artifact_key` equal to the key used in the Human Index entry,  
* `role`: `"snapshot"`,  
* `discovered_physical_path` pointing to MATRIX\_PATH,  
* `sha256`, `size_bytes`, `produced_at_utc`, and `proof_anchor` matching the governed path-proof transcript for this artifact.

If additional labeling is needed, use §8.3 metadata keys (for example `epic_id` and `record_type:"token_evidence_matrix"`). Unknown keys remain rejected.

Exactly one Mirror record per epic is allowed for this family; additional QA tables or notes under the same directory are separate artifacts and MUST NOT reuse the same `artifact_key`.

**Path-proofs.**  
Each matrix artifact MUST have a sibling path-proof transcript (for example `token_evidence_matrix.md.path_proof.txt`) that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via `proof_anchor`.

#### **Acceptance hints (names-only)**

PF12 does not own token semantics. For epic Token/Evidence Matrices, PF12 binds the matrix family to existing QA tokens by name and path only. Epics and QA plans use the matrix as a ledger; PF12 governs only its existence, location, and indexing.

---

### **8.6.4 Discipline reminder (current-state; unchanged)**

Every entry above must have:

* Exactly one Human Index entry in `docs/evidence/INDEX.json`.  
* Exactly one Mirror record in `artifacts/evidence_index.jsonl`.  
* Exactly one governed path-proof transcript (`*.path_proof.txt`), referenced by `proof_anchor`.

Mirror records must follow §8.3:

* Canonical JSONL  
* Single mirror file  
* Sorted field order and sorted records  
* LF-terminated  
* Unknown-key rejection  
* `proof_anchor` pointing to a stored path-proof transcript for the same artifact  
  * 

  ### **8.6.5 Acceptance impact**

* This section is a **names-only catalog** of governed artifact families and their paths.

* It does **not** introduce new acceptance tokens.

* Enforcement remains via existing mirror/index tokens (for example, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`), plus the specific domain tokens referenced by Governance and QA.

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

**Authoritative Endpoint Catalog file (records-only; names-only fields).**

The authoritative Catalog file lives at:

* `docs/ENDPOINTS_CATALOG.json` (records-only; canonical JSON), and

* `docs/ENDPOINTS_CATALOG.json.sha256` (checksum sidecar; computed over the catalog’s canonical bytes).

This Catalog is a machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints) used to support QA, audits, and transport reasoning. It contains **names-only metadata** and MUST NOT embed secrets or example payload bytes.

**Minimum required fields (per endpoint record).**  
 Each endpoint entry in `docs/ENDPOINTS_CATALOG.json` MUST include at least:

* `path` — route path (e.g., `/reader`, `/api/compat/v1`, `/internal/version`) as a string.

* `method` — HTTP method as a string (e.g., `GET`, `POST`, `HEAD`).

* `classification` — one of:  
   `public_reader`, `public_compat`, `internal_identity`, `ops`, `dev_harness`.

* `blueprint_module` — owning module path (names-only) such as `adapter/http_reader.py` or `engine/http/compat_handler.py`.

* `rails_profile` — a short names-only description of expected rails posture (e.g., “closed rails”, “APP\_ENV-gated dev harness”, “ops no-store”), without secrets.

Additional fields MAY exist, but they MUST remain names-only and MUST remain compatible with the owning schema/checks.

**Suggested minimal schema (example).**  
 {  
 "generated\_at\_utc": "YYYY-MM-DDThh:mm:ssZ",  
 "endpoints": \[  
 {  
 "path": "\<route-path\>",  
 "method": "\<METHOD\>",  
 "classification": "\<one-of: public\_reader|public\_compat|internal\_identity|ops|dev\_harness\>",  
 "blueprint\_module": "\<module-path\>",  
 "rails\_profile": "\<names-only rails summary\>"  
 }  
 \]  
 }

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

## **8.13 Stateless QA export families (no-DB JSON mode) \[Required−Now\]**

**Purpose.**  
 Record the governed evidence families used to exercise the engine in a **stateless/no-DB QA mode**, using only CLI \+ files. These families do not replace existing DB-bound evidence; they provide a complementary way to prove engine math and Reader/CLI parity when no app user model or persistent BodyGraph records are available.

**Family: `qa.bodygraph_export.stateless`**

* **Role.** Captures a single BodyGraph export JSON object produced directly from birth data or vendor JSON via CLI, without reading or writing app/user tables.

* **Minimum content (names-only).**

  * `schema` — a string tag (e.g. `"hdctl_bodygraph_export.v1"`) governed by this document.

  * `input` — a birth tuple or vendor JSON descriptor (names-only; schema pinned in PF12 §3.x).

  * `bodygraph` — a structure containing centers, channels, gates, profile, authority, definition, and type as IDs (titles-only to HDE-Math-Spec and HDE-Schemas & Artifacts catalogs).

  * `meta` — engine/build identity fields (e.g. `engine_tag`, `release_id`, `invocation_tag`) routed to HDE-Math-Spec/HDE-Governance by title.

* **Canonical JSON.** Artifact bytes MUST obey PF12 canonical JSON rules: UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF; arrays used as sets deduped and ASCII-sorted.

* **Stateless posture.** No app-level user IDs or DB row identifiers are permitted in this artifact; provenance is via `input` and catalog IDs only.

* **Indexing.** When used as governed evidence, each artifact MUST be indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` with a `proof_anchor` to a co-located path-proof transcript (see §8.3).

**Family: `qa.compat_export.stateless`**

* **Role.** Captures a compat run in stateless mode, using two BodyGraph exports or two birth tuples as inputs, and emits compat \+ Reader envelope JSON without DB users.

* **Minimum content (names-only).**

  * `schema` — a string tag (e.g. `"hdctl_compat_export.v1"`) governed here.

  * `inputs` — references to the two charts (by birth data and/or BodyGraph export identity).

  * `compat` — internal compat result (Magic-10 IDs and bands only; numbers remain admin/internal; arithmetic lives in HDE-Math-Spec).

  * `reader_envelope` — nested copy of the six-key Reader v1 success body for this pair (see PF01/PF05 by title), used for Reader↔CLI parity checks; this is not a separate public transport surface.

  * `meta` — identity fields as above (engine\_tag, release\_id, invocation\_tag).

* **Canonical JSON.** Same canonical JSON requirements as `qa.bodygraph_export.stateless`.

* **Stateless posture.** No DB user IDs; only birth/BodyGraph identities and catalog IDs.

* **Indexing.** Governed uses MUST be indexed and mirrored under the Evidence Index discipline, with path-proofs, like other PF12 evidence families.

**Family: `qa.run_bundle.stateless` (optional)**

* **Role.** Provides a single-file “bundle” tying together inputs, BodyGraph exports, and compat exports for a QA run, to simplify reproduction and auditing.

* **Minimum content (names-only).**

  * `schema` — bundle schema tag (e.g. `"hdctl_run_bundle.v1"`).

  * `inputs` — original birth tuples or vendor descriptors.

  * `artifacts` — references (by `artifact_key` and/or file path) to the BodyGraph export and compat export artifacts produced in this run.

  * `meta` — minimal identity fields (engine\_tag, release\_id, invocation\_tag, run\_id).

* **Canonical JSON.** Same canonical JSON posture as other QA families; arrays-as-sets semantics apply to any list of artifact references.

* **Indexing.** When used as governed evidence, bundles are indexed and mirrored like other artifacts; they do not replace indexing of the underlying BodyGraph/compat exports.

**No transport bytes here.**  
 These families define **artifact shapes and governance**, not CLI flags or HTTP contracts. CLI command names, flags (for example, a future `hdctl bg:export-json` or pure-mode `showcompat`), and any QA scripts that produce these artifacts are specified in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide; PF12 remains contract-free and schema-first.

**Acceptance (names-only).**  
 When these families are adopted by a future epic, PF12 and PF09 may attach the following hints to them (token semantics live in HDE-Governance):

* `JSON_CANONICAL_CHECK_OK` — canonical JSON checks for stateless QA artifacts.

* `TWO_RUN_IDENTITY_OK` — two-run identity for stateless exports.

* `CLI_SHOWCOMPAT_CANON_OK`, `CLI_STDOUT_LF_OK`, `CLI_READER_PARITY_OK` — when compat exports are wired through the canonical emitter and Reader parity harnesses (titles-only to HDE-CLI-API-Vendor-Ref / HDE-Math-Spec).

* `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_HASH_OK` — Index/Mirror parity and path-proof discipline including these families.

Governance and QA docs (PF04, PF09, PF19, PF20) refer to these families by name (`qa.bodygraph_export.stateless`, `qa.compat_export.stateless`, `qa.run_bundle.stateless`) and must not define parallel path lists.

## **8.14 Config artifacts & acceptance map (D5) \[Required−Now\]**

**Purpose.**  
 Record the governed **config artifact families** and the **config acceptance map** introduced in D5 of HDE-EPIC018 and tie them into the Evidence Catalog and Machine Mirror. These artifacts are generated under closed rails using the hardened registry loader and canonical serializer, and they provide the concrete evidence surfaces for config-related acceptance tokens (names-only; semantics live in Glow QA Guide and HDE-Governance).

**Scope.**

This section covers:

* `artifacts/thresholds/magic10_config.json` — governed Magic-10 config snapshot.

* `artifacts/thresholds/band_edges.json` — governed band-edges config snapshot.

* `audit/EPIC-018_config_acceptance_map.json` — governed PF09-style config acceptance map for HDE-EPIC018.

The registry report at `artifacts/registry/registry_report.json` is governed separately in §8.5; this section only cross-references it where needed.

---

### **8.14.1 Magic-10 config artifact (`config.magic10`)**

**Path (fixed).**  
 `artifacts/thresholds/magic10_config.json`

**Role and `artifact_key`.**

* Mirror `artifact_key`: `"config.magic10"` (names-only).

* Mirror `role`: `"snapshot"`.

**Generation and env rails (titles-only).**

* Generated by `tools/config/generate_config_artifacts.py` under closed rails:

  * `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

* Uses the hardened registry loader and the shared canonical serializer (per §4) to ensure deterministic bytes and two-run identity.

**Canonical JSON and schema tag.**

`artifacts/thresholds/magic10_config.json` **MUST**:

* Be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Contain a top-level `schema` field whose value **MUST** equal `"magic10_config.v1"`.

* Use field shapes and types pinned by the owning JSON Schema for this artifact (names-only; the schema file is referenced here by title, not path).

**Content (names-only, from Addendum 6).**

At minimum, the Magic-10 config JSON **MUST**:

* Capture the normative Magic-10 order as a closed list matching the Magic-10 catalog (§2.6) — ten category IDs in the pinned order.

* Record per-category caps as **integer bounds** for all categories (inputs \+ integer limits); details of the cap object shape are governed by the config schema and tests, not restated here.

* Include seed metadata for each Magic-10 category with at least the fields:

  * `template_id` — string;

  * `seed_version` — integer or string version identifier;

  * `updated_at_utc` — UTC ISO-8601 timestamp string;

  * `checksum_sha256` — lowercase 64-hex digest of the seed’s canonical bytes.

The config **MUST NOT** introduce new Magic-10 IDs; all IDs must belong to the closed domain defined in the Magic-10 catalog (§2.6, §3.3). Any unknown ID is a hard error.

---

### **8.14.2 Band-edges config artifact (`config.band_edges`)**

**Path (fixed).**  
 `artifacts/thresholds/band_edges.json`

**Role and `artifact_key`.**

* Mirror `artifact_key`: `"config.band_edges"` (names-only).

* Mirror `role`: `"snapshot"`.

**Generation and env rails (titles-only).**

* Generated by `tools/config/generate_config_artifacts.py` under the same closed-rails profile as `config.magic10` (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`).

* Uses the shared canonical serializer; two-run identity must hold for this artifact as well.

**Canonical JSON and schema tag.**

`artifacts/thresholds/band_edges.json` **MUST**:

* Be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Contain a top-level `schema` field whose value **MUST** equal `"band_edges.v1"`.

* Include top-level fields for:

  * band names and edges,

  * clamp policy,

  * rounding mode, and

  * version \+ a source pointer back to `math/thresholds.json`,

* with exact field names and types pinned by the owning JSON Schema; PF12 does not restate the full schema.

**Content (names-only, from Addendum 6).**

At minimum, the band-edges config JSON **MUST**:

* Enumerate the band names and the numeric edges used for banding, in a form consistent with the engine’s band constants (names-only; arithmetic remains in Math).

* Encode clamp behavior and rounding mode (for example, how values at or beyond the defined edges are handled and how intermediate values are rounded) in explicit fields governed by the schema.

* Include a version identifier for the band-edges config itself and a pointer back to `math/thresholds.json` indicating which thresholds source this config was derived from.

Any mismatch between band edges and `math/thresholds.json` (for example, missing bands, unsorted edges, or incompatible ranges) is a hard error in the config tests and should be treated as a spec violation.

---

### **8.14.3 EPIC-018 config acceptance map (`epic018.config.acceptance_map`)**

**Path (fixed).**  
 `audit/EPIC-018_config_acceptance_map.json`

**Role and `artifact_key`.**

* Mirror `artifact_key`: `"epic018.config.acceptance_map"` (names-only).

* Mirror `role`: `"snapshot"`.

**Purpose.**  
 Record, in canonical JSON, the mapping between PF09 config tasks, governed config artifacts, config-related acceptance tokens, and the tests that uphold them for HDE-EPIC018 D5.

**Canonical JSON and shape.**

`audit/EPIC-018_config_acceptance_map.json` **MUST**:

* Be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Use a top-level JSON object where each property name is a PF09 task ID string (for example, `"HDE-CALC004"`, `"HDE-CALC004.3"`, `"HDE-CALC004.7"`).

* Map each task ID to an object with at least the following fields:

  * `artifact_key` — string; **MUST** be one of the governed config or registry artifact keys (for example `"registry.registry_report"`, `"config.magic10"`, `"config.band_edges"`).

  * `tokens` — array of strings; acceptance token names (names-only) relevant to the task (for example, `CONFIG_REGISTRY_OK`, `CONFIG_MAGIC10_OK`); array-as-set semantics apply (dedupe \+ ASCII sort).

  * `test_names` — array of strings; names or paths of tests that uphold the mapping (for example, `tests/config/test_config_artifacts.py::test_magic10_config_snapshot`); array-as-set semantics apply.

The exact set of allowed task IDs, artifact keys, token names, and test names is constrained by PF09, PF19, PF04, and the test suite; config acceptance-map tests enforce that:

* Every task ID named in the map is a known PF09 task ID.

* Every `artifact_key` corresponds to an artifact listed in the Evidence Index (§8.6) and Appendix C.

* Every `tokens[]` entry is a known token name (semantics live in Governance/QA).

* Every `test_names[]` entry refers to an existing test artifact (file and, when encoded, node).

**Indexing and parity.**

All three config families in this section **MUST** participate in the standard Evidence Index/Mirror discipline:

* **Human Index.** `docs/evidence/INDEX.json` **MUST** include entries with the following `(artifact_key, discovered_physical_path)` pairs:

  * `("config.magic10", "artifacts/thresholds/magic10_config.json")`

  * `("config.band_edges", "artifacts/thresholds/band_edges.json")`

  * `("epic018.config.acceptance_map", "audit/EPIC-018_config_acceptance_map.json")`

* and `docs/evidence/INDEX.sha256` **MUST** be updated in the same PR as any change to these artifacts or their paths.

* **Machine mirror.** `artifacts/evidence_index.jsonl` **MUST** contain canonical JSONL records for each of the above artifact keys with:

  * `artifact_key`,

  * `role` (`"snapshot"` for all three),

  * `discovered_physical_path` equal to the paths above,

  * `sha256` and `size_bytes` matching the artifact’s canonical bytes,

  * `produced_at_utc` reflecting the evidence refresh time, and

  * `proof_anchor` pointing to the matching `.path_proof.txt` transcript alongside each artifact.

Mirror records **MUST** obey §8.3’s schema, field order, sort-before-write, and single-mirror-file rules.

**Path-proof requirements.**

Each of the three artifacts **MUST** have a sibling path-proof transcript:

* `artifacts/thresholds/magic10_config.json.path_proof.txt`

* `artifacts/thresholds/band_edges.json.path_proof.txt`

* `audit/EPIC-018_config_acceptance_map.json.path_proof.txt`

Each transcript **MUST** follow the path-proof schema in §8.3 (exactly one record with `path`, `sha256`, `size_bytes`, `mtime_utc`, `produced_at_utc`) and **MUST** match the mirror record and the artifact bytes exactly.

## **8.15 Config bundles (typed FE/BE) \[Required−Now\]**

**Purpose.**  
 Record the governed **typed config bundles** introduced in D6 of HDE-EPIC018 and tie them into the Evidence Catalog and Machine Mirror. These bundles are deterministic, canonical JSON projections of already-governed config artifacts and registry state, and serve as typed configuration payloads for backend and frontend consumers. They are generated under closed rails and provide the evidence surface for bundle-related acceptance tokens (names-only; semantics live in Glow QA Guide and HDE-Governance).

**Scope.**

This section covers two new governed artifact families:

* `config_bundle.fe` — typed **frontend** config bundle.

* `config_bundle.be` — typed **backend** config bundle.

Concrete bundle files live under `artifacts/config_bundles/` (names-only). Exact filenames are owned by the bundle generator and tests; PF12 governs the **family**, not per-file naming.

---

### **8.15.1 Backend config bundle (`config_bundle.be`)**

**Artifact family.**

* Artifact key (mirror / Evidence Index): `"config_bundle.be"`.

* Role: `"snapshot"` (typed backend bundle).

* Directory: `artifacts/config_bundles/` (filenames owned by the generator; tests and Evidence Index entries pin the exact paths).

**Generation and env rails (titles-only).**

* Generated by `engine/config/bundles.py` and `tools/config/generate_bundles.py`.

* Generation **MUST** run under the same closed-rails profile used for D5 config artifacts:

  * `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

* Bundles are built exclusively from:

  * governed Magic-10 config (`config.magic10`),

  * governed band-edges config (`config.band_edges`), and

  * the registry report (`registry.registry_report`),

* via the hardened registry loader (titles-only to Mechanics/Registry).

**Canonical JSON and schema tag.**

Each backend bundle JSON **MUST**:

* Be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Contain a top-level `schema` field whose value **MUST** equal `"config_bundle.be.v1"`.

* Use field shapes and types pinned by the local JSON Schema used in tests (titles-only; schema files live under `docs/schemas/` and are not PF12-canonical yet).

**Content (names-only, from Addendum 7).**

At minimum, the backend bundle **MUST** contain:

* A Magic-10 section that **matches** the governed `config.magic10` artifact semantically:

  * normative Magic-10 order,

  * per-category caps for all ten categories, and

  * seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256).

* A band-edges section that **matches** `config.band_edges` semantically:

  * band names and edges,

  * clamp policy,

  * rounding mode,

  * version and a pointer to the source thresholds (names-only).

* Full topology slices aligned with the registry report:

  * channel objects with at least the fields `id`, `gates`, `centers`, `circuit_primary`, `substream`, `primary_domain`, `domains`, `flags` (exact field set pinned by schema/tests), where:

    * `id` **MUST** be a canonical channel ID (`NN-NN` or multi-pair string) consistent with the Channels catalog, and

    * center/domain/circuit values **MUST** be consistent with the registry report and catalogs (titles-only to §2.1/§3.2).

  * center records and domain lists consistent with the registry report.

  * an `alias_policy` block whose semantics match the registry’s alias policy (titles-only; details governed by Mechanics/Registry).

PF12 does **not** restate the full JSON shape; concrete field definitions are owned by the bundle schemas and tests. The requirements above are names-only semantic constraints.

**Sources block.**

Each backend bundle **MUST** include a `sources` object that records, for each upstream governed artifact:

* an entry for the Magic-10 config (`config.magic10`),

* an entry for the band-edges config (`config.band_edges`), and

* an entry for the registry report (`registry.registry_report`).

Each `sources` entry **MUST** contain at least:

* `path` — the artifact’s repo-relative path (for example, `artifacts/thresholds/magic10_config.json`).

* `sha256` — lowercase 64-hex digest of the artifact’s canonical bytes.

* `size_bytes` — integer byte length of the artifact’s canonical bytes.

Tests MUST assert that these `path/sha256/size_bytes` triples match the current governed artifacts; any mismatch is an error.

**Two-run identity.**

Generating the backend bundle twice over the same inputs and code under closed rails **MUST** produce identical bytes. Bundle tests (names-only) MUST assert two-run identity and canonical JSON for this artifact.

---

### **8.15.2 Frontend config bundle (`config_bundle.fe`)**

**Artifact family.**

* Artifact key (mirror / Evidence Index): `"config_bundle.fe"`.

* Role: `"snapshot"` (typed frontend bundle).

* Directory: `artifacts/config_bundles/` (filenames owned by the generator; tests and Evidence Index entries pin the exact paths).

**Generation and env rails.**

* Generated by the same bundle generator (`engine/config/bundles.py` \+ `tools/config/generate_bundles.py`) under the same closed-rails profile as the backend bundle.

* Derived exclusively from the same governed config artifacts and registry report as the backend bundle; no additional config sources.

**Canonical JSON and schema tag.**

Each frontend bundle JSON **MUST**:

* Be canonical JSON per §4.

* Contain a top-level `schema` field whose value **MUST** equal `"config_bundle.fe.v1"`.

* Conform structurally to the local frontend bundle JSON Schema used in tests (titles-only; schema lives under `docs/schemas/`).

**Content (names-only, from Addendum 7).**

At minimum, the frontend bundle **MUST** contain:

* Magic-10 content sufficient for client usage:

  * Magic-10 order and per-category caps consistent with the backend bundle and `config.magic10`.

* Band-edges content sufficient for client usage:

  * band names, edges, clamp behavior, rounding mode, version, and a pointer to the thresholds source, consistent with `config.band_edges`.

* A trimmed topology view:

  * channel identifiers (IDs) with associated center/domain information such that:

    * the set of channel IDs **MUST** equal the `channel_ids` recorded in the registry report’s `artifacts.registry` section, and

    * centers/domains/alias policy information is consistent with the backend bundle and registry report.

* An `alias_policy` section aligned with the registry report.

* A `sources` object with the same structure and constraints as the backend bundle’s `sources` block (entries for Magic-10 config, band-edges config, and registry report, each with `path`, `sha256`, `size_bytes` matching the governed artifacts).

**Two-run identity.**

Generating the frontend bundle twice over the same inputs and code under closed rails **MUST** produce identical bytes. Bundle tests MUST assert two-run identity and canonical JSON for this artifact.

---

### **8.15.3 Indexing, path-proofs, and tokens**

Both bundle families **MUST** participate in the standard Evidence Index/Mirror discipline:

* **Human Index** (`docs/evidence/INDEX.json`):

  * For each concrete frontend bundle file under `artifacts/config_bundles/`, there **MUST** be an entry with:

    * `artifact_key: "config_bundle.fe"`,

    * `discovered_physical_path` equal to that file’s repo-relative path.

  * For each concrete backend bundle file under `artifacts/config_bundles/`, there **MUST** be an entry with:

    * `artifact_key: "config_bundle.be"`,

    * `discovered_physical_path` equal to that file’s repo-relative path.

  * `docs/evidence/INDEX.sha256` **MUST** be updated in the same PR as any change to bundle paths or bytes.

* **Machine mirror** (`artifacts/evidence_index.jsonl`):

  * **MUST** contain canonical JSONL records for `config_bundle.fe` and `config_bundle.be` with:

    * `artifact_key` set to `"config_bundle.fe"` or `"config_bundle.be"` as appropriate,

    * `role:"snapshot"`,

    * `discovered_physical_path` equal to the bundle path recorded in the Human Index,

    * `sha256`, `size_bytes` computed from the bundle’s canonical bytes,

    * `produced_at_utc` reflecting the evidence refresh time, and

    * `proof_anchor` pointing to the bundle’s `.path_proof.txt`.

  * Mirror records **MUST** obey all §8.3 rules (field set, ASCII field order, sort-before-write, single mirror file, unknown-key rejection).

* **Path-proofs**:

  * Each concrete frontend bundle file MUST have a sibling path-proof transcript named `<bundle_file>.path_proof.txt` stored alongside the bundle file, whose `path`, `sha256`, `size_bytes`, `mtime_utc`, and `produced_at_utc` match the bundle’s canonical bytes and mirror record.

  * The same requirement applies to backend bundle files.

**Acceptance hints (names-only).**

PF12 does not own token semantics, but these bundles are the governed surface for bundle-related tokens, including:

* `CONFIG_BUNDLES_DETERMINISTIC_OK` — typed frontend and backend bundles are generated under closed rails from governed config artifacts and registry report, are canonical JSON, satisfy two-run identity, and contain a `sources` block whose `path/sha256/size_bytes` entries match the current governed artifacts.

Tokens and detailed CI policy live in Glow QA Guide and HDE-Governance; PF12 binds these tokens to the `config_bundle.fe` and `config_bundle.be` families by **artifact key, directory, and sources linkage**, not by test names.

## **8.16 Repo implementation docs (non-canonical) \[Required−Now\]**

**Purpose.**  
 Record the role and limits of **repo-level implementation documents** that describe PF12-owned artifacts and rails (for example, README, AGENTS, and selected `./docs/**` files) so that they remain consistent with this document without becoming parallel sources of truth.

These docs are **not canon**. They exist to help humans run and reason about the EPIC018 engine and evidence harness; PF12 remains the single home for schemas, governed artifact families, and Evidence Catalog entries.

---

### **8.16.1 Non-canonical implementation docs (titles/paths only)**

The repository contains implementation-level docs that describe PF12-governed behavior for EPIC018:

* Top-level docs

  * `README.md` — EPIC018-centric engine overview; lists D1–D7 outcomes and gives a closed-rails “quickstart” and evidence-harness workflow.

  * `CHANGELOG.md` — includes an EPIC018 entry summarizing deterministic rails, CLI guards, evidence skeleton and sanity pipeline, governed config artifacts, typed bundles, and the manifest/close report.

  * `AGENTS.md` — operational guidance for Codex/dev agents under EPIC018 rails (closed env, single emitter/serializer, CLI guards, evidence tools, and close-out workflow).

* Evidence posture crib

  * `docs/evidence/EPIC018_evidence.md` — implementation-level view of the EPIC018 evidence skeleton, orientation demo, sanity pipeline, and evidence-update commands. It explains **how** to run the harness and **where** artifacts live, but **must not** redefine schemas, canonical JSON rules, or token semantics already owned by PF12, Glow QA Guide, or Governance.

* Config and bundles crib

  * `docs/config_and_bundles.md` — implementation-level view of:

    * D5 governed config artifacts (`config.magic10`, `config.band_edges`, `registry.registry_report`) and the EPIC018 config acceptance map (`epic018.config.acceptance_map`), and

    * D6 typed FE/BE config bundles (`config_bundle.fe`, `config_bundle.be`) and their local JSON Schemas under `docs/schemas/`.  
       This doc explains **how** to generate and inspect these artifacts using the canonical tools, but PF12 §8.5, §8.14, and §8.15 remain the single homes for their families, canonical JSON posture, and Evidence Index/Mirror behavior.

* Runbook and index cribs

  * `docs/INDEX.md` — repo-level index that points to EPIC018 close-out artifacts (manifest, close report, config acceptance map) and the evidence/tooling surfaces described in §8 (Evidence Index, orientation demo, sanity pipeline, CLI guards, config/bundle generators, determinism helper).

  * `docs/RUN.md` — EPIC018-aligned developer flight checks (env pins, serializer parity, evidence & guard workflow, config and bundle generation), expressed as **operational steps** that must remain consistent with PF12 §4, §6, and §8 but never override them.

Other architecture/CLI docs under `docs/architecture/**` and `docs/CLI_*.md` reference PF12-governed artifacts (for example, emitter/serializer guardrails, CLI guards, evidence coupling) **by title only** and must defer to PF12 and PF-Canon for normative rules.

---

### **8.16.2 Constraints on repo docs (must follow PF12)**

These implementation docs **MUST** obey the following constraints:

* **Non-canonical status.**

  * Repo docs (`README.md`, `AGENTS.md`, `CHANGELOG.md`, `docs/INDEX.md`, `docs/RUN.md`, `docs/config_and_bundles.md`, `docs/evidence/EPIC018_evidence.md`, and related `./docs/**` files) are **not** part of PF-Canon.

  * When they conflict with PF12 or other PF documents, the PF documents **win**; the drift is a bug in the repo docs and must be fixed there.

* **Titles-only routing.**

  * Repo docs **MUST** reference PF documents **by title only** (for example, “HDE-Schemas and Artifacts”, “Glow QA Guide”, “HDE-Phased Epics”, “Epic-Process-Guide”) and **MUST NOT** inline or restate canonical schemas, Evidence Index field sets, or acceptance token definitions.

  * Any normative claim about schemas, canonical JSON rules, Evidence Index/Mirror behavior, or token semantics **must** appear in PF-Canon, not in repo docs.

* **No parallel Evidence Catalog.**

  * Repo docs **MUST NOT** maintain independent, authoritative lists of governed evidence paths or artifact families.

  * The single home for governed artifact families and titles/paths is **PF12 §8.x and §8.6**; any lists in repo docs must explicitly be framed as **summaries** or **cribs** and must be kept in sync with PF12 or removed.

* **No token ownership.**

  * Repo docs **MUST NOT** introduce new acceptance token names, redefine token semantics, or change which artifacts a token covers.

  * Token names and meanings remain owned by **HDE-Governance** and **Glow QA Guide**; PF12 provides names-only hints and bindings to artifacts (§0.2, §8), not token semantics.

* **Path lists are illustrative only.**

  * Where repo docs list specific artifact paths (for example, config artifacts under `artifacts/thresholds/`, bundles under `artifacts/config_bundles/`, or evidence reports under `artifacts/**` / `audit/**`), those lists are **illustrative** and **must** match the authoritative lists in PF12 §8.5, §8.6, §8.14, §8.15 and Appendix C.

  * If a path appears in repo docs but not in PF12’s Evidence Catalog, treat it as **non-governed** until a PF12 Doc-Delta adds it.

---

### **8.16.3 Doc-Delta expectations**

Repo docs themselves do **not** require a Doc-Delta when they change wording or flow, but:

* Any change to **governed artifacts**, **Evidence Index entries**, **Machine Mirror records**, **config artifacts**, or **typed bundles** still requires a Doc-Delta per §9, regardless of whether a repo doc mentions those artifacts.

* If a change **relies** on a new repo doc (for example, adding `docs/config_and_bundles.md` as the implementation crib for D5/D6 config/bundles) and that change also adjusts governed artifacts or Evidence Index entries, the Doc-Delta **MUST** name both:

  * the PF12 sections it affects (for example, §8.5, §8.14, §8.15, §8.6, Appendix C), and

  * the new or updated repo docs (by path) as **implementation references only**.

## 8.17 Live QA evidence layout (audit/qa//…) \[Required−Now\]

Purpose.  
Standardize the layout and naming of Live QA evidence under the governed `audit/**` root so that:

* Live QA artifacts are easy to locate and reason about across epics and attempts.  
* Evidence promoted to governed status can be indexed and mirrored consistently.  
* The QA process can rely on predictable naming without re-specifying it per epic.

Path provenance (normative).  
 Live QA plans and runbooks MUST NOT list a file path as “required” unless the path is one of:

* **Canon-defined** — the path (or path-pattern) is explicitly defined by PF canon (including this section and the Evidence Index entries catalog), or

* **Audit-proven** — the path’s existence is already proven by an existing governed artifact family, or

* **QA-created** — the plan includes inline creation instructions and validation for the path.

Proven or created, otherwise forbidden (MUST).  
 If a path is not canon-defined and not audit-proven, it MUST either be created under QA with explicit instructions and justification, or it MUST NOT appear in the plan.

QA-created path requirements (MUST).  
 When a plan requires QA to create a file that has no prior canonical existence, the relevant step MUST include:

* exact `mkdir` / write instructions (no placeholders),

* a one-line purpose (what the file proves and why it exists),

* explicit PASS and FAIL predicates tied to the file’s contents.

QA write scope (MUST).  
 QA MAY create folders/files only under `audit/**` or `artifacts/**`.

Pre-existing vs QA-run artifacts (MUST).  
 Plans MUST separate pre-existing artifacts (expected to exist before execution) from QA-run artifacts (created during execution).

Preflight presence gating (MUST).  
 Preflight “presence” checks MUST only gate on pre-existing artifacts. A QA-run artifact MUST NOT be required in preflight unless the plan also creates it in that same preflight step.

New standardized evidence families (MUST).  
 If a new recurring QA evidence family/path is needed, it MUST be introduced via Glow HD Engine Build Notes addendum (or the owning PF canon home), then drained into the owning PF document, before plans may require it.

Scope / root.  
The canonical root for Live QA evidence is:

* `EPIC_QA_ROOT = audit/qa/<epic-id>/`

Within `EPIC_QA_ROOT`, evidence is organized primarily by **check\_id** (current-state), with a stable epic-level manifest at:

* `audit/qa/<epic-id>/qa_step_logs_manifest.json`

Run-id discipline is **not** a correctness mechanism. Per-run directories MAY exist for convenience/history retention, but are optional and non-canon. The governance posture is current-state indexing by `check_id`.

This section does not define:

* Live QA rails posture, D-goal semantics, or QA tokens (titles-only routing to Glow QA Guide, HDE-Phased Epics, HDE-Governance, and HDE-Build Checklist).  
* Which specific Live QA artifacts must be indexed in the Evidence Index/Mirror; that remains governed by the QA source-of-truth documents and epic-specific plans.

Current-state vs history retention (normative).  
Under `audit/qa/<epic-id>/…`:

* **Current-state evidence** is the set of artifacts referenced by `qa_step_logs_manifest.json` as the latest authoritative results for each `check_id`.  
* **History retention** MAY be stored under an optional `runs/<run_id>/…` subtree. These retained copies are non-canon by default and must not be required for closure claims.

Tools MUST NOT infer run state by enumerating subdirectories under `audit/qa/<epic-id>/`. The manifest is the authoritative index of current-state step evidence.

---

### **8.17.1 Root and step directories**

Epic QA root (per epic).  
 Each epic’s Live QA area lives under:

* `EPIC_QA_ROOT = audit/qa/<epic-id>/`

`EPIC_QA_ROOT` MUST use lower-case ASCII directory names for fixed directory slugs (for example `00_meta/`, `checks/`, `results/`). Per-check directories under `checks/` are named by the `check_id` token and are exempt from the lower-case rule (see Directory name rules).

`EPIC_QA_ROOT` MAY contain:

* `00_meta/` — stable, mechanically produced epic-level QA metadata (for example, baseline rails/env pins capture, optional debugging captures).

* `checks/` — current-state per-check directories (one directory per `check_id`). Each check directory contains `primary.log` and MAY contain auxiliary `tmp_*` supporting files or plan-owned outputs.

* `results/` — current-state step outputs and verdict artifacts (names-only; plan-owned).

* `snapshots/` — run-local convenience copies of governed artifacts and headers (names-only; non-canon).

* `closeout/` — current-state closeout summaries (names-only; plan-owned).

* `remediation/` — remediation-only staging (if present); excluded from governed Evidence Index/Mirror unless explicitly governed elsewhere.

Planning-trace deliverables (hard rule).  
 Live QA Plans MUST NOT include any required deliverable whose sole purpose is “PF23 consult capture.” Planning consult capture is planning-time only and is not a governed member of the `audit/qa/<epic-id>/…` evidence layout.

Optional per-run subtree (history retention only).  
 A per-run subtree MAY exist at:

* `audit/qa/<epic-id>/runs/<run_id>/...`

If present, it MAY mirror the same directory names (`00_meta/`, `checks/`, `results/`, `snapshots/`, `closeout/`) for that attempt. This subtree is optional and non-canon unless the QA plan explicitly promotes specific artifacts within it to governed evidence.

Directory name rules.  
 Directory names created under `audit/qa/<epic-id>/…` MUST be lower-case ASCII for fixed directory slugs. Use `-` as the default separator for new plan-owned directory slugs.

Exception (check\_id directories).  
 Directories under `audit/qa/<epic-id>/checks/` MUST use the exact `check_id` string (case-sensitive) as the directory name (for example `checks/D08_qa_doc_deltas_capture/`). The allowed character set for `check_id` directory names is: `A–Z`, `a–z`, `0–9`, `_`, and `-`. The `check_id` directory name MUST match the `check_id` used for manifest keying.

---

### **8.17.2 Primary step logs and emptiness rules**

Mechanical, not hand-edited (governed evidence rule).  
 Any Live QA artifact treated as QA evidence (for example: indexed, mirrored, or referenced as acceptance evidence) MUST be produced by commands (shell/scripts/CLI tools). Manual editing in an editor is prohibited for artifacts treated as evidence.

Placeholders that imply later human fill (for example, `(fill PASS/FAIL)` or “fill manually as run proceeds”) are non-conforming in approved QA evidence templates.

If a Live QA run requires summary or RCA artifacts, they MUST be generated mechanically from machine-readable inputs (for example: step exit codes, step logs, existence checks), not by human fill.

Primary log per check\_id (current-state).  
 Each Live QA check that produces evidence MUST have exactly one current-state primary log file referenced by `qa_step_logs_manifest.json` for that `check_id`.

Primary log location (canonical).  
 Primary logs MUST live at:

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`

The directory `checks/<check_id>/` is the check-scoped home for the check. The `<check_id>` directory name MUST match the `check_id` used for manifest keying (see §8.17.1).

Primary log filename (normative constraints).

* The primary log filename is fixed: `primary.log`.

* The log’s header (format owned by QA source-of-truth documents) MUST include the true `check_id` used for manifest keying.

Non-empty requirement.  
 The primary log for a check MUST be a non-empty, LF-terminated text file. It MUST NOT be zero bytes.

If a step fails to complete or tooling fails, the primary log MUST STILL be written and MUST contain at least:

* a short summary of what the check attempted, and

* a terse failure description and/or final status line consistent with Live QA status semantics (for example, PASS/FAIL\_BEHAVIOR/FAIL\_TOOLING/TOOLING\_BLOCKED).

It is an error for a planned check to have no primary log at all.

Empty files.  
 Governed Live QA evidence files under `audit/qa/<epic-id>/…` MUST NOT be empty:

* If a planned artifact is not produced, the file MUST be absent rather than present with size 0\.

* Path-proofs and Machine Mirror records MUST NOT point to zero-byte QA artifacts.

Exception: Sentinel files MAY be empty if clearly marked as sentinel and MUST NOT be referenced by the Human Evidence Index, Machine Mirror, or acceptance binding surfaces.

---

### 8.17.3 Supporting files and `tmp_*` naming

Supporting files (auxiliary; not canonical per-step).  
A Live QA check MAY produce additional supporting files (for example, JSON request bodies, sorted ID lists, raw CLI outputs). These files are auxiliary and do not replace the primary log.

Any supporting file SHOULD:

* live under `audit/qa/<epic-id>/results/` or a check-scoped subdirectory, and  
* use a `tmp_` prefix (for example, `tmp_http_request.json`, `tmp_sorted_ids.txt`, `tmp_cli_output.txt`).

Where a supporting file materially contributes to proof, the primary log SHOULD:

* mention the filename explicitly, and  
* briefly describe how it is used.

Canonical per-check surface.  
For acceptance and audit purposes, the primary log remains the canonical per-check artifact. Supporting files are auxiliary unless separately promoted to governed evidence by the owning evidence catalog and indexed/mirrored accordingly.

### **8.17.4 Env/rails snapshots and D-goal linkage**

Env/rails snapshots (current-state).  
 Env/rails snapshot data MUST be captured mechanically for the Live QA run. To preserve a minimal required output set, the required capture surface is the per-check `primary.log` (see §8.17.2): the primary log SHOULD include the relevant rails/env pins in a machine-grep-friendly header block.

Separate snapshot files under `audit/qa/<epic-id>/…` MAY be produced (recommended: under `00_meta/` for baseline and under `results/` for per-check snapshots), but they are optional and MUST NOT be required for closure unless explicitly promoted as acceptance-decisive governed evidence.

Each snapshot (whether embedded in a primary log header or stored as a standalone text artifact) MUST clearly record, at minimum, values of:

* SAFE\_MODE

* ALLOW\_NETWORK

* APP\_ENV

* LC\_ALL

* LANG

* TZ

in a machine-parsable form consistent with the QA rails pins.

D-goal/token references (titles-only).  
 When a Live QA artifact is intended to satisfy or inform a specific D-goal or token:

* the corresponding primary log SHOULD include a short, machine-grep-friendly header line stating the D-goal and token names (names-only), and

* acceptance wiring documents SHOULD reference the check\_id and primary log path by title only (titles-only routing).

Ownership of semantics.  
 PF12 standardizes layout and naming only. Semantics for:

* rails posture and env pins,

* D-goals and QA tokens, and

* Live QA workflows and status classifications (for example, PASS/FAIL\_BEHAVIOR/FAIL\_TOOLING/TOOLING\_BLOCKED),

remain owned by the QA source-of-truth documents and are referenced here by title only.

### **8.17.5 Codespaces snapshot (Step-0; current-state) \[Optional\]**

Status (normative).  
 This artifact is OPTIONAL. Live QA Plans MUST NOT require it for closure by default.

If it is produced and treated as governed evidence, it MUST be generated by commands and MUST NOT be hand-edited (see §8.17.2), and it MUST conform to the canonical bytes and schema rules below.

Purpose.  
 If produced, provide a single, mechanically generated snapshot of the Codespaces execution context at the start of Live QA so later review can see:

* determinism and rails posture (pins and rails variables),

* tooling versions used for the run,

* presence-only status for required secrets and env keys,

without leaking secret values.

Canonical path (current-state; epic-level).  
 `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`

Optional per-run copy (non-canon; allowed).  
 A run-scoped copy MAY exist at:  
 `audit/qa/<epic-id>/runs/<run_id>/snapshots/codespaces_snapshot.json`  
 If both exist for a given attempt, they MUST be byte-identical.

Run-id discipline note (normative).  
 `run_id` is optional metadata and MUST NOT be used as a governance key. The epic-level current-state snapshot is authoritative; run directories are optional retention only.

Canonical JSON (required).

* UTF-8, no BOM.

* ASCII-sorted keys at every object level.

* Compact separators.

* Exactly one trailing LF.

* No ANSI sequences.

Schema (minimum; reject unknown keys).  
 `codespaces_snapshot.json` MUST be a JSON object with exactly the keys below:

* `schema` — string, MUST equal `"codespaces_snapshot.v1"`.

* `captured_at_utc` — string, UTC ISO-8601 (`YYYY-MM-DDThh:mm:ssZ`).

* `epic_id` — string (for example `hde-epic022`).

* `run_id` — string or null.

  * If present as a string, it MUST be a UTC timestamp label (for example `20251221T031045Z`).

  * It MUST NOT be required for correctness and MUST NOT be used for keying.

* `rails` — object with exactly:

  * `SAFE_MODE` — integer or boolean (effective value).

  * `ALLOW_NETWORK` — integer or boolean (effective value).

  * `APP_ENV` — string or null (names-only).

  * `LC_ALL` — string.

  * `LANG` — string.

  * `TZ` — string.

* `tool_versions` — array of objects treated as a set (dedupe \+ ASCII-sort by `tool`):

  * each item MUST be `{ "tool": <string>, "version": <string> }`

  * examples (non-normative): `"python"`, `"pip"`, `"poetry"`, `"os"`

  * tool versions MUST be collected without invoking repository state (no VCS-derived identity).

* `env_presence` — array of objects treated as a set (dedupe \+ ASCII-sort by `name`):

  * each item MUST be `{ "name": <string>, "present": <boolean> }`

  * Values MUST NOT be recorded. Only name and presence boolean.

  * The list of names to include is owned by the Live QA plan (titles-only routing to the QA source-of-truth).

* `notes` — array of strings (optional; names-only; no secrets).

Indexing (when used as governed evidence).  
 When the Codespaces snapshot is used as governed evidence (for example, referenced by acceptance artifacts), the indexed artifact MUST be the epic-level current-state snapshot:

* `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`

Optional per-run copies are history retention and do not need separate indexing unless explicitly promoted by acceptance wiring.

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
* `config.magic10` — Magic-10 configuration snapshot; governed config artifact capturing Magic-10 order, per-category caps (integer bounds), and seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256) under closed rails; canonical JSON; manifest-listed as evidence only (not a pack input). (path: `artifacts/thresholds/magic10_config.json`)

* `config.band_edges` — Band-edges configuration snapshot; governed config artifact capturing band names, edges, clamp behavior, rounding mode, version, and a source pointer back to `math/thresholds.json`; canonical JSON; generated under closed rails. (path: `artifacts/thresholds/band_edges.json`)

* `epic018.config.acceptance_map` — HDE-EPIC018 config acceptance map; PF09-style mapping from config tasks (e.g., HDE-CALC004, HDE-CALC004.3, HDE-CALC004.7) to artifact keys, config-related tokens, and tests; canonical JSON; used to prove that each config task is wired to existing artifacts and real tests only. (path: `audit/EPIC-018_config_acceptance_map.json`)  
* `config_bundle.fe` — Typed frontend config bundle; governed config artifact produced under closed rails from the Magic-10 and band-edges config artifacts plus the registry report; canonical JSON; includes a sources block that records path/sha256/size\_bytes for each upstream governed artifact; used by client-facing components as a read-only projection. (path: JSON file under `artifacts/config_bundles/`)

* `config_bundle.be` — Typed backend config bundle; governed config artifact produced under closed rails from the same governed config artifacts and registry report; canonical JSON; includes full topology slices (channels/centers/domains/alias\_policy) and a sources block with path/sha256/size\_bytes for each upstream governed artifact; used by internal engine/adapter code as a read-only projection. (path: JSON file under `artifacts/config_bundles/`)  
* endpoint\_catalog\_file — Authoritative Endpoint Catalog (records-only) plus checksum. (paths: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`)

* endpoint\_catalog\_snapshot — Reader JSON success-endpoints snapshot; proves success envelopes. (path: `artifacts/reader/endpoints_snapshot.json`)

* endpoint\_env\_gate\_proof — Env-gating proof (headers-only); shows non-prod entries unreachable in prod. (path: `artifacts/proofs/endpoints_env_gate_proof.log`)

* a7\_headers\_get — A7 GET (200) headers snapshot (headers-only). (path: `artifacts/proofs/success_get.txt`)

* a7\_headers\_head — A7 HEAD (200) headers snapshot (headers-only). (path: `artifacts/proofs/success_head.txt`)

* a7\_headers\_304 — A7 304 headers snapshot (headers-only; omits Content-Type and Content-Length). (path: `artifacts/proofs/success_304.txt`)

* a7\_headers\_writers\_errors — Writers/errors posture headers snapshot (no-store, no ETag). (path: `artifacts/proofs/success_writers_errors.txt`)

* reader\_success\_proof — Composite proof JSON for GET/HEAD/304 on Catalog route. (path: `artifacts/proofs/reader_success_get_head_304.json`)

* artifacts/proofs/ops\_refusal\_proof.txt — ops refusal proof capturing why rails were closed and how the system declined a run under closed‑rails posture.

* encoding\_invariance\_probe — Proof that identity (ETag) and effective length are stable across Accept-Encoding. (path: `artifacts/proofs/encoding_invariance.txt`)

* start\_command\_capture — Effective start command captured as bytes \+ sha256. (path: `artifacts/proofs/start_command_capture.txt`)

* env\_inventory — Environment inventory (names-only) proving consulted keys. (path: `artifacts/proofs/env_inventory.json`)

* env\_pins — Environment pins snapshot used for specific runs (LC\_ALL, LANG, TZ). **Does not** satisfy `DETERMINISM_ENV_PINS_OK`; the canonical determinism env pins surface is `audit/gates/determinism/env_pins.log` (see §8.3.3). (path: `artifacts/proofs/env_pins.txt`)

* validator\_outputs — Validator outputs proving config sanity. (path: `artifacts/proofs/validator_outputs.json`)

* internal\_version\_get\_head — /internal/version ops identity proof (headers/body/conditionals). (path: `artifacts/proofs/internal_version_get_head.json`)

* cli\_showcompat\_stdout — Exact showcompat stdout capture (LF-terminated; non-empty on success). (path: `artifacts/cli/showcompat/stdout.json`)

* cli\_showcompat\_stdout\_sha256 — SHA-256 sidecar for the showcompat stdout capture bytes. (path: `artifacts/cli/showcompat/stdout.json.sha256`)

* cli\_showcompat\_args — Names-only capture arguments/env snapshot used by the deterministic generator (no secrets). (path: `artifacts/cli/showcompat/args.json`)

* cli\_showcompat\_generator — Deterministic producer tool for EPIC022 D2 showcompat capture artifacts. (path: `tools/cli/generate_showcompat_artifacts.py`)

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

* canonical\_json\_check — Canonical JSON gate check log. (path: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`)

* canonicalization\_compare — Canonical JSON gate compare log. (path: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`)

* json\_gate\_structured\_record (optional) — Canonical JSON gate structured record (canonical JSON). (path: `audit/gates/json_gate/canonical/json_gate_structured_record.json`)

* evidence\_index\_snapshot — Evidence index snapshot artifact (single-home gate-family surface). (path: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`)  
* topology\_orientation\_demo — Orientation demo transcript and helper reports used as the exemplar for path-proof validation and topology invariants. (paths: `audit/gates/topology/orientation_demo.txt`, `audit/gates/topology/degree_check.log`, `audit/gates/topology/multiplicity_vector.log`)

* env\_matrix\_snapshot — Runtime environment matrix (names-only; capture). (path: `artifacts/runtime/env_matrix.snapshot.json`)

* env\_matrix\_failure — Runtime environment matrix failure envelope (frozen failure). (path: `artifacts/runtime/env_matrix.failure.json`)

* env\_connectivity\_snapshot — Dev-only resolver connectivity snapshot. (path: `artifacts/runtime/env_connectivity.snapshot.json`)

* bodygraph\_source\_selection — Source selection snapshot (names-only; no PII). (path: `artifacts/bodygraph/source_selection.snapshot.json`)

* bodygraph\_invariance\_ab — Provider/source invariance proof (A→B). (path: `artifacts/bodygraph/source_invariance/ab.json`)

* bodygraph\_invariance\_ba — Provider/source invariance proof (B→A). (path: `artifacts/bodygraph/source_invariance/ba.json`)

* bodygraph\_invariance\_summary — Summary of invariance checks. (path: `artifacts/bodygraph/source_invariance/summary.json`)

* close\_pack\_report — EPIC close-out report (scope, tokens PASS roster, merged SHAs). (path pattern: `audit/EPIC-<NNN>_close_report.md`)

* close\_pack\_manifest — Close-pack manifest (artifact keys, sha256, size). (path pattern: `audit/EPIC-<NNN>_MANIFEST.json`)

* sbom\_cyclonedx (optional) — Software Bill of Materials (CycloneDX) with hash. (paths: `sbom/cyclonedx.json`, `sbom/cyclonedx.json.sha256`)

* cli\_preview\_stdout — Admin preview stdout (LF-terminated narrative text; no ANSI). (path: `artifacts/cli/narrative/stdout.txt`)

* cli\_preview\_sidecar — Admin preview sidecar (ids-only; canonical JSON; no prose). (path: `artifacts/cli/narrative/sidecar.json`)

* narratives\_coverage\_10x4 — Router coverage table (10 categories × 4 bands). (path: `audit/gates/narratives/keys_10x4.table.json`)

# **Appendix D — Stateless JSON QA artifacts \[Speculative\]**

**Status:** Speculative — accepted future design, not yet wired.  
 This appendix canonically defines stateless JSON artifact *families* for a future no-DB QA mode, as described in **HDE-Build Notes Addendum 11**.  
 These artifacts are **not required for current acceptance** until a dedicated epic defines concrete paths and schemas.

---

## **D.1 Scope**

This appendix describes the intended artifact families for a **stateless (no-DB) QA mode**:

* A canonical **BodyGraph export JSON** for single-chart QA.

* A canonical **compat export JSON** for compatibility QA.

* An optional composite **run-bundle artifact** that groups per-run JSON exports and proof metadata.

This appendix **does not** fix concrete paths or full JSON schemas.  
 Those will be defined by a future epic and then drained into this appendix as normative detail.

Process, CLI surfaces, and CI flows for stateless QA remain single-homed in:

* **HDE-CLI-API-Vendor-Ref**

* **HDE-Mechanics Guide**

* **Glow QA Guide**

* **HDE-Phased Epics**

---

## **D.2 Artifact families (design, not yet wired)**

### **D.2.1 BodyGraph export JSON**

A canonical JSON document representing a **single BodyGraph**, suitable for round-trip QA without access to the backing database.

Informal expectations:

* Includes the birth/event inputs needed to reconstruct the chart.

* Encodes the derived BodyGraph topology (centers, gates, channels, splits).

* Uses stable identifiers consistent with the catalogs defined elsewhere in PF canon.

Exact field names, nesting, and allowed value ranges are intentionally deferred to a future epic.

---

### **D.2.2 Compat export JSON**

A canonical JSON document representing the **compatibility view** for one or more charts (for example, relationships or composites) in a form that can be evaluated by stateless tools.

Informal expectations:

* Mirrors the compat structures already used by the engine.

* Is sufficient to replay compat scoring and bands in a stateless QA harness.

No precise JSON shape is fixed in this appendix.

---

### **D.2.3 Run-bundle artifact**

An optional composite artifact that groups:

* One or more **BodyGraph export** JSON documents.

* Any corresponding **compat export** JSON documents.

* Minimal metadata required to replay a QA run (for example: tool/version identifiers, rails posture, references to evidence artifacts).

This concept is recorded here to give future work a **canonical home** for its schema.  
 Current PF canon does **not** require this artifact for acceptance.

---

## **D.3 Normative status and gating**

Until a dedicated epic defines concrete JSON schemas and paths:

* These artifact families are **not** referenced by any acceptance token.

* No CI job, QA checklist, or governance rule may treat their presence or absence as a gate.

* Any prototype implementation **MUST** be clearly marked as experimental and **SHOULD** reference:

  * this appendix, and

  * the corresponding entry in **HDE-Build Notes**.

Once schemas and paths are finalized in a future epic:

* This appendix will be updated with full canonical detail (paths and schemas).

* Relevant PF documents will reference this appendix as the **single home** for stateless JSON QA artifact definitions.

