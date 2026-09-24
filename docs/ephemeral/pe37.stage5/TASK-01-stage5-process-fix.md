---
artifact_type: PE_TASK_BRIEF
artifact_version: "1.0"
created_date: 2026-09-24
session: PE37 — brief written by PE36 at hand-off
status: AUTHORIZED
authority: Product Owner instruction, 2026-09-24, quoted verbatim below
baseline: main @ 4c57d92 (PR #479 merged)
---

# PE37 Task 01 — the stage 5 process fix, and the stopped Modification resumed in step with it

## The instruction

Nathan, 2026-09-24, after reading the recovery analysis:

> "the main thing is that this needs to be A PROCESS. this ad-hoc deciding and choosing is going to
> lead me to more weeks of bullshit. I need to know how to resume the process with it working
> correctly, and to fix the process parts that were broken. Not just random out of sync decisions"
>
> "So I need a process fix, prompt fixes, design fixes, and prompt to hand back to the alpha run
> system that will fix this IN STEP with the process."

**What each phrase means here:**
- **"The alpha run system"** is the `GCFPE-MGMT-10` maintenance session that ran the Alpha Feedback
  Modification and the stopped follow-up.
- **"In step"** means the follow-up's cleanup resumes through the fixed process, in its own modes and
  gates. It is not landed by hand.

**Do not answer with a menu of choices.** PE36 did that first and was corrected. A decision belongs to
Nathan only where the process names his gate: approving a mode's output, merging, installing, or a
rule change he has not yet made.

## Definition of done

1. **The process fix is a recorded ruling,** `D26`, with a tested guard (`D14`, `GUARD-001`). The
   documents that carry the process agree with it: the template, the validator, the review brief,
   DISP-001 and the session working rules.
2. **The MGMT-10 prompt runs the fixed process.** That is the proposed body in Notion. Its spine, modes
   and result routing carry D26. Each recorded design contradiction in it is resolved, or deferred by
   name with a reason. It satisfies ITEM-23 and ITEM-40's gates (§6).
3. **A resume procedure** names every step from here to PR05, and who does each.
4. **The follow-up is resumed in step.** When the stage 5 pull request is merged, a new
   `GCFPE-MGMT-10` session is created to resume `MODIFICATION-20260923-closeout-residuals` at
   `MODE = PLAN` under D26, and Nathan gets its link. Nathan's instruction of 2026-09-24 was *"by
   handoff I mean create a new session"*. That session is maintenance, so C-TOP's ban on
   session-creating sessions does not bind it (D23 clarification).
5. **One pull request** holds every repository change. Every Notion edit is read back. The redesign
   tracking page shows stage 5.
6. **Nothing live changes in this task:** no live prompt body, skill, registry row or graph part. The
   MGMT-10 proposed body and the triage prompt are not live.

## What is broken, and where it is recorded

Start from these. Do not re-audit.

| Source | What it gives you |
|---|---|
| `docs/ephemeral/pe36.mgmt-redesign/RECOVERY-ANALYSIS-20260924.md` §4.4, §6, §7 | the rules that drove the loop, each with its smallest patch; the escalation triggers; the stopping rule |
| `docs/ephemeral/pe36.mgmt-redesign/recovery-20260924/read_process.json` | the same rules with evidence and authorship; every review loop of 09-23/24 |
| `docs/ephemeral/modifications/evidence/closeout-residuals/RCA-20260924-closeout-residuals.md` §4 and §7 | root causes RC1–RC9, and corrective actions 1–11 |
| `…/closeout-residuals/ANALYZE-anchor-census.md`, *The proposed MGMT-10 body* | 12 design contradictions in the MGMT-10 prompt |
| `MODIFICATION-20260923-closeout-residuals.md` §A decision 11 | sends those design contradictions to stage 5, which is this task |

## The fix, as far as it is settled

The recovery analysis settled the substance. PE37 writes it. Open points are marked **open**.

### 1. `D26`, the ruling, in `gcfpe.decision-record.md`

- **Reviews are bounded.** This is the recovery analysis §7, rules 1–6:
  - a dry run first;
  - at most two full reviews and one check of the repair's diff;
  - a required-finding rubric;
  - non-blocking findings listed as accepted risks;
  - early stops when defects do not halve, when most sit in text a repair added, or at twice the
    estimate;
  - an exit rule is never tightened, and every stopping rule is labelled with who set it.

  It applies to ANALYZE and PLAN reviews, and to D24 skill reviews: after two consecutive
  SKILL_REPAIR_REQUIRED rounds, Nathan decides before a third.
- **Failure paths.** A plan automates its normal path only. A failure after the first external write
  ends the same way every time:
  1. commit a failure record that reaches `main`, in a record PR;
  2. sweep read-only;
  3. keep the freeze;
  4. return to Nathan.

  Where a rollback would need a copy of a Notion body that D22 forbids, the rollback is Nathan's
  restoration from Notion page history. The record stays EXECUTING until he has restored the bodies,
  and nothing further is automated.
- **Resume only at checkpoints.**
  - At mode boundaries.
  - Before the first external write, by restarting.
  - At each post-merge step, started from `main`, with the merge detected by files on `main` and
    never by commit subjects, because this repository squash-merges.
  - Within one session: values recorded once, apply-once tests, and operations safe to send twice.
- **Cost on the record.** ANALYZE states a time and token estimate for PLAN and EXECUTE.
  `interaction_cost` counts ANALYZE and PLAN review rounds.
- **Verifying a rule change searches for surviving old text** by broad match minus exceptions
  (SCOPE-001). This is the Alpha run's completion-check failure.
- **Escalation to the multi-agent mode** is one bounded pass on a named trigger (recovery analysis
  §6).
- **What it supersedes.** Write these inside D26, and add no successor section under D24 (see
  *Anchors*):
  - D20's and template rule 3's claim that the scope freeze bounds the review loops;
  - D24 condition 5's uncapped re-review.

  A one-line pointer under D20 is fine.
- **Guard.** The validator's format 2.1 checks (§3), proven by injected regressions. The session
  behaviours (budget, exit-rule provenance, faithful compaction summaries) have no mechanical guard,
  and D26 says so rather than implying one.
- **Transition (open; state it in D26):** a record begun before D26 adopts format 2.1 when it next
  changes mode. Rounds run before D26 are cited from its RCA, not entered in the ledger.

### 2. Template v2.1, `modification-template.md`

| Where | Change |
|---|---|
| Rule 1 | "…records a finding and returns **to the Product Owner with a DECISION NEEDED**" |
| Rule 3 | "It bounds scope, not review rounds; rule 8 bounds those" |
| Rule 4 | A rule change's verification includes the old-text search |
| Rule 5 | A stop is a disposition; the steps after it are `NOT_RUN`, citing the stop |
| Rule 6 | The D22 carve-out above |
| New rule 8 | Review bounds, citing D26 |
| §P standard | "…executed mechanically with no interpretation **on its normal path**. A failure path ends with a record, a stop and a return to Nathan" |
| Frontmatter | `format: "2.1"`, `estimate`, a `reviews` ledger |
| §P | a place for open findings accepted as risks |

`interaction_cost` counts review rounds.

### 3. Validator, `modification_validate.py`

- **When `format` ≥ 2.1:**
  - `reviews` is a list of `{mode: ANALYZE|PLAN|SKILL, kind: DRY_RUN|FULL|DIFF_CHECK, date, required_open, outcome}`;
  - per mode, at most 2 FULL and 1 DIFF_CHECK, unless the override names `review_cap`;
  - PLAN's first FULL review comes after a DRY_RUN, unless the override names `dry_run`;
  - `estimate` is required at ANALYZED and later, except in terminal states.

  `OVERRIDABLE` gains `review_cap` and `dry_run`.
- **Legacy records (no `format`) validate exactly as today.** All four records under
  `docs/ephemeral/modifications/` must still pass.
- **Selftest:**
  - a must-fail and a must-pass case for each check;
  - the template validating as shipped (INTAKE) and as filled (ANALYZING);
  - proof that the guard fires, from a scratch copy with the check disabled (GUARD-001).

  Today's baseline is 39/39.

### 4. The review brief, `reviewer-prompt-template.md`

Add a second template, for ANALYZE and PLAN reviews:
- **Required findings:** a normal-path defect; a silent wrong edit to a body, governed document or
  control page; a silent breach of a ruling; a plausible path with a silent or destructive outcome. A
  loud stop that returns to Nathan is listed, not required.
- **Verifiers** refute by default.
- **No "try hard".** The attack list goes weakest first.
- **Count and trend:** count distinct confirmed required defects, and report the trend.
- **The cap and the exit** are stated in the brief.
- **Committed before spawning:** the filled brief goes under `docs/ephemeral/` before the reviewer is
  spawned, as D24 condition 2 requires for skill reviews.

### 5. DISP-001 and the session working rules

- **`ecosystem-change-management.md`, DISP-001:** a finding is resolved when it is fixed, declined with
  reasoning, or listed as an accepted risk in an approval request Nathan approves. This applies when a
  change closes, not at each review round.
- **`session-working-rules.md`:** a short *Loops* section citing D26:
  - a status update inside a loop carries the trend and an option to stop;
  - a changed commitment is headlined as a correction;
  - a compaction summary quotes the commitment and Nathan's reply word for word;
  - re-price at twice the estimate.

  `glow-po-reporting` needs the same lines but is a skill, so it waits for the next package cycle.
  Record that as carried.

### 6. The MGMT-10 proposed body, Notion `3e34590a05eb811b93d2da9b4ef8106d`

PE36 wrote this prompt. It is approved for testing and is not live.

- **Spine.**
  - Replace "This is what bounds review loops, and it is independent of how much a Modification
    contains." with the corrected statement.
  - Add a short *Reviews are bounded* block carrying D26's behaviour. The prompt carries behaviour
    and cites D26 for the rest.
  - *One session*: resume only at checkpoints.
- **ANALYZE:** the estimate, and review rounds in the cost.
- **PLAN:**
  - the normal path is mechanical;
  - the failure-path ending;
  - a dry run first;
  - the cap;
  - the plan is presented with every open finding listed;
  - a plan stopped before approval resumes as a §P successor, never as a rewrite of the dated plan.
- **EXECUTE:** the D22 carve-out and the failure procedure.
- **Result routing:** a result for a mode returned pending approval. This is census contradiction 5.
- **The census's 12 contradictions:** resolve each, or defer it by name with a reason. Examples:
  - "Must not: change anything" becomes "outside its own section of the record";
  - who writes the approval fields: the session, on Nathan's recorded approval;
  - the artifact-location sentence covers all three writable paths;
  - raw-request ANALYZE creates the record and its branch;
  - post-install verification closes EXECUTE after Nathan installs;
  - the page's status block is page state, not body.
- **ITEM-23 and ITEM-40, in step with the follow-up.** The follow-up's PART-11 planned exactly these
  edits to this page, as rules `R-ITEM23` and `LGCFPE-MGMT-10-PROPOSED-1` in
  `…/closeout-residuals/plan/engine/`:
  - delete the two release label lines (`Prompt version:`, `Ecosystem release:`);
  - adjust the preamble so it no longer promises them.

  Apply those here, then confirm that `R-ITEM23-gate` and `R-ITEM40` read 0 on the page. The resumed
  plan then **verifies** PART-11 and does not edit it. Its `R-ITEM23` expects 2 matches, and there will
  be 0, so the resumed plan must say so.
- **Read the page back.** A transient read is allowed under D22; disclose it.

### 7. The resume procedure, and the session that carries it out

Write `docs/ephemeral/pe37.stage5/RESUME-PROCEDURE.md`, one line per step with its owner:

1. **Nathan** merges the stage 5 PR. Merging preserves the record; D26 is recorded from his
   instruction, and he corrects any part of it.
2. **PE37** creates the MGMT-10 session: proposed body, `MODE = PLAN`,
   `MODIFICATION-20260923-closeout-residuals`, with the resume procedure as its input.
3. **The MGMT-10 session** resumes the plan:
   - brings the record to format 2.1;
   - writes a §P successor: the content as it stands, the machinery withdrawn (recovery analysis
     §4.3), R8-02 fixed, the failure record in a record PR, PART-11 verified;
   - re-derives the text results on the new base (see *Anchors*);
   - runs one dry run of the normal path on fresh fetches, and one in-order run of the manifest;
   - runs at most one check of its diff;
   - returns the plan with its open findings listed and its estimate.
4. **Nathan** approves the plan (`plan_approved_by`). This is the process's gate.
5. **The same session executes it,** the way E6 did:
   - one D24 review round of the 7 packages; a rejection returns to Nathan;
   - Nathan installs;
   - the bodies land under the existing freeze;
   - the merges;
   - post-install verification from `main`.

   Any failure takes D26's failure path.
6. **Nathan** lifts the freeze: the Alpha run's E6 freeze and the follow-up's. It is recorded in both
   Modifications' §E.
7. **PR05** starts. It is product work and the first real run of the post-D23 ecosystem, with the
   recovery analysis's watch points.
8. **Stage 5 closes** once the follow-up has run cleanly under D26. Then a decision-record entry
   declares the model standing, and promotion (stages 2–3) opens.

## Anchors: stay in step with the parked plan's texts

The follow-up's texts (`…/closeout-residuals/plan/texts/edits.json`) insert at exact anchors, each of
which must occur exactly once. Keep them intact and unique:

| File | Anchor |
|---|---|
| `gcfpe.decision-record.md` | "this entry says so rather than implying a guard exists." (D24's last line; the drafted D25 goes after it) |
| `gcfpe.decision-record.md` | the `## D24 —`, `## D23 —`, `## D19 —` and `## D15 —` headings |
| `session-working-rules.md` | "- **IN FLIGHT** — something is running; the Product Owner waits" |
| `notion-write-boundary.md`, `prompt-body-content-policy.md` | the anchored lines listed in `edits.json` |

**Append D26 after D24's last line.** D25 then lands between them when the follow-up applies its
texts. **Put nothing else after that line.** A successor section under D24 would split D24 from the
drafted D25.

Stage 5 changes files the follow-up also changes, so the follow-up's recorded result hashes
(`texts/apply_texts_proof.json`) stop holding. That is expected: the resumed plan re-derives them
(procedure step 3).

## Bounds on this task

D26 applies to its own authoring:
- **Dry run first:** the validator selftest, the template cases, and all four Modification records.
- **Then at most two full reviews** of the package, by fresh reviewer subagents under the new review
  brief, committed before they are spawned.
- **Then at most one check of the diff.** Then report to Nathan with the open findings listed.
- **Estimate:** about half a day. Report against it.

## Where to write

| What | Where |
|---|---|
| The ruling, template, validator, review brief, DISP-001 and working rules | `docs/prompt_ecosystem_management/` |
| The brief's outputs, reviews and the resume procedure | `docs/ephemeral/pe37.stage5/` |
| The MGMT-10 proposed body | Notion, in place |
| The stage 5 status | the redesign tracking page, `3e34590a05eb81e7927efe0541258916` |

Branch `docs/<yyyymmdd>-pe37-stage5`, one pull request, and Nathan merges.
