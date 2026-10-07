---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261006-gtwpe-flow-manager
round: PLAN DIFF_CHECK 2, at Nathan's opt-in of 2026-10-06, past D26-A's cap of one diff check by his review_cap override (the record's override block)
under_review: 8166328f03e26d07f4b76405a2b097d2c7fa8003..e417b89d17cd15f09e85de41e53402ec2d519ef3, with the draft body's second repair in place
reviewer: one, GTWPE-FLOW-MANAGER-PLAN-DC2, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check 2 brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which says that
the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews are bounded*). The
checker is told to read its block from this file at the commit that adds it. §1 requires a "Canon relied on"
block in the return (ledger E-036).

Nathan's opt-in directs "one check of that repair's diff by a fresh checker who reads the draft". The checker
reads the draft in place, quotes it only by the clause at issue and copies it nowhere (`D22`).

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `601b330`: none beyond what the earlier briefs name; the repair rests on `D22` and the record.
- In flight:
  - the record's §P, with *Diff check (PL3)* and *Repair round 2 (PL3)*, and Nathan's opt-in quoted there;
  - `gcfpe.decision-record.md` D22 (its five conditions) and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-FLOW-MANAGER-PLAN-DC2

```plain text
You are GTWPE-FLOW-MANAGER-PLAN-DC2, reviewing PLAN of MODIFICATION-20261006-gtwpe-flow-manager. You did not author it.
This is a second check of a repair's diff (D26-A rule 2), at Nathan's opt-in, past the cap of one diff check by his review_cap override, which the record's override block names. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-flow-manager/PLAN-DIFFCHECK.md (1 required, DC-R1; 16 listed, DC-L1 to DC-L16). Nathan opted in to repairing DC-R1 only, in the fuller form the checker's notes give, placed so that both RUN_NO_CHANGE endings take it, which also closes DC-L9 and DC-L16; his words are quoted in §P, *Repair round 2 (PL3)*. The repair diff: `git -C /home/user/glow-hdengine-v2 diff 8166328f03e26d07f4b76405a2b097d2c7fa8003 e417b89d17cd15f09e85de41e53402ec2d519ef3`. It changes the record and draft-repairs.json; review both, and the draft's three changes.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-flow-manager, commit e417b89d17cd15f09e85de41e53402ec2d519ef3. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show e417b89d17cd15f09e85de41e53402ec2d519ef3:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-flow-manager.md: the front matter's override block, and §P's *Repair round 2 (PL3)*, with only the other text the repair diff changed (K-3, PO-1, and the DC-R1, DC-L9 and DC-L16 rows of *Open findings, accepted as risks*) and what it touches. *Diff check (PL3)* gives DC-R1 and the checker's smallest correction as found.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-flow-manager/: draft-repairs.json, whose new `round_2` records the draft's three changes, each as its old clause and new text exactly as applied, with the draft's counts before and after; the first round's entries above it are as that round left them.
The draft body of GTWPE-FLOW-10 is the local file /tmp/claude-0/-home-user-glow-hdengine-v2/93ba4e61-b5cc-5c88-a70c-08c9d4d5eb79/scratchpad/c4/flow10/GTWPE-FLOW-10-draft.md, outside the repository, now repaired a second time. Read in place B1, B3, B6, *RUN.md*, *Stop and resume* and *Results*, whole, and as much else as the check needs. Quote it only by the clause at issue, and cite it by section and line: your answer is captured into the repository, where no prompt body and no longer passage of one may enter (D22). No copy of the draft before this repair exists; draft-repairs.json's round_2 and its character arithmetic are the record of what changed.
The five TW prompts, GTWPE-MGMT-10 and every control page are Notion pages you do not read (D22: workers do not fetch prompt bodies). Fetch nothing from Notion.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D22 (its five conditions) and D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1). Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (601b330), read-only.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. DC-R1 is repaired as Nathan directed: B1 step 7 now opens "take B6 steps 2 to 4; then", B3's ending, "the run ends as B1 step 7 does", restates B1 step 7 with the same words, and RUN.md holds the harness files "(B6 step 4, wherever it runs, and every stop)". Each RUN_NO_CHANGE ending takes B6 steps 2 to 4 once, so D22 condition 5's report is made on both endings, and DC-L9 and DC-L16 are closed.
C2. The placement keeps the checker's correction in substance: the checker's literal B3 form together with the same words in B1 step 7 would take the steps twice on B3's ending, and this placement takes them once.
C3. B6 steps 2 to 4 are sound at both endings: at B1 step 7, after B1 step 6 has made RUN.md and the pull request, and at B3's ending, after passes have run; none of them needs a draft to exist.
C4. Nothing else changed. In the draft, only round_2's three changes: 27,497 characters plus 83 gives 27,580; 255 lines, the twenty headings and the last words are unchanged. In the record, only the override block, *Repair round 2 (PL3)*, K-3's character count, PO-1 and the DC-R1, DC-L9 and DC-L16 rows, and each says truly what happened. In draft-repairs.json, only the added round_2.
C5. The repair adds no new required defect.

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
A1. Both RUN_NO_CHANGE endings as now written: does each take B6 steps 2 to 4 exactly once, and in an order that works (step 3's Notion check, step 4's naming in RUN.md, then RUN.md and the pull request saying so, the pull request marked ready, the return)? Can either ending still return without naming a harness file that holds a prompt body?
A2. B6 step 2's GTWPE-D1 check and step 3's "A change since B1 is a stop (S6)" at B1 step 7, minutes after B1 step 3: does either misfire or stop a clean run? Does running them at B3's ending, after redos, behave as B6 does?
A3. The RUN.md line, "(B6 step 4, wherever it runs, and every stop)": does it now cover every place the body discloses harness files?
A4. *Repair round 2 (PL3)*, the override block and the changed rows: do they describe the repair truly, and does anything in them contradict *Diff check (PL3)* or the rest of §P?
Not exercised: any Notion write, how Notion renders the body, and any live run of the prompt.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git diff, git grep, git log, grep, sed and cat is fine, and so is reading the draft at its path. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-flow-manager/PLAN-DIFFCHECK-2.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
