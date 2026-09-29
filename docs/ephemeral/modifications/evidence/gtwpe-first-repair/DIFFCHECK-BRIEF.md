---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20260929-gtwpe-first-repair
round: PLAN DIFF_CHECK, the one D26-A rule 2 allows
under_review: e7e4d4c..bba16f9
reviewer: one, GTWPE-FIRST-REPAIR-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text, and §6 is too, except its record-path sentence, as in
`PLAN-REVIEW-BRIEF.md`. The reviewer is told to read this block from the commit that adds it.

Brief: 5544 bytes, sha256 `af41f422f4be041e44ac88af7af39fdec54b7eee6e6846be034c4177d5a4317a`.

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- HDE Governance (PF04) §9.1.6 and HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, on `main` at `fffadb5`.
- In flight: the record's §A and §P at `bba16f9`; `PLAN-REVIEW-A.md` and `PLAN-REVIEW-B.md`;
  `reviewer-prompt-template.md`'s second template; `gcfpe.decision-record.md` D26 (A to C).

## The brief for GTWPE-FIRST-REPAIR-PLAN-DC

```plain text
You are GTWPE-FIRST-REPAIR-PLAN-DC, checking the repair's diff for PLAN of MODIFICATION-20260929-gtwpe-first-repair. You did not author it.
This is the one check of the repair's diff that D26-A rule 2 allows after full review 1. No further round follows it: whatever stays open goes to Nathan with the plan.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20260929-modification-gtwpe-first-repair. The round reviewed commit e7e4d4cab7450d8574c1cc5066c47812005f84bb; the repair is commit bba16f9f885e46632f11115ca9767ef61ab6c0de. Read the diff with `git diff e7e4d4cab7450d8574c1cc5066c47812005f84bb bba16f9f885e46632f11115ca9767ef61ab6c0de -- docs/ephemeral/modifications/`, and any file at bba16f9 with `git show bba16f9f885e46632f11115ca9767ef61ab6c0de:<path>`. The refs are already fetched; do not fetch.
The prior round's records: docs/ephemeral/modifications/evidence/gtwpe-first-repair/PLAN-REVIEW-A.md and docs/ephemeral/modifications/evidence/gtwpe-first-repair/PLAN-REVIEW-B.md at bba16f9. The record's §P, at bba16f9, lists the seven required findings it took from them and each repair, under *Full review (PL3)*, and the checks it ran after them under *Repair check (PL3)*.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md, at the sections your checks need.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (fffadb5), read-only.
GTWPE-MGMT-10's body is a Notion page you do not read; edits.json's anchors stand in for it. You fetch nothing from Notion.
The round's estimate is about 0.2M tokens. Read the diff whole, and the records at the findings you check.
Your record carries a block headed "Canon relied on", after your findings.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. Each of the seven required findings (A's RA-1 to RA-5, B's RB-1 to RB-5, which §P numbers 1 to 7) is fixed by the diff.
C2. The diff introduces no new REQUIRED defect.
C3. The diff repairs nothing else: every listed finding stays listed (K-15 to K-17), and no text outside the seven repairs changed, except the phrase counts and ledger entries the repairs imply.

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
A1. The failure path after the repair (steps 1, 2 and 4, PO-5, X2's rollback): does every stop after W1 now bring a failure record to main, and does any path now leave Nathan with contradictory instructions?
A2. X5's new commands, with P2's scratch-repository evidence: do they work when the remote branch was deleted at merge and when it was kept, and when the local branch still tracks something?
A3. E11's and E12's new texts in edits.json: do they fix RA-4/RB-4 and RA-3 without saying more than their items, and are their new check phrases unique and present?
A4. X2's commit and X4.1's search of «NEW»'s body: fixed, and consistent with X1.12 and X3?
A5. phrases.json and EXEC-READBACK-BRIEF.md, rebuilt: 75 phrases, the brief without counts.
For each of the seven: fixed, not fixed, or fixed with a new defect.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no script or Python run (reading with git show, git diff, git grep, git log, grep and cat is fine); no Notion write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-first-repair/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
