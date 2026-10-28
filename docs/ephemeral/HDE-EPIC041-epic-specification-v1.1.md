---
artifact_type: EPIC_SPECIFICATION
artifact_version: "1.1"
logical_id: HDE-EPIC041-EPIC-SPECIFICATION
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
state: SPECIFICATION_PENDING
approval_sentinel: ASK OK?
author: Isis (v1.0 by Isis-55, https://claude.ai/code/session_01Q789u1otbrFy2ZhqojikVt; v1.1 by the same continuing Isis role, Isis-56, https://claude.ai/code/session_01Q789u35D8uKpsTHJ67oMCz)
reviewer: Thoth (Thoth-20; https://claude.ai/code/session_01Q789u24G3yiuVFFZofiVfx), the same continuing Thoth reviewer under HDE Governance §9.1.1, as recorded by review v1.0
prompt: CF-E-40 — Revise Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb8113a64dda1a380c1b96; page state 2026-10-27T13:17:15.163Z, read in full); v1.0 was formed under CF-E-20 — Create Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb8129a159df9439b4e922)
revision_mode: PREAPPROVAL_REVISION
supersedes: docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md (v1.0, SPECIFICATION_PENDING, denied; preserved unchanged)
review_ref: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md (CF-E-30, INITIAL_DENY, redlines RL-1 to RL-7; merged as 0891314, #782)
application_record: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1-application-record.md
ecosystem_release: GCFPE-20261027.1 / 102726.1
authored_at: 2026-10-28 (v1.0 and v1.1)
repository_head_read: origin/main 0891314 (v1.1); db590ab (v1.0)
kickoff_ref: docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md
class_selection_ref: docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md
format_authority: PF27 Plan Templates §2 HDE-EPIC-Specification, "Epic Record Template (Normative)"
pf09_phase: Separation (Phase III)
next_prompt: CF-E-30
next_actor: Thoth (Specification review)
---

# HDE-EPIC041 — Epic Specification: Separation Pass 4

This is a pending Specification, version 1.1: the complete replacement of the denied v1.0, applying Thoth's review v1.0 redlines RL-1 to RL-7 (application record: `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1-application-record.md`). It is not approved, and it authorizes no Implementation Audit, Plan, PR, Ops, QA, PF09 movement or closure (HDE Governance §9.1.1). Merging this file preserves the record and approves nothing (D21-C).

## 0. Format resolved, lineage and canon relied on

**Format.** The permanent Epic Specification format is the **Epic Record Template (Normative)** in *Plan Templates* §2 "HDE-EPIC-Specification" (Change Process Guide §1.2 and §0.1A route there; Plan Templates "Artifact execution boundary" says the template owns Epic Specification format). Sections 1 to 12 below follow its field order: Meta; Business Case; Contract and Compatibility Posture; Existing Work Check; Deliverables; PF Reference Map; Exact-Source Evidence and Acceptance; QA Rails; Tracked Issues; Specification Preflight. This file declares no schema-version token of its own, and reuses none from a neighbouring artifact.

**Lineage.**

| Item | Value |
| :- | :- |
| Kickoff | `docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md`, `SPECIFICATION_KICKOFF`, `KICKOFF_READY`, merged to `main` by `amthorn78/glow-hdengine-v2#780` as `db590ab`; read in full. It is the sole substantive formation input |
| Selection | `docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md`, `CLASS_SELECTED`, class `EPIC`, by Nathan / Product Owner; merged as `8d56b19` (#779) |
| Repository head read | `origin/main` `db590ab` (v1.0); `origin/main` `0891314` (v1.1). The only change between them is the two `docs/ephemeral/` files merged by #781 and #782 |
| Review | `docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md`, CF-E-30, decision `INITIAL_DENY` with redlines RL-1 to RL-7 and Rulings R-A to R-C; merged as `0891314` (#782); read in full |
| Superseded version | `docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md` (v1.0, 45,985 bytes), preserved unchanged |
| Source | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`, Task HDE-SEPA006 and Subtasks .1 to .3, re-read in full by Isis (lines 1280 to 1379) |
| Author / reviewer | Isis authors and revises; the same continuing Thoth reviewer (Thoth-20) reviews and returns exact denial or redlines (HDE Governance §9.1.1) |

**Canon searched and relied on** (resolved from `docs/pfcanon/` on `main`; terms: chart loader, `engine/charts`, SEPA006, orchestrat, pure-compute, production-functional, Epic Record Template, close-pack, doc-delta, acceptance map):

| Document (title) | Sections relied on |
| :- | :- |
| Plan Templates | §2 "Epic Record Template (Normative)" in full: Meta, Business Case (including "Requirement and work-unit business case", re-read for v1.1), Contract and Compatibility Posture, Existing Work Check, Deliverables, PF Reference Map, Exact-Source Evidence and Acceptance, QA Rails, Tracked Issues, Specification Preflight (A to E); "Artifact execution boundary"; "Repository loci and file minting"; "Canon precedence for template use" (read in full for v1.1) |
| HDE Build Checklist — Separation (v1.1.8) | §0.4 "Authority and Work-Record Routing" including "Epic and CRD boundary"; Phase III header and notes; Task HDE-SEPA006 and Subtasks .1 to .3 |
| HDE Architecture | §1.1 "Single homes": "Non-BodyGraph chart loader classification [Required-Now]" and the Engine Core / sampler-core paragraph |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" (including "A revision supplies a complete replacement, preserves the prior artifact and returns to the actual decision owner"); §9.7.7 "Plan approval gate": "Business Case section required (Epic Specifications)" and "Business case for every requirement and work unit" (read in full for v1.1); "Production-functional epic live-proof requirement" and "Other production-affecting scope" |
| Change Process Guide | §1.2 "Specification: Resolve and use the current owning format"; §1.3; "Plan path provenance"; "Plan locus validation labels"; "Audit provenance in planning artifacts"; "Mandatory vendor minimum for production-functional surfaces" |
| HDE Schemas and Artifacts | "Optional token compatibility" and "Acceptance map — legacy token compatibility shape (clarification)" (for TI-07 only) |
| 7 Phases of Alchemical Engineering | §3 Separation (phase name and definition) |
| HDE Build Notes (PF10, v13.9) | Searched by term for the loader, `engine/charts`, `get_chart`, the Adapter/Engine chart boundary, HDE-SEPA006, acceptance map and close-pack. No match. PF10 is silent on this Epic's topic, so permanent canon governs. Its decisions on the S19 routed security findings are adjacent; they bear on this Epic only as TI-02 states |
| AGENTS.md (repository instruction file) | Canon-first rule; closed-rails defaults; PF canon read-only |
| Glow QA Guide | Named by title only as the QA home (§9). Not read in full for this Specification; no conformance to it is claimed beyond that pointer |
| Review v1.0 (in-flight, `docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md`) | §3 redlines RL-1 to RL-7, applied in full; §4 Rulings R-A to R-C (§13) |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

**Corrections carried from the kickoff.** The kickoff (§2) records that the selection record's "no current addenda" reading of PF10 was superseded: PF10 is v13.9 and has one addendum. Isis re-checked PF10 v13.9 directly and confirms it. The class, identity and PF09 mapping are unchanged.

## 1. Meta

* **Epic ID:** `HDE-EPIC041`
* **Epic name (short):** Separation Pass 4
* **Alchemical phase:** `Separation` (Phase III of PF09.3; PF21 §3)
* **Phase rationale:** HDE-SEPA006 is the last Separation unit not Done. It decides where chart-acquisition orchestration ends and deterministic Engine chart computation begins, which is the filtering and choosing PF21 assigns to Separation, and PF09.3 places it as "a sibling of HDE-SEPA005, not part of the Magic10 mechanics-configuration task".
* **Status:** `Pending Review` (the Specification is awaiting Thoth review; no implementation has begun)
* **Explicit approval sentinel:** `ASK OK?`
* **Date started:** `2026-10-28` (Specification formation; no implementation work has started)
* **Date completed:** `[INTENTIONALLY LEFT BLANK]`

## 2. Business Case

### 2.1 Epic-level Business Case

* **Problem statement.** The non-BodyGraph chart loader, which canon classifies as drift, mixes chart acquisition (rails and environment evaluation, provider selection, clocks, correlation context, logging, filesystem writes) with chart computation inside Engine-owned code. HDE Architecture classifies it as "implementation drift, not a sanctioned Engine I/O seam". The people who bear this are the delivery team: running or testing the chart path wrote to a tracked repository file through the loader's own call log (E-2), and its legacy-signature path calls a method the default fixtures provider does not define (E-1). PF09.3 records that the loader is not a release member and is not reached at runtime, so no Glow-user or production-operator impact is observed or claimed. Two defects are observed (E-1, E-2 below): the legacy-signature path calls a method the default fixtures provider does not define, and running a test of that path wrote to a tracked repository file through the loader's own call log.
* **Proposed change.** Establish a supported Adapter-owned orchestration entry for chart acquisition; keep only pure, explicit-input validation and normalization under Engine ownership; move every supported caller to the correct interface; retire the mixed operational boundary or keep only a genuinely pure compatibility surface; and prove the boundary with automated checks.
* **Value / impact.** Risk reduction and delivery-team value: a chart path whose Engine side cannot read the environment, clocks, providers, logs or filesystem, and whose operational side has one owner; removal of a known broken call path; removal of a test-time mutation of a tracked file. No user-visible change is intended (§4).
* **Why now.** The source classifies the work "Required-Now architecture correction". HDE-CRD-0002's CI-coverage work exposed the legacy-signature defect and left it deferred to the Product Owner, with all prior Separation tasks (HDE-SEPA001 to HDE-SEPA005) Done. The Product Owner selected this Epic on 2026-10-28. The source holds no production incident, user-visible symptom or measure beyond these; none is asserted here.
* **If not done.** The legacy-signature path stays broken against the default fixtures provider (E-1); exercising the loader's call log can again append to the tracked `artifacts/logs/loader_call.jsonl` (E-2); and the defect stays hidden behind a retired test rather than closed (E-3). The source records no user-visible or production consequence, and none is asserted.
* **What success looks like.** Each acceptance criterion in §3 is met with exact-source evidence: the Engine chart computation is demonstrably pure; one Adapter-owned orchestration entry owns the operational concerns; every supported caller has a recorded disposition and runs against the correct interface; governed caller output and failure behavior are preserved; and no tracked file is mutated by running the covering tests. Success is qualitative and checked by the criteria; the source defines no numeric target.
* **Scope boundaries.** In: Task HDE-SEPA006 and Subtasks .1, .2, .3 as written in PF09.3 (§3). Out: everything in §2.2.
* **Non-goals** (source-stated, Task notes and dependencies):
  1. No scoring algorithm and no full Magic10 delivery.
  2. No new provider contract and no fallback data.
  3. No broader Engine I/O exemption or additional Engine I/O carve-out.
  4. No production operation, and no live vendor or production database activity unless separately authorized.
  5. No provenance helper, and no completion claim for Dissolution's Engine Core work, HDE-SEPA005.3's typed mechanics-configuration loader or HDE-CONJ010.4's Core-backed compatibility integration, which stay intact and do not become a second home for this migration.
* **Separation from technical scope.** This Business Case does not stand in for the technical scope in §3 and §6.

### 2.2 Exclusions

The items above, plus: not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope (their CLOSE / CHANGE_CLOSED decisions and accepted evidence are "not acceptance of this separate migration"); no PF20 or PF30 entry and no PF30 gate (HDE Governance §9.1.1); no board-card or PF09 status movement; and no claim that any part is implemented, QA'd or complete.

### 2.3 Observed evidence used by the requirement business cases

Each item is a fact Isis can point to; each is labelled with how it was established. None is a forecast.

| ID | Observation | Basis |
| :- | :- | :- |
| E-1 | In the legacy signature, `engine/charts/loader.py` line 81 calls `provider.get_chart(...)`; the `FixturesProvider` class that `engine/config/provider_loader.py` imports (`engine/provider/fixtures.py`) defines `get_pair_profile` and no `get_chart`. PF09.3 records that the call fails with `AttributeError` | Canon-cited (PF09.3 Task HDE-SEPA006 notes). Isis re-read lines 78 to 83 of the loader and grepped both classes on `main` `db590ab`. Static reading only; the call was not executed (§11, TI-03) |
| E-2 | Running the retired legacy-signature test appended to the tracked `artifacts/logs/loader_call.jsonl` through the loader's own call log; the file remains tracked | Canon-cited (PF09.3 Task HDE-SEPA006 notes); Isis confirmed the file is tracked on `main` |
| E-3 | HDE-CRD-0002 retired `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` because of E-1; the retirement "neither migrates nor removes the legacy signature"; `audit/HDE-CRD-0002_close_report.md` defers the defect to the Product Owner | Canon-cited (PF09.3 Subtask HDE-SEPA006.2 notes and Task notes) |
| E-4 | `engine/charts/loader.py` (173 lines) performs environment and rails evaluation, clock reads, a correlation id and a keys-only log write relative to the working directory, and returns fixture-style data with Gates `[1, 2, 3]` on two paths, in a module canon assigns to Engine | Canon-cited (HDE Architecture §1.1, classification at commit `5ef911fe`). Master Scrum read the file (kickoff V-5); Isis re-read the 78 to 83 span and confirmed the line count and the importers in E-5 |
| E-5 | Candidate importers of the loader on `main` `db590ab`: one script, `scripts/make_compat_determinism_artifacts.py`, and two loader tests. No importer under `engine/` or `adapter/` | Observed by static `grep` by Isis, confirming kickoff V-10. Not an exhaustive or authoritative caller inventory (§11, TI-03). The path is provenance, not a required path (§6) |

### 2.4 Requirement business cases

Each requirement states Beneficiary, Evidence, Benefit and Measure (Plan Templates, "Requirement and work-unit business case"). No budget, session, round or push ceiling is stated or implied.

| Req | Beneficiary | Evidence | Benefit | Measure (checked after delivery) |
| :- | :- | :- | :- | :- |
| R-01 Adapter-owned orchestration | Delivery team | E-1, E-2 (E-4 locates the concerns) | Running or testing the chart path no longer writes a tracked repository file through an operational log inside Engine code (E-2), and provider selection no longer sits in an Engine path that calls a method the default provider does not define (E-1): the operational concerns have one Adapter-owned owner | AC-01: the operational concerns are located in Adapter-owned orchestration and absent from Engine chart code; acquisition uses the sanctioned resolver/ingest boundary. AC-05: running the covering tests leaves tracked files unchanged |
| R-02 Pure Engine chart computation | Delivery team | E-2, E-4 | Engine chart validation and normalization become deterministic, testable data-in/data-out, with no write to a tracked file as a side effect of use | AC-02: Engine chart code reads no environment, clock, randomness, provider, network, log or filesystem state and has no import-time side effect; AC-05 adds that running its covering tests leaves tracked files unchanged |
| R-03 Caller migration and retirement | Delivery team | E-1, E-3, E-5 | No supported caller depends on the broken legacy-signature path or on the mixed Engine module; a defect already worked around by test retirement is actually closed, not hidden | AC-03: the supported-caller inventory has a disposition for every member; the operational Engine path is removed or only a pure surface with an owning-contract basis remains |
| R-04 Boundary and behavior verification | Delivery team; QA | E-2, E-3 | Regression of the boundary is caught by automated checks rather than by a later accident like E-2 | AC-04: positive and negative automated checks prove the AC-02 purity and the AC-01 ownership; AC-05 shows governed outputs preserved |

## 3. Requirements and acceptance criteria

Identities are stable for this Epic: `R-nn` for requirements, `AC-nn` for acceptance criteria. They add no token and are not acceptance tokens. Wording stays at scope-and-outcome level; the Implementation Audit and Plan resolve paths, commands and work units.

| Req | Work item | Requirement (outcome) |
| :- | :- | :- |
| R-01 | HDE-SEPA006.1 | Environment and SAFE_MODE/rails evaluation, provider selection, chart acquisition, wall and performance clocks, correlation context, operational logging and filesystem writes belong to one supported Adapter-owned orchestration entry. Vendor or database acquisition goes through the sanctioned BodyGraph resolver/ingest boundary. No fallback data and no additional Engine I/O carve-out is introduced. |
| R-02 | HDE-SEPA006.1 | Engine chart validation and normalization are explicit data-in/data-out computation with no time, randomness, environment, network, provider, logging or filesystem side effects, and no import-time side effect. Explicit inputs, outputs, failure behavior and orchestration ownership are defined for the migration |
| R-03 | HDE-SEPA006.2 | Every actual supported runtime, tooling and test caller, identified at implementation time and including the active compatibility-determinism artifact generator and the relevant loader/provider tests, is migrated to the correct orchestration or pure-computation interface. The old operational Engine path is removed, or only a genuinely pure compatibility surface is kept where its owning contract permits it. An import-path rename alone is not migration. Historical audit captures stay unchanged. The migration preserves governed caller output and failure behavior, and applicable CLI/API/Vendor and Mechanics behavior. |
| R-04 | HDE-SEPA006.3 | Meaningful automated checks prove the R-02 purity and no import side effect; exercise the orchestration rails, correlation context, keys-only logging and failure behavior with controlled fixtures; verify the complete caller migration; and reconcile R-01 to R-03, including any retained pure surface |

| AC | Binds | Criterion |
| :- | :- | :- |
| AC-01 | R-01 | The operational concerns listed in R-01 are owned by the Adapter-owned orchestration entry, and a supported orchestration path exists for each supported use. Vendor/DB acquisition, where used, goes through the sanctioned resolver/ingest boundary |
| AC-02 | R-02 | An explicit interface and side-effect account shows the Engine chart code takes explicit inputs and returns data, with none of the listed side effects, including at import |
| AC-03 | R-03 | The supported-caller inventory, with exact source attribution, gives every member a disposition; each is migrated or retired; the old operational Engine path is removed, or a retained compatibility surface has both an owning-contract basis and evidence of actual purity |
| AC-04 | R-04 | Positive and negative automated boundary checks, controlled fixtures for rails, correlation context, keys-only logging and failure behavior, and the reconciliation of R-01 to R-03 all pass, with actual commands, configuration, tested-source identity, results, responsible actor, time and limitations recorded |
| AC-05 | R-01, R-03, R-04 | Regression results show governed caller output and failure behavior preserved; no fallback data exists in the changed boundary; running the covering tests leaves tracked files unchanged |

AC-05's "tracked files unchanged" limb is Isis's reading of E-2 and of the Task boundary that Engine chart code has no filesystem write; it adds no scope beyond that boundary.

**Not evidence of any criterion** (source-stated): a moved filename, a successful import, a static source observation, or another change's accepted QA.

**Decision for the Product Owner (D-1, not made here).** The source makes the Product Owner "this task's decision owner, including for the legacy chart-loader defect". No repair, retirement or retention decision is recorded. The Specification states the outcome at the level canon fixes (R-03, AC-03: remove the old operational path, or keep only a genuinely pure surface), and does not choose among repair, retirement and pure retention. The decision is owned by the Product Owner and is needed by the Implementation Audit and Plan (§11, TI-01). The Specification can be formed and reviewed without it.

## 4. Contract and Compatibility Posture

* **Contract changes / new surfaces.** One internal change in ownership: a supported Adapter-owned chart-acquisition orchestration entry (R-01) and an Engine-side pure validation/normalization interface (R-02). **No new public route, flag, public payload field, CLI command or flag, provider contract, or HTTP home is introduced or authorized.** The exact internal interface shapes belong to the Implementation Plan.
* **Justification.** The ownership move is the capability HDE Architecture §1.1 and the Task require; it is necessary to achieve §2.1 and adds no external surface.
* **Flag strategy.** No new flag. No existing surface is reused as a flag.
* **Backward-compat posture.** Unchanged by default: governed caller output and failure behavior, CLI/API/Vendor behavior and Mechanics behavior (R-03); the Reader (production `POST /api/reader` v1 and v2; dev `GET /reader`), `hdctl showcompat` and the Engine Core pure-compute path are not in scope and are not changed. Changes for existing users: none intended. Changes for in-repo callers: the supported callers move to the new interfaces (R-03). Rollout or migration: no data migration and no release cut is part of this Epic. The release-admission surface (`catalog/manifest.json`) is not changed by this Specification; whether the Implementation Plan's work touches a release member is for the Plan to state. Historical audit captures stay unchanged.
* **Public-surface posture stated with its limit.** The source states the loader "is not reached at runtime", and Isis's static search found no importer under `engine/` or `adapter/` (E-5). Whether any public or CLI surface reaches the loader, directly or by dynamic import, is not established (TI-03). This Specification therefore commits to no public change (above) and does not assert "no public surface is affected" as a finding.
* **Open-rails QA declaration (Governance "Production-functional epic live-proof requirement"; Plan Templates).**
  1. *Affected surfaces identified here:* the non-BodyGraph chart loader and its supported callers; the new Adapter-owned orchestration entry; the Engine pure normalization interface.
  2. *Declaration.* On the source's statements and E-5, none of these is a surface used to produce a production feature that PF canon describes as functional. That declaration rests on the source and a static search, and Isis does not treat it as proven.
  3. *Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it.
  4. *Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption.
  5. *Authorization.* The row authorizes no live vendor or production database activity. Any live step needs separate, task-specific Product Owner authorization (§9).
* **Implementation preservation.** Any Plan, guide or QA-prep artifact derived from this Specification must preserve items 3 and 4.
* **Vendor-call ownership (Glow app integration).** This Epic does not change Glow app integration. Ownership stays as canon states: the HD Engine owns vendor acquisition, persistence-facing, retrieval-facing and compute-facing behavior; Adapter-owned orchestration is the operational owner inside it. No direct app-side vendor call and no bypass of the HD Engine vendor seam is proposed, so no ADR justification is needed. The secret boundary, app-to-engine contract and raw-vendor-data boundary are unchanged.
* **Vendor payload normalization posture.** This Epic involves chart *normalization* inside the loader. It **records no vendor adapter or schema proof** and implements no vendor runtime adapter. It does not claim that vendor chart data feeds the existing BodyGraph cache, the person/cache contract or the compatibility compute path; full vendor runtime conformance; legacy ingest replacement; or completion of any parent task beyond the scoped Task HDE-SEPA006.
* **`bg:resolve --source vendor` route-policy posture.** Not covered by this slice (path status: unsupported nonclaim for this Epic). This Epic does not claim `bg:resolve` resolves complete BodyGraph detail, that `charts/simple` success proves full BodyGraph resolution, or canonical v2 BodyGraph-resolution runtime compatibility.
* **Configured-v2 mapped-cache.** Not touched. Nothing here treats dry-run mapping, compatibility computation or a bounded smoke as proof that durable or production-like mapped-cache writes are supported.

## 5. Existing Work Check

* **Existing features and components.**
  * Today's loader module (`engine/charts/loader.py`, canon-cited by HDE Architecture §1.1) is "current repository reality until separately remediated".
  * The sanctioned BodyGraph resolver/ingest boundary and the existing vendor/DB obligations stay intact.
  * Engine Core (`compute_core`) and the compatibility compute path are pure-compute homes (HDE Architecture §1.1) and are not this Epic's home for chart acquisition.
  * HDE-SEPA005.3's typed mechanics-configuration loader and HDE-CONJ010.4's Core-backed compatibility integration are Done or separate (PF09.3) and are not a second home for this migration.
* **Prior epics and Build Notes relevant (titles/IDs only).** HDE-CRD-0001 and HDE-CRD-0002 (closed); HDE-EPIC040 (closed; Separation Pass 3); HDE-SEPA001 to HDE-SEPA005 (Done). HDE Build Notes is silent on this topic; its decisions on the S19 routed security findings are adjacent (TI-02). The earlier addendum that recorded the loader defect (cited by PF09.3 and the HDE-CRD-0002 close report) is not present in v13.9; the defect is fully stated in PF09.3's Task notes, so no gap results.
* **Existing acceptance evidence reviewed.** `tests/retired_tests.md` row for the retired legacy-signature test; `audit/HDE-CRD-0002_close_report.md` (deferral to the Product Owner); the retained coverage the source names, `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`. Their definitions were observed to exist; **whether they pass has not been run** (TI-04).
* **Legacy token references reused:** `None`.
* **Existing evidence located.** The tracked `artifacts/logs/loader_call.jsonl` (the file E-2 mutated; HDE-CRD-0002 left it unchanged). No governed evidence for HDE-EPIC041 exists.
* **Gap statement.** Unproven or unestablished: the complete supported-caller set including dynamic imports, scripts outside the paths searched, documentation-referenced commands and CI selection lists (TI-03); whether the retained-coverage tests pass (TI-04); whether the dates and states canon asserts for commits `6c6f4b2a` (2025-09-28) and `5ef911fe` match the repository, since the clone seen by the kickoff was shallow (TI-05); which owning contract, if any, permits a retained pure compatibility surface (TI-06); whether any public or CLI surface reaches the loader (TI-03).
* **Sequencing note (advisory).** Candidate CRD Items List items 9 and 10 (the S19 routed security findings change and the unresolved `main` CI failure) share a code neighbourhood and are owned by no change. The selection record records Master Scrum's advice, "not a canon rule", that deciding them before the Implementation Audit is advisable. This Specification neither depends on nor holds for them (TI-02).

## 6. Deliverables (Jobs To Be Done)

No deliverable is an OPS task. There is no OPS work in this Epic, so the OPS note and Ops Task Record do not apply. Each deliverable is a *required future deliverable*, not an artifact asserted to exist. Paths, commands and work units belong to the Implementation Audit and Plan.

**Locus validation.** The only existing loci named in this Specification are `engine/charts/loader.py` and `artifacts/logs/loader_call.jsonl` (label: Canon-cited, HDE Architecture §1.1 and PF09.3 Task HDE-SEPA006), and `tests/retired_tests.md` and the two retained-coverage test names (label: Canon-cited, PF09.3 Task notes). Every other file, module, script, new interface or test is *unknown pending discovery* and is not required by this Specification. The script `scripts/make_compat_determinism_artifacts.py` and the two loader tests (E-5) are provenance from Isis's static search on `main` `db590ab` and are not required paths; the Implementation Audit must validate them.

* **D1 — Adapter-owned orchestration entry (HDE-SEPA006.1; R-01).**
  *Job:* the operational concerns move to a supported Adapter-owned entry.
  *Evidence required:* implementation diff; explicit input/output and side-effect account; positive and negative boundary-check results.
  *PF references:* HDE Architecture §1.1; HDE CLI/API/Vendor Reference (preserved behavior); PF09.3 Subtask HDE-SEPA006.1.
* **D2 — Pure Engine chart validation and normalization (HDE-SEPA006.1; R-02).**
  *Job:* the Engine side takes explicit inputs and returns data with no side effect, including at import.
  *Evidence required:* the interface/side-effect account, plus focused purity checks.
  *PF references:* HDE Architecture §1.1 ("purity" rule); PF09.3 Subtask HDE-SEPA006.1.
* **D3 — Supported-caller migration and retirement (HDE-SEPA006.2; R-03).**
  *Job:* migrate every supported caller; remove the old operational path or keep a justified pure surface.
  *Evidence required:* supported-caller inventory with exact source attribution and a disposition per member; migration/retirement diff; focused runtime, tooling and loader/provider caller-regression results; for any retained surface, an owning-contract basis and evidence of purity.
  *PF references:* PF09.3 Subtask HDE-SEPA006.2; HDE Mechanics Guide (preserved behavior).
* **D4 — Boundary and behavior verification (HDE-SEPA006.3; R-04).**
  *Job:* automated checks and the reconciliation of D1 to D3.
  *Evidence required:* boundary and caller-regression results; controlled positive/negative and side-effect checks; actual commands, configuration, tested-source identity, results, responsible actor, time and limitations; indexing through the existing governed writer.
  *PF references:* PF09.3 Subtask HDE-SEPA006.3; HDE Schemas and Artifacts (evidence families, by title).
* **D5 — Epic close preparation baseline (all requirements).** The close pack and doc-delta surfaces in §10, for eventual close.

These map to PR plans, CI jobs and QA playbooks by title only (Change Process Guide; Glow QA Guide).

## 7. PF Reference Map

* **Core.** 7 Phases of Alchemical Engineering §3 (Separation); Change Process Guide §1.2 and §1.3 (plus the plan-path and locus rules); HDE Build Checklist — Separation (v1.1.8), Task HDE-SEPA006 and Subtasks .1 to .3; Glow QA Guide (title only, §9).
* **Additional.** HDE Architecture §1.1; HDE Governance §9.1.1 and the production-functional live-proof requirement; HDE CLI/API/Vendor Reference and HDE Mechanics Guide (preserved-behavior contracts, by title); HDE Schemas and Artifacts (evidence families and canonical paths, by title).

**HDE work-item mapping** (exact PF09.3 identities preserved; one block per task-like item):

| Work item ID | PF09 disposition | Phased PF09 document | Task ID | Subtask ID | Exact source heading | Contribution | Status nonclaim |
| :- | :- | :- | :- | :- | :- | :- | :- |
| W-SEPA006 | in the current epic | PF09.3-Canon-HDE-Build-Checklist-Separation, v1.1.8 | HDE-SEPA006 | HDE-SEPA006.1, .2 and .3 (mapped in the rows below) | Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction | advances | This Specification does not move PF09 status; source status stays **Not done** |
| W-SEPA006.1 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.1 | Subtask HDE-SEPA006.1 — Adapter-owned acquisition and pure Engine normalization | advances | Source status stays **Not done**; no movement |
| W-SEPA006.2 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.2 | Subtask HDE-SEPA006.2 — Supported caller migration | advances | Source status stays **Not done**; no movement |
| W-SEPA006.3 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | advances | Source status stays **Not done**; no movement |

Out of the Epic (35 units, preserved **Done**, context only): HDE-SEPA001 to HDE-SEPA005 and all their subtasks. Phase III master status: **Not Done**. The 39-unit count (35 Done, 4 Not done) is the kickoff's script-verified result (§3); Isis re-read the Phase III header and the Task HDE-SEPA006 section directly.

## 8. Exact-Source Evidence and Acceptance

* **Governing acceptance scope.** AC-01 to AC-05 (§3), each binding the PF09.3 unit shown. Governing requirements: HDE Architecture §1.1 (purity and the chart-loader classification); PF09.3 Task HDE-SEPA006 and Subtasks.
* **Repository and source identity.** Repository `amthorn78/glow-hdengine-v2`. Planning baseline: `main` `db590ab`; PF09.3 v1.1.8 (git blob `8b2dbf49081ea53690efa9b8eb7d8d493e8614e9`, 89,754 bytes, per the kickoff). At execution and review the exact implementation or QA candidate is bound by the PR number, base SHA, reviewed head SHA, relied-upon exact-head CI, review record, merge SHA and post-merge repository fact, each recorded as it occurs.
* **Direct-main identity.** Not applicable. No direct-main write is authorized by this Specification.
* **Workflow and QA evidence.** The applicable CI workflow and exact tested SHA, the check set, conclusion, governed reports, Index/Mirror rows, path proofs and attestations are required only for the changed surfaces. Governed evidence is produced by the canonical tools only; no hand edits. Required governed evidence is indexed through the existing authorized writer, and tested-source attribution is kept distinct from any later evidence-storage commit and from review-time HEAD (PF09.3 Task HDE-SEPA006, 'Deliverables and required evidence'; HDE Schemas and Artifacts). This is a governed-evidence obligation, not a requirement.
* **Decision requirement.** QA verdict: the authorized QA owner (Kronos, independent). Acceptance and closure: Isis per HDE Governance §9.1.1. D-1 (§3) is the Product Owner's. No decision is claimed as issued.
* **Evidence proportionality.** Evidence is tied to AC-01 to AC-05 and the changed surfaces only. No unrelated full-suite, roster or matrix is required because an earlier epic used one.
* **Legacy token references.** None. No token roster, registry lookup, claim or token-evidence matrix is required or minted.
* **PF09 scope/status binding.** The work-item mapping (§7) is separate from acceptance evidence. A mapping, repository fact, CI result, QA verdict or artifact hash does not itself move PF09 status.
* **Non-token obligations and nonclaims.** This Specification establishes no implementation, behavior, compatibility, QA, OPS, deployment, release, acceptance, build-checklist movement, closure or canon-change claim. The kickoff's facts E-1 to E-5 are context for the Audit, not requirements.

## 9. QA Rails — Open/Close (Final PR)

* **Closed rails default.** Final-PR CI and any acceptance-relevant proof runs are expected under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).
* **Opened-rails exception.** None is declared at the Specification level. §4 states the binding condition under which an opened-rails live vendor step becomes mandatory, and the scope of the Product Owner's authorization it would need. If that condition is met, open-conformance evidence is required alongside closed-refusal evidence, as the governing QA posture requires.
* **Live QA.** Live QA is required for eventual close of this Epic. Governing documents, by title: Glow QA Guide; Change Process Guide. The QA Plan is a separate work product; this Specification embeds no runbook, commands, step sequence, QA root layout or evidence-directory scheme.
* **Evidence families expected at close (titles only).** Boundary and caller-regression results; the supported-caller inventory; governed evidence indexed by the existing authorized writer; the close pack of §10.
* **Legacy tokens.** None.

## 10. Close-pack baseline and doc-delta baseline (eventual close; names only)

Required close-pack artifacts (PF27 Specification Preflight B and D; paths follow the `EPIC-###` canon pattern):

| Artifact | Path |
| :- | :- |
| Epic close report | `audit/EPIC-041_close_report.md` |
| Epic manifest | `audit/EPIC-041_MANIFEST.json` (with `key_outputs` as a map binding each declared close-pack artifact) |
| Epic acceptance map | `docs/acceptance_map_epic041.json` (see TI-07; carries no token roster) |
| Acceptance-map viability log | `audit/qa/hde-epic041/acceptance_map_viability.log` (conditional on the acceptance map, per Preflight B) |
| Token-to-evidence matrix | Not required: no active scoped legacy token use |

Path-proof transcripts included in the close pack (explicit filenames): `audit/EPIC-041_close_report.md.path_proof.txt`; `audit/EPIC-041_MANIFEST.json.path_proof.txt`; `docs/acceptance_map_epic041.json.path_proof.txt`.

Doc-delta surfaces (both declared, lowercase epic id): draft/staging `audit/docdeltas/hde-epic041_doc_deltas.md`; epic-scoped capture and authoritative record `audit/qa/hde-epic041/00_meta/doc_deltas.md`.

Minimum evidence pointers (PF27 Preflight D, canonical per HDE Schemas and Artifacts): `docs/evidence/INDEX.json`; `docs/evidence/INDEX.sha256`; `artifacts/evidence_index.jsonl`; `artifacts/evidence_index.jsonl.sha256`; `artifacts/evidence_index.jsonl.path_proof.txt`. The evidence-index snapshot family is not included, because this Specification plans no D23 deliverable.

These are expected locations under canon for eventual close. They are not asserted to exist and are written only by the canonical tools. Directory names are lowercase ASCII (Preflight E). Close mechanics belong to the owning QA and closeout artifacts, not here.

## 11. Tracked Issues

Status at formation: all **Open**. Each must end this Epic proved, carried forward, promoted to a cross-epic ISSUE-XXX, or explicitly dropped (Plan Templates, "Tracked Issues").

| Issue ID | Title | Status | Scope | Disposition for this Epic |
| :- | :- | :- | :- | :- |
| ISSUE-EPIC041-TI-01 | Legacy chart-loader defect: repair, retirement or pure retention | Open; Product Owner decision (D-1) | The Product Owner is the Task's decision owner and no decision is recorded (E-1, E-3) | Decided by the Product Owner before or within the Implementation Plan; R-03 and AC-03 hold for any choice |
| ISSUE-EPIC041-TI-02 | Sequencing against Candidate CRD Items List items 9 and 10 and the `main` CI failure | Open; advisory | Items 9 and 10 share a code neighbourhood (`adapter/http_reader.py`, `engine/providers/vendor_http.py`, the BodyGraph resolver path) and HDE Build Notes' decisions on the S19 routed security findings are item 9's prerequisite. The latest `main` `ci` push failure was reported as the OBS-17 failure at `1fb4731b` (selection record §5, not re-verified here). If the Adapter-owned orchestration entry performs resolver-selected vendor acquisition, HDE Build Notes' decisions on vendor route selection and on the production vendor override scope govern that path; the Implementation Audit determines whether they apply. | Product Owner; this Specification does not wait for them. Re-checked at the Audit |
| ISSUE-EPIC041-TI-03 | Completeness of the supported-caller set, and public/CLI reach of the loader | Open | E-5 is a starting observation. Dynamic imports, scripts outside the paths searched, documentation-referenced commands and CI selection lists (`pytest.ini` and `ci/checks/classify_ci_changes.py` name a loader test) are not inventoried; E-1 is not executed. Copies of the loader's importers and of the retired test under `.audit_src/` (`scripts/`, `tests/loader/`, `tests/compat/`, `tests/provider/`; kickoff V-10) are classified by the Implementation Audit as supported callers or as historical audit captures, which R-03 keeps unchanged. | Implementation Audit and AC-03 |
| ISSUE-EPIC041-TI-04 | Retained-coverage tests not run | Open | The two tests PF09.3 names as retained coverage exist but pass/fail is unknown | Implementation Audit, then AC-05 |
| ISSUE-EPIC041-TI-05 | Commits `6c6f4b2a` and `5ef911fe` unresolved in the kickoff's shallow clone | Open | The defect date (2025-09-28) and the classification commit are source-stated and not independently verified | Implementation Audit |
| ISSUE-EPIC041-TI-06 | Owning contract for a retained pure compatibility surface | Open | PF09.3 permits it only "if its owning contract permits it"; no owning contract is identified | Implementation Audit; Product Owner if it is a product choice |
| ISSUE-EPIC041-TI-07 | Canon tension on the acceptance map for tokenless work | Open; reported, no canon change proposed here | Plan Templates (Preflight B) lists "the epic acceptance map" in the close-pack minimum, without a condition. HDE Schemas and Artifacts says a new acceptance map is not required for tokenless work. No acceptance map for HDE-EPIC038 to HDE-EPIC040 is present under `docs/` on `main` (static listing by Isis; how those Epics closed is not established here). This Specification lists the stricter set (§10), and states that no token roster is required | Thoth to confirm the reading; if canon needs a change, report it to the Product Owner. Not resolved by editing canon |

## 12. Specification Preflight

* **Epic Planning only, no QA planning.** Confirmed. This Specification contains no runbook, command line, step sequence, environment setup, Step-0 procedure, QA root layout or manual PASS/FAIL field.
* **A. Legacy token validation.** No active scoped legacy token use. No token roster, claim, lookup or matrix is required; none is minted.
* **B. Close-pack baseline declared.** Yes (§10), titles and paths only; close report, manifest, acceptance map, viability log and both doc-delta surfaces are declared; the token matrix is declared not required. Close-report field requirements (canon pointer fields, workflow-truthfulness fields, reused-proof-family fields) bind at close and are not satisfied here.
* **C. Local-bundle completeness.** No local bundle directory is claimed by any deliverable; not applicable.
* **D. Canonical evidence-path binding.** The paths named in §10 are PF27 and PF12 canonical forms (pattern `EPIC-###`, lowercase directories, Index/Mirror pair and the `.path_proof.txt` suffix). The canonical JSON gate family and the evidence-index snapshot are not bound by this Epic. No new compare artifact path is introduced.
* **E. Lowercase directory naming.** Satisfied.
* **Plan path provenance and locus labels.** Satisfied by §6 "Locus validation": existing loci are Canon-cited; all other loci are unknown pending discovery or are provenance only.
* **Reality Audits.** Not consulted; not a gate.
* **Placeholders.** None. Unresolved decisions are listed as D-1 and TI-01 to TI-07.
* **Scope boundary check.** Atomic tasks, file edits, commands, planned PR/Ops work units, detailed PR plans, approval objects and receipts are not prescribed (HDE Governance §9.1.1).

## 13. Retained review context, revision history, TypeSafe reading, surface advice and nonclaims

**Retained Thoth review context.** The reviewer is the same continuing Thoth reviewer under HDE Governance §9.1.1: Thoth-20 (https://claude.ai/code/session_01Q789u24G3yiuVFFZofiVfx), as recorded by review v1.0. v1.0 recorded that identity as unknown, because neither the kickoff nor CF-E-20 named it. The review route is CF-E-30 (Review and Approve Epic Specification).

Review v1.0 ruled on the questions v1.0 asked:

* **Ruling R-A (TI-07).** The stricter reading stands, and §10 keeps the acceptance map, with no token roster. Whether tokenless Epics should still need an acceptance map is a canon question, not a Specification defect. TI-07 stays Open. Its disposition is to report the question to the Product Owner as a possible canon change. No canon is edited.
* **Ruling R-B (§4 open-rails declaration).** Accepted. Downstream artifacts must preserve items 3 and 4.
* **Ruling R-C (evidence basis).** Observed repository and test-run defects qualify as evidence. "No production incident" is a truthful nonclaim, not a gap.
* **Status `Pending Review`.** Accepted as the template value.

**Question for this re-review.** Do RL-1 to RL-7 apply as written? The application record gives the application item by item.

**Pre-approval revision history.**

| Version | Prompt | Author | Result |
| :- | :- | :- | :- |
| 1.0 | CF-E-20 | Isis-55 | `SPECIFICATION_PENDING`; reviewed by Thoth-20 under CF-E-30: `INITIAL_DENY`, redlines RL-1 to RL-7 (#782) |
| 1.1 | CF-E-40 | Isis-56 (same continuing Isis role) | `SPECIFICATION_PENDING`, `ASK OK?`; RL-1 to RL-7 applied; returns to Thoth-20 under CF-E-30 |

**TypeSafe reading for the CF-E-30 re-review.**

* Method: installed scoring skill, request v8.2, script run once, session kind `review`, label "HDE-EPIC041 CF-E-30 Specification re-review".
* No Notion row was written. This is an executing-flow session; CF-E-40 writes only under `docs/ephemeral/`.
* Action sent (v8.2): "Re-review one revised pending Epic Specification of about 47 KB that was reviewed once and denied, checking against an item-by-item application record that seven exact redlines the reviewer wrote were applied: three rewrite business-case text for the Epic and two of its five requirements, one of which is removed and restated as constraints, and four are small citation, precedence and tracked-issue additions; the reviewer approves or returns exact redlines. A written prompt with steps exists; no code, test or canon change and no live run against a provider occurs. An implementation audit and plan, independently reviewed, follow later."
* As printed: **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.78 (confidence 0.82); rung probabilities low 0.00, medium 0.25, high 0.73, extra high 0.02, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.98, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.245, Opus 5.5 at high 0.715, Opus 5.5 at extra high 0.020, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.005, Sonnet 5.5 at high 0.015, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T03:14:42Z. Nathan picks the cell.
* Flags: none printed.
* Note on the action text: it said "about 47 KB". The saved v1.1 is about 52 KB. The reading was run once and not repeated.
* Readings in earlier versions: v1.0 §13 keeps the reading for the first CF-E-30 review. Review v1.0 §5 keeps the reading for this CF-E-40 session.
* Picks: Nathan has stated no pick for the CF-E-30 re-review and none for this CF-E-40 session, so none is recorded.

**Surface advice (CF-E-30 re-review).**

* Run it in the continuing Thoth-20 role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this revision's pull request merges.
* Needs:
  * read access to `main`, including `docs/pfcanon/` (HDE Governance §9.7.7, Plan Templates §2), this v1.1, its application record, v1.0 and review v1.0;
  * the CF-E-30 Notion page;
  * write access to one branch and one pull request under `docs/ephemeral/`.
* A diff of v1.0 against v1.1 is the fastest check of the application. The application record lists every change that a redline does not itself state.
* Not needed: Notion writes, code or test execution, or production, vendor, Railway or database access.

**Verification performed by Isis.**

* *v1.0.* Static reads and `grep` only, on `main` `db590ab`:
  * `engine/charts/loader.py`: line count, and lines 78 to 83;
  * the two `FixturesProvider` classes and their `get_chart` / `get_pair_profile` definitions;
  * importers of the loader;
  * tracked status of `artifacts/logs/loader_call.jsonl`;
  * PF10 v13.9 searches;
  * the PF09.3 and PF02 passages quoted above.
* *v1.1.* Static reads and `git`/`grep` only, on `main` `0891314`:
  * `git diff db590ab 0891314` changes only the two `docs/ephemeral/` files of #781 and #782, so the v1.0 repository observations E-1 to E-5 still hold on this head;
  * `.audit_src/` was listed to confirm the RL-7 copies exist;
  * HDE Governance §9.7.7 and Plan Templates §2 "Business Case", "Requirement and work-unit business case" and "Canon precedence for template use" were read in full;
  * PF10 v13.9 was searched for the chart loader, `SEPA006`, `get_chart` and business case, with no match.
* *Both.* No test, script or provider call was run, and nothing outside `docs/ephemeral/` was changed.

**Nonclaims.** This Specification does not establish any of these: a QA verdict, acceptance, approval, an Implementation Audit, a Plan, a PR, a Proceed, merge authority, PF09 movement, a board change, a canon change, a PF10 addendum, OPS, deployment, build-checklist movement or closure. It adds no scope to HDE-SEPA006 and removes none. RL-3 restates R-05's source obligations as constraints on R-01 and R-03 and as a governed-evidence obligation in §8. It drops none of them.
