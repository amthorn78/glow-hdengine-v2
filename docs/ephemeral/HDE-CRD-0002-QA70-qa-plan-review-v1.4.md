---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-CRD-0002-QA70-QA-PLAN-REVIEW
artifact_version: "1.4"
predecessor: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.3.md (DENY of approved QA Plan v1.2 against the delivered WU-REM-02 change; blob bf5cdaa81114; SHA-256 7691b8f24648469c9f684f43d14eb11bb165d175e1dd4e18473004a1a62db813; unchanged)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW, by the Product Owner's direction D-2 (a revised successor after QA-80; direction §4)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING, as the direction applies the initial mode
prompt_mode: REVIEW
decision: APPROVE
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
reviewer: Isis (Isis-53), continuing Lead Developer and QA Plan decision owner for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, the session of reviews v1.0 to v1.3)
session_disposition: continuing Isis context, as the QA-80 handoff v1.2 routes it
context_conflict: none
prompt: QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf; page state 2026-10-12T02:29:54.691Z, unchanged; read in full at review v1.3 in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_PLAN_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (QA_PLAN v1.3, PLAN_PENDING_REVISED; blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; 119,368 bytes, 781 lines; read in full by word diff against v1.2, with every changed region read in place)
QA_PLAN_BASE: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (approved; blob 66f6016cc75b; unchanged)
REDLINE_APPLICATION_REPORT_ID: docs/ephemeral/HDE-CRD-0002-QA80-redline-application-report-v1.2.md (blob 67640c8378aa; SHA-256 36893bf1460900e0f6497aaa71194426bb695a475cd1403016ce417d855b59d2; read in full)
QA80_CHECKPOINT_ID: docs/ephemeral/HDE-CRD-0002-QA80-checkpoint-v1.2.md (blob 1ed6e4450ee7; read)
PO_DIRECTION_ID: docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md (blob a2db4f362bf4; on main through #736)
QA_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE; unchanged)
author: Kronos, the QA authority and QA Plan author for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (568,847 bytes; SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; byte-identical to the version review v1.3 read)
repository_head_read: origin/main 3d7c40ea (amthorn78/glow-hdengine-v2#738 merged); tree outside docs/ephemeral/ and docs/pfcanon/ equal to 22a3bc0's
PF10_ADDENDUM_OUTPUT: NONE (an initial-mode APPROVE produces no addendum; direction §5)
canon_conflict_register: CR-1 to CR-11 carried; CR-12 APPROVED (Product Owner), recorded in Plan v1.3 §13 field for field; no new conflict
decision_time_utc: 2026-10-25T16:38:19Z
next_prompt: QA-90 — Create Bounded QA Execution Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8), the continuing Kronos (direction D-3)
handoff: docs/ephemeral/HDE-CRD-0002-QA70-handoff-to-qa90-v1.1.md
---

# HDE-CRD-0002 — QA Plan Review v1.4 (QA-70, review of Plan v1.3)

## 1. Decision

**`APPROVE`.** QA Plan v1.3 applies each of RL-18 to RL-22 exactly once and changes nothing outside those regions and QA-80's bookkeeping (§3). FND-201, FND-202 and FND-203 are corrected. No new finding arises (§4).

The whole Plan is coherent, complete, bounded and executable for every check it still has to run:
- check 13's remediation verification at the remedied code (state (b));
- checks 16 to 21, which have not been run.

The fourteen accepted results stay attributed to the code they tested (state (a)).

**What this approval is and is not.**
- **v1.3 becomes the approved Plan, replacing v1.2.** v1.2's bytes stay unedited.
- **No PF10 addendum** records the change (direction §5). This review, Plan v1.3 and the application report v1.2 record it.
- **Not a QA result.** The approval is not task selection, execution, PASS, merge or closure. Check 13 stays `FAIL_BEHAVIOR` until Kronos's verification under §9 returns.
- **Control goes to Kronos at QA-90 (direction D-3)**, to create check 13's bounded verification task from this Plan.

## 2. Review method and independent checks

Everything ran in a fresh `--no-hardlinks` full-history scratch clone of `main`, detached at `3d7c40ea` (`git rev-parse --is-shallow-repository` `false`). Nothing from the clone was committed.

| # | Check | Result |
| :- | :- | :- |
| 1 | Word diff, `git diff --no-index --word-diff` of v1.2 and v1.3; `-U0` hunk count | 30 hunks. Each sits in an RL-18 to RL-22 region or in QA-80's bookkeeping: front matter, title and state paragraph, §0, §13, §14, §15, Canon relied on, provenance. Matches report §6 |
| 2 | Check headings and `Surface / D-goal mapping` lines of v1.2 and v1.3 | Identical |
| 3 | Check 1's block: v1.2 lines 224 to 246 against v1.3 lines 232 to 254 (`cmp`) | Byte-identical, as RL-19 requires |
| 4 | RL-19's guard at `3d7c40ea`: `git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'` | Empty. So `main`'s code equals `22a3bc0`'s, where review v1.3 §2 row 2 observed "141 passed" |
| 5 | RL-20's read (i) at `3d7c40ea`: the `git diff --stat` and the `git status --porcelain --untracked-files=all` reads, both with base `22a3bc0` and the six exclusions | Both print nothing. The three graph globs list 10 tracked files |
| 6 | Report anchors (v1.3 lines 88 to 91, 158, 217, 218, 430, 432 to 434, 596 to 601, 632) | Each holds the applied text the report names |
| 7 | Byte lint of v1.3 | No CR, no U+2026, no triple full stop; one final LF |

## 3. Redline verification (review v1.3 §6)

| ID | Required outcome | In v1.3 | Verdict |
| :- | :- | :- | :- |
| RL-18 | §2 defines two attributed tested states:<br>- (a) `2e03a268`, tree `af5293473238`, for checks 1 to 12, 14 and 15, not re-executed;<br>- (b) a `main` commit whose tree outside the two prefixes equals `22a3bc0`'s (tree `c92ff9004856`), for check 13's verification and checks 16 to 21.<br>Release unchanged, with the comparison cited. §11 reports both states | Lines 88 to 91, with every value exact; line 632 names both states and which checks each covers, and also assigns check 13's attempt 1 to state (a) | Applied |
| RL-19 | Check 1 unchanged. A state-(b) E-L execution records check 1 step 1's five reads with the new base, plus step 2's manifest and `hdctl --version` reads, under its own `=== CONTEXT ===`. Rule A's HEAD read refers to its own recorded commit; "candidate changed" maps to `TOOLING_BLOCKED` | Line 217, a sub-bullet of rule A's E-L bullet, with every read and value exact; check 1 byte-identical (§2 row 3) | Applied |
| RL-20 | Read (i)'s base becomes `22a3bc0`, with the same pathspec and the history sentence updated; §5.4 names state (b) and `22a3bc0` | Lines 218 and 158 | Applied; both reads silent on `main` (§2 row 5) |
| RL-21 | Step 3 "141 passed". The provenance sentence names where each value was observed. Step 1, 2 and 4 predicates and Outcomes unchanged | Lines 430 and 432 to 434; the Outcomes line (435) is unchanged | Applied |
| RL-22 | A §9 bullet: verification and return, not attempt 2 or a reset; state (b), E-L, full history, same `check_id`, rails, class and deliverable; the notes carry the attempt-1 signature and name the remedy; `faa2246` is the failure context; merge by `check_id`; the label is Kronos's | Lines 596 to 601, every element present | Applied |

**Bookkeeping.**
- CR-12 is recorded in §13 field for field with the direction §6, and its history adds review v1.3's application.
- §14 adds three rows from review v1.3 §8: check 13's verification, CR-12 and O-1.
- §15 holds the TypeSafe reading for this review.
- The N-201 to N-204 notes are treated as report §5 states. N-201 (O-1) now has a §14 row, and N-204 is closed by #736.

## 4. Findings

**None.** Gate freeze holds (Plan Templates "Review stability and no-moving-target discipline"): only the text changed for v1.3 was examined for new blockers, and none was found.

Non-gating notes:
- **N-301: a hold on v1.2's scope until this approval.** The new state paragraph says that until Isis approves v1.3, neither v1.2 nor v1.3 authorizes "the remediation verification of check 13 or checks 16 to 21". This follows from FND-202 and ends with this approval. It adds no requirement.
- **N-302: generic "tested source" references.** Report §6 lists the references left unchanged: §3.2 E-L and E-V V-A, check 3 step 2 and check 21's Rails/Env line. They read through §2's two states, which is coherent: an accepted check ran at state (a), and every later execution runs at state (b).
- **N-303: check 20 V-A.** "A clean clone at the tested source" is not guard-checked inside check 20, as in v1.2. P1 reads the interpreter, `engine` and the `release_id`, and the release is identical in both states. This is unchanged text and not a finding.
- **Carried to QA-90 (N-201 of review v1.3):** the verification task records the shell's `TMPDIR` posture, because O-1 (OPS03 `EXDEV`) is still open with Thoth and the Product Owner.

## 5. CANON_CONFLICT_REGISTER

- **CR-1 to CR-8 and CR-10:** carried unchanged.
- **CR-9:** `PROPOSED` (Isis, IA-30 boundary).
- **CR-11:** `APPROVED_AS_CHANGED`, alternative (a).
- **CR-12:** `APPROVED` (Product Owner, 2026-10-25), alternative (a). Applied again here, through the mode and routing of this review.
- **New conflicts:** none.

## 6. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Check 13's remediation verification task (addendum 2.27 V-6; Plan §9), with its attempt label | Kronos, QA-90 (direction D-3) | Next |
| Its execution and evidence review | Operator the Product Owner chooses; Kronos at QA-110 | After the task |
| Selection of checks 16 to 21; check 20's venue and initiator; the evidence-only commit grant | Product Owner, at QA-90 | Not selected |
| O-1 (OPS03 `EXDEV`) | Thoth; Product Owner if independent | Open |
| O-A, D-1/LR6-O1, FND-028 | Product Owner | Unchanged |
| The QA-70/QA-80 route gap for an approved-Plan change | GCFPE-MGMT-10 maintenance owner (direction §7) | Reported there |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| CR-11 permanent drainage | Product Owner | Not a condition of the run |
| G-1, PO-2 and PO-5 drainage, O-2 to O-4 | As HDE Build Notes 2.28 records them | Unchanged |

## 7. TypeSafe reading for the receiving session (QA-90)

Action sent (v8.2): "As the continuing QA authority, create one bounded QA execution task from an already approved whole-change QA plan of 21 checks, for the remediation verification of one previously failed local check (a read-only pre-push tool check with four steps, whose main command runs about 25 minutes) after its three-file fix merged: exact commands, the candidate reads that pin the fixed code, the evidence publication and validation steps, and the attempt identity, written as a Markdown task record; other checks join the task only if the Product Owner selects them. Authoring changes no code and makes no live run against a provider; an operator executes the task and an independent evidence review follows."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at medium.**
  - Effort score 1.20 (confidence 0.82). Rung probabilities: low 0.04, medium 0.74, high 0.21, extra high 0.01, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.69, Sonnet 5.5 0.27, Haiku 5.5 0.03 (confidence 0.59).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.007, Fable 5.1 at high 0.002, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.028, Opus 5.5 at medium 0.511, Opus 5.5 at high 0.145, Opus 5.5 at extra high 0.007, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.011, Sonnet 5.5 at medium 0.200, Sonnet 5.5 at high 0.057, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.022, Haiku 5.5 at high 0.006, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Sent 2026-10-25T16:38:08Z. Nathan picks the cell.
  - Flags: none printed.
- **Detail line: not captured.** The script printed it, but the display command used in this session showed only the first lines of its output. The script was not run again, because a skill rule allows one reading per text.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-90 HDE-CRD-0002 check 13 remediation verification task from QA Plan v1.3", before this review was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - QA-90: Nathan's pick is not stated.
  - This QA-70 session: Nathan's pick is not stated. Its reading is in Plan v1.3 §15 (Opus 5.5 at high, score 2.33).

**Surface advice.**
- **Session.** Run QA-90 in the continuing Kronos session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV) on `amthorn78/glow-hdengine-v2`. It needs Notion read access for the QA-90 prompt.
- **Reads:**
  - Plan v1.3: §2, §3.2 E-L, §5.4 and §5.5, §7 rule A (with its state-(b) sub-bullet), check 13 and §9;
  - this review;
  - review v1.3 N-201;
  - addendum 2.28 (R-2; O-1);
  - the check 13 attempt-1 primary on `main` at `faa2246`.
- **Writes:** only the task record and its handoff under `docs/ephemeral/`, by pull request.
- **Not needed:** no execution while authoring the task, and no production, vendor, Railway or database access.
- **For the executor's venue:** the task asks for a full-history E-L clone at a state-(b) commit with CI's install. Step 1 takes about 25 minutes.

## Canon relied on

Read on `main` at `3d7c40ea`; this branch edits no `docs/pfcanon/` file. `docs/pfcanon/` is byte-identical to review v1.3's read (last changed by `21141b39`). Review v1.3's "Canon relied on" stays the basis for every topic not listed here.

| Decision topic | Sources read (title, version, sections) | Applied in |
| :- | :- | :- |
| Mode, criteria, routing | QA-70 — Review Whole-Change QA Plan — 100926.1 (page state 2026-10-12T02:29:54.691Z), read in full at review v1.3 in this session and unchanged: "Execute and decision criteria" 1, 2 and 4 ("decide `APPROVE` only if the whole pending Plan is coherent, complete, bounded, and executable"), "Required result and routing" (initial `APPROVE`: no addendum; QA-90 in the continuing Kronos session) | §1; handoff |
| Route for this decision | Product Owner direction v1.0 (D-2, D-3, §4, §5, CR-12), read in full at review v1.3 | Front matter; §1; §5 |
| Gate freeze; provenance | PF27-Canon-Plan-Templates v2.0.5 "Review stability and no-moving-target discipline" (read in full at review v1.3) | §4 |
| Candidate identity | PF27 v2.0.5 "VCS mutation and exact-source identity boundary (hard)"; `AGENTS.md` "Evidence attribution, currentness and distinct decisions" (read at review v1.3) | §3 RL-18 to RL-20 |
| Remediation verification | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6 (read in full at review v1.3); HDE Build Notes v13.8 addenda 2.27 (V-6) and 2.28 (R-2), read at review v1.3 | §3 RL-22; §6 |
| Blocker test | PF04-Canon-HDE-Governance v2.8.7 §9.8.3, §9.7.4, §9.7.7 (read in full at review v1.0; unchanged) | §4 |
| TypeSafe reading | HDE Build Notes 2.1; the installed TypeSafe scoring skill | §7 |

**In-flight documents read here:**
- Plan v1.3, through its full word diff against v1.2, with every changed region read in place;
- the redline application report v1.2, in full;
- the QA-80 checkpoint v1.2 and the QA-80 handoff v1.2.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-70-20261025-05 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | S20; QA Plan v1.3 (successor of approved v1.2); RL-18 to RL-22; remediation QA110-F01, WU-REM-02 |
| prompt | QA-70 — Review Whole-Change QA Plan — 100926.1, page state of 2026-10-12T02:29:54.691Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, QA-70, `INITIAL_QA_PLAN_REVIEW` by Product Owner direction D-2 |
| capture time | 2026-10-25T16:38:19Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-70-20261024-01 to -03 and -20261025-04 (reviews v1.0 to v1.3); GCFPE-USE-HDE-CRD-0002-QA-80-20261025-03 (Kronos, Plan v1.3) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
