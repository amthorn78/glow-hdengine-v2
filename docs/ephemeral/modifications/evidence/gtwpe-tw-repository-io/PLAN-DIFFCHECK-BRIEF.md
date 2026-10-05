---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261005-gtwpe-tw-repository-io
round: PLAN DIFF_CHECK, the one D26-A rule 2 allows after the full reviews; Nathan's analysis approval of 2026-10-05 directs a second reviewer or a diff check if the full review finds a required defect, and it found one
under_review: 29fe34144d6c9f25ab921f1d583a166f33bc1fdc..2eff7aed837dfe00bed77008ac81cf8ad8c554b8
reviewer: one, GTWPE-TW-REPOSITORY-IO-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which
says that the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews
are bounded*). The checker is told to read its block from this file at the commit that adds it.

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `20d0dd8`, as §A read them:
  - HDE Governance (PF04) §9.1.6;
  - HDE Build Notes (PF10) 2.29 PF10-CANON-001 and 2.38 PF10-AINEUTRAL-001.
- In flight:
  - the record's §A (approved) and §P;
  - Nathan's approval in `analyze_approved_by`;
  - `gcfpe.decision-record.md` D22 and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-TW-REPOSITORY-IO-PLAN-DC

```plain text
You are GTWPE-TW-REPOSITORY-IO-PLAN-DC, reviewing PLAN of MODIFICATION-20261005-gtwpe-tw-repository-io. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of 1. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-tw-repository-io/PLAN-REVIEW.md (1 required, R-1; 16 listed, L1 to L16). The session confirmed R-1, counted L1 as required too, and repaired both; L2 to L16 stay for Nathan's opt-in. The repair diff: `git -C /home/user/glow-hdengine-v2 diff 29fe34144d6c9f25ab921f1d583a166f33bc1fdc 2eff7aed837dfe00bed77008ac81cf8ad8c554b8`. Besides the record, it adds PLAN-REVIEW.md (the full review's return, captured unedited) and changes PLAN-REVIEW-BRIEF.md (only the commit it names); review the record's changes.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261005-modification-gtwpe-tw-repository-io, commit 2eff7aed837dfe00bed77008ac81cf8ad8c554b8. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show 2eff7aed837dfe00bed77008ac81cf8ad8c554b8:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261005-gtwpe-tw-repository-io.md, section §P and the front matter's override and reviews, and only the text the repair diff changed, with what it touches. §P, *Full review (PL3)* and *Repair round (PL3)*, say what changed and why.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-repository-io/: edits.json, edits_check.py and ctl_check.py, all unchanged by the repair.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1). Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (20d0dd8), read-only.
The six TW prompts and every control page are Notion pages you do not read (D22: workers do not fetch prompt bodies); §P quotes the control texts in full. Fetch nothing from Notion.
The dry run that preceded the review: §P, *Dry run (PL3)*, P1 to P8. The full review: §P, *Full review (PL3)*.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. R-1 is repaired by the reviewer's own correction: HDE-NEW and HUB-NEW now carry A1-NEW's sentence word for word, "TW Flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run this release: TW runs by Nathan's direct invocations until the Flow Manager (C4).", and the readbacks check it: X4.4 and X4.6 by `--has`, X4.3 (2) and X4.5 by reading.
C2. L1 is repaired: the override block, *SECTION* and *Nathan's directions* state the waiver as Nathan worded it, for tw-flowmaster ("for TW Flowmaster" on the selection page), and each still says that neither skill runs the release.
C3. Each new `--has` argument is an exact substring of the section ctl_check.py reads on its page (from the new heading to the renamed one) once the values are substituted, and its quoting in the step's command keeps the apostrophe; so ctl_check.py post passes on a correct page and fails on one without the sentence.
C4. Nothing else in §P changed: edits.json and «H» are unchanged, and so is every other step, value and Notion write. The added text (*Full review*, *Repair round*, the *Harness files* entries and the reviews ledger's FULL round) describes the round truly.
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
A1. The Q-1 sentence on each of the four pages against Nathan's Q-1 answer in analyze_approved_by ("the selection page and the notes say that tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run it, and TW runs by Nathan's direct invocations until the Flow Manager (C4)"): A1-NEW, HDE-NEW and HUB-NEW word for word, and *SECTION*'s longer form. Does any page now say less, or more, than he directed?
A2. The `--has` arguments of X4.4 and X4.6: exact match against A1-NEW and HUB-NEW; the quoting inside the Markdown table; whether ctl_check.py's section bounds hold the sentence on both pages; what Notion's rendering could do to it (K-4).
A3. L1's wording against Nathan's words and §A's Q-1 (a): could "for TW Flowmaster" on the selection page, or the override reason, be read as wider or narrower than his waiver?
A4. The session's count of L1 as required under D26-A rule 3: is it right, or should L1 have stayed listed for Nathan's opt-in?
A5. Whether the diff changes anything that *Repair round (PL3)* and the added sections do not name, and whether *Full review (PL3)*'s account (counts, hashes, sizes, times, the hook's flag) is true.
Not exercised by any dry run: every Notion write; how Notion renders the texts (K-4); `git fetch origin main` (K-14).

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py, which writes nothing, or ctl_check.py's functions on text you build in memory, never on disk (run Python with PYTHONDONTWRITEBYTECODE=1). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-repository-io/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
