2 distinct confirmed REQUIRED findings

# closeout-residuals PLAN diff check: PLAN-DC-1

Reviewer: PLAN-DC-1, a fresh-context subagent. My only brief is
`docs/ephemeral/modifications/evidence/closeout-residuals/plan/resume-20260924/REVIEW-BRIEF-diffcheck.md` at
`217068c` (102 lines, 7 863 B, sha256 `b5ab8126…`). Under review: `git diff d179277 66fd01f`, read at `66fd01f`,
not the branch head. That covers the §P successor (record lines 942–1203), the front matter's `format`, `status`,
`estimate` and `reviews`, and `resume-20260924/` (`README.md`, `dryrun-summary.json`, `control-edits.json`). I made
no Notion, Drive or GitHub read or write, fetched no prompt body, and did not open the other reviewer's record. Every
`land.py` and `ctrl.py` run below used an empty `--harness-root`, so no harness file was read (`D22`).

**Answer.** The successor mostly does what it claims. I reproduced C3, C4, C5 and C8, and each holds. C6 holds for
R8-02. C1 holds with one small gap. C2 does not hold as written. I found two required defects, both in the
successor's own text:

- **REQ-1 (R3, also R4).** Checkpoint 2 restarts EXECUTE on a new branch after a session is lost before X5.0, with
  a fresh D24 round. If the lost session had already committed a `SKILL_REPAIR_REQUIRED` verdict, nothing on the
  new branch can see it. `fill_brief.py` writes a first-round brief ("NONE, first review."), and the rejection is
  re-rolled on unrepaired content without ever reaching Nathan. The dated route caught this case. The successor
  withdrew that route and put nothing in its place.
- **REQ-2 (R1).** Withdrawing X7.7 leaves X7.6 telling Nathan, in the close-out PR's body, not to merge before
  X7.7's commit, which never comes. The run also loses its last return to Nathan.

Each has a one-sentence correction, given below. The most useful LISTED point is L1: failure-path step 2 still
passes `--run EX/run.json`, and since the rulings-note change there is no such file on the failure branch.

## What I reproduced

Everything below ran read-only, on `git archive` extracts of `66fd01f` and `d179277` in my scratchpad, with
`PYTHONDONTWRITEBYTECODE=1`.

- **Validator.** `modification_validate.py` passes the record at `66fd01f` (1/1, `PLANNING`), and `--selftest` gives
  64/64. I made two scratch copies of the record. One is set to `PLANNED` with `plan_approved_by` filled, as
  `main` will be after approval, and it passes. The other is that copy set to `EXECUTING`, with a §E of step rows
  only (the failure record), and it passes too. The validator checks no §E before `COMPLETE`.
- **`control-edits.json` (C5).** 15 entries. They are `EV/notion/edits.json`'s 24 less exactly `PART-11-TRACK-01`,
  `TRACK-STATUS-01` to `03`, `TRACK-UNIT-STOPPED`, `TRACK-STATUS-STOP-01` to `03` and `TRACK-FREEZE-LIFT-STOP`, in
  the same order. Each kept entry's serialized bytes occur in both files. The sha256 is `72889b24…`, as the table
  says.
- **`ctrl.py` (A5).** `edits` and `op` look each id up in the file, then work from that entry, the page and
  `run.json` alone. So for the 15 kept ids, the default file and `control-edits.json` behave the same. Only `all`
  walks the whole file, and X4.6 and the sweep both pass `--edits`. With `--edits control-edits.json`, a stray call
  for a withdrawn id fails with `UNKNOWN_EDIT`. `m2.py` uses only ctrl's child-page regex.
- **Texts (C8).** I ran `apply_texts.py` on a copy of `d179277`, labels in order:
  - X2.2: `c8cdfd5a…`, 111 107 B;
  - X3.5: `2501579e…`, 16 113 B;
  - X5.2, with the all-zero stand-in URL: `8fde58f2…`, 11 865 B;
  - close, with 2026-01-01 and the expected freeze lines: `b324490a…` (113 065 B), `c24061b8…` (7 125 B) and
    `9e2d822c…` (19 234 B).

  A second run of each label applied nothing.
- **Git, in a scratch simulation** (a bare origin and a clone, with the `66fd01f` tree as `main` and squash merges):
  - failure step 1's `git archive … | tar -x --strip-components=5` puts committed `EX` at `failure/execute/`. The
    failure branch has no `EX/run.json`;
  - after a failure record's squash merge, checkpoint 3's `git cat-file -e` exits 128. After an execution
    branch's squash merge it exits 0, and `git log -1 origin/main -- …/execute/run.json` finds the merge commit
    that the D25 line needs;
  - on a close branch opened from `origin/main` after that merge, `runjson.py` recorded `install_date` and
    `close_date`, `apply_texts.py … close` applied, and the three-dot check listed only open paths (A3);
  - with `main` moved outside the open paths during EXECUTE, the two-dot diff lists `README.md` and the three-dot
    diff does not (R8-02).
- **Dry-run evidence (C4).** `dryrun-summary.json` matches the successor's dry-run table. For
  `GCFPE-MGMT-10-PROPOSED`, `check` passes with `R-ITEM40` 0 and `R-ITEM23-gate` 0, `plan` refuses `ALREADY_LANDED`,
  and `state` reads `LANDED`.

## The claims

| claim | verdict |
|---|---|
| C1 | Holds for every Notion and body command. One normal-path guard goes with the superseded preamble without a table row (L10). The new push command and branch name are in checkpoint 1, not the table |
| C2 | Not as written. Step 2's `ctrl.py all --run EX/run.json` fails on the failure branch (L1). Step 1's `git archive` needs `origin/<branch>` in a fresh clone (L2). Opening the PR needs the GitHub tools, not git. With those fixed, the four steps run on committed tools. The PR carries only `docs/ephemeral/` paths if staged narrowly, and nothing checks that (L3) |
| C3 | Holds (simulated). One gap sits outside the text: nothing names the branch that a before-X5.0 ruling or a plan change is written on. If one were made from the execution branch, it would carry `EX/run.json` to `main`, and X0.2's `runjson.py … base` would then keep the stale base (`"kept": true`) |
| C4 | Holds |
| C5 | Holds |
| C6 | Holds. One limit: `--name-only` reports a rename by its destination only, so a rename into the open paths from outside would pass. No step makes one |
| C7 | Holds. It is also how REQ-1 happens: after a restart, `k` = 1 and the first-round variant hide the earlier round |
| C8 | Holds |

## REQUIRED

### REQ-1: R3 (a silent breach of a Product Owner ruling), also R4

**The text.** Checkpoint 2 (record lines 1032–1037): "A session lost or stopped before X5.0's Notion call is
followed by a new session that restarts EXECUTE at X0.2 on a new branch … X1 to X4 run again in full, including
X4.3's packaging and a fresh D24 round." It works together with the table's X4.4 row (line 1058): "`--prior-file`
and the new-session resume (P-109) are withdrawn."

**The evidence.**

- **Where the verdict ends up.** Spec X4.4 (line 6240) commits and pushes each verdict "unedited as it returns".
  Suppose a session commits a `SKILL_REPAIR_REQUIRED` verdict and is lost before it returns it. The rejection then
  exists only on that session's pushed branch, and checkpoint 2 leaves that branch unmerged.
- **Why `fill_brief.py` cannot see it.** It counts briefs only in the working tree (lines 62–64). It tests
  `REPAIR_VERDICT_PENDING` only when the newest brief is already in that directory (lines 74–84). A branch made
  from `main` has neither.
- **Reproduced in the scratch simulation.** The lost attempt's branch holds `REVIEWER-PROMPT-cr1.md` and
  `SECTION-10-REVIEW-cr1-SFR-CR1-1.md` reading `SKILL_REPAIR_REQUIRED`, committed and pushed.
  - On that branch, `fill_brief.py` refuses with `REPAIR_VERDICT_PENDING` (exit 1). That is the dated route.
  - On a restart branch made by checkpoint 1's commands, it exits 0. It gives `k` = 1 and `round: cr1`, with the
    PRIOR text "NONE for these bytes: this is the first review of this Modification's packages" and the REREVIEW
    text "NONE, first review."
  - The verdict is still one `git grep` away on the lost branch.
- **The rulings it breaches.**
  - D24 condition 5: "Any `SKILL_REPAIR_REQUIRED` finding is repaired and re-reviewed by fresh reviewers on the new
    bytes."
  - The successor's own rule (line 990): "It is returned to Nathan and not re-rolled (`D26-A` rule 2)".
    RESUME-PROCEDURE step 5.1 says the same.
  - "or stopped" in checkpoint 2 also conflicts with *Before it* (lines 986–992), which sends a stop to Nathan's
    ruling, not to a restart.

**Path, likelihood, consequence.**

- **Path:** failure (a session lost at X4.4), leading back onto the normal path.
- **Likelihood:** low.
- **Consequence:** silent. Packages that a reviewer rejected go to fresh reviewers unrepaired, as a first review.
  If the fresh pair confirms them, they are delivered, the bodies land and the packages are installed. Nathan never
  sees the rejection.

**The smallest correction.** In checkpoint 2, write "lost" for "lost or stopped", since a stop follows *Before
it*. Then add: before X0.2, the new session runs
`git grep -l SKILL_REPAIR_REQUIRED origin/<lost attempt's branch> -- 'docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr*'`.
A hit is the X4.4 stop: the session returns `IMPLEMENTATION_BLOCKED` to Nathan with that verdict, and does not
restart.

**In text the last repair added:** yes. Checkpoint 2 and the X4.4 row replace the dated same-branch route (P-109),
which is where the refusal fired.

### REQ-2: R1 (a defect on the normal success path)

**The text.**

- The table's X7.7 row (line 1069): "Under DN-8 (A), **withdrawn**".
- The rulings note (line 1192): "dated step 28 does not run".
- The table's own rule (line 1051): "The dated §P steps and spec §9 rows stand, with these changes. Nothing else in
  a step moves."
- The table's X7.6 row (line 1068) changes only the path check and the text results.

**The evidence.** Spec X7.6 (line 6274) still "opens the close-out PR, its body saying not to merge it before X7.7's
commit", and it has no return to Nathan. X7.7 (line 6275) held the run's final "Returns to Nathan" and "this is step
28's disposition". The dated Product Owner actions (line 895) say "Merge the close-out PR after step 28."

**Path, likelihood, consequence.**

- **Path:** normal.
- **Likelihood:** certain on a literal run.
- **Consequence:** the close-out PR tells Nathan not to merge before a commit that never comes, while the
  successor's own action list tells him to merge it. The run ends at X7.6 with no return to Nathan, and §E gets no
  disposition for step 28 (template rule 5). Nothing is written wrong, and a session that notices can work around
  it. But the template requires a normal path that runs with no interpretation.

**The smallest correction.** Add to the X7.7 row: "X7.6's PR body drops 'not to merge it before X7.7's commit';
X7.6 records dated step 28 in §E as withdrawn (DN-8 (A)) and returns to Nathan."

**In text the last repair added:** yes.

## LISTED

One entry each, with its path, likelihood and consequence, and whether the last repair added it.

- **L1.** Failure step 2 passes `--run EX/run.json`, but step 1 now extracts `EX` to `failure/execute/`, so the
  failure branch has no `EX/run.json`. The run fails with `FileNotFoundError`: exit 1 and empty stdout, the same
  exit code that a `MIXED` or `DOUBLED` sweep gives. `--run …/failure/execute/run.json` runs. Failure; certain
  once taken; loud; last repair: yes (the rulings-note change stopped short of step 2).
- **L2.** Failure step 1's `git archive <execution branch>` fails in a fresh clone, which is what a new session
  after a loss has. Git reports "not a valid object name", tar reports "does not look like a tar archive", and the
  pipeline exits 2. `origin/<branch>` works. Failure; likely in that case; loud; yes.
- **L3.** `git archive` copies committed `EX` only. So the failing step's uncommitted `EX` outputs (for example
  the X5.4 summaries since the last ten-page commit) miss `failure/execute/`, and they survive the checkout as
  untracked files at `EX`'s own path. An uncommitted edit to a file both branches share is carried over too, such
  as X5.2's `notion-write-boundary.md` between its write and its commit (simulated). Step 1 names no paths to stage
  and has no staged-set check, which the dated stop record had (`git diff --cached --name-only`). A broad
  `git add -A` would therefore put these files in a PR described as carrying no rule change. Failure; low; an
  evidence gap, or unannounced rule text on `main`; yes.
- **L4.** Step 1 copies the failing step's "output" without the dated limit "counts and ids, no body text". A
  failing X5.4 `plan` (a non-empty `reapply_unsafe`) prints `ops` that quote body lines, and those would then be
  merged to `main`. This is a `D22` grey zone: task evidence, or a committed body. Failure; low; yes.
- **L5.** Step 4 names to Nathan only the bodies reading `LANDED` or `PARTIAL` and the control edits reading
  `LANDED`. A control edit that the sweep reads `DOUBLED` or `MIXED` is recorded only in `failure/sweep.json`, and
  it can outlast his restoration. The dated list named both states. Failure; low; a stray control-page line; yes.
- **L6.** The failure record's §E has step rows, but no part or item is recorded `BLOCKED` "with its applied steps
  named" (`D26-B`, template rules 5 and 6). Nothing checks §E before `COMPLETE`. Failure; certain once taken; record
  completeness; yes.
- **L7.** The lost-session test ("`execute_date_X5.0` … and no execution PR merged") also matches a session lost
  after X6.4 opened the PR and before Nathan merged it. A new session started in that window would take the failure
  path and ask Nathan to restore 50 correctly landed bodies. Testing for "no execution PR open" fixes it. Failure;
  low; loud but misleading; yes.
- **L8.** X5.0's dated gate still stands: "From that commit on, a failure is a stop past X5.0". *Before it* puts the
  boundary at the Notion call instead. So a failure between the execute-date commit and the call has two routes.
  Failure; low; loud either way; yes.
- **L9.** Checkpoint 1 restates X0.2's gate without the dated "After the reset". Checked after `runjson.py`, the
  gate fails on `?? …/execute/` (simulated). The dated row still holds the timing. Normal; low; loud; yes.
- **L10.** "Everything else in the preamble is superseded" also drops *Commits and pushes*' rule that a step
  commits only its own paths, and only when `git status --porcelain -- <paths>` prints something. The table names no
  replacement (C1). So an in-session re-run meets `git commit`'s "nothing to commit", with exit 1. Normal; low;
  loud; yes.
- **L11.** After a D24 rejection and a plan change by Nathan, the restarted X4.4 gets `k` = 1 and "NONE, first
  review.", so the re-review is not told which findings were repaired. The withdrawn `--prior-file` route did that,
  so the plan change must restate it. Failure, then a plan change; low; Nathan approves that plan; yes.
- **L12.** A restart's X4.4 delivery names no earlier delivery it supersedes, because its list reads only
  `attempt-*/` and this branch's `git log`. Nathan then holds two unmarked cr1 sets. X7.2 names archives by sha256,
  and X7.4's freeze-digest check makes the void set harmless, since its content is the same. Failure; low;
  confusion only; yes.
- **L13.** A second failure record (after a plan change) extracts into the `failure/execute/` already on `main`, so
  it mixes two attempts' `EX` files: tar overwrites the shared paths and keeps the rest. Failure; low; evidence
  clutter; yes.
- **L14.** The failure-path return does not carry `D22` condition 5's harness-file disclosure for the sweep's 50
  body fetches. X6.4 and X7.6 carry it on the normal path, and `D22` binds the session regardless. Failure; low;
  yes.
- **L15.** Step 1 says "checkpoint 3's test stays true". It means the test stays false until the execution PR
  merges, which is C3's point. Wording only; yes.
- **L16.** The `reviews` ledger's `DRY_RUN` outcome still says stage 5 removed the tracking-page anchors. Nathan
  corrected that, and the correction appears only in the body. Documentation; certain; yes.

## Trend and the cap

There is no prior round, so §6's review-2 clause and the halving test do not apply. Every finding here, 2 REQUIRED
and 16 LISTED, sits in text the last repair added. That is expected for a check scoped to that repair's diff, and it
is also `D26-A` rule 5's signal to return to Nathan. This is the one diff check, so the cap is reached. The output
goes to Nathan with every open finding listed, and LISTED findings are not repaired unless he opts in.

DECISION NEEDED: Nathan decides whether REQ-1 and REQ-2 (one sentence each) are repaired before he approves the
plan, or accepted as listed risks, and whether to opt in to any LISTED finding. L1 is the cheapest, and I would take
it with them.
