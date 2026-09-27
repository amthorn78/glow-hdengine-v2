---
artifact_type: QA_PLAN_APPROVAL_REVOCATION
artifact_version: "1.0"
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
revoked_decision: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.2.md (QA_PLAN_REVIEW v1.2, APPROVE of QA Plan v1.1; SHA-256 66ab1331ac3fb5713f487d61841c9dc16fd26fc718e29eb9765515de3eb7e77d)
authority: Product Owner, 2026-09-27 ("Revoke the plan approval, That is abject failure.")
recorded_by: Isis-51, author of the revoked review (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq)
plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.1.md (QA_PLAN v1.1; SHA-256 769e64e27685622e02996d1e19e4995c3893fe769f00a4fe0370b8fddc98e5a5); state after this record PLAN_PENDING_REVISED, not approved
plan_author: Kronos-23 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
void_handoff: docs/ephemeral/HDE-EPIC040-QA70-handoff-to-qa90-v1.0.md (SHA-256 3de0c1915b56ff9035580dd0ce8ec886d49600dee90c26c69e3cd2e899f8c66a)
next_review: QA-70 — Review Whole-Change QA Plan — 091426.1, run by Isis-52 (docs/ephemeral/HDE-EPIC040-QA70-handoff-to-qa70-isis52-v1.0.md)
alpha_feedback: docs/ephemeral/GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md
recorded_date: 2026-09-27
---

# HDE-EPIC040 — QA-70 approval of QA Plan v1.1 revoked

## 1. Revocation

On 2026-09-27 the Product Owner revoked the `APPROVE` in QA Plan Review v1.2. QA Plan v1.1 is **not approved**. It returns to `PLAN_PENDING_REVISED`, the state QA-80 left it in, and goes to a new QA-70 review run by Isis-52.

The Product Owner, verbatim:

> "this hardly looks like a coherent plan at all. You have tasks that do nothing and an empty one. How is this even remotely approvable?"

> "Revoke the plan approval, That is abject failure."

## 2. What the approval accepted

These are facts in Plan v1.1, by line:

| Item | Fact |
| --- | --- |
| Check 13 `live-db-reader-refusal` | Removed, but kept as a numbered heading and matrix row. It has no executor, command or evidence (L355, L823–L825) |
| Checks 12 and 14 | Run no command. Each block holds only a `PARKED` record that the QA/infra executor writes (L354, L356, L803–L821, L827–L845) |
| Collection | Counted as 14 checks. Two of them run nothing (L399) |

Why review v1.2 missed them:

- It checked that each of review v1.1's 13 redlines had been applied (§2), and checked the new code claims (§3). It did not judge the whole Plan again.
- It stated "In the text that QA-80 changed, I found no blocker" (§4). Checks 12 to 14 are text that QA-80 changed.
- The `PARKED` form of checks 12 and 14 came from the reviewer's own redline RL-09 in review v1.1 ("No commands, inputs or probes"). The reviewer approved the result of its own redline without testing it against canon.

This record decides nothing about the Plan. The new QA-70 decides what is a blocker. The canon tests that apply are listed under "Canon relied on". RL-09's choice to make the deferrals into checks was the reviewer's, not canon's. Glow QA Guide §3.3 requires only that a requirement blocked by the pre-App environment be "explicitly called out in epic-level QA plans and deferred". Review v1.1's redlines therefore do not bind the form a coherent Plan takes.

## 3. Effect

| Item | Effect |
| --- | --- |
| Review v1.2 | Its `APPROVE` is revoked. The file stays as a historical record, because an issued version is never edited. Its note N-01 and its verification tables are evidence only |
| QA-90 handoff | `docs/ephemeral/HDE-EPIC040-QA70-handoff-to-qa90-v1.0.md` is void. No QA-90 task, and no QA-100 or later work, may derive from it or from review v1.2 |
| Unchanged | QA Plan v1.1 and the QA-80 redline application report, as Kronos-23 authored them. Review v1.1 (the DENY of Plan v1.0) and its findings. The QA Audit, Live QA Guide, readiness, PO disposition and RCA v1.1 |
| Reviewer | At the Product Owner's direction, Isis-52, a new version of this Isis session, runs QA-70 on Plan v1.1. Isis-51 makes no further QA-70 decision on this Plan |
| Alpha | The Epic stays at QA-70. The stop record `docs/ephemeral/HDE-EPIC040-alpha-state-stopped-failed-at-qa-v1.0.md` named QA-70 as the resume point. The Product Owner restarted QA-70 on 2026-09-27 (review v1.1, `restart_authority`) and has now directed a second QA-70 in Isis-52. No new stop is declared and no state token is minted |
| Prompt failure | Reported as Alpha feedback in `docs/ephemeral/GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md` |

## Canon relied on

Read from `docs/pfcanon/` on `main` (`bf6e8da`):

- **Plan Templates** (`PF27-Canon-Plan-Templates-v2.0.4.md`): "Evidence coverage and optional legacy-token binding". Every check block MUST be an explicit evidence requirement with a mechanical PASS/FAIL predicate and the evidence captured for it, and a Live QA Plan MUST NOT include a check "for good measure". Also "Live QA Plan approval materiality discipline" and "Review stability and no-moving-target discipline", both read in full.
- **Glow QA Guide** (`PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.3, the pre-App deferral of user-bound requirements. §3.4.8, which says closed-rails testing remains the responsibility of CI and pre-merge QA. §3.4.14, the minimum viable Live QA plan: every criterion is covered by a step, and information that GitHub or a governed artifact already records is not duplicated.

Other sources:

- **Alpha state rule:** decision D18 and its 2026-09-23 successors (`docs/prompt_ecosystem_management/gcfpe.decision-record.md`). Alpha state is what the Epic's own artifacts under `docs/ephemeral/` record.
- **QA-70 prompt** (091426.1; Notion page as of 2026-09-24T15:55:17.352Z; read in full): "Execute and decision criteria" steps 1 and 2; "Runtime artifact and handoff contract" (an issued version is never edited).
- **In-flight documents, read in full:** Plan v1.1, review v1.1, review v1.2, the QA-80 redline application report and the Alpha state record v1.0.

## Nonclaims

This record makes no QA-70 decision on Plan v1.1. It issues no redlines, selects no task, executes no QA, produces no PF10 addendum and edits no prompt. Merging it preserves the record and approves nothing (D21-C).
