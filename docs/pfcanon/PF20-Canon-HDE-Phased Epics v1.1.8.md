**Title**: PF20-Canon-HDE-Phased Epics

**Status:** Canon

**Version:** v1.1.8

**Effective Date:** 2025-11-30

**Last Update Gate:** HDE-EPIC018 Closure

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

**D2 — Determinism environment pins (Calcination determinism rails)**

* **Job to be done:**

  * Define and implement a coherent determinism environment policy for engine and CLI runs, pinning `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK` and any other relevant environment variables for CI, local dev, and QA consoles so that canonical serializer and comparator behavior is deterministic across environments.

  * Capture this policy in PF05/PF14 references and ensure that CI and test harnesses enforce it for all determinism-sensitive tests, using the canonical helper and rails checks delivered by this epic rather than ad-hoc env configuration.

* **Evidence (titles-only):**

  * **Helper and rails implementation (code surfaces):**

    * `engine/runtime/determinism_env.py` — defines `DETERMINISM_ENV_PINS` (including `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`), and exposes `ensure_determinism_env`, `render_env_log`, and `record_env_log` as the single canonical abstraction for determinism env rails.

    * CI workflow entries in `.github/workflows/ci.yml` that pin `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` for determinism-sensitive jobs, with comments documenting this as the determinism env posture for EPIC018.

    * `ci/checks/check_env_pins.sh` — CI script that asserts these exact pins for determinism jobs and fails if any deviate, so CI cannot silently drift to an open-rails configuration for determinism work.

  * **Determinism env log and governed evidence (artifacts \+ index/mirror):**

    * `audit/gates/determinism/env_pins.log` — canonical JSON log (sorted keys, compact, LF-terminated) written by `record_env_log`, recording:

      * `env` block with the effective `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK` values;

      * `status` field (for example `"success"`/`"failure"`); and

      * `suites` array naming determinism-sensitive suites (for example `ci:determinism-rails`, `tests:invariance`, `tests:evidence-ordering`, `orientation:demo`).

    * `audit/gates/determinism/env_pins.log.path_proof.txt` — governed path-proof carrying matching `path`, `size_bytes`, `sha256`, and `mtime_utc` / `produced_at_utc`, consistent with EPIC017/EPIC018 path-proof rules for evidence logs.

    * `docs/evidence/INDEX.json` entry with `artifact_key: "audit.determinism.env_pins" → audit/gates/determinism/env_pins.log`, and a corresponding `artifacts/evidence_index.jsonl` record with the same hash, size, and `proof_anchor` pointing to `audit/gates/determinism/env_pins.log.path_proof.txt`, establishing this as the single canonical mirror entry for determinism env rails evidence.

  * **Determinism env tests and invariance coverage (tests):**

    * `tests/invariance/test_locale_tz.py` — imports `DETERMINISM_ENV_PINS` / `ensure_determinism_env`, asserts that `LC_ALL=C` and `TZ=UTC` (and other pins as applicable) are present in `os.environ`, and checks that `ensure_determinism_env()` returns the expected pin dict.

    * `tests/invariance/test_bytes_identity.py` — calls `ensure_determinism_env()` before running the bytes identity check on the canonical serializer, directly coupling determinism env pins to serializer identity tests.

    * `tests/invariance/test_determinism_env_helper.py` — adds unit tests for missing/mismatched pins, env log writing/verification, and `apply=True` behavior, ensuring the helper fails closed under misconfiguration and that env logs remain canonical and checkable.

    * CI runs for these tests (and related determinism suites) must pass under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), enforcing the determinism policy.

  * **Token linkage (names-only; semantics in PF19/PF04/PF09/PF12):**

    * QA/rails tokens `DETERMINISM_ENV_PINS_OK` and `ENV_RAILS_POLICY_OK` (as registered in PF19 §9A and referenced in §2.3.5/§2.3.6 of this document) are the acceptance tokens for D2:

      * `DETERMINISM_ENV_PINS_OK` — all determinism-sensitive suites (serializer invariance, evidence ordering, orientation demo, relevant CI jobs) run under the pinned env rails defined above, with failures when pins are missing or mismatched.

      * `ENV_RAILS_POLICY_OK` — the determinism env helper, CI env pins, env log, path-proof, and Evidence Index/mirror records are present and coherent as a governed evidence family.

    * PF20’s role is to require these tokens for HDE-EPIC018 and point to their evidence surfaces (helper module, CI env config, env\_pins log \+ path-proof, invariance tests, and index/mirror entries); their detailed semantics and QA mappings remain in PF19 §9A and PF04/PF09/PF12.

* **PF references:**

  * PF04 — HDE Governance (env rails and tokens).

  * PF05 — HDE-CLI-API-Vendor-Ref (engine/CLI surfaces and determinism-sensitive commands).

  * PF09 — HDE-Build Checklist (Phase I determinism rails and CI gates).

  * PF12 — HDE-Schemas & Artifacts (Evidence Index & mirror, governed log/path-proof families).

  * PF14 — HDE Mechanics Guide (mechanical jobs for determinism, invariance, and evidence).

  * PF19 — Glow QA Guide (rails semantics and QA Acceptance Tokens Registry §9A).

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

**D4 — Evidence skeleton and sanity pipeline**

* **Job to be done:**

  * Extend and stabilise the evidence skeleton so that there is a simple, repeatable **sanity pipeline** that can be run in CI and on demand to verify that the Human Evidence Index (`docs/evidence/INDEX.json`), hash sentinel (`docs/evidence/INDEX.sha256`), Machine Evidence Mirror (`artifacts/evidence_index.jsonl`), and governed path-proofs remain coherent as new artifact families (including CLI guards and config artifacts) are added.

  * Implement this as a closed-rails sanity pipeline entrypoint (`tools/evidence/run_sanity_pipeline.py`) that calls the determinism env helper, runs a fixed sequence of checks (serializer determinism, env pins checks, invariance tests, CLI guards, PF12 evidence skeleton checks), and emits a deterministic sanity log, and ensure that the pipeline has its own acceptance token (`SANITY_PIPELINE_OK`) and that running it successfully under closed rails is required for closing this epic.

* **Evidence (titles-only):**

  * **Sanity pipeline entrypoint and orchestration:**

    * `tools/evidence/run_sanity_pipeline.py` — defines the sanity pipeline entrypoint that:

      * calls `ensure_determinism_env()` (from the determinism env helper) at startup to enforce closed-rails env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`);

      * defines a fixed set of sanity steps (for example serializer tests, env pins check, invariance tests, CLI guards, ordering/evidence/orientation checks);

      * executes steps in order, recording lines of the form `check <name>:OK` / `check <name>:FAIL` and stopping on the first failure; and

      * writes a canonical log containing a header (for example `sanity_pipeline`), a single `env:` line with sorted env pins, one line per step result, and a final `summary:PASS` or `summary:FAIL` line, with no timestamps or other env-dependent content.

  * **Sanity log artifact and governance:**

    * `artifacts/sanity/sanity.log` — canonical sanity pipeline log written by `tools/evidence/run_sanity_pipeline.py` under closed rails, recording env pins, step results, and the final summary line.

    * `artifacts/sanity/sanity.log.path_proof.txt` — path-proof transcript for the sanity log (including at least `path`, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`) generated via the evidence tooling, governed under the same path-proof rules as other PF12 evidence artifacts.

    * `docs/evidence/INDEX.json` entry with `artifact_key: "sanity.pipeline.log"` pointing to `artifacts/sanity/sanity.log`, and corresponding `artifacts/evidence_index.jsonl` record with matching `sha256`, `size_bytes`, and `proof_anchor: "artifacts/sanity/sanity.log.path_proof.txt"`; `docs/evidence/INDEX.sha256` updated to reflect the new canonical INDEX body after adding the sanity pipeline entry.

  * **Evidence skeleton checks and self-record invariants:**

    * `tools/evidence/update_evidence_index.py` — canonical tool for maintaining the Evidence Index, hash sentinel, Machine Mirror body, and associated path-proofs, invoked both by the sanity pipeline and dedicated evidence CI jobs.

    * `tests/evidence/test_evidence_skeleton.py` — test suite that asserts:

      * mirror records are unique and sorted and have the full PF12 key set;

      * each indexed artifact has a corresponding path proof that matches `path`, `sha256`, `size_bytes`, and carries valid UTC `mtime_utc` / `produced_at_utc` fields; and

      * the `index.machine_mirror` self-record (`artifact_key` and `proof_anchor` for `artifacts/evidence_index.jsonl`) has a `sha256` equal to the hash of the mirror body and stays in sync with `artifacts/evidence_index.jsonl.path_proof.txt`.

    * `tests/ops/test_evidence_index.py` — tests that enforce Human Index ↔ Machine Mirror ↔ path-proof invariants for all governed artifacts in scope, including the newly added sanity pipeline log and any refreshed artifacts (such as `artifacts/engine/order/abba_identity.bytes` and its path proof) touched as part of D4.

    * `tests/evidence/test_sanity_pipeline.py` — tests for the sanity pipeline orchestrator itself, confirming:

      * in the success case, a configured sequence of steps with return code 0 yields `summary:PASS` and logs each `check <name>:OK` line; and

      * in the failure case, the pipeline exits non-zero, records `check <name>:FAIL` for the first failing step, does not log subsequent steps, and ends with `summary:FAIL`.

  * **CI job for the sanity pipeline (titles-only):**  
    * A dedicated **sanity-pipeline** job in `.github/workflows/ci.yml` that:

      * runs under the same closed-rails env posture as the main test job (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`);

      * invokes `python tools/evidence/run_sanity_pipeline.py` and treats any non-zero exit code as a CI failure; and  
      * runs alongside, not instead of, the individual evidence skeleton and orientation checks (for example `update_evidence_index.py --check`, `orientation_demo.py --check`), so that the pipeline acts as an orchestrated “belt and suspenders” entrypoint rather than a replacement for existing CI rails.  
* **PF references:** PF09 — HDE-Build Checklist (Phase I / Evidence Index & Machine Mirror skeleton and sanity job); PF12 — HDE-Schemas & Artifacts (Evidence Index & Machine Mirror schema; governed log and path-proof semantics); PF14 — HDE Mechanics Guide (evidence tooling and skeleton jobs); PF19 — Glow QA Guide (evidence tokens and `SANITY_PIPELINE_OK` semantics).

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
  * 

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

    * Each step writes exactly **one primary evidence file** (log or JSON) under `audit/qa/HDE-EPIC017/…` — typically under `audit/qa/HDE-EPIC017/logs/`.

    * Kronos (QA persona) reviews that single file and issues a QA addendum (`QA0X`) summarizing behavior, doc deltas, and verdict for that step.

    * Any helper files derived from that step (for example, a prettified JSON view) must also live under `audit/qa/HDE-EPIC017/**` and be referenced from the same QA addendum, but the canonical artifact for the step is one file.

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

  * None recorded yet; this epic is expected to be mirrored to the Glow Dev Board (HD Engine) when scheduled, consistent with PF20 §0 “Epic Records (Per-Epic Tracking)”.

* **Status:** Closed

* **Date started:** 2025.11.26

* **Date completed:** 2025.11.29

* **Deliverables:** D1–D7 as defined in §2.3.3 are implemented and evidenced (serializer/emitter completion, determinism env rails, CLI guards, evidence skeleton & sanity pipeline, governed config artifacts & acceptance map, typed FE/BE bundles, and repo docs alignment); remaining work is primarily PF-Canon documentation deltas and future admin-surface/admin-bundle epics, not further changes inside EPIC018.

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

  * Introduce deterministic, AST-based CLI guard tools that:

    * enforce the “no ad-hoc `json.dumps`/`json.dump` in governed CLI scope” rule; and

    * prove that governed CLI handlers (at minimum `showcompat` and `bg:resolve`) route through canonical emitter symbols, with Aux treated as an explicitly documented optional emitter case;

  * all running under the determinism environment rails defined in D2.

  * Ensure guard artifacts are emitted as governed evidence under `artifacts/cli/guards/…`, with path-proofs and Evidence Index/mirror records, and that CI runs both guard tools and their tests under closed rails before downstream evidence and topology checks.

* **Evidence (titles-only):**

  * **Guard tools (code surfaces):**

    * `tools/cli/serializer_grep_guard.py` — AST-based serializer grep guard that:

      * walks Python files under the governed CLI scope (`engine/cli/**` by default, plus any extra roots passed via `--paths`);

      * detects imports of `json` and calls to `json.dumps` / `json.dump` (including via aliases); and

      * renders a deterministic text report with:

        * a single `scope:` line listing scanned roots; and

        * a `summary: PASS|FAIL` line followed (on FAIL) by sorted violation lines naming file(s) and location(s), with no timestamps or env-dependent content.

    * `tools/cli/emitter_symbol_proof.py` — AST-based emitter proof tool over `engine/cli/main.py` that:

      * inspects governed handlers (`showcompat`, `bg_resolve`, and `aux_preview`);

      * records for each handler a line of the form `handler:function:emitters` where `emitters` is a sorted list of canonical emitter symbols (`emitter.emit_public`, `emit_reader_public_envelope`, etc.);

      * writes a deterministic `summary: PASS|FAIL` line based on whether required handlers have at least one canonical emitter; and

      * treats Aux as an explicitly optional emitter case by emitting `aux-preview:aux_preview:<none>` when no canonical emitter is present, without failing the proof.

  * **Guard artifacts and governed evidence (artifacts \+ path-proofs):**

    * `artifacts/cli/guards/serializer_grep_guard.log` — serializer grep guard report for the real repo, showing:

      * a header/scope line describing the governed CLI search roots; and

      * `summary: PASS` when no disallowed `json.dumps`/`json.dump` calls are present in governed scope.

    * `artifacts/cli/guards/serializer_grep_guard.log.path_proof.txt` — governed path-proof transcript (path, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`) for the serializer grep guard log.

    * `artifacts/cli/guards/emitter_symbol_proof.txt` — emitter symbol proof report listing governed CLI handlers and their canonical emitters, including an explicit exempt `<none>` line for Aux when applicable, plus a deterministic summary line.

    * `artifacts/cli/guards/emitter_symbol_proof.txt.path_proof.txt` — governed path-proof for the emitter symbol proof artifact.

  * **Evidence Index and Machine Mirror (titles-only):**

    * `docs/evidence/INDEX.json` entries for:

      * `artifact_key: "cli.guard.serializer_grep" → artifacts/cli/guards/serializer_grep_guard.log`;

      * `artifact_key: "cli.guard.emitter_symbol_proof" → artifacts/cli/guards/emitter_symbol_proof.txt`.

    * Corresponding `artifacts/evidence_index.jsonl` records with matching `sha256` and `size_bytes` and `proof_anchor` fields pointing to the guard artifacts’ `.path_proof.txt` siblings.

    * `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt` updated for the post-guard Evidence Index state, with `update_evidence_index.py --check` passing under closed rails to prove coherence after the guard artifacts and their path-proofs are added.

  * **Tests and CI wiring (titles-only):**

    * CI workflow entries in `.github/workflows/ci.yml` that:

      * run `ci/checks/check_env_pins.sh` to assert determinism env pins;

      * invoke `python tools/cli/serializer_grep_guard.py` and `python tools/cli/emitter_symbol_proof.py` under closed rails (the same env pins as D2); and

      * run `pytest tests/cli/test_serializer_guards.py` before evidence/orientation checks.

    * `tests/cli/test_serializer_guards.py` — guard test module that:

      * asserts both guards exit with `returncode == 0` and PASS summaries on the clean repo;

      * creates a temporary “bad” file containing a direct `json.dumps` call under a temp path to prove that the serializer grep guard exits non-zero and logs `summary: FAIL` with an explicit violation line;

      * constructs synthetic CLI handler files without canonical emitters to prove that the emitter proof exits non-zero and logs `summary: FAIL` with `<none>` emitter lists.

    * These tests ensure the guards are deterministic in the clean case and fail closed with clear evidence in violation cases, under the determinism env pins enforced by D2.

  * **Token linkage (names-only; semantics in PF19/PF04/PF09/PF12):**

    * `CLI_SERIALIZER_GUARD_OK` — CI runs CLI serializer and emitter guards under determinism env rails; the guard tools succeed on the real repo and `tests/cli/test_serializer_guards.py` passes, proving the CLI is free of disallowed JSON serialization in governed scope and that governed handlers route through canonical emitters.

    * `SERIALIZER_GREP_GUARD_OK` — the serializer grep guard artifact (`artifacts/cli/guards/serializer_grep_guard.log` \+ path-proof \+ Index/mirror record) exists and encodes a PASS summary for the governed CLI scope under closed rails.

    * `EMITTER_SYMBOL_PROOF_OK` — the emitter symbol proof artifact (`artifacts/cli/guards/emitter_symbol_proof.txt` \+ path-proof \+ Index/mirror record) exists, lists governed CLI handlers and their canonical emitter symbols, returns PASS for non-optional handlers, and records Aux’s current status as an explicit optional/emempt emitter case.

    * These guard tokens also support `READER_CLI_PARITY_OK` at the CLI layer by demonstrating that governed CLI handlers are wired through the same canonical emitters used by Reader; PF19 §9A remains the semantic home for all of these tokens.

* **PF references:** PF05 — HDE-CLI-API-Vendor-Ref (CLI surfaces, guard roles); PF09 — HDE-Build Checklist (Calcination / D3 CLI guard tasks); PF12 — HDE-Schemas & Artifacts (Evidence Index & path-proof rules); PF14 — HDE-Mechanics Guide (CLI mechanics / guards); PF19 — Glow QA Guide (§9A QA Acceptance Tokens Registry and CLI guard tokens).

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

  * Define, implement, and evidence typed configuration bundles for front-end and back-end consumers that are generated deterministically, under closed rails, from the existing governed config artifacts (for example Magic-10 config, band edges, registry report) and the PF14/PF12 registry loader.

  * Ensure that:

    * bundle generation uses the canonical JSON emitter (UTF-8, sorted keys, compact, exactly one trailing LF);

    * backend and frontend bundles expose the intended scopes (backend: full internal config surface; frontend: slimmer client-facing view); and

    * bundles are treated as first-class governed artifacts: they have path-proofs, Evidence Index entries (`config_bundle.be`, `config_bundle.fe`), Machine Mirror records, and acceptance tests that prove determinism, schema conformance, and strict linkage back to their source config artifacts.

* **Evidence (titles-only):**

  * **Bundle generator and closed-rails posture (code surfaces):**

    * `engine/config/bundles.py` — typed bundle builder module that:

      * constructs backend and frontend bundle structures from governed config artifacts via the registry loader (for example Magic-10 config, band edges, registry report);

      * calls a closed-rails guard (for example `require_closed_rails()`) before building to ensure generation only runs under `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`; and

      * writes bundle JSON via the canonical serializer so that outputs are deterministic and canonical.

    * `tools/config/generate_bundles.py` — bundle generation entrypoint that:

      * runs under closed rails (using the same helpers as D5) to invoke the backend and frontend bundle builders; and

      * writes canonical FE/BE bundle JSON files to `artifacts/config_bundles/…` in a single run suitable for CI and local use.

  * **Typed bundle artifacts and schemas (artifacts \+ local schemas):**

    * Backend bundle artifact:

      * `artifacts/config_bundles/be_bundle.json` — backend bundle (for example `config_bundle.be.v1`), containing:

        * full Magic-10 config (order, caps, seeds, schema);

        * full band edges payload (schema, source, bands, edges, clamp, rounding, version);

        * full channel objects (ids, gates, centers, primary/secondary domains, circuit metadata, flags);

        * centers, domains, alias policy; and

        * a `sources` block with `path`, `sha256`, and `size_bytes` digests for each upstream governed artifact (for example Magic-10 config, band edges, registry report).

      * `artifacts/config_bundles/be_bundle.json.path_proof.txt` — governed path-proof for the backend bundle (path, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`).

    * Frontend bundle artifact:

      * `artifacts/config_bundles/fe_bundle.json` — frontend bundle (for example `config_bundle.fe.v1`), containing:

        * Magic-10 order and caps;

        * band edges/bands/clamp/rounding/version;

        * channel ids plus minimal channel metadata (centers, domains, alias policy) appropriate for clients; and

        * a `sources` block analogous to the backend bundle, with digests tied back to the same governed config artifacts.

      * `artifacts/config_bundles/fe_bundle.json.path_proof.txt` — governed path-proof for the frontend bundle.

    * Local JSON Schemas (test-only):

      * `docs/schemas/config_bundle_be.json` and `docs/schemas/config_bundle_fe.json` — local JSON Schemas used by tests to validate bundle structure (schema string, required sections, object shapes). These schemas are test aids only and remain outside the PF12 canonical schema catalog until PF-Canon is explicitly updated.

  * **Evidence Index and Machine Mirror wiring (titles-only):**

    * `docs/evidence/INDEX.json` entries:

      * `artifact_key: "config_bundle.be" → artifacts/config_bundles/be_bundle.json`;

      * `artifact_key: "config_bundle.fe" → artifacts/config_bundles/fe_bundle.json`.

    * Corresponding `artifacts/evidence_index.jsonl` records for `config_bundle.be` and `config_bundle.fe` with matching `sha256` and `size_bytes` and `proof_anchor` fields pointing to the `.path_proof.txt` siblings.

    * `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt` updated after bundles are added so that the Human Evidence Index, hash sentinel, and Machine Mirror self-record remain coherent (as verified by the evidence skeleton checks in D4).

  * **Tests and CI wiring (titles-only):**

    * `tests/config/test_typed_bundles.py` — typed bundle test module that at minimum:

      * enforces two-run identity for backend and frontend bundles (same bytes, same SHA-256 across two runs under closed rails);

      * validates FE/BE bundle structure against `docs/schemas/config_bundle_fe.json` and `docs/schemas/config_bundle_be.json`; and

      * asserts strict linkage to governed config artifacts by comparing the `sources` block entries (paths, `sha256`, `size_bytes`) against current `artifacts/thresholds/magic10_config.json`, `artifacts/thresholds/band_edges.json`, `artifacts/registry/registry_report.json`, and related config artifacts.

    * CI workflow entries in `.github/workflows/ci.yml` that:

      * run the bundle generator under closed rails (via the same closed-rails env helpers used in D5) to produce `be_bundle.json` and `fe_bundle.json`; and

      * execute `pytest tests/config/test_typed_bundles.py` alongside existing config and evidence tests, with failures blocking epic closure.

  * **Token linkage (names-only; semantics in PF19/PF12/PF09/PF14):**

    * `CONFIG_BUNDLES_DETERMINISTIC_OK` — typed FE/BE bundles are generated under closed rails from governed config artifacts and the registry loader, are canonical JSON, satisfy two-run identity, conform to the FE/BE bundle schemas, and contain a `sources` block whose digests match the current governed config artifacts.

    * This token’s canonical definition and evidence mapping live in the QA Acceptance Tokens Registry (PF19 §9A) and in PF12/PF09/PF14; PF20’s role is to require it for HDE-EPIC018 and to point to the bundle generator, bundle artifacts, path-proofs, Index/mirror records, and typed bundle tests as the evidence surfaces for D6.

* **PF references:** PF12 — HDE-Schemas & Artifacts (config artifacts, Evidence Index & mirror, governed bundles); PF14 — HDE-Mechanics Guide (config mechanics and bundle consumers); PF09 — HDE-Build Checklist (Phase I / HDE-EPIC018 D5/D6 config tasks); PF19 — Glow QA Guide (§9A config & evidence tokens); PF01 — HDE-Math-Spec (bands/thresholds as used in Magic-10 config).

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

  * `CLI_SERIALIZER_GUARD_OK`

  * `SERIALIZER_GREP_GUARD_OK`

  * `EMITTER_SYMBOL_PROOF_OK`

  * `READER_CLI_PARITY_OK`

These tokens are registered and defined in the QA Acceptance Tokens Registry in PF19 §9A; PF20’s role is to record that HDE-EPIC018 must satisfy them and to point to their guard evidence surfaces (guard tools, artifacts, Index/mirror records, and tests) in §2.3.3 and in the epic’s close-out manifest, not to restate their semantics.

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

**Close-pack / documentation (repo docs alignment, non-canonical but required)**

In addition to the EPIC-018 manifest and close report, EPIC018’s close-pack **MUST** include a repository-docs alignment step. This step updates top-level, repo-facing documentation so that it is consistent with PF-Canon and the EPIC-018 manifest/close report, while keeping PF-Canon documents themselves unchanged. At minimum, the following files are expected to be refreshed and aligned under the EPIC018 rails:

* **Top-level repo docs (EPIC018-aligned):**

  * `README.md` — EPIC018-centric overview of Glow HD Engine, explicitly listing D1–D7 outcomes (canonical JSON, closed-rails env policy, CLI guards, evidence skeleton & sanity pipeline, governed config artifacts & acceptance map, typed FE/BE bundles, and EPIC-018 manifest/close report) and pointing to PF-Canon titles for normative rules.

  * `CHANGELOG.md` — entry for “EPIC-018: HD Calcination Pass 3 close-out,” summarising what was added/changed under EPIC018 (determinism rails, CLI guards, evidence skeleton & sanity pipeline, D5 config artifacts & acceptance map, D6 typed bundles, D7 manifest/close report) without redefining PF-Canon.

  * `AGENTS.md` — simplified, EPIC018-aligned agent guidance that:

    * sets PF-Canon (PF12, PF19, PF20, etc.) as the hierarchy;

    * reiterates “never hand-edit governed artifacts”; and

    * describes roles/rails/workflows for Codex/dev agents, evidence harness, config/bundle agents, and doc agents under the EPIC018 rails (closed env, single emitter/serializer, CLI guards, evidence tools), by title only.

* **Implementation docs under `./docs/**` (EPIC018 configuration and evidence cribs):**

  * `docs/INDEX.md` — docs index listing EPIC018 close-out artifacts (manifest, close report, config acceptance map) as governed and pointing by title to the evidence skeleton, orientation demo, sanity pipeline, CLI guards, config/bundle generators, and determinism helper.

  * `docs/RUN.md` — developer runbook (for example “Developer flight checks (EPIC018)”) that pins closed rails and sketches a quick-check flow (env check, serializer parity test) and an evidence/guard workflow (CLI guards, evidence index update, orientation demo, sanity pipeline, config/bundle generation).

  * `docs/config_and_bundles.md` — implementation-level crib for D5/D6, describing governed config artifacts and the EPIC018 config acceptance map, typed FE/BE bundles and their local schemas under `docs/schemas/`, and the requirement to use canonical tools and PF12 discipline.

  * `docs/evidence/EPIC018_evidence.md` — implementation-level crib for D4 evidence skeleton & sanity pipeline, capturing the skeleton, orientation demo, sanity pipeline, evidence-update commands, and rails by **title only**, and explicitly forbidding manual edits to governed evidence artifacts (Index, mirror, path-proofs, sanity log).

These repo docs are **not PF-Canon**; PF-Canon (PF01/PF02/PF04/PF05/PF09/PF12/PF14/PF19/PF20) remains the single home for math, contracts, tokens, and evidence rules. However, for EPIC018 close-pack, PF20 treats this repo-docs alignment sweep as a **required (non-canonical) deliverable**:

* HDE-EPIC018 is not considered fully closed until:

  * `audit/EPIC-018_MANIFEST.json` and `audit/EPIC-018_close_report.md` list these repo docs under the appropriate “non-canonical documentation” or similar section; and

  * the updated repo docs are consistent with the EPIC-018 manifest/close report and with PF-Canon, using **titles-only routing** back to PF-Canon for norms.

At the same time, any future changes to these repo docs **do not** change PF-Canon on their own; they must follow PF06/PF12 Doc-Delta and evidence rules if they imply changes to governed artifacts or acceptance semantics.

**EPIC018 compat environment note and Live QA vs CI split**

For HDE-EPIC018, PF20 records the following environment and responsibility split for key token families:

* **Compat tokens (D1) — vendor-backed compat from Codespaces:**

  * For this epic, compat-related Canonical Serialization Package tokens such as `CLI_SHOWCOMPAT_CANON_OK`, `CLI_TWO_RUN_IDENTITY_OK`, and related D1 tokens are being exercised via **vendor-backed compat flows from Codespaces into Railway**, not via a purely local dev harness.

  * The canonical proofs for these tokens in EPIC018 therefore come from:

    * CI and/or determinism harnesses that call `hdctl showcompat` under closed rails; and

    * vendor-backed compat runs invoked from Codespaces under the rails described in §2.3.6, with compat JSON and Reader envelopes recorded as governed artifacts and indexed into the Evidence Index and Machine Mirror.

  * PF05/PF19 remain the semantic homes for `CLI_SHOWCOMPAT_CANON_OK`, `CLI_TWO_RUN_IDENTITY_OK`, and related tokens; this note only states that, for EPIC018, their **canonical environment** is the vendor-backed engine, with Live QA and CI evidence pointing at the same behavior.

* **D3/D4 mechanics tokens — CI-owned; Live QA as smoke evidence:**

  * CLI guard tokens (`CLI_SERIALIZER_GUARD_OK`, `SERIALIZER_GREP_GUARD_OK`, `EMITTER_SYMBOL_PROOF_OK`) and sanity pipeline token `SANITY_PIPELINE_OK` are primarily **CI-owned mechanics tokens** for EPIC018. Their acceptance evidence comes from the closed-rails CI jobs that:

    * run the guard tools and their test suite; and

    * run `tools/evidence/run_sanity_pipeline.py` under closed rails to produce `artifacts/sanity/sanity.log` and a green exit code, as described in §2.3.3 and §2.3.6.

  * Live QA executions of these mechanics (for example, CLI guards or sanity pipeline runs from an open-rails Codespaces environment) are treated as **smoke tests**:

    * their logs and exit codes **MUST** be captured mechanically under `audit/qa/hde-epic018/d3-cli-guards/**` and `audit/qa/hde-epic018/d4-sanity/**` (and referenced from `audit/qa/hde-epic018/qa_notes.md`);

    * they are **not** counted as satisfying guard or sanity tokens for epic acceptance unless PF20 explicitly ties a token to a green Live QA run; and

    * non-zero exit codes from these Live QA runs are recorded as QA findings for that environment and cross-checked against CI status, rather than automatically blocking epic close.

* **Responsibility split:**

  * CI/closed-rails harnesses (described in PF09/PF14/PF19 and summarised in §2.3.3/§2.3.6) remain the **canonical proving ground** for mechanics tokens (CLI guards, sanity pipeline, evidence skeleton).

  * Live QA flows from Codespaces → Railway are used to:

    * demonstrate vendor-backed compat behavior for D1 tokens in the intended prod-like environment; and

    * provide smoke-test visibility into D3/D4 mechanics, with evidence under `audit/qa/hde-epic018/**` treated as QA context, not primary acceptance evidence, unless explicitly promoted in future PF20 updates.

This note is specific to HDE-EPIC018. Future epics that change where compat tokens are proved or promote Live QA runs to acceptance gates **MUST** record those decisions explicitly in their own PF20 epic record.

**EPIC018 implementation posture (D1–D7)**

As of BN 7.8.9 (Drain A25), HDE-EPIC018 has delivered the D1–D7 deliverables defined in §2.3.3:

* D1 — canonical serializer/emitter completion across governed JSON — is implemented and evidenced via the shared serializer/emitter, canonical JSON logs, AB↔BA and two-run identity tests, and CLI compat snapshots.

* D2 — determinism env rails — is implemented and evidenced via the shared determinism env helper, closed-rails CI env pins and checks, and governed env-pins logs.

* D3 — CLI serializer guards — is implemented and evidenced via the AST-based serializer grep guard and emitter symbol proof tools, their governed artifacts under `artifacts/cli/guards/…`, and guard test suites.

* D4 — evidence skeleton and sanity pipeline — is implemented and evidenced via the sanity pipeline entrypoint and log, P1 fixes to the machine mirror self-proof, and extended evidence skeleton tests and CI jobs.

* D5 — config artifacts and acceptance map — is implemented and evidenced via governed config artifacts (registry report, Magic-10 config, band edges), an EPIC018 config acceptance map, and tests/CI wiring tied into the Evidence Index/mirror.

* D6 — typed FE/BE bundles — is implemented and evidenced via the bundle generator, FE/BE bundle artifacts under `artifacts/config_bundles/…`, local schemas, tests for schema conformance and two-run identity, and Index/mirror entries.

* D7 — manifest, close report, and repo docs alignment — is implemented and evidenced via the EPIC018 manifest and close report in audit space and the repo-docs alignment sweep recorded in the D7 close-pack block above.

The full implementation and QA trace for these deliverables is captured in **PF10 — HDE-Build Notes** (EPIC018 addenda) and in the governed artifacts and Index/mirror records referenced in this subsection and §2.3.3. Remaining work called out in Addendum 27 (for example PF-Canon doc deltas and future admin-surface/admin-bundle epics) is intentionally scoped outside HDE-EPIC018 and will be addressed via cross-epic issues and future epics, not by keeping EPIC018’s implementation open.

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

  * The evidence sanity pipeline for HDE-EPIC018 is implemented as a **closed-rails CI job** that runs `python tools/evidence/run_sanity_pipeline.py` under `SAFE_MODE=1`, `ALLOW_NETWORK=0` and pinned determinism env values (`LC_ALL=C`, `LANG=C`, `TZ=UTC`). This CI job **MUST** succeed (exit code 0\) on the final PR that closes the epic and produce a canonical sanity log at `artifacts/sanity/sanity.log` (with a governed path proof and Evidence Index/mirror records), proving that the Evidence Index, hash sentinel, Machine Mirror, and governed path-proofs remain coherent after all EPIC018 changes.

  * The `SANITY_PIPELINE_OK` token is satisfied **only** by these closed-rails CI runs. Optional sanity runs in other environments (for example, an open-rails Codespaces session with `SAFE_MODE=0`, `ALLOW_NETWORK=1`, non-canonical `LANG`) are allowed for observability and QA exploration, but when the pipeline detects an env pins mismatch and exits non-zero, that run **does not** contribute to epic acceptance. Such runs must be treated as QA failures for that environment and recorded as such in QA notes under `audit/qa/hde-epic018/**` (for example in `audit/qa/hde-epic018/qa_notes.md`), not as evidence for `SANITY_PIPELINE_OK`.

  * If a closed-rails CI run of the sanity pipeline fails for **non-env reasons** (for example serializer errors, mirror mismatches, or path-proof bugs), those failures **MUST** be treated as real defects that block D4 acceptance and require implementation fixes and new evidence. PF20’s role is to require `SANITY_PIPELINE_OK` for HDE-EPIC018 and to point to the sanity pipeline CI job and `artifacts/sanity/sanity.log` as the governed acceptance evidence; token semantics and detailed QA mappings remain in PF19, PF04, PF09, and PF12.

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

To close HDE-EPIC018, the epic record must explicitly list each tracked intra-epic issue and its final status for this epic.

In this document, an **issue** is any *unexpected* condition, behavior, gap, or risk discovered during implementation or QA, not a synonym for “deliverable” or “task.” An issue exists when reality diverges from the current plan or canon (for example: failing or flaky tests, ambiguous or conflicting specs, misaligned tools, missing or inconsistent evidence, surprising runtime behavior, or hard environment constraints such as “no user IDs in prod”). Planned work items, epics, and deliverables do **not** automatically become issues just because they are incomplete; they are tracked as issues only when there is something structurally blocking, surprising, or unclear about them (for example: “cannot be done under current rails,” “spec is incomplete,” or “tooling cannot represent required behavior”).

Every issue must end this epic in one of these states:

* **Completed under HDE-EPIC018**

* **Carried forward to another epic** (with a concrete epic ID or clearly described future epic)

* **Promoted to a cross-epic issue** (ISSUE-XXX in §1 “Outstanding Issues”)

* **Explicitly dropped** (with a one-line rationale)

For each tracked intra-epic issue, the epic record SHOULD provide at least:

* **Issue ID** (for example `ISSUE-<EPIC>-<NAME>` or a short label if no ID is minted)

* **Title** (short, descriptive name)

* **Status** (for example: `Completed under <EPIC-ID>`, `Carried forward to <EPIC-ID>`, `Cross-epic ISSUE-XXX`, `Dropped`)

* **Scope / description** (1–3 sentences explaining what the issue covers)

* **Disposition for this epic** (brief note describing what happened to this issue in this epic: proved, carried forward, cross-epic, or dropped)

  ---

**Issues completed under HDE-EPIC018**

* None yet recorded as of this version; if EPIC018 discovers and resolves specific implementation or QA issues (for example evidence skeleton inconsistencies or guard misconfigurations), they MUST be added here with `Status: Completed under HDE-EPIC018` before final close.

  ---

**Issues carried forward or promoted**

**Issue ID:** `ISSUE-018-ADMIN-SURFACES`  
 **Title:** Admin bundle and admin surfaces (pre-Glow product payload)  
 **Status:** **Carried forward to future Coagulation-phase epic (ID TBD)**

* **Scope / description:**

  * EPIC018’s Calcination scope focused on engine foundations (D1–D7) and intentionally did **not** implement a full admin bundle and admin product surfaces (for example a single JSON admin bundle containing two BodyGraphs, Magic-10 compat with scores/bands, and three narratives, and corresponding Admin CLI/HTTP routes or GUI).

  * PF10 Addenda and the Dev Retrospective recognise this as a missing but critical product-level surface: pre-Glow, CLI and Admin GUI are expected to expose a full product payload for a pair, backed by canonical engine behavior and governed artifacts.

* **Disposition for this epic:**

  * HDE-EPIC018 records `ISSUE-018-ADMIN-SURFACES` as **out of scope for Calcination implementation** but important for product readiness. No admin bundle builder, CLI full-bundle command, or admin HTTP route is implemented under this epic.

  * This issue is carried forward to a future **Coagulation-phase admin-surfaces epic (ID TBD)**, which will define and implement the admin bundle builder, CLI/HTTP admin endpoints, and any minimal Admin GUI required for pre-Glow product usage. When that epic is minted, PF20 §1 “Outstanding Issues (Cross-Epic)” and that epic’s §2.x record MUST either promote this issue to a cross-epic ISSUE-XXX or list it as a carried-forward issue with a concrete epic ID.

  ---

**Issues explicitly dropped**

* None at this time. If EPIC018 or the PO decides to drop any identified issue, it MUST be listed here with a one-line rationale (for example “no longer aligned with current product scope”), consistent with PF20 §2.1.7.

**Rule (normative):**  
 No issue is allowed to disappear at close: each must be **proved, carried forward to another epic (or clearly described future epic), promoted to a cross-epic ISSUE-XXX, or explicitly dropped** in this section and, where applicable, mirrored in PF20 §1 as a cross-epic issue.

### 2.4 HDE-EPIC019 Epic Plan

#### 2.4.1 Meta

* **Epic ID:** HDE-EPIC019

* **Epic name (short):** Dissolution Pass 2

* **Alchemical phase:** Dissolution

* **Phase rationale (1–3 sentences):**  
   PF09 Phase II — Dissolution (“Normalize and make it pure”) defines this phase as the place where already-normalized inputs are carried through to deterministic, schema‑governed engine behavior for compat, sampler/ranker, and the core engine, with evidence integrated into the global Evidence Index and Machine Mirror. HDE-EPIC019 is the second Dissolution pass and is responsible for closing the remaining Not done work for the swipe sampler/ranker (HDE‑DISS003) and deterministic engine core (HDE‑DISS004) so that Phase II behavior is deterministic, reproducible, and fully evidenced under the same rails Calcination epics hardened.

* **Related boards:**

  * Glow HDE Epics tracking board — epic row/card for `HDE-EPIC019` (to be created/linked per PF20 §2 “Epic Records (Per‑Epic Tracking)”).

* **Status:** `In Progress` 

* **Date started:** 2025.11.29

* **Date completed:** TBD

* **Owner(s):**

  * Lead Dev: Isis (HD Engine)

  * Approver: Thoth (Head of Development)

  * Product Owner: HD Engine PO (per PF06 roles)

  * QA representative: Kronos (or delegate) per PF19/PF06 QA roles

#### 2.4.2 Existing Work Check (MUST)

##### Existing features review (summary)

* **Phase II — Dissolution work already Done (PF09):**

  * **HDE-DISS001 — Input Normalization & Validation Layer:**  
     Normalization, AB↔BA canonical JSON, schema validation, and evidence coverage are implemented and evidenced.

  * **HDE-DISS002 — Compatibility Engine (pair):**  
     Compat semantics, ABBA parity, canonical JSON identity hash, and compat evidence/indexing are in place.

  * **HDE-DISS005 — Band Thresholds & Tuning (admin):**  
     Marked Done/history‑only; satisfied under HDE‑EPIC007 — Magic‑10 Category Engine.

  * **HDE-DISS006 — Category Framework (internal):**  
     Marked Done/history‑only; also satisfied under HDE‑EPIC007.

* **Calcination foundations relevant to this epic (PF20 \+ PF09):**

  * **HDE-EPIC017 — HD Calcination Pass 2:**  
     Hardened the canonical serialization package, Evidence Index \+ mirror skeleton, programmatic configuration system, and deterministic ordering module.

  * **HDE-EPIC018 — HD Calcination Pass 3:**  
     Standardized determinism env pins, finalized canonical serializer coverage on governed surfaces, hardened evidence skeleton and sanity pipeline, and finalized config/bundle story.

* **Scope of remaining Dissolution gaps (PF09 Phase II):**

  * **HDE-DISS003 — Swipe Sampler & Ranker (all subtasks .1–.6):** Not done.

  * **HDE-DISS004 — Deterministic Engine Core (all subtasks .1–.4):** Not done.

  * Normalization, compat, bands, and categories are treated as existing work and must not be re‑implemented; EPIC019 must build on them.

* **Prototypes / partial harnesses:**

  * Any sampler/ranker or engine‑core prototypes noted in PF10 — HDE‑Build Notes v7.9 are treated as historical input only; they are not evidence. They may be referenced by Addendum ID and short title during implementation but must be superseded by PF09/PF12/PF14‑aligned evidence under EPIC019.

##### Existing tokens validated (reused, not re‑proved)

* **From Calcination epics and PF19 (determinism, serializer, baseline rails):**

  * Canonical JSON and determinism:

    * `JSON_CANONICAL_CHECK_OK`

    * `TWO_RUN_IDENTITY_OK`

    * `COMPOSITE_ABBA_IDENTITY_OK`

    * `AB_BA_PARITY_OK` (proved for compat and category layers)

  * Baseline PR / rails / evidence discipline:

    * `PR_OPENED_OK`

    * `TESTS_PASS_OK`

    * `DOC_DELTA_PRESENT_OK`

    * `EVIDENCE_INDEX_UPDATED_OK`

    * `EVIDENCE_INDEX_HASH_OK`

    * `EVIDENCE_INDEX_MIRROR_OK`

    * `EVIDENCE_PATHS_VALIDATED_OK`

    * `MACHINE_MIRROR_UPDATED_OK`

    * `QA_PRECOMMIT_CHECKLIST_OK`

    * `QA_POSTCOMMIT_CHECKLIST_OK`

    * `ENV_RAILS_POLICY_OK`

    * `DETERMINISM_ENV_PINS_OK`

    * `SANITY_PIPELINE_OK` (for determinism/sanity pipeline wiring).

* **From DISS001/DISS002 and EPIC007 band/category work (PF09 \+ PF20):**

  * `AB_BA_PARITY_OK` established for compat and category outputs.

  * Evidence discipline tokens (`EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`) already exercised for compat/category artifact families.

These tokens’ meanings and QA mappings remain single‑homed in PF04/PF19; EPIC019 reuses them and extends their coverage to sampler and core artifacts rather than redefining them.

##### Existing evidence located (titles‑only)

Titles/families only; concrete paths and schemas remain governed by PF12/PF09/PF14:

* Normalization, compat, and category evidence:

  * Normalization snapshots and AB↔BA logs from HDE‑DISS001.

  * Compat ABBA/AB↔BA parity logs, identity hashes, and canonical compare logs from HDE‑DISS002.

  * Band thresholds and Magic‑10 category snapshots and calculators from HDE‑DISS005/006 and HDE‑EPIC007.

* Evidence Index / Mirror:

  * Human Evidence Index and hash sentinel for existing families (INDEX JSON \+ hash).

  * Machine Evidence Mirror entries for compat and category artifacts.

* Determinism env pins and sanity pipeline (EPIC018):

  * Determinism env log(s) demonstrating pinned env values.

  * Sanity pipeline log(s) and corresponding Index/Mirror entries used as pattern for new EPIC019 evidence families.

##### Gap statement (explicit)

EPIC019 is defined to close at least the following Phase II gaps:

* No implemented, fully‑evidenced **swipe sampler/ranker** aligned with PF01/PF09 semantics (zero‑weight enforcement, eligibility/diversity constraints, deterministic scoring and ordering).

* No deterministic **sampler/ranker harness** with two‑run identity and ABBA proofs wired into Evidence Index/Mirror.

* No **seedable dev/admin sampler flow** with evidence that seed affects only candidate selection order and not public bytes.

* No **dev‑only sampler endpoint harness** for QA/debugging, aligned with PF05/PF19 rails.

* No proven, fully‑evidenced **Deterministic Engine Core** showing “pure compute” (no I/O/clocks/globals), AB↔BA neutrality, two‑run identity, and canonical JSON evidence integrated into the Evidence Index and Machine Mirror.

#### 2.4.3 Deliverables (Jobs To Be Done)

Deliverables D1–D5 correspond to the five workstreams defined in the kickoff, each mapped to explicit PF09 Phase II tasks/subtasks.

---

##### Deliverable D1 — Sampler/ranker deterministic pool and scoring (HDE-DISS003.1–.3)

* **PF09 scope:**

  * HDE‑DISS003 — Swipe Sampler & Ranker (task‑level)

  * HDE‑DISS003.1 — Zero‑weight rule enforcement

  * HDE‑DISS003.2 — Pool formation & eligibility filters

  * HDE‑DISS003.3 — Deterministic scoring & total order

* **Job to be done:**  
   Implement the sampler/ranker such that it:

  * Honors viewer weights and **enforces zero‑weight rules** (zero‑weight users never appear in the sampled pool).

  * Forms an eligibility‑filtered candidate pool consistent with PF09 Phase II semantics (normalization/compat/bands/categories already applied).

  * Applies deterministic scoring and tie‑breaking consistent with PF01/PF14 comparators, producing a total order over the candidate pool.

* **Evidence required (titles‑only):**

  * Sampler pool formation and eligibility snapshots.

  * Scoring and ordering logs showing stable rank order across repeated runs under closed rails.

  * Zero‑weight enforcement tests and logs (demonstrating zero‑weight users are excluded).

* **PF references:**

  * PF09 — Canon‑HDE‑Build Checklist, Phase II — Dissolution (HDE‑DISS003.1–.3).

  * PF01 — Canon‑HDE‑Math‑Spec (score and comparator semantics).

  * PF14 — Canon‑HDE‑Mechanics Guide (sampler/ranker mechanics and ordering module).

  * PF12 — Canon‑HDE‑Schemas and Artifacts (sampler snapshot / evidence schemas).

  * PF19 — Canon‑Glow QA Guide (determinism test patterns and QA token mappings).

---

##### Deliverable D2 — Seedable dev/admin sampler flows (HDE-DISS003.4)

* **PF09 scope:**

  * HDE‑DISS003.4 — Seedable sampler behavior for dev/admin.

* **Job to be done:**  
   Ensure dev/admin‑only sampler flows accept an optional seed and, under closed rails, produce byte‑identical outputs for identical inputs \+ seed without changing any public‑visible bytes or external behavior.

* **Evidence required (titles‑only):**

  * Seed replay logs demonstrating two‑run identity and ABBA behavior for sampler outputs.

  * Tests/logs proving that enabling/disabling seed affects only candidate ordering and not the underlying pool or public result payload.

* **PF references:**

  * PF09 — Canon‑HDE‑Build Checklist, Phase II (HDE‑DISS003.4).

  * PF14 — Canon‑HDE‑Mechanics Guide (sampler dev/admin flows).

  * PF19 — Canon‑Glow QA Guide (two‑run identity QA mappings and rails).

---

##### Deliverable D3 — Dev-only sampler endpoint harness (HDE-DISS003.5)

* **PF09 scope:**

  * HDE‑DISS003.5 — Dev‑only sampler endpoint harness.

* **Job to be done:**  
   Provide a dev‑only sampler endpoint harness that:

  * Exposes candidate IDs and seed echo in canonical JSON, suitable for QA and debugging.

  * Uses the same deterministic sampler/ranker logic as CLI harnesses.

  * Remains clearly non‑public and adheres to PF19/PF04 rails for dev/admin surfaces.

* **Evidence required (titles‑only):**

  * Endpoint harness tests and logs demonstrating canonical JSON, two‑run identity, and AB↔BA behavior for sampler outputs.

  * Evidence that endpoint is gated by dev/admin rails (e.g., auth/whitelist checks, environment flags).

* **PF references:**

  * PF05 — Canon‑HDE‑CLI‑API‑Vendor‑Ref (endpoint surfaces and CLI/HTTP behavior).

  * PF09 — Canon‑HDE‑Build Checklist, Phase II (HDE‑DISS003.5).

  * PF19 — Canon‑Glow QA Guide (rails and QA playbooks for dev‑only endpoints).

  * PF02 — Canon‑HDE‑Architecture (placement of sampler endpoint within the engine architecture).

---

##### Deliverable D4 — Sampler/ranker evidence and indexing (HDE-DISS003.6)

* **PF09 scope:**

  * HDE‑DISS003.6 — Sampler evidence & Index/Mirror coverage.

* **Job to be done:**  
   Bring sampler/ranker artifacts into the governed Evidence Index & Machine Mirror with path‑proofs, enforcing canonical JSONL (UTF‑8, one LF), fixed field order, and unknown‑key rejection for mirror entries, in parity with compat/category evidence.

* **Evidence required (titles‑only):**

  * Updated human Evidence Index entries and hash sentinel for sampler evidence families.

  * Updated machine Evidence Mirror records (JSONL) for sampler snapshots, diversity checks, and seed replay logs, with `proof_anchor` fields pointing to path‑proof files.

  * Path‑proof artifacts showing that mirror entries match underlying artifacts.

* **PF references:**

  * PF09 — Canon‑HDE‑Build Checklist (Evidence Index rules and DISS003.6).

  * PF12 — Canon‑HDE‑Schemas and Artifacts (Index/Mirror schemas, path‑proof structures).

  * PF14 — Canon‑HDE‑Mechanics Guide (evidence tooling and mirror writers).

  * PF19 — Canon‑Glow QA Guide (evidence discipline and QA tokens for Index/Mirror).

---

##### Deliverable D5 — Deterministic Engine Core behavior and evidence (HDE-DISS004.1–.4)

* **PF09 scope:**

  * HDE‑DISS004 — Deterministic Engine Core (task‑level)

  * HDE‑DISS004.1 — Pure compute (no I/O/clocks/globals)

  * HDE‑DISS004.2 — AB↔BA & two‑run identity for Engine Core

  * HDE‑DISS004.3 — Canonical JSON compare for core artifacts

  * HDE‑DISS004.4 — Engine core evidence & indexing

* **Job to be done:**  
   Prove the Engine Core is a pure‑compute unit that:

  * Performs no I/O, does not touch clocks, environment, filesystem, network, or process‑wide globals under governed rails.

  * Satisfies AB↔BA neutrality and two‑run identity for core operations (same inputs under closed rails → same outputs; swapping A/B yields expected neutral/compatible behavior).

  * Emits any JSON evidence in canonical form and passes canonical‑compare checks.

  * Has all governed core evidence indexed and mirrored with path‑proofs alongside sampler and compat/category evidence.

* **Evidence required (titles‑only):**

  * Static guard report showing no I/O/clocks/globals for core code paths.

  * Two‑run identity logs for core computations.

  * ABBA/AB↔BA identity bytes/logs for Engine Core behavior.

  * Canonical‑JSON compare logs for core evidence artifacts.

  * Index/Mirror entries and path‑proofs for all core evidence families.

* **PF references:**

  * PF09 — Canon‑HDE‑Build Checklist, Phase II (HDE‑DISS004.\*).

  * PF14 — Canon‑HDE‑Mechanics Guide (Engine Core semantics, ABBA/two‑run proofs).

  * PF12 — Canon‑HDE‑Schemas and Artifacts (core evidence schemas and mirror records).

  * PF19 — Canon‑Glow QA Guide (determinism and no‑I/O QA playbooks).

  * PF01 — Canon‑HDE‑Math‑Spec (core math invariants).

  * PF02 — Canon‑HDE‑Architecture (Engine Core component boundaries).

#### 2.4.4 PF Reference Map

This epic leans on the following PF documents and sections (titles \+ sections only; bytes single‑homed there):

* **PF21 — 7 Phases of Alchemical Engineering**

  * Phase: Dissolution (phase definition and rationale).

* **PF06 — Canon‑Epic‑Process‑Guide**

  * Epic lifecycle, Codex PR discipline, roles (Lead Dev, PO, QA, Master Scrum).

* **PF09 — Canon‑HDE‑Build Checklist**

  * Phase II — Dissolution (tasks HDE‑DISS003.\* and HDE‑DISS004.\*; Evidence Index rules).

* **PF19 — Canon‑Glow QA Guide**

  * QA rails, QA Acceptance Tokens Registry §9A, determinism env pins, QA checklists, and evidence expectations.

* **PF20 — Canon‑HDE‑Phased Epics**

  * §2.2 HDE‑EPIC017 — HD Calcination Pass 2 (foundations).

  * §2.3 HDE‑EPIC018 — HDE Calcination Pass 3 (determinism, serializer, evidence skeleton).

  * §2.1 Epic Record Template (normative structure for this epic).

* **PF01 — Canon‑HDE‑Math‑Spec**

  * Score computation, comparators, and ordering invariants used by sampler/ranker and core.

* **PF02 — Canon‑HDE‑Architecture**

  * Engine Core, sampler/ranker, CLI, and HTTP endpoint placement within the system.

* **PF04 — Canon‑HDE‑Governance**

  * Token semantics, env rails policy, Codex/QA authority semantics.

* **PF05 — Canon‑HDE‑CLI‑API‑Vendor‑Ref**

  * CLI commands and dev‑only endpoints relevant to sampler and Engine Core evidence flows.

* **PF07 — Canon‑Glow‑Infrastructure**

  * Environment layout, env pins, SAFE\_MODE/ALLOW\_NETWORK defaults for CI and prod‑like runs.

* **PF12 — Canon‑HDE‑Schemas and Artifacts**

  * Evidence Index schema, Machine Mirror schema, path‑proof structures, and sampler/core evidence shapes.

* **PF14 — Canon‑HDE‑Mechanics Guide**

  * Sampler/ranker mechanics, Deterministic Engine Core mechanics, evidence tooling, determinism harnesses.

* **PF03 — Technical Writing Best Practices**

  * Style and structure expectations for doc deltas and evidence documentation.

* **PF10 — HDE‑Build Notes (status context only)**

  * Historical notes and prior Dissolution / prototype attempts; not used as evidence.

#### 2.4.5 Tokens and Evidence (Acceptance)

##### Baseline acceptance tokens (reused)

These tokens are considered required baseline for any HDE epic and are reused here; their semantics remain single‑homed in PF04/PF19:

* `PR_OPENED_OK`

* `TESTS_PASS_OK`

* `DOC_DELTA_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `QA_PRECOMMIT_CHECKLIST_OK`

* `QA_POSTCOMMIT_CHECKLIST_OK`

* `ENV_RAILS_POLICY_OK`

* `DETERMINISM_ENV_PINS_OK`

* `SANITY_PIPELINE_OK` (for determinism/sanity pipeline when new evidence families are wired).

##### Phase‑specific tokens for HDE-EPIC019

EPIC019 must satisfy the following Phase II Dissolution tokens for sampler/ranker and Engine Core surfaces (names per PF09/PF19):

* **Determinism and parity:**

  * `TWO_RUN_IDENTITY_OK` (extended to sampler and Engine Core evidence suites).

  * `COMPOSITE_ABBA_IDENTITY_OK` (composite ABBA identity across compat \+ sampler \+ core where applicable).

  * `AB_BA_PARITY_OK` (AB↔BA parity for sampler and Engine Core operations).

* **Engine purity:**

  * `NO_IO_NO_CLOCKS_OK` (pure compute Engine Core under governed rails).

* **Canonical JSON for sampler/core/evidence:**

  * `JSON_CANONICAL_CHECK_OK` (canonical JSON checks applied to sampler and core evidence artifacts).

* **Evidence Index & Mirror discipline:**

  * `EVIDENCE_INDEX_UPDATED_OK` (already in baseline; must explicitly include sampler/core families).

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

The meanings and QA mappings for these tokens remain governed by PF19 §9A; EPIC019’s responsibility in PF20 is to require them for epic completion and ensure evidence is present and indexed for them in this epic’s acceptance map.

##### Evidence families (titles‑only)

Evidence must be captured and indexed according to PF12/PF09/PF14; titles below are families, not exhaustive file lists:

* **Sampler/ranker evidence:**

  * Sampler pool/eligibility snapshots.

  * Sampler ABBA / AB↔BA logs.

  * Sampler two‑run identity logs.

  * Diversity checks artifacts (window/bound/recent constraints).

  * Seed replay logs (dev/admin).

* **Dev‑only sampler endpoint harness evidence:**

  * Endpoint request/response snapshots in canonical JSON.

  * Endpoint two‑run and AB↔BA parity logs.

  * Evidence of rails gating (auth/flags).

* **Engine Core evidence:**

  * Static guard report for “no I/O/clocks/globals”.

  * Engine Core two‑run identity logs.

  * Engine Core ABBA identity bytes/logs.

  * Canonical JSON compare logs for core evidence.

* **Index/Mirror and path‑proof evidence:**

  * Updated human Evidence Index entries and hash sentinel for sampler and Engine Core evidence families.

  * Machine Mirror JSONL entries for sampler/core artifacts (fixed field order, unknown‑key rejection, canonical JSONL).

  * Path‑proof artifacts for sampler and Engine Core evidence entries.

Each evidence family must be reflected in both the human Evidence Index and Machine Mirror, and mapped to the corresponding tokens in the acceptance roster for HDE‑EPIC019.

#### 2.4.6 QA Rails — Open/Close (Final PR)

Rails posture for HDE‑EPIC019 follows PF19/PF04 and the determinism patterns from HDE‑EPIC018; this epic extends those rails to sampler and Engine Core suites.

* **Closed‑rails requirement for determinism suites:**

  * All CI jobs that prove sampler/core determinism and evidence invariants must run under:

    * `SAFE_MODE=1`

    * `ALLOW_NETWORK=0`

    * `LC_ALL=C`, `LANG=C`

    * `TZ=UTC`

    * Any additional pins specified in PF19/PF04 (e.g., locale and randomness controls).

  * These jobs must be explicitly wired to `DETERMINISM_ENV_PINS_OK` and `ENV_RAILS_POLICY_OK` with env‑log/path‑proof evidence recorded in the Evidence Index and Mirror.

* **Rails behavior for dev-only sampler endpoint harness:**

  * Tests for the dev‑only endpoint harness must respect rails policies:

    * Endpoint is only available under dev/admin conditions (e.g., feature flag, auth guard, restricted environment).

    * No external I/O or network is performed beyond what PF05/PF07 explicitly permit for dev‑only diagnostics.

    * Logs remain governed (no user PII, keys‑only where required).

  * Rails‑related QA tokens from PF19 (e.g., `ENV_RAILS_POLICY_OK`, QA checklist tokens) must be satisfied for endpoint tests.

* **Final PR acceptance conditions:**

  * HDE‑EPIC019 cannot be marked Done in PF20 until:

    * All Deliverables D1–D5 are satisfied with passing tests under governed rails.

    * Baseline and phase‑specific tokens listed in §2.1.5 are present and Green in the final Codex close pack for this epic.

    * Evidence for all required tokens is indexed in the human Evidence Index and Machine Mirror with path‑proofs (per PF09/PF12/PF14).

    * QA checklist tokens (`QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK`) confirm that pre‑commit and post‑commit QA posture has been followed for sampler and Engine Core changes.

* **QA execution pattern:**

  * EPIC019 will follow the PF06/PF19 pattern of:

    * Codex PRs for implementation and evidence work.

    * A dedicated Live QA / final QA PR under governed rails (prod‑like Codespaces), capturing final evidence snapshots and acceptance map entries for this epic.

#### 24.7 Tracked Issues

At planning time for HDE‑EPIC019:

* **Tracked intra‑epic issues:**

  * None yet. This section is intentionally empty at kickoff; issues will be minted during implementation/QA only when reality diverges from plan or canon, per PF20 §2.1.7.

* **Cross‑epic issues (PF20 §1):**

  * Existing cross‑epic issues such as `ISSUE-017-NO-USER-QA`, `ISSUE-017-STATELESS-JSON-QA`, and `ISSUE-QA-TOKENS-LIBRARY` remain tracked in PF20 §1 and may receive additional evidence from HDE‑EPIC019 but are not explicitly assigned to this epic at kickoff.

* **Future disposition rule (normative for this epic):**

  * At epic close, every intra‑epic issue discovered under HDE‑EPIC019 must be either:

    * Completed under HDE‑EPIC019,

    * Carried forward to a named future epic,

    * Promoted to a cross‑epic ISSUE‑XXX in PF20 §1, or

    * Explicitly dropped with a one‑line rationale, in line with PF20’s normative rules.

ASK OK?

