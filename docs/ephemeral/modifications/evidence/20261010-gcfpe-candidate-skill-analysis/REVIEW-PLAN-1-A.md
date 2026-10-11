Distinct confirmed REQUIRED findings: 2

# PLAN review 1 of 2 — reviewer A — MODIFICATION-20261010-gcfpe-candidate-skill-analysis

**Two required defects, both in steps that PLAN successor 2 added. The rest of the plan holds.**

- **The 22 operations are clean.** I read the eight live pages at 12:12–12:16Z, and all eight were still at their pinned revisions. Each span is unique, sits on one line and carries no mention, link or escape markup. No replacement removes a prohibition, a return route or a required field list. The graph repair, the 237-edge build (`ff296b1e…`) and every expected digest in §4 reproduce exactly.
- **R-A1 (R3).** X5 compares each repaired page byte for byte with an earlier transient read. The prompt-corpus policy and D22 forbid that, and the plan presents it as compliant.
- **R-A2 (R1).** X6 writes the final §E and sets `COMPLETE` before X7 and X8 run. The normal path therefore cannot be run without interpretation, and the record cannot truthfully hold the outcomes of those two steps.

I reviewed commit `cfa3a49637680802395f42839cd97e488c7300e9`. The working tree at `2c9ded0c` differs from it only by the two brief files.

## REQUIRED findings

### R-A1 — R3 — X5's landing check is a byte comparison of prompt bodies, presented as D22-compliant

**Text or step**
- **X5 verification:** "`check`: every page `revision_moved`, `pre_edit_read_found` and `rest_unchanged` true, `differing_lines` 0, …".
- **§3, design point 5:** the re-read page must "equal the pre-edit read of the pinned revision with exactly the planned operations applied … Nothing is stored or hashed (D22)".
- **Elsewhere:** the record's §P *Checks* bullet, §12 and brief claim C7 say the same.
- **Code:** `body_check.py` lines 354–364. Line 360 is `row["rest_unchanged"] = expected == body`, where `expected` is X2's read with the operations applied. Line 362 counts the unequal lines.

**Evidence**
- **The corpus policy forbids it.** `prompt-corpus-policy.md` holds the Product Owner's directive of 2026-09-21, which is permanent. Line 31 forbids "byte-for-byte comparisons, hashes, or raw-file identity checks for prompt bodies". Line 41 says a plan that conflicts with the directive "is defective".
- **D22 forbids it.** The rule is in the decision record, lines 1228–1238, and in the policy, lines 102–112. It allows a transient file only when all of these hold:
  - it serves "only the read or check in hand, and is never a source for later work" (condition 2);
  - it is "never hashed, byte-compared or otherwise used as the body's identity" (condition 3);
  - where it cannot be deleted, it is "left to the harness's teardown and never read again" (condition 4).
  - D22 also lists, "without exception", "body hashes or byte comparison".
- **The postflight procedure forbids it.** Line 87 of `postflight-procedure.md` lists "byte-for-byte body identity against a stored copy" as prohibited.
- **X5 breaches all three D22 conditions.** At X5 it reads again X2's harness record of each body, which can be up to 240 minutes old, applies the operations and requires byte equality with the post-edit read.
- **Being in memory does not help.** D22 forbids the comparison itself, not only its storage.
- **Nothing asks Nathan for an exception.** I found no carve-out for a landing check in D22–D27 or in the record. The plan asserts that the check complies, so approving it would breach the ruling without anyone noticing.
- **The dry run never ran it.** N2 calls `plan`, not `check`, so the first comparison would happen at X5 of the first EXECUTE.
- **It is also the plan's only catch-all against a partial or stray edit.** I tested this on synthetic text built from `edits.json`.
  - A partial QA50-1 landing leaves "another authorized operator executes them" on the step-3 line.
  - That landing still reads `LANDED` and passes both G-F02-A and G-F02-B. G-F02-A's line-level exception "record the execution arrangement" exempts the whole line.
  - So removing the comparison with nothing in its place would allow a silent wrong edit (R2).

**Path:** normal.
**Likelihood:** certain; X5 runs the comparison on every page.
**Consequence:**
- EXECUTE performs a comparison that the Product Owner's permanent policy calls defective, under an approval obtained on an explicit claim that it complies.
- Raw-byte identity also turns any rendering difference into a stop after the writes, and Nathan then restores eight pages from page history.

**Smallest correction, one of two:**
- **(a) Ask Nathan for an exception.** Withdraw the D22-compliance claims in §3.5, §12 and the §P *Checks* bullet. In the approval request, ask Nathan for an explicit, scoped exception covering X5's in-memory whole-page comparison and its reuse of the X2 read.
- **(b) Replace the comparison.** Remove `rest_unchanged`, `differing_lines` and the pre-edit lookup from X5. In their place, add read-only text checks:
  - G-F02-A evaluated per sentence instead of per line;
  - for each operation, a check that the replaced span's distinctive old phrases are gone, where the new text does not repeat them.

  Then list the remaining risk, a stray edit no check can see, as accepted.

**In text the last repair added?** No repair round has run yet. This is new text in successor 2.

### R-A2 — R1 — X6 closes the record before X7 and X8 run

**Text or step**
- **X6:** "Write §E: step dispositions X0–X8, parts, artifacts with their readbacks … Item dispositions: … ITEM-04 `VERIFIED` … Set `status: COMPLETE` … Commit and push."
- **X7** writes the tracking lines W9–W10, which belong to PART-04. **X8** updates the body of PR #600 and marks it ready for review. Both run after X6.
- W9's text cites the "record link at the X6 commit", and §7's flow runs "X6 §E and COMPLETE; X7 tracking lines; X8 PR ready".
- No step after X6 writes the record.

**Evidence**
- **The template requires every step to carry a disposition.** Rule 5: "Every §E step and item carries a disposition … Silence is impossible by construction."
- **The template requires a plan that runs without interpretation.** §P: "A plan is complete when it could be executed mechanically with no interpretation on its normal path."
- **At X6 the executor must write outcomes that do not exist yet:** the dispositions and readbacks of X7 and X8, and `VERIFIED` for ITEM-04, whose part includes X7's Notion tracking.
- **That leaves two bad options.** The executor either claims those outcomes before measuring them, or leaves them without outcomes in a record already marked `COMPLETE`.
- **The validator does not catch it.** It does not check step dispositions. I copied the record to my scratch directory and set it to X6's state. `modification_validate.py` passes it.
- **The failure path breaks too.** §6 says "`status` stays `EXECUTING`", which cannot be true for a failure at X7 or X8. Read literally, a failed tracking line would record a PART-01 that landed as `BLOCKED` and revert X3.

**Path:** normal.
**Likelihood:** certain.
**Consequence:** the record Nathan merges either claims outcomes for X7, X8 and ITEM-04 before they occur, or never records them. The failure path also contradicts itself for the last two steps.

**Smallest correction**
- Move the record-closing work into a final step after X8:
  - the dispositions and readbacks of X7 and X8;
  - the item dispositions;
  - `COMPLETE` and `interaction_cost_actual`;
  - commit and push, then check the PR head again.
- Link W9–W10 to the record's path or to PR #600 instead of the X6 commit.
- Give §6 a separate case for an X7 or X8 failure, which affects PART-04 only.

**In text the last repair added?** No repair round has run yet. This is new text in successor 2.

## LISTED findings

- **L-A1** — failure path; low–medium; a stop after the writes, then page restores; new. X4 has the executor copy 22 `old_str`/`new_str` values by hand from X2's output (EVID-001). A truncated `old_str` passes the per-operation state and the guards (R-A1), so a replacement landing check must still catch it.
- **L-A2** — future audits; low; a hybrid reintroduction passes the registry form; new. G-F02-A exempts a whole line once it says "record the execution arrangement". Evaluated per sentence, its exceptions keep the permitted sentences and still fire on the old one.
- **L-A3** — claim C2; low; a paraphrased reintroduction passes; new. G-F04-A needs IA-40, QA-80 and *not*/*never* in one sentence, and G-F05-B matches three literal phrases, so neither is a broad match minus exceptions (D26-E). On the live pages they still catch the only instances: PE has one IA-40/QA-80 sentence, and only CF-C-30, CF-E-30 and PE carry the old format home.
- **L-A4** — normal path; low–medium; an extra question to Nathan, or a "pending" note in QA Plans; new. QA50-1's "Record the execution arrangement the Product Owner chooses" can be read as needing his choice at QA-planning time. Adding "when he has made one" closes it.
- **L-A5** — normal path; low; format drift in the addenda Nathan pastes; new. F05_FMT sends producers to PF06 §0.1A and PF27, but PF06 §0.1A assigns writing guidance to Technical Writing Best Practices, whose §9 *Output* says more:
  - follow the target's structure: HDE Build Notes' TEMPLATE entry with number and title, Timestamp and Details;
  - put a unique identifier in the title when needed;
  - cite other PFs inside PF10 by exact title, never by file name.

  F05_FMT also drops "unique metadata when needed" and narrows "status" to "approval status", which in CF-C-30 and CF-E-30 sits beside "It carries no status … field". §13 does not list PF03.
- **L-A6** — concurrent changes; low–medium; duplicate addendum numbers unless Nathan renumbers when pasting; the canon requires the behavior, but it is new to these producers. Producers now take the next number from the PF10 file at creation, and D6/D8 forbid tracking the paste. Two approvals made before the first paste get the same number. "The current controlled PF10 Markdown" is singular, while PF04's *Supersession* and PF10 §4 require one continuous sequence across a lettered set. This belongs on the backlog.
- **L-A7** — normal path; low; stale restated format lands without a stop; new. X1 compares the branch with its merge base but does not re-check `docs/pfcanon` on a freshly fetched `origin/main` before EXECUTE. The fix is `git diff --quiet 1ea6a262 origin/main -- docs/pfcanon` after the fetch.
- **L-A8** — normal path; low; addenda shaped differently by producer; new. IA-30 (YAML block), QA-70 and RS-20 (inline field lists) receive F05_FMT without ESC-40's "Beside that subject matter" bridge. Their producers must infer how the subject matter and the field list combine.
- **L-A9** — failure path; low; a false stop after the writes; new. X5's `--since-minutes 240` loses X2's reads after four hours, so `pre_edit_read_found` fails. In this same session, another agent's read could also become `fetches[-1]`. Option (b) of R-A1 removes the first cause.
- **L-A10** — failure path; low; a stop after W1 is already written; partly P2-5. The dry run cannot test four things:
  - `update_content` matching `old_str` values that carry inline markup: `**…**` and backticks in CFC30-2, CFE30-2, PE-3 and the IA-30 spans;
  - whether a call with several replacements is atomic;
  - the async path;
  - how italics re-render.

  A surprise at W2 leaves QA-50 already written.
- **L-A11** — needs interpretation; low; each fails loudly; new.
  - X0 puts the approval "verbatim in `plan_approved_by`", though the record's convention puts the name in that field and the quote in the section (§A.10).
  - X4 polls an async task with no bound.
  - X6's `grep -c` fails if §E repeats the TypeSafe phrase.
  - X7 depends on a status line that will not exist until PLAN returns.
  - X4, X7 and X8 verify by reading tool results, not by running a committed command (D26-A rule 1).
- **L-A12** — D22 hygiene; low; new. `all_fetches` opens every fetch record of a page within its window, including other agents' reads and the files §12 says are left to teardown and never read again (condition 4). The brief's `--since-minutes 600` makes reviewers do the same.
- **L-A13** — pre-existing; low; a label only. IA-30's `plan_delta_return` is the only branch whose `route_kind` is `TERMINAL_MANUAL_BOUNDARY` while `terminal_for_invocation` is false. I found no consumer of that label.
- **L-A14** — scope reading; low; already visible in §10. DN-1 keeps "the derived registry". The plan delivers the deriver's report and the guard assertions, and defers assembling a full candidate registry to release qualification; the approval request should name that reading. ITEM-01 `VERIFIED` covers only DN-1's narrowed scope, so §E must cite DN-1.

## Claims C1–C8

| Claim | Verdict | Basis |
|---|---|---|
| C1 operations | Holds | My `body_check.py plan` runs on the eight pages: 22 of 22 operations applied; every page batch-safe; failing guard rows go from 27 to 0. Spans checked against the live text: PE-1 matches IA-40's two modes, and QA-80 is preapproval-only (coverage.md). PE-2 changes nothing outside GCFPE. The three IA-30 locations are all repaired. ESC-40 keeps its field list. CFC30-3 and CFE30-3 keep "Do not track … that paste" |
| C2 guards | Partly | Fixtures fire every guard, and the registry form agrees on 24 of 24 fixtures and 32 of 32 page rows. G-F04-A and G-F05-B are narrow (L-A3); G-F02-A's line unit masks leftovers (L-A2) |
| C3 graph | Holds | Reproduced: 7 changes; 237 edges and 25 files rewritten, then 0; build `ff296b1e…`, 596,008 B; parts manifest `b27c11ca…` over 56 files; derivation 771 B `27a2be82…`, deriver exit 1, drift `[PR-40, RS-20]`; guards 8,869 B `8eb54659…`. The branches match RS-20's live *Rescope authorship, independent review and return* and *Required inputs*, F09 and plan-redlines. They do not overlap the existing branches: the non-PR native, PR-30 and PR-35 branches need another recorded origin, and the pre-Proceed case has no `PR_RETURN_PHASE`. The new edge sits at position 126; the largest `global.json` index is 124, not 125 as §3 says. No consumer depends on edge order. `format_expectations` passes through the build, the deriver and `regenerate_contract.py`; only the September validator's `EXPECTED_PF10_ADDENDUM_CONTRACT_PATHS` rejects it (P2-4) |
| C4 mechanical execution | Refuted at X6 | R-A2. X0 and X6 validator gates pass on scratch copies of the record. X1–X5 are mechanical apart from L-A11. The failure path meets D26-B and rule 6 up to X6 |
| C5 scope | Holds | Nothing moved is executed. MB-007 and MB-008 are each on the Modification Backlog once (I read the page at its 12:01:31Z revision). L-A14 is a reading of DN-1, not a dropped item |
| C6 canon | Holds, incomplete | F05_FMT covers PF06 §0.1A and PF27's elements, except "unique metadata" and the PF03 routing (L-A5). No PF change. No conflict with D27 found (L-A4 aside) |
| C7 D22 | Refuted | R-A1. The anchors and X2's rehearsal are compliant; X5's whole-page comparison is not |
| C8 §8 listing | Holds | F01, F06, F07, F08, L01–L11, MB-005, MB-006, SB-1 and P2-1 to P2-6 are correctly listed or moved. P2-1 matches F05's approved scope and is on the backlog |

## What I ran

All runs were read-only against the repository and Notion.

- I fetched the eight pages, plus IA-40, CF-C-40, CF-E-40 and the Modification Backlog. All eight targets were at their pins.
- I ran `body_check.py plan --since-minutes 600` on subsets of pages and read its output in this session only.
- I ran `dry_run.py` with the skills root and `scratchpad/review-a/dryrun`: 10 of 10 gates passed at 12:24:24Z, on HEAD `2c9ded0c` and main `1ea6a262`.
- I replayed §5.2's X3 commands in `scratchpad/review-a/x3`.
- I ran `modification_validate.py` on scratch copies of the record set to X0's and X6's states.
- I ran a synthetic partial-landing test.
- I searched the shipped skills that read the PF10 addendum contract.

## D22 disclosure

- **Bodies I read.** QA-50, CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40, IA-40, CF-C-40 and CF-E-40 came back inline in this subagent's transcript.
- **The PE body** came back as the harness file `tool-results/mcp-Notion-notion-fetch-1791720869793.txt`, which I read in slices in memory.
- **What body_check read.** It read the newest fetch of each page. Its scan also opened earlier fetch records of the same pages: the PLAN session's files listed in §12 and another reviewer's reads.
- **One extra read.** To write this disclosure, I listed the tool-results directory by page and revision, which parsed those files' headers in memory.
- **Nothing hashed, compared or stored.** I hashed or byte-compared no body. I wrote no body, and nothing derived from one, to the repository or to my scratch directory. The only body text shown was the operations' spans, printed in this session as the brief directs, and the short excerpts quoted above.
- **Files left behind.** This session cannot delete harness files, so they are left to the harness's teardown.

## Canon relied on

I searched `docs/pfcanon/` on `main` (`1ea6a262`, identical to the branch) for: addendum, Build Notes, numbering, H2, page-ready, format, and canon precedence. I read these sections:

| Source | Sections read | Use |
|---|---|---|
| PF06-Canon-Change-Process-Guide v2.5.4 | §0.1A in full, lines 21–64, including the addendum rule at line 64; §0.2 *AI review retrieval and proof order* and *Build Notes reference posture*, lines 276–288 | F05's format (A3); how to cite Build Notes |
| PF27-Canon-Plan-Templates v2.0.5 | *Out of scope and source routing* and *Canon precedence for template use*, lines 259–294 | F05's format; precedence |
| PF03-Reference-Technical-Writing-Best-Practices v1.8.8 | §9 *Writing PF10-HDE-Build-Notes content*, lines 306–358 | PF06 assigns addendum writing guidance here (L-A5) |
| HDE Build Notes (PF10-HDE-Build-Notes v13.5.1, `main`) | Complete, 189 lines: §§1–9, TEMPLATE, index ("No current addenda") | No applicable addendum; the continuous sequence (L-A6) |
| PF04-Canon-HDE-Governance v2.8.7 | *Supersession* and the Build Notes reference posture, lines 23–31 | Lettered sets (L-A6) |
| In-flight documents | Record §A and §P, including the DN-1 decision; PLAN-SUCCESSOR-2 and all six `plan-successor-2/` files; PLAN-SUCCESSOR-1; PLAN-20261011; plan-redlines.md; plan-flows.md; findings.md; coverage.md, QA-80 rows; MODIFICATION-20261009's `execute/candidate-graph-parts` | Scope and the base candidate |
| Repository controls | Decision record D6, D8, D9, D13–D15, D20–D22, D26, D27; modification-template.md; modification_validate.py; ecosystem-change-management.md; notion-write-boundary.md; prompt-corpus-policy.md; postflight-procedure.md; prompt-validation-procedure.md; AGENTS.md | The rubric and R-A1/R-A2 |

On whether a prompt body may be byte-compared, PF canon is silent. That question is governed by the prompt-ecosystem rulings listed in the last row.

IN FLIGHT. Both required findings go back to the PLAN author for repair, followed by the single DIFF_CHECK. If the author keeps the whole-page comparison, R-A1 becomes a decision for Nathan.
