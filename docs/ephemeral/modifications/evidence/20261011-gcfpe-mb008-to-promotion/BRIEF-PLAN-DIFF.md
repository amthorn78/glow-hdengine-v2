# PLAN repair DIFF_CHECK brief — reviewer C

Committed before the reviewer is spawned (D24 condition 2, D26-A). The rubric and the cap are the fixed text of the committed `BRIEF-PLAN-1-A.md`, §3 and §5, which bind unchanged.

```plain text
You are REVIEWER-PLAN-DIFF-C, checking the repair of MODIFICATION-20261011-gcfpe-mb008-to-promotion's PLAN after full
review 1. You did not author it, and you were not reviewer A or B.

This is the one bounded check of the repair's diff that D26-A allows after a FULL round. It is not another FULL review.
The rubric and the cap are the fixed text in the committed BRIEF-PLAN-1-A.md (same directory), section 3 (what counts as
a required finding: R1-R4) and section 5 (the cap and the exit). Read those two sections there; they bind you unchanged.
No scope, severity or exit rule is widened. The round-1 reviewer records are immutable.

=== WHAT TO CHECK ===
Repository /home/user/glow-hdengine-v2. Only this diff, between commits, not the working tree or branch head:

    git diff 1b742bb84e42b5fdceb63eebcc2ba3b7cce0b15d 4eb8872 -- \
      docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md \
      docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md \
      docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/

Read whole files at 4eb8872 where the diff needs context. Canon is main at 9312add259ddcf42f98516680c3c003414949f26
(docs/pfcanon/). Read AGENTS.md first; it governs. Governing documents as listed in BRIEF-PLAN-1-A.md section 1, plus the
governance audit's references/project-prompt-registry-schema.md in the installed amthor-workspace-governance-audit tree.
Notion is read-only for you. D22 applies: no copies of page bodies on disk beyond a transient read for one check, no
hashes of bodies. Installed skills are read-only; copy to scratch before running anything:
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/

The repaired plan's dry run: plan/dry-run.json at 4055a357, eleven gates all passing. You can rerun it or any gate: the
command is in plan/dry_run.py's docstring. It reads the fetch records of the session that runs it, so in your session
fetch the pages it needs first (the 56 page ids in plan/edits.json and the nine control page ids in plan/control_check.py)
and pass a time taken just before your fetches.

=== THE EIGHT REQUIRED FINDINGS BEING REPAIRED ===
From REVIEW-PLAN-1-A.md and REVIEW-PLAN-1-B.md in the same directory:
- R-A1 / P-B3 (R1). PR-35's "selected GCFPE-MGMT-10 ... 091426.1" binding and PE's MGMT-10 contract text name the
  manager DN-C A replaces. Repair: edits.json MG-PR35, MG-PE-1, MG-PE-2; guard G-MGMT-1 over all 56 pages.
- R-A2 (R1). The MGMT-10 registry row was unspecified, and two proposal assertions fail on the successor. Repair:
  mgmt10-registry-row.json; registry-header-100926.1.json; registry_assemble.py (build, check, assertions, compare); dry-run
  gate N9; G-TS-1 and G-TS-7 cover MGMT-10.
- R-A3 (R2). M-HEAD duplicated the Prompt ID line; M-TS orphaned "Never without his approval." Repair: M-HEAD spans the
  page state through the Prompt ID line (15 line breaks); M-TS inserts at the paragraph's end; G-MGMT-2 to G-MGMT-5;
  body_check.py's bounded multi-line spans and count-only fixtures.
- P-B1 (R2). In-place controls only partly rewritten, with no check that can fail. Repair: activation-delta-100926.1.json;
  control_check.py (phases activation and archived); PLAN section 7 X15, X16, X19; dry-run gate N10.
- P-B2 (R2). Both 100926.1 contracts carried 091426.1's promoted_at. Repair: the glow-graph-contract patch carries
  promoted_at only for the template's own selected release.
- P-B4 (R1). No post-merge checkpoint. Repair: X22.
- P-B5 (R1). X2's check needed a profile X8 builds. Repair: X2 is a read-only rehearsal; the successor's operations run with
  the others at X4-X6; its profile checks at X12.
- P-B6 (R2). The selected parts took the candidate prologue. Repair: graph_assemble.py flip writes the selected prologue;
  check --flipped compares it.

=== QUESTIONS TO ANSWER ===
Is each of the eight fixed? Did the repair add a new required defect (R1-R4), above all in: the registry assembly
(does the assembled 100926.1 registry carry false or stale header or row values, or drop an assertion it should keep);
control_check.py (a current statement it would pass, or a correct activated page it would fail; its historical-section,
predecessor-marker and struck-text rules); the activation delta (a release-bound statement on a control page it leaves
unstated, or a change it makes to a dated record or to Alpha state); the X2 and X22 steps against D26-B and D26-C; and the
plan's new claims against the dry-run receipt. The LISTED findings of round 1 were deliberately not repaired unless a repair
names them; do not report their absence as a defect. The author's own judgement in a recommendation is Nathan's to accept;
it is a defect only if adopting it as written would silently breach a ruling.
Not exercised by the dry run: the Notion writes themselves; the duplicate (stood in by the testing page); the X6 report
(stood in by the pinned revisions); the selected-stage values (stood in); the package build beyond the redlines, the patch
and the derived profile; the D24 review; the post-flight; the promotion transaction. Questions about them are questions,
not findings, unless the plan as written would make one of them fail or go silently wrong.

=== DELIVERABLE ===
Write a new record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/REVIEW-PLAN-DIFF.md.
First line: the count of distinct confirmed REQUIRED findings. Then the disposition of each of the eight (fixed, not fixed,
or fixed with a new defect); each new required finding with rubric class, exact text or step, evidence, path, likelihood,
consequence, smallest correction, and whether it is in text the repair added; each LISTED observation in one line; the
trend in the count (8 at round 1). State the checks you ran and any you could not. Add a short "Canon relied on" line
(AGENTS.md). Do not edit any other file, commit, push, merge, install, write to Notion, or edit a prompt body or skill.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT. After this check the plan returns to
Nathan with every open finding listed; this check does not impose a zero-finding exit.
```
