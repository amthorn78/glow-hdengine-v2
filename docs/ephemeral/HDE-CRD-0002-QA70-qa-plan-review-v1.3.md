---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-CRD-0002-QA70-QA-PLAN-REVIEW
artifact_version: "1.3"
predecessor: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md (APPROVE of QA Plan v1.2; blob 502412897d6a; SHA-256 b33d38a25defc48348189b9846a4e8d4f476b72d566882c67414c9af323037ef; unchanged)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW, by the Product Owner's direction D-1 for this decision (direction §4); the approved Plan v1.2 is reviewed against the delivered WU-REM-02 change with no proposed delta
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING, as the direction applies the initial mode
prompt_mode: REVIEW
decision: DENY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
reviewer: Isis (Isis-53), continuing Lead Developer and QA Plan decision owner for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, the session of reviews v1.0 to v1.2 and of the ESC-40 remediation review for QA110-F01)
session_disposition: continuing Isis context, as the Product Owner direction names it (direction §7)
context_conflict: none
prompt: QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf; page state 2026-10-12T02:29:54.691Z, unchanged since review v1.0; read in full at this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_PLAN_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (QA_PLAN v1.2, approved by review v1.2 on 2026-10-24T14:52:19Z; blob 66f6016cc75b; SHA-256 8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9; 107,529 bytes, 728 lines; never edited; check 13, §2, §3.2, §5.4 to §5.6, §7 rules A and B, checks 1, 2, 11, 15, 16 and 21, §8, §9 and §11 re-read in full here)
PO_DIRECTION_ID: docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md (PRODUCT_OWNER_DIRECTION v1.0, D-1 to D-3 and CR-12; blob a2db4f362bf4; SHA-256 4731f41166ef58facc26159c28a530fa11a19095c3d318492c9c3c08171ba7ae; 17,467 bytes; read in full). It is not on main at this review: its commit 3727379b reached amthorn78/glow-hdengine-v2#735's branch at 15:44:46Z, one minute after #735 was squash-merged at 15:43:46Z, so squash a35ccc19 holds only the lineage review. This review's pull request carries that commit byte for byte (§2, N-204)
LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-work-unit-lineage-review-v1.0.md (PR-40 ACCEPT of #734; blob 7f0fc054a01e; SHA-256 134b9d1f2a0bee11787592d0c28983ef65e14e5c85a87a6d1bc0e3c1a3ff51d0; read in full)
DELIVERED_CHANGE: amthorn78/glow-hdengine-v2#734, squash 22a3bc040a60c75b089a629172a5d829f20d8e98 (tree c92ff9004856dc5feead6735dd50ef9b5f7d8bbd): tools/ci/prepush_check.py, tests/tools/test_prepush_check.py, README.md
REMEDIATION_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md (ESC-40 APPROVE_AS_CHANGED with C-1; blob 324ab0552f02; this reviewer's own record), with addendum 2.27 as published in PF10 v13.8
QA_EVIDENCE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md (blob 0a797250aa81; rulings R-1 and R-2), as addendum 2.28 records it
ESCALATION_REPORT_ID: docs/ephemeral/HDE-CRD-0002-ESC10-qa-escalation-report-v1.0.md (QA110-F01; blob 2cfc8e558a32)
QA_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE; unchanged; §7 items 2 and 9 re-read)
author: Kronos, the QA authority and QA Plan author for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (568,847 bytes; SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c). v13.7.8 to v13.7.9 adds 2.27; v13.7.9 to v13.8 adds 2.28 and its index line. 2.28 read in full; 2.27 read at its C-1, V-1 to V-6, "Epic, task, and status effects" and obligations lines
repository_head_read: origin/main 21141b392eaecb94be0f82044fc1a6713612e089 ("PF10", after a35ccc19, #735); code outside docs/ephemeral/ and docs/pfcanon/ equal to 22a3bc0's
PF10_ADDENDUM_OUTPUT: NONE (an initial-mode DENY produces no addendum; direction §5, "No PF10 addendum records the Plan change")
canon_conflict_register: CR-1 to CR-11 carried unchanged; CR-12 APPROVED (Product Owner), carried from the direction §6; no new conflict (§5)
decision_time_utc: 2026-10-25T16:14:31Z
next_prompt: QA-80 — Revise Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8), the same Kronos author, with approved Plan v1.2 as its target by direction D-2
handoff: docs/ephemeral/HDE-CRD-0002-QA70-handoff-to-qa80-v1.2.md
---

# HDE-CRD-0002 — QA Plan Review v1.3 (QA-70, approved Plan v1.2 against the delivered WU-REM-02 change)

## 1. Decision

**`DENY`.** Approved QA Plan v1.2 cannot verify the QA110-F01 remedy as written. It needs five redlines (§6), and under direction D-2 they go to Kronos at QA-80. The approved bytes of v1.2 stay unedited; the revision is a successor file.

- **FND-201 (Blocker).** Check 13 step 3 expects "137 passed". The delivered owner test has 141 tests, and all 141 pass on `main`. A correct tool would therefore be judged `FAIL_BEHAVIOR`. This is C-1's item, raised at ESC-40 and still unresolved.
- **FND-202 (Blocker).** The Plan's tested source is code equal to `0b15328d`'s (§2). Check 1's guard, common rule A, check 21's copy guard and §5.4's evidence checkout all enforce that. No commit has both that code and the remedy. So either:
  - check 13's verification (addendum 2.27 V-6) tests the old tool and reproduces QA110-F01; or
  - at `main`'s code, every remaining execution stops `TOOLING_BLOCKED` ("candidate changed").

  Checks 16 to 21 are caught the same way, so S22 and §11's `verdict: PASS` cannot be reached.
- **FND-203 (Caveat).** §9 gives no evidence identity for check 13's next execution. QA-110 ruling R-2 consumed check 13's one ordinary rerun, and addendum 2.28 records that the next execution "is the remediation route's verification and return (Glow QA Guide §10.6 step 5), not an ordinary attempt 2 and not a reset". The Plan does not say how that execution is labelled, recorded or published.

**A correction of my own earlier conclusion.** At ESC-40 I approved C-1, which addendum 2.27 records as "QA Plan v1.2 check 13: step 3's count changes through C-1's delta. The rest of the check is unchanged." That is true of check 13's text, but it missed a coupled constraint: the Plan's candidate pin (§2, check 1, rule A, §5.4) also has to move to the remedied code.
- FND-202 and FND-203 are that omission, classed Review Drift (§4).
- They are not author churn (Plan Templates "Non-author penalty rule").
- Addendum 2.27 is not edited (direction §5).

**What stays as it is:**
- check 13's objective, target, the step 1, 2 and 4 predicates and its Outcomes line (C-1);
- every other check's actions and predicates;
- the fourteen accepted results (checks 1 to 12, 14 and 15). They stay attributed to the state they tested; an explicit comparison shows the three-file change leaves what they assert unchanged (§3), so none is re-executed.

## 2. Review method and independent checks

All under closed rails (`env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, an empty scratch `HOME`), in a fresh `--no-hardlinks` full-history scratch clone of `main`, detached at `21141b39`:
- `git rev-parse --is-shallow-repository`: `false`;
- no alternates;
- CPython 3.12.3 venv with CI's install (the ESC-40 rehearsal venv), with `PYTHONPATH` set to the clone, and `tools.ci.prepush_check` resolving inside it.

Nothing from the clone was committed or pushed.

| # | Check | Result |
| :- | :- | :- |
| 1 | `python -m pytest -p no:cacheprovider --collect-only -q tests/tools/test_prepush_check.py` | `141 tests collected`, exit 0 |
| 2 | `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` (check 13 step 3's command) | `141 passed in 138.80s`, exit 0; `git status --porcelain` empty afterwards (2026-10-25T16:13:41Z) |
| 3 | Check 1 step 1's guard as written, on `main`: `git diff --stat 0b15328d585a764c124936b4524b766525daf1d9 origin/main -- . ':!docs/ephemeral' ':!docs/pfcanon'` | 45 files. 42 are #726's evidence (`audit/qa/hde-crd-0002/**` and the ten updater-owned graph files). The other 3 are `README.md`, `tests/tools/test_prepush_check.py` and `tools/ci/prepush_check.py` |
| 4 | The same diff from QA-100's tested source `2e03a2686af87ab0607c6cfb9afb4ad79bcdb171` (tree `af5293473238`) | The same 45 files: that commit's code equals `0b15328d`'s |
| 5 | Candidate delta with §2's evidence-only paths excluded: `git diff --stat 0b15328d 22a3bc0 -- . ':!docs/ephemeral' ':!docs/pfcanon' ':!audit/qa/hde-crd-0002' ':!docs/evidence/INDEX.*' ':!artifacts/evidence_index.jsonl*' ':!audit/gates/topology/orientation_demo.txt*'` | Exactly the three WU-REM-02 files (+164/−19). The same from `2e03a268` names the same three |
| 6 | The redlined E-L guard on `main`: `git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'` at `21141b39` | Empty |
| 7 | Release membership of the three files (`grep -c` in `catalog/manifest.json`) | 0 each; release `1.3.0` and its `release_id` are unchanged |
| 8 | Check 15 step 4's read, `grep -c 'omits 16 of the 45' README.md`, at `21141b39` | `1`; the README change is two lines in the pre-push section (`git diff 0b15328d origin/main -- README.md`) |
| 9 | Plan text: every reference to `0b15328d`, "tested source", "tested commit", `README` and `prepush` | §3 and §6 anchors; no other check reads the three files |
| 10 | Canon search, `git grep -n -i -E 'tested source\|candidate guard\|re-?verification\|remediation verification'` and `'candidate (changed\|guard)\|new candidate'` on `origin/main -- docs/pfcanon/` | Plan Templates "VCS mutation and exact-source identity boundary (hard)" ("treat a later push as a new candidate unless rerun evidence or an explicit comparison proves the relevant reviewed and tested scope unchanged"); PF10 2.28 "Re-verification of check 13 after a repair \| Kronos"; no rule on how a QA Plan re-pins its candidate after a remediation |
| 11 | The direction's presence on `main` | Absent from `a35ccc19` and `21141b39`; present at `3727379b` on `docs/20261025-hde-crd-0002-wu-rem-02-pr40`. That commit is cherry-picked onto this review's branch with its author and message; the blob, `a2db4f362bf4`, is unchanged |

Corroborating records, read and not re-run:
- lineage review §8 at `22a3bc0`: V-1 141 passed; V-2 step 1 exit 0 with every report `PASS` and "repository unchanged", in 1,625 s; step 2 exit 0;
- push run 40203695760 on `22a3bc0`: changed tests 141 passed.

## 3. Impact of the delivered change on the accepted results

The candidate moves by three files that are not release members (§2 rows 5 and 7). Plan Templates' explicit-comparison rule and `AGENTS.md` "Evidence attribution, currentness and distinct decisions" ("Explain an affected conclusion and route only the needed focused review, revision or retest through its existing owner. A changed/different/unavailable SHA alone does not revoke approval, require reapproval, freeze the repository, trigger automatic reruns or require a routine scope-equivalence certificate.") apply.

| Accepted check | Reads one of the three files? | Effect |
| :- | :- | :- |
| 1 `qa-01-preflight` | `test -e tools/ci/prepush_check.py`; collects the owner test "at least" the Audit's 137; the guard against `0b15328d` | Existence and "at least" still hold (141). The guard identity is what FND-202 changes; check 1's executed result stays as recorded, and later executions record their own candidate reads (RL-19) |
| 2 `qa-02-ci-coverage` | Step 1 runs one node in the owner module, `test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository` | The module gained tests only (+87/−0); the node is unchanged and passes at `22a3bc0` (§2 row 2; lineage V-1; push run 40203695760). Check 13 step 3 re-exercises it at the new candidate. No retest |
| 15 `qa-15-s01-removal` | Step 4 reads `README.md` | Count still `1` (§2 row 8). No retest |
| 3 to 12, 14 | None (§2 row 9) | None |

**Conclusion:**
- The fourteen accepted results stay attributed to the state they tested: `2e03a268`, tree `af5293473238`, code equal to `0b15328d`.
- They are not re-executed. QA-120 reports both tested states (RL-18).
- Evidence authority over them stays Kronos's (QA-110).
- That checks 1 to 15 ran under v1.2 while the run continues under its successor does not reopen them: no predicate of theirs changes (§6).

## 4. Findings

**Blocker test.** As in reviews v1.0 and v1.1:
- HDE-Governance §9.8.3: "A Blocker is only an issue that prevents the operator from executing the plan in the target environment or prevents reviewers from determining pass/fail for the in-scope behavior with confidence";
- §9.7.7, "Live QA Plan approval blockers are operational only";
- a Caveat states its deviation and why it does not block (§9.7.4).

**Provenance** (Plan Templates "Review stability and no-moving-target discipline"):
- Every finding sits in text unchanged since the approval.
- Each finding's trigger is a newly supplied authoritative input: #734's merge as `22a3bc0` and the PR-40 ACCEPT, both after review v1.2's approval.
- Classes:
  - FND-201: **Previously raised and still unresolved** (C-1, ESC-40).
  - FND-202 and FND-203: **Review Drift**, this reviewer's. The coupled constraint was visible at ESC-40, when C-1 named the change to Plan v1.2. They are consolidated here under the "Review Drift handling" rule, so nothing more from that family is drip-fed in a later round.
- Every triggering input is real (HDE Build Notes 2.11 rule 4, as 2.18 leaves it): the code on `main` and the venue check 13 already ran in.

### FND-201 — Blocker — Check 13 step 3's expected count no longer matches the owner test

- **Region:** Plan v1.2 line 422 ("Step 3 \"137 passed\"; step 4 empty."); coupled line 424 ("Every line above was observed at `0b15328d` (Audit §7 item 9)").
- **Defect (O).** Step 3 runs `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py`. WU-REM-02's R-4 added four test items to that module (addendum 2.27; lineage review §5), and nothing was removed. It now collects 141 and passes 141 (§2 rows 1 and 2; lineage review §8 V-1; push run 40203695760).
- **Why it blocks.** Under the predicate as written, a correct tool and owner test produce "141 passed", which contradicts the explicit predicate. Common rule B then gives `FAIL_BEHAVIOR`. Reviewers cannot determine pass or fail for S20 with confidence (§9.8.3).
- **Correction scope (C-1).** Step 3's count and its provenance sentence only.

### FND-202 — Blocker — The tested source is pinned to the code without the remedy

- **Regions:**
  - line 84 (§2 "Candidate": "Tested source: the commit on `main` at execution whose code outside `docs/ephemeral/` and `docs/pfcanon/` equals `0b15328d`'s (that code equals `3a5d846`'s; Audit §2). Check 1 records the exact commit and enforces this guard");
  - lines 231, 242 and 243 (check 1 step 1's `git diff --stat 0b15328d585a764c124936b4524b766525daf1d9 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'`, with "the diff is empty" in the predicate, and "a non-empty step 1 diff or a different `release_id` → `TOOLING_BLOCKED` (\"candidate changed\"), stop the run and route to Kronos");
  - line 209 (rule A: "`git rev-parse HEAD` equals the tested commit check 1 recorded");
  - line 210 (check 21's copy, read (i): `git diff --stat 0b15328d585a764c124936b4524b766525daf1d9 -- .` and the status read, each with the evidence-path exclusions, "each print nothing");
  - line 151 (§5.4: "at or after the tested source (code identical)" and "its history holds `0b15328d`");
  - line 616 (§11: "The report states: the tested commit and tree").
- **Defect (O).**
  - The code that satisfies the guard is `0b15328d`'s, which is the tool QA110-F01 found defective. The remedy changes `tools/ci/prepush_check.py`, so no commit has guard-equal code and the remedy (§2 rows 3 to 5).
  - A check 13 execution that meets rule A (HEAD equals check 1's recorded `2e03a268`) runs the old `make_copy` with `--shared`. On a full-history E-L clone that reproduces exit 4: the QA-100 workstation result, and V-3 of the lineage review.
  - An execution at `main`'s code fails rule A for checks 2 to 15. If check 1 were re-run, its guard would print the three files.
  - Check 21's copy is taken from an evidence checkout cloned from `main`, so it holds the three files and its guard (i) prints them. §5.4's "at or after the tested source (code identical)" cannot be met from `main` after `22a3bc0`.
- **Why it blocks.**
  - The operator cannot execute addendum 2.27's V-6 ("Kronos verifies check 13 in the QA-100 venue class (E-L, full history) under the Plan as amended") against the remedied code in any target environment.
  - Run as written, it tests the unremedied tool, so its result cannot show whether the remedy works.
  - Check 21 stops at readiness, so S22 is unproven, and §11 forbids `verdict: PASS` while any check is not `PASS`.
- **Correction scope.**
  - A second, attributed tested state for every later execution, the commit `22a3bc0` (RL-18).
  - Each later E-L execution records its own candidate reads (RL-19).
  - The two copy and checkout guards move to the new base (RL-20).
  - Check 1 itself is not re-executed and no accepted result is reopened (§3).
- **Real input.** The code on `main` and the E-L venue the Plan prescribes.

### FND-203 — Caveat — No evidence identity for check 13's remediation verification

- **Region:** §9, lines 582 to 585 (one ordinary rerun, "only Kronos's actual QA-110 decision allows attempt 2"; escalation "through the ESC-10 remediation route").
- **Defect (O).**
  - R-2 ruled that "each check's one ordinary rerun is consumed, so no attempt 2 remains for check 3 or check 13", and that "a later execution of check 13 after a repair is the remediation route's verification and return (Glow QA Guide §10.6 step 5), not an ordinary attempt 2 and not a reset" (addendum 2.28).
  - §5.5 requires each returned proof to carry "the attempt number".
  - §9 names only attempts 1 and 2, so the Plan does not say how that execution is labelled or what its primary carries.
- **Why it does not block (§9.7.4).** §9's escalation bullet already routes through Glow QA Guide §10.6, whose step 5 and "Evidence-package caveats and failure history" govern the return. QA-90 could author the task from canon. The Plan should still state it, so the task and QA-110 judge one recorded identity. The correction rides the same revision.
- **Correction scope:** one §9 bullet (RL-22). The attempt label it records is Kronos's (direction §4: "attempt accounting, which stays Kronos's").

### Non-gating notes (no correction required)

- **N-201: O-1 venue caution, for QA-90.** Attempt 1's replay step 08 failed in `tests/ops/test_hde_epic038_ops03.py` (`EXDEV`) because `TMPDIR` sat on another filesystem than `/tmp`. The Moon Loop that unset `TMPDIR` removed that cause (addendum 2.28). O-1 stays undecided with Thoth and the Product Owner, so the verification task should record the shell's `TMPDIR` posture. This review decides nothing about O-1.
- **N-202: PF10 is now v13.8.** Check 13 step 1's build-notes predicate already admits "the single PF10 file then on `main`, recorded as a CAVEAT", and check 15 step 1 "the PF10 file in force, recorded". No redline.
- **N-203: O-A.** The owner test's own `--shared` fixtures re-time the E-L clone's pack during step 3 (lineage review §8). Step 3 runs after step 1's guarded window, and step 4 reads `git status` only, so no predicate is affected. O-A stays with the Product Owner.
- **N-204: input gap, closed by this pull request.** The direction file missed #735's merge (front matter). This review's pull request carries commit `3727379b` unchanged (blob `a2db4f362bf4`). It must merge before QA-80 starts.

## 5. CANON_CONFLICT_REGISTER

- **Carried unchanged** as Plan v1.2 §13 records them: CR-1 to CR-8 and CR-10. CR-9 stays `PROPOSED` (Isis, IA-30 boundary). CR-11 stays `APPROVED_AS_CHANGED`, alternative (a) (review v1.0 §5).
- **CR-12:** `APPROVED` by the Product Owner, 2026-10-25, alternative (a), as the direction §6 records it field for field. This review applies it:
  - the mode (§1);
  - the route to QA-80 with approved Plan v1.2 as its target;
  - no addendum.

  QA-80 carries CR-12 into the successor Plan's §13 (§6).
- **New conflicts:** none. FND-201 to FND-203 are Plan defects under undisputed canon. Canon is silent on how a QA Plan re-pins its candidate after a remediation (§2 row 10), and the redlines rest on the Plan's own guard design and Plan Templates' explicit-comparison rule.

## 6. Redlines for QA-80

One-pass bundle (Plan Templates "Redline bundle construction discipline"):
- Anchors are line numbers of approved Plan v1.2, and no two regions overlap.
- Values that must be used are given exactly. Kronos chooses the wording around them.
- QA-80's bookkeeping follows its prompt: front matter, the successor version and its predecessor (v1.2, approved, immutable), §13 with CR-12, §14, §15, Canon relied on and provenance.

| ID | Base region (Plan v1.2) | Required outcome | Finding |
| :- | :- | :- | :- |
| RL-18 | Line 84 (§2 "Candidate"); line 616 (§11 "The report states") | §2 defines the tested source in two attributed states. **(a)** Checks 1 to 12, 14 and 15 as executed and accepted: `2e03a2686af87ab0607c6cfb9afb4ad79bcdb171`, tree `af5293473238`, code outside `docs/ephemeral/` and `docs/pfcanon/` equal to `0b15328d`'s. They are not re-executed. **(b)** Every later execution, that is check 13's remediation verification and checks 16 to 21: a commit on `main` whose tree outside `docs/ephemeral/` and `docs/pfcanon/` equals `22a3bc040a60c75b089a629172a5d829f20d8e98`'s (tree `c92ff9004856dc5feead6735dd50ef9b5f7d8bbd`). That is `0b15328d`'s code plus #726's evidence and WU-REM-02's three files from #734. §2 states that release `1.3.0` and its `release_id` are unchanged, because none of the three files is a release member, and cites §3 of this review for the comparison. §11's report states both tested states and which checks each covers | FND-202 |
| RL-19 | Line 209 (§7 rule A, "E-L and E-D" bullet); lines 231, 242, 243 (CHECK 1 step 1, PASS predicate, Outcomes) | Check 1's text and accepted result stay as executed. A state-(b) E-L execution records, under its own `=== CONTEXT ===` before its main commands, check 1 step 1's reads with the new base: `git rev-parse HEAD`; `git rev-parse HEAD^{tree}`; `git rev-parse --is-shallow-repository` (`false`); `git cat-file -e '7136040^{commit}'`; and `git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'` (empty). It also records check 1 step 2's `sha256sum catalog/manifest.json` and `hdctl --version` reads, with check 1's expected values. For such an execution, rule A's "equals the tested commit check 1 recorded" reads "equals the tested commit its own candidate reads recorded". A non-empty diff or a different `release_id` is `TOOLING_BLOCKED` ("candidate changed"), as check 1's Outcomes line maps it | FND-202 |
| RL-20 | Line 210 (§7 rule A, check 21's test copy, read (i)); line 151 (§5.4 "Evidence checkout") | In read (i), the base `0b15328d585a764c124936b4524b766525daf1d9` becomes `22a3bc040a60c75b089a629172a5d829f20d8e98`. The pathspec stays the same (it prints nothing on `main` at `21141b39`, §2 row 6, with the exclusions as well), and the history sentence names `22a3bc0`. In §5.4, "at or after the tested source (code identical)" names state (b), and "its history holds `0b15328d`" becomes "its history holds `22a3bc0`" | FND-202 |
| RL-21 | Lines 422 and 424 (CHECK 13 PASS predicate and its provenance sentence) | Line 422: "Step 3 \"141 passed\"; step 4 empty." Line 424 states where each value was observed:<br>- step 3's 141 at `22a3bc0` (WU-REM-02 lineage review §8 V-1; push run 40203695760) and at `21141b39` (this review §2 row 2);<br>- the step 1 and step 2 lines at `0b15328d` (Audit §7 item 9) and again at `22a3bc0` (lineage review §8 V-2, whose build-notes line names PF10 v13.7.9, the CAVEAT form);<br>- step 1 took about 27 minutes there.<br>The step 1, 2 and 4 predicates and the Outcomes line are unchanged (C-1) | FND-201 |
| RL-22 | §9, a new bullet after line 585 ("Escalation") | "Remediation verification (check 13, QA110-F01)". It states:<br>- check 13's next execution is the remediation route's verification and return (Glow QA Guide §10.6 step 5; addendum 2.27 V-6), not an ordinary attempt 2 and not a reset (QA-110 review v1.0 ruling R-2; addendum 2.28);<br>- it runs at state (b) (RL-18, RL-19) in E-L with full history, with the same `check_id`, rails, environment class and deliverable;<br>- its primary opens its notes with the attempt-1 failure signature (exit 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION`, finding QA110-F01) and names the remedy (#734, squash `22a3bc0`);<br>- the `FAIL_BEHAVIOR` primary committed on `main` at `faa2246` stays the visible failure context (Glow QA Guide §10.6 "Evidence-package caveats and failure history");<br>- publication merges by `check_id` (§5.4), so git history keeps attempt 1's bytes;<br>- the attempt label it records, and returns under §5.5, is the one Kronos sets | FND-203 |

## 7. Coverage after correction

- **Unchanged:** S02 to S22 keep their checks (Plan §10), and S01 keeps check 15. The Live QA minimum stays checks 17 to 19 plus check 20. No check is added, removed, parked or rescoped.
- After RL-18 to RL-21, check 13 can verify S20 on the remedied code. After RL-20, check 21 can reach its decisive point, so S22 is provable again.
- The fourteen accepted results stand as attributed (§3).

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Successor QA Plan per §6, with an item-by-item application report | Kronos, QA-80 (direction D-2) | Next, after this review's pull request merges |
| Review of the successor | Isis, QA-70, `INITIAL_QA_PLAN_REVIEW` | After QA-80 |
| Check 13's remediation verification (V-6), from the Plan Isis approves | Kronos, QA-90 (direction D-3) | After approval |
| O-1 (OPS03 `EXDEV`) | Thoth; Product Owner if independent | Open (N-201) |
| O-A, D-1/LR6-O1, FND-028 | Product Owner | Unchanged |
| Selection of checks 16 to 21; check 20's venue and initiator | Product Owner, at QA-90 | Not selected |
| The QA-70/QA-80 route gap for an approved-Plan change | GCFPE-MGMT-10 maintenance owner (direction §7) | Reported there; not repeated |
| CR-9 | Isis, IA-30 boundary | `PROPOSED`, unchanged |
| CR-11 permanent drainage | Product Owner | Not a condition of the run |
| G-1, PO-2 and PO-5 drainage, O-2 to O-4 | As addendum 2.28 records them | Unchanged |

## 9. TypeSafe reading for the receiving session (QA-80)

Action sent (v8.2): "As its original author, revise one already approved whole-change QA plan of 21 separately verifiable checks (about 730 lines) that its independent reviewer has now denied after a three-file remediation merged, applying exactly five required redlines on about ten lines: redefine the tested candidate and its read-only guards so the remaining executions test the remediated code while fourteen accepted results stay attributed to the earlier code, change one expected test count from 137 to 141, and state how the one failed check's remediation verification is identified and recorded; then write an item-by-item application report, changing nothing else. It is a Markdown record only: no task list exists for this revision, no live run against a provider occurs, and an independent re-review, a bounded task, its execution and an evidence review follow."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 1.86 (confidence 0.81). Rung probabilities: low 0.00, medium 0.22, high 0.71, extra high 0.07, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.90, Sonnet 5.5 0.09, Haiku 5.5 0.00 (confidence 0.87).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.198, Opus 5.5 at high 0.639, Opus 5.5 at extra high 0.063, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.020, Sonnet 5.5 at high 0.064, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Sent 2026-10-25T16:13:27Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-25T16:13:27Z; HTTP 200 in 0.54 s; 5512 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`. It was run once with session kind `review` and label "QA-80 HDE-CRD-0002 QA Plan v1.2 revision after QA-70 review v1.3 DENY (C-1 route)", before this review was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - QA-80: Nathan's pick is not stated.
  - This QA-70 session: Nathan's pick is not stated. Its reading is in the direction §8 (Opus 5.5 at high, score 2.09).

**Surface advice.**
- **Session.** Run QA-80 in the same Kronos author session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV) on `amthorn78/glow-hdengine-v2`. If it cannot be continued, Nathan creates a top-level Claude Code cloud session for the Kronos role on the same repository, and the revision records that.
- **Reads.**
  - Notion read access for the QA-80 prompt.
  - This review and the direction (§4 and §5: QA-80's target and the superseded `WRONG_ROUTE_APPROVED_BASE`).
  - Plan v1.2, and the application reports v1.0 and v1.1.
  - The lineage review §4, §5 and §8; addenda 2.27 and 2.28 in PF10 v13.8.
- **Optional re-checks.** Each runs offline in a full-history scratch clone in under a minute:
  - §2 rows 3 to 6 (the guard diffs);
  - row 1 (the owner test's collected count).

  The 24-minute step 1 is not needed.
- **No access needed:** production, the vendor, Railway or the database; no evidence publication.
- **Writes:** only the successor Plan, its application report, a checkpoint and the handoff, under `docs/ephemeral/`, by pull request.
- **Order:** this review's pull request merges first. It also carries the direction, which missed #735.

## Canon relied on

Read on `main` at `21141b39`; this branch edits no `docs/pfcanon/` file. Since review v1.0 (`55465c2`), `docs/pfcanon/` has changed only by the two PF10 commits (`c4915904`, `21141b39`). Every other PF source cited here is byte-identical to the version read at reviews v1.0 to v1.2.

| Decision topic | Sources read (title, version, sections) | Applied in |
| :- | :- | :- |
| Mode, decision states, routing, artifacts | QA-70 — Review Whole-Change QA Plan — 100926.1 (page state 2026-10-12T02:29:54.691Z), read in full at this invocation: "Required inputs and review mode", "Execute and decision criteria" 2 and 4, "Required result and routing", "Runtime artifact and handoff contract" | §1, §6, §9, handoff |
| The Product Owner's route for this decision (scoped override) | `docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md`, read in full: D-1 to D-3; §4 (QA-70 initial mode; QA-80's target; QA-90 return; "A redline beyond step 3's count is Isis's to ground in evidence against that approval"); §5 (supersessions, no addendum); CR-12. `AGENTS.md` "Canon-first rule" ("a formally approved bounded Product Owner rescope supersedes it for the exact decision it adjudicates") | Front matter; §1; §5; RL-22's attempt label |
| QA-80's target and outputs | QA-80 — Revise Whole-Change QA Plan — 100926.1 (page state 2026-10-12T02:30:18.516Z), read in full at this invocation: "Required inputs", "Controlled sources, overlays, and revision boundary", "Execute", "Required result and routing", as the direction supersedes `WRONG_ROUTE_APPROVED_BASE` for this decision | §6 bookkeeping; handoff |
| Blocker and caveat test | PF04-Canon-HDE-Governance v2.8.7 §9.8.3, §9.7.4, §9.7.7, §9.8.2 (read in full at review v1.0; unchanged) | §4 |
| Revision-loop provenance | PF27-Canon-Plan-Templates v2.0.5 "Review stability and no-moving-target discipline", read in full here: gate freeze triggers ("a newly supplied authoritative input"), "Coupled-constraint rule", "Unchanged-text blocker rule", "Review Drift handling", "Non-author penalty rule", the three provenance classes | §1; §4 provenance |
| Candidate identity after a change | PF27 v2.0.5 "VCS mutation and exact-source identity boundary (hard)", read here ("treat a later push as a new candidate unless rerun evidence or an explicit comparison proves the relevant reviewed and tested scope unchanged"; "They MUST NOT instruct branch creation, checkout, commit, push, merge, rebase, PR creation, or another VCS mutation as part of QA execution"; the redlines add read-only `git` observations only); `AGENTS.md` "Evidence attribution, currentness and distinct decisions" | §3; RL-18 to RL-20 |
| Status mapping | PF27 v2.0.5 "Exact status predicates" and "Causal precedence" (read in full at review v1.1); Plan v1.2 §7 rule B | FND-201, FND-202 |
| Remediation return, attempts, failure visibility | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6, read in full here: "Common remediation cycle and return owner" step 5 ("Later QA retains Kronos's evidence/Plan responsibilities and actual return stage"), the attempt-limit paragraph ("Nominal remediation cycles must not reset attempts or bypass that limit"), "Evidence-package caveats and failure history" | FND-203; RL-22 |
| The approved remedy, C-1, V-6 | HDE Build Notes v13.8 addendum 2.27 (C-1, V-1 to V-6, "Epic, task, and status effects", obligations); remediation review v1.0 §4 (this reviewer's) | §1 correction; FND-201, FND-202 |
| QA-110 rulings; O-1; the QA-100 venue | HDE Build Notes v13.8 addendum 2.28, read in full (R-2; QA110-F01 observed and venue lines; O-1; the Moon Loop) | FND-203; N-201 |
| Delivered change | Lineage review v1.0, read in full (§3 to §5, §8); `git diff` of `0b15328d`, `2e03a268`, `22a3bc0` and `21141b39`; `catalog/manifest.json` | §2, §3 |
| Real inputs | HDE Build Notes 2.11 rules 4 to 7, as 2.18 leaves them (read at review v1.0; unchanged in v13.8) | §4 |
| Repository rules | `AGENTS.md`: closed rails, "Pytest readiness rule", truncation guardrail, "QA output placement", PR descriptions | §2; publication |
| TypeSafe reading | HDE Build Notes 2.1; the installed TypeSafe scoring skill | §9 |

**HDE Build Notes.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md` (SHA-256 above) is the version in force. v13.7.8 was read in full at QA-20 in this session. The v13.7.8 to v13.8 diff adds only 2.27, 2.28 and their index lines: 2.28 was read in full here, and 2.27 is this reviewer's own record, read at the lines cited.

**Searched and silent:** canon names no procedure for re-pinning a QA Plan's candidate after a remediation lands (§2 row 10). The redlines therefore rest on the Plan's own guard design and on PF27's explicit-comparison rule.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-70-20261025-04 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | S20; QA Plan v1.2 (approved), check 13 and its candidate (§2, check 1, rule A, §5.4, §9, §11); remediation QA110-F01, WU-REM-02 |
| prompt | QA-70 — Review Whole-Change QA Plan — 100926.1, page state of 2026-10-12T02:29:54.691Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, QA-70, `INITIAL_QA_PLAN_REVIEW` by Product Owner direction D-1 |
| capture time | 2026-10-25T16:14:31Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-70-20261024-01 to -03 (reviews v1.0 to v1.2); the ESC-40 use of the remediation review v1.0; GCFPE-USE-HDE-CRD-0002-PR-40-20261025-WU-REM-02-01 and -02 (lineage review; direction record) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
