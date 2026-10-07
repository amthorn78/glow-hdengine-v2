---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261007-gtwpe-tw-flow-rulings
round: PLAN DIFF_CHECK, the one check of the repair's diff that D26-A rule 2 allows; the full review found 8 required defects
under_review: 1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f..9fefe96c1fd1bad898111bc35582619cc75d3c50
reviewer: one, GTWPE-TW-FLOW-RULINGS-PLAN-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# PLAN diff-check brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which says that
the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews are bounded*). The
checker is handed nothing but this file's repository path, as Nathan's ruling 1 of 2026-10-07 requires ("you may
not pass arbitrary context in handoffs"), and reads its block from this file.

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- On `main` at `128836a`, by title and section, as the repair cites them: HDE Governance §2.0.19, §9.1.1 with
  *Historical drainage*, §9.1.5 and §9.1.6; HDE Build Notes, *Precedence, versioning, and scope*, 2.14 and 2.38;
  Change Process Guide §1.1.2, §3.5.1, §6.3 and *Post-QA documentation drainage ordering (normative)*; Plan
  Templates §2, *Historical-only posture (normative)*; HDE CRD Records §1, §3.2, §4.2 and §6; HDE Phased Epics §0
  and *Drain posture*.
- In flight: the three request files; the record's approved §A and Nathan's approval of it; the two full reviews'
  records; `gcfpe.decision-record.md` D21, D22 and D26; the GTWPE decision record's GTWPE-D1; the GTWPE handoff
  table.

## The brief

```plain text
You are GTWPE-TW-FLOW-RULINGS-PLAN-DC, reviewing PLAN of MODIFICATION-20261007-gtwpe-tw-flow-rulings. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of at most 2. The prior round's records are docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/PLAN-REVIEW-A.md (4 required, R-1 to R-4; 25 listed, L1 to L25) and PLAN-REVIEW-B.md (3 required, RQ-B1 to RQ-B3; 28 listed, L1 to L28). The session confirmed the five distinct required findings, and A's L1, A's L10 and B's L6 as required too, and refuted A's L8 and L9: 8 distinct required defects, RQ-1 to RQ-8, each repaired in §P. You review the repair diff against them.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261007-modification-gtwpe-tw-flow-rulings, commit 9fefe96c1fd1bad898111bc35582619cc75d3c50. Read that commit, not the branch head, with `git show 9fefe96c1fd1bad898111bc35582619cc75d3c50:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20261007-gtwpe-tw-flow-rulings.md, section §P, which this mode wrote; §A above it is frozen, approved by Nathan at b4219de, and his words are in the front matter's analyze_approved_by. The status is PLANNING. The repair diff is `git diff 1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f 9fefe96c1fd1bad898111bc35582619cc75d3c50`, over the record and its evidence; the two review briefs were added at f77a77b and the two captured reviews at 9fefe96. §P's *Full review (PL3)* says how each of RQ-1 to RQ-8 was confirmed, *Repair round (PL3)* where each was repaired and what was checked after, and *Listed findings, accepted as risks (PL3)* gives each listed finding's reason.
Its evidence, in docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/: edits.json (now 205 edits, each an anchor of a member's current body and its new text), edits_check.py (run it: `PYTHONDONTWRITEBYTECODE=1 python3 <path>/edits_check.py <path>/edits.json`, and with `--inject <fault>`; it writes nothing), gtwpe.decision-record.md and gtwpe.handoffs.md (the exact files X1.4 copies into docs/prompt_ecosystem_management/gtwpe/; diff each against the current file there and against its version at 1f73053), and ctl_check.py. The members' bodies are Notion pages you do not read: GTWPE-MGMT-10 100526.2 says "Workers do not fetch a prompt body, with two exceptions an approval must name", and no approval names one here. The repair's six new or widened anchors (G-FLOW-10-E37 and E52 to E55, APPLY-10-E19) were checked against the session's live fetches; the repository holds the current texts they cut from in C4's records for GTWPE-FLOW-10 (MODIFICATION-20261006-gtwpe-flow-manager.md, §P, and evidence/gtwpe-flow-manager/draft-repairs.json) and, for TW-APPLY-10, in evidence/gtwpe-tw-repository-io/edits-2.json and evidence/gtwpe-tw-document-rules/edits.json. Where those records do not hold a clause, say so rather than assume.
The request: Nathan's own words, where the three files his request names record them, on main at 128836aef7d45ae9f8c8118d2c5ab025d5ec634a: docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md, docs/ephemeral/gtwpe.rewrite/ERRORS.md and docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md. Their other text, by PE37, PE39 and PE40, is a claim to check, never the request. Nathan's rulings of 2026-09-28 are in docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md §8.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md, gtwpe/gtwpe.handoffs.md, reviewer-prompt-template.md (the second template) and notion-write-boundary.md. MODIFICATION-20260930-gtwpe-tw-model-advice.md holds the permitted exceptions the repair round cites for TW-TRIAGE-10's model-advice bans.
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (128836a), read-only. The sections the repair relies on are in §P's *Canon and rulings relied on, for PLAN*.
The checks after the repair: §P, *Repair round (PL3)*, *Checks after the repair*: edits_check.py PASS on 205 edits, each injected fault caught by its own code; the new anchors once each in the live pages; each changed passage read in place; the two-sided check for the changed rows; the Alpha 1 and Hub readbacks simulated again on the repaired texts; X1.4's search clean; both record checks exit 0 at PLANNING and on a scratch copy at PLANNED; all 18 tables even.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. Each of RQ-1 to RQ-8 is fixed by the repair, where *Repair round (PL3)* says, in every text that carries the defect.
C2. The repair adds no new defect: each new or changed text is accurate to its source, whether canon, Nathan's words, a ruling, a prompt body as the record quotes it, or an earlier record; and each new anchor is unique, absent from every new text after its edit, and overlaps no other edit's anchor.
C3. The repair keeps §P consistent with itself and with its evidence: edits.json, the two gtwpe/ files, the control texts, *The edits, by rule*, *§A's passages*, *What the plan settles*, the two-sided checks, the open findings, the counts and the fixed values «H», «HD» and «HT» agree.
C4. The record corrections are true: K-24, *Harness files*, *Excerpts* and the intro; and the corrections to the dated dry run (DR-1's answer number, P8's simulation, P9's cell count) are recorded beside it, not made in it.
C5. No finding in *Listed findings, accepted as risks (PL3)* is required under §3, and each reason holds.

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
A1. RQ-1's widened hold-back and its exception: whether every text that holds back a change now covers a change from any source (S-HOLD, the record prompts' E10, B1 step 6, check 6, S4, G-FLOW-10-E14, E15 and E18, F3, F8, GTWPE-D3, *SECTION*, A1-NEW, P-1, *What the plan settles*); whether a CRD's own PF30 record is kept outside it the same way everywhere; and whether that exception decides ledger E-010's open conflict, which stays Nathan's. Against HDE Governance §2.0.19 and §9.1.1 with *Historical drainage*, the Change Process Guide's *Post-QA documentation drainage ordering (normative)* and HDE CRD Records §3.2 and §4.2, whole.
A2. RQ-2: whether the part of a change that cannot drain is now accounted for in the triage file (TRIAGE-10-E04, E11, E14), B1 steps 5 to 7, B3, B6 step 5, S4, *Results*, F11, GTWPE-D3, GTWPE-D4 and *SECTION*; and whether PF20 or the PF30 family named in a reason without a specification can still trip B1 step 5's "names an ineligible document to route" or E43's and E50's "with no part left to drain".
A3. RQ-5 and RQ-8: whether "each change not held back that the triage file names for it" and "Files given alone mean `RUN`, and naming this prompt to start it is not an input" close the paths the reviews found and open none: a run that names the prompt and gives files alone; a resume; a held-back change on a document that returns `no redlines`.
A4. RQ-7 and RQ-3: the four new GTWPE-FLOW-10 edits and the new TW-APPLY-10 edit, each anchor against the earlier records that hold its text, each new text against its neighbours; the choice not to edit *Proof logs (GTWPE-D1)*; and the no-change-report exception against P-4.
A5. RQ-6 and RQ-4: GTWPE-D2 to GTWPE-D4's provenance against analyze_approved_by and §P's labels (P-2, P-3, P-4, DR-1, the triage file's settlement, RQ-1, RQ-2), and the handoff table's opening sentence.
A6. The record corrections and the dated-record rule: K-24; *Harness files* on the PE Metaprompt's three fetches and how their lines were counted, the second compaction, the transcript reads and the reviewers' transcripts; *Excerpts*; the corrections to DR-1, P8 and P9, and P8's re-run.
A7. The listed findings' reasons: whether any listed finding is required under §3 after all.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine, and so is running edits_check.py, which writes nothing. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/PLAN-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
