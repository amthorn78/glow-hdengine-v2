---
artifact_type: PRODUCT_OWNER_DIRECTION
artifact_id: HDE-CRD-0002-PO-DIRECTION-QA110-F01-C1-ROUTE
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md (blob a2db4f362bf4; SHA-256 4731f41166ef58facc26159c28a530fa11a19095c3d318492c9c3c08171ba7ae), preserved unchanged. v1.1 replaces it for three reasons (§0)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
subject: the route by which QA Plan v1.2 check 13 is brought in line with the delivered WU-REM-02 change and returned to Kronos for its rerun (remediation of QA110-F01, change C-1)
decision_owner: Nathan / Product Owner
decided_at: 2026-10-25 (UTC), in session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), in answer to the terminal Product Owner return of the WU-REM-02 lineage review; recorded 2026-10-25T15:45:00Z
recorded_by: the continuing whole-change HDE-CRD-0002 Implementation Agent, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), in its read-only PR-40 role. Recorder only; the direction is the Product Owner's
state: IN_FORCE for this decision (§3, §4)
answers: docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-work-unit-lineage-review-v1.0.md §10 (decision ACCEPT; progression TERMINAL_PRODUCT_OWNER_RETURN, DECISION NEEDED; blob 7f0fc054a01e). That review is not edited; its ACCEPT is unchanged
supersedes_for_this_decision_only: the route bullets of change C-1 in docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md §4 and in HDE Build Notes addendum 2.27 "Approved delta", C-1; and addendum 2.28's restatement of that route, in "Required canon drainage" and in its "Deferred obligations" row for C-1 (§5). Nothing else in C-1, in the remediation review, or in addendum 2.27 or 2.28
repository_head_read: origin/main 21141b392eaecb94be0f82044fc1a6713612e089 (PF10 v13.8); the lineage review landed through #735 as a35ccc1
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (568,847 bytes; SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c); addenda 2.27 and 2.28 read in full
pf10_addendum_created: none. The recorder is not an addendum producer, and this record edits no PF file
next_stage: QA-70 — Review Whole-Change QA Plan — 100926.1, Isis (§7)
---

# HDE-CRD-0002 — Product Owner direction: the route for QA Plan v1.2 check 13 after WU-REM-02 (v1.1)

## 0. Why v1.1

1. **v1.0 did not reach `main`.** The Product Owner merged #735 at 2026-10-25T15:43:46Z with one commit, the lineage review (head `1226e19`, squash `a35ccc1`). v1.0 was pushed to that branch afterwards, so it is on no branch that `main` will receive. This version and v1.0 land together through the pull request named in §7. v1.0 is unchanged.
2. **PF10 v13.8 restates the route this direction replaces.** The Product Owner committed PF10 v13.8 at 15:57:01Z (`21141b3`). Its addendum 2.28 records the QA-110 review of 01:26Z. In "Required canon drainage" it says: "A QA Plan v1.2 delta for check 13 step 3's count (C-1 of addendum 2.27): Plan v1.2 is an approved base, so Kronos authors an approved-Plan delta and QA-70 reviews it, not QA-80". Its "Deferred obligations" table also lists "C-1 QA Plan v1.2 delta … Kronos (author, verifier); Isis at QA-70 | Not due". Both restate C-1's route from a source written before the Product Owner's direction. This direction supersedes them for the same decision (§5).
3. **The prompt-ecosystem gap now lives on the GCFPE Modification Backlog** as MB-021 (§7). The Product Owner directed the same day that all GCFPE feedback is consolidated there.

The direction itself (§1, §3) is unchanged.

## 1. Product Owner's words (verbatim)

> "yes, this is a missing route for sure. good catch. This is how I want to handle this:
>
> * Send a request for Isis to review the changes against the current QA Plan (QA-70)
>
> IF the plan needs changes, then it must go to QA-80 and go through that cycle
>
> Either way, it must eventually return to Kronos so the previously failed step instruction can be created with QA-90 for rerun"

## 2. The decision this answers

The WU-REM-02 lineage review accepted the delivered change: #734, squash `22a3bc0`. Its §10 returned one decision to the Product Owner, because no prompt in release 100926.1 authors the route of change C-1.

That route reads:
- Kronos authors a standalone bounded delta to approved QA Plan v1.2 (check 13 step 3, "137 passed" → 141).
- Isis decides it at QA-70 in `APPROVED_QA_PLAN_DELTA_REVIEW` mode.
- It does not go through QA-80.

The owner test count on `main` is 141 (lineage review §8, V-1).

## 3. Direction

| # | Direction |
| :- | :- |
| D-1 | Isis reviews approved QA Plan v1.2 at QA-70 against the delivered WU-REM-02 change, with no Kronos-authored delta before the review. The delivered change is #734, accepted in the lineage review v1.0 |
| D-2 | If the Plan needs changes, Isis returns them as exact redlines to Kronos at QA-80. The QA-80 → QA-70 cycle then runs until Isis approves |
| D-3 | Either way, control returns to Kronos at QA-90 to create the bounded task for check 13's rerun, from the Plan Isis approves: v1.2 as it stands, or its approved successor |

## 4. How the selected prompts apply under D-1 to D-3

This section is the recorder's reading of the direction against the prompt texts read in this session. The receiving roles apply it.

- **QA-70, the first review (D-1).**
  - Binding: `QA_PLAN_ID` docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (approved by QA-70 review v1.2, decision APPROVE, 2026-10-24T14:52:19Z).
  - Mode: QA-70 requires exactly one `REVIEW_MODE`, and neither of its modes covers an approved Plan reviewed with no proposed delta. By this direction the review takes `REVIEW_MODE: INITIAL_QA_PLAN_REVIEW` and that mode's decision states and routing, because D-1 to D-3 are exactly that routing:
    - `APPROVE` → QA-90 in the continuing Kronos context;
    - `DENY` with exact redlines → QA-80 in the same Kronos author context.
  - The bytes of approved Plan v1.2 are never edited. A revision is a successor file.
- **QA-80 (D-2).**
  - By this direction, approved Plan v1.2, or a pending successor of it, is QA-80's target for this decision. QA-80 does not return `WRONG_ROUTE_APPROVED_BASE` here.
  - Kronos produces a complete successor QA Plan, the next version, and a redline application report. The state is `PLAN_PENDING_REVISED`, back to the same Isis at QA-70 in `INITIAL_QA_PLAN_REVIEW`, as QA-80 routes it.
- **QA-90 (D-3).**
  - On `APPROVE`, the continuing Kronos creates check 13's bounded rerun task from the approved Plan. This is the remediation return: addendum 2.27 V-6; Glow QA Guide §10.6 "Common remediation cycle and return owner", step 5.
  - Unchanged by this direction:
    - C-1's "It is not an ordinary attempt 2 (escalation report §12)";
    - Glow QA Guide §10.6's "Nominal remediation cycles must not reset attempts or bypass that limit";
    - attempt accounting, which stays Kronos's.
  - The other checks' recorded results are not reopened by this direction.
- **Unchanged, apart from the route:**
  - the rest of C-1, including "Check 13's objective, target, step 1, 2 and 4 predicates and outcome map are unchanged" (remediation review §4), as Isis approved it at ESC-40;
  - the rest of addendum 2.27.

  A redline beyond step 3's count is Isis's to ground in evidence against that approval.

## 5. What this supersedes, and the consequences

| Superseded for this decision only | Text | Replaced by |
| :- | :- | :- |
| Addendum 2.27 C-1; remediation review v1.0 §4 | "Kronos authors the delta"; "Isis decides it at QA-70 in APPROVED_QA_PLAN_DELTA_REVIEW mode, and its qualifying approval produces its own addendum"; "The delta does not go through QA-80, which revises only pending Plans" | D-1, D-2 |
| Addendum 2.28 (PF10 v13.8), "Required canon drainage" and "Deferred obligations" | "Plan v1.2 is an approved base, so Kronos authors an approved-Plan delta and QA-70 reviews it, not QA-80"; the C-1 row "Kronos (author, verifier); Isis at QA-70" | D-1, D-2. Kronos stays the verifier of check 13 (V-6) under D-3 |
| QA-70 — Review Whole-Change QA Plan — 100926.1 | Delta DENY: "Do not send the approved base to QA-80 as a rewrite request"; the two-mode rule as it applies to an approved base with no delta | §4, QA-70 |
| QA-80 — Revise Whole-Change QA Plan — 100926.1 | "never revises an already approved QA Plan"; `WRONG_ROUTE_APPROVED_BASE` | §4, QA-80 |

**Consequences:**
- **No PF10 addendum records the Plan change.**
  - QA-70's initial mode produces none, but the delta approval C-1 expected would have produced one.
  - The change to check 13 is recorded instead in QA-70's review, in any successor Plan with its redline application report, and in this record.
  - Addendum 2.27 is not edited, and it still names the delta route. This record supersedes that route for this decision.
- **Thoth's original route is close to this one.** Proposal v1.0 §11 item 5 read "revised first through QA-80 and QA-70", and the remediation review's C-1 replaced it. This direction restores a QA-70-first form of it by Product Owner decision.
- **The lineage review v1.0 stays as issued.** Its terminal return is answered here.

## 6. Canon-conflict register

**Carried unchanged** (lineage review v1.0 §11):

| ID | Status | Decision owner |
| :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED | Thoth |
| CR-4 | APPROVED | Product Owner |
| CR-5 | APPROVED_AS_CHANGED | Product Owner |
| CR-6 | APPROVED (a) | IA through RS-20 |
| CR-7, CR-8 | APPROVED (a) each | Product Owner |
| CR-9 | PROPOSED, not yet reviewed | Isis (IA-30) |
| CR-10 | APPROVED (a) | Isis (ESC-40) |
| CR-11 | APPROVED_AS_CHANGED (a) | Isis (QA-70 review v1.0) |

**New entry CR-12:**

| Field | Value |
| :- | :- |
| ID | CR-12 |
| Classification | Route conflict: a Product Owner direction against an HDE Build Notes rule (addendum 2.27 C-1) and the QA-70 and QA-80 prompt texts, for one decision |
| Sources | PF10 v13.8 addendum 2.27 "Approved delta", C-1, and addendum 2.28 "Required canon drainage" and "Deferred obligations"; docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md §4 (blob 324ab0552f02); QA-70 and QA-80, release 100926.1, as §5 quotes them |
| Conflict | C-1 requires a Kronos-authored delta, a QA-70 delta-mode decision and no QA-80. No prompt in release 100926.1 authors such a delta (lineage review v1.0 §10). The Product Owner directs QA-70 first, QA-80 if changes are needed, then QA-90 |
| Affected | S20; QA Plan v1.2 check 13; the QA-70, QA-80 and QA-90 stages for check 13 |
| Alternatives | (a) the Product Owner's route, D-1 to D-3; (b) C-1's delta route, once a prompt that authors an approved-Plan delta is named |
| Disposition | (a) |
| Interim treatment | This record |
| Unresolved risk | No PF10 addendum records the Plan change (§5) |
| Permanent drainage | No PF canon change proposed by the recorder. The prompt-route gap goes to the GCFPE-MGMT-10 maintenance owner (§7) |
| Status | APPROVED |
| Decision owner and time | Nathan / Product Owner, 2026-10-25 (UTC) |
| Reviewed artifact | docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-work-unit-lineage-review-v1.0.md §10 |
| History | Proposal v1.0 §11 item 5: QA-80 then QA-70 (Thoth). Remediation review v1.0 C-1: delta, QA-70 delta mode, no QA-80 (Isis, ESC-40, APPROVE_AS_CHANGED). Lineage review v1.0 §10: the delta has no author prompt (the IA, PR-40). Direction v1.0: (a) (Product Owner). Addendum 2.28 (PF10 v13.8, committed after the direction) restates C-1's route from the QA-110 review of 01:26Z. Direction v1.1: (a) stands, and supersedes that restatement for this decision |

## 7. Prompt-ecosystem report and next stage

**Report to the GCFPE-MGMT-10 maintenance owner.**
- **Prompt identity:** release GCFPE-20261009.1 / 100926.1; QA-70, QA-80 and QA-90.
- **Expected:** a route for a material change to an approved QA Plan that a remediation makes necessary.
- **Actual:**
  - QA-70 reviews a standalone delta but names no prompt that authors one;
  - QA-80 revises only pending Plans;
  - QA-50 authors initial Plans;
  - QA-90 and QA-110 work on tasks and evidence.
- **Evidence:** lineage review v1.0 §10.
- **Interim treatment:** this direction.
- **Where it is recorded:** the GCFPE Modification Backlog (Notion page `3e54590a05eb81eb818fd0f42045167a`), entry MB-021, S2, OPEN. It was written and read back on 2026-10-25, on the Product Owner's instruction that all GCFPE feedback is consolidated there.

**Next stage.** QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf).
- **Reviewer:** Isis (Isis-53), the continuing Lead Developer and QA Plan decision owner (execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok).
- **Plan author:** Kronos (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV).
- **Order:** this record and v1.0 reach `main` through their own pull request (the one that carries this file; the lineage review is already on `main` through #735) before QA-70 starts.

## 8. TypeSafe reading for the receiving session (QA-70)

Carried unchanged from v1.0. The receiving session and its work are the same, and the skill takes one reading per receiving session, so it was not run again.

Action sent (v8.2): "As the continuing QA Plan reviewer, re-review one already approved whole-change QA Plan (about 730 lines, 15 checks) against a three-file remediation change that has merged and passed its lineage review, under a recorded Product Owner routing direction, and decide whether the one affected check (a pre-push tool check whose expected test count no longer matches) needs Plan changes: approve the Plan as it stands or deny it with exact redlines, written as a Markdown review record. No code is changed, no task list exists and no live run against a provider occurs; a Plan revision and a fresh review follow a denial, and a bounded QA task, its execution and an independent evidence review follow approval."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.09 (confidence 0.76). Rung probabilities: low 0.00, medium 0.14, high 0.65, extra high 0.20, max 0.01, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.93, Sonnet 5.5 0.05, Haiku 5.5 0.00 (confidence 0.91).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.130, Opus 5.5 at high 0.605, Opus 5.5 at extra high 0.186, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.007, Sonnet 5.5 at high 0.033, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - **Flags: none.**
  - Sent 2026-10-25T15:42:31Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-25T15:42:31Z; HTTP 200 in 0.58 s; 5484 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review`, before v1.0 was saved.
- **Records:** the Notion row was not written. Nathan's pick for the QA-70 session is not stated.

**Surface advice:** run the review in the continuing Isis context for HDE-CRD-0002 (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), or in a top-level Claude Code cloud session Nathan creates for that role. It works on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt.
- **Reads:**
  - Plan v1.2 check 13 and its QA-70 review v1.2;
  - this record;
  - the lineage review;
  - the remediation review with the addendum record;
  - the QA-110 evidence review and the escalation report;
  - the three landed files on `main`.
- **Optional re-run:** only the owner test of step 3, in a throwaway clone with CI's install under closed rails. Step 1's full command took about 24 minutes in the Plan's own observation (check 13), and nothing in D-1 needs it.
- **Writes:** only the QA-70 review and its handoff under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.

## 9. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-PR-40-20261025-WU-REM-02-02` (continuation of `…-PR-40-20261025-WU-REM-02-01`, the lineage review) |
| Change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| Requirement / work unit | S20; WU-REM-02; QA Plan v1.2 check 13 |
| Prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1 (its terminal Product Owner return answered); QA-70 and QA-80, page states of 2026-10-12T02:29:54.691Z and 2026-10-12T02:30:18.516Z, read as the receivers' contracts |
| Release | GCFPE-20261009.1 / 100926.1 |
| Role and stage | whole-change IA, read-only PR-40, recording a Product Owner direction |
| Capture time | 2026-10-25T15:45:00Z (v1.0); 2026-10-25T16:25:00Z (v1.1) |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |
| Repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |

## 10. Nonclaims

This record makes no QA Plan decision: whether check 13 needs a change, and which, is Isis's at QA-70.

It also establishes none of the following:
- a task, an attempt or a QA verdict;
- acceptance, Ops, deployment, drainage or closure.

It edits no PF canon, Plan, review, code, test, workflow or governed evidence.

## Canon relied on

Read on `main` at `21141b3`. PF10 is v13.8. v1.0 read v13.7.9 at `22a3bc0`.

| Decision topic | Sources and sections |
| :- | :- |
| The decision answered; ACCEPT preserved | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full in this session: "Resolve the next approved Plan stage", "TERMINAL OR MANUAL-PREREQUISITE RETURN", "Mandatory single-block handoff"; lineage review v1.0 §10 |
| C-1 as approved, and what stays | HDE Build Notes v13.8 addendum 2.27, read in full ("Approved delta" C-1, "Verification" V-6, "Unresolved obligations and owners"); docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md §4 and §3 row 12 |
| The later restatement of C-1's route | HDE Build Notes v13.8 addendum 2.28, read in full: its "Required canon drainage", "Deferred obligations and unresolved work", "Epic, task, and status effects" and "Relationship to existing HDE Build Notes guidance" ("Supersedes nothing and amends no earlier addendum"). It records QA-110 and PR-35 source documents that predate the Product Owner's direction |
| A bounded Product Owner decision superseding canon for one decision | `AGENTS.md` "Canon-first rule" ("a formally approved bounded Product Owner rescope supersedes it for the exact decision it adjudicates") and "PF canon is read-only unless the prompt explicitly directs a change" |
| QA-70 modes, decision states and routing | QA-70 — Review Whole-Change QA Plan — 100926.1, read in full: "Required inputs and review mode", "Execute and decision criteria", "Required result and routing", "Runtime artifact and handoff contract" |
| QA-80 target and routing | QA-80 — Revise Whole-Change QA Plan — 100926.1, read in full: "Role and native purpose", "Controlled sources, overlays, and revision boundary", "Execute", "Required result and routing" |
| Return owner; attempts; failure visibility | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6, read in full ("Common remediation cycle and return owner" step 5 and the attempt-limit paragraph; "Evidence-package caveats and failure history") |
| Check 13 as approved | docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md "CHECK 13 `qa-13-prepush-check`" (blob 66f6016cc75b); docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md front matter (blob 502412897d6a) |
| Searched, silent | `git grep -i -E 'APPROVED_QA_PLAN_DELTA\|QA Plan delta\|delta to (an \|the )?approved QA Plan\|approved-Plan delta\|QA-80' origin/main -- docs/pfcanon/` returns only addendum 2.27 (lines 3013, 3016 and 3064). That addendum names Kronos as the author role but names no authoring prompt. The Glow QA Guide §10.6 leaves Plan responsibility with Kronos and also names no prompt. The gap is a prompt-ecosystem gap (§7) |
