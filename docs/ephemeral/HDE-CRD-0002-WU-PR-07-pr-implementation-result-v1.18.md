---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.18"
result: none (PR-35 checkpoint; CX7-19 fixed with a sibling slice gap; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.17.md (preserved unchanged)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
companion_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/670 (against main; head 606e1b4, hosted CI green on ubuntu-26.04; carried by #668; the Product Owner merges it)
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: 5bf0db6ea378445e003b26ad75736a16be725ed2
commits_in_this_push: 46ab9d2 (CX7-19 and the slice gap), e0c4e2a (the ADR's lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T14:06:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.18 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Hosted CI on `5bf0db6`:** passed (run 39608580531, 13:30:23Z to 13:51:01Z).
- **Codex round 17** (review 5600624933 on `5bf0db6`, 13:39:30Z):
  - it did not re-raise CX7-17 or CX7-18, so both threads are resolved;
  - it raised one new P1, CX7-19, on a real input (§2).
- **No design question.** CX7-19 is a defect in how this session implemented PO-35-16's chosen rule, a title derived from a tracked canon file name. The fix keeps that rule and reads every tracked file name. Checking the other audit rules the same way found one sibling gap, in the allocation's slice form (§3).
- **The fix.** It is in `46ab9d2`, and the ADR's lines are in `e0c4e2a`. Both are in this push.

## 2. Review findings (round 17)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-17, CX7-18 | Codex, `477570d`, P1 | fixed in `4fac34f` (v1.17) | — | — | Round 17 did not re-raise them; both threads are resolved |
| CX7-19 | Codex, `5bf0db6`, P1 (comment 4337527616, thread `PRRT_kwDOP103ks6uyjso`) | `tools/qa/generate_epic_close_pack.py`, `PF_DOCUMENT_RE` | The PF-title parser reads only hyphenated file names with a PF number and a version. So `HD Engine Epics Map`, from the tracked `PF16-Canon-HD Engine Epics Map v2.3.8.md`, gives `PF_TITLE_UNKNOWN` | Yes: the tracked `docs/pfcanon/` files on the head. Nine of the 34 did not match. The schema's title pattern also refused `7 Phases of Alchemical Engineering` (PF21), because it begins with a digit | Fixed (addendum 2.14 rule 2). The thread is answered and stays open until the next review |

**Cause.** v1.17's test of the title rule named twelve expected titles, all from hyphenated file names. It never required every tracked file to yield a title. The new test does.

**Rule 8.** Round 16 raised the closure override and the posture, and round 17 raised PF-title parsing. They are different contracts, so the rule is not triggered.

The review history across seventeen rounds:
- eighteen P1s, CX7-1 to CX7-10 and CX7-12 to CX7-19, all fixed;
- one P2, CX7-11, with a stated limit.

Three further rounds failed on the Codex usage limit.

## 3. The audit rules checked against tracked inputs

After CX7-19, each rule that PO-35-16 to PO-35-19 introduced was run against the real tracked files it reads.

| Rule | Tracked inputs | Result |
| :- | :- | :- |
| PF titles (PO-35-16) | the 34 `docs/pfcanon/` files | CX7-19: 9 unmatched. Fixed: 34 files, 34 distinct titles, each accepted by the schema's pattern |
| Allocation slice (PO-35-19) | HDE-CRD-0002's plan v1.1 (`WU-PR-01` to `WU-PR-08`, `WU-DOC-01`, `WU-OPS-01`); HDE-EPIC040's plan v2.1 and PR plans (`PR01` to `PR07`, `PR06a`, `PR06b`) | **Gap:** the pattern refused HDE-EPIC040's `PR01` form, so an Epic could not allocate its deliverables to its own slices. Fixed: `PR<nn>` with an optional lowercase letter is accepted beside `#<n>` and `WU-…` |
| Deferral heading (PO-35-17) | every Markdown heading of the 7 PF09 files and PF30.1 | 422 of 426 headings are valid heading values. 3 PF09.6 headings contain words that the feedback-dependency refusal rejects (`release identity`, `release\_id`), and 1 PF30.1 heading is a template (`<CRD_ID>`). **Stated limit, no change:** ADR decision 6 applies that refusal unchanged to every causal value, and such a deferral can take the ADR-status form |
| Registers (PO-35-17) | the 7 PF09 files and PF30.1 | all match their register patterns |
| QA plan (PO-35-18) | HDE-EPIC040 QA plan v1.2 and its ledger | 12 checks in plan order, equal to the ledger's 12 (v1.17's test) |
| QA RCA (canon) | `audit/EPIC-024_QA_RCA.md`, `audit/EPIC-030_QA_RCA.md` | both have the derived form `audit/<prefix>_QA_RCA.md` |

## 4. Implementation

- **`tools/qa/generate_epic_close_pack.py`** (`46ab9d2`):
  - `PF_DOCUMENT_RE`: the PF number, the kind and the version are each optional, and the parts may be separated by hyphens, spaces or both;
  - `_pf_title_key` also reads a run of spaces as one.
- **`schemas/close_candidate_source.v2.json`** (`46ab9d2`):
  - `pf_title` allows digits;
  - an allocation slice may also be `PR<nn>` with an optional lowercase letter.
- **`tests/qa/test_generate_epic_close_pack.py`** (`46ab9d2`):
  - the title-derivation test requires every tracked PF file to give one title that the schema's pattern accepts;
  - new cases: a close pack bounded by `HD Engine Epics Map` and `7 Phases of Alchemical Engineering`, and an Epic allocation to `PR01` and `PR06a`;
  - a new test holds the slice pattern to the real plans' slice IDs.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`e0c4e2a`):
  - the PF-title and slice stated limits widened;
  - the deferral-heading limit (§3);
  - the amendment line points to this record.

## 5. Local checks

All runs were in this session's clones, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `46ab9d2` | 886 passed (883 before, plus 3 new cases) |
| 2 | Negative control: the new tests against `5bf0db6`'s writer and schema | 4 failed, all behaviourally:<br>• the derivation test lists the 9 unparsed files;<br>• the reviewer's titles are refused (exit 1);<br>• the Epic allocation is refused (exit 1);<br>• the real plans' `PR01` to `PR07` and `PR06a`/`PR06b` fail the slice pattern |
| 3 | Replay of `e0c4e2a`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 13:46:51Z to 14:05:49Z, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, exit 0:<br>• changed tests 4,502 passed, 2 skipped;<br>• product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 |

## 6. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| An Epic plan's `PR<nn>` slice ID is a work-unit ID under PO-35-19 | `schemas/close_candidate_source.v2.json` | PO-35-19 named "a work-unit ID or a PR reference", and HDE-EPIC040's plan names its work slices `PR01` to `PR07` | §5 rows 1 and 2 | the next Codex round |
| The feedback-dependency refusal stays unchanged for a deferral heading | `docs/adr/hde/close_pack_writer_adr.md` | ADR decision 6 applies it to every causal value, and the ADR-status form remains available | §3 | same |
| The title pattern allows digits anywhere | `schemas/close_candidate_source.v2.json` | `7 Phases of Alchemical Engineering` is a tracked title, and every title is checked against the tracked files anyway | §5 row 1 | same |

## 7. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 24 hours 51 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 17 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 20 runs:
  - 15 successes: 6 on ubuntu-24.04, 2 on ubuntu-26.04 with the image read (`c9bff83`, `a2ba526`), and 7 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`, `3eb31c3`, `f6e1ad0`, `477570d`, `5bf0db6`);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-19. None new.

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.17 §9)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 104 | 13:29 to 13:31 | Replies on CX7-17 and CX7-18; push `477570d..5bf0db6`; update #668's description | pushed and read back |
| 105 | 13:31 | Check-in `trig_01QoRDp6KabsNijXqhjBYqyX` armed for 14:22 | armed |
| 106 | 13:30 onwards | Hosted `test` on `5bf0db6` (run 39608580531) | success |
| 107 | 13:39 | Codex review 5600624933 on `5bf0db6` | CX7-17 and CX7-18 not re-raised; CX7-19 (P1) |
| 108 | ~13:50 | Resolve the CX7-17 and CX7-18 threads | resolved |
| 109 | next | Reply on CX7-19; push `5bf0db6..` this record; update #668's description; re-arm the check-in | — |

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-19 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (`MERGE_PENDING`), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
