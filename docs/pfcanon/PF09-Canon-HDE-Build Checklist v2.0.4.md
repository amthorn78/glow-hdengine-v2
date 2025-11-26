# 0\) Front Matter

## 0.1 Header

**Title:** PF09-Canon-HDE-Build Checklist

**Version:** v2.0.4

**Status:** Canon

**Effective date:** 2025-11-26

**Last Update Gate:** PF14 Review s22

**Invocation tag:** INV-f2ac55d77ce9aacc

## 0.1 Scope

Build-only, dependency-ordered checklist of HD Engine components and concrete implementation tasks required to reach a stable production run. This list excludes documentation and process chores and focuses on shipping code, wiring transport, enforcing determinism, and proving behavior with runnable evidence. Checklist items are organized by seven alchemical phases (Calcination, Dissolution, Separation, Conjunction, Fermentation, Distillation, Coagulation), and each task/subtask is tagged with a tracking ID of the form `HDE-<PHASE><NNN>` or `HDE-<PHASE><NNN>.<m>` (for example, `HDE-CALC001`, `HDE-CALC001.1`). These IDs are for traceability only and do not imply priority or status.

## **0.2 Conventions**

**Statuses** are canonical and use the following values only:

* **Done** — Required behavior is implemented and evidenced for the slice this row covers.

* **Partial** — Some but not all of the required behavior or evidence for this row is implemented; notes explain the gap.

* **Not done** — Behavior is specified in canon, but implementation and/or evidence are still absent.

* **Consolidation pending** — Behavior exists in multiple slices and must be consolidated under a single epic or harness before it is treated as Done.

* **Optional** — Non-blocking work that may be implemented without gating releases.

**Tracking IDs:**

* Tasks use `HDE-<PHASE><NNN>` (for example, `HDE-CALC001`, `HDE-DISS003`).

* Subtasks use `HDE-<PHASE><NNN>.<m>` (for example, `HDE-CALC001.1`).

* IDs are stable labels only and do **not** imply priority or status.

**“SoT: canon” usage:**

* “SoT: canon” appears only in **Notes**, never in **Status**.

* Use it to mark behavior that is locked by spec (PF01/PF02/PF04/PF12/PF14/PF19/PF20) while implementation and/or evidence for this checklist row are still pending.

**Sequencing pattern:**

* When reasoning about work, prefer the following order: **determinism first → transport parity → evidence**.

* PF09 expresses this sequencing via tasks and subtasks; the underlying math, transport contracts, and token semantics remain in PF canon.

**QA acceptance tokens and ownership:**

* PF09 is a **consumer of token names only**. It does **not** define token semantics.

* Normative definitions and evidence mappings for QA acceptance tokens live in the **QA Acceptance Tokens Library** described in the Glow QA Guide (PF19), with individual tokens owned by Governance, Schemas & Artifacts, Mechanics, and Epics (PF04/PF12/PF14/PF20 and related PF-docs) as appropriate.

* Checklist rows in PF09 refer to tokens by name (for example `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`) to indicate which acceptance gates they participate in; meaning, scope, and proof requirements for each token are taken from the QA token library and its owning PF-docs, not from PF09 itself.

---

## **0.3 Evidence Index and mirror (paths pinned)**

### **0.3.1 Human Index (authoritative)**

* **Human Index.** `docs/evidence/INDEX.json` — titles and paths only; no payload bytes. **Single home for the listing:** see **PF12 §8.6 “Evidence Index entries (titles/paths only)”**. PF09 does **not** duplicate that list.

* **Human Index hash sentinel.** `docs/evidence/INDEX.sha256` — sha256 over the exact bytes of `INDEX.json`. Update in the same PR as the Human Index. **Gate:** `EVIDENCE_INDEX_HASH_OK`.

### **0.3.2 Machine Mirror (records-only)**

* **Machine mirror.** `artifacts/evidence_index.jsonl` — one JSON object per line; canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing `\n`). Unknown keys are rejected. Keep **1:1 parity** with the Human Index; provide path-proofs.

### **0.3.3 Mirror discipline (normative)**

* The machine mirror is **one and only one** file at `artifacts/evidence_index.jsonl`.

* Mirror content is **records-only canonical JSONL**:

  * UTF-8 (no BOM).

  * ASCII-sorted keys.

  * Compact separators.

  * Exactly one LF per record.

  * Unknown keys **rejected**.

  * **Sort-before-write** by `(artifact_key, discovered_physical_path)`.

* **Exact field order** (per PF12/PF10):

   `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

### **0.3.4 Minimum mirror record fields (reject unknown keys)**

Each record in the machine mirror uses at least the following fields; unknown keys are rejected:

{

  "artifact\_key": "",

  "role": "\<proof|golden|snapshot|script|log\>",

  "sha256": "\<lowercase 64-hex\>",

  "size\_bytes": 0,

  "produced\_at\_utc": "",

  "discovered\_physical\_path": "",

  "proof\_anchor": ""

}

### **0.3.5 Field order and write discipline (merge-blocking)**

* **ASCII field order (exact):**

   `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

* **Sort-before-write** by the tuple `(artifact_key, discovered_physical_path)`.

* **Single mirror file:** exactly one `artifacts/evidence_index.jsonl` in the repo.

* **Uniqueness:** the pair `(artifact_key, discovered_physical_path)` is unique; duplicates fail CI.

* **CI gate:** fail the PR on:

  * Missing human↔machine parity.

  * Non-canonical JSONL.

  * Unknown keys.

  * Missing path-proofs.

  * Wrong field order.

  * Unsorted records.

### **0.3.6 Parity and path-proofs**

* **Same-PR parity.** Human Index ↔ Machine Mirror MUST be **1:1** in the **same PR** or commit that adds, moves, or renames artifacts.

* **Path-proofs.** Store a `path_proof.txt` alongside each governed artifact and reference it via `proof_anchor`. The `proof_anchor` MUST exactly match the stored path-proof for that artifact.

* **Governed locations only.** Index artifacts only from governed paths (`artifacts/**`, `audit/**`, `docs/evidence/**`). Transient generator paths (for example `codex/out/**`) are not authoritative and **MUST NOT** be indexed — relocate proofs under `artifacts/**` before gating.

### **0.3.7 Registry report (names-only)**

* `artifacts/registry/registry_report.json` — canonical JSON; kept in sync and mirrored.

### **0.3.8 Governed record types**

* **Single home:** **PF12 Appendix C “Governed artifact record types.”** PF09 does not define or duplicate governed record type schemas.

### **0.3.9 Locale pins for all byte checks**

* All mirror/index checks and governed byte comparisons run with:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

---

## **0.4 A7 proof surface (titles-only pointers)**

### **0.4.1 Single home (location & scope)**

* **Catalog file.** `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256`.

* **Scope.** List **JSON success routes only**, each with an env-gate; **exclude all `/internal/*`**.

* **Proof surface.** A7 proofs run **only** on a route listed in the Catalog.

### **0.4.2 Env-gating proof (headers-only)**

* `artifacts/proofs/endpoints_env_gate_proof.log` shows that non-prod entries are unreachable in prod.

* Index in Human \+ Machine evidence in the same PR.

### **0.4.3 A7 invariants to prove (headers-only)**

For the Catalog JSON success route under test:

* **200\.**

  * Strong **quoted** `ETag`.

  * `Vary: Authorization, Accept-Encoding`.

  * Policy-compliant success cache headers.

* **HEAD.**

  * Status 200; no body.

  * Validators mirror 200\.

  * `Content-Type == GET`.

  * `Content-Length == len(identity 200 body)`.

* **304\.**

  * Only after a prior 200 for the same resource.

  * **Omit** `Content-Type`.

  * **Omit** `Content-Length`.

  * Validators mirror the cached 200\.

* **Encoding invariance.**

  * For the same canonical LF-terminated body, ETag identity and effective `Content-Length` are stable across accepted encodings (identity/gzip/br).

* **Writers/errors posture.**

  * Writers and error routes carry `Cache-Control: no-store`.

### **0.4.4 Artifacts (headers-only; one LF each)**

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_encoding_invariance.txt`

* `artifacts/proofs/success_writers_errors.txt`

Capture on a Catalog route; index Human+Machine in the same PR. The machine mirror remains records-only canonical JSONL (unknown-key rejection; each record has a `proof_anchor`).

### **0.4.5 Transport guidance — A7 rows & Catalog tie-in**

* A7 rows apply **only** to routes declared in `docs/ENDPOINTS_CATALOG.json`.

* `/internal/*` routes (including `/internal/version`) are never Catalog-eligible and are verified under ops posture: `Cache-Control: no-store`, no `ETag`, HEAD 200 parity, conditionals ignored.

* When capturing A7 proofs:

  * Always cite the Catalog entry used.

  * Include the env-gate proof in the same PR.

  * Ensure all artifacts are indexed and mirrored under the Evidence Index discipline above.

### **0.4.6 A7/Catalog acceptance (titles-only)**

A7/Catalog gating uses the following Governance tokens (names-only):

* `ENDPOINTS_CATALOG_OK`

* `ENDPOINTS_CATALOG_ENV_GATE_OK`

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

---

## **0.5 Index & mirror discipline**

Update the Human Evidence Index (`docs/evidence/INDEX.json`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) in the **same PR** whenever governed artifacts are added, moved, or removed. Mirror rules:

* Records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF).

* Unknown keys rejected.

* Each record includes `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a co-located path-proof file.

Locale pins apply to all byte checks: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Index/mirror acceptance (titles-only; tokens live in HDE-Governance / HDE-Schemas & Artifacts):**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `EVIDENCE_PATH_PROOFS_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

* `ENV_LC_ALL_C_OK`

PF09 remains a **consumer** of these tokens and artifact definitions; token semantics and mirror schema live in HDE-Governance and HDE-Schemas & Artifacts.

---

# Phase I — Calcination (Foundations first) 

* **Phase description:** Foundational mechanics for the HD Engine: freeze and validate core catalogs, stand up canonical serialization and total-order infrastructure, and wire repository/tooling skeleton plus the programmatic configuration system.

* **Phase master status:** **Mixed** (one task Done; remaining tasks Not done / In progress).

* **Notes:**

  * PF09 is consumer-only; math, schemas, governance tokens, and HTTP contracts live in PF01/PF12/PF04/PF05/PF14.

  * This phase focuses on determinism primitives (catalogs, serialization, comparators) and repository evidence infrastructure that later phases build on.

---

## Task HDE-CALC001 — Canonical Enumerations Registry

* **Task name/label:** Canonical Enumerations Registry

* **Task status:** **Done**

* **Task ID:** HDE-CALC001

* **Task description:**  
   Freeze and validate the enumerations registry (centers, gates, channels, categories) against PF12 catalogs and schemas, enforce canonical forms and set semantics, prove closure/uniqueness, and emit registry evidence artifacts indexed in the Evidence Index/Mirror system.

* **Task notes:**

  * Enumerations are frozen in canon (HDE-Math-Spec; HDE-Schemas & Artifacts; titles-only).

  * The Registry structure and generation scripts are in place; this component is considered complete for Calcination.

### Subtask HDE-CALC001.1 — Registry validation job

* **Subtask name/label:** Registry validation job

* **Subtask description:**  
   Provide a single registry job that loads centers, gates, channels, and categories from PF12 catalogs and validates each domain against its JSON Schema, hard-failing on unknown IDs, duplicates, non-canonical channel forms, or schema mismatches.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (validation behavior; semantic tokens live in Governance/Schemas)

* **Evidence / artifacts:**

  * Covered by registry evidence families listed below (domain\_snapshot, closure\_report, registry\_checksums).

* **Notes:**  
   PF09 does not restate schemas; it requires the job to exist and enforce failure on invalid domain entries.

### Subtask HDE-CALC001.2 — Channel normalization & set semantics

* **Subtask name/label:** Channel normalization & set semantics

* **Subtask description:**  
   Normalize channels to canonical `NN–NN` (zero-padded, min-first) form and enforce ASCII sort \+ dedupe for any arrays that represent sets before hashing/compare.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (relates to canonicalization/ordering tokens tracked elsewhere)

* **Evidence / artifacts:**

  * Reflected in `closure_report` and ordering evidence families.

* **Notes:**  
   PF09 does not restate invariants; it requires that normalization and set semantics be enforced by this job.

### Subtask HDE-CALC001.3 — Closure & uniqueness

* **Subtask name/label:** Domain closure & uniqueness

* **Subtask description:**  
   Registry validation must prove closure and uniqueness across all domains (no extras or omissions, no duplicate IDs, no cross-catalog drift). Any drift must fail CI.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (closure-related tokens tracked in Governance)

* **Evidence / artifacts:**

  * `closure_report` — proofs of domain closure & uniqueness; channel-normalization rejects.

* **Notes:**  
   CI is expected to fail closed on any mismatch in domain closure or uniqueness.

### Subtask HDE-CALC001.4 — Registry evidence artifacts

* **Subtask name/label:** Registry evidence artifacts

* **Subtask description:**  
   Emit a records-only registry snapshot and supporting reports (closure and checksums) that capture domain counts and canonical sha256/size\_bytes for governed artifacts, and ensure they are indexed under the Evidence Index discipline (Human Index \+ Machine Mirror in the same PR, with path-proofs).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_INDEX_HASH_OK` (implied by Index updates)

* **Evidence / artifacts:**

  * `engine.config.registry_loader` — typed loader implementation for PF12 catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations).

  * `tests/config/` loader tests (titles-only), including unknown-ID and duplicate-ID cases and alias-policy OFF/ON enforcement.

* **Notes:**  
   PF09 does not restate loader schemas or typed error classes; those remain single-homed in PF12 and PF14. This subtask requires that the canonical loader and its tests exist and enforce the fail-closed behavior described above.  
*  Artifact paths and schemas live in HDE-Schemas & Artifacts; PF09 requires their presence and correct indexing.

### Subtask HDE-CALC001.5 — Determinism pins

* **Subtask name/label:** Determinism pins for registry job

* **Subtask description:**  
   Run registry validation and snapshot generation under determinism pins using canonical JSON: `LC_ALL=C`, `LANG=C`, `TZ=UTC`; UTF-8 (no BOM); sorted keys; compact; exactly one trailing LF.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK` (shared canonical JSON check family)

* **Evidence / artifacts:**

  * Canonical JSON checks on registry artifacts (via shared canonical JSON evidence).

* **Notes:**  
   Ensures registry artifacts are stable and canonical across runs.

### Subtask HDE-CALC001.6 — Indexing & mirror discipline (registry)

* **Subtask name/label:** Registry Indexing & mirror discipline

* **Subtask description:**  
   Index registry evidence in `docs/evidence/INDEX.json` and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; each record includes a `proof_anchor` to a co-located path-proof).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  * `*.path_proof.txt` for registry artifacts

* **Notes:**  
   PF09 defers mirror schema details to PF12; this subtask enforces usage, not schema definition.

---

## Task HDE-CALC002 — Canonical Serialization Package

* **Task name/label:** Canonical Serialization Package

* **Task status:** **Partial**

* **Task ID:** HDE-CALC002

* **Task description:**  
   Provide a single canonical serializer/emitter for all public JSON bytes (Reader, CLI, evidence), enforce canonical JSON rules and arrays-as-sets semantics, and prove determinism (AB↔BA, two-run identity) with harness evidence; keep CLI/Reader parity under closed rails.

* **Task notes:**

  * Audit (v1 — 2025-11-17) identified missing tokens and gaps across multiple surfaces; EPIC017 PR01 (D1) centralized the canonical JSON serializer (`engine/stable/sercanon.py` \+ `engine/serializer/canon.sercanon`), routed Reader v1 and `hdctl showcompat` through the shared emitter path, and added the first AB↔BA/two-run/Reader↔CLI/parity and preimage-recompute harness for CLI compat under closed rails.

  * D1 evidence includes CLI showcompat harness artifacts (`artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`, `artifacts/cli/reader_dump.json`, `artifacts/cli/reader_cli_parity.bytes`, `artifacts/cli/preimage_recompute.log`) and serializer guard logs (`artifacts/cli/guards/serializer_grep_guard.log`, `artifacts/cli/guards/emitter_symbol_proof.txt`), indexed under the Evidence Index/Mirror discipline.

  * Task remains **Partial** until later slices (D2–D4) extend canonical serialization and determinism coverage to all required surfaces and tokens.

  

### Subtask HDE-CALC002.1 — Shared presenter/emitter

* **Subtask name/label:** Single presenter/emitter for Reader & CLI

* **Subtask description:**  
   Ensure a single presenter/emitter entrypoint symbol is shared between Reader and CLI for public JSON emission.

* **Subtask status:** **In progress** (harness and guards exist but not fully proven)

* **Epic or card:** EPIC-017 (D1)

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_NO_ALT_JSON_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

  * `artifacts/cli/guards/serializer_grep_guard.log`

* **Notes:**  
   Single-emitter rule is in place but parity gaps remain in other phases; full token set not yet green.

### Subtask HDE-CALC002.2 — Canonical JSON rules

* **Subtask name/label:** Canonical JSON rules for public bytes

* **Subtask description:**  
   Enforce canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted.

* **Subtask status:** **In progress**

* **Epic or card:** EPIC-017 (D1)

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `ERROR_JSON_CANON_OK` (shared canonical JSON family)

* **Evidence / artifacts:**

  * `tests/test_emitter_determinism.py`

  * `audit/gates/canonical_json/json_canonical_check.log`

  * `audit/gates/canonical_json/json_canon_compare.log`

* **Notes:**  
   Harness and checks exist, but canonicalization must be proven across all surfaces before tokens are considered green.

### Subtask HDE-CALC002.3 — Arrays-as-sets semantics

* **Subtask name/label:** Arrays-as-sets discipline

* **Subtask description:**  
   Deduplicate and ASCII-sort arrays that function as sets before hashing or comparison.

* **Subtask status:** **In progress**

* **Epic or card:** EPIC-017 (D1)

* **Tokens:** **Unknown** (implicit in canonicalization and tie-break module tokens)

* **Evidence / artifacts:**

  * Shared canonical JSON compare logs (as above).

* **Notes:**  
   Behavior is tied to comparator and canonicalization work in other tasks.

### Subtask HDE-CALC002.4 — Determinism environment pins

* **Subtask name/label:** Determinism pins for serialization

* **Subtask description:**  
   Run all dumps/compares under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* **Subtask status:** **In progress**

* **Epic or card:** EPIC-017 (D1)

* **Tokens:**

  * `ENV_LC_ALL_C_OK`

* **Evidence / artifacts:**

  * Harness and CI configuration for determinism pins (PF10 Addenda; logs referenced above).

* **Notes:**  
   Applies to both CLI/Reader canonicalization and evidence capture.

### **Subtask HDE-CALC002.5 — Determinism & parity harness**

* Subtask name/label: Determinism and parity harness

* Subtask description:  
   Prove AB↔BA parity, two-run identity, Reader↔CLI parity, and preimage recompute for the canonical serializer and hdctl showcompat.

* Subtask status: Done

* Epic or card: EPIC-017 (D1)

* Tokens:

  * TWO\_RUN\_IDENTITY\_OK

  * COMPOSITE\_ABBA\_IDENTITY\_OK

  * CLI\_READER\_EMITTER\_PARITY\_OK

  * CLI\_AB\_BA\_PARITY\_OK

  * PREIMAGE\_RECOMPUTE\_OK

  * JSON\_CANONICAL\_CHECK\_OK

* Evidence / artifacts:

  * Harness script (titles-only):

    * scripts/cli/canonical\_harness.py — drives AB↔BA, two-run, Reader↔CLI parity, and preimage recompute for hdctl showcompat under rails-closed env.

  * CLI tests (titles-only):

    * tests/cli/test\_showcompat\_parity\_and\_identity.py — AB↔BA parity, two-run identity, Reader↔CLI parity, and preimage recompute checks.

    * tests/cli/test\_cli\_canonical\_bytes.py — canonical JSON shape, LF termination, and non-empty stdout for showcompat.

    * tests/cli/test\_showcompat\_sources.py — source semantics for \--source vendor and \--source db, including compat meta fields (engine\_tag, release\_id, invocation\_tag).

  * CLI determinism and parity artifacts:

    * artifacts/cli/ab.json — canonical compat/admin JSON output for (A,B) under showcompat.

    * artifacts/cli/ba.json — canonical compat/admin JSON output for (B,A); must be byte-identical to ab.json.

    * artifacts/cli/summary.json — canonical JSON summary containing SHA-256 digests for AB/BA runs and ab\_ba\_equal: true, plus two-run identity checks.

    * artifacts/cli/reader\_dump.json — Reader v1 envelope body captured via CLI \--dump-reader for parity checks.

    * artifacts/cli/reader\_cli\_parity.bytes — byte-equality sample for Reader↔CLI parity on the same inputs.

    * artifacts/cli/preimage\_recompute.log — preimage recompute log for Reader envelopes (computed\_sha256, stored\_sha256, match:true).

  * Serializer guard artifacts (shared with HDE-CALC002.6):

    * artifacts/cli/guards/serializer\_grep\_guard.log — grep guard confirming no ad-hoc JSON serializers on governed paths.

    * artifacts/cli/guards/emitter\_symbol\_proof.txt — emitter symbol proof documenting emit\_public and Reader emitter call sites.

  * EPIC017 QA05 Reader envelope evidence (CLI QA environment):

    * Audit/QA/HDE-EPIC017/logs/step\_showcompat\_dump\_reader1.txt (path name indicative; exact path governed by QA harness) — Reader v1 envelope produced by hdctl showcompat \--source vendor \--dump-reader for a synthetic birth pair, showing:

      * Exactly the six canonical keys (reader\_version, eligible, categories, meta, release\_id, idempotence\_hash).

      * categories containing a single harmony entry with a band drawn from Cool, Open, Warm, or Glow and no numerics.

      * meta.engine\_tag \= hdengine-dev, meta.invocation\_tag \= INV-LOCAL, release\_id as an all-zero 64-hex string, and idempotence\_hash as a 64-hex lowercase string.

* Notes:

  * The harness and CI artifacts above are run under closed rails with determinism pins (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) and are indexed under the Evidence Index and Mirror discipline (see sections 0.3 and 0.5).

  * EPIC017 D1 closes the canonical serialization slice for hdctl showcompat: stdout compat output is canonical JSON and non-empty, AB↔BA parity and two-run identity are proven, Reader↔CLI parity is established via \--dump-reader, and preimage recompute for Reader envelopes is verified.

  * EPIC017 QA05 adds a QA-layer confirmation that hdctl showcompat \--source vendor \--dump-reader in the Codespaces CLI environment produces a Reader v1 envelope that matches the six-key, numeric-free covenant (harmony-only categories, eligible flag, meta, release\_id, idempotence\_hash). The meta.engine\_tag, meta.invocation\_tag, and release\_id values in this envelope reflect the CLI/local identity (hdengine-dev, INV-LOCAL, zero release) and must not be treated as the Railway production engine identity; the canonical production identity remains the /internal/version ops surface on Railway.

  * This subtask remains scoped to the serializer and parity harness; API-level Reader A7 transport proofs and Catalog routing are handled in Conjunction and Distillation tasks.

### **Subtask HDE-CALC002.6 — Canonical guard artifacts for CLI serializer/emitter**

* **Subtask name/label:** Canonical guard artifacts for CLI serializer/emitter

* **Subtask description:**  
   Treat the CLI serializer/emitter guard logs under `artifacts/cli/guards/**` as the canonical guard artifacts for CLI serializer coupling. In particular:

  * `artifacts/cli/guards/serializer_grep_guard.log` — grep-guard proving there are no ad-hoc serializers on public paths.

  * `artifacts/cli/guards/emitter_symbol_proof.txt` — import-graph/symbol proof that only the shared presenter/emitter symbol is used for public bytes.

* Ensure that Evidence Index and Machine Mirror records for CLI serializer coupling use these paths as their `discovered_physical_path` values, with co-located `path_proof` files and canonical JSONL mirror records. Implementations MAY also write copies of these logs under `audit/gates/guards/**` for internal audit workflows, but those locations are **secondary** and not required for mechanics-level acceptance.

* **Subtask status:** **In progress**

* **Epic or card:** **EPIC-017 (D1)**

* **Tokens:**

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

* **Notes:**  
   This subtask aligns CLI serializer/emitter guard evidence with the Documentation Artifacts and Registry canon: guard logs live at `artifacts/cli/guards/**` and are indexed and mirrored under the global Evidence Index discipline. PF09 remains consumer-only for record schemas and token semantics; those live in HDE-Governance and HDE-Schemas & Artifacts.

---

## Task HDE-CALC003 — Repository & Tooling Skeleton

**Task name/label:** Repository & Tooling Skeleton

**Task status:** **Partial**

**Task ID:** HDE-CALC003

**Task description:**  
 Provide a deterministic repository/tooling skeleton with an ordered sanity pipeline, Human Evidence Index and Machine Mirror, strict mirror discipline, locale pins, per-run registry report, topology orientation demo, and CI gates that enforce evidence presence and parity.

**Task notes:**

* Audit (v1 — 2025-11-17) originally flagged missing mirror/index and canonicalization tokens. EPIC017 PR02 (D2) implemented the **evidence skeleton**: `tools/evidence/update_evidence_index.py` now owns `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` is the single Machine Mirror, `.path_proof.txt` files are generated consistently, and the **topology orientation demo** (`audit/gates/topology/orientation_demo.txt`) is wired into CI.

* Evidence skeleton CI now runs under rails-closed env (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and includes:

  * `python tools/evidence/update_evidence_index.py --check`

  * `python tools/evidence/orientation_demo.py --check`

  * `ci/checks/check_mirror_schema.sh`

  * `python -m pytest tests/evidence tests/ops/test_evidence_index.py`

* ensuring INDEX/sentinel/mirror/path-proofs/orientation demo are canonical and drift-free.

* Task remains **Partial** until the ordered sanity pipeline (`scripts/make_sanity.sh` or equivalent), per-run registry\_report integration, and global locale pins for all lint/test/artifact jobs are fully implemented and evidenced.

  

### Subtask HDE-CALC003.1 — Sanity pipeline (ordered)

* **Subtask name/label:** Sanity pipeline (ordered)

* **Subtask description:**  
   Provide a single local sanity target (e.g. `scripts/make_sanity.sh`) that, when run, executes in order:  
   formatting → lint/type checks → unit and property tests → JSON-Schema validation for governed inputs → goldens/evidence capture → Index & Machine Mirror parity checks with path-proof validation.

* **Subtask status:** **Unknown**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

* **Evidence / artifacts:**

  * Sanity pipeline transcripts/logs (not explicitly named here; referenced via gate scripts).

* **Notes:**  
   PF09 does not pin script name or tools; it requires this ordered pipeline to exist and be runnable.

### Subtask HDE-CALC003.2 — Human Evidence Index

* **Subtask name/label:** Human Evidence Index (titles/paths only)

* **Subtask description:**  
   Maintain `docs/evidence/INDEX.json` as the single home for evidence titles/paths; update in the same PR as governed artifacts, without duplicating its entries in PF09.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D2)**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_HASH_OK`

* **Evidence / artifacts:**

  * `tools/evidence/update_evidence_index.py` — canonicalizes and writes `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`.

  * `docs/evidence/INDEX.json` — canonical list of `{artifact_key, discovered_physical_path}` objects.

  * `docs/evidence/INDEX.sha256` — sha256 over canonical `INDEX.json` bytes.

  * `tests/evidence/test_evidence_skeleton.py` — validates that on-disk INDEX matches canonical render and sentinel hash.

  * `tests/ops/test_evidence_index.py` — ops-level checks for Index/hash behavior.

* **Notes:**  
   PF09 does not restate Index entries or schemas; those remain single-homed in PF12. This subtask records that the Human Index and sentinel now exist, are canonical, and are enforced by CI under rails-closed env.

### Subtask HDE-CALC003.3 — Evidence Index hash sentinel

**Subtask name/label:** Human Evidence Index hash sentinel

**Subtask description:**  
 Maintain `docs/evidence/INDEX.sha256` as sha256 over the exact bytes of `INDEX.json`; update in the same PR as the Human Index and gate on `EVIDENCE_INDEX_HASH_OK`.

**Subtask status:** **Complete**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

* `EVIDENCE_INDEX_HASH_OK`

  **Evidence / artifacts:**

* `tools/evidence/update_evidence_index.py` — computes and writes `docs/evidence/INDEX.sha256`.

* `docs/evidence/INDEX.sha256` — single-line sentinel `<sha> docs/evidence/INDEX.json`.

* `tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` — ensure sentinel matches canonical `INDEX.json`.

  **Notes:**  
   CI will now fail on any mismatch between `INDEX.json` and `INDEX.sha256`, closing the loop PF09/PF12 describe for drift detection.

### Subtask HDE-CALC003.4 — Machine Evidence Index (JSONL)

**Subtask name/label:** Machine Evidence Index — JSONL (records-only)

**Subtask description:**  
 Provide `artifacts/evidence_index.jsonl` as a records-only Machine Mirror with one JSON object per line; canonical JSONL (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one LF); unknown keys rejected; maintain 1:1 parity with the Human Index; provide path-proofs.

**Subtask status:** **Complete**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

  **Evidence / artifacts:**

* `artifacts/evidence_index.jsonl` — the single Machine Mirror file.

* `tools/evidence/update_evidence_index.py` — renders mirror records from the canonical Human Index.

* `ci/checks/check_mirror_schema.sh` — enforces field set/order, canonical JSONL, and self-record behavior.

* `tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` — validate mirror consistency, path-proof wiring, and self-record handling.

  **Notes:**  
   Mirror schema and record-type semantics remain in PF12 Appendix C; PF09 enforces usage, parity, and CI behavior for the hardened Machine Mirror.

### Subtask HDE-CALC003.5 — Mirror discipline

**Subtask name/label:** Mirror discipline (field order & uniqueness)

**Subtask description:**  
 Enforce ASCII field order `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`; sort-before-write by `(artifact_key, discovered_physical_path)`; ensure uniqueness of that pair; keep `artifacts/evidence_index.jsonl` as the single Machine Mirror file.

**Subtask status:** **Complete**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

  **Evidence / artifacts:**  
* `artifacts/evidence_index.jsonl` — hardened Machine Mirror.

* `ci/checks/check_mirror_schema.sh` — asserts field set/order, uniqueness, and canonical JSONL.

  **Notes:**  
   PF12 remains the single home for mirror schema; PF09 now reflects that mirror discipline is enforced and CI-gated via the EPIC017 D2 work.

### Subtask HDE-CALC003.6 — Registry report (per-run)

* **Subtask name/label:** Registry report generation (names-only)

* **Subtask description:**  
   Produce `artifacts/registry/registry_report.json` (canonical JSON) on every run.

* **Subtask status:** **Unknown**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK` (when indexed)

* **Evidence / artifacts:**

  * `artifacts/registry/registry_report.json`

* **Notes:**  
   High-level behavioral requirement; detailed schema is governed by PF12.

### Subtask HDE-CALC003.7 — Locale pins (repo-wide)

* **Subtask name/label:** Locale pins for all byte checks

* **Subtask description:**  
   Export `LC_ALL=C`, `LANG=C`, `TZ=UTC` in all lint/test/artifact jobs to ensure determinism across builds.

* **Subtask status:** **Partial**

* **Epic or card:** **EPIC-017 (D2)**

* **Tokens:**

  * `ENV_LC_ALL_C_OK`

* **Evidence / artifacts:**

  * CI workflow environment for evidence skeleton jobs (titles-only):

    * `.github/workflows/ci.yml` — sets `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` for evidence runs.

  * CI logs for:

    * `python tools/evidence/update_evidence_index.py --check`

    * `python tools/evidence/orientation_demo.py --check`

    * `python -m pytest tests/evidence tests/ops/test_evidence_index.py`

* **Notes:**  
   Locale pins are now enforced for evidence skeleton and mirror checks under EPIC017 D2. Additional work is needed to extend these pins to **all** lint/test/artifact jobs before this subtask can be considered fully complete.

### Subtask HDE-CALC003.8 — Topology orientation demo

**Subtask name/label:** Topology orientation demo

**Subtask description:**  
 Add `audit/gates/topology/orientation_demo.txt` showing high→low normalized to min→max `NN–NN` (before/after) as a topology orientation demo.

**Subtask status:** **Complete**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* (Topology-orientation token name, if any, remains single-homed in Governance.)  
  **Evidence / artifacts:**  
* `tools/evidence/orientation_demo.py` — generates and checks `orientation_demo.txt`.

* `audit/gates/topology/orientation_demo.txt` — deterministic report with header, `total_artifacts`, `status: ok|mismatch`, and sample/issue lines.

* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — path-proof transcript.

* `tests/evidence/test_orientation_demo.py` — validates orientation demo behavior and mismatch detection.  
  **Notes:**  
   CI runs `python tools/evidence/orientation_demo.py --check` under pinned env; this subtask now represents a governed, drift-checked topology orientation demo as part of the evidence skeleton.

### Subtask HDE-CALC003.9 — Wire local run targets

* **Subtask name/label:** Wire local run targets for sanity pipeline

* **Subtask description:**  
   Keep `scripts/make_sanity.sh` current and wired to the ordered sanity pipeline.

* **Subtask status:** **Unknown** (script may exist; audit only calls for keeping it current)

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * `scripts/make_sanity.sh`

* **Notes:**  
   CLI entrypoint for local developer sanity runs.

### Subtask HDE-CALC003.10 — Indexing & parity gates

**Subtask name/label:** Indexing & parity CI gates

**Subtask description:**  
 Update Human Index and Machine Mirror in the same PR (records-only; with path-proofs); ensure governed locations only (`artifacts/**`, `audit/**`, `docs/evidence/**`); reject ungoverned `codex/out/**`; CI fails if Index/Mirror miss entries, violate canonical JSONL, have unknown keys, missing path-proofs, wrong field order, or are unsorted.

**Subtask status:** **Partial**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `EVIDENCE_PATH_PROOFS_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

  **Evidence / artifacts:**

* CI evidence skeleton jobs and checks (titles-only):

  * `python tools/evidence/update_evidence_index.py --check`

  * `python tools/evidence/orientation_demo.py --check`

  * `ci/checks/check_mirror_schema.sh`

  * `python -m pytest tests/evidence tests/ops/test_evidence_index.py`

* Hardened artifacts:

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  * `*.path_proof.txt` for governed artifacts (including topology.orientation\_demo).

  **Notes:**  
     EPIC017 PR02 wires Index/Mirror/Orientation gating into CI and closes a large part of this subtask. Additional CI integration (e.g., full sanity pipeline covering pack identity, A7 proofs, DB posture, BodyGraph gates) remains to be implemented in later Distillation tasks.

---

## Task HDE-CALC004 — Programmatic Configuration System

* **Task name/label:** Programmatic Configuration System

* **Task status:** **Partial**

* **Task ID:** HDE-CALC004

* **Task description:**  
   Provide a typed, deterministic configuration system that loads governed catalogs, validates/normalizes them, enforces alias policy, emits a registry report, and exposes typed FE/BE bundles, with evidence integrated into the Index/Mirror system.

* **Task notes:**

  * Audit (v1 — 2025-11-17) originally flagged missing unknown-ID failure capture and registry report artifacts, with indices not updated. EPIC017 PR03 (D3) implemented the PF12-aligned registry loader (`engine.config.registry_loader`), enforced explicit alias policy OFF/ON with allow-list ledgers, added the canonical `registry_report.v1` generator (`tools/generate_registry_report.py`), and wired `artifacts/registry/registry_report.json` into the Evidence Index/Mirror with a governed path-proof under rails-closed CI.

  * D3 evidence includes loader tests under `tests/config/` (unknown IDs, duplicates, alias policy), registry\_report determinism tests (`registry_report.v1` shape, canonical LF-terminated JSON, two-run identity), and Index/Mirror coherence tests for `registry_report` and its path-proof.

  * Task remains **Partial** until typed FE/BE bundles (004.5/004.6) and any additional configuration artifacts are implemented and indexed; this row currently reflects only the loader \+ registry\_report slice (EPIC017 D3).

  ### Subtask HDE-CALC004.1 — Unknown-ID hard-fail

* **Subtask name/label:** Unknown-ID hard-fail

* **Subtask description:**  
   Loader must hard-fail (typed error) on any unknown identifier.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D3)**

* **Tokens:**

  * `UNKNOWN_IDS_FAIL_CLOSED_OK`

  * `CONFIG_GEN_OK`

* **Evidence / artifacts:**

  * `engine.config.registry_loader` — typed loader implementation for PF12 catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations).

  * `tests/config/` loader tests (titles-only), including unknown-ID and duplicate-ID cases and alias-policy OFF/ON enforcement.

* **Notes:**  
   PF09 does not restate loader schemas or typed error classes; those remain single-homed in PF12 and PF14. This subtask records that the canonical loader and its tests exist and enforce the fail-closed behavior described above.

  ### **Subtask HDE-CALC004.2 — Input-alias policy configuration**

* **Subtask name/label:** Input-alias policy configuration

* **Subtask description:**  
   Default alias policy **OFF**; if ON, normalize via declared alias ledgers; outputs remain canonical; reject unknown aliases and undeclared entries.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D3)**

* **Tokens:**

  * `UNKNOWN_IDS_FAIL_CLOSED_OK`

* **Evidence / artifacts:**

  * `tests/config/test_alias_policy_enforcement.py` (titles-only) — verifies alias policy OFF by default, OFF+empty ledger still fails, and allow-list policy with a non-empty ledger produces the expected `alias_map`.

* **Notes:**  
   Alias-policy token semantics are single-homed in Governance/Schemas; PF09 records that the loader tests enforce the OFF/allow-list/fail-closed behavior.

### Subtask HDE-CALC004.3 — Registry report emission

* **Subtask name/label:** Emit registry report each run

* **Subtask description:**  
   Emit a names-only, canonical JSON registry report each run at `artifacts/registry/registry_report.json`.

* **Subtask status:** **Complete**

* **Epic or card:**EPIC-017 (D3)  
* **Tokens:**  
* `CONFIG_GEN_OK`

* `JSON_CANONICAL_CHECK_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`  
* **Evidence / artifacts:**

  * `tools/generate_registry_report.py` — programmatic generator for `registry_report.v1`, driven by the canonical loader in HDE-CALC004.1.

  * `artifacts/registry/registry_report.json` — LF-terminated, canonical JSON registry report (schema and field shapes governed by PF12).

  * `artifacts/registry/registry_report.json.path_proof.txt` — path-proof transcript for the registry report artifact (path, sha256, size\_bytes, produced\_at\_utc).

* **Notes:**  
  Registry report generation is now implemented via `tools/generate_registry_report.py` and participates in canonical JSON and Index/Mirror discipline as required for D3.

### Subtask HDE-CALC004.4 — Registry report alias policy summary

* **Subtask name/label:** Registry report alias policy summary

* **Subtask description:**  
   Ensure the registry report includes a names-only alias policy summary that reflects loader behavior: `mode` is `off` or `allow_list` (closed set), and `aliases` is a mapping from alias IDs to canonical channel IDs when allow-list is enabled.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D3)**

* **Tokens:**

  * `CONFIG_GEN_OK`

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * Registry report fields; schema lives in PF12.

* **Notes:**  
   D3 registry\_report tests verify that `alias_policy.mode` and `alias_policy.aliases` reflect the loader’s alias allow-list mode and ledger contents. PF09 stays schema-agnostic and records that this summary exists and is governed.

### Subtask HDE-CALC004.5 — Typed FE bundle

* **Subtask name/label:** Typed FE bundle

* **Subtask description:**  
   Generate a front-end typed constants bundle exposing closed enums/domains and read-only constants needed by the FE client (e.g. category IDs and band labels); bundle exists, is typed/immutable, and is consistent with PF12 catalogs.

* **Subtask status:** **Unknown**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * FE bundle artifacts (not enumerated here).

### Subtask HDE-CALC004.6 — Typed BE bundle

* **Subtask name/label:** Typed BE bundle

* **Subtask description:**  
   Generate a backend enums & constants bundle exposing the same frozen domains to backend code (enums, discriminated unions); bundle exists, is typed/immutable, and stays in sync with the FE bundle and underlying catalogs.

* **Subtask status:** **Unknown**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * BE bundle artifacts (not enumerated here).

  ### **Subtask HDE-CALC004.7 — Indexing & parity for config artifacts**

* **Subtask name/label:** Indexing & parity (Programmatic Configuration System)

* **Subtask description:**  
   Update Human Index and Machine Mirror in the same PR (records-only; with path-proofs) for registry report and configuration-related artifacts; do not list entries in PF09; see PF12 §8.6 for Index/Mirror schema.

* **Subtask status:** **Partial**

* **Epic or card:** **EPIC-017 (D3)**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * Index/Mirror entries for `artifacts/registry/registry_report.json` (artifact\_key `registry.registry_report` in `docs/evidence/INDEX.json` and corresponding record in `artifacts/evidence_index.jsonl` with a `proof_anchor` to `artifacts/registry/registry_report.json.path_proof.txt`).

  * `tests/config/` registry\_report tests (titles-only) that verify canonical shape, `schema:"registry_report.v1"`, two-run identity, and Index/Mirror coherence for `registry_report` (including SHA/size matching Index and mirror).

* **Notes:**  
   D3 closes the indexing and parity story for the **registry\_report** artifact. Additional config artifacts (e.g., FE/BE bundles) will extend this subtask beyond D3; hence status remains **Partial** until all configuration-related artifacts are governed and indexed under the same discipline.

---

## **Task HDE-CALC005 — Deterministic Tie-Break & Total-Order Module**

* **Task name/label:** Deterministic Tie-Break & Total-Order Module

* **Task status:** **Done**

* **Task ID:** HDE-CALC005

* **Task description:**  
   Provide ASCII-based comparators and helpers that impose deterministic, locale-free total order over IDs, centers, channels, and categories, and prove comparator properties with property tests and ABBA/two-run identity checks; ensure canonicalization respects arrays-as-sets semantics and is backed by ordering evidence families.

* **Task notes:**

  * **Status lock (HDE-EPIC006 — Mechanics Foundations):** PF09 Phase-I “Deterministic tie-break & total-order module — Implement” is satisfied under **HDE-EPIC006**, which closed tie-break/total-order, comparators, invariance, and `/internal/version` HEAD/conditionals remediation for this module. This row is now history-only; any new comparator or ordering work is tracked in downstream epics and global-discipline tasks.

  * Audit (v1 — 2025-11-17) originally flagged missing `JSON_CANONICAL_CHECK_OK` / `TWO_RUN_IDENTITY_OK` tokens and the absence of comparator proofs and sorted ordering snapshots.

  * EPIC017 PR04 (WS-D4) introduced the **ordering layer** and hardened much of the **evidence plumbing** for this module:

    * A dedicated `engine/order` package now provides comparators and helpers for IDs, channels, categories, and arrays-as-sets.

    * `tools/order/generate_ordering_artifacts.py` is the **single writer** for ordering artifacts under `artifacts/engine/order/**`, generating:

      * `channels_sorted.snapshot.json`

      * `categories_iter.snapshot.json`

      * `props_total_order.log`

      * `abba_identity.bytes`

    * Ordering artifacts support a `--check` mode for two-run identity, and new tests (`tests/order/test_total_order_properties.py`, `tests/order/test_ordering_artifacts_stability.py`) cover total-order properties and artifact stability / ABBA parity.

    * `tools/evidence/update_evidence_index.py` is the **sole writer** for `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and governed `*.path_proof.txt`, and `ci/checks/check_mirror_schema.sh` enforces mirror schema and self-record rules as part of the evidence skeleton.

  * WS-D4b (EPIC017 PR04r) completed the **evidence remediation** for this task:

    * Finalized `mtime_utc` semantics for governed path-proofs as **refresh-time mtime** (UTC ISO-8601, truncated to seconds, microsecond==0, monotone `<= stat().st_mtime` at check time), aligned with PF12/PF19.

    * Regenerated all governed `*.path_proof.txt` to the `{path, size_bytes, sha256, mtime_utc, produced_at_utc}` schema and refreshed `artifacts/evidence_index.jsonl` so the Machine Mirror self-record and its proof match the body hash and file size.

    * Regenerated `artifacts/engine/order/abba_identity.bytes` via `tools/order/generate_ordering_artifacts.py` so its on-disk bytes, Mirror record, and path-proof all agree on a 32-byte artifact and canonical SHA, resolving the earlier ABBA mismatch.

    * Updated `tools/evidence/update_evidence_index.py`, `ci/checks/check_mirror_schema.sh`, and the evidence tests (`tests/evidence/test_evidence_skeleton.py`, `tests/ops/test_evidence_index.py`) to enforce the same `mtime_utc` semantics (format \+ monotone vs `stat()`), so mirror schema and evidence skeleton checks now pass under rails-closed CI.

  * As a result, WS-D4 tokens that depend on ordering math and generator ownership **and** on the hardened evidence skeleton (for example `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`, `ORDERING_ARTIFACTS_DETERMINISTIC_OK`, `EVIDENCE_PATH_PROOFS_OK`, `EVIDENCE_PATH_PROOFS_SHAPE_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`) are now **green** under the standard rails-closed CI pipeline. All subtasks HDE-CALC005.1–HDE-CALC005.6 are treated as complete for this Phase-I module; remaining ordering usage is enforced by higher-level “global discipline” tasks.

---

### **Subtask HDE-CALC005.1 — ASCII comparators**

* **Subtask name/label:** ASCII domain comparators

* **Subtask description:**  
   Implement ASCII comparators for:

  * IDs and centers (string-based)

  * channels (`NN–NN` min-first, zero-padded)

  * categories (frozen Magic-10 rank → ASCII)

* **Subtask status:** **Complete**

* **Epic or card:** **HDE-EPIC006 (Mechanics Foundations); EPIC-017 (D4)**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * `order/channels_sorted`, `order/categories_iter` evidence families (see below).

---

### **Subtask HDE-CALC005.2 — Helpers for ordering**

* **Subtask name/label:** Ordering helpers

* **Subtask description:**  
   Provide helpers: `dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`, and require their use at all ordered emission sites (composites, categories, evidence).

* **Subtask status:** **Complete**

* **Epic or card:** **HDE-EPIC006 (Mechanics Foundations); EPIC-017 (D4)**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * `order/props_total_order`, `canonical/json_compare` families; canonical JSON compare logs.

---

### **Subtask HDE-CALC005.3 — Property tests & ordering proofs**

* **Subtask name/label:** Comparator property tests & ordering proofs

* **Subtask description:**  
   Add property tests for antisymmetry, transitivity, and totality; prove channel order (min-first `NN–NN`) and category iteration loop equals the frozen order.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D4)**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK` (once ordering effects are verified by byte compare)

* **Evidence / artifacts:**

  * `order/props_total_order`

  * `order/channels_sorted`

  * `order/categories_iter`

* **Notes:**  
   Comparator property tests and ordering snapshots are now driven by the EPIC017 ordering layer, run under the standard rails-closed CI pipeline, and wired into the EPIC017 D4 acceptance map; `JSON_CANONICAL_CHECK_OK` and `TWO_RUN_IDENTITY_OK` are satisfied via these artifacts.

---

### **Subtask HDE-CALC005.4 — Determinism checks**

* **Subtask name/label:** AB↔BA & two-run identity checks

* **Subtask description:**  
   Add AB↔BA and two-run identity checks for outputs produced under these comparators; canonical re-serialization byte-compare under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D1)** *(harness artifacts referenced)*

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

  * `COMPOSITE_ABBA_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json`

  * `artifacts/cli/summary.json`

  * `artifacts/cli/reader_dump.json`

  * `artifacts/cli/reader_cli_parity.bytes`

  * `artifacts/cli/preimage_recompute.log`

---

### **Subtask HDE-CALC005.5 — Canonical JSON & serializer determinism evidence**

* **Subtask name/label:** Serializer determinism & canonical JSON evidence

* **Subtask description:**  
   Provide tests and logs that prove serializer determinism and canonical JSON under these comparator policies.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D1)**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * `tests/test_emitter_determinism.py`

  * `audit/gates/canonical_json/json_canonical_check.log`

  * `audit/gates/canonical_json/json_canon_compare.log`

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

* **Notes:**  
   These artifacts run under rails-closed CI (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and are indexed with path-proofs. They now fully satisfy the `JSON_CANONICAL_CHECK_OK` acceptance token as recorded in the EPIC017 manifest and acceptance map.

---

### **Subtask HDE-CALC005.6 — Ordering & comparator evidence families**

* **Subtask name/label:** Ordering & comparator evidence families

* **Subtask description:**  
   Track ordering evidence families for the tie-break module and ensure they are generated by a single tool, are deterministic under pinned environment settings, and are indexed in the Evidence Index and mirrored 1:1 in the Machine Mirror in the same PR:

  * **Generator-owned ordering artifacts.**

    * `tools/order/generate_ordering_artifacts.py` is the **single writer** for ordering artifacts under `artifacts/engine/order/**`.

    * The governed ordering artifacts are:

      * `artifacts/engine/order/channels_sorted.snapshot.json` — channel ordering snapshot.

      * `artifacts/engine/order/categories_iter.snapshot.json` — Magic-10 category loop order.

      * `artifacts/engine/order/props_total_order.log` — comparator property-test proofs (antisymmetry, transitivity, totality).

      * `artifacts/engine/order/abba_identity.bytes` — AB↔BA byte-equality evidence for comparator outputs.

  * **Deterministic runs.**

    * The ordering generator MUST support a `--check` (or equivalent) mode and be deterministic under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; two successive runs with the same inputs produce byte-identical ordering artifacts (`ORDERING_ARTIFACTS_DETERMINISTIC_OK`).

  * **Index/Mirror & proofs.**

    * On each run, the generator (together with the evidence tools) rewrites the Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`), Machine Mirror (`artifacts/evidence_index.jsonl`), and associated `.path_proof.txt` files so that ordering artifacts, Index, mirror, and proofs move in lockstep.

    * Mirror records for the ordering artifacts follow PF12 mirror schema (fixed field set/order), include `proof_anchor` pointing to each ordering artifact’s path-proof transcript, and are validated (alongside proofs) by `ci/checks/check_mirror_schema.sh`.

* PF09 does not define ordering schemas or comparator math; those remain single-homed in HDE-Math-Spec and HDE-Schemas & Artifacts. This subtask ensures that ordering artifacts and their evidence plumbing are generator-owned, deterministic, and fully integrated into the Evidence Index/Mirror system.

* **Subtask status:** **Complete**

* **Epic or card:** **EPIC-017 (D4, WS-D4b — Evidence mtime re-alignment)**

* **Tokens:**

  * `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`

  * `ORDERING_ARTIFACTS_DETERMINISTIC_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `EVIDENCE_PATH_PROOFS_SHAPE_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

* **Evidence / artifacts (titles-only; PF09 is consumer-only):**

  * **Generator & tools:**

    * `engine/order/__init__.py`, `engine/order/comparators.py`, `engine/order/artifacts.py` (or equivalent ordering modules).

    * `tools/order/generate_ordering_artifacts.py` — generator for ordering artifacts (write \+ `--check` modes).

    * `tools/evidence/update_evidence_index.py` — single writer for Index, sentinel, mirror, and governed path-proofs.

    * `tools/evidence/orientation_demo.py` — topology orientation demo and consistency checks.

    * `ci/checks/check_mirror_schema.sh` — mirror schema & path-proof shape/monotonicity check.

  * **Ordering artifacts (governed, generator-owned):**

    * `artifacts/engine/order/channels_sorted.snapshot.json`

    * `artifacts/engine/order/categories_iter.snapshot.json`

    * `artifacts/engine/order/props_total_order.log`

    * `artifacts/engine/order/abba_identity.bytes`

  * **Index/Mirror/Proofs:**

    * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

    * `artifacts/evidence_index.jsonl`

    * `artifacts/engine/order/channels_sorted.snapshot.json.path_proof.txt`

    * `artifacts/engine/order/categories_iter.snapshot.json.path_proof.txt`

    * `artifacts/engine/order/props_total_order.log.path_proof.txt`

    * `artifacts/engine/order/abba_identity.bytes.path_proof.txt`

  * **Tests:**

    * `tests/order/test_total_order_properties.py` — total-order property tests.

    * `tests/order/test_ordering_artifacts_stability.py` — ordering artifact stability / ABBA parity tests.

    * `tests/evidence/test_evidence_skeleton.py` — evidence skeleton & proof checks (now green for `mtime_utc` format/monotone semantics and path-proof shape).

    * `tests/ops/test_evidence_index.py` — Index/mirror consistency tests (now green for `mtime_utc` semantics).

* **Notes:**

  * WS-D4 established the ordering layer, generator, and initial evidence plumbing. WS-D4b finalized the `mtime_utc` semantics for governed path-proofs (refresh-time, monotone, UTC ISO) and regenerated ABBA and path-proof artifacts so that artifact bytes, Mirror records, and `*.path_proof.txt` contents all agree.

  * Under the standard rails-closed CI pipeline (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), the ordering evidence families and their Index/Mirror wiring now satisfy all of the tokens listed above, including `CI_CHECK_MIRROR_SCHEMA_OK` and `EVIDENCE_PATH_PROOFS_SHAPE_OK`.

  * Further ordering-related work (for example, wiring comparators into all surfaces and the global discipline tasks) is tracked in other subtasks and tasks; this subtask specifically is considered **Complete** for EPIC017 D4/D4b.

  # Phase II — Dissolution (Normalize and make it pure) 

* **Phase description:** Normalize and validate all inputs, enforce canonical ID and preference semantics, and establish deterministic, schema-governed behavior for compat, sampler/ranker, engine core, band thresholds, and category framework.

* **Phase master status:** **Mixed**

* **Notes:**

  * The header previously said “Completed”, but multiple tasks in this phase are explicitly marked **Not done**, so the phase is best treated as **Mixed**.

  * Canon behavior for several components (sampler/ranker, engine core, band thresholds, category framework) is specified in PF14/PF-Math, but PF09 tracks implementation/evidence state here.

  ---

  ## Task HDE-DISS001 — Input Normalization & Validation Layer

* **Task ID:** HDE-DISS001

* **Task name/label:** Input Normalization & Validation Layer

* **Task status:** **Done**

* **Task description:**  
   Normalize IDs and viewer\_prefs, enforce schema-based validation, and guarantee canonical JSON forms and AB↔BA neutrality for normalized inputs, with hard-fail behavior for unknown IDs and invalid shapes.

* **Task notes:**

  * IDs normalize via declared alias ledgers when normalization is enabled; otherwise, unknown IDs are rejected.

  * viewer\_prefs must satisfy:

    * `top_category ∈ Magic-10`, and

    * `weights` contains all ten Magic-10 keys with integer values 0..100 (no floats).

  * Zero-weight rule is enforced downstream by the sampler/ranker (PF14 §11, titles-only).

  * Normalized forms are re-serialized to canonical JSON:

    * UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF.

    * Arrays-as-sets deduped and ASCII-sorted.

    * Normalization is AB↔BA neutral: normalized JSON for (A,B) is byte-identical to (B,A).

* **Task-level tokens (titles-only):**

  * `UNKNOWN_IDS_FAIL_CLOSED_OK`

  * `ALIAS_NORMALIZATION_OK` (when enabled)

  * `PREFS_KEYSET_10_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

  ### Subtask HDE-DISS001.1 — ID normalization & alias policy

* **Subtask name/label:** ID normalization & alias policy

* **Subtask description:**  
   Normalize IDs via declared alias ledgers when normalization is enabled; otherwise, reject unknown IDs with a typed error.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `UNKNOWN_IDS_FAIL_CLOSED_OK`

  * `ALIAS_NORMALIZATION_OK` (when enabled)

* **Evidence / artifacts:**

  * Invalid shapes/IDs: service-side typed error tests (`invalid_prefs`, `invalid_json`)

  * Normalization snapshots and canonical-compare logs

* **Notes:**  
   Behavior is governed by canon (PF14/PF12); PF09 records that the implementation enforces this.

  ### Subtask HDE-DISS001.2 — viewer\_prefs shape & keyset

* **Subtask name/label:** viewer\_prefs validation

* **Subtask description:**  
   Enforce that `viewer_prefs.top_category ∈ Magic-10` and `viewer_prefs.weights` contains exactly all ten Magic-10 keys with integer values 0..100 (no floats).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `PREFS_KEYSET_10_OK`

  * `UNKNOWN_IDS_FAIL_CLOSED_OK` (for bad IDs)

* **Evidence / artifacts:**

  * Service-side typed error tests for `invalid_prefs` and `invalid_json`

* **Notes:**  
   Zero-weight semantics are enforced in the sampler/ranker, not here.

  ### Subtask HDE-DISS001.3 — Zero-weight rule handoff

* **Subtask name/label:** Zero-weight rule handoff to sampler/ranker

* **Subtask description:**  
   Ensure that viewer\_prefs normalization preserves weight=0 semantics and that enforcement of “exclude candidates whose \#1 equals a 0-weight category” is delegated to the sampler/ranker.

* **Subtask status:** **Complete (SoT-level behavior; enforced downstream)**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK` (end-to-end identity relies on consistent handoff)

* **Evidence / artifacts:**

  * Referenced sampler/ranker evidence families (see HDE-DISS003).

* **Notes:**  
   This subtask is mainly a contract boundary: PF09 marks that enforcement happens downstream, not in the normalization layer.

  ### Subtask HDE-DISS001.4 — Canonical JSON normalization & ABBA

* **Subtask name/label:** Canonical JSON & AB↔BA neutrality

* **Subtask description:**  
   Re-serialize normalized inputs to canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays-as-sets are deduped and ASCII-sorted. Normalization must be AB↔BA neutral: (A,B) and (B,A) normalize to byte-identical JSON.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `tests/test_emitter/test_emitter_determinism.py` — success parity (CLI vs service)

  * Normalization snapshots and canonical-compare logs

* **Notes:**  
   Shares canonicalization infrastructure with the Canonical Serialization Package from Phase I.

  ### Subtask HDE-DISS001.5 — Schema validation CI job

* **Subtask name/label:** JSON-Schema validation CI job

* **Subtask description:**  
   Maintain a JSON-Schema validation CI job that is present and passing for all governed input shapes (IDs, prefs, and other catalog-bound payloads); use an allowed JSON-Schema validator (e.g. AJV or equivalent); any schema drift or unknown field must fail the job.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `UNKNOWN_IDS_FAIL_CLOSED_OK` (unknown fields/IDs must fail)

  * `JSON_CANONICAL_CHECK_OK` (canonical lints shared across inputs)

* **Evidence / artifacts:**

  * CI job configuration and logs (tool names/paths not pinned in PF09)

* **Notes:**  
   PF09 does not pin tool names/paths; schemas and validator behavior are single-homed in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

  ### Subtask HDE-DISS001.6 — Evidence coverage (normalization)

* **Subtask name/label:** Normalization & validation evidence coverage

* **Subtask description:**  
   Maintain evidence for normalization and validation behavior, including success parity, invalid shapes/IDs, and canonicalization logs, and index them under the global Evidence Index & mirror discipline.

* **Subtask status:** **Complete** (for the named artifacts)

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts (titles/paths only):**

  * `tests/test_emitter/test_emitter_determinism.py`

  * Service-side typed error tests (`invalid_prefs`, `invalid_json`)

  * Normalization snapshots & canonical-compare logs

* **Notes:**  
   Indexing details follow the generic Evidence Index section; PF09 does not restate mirror schema here.

  ---

  ## Task HDE-DISS002 — Compatibility Engine (pair)

* **Task ID:** HDE-DISS002

* **Task name/label:** Compatibility Engine (pair)

* **Task status:** **Done**

* **Task description:**  
   Compute per-category integer scores and bands, select narrative keys, and emit ten categories in frozen Magic-10 order for a pair (a,b), with AB↔BA parity and canonical JSON behavior, using per-channel semantics and strict input typing.

* **Task notes:**

  * Scope includes:

    * Per-category score (0..100) and band mapping via inclusive-high edges (e.g. 24/49/74/100) using `round_half_up`.

    * Selection of `personal_key` / `shared_key`.

    * Emission of 10 categories in frozen Magic-10 order (HDE-Schemas & Artifacts §2.6; HDE-Math-Spec §5.1).

  * Per-channel semantics:

    * Each channel is a canonical `NN-NN` edge (min-first, zero-padded).

    * Record compromise direction \+ gate.

    * Integration {10, 20, 34, 57} channels are independent and MUST be validated for AB↔BA parity.

  * Inputs:

    * `a`, `b` each: an ID or a full person payload (Reader schema).

    * Must not mix ID vs payload for the same party (mixed shape ⇒ `invalid_json`).

* **Task-level tokens (titles-only):**

  * `JSON_CANONICAL_CHECK_OK`

  * `AB_BA_PARITY_OK` (including Integration cases)

  * `TWO_RUN_IDENTITY_OK`

  ### Subtask HDE-DISS002.1 — Per-category scoring & banding

* **Subtask name/label:** Per-category scoring & band thresholds

* **Subtask description:**  
   Compute per-category integer scores (0..100) and map each to a band using inclusive-high thresholds (e.g. 24/49/74/100) with `round_half_up`, consistent with PF-Math.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * Implied via compat identity hash (`artifacts/compat/identity_hash.txt`) and AB↔BA logs.

  ### Subtask HDE-DISS002.2 — Narrative key selection

* **Subtask name/label:** Narrative key selection (10×2 table)

* **Subtask description:**  
   Select `{personal_key, shared_key}` per category from governed narrative key ledgers, emitting ten categories in frozen Magic-10 order.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * `artifacts/narratives/key_table_10x2.snapshot.json` — 10×2 narrative key table

  ### Subtask HDE-DISS002.3 — Per-channel semantics & Integration ABBA

* **Subtask name/label:** Per-channel semantics & Integration parity

* **Subtask description:**  
   Treat each channel as canonical `NN-NN` (min-first, zero-padded), recording compromise direction \+ gate. Integration channels {10, 20, 34, 57} are independent and must be validated for AB↔BA parity.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `AB_BA_PARITY_OK` (including Integration cases)

* **Evidence / artifacts:**

  * AB↔BA parity logs, including Integration channel pairs (e.g. 20-34 vs 20-57).

  ### Subtask HDE-DISS002.4 — Input typing & error semantics

* **Subtask name/label:** Input typing & `invalid_json` enforcement

* **Subtask description:**  
   For inputs `a` and `b`, ensure each is either an ID or a full person payload (Reader schema); do not mix ID vs payload for the same party; mixed shape must produce `invalid_json`.

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK` (error envelopes follow canonical JSON)

* **Evidence / artifacts:**

  * Service-side typed error tests for `invalid_json` in compat flows.

  ### Subtask HDE-DISS002.5 — Canonical JSON & identity hash

* **Subtask name/label:** Canonical JSON & compat identity hash

* **Subtask description:**  
   Ensure compat output is canonical JSON (UTF-8/no BOM; sorted keys; compact; one LF; arrays-as-sets deduped & ASCII-sorted) and compute an `identity_hash` (sha256 of LF-terminated compat body).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/compat/identity_hash.txt` — sha256 of LF-terminated compat body

  ### Subtask HDE-DISS002.6 — Evidence & indexing (compat)

* **Subtask name/label:** Compatibility Engine evidence & indexing

* **Subtask description:**  
   Maintain compat evidence (narrative key table, compat identity hash, AB↔BA logs) and index them in the Evidence Index and Machine Mirror with path-proofs, per global Evidence Index discipline.

* **Subtask status:** **Complete** (for named artifacts)

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts (titles/paths only):**

  * `artifacts/narratives/key_table_10x2.snapshot.json`

  * `artifacts/compat/identity_hash.txt`

  * AB↔BA parity logs for compat (Integration channels included)

  ---

  ## Task HDE-DISS003 — Swipe Sampler & Ranker

* **Task ID:** HDE-DISS003

* **Task name/label:** Swipe Sampler & Ranker

* **Task status:** **Not done**

* **Task description:**  
   Build a deterministic swipe sampler/ranker that enforces the zero-weight rule, diversity constraints, deterministic scoring and ranking, optional seedability in dev/admin flows, and provides a dev-only sampling endpoint, with canonical JSON outputs and evidence integrated into the Evidence Index/Mirror.

* **Task notes:**

  * Audit (v1 — 2025-11-17): zero-weight enforcement, diversity checks, and sampler/ranker evidence are referenced from canon but not yet wired as a complete engine-level harness.

* **Task-level tokens (titles-only):**

  * Determinism & parity: `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`

  * Canonical JSON: `JSON_CANONICAL_CHECK_OK`

  ### Subtask HDE-DISS003.1 — Zero-weight rule enforcement

* **Subtask name/label:** Zero-weight enforcement in candidate pool

* **Subtask description:**  
   Enforce the zero-weight rule when forming the candidate pool: exclude any candidate whose `#1` category corresponds to a viewer weight of 0\.

* **Subtask status:** **Not done** (referenced in canon, not fully wired)

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK` (end-to-end determinism depends on deterministic exclusion)

* **Evidence / artifacts:**

  * To be covered by “Sampler snapshots” and “Seed replay logs” once implemented.

  ### Subtask HDE-DISS003.2 — Pool formation & eligibility

* **Subtask name/label:** Pool formation & eligibility filters

* **Subtask description:**  
   Apply viewer eligibility filters (titles-only to Mechanics/Math) and assemble the candidate pool before ranking; enforce diversity constraints (window K, bound N, recent R) prior to final ordering.

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * “Diversity checks” artifacts demonstrating window/bound/recent constraints satisfaction.

  ### Subtask HDE-DISS003.3 — Deterministic scoring & ranking

* **Subtask name/label:** Deterministic scoring & total order

* **Subtask description:**  
   Use a deterministic fixed-point score function across the ten categories (integer path); sort candidates by score in the specified direction, then break ties using the ID comparator to guarantee a stable total order.

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `COMPOSITE_ABBA_IDENTITY_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * “Sampler snapshots” — candidate pools and ranked outputs (canonical JSON; one LF).

  ### Subtask HDE-DISS003.4 — Seedability (dev/admin only)

* **Subtask name/label:** Seedable dev/admin sampling

* **Subtask description:**  
   For non-public flows, accept an optional seed input; with the same inputs and seed, sampler outputs must be byte-identical. Seed use must not alter public bytes.

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * “Seed replay logs” showing identical outputs for identical inputs/seed and ABBA/two-run identity for sampler outputs.

  ### Subtask HDE-DISS003.5 — Sampler endpoint harness

* **Subtask name/label:** Dev-only sampler endpoint harness

* **Subtask description:**  
   Wire a dev-only sampling endpoint (for example `POST /api/sample/v1`) that returns candidate IDs only and echoes the seed in `meta` when present; CLI tooling (sample) remains the primary dev harness.

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * Endpoint harness logs and snapshots (canonical JSON; one LF).

  ### Subtask HDE-DISS003.6 — Evidence & indexing (sampler/ranker)

* **Subtask name/label:** Sampler/ranker evidence & indexing

* **Subtask description:**  
   Index sampler/ranker artifacts in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; proof\_anchor to a co-located `path_proof.txt`).

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts (families; titles-only):**

  * Sampler snapshots

  * Diversity checks artifacts

  * Seed replay logs

  ---

  ## Task HDE-DISS004 — Deterministic Engine Core

* **Task ID:** HDE-DISS004

* **Task name/label:** Deterministic Engine Core

* **Task status:** **Not done**

* **Task description:**  
   Maintain a pure-compute core (ops, scoring, aggregation) with no I/O/clocks/globals, AB↔BA neutrality, two-run identity, stable reductions via ASCII sorting, and canonical JSON for any core-emitted evidence, with deterministic behavior proven by dedicated artifacts.

* **Task notes:**

  * Audit (v1 — 2025-11-17):

    * Missing tokens: `TWO_RUN_IDENTITY_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `NO_IO_NO_CLOCKS_OK`.

    * No committed, passing artifacts under the listed paths.

  * Notes (SoT): core is intended to be pure compute, with no I/O, clocks, or env/global state; all reductions stabilize via ASCII sort; any JSON evidence is canonical; all checks run under `LC_ALL=C`.

* **Task-level tokens (titles-only):**

  * `TWO_RUN_IDENTITY_OK`

  * `AB_BA_PARITY_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `NO_IO_NO_CLOCKS_OK`

  ### Subtask HDE-DISS004.1 — No I/O, no clocks, no globals

* **Subtask name/label:** Pure compute (no I/O/clocks/globals)

* **Subtask description:**  
   Ensure the Engine Core performs no I/O and does not access clocks, environment, filesystem, network, or process-wide globals; prove via static/grep guard and import-graph analysis.

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `NO_IO_NO_CLOCKS_OK`

* **Evidence / artifacts:**

  * `artifacts/engine/guards/no_io_no_clock.report` — static proof (no I/O, clocks, globals)

  ### Subtask HDE-DISS004.2 — AB↔BA parity & two-run identity

* **Subtask name/label:** AB↔BA & two-run identity for Engine Core

* **Subtask description:**  
   Prove that executions are AB↔BA neutral (swapping A,B yields byte-identical outputs) and satisfy two-run identity (running twice with same inputs yields identical outputs).

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

  * `AB_BA_PARITY_OK`

* **Evidence / artifacts:**

  * `artifacts/engine/tworun_identity.log` — two-run identity proof

  * `artifacts/engine/abba_identity.bytes` — AB↔BA compare

  ### Subtask HDE-DISS004.3 — Canonical JSON for core-emitted evidence

* **Subtask name/label:** Canonical JSON compare for core artifacts

* **Subtask description:**  
   Ensure any JSON emitted by the core for evidence is canonical (UTF-8/no BOM; sorted keys; compact; exactly one LF) and matches its canonical re-serialization (empty diff).

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts (family; titles-only):**

  * Canonical JSON compare artifacts for core (paths owned by HDE-Schemas & Artifacts; shared with Canonical Serialization Package)

  ### Subtask HDE-DISS004.4 — Evidence & indexing (engine core)

* **Subtask name/label:** Engine core evidence & indexing

* **Subtask description:**  
   Ensure two-run/ABBA/no-I/O proofs and canonical compare artifacts are indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` (records-only; one LF; unknown-key reject; fixed field order; proof\_anchor to path\_proof transcripts).

* **Subtask status:** **Not done**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  ---

  ## Task HDE-DISS005 — Band Thresholds & Tuning (admin)

* **Task ID:** HDE-DISS005

* **Task name/label:** Band Thresholds & Tuning (admin)

* **Task status:** Done

* **Task description:** Admin-only band thresholds & tuning workflow: pin inclusive-high band policy with edge fixtures, route numeric thresholds to the constants pack, capture diffs and identity hashes for tuning runs, and index tuning artifacts under the Evidence Index.  
* **Task notes:**  
  * **Status lock (PF16):** PF09 Phase-II “Band thresholds & tuning (admin)” is satisfied under **HDE-EPIC007 — Magic-10 Category Engine (Signals)** and is not carried forward to remaining epics.

  * **Historical audit:** Audit (v1 — 2025-11-17) remains as historical context only. Current canon treats this checklist task as fully closed by EPIC-007. Any new tuning work must be routed via **HDE Phased Epics**, not by reopening this row.


  

  ### **Subtask HDE-DISS005.1 — Band policy & edge fixtures**

* **Subtask name/label:** Band edge fixtures (24/49/74/100)

* **Subtask description:**  
   Pin inclusive-high band policy; add edge-case fixtures at 24/49/74/100 per preset (with \+1 transitions).

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `BAND_EDGE_GOLDENS_OK`

* **Evidence / artifacts:**

  * `artifacts/thresholds/*.json`

  * `audit/gates/bands/edges.snapshot.json`

  ---

  ### **Subtask HDE-DISS005.2 — Route thresholds to constants pack**

* **Subtask name/label:** Route thresholds to constants pack & keep public numeric-free

* **Subtask description:**  
   Route numeric thresholds to the constants pack (HDE-Math-Spec / HDE-Schemas & Artifacts) and keep public output numeric-free.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `M10_MAPS_OK`

* **Evidence / artifacts:**

  * `artifacts/thresholds/*.json` (constants pack-aligned)

  ---

  ### **Subtask HDE-DISS005.3 — Diffs & identity hash for tuning runs**

* **Subtask name/label:** Tuning diffs & identity hash

* **Subtask description:**  
   Capture compact diffs per change and compute `identity_hash` over the LF-terminated compat body for each tuning run.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `RELEASE_ID_RECOMPUTE_OK`

* **Evidence / artifacts:**

  * `audit/gates/bands/edges.diff.json`

  * `artifacts/thresholds/identity_hash.txt`

  ---

  ### **Subtask HDE-DISS005.4 — Evidence & indexing (bands)**

* **Subtask name/label:** Band thresholds evidence & indexing

* **Subtask description:**  
   Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs) for all band thresholds artifacts, following Evidence Index & mirror discipline.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  ---

  ## **Task HDE-DISS006 — Category Framework (internal)**

* **Task ID:** HDE-DISS006

* **Task name/label:** Category Framework (internal)

* **Task status:** **Done**

* **Task description:**  
   Implement per-category calculators and precedence hooks over Magic-10, enforce frozen category order and AB↔BA/two-run identity, and integrate per-channel mechanics for category-level behavior, with canonical JSON evidence and indexing.

* **Task notes:**

  * **Status lock (HDE-EPIC007 — Magic-10 Category Engine (Signals)):**  
     PF09 Phase-II “Category framework” is satisfied under **HDE-EPIC007**; this checklist row is history-only and does not carry forward to remaining epics.

  * **Status (Audit v1 — 2025-11-17):**  
     Previously marked *Not done* and called out missing `CATEGORY_FRAMEWORK_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, and `TWO_RUN_IDENTITY_OK` tokens, as well as missing Magic-10 key table and compat parity evidence.  
     These audit notes are now historical context only; acceptance lives in the EPIC-007 exit set and associated manifest/acceptance maps.

* **Task-level tokens (titles-only):**

  * `CATEGORY_FRAMEWORK_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `AB_BA_PARITY_OK` (category layer)

  * `TWO_RUN_IDENTITY_OK`

  ---

  ### **Subtask HDE-DISS006.1 — Per-category calculators & precedence hooks**

* **Subtask name/label:** Category calculators & precedence

* **Subtask description:**  
   Implement per-category calculators and precedence hooks; use total-order utilities (§5) for any ordered emission.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `CATEGORY_FRAMEWORK_OK`

* **Evidence / artifacts:**

  * `artifacts/category/calculators.snapshot.json` — governed calculators snapshot (schema single-home: PF12)

  ---

  ### **Subtask HDE-DISS006.2 — Frozen Magic-10 order & ABBA / two-run**

* **Subtask name/label:** Magic-10 order & symmetry

* **Subtask description:**  
   Enforce frozen Magic-10 order at all emission points and enforce AB↔BA and two-run identity for category-level outputs.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `AB_BA_PARITY_OK` (category layer)

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/category/abba_identity.bytes` — ABBA identity evidence for category outputs.

  ---

  ### **Subtask HDE-DISS006.3 — Per-channel mechanics integration**

* **Subtask name/label:** Per-channel category mechanics

* **Subtask description:**  
   Integrate per-channel mechanics into the category framework:

  * Treat channels as canonical `NN-NN` edges.

  * Track compromise direction \+ gate.

  * Treat circuit as channel-scoped, with optional bridge/timing analytics for internal use.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `CATEGORY_FRAMEWORK_OK`

* **Evidence / artifacts:**

  * Captured in category calculators snapshots and ABBA logs listed above.

  ---

  ### **Subtask HDE-DISS006.4 — Canonical JSON & evidence**

* **Subtask name/label:** Category framework canonical JSON & evidence

* **Subtask description:**  
   Ensure category framework evidence (calculators snapshot, ABBA identity, canonical-compare logs) uses canonical JSON and satisfies JSON re-serialization compare (UTF-8/no BOM; sorted keys; compact; one LF).

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts (titles/paths only):**

  * `artifacts/category/calculators.snapshot.json`

  * `artifacts/category/abba_identity.bytes`

  * Canonical-compare logs (paths owned by Evidence Index)

  ---

  ### **Subtask HDE-DISS006.5 — Evidence & indexing (category framework)**

* **Subtask name/label:** Category framework evidence & indexing

* **Subtask description:**  
   Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs) for category framework artifacts, using the global Evidence Index & mirror rules.

* **Subtask status:** **Complete (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  ---

# Phase III — Separation (Public shape, identity, guardrails)

* **Phase description:**  
   Wire persistence, public presenter/emitter, error envelope, and internal ops identity surfaces so that public and operator-visible bytes are canonical, deterministic, and backed by indexed evidence.

* **Phase master status:** **Mixed**

* **Notes:**

---

## Task HDE-SEPA001 — Persistence Layer

* **Task ID:** HDE-SEPA001

* **Task name/label:** Persistence Layer

* **Task description:**  
   Persist public results and provenance with canonical bytes, an explicit link to `release_id`, idempotent DB writes, and integrity checks that stored bodies equal emitted bodies, under least‑privilege DB posture and without logging secrets/PII.

* **Task status:** **Complete** (marked “Done”)

* **Task notes:**

  * Writer surfaces use `Cache-Control: no-store`.

  * DDL and grants are kept current; PF09 consumes but does not define token semantics.

### Subtask HDE-SEPA001.1 — Idempotent write path to DB

* **Subtask ID:** HDE-SEPA001.1

* **Subtask name/label:** Idempotent DB write path

* **Subtask description:**  
   Ensure an idempotent write path to the DB for public payloads so that repeated writes do not produce double‑writes or drift.

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:** Unknown (idempotent write tokens live in HDE-Governance; PF09 is consumer‑only).

* **Evidence / artifacts:**

  * Implicit in DB and persistence tests (paths not pinned in PF09).

* **Notes:**  
   The checklist calls out idempotence as an expectation, not by a specific token name.

### Subtask HDE-SEPA001.2 — Canonical byte-compare vs emitter

* **Subtask ID:** HDE-SEPA001.2

* **Subtask name/label:** Stored body equals emitter output

* **Subtask description:**  
   Verify via canonical byte-compare that the stored public body in the DB is **byte‑for‑byte equal** to the emitter output.

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:**

  * Likely uses `JSON_CANONICAL_CHECK_OK` indirectly (semantics live in canon; not named here).

* **Evidence / artifacts:**

  * `artifacts/presenter/json_canon_compare.log`

### Subtask HDE-SEPA001.3 — Grants / DDL least-privilege posture

* **Subtask ID:** HDE-SEPA001.3

* **Subtask name/label:** DB grants & DDL posture

* **Subtask description:**  
   Keep DB grants and DDL artifacts current and consistent with least‑privilege posture for persistence of public payloads.

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:** Unknown (DB security tokens live in Governance).

* **Evidence / artifacts:**

  * `artifacts/db/ddl_applied.sql`

  * `artifacts/db/grants.txt`

### Subtask HDE-SEPA001.4 — No secrets/PII in logs

* **Subtask ID:** HDE-SEPA001.4

* **Subtask name/label:** Logging discipline (no secrets/PII)

* **Subtask description:**  
   Ensure that persistence and writer pathways do **not** emit secrets or PII into logs; logs are keys‑only and redacted as needed.

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:** Unknown (log‑scrubbing tokens live in Governance).

* **Evidence / artifacts:**

  * Logging configuration and tests (paths not pinned here).

### Subtask HDE-SEPA001.5 — Identity snapshot for services

* **Subtask ID:** HDE-SEPA001.5

* **Subtask name/label:** Service identity snapshot

* **Subtask description:**  
   Maintain a service identity snapshot for persisted public results and provenance.

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:**

  * Supports identity/provenance tokens (e.g., `RELEASE_ID_RECOMPUTE_OK` indirectly; semantics elsewhere).

* **Evidence / artifacts:**

  * `artifacts/identity/service_identity.json`

### Subtask HDE-SEPA001.6 — Persistence evidence indexing

* **Subtask ID:** HDE-SEPA001.6

* **Subtask name/label:** Evidence Index & Machine Mirror parity (persistence)

* **Subtask description:**  
   Index persistence evidence in the Human Evidence Index and Machine Mirror in the same PR:

  * Update `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`.

  * Update `artifacts/evidence_index.jsonl` (records-only canonical JSONL; UTF‑8, one LF; unknown‑key reject; fixed field order; each record includes a `proof_anchor` to a co‑located path\_proof).

* **Subtask status:** **Complete**

* **Epic or card:** Unknown

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## Task HDE-SEPA002 — Error Envelope & Token Set

* **Task ID:** HDE-SEPA002

* **Task name/label:** Error Envelope & Token Set

* **Task description:**  
   Provide a central typed, numeric‑free error envelope with canonical JSON, validated token map, Reader↔CLI parity, CLI stream discipline, and evidence indexed in the Evidence Index and Machine Mirror.

* **Task status:** **Not done**

* **Task notes:**

  * Audit v1 (2025‑11‑17): missing `CLI_STDERR_ONLY_ON_ERROR_OK`, `CLI_STDOUT_LF_OK`, `JSON_CANONICAL_CHECK_OK`; writers/errors header posture is not yet proven on a Catalog success route; no passing evidence artifacts recorded.

  * Behavior is well‑specified but tokens/evidence are incomplete.

### Subtask HDE-SEPA002.1 — Error envelope shape & numeric-free body

* **Subtask ID:** HDE-SEPA002.1

* **Subtask name/label:** Typed, numeric‑free error envelope

* **Subtask description:**  
   Emit error bodies as typed, numeric‑free JSON:

  * Shape: `{"ok": false, "code": "…", "error": "…“}` only.

  * LF‑terminated, serialized by the single presenter/emitter.

  * No PII, no payload echoes, no SR/XR numerics.

* **Subtask status:** **Not started / evidence missing** (spec is present, but package is marked Not done)

* **Epic or card:** Unknown

* **Tokens:**

  * `ERROR_JSON_CANON_OK` (shape & canonicality)

* **Evidence / artifacts:**

  * `errors/schema_check` (envelope shape; see 002.8)

### Subtask HDE-SEPA002.2 — Error transport headers (writers/errors)

* **Subtask ID:** HDE-SEPA002.2

* **Subtask name/label:** Error transport headers (no-store, no ETag)

* **Subtask description:**  
   For error responses, enforce:

  * `Content-Type: application/json; charset=utf-8`

  * `Cache-Control: no-store`

  * No `ETag` header  
     on writers/errors routes, which are **not** Catalog‑eligible; A7 success proofs stay bound to Catalog success routes only.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * Header‑posture tokens (names live in Governance; not restated here).

* **Evidence / artifacts:**

  * `tests/transport/headers/no_store_writers_errors.snap`

### Subtask HDE-SEPA002.3 — Error token map & casing

* **Subtask ID:** HDE-SEPA002.3

* **Subtask name/label:** Token map & lower\_snake casing

* **Subtask description:**  
   Maintain a canonical error token→message table that:

  * Matches a golden map byte‑for‑byte.

  * Uses lower\_snake casing for all tokens.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `ERROR_TOKEN_MAP_OK`

* **Evidence / artifacts:**

  * `errors/token_map` — canonical token→message snapshot (golden).

### Subtask HDE-SEPA002.4 — Canonical JSON for error envelopes

* **Subtask ID:** HDE-SEPA002.4

* **Subtask name/label:** Canonical JSON & re‑serialization check

* **Subtask description:**  
   Ensure error responses are canonical JSON:

  * UTF‑8 (no BOM).

  * ASCII‑sorted keys.

  * Compact; exactly one trailing LF.

  * Arrays‑as‑sets deduped and ASCII‑sorted.  
     Prove canonicality via re‑serialization compare (expected empty diff).

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `ERROR_JSON_CANON_OK`

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/canonical/json_canon_compare.log`

  * `errors/canonical_check` — encoding/key‑order/compact/LF proof

### Subtask HDE-SEPA002.5 — Reader↔CLI error parity & two-run identity

* **Subtask ID:** HDE-SEPA002.5

* **Subtask name/label:** Error parity & determinism

* **Subtask description:**  
   Ensure that for the same error condition:

  * Reader and CLI emit **byte‑identical** error envelopes.

  * Re‑emitting the same error twice produces bitwise‑identical bytes.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `parity/errors_reader_cli` — byte‑equality proofs

    ### **Subtask HDE-SEPA002.6 — CLI stderr/stdout discipline & usage exit 64**

*Subtask name/label:* CLI stderr/stdout discipline & usage exit code

*Subtask description:*

Enforce CLI stream and exit-code discipline for all CLI commands in alignment with the mechanics and CLI spec:

* **Streams:**

  * Successful runs write **only** the public JSON body to `stdout`, LF-terminated, with no ANSI escapes and no extra bytes.

  * Error runs write typed, numeric-free JSON error envelopes to `stderr` only; successful runs **never** write to `stderr`.

  * No mixed streams: a run is either stdout-only success or stderr-only failure.

* **Exit codes:**

  * `0` on success (canonical JSON body on stdout; stderr empty).

  * `64` on usage errors (bad flags/arguments or invalid invocation); on usage error, stdout is empty and diagnostics appear only as a typed error envelope on stderr.

  * Other failures use non-zero codes as defined in Governance/CLI specs; stdout remains empty on failure.

*Subtask status:* Not started (behavior specified; evidence pending)

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `CLI_USAGE_ERR_EXIT64_OK`

* `CLI_STDERR_ONLY_ON_ERROR_OK`

* `CLI_STDOUT_LF_OK`

*Evidence / artifacts (titles/paths only):*

* CLI harness logs and tests that cover:

  * A successful command with canonical JSON on stdout and empty stderr.

  * A usage-error case (exit code 64\) with empty stdout and an error envelope on stderr.

* Indexing of these artifacts follows the global Evidence Index & Machine Mirror discipline (front matter 0.3–0.5); PF09 does not restate mirror schemas.

### Subtask HDE-SEPA002.7 — Writers/errors headers posture validation

* **Subtask ID:** HDE-SEPA002.7

* **Subtask name/label:** Writers/errors header posture proofs

* **Subtask description:**  
   Prove that when the error envelope appears on writers/errors routes, response headers match Governance:

  * `Cache-Control: no-store`

  * No `ETag`

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * Header posture tokens (names live in Governance).

* **Evidence / artifacts:**

  * `tests/transport/headers/no_store_writers_errors.snap`

### Subtask HDE-SEPA002.8 — Error-envelope evidence & indexing

* **Subtask ID:** HDE-SEPA002.8

* **Subtask name/label:** Error evidence families & indexing

* **Subtask description:**  
   Maintain and index error-envelope evidence families:

  * `errors/token_map` — canonical token→message snapshot (golden).

  * `errors/schema_check` — JSON-Schema validation for error-envelope shape.

  * `errors/canonical_check` — encoding/key‑order/compact/LF proof.

  * `parity/errors_reader_cli` — Reader↔CLI byte‑equality proofs.  
     List all in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR (records‑only canonical JSONL; one LF; unknown‑key reject; fixed field order; each record includes a `proof_anchor` to a co‑located path\_proof transcript).

* **Subtask status:** **Not done**

* **Epic or card:** Unknown

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `artifacts/evidence_index.jsonl`

  * `errors/*` evidence artifacts listed above

---

## Task HDE-SEPA003 — Public Presenter / Emitter

* **Task ID:** HDE-SEPA003

* **Task name/label:** Public Presenter / Emitter

* **Task description:**  
   Ensure Reader and CLI share a single allow‑listed presenter/emitter symbol, emit canonical JSON, enforce stream discipline, satisfy ABBA/two‑run identity, and prove the preimage flow with indexed evidence.

* **Task status:** **Not done**

* **Task notes:**

  * Audit (2025‑11‑18): Reader↔CLI parity fails under rails‑closed in at least one case (`Warm/alpha` vs `Open/dev`); CLI `showcompat` sometimes produced empty or non‑matching output.

  * A shared emitter path is specified in canon but not yet proven in evidence.

### Subtask HDE-SEPA003.1 — Single shared presenter/emitter symbol

* **Subtask ID:** HDE-SEPA003.1

* **Subtask name/label:** Shared emitter entrypoint

* **Subtask description:**  
   Ensure Reader and CLI both call the **same** presenter/emitter entrypoint symbol, enforced via a CI allow‑list.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/guards/emitter_symbol_proof.txt` — import‑graph/symbol proof

  * `artifacts/cli/guards/serializer_grep_guard.log` — grep guard for ad‑hoc serializers

### Subtask HDE-SEPA003.2 — Canonical JSON & non-empty showcompat

* **Subtask ID:** HDE-SEPA003.2

* **Subtask name/label:** Canonical showcompat output

* **Subtask description:**  
   Prove that `showcompat` emits non‑empty, LF‑terminated canonical JSON:

  * UTF‑8 (no BOM).

  * ASCII‑sorted keys.

  * Compact; one trailing LF.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `CLI_SHOWCOMPAT_CANON_OK`

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * `artifacts/presenter/preimage_recompute.log` (preimage & canonical checks)

### Subtask HDE-SEPA003.3 — Streams discipline for presenter flows

* **Subtask ID:** HDE-SEPA003.3

* **Subtask name/label:** stdout/stderr discipline for public flows

* **Subtask description:**  
   Enforce stream discipline:

  * Success → `stdout` with exactly one LF.

  * Errors → `stderr` only.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `CLI_STDOUT_LF_OK`

  * `CLI_STDERR_ONLY_ON_ERROR_OK`

* **Evidence / artifacts:**

  * CLI harness logs (paths not pinned here).

### Subtask HDE-SEPA003.4 — AB↔BA and two-run identity for presenter

* **Subtask ID:** HDE-SEPA003.4

* **Subtask name/label:** ABBA/two-run parity for presenter surfaces

* **Subtask description:**  
   Re‑prove that on parity flows:

  * `(A,B)` vs `(B,A)` produce identical bytes (AB↔BA).

  * Two runs with identical inputs produce bitwise‑identical public bytes.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `TWO_RUN_IDENTITY_OK`

  * `COMPOSITE_ABBA_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/presenter/reader_cli_parity.bytes` — Reader↔CLI parity sample

### Subtask HDE-SEPA003.5 — Preimage recompute & identity coupling

* **Subtask ID:** HDE-SEPA003.5

* **Subtask name/label:** Preimage recompute & identity proof

* **Subtask description:**  
   Prove that preimage hashing (`idempotence_hash`) and identity coupling (e.g., `release_id`) are correct by recomputing preimage/digests and comparing against emitted bytes.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `PREIMAGE_RECOMPUTE_OK`

* **Evidence / artifacts:**

  * `artifacts/presenter/preimage_recompute.log`

### Subtask HDE-SEPA003.6 — Presenter evidence indexing

* **Subtask ID:** HDE-SEPA003.6

* **Subtask name/label:** Presenter evidence & indexing

* **Subtask description:**  
   Index presenter/emitter evidence artifacts in the Human Evidence Index and Machine Mirror in the same PR (records‑only; with path‑proofs), following global Evidence Index & mirror rules.

* **Subtask status:** **Not done**

* **Epic or card:** Unknown

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `artifacts/presenter/preimage_recompute.log`

  * `artifacts/presenter/reader_cli_parity.bytes`

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

---

## Task HDE-SEPA004 — Internal Ops Surface /internal/version

* **Task ID:** HDE-SEPA004

* **Task name/label:** Internal Ops Surface /internal/version

* **Task description:**  
   Provide an operator‑only, side‑effect‑free `/internal/version` endpoint that exposes engine identity, with no‑store/no‑ETag headers, HEAD parity, conditionals ignored, and fully indexed evidence.

* **Task status:** **Not done**

* **Task notes:**

  * Audit v1 (2025‑11‑17) lists missing `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`; headers/body proofs are incomplete and no full GET/HEAD/conditional/identity proof set exists.

### Subtask HDE-SEPA004.1 — GET/HEAD 200 parity

* **Subtask ID:** HDE-SEPA004.1

* **Subtask name/label:** GET/HEAD header parity

* **Subtask description:**  
   Implement HEAD parity for `/internal/version`:

  * `GET` returns 200 with JSON body.

  * `HEAD` returns 200, mirrors GET validators (including `Content-Type`), has no body, and `Content-Length == len(identity GET body)`.

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * `INTVER_200_CTYPE_JSON_UTF8_OK`

  * `INTVER_HEAD_PARITY_OK`

* **Evidence / artifacts:**

  * `artifacts/ops/internal_version/headers_get.txt`

  * `artifacts/ops/internal_version/headers_head.txt`

  * `artifacts/ops/internal_version/body_get.json`

  * `artifacts/ops/internal_version/body_get.sha256`

### **Subtask HDE-SEPA004.2 — Conditionals ignored (never 304\)**

* **Subtask ID:** HDE-SEPA004.2

* **Subtask name/label:** Conditional-ignore behavior

* **Subtask description:**  
   Ensure that `/internal/version` ignores conditional headers and never returns 304:

  * Requests with `If-None-Match` or `If-Modified-Since` still return 200 with the same body and headers as an ordinary GET.

* **Subtask status:** **Done**

* **Epic or card:** EPIC-017 (QA01 conditional GET verification)

* **Tokens:**

  * `INTVER_CONDITIONALS_IGNORED_OK`

* **Evidence / artifacts:**

  * `Audit/QA/HDE-EPIC017/logs/intver_get_conditional.txt` — conditional GET `/internal/version` with `If-*` headers showing 200 OK, `Cache-Control: no-store`, no `ETag`/`Last-Modified`, and a JSON body identical to the non-conditional GET.

  * `Audit/QA/HDE-EPIC017/logs/intver_get_full.txt` — baseline non-conditional GET `/internal/version` headers/body for comparison.

* **Notes:**  
   This QA evidence demonstrates that `/internal/version` ignores conditional headers for GET and never returns 304, while preserving header posture and body equality relative to non-conditional GET. The remaining open work for `/internal/version` (body-shape contract and identity/two-run proof) is tracked at the task level and in other subtasks, not here.

### Subtask HDE-SEPA004.3 — No-store & no ETag posture

* **Subtask ID:** HDE-SEPA004.3

* **Subtask name/label:** No-store, no ETag headers

* **Subtask description:**  
   Maintain ops-surface posture for `/internal/version`:

  * `Cache-Control: no-store`

  * No `ETag` header

  * No caching validators (no `Last-Modified`).

* **Subtask status:** **Done**

* **Epic or card:** EPIC-017 (QA01 conditional GET verification)

* **Tokens:**

  * `INTVER_200_NO_ETAG_OK`

* **Evidence / artifacts:**

  * `Audit/QA/HDE-EPIC017/logs/intver_get_full.txt` — GET `/internal/version` showing 200 OK, `Cache-Control: no-store`, JSON content type, and no `ETag`/`Last-Modified` headers.

  * `Audit/QA/HDE-EPIC017/logs/intver_head_full.txt` — HEAD `/internal/version` showing 200 OK, matching validators (including `Content-Type`) and no `ETag`/`Last-Modified`, with no body.

  * `Audit/QA/HDE-EPIC017/logs/intver_get_conditional.txt` — conditional GET `/internal/version` with `If-*` headers showing the same header posture (no-store, no validators, JSON content type) as the ordinary GET.

* **Notes:**  
   Together, these artifacts show that `/internal/version` consistently uses `Cache-Control: no-store` and omits `ETag` and `Last-Modified` for GET, HEAD, and conditional GET in Railway prod. Body-shape compliance (adding `invocation_sha256`, frozen field order) is still outstanding and is handled by other tasks; this subtask is scoped only to header posture.

### Subtask HDE-SEPA004.4 — Two-run identity & related identity artifacts

* **Subtask ID:** HDE-SEPA004.4

* **Subtask name/label:** Two-run identity & identity coupling

* **Subtask description:**  
   Prove two-run identity for `/internal/version` bodies and ensure they are consistent with identity/provenance artifacts:

  * Two consecutive GETs produce byte‑identical bodies (LF‑terminated).

  * Body values match identity & math artifacts (`release_id`, etc.).

* **Subtask status:** **Not started**

* **Epic or card:** Unknown

* **Tokens:**

  * Supports `TWO_RUN_IDENTITY_OK` for identity components (not named explicitly here).

* **Evidence / artifacts:**

  * `artifacts/ops/internal_version/two_run_identity.log`

  * `artifacts/math/freeze_pack_manifest.json`

  * `artifacts/math/release_id.txt`

  * `artifacts/math/release_id_recompute.log`

  * `artifacts/identity/emitter_sha256.txt`

### Subtask HDE-SEPA004.5 — Internal ops evidence indexing

* **Subtask ID:** HDE-SEPA004.5

* **Subtask name/label:** /internal/version evidence & indexing

* **Subtask description:**  
   Index all `/internal/version` artifacts and related identity artifacts in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in the same PR (records‑only canonical JSONL; one LF; unknown‑key reject; fixed field order; with path‑proofs).

* **Subtask status:** **Not done**

* **Epic or card:** Unknown

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * All artifacts listed in 004.1–004.4, plus their `path_proof` transcripts.

  * 

---

# **Phase IV — Conjunction (Surfaces and tools meet the core)**

* **Phase description:**  
   Wire dev/test HTTP harnesses, compat and Reader public surfaces, CLI surfaces and tooling, and writer APIs to the deterministic engine core, enforcing canonical JSON, A7 transport posture, and Index/Mirror discipline.

* **Phase master status:** **Mixed**

  * **Done:** Dev HTTP Harness (single home)

  * **Not done:** Compat Surface (internal), CLI Serializer Coupling, CLI Conformance, Reader Surface (API), Caching & Transport Wiring (Reader), CLI Tooling (showcompat, sample), Writer Surfaces (API), Global discipline

* **Notes:**

  * Many tasks in this phase share artifacts and tokens (especially CLI and Reader A7/A8 surfaces). This structure keeps them trackable as separate checklist rows while acknowledging shared evidence.

  ---

  ## Task HDE-CONJ001 — Dev HTTP Harness (single home)

* **Task ID:** HDE-CONJ001

* **Task name/label:** Dev HTTP Harness (single home)

* **Task status:** **Done**

* **Task description:**  
   Provide a single dev/QA HTTP harness for end-to-end validation of the Engine that exercises Reader/CLI surfaces without being a production surface, enforces no-store and canonical JSON, and maintains evidence and Index/Mirror entries.

* **Task notes:**

  * Single home for local/QA validation of the Engine: end-to-end HTTP runs that exercise the Reader/CLI surfaces without being production surfaces.

  * Defaults:

    * `Cache-Control: no-store` on all harness responses.

    * Never exposes SR/XR numerics or other internal scores in public JSON.

    * Runs under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

  * Supplemental only:

    * Authoritative A7 proofs live on the Catalog JSON success route.

    * Harness may call the same emitter and logic; A7 acceptance is driven by Catalog route artifacts and tokens.

  * PF09 is consumer-only; token semantics and schemas live in Governance/CLI/Schemas.

### **Subtask HDE-CONJ001.1 — Harness behavior & non-production posture**

* **Subtask name/label:** Harness behavior & non-production posture

* **Subtask description:**  
   Ensure the dev HTTP harness is the single home for local/QA Engine validation and remains strictly non-production:

  * **Dev-only posture.**

    * Bound only to loopback (for example `127.0.0.1`) and not exposed as a public surface.

    * CORS disabled for harness routes.

    * Runs with `APP_ENV=dev` when capturing evidence; debug reloader is OFF during evidence runs.

  * **Response and payload posture.**

    * Uses `Cache-Control: no-store` on all harness responses.

    * Never exposes SR/XR numerics or other internal scores in JSON outputs.

    * Emits canonical JSON via the shared presenter/emitter (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and sorted), under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* PF09 does not pin the exact set of dev routes or curl commands; those remain documented in Mechanics and CLI/API docs by title. This subtask requires that the harness be dev-only, loopback-bound, canonical, and non-public when used for evidence.

* **Subtask status:** **Complete** (behavioral target; evidence already exists for current harness)

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (rails, transport, and canonical JSON tokens live in Governance and other tasks; PF09 is consumer-only here)

* **Evidence / artifacts:**

  * `tests/harness/test_end_to_end.py` (behavioral tests that exercise Reader/CLI surfaces through the harness)


  ### Subtask HDE-CONJ001.2 — Harness parity & canonicalization

* **Subtask name/label:** Harness parity with CLI & canonical JSON

* **Subtask description:**  
   Prove that the harness:

  * Matches CLI behavior for supported flows (harness parity with CLI).

  * Exhibits AB↔BA parity on compat payloads for pair inputs.

  * Passes canonicalization checks (canonical JSON, LF-termination, sorted keys, arrays-as-sets deduped and sorted).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (token semantics are referenced only by title)

* **Evidence / artifacts:**

  * `audit/gates/parity/*.bytes`

  * `audit/gates/canonical_json/*.log`

  ### Subtask HDE-CONJ001.3 — Harness evidence indexing

* **Subtask name/label:** Harness Evidence Index & Machine Mirror

* **Subtask description:**  
   Index harness evidence in the human Evidence Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

* **Subtask status:** **Complete**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ002 — Compat Surface (internal)

* **Task ID:** HDE-CONJ002

* **Task name/label:** Compat Surface (internal)

* **Task status:** **Not done**

* **Task description:**  
   Implement an internal-only compat surface using the shared presenter/emitter, with canonical JSON, AB↔BA parity (including Integration channels), and identity\_hash capture, and index its evidence.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * Missing tokens (titles-only; tokens live in Governance/Schemas):

    * `CATEGORY_FRAMEWORK_OK`

    * `AB_BA_PARITY_OK`

    * `JSON_CANONICAL_CHECK_OK`

    * `TWO_RUN_IDENTITY_OK`

  * No Magic-10 key table or compat parity logs recorded for this internal surface.

  * Internal endpoint for pair-compat emission and QA; not a public product surface.

  * Uses the same presenter/emitter as Reader/CLI.

  * Never exposes SR/XR numerics on Reader; any CLI-only diagnostic sidecar is flag-guarded and admin-only.

  ### Subtask HDE-CONJ002.1 — Compat endpoint semantics

* **Subtask name/label:** Internal compat endpoint behavior

* **Subtask description:**  
   Maintain an internal endpoint for pair-compat emission and QA that:

  * Uses the shared presenter/emitter.

  * Is not a public product surface.

  * Never exposes SR/XR numerics on Reader; CLI diagnostics (if any) are flag-guarded and admin-only.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * Endpoint implementation and tests (paths not pinned here).

  ### Subtask HDE-CONJ002.2 — Canonical compat JSON & parity

* **Subtask name/label:** Canonical compat output & ABBA parity

* **Subtask description:**  
   Ensure internal compat responses:

  * Are canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays-as-sets deduped and sorted.

  * Obey AB↔BA parity on the full compat body, including Integration channel cases (e.g. `20–34` vs `20–57`).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CATEGORY_FRAMEWORK_OK`

  * `AB_BA_PARITY_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `tests/compat/test_abba_parity.py`

  ### Subtask HDE-CONJ002.3 — identity\_hash capture

* **Subtask name/label:** identity\_hash for compat payloads

* **Subtask description:**  
   Capture `identity_hash` for compat payloads as sha256 over the LF-terminated compat body for internal/admin evidence.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `AB_BA_PARITY_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/compat/identity_hash.txt`

  ### Subtask HDE-CONJ002.4 — Compat evidence indexing

* **Subtask name/label:** Compat surface Evidence Index & mirror

* **Subtask description:**  
   Index compat artifacts (`artifacts/compat/identity_hash.txt`, `tests/compat/test_abba_parity.py`) in the human Evidence Index and machine mirror in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ003 — CLI Serializer Coupling

* **Task ID:** HDE-CONJ003

* **Task name/label:** CLI Serializer Coupling

* **Task status:** **Not done**

* **Task description:**  
   Ensure CLI, Reader, and compat flows in tests all use the same presenter/emitter symbol as production, enforce an allow-list of emitters, and prove parity/determinism and absence of ad-hoc JSON via grep/symbol proofs and evidence.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17).**

  * Test harnesses that exercise public JSON (Reader, CLI, compat) MUST call the same presenter/emitter symbol used in production.

  * No test-only serializers or bypass paths allowed for public bytes.

  * Maintain an explicit allow-list of presenter/emitter symbols; CI must enforce it and keep grep/symbol proofs consistent.

  * Missing tokens (titles-only):

    * `CLI_READER_EMITTER_PARITY_OK`

    * `CLI_NO_ALT_JSON_OK`

    * `CLI_SHOWCOMPAT_CANON_OK`

    * `TWO_RUN_IDENTITY_OK`

  * Grep/symbol proof artifacts not yet recorded.

  * Reader and CLI share one emitter:

    * CLI Reader surfaces (stdout or `--dump-reader`) must be byte-identical to the Reader body.

    * No ad-hoc serializers on public paths; guarded via grep and import-graph symbol proofs.

  ### Subtask HDE-CONJ003.1 — Shared emitter in tests

* **Subtask name/label:** Test harness uses production presenter/emitter

* **Subtask description:**  
   Ensure all test harnesses that exercise public JSON (Reader, CLI, compat) call the same presenter/emitter symbol used in production; no test-only serializers or bypass paths permitted.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_NO_ALT_JSON_OK`

* **Evidence / artifacts:**

  * `tests/test_emitter_determinism.py`

  ### Subtask HDE-CONJ003.2 — Emitter allow-list & grep/symbol proofs

* **Subtask name/label:** Emitter allow-list enforcement

* **Subtask description:**  
   Maintain and enforce an explicit allow-list of presenter/emitter symbols for public bytes; CI uses grep/symbol proofs to ensure only allow-listed symbols serialize public bytes.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CLI_NO_ALT_JSON_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

  ### Subtask HDE-CONJ003.3 — CLI/Reader parity & canonical JSON

* **Subtask name/label:** CLI/Reader parity & canonical JSON checks

* **Subtask description:**  
   Prove that CLI Reader surfaces (stdout / `--dump-reader`) are byte-identical to Reader bodies and that outputs are canonical JSON with LF-termination.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_SHOWCOMPAT_CANON_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `tests/test_emitter_determinism.py`

  * `artifacts/cli/reader_cli_parity.bytes`

  ### Subtask HDE-CONJ003.4 — Serializer coupling evidence indexing

* **Subtask name/label:** Serializer coupling Evidence Index & mirror

* **Subtask description:**  
   Index `tests/test_emitter_determinism.py`, `serializer_grep_guard.log`, `emitter_symbol_proof.txt`, and `reader_cli_parity.bytes` in the human Evidence Index and machine mirror in the same PR (records-only JSONL; one LF; with path-proofs).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ004 — CLI Conformance

* **Task ID:** HDE-CONJ004

* **Task name/label:** CLI Conformance

* **Task status:** **Not done**

* **Task description:**  
   Prove CLI installation and entrypoints, showcompat wiring, canonical JSON output, CLI↔Reader parity, AB↔BA/two-run identity for CLI compat flows, and index the key CLI artifacts.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * No CLI conformance artifacts recorded for `ab.json` / `ba.json` / `summary.json`.

  * CLI parity/determinism harness exists as a plan; acceptance tokens not yet proven or indexed.

  * Goal:

    * `showcompat` present and wired.

    * CLI outputs LF-terminated canonical JSON.

    * Reader↔CLI parity established.

    * AB↔BA & two-run identity proven for CLI compat flows.

    * Installation and help flows exit cleanly.

### **Subtask HDE-CONJ004.1 — CLI install and entrypoints**

* Subtask ID: HDE-CONJ004.1

* Subtask name/label: CLI installation and entrypoint checks

* Subtask description:  
   Validate CLI installation and entrypoints:

  * pyproject entrypoint is available and working.

  * python \-m entrypoint is available and working.

  * Installation path is correct for the target environment.

  * hdctl \--help exits with status 0 and prints help text to stdout.

* Subtask status: Partial

* Epic or card: EPIC-017 (QA02 CLI help availability)

* Tokens:

  * CLI\_PYPROJECT\_ENTRYPOINT\_OK

  * CLI\_MODULE\_RUN\_OK

  * CLI\_INSTALL\_OK

  * CLI\_HELP\_EXIT\_0\_OK

  * CLI\_HELP\_STDOUT\_OK  
  * CLI\_HELP\_OK

* Evidence / artifacts:

  * EPIC017 QA02 hdctl help run (Codespaces → Railway): help banner showing hdctl is on PATH, runs successfully, and exposes the subcommands showcompat, aux-preview, and bg:resolve with concise, canon-consistent descriptions (stored under the EPIC017 QA logs area; path not pinned here).

  * Future CLI install and entrypoint logs (pyproject entrypoint, python \-m entrypoint, installation path) to be captured and indexed when those aspects are exercised.

* Notes:

  * For EPIC017 QA02, the acceptance criterion for this slice is that the hdctl CLI entrypoint exists in the Codespace environment, runs without error, and exposes the three expected subcommands. That confirms CLI availability and shape so later QA steps can safely rely on hdctl for compat, aux-preview, and bg:resolve runs.

  * This subtask remains Partial because it still requires explicit evidence for pyproject and python \-m entrypoints and installation path across supported environments; those will be validated and indexed in future work. The help-related tokens (CLI\_HELP\_EXIT\_0\_OK and CLI\_HELP\_STDOUT\_OK) are considered covered for EPIC017 in the Codespaces → Railway QA setup, but the broader CLI installation and entrypoint tokens remain open until additional evidence is captured.

### **Subtask HDE-CONJ004.2 — showcompat canonical JSON & presence**

* Subtask name/label: showcompat presence and canonical JSON

* Subtask description:  
   Ensure showcompat is present and wired, emitting LF-terminated canonical JSON and participating in the CLI parity harness for compat flows.

* Subtask status: Partial

* Epic or card: EPIC-017 (QA03 showcompat from birth data)

* Tokens:

  * CLI\_SHOWCOMPAT\_PRESENT

  * CLI\_SHOWCOMPAT\_CANON\_OK

  * JSON\_CANONICAL\_CHECK\_OK

* Evidence / artifacts:

  * EPIC017 QA03 showcompat run in Codespaces: hdctl showcompat \--source vendor with synthetic birth-only inputs producing a single compat JSON object (top-level keys a, b, compat, viewer\_prefs) with 10 Magic-10 categories, band and score fields, neutral viewer\_prefs (all weights set to 50), and a CLI meta block (local engine\_tag, invocation\_tag, and all-zero release\_id).

  * Planned and existing CLI harness artifacts for canonical JSON and parity (mechanics-level evidence):

    * artifacts/cli/ab.json

    * artifacts/cli/ba.json

    * artifacts/cli/summary.json

* Notes:

  * EPIC017 QA03 proves that showcompat is present and runnable in the Codespaces environment, and that showcompat \--source vendor from birth-only input produces a compat JSON payload with 10 Magic-10 categories, bands, scores, neutral viewer\_prefs, and a CLI-scoped meta section. For this QA step, the acceptance criterion is simply “compat JSON produced from births with explicit \--source vendor”; AB↔BA parity, Reader envelope checks, and vendor ingest traces are intentionally deferred to later QA steps.

  * In the current pre-App, no-user posture, showcompat from births must be invoked with \--source vendor to avoid hanging or following DB/auto paths that are not appropriate for this environment; the default showcompat without \--source remains discouraged for QA until DB-backed user flows and app integration exist.

  * The meta fields in compat output (engine\_tag \= hdengine-dev, invocation\_tag \= INV-LOCAL, release\_id all zeros) are CLI/local identifiers and must not be confused with the Railway prod engine identity, which is governed by the /internal/version ops surface on Railway. This is an expected split between “CLI as QA console” and “prod engine identity,” not a canon violation.

  * This subtask is marked Partial because the full scope still requires canonical JSON enforcement and participation in the parity harness (AB↔BA, two-run identity, Reader↔CLI parity, and evidence indexing using artifacts/cli/ab.json, artifacts/cli/ba.json, and artifacts/cli/summary.json). Those aspects are covered mechanically by the Canonical Serialization Package and related subtasks and will be reflected here as Done once the CLI conformance harness and indexing are fully wired and passing.

  ### Subtask HDE-CONJ004.3 — CLI compat parity & determinism

* **Subtask name/label:** CLI ABBA & two-run identity

* **Subtask description:**  
   Prove Reader↔CLI parity and AB↔BA / two-run identity for CLI compat flows, using `ab.json`, `ba.json`, and `summary.json`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_AB_BA_PARITY_OK`

  * `CLI_TWO_RUN_IDENTITY_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json` (byte-identical to `ab.json`)

  * `artifacts/cli/summary.json`

  ### Subtask HDE-CONJ004.4 — CLI conformance evidence indexing

* **Subtask name/label:** CLI conformance Evidence Index & mirror

* **Subtask description:**  
   Index `ab.json`, `ba.json`, and `summary.json` in both the Human Index and machine mirror in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

    ### **Subtask HDE-CONJ004.5 — PF05 command catalog conformance**

*Subtask name/label:* PF05 command catalog conformance

*Subtask description:*

Verify that the implemented CLI command set and behavior conform to **HDE-CLI-API-Vendor-Ref** (titles-only), treating any divergence as a defect until either the CLI implementation or HDE-CLI-API-Vendor-Ref is updated:

* **Command catalog as single home.**

  * Use PF05’s command catalog and “CLI Overview & Conventions” sections as the single home for CLI commands, flags, and statuses.

  * Do not duplicate the catalog in PF09; this subtask only requires tests and evidence that compare actual CLI behavior to PF05.

* **Conformance behavior.**

  * For each implemented command, ensure:

    * Help/usage text matches PF05 (names, flags, required/optional arguments, subcommand descriptions).

    * Exit codes and streams behavior follow PF05 and the error envelope rules (success on stdout only; errors on stderr only; exit 64 for usage errors).

    * Payload shapes and error models conform to PF05 and the mechanics/transport rules (titles-only; schemas live in PF05/PF12).

  * Treat any mismatch between `hdctl` behavior and PF05 as a failing test (defect) until corrected.

* **Implemented set coverage.**

  * Ensure that the set of CLI commands implemented in the binary matches the PF05 catalog for the supported environment (no undocumented commands, no missing required commands).

  * Gate this via `CLI_IMPLEMENTED_SET_OK` to indicate that the implemented set is in sync with PF05.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* CLI conformance:

  * `CLI_PYPROJECT_ENTRYPOINT_OK`

  * `CLI_MODULE_RUN_OK`

  * `CLI_INSTALL_OK`

  * `CLI_HELP_EXIT_0_OK`

  * `CLI_HELP_STDOUT_OK`

  * `CLI_STDERR_ONLY_ON_ERROR_OK`

  * `CLI_IMPLEMENTED_SET_OK`

*Evidence / artifacts (titles/paths only):*

* CLI install/help/version logs and command-invocation tests that:

  * Show `hdctl` is installed and reachable (pyproject entrypoint and `python -m engine.cli`).

  * Verify `hdctl --help` and `hdctl --version` exit 0 and write to stdout (no stderr noise).

  * Exercise each documented command and compare observed flags/usage/behavior against PF05’s catalog.

* Indexing of these artifacts follows the global Evidence Index & Machine Mirror discipline (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`); PF09 does not restate Mirror schema.  
  ---

  ## Task HDE-CONJ005 — Reader Surface (API)

* **Task ID:** HDE-CONJ005

* **Task name/label:** Reader Surface (API)

* **Task status:** **Not done**

* **Task description:**  
   Provide a six-key Reader v1 envelope on a Catalog JSON success route via the shared presenter/emitter, prove A7 transport invariants (200/HEAD/304, ETag, Vary, encoding invariance), maintain an Endpoint Catalog, and index proofs.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * Missing tokens:

    * `ENDPOINTS_CATALOG_OK`

    * `ENDPOINTS_CATALOG_ENV_GATE_OK`

    * `A7_GET_QUOTED_ETAG_OK`

    * `A7_HEAD_PARITY_OK`

    * `A7_304_OMITS_CT_CL_OK`

    * `A7_VARY_AUTH_AE_OK`

    * `A7_ENCODING_INVARIANCE_OK`

    * `READER_200_CTYPE_JSON_UTF8_OK`

  * Catalog \+ GET/HEAD/304/encoding proofs are absent.

  ### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON

* **Subtask name/label:** Six-key Reader envelope & canonical JSON

* **Subtask description:**  
   Ensure public success body is the six-key envelope:

   {  
*   "reader\_version": "v1",  
*   "eligible": …,  
*   "categories": …,  
*   "meta": …,  
*   "release\_id": …,  
*   "idempotence\_hash": …  
* }  
*  Emitted via the single presenter/emitter as canonical JSON: UTF-8 (no BOM); ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and ASCII-sorted; checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `READER_200_CTYPE_JSON_UTF8_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/success_get.txt` (body \+ headers)

  ### Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates

* **Subtask name/label:** Endpoint Catalog entries & env gating

* **Subtask description:**  
   Maintain `docs/ENDPOINTS_CATALOG.json` as the single home for JSON success routes eligible for A7 proofs, with env-gates per entry; non-prod entries must be unreachable in prod.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `ENDPOINTS_CATALOG_OK`

  * `ENDPOINTS_CATALOG_ENV_GATE_OK`

* **Evidence / artifacts:**

  * `docs/ENDPOINTS_CATALOG.json`

  * `docs/ENDPOINTS_CATALOG.json.sha256`

  * `artifacts/proofs/endpoints_env_gate_proof.log`

  ### Subtask HDE-CONJ005.3 — A7 transport invariants (Reader)

* **Subtask name/label:** A7 GET/HEAD/304/encoding invariance (Reader)

* **Subtask description:**  
   On the Catalog JSON success route, prove:

  * Strong quoted ETag on 200\.

  * `Vary: Authorization, Accept-Encoding`.

  * HEAD 200 parity: `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

  * 304 only after prior 200; omit `Content-Type` and `Content-Length`.

  * POST non-conditional.

  * Writers/errors: `Cache-Control: no-store`, no `ETag`.

  * Encoding invariance: ETag and effective Content-Length stable across accepted encodings.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `A7_GET_QUOTED_ETAG_OK`

  * `A7_HEAD_PARITY_OK`

  * `A7_304_OMITS_CT_CL_OK`

  * `A7_VARY_AUTH_AE_OK`

  * `A7_ENCODING_INVARIANCE_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/success_get.txt`

  * `artifacts/proofs/success_head.txt`

  * `artifacts/proofs/success_304.txt`

  * `artifacts/proofs/success_encoding_invariance.txt`

  * `artifacts/proofs/success_writers_errors.txt`

  ### Subtask HDE-CONJ005.4 — Reader A7 evidence indexing

* **Subtask name/label:** Reader Catalog & A7 Evidence Index & mirror

* **Subtask description:**  
   Index Catalog and A7 artifacts (`docs/ENDPOINTS_CATALOG.*`, `success_get/head/304/encoding_invariance`, `endpoints_env_gate_proof.log`, `success_writers_errors.txt`) in both Human Index and machine mirror in the same PR.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ006 — Caching & Transport Wiring (Reader)

* **Task ID:** HDE-CONJ006

* **Task name/label:** Caching & Transport Wiring (Reader)

* **Task status:** **Not done**

* **Task description:**  
   Explicitly tie A7 proofs to the Catalog JSON success route and capture GET/HEAD/304/encoding/headers evidence with env-gate proof for Reader transport.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * A7 matrix not proven on a cataloged JSON success route; encoding invariance and env-gate evidence missing.

  ### Subtask HDE-CONJ006.1 — Enforce A7 matrix on Catalog route

* **Subtask name/label:** A7 matrix enforcement on Catalog route

* **Subtask description:**  
   Enforce the A7 matrix on the Catalog JSON success route:

  * ETag on 200 (over canonical LF-terminated body).

  * 304 omits `Content-Type` and `Content-Length`; no body.

  * HEAD 200 parity.

  * POST non-conditional.

  * Writers/errors: `Cache-Control: no-store`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `A7_GET_QUOTED_ETAG_OK`

  * `A7_HEAD_PARITY_OK`

  * `A7_304_OMITS_CT_CL_OK`

  * `A7_VARY_AUTH_AE_OK`

  * `A7_TRANSPORT_PROOF_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/success_get.txt`

  * `artifacts/proofs/success_head.txt`

  * `artifacts/proofs/success_304.txt`

  * `artifacts/proofs/success_writers_errors.txt`

  ### Subtask HDE-CONJ006.2 — Encoding invariance & env-gate

* **Subtask name/label:** Encoding invariance & env-gate proof

* **Subtask description:**  
   Prove encoding invariance across accepted `Accept-Encoding` values and provide env-gate proof for the Catalog route.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `A7_ENCODING_INVARIANCE_OK`

  * `A7_VARY_AUTH_AE_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/success_encoding_invariance.txt`

  * `artifacts/proofs/endpoints_env_gate_proof.log`

  ### Subtask HDE-CONJ006.3 — Caching & transport evidence indexing

* **Subtask name/label:** Reader transport Evidence Index & mirror

* **Subtask description:**  
   Update Human Index and mirror in the same PR for Reader transport proofs (success\_get/head/304, encoding\_invariance, writers\_errors, env\_gate).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ007 — CLI Tooling (showcompat, sample)

* **Task ID:** HDE-CONJ007

* **Task name/label:** CLI Tooling (showcompat, sample)

* **Task status:** **Not done**

* **Task description:**  
   Provide showcompat and sample CLI tooling with deterministic, canonical JSON outputs, diversity constraints, parity/determinism harness, and indexed artifacts.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * CLI parity/determinism harness exists as a plan; acceptance tokens not yet proven or indexed.

  ### Subtask HDE-CONJ007.1 — showcompat semantics & gating

* **Subtask name/label:** showcompat body & gating

* **Subtask description:**  
   For `showcompat`:

  * Emit a six-key LF-terminated body via shared emitter.

  * When `eligible == true` and `v1`, include exactly one `{id: "harmony", band}`.

  * Keep merge-blocking until parity/determinism tokens pass.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `PREIMAGE_RECOMPUTE_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `CLI_STDOUT_LF_OK`

  * `CLI_AB_BA_PARITY_OK`

  * `CLI_TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json`

  * `artifacts/cli/summary.json`

  ### Subtask HDE-CONJ007.2 — sample CLI semantics & diversity

* **Subtask name/label:** sample IDs, seed, & diversity

* **Subtask description:**  
   For `sample` (dev-only):

  * Return IDs-only with deterministic order.

  * Echo seed in `meta` when provided.

  * Enforce diversity window/bounds/recent constraints.

  * Exactly one LF in output.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `COMPOSITE_ABBA_IDENTITY_OK`

  * `TWO_RUN_IDENTITY_OK`

* **Evidence / artifacts:**

  * `artifacts/cli/ab.json` / `ba.json` / `summary.json` (reused)

  ### Subtask HDE-CONJ007.3 — CLI conformance & parity tokens

* **Subtask name/label:** CLI conformance & parity harness tokens

* **Subtask description:**  
   Ensure CLI conformance tokens and parity-harness tokens are satisfied:

  * CLI conformance:

    * `CLI_PYPROJECT_ENTRYPOINT_OK`

    * `CLI_MODULE_RUN_OK`

    * `CLI_INSTALL_OK`

    * `CLI_HELP_EXIT_0_OK`

    * `CLI_HELP_STDOUT_OK`

    * `CLI_STDERR_ONLY_ON_ERROR_OK`

  * Parity harness:

    * `CLI_SHOWCOMPAT_PRESENT`

    * `CLI_SHOWCOMPAT_CANON_OK`

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** (as listed above)

* **Evidence / artifacts:**

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json`

  * `artifacts/cli/summary.json`

  ### Subtask HDE-CONJ007.4 — CLI tooling evidence indexing

* **Subtask name/label:** showcompat/sample Evidence Index & mirror

* **Subtask description:**  
   Index `artifacts/cli/ab.json`, `ba.json`, and `summary.json` in Human Index and mirror (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present) in the same PR.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-CONJ008 — Writer Surfaces (API)

* **Task ID:** HDE-CONJ008

* **Task name/label:** Writer Surfaces (API)

* **Task status:** **Not done**

* **Task description:**  
   Implement writer APIs with typed numeric-free envelopes, idempotent write paths, correct headers (no-store, no ETag), canonical JSON output (if any), and indexed writer evidence, while keeping A7 tokens scoped to success routes.

* **Task notes:**

  * Writers: `Cache-Control: no-store`, never 304\.

  * Writers are not A7 proof surfaces; A7 tokens (`A7_*`, `READER_*`) remain bound to Catalog success routes.

  ### Subtask HDE-CONJ008.1 — Writer envelope & posture

* **Subtask name/label:** Typed success/error envelopes & A7 posture

* **Subtask description:**  
   Define typed success and error envelopes (numeric-free) and A7 posture:

  * Writers: `Cache-Control: no-store`, never 304\.

  * Errors: typed, numeric-free JSON with `Content-Type: application/json; charset=utf-8`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (A7 family excluded from writers)

* **Evidence / artifacts:**

  * `tests/transport/headers/no_store_writers_errors.snap`

  ### Subtask HDE-CONJ008.2 — Idempotent writer path & byte parity

* **Subtask name/label:** Idempotent write path & emitter parity

* **Subtask description:**  
   Ensure an idempotent write path:

  * Canonicalize body before persist.

  * Record `release_id`.

  * Run byte-equality checks between stored bytes and emitter output.

  * Re-issuing the same valid request leaves state unchanged and preserves response semantics.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * Write/readback byte parity logs.

  ### Subtask HDE-CONJ008.3 — Writer evidence presence & indexing

* **Subtask name/label:** Writer evidence & Index/Mirror discipline

* **Subtask description:**  
   Capture and index writer evidence artifacts (write/readback logs, DDL updates, ops logs) with Evidence Index entries and machine mirror records; `EVIDENCE_INDEX_UPDATED_OK` and related Index/Mirror tokens gate that evidence is captured and synchronized.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * Writer DDL updates & ops logs (paths not pinned)

  * Evidence Index entries for writer artifacts

  ### Subtask HDE-CONJ008.4 — A7 family excluded for writers

* **Subtask name/label:** A7 tokens scoping for writers

* **Subtask description:**  
   Ensure Governance A7 tokens (`A7_*`, `READER_*`) remain bound to Catalog JSON success routes only; writer routes are not used as A7 proof surfaces and are not directly gated by A7 tokens.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **None** (behavioral scoping; A7 tokens deliberately not applied)

* **Evidence / artifacts:**

  * Governance configuration and test plans (titles-only in PF docs).

  ---

  ## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)

* **Task ID:** HDE-CONJ009

* **Task name/label:** Global discipline (single-emitter canonical JSON & Index updates)

* **Task status:** **Not done** (tracked as ongoing global requirement)

* **Task description:**  
   Enforce single-emitter canonical JSON rules across all surfaces and require Evidence Index/Mirror updates whenever artifacts change.

* **Task notes:**

  * All surfaces honor single-emitter, canonical JSON rules:

    * UTF-8, no BOM.

    * ASCII-sorted keys.

    * Compact separators.

    * Exactly one LF.

    * Arrays-as-sets deduped and ASCII-sorted.

  * All checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

  * Index updates are mandatory:

    * Update Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and machine mirror (`artifacts/evidence_index.jsonl`) in the same PR that adds or changes artifacts (records-only canonical JSONL; one LF; unknown-key reject; path-proofs in place).

  * HDE-Schemas & Artifacts §8.6 is the single home for the entries list; PF09 does not duplicate it.

  ### Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)

* **Subtask name/label:** Canonical JSON invariants enforcement

* **Subtask description:**  
   Enforce canonical JSON invariants (encoding, key order, compactness, LF, set ordering) for all surfaces that emit JSON, using the single shared emitter.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * Canonical-compare logs across phases (various `canonical_json/*.log` and `json_canon_compare` artifacts).

  ### Subtask HDE-CONJ009.2 — Global Index/Mirror discipline

* **Subtask name/label:** Global Evidence Index & Mirror enforcement

* **Subtask description:**  
   Ensure that whenever any artifacts are added or changed, the Evidence Index and Machine Mirror are updated in the same PR, with canonical JSONL, unknown-key reject, and path-proofs in place.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

# 

# Phase V — Fermentation (Narratives & external bridges)

**Overall status.** Partial — semantics and routes are specified in canon, but none of the items in this phase are yet fully accepted as Done. All remain **Not done** until tokens pass and evidence is indexed in the Human Index and Machine Mirror.

---

## **Task FERM001 — SAFE rails & provider gate**

* **Task ID:** FERM001

* **Task name/label:** SAFE rails & provider gate

* **Task status:** Not done (Audit v1 — 2025-11-17)

* **Task description:**  
   Establish and prove SAFE rails posture and provider gating for vendor HTTP, including closed-rails refusal behavior, pinned open-rails policy (timeouts, retries, backoff, 429 handling), observability, and evidence/indexing discipline.

* **Task notes:**

  * SAFE rails tokens are **missing** and not yet wired as acceptance gates (titles-only; token semantics live in HDE-Governance):

    * `SAFE_RAILS_CLOSED_OK`

    * `SAFE_RAILS_OPEN_OK`

    * `SAFE_LOG_REDACTION_OK`

    * `SAFE_RETRY_BACKOFF_OK`

    * `SAFE_429_TYPED_REFUSAL_OK`

  * No SAFE-rails evidence has been captured yet.

  * Rails are **closed by default**; vendor HTTP is allowed only when **both** gates are open:

    * Closed rails: `SAFE_MODE = 1`, `ALLOW_NETWORK = 0`.

    * Open rails: `SAFE_MODE = 0`, `ALLOW_NETWORK = 1`.

  * Under **closed rails**:

    * Refusals are typed, numeric-free JSON bodies, LF-terminated.

    * No secrets in logs.

    * No `ETag`.

    * No `Vary` on error/ops routes.

    * No response compression on refusal.

    * Request shapes may be computed for diagnostics, but **no outbound I/O** is permitted.

  * Routing (titles-only):

    * Rails policy & token semantics: **HDE-Governance**.

    * Vendor bytes and on-wire contract: **HDE-CLI-API-Vendor-Ref**.

    * Mechanics (request shaping, SAFE rails hooks): **HDE-Mechanics Guide** (§7.1/§7.3).

---

### **Subtask FERM001.1 — SAFE rails closed posture & refusal path**

* **Subtask name/label:** Closed-rails refusal posture & log discipline

* **Subtask description:**

   Prove that under **closed rails** (`SAFE_MODE=1`, `ALLOW_NETWORK=0`):

  * **No outbound I/O:**

    * There are no sockets, DNS lookups, or HTTP calls when rails are closed, including for provider and BodyGraph flows.

  * **Typed refusal envelope:**

    * Provider-bound requests produce a typed refusal envelope (for example `PROVIDER_DISABLED`), encoded as numeric-free JSON with exactly one trailing LF.

    * Refusal responses carry no `ETag`, no `Vary` on error/ops routes, and no response compression.

  * **Keys-only log redaction:**

    * Logs for these refusal paths are keys-only, with bounded, stable fields such as:

      * Header names, route, status, duration, `idempotence_hash`, `release_id`.

    * All secret values (for example `HD-Api-Key`) are redacted (e.g. `HD-Api-Key: REDACTED`); no payload bodies are logged.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in Governance / Epics):**

  * `SAFE_RAILS_CLOSED_OK`

  * `SAFE_LOG_REDACTION_OK`

* **Evidence / artifacts (titles/paths only):**

  * `ci/jobs/rails_closed_refusal.yml` — closed-rails refusal proof harness (no outbound I/O, typed refusal envelopes, keys-only logs).

  * Rails closed-posture snapshot and refusal fixtures (titles/paths single-homed in Governance/Schemas).

---

### **Subtask FERM001.2 — SAFE rails open posture & policy (integration gate)**

* **Subtask name/label:** Open-rails policy (timeouts, retries, backoff, 429\)

* **Subtask description:**

   Define and prove the **open-rails** policy for vendor HTTP, pinning timeouts, retries, backoff, and typed 429 handling before live tests:

  * **Timeout profiles:**

    * `timeout_profile ∈ {small, default, long}` mapped to `(connect_timeout_ms, read_timeout_ms, total_timeout_ms)` from **closed integer sets**.

  * **Retries:**

    * `max_attempts ∈ {0,1,2,3}` (including the initial attempt).

    * `retryable = {network_error, 5xx}`.

    * Do **not** retry 429 or any other 4xx status in this component.

  * **Backoff:**

    * `backoff ∈ {none, fixed, exponential}` with closed integer parameters.

    * No jitter.

    * Accumulated delay must not exceed `total_timeout_ms`.

  * **Typed 429 handling:**

    * On HTTP 429, emit a typed `PROVIDER_RATE_LIMITED` error.

    * If `Retry-After` is valid (delta-seconds or HTTP-date), compute `retry_after_ms ≥ 0`.

    * On invalid/unsupported/overflow `Retry-After`, omit `retry_after_ms`.

    * 429 is **never** treated as a success path in this epic.

  * **Success behavior (open rails):**

    * Success paths emit canonical JSON envelopes governed by the vendor bytes contract (titles-only to HDE-CLI-API-Vendor-Ref).

    * Determinism and AB↔BA coherence remain satisfied under this policy (canonical JSON, single LF, two-run identity where applicable).

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in Governance / Epics):**

  * `SAFE_RAILS_OPEN_OK`

  * `SAFE_RETRY_BACKOFF_OK`

  * `SAFE_429_TYPED_REFUSAL_OK`

* **Evidence / artifacts (titles/paths only):**

  * `ci/jobs/rails_open_conformance.yml` — success / retry / 429 exercise under pinned timeout and backoff policy.

  * `artifacts/vendor/policies_pinned.md` — selected timeout/retry/backoff/429 parameters and profiles.

  * `artifacts/vendor/retry_after_parse.log` — `Retry-After` parse/normalization traces (valid vs invalid/overflow cases).

---

### **Subtask FERM001.3 — Observability & log posture (SAFE rails)**

* **Subtask name/label:** SAFE rails observability & redaction

* **Subtask description:**

   Ensure SAFE rails behavior is observable without leaking payloads or secrets:

  * **Counters/timers:**

    * Counters and timers distinguish success vs failure classes, including at least: `network_error`, `4xx`, `5xx`, `429`.

  * **Bounded labels:**

    * Labels are bounded and well-defined (for example `route`, `outcome`, `rails_state`, `timeout_profile`), avoiding high-cardinality tags.

  * **Log posture:**

    * Logs never include payload bodies or secret header values.

    * Secret-like fields are consistently redacted while preserving enough keys to diagnose rails state and outcome.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in Governance / Epics):**

  * `SAFE_LOG_REDACTION_OK`

* **Evidence / artifacts (titles/paths only):**

  * `ci/jobs/logs_keys_only_redaction.yml` — log redaction and keys-only check.

  * Observability dashboard snapshots or logs (titles/paths single-homed in Governance/Schemas) showing bounded label sets and separated outcome classes.

---

### **Subtask FERM001.4 — SAFE rails evidence & indexing**

* **Subtask name/label:** SAFE rails evidence & Evidence Index discipline

* **Subtask description:**

   For SAFE rails and provider-gate artifacts, enforce Evidence Index/Mirror discipline:

  * **Required SAFE-rails artifacts:**

    * `ci/jobs/rails_closed_refusal.yml` — closed-rails refusal proof harness.

    * `ci/jobs/rails_open_conformance.yml` — success / retry / 429 exercise.

    * `ci/jobs/logs_keys_only_redaction.yml` — log redaction check.

    * `artifacts/vendor/policies_pinned.md` — pinned timeout/retry/backoff/429 parameters.

    * `artifacts/vendor/retry_after_parse.log` — `Retry-After` parse/normalization traces.

  * **Indexing (same-PR rule):**

    * Update, in the **same PR** that adds or changes any SAFE-rails artifacts:

      * `docs/evidence/INDEX.json` (Human Index)

      * `docs/evidence/INDEX.sha256` (hash sentinel)

      * `artifacts/evidence_index.jsonl` (Machine Mirror)

    * Keep the Machine Mirror as **records-only canonical JSONL**:

      * UTF-8, no BOM.

      * ASCII-sorted keys.

      * Compact separators.

      * Exactly one trailing LF per record.

      * Unknown-key reject.

      * Fixed field order.

      * `proof_anchor` pointing to a co-located `*.path_proof.txt`.

    * Treat **HDE-Schemas & Artifacts** §8.6 as the single home for the evidence listing; Appendix C defines record types and schemas. PF09 (this subtask) does not duplicate those schemas.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in Governance / Epics):**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts (titles/paths only):**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  * SAFE-rails artifacts listed above, plus their `*.path_proof.txt` transcripts.

---

## **Task FERM002 — Narrative Selection Router (keys only)**

* **Task ID:** FERM002

* **Task name/label:** Narrative Selection Router (keys only)

* **Task status:** Not done

* **Task description:**  
   Implement and prove a deterministic **Narrative Selection Router** that operates on **keys only**, not text. For any supported input `(category, band, perspective, viewer_top, flags)`, the router must produce stable `{personal_key, shared_key}` outputs with:

  * No randomization or time-based behavior.

  * No implicit fallbacks (missing mappings return `missing_narrative_key`).

  * Strict CLI↔Reader parity via the shared presenter/emitter (same keys, same canonical JSON bytes).

* **Task notes:**

  * The router **only selects narrative keys**; it never produces narrative prose.

  * **Inputs:** `(category, band, perspective ∈ {personal, shared}, viewer_top, flags)`.

  * **Outputs:** `{personal_key, shared_key}` or typed `missing_narrative_key` values.

  * Deterministic behavior:

    * No RNG.

    * No dependence on wall-clock time or ambient environment.

    * No DB or vendor lookups in the selection path.

  * CLI and Reader both call the **same router** through the shared presenter/emitter, so keys and bytes remain aligned across surfaces.

  * Routing (titles-only):

    * Category framework & mechanics: **HDE-Mechanics Guide** (§7).

    * Banding & category semantics: **HDE-Math-Spec**.

    * Narrative Key Registry & pack identity: **FERM003** / **Narratives Guide** (titles-only).

  ---

  ### **Subtask FERM002.1 — Deterministic router implementation**

* **Subtask name/label:** Implement deterministic keys-only router

* **Subtask description:**

   Implement the router as a pure, deterministic component and wire it to all relevant surfaces:

  * **Freeze the argument schema:**

    * Define and fix the exact router input shape  
       `(category, band, perspective, viewer_top, flags)`  
       with no implicit or hidden parameters.

    * Treat this schema as part of the public behavior contract for routing; changes must go through a future epic and Doc-Delta.

  * **Deterministic selection rules:**

    * Use explicit **total-order** utilities (as in Mechanics §5) for any “top N” or tie-break logic.

    * Ensure candidate ordering is fully specified and stable (no dependence on Python dict/set iteration order, DB row order, or nondeterministic joins).

  * **No side effects / external I/O:**

    * Eliminate clocks, randomness, and external I/O from routing logic:

      * No `datetime.now()` or equivalent.

      * No calls to filesystem, network, DB, or vendor adapters in the selection path.

    * Router decisions must be a pure function of its inputs plus the pinned registry content (titles-only to FERM003).

  * **Keys-only behavior:**

    * Router returns keys from the Narrative Key Registry; it does **not** emit narrative text, snippets, or prose.

    * When a mapping is missing, router returns a typed `missing_narrative_key` indicator; no implicit fallback keys or packs.

  * **CLI/Reader integration:**

    * Wire the router into CLI and Reader via the **shared presenter/emitter** so that:

      * For identical `(category, band, perspective, viewer_top, flags)`, CLI and Reader receive the same `{personal_key, shared_key}` pair.

      * The JSON envelopes on each surface are canonical and byte-identical where PF05 defines Reader↔CLI parity.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

  * `CLI_READER_PARITY_OK` — CLI/Reader parity via shared emitter.

  * `TWO_RUN_IDENTITY_OK` — repeat runs produce identical router outputs.

  * A router-specific keys-only token (for example `NARR_ROUTER_KEYS_ONLY_OK`) may be introduced in Governance; PF09 references it by title only when minted.

* **Evidence / artifacts (titles/paths only):**

  * `tests/narratives/test_router.py` — implementation-level tests and edge cases for router behavior (no RNG, no fallbacks, missing mappings).

  * Implementation wiring evidence is captured indirectly via the parity and coverage artifacts in Subtask FERM002.2.

  ---

  ### **Subtask FERM002.2 — Router tests, parity, and evidence indexing**

* **Subtask name/label:** Router tests, coverage, and Evidence Index discipline

* **Subtask description:**

   Add tests and evidence artifacts to prove router behavior and keep all surfaces in parity, and ensure everything is indexed under the standard Evidence discipline:

  * **Unit tests & coverage:**

    * For each `(category, band, perspective)` case in the supported matrix:

      * Verify **two-run identity**: same inputs → same `{personal_key, shared_key}` on repeated runs.

      * Verify **AB↔BA coherence** where applicable (for example A–B vs B–A inputs yield the same key pairing once normalized).

    * Cover both `personal` and `shared` perspectives and explicit edge cases:

      * Known mappings.

      * Missing mappings (router returns `missing_narrative_key`, not a fallback).

  * **Acceptance behavior (titles-only):**

    * Resolver returns `{personal_key, shared_key}` or `missing_narrative_key` for each slot.

    * Outputs are **canonical JSON**:

      * UTF-8 (no BOM).

      * ASCII-sorted keys.

      * Compact separators.

      * Exactly one trailing LF.

    * Reader’s public surface remains **bands-only**; keys map to narrative content by title (via narrative packs, not in PF09).

    * CLI and Reader use the **same keys** for the same inputs (parity via shared presenter/emitter); where PF05 defines Reader↔CLI parity bytes, router JSON envelopes participate in those parity checks.

  * **Parity and coverage artifacts (titles/paths only):**

    * `audit/gates/narratives/keys_10x4.table.json` — router coverage snapshot (e.g. 10 categories × 4 bands), canonical JSON (UTF-8, sorted keys, compact, one LF); shows `{personal_key, shared_key}` and `missing_narrative_key` cases for each `(category, band, perspective)`.

    * `artifacts/narratives/router/parity_abba.log` — AB↔BA and two-run identity log for router outputs (keys-only, no prose).

    * `artifacts/narratives/router/cli_http_parity.log` — CLI=HTTP parity compare for router responses, showing byte-identical canonical JSON where parity is defined.

    * `tests/narratives/test_router.py` — unit tests and edge cases (as above).

  * **Indexing discipline (Evidence Index & Machine Mirror):**

    * In the **same PR** that introduces or changes any router artifacts:

      * Update `docs/evidence/INDEX.json` (Human Index).

      * Update `docs/evidence/INDEX.sha256` (hash sentinel).

      * Update `artifacts/evidence_index.jsonl` (Machine Mirror).

    * Ensure the Machine Mirror remains:

      * Records-only canonical JSONL (UTF-8; sorted keys; compact; exactly one LF).

      * Unknown-key rejecting with fixed field order.

      * Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

    * **HDE-Schemas & Artifacts** §8.6 and Appendix C remain the single homes for evidence listing and record types; PF09 does not restate schemas.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

  * `CLI_READER_PARITY_OK` — CLI/Reader parity proven with router outputs.

  * `TWO_RUN_IDENTITY_OK` — two-run identity for router outputs.

  * `JSON_CANONICAL_CHECK_OK` — canonical JSON checks for router artifacts.

  * `EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated for router artifacts.

  * `MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside Evidence Index.

  * `EVIDENCE_PATHS_VALIDATED_OK` — router artifact paths validated against the mirror.

* **Evidence / artifacts (titles/paths only):**

  * `audit/gates/narratives/keys_10x4.table.json`

  * `artifacts/narratives/router/parity_abba.log`

  * `artifacts/narratives/router/cli_http_parity.log`

  * `tests/narratives/test_router.py`

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`


  * 

---

## **Task FERM003 — Narrative Key Registry & Manifests**

* **Task ID:** FERM003

* **Task name/label:** Narrative Key Registry & Manifests

* **Task status:** Not done

* **Task description:**  
   Establish **versioned, diffable narrative key manifests** as the single source of truth for narrative keys, with **exactly one key per `(category, band, perspective)`**, pack identity derived from canonical manifest bytes, and Doc-Delta plus Evidence Index/Mirror discipline for every change. The registry and manifests are **keys-only**: they carry narrative identifiers and routing metadata, and **no narrative prose or text is stored in the engine**; prose lives in narrative packs/copy docs governed by the Narratives Guide (titles-only).

* **Task notes:**

  * Versioned, diffable manifests are the **single source of truth** for narrative keys.

  * There is **exactly one key** for each `(category, band, perspective)` combination; closure checks (no missing or duplicate keys) are enforced by the manifest validator and must fail CI on defects.

  * Manifests are canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF) and contain enough fields to capture `(category, band, perspective, language/variant, key)` per entry; detailed schema is single-homed in HDE-Schemas & Artifacts (titles-only).

  * Pack identity is:

    * `pack_sha = sha256(canonical manifest bytes)`, and

    * Packs are stored under `/narratives/<pack_sha>/…`.

  * Exporter and loader behavior for packs is owned by **HDE-Mechanics Guide** and the **Narratives Guide** (titles-only); PF09 does not define exporter/loader mechanics, only that manifests and identity artifacts exist, are canonical, and are indexed with Doc-Delta and Evidence Index/Mirror discipline.

  * 

---

### **Subtask FERM003.1 — Manifest shape & closure validation**

*Subtask name/label:* Manifest shape & registry closure

*Subtask description:*

Define the manifest schema and implement closure checks over the narrative key space.

**Manifest shape:**

* Manifests are canonical JSON:

  * UTF-8 (no BOM).

  * ASCII-sorted keys.

  * Compact separators.

  * Exactly one trailing LF.

* Each manifest record includes enough fields to capture:

  * category

  * band

  * perspective (e.g. personal / shared)

  * language/variant

  * key

**Closure validator:**

* Implement a validator that fails if any required `(category, band, perspective)` combination is missing or duplicated in the registry.

* Treat any gaps or duplicates as defects until resolved.

**Registry as single source of truth:**

* Ensure that all narrative key usage routes through these manifests; other components (router, packs, exporter/loader) treat the manifests as authoritative, by title only.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `JSON_CANONICAL_CHECK_OK` — canonical JSON checks for governed manifests and registry files.

* `UNKNOWN_IDS_FAIL_CLOSED_OK` — manifest builder rejects unknown or stray IDs in the registry.

* `TIEBREAK_TOTAL_ORDER_OK` — deterministic ordering applied when ties occur in the registry key space.

*Evidence / artifacts (titles/paths only):*

* `artifacts/narratives/registry/*.json` — narrative key manifests (canonical JSON; one LF) with full `(category, band, perspective, language/variant, key)` coverage.

---

### **Subtask FERM003.2 — Diffing, Doc-Delta wiring, identity, and indexing**

*Subtask name/label:* Manifests diffing, Doc-Delta, pack identity, and Evidence Index

*Subtask description:*

Add diff tooling, Doc-Delta policy, pack identity computation, and evidence/indexing discipline.

**Diff tooling:**

* Build a concise diff artifact for manifest changes:

  * Capture additions, removals, and modifications of keys across manifests.

  * Produce a compact, readable artifact for each change set.

**Doc-Delta policy:**

* Enforce that any registry change is accompanied by:

  * A `DOC-DELTA-*.md` entry, recording the change and rationale (titles-only; no payload duplication).

  * Evidence updates in the same PR.

**Pack identity:**

* Compute `pack_sha = sha256(canonical manifest bytes)` for each manifest.

* Verify that pack identity matches the manifest bytes used to build `/narratives/<pack_sha>/…`.

* Ensure ABBA / two-run identity remains unaffected by registry changes:

  * Same manifest bytes → same `pack_sha` in repeated runs.

  * Swapping inputs in compat/narrative selection flows does not change pack identity once normalized (AB↔BA).

**Evidence & diff artifacts (titles/paths only):**

* `artifacts/narratives/registry/*.json` — canonical manifests (see FERM003.1).

* `audit/gates/narratives/registry.diff.json` — compact diff of manifest changes.

* `docs/changes/DOC-DELTA-*.md` — Doc-Delta records for registry changes (titles-only; no narrative payload bytes).

**Evidence Index & Machine Mirror:**

* In the same PR that changes any registry manifest or diff:

  * Update `docs/evidence/INDEX.json` (Human Index).

  * Update `docs/evidence/INDEX.sha256` (hash sentinel).

  * Update `artifacts/evidence_index.jsonl` (Machine Mirror).

* Ensure the Machine Mirror remains:

  * Records-only canonical JSONL (UTF-8; sorted keys; compact; exactly one LF).

  * Unknown-key rejecting, with fixed field order.

  * Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

* `HDE-Schemas & Artifacts` §8.6 and Appendix C remain the single homes for listing and record types; PF09 routes to them by title only and does not restate schemas.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `DOC_DELTA_PRESENT_OK` — Doc-Delta artifacts captured for registry/manifests changes.

* `JSON_CANONICAL_CHECK_OK` — canonical JSON checks for manifests and diff artifacts.

* `AB_BA_PARITY_OK` — AB↔BA parity remains satisfied after registry changes (where applicable).

* `TWO_RUN_IDENTITY_OK` — two-run identity holds for pack identity and related proofs.

* `EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated when registry artifacts change.

* `EVIDENCE_INDEX_HASH_OK` — index hash recorded for the updated evidence set.

* `MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside the Evidence Index.

* `EVIDENCE_PATHS_VALIDATED_OK` — registry-related artifact paths validated against the Machine Mirror.

* `EVIDENCE_PATH_PROOFS_OK` — each registry-related artifact accompanied by a path proof.

* `CI_CHECK_MIRROR_SCHEMA_OK` — CI schema check for the Machine Mirror.

* `CI_CHECK_FINAL_LF_OK` — final-LF check for governed JSON/JSONL artifacts.

*Evidence / artifacts (titles/paths only):*

* `artifacts/narratives/registry/*.json`

* `audit/gates/narratives/registry.diff.json`

* `docs/changes/DOC-DELTA-*.md`

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `artifacts/evidence_index.jsonl`

---

## **Task FERM004 — Database Runtime Posture**

* **Task ID:** FERM004

* **Task name/label:** Database Runtime Posture

* **Task status:** Not done (Audit v1 — 2025-11-17)

* **Task description:**  
   Define and prove database runtime posture for the engine, including search\_path, role/grants, DDL fingerprint, dev fallback via DB bridge, bridge capability and provider parity, total-failure behavior, and evidence/indexing discipline. All DB posture scripts must use the adapter façade and route token semantics and schemas to HDE-Governance and HDE-Schemas & Artifacts.

* **Task notes:**

  * **Missing tokens** (titles-only; tokens live in HDE-Governance):

    * `DB_RUNTIME_SEARCH_PATH_OK`

    * `DB_ROLE_OK`

    * `DB_SCHEMA_FINGERPRINT_OK`

    * `DB_CONN_ENV_OK`

    * `DB_BRIDGE_FALLBACK_OK`

    * `DEV_DB_BRIDGE_FALLBACK_OK`

    * `DB_PROVIDER_PARITY_OK`

    * `DB_BRIDGE_CAPS_OK`

  * Evidence is currently empty for this phase:  
     **Evidence:** — (no posture/bridge artifacts indexed yet).

  * PF09 expresses only **which tokens gate DB posture** for this phase; token semantics and artifact schemas live in **HDE-Governance** and **HDE-Schemas & Artifacts** (titles-only).

---

### Subtask FERM004.1 — Adapter façade, runtime search\_path, and structural posture

*Subtask name/label:* Adapter façade, search\_path, and structural posture

*Subtask description:*

Define and prove the core runtime DB posture, using the provider-agnostic adapter façade, including search\_path, grants, DDL fingerprint, constraints, and boundary view posture:

* **Adapter façade only**

  * All DB posture and evidence scripts **MUST** call the **DBAccess façade** (provider-agnostic adapter), never raw driver clients, to guarantee parity across TCP and HTTPS providers.

* **Runtime search\_path**

  * Prove that the runtime `search_path` is exactly `hde, public` (unquoted, in that order) for the engine’s DB role.

  * Capture a `check_schema` artifact demonstrating the runtime search\_path and visible namespaces at the moment posture is captured.

* **Least-privilege grants**

  * Capture a grants snapshot for the runtime role.

  * Verify there are **no extraneous DML/DDL privileges** beyond what the engine requires to serve public workloads.

* **DDL fingerprint and constraints**

  * Capture normalized DDL for the relevant schemas in a stable order and compute a SHA-256 fingerprint; store the result as a governed artifact.

  * Capture a constraints snapshot, including FK, uniqueness, and any invariants called out in epic/spec documents.

  * Treat any unexpected change in the DDL fingerprint or constraints snapshot as a posture change that must be tracked via Governance and Schemas by title.

* **Boundary view posture**

  * Capture a dedicated proof that the boundary view used by engine/CLI for public reads is **read-only** and does not permit writes outside the HDE schema.

  * The boundary-view proof path and schema remain single-homed in **HDE-Schemas & Artifacts**; PF09 only requires that the proof artifact exists and is kept in sync with runtime posture.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `DB_RUNTIME_SEARCH_PATH_OK`

* `DB_ROLE_OK`

* `DB_SCHEMA_FINGERPRINT_OK`

*Evidence / artifacts (titles/paths only):*

* `artifacts/db/check_schema.txt` — runtime search\_path and visible schemas snapshot.

* `artifacts/db/grants.txt` — grants snapshot for the runtime role (least-privilege proof).

* `artifacts/db/ddl_fingerprint.json` — normalized DDL fingerprint (includes SHA-256 and any supporting metadata).

* `artifacts/db/check_constraints.txt` — constraints snapshot (FK, uniqueness, and invariants referenced from canon).

* `boundary_view.readonly.proof` — boundary view read-only posture proof.

---

### **Subtask FERM004.2 — Dev fallback & bridge capability / provider parity**

* **Subtask name/label:** Dev fallback, bridge caps, and provider parity

* **Subtask description:**

   Implement dev fallback behavior via the DB bridge and prove bridge capability and provider parity:

  * **Dev fallback (adapter):**

    * In `APP_ENV=dev`, when `DATABASE_URL` is present but **unusable**, fallback to `DB_BRIDGE_URL` (HTTPS) via the adapter façade.

    * Record all attempts and the **selected source** in a resolver snapshot:

      * Attempts (e.g. `database_url_attempt`, `db_bridge_url_attempt`).

      * Result (`success` / `failure`).

      * Final selected provider.

  * **Bridge capability:**

    * Snapshot bridge capabilities (endpoints and grants) via the adapter façade.

  * **Provider parity:**

    * Demonstrate that queries against the bridge produce results **identical** to direct DB access on a canonical corpus.

    * Use a normalized output format for comparison and store parity results under governed paths.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

  * `DEV_DB_BRIDGE_FALLBACK_OK`

  * `DB_BRIDGE_CAPS_OK`

  * `DB_PROVIDER_PARITY_OK`

* **Evidence / artifacts (titles/paths only):**

  * `artifacts/runtime/env_connectivity.snapshot.json` — dev resolver snapshot (attempts/result/selected provider).

  * `artifacts/db_bridge/adapter_selection.snapshot.json` — adapter selection details for DB vs bridge.

  * `artifacts/db_bridge/caps.snapshot.json` — bridge capabilities (endpoints/grants).

  * `artifacts/db/provider_parity/*.json` — normalized provider parity results (bridge vs direct DB on canonical corpus).

---

### **Subtask FERM004.3 — Non-dev total failure behavior and typed errors**

* **Subtask name/label:** Non-dev presence-order selection & failure posture

* **Subtask description:**

   Define and prove non-dev selection and failure behavior without proactive probes:

  * **Presence-order selection (non-dev):**

    * In non-dev environments, use **presence-order** selection for connectivity:

      * If `DATABASE_URL` is valid, use it.

      * Else, if `DB_BRIDGE_URL` is valid, use it.

      * Else, emit a typed error.

  * **No proactive probes:**

    * Do **not** run proactive probes beyond what the adapter uses to fulfill a request; do not perform speculative or background connectivity checks.

  * **Deterministic, numeric-free error on total failure:**

    * On total failure (no usable provider), emit a deterministic, numeric-free error envelope describing the failure state.

    * Error payloads must remain numeric-free in user-visible text; traceability goes through IDs and logs, not numeric error codes in public envelopes.

* **Subtask status:** Not started

* **Epic or card:** Unknown

* **Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

  * `DB_CONN_ENV_OK`

  * `DB_BRIDGE_FALLBACK_OK`

* **Evidence / artifacts (titles/paths only):**

  * `artifacts/runtime/env_connectivity.snapshot.json` — presence-order behavior and total-failure traces.

  * `artifacts/db/provider_parity/*.json` — may be reused to show correct selection when connections succeed.

---

### Subtask FERM004.4 — DB posture acceptance, capture discipline, and Evidence Index/Mirror

*Subtask name/label:* DB posture gating, capture discipline, and evidence indexing

*Subtask description:*

Wire DB posture acceptance tokens for this phase and enforce a single capture/indexing discipline over all DB posture and bridge artifacts:

* **DB posture & durability tokens** (titles-only; semantics live in HDE-Governance):

  * `DB_RUNTIME_SEARCH_PATH_OK`

  * `DB_ROLE_OK`

  * `DB_SCHEMA_FINGERPRINT_OK`

* **Connectivity & error tokens:**

  * `DB_CONN_ENV_OK` — presence-order behavior and typed, numeric-free error on total failure.

* **Bridge & fallback tokens:**

  * `DB_BRIDGE_FALLBACK_OK`

  * `DEV_DB_BRIDGE_FALLBACK_OK`

  * `DB_PROVIDER_PARITY_OK`

  * `DB_BRIDGE_CAPS_OK`

* **Index/mirror/path-proofs tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Posture capture discipline (must):**

  * Run all governed DB posture captures (including DDL, constraints, boundary view, connectivity, and parity) under deterministic env pins:

    * `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

  * Produce canonical JSON or LF-terminated text for all governed artifacts:

    * UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF.

  * Keep all posture artifacts and logs **secret-free**:

    * No credentials, connection strings, or sensitive payload bodies; logs are keys-only.

* **Evidence Index & Machine Mirror discipline:**

  * Whenever any DB posture or bridge artifact changes, update in the **same PR**:

    * `docs/evidence/INDEX.json` (Human Index).

    * `docs/evidence/INDEX.sha256` (hash sentinel).

    * `artifacts/evidence_index.jsonl` (Machine Mirror).

  * Machine Mirror requirements:

    * Records-only canonical JSONL (UTF-8, sorted keys, compact, exactly one LF).

    * Unknown-key reject; a **single** mirror file.

    * Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

  * PF09 does **not** define mirror schema or token semantics; it routes to **HDE-Schemas & Artifacts** and **HDE-Governance** by title.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* As listed above; PF09 references them by title only.

*Evidence / artifacts (titles/paths only):*

* Core DB posture artifacts:

  * `artifacts/db/check_schema.txt`

  * `artifacts/db/grants.txt`

  * `artifacts/db/ddl_fingerprint.json`

  * `artifacts/db/check_constraints.txt`

  * `boundary_view.readonly.proof`

* Bridge & connectivity artifacts:

  * `artifacts/runtime/env_connectivity.snapshot.json`

  * `artifacts/db_bridge/adapter_selection.snapshot.json`

  * `artifacts/db_bridge/caps.snapshot.json`

  * `artifacts/db/provider_parity/*.json`

* Index artifacts:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## **Task FERM005 — CLI Aux preview story (admin surface & evidence)**

*Task ID:* FERM005

*Task name/label:* CLI Aux preview story (admin surface & evidence)

*Task status:* Done (history-locked via EPIC-010 / EPIC-017)

*Task description:*  
 Track and validate the CLI Aux preview “story” end-to-end: an admin preview surface that uses the shared presenter/emitter, emits narrative text on stdout plus a minimal IDs-only JSON sidecar, and is captured as governed evidence (indexed and mirrored). This task records that the CLI Aux story has been implemented and proven via EPIC-010 and EPIC-017 QA runs.

*Task notes:*

* EPIC-010 established the CLI preview posture and indexing for Aux narratives via `artifacts/cli/narrative/stdout.txt` and `artifacts/cli/narrative/sidecar.json`; that work is history-locked as Done.

* EPIC-017 QA06/QA07 added QA evidence that, in Codespaces CLI, `hdctl aux-preview` can:

  * Generate a valid Aux narrative from compat JSON (public text: non-empty, numeric-free, present-tense, no HD jargon or fate/destiny language).

  * Produce a minimal admin JSON selector with `composition_id`, `pack_sha`, `pair` IDs, and `release_id`, traceable back to compat and the pinned narratives pack.

---

### **Subtask FERM005.1 — CLI Aux preview posture (enabled, indexed, and evidenced)**

*Subtask name/label:* CLI Aux preview posture (Enabled and Indexed)

*Subtask description:*

Prove that the CLI admin preview surface for Aux narratives is wired, uses the shared presenter/emitter, and is captured under the Evidence Index discipline.

**Preview posture:**

* Admin preview is enabled for allowed operators and uses the **same presenter/emitter** as Reader.

* Preview output on stdout is LF-terminated text with **no ANSI escapes**.

* Narrative IDs and bands are exposed only via an **IDs-only canonical JSON sidecar**.

**Narrative artifacts:**

* `artifacts/cli/narrative/stdout.txt`

  * LF-terminated Aux preview text for the CLI admin surface (no ANSI).

* `artifacts/cli/narrative/sidecar.json`

  * IDs-only canonical JSON sidecar for the same preview (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one LF).

  * Contains only selectors (for example `composition_id`, `key`, `pack_sha`, `pair` IDs, `release_id`); no narrative prose.

These artifacts must be listed in the **Human Evidence Index** and mirrored in the **Machine Mirror** in the same PR.

**Preview indexing posture and QA story:**

* CI gates on `CLI_PREVIEW_ENABLED_OK` and `CLI_PREVIEW_INDEXED_OK` confirm that:

  * The preview surface exists and is wired to the shared presenter/emitter.

  * Preview artifacts are captured under the Evidence Index discipline.

* EPIC-010 acceptance (history-locked):

  * `artifacts/cli/narrative/stdout.txt` and `sidecar.json` exist and are indexed.

* EPIC-017 QA06 Aux narrative evidence (CLI QA environment):

  * `Audit/QA/HDE-EPIC017/logs/step_aux_preview1.txt` — narrative text produced by:

    * `hdctl aux-preview --show-narrative` against compat JSON from `showcompat --source vendor` for a synthetic birth pair.

    * Contains a short, coherent, numeric-free, present-tense narrative with no Human Design jargon and no fate/destiny language, matching Aux public copy canon.

* EPIC-017 QA07 Aux admin JSON sidecar evidence (CLI QA environment):

  * `Audit/QA/HDE-EPIC017/logs/step_aux_preview1_admin.json` — Aux admin JSON sidecar produced by:

    * `hdctl aux-preview --admin-out` for the same compat JSON.

    * Contains at minimum:

      * `composition_id` / `key` of the form `<category>.<band>.<perspective>.<slot>` (for example `heat.open.shared.1`).

      * `pack_sha` as a 64-character lowercase hex digest for the narratives pack.

      * `pair.{a_person_uid,b_person_uid}` matching the compat JSON `person_uid`s.

      * `release_id` as an all-zero 64-hex string consistent with CLI/local identity.

    * Confirms Aux selects compositions from a pinned narratives pack in a traceable, compat-aligned way.

*For acceptance under this subtask, it is sufficient that:*

* A governed admin preview surface exists and is wired to the shared presenter/emitter.

* A preview narrative artifact exists and is indexed (`artifacts/cli/narrative/stdout.txt` and `sidecar.json` for EPIC-010).

* At least one QA run (such as EPIC-017 QA06/QA07) demonstrates that, from CLI compat JSON, Aux can generate both:

  * Public narrative text that respects the public covenant (no numerics in text; no HD jargon; appropriate tone).

  * A minimal admin JSON selector (`composition_id`/`key`, `pack_sha`, `pair` IDs, `release_id`) consistent with compat and the pinned narratives pack.

Deeper determinism checks for Aux (e.g. AB↔BA and two-run identity for admin JSON and narrative text, multi-pack routing invariants) remain scoped to other tasks and future QA phases; this Fermentation subtask records preview posture, evidence presence, basic tonality compliance, and minimal admin JSON sidecar correctness.

*Subtask status:* Done (EPIC-010 / EPIC-017)

*Epic or card:*

* EPIC-010 — Aux narratives and CLI preview (history-locked)

* EPIC-017 — Aux narrative QA (QA06/QA07)

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `CLI_PREVIEW_ENABLED_OK` — CLI Aux preview surface exists and is wired.

* `CLI_PREVIEW_INDEXED_OK` — preview artifacts captured under Evidence Index.

* `JSON_CANONICAL_CHECK_OK` — canonical JSON checks for the preview sidecar and mirror records.

* `EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated when preview artifacts change.

* `MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside the Evidence Index.

* `EVIDENCE_PATHS_VALIDATED_OK` — preview artifact paths validated against the Machine Mirror.

*Evidence / artifacts (titles/paths only):*

* `artifacts/cli/narrative/stdout.txt` — canonical LF-terminated Aux preview text for the CLI admin surface.

* `artifacts/cli/narrative/sidecar.json` — IDs-only canonical JSON sidecar for the same preview.

* `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` — Human Evidence Index entries and hash sentinel for CLI preview artifacts.

* `artifacts/evidence_index.jsonl` — Machine Mirror records for CLI preview artifacts, with `proof_anchor` references to path-proof transcripts.

* `Audit/QA/HDE-EPIC017/logs/step_aux_preview1.txt` — EPIC-017 QA06 Aux narrative evidence.

* `Audit/QA/HDE-EPIC017/logs/step_aux_preview1_admin.json` — EPIC-017 QA07 Aux admin JSON sidecar evidence.

# 

# 

# 

# **Phase VI — Distillation (Evidence & performance)** 

* **Phase description:**  
   Integrate gate scripts and evidence harnesses, pack/manifest identity, environment snapshot & observability, and performance/load harnesses to prove determinism, A7 transport posture, rails/DB/BodyGraph mechanics, and evidence-index discipline under canonical JSON.

* **Phase master status:** **Not done**

* **Notes:**

  * Harness and gates are specified in canon and PF09, but pack/manifest, environment snapshot, and the integrated evidence harness remain pending.

---

## Task HDE-DIST001 — Gate scripts & evidence harness

* **Task ID:** HDE-DIST001

* **Task name/label:** Gate scripts & evidence harness

* **Task status:** **Not done**

* **Task description:**  
   Provide one-button runners that exercise all critical mechanics (determinism, A7, rails, DB posture, BodyGraph) and produce the full set of binary evidence artifacts in a deterministic, repeatable way, with Index/Mirror discipline.

* **Task notes:**

  * This task ties together multiple acceptance dimensions (determinism, transport, rails policy, DB and BodyGraph posture) and a large evidence surface.

  * PF09 is consumer-only for tokens; semantics live in Governance/CLI/Schemas/Mechanics.

### Subtask HDE-DIST001.1 — Determinism gates

* **Subtask name/label:** Determinism & parity gates

* **Subtask description:**  
   Implement deterministic gates that:

  * **Preimage recompute:** Strip `idempotence_hash`, re-serialize the five-key preimage as canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped & ASCII-sorted; `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and compute `sha256(preimage_bytes)`; result must equal the published `idempotence_hash`.

  * **Reader↔CLI parity:** For a fixed corpus of pairs, run Reader and CLI on the same inputs and byte-compare JSON envelopes; outputs must be identical (single emitter, canonical JSON).

  * **AB↔BA & two-run identity:** For each Integration pair (e.g., `20–34` vs `34–20`, `20–57` vs `57–20`), show AB/BA narrative & banding coherence and two-run byte identity.

  * **Canonical JSON compare:** Re-emit a sample of envelopes and verify they are canonical JSON and match their canonical re-serialization.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `PREIMAGE_RECOMPUTE_OK`

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_AB_BA_PARITY_OK`

  * `TWO_RUN_IDENTITY_OK`

  * `JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

* **Determinism / parity:**

  * **`audit/gates/parity/reader_cli/ab.json`**

  * **`audit/gates/parity/reader_cli/ba.json`**

  * **`audit/gates/parity/reader_cli/summary.json`**

  * **`audit/gates/determinism/abba.bytes`**

  * **`audit/gates/determinism/tworun_identity.sha256`**

  * **`audit/gates/canonical_json/json_canon_compare.log`**

* **Two-run marker:**

  * **`artifacts/cards/A3/IDENTITY_OK.txt` — marker card indicating that two-run identity checks have passed for the release corpus.**  
* **Notes:**

  * All runs must obey `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### Subtask HDE-DIST001.2 — A7 transport gates on Catalog route

* **Subtask name/label:** A7 & Catalog transport proofs

* **Subtask description:**  
   On a **Catalog JSON success route**, prove the full A7 matrix and catalog posture:

  * 200 success with:

    * `Content-Type: application/json; charset=utf-8`

    * Strong, quoted ETag over the LF-terminated body.

    * `Cache-Control: private, max-age=0, must-revalidate`.

    * `Vary: Authorization, Accept-Encoding`.

  * HEAD: status 200; no body; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

  * 304: only after a successful 200; no body; omit `Content-Type` and `Content-Length`; validators mirror cached 200\.

  * POST: non-conditional; never returns 304\.

  * Writers/errors: `Cache-Control: no-store`; no `ETag` on error responses; errors use `Content-Type: application/json; charset=utf-8`.

  * Encoding invariance: for a fixed canonical LF-terminated body, ETag and effective `Content-Length` are stable across `identity/gzip/br`.

  * Env-gating proof: non-prod Catalog entries are unreachable with `APP_ENV=prod`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `A7_GET_QUOTED_ETAG_OK`

  * `A7_HEAD_PARITY_OK`

  * `A7_304_OMITS_CT_CL_OK`

  * `A7_VARY_AUTH_AE_OK`

  * `A7_ENCODING_INVARIANCE_OK`

  * `A7_TRANSPORT_PROOF_OK`

  * `ENDPOINTS_CATALOG_OK`

  * `ENDPOINTS_CATALOG_ENV_GATE_OK`

* **Evidence / artifacts:**

  * Transport (Catalog route):

    * `artifacts/reader/endpoints_snapshot.json`

    * `artifacts/proofs/success_get.txt`

    * `artifacts/proofs/success_head.txt`

    * `artifacts/proofs/success_304.txt`

    * `artifacts/proofs/success_writers_errors.txt`

    * `artifacts/proofs/encoding_invariance.txt`

    * `artifacts/proofs/endpoints_env_gate_proof.log`

  * Aux headers-only checks (EPIC-010):

    * `tests/transport/headers/aux_text_200.snap`

    * `tests/transport/headers/aux_suppression_200.snap`

* **Notes:**

  * A7 proofs must be captured on a Catalog JSON success route; `/internal/version` is excluded.

### 

### **Subtask HDE-DIST001.3 — CI rails closed/open policy & rails gates**

* **Subtask name/label:** CI rails closed/open policy & rails gates

* **Subtask description:**  
   Enforce SAFE rails posture for all CI and dev harness runs, with explicit closed/open gates, governed retry/backoff behavior, and typed, numeric-free refusals:

  * **Rails CLOSED by default.**

    * Run CI pipelines with rails CLOSED by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).

    * Under closed rails, vendor and external HTTP calls are not permitted; any attempt to reach a provider must return a typed, numeric-free refusal envelope instead of performing outbound I/O.

  * **Retry/backoff family (open rails only).**

    * For any job that opens rails (for example, live vendor or bridge checks), use a policy-pinned retry/backoff family drawn from a closed set `{none, fixed, exponential}` with integer parameters; no jitter is allowed.

    * Retryable conditions are restricted to `{network_error, 5xx}`; other 4xx responses (beyond the typed 429 behavior below) MUST NOT be retried in this component.

  * **Closed rails gate.**

    * Prove there is **no outbound network I/O** under closed rails, including BodyGraph/vendor flows.

    * Show that refusal envelopes are typed, numeric-free JSON and that logs are keys-only (no payload bodies, header values, or secrets).

    * Capture a rails posture sanity check log and at least one refusal fixture under closed rails; both artifacts are governed and indexed under the Evidence Index discipline (PF09 does not define their schemas or exact paths; those live in HDE-Governance and HDE-Schemas & Artifacts).

  * **Open rails gate (pinned).**

    * Show that retry/backoff behavior matches the pinned profile (family and parameters) and respects the retryable-condition rules above.

    * Show that `429` responses produce a typed `PROVIDER_RATE_LIMITED` error with `retry_after_ms` only when a valid `Retry-After` header is present; there is no auto-success path in this epic.

    * Demonstrate that determinism and AB↔BA parity remain intact under open-rails runs (canonical JSON, single LF).

* PF09 does not redefine SAFE-rails token semantics or transport matrices; those remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref. This subtask requires that the rails harnesses (closed and open), refusal fixtures, and logs exist and are indexed, and that they prove the SAFE-rails and retry/backoff behavior described above.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `ENV_RAILS_POLICY_OK`

  * `ENV_LC_ALL_C_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * Rails CI jobs (titles-only):

    * `ci/jobs/rails_closed_refusal.yml` — closed-rails refusal and posture sanity.

    * `ci/jobs/rails_open_conformance.yml` — open-rails retry/backoff and 429 conformance.

    * `ci/jobs/logs_keys_only_redaction.yml` — keys-only logging and redaction checks.

  * Rails posture log and refusal fixture for closed rails (titles/paths owned by HDE-Governance and HDE-Schemas & Artifacts).

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

### 

### **Subtask HDE-DIST001.4 — DB posture & runtime checks (harness for FERM004)**

*Subtask name/label:* DB posture & runtime checks (FERM004 harness)

*Subtask description:*

Use the Distillation harness to **prove and exercise** the DB runtime posture defined in **Task FERM004 — Database Runtime Posture** for this phase, without redefining posture semantics:

* **Semantic home**

  * DB runtime posture semantics (adapter façade, search\_path, grants, DDL fingerprint, constraints, boundary view posture, bridge fallback, provider parity, and total-failure behavior) are owned by **FERM004** in Phase V — Fermentation.

  * This subtask adopts those semantics and focuses on **where** they are proved in the Distillation harness, not on re-specifying behavior.

* **Posture artifacts to capture in this harness**

  * Produce and index the same governed DB posture artifacts required by FERM004, at minimum:

    * `artifacts/db/ddl_fingerprint.json` — normalized DDL snapshot of the runtime schema with stable ordering.

    * `artifacts/db/grants.txt` — baseline roles/grants listing.

    * `artifacts/db/check_schema.txt` — schema/search\_path echo and verification.

    * `artifacts/db/check_constraints.txt` — constraint checks (including FK, uniqueness, and invariants called out in epic/spec docs).

    * `boundary_view.readonly.proof` — boundary view read-only proof (path and schema owned by HDE-Schemas & Artifacts).

    * `artifacts/runtime/env_connectivity.snapshot.json` — names-only snapshot of how DB connectivity was resolved (dev-only), with schema owned by HDE-Schemas & Artifacts.

  * When possible, reuse the same scripts and adapter façade entrypoints used for FERM004 posture captures so that evidence remains consistent across phases.

* **Capture discipline (aligned with FERM004.4)**

  * Run posture captures under deterministic env pins:

    * `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

  * Ensure all governed artifacts are canonical JSON or LF-terminated text:

    * UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF.

  * Keep posture artifacts and logs **secret-free** (no credentials or connection strings; logs are keys-only).

* **Evidence Index & Mirror**

  * When this harness adds or updates any DB posture artifacts:

    * Update `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` in the same PR.

    * Update `artifacts/evidence_index.jsonl` under the global Machine Mirror rules (records-only canonical JSONL, unknown-key reject, single file, `proof_anchor` present for each artifact).

  * PF09 does not define mirror schema or token semantics; it routes to **HDE-Schemas & Artifacts** and **HDE-Governance** by title.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (if verified here; titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

* `DB_RUNTIME_SEARCH_PATH_OK`

* `DB_ROLE_OK`

* `DB_SCHEMA_FINGERPRINT_OK`

* `DB_CONN_ENV_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts (titles/paths only):*

* `artifacts/db/ddl_fingerprint.json`

* `artifacts/db/grants.txt`

* `artifacts/db/check_schema.txt`

* `artifacts/db/check_constraints.txt`

* `boundary_view.readonly.proof`

* `artifacts/runtime/env_connectivity.snapshot.json`

* `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

* `artifacts/evidence_index.jsonl`

### Subtask HDE-DIST001.5 — BodyGraph mechanics gates

* **Subtask name/label:** BodyGraph source & policy proofs  
* **Subtask description:**  
   When verified here, prove BodyGraph behavior:  
  * Source selection and invariance across AB/BA.  
  * Vendor calls disabled in prod as required.  
  * TTL / stale-while-revalidate policy is pinned.  
  * Rate-limit and circuit-breaker policies behave as specified.  
  * **Refresh worker & POLICY alignment (titles-only).** The BodyGraph refresh worker (`scripts/bodygraph/run_refresh_worker.py`) is the dev-only job that drives the TTL/SWR, rate-limit, and circuit-breaker behavior captured in `artifacts/bodygraph/refresh_policy.snapshot.json` and related metrics/logs. PF14 and the ADRs define a v1 nested schema for this snapshot (including `ttl_s`/`swr_s`, nested `rate_limit{requests_per_window,window_s}`, nested `circuit_breaker{fail_threshold,window_s,cooldown_s}`, and a `sample_counts` block with counters such as `refresh_failures`, `breaker_tripped`, and `rate_limit_hits`). This subtask records that the refresh worker’s internal `POLICY` constant and behavior remain in lock-step with that v1 schema and the ADR/snapshot owned by HDE-Build Notes and HDE-Schemas & Artifacts; PF09 does not restate the schema or numeric values here, it only requires that the governed snapshot and associated metrics/logs exist and reflect the policy those documents describe.  
* **Subtask status:** **Not started**  
* **Epic or card:** **Unknown**  
* **Tokens (if verified here):**  
  * `BG_SOURCE_SELECTION_OK`  
  * `DEV_DB_BRIDGE_FALLBACK_OK`  
  * `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`  
  * `BG_SOURCE_INVARIANCE_OK`  
  * `BG_TTL_SWR_POLICY_OK`  
  * `BG_RATE_LIMIT_POLICY_OK`  
  * `BG_CIRCUIT_BREAKER_POLICY_OK`

* **Evidence / artifacts:**

  * BodyGraph proofs:

    * `artifacts/bodygraph/source_selection.snapshot.json`

    * `artifacts/bodygraph/source_invariance/ab.json`

    * `artifacts/bodygraph/source_invariance/ba.json`

    * `artifacts/bodygraph/source_invariance/summary.json`

    * `artifacts/bodygraph/refresh_policy.snapshot.json`

    * `artifacts/bodygraph/metrics.snapshot.json`

    * `artifacts/bodygraph/keys_only.logs.sample`

### Subtask HDE-DIST001.6 — One-button evidence harness & release sanity pipeline

* **Subtask name/label:** One-button evidence harness & release sanity pipeline

* **Subtask description:**  
   Implement a one-button runner that executes the release & provenance sanity pipeline end-to-end and fails closed on any drift:

  * **Ordered steps (minimum sequence).**

    * Format (code/docs).

    * Lint / type checks.

    * Unit \+ property tests (determinism, comparators).

    * Schema validation (domains and payloads as applicable).

    * Goldens (AB↔BA, two-run identity, band edges, canonical-compare).

    * Capture artifacts for **this release**, including at least:

      * Pack identity artifacts (`artifacts/math/freeze_pack_manifest.json`, `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`).

      * Reader transport proofs (A7) on a Catalog JSON success route (see A7 tasks and Endpoint Catalog).

      * Internal-ops `/internal/version` headers/body proofs (see HDE-SEPA004 and runtime packaging tasks).

      * DB posture artifacts (see DB posture subtasks).

      * BodyGraph source/policy proofs (see BodyGraph mechanics subtasks).

    * Index \+ Mirror parity check: update `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in the same commit/PR, then verify:

      * 1:1 join between titles/paths and mirror records.

      * Canonical JSONL (UTF-8; sorted keys; compact; one LF).

      * Path-proofs present and referenced by `proof_anchor`.

  * **Transcript & discipline.**

    * Emit `artifacts/proofs/sanity_pipeline.transcript.log` capturing ordered steps and pass/fail status.

    * Run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; keep all evidence artifacts canonical and secret-free.

* PF09 does not redefine token semantics for determinism, A7, `/internal/version`, DB posture, or BodyGraph behavior; those remain single-homed in HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Schemas & Artifacts, and Mechanics. This subtask requires that the one-button runner drive all governed gates for a release and enforce Index/Mirror parity for the resulting artifacts.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/sanity_pipeline.transcript.log`

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ### **Subtask HDE-DIST001.7 — Vendor ingest source policy & proofs**

* Subtask name/label: Vendor ingest source policy & proofs

* Subtask description:  
   Prove that the BodyGraph vendor ingest pipeline obeys the environment-aware source policy and source invariance rules from Mechanics, using governed evidence and rails gates:

  * Env-aware policy (prod vs dev).

    * In prod, the database is the source of truth; vendor APIs are never called inline on the hot request path.

    * In dev, direct vendor calls are allowed, but on success the ingest MUST upsert the BodyGraph into the DB so subsequent reads are repeatable.

  * Per-call source selection (no modes).

    * Source is chosen per call on operator surfaces (for example via CLI flag or ops parameter); there are no hidden “engine modes” that silently flip between DB and vendor.

    * For BodyGraph flows, capture artifacts/bodygraph/source\_selection.snapshot.json as canonical JSON (titles-only to HDE-Schemas & Artifacts for schema) with at least attempted and selected source information; gate via BG\_SOURCE\_SELECTION\_OK.

  * Unknown ENGINE\_\* env fail-closed.

    * Any unknown ENGINE\_\* environment variable that would affect source selection MUST fail fast with a typed error and MUST NOT perform vendor I/O.

    * Demonstrate this behavior under the rails harness (closed rails by default) and capture keys-only logs; semantics for refusal envelopes and rails posture are governed by HDE-Governance (titles-only).

  * Rails-closed vendor behavior.

    * When rails are closed, any request that sets source=vendor MUST return a typed refusal and MUST NOT issue outbound HTTP to the vendor.

    * This requirement is enforced in conjunction with the CI rails gates (ENV\_RAILS\_POLICY\_OK) and BodyGraph source selection tests.

  * Source invariance (DB vs vendor).

    * For the same normalized inputs, show that DB-sourced and vendor-sourced bodies are byte-identical when emitted via the shared presenter/emitter.

    * Use the BodyGraph invariance artifacts under artifacts/bodygraph/source\_invariance/ (ab.json, ba.json, summary.json) and prove ab\_ba\_equal: true in the summary.

* Subtask status: Partial

* Epic or card: EPIC-017 (QA08 vendor dry-run resolve) for the vendor dry-run slice; future epic (TBD) for full source policy/invariance closure

* Tokens:

  * BG\_SOURCE\_SELECTION\_OK

  * BG\_VENDOR\_CALLS\_DISABLED\_IN\_PROD\_OK

  * BG\_DEV\_DIRECT\_CALLS\_UPSERT\_OK

  * BG\_SOURCE\_INVARIANCE\_OK

  * ENV\_RAILS\_POLICY\_OK

  * EVIDENCE\_INDEX\_UPDATED\_OK

  * EVIDENCE\_INDEX\_MIRROR\_OK

* Evidence / artifacts:

  * artifacts/bodygraph/source\_selection.snapshot.json — canonical JSON snapshot of attempted and selected sources for BodyGraph flows (schema and details routed to HDE-Schemas & Artifacts).

  * artifacts/bodygraph/source\_invariance/ab.json — DB vs vendor AB BodyGraph invariance sample.

  * artifacts/bodygraph/source\_invariance/ba.json — DB vs vendor BA BodyGraph invariance sample.

  * artifacts/bodygraph/source\_invariance/summary.json — summary proving ab\_ba\_equal: true for DB/vender invariance when implemented.

  * Rails/CI logs demonstrating closed-rails refusal and no outbound vendor I/O (paths not pinned here; governed by HDE-Governance and Glow QA Guide).

  * docs/evidence/INDEX.json / docs/evidence/INDEX.sha256 — Human Evidence Index and hash sentinel including the above artifacts.

  * artifacts/evidence\_index.jsonl — Machine Mirror entries and path-proofs for the above artifacts.

  * EPIC017 QA08 vendor dry-run evidence (CLI QA environment):

    * Audit/QA/HDE-EPIC017/logs/step\_bg\_resolve\_vendor\_dry\_run1.txt — resolver+ingest metadata JSON for hdctl bg:resolve \--source vendor \--dry-run on a synthetic birth tuple, showing:

      * requested\_source and resolved\_source both "vendor", allow\_network: true, safe\_mode: false, dry\_run: true, upsert: false, user\_id "qa\_epic017\_vendor1";

      * ingest with provider "hdapi", vendor\_version: 1, non-zero duration\_ms, rows\_written: 0, db\_rows\_after: 0;

      * matching input\_fingerprint, payload\_sha256, db\_emitted\_sha256, parity\_match: true;

      * a composite idempotency\_key combining UUID, provider, version, and fingerprint; and status: "ok".

* Notes:

  * EPIC017 QA08 demonstrates that, in the Codespaces → Railway QA posture, vendor ingest can be exercised via hdctl bg:resolve \--source vendor \--dry-run for a synthetic birth tuple and QA user key, with open rails explicitly enabled (SAFE\_MODE=0, ALLOW\_NETWORK=1), no DB writes (rows\_written: 0, db\_rows\_after: 0), and parity\_match: true between vendor payload and would-be DB shape. This satisfies the “vendor dry-run resolve” slice of this subtask and confirms that the vendor path and ingest bridge behave as expected in dry-run mode without mutating the DB.

  * This subtask remains Partial because the broader vendor ingest source policy is not fully proven yet: prod rails-closed refusal semantics, unknown ENGINE\_\* fail-closed behavior, full BG\_SOURCE\_SELECTION\_OK coverage, and DB vs vendor source invariance using the artifacts/bodygraph/source\_invariance/\*\* family still require implementation and evidence. Those aspects are reserved for future epics and will be reflected here by promoting this subtask to Done once the remaining tokens and artifacts are in place and indexed.

### **Subtask HDE-DIST001.8 — Partition plan & verify (EPIC-011)**

* **Subtask name/label:** Partition plan & verify (EPIC-011)

* **Subtask description:**  
   Enforce EPIC-011’s non-deferred partition stance by producing and indexing partition plan and verification artifacts under governed paths:

  * `artifacts/db/partition/partition_plan.txt` — planned partition layout for HDE tables in scope.

  * `artifacts/db/partition/partition_verify.log` — verification output showing that the live DB matches the plan.

* For EPIC-011 there is no “defer partition” behavior for these tables: both the partition plan and verify artifacts are required. PF09 does not define partition semantics or thresholds; those remain in HDE-Governance and infra docs. This subtask ensures that the mechanics harness generates the governed artifacts and that they are part of the Evidence Index/Mirror set.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; semantics live in Governance/infra):**

  * `PARTITION_PLAN_OK`

  * `DB_SCHEMA_FINGERPRINT_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `artifacts/db/partition/partition_plan.txt`

  * `artifacts/db/partition/partition_verify.log`

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST001.9 — DB–bridge parity & env connectivity**

* **Subtask name/label:** DB–bridge parity & env connectivity

* **Subtask description:**  
   Prove parity between direct DB reads and bridge-mediated reads for BodyGraph, and capture the associated environment connectivity posture:

  * **Bridge parity transcripts.**

    * Produce `artifacts/bodygraph/vendor_upsert.<alias>.json` — vendor upsert transcript for a chosen alias (titles-only to HDE-Schemas & Artifacts for schema).

    * Produce `artifacts/bodygraph/db_resolve.<alias>.json` — DB resolve transcript for the same alias.

    * Use `artifacts/presenter/json_canon_compare.log` to show that the DB and bridge bodies are structurally equal under canonical JSON serialization.

  * **Env connectivity snapshot.**

    * In the same change window, capture `artifacts/runtime/env_connectivity.snapshot.json` as a canonical JSON snapshot of DB connectivity resolution (dev-only, names-only); schema and required fields are single-homed in HDE-Schemas & Artifacts.

* PF09 does not restate the JSON schemas for these artifacts or define DB/bridge policy values; those remain in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed bridge parity and env connectivity artifacts exist, are canonical, and are indexed under the Evidence Index discipline.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; semantics live in Governance/Schemas):**

  * `DB_CONN_ENV_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `artifacts/bodygraph/vendor_upsert.<alias>.json`

  * `artifacts/bodygraph/db_resolve.<alias>.json`

  * `artifacts/presenter/json_canon_compare.log`

  * `artifacts/runtime/env_connectivity.snapshot.json`

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST001.10 — Architecture snapshot (keys-only) evidence**

* **Subtask name/label:** Architecture snapshot (keys-only) evidence

* **Subtask description:**  
   Capture and index a keys-only architecture snapshot that reflects the Engine’s public and internal surfaces without exposing secrets or raw payloads:

  * Emit a governed architecture snapshot artifact (path and schema owned by HDE-Schemas & Artifacts) as canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

  * Ensure the snapshot is keys-only: no raw birth data, no vendor payloads, no credentials or sensitive header values.

  * Treat the snapshot as part of the gate harness evidence surface alongside determinism, A7, rails, DB posture, BodyGraph, and narrative key-table artifacts.

* PF09 does not define the concrete path or schema for the architecture snapshot; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed snapshot exist, be canonical and secret-free, and be indexed under the global Evidence Index discipline.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; semantics live in Governance/Schemas):**

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * Architecture snapshot artifact (titles-only; schema & path in HDE-Schemas & Artifacts)

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## Task HDE-DIST002 — Pack/manifest & release identity

* **Task ID:** HDE-DIST002

* **Task name/label:** Pack/manifest & release identity

* **Task status:** **Not done**

* **Task description:**  
   Canonicalize `catalog/manifest.json`, compute and recompute `release_id` as `sha256(canonical_bytes("catalog/manifest.json"))`, ensure manifest structure invariants, and index pack/manifest identity artifacts.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done; manifest freeze and release\_id recompute not run; no pack identity artifacts indexed.

### **Subtask HDE-DIST002.1 — Canonical `catalog/manifest.json`**

* **Subtask name/label:** Canonical `catalog/manifest.json`

* **Subtask description:**  
   Enforce manifest integrity and path invariants for `catalog/manifest.json`:

  * **Canonical JSON.**

    * `catalog/manifest.json` MUST be canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF), as defined in HDE-Schemas & Artifacts (titles-only).

  * **File list invariants.**

    * The manifest’s file list is ASCII-sorted by path.

    * There are no duplicate paths.

    * `catalog/manifest.json` MUST NOT appear in its own file list.

  * **Path constraints & pack root.**

    * Each listed path is rooted under the pack’s `"catalog/"` tree (path semantics and root rules are single-homed in HDE-Schemas & Artifacts).

    * Paths are POSIX-style (no `..` segments, no `//` sequences), and each path length is within the governed limits.

    * These invariants are enforced under the `PACK_ROOT_PINNED_OK`, `MANIFEST_PATH_ASCII_SORT_OK`, and `MANIFEST_NO_DUP_PATHS_OK` token family; PF09 consumes these tokens but does not redefine their semantics.

  * **Entry identity (by title).**

    * Per-entry `{path, sha256, size_bytes}` identity is verified via the manifest checksums audit (see HDE-DIST002.3); PF09 does not restate the per-entry schema here.

* All manifest checks MUST run under `LC_ALL=C`, `LANG=C`, `TZ=UTC` using canonical JSON rules shared with the rest of the Evidence Index discipline.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `PACK_MANIFEST_NO_SELF_LISTING_OK`

  * `MANIFEST_PATH_ASCII_SORT_OK`

  * `MANIFEST_NO_DUP_PATHS_OK`

  * `PACK_ROOT_PINNED_OK`

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * `artifacts/math/freeze_pack_manifest.json`

* **Notes:**  
   Detailed manifest shape and per-entry schema remain single-homed in HDE-Schemas & Artifacts; PF09 requires that the canonicalized manifest and its file list invariants are enforced and evidenced.

### 

### Subtask HDE-DIST002.2 — release\_id compute & recompute

* **Subtask name/label:** release\_id computation & recompute proof

* **Subtask description:**

  * Compute `release_id` as lowercase hex-64 `sha256(canonical_bytes("catalog/manifest.json"))`.

  * Capture recompute logs showing recomputation equals the on-disk `release_id`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `RELEASE_ID_RECOMPUTE_OK`

  * `MANIFEST_SHA256_HEX64_OK`

* **Evidence / artifacts:**

  * `artifacts/math/release_id.txt`

  * `artifacts/math/release_id_recompute.log`

### Subtask HDE-DIST002.3 — Checksums audit

* **Subtask name/label:** Manifest checksums audit

* **Subtask description:**  
   Run a checksums audit over manifest-listed artifacts and capture its log.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (audit behavior; semantics live in canon)

* **Evidence / artifacts:**

  * `artifacts/math/checksums_audit.log`

### Subtask HDE-DIST002.4 — Pack/manifest indexing

* **Subtask name/label:** Index pack/manifest identity artifacts

* **Subtask description:**  
   Index manifest and release identity artifacts in Human Index and Machine Mirror in the same PR; each mirror record includes a `proof_anchor` path-proof; HDE-Schemas & Artifacts §8.6 is the single home for listing and record types.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST002.5 — Release bindings evidence & indexing**

* **Subtask name/label:** Release bindings evidence & indexing

* **Subtask description:**  
   Capture and index the release bindings artifact that ties `release_id` to BodyGraph data source policy and refresh behavior:

  * Produce `artifacts/bodygraph/release_bindings.json` as canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

  * Record, at minimum, the governed fields `{release_id, data_source_policy, ttl_s, swr_s, snapshot_counts{…}}` as defined in HDE-Schemas & Artifacts (titles-only).

  * Index `release_bindings.json` in `docs/evidence/INDEX.json` and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to a co-located path\_proof).

* PF09 does not define the JSON schema or semantics of `release_bindings.json`; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed artifact exist, be canonical, and be indexed alongside pack/manifest identity evidence.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `JSON_CANONICAL_CHECK_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `artifacts/bodygraph/release_bindings.json`

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## Task HDE-DIST003 — Environment snapshot (singleton) & observability

* **Task ID:** HDE-DIST003

* **Task name/label:** Environment snapshot (singleton) & observability

* **Task status:** **Not done**

* **Task description:**  
   Capture a v3 singleton environment snapshot, plus keys-only logs and metrics snapshots, and index them under the Evidence Index discipline.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done; env matrix, metrics, and keys-only log samples are missing.

### Subtask HDE-DIST003.1 — Environment snapshot singleton (v3)

* **Subtask name/label:** `env_matrix.snapshot.json` v3 singleton

* **Subtask description:**

  * Produce `artifacts/runtime/env_matrix.snapshot.json` as a **singleton** per repo.

  * Enforce schema v3 (unknown-key rejection) with canonical JSON (`UTF-8`, sorted keys, compact, one LF).

  * Minimum shape:

    * `schema_version: 3`

    * `default_rails` for `dev/stage/prod/CI` with SAFE\_MODE/ALLOW\_NETWORK pins.

    * `determinism_pins`: `LC_ALL="C"`, `LANG="C"`, `TZ="UTC"`.

    * `presence` map for critical env vars (e.g., `DATABASE_URL`, `DB_BRIDGE_URL`, `db_allow_bridge_in_prod`).

    * `notes: []`.

  * Open in write mode (overwrite, never append); exactly one JSON object; final LF; no auxiliary content.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `ENV_SNAPSHOT_SINGLETON_OK`

  * `ENV_SNAPSHOT_SCHEMA_V3_OK`

  * `ENV_PINS_PRESENT_OK`

* **Evidence / artifacts:**

  * `artifacts/runtime/env_matrix.snapshot.json`

### Subtask HDE-DIST003.2 — Logs observability (keys-only)

* **Subtask name/label:** Keys-only logs sample

* **Subtask description:**

  * Ensure logs are keys-only: no raw birth data, no vendor payloads, no secrets.

  * Redact any key-like values.

  * Provide a sanitized log sample at `artifacts/bodygraph/keys_only.logs.sample`.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `LOGS_KEYS_ONLY_SAMPLE_OK`

  * `OBS_KEYS_ONLY_OK`

  * `BG_PRIVACY_OK`

* **Evidence / artifacts:**

  * `artifacts/bodygraph/keys_only.logs.sample`

### Subtask HDE-DIST003.3 — Metrics observability

* **Subtask name/label:** Metrics snapshot

* **Subtask description:**

  * Capture metrics including:

    * Counters (refresh successes/failures; rate-limit hits; circuit-breaker openings).

    * Histograms (e.g., `engine.latency_ms`, `presenter.latency_ms`).

    * Gauges (e.g., staleness%).

  * Store as canonical JSON at `artifacts/bodygraph/metrics.snapshot.json` (single LF).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `BG_METRICS_OK`

* **Evidence / artifacts:**

  * `artifacts/bodygraph/metrics.snapshot.json`

### Subtask HDE-DIST003.4 — Env snapshot & observability indexing

* **Subtask name/label:** Index env snapshot, logs, and metrics

* **Subtask description:**  
   Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR to include env snapshot, logs sample, and metrics artifacts, with `proof_anchor` path-proofs.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## Task HDE-DIST004 — Performance & Load Harness

* **Task ID:** HDE-DIST004

* **Task name/label:** Performance & Load Harness

* **Task status:** **Not done**

* **Task description:**  
   Provide a non-PII, deterministic performance suite with stable labels, reproducible scenarios, and SLO probes, with evidence and CI jobs.

* **Task notes:**

  * Focus is on reproducible metrics, parity under load, and safe logging.

### Subtask HDE-DIST004.1 — Profiles & run shapes

* **Subtask name/label:** Profiles & run shapes

* **Subtask description:**  
   Define and run performance profiles for the Engine’s key surfaces and microbenchmarks:

  * **Surfaces covered:** Reader, Compat, and the Narrative Selection Router (keys-only).

  * **Profiles:** small / default / long runs; warm vs cold runs; bounded concurrency; rails CLOSED by default unless explicitly opened under the rails gates.

  * **Microbenchmarks:** compat core computation and narrative key lookups (titles-only to Mechanics/Math for detailed behavior).

* PF09 does not define numeric SLO thresholds or success/failure posture; those remain single-homed in Governance. This subtask requires that the performance harness exercise these surfaces and microbenchmarks under the defined profiles.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (performance semantics and SLO tokens live in Governance; PF09 is consumer-only)

* **Evidence / artifacts:**

  * `artifacts/bench/bench_report_{release_id}.json`

### Subtask HDE-DIST004.2 — Metrics & SLO probes

* **Subtask name/label:** Metrics, SLOs, and parity under load

* **Subtask description:**

  * Capture percentiles and histograms (e.g., `engine.latency_ms`, `presenter.latency_ms`).

  * Counters by outcome.

  * Use bounded labels (`route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`).

  * Run SLO probes for steady-state latency (p95/p99 bands) and budget for canonicalization and preimage cost.

  * Prove parity under realistic load.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (SLO semantics are descriptive here)

* **Evidence / artifacts:**

  * `artifacts/bench/bench_report_{release_id}.json`

  * `artifacts/bench/parity_identity_{release_id}.log`

  * `artifacts/bench/transport_headers_{release_id}/…`

### Subtask HDE-DIST004.3 — Bench CI jobs

* **Subtask name/label:** Bench CI orchestration

* **Subtask description:**  
   Wire CI jobs for math/transport and vendor-open bench runs and SLO verification:

  * `ci/jobs/bench_math_transport.yml`

  * `ci/jobs/bench_vendor_open.yml`

  * `ci/jobs/slo_verify.yml`

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown**

* **Evidence / artifacts:**

  * The CI job definitions above

### Subtask HDE-DIST004.4 — Performance harness indexing

* **Subtask name/label:** Index performance & load artifacts

* **Subtask description:**  
   Update Human Index and Machine Mirror in the same PR for bench artifacts (records-only canonical JSONL; one LF; `proof_anchor` present).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

---

## Task HDE-DIST005 — Global discipline (Phase VI)

* **Task ID:** HDE-DIST005

* **Task name/label:** Global discipline (Phase VI)

* **Task status:** **Not done** (treated as an ongoing global requirement)

* **Task description:**  
   Enforce that all Phase VI evidence artifacts use canonical encodings and are captured under pinned locale, and that every artifact addition/move/removal is reflected in both Human Index and Machine Mirror in the same PR.

* **Task notes:**

  * All artifacts under evidence are canonical JSON or headers-only text and LF-terminated.

  * All harnesses and checks that reason about bytes run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

  * Index updates are mandatory for `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`.

  * HDE-Schemas & Artifacts §8.6 is the single home for the evidence listing; Appendix C is the single home for record type schemas; PF09 does not redefine them.

### Subtask HDE-DIST005.1 — Canonical encodings & environment pins

* **Subtask name/label:** Canonical encodings & LC pins

* **Subtask description:**  
   Ensure all Phase VI evidence artifacts:

  * Use canonical JSON or headers-only text, LF-terminated.

  * Are produced under `LC_ALL=C`, `LANG=C`, `TZ=UTC` for any byte-sensitive harnesses.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `ENV_LC_ALL_C_OK`

  * `CI_CHECK_FINAL_LF_OK`

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence / artifacts:**

  * Various canonical JSON and canonical-compare logs across Phase VI (e.g., `audit/gates/canonical_json/json_canon_compare.log`).

### Subtask HDE-DIST005.2 — Global Index & Mirror discipline

* **Subtask name/label:** Evidence Index & Machine Mirror updates

* **Subtask description:**  
   For any artifact added/moved/removed in this phase:

  * Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR.

  * Keep `artifacts/evidence_index.jsonl` as records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF; unknown-key reject).

  * Maintain fixed field order and `proof_anchor` to co-located path\_proof files.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

## Task HDE-DIST006 — Identity & Provenance module

*Task name/label:* Identity & Provenance fields, helpers, and evidence

*Task description:*  
 Wire the Identity & Provenance module as the single source of truth for engine and release identity. Identity values are initialized once per cut and are read-only thereafter; all public and operator surfaces consume via helpers (titles-only to PF‑Canon‑HDE‑Mechanics §13). PF09 binds the identity fields, helpers, and evidence artifacts to specific acceptance tokens.

*Task status:* Not started

*Epic or card:* Unknown

### Subtask HDE-DIST006.1 — Identity fields & source-of-truth

*Subtask name/label:* Identity field set & immutability

*Subtask description:*

* Ensure the Identity & Provenance module exposes and persists exactly these fields — no extras — as read-only values after freeze (titles-only to Mechanics §13.1):

  * `engine_tag`

  * `build_commit`

  * `invocation_tag`

  * `invocation_sha256`

  * `emitter_sha256`

  * `release_id`

* Prove that:

  * `release_id` is derived only from the PF‑12 freeze pack manifest (`pack/manifest`), as `sha256(canonical manifest bytes)`, and is not recomputed at request time.

  * `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` are taken from the build snapshot at cut time; `invocation_tag` and Invocation bytes come from the Invocation registry (titles-only).

  * Identity fields are not mutated after freeze and are not overridden by env vars, flags, or other alternate sources on public paths.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; live in Governance / Identity canon):*

* `RELEASE_ID_RECOMPUTE_OK`

* `TWO_RUN_IDENTITY_OK`

* `CLI_READER_EMITTER_PARITY_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts (titles/paths only; schemas live in PF‑Canon‑HDE‑Schemas & Artifacts / PF‑Canon‑HDE‑Mechanics §13.6):*

* `artifacts/pack/manifest.json` (or equivalent canonical bytes snapshot) — `pack/manifest`

* `artifacts/identity/release_id.json` — `identity/release_id`

* `artifacts/identity/release_id_recompute.log` — `identity/release_id_recompute`

### Subtask HDE-DIST006.2 — Identity helpers & parity

*Subtask name/label:* identity\_meta / identity\_admin helpers

*Subtask description:*

* Prove that public Reader and CLI code paths obtain identity from the Identity & Provenance module helpers (titles-only to Mechanics §13.2):

  * `identity_meta()` → `{"engine_tag","invocation_tag"}` is injected into the Reader public envelope before idempotence hashing (preimage) and is present in both Reader and CLI responses on public surfaces.

  * `identity_admin()` → `{"engine_tag","release_id","invocation_tag","invocation_sha256","build_commit","emitter_sha256"}` is used by internal/admin surfaces (including `/internal/version`) and evidence capture.

* Demonstrate CLI↔Reader parity on identity\_meta: the same inputs yield byte-identical public bodies (LF-terminated canonical JSON).

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only):*

* `CLI_READER_EMITTER_PARITY_OK`

* `TWO_RUN_IDENTITY_OK`

*Evidence / artifacts:*

* `artifacts/parity/two_run_identity.log` — `parity/two_run_identity` (two-run identity digest/log for public bodies, LF-terminated)

* `artifacts/identity/service_identity.json` — `identity/service_identity` (admin snapshot of identity fields)

### Subtask HDE-DIST006.3 — Identity hashes & mirror discipline

*Subtask name/label:* Identity hashes & Mirror records

*Subtask description:*

* Capture and persist build-time hashes for the shared emitter and invocation and index them as identity artifacts (titles-only to Mechanics §13.6):

  * `identity/emitter_sha256` — hash of the allow-listed presenter/emitter source.

  * `identity/invocation_sha256` — hash of canonical Invocation bytes.

* List the identity artifacts by title/path in `docs/evidence/INDEX.json` and mirror them 1:1 in `artifacts/evidence_index.jsonl` as canonical JSONL (UTF‑8, sorted keys, compact, exactly one LF).

* Enforce mirror discipline:

  * One JSON object per line.

  * Reject unknown keys in mirror records.

  * `(artifact_key, discovered_physical_path)` in the mirror matches the human Index entry.

  * Each record includes a `proof_anchor` path-proof stored alongside the artifact.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only):*

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts:*

* `artifacts/identity/emitter_sha256.json` — `identity/emitter_sha256`

* `artifacts/identity/invocation_sha256.json` — `identity/invocation_sha256`

* `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

* `artifacts/evidence_index.jsonl`

**Acceptance impact**

Tokens referenced (all already defined in PF14 / Governance; no new tokens):

* `RELEASE_ID_RECOMPUTE_OK`, `TWO_RUN_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

These are being **bound** more concretely to identity-module evidence; no new token definitions are introduced.

**Artifacts impact**

New or clarified artifact paths mentioned:

* `artifacts/pack/manifest.json` (or equivalent) — `pack/manifest`

* `artifacts/identity/release_id.json` — `identity/release_id`

* `artifacts/identity/release_id_recompute.log` — `identity/release_id_recompute`

* `artifacts/parity/two_run_identity.log` — `parity/two_run_identity`

* `artifacts/identity/service_identity.json` — `identity/service_identity`

* `artifacts/identity/emitter_sha256.json` — `identity/emitter_sha256`

* `artifacts/identity/invocation_sha256.json` — `identity/invocation_sha256`

Schemas and exact field shapes remain routed to PF‑Canon‑HDE‑Schemas & Artifacts / PF14 Mechanics.

# ---

#  Phase VII — Coagulation (SDKs & runtime packaging) 

* **Phase description:**  
   Ship a hardened runtime and minimal client SDKs that emit the six-key public envelope and typed errors, and lock evidence/ops practices to Governance, with no contract bytes or schemas defined here (titles-only routing to canon).

* **Phase master status:** **Not done**

* **Notes:**

  * Scope is runtime packaging, production ops posture (including `/internal/version`), A7 behavior on success routes, and minimal SDKs that mirror public contracts.

  ---

  ## Task HDE-COAG001 — Packaging & Runtime

* **Task ID:** HDE-COAG001

* **Task name/label:** Packaging & Runtime

* **Task status:** **Not done**

* **Task description:**  
   Produce a deterministic, hardened runtime artifact aligned with Governance: reproducible image, env/rails pins, start command capture, ops surface for `/internal/version`, optional caching, and security posture for writers/inputs, with evidence indexed.

* **Task notes:**

  * **Status (Audit v1 — 2025-11-17):** Not done.

  * Missing tokens (titles-only; tokens live in HDE-Governance):

    * `SERVICE_START_CMD_CAPTURED_OK`

    * `GUNICORN_APP_FACTORY_OK`

    * `ENV_PORT_REQUIRED_OK`

  * SBOM / start-command / env pins proofs are not yet gathered.

  ### Subtask HDE-COAG001.1 — Image hygiene

* **Subtask name/label:** Runtime image hygiene & reproducibility

* **Subtask description:**

  * Build **reproducible** container images for the engine runtime.

  * Run as non-root; prefer a read-only filesystem where practical.

  * Generate a **CycloneDX SBOM** for the runtime image.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (SBOM and reproducibility semantics live in Governance/Security canon)

* **Evidence / artifacts:**

  * `sbom/cyclonedx.json`

  * `sbom/cyclonedx.json.sha256`

* **Notes:**

  * SBOM must be present and hashed; PF09 only references their paths and gating tokens by title.

  ### Subtask HDE-COAG001.2 — Env & secrets posture

* **Subtask name/label:** Env allow-list & secrets discipline

* **Subtask description:**

  * Enforce an **env allow-list**; ignore or fail on unexpected env keys.

  * Ensure rails defaults match infra inventory for each environment (dev/stage open; prod/CI closed), per Glow-Infrastructure.

  * Never log secrets or PII; enforce redaction for any key-like header or token.

  * Export and verify `LC_ALL=C`, `LANG=C`, `TZ=UTC` in the runtime environment to preserve determinism.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `ENV_LC_ALL_C_OK` (indirectly implied via env pins)

  * Other env/rails tokens live in Governance; PF09 only routes to them.

* **Evidence / artifacts:**

  * `artifacts/proofs/env_pins.txt` — captures `LC_ALL`, `LANG`, `TZ`, rails posture, and port binding in effect.

  ### Subtask HDE-COAG001.3 — Start command & service factory

* **Subtask name/label:** Service start command & app factory

* **Subtask description:**

  * Capture the exact **production start command** as `artifacts/proofs/start_command_capture.txt` (UTF-8; one LF; no secrets).

  * Prove the runtime starts via the configured **app factory** (e.g., `adapter.factory:create_app`) rather than ad-hoc entrypoints.

  * Ensure the service binds `$PORT`, not a hard-coded port (enforce `ENV_PORT_REQUIRED_OK`).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `SERVICE_START_CMD_CAPTURED_OK`

  * `GUNICORN_APP_FACTORY_OK`

  * `ENV_PORT_REQUIRED_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/start_command_capture.txt`

  * `artifacts/proofs/env_pins.txt` (captures port binding and env pins)

### **Subtask HDE-COAG001.4 — Health & ops surface `/internal/version`**

*Subtask name/label:* `/internal/version` ops surface behavior

*Subtask description:*  
 Implement and prove `/internal/version` behavior, aligned with the Identity & Provenance Module (§13) and Internal Meta Surface (§14) in the Mechanics guide (titles-only). This subtask pins the ops transport posture, payload shape, and evidence artifacts for the internal meta endpoint:

* GET `/internal/version` is **operator-only**, always:

  * `Cache-Control: no-store`

  * **No ETag**

  * `Content-Type: application/json; charset=utf-8`

  * **No `Last-Modified` header**

* HEAD `/internal/version`:

  * Returns 200 with no body.

  * Mirrors 200 validators, including `Content-Type`.

  * `Content-Length == len(identity GET body)` (LF-terminated canonical body).

* Conditionals (`If-Modified-Since`, `If-None-Match`) are **ignored**; the endpoint never returns 304 and is not A7-eligible.

* Body:

  * Body is canonical JSON (UTF‑8, no BOM, compact, exactly one trailing LF).

  * Key order is **frozen** and matches the Identity & Provenance / Internal Meta spec (titles-only to Mechanics §13–§14):

    1. `engine_tag`

    2. `build_commit`

    3. `invocation_tag`

    4. `invocation_sha256`

    5. `emitter_sha256`

    6. `release_id`

  * Values are sourced via `identity_admin()` from the Identity & Provenance module (no direct env reads at emit time; no mutation after freeze).

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens (titles-only; live in HDE-Governance):*

* `INTVER_200_CTYPE_JSON_UTF8_OK`

* `INTVER_HEAD_PARITY_OK`

* `INTVER_CONDITIONALS_IGNORED_OK`

* `INTVER_200_NO_ETAG_OK`

* `TWO_RUN_IDENTITY_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts:*

* `artifacts/ops/internal_version/headers_get.txt` — raw GET headers (`intver/headers_get`)

* `artifacts/ops/internal_version/headers_head.txt` — raw HEAD headers (`intver/headers_head`)

* `artifacts/ops/internal_version/body_get.json` — exact LF-terminated GET body (`intver/body_get`)

* `artifacts/ops/internal_version/cond_if_none_match.txt` — GET with `If-None-Match` still returning 200 (`intver/cond_if_none_match`)

* `artifacts/ops/internal_version/cond_if_modified_since.txt` — GET with `If-Modified-Since` still returning 200 (`intver/cond_if_modified_since`)

* `artifacts/ops/internal_version/two_run_identity.log` — two-run identity log for `/internal/version` (`intver/two_run_identity`)

* `artifacts/ops/internal_version/provenance_note.json` (or `.md`) — operator note capturing `release_id`, `invocation_tag`, optional `build_commit`, capture timestamp (`intver/provenance_note`)

*Notes:*

* For all `intver/*` artifacts, list titles/paths in `docs/evidence/INDEX.json` and mirror 1:1 in `artifacts/evidence_index.jsonl` (canonical JSONL, one LF; unknown keys rejected). The mirror records include `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor` pointing to a co-located path-proof file.

**Acceptance impact**

Tokens referenced here:

* `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

All tokens already exist in Governance / PF14; we only clarify which artifacts and checks satisfy them for `/internal/version`.

**Artifacts impact**

New or refined artifact paths:

* `artifacts/ops/internal_version/body_get.json` (canonical body; replaces generic `body.json` naming)

* `artifacts/ops/internal_version/cond_if_none_match.txt`

* `artifacts/ops/internal_version/cond_if_modified_since.txt`

* `artifacts/ops/internal_version/two_run_identity.log`

* `artifacts/ops/internal_version/provenance_note.json`

These correspond to PF14’s `intver/*` artifact keys; schemas remain routed to PF‑Canon‑HDE‑Schemas & Artifacts.

### **Subtask HDE-COAG001.5 — Optional production caching**

*Subtask name/label:* Private Reader cache (optional)

*Subtask description:*

If a production cache is used, provide a **private, composite-key cache** for Reader and Compat that preserves A7 transport rules and deterministic invalidation:

* **Composite key (keys-only).**

  * Use a composite cache key of the form:

    * `{viewer_id | person_id(s)}, design_fingerprint, thresholds_identity, release_id`.

  * Normalize `{a,b}` pairs to a stable order before keying (AB↔BA neutrality) so that compat/Reader responses for `(A,B)` and `(B,A)` hit the same cache entry.

  * Include `viewer_id` in the key **only** when cacheable output depends on viewer preferences (e.g. perspective); otherwise, omit it so that the same content is shared across viewers.

* **Deterministic key construction.**

  * Key construction must be pure and reproducible:

    * No dependence on clocks, randomness, or ambient environment state.

    * Derived only from the normalized inputs and identity fields listed above (titles-only to Mechanics/Math for design\_fingerprint and thresholds\_identity semantics).

* **A7-consistent transport behavior.**

  * Cache hits must preserve full A7 semantics for the success route:

    * 200: `Content-Type: application/json; charset=utf-8`; strong, quoted ETag over the LF-terminated body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.

    * 304: only after a prior 200 for the same ETag; no body; omit `Content-Type` and `Content-Length`; validators mirror the cached 200; ETag present.

    * HEAD: status 200; no body; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

  * Writers and errors **bypass** the cache and continue to send `Cache-Control: no-store` with **no ETag**; cached paths must not alter typed error envelopes.

  * `/internal/version` remains operator-only and is never cached.

* **Deterministic invalidation.**

  * Invalidate cache entries immediately on any change to:

    * `release_id`,

    * `thresholds_identity`,

    * design/manifest identity (design\_fingerprint or pack/manifest identity), or

    * input payloads that affect the response (including viewer\_prefs when present).

  * Once invalidated, no stale bytes may be served; cache re-populates only via fresh emissions under the same A7 posture.

* **Controls & diagnostics.**

  * Default **OFF**: the production cache is disabled by default and may be enabled **only** via a documented runtime flag or configuration toggle; PF09 does not pin the flag name or config path.

  * Metrics:

    * Emit **bounded** counters for cache hits, misses, and invalidations (labels such as `route`, `outcome`, `rails_state`, `timeout_profile`), reusing the global observability/metrics discipline.

  * Optional diagnostics:

    * When enabled for debugging, maintain a redaction-safe, keys-only debug log of cache decisions (hits/misses/invalidation) suitable for local analysis; routes, IDs, and state are logged via bounded labels only; no raw payloads or secrets may appear.

* PF09 does not define cache internals, SLO thresholds, or diagnostics log paths; those remain single-homed in Governance, Mechanics, and infra/ops docs. This subtask records that, when a production cache is present, it obeys composite-key, determinism, A7-consistent transport, deterministic invalidation, metrics, and optional diagnostic logging as described above.

*Subtask status:* Not started

*Epic or card:* Unknown

*Tokens:* (unchanged; semantics live in Governance; PF09 routes by title only)

*Evidence / artifacts:* (unchanged; cache behavior is supported by existing A7 and parity/observability evidence from other phases)

### Subtask HDE-COAG001.6 — Security posture for writers & inputs

* **Subtask name/label:** Writers & input security posture

* **Subtask description:**

  * Apply per-route **rate limits** on writer endpoints; no unbounded fan-out.

  * Writers and error routes always send `Cache-Control: no-store` and **never send ETag**.

  * Inputs are validated against schemas (titles-only to HDE-Schemas & Artifacts).

  * Never log secrets or PII; enforce redaction at the logger boundary.

  * For browser-facing writers: rotate CSRF token on login and allow exactly one safe retry on CSRF failure.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; PF09 consumer-only):**

  * A7-related success tokens (for success routes, not writers):

    * `READER_200_CTYPE_JSON_UTF8_OK`

    * `A7_GET_QUOTED_ETAG_OK`

    * `A7_HEAD_PARITY_OK`

    * `A7_304_OMITS_CT_CL_OK`

    * `A7_VARY_AUTH_AE_OK`

    * `A7_ENCODING_INVARIANCE_OK`

  * Body parity & pack identity:

    * `MANIFEST_SHA256_HEX64_OK`

    * `RELEASE_ID_RECOMPUTE_OK`

    * `PACK_MANIFEST_NO_SELF_LISTING_OK`

  * Packaging & Ops:

    * `SERVICE_START_CMD_CAPTURED_OK`

    * `GUNICORN_APP_FACTORY_OK`

    * `ENV_PORT_REQUIRED_OK`

* **Evidence / artifacts:**

  * Writer-specific logs and DDL updates would be indexed via Evidence Index; PF09 only lists high-level paths under other phases.

  ### Subtask HDE-COAG001.7 — Packaging & runtime indexing

* **Subtask name/label:** Index runtime & A7 evidence artifacts

* **Subtask description:**  
   For the runtime-related artifacts in this task:

  * Update, in the same PR:

    * `docs/evidence/INDEX.json`

    * `docs/evidence/INDEX.sha256`

    * `artifacts/evidence_index.jsonl`

  * Keep the Machine Mirror as **records-only canonical JSONL** (UTF-8; one LF per record; unknown-key reject; fixed field order; `proof_anchor` to co-located `path_proof.txt`).

  * Rely on HDE-Schemas & Artifacts §8.6 and Appendix C for entry listings and record-type schemas.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ### **Subtask HDE-COAG001.8 — Health/ready probes & graceful shutdown**

* **Subtask name/label:** Health/ready probes & graceful shutdown

* **Subtask description:**  
   Prove that the runtime exposes canonical health/readiness endpoints and shuts down gracefully:

  * **HTTP probes.**

    * Expose `/healthz` as a liveness probe (process up, core initialized).

    * Expose `/readyz` as a readiness probe (emitter wired, pack loaded, manifest hashed, rails posture read).

    * Both probes return minimal, numeric-free JSON bodies that are canonical (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF), using the shared presenter/emitter and global canonical JSON rules.

  * **Lifecycle & graceful shutdown.**

    * On `SIGTERM`, stop accepting new traffic, allow in-flight requests to complete, and then exit cleanly with status 0\.

    * Emit a final readiness/health snapshot (or log) that clearly indicates the “stopping” state, without leaking payloads or secrets.

  * **Evidence & indexing.**

    * Capture governed health/ready and shutdown artifacts (titles and paths owned by the Documentation Artifacts and Registry section) and index them under the Evidence Index discipline: list them in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path\_proof files).

* PF09 does not define the exact JSON schema or artifact paths for the probes and lifecycle logs; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed probes and lifecycle behavior exist, are canonical and numeric-free, and are evidenced and indexed.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; semantics live in Governance/Schemas):**

  * `JSON_CANONICAL_CHECK_OK`

  * `ENV_LC_ALL_C_OK`

  * `CI_CHECK_FINAL_LF_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * Health/ready probe artifacts and lifecycle/shutdown logs (titles/paths listed in §36 Documentation Artifacts and Registry).

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-COAG002 — SDKs (TypeScript / Python)

* **Task ID:** HDE-COAG002

* **Task name/label:** SDKs (TypeScript / Python)

* **Task status:** **Not done**

* **Task description:**  
   Provide minimal TypeScript and Python SDKs that mirror the six-key public envelope and typed error contracts, ensuring canonical JSON behavior and parity with Reader, with no public numerics or hidden behavior.

* **Task notes:**

  * SDKs must route contract ownership by title to HDE-CLI-API-Vendor-Ref; PF09 does not restate schemas or bytes.

  ### Subtask HDE-COAG002.1 — Models & serialization

* **Subtask name/label:** SDK data models & canonical JSON serialization

* **Subtask description:**

  * Define strongly-typed models for:

    * The six-key success envelope.

    * Typed error shapes.

  * Route contract ownership (by title) to HDE-CLI-API-Vendor-Ref.

  * Implement canonical JSON serialization in SDKs:

    * UTF-8, no BOM.

    * Sorted keys.

    * Compact (no extra whitespace).

    * Exactly one trailing LF.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `SDK_ROUND_TRIP_CANONICAL_JSON_OK` (implicitly depends on canonical serialization)

* **Evidence / artifacts:**

  * Type and schema fixtures:

    * `sdks/typescript/schemas/*.json`

    * `sdks/python/schemas/*.json`

  ### Subtask HDE-COAG002.2 — Round-trip & Reader parity

* **Subtask name/label:** Round-trip and Reader/error parity

* **Subtask description:**

  * Ensure `serialize → parse → serialize` is **byte-exact** for valid payloads (canonical JSON round-trip).

  * For a shared test corpus, show SDK responses match Reader’s public envelope and typed error shapes exactly:

    * No extra fields.

    * No missing fields.

    * No renaming.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `SDK_ROUND_TRIP_CANONICAL_JSON_OK`

  * `SDK_READER_PARITY_OK`

  * `SDK_ERROR_CONTRACT_PARITY_OK`

* **Evidence / artifacts:**

  * Test outputs:

    * `sdks/typescript/tests/*`

    * `sdks/python/tests/*`

  * Artifacts per SDK:

    * `sdks/<lang>/artifacts/schema_hashes.json`

    * `sdks/<lang>/artifacts/reader_roundtrip.bytes`

    * `sdks/<lang>/artifacts/error_contract_snapshot.json`

  ### Subtask HDE-COAG002.3 — Optional retries & conditional GET

* **Subtask name/label:** Optional conditional GET helper

* **Subtask description:**

  * Default: **no automatic retries**; SDK must not introduce its own retry policy.

  * Where implemented, a conditional GET helper for Reader:

    * Constructs headers according to the same rules as the core (titles-only).

    * Must not change ETag semantics.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (conditional GET behavior is referenced by title only)

* **Evidence / artifacts:**

  * `sdks/<lang>/artifacts/conditional_get_headers.snap` (if implemented)

  ### Subtask HDE-COAG002.4 — SDK artifacts indexing

* **Subtask name/label:** Index SDK evidence artifacts

* **Subtask description:**  
   Update Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR for all SDK artifacts; ensure mirror records follow HDE-Schemas & Artifacts §8.3/§8.6 (canonical JSONL, single file, `proof_anchor`, governed paths).

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

  ## Task HDE-COAG003 — Runbooks & Deployment Guards

* **Task ID:** HDE-COAG003

* **Task name/label:** Runbooks & Deployment Guards

* **Task status:** **Not done**

* **Task description:**  
   Codify a repeatable go-live and rollback process that enforces Doc-Delta discipline, release identity, Index parity, parity/rails/ops gates, and alerting on critical failures.

* **Task notes:**

  * Phase describes **Build → Verify → Release → Rollback** flows, pre-flight CI jobs, and metrics/alerts, but they are not yet fully implemented or evidenced.

  ### **Subtask HDE-COAG003.1 — Build/Verify/Release/Rollback & incident runbooks**

* **Subtask name/label:** Build/Verify/Release/Rollback & incident runbooks

* **Subtask description:**  
   Write concise, operator-focused runbooks for:

  * **Build → Verify → Release → Rollback** flows, covering:

    * Regenerating `release_id` from the canonical manifest (via SHA-256).

    * Rebuilding and verifying evidence for A7, determinism & parity, DB posture, and BodyGraph invariance.

    * Updating the Human Evidence Index, hash sentinel, and Machine Mirror (same PR).

    * Performing a safe rollback that preserves data safety and verifies no stale cache entries or A7 breakage.

  * **Incident handling:**

    * Elevated `5xx` rates on Reader/Compat surfaces.

    * Slow Reader/Compat responses (latency regressions).

    * Stuck queue or processing backlog.

    * DB lag or degraded DB posture.

* Runbooks SHOULD reference the “pointer-flip” rollback pattern by title (flipping pointers to the last known-good `release_id`) where appropriate; PF09 does not restate pointer mechanics or DB migration steps. This subtask requires that operational runbooks exist, are kept in sync with release identity and evidence practices, and are captured as governed artifacts.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (runbooks themselves are not token-gated; tokens apply to the mechanics they orchestrate)

* **Evidence / artifacts:**

  * `docs/runbooks/*.md`

### 

### Subtask HDE-COAG003.2 — Pre-flight CI jobs

* **Subtask name/label:** Pre-flight CI gate jobs

* **Subtask description:**  
   Add pre-flight CI jobs that **fail fast** on:

  * Parity drift (CLI↔Reader / SDK↔Reader).

  * Canonical bytes mismatch (JSON canonicalization).

  * Stale `docs/evidence/INDEX.json` vs `artifacts/evidence_index.jsonl`.

  * ETag invariance / A7 regressions.

  * Rails posture violations and missing env pins.

  * 429 handling regressions.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * Likely re-use of parity, JSON canonical, A7, env, and evidence tokens listed in other phases; PF09 only references them by name.

* **Evidence / artifacts:**

  * `audit/gates/ops/release_dryrun.log` (dry-run output can be part of pre-flight verification)

  ### **Subtask HDE-COAG003.3 — Ops metrics, dashboards & alerting**

* **Subtask name/label:** Ops metrics, dashboards & alerting

* **Subtask description:**  
   Configure production metrics, dashboards, and alerts with bounded labels and actionable signals:

  * **Surfaces & dashboards.**

    * Provide dashboards for Reader, Compat, the Narrative Selection Router, and the Server Cache.

    * Include panels for:

      * Latencies and error rates by surface.

      * Cache hit/miss ratios and cache-related latencies.

      * Rate-limit outcomes.

      * A7 headers health on the Catalog JSON success route (e.g., ETag, Vary, cache headers).

  * **Metrics & labels.**

    * Use bounded labels such as `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`.

    * Capture counters, histograms, and gauges for request counts, latency percentiles, cache hits/misses, rate-limit outcomes, and BodyGraph ingest signals (titles-only to Mechanics/Distillation for schema).

  * **Alerts.**

    * Define alerts for:

      * Unexpected spikes in `5xx` and `429`.

      * Circuit-breaker activations.

      * A7 invariant failures or degraded A7 headers health.

      * Evidence indexing failures (missing mirror records or `proof_anchor` mismatches).

      * Cache hit-ratio or latency breaching agreed budgets.

* PF09 does not define SLO thresholds or alert routing; those remain single-homed in Governance and ops docs. This subtask requires that metrics/dashboards reflect the key Engine surfaces and cache, and that alerts are wired to error/latency/A7/evidence/cache health in a bounded, non-PII way.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:** **Unknown** (SLO/alert tokens, if any, live in Governance; PF09 is consumer-only here)

* **Evidence / artifacts:**

  * `artifacts/ops/alerts/*.json`


  ### Subtask HDE-COAG003.4 — Runbook & ops indexing

* **Subtask name/label:** Index runbooks and ops artifacts

* **Subtask description:**  
   Update Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR for runbooks, ops dry runs, and alert configs. Mirror must follow HDE-Schemas & Artifacts §8.3/§8.6 (canonical JSONL, one file, unknown-key reject, `proof_anchor` path-proofs). PF09 depends on Governance and Schemas for token semantics and record schemas; it only requires evidence presence and indexing.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_INDEX_HASH_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Evidence / artifacts:**

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  ---

### **Subtask HDE-COAG003.5 — Post-deploy smoke harness & indexing**

* **Subtask name/label:** Post-deploy smoke harness & indexing

* **Subtask description:**  
   Provide a post-deploy smoke harness that runs against the live production environment immediately after deploy and captures a minimal, governed evidence set:

  * **Scope & pins.**

    * Run all smoke checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

    * Use a JSON success route listed in `docs/ENDPOINTS_CATALOG.json` as the A7 smoke surface; `/internal/version` remains ops-only and not A7-eligible.

  * **Success route (A7) transport smoke.**

    * Capture headers-only proofs for:

      * `artifacts/proofs/success_get.txt` — 200 with strong quoted ETag, JSON Content-Type, Cache-Control, and Vary.

      * `artifacts/proofs/success_head.txt` — HEAD parity (no body; validators mirror 200; Content-Type \== GET; Content-Length \== identity 200 body).

      * `artifacts/proofs/success_304.txt` — 304 only after a prior 200; no body; omit Content-Type and Content-Length; validators mirror cached 200\.

      * `artifacts/proofs/success_writers_errors.txt` — writers/errors posture (no-store, no ETag; error Content-Type).

  * **Writers & errors posture smoke.**

    * Confirm that writers and error routes on the exercised surfaces send `Cache-Control: no-store` and no ETag, and that errors are typed, numeric-free JSON with `Content-Type: application/json; charset=utf-8`, as governed by HDE-CLI-API-Vendor-Ref and HDE-Governance.

  * **Internal ops `/internal/version` smoke.**

    * Capture:

      * `artifacts/ops/internal_version/headers_get.txt` and `headers_head.txt` — GET/HEAD 200 posture (no-store, no ETag; HEAD mirrors GET validators; Content-Length matches LF-terminated body).

      * `artifacts/ops/internal_version/cond_if_none_match_headers.txt` and `cond_if_modified_since_headers.txt` — conditionals ignored; endpoint never returns 304\.

      * `artifacts/ops/internal_version/body_get.json` and `body_get.sha256` — canonical JSON body and its hash.

      * `artifacts/ops/internal_version/provenance_note.md` — human-readable provenance note for the deployed release.

  * **DB posture smoke.**

    * Reuse DB posture artifacts from the DB posture tasks to spot-check live DB:

      * `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`, `artifacts/db/check_constraints.txt`.

      * Optional: `artifacts/db/partition_plan.txt` and `artifacts/db/db_rw_smoke.log` for partition and read/write smoke where run.

  * **Pins & harness evidence.**

    * Capture `artifacts/proofs/env_pins.txt` showing runtime env pins and rails posture in effect during smoke.

  * **Indexing.**

    * List all smoke artifacts in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR, using canonical JSONL (one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path\_proof transcripts).

* PF09 does not redefine A7, writers/error, INTVER, or DB token semantics; those remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref. This subtask requires that a post-deploy smoke harness exist, capture the governed artifacts above, and satisfy Evidence Index & Mirror discipline.

* **Subtask status:** **Not started**

* **Epic or card:** **Unknown**

* **Tokens (titles-only; semantics live in Governance/Schemas):**

  * `A7_GET_QUOTED_ETAG_OK`

  * `A7_HEAD_PARITY_OK`

  * `A7_304_OMITS_CT_CL_OK`

  * `A7_VARY_AUTH_AE_OK`

  * `READER_200_CTYPE_JSON_UTF8_OK`

  * `INTVER_200_CTYPE_JSON_UTF8_OK`

  * `INTVER_HEAD_PARITY_OK`

  * `INTVER_CONDITIONALS_IGNORED_OK`

  * `INTVER_200_NO_ETAG_OK`

  * DB posture tokens (e.g., `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`)

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Evidence / artifacts:**

  * `artifacts/proofs/success_get.txt`

  * `artifacts/proofs/success_head.txt`

  * `artifacts/proofs/success_304.txt`

  * `artifacts/proofs/success_writers_errors.txt`

  * `artifacts/ops/internal_version/headers_get.txt`

  * `artifacts/ops/internal_version/headers_head.txt`

  * `artifacts/ops/internal_version/cond_if_none_match_headers.txt`

  * `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

  * `artifacts/ops/internal_version/body_get.json`

  * `artifacts/ops/internal_version/body_get.sha256`

  * `artifacts/ops/internal_version/provenance_note.md`

  * `artifacts/db/ddl_fingerprint.json`

  * `artifacts/db/grants.txt`

  * `artifacts/db/check_schema.txt`

  * `artifacts/db/check_constraints.txt`

  * `artifacts/db/partition_plan.txt` (if used)

  * `artifacts/db/db_rw_smoke.log` (optional)

  * `artifacts/proofs/env_pins.txt`

  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

## Task HDE-COAG004— Stateless JSON QA mode (non-gating tracker)

*Task ID:* HDE-COAG00X  
 *Task name/label:* Stateless JSON QA mode (non-gating tracker)  
 *Task status:* Not started

*Task description:*  
 Track the future stateless JSON QA mode described in PF14 and ensure it does not accidentally become a merge-blocking gate before the owning epic lands:

* **Scope and ownership (titles-only).**

  * PF14 — HDE-Mechanics Guide §17.9 (“Stateless JSON QA mode”) and HDE-Build Notes Addendum 11 define a future, no-DB JSON QA mode for BodyGraph export, compat export, and vendor-to-engine pipelines.

  * HDE-Schemas & Artifacts, HDE-CLI-API-Vendor-Ref, Glow QA Guide, and HDE Phased Epics remain the single homes for schemas, CLI command shapes, QA plans, and acceptance wiring for these stateless flows.

* **Non-gating posture.**

  * Until the stateless JSON QA mode is implemented and drained into PF04/PF12/PF19/PF20 with explicit tokens, no PF09 acceptance token or CI job may treat the presence or absence of stateless JSON QA artifacts as a merge-blocking gate.

  * PF09 continues to gate the current DB-backed engine and CLI flows for this slice (BodyGraph, compat, Reader, Aux), as defined elsewhere in this checklist.

* **Documentation discipline.**

  * When the stateless JSON QA epic is created, reference it in this row by title only and update task status, but do not define new transport bytes or schemas here; PF09 only tracks that the epic exists and whether its acceptance tokens are wired.

*Task notes:*  
 This task exists to mirror PF14 §17.9’s non-gating status in PF09. It does not introduce new tokens; any future stateless QA tokens must be defined in HDE-Governance and HDE Phased Epics.

*Epic or card:* Unknown (future stateless JSON QA epic; titles-only)

*Tokens:*  
 None yet; PF14 §17.9 explicitly forbids gating on stateless JSON QA artifacts until a future epic defines tokens. PF09 records the non-gating constraint only.

*Evidence / artifacts:*  
 None; PF09 does not require stateless JSON QA artifacts until the future epic is live.

**Acceptance impact**

* No new tokens are introduced; this row explicitly states that there are *no* stateless JSON QA tokens yet and that none may be treated as gates.

* This aligns PF09 with PF14 §17.9’s requirement that stateless QA mode is informative/non-gating until explicitly wired in Governance/Phased Epics.

**Artifacts impact**

* No new artifact paths are required for this task.

* References to stateless BodyGraph/compat/vendor artifacts and run bundles remain titles-only and single-homed in HDE-Schemas & Artifacts, HDE-CLI-API-Vendor-Ref, Glow QA Guide, and HDE Phased Epics.

## **Task HDE-COAG005 — Interim no-user CLI QA posture (pre-Glow prod)**

*Task ID:* HDE-COAG00Y  
 *Task name/label:* Interim no-user CLI QA posture (pre-Glow prod)  
 *Task status:* Not started

*Task description:*  
 Encode, for PF09, the pre-Glow production CLI QA constraints from PF14 §17.10 and the QA docs, without redefining schemas or transport bytes:

* **Environment assumptions (titles-only).**

  * In pre-Glow production, there is no app-level user model and no persistent user-bound BodyGraph rows configured in the database.

  * Mechanics and QA MUST NOT create app-like user records in production ahead of Glow App integration (see PF14 — HDE-Mechanics Guide §17.10 and Glow QA Guide by title).

* **Compat & Reader Live QA (showcompat).**

  * In pre-Glow prod Live QA, `hdctl showcompat` MUST be exercised with birth arguments only (for example, `--birthdate-a/-b`, `--birthtime-a/-b`, `--location-a/-b`).

  * `--user-a/--user-b` and `--source=db` MUST NOT be used in production QA flows while the app user model is absent.

  * QA MUST continue to verify, for birth-based compat runs:

    * Canonical JSON on stdout (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF), reusing the canonical JSON harness covered by HDE-CALC005 and HDE-CONJ004.

    * AB↔BA identity using swapped birth tuples (AB vs BA), reusing the CLI AB/BA parity harness (`artifacts/cli/ab.json`, `ba.json`, `summary.json`).

    * Reader v1 envelopes via `--dump-reader`, with Reader↔CLI parity proven via the shared presenter/emitter, as governed by PF14 and the CLI parity tasks in this checklist.

* **Aux narratives Live QA (aux-preview).**

  * In pre-Glow prod, `hdctl aux-preview` MUST consume compat JSON produced from birth-based `showcompat` runs as described above; QA MUST NOT rely on DB-backed users to exercise Aux.

  * Aux preview remains a file-based consumer of compat JSON in this mode; narrative IDs and bands are exposed to admins only via governed JSON sidecars, as defined in PF05/PF17/PF18 by title.

* **BodyGraph resolver & vendor ingest (bg:resolve).**

  * In pre-Glow prod, CLI `--user` arguments passed to `bg:resolve` MUST be treated as ephemeral QA keys only (for example, `qa_epic017_resolve1`, `qa_epic017_vendor1`) and MUST NOT be interpreted as real app user IDs.

  * Under rails CLOSED, any `bg:resolve --source=vendor` invocation MUST return a typed refusal and MUST NOT perform outbound HTTP.

  * Under rails OPEN in pre-Glow prod, QA MAY:

    * Run `bg:resolve` DB/auto stub checks that do not create real DB rows.

    * Run `bg:resolve --source=vendor --dry-run` to exercise vendor shaping and ingest metadata without writing DB rows.

  * `bg:resolve --source=vendor --upsert` MUST NOT be invoked in production until a future epic (recorded in HDE Phased Epics and governed by Glow QA Guide) re-opens user-bound DB coverage for environments with a live app user model.

* **Evidence skeleton for CLI QA (pre-Glow prod).**

  * For Live QA sessions in pre-Glow prod that exercise `showcompat`, `aux-preview`, or `bg:resolve`:

    * Mechanics MUST snapshot the Human Evidence Index and Machine Mirror before and after the QA run:

      * `docs/evidence/INDEX.json`

      * `docs/evidence/INDEX.sha256`

      * `artifacts/evidence_index.jsonl`

      * governed `*.path_proof.txt` records

    * Any mutation of these governed evidence artifacts during such QA runs MUST be treated as a defect or unexpected side effect.

    * CLI QA flows in this mode MUST NOT write governed evidence artifacts directly; they only consume the evidence skeleton defined elsewhere in this checklist (HDE-COAG001 and HDE-DIST001) and in PF12/PF14.

* **Forward plan (routing only; titles-only).**

  * Once the Glow App and user model are integrated, a future epic recorded in HDE Phased Epics and governed by the Glow QA Guide will:

    * Use real app user IDs to exercise DB-backed `showcompat` and `bg:resolve --source=vendor --upsert` in prod or stage.

    * Close out any acceptance tokens that currently depend on DB-backed user flows, routing to HDE-Governance/HDE Phased Epics by title.

  * Until that epic is live, QA requirements that assume “existing users in prod” MUST be treated as blocked by environment and satisfied instead using the no-user QA mode recorded in this task.

*Task notes:*

* PF09 does not define new CLI commands, flags, or schemas here; those remain single-homed in PF05, PF12, PF14, PF19, and PF20 by title.

* This task ties the pre-Glow no-user QA posture for CLI to concrete checklist expectations without changing long-term DB-backed semantics.

*Epic or card:* Unknown (pre-Glow QA epic; titles-only)

*Tokens (titles-only; semantics live in Governance/QA docs):*

* This row primarily reuses existing tokens and environment constraints:

  * Rails and env pins: `SAFE_RAILS_DEFAULT_OK`, `ENV_LC_ALL_C_OK`, `ENV_TZ_UTC_OK` (already referenced elsewhere in PF09).

  * Canonical JSON and parity: `JSON_CANONICAL_CHECK_OK`, `CLI_AB_BA_PARITY_OK`, `CLI_TWO_RUN_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`.

  * Evidence discipline: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

* If Governance adds a dedicated “NO\_USER\_QA\_MODE\_OK” token in future, this task should reference it by title only.

*Evidence / artifacts (titles/paths only):*

* For compat & Aux QA:

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json`

  * `artifacts/cli/summary.json`

  * `artifacts/cli/narrative/stdout.txt` (Aux preview text; titles-only)

  * `artifacts/cli/narrative/sidecar.json` (Aux preview IDs-only JSON sidecar)

* Evidence skeleton (snapshots, read-only posture):

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  * governed `*.path_proof.txt` (paths and schemas single-homed in HDE-Schemas & Artifacts)  
