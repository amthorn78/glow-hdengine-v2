---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261006-gtwpe-flow-manager
round: PLAN DIFF_CHECK, the one D26-A rule 2 allows after the full reviews; Nathan's analysis approval of 2026-10-06 directs a second reviewer or a diff check if the full review finds a required defect, and it found two
under_review: 43150c6dc24cd15b3aa64171d8d22f5f059a8df2..ed964dcd6a8e7d0f87442295af9ad70d0b269dd8, with the draft body's repairs in place
reviewer: one, GTWPE-FLOW-MANAGER-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which says that
the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews are bounded*). The
checker is told to read its block from this file at the commit that adds it. As the full review's brief did, §1
requires a "Canon relied on" block in the return (ledger E-036).

The draft body is the object of the repair, so the checker reads it in place, as the full reviewer did under
Nathan's approval, which directs this check. It quotes it only by the clause at issue and copies it nowhere
(`D22`).

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `601b330`:
  - Change Process Guide (PF06) §3.5.2.8;
  - HDE Governance (PF04) §9.1.1;
  - Technical Writing Best Practices (PF03) §3.
- In flight:
  - the record's §A (approved) and §P, with the full review's return, `PLAN-REVIEW.md`;
  - `gcfpe.decision-record.md` D22 (its five conditions) and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-FLOW-MANAGER-PLAN-DC

```plain text
You are GTWPE-FLOW-MANAGER-PLAN-DC, reviewing PLAN of MODIFICATION-20261006-gtwpe-flow-manager. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of 1. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-flow-manager/PLAN-REVIEW.md (2 required, R-1 and R-2; 22 listed, L1 to L22). The session confirmed R-1 and R-2, counted L5 and L16 as required too, and repaired all four; the other twenty listed findings stay for Nathan's opt-in. The repair diff: `git -C /home/user/glow-hdengine-v2 diff 43150c6dc24cd15b3aa64171d8d22f5f059a8df2 ed964dcd6a8e7d0f87442295af9ad70d0b269dd8`. Besides the record, gtwpe.handoffs.md and draft-repairs.json, it adds PLAN-REVIEW-BRIEF.md (the full review's brief) and PLAN-REVIEW.md (its return, captured unedited); review the record's, gtwpe.handoffs.md's and draft-repairs.json's changes, and the draft's.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-flow-manager, commit ed964dcd6a8e7d0f87442295af9ad70d0b269dd8. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show ed964dcd6a8e7d0f87442295af9ad70d0b269dd8:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-flow-manager.md, section §P and the front matter's reviews, and only the text the repair diff changed, with what it touches. §P, *Full review (PL3)* and *Repair round (PL3)*, say what changed and why.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-flow-manager/: draft-repairs.json, the nine changes to the draft body, each as its old clause and new text exactly as applied, with the draft's counts before and after; gtwpe.handoffs.md, whose rows F3 and F8 the repair changed.
The draft body of GTWPE-FLOW-10 is the local file /tmp/claude-0/-home-user-glow-hdengine-v2/93ba4e61-b5cc-5c88-a70c-08c9d4d5eb79/scratchpad/c4/flow10/GTWPE-FLOW-10-draft.md, outside the repository, now repaired. Read in place the sections the nine changes touch, whole, and as much else as the check needs. Quote it only by the clause at issue, and cite it by section and line: your answer is captured into the repository, where no prompt body and no longer passage of one may enter (D22). No copy of the draft before the repair exists; draft-repairs.json and its character arithmetic are the record of what changed.
The five TW prompts, GTWPE-MGMT-10 and every control page are Notion pages you do not read (D22: workers do not fetch prompt bodies). The full review's brief, PLAN-REVIEW-BRIEF.md, names the evidence that quotes their texts. Fetch nothing from Notion.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26 (D22's five conditions above all), modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1). Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (601b330), read-only; the repair rests on the Change Process Guide (PF06) §3.5.2.8, the post-QA drain ordering, and HDE Governance (PF04) §9.1.1.
The dry run that preceded the review: §P, *Dry run (PL3)*, P1 to P13. The full review: §P, *Full review (PL3)*.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. R-1 is repaired by the reviewer's own correction, its items 1 to 3: Nathan's decision to leave a held-back PF10 change out is a selected boundary that every invocation for those documents carries; invocation item 5 lets Nathan's decision set a boundary; check 6 after each pass sees a pass that took a held-back change as a basis, and stops its document (S4); S4's row names it. No TW prompt needs to change.
C2. R-2 is repaired: every stop records, as B6 step 4 does, the harness files the session holds that carry a prompt body and what became of each; B6 names its own beside those of the run's earlier sessions; RUN.md holds every session's. D22 condition 5 is met at a stop and at B6.
C3. L5 is repaired: a run in which no routed document has a draft and none has stopped ends after B3 as B1 step 7 does, with RUN_NO_CHANGE, and the result's row says so.
C4. L16 is repaired: X1.4's search uses two -e patterns and no pipe; it finds no hit at 601b330 and hits only in the new file after X1.4.
C5. gtwpe.handoffs.md's F3 and F8 follow the body's new S4 stop, and nothing else in the file changed; «HT» is its new sha256.
C6. Nothing else changed. In the draft, only the nine changes draft-repairs.json records: 26,553 characters plus 944 gives 27,497; 253 lines became 255; the twenty headings and the last words are unchanged. In §P, only the values the repairs move (the draft's 255 lines and 27,497 characters, and «HT»), the evidence table's row for draft-repairs.json, *Full review (PL3)*, *Repair round (PL3)*, the twenty listed findings added to *Open findings*, the *Harness files* entries and the ledger's FULL round, and each describes the round truly.
C7. The session's counts of L5 and L16 as required under R1 are right, and the repair adds no new required defect.

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
A1. Check 6 and its S4: does a pass that took a held-back change as a basis now stop its document on each of the full review's three routes (Nathan's "leave it out", a document triage did not link to the change, a document B5 adds)? Is the check mechanical from what a pass writes? Do a document-level S4, *Redo from canon* and *Resume* fit together: a resume with "leave it out" redoes the document from canon with the boundary, and one with "draft it" keeps the pass's outputs? Does "A difference in checks 1 to 5 is a stop (S6)" sit well beside check 6's S4?
A2. "His decision to leave it out is a selected boundary that excludes the change": is the boundary still Nathan's, as C1's R9 requires ("the Flow Manager never narrows a pass to a selection")? Can a drain take it under its own intake, which accepts an unambiguous natural-language selection?
A3. R-2's text against D22 conditions 4 and 5: subagent transcripts and saves included; "what became of each" against condition 4's deletion or teardown.
A4. L5's new B3 paragraph: its order with stopped documents and with documents B5 adds; does it end the run cleanly without B4 to B6?
A5. The twenty listed findings in *Open findings*: each faithful to PLAN-REVIEW.md, with the reviewer's likelihood and consequence; L20's first half truly met by F3's change.
A6. Anything the repair added that breaks one of the full review's claims C1 to C8 (PLAN-REVIEW-BRIEF.md, §2).
Not exercised: any Notion write, the duplication, how Notion renders the body, and any live run of the prompt.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git diff, git grep, git log, grep, sed and cat is fine, and so is reading the draft at its path. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-flow-manager/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
