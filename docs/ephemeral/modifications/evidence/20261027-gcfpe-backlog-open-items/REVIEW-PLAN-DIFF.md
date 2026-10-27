0 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-DIFF — PLAN of MODIFICATION-20261027-gcfpe-backlog-open-items, check of the round-1 repair's diff

- **Reviewer:** REVIEWER-PLAN-DIFF-C. I did not write this plan, and I was not reviewer A or B.
- **Brief:** `BRIEF-PLAN-DIFF.md` (branch head `6474eca`). Rubric and cap: `BRIEF-PLAN-1-A.md` §3 and §5, applied as written.
- **Checked:** `git diff f2346b2 885638d`, 15 files. Every file was read from commit `885638d`, not from the branch head.
- **Canon:** `docs/pfcanon/` at `885638d` matches `origin/main` `91925e9` (the `git diff` is empty).
- **Mode:** read-only.
  - The only repository file I wrote is this record. I made no Notion write and edited no prompt body.
  - I ran tools only on a `git archive` copy of `885638d` in the session scratchpad, which I then deleted.
  - I set `PYTHONDONTWRITEBYTECODE=1`.

## Answer first

- **All four required findings are fixed: R-1, R-2, R-B1 and R-B2.** None was fixed with a new defect.
- **No new required defect.** I attacked every point the brief names, and each held. Each weakness I found ends in a loud stop or is cosmetic, so D26-A rule 3 lists it rather than requiring it.
- **8 LISTED** (L-D1 to L-D8).
- **Trend:** 4 required defects in round 1, 0 now.
- **This is D26-A's one check of a repair's diff.** Under §5 the output now goes to Nathan with every open finding listed. Zero findings is not what ends the review: the review ends because D26-A's diff check is now spent.
- **Closing state:** DECISION NEEDED.

## Disposition of the round-1 required findings

### R-1 (R1, R4): **fixed**

**The applier.**
- `plan/repo_edits_102726.py` reads the design returns' own `repo_edits`: W6-RE-19/20/21/28 for X1, and RE-W7-03 to RE-W7-11 and RE-W8-01 to RE-W8-08 for X26. Nothing is retyped, except W1's note anchor.
- The note is re-anchored on D30's closing line. W1's text (its `new` minus its `old`) is kept.

**What I ran on the scratch copy:**
- `selftest`: 14 of 14 cases pass.
- X1 `check --state before`: ok. 20 edits on 5 files, each `old` string at count 1. The 7 `repository` guards are at W6's counts (19F 4, 19R 0, 20R 0, 21F 2, 21R 0, 28F 1, 28R 0).
- X1 `apply`: 5 files written.
- X1 `check --state after`: ok. The guards are 0, 2, 1, 0, 4, 0, 1, which matches PLAN X1. The note heading occurs once and comes after `## D30`. v5.0.0 is equal to `main`.
- A second X1 `apply` is refused (`NEW_FILE_EXISTS` / `OLD_COUNT`) and writes 0 files.
- X26 without values is refused (`UNFILLED_MARKER`). With `--stand-in-values` it applies to 3 files, and its after-check is ok: the promotion heading occurs once, and the earlier entries are a byte prefix.

**Wrong-span checks.**
- In both sets, no edit's `new` contains a later edit's `old` in the same file, and no two `old` strings overlap. So `replace(old, new, 1)`, guarded by "count 1 before and at application", cannot land inside an earlier replacement.
- `apply` writes nothing unless its in-memory after-check passes.
- Stand-in values are refused on the real tree.
- N11 and the self-test run only on scratch copies.

**The `notion-control` guards.**
- `activation_render_102726.py` now evaluates them for `part17`:
  - In `plan`: on the read before the operations, at W6's before counts, and on the rendered text after them.
  - In `check`: on the fresh read.
- I tested this on my own fresh reads of the Hub and the register, fetched after 2026-10-27T11:01:53Z:
  - **Revisions:** the Hub is still at 2026-10-27T03:02:37.191Z, and the register at 2026-10-12T17:17:45.991Z.
  - **Unpinned:** the Hub is refused (`PIN_REQUIRED`).
  - **Pinned:** 24 operations applied, 0 refused. Before: HUB-F 13, RH 0, RN 0, RP 0; REG-F 4, RN 0. After: 0, 4, 2, 2; 2, 2, every guard passing.
  - **`check --phase part17` on the unedited reads:** fails, exit 1, with every `notion-control` guard listed. So X8 can no longer pass with a surviving retired line.
- Self-tests:
  - `activation_render_102726.py selftest`: 24 of 24.
  - `make_activation_ops_102726.py check` and `selftest`: pass.
  - `body_check.py selftest`: 118 guards, 377 fixture rows.

**Commands named.**
- X1, X8 and X26 name the commands, in both §P and PLAN §5.
- `run` now carries N10's PART-17 guards, N11 and N12, so X0(f) runs them.

### R-2 (R3): **fixed**

**What was reverted.** All four L-C1 widenings were removed, and now read by work unit:
- `edits.json` W2-IA-30-BC-2 lost its "including a unit whose acceptance criterion or outcome …" clause.
- W2-IA-30-EM-2 reads "For every work unit the delta adds or changes, an acceptance criterion that depends on emulating an external system …".
- `guards.json` G-W2-BC-4 and G-W2-EM-2 are cut by work unit, with fixtures that fail the acceptance-criterion cut.
- PART-03 and PART-04 cite ITEM-14's and ITEM-15's frozen cut, and say that L-C1 stays an accepted risk.

**Checks.**
- `assemble_edits.py --check` and `assemble_guards.py --check` both report current.
- A `git grep` of `plan/` (outside `work/` and the receipts), of `docs/prompt_ecosystem_management/` and of `docs/graph/` finds no remaining widening text. What it does find are C-24's notes and the N12 injection strings.

**D30 now states exactly DN-3 (b) for ITEM-15 and ITEM-17, and nothing wider.**
- **D30-A against ITEM-15.** The delta bullet now reads "In `MATERIAL_PLAN_DELTA_REVIEW`, for every work unit the delta adds or changes, such a criterion is a ground for `DELTA_DENY`". Together with the initial-review bullet, that is ITEM-15's statement.
- **D30-B against ITEM-17.** D30-B is ITEM-17.
- **The other unchanged lines add no scope.** These are the redline's pin or precondition, `INSTRUCTION_READY`, and the term definitions. They state how the bodies carry the two items.
- **The heading.** It quotes Nathan's DN-3 line, which now matches what the rulings say.
- **What changed.** The diff changes only the delta bullet and the tested-guard description of G-W2-EM-2. PLAN §12 says the same.

**Disclosure.**
- The correction is disclosed in §P *Disclosed deviations*, in PLAN §12 and in C-24.
- D30 has never been on `main`. D26's "corrected by a successor section, not by an edit in place" is scoped to a part of D26 that Nathan corrects, so it does not govern this. L-D8 notes that D30 itself carries no mark of the correction.

### R-B1 (R1): **fixed**

- **The text form.** X17's step names `normalize_fetch.normalize(read)` as the one text form. The reviewers run `x12_qualify_102726.py run` and `registry_assemble_102726.py assertions --registry … --audit-root … --successor-map … --landed --fetched-after …` on their own reads.
- **The flags exist.** Both tools accept these flags.
- **The tools enforce the form.**
  - `x12_qualify_102726.py` refuses a payload that is not normalized (`payload_normalized`).
  - `registry_assemble_102726.py assertions` reports `text_form` "normalize_fetch.normalize (C-15)", which is the value X17's verification requires.
- **Raw runs are void.** The verification voids a review that reports a run on raw fetches.

### R-B2 (R2): **fixed**

- **The rebuilt link.**
  - `make_activation_ops_102726.py` rebuilds C-REG with `[pull request #@CONTROLS_PR](…/pull/@CONTROLS_PR)`.
  - It refuses a C-REG that lacks W8's #768 link, or carries it twice.
  - The file equals the rebuild, C-REG carries the marker twice and does not contain `#768`.
- **Unfilled refused.** `activation_render_102726.py` refuses an unfilled `@CONTROLS_PR` (`UNFILLED_MARKER`), as self-test case `c26_*` shows.
- **The number.** X1 records it once, in `execute/controls-pr-102726.1.json`. X9 fills it with `--set`, which both `plan` and `check` accept.
- **Two markers for one pull request.** L-D2 covers this.

## New REQUIRED findings

None. Each candidate the brief named, as tested:

- **The X8 refusal when a before-count differs from W6's on a volatile page.**
  - **It can fail.** Self-test `part17_before_counts_differ_from_w6` shows it.
  - **It does not fail on today's real reads.** The Hub has not moved since 03:02:37Z. P-L8's "subtree revision moves without page edits" changes no text, so no count changes either.
  - **When it fails on a correct result.** This needs a foreign edit that changes a guarded line between W6's read and X8. It then stops before any write, loudly, with a return to Nathan, which D26-A rule 3 lists rather than requires. See L-D1.
- **The edit applier.** It cannot write a wrong span silently on these inputs (see R-1). It writes the real tree only at X1 and X26, as designed. The dry run and self-test write only scratch copies.
- **D30's in-place correction.** It is exact and disclosed (see R-2).
- **`@CONTROLS_PR` and `@PROCEDURE_PR`.**
  - **On the normal path they hold one value.** `@PROCEDURE_PR` is "the pull request that landed v5.1.0 on main", and under C-12 that is the controls pull request.
  - **They can diverge only if the controls pull request is replaced.** X1's "never rewritten" rule has no path for that.
  - **Consequence:** a wrong provenance link on the register, low. See L-D2.

## LISTED findings

| ID | Finding | Path | Likelihood | Consequence | In repair text |
|---|---|---|---|---|---|
| L-D1 | X8 `plan --phase part17` (and X0(f)'s N10) refuses a page whose guard count before the edit differs from W6's measurement. It does so even when a foreign edit has already removed a retired line inside an operation's span, a case where the result would be correct | failure (concurrent edit) | low | a loud stop before any write, then a return to Nathan; this is P-L8's accepted case reached earlier | yes (C-23) |
| L-D2 | `@CONTROLS_PR` (from `execute/controls-pr-102726.1.json`, X1) and `@PROCEDURE_PR` (the pull request detected at X18, P2) name the same pull request, but they are filled from different sources and nothing checks that they are equal. Smallest fix: fill both from the X1 file, and have X18 assert that the merge it detects is that pull request | failure (a replacement controls pull request) | low | the candidate record and the procedure binding on the register cite different pull requests | yes (C-26) |
| L-D3 | C-24 says "L-C1 stays an accepted risk, and the return offers it to Nathan as an opt-in". §P *Product Owner actions* and PLAN §9 ask only whether R-P1 and R-P2 are opted in | normal | certain | Nathan is not prompted about L-C1. Template rule 8 still lets him opt in to any listed finding | yes (C-24) |
| L-D4 | The repair rewrote the PLAN's introduction to "at most two FULL reviews, then one diff check", which resolves round 1's L-8 wording. The ledger and C-23 to C-26 say only the four required findings were repaired, and nothing discloses this change. §13's estimate, the consequence of L-8, is unchanged | normal | certain | none in behaviour; the "four only" statement is inexact | yes |
| L-D5 | `repo_edits_102726.py check --set X26 --state before` reports `ok` with unfilled markers when no `--values` is given. Its append rows are always ok, and it skips the in-memory render. PLAN X26 always passes `--values`, and `apply` refuses unfilled markers | normal, if misinvoked | low | a before-check that claims "no marker unfilled" without testing it. No write follows | yes (C-23) |
| L-D6 | X26's after-check defaults `--before-ref` to `origin/main`. On a stale `origin/main`, the prefix test fails falsely, because the branch inserts the D23 successor mid-file (at line 1561) and D30. X18 detects the controls merge on `main` first | failure | low | a loud false stop at X26 | yes (C-23) |
| L-D7 | The action text in `typesafe-execute.md` says "land four repository control files". PLAN's summary says "five repository controls", and X1 writes 5 files | normal | certain | the input to the TypeSafe reading is worded slightly low; the reading is otherwise unaffected | yes (not the repair) |
| L-D8 | D30 itself carries no mark that its delta bullet was corrected. The disclosure sits only in §P, PLAN §12 and C-24 | normal | certain | after the merge, a reader of the decision record alone sees no trace of the correction. The branch history keeps it | yes (C-24) |

## Contradictions with unchanged text (question 3)

- **§P's step table and PLAN §5 agree** at X1, X8, X9, X17 and X26 (commands, counts and markers).
- **§10's accepted risks are consistent with the repair.** P-L8 (the Hub's volatility) is the case that L-D1 reaches earlier. P-L4 is consistent with C-25.
- **The ledger entry matches the round-1 records:** A had 2 required and 15 listed, B had 2 required and 10 listed, and the distinct count is 4. Its "repairs the four only" is inexact by L-D4.
- **Only contradiction found:** L-D3 (C-24 against §P and PLAN §9).
- **The record validator passes on the commit:** `modification_validate.py`, 1 of 1.
- **Receipt attribution.** The `review1_repair` receipt names its tested state honestly: head `f1680af` with the repair uncommitted, run at 10:53:14Z. Commit `885638d` (10:54:37Z) holds the same tools, and my reruns on `885638d` reproduce every count it records.

## Trend

- Round 1: 4 distinct confirmed required defects.
- This diff check: 0.
- None of this round's findings is required. The LISTED ones sit mostly in the repair's own text, which rule 5 counts only for required defects.

## Notion pages read (D22)

- Glow Operations Hub `3ce4590a05eb814f8892f88ff8539308`, as of 2026-10-27T03:02:37.191Z.
- GCFPE Membership and Release Register `3d24590a05eb81ce942ad994cfca9fa1`, as of 2026-10-12T17:17:45.991Z.

Both were read with `notion-fetch`, read-only. Both results were too large to return inline, so the harness saved them in its own tool-results folder. The plan's tools read them there, in memory only, for guard counts. I copied no body text, and wrote none here.

## Canon relied on

- **`AGENTS.md`:** the canon-first rule; *Code review guidelines* (real inputs); *Evidence attribution, currentness and distinct decisions*.
- **PF10-HDE-Build-Notes v13.9, as on `origin/main` `91925e9`.**
  - I read no older PF10 base.
  - The local `main` ref in this clone is stale. It points to `9dda63d`, which carries PF10 v13.8.8. I did not read it. The plan's tools use `origin/main`.
- **PF06-Canon-Change-Process-Guide v2.5.5:** §0.1A, its agent-authored addendum paragraph ("Resolve the current continuous addendum number and format before authoring"). G-W6-HUB-RN and G-W6-REG-RN require exactly this.
- **Repository controls:**
  - `modification-template.md`: rules 1, 4 and 8, and §P;
  - `gcfpe.decision-record.md`: D26 (preamble and D26-A rules 1 to 6) and D30 in full;
  - the record's §A.13 (L-C1), §A.14 (DN-3; "All other listed findings are accepted as risks"), §P, and the ITEM-14, ITEM-15 and ITEM-17 statements;
  - `plan/coordinator-decisions.md`: C-15, C-22, and C-23 to C-26.

DECISION NEEDED
