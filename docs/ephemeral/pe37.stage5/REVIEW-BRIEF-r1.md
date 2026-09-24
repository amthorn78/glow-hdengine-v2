---
artifact_type: REVIEW_BRIEF
created_date: 2026-09-24
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.2, *ANALYZE and PLAN review brief*
round: 1 of at most 2 full reviews (D26-A), after the dry run in DRY-RUN.md
reviewers: PE37-R1-A, PE37-R1-B — fresh-context subagents, each with this brief only
committed_before_spawn: true
---

# Review brief — stage 5, round 1

Stage 5 is a rule package, not a Modification's §A or §P, so §1 names the package instead of a
record section. §3, §5 and §6 are the template's fixed text, with only the record path filled.

```plain text
You are <REVIEWER_ID>, reviewing the stage 5 rule package (D26) of the GCFPE MGMT redesign. You did
not author it. This is full review 1 of at most 2 for this package (D26-A).

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch docs/20260924-pe37-stage5, commit dc023a5b6d6f6bdb77e2942c74240b07090cf20b.
Read that commit, not the branch head: `git show dc023a5:<path>`, or `git diff 4c57d92 dc023a5`.
The package is the diff from main @ 4c57d92 to that commit:
  docs/prompt_ecosystem_management/gcfpe.decision-record.md   D26 (appended after D24), a pointer under D20
  docs/prompt_ecosystem_management/modification-template.md   v2.1
  docs/prompt_ecosystem_management/modification_validate.py   format 2.1 checks and selftest
  docs/prompt_ecosystem_management/reviewer-prompt-template.md  the second template
  docs/prompt_ecosystem_management/ecosystem-change-management.md  DISP-001, §5 item 6
  docs/prompt_ecosystem_management/session-working-rules.md   the Loops section
  docs/ephemeral/pe37.stage5/  MGMT-10-REVISION.md, RESUME-PROCEDURE.md, DRY-RUN.md, guard_proof.py
And one Notion page, revised in place and not live: 3e34590a05eb811b93d2da9b4ef8106d, the
GCFPE-MGMT-10 PROPOSED BODY. You may read it through the Notion connector. It is a read, not a copy
(D22): make no file of it, and do not hash or store it.
Its evidence: the task brief docs/ephemeral/pe37.stage5/TASK-01-stage5-process-fix.md, which is on
branch docs/20260924-pe36-to-pe37-succession (PR #480, NOT MERGED; read it with
`git fetch origin docs/20260924-pe36-to-pe37-succession` then `git show FETCH_HEAD:<path>`);
docs/ephemeral/pe36.mgmt-redesign/RECOVERY-ANALYSIS-20260924.md §4.3, §4.4, §6, §7;
docs/ephemeral/modifications/evidence/closeout-residuals/RCA-20260924-closeout-residuals.md §7, §8;
docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-anchor-census.md, *The proposed
MGMT-10 body*. Governing documents: docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md.
Also read AGENTS.md at the repository root. It governs.
The dry run that preceded you: docs/ephemeral/pe37.stage5/DRY-RUN.md. Selftest 64/64, the four
Modification records 4/4, GUARD-001 proven for every D26 check, the parked plan's 11 anchors each
unique, and its texts X2.2 and X3.5 applied on a scratch tree.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1 D26 carries the recovery analysis §7 rules 1-6, the failure path, the checkpoints, the cost
   rule, the old-text search and the escalation triggers, as the task brief §1 lists them, and
   supersedes only D20's loop claim, template rule 3's, and D24 condition 5's uncapped re-review.
C2 A record with no `format` validates exactly as before; all four existing records still pass.
C3 Each format 2.1 check fires: guard_proof.py disables each in a scratch copy and its own
   regressions fail.
C4 The follow-up's text anchors stay unique, and D26 sits after D24's last line so the drafted D25
   lands between D24 and D26.
C5 The MGMT-10 proposed body now runs D26 and resolves each of the census's 12 contradictions, or
   defers one by name; R-ITEM23-gate and R-ITEM40 read 0 on the page.
C6 The resume procedure names every step from here to PR05 and its owner, and step 3 lets the
   resumed plan run under D26 without a full review.
C7 Nothing live changed: no live prompt body, skill, registry row or graph part.

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
A1 The MGMT-10 body's EXECUTE: before the first external write a failed part is blocked and the
   others carry on; after it, D26-B stops everything. Is there a path where a part fails after an
   external write and the session carries on silently, or where "undo its repository steps" undoes
   something that is not the session's?
A2 The new result code PRODUCT_OWNER_ACTION_PENDING exists only on the proposed page. The live
   registry row and graph part declare three results. Is anything live now inconsistent, or does
   the deferral in MGMT-10-REVISION.md hold?
A3 RESUME-PROCEDURE.md step 3 runs no full review: one dry run and at most one diff check. Is that
   within D26-A and the recovery analysis's decision 2 (revised), or does it breach a ruling?
A4 D26's authority: it is recorded from Nathan's instruction of 2026-09-24 and binds from the merge.
   Does anything in D26 go beyond what the recovery analysis §7 and the task brief §1 settled?
A5 The validator: _waived, the order of the ledger checks, a ledger entry that is well-formed except
   for one field, and whether `estimate` is required at the right statuses. Does a legacy record
   now fail anywhere?
A6 The parked plan's anchors and its engine (canon.py reads the decision record): does anything in
   the new text break an assertion there that the dry run did not run (labels X5.2 and close need
   run-time tokens and were only anchor-counted)?
Not exercised by the dry run: whether a session follows the new MGMT-10 text, and the resumed plan.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to docs/ephemeral/pe37.stage5/REVIEW-r1-<REVIEWER_ID>.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
