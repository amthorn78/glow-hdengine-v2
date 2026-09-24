0 distinct confirmed REQUIRED findings

# Stage 5 diff check: PE37-DC

Reviewer: PE37-DC, a fresh-context subagent working only from the fenced brief in
`docs/ephemeral/pe37.stage5/REVIEW-BRIEF-diffcheck.md` (@ b3c5a45). Under review: `git diff 061e4b1 8b292c3`,
less reviewer PE37-R1-B's record, which that range also adds. The four files under review are the same at
b3c5a45 as at 8b292c3. I made no Notion read or write.

**Answer.** The repair does what it claims. C1 and C2 hold, C3 holds, and C4 holds with two small wording
points. Withdrawing `PART-11-TRACK-01` breaks nothing on the parked plan's normal path. No gate, count or tool
depends on that edit being present (A1). The new item 6 is cross-referenced correctly by the step table. Its
own "step 7 return" uses the table's word for an item number, but the meaning is clear (A2). `REVIEWS.md`
reports both records faithfully, apart from two points (A3). I found no required defect.

The most substantive LISTED point is L1. The withdrawal departs from §A Decision 11, which Nathan approved,
and item 6 does not route that departure the way it routes the seven upstream findings. I refuted it as
REQUIRED because it is not silent. The withdrawal is stated by id, with its reason, in the successor that the
diff check reviews and that Nathan reads before he approves. It is the cheapest thing to fold in if Nathan
opts in.

## What I reproduced (read-only; scratch `git archive 8b292c3` extract; PYTHONDONTWRITEBYTECODE=1)

- `modification_validate.py --selftest`: 64/64. The parked record validates 1/1.
- The validator diff changes a comment and nothing else (two `+` lines, one `-` line, all `#`).
- Every consumer of `plan/notion/edits.json`. The normal path reaches edits only by id: `ctrl.py edits` / `op`
  at X5.0, X5.3, X5.6, X7.5 and X7.7, and `ctrl.py all --expect unlanded` at X4.6. `apply_texts.py` and
  `run_proof_x.py` read `texts/edits.json`, not the Notion file. `ctrl_proof.py` is a PLAN proof, not a gate.

## REQUIRED

None.

## LISTED (one line each: path; likelihood; consequence; in text the last repair added?)

1. **The withdrawal departs from §A Decision 11 without a `DECISION NEEDED`.** §A Decision 11
   (`analyze_approved_by: Nathan`) says the contradictions "are recorded on the redesign tracking page at
   EXECUTE". Step 3 item 2 now withdraws that record, and item 6 routes seven upstream findings but not this
   one. The dated §P's *Explicitly not in scope* line also still says "recorded on the tracking page, step 19".
   - Path, likelihood and consequence: normal path; certain; an approved §A decision is dropped by plan
     approval, the channel that item 6 itself says does not cover upstream departures.
   - Why it is not REQUIRED: it is disclosed by id and reason in the successor, so it is not silent.
   - Smallest correction: add it to item 6 as an eighth entry, with the recommendation "withdraw; stage 5
     resolved them (`MGMT-10-REVISION.md`)".
   - Yes, in the last repair's text.
2. **The executable manifest still names the withdrawn edit.** Spec X5.6 ("append `PART-11-TRACK-01` … to
   `EX/ctrl/sent.txt` … Applies `PART-11-TRACK-01`, …"), `edits.json`, `ctrl_proof.py`'s `SUCCESS` and
   `anchor_check_plan.json` all still carry it. Only the successor's content list withdraws it, and "withdrawn,
   not rewritten" does not say whether X5.6's step text or `edits.json` changes. It is the same pattern as the
   sent list, which the successor withdraws in bulk.
   - Path, likelihood and consequence: normal path; low (the session that writes "less `PART-11-TRACK-01`"
     executes X5.6, and the diff check reads the successor); if it happens, RQ-1's false paragraph is written
     after all.
   - Yes, in the last repair's text.
3. **"The Notion edits" lost its count.** It was "the 19 Notion edits", and `edits.json` holds 24, 5 of them
   stop-only. The repair dropped the number instead of saying 18, so which edits are content now rests on the
   *machinery withdrawn* bullet. No tool checks a count. Normal path; low; ambiguity only. Yes, repair text.
4. **Item 6 says "in the step 7 return"; it means item 7.** In this file, "step 7" is the table's *Start PR05*.
   The done-when column's own form is "step 3, item 6". Normal path; low (item 7 is "Return the plan"); a
   misreading would be loud. Yes, repair text.
5. **Items 6 and 7 conflict literally.** Item 7 lists "every open finding … as an accepted risk", and item 6
   says the seven "are not listed as accepted risks". The specific rule wins on an ordinary reading. Normal
   path; low; loud if misread (the seven would still reach Nathan). Item 6 is repair text; item 7 is only
   renumbered.
6. **Step 4's done-when does not require the seven dispositions.** It requires only `plan_approved_by`.
   Item 6's "the plan is not approved past them" binds the session but not the gate. Normal path; low (Nathan
   sees the `DECISION NEEDED`); an approval without answers is ambiguous but visible. Adjacent to repair text;
   step 4 is unchanged.
7. **"Each goes … as one `DECISION NEEDED`" reads either way.** It could mean one block of seven or seven
   decisions. The table ("a `DECISION NEEDED` for the seven") suggests one block. Cosmetic. Yes, repair text.
8. **The validator comment points to the wrong place.** It says "review rounds are bounded by D26, below", but
   `_d26_checks` (line 316) and its call (lines 368–372) are above line 464. Cosmetic. Yes, repair text.
9. **The execution-and-delegation paraphrase drops a qualifier.** It shortens DISP-001's "listed as an
   accepted risk, with its reason, in an approval request Nathan approves" and drops "with its reason". It
   names DISP-001 as the definition, so the governing text still governs. Cosmetic. Yes, repair text.
10. **`REVIEWS.md` says LISTED findings are "None … repaired"** (D26-A rule 4). The D26-E old-text fixes close
    A L4 and B LISTED 1–2. They are justified as D26-E obligations, and the ledger says so in its own section,
    but the sentence is literally inaccurate. Cosmetic. Yes, repair text.
11. **`REVIEWS.md` adds a reading that neither record gives.** Of "the first external write" it says "Read it as
    the first Notion write". That answers only one of B's two questions (not per part versus per
    Modification), and a ledger note does not bind the MGMT-10 page. Failure path; low; recorded, not silent.
    Yes, repair text.
12. **A known certain dry-run failure is left in place.** `REVIEWS.md` correctly says the TRACK-STATUS-01..03
    anchors (A L1) will fail X4.6's `ctrl.py all --expect unlanded` loudly, which returns the plan to Nathan
    once through D26-F trigger 2. That is a certain extra round trip that could be priced now. Normal path;
    certain; loud. Not in repair text (the LISTED is A's).

## The attack list, answered

- **A1: no silent break.** `TRACK-FREEZE-START`, `TRACK-FREEZE-LIFT` and the stop lines insert before the same
  anchor, `**The three decisions below are recorded as`. Each `new_str` re-ends with the anchor, so the anchor
  stays once whether or not `PART-11-TRACK-01` lands, and the lift still follows the start. X4.6's
  `--expect unlanded` tests each edit's own anchor, and PART-11's is present, so leaving the entry in
  `edits.json` is harmless. X5.6's readback covers only what was applied. No normal-path command checks a count
  of Notion edits. `ctrl_proof.py`'s success order and `ctrl_proof.out.json` still model the edit, but they are
  PLAN proofs, and re-running them would prove a superset in memory without writing anything. The residual is
  L2 (the manifest's step text), not a gate.
- **A2: the cross-references resolve correctly.** The table's "(step 3, item 6)" points at the new item 6. The
  kickoff's "step 3; follow it in order" is unaffected. "Step 6 return" appears only in R-B1's proposed
  correction, not in the committed text. The one slip is item 6's own "step 7 return" (L4).
- **A3: faithful, with two small points.** The counts check out: A has 13 LISTED and B has 16, 29 in all; RQ-1
  is R2, and R-B1 is R3 (and R1). The quotations are accurate. The "as the task brief specified" attribution is
  supported (`TASK-01` line 137: "PLAN's first FULL review comes after a DRY_RUN"). The census-summary
  finding's "answered by stage 5" is supported by `MGMT-10-REVISION.md`, *The census's A1–A5 on this page*.
  The two points are L10 and L11.

## Prior REQUIRED findings

- **RQ-1 (PE37-R1-A, R2): fixed.** Step 3 item 2 withdraws `PART-11-TRACK-01` by id, with its reason. What
  remains is LISTED 2 and 3.
- **R-B1 (PE37-R1-B, R3/R1): fixed.** Item 6 names all seven findings, which match §P *Findings on upstream
  sections* and spec §10.1 less its two non-§A rows. It routes them as a `DECISION NEEDED` with the §A text,
  the handling and a recommendation, and step 3's done-when requires it. It came with new LISTED points 1 and
  4–7, none of them required.

**Trend:** distinct confirmed REQUIRED went from 2 (round 1) to 0 (this diff check), which more than halves.
Most of this check's LISTED findings (10 of 12) sit in text the last repair added. For a check scoped to the
repair's diff, that is expected, and none is required. The cap in brief §5 is now reached: two full reviews at
most, and the one diff check. The output goes to Nathan with the LISTED findings above. None is repaired
unless he opts in, and L1 is the cheapest to take.

DECISION NEEDED: Nathan decides whether to accept the 12 LISTED findings as risks or opt in to repairing any.
L1 (routing the §A Decision 11 departure through item 6) is the one I would take.
