---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief")
modification: MODIFICATION-20261006-gtwpe-tw-document-rules
round: PLAN full review 1 of at most 2 (D26-A rule 2)
under_review: fd14d328ab5b591f65459b570a3f633377691e88
reviewers: one, GTWPE-TW-DOCUMENT-RULES-PLAN-A, a fresh general-purpose subagent, neither forked nor context-inheriting (Nathan's approval of 2026-10-06: one full review by a single reviewer)
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN review brief, filled

The slots are filled. §3 and §5 are the template's fixed text. §6 is fixed text too, except its
record-path sentence, which says that the reviewer writes nothing and that its answer is captured.
GTWPE-MGMT-10 100526.2, *Reviews are bounded*, says so: "The brief's instruction to write a record
gives way to the write-nothing clause: a reviewer writes nothing, and its return is captured".

The template says to spawn two reviewers. Nathan's approval of 2026-10-06 directs one, with a second
reviewer or a diff check only if this review finds a required defect. The reviewer is told to read its
block from this file at the commit that adds it.

Ledger E-036 found that C2's captured review return had no "Canon relied on" block, which `AGENTS.md`
asks of every review artifact, and that a later brief can require the block in the return itself. §1
below requires it, in the heading form the repository's hook reads.

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `b1bd769`:
  - HDE CRD Records (PF30.1) §3.2 and §6;
  - HDE Governance (PF04) §9.1.1 and §9.1.6;
  - Reference Technical Writing Best Practices (PF03) §7 and §15.1;
  - HDE Phased Epics (PF20) §0;
  - HDE Build Notes, by title (2.30 PF10-CITE-001).
- In flight:
  - the record's §A (approved) and §P;
  - Nathan's target architecture, `docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md`,
    §§4, 5, 8 and 9 and his answers 6 and 8, with his gate ruling of 2026-10-06 as `analyze_approved_by`
    quotes it;
  - `gcfpe.decision-record.md` D21, D22 and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-TW-DOCUMENT-RULES-PLAN-A

```plain text
You are GTWPE-TW-DOCUMENT-RULES-PLAN-A, reviewing PLAN of MODIFICATION-20261006-gtwpe-tw-document-rules. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A). It is the only full review planned: Nathan directed one review by a single reviewer, with a second reviewer or a diff check only if this review finds a required defect. Whatever stays open goes to Nathan with the plan.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-tw-document-rules, commit fd14d328ab5b591f65459b570a3f633377691e88. Read that commit, not the branch head, with `git show fd14d328ab5b591f65459b570a3f633377691e88:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-tw-document-rules.md, section §P. §A is approved and frozen: read it as the scope, not as work to review. Its ITEM-01 to ITEM-08, its rules R2 to R8, its passage list and its A3 pages are what §P carries out. Nathan's approval, quoted in analyze_approved_by, answers Q-1 (the waiver for tw-flowmaster) and gives his ruling of 2026-10-06 on the Last Update Gate, which §P builds where §A says "BN and the source filename".
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/: edits.json (the 57 edits to five operational TW prompts, with GTWPE-D1's items, the absent phrases and the rules for sending); edits_check.py (its consistency check, which reads edits.json and the GTWPE decision record only); ctl_check.py (the pre-read and readback of two control pages, a copy of the last TW change's script).
The five prompts §P edits, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10 at 100626.1, are Notion pages you do not read (D22: workers do not fetch prompt bodies). Each edit's `old` in edits.json is exact page text, cut to the clause at issue; §P's dry run (P3, P4) found each once in a live fetch, by reading, twice, and read each passage with its new text in place. Earlier evidence quotes more of those bodies: docs/ephemeral/modifications/evidence/gtwpe-tw-repository-io/edits-2.json holds the anchors and new texts that made the 100626.1 versions, and evidence/gtwpe-tw-model-advice/edits.json the ones before them. The control pages' current texts that §P replaces are quoted in full in §P, *The control texts*. Fetch nothing from Notion.
GTWPE-MGMT-10 100526.2, the prompt this Modification runs through, is a Notion page too; §P cites its route and rules. docs/ephemeral/modifications/evidence/gtwpe-writing-side/edits.json holds the edits that made 100526.2, and docs/ephemeral/modifications/MODIFICATION-20261005-gtwpe-tw-repository-io.md is the last TW change, whose §P and §E this plan follows for the selection route and the control pages.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1, Nathan's words and what follows from them), reviewer-prompt-template.md (the second template), notion-write-boundary.md and prompt-body-content-policy.md. Nathan's target architecture is docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md on origin/main, above all §§4, 5, 8 and 9 and his answers 6 and 8; its update of 2026-10-06 that records his gate ruling is in an open pull request and not on main, so use his words as analyze_approved_by quotes them.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (b1bd769), read-only. The sections §P relies on most: HDE CRD Records (PF30.1) §3.2 and §6; HDE Governance (PF04) §9.1.1 and §9.1.6; Reference Technical Writing Best Practices (PF03) §7 and §15.1; HDE Phased Epics (PF20) §0; HDE Build Notes (PF10) 2.30 PF10-CITE-001.
The dry run that preceded you: §P, *Dry run (PL3)*, P1 to P11: three defects in the plan's own new texts and two exceptions missing from its D26-E table found and repaired before you (DR-1 to DR-4), and finding P-3 on §A recorded. No required defect open.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. §P can be executed mechanically on its normal path: every value is fixed once (*Values*, *Values fixed in this plan*), every Notion write has its exact text (edits.json; *The control texts*), and every step has a check that could fail.
C2. edits.json carries out ITEM-01 to ITEM-07 as §A settles them, by R2 to R8 and Nathan's gate ruling, and nothing more: it covers §A's passages (with P-1's correction) and the ten identity lines, adds no passage, and each new text replaces only the clause at issue, so that the sentence it sits in still reads as one sentence of that prompt.
C3. The new texts contradict nothing they leave in each body, apart from the exceptions *The new pages' checks* lists; they keep GTWPE-D1 whole in all five prompts (a separate proof log for each file written, every minimum item in Nathan's words, the link by name and place); and they breach no ruling: Nathan's gate ruling, GTWPE-D1, D21-C, D22, D26, the PE Metaprompt's authoring exclusion (no model, surface or effort advice), Nathan's merge rule, and HDE CRD Records §6 on PF30 volumes.
C4. X1.3's readback, step (g), tells each new page as edited from any page the edits did not make: its title and parent, its identity lines, each new text present, each anchor and absent phrase gone by phrase, its headings and last words, GTWPE-D1 by phrase, and the D26-E broad match with its listed exceptions.
C5. W1 to W20 are all the Notion writes the plan makes, each within the authority it cites. The selection page's writes (SEL-1, SEL-2 with *SECTION*), the notes on Alpha 1, HDE TW and the Operations Hub, and the catalog's checked-through commit carry out ITEM-08 and Nathan's Q-1 waiver, and leave exactly one `Current operation` heading on the selection page.
C6. The handoff of the change-history entry is coherent: a drain prepares it as a content redline naming the version TW-APPLY-10 will derive and the preparation date; TW-APPLY-10 derives the same fields and returns a package whose entry disagrees, a loud stop (K-4).

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
A1. The record prompts' new output, REC-OUT, REC-FIELDS, REC-VOL, REC-MISSING, REC-CHECK and REC-BLOCK, as the dry run's DR-1 and DR-2 left them, against §A's ITEM-05 and ITEM-06, HDE CRD Records §3.2 and §6, HDE Governance §9.1.1 (E-010), and the kept text around them, such as "Do not invent volumes, rollover thresholds, numbering/insertion authority", "edit/publish/renumber/insert into an authoritative PF" and "successful creation is not source insertion". Is DR-1's rollover rule faithful to §6 and to §A's R8 statement? Is P-3 right that §A's risk 6 is inexact, or does DR-1 depart from the approved analysis? Would a record prompt know where to write a new volume's review copy and its proof log?
A2. The Last Update Gate in AP-GATE, DC-SRC, DC-SUB and REC-FIELDS against Nathan's ruling: `BN` and the PF10 version for PF10; a non-PF10 source's filename alone; never another PF as a source; `; ` between several sources (K-3); the `BN 13.5` example (K-13). Read the kept text beside them: "Never substitute the redlines artifact/report filename or an inferred gate token", the fileless-source sentence, and the handoff's "source-file header provenance".
A3. Document control and no Draft in the drains and TW-APPLY-10: DC-AUTH, DC-HIST, DC-OTHER, AP-AUTH, AP-AGREE, AP-DATE, AP-REF, AP-STATUS and AP-VERIFY. Do they bring every field forward as §A's ITEM-01 lists it, and make the fields agree? Is K-4 a loud stop, never a silent wrong date? Does the drains' hygiene rule, which removes a Draft marker "anywhere in the target", collide with "Reserve the header's document-control fields for Apply's verified metadata plan" or with AP-STATUS?
A4. PF09-JUDGE and PF09-EVID against §A's ITEM-04 and the kept PF09 text, such as "Done requires the applicable actual completion/acceptance evidence" and "do not automatically close or reopen unrelated rows".
A5. The selection route: *SECTION*'s Current operation and its four paragraphs; SEL-1 sent before SEL-2 in one call; A1-NEW, HDE-NEW, HUB-NEW and CAT-NEW; the waiver's wording against Nathan's Q-1 answer; X4.3 to X4.6's readbacks and ctl_check.py's arguments; «R»'s rule.
A6. The readback's power and the evidence: would X1.3 (g) catch a duplicated, partial or misplaced edit? Do edits_check.py's eleven checks and their injections test what they say? Does any file the branch adds carry a passage of a TW body longer than an edit's anchor (D22)?
Not exercised by the dry run: any Notion write, the duplication and its polling, and how Notion renders the new texts (K-5).

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, grep, sed and cat is fine, and so is running edits_check.py on edits.json, which writes nothing (run it with PYTHONDONTWRITEBYTECODE=1). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/PLAN-REVIEW.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
