---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.20"
result: MERGE_PENDING (historical pre-merge evidence; the Product Owner merges manually)
phase: PR-35 (review resolution and merge readiness), dedicated session; terminal for PR-35
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.19.md (preserved unchanged); v1.10's MERGE_PENDING was withdrawn by v1.11, and v1.16's by v1.17
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
sessions: PR-30 https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF; PR-35 https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
companion_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/670 (against main; carried by #668; independent merge)
branch: claude/gallant-cerf-ysdde5
reviewed_and_ci_tested_head: 073e5d603691d89da0d86b80b86be6d95360566e
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T15:44:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.20 (MERGE_PENDING)

## 1. Result

**MERGE_PENDING. Ready to merge:** [amthorn78/glow-hdengine-v2#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668).

- **Head:** `073e5d6` is the reviewed and CI-tested head. This record's commit adds only this file under `docs/ephemeral/`, a CI-exempt prefix with no lane.
- **Mergeability:** `clean`, against base `main` `390bc99`.
- **Merge:** the Product Owner's manual action. No agent merges, enables auto-merge or schedules a merge.

This is historical pre-merge evidence. It does not claim a merge, a QA verdict, acceptance, Ops, deployment or closure.

v1.16's `MERGE_PENDING` was withdrawn when round 16 raised findings on that record's own commit. If a review of this record's commit raises a finding, this record is withdrawn in the same way.

## 2. Merge-readiness predicates (glow-hde-pr-development, PR-35)

| Predicate | Evidence |
| :- | :- |
| Approved implementation scope complete | Plan v1.1, delivered at PR-30 (result v1.0). AQ-1 conditions C-1 to C-5 applied (v1.7). Every PR-35 P1, CX7-1 to CX7-10 and CX7-12 to CX7-21, is fixed (v1.1 to v1.19), many under the Product Owner's design decisions PO-35-1 to PO-35-21 |
| Local checks pass on the candidate | Replay of `f458e1f`, which `073e5d6` extends only with `docs/ephemeral/`: all 16 steps, in a mount namespace with `/tmp` as a 2 GB `strictatime` tmpfs, PASS (v1.19 §6) |
| Pushed; the PR reflects the remote head | `cec8367..073e5d6` pushed and read back; PR head `073e5d6` |
| Review findings resolved on the current head | Codex's review of `073e5d6` completed at 15:30:17Z with no findings: its summary comment 6296260293 records `has_any_findings: false`. CX7-20 and CX7-21 were not re-raised, and their threads are resolved. All 21 review threads are resolved. CX7-11 (P2) keeps its stated limit (v1.10 §3) |
| Required CI passes on the current candidate | Run 39623318908, job 119302094074, `test`, success, 15:10:36Z to 15:30:33Z, ubuntu-26.04 image 20261012.163.1, runner 2.338.0 (§4) |
| No unresolved material rescope, dependency or repository conflict | `mergeable_state: clean`. The ceiling is not passed (§6). #669 and #670 have no merge-order dependency with #668 |
| Result and handoff saved and read back | this record |

## 3. Review findings (round 19)

None. Codex reviewed `073e5d6` and reported no findings. The CX7-20 and CX7-21 threads are resolved.

The history across nineteen completed rounds:
- twenty P1s, CX7-1 to CX7-10 and CX7-12 to CX7-21, all fixed. Under PF10 addendum 2.14, none was declined;
- one P2, CX7-11, with a stated limit under addendum 2.11 rule 7.

Three further rounds failed on the Codex usage limit.

The Product Owner's decisions in this phase are PO-35-1 to PO-35-21, each in the record where it was taken (v1.1 to v1.19).

## 4. Hosted CI proof on the current head

Run 39623318908 (job 119302094074), `ci` / `test`: success. The whole job log was read (924 lines).

| Item | Value |
| :- | :- |
| Image | `ubuntu-26.04`, version 20261012.163.1 (Ubuntu 26.04.1 LTS); runner 2.338.0; label `ubuntu-latest` (unpinned) |
| `HEAD_SHA` / `BASE_SHA` | `073e5d603691d89da0d86b80b86be6d95360566e` / `390bc9960a3e9012f67fe7ea39905b624259c87e` |
| Classification | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=36;lanes=product,compat,db,rails,evidence,qa,release` |
| Changed tests | 4,521 passed, 2 skipped |
| Product, compat, db | 77; 119 passed, 3 skipped, 2 xfailed; 269 |
| Rails | four runs: 120, 113, 155 and 138 passed |
| Evidence, qa, release | 134; 488; 79 |
| Final step | `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

Companion #670, run 39526496622 on `606e1b4`: success on ubuntu-26.04, all seven lanes (v1.9 §7).

## 5. In-flight decisions

Every in-flight decision of this work unit is recorded where it was taken, with what changed, why and its test:
- PR-30 result v1.0;
- the PR-35 checkpoints v1.1 to v1.9, v1.11 to v1.15 and v1.17 to v1.19, each in its "In-flight decisions" section.

New in this record: NONE.

## 6. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4, as counted from v1.5 onwards. No new session.
- **Elapsed:** from PR-10's start (2026-10-20T13:14:32Z) to this record, 26 hours 29 minutes with waits included.
  - That includes a gap of about six hours, from about 05:35 to 11:40, while this session's worker restarted.
  - It is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 19 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 22 runs:
  - 17 successes: 6 on ubuntu-24.04, 3 on ubuntu-26.04 with the image read (`c9bff83`, `a2ba526`, `073e5d6`), and 8 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`, `3eb31c3`, `f6e1ad0`, `477570d`, `5bf0db6`, `cec8367`);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-21.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.19 §9)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 115 | 14:56 to 14:57 | Replies on CX7-20 and CX7-21; push `cec8367..073e5d6`; update #668's description; check-in `trig_01Excqvx3bpiZMFAW17WAGkM` armed for 15:48 | pushed and read back |
| 116 | 15:10 to 15:30 | Hosted `test` on `073e5d6` (run 39623318908) | success, all seven lanes, ubuntu-26.04 |
| 117 | 15:30 | Codex review of `073e5d6` | no findings |
| 118 | ~15:41 to 15:43 | Resolve the CX7-20 and CX7-21 threads; read the whole job log; TypeSafe v8.2 reading for the PR-40 handoff (§8) | resolved; read |
| 119 | next | Push this record; update #668's description; re-arm the check-in; the conditional PR-40 handoff goes to the Product Owner | — |

## 8. TypeSafe reading for the PR-40 handoff

The reading, as the scoring skill prints it. It replaces v1.16's reading, because the action text's counts changed.

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.53 (confidence 0.65); rung probabilities low 0.00, medium 0.06, high 0.37, extra high 0.54, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.97, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.011, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.058, Opus 5.5 at high 0.359, Opus 5.5 at extra high 0.524, Opus 5.5 at max 0.029, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.004, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-21T15:42:35Z. Nathan picks the cell.

The action text sent: "Independent post-merge lineage review of one already-reviewed pull-request work unit, HDE-CRD-0002 WU-PR-07 (requirement S21): check against the repository that merged pull request #668 (58 commits, 36 files, about 7,700 added lines, nineteen Codex review rounds, twenty-one Product Owner design decisions recorded in its result records, hosted CI green) and its companion #670 (3 files) delivered the work unit's seven acceptance items from its existing instruction and plan. There is no live run of new code against a provider, and QA and the change's close gate follow as later independent gates."

Advice on the execution surface: a Claude Code session with the repository checked out at `main` after the merge, GitHub read access for the PR, run and review records, and closed rails. The review is read-only on the repository except for its own output artifacts.

## 9. Conditional PR-40 handoff

Use it only after the Product Owner has manually merged #668, and only where no `MERGE_OBSERVED` result was returned for that merge. It is reproduced in the session's final response.

- **This record's `MERGE_PENDING`:** historical pre-merge evidence for head `073e5d6`.
- **The merge:** the Product Owner's own later assertion.
- **PR-40:** verifies the actual merged state and the landed lineage independently. That includes:
  - each Product Owner amendment of the ADR, PO-35-7 to PO-35-21;
  - the PF10 addendum 2.14 check that no P1 on a real input was declined.

## 10. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Merge of #668 | Product Owner | ready (§1) |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| PR-40 lineage review of WU-PR-07 | the whole-change Implementation Agent, after the merge | conditional handoff (§9) |
| HDE-CRD-0002's QA plan maps every S-ID to a check, and its QA report follows the QA-120 form, so its own close can be `SATISFIED` | HDE-CRD-0002's QA planning (QA-50) and QA report (QA-120) | a consequence of PO-35-20 and PO-35-21 (v1.19 §10) |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |
| The undeclared ruby dependency (PF10's open item after the move to Ubuntu 26.04) | Product Owner (documentation delta candidate) | observation recorded in v1.9 §5 |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
