**Title**: PF20-Canon-HDE-Phased Epics

**Status:** Canon

**Version:** v1.0.8

**Effective Date:** 2025-11-26

**Last Update Gate:** HDE-EPIC018 Addtion

**Invocation tag:** INV-f2ac55d77ce9aacc

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
  ---

Issue record: ISSUE-017-NO-USER-QA \<allocated\>

Issue record: ISSUE-017-STATELESS-JSON-QA \<allocated\>

Issue record: ISSUE-QA-TOKENS-LIBRARY \<allocated\>

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
  * When an epic uses CLI serializer/emitter guards as part of its acceptance (for example, a Calcination epic that hardens the Canonical Serialization Package), the canonical evidence paths for those guards MUST be `artifacts/cli/guards/serializer_grep_guard.log` and `artifacts/cli/guards/emitter_symbol_proof.txt`. Any `audit/gates/guards/…` copies are considered legacy/auxiliary and are not required for epic acceptance.

**Rule (normative):**

An epic is not marked **Done** in PF20 until:

1. all required acceptance tokens for that epic are listed here, and  
2. each token has corresponding evidence indexed in the **human Evidence Index** and **machine mirror** in the same PR, per PF06/PF09/PF12/PF19.

**QA Acceptance Tokens Library integration (PF19 §9A)**

For QA-oriented acceptance tokens, this document is a **consumer** of the QA Acceptance Tokens Registry defined in PF19 — Glow QA Guide §9A:

* The **semantic home** for QA acceptance tokens (names, scope, QA definitions, and evidence mappings) is the QA Acceptance Tokens Registry in PF19 §9A. PF19 defines the token metadata model and lists concrete tokens grouped by scope (pre-commit/CI, evidence, A7/transport, Aux, CLI/API & SDKs, App-layer).

* PF20 epic records **MUST** treat QA acceptance tokens as **names-only roster entries** that point into PF19 §9A (and, where applicable, to PF04/PF09/PF12 for governance, build, or schema details). EPIC sections in this document **MUST NOT** redefine QA token semantics locally.

* For each EPIC, §2.1.5 and the EPIC-specific “Tokens and Evidence (Acceptance)” subsection **SHOULD**:

  * list required QA tokens by **canonical name** from the PF19 §9A registry;

  * indicate their scope (for example “pre-commit/CI”, “post-commit/live QA”, “evidence”, “transport/A7”, “App-layer”); and

  * provide titles-only evidence pointers (for example to PF19 playbooks and PF12/PF09 artifacts) that show how the EPIC proves each token.

For legacy EPIC records that pre-date PF19 §9A, any future edits **MUST** move them toward this pattern instead of copying or restating token semantics inside PF20.

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

  #### **2.1.7 Tracked Issues**

When closing an epic, the epic record MUST include a list of **tracked intra-epic issues** and their final status for this epic. 

In this document, an **issue** is any *unexpected* condition, behavior, gap, or risk discovered during implementation or QA, not a synonym for “deliverable” or “task.” An issue exists when reality diverges from the current plan or canon (for example: failing or flaky tests, ambiguous or conflicting specs, misaligned tools, missing or inconsistent evidence, surprising runtime behavior, or hard environment constraints such as “no user IDs in prod”). Planned work items, epics, and deliverables do **not** automatically become issues just because they are incomplete; they are tracked as issues only when there is something structurally blocking, surprising, or unclear about them (for example: “cannot be done under current rails,” “spec is incomplete,” or “tooling cannot represent required behavior”).

Every tracked issue must end the epic in one of these states:

* **Completed under this epic**

* **Carried forward to another epic** (with a concrete epic ID)

* **Promoted to a cross-epic issue** (ISSUE-XXX in §1 “Outstanding Issues”)

* **Explicitly dropped** (with a one-line rationale)

For each tracked intra-epic issue, the epic record SHOULD provide at least:

* **Issue ID** (e.g. `ISSUE-<EPIC>-<NAME>` or a short label if no ID is minted)

* **Title** (short, descriptive name)

* **Status** (for example: `Completed under <EPIC-ID>`, `Carried forward to <EPIC-ID>`, `Cross-epic ISSUE-XXX`, `Dropped`)

* **Scope / description** (1–3 sentences explaining what the issue covers)

* **Disposition for this epic** (brief note describing what happened to this issue in this epic: proved, carried forward, cross-epic, or dropped)

When listing issues:

* **Issues completed:**

  * Short list of issues whose **Status** is “Completed under \<EPIC-ID\>,” linking to §1 “Outstanding Issues (Cross-Epic)” where relevant.

* **Issues not done / out-of-scope:**

  * For each, make the disposition explicit:

    * **Moves to another epic:** name the destination epic ID.

    * **Becomes a new cross-epic issue:** give the ISSUE-XXX ID in §1.

    * **Explicitly dropped:** include a one-line rationale (“no longer aligned with current product scope,” etc.).

**Rule (normative):**  
 No epic is closed as “Done” while silently dropping known issues. Every known issue must be: **proved, carried forward, promoted to a cross-epic ISSUE-XXX, or explicitly dropped** in this section, with statuses and destinations clearly recorded.

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

* **Status: `Closed`**

* **Deliverables: D1–D4 Done, D5 Completed (manifest \+ close report \+ doc-deltas); EPIC011 ingest remains parked for a future epic.**

* **Date started: `2025.11.21`**

* **Date completed: 2025.11.26**

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

*Evidence required (titles‑only):*

* Grep‑guard for ad‑hoc serializers on governed paths (no `json.dumps` / `jsonify` outside the canonical serializer and explicitly whitelisted admin dumps).

* Emitter symbol proof showing that Reader v1 and CLI compat use the single presenter/emitter path.

* Canonical JSON check and canonical re‑serialization compare logs for the shared serializer/emitter.

* EPIC017 CLI canonicalization harness artifacts proving AB↔BA parity, two‑run identity, Reader/CLI parity, and preimage recompute for `hdctl showcompat`; concretely:

  * CLI AB/BA parity set — artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/cli/summary.json (AB↔BA hashes and equality flags).

  * Reader dump snapshot — artifacts/cli/reader\_dump.json.

  * Reader↔CLI parity bytes — artifacts/cli/reader\_cli\_parity.bytes.

  * Preimage recompute log — artifacts/cli/preimage\_recompute.log.

  * Serializer/emitter guard logs — artifacts/cli/guards/serializer\_grep\_guard.log, artifacts/cli/guards/emitter\_symbol\_proof.txt.

* CLI stdout snapshot for `hdctl showcompat` compat JSON (LF‑terminated canonical JSON; non‑empty) captured under closed rails, with the corresponding entries present in the human Evidence Index and machine mirror in the same PR.

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

* Evidence tests & CI harness (titles-only) — `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_orientation_demo.py`, and `ci/checks/check_mirror_schema.sh` (or their successors), executed under rails-closed environment (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) to enforce coherence and freshness of INDEX, sentinel, mirror, path-proofs, and the topology orientation demo for this epic.

  ---

**Deliverable D3 — Programmatic Configuration System & `registry_report.v1`**

* *Job to be done:*  
   Implement a PF12-aligned, typed configuration loader for the HDE catalogs and manifest that hard-fails on unknown/duplicate IDs and enforces explicit alias policy, and generate a canonical `registry_report.v1` on every run, wired into the Evidence Index and Machine Mirror.

* *Evidence required (titles-only):*

  * **Loader behavior:**

    * `engine.config.registry_loader` — typed registry loader that:

      * Loads `gates_v1.json`, `channels_v1.json`, `magic10.json`, `magic10_caps.json`, `magic10_seeds.json`, and `manifest.json` (PF12 §2/§6).

      * Raises `UnknownIdError`, `DuplicateIdError`, `AliasPolicyError`, `SchemaValidationError` on unknown IDs, duplicates, malformed records, or alias policy violations.

      * Enforces alias policy OFF by default; when `allow_aliases=True`, validates `alias_ledger` and ensures alias targets exist in the canonical channel set.

    * `tests/config/` loader tests (titles-only), including:

      * unknown-ID and duplicate-ID failure cases;

      * alias-policy OFF vs allow-list behavior (`tests/config/test_alias_policy_enforcement.py`).

  * **Registry report generation & determinism:**

    * `tools/generate_registry_report.py` — programmatic generator for `registry_report.v1` that:

      * Uses the canonical serializer (UTF-8, sorted keys, compact, one LF);

      * Computes a stable `generated_at_utc` using `SOURCE_DATE_EPOCH` if set, or reuses an existing `generated_at_utc` to guarantee two-run identity for unchanged inputs;

      * Populates `artifacts/registry/registry_report.json` with:

        * `schema: "registry_report.v1"`;

        * `inputs` summarizing catalogs and manifest (`path/sha256/size/count`);

        * `artifacts.registry` with `channel_ids`, `gate_centers`, `centers`, `domains`, `domain_counts`, `magic10` (order/caps/seeds), and `alias_policy{mode:"off|allow_list", aliases{alias→canonical_id}}`;

    * `artifacts/registry/registry_report.json` — LF-terminated canonical JSON file, schema and field shapes per PF12;

    * `artifacts/registry/registry_report.json.path_proof.txt` — path-proof transcript for the report (path, sha256, size\_bytes, produced\_at\_utc; mtime semantics governed by PF12/PF19);

    * `docs/evidence/INDEX.json` record for `artifact_key:"registry.registry_report"` and `discovered_physical_path:"artifacts/registry/registry_report.json"`, plus corresponding `artifacts/evidence_index.jsonl` record with `role:"snapshot"` and `proof_anchor:"artifacts/registry/registry_report.json.path_proof.txt"`.  
    * `tests/config/test_registry_report_determinism.py` and related config tests — assert `schema:"registry_report.v1"`, canonical JSON form, and byte-for-byte two-run identity and SHA-256 stability;  
    * `tests/evidence/test_evidence_skeleton.py`, `tests/ops/test_evidence_index.py` — verify SHA/size consistency across artifact, Index entry, Mirror record, and path-proof for `registry_report`.

* *PF references:* PF12 — HDE-Schemas & Artifacts (§2, §4, §8.5-8.6), PF14 — HDE-Mechanics Guide §3 (Programmatic Configuration System), PF09 — HDE-Build Checklist (Phase I Programmatic Config tasks), PF04 — HDE-Governance (CONFIG/UNKNOWN-ID token semantics).  
  ---

**Deliverable D4 — Deterministic Tie-Break & Total-Order Module**

* *Job to be done:*  
   Provide reusable comparators and helpers that impose a **total, deterministic order** over IDs, channels, Magic-10 categories, and arrays-as-sets, and prove antisymmetry, transitivity, AB↔BA parity, and two-run identity for ordering artifacts, with evidence wired into the Index/Mirror and enforced by CI.

* *Evidence required (titles-only):*

  * **Ordering layer and artifacts (delivered in WS-D3/WS-D4):**

    * `engine/order/` module(s) implementing comparator and helper functions (`normalize_channel_id`, `dedupe_and_sort_categories`, `canonical_order`, etc.).

    * `tools/generate_registry_report.py` and `tools/order/generate_order_signatures.py` / `scripts/cli/canonical_harness.py` (titles-only) — harnesses that drive AB↔BA and two-run checks for ordering and compat output.

    * Ordering artifacts (generator-owned), as defined in PF12/PF09 and present under `artifacts/engine/order/**`:

      * `artifacts/engine/order/channels_sorted.json` or `channels_sorted.snapshot.json` — canonical channel order snapshot;

      * `artifacts/engine/order/categories_iter.json` or `categories_iter.snapshot.json` — Magic-10 category iteration snapshot;

      * `artifacts/engine/order/props_total_order.log` — comparator property-test log;

      * `artifacts/engine/abba_identity.bytes` — AB↔BA identity evidence.

* **Evidence wiring & CI harness (delivered in WS-D4b; NEW CANON semantics for mtime\_utc):**

  * **Human Index & sentinel** — `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256` updated with entries for all ordering artifacts (`artifact_key` / `discovered_physical_path` pairs for each `artifacts/engine/order/**` artifact), in the same PR as the artifacts and mirror updates.

  * **Machine Mirror records** — `artifacts/evidence_index.jsonl` records for ordering artifacts, each including a `proof_anchor` to the corresponding `*.path_proof.txt` transcript. Mirror schema, field set, and unknown-key rejection follow PF12’s Machine Mirror rules; records are canonical JSONL (UTF-8, sorted keys, compact, exactly one LF).

  * **Path-proof transcripts** — one `*.path_proof.txt` per ordering artifact (`channels_sorted.snapshot.json`, `categories_iter.snapshot.json`, `props_total_order.log`, `abba_identity.bytes`), using the path-proof schema and `mtime_utc` semantics defined in PF12/PF14/PF19 (refresh-time, monotone UTC ISO). Each transcript is regenerated via `tools/evidence/update_evidence_index.py` under WS-D4b and kept in sync with the mirror.

  * **Ordering & compat tests** — `tests/order/test_total_order_properties.py` and `tests/cli/test_showcompat_parity_and_identity.py` cover antisymmetry, transitivity, AB↔BA parity, and two-run identity for ordering artifacts and CLI compat output. These tests run green under the WS-D4b semantics.

  * **Evidence skeleton, mirror, and schema tests** — `tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` validate the evidence skeleton for ordering artifacts (Index ↔ Mirror ↔ path-proof), including `mtime_utc` monotone checks, and `ci/checks/check_mirror_schema.sh` enforces Machine Mirror schema, `mtime_utc` / `produced_at_utc` format, and self-record invariants. Under WS-D4b, these tests and checks are expected to pass, satisfying the EPIC017 D2/D4 tokens (`EVIDENCE_INDEX_*`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `ORDERING_ARTIFACTS_*`, `COMPOSITE_ABBA_IDENTITY_OK`, `TIEBREAK_TOTAL_ORDER_OK`).

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

**Canonical Serialization Package (EPIC017 D1):**

* `CLI_NO_ALT_JSON_OK`

* `CLI_SHOWCOMPAT_CANON_OK`

* `CLI_STDOUT_LF_OK`

* `CLI_AB_BA_PARITY_OK`

* `CLI_READER_PARITY_OK`

* `TWO_RUN_IDENTITY_OK`

* `JSON_CANONICAL_CHECK_OK`

* `PREIMAGE_RECOMPUTE_OK`

**Evidence indices & mirror (EPIC017 D2):**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `EVIDENCE_PATH_PROOFS_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

* **Programmatic Configuration System:**

  * `CONFIG_GEN_OK`

  * `UNKNOWN_IDS_FAIL_CLOSED_OK` (or the chosen canonical name for this behavior)

  * `JSON_CANONICAL_CHECK_OK` (registry report)

* **Deterministic Tie-Break & Total-Order:**

  * `COMPOSITE_ABBA_IDENTITY_OK`

  * `TIEBREAK_TOTAL_ORDER_OK` (or equivalent ordering token)

  * `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`

  * `ORDERING_ARTIFACTS_DETERMINISTIC_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * `TWO_RUN_IDENTITY_OK`

  * `EVIDENCE_PATH_PROOFS_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

**Evidence pointers (titles-only)**

* Human Evidence Index and sentinel:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

**`EPIC017 manifest, close-out, and acceptance record (titles-only):`**

* `audit/EPIC017_MANIFEST.json — EPIC017 token→artifact manifest.`

* `audit/EPIC017_close_report.md — EPIC017 close-out report (D1–D5 status and evidence summary).`

* `docs/acceptance_map_epic017.json — EPIC017 acceptance map linking deliverables D1–D4 and their tokens to specific manifest entries.`

**EPIC017 D2 evidence skeleton & topology orientation (titles-only):**

* `docs/evidence/INDEX.json` — Human Evidence Index entries updated for EPIC017’s evidence skeleton artifacts.

* `docs/evidence/INDEX.sha256` — Hash sentinel for the Human Index.

* `artifacts/evidence_index.jsonl` — Machine Evidence Mirror records for EPIC017 evidence skeleton artifacts, including path-proof anchors.

* `audit/gates/topology/orientation_demo.txt` — Topology orientation demo report.

* `tests/evidence/test_evidence_skeleton.py` — Evidence skeleton test suite.

* `tests/evidence/test_orientation_demo.py` — Orientation demo validation tests.

* `ci/checks/check_mirror_schema.sh` — Mirror schema & self-record check invoked by CI.

* Machine mirror:

  * `artifacts/evidence_index.jsonl`

* Canonical serializer evidence:

  * `audit/gates/canonical_json/json_canonical_check.log`

  * `audit/gates/canonical_json/json_canon_compare.log`

  * `artifacts/cli/guards/serializer_grep_guard.log`

  * `artifacts/cli/guards/emitter_symbol_proof.txt`

**EPIC017 D4 ordering & evidence remediation (titles-only):**

* Ordering artifacts (generator-owned):

  * `artifacts/engine/order/channels_sorted.snapshot.json` — hannel ordering snapshot.

  * `artifacts/engine/order/categories_iter.snapshot.json` — Magic-10 category iteration snapshot.

  * `artifacts/engine/order/props_total_order.log` — comparator property-test proofs (antisymmetry, transitivity, totality).

  * `artifacts/engine/order/abba_identity.bytes` — AB↔BA byte-equality evidence for comparator outputs.

* Evidence Index & Machine Mirror records:

  * Human Index entries in `docs/evidence/INDEX.json` for each ordering artifact (artifact\_keys and discovered\_physical\_paths under `artifacts/engine/order/**`).

  * Machine Mirror records in `artifacts/evidence_index.jsonl` for the same artifact\_keys, with `proof_anchor` fields pointing to the corresponding path-proof transcripts.

* Path-proof transcripts (one per artifact):

  * `artifacts/engine/order/channels_sorted.snapshot.json.path_proof.txt`

  * `artifacts/engine/order/categories_iter.snapshot.json.path_proof.txt`

  * `artifacts/engine/order/props_total_order.log.path_proof.txt`

  * `artifacts/engine/order/abba_identity.bytes.path_proof.txt`

* Tests and CI jobs (titles-only) that back WS-D4 tokens:

  * Ordering property tests and harnesses — `tests/order/*`, `tests/mech/test_order_properties.py`.

  * Evidence skeleton and mirror tests — `tests/evidence/*`, `tests/ops/test_evidence_index.py`.

  * Mirror schema check — `ci/checks/check_mirror_schema.sh`.

*(Scripts and test suites are named here for EPIC017 WS-D4; their semantics and CI wiring remain governed by PF09, PF14, and PF19.)*

* **EPIC017 CLI canonicalization harness (D1):**

  * `artifacts/cli/ab.json` — AB slice of AB↔BA parity set (`cli.showcompat.ab`).

  * `artifacts/cli/ba.json` — BA slice of AB↔BA parity set (`cli.showcompat.ba`).

  * `artifacts/cli/summary.json` — summary of AB↔BA and two‑run identity hashes and equality flags (`cli.showcompat.summary`).

  * `artifacts/cli/reader_dump.json` — Reader v1 envelope dump for the canonicalized pair (`cli.showcompat.reader_dump`).

  * `artifacts/cli/reader_cli_parity.bytes` — raw bytes for Reader↔CLI parity comparison (`cli.showcompat.reader_cli_parity`).

  * `artifacts/cli/preimage_recompute.log` — preimage recompute log for Reader envelopes (`cli.showcompat.preimage_recompute`).

* Registry & config evidence **(EPIC017 D3 — Programmatic Configuration System):**  
* `engine.config.registry_loader` — typed, PF12-aligned registry loader for HDE catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations; alias policy OFF by default, allow-list only when explicitly enabled).

* `tools/generate_registry_report.py` — programmatic generator for `registry_report.v1`, driven by the canonical loader in PF14/PF09.

* `artifacts/registry/registry_report.json` — LF-terminated, canonical JSON registry report (schema and field shapes governed by PF12).

* `artifacts/registry/registry_report.json.path_proof.txt` — path-proof transcript for the registry report artifact (path, sha256, size\_bytes, produced\_at\_utc).

* Human Evidence Index entry for `artifact_key:"registry.registry_report"` in `docs/evidence/INDEX.json` (discovered\_physical\_path `artifacts/registry/registry_report.json`) and the corresponding Machine Mirror record in `artifacts/evidence_index.jsonl` (role `snapshot`, `proof_anchor:"artifacts/registry/registry_report.json.path_proof.txt"`).

* `tests/config/` registry loader and registry\_report tests (titles-only), including:

  * loader tests for unknown IDs, duplicate IDs, and alias policy OFF/ON behavior;

  * registry\_report determinism tests (`schema:"registry_report.v1"`, canonical JSON, two-run identity);

  * registry\_report indexing tests that prove SHA/size consistency across artifact, Index entry, mirror record, and path-proof.


* Order/comparator evidence:

  * `artifacts/engine/order/props_total_order.log`

  * `artifacts/engine/order/channels_sorted.snapshot.json`

  * `artifacts/engine/order/categories_iter.snapshot.json`

  * `artifacts/engine/order/abba_identity.bytes`

All of the above must be present in **both** the human Index and machine mirror (with path-proofs) in the epic’s closing PR.

**EPIC017 closure status.** As of BN 7.7.8 (Drain A9), all baseline PR tokens in this subsection and the Calcination phase-specific tokens for Deliverables D1–D4 are **green** and backed by indexed evidence under the pre-Glow “no-user” QA mode described in PF10 — HDE-Build Notes Addendum 10 “No User IDs in Pre-Glow Prod QA”. Canonical Serialization Package tokens (for example `CLI_SHOWCOMPAT_CANON_OK`, `COMPOSITE_ABBA_IDENTITY_OK`) are exercised via birth-based `showcompat` flows only; tokens that depend on DB-backed user flows or `bg:resolve --source=vendor --upsert` are **blocked by environment** and explicitly deferred to a future epic once Glow App user IDs exist. This subsection is the acceptance roster for HDE-EPIC017; any DB-backed user-flow acceptance tokens belong to that future epic, not to EPIC017.

**QA tokens library note (EPIC017)**

The token roster listed in this subsection for HDE-EPIC017 reflects the **de facto QA acceptance set** used for this epic (Canonical Serialization Package tokens, Evidence Skeleton tokens, QA rails, configuration, ordering), reconstructed from PF09, PF10, PF19, and the EPIC017 QA Plan. Now that PF19 — Glow QA Guide defines the QA Acceptance Tokens Registry in §9A, this roster **MUST** be treated as a **names-only consumer** of that registry:

* Canonical QA token names and their normative QA definitions live in PF19 §9A (and in the owner PF docs it references, such as PF04/PF09/PF12/PF05). This §2.2.5 list is an epic-specific roster of “tokens required for HDE-EPIC017,” not a parallel source of semantics.

* Any QA token used in HDE-EPIC017 acceptance that does not yet appear in PF19 §9A **MUST** be added to the PF19 registry (with owner PF, scope, QA definition, and evidence mapping) rather than defined here.

* Future maintenance for HDE-EPIC017 (for example re-running QA or auditing evidence after refactors) **SHOULD** use PF19 §9A as the single semantic reference for QA tokens, with this section used only to state which tokens EPIC017 is expected to satisfy and where its evidence is indexed.

This aligns HDE-EPIC017 with the QA token routing rules in PF19 §9A.9–§9A.10 and avoids duplicating or drifting token semantics inside PF20.

**Internal ops endpoint `/internal/version` (EPIC017 QA status)**

For the internal ops endpoint `/internal/version`, EPIC017 has **split acceptance**:

* **Transport / headers / conditionals — QA proved in prod via Codespaces (EPIC017):**

  * Manual QA captured non-conditional GET, HEAD, and conditional GET (`GET /internal/version` with `If-*` headers) against the Railway HD Engine endpoint and stored the artifacts under `audit/qa/hde-epic017/logs`, including at least:

    * `audit/qa/hde-epic017/logs/intver_get_full.txt` — baseline GET status/headers/body.

    * `audit/qa/hde-epic017/logs/intver_head_full.txt` — baseline HEAD status/headers.

    * `audit/qa/hde-epic017/logs/intver_get_conditional.txt` — conditional GET status/headers/body.

  * These artifacts show that, for `/internal/version` on Railway prod:

    * GET, HEAD, and conditional GET all return `200 OK` (no `304 Not Modified`), even when `If-*` headers are present.

    * Response headers use `Cache-Control: no-store`, an appropriate `Content-Type: application/json; charset=utf-8`, and **no** `ETag` or `Last-Modified` validators.

    * The JSON body for conditional GET matches the non-conditional GET body byte-for-byte, confirming that conditionals do not change the body shape or content from a transport perspective.

  * For EPIC017, this is sufficient to treat `/internal/version` **transport/header/conditional behavior** as QA-proved in prod; no further manual QA is required on headers/conditionals for this epic.

* **Body contract — Not Done (implementation bug, to be fixed outside EPIC017):**

  * The current `/internal/version` response body still:

    * omits `invocation_sha256` from the Identity & Provenance contract; and

    * uses a non-canonical field order (for example, `release_id` is not last; `build_commit` and `invocation_tag` appear out of frozen order).

  * This is a known specification mismatch with the Identity & Provenance contract and has been observed in earlier GET/HEAD checks as well as in the conditional GET QA step.

  * As a result, **any acceptance token(s) that require the full `/internal/version` body contract to be correct MUST NOT be considered satisfied under HDE-EPIC017**. Those tokens remain open and are blocked on a future implementation change that:

    * adds `invocation_sha256` to the response body;

    * enforces the canonical field order defined in Governance/Identity & Provenance canon; and

    * is backed by updated `/internal/version` QA evidence (at minimum a fresh GET artifact, and ideally a minimal two-run identity check) captured and indexed in the Evidence Index and Machine Mirror.

  * The body-shape bug is tracked in the Implementation Bug Tracker (bug card ID to be recorded there); EPIC017’s acceptance roster **must not close** `/internal_version` body-shape tokens until that bug is resolved and new evidence is captured.

**Vendor ingest dry-run (EPIC017 Live QA status)**

For vendor ingest, EPIC017 includes a **single dry-run resolver step** as part of Live QA from Codespaces into Railway prod:

* **QA step and artifact:**

  * A manual QA step runs `hdctl bg:resolve --source vendor --dry-run` for a synthetic birth tuple and QA user key and writes a single JSON artifact under `audit/qa/hde-epic017/logs/`, for example `audit/qa/hde-epic017/logs/step_bg_resolve_vendor_dry_run1.txt`.

  * This artifact contains both the resolver block and the ingest metadata for that call; it is the primary evidence file for this vendor dry-run QA step.

* **Resolver behavior (open rails, vendor path, dry-run):**

  * The resolver block shows at least:

    * `requested_source: "vendor"`, `resolved_source: "vendor"`.

    * `allow_network: true`, `safe_mode: false` (open rails for this vendor call).

    * `dry_run: true`, `upsert: false`.

    * `user_id: "qa_epic017_vendor1"` (a QA-only key, not a real app user).

  * This confirms that `bg:resolve` understood the CLI flags, selected the vendor path under open rails, and marked the run as a dry-run with no upsert semantics, using a disposable QA key consistent with the “no user IDs in prod” constraint.

* **Vendor ingest behavior (provider \+ no DB writes):**

  * The ingest block shows at least:

    * `provider: "hdapi"`, `vendor_version: 1`.

    * `rows_written: 0`, `db_rows_after: 0`.

    * A non-zero `duration_ms` consistent with a live HTTP call through the ingest path.

  * This matches the intended behavior for a dry-run ingest in pre-Glow prod: the vendor API is called under open rails, bridge logic runs, but no rows are written to the DB and DB row counts remain unchanged.

* **Parity, hashing, and idempotency metadata:**

  * The artifact records matching `input_fingerprint` and `payload_sha256`, with `db_emitted_sha256` equal to the same SHA-256 value and `parity_match: true`, indicating that the ingest logic would store a payload consistent with what was received from the vendor.

  * It also includes an `idempotency_key` that combines a UUID, provider (`hdapi`), `vendor_version`, and the input fingerprint, together with the QA user key, giving enough information to identify and deduplicate this dry-run request.

* **Disposition for this epic:**

  * For HDE-EPIC017, this single well-formed vendor dry-run artifact is sufficient to treat the **vendor ingest dry-run path** as Live-QA-proved for its intended scope: “can call vendor from Codespaces into Railway under open rails, bridge payload to DB shape, record parity metadata, and avoid DB writes.”

  * Deeper properties such as multi-run idempotence across time, broader provider coverage, and user-bound upsert behavior remain out of scope for EPIC017 and, where needed, must be picked up by future epics that own vendor ingest automation and app-user integration.

  ---

    #### **2.2.6 QA Rails — Open/Close (Final PR)**

For HDE-EPIC017, there are two distinct QA rail postures:

1. **Closed-rails CI and pre-commit harness in the repo**, and

2. **Open-rails manual Live QA from Codespaces into Railway prod.**

Both must be recorded here.

* **Pre-commit / CI posture (closed rails):**

  * CI and pre-commit runs for this epic use **closed rails by default**: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, with deterministic environment pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`). No vendor calls are expected for EPIC017 CI jobs.

  * All serializer, comparator, and evidence jobs (canonical JSON checks, mirror schema checks, ordering property tests, registry report generation) must run under this closed-rails posture unless a job is explicitly documented in PF09/PF14/PF19 as requiring open rails.

  * Any CI job that opens rails (for example, a DB connectivity check) **MUST** attach governed evidence in the same PR and be clearly labeled in PF09/PF19; by default, EPIC017 keeps all repository-level work strictly local and deterministic.

* **Post-commit (final proof run):**

  * The final PR that closes EPIC017 must run the full Phase I harness once in a representative environment under closed rails, collecting:

    * serializer/emitter proofs;

    * registry report and domain closure proofs;

    * A7-adjacent evidence where relevant (using Catalog JSON success only), while keeping Aux and `/internal/version` under their existing non-A7 governance.

  * Evidence from this final proof run must be indexed into the human Evidence Index and Machine Mirror in the same PR, satisfying the baseline and Calcination-specific acceptance tokens listed in §2.2.5.

* **Manual Live QA from Codespaces (EPIC017 Live QA pattern):**

  * For EPIC017 Live QA on prod surfaces (CLI, Aux, vendor ingest dry-run, `/internal/version`), manual steps follow this pattern:

    * The PO runs **one command per QA step** in a Codespace attached to the engine repo (either a CLI command such as `hdctl …` or a single HTTP request).

    * Each step writes exactly **one primary evidence file** (log or JSON) under `audit/qa/hde-epic017/…` — typically under `audit/qa/hde-epic017/logs/`.

    * Kronos (QA persona) reviews that single file and issues a QA addendum (`QA0X`) summarizing behavior, doc deltas, and verdict for that step.

    * Any helper files derived from that step (for example, a prettified JSON view) must also live under `audit/qa/hde-epic017/**` and be referenced from the same QA addendum, but the canonical artifact for the step is one file.

  * **Rails posture for manual Live QA (EPIC017 only):**

    * Manual Live QA steps that touch vendor or Railway **MUST** run with **open rails** in the Codespace: `ALLOW_NETWORK=1`, `SAFE_MODE=0` (or equivalent) as required by the command.

    * Manual Live QA is strictly read-only with respect to prod:

      * No production code or configuration changes.

      * No writes outside `audit/qa/**`.

      * For vendor ingest, only `bg:resolve --source vendor --dry-run` (no DB writes) or clearly identified vendor stubs are permitted; `bg:resolve --source vendor --upsert` remains prohibited in pre-Glow prod.

      * DB writes that resemble real app user creation remain out of scope until the Glow App user model exists (see `ISSUE-017-NO-USER-QA` and `ISSUE-017-STATELESS-JSON-QA` in §1).

    * Closed-rails duplicate testing (for example, re-running CI test suites by hand under `SAFE_MODE=1`, `ALLOW_NETWORK=0`) is **not** part of manual Live QA; it belongs to CI and repo-level PR QA for the EPIC017 foundations.

* **QA rail tokens (names-only):**

  * EPIC017 relies on the standard QA rail tokens as defined in PF19 and the QA Acceptance Tokens Registry in PF19 §9A; this section lists them by canonical name only:

    * `QA_PRECOMMIT_CHECKLIST_OK`

    * `QA_POSTCOMMIT_CHECKLIST_OK`

    * `ENV_RAILS_POLICY_OK`

  * The meanings and evidence mappings for these tokens are owned by PF19 §9A; EPIC017’s responsibility in PF20 is to show that they are required for this epic and that evidence for them is indexed alongside the other acceptance tokens in §2.2.5.

---

#### **2.2.7 Tracked Issues**

To close HDE-EPIC017, the epic report must explicitly list each tracked intra-epic issue and its final status.

In this document, an **issue** is any *unexpected* condition, behavior, gap, or risk discovered during implementation or QA, not a synonym for “deliverable” or “task.” An issue exists when reality diverges from the current plan or canon (for example: failing or flaky tests, ambiguous or conflicting specs, misaligned tools, missing or inconsistent evidence, surprising runtime behavior, or hard environment constraints such as “no user IDs in prod”). Planned work items, epics, and deliverables do **not** automatically become issues just because they are incomplete; they are tracked as issues only when there is something structurally blocking, surprising, or unclear about them (for example: “cannot be done under current rails,” “spec is incomplete,” or “tooling cannot represent required behavior”).

Every issue must end this epic in one of these states:

* **Completed under HDE-EPIC017**

* **Carried forward to another epic** (with a clear destination)

* **Explicitly dropped** (with a one-line rationale)

Tracked intra-epic issues for HDE-EPIC017:

---

Issue ID: `ISSUE-017-MTIME` \<allocated\> 

Issue ID: `ISSUE-017-STATELESS-JSON-QA` \<allocated\> 

Item: SDK / Admin-UI work (previously EPIC014) \<allocated\>   
---

**Rule (normative):**  
 No issue is allowed to disappear at close: each must be **proved, carried forward, promoted to a cross-epic ISSUE-XXX, or explicitly dropped** in this section and, where applicable, mirrored in PF20 §1 as a cross-epic issue

### **2.3 HDE-EPIC018 — HDE Calcination Pass 3**

#### **2.3.1 Meta**

* **Epic ID:** HDE-EPIC018

* **Epic name (short):** HDE Calcination Pass 3

* **Alchemical phase:** Calcination (Foundations first)

* **Phase rationale (1–3 sentences):**

  * PF09 Phase I shows that the canonical serializer/emitter, determinism rails, evidence skeleton, and configuration system for the HD Engine are partially implemented and only partially evidenced; EPIC017 closed a first slice of this but left structured gaps in PF09 Phase I task families HDE-CALC002/3/4.

  * HDE-EPIC018 is the third Calcination pass on these foundations: it completes canonical serializer coverage across governed JSON surfaces, standardises determinism environment pins, hardens CLI serializer guards and evidence indexing, and finishes the config registry and typed bundle story so that PF09 Phase I Calcination work can be treated as “hard base” rather than partial.

* **Related boards:**

  * None recorded yet; this epic is expected to be mirrored to the Glow Dev Board (HD Engine) when scheduled, consistent with PF20 §0 “Epic Records (Per‑Epic Tracking)”.

* **Status:** `In Progress`

* **Date started:** 2025.11.26

* **Date completed:** TBD

---

#### **2.3.2 Existing Work Check (MUST)**

**Existing features review (summary)**

* **Canonical serializer, single-emitter rules, and idempotence — Specified and partially implemented (EPIC017).**

  * PF01/PF02/PF14 already define canonical JSON (UTF‑8, sorted keys, compact, exactly one trailing LF) and the preimage/idempotence recipe for idempotence\_hash, with a single presenter/emitter shared between Reader and CLI and AB↔BA / two‑run identity requirements.

  * HDE-EPIC017 wired this into the Compat/Reader surfaces and proved JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK, COMPOSITE\_ABBA\_IDENTITY\_OK, and related Canonical Serialization Package tokens for those paths, with evidence indexed in the Evidence Index and machine mirror.

* **Ordering and tie-break module — Implemented and evidenced (EPIC006/EPIC017).**

  * Deterministic total-order comparators and helpers exist, with ordering artifacts under artifacts/engine/order/\*\*, mirror records, and path-proofs governed by PF12/PF19; EPIC017 closed ORDERING\_ARTIFACTS\_SINGLE\_SOURCE\_OK, ORDERING\_ARTIFACTS\_DETERMINISTIC\_OK, and evidence skeleton tokens such as EVIDENCE\_PATH\_PROOFS\_OK and CI\_CHECK\_MIRROR\_SCHEMA\_OK.

* **Evidence Index and machine mirror — Canon defined and partially hardened.**

  * PF09/PF12 define docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, and artifacts/evidence\_index.jsonl as the human index, hash sentinel, and machine mirror, with canonical JSONL and path-proof discipline; EPIC017 implemented a working update\_evidence\_index toolchain and CI checks that keep Index, mirror, and path-proofs in lockstep for the evidence families it touched.

* **Configuration loader and registry — Specified; partial implementation.**

  * PF12/PF14 define catalog ownership, loader behavior, and a required registry\_report.json artifact with unknown-ID hard‑fail semantics; EPIC017 and prior work stood up a basic registry report and some loader paths but did not finish the full config catalog, acceptance mapping, or typed bundle story.

* **QA rails and environment semantics — Defined in PF04/PF19 and exercised in EPIC017.**

  * PF04/PF19 define SAFE\_MODE / ALLOW\_NETWORK rails for CI, Codespaces, and prod Live QA; EPIC017 already used these rails for determinism and Live QA, including manual Codespaces‑to‑Railway checks for /internal/version and vendor dry‑run, with rails tokens QA\_PRECOMMIT\_CHECKLIST\_OK, QA\_POSTCOMMIT\_CHECKLIST\_OK, and ENV\_RAILS\_POLICY\_OK in play.

* **EPIC017 close posture.**

  * PF20 §2.2 records EPIC017 as Closed with D1–D4 Done and D5 Completed, leaving ingest and stateless JSON QA for future epics; it also allocates cross‑epic issues ISSUE‑017‑NO‑USER‑QA and ISSUE‑017‑STATELESS‑JSON‑QA for follow‑up. HDE-EPIC018 builds directly on this base for serializer, determinism rails, and evidence skeleton but does not itself close the cross‑epic issues unless explicitly extended.

**Existing tokens validated (names-only, reused here)**

EPIC018 reuses, without redefining semantics, the following acceptance tokens already in use and, in many cases, already proved for subsets of the system under EPIC017 and prior work (semantics in PF19 §9A, PF04, PF09, PF12, PF14):

* JSON\_CANONICAL\_CHECK\_OK

* TWO\_RUN\_IDENTITY\_OK

* COMPOSITE\_ABBA\_IDENTITY\_OK

* ORDERING\_ARTIFACTS\_SINGLE\_SOURCE\_OK

* ORDERING\_ARTIFACTS\_DETERMINISTIC\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* EVIDENCE\_INDEX\_MIRROR\_OK

* EVIDENCE\_PATHS\_VALIDATED\_OK

* EVIDENCE\_PATH\_PROOFS\_OK

* EVIDENCE\_PATH\_PROOFS\_SHAPE\_OK

* CI\_CHECK\_MIRROR\_SCHEMA\_OK

* QA\_PRECOMMIT\_CHECKLIST\_OK

* QA\_POSTCOMMIT\_CHECKLIST\_OK

* ENV\_RAILS\_POLICY\_OK

These tokens are expected to remain in scope for EPIC018; this epic extends their coverage to additional surfaces (more JSON artifacts, CLI guards, config reports, typed bundles) rather than redefining them.

**Existing evidence located (titles-only)**

Representative evidence families and artifacts that EPIC018 treats as starting points include:

* Canonical serialization and ABBA identity:

  * artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/cli/summary.json, artifacts/cli/reader\_dump.json

  * artifacts/cli/reader\_cli\_parity.bytes

  * audit/gates/canonical\_json/json\_canonical\_check.log, json\_canon\_compare.log

* Ordering and tie-break artifacts:

  * artifacts/engine/order/channels\_sorted.snapshot.json

  * artifacts/engine/order/categories\_iter.snapshot.json

  * artifacts/engine/order/props\_total\_order.log

  * artifacts/engine/order/abba\_identity.bytes

* Evidence skeleton and mirror:

  * docs/evidence/INDEX.json

  * docs/evidence/INDEX.sha256

  * artifacts/evidence\_index.jsonl

  * governed \*.path\_proof.txt files for core artifacts

* Config and registry (partial):

  * artifacts/registry/registry\_report.json (as defined in PF12/PF14 and PF09 Phase I)

EPIC018 must extend these families and create new ones (for config, CLI guards, typed bundles) while keeping the Evidence Index and mirror discipline intact.

**Gap statement (what EPIC018 must address)**

* Serializer/emitter behavior is not yet canonicalised across all governed JSON surfaces; some CLI and config outputs still rely on ad‑hoc serializers or incomplete canonical JSON guarantees.

* Determinism environment pins (LC\_ALL, LANG, TZ, SAFE\_MODE, ALLOW\_NETWORK) are not yet enforced as a coherent policy across CLI, tests, and CI; determinism drift remains possible when running outside the “happy path” CI environment.

* CLI serializer guards and guard artifacts are partial; there is no single, governed evidence family that proves CLI outputs are being generated under correct rails and canonical serializer semantics.

* The Evidence Index and machine mirror do not yet carry a simple, repeatable sanity pipeline for “does the evidence skeleton itself still make sense,” especially as new artifact families come online.

* Configuration artifacts (registry report and related config outputs) are not yet fully cataloged, mapped to tokens, or indexed in a way that QA and governance can rely on; there is no clear acceptance mapping from PF09 Phase I config tasks to concrete artifacts and tokens.

* Typed FE/BE configuration bundles have been specified in outline but are not yet wired as first‑class, tested, governed artifacts with clear determinism and evidence guarantees.

---

#### **2.3.3 Deliverables (Jobs To Be Done)**

**D1 — Canonical serializer/emitter completion across governed JSON**

* **Job to be done:**

  * Extend the canonical serializer/emitter so that all governed JSON outputs for the engine and CLI—compat JSON, Reader envelopes, CLI sidecars, config reports, registry snapshots, and any new JSON artifacts introduced by this epic—are produced through the single canonical emitter with explicit canonical JSON guarantees (UTF‑8, no BOM, sorted keys, compact, exactly one trailing LF).

  * Ensure AB↔BA and two‑run identity continue to hold for these surfaces under the pinned determinism environment (see D2), and that any drift is caught by property tests and serializer guards.

* **Evidence (titles-only):**

  * Tests: serializer determinism and canonical JSON tests (extensions of tests/test\_emitter\_determinism.py and canonical compare logs).

  * Artifacts: updated canonical JSON logs under audit/gates/canonical\_json/\*\* and additional CLI output snapshots under artifacts/cli/\*\* (including narrative sidecars and config JSON).

  * Index/mirror: docs/evidence/INDEX.json entries and artifacts/evidence\_index.jsonl records for all new JSON artifacts, with path-proofs.

* **PF references:** PF01 — HDE-Math-Spec; PF02 — HDE Architecture; PF05 — HDE-CLI-API-Vendor-Ref; PF12 — HDE-Schemas & Artifacts; PF14 — HDE Mechanics Guide; PF19 — Glow QA Guide.

---

**D2 — Determinism environment pins (Calcination determinism rails)**

* **Job to be done:**

  * Define and implement a coherent determinism environment policy for engine and CLI runs, pinning LC\_ALL, LANG, TZ, SAFE\_MODE, ALLOW\_NETWORK, and any other relevant environment variables for CI, local dev, and QA consoles, so that canonical serializer and comparator behavior is deterministic across environments.

  * Capture this policy in PF05/PF14 references and ensure that CI and test harnesses enforce it for all determinism‑sensitive tests.

* **Evidence (titles-only):**

  * Tests: determinism policy tests (for example, tests that assert failure when environment pins are omitted, plus two‑run identity tests across environments).

  * Artifacts: logs under audit/gates/determinism/\*\* (or equivalent) recording environment pins and two‑run identity proofs.

  * Index/mirror: updated evidence index entries referencing determinism artifacts and their path‑proofs.

* **PF references:** PF04 — HDE Governance (env rails); PF05 — HDE-CLI-API-Vendor-Ref; PF09 — HDE-Build Checklist; PF14 — HDE Mechanics Guide; PF19 — Glow QA Guide (rails semantics).

---

**D3 — CLI serializer guard artifacts and evidence indexing**

* **Job to be done:**

  * Introduce governed CLI serializer guard artifacts and guard jobs that prove the CLI is using the canonical emitter under the correct determinism environment and that critical CLI JSON surfaces (compat, Reader dumps, aux previews, config sidecars, registry reports) conform to canonical JSON and serializer policies.

  * Ensure CLI guard artifacts are indexed in the Evidence Index and machine mirror alongside existing Canonical Serialization Package artifacts, and that the guard jobs are wired into PF09 CI jobs and PF19 QA playbooks.

* **Evidence (titles-only):**

  * Artifacts: artifacts/cli/guards/serializer\_guard.log, artifacts/cli/guards/emitter\_symbol\_proof.txt (extended/updated), and any new guard artifacts defined in PF05.

  * Tests: tests covering CLI guard behavior (for example, tests/cli/test\_serializer\_guards.py) and their integration with determinism rails.

  * Index/mirror: docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl entries for the CLI guard artifacts with governed \*.path\_proof.txt files.

* **PF references:** PF05 — HDE-CLI-API-Vendor-Ref; PF09 — HDE-Build Checklist; PF12 — HDE-Schemas & Artifacts; PF14 — HDE Mechanics Guide; PF19 — Glow QA Guide.

---

**D4 — Evidence skeleton and sanity pipeline**

* **Job to be done:**

  * Extend and stabilise the evidence skeleton so that there is a simple, repeatable “sanity pipeline” that can be run in CI and on demand to verify that the Evidence Index, hash sentinel, machine mirror, and governed path‑proofs remain coherent as new artifact families (including CLI guards and config artifacts) are added.

  * Ensure the sanity pipeline has its own acceptance token (for example SANITY\_PIPELINE\_OK) and that running it is required for closing this epic.

* **Evidence (titles-only):**

  * Tools: tools/evidence/update\_evidence\_index.py, tools/evidence/sanity\_pipeline.py (or equivalent), and CI script entries for the sanity job.

  * Artifacts: updated docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, and governed path‑proofs for all artifacts touched by this epic.

  * Tests: tests/evidence/test\_evidence\_skeleton.py and tests/ops/test\_evidence\_index.py extended to cover new artifacts and sanity pipeline behavior.

* **PF references:** PF09 — HDE-Build Checklist; PF12 — HDE-Schemas & Artifacts; PF19 — Glow QA Guide (evidence tokens).

---

**D5 — Config artifacts and acceptance mapping**

* **Job to be done:**

  * Finish the configuration registry story for Calcination: define and emit the governed set of config JSON artifacts (for example thresholds, category maps, Magic‑10 configuration, and registry reports), map them to PF09 Phase I config tasks, and define acceptance tokens that express when the config catalog is complete and in sync with canon.

  * Ensure config artifacts are canonical JSON, indexed in the Evidence Index and mirror with path‑proofs, and referenced by PF19 QA playbooks as evidence for config‑related QA.

* **Evidence (titles-only):**

  * Artifacts: artifacts/registry/registry\_report.json (updated), artifacts/thresholds/\*.json, audit/gates/bands/edges.snapshot.json, and any additional config artifacts defined in PF12.

  * Index/mirror: docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl entries for config artifacts plus governed \*.path\_proof.txt files.

  * Mapping: a small config acceptance map file (for example audit/EPIC-018\_config\_acceptance\_map.json) that ties PF09 Phase I config tasks to config artifacts and tokens.

* **PF references:** PF01 — HDE-Math-Spec (where thresholds and bands are defined); PF12 — HDE-Schemas & Artifacts; PF14 — HDE Mechanics Guide; PF09 — HDE-Build Checklist; PF19 — Glow QA Guide.

---

**D6 — Typed FE/BE bundles**

* **Job to be done:**

  * Define, implement, and evidence typed configuration bundles for front‑end and back‑end consumers (for example “typed bundles” that package together config slices needed by each surface) such that they can be generated deterministically from the canonical config artifacts, validated against schemas, and treated as first‑class, governed artifacts in the Evidence Index and machine mirror.

  * Ensure typed bundles either reuse the canonical serializer/emitter (D1) or consume canonical JSON sources with deterministic transforms, and that their schemas are captured in PF12/PF14.

* **Evidence (titles-only):**

  * Artifacts: artifacts/config\_bundles/\*.json (or equivalent) for FE/BE bundles, plus any typed bundle manifest files.

  * Tests: tests/config/test\_typed\_bundles.py (or equivalent) proving schema validity, determinism, and correct mapping from base config artifacts.

  * Index/mirror: docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl entries for typed bundles with governed path‑proofs.

* **PF references:** PF12 — HDE-Schemas & Artifacts; PF14 — HDE Mechanics Guide; PF19 — Glow QA Guide.

---

#### **2.3.4 PF Reference Map**

**Core PF references (per PF20 template)**

* PF21 — 7 Phases of Alchemical Engineering (phase names and meanings; Calcination as “Foundations first”).

* PF06 — Epic Process Guide (epic lifecycle, roles, PR discipline).

* PF09 — HDE-Build Checklist (Phase I Calcination tasks HDE-CALC002/3/4 and their CI gates).

* PF19 — Glow QA Guide (QA Acceptance Tokens Registry §9A; QA rails and playbooks).

* PF20 — HDE-Phased Epics (this document; epic mapping and acceptance roster).

**Additional PF references used by this epic**

* PF01 — HDE-Math-Spec (canonical JSON, idempotence\_hash, bands/threshold math).

* PF02 — HDE Architecture (single-emitter rules, surface responsibilities).

* PF04 — HDE Governance (env rails, ownership, Identity & Provenance).

* PF05 — HDE-CLI-API-Vendor-Ref (CLI surfaces, commands, serializer/Reader parity).

* PF12 — HDE-Schemas & Artifacts (schemas for JSON artifacts, Evidence Index and mirror schema).

* PF14 — HDE Mechanics Guide (mechanical jobs, ordering module, config loaders).

* PF17 — HDE Narratives Guide (where CLI/Reader narrative surfaces need serializer parity).

---

#### **2.3.5 Tokens and Evidence (Acceptance)**

**Baseline PR and repo tokens (names-only)**

These apply to all epics and must be satisfied for HDE-EPIC018:

* PR\_OPENED\_OK

* TESTS\_PASS\_OK

* DOC\_DELTA\_PRESENT\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* EVIDENCE\_INDEX\_HASH\_OK

* MACHINE\_MIRROR\_UPDATED\_OK

**Rails and QA checklist tokens (names-only)**

* QA\_PRECOMMIT\_CHECKLIST\_OK

* QA\_POSTCOMMIT\_CHECKLIST\_OK

* ENV\_RAILS\_POLICY\_OK

These tokens have semantics and evidence mappings defined in PF19 §9A and PF04/PF09; EPIC018’s responsibility is to require them for close and ensure their evidence is indexed.

**Phase-specific tokens for HDE-EPIC018 (names-only, roster for this epic)**

The following tokens (existing or newly registered in PF19 §9A) are expected to be part of EPIC018 acceptance; semantics and detailed mappings live in PF19/PF04/PF09/PF12, not here.

* Canonical serialization and determinism:

  * JSON\_CANONICAL\_CHECK\_OK

  * TWO\_RUN\_IDENTITY\_OK

  * COMPOSITE\_ABBA\_IDENTITY\_OK

* Determinism rails and environment pins:

  * DETERMINISM\_ENV\_PINS\_OK (name to be registered in PF19 §9A; scope: env rails for determinism-sensitive paths)

* CLI guards and parity:

  * CLI\_SERIALIZER\_GUARD\_OK (or equivalent CLI guard token defined in PF19 §9A)

  * READER\_CLI\_PARITY\_OK (existing Canonical Serialization Package token; reused here)

* Evidence skeleton and sanity pipeline:

  * EVIDENCE\_INDEX\_UPDATED\_OK

  * EVIDENCE\_INDEX\_MIRROR\_OK

  * EVIDENCE\_PATHS\_VALIDATED\_OK

  * EVIDENCE\_PATH\_PROOFS\_OK

  * EVIDENCE\_PATH\_PROOFS\_SHAPE\_OK

  * CI\_CHECK\_MIRROR\_SCHEMA\_OK

  * SANITY\_PIPELINE\_OK (new or existing token for the evidence sanity pipeline)

* Config and typed bundles:

  * CONFIG\_REGISTRY\_OK

  * CONFIG\_MAGIC10\_OK

  * CONFIG\_BUNDLES\_DETERMINISTIC\_OK

All QA-oriented tokens above must appear in the PF19 QA Acceptance Tokens Registry; PF20 §2.3.5 is a names‑only roster of “tokens required for HDE-EPIC018,” not a second source of semantics.

**Evidence pointers (titles-only; to be populated as work lands)**

At close, HDE-EPIC018 is expected to have at least the following evidence pointers recorded in PF20 and PF19:

* PF10 — HDE Build Notes (entries tagged HDE-EPIC018) as historical context only, not normative proof.

* audit/EPIC-018\_MANIFEST.json — manifest of all epic artifacts and tokens.

* audit/EPIC-018\_close\_report.md — narrative close report summarising evidence and token status.

* docs/evidence/INDEX.json entries for:

  * canonical JSON gates and logs (serializer/emitter tests, CLI guard outputs)

  * determinism rails and two‑run identity artifacts

  * CLI guard artifacts (serializer\_guard.log, emitter\_symbol\_proof.txt, etc.)

  * evidence sanity pipeline outputs

  * config artifacts (thresholds, registry\_report, category maps)

  * typed FE/BE bundles

* artifacts/evidence\_index.jsonl records with artifact\_key values corresponding to all of the above, each with a proof\_anchor to a governed \*.path\_proof.txt file.

Per PF20 §2.1 and PF19 §9A, HDE-EPIC018 cannot be marked Done until every token in this roster has corresponding index and mirror evidence.

---

#### **2.3.6 QA Rails — Open/Close (Final PR)**

For the final PR that closes HDE-EPIC018, PF20 expects the following rails posture (names-only; semantics in PF04/PF09/PF19).

* **Pre‑commit / CI rails posture:**

  * Default CI jobs run with SAFE\_MODE=1 and ALLOW\_NETWORK=0, proving determinism under closed rails and ensuring canonical serializer, registry, and bundle tests pass without external network.

  * Determinism-sensitive jobs (for example two‑run identity or cross‑env determinism checks) MAY open rails locally as needed, but any such openings MUST be documented in PF06/PF09 job descriptions and produce evidence indexed in the same PR.

* **Rails for CLI guards and serializer tests:**

  * CLI guard jobs that exercise serializer behavior should run under the determinism environment pins defined in D2; any deviation (for example locale differences) MUST be treated as failure.

  * Rails tokens ENV\_RAILS\_POLICY\_OK and DETERMINISM\_ENV\_PINS\_OK are required to be green at close, with evidence in the Evidence Index/mirror.

* **Evidence skeleton and sanity pipeline rails:**

  * The evidence sanity pipeline (for example a CI job running tools/evidence/sanity\_pipeline.py) runs under closed rails (SAFE\_MODE=1, ALLOW\_NETWORK=0) and MUST succeed before epic close.

  * SANITY\_PIPELINE\_OK is required, with artifacts and mirror records proving that Index, mirror, and path-proofs are coherent after all EPIC018 changes.

* **Config and typed bundle QA rails:**

  * Config artifacts and typed bundles are generated and validated under closed rails; any job that opens rails (for example to fetch reference data) MUST be tightly scoped and produce evidence in the same PR.

  * Config-related tokens (CONFIG\_REGISTRY\_OK, CONFIG\_MAGIC10\_OK, CONFIG\_BUNDLES\_DETERMINISTIC\_OK) depend on these rails constraints and associated QA playbooks in PF19.

* **Rails tokens (names-only) expected in the final acceptance set:**

  * QA\_PRECOMMIT\_CHECKLIST\_OK

  * QA\_POSTCOMMIT\_CHECKLIST\_OK

  * ENV\_RAILS\_POLICY\_OK

  * DETERMINISM\_ENV\_PINS\_OK

  * SANITY\_PIPELINE\_OK

HDE-EPIC018’s PF20 entry is responsible for stating that these rails tokens are required and pointing to their indexed evidence; token semantics remain in PF19, PF04, PF09, and PF12.

---

#### **2.3.7 Tracked Issues**

For HDE-EPIC018, PF20 tracks intra‑epic issues per the PF20 §2.1.7 rules; at kickoff time there are no EPIC018‑specific issues yet recorded, but this section is reserved for issues discovered during implementation and QA.

**Issues completed under HDE-EPIC018**

* None yet; to be populated as issues are discovered and resolved.

**Issues carried forward or promoted**

* Any cross‑epic issues from PF20 §1 (for example ISSUE‑017‑STATELESS‑JSON‑QA, ISSUE‑QA‑TOKENS‑LIBRARY) that EPIC018 materially addresses MUST be given explicit dispositions here at close (for example “partially addressed; remaining work carried forward to HDE-EPIC0xx”); this will be updated when EPIC018 work lands.

**Issues explicitly dropped**

* None at kickoff; any decision to drop an identified issue must be recorded here with a one‑line rationale, consistent with PF20 §2.1.7.

