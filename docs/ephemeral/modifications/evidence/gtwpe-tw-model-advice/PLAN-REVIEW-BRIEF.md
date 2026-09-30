---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief")
modification: MODIFICATION-20260930-gtwpe-tw-model-advice
round: PLAN full review 1 of at most 2 (D26-A rule 2)
under_review: cc08e2a78711ba34cc6874f3dc07108690010e75
reviewers: one, GTWPE-TW-ADVICE-PLAN-A, a fresh general-purpose subagent, neither forked nor context-inheriting (Nathan's direction of 2026-09-30: one full review by a single reviewer)
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN review brief, filled

The slots are filled; §3 and §5 are the template's fixed text, and §6 is too, except its record-path
sentence, which says the reviewer writes nothing and its answer is captured, as a worker writes
nothing (GTWPE-MGMT-10 092926.2, *Reviews are bounded*; the first repair's brief did the same). The
template says to spawn two reviewers; Nathan directed one for this Modification, at his approval of
2026-09-30. The reviewer is told to read its block from this file at the commit that adds it.

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- HDE Governance (PF04) §9.1.6 and HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, on `main` at `f83c755`.
- In flight: the record's §A (approved) and §P; `gcfpe.decision-record.md` D22, D24 and D26.

## The brief for GTWPE-TW-ADVICE-PLAN-A

```plain text
You are GTWPE-TW-ADVICE-PLAN-A, reviewing PLAN of MODIFICATION-20260930-gtwpe-tw-model-advice. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A). It is the only full review planned: Nathan directed one review by a single reviewer, with a second reviewer or a diff check only if this review finds a required defect. Whatever stays open goes to Nathan with the plan.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20260930-modification-gtwpe-tw-model-advice, commit cc08e2a78711ba34cc6874f3dc07108690010e75. Read that commit, not the branch head, with `git show cc08e2a78711ba34cc6874f3dc07108690010e75:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20260930-gtwpe-tw-model-advice.md, section §P. §A is approved and frozen: read it as the scope, not as work to review; its *Revision of 2026-09-30* supersedes the subsections it names.
Its evidence: docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/edits.json (the 69 prompt edits), skill_edits.py (the 32 skill edits), guard_proof.py.
The seven prompts §P edits are TW-ALPHA Notion pages you do not read (D22: workers do not fetch prompt bodies). Each edit's `old`, `start` and `end` in edits.json is exact page text; §P's dry run (P3, P4) found each once in live fetches. Fetch nothing from Notion.
The skills §P edits are installed, read-only, at /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/ (tw-flowmaster, flowmaster-validate). You may read them with grep, sed and cat; they hold no prompt body.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also reviewer-prompt-template.md and notion-write-boundary.md. The change prompt, GTWPE-MGMT-10 092926.2, is summarized where §P cites it; its rules that matter here are quoted in §A and §P.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (f83c755), read-only.
The dry run that preceded you: §P, *Dry run (PL3)*, P1 to P11: no required defect; one finding against §A recorded (P-F1), and one correction of §A's count (P-F2).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. §P can be executed mechanically on its normal path: every value is fixed once (*Values*), every Notion write has its exact text (edits.json; *The control texts*), and every step has a check that could fail.
C2. edits.json removes exactly §A's 63 passages from the seven members, with the identity lines, keeps every exception §A lists, and changes nothing else; with them the flow still works without TW-ASSESS-10 (READY goes to TW-APPLY-10; TW-APPLY-10 requires no assessment; no handoff carries a recommendation).
C3. `absent_after` and `counts_after` in edits.json are right: after the edits those phrases are absent, and the kept terms occur at exactly the listed counts.
C4. skill_edits.py carries out §A's skill scope (*Revision of 2026-09-30*) and nothing more; the Primary core is untouched; the guard proof proves each new guard; P-F2's fourth validator_revision site is required.
C5. The 21 page writes of X1.5 and the 5 control writes of X4.2 to X4.6 are all the Notion writes the plan makes, each within the authority it cites, and PART-01's selection waits for PART-02's verified install.
C6. Nathan's directions at approval are applied: the lean review, the S-1 guard dropped (K-1), the time aim, and C5 recorded.

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
A1. The replacement texts in edits.json that are not pure deletions: the new preflight step 5 of the drains and TW-APPLY-10, the new step 5 of the two record prompts, TW-APPLY-10's "Do not require a large manifest…" sentence, the drains' "Preflight does not require…" sentence, and TW-MGMT-10's "Use PE's supported identity/header scheme. Real missing task capabilities remain exact blockers." Does any of them add or change meaning beyond removing the scoped passage ("Nothing else in those prompts changes")?
A2. The 18 span edits: is the rule for composing old_str from the fetch mechanical, including the block's escaped tags and X1.5's one retry without backslashes? Can a span consume text it should not?
A3. counts_after (for example TW-TRIAGE-10: model 3, advice 2, assessment 2; TW-MGMT-10: model 3, advice 1), derived by the author's reading of the bodies against §A's exceptions. Check them against §A's exception list and the anchors.
A4. *The control texts*: does SECTION's "still apply except where they run or name TW-ASSESS-10 or give model or effort advice" state the prior operation's status unambiguously (§A F-1)? Are the heading counts in X4.4 (32) and X4.6 (139) right from the dry run's 31 and 138?
A5. skill_edits.py: the rewritten profile condition ("carry the exact no-redlines contract"), with K-1 accepted; line 339's kept rule; the GCFPE sentences kept on lines 351 and 352; and whether "Validate the manifest and fixed policies" still reads correctly.
A6. X3 and S-3: if the synced directory never shows the install, does the plan stop loudly and resume correctly? Is the post-install comparison sufficient (tree digests plus the validator)?
A7. P-F2: moving the GCFPE validation profile's validator_revision in flowmaster-validate. Any consequence for the GCFPE beyond §A's S-4?
Not exercised by the dry run: any Notion write, the duplication and polling of X1.5, the install, and the reviewers of X1.4.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no script or Python run, since skill_edits.py and guard_proof.py write directories (reading with git show, git grep, git log, grep, sed and cat is fine); no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/PLAN-REVIEW.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
