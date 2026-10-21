---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.10"
result: MERGE_PENDING (historical pre-merge evidence; the Product Owner merges manually)
phase: PR-35 (review resolution and merge readiness), dedicated session; terminal for PR-35
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.9.md (preserved unchanged)
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
reviewed_and_ci_tested_head: c9bff839a34cc9dfaf2f4e61f6bd0b59dda1931a
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T02:20:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.10 (MERGE_PENDING)

## 1. Result

**MERGE_PENDING. Ready to merge:** [amthorn78/glow-hdengine-v2#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668).

- **Head:** `c9bff83` is the reviewed and CI-tested head. This record's commit adds only this file under `docs/ephemeral/`, a CI-exempt prefix with no lane.
- **Mergeability:** `clean`, against base `main` `390bc99`.
- **Merge:** the Product Owner's manual action. No agent merges, enables auto-merge or schedules a merge.

This is historical pre-merge evidence. It does not claim a merge, a QA verdict, acceptance, Ops, deployment or closure.

## 2. Merge-readiness predicates (glow-hde-pr-development, PR-35)

| Predicate | Evidence |
| :- | :- |
| Approved implementation scope complete | Plan v1.1, delivered at PR-30 (result v1.0). AQ-1 conditions C-1 to C-5 applied (v1.7). The PR-35 corrections CX7-1 to CX7-10 and the schema-field audit are fixed (v1.1 to v1.9) |
| Local checks pass on the candidate | Replay of tree `1f9a160d…` (the tree of `cf39b95`, which `c9bff83` extends only with `docs/ephemeral/`), all 16 steps, in a mount namespace with `/tmp` as a 2 GB `strictatime` tmpfs: PASS (v1.9 §7) |
| Pushed; the PR reflects the remote head | `0b57143..c9bff83` pushed and read back; PR head `c9bff83` |
| Review findings resolved on the current head | Codex review 5594053557 on `c9bff83`. CX7-10 was not re-raised, and its thread is resolved. One P2, CX7-11, has a stated limit under addendum 2.11 rule 7 (§3). All 11 review threads are resolved |
| Required CI passes on the current candidate | Run 39529557115, job 118992072816, `test`, success, 01:49:55Z to 02:10:33Z, ubuntu-26.04 image 20261018.168.1, runner 2.338.0 (§4) |
| No unresolved material rescope, dependency or repository conflict | `mergeable_state: clean`. The ceiling is not passed (§6). #669 and #670 have no merge-order dependency with #668 |
| Result and handoff saved and read back | this record |

## 3. Review findings (round 9)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-11 | Codex, `c9bff83`, P2 (thread `PRRT_kwDOP103ks6umHi1`, comment 4332264364) | `tools/evidence/update_evidence_index.py`, CRD close-pack registration | Tracked symlinks at both CRD close-pack paths would be registered, and their target bytes attested | No. The writer is the pair's only producer and installs regular files. No CRD close pack exists on `main`. A symlink there needs a hand-committed governed artifact, which AGENTS.md forbids, and the writer's `--check` refuses it (`OUTPUT_TARGET_NOT_REGULAR`, `OUTPUT_PARENT_ALIASED`) | Stated limit (addendum 2.11 rule 7; P2, not security, so not first to the Product Owner); thread answered and resolved |

The review history across nine rounds: ten P1s, CX7-1 to CX7-10, all fixed, and one P2, CX7-11, with a stated limit. Two further rounds failed on the Codex usage limit.

## 4. Hosted CI proof on the current head

Run 39529557115 (run 3793), job 118992072816, `ci` / `test`: success. The whole job log was read from the run's log archive.

| Item | Value |
| :- | :- |
| Image | `ubuntu-26.04`, version 20261018.168.1; runner 2.338.0; label `ubuntu-latest` (unpinned) |
| `HEAD_SHA` / `BASE_SHA` | `c9bff839a34cc9dfaf2f4e61f6bd0b59dda1931a` / `390bc9960a3e9012f67fe7ea39905b624259c87e` |
| Classification | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=26;lanes=product,compat,db,rails,evidence,qa,release` |
| Changed tests | 4,143 passed, 2 skipped |
| Product, compat, db, rails | 77; 119 passed, 3 skipped, 2 xfailed; 269; 138 |
| Evidence, qa, release | 134; 488; 79 |
| Final step | `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

Companion #670, run 39526496622 on `606e1b4`: success on the same image, all seven lanes (v1.9 §7).

## 5. In-flight decisions

Every in-flight decision of this work unit is recorded where it was taken, with what changed, why and its test:
- PR-30 result v1.0;
- the PR-35 checkpoints v1.1 to v1.9, each in its "In-flight decisions" section; v1.9 §8 holds the ID-16 rows for the ubuntu-26.04 fixes and for merging #670's head ahead of its merge.

New in this record: NONE.

## 6. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4, as counted in v1.5 to v1.9. No new session: #670 was opened from this PR-35 session.
- **Elapsed:** from PR-10's start (2026-10-20T13:14:32Z) to this record (2026-10-21T02:20Z), 13 hours 6 minutes of wall clock with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 9 completed, plus 2 that failed on the usage limit.
- **Hosted CI on #668:** 12 runs:
  - 7 successes: 6 on ubuntu-24.04 (`f42dd52`, `a6c6655`, `c1a41b4`, `5d04297`, `ca8c3cc`, `0d50b06`) and 1 on ubuntu-26.04 (`c9bff83`);
  - 4 failures on ubuntu-26.04 (`45e4cef`, `b0a7305`, `abc0254`, `0b57143`);
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-9.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.9 §10)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 66 | 01:49 | Reply on CX7-10; push `0b57143..c9bff83`; update #668's description | pushed and read back (v1.9 sha256 a992c90d…) |
| 67 | 01:49 to 02:10 | Hosted `test` on `c9bff83` (run 39529557115) | **success**, all seven lanes, ubuntu-26.04 |
| 68 | 01:59 | Codex review 5594053557 on `c9bff83` | CX7-11 (P2); CX7-10 answered |
| 69 | ~02:01 | Reply on CX7-11 with the stated limit; resolve the CX7-11 and CX7-10 threads | resolved; 11 of 11 threads resolved |
| 70 | 02:11 | TypeSafe v8.2 reading for the PR-40 handoff (§8) | read |
| 71 | next | Push this record; the conditional PR-40 handoff goes to the Product Owner | — |

## 8. TypeSafe reading for the PR-40 handoff

The reading, as the scoring skill prints it:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.49 (confidence 0.63); rung probabilities low 0.00, medium 0.07, high 0.39, extra high 0.52, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.98, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.005, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.069, Opus 5.5 at high 0.382, Opus 5.5 at extra high 0.510, Opus 5.5 at max 0.020, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.004, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-21T02:11:38Z. Nathan picks the cell.

The action text sent: "Independent post-merge lineage review of one already-reviewed pull-request work unit, HDE-CRD-0002 WU-PR-07 (requirement S21): check against the repository that merged pull request #668 (31 commits, 25 files, about 4,900 added lines, nine Codex review rounds, hosted CI green) and its companion #670 (3 files) delivered the work unit's seven acceptance items from its existing instruction and plan. There is no live run of new code against a provider, and QA and the change's close gate follow as later independent gates."

Advice on the execution surface: a Claude Code session with the repository checked out at `main` after the merge, GitHub read access for the PR, run and review records, and closed rails. The review is read-only on the repository except for its own output artifacts.

## 9. Conditional PR-40 handoff

Use it only after the Product Owner has manually merged #668, and only where no `MERGE_OBSERVED` result was returned for that merge. It is reproduced in the session's final response.

- **This record's `MERGE_PENDING`:** historical pre-merge evidence for head `c9bff83`.
- **The merge:** the Product Owner's own later assertion.
- **PR-40:** verifies the actual merged state and the landed lineage independently.

## 10. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Merge of #668 | Product Owner | ready (§1) |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| PR-40 lineage review of WU-PR-07 | the whole-change Implementation Agent, after the merge | conditional handoff (§9) |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |
| The undeclared ruby dependency (PF10's open item after the move to Ubuntu 26.04) | Product Owner (documentation delta candidate) | observation recorded in v1.9 §5: ruby present on ubuntu-26.04 |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
