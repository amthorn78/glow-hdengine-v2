# PLAN bounded-repair DIFF_CHECK brief — reviewer D

Committed before the reviewer is spawned (D24 condition 2, D26-A). Nathan opted into this one check on 2026-10-12 and overrode the review cap (`review_cap`) for it alone; the record's frontmatter `override` and §P *Repair opt-in — 2026-10-12* hold his words. The rubric and the cap are the fixed text of the committed `BRIEF-PLAN-1-A.md`, §3 and §5, which bind unchanged apart from that override.

```plain text
You are REVIEWER-PLAN-DIFF-D, checking the bounded repair of MODIFICATION-20261011-gcfpe-mb008-to-promotion's PLAN
that Nathan opted into after the diff check. You did not author it, and you were not reviewer A, B or C.

This is the one check of the repair's diff that Nathan authorized beyond D26-A's cap. It is not a FULL review. The rubric
and the exit are the fixed text in the committed BRIEF-PLAN-1-A.md (same directory), section 3 (what counts as a required
finding: R1-R4) and section 5 (the cap and the exit). Read those two sections there; they bind you unchanged. No scope,
severity or exit rule is widened. Earlier reviewer records are immutable.

=== WHAT TO CHECK ===
Repository /home/user/glow-hdengine-v2. Only this diff, between commits, not the working tree or branch head:

    git diff 1fc352a 7c41120 -- \
      docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md \
      docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md \
      docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/

Read whole files at 7c41120 where the diff needs context. Canon is main at 9312add259ddcf42f98516680c3c003414949f26
(docs/pfcanon/). Read AGENTS.md first; it governs. Governing documents as listed in BRIEF-PLAN-1-A.md section 1, plus
authoritative-surfaces.md (Stale-state sweep; Restating is allowed; asserting is not; the D18 successor on Alpha state) and
PF04-Canon-HDE-Governance v2.8.7 section 9.1.6 (the Living Prompt Flow Map). Notion is read-only for you. D22 applies to
prompt bodies: no copies of a prompt body on disk beyond a transient read for one check, no hashes of bodies. Installed
skills are read-only; copy to scratch before running anything:
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/

The repaired plan's dry run: plan/dry-run.json at a50deab2, eleven gates all passing. You can rerun it or any gate: the
command is in plan/dry_run.py's docstring. It reads the fetch records of the session that runs it, so in your session
fetch the pages it needs first (the 56 page ids in plan/edits.json, the nine control page ids in plan/control_check.py,
and the candidate inventory 3f44590a05eb8110aa69fe4189ad9abc) and pass a time taken just before your fetches.
activation_render.py plan --emit prints every activation operation and the two new pages' content for your terminal; do
not write that output into the repository.

=== WHAT IS BEING REPAIRED ===
From REVIEW-PLAN-DIFF.md in the same directory, with the repair:
- P-B1-R (R2). The Flow Index's actor-map MGMT-10 row and its bindings paragraph were outside the delta. Repair: both are
  operations in activation-ops.json (FI-ACTOR-1, FI-ACTOR-2, FI-BIND-P).
- DIFF-1 (R1/R2). The register's Release rule line could not be rendered both true and passing. Repair: the activation is
  now exact anchored operations, and the register's new Current sections are written in full (REG-MEM's release rule
  carries no 091426.1 clause; the historical clause stays in the renamed Historical section); N10 renders every operation
  on the fresh reads and runs control_check on the result.
- DIFF-2 (R2). NEW_CURRENT carried unstated Current-selection passages. Repair: REG-SEL writes the new Current selection in
  full (the token as @PRODUCTION_TOKEN, a pointer instead of the Alpha paragraph, the transaction order left to the
  register entry), and no section is carried by a rule.
- DIFF-3 (R2). The registry kept a note citing a deleted key. Repair: the fetch-manifest authority row is deleted with the
  convention; registry_assemble.py check refuses a header string citing a deleted key; N9 tests it.
- Listed, opted in: L-2 and L-3 (PLAN wording), L-5 (assertions --landed with --page/--shared at X11 and X18), L-6 (marker
  wording), L-9 (X6a, the inventory writes).
activation-delta-100926.1.json is removed; activation-ops.json and activation_render.py replace it.

=== QUESTIONS TO ANSWER ===
Is each repaired finding fixed? Did the repair add a new required defect (R1-R4), above all in: the texts the activation
writes (a sentence that is false at some moment of X15-X22 or after it, a release-bound statement on an in-place control
still left unstated, a change to a dated record or to Alpha state, a statement about the selected release that the
evidence will not support); activation_render.py (an operation it would apply wrongly, a rendered page it would pass that a
reader would see as stale, a check mode that could pass on an unlanded write); the pin rule for pages the plan moves itself;
the registry changes; and the plan's new claims against the dry-run receipt. Findings the diff check listed and Nathan did
not opt into (L-1, L-7, L-10, L-11, L-12) stay listed; do not report their absence as a defect. The author's own judgement in
a recommendation is Nathan's to accept; it is a defect only if adopting it as written would silently breach a ruling.
Not exercised by the dry run: the Notion writes themselves; the duplicate and the two new pages' creation; the X6 report;
the activation markers' real values; the package build beyond the redlines, the patch and the derived profile; the D24
review; the post-flight; the promotion transaction. Questions about them are questions, not findings, unless the plan as
written would make one of them fail or go silently wrong.

=== DELIVERABLE ===
Write a new record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/REVIEW-PLAN-DIFF-2.md.
First line: the count of distinct confirmed REQUIRED findings. Then the disposition of each repaired finding (fixed, not
fixed, or fixed with a new defect); each new required finding with rubric class, exact text or step, evidence, path,
likelihood, consequence, smallest correction, and whether it is in text the repair added; each LISTED observation in one
line; the trend in the count (8, then 4). State the checks you ran and any you could not. Add a short "Canon relied on"
line (AGENTS.md). Do not edit any other file, commit, push, merge, install, write to Notion, or edit a prompt body or skill.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT. After this check the plan returns to
Nathan for approval with every open finding listed; this check does not impose a zero-finding exit.
```
