---
artifact_type: PROMPT_ECOSYSTEM_DECISION_RECORD
artifact_version: "1.1"
created_date: 2026-10-05
status: BINDING
authority: Product Owner rulings for the GTWPE, from 2026-10-05
applies_to: the GTWPE (Glow Technical Writing Prompt Ecosystem) — every prompt it maintains or builds, through every revision, consolidation and handoff
---

# GTWPE decision record

Product Owner rulings that govern the GTWPE, with what follows from each. They are kept here, not in
`docs/ephemeral/`, because they outlive any one change or release. Entries carry the `GTWPE-` prefix so
they are not confused with the GCFPE decision record's `D` numbers or the GTWPE design's `D-` numbers.

## GTWPE-D1 — Every artifact has its own proof log

Nathan, 2026-10-05, verbatim:

> For the GTWPE, I want to make sure one critical requirement is preserved: every prompt that produces one of the defined GTWPE artifacts must also produce a separate proof log documenting how that artifact was created.
>
> For this requirement, there are only two possible artifact types:
>
> * The redlines Markdown file
> * The final updated PF Markdown file
>
> If a prompt produces either one of these, that output counts as an artifact and requires its own separate proof log. If a prompt produces both, then each artifact must have its own corresponding proof log, unless the prompt explicitly defines a single combined proof log that clearly covers both outputs.
>
> Ordinary conversational responses, status updates, recommendations, analysis, or other inline text do not count as artifacts for this requirement.
>
> Each proof log must, at minimum, record:
>
> * The artifact produced
> * The source files and inputs used
> * The substantive changes made
> * The basis for those changes
> * Any important constraints, assumptions, or interpretations applied
> * Any validation or verification performed
> * Any unresolved issues, limitations, or deviations
> * Enough identifying information to associate the proof log unambiguously with the correct redlines file or final PF file
>
> The proof log should provide enough evidence for another session or reviewer to understand what changed, what those changes were based on, how the artifact was produced, and what was verified.
>
> This requirement must remain intact throughout the GTWPE system. It must not be omitted, weakened, or lost during prompt revisions, consolidation, or handoffs.

What follows from it:

- **Which prompts it binds is decided by what they write, not by their names.** Any GTWPE prompt that
  writes a redlines Markdown file or a final updated PF Markdown file is bound, now and in every later
  version.
- **Every change keeps it whole.** A change to such a prompt, made through GTWPE-MGMT-10, leaves the
  requirement in full: the separate proof log, every minimum item, and the link to its artifact. A
  revision, consolidation or handoff that would drop or weaken any of these does not meet this record.
- **"Proof log" here is not the repository's governed evidence.** Canon and `AGENTS.md` use "proof"
  for evidence about the engine itself, much of it governed and written only by the canonical tools:
  path proofs, and proof logs such as the two-run identity proof log. A GTWPE proof log is the record a
  prompt writes beside its own artifact. This ruling does not make it governed evidence.
- **Canon is silent, so this ruling governs.** PF canon on `main` at `f29d778` was searched for "proof
  log", "processing report", "application report", "redline report" and "apply report". Only "proof
  log" matched. In HDE Governance, the Change Process Guide, the HDE Build Checklist (Separation), HDE
  Schemas and Artifacts, the HDE Mechanics Guide and HDE Phased Epics, each hit is an evidence log for
  the engine's own checks, such as the coupling proof log and the release-ID recompute proof log. The
  Glow QA Guide's one hit is the phrase "proof logic". HDE Build Notes has none. No PF document sets a
  rule for proof logs of technical-writing artifacts.

## GTWPE-D2 — A run's inputs, and every handoff, are files only

Nathan, 2026-10-07, verbatim (`docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md`, ruling 1; ledger
`ERRORS.md`, E-045):

> the only inputs should be the filenames. Any other context will corrupt the run. this needs to be explicitly documented. you may not pass arbitrary context in handoffs

And, in `PE40-INIT-20261007.md` alone:

> make sure this is clear in the operations hub. this is very important at every phase.

What follows from it:

- **A run takes files and nothing else.** The execution prompt that starts GTWPE-FLOW-10 gives `RUN` and
  the run's input files, or `RESUME` and the run's `RUN.md`. Each file is attached or named by its
  repository path. A PF document is named by its directory and versionless name, such as
  `PF10-HDE-Build-Notes` in `docs/pfcanon/`, and the run records the file it resolved and its blob. No
  description of the change, selected boundary, run name, authorization or other context is passed.
- **Nathan's own decisions reach a run as files.** A decision a stop asks for, a PF30 rollover and a
  change's closure decision are files the execution prompt names; a resume names the run's `RUN.md`.
- **Every handoff carries files only.** A pass invocation gives the prompt to run and files: its pass
  directory, its target, its sources, where to write, and the run's `RUN.md`, which gives the branch and
  the pull request. A pass returns its outcome and the repository paths of what it wrote; anything more it
  has to say is in those files.
- **Nothing narrows a source.** There is no selected boundary: every pass reads every source whole.
- **What is given beyond files is not taken.** A run, a pass or a TW prompt invoked directly that is given
  anything beyond the prompt to run and its files stops at intake and names what it was given.
- **It binds GTWPE-MGMT-10 too.** Its request is the files that record it. Nathan's words in those files
  are the request, and any other text in them is a claim to check. Its reviewers and workers are handed
  nothing but their committed brief's repository path.
- **What is not an input.** Naming the prompt to run, as Nathan's answer 2 of 2026-09-29 does; the mode
  of a prompt that has modes, such as GTWPE-MGMT-10's `MODE`, and the Modification ID its `PLAN` and
  `EXECUTE` take, which names the record's file; an output location given as a path on a branch; a
  prompt's own reads of its selection and of the prompt bodies it runs; and Nathan's approvals to
  GTWPE-MGMT-10, which `D21` requires quoted into the record.
- **"at every phase".** It binds every GTWPE prompt, and every prompt, request and handoff written for a
  GTWPE run or Modification. The Operations Hub's current TW section states it.

Nathan accepted these consequences when he approved the analysis of
MODIFICATION-20261007-gtwpe-tw-flow-rulings on 2026-10-07 (its S-1, S-2, S-3 and S-8, and ITEM-07) and then
its plan (its P-3 and P-4, and its reading of the PE Metaprompt's handoff rule); his words are in that
record's `analyze_approved_by` and `plan_approved_by`.

**Canon relied on:** on `main` at `128836a`, HDE Build Notes 2.14 ("Do not pin a PF file version in a
prompt") and HDE Governance §9.1.6 (a document named by its controlled directory and versionless name, the
exact binding kept in run artifacts). Canon sets no rule for how a technical-writing prompt's inputs and
handoffs are given, so this ruling governs there.

## GTWPE-D3 — Every PF10 addendum is drained, and a prompt in the run evaluates the drain targets

Nathan, 2026-10-07, verbatim (`PE40-INIT-20261007.md`, ruling 2; `ERRORS.md`, E-044 and E-051):

> if there are addenda in PF10, that means they need to be drained, otherwise they would not be in there. Whether or not an addendum states an explicit drain target, it needs to be drained.

And:

> part of this run is to have a prompt evaluate the drain targets.

And, on PE40's report of 2026-10-07 (`ERRORS.md`, E-044 and E-052):

> all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target.

And, approving the analysis of MODIFICATION-20261007-gtwpe-tw-flow-rulings on 2026-10-07:

> DC-L1: a drain's `no redlines` return stays exactly as it is, and the equivalence location stays inside the drain.

What follows from it:

- **Every addendum is accounted for.** `RUN.md` and the run's pull request give every change in the run
  its account, each PF10 addendum among them: the documents it drains into, or where it is already
  represented, for each document it bears on; and, for any part of it that cannot drain in this run, why.
- **A change is already represented only on a pass's verified finding, never on the triage's.** That is
  shown by a drain's verified `no redlines`, whose exact equivalence location stays inside the drain, the
  return itself unchanged, or by a record pass's verified `no changes`, for each document the change bears
  on.
- **The triage pass.** TW-TRIAGE-10 is the run's triage pass. GTWPE-FLOW-10 runs it, and it evaluates
  the drain targets against every source the run has, the specification included, and writes its account
  of every change, each PF10 addendum among them, as one triage file. That file is neither of GTWPE-D1's
  two artifact types. Invoked directly, the prompt stays optional routing help.
- **No document is gated on a drain target or a specification, PF20 and PF30 aside.** Every eligible
  document is updated on context and scope, PF27 among them. PF20 and PF30 keep their own rule
  (GTWPE-D4).
- **Canon sets the timing.** A change that belongs to an epic or a CRD, from PF10 or from another source
  such as its specification, drains only after that change's QA and its closure decision (the Change
  Process Guide's *Post-QA documentation drainage ordering (normative)*; HDE Governance §2.0.19, §9.1.1's
  *Historical drainage*, "a Specification or Plan alone does not supersede canon", and §9.1.5). A run
  whose files do not show that change closed holds it back, with the closure it waits for, and every pass
  leaves it undrafted. A CRD's own record in PF30 is not held back: HDE CRD Records §3.2 enters it when
  the CRD is registered and updates it in place (GTWPE-D4). The closure decision reaches a run as a file
  (GTWPE-D2).
- **PF10 is never a target** (Nathan, 2026-09-28: "No, pF10 will NEVER be a merge target, EVER>"). A
  change whose only home is PF10 is accounted for as one that cannot drain.
- **`RUN_NO_CHANGE` only** when every change in the run's account, each PF10 change among them, is shown
  already represented, with no part left to drain, or the account holds no change. A run that drafts nothing
  while a change, or part of one, cannot drain in it ends stopped, naming each and why.

Nathan accepted these consequences when he approved the analysis of
MODIFICATION-20261007-gtwpe-tw-flow-rulings on 2026-10-07 (its S-4 and S-5) and then its plan (its DR-1, its
P-2, its settlement of the triage file, and its repairs RQ-1 and RQ-2); his words are in that record's
`analyze_approved_by` and `plan_approved_by`.

**Canon relied on:** on `main` at `128836a`, HDE Build Notes, *Precedence, versioning, and scope* (an
addendum governs until it is drained; drained guidance leaves at formal revision); the Change Process
Guide, *Post-QA documentation drainage ordering (normative)*; HDE Governance §2.0.19, *Post-closure
maintenance ordering*, §9.1.1, *Historical drainage*, and §9.1.5; HDE CRD Records §3.2.

## GTWPE-D4 — PF20 and PF30 are updated whenever a specification is involved, through their own prompts

Nathan, 2026-10-07, verbatim (`PE40-INIT-20261007.md`, ruling 3; `ERRORS.md`, E-046):

> of course there is PF20

> PF20 and PF30 must be updated as part of this. of course.

And, on PE40's report of 2026-10-07 (`ERRORS.md`, E-046 and E-052):

> If there is a spec involved, those docs are updated. if not, then not. its basic.

And (`ERRORS.md`, E-053):

> PF30 and PF20 DON't need the redliner. They should not need that step. They never have.

And, approving the analysis of MODIFICATION-20261007-gtwpe-tw-flow-rulings on 2026-10-07:

> S-1 to S-8 are accepted, including S-7 for PF10 changes to PF20 and PF30, which sets aside the architecture's §9 sentence "The agent must not update PF20 or PF30 from PF10 alone" for those changes (DC-L2).

What follows from it:

- **With a specification, both; without one, neither.** Whenever a run's inputs include a specification,
  PF20 and PF30 are both updated, each through its own prompt, on the run's context and scope. Without
  one, neither is, and the part of each change that bears on them is accounted for as waiting for one
  (GTWPE-D3). No authorization input exists for either (GTWPE-D2).
- **Only their own prompts.** TW-RECORD-10 updates PF20, and TW-RECORD-20 the PF30 family. Neither document
  goes through the redliner, TW-DRAIN-10 and TW-APPLY-10.
- **The record prompts make every change their document takes.** The specification's record goes in the
  document whose scope it is (HDE Phased Epics §0; HDE CRD Records §1): inserted once, or an existing
  record updated in place, a CRD's as HDE CRD Records §4.2 requires and an epic's within HDE Phased Epics'
  *Drain posture*. Each PF10 change that bears on the document in context and scope goes in too, such as
  HDE Build Notes 2.14's terms for PF30, as Nathan's approval of S-7 sets out, and so does any other change
  a source carries that bears on it; a held-back change waits (GTWPE-D3).
- **An epic's record waits for its closure.** PF20 takes an Epic Specification's record only when the run's
  files show the epic closed (Plan Templates §2, *Historical-only posture (normative)*; Change Process
  Guide §1.1.2, §3.5.1 and §6.3). Until then that record waits, accounted for (GTWPE-D3). A CRD's record
  does not wait: HDE CRD Records §3.2 enters a CRD's record when the CRD is registered and updates it in
  place, and TW-RECORD-20 makes it from the CRD's approval evidence.
- **A record prompt's no-change result** is exactly `no changes`, after it has read the document and
  every source whole.
- **Canon.** HDE Governance §9.1.1 keeps PF20 and PF30 as historical homes that the active workflow does
  not update, and lets only a separately authorized historical drainage action add to them. A drain run
  Nathan starts is that maintenance, not the active workflow, and an update in place keeps a record's
  earlier rows and its identity. The canon conflict on PF20 and PF30 records that ledger E-010 records
  stays Nathan's.

Nathan accepted these consequences when he approved the analysis of
MODIFICATION-20261007-gtwpe-tw-flow-rulings on 2026-10-07 (its S-6 and S-7) and then its plan (its P-2,
and its repairs RQ-1 and RQ-2); his words are in that record's `analyze_approved_by` and
`plan_approved_by`.

**Canon relied on:** on `main` at `128836a`, HDE Governance §9.1.1, with *Historical drainage*; Plan
Templates §2, *Historical-only posture (normative)*; the Change Process Guide §1.1.2, §3.5.1 and §6.3; HDE
CRD Records §1, §3.2, §4.2 and §6; HDE Phased Epics §0 and *Drain posture*; HDE Build Notes 2.14.
