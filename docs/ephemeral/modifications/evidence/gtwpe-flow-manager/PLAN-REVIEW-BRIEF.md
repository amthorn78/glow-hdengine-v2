---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief")
modification: MODIFICATION-20261006-gtwpe-flow-manager
round: PLAN full review 1 of at most 2 (D26-A rule 2)
under_review: 43150c6dc24cd15b3aa64171d8d22f5f059a8df2
reviewers: one, GTWPE-FLOW-MANAGER-PLAN-A, a fresh general-purpose subagent, neither forked nor context-inheriting (Nathan's approval of 2026-10-06: one full review by a single reviewer, who reads the draft body)
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN review brief, filled

The slots are filled. §3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path
sentence, which says that the reviewer writes nothing and that its answer is captured. GTWPE-MGMT-10 100526.2,
*Reviews are bounded*, says so: "The brief's instruction to write a record gives way to the write-nothing clause:
a reviewer writes nothing, and its return is captured".

The template says to spawn two reviewers. Nathan's approval of 2026-10-06 directs one, who reads the draft body,
with a second reviewer or a diff check only if this review finds a required defect. The reviewer is told to read
its block from this file at the commit that adds it.

The draft body is the one prompt body this reviewer reads. It is a local file outside the repository, in the
authoring session's scratchpad, as Nathan approved ("GTWPE-FLOW-10's body is drafted and reviewed in the session
that runs PLAN and is never stored in the repository"). The reviewer reads it in place, quotes from it no more
than the clause at issue, and copies it nowhere (`D22`).

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `601b330`:
  - Technical Writing Best Practices (PF03), whole;
  - Change Process Guide (PF06) §0.2 and §3.5.2.8;
  - HDE Governance (PF04) §0.4, §9.1.1 and §9.1.6;
  - HDE Build Notes, by title (2.29 PF10-CANON-001, 2.38 PF10-AINEUTRAL-001).
- In flight:
  - the record's §A (approved) and §P;
  - Nathan's target architecture, `docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md`, whole;
  - `gcfpe.decision-record.md` D21, D22 and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-FLOW-MANAGER-PLAN-A

```plain text
You are GTWPE-FLOW-MANAGER-PLAN-A, reviewing PLAN of MODIFICATION-20261006-gtwpe-flow-manager. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A). It is the only full review planned: Nathan directed one review by a single reviewer, who reads the draft body, with a second reviewer or a diff check only if this review finds a required defect. Whatever stays open goes to Nathan with the plan.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-flow-manager, commit 43150c6dc24cd15b3aa64171d8d22f5f059a8df2. Read that commit, not the branch head, with `git show 43150c6dc24cd15b3aa64171d8d22f5f059a8df2:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-flow-manager.md, section §P. §A is approved and frozen: read it as the scope, not as work to review. Its ITEM-01 to ITEM-09, its settled design (*The Flow Manager, settled*: B1 to B6, S1 to S6, the run layout, the execution prompt, eligibility, GTWPE-D1, E-006, E-016 and E-022, the handoff table, the catalog) and its risks are what §P carries out. Nathan's approval, quoted in analyze_approved_by, approves three choices: no document copied ahead of its pass; the body drafted and reviewed in this session and never stored in the repository; the new page made by duplicating a child page of the GTWPE parent page (F-2).
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-flow-manager/: gtwpe.handoffs.md, the handoff table's exact text, which X1.4 copies to docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md.
The draft body of the new prompt, GTWPE-FLOW-10 — Run the Technical Writing Flow, is the local file /tmp/claude-0/-home-user-glow-hdengine-v2/93ba4e61-b5cc-5c88-a70c-08c9d4d5eb79/scratchpad/c4/flow10/GTWPE-FLOW-10-draft.md, outside the repository. Read it whole: it is the main object of this review. Its `«V»` in lines 1 and 2 is the version EXECUTE fixes. It is in Notion-flavored Markdown, so its tables are `<table>` blocks. Quote it only by the clause at issue, never more, and cite it by section and line: your answer is captured into the repository, where no prompt body and no longer passage of one may enter (D22).
The five prompts the body runs as passes, TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10, TW-RECORD-10 and TW-RECORD-20 at 100626.2, are Notion pages you do not read (D22: workers do not fetch prompt bodies; Nathan's approval names only the draft). Their intake, output and return texts are in earlier evidence: docs/ephemeral/modifications/evidence/gtwpe-tw-repository-io/edits-2.json holds the anchors and new texts that made the repository input and output rules (the 100626.1 versions), and evidence/gtwpe-tw-document-rules/edits.json the ones that made the 100626.2 versions; §A's *How the TW prompts fit, unchanged* and §P's *The two-sided check (P5)* quote the clauses at issue, which the authoring session found in live fetches. GTWPE-MGMT-10 100526.2, the prompt this Modification runs through, is a Notion page too; §A and §P quote and cite its route and rules, and docs/ephemeral/modifications/evidence/gtwpe-writing-side/edits.json holds the edits that made it. Fetch nothing from Notion.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1, Nathan's words and what follows from them), reviewer-prompt-template.md (the second template), notion-write-boundary.md and prompt-body-content-policy.md. Nathan's target architecture is docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md, whole, with his answers 1 to 8, his directions of 2026-09-29 and his rulings of 2026-10-06 on the Last Update Gate. C1's approved analysis is docs/ephemeral/modifications/MODIFICATION-20261005-gtwpe-writing-side.md §A (A.2, A.4 with *The stop, designed*, A.5, A.6, A.8). Design v1.2 is docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.2.md; its §6 is the table the new file replaces.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (601b330), read-only. The sections the body relies on most: Technical Writing Best Practices (PF03), whole; Change Process Guide (PF06) §0.2 and §3.5.2.8; HDE Governance (PF04) §0.4, §9.1.1 and §9.1.6; HDE Build Notes (PF10) 2.29 PF10-CANON-001 and 2.38 PF10-AINEUTRAL-001; HDE CRD Records (PF30.1) §6.
The dry run that preceded you: §P, *Dry run (PL3)*, P1 to P13: no required defect; both record checks exit 0 on a scratch copy at PLANNED; the two-sided check passes; the draft's structure, phrases and absences as planned, by script; the handoff table's H11 to H13 identical to design §6.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. §P can be executed mechanically on its normal path: every value is fixed once (*Values*, *Values fixed in this plan*), every Notion write has its exact text (the draft for W3, *The catalog texts* for W4), and every step has a check that could fail.
C2. The draft carries out ITEM-01 to ITEM-07 as §A settles them, with §P's findings P-1 to P-4 and *What the plan settles*, and adds nothing outside them. A session given only this body, an execution prompt and the repository could run the flow mechanically to a review-ready pull request or a truthful stop.
C3. Every pass invocation the draft defines supplies what each TW prompt's intake requires, and every return each TW prompt gives is consumed (§P P5), so no TW prompt needs to change.
C4. The draft keeps GTWPE-D1 whole: the Flow Manager writes neither artifact type; every artifact in a run comes from a pass with its own proof log beside it; B6 checks the eight items; and the body carries the requirement and the eight items in Nathan's words.
C5. The draft breaches no ruling: GTWPE-D1; D21-C; D22; Nathan's redlining discipline and stop rule (2026-09-29); no model, effort or strength advice (R16); his eligibility rulings (2026-09-28) and PF27 and PF30 instruction (2026-09-25); his Last Update Gate rulings (2026-10-06); canon read-only (PF10-CANON-001); merges Nathan's (HDE Governance §9.1.1); the post-QA drain ordering (Change Process Guide §3.5.2.8); and the PE Metaprompt's authoring exclusion.
C6. gtwpe.handoffs.md indexes the draft's handoffs correctly for GTWPE-MGMT-10's closure and carries H11 to H13 unchanged; W4's catalog texts add the member's row, the members note, the design entry and the checked-through commit as ITEM-08 and ITEM-09 require, and nothing else.
C7. X1.3's readback, step (h), tells the published page from any page the plan did not intend: title, parent, icon, identity lines, headings, the text read against the draft, GTWPE-D1's phrases, the absent phrases and the D26-E broad match.
C8. W1 to W4 are all the Notion writes the plan makes, each within GTWPE-MGMT-10's *Notion writes* as F-2 applies them and Nathan approved.

=== 3. WHAT COUNTS AS A REQUIRED FINDING — FIXED TEXT, DO NOT EDIT ===
Only these are REQUIRED:
  R1  a defect on the normal success path;
  R2  a silent wrong edit to a prompt body, governed document or control page;
  R3  a silent breach of a Product Owner ruling, however unlikely;
  R4  a plausible path with a silent or destructive outcome.
A failure that ends in a loud stop and a return to Nathan is NOT required: list it as LISTED.
Everything else is LISTED. For each finding give its path (normal or failure), its likelihood, its
consequence, and whether it sits in text the last repair added. Refute your own findings first: a
finding you cannot reproduce from the committed text is not a finding.

=== 4. WHAT TO ATTACK, WEAKEST FIRST ===
A1. The draft's stop and resume design: S1 to S6, which stop a document and which the run; the same-date rule for a drain and its apply; *Resume*'s checks; *Redo from canon*. Can a resumed or redone run silently skip, repeat or double-apply work, leave a superseded draft where a pass will collide with it, or end review-ready with a document missing? Do B4, B5 and B6 terminate (one redo, then S5; B5's one further review)?
A2. The pass invocations and returns against the TW prompts' texts in the C2 and C3 evidence: output paths given as a directory plus a file-name rule for TW-APPLY-10 and the record prompts; the diagnostic's return as a new drain pass that carries the lineage; PARTIAL_PACKAGE; BLOCKED with an input the run holds; a record prompt's question; TW-RECORD-20's rollover paths.
A3. §P's findings P-1 to P-4 and *What the plan settles*: is each faithful to the sources §A cites, or does it change what Nathan approved? Above all P-3, the narrowed check of the remote, and P-2, a held-back PF10 change stopping its documents.
A4. *Eligibility and routing* and the record passes against Nathan's rulings, HDE Governance §9.1.1, ledger E-010, a PF30 rollover and PF20's single structure.
A5. Anything in the draft that would let the Flow Manager write an artifact, edit a draft, merge, write Notion, Drive, Library or canon, create a session, or carry configuration advice; and B6's E-016 and Notion checks.
A6. EXECUTE's steps: X1.0's preconditions; X1.3's duplication of the architecture page, its populated check, the title and icon, W3's send of the draft and the readback's power; X1.4's copy; X2 and X3's merge detection and «M»; W4's row insertion and its readback; X5's restart; the failure path.
A7. gtwpe.handoffs.md's rows F1 to F9 against the draft, its result codes, and the closure §A records.
Not exercised by the dry run: any Notion write, the duplication and its polling, how Notion renders the body and the new table row, and any live run of the prompt.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, grep, sed and cat is fine, and so is reading the draft at its path. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-flow-manager/PLAN-REVIEW.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
