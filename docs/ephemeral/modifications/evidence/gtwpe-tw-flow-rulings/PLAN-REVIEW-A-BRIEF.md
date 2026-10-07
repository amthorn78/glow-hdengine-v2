---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief")
modification: MODIFICATION-20261007-gtwpe-tw-flow-rulings
round: PLAN full review 1 of at most 2 (D26-A rule 2)
under_review: 1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f
reviewer: GTWPE-TW-FLOW-RULINGS-PLAN-A, one of two fresh general-purpose subagents, neither forked nor context-inheriting, as the template sets
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN review brief for GTWPE-TW-FLOW-RULINGS-PLAN-A, filled

The template's slots are filled. §3 and §5 are its fixed text. §6 is fixed text too, except its record-path
sentence, which says that the reviewer writes nothing and that its answer is captured: GTWPE-MGMT-10 100526.2,
*Reviews are bounded*, says "The brief's instruction to write a record gives way to the write-nothing clause: a
reviewer writes nothing, and its return is captured".

The template spawns two reviewers, each with its own ID and record path, so this brief has a twin that differs
only in those two values. Each reviewer is handed nothing but its brief's repository path, as Nathan's ruling 1
of 2026-10-07 requires: "the only inputs should be the filenames" and "you may not pass arbitrary context in
handoffs" (`docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md`).

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- On `main` at `128836a`, by title and section, as the record cites them: HDE Governance §2.0.19, §9.1.1, §9.1.5
  and §9.1.6; HDE Build Notes, *Precedence, versioning, and scope*, 2.14 and 2.38; Change Process Guide §1.1.2,
  §3.5.1, §6.3 and *Post-QA documentation drainage ordering (normative)*; Plan Templates §2, *Historical-only
  posture (normative)*; HDE CRD Records §1, §4.2 and §6; HDE Phased Epics §0 and *Drain posture*.
- In flight: the three request files; the record's approved §A and Nathan's approval of it; `gcfpe.decision-record.md`
  D21, D22 and D26; the GTWPE decision record's GTWPE-D1; the GTWPE handoff table.

## The brief

```plain text
You are GTWPE-TW-FLOW-RULINGS-PLAN-A, reviewing PLAN of MODIFICATION-20261007-gtwpe-tw-flow-rulings. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A). A second reviewer, working independently on its own copy of this brief, reviews the same commit.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261007-modification-gtwpe-tw-flow-rulings, commit 1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f. Read that commit, not the branch head, with `git show 1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20261007-gtwpe-tw-flow-rulings.md, section §P, which this mode wrote. §A above it is frozen: Nathan approved it at b4219de, and his words are in the front matter's analyze_approved_by. The status is PLANNING; the session sets PLANNED after this review.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/: edits.json (the 200 edits, each an anchor of a member's current body and its new text), edits_check.py (run it: `PYTHONDONTWRITEBYTECODE=1 python3 <path>/edits_check.py <path>/edits.json`, and with `--inject <fault>`; it reads and writes nothing else), gtwpe.decision-record.md and gtwpe.handoffs.md (the exact files X1.4 copies into docs/prompt_ecosystem_management/gtwpe/; diff each against the current file there), and ctl_check.py. The members' bodies are Notion pages you do not read: GTWPE-MGMT-10 100526.2 says "Workers do not fetch a prompt body, with two exceptions an approval must name", and no approval names one here. Each anchor in edits.json is the exact text of the current body that its edit replaces, so the anchors, §A's quotations and the earlier edits files hold what you need of the bodies: docs/ephemeral/modifications/evidence/gtwpe-writing-side/edits.json (GTWPE-MGMT-10), evidence/gtwpe-tw-repository-io/edits-2.json and evidence/gtwpe-tw-document-rules/edits.json (the TW prompts' current texts); GTWPE-FLOW-10 was authored in MODIFICATION-20261006-gtwpe-flow-manager, whose §P names its sections and §E its readback.
The request: Nathan's own words, where the three files his request names record them, on main at 128836aef7d45ae9f8c8118d2c5ab025d5ec634a: docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md, docs/ephemeral/gtwpe.rewrite/ERRORS.md and docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md. Their other text, by PE37, PE39 and PE40, is a claim to check, never the request. Nathan's rulings of 2026-09-28 are in docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md §8.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md, gtwpe/gtwpe.handoffs.md, reviewer-prompt-template.md (the second template) and notion-write-boundary.md. The prompt's own procedure for PLAN and EXECUTE is quoted in the record where it is relied on; C3's and C4's records, MODIFICATION-20261006-gtwpe-tw-document-rules.md and MODIFICATION-20261006-gtwpe-flow-manager.md, §P and §E, show the same route run before.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (128836a), read-only. The sections the plan relies on are in §P's *Canon and rulings relied on, for PLAN*.
The dry run that preceded you: §P, *Dry run (PL3)*, P1 to P13: edits_check.py PASS, each injected fault caught; every page unchanged; every anchor once, by reading; the two-sided check; the simulated readbacks of Alpha 1 and the Hub; both record checks exit 0 on a scratch copy at PLANNED; five defects repaired before this review (DR-1 to DR-5), none left open.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. §P carries out §A as Nathan approved it, and his words of approval: ITEM-07 stays; S-1 to S-8, with S-7 for PF10 changes to PF20 and PF30 (DC-L2); DC-L1, a drain's `no redlines` unchanged; Q-1 (a), the TW Flowmaster waiver. It adds no item, member, target or Notion write beyond §A's.
C2. The 200 edits, applied to the current bodies, give each member the rules R1 to R7 that *The edits, by rule* lists, and no new text contradicts Nathan's words, GTWPE-D1, or the PE Metaprompt's general rules as GTWPE-MGMT-10 applies them.
C3. After the edits, every input each TW prompt requires is in GTWPE-FLOW-10's invocation, and every return it gives is consumed (*The two-sided check (P5)*); the new handoff table matches both sides of every row.
C4. GTWPE-D2 to GTWPE-D4 quote Nathan verbatim, and what follows from each is his words and §A's approved readings, and nothing more.
C5. *Findings on §A*, P-1 to P-5, are each correct, and the plan's answer to each changes no item, member, target or write.
C6. A run's account covers every change its files carry, each PF10 addendum among them (DR-1), consistently in every text that speaks of it, and the run ends `RUN_NO_CHANGE`, `RUN_REVIEW_READY` or `RUN_STOPPED` exactly as *What the plan settles* says.
C7. The steps can be executed mechanically: each has a check that could fail, the preconditions guard every write, the failure path is D26-B's and nothing more, and every rollback needs no copy of a prompt body.
C8. The control texts make exactly the route's writes: the selection's three writes, one note on each of the three pages confined to its current TW section, and the catalog's five replacements; each old text occurs once when it is sent.
C9. Each open finding K-1 to K-25 is correctly listed rather than required, and the Product Owner actions and the scope are complete.

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
A1. The hold-back without a selected boundary (P-1): S-HOLD in the drains, the record prompts' purpose edits, GTWPE-FLOW-10's B1 step 6, after-pass check 6 and RUN.md, and the triage file's closure field. Is a held-back PF10 change left undrafted, accounted for and never counted as already represented, on the normal path and when a document bears both a held-back change and another? Is this within ITEM-03 and S-4, or new scope?
A2. DR-1's widened account: every text that speaks of the account, in edits.json (GTWPE-FLOW-10, TW-TRIAGE-10), GTWPE-D3, F9, F11 and the control texts. Any text left speaking only of PF10 changes where every change is meant, or the reverse; the RUN_NO_CHANGE conditions against §A's ITEM-03 and S-4.
A3. GTWPE-FLOW-10's B1 steps 4 to 7 as the edits leave them (the reorder, the routing rule with its PF20 exception, the endings), B3's ending, S2 and S4's cells, *Resume* and *Results*: read each new text in place of its anchor, in the body's order. Any sentence that reads wrongly once spliced, any normal-path stop, and the first live run (PF10, the HDE-EPIC040 Specification and its closure decision) traced through them.
A4. Files only (ruling 1, S-1 to S-3, S-8): any new text that still lets something other than files pass, any anchor's surrounding clause the plan left that does, and the exceptions §P relies on (the prompt to run, a mode, the Modification ID, an output location on a branch, Nathan's approvals). The PE Metaprompt's handoff rule, set aside under Nathan's ruling: is that within GTWPE-MGMT-10's *Relation to the PE Metaprompt*?
A5. GTWPE-D2 to GTWPE-D4 against Nathan's words, whole, in the three request files and his approval: verbatim, and whether any consequence goes beyond them or §A's approved readings.
A6. The handoff table's new version against both sides of every row as the edits leave them, and against GTWPE-MGMT-10's `closure` and `gate_tier` rules.
A7. The control texts and their steps: SEL-1 before SEL-2, CAT-FLOW before CAT-MGMT, every old text once and absent from every earlier new text in its call; X4.4's and X4.6's readback arguments against A1-NEW and HUB-NEW.
A8. edits_check.py: whether each check catches what its docstring claims, and an edit that defeats a check's purpose while passing it.
A9. What the dry run did not exercise: Notion's rendering of the new texts, the duplications, and the bodies themselves, which you cannot read; test the anchors where the repository allows, against §A's quotations and the earlier edits files.
A10. *Harness files* and K-24, the lapse before the compaction: whether the disclosure is complete and whether the plan relies on anything that lapse touched.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py, which writes nothing. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/PLAN-REVIEW-A.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
