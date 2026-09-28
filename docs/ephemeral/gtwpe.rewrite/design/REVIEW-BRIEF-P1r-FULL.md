---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), v1.2
round: full review 1 of at most 2 for this design (D26-A rule 2); plan v1.2 §16.1 gives P1r one dry run and one fresh full review
reviewers: two, GTWPE-P1R-R1-A and GTWPE-P1R-R1-B, fresh general-purpose subagents, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# P1r full-review brief, filled

The slots are filled; §3, §5 and §6 are the template's fixed text, with §6's record-path slot
filled as P1's was. The two reviewers receive the same brief. Reviewer B's differs from A's only in
two places: its first line names `GTWPE-P1R-R1-B`, and §6 names the record file
`REVIEW-P1r-R1-B.md`. Each brief below is given to its reviewer as its only brief.

## Canon relied on

Read in writing this brief:

- `AGENTS.md` (sha256 `2a28ac5c…`): the canon-first rule; PF canon is read-only.
- PF04 — HDE Governance §9.1.6, in full.
- In-flight documents: plan v1.2, §16 above all; `CHECKPOINT.md` §8 and §10.1;
  `design/DRY-RUN-P1r.md`; `design/GTWPE-DESIGN-v1.1.md` at `a33647c`;
  `design/REVIEW-P1-DIFFCHECK-R1.md`; `gcfpe.decision-record.md` D20 to D22 and D26;
  `modification-template.md`; `reviewer-prompt-template.md` v1.2.

## The brief for GTWPE-P1R-R1-A

```plain text
You are GTWPE-P1R-R1-A, reviewing PLAN of the GTWPE design package, GTWPE-DESIGN v1.1 (plan phase P1r; not a Modification record). You did not author it.
This is full review 1 of at most 2 for this mode (D26-A). A second reviewer, GTWPE-P1R-R1-B, reviews the same commit independently; you do not see each other's work. The prior rounds on this design: a dry run and one diff check of v1.0 in P1 (design/DRY-RUN-P1.md; design/REVIEW-P1-DIFFCHECK-R1.md), and the P1r dry run of v1.1 (below).

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20260925-gtwpe-w1, commit a33647c283b92c0687555af1d16d3bc41be7921a. Read that commit, not the branch head.
The record: docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.1.md, the whole file at that commit. §11 (GTWPE-MGMT-10, the change prompt) and §12 and §13 (the new build order and tests) are the heart of this revision; §0.1 lists everything that changed from v1.0.
Its evidence: docs/ephemeral/gtwpe.rewrite/design/DRY-RUN-P1r.md; docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md §8 (Nathan's rulings and directions, verbatim) and §10.1 (the relay that started P1r); docs/ephemeral/gtwpe.rewrite/design/P1-SOURCE-NOTES.md; docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.0.md and design/REVIEW-P1-DIFFCHECK-R1.md (RQ-1 to RQ-3). The governing plan is GTWPE-IMPLEMENTATION-PLAN-v1.2.md, §16 above all, and the error ledger is ERRORS.md; both are on PE37's branch, not this one: read them with `git show origin/docs/20260928-pe37-gtwpe-facilitation:docs/ephemeral/gtwpe.rewrite/GTWPE-IMPLEMENTATION-PLAN-v1.2.md` (commit 0ecb6a1) and the same for ERRORS.md. The ref is already fetched; do not fetch.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on main (origin/main, 0db3f0e), read-only; HDE Governance (PF04) §9.1.6 governs prompt ecosystems. Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also modification_validate.py, notion-write-boundary.md and reviewer-prompt-template.md.
The dry run that preceded you: docs/ephemeral/gtwpe.rewrite/design/DRY-RUN-P1r.md, 6 distinct required defects (DRr-1 to DRr-6, all R1) and 3 listed, all 6 repaired in a33647c, which also added decisions D-14 and D-15.
Your record carries a block headed "Canon relied on", listing the PF titles and sections and the in-flight documents you actually read (AGENTS.md canon-first rule; the repository's hook checks that the block exists). Put it after your findings.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. v1.1 puts GTWPE-MGMT-10 first, in plan v1.2 §16.1's order, and settles every item of plan v1.2 §16.2 (§0.1; §12.1).
C2. GTWPE-MGMT-10, as §11 specifies it, carries one Modification from request to a verified landing. Every step of its three modes names a check, and a record written as §11.3 and §11.4 say passes modification_validate.py at ANALYZED, PLANNED, EXECUTING and COMPLETE once P2(a) adds the `tool` class (the dry run's check 1).
C3. Its tier and closure rules (§11.3) are computable from §6's handoff table without closure.py, and its drift check (§11.4 A0; §11.7) detects a change to its source page, to the PE Metaprompt and on the watched paths.
C4. The route by which each kind of target changes (§11.5) needs no copy of a prompt body; a prompt page's rollback is a re-selection; and the way it reads prompt bodies (§11.6) meets D22's five conditions.
C5. RQ-1 to RQ-3 are carried into the build as PE37 decided under Nathan's delegation: PF27 only with a specification (§4.1.1; §5.1 S2); every input recorded by gtwpe_read.py, and S2's search at the blob (§5.1); a Notion page that is a prompt body refused before any fetch, identified by its title and ID (§5.1 S1).
C6. §4's Boundaries, §4.4's Writes, §11.2, §12.2's destination rule and §14 D-10 agree.
C7. The pilot (§13.2) tests the change prompt as Nathan will use it: W1 follows the published body, the cold run tests the body without W1's context, and every pilot finding against the body becomes GTWPE-MGMT-10's first repair.
C8. Nathan's rulings of 2026-09-28 still hold everywhere v1.1 changed: "No, pF10 will NEVER be a merge target, EVER>"; "with the exception of PF03 only files with "canon" in their title are valid merge targets"; "PF20 and PF30 are special targets with dedicated prompts"; and his G0 direction, "Make sure that the tw mgmt prompt works so I can repair the rest of the prompts, because I am sure none of this works right. that is what I want. All these code words and references mean nothing to me. I need the problem solved".

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
A1. §11.6 and §16 treat the capture of a worker's return, from a transcript that also holds a prompt body, as part of "the check in hand" under D22. Is that reading sound against D22's conditions 2 and 4, and against RQ-3's reasoning in design/REVIEW-P1-DIFFCHECK-R1.md? Does anything else re-read a harness file that holds a body?
A2. §11.3's tier and closure rules. Can a session apply the tier rule to a real change without judgement ("provably changes neither")? Does "read from §6" give the same closure twice? What happens to that rule when §6's table moves into gtwpe-run-procedure.md at P4?
A3. Walk the pilot (§13.2) through ANALYZE, PLAN and EXECUTE (§11.4) against modification_validate.py and modification-template.md. Is any state, field, approval or return missing? The dry run found item_count_at_approval; look for the next one. Check X2 to X5 around the two merges, and X4's PROMOTION_CHECKPOINT_REQUIRED.
A4. §11.5's route for a prompt page: duplicate, edit, identity lines, whole readback, selection. Is any step a silent wrong edit to a prompt body (R2), or a D22 breach? Is its rollback real?
A5. §5.1 S1 after DRr-5: can S1 classify a Notion page by title and ID without fetching its body? Does "its path lies under AI Prompts" catch every prompt body a run could be given?
A6. The build order. Does any section still describe v1.0's order (P2 tools, P3 publish, P4 trials, P5 adoption)? Do §2.2, §3, §12.1, §12.2, §12.5 and §13 agree with plan v1.2 §16.1 and §16.3?
A7. §11.4 A0's drift check. Can it detect each trigger it claims, at the resolution it names? What is the last-close commit before the first Modification closes?
A8. The unchanged text against the new: §4.4 against §11; §6's H12 and H13 against §11.4; D-13 and D-14 against §13.2; §7.4's capture against §11.4's capture paragraph.
What the dry run did not exercise: any Notion write or page duplication (none happens before G2); the real P2(a) validator change (the dry run used a scratch copy with `tool` added); resolving readers.lock against PyPI; a reviewer-record capture other than P0's and P1's.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion, Drive, GitHub or session action; no agent (kickoff workaround D6). W1 captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/gtwpe.rewrite/design/REVIEW-P1r-R1-A.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

## The brief for GTWPE-P1R-R1-B

Identical to the brief above, character for character, except for these two substitutions:

- in its first line, `You are GTWPE-P1R-R1-A` becomes `You are GTWPE-P1R-R1-B`, and in the
  second line, `A second reviewer, GTWPE-P1R-R1-B, reviews` becomes `A second reviewer,
  GTWPE-P1R-R1-A, reviews`;
- in §6, `REVIEW-P1r-R1-A.md` becomes `REVIEW-P1r-R1-B.md`.

W1 builds B's text from A's by exactly these replacements, by script, and records the sha256 of
each brief as sent in the reviews ledger's outcome.
