**Title**: PF20 — HDE Phased Epics Map

**Status:** Canon

**Version:** v0.2

**Effective Date:** 2025-11-21

**Last Update Gate:** HDE-EPOC017

## **0\. Purpose & Scope**

This document is the **single PF home** for:

* Mapping each **HDE epic** to an **alchemical phase** (Calcination → Coagulation) as defined in **7 Phases of Alchemical Engineering** (PF21, titles‑only).  
* Tracking **per‑epic intent, deliverables, PF references, acceptance tokens, and evidence pointers**, in a form that can be mirrored on JSON boards and JIRA.  
* Recording **cross‑epic “Outstanding issues”** that must be explicitly carried forward or closed.

This document does **not** redefine:

* Math or token semantics (PF01, PF04).  
* Epic execution flow (PF06), build/CI wiring (PF09), or QA playbooks (PF19).

Those remain single homes; PF20 only **names and tracks** epics, phases, and evidence outcomes.

---

## **1\. Outstanding Issues (Cross‑Epic)**

Use this section to track **open, cross‑cutting issues** that may span multiple epics and phases.

Each issue row should be **short, factual, and testable**.

**Issue record template**

* **Issue ID:** `ISSUE-XXX`  
* **Issue name:**  
* **Description:**  
* **Acceptance:** (what specific observation/test proves this is resolved)  
* **Mapped alchemical phase(s):** (e.g. `Calcination`, `Distillation + Coagulation`)  
* **Linked epics:** (IDs only, e.g. `HDE-EPIC017, HDE-EPIC019`)  
* **Evidence pointer(s):** (titles-only, e.g. “PF10 — HDE Build Notes, entry ‘ISSUE-XXX’”; “docs/evidence/INDEX.json entry ‘ISSUE-XXX snapshot’”)

*(No issues populated yet — PO/Scrum Master will add as they emerge.)*

---

## **2\. Epic Records (Per‑Epic Tracking)**

Each epic tracked in PF20 **MUST** have exactly one “Epic record” in this section.

* The **phase** is chosen from PF21’s 7 phases (titles-only).  
* Each epic record is **append‑only**; corrections happen via new PF20 changes, not by rewriting history silently.  
* JIRA/JSON boards **mirror** this mapping but do not replace it.

  ### **2.1 Epic Record Template (Normative)**

For every epic, fill out the following fields as the **canonical PF20 record**.

#### **2.1.1 Meta**

* **Epic ID:** `HDE-EPICXXX`  
* **Epic name (short):**  
* **Alchemical phase:** (exact phase name per PF21, e.g. `Calcination`, `Dissolution`, …)  
* **Phase rationale (1–3 sentences):** Why this epic belongs in this phase.  
* **Related boards:** (JIRA epic key(s), JSON board lane/card IDs if needed)  
* **Status:** `Planned | In Progress | Blocked | Done | Won’t Do | Superseded`  
* **Date started:** `YYYY‑MM‑DD`  
* **Date completed:** `YYYY‑MM‑DD` (or `TBD`)  
* **Owner(s):** Lead Dev, IA, PO (names/roles only, consistent with PF06 roles).

  #### **2.1.2 Existing Work Check (MUST)**

Before any new implementation work is planned or started for this epic:

* **Existing features review (summary):**  
  * What features, flows, or components already cover part of this intent?  
  * What prior epics or PF10 build notes are relevant (titles/IDs only)?  
* **Existing tokens validated:**  
  * List **acceptance tokens** already satisfied that this epic will **reuse**, not re‑prove (names-only, e.g. `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`).  
* **Existing evidence located:**  
  * Pointers by title to relevant artifacts and index/mirror records (e.g. “Machine mirror record for `artifact_key=reader_a7_headers`”).  
* **Gap statement:**  
  * Short bullet list of what **remains unproven** or **drifts** that this epic is explicitly meant to address.

**Rule (normative):**

No new work is scoped for this epic until the Existing Work Check is filled in and reviewed. This applies to **features, tokens, and evidence**. If this section is blank or obviously stale, the epic is **not ready** to enter “In Progress”.

#### **2.1.3 Deliverables (Jobs To Be Done)**

List **concrete, observable deliverables**; each should be testable:

* **Deliverable D1:**  
  * *Job to be done:*  
  * *Evidence required:* (artifact titles, mirror records, snapshots; titles-only)  
  * *PF references:* (PF titles \+ sections, e.g. “PF14 — HDE Mechanics Guide §1.3 Evidence & CI coupling”)

Repeat D2, D3, … as needed.

These deliverables should map cleanly to PF06 PR plans, PF09 CI jobs, and PF19 QA playbooks (titles-only).

#### **2.1.4 PF Reference Map**

Summarize **which PF docs and sections this epic leans on** (no duplicated bytes):

* **Core:**  
  * PF21 — 7 Phases of Alchemical Engineering (§phase used)  
  * PF06 — Epic Process Guide (§0.4 Execution posture and flow; §2.x as applicable)  
  * PF09 — HDE Build Checklist (pre/post‑commit CI gates; titles-only)  
  * PF19 — Glow QA Guide (§2 Pre‑commit QA; §5 Component playbooks; §11 Roles)  
* **Additional (as needed):**  
  * PF01 — HDE Math Spec  
  * PF02 — HDE Architecture  
  * PF04 — HDE Governance  
  * PF05 — HDE CLI‑API‑Vendor Ref  
  * PF12 — HDE Schemas & Artifacts  
  * PF14 — HDE Mechanics Guide  
  * PF17 — HDE Narratives Guide

Only **list titles and sections** here; do not restate content.

#### **2.1.5 Tokens and Evidence (Acceptance)**

This is the **names‑only acceptance roster** plus pointers to evidence surfaces.

* **Required baseline tokens (always for epic close):**

  * `PR_OPENED_OK` (PF06)  
  * `TESTS_PASS_OK`  
  * `DOC_DELTA_PRESENT_OK`  
  * `EVIDENCE_INDEX_UPDATED_OK`  
  * `MACHINE_MIRROR_UPDATED_OK`  
  * `EVIDENCE_INDEX_HASH_OK` (if applicable per PF09/PF12)  
* **QA rail tokens (open/close, both pre and post‑commit on final PR):**

  * `QA_PRECOMMIT_CHECKLIST_OK` (PF19)  
  * `QA_POSTCOMMIT_CHECKLIST_OK` (PF19)  
  * `ENV_RAILS_POLICY_OK` (PF04; closed refusal / open conformance).  
* **Phase‑specific tokens:**

  * List any additional acceptance tokens required by this epic’s design (names-only), e.g.  
    * Calcination: tokens that prove **audit and kill‑list of drift/debt**.  
    * Distillation: tokens that prove **refactors and repeatability**.  
    * Coagulation: tokens that prove **solidified, release‑grade posture**.  
  * Actual semantics live in PF04/PF09/PF12/PF19, not here.  
* **Evidence pointers (titles-only):**

  * Human Evidence Index: `docs/evidence/INDEX.json` record titles.  
  * Hash sentinel: `docs/evidence/INDEX.sha256`.  
  * Machine Mirror: `artifacts/evidence_index.jsonl` records (artifact\_key \+ proof\_anchor).  
  * Close pack: `audit/EPIC-<ID>_close_report.md`, `audit/EPIC-<ID>_MANIFEST.json` (titles-only; schema in PF12).

**Rule (normative):**

An epic is not marked **Done** in PF20 until:

1. all required acceptance tokens for that epic are listed here, and  
2. each token has corresponding evidence indexed in the **human Evidence Index** and **machine mirror** in the same PR, per PF06/PF09/PF12/PF19.

   #### **2.1.6 QA Rails — Open/Close (Final PR)**

For the **final PR** that closes the epic:

* **Pre‑commit / CI (rails posture):**

  * Confirm pre‑commit rails checks ran with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default (PF19).  
  * Document any job that opened rails and the evidence it produced and indexed in the same PR.  
* **Post‑commit (final proof run):**

  * Record the rails configuration used for final QA runs.  
  * Capture and index evidence for **closed refusal** and **open conformance** as required by PF04/PF19.  
* **Tokens (names-only, example set):**

  * `QA_PRECOMMIT_CHECKLIST_OK`  
  * `QA_POSTCOMMIT_CHECKLIST_OK`  
  * `ENV_RAILS_POLICY_OK`  
  * Any additional rails‑specific tokens defined in PF04/PF09/PF19, as applicable.

  #### **2.1.7 Issues Not Done (Epic‑Scoped)**

When closing an epic:

* **Issues completed:** (short list, linking to “Outstanding Issues” where relevant)  
* **Issues not done / out‑of‑scope:**  
  * For each, note whether it:  
    * moves to **another epic** (ID),  
    * becomes a **new ISSUE‑XXX** in §1,  
    * or is explicitly **dropped** (with a one‑line rationale).

**Rule (normative):**

No epic is closed as “Done” while silently dropping known issues. Every known issue must be: proved, carried forward, or explicitly dropped in this section.

---

Here’s a PF20-ready epic record for **HDE-EPIC017 — HD Calcination Pass 2**, following the template in §2.1.

You can drop this under `### 2.2 HDE-EPIC017 — HD Calcination Pass 2` in PF20 and use it as the first non-placeholder epic.

---

### **2.2 HDE-EPIC017 — HD Calcination Pass 2**

#### **2.2.1 Meta**

* **Epic ID:** `HDE-EPIC017`

* **Epic name (short):** HD Calcination Pass 2

* **Alchemical phase:** Calcination (Foundations first)

* **Phase rationale (1–3 sentences):**

  * PF09 Phase I shows that core foundations such as the canonical serializer, evidence indices, config system, and total-order module are specified but not fully implemented or evidenced.

  * This epic “burns down” drift and partial implementations around those foundations: it either proves them with passing tokens and indexed evidence or removes/rewrites what cannot be justified.

  * The result is a smaller, harder base: one serializer/emitter, one evidence system, one config loader, and one order module that the rest of the engine can safely build on.

* **Related boards:**

  * Glow Dev Board (HD Engine) — card `HDE-EPIC017`, lane `PLAN`.

* **Status:** `Planned`

* **Date started:** `TBD`

* **Date completed:** `TBD`

* **Owner(s):**

  * Lead Dev: Isis

  * Scrum Master: Master Scrum

  * CRD authority: Thoth

  * QA stewardship: Glow QA Guide (PF19)

  ---

  #### **2.2.2 Existing Work Check (MUST)**

**Existing features and specs**

* **Canonical Enumerations Registry — Done (PF09 Phase I).**

  * Centers, gates, channels, and Magic-10 categories are frozen in canon under the topology and Magic-10 catalogs in HDE-Schemas & Artifacts.

  * Mechanics already has a registry job that validates domains against schemas and emits a domain snapshot and closure report.

* **Canonical JSON, idempotence, and serializer rules — Specified.**

  * Math and transport already define canonical JSON (UTF-8, sorted keys, compact, exactly one trailing LF) and the preimage/idempotence recipe for `idempotence_hash`.

  * Architecture and Mechanics already require a **single presenter/emitter** for Reader and CLI, no ad-hoc serializers, and AB↔BA / two-run identity.

* **Evidence Index and mirror discipline — Specified.**

  * PF09/PF12 pin the human Evidence Index at `docs/evidence/INDEX.json`, the hash sentinel at `docs/evidence/INDEX.sha256`, and the machine mirror at `artifacts/evidence_index.jsonl`, including canonical JSONL, field order, sort-before-write, 1:1 parity, and path-proofs.

* **Programmatic Configuration and registry report — Specified.**

  * PF12 and PF14 define catalog ownership and loader behavior; PF09 Phase I lists a required registry report at `artifacts/registry/registry_report.json` and unknown-ID hard-fail semantics.

* **Deterministic tie-break and total-order rules — Specified.**

  * PF01 and PF14 define comparator policy for IDs, channels (`NN–NN` min-first), and Magic-10 categories, plus helper functions (`dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`) and property-test requirements.

* **EPIC011 outcome and epic map reset.**

  * PF10 Addendum 1 marks HDE-EPIC011 as failed, retires PF16 as an active epic map, and designates PF20 as the new single home for epic planning.

  * The board already records HDE-EPIC011 as `CANCELED` (Failed) and HDE-EPIC012–014 as `CANCELED` (“Won’t Do”).

**Existing tokens validated (reused, not re-proved)**

These tokens are considered foundational and will be **reused**, not re-designed, in this epic:

* Domain/registry: `CATALOG_DOMAIN_CLOSED_OK`, `MAGIC10_DOMAIN_CLOSED_OK`, `M10_DEFS_OK`, `CATALOG_ORIENTATION_CANON_OK`.

* Evidence discipline: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_HASH_OK`.

This epic will **prove or re-prove** determinism and serializer/evidence tokens where PF09 Phase I explicitly shows gaps.

**Existing evidence located (by title only)**

* Domain snapshot, closure report, and registry checksums for topology catalogs (centers/gates/channels/categories).

* Initial canonical-JSON and emitter determinism logs (`json_canonical_check.log`, `json_canon_compare.log`, serializer grep-guard, emitter symbol proof), though currently not backed by all required tokens in PF09 Phase I.

**Gap statement (explicit)**

PF09 Phase I marks the following as **Not done** (no passing evidence or complete token rosters):

* **Canonical Serialization Package** — spec exists, but we lack a complete, tested implementation with:

  * single emitter proof (Reader \+ CLI),

  * canonical JSON enforcement,

  * AB↔BA and two-run identity,

  * CLI stdout discipline.

* **Repository & Tooling Skeleton** — evidence indices and mirror not actually present and wired; no enforced registry report or topology orientation demo; no same-PR parity.

* **Programmatic Configuration System** — no implemented loader with unknown-ID hard-fail, alias policy, and registry report wired into indices.

* **Deterministic Tie-Break & Total-Order Module** — comparator helpers and related property tests not wired; no canonical ordering artifacts indexed.

EPIC017 is defined to address **exactly these Phase I gaps** plus any drift that accrued while EPIC011 was in flight.

---

#### **2.2.3 Deliverables (Jobs To Be Done)**

**Deliverable D1 — Canonical Serialization Package implemented and evidenced**

* *Job to be done:*  
   Make the **single presenter/emitter** the only public JSON path for Reader, CLI, and governed JSON artifacts, with canonical JSON, AB↔BA, and two-run identity proved and indexed.

* *Evidence required (titles-only):*

  * Grep-guard for ad-hoc serializers (no `json.dumps/jsonify` on public paths).

  * Emitter symbol proof (Reader and CLI call the same emitter).

  * Canonical JSON check and canonical re-serialization compare logs.

  * AB↔BA and two-run identity logs.

  * CLI stdout snapshot for `showcompat` (six-key body, one LF).

* *PF references:* PF01 — HDE-Math-Spec (idempotence, bands), PF02 — HDE Architecture (single emitter), PF05 — HDE-CLI-API-Vendor-Ref (Reader/CLI bytes), PF12 — HDE-Schemas & Artifacts (canonical JSON), PF14 — HDE-Mechanics Guide (serializer tasks), PF09 — HDE-Build Checklist §Phase I.

  ---

**Deliverable D2 — Repository & Tooling Skeleton wired to indices and mirror**

* *Job to be done:*  
   Provide a minimal but complete **evidence skeleton**: human Evidence Index, hash sentinel, machine mirror, registry report, and topology orientation demo, all updated in the same PR and enforced in CI.

* *Evidence required (titles-only):*

  * Human Evidence Index (`docs/evidence/INDEX.json`) with updated entries.

  * Hash sentinel (`docs/evidence/INDEX.sha256`) recomputed.

  * Machine mirror (`artifacts/evidence_index.jsonl`) with canonical JSONL, exact field order, sort-before-write, unknown-key rejection, and path-proofs.

  * Registry report (`artifacts/registry/registry_report.json`) produced each run.

  * Topology orientation demo (`audit/gates/topology/orientation_demo.txt`).

* *PF references:* PF12 — HDE-Schemas & Artifacts (Index/mirror schema), PF09 — HDE-Build Checklist (Phase I tasks, A7 surface), PF14 — HDE-Mechanics Guide (evidence pipeline), PF04 — HDE-Governance (tokens).

  ---

**Deliverable D3 — Programmatic Configuration System with hard-fail and registry report**

* *Job to be done:*  
   Implement a **typed config loader** for HDE catalogs that hard-fails on unknown IDs, applies explicit alias policy, and emits a canonical JSON registry report that is indexed in both human and machine evidence indices.

* *Evidence required (titles-only):*

  * Loader tests showing unknown-ID hard-fail behavior.

  * Alias-policy tests (OFF by default; ON uses allow-lists only).

  * Registry report artifact (`artifacts/registry/registry_report.json`) and its Index/mirror entries.

* *PF references:* PF12 — HDE-Schemas & Artifacts (catalogs), PF14 — HDE-Mechanics Guide §3 (configuration system), PF09 — HDE-Build Checklist Phase I, PF04 — HDE-Governance (acceptance tokens).

  ---

**Deliverable D4 — Deterministic Tie-Break & Total-Order Module**

* *Job to be done:*  
   Provide reusable comparators and helpers that impose a **total, deterministic order** over IDs, channels, categories, and arrays-as-sets, and prove antisymmetry, transitivity, totality, AB↔BA identity, and two-run identity with indexed artifacts.

* *Evidence required (titles-only):*

  * Comparator property-test logs (`props_total_order.log`).

  * Channel order snapshot (`channels_sorted.snapshot.json`).

  * Category iteration snapshot (`categories_iter.snapshot.json`).

  * AB↔BA identity bytes (`abba_identity.bytes`).

* *PF references:* PF01 — HDE-Math-Spec (ordering semantics), PF14 — HDE-Mechanics Guide §5 (comparator policy), PF12 — HDE-Schemas & Artifacts (channel/catalog constraints), PF09 — HDE-Build Checklist Phase I.

  ---

**Deliverable D5 — PF09 Phase I reconciled and EPIC011 debt explicitly parked**

* *Job to be done:*  
   Bring PF09 Phase I into alignment with reality by marking Canonical Serialization, Repository & Tooling Skeleton, Programmatic Configuration System, and Total-Order Module as **Done** (with evidence) or explicitly moving remaining items to later phases/epics in PF20, with clear ISSUE IDs.

* *Evidence required (titles-only):*

  * PF09 redlines reflecting updated statuses and pointers to PF20/HDE-EPIC017.

  * PF10 Build Notes entry confirming Addendum 1 has been drained to PF16/PF20 and that EPIC011 remains failed but fully documented.

  ---

  #### **2.2.4 PF Reference Map**

* **Core:**

  * PF21 — 7 Phases of Alchemical Engineering (Calcination definition).

  * PF09 — HDE-Build Checklist (Phase I — Calcination “Foundations first”).

  * PF06 — Epic Process Guide (PR-first, same-PR evidence parity).

  * PF19 — Glow QA Guide (pre/post-commit QA rail, env pins, A7 catalog posture).

* **Additional:**

  * PF01 — HDE-Math-Spec (canonical JSON, idempotence, ordering, bands).

  * PF02 — HDE Architecture (single emitter, engine/adapter/presenter boundaries).

  * PF04 — HDE-Governance (token registry, A7, evidence policy).

  * PF05 — HDE-CLI-API-Vendor-Ref (Reader/CLI transport bytes, CLI stream rules).

  * PF12 — HDE-Schemas & Artifacts (catalogs, manifest, Evidence Index & mirror schema).

  * PF14 — HDE-Mechanics Guide (serializer, config loader, comparators, evidence jobs).

  * PF10 — HDE-Build Notes (EPIC011 failure and PF16 retirement addenda).

  * PF16 — HD Engine Epics Map (historical only; EPIC011 failed, EPIC012+ won’t-do).

  * PF20 — HDE Phased Epics Map (this document; epic tracking and phase mapping).

  ---

  #### **2.2.5 Tokens and Evidence (Acceptance)**

**Baseline PR tokens (always for epic close)**

* `PR_OPENED_OK`

* `TESTS_PASS_OK`

* `DOC_DELTA_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

**Phase-specific tokens (Calcination; foundations hardened)**

For EPIC017, the epic is considered **Done** only when at least these tokens are green and backed by indexed evidence:

* **Canonical Serialization Package:**

  * `CLI_NO_ALT_JSON_OK`

  * `CLI_READER_PARITY_OK` (supersedes older parity names)

  * `CLI_SHOWCOMPAT_CANON_OK`

  * `CLI_STDOUT_LF_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

  * `COMPOSITE_ABBA_IDENTITY_OK`

* **Evidence indices & mirror:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

* **Programmatic Configuration System:**

  * `CONFIG_GEN_OK`

  * `UNKNOWN_IDS_FAIL_CLOSED_OK` (or the chosen canonical name for this behavior)

  * `JSON_CANONICAL_CHECK_OK` (registry report)

* **Deterministic Tie-Break & Total-Order:**

  * `TIEBREAK_TOTAL_ORDER_OK` (or equivalent ordering token)

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

**Evidence pointers (titles-only)**

* Human Evidence Index and sentinel:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

* Machine mirror:

  * `artifacts/evidence_index.jsonl`

* Canonical serializer evidence:

  * `audit/gates/canonical_json/json_canonical_check.log`

  * `audit/gates/canonical_json/json_canon_compare.log`

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

* Registry & config evidence:

  * `artifacts/registry/registry_report.json`

* Order/comparator evidence:

  * `artifacts/engine/order/props_total_order.log`

  * `artifacts/engine/order/channels_sorted.snapshot.json`

  * `artifacts/engine/order/categories_iter.snapshot.json`

  * `artifacts/engine/order/abba_identity.bytes`

All of the above must be present in **both** the human Index and machine mirror (with path-proofs) in the epic’s closing PR.

---

#### **2.2.6 QA Rails — Open/Close (Final PR)**

* **Pre-commit / CI posture:**

  * CI and pre-commit runs for this epic use **closed rails by default**: `SAFE_MODE=1`, `ALLOW_NETWORK=0`. No vendor calls are expected for this epic.

  * Any job that opens rails (e.g., for DB connectivity checks) must attach governed evidence and be clearly marked; by default, EPIC017 should keep all work strictly local and deterministic.

* **Determinism pins:**

  * All serializer, comparator, and evidence jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* **Post-commit (final proof run):**

  * Run the full Phase I harness once in a representative environment, collecting:

    * serializer/emitter proofs,

    * registry report and domain closure proofs,

    * A7-adjacent evidence where relevant (using Catalog JSON success only), while keeping Aux and `/internal/version` under their existing non-A7 governance.

* **QA tokens for rails:**

  * `QA_PRECOMMIT_CHECKLIST_OK`

  * `QA_POSTCOMMIT_CHECKLIST_OK`

  * `ENV_RAILS_POLICY_OK`

  ---

  #### **2.2.7 Issues Not Done (Epic-Scoped)**

To close HDE-EPIC017, the epic report must explicitly account for any unresolved Phase I items:

* **Issues completed:**

  * List ISSUE-IDs (from PF20 §1 Outstanding Issues) that were fully resolved here, e.g.:

    * `ISSUE-001` — “Serializer drift vs PF05 bytes” — resolved by single-emitter proof.

    * `ISSUE-002` — “Evidence Index vs mirror parity gaps” — resolved by PF12-compliant mirror.

* **Issues not done / out-of-scope:**

  * Items that remain open after EPIC017 must be handled as follows:

    * Moved to a later phase epic (e.g. a Distillation epic that focuses on performance/caching).

    * Promoted to a new ISSUE-ID in PF20 §1 (cross-epic).

    * Explicitly dropped with a one-line rationale (“no longer aligned with current product scope”).

* **Known exclusions for EPIC017:**

  * Performance & cache distillation (previously EPIC012) remains out of scope and will be handled, if at all, in a future Distillation-phase epic.

  * Release & provenance packaging (previously EPIC013) and SDK/Admin-UI work (EPIC014) are explicitly “Won’t Do” under the old map; any revival must come as new epics under PF20, not as trailing work in EPIC017.

No issue is allowed to “disappear” at close: each must be proved, carried forward, or explicitly dropped in this section and in PF20 §1.

