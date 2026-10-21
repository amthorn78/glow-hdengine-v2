---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-PR-07-PO-DISPOSITION-BUSINESS-CASE
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07 (business case); WU-PR-06 (D-1 measure)
decision_owner: Nathan / Product Owner
decided_at: 2026-10-20, in the Isis Lead Developer session below (recorded 2026-10-20T13:07:49Z)
recorded_by: Isis, continuing Lead Developer for HDE-CRD-0002, session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 (recorder and drafter of the business case; the decisions are the Product Owner's)
decides: decisions 1 and 2 returned to the Product Owner by docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-work-unit-lineage-review-v1.0.md (blob 1b69f1370c80e51c86330824c88faaaa07f7d3b5), as recorded in HDE Build Notes addendum 2.12
repository_head_read: origin/main 043fa914
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (blob 41d5cfd2da6d18aa46351477edb6d6e8a169e0e3); addenda 2.11 and 2.12 read in full
lineage_review_unchanged: yes (v1.0 is not edited; its ACCEPT stands)
pf10_addendum_created: none
---

# HDE-CRD-0002 — Product Owner disposition: WU-PR-07 business case and WU-PR-06 measure (v1.0)

## 1. Product Owner's words (verbatim)

> "adopt the business case, option A, give me the PR-10 handoff"

The business case adopted is the draft Isis gave in the same session, reproduced in §2 without change. Option A is the WU-PR-06 option of addendum 2.11 and lineage review v1.0 (LR6-O1), reproduced in §3.

## 2. Decision 1 — WU-PR-07 business case (addendum 2.11 rule 1): ADOPTED

WU-PR-07 is the seventh unit of Implementation Plan v1.1: S21, the close-pack writer for Epic and CRD identities, the close-run evidence family and the ADR draft. This business case meets addendum 2.12's first returned decision. PR-10 for WU-PR-07 is now runnable.

| Rule 1 field | Adopted text |
| :- | :- |
| Beneficiary | The Product Owner and the delivery team, at every Epic or CRD closure, starting with HDE-CRD-0002's own |
| Evidence | HDE-EPIC040 (2026-09-29). Closure decision v1.0 recorded `CLOSE` at 17:46:21Z, and v1.1 reversed it to `DO_NOT_CLOSE` at 18:39:19Z because no close pack existed. CLOSE01 stopped `STOPPED_TERMINAL` at 18:55:08Z: the generic writer cannot express the close report canon requires (B-1), and no home exists for same-run close evidence (B-2). The epic then closed by Product Owner-authorized exceptional closure (closure decision v1.2, 19:53:33Z), after an extra evidence-landing work unit (QAEV01). HDE-EPIC038: its ordinary closeout also failed. The r5 closeout architecture failed, PR #385 was never merged, and the epic closed by exception (HDE Phased Epics §2.23 and §2.24, GAP-001 and GAP-003) |
| Benefit | Closure completes on the ordinary path. There is no premature `CLOSE`, no stop-and-redesign detour, and no per-change exception authorization from the Product Owner |
| Measure | HDE-CRD-0002 closes through the ordinary Close Gate with the new writer on the first attempt: the close pack is written, every check mode passes, and no exceptional-closure record is needed |
| Cost ceiling | One PR, with review rounds capped by addendum 2.11 rule 8. At most 4 sessions or 3 days from PR-10 to merge. Past that, the unit returns to the Product Owner |

**Evidence sources:**
- `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md`, `-v1.1.md` and `-v1.2.md`;
- `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` §0 and §1;
- `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` §0 to §4 (CC-1 and CC-2, the origin of candidate item 8 and of S21);
- `docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md` §2.23 and §2.24.

**Rule 2 basis** (the Lead Developer's computation from those records, not a forecast). The writer is internal tooling, so rule 2 asks that its expected saving, from observed incident data, exceed its ceiling.
- **Saving per closure.** The HDE-EPIC040 detour took a reversed closure decision, the CLOSE01 session, the lead-developer decision, the QAEV01 work unit and a third closure-decision version: about three sessions beyond an ordinary close, plus one wrong `CLOSE` recorded on `main`.
- **Break-even.** The ceiling is four sessions, so the saving passes it within two closures, HDE-CRD-0002's own and the next one.
- **The other path.** The cheaper options addendum 2.11 names, a canon change to the close-report requirement or keeping exceptional closure, were weighed in the same session. The Product Owner chose the writer. Either alternative would have needed a Specification delta for S21 (addendum 2.12, decision 1).

**How the ceiling is counted.** These are the recorder's implementation readings of the adopted text; the Product Owner may override them.
- **Sessions.** Count the top-level sessions spent on WU-PR-07 from PR-10 to merge: the PR-10 invocation, the PR-20/PR-30 session and the PR-35 session make three. Any further session, or any repeat of a stage, counts toward the four.
- **Days.** Elapsed days run from the start of PR-10 to the merge. Time the unit waits on a Product Owner decision does not count: the Proceed, AQ-1 and the merge itself. The ceiling bounds the work's spend, not the Product Owner's queue.
- **Rule 8 applies as written.** Two consecutive review rounds raising findings of the same class stop the fixing of instances, and the session asks the Product Owner one design question.

**Unchanged:**
- **Approved scope.** S21's scope and acceptance intent (Specification v1.1), and WU-PR-07's design: IF-3, IF-4, the Terminal-state reachability bullet and acceptance items (1) to (7) in Implementation Plan v1.1 §5 and §7.
- **AQ-1.** The Product Owner still approves the S21 ADR before WU-PR-07 merges (Plan v1.1 §13).
- **The rest of addendum 2.11.** Rules 4 to 7 (real inputs, constructed inputs, no emulation of external systems, finding disposition) apply to WU-PR-07's instruction, plan and reviews.

**Gate path (addendum 2.11 rule 3):**
- PR-10 carries this business case and ceiling into the WU-PR-07 instruction;
- PR-20 states how the plan stays within the ceiling;
- the Product Owner gives the Proceed against them;
- PR-40 records the unit's actual cost against the ceiling.

## 3. Decision 2 — WU-PR-06 disposition (postmortem D-1; LR6-O1): OPTION A

- **The measure.** Each remaining HDE-CRD-0002 unit's PR-40 lineage review records any hosted CI failure that a local replay (`python tools/ci/prepush_check.py replay`) would have caught, as addendum 2.11 states option A. The remaining units are WU-PR-07, WU-PR-08 and WU-DOC-01.
- **Stop rule.** If none is recorded by HDE-CRD-0002's QA-10 readiness stage, the replay report is removed in a later change.
- **Owner.** The Implementation Agent records the line in each PR-40 review. The removal decision at QA-10 is the Product Owner's.
- **What this settles.** S20 stays in scope as delivered by #660; no Specification delta is made. The merge of #660 had already ruled out closing it unmerged (option B), and option C (strip the replay) is not taken.
- **Upkeep.** The tool's `ci.yml` SHA-256 pin is updated by any later PR that edits `.github/workflows/ci.yml` (lineage review LR6-O5). No planned unit edits that file.

## 4. Decisions not made here

- **Addendum 2.11's misnumbered cross-references** (addendum 2.12 decision 3; LR6-O2) stay with the Product Owner for a later PF10 version. Until then, each reference is read by the rule its wording describes, using the numbering stated in addendum 2.12.
- **WU-PR-08's S01 real-input fact** (the Railway build command and deploy trigger) is still due before WU-PR-08's PR-10 (addendum 2.12 decision 4).

## 5. Next stage

| Field | Value |
| :- | :- |
| Prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a) |
| Receiving role | The continuing whole-change HDE-CRD-0002 Implementation Agent (session lineage https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah and https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j) |
| `IMPLEMENTATION_PLAN_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (approved) |
| `PLAN_REVIEW_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (IA-30 INITIAL_APPROVE) |
| `WORK_UNIT_ID` | `WU-PR-07` |
| Dependency state | Ready. Plan v1.1 §7: "Seventh; after WU-PR-02 (updater model)". WU-PR-02 is accepted (addendum 2.5); WU-PR-06 is accepted (addendum 2.12); this record supplies the 2.11 business case |
| `EXECUTION_POSTURE` | `MANUAL_PROMPT_EXECUTION` |

### TypeSafe reading for the receiving session (PR-10, WU-PR-07)

Action sent (v8.2): "Write, as the whole-change Implementation Agent, a new PR work-unit instruction for the seventh unit of an approved ten-unit CRD Implementation Plan: a close-pack writer extension for Epic and CRD identities (a new candidate-source schema version, changes to an existing writer of about 3,800 lines with a 4,300-line test file, a new close-run evidence family in the canonical evidence updater, and an ADR draft), carrying an adopted business case and cost ceiling and a terminal-state reachability design already approved in the Plan. A task list exists in the Plan's unit block; no code is written and no live run occurs; a dedicated PR planning session, a Product Owner Proceed and a later lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.07 (confidence 0.70); rung probabilities low 0.04, medium 0.11, high 0.61, extra high 0.22, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.76, Sonnet 5.5 0.20, Haiku 5.5 0.02 (confidence 0.68). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.012, Fable 5.1 at extra high 0.004, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.030, Opus 5.5 at medium 0.084, Opus 5.5 at high 0.464, Opus 5.5 at extra high 0.167, Opus 5.5 at max 0.015, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.008, Sonnet 5.5 at medium 0.022, Sonnet 5.5 at high 0.122, Sonnet 5.5 at extra high 0.044, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.002, Haiku 5.5 at high 0.012, Haiku 5.5 at extra high 0.004, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T13:07:33Z. Flags: none.
- **Detail:** v8.2 sent 2026-10-20T13:07:33Z; HTTP 200 in 0.91 s; 5490 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
- **Nathan's pick for PR-10:** not stated.
- **Notion row:** not written (addendum 2.1).

**Surface advice:** run PR-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role. It reads from `main`:
- this record;
- Implementation Plan v1.1 §5 (IF-3, IF-4), §7 WU-PR-07, §9 and §13;
- Plan review v1.1 §3;
- the Audit's §5.6, §6 S21 and §8;
- `docs/pfcanon/` with PF10 addenda 2.11 and 2.12;
- for the unit's facts: `tools/qa/generate_epic_close_pack.py`, `schemas/epic_close_candidate_source.v1.json`, `tests/qa/test_generate_epic_close_pack.py`, `tools/evidence/update_evidence_index.py` and `.github/workflows/epic-closeout-validation.yml`.

It writes only its instruction artifact under `docs/ephemeral/`, and needs no live vendor, production or database access. This record's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `043fa914`.

- **PF10-HDE-Build-Notes v13.6.3:**
  - addendum 2.11 in full (rule 1 fields; rule 2 internal-tooling test; rule 3 gates; rules 4 to 8; "Epic, task, and status effects", which names WU-PR-07's prerequisite and WU-PR-06's options A to C);
  - addendum 2.12 in full ("Decisions returned to the Product Owner" 1 to 5; "Resume point");
  - addendum 2.1 (TypeSafe reading; no Notion row);
  - addendum 2.5 not re-read; WU-PR-02's acceptance is taken as addendum 2.12 cites it.
- **PF04-Canon-HDE-Governance v2.8.7 §9.1.2:** Product Owner dispositions govern within their scope; in-flight documents are canon for their change.
- **PF06-Canon-Change-Process-Guide v2.5.4 §3.5.1** (read in full on 2026-10-12; `docs/pfcanon/` has changed only in PF10 since): "Exceptional closure record" and the ordinary Close Gate, the closure path the business case concerns.
- **PF20-Reference-HDE-Phased-Epicsv1.9.6 §2.23 and §2.24:** HDE-EPIC038 closeout failure, GAP-001 and GAP-003 (read in the passages cited). §2.21, §2.22 and §2.25 were searched, not read in full, for the close-pack posture of HDE-EPIC036, 037 and 039.
- **PR-10 — Create PR Work-Unit Instructions — 100926.1:** "Resolve the next approved Plan stage", "Inputs", "Managed entry, execution posture and continuing identity".

**In-flight documents read:**
- `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-work-unit-lineage-review-v1.0.md`, through addendum 2.12, which records it;
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` and `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (reviewed and approved by this recorder);
- the HDE-EPIC040 closure records named in §2.

**Repository fact:** `tools/qa/generate_epic_close_pack.py` is 3,869 lines and `tests/qa/test_generate_epic_close_pack.py` is 4,274 lines at `043fa914`.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / Product Owner disposition / WU-PR-07 business case and WU-PR-06 D-1 |
| change | CRD HDE-CRD-0002 |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, Lead Developer, recording Product Owner decisions returned by PR-40 (WU-PR-06) |
| capture time | 2026-10-20T13:07:49Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
