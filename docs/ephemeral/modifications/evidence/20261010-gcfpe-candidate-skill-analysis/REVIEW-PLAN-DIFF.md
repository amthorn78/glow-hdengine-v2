Distinct confirmed REQUIRED findings: 0

# PLAN DIFF_CHECK — reviewer C — MODIFICATION-20261010-gcfpe-candidate-skill-analysis

**Both round-1 required findings are fixed, and the repair adds no required defect. The count falls from 2 to 0. Seven listed observations remain, and none of them needs a repair round.**

- **R-A1 / B-1 (R3): fixed.** `check` now uses only the post-write read that `--fetched-after` selects, and judges each operation by anchor counts against the committed `edits.json`. No mode of `body_check.py` compares two reads to decide anything, reuses X2's read, or opens a saved fetch file written before its cutoff. I simulated landings in memory on my own fresh reads of the eight pages. A correct landing passed on all eight. Every incomplete batch, duplicated replacement, kept old span and shortened replacement failed.
- **R-A2 / B-2 (R1): fixed.** X6 records X0–X5 and leaves the record `EXECUTING`. X7 and X8 run next. Only X9 sets `COMPLETE`, then marks PR #600 ready. §6 has a case for X6–X9 in which PART-01 stays landed. The validator passes scratch copies of the record at both the X6 and X9 states.
- **What the repair leaves open (listed):**
  - **L-C1.** The anchor counts cannot see an `old_str` shortened by less than an anchor's length. Only X5's full reading catches the fragment that cut leaves, yet §3 point 5 says such a cut "fails".
  - **L-C2.** W9 says "EXECUTE complete" at X7, before X8 and X9 run.

I reviewed only the repair, from `cfa3a49637680802395f42839cd97e488c7300e9` to `c9bdae72baec052a6d83a5f49e01c5493416f36b`. I read all four commits between them.
- `2c9ded0c` and `80928f6f` change no plan text.
- The round-1 records have not changed since `80928f6f`, and the briefs have not changed since `2c9ded0c`.
- The repair leaves `edits.json` and `graph_repair.py` unchanged, and touches nothing outside `docs/ephemeral/`.
- At the branch head `eb31b964`, the plan files and the record are byte-identical to `c9bdae72`.

## Dispositions of the round-1 required findings

### R-A1 / B-1 — R3 — fixed

**The code.**
- **`check`** (`body_check.py` lines 405–410) takes the newest read after the cutoff. It requires `revision_moved`, `landed` for every operation, and every guard.
- **Removed:** `pre_edit_read_found`, `rest_unchanged`, `differing_lines` and the pre-edit lookup.
- **`landed()`** (lines 186–198) uses only the read in hand and the operation's `start`, `end` and `new` from `edits.json`.
- **`registry`** uses the newest read after the same cutoff.
- **Saved fetch files** (tool results) with an mtime before the cutoff are skipped before they are opened (line 118).
- **Transcripts** are parsed newest first and stop at the first entry older than the cutoff (lines 77–99).
- **A forgotten `--fetched-after`** still uses only the newest read, so no path brings the comparison back.

**On the live pages.** I took my own fresh reads after `T` = 13:10:53.000Z, applied the edits in memory, and printed counts only.

| Case | Result |
|---|---|
| Correct landing | passes on 8 of 8 pages |
| Every incomplete batch: each proper subset of a page's operations, including none applied | 0 of 82 pass |
| Replacement inserted twice; replacement beside a kept old span (before or after); replacement shortened by one character | each fails for all 22 operations |
| IA30-1 and PE-1, whose start anchors recur in their own replacements | counted correctly, and fail in every case above |
| Eight operations whose end anchors recur in their own replacements (QA50-1, CFC30-2/3, CFE30-2/3, ESC40-1, PE-3, PE-5) | counted correctly. No end anchor recurs in another operation's replacement on the same page |
| A stray change outside every span | passes on 8 of 8 pages, as P2-7 states |
| An `old_str` shortened inside an anchor | passes for 22 of 22 operations (L-C1) |

**`plan` (X2) on the same reads.**
- All eight pages sit at their pins, and 22 of 22 operations apply.
- `batch_safe` holds with every end anchor unique.
- `check_would_pass` is true on 8 of 8 pages.
- Failing guard rows fall from 27 to 0.

**G-F02-A per sentence.** I built a synthetic line from `edits.json` and the guard's own fail fixture: "3. Record the execution arrangement the Product Owner chooses. Another authorized operator executes them."
- Per line it passes. Per sentence it fails.
- The registry form, run through the shipped engine, fails it too.
- The dry run's registry-form gate agrees on 24 of 24 fixtures and 32 of 32 page rows.

**The text.** §3 point 5, §12, the docstring and the record's §P *Checks* bullet now describe a single-read check. X5 adds a full reading of each landed page under PF04 §9.1.6, and §8 lists P2-7. Two precision gaps remain: L-C1 and L-C4.

### R-A2 / B-2 — R1 — fixed

- **The step order.**
  - X6 is a checkpoint that leaves the record `EXECUTING` (line 112).
  - X7 writes W9 and W10.
  - X8 writes only the PR body.
  - X9 records X6–X9 and the item dispositions, sets `COMPLETE` and `interaction_cost_actual`, commits and pushes, then marks PR #600 ready and checks the head (line 115).
- **The record never claims a step that has not run.**
- **The validator** (`modification_validate.py`) passed scratch copies of the record at two states:
  - the X6 state: `EXECUTING`, approval set, a DIFF_CHECK ledger entry added, §E partly filled;
  - the X9 state: `COMPLETE`, four item dispositions, `interaction_cost_actual` set.
- **The failure path.** §6 has a new case, "At X6 to X9" (lines 156–159), in which PART-01 stays landed and X3 is not reverted. The flow diagram matches it.
- **W9's link.** W9 links the record by its path and by PR #600. PR #600 is this branch's record PR: open, draft, head `eb31b964`, base `main` `1ea6a262`.
- **Left open:** L-C2 and L-C3.

## New required defects

None.

- **L-C1 is not required.** The wrong edit needs a copy slip at X4, and the plan's own X5 reading looks for exactly that fragment. That makes it a low-likelihood failure-path risk, not a silent normal-path edit.
- **L-C2 is not required.** On the normal path, W9 becomes true when X9 completes. On the failure path, the stop is loud and the record states what X7 wrote. The rubric lists such cases.

## Trend

- **The count halved.** Round 1 found 2 distinct required defects. This check finds 0.
- **Six of the seven listed observations sit in text the repair added.** A check confined to the repair's diff produces that by construction.
- **The cap is reached.** D26-A allows two FULL reviews and one DIFF_CHECK per mode, and §11 names this check as PLAN's last review. The plan returns to Nathan with every open finding.

## LISTED observations

Each line gives the path, likelihood and consequence, and whether the text is in the repair.

- **L-C1 — the anchor counts miss a cut inside an anchor.** Failure path: a copy slip at X4. Likelihood low. Consequence: a fragment of the old text, from 1 character up to the anchor's length, stays at a span edge if the reading misses it. In repair text: yes.
  - **What the counts see.** They catch an `old_str` cut that leaves a whole anchor. They do not catch a cut inside one.
  - **What I found.** On my reads, each of the 22 `old_str` values, shortened by one character at either end, still passes X5's `check`, every guard included. The largest passing cut is 16 characters (PE-1, tail) to 78 characters (PE-3, head). `update_content` would accept such an `old_str`, because the shorter text is still unique on the page.
  - **What catches it.** Only X5's full reading, which is a reading rather than a command (template rule 4).
  - **What the plan claims.** §3 point 5 and the `landed()` docstring say a truncated or partial replacement "leaves a count off and fails". P2-7 accepts only changes outside the spans.
  - **Smallest correction, either of:**
    - state the gap and extend P2-7 to "a fragment at a span edge";
    - add short committed context anchors either side of each span, and require context, replacement and context to occur once. That needs no earlier read.
- **L-C2 — W9 claims completion at X7.** Normal path: Notion says "EXECUTE complete" for a few minutes while the record says `EXECUTING`. Failure path (X8 or X9 fails): both tracking pages keep the claim. Likelihood low. Consequence: two Notion maintenance surfaces overstate the state until Nathan acts; the stop is loud. In repair text: the step order and the §6 wording; the W9 sentence itself predates the repair.
  - **Why it stays.** §6 swaps back only "a half-written tracking line". It does not say whether a complete W9 beside a failed W10 counts as half-written.
  - **Smallest correction, either of:**
    - word W9 so it is true when written, for example "EXECUTE's page and graph changes landed and were verified on <date>; the record closes in PR #600";
    - swap back any W9 or W10 already written when X8 or X9 fails.
  - **Also, predating the repair.** "The package work moved to a new Modification (DN-1)" reads as if that Modification exists. None does yet; MB-008 carries the work.
- **L-C3 — X9 records itself before its last checks.** Normal path. Likelihood low. Consequence: interpretation only. In repair text: yes.
  - **The gap.** X9's own push, ready-for-review and head checks run after its commit, so X9's row has to be written before them.
  - **After X9's push.** If a later check fails, §6's "Keep `status: EXECUTING`" holds only by applying X9's rollback (R-G). The X6–X9 case does not say so.
  - **Smallest correction.** X9 records its pre-commit checks, and the return to Nathan reports the push, ready and head checks.
- **L-C4 — the D22 wording is slightly broader than the code.** Hygiene. Likelihood low. Consequence: none, because neither mechanism feeds a landing decision and nothing is stored, so neither creates the parallel copy the corpus policy targets. In repair text: the claims and `_recent_lines` are new; the de-duplication key predates the repair.
  - **The block read.** `_recent_lines` reads a transcript's tail in 1 MiB blocks. At X5 that block is likely to load the bytes of X2's earlier reads into memory, though never parse them.
  - **The de-duplication.** `all_fetches` keys captures by `(as_of, body)`, so Python hashes and compares body strings in memory.
  - **The claims.** The docstring, §3 point 5 and §12 say no body is "hashed, compared with another read" and that a transcript is "read only back to the cutoff".
  - **Smallest correction.** Key captures by `(as_of, captured)`, and say "parsed back to the cutoff".
- **L-C5 — no fixture pins the sentence unit.** G-F02-A moved to sentence units, but its one fail fixture also fails per line. Maintenance path. Likelihood low. In repair text: yes.
  - **Smallest correction.** Add the synthetic line from R-A1 above as a fail fixture, which pins the repaired behaviour (GUARD-001).
- **L-C6 — wording left behind.** Cosmetic. In repair text: partly.
  - "X0–X8" survives in two places, although the steps now run to X9:
    - PLAN-SUCCESSOR-2's opening paragraph (line 5), the sentence the repair edited;
    - the record's §P summary (line 210).
  - §13 does not list PF04 §9.1.6 as the basis for X5's full reading, which the X5 row cites.
  - R-N and §9 verify a restore by "every operation `UNTOUCHED`". `check` no longer reports that state; `plan`'s `state_before` still does.
- **L-C7 — the newest-first scan assumes timestamp order.** Failure path. Likelihood low. Consequence: a loud false stop after the writes, into the X4/X5 failure path. In repair text: yes, the scan is new.
  - **What I measured.** Before any fetch, my own transcript had 37 inversions of 1–5 ms in 148 entries. That is far smaller than the seconds between `T` and the reads the scan must find.
  - **The risk.** An entry appended late with an older timestamp would end the scan before the X5 reads, and `check` would report `NO_FETCH_FOUND`. One example is a message queued during X5, if the harness stamps it when it is typed. I have not verified that.
  - **Foreign reads.** Any read in the session after `T` is eligible, including another agent's. That is still a fresh read, and a pre-write read fails `revision_moved`.
  - **No silent stale selection.** No path selects a stale read without failing.

## Checks I ran, and their limits

**Ran:**

- **Repair diff.** I compared `git diff cfa3a496 c9bdae72` over the record, PLAN-SUCCESSOR-2, `body_check.py`, `dry_run.py`, `guards.json` and `dry-run.json`. The four `git diff --quiet` identities are in the header.
- **Fresh reads.** I took `T` with `date -u` before any fetch, then fetched the eight pages at 13:10:58–13:11:03Z. All eight were at their pins.
- **`body_check.py plan --no-ops --fetched-after T`** on all pages, and **`plan --fetched-after T --prompts IA-30 PE QA-50`**. I read the spans in this session only. Results are under R-A1.
- **Two scratch scripts** (`review-c/scripts/landing_sim.py` and `trunc_with_guards.py`). They import `body_check.py`, apply the edits and wrong edits in memory to the read in hand, and print ids, counts and booleans only.
- **G-F02-A on synthetic lines,** through a scratch copy of the shipped audit engine.
- **`dry_run.py <skills-root> review-c/dryrun 600 T`:** 10 of 10 gates pass at 13:13:15Z, on HEAD `eb31b964` and `main` `1ea6a262`.
- **X3's commands replayed in scratch** with scratch copies of the two skills. Every §4 value reproduces:

  | Output | Value |
  |---|---|
  | Freeze | `9 e241bb9a…` and `15 c214e874…` |
  | Apply and reindex | 7 changes; 237 edges and 25 files rewritten; a second apply and reindex change nothing |
  | Base build | 236 edges, `3510b2bf…` |
  | Repaired build | 237 edges, 596,008 B, `ff296b1e740a…` |
  | `check` and `built` | `"ok": true` |
  | Derivation | deriver exit 1; 771 B; `27a2be82b533…` |
  | Guards | 9,013 B; `62245446821994f70a50091664d45bc9234f0ad011b0d24a614692769d233114` |
  | Parts manifest | `b27c11ca2f93…` over 56 files |
  | Repository | `git status` clean |

- **`modification_validate.py`** on scratch copies of the record at the X6 and X9 states: 2 of 2 pass.
- **PR #600,** read through `pull_request_read`.

**Limits:**

- **No Notion write was made.** These remain untested against Notion:
  - X4: `update_content` matching spans that carry inline markup, the atomicity of a call with several replacements, and the async path;
  - X7: how W9 and W10 render, and whether the PLAN-return status line they replace exists;
  - how Notion renders the 22 replacements (P2-5).
- **The full reading is a judgement.** No command can rehearse it.
- **The simulations are in memory.** They apply edits as `update_content` is expected to; Notion may differ.
- **The ordering check covers only my own transcript.** I did not read the main session's transcript, which holds earlier reads (D22 condition 4).
- **Not re-reviewed:** the content of the 22 operations, the graph repair's design and F05's canon alignment, beyond reproducing the committed values. Round 1 cleared them, and the repair did not change `edits.json` or `graph_repair.py`.

## D22 disclosure

- **Bodies I read.**
  - QA-50, CF-C-30, CF-E-30, IA-30, QA-70, RS-20 and ESC-40 came back inline in this subagent's transcript (`subagents/agent-af7dd7dd1c6356fd5.jsonl`).
  - The harness saved PE to `tool-results/mcp-Notion-notion-fetch-1791724262671.txt`. I did not open that file myself.
- **What read them, in memory, through `all_fetches` with the cutoff 13:10:53.000Z:**
  - `body_check.py`: my two `plan` runs, and the dry run's `plan --no-ops` and `registry`;
  - my two scratch scripts.
- **What was printed.** The `plan` run with operations printed the ten spans and replacements of QA-50, IA-30 and PE in this session. This record names them only by operation ID.
- **`body_check.py`'s own mechanics** (L-C4) applied to my runs too. It read my transcript's tail in 1 MiB blocks and de-duplicated captures in memory by body text.
- **Before `T`**, I parsed only the timestamp fields of my own transcript, which then held no prompt body. I listed the session's tool-result files by name, size and time only.
- **Nothing hashed, byte-compared or stored by me.** I wrote no body, and nothing derived from one, to the repository or to scratch. Scratch holds:
  - the two scripts;
  - the dry-run receipt;
  - the X3 replay outputs;
  - two validator copies of the record.

  None of them contains body text.
- **Files left behind.** This session cannot delete harness files, so my transcript and the PE tool-result file are left to the harness's teardown and are not read again.

## Canon relied on

I searched `docs/pfcanon/` on `main` (`1ea6a262`, which the branch does not change) for:
- readback, read back and read-back;
- byte-for-byte, byte comparison and byte-compar;
- prompt body and transient read;
- ready for review, draft PR, tracking line, page history, transient and harness record;
- D22 and corpus.

| Source | Sections read | Use |
|---|---|---|
| PF04-Canon-HDE-Governance v2.8.7 | §9.1.6 *Prompt ecosystem governance and provenance*, in full (lines 2503–2527): read back complete changed bodies; static checks and publication readback are not runtime validation | Basis for X5's full reading (R-A1, L-C1) |
| PF04-Canon-HDE-Governance v2.8.7 | §9.1.3 *Artifact storage and execution-surface selection* (lines 2441–2459): Notion holds operational state; scratch holds transient intermediates | W9 and W10 as Notion operational state (L-C2); my scratch use |
| PF10-HDE-Build-Notes v13.5.1 | Front matter; *Precedence, versioning, and scope* §§1–2 (lines 1–40); Addendum Index ("No current addenda") | No PF10 addendum overrides anything this check relies on |

- **Other hits.** The search's other hits concern HDE product evidence, such as byte comparison of engine outputs and mapped-cache write and read-back. None concerns prompt bodies or tracking.
- **Where canon is silent.** PF canon says nothing on transient prompt-body reads, body comparison or tracking-line wording. The governing rulings for those are these prompt-ecosystem documents:
  - the decision record's D22 (lines 1204–1301) and D26-A to D26-F (lines 1694–1838);
  - `prompt-corpus-policy.md`, in full, including the D22 amendment;
  - `modification-template.md`: rules 1–8, §P and §E;
  - `session-working-rules.md`, *Tracking is part of the work*;
  - `modification_validate.py`: entry gates, `COMPLETE` checks and the command line;
  - `AGENTS.md`: the canon-first rule and the PR-description rule.
- **In-flight documents:**
  - `BRIEF-PLAN-DIFF.md` at `eb31b964`;
  - `BRIEF-PLAN-1-A.md`, whole, including §3 and §5;
  - `REVIEW-PLAN-1-A.md` and `REVIEW-PLAN-1-B.md`;
  - the record's frontmatter and §P (DN-1, successor 2, review round 1) at `c9bdae72`;
  - `PLAN-SUCCESSOR-2-20261011.md` at `c9bdae72`, in full;
  - `plan-successor-2/`: `body_check.py`, `dry_run.py`, `guards.json`, `dry-run.json` and `edits.json`.

DECISION NEEDED. The plan returns to Nathan for EXECUTE approval. No required finding is open, and the cap is reached.

- **Option 1 (recommended): approve.** Approve the plan at the commit that carries this record, accepting P2-1 to P2-7, the round-1 listed findings and L-C1 to L-C7. Every failure path above stops loudly, and X5's full reading covers L-C1.
- **Option 2: opt in to two text-only corrections.** These are L-C1 (the §3 point 5 claim and P2-7) and L-C2 (W9's wording). That is a further round priced under D26-A rule 4, after the last review §11 allows for PLAN.

I recommend Option 1. Neither correction changes what EXECUTE does on its normal path.
