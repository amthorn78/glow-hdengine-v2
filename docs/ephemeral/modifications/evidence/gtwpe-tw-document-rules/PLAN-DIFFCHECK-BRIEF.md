---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261006-gtwpe-tw-document-rules
round: PLAN DIFF_CHECK, the one D26-A rule 2 allows after the full reviews; Nathan's analysis approval of 2026-10-06 directs a second reviewer or a diff check if the full review finds a required defect, and it found one
under_review: fd14d328ab5b591f65459b570a3f633377691e88..6679e4b299b2c92fbb802b59cc1a08517cd8321b
reviewer: one, GTWPE-TW-DOCUMENT-RULES-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which
says that the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews
are bounded*). The checker is told to read its block from this file at the commit that adds it. As the
full review's brief did, §1 requires a "Canon relied on" block in the return (ledger E-036).

## Canon relied on

- `AGENTS.md`: the canon-first rule, and PF canon is read-only.
- On `main` at `b1bd769`:
  - HDE CRD Records (PF30.1) §3.2, §6 and §7;
  - HDE Phased Epics (PF20) §1 and §2.6.1;
  - HDE Governance (PF04) §9.1.1 and §9.3.1;
  - HDE CLI-API-Vendor Ref (PF05) §11.1, and the HDE Copy Tonality Guide (PF15)'s change log.
- In flight:
  - the record's §A (approved) and §P, with the full review's return, `PLAN-REVIEW.md`;
  - Nathan's approval in `analyze_approved_by`, and his target architecture's §4;
  - `gcfpe.decision-record.md` D22 and D26;
  - the GTWPE decision record's GTWPE-D1.

## The brief for GTWPE-TW-DOCUMENT-RULES-PLAN-DC

```plain text
You are GTWPE-TW-DOCUMENT-RULES-PLAN-DC, reviewing PLAN of MODIFICATION-20261006-gtwpe-tw-document-rules. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of 1. Prior round's record: docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/PLAN-REVIEW.md (1 required, R-1; 15 listed, L1 to L15). The session confirmed R-1, counted L5 and its own finding S-1 as required too, and repaired all three; the other fourteen listed findings stay for Nathan's opt-in. The repair diff: `git -C /home/user/glow-hdengine-v2 diff fd14d328ab5b591f65459b570a3f633377691e88 6679e4b299b2c92fbb802b59cc1a08517cd8321b`. Besides the record and edits.json, it adds PLAN-REVIEW-BRIEF.md (the full review's brief) and PLAN-REVIEW.md (its return, captured unedited); review the record's and edits.json's changes.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261006-modification-gtwpe-tw-document-rules, commit 6679e4b299b2c92fbb802b59cc1a08517cd8321b. Read that commit, not the branch head, with `git -C /home/user/glow-hdengine-v2 show 6679e4b299b2c92fbb802b59cc1a08517cd8321b:<path>`.
The record: docs/ephemeral/modifications/MODIFICATION-20261006-gtwpe-tw-document-rules.md, section §P and the front matter's reviews, and only the text the repair diff changed, with what it touches. §P, *Full review (PL3)* and *Repair round (PL3)*, say what changed and why.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/: edits.json, whose new texts for six rule keys the repair changed (DC-HIST, REC-FIELDS-PF20, REC-FIELDS-PF30, REC-CHECK, AP-AUTH, AP-VERIFY); edits_check.py and ctl_check.py, unchanged.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md (GTWPE-D1). Nathan's target architecture is docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md on origin/main; its §4 says what "draft" means. Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (b1bd769), read-only; the repair rests on HDE CRD Records (PF30.1) §3.2, §6 and §7, HDE Phased Epics (PF20) §1 and §2.6.1, HDE Governance (PF04) §9.1.1 and §9.3.1, HDE CLI-API-Vendor Ref (PF05) §11.1 and the HDE Copy Tonality Guide (PF15)'s change log.
The five TW prompts and every control page are Notion pages you do not read (D22: workers do not fetch prompt bodies). Each edit's `old` in edits.json is exact page text; §P quotes the control texts in full. Fetch nothing from Notion.
The dry run that preceded the review: §P, *Dry run (PL3)*, P1 to P11. The full review: §P, *Full review (PL3)*.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md; ledger E-036).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. R-1 is repaired by the reviewer's own correction: REC-FIELDS-PF20 and REC-FIELDS-PF30 now hold the inserted entry (in TW-RECORD-20, record) and the control fields to the no-Draft rule, and say that every other byte stays as canon has it, a template's placeholders and earlier records among them; REC-CHECK checks the inserted entry and those fields. On PF20 and PF30.1 as they are on main, a run can meet "copied byte for byte" and the no-Draft rule at once.
C2. S-1 is repaired: DC-HIST and AP-VERIFY now except what "canon requires ... there, as in a template or a record kept as history", ITEM-03's own "except where canon requires it", so a drain on PF20 keeps §2.6.1's historical "TBD" and TW-APPLY-10 accepts it.
C3. L5 is repaired: a drain prepares the change-history entry in the target's own entry format, dated with the preparation date only where that format dates an entry, and AP-AUTH expects the date it derives on the same condition. K-4 still holds where the format dates an entry.
C4. The selection page's two sentences (*SECTION* and its *Current operation*) and A1-NEW now state the repaired rule, and no readback depends on the changed words.
C5. Nothing else in §P changed: anchors, members, edit counts, values, steps and Notion writes are as before; «H» is the repaired edits.json's sha256; edits_check.py passes, with its eleven injected faults each caught by its own code. The added text (*Full review (PL3)*, *Repair round (PL3)*, the *Harness files* entries and the ledger's FULL round) describes the round truly.
C6. The session's counts of L5 and S-1 as required under D26-A rule 3 are right, and the repair adds no new required defect.

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
A1. R-1's repair against PF20 and PF30.1 on main, HDE Governance §9.1.1, HDE CRD Records §6 and §7, and ITEM-03. Can a record run now meet every rule at once, on the normal path and on a rollover? Does "every other byte stays as canon has it" conflict with REC-VOL's rollover changes to the active volume (Volume status, Next volume), with REC-FIELDS' own control fields, or with a stale status that sits outside the header?
A2. S-1's repair. Is "unless canon requires that exact language there, as in a template or a record kept as history" faithful to ITEM-03 and the architecture's §4? Does it let a drain keep a real drafting marker, such as a TODO or an editorial note, by calling it canon? Was the session right that the prior wording would have had a drain remove PF20's historical "TBD"?
A3. L5's repair against HDE CLI-API-Vendor Ref §11.1, the HDE Copy Tonality Guide's change log, HDE Governance §9.3.1's entry grammar and K-4. Does any target's entry now go undated where its format dates one, or the reverse? Do DC-HIST and AP-AUTH still agree with AP-AGREE and AP-VERIFY?
A4. The session's count of L5 and S-1 as required: right, or should either have stayed listed for Nathan's opt-in?
A5. Whether the diff changes anything that *Repair round (PL3)* and the added sections do not name, and whether *Full review (PL3)*'s account (counts, hashes, sizes, times) is true.
Not exercised by any dry run: every Notion write; the duplication and its polling; how Notion renders the texts (K-5).

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py on edits.json, which writes nothing (run it with PYTHONDONTWRITEBYTECODE=1). The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-document-rules/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
