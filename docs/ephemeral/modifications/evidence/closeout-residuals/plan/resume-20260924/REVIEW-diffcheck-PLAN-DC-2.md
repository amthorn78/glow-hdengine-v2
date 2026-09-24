2 distinct confirmed REQUIRED findings

# PLAN-DC-2 — diff check of PLAN, MODIFICATION-20260923-closeout-residuals

- **Reviewer:** PLAN-DC-2, a fresh subagent with no part in authoring the plan. Record written 2026-09-24.
- **Brief:** `REVIEW-BRIEF-diffcheck.md` at `217068c` (blob `3ea5a3c7`, 7 863 B), read in full.
- **Reviewed:** commit `66fd01f5014c05c9c70a590c79eaee01c8e00710`, `git diff d179277 66fd01f`: the §P successor, the front matter's
  `format`, `status`, `estimate` and `reviews`, and `resume-20260924/` (README, dry-run summary, control edits).
- **How:** read against the spec's §9 and §7.3, the EV tools, D20 to D26, the template, the validator and
  RESUME-PROCEDURE.md. Every mechanical claim below was re-run in a scratch clone (`scratchpad/dc2/`) of the local
  repository. Nothing was fetched.

## REQUIRED

### DC2-01 — R3, also R4: a restart before X5.0 re-rolls a D24 rejection, and nothing can see it

- **Path:** failure, then restart (checkpoint 2, before the first external write).
- **Likelihood:** low.
- **Consequence:** silent. A rejected package set is delivered and installed without its rejection ever being repaired
  or returned to Nathan.
- **In text the last repair added:** yes (checkpoint 2 and the X4.4 row).

**The text.**

- Checkpoint 2 (record lines 1032–1035): "A session lost or stopped before X5.0's Notion call is followed by a new
  session that restarts EXECUTE at X0.2 on a new branch … The earlier branch stays unmerged, for Nathan to delete.
  X1 to X4 run again in full, including X4.3's packaging and a fresh D24 round."
- Row 11, X4.4 (line 1058): "`fill_brief.py EX/packages.json --write` only. It prints `k` = 1, because no
  `REVIEWER-PROMPT-cr*.md` exists yet in the closeout-residuals evidence directory on `main`."

**Evidence.**

- **The guard is blind after a restart.** `EV/skills/fill_brief.py` (lines 62–88) looks for earlier briefs only in
  the working tree: the closeout-residuals directory and its `attempt-*/`. Finding none, it uses the first variant.
  `REPAIR_VERDICT_PENDING` and `PRIOR_ROUND_DELIVERED` can fire only when an earlier brief is in the working tree.
  A branch cut from `main` never has one. So after a restart, the one mechanical guard behind "not re-rolled" cannot
  fire.
- **Reproduced** in the scratch clone. Attempt 1 is on `docs/20260925-closeout-residuals-execute`, holding
  `REVIEWER-PROMPT-cr1.md` and a `SECTION-10-REVIEW-cr1-SFR-CR1-1.md` that reads `SKILL_REPAIR_REQUIRED`.
  - A re-cut on that same branch exits 1: `{"refused": "REPAIR_VERDICT_PENDING", …}`.
  - The checkpoint-2 restart on `…-execute-2`, cut from `d179277`, exits 0 with `k` 1. Its brief says "NONE for these
    bytes: this is the first review of this Modification's packages" and "NONE, first review."
- **The new round reviews the same content.** X4.3's re-cut changes only the archive sha256s: they vary with file
  mtimes, as the dry-run summary's X4.3 note says. The freeze digests are fixed by `expected_after_patch.txt`. So the
  "fresh" round re-reviews the rejected bytes.
- **The rulings it breaches:**
  - D24 condition 5, which D26 keeps (decision record, D26, *What it supersedes*): "A `SKILL_REPAIR_REQUIRED`
    finding is still repaired and re-reviewed by fresh reviewers on the new bytes, within D26-A rule 2's cap".
  - RESUME-PROCEDURE.md step 5.1: "`SKILL_REPAIR_REQUIRED` returns to Nathan. It is not re-rolled (`D26-A` rule 2)".
  - The successor itself (line 990): "It is returned to Nathan and not re-rolled".
- **The RCA already classed this path** (all in `rca-20260924/`):
  - R8-03, "rejection re-rolled on same bytes", is classed as a "silent D24 condition 5 breach"
    (`defects-r4-r8-path-consequence.csv`).
  - R5-03 is listed as a requirement any stop-and-return design still has to meet: "the D24 verdicts must survive
    the next X0.2 reset" (`process-review.json`, around line 900).
  - The same file calls a D24 rejection "the plan's likeliest failure" (around line 882).

**How it happens.**

1. X4.4 commits and pushes each verdict as it returns.
2. A rejection stops EXECUTE only once the session has written the §E row and returned.
3. A session lost between the verdict's push and that return leaves the rejection on the branch, and nothing reaches
   Nathan.
4. The next session follows checkpoint 2: a new branch, a fresh round, and a brief saying no review came before.
5. If both new reviewers confirm, the archives are delivered and installed at X7.3. The rejecting verdict survives
   only on a branch the plan leaves "for Nathan to delete".

Checkpoint 2's "or stopped" also prescribes the same restart after a stop that did reach Nathan. The failure path's
first bullet says his ruling comes next instead: end the Modification, or a plan change.

**Smallest correction, in checkpoint 2:**

1. Change "lost or stopped" to "lost".
2. Add a check before X0.2. Run `git fetch origin`. Then, for each `origin/docs/*-closeout-residuals-execute*`
   branch, run
   `git grep -l SKILL_REPAIR_REQUIRED <branch> -- 'docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr*'`.
   Any output means no restart: return to Nathan as the stop before the first external write.

Grep only the verdict files, because the brief itself contains the word once. In the scratch clone this command
lists the rejecting verdict.

### DC2-02 — R1: the normal path ends with a close-out PR that says not to merge it

- **Path:** normal.
- **Likelihood:** certain, on the text as written.
- **Consequence:** X7.8 stalls, or Nathan has to override the PR's own instruction. No page or document is edited
  wrongly.
- **In text the last repair added:** yes. The successor's row 28 withdrew X7.7 and left X7.6's dependent sentence
  standing. The sentence itself is the spec's, unchanged.

**The text.**

- Spec §9, X7.6 (line 6274): "Commits (`closeout-residuals X7.6: close`), pushes, and opens the close-out PR, its
  body saying not to merge it before X7.7's commit."
- Successor row 28 (line 1069): "X7.7 | Under DN-8 (A), **withdrawn**".
- The rulings note (line 1192): "dated step 28 does not run".
- The table's lead-in (line 1051): "Nothing else in a step moves."
- Row 27 changes only X7.6's path check and its text results.

**Evidence.**

- X7.7 was also the normal path's final "Returns to Nathan" (line 6275), and the step that wrote step 28's §E
  disposition ("this is step 28's disposition"). With X7.7 withdrawn, X7.6 does neither.
- Template rule 5: "A skipped step is a recorded disposition, never an omission."
- The successor's own Product Owner actions say "merge the close-out PR" with no condition, which the PR body
  contradicts.

**Consequence.** Every successful run ends the same way:

- a close-out PR whose body forbids merging it until a commit that never comes;
- no return to Nathan after X7.6;
- no §E disposition for step 28.

Until that PR merges, `COMPLETE`, the `D25 applies from:` line and the three close texts stay off `main`.

**Smallest correction, in row 27:** "X7.6 opens the close-out PR without the X7.7 sentence, records step 28 in §E
as withdrawn under DN-8 (A), and returns to Nathan for X7.8."

## LISTED

Each line gives: path; likelihood; consequence; in text the last repair added.

- L1 — Failure step 2 runs `ctrl.py all --run EX/run.json …` on the failure branch, where the rulings-note change left no `EX/run.json` (it is copied to `failure/execute/`); reproduced on a simulated failure branch: `FileNotFoundError`, exit 1; fix: `--run docs/ephemeral/modifications/evidence/closeout-residuals/failure/execute/run.json`. [failure; certain whenever step 2 runs; loud, but the obvious workaround (restoring `EX/run.json` at its own path and committing it on the same PR) recreates the checkpoint-3 false positive the rulings note removed; yes]
- L2 — Failure step 1's `git checkout -B … origin/main` carries uncommitted tracked edits and untracked `EX` files onto the failure branch (reproduced: an uncommitted `notion-write-boundary.md` edit and an `EX/landing/` file both carried over, checkout exit 0), and the step names no staging scope or staged-path check where the dated stop record had "`git add` the record and `AT` only; `git diff --cached --name-only` lists nothing else"; "It carries no registry, graph, skill-text or rule change" is stated, not checked. [failure; low: needs a failure inside X5.2's write-to-commit window plus broad staging; a half-applied governed document or EX-path files in a PR Nathan is told to merge; yes]
- L3 — Failure step 1 copies the failing step's "output, copied from `$SCRATCH` into `failure/`" without the dated qualifier "(the refusal or check JSON: counts and ids, no body text)"; a `land.py plan` output, whose `ops` carry prompt-body lines, copied as that output would commit body text. [failure; low; a D22 breach in a PR to main; yes]
- L4 — The failure record sets `EXECUTING` and step rows, but does not record the failing part(s) `BLOCKED` with their applied steps named (template rule 6, D26-B), does not cite the sweep from §E, and does not disclose the sweep's harness files (D22 condition 5); the validator checks none of these at `EXECUTING`. [failure; certain if followed literally; record completeness; yes]
- L5 — The window from X5.0's execute-date commit to its Notion call is claimed by checkpoint 2 (restart), by the lost-session bullet (failure path, keyed on `execute_date_X5.0` "on the pushed execution branch", with no rule for choosing among `-execute-<n>` branches), and for a failing gate by both "Before it" (main unchanged) and the unamended X5.0 row ("a stop past X5.0"); X5.0's pre-write test reads `TOKEN_NOT_RECORDED` before any landed test, so a restart on a fresh `run.json` cannot see an earlier attempt's freeze line and would write a second, differently dated one. [failure/restart; very low; usually a loud, conservative return, at worst a silent duplicate tracking-page line; yes]
- L6 — After a checkpoint-2 restart that follows a delivery, X4.4's delivery message cannot name the earlier delivery as superseded (it looks in `attempt-*/` and this branch's `git log`), so Nathan holds two "cr1" sets; X7.2 names archives by sha256 and X7.4 compares freeze digests, which are equal across attempts. [restart; low; confusion only; yes]
- L7 — A stop before X5.0 does not tell Nathan that archives already delivered at X4.4 must not be installed (the dated stop record's step 4 did); X4.4's own message says to install at X7.3 and not before, and X7.4's digest comparison catches a wrong install. [failure; low; loud; yes]
- L8 — Post-merge routing gaps: X7.2's failure record is "made on a branch opened from `origin/main`", but checkpoint 3 names only the close branch opened at X7.4; and "After X7.4 has committed, it continues on the close branch" gives no test for that state or for finding the branch. [failure, post-merge; low; loud; yes]
- L9 — C1 is overstated: superseding *Commits and pushes* and *The landing unit* also drops two normal-path rules the table does not name, "A step commits only its own paths, and only when `git status --porcelain -- <paths>` prints something" and the forward-repair bound "Any refusal, or a second failing `check`, cannot be repaired forward", while X5.4's gate still cites "the landing-unit rule above". [normal; certain; small: an empty commit on a re-run errors loudly, and forward repair is unbounded but apply-once; yes]
- L10 — Checkpoint 1 states its gate after `mkdir -p EX` and `runjson.py EX/run.json base …`; read in that order, `git status --porcelain` shows the new untracked `EX/` and the gate fails (the spec's X0.2 row says "After the reset"). [normal; low, a misreading; a loud stop before any write; yes]
- L11 — C6: `git diff --name-only origin/main...HEAD` reports only the destination of a rename (reproduced: a move from `scripts/` into `docs/ephemeral/` lists only the new path; `--no-renames` lists both), so a rename from outside the three paths into them would pass; the plan makes none. [normal; very low; an outside deletion admitted; yes]
- L12 — Format 2.1: X4.4's D24 round is a `SKILL` review round, which template rule 8 puts in the `reviews` ledger, but no X-row says to enter it. [normal; certain; record completeness, and the validator does not require it; yes]
- L13 — The filled D24 brief's header cites `reviewer-prompt-template.md v1.1` (from `fill_brief.py`); the file is 1.2 since #481, whose change added an introduction and the second template and left the skill template's block unchanged. [normal; certain; cosmetic; no]

## The claims, checked

- **C1: partly true.** No normal-path command changes beyond the table and checkpoints 1 and 3. Two normal-path rules
  go with the superseded paragraphs (L9).
- **C2: not as written.**
  - What holds: the `git archive | tar --strip-components=5` copy is correct. Reproduced: `failure/execute/` receives
    `run.json`, `ctrl/` and `landing/`, and both stages exit 0. A record cut from `main` with `status: EXECUTING` and
    a §E validates (`modification_validate.py` exit 0).
  - What fails: step 2's `--run` names a missing file (L1), and the PR's paths depend on staging the step does not
    fix (L2).
- **C3: true.** `failure/execute/run.json` is a different path from checkpoint 3's `…/execute/run.json`, and no other
  step puts `EX` on `main` before the execution PR merges. The caveat is L1's workaround.
- **C4: true on the committed dry-run evidence.** `check` exits 0 with `R-ITEM40` 0 and `R-ITEM23-gate` 0, `state`
  reads `LANDED`, and `plan` refuses `ALREADY_LANDED`. Not re-fetched here.
- **C5: true.**
  - Exactly the nine named ids are removed.
  - The file equals `json.dumps(<the 15 kept entries of edits.json>, indent=1, ensure_ascii=False) + "\n"`, which is
    how `edits.json` itself is serialized. So each kept entry is byte-identical, and the order is kept. The sha256 is
    `72889b24…`, as stated.
  - `ctrl.py edits` and `op` read only the named entry. Only `all --expect unlanded` depends on the file, and X4.6
    passes it `--edits`. The sweep also passes it.
- **C6: true.** The three-dot form fixes R8-02, with L11's rename caveat.
- **C7: true, mechanically (reproduced).** This is the cause of DC2-01.
- **C8: true.** Reproduced on a clean worktree of `d179277`:

  | label | file | sha256 | bytes |
  |---|---|---|---|
  | X2.2 | `gcfpe.decision-record.md` | `c8cdfd5a…` | 111 107 |
  | X3.5 | `session-working-rules.md` | `2501579e…` | 16 113 |
  | X5.2, stand-in URL | `notion-write-boundary.md` | `8fde58f2…` | 11 865 |
  | close, 2026-01-01 and the expected freeze lines | `gcfpe.decision-record.md` | `b324490a…` | 113 065 |
  | close | `prompt-body-content-policy.md` | `c24061b8…` | 7 125 |
  | close | `REVIEWER-PROMPT-a5.md` | `9e2d822c…` | 19 234 |

  A re-run of each label applies nothing.

## The attack points

- **A1** — Step 1's copy is correct and its record validates. Step 2 fails as written (L1). Staging is unguarded
  (L2, L3).
- **A2** — `k` is 1 and the variant is the first. Neither `PRIOR_ROUND_DELIVERED` nor `REPAIR_VERDICT_PENDING` can
  fire (DC2-01). X7.2 cannot name an earlier attempt's archive: it names archives by the `EX/packages.json` on
  `main`, which only the merged attempt's branch can put there.
- **A3** — X7.4 to X7.7 can run on a close branch cut from `main` after the merge. By then `EX/run.json`,
  `EX/packages.json` and `control-edits.json` are all on `main`. `run_gate.py` creates `--out` itself, and
  `apply_texts.py close` reproduces. The `D25` line and the three-dot check work there. The one failure is X7.6's PR
  body (DC2-02).
- **A4** — Covered by DC2-02 and L9; the sent list, lease, branch rule and `AT` are otherwise replaced.
- **A5** — C5 holds.
- **A6** — DC2-01 (D24 and D26-A rule 2), L3 and L4 (D22, D26-B). The D21-B tension before the first write is
  already listed as OF-3; after the first write, D26-B governs.

## Not exercised

Nothing was read from or written to Notion, Drive or GitHub. No Notion page was fetched, so no harness file from this
review holds a prompt body. C4 and the anchor checks rest on the committed dry-run evidence. Not run: every Notion
write, `m2.py`, the D24 review, the delivery, the install, X7.4, ESC-25, and the live sweep.

There is no prior round, so §6's review-2 clause does not apply. Both REQUIRED findings, and 12 of the 13 LISTED
findings, sit in text the last repair added. This check is the last one the cap allows (§5), so the output goes to
Nathan with every finding above open.

DECISION NEEDED
