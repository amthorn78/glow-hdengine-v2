---
artifact_type: PE_WORK_RECORD
created_date: 2026-09-29
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
authority: Nathan (Product Owner), 2026-09-29 — the target architecture and his answers to PE37's eight questions, both verbatim below
status: GOVERNING — the target the GTWPE design must meet. It supersedes the GTWPE design's single-session, direct-canon-edit run model where they differ
---

# GTWPE target architecture (Nathan, 2026-09-29)

**What this governs.** The document-writing side of the GTWPE: how a requested change becomes complete, correctly
versioned replacement PF documents in a pull request. It does not change the TW change prompt (GTWPE-MGMT-10, which
repairs prompts) or its pilot.

**PE37's reading, for W1** (each point traces to Nathan's words below):
- Three roles, never the same session: the **Change Manager** (intake and triage of a requested change; prepares the
  execution package), the **Flow Manager** (a standalone session Nathan starts; runs the whole writing flow in one turn,
  with as many subagents as it judges useful), and the **TW change prompt** (repairs the prompts themselves). Item 1 of
  the answers names the first two; the third is PE37's reading, to be confirmed by Nathan.
- Inputs arrive as attached files or as repository paths. The source blob's packaging is not prescribed.
- Output: a PR holding complete replacement documents in a clearly named drafts area; canon files untouched; nothing
  inside a document says "draft". Promotion into canon is out of scope.
- Large PFs are produced by copying the canon file into the drafts area and editing the copy, never by regenerating it:
  six PFs exceed one response (PF04, PF11, PF12, PF14, PF19, PF20).
- Last Update Gate: `BN` + the version of the PF file used as source, or `BN` + the source filename. **Open point:**
  `AGENTS.md` says PF documents other than PF10 never cite PF10 by version; Nathan's rule makes the gate name it.
- PF03 runs the same flow; it is classified reference, not canon, with the same completeness standard.
- PF09, PF20 and PF30 keep specialized handling. PF20 and PF30 reconcile the original specification with every
  applicable PF10 change. PF30 is a volume family (PF30.1, …) and may be split into new volumes; PF20 keeps its current
  single structure until Nathan formally splits it.

## The target architecture, verbatim

Glow Technical Writing Prompt-Flow Ecosystem
The target architecture for the Glow technical-writing ecosystem is a single-turn execution flow. This is ambitious because of the amount of context involved, but the intention is that a sufficiently capable model should be able to complete the entire technical-writing cycle within one standalone session.
1. Manager-session triage
A persistent manager session receives the requested change and performs the initial triage.
Its responsibility is to determine:

* what source material is relevant;
* which PF documents are potentially affected;
* which specification governs the requested work;
* which document-specific technical-writing prompts will be required; and
* what context must be passed into the execution session.

The manager then creates a complete execution prompt for a standalone technical-writing session.
The manager does not perform the document revisions itself. Its job is to prepare and scope the execution.
2. Inputs to the standalone execution session
The standalone session receives the manager's execution prompt together with the required source materials.
The working inputs may include:

* a source blob containing the relevant project/change context, or a relevant PF10 set;
* the governing specification file, which may be either:
   * a CRD, or
   * an Epic Spec;
* the current PF canon documents that may be affected; and
* any additional context identified during manager triage.

The standalone session must perform its own execution-time triage against these inputs rather than blindly assuming that every supplied document requires modification.
3. Single-turn execution
Once initialized, the standalone session should execute the complete workflow in a single turn.
It should:

1. Review the entire supplied context.
2. Reconfirm the scope of the requested change.
3. Determine which eligible PF documents are actually affected.
4. Open a PR for the technical-writing work.
5. Create an adjacent working area within the PR, such as `PF Canon Drafts` or another clearly named equivalent.
6. Copy the affected PF documents into that working area.
7. Run the appropriate technical-writing process against each eligible document.
8. Produce fully revised replacement versions of every affected document.
9. Update document version numbers, dates, last-updated information, and any applicable update gates or equivalent document-control metadata.
10. Perform cross-document consistency checks.
11. Leave the PR in a complete, reviewable state with all proposed replacement documents ready for approval and incorporation into canon.

The existing canonical PF documents remain untouched during this process unless an execution prompt explicitly authorizes modification of them.
4. Meaning of "draft"
The documents produced inside the PR are drafts only in the workflow sense: they are proposed replacements awaiting review and merge.
They must not be written as provisional, incomplete, or internally marked draft documents.
Every generated document must be complete and ready to become the canonical document without further technical-writing cleanup.
Accordingly:

* Do not add `Draft`, `DRAFT`, `Proposed`, `Working Draft`, or similar status language to the document body, title, header, metadata, or document-control fields unless that exact language is independently required by the canonical document format.
* Do not leave placeholders, TODOs, unresolved drafting notes, editorial commentary, temporary annotations, or instructions for a future writer.
* Do not describe the document as awaiting completion.
* Do not preserve an old document status merely because the source copy contained stale status information.
* Do not use the working-folder name, such as `PF Canon Drafts`, as evidence that the documents themselves should carry a draft status.

The distinction is:
PR/workspace status: draft and awaiting review.
Document content and document-control state: complete, current, and publication-ready.
If approved, the document should be capable of becoming canon without another substantive writing pass.
5. Versioning, dates, and update gates
Every affected document must have its document-control information brought fully forward as part of the same technical-writing pass.
The agent must correctly update, where applicable:

* the document's version number;
* the document's last-updated date;
* any other required document dates;
* applicable last-update gates;
* revision or change-history information;
* document-control fields that depend on the revision;
* internal references whose version-sensitive information must change; and
* any equivalent metadata required by that PF document's canonical structure.

These are not optional cleanup tasks. They are part of producing a valid replacement document.
The new version number must represent the resulting revised document rather than retaining the version number of the copied canonical source.
Dates must correspond to the actual revision being produced. An old date must not be retained merely because most of the document remained unchanged.
Any last-update gate or equivalent control mechanism must be evaluated and set from the actual completed change, not copied forward mechanically. The agent must inspect the governing rules and the document's current state and set those values correctly for the new version.
All version, date, revision-history, and update-gate fields within a document must agree with one another. The agent must treat contradictory document-control metadata as an error to resolve before completing the PR.
6. Document eligibility and specialized prompt handling
The technical-writing system should operate only on the designated PF canon documents, with PF03 treated as an explicitly supported special case.
Some documents require their own specialized technical-writing prompts rather than the generic PF-document process.
In particular:

* PF09 uses its own specialized prompt.
* PF20 uses its own specialized prompt.
* PF30 uses its own specialized prompt.
* PF03 must be handled according to its defined special-case rules.

The execution session must select the appropriate prompt or procedure for each document rather than treating every PF document identically.
7. Full-context scope analysis
A critical requirement is that every document-specific technical-writing process must inspect the entire supplied source context for scope relevance.
The agent must not limit itself to:

* explicitly named documents;
* individual extracted passages;
* obvious keyword matches;
* currently marked statuses; or
* only the PF10 text itself.

The purpose of the source blob is to allow the agent to understand the change in context and determine all downstream documentation implications.
This is especially important for PF09.
A document-specific prompt may govern how a particular PF document is rewritten, but it must still evaluate that document against the complete supplied change context.
8. PF09 row-status handling
Earlier versions of the PF09 workflow placed more explicit emphasis on row statuses. That behavior appears to have become less prominent in the current iteration.
That is acceptable provided the new workflow preserves the underlying requirement.
For every potentially affected PF09 row, the agent must inspect the full relevant source context and determine whether the evidence now supports:

* updating the row;
* leaving the row open;
* closing the row; or
* otherwise changing its documented state.

A PF09 row should therefore not remain open merely because no explicit instruction says to close it. Conversely, it should not be closed solely because a related change was implemented.
Its status must be determined from the complete available evidence.
The resulting PF09 must represent the current state of the project after the supplied changes are incorporated, not simply an accumulation of earlier row states.
9. PF20 and PF30 source-of-truth integration
PF20 and PF30 require special treatment because their updates must reflect both the original specification and the subsequent canonical modifications introduced through PF10.
When updating either PF20 or PF30, the technical-writing agent must consider:

1. the original governing specification, whether a CRD or Epic Spec; and
2. all applicable PF10 changes that modify, clarify, supersede, or extend that specification.

The resulting PF20 or PF30 document must represent the effective current state after those sources are reconciled.
The agent must not update PF20 or PF30 from PF10 alone, because doing so may omit requirements that remain valid from the original specification.
Likewise, it must not rely on the original specification alone when PF10 has subsequently changed its effective meaning.
The original specification establishes the underlying requirement set. Applicable PF10 material modifies that requirement set. PF20 and PF30 must reflect the resulting effective state.
10. Completion standard
Before considering a document complete, the standalone execution session must verify that:

* all relevant source context has been considered;
* all required substantive changes have been incorporated;
* document-specific technical-writing rules have been followed;
* cross-document implications have been reconciled;
* the new version number is correct;
* all relevant dates are correct;
* last-update gates and equivalent control fields are correct;
* revision information is internally consistent;
* stale metadata from the prior canonical version has not been carried forward incorrectly;
* no drafting markers, TODOs, placeholders, or editorial notes remain;
* no internal status identifies the document as a draft merely because it resides in the PR draft workspace; and
* the document is complete enough to replace the current canonical version immediately upon approval.

A technically correct content change with incorrect versioning, dates, update gates, or document-control metadata is not a completed technical-writing result.
11. Intended end state
The intended flow is therefore:
Requested change → Manager triage → Complete standalone execution prompt → Standalone session → Context-wide triage → PR creation → PF working copies → Document-specific technical-writing passes → Version/date/update-gate reconciliation → Cross-document consistency review → Complete replacement documents → Review-ready PR
The goal is for the standalone execution session to perform this entire chain in one turn, using the manager-generated prompt and supplied context as a self-contained execution package.
The PR contains proposed replacement documents, but those documents themselves must already represent their final, complete, correctly versioned canonical form. Review should determine whether they are accepted, not whether they still need to be finished.

## Nathan's answers to PE37's eight questions, verbatim

1. Change Manager vs. Flow Manager
Yes. The Change Manager and the Flow Manager are separate roles.
The Change Manager handles the upstream intake and triage of requested changes. It determines what work needs to happen and prepares the material that should be handed off.
The Flow Manager is the execution-side manager for the technical-writing workflow. It receives the prepared prompt and inputs and is responsible for running the full documentation-update flow.
These should not be treated as the same session or role.
2. How the Flow Manager session is started
I start the Flow Manager in a new standalone session.
I initiate that session by instructing it to run the technical-writing flow prompt and provide the required inputs either:
   * as attached files; or
   * as filenames or paths that already exist in the repository.
The Flow Manager should therefore be able to work from either directly attached source material or repository-resident files identified in the invocation.
3. Use of subagents
Yes. The Flow Manager should use as many subagents as it determines are useful or necessary to execute the work correctly.
I am intentionally relying on a high-reasoning model to determine how to divide the work, how many parallel or specialized passes are needed, and how to reconcile the results.
I do not want to prescribe a rigid subagent count or decomposition strategy in advance. The Flow Manager should make that determination from the actual scope and complexity of the change.
4. How proposed files ultimately enter canon
A suggestion for how the resulting files could be incorporated into canon is fine, but this workflow does not need to define or litigate the canon-promotion process.
The responsibility of this flow ends with producing complete, review-ready, correctly versioned replacement documents.
How those files are later approved, moved, merged, or promoted into the canonical location is outside the scope of this workflow.
5. What constitutes the source blob
The source blob is flexible.
It may consist of:
   * an existing PF10 set together with the relevant specification file; or
   * any other file or collection of source material that contains the change context the Flow Manager needs to process.
The specification may be a CRD, Epic Spec, or other governing spec as applicable.
I do not need to prescribe exactly how the source blob is compiled, packaged, organized, or passed into the Flow Manager session.
That packaging decision can be handled by the Change Manager, the Flow Manager, or both, provided the Flow Manager ultimately receives enough context to evaluate the requested change correctly and scan the complete supplied source context for relevance.
6. Last Update Gate
The Last Update Gate may use the following form:
BN + the version number of the PF file used
when the source is a PF document.
If the source is not PF10 or another PF file, the Last Update Gate may instead use:
BN + the source filename
The purpose is to identify the source revision or source artifact that justified the most recent update.
The Flow Manager should therefore derive this field from the actual source used for the update rather than copying forward a stale value.
7. PF03 status
PF03 should be handled by the same technical-writing workflow as the other eligible PF documents.
The only distinction is classification:
   * the other applicable PF documents are treated as canon;
   * PF03 is classified as reference, not canon.
That classification difference should not imply that PF03 is incomplete, provisional, lower-quality, or exempt from the normal completeness and document-control requirements.
If PF03 is updated, the resulting version should still be complete, internally consistent, properly versioned, correctly dated, and ready for use as the current reference document.
8. PF20 and PF30 volume handling
Yes, PF20 and PF30 should continue to receive their specialized treatment, with an additional structural consideration for document size.
PF30
PF30 may consist of multiple volumes where necessary. The existing `PF30.1` naming pattern reflects this possibility.
If PF30 becomes too large to remain practical for agents or humans to read and reason over reliably as a single document, it should be divided into additional logically organized volumes rather than allowed to grow indefinitely.
The Flow Manager should therefore recognize that PF30 is potentially a multi-volume document family and should evaluate the appropriate volume or volumes when determining scope.
PF20
PF20 is also becoming large enough that it may eventually require the same kind of multi-volume treatment.
That structural change has not yet been implemented or formally established, so the Flow Manager should not invent a PF20 volume structure on its own merely because the document is large.
However, the architecture should not assume that PF20 will necessarily remain a single document forever. The workflow should be compatible with a future decision to split PF20 into multiple volumes if that becomes necessary.
Until that change is formally made, PF20 should continue to be handled according to its current established structure.

## Nathan's later directions, 2026-09-29, verbatim

These are part of the target. Nothing in this record is implemented yet: Nathan's direction is "I
don't want to implement anything until we are confident in the change management system."

### Redlining discipline

> I just want to make sure the discipline of the prompts is not glossed over. I have put a LOT of work into these. PF20 and 30 don't need a redliner, since they are only getting one session, but all other processes MUST go through the redlining and redline apply process, with reports for each phase. this is an important determinism and drift control

Nathan's correction, same day, verbatim:

> When I say "y are only getting one session" I mean they only get one SECTION

What this means for the design:
- Every document except PF20 and PF30 (PF03, PF09 and the generic documents) goes through two
  phases: redline creation, then redline apply to the drafts copy. Each phase produces its own
  report.
- PF20 and PF30 need no redliner because each change adds only one section to them. That section is
  written directly, and the pass still produces a report.
- The existing redlining and redline-apply prompts' rules are kept and carried into the new flow,
  not replaced.

### Stop rather than produce substandard results

> if it just ends up being too much for a single turn, then some sort of stop mechanism might be needed. I want that over the production of substandard results.

What this means for the design:
- The Flow Manager's one-turn run is the goal, not a guarantee. When the work does not fit one turn
  at full quality, the Flow Manager stops at a clean phase boundary and reports what is done, what
  is not, and how to resume. It never finishes by lowering quality.
- The exact stop signals and the resume method are still to be designed.

### No model recommendations or strength assessments in the TW prompts

> Update the change list, there should be no hard coded model recommendations or strength assessments at all

Nathan's clarification, same day, verbatim:

> In the tw prompts I mean

What this means for the design:
- No technical-writing prompt carries a model, surface or effort recommendation, a workload profile, a strength rating or a session-strength assessment. Nathan chooses the model and effort for each session.
- The eight current TW-ALPHA prompts lose their model-guidance blocks, and TW-ASSESS-10, the session-strength assessment prompt, is retired with no replacement. The rebuilt GTWPE prompts carry none of this.
- It is an item on the TW prompts' repair list, not a canon change: Nathan ruled that no PF10 addendum is needed ("We don't need an addendum for this, it can just go in the list of repairs.").

## Nathan's direction, 2026-10-05: a proof log for every artifact

Nathan's words are recorded verbatim, once, as GTWPE-D1 in
`docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`, which governs it across the whole
GTWPE and outlives this record.

What this means for the design:
- Every step of the writing flow that writes a redlines Markdown file or a final updated PF Markdown file
  also writes that artifact's own proof log, with at least the contents GTWPE-D1 lists. A step that
  writes both writes one proof log for each, unless its prompt explicitly defines one combined proof log
  that clearly covers both.
- No revision, consolidation or handoff may drop or weaken it.

## Status, 2026-10-05

The change management system this target waited on is proven. GTWPE-MGMT-10 carried three Modifications from
request to a verified landing, each analysed, planned, reviewed and approved by Nathan:

- MODIFICATION-20260929-gtwpe-pilot: one repair to TW-MGMT-10, selected on all four TW pages.
- MODIFICATION-20260929-gtwpe-first-repair: GTWPE-MGMT-10's own repair (092926.2), with the record-check tool
  landed through its own pull request (#566), the first test of the repository route.
- MODIFICATION-20260930-gtwpe-tw-model-advice: the "no model recommendations or strength assessments" item
  above. TW-ALPHA-20261004.1 is selected: seven prompts at 100426.1, TW-ASSESS-10 retired, and tw-flowmaster
  1.3.0 and flowmaster-validate 3.3.2 installed by Nathan.

The writing side described here is still not built; its build is the next decision for Nathan. Open items carried
forward are in `ERRORS.md` (E-029) and the change prompt's candidate list.

### Update, 2026-10-05 (PE39)

Nathan started the build. He approved the analysis of MODIFICATION-20261005-gtwpe-writing-side, which orders it
as six changes, C1 to C6, each run through GTWPE-MGMT-10. The three roles were settled from canon. Nathan kept his
Last Update Gate rule, and he adds one sentence to PF10 exempting the gate before C3. C1 is `COMPLETE` (#573,
merged at `ef75b31`): GTWPE-MGMT-10 100526.2 is selected, and it keeps GTWPE-D1 whole through every later change.
PE39 accepted it against the record on `main`, both record checks, and the catalog and 100526.2 read live. C2, the
TW prompts on the repository with their proof logs, is next when Nathan says so.

### Update, 2026-10-06 (PE39)

C2 is `COMPLETE` (amthorn78/glow-hdengine-v2#577, merged at `7c18c26`). Its first `EXECUTE` stopped on wrong
counts in the plan and left a failure record (#575, ledger E-035); the successor plan re-measured them and ran
clean. TW-ALPHA-20261006.1 is selected: TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and
TW-APPLY-10 at 100626.1. They stay in Notion; they read PF canon from `docs/pfcanon/` on `main`, write their
outputs at the repository path each invocation names under `docs/ephemeral/`, and never merge. TW-DRAIN-10,
TW-DRAIN-20 and TW-APPLY-10 write a separate proof log beside each redlines file and revised PF, with all eight of
GTWPE-D1's items. TW-MGMT-10 is no longer selected; GTWPE-MGMT-10 maintains the TW prompts. TW Flowmaster 1.3.0
does not run this release, so TW runs by Nathan's direct invocations until the Flow Manager (C4).

PE39 accepted it against the record on `main` and both record checks over all six GTWPE records (6/6 each), and
read live in Notion the selection page, *HDE TW*, the GTWPE catalog, *Alpha 1*, the Operations Hub and the three
prompts that GTWPE-D1 binds. C3, the document rules, comes next when Nathan says so; it needs his one PF10
sentence exempting the Last Update Gate first.

### Update, 2026-10-06 (PE39): no PF10 sentence for the Last Update Gate

Nathan ruled that the Last Update Gate needs no PF10 sentence: the gate records the source an update used, and
it is not a citation of PF10. Canon agrees: 2.30 PF10-CITE-001's own drain-target list, built from a line-level
search, names none of the PF headers whose gate carries a PF10 or BN version. C3 builds Nathan's gate rule
(`BN` and the version of the PF file used, or `BN` and the source filename) with no canon change first, and it
can start when he says so. This replaces the last sentence of the update above.

### Update, 2026-10-06 (PE39): the gate for a source other than PF10

Nathan, 2026-10-06, verbatim: "the gate name for a non PF10 source should just be the filename of the source.
that simple", and then: "I would never use a PF target as a source, that does not make sense." So a change's
source is PF10 or a file that is not a PF document, never another PF. The Last Update Gate is `BN` and the PF10
version used when the source is PF10, and the source's filename alone, with no `BN`, for any other source. This
replaces answer 6 above, whose second form was `BN` and the source filename. C3 builds the rule in this form.
