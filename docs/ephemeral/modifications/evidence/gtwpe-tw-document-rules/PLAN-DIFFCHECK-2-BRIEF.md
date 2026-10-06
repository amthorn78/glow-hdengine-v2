---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261006-gtwpe-tw-document-rules
round: PLAN DIFF_CHECK 2, past D26-A's cap of one diff check per mode, on Nathan's opt-in of 2026-10-06 overriding review_cap for one more round
under_review: 87b6058a21766cd358e910147d13cc0fd975dd85..8bd0b386253db1a1120f2ac992af3bf30f627bd5
reviewer: one, GTWPE-TW-DOCUMENT-RULES-PLAN-DC2, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check 2 brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which
says that the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews
are bounded*). The checker is told to read its block from this file at the commit that adds it. As the
earlier briefs did, §1 requires a "Canon relied on" block in the return (ledger E-036).

Nathan's opt-in directs this one check and its exit: if it finds no required defect, the plan returns to
him for approval; if it finds one, the session stops and reports it unrepaired.

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `b1bd769`:
  - HDE CRD Records (PF30.1) §3.2, §4.2 and §4.4, and HDE-CRD-0001's material-change history in §8;
  - HDE Governance (PF04) §9.3.1;
  - HDE CLI-API-Vendor Ref (PF05) §11.1, and the HDE Copy Tonality Guide (PF15)'s change log.
- In flight:
  - the record's §A (approved) and §P, with `PLAN-REVIEW.md` and `PLAN-DIFFCHECK.md`;
  - Nathan's opt-in of 2026-10-06, quoted in §P's *Repair round 2 (PL3), Nathan's opt-in*;
  - `gcfpe.decision-record.md` D22 and D26.

## The brief for GTWPE-TW-DOCUMENT-RULES-PLAN-DC2

```plain text
You are GTWPE-TW-DOCUMENT-RULES-PLAN-DC2, reviewing PLAN of MODIFICATION-20261006-gtwpe-tw-document-rules. You did not author it.
This is a second check of a repair's diff, past D26-A's cap of one, on Nathan's opt-in of 2026-10-06, which overrides review_cap for this one round. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/PLAN-DIFFCHECK.md (1 required, DC-R1; 7 listed, DC-L1 to DC-L7). Nathan opted in to repairing DC-R1 alone: the checker's smallest correction, applied exactly as §P's *Diff check (PL3)* gives it, to DC-HIST in both drains and to AP-AUTH, with the plan's own descriptions of those texts (the DC-HIST and AP-AUTH rows, K-4 and DC-L1) brought into line, and nothing else repaired. The repair diff: `git -C /home/user/glow-hdengine-v2 diff 87b6058a21766cd358e910147d13cc0fd975dd85 8bd0b386253db1a1120f2ac992af3bf30f627bd5`. It changes the record and edits.json only.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-tw-document-rules, commit 8bd0b386253db1a1120f2ac992af3bf30f627bd5. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show 8bd0b386253db1a1120f2ac992af3bf30f627bd5:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-tw-document-rules.md, section §P and the front matter's override, and only the text the repair diff changed, with what it touches. §P, *Repair round 2 (PL3), Nathan's opt-in*, quotes Nathan's words and says what changed.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/: edits.json, whose new texts for DRAIN-10-06, DRAIN-20-06 (DC-HIST) and APPLY-10-03 (AP-AUTH) the repair changed; edits_check.py and ctl_check.py, unchanged.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md. Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (b1bd769), read-only; the repair rests on HDE CRD Records (PF30.1) §3.2, §4.2 and §4.4 and HDE-CRD-0001's material-change history in §8, HDE Governance (PF04) §9.3.1, HDE CLI-API-Vendor Ref (PF05) §11.1 and the HDE Copy Tonality Guide (PF15)'s change log.
The five TW prompts and every control page are Notion pages you do not read (D22: workers do not fetch prompt bodies). Each edit's `old` in edits.json is exact page text; §P quotes the control texts in full. Fetch nothing from Notion.
The earlier rounds: §P, *Dry run (PL3)*, *Full review (PL3)*, *Repair round (PL3)* and *Diff check (PL3)*.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. DC-R1 is repaired by the prior checker's own smallest correction, applied exactly: DC-HIST, in both drains, and AP-AUTH now name the version and the revision date only where the entry's format records them, and a date the format gives another meaning, such as an HDE CRD Records material-change row's decision date, keeps that meaning. A drain updating a PF30 record can now prepare a material-change row that fits HDE CRD Records §4.2, and TW-APPLY-10 accepts it.
C2. The plan's own descriptions now match the repaired texts: the DC-HIST and AP-AUTH rows of *The edits, by rule*, K-4 and DC-L1. DC-R1's row records the repair and the likelihood as Nathan's opt-in corrects it.
C3. Nothing else changed. No anchor, member, edit count, value, step or Notion write changed, and edits.json differs from 87b6058 only in the new texts of DRAIN-10-06, DRAIN-20-06 and APPLY-10-03. «H» is its sha256. edits_check.py passes, with its eleven injected faults each caught by its own code. The override block names review_cap for this one round, and *Repair round 2 (PL3)* quotes Nathan's words verbatim.
C4. The repair adds no new required defect.

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
A1. AP-AGREE, unchanged at Nathan's direction: "All version, date, change-history and gate values in the revised PF must agree with one another; a disagreement is a blocker returned to the preparer." Beside the repaired AP-AUTH, could it make TW-APPLY-10 return a correct PF30 material-change row whose Date is a decision date, or let a wrong one through? Is either outcome a loud stop, or silent?
A2. The repaired DC-HIST and AP-AUTH against HDE CRD Records §4.2 and §4.4, HDE Governance §9.3.1, HDE CLI-API-Vendor Ref §11.1, the HDE Copy Tonality Guide's change log and K-4: does each format's entry now come out right, and does TW-APPLY-10 accept it?
A3. Whether each repaired sentence still reads as one sentence of its prompt, and agrees with the kept text around it, such as DC-HIST's "Do not add identity-only redlines or predate execution to force a change" and AP-DATE.
A4. Whether the diff changes anything *Repair round 2 (PL3)* does not name; whether the plan's descriptions match the texts; whether the override block's wording matches Nathan's "overriding review_cap for one more round".
Not exercised by any dry run: every Notion write; the duplication and its polling; how Notion renders the texts (K-5).

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py on edits.json, which writes nothing (run it with PYTHONDONTWRITEBYTECODE=1). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/PLAN-DIFFCHECK-2.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
