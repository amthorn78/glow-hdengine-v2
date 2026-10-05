---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261005-gtwpe-writing-side
round: PLAN DIFF_CHECK, the one D26-A rule 2 allows after the full reviews; Nathan's opt-in of 2026-10-05 to repairing L1 to L8 asks for it
under_review: c0c66901794dba5e5bf6765084398d656560ce3a..44a297345c8cd9752a0fc7fa986d60bc07923df8
reviewer: one, GTWPE-WRITING-SIDE-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text; §6 is too, except its record-path sentence, which says the
checker writes nothing and its answer is captured (GTWPE-MGMT-10 100526.1, *Reviews are bounded*).
The checker is told to read its block from this file at the commit that adds it.

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- HDE Governance (PF04) §9.1.6 and HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, on `main` at `31deec4`, as §A read them.
- In flight: the record's §A (approved) and §P; `gcfpe.decision-record.md` D22 and D26; the GTWPE
  decision record's GTWPE-D1.

## The brief for GTWPE-WRITING-SIDE-PLAN-DC

```plain text
You are GTWPE-WRITING-SIDE-PLAN-DC, reviewing PLAN of MODIFICATION-20261005-gtwpe-writing-side. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of 1. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-writing-side/PLAN-REVIEW.md (0 required; 8 listed, L1 to L8). Nathan opted in to repairing all eight, each by the reviewer's own correction; his words are quoted in §P, *Repair round (PL3), Nathan's opt-in*. The repair diff: `git -C /home/user/glow-hdengine-v2 diff c0c66901794dba5e5bf6765084398d656560ce3a 44a297345c8cd9752a0fc7fa986d60bc07923df8`.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261005-modification-gtwpe-writing-side, commit 44a297345c8cd9752a0fc7fa986d60bc07923df8. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show 44a297345c8cd9752a0fc7fa986d60bc07923df8:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261005-gtwpe-writing-side.md, section §P, and only the text the repair diff changed, with what it touches.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-writing-side/: edits.json (E6 and E7 changed), e8_guard_proof.py (new), edits_check.py (unchanged).
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1). Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (31deec4), read-only.
The prompt §P edits, GTWPE-MGMT-10 100526.1, is a Notion page you do not read (D22: workers do not fetch prompt bodies). Fetch nothing from Notion.
The dry run that preceded the review: §P, *Dry run (PL3)*, P1 to P9, no required defect; P10 was added in the repair. The full review: §P, *Full review (PL3)*.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. Each of L1 to L8 is repaired by the reviewer's own correction, where §P's *Repair round* table says, and the two places that go past the reviewer's words (L3's restated sentence; L6's "otherwise as still open") say what is true.
C2. «H» is the sha256 of edits.json at 44a2973, and edits_check.py and e8_guard_proof.py each exit 0 on the committed files.
C3. E7's new check phrase, `Capture`, at count 1, still tells the edited page from one E7 did not make, given §P's reading that `Capture`, case-sensitive, occurs 0 times in 100526.1, and that X1.7 (5) checks each edit's place.
C4. e8_guard_proof.py shows E8's rule passing the complete synthetic text, and failing a text that lacks one minimum item, for each of the eight, and a text that lacks the separate proof log; it reads no prompt body and writes nothing.
C5. Nothing else in §P changed, and the repair adds no new required defect.

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
A1. L3. Does dropping E7's prefix and suffix weaken X1.7 (4)? Could the edited page show `Capture` once while E7 landed partly or in the wrong place, and does X1.7 (5) catch that? Is the restated quoting sentence under *How the plan runs* now true of §P, edits.json, edits_check.py and e8_guard_proof.py, and is the brief's 114-character line described correctly?
A2. L8. Does e8_guard_proof.py read GTWPE-D1's eight minimum items correctly from the decision record, and fail each deficient text on that item alone? Could it pass with a parsing error, such as fewer items read? Does P10's row claim more than the script shows?
A3. L1 and L6 in the steps table. Is X4.2 now mechanical on X1.0's one-part branch (pre-read, send, readback, readings)? Is X4.1's rule for T-1 consistent with ITEM-01's disposition and with X5's return?
A4. L2, L4, L5 and L7. Do the new texts read correctly in place (E6 in A2's cell; C5-NEW and C6-NEW on the catalog; X1.0 (1))? Does any of them now contradict §A, GTWPE-D1 or another part of §P?
A5. Whether the diff changes anything the *Repair round* table does not name.
Not exercised by any dry run: every Notion write; how Notion renders the new texts; E8 on a live TW page.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py and e8_guard_proof.py, which write nothing (run them with PYTHONDONTWRITEBYTECODE=1). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-writing-side/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
