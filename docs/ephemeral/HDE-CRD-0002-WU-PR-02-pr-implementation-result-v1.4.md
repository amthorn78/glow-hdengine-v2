---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.4.md
artifact_version: "1.4"
result_state: MERGE_PENDING
artifact_state: MERGE_PENDING — historical pre-merge evidence; not a claim that the PR is merged
phase: PR-35 (review resolution and merge readiness)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.3.md (v1.3, PR-35 checkpoint for the third corrective push; blob 320fa002afa856e4f19d90361be3d8d70c3d962e). Preserved unchanged; v1.0 to v1.2 likewise
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d92f90b3389d56d498f12964a91a9)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5804a88bcf861f45ea24d8846288f)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0) — lineage only
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain), as planned by PR_IMPLEMENTATION_PLAN_ID v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112da05bbcc9fae7316f64d1657824ff; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this PR-35 session; unchanged on main 0cd7b84 and on the branch)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (reviewer chain) and § 2.1 (TypeSafe reading)
pf10_addendum_created: none (PR-35 is not a qualifying approval prompt)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0 (Nathan's PR-30 invocation naming plan v1.0). PR-35 continued under it; no other Proceed exists or was requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-02 PR-35 session, https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK; session_disposition NEW_DEDICATED; role_session_ref NOT_YET_ASSIGNED (Nathan assigns). PR-20/PR-30 session: https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/intelligent-cannon-32u7tl; pull request amthorn78/glow-hdengine-v2#634 (open, not draft, base main 0cd7b843462df94273bb686def5e4a353d0b98ba)
verified_candidate: 433c1a561f9f37a8b601808a721b8746c83db18a (v1.3 checkpoint commit; its code tree equals a028b0c, the last code commit: git diff a028b0c 433c1a5 adds only docs/ephemeral/…-result-v1.3.md)
record_commit: the commit that adds this file, on top of 433c1a5; it changes only docs/ephemeral/. Its own identity is not written into itself; its hosted CI and Codex summary are read by this session after the push and reported in the MERGE_PENDING return
created_at: 2026-10-13T20:21:00Z
---

# HDE-CRD-0002 WU-PR-02 — PR implementation result v1.4 (PR-35, MERGE_PENDING)

## 1. Result

**MERGE_PENDING — Ready to merge**, for [amthorn78/glow-hdengine-v2#634](https://github.com/amthorn78/glow-hdengine-v2/pull/634) at the verified candidate `433c1a5`. Four Codex code-review findings were raised across three reviewed heads: CX-1, CX-3 and CX-4 are corrected and CX-2 is an accepted residual by the Product Owner's decision. The Codex code review of `433c1a5` is clean, every review thread is resolved, required hosted CI on `433c1a5` passes, local checks pass on its code tree, and the PR is open and mergeable with no conflict (§2). This record's own commit changes only `docs/ephemeral/`; its CI is read before the return and reported there.

This is historical pre-merge evidence. Nathan / Product Owner merges manually. No agent merges, enables auto-merge or schedules a merge. PR-40 independently verifies the merged state and landed lineage after the merge.

## 2. Readiness predicates (PR-35 "Genuine merge-readiness gate")

| Predicate | Evidence on `433c1a5` | Holds |
| :- | :- | :- |
| Every applicable current-head review read; every required substantive finding resolved or lawfully waived | Codex code review summary (issue comment 6152304678): Code Review completed 2026-10-13T20:09:54Z on `433c1a5`, trigger "New commits"; no new Codex review or review comment on `433c1a5` (the last Codex review, 5509067586, is on `e7ec65f`); one 👍 reaction on the PR, whose `updated_at` moved to 2026-10-13T20:09:55Z with the summary's completion (Codex "reacts with 👍 once all reviews finish with no findings"; the reactor identity was not read). CX-1, CX-3, CX-4 corrected; CX-2 accepted residual by Product Owner decision (v1.2 §3.1). Codex security review not part of the chain (PF10 addendum 2.3) | yes |
| No required review thread unresolved | 4 threads, 4 resolved: `PRRT_kwDOP103ks6sAH60` (CX-1), `PRRT_kwDOP103ks6sA712` (CX-2), `PRRT_kwDOP103ks6sA719` (CX-3), `PRRT_kwDOP103ks6sCFjw` (CX-4) | yes |
| Required current-head CI passes | check `test`, run 38460145263 / job 115512888315 on `433c1a5`: success 2026-10-13T20:06:16Z–20:16:30Z; classify, Python setup, dependencies, pytest readiness, env pins and changed tests success; EVIDENCE and RELEASE lanes success (the release lane builds and verifies the attestation on the hosted runner); PRODUCT, COMPAT, DB, RAILS, QA skipped as classified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` printed | yes |
| Local required tests pass for the current head | the code tree of `433c1a5` is `a028b0c`'s; v1.3 §4 (E-CI: validators 0; changed-test 198, evidence lane 130, config + engine-core 165, release lane 79, qa lane 488 passed; CI-like attestation build and verify PASS) and v1.3 §3 (E-DEB: builds and verifies) | yes |
| Remote head identity matches the verified candidate | remote head read back `433c1a561f9f37a8b601808a721b8746c83db18a` after push 3 at 20:06:07Z; this record's commit is the only later commit and changes only `docs/ephemeral/` | yes (record commit verified at return) |
| PR open and mergeable, no blocking conflict | `state: open`, `draft: false`, `merged: false`, `mergeable_state: clean`, head `433c1a5`, base `main` `0cd7b84` (no commit on `main` after the base), read 2026-10-13T~20:19Z | yes |
| Action ledger and final checkpoint complete, saved, read back, linked | this record (§7), read back after commit; checkpoints v1.1 to v1.3 | yes |

## 3. Hosted CI

| Run / job | Head | Result | Status |
| :- | :- | :- | :- |
| 38446041858 / 115465311140 | `4d11089` | success 18:22:50Z–18:34:58Z; EVIDENCE, RELEASE success; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | stale (CX-1) |
| 38450463942 / 115479729750 | `b6fe37d` | success 18:53:53Z–19:06:27Z | stale (CX-2/CX-3 review) |
| 38456991751 / 115502168686 | `e7ec65f` | success 19:42:40Z–19:53:35Z | stale (CX-4) |
| **38460145263 / 115512888315** | **`433c1a5`** | **success 20:06:16Z–20:16:30Z; EVIDENCE, RELEASE success; changed tests success; other lanes skipped as classified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`** | **current verified candidate** |

No CI run was cancelled by this session; no `[skip ci]` or other suppression was used. Each superseded run completed before the next corrective push.

## 4. Review matrix (final)

| ID | Head | Finding (Codex code review) | Disposition | Record |
| :- | :- | :- | :- | :- |
| CX-1 | `c27c5e8` | P1 "Verify captures before relabeling them as current" | corrected by `c0ca923` (labels move only for captures whose bytes changed since the Mirror last recorded them) | v1.1 |
| CX-2 | `b6fe37d` | P1 "Require producer proof before advancing capture labels" | **accepted residual by Product Owner decision**; no code change; recorded for the IA at PR-40 | v1.2 §3.1, §8 |
| CX-3 | `b6fe37d` | P2 "Validate the manifest before minting a release label" | corrected by `489bc17` (full manifest validation before any label) | v1.2 |
| CX-4 | `e7ec65f` | P2 "Detect setuptools using the wheel child's environment" | corrected by `a028b0c` (probe in the wheel child's environment), reproduced before/after on E-DEB | v1.3 |
| — | `433c1a5` | none | clean (§2) | this record |

Finding identifiers: v1.2 §2 (`CX-<n>`; v1.1's "CR-1" is CX-1).

## 5. In-flight decisions (consolidated)

| ID | Decision | Record | Tested by |
| :- | :- | :- | :- |
| ID-35-1 | CX-1: labels bound to regenerated captures; incoherent labels refused; config delta strips the label only on a regenerated primary | v1.1 §5 | v1.1 §4 |
| ID-35-2 | PD-10 superseded: the manifest-only-cut invariant restored in full and extended to an updater run | v1.1 §5 | same |
| ID-35-3 | `test_release_labels_follow_the_manifest_through_the_updater_alone` replaced by the regenerated-capture test | v1.1 §5 | same |
| ID-35-4 | CX-3: full manifest validation (`manifest_only_problems`) before minting a label | v1.2 §6 | v1.2 §5 |
| ID-35-5 | CX-4: wheel layout compat decided by a probe in the wheel child's environment; the console-entrypoint test isolates the probe | v1.3 §5 | v1.3 §3, §4 |

No other decision was taken. No rescope, PF10 addendum, Proceed or approval was created.

## 6. Attributable delta for PR-40

`git diff 0cd7b84 433c1a5`: the PR-30 commit `c27c5e8` (15 paths: four tool/validator files, three test files, eight governed companions), result v1.0 (`4d11089`), and the PR-35 commits `c0ca923` (updater +75/−5, test +91/−25), `489bc17` (updater +7/−1, test +13/−0), `a028b0c` (builder +30/−6, test +42/−7), plus results v1.1 (`b6fe37d`), v1.2 (`e7ec65f`), v1.3 (`433c1a5`) and this v1.4. The PR-35 corrections change no governed companion (updater written twice, no diff, at each corrected head), no release member and no `docs/pfcanon/` file.

## 7. PR_REMOTE_ACTION_LEDGER (PR-35, continued from v1.3 §6)

| Time (UTC) | Action | Fact |
| :- | :- | :- |
| 20:06:07 | Push 3 | `e7ec65f..433c1a5` (`a028b0c` + v1.3), no force; remote head read back `433c1a561f9f37a8b601808a721b8746c83db18a` |
| ~20:06 | CX-4 thread | reply 4263445882; thread `PRRT_kwDOP103ks6sCFjw` resolved |
| ~20:07 | PR description | updated: CX-4 under "Why", "What changed" and "Checks run"; `a028b0c` checks and the E-DEB reproduction; headings kept |
| 20:09:54–55 | Codex review on `433c1a5` | summary completed; no review comments; PR reactions `+1` = 1, PR `updated_at` 20:09:55Z |
| ~20:10 | Review and thread re-read | 4 threads, 4 resolved; no Codex review after 5509067586 |
| 20:11:08 | TypeSafe reading for PR-40 | §9 |
| 20:16:30 (read ~20:19) | Hosted CI on `433c1a5` | run 38460145263 success, §3 |
| ~20:19 | Mergeability read | `mergeable_state: clean`, §2 |
| after this record's commit | Push 4 (record only) | read back, then CI and Codex summary on the record commit read before the return |

**Remaining useful local action:** none. **Safety-net check-in:** trigger `trig_015UpKwTaRpbAnyN781w5fvk` (20:36Z) pending; the subscription stays active until the merge or close.

## 8. Unresolved items and owners

| Item | Owner |
| :- | :- |
| CX-2 residual: after a manifest cut, a capture changed by something other than its owner (stale restore, truncation, forbidden hand edit) takes the new label at the next updater run; owner-certified labels would change D-1 for WU-PR-03/04/05/08. Accepted by the Product Owner | IA at PR-40 |
| PD-10 superseded by ID-35-2; PD-11 stands; `test_isolated_console_entrypoint_is_installed_from_tracked_package` adapted by ID-35-5 although plan §8.1 listed it unchanged | IA at PR-40 |
| OBS-W2-1, OBS-W2-2 (doc-delta candidates), OBS-W2-3 (other ambient probes) | plan §17 owners |
| OBS-17 (qa lane, `tests/qa/test_generate_epic_close_pack.py`; the qa lane was not selected on this PR and passed locally, 488) | QA tool and test owner through the IA |
| Prompt-use provenance writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent | pending, non-gating |
| Merge | Nathan / Product Owner (manual) |

## 9. TypeSafe reading for the receiving session (PR-40, WU-PR-02)

Action sent (v6): "After the Product Owner's manual merge, in the continuing whole-change implementation session, independently review the landed lineage of one merged pull request for one work unit of an approved change (a first lineage review of this unit): verify the merge and squash attribution, then check about seven source and test files across four release-evidence tools and one validator, the governed index and mirror companions regenerated only by their owner tool, four review corrections and one Product Owner-accepted residual made during review resolution, against the approved specification, plan, instruction and canon, following the existing ordered review procedure, and decide accept or reject and the next approved stage. Read-only; no live vendor, production or database run; a later QA lane follows."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.52 (confidence 0.59); rung probabilities low 0.00, medium 0.05, high 0.49, extra high 0.35, max 0.11, ultracode 0.00. Model probabilities Fable 5.1 0.28, Opus 5.5 0.72 (confidence 0.44). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.04, Opus 5.5 at high 0.35, Opus 5.5 at extra high 0.25, Opus 5.5 at max 0.08, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.14, Fable 5.1 at extra high 0.10, Fable 5.1 at max 0.03, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and high. Sent 2026-10-13T20:11:08Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T20:11:08Z; HTTP 200 in 0.78 s; 4254 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between extra high and high.
- **Notion row:** not written, as PR-35 directs. **Nathan's pick for PR-40:** not stated. **For this PR-35 session:** not stated (reading in PR-30 result v1.0 §9).

**Surface advice:** run PR-40 in the continuing whole-change HDE-CRD-0002 IA context as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with GitHub access to #634 (merge facts, commits, reviews, threads, check runs) and Notion read access for the prompt. Reproducing the corrections needs package-index access to build the E-CI environment (Python 3.12 with CI's install); re-verifying S06 or CX-4 needs the cloud container's `/usr/bin/python3` (CPython 3.13.16) with Ubuntu's patched setuptools 68.1.2, as v1.3 §3 describes. No live vendor, production or database access is needed. Enter only after Nathan's manual merge.

## 10. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-35 / review resolution 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page last edited 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-02 PR-35 session / PR-35 |
| capture time | 2026-10-13T20:21:00Z |
| execution identity | https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK |
| inherited usage | PR-10 instruction 1; PR-20 plan 1; PR-30 implementation 1 (result v1.0 §10) |
| repository persistence | recorded here only (writer absent; pending, non-gating) |

## 11. PR-40 native package (by repository path)

- PR instruction: `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md`
- Detailed PR plan: `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md` (and its prototype diff)
- PR-30 result (`PR_CANDIDATE_PUBLISHED`): `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md`
- PR-35 checkpoints: `…-result-v1.1.md`, `…-result-v1.2.md` (CX-2 Product Owner decision), `…-result-v1.3.md`
- PR-35 result (`MERGE_PENDING`, historical pre-merge evidence): this record
- Ordered PR_REFS: amthorn78/glow-hdengine-v2#634 only
- Approved lineage: Specification v1.1 (approved), Implementation Audit v1.0, Implementation Plan v1.1, Plan review v1.1, PF10 addenda 2.3 and 2.1
- CANON_CONFLICT_REGISTER: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); carried unchanged; no new entry
- Recovery state: none open. NOT PRODUCED: a `MERGE_OBSERVED` result (pending a merge); any QA, Ops, acceptance or closure artifact; a PF10 addendum. NOT EXECUTED: the Codex security review (deprecated); hosted qa lane (not selected)
- Return owner: the whole-change HDE-CRD-0002 IA (session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j in the records)

## 12. GCF-17 continuity

`WORK_UNIT_ID` WU-PR-02; original Proceed (front matter); workspace `/home/user/glow-hdengine-v2` (cloud container; recoverable from the branch); branch `claude/intelligent-cannon-32u7tl`; pull request #634; PR instruction v1.0; detailed plan v1.0; primary skill glow-hde-pr-development; recovery lineage plan v1.0 → result v1.0 → v1.1 → v1.2 → v1.3 → this v1.4.

## Canon relied on

Read on `main` at `0cd7b84` (the branch changes no file under `docs/pfcanon/`):
- **Merge readiness and result:** PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 ("Genuine merge-readiness gate", "Other lawful results", "Mandatory single-block handoff"); HDE Governance §9.1.1 (PR merges remain Product Owner actions; the normal review and evidence chain); PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 2 and 3 (only the Codex code review; `MERGE_PENDING` does not depend on a security review) and addendum 2.1 (TypeSafe reading; no AI recommendation); PR instruction v1.0 §12; plan v1.0 §19.
- **Corrections:** as recorded in v1.1, v1.2 and v1.3 "Canon relied on": HDE Schemas & Artifacts §6.2, §6.2.1, §6.3, §6.4, §8.3; Implementation Plan v1.1 §5 IF-7, §7 WU-PR-02 acceptance (1) and (4), §10; PR instruction v1.0 §4, §8 D-1, §11.
- **PR-40 receiver contract:** PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f), section "Inputs" (the native package of §11 and the merge-entry rule).
- **Operative documentation:** `AGENTS.md` (PR descriptions; evidence attribution; sole Index/Mirror writer; closed rails; pytest readiness).

## Nonclaims

`MERGE_PENDING` is pre-merge readiness only: not a merge, not QA evidence, QA verdict, acceptance, PF09/PF30 movement, deployment, canon change or closure. CI green is not QA. HDE-CRD-0002 has no QA evidence from this PR (admission readiness only).
