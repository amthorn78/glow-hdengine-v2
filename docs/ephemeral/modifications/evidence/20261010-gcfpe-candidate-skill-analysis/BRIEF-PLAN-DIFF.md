# PLAN repair DIFF_CHECK — reviewer C

You are PLAN DIFF_CHECK reviewer C for MODIFICATION-20261010-gcfpe-candidate-skill-analysis. You did not author the plan or its repair, and you did not take part in review round 1.

This is the one bounded repair-diff check D26-A allows after FULL round 1. It is not another FULL review. The rubric and the cap are the fixed text in the committed canonical brief `BRIEF-PLAN-1-A.md`, §3 and §5; read them there. No scope, severity or exit rule is widened. The round-1 reviewer records are immutable.

**What you review.** Only the repair, from `cfa3a49637680802395f42839cd97e488c7300e9` (the commit round 1 reviewed) to `c9bdae72baec052a6d83a5f49e01c5493416f36b` in `amthorn78/glow-hdengine-v2`, branch `docs/20261010-modification-gcfpe-candidate-skill-analysis`. Use those commits, not the branch head. Between them are four commits:
- `2c9ded0c`: the round-1 review briefs. It contains no plan change.
- `80928f6f`: the round-1 records, the reviews-ledger entry and a §P note. It contains no plan change.
- `0f39f89f`: the repair.
- `c9bdae72`: the fresh-read dry-run receipt that goes with the repair.

The governing `main` baseline is `1ea6a262032c3c4de19c38c549d737d72b03ec2f`.

**The required findings being repaired.** Both reviewers found the same two. Read them in `docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/REVIEW-PLAN-1-A.md` and `REVIEW-PLAN-1-B.md`.

- **R-A1 / B-1 (R3).** X5's landing check compared each landed page, byte for byte, with the pre-edit transient read recovered from the harness records. D22 forbids that comparison and the reuse of the earlier read, yet the plan certified the check as D22-compliant. The repair takes the reviewers' author route; no D22 exception is sought.
  - `body_check.py check` uses only the read in hand, chosen by `--fetched-after`. It checks each operation by anchor counts: the replacement is present, and the old span's start and end anchors survive only where the page's replacements carry them.
  - `plan` (X2) proves that every end anchor is unique in the unedited page, and that X5's check passes on that same read with the edits applied in memory.
  - The scan never opens a saved fetch written before its cutoff, and reads a transcript only back to the cutoff.
  - G-F02-A is evaluated per sentence.
  - X5 adds a full reading of each landed page (PF04 §9.1.6). §8 lists a stray change outside the spans as P2-7.
  - §3 point 5, §12 and the record's §P *Checks* bullet are reworded.
- **R-A2 / B-2 (R1).** X6 closed the record before X7 and X8 ran. Now:
  - X6 is a checkpoint that leaves the record `EXECUTING`;
  - X7 writes the tracking lines W9 and W10;
  - X8 updates the PR body;
  - X9 closes the record, then marks PR #600 ready for review and checks the head;
  - W9 links the record by its path and PR #600, not by a commit;
  - §6 gains a case for a failure at X6 to X9, where PART-01 stays landed.

**Not repaired.** The LISTED findings L-A1 to L-A14 and L-B1 to L-B19 were not repaired without an opt-in. That includes the §3 point 3 erratum (L-B13). §8 now lists all of them by reference.

**What to attack.** Check whether each required finding is fixed without introducing a new required defect.
1. Does any mode of `body_check.py` still compare two reads of a body, reuse an earlier read for a later check, or open a saved read written before its cutoff (D22 conditions 2 to 4; `prompt-corpus-policy.md`)?
2. Can the anchor-count landing pass a wrong edit, or fail a correct one, on the live pages? Consider:
   - an operation whose start anchor also occurs in its replacement (IA30-1, PE-1);
   - end anchors repeated by other replacements on the same page;
   - a partial `update_content` batch.
3. Can `--fetched-after` select a stale or foreign read? Consider whether the time format matches the harness timestamps, the newest-first transcript scan stopping early, and subagent records.
4. Do X6 to X9 now run without interpretation? Is the failure path consistent for every step?
5. Is the W9 text accurate? Are the §4 expected values (build, parts manifest, derivation, guards `62245446…`) reproducible on the committed code?
6. What the dry run did not exercise: no Notion write, so X4 and X7 are untested against Notion's own rendering.

**How to check, read-only.**
- Take a time T with `date -u +%Y-%m-%dT%H:%M:%S.000Z` before any fetch.
- Read the eight pages fresh with the Notion fetch tool. PLAN-SUCCESSOR-2 §2 lists their IDs.
- Run `PYTHONDONTWRITEBYTECODE=1 python3 <path>/body_check.py plan --fetched-after T`. Read its output in your session only (D22): never redirect, hash or cache it, and never quote a whole body.
- You may run `dry_run.py <skills-root> <your-scratch-dir> 600 T`. The skills root is `/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502`; never write there. Your scratch directory is `/tmp/claude-0/-home-user-glow-hdengine-v2/de11ca17-0aff-5fef-9790-e19ef40c79e6/scratchpad/review-c/`.
- AGENTS.md's canon-first rule applies. Search `docs/pfcanon/` on `origin/main` for the terms you rely on, read the governing sections in full, and list them in your record under a heading "Canon relied on".

**Deliverable.** Write a new record to `docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/REVIEW-PLAN-DIFF.md`. Keep the canonical deliverable shape:
- The first line states the count of distinct confirmed REQUIRED findings.
- Give the disposition of R-A1 / B-1 and of R-A2 / B-2: fixed, not fixed, or fixed with a new defect.
- Give any new required defect, with its rubric class, path, likelihood and consequence, and whether it sits in text the repair added.
- Give the trend in the count and any listed observation.
- State the checks you actually ran, and their limits.
- Close with DECISION NEEDED, NOTHING NEEDED or IN FLIGHT.

Do not edit any other file. Do not commit, publish, merge, install, write to Notion or edit prompt bodies.

After this DIFF_CHECK the plan returns to Nathan with any open findings. This check does not impose a zero-finding exit.
