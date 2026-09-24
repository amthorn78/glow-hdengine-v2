---
artifact_type: PROMPT_ENGINEER_SESSION_SUCCESSION_RECORD
artifact_version: "1.0"
created_date: 2026-09-24
status: BINDING
predecessor: PE36
successor: PE37
authority: Product Owner instruction, 2026-09-24 — "hand this work off to a new PE session, you are PE36, it will be PE37"; "by handoff I mean create a new session"
baseline: main @ 4c57d92 (PR #479, merged) at authorship
role_change: false
---

# PE36 → PE37 succession record

| | |
|---|---|
| Predecessor | **PE36**, `session_01Aniz3abekzoEbAax1UbWar`. **Retired 2026-09-24** |
| Successor | **PE37**, `session_018teDumz2XyKdoXF9p3BKFM`. Created 2026-09-24 at 10:52Z by PE36 at Nathan's instruction, in the same environment, with PE36 as its parent |
| Charter | **General prompt engineering and maintenance, with one authorized task:** the stage 5 process fix |
| Baseline | `main @ 4c57d92` |
| Installed skills | flowmaster-validate 31 `a79401de…`, change-flow 22 `ee546df5…`, glow-hde-pr-development 4 `68077fa6…`, session-relay-flowmaster 5 `15aef989…`, amthor-workspace-governance-audit 15 `819915e4…`, tw-flowmaster 2 `fd6c344b…`, glow-graph-contract 6 `4e671ddc…`. E6 step 2, re-measured 2026-09-24 |

PE36's transcript is not a system of record, and PE37 does not have it, by design.

**Read this first, with `authoritative-surfaces.md` and `gcfpe.decision-record.md` (D1–D24).** Then
read the recovery analysis, `docs/ephemeral/pe36.mgmt-redesign/RECOVERY-ANALYSIS-20260924.md`.

## Your task, and the instruction behind it

**`docs/ephemeral/pe37.stage5/TASK-01-stage5-process-fix.md` is your first task.** It is authorized,
scoped, and has a definition of done. Start there.

Nathan's instruction, 2026-09-24:

> "the main thing is that this needs to be A PROCESS. this ad-hoc deciding and choosing is going to
> lead me to more weeks of bullshit. I need to know how to resume the process with it working
> correctly, and to fix the process parts that were broken. Not just random out of sync decisions"
>
> "So I need a process fix, prompt fixes, design fixes, and prompt to hand back to the alpha run
> system that will fix this IN STEP with the process."

**The most important line in this record:** the process decides what happens next. When you are
tempted to hand Nathan a list of options, find the gate in the process that owns the question.

## Where the work stands

| | |
|---|---|
| Live ecosystem | `GCFPE-20260914.1` / `091426.1` / 55. All six Alpha Feedback entries are live since 2026-09-23: 55 bodies edited in place at E6, six skills, graph, registry and the R1 successor. **About 50 bodies still carry old text beside the new rules.** That is the follow-up's scope |
| The follow-up | `MODIFICATION-20260923-closeout-residuals`: PLANNED, **not approved**. Its PLAN was stopped by Nathan on 2026-09-24 at 08:28Z after eight review rounds. Its content is stable and re-applies to `main` today. Its failure-handling machinery is to be withdrawn |
| The E6 change freeze | **Never lifted on the record** (E6 report, step 8 `pending`). No GCFPE lifecycle session runs until it lifts, and PR05 waits on it. It lifts at the follow-up's close (task, procedure step 6) |
| MGMT-10 | The live `091426.1` body has no modes. The **proposed body** (Notion `3e34590a05eb811b93d2da9b4ef8106d`) is APPROVED_FOR_TESTING and not promoted. It is yours to revise in stage 5 |
| Triage prompt | Notion `3e34590a05eb81bfbf1ed0651e6b6ddf`, proposed for testing. No recorded defect |
| Redesign stages | 0–4 done. **5, "fix what the pilot exposes", is your task.** 6 not started. Tracking page `3e34590a05eb81e7927efe0541258916` |
| Decision record | Ends at D24 with its successors. **D25 is drafted only in the parked plan's texts** (`P29-D25`) and lands with the follow-up. Your ruling is D26 |
| Alpha, HDE-EPIC040 | PR04 accepted by its PR-40 review (#469). **PR05 is product work and not yours**; it waits on the freeze |

## Open — carried, with owners

1. **The follow-up Modification** resumes through the process once stage 5 lands (task, §7). It is
   not yours to execute.
2. **The E6 freeze.** Nathan lifts it at the follow-up's close.
3. **Promotion of the MGMT-10 proposed body** (stages 2–3). After stage 5, and after the follow-up has
   run cleanly under it.
4. **`glow-po-reporting` needs D26's loop-reporting lines.** It is a skill, so this waits for the next
   package cycle.
5. **Seven known defects fall outside the follow-up's 40 items:**
   - the Modification Backlog's MB-001 to MB-004;
   - TW-01 (TW is out of scope);
   - ITEM-39b (none needed);
   - the MGMT-10 design notes, which are now in your task.

   See the recovery analysis §4.2.
6. **Candidate-era (09-15) full prompt-body text is committed under `docs/ephemeral/`,** in the
   post-flight evidence manifests. This is a corpus-policy question, and Nathan's call. It is noted,
   not acted on.
7. **Stray remote branches** that only Nathan can delete:
   - `docs/20260922-pe36-stage1-modification-format`
   - `docs/20260923-modification-intake-alpha-feedback-open-items` (its drafts are ABANDONED)
   - `docs/20260923-d22-transient-body-files` (#475 was closed; its content landed in #474)
   - `claude/hopeful-carson-ohz7u3` (#472 merged)

## Settled — do not reopen without new evidence

- **The redesign's rulings stand:**
  - `D20`: one prompt, three modes;
  - `D21`: one run is one Modification, in parts, and a merge preserves and never approves;
  - `D22`: a transient read of a body is a read, not a copy;
  - the `D23` rulings;
  - `D24`: skill reviews by reviewer subagents.

  Your stage 5 work **corrects** D20's scope-freeze claim and caps D24's re-review, inside D26. It does
  not reopen the rulings themselves.
- **The recovery analysis's findings:**
  - nothing live to roll back;
  - none of the 48 known defects is material;
  - the follow-up's content converged by round 5;
  - its machinery was review-induced regression and is withdrawn;
  - the follow-up lands (decision 2, revised).
- **C-TOP binds the main ecosystem only.** Maintenance sessions, PE sessions included, may create
  sessions when Nathan asks, and he asked on 2026-09-24.
- **Everything under *Settled* in `pe35-to-pe36.md` still holds.** Reading prompts is fine and copying
  them is not; a body carries behaviour, not governance state; `AUTH-001`; the graph is rebuilt by
  script; freeze digests are rooted at the skill directory.

## Completed by PE36

- **Task 01:** three skills brought into line with the Notion write boundary. `SKILL_FIT_CONFIRMED`,
  installed and digest-verified (`docs/ephemeral/pe36.task-01/`).
- **The GCFPE MGMT redesign:**
  - the audit, the RCA and `D20`, `D21`;
  - the Modification format, its template, `modification_validate.py` and `closure.py`;
  - the triage prompt, and two triage comparison tests;
  - the MGMT-10 proposed body.

  PRs #468, #470, #471, #473.
- **The recovery analysis, 2026-09-24:** #479. Its decision 2 was revised the same day.

## Process faults PE36 made — do not repeat

- **Claimed the scope freeze bounds the review loops.** It bounds the item list only. PE36's own audit
  named the real problem, review loops with no convergence rule, and the design answered it with the
  freeze. Eight PLAN rounds followed.
- **Skipped the small pilot.** The redesign said to pilot PLAN and EXECUTE on one small change. PE36's
  09-23 handoff sent six items into their first run, which edited all 55 live bodies.
- **Wrote rules without testing what they cost on the failure path.**
  - Rule 6, "a part lands whole or not at all", met D22's no-copy rule, and the result was rollback
    machinery.
  - §P's "executed mechanically with no interpretation", applied to failure paths, has no fixed point.
  - `interaction_cost` did not count review rounds.
- **Led a report with the wrong fact.** The recovery analysis opened "The eight rounds changed nothing
  live". That was accurate, but it read as "nothing was achieved". Lead with what the person's work
  achieved.
- **Judged by the measure easiest to compute.** Recommended parking the cleanup because nothing breaks,
  which is not whether Nathan's changes took effect. Corrected the same day.
- **Answered "this needs to be A PROCESS" with three ad-hoc decisions.**

The through-line: **a rule designed without its failure-path cost, and a judgement made on the
measure that was easiest to compute.**

## PE37's first actions, in order

1. **Confirm your session id** against this record's table. PE36 recorded it when it created you. If
   it is wrong, correct it in place: it is a current-state field.
2. **Confirm the baseline yourself:**
   - `main` is at or after `4c57d92`. This record is in PR #480; read it from that PR's branch until
     it merges, and branch your own work from `main` once it has;
   - `freeze.py` on each installed skill directory matches the table above;
   - the follow-up record reads PLANNED with an empty `plan_approved_by`;
   - `modification_validate.py --selftest` passes 39/39.
3. **Read the task brief,** then the recovery analysis §4.3, §4.4, §6 and §7, then the RCA §7, then
   the census's *The proposed MGMT-10 body*.
4. **Do the task in the brief's order.** It is bounded by its own rule: dry run first, at most two full
   reviews and one diff check, then to Nathan with open findings listed.
5. **Do not execute the follow-up yourself.** Your task ends when the MGMT-10 session that resumes it
   exists and Nathan has its link.

## How to work

- **Merging:** Nathan alone merges. Never merge, never enable auto-merge.
- **Skills:** they live in a one-way synced directory, so never write to it. Copy to scratch, run with
  `PYTHONDONTWRITEBYTECODE=1`, package, and hand the `.skill` files to Nathan; only he installs.
  Independent review is mandatory before any install.
- **Prompt bodies** are authored in Notion in place and never mirrored into the repository.
- **Writable paths:** `docs/pfcanon/` is read-only. Write only to `docs/ephemeral/`, `docs/graph/`,
  `docs/prompt_ecosystem_management/`, Notion where a destination rule allows it, and installed
  skills.
- **Reporting:** report the way `glow-po-reporting` requires. The answer first; a correction plainly,
  not buried; close with `DECISION NEEDED`, `NOTHING NEEDED` or `IN FLIGHT`. Record before reporting,
  and read the record back before claiming it.
