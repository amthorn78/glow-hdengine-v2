---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), v1.2
round: the one check of the repair's diff allowed in P1 (D26-A rule 2; plan §5, P1: "One dry run, then at most one diff check")
reviewers: one, GTWPE-P1-DC-R1. The template's two reviewers are for full reviews; P1 has a single diff check and no full review
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# P1 diff-check brief, filled

Slots are filled; §3, §5 and §6 are the template's fixed text, unchanged. The brief below is given
to the reviewer as its only brief.

## Canon relied on

Read in writing this brief:

- `AGENTS.md` (current, sha256 `2a28ac5c…`): the canon-first rule and lines 11 to 20.
- PF03 — Technical Writing Best Practices §8 and §15.2.
- PF06 — Change Process Guide §0.6.10 and §1.1.11.
- PF27 — Plan Templates, *Review guardrails*, including *Review stability and no-moving-target
  discipline*.
- PF10 — HDE Build Notes 2.14, 2.29 and 2.30.
- In-flight documents: `GTWPE-IMPLEMENTATION-PLAN-v1.1.md` §2 and §5; `CHECKPOINT.md` §8;
  `design/DRY-RUN-P1.md`; `design/GTWPE-DESIGN-v1.0.md` at `42badb7`; `gcfpe.decision-record.md`
  D26; `reviewer-prompt-template.md` v1.2.

## The brief

```plain text
You are GTWPE-P1-DC-R1, reviewing PLAN of the GTWPE design package, GTWPE-DESIGN v1.0 (plan phase P1; not a Modification record). You did not author it.
This is not a full review. It is the one check of the repair's diff that D26-A rule 2 allows; the plan fixes P1's budget at one dry run and at most one diff check. The prior round is the dry run, recorded at docs/ephemeral/gtwpe.rewrite/design/DRY-RUN-P1.md (commit e70b8edec569fd0b9ef0da64002be67df60ffe7a). The repair diff you are reviewing against it is `git diff e70b8edec569fd0b9ef0da64002be67df60ffe7a 42badb78d254f72e7a184e27a25e156f73a9d9c0 -- docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.0.md`.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20260925-gtwpe-w1, commit 42badb78d254f72e7a184e27a25e156f73a9d9c0. Read that commit, not the branch head.
The record: docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.0.md, the whole file at that commit, with the repair diff above as your scope. Read the unchanged text only as far as you need to judge whether the repair is right and consistent with it.
Its evidence: docs/ephemeral/gtwpe.rewrite/design/DRY-RUN-P1.md; docs/ephemeral/gtwpe.rewrite/design/P1-SOURCE-NOTES.md; docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md §8 (Nathan's rulings, verbatim); docs/ephemeral/gtwpe.rewrite/GTWPE-IMPLEMENTATION-PLAN-v1.1.md (the governing plan, §2 above all); docs/ephemeral/gtwpe.rewrite/ERRORS.md. Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on main, read-only. Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md.
The dry run that preceded you: docs/ephemeral/gtwpe.rewrite/design/DRY-RUN-P1.md, 8 distinct required defects (DR-1 to DR-8, seven R1 and one R3) and 4 listed; the repair claims to fix all 8 and nothing else.
Your record carries a block headed "Canon relied on", listing the PF titles and sections and the in-flight documents you actually read (AGENTS.md canon-first rule; the repository's hook checks that the block exists). Put it after your findings.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. The repair fixes each of DR-1 to DR-8 as DRY-RUN-P1.md §4 states it, and changes nothing else in the design.
C2. DR-1: §4.1's inputs (a), (b), (c) and table §4.1.1 express all six rows of plan §2.2 correctly, including "A specification without PF10" and "PF10 only", under Nathan's rulings that PF20 and PF30 are reached only through their dedicated prompts.
C3. DR-2: every stage check in §5.1 now names a command, and §12.1's P2 list builds each of them: targets-check, validate, approval-check, apply, capture, verify-check, pr-check, postcheck, detect-merge.
C4. DR-3 and DR-4: no normal path copies a repository input's bytes into the run directory, and no path writes a Notion prompt body into a record.
C5. DR-5: §5.1 S2 now states how Path A's candidates are found.
C6. DR-6: no "PF27 §1" citation remains; each now names PF27's *Review guardrails*.
C7. DR-7 and DR-8: §4.2, §4.3 and §4.4 now carry the PE's contract fields, and §1.1 states the PF03, PF06 and PF10 check with a home for every rule it lists.
C8. Nathan's three rulings of 2026-09-28 still hold everywhere the repair touched: "No, pF10 will NEVER be a merge target, EVER>"; "with the exception of PF03 only files with "canon" in their title are valid merge targets"; "PF20 and PF30 are special targets with dedicated prompts".

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
A1. DR-4: a prompt-body Notion input is now recorded by identity only. Does any other path still put the body into the repository: a drafter's captured return quoting it, the G3 package, the run report?
A2. DR-3: repository inputs are now pointers, not copies. Do H3, H4, S3's brief or S4 still assume a source .md exists for a repository input?
A3. DR-1: check each row of §4.1.1 against plan §2.2 word by word, and against §8.7's merge-target classes. Is PF27 "evaluated" exactly when a specification exists, and "not touched" otherwise? Is any PF30 or PF20 work drafted by GTWPE-RUN-10 on any row?
A4. DR-2: can each new check fail selectively (CHK-001 in ecosystem-change-management.md)? Above all approval-check: could a vague or partial reply from Nathan pass, and does "or the package version whose file list is fixed" hold only when the package really fixes the list?
A5. DR-7: does §4.4's contract table agree with §11 on writes, exclusions and results?
A6. DR-8: does §1.1 claim any rule is met without a place in the design that meets it?
A7. Did the repair's new text contradict unchanged text anywhere: §5.1 S1 against §6 H2; §4.1's inputs against §9.5's Q2 row; §12.1's list against §13.2; §4.1.1 against §10.4?
What the dry run did not exercise: a live Drive input; capture of a foreground subagent's return; real G3 reply wording; the nine subcommands, which do not exist until P2.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state; no Notion, Drive, GitHub or session action; no agent (kickoff workaround D6). W1 captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/gtwpe.rewrite/design/REVIEW-P1-DIFFCHECK-R1.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
