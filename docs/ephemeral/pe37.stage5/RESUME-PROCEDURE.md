---
artifact_type: PE_RESUME_PROCEDURE
created_date: 2026-09-24
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
authority: Product Owner instruction, 2026-09-24 — "I need to know how to resume the process with it working correctly"; task brief TASK-01 §7
governs: MODIFICATION-20260923-closeout-residuals, from PLANNED (stopped 2026-09-24 08:28Z) to PR05
rule: D26
---

# Resume procedure: from here to PR05

**The process decides each step, and each step has one owner.** Nathan's gates are the ones the
process names: merging, approving a mode's output, installing, and lifting the freeze. Nothing else
waits on him, and nothing here asks him to choose between options.

| # | Step | Owner | Done when |
|---|---|---|---|
| 1 | **Merge the stage 5 pull request.** Merging preserves the record (`D21-C`). `D26` is recorded from his instruction of 2026-09-24; a part he corrects is corrected by a successor section in the decision record | **Nathan** | D26 is on `main`, and `modification_validate.py --selftest` on `main` passes 64/64 |
| 2 | **Create the MGMT-10 session** with the kickoff below, and give Nathan its link | **PE37** | the session exists; its id and link are recorded in this file's *Record* section |
| 3 | **Resume the plan under D26** (detail below) and return it with its open findings listed | **the MGMT-10 session** | the record is `PLANNED` at format 2.1, with a §P successor, a `reviews` ledger holding one `DRY_RUN` and at most one `DIFF_CHECK`, and an `estimate`; the result is `PRODUCT_OWNER_ACTION_PENDING`, carrying a `DECISION NEEDED` for the seven upstream findings (step 3, item 6) |
| 4 | **Approve the plan.** The session records `plan_approved_by` from his words | **Nathan**, the process's gate | `plan_approved_by` is set, quoting him |
| 5 | **Execute it** the way E6 did (detail below) | **the same MGMT-10 session**; Nathan installs and merges | the record is `COMPLETE`, or stopped on D26-B's path and back with Nathan |
| 6 | **Lift the freeze:** the Alpha run's E6 freeze and the follow-up's, recorded in both Modifications' §E | **Nathan** | both §E sections record the lift, with its date and his words |
| 7 | **Start PR05.** Product work, and the first real run of the post-D23 ecosystem, with the recovery analysis §8's watch points | **Nathan**, then the Alpha sessions | PR05's kickoff exists |
| 8 | **Close stage 5** once the follow-up has run cleanly under D26: a decision-record entry declares the model standing, and promotion (stages 2–3) opens | **PE37** or its successor, on the record from steps 3–5 | the entry is on `main` and the tracking page shows stage 5 closed |

## Step 3 in detail — the MGMT-10 session resumes `PLAN`

1. **Bring the record to format 2.1** (`D26` transition): add `format: "2.1"`, set `estimate` for the
   work still to come, and start `reviews: []`. Set `status: PLANNING`. The eight PLAN rounds of
   2026-09-23/24 are cited from the RCA, not entered in the ledger.
2. **Write a successor section below the dated §P.** The dated plan is not rewritten. The successor
   names the minimal execution in the recovery analysis §4.3:
   - **the content as it stands:** the 51 body edits, the 7 skill diffs, the registry diff and its
     guards, the graph reindex, the 11 repository texts and the Notion edits, **less
     `PART-11-TRACK-01`**. That edit writes a dated paragraph to the redesign tracking page saying
     the proposed body's contradictions are not resolved and wait for stage 5. Stage 5 resolved
     them (`MGMT-10-REVISION.md`), so the paragraph would be false when written. It is withdrawn,
     not rewritten;
   - **the normal-path tools as they stand:** `land.py`, `run_gate.py`, `apply_texts.py`, `m2.py`
     and the first-round D24 brief, with **R8-02 fixed**: X6.4's two-dot
     `git diff --name-only origin/main HEAD` becomes a three-dot merge-base diff, and X7.6 uses the
     same form (`rca-20260924/round8-review-results.json`);
   - **the machinery withdrawn:** automated stop and reversal; the stop record, restoration check,
     lift and end routes; resuming in a new session at any step; leases, the sent list, post-merge
     routing, and the D24 re-roll variants. R8-01, R8-03 and R8-04 go with it;
   - **the failure path is D26-B's:** a failure record committed to `main` in a record pull request,
     a read-only sweep, the freeze kept, and a return to Nathan; restoring bodies is his, from
     Notion page history;
   - **checkpoints are D26-C's:** mode boundaries; before the first Notion write, by restarting;
     each post-merge step started from `main`, with the merge detected by files on `main`;
   - **PART-11 is verified, not applied.** Stage 5 already applied `R-ITEM23` and
     `LGCFPE-MGMT-10-PROPOSED-1` to the proposed MGMT-10 page
     (`docs/ephemeral/pe37.stage5/MGMT-10-REVISION.md`). The plan's `R-ITEM23` expects 2 matches
     there and will find 0; the successor says so, and PART-11's step becomes a check that
     `R-ITEM23-gate` and `R-ITEM40` read 0.
3. **Re-derive the text results on the new base.** Stage 5 changed `gcfpe.decision-record.md`,
   `session-working-rules.md` and `ecosystem-change-management.md`, so the result hashes in
   `…/plan/texts/apply_texts_proof.json` no longer hold. Re-run `apply_texts.py` on a scratch tree
   for each label and record the new hashes. Every anchor still occurs exactly once: PE37 checked
   all 11 on the stage 5 tree, and X2.2 and X3.5 applied cleanly there.
4. **Dry run once:** every normal-path gate and readback on fresh fetches, read-only, then one
   in-order run of the manifest. Enter it in `reviews` as `PLAN` / `DRY_RUN`.
5. **At most one check of the successor's diff**, with the *ANALYZE and PLAN review brief* from
   `reviewer-prompt-template.md`, committed before the reviewer is spawned. Enter it as `PLAN` /
   `DIFF_CHECK`. There are no full reviews: the eight rounds already reviewed the content, and the
   recovery analysis §4.3 found it stable since round 6.
6. **Put the seven findings on upstream sections to Nathan.** The dated §P records them under
   *Findings on upstream sections* (spec §10.1): the census's RS-40 A5 row; the census summary for
   the proposed MGMT-10 body; `validator_revision`'s absence from §A's Decision 1; the merge count;
   the freeze window; the Notion targets §A omitted; ITEM-13's oracle input. Under template rule 1
   (v2.1) each goes to Nathan in the step 7 return as one `DECISION NEEDED`, each with the §A text
   it contradicts, the plan's current handling and the session's recommendation. They are not
   listed as accepted risks, and the plan is not approved past them. The census-summary finding is
   answered by stage 5 (`MGMT-10-REVISION.md`); say so.
7. **Return the plan** as `PRODUCT_OWNER_ACTION_PENDING`, with every open finding listed as an
   accepted risk (including round 8's 27 non-blocking findings, and the downgraded
   lift-after-stop finding, which goes with the machinery), and the estimate against what has been
   spent. Validate with `modification_validate.py` before returning.

**If the dry run fails on the normal path**, that is D26-F's trigger 2: one bounded check of
executability, then back to Nathan. It is not a review round.

## Step 5 in detail — `EXECUTE`

1. **One D24 review round of the 7 skill packages**, by two fresh reviewer subagents under the skill
   review brief. `SKILL_REPAIR_REQUIRED` returns to Nathan. It is not re-rolled (`D26-A` rule 2).
2. **Nathan installs.** The session returns `PRODUCT_OWNER_ACTION_PENDING` and waits.
3. **The bodies land under the existing freeze**, by the normal-path tools, with each write read
   back.
4. **The merges.** Each is Nathan's; the session detects each by files on `main`.
5. **Post-install verification from `main`:** the digest comparison, then `ECOSYSTEM_CHANGE_COMPLETE`.

**Any failure after the first external write takes D26-B's path:** the failure record in a record
pull request, a read-only sweep, the freeze kept, a return to Nathan. Nothing further is automated.

## The kickoff for step 2

PE37 creates the session with exactly this text, filling only `<STAGE5_PR>`:

```text
You are a GCFPE-MGMT-10 maintenance session. Run the prompt on this Notion page, as it stands when
you read it: 3e34590a05eb811b93d2da9b4ef8106d (GCFPE-MGMT-10 — Manage an Ecosystem Change —
PROPOSED BODY). It is approved for testing and is not live. Read it in full before anything else;
it is a read, not a copy (D22).

MODE = PLAN
Subject: MODIFICATION-20260923-closeout-residuals

This resumes a plan that was stopped before approval on 2026-09-24. It resumes under D26, which
was recorded by stage 5 of the MGMT redesign (<STAGE5_PR>, merged). Your input is
docs/ephemeral/pe37.stage5/RESUME-PROCEDURE.md, step 3; follow it in order. Read first:
docs/prompt_ecosystem_management/gcfpe.decision-record.md D20–D26,
docs/ephemeral/pe36.mgmt-redesign/RECOVERY-ANALYSIS-20260924.md §4.3, and the RCA at
docs/ephemeral/modifications/evidence/closeout-residuals/RCA-20260924-closeout-residuals.md §8.

You are a maintenance session: C-TOP's ban on session-creating sessions does not bind you, but you
create none. Nathan alone merges and installs. Return the plan with its open findings listed, and
stop there: EXECUTE starts only after Nathan's approval is recorded in plan_approved_by.
```

## Record

| | |
|---|---|
| Stage 5 pull request | #481, opened 2026-09-24 from `docs/20260924-pe37-stage5`; not merged |
| MGMT-10 session | *filled at step 2* |
