---
artifact_type: EPIC_SPECIFICATION_REVIEW
artifact_version: "1.0"
logical_id: HDE-EPIC041-EPIC-SPECIFICATION-REVIEW
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
review_mode: INITIAL_SPECIFICATION_REVIEW
decision: INITIAL_DENY
reviewed_artifact: docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md
reviewed_artifact_version: "1.0"
reviewed_artifact_state: SPECIFICATION_PENDING (unchanged by this review)
reviewed_artifact_blob: 45,985 bytes on main at 34445a3 (merged by amthorn78/glow-hdengine-v2#781)
kickoff_ref: docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md (KICKOFF_READY; merged as db590ab, #780)
class_selection_ref: docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md (CLASS_SELECTED, EPIC; merged as 8d56b19, #779)
reviewer: Thoth (Thoth-20; https://claude.ai/code/session_01Q789u24G3yiuVFFZofiVfx), the continuing Thoth reviewer for this change under HDE Governance §9.1.1
author_of_reviewed_artifact: Isis (Isis-55)
prompt: CF-E-30 — Review and Approve Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb81a88f00d49a698027bb; page state 2026-10-27T13:21:53.464Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head_read: origin/main 34445a3
reviewed_at: 2026-10-28
pf10_addendum: NONE (INITIAL_DENY creates no PF10 addendum)
next_prompt: CF-E-40 — Revise Epic Specification — 102726.1
next_actor: Isis (same author)
---

# HDE-EPIC041 — Epic Specification review (CF-E-30): INITIAL_DENY

## 1. Decision

**INITIAL_DENY** of `docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md` v1.0.

* Two of the five requirements, R-01 and R-05, have no business case that meets HDE Governance §9.7.7 and Plan Templates §2. Under §9.7.7, "Specification approval blocks a requirement without a business case."
* The Epic-level Business Case leaves out one item that §9.7.7 lists as required, "If not done", and it justifies one beneficiary by conformance to canon.
* Everything else in the Specification is accepted (§4). That covers scope, PF09 mapping, contract posture, open-rails declaration, close-pack baseline, tracked issues and preflight.
* The seven redlines in §3 are exact and bounded. RL-1 to RL-3 are blocking. RL-4 to RL-7 would not block on their own, but the replacement applies them.

Effects of this decision:

* The Specification stays `SPECIFICATION_PENDING`.
* It authorizes no Implementation Audit, Plan, PR, Ops, QA, PF09 movement or closure.
* It creates no PF10 addendum. Initial denial is not a qualifying approval surface.
* Isis returns one complete replacement, v1.1, to this same reviewer (HDE Governance §9.1.1).

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `34445a3`. This branch changes nothing under `docs/pfcanon/`.

Search terms used:

* chart loader, `engine/charts`, `get_chart`, SEPA006;
* business case, beneficiary, "If not done";
* acceptance map, tokenless;
* Production-functional, production-affecting, open-rails;
* precedence, Build Notes citation, addendum;
* Epic Record Template.

| Document (title; file read) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §9.7.7 "Plan approval gate", whole section: "Business Case section required (Epic Specifications)", "Business case for every requirement and work unit", "Template adherence is structural only", "Template-hygiene materiality rule", "Severity mapping", "Truth/proof blockers only", "Specification review boundary" | F-1 to F-3 (blocking); severity of F-4 to F-7; review boundary (no tasks, commands or work units required of a Specification) |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" | Reviewer and author roles; replacement returns to the same reviewer; Specification stays at scope and outcome level |
| HDE Governance | "Production-functional epic live-proof requirement"; "Other production-affecting scope" | Ruling R-B (§4 open-rails declaration) |
| HDE Governance | §2.0.19 "QA bootstrap & harness (EPIC021+)", opening paragraph | Ruling R-A (TI-07) |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §2 "Epic Record Template (Normative)": Meta, Business Case (including "Requirement and work-unit business case"), Contract and Compatibility Posture, Existing Work Check, Deliverables, PF Reference Map, Exact-Source Evidence and Acceptance, QA Rails, Tracked Issues, Specification Preflight A to E; "Artifact execution boundary"; "Canon precedence for template use" | Structural completeness; F-1 to F-3; F-4 (precedence rule); F-5 (Build Notes citation by title); Rulings R-A and R-C |
| HDE Build Checklist — Separation (`PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 (lines 1280 to 1379) | Scope fidelity; source statement that the loader "is not a release member" and "is not reached at runtime" (F-2); source location of R-05's content (F-3) |
| HDE Architecture (`PF02-Canon-HDE-Architecture-v2.4.7.md`) | §1.1 "Non-BodyGraph chart loader classification [Required-Now]" | E-4 is this classification, which makes it conformance-to-canon evidence (F-2) |
| HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`) | "Optional token compatibility"; "Acceptance map — legacy token compatibility shape (clarification)", opening paragraph | Ruling R-A |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`, the current controlled PF10) | Whole document searched by term. Read: "Precedence, versioning, and scope", the Addendum Index, and the one active addendum, on the S19 routed security findings: its decision table and the decisions on the production vendor override scope and on vendor route selection | Build Notes has nothing on the chart loader, `engine/charts`, `get_chart`, HDE-SEPA006, acceptance maps or Business Case. Permanent canon therefore governs every decision topic. The S19 decisions bear on F-6 only |
| Kickoff `docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md` (in-flight) | §10 "Inputs for the Specification's Business Case and requirement business cases"; §7 V-7, V-10 | §10 states "Canon conformance alone is not a business case … the observed incidents in (a) and (b) carry that weight" (F-2). V-10 records the `.audit_src/` copies (F-7) |
| AGENTS.md (repository instruction file) | Canon-first rule; PF canon read-only; evidence attribution | Review procedure only |

Scoped overrides: none. No PF10 addendum and no Product Owner rescope governs any topic decided here.

Silence: canon is silent on one question. It does not say whether a tokenless Epic should still carry an acceptance map. That question is reported, not resolved (Ruling R-A).

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Verification performed by Thoth

Thoth checked the repository facts the Specification relies on, using static reads on `main` `34445a3`. Nothing was executed.

| Spec claim | Check | Result |
| :- | :- | :- |
| E-1: `engine/charts/loader.py` line 81 calls `provider.get_chart`, and the default fixtures provider has no `get_chart` | Read loader lines 1 to 40 and 70 to 90. Grepped `engine/config/provider_loader.py` and both fixtures classes | Confirmed. Line 81 is `provider.get_chart(...)`. `provider_loader.py` imports `engine.provider.fixtures.FixturesProvider` and uses `fixtures` as `DEFAULT_PROVIDER`. That class defines only `get_pair_profile`. A different class, `engine/providers/fixtures_provider.py::FixturesProvider`, does define `get_chart`, but `provider_loader.py` does not import it. Not executed |
| E-2: `artifacts/logs/loader_call.jsonl` is tracked | `git ls-files` | Confirmed tracked. The two current loader tests carry comments saying the loader writes that file relative to CWD and redirect it |
| E-4: 173 lines | `wc -l` | 173 |
| E-5: importers | `grep` for `engine.charts`, `charts.loader` and `load_chart` over `*.py` | Confirmed: `scripts/make_compat_determinism_artifacts.py`, `tests/loader/test_load_chart_fixture_only.py` and `tests/loader/test_loader_logs_keys_only.py`, with none under `engine/` or `adapter/`. The search also found copies under `.audit_src/` (scripts, tests/loader, tests/compat, tests/provider). E-5 does not mention them (F-7) |
| Retained-coverage tests exist | `grep` | Both test functions exist at the named paths. Not run (TI-04 stands) |
| PF10 is v13.9 with one addendum | Read the PF10 file | Confirmed |

## 3. Findings and exact redlines

Severity follows HDE Governance §9.7.7, "Severity mapping".

Each redline names the text to replace or the place to insert. Isis applies all seven to one complete replacement, v1.1, and keeps every other accepted section unchanged (§4). The phrase "consequential renumbering and references" means only the cross-references the redline itself makes stale.

### F-1 / RL-1: Epic-level Business Case (Blocker)

**Defects:**

* The §2.1 Business Case leaves out "If not done: expected consequence or risk". HDE Governance §9.7.7 lists this among the minimum contents that "all MUST be present".
* The Problem statement names a production operator who "carries an Engine whose boundary does not match its documented ownership". That is conformance to canon, which is not a justification. PF09.3 also records that the loader "is not a release member" and "is not reached at runtime", so no production-operator impact is observed.

**RL-1a.** In §2.1 **Problem statement**, replace:

> The people who bear this are the delivery team, who cannot trust or test the chart path as a pure computation, and the production operator, who carries an Engine whose boundary does not match its documented ownership.

with:

> The people who bear this are the delivery team: running or testing the chart path wrote to a tracked repository file through the loader's own call log (E-2), and its legacy-signature path calls a method the default fixtures provider does not define (E-1). PF09.3 records that the loader is not a release member and is not reached at runtime, so no Glow-user or production-operator impact is observed or claimed.

**RL-1b.** In §2.1, insert directly after the **Why now** bullet:

> * **If not done.** The legacy-signature path stays broken against the default fixtures provider (E-1); exercising the loader's call log can again append to the tracked `artifacts/logs/loader_call.jsonl` (E-2); and the defect stays hidden behind a retired test rather than closed (E-3). The source records no user-visible or production consequence, and none is asserted.

### F-2 / RL-2: R-01 business case (Blocker)

**Defects:**

* R-01's only Evidence is E-4. E-4 is the HDE Architecture §1.1 classification of the loader as drift, so it is conformance to canon. Plan Templates §2 and HDE Governance §9.7.7 both say conformance to canon "[is] not a business case".
* The kickoff (§10) says the same thing in its own words.
* The listed beneficiary "production operator" is contradicted by the source: not a release member, not reached at runtime.
* The observed incidents E-1 and E-2 are caused by operational concerns sitting inside the loader. They support R-01, but R-01 does not cite them.

**RL-2.** In §2.4, replace the R-01 row:

> | R-01 Adapter-owned orchestration | Delivery team; production operator | E-4 | Operational concerns (rails, provider choice, acquisition, clocks, correlation, logging, filesystem) have one owner outside Engine, so Engine behavior no longer depends on them | AC-01: the operational concerns are located in Adapter-owned orchestration and absent from Engine chart code; acquisition uses the sanctioned resolver/ingest boundary |

with:

> | R-01 Adapter-owned orchestration | Delivery team | E-1, E-2 (E-4 locates the concerns) | Running or testing the chart path no longer writes a tracked repository file through an operational log inside Engine code (E-2), and provider selection no longer sits in an Engine path that calls a method the default provider does not define (E-1): the operational concerns have one Adapter-owned owner | AC-01: the operational concerns are located in Adapter-owned orchestration and absent from Engine chart code; acquisition uses the sanctioned resolver/ingest boundary. AC-05: running the covering tests leaves tracked files unchanged |

### F-3 / RL-3: R-05 business case (Blocker)

**Defects:**

* R-05's stated Benefit has two limbs. The first is that the claim of preserved behavior "is attributable to an exact tested source"; the second is indexing evidence through the authorized writer. Both are "more complete or more faithful evidence … or records for their own sake", which Plan Templates §2 and HDE Governance §9.7.7 exclude from a business case.
* The preservation limb has no observed incident. E-3 records a retired test and a deferred defect, not a change of caller behavior.
* The content of R-05 is still source-required. In PF09.3 it sits as a dependency and constraint of the Task and of Subtasks .1 and .2 ("Preserve governed caller output and failure behavior"; "Do not introduce fallback data"), and as a Task deliverable ("Required governed evidence is indexed through the existing authorized writer").
* So R-05 is a set of constraints on R-01 and R-03 plus a governed-evidence obligation. It is not a requirement with its own benefit. Restating it that way keeps every source obligation and removes the requirement that has no business case.

**RL-3.** Make these changes:

1. §2.4: delete the R-05 row.
2. §3, requirements table: delete the R-05 row.
3. §3, R-01 requirement text: append the sentence "No fallback data and no additional Engine I/O carve-out is introduced."
4. §3, R-03 requirement text: append the sentence "The migration preserves governed caller output and failure behavior, and applicable CLI/API/Vendor and Mechanics behavior."
5. §3, acceptance-criteria table: change AC-05's **Binds** cell from `R-05` to `R-01, R-03, R-04`.
6. §3: delete the AC-06 row.
7. §8, **Workflow and QA evidence**: append this sentence: "Required governed evidence is indexed through the existing authorized writer, and tested-source attribution is kept distinct from any later evidence-storage commit and from review-time HEAD (PF09.3 Task HDE-SEPA006, 'Deliverables and required evidence'; HDE Schemas and Artifacts). This is a governed-evidence obligation, not a requirement."
8. §8: change "AC-01 to AC-06" to "AC-01 to AC-05" in both places it occurs, **Governing acceptance scope** and **Evidence proportionality**.
9. §6 D4 heading: change "(HDE-SEPA006.3; R-04, R-05)" to "(HDE-SEPA006.3; R-04)".
10. §4 **Backward-compat posture**: change "Mechanics behavior (R-05)" to "Mechanics behavior (R-03)".
11. Apply the consequential renumbering and references. Do not renumber R-01 to R-04 or AC-01 to AC-05.

### F-4 / RL-4: Canon precedence rule absent (Suggestion; non-blocking alone)

**Defect:** Plan Templates, "Canon precedence for template use", says "Every template and derived artifact MUST include this precedence rule". The Specification states the effect of the rule in prose but does not include it. Under the template-hygiene materiality rule this does not change authority, because Build Notes is silent here.

**RL-4.** In §0, insert directly after the "Canon searched and relied on" table, as a block quote:

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

### F-5 / RL-5: Build Notes cited by internal addendum number (Nit)

**Defect:** Plan Templates, "Canon precedence for template use", says: "Cite HDE Build Notes by title alone in current PF prose and derived references, without an internal addendum number, heading, section or file-version locator." The Specification does this three times:

* §0 table: "Addendum 2.1 (S19 routed security findings)";
* §5: "PF10 v13.9 is silent on this topic; its addendum 2.1 is adjacent";
* TI-02: "PF10 addendum 2.1 decisions".

The §0 file identity "v13.9" may stay, because the same rule preserves actual file identities in source-use inventories.

**RL-5.** Make these replacements:

* In the §0 table, replace "Addendum 2.1 (S19 routed security findings) is adjacent, not overlapping (§5, TI-02)" with "Its decisions on the S19 routed security findings are adjacent; they bear on this Epic only as TI-02 states".
* In §5, replace "PF10 v13.9 is silent on this topic; its addendum 2.1 is adjacent (TI-02)." with "HDE Build Notes is silent on this topic; its decisions on the S19 routed security findings are adjacent (TI-02)."
* In TI-02, replace "PF10 addendum 2.1 decisions are item 9's prerequisite" with "HDE Build Notes' decisions on the S19 routed security findings are item 9's prerequisite".

### F-6 / RL-6: Possible Build Notes reach into the new orchestration path (Caveat)

**Defect:**

* R-01 sends any vendor acquisition through the sanctioned BodyGraph resolver/ingest boundary.
* Build Notes' S19 decisions govern exactly that boundary for resolver-selected vendor acquisition: vendor route selection fails closed outside a terminal v1 or v2. They also govern the production vendor override scope for CLI vendor-acquisition paths.
* "Adjacent, not overlapping" is therefore true only while the new orchestration entry performs no resolver-selected vendor acquisition.
* Safe default: TI-02 is already re-checked at the Implementation Audit.

**RL-6.** In TI-02's **Scope** cell, append:

> If the Adapter-owned orchestration entry performs resolver-selected vendor acquisition, HDE Build Notes' decisions on vendor route selection and on the production vendor override scope govern that path; the Implementation Audit determines whether they apply.

### F-7 / RL-7: `.audit_src/` copies not noted in E-5 / TI-03 (Suggestion)

**Defect:**

* Thoth's search found loader-importing copies under `.audit_src/` (`scripts/`, `tests/loader/`, `tests/compat/`, `tests/provider/`). Kickoff V-10 also records them. E-5 and TI-03 omit them.
* R-03 keeps historical audit captures unchanged, so the Audit must classify each copy.

**RL-7.** In TI-03's **Scope** cell, append:

> Copies of the loader's importers and of the retired test under `.audit_src/` (`scripts/`, `tests/loader/`, `tests/compat/`, `tests/provider/`; kickoff V-10) are classified by the Implementation Audit as supported callers or as historical audit captures, which R-03 keeps unchanged.

## 4. Accepted, and rulings on the questions Isis raised

### 4.1 Accepted without change

* **Structure.** Every Epic Record Template section, required gate and the `ASK OK?` sentinel are present (HDE Governance §9.7.7, "Template adherence is structural only").
* **Status `Pending Review`.** This is a template value and is correct for a Specification awaiting review.
* **Scope fidelity to PF09.3 Task HDE-SEPA006 and Subtasks .1 to .3.** Nothing is added or dropped. Non-goals and exclusions are source-stated. The work-item mapping preserves exact identities and states the status nonclaim.
* **Business cases of R-02, R-03 and R-04.** These meet the rule:
  * the beneficiary is the delivery team;
  * the evidence is the observed defects E-1 and E-2 and the observed test retirement E-3;
  * each benefit is stated as risk;
  * each has an after-delivery measure.

  R-04's checks rest on an observed incident (E-2) and on a defect that a retired test left hidden (E-3). They are verification of the change, not internal tooling for its own sake.
* **D-1 / TI-01.** Leaving the repair, retirement or pure-retention choice to the Product Owner is correct. PF09.3 names the Product Owner "this task's decision owner".
  * R-03 and AC-03 hold under any of the three choices.
  * A Specification may leave this choice open, because it does not claim acceptance or closure (§9.7.7, "No scope laundering").
  * The Implementation Audit and Plan need it.
* **Contract and Compatibility Posture.**
  * No public, CLI, provider-contract or HTTP-home change is introduced.
  * Backward-compatibility posture is stated.
  * The vendor-ownership, vendor-normalization, `bg:resolve` and mapped-cache nonclaims are present and correctly scoped.
* **Existing Work Check, Deliverables, PF Reference Map, Exact-Source Evidence, QA Rails, close-pack and doc-delta baselines, and Preflight A to E.** All conform to Plan Templates §2.
  * Every path in §10 uses the canonical `EPIC-###` and lowercase forms.
  * Path-proof filenames are explicit.
  * No QA runbook content is embedded.

### 4.2 Ruling R-A — TI-07, the acceptance map for tokenless work

Isis's stricter reading is correct, and §10's listing of the acceptance map stands.

* Plan Templates Preflight B makes "the epic acceptance map" part of the minimum close-pack baseline, with no condition.
* It also says an Epic Specification is not approvable if it omits that baseline.
* HDE Governance §2.0.19 says an acceptance map is "required only by a separate current scoped requirement". Preflight B is such a requirement.
* HDE Schemas and Artifacts' clarification ("do not require a new acceptance map … for tokenless work") is limited to that clarification's own token-shape rules. It does not lift Preflight B.
* The map carries no token roster, as §10 already states.

Whether tokenless Epics should still need an acceptance map is a canon question. It is not a Specification defect.

* TI-07 stays Open.
* Its disposition is to report the question to the Product Owner as a possible canon change.
* No canon is edited.

### 4.3 Ruling R-B — the §4 open-rails declaration and its binding condition

The declaration is accepted. It conforms to Plan Templates §2 "Open-rails QA declaration" and "Implementation preservation", and to HDE Governance "Production-functional epic live-proof requirement" and "Other production-affecting scope".

* The no-production-functional-surface declaration rests on the source: not a release member, not reached at runtime.
* The declaration is labelled unproven.
* It is bound to a condition: if the Implementation Audit finds production-functional use or deployed or CLI vendor reach, the mandatory synthetic live vendor test applies.
* For the broader production-affecting scope, it keeps the requirement and records no exemption.
* Downstream artifacts must preserve items 3 and 4.
* No live activity is authorized.

### 4.4 Ruling R-C — the evidence is observed defects, not a production incident

This is acceptable.

* Plan Templates requires observed incidents or measurements, and a defect observed in the repository or during a test run qualifies.
* E-1 is canon-cited and confirmed statically. E-2 is canon-cited and confirmed by the tracked file.
* "No production incident" is a truthful nonclaim. It is not a gap.
* What fails is only the two requirements, R-01 and R-05, whose business cases do not rest on that evidence (F-2, F-3).

## 5. Next state and reading for the receiving session

* **Next state:**
  * The Specification stays `SPECIFICATION_PENDING` at v1.0, and its approval sentinel stays `ASK OK?`.
  * Next is CF-E-40, run by Isis. Isis writes one complete replacement, `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md`, and an application report, then returns them to this same reviewer through CF-E-30.
  * If a redline is ambiguous, Isis returns it to Thoth and does not guess.
* **Open items and owners:**
  * D-1 / TI-01: Product Owner.
  * TI-02 to TI-06: the Implementation Audit, after approval.
  * TI-07: report to the Product Owner.
  * None of these blocks the revision.
* **TypeSafe reading for CF-E-40.**
  * Method: installed scoring skill, request v8.2, script run once, session kind `authoring`, label "HDE-EPIC041 CF-E-40 Specification revision". No Notion row was written.
  * Action sent (v8.2): "Revise one pending Epic Specification of about 46 KB that has been reviewed once and denied, by applying seven exact reviewer redlines into one complete replacement version: three rewrite business-case text for the Epic and two of its five requirements, and four are small citation, precedence and tracked-issue additions. A written prompt with steps exists; no code, test or canon change and no live run against a provider occurs. The replacement returns to the same independent reviewer for a second review."
  * As printed: **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.56 (confidence 0.69); rung probabilities low 0.00, medium 0.45, high 0.54, extra high 0.01, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.84, Sonnet 5.5 0.16, Haiku 5.5 0.00 (confidence 0.79). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.378, Opus 5.5 at high 0.454, Opus 5.5 at extra high 0.008, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.072, Sonnet 5.5 at high 0.086, Sonnet 5.5 at extra high 0.002, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between medium and high. Sent 2026-10-28T03:06:29Z. Nathan picks the cell.
  * Picks: Nathan has stated no pick for CF-E-40 and none for this CF-E-30 session, so none is recorded.
* **Surface advice (CF-E-40):**
  * Run it in the continuing Isis role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this review's pull request merges.
  * Needs: read access to `main`, including `docs/pfcanon/` and this review; the CF-E-40 Notion page; write access to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: Notion writes, code or test execution, or production, vendor, Railway or database access.

## 6. Nonclaims

This review establishes none of the following:

* approval of any version;
* an Implementation Audit, Plan, PR, Proceed or merge authority;
* QA, Ops or acceptance;
* PF09 or board movement;
* a canon change, a PF10 addendum or closure.

It also does not edit the reviewed artifact. Merging this file preserves the record and approves nothing (D21-C).
