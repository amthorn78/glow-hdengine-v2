**Title**: PF20-Reference-HDE-Phased Epics

**Status:** Reference

**Version:** v1.8

**Effective date:** 2026-03-19

**Last Update Gate:** HDE-EPIC027 Closure

**Invocation tag:** INV-f2ac55d77ce9aacc

## **0\. Purpose & Scope**

**Historical reference only. Not for planning.**

PF20 is a **reference ledger** of historical epic records and their trace pointers. It is not an epic planning document and must not be used to derive requirements, gates, or “what to do next.”

This document is the single PF home for:

* **Mapping** each HDE epic to an alchemical phase (Calcination → Coagulation) as defined in **7 Phases of Alchemical Engineering** (titles-only).

* **Recording** per-epic historical intent, deliverables, PF references, acceptance token names, and evidence pointers **as they existed for that epic**.

* **Recording** cross-epic “Outstanding issues” as a **historical index** of known gaps and carry-forward decisions.

**Historicals only. Not to be used for planning of any kind:**

* PF20 MUST NOT be used to plan new epics, define acceptance rosters, choose tokens, design QA, design evidence capture, or decide rails posture.

* PF20 MUST NOT be used as a source of “baseline token rosters” or “required now” requirements.

* If a reader needs planning guidance, they MUST consult the owning PF documents (titles-only). PF20 may point to those documents, but PF20 itself is not authoritative for planning rules.

This document does not redefine:

* Governance primitives, token registry, or token semantics (titles-only).

* Math mechanics (titles-only).

* Epic execution flow (titles-only).

* Build/CI wiring and checklist status semantics (titles-only).

* QA playbooks, QA planning, or Live QA runbooks (titles-only).

* Evidence schemas and artifact conventions (titles-only).

* Templates (titles-only).

Those remain single homes. PF20 only records what an epic **claimed/used/produced**, plus where evidence was stored, for historical traceability.

### **Token naming discipline (historical recording rules)**

PF20 may contain token names as they were recorded in historical epic artifacts. Token names in PF20 are **not** authoritative requirements.

* When interpreting any token name in PF20, the canonical source of truth is the Token Registry in **HDE Governance** (titles-only).

* PF20 must not introduce token aliases. If a historical epic record contains a token alias, it must be treated as **historical drift**, not something to copy forward.

* For `/internal/version` specifically:

  * The canonical conditional semantics token name is `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`.

  * Any alias intended to mean “conditionals return 200 and never 304” (including `INTERNAL_VERSION_COND_200_NO_304_OK`) is non-canon and must be treated as drift if present in historical artifacts.

  * Older epic records may contain legacy `INTVER_*` alias tokens as historical artifacts. Do not copy them forward into new acceptance rosters.

### **PF23 consult (planning is out of scope here)**

PF20 does not define planning posture. Planning rules that require PF23 consultation live in the owning canon (titles-only). PF20 may cite PF23 anchors as provenance for how an epic was scoped, but PF20 does not restate PF23 contents and must not be used as a substitute for PF23 in any plan.

### **Portability vs provenance (historical references)**

PF20 may reference non-PF artifacts (reports, logs, step outputs) as provenance. These references are historical pointers only.

* Historical epic records may cite external artifacts. Those citations must not be treated as execution dependencies for new work.

* Any portability/provenance rules for plans, remediation guides, or QA execution are governed elsewhere (titles-only). PF20 does not restate them.

### **QA and runbook exclusion (hard rail)**

PF20 is not a QA planning or runbook document.

* PF20 MUST NOT embed QA runbooks or step-level QA planning (commands, procedures, operator walkthroughs, step sequences, QA\_ROOT design, evidence directory naming conventions, README generator rules, or “do X then Y” execution scripts).

* PF20 may record (historically) whether Live QA was required for an epic close and may name governing documents by title.

### **OPS and remediation posture (historical references only)**

PF20 may mention OPS tasks and remediation guides as part of historical epic records. The execution rules, templates, and verification discipline for OPS and remediation are governed elsewhere (titles-only). PF20 does not restate those rules and must not be used as an OPS/remediation planning guide.

### **Template posture**

PF27 is the canonical home for Epic Plan and QA Plan templates. PF20 MUST NOT embed or duplicate templates.

### **Drain posture (maintenance rules for this reference ledger)**

* During drains, do not mass-edit historical epic records.

* Closed epics (Status: Done) do not need to be updated during Build Notes drains.

* Only update a prior epic record when the change prevents future reader confusion (for example: a wrong token name, a wrong canonical evidence filename/path, or a broken cross-reference that would mislead interpretation). Otherwise, treat prior epic records as historical snapshots.

### **Build Notes posture (historical context)**

PF10 Build Notes are living context. When PF10 is referenced inside PF20, avoid BN version strings and brittle section anchoring. Prefer the relevant Addendum entry (number \+ title) when available.

### **Scope note — epics not yet recorded in PF20**

If an epic does not yet have a PF20 “Epic Record,” PF20 has nothing to say about its planning or acceptance. Do not infer requirements from PF20. Planning artifacts must use the owning canon and templates (titles-only).

---

## **Phase Exit Criteria (planning rule)**

**Historical interpretation only. Not a planning gate.**

PF20 records phases and epic outcomes historically. Any “phase exit” language in PF20 is a retrospective description of what was treated as “exit-ready” at the time, not a rule to plan against.

When PF20 records that a phase was treated as exit-ready, the historical basis typically included:

* At least one epic in that phase recorded as Status: Done with its D-goals accepted and a completed “Tokens and Evidence (Acceptance)” roster for that epic record.

* A close pack (manifest, close report, acceptance map) with required evidence indexed under the evidence discipline recorded for that phase.

* No “Not done” foundation rows left for that phase in the build checklist, or explicit disposition of remaining items (rescoped, carried forward, or explicitly dropped with rationale).

* Tracked issues for Done epics explicitly disposed (completed, carried forward, promoted to cross-epic issue, or explicitly dropped).

PF20 does not enforce these criteria for new work. For current planning and phase discipline, consult the owning canon and templates (titles-only).

---

## **1\. Outstanding Issues (Cross-Epic)**

Use this section to track **open, cross-cutting issue IDs** that may span multiple epics and phases.

PF20 intentionally keeps this ledger **allocation-only** to prevent document bloat. An entry MAY remain `\<allocated\>` indefinitely.

* PF20’s job is to reserve and reference the Issue ID.

* Detailed description, acceptance criteria, and evidence pointers (if needed) MUST live in the owning epic record(s) and/or governed artifacts (titles-only), not in PF20 §1.

### Allocated issue IDs (canonical ledger)

**Issue record: ISSUE-017-NO-USER-QA \<allocated\>**

**Issue record: ISSUE-017-STATELESS-JSON-QA \<allocated\>**

**Issue record: ISSUE-QA-TOKENS-LIBRARY \<allocated\>**

**Issue record: ISSUE-APPENV-D3-GATING \<allocated\>**

**Issue record: ISSUE-EVIDENCE-MIRROR-SELF-RECORD \<allocated\>**

**Issue record: ISSUE-EVIDENCE-SCHEMA-VALIDATION-DEPS \<allocated\>**

**Issue record: ISSUE-INTVER-CONDITIONAL-ARTIFACT-KEYS \<allocated\>**

**Issue record: ISSUE-INTVER-AUTH-POSTURE \<allocated\>**

**Issue record: ISSUE-CLI-SHOWCOMPAT-EXITCODE-DRIFT \<allocated\>**

**Issue record: ISSUE-PF04-TOKEN-REGISTRY-DRIFT \<allocated\>**

**Issue record: ISSUE-MIRROR-SCHEMA-INVOKE-DRIFT \<allocated\>**

**Issue record: ISSUE-CODESPACES-QA-CONFIG \<allocated\>**

**Issue record: ISSUE-LIVEQA-GITLESS-RUNBOOKS \<allocated\>**

**Issue record: ISSUE-LIVEQA-PLAN-LINT \<allocated\>**

---

## **2\. Epic Records (Per‑Epic Tracking)**

This template has been moved to PF27.

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

* **Status: `Done`**

* **Deliverables: D1–D4 Done, D5 Completed (manifest \+ close report \+ doc-deltas); EPIC011 ingest remains parked for a future epic.**

* **`Date started: 2025-11-21`**

* **`Date completed: 2025-11-26`**  
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

  * `artifacts/engine/order/channels_sorted.snapshot.json` — channel ordering snapshot.

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

* **Status:** Done  
* **Date started:** 2025-11-26

* **Date completed:** 2025-11-29

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

  * PF20 §2.2 records EPIC017 as Done with D1–D4 Done and D5 Completed, leaving ingest and stateless JSON QA for future epics; it also allocates cross‑epic issues ISSUE‑017‑NO‑USER‑QA and ISSUE‑017‑STATELESS‑JSON‑QA for follow‑up. HDE-EPIC018 builds directly on this base for serializer, determinism rails, and evidence skeleton but does not itself close the cross‑epic issues unless explicitly extended.

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

### **2.4 HDE-EPIC019 Epic Plan**

#### 2.4.1 Meta

* **Epic ID:** HDE-EPIC019

* **Epic name (short):** Dissolution Pass 2

* **Alchemical phase:** Dissolution

* **Phase rationale (1–3 sentences):**  
   PF09 Phase II — Dissolution (“Normalize and make it pure”) defines this phase as the place where already-normalized inputs are carried through to deterministic, schema‑governed engine behavior for compat, sampler/ranker, and the core engine, with evidence integrated into the global Evidence Index and Machine Mirror. HDE-EPIC019 is the second Dissolution pass and is responsible for closing the remaining Not done work for the swipe sampler/ranker (HDE‑DISS003) and deterministic engine core (HDE‑DISS004) so that Phase II behavior is deterministic, reproducible, and fully evidenced under the same rails Calcination epics hardened.

* **Related boards:**

  * Glow HDE Epics tracking board — epic row/card for `HDE-EPIC019` (to be created/linked per PF20 §2 “Epic Records (Per‑Epic Tracking)”).

* **Status:** Done

* **Date started:** 2025-11-29

* **Date completed:** 2025-12-05

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

  * Any sampler/ranker or engine-core prototypes noted in PF10 — HDE-Build Notes are treated as historical input only; they are not evidence. They may be referenced by Addendum ID and short title during implementation but must be superseded by PF09/PF12/PF14-aligned evidence under EPIC019.

##### Existing tokens validated (reused, not re‑proved)

* **From Calcination epics and PF19 (determinism, serializer, baseline rails):**

  * Canonical JSON and determinism:

    * `JSON_CANONICAL_CHECK_OK`

    * `TWO_RUN_IDENTITY_OK`

    * `COMPOSITE_ABBA_IDENTITY_OK`

    * `AB_BA_PARITY_OK` (proved for compat and category layers)

  * Baseline PR / rails / evidence discipline:

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

##### **Deliverable D1 — Sampler/ranker deterministic pool and scoring (HDE-DISS003.1–.3)**

* **PF09 scope:**

  * HDE-DISS003 — Swipe Sampler & Ranker (task-level)

  * HDE-DISS003.1 — Zero-weight rule enforcement

  * HDE-DISS003.2 — Pool formation & eligibility filters

  * HDE-DISS003.3 — Deterministic scoring & total order

* **Job to be done:**  
   Implement the sampler/ranker such that it:

  * Honors viewer weights and **enforces zero-weight rules** (zero-weight users never appear in the sampled pool).

  * Forms an eligibility-filtered candidate pool consistent with PF09 Phase II semantics (normalization/compat/bands/categories already applied).

  * Applies deterministic scoring and tie-breaking consistent with PF01/PF14 comparators, producing a total order over the candidate pool.

* **Evidence required (titles-only):**

  * Sampler pool formation and eligibility snapshots.

  * Scoring and ordering logs showing stable rank order across repeated runs under closed rails.

  * Zero-weight enforcement tests and logs (demonstrating zero-weight users are excluded).

* **Implementation note (non-normative):**  
   As of PR 2 for HDE-EPIC019, the “deterministic pool and scoring” behavior for this deliverable is realized by the pure-compute sampler core in `engine/sampler/core.py` (exported via `engine/sampler/__init__.py`) together with unit tests in `tests/unit/test_sampler_core.py`; this module enforces zero-weight exclusion, PF09/PF14-aligned eligibility rules, and deterministic ordering using existing comparators, all without introducing I/O, clocks, environment reads, or module-level global state.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist, Phase II — Dissolution (HDE-DISS003.1–.3).

  * PF01 — Canon-HDE-Math-Spec (score and comparator semantics).

  * PF14 — Canon-HDE-Mechanics Guide (sampler/ranker mechanics and ordering module).

  * PF12 — Canon-HDE-Schemas and Artifacts (sampler snapshot / evidence schemas).

  * PF19 — Canon-Glow QA Guide (determinism test patterns and QA token mappings).

---

##### **Deliverable D2 — Seedable dev/admin sampler flows (HDE-DISS003.4)**

* **PF09 scope:**

  * HDE-DISS003.4 — Seedable sampler behavior for dev/admin.

* **Job to be done:**  
   Ensure dev/admin-only sampler flows accept an optional seed and, under closed rails, produce byte-identical outputs for identical inputs \+ seed without changing any public-visible bytes or external behavior.

* **Evidence required (titles-only):**

  * Seed replay logs demonstrating two-run identity and ABBA behavior for sampler outputs.

  * Tests/logs proving that enabling/disabling seed affects only candidate ordering and not the underlying pool or public result payload.

* **Implementation note (non-normative):**  
   As of PR 3 for HDE-EPIC019, the seedable dev/admin sampler flows for this deliverable are realized via a dev/admin-only `hdctl` subcommand `dev:sampler` that is gated by `APP_ENV` (restricted to dev/test/local), reads a JSON candidates payload into the pure-compute sampler core used for Deliverable D1, and emits canonical JSON on stdout that includes the viewer identifier, the seed echo, and ranked candidate details under closed rails. In this PR, the `seed` argument is metadata-only and does **not** influence candidate selection or ordering; any future seed-based tie-breaking behavior will be added in subsequent epic work while preserving the determinism and candidate-set stability required by this PF20 record. This CLI command is an internal QA/admin harness, not part of the public user-facing CLI contract; detailed CLI bytes and harness semantics remain single-homed in the CLI/API and schema documents (titles-only, e.g. CLI/API reference and schemas & artifacts), not here.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist, Phase II (HDE-DISS003.4).

  * PF14 — Canon-HDE-Mechanics Guide (sampler dev/admin flows).

  * PF19 — Canon-Glow QA Guide (two-run identity QA mappings and rails).

---

##### **Deliverable D3 — Dev-only sampler endpoint harness (HDE-DISS003.5)**

* **PF09 scope:**

  * HDE-DISS003.5 — Dev-only sampler endpoint harness.

* **Job to be done:**  
   Provide a dev-only sampler endpoint harness that:

  * Exposes candidate IDs and seed echo in canonical JSON, suitable for QA and debugging.

  * Uses the same deterministic sampler/ranker logic as CLI harnesses.

  * Remains clearly non-public and adheres to PF19/PF04 rails for dev/admin surfaces.

* **Evidence required (titles-only):**

  * Endpoint harness tests and logs demonstrating canonical JSON, two-run identity, and AB↔BA behavior for sampler outputs.

  * Evidence that endpoint is gated by dev/admin rails (for example explicit environment gating and writer-style forbidden envelopes outside allowed dev/admin environments).

* **Implementation note (non-normative):**  
   As of the EPIC019 implementation work, this deliverable is realized by a dev/admin-only HTTP sampler harness at `POST /internal/dev/sampler` on the internal reader surface. The handler uses the same pure-compute sampler core as Deliverables D1/D2, building `ViewerProfile` and `CandidateFeatures` from the incoming candidate IDs and calling the sampler’s `sample_and_rank` function without changing eligibility or ordering semantics. It emits canonical JSON (UTF-8, sorted keys, compact, single trailing newline) containing only `viewer_id`, `meta.seed`, and the ordered `candidate_ids` list.

   **Normative gating requirement:** in line with PF05/PF14/PF04 and the EPIC019 design, this harness is **intended** to be strictly gated by `APP_ENV`: requests are permitted only when `APP_ENV` is explicitly one of `dev`, `test`, or `local`; missing, empty, or any other `APP_ENV` value **must** result in a writer-style `403 forbidden` envelope. The HTTP harness mirrors the dev sampler CLI semantics (seed is echoed as metadata but does not alter ranking in this epic) and remains an internal dev/admin tool: it is excluded from the Endpoint Catalog and A7 proofs, and detailed HTTP bytes, host/port bindings, and rails semantics remain single-homed in the CLI/API reference, infrastructure, governance, mechanics, and QA guide documents (titles-only).

   **Discovery vs. expected behavior:** subsequent discovery runs in a prod-like Codespaces environment (recorded in PF10 — HDE Build Notes and infra/QA artifacts by title) have confirmed that, when a dev Reader process is started under closed rails with `APP_ENV=dev`, the harness responds on its infra-defined base URL with well-formed HTTP/1.1 and the canonical JSON body described above. The same discovery also observed that, in that environment, invoking the harness under `APP_ENV=prod` can still yield `HTTP/1.1 200 OK` with canonical JSON rather than the expected 403 writer envelope. This does **not** change the normative gating requirement; it indicates a **gating discrepancy** (behavioral or configuration bug) that must be corrected by remedial implementation and/or infra wiring so that runtime behavior matches PF05/PF14/PF04 and this D3 record.

   **Infra posture and Live QA:** remedial infra work for EPIC019 (tracked in PF10 — HDE Build Notes and infra docs by title) now provides a canonical dev Reader start helper and an infra-owned dev sampler URL binding for Codespaces/local dev. For the purposes of PF20:

  * D3 acceptance remains contingent on:

    * a working dev Reader HTTP harness in the target environment, with its base URL and dev sampler URL defined and validated by infra per PF07/PF09/PF14; and

    * correct `APP_ENV` gating behavior at the harness (200 with canonical JSON under `APP_ENV ∈ {dev,test,local}`; 403 writer envelope under `APP_ENV` values outside that set, including `prod`, missing, or empty), proven by adapter tests and at least one Live QA run.

  * For **live HTTP QA runs** (for example steps that call `/internal/dev/sampler` from a Codespaces shell), when QA rails are correctly set (for example `SAFE_MODE=1`, appropriate `ALLOW_NETWORK` posture, `APP_ENV=dev` for the allowed call and `APP_ENV=prod` for the gated call) and the request payload matches the handler’s expected JSON shape:

    * If the HTTP call fails at the protocol layer (for example `HTTP_STATUS:000`, HTTP/0.9 errors, or otherwise no HTTP/1.x status and no JSON body), the result MUST be classified as an **infra/tooling failure** (for example `FAIL_TOOLING` in QA logs): the dev sampler handler has not been invoked, and D3 behavior and gating remain unproven.

    * If the HTTP call succeeds at the protocol layer but returns a `200 OK` response under `APP_ENV` values that are supposed to be forbidden (for example `APP_ENV=prod`), this MUST be treated as a **gating bug or misconfiguration**, not as a passing D3 run: the behavior diverges from the normative gating requirement above and D3 acceptance is not satisfied until the implementation/infra wiring is corrected and the expected 403 behavior is observed and evidenced.

* Under these rules, D3 cannot be marked satisfied or Green for this epic in PF20 until both: (1) a working dev Reader HTTP harness and infra-owned dev sampler URL exist and are validated per PF07/PF09/PF14, and (2) Live QA evidence shows `/internal/dev/sampler` behaving according to the APP\_ENV gating semantics described here for both allowed (`APP_ENV=dev/test/local`) and forbidden (`APP_ENV=prod`/missing/empty) modes, with the resulting logs and artifacts wired into the EPIC019 acceptance map and manifest.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist, Phase II (HDE-DISS003.5).

  * PF14 — Canon-HDE-Mechanics Guide (sampler dev/admin flows and dev/internal harness semantics).

  * PF19 — Canon-Glow QA Guide (rails, QA failure classifications, and QA playbooks for dev-only endpoints).

  * PF07 — Glow Infrastructure (dev Reader HTTP harness and infra-owned dev sampler URLs).

  * PF05 — HDE-CLI-API-Vendor-Ref (endpoint surfaces and HTTP behavior).

  * PF02 — HDE-Architecture (placement of sampler endpoint within the engine architecture).

---

##### **Deliverable D4 — Sampler/ranker evidence and indexing (HDE-DISS003.6)**

* **PF09 scope:**

  * HDE-DISS003.6 — Sampler evidence & Index/Mirror coverage.

* **Job to be done:**  
   Bring sampler/ranker artifacts into the governed Evidence Index & Machine Mirror with path-proofs, enforcing canonical JSONL (UTF-8, one LF), fixed field order, and unknown-key rejection for mirror entries, in parity with compat/category evidence, so that sampler behavior (pool, ordering, diversity, seed behavior) is evidenced under the same discipline as compat and category layers.

* **Evidence required (titles-only):**

  * **Sampler evidence families (names-only; schemas, artifacts, and Mirror records governed by the schemas & artifacts and mechanics docs):**

    * `sampler_pool_snapshots` — sampler pool/eligibility snapshot artifacts (viewer, candidate IDs, bands, compat scores, weights, eligibility flags) with governed artifacts under `artifacts/sampler/pool_snapshots/…` and a sampler pool snapshots schema under `docs/schemas/sampler/pool_snapshots.schema.json`.

    * `sampler_two_run_logs` — sampler two-run identity logs (same inputs → identical ordering), with artifacts under `artifacts/sampler/two_run/…` and a corresponding two-run logs schema.

    * `sampler_abba_logs` — AB/BA/ABBA sampler runs for parity checks, with artifacts under `artifacts/sampler/abba/…` and an ABBA logs schema.

    * `sampler_diversity_artifacts` — diversity/window/recent-constraint evidence, with artifacts under `artifacts/sampler/diversity/…` and a diversity artifacts schema.

    * `sampler_seed_replay_logs` — seed replay logs from dev sampler CLI/HTTP harnesses, showing repeated seeded runs and proving seed-echo semantics and candidate-set stability, with artifacts under `artifacts/sampler/seed_replay/…` and a seed replay logs schema.

  * **Index & sentinel (human Evidence Index; titles-only):**

    * `docs/evidence/INDEX.json` entries for each sampler family (artifact\_key names such as `sampler_pool_snapshots`, `sampler_two_run_logs`, `sampler_abba_logs`, `sampler_diversity_artifacts`, `sampler_seed_replay_logs`) pointing to the governed sampler artifacts above.

    * `docs/evidence/INDEX.sha256` regenerated over the canonical bytes of `docs/evidence/INDEX.json` after sampler families are added.

  * **Machine Evidence Mirror & path-proofs (JSONL, Mirror-wide discipline):**

    * `artifacts/evidence_index.jsonl` records for sampler artifacts and their schemas, each with the full Mirror field set (including `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`) and governed field order, in parity with existing compat/category evidence families.

    * Path-proof transcripts (`*.path_proof.txt`) for each sampler artifact and schema (for example sampler pool snapshots, two-run identity logs, ABBA logs, diversity artifacts, seed replay logs, and their schemas), with path, `sha256`, `size_bytes`, and UTC time fields consistent with the corresponding Mirror records.

  * **Tests and tooling (titles-only):**

    * Sampler evidence generator tooling (for example a dedicated sampler evidence generator that calls the sampler core plus dev sampler CLI/HTTP harnesses under closed rails) and the evidence-index update toolchain used to wire sampler families into the Index/Mirror and sentinel.

    * Evidence tests (for example `tests/evidence/test_sampler_evidence.py` and related suites) that:

      * validate sampler artifacts against their schemas;

      * assert that `docs/evidence/INDEX.json` contains sampler family entries with the expected shapes and that `docs/evidence/INDEX.sha256` matches the canonical Index body; and

      * verify that `artifacts/evidence_index.jsonl` contains sampler Mirror records matching the Index entries and that each sampler artifact/schema has a corresponding path-proof referenced by `proof_anchor`.

* **Implementation note (non-normative):**  
   As of PR 5 for HDE-EPIC019, this deliverable is realized by defining the sampler evidence families `sampler_pool_snapshots`, `sampler_two_run_logs`, `sampler_abba_logs`, `sampler_diversity_artifacts`, and `sampler_seed_replay_logs`, generating their governed artifacts under `artifacts/sampler/**` via a sampler evidence generator that reuses the sampler core and dev sampler harnesses under closed rails, adding matching sampler schemas under `docs/schemas/sampler/**`, and extending `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` with sampler entries and path-proofs via the existing evidence tooling. A follow-up bugfix PR corrects a provenance defect by refreshing the sampler Mirror entries and their path-proof transcripts so that `produced_at_utc` for sampler families reflects the actual evidence refresh time and matches the corresponding path-proof timestamps.

   For D4, EPIC019 is considered complete when these sampler families, artifacts, schemas, Index/Mirror entries, and path-proofs are present and coherent under the schemas & artifacts and mechanics canon; detailed schema shapes, Mirror field semantics, and provenance rules remain single-homed in those PF documents. As of the HDE-EPIC019 QA summary referenced in this version (combined CI sampler evidence tests and Live QA Step 5 in the prod Codespace run), those conditions are met: the sampler families above exist under governed paths, their schemas and Index/Mirror entries are wired and validated by `tests/evidence/test_sampler_evidence.py` and related suites, and acceptance map/manifest bindings for D4 tokens point at these artifacts. This deliverable is therefore treated as **satisfied** for HDE-EPIC019; future epics may add new sampler evidence families or QA playbooks without reopening D4, provided they respect the same PF12/PF14 evidence discipline.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist (Evidence Index rules and DISS003.6).

  * PF12 — Canon-HDE-Schemas and Artifacts (Index/Mirror schemas, sampler evidence families, path-proof structures).

  * PF14 — Canon-HDE-Mechanics Guide (evidence tooling, sampler evidence generator, Mirror writers).

  * PF19 — Canon-Glow QA Guide (evidence discipline and QA tokens for Index/Mirror).

    

---

##### **Deliverable D5 — Deterministic Engine Core behavior and evidence (HDE-DISS004.1–.4)**

* **PF09 scope:**

  * HDE-DISS004 — Deterministic Engine Core (task-level)

  * HDE-DISS004.1 — Pure compute (no I/O/clocks/globals)

  * HDE-DISS004.2 — AB↔BA & two-run identity for Engine Core

  * HDE-DISS004.3 — Canonical JSON compare for core artifacts

  * HDE-DISS004.4 — Engine core evidence & indexing

* **Job to be done:**  
   Prove the Engine Core is a pure-compute unit that:

  * Performs no I/O, does not touch clocks, environment, filesystem, network, or process-wide globals under governed rails.

  * Satisfies AB↔BA neutrality and two-run identity for core operations (same inputs under closed rails → same outputs; swapping A/B yields expected neutral/compatible behavior).

  * Emits any JSON evidence in canonical form and passes canonical-compare checks.

  * Has all governed core evidence indexed and mirrored with path-proofs alongside sampler and compat/category evidence.

* **Evidence required (titles-only):**

  * Static guard report showing no I/O/clocks/globals for core code paths.

  * Two-run identity logs for core computations.

  * ABBA/AB↔BA identity bytes/logs for Engine Core behavior.

  * Canonical-JSON compare logs for core evidence artifacts.

  * Index/Mirror entries and path-proofs for all core evidence families.

* **Implementation note (non-normative):**  
   As of the completed HDE-EPIC019 work, this deliverable is realized in two parts:

  * **Behavior (HDE-DISS004.1–.3):**  
     The pure-compute Engine Core module in `engine/core/core.py` (exported via `engine/core/__init__.py`) with the frozen dataclasses `ParticipantState`, `CoreConfig`, `PerspectiveBreakdown`, and `CoreResult` as the Engine Core input/output structures. A dedicated test suite under `tests/core/` enforces (under closed determinism rails) that Engine Core code paths import without side effects (no I/O, env, clocks, network, or globals), satisfy AB↔BA neutral metrics for neutral outputs, and exhibit two-run identity and JSON-ready `CoreResult` semantics when serialized via `dataclasses.asdict` with sorted keys.

  * **Evidence & indexing (HDE-DISS004.4):**  
     Engine Core evidence families are added as governed artifacts and schemas and wired into the Evidence Index and Machine Mirror with path-proofs, mirroring the sampler evidence pattern for D4 (titles-only; shapes and field semantics remain single-homed in the schemas & artifacts and mechanics documents). Specifically:

    * Engine Core evidence families (names-only, governed elsewhere), for example:

      * `engine_core_purity_report` — purity report artifacts under `artifacts/core/purity/…` with a corresponding Engine Core purity-report schema.

      * `engine_core_two_run_logs` — Engine Core two-run identity logs under `artifacts/core/two_run/…` with a corresponding two-run logs schema.

      * `engine_core_abba_logs` — Engine Core AB/BA/ABBA parity logs under `artifacts/core/abba/…` with a corresponding ABBA logs schema.

      * `engine_core_json_compare_logs` — canonical JSON compare logs for Engine Core evidence under `artifacts/core/json_compare/…` with a corresponding JSON-compare logs schema.

    * Human Evidence Index entries and hash sentinel for these families (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`), plus Machine Mirror JSONL records in `artifacts/evidence_index.jsonl` and path-proof transcripts (`*.path_proof.txt`) that satisfy the Mirror and provenance invariants alongside sampler evidence.

    * Inclusion of these Engine Core evidence generators and checks in the closed-rails determinism/sanity pipeline and env-pins gate so that the pipeline produces canonical `sanity.log` and env-pins logs whose updated hashes and sizes are reflected in the Human Evidence Index, Machine Mirror, path-proofs, and the EPIC019 manifest.

* EPIC019’s acceptance map and manifest now bind the D5-related tokens (for example `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `NO_IO_NO_CLOCKS_OK`, and the relevant `EVIDENCE_INDEX_*`/`EVIDENCE_PATHS_VALIDATED_OK`/`MACHINE_MIRROR_UPDATED_OK` tokens) to these Engine Core evidence families, sanity/env-pins runs, and Index/Mirror artifacts, and new audit tests enforce manifest↔acceptance map consistency for these bindings. For D5, HDE-EPIC019 is considered complete when the Engine Core behavior and evidence requirements above are satisfied under governed rails and the EPIC019 acceptance map and manifest show all D5 tokens as Green with corresponding governed artifacts and tests, with detailed schema shapes, evidence family layouts, and Mirror/provenance rules remaining single-homed in the schemas & artifacts, mechanics, governance, and QA canon.

   As of the HDE-EPIC019 QA summary reflected in this version, those conditions are met at the repo/CI level and reinforced by Live QA: Engine Core behavior tests (`tests/core/**`) and Engine Core evidence tests (`tests/evidence/test_engine_core_evidence.py` and related suites) run and pass under closed determinism rails; Engine Core evidence families appear in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` with governed path-proofs; and the determinism/sanity pipeline and env-pins CI jobs execute successfully, producing canonical `artifacts/sanity/sanity.log` and env-pins logs whose hashes and sizes match their Index/Mirror and manifest entries. The Codespace Live QA run for Step 6 re-exercised core behavior and evidence tests successfully; Step 7’s attempt to invoke the sanity pipeline from that environment produced no captured log and is classified in the QA summary as a **tooling/logging gap for that environment**, not as a failure of D5 behavior or evidence, because the closed-rails CI pipeline remains the canonical evidence for `SANITY_PIPELINE_OK` and `DETERMINISM_ENV_PINS_OK` in this epic. Taken together, D5 is therefore treated as **satisfied** for HDE-EPIC019 in PF20; any future changes to Engine Core evidence or the sanity pipeline must preserve these properties and update PF09/PF12/PF14/PF19 and the EPIC019 acceptance map/manifest accordingly.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist, Phase II (HDE-DISS004.\*).  
  * PF14 — Canon-HDE-Mechanics Guide (Engine Core semantics, ABBA/two-run proofs, evidence tooling).  
  * PF12 — Canon-HDE-Schemas and Artifacts (core evidence schemas and mirror records).  
  * PF19 — Canon-Glow QA Guide (determinism and no-I/O QA playbooks).  
  * PF01 — Canon-HDE-Math-Spec (core math invariants).  
  * PF02 — Canon-HDE-Architecture (Engine Core component boundaries).

##### **Deliverable D6 — Live vendor transport proof under open rails (EPIC019 vendor D-goal)**

* **PF09 scope:**

  * Vendor ingest–related Dissolution tasks for this epic (titles-only; see PF09 Phase II vendor ingest / live vendor QA tasks for normative scope and names).

* **Job to be done:**  
   Demonstrate at least **one real vendor transport** for this epic under **open rails**, in a prod-like environment, with evidence sufficient to prove that:

  * `ALLOW_NETWORK=1` was enabled and rails were explicitly set to an open-rails posture appropriate for Live Vendor QA (including `SAFE_MODE` and core determinism pins, per PF04/PF19);

  * a real HTTP or CLI call reached the vendor (for example via engine/Reader/CLI ingest paths as defined in PF05/PF14/PF07), and a response (success or controlled failure) was received; and

  * the rails and environment at the time of the vendor call were captured as evidence alongside the transport trace.

* Closed-rails tests (for example ingest unit tests, local harnesses, or CI runs with `ALLOW_NETWORK=0`) may prove sampler/core mechanics and evidence wiring but **cannot**, by themselves, satisfy this D6 D-goal for live vendor activity.

* **Evidence required (titles-only):**

  * **Open-rails environment baseline:**

    * A dedicated env/rails baseline log for the Live Vendor QA run (for example `audit/qa/hde-epic019/D0_env_rails_open.log`), recording at least `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, and `TZ` and clearly marking the session as an open-rails Live Vendor QA run for HDE-EPIC019.

  * **Prod connectivity to vendor / Railway:**

    * Discovery evidence that vendor-facing endpoints are reachable from the QA environment (for example a connectivity check to the canonical Railway host/port or vendor gateway URL under open rails, with response or connection failure captured as a governed log).

    * This evidence must distinguish “no path to vendor” (pure infra failure) from “vendor responded with an application or transport error.”

  * **Reader/CLI service readiness (dev/prod harness):**

    * Evidence that the engine/Reader/CLI surfaces used for live vendor calls are running and reachable in the target environment (for example a simple CLI/HTTP health check to a known internal endpoint with an HTTP/1.x status and JSON body before attempting vendor calls).

  * **Live vendor transport trace (minimum proof):**

    * At least one governed log or JSON artifact under `audit/qa/hde-epic019/…` that shows:

      * the exact command or HTTP request used to trigger vendor ingest (CLI or Reader/HTTP), including target URL or CLI arguments and rails context;

      * the resulting HTTP status and headers for the vendor-facing call (including vendor host/URL or an unambiguous proxy of it per PF14/PF07); and

      * either a successful vendor response (for example a JSON payload or an expected success code) or a controlled, documented failure (for example a vendor 4xx/5xx, timeout, or auth failure) that still proves real transport to the vendor surface.

    * This evidence must be sufficient to support a QA acceptance token (for example `LIVE_VENDOR_TRANSPORT_OK`) in PF19 §9A, with EPIC019 consuming that token by name in its acceptance map.

  * **Rails and discovery linkage (names-only):**

    * A short QA summary artifact for the Live Vendor QA session (for example `audit/qa/hde-epic019/qa_rerun_vendor_live_summary.md`) that:

      * ties the vendor transport trace back to the rails baseline log and any discovery artifacts (for example service topology, Railway endpoints, Reader/CLI readiness);

      * states explicitly whether the vendor call met the intended acceptance condition (for example “success response from vendor X under open rails” or “controlled failure from vendor X under open rails”); and

      * identifies which PF19 QA tokens and PF09 tasks this evidence satisfies (names-only, for example `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, `DISCOVERY_BASELINE_OK` once those tokens are registered in PF19).

* **Implementation note (non-normative):**  
   For HDE-EPIC019, this deliverable is a **Live QA D-goal** that sits on top of the sampler/core mechanics and evidence work in D1–D5. The sampler and Engine Core mechanics and evidence families (D1–D5) may be exercised entirely under closed rails and CI harnesses, but D6 requires at least one **explicit Live Vendor QA run** under open rails, using the actual engine/Reader/CLI surfaces and vendor/Railway topology described in PF05/PF07/PF14, with rails, environment, and transport captured as governed evidence.

   As of the Remediation PR for D6 (Card C3), this D-goal is realized via a dedicated **open-rails Live Vendor QA harness** (`scripts/qa/d6_live_vendor_qa.py`, titles-only) that:

  * pins `ALLOW_NETWORK=1`, `SAFE_MODE=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC` for its runs, and records these pins (plus `APP_ENV` and vendor host) in a governed `rails_snapshot` artifact under `audit/qa/hde-epic019/d6-vendor-live-qa/…`;

  * exercises the canonical HDAPI BodyGraph endpoint (for example via the vendor’s `/bodygraphs` route as defined by PF05/PF07/PF14) using a minimal BodyGraph payload; and

  * classifies outcomes as:

    * `OK` — 2xx status and successfully parsed JSON response, captured in a **happy-path** JSONL log;

    * `FAIL_VENDOR` — non-2xx vendor responses (for example 4xx/5xx with structured JSON error bodies) captured in a **fail\_vendor** JSONL log; and

    * `FAIL_TOOLING` — infra/tooling failures (for example DNS or connection failures such as `https://invalid.invalid`) captured in a **fail\_tooling** JSONL log.

* The Human Evidence Index and Machine Mirror now carry EPIC019 D6 evidence families (artifact\_keys names only), for example:

  * `epic019.d6.vendor_live_qa.discovery_notes` → discovery notes for the D6 harness and vendor surfaces;

  * `epic019.d6.vendor_live_qa.happy_path` → governed JSONL log(s) for OK runs;

  * `epic019.d6.vendor_live_qa.fail_vendor` → governed JSONL log(s) for vendor-side failures;

  * `epic019.d6.vendor_live_qa.fail_tooling` → governed JSONL log(s) for infra/tooling failures;

  * `epic019.d6.vendor_live_qa.rails_snapshot` → governed rails snapshot JSON for the D6 Live Vendor QA session.

* Each of these families has an entry in `docs/evidence/INDEX.json`, a corresponding Machine Mirror record in `artifacts/evidence_index.jsonl`, and a governed path-proof (`*.path_proof.txt`), and the evidence skeleton/orientation demo checks have been updated to remain coherent after adding this D6 skeleton. The **EPIC019 acceptance map** now includes a D6 foundation “D6 — Live vendor QA and classification (HDE-EPIC019 remedial)” whose `tokens` and `manifest_tokens` sets include the Live Vendor QA tokens:

  * `LIVE_VENDOR_TRANSPORT_OK` — tied to the D6 harness and its happy-path and failure logs;

  * `OPEN_RAILS_ENV_OK` — tied to the D6 rails snapshot and happy-path log(s);

  * `DISCOVERY_BASELINE_OK` — tied to the discovery notes and rails snapshot.

* The `audit/EPIC019_MANIFEST.json` entry for each token binds it to these artifact\_keys and their governed artifacts (with paths, hashes, sizes, and proof anchors matching the Evidence Index and Machine Mirror), and dedicated audit tests enforce acceptance map ↔ manifest consistency for D6.

   For D6, HDE-EPIC019 is considered complete when:

  * at least one OK run and at least one classified failure (FAIL\_VENDOR and/or FAIL\_TOOLING) exist as governed D6 logs under open rails;

  * a governed rails snapshot and discovery baseline tie those logs to their rails and infra context; and

  * the D6 tokens (`LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, `DISCOVERY_BASELINE_OK`) are Green in the EPIC019 acceptance map and manifest and their evidence is indexed in the Evidence Index and Machine Mirror as described. As of the D6 Remediation PR summarized here, those conditions are satisfied at the repo/CI level for EPIC019; any future Live Vendor QA epics must either build on these D6 families or extend them in a way that maintains PF12/PF14 evidence discipline and PF19 token semantics.

* **PF references:**

  * PF09 — Canon-HDE-Build Checklist, Phase II (HDE-DISS003 vendor ingest / live vendor QA tasks).

  * PF14 — Canon-HDE-Mechanics Guide (vendor ingest mechanics and Live Vendor QA harness expectations).

  * PF12 — Canon-HDE-Schemas and Artifacts (evidence families, Evidence Index & mirror schema, path-proof structures).

  * PF19 — Canon-Glow QA Guide (§9A QA Acceptance Tokens Registry; Live Vendor QA tokens and evidence mappings).

  * PF07 — Glow Infrastructure (vendor endpoints, environment layout, SAFE\_MODE/ALLOW\_NETWORK defaults).

  * PF05 — HDE-CLI-API-Vendor-Ref (HDAPI transport bytes and vendor POST surfaces).

  * PF02 — HDE-Architecture (placement of vendor ingest paths and Live Vendor QA harnesses within the system).

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

#### **2.4.5 Tokens and Evidence (Acceptance)**

##### **Baseline acceptance tokens (reused)**

These tokens are considered required baseline for any HDE epic and are reused here; their semantics remain single-homed in PF04/PF19:

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

  ##### **Phase-specific tokens for HDE-EPIC019**

EPIC019 must satisfy the following Phase II Dissolution tokens for sampler/ranker, Engine Core, and Live Vendor QA surfaces (names per PF09/PF19):

* **Determinism and parity (sampler and core):**

  * `TWO_RUN_IDENTITY_OK` (extended to sampler and Engine Core evidence suites).

  * `COMPOSITE_ABBA_IDENTITY_OK` (composite ABBA identity across compat \+ sampler \+ core where applicable).

  * `AB_BA_PARITY_OK` (AB↔BA parity for sampler and Engine Core operations).

* **Engine purity (core):**

  * `NO_IO_NO_CLOCKS_OK` (pure compute Engine Core under governed rails).

* **Canonical JSON for sampler/core/evidence:**

  * `JSON_CANONICAL_CHECK_OK` (canonical JSON checks applied to sampler and core evidence artifacts).

* **Evidence Index & Mirror discipline (sampler/core families):**

  * `EVIDENCE_INDEX_UPDATED_OK` (already in baseline; must explicitly include sampler/core families).

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

* **Live Vendor QA (D6):**

  * `LIVE_VENDOR_TRANSPORT_OK` — Live Vendor QA token satisfied when at least one open-rails D6 harness run demonstrates a real vendor transport (HDAPI BodyGraph) with a governed happy-path log and at least one classified failure, backed by D6 evidence families and indexed artifacts.

  * `OPEN_RAILS_ENV_OK` — rails token satisfied when the D6 harness produces a governed rails snapshot showing `ALLOW_NETWORK=1`, `SAFE_MODE=0`, pinned locale/TZ, and PF-Canon references for the D6 Live Vendor QA session.

  * `DISCOVERY_BASELINE_OK` — discovery token satisfied when a D6 discovery note and rails snapshot exist and describe the Live Vendor QA surfaces, env keys, and rail choices for EPIC019.

The meanings and QA mappings for all of these tokens remain governed by PF19 §9A (and PF04/PF09/PF12/PF14 as referenced there); EPIC019’s responsibility in PF20 is to require them for epic completion and ensure evidence is present and indexed for them in this epic’s acceptance map and manifest.

##### **Evidence families (titles-only)**

Evidence must be captured and indexed according to PF12/PF09/PF14; titles below are families, not exhaustive file lists:

* **Sampler/ranker evidence (D1/D4):**

  * Sampler pool/eligibility snapshots.

  * Sampler ABBA / AB↔BA logs.

  * Sampler two-run identity logs.

  * Diversity/window/recent-constraint evidence.

  * Seed replay logs (dev/admin).

* **Dev-only sampler endpoint harness evidence (D3):**

  * Endpoint request/response snapshots in canonical JSON.

  * Endpoint two-run and AB↔BA parity logs.

  * Evidence of APP\_ENV gating (dev/test/local allowed; forbidden modes returning writer 403).

* **Engine Core evidence (D5):**

  * Static guard report for “no I/O/clocks/globals”.

  * Engine Core two-run identity logs.

  * Engine Core ABBA identity bytes/logs.

  * Canonical JSON compare logs for core evidence.

* **Index/Mirror and path-proof evidence (D4/D5 and shared):**

  * Updated human Evidence Index entries and hash sentinel for sampler and Engine Core evidence families.

  * Machine Mirror JSONL entries for sampler/core artifacts (fixed field order, unknown-key rejection, canonical JSONL).

  * Path-proof artifacts for sampler and Engine Core evidence entries.

* **Live Vendor QA evidence (D6):**

  * D6 discovery notes and vendor surface description (EPIC019 D6 discovery baseline).

  * D6 happy-path JSONL log(s) for OK vendor runs.

  * D6 fail\_vendor JSONL log(s) for vendor-side errors.

  * D6 fail\_tooling JSONL log(s) for infra/tooling failures.

  * D6 rails snapshot JSON documenting open-rails posture (env pins, vendor host, PF-Canon references).

Each evidence family must be reflected in both the human Evidence Index and Machine Mirror, and mapped to the corresponding tokens in the acceptance roster for HDE-EPIC019.

##### **EPIC019 acceptance map (titles-only)**

* `docs/acceptance_map_epic019.json` — EPIC019 acceptance map that enumerates Deliverables **D1–D6** and their PF19/PF09 QA tokens and exposes a `token_status` table keyed by token name. The acceptance map and `audit/EPIC019_MANIFEST.json` together form the canonical acceptance roster for this epic:

  * For each deliverable D1–D5, the acceptance map lists the PF19/PF09 tokens that must be satisfied (for example sampler determinism and purity tokens for D1, rails and CLI/endpoint QA tokens for D2–D3, sampler evidence tokens for D4, and Engine Core determinism and evidence tokens for D5), and the `token_status` table records, for each token, its status plus titles-only references to the tests and governed artifacts that prove it.

  * For D6, the acceptance map includes a foundation “D6 — Live vendor QA and classification (HDE-EPIC019 remedial)” whose `tokens` and `manifest_tokens` sets include `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK`. Each of these tokens has its `tests` and `artifacts` lists populated with titles-only references to the D6 harness and D6 evidence families (for example the D6 discovery note, rails snapshot, and the happy\_path, fail\_vendor, and fail\_tooling JSONL logs).

  * The EPIC019 manifest binds each token to concrete evidence artifacts (for example the epic manifest and acceptance map themselves, sampler and Engine Core evidence families in the Evidence Index and Machine Mirror, D6 discovery/rails snapshot/logs, and the determinism/sanity pipeline and env-pins logs), and dedicated audit tests assert that every token in the acceptance map is backed by manifest entries whose artifact titles and paths match the map’s declared evidence homes.

  * In the final, closed state for HDE-EPIC019, all required baseline, phase-specific, and Live Vendor QA tokens for this epic (as listed in §2.4.5) are expected to be Green in this acceptance map/manifest pair, with non-empty `tests` and `artifacts` lists that point to governed evidence families under the schemas & artifacts and mechanics canon; PF20 records this structure and the requirement that manifest, acceptance map, Evidence Index, and Machine Mirror remain in sync, but the detailed schema shapes, evidence family layouts, and token semantics remain single-homed in the governance, build, schemas, and QA documents.

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

    * Carried forward to a named future epic,

    * Promoted to a cross‑epic ISSUE‑XXX in PF20 §1, or

    * Explicitly dropped with a one‑line rationale, in line with PF20’s normative rules.

#### **2.4.7 Tracked Issues**

No tracked issues were explicitly recorded in this PF20 epic record at the time of closure. Any later-discovered cross-cutting issues MUST be tracked in §1 “Outstanding Issues (Cross-Epic)” and explicitly disposed of in the relevant future epic record(s).

### **2.5 HDE-EPIC020 Epic Plan**

#### 2.5.1 Meta

* **Epic ID:** HDE-EPIC020

* **Epic name (short):** Separation Pass 1 — Error & Identity Surfaces

* **Alchemical phase:** Separation (Phase III, per PF21 — 7 Phases of Alchemical Engineering)

* **Phase rationale (1–3 sentences):**  
   Separation Phase III in PF09/PF21 is where public and operator-visible surfaces are given a stable, canonical shape with explicit identity and guardrails. HDE-EPIC020 applies these Separation semantics to three surfaces: the error envelope and token set, the shared public presenter/emitter, and the `/internal/version` identity surface, wiring all three to canonical JSON, determinism, and indexed evidence building on the Calcination/Dissolution foundation.

* **Related boards:**

  * HDE Engine Phase III / Separation board (Separation lane; exact IDs to be assigned by Master Scrum).

* **Status:** `Done`

* **Date started:** 2025-12-05

* **Date completed:** 2025-12-08

---

#### 2.5.2 Existing Work Check (MUST)

##### Existing features review (summary)

The following features and flows already cover part of this epic’s intent and are treated as existing coverage rather than new obligations:

* **Persistence & Evidence Index foundation (Phase III, Task HDE-SEPA001.\*):**  
   Persistence layer, logging discipline, DB grants, service identity snapshot, and persistence evidence indexing are already Done and provide the Separation foundation this epic builds on.

* **Canonical JSON & determinism rules (Calcination / prior epics):**  
   Canonical bytes and determinism rules for the engine have already been proved under earlier epics (EPIC017 and successors) and are treated as pre-existing serialization and invariance canon for error and presenter flows.

* **`/internal/version` transport & header posture (HDE-SEPA004.2, 004.3):**  
   Header and conditional behavior for `/internal/version` (no 304, `Cache-Control: no-store`, no ETag, stable JSON body across conditionals) were proved via EPIC017 Live QA and are not re-opened by this epic.

* **Existing `/internal/version` identity evidence (EPIC018):**  
   EPIC018 contributed env/prod handshake artifacts for `/internal/version` identity but left the body contract (field set and canonical ordering) and explicit coupling to frozen identity artifacts open. Those partial artifacts are reused as context but do not satisfy this epic’s identity/two-run obligations.

##### Existing tokens validated (names-only)

Tokens that are already satisfied and reused, not re-proved:

* **Identity / ops tokens for `/internal/version` transport & caching:**

  * `INTVER_CONDITIONALS_IGNORED_OK`

  * `INTVER_200_NO_ETAG_OK`

* **Persistence / Evidence Index baseline tokens (from HDE-SEPA001.\*):**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

These tokens remain in effect and are referenced in this epic as prerequisites for error, presenter, and ops identity evidence wiring.

##### Existing evidence located (titles/paths only)

The following evidence sets are treated as inputs to planning and as support for “Existing Work,” not as new deliverables:

* `/internal/version` transport and header posture (EPIC017 Live QA):

  * `audit/qa/hde-epic017/logs/intver_get_full.txt`

  * `audit/qa/hde-epic017/logs/intver_head_full.txt`

  * `audit/qa/hde-epic017/logs/intver_get_conditional.txt`

* `/internal/version` env/prod handshake (EPIC018 QA):

  * `audit/qa/hde-epic018/d2-env/d2-env-prod-handshake-001.*` (body, stderr, related logs)

* Global Evidence Index and Machine Mirror:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

##### Gap statement (what remains unproven / drifting)

* **Error envelope & token set (HDE-SEPA002.\*):**

  * No proved canonical JSON for error bodies; numeric-free, governed error envelope shape is unproved.

  * Error transport headers and success-path header posture for writers/errors are not validated.

  * Error token map and casing remain unproved.

  * Reader/CLI error parity and CLI error stream discipline are not covered.

  * Error-envelope evidence is not fully indexed into the Evidence Index and Mirror.

* **Public presenter / emitter (HDE-SEPA003.\*):**

  * Shared presenter/emitter symbol between Reader and CLI is not enforced or evidenced.

  * `showcompat` canonical JSON output is unproved (non-empty, sorted keys, LF-terminated).

  * Presenter stream discipline (stdout LF, stderr-only for errors) is not enforced.

  * AB↔BA and two-run identity for presenter surfaces is unproved.

  * Preimage recompute and identity coupling for public bodies have not been demonstrated.

  * Presenter evidence is not indexed according to global Evidence Index/Mirror rules.

* **Internal ops identity surface `/internal/version` (HDE-SEPA004.1 & 004.4):**

  * GET/HEAD header and body parity for `/internal/version` is unproved under Separation requirements.

  * Two-run identity for `/internal/version` bodies and explicit coupling of identity fields (e.g., `engine_tag`, `release_id`, `invocation_tag`, `build_commit`, `emitter_sha256`, `invocation_sha256`) to frozen identity artifacts is unproved.

  * Identity evidence and path-proofs are not yet wired into the Evidence Index/Mirror as a complete identity surface.

---

#### 2.5.3 Deliverables (Jobs To Be Done)

##### D1 — Error Envelope & Token Set (HDE-SEPA002.\*)

* **Job to be done (clear, testable):**  
   Establish a central, canonical error envelope and token set for the engine such that all governed error surfaces:

  * emit numeric-free, canonical JSON error bodies;

  * use correct transport headers on the writers/errors route;

  * share a validated, governed error token map and casing;

  * maintain Reader/CLI parity and CLI error stream discipline; and

  * produce indexed error evidence in the Evidence Index and Mirror.

* **PF09 scope mapping:**

  * Task `HDE-SEPA002 — Error Envelope & Token Set`

  * Subtasks `HDE-SEPA002.1` through `HDE-SEPA002.8` (all Not done, explicitly assigned to this epic).

* **Evidence required (titles/paths only; to be produced or updated):**

  * `errors/schema_check/*` — schema and canonical JSON checks for error envelope.

  * `tests/transport/headers/no_store_writers_errors.snap` — header posture snapshots for writers/errors success route.

  * `errors/token_map/*` — governed error token map and casing samples.

  * `parity/errors_reader_cli.*` — Reader/CLI error parity bytes.

  * Evidence Index/Mirror entries in:

    * `docs/evidence/INDEX.json`

    * `docs/evidence/INDEX.sha256`

    * `artifacts/evidence_index.jsonl` (error-envelope-specific keys).

* **PF references (titles \+ sections only):**

  * PF09 — Canon-HDE-Build Checklist: Phase III, Task HDE-SEPA002 and subtasks.

  * PF14 — Canon-HDE-Mechanics Guide: error transport mechanics and stream discipline sections.

  * PF12 — Canon-HDE-Schemas and Artifacts: error envelope JSON schema and artifact layout.

  * PF02 — Canon-HDE-Architecture: error surfaces and writer/reader topology.

  * PF05 — Canon-HDE-CLI-API-Vendor-Ref: CLI error surfaces and contract.

  * PF19 — Canon-Glow QA Guide: QA tokens and Live/CI posture for error flows.

  * PF04 — Canon-HDE-Governance: error token semantics and naming.

**Scope note (clarification):**  
 For HDE-EPIC020, D1 is scoped to **engine/Reader dev harness and CLI error semantics** only. In particular:

* D1 acceptance covers:

  * CLI usage-error behavior for at least one canonical `hdctl` error scenario (for example, `showcompat` missing required flags) under dev rails; and

  * compat error envelope behavior on the engine/Reader dev harness (including malformed-JSON handling) at the documented dev HTTP surface, with numeric-free, canonical JSON error bodies and correct headers, as governed by PF05/PF14/PF19.

* Vendor ingest flows and the broader compat HTTP matrix (for example vendor-backed compat happy paths, additional error modes, and A7-adjacent transport checks) are **explicitly deferred** to future Separation/Conjunction epics that own vendor ingest QA and A7-like transport, and **are not part of D1 acceptance** for HDE-EPIC020. Any expectations around vendor ingest compat must be tracked via cross-epic issues and later D-goals, not retrofitted into this epic.

---

##### D2 — Public Presenter / Emitter (HDE-SEPA003.\*)

* **Job to be done (clear, testable):**  
   Pin a single, allow-listed presenter/emitter implementation shared by Reader and CLI, and prove that all presenter surfaces (including `showcompat`) emit canonical JSON with governed stream discipline and deterministic bytes, backed by identity-coupled preimage evidence indexed in the Evidence Index and Mirror.

* **PF09 scope mapping:**

  * Task `HDE-SEPA003 — Public Presenter / Emitter` (status: Not done).

  * Subtasks `HDE-SEPA003.1`–`HDE-SEPA003.6` (Not done; no epic assigned yet in PF09, now explicitly owned by HDE-EPIC020).

* **Evidence required (titles/paths only; to be produced or updated):**

  * `artifacts/cli/guards/emitter_symbol_proof.txt` — shared emitter entrypoint proof.

  * `artifacts/cli/guards/serializer_grep_guard.log` — guard against ad-hoc serializers.

  * `artifacts/presenter/preimage_recompute.log` — preimage recompute and canonical JSON checks.

  * `artifacts/presenter/reader_cli_parity.bytes` — Reader/CLI parity sample for presenter surfaces.

  * CLI harness logs under `artifacts/cli/` or `audit/qa/hde-epic020/` demonstrating stream discipline and LF termination.

  * Evidence Index/Mirror entries binding presenter artifacts under appropriate `artifact_key` values in:

    * `docs/evidence/INDEX.json`

    * `artifacts/evidence_index.jsonl`.

* **PF references (titles \+ sections only):**

  * PF09 — Canon-HDE-Build Checklist: Task HDE-SEPA003 and subtasks.

  * PF14 — Canon-HDE-Mechanics Guide: presenter/emitter mechanics and identity coupling.

  * PF12 — Canon-HDE-Schemas and Artifacts: canonical JSON and Evidence Index schema.

  * PF01 — Canon-HDE-Math Spec: identity/preimage hashing semantics.

  * PF02 — Canon-HDE-Architecture: presenter/emitter integration across Reader and CLI.

  * PF05 — Canon-HDE-CLI-API-Vendor-Ref: CLI showcompat behavior and public JSON contracts.

  * PF19 — Canon-Glow QA Guide: QA tokens for canonical JSON and two-run identity.

  * PF04 — Canon-HDE-Governance: token semantics and naming for presenter, determinism, and evidence.

---

##### D3 — Internal Ops Identity Surface `/internal/version` (HDE-SEPA004.1 & 004.4)

* **Job to be done (clear, testable):**  
   Complete `/internal/version` as the operator-only identity surface for the engine by proving:

  * GET/HEAD header and body parity under Separation;

  * two-run identity for `/internal/version` bodies under pinned environment; and

  * explicit coupling of identity fields to frozen identity artifacts, with governed evidence indexed into the Evidence Index and Mirror.

* **PF09 scope mapping:**

  * Task `HDE-SEPA004 — Internal Ops Surface /internal/version` (epic: Separation; mixed status).

  * Subtasks in-scope for this epic:

    * `HDE-SEPA004.1 — GET/HEAD header parity` (Not done).

    * `HDE-SEPA004.4 — Two-run identity and identity coupling` (Not done).

  * Subtasks already complete and treated as existing coverage:

    * `HDE-SEPA004.2 — Conditionals ignored (never 304)` (Done).

    * `HDE-SEPA004.3 — No-store & no ETag posture` (Done).

* **Evidence required (titles/paths only; to be produced or updated):**

  * `artifacts/ops/internal_version/headers_get.txt`

  * `artifacts/ops/internal_version/headers_head.txt`

  * `artifacts/ops/internal_version/body_get.json`

  * `artifacts/ops/internal_version/body_get.sha256`

  * `artifacts/ops/internal_version/two_run_identity.log`

  * Identity/provenance artifacts:

    * `artifacts/math/freeze_pack_manifest.json`

    * `artifacts/math/release_id.txt`

    * `artifacts/math/release_id_recompute.log`

    * `artifacts/identity/emitter_sha256.txt`

  * Updated Evidence Index/Mirror entries for `/internal/version` identity artifacts and logs.

* **PF references (titles \+ sections only):**

  * PF09 — Canon-HDE-Build Checklist: Task HDE-SEPA004 and subtasks.

  * PF14 — Canon-HDE-Mechanics Guide: identity and provenance mechanics, `/internal` surfaces.

  * PF12 — Canon-HDE-Schemas and Artifacts: identity artifacts, freeze pack manifest, Evidence Index schema.

  * PF01 — Canon-HDE-Math Spec: identity hashing (`idempotence_hash`, `release_id`) and two-run identity math.

  * PF02 — Canon-HDE-Architecture: internal ops endpoints and service identity.

  * PF19 — Canon-Glow QA Guide: QA rails and identity proof tokens.

  * PF04 — Canon-HDE-Governance: identity contract (field set and canonical ordering) and token semantics.

---

#### 2.5.4 PF Reference Map

This epic relies on the following PF documents and sections (titles \+ sections only, no duplicated bytes):

* **PF21 — 7 Phases of Alchemical Engineering:**

  * Phase III — Separation (public shape, identity, guardrails) semantics.

* **PF06 — Canon-Epic-Process-Guide:**

  * §1.1 Standard epic flow (PLAN → CRD → IP → PR).

  * Multi-PR epics and rails defaults.

* **PF20 — Canon-HDE-Phased Epics:**

  * §2.1 Epic Record Template (this section).

  * EPIC017/018/019 entries used for Existing Work Check and D-goal alignment.

* **PF09 — Canon-HDE-Build Checklist:**

  * Phase III / Separation tasks: HDE-SEPA001.*, HDE-SEPA002.*, HDE-SEPA003.*, HDE-SEPA004.*.

* **PF19 — Canon-Glow QA Guide:**

  * Live QA pattern (one command → one primary artifact under `audit/qa/<epic-id>/…`).

  * QA tokens and checklist expectations for CI vs Live QA.

* **PF14 — Canon-HDE-Mechanics Guide:**

  * Mechanics for error transport, presenter/emitter, identity and provenance.

* **PF12 — Canon-HDE-Schemas and Artifacts:**

  * JSON schema expectations and artifact layouts for error envelope, presenter outputs, identity artifacts, and Evidence Index/Mirror.

* **PF01 — Canon-HDE-Math Spec:**

  * Determinism, two-run identity, AB↔BA parity, and identity/preimage hashing semantics.

* **PF02 — Canon-HDE-Architecture:**

  * Integration of presenter/emitter, error surfaces, and `/internal/version` in the engine architecture.

* **PF05 — Canon-HDE-CLI-API-Vendor-Ref:**

  * CLI and API surface contracts for presenter/emitter and error flows.

* **PF04 — Canon-HDE-Governance:**

  * Token semantics, naming conventions, and governance rules for Separation surfaces.

* **PF10 — HDE-Build Notes:**

  * Status and history for prior epics, used only for Existing Work Check and planning, not as evidence (per PF20/PF10 rules).

---

#### 2.5.5 Tokens and Evidence (Acceptance)

This section lists the acceptance tokens that must be green for HDE-EPIC020 to be considered Done, along with evidence families (titles-only) and their scope.

##### D1 — Error Envelope & Token Set (HDE-SEPA002.\*)

* **Canonical JSON & schema tokens:**

  * `ERROR_JSON_CANON_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * Evidence: `errors/schema_check/*`, `artifacts/presenter/preimage_recompute.log` (where reused for canonical checks), updated Evidence Index entries.

* **Token map & casing:**

  * `ERROR_TOKEN_MAP_OK`

  * Evidence: `errors/token_map/*` plus aligned index entries.

* **Parity & stream discipline:**

  * `CLI_READER_EMITTER_PARITY_OK` (for error envelope surfaces shared with presenter).

  * `CLI_STDOUT_LF_OK`

  * `CLI_STDERR_ONLY_ON_ERROR_OK`

  * Evidence: `parity/errors_reader_cli.*`, CLI harness logs under `audit/qa/hde-epic020/errors/*`.

* **Evidence indexing:**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * Evidence: updated entries in `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` covering all error-envelope artifacts.

##### D2 — Public Presenter / Emitter (HDE-SEPA003.\*)

* **Shared emitter symbol:**

  * `CLI_READER_EMITTER_PARITY_OK`

  * Evidence: `artifacts/cli/guards/emitter_symbol_proof.txt`, `artifacts/cli/guards/serializer_grep_guard.log`, plus CI logs proving allow-list enforcement.

* **Canonical `showcompat` output:**

  * `CLI_SHOWCOMPAT_CANON_OK`

  * `JSON_CANONICAL_CHECK_OK`

  * Evidence: `artifacts/presenter/preimage_recompute.log` (canonical JSON and preimage checks), CLI harness logs capturing showcompat output.

* **Stream discipline:**

  * `CLI_STDOUT_LF_OK`

  * `CLI_STDERR_ONLY_ON_ERROR_OK`

  * Evidence: CLI-level tests and logs demonstrating success→stdout (LF-terminated) and errors→stderr only, stored under `audit/qa/hde-epic020/cli_presenter/*`.

* **Two-run and AB↔BA identity:**

  * `TWO_RUN_IDENTITY_OK`

  * `COMPOSITE_ABBA_IDENTITY_OK`

  * Evidence: `artifacts/presenter/reader_cli_parity.bytes` and associated logs capturing AB↔BA and two-run runs.

* **Preimage recompute & indexing:**

  * `PREIMAGE_RECOMPUTE_OK`

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

  * Evidence: `artifacts/presenter/preimage_recompute.log`, Evidence Index/Mirror entries tying presenter artifacts (including preimage logs and parity samples) to governed path-proofs.

##### D3 — Internal Ops Identity Surface `/internal/version` (HDE-SEPA004.1 & 004.4)

* **Header and method parity:**

  * `INTVER_200_CTYPE_JSON_UTF8_OK`

  * `INTVER_HEAD_PARITY_OK`

  * Evidence:

    * `artifacts/ops/internal_version/headers_get.txt`

    * `artifacts/ops/internal_version/headers_head.txt`

    * `artifacts/ops/internal_version/body_get.json` / `body_get.sha256`

* **Two-run identity & identity coupling:**

  * Supports `TWO_RUN_IDENTITY_OK` for `/internal/version` identity surface.

  * Evidence:

    * `artifacts/ops/internal_version/two_run_identity.log`

    * `artifacts/math/freeze_pack_manifest.json`

    * `artifacts/math/release_id.txt`

    * `artifacts/math/release_id_recompute.log`

    * `artifacts/identity/emitter_sha256.txt`  
       with Evidence Index entries binding them into a coherent identity surface.

* **Rails and environment:**

  * `ENV_RAILS_POLICY_OK` (ensuring tests and identity proofs run under governed env pins where required).

  * Evidence: environment logs and CI job configuration consistent with PF06/PF19/PF20 determinism and rails policy.

##### Baseline QA tokens (epic-level)

For all D-goals, the following QA tokens must be Green for epic acceptance:

* `QA_PRECOMMIT_CHECKLIST_OK` — pre-commit QA posture satisfied (PF19).

* `QA_POSTCOMMIT_CHECKLIST_OK` — final QA posture and Live QA (if any) satisfied (PF19).

* `QA_EVIDENCE_ONLY_OK` and `QA_CI_DIFF_SCOPED_OK` for evidence-only / QA-only PRs (PF06/PF19).

**EPIC020 bundles/manifests as epic-level evidence (clarification):**  
 For this epic, the error, presenter, and `/internal/version` D-goals (D1–D3) and their rails tokens are additionally represented as **EPIC020-scoped evidence bundles and manifests**:

* The EPIC020 acceptance map (`docs/acceptance_map_epic020.json`) and manifest (`audit/EPIC020_MANIFEST.json`) are bundled into governed **EPIC020 evidence bundle artifacts** (titles-only) that are registered in the Human Evidence Index and Machine Mirror under epic-specific `artifact_key` values, with path-proofs and closed-rails CI jobs maintaining their integrity.

* These EPIC020 bundles/manifests do not change token semantics or evidence rules; they are the **epic-level aggregation surface** for D1–D3 tokens and evidence, built on top of the underlying error, presenter, and `/internal/version` artifacts and families described above, and integrated into the Evidence Index/Mirror per PF09/PF12/PF14.

* Future Separation/Conjunction epics that add or modify error, presenter, or `/internal/version` behavior **SHOULD** build on this pattern (epic-scoped bundles/manifests \+ Index/Mirror entries) rather than inventing parallel aggregation mechanisms; PF12/PF14/PF19 remain the single homes for bundle schemas, generator mechanics, and QA expectations around these epic-bundled artifacts.

---

#### 2.5.6 QA Rails — Open/Close (Final PR)

This section defines the rails posture for HDE-EPIC020 final PRs, consistent with PF06, PF19, and PF20.

##### Pre-commit / CI rails (default posture)

* All determinism-, canonical-JSON-, and identity-related CI jobs for this epic **MUST** run under closed rails, using the standard determinism env pins:

  * `SAFE_MODE=1`

  * `ALLOW_NETWORK=0`

  * `LC_ALL=C`, `LANG=C`

  * `TZ=UTC`

* as defined in the determinism env helpers and CI workflows for prior epics.

* Any CI job that opens rails (for example, if future Separation tasks required live HTTP) must:

  * explicitly pin policy and env variables;

  * record an env snapshot log under `audit/gates/` or `audit/qa/hde-epic020/`; and

  * attach path-proofs and Evidence Index/Mirror entries in the same PR (PF06, PF19).

* For this epic, presenter/error identity proofs are expected to be **closed-rails** and environment-agnostic; no open-rails vendor transport is required for acceptance (vendor Live QA is handled under prior Distillation epic(s) and PF09 D6 tasks, not here).

##### Post-commit / Live QA rails (if invoked)

* If any Live QA is run for HDE-EPIC020 (e.g., manual checks of error envelope or `/internal/version` from prod-like Codespaces), it must follow PF19’s Live QA pattern:

  * one command → one primary artifact under `audit/qa/hde-epic020/...`;

  * helper artifacts stored alongside and referenced from a QA addendum;

  * copy/paste-ready commands, no ambiguous shell pseudo-code.

* Live QA steps **must not** introduce new production code changes; any QA PR for this epic is evidence-only (`QA_EVIDENCE_ONLY_OK`) and scoped CI (`QA_CI_DIFF_SCOPED_OK`).

##### Rails-related tokens (epic-level)

The following rails-related tokens must be Green in the EPIC020 close pack:

* `ENV_RAILS_POLICY_OK` — env pins and rails policy are respected across CI and QA jobs relevant to this epic.

* `QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK` — QA posture followed.

* `QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK` — for any QA-only/Live QA PRs associated with this epic.

#### **2.5.7 Tracked Issues**

No tracked issues were explicitly recorded in this PF20 epic record at the time of closure. Any later-discovered cross-cutting issues MUST be tracked in §1 “Outstanding Issues (Cross-Epic)” and explicitly disposed of in the relevant future epic record(s).

---

###  **2.6 HDE-EPIC021 Epic Plan**

*HDE-EPIC021 Calcination Pass 4*

(Naming note: PF20 already uses “HDE Calcination Pass 3” for HDE‑EPIC018. This epic keeps the distinct short name “HDE‑EPIC021 Calcination Pass 4” for traceability across PF20, PF09, manifests, and acceptance maps.)

---

#### **2.6.1 Meta**

* **Epic ID:** HDE-EPIC021

* **Epic name (short):** HDE-EPIC021 Calcination Pass 4

* **Alchemical phase:** Calcination (Foundations first)

* **Phase rationale (short):**

  * PF09 Phase I Calcination owns the foundational mechanics for the HD Engine: canonical JSON and determinism primitives, the Evidence Index/Mirror skeleton, registry/config bundles, and QA/rails skeleton that later phases reuse.

  * PF20 records that earlier Calcination epics (HDE-EPIC017, HDE-EPIC018, HDE-EPIC020) closed an initial slice of canonical serializer, determinism rails, evidence skeleton, and config, but left structured gaps in HDE-CALC002 (Canonical Serialization Package) and HDE-CALC003 (Repository and Tooling Skeleton).

  * HDE-EPIC021 is the next Calcination pass to finish the remaining Consolidation pending / Partial / Unknown / Not done rows in HDE-CALC002.\* and HDE-CALC003.\* so Calcination can be treated as a hard base for later phases.

* **Related boards / tracking:**

  * Glow Dev Board — HD Engine lane — epic card “HDE-EPIC021 Calcination Pass 4”.

  * Any mirrored tracking artifacts (JIRA/JSON) must reference this Epic ID and short name and treat PF20 as the single epic-plan source of truth.

* **Status:** Done

* **Date started:** 2025-12-07

* **Date completed:** TBD

* **Evidence status (D1–D3):** Evidence-complete per EPIC021 QA Summary and Live QA Steps 1–7 (PR-level suites plus QA\_ROOT evidence under `audit/qa/hde-epic021/`, including the Live QA readout directory under `audit/qa/hde-epic021/live-qa/`). This epic record is closed as Done with canonical QA token names recorded in §2.6.5 and no placeholder token naming dependencies.

* **Blockers / dependencies:** None recorded in PF20.

  * Note: PF09 may still show Partial on some EPIC021-linked D3 rows due to status wording or legacy placeholder-token notes. Treat that as checklist reconciliation work outside PF20, not as a behavioral blocker for this epic record.

---

#### 2.6.2 Existing Work Check (MUST)

##### Existing features review (summary)

Using PF09, prior Calcination epic records, and PF10 context only as history:

* **Canonical serializer and determinism:**

  * HDE‑EPIC017 and HDE‑EPIC018 implemented the initial canonical serializer for `hdctl showcompat` and Reader compat success paths, including AB↔BA identity, two‑run identity, canonical JSON checks, and deterministic env pins for their harnesses.

  * Core CLI canonicalization harnesses and guard tests exist, including:

    * Canonicalization harness script(s) under `scripts/cli/` driving `hdctl`/Reader comparisons.

    * Artifacts in `artifacts/cli/` such as `ab.json`, `ba.json`, `summary.json`, Reader dumps, AB/BA preimage logs, and serializer guard logs.

    * Serializer guard tests in `tests/cli/` that enforce canonicalization and error envelope behavior for governed JSON surfaces.

* **Evidence skeleton and env pins:**

  * Evidence Index and Machine Mirror exist and are wired into CI for regeneration on evidence‑touching PRs, with canonical index and mirror artifacts under the PF12 evidence catalog.

  * An orientation demo and sanity pipeline are present and partially wired, but discipline around when the Evidence Index and Machine Mirror must be regenerated (same‑PR touch discipline) is only partially enforced.

  * Locale/env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, plus `SAFE_MODE` and `ALLOW_NETWORK` posture) are enforced for some determinism and evidence pipelines, but are not yet repo‑wide for all byte‑sensitive jobs.

* **Config bundles and registry loader:**

  * Registry loader and configuration bundles exist for catalogs such as Magic‑10, band edges, and topology; these produce governed artifacts already indexed and mirrored under PF12’s Evidence Catalog.

* **QA and acceptance scaffolding:**  
* PF09 Calcination tasks and previous epics have established:  
  * A QA\_ROOT convention (`audit/qa/<epic>/...`) for Live QA and local QA harness runs.  
  * A basic sanity pipeline that can be invoked to validate a small set of canonical flows.  
  * Early acceptance maps/manifests for prior epics. EPIC021 is scoped to implement the QA tooling bootstrap and acceptance-map viability behavior and to bind that behavior to canonical QA tokens (token names are recorded in §2.6.5; semantics remain single-homed in Governance and the Glow QA Guide).

##### Existing tokens validated (names‑only, reused)

EPIC021 will **reuse, not re‑prove** the following acceptance tokens already green from earlier Calcination work (PF20 \+ PF09):

* `TWO_RUN_IDENTITY_OK`

* `COMPOSITE_ABBA_IDENTITY_OK`

* `CLI_READER_EMITTER_PARITY_OK` (for the existing surfaces covered in HDE‑EPIC017/018)

* `JSON_CANONICAL_CHECK_OK` (existing canonical JSON checks)

* `CLI_SERIALIZER_GUARD_OK` (existing serializer guard coverage)

* `EVIDENCE_INDEX_UPDATED_OK` (baseline index updates wired into CI)

* `EVIDENCE_INDEX_MIRROR_OK` (existing Mirror regeneration)

* `EVIDENCE_INDEX_HASH_OK` (hash proofs already present where PF09/PF12 require them)

* `EVIDENCE_PATHS_VALIDATED_OK` (existing evidence path validation jobs)

* `CI_CHECK_MIRROR_SCHEMA_OK` (Mirror schema check already wired in some pipelines)

* `SANITY_PIPELINE_LOGGED_OK` (sanity pipeline producing logs under QA\_ROOT for at least one prior epic)

These tokens stay in scope as **reused foundations**; EPIC021 may extend their coverage to new surfaces, but does not re‑litigate the already‑proved behavior.

##### Existing evidence located (titles‑only pointers)

EPIC021 assumes the following evidence families already exist and remain canonical:

* **Canonical serializer harness artifacts**

  * “Canonical serializer AB/BA harness artifacts” — AB/BA JSON pairs and their associated proof logs, plus Reader/CLI parity outputs under `artifacts/cli/...`.

  * “Serializer guard evidence set” — guard logs and failure classification outputs.

* **Evidence Index / Machine Mirror / orientation demo**

  * “Evidence Index (Calcination base)” — existing `INDEX` artifact(s) and their Machine Mirror counterparts under the PF12 evidence catalog.

  * “Machine Mirror (Calcination base)” — machine mirror artifact(s) that already mirror the base index and orientation demo.

  * “Orientation demo and sanity logs (Calcination base)” — baseline sanity/pipeline logs under QA\_ROOT for prior epics.

* **Registry and config artifacts**

  * “Registry loader outputs (Calcination base)” — registry artifacts and index entries for Magic‑10, band edges, and topology.

##### Gap statement (what remains unproven / drifted)

EPIC021 explicitly aims to address these gaps, aligned with the three workstreams:

* **Canonical serializer consolidation gaps:**

  * Canonical serializer rules and arrays‑as‑sets semantics are not yet consolidated across all governed JSON surfaces; some flows still use legacy emitters or tolerate alt‑JSON.

  * Reader/CLI parity is not yet enforced in a single canonical harness for all Calcination‑owned surfaces.

* **Evidence skeleton and env pins deepening gaps:**

  * `registry_report` is not yet a governed artifact with a clear schema and Evidence Index/Mirror discipline.

  * Env pins (`DETERMINISM_ENV_PINS_OK`) are not yet enforced across all relevant determinism and evidence pipelines.

  * Local sanity entrypoints and Index/Mirror touch discipline are only partially enforced in CI.

* **QA bootstrap / harness discipline / viability gaps:**

  * QA tooling bootstrap (ensuring pytest and QA harnesses are runnable and classified correctly) is only partially implemented and not explicitly tokenized.

  * QA harness discipline around QA\_ROOT, log aggregation, and step logging is incomplete.

  * Acceptance map / QA plan viability checks exist as PF09 requirements but not yet as implemented, evidenced, and tokenized behavior in PF04/PF19.

No new work under EPIC021 is scoped until this Existing Work Check is treated as reviewed and accepted per PF20 §2.1.2.

---

#### 2.6.3 Deliverables (Jobs To Be Done)

##### D1 — Canonical serializer consolidation (HDE‑CALC002.\*)

* **Job to be done:**  
   Consolidate and finalize canonical serializer/emitter semantics across all Calcination‑owned JSON surfaces, including canonical JSON encoding, arrays‑as‑sets behavior, and Reader/CLI parity, under pinned deterministic envs.

* **Evidence required (titles‑only):**

  * “EPIC021 canonical serializer harness report” — updated harness outputs showing AB↔BA and two‑run identity across all Calcination surfaces.

  * “EPIC021 Reader/CLI parity report” — parity evidence for Reader vs CLI across the expanded surface set.

  * “Serializer guard regression suite report” — guard tests proving no regressions in error envelope or canonicalization behavior for governed JSON.

  * “EPIC021 canonical JSON/arrays‑as‑sets acceptance map entries” — acceptance map entries (under the EPIC021 acceptance map) tying D1 tokens to harness tests and artifacts.

* **PF references:**

  * PF01 — Canon‑HDE‑Math‑Spec (canonical JSON, arrays‑as‑sets, determinism primitives).

  * PF02 — Canon‑HDE Architecture (serializer/presenter component responsibilities).

  * PF05 — Canon‑HDE‑CLI‑API‑Vendor‑Ref (CLI/Reader JSON contracts).

  * PF09 — Canon‑HDE‑Build Checklist (HDE‑CALC002.\* tasks).

  * PF14 — Canon‑HDE‑Mechanics Guide (serializer and presenter mechanics; determinism harnesses).

  * PF19 — Canon‑Glow QA Guide (component QA playbooks for serializer/CLI).

* **Indicative CLI usage (non‑exhaustive, existing patterns):**

  * `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC hdctl showcompat --mode=canonical --output artifacts/cli/epic021_showcompat.json`

  * `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/cli/test_serializer_*.py`

##### D2 — Evidence skeleton and env pins deepening (HDE‑CALC003.6, .7, .9, .11)

* **Job to be done:**  
   Turn the Evidence skeleton (Evidence Index, Machine Mirror, sanity/orientation pipeline) and env pins into hardened, CI‑enforced behavior with a governed `registry_report`, repo‑wide determinism env pins, and explicit Index/Mirror touch discipline.

* **Evidence required (titles‑only):**

  * “EPIC021 registry\_report artifact” — governed `registry_report` artifact and schema, with path proofs and Evidence Index/Mirror entries.

  * “EPIC021 env pins report” — log and index entries proving determinism env pins (`DETERMINISM_ENV_PINS_OK`) for all relevant jobs.

  * “EPIC021 Index/Mirror discipline report” — CI reports showing same‑PR regeneration of Evidence Index and Machine Mirror for evidence‑touching changes.

  * “EPIC021 sanity pipeline acceptance snapshot” — snapshot of sanity pipeline behavior under pinned envs, including any newly governed local entrypoint.

* **PF references:**

  * PF07 — Canon‑Glow‑Infrastructure (CI environments, rails posture).

  * PF09 — Canon‑HDE‑Build Checklist (HDE‑CALC003.6–.7, .9, .11).

  * PF12 — Canon‑HDE‑Schemas and Artifacts (Evidence Index, Machine Mirror, registry artifacts, QA artifacts).

  * PF14 — Canon‑HDE‑Mechanics Guide (evidence tools, sanity pipeline, Mirror discipline).

  * PF19 — Canon‑Glow QA Guide (evidence/QA artifacts and QA\_ROOT patterns).

* **Indicative commands (non-exhaustive, existing patterns):**  
* SAFE\_MODE=1 ALLOW\_NETWORK=0 LC\_ALL=C LANG=C TZ=UTC python tools/generate\_registry\_report.py

  * Expected output (governed, canonical): artifacts/registry/registry\_report.json

* CI job equivalents (per PF09) to refresh Evidence Index/Mirror and sanity evidence under pinned envs:

  * SAFE\_MODE=1 ALLOW\_NETWORK=0 LC\_ALL=C LANG=C TZ=UTC python tools/evidence/update\_evidence\_index.py

  * SAFE\_MODE=1 ALLOW\_NETWORK=0 LC\_ALL=C LANG=C TZ=UTC python tools/evidence/run\_sanity\_pipeline.py


  ##### **D3 — QA bootstrap, harness discipline, viability (HDE-CALC003.12–.15)**

**Job to be done:**  
 Implement a standard QA tooling bootstrap, enforce QA\_ROOT discipline and step logging for QA harnesses, and implement the acceptance-map viability checks required by PF09, wired into CI and Live QA under governed rails.

**Implementation notes (EPIC021 QA harness):**

* EPIC021’s operator entrypoint is `tools/qa/epic021_qa.py`. It MUST execute the harness when run as a script (not be a no-op), and MUST return a non-zero exit code on failure.

* The entrypoint MUST validate closed-rails determinism env pins using the canonical helper `engine.runtime.determinism_env.ensure_determinism_env` (validate-only; do not mutate env pins).

* EPIC021’s harness orchestration uses the generic harness module `tools/qa/qa_harness.py` (via a HarnessConfig), while preserving EPIC021’s externally observable behavior (run-id semantics, QA\_ROOT layout, log formats, manifest structure, and viability log format).

**Entrypoint behavior requirement (closed rails):**  
 Under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), running `python tools/qa/epic021_qa.py` MUST:

1. Validate determinism env pins up front.

   * If pins are wrong or missing, exit non-zero and MUST NOT create `audit/qa/hde-epic021/<run-id>/` or write a manifest entry for that run.

2. Determine a `run_id` (default or from `EPIC021_QA_RUN_ID`).

3. Create `audit/qa/hde-epic021/<run-id>/`.

4. Emit `D0_bootstrap.log` and the canonical sequence of `step_*.log` files for the EPIC021 D3 QA steps.

5. Append/update `audit/qa/hde-epic021/qa_step_logs_manifest.json` with exactly one manifest entry per `run_id` (dedupe by run\_id).

6. Append/update `audit/qa/hde-epic021/acceptance_map_viability.log` with a summary line aligned to the EPIC021 acceptance map and token→evidence matrix.

7. Return exit code 0 only if the latest manifest entry for this `run_id` shows all steps `status == "PASS"`; otherwise return non-zero.

**Evidence required (titles-only):**

* “EPIC021 canonical bootstrap log (`audit/qa/hde-epic021/test_tooling_bootstrap.log`)" — epic-level register proving tooling bootstrap behavior and tooling-vs-behavior classification.

* “EPIC021 per-run bootstrap and step logs” — run-scoped logs under `audit/qa/hde-epic021/<run-id>/`, including `D0_bootstrap.log` and `step_*.log`, each with pinned env metadata and per-step outcomes.

* “EPIC021 QA step logs manifest (`audit/qa/hde-epic021/qa_step_logs_manifest.json`)" — per-epic manifest enumerating runs and step log paths; deduped by run\_id.

* “EPIC021 acceptance-map viability log (`audit/qa/hde-epic021/acceptance_map_viability.log`)" — viability report showing token coverage classification for the EPIC021 acceptance map (COVERED / PLANNED / MISSING summary line).

* “EPIC021 acceptance map (`docs/acceptance_map_epic021.json`) and acceptance-artifacts alignment guard” — acceptance map entries for EPIC021 showing token→test→artifact wiring, plus an alignment test (for example `tests/qa/test_epic021_acceptance_alignment.py`) that prevents matrix↔map drift.

* “EPIC021 harness entrypoint selftest (CI)” — subprocess-based tests (for example `tests/qa/test_epic021_harness_entrypoint.py`) that:

  * prove the happy-path artifacts and exit code under closed rails, and

  * prove env-pin failure behavior (non-zero exit, no QA\_ROOT run directory or manifest entry for the failing run id).

* “Generic QA harness unit tests (CI)” — unit tests covering generic harness behavior (for example `tests/qa/test_generic_qa_harness.py`) and demonstrating that EPIC021’s refactor preserves externally observable behavior.

* “Closed-rails CI gating for EPIC021 entrypoint” — `.github/workflows/ci.yml` runs the EPIC021 entrypoint selftest under closed rails so regressions fail CI.

* “EPIC021 QA\_ROOT operator guide” — `audit/qa/hde-epic021/README.md` describing the operator command and the exact QA\_ROOT artifacts a successful run must produce.

* “EPIC021 Live QA readout directory” — `audit/qa/hde-epic021/live-qa/` containing step evidence artifacts for Steps 1–7 (for example `STEP1_*` through `STEP6_qa_root_summary.json`) plus an auto-generated `audit/qa/hde-epic021/live-qa/README.md` that lists commands, evidence files, PF references (titles-only), and verdict.

* “EPIC021 Live QA harness run (live-qa-1)” — `audit/qa/hde-epic021/live-qa-1/` containing `D0_bootstrap.log` and the D3 `step_*.log` sequence, with a manifest entry showing PASS statuses and a viability log update for the same run id.

* “QA harness pattern note (non-canonical)” — `docs/qa_harness_pattern.md` (titles-only pointer; operator guidance, not PF canon).

**PF references:**

* PF09 — Canon-HDE-Build Checklist (HDE-CALC003.12–.15 bootstrap and viability tasks).

* PF14 — Canon-HDE-Mechanics Guide (§QA tooling bootstrap, orientation/sanity pipeline, QA\_ROOT conventions).

* PF19 — Canon-Glow QA Guide (QA playbooks, QA\_ROOT, QA tooling roles, QA tokens).

* PF04 — Canon-HDE-Governance (governance tokens, rails policy, QA decision rules).

---

#### **2.6.4 PF Reference Map**

EPIC021 leans on the following PF documents and sections (titles/sections only):

* **Core:**

  * PF21 — 7 Phases of Alchemical Engineering (Calcination phase semantics).

  * PF06 — Canon-Epic-Process-Guide (epic lifecycle, CodEx-assisted PRs, Live QA epics).

  * PF09 — Canon-HDE-Build Checklist (Phase I Calcination tasks HDE-CALC002.\* and HDE-CALC003.6–.7, .9, .11–.18).

  * PF19 — Canon-Glow QA Guide (QA rails, QA\_ROOT patterns, QA tokens library, env pins, QA checklists).

  * PF20 — Canon-HDE-Phased Epics (§2.1 Epic Record Template (Normative)).

* **Additional:**

  * PF01 — Canon-HDE-Math-Spec (canonical JSON, arrays-as-sets, determinism).

  * PF02 — Canon-HDE Architecture (component responsibilities for serializer/presenter, CLI, Reader, evidence tools).

  * PF04 — Canon-HDE-Governance (governance tokens, env rails policy, error envelope governance, QA decision rules).

  * PF05 — Canon-HDE-CLI-API-Vendor-Ref (CLI/Reader JSON contracts and canonical JSON rules).

  * PF07 — Canon-Glow-Infrastructure (environments, CI, and execution contexts).

  * PF12 — Canon-HDE-Schemas & Artifacts (evidence schemas, Evidence Index/Mirror discipline, manifest and artifact keys).

  * PF14 — Canon-HDE-Mechanics Guide (evidence tools, QA bootstrap mechanics, determinism helpers, QA\_ROOT conventions).

---

#### **2.6.5 Tokens and Evidence (Acceptance)**

##### **Baseline / epic-level tokens (required for close)**

Per PF20 §2.1.5 and PF20 §2.4.5, EPIC021 must satisfy the extended baseline token set that applies to all later HDE epics:

**Required baseline tokens (always for epic close):**

* `TESTS_PASS_OK`

* `DOC_DELTA_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK` (if applicable per PF09/PF12)

**Baseline QA rail tokens:**

* `QA_PRECOMMIT_CHECKLIST_OK` (PF19)

* `QA_POSTCOMMIT_CHECKLIST_OK` (PF19)

* `ENV_RAILS_POLICY_OK` (PF04; closed refusal / open conformance)

**Baseline determinism/evidence tokens (extended baseline for later epics):**

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `DETERMINISM_ENV_PINS_OK`

* `SANITY_PIPELINE_OK`

These 12 tokens form the baseline acceptance roster for EPIC021; all D1–D3 work is in addition to, but not instead of, these.

* “EPIC021 final PR CI summary” — final HDE-EPIC021 PR(s) with green CI and doc deltas (baseline `TESTS_PASS_OK`, `DOC_DELTA_PRESENT_OK`).

* “EPIC021 Evidence Index / Machine Mirror update manifest” — entries showing new or updated artifacts and their hash proofs (`EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`).

* “EPIC021 evidence path validation report” — CI job and report demonstrating `EVIDENCE_PATHS_VALIDATED_OK`.

* “EPIC021 env pins compliance report” — consolidated report showing `DETERMINISM_ENV_PINS_OK` across relevant suites.

* “EPIC021 sanity pipeline summary” — report/log showing `SANITY_PIPELINE_OK` (pipeline executed clean on targeted surfaces).

* “EPIC021 QA checklists and rails log” — QA checklists and env rails policy evidence for final PR (`QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK`, `ENV_RAILS_POLICY_OK`).

##### **D1 tokens — canonical serializer consolidation**

Scope: determinism and serializer behavior across Calcination-governed JSON surfaces.

**Tokens (names-only):**

* `CLI_READER_EMITTER_PARITY_OK` (extended for EPIC021 surface set)

* `CLI_NO_ALT_JSON_OK`

* `JSON_CANONICAL_CHECK_OK`

* `ERROR_JSON_CANON_OK`

* `CLI_SERIALIZER_GUARD_OK`

* `DETERMINISM_ENV_PINS_OK` (baseline token; D1 is responsible for satisfying it for serializer/CLI suites)

**Evidence pointers (titles-only):**

* “EPIC021 canonical serializer harness regression report” — harness runs showing no alt-JSON, canonical JSON, AB/BA and two-run identity across all governed surfaces.

* “EPIC021 serializer guard coverage report” — guard test coverage over governed JSON surfaces with logs under `artifacts/cli/guards/`.

* “EPIC021 Reader/CLI parity parity\_delta report” — parity checking report across the extended surface set.

* “EPIC021 env pins suite report (serializer/CLI)” — explicit env pin logs for serializer/CLI determinism tests.

##### **D2 tokens — evidence skeleton and env pins deepening**

Scope: Evidence Index, Machine Mirror, registry\_report, env pins, and sanity pipeline at the repository skeleton level.

**Tokens (names-only):**

* `EVIDENCE_INDEX_UPDATED_OK` (baseline; extended to EPIC021 artifacts)

* `EVIDENCE_INDEX_MIRROR_OK` (baseline extension for EPIC021 artifacts)

* `EVIDENCE_INDEX_HASH_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `DETERMINISM_ENV_PINS_OK` (baseline; applied to evidence/registry jobs)

* `SANITY_PIPELINE_OK` (baseline; pipeline runs clean under pinned envs for EPIC021 scope)

EPIC021 does not introduce new semantics for these tokens; it extends their coverage and ensures CI/QA wiring is complete for the evidence skeleton and registry/env-pins surfaces.

**Evidence pointers (titles-only):**

* “EPIC021 registry\_report artifact & schema” — governed registry\_report plus schema description and path proofs, with Evidence Index/Mirror entries.

* “EPIC021 Index/Mirror CI discipline report” — CI logs and acceptance entries showing same-PR regeneration for EPIC021 evidence changes.

* “EPIC021 Mirror schema \+ hash report” — job outputs demonstrating `CI_CHECK_MIRROR_SCHEMA_OK` and `EVIDENCE_INDEX_HASH_OK` for EPIC021’s additions.

* “EPIC021 env pins coverage matrix (evidence/registry jobs)” — mapping of jobs to env pins, demonstrating `DETERMINISM_ENV_PINS_OK`.

* “EPIC021 sanity pipeline summary (Calcination skeleton)” — pipeline outputs proving `SANITY_PIPELINE_OK` on the updated skeleton.

##### **D3 tokens — QA bootstrap, harness discipline, viability**

Scope: QA tooling bootstrap, QA\_ROOT discipline, step logging, and viability checks for the EPIC021 acceptance map.

**Tokens (names-only):**

* `SANITY_PIPELINE_LOGGED_OK` (QA) — sanity pipeline emits canonical logs under QA\_ROOT for EPIC021.

* `QA_STEP_LOGS_CONSOLIDATED_OK` (QA) — QA harness logs are consolidated and discoverable for EPIC021 tests.

* `QA_BOOTSTRAP_OK` (QA) — closed-rails QA tooling bootstrap completes successfully and establishes that QA tooling is ready before deeper QA or Live QA steps proceed.

* `QA_BOOTSTRAP_TOOLING_FAIL` (QA) — bootstrap and log format support distinct tooling-failure vs behavior-failure classification (FAIL\_TOOLING vs FAIL\_BEHAVIOR) and evidence of that classification exists.

* `QA_HARNESS_DISCIPLINE_OK` (QA) — QA\_ROOT discipline is enforced (expected per-run logs, manifest behavior, stable headers, and evidence mapping).

* `QA_ACCEPTANCE_MAP_VIABILITY_OK` (QA) — acceptance-map viability check exists and is runnable; viability outputs are produced and wired into the acceptance map and token/evidence matrix.

**Notes on SANITY tokens:**

* `SANITY_PIPELINE_OK` (baseline) proves the pipeline ran successfully on the targeted suite under pinned envs.

* `SANITY_PIPELINE_LOGGED_OK` proves that pipeline runs produced canonical, QA\_ROOT-anchored logs and are wired into acceptance maps and QA manifests.

**Evidence pointers (titles-only):**

* “EPIC021 QA tooling bootstrap log (`audit/qa/hde-epic021/test_tooling_bootstrap.log`)" — QA\_ROOT log proving bootstrap behavior and classification.

* “EPIC021 per-run bootstrap and step logs” — run-scoped logs under `audit/qa/hde-epic021/<run-id>/`, including `D0_bootstrap.log` and `step_*.log`, each with pinned env metadata and per-step outcomes.

* “EPIC021 QA step logs manifest (`audit/qa/hde-epic021/qa_step_logs_manifest.json`)" — per-epic manifest enumerating runs and step log paths; deduped by run\_id.

* “EPIC021 acceptance-map viability log (`audit/qa/hde-epic021/acceptance_map_viability.log`)" — viability report showing token coverage classification for the EPIC021 acceptance map (COVERED / PLANNED / MISSING summary line).

* “EPIC021 acceptance map (`docs/acceptance_map_epic021.json`) and acceptance-artifacts alignment guard” — acceptance map entries for EPIC021 showing token to test to artifact wiring, plus an alignment test that prevents matrix to map drift.

* “EPIC021 harness entrypoint selftest (CI)” — subprocess-based tests that prove happy-path artifacts and exit code under closed rails, and prove env-pin failure behavior (non-zero exit, no QA\_ROOT run directory or manifest entry for the failing run id).

* “Generic QA harness unit tests (CI)” — unit tests covering generic harness behavior and demonstrating that EPIC021’s refactor preserves externally observable behavior.

##### **Token/Evidence Matrix (PF04/PF19 compliance)**

* `audit/qa/hde-epic021/token_evidence_matrix.md` — the single normative place for the EPIC021 token → evidence ledger.

  * One row per acceptance token (baseline \+ D1/D2/D3 \+ governance-owned QA tokens).

  * Matrix rows must reference governed evidence artifacts and match the Evidence Index and Machine Mirror (paths, hashes, proof anchors).

* PF20’s EPIC021 record references this matrix but does not duplicate it. Alignment is enforced by EPIC021 acceptance alignment tests (for example `tests/qa/test_epic021_acceptance_alignment.py`).

---

#### 2.6.6 QA Rails — Open/Close (Final PR)

Rails posture follows PF07, PF19, and PF04.

##### Pre‑commit / CI rails

* **Default rails for determinism/evidence/QA suites:**

  * `SAFE_MODE=1`

  * `ALLOW_NETWORK=0`

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* **Rule:**

  * All determinism, serializer, registry, evidence, sanity pipeline, and QA harness tests for EPIC021 must run under these pins unless PF04 explicitly allows a controlled relaxation scoped to a specific job.

  * Deviation from these env pins during these suites is treated as a **tooling failure**, not a test flake or behavior failure.

* **Tokens tied to pre‑commit/CI rails:**

  * `DETERMINISM_ENV_PINS_OK` (baseline) — aggregated proof that the key suites ran under the pinned envs.

  * `QA_PRECOMMIT_CHECKLIST_OK` — QA confirms rails posture and pre‑commit checks for the final PR.

##### Post‑commit / Live‑QA rails

* Live QA runs (EPIC021 Live QA guide) must:

  * Use the same env pins as CI for determinism‑sensitive flows.

  * Log all QA steps under `audit/qa/hde-epic021/...` (QA\_ROOT).

  * Treat any rails opening (e.g. network access) as explicitly sanctioned and logged per PF04 and PF19.

* **Tokens tied to post‑commit rails and QA:**

  * `SANITY_PIPELINE_OK` — sanity pipeline completes successfully under pinned envs.

  * `SANITY_PIPELINE_LOGGED_OK` — pipeline logs are captured and wired under QA\_ROOT.

  * `QA_STEP_LOGS_CONSOLIDATED_OK` — QA harness logs consolidated and discoverable.

  * `QA_POSTCOMMIT_CHECKLIST_OK` — QA confirms post‑commit QA posture and evidence coverage.

  * `ENV_RAILS_POLICY_OK` — proves rails policy compliance/refusal for any requested rails opening.

##### SANITY\_PIPELINE\_OK vs SANITY\_PIPELINE\_LOGGED\_OK semantics

* `SANITY_PIPELINE_OK` (baseline token):

  * Proof that a defined sanity/health pipeline has run to completion and all governed checks passed under deterministic env pins.

  * Primarily owned by D2 (evidence skeleton) and validated in CI.

* `SANITY_PIPELINE_LOGGED_OK` (QA token):

  * Proof that these pipeline runs are **logged**, structured, and stored under QA\_ROOT, with references in the acceptance map and token/evidence matrix.

  * Primarily owned by D3 (QA bootstrap/viability) and validated in Live QA / QA harness runs.

This split matches PF19’s separation between **behavioral health checks** and **QA observability/logging guarantees**.

---

#### **2.6.7 Tracked Issues**

1. **QA-TOKENS-BOOTSTRAP-NAMING**

   **Status:** Completed under HDE-EPIC021 (canon reconciliation in PF20)

   **Description:** Earlier drafts of the EPIC021 epic record carried placeholder token IDs for QA bootstrap and acceptance-map viability. Canonical QA token names for these behaviors now exist in Governance and are referenced by the QA Guide.

   **Disposition for EPIC021:**

* EPIC021 evidence remains the same (bootstrap logs, per-run step logs, manifest, viability log, acceptance map, token/evidence matrix).

* PF20 now records the canonical token names in §2.6.5 and does not use placeholder `PF04-DD-*` or `PF19-DD-*` token IDs for EPIC021 acceptance.  
2. **SANITY-PIPELINE-INDEX-REFRESH-USES-CURRENT-RUN**

   * **Status:** Completed under HDE-EPIC021

   * **Description:** The sanity pipeline post-run Evidence Index refresh originally used the previous run’s `sanity.log`, leaving index/mirror/path proof stale until a subsequent run.

   * **Disposition for EPIC021:** Fixed so the sanity log for the current run is written before refresh, and the refreshed state is reflected in the log and Evidence Catalog wiring.

3. **QA-STEP-LOGS-MANIFEST-DEDUPES-RUN-ID**

   * **Status:** Completed under HDE-EPIC021

   * **Description:** Repeated QA runs with the same run\_id appended duplicate entries to `qa_step_logs_manifest.json`, producing ambiguous/stale manifest rows for a single run\_id.

   * **Disposition for EPIC021:** Fixed to dedupe by run\_id before appending, so the manifest contains at most one entry per run\_id and reflects the latest state of run-scoped QA\_ROOT logs.

4. **SANITY-PIPELINE-LATENCY**

   * **Status:** Monitored (open)

   * **Description:** Maintain acceptable runtime for the sanity pipeline as EPIC021 extends its surface, so that it remains viable as a pre-commit/CI health check and not just a nightly job.

   * **Handling in EPIC021:**

     * Track runtime changes as acceptance-map metadata.

     * If the pipeline becomes too heavy for pre-commit, adjust its gating semantics per PF09 (for example move to scheduled job) but maintain deterministic env pins and logging requirements.

5\. **QA-HARNESS-ENTRYPOINT-EXECUTES-UNDER-CLOSED-RAILS**

* **Status:** Completed under HDE-EPIC021

* **Description:** The EPIC021 harness script existed, but operator invocation as a script did not reliably execute the harness under closed rails. The entrypoint must validate determinism env pins, run the harness, and either produce the required QA\_ROOT artifacts or fail cleanly with a non-zero exit and no artifacts for the failing run id.

* **Disposition for EPIC021:** Completed via Remedial PR1: entrypoint wiring \+ determinism env validation \+ subprocess-based entrypoint tests.

6. **CI-GATING-EPIC021-HARNESS-ENTRYPOINT**

   * **Status:** Completed under HDE-EPIC021

   * **Description:** CI lacked a closed-rails gating step that would fail if the EPIC021 harness entrypoint stopped producing the expected QA\_ROOT artifacts (run directory, logs, manifest, and viability log), allowing regressions to slip.

   * **Disposition for EPIC021:** Completed via Remedial PR3: CI runs the entrypoint selftest under closed rails, and the EPIC021 QA\_ROOT operator README was updated to reflect the expected artifacts.

Tracked issues are part of the epic’s governance story. Before EPIC021 can be marked Done, every tracked issue must be Completed under this epic, carried forward to a concrete epic ID, promoted to a cross-epic ISSUE-XXX, or explicitly dropped with rationale.

---

### **2.7 HDE-EPIC022 Epic Plan**

#### **2.7.1 Meta**

**Epic ID:** HDE-EPIC022  
**Epic title:** HDE Separation Pass 2

**Status:** Done

**Date started:** 2025-12-14

**Date completed:** 2026-01-03

**Alchemical phase:** Phase III — Separation (close remaining Separation-phase governance \+ evidence obligations for error parity, presenter stream discipline, and /internal/version identity/indexing)

**Primary intent (CRD statement):**  
Complete the Separation “seams” where public bytes, errors, identity, and evidence discipline can drift:  
Reader↔CLI error envelope parity \+ idempotence for required scenarios,  
Presenter-driven flow stream discipline (stdout-only success / stderr-only failure),  
/internal/version identity coupling \+ two-run identity \+ evidence indexing parity (human index ↔ machine mirror, same-PR rule).

**PF09 scope items owned by this epic:**  
Task HDE-SEPA002 (Partial) and Subtask HDE-SEPA002.5 (Partial)  
Task HDE-SEPA003 (Partial) and Subtask HDE-SEPA003.3 (Not done)  
Task HDE-SEPA004 (Partial) and Subtasks HDE-SEPA004.4 (Not done), HDE-SEPA004.5 (Not done)

**Out of scope (explicit):**  
No changes to HDE math mechanics, schemas, or gate/channel catalog content unless required to satisfy the PF09 items above.  
No new public commands or endpoint surfaces beyond what is required to close the listed PF09 items.

---

#### **2.7.2 Existing Work Check (MUST)**

##### **Existing features review (summary)**

Error envelope \+ token map is already governed and present (Separation task HDE-SEPA002 is “Partial” primarily because follow-up parity/idempotence remains under HDE-SEPA002.5).  
Governed error parity harness and stored parity artifacts already exist for a scenario set (HDE-SEPA002.5 is “Partial”; parity for broader scenarios is explicitly called out as remaining work).

CLI stream discipline for stderr/stdout \+ usage exit 64 is already enforced for the EPIC020 CLI slice (HDE-SEPA002.6 is “Done” and includes a concrete CLI test suite).  
Presenter / showcompat parity \+ identity harnesses exist, but HDE-SEPA003.3 remains “Not done” due to incomplete/uncoupled evidence ownership (explicitly described as covered piecemeal and not formally closed).  
/internal/version endpoint behavior and baseline artifact bundle exist for GET/HEAD parity, conditional ignoring, and no-ETag/no-Last-Modified behavior (HDE-SEPA004.1–004.3 are “Done”).

Remaining internal-version work is specifically identity coupling \+ two-run identity proof \+ evidence indexing parity (HDE-SEPA004.4 and HDE-SEPA004.5 are “Not done”).

##### **Existing tokens validated (names only; no restatement)**

Error \+ parity: ERROR\_JSON\_CANON\_OK, ERROR\_TOKEN\_MAP\_OK, CLI\_READER\_PARITY\_OK, TWO\_RUN\_IDENTITY\_OK  
Stream discipline: CLI\_STDOUT\_LF\_OK  
Stream discipline (non-token requirement; enforced by tests/evidence): success → stderr empty; errors → stdout empty; no mixed streams

Internal version (PF04-registered canonical names only):  
INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK, INTERNAL\_VERSION\_HEAD\_PARITY\_OK, INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK, INTERNAL\_VERSION\_NO\_ETAG\_OK, INTERNAL\_VERSION\_NO\_STORE\_OK

Pack/identity coupling dependencies (must remain valid where referenced):  
RELEASE\_ID\_RECOMPUTE\_OK, RELEASE\_ID\_FROM\_MANIFEST\_OK

Evidence/index/rails baseline (epic-close): see §2.1.5.A

##### **Existing evidence located (titles-only pointers)**

**Error parity artifacts \+ tests:**  
parity/errors\_reader\_cli.{scenario}.http.json  
parity/errors\_reader\_cli.{scenario}.cli.txt  
tests/cli/test\_errors\_parity.py::test\_http\_and\_cli\_parity (and associated parity/token-map tests referenced in PF09)

**CLI stream/usage discipline tests already present:**  
tests/cli/test\_cli\_usage\_and\_errors.py  
tests/cli/test\_cli\_canonical\_bytes.py

**Presenter/showcompat evidence families already defined:**  
artifacts/cli/showcompat/stdout.json

artifacts/cli/showcompat/stdout.sha256

artifacts/cli/showcompat/args.json 

**Clarification (showcompat stdout vs Reader v1 bytes):** `hdctl showcompat` stdout is the compat payload and may include numeric scores/weights. Numeric-free posture applies to typed error envelopes and the Reader v1 public success envelope. When CLI parity requires Reader v1 bytes, they are captured via `--dump-reader` sidecar output, not from showcompat stdout.

Note: These showcompat capture artifacts are deterministic fixtures for CLI stream/bytes discipline. They are not release identity proofs; release identity and coupling proofs live under the /internal/version deliverable and its governed evidence bundle.

**Internal version evidence bundle already defined:**

artifacts/ops/internal\_version/body\_get.json (+ .sha256)

artifacts/ops/internal\_version/headers\_get.txt

artifacts/ops/internal\_version/headers\_head.txt

artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt (canonical; legacy alias: cond\_if\_none\_match\_headers.txt)

artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt (canonical; legacy alias: cond\_if\_modified\_since\_headers.txt)

artifacts/ops/internal\_version/request\_chain\_manifest.json (+ .path\_proof.txt)

**Evidence index \+ machine mirror:**  
docs/evidence/INDEX.json, docs/evidence/INDEX.sha256  
artifacts/evidence\_index.jsonl

**EPIC022 close-pack and acceptance scaffold (PR1 / D0 scaffolding):**

audit/qa/hde-epic022/token\_evidence\_matrix.md  
docs/acceptance\_map\_epic022.json  
audit/EPIC-022\_close\_report.md  
audit/EPIC-022\_MANIFEST.json  
tests/qa/test\_epic022\_acceptance\_scaffold.py

##### **Gap statement (what this epic must close)**

HDE-SEPA002.5: Extend/complete Reader↔CLI parity \+ idempotence proofs for the required additional error scenarios (explicitly called out as missing coverage), and ensure acceptance bindings are current for this epic’s close pack.  
HDE-SEPA003.3: Close the “streams discipline for presenter flows” subtask by binding concrete evidence (tests \+ artifacts) to the required tokens, eliminating ownership ambiguity.  
HDE-SEPA004.4: Produce two-run identity proof(s) and identity coupling proof(s) for /internal/version (body fields must match pack/identity sources).  
HDE-SEPA004.5: Ensure Evidence Index (human) and machine mirror are updated with 1:1 parity for the internal-version and related identity artifacts, with path-proof validation.

---

#### **2.7.3 Deliverables (Jobs To Be Done)**

##### **D0 — Epic close-pack readiness and evidence discipline (supporting deliverable)**

**Job to be done:** Ensure this epic can be approved and closed without “evidence thrash” by producing the required acceptance bindings, close-pack artifacts, Live QA close-stage artifacts (D0 discovery artifact \+ QA RCA/doc-delta summary; titles-only here), and index/mirror updates in the same PR(s) that introduce/modify evidence.

**Scope:** Epic-level acceptance/evidence artifacts (no new product surface implied), including the Live QA close artifacts required for epic close under PF06/PF19 (planning/runbook content remains out of scope).

**Acceptance outcome:** A reviewer can trace every required token in §2.1.5 to concrete evidence artifacts and verify index/mirror parity without inference.

**Acceptance guardrails (anti-thrash; EPIC022-specific):**

* Remediation-only run-bundle content under `audit/qa/hde-epic022/remediation/**` (including any `remediation_only/` snapshot directories) MUST NOT be indexed into `docs/evidence/INDEX.json` or `artifacts/evidence_index.jsonl`. Only governed artifact surfaces (for example `artifacts/ops/internal_version/**`) and canonical close-pack artifacts may be indexed/mirrored.  
* The “internal\_version” focused test runs MUST be repeatable under the epic’s closed-rails posture. If optional schema-validation dependencies are absent (for example `jsonschema`), tests MUST skip with an explicit install hint rather than failing at import-time during collection.  
* Evidence validation MUST explicitly cover Machine Mirror **self-record** proof semantics (to avoid PROOF\_SHA mismatch loops). Keep a dedicated regression test and the mirror schema/proof validator in the close-pack verification set. The mirror schema check entrypoint is a Python script; invoking it via bash is invalid.  
* Evidence validation MUST explicitly cover path-proof freshness for the Human Evidence Index and its hash sentinel: `docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt` must match the current bytes of `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`. Any stale proof transcript is a hard failure.  
* Evidence validation MUST explicitly cover the Machine Mirror sibling path-proof: `artifacts/evidence_index.jsonl.path_proof.txt` MUST match the current bytes of `artifacts/evidence_index.jsonl` (path, `sha256`, `size_bytes`, and time fields). Any stale mirror proof transcript is a hard failure.  
* Any mismatch between a governed artifact’s on-disk bytes and its sibling `*.path_proof.txt` and Machine Mirror record (example class: ordering artifacts such as `artifacts/engine/order/abba_identity.bytes`) is a hard failure. Remediation is to regenerate via the canonical evidence tooling (for example `tools/evidence/update_evidence_index.py`), not to hand-edit proofs or mirror rows.  
* Acceptance bindings MUST be structurally validated: no duplicate tokens, no placeholder bindings for claimed-satisfied tokens, and acceptance map ↔ token/evidence matrix roster alignment.

##### **D1 — Error Envelope Parity Pass 2 (close HDE-SEPA002 \+ HDE-SEPA002.5)**

**Job to be done:** Ensure the same underlying error conditions produce byte-identical, numeric-free, canonical error envelopes across Reader HTTP and CLI, with idempotence proof(s), for the required scenario set (including the explicitly-called-out missing scenarios).

**PF09 mapping (must close):**  
Task: HDE-SEPA002  
Subtask: HDE-SEPA002.5

**Acceptance outcome:** The parity harness \+ stored artifacts \+ tests prove parity and two-run identity for the required scenarios under closed rails, and the acceptance bindings for this epic record those proofs.

##### **D2 — Presenter Flow Stream Discipline Closeout (close HDE-SEPA003 \+ HDE-SEPA003.3)**

**Job to be done:** Ensure presenter-driven CLI flows obey the strict stream contract: stdout-only success (one LF), stderr-only failure (typed numeric-free envelope), and close the PF09 bookkeeping gap so this requirement is no longer “piecemeal.”

**PF09 mapping (must close):**  
Task: HDE-SEPA003  
Subtask: HDE-SEPA003.3

**Acceptance outcome:** Concrete test coverage and artifacts are bound to the required token(s) and stream-discipline requirements; the epic close pack demonstrates compliance without relying on “implied by other rows.”

##### **D3 — /internal/version Identity Coupling \+ Indexing Closeout (close HDE-SEPA004 \+ HDE-SEPA004.4 \+ HDE-SEPA004.5)**

**Job to be done:** Make /internal/version a hardened, deterministic identity surface:  
body schema is frozen (six fields, frozen order, canonical JSON, LF-terminated),  
two-run identity is proven and recorded,  
body values are coupled to pack/identity sources (release\_id, build\_commit, invocation/emitter hashes), and  
the evidence is correctly indexed in both human and machine systems (same-PR rule).

**PF09 mapping (must close):**  
Task: HDE-SEPA004  
Subtask: HDE-SEPA004.4  
Subtask: HDE-SEPA004.5

**Acceptance outcome:** /internal/version is deterministic, coupled, and fully represented in Evidence Index \+ machine mirror, with path-proof validation.

**/internal/version proof surface invariants (minimum checklist; must be explicit):**

Any remediation guide, QA step, or probe tool that produces governed `/internal/version` evidence MUST explicitly enumerate and verify the following canon-critical invariants (do not imply these checks by referencing PF sections only):

A. Transport

* GET MUST return 200

* HEAD MUST return 200 and satisfy parity expectations

* Conditional requests (`If-None-Match`, `If-Modified-Since`) MUST NOT yield 304; they MUST return 200

B. Headers

* `Cache-Control: no-store` MUST be present

* `Content-Type: application/json; charset=utf-8` MUST be present

* `ETag` MUST be absent

* `Last-Modified` MUST be absent

C. Body (identity payload)

* Body MUST be fixed-schema JSON with exactly these keys (no extras):  
   `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`

* Body bytes MUST satisfy the canon “identity bytes” posture (canonical bytes, including LF termination) where applicable to the proof surface.

**Token emission gating (no “false OK”):**

* A tool MUST NOT emit any `*_OK` token unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run.

* If a run status is `FAIL_TOOLING` (or equivalent), the tool MUST NOT emit `*_OK` tokens for invariants that did not pass. It MUST NOT emit integrity-success tokens unless those checks demonstrably passed on the produced artifacts.

**Coupling requirement (anti-mixed-target / anti-redirect drift):**

For each probe run, the evidence must be coupled such that emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit `*_OK` tokens.

**Release identity and Freeze-Pack semantics (no dual semantics; hard constraint for D3):**

* The Freeze-Pack Manifest Single Source of Truth is `catalog/manifest.json`. No other file is permitted to act as the SoT for Freeze-Pack membership or release identity.

* `catalog/manifest.json` schema posture is closed for identity: it MUST contain exactly `root`, `version`, `built_at_utc`, `files` (and no other top-level keys), and the manifest MUST NOT list itself in `files`.

* Canonical bytes rule: identity and verification operate on canonical JSON bytes (UTF-8, no BOM, ASCII-sorted keys recursively, compact separators, exactly one trailing LF).

* `release_id` definition is fixed for D3 coupling: `release_id = sha256(canonical_bytes(catalog/manifest.json))` (lowercase 64-hex).

* `artifacts/math/freeze_pack_manifest.json` is an evidence copy of the Freeze-Pack Manifest and MUST be byte-identical (canonical bytes) to the on-disk `catalog/manifest.json`. “Equal” means byte-equal canonical bytes, not “JSON-equivalent.”

* No branching semantics are permitted. Any manifest-like summaries (for example `manifest_snapshot.json`) are evidence only and MUST NOT be substituted for the Freeze-Pack Manifest SoT or its evidence-copy path.

---

#### **2.7.4 PF Reference Map**

PF10 — HDE-Build Notes (superseding staging layer; captured deltas drain into the owning PF docs) (includes Addendum 1: Live QA planning is not part of Epic Plan content)

PF09 — HDE-Build Checklist:  
 Phase III — Separation  
 HDE-SEPA002, HDE-SEPA002.5  
 HDE-SEPA003, HDE-SEPA003.3  
 HDE-SEPA004, HDE-SEPA004.4, HDE-SEPA004.5

PF20 — HDE-Phased Epics:  
 §2.1 Epic Record Template (Normative)  
 §2.4.5 Baseline token set for epic closure  
 QA rails conventions (not a Live QA runbook; Live QA planning placement is governed by PF10 Addendum 1\)

PF04 — HDE-Governance:  
 /internal/version token registry (canonical INTERNAL\_VERSION\_\* names; INTVER\_\* aliases deprecated)  
 Registry enforcement (unregistered tokens are invalid for acceptance artifacts)  
 Rails posture: closed refusal / open conformance policy  
 Pack identity \+ release\_id recompute tokens  
 Sanity pipeline entrypoint requirement  
 CLI parity token naming cleanup (CLI\_READER\_PARITY\_OK is canonical; CLI\_READER\_EMITTER\_PARITY\_OK is deprecated)

PF05 — HDE-CLI-API-Vendor-Ref:  
 hdctl showcompat contract and evidence surfaces  
 CLI stdout/stderr and canonical JSON requirements

PF12 — HDE-Schemas and Artifacts:  
 Evidence Index \+ machine mirror contract (docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, path proofs)  
 Evidence family paths for: showcompat, error parity artifacts, internal version artifacts  
 Determinism env pins governed log surface (audit/gates/determinism/env\_pins.log \+ .path\_proof.txt)

PF14 — HDE-Mechanics Guide:  
 /internal/version six-field schema \+ frozen key order requirement (behavior-level requirements; token names sourced from PF04)  
 Identity artifacts and coupling touchpoints (service identity snapshot, emitter hash, release\_id artifacts)  
 CLI stream-discipline enforcement expectations

PF19 — Glow QA Guide:  
 Required additional error scenarios to cover (DB-unavailable; closed-rails vendor attempt)  
 Token/Evidence Matrix requirements \+ location conventions  
 Determinism pins and acceptance discipline (titles-only, with governed artifacts via PF12)  
 Token naming note: For AB/BA identity, the canonical PF04 token name is COMPOSITE\_ABBA\_IDENTITY\_OK; treat any PF19 legacy naming as legacy until drained/updated.

---

#### **2.7.5 Tokens and Evidence (Acceptance)**

##### **A. Baseline (required for epic close)**

**A1. Baseline tokens (PF06 close gate; required)**

TESTS\_PASS\_OK  
DOC\_DELTA\_PRESENT\_OK  
EVIDENCE\_INDEX\_UPDATED\_OK  
EVIDENCE\_INDEX\_HASH\_OK  
EVIDENCE\_INDEX\_MIRROR\_OK  
EVIDENCE\_PATHS\_VALIDATED\_OK  
MACHINE\_MIRROR\_UPDATED\_OK  
QA\_PRECOMMIT\_CHECKLIST\_OK  
QA\_POSTCOMMIT\_CHECKLIST\_OK  
ENV\_RAILS\_POLICY\_OK  
DETERMINISM\_ENV\_PINS\_OK  
SANITY\_PIPELINE\_OK  
CLOSE\_PACK\_FILES\_PRESENT\_OK

**A2. Baseline acceptance artifacts (paths must exist for epic close)**

Token/Evidence Matrix (required; may be skeletal at plan approval, must be complete for epic close; not embedded here):  
audit/qa/hde-epic022/token\_evidence\_matrix.md

Acceptance map (epic):  
docs/acceptance\_map\_epic022.json

Epic close-pack files (required):  
audit/EPIC-022\_close\_report.md  
audit/EPIC-022\_MANIFEST.json (ID formatting decision tracked in §2.1.7 / ADRs below)

Evidence Index (human):  
docs/evidence/INDEX.json and docs/evidence/INDEX.sha256

docs/evidence/INDEX.json.path\_proof.txt

docs/evidence/INDEX.sha256.path\_proof.txt

Machine mirror:

artifacts/evidence\_index.jsonl

artifacts/evidence\_index.jsonl.path\_proof.txt

Determinism env pins log (canonical governed surface for DETERMINISM\_ENV\_PINS\_OK):  
audit/gates/determinism/env\_pins.log  
audit/gates/determinism/env\_pins.log.path\_proof.txt  
(Indexes must reflect artifact\_key "audit.determinism.env\_pins" → audit/gates/determinism/env\_pins.log, with mirror proof\_anchor pointing to audit/gates/determinism/env\_pins.log.path\_proof.txt.)

##### **B. Deliverable acceptance mapping**

###### *D1 — HDE-SEPA002 (Task) \+ HDE-SEPA002.5 (Subtask)*

**B1. Required tokens**  
For Task HDE-SEPA002 (task-level completion condition for this epic):  
ERROR\_JSON\_CANON\_OK (must remain valid)  
ERROR\_TOKEN\_MAP\_OK (must remain valid)

For Subtask HDE-SEPA002.5 (closure gates):  
CLI\_READER\_PARITY\_OK  
TWO\_RUN\_IDENTITY\_OK

Also required (baseline, but exercised here):  
ENV\_RAILS\_POLICY\_OK (closed-rails refusal behavior must be evidenced as part of the required scenario set)

**B2. Required evidence (concrete artifacts / tests / index parity)**

Stored parity artifacts (must include the required scenarios; file set enumerated in the token/evidence matrix):  
parity/errors\_reader\_cli.{scenario}.http.json  
parity/errors\_reader\_cli.{scenario}.cli.txt

Scenario semantics that MUST be represented among {scenario}:  
forced DB-unavailable scenario  
closed-rails vendor attempt (e.g., explicit \--source=vendor while rails are closed)

Canonical scenario IDs (current parity roster ordering):

invalid\_json  
 invalid\_viewer\_prefs  
 db\_unavailable  
 vendor\_attempt\_closed\_rails

Parity test proof (must be bound in acceptance map \+ matrix):  
tests/cli/test\_errors\_parity.py::test\_http\_and\_cli\_parity

Evidence index \+ mirror updates in the same PR as any parity artifact change:  
docs/evidence/INDEX.json entry(ies) for updated/new parity artifacts  
artifacts/evidence\_index.jsonl mirror records (1:1 parity with human index)  
Path-proof validation for each newly added/changed parity artifact (referenced by mirror records)

###### *D2 — HDE-SEPA003 (Task) \+ HDE-SEPA003.3 (Subtask)*

**B3. Required tokens**  
For Subtask HDE-SEPA003.3 (closure gates):  
CLI\_STDOUT\_LF\_OK

Non-token requirement: Enforce PF05 stream discipline: success → stderr empty; errors → stdout empty; no mixed streams.

Acceptance artifacts for this epic (Acceptance Map \+ Token/Evidence Matrix) must not claim or reference CLI\_STDERR\_ONLY\_ON\_ERROR\_OK; stream discipline is asserted via the B4 evidence.

Task HDE-SEPA003 completion for this epic:  
Task is considered closed when HDE-SEPA003.3 is closed and its tokens are bound to concrete evidence in this epic’s acceptance artifacts.

**B4. Required evidence (concrete artifacts / tests / index parity)**

CLI stream-discipline tests (must be bound in acceptance map \+ matrix):  
tests/cli/test\_cli\_canonical\_bytes.py (canonical bytes \+ LF discipline for public JSON)  
tests/cli/test\_cli\_usage\_and\_errors.py (stdout empty on failure; stderr empty on success; exit posture)

 Presenter/showcompat concrete public-byte artifacts (evidence surface, filenames only):

* `artifacts/cli/showcompat/stdout.json`  
* `artifacts/cli/showcompat/stdout.json.sha256` *(canonical checksum sidecar)*  
* `artifacts/cli/showcompat/stdout.sha256` *(legacy alias; emitted for compatibility during transition)*

* `artifacts/cli/showcompat/args.json`

* Coupling verification MUST be recorded as the canonical `internal_version` evidence bundle under `artifacts/ops/internal_version/` for the existing `/internal/version` and `identity/two-run` token set:

  * `artifacts/ops/internal_version/headers_get.txt`  
  * `artifacts/ops/internal_version/headers_head.txt`  
  * `artifacts/ops/internal_version/body_get.json`  
  * `artifacts/ops/internal_version/body_get.sha256`  
  * `artifacts/ops/internal_version/two_run_identity.log`  
  * Conditional header snapshot artifacts (filenames per the canonical PF12 internal\_version evidence keys)

* Filename policy: the canonical filenames above (and any explicitly permitted legacy aliases) are the only allowed variants for EPIC022. Do not introduce ad-hoc filename variants; do not bind acceptance to legacy aliases.

Evidence index \+ mirror updates in the same PR as any showcompat evidence change:  
docs/evidence/INDEX.json entries for the showcompat artifacts above  
artifacts/evidence\_index.jsonl mirror records (1:1 parity)  
Path-proof validation for each showcompat artifact referenced

###### *D3 — HDE-SEPA004 (Task) \+ HDE-SEPA004.4 (Subtask) \+ HDE-SEPA004.5 (Subtask)*

**B5. Required tokens**

Internal version behavior (PF04-registered tokens only):  
INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK  
INTERNAL\_VERSION\_HEAD\_PARITY\_OK  
INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK  
INTERNAL\_VERSION\_NO\_ETAG\_OK  
INTERNAL\_VERSION\_NO\_STORE\_OK

Identity/idempotence requirements:  
TWO\_RUN\_IDENTITY\_OK (two consecutive GETs produce byte-identical bodies; proof recorded)

Coupling dependencies that must remain valid where referenced by /internal/version:  
RELEASE\_ID\_RECOMPUTE\_OK  
RELEASE\_ID\_FROM\_MANIFEST\_OK

**Freeze-Pack coupling semantics (clarification; no dual semantics):**

For EPIC022, these coupling dependencies are anchored to a single Freeze-Pack contract:

* `RELEASE_ID_FROM_MANIFEST_OK` and `RELEASE_ID_RECOMPUTE_OK` are evaluated against **canonical bytes** of `catalog/manifest.json` (Freeze-Pack SoT), with `release_id = sha256(canonical_bytes(catalog/manifest.json))`.

* `artifacts/math/freeze_pack_manifest.json` is an evidence copy and MUST be byte-identical to `catalog/manifest.json` on canonical bytes. Do not treat “JSON-equivalent” as equal.

* No alternate manifest semantics are permitted for these tokens; manifest-like summaries (for example `manifest_snapshot.json`) are evidence only and MUST NOT be used as identity inputs.

Evidence indexing requirements (explicitly closed by HDE-SEPA004.5 but also baseline):  
EVIDENCE\_INDEX\_UPDATED\_OK  
EVIDENCE\_INDEX\_HASH\_OK  
EVIDENCE\_INDEX\_MIRROR\_OK  
EVIDENCE\_PATHS\_VALIDATED\_OK  
MACHINE\_MIRROR\_UPDATED\_OK

Clarifying note (to prevent guessing): PF04/PF14 requirements like “Last-Modified absent” and “six keys in frozen order with no extra top-level keys” remain mandatory behavior checks, but are evidenced via the B6 artifacts \+ verifier/provenance outputs rather than being represented as separate acceptance tokens under the PF04 /internal/version registry (see ADR list).

**B6. Required evidence for HDE-SEPA004.4 (identity coupling \+ two-run identity)**

/internal/version artifact bundle (must exist and be indexed):

artifacts/ops/internal\_version/body\_get.json

artifacts/ops/internal\_version/body\_get.sha256

artifacts/ops/internal\_version/headers\_get.txt

artifacts/ops/internal\_version/headers\_head.txt

artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt (canonical; legacy alias: cond\_if\_none\_match\_headers.txt)

artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt (canonical; legacy alias: cond\_if\_modified\_since\_headers.txt)

artifacts/ops/internal\_version/request\_chain\_manifest.json

artifacts/ops/internal\_version/request\_chain\_manifest.json.path\_proof.txt (proof anchor; MUST NOT be bound as primary token evidence)

artifacts/ops/internal\_version/two\_run\_identity.log (required output of this epic if missing; this is the governed proof artifact for two-run identity \+ coupling verification)

Coupling verification MUST be recorded inside `artifacts/ops/internal_version/two_run_identity.log` (pass/fail checks that the six fields match their governing identity sources, plus an explicit two-run identity result). No new acceptance tokens are introduced for “coupling proof”; the proof is bound under the existing /internal/version and identity/two-run token set.

Determinism pins evidence surface for the capture/proof runs (canonical governed log; satisfies DETERMINISM\_ENV\_PINS\_OK):  
audit/gates/determinism/env\_pins.log (binds DETERMINISM\_ENV\_PINS\_OK; referenced in token/evidence matrix \+ acceptance map)  
audit/gates/determinism/env\_pins.log.path\_proof.txt (mirror proof\_anchor for artifact\_key "audit.determinism.env\_pins")

Note: audit/gates/determinism/env\_pins.log satisfies baseline determinism pins (DETERMINISM\_ENV\_PINS\_OK), while artifacts/proofs/env\_pins.txt (if present) is a separate environment-pins snapshot used for other proof/provenance contexts and must not be treated as the determinism pins log surface.

Identity coupling sources (must exist and be referenced in the coupling proof log and/or epic acceptance artifacts):  
artifacts/identity/service\_identity.json  
artifacts/identity/emitter\_sha256.txt  
artifacts/math/release\_id.txt  
artifacts/math/release\_id\_recompute.log  
artifacts/math/freeze\_pack\_manifest.json

Schema-level coupling acceptance (must be satisfied and reflected in the proof artifacts):  
/internal/version body contains exactly six fields in frozen order:  
engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id  
Values match the corresponding pack/identity artifacts (as applicable) under the determinism pins required for proof runs.

**B7. Required evidence for HDE-SEPA004.5 (index/mirror parity \+ path proofs)**

Human Evidence Index updated to include (at minimum) all artifacts listed in B6.  
Machine mirror (artifacts/evidence\_index.jsonl) updated with 1:1 parity records for those artifacts, including proof anchors.  
Path-proof validation outputs exist for each referenced artifact path and are traceable from the mirror record.

Determinism pins indexing parity must be correct (mechanical requirement, not optional):  
docs/evidence/INDEX.json contains artifact\_key: "audit.determinism.env\_pins" with discovered\_physical\_path: "audit/gates/determinism/env\_pins.log" and artifacts/evidence\_index.jsonl contains the matching record whose proof\_anchor is exactly audit/gates/determinism/env\_pins.log.path\_proof.txt; the token/evidence matrix row for DETERMINISM\_ENV\_PINS\_OK must reference audit/gates/determinism/env\_pins.log (not artifacts/proofs/env\_pins.txt).

---

#### **2.7.6 QA Rails — Open/Close (Final PR)**

This section defines QA rails expectations for the final PR that closes HDE-EPIC022. It is planning/tracking only.

**Closure posture (EPIC022):** EPIC022 is closed **Done** with any remaining QA tasks explicitly **DEFERRED** to future epics. Deferred items MUST NOT be claimed as satisfied; they must be recorded as deferred in the acceptance artifacts and close-pack narrative.

---

##### **A. Final PR QA sequence**

**A1. Pre-commit / CI (rails posture)**  
Default posture for CI and local QA is **closed rails**: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

If any job opens rails, it MUST be:

* explicitly declared (what opened, why, and what evidence it produced),  
* safe (no secrets/PII; keys-only logs),  
* recorded as evidence (mechanically generated),  
* and indexed/mirrored in the same change-set as the evidence change.

**A2. Post-commit (final proof run)**  
Final proof runs MUST record:

* determinism env pins posture (for `DETERMINISM_ENV_PINS_OK`, via the canonical determinism pins evidence surface),  
* rails posture (closed vs open),  
* and the acceptance-evidence cut being verified (acceptance map \+ token/evidence matrix \+ close-pack outputs),

without embedding a detailed runbook into the Epic Plan.

---

##### **B. Live QA requirement (closeout requirement; EPIC022 deferral-aware)**

Live QA is a Close Gate requirement in general (owned by the Epic Process Guide and the Glow QA Guide). This Epic Plan intentionally does not include Live QA planning/runbook content (commands, step sequence, operator walkthroughs, or directory-design rules).

**Normal Live QA close artifacts (titles-only; required when not deferred):**

* a D0 Discovery artifact, and  
* a QA outcome summary \+ doc-delta note (brief; evidence-linked),

expected under `audit/qa/hde-epic022/` and/or included/referenced by `audit/EPIC-022_close_report.md`.

These Live QA close artifacts are treated as QA evidence and MUST be mechanically produced from command outputs. Manual fill placeholders (for example “(fill PASS/FAIL)”) and manual editor updates are non-conforming for any file used as QA evidence.

**EPIC022 deferral rule (this epic):**  
Any missing Live QA artifacts for EPIC022 are **deferred**. They MUST be recorded as deferred (not implied as completed), and no acceptance tokens may be claimed on the basis of missing/unfinished Live QA steps.

**/internal/version auth posture (planning posture; avoid false blockers):**  
`/internal/version` is treated as **operator-network-only** under the interim posture. Plans and runbooks MUST NOT require an Authorization header as a prerequisite for evidence capture. If an environment uses an auth header in practice, it is execution convenience only and must not be treated as canon-required.

---

##### **C. Close conditions (Final PR is eligible for merge/close only if)**

The close PR is eligible only if:

1. **All non-deferred acceptance claims are satisfied and bound to evidence.**  
   All required (non-deferred) tokens in `#### **2.7.5 Tokens and Evidence (Acceptance)**` are satisfied and bound to concrete evidence in the epic close-pack and acceptance artifacts (titles/paths as listed there), including at minimum:  
* `audit/qa/hde-epic022/token_evidence_matrix.md`  
* `docs/acceptance_map_epic022.json`  
* `audit/EPIC-022_close_report.md`  
* `audit/EPIC-022_MANIFEST.json`  
* `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl` (and required sibling proof anchors)  
2. **Deferred items are explicit and unclaimed.**  
   Any deferred QA work MUST be explicitly recorded as deferred in the acceptance artifacts and close report, and MUST NOT be claimed as satisfied (no `_OK` claims for deferred work).  
3. **Evidence Index \+ machine mirror parity is maintained.**  
   Evidence Index \+ machine mirror MUST be updated in the same change-set as evidence changes and must pass validators (EVIDENCE\_\* tokens).  
4. **Sequencing rule (prevent stale close-packs).**  
   If any remediation or reconciliation changes a step status from `FAIL_*` to `PASS` (or changes any acceptance-binding artifact), close-pack generation MUST be rerun against the updated acceptance state before the epic is treated as close-ready.

---

##### **D. Close-pack generation and verification (Z0 / Z1 semantics)**

PF20 does not define the Z-step runbook. It defines what these steps mean if they appear in EPIC022 execution artifacts.

**Z0 — close\_pack\_generate (required meaning for close):**

* Z0 is the close-pack generator meaning for EPIC022.  
* Z0 produces the canonical close-pack outputs for this epic:  
  `audit/EPIC-022_close_report.md` and `audit/EPIC-022_MANIFEST.json`  
  from the current acceptance state (acceptance map \+ token/evidence matrix \+ governed evidence index/mirror).  
* Z0 MUST be treated as stale if executed before later remediation that changes step status or acceptance bindings; rerun Z0 after the final remediation cut (see §2.7.6.C).

**Z1 — close\_pack\_verify (optional/N.A. until defined):**

* Z1 is optional and MUST NOT be treated as a gating requirement unless it is explicitly defined as an executable step with evidenced outputs.  
* If a matrix or manifest references Z1 but no executable Z1 step exists (or no Z1 evidence exists), Z1 MUST be treated as N/A for close gating and tracked under ISSUE-CLOSEPACK-Z1-SEMANTICS (§1).  
* If Z1 is adopted in future work, its purpose is verification: it must verify internal consistency between (a) close-pack outputs, (b) acceptance artifacts, and (c) indexed evidence surfaces, and it must be captured and indexed like other governed QA artifacts.

**Token claim semantics in step logs and close-pack artifacts (claims, not rosters):**  
Tokens listed in step logs and close-pack artifacts are claims, not rosters:

* On PASS: allowed to claim `*_OK` tokens.  
* On FAIL / FAIL\_TOOLING / TOOLING\_BLOCKED / FAIL\_BEHAVIOR: must not claim any `*_OK` tokens.  
* If a step needs to record “intended tokens,” they must be recorded under a distinct field name (for example `intended_tokens`) to avoid governance confusion.

---

#### **2.7.7 Tracked Issues (if applicable; EPIC022 posture)**

**Tracking posture (EPIC022):** Any remaining QA issues below are **DEFERRED** to future epics and are not EPIC022 close blockers. They MUST be recorded as deferred in acceptance artifacts and must not be claimed as satisfied.

**Epic ID / filename normalization**  
Issue: File/path naming must be correct to avoid evidence/index drift and close-pack rejection.  
Why it matters: Close-pack artifacts and QA roots must not spawn parallel spellings.  
Posture: Deferred.

**DB-unavailable scenario determinism for parity harness**  
Issue: The parity harness must cover a forced DB-unavailable scenario deterministically (no flaky environment dependencies).  
Why it matters: Required for deterministic reproduction when claimed; weak determinism undermines evidence stability.  
Posture: Deferred.

**HDE-SEPA003.3 evidence ownership closure**  
Issue: Evidence ownership is described as “captured elsewhere,” creating perpetual scope ambiguity.  
Why it matters: Weakens enforcement of stream discipline for presenter flows.  
Posture: Deferred.

**Ordering evidence drift: abba\_identity.bytes proof/mirror mismatch**  
Issue: A governed ordering artifact may have mismatched metadata between bytes, sibling path-proof, and/or mirror record.  
Why it matters: Breaks path-proof validation and can cause validators to fail or certify incorrect evidence.  
Posture: Deferred.

**/internal/version coupling proof format**  
Issue: A stable, reviewable proof for identity coupling is required beyond “the endpoint returns fields.”  
Why it matters: Coupling and two-run identity proof must be deterministic and indexable when claimed.  
Posture: Deferred.

**Token registry drift (PF04) vs EPIC022 acceptance roster**  
Issue: Acceptance rosters and artifacts must not claim tokens that are not registered in the canonical token registry.  
Why it matters: Token registry mismatch must block claiming acceptance for those tokens (but must not block evidence capture).  
Posture: Deferred; do not maintain “known unregistered tokens” lists in this epic record—treat registry validation output as the authoritative evidence.

### **2.8 HDE-EPIC023 Epic Plan**

#### **2.8.1 Meta**

**Epic ID:** HDE-EPIC023  
 **Epic title:** HDE Calcination Pass 5  
 **Status:** Done (closure approved via override)  
 **Date started:** 2026-01-04  
 **Date completed:** 2026-01-11  
 **Alchemical phase:** Calcination (phase numbering Unknown (not present in inputs))  
 **Primary location(s):** `audit/qa/hde-epic023/`; `audit/gates/`; `audit/EPIC-023_close_report.md`; `audit/EPIC-023_MANIFEST.json`; `docs/acceptance_map_epic023.json`  
 **Branch:** Unknown (not present in inputs)  
 **Primary intent (CRD statement):** Close out Calcination Pass 5 by establishing governed acceptance/evidence scaffolding, resolving evidence-index snapshot discipline \+ schema hygiene, ensuring canonical JSON gate artifacts exist at canonical loci, capturing PF23 consult evidence, pinning acceptance-alignment validator rails, and producing a governed close-pack \+ docs surfaces (planned: r2 Implementation Plan; actual: PF10 execution \+ closure override).

**Outcome posture (PF10):** “Outcome label: Closure approved (override)” with accepted gaps \+ drain targets recorded in PF10 — HDE Build Notes, §2.55.

**PF09 scope pointers (as provided in r2 Implementation Plan; ownership Unknown (not present in inputs)):**

* **HDE-CALC003.1**

* **HDE-CALC003.2**

* **HDE-CALC003.9**

* **HDE-CALC003.10**

* **HDE-CALC003.11**

* **HDE-CALC003.13**

* **HDE-CALC003.15**

* **HDE-SEPA004.4**

* **HDE-SEPA004.5**

**Out of scope (explicit):** Unknown (not present in inputs)

Plan revision note (mismatch): PF10 references “r4 Epic Plan HDE-EPIC023” (PF10 — HDE Build Notes, §2.2), but the provided Implementation Guide input is “r2 Implementation Plan HDE-EPIC023.md”; r4 content is Unknown (not present in inputs).

#### **2.8.2 Existing Work Check**

**Planned (r2 Implementation Plan — Brief recap of scope):**

* Epic framed as a closure \+ evidence-discipline pass: tighten governed evidence surfaces, avoid fabricated paths, and make acceptance artifacts canonical and checkable (r2 Implementation Plan HDE-EPIC023 — “Brief recap of scope (EPIC023)”).

* Canonical directory policy for canonical JSON gate artifacts: `audit/gates/canonical_json/` (decision reinforced in PF10 — HDE Build Notes, §2.2).

* Evidence registry / index surfaces are assumed to exist and must be validated without introducing ad-hoc lockfiles (r2 plan PR-05 intent; details in PR-05 section).

**Actual baseline condition observed during execution (PF10 anchors):**

* Canonical JSON gate directory policy explicitly set: “canonical directory for JSON canonicalization is `audit/gates/canonical_json/`” (PF10 — HDE Build Notes, §2.2).

* Revalidation sweep expanded scope to include EPIC-022 close-pack proof files due to evidence tooling encountering missing proofs (PF10 — HDE Build Notes, §2.16; proof files cited there, e.g., `audit/EPIC-022_close_report.md.path_proof.txt`, `audit/EPIC-022_MANIFEST.json.path_proof.txt`).

* Evidence-index snapshot discipline identified as tooling-blocked posture, later accepted as an override gap with a drain target (PF10 — HDE Build Notes, §2.53 and §2.55).

Existing-work uncertainty: What specifically existed in-repo before 2026-01-04 beyond the above decisions is Unknown (not present in inputs).

#### **2.8.3 Deliverables (Jobs-to-be-done) — Planned vs Actual Reconciliation**

##### **D0 — Epic close-pack readiness and evidence discipline (supporting deliverable)**

**Planned (r2 Implementation Plan — Crosswalk \+ PR-01):**

* Intent/scope: “Epic close-pack readiness and evidence discipline (supporting deliverable).”

* Planned implementation emphasis: acceptance scaffolds \+ doc-delta surfaces \+ evidence-index mirror/paths validity (PR-01).

* Planned acceptance tokens (PR-01): `DOC_DELTA_PRESENT_OK`, `QA_ACCEPTANCE_MAP_VIABILITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

* Planned evidence outputs include (PR-01 “Evidence outputs”): `audit/qa/hde-epic023/doc_deltas.md`, `audit/qa/hde-epic023/doc_delta.mirror.json`, `audit/qa/hde-epic023/evidence_index_snapshot.json`, `audit/qa/hde-epic023/token_evidence_matrix.md`, `audit/qa/hde-epic023/qa_step_logs_manifest.json`, `audit/qa/hde-epic023/qa_step_log_header.json`, and `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json` (plus conditional `artifacts/...` updates if governed bytes change).

**Actual (PF10):**

* PR01 executed as remediation-heavy review stream (PF10 — HDE Build Notes, §2.9) with evidence tooling checks referenced (names-only; detailed command lines omitted here).

* QA decision stream includes (PASS):

  * `CHECK D07_codespaces_snapshot` and `CHECK D08_qa_doc_deltas_capture` with evidence pointers `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json` and `audit/qa/hde-epic023/00_meta/doc_deltas.md` (PF10 — HDE Build Notes, §2.22).

  * `CHECK D10_doc_delta_draft` with evidence pointer `audit/docdeltas/hde-epic023_doc_deltas.md` (PF10 — HDE Build Notes, §2.32).

* Doc-delta canonical posture decision recorded separately: doc deltas live at `audit/docdeltas/*.md` and epic-scoped mirrors may exist under `audit/qa/...` (PF10 — HDE Build Notes, §2.5).

Disposition: Partially satisfied; doc-delta evidence exists and is checked, but planned vs actual paths differ across stages (`audit/qa/hde-epic023/doc_deltas.md` vs `audit/qa/hde-epic023/00_meta/doc_deltas.md` vs `audit/docdeltas/hde-epic023_doc_deltas.md`). The planned artifact `audit/qa/hde-epic023/qa_step_log_header.json` is Unknown (not present in inputs) in PF10, and must not be assumed.

##### **D1 — Determinism pins posture for governed bytes (no ad-hoc env-pins lock artifacts)**

**Planned (r2 Implementation Plan — Crosswalk \+ PR-05):**

* Intent/scope: “Determinism pins posture for governed bytes (no ad-hoc env-pins lock artifacts).”

* Planned acceptance tokens (PR-05): `QA_ACCEPTANCE_MAP_VIABILITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`, `JSON_CANONICAL_CHECK_OK`, `DOC_DELTA_PRESENT_OK`, `TWO_RUN_IDENTITY_OK`.

**Actual (PF10):**

* Determinism policy and ADR framing recorded: ADR-001 (PF10 — HDE Build Notes, §2.40, §2.41, §2.42) and explicit constraints on determinism checks and entrypoints (PF10 — HDE Build Notes, §2.44, §2.45).

* QA decision stream (PASS):

  * `CHECK D17_env_pins` with evidence pointers `audit/qa/hde-epic023/checks/D17_env_pins/primary.log` and `audit/qa/hde-epic023/checks/D17_env_pins/structured_record.json` (PF10 — HDE Build Notes, §2.47).

  * `CHECK D18_sanity_log` with evidence pointers `audit/qa/hde-epic023/checks/D18_sanity_log/primary.log` and `audit/qa/hde-epic023/checks/D18_sanity_log/structured_record.json` (PF10 — HDE Build Notes, §2.48).

* Additional determinism-related evidence surfaces referenced: `artifacts/ops/internal_version/` and `docs/ENDPOINTS_CATALOG.json` (PF10 — HDE Build Notes, §2.51). Specific header file names under `artifacts/ops/internal_version/` are prefixes only (e.g., `artifacts/ops/internal_version/headers_`); full filenames are Unknown (not present in inputs).

Disposition: Satisfied with recorded ADR posture and PASS checks; no ad-hoc env-pin lockfile artifacts are evidenced in PF10 beyond the governed check outputs cited above.

D2 — Canonical JSON artifacts exist at canonical loci \+ include path-proofs; compare is evidence under canonical token

**Planned (r2 Implementation Plan — Crosswalk \+ PR-03):**

* Intent/scope: “Canonical JSON artifacts must exist at canonical loci \+ include path-proofs; compare is evidence under the canonical token.”

* Planned acceptance tokens (PR-03): `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

* Planned evidence outputs (PR-03 “Evidence outputs”): `audit/gates/canonical_json/json_canon_compare.log`, `audit/gates/canonical_json/canonical_json_gate.json`, `audit/gates/canonical_json/canonical_json_gate.sha256` plus corresponding `.path_proof.txt` files.

**Actual (PF10):**

* Canonical directory decision reaffirmed: `audit/gates/canonical_json/` is canonical (PF10 — HDE Build Notes, §2.2).

* QA decision stream (PASS):

  * `CHECK D20_json_gate_compare_log` with evidence pointer `audit/gates/canonical_json/json_canon_compare.log` (PF10 — HDE Build Notes, §2.50).

  * `CHECK D22_canonical_json_gate_structured_record` with evidence pointer `audit/qa/hde-epic023/checks/D22_canonical_json_gate_structured_record/primary.log` (PF10 — HDE Build Notes, §2.52).

  * `CHECK D19_json_gate_check_log` with evidence pointers `audit/qa/hde-epic023/checks/D19_json_gate_check_log/primary.log` and `audit/qa/hde-epic023/checks/D19_json_gate_check_log/structured_record.json` (PF10 — HDE Build Notes, §2.49).

* **Recorded mismatch accepted at close:** Closure override notes canonical JSON gate directory drift, citing additional surfaces under `audit/gates/json_gate/canonical/` (PF10 — HDE Build Notes, §2.55).

Disposition: Satisfied with PASS checks, with an explicit accepted mismatch: dual-family reporting (`audit/gates/canonical_json/` vs `audit/gates/json_gate/canonical/`) recorded as a closure-override gap (PF10 — HDE Build Notes, §2.55).

##### **D3 — Acceptance-alignment validator rails pinned, and test exists**

**Planned (r2 Implementation Plan — Crosswalk \+ PR-04):**

* Intent/scope: “Acceptance alignment validator rails must be pinned, and test must exist.”

* Planned acceptance token (PR-04): `QA_ACCEPTANCE_MAP_VIABILITY_OK`.

* Planned evidence outputs (PR-04 “Evidence outputs”): `tests/qa/test_epic023_acceptance_alignment.py`, `audit/qa/hde-epic023/qa_step_logs_manifest.json`, `audit/qa/hde-epic023/qa_step_log_header.json`.

**Actual (PF10):**

* Test creation/rails alignment recorded: `tests/qa/test_epic023_acceptance_alignment.py` (PF10 — HDE Build Notes, §2.11 and §2.12).

* Remediation loop recorded: token evidence matrix parsing updated to align r2/r3/r4 drift, supporting the validator (PF10 — HDE Build Notes, §2.28) with transcript evidence `audit/qa/hde-epic023/remediation/s1_dev_fix_d04_parser/pytest_epic023_acceptance_alignment.txt`.

* Closed-rails rerun evidence recorded for D04 validator: `audit/qa/hde-epic023/checks/d04_acceptance_alignment_validator/primary.log` and manifest correction note (PF10 — HDE Build Notes, §2.29).

Disposition: Satisfied; planned test exists and remediation/rerun evidence is recorded. Planned `audit/qa/hde-epic023/qa_step_log_header.json` remains Unknown (not present in inputs) in PF10 and must not be assumed.

##### **D4 — PF23 consult note exists (non-token deliverable)**

**Planned (r2 Implementation Plan — Crosswalk \+ PR-02):**

* Intent/scope: “PF23 consult note must exist but is non-token.”

* Planned evidence outputs (PR-02 “Evidence outputs”): `audit/qa/hde-epic023/pf23_consult_note.md` (plus doc-delta updates if changed).

**Actual (PF10):**

* PF23 consult capture check (PASS): `CHECK D09_pf23_consult_capture` with evidence pointer `audit/qa/hde-epic023/00_meta/pf23_consult.md` (PF10 — HDE Build Notes, §2.25).

* PR02 references consult-note artifact: `audit/qa/hde-epic023/pf23_consult_note.md` (PF10 — HDE Build Notes, §2.10).

Disposition: Satisfied, with a naming/location mismatch that must be archived: planned/PR02 artifact `audit/qa/hde-epic023/pf23_consult_note.md` vs check-evidenced `audit/qa/hde-epic023/00_meta/pf23_consult.md` (PF10 — HDE Build Notes, §2.25 and §2.10).

##### **D5 — All jobs-to-be-done: close-pack \+ docs PR**

**Planned (r2 Implementation Plan — Crosswalk \+ PR-06):**

* Intent/scope: “All jobs-to-be-done; close-pack \+ docs PR.”

* Planned acceptance tokens (PR-06): `QA_ACCEPTANCE_MAP_VIABILITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`, `JSON_CANONICAL_CHECK_OK`, `DOC_DELTA_PRESENT_OK`, `TWO_RUN_IDENTITY_OK`.

* Planned evidence outputs (PR-06 “Evidence outputs” includes): `audit/EPIC-023_close_report.md`, `audit/EPIC-023_MANIFEST.json`, `docs/acceptance_map_epic023.json`, `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256` (plus `.path_proof.txt` variants).

**Actual (PF10):**

* Close pack artifacts produced and referenced: `audit/EPIC-023_close_report.md` and `audit/EPIC-023_MANIFEST.json` (PF10 — HDE Build Notes, §2.14; and closure-override references in §2.55).

* Acceptance map and docs surfaces referenced: `docs/acceptance_map_epic023.json` and `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` (PF10 — HDE Build Notes, §2.15 and §2.37).

* Evidence-index mirror/registry checks (PASS): `CHECK D13_human_index`, `CHECK D14_index_hash_sentinel`, `CHECK D15_machine_mirror` with evidence pointers `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.mirror.json` (PF10 — HDE Build Notes, §2.37).

* Evidence-index snapshot posture (PASS but tooling-blocked posture): `CHECK D23_evidence_index_snapshot_artifact` with evidence pointers `audit/qa/hde-epic023/checks/D23_evidence_index_snapshot_artifact/primary.log` and `audit/qa/hde-epic023/checks/D23_evidence_index_snapshot_artifact/structured_record.json`; closure override also cites `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` (PF10 — HDE Build Notes, §2.53 and §2.55).

* Final closure posture recorded as override with gaps and drain targets (PF10 — HDE Build Notes, §2.55).

Disposition: Satisfied for close-pack \+ docs surfaces with an explicit override posture; accepted gaps include doc updates to PF12/PF19 and canonical JSON \+ evidence-index snapshot gate-family drift (PF10 — HDE Build Notes, §2.55).

#### **2.8.4 PF Reference Map**

* PF10 — HDE Build Notes, §2.2 (canonical JSON gate directory decision)

* PF10 — HDE Build Notes, §2.5 (doc-delta canonical posture)

* PF10 — HDE Build Notes, §2.9–§2.15 (EPIC023 PR review stream \+ docs PR)

* PF10 — HDE Build Notes, §2.16 (revalidation sweep; scope expansion to EPIC-022 proof files)

* PF10 — HDE Build Notes, §2.22, §2.25, §2.26, §2.29, §2.30, §2.32, §2.34, §2.35, §2.37, §2.46–§2.53 (closure check stream decisions \+ evidence pointers)

* PF10 — HDE Build Notes, §2.40–§2.45 (ADR-001 determinism \+ entrypoint policy)

* PF10 — HDE Build Notes, §2.55 (closure override; accepted gaps \+ drain targets)

* PF27 — Canon Plan Templates, §Epic Record Template (Normative)

* r2 Implementation Plan HDE-EPIC023.md — §Brief recap of scope (EPIC023); §Crosswalk: IG items → Plan tasks; §PR-01…§PR-06

---

#### **2.8.5 Tokens and Evidence (Acceptance)**

##### **A. Baseline (required for epic close)**

**A1. Planned baseline tokens (r2 plan PR-06):**

* `QA_ACCEPTANCE_MAP_VIABILITY_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `SANITY_PIPELINE_OK`

* `DETERMINISM_ENV_PINS_OK`

* `JSON_CANONICAL_CHECK_OK`

* `DOC_DELTA_PRESENT_OK`

* `TWO_RUN_IDENTITY_OK`

**A2. Actual token coverage posture (PF10):**

* PF10 records an explicit 8-token set as “Key proof facts” and ties it to evidence pointers `audit/qa/hde-epic023/token_evidence_matrix.md` and `audit/qa/hde-epic023/acceptance_map_viability.log` (PF10 — HDE Build Notes, §2.13).

##### **B. Deliverable tokens (this epic)**

* **D0:** Planned tokens `DOC_DELTA_PRESENT_OK`, `QA_ACCEPTANCE_MAP_VIABILITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`; actual evidence includes `audit/docdeltas/hde-epic023_doc_deltas.md` (PF10 §2.32) and `audit/qa/hde-epic023/acceptance_map_viability.log` \+ `audit/qa/hde-epic023/token_evidence_matrix.md` (PF10 §2.26 / §2.13).

* **D1:** Planned determinism tokens `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`; actual checks include `audit/qa/hde-epic023/checks/D17_env_pins/...` and `audit/qa/hde-epic023/checks/D18_sanity_log/...` (PF10 §2.47 / §2.48).

* **D2:** Planned `JSON_CANONICAL_CHECK_OK`; actual gate evidence includes `audit/gates/canonical_json/json_canon_compare.log` (PF10 §2.50) and `audit/qa/hde-epic023/checks/D19_json_gate_check_log/...` (PF10 §2.49).

* **D3:** Planned validator posture supports `QA_ACCEPTANCE_MAP_VIABILITY_OK`; actual includes `tests/qa/test_epic023_acceptance_alignment.py` (PF10 §2.11 / §2.12) and `audit/qa/hde-epic023/checks/d04_acceptance_alignment_validator/primary.log` (PF10 §2.29).

* **D4:** Non-token; actual includes `audit/qa/hde-epic023/00_meta/pf23_consult.md` (PF10 §2.25) and PR02 consult-note reference `audit/qa/hde-epic023/pf23_consult_note.md` (PF10 §2.10).

* **D5:** Close pack \+ docs; actual includes `audit/EPIC-023_close_report.md`, `audit/EPIC-023_MANIFEST.json`, `docs/acceptance_map_epic023.json`, `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256` (PF10 §2.14 / §2.15 / §2.37).

##### **C. Evidence pointers (titles-only; non-exhaustive; verbatim paths only)**

* `audit/qa/hde-epic023/token_evidence_matrix.md`

* `audit/qa/hde-epic023/acceptance_map_viability.log`

* `audit/EPIC-023_close_report.md`

* `audit/EPIC-023_MANIFEST.json`

* `docs/acceptance_map_epic023.json`

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `audit/gates/canonical_json/json_canon_compare.log`

* `audit/gates/topology/orientation_demo.txt`

* `audit/qa/hde-epic023/checks/D23_evidence_index_snapshot_artifact/primary.log`

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` (cited in PF10 closure override)

---

#### **2.8.6 QA Rails — Open/Close (Final PR)**

##### **A. QA check stream executed (PF10 decision series; outcomes)**

* PASS: `CHECK D07_codespaces_snapshot` and `CHECK D08_qa_doc_deltas_capture` → `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json`, `audit/qa/hde-epic023/00_meta/doc_deltas.md` (PF10 — HDE Build Notes, §2.22).

* PASS: `CHECK D09_pf23_consult_capture` and `CHECK D01_acceptance_map` → `audit/qa/hde-epic023/00_meta/pf23_consult.md`, `docs/acceptance_map_epic023.json` (PF10 — HDE Build Notes, §2.25).

* PASS: `CHECK D02_token_evidence_matrix` and `CHECK D03_acceptance_viability` → `audit/qa/hde-epic023/token_evidence_matrix.md`, `audit/qa/hde-epic023/acceptance_map_viability.log` (PF10 — HDE Build Notes, §2.26).

* PASS: `CHECK D05_step_logs_manifest` and `CHECK D06_primary_step_logs` → `audit/qa/hde-epic023/qa_step_logs_manifest.json` and `audit/qa/hde-epic023/checks/` (PF10 — HDE Build Notes, §2.30).

* PASS: `CHECK D10_doc_delta_draft` and `CHECK D11_close_report` → `audit/docdeltas/hde-epic023_doc_deltas.md` and close-pack references (PF10 — HDE Build Notes, §2.32 and §2.34).

* PASS: `CHECK D12_close_pack_manifest` → `audit/EPIC-023_MANIFEST.json` (PF10 — HDE Build Notes, §2.35).

* PASS: `CHECK D13_human_index`, `CHECK D14_index_hash_sentinel`, `CHECK D15_machine_mirror` → `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.mirror.json` (PF10 — HDE Build Notes, §2.37).

* PASS: `CHECK D16_orientation_demo` → `audit/gates/topology/orientation_demo.txt`, `audit/qa/hde-epic023/checks/D16_orientation_demo/...` (PF10 — HDE Build Notes, §2.46).

* PASS: `CHECK D17_env_pins` → `audit/qa/hde-epic023/checks/D17_env_pins/...` (PF10 — HDE Build Notes, §2.47).

* PASS: `CHECK D18_sanity_log` → `audit/qa/hde-epic023/checks/D18_sanity_log/...` (PF10 — HDE Build Notes, §2.48).

* PASS: `CHECK D19_json_gate_check_log` and `CHECK D20_json_gate_compare_log` → `audit/qa/hde-epic023/checks/D19_json_gate_check_log/...`, `audit/gates/canonical_json/json_canon_compare.log` (PF10 — HDE Build Notes, §2.49 and §2.50).

* PASS: `CHECK D22_canonical_json_gate_structured_record` → `audit/qa/hde-epic023/checks/D22_canonical_json_gate_structured_record/primary.log` (PF10 — HDE Build Notes, §2.52).

* PASS (posture-only; tooling-blocked acceptance recorded): `CHECK D23_evidence_index_snapshot_artifact` → `audit/qa/hde-epic023/checks/D23_evidence_index_snapshot_artifact/primary.log` (PF10 — HDE Build Notes, §2.53).

##### **B. Reruns / remediations explicitly recorded**

* Closed-rails rerun recorded for acceptance-alignment validator: `audit/qa/hde-epic023/checks/d04_acceptance_alignment_validator/primary.log` and related manifest correction note (PF10 — HDE Build Notes, §2.29).

* Parsing remediation to align r2/r3/r4 token evidence matrix for validator: `audit/qa/hde-epic023/remediation/s1_dev_fix_d04_parser/pytest_epic023_acceptance_alignment.txt` (PF10 — HDE Build Notes, §2.28).

##### **C. Close posture (override) and non-blocking gaps**

* Closure override accepted gaps include:

  * Evidence-index snapshot pointer recorded at `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` while D23 remains tooling-blocked posture; drain targets recorded (PF10 — HDE Build Notes, §2.55).

  * Canonical JSON gate directory drift noted (`audit/gates/canonical_json/` vs `audit/gates/json_gate/canonical/`), to be converged later (PF10 — HDE Build Notes, §2.55).

  * PF12 and PF19 updates explicitly listed as drain targets (PF10 — HDE Build Notes, §2.55).

---

#### **2.8.7 Tracked Issues (if applicable; EPIC023 posture)**

**Tracked issues referenced in r2 plan:** `TI-023-01`, `TI-023-02`, `TI-023-03` (r2 Implementation Plan HDE-EPIC023.md — PR-06 “Tracked issues \+ disposition”).

**Actual disposition detail:** PF10 notes that the close report contains TI dispositions, but does not include the per-TI outcomes verbatim in the build notes; therefore per-TI outcomes are Unknown (not present in inputs). Evidence pointer: `audit/EPIC-023_close_report.md` (PF10 — HDE Build Notes, §2.14).

**Accepted closure gaps tracked as drain targets (PF10):**

* “PF12 updates to align canonical JSON gate artifacts and evidence-index snapshot discipline” (PF10 — HDE Build Notes, §2.55).

* “PF19 update for Live QA Plan template overlap with EPIC closure record” (PF10 — HDE Build Notes, §2.55).

* “Converge canonical JSON gate reporting under a single gate family” (PF10 — HDE Build Notes, §2.55).

---

#### **2.8.8 Plan Preflight (MUST)**

**Normative preflight items (PF27 — Canon Plan Templates, §Epic Record Template (Normative) → “Plan Preflight (MUST)”):**

* Confirm plan uses canonical naming and does not invent evidence paths.

  * Actual enforcement signal: PF10 records anti-fabrication posture (“forbid invented entrypoints and fabricated path proof usage”) (PF10 — HDE Build Notes, §2.44; also reinforced in PR03 review notes in §2.11).

* Confirm acceptance tokens are explicitly listed and evidence pointers are enumerated.

  * Planned: explicit token lists in r2 plan PR-01/PR-03/PR-05/PR-06.

  * Actual: PF10 records an 8-token set tied to `audit/qa/hde-epic023/token_evidence_matrix.md` (PF10 — HDE Build Notes, §2.13).

* Confirm closure posture expectations vs tooling constraints are surfaced before “Done.”

  * Actual: D23 posture recorded as tooling-blocked and accepted via closure override with drain targets (PF10 — HDE Build Notes, §2.53 and §2.55).

Preflight completion record: Unknown (not present in inputs) beyond the enforcement signals and closure-override documentation cited above.

### **2.9 HDE-EPIC024 Epic Plan**

#### **2.9.1 Meta**

**Epic ID:** HDE-EPIC024  
**Epic name:** HDE Pre-Conjunction Pass 1  
**Phase:** Pre-Conjunction (Calcination)  
**Status:** Done (PF10 — HDE Build Notes, §2.30 “Verdict: READY WITH CAVEATS”; PF10 — HDE Build Notes, §2.31 “Closure decision: SATISFIED (close the epic now)”)  
**Start date:** 2026-01-13  
**Date completed:** 2026-01-21  
**Owner:** PO

**Stakeholders (roles-only):** HDE Lead Dev; QA Reviewer-of-Record; Governance Reviewer-of-Record; CI/Infra owner (as needed for merge-gating scripts)  
**Scope canonical anchor:** PF09 — HDE Build Checklist, §Subtask HDE-CALC002.1 (Pre-Conjunction Pass scaffolding and gates)  
**Epic intent (one line; planned):** Produce a repo-first, deterministic “Pre-Conjunction Pass” gate family: canonical JSON, arrays-as-sets, env pins, evidence index snapshot/binding, CLI stream discipline, sampler evidence, and QA harness discipline, such that closure artifacts can be generated without ad-hoc runbooks.

Plan revision note (mismatch): PF10 execution repeatedly references `r5 Live QA Plan HDE-EPIC024.md` as the “Approved Plan” for checks (not present in inputs). Planned scope source for this archive record is `r3 Epic Plan HDE-EPIC024.md`; PF10 remains authoritative for actual results/outcomes.

#### **2.9.2 Existing Work Check**

**Planned (r3 Epic Plan HDE-EPIC024.md):**

* **In-scope checklist items (PF09 citations):**  
  * **HDE-CALC002.1** — One serializer and one emitter for all public bytes  
  * **HDE-CALC002.2** — Canonical JSON rules across all surfaces  
  * **HDE-CALC002.3** — Arrays-as-sets semantics (registry \+ topology)  
  * **HDE-CALC002.4** — Determinism environment pins (LC\_ALL, LANG, TZ)  
  * **HDE-CALC003.9** — Local run targets for sanity pipeline  
  * **HDE-CALC003.10** — Indexing & parity CI gates  
  * **HDE-CALC003.11** — Evidence index touch discipline  
  * **HDE-CALC003.13** — Canonical pytest invocation (python \-m pytest)  
  * **HDE-CALC003.14** — QA harness discipline (step logs \+ manifest) — skeleton  
  * **HDE-CALC003.19** — D23 Evidence Index snapshot artifact exists  
  * **HDE-DISS003.2** — Pool formation & eligibility filters  
  * **HDE-SEPA003.3** — Consolidate stream discipline for presenter-driven CLI flows  
* **Explicitly out-of-scope (planned):** any full pass on “Conjunction” or “Separation” scope beyond the subset above.  
* **Existing governed evidence surfaces expected before EPIC024 (carry-forward posture):**  
  * Evidence Index (human): `docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`  
  * Evidence Index (machine): `artifacts/evidence_index.jsonl` \+ `artifacts/evidence_index.jsonl.sha256`  
  * EPIC023 acceptance map: `docs/acceptance_map_epic023.json`  
  * EPIC023 close pack: `audit/EPIC-023_MANIFEST.json` \+ `audit/EPIC-023_close_report.md`  
* **Known drift/ambiguity risks (planned):**  
  * Token registry authority / aliasing: PF10 addenda “Token authority \+ acceptance artifact normalization” (plan cites PF10 §2.1; section not present in PF10 v9.4.4 inputs)  
  * Evidence path binding authority: PF10 addenda “Evidence path binding authority order” (plan cites PF10 §2.2; section not present in PF10 v9.4.4 inputs)  
  * Acceptance map path-of-record: PF10 addenda “Acceptance map path-of-record for EPIC024” (plan cites PF10 §2.3; section not present in PF10 v9.4.4 inputs)  
  * Evidence Index snapshot contract (D23) mechanical PASS/FAIL: PF10 addenda “Evidence Index snapshot (D23) mechanical PASS/FAIL contract” (plan cites PF10 §2-4; section not present in PF10 v9.4.4 inputs)

**Actual baseline condition observed (PF10):**

* EPIC024 produced a dedicated QA root: `audit/qa/hde-epic024/` with check receipts written under `audit/qa/hde-epic024/checks/` (PF10 — HDE Build Notes, §2.11–§2.29).  
* The “known drift/ambiguity risks” manifested as explicit ADR notes and remediation loops during execution (examples):  
  * Canonical gate runner \+ evidence artifacts required remediation / reruns before “PASS” receipts stabilized (PF10 — HDE Build Notes, §2.12, §2.18–§2.20).  
  * Token registry validity required remediation and an OPS rerun stream (PF10 — HDE Build Notes, §2.18–§2.21).  
  * Evidence index snapshot contract / binding validation was executed and archived via remediation rerun artifacts (PF10 — HDE Build Notes, §2.20).  
* Carry-forward surfaces were referenced as baseline (PF10 — HDE Build Notes, §2.31 cites `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`).

#### **2.9.3 Deliverables (Jobs-to-be-done) — Planned vs Actual Reconciliation**

##### **D1 — Public-bytes emitter consolidation across CLI / reader\_v1 / mirror / evidence\_index**

* **Planned:** Ensure “one serializer and one emitter for all public bytes” by consolidating emission behavior across reader\_v1 and CLI, with parity discipline and a D00 check receipt.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `artifacts/mirror/hde/all/v1/main.json`  
  * `artifacts/evidence_index.jsonl`  
  * `tools/reader_v1/emit_public_bytes.py`  
  * `tools/cli/emit_public_bytes.py`  
  * `audit/gates/canonical_json/json_canonical_check.log`  
  * `audit/gates/canonical_json/json_canonical_check.sha256`  
  * `audit/qa/hde-epic024/checks/D00_public_bytes_parity/primary.log`  
* **Actual (PF10):** Unknown (not present in inputs)  
  * PF10 does not include a `CHECK D00_public_bytes_parity` receipt or any reference to `tools/reader_v1/emit_public_bytes.py` / `tools/cli/emit_public_bytes.py`.  
* **Disposition:** Unclear

##### **D2 — Canonical JSON rules across all surfaces (gate \+ artifacts)**

* **Planned:** Canonical JSON gate is repo-present, deterministic, and emits an auditable check log for closure.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/evidence/run_canonical_json_gate.py`  
  * `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
  * `audit/gates/json_gate/canonical/json_gate_check_log.sha256`  
  * `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`  
* **Actual (PF10):** PASS — PF10 — HDE Build Notes, §2.12 (“**Decision:** PASS for CHECK D02\_canonical\_json\_gate”).  
  * Evidence pointers: `tools/evidence/run_canonical_json_gate.py`; `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`; `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`; `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`.  
  * Planned artifact `audit/gates/json_gate/canonical/json_gate_check_log.sha256`: Unknown (not present in inputs)  
* **Disposition:** Satisfied (PASS receipt recorded; one planned artifact not referenced in PF10)

##### **D3 — Arrays-as-sets semantics (determinism gate)**

* **Planned:** Arrays-as-sets determinism gate exists and produces deterministic audit logs.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/evidence/run_arrays_as_sets_gate.py`  
  * `audit/gates/determinism/arrays_as_sets.log`  
  * `audit/gates/determinism/arrays_as_sets.sha256`  
  * `audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log`  
* **Actual (PF10):** PASS — PF10 — HDE Build Notes, §2.13 (“**Decision:** PASS for CHECK D05\_arrays\_as\_sets”).  
  * Evidence pointers: `tools/evidence/run_arrays_as_sets_gate.py`; `audit/gates/determinism/arrays_as_sets.log`; `audit/gates/determinism/arrays_as_sets.sha256`; `audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log`.  
* **Disposition:** Satisfied

##### **D4 — Determinism environment pins (LC\_ALL, LANG, TZ)**

* **Planned:** Determinism environment pins are gated and recorded, specifically including LC\_ALL=C.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/evidence/run_env_pins_gate.py`  
  * `audit/gates/determinism/env_pins.log`  
  * `audit/gates/determinism/env_pins.sha256`  
  * `audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log`  
* **Actual (PF10):** PASS — PF10 — HDE Build Notes, §2.24 (“**Decision:** PASS for CHECK D01\_env\_pins\_gate”).  
  * Evidence pointers: `tools/evidence/run_env_pins_gate.py`; `audit/gates/determinism/env_pins.log`; `audit/gates/determinism/env_pins.sha256`; `audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log`.  
* **Disposition:** Satisfied

##### **D5 — Sanity pipeline (local run target and gating posture)**

* **Planned:** Provide and validate a sanity pipeline run target sufficient for “canary” posture.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`  
* **Actual (PF10):** PASS — PF10 — HDE Build Notes, §2.28 (“**Decision:** PASS for CHECK D07\_sanity\_pipeline”).  
  * Evidence pointer: `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`.  
* **Disposition:** Satisfied

##### **D6 — Evidence index / mirror parity CI gates implemented (CI gating)**

* **Planned:** Provide CI checks for evidence index and machine mirror parity, including schema checks and a declared audit trail when these surfaces change.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `docs/evidence/INDEX.json.path_proof.txt`  
  * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `ci/checks/check_evidence_index.sh`  
  * `ci/checks/check_machine_mirror_index.sh`  
  * `ci/checks/check_machine_mirror.sh`  
  * `ci/checks/check_machine_mirror_index_schema.sh`  
  * `audit/qa/hde-epic024/checks/<check_id>/primary.log`  
* **Actual (PF10):** Unknown (not present in inputs)  
  * PF10 contains limited adjacent evidence: evidence index snapshot contract checks and binding validation reruns (PF10 — HDE Build Notes, §2.14 and §2.20), and CI workflow wiring is referenced as added in a remedial PR (`.github/workflows/ci.yml`) (PF10 — HDE Build Notes, §2.19).  
  * Planned CI check scripts under `ci/checks/`: Unknown (not present in inputs)  
  * Planned path-proof artifacts for `docs/evidence/INDEX.*`: Unknown (not present in inputs)  
* **Disposition:** Unclear

##### **D7 — Evidence index touch discipline & manifest enforcement**

* **Planned:** Enforce “touch discipline” such that PRs that modify evidence index / mirror declare and regenerate the required snapshot/binding artifacts, with auditable receipts under QA root.  
* **Planned evidence required (verbatim planning notes):** “QA step logs demonstrating check-mode enforcement for evidence index touches; binding validation receipts for evidence-path mapping.”  
* **Actual (PF10):** Evidence index contract and validation artifacts exist:  
  * Evidence index snapshot receipt: PF10 — HDE Build Notes, §2.14 (“**Decision:** PASS for CHECK D09\_evidence\_index\_snapshot”) with `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256` and `audit/qa/hde-epic024/checks/D09_evidence_index_snapshot/primary.log`.  
  * Binding validation artifacts were produced during OPS rerun: `audit/qa/hde-epic024/remediation/s3_po_006_rerun/evidence_path_binding_validation.ndjson` \+ `.sha256` (PF10 — HDE Build Notes, §2.20).  
* **Disposition:** Unclear  
  * Core validations exist, but the full “touch discipline” enforcement surface is not fully enumerated in PF10.

##### **D8 — QA harness discipline (repo-first) \+ canonical pytest invocation**

* **Planned:** Establish repo-first QA harness discipline: per-check receipts (`primary.log`), a step logs manifest, and a harness selftest entrypoint; canonical pytest invocation via `python -m pytest`.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/qa_harness/selftest_ci_entrypoint.sh`  
  * `audit/qa/hde-epic024/selftest/run1/selftest_report.json`  
  * `audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log`  
  * `audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log`  
* **Actual (PF10):** PASS — harness selftest and step logs manifest both recorded PASS receipts:  
  * PF10 — HDE Build Notes, §2.16 (“**Decision:** PASS for CHECK D14\_harness\_selftest”) with `tools/qa_harness/selftest_ci_entrypoint.sh`, `audit/qa/hde-epic024/selftest/run1/selftest_report.json`, and `audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log`.  
  * PF10 — HDE Build Notes, §2.17 (“**Decision:** PASS for CHECK D19\_step\_logs\_manifest”) with `tools/qa_harness/generate_step_logs_manifest.py`, `audit/qa/hde-epic024/qa_step_logs_manifest.json`, `audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt`, and `audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log`.  
  * Canonical pytest invocation (`python -m pytest`): Unknown (not present in inputs)  
    * PF10 does not record a distinct receipt for this invocation form.  
* **Disposition:** Satisfied (core harness discipline receipts PASS; pytest-invocation evidence not explicitly recorded)

##### **D9 — Evidence Index snapshot artifact exists (D23 contract \+ binding)**

* **Planned:** Provide the D23 “Evidence Index snapshot” contract and binding validation artifacts and receipts.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.sha256`  
  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
  * `audit/gates/evidence_index_snapshot/evidence_path_binding_validation.ndjson`  
  * `audit/gates/evidence_index_snapshot/evidence_path_binding_validation.sha256`  
  * `audit/qa/hde-epic024/checks/D23_evidence_index_snapshot_contract/primary.log`  
* **Actual (PF10):** PASS (with path deviations for some planned artifacts).  
  * Snapshot artifact exists and is validated via PASS receipt for D09: PF10 — HDE Build Notes, §2.14 with `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256`, plus `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`.  
  * D23 contract rerun and binding validation outputs were archived under remediation during OPS rerun (PF10 — HDE Build Notes, §2.20): `audit/qa/hde-epic024/remediation/s3_po_006_rerun/d23_evidence_index_snapshot_contract_rerun.ndjson`, `audit/qa/hde-epic024/remediation/s3_po_006_rerun/evidence_path_binding_validation.ndjson`, `audit/qa/hde-epic024/remediation/s3_po_006_rerun/evidence_path_binding_validation.sha256`.  
  * Planned path `audit/gates/evidence_index_snapshot/evidence_path_binding_validation.*`: Unknown (not present in inputs)  
  * Planned receipt `audit/qa/hde-epic024/checks/D23_evidence_index_snapshot_contract/primary.log`: Unknown (not present in inputs)  
* **Disposition:** Satisfied (artifact family present and validated; some outputs recorded at different loci than planned)

##### **D10 — Sampler pool formation & eligibility filters (evidence family)**

* **Planned:** Provide deterministic sampler pool snapshots and related evidence surfaces.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/sampler/emit_pool_snapshot.py`  
  * `artifacts/sampler/pool_snapshots/**`  
  * `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`  
* **Actual (PF10):** PASS receipt exists for sampler evidence, but planned sampler artifacts are not referenced in PF10.  
  * PF10 — HDE Build Notes, §2.27 (“**Decision:** PASS for CHECK D04\_sampler\_evidence”) with `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`.  
  * Planned evidence `tools/sampler/emit_pool_snapshot.py` and `artifacts/sampler/pool_snapshots/**`: Unknown (not present in inputs)  
* **Disposition:** Unclear  
  * PASS receipt exists, but planned artifact family is not evidenced in PF10.

##### **D11 — Consolidate stream discipline for presenter-driven CLI flows**

* **Planned:** Consolidate and validate stream discipline for presenter-driven CLI flows, including showcompat capture artifacts and CLI guardrails.  
* **Planned evidence required (verbatim list items from r3 plan):**  
  * `tools/evidence/generate_showcompat_artifacts.py`  
  * `artifacts/cli/showcompat/hde/all/v1/main.json`  
  * `artifacts/cli/showcompat/hde/all/v1/main.json.sha256`  
  * `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log`  
  * `audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log`  
* **Actual (PF10):** PASS — showcompat artifacts and CLI guardrail both have PASS receipts.  
  * PF10 — HDE Build Notes, §2.25 (“**Decision:** PASS for CHECK D03\_showcompat\_artifacts”) with `tools/evidence/generate_showcompat_artifacts.py`, `artifacts/cli/showcompat/hde/all/v1/main.json`, `artifacts/cli/showcompat/hde/all/v1/main.json.sha256`, and `audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log`.  
  * PF10 — HDE Build Notes, §2.26 (“**Decision:** PASS for CHECK D08\_cli\_guardrail”) with `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log` and CLI enforcement loci (`tools/cli/run_shim.py`, `tools/cli/__main__.py`, `tools/cli/guardrail.py`).  
* **Disposition:** Satisfied

Deliverables register mismatch note: PF10’s closure review includes a separate “deliverables register” (DEL-01..DEL-10) keyed to check receipts and closure artifacts; this does not 1:1 match the r3 plan’s D1–D11 list (PF10 — HDE Build Notes, §2.31). This record preserves the mismatch rather than reconciling it.

#### **2.9.4 PF Reference Map**

**Planned PF reference map (r3 Epic Plan HDE-EPIC024.md; selection):**

* PF27 — Canon Plan Templates, §2 HDE-EPIC-Plan (template-of-record for this plan structure)  
* PF09 — HDE Build Checklist, §Subtasks HDE-CALC002.1–HDE-CALC003.19; HDE-DISS003.2; HDE-SEPA003.3  
* PF04 — HDE Governance, §2.0.1 Determinism; §2.0.2 Canonical JSON; §2.0.6 Evidence tokens; §2.0.8 CLI/SDK parity harness; §2.0.10 Env/rails/infra; §2.0.19 QA harness tokens; §4.1.8 Sanity pipeline  
* PF12 — HDE Schemas and Artifacts, §4 Canonical JSON \+ arrays-as-sets; §8 Evidence Index \+ Mirror \+ path-proof discipline; showcompat deterministic capture evidence family; sampler evidence families; evidence index snapshot artifact family  
* PF14 — HDE Mechanics Guide, §1.1 / §1.3 / §1.6.x / §4.x / §5.1 / §11.3.x / §16.1–§16.2 (titles-only references)  
* PF19 — Glow QA Guide, §4.4 QA log discipline (qa\_step\_logs\_manifest.json, per-check primary.log, QA\_ROOT rules)  
* PF23 — Reality Audits, §1.2 Current Audit (presenter/emitter layering notes; evidence layout notes; showcompat capture tool references)  
* Epic Process Guide, §0.4 Execution posture; §3.5 Close Gate

**Execution and results sources used for this archive record:**

* PF10 — HDE Build Notes, §2.6–§2.31 (PR review stream, QA checks, remediation loops, closeout summary, closure review)  
* `r3 Epic Plan HDE-EPIC024.md` (planned deliverables/tokens/rails; several PF10 section pointers in this plan do not exist in PF10 v9.4.4 inputs)  
* PF20 — HDE-Phased Epics, §2.8 (adjacent epic-record style model \+ carry-forward context)

#### **2.9.5 Tokens and Evidence (Acceptance)**

##### **A) Acceptance tokens (names-only; planned roster)**

* **Base tokens (planned):**  
  * `ENV_LC_ALL_C_OK`  
  * `CANONICAL_JSON_GATE_OK`  
  * `ARRAYS_AS_SETS_OK`  
  * `SANITY_PIPELINE_OK`  
  * `EVIDENCE_INDEX_SNAPSHOT_CONTRACT_OK`  
  * `EVIDENCE_INDEX_PATH_BINDING_OK`  
  * `CLI_STREAM_DISCIPLINE_OK`  
  * `SAMPLER_POOL_OK`  
  * `QA_HARNESS_SELFTEST_OK`  
  * `QA_STEP_LOGS_MANIFEST_OK`  
  * `ACCEPTANCE_MAP_VIABILITY_OK`  
  * `TOKEN_REGISTRY_VALIDITY_OK`  
  * `LOWERCASE_NAMING_OK`  
  * `CLOSE_PACK_OK`  
* **QA check receipts (planned; PASS/FAIL contract):**  
  * `CHECK_D01_PASS` / `CHECK_D01_FAIL`  
  * `CHECK_D02_PASS` / `CHECK_D02_FAIL`  
  * `CHECK_D03_PASS` / `CHECK_D03_FAIL`  
  * `CHECK_D04_PASS` / `CHECK_D04_FAIL`  
  * `CHECK_D05_PASS` / `CHECK_D05_FAIL`  
  * `CHECK_D07_PASS` / `CHECK_D07_FAIL`  
  * `CHECK_D08_PASS` / `CHECK_D08_FAIL`  
  * `CHECK_D09_PASS` / `CHECK_D09_FAIL`  
  * `CHECK_D13_PASS` / `CHECK_D13_FAIL`  
  * `CHECK_D14_PASS` / `CHECK_D14_FAIL`  
  * `CHECK_D16_PASS` / `CHECK_D16_FAIL`  
  * `CHECK_D19_PASS` / `CHECK_D19_FAIL`  
  * `CHECK_PO_011_PASS` / `CHECK_PO_011_FAIL`  
  * `CHECK_PO_006_PASS` / `CHECK_PO_006_FAIL`  
  * `CHECK_PO_017_PASS` / `CHECK_PO_017_FAIL`  
  * `CHECK_D23_PASS` / `CHECK_D23_FAIL`  
  * `CHECK_STEP_0B_PASS` / `CHECK_STEP_0B_FAIL`  
  * `CHECK_CLOSEOUT_SUMMARY_PRESENT_OK`  
  * `CHECK_EPIC_CLOSURE_DECISION_PRESENT_OK`  
* **Close gate tokens (planned):**  
  * `CLOSE_PACK_PRESENT_OK`  
  * `EPIC_MANIFEST_VALID_OK`  
  * `DOC_DELTAS_CAPTURED_OK`  
  * `ACCEPTANCE_ARTIFACTS_PRESENT_OK`

##### **B) Evidence outputs required for close (planned; titles-only set)**

* Acceptance map path-of-record: `docs/acceptance_map_epic024.json`  
* QA root: `audit/qa/hde-epic024/` and per-check receipts at `audit/qa/hde-epic024/checks/<check_id>/primary.log`  
* Canonical JSON gate family: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
* Arrays-as-sets gate family: `audit/gates/determinism/arrays_as_sets.log` \+ `.sha256`  
* Env pins gate family: `audit/gates/determinism/env_pins.log` \+ `.sha256`  
* Evidence index snapshot family: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256`  
* Close pack endpoints (planned): `audit/EPIC-024_close_report.md` and `audit/EPIC-024_MANIFEST.json`  
* Doc deltas path-of-record (planned): `audit/docdeltas/hde-epic024_doc_deltas.md`

##### **C) Actual token/evidence posture recorded (PF10)**

* **Check receipts recorded as PASS (PF10):**  
  * `CHECK_STEP_0B_PASS`: PF10 — HDE Build Notes, §2.11 with `audit/qa/hde-epic024/checks/Step-0B_doc_delta_capture/primary.log`  
  * `CHECK_D02_PASS`: PF10 — HDE Build Notes, §2.12 with `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`  
  * `CHECK_D05_PASS`: PF10 — HDE Build Notes, §2.13 with `audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log`  
  * `CHECK_D09_PASS`: PF10 — HDE Build Notes, §2.14 with `audit/qa/hde-epic024/checks/D09_evidence_index_snapshot/primary.log`  
  * `CHECK_D13_PASS`: PF10 — HDE Build Notes, §2.15 with `audit/qa/hde-epic024/checks/D13_acceptance_map_viability/primary.log`  
  * `CHECK_D14_PASS`: PF10 — HDE Build Notes, §2.16 with `audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log`  
  * `CHECK_D19_PASS`: PF10 — HDE Build Notes, §2.17 with `audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log`  
  * `CHECK_PO_006_PASS`: PF10 — HDE Build Notes, §2.21 with `audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log`  
  * `CHECK_D16_PASS`: PF10 — HDE Build Notes, §2.22 with `audit/qa/hde-epic024/checks/D16_close_pack/primary.log`  
  * `CHECK_PO_011_PASS`: PF10 — HDE Build Notes, §2.23 with `audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log`  
  * `CHECK_D01_PASS`: PF10 — HDE Build Notes, §2.24 with `audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log`  
  * `CHECK_D03_PASS`: PF10 — HDE Build Notes, §2.25 with `audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log`  
  * `CHECK_D08_PASS`: PF10 — HDE Build Notes, §2.26 with `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log`  
  * `CHECK_D04_PASS`: PF10 — HDE Build Notes, §2.27 with `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`  
  * `CHECK_D07_PASS`: PF10 — HDE Build Notes, §2.28 with `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`  
  * `CHECK_PO_017_PASS`: PF10 — HDE Build Notes, §2.29 with `audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log`  
* **Close pack artifacts recorded (PF10):**  
  * `audit/EPIC-024_MANIFEST.json`, `audit/EPIC-024_hash_manifest.json`, `audit/EPIC-024_close_report.md` (PF10 — HDE Build Notes, §2.22 and §2.31)  
  * Planned close pack endpoints in r3 plan (`audit/EPIC-024_close_report.md` \+ `audit/EPIC-024_MANIFEST.json`) are present; PF10 adds `audit/EPIC-024_hash_manifest.json` beyond the planned list.  
* **Acceptance artifacts recorded (PF10):**  
  * `docs/acceptance_map_epic024.json` and sibling `docs/acceptance_map_epic024.json.path_proof.txt` (PF10 — HDE Build Notes, §2.15 and §2.31)  
  * `audit/qa/hde-epic024/acceptance_map_viability.log` (PF10 — HDE Build Notes, §2.15)  
  * `audit/qa/hde-epic024/token_evidence_matrix.md` (PF10 — HDE Build Notes, §2.16; includes a “token evidence matrix” with 25 tokens documented)  
* **Evidence index snapshot \+ binding validation (PF10):**  
  * Snapshot: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256` \+ `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt` (PF10 — HDE Build Notes, §2.14 and §2.20)  
  * Binding validation outputs recorded under remediation (PF10 — HDE Build Notes, §2.20): `audit/qa/hde-epic024/remediation/s3_po_006_rerun/evidence_path_binding_validation.ndjson` \+ `.sha256`

#### **2.9.6 QA Rails — Open/Close (Final PR)**

##### **A) Planned rails posture (r3 Epic Plan HDE-EPIC024.md)**

* **Open rails (planned):**  
  * No aliases in tokens; names-only roster.  
  * Acceptance map viability must PASS.  
  * QA harness discipline must be repo-first: per-check `primary.log` receipts; step logs manifest exists.  
  * Determinism gates (canonical JSON, arrays-as-sets, env pins) emit deterministic audit artifacts.  
* **Close rails (planned):**  
  * Close pack endpoints are present at `audit/EPIC-024_close_report.md` and `audit/EPIC-024_MANIFEST.json`.  
  * Doc deltas are captured at `audit/docdeltas/hde-epic024_doc_deltas.md`.  
  * Evidence index snapshot contract and binding validation artifacts exist.  
  * “PF20 has no step-by-step runbooks” posture: execution belongs in PF10 logs \+ harness scripts.

##### **B) Actual QA event stream (PF10; executed checks \+ outcomes)**

* PR review stream preceding QA receipts (PF10 — HDE Build Notes, §2.6–§2.10): PR01..PR05 reviews (including a Docs PR) recorded issues and deltas feeding later remediation.  
* Step-0B preflight doc delta capture (PF10 — HDE Build Notes, §2.11): PASS receipt and doc delta artifact creation — `audit/docdeltas/hde-epic024_doc_deltas.md`.  
* Determinism/evidence gates executed and recorded as PASS receipts:  
  * D02 canonical JSON (PF10 — HDE Build Notes, §2.12): `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` \+ `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`  
  * D05 arrays-as-sets (PF10 — HDE Build Notes, §2.13): `audit/gates/determinism/arrays_as_sets.log` \+ `.sha256`  
  * D09 evidence index snapshot (PF10 — HDE Build Notes, §2.14): `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256`  
  * D01 env pins (PF10 — HDE Build Notes, §2.24): `audit/gates/determinism/env_pins.log` \+ `.sha256`  
* Acceptance and harness discipline rails executed and recorded as PASS receipts:  
  * D13 acceptance map viability (PF10 — HDE Build Notes, §2.15): `docs/acceptance_map_epic024.json` \+ `audit/qa/hde-epic024/acceptance_map_viability.log`  
  * D14 harness selftest (PF10 — HDE Build Notes, §2.16): `tools/qa_harness/selftest_ci_entrypoint.sh` \+ `audit/qa/hde-epic024/selftest/run1/selftest_report.json`  
  * D19 step logs manifest (PF10 — HDE Build Notes, §2.17): `audit/qa/hde-epic024/qa_step_logs_manifest.json` \+ `.json.path_proof.txt`  
* Stream discipline and sampling rails executed and recorded as PASS receipts:  
  * D03 showcompat artifacts (PF10 — HDE Build Notes, §2.25): `artifacts/cli/showcompat/hde/all/v1/main.json` \+ `.sha256`  
  * D08 CLI guardrail (PF10 — HDE Build Notes, §2.26): enforcement loci under `tools/cli/` and receipt `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log`  
  * D04 sampler evidence (PF10 — HDE Build Notes, §2.27): receipt `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`  
  * D07 sanity pipeline (PF10 — HDE Build Notes, §2.28): receipt `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`  
* Governance/registry rails executed and recorded:  
  * po-006 token registry validity (PF10 — HDE Build Notes, §2.21): PASS receipt and comparison artifact `audit/qa/hde-epic024/checks/po-006_token_registry_validity/token_comparison.json`  
  * po-017 lowercase naming (PF10 — HDE Build Notes, §2.29): PASS receipt `audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log`  
* Close rails executed and recorded:  
  * D16 close pack (PF10 — HDE Build Notes, §2.22): PASS receipt \+ close artifacts (`audit/EPIC-024_MANIFEST.json`, `audit/EPIC-024_hash_manifest.json`, `audit/EPIC-024_close_report.md`)  
  * po-011 doc delta capture (PF10 — HDE Build Notes, §2.23): PASS receipt (distinct from Step-0B capture) — `audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log`

##### **C) Remediation loops (PF10; PR and OPS actions recorded)**

* Remedial PR01 (PF10 — HDE Build Notes, §2.18): token registry discovery \+ consistency fixes; evidence: `audit/qa/hde-epic024/remediation/s1_token_registry_discovery/codex_report.md`, `audit/qa/hde-epic024/remediation/s1_token_registry_discovery/token_sets.json`.  
* Remedial PR02 (PF10 — HDE Build Notes, §2.19): CI wiring and acceptance artifact adjustments; evidence: `.github/workflows/ci.yml`, `audit/qa/hde-epic024/remediation/s2_dev_acceptance_artifacts/acceptance_map_viability.json`, `audit/qa/hde-epic024/remediation/s2_dev_acceptance_artifacts/token_registry_export.csv`.  
* Remedial OPS01 (PF10 — HDE Build Notes, §2.20): reruns for po-006 and evidence index snapshot/binding validation; evidence: `audit/qa/hde-epic024/remediation/s3_po_006_rerun/ops_transcript.txt`, `audit/qa/hde-epic024/remediation/s3_po_006_rerun/po-006_token_registry_validity_rerun.md`, `audit/qa/hde-epic024/remediation/s3_po_006_rerun/d23_evidence_index_snapshot_contract_rerun.ndjson`, `audit/qa/hde-epic024/remediation/s3_po_006_rerun/evidence_path_binding_validation.ndjson`.

##### **D) Closeout posture (PF10)**

* PF10 closeout summary: “Verdict: READY WITH CAVEATS” (PF10 — HDE Build Notes, §2.30).  
* PF10 closure review: “Closure decision: SATISFIED (close the epic now)” with deferrals noted in that snapshot (PF10 — HDE Build Notes, §2.31). Later remediation/OPS rerun sections record PASS receipts for items earlier flagged as blocked (see §2.9.7).

#### **2.9.7 Tracked Issues**

**Planned (r3 Epic Plan HDE-EPIC024.md):**

* “Tracked Issues: None. Items drained to PF10 v9.3.6 §2.1–§2.4.”  
  * Note: This plan’s PF10 pointers reference v9.3.6 sections not present in PF10 v9.4.4 inputs; status is not recoverable from the provided PF10 inputs.  
  * Status: Unknown (not present in inputs)

**Actual issues / deferrals recorded (PF10):**

* **Plan vs execution drift (systemic):** PF10 check receipts record multiple ADR-DEV deviations (runner/script names, artifact loci, wrapper scripts, receipt formats) while still closing with PASS outcomes (PF10 — HDE Build Notes, §2.12–§2.29).  
* **Closure-review snapshot mismatch:** PF10 closure review (timestamped 2026-01-17 UTC) flags PO-006 and acceptance map viability as blocked/buggy, but later PF10 sections record PASS receipts after remediation/OPS rerun (PF10 — HDE Build Notes, §2.19–§2.21 vs §2.31). This record preserves the timeline mismatch.  
* **PO-006 token registry validity (deferral noted in snapshot):** PF10 closure review records `FAIL_BEHAVIOR` for po-006 because the token evidence matrix has 25 tokens while the token registry export has 14 (“missing 11 tokens”); later PF10 records `PASS` for CHECK po-006 after remediation/OPS rerun (PF10 — HDE Build Notes, §2.19–§2.21 vs §2.31).  
* **Acceptance map viability phantom pass bug (deferral noted in snapshot):** PF10 closure review records `FAIL_BEHAVIOR` for D13 due to a “phantom pass bug”; PF10 later records `PASS` for CHECK D13\_acceptance\_map\_viability (PF10 — HDE Build Notes, §2.15 vs §2.31).  
* **Token alias deprecation noted in snapshot:** PF10 closure review notes `QA_STEP_LOGS_CONSOLIDATED_OK` is deprecated and canonical is `QA_HARNESS_DISCIPLINE_OK` (PF10 — HDE Build Notes, §2.31).  
* **Evidence-path binding outputs locus drift:** r3 plan expects binding validation outputs under `audit/gates/evidence_index_snapshot/`; PF10 records binding validation outputs under remediation (`audit/qa/hde-epic024/remediation/s3_po_006_rerun/`) (PF10 — HDE Build Notes, §2.20).

#### **2.9.8 Plan Preflight (MUST)**

**Planned preflight gates (r3 Epic Plan HDE-EPIC024.md):**

* **A) Existing Work Check complete** (scope anchors and out-of-scope defined)  
* **B) Deliverables enumerated** (D1–D11 list complete with evidence required)  
* **C) Token roster present** (names-only; no aliases; PASS/FAIL receipts defined)  
* **D) QA rails defined** (open/close rails posture; no PF20 runbooks)  
* **E) Close pack baseline declared** (planned): `audit/EPIC-024_close_report.md` \+ `audit/EPIC-024_MANIFEST.json` (plus doc deltas, acceptance artifacts, and QA root requirements)

**Actual close gates observed (PF10; manual results for EPIC024 close):**

* Step receipts recorded as PASS for the planned receipt set (subset where PF10 provides receipts):  
  * Step-0B doc deltas: PF10 — HDE Build Notes, §2.11 (`audit/qa/hde-epic024/checks/Step-0B_doc_delta_capture/primary.log`)  
  * D01 env pins: PF10 — HDE Build Notes, §2.24  
  * D02 canonical JSON: PF10 — HDE Build Notes, §2.12  
  * D03 showcompat artifacts: PF10 — HDE Build Notes, §2.25  
  * D04 sampler evidence: PF10 — HDE Build Notes, §2.27  
  * D05 arrays-as-sets: PF10 — HDE Build Notes, §2.13  
  * D07 sanity pipeline: PF10 — HDE Build Notes, §2.28  
  * D08 CLI guardrail: PF10 — HDE Build Notes, §2.26  
  * D09 evidence index snapshot: PF10 — HDE Build Notes, §2.14  
  * D13 acceptance map viability: PF10 — HDE Build Notes, §2.15  
  * D14 harness selftest: PF10 — HDE Build Notes, §2.16  
  * D16 close pack: PF10 — HDE Build Notes, §2.22  
  * D19 step logs manifest: PF10 — HDE Build Notes, §2.17  
  * po-006 token registry validity: PF10 — HDE Build Notes, §2.21  
  * po-011 doc delta capture: PF10 — HDE Build Notes, §2.23  
  * po-017 lowercase naming: PF10 — HDE Build Notes, §2.29  
* Close pack baseline declared in the plan is satisfied and expanded in PF10:  
  * Present: `audit/EPIC-024_close_report.md`, `audit/EPIC-024_MANIFEST.json` (PF10 — HDE Build Notes, §2.22)  
  * Additional PF10 artifact: `audit/EPIC-024_hash_manifest.json` (PF10 — HDE Build Notes, §2.22)  
* Plan “ASK OK?” placeholder: present in `r3 Epic Plan HDE-EPIC024.md` preflight section; approval disposition is not recorded in that plan file. PF10 nonetheless records closure (“SATISFIED”) (PF10 — HDE Build Notes, §2.31).

### **2.10 HDE-EPIC025 Epic Plan**

#### **2.10.1 Meta**

**Status:** Done  
**Phase:** Conjunction (PF21)  
**Priority:** P0  
**Owner:** PO  
**Epic name (short):** Conjunction Pass 1  
**Date started:** 2026-01-23  
**Date completed:** 2026-02-06  
**Epic outcome (per PF10):** “Overall readiness: Ready with caveats” (PF10 — HDE Build Notes, §2.50)

**Active PRs:** Unknown (not present in inputs)

**Depends on:**

* HDE-EPIC024  
* HDE-EPIC023  
* PF20 — HDE-Phased Epics  
* PF10 — HDE Build Notes  
* PF12 — HDE Schemas & Artifacts  
* PF19 — Glow QA Guide  
* PF09 — HDE Build Checklist  
* PF04 — HDE Governance

#### **2.10.2 Existing Work Check**

**Planned (from r7 Epic Plan HDE-EPIC025.md):**

* Compatibility surface internal contract and endpoint catalog discipline.  
* CLI showcompat contract truth and serializer coupling.  
* Reader bytes and transport invariants (A7) existing proof surface check.  
* Canonical bytes and canonical JSON gating surfaces check.  
* Evidence index and mirror parity check.  
* Close pack pair and docdeltas surfaces check.  
* If gaps are found, capture as TI-\#\#\# and/or cross-epic ISSUE-\#\#\#, and defer.

**Actual (from PF10):**

* Baseline discovery executed and logged as `d0_discovery` (PF10 — HDE Build Notes, §2.30) with evidence pointer `checks/d0_discovery/primary.log`.  
* Endpoint catalog/internal-only/env-gate posture is explicitly evidenced (PF10 — HDE Build Notes, §2.11): token evidence recorded as `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, with evidence pointer `artifacts/audit/compat_endpoints_catalog.json`.  
* Reader A7 proof surface is captured (PF10 — HDE Build Notes, §2.13): evidence pointers include `artifacts/proofs/bytes_for_reader_a7.json` and `artifacts/proofs/reader_a7_invariants_report.json`.  
* Close-pack and global gates executed/recorded during close (PF10 — HDE Build Notes, §2.14): evidence pointers include `"audit/EPIC-025_MANIFEST.json"`, `"audit/EPIC-025_close_report.md"`, `audit/qa/hde-epic025/run.json`, and `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`.

#### **2.10.3 Deliverables (Jobs-to-be-done) — Planned vs Actual Reconciliation**

**Planned deliverables (from r7 Epic Plan HDE-EPIC025.md):**

##### **D1 — Compat surface contract and endpoint catalog discipline**

* **Plan statement:** “Compatibility surface internal contract is explicit and enforced.”  
* **Planned acceptance tokens (names-only):** `HTTP_COMPAT_ENDPOINT_CATALOG_OK`, `HTTP_COMPAT_INTERNAL_ADMIN_OK`, `HTTP_COMPAT_GET_IS_PROBE_ONLY_OK`, `HTTP_COMPAT_POST_ONLY_OK`, `HTTP_COMPAT_ENV_GATE_PRESENT_OK`.  
* **Actual (PF10):** PR01 delivered catalog \+ internal-only \+ env-gate posture (PF10 — HDE Build Notes, §2.11) with token evidence recorded as `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK` and evidence pointer `artifacts/audit/compat_endpoints_catalog.json` (PF10 — HDE Build Notes, §2.11 “Evidence Print”).  
* **Disposition:** Satisfied (evidence present; planned token names are not the token names recorded in PF10).

##### **D2 — CLI contract truth is serializer-coupled**

* **Plan statement:** “CLI contract truth is serializer-coupled and no longer needs the HTTP compat endpoint.”  
* **Planned acceptance token (names-only):** `CLI_SHOWCOMPAT_OUTPUT_EQUALS_SERIALIZER_OK`.  
* **Actual (PF10):** PR02 added parity coverage across CLI+HTTP (`tests/http/test_compat_contract_parity.py`, `tests/cli/test_show_compat.py`) with local proof PASS (“3 passed”) (PF10 — HDE Build Notes, §2.12).  
* **Disposition:** Satisfied (evidence indicates behavior; token not explicitly claimed by this name in PF10).

##### **D3 — CLI conformance and tooling is tightened**

* **Plan statement:** “CLI conformance and tooling is tightened; errors parity and return code behavior is locked.”  
* **Planned acceptance tokens (names-only):** `CLI_SHOWCOMPAT_RETURNS_0_OK`, `CLI_ERRORS_PARITY_OK`, `CLI_SHOWCOMPAT_CONTRACT_OK`, `COMPAT_TRUTH_SER_IS_WIRED_OK`.  
* **Actual (PF10):**  
  * CLI showcompat and contract parity tests exercised with local proof PASS (`tests/cli/test_show_compat.py`, `tests/http/test_compat_contract_parity.py`) (PF10 — HDE Build Notes, §2.12).  
  * CLI errors parity baseline test exists and passed locally (`tests/cli/test_cli_errors_parity.py` with local proof “3 passed”) (PF10 — HDE Build Notes, §2.11).  
* **Disposition:** Satisfied (evidence present; tokens not explicitly claimed by these names in PF10).

##### **D4 — Reader surface and transport invariants are locked**

* **Plan statement:** “Reader surface and transport invariants are locked.”  
* **Planned acceptance tokens (names-only):** `HTTP_COMPAT_ENDPOINT_IS_INTERNAL_OK`, `READER_SURFACE_A7_INVARIANTS_OK`, `HTTP_READER_BYTES_CANONICAL_OK`, `READER_MANDATORY_JSON_GATE_OK`.  
* **Actual (PF10):** PR03 produced reader A7 proof artifacts (PF10 — HDE Build Notes, §2.13), including `artifacts/proofs/bytes_for_reader_a7.json`, `artifacts/proofs/bytes_for_reader_a7.json.sha256`, and `artifacts/proofs/reader_a7_invariants_report.json`.  
* **Disposition:** Satisfied (proof artifacts present; tokens not explicitly claimed by these names in PF10).

##### **D5 — Global discipline: canonical JSON and evidence indexing is locked**

* **Plan statement:** “Global discipline — canonical JSON and evidence indexing is locked.”  
* **Planned acceptance tokens (names-only):** `CANONICAL_JSON_GATE_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_MIRROR_PARITY_OK`, `STEP_LOGS_MANIFEST_OK`.  
* **Actual (PF10):** PR04 recorded token satisfaction for `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_MIRROR_PARITY_OK` (PF10 — HDE Build Notes, §2.14). Evidence pointers include:  
  * `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log` and `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
  * `audit/qa/hde-epic025/checks/gate_evidence_index_snapshot/primary.log` and `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
  * `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log` and `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/evidence_paths_validation.ndjson`  
  * `audit/qa/hde-epic025/step_log_manifest.json` (file present; token `STEP_LOGS_MANIFEST_OK` is not explicitly claimed by this name in PF10)  
* **Disposition:** Satisfied for evidence-path validation, evidence index update, mirror parity; partial on token-name coverage (some planned token names not explicitly used in PF10).

##### **D6 — Close pack is canonical and complete**

* **Plan statement:** “Close report and manifest are canonical, evidence-rooted, and self-describing.”  
* **Planned acceptance tokens (names-only):** `CLOSE_PACK_PAIR_OK`, `CLOSE_REPORT_KEY_OUTPUTS_BOUND_OK`, `TOKEN_EVIDENCE_MATRIX_OK`, `QA_EVIDENCE_ROOT_OK`, `EPIC_CLOSE_PACK_OK`.  
* **Actual (PF10):** PR04 recorded token satisfaction for `QA_EVIDENCE_ROOT_OK`, `CLOSE_PACK_PAIR_OK`, `CLOSE_REPORT_KEY_OUTPUTS_BOUND_OK` (PF10 — HDE Build Notes, §2.14) with evidence pointers including `"audit/EPIC-025_MANIFEST.json"`, `"audit/EPIC-025_close_report.md"`, and `audit/qa/hde-epic025/run.json`.  
* **Disposition:** Mostly satisfied (close-pack pair \+ key outputs binding \+ QA evidence root). `TOKEN_EVIDENCE_MATRIX_OK` is **Unknown (not present in inputs)**: PF10 does not reference `audit/qa/hde-epic025/token_evidence_matrix.md` (planned), nor cite an alternate token→evidence matrix artifact.

##### **Docs sweep (planned; out-of-band)**

* **Planned:** “Docs sweep PR (out-of-band, as needed).” (r7 Epic Plan HDE-EPIC025.md)  
* **Actual (PF10):** Docs PR executed (PF10 — HDE Build Notes, §2.15) with evidence pointer `audit/docdeltas/hde-epic025_doc_deltas.md`.

**Planned vs actual notes (non-silent mismatches):**

* Planned token naming uses `HTTP_COMPAT_*` tokens; PF10 records `ENDPOINTS_CATALOG_*` token evidence and does not explicitly claim the `HTTP_COMPAT_*` token names (PF10 — HDE Build Notes, §2.11).  
* Planned QA check log naming in r7 uses long-form check directories (example: `audit/qa/hde-epic025/checks/po-001_selected_route_a7_invariants/primary.log`), while PF10 records check logs under short IDs (example: `audit/qa/hde-epic025/checks/po-001/primary.log`) (PF10 — HDE Build Notes, §2.31).  
* r7 plan expects `audit/qa/hde-epic025/closeout_summary.md`; PF10 does not reference this artifact (**Unknown (not present in inputs)**).

#### **2.10.4 PF Reference Map**

**Planned PF references (from r7 Epic Plan HDE-EPIC025.md “Depends on”):**

* HDE-EPIC024  
* HDE-EPIC023  
* PF20 — HDE-Phased Epics  
* PF10 — HDE Build Notes  
* PF12 — HDE Schemas & Artifacts  
* PF19 — Glow QA Guide  
* PF09 — HDE Build Checklist  
* PF04 — HDE Governance

**Execution and results sources used for this archive record:**

* PF10 — HDE Build Notes, §2.11 (PR01), §2.12 (PR02), §2.13 (PR03), §2.14 (PR04), §2.15 (Docs PR), §2.16 (Retrospective), §2.17 (PF23 Updated), §2.18 (Audit Report), §2.19 (ADR-EPIC025-ARCH-001), §2.30–§2.46 (QA step logs), §2.50 (Final QA Closeout Review \+ QA RCA).  
* r7 Epic Plan HDE-EPIC025.md (planned scope, acceptance tokens, planned evidence outputs).  
* PF27 — Plan Templates, §2.4.3 Epic Record Template (Normative).

#### **2.10.5 Tokens and Evidence (Acceptance)**

**Planned tokens (from r7 Epic Plan HDE-EPIC025.md; names-only; no aliases):**

* Baseline tokens: `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`, `HTTP_COMPAT_ENDPOINT_CATALOG_OK`, `CLI_SHOWCOMPAT_CONTRACT_OK`, `READER_SURFACE_A7_INVARIANTS_OK`, `CANONICAL_JSON_GATE_OK`  
* Deliverable-specific tokens: `HTTP_COMPAT_INTERNAL_ADMIN_OK`, `HTTP_COMPAT_GET_IS_PROBE_ONLY_OK`, `HTTP_COMPAT_POST_ONLY_OK`, `HTTP_COMPAT_ENV_GATE_PRESENT_OK`, `CLI_SHOWCOMPAT_OUTPUT_EQUALS_SERIALIZER_OK`, `CLI_SHOWCOMPAT_RETURNS_0_OK`, `CLI_ERRORS_PARITY_OK`, `COMPAT_TRUTH_SER_IS_WIRED_OK`, `HTTP_COMPAT_ENDPOINT_IS_INTERNAL_OK`, `HTTP_READER_BYTES_CANONICAL_OK`, `READER_MANDATORY_JSON_GATE_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_MIRROR_PARITY_OK`, `STEP_LOGS_MANIFEST_OK`  
* Close gate token set: `QA_EVIDENCE_ROOT_OK`, `EPIC_CLOSE_PACK_OK`, `CLOSE_PACK_PAIR_OK`, `CLOSE_REPORT_KEY_OUTPUTS_BOUND_OK`, `TOKEN_EVIDENCE_MATRIX_OK`

**Planned evidence outputs (from r7 Epic Plan HDE-EPIC025.md; verbatim paths):**

* `audit/qa/hde-epic025/` root populated with step logs and check logs.  
* `audit/qa/hde-epic025/checks/d0_discovery/primary.log`  
* `audit/qa/hde-epic025/checks/po-001_selected_route_a7_invariants/primary.log`  
* `audit/qa/hde-epic025/checks/po-002_capture_a7_bytes/primary.log`  
* `audit/qa/hde-epic025/checks/po-003_cli_showcompat_contract/primary.log`  
* `audit/qa/hde-epic025/checks/po-004_cli_error_parity/primary.log`  
* `audit/qa/hde-epic025/checks/po-005_cli_showcompat_output_parity/primary.log`  
* `audit/qa/hde-epic025/checks/po-006_check_http_compat_mandatory_gate/primary.log`  
* `audit/qa/hde-epic025/checks/po-007_check_http_compat_internal/primary.log`  
* `audit/qa/hde-epic025/checks/po-008_check_http_compat_get_is_probe_only/primary.log`  
* `audit/qa/hde-epic025/checks/po-009_check_http_compat_post_only/primary.log`  
* `audit/qa/hde-epic025/checks/po-010_check_http_compat_env_gate/primary.log`  
* `audit/qa/hde-epic025/checks/po-011_gate_canonical_json/primary.log`  
* `audit/qa/hde-epic025/checks/po-012_gate_arrays_as_sets/primary.log`  
* `audit/qa/hde-epic025/checks/po-013_gate_env_pins/primary.log`  
* `audit/qa/hde-epic025/checks/po-014_gate_evidence_paths/primary.log`  
* `audit/EPIC-025_close_report.md`  
* `audit/EPIC-025_MANIFEST.json`  
* `audit/qa/hde-epic025/token_evidence_matrix.md`  
* `docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/audit/ENDPOINTS_CATALOG.json` \+ `docs/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/proofs/*` (reader bytes, invariants reports, parity proofs)  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` \+ `.sha256`  
* `audit/gates/determinism/arrays_as_sets.log` \+ `.sha256`  
* `audit/gates/determinism/env_pins.log` \+ `.sha256`  
* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.sha256`  
* `docs/acceptance_map_epic025.json`  
* `docs/acceptance_map_epic025.json.path_proof.txt`  
* `audit/docdeltas/hde-epic025_doc_deltas.md`  
* `audit/qa/hde-epic025/step_log_manifest.json`  
* `audit/qa/hde-epic025/run.json`  
* `audit/qa/hde-epic025/closeout_summary.md`

**Actual token claims and evidence pointers (from PF10):**

* PF10 §2.11 token evidence recorded (names-only): `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`.  
* PF10 §2.14 tokens satisfied (names-only): `QA_EVIDENCE_ROOT_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_MIRROR_PARITY_OK`, `CLOSE_PACK_PAIR_OK`, `CLOSE_REPORT_KEY_OUTPUTS_BOUND_OK`.

**Evidence pointers (verbatim; PF10 §2.14 unless otherwise stated):**

* `"audit/EPIC-025_MANIFEST.json"` (normalized: `audit/epic-025_manifest.json`)  
* `"audit/EPIC-025_close_report.md"` (normalized: `audit/epic-025_close_report.md`)  
* `audit/qa/hde-epic025/run.json`  
* `audit/qa/hde-epic025/step_log_manifest.json`  
* `docs/acceptance_map_epic025.json`  
* `docs/acceptance_map_epic025.json.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`  
* `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/evidence_paths_validation.ndjson`  
* `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/evidence_paths_validation.ndjson.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `audit/qa/hde-epic025/checks/gate_evidence_index_snapshot/primary.log`  
* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.sha256`  
* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
* `audit/qa/hde-epic025/checks/gate_evidence_index_snapshot/evidence_index_snapshot.log`  
* `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log`  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.sha256`  
* `audit/qa/hde-epic025/checks/gate_canonical_json/json_gate_check_summary.txt`  
* `audit/qa/hde-epic025/checks/gate_arrays_as_sets/primary.log`  
* `audit/gates/determinism/arrays_as_sets.log`  
* `audit/gates/determinism/arrays_as_sets.log.sha256`  
* `audit/qa/hde-epic025/checks/gate_env_pins/primary.log`  
* `audit/gates/determinism/env_pins.log`  
* `audit/gates/determinism/env_pins.log.sha256`  
* `audit/docdeltas/hde-epic025_doc_deltas.md`  
* `artifacts/audit/compat_endpoints_catalog.json` (PF10 — HDE Build Notes, §2.11)  
* `"artifacts/audit/ENDPOINTS_CATALOG.json"` (normalized: `artifacts/audit/endpoints_catalog.json`) (PF10 — HDE Build Notes, §2.13)  
* `"docs/ENDPOINTS_CATALOG.json.sha256"` (normalized: `docs/endpoints_catalog.json.sha256`) (PF10 — HDE Build Notes, §2.13)  
* `artifacts/proofs/bytes_for_reader_a7.json` (PF10 — HDE Build Notes, §2.13)  
* `artifacts/proofs/reader_a7_invariants_report.json` (PF10 — HDE Build Notes, §2.13)

**Gaps / unknowns (from planned vs PF10-cited artifacts):**

* `audit/qa/hde-epic025/token_evidence_matrix.md` is **Unknown (not present in inputs)** (planned by r7; not referenced in PF10).  
* `audit/qa/hde-epic025/closeout_summary.md` is **Unknown (not present in inputs)** (planned by r7; not referenced in PF10).  
* Planned check-log directory names in r7 (e.g., `po-001_selected_route_a7_invariants`) do not match PF10-cited check-log paths (e.g., `audit/qa/hde-epic025/checks/po-001/primary.log`) (PF10 — HDE Build Notes, §2.31).

#### **2.10.6 QA Rails — Open/Close (Final PR)**

**Planned QA rails posture (from r7 Epic Plan HDE-EPIC025.md):** Unknown (not present in inputs).

**Actual QA execution posture (PF10):**

* PF10 records all step-level verdicts PASS for the QA run step set (PF10 — HDE Build Notes, §2.50 “What passed: PF10 §§2.30–2.46 show all step-level verdicts PASS.”).  
* Step set executed (PF10 section anchors): `d0_discovery` (PF10 §2.30) and `po-001` through `po-014` (PF10 §§2.31–2.46).  
* Core QA evidence pointers (PF10 — HDE Build Notes, §2.14 and §§2.30–2.46): `audit/qa/hde-epic025/run.json`, `audit/qa/hde-epic025/step_log_manifest.json`.  
* Example per-check evidence pointers (PF10 — HDE Build Notes, §§2.31–2.46):  
  * `audit/qa/hde-epic025/checks/po-001/primary.log`  
  * `audit/qa/hde-epic025/checks/po-005/primary.log`  
  * `audit/qa/hde-epic025/checks/po-014/primary.log`

**Recorded QA deviations / ADRs (PF10):**

* Rails posture mismatch recorded for `po-005` with “open rails” deviation (`ALLOW_NETWORK=1 SAFE_MODE=0`) and logged as `ADR-DEV-01` (PF10 — HDE Build Notes, §2.38; also summarized in PF10 §2.50).  
* Additional QA execution ADRs recorded in the step logs: `ADR-DEV-02` and `ADR-DEV-03` (PF10 — HDE Build Notes, §2.38–§2.46; summarized in PF10 §2.50).  
* QA closeout process caveat recorded: PF10 notes the run did not have a discrete QA plan document and relied on inlined plan steps \+ manual logging (PF10 — HDE Build Notes, §2.50 “Process caveat”).

#### **2.10.7 Tracked Issues**

**Planned deferrals and issues tracked by this epic (from r7 Epic Plan HDE-EPIC025.md):**

* **TI-001:** “Legacy endpoints table is not fully stable; some mismatch between docs and actual surface remains.”  
  * Disposition: Unknown (not present in inputs).  
* **TI-002:** “Dev HTTP Harness and Writer Surfaces are still missing; deferred.”  
  * Disposition: Carried forward — PF10 records: “TI-002: defers Dev HTTP Harness and Writer Surfaces to HDE-EPIC026.” (PF10 — HDE Build Notes, §2.14).  
* **TI-003:** “Determine whether evidence index should embed per-run summary (future).”  
  * Disposition: Unknown (not present in inputs).  
* **TI-004:** “Normalize internal endpoint error responses (if needed) — deferred.”  
  * Disposition: Unknown (not present in inputs).

**Planned cross-epic issues (from r7 Epic Plan HDE-EPIC025.md):**

* ISSUE-QA-ROOT-NAMING — Unknown (not present in inputs).  
* ISSUE-CLOSEPACK-PAIR — Unknown (not present in inputs).  
* ISSUE-EVIDENCE-ENDPOINTS — Unknown (not present in inputs).  
* ISSUE-EVIDENCE-PATHS-VALIDATOR — Unknown (not present in inputs).

**Additional PF10-recorded gaps (not explicitly listed in r7 plan):**

* “Tooling audit requested: ensure evidence tooling auto-enumerates all required artifacts; avoid manual omissions.” (PF10 — HDE Build Notes, §2.16 “Gaps and follow-ups”).  
* “Need official link to reality audit endpoints and helper surfaces; reduce ambiguity.” (PF10 — HDE Build Notes, §2.16 “Gaps and follow-ups”).

#### **2.10.8 Plan Preflight (MUST)**

**Planned preflight rails (from r7 Epic Plan HDE-EPIC025.md):**

* P1 Token registry validation: planned token names must match canonical registry names; no aliases.  
* P2 Close pack baseline: close report \+ manifest must exist as a pair (`audit/EPIC-025_close_report.md`, `audit/EPIC-025_MANIFEST.json`).  
* P3 Evidence bundle completeness: required evidence artifacts must be produced and path-proofed.  
* P4 Canonical evidence-path binding validator: run evidence-path binding validator; treat missing/unknown paths as defects.  
* P5 Acceptance artifact hygiene: acceptance map and evidence index must have `.sha256` and `.path_proof.txt` where required.  
* P6 Lowercase directory naming: audit/qa evidence root must be lowercase and consistent.

**Actual (PF10):**

* Close pack pair exists and is cited as evidence pointers: `"audit/EPIC-025_close_report.md"`, `"audit/EPIC-025_MANIFEST.json"` (PF10 — HDE Build Notes, §2.14).  
* Evidence-path binding validation is explicitly recorded: `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log` and `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/evidence_paths_validation.ndjson` (PF10 — HDE Build Notes, §2.14).  
* Acceptance map and evidence index artifacts are cited with path proofs/hashes (PF10 — HDE Build Notes, §2.14): `docs/acceptance_map_epic025.json.path_proof.txt`, `docs/evidence/INDEX.sha256`, `docs/evidence/INDEX.json.path_proof.txt`.  
* Planned `audit/qa/hde-epic025/token_evidence_matrix.md` remains Unknown (not present in inputs): not referenced by PF10.

### **2.11 HDE-EPIC026 Epic Plan**

#### **2.11.1 Meta**

**Epic ID:** HDE-EPIC026  
**Epic title (Implementation Guide):** Conjunction Pass 2 (r8 epic plan HDE-EPIC026.md, header)  
**Epic name (short):** HDE Conjunction Pass 2  
**Phase:** Conjunction (PF21)  
**Status:** Archived  
**Owner:** Unknown (not present in inputs)  
**Priority:** Unknown (not present in inputs)  
**Date started:** 2026-02-07 (PF10 — HDE Build Notes, §2.5 PR01 HDE-EPIC026 2026-02-07)  
**Date completed:** 2026-03-03 (task input; PF10 close date not explicitly stated)  
**Epic outcome (per PF10):** “Overall readiness (PF10-evidence-grounded): Not ready” (PF10 — HDE Build Notes, §2.32 HDE-EPIC026 QA Closeout Summary)

**Epic intent (planned; one paragraph):** Objective: extend the HDE Engine and Glow `/v1` API to support Conjunction as a first-class result surface with deterministic outputs, including provider acquisition posture, dev harness endpoints (sampler/reader/writer), showcompat/CLI support, evidence/index hygiene, and a close-pack generator for archival closeout artifacts. (r8 epic plan HDE-EPIC026.md, §2 Epic intent; §4 Deliverables)

**Scope anchor (PF13):** Unknown (not present in inputs)  
**Stakeholders:** Unknown (not present in inputs)

**PR stream (PF10):** PR01–PR08 \+ Docs PR (PF10 — HDE Build Notes, §2.5–§2.14)  
**QA log stream (PF10):** CHECK `po-000` through CHECK `po-012` (PF10 — HDE Build Notes, §2.19–§2.31)

#### **2.11.2 Existing Work Check (MUST)**

**Planned existing-work posture (Implementation Guide):**

* Existing showcompat already had a Conjunction placeholder; this epic extends it to emit canonical Conjunction outputs. (r8 epic plan HDE-EPIC026.md, §3 Existing Work Check)  
* Existing `/dev/sampler` and `/dev/reader` endpoints exist for other surfaces; this epic adds Conjunction variants. (r8 epic plan HDE-EPIC026.md, §3 Existing Work Check)  
* Existing evidence/index and close-pack generator patterns exist; this epic extends them for EPIC026 close artifacts. (r8 epic plan HDE-EPIC026.md, §3 Existing Work Check; §4.8 Deliverable D-008)

**Actual reuse and delta (PF10):**

* showcompat/CLI Conjunction support changes are recorded in PR05 and validated in CHECK `po-008` and CHECK `po-009` (PF10 — HDE Build Notes, §2.9 PR05 HDE-EPIC026; §2.26; §2.28), with closeout caveat that CHECK `po-009` is treated as “not executable as intended” and “REMEDIATION DEFERRED DUE TO PLANNING DEFECT” (PF10 — HDE Build Notes, §2.32).  
* Dev harness endpoints are recorded in PR03 and PR04 and validated in CHECK `po-005` / `po-006` / `po-007` (PF10 — HDE Build Notes, §2.7 PR03; §2.8 PR04; §2.23–§2.25), with closeout caveat that CHECK `po-005` is treated as “Contaminated (not auditable from PF10)” and cited as a reason overall readiness is “Not ready” (PF10 — HDE Build Notes, §2.32).  
* Close-pack generator and close-pack artifacts are recorded under PR08 (including remediation attempts) and validated in CHECK `po-012` (PF10 — HDE Build Notes, §2.13 PR08; §2.31).

#### **2.11.3 Deliverables (Jobs-to-be-done) — Planned vs Actual Reconciliation**

##### **D1 — Conjunction output contract and deterministic envelope**

* **Planned (Implementation Guide):** Deliverable D-001 — “Define and land the canonical Conjunction output contract (bytes/canonical form), including deterministic preimage rules and ABBA identity invariants.” (r8 epic plan HDE-EPIC026.md, §4.1 Deliverable D-001)  
* **Actual (PF10):** PR01 records token evidence print including `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK` (PF10 — HDE Build Notes, §2.5). Live QA CHECK `po-000` and CHECK `po-001` are recorded as PASS, with evidence under `audit/qa/hde-epic026/checks/po-001/primary.log` (PF10 — HDE Build Notes, §2.19).  
* **Disposition (archive):** Satisfied — PASS for `po-000`/`po-001` is not cited as a closeout blocker (PF10 — HDE Build Notes, §2.32).

##### **D2 — Provider acquisition posture for Conjunction inputs**

* **Planned (Implementation Guide):** Deliverable D-002 — “Establish provider acquisition posture (local-first), including deterministic handling of missing providers and explicit error semantics surfaced through the `/v1` Conjunction result lane.” (r8 epic plan HDE-EPIC026.md, §4.2 Deliverable D-002)  
* **Actual (PF10):** PR02 records provider acquisition changes (PF10 — HDE Build Notes, §2.6). Live QA CHECK `po-002` is recorded as PASS (PF10 — HDE Build Notes, §2.20). CHECK `po-003`/`po-004` are recorded as PASS with ADR-DEV-01 and ADR-DEV-02 deviations recorded (PF10 — HDE Build Notes, §2.21).  
* **Disposition (archive):** Satisfied — PASS for `po-002`–`po-004` is not cited as a closeout blocker (PF10 — HDE Build Notes, §2.32).

##### **D3 — Dev HTTP harness: sampler \+ reader Conjunction preview endpoints**

* **Planned (Implementation Guide):** Deliverable D-003 — “Add dev-only HTTP harness endpoints for Conjunction preview (`/dev/sampler/conjunction`, `/dev/reader/conjunction`) and ensure they are rails-gated and deterministic.” (r8 epic plan HDE-EPIC026.md, §4.3 Deliverable D-003)  
* **Actual (PF10):** PR03 records endpoints added (`/dev/sampler/conjunction`, `/dev/reader/conjunction`) and catalog updates (PF10 — HDE Build Notes, §2.7). Live QA CHECK `po-005` and CHECK `po-006` are recorded as PASS with evidence pointers including `audit/qa/hde-epic026/checks/po-005/primary.log` and `audit/qa/hde-epic026/checks/po-005/route_proof.txt` (PF10 — HDE Build Notes, §2.23) and the `po-006` evidence directory (`audit/qa/hde-epic026/checks/po-006/`) (PF10 — HDE Build Notes, §2.24).  
* **Disposition (archive):** Not satisfied for closeout — PF10’s QA Closeout Summary treats CHECK `po-005` as “Contaminated (not auditable from PF10)” and cites it as a direct reason overall readiness is “Not ready” (PF10 — HDE Build Notes, §2.32), even though §2.23 records a PASS.

##### **D4 — Dev writer harness: Conjunction preview writer endpoint**

* **Planned (Implementation Guide):** Deliverable D-004 — “Add dev-only writer endpoint for Conjunction preview (`/dev/writer/conjunction`) and ensure rails gating and deterministic behavior.” (r8 epic plan HDE-EPIC026.md, §4.4 Deliverable D-004)  
* **Actual (PF10):** PR04 records `/dev/writer/conjunction` plus endpoint catalog updates (PF10 — HDE Build Notes, §2.8). Live QA CHECK `po-007` is recorded as PASS with evidence pointers including `audit/qa/hde-epic026/checks/po-007/primary.log` (PF10 — HDE Build Notes, §2.25).  
* **Disposition (archive):** Satisfied — PASS for `po-007` is not cited as a closeout blocker (PF10 — HDE Build Notes, §2.32).

##### **D5 — Governed evidence posture for Conjunction outputs**

* **Planned (Implementation Guide):** Deliverable D-005 — “Bind Conjunction outputs to governed evidence posture: evidence index entries, path proofs, and close-pack artifacts suitable for audit.” (r8 epic plan HDE-EPIC026.md, §4.5 Deliverable D-005)  
* **Actual (PF10):** PR07 records evidence/index updates and governance surfaces (PF10 — HDE Build Notes, §2.12). Live QA CHECK `po-011` is recorded as PASS (PF10 — HDE Build Notes, §2.30). CHECK `po-012` close pack includes an evidence index file `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_evidence_index.json` (PF10 — HDE Build Notes, §2.31).  
* **Disposition (archive):** Partial — evidence/index artifacts exist (e.g., `epic-026_evidence_index.json` in the `po-012` close pack), but PF10’s QA Closeout Summary diagnoses “evidence hygiene \+ plan-to-evidence traceability drift,” and overall readiness remains “Not ready” due to `po-005`/`po-009` (PF10 — HDE Build Notes, §2.32).

##### **D6 — showcompat: Conjunction support \+ rails-safe CLI behavior**

* **Planned (Implementation Guide):** Deliverable D-006 — “Extend showcompat for Conjunction, ensure deterministic rendering, and enforce rails refusal (closed) versus open-rails acquisition semantics.” (r8 epic plan HDE-EPIC026.md, §4.6 Deliverable D-006)  
* **Actual (PF10):** PR05 records showcompat changes (PF10 — HDE Build Notes, §2.9). Live QA CHECK `po-008` is recorded as PASS (PF10 — HDE Build Notes, §2.26). CHECK `po-009` is recorded, with evidence pointers including `audit/qa/hde-epic026/checks/po-009/primary.log` (PF10 — HDE Build Notes, §2.28), but the QA Closeout Summary states CHECK `po-009` is “not executable as intended” and its decision is “REMEDIATION DEFERRED DUE TO PLANNING DEFECT,” and cites `po-009` as a reason overall readiness is “Not ready” (PF10 — HDE Build Notes, §2.32).  
* **Disposition (archive):** Not satisfied for closeout — Conjunction showcompat exists and `po-008` passes, but `po-009` is not accepted as executed-as-intended at close (PF10 — HDE Build Notes, §2.32).

##### **D7 — Documentation \+ endpoints catalog alignment**

* **Planned (Implementation Guide):** Deliverable D-007 — “Update docs and public-facing catalogs to include Conjunction surfaces, endpoints, and deterministic behavior notes.” (r8 epic plan HDE-EPIC026.md, §4.7 Deliverable D-007)  
* **Actual (PF10):** PR06 (docs alignment) and the Docs PR are recorded (PF10 — HDE Build Notes, §2.11 PR06; §2.14). Live QA CHECK `po-010` is recorded as PASS (PF10 — HDE Build Notes, §2.29). The close pack includes `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json` and its hash `endpoints_catalog.json.sha256` (PF10 — HDE Build Notes, §2.31).  
* **Disposition (archive):** Satisfied — doc step `po-010` is PASS and the endpoints catalog artifact is present in the close pack (PF10 — HDE Build Notes, §2.31), though overall readiness remains “Not ready” for unrelated blockers (PF10 — HDE Build Notes, §2.32).

##### **D8 — Close posture: Live QA close \+ close-pack generator**

* **Planned (Implementation Guide):** Deliverable D-008 — “Generate a deterministic close-pack for EPIC026 using `tools/qa/generate_epic026_close_pack.py` (manifest, close report, acceptance map, and supporting evidence pointers).” (r8 epic plan HDE-EPIC026.md, §4.8 Deliverable D-008)  
* **Actual (PF10):** PR08 records the close-pack generator and remediation loops (PF10 — HDE Build Notes, §2.13 PR08). CHECK `po-012` is recorded as PASS (PF10 — HDE Build Notes, §2.31) and produces a close pack copy including `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_manifest.json`, `epic-026_close_report.md`, and `epic-026_acceptance_map.md` (PF10 — HDE Build Notes, §2.31). PF10 also records additional close-pack artifacts in remediation outputs, including `"audit/EPIC-026_MANIFEST.json"` (normalized: `audit/epic-026_manifest.json`) (PF10 — HDE Build Notes, §2.13 Remediation 2 evidence print).  
* **Disposition (archive):** Satisfied for close-pack generation — close-pack artifacts are present and `po-012` is PASS, but overall readiness remains “Not ready” due to the `po-005`/`po-009` blockers cited in the QA Closeout Summary (PF10 — HDE Build Notes, §2.32).

#### **2.11.4 PF Reference Map**

**Primary PF references (Implementation Guide PF map):**

* PF04 — HDE Governance (tokens, rails, acceptance posture) (r8 epic plan HDE-EPIC026.md, §4 PF Reference Map)  
* PF09 — HDE Build Checklist (close pack mapping, baseline artifacts) (r8 epic plan HDE-EPIC026.md, §4 PF Reference Map)  
* PF14 — HDE Mechanics Guide (Conjunction semantics; showcompat surfaces) (r8 epic plan HDE-EPIC026.md, §4 PF Reference Map)  
* PF10 — HDE Build Notes (execution \+ results archive) (r8 epic plan HDE-EPIC026.md, §4 PF Reference Map)

**Execution \+ results sources used for this archive entry:**

* PF10 — HDE Build Notes, §2.5–§2.14 (HDE-EPIC026 PR01–PR08 \+ Docs PR)  
* PF10 — HDE Build Notes, §2.19–§2.32 (HDE-EPIC026 QA step logs \+ QA Closeout Summary)  
* r8 epic plan HDE-EPIC026.md, §2–§9 (planned intent, deliverables, tokens/evidence claims, QA rails, tracked issues, plan preflight)  
* PF27 — Plan Templates, §6.4 Epic Record Template (Normative) (required fields/sections)

#### **2.11.5 Tokens and Evidence (Acceptance)**

**Planned acceptance tokens (in-scope):**

* `JSON_CANONICAL_CHECK_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `COMPOSITE_ABBA_IDENTITY_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `PREIMAGE_RECOMPUTE_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `DETERMINISM_ENV_PINS_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `EVIDENCE_INDEX_UPDATED_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `EVIDENCE_INDEX_MIRROR_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `EVIDENCE_PATHS_VALIDATED_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `CLOSE_PACK_COMPLETE_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `QA_CLOSE_REPORT_GENERATED_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `MANIFEST_GENERATED_OK` (r8 epic plan HDE-EPIC026.md, §5.1)  
* `ACCEPTANCE_MAP_GENERATED_OK` (r8 epic plan HDE-EPIC026.md, §5.1)

**Planned evidence claims (titles-only):**

* “Canonical JSON gate result” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Composite ABBA identity verification” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Determinism environment pin verification” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Evidence index updated entry for EPIC026” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Evidence index mirror updated (if applicable)” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Evidence paths validated” (r8 epic plan HDE-EPIC026.md, §5.2)  
* “Close pack manifest \+ close report \+ acceptance map generated” (r8 epic plan HDE-EPIC026.md, §5.2)

**Actual token claims and evidence pointers (PF10):**

* `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK` are explicitly listed in the PR01 token evidence print (PF10 — HDE Build Notes, §2.5), and Live QA CHECK `po-000` / `po-001` evidence is captured under `audit/qa/hde-epic026/checks/po-001/primary.log` (PF10 — HDE Build Notes, §2.19).  
* Environment pins are evidenced via captured rails/env headers in Live QA logs (e.g., PF10 explicitly cites primary.log headers for CHECK `po-003` including `captured_env` keys SAFE\_MODE / ALLOW\_NETWORK / PYTHONHASHSEED / LANG / LC\_ALL) (PF10 — HDE Build Notes, §2.21; §2.32), but the specific token name `DETERMINISM_ENV_PINS_OK` is **not** explicitly claimed as a token string in PF10.  
  * Disposition for token-name claim: Unknown (not present in inputs).  
* Evidence index \+ close pack artifacts are present in CHECK `po-012` close pack copy, including:  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_manifest.json`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_close_report.md`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_acceptance_map.md`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_evidence_index.json`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json.sha256`  
    (PF10 — HDE Build Notes, §2.31)  
* Additional close-pack artifacts are recorded as outputs in PR08 Remediation 2 evidence print, including `"audit/EPIC-026_MANIFEST.json"` (normalized: `audit/epic-026_manifest.json`) and `"audit/EPIC-026_close_report.md"` (normalized: `audit/epic-026_close_report.md`) (PF10 — HDE Build Notes, §2.13 Remediation 2 evidence print).

**Planned vs actual acceptance mismatch (token-name traceability):**

* PF10’s QA Closeout Summary diagnoses “evidence hygiene \+ plan-to-evidence traceability drift” and does not assert satisfaction of all planned token names as token strings (notably `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and the close-pack token names) even where related artifacts exist (PF10 — HDE Build Notes, §2.32).  
  * Disposition for those token-name claims: Unknown (not present in inputs).

#### **2.11.6 QA Rails — Open/Close (Final PR)**

**Planned QA rails posture (Implementation Guide):**

* Live QA is required for epic close; the plan is recorded as checks `po-000` through `po-012` and requires audited evidence capture under the canonical `audit/qa/...` root. (r8 epic plan HDE-EPIC026.md, §8.1)  
* Rails posture: “Closed rails” should refuse provider acquisition; “open rails” permits provider acquisition where required by the step. (r8 epic plan HDE-EPIC026.md, §6)

**Actual QA execution (PF10 — step log stream):**

* CHECK `po-000` \+ `po-001` — PASS (PF10 — HDE Build Notes, §2.19)  
* CHECK `po-002` — PASS (PF10 — HDE Build Notes, §2.20)  
* CHECK `po-003` \+ `po-004` — PASS; ADR-DEV-01 / ADR-DEV-02 captured as deviations (PF10 — HDE Build Notes, §2.21)  
* CHECK `po-005` — PASS (PF10 — HDE Build Notes, §2.23)  
  * Closeout caveat: treated as “Contaminated (not auditable from PF10)” and cited as a reason overall readiness is “Not ready” (PF10 — HDE Build Notes, §2.32).  
* CHECK `po-006` — PASS (PF10 — HDE Build Notes, §2.24)  
* CHECK `po-007` — PASS (PF10 — HDE Build Notes, §2.25)  
* CHECK `po-008` — PASS (PF10 — HDE Build Notes, §2.26)  
* CHECK `po-009` — recorded with evidence pointers under `audit/qa/hde-epic026/checks/po-009/` (PF10 — HDE Build Notes, §2.28)  
  * Closeout caveat: decision treated as “REMEDIATION DEFERRED DUE TO PLANNING DEFECT,” “not executable as intended,” and cited as a reason overall readiness is “Not ready” (PF10 — HDE Build Notes, §2.32).  
* CHECK `po-010` — PASS (PF10 — HDE Build Notes, §2.29)  
* CHECK `po-011` — PASS (PF10 — HDE Build Notes, §2.30)  
* CHECK `po-012` — PASS; close pack copy created under `audit/qa/hde-epic026/checks/po-012/close_pack_copy/` (PF10 — HDE Build Notes, §2.31)

**Closeout posture (PF10):**

* “Overall readiness (PF10-evidence-grounded): Not ready” because: (1) CHECK `po-005` is “not auditable” from PF10 as recorded, and (2) CHECK `po-009` “is not executable as intended” with remediation deferred due to a planning defect. (PF10 — HDE Build Notes, §2.32)

#### **2.11.7 Tracked Issues**

**Tracked issues (Implementation Guide):**

* TI-001 — “Provider acquisition semantics: enforce local-first; explicit error surfaces when provider missing.” (r8 epic plan HDE-EPIC026.md, §8.2)  
* TI-002 — “Close-pack baseline artifacts need explicit PF09 mapping (step logs, acceptance map, manifest, drift summary, doc deltas).” (r8 epic plan HDE-EPIC026.md, §8.2)  
* TI-003 — “Evidence mirror posture may be optional; decide whether to ship mirror update this pass.” (r8 epic plan HDE-EPIC026.md, §8.2)  
* TI-004 — “Open rails lane: ensure showcompat can exercise provider-acquisition path when explicitly allowed.” (r8 epic plan HDE-EPIC026.md, §8.2)

**Disposition (PF10):**

* TI-001: Unknown (not present in inputs) — PF10 does not reference TI-001 by label.  
* TI-002: Addressed in remediation loop — PR08 Remediation 2 records “ADR status line: ADR-TI002-EPIC026-001” and adds explicit mapping for TI-002 / PF09 baseline artifacts (PF10 — HDE Build Notes, §2.13 Remediation 2; evidence outputs include `"audit/EPIC-026_step_logs_manifest.json"` (normalized: `audit/epic-026_step_logs_manifest.json`)).  
* TI-003: Unknown (not present in inputs) — PF10 does not reference TI-003 by label.  
* TI-004: Not satisfied for closeout — PF10 closeout posture cites CHECK `po-009` as “not executable as intended” and defers remediation due to a planning defect (PF10 — HDE Build Notes, §2.32).

**ADRs / recorded deviations (PF10):**

* ADR-DEV-01 and ADR-DEV-02 recorded in the `po-003`/`po-004` QA block (PF10 — HDE Build Notes, §2.21) as deviations related to QA helper/header and evidence posture.

#### **2.11.8 Plan Preflight (MUST)**

* Planned preflight posture: “No additional preflight gates beyond deliverables above.” (r8 epic plan HDE-EPIC026.md, §9 Plan Preflight)

**A. Token registry validation (names-only):**

* Planned tokens list is explicit (r8 epic plan HDE-EPIC026.md, §5.1).  
* PF10 explicitly claims a subset of planned token names (e.g., PR01 token evidence print lists `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK`) (PF10 — HDE Build Notes, §2.5), but PF10 does not explicitly claim all planned token names as token strings (PF10 — HDE Build Notes, §2.32).  
  * Validation result: Partial (PF10-evidenced subset) / Unknown (not present in inputs) for the remainder.

**B. Close-pack completeness (manifest \+ close report \+ acceptance map):**

* CHECK `po-012` close pack copy contains:  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_manifest.json`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_close_report.md`  
  * `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_acceptance_map.md`  
    (PF10 — HDE Build Notes, §2.31)  
* PF10 also records additional close-pack artifacts under mixed-case naming in PR08 remediation outputs (example: `"audit/EPIC-026_MANIFEST.json"` (normalized: `audit/epic-026_manifest.json`)) (PF10 — HDE Build Notes, §2.13 Remediation 2 evidence print).

**C. Evidence bundle completeness for local-bundle deliverables:**

* Unknown (not present in inputs) — the Implementation Guide does not define local-bundle deliverables for this epic beyond the close pack, and PF10 does not declare an explicit local-bundle completeness gate for EPIC026.

**D. Canonical evidence-path binding validation:**

* Canonical evidence roots and step logs are captured under `audit/qa/hde-epic026/checks/...` for Live QA (e.g., `audit/qa/hde-epic026/checks/po-001/primary.log`, `audit/qa/hde-epic026/checks/po-012/primary.log`) (PF10 — HDE Build Notes, §2.19; §2.31).  
* Closeout caveat: PF10 QA Closeout Summary diagnoses “plan-to-evidence traceability drift,” and treats CHECK `po-005` as contaminated/not auditable and CHECK `po-009` as not executable-as-intended (PF10 — HDE Build Notes, §2.32).

**E. Roll-forward integrity:**

* PF10 closeout posture sets overall readiness to “Not ready” pending resolution of the `po-005` auditability defect and the `po-009` planning-defect remediation deferral (PF10 — HDE Build Notes, §2.32).

### **2.12 HDE-EPIC027 Epic Plan**

#### **2.12.1 Meta**

**Epic ID:** HDE-EPIC027  
**Epic title (Implementation Guide):** Conjunction Pass 3 (`r7 Epic Plan HDE-EPIC027.md`, header)  
**Epic name (short):** Conjunction Pass 3  
**Phase:** Conjunction  
**Status:** Archived  
**Owner:** Unknown (not present in inputs)  
**Priority:** Unknown (not present in inputs)  
**Date started:** 2025.03.11 (operator-provided)  
**Date completed:** 2025.03.19 (operator-provided)  
**Epic outcome (per PF10):** Done

**Epic intent (planned; one paragraph):** This epic is a Conjunction hardening and completion pass. It preserves the existing Reader covenant, keeps A7 proofs bound to the cataloged JSON success route family, keeps writers outside the A7 proof surface family, forbids new token names and public contract surfaces, and finishes the remaining Conjunction work in compat, CLI serializer coupling, reader transport wiring, CLI tooling, writer surfaces, and global evidence discipline. (`r7 Epic Plan HDE-EPIC027.md`, §Business Case; §Contract and Compatibility Posture)

**Scope anchor (plan):** `r7 Epic Plan HDE-EPIC027.md`, §Deliverables (Jobs To Be Done)  
**Stakeholders:** Unknown (not present in inputs)

**PR stream (PF10):** PR-01 cleanup/remediation, PR02, PR03, PR04, Audit Analysis, Implementation Report, ADR Set (PF10 — HDE Build Notes, §2.1–§2.8)  
**QA log stream (PF10):** CHECK `d0_discovery`, `po-001`, `po-002`, `po-003`, `po-004`, `po-005`, `po-006`, `po-007`, `po-008`, `po-009`, `po-010` (PF10 — HDE Build Notes, §2.11–§2.21)

**Date provenance mismatch:** PF10 QA evidence and closeout artifacts repeatedly cite March 2026 timestamps, including `2026-03-19T07:32:00Z` and `2026-03-19T07:32:17Z` in `audit/qa/hde-epic027/checks/po-010/primary.log` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`, while the operator-provided start/close dates are `2025.03.11` and `2025.03.19`. This archive record preserves the operator-provided dates and records the mismatch explicitly.

**Plan-source mismatch:** PF10’s Implementation Report cites `r5 Implementation Plan HDE-EPIC027.md` as the approved execution-shape source, while this archive record uses `r7 Epic Plan HDE-EPIC027.md` as the planned-scope input per task instructions. PF10 remains the source of truth for what happened.

#### **2.12.2 Existing Work Check (MUST)**

**Planned existing-work posture (`r7 Epic Plan HDE-EPIC027.md`, §Existing Work Check (MUST)):**

* PF09 already treated Conjunction as a partially built phase rather than a blank slate, with Dev HTTP Harness and Caching and Transport Wiring (Reader) already complete and other Conjunction rows still partial/not done.  
* Existing canon-aligned reusable slices explicitly identified by the plan:  
  * Dev HTTP Harness already exists as the single dev/QA HTTP harness.  
  * CLI Serializer Coupling already has a mechanics home and canonical shared presenter/emitter rules.  
  * Reader success-route proof posture, Endpoint Catalog posture, and A7 success-route invariants already exist and are reused.  
  * Writer mechanics already exist as a distinct surface family outside the A7 proof family.  
* Existing tokens validated in the plan include: `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`.

**Actual reuse and delta (PF10):**

* PF10’s Implementation Report explicitly states: “The approved execution shape reused already-implemented D1, D3, and D4 scope, and concentrated new work into four PR slices: compat identity-hash and compat indexing, CLI installability/conformance, writer readback/indexing, and EPIC027 acceptance-ledger plus close-pack bindings.” (PF10 — HDE Build Notes, §2.7)  
* PF10 records the following concrete reuse/completion outcomes:  
  * PR-01 supports HDE-CONJ002.3 and HDE-CONJ002.4 moving to Done (PF10 — HDE Build Notes, §2.2).  
  * PR02 supports the impacted CLI/installability subtasks moving to Done (PF10 — HDE Build Notes, §2.3).  
  * PR03 supports HDE-CONJ008.2 and HDE-CONJ008.3 moving to Done and preserves writer/A7 separation (PF10 — HDE Build Notes, §2.4).  
  * PR04 binds 17 canonical tokens in the remedial acceptance map and produces close-pack artifacts at canonical paths (PF10 — HDE Build Notes, §2.5).  
* PF10 Audit Analysis records one remaining canon delta only: “The only concrete canon delta supported by the allowlisted evidence is a PF14 mechanics correction for the dev writer conjunction endpoint method.” It also states: “No PF09 runnable-task delta is required from this audit pass.” (PF10 — HDE Build Notes, §2.6)

#### **2.12.3 Deliverables (Jobs-to-be-done) — Planned vs Actual Reconciliation**

##### **D1 — Dev HTTP Harness completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D1):** Reuse the already-complete non-production harness behavior and close the remaining infra wiring so the dev harness remains the single home for local and QA conjunction validation without becoming a public surface. Includes `HDE-CONJ001.1` and `HDE-CONJ001.4`.  
* **Actual (PF10):** PF10’s Implementation Report states the approved execution shape reused D1 as already-implemented scope rather than landing a new PR slice for it (PF10 — HDE Build Notes, §2.7 “The approved execution shape reused already-implemented D1, D3, and D4 scope”).  
* **Disposition (archive):** Satisfied as reused baseline. New EPIC027-specific D1 evidence pointers are Unknown (not present in inputs).

##### **D2 — Compat Surface hardening**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D2):** Finish the internal compat surface so conjunction compat semantics, canonical bytes, identity-hash capture, and evidence indexing are explicit, deterministic, and closure-ready. Includes `HDE-CONJ002.1`, `HDE-CONJ002.2`, `HDE-CONJ002.3`, `HDE-CONJ002.4`.  
* **Actual (PF10):** PR-01 ended as a compat-only closure slice for `HDE-CONJ002.3` and `HDE-CONJ002.4`, with the final remediation preserving the compat-only branch state, neutralizing bridge artifact churn, and resolving the CI blocker through a targeted checker/test fix. Concrete anchors include:  
  * `ci/checks/check_bridge_consistency.py`  
  * `tests/unit/test_check_bridge_consistency.py`  
  * `artifacts/db_bridge/adapter_selection.snapshot.json`  
  * `artifacts/evidence_index.jsonl`  
    (PF10 — HDE Build Notes, §2.1; §2.2; §2.7)  
* **Disposition (archive):** Satisfied. PF10 explicitly says the reviewed combined evidence supports moving `HDE-CONJ002.3` and `HDE-CONJ002.4` to Done (PF10 — HDE Build Notes, §2.2).

##### **D3 — CLI Serializer Coupling completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D3):** Close the remaining serializer-coupling work so conjunction-related CLI bytes are forced through the shared presenter/emitter path, guarded against ad-hoc serialization, and proven deterministic. Includes `HDE-CONJ003.1`, `HDE-CONJ003.2`, `HDE-CONJ003.3`, `HDE-CONJ003.4`.  
* **Actual (PF10):** PF10’s Implementation Report states D3 was reused as already-implemented scope: “The approved execution shape reused already-implemented D1, D3, and D4 scope.” (PF10 — HDE Build Notes, §2.7)  
* **Disposition (archive):** Satisfied as reused baseline. New EPIC027-specific D3 evidence pointers are Unknown (not present in inputs).

##### **D4 — Reader Surface and Transport Wiring completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D4):** Finish the conjunction-facing Reader success-route work so the Reader body, Endpoint Catalog posture, A7 success-route transport behavior, env-gating, encoding invariance, and transport evidence indexing are complete and canon-aligned. Includes `HDE-CONJ005.1`–`HDE-CONJ005.4` and reuses `HDE-CONJ006.1`–`HDE-CONJ006.3`.  
* **Actual (PF10):** PF10’s Implementation Report states D4 was reused as already-implemented scope (PF10 — HDE Build Notes, §2.7). The QA stream also records PASS for runtime/transport checks:  
  * CHECK `po-005`: “A7 transport test passed” and “the catalog route inventory includes `/reader`” (PF10 — HDE Build Notes, §2.16)  
  * CHECK `po-010`: “Runtime proof requirements are satisfied” and “Governed metadata trust constraints are satisfied in final state” (PF10 — HDE Build Notes, §2.21, content for `po-010`)  
* **Disposition (archive):** Satisfied as reused baseline, with additional PASS runtime proof recorded in the QA stream.

##### **D5 — CLI Conformance and CLI Tooling completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D5):** Complete the operator-facing CLI surface for conjunction by closing installability, entrypoints, showcompat conjunction behavior, sample behavior, conformance, parity, help/argument-policing captures, and tooling evidence indexing. Includes `HDE-CONJ004.1`–`HDE-CONJ004.5` and `HDE-CONJ007.1`–`HDE-CONJ007.4`.  
* **Actual (PF10):** PR02 delivered explicit CLI installability, help/version, argument-policing, deterministic sampler evidence, and governed CLI artifact coherence. Concrete evidence anchors include:  
  * `artifacts/cli/install/entrypoints.txt`  
  * `artifacts/cli/install/installability_summary.json`  
  * `artifacts/cli/summary.json`  
  * PASS QA steps `po-003` and `po-004`  
    (PF10 — HDE Build Notes, §2.3; §2.14; §2.15; §2.7)  
* **Disposition (archive):** Satisfied. PF10 states the reviewed evidence supports moving the impacted PR02 subtasks to Done (PF10 — HDE Build Notes, §2.3).

##### **D6 — Writer Surfaces completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D6):** Finish conjunction writer posture so the writer envelope, idempotent write path, evidence indexing, and explicit A7 exclusion posture are complete without widening the A7 proof surface. Includes `HDE-CONJ008.1`–`HDE-CONJ008.4`.  
* **Actual (PF10):** PR03 delivered writer readback-parity and governed writer evidence while preserving writer/A7 separation. Concrete evidence anchors include:  
  * `artifacts/writer/conjunction_write_readback.log`  
  * `artifacts/writer/conjunction_writer_summary.json`  
  * PASS QA step `po-006`: “this step did not treat writer proof as A7 family proof.”  
    (PF10 — HDE Build Notes, §2.4; §2.17; §2.7)  
* **Disposition (archive):** Satisfied. PF10 states the combined work supports changing `HDE-CONJ008.2` and `HDE-CONJ008.3` to Done (PF10 — HDE Build Notes, §2.4).

##### **D7 — Global discipline completion**

* **Planned (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable D7):** Close the remaining conjunction-wide canonical JSON and Index/Mirror discipline work so all conjunction-touched surfaces participate in the single-emitter, canonical-JSON, same-PR evidence posture. Includes `HDE-CONJ009.1` and `HDE-CONJ009.2`.  
* **Actual (PF10):** PR04 delivered the EPIC027 close-pack slice with canonical acceptance ledgers and same-run QA gate logs. Concrete evidence anchors include:  
  * `docs/acceptance_map_epic027.json`  
  * `audit/qa/hde-epic027/token_evidence_matrix.md`  
  * `audit/qa/hde-epic027/acceptance_map_viability.log`  
  * `audit/EPIC-027_close_report.md`  
  * `audit/EPIC-027_MANIFEST.json`  
  * `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
  * PASS QA steps `po-007`, `po-008`, `po-009`, `po-010`  
    (PF10 — HDE Build Notes, §2.5; §2.18–§2.21; §2.7)  
* **Disposition (archive):** Satisfied as implemented. PF10 states PR04’s remedial acceptance map binds 17 canonical tokens and the close-pack artifacts exist at required canonical paths (PF10 — HDE Build Notes, §2.5). Epic-level closure readiness is still “Not ready” because a PF14 mechanics correction remained open before closure was decided (PF10 — HDE Build Notes, §2.22; §2.8).

**Planned vs actual mismatches (explicit archive notes):**

* **Plan source mismatch:** PF10 Implementation Report cites `r5 Implementation Plan HDE-EPIC027.md` as the approved execution-shape source, while this archive entry uses `r7 Epic Plan HDE-EPIC027.md` as the planned-scope input by task instruction.  
* **Outcome mismatch:** PF10 records all QA steps `d0_discovery` and `po-001` through `po-010` as PASS, but the final closeout posture remains “Overall readiness: Not ready” because PF10’s ADR set requires the PF14 dev-writer conjunction endpoint correction to drain before closure is decided.  
* **QA log mismatch:** PF10 section `2.21) QA Pass - HDE-EPIC027 - CHECK po-009` contains content for `CHECK po-010: PO-010`. The heading and the check content do not match.  
* **Scope mismatch:** The plan treated D1, D3, and D4 as reused baseline, but PF10’s implementation narrative is centered on PR-01 through PR-04 and does not restate a separate closure artifact for the reuse boundary beyond the Implementation Report summary.  
* **Docs sweep mismatch:** `r7 Epic Plan HDE-EPIC027.md` does not define a standalone docs-sweep deliverable, and PF10 does not provide a distinct EPIC027 Docs PR section.

#### **2.12.4 PF Reference Map**

**Core PF references (from `r7 Epic Plan HDE-EPIC027.md`, §PF Reference Map):**

* PF21 — 7 Phases of Alchemical Engineering, §4. Conjunction  
* PF10 — HDE Build Notes  
* PF27 — Canon Plan Templates  
* PF09 — Canon-HDE-Build-Checklist  
* PF14 — Canon-HDE-Mechanics-Guide  
* PF23 — Canon-Reality-Audits  
* PF02 — Canon-HDE-Architecture  
* PF04 — Canon-HDE-Governance  
* PF05 — Canon-HDE-CLI-API-Vendor-Ref  
* PF12 — Canon-HDE-Schemas-and-Artifacts  
* PF19 — Canon-Glow-QA-Guide  
* PF06 — Canon-Epic-Process-Guide

**Execution and results sources used for this archive entry:**

* PF10 — HDE Build Notes, §2.1) Remediation Plan PR-01 \- HDE-EPIC027  
* PF10 — HDE Build Notes, §2.2) PR-01 Cleanup HDE-EPIC027  
* PF10 — HDE Build Notes, §2.3) PR02 HDE-EPIC027  
* PF10 — HDE Build Notes, §2.4) PR03 HDE-EPIC027  
* PF10 — HDE Build Notes, §2.5) PR04 HDE-EPIC027  
* PF10 — HDE Build Notes, §2.6) Audit Analysis HDE-EPIC027  
* PF10 — HDE Build Notes, §2.7) HDE-EPIC027 Implementation Report  
* PF10 — HDE Build Notes, §2.8) HDE-EPIC027 ADR Set  
* PF10 — HDE Build Notes, §2.11) QA Pass \- HDE-EPIC027 \- CHECK d0\_discovery: d0 through §2.21) QA Pass \- HDE-EPIC027 \- CHECK po-009  
* PF10 — HDE Build Notes, §2.22) HDE-EPIC027 Final QA Closeout Review \+ QA RCA  
* `r7 Epic Plan HDE-EPIC027.md`, §Existing Work Check (MUST), §Deliverables (Jobs To Be Done), §Tokens and Evidence (Acceptance), §QA Rails — Open/Close (Final PR), §Tracked Issues, §Plan Preflight (MUST)  
* PF27 — Canon Plan Templates, §Epic Record Template (Normative)

#### **2.12.5 Tokens and Evidence (Acceptance)**

**Planned token inventory (`r7 Epic Plan HDE-EPIC027.md`, §Token Inventory):**

* Baseline close tokens: `TESTS_PASS_OK`, `DOC_DELTA_PRESENT_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`  
* Additional in-scope token families:  
  * Compat / global discipline: `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`  
  * CLI parity: `CLI_READER_PARITY_OK`  
  * Reader/A7 transport: `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`  
  * Global discipline: `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`  
  * Rails: `ENV_RAILS_POLICY_OK`

**Planned evidence families (`r7 Epic Plan HDE-EPIC027.md`, §Deliverable-level in-scope token posture):**

* Dev harness posture and infra-wiring family  
* Compat contract, canonical-compat, and compat identity family  
* CLI shared presenter and emitter parity family  
* CLI help, installability, argument-policing, and command-conformance family  
* Reader success-route and Endpoint Catalog family  
* A7 success-route and encoding-invariance family  
* Writer envelope, idempotence, and write and readback parity family  
* Human Evidence Index and Machine Mirror coherence family  
* Canonical JSON gate and same-PR proof-anchor refresh family

**Actual token/evidence posture (PF10):**

* **Explicit token claims in PR-01:** `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`, `COMPOSITE_ABBA_IDENTITY_OK` (PF10 — HDE Build Notes, §2.5 PR-01 token evidence print as summarized in §2.7).  
* **Explicit close-pack ledger claim in PR-04:** “The Remedial PR acceptance map now binds 17 canonical tokens” and “The Remedial PR token matrix now mirrors that expanded ledger.” Exact 17-token list is Unknown (not present in inputs). (PF10 — HDE Build Notes, §2.5; §2.22)  
* **Concrete evidence pointers recorded in PF10:**  
  * `docs/acceptance_map_epic027.json`  
  * `audit/qa/hde-epic027/token_evidence_matrix.md`  
  * `audit/qa/hde-epic027/acceptance_map_viability.log`  
  * `audit/EPIC-027_close_report.md`  
  * `audit/EPIC-027_MANIFEST.json`  
  * `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`  
  * `artifacts/evidence_index.jsonl`  
  * `docs/evidence/INDEX.json`  
  * `artifacts/compat/identity_hash.txt`  
  * `artifacts/cli/install/entrypoints.txt`  
  * `artifacts/cli/install/installability_summary.json`  
  * `artifacts/cli/summary.json`  
  * `artifacts/writer/conjunction_write_readback.log`  
  * `artifacts/writer/conjunction_writer_summary.json`  
  * `audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt`  
  * `audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt`  
* **Token-name mismatch note:** PF10 does not enumerate the full planned token roster verbatim. The archive record preserves the r7 planned token inventory and separately records PF10’s narrower explicit token claims and the 17-token-close-pack statement.

#### **2.12.6 QA Rails — Open/Close (Final PR)**

**Planned rails posture (`r7 Epic Plan HDE-EPIC027.md`, §QA Rails — Open/Close (Final PR)):**

* Final-PR rails posture is closed by default for acceptance-relevant proof runs.  
* Any opened-rails exception is titles-only posture, not a runbook.  
* Live QA is required at epic close under PF06 and PF19.  
* The epic plan explicitly does not embed a Live QA runbook, step list, command sequence, QA root layout, or evidence directory design.

**Actual QA event stream (PF10 — HDE Build Notes, §2.11–§2.21):**

* CHECK `d0_discovery` — PASS; “The step’s governed `primary.log` now satisfies the PF-Canon trust constraint.” Evidence pointer: `audit/qa/hde-epic027/checks/d0_discovery/primary.log`  
* CHECK `po-001` — PASS; “4 passed in 2.40s.” Evidence pointer: `audit/qa/hde-epic027/checks/po-001/primary.log`  
* CHECK `po-002` — PASS; “identity-proof discoverability is explicit in the updater or mirror output.” Evidence pointer: `audit/qa/hde-epic027/checks/po-002/primary.log`  
* CHECK `po-003` — PASS; parity test \+ help behavior recorded. Evidence pointer: `audit/qa/hde-epic027/checks/po-003/primary.log`  
* CHECK `po-004` — PASS; “bg:resolve \--help returned usage text with rc=0.” Evidence pointer: `audit/qa/hde-epic027/checks/po-004/primary.log`  
* CHECK `po-005` — PASS; “A7 transport test passed.” Evidence pointer: `audit/qa/hde-epic027/checks/po-005/primary.log`  
* CHECK `po-006` — PASS; “this step did not treat writer proof as A7 family proof.” Evidence pointer: `audit/qa/hde-epic027/checks/po-006/primary.log`  
* CHECK `po-007` — PASS; “all evidence-discipline jobs passed” and “EPIC027 manifest coverage is present in required mapping loci.” Evidence pointers: `audit/qa/hde-epic027/checks/po-007/primary.log`, `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
* CHECK `po-008` — PASS; “the close-pack generator ran” and “the EPIC027 qa-step manifest is ledger-bound.” Evidence pointer: `audit/qa/hde-epic027/checks/po-008/primary.log`  
* CHECK `po-009` — PASS; “no unexpected public success surface appears in the catalog inventory” and “no non-canonical token names are introduced in the token inventory.” Evidence pointer: `audit/qa/hde-epic027/checks/po-009/primary.log`  
* CHECK `po-010` — PASS; “Runtime proof requirements are satisfied” and “Governed metadata trust constraints are satisfied in final state.” Evidence pointers:  
  * `audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt`  
  * `audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt`  
  * `audit/qa/hde-epic027/checks/po-010/primary.log`

**QA stream mismatch archived explicitly:**

* PF10 heading mismatch: section `2.21) QA Pass - HDE-EPIC027 - CHECK po-009` contains content for `CHECK po-010: PO-010`.  
* PF10 closeout posture mismatch: step-level PASS is strong across `d0_discovery` and `po-001` through `po-010`, but the final QA Closeout Summary still states “Overall readiness: Not ready” because closure remained blocked on the PF14 dev-writer conjunction endpoint mechanics correction (PF10 — HDE Build Notes, §2.22; §2.8).

#### **2.12.7 Tracked Issues**

**Tracked issues at plan creation (`r7 Epic Plan HDE-EPIC027.md`, §Tracked Issues):**

* “Tracked Issues: None at plan creation.”  
* Planning-time rule: if a reality ambiguity, canon contradiction, or unproven repo locus appears during planning or execution, it must be recorded and disposed as Completed, Carried forward, Promoted, or Explicitly dropped.

**Actual tracked issues / ADRs recorded in PF10:**

* **ADR-027-CLOSE-01 — PF14 dev writer conjunction endpoint correction timing**  
  * Decision: “Drain the PF14 correction before closure is decided.”  
  * Why it matters: PF10 classifies this as the only concrete remaining canon delta after EPIC027.  
  * Evidence anchor: PF10 — HDE Build Notes, §2.8  
* **ADR-027-CLOSE-02 — PF09 EPIC027 completion-row timing**  
  * Decision: Update PF09 rows now; do not hold PF09 status moves hostage to the PF14 doc drain.  
  * Supported rows: `HDE-CONJ002.3`, `HDE-CONJ002.4`, `HDE-CONJ008.2`, `HDE-CONJ008.3`, `HDE-CONJ009.2`  
  * Evidence anchor: PF10 — HDE Build Notes, §2.8  
* **ADR-027-CLOSE-03 — PF10 audit conclusion on PF09 runnable-task delta**  
  * Decision: Accept that no new PF09 runnable-task delta is required.  
  * Evidence anchor: PF10 — HDE Build Notes, §2.8  
* **ADR-027-CLOSE-04 — Status of observational drift themes**  
  * Decision: Treat dual `create_app` loci, evidence-root classification/root proliferation, and determinism-versus-I/O seam placement as closed observations unless they re-trigger.  
  * Evidence anchor: PF10 — HDE Build Notes, §2.8

**Implementation-vs-closeout mismatch archived explicitly:**

* PF10 Implementation Report states the remaining issue is only a PF14 mechanics correction and no new PF09 runnable-task delta is required (PF10 — HDE Build Notes, §2.6; §2.7).  
* PF10 QA Closeout Summary still marks “Overall readiness: Not ready” because ADR-027-CLOSE-01 requires the PF14 correction before closure is decided (PF10 — HDE Build Notes, §2.22; §2.8).

#### **2.12.8 Plan Preflight (MUST)**

**Planned preflight posture (`r7 Epic Plan HDE-EPIC027.md`, §Plan Preflight (MUST)):**

* PF23 consult completed for planning traceability.  
* Acceptance token names must remain canonical; no local aliases or newly minted token names in the plan.  
* Close-pack baseline for epic close is declared by title only: epic close report, epic manifest, epic acceptance map, token-to-evidence matrix when required.  
* The plan remains Epic Planning only and does not embed QA runbooks, step sequences, commands, or evidence directory design.

**Actual archive-level reconciliation:**

* **Existing Work Check:** present in the plan and corroborated by PF10’s Implementation Report reuse statement for D1, D3, and D4 (PF10 — HDE Build Notes, §2.7).  
* **Canonical token naming:** PF10 step `po-009` records “no non-canonical token names are introduced in the token inventory.” Evidence pointer: `audit/qa/hde-epic027/checks/po-009/primary.log` (PF10 — HDE Build Notes, §2.20).  
* **Close-pack baseline:** present in actual evidence:  
  * `docs/acceptance_map_epic027.json`  
  * `audit/qa/hde-epic027/token_evidence_matrix.md`  
  * `audit/qa/hde-epic027/acceptance_map_viability.log`  
  * `audit/EPIC-027_close_report.md`  
  * `audit/EPIC-027_MANIFEST.json`  
    (PF10 — HDE Build Notes, §2.5; §2.18–§2.19)  
* **QA runbook exclusion:** preserved. PF10 Implementation Report restates that the epic “forbids new token names, new public contract surfaces, and embedded Live QA runbooks.” (PF10 — HDE Build Notes, §2.7)

**Archive mismatch note:** The planned preflight posture is satisfied at the plan/structure level, but final close readiness was still blocked by a non-runnable canon delta (PF14 dev writer conjunction endpoint method correction) per ADR-027-CLOSE-01.

