---
artifact_type: SPECIFICATION_KICKOFF
artifact_version: "1.0"
logical_id: HDE-EPIC041-SPECIFICATION-KICKOFF
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
producer: Master Scrum (Master Scrum 02C; https://claude.ai/code/session_01Q789tzPQvQrVkpkVk2LWhC)
prompt: CF-E-10 — Prepare Epic Specification Kickoff Handoff — 102726.1 (https://app.notion.com/p/4064590a05eb81a0a3a8e043017dffbb; page state 2026-10-27T13:22:24.392Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
state: KICKOFF_READY
prepared_at: 2026-10-28T02:50:00Z
repository_head_read: origin/main 8d56b19 (includes #779)
class_selection_ref: docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md
source_ref: docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md
pf09_phase: Separation (Phase III)
pf09_planned_work: HDE-SEPA006; HDE-SEPA006.1; HDE-SEPA006.2; HDE-SEPA006.3
next_prompt: CF-E-20
next_actor: Isis
---

# HDE-EPIC041 — Epic Specification kickoff

This kickoff is transient scaffolding. It is not a Specification, an approval, an Implementation Audit or Plan, a QA plan or a PF10 artifact, and it grants no authority (HDE Governance §9.1.1: "Class-specific kickoff … no Specification, IP, work-unit structure or mutation authorization"). Isis resolves the Specification format from canon (Plan Templates, "Epic Record Template (Normative)") and does not take it from this file.

## 1. Result

| Field | Value |
| :- | :- |
| State | `KICKOFF_READY`. No blocker. Isis can author a pending Epic Specification from this artifact alone |
| Change | `HDE-EPIC041`, "Separation Pass 4", `CHANGE_CLASS: EPIC` |
| Selection | `CLASS_SELECTED` by Nathan / Product Owner, recorded by CF-PO-10 (§2) |
| Planned work | Task HDE-SEPA006, "Non-BodyGraph chart-loader boundary correction", with Subtasks HDE-SEPA006.1, .2 and .3, all `Not done` in the source (§3) |
| Open items | Four, none blocking Specification formation (§9). One is a Product Owner decision Isis must not invent: the disposition of the legacy chart-loader defect |
| Review chain | Isis authors; the same continuing Thoth session reviews (HDE Governance §9.1.1) |

## 2. Lineage

| Item | Value |
| :- | :- |
| Selection record | `docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md`: `CLASS_SELECTED`, class `EPIC`, mode `EVIDENCED_SELECTION_RECORDING_OR_RECOVERY`, route CF-E-10. Merged to `main` by `amthorn78/glow-hdengine-v2#779` as `8d56b19`; read in full |
| Product Owner evidence | Verbatim in the selection record §2: "Yes, run CF-PO-10 with PF09.3. This will be HDE-EPIC041, Separation pass 4" (2026-10-28) |
| Source | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`, v1.1.8, status Canon, effective 2026-10-26. Git blob `8b2dbf49081ea53690efa9b8eb7d8d493e8614e9`, 89,754 bytes, equal to the blob and size the selection record cites. Read: §0.1 to §0.6 in full; the Phase III header and notes; Task HDE-SEPA006 and its three Subtasks in full (line 1280 to the section end at line 1379); the status line of all 39 units |
| Working tree | `main` at `8d56b19`. The clone is shallow: commits `6c6f4b2a` and `5ef911fec556a6c24bda8196b085f43c2da02150` cannot be resolved locally (§8, U-1) |
| Selection-record correction | The selection record's "Canon relied on" says PF10 v13.8.9 has "No current addenda". On `main` at its own read head, the current PF10 was already v13.9 (`dfa047c`, 2026-10-27, an ancestor of `de27c35`), and it carries one addendum (§6). The record is an issued version and is not edited. This kickoff supersedes that one reading. The correction does not change the class, the identity or the mapping |

## 3. PF09 planned-work mapping (preserve exactly)

Epic formation "preserves the exact phase, eligible inventory, identifiers, and source statuses" (PF09.3 §0.4, "Epic and CRD boundary"). Verified by a script reading every unit heading and its status line:

- Phase III, Separation. Phase master status: **Not Done**. 39 task and subtask units: 35 **Done**, 4 **Not done**.
- **In the Epic's inventory (4, all Not done):**

| Unit | Title | Source status |
| :- | :- | :- |
| Task HDE-SEPA006 | Non-BodyGraph chart-loader boundary correction | Not done |
| Subtask HDE-SEPA006.1 | Adapter-owned acquisition and pure Engine normalization | Not done |
| Subtask HDE-SEPA006.2 | Supported caller migration | Not done |
| Subtask HDE-SEPA006.3 | Boundary and behavior verification | Not done |

- **Context, not scope (35 Done):** HDE-SEPA001 to HDE-SEPA005 and all their subtasks. HDE-SEPA005 and its five subtasks are Done. Their statuses are preserved unchanged.
- **Source row fields for Task HDE-SEPA006:**
  - Phase placement: Separation; "a sibling of HDE-SEPA005, not part of the Magic10 mechanics-configuration task".
  - Priority: "Required-Now architecture correction". "This priority does not select a release, implementation date, or development unit."
  - Epic or card: "Not selected. This is separate planned product work, not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope."
  - Owner / execution lane: Implementation Agent (IA) for implementation planning and delivery coordination; the dedicated PR implementation lane delivers the authorized code, tooling, tests and evidence. The Product Owner is the task's decision owner, including for the legacy chart-loader defect. "No individual session is assigned by this row."
  - Subtasks .1 to .3 own: the Task's IA and dedicated PR implementation lane; for .3, "independent QA and acceptance retain their applicable owners".
- No PF09 status moves. Nothing in this Epic's Specification, its approval or its closure moves a PF09 row; a PF09 update needs its own authorization (PF09.3 §0.4, §0.6).

## 4. Problem and capability (source-supported)

**Problem, source-stated.** The non-BodyGraph chart loader mixes chart acquisition orchestration with chart computation. HDE Architecture §1.1 ("Non-BodyGraph chart loader classification [Required-Now]") classifies the loader as "implementation drift, not a sanctioned Engine I/O seam". It places environment and rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging and filesystem writes in Adapter-owned orchestration. It lets pure validation and normalization stay under Engine ownership "only as explicit data-in/data-out computation". It states that "The checked-in loader remains current repository reality until separately remediated; this classification does not claim that relocation, caller migration, or removal has occurred."

**Capability, source-stated (Task description).** "Separate chart-acquisition orchestration from deterministic Engine chart computation. Establish the supported Adapter-owned orchestration entrypoint, retain only pure validation/normalization under Engine ownership, migrate supported active callers, and retire the mixed operational boundary."

**Corroborating context (not authority).** HDE State of the Repository §2.2 (a 2026-09-15 snapshot assessment) describes the same gap, adds that the loader has fixture-style returns including Gates `[1, 2, 3]` and a legacy fallback when the provider resolver is unavailable, and says "An import-path rename alone would not resolve it." Both statements are confirmed at `main` (§7, V-5).

## 5. Outcomes, in-scope requirements, exclusions, constraints, dependencies

### 5.1 In-scope outcomes and requirements (source-stated; one block per planned-work unit)

**HDE-SEPA006 (Task).** Deliverables and required evidence: implementation diff; supported runtime/tooling/test caller inventory with each caller's disposition; explicit input/output and side-effect boundary evidence; focused boundary, failure and caller-regression results; actual tested-source attribution; governed evidence indexed through the existing authorized writer. These are "required future deliverables, not artifacts asserted to exist". Implementation / integration boundary: Adapter-owned orchestration owns environment and SAFE_MODE/rails evaluation, provider selection, chart acquisition, wall and performance clocks, correlation context, operational logging and filesystem writes. Vendor or database acquisition uses the sanctioned BodyGraph resolver/ingest boundary. Engine chart validation and normalization consume explicit inputs and return pure data, with no operational or import-time side effects.

**HDE-SEPA006.1 — Adapter-owned acquisition and pure Engine normalization.**
- Move environment and rails evaluation, provider selection, acquisition, clocks, correlation context, operational logging and filesystem writes into Adapter-owned orchestration.
- Use the sanctioned BodyGraph resolver/ingest boundary for vendor and DB acquisition.
- Retain Engine validation and normalization only as explicit data-in/data-out computation, without time, randomness, environment, network, provider, logging or filesystem side effects.
- Establish explicit inputs, outputs, failure behavior and orchestration ownership for HDE-SEPA006.2. Preserve applicable CLI/API/Vendor and Mechanics behavior. No fallback data and no additional Engine I/O carve-out.
- Evidence: actual implementation diff and explicit interface/side-effect account, supported by focused positive and negative automated boundary checks. "Exact implementation paths and commands belong to the authorized plan."

**HDE-SEPA006.2 — Supported caller migration.**
- Identify actual supported runtime, tooling and test callers at implementation time and migrate each to the correct orchestration or pure-computation interface. Include "the active compatibility-determinism artifact generator and relevant loader/provider tests".
- Remove the old operational Engine path, "or retain only a genuinely pure compatibility surface if its owning contract permits it". A retained compatibility surface needs both an owning-contract basis and evidence of actual purity.
- Preserve governed caller output and failure behavior; keep historical audit captures unchanged; "Do not treat an import-path rename as complete migration."
- Evidence: supported-caller inventory with exact source attribution and a disposition for every member; migration/retirement diff; focused runtime, tooling and loader/provider caller-regression results.
- Note carried from the source: the retirement of the legacy-signature test by HDE-CRD-0002 "is not caller migration: it neither migrates nor removes the legacy signature, and the loader defect … remains unfixed."

**HDE-SEPA006.3 — Boundary and behavior verification.**
- Implement meaningful automated checks proving Engine chart computation uses explicit inputs and does not read environment, clocks, randomness, providers, network, logs or filesystem state; check that import introduces no operational side effects.
- Exercise applicable orchestration rails, correlation context, keys-only logging and failure behavior using controlled fixtures. Verify the complete supported-caller migration and preservation of governed outputs.
- Reconcile .1 and .2, including any permitted pure compatibility surface.
- Evidence: boundary and caller-regression results; controlled positive/negative and side-effect checks; actual commands, configuration, tested-source identity, results, responsible actor, time and limitations; indexing through the existing governed writer. "A moved filename, successful import, static source observation, or another change's accepted QA does not establish this task's boundary, behavior, or completion."

### 5.2 Exclusions and non-goals (source-stated)

- No scoring algorithm, full Magic10 delivery, new provider contract, fallback data, broader Engine I/O exemption, production operation or provenance helper (Task notes).
- No live vendor or production database activity unless separately authorized (Task dependencies; Subtask .3). The row "does not authorize implementation".
- Not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope. Their CLOSE / CHANGE_CLOSED decisions and accepted evidence are "not acceptance of this separate migration".
- No implementation, QA or completion of any part is claimed for the task (Task notes).
- Dissolution's Engine Core work, HDE-SEPA005.3's immutable typed mechanics-configuration loader, HDE-CONJ010.4's Core-backed compatibility integration, and the existing BodyGraph/vendor/DB obligations "neither complete this migration nor become a second home for it" and stay intact.
- Not a PF20 or PF30 entry and not a PF30 gate: "Do not collapse Epic identity into CRD identity or use PF30 as an Epic gate" (CF-E-10 step 2).

### 5.3 Constraints (canon-stated; Isis applies them to the Specification)

- Purity rule (HDE Architecture §1.1): deterministic compute is pure: no time, network, file I/O, randomness or environment reads at compute time; no import-time side effects. The BodyGraph seam carve-out "does not relax purity" for Engine Core, sampler core or other deterministic compute modules.
- A Specification stays at scope-and-outcome level. It must not prescribe atomic tasks, file edits, commands, planned PR or Ops work units, detailed PR plans, approval objects or receipts. It preserves the Epic's phase and exact PF09 inventory (HDE Governance §9.1.1).
- A Specification must not reference a file path as required unless canon defines it, an audit proves it, or QA creates it, and an asserted implementation locus needs a validation label (Change Process Guide, "Plan path provenance" and "Plan locus validation labels"). The paths in §7 are Master Scrum's read-only observations, offered as discovery context for the Implementation Audit. They are not required paths and not source-stated scope.
- A Specification references canon by title only (Change Process Guide). This kickoff uses file names for traceability only.
- Business case per requirement (Plan Templates, Epic Record Template): see §10.

### 5.4 Dependencies and sequencing (source-stated)

- Preserve HDE Architecture §1.1's pure-compute rule and sanctioned BodyGraph resolver/ingest boundary, with the applicable HDE CLI/API/Vendor Reference and HDE Mechanics Guide contracts.
- Establish the explicit orchestration and pure-computation interfaces in .1 before completing caller migration in .2. Develop verification with both; .3 reconciles the final boundary and caller set.
- Resolve actual callers, concrete paths, commands, dependencies and delivery work units during authorized implementation planning.

## 6. Canon searched and relied on

Canon was resolved from `docs/pfcanon/` on `main` (`8d56b19`), PF09.3 re-read in full for the sections above. Terms searched: chart.loader, engine/charts, SEPA006, orchestrat, pure-compute, Epic kickoff, Epic Specification, Epic Record Template, Adapter, vendor_http, http_reader.

| Document (title) | Sections relied on |
| :- | :- |
| HDE Build Checklist — Separation (v1.1.8) | §0.1 to §0.6; Phase III header and notes; Task HDE-SEPA006 and .1 to .3; every unit's status |
| HDE Architecture | §1.1 "Single homes", including "Non-BodyGraph chart loader classification [Required-Now]" and the role-boundaries paragraph |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" (kickoff role, Specification boundary, review chain, historical drainage) |
| Change Process Guide | Specification format authority; "Plan path provenance"; "Plan locus validation labels"; "Audit provenance in planning artifacts" |
| Plan Templates | §2 HDE-EPIC-Specification, "Epic Record Template (Normative)": Meta, Business Case, Contract and Compatibility Posture, Existing Work Check, Deliverables, PF Reference Map, Exact-Source Evidence and Acceptance, QA Rails, Tracked Issues, Specification Preflight; and the statement that a kickoff is transient scaffolding |
| HDE State of the Repository | §2.2 (corroborating context only) |
| HDE Build Notes (PF10, current v13.9) | Precedence and silence rules; the whole of addendum 2.1. See below |
| AGENTS.md (repository instruction file) | Canon-first rule; closed-rails defaults; PF canon read-only |

**PF10 reading (current v13.9, one addendum).** Addendum 2.1, "Canon policy for the S19 routed security findings: production vendor gate scope, vendor route selection, compat route gating, evidence-tool output roots and gate-row content", decides D-1 to D-5. Its scope is the production vendor override on `hdctl showcompat`/conjunction acquisition, vendor route selection, `POST /api/compat/v1` gating, attestation-builder output roots and governed gate-row content. A search of PF10 v13.9 for the loader, `engine/charts`, `get_chart`, the Adapter/Engine chart boundary and HDE-SEPA006 finds nothing. Under PF10's silence rule, PF10 is silent on this Epic's topic and permanent canon governs. The addendum is adjacent, not overlapping: its decisions are the prerequisite for Candidate CRD Items List item 9, a separate change that touches code near this Epic (§9, O-2).

**Source reference not resolvable in current PF10.** PF09.3 and the HDE-CRD-0002 close report cite "HDE Build Notes" (addendum 2.2 of the earlier v13.8.8) as the record of the loader defect. That addendum is not in v13.9 (`44dba78` started v13.8.9 and removed v13.8.8). The defect is nonetheless fully stated in PF09.3's Task HDE-SEPA006 notes, so no gap results.

## 7. Verified facts (read-only checks by Master Scrum, `main` at `8d56b19`)

All checks are static reads or `git` queries. No test, script or provider call was run, and nothing in the repository was changed.

| ID | Fact | Method and result |
| :- | :- | :- |
| V-1 | Selection record is on `main`, state `CLASS_SELECTED`, class `EPIC`, next prompt CF-E-10 | `git log` shows `8d56b19 … (#779)`; file read in full |
| V-2 | PF09.3 is the version and bytes the selection record cites | `git hash-object` = `8b2dbf49…8614e9`; `wc -c` = 89,754 |
| V-3 | 39 units; 35 Done; 4 Not done; phase master Not Done | Script over unit headings and status lines. One status line (HDE-SEPA002.6) uses italic markup, `*Subtask status:* **Done**`; counted Done |
| V-4 | `HDE-EPIC041` is not an existing real Epic identity | `git grep` on `main`: occurrences only in `tests/qa/test_generate_epic_close_pack.py` fixtures and one HDE-CRD-0002 QA preflight log; no record, card or PF09 row. PF20 has Epic records to HDE-EPIC040 |
| V-5 | The loader file matches the canon description | `engine/charts/loader.py` (173 lines) reads `SAFE_MODE` from the environment; reads wall and performance clocks; calls `resolve_provider` in a legacy signature path; returns a fixture dict with Gates `[1, 2, 3]` on the new-signature path; returns `{"gates": [1, 2, 3]}` if `resolve_provider` could not be imported; computes a correlation id; and appends a keys-only JSON line to `artifacts/logs/loader_call.jsonl`, relative to the working directory, creating the directory |
| V-6 | The legacy-signature defect is present as the source states | `engine/charts/loader.py:81` calls `provider.get_chart(...)`. `engine/config/provider_loader.py` imports `FixturesProvider` from `engine.provider.fixtures` (line 14) and constructs it for the `fixtures` provider (line 274). `engine/provider/fixtures.py`'s `FixturesProvider` defines `get_pair_profile` and no `get_chart`. A different `FixturesProvider` in `engine/providers/fixtures_provider.py` does define `get_chart` but is not the class `provider_loader` imports. Static reading only; the call was not executed, so an `AttributeError` at runtime is consistent with, not demonstrated by, this check |
| V-7 | The retired test is retired and recorded | `tests/retired_tests.md` row for `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` states the defect, dates it to `6c6f4b2a` (2025-09-28), and says only tests call the signature, the loader is not a release member and is not reached at runtime. The file is absent from `tests/loader/` on `main` (a copy remains under `.audit_src/`) |
| V-8 | HDE-CRD-0002 deferred the defect to the Product Owner | `audit/HDE-CRD-0002_close_report.md` line 133: `HDE-SEPA006`, ADR status Deferred to the Product Owner as decision owner |
| V-9 | The tracked log the loader writes exists | `artifacts/logs/loader_call.jsonl` is tracked, 12,536 bytes |
| V-10 | Candidate callers and references at `main` (static `git grep`, not an exhaustive or authoritative inventory) | Importers of the loader: `scripts/make_compat_determinism_artifacts.py` (calls the new signature with keyword arguments; this is the "active compatibility-determinism artifact generator"; it writes `artifacts/compat/`); `tests/loader/test_load_chart_fixture_only.py`; `tests/loader/test_loader_logs_keys_only.py`. Path references only: `pytest.ini` line 72 and `ci/checks/classify_ci_changes.py` line 112 (both name `tests/loader/test_load_chart_fixture_only.py`); `tests/retired_tests.md`. No importer was found under `engine/` or `adapter/`. `adapter/http_reader.py::_safe_load_chart` is an unrelated path-reading helper with a similar name. A tracked `.audit_src/` tree and several historical capture trees contain copies of the loader and its tests |
| V-11 | The retained coverage the source names exists | `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` are both defined on `main`. Whether they pass was not run (see U-3) |

## 8. Source-stated claims, assumptions and unknowns

**Source-stated, carried without independent verification.**
- S-1. The defect dates to commit `6c6f4b2a` (2025-09-28) and HDE Architecture's classification is made "at repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`". The local clone is shallow, so neither commit resolves here (U-1).
- S-2. HDE-EPIC040 is closed (`CLOSE` / `CHANGE_CLOSED`, 2026-09-29) and the prior-Epic gate in HDE Governance §1.1 is met; the Development Board's only non-`DONE` Epic card is HDE-EPIC019, a stale row for an Epic PF20 records as Done. From the selection record §4; not re-read here.
- S-3. The latest `ci` push run on `main` is the OBS-17 failure at `1fb4731b` (run 40359063642); later commits on `main` are documentation-only; the owner is the Product Owner (Candidate CRD Items List item 10). From the selection record §5; not re-verified here.
- S-4. Candidate CRD Items List items 9 and 10 are open and owned by no change. Item 9 is the S19 findings change (PF10 addendum 2.1 confirms: state Open, review status New). Item 10(b) FND-022 and item 9's X-03 and R01 touch code near this Epic. From the selection record §5 and PF10 addendum 2.1. The list itself was not read.
- S-5. The Product Owner's earlier question and Master Scrum's answer: the Epic may begin first; deciding items 9 and 10 before the Implementation Audit is advised. This is Master Scrum's judgement in the selection session, "not a canon rule" (selection record §2).

**Assumptions made by this kickoff:** none that the Specification depends on.

**Unknowns (preserved; none blocks Specification formation).**
- U-1. Whether `6c6f4b2a` and `5ef911fe` match the dates and state the canon and the retired-test ledger assert. Owner: Implementation Audit.
- U-2. The complete supported-caller set, including dynamic imports, scripts outside the paths searched, documentation-referenced commands and CI selection lists. V-10 is a starting observation only. Owner: IA (HDE-SEPA006.2 states callers are resolved "at implementation time").
- U-3. Whether the retained-coverage tests named in the source pass (their definitions exist, V-11). Owner: IA.
- U-4. Which owning contract, if any, permits a retained pure compatibility surface (HDE-SEPA006.2). Owner: IA, with the Product Owner where it is a product choice.
- U-5. Whether any public or CLI surface reaches the loader. V-10 found none under `engine/` or `adapter/`, and the source says it "is not reached at runtime", but the source does not state a public-surface posture. Owner: IA. Isis states the Contract and Compatibility Posture from the source's own preservation language (§5.2) and does not assert "no public change" as a finding.

## 9. Open items and decisions

| ID | Item | Owner | Effect on the Specification |
| :- | :- | :- | :- |
| O-1 | **Disposition of the legacy chart-loader defect.** The source makes the Product Owner "this task's decision owner, including for the legacy chart-loader defect", and the HDE-CRD-0002 close report deferred it to him. No decision is recorded on repair, retirement or retention of the legacy signature. | Product Owner (Nathan) | The Epic's scope already covers it: the task "retires the mixed operational boundary", the phase notes say HDE-SEPA006 "owns the legacy chart-loader defect", and .2 requires removal or a genuinely pure retained surface. Isis can state the outcome at that level and record O-1 as a Product Owner decision for the Implementation Audit and Plan. Return it to Nathan only if Isis judges the Specification cannot be formed without it. Do not invent the choice |
| O-2 | Sequencing against Candidate CRD Items List items 9 and 10 (shared code neighbourhood: `adapter/http_reader.py`, `engine/providers/vendor_http.py`, the BodyGraph resolver path; PF10 addendum 2.1 decisions are item 9's prerequisite) and the unresolved `main` CI failure | Product Owner | Advisory only (S-5). Isis may record an Existing Work Check and a Tracked Issue. It must not hold the Specification for them |
| O-3 | No board card or "Epic or card" assignment exists ("Not selected" in the source) | Product Owner / authorized manual operator | Board maintenance is distinct from the Specification (HDE Governance §9.1.1). Not a prerequisite |
| O-4 | Date started, status and the `ASK OK?` sentinel in the Epic Specification Meta | Isis | Authoring choices for Isis under Plan Templates; the kickoff supplies none |

## 10. Inputs for the Specification's Business Case and requirement business cases

Plan Templates requires a Business Case for the Epic and for every requirement, citing "observed incidents or measurements", with "conformance to canon" and "could prevent" without an observed incident excluded. This kickoff supplies the observed facts and does not author the case.

- **Observed, source-stated and now partly verified:** (a) the legacy signature calls a method the default fixtures provider class lacks (V-6), exposed by HDE-CRD-0002's CI-coverage work, with a test retired as a result (V-7); (b) running the retired test appended to the tracked `artifacts/logs/loader_call.jsonl` through the loader's own call log (source-stated, Task notes; V-9 confirms the file is tracked); (c) the loader performs environment, clock, logging and filesystem work in a module canon classifies as Engine (V-5).
- **Source-stated priority:** "Required-Now architecture correction" (HDE Architecture §1.1; PF09.3 priority). Canon conformance alone is not a business case under Plan Templates; the observed incidents in (a) and (b) carry that weight.
- **Not in the source:** a user-visible symptom, a production incident, a measure of benefit, or a "why now" beyond the Product Owner's selection of this Epic and the Required-Now priority. Isis authors Beneficiary, Benefit and Measure, and states plainly where the source holds no observed incident.
- **Scope boundaries and non-goals** are in §5.2.

## 11. Source accounting

| Source unit (PF09.3 and the selection record) | Carried in |
| :- | :- |
| Header (title, v1.1.8, Canon, 2026-10-26, Last Update Gate) | §2 |
| §0.1 Scope (Separation: narrowing and commitment; no renewed broad exploration) | §6 (relied on); phase placement §3 |
| §0.2 Eligibility and exclusions | §6; no standalone documentation-only task is created (consistent with §5.2) |
| §0.3 Status values, deferral convention, repository support vs PF09 status | §3 (statuses preserved); §5.2 |
| §0.4 Authority routing; Epic and CRD boundary | §3, §5.2, §5.3 |
| §0.5 Evidence and legacy references | §5.1 (evidence requirements); no token ceremony introduced |
| §0.6 Completion standard | §3 (no status movement) |
| Phase III description, master status, notes | §3; §5.2 (HDE-SEPA005 Done; the two live observations re-homed to Coagulation are not this Epic's) |
| Task HDE-SEPA006: description, status, placement, owner, priority, Epic or card, dependencies, boundary, deliverables, notes (2 bullets on the defect and on closed CRDs) | §3, §4, §5.1, §5.2, §5.4, §7 (V-5 to V-9), §9 (O-1) |
| Subtasks .1, .2, .3: description, status, owner, dependencies, evidence, .2 note | §3, §5.1, §5.4 |
| Selection record §1 to §6 | §2, §3, §8 (S-2 to S-5), §9 |

Nothing meaningful in the source was omitted. The long Task note on the defect is restated in §5.1, §7 and §9, not reproduced verbatim; Isis reads the original in the Task HDE-SEPA006 section.

## 12. Specification coverage guide

This points to where this kickoff holds material for each field of the Epic Record Template. It does not restate the template.

| Template field | Kickoff material |
| :- | :- |
| Meta | Epic ID, name, phase "Separation" (§1, §2); phase rationale from PF09.3 §0.1 and the Task's "Phase placement" (§3); date, status, `ASK OK?` are Isis's (O-4) |
| Business Case | §4, §10 |
| Contract and Compatibility Posture | §5.1 (preserve governed caller output, failure behavior, CLI/API/Vendor and Mechanics behavior); §5.2; U-5 |
| Existing Work Check | §5.2 (HDE-SEPA005.3, HDE-CONJ010.4, Engine Core, BodyGraph resolver, HDE-CRD-0001/0002), §7 (V-7, V-8, V-10), O-2 |
| Deliverables | §5.1, at outcome level (no atomic tasks, commands or file edits) |
| PF Reference Map | §3, §6 |
| Exact-Source Evidence and Acceptance | §5.1 evidence requirements; §5.2 ("a moved filename, successful import, static source observation … does not establish" completion) |
| QA Rails | The source excludes live vendor and production DB activity unless separately authorized (§5.2). Whether open-rails or live proof applies is Isis's to state from canon; the kickoff makes no claim |
| Tracked Issues | §9 (O-1 to O-3), §8 (U-1 to U-5) |
| Specification Preflight | Isis's |

## 13. Boundaries and nonclaims

- This kickoff establishes no QA verdict, acceptance, Specification approval, Implementation Audit, Plan, PR, Proceed, merge authority, PF09 movement, board change, canon change or closure.
- It adds no scope to HDE-SEPA006 and removes none. Where it offers an observation (§7), the observation is context for the Implementation Audit, not a requirement.
- The local clone was shallow and no test, script or live provider call was run. Facts that depend on those are marked source-stated (§8).
- Merging this kickoff preserves the record and approves nothing (D21-C).

## 14. Receiver and reading for the next session

- Next prompt: CF-E-20 — Create Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb8129a159df9439b4e922). Next actor: Isis. `KICKOFF_HANDOFF_ID` is this file's repository path, `docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md`. It must be on `main` (its pull request merged) before CF-E-20 runs.
- **TypeSafe reading for CF-E-20** (installed scoring skill, request v8.2, script run once, session kind `review`, label "HDE-EPIC041 CF-E-20 Specification"; no Notion row written):
  - Action sent (v8.2): "Author one new pending Epic Specification document from one complete kickoff document: a single task with three subtasks, about 10 KB of source text, correcting an architecture boundary in one legacy Python module and its few callers. A fixed canon template for the Specification exists and the kickoff supplies the source facts; no code, test or canon change and no live run against a provider occurs. The Specification is new, not yet reviewed, and is followed by an independent reviewer and later an implementation audit and plan."
  - As printed: **TypeSafe v8.2: Sonnet 5.5 at medium.** Effort score 1.25 (confidence 0.83); rung probabilities low 0.01, medium 0.76, high 0.21, extra high 0.02, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.18, Sonnet 5.5 0.80, Haiku 5.5 0.01 (confidence 0.73). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.008, Fable 5.1 at high 0.002, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.002, Opus 5.5 at medium 0.137, Opus 5.5 at high 0.038, Opus 5.5 at extra high 0.004, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.008, Sonnet 5.5 at medium 0.608, Sonnet 5.5 at high 0.168, Sonnet 5.5 at extra high 0.016, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.008, Haiku 5.5 at high 0.002, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T02:45:28Z. Nathan picks the cell.
  - Flags: none printed.
  - Picks: Nathan's pick for CF-E-20 is not stated. For this CF-E-10 session, no setting was stated; none is recorded.
- **Surface advice (CF-E-20).** A top-level Claude Code cloud session for Isis on `amthorn78/glow-hdengine-v2`, started after this kickoff's pull request merges. Read access to `main` (including `docs/pfcanon/`, PF27 Epic Record Template and PF09.3) and to the CF-E-20 Notion page. Write access to one branch and one pull request under `docs/ephemeral/`. Not needed: Notion writes, production, vendor, Railway or database access, or code execution. The Specification can be written from the kickoff plus the cited canon.
