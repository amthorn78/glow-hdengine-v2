---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC041-WU-PR-01-PR-IMPLEMENTATION-RESULT
artifact_version: "1.5"
phase: PR-35
result: MERGE_PENDING
predecessor: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.4.md (v1.4, PR-35 checkpoint after the F-1 fix; 10,628 bytes; blob 9b41a83a1dd3; sha256 505405583b34e7a858fc74b4fbe1814caba2296d0a91f0db90480b3a03d8716a; pushed as 2992cd07; preserved unchanged)
supersession_reason: v1.4 recorded the F-1 correction push and named the next evidence. This version records that evidence on 2992cd07 and the PR-35 result. v1.2 and v1.3 stay as history; their MERGE_PENDING was withdrawn by v1.4
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md (v1.0)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0)
REMEDIATION_REVIEW_ID: none
RESCOPE_REVIEW_ID: none
proceed: the Product Owner's invocation of PR-30 — PR Implementation Proceed — 102726.1 for exactly PR_IMPLEMENTATION_PLAN v1.0, 2026-10-28; carried over; no new Proceed requested or created
pf10_read: as v1.1 (docs/pfcanon/PF10-HDE-Build-Notes-v13.9.1.md; provenance)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1 (https://app.notion.com/p/4064590a05eb8108a9f5cececa4b3149)
primary_skill: glow-hde-pr-development 1.5.0
session: https://claude.ai/code/session_01Q789tzt85iauNogD8xS2zg (the dedicated WU-PR-01 PR-35 session)
pull_request: amthorn78/glow-hdengine-v2#791 (https://github.com/amthorn78/glow-hdengine-v2/pull/791)
branch: claude/wu-pr-01-implementation-plan-js521f
base: origin/main e121e354060afe3007a84d82b61b073df1da666b (unchanged)
head_verified_by_this_record: 2992cd070b905c4fd20cadef38260f564e194ec5
tested_source: 72d40b5f49dd1081c5db82dc223b92a8945a2c9b (2992cd07 adds only the v1.4 record under docs/ephemeral/)
pr_refs: [amthorn78/glow-hdengine-v2#791]
created_at: 2026-10-28 (UTC)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; no new entry
---

# HDE-EPIC041 WU-PR-01 — PR Implementation Result v1.5 (PR-35, MERGE_PENDING)

## 1. Result

**MERGE_PENDING — Ready to merge:** [amthorn78/glow-hdengine-v2#791](https://github.com/amthorn78/glow-hdengine-v2/pull/791), on head `2992cd07`. This record's own commit is covered by §6.

| Item | On `2992cd07` |
| :- | :- |
| Codex code review | completed 15:56:43Z, `has_any_findings: false`, `has_unresolved_findings: false` (§3) |
| Review threads | 1, resolved: F-1, fixed in `72d40b5f` (v1.4 §2) |
| Hosted `test` | success, all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§2) |
| Mergeability | `mergeable_state: clean`; open, not draft; base `e121e354` |
| Local checks | plan v1.0 §11 items 1 to 5 passed on `72d40b5f` (v1.4 §4), whose code tree `2992cd07` carries unchanged |

PR-35's corrections:
* `e6797eab`: the merge of `main` after #792.
* `b399cfd0`: the clock-safe keys-only log test (ID-35-1).
* `72d40b5f`: the F-1 purity fix (ID-35-4).

Not done: the merge. Nathan merges manually. This is pre-merge evidence only.

## 2. Head identity and hosted CI on `2992cd07`

* **Head.** `2992cd070b905c4fd20cadef38260f564e194ec5`, read back with `git ls-remote` after the push at about 15:55Z and again at about 16:13Z; the PR reports the same head. It adds only the v1.4 record to `72d40b5f`. The PR's diff from `main`: 7 code and test files (+674), plus the records v1.0 to v1.4.
* **CI.** Check run 122931449859 (run 40720839619), `test`, conclusion `success`, 15:56:17Z to 16:11:32Z. Every step succeeded:
  * checkout `HEAD is now at 2992cd07`;
  * `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=12;lanes=product,compat,db,rails,evidence,qa,release`;
  * changed-test step 3669 passed;
  * product 77; compatibility 119 passed, 3 skipped, 2 xfailed; database 269; rails 120, 113 and 155, then 160; evidence 134; QA 488; release 79;
  * final `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
* The changed-test count equals the local item 3 on `72d40b5f` (v1.4 §4).
* The stale run on `b4f897d5` (40718015218) was superseded by this one, as v1.4 §5 stated.

## 3. Reviews

| Round | Head | Result |
| :- | :- | :- |
| 1 | `c6e50a98` | Codex: no findings |
| 2 | `1b273594` | Codex: no findings |
| 3 | `8b556e94` | Codex: automatic run stalled; manual re-run under PO-35-1: no findings (v1.3 §3) |
| 4 | `b4f897d5` | Codex review 5685440601: one P2, F-1; fixed in `72d40b5f`; reply 4402874736 names the commit; thread `PRRT_kwDOP103ks6xMqM-` resolved (now outdated) |
| 5 | `2992cd07` | Codex: started 15:55:32Z, completed 15:56:43.187850Z, `has_any_findings: false`, `has_unresolved_findings: false` |

Security review: not run, and not required (v1.1 §3). P1 findings: none. Security findings: none. The repeated finding class trigger did not fire: F-1 is the only finding, and round 5 raised none.

## 4. Merge-readiness gate on `2992cd07`

| Predicate | State |
| :- | :- |
| Every applicable current-head review read; every finding fixed or answered; no open P1 on a real input | met (§3) |
| No required review thread unresolved | met (the one thread is resolved) |
| Required current-head CI passes | met (§2); no waiver used or needed |
| Local required tests pass for the current head | met: items 1 to 5 on `72d40b5f` (v1.4 §4); the full replay passed on `b399cfd0` (v1.1 §4), and the F-1 change since then is limited to `engine/charts/pure.py` and its purity test |
| Remote head equals the verified candidate | met (§2) |
| PR open and mergeable, no blocking conflict | met (`mergeable_state: clean`) |
| Ledger and final checkpoint saved and read back | this record, read back after the push (§6) |
| Approved scope complete; no unresolved material rescope or dependency | met: plan v1.0 §6 delivered; the merge-order dependency on #792 is met |

Remaining risks for this PR: NONE. OBS-4 (v1.2 §9) is a defect in an existing test outside this unit, not a risk to this change.

## 5. In-flight decisions

ID-35-1 to ID-35-3 (v1.2 §6) and ID-35-4 (v1.4 §3), unchanged. No new one.

## 6. PR_REMOTE_ACTION_LEDGER (continues v1.4 §5)

| # | Time (UTC) | Action | Outcome |
| -: | :- | :- | :- |
| 32 | ~15:55 | Pushed `72d40b5f` and v1.4 (`b4f897d5..2992cd07`, fast-forward); read back the remote head and the record (10,628 bytes) | remote head `2992cd07` |
| 33 | 15:55:38 | Replied on the F-1 thread (comment 4402874736) naming `72d40b5f`; resolved thread `PRRT_kwDOP103ks6xMqM-`; updated the PR description | resolved |
| 34 | 15:55:32 to 15:56:43 | Events: the Codex review of `2992cd07`, `running`, then `completed` with no findings | §3 |
| 35 | 16:11:43 | Event `check_suite.completed`; read the check run, the full job log, the PR, the threads and the reviews | CI success; `clean`; 1 resolved thread (§2, §3) |
| 36 | 16:13:04 | TypeSafe re-read for PR-40 on the revised action text (§7) | HTTP 200 |
| 37 | next | Commit and push this record (`docs/ephemeral/` only); read back the remote head; observe hosted `test`, Codex and mergeability on the new head through the subscription. The safety-net check-in `trig_01SSKXwVxBUmgqcPcG4THhbP` is armed for 16:30Z | — |

**About this record's own commit.** It adds only this file under `docs/ephemeral/` and leaves the code tree unchanged. Hosted `test` runs on that head because the PR as a whole selects all seven lanes, and Codex reviews it.
* The session's reply, before the conditional PR-40 block, shows that head's hosted `test` result with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, its Codex state and its `mergeable_state`.
* If Codex raises a finding on it, the finding is handled under PR-35, a further record replaces this one, and the PR-40 block is not issued.
* If the Codex run stalls, the session asks the Product Owner (PO-35-1 covered `8b556e94` only).
* If CI or mergeability differs, a further record replaces this one.

Stale or cancelled runs: none active. Remaining useful local action: none.

## 7. TypeSafe reading and surface advice for the receiving session (PR-40)

* **First reading, superseded.** The action text read at 12:30:58Z (v1.2 §10: "TypeSafe v8.2: Opus 5.5 at extra high") described the PR before its review phase. It said "two result records" and no corrective commits, which is no longer true. It is kept as history.
* **Method.** Installed TypeSafe scoring skill, request v8.2, `score_v8.py` run once on the revised text; session kind `review`; label "HDE-EPIC041 PR-40 WU-PR-01 lineage review (revised facts)". The Notion row was not written.
* **Action sent (v8.2).** "In a dedicated session, after the Product Owner's manual merge, review read-only the landed lineage of one merged pull request of about 670 added lines of code and tests (two new Python modules, four new test files and a 13-line CI classifier registration, changing no existing caller), whose review phase added a merge commit from the base branch, two small corrective commits (a test fix and a purity fix answering one automated review finding) and six result records, against its already approved instruction, detailed plan, whole-change plan and specification, and write one lineage review record; a task list exists in the plan; no live run against a provider occurs; the review's acceptance decides whether the next of three work units is planned, and a separate QA lane follows later."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.58 (confidence 0.66); rung probabilities low 0.00, medium 0.03, high 0.40, extra high 0.52, max 0.05, ultracode 0.00. Model probabilities Fable 5.1 0.04, Opus 5.5 0.94, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.92). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.016, Fable 5.1 at extra high 0.021, Fable 5.1 at max 0.002, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.028, Opus 5.5 at high 0.376, Opus 5.5 at extra high 0.489, Opus 5.5 at max 0.047, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.008, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-28T16:13:04Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.66 s; 5495 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high; model by rule: Opus 5.5.
* **Picks.** Nathan has stated no pick for PR-40 and none for this PR-35 session, so none is recorded.
* **Surface advice (PR-40).** As v1.2 §10:
  * a new top-level Claude Code cloud session after the merge, with read access to the merged state, #791's commits, reviews and checks, and #792;
  * it writes only its own review record under `docs/ephemeral/`, through its own pull request;
  * any test re-run uses CPython 3.12 with CI's install and `env -i` closed rails, after `git fetch --unshallow`;
  * no tool calls during `prepush_check.py replay`;
  * no open rails, vendor, Railway, database or Notion writes.
* **Two lineage facts for PR-40 to check.** The F-1 thread and its fix in `72d40b5f`. And the code that differs from the plan's companion diff: `engine/charts/pure.py` (`_parse_time`), `tests/charts/test_chart_pure_purity.py` and `tests/adapter/test_chart_orchestration.py`, as ID-35-1 and ID-35-4 record.

## 8. Unchanged

* v1.2 §8 (#792).
* v1.2 §9 (unresolved items and owners, with OBS-4).
* v1.2 §11 (prompt-use provenance; corrective commits now `e6797eab`, `b399cfd0`, `72d40b5f`; head `2992cd07`).
* v1.2 §12 (the conditional PR-40 terms: the block is usable only after Nathan has manually merged #791, and only where no `MERGE_OBSERVED` result was returned for that merge; PR-40 independently verifies the merged state and the landed lineage; it is entered once per merge).
* v1.3 §3 (PO-35-1).
* v1.4 §2 to §4 (F-1 and ID-35-4).

## Canon relied on

As v1.2 "Canon relied on" and v1.4 "Canon relied on". The topics this version decides map as follows:

| Topic | Sources and sections | How it governs |
| :- | :- | :- |
| Readiness gate and result | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1, "Genuine merge-readiness gate" and "Other lawful results"; `glow-hde-pr-development` 1.5.0, "In PR-35, reach genuine merge readiness" | §4 maps each predicate on `2992cd07` |
| The F-1 thread | Change Process Guide (v2.5.5), "PR review finding disposition (every pull request; real inputs only)"; Plan Templates (v2.0.6), "Review guardrails" | fixed, the reply names the commit, the thread is resolved; no repeated class |
| The re-read reading | TypeSafe scoring skill, "What not to do" ("a genuinely revised prompt gets a new reading, recorded as such") | §7 records both readings |

## Nonclaims

This record is pre-merge readiness evidence only. It is not a merge, a lineage review, acceptance, QA, Ops, deployment, PF09 or board movement, a canon change, a PF10 addendum or closure. No agent merges #791; Nathan does.
