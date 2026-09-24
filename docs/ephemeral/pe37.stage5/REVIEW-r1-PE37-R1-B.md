1 distinct confirmed REQUIRED finding

# Review r1 — PE37-R1-B — stage 5 rule package (D26), full review 1 of 2

Reviewer: PE37-R1-B, a fresh-context subagent working only from the committed brief
`docs/ephemeral/pe37.stage5/REVIEW-BRIEF-r1.md` (@ 772d9f7). Under review: `git diff 4c57d92 dc023a5`,
read at dc023a5 and not at the branch head. The Notion page 3e34590a05eb811b93d2da9b4ef8106d was read once
through the connector, into context only. The read reported `page_last_edited_at` 2026-09-24T11:00:24Z.
No file, copy or hash of the page was made.

**Answer.** The package does what C1–C4 and C7 claim, and C5 holds on the page. C6 does not fully hold. The
resume procedure's step 3 is the resumed session's only input, and it does not route the seven upstream
findings that the parked plan's §P already records against §A. Template rule 1 v2.1, and the page's *The
record*, now say such findings go to Nathan with a `DECISION NEEDED` before the session carries on. So on its
normal path, the resumed session either stops on a step the procedure never mentions, or carries on past the
findings, which is the behaviour the rule 1 patch exists to stop. That is one required finding. Everything
else is LISTED.

## What I reproduced (read-only, on a `git archive dc023a5` scratch extract, PYTHONDONTWRITEBYTECODE=1)

- `modification_validate.py --selftest`: 64/64. The four Modification records: 4/4 (C2).
- `guard_proof.py`: every D26 check fires when it is disabled. The failing case counts are 17 (`_format`),
  8 (ledger shape), 3 (cap), 3 (dry run), 2 (estimate), 16 (`_d26_checks`) and 1 (`_waived`) (C3).
- All 11 `edits.json` anchors occur exactly once on the stage 5 tree. I ran `apply_texts.py` for **all four**
  labels, X2.2, X3.5, X5.2 and close, with stand-in `--run` and `--installed-freeze` values, the same way the
  earlier proof did. All four apply. The headings then run `## D23`, `## D24`, `## D25`, `## D26` in that
  order (C4, A6).
- The engine: `canon.py` loads 16 canonical texts. The `closeout_rules.py` self-test gives
  `checks_matching_authored_or_canonical: []`. The engine touches the proposed MGMT-10 page only through
  R-ITEM23 (delete, expects 2), the local edit LGCFPE-MGMT-10-PROPOSED-1, and the checks R-ITEM40 and
  R-ITEM23-gate. None of these can match the D26 text that was added to the page (A6).
- The page, by reading. No line starts with a `Prompt version`, `Ecosystem release` or `Set` label followed by
  a colon, so R-ITEM23-gate reads 0. No R-ITEM40 pattern occurs, so R-ITEM40 reads 0. Each of the census's 12
  contradictions is resolved on the page as `MGMT-10-REVISION.md` states (C5).

## REQUIRED

### R-B1 — the resume procedure omits the recorded upstream findings that rule 1 v2.1 sends to Nathan

- **Rubric class:** R3, a silent breach of a Product Owner ruling. It is also an R1 defect on the procedure's
  normal path.
- **Exact text or step.** Start with `RESUME-PROCEDURE.md` step 3 and *Step 3 in detail*, items 1–6. The
  kickoff tells the session: "Your input is … RESUME-PROCEDURE.md, step 3; follow it in order". No item
  mentions the §P subsection *Findings on upstream sections* of `MODIFICATION-20260923-closeout-residuals.md`,
  which is at line 909 at dc023a5. That subsection holds seven findings against §A: the census's RS-40 A5 row;
  the census summary for the proposed MGMT-10 body; `validator_revision`'s absence from Decision 1; the merge
  count; **the freeze window**; the Notion targets §A omitted; and ITEM-13's oracle input. Line 826 of the
  record adds an eighth reference, "an upstream finding against §A order 4". Step 3's done-when requires the
  result `PRODUCT_OWNER_ACTION_PENDING` and nothing else.
- **Evidence.**
  - Template rule 1 v2.1, added in this package, reads: "A mode that believes an upstream section is wrong
    records a finding and returns to the Product Owner with a `DECISION NEEDED` — it does not edit upstream,
    and it does not carry on past the finding." The page's *The record* says the same.
  - The recovery analysis §4.4 row "An upstream finding 'records a finding and returns'" names this exact
    record as the failure: "PLAN recorded 7 findings against §A and kept going". The RCA line 186 and
    `read_process.json` line 52 say the same.
  - The findings are undisposed. The record says only "Recorded in spec §10.1 and not edited here (template
    rule 1)". No Nathan disposition appears in the recovery analysis §8, the RCA or the task brief.
  - Step 3.6 asks only for "every open finding listed as an accepted risk", naming round 8's 27 and the
    lift-after-stop finding.
- **Path and likelihood:** the normal path. Likelihood is high, because the resumed session reads the record
  and the findings are in its §P.
- **Consequence:** there are two outcomes, and both are bad.
  - The session follows the procedure in order and returns the plan. The §A contradictions, including a
    changed freeze window, are either dropped or folded into "accepted risks". Nathan's plan approval then
    accepts a change to the approved §A without the `DECISION NEEDED` that rule 1 requires. That is silent,
    and it re-creates the RC behaviour the patch was written to stop.
  - Or the session honours rule 1 and stops, at a point the procedure never names. That costs an unplanned
    round trip, and step 3's "done when" cannot be met as written.
- **Smallest correction.** Add one item to *Step 3 in detail*, before the successor is written:
  > "The §P findings on upstream sections (seven, recorded against §A) go to Nathan as a `DECISION
  > NEEDED` in the step 6 return, each with a proposed disposition (§A successor, declined, or accepted); the
  > plan is not presented as approvable past them."

  Then add "and a `DECISION NEEDED` for the upstream findings" to step 3's done-when.
- **In text the last repair added:** no. This is the first review. The defect is an omission in
  `RESUME-PROCEDURE.md`, which is new in this package. It is not in the dc023a5 repair, `_waived`.

## LISTED (one line each: path; likelihood; consequence; in the last repair?)

1. **The validator still states the superseded claim.** `modification_validate.py` line 464 reads "scope
   freeze is the rule that bounds the review loops". No D26-E search for surviving old text was run on stage
   5's own rule change (`DRY-RUN.md` lists none). Normal path; low likelihood; a comment only; not in the last
   repair.
2. **`execution-and-delegation-model.md` lines 93–95 invite the reading D26 supersedes.** It says
   "'Non-blocking' is not a disposition … Drive every finding to resolution". This is DISP-001's "repair
   everything" wording, and the page's *Read these* cites the file. It reconciles with the new DISP-001
   definition of "resolved", so I did not count it as required. Normal path; low likelihood; a session could
   repair listed findings without Nathan's opt-in; not in the last repair. Correction: a one-line pointer to
   D26.
3. **"The first external write" is undefined.** D26-B, D26-C, template rule 6 and the page's `EXECUTE` do not
   say whether it counts across the Modification or per part, and do not say whether a pushed commit, an open
   pull request or a merge counts. Failure path; low likelihood; a session could block one part and carry on
   after another part has already written to Notion, or the reverse. The outcome is recorded, not silent.
   Not in the last repair.
4. **"Undo its repository steps" does not say how.** The page's `EXECUTE`, before the first external write,
   gives no method. Parts that are not ordered share one branch, so a file-level revert could undo another
   part's edits to a shared file such as `gcfpe.decision-record.md`. Failure path; low likelihood; a partly
   wrong branch, caught by that part's own verification; not in the last repair.
5. **The kickoff says the page "is approved for testing".** Nathan's 2026-09-22 approval predates the stage 5
   revision. `MGMT-10-REVISION.md` and the page's `revised_stage5` field say so, but the kickoff does not, and
   the resumed session will edit about 50 live bodies under the revised text. Normal path; the disclosure
   exists; the correction is one clause in the kickoff, or Nathan's approval of the revision recorded at step
   1. Not in the last repair.
6. **`RESUME-PROCEDURE.md` step 5.1 misattributes a stopping rule.** It reads "It is not re-rolled (`D26-A`
   rule 2)". D26-A rule 2 allows a second full skill review. The one-round limit was set by the task brief §7
   step 5 and recovery analysis decision 2, and D26-A rule 6 requires naming who set a stopping rule. Normal
   path; the outcome is a loud return to Nathan; not in the last repair.
7. **The validator's dry-run check covers `PLAN` only.** D26-A rule 1, and page rule 1, require a dry run
   before any `ANALYZE` or skill full review too. D26's guard list says "PLAN's first FULL review", but its
   list of unguarded behaviours does not name the gap. Normal path; low consequence; not in the last repair.
8. **The cap trusts the ledger to be complete.** A round that is never entered evades it silently, and D26's
   list of unguarded behaviours does not say so. Normal path; low likelihood; not in the last repair.
9. **The skill cap counts per Modification.** `SKILL` has a cap of 2 `FULL` rounds per Modification, across
   every package. D26-A counts per loop, "after two consecutive `SKILL_REPAIR_REQUIRED`". A Modification with
   two separately reviewed packages then needs an override. Loud (the validator fails); low likelihood; not in
   the last repair.
10. **Some `format` values silently skip the D26 checks.** A value below 2.1 or other than none, such as "2"
    or "2.0", is validated as legacy. The template defines legacy only as "no format". Low likelihood; the D26
    checks are silently skipped; not in the last repair.
11. **The half-applied check has no exit from `EXECUTING`.** Under the D26-B carve-out the record stays
    `EXECUTING`, where the check does not run. A later `BLOCKED` or `COMPLETE`, after Nathan restores the
    bodies, fails the check unless dispositions are rewritten, and no text says how. Loud (the validator
    fails); not in the last repair.
12. **Resume step 3.3 names only `apply_texts_proof.json` as invalidated.** `plan/registry/guard_tests.json`
    also pins `decision_record_sha256` 003a9f3f…, which stage 5 moves. Loud, if a gate compares it; not in
    the last repair.
13. **C1 understates what D26 supersedes.** C1 says D26 supersedes "only" three claims, but D26's own list
    has a third bullet, DISP-001's "repair everything" reading. That is within the task brief §5, so authority
    is not exceeded (A4). The claim wording is the only issue; not in the last repair.
14. **D26-A rule 5 drops the recovery analysis §7 qualifier.** It says "twice the estimate" where the analysis
    said "the estimate Nathan approved". `session-working-rules.md` keeps the qualifier. Cosmetic; not in the
    last repair.
15. **"Keep the freeze" assumes a freeze.** D26-B and the page say it with no rule for a Modification that
    has none. Failure path; low likelihood; not in the last repair.
16. **`interaction_cost`'s "review rounds" does not say whether `DRY_RUN` and `DIFF_CHECK` entries count.**
    Low consequence; not in the last repair.

## The attack list, answered

- **A1:** I found no path where a part fails after its own external write and the session carries on. The
  page sends that case to D26-B unambiguously. The open points are "first external write" and the method of
  undoing repository steps (LISTED 3 and 4).
- **A2:** Nothing live is inconsistent. The live registry row and graph part describe the live `091426.1`
  body, which is not run. The deferral to promotion holds. The kickoff's approval wording is LISTED 5.
- **A3:** Step 3 has zero full reviews, one dry run and at most one `DIFF_CHECK`. That is within D26-A rule 2's
  cap and matches decision 2 (revised): "one fresh rehearsal … No review loop". The defect in step 3 is R-B1,
  not the review count.
- **A4:** I found nothing that exceeds the recovery analysis §7 and the task brief §1. Minor wording
  differences are LISTED 13 and 14.
- **A5:** No legacy record fails. The ledger order, `_waived` and the `estimate` statuses behave as the
  docstring says. The gaps are LISTED 7–11.
- **A6:** Nothing breaks, and I ran all four labels, including X5.2 and close.

**Trend:** not applicable; this is review 1.

IN FLIGHT: R-B1 is for the author to repair in this round. Review 2, or the one check of the repair's diff,
follows under D26-A. Nothing is Nathan's yet.
