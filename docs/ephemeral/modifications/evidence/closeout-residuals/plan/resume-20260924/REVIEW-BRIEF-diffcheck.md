---
artifact_type: PLAN_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md, "ANALYZE and PLAN review brief — canonical template"
modification: MODIFICATION-20260923-closeout-residuals
mode: PLAN
kind: DIFF_CHECK
filled: 2026-09-24, by the resumed PLAN session, and committed before either reviewer was spawned
reviewers: PLAN-DC-1 (record REVIEW-diffcheck-PLAN-DC-1.md), PLAN-DC-2 (record REVIEW-diffcheck-PLAN-DC-2.md), both beside this file
---

Sections 3, 5 and 6 are the template's fixed text, copied unchanged. Only the slots were filled. The two places where
a slot reads differently for a diff check are marked *[diff check]*.

```plain text
You are <REVIEWER_ID>, reviewing PLAN of MODIFICATION-20260923-closeout-residuals. You did not author it.
[diff check] This is not a full review. It is the one check of a diff that D26-A rule 2 allows after at most two
full reviews. RESUME-PROCEDURE.md step 3.5 sets it as the only review of this resumed PLAN: the eight rounds before
D26 reviewed the content, and the recovery analysis §4.3 found that content stable since round 6. The diff under check
is the §P successor and its evidence: the change from origin/main to the commit below.

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, branch claude/exciting-cerf-uiqaj2, commit 66fd01f5014c05c9c70a590c79eaee01c8e00710. Read that commit, not the branch head.
The record: docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md, section §P, and within it only
the part from the heading "### Successor, 2026-09-24 — the plan resumed under D26" to the end of the file, plus the
front matter's `format`, `status`, `estimate` and `reviews`. The diff is `git diff d179277 66fd01f`.
Its evidence: docs/ephemeral/modifications/evidence/closeout-residuals/plan/resume-20260924/ (README.md,
dryrun-summary.json, control-edits.json). What it amends: the dated §P above it, and
docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md §9 (the X-rows) and §7.3, with the
tools under docs/ephemeral/modifications/evidence/closeout-residuals/plan/ (EV).
Its governing documents: docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md. Also read
docs/ephemeral/pe37.stage5/RESUME-PROCEDURE.md step 3.
The dry run that preceded you: resume-20260924/dryrun-summary.json. Every normal-path gate passed on main d179277
except TRACK-STATUS-01..03 (anchors gone; withdrawn by Nathan's DN-8 ruling), and ESC-25's rehearsal was not run (the
harness permission classifier refused the command).

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1  Withdrawing the machinery removes only failure-path and cross-session routing. It does not change a single
    normal-path command other than those the successor's "Changes to the dated steps" table names.
C2  The D26-B failure path, as written (four steps), can be carried out with committed tools and git commands alone,
    and its record PR to main carries only docs/ephemeral/ paths.
C3  Checkpoint 3's merge test (`git cat-file -e origin/main:<EX>/run.json`) is true only after the execution PR
    merges. Nothing else in the plan puts that file on main, including the failure record, after the rulings-note
    change.
C4  X4.5 and X5.5 run `check`, not `plan`, on GCFPE-MGMT-10-PROPOSED, and PART-11 needs no write.
C5  control-edits.json is EV/notion/edits.json less exactly nine ids, with every other entry byte-for-byte unchanged.
    Every normal-path ctrl.py call either passes it with --edits or does not depend on the withdrawn ids.
C6  The three-dot path checks at X6.4 and X7.6 fix R8-02 and admit no path outside the three open paths.
C7  fill_brief.py without --prior-file gives k = 1 and the first-round variant on the normal path, and also after a
    restart before X5.0 (checkpoint 2).
C8  The re-derived text results (X2.1, X3.4, X5.2, close) are what apply_texts.py produces on main d179277.

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
A1  Failure-path step 1 and step 2 (C2, C3). Is the git archive | tar command correct? Does the failure-record branch
    from origin/main carry a record that validates at EXECUTING with a §E the template accepts? Can the sweep's
    commands run as written, with the arguments each tool actually takes?
A2  Checkpoint 2, restarting before the first Notion write on a new branch. Check k, the brief variant,
    PRIOR_ROUND_DELIVERED and REPAIR_VERDICT_PENDING in fill_brief.py when an earlier attempt's brief and verdicts
    exist only on an unmerged branch. Check that X7.2 cannot name an earlier attempt's archive.
A3  Checkpoint 3 and the close branch. Can X7.4 to X7.7 run from a branch opened from origin/main after the merge?
    That includes the D25 line, apply_texts close, and the close-out PR's path check.
A4  The "Changes to the dated steps" table against the spec's X-rows. Does any normal-path X-row still depend on a
    withdrawn element (the sent list, the lease push, the branch rule, AT, stop lines) in a way the table does not
    replace?
A5  C5: every ctrl.py call site (X4.6, X5.0, X5.3, X5.6, X7.5, the sweep). Does `ctrl.py op` or `ctrl.py edits`
    behave the same with the default edits file for the kept ids?
A6  Anything in the successor that silently contradicts D26, D21-B or D22, or Nathan's rulings quoted in the record.
Not exercised by the dry run: every Notion write (X5.0 to X5.6, X7.5); the m2.py page creation; the D24 review and
the delivery; the install and X7.4; the whole failure path; and ESC-25.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to <RECORD_PATH>. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

*[diff check]* `<REVIEWER_ID>` and `<RECORD_PATH>` are given to each reviewer at spawn, as the front matter lists.
"The last repair" in §3 and §6 means this successor, including the rulings-note change to failure-path step 1. There
is no prior round, so §6's review-2 clause does not apply.
