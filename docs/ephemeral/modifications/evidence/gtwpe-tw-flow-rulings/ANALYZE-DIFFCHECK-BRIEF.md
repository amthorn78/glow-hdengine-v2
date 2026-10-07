---
artifact_type: FILLED_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), used for the check of the repair's diff
modification: MODIFICATION-20261007-gtwpe-tw-flow-rulings
round: ANALYZE DIFF_CHECK, the one check of the repair's diff that D26-A rule 2 allows; the full review found 7 required defects
under_review: cc6b92331ce14a0d5244290a6f0b2a1f84484e25..a14fcf38d762a8742cd873ce95a2733ec53708a7
reviewer: one, GTWPE-TW-FLOW-RULINGS-ANALYZE-DC, a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# ANALYZE diff-check brief, filled

§3 and §5 are the template's fixed text. §6 is fixed text too, except its record-path sentence, which says that
the checker writes nothing and that its answer is captured (GTWPE-MGMT-10 100526.2, *Reviews are bounded*). The
checker is handed nothing but this file's repository path, as Nathan's ruling 1 of 2026-10-07 requires ("you may
not pass arbitrary context in handoffs"), and reads its block from this file.

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- On `main` at `128836a`, by title and section, as the repair cites them: HDE Governance §2.0.19, §9.1.1, §9.1.5
  and §9.1.6; HDE Build Notes, *Precedence, versioning, and scope*, 2.14 and 2.37; Change Process Guide §1.1.2,
  §3.5.1, §6.3 and *Post-QA documentation drainage ordering (normative)*; Plan Templates §2, *Historical-only
  posture (normative)*; HDE CRD Records §1, §4.2 and §6; HDE Phased Epics §0 and *Drain posture*.
- In flight: the three request files; the two full reviews' records; `gcfpe.decision-record.md` D21, D22 and
  D26; the GTWPE decision record's GTWPE-D1; the GTWPE handoff table.

## The brief

```plain text
You are GTWPE-TW-FLOW-RULINGS-ANALYZE-DC, reviewing ANALYZE of MODIFICATION-20261007-gtwpe-tw-flow-rulings. You did not author it.
This is the check of the repair's diff (D26-A rule 2), after full review 1 of at most 2. The prior round's records are docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/ANALYZE-REVIEW-A.md (1 required, R-1; 22 listed, L1 to L22) and ANALYZE-REVIEW-B.md (3 required, R-1 to R-3; 20 listed, L1 to L20). The session confirmed all four required findings, and A's L13 and both reviewers' version-pinning and sentence-count findings as required too: 7 distinct required defects, RQ-1 to RQ-7, each repaired in §A. You review the repair diff against them.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20261007-modification-gtwpe-tw-flow-rulings, commit a14fcf38d762a8742cd873ce95a2733ec53708a7. Read that commit, not the branch head, with `git show a14fcf38d762a8742cd873ce95a2733ec53708a7:<path>`. The working tree is at /home/user/glow-hdengine-v2.
The record: docs/ephemeral/modifications/MODIFICATION-20261007-gtwpe-tw-flow-rulings.md: its front matter, its Intake and its section §A. The repair diff is `git diff cc6b92331ce14a0d5244290a6f0b2a1f84484e25 a14fcf38d762a8742cd873ce95a2733ec53708a7 -- docs/ephemeral/modifications/MODIFICATION-20261007-gtwpe-tw-flow-rulings.md`. §A's *Full review (A6)* says how each of RQ-1 to RQ-7 was confirmed and where it was repaired, and *Listed findings, accepted as risks (A6)* gives each listed finding's reason. The commit also adds the two captured reviews; the briefs were added at 024425c.
The request: Nathan's own words, where the three files his request names record them, on main at 128836aef7d45ae9f8c8118d2c5ab025d5ec634a: docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md, docs/ephemeral/gtwpe.rewrite/ERRORS.md and docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md. Their other text, by PE37, PE39 and PE40, is a claim to check, never the request.
Its evidence: the members' bodies are Notion pages you do not read ("Workers do not fetch a prompt body, with two exceptions an approval must name", GTWPE-MGMT-10 100526.2). The record quotes each clause at issue from the authoring session's live fetches. Earlier evidence in the repository holds the anchors and new texts that made the current versions: docs/ephemeral/modifications/evidence/gtwpe-writing-side/edits.json, evidence/gtwpe-tw-repository-io/edits-2.json and evidence/gtwpe-tw-document-rules/edits.json; C4's record, MODIFICATION-20261006-gtwpe-flow-manager.md, §P and §E, for GTWPE-FLOW-10; C2's and C3's records for the Flowmaster waivers. The GTWPE handoff table is docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md.
Its governing documents: docs/prompt_ecosystem_management/ — read gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md; also gtwpe/gtwpe.decision-record.md and reviewer-prompt-template.md (the second template).
Read AGENTS.md first. It governs. PF canon is docs/pfcanon/ on origin/main (128836a), read-only. The sections the repair cites are in the record's *Canon and rulings relied on*.
The dry run that preceded the full review: §A, *Dry run (A6)*, D1 to D9, no required defect left open. After the repair, the session ran D1, D2 and D6 again: both record checks exit 0; 16 tables, all even; 83 of 83 repository quotations found.
Your answer must carry, before its closing line, a block headed exactly `## Canon relied on` that lists what you read: PF canon by title and section, and other governing documents by file and section (AGENTS.md).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. Each of RQ-1 to RQ-7 is fixed by the repair, where *Full review (A6)* says.
C2. The repair adds no new defect: each new sentence is accurate to its source, whether canon, Nathan's words, a ledger row or an earlier record.
C3. The repair keeps §A consistent with itself: the S table, *What changes*, *Member dispositions*, *GTWPE-D1, prompt by prompt*, *Scope*, the risks, *Candidates*, *Open questions*, readiness, the canon table and the front matter agree.
C4. No listed finding is required under §3, and each listed finding's reason holds.

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
A1. RQ-2's new canon text in ITEM-03 and ITEM-05: the closure timing for PF10 drainage and for PF20's epic record, and §9.1.1 as now cited, with the reading that a run Nathan starts after closure is that maintenance and not the active workflow. Against the cited sections, whole.
A2. RQ-1's restated rule (ITEM-05, S-6, risk 6, *The first live run*): whether it now follows ruling 3 and the ruling in E-046 and E-052 without narrowing them, and whether the first live run's text follows from it: PF30 updated with the PF10 changes that bear on it, and HDE-EPIC040's closure decision among the inputs.
A3. RQ-7's scope: whether fixing E-033's "until G5", C3's F-1 and E-042's two links under ITEM-08 is within the item's statement or widens the request, and whether *Scope*'s counts for them hold against the repository's evidence (E-033's and E-042's rows, C4's dry run D5, C3's F-1).
A4. RQ-3: Q-1, readiness and the interaction cost, against C2's and C3's Q-1s and override blocks.
A5. RQ-6: risk 14 against HDE Build Notes 2.14 and HDE Governance §9.1.6, and whether a PF document named by its directory and versionless name still meets ruling 1's "the only inputs should be the filenames".
A6. RQ-4 and RQ-5: ITEM-03's accounting, ITEM-04's repair 3, S-4, and ITEM-01's GTWPE-D2 to GTWPE-D4.
A7. The listed findings' reasons: whether any listed finding is required under §3 after all.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to your final answer only. You write nothing at all: no file, not even under /tmp; no git command that changes any state, including fetch; no Notion read, write, comment or page action; no Drive, GitHub or session action; no agent (a worker writes nothing). Reading with git show, git grep, git log, git diff, grep, sed and cat is fine. The session captures your final answer unedited, by a script, from your own transcript into docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/ANALYZE-DIFFCHECK.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
