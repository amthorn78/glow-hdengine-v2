1

GTWPE-FLOW-MANAGER-PLAN-DC: check of the repair's diff (D26-A rule 2) on PLAN of MODIFICATION-20261006-gtwpe-flow-manager, after full review 1 of 1. I checked `43150c6..ed964dc` and read the repaired draft of GTWPE-FLOW-10 whole, in place. All four repairs work, but the L5 repair opens one new path that misses a required disclosure:
- **DC-R1.** A run that ends `RUN_NO_CHANGE` at B3 has already run drains that read the TW prompt bodies. Its record never names the harness files that hold those bodies.

REQUIRED

**DC-R1: R3, a silent breach of a ruling, and also R1, a defect on the normal success path.** The ruling is `D22` condition 5, as this Modification's ITEM-07 (E-016) applies it.
- **Text, in the draft:**
  - B3 (line 155) ends the run with "the run ends as B1 step 7 does".
  - B1 step 7 (line 150) names no harness file.
  - *RUN.md* (line 107) holds the harness files only "(B6, and every stop)".
  - The files are named in two places only: B6 step 4 (line 174) and *On any stop* (line 230).
  - *After each pass* (line 140) still says "B6 checks two Notion pages".
- **Evidence:**
  - On this path every routed document has been through a drain, and a pass reads its TW prompt's body live from Notion (line 26). The session's transcript, or a subagent's, therefore holds a TW body.
  - The run then returns `RUN_NO_CHANGE`, which ends `NOTHING NEEDED` (line 252). It never reaches B6 and never stops.
  - `RUN.md` records each read (line 26) but names no file that holds a body. The session confirmed R-2 on exactly this point: R-2 found that the per-pass read record "says which bodies were read, but not which files hold them" (PLAN-REVIEW.md).
  - The rule has three approved sources:
    - this record's ITEM-07, "E-016, harness files disclosed in the run report", with §A's "At B6, `RUN.md` names every harness file that holds a prompt body";
    - C1's §A A.6, its E-016 row;
    - design v1.2 §11.6.
  - No later session exists to make the disclosure, and nothing checks for it.
- **Refutation tried, and it fails:**
  - The per-pass read record is not enough, by the session's own R-2 confirmation.
  - Line 107's "every session of the run" is limited by its own parenthetical, which leaves this ending out.
  - `RUN_NO_CHANGE` is not a stop, so *On any stop* does not apply.
- **Path, likelihood and consequence:**
  - **Path:** normal. Every drain returns `no redlines`, which is the path the session called the normal success path when it confirmed L5.
  - **Likelihood:** medium, the reviewer's rating for L5. On that path the omission is certain.
  - **Consequence:** silent. As with R-2, the practical harm is small, because the files are left to the harness's teardown.
- **Smallest correction:**
  - Line 155: "the run ends as B1 step 7 does" becomes "the run takes B6 step 4, then ends as B1 step 7 does".
  - Line 107: "(B6, and every stop)" becomes "(B6 step 4, wherever it runs, and every stop)".
  - Writing "B6 steps 2 to 4" instead also closes DC-L9.
  - The same words in B1 step 7 also close DC-L16.
- **In text the last repair added:** yes. L5's sentence in B3 creates the path, and R-2's line 107 lists the disclosure points without it.

LISTED

Each line gives the attack item, the finding, its path, its likelihood, its consequence, and whether it sits in text the last repair added.
- **DC-L1 (A1).** S6's row (line 226) still stops the run on "a difference in the checks after a pass". Line 140 now sends check 6 to S4 for the document, and S4's row (line 216) names that case. Failure path, when check 6 fires; low; the run stops instead of the document, loudly either way. In repair text: line 140 was narrowed, line 226 was not.
- **DC-L2 (A1, A2).** Two gaps leave a later pass without Nathan's "leave it out" boundary:
  - Nathan's decision at a resume is not among `RUN.md`'s contents (lines 100 to 107), so a later session may not have it.
  - B1 step 5's boundary binds only "those documents" (line 148), so a document that triage did not link to the change never carries it.

  Check 6 then stops the document again for a decision Nathan has already given. Resume path; low to medium on runs over several sessions; a repeated loud S4. In repair text.
- **DC-L3 (A1).** The body says neither that "leave it out" redoes the document from canon nor that "draft it" keeps the pass's outputs. Both follow from *Resume*'s "nothing completed and verified is redone" (line 231) and *Redo from canon* (line 178). A wrong choice meets check 6 after the next pass, or a collision at the output path (S3). Resume path; low; a loud stop or one needless redo. Relies on repair text.
- **DC-L4 (A1).** After "draft it", check 6's exception assumes `RUN.md` still lists the change as held back. B6 step 5 (line 175) then lists it as held back while the drafts carry it. Normal path after "draft it"; low; an inexact pull-request description, which Nathan sees. Partly in repair text.
- **DC-L5 (A1).** Check 6 is mechanical: it reads the basis each proof log records (GTWPE-D1's fourth item) and the redlines themselves. Each draft's Last Update Gate names the whole PF10 file (`BN <version>`, line 160). A strict reading of that as a basis would stop every document in a run that holds a change back. Normal path with a held-back change; low; loud S4 stops. In repair text.
- **DC-L6 (A2).** The boundary is still Nathan's, so C1's R9 holds: the Flow Manager only relays his decision, and PF10 still goes to each pass whole, by its path.
  - A drain takes the exclusion as a selection, or asks a question (S4).
  - §P's P5 shows the record prompts reading "every applicable PF10 change" and does not show them accepting a boundary. A record pass that ignores one meets check 6 (S4).

  Held-back path for PF20 or PF30; low; loud. In repair text. I could not read the drains' intake (`D22`), so this rests on P5's quotations and on the brief.
- **DC-L7 (A3).** *On any stop* (line 230) records "what became of each" file. It leaves the deletion of a save the session could delete to B6 step 4, by reference, so a literal stop could leave the save in place and say so. Stop path; low, since the TW bodies came back inline at 100626.2; disclosed, so not silent. In repair text.
- **DC-L8 (A3).** A stop at intake (B1 step 2, S2) comes before step 6 creates the branch, `RUN.md` and the pull request. That includes refusing an input that is a prompt body. The new disclosure has nowhere to go, and the return names the reason but no file. Failure path; low; the unreported transcript copy E-022 describes. A pre-existing gap, which the repair's "every stop" inherits.
- **DC-L9 (A4, beside DC-R1).** The B3 ending also skips B6 step 3's check of the two Notion pages, so after passes have run, K-1's "B6's Notion check sees only two pages" sees none. On a redo path that leaves superseded artifacts, it also skips B6 step 2's eight-item proof-log check.
  - Step 3: normal path, medium; the harm needs a stray Notion write, which is very unlikely.
  - Step 2: redo path; low.

  In repair text.
- **DC-L10 (A4).** On a B4 or B5 *Redo from canon* whose drain now returns `no redlines`, line 155's "no routed document has a draft" can hold although the result row's "every drain's `no redlines`" (line 251) does not. An earlier drain returned `READY`. The run then ends `RUN_NO_CHANGE` before B5 step 4's second review. Redo path; low; the final state is truthful, but the result's wording does not fit it. In repair text. The ordering is otherwise right: "none has stopped" sends a stopped document down the stop path, and a document B5 adds arrives while other drafts exist.
- **DC-L11 (A5).** Two rows lose detail:
  - L19 turns the reviewer's "`<key>` inside a `<td>` (line 86)" into "a placeholder in a table cell", which also reads as CAT-ROW's substituted cells.
  - L20's first half is met by signal, since F3 now carries S4. F3 still does not name a drain's question, as F8 names the record prompts' question.

  Certain; no consequence for execution. In repair text.
- **DC-L12 (C6).** *Repair round (PL3)*'s "Each repair is the reviewer's smallest correction ... and nothing else changed" is inexact for R-1:
  - The reviewer's item 3 left check 6 under "A difference is already a stop", which is S6 and stops the run.
  - The session made it a document-level S4 with an exception, and added S4's row, the `RUN.md` line, F3 and F8.

  The table itself states each change truly. Certain; a reader may credit the reviewer with the S4 design. In repair text.
- **DC-L13 (C6).** *Harness files, for `PLAN`* names `capture.py` but not the script that "applied the draft's nine changes". Certain; none for `D22`, since the clauses it handled are committed in `draft-repairs.json`. In repair text.
- **DC-L14 (D22).** `draft-repairs.json` commits passages of the unpublished body, each a clause long:
  - its old clauses run from 51 to 192 characters, and one is B3's whole text before the repair;
  - its new texts run from 95 to 457 characters, and two repeat their old clause whole.

  This matches the edits.json practice and the "clause at issue" limit, but each old clause is longer than a shortest unique anchor would be. Certain; small and visible. In repair text.
- **DC-L15 (A5).** The record's reason for keeping L14 listed, "Not one of the four required kinds", is arguable. A captured review that differs from the reviewer's return is a silent outcome on the normal path (EVID-001), at the reviewer's medium likelihood. L14 stays listed, as the reviewer classed it; only the reason is new text.
- **DC-L16 (pre-existing).** B1 step 7 (line 150) also ends `RUN_NO_CHANGE` without naming any harness file. There the transcript holds at most GTWPE-FLOW-10's own body, which counts as a `D22` read only if the session fetched it from Notion. Normal path; medium; small. Outside the repair; DC-R1's correction, placed in B1 step 7, covers both endings.

DISPOSITIONS OF THE LAST ROUND'S REQUIRED FINDINGS, AND THE TREND
- **R-1: fixed.** On all three routes, check 6 (line 139) now stops the document (S4) when a pass takes a held-back change as a basis. Route (a) also carries Nathan's boundary (lines 116 and 148). I could not reproduce a silent path. What remains is listed as DC-L1 to DC-L6.
- **R-2: fixed at every stop and at B6** (lines 107, 174 and 230). It is not fixed on B3's new ending (DC-R1), and a stop before `RUN.md` exists cannot meet it (DC-L8, pre-existing).
- **L5: fixed, with a new defect**, DC-R1.
- **L16: fixed.** The search finds nothing at `601b330` and two lines in the new file (lines 10 and 17), both matching `handoff table`. The old escaped form matches nothing.
- **Trend.** Four confirmed required findings (R-1, R-2, L5 and L16) became one (DC-R1), so the count halved. DC-R1 and most listed findings sit in text the last repair added, which is D26-A rule 5's second signal. This is also the last round Nathan's direction allows.

WHAT HOLDS, CLAIM BY CLAIM
- **C1 holds.** No TW prompt needs to change, apart from DC-L6's caveat on the record prompts.
- **C2 holds at every stop and at B6.** It fails on B3's new ending (DC-R1).
- **C3 holds for the result code.** The new ending skips B6's run-level steps (DC-R1, DC-L9).
- **C4 holds.**
- **C5 holds.** Only F3 and F8 changed. The file grew from 7,508 to 7,557 bytes, and its sha256 `61aee2ae…2c4bef` equals «HT».
- **C6 holds** for the draft and for §P's values. Two record statements are inexact (DC-L12, DC-L13), and two listed rows lose detail (DC-L11).
- **C7: half holds.** L5 and L16 were rightly counted under R1. The repair adds one required defect, DC-R1.
- **The full review's claims (A6).** On the new ending, DC-R1 breaks its C5 (`D22`) and its C2 (ITEM-07, which §A settles at B6). Its C1, C3, C4, C6, C7 and C8 still hold. The readback's broad match (X1.3 (h)(10)) finds three new `session` hits, all within that term's exception.

CHECKS I RAN, ALL READ-ONLY
- **The brief.** At `3f32337` its sha256 is `a4f6987fbc4575b6566eed244abd7da57a05196518f7028bb0813feddab0d5c5`, and `3f32337` adds only that file to `ed964dc`.
- **The repair diff** touches five files:
  - The record changes in these places and no others: the front matter's FULL round, the evidence row, «HT», the 255 lines in two places, X1.4, K-3, the twenty listed rows, *Full review*, *Repair round* and *Harness files*.
  - `gtwpe.handoffs.md` changes in two lines.
- **The draft, by script, printing counts only.** It was last modified at 19:31:21Z, before `ed964dc` was committed at 19:34:18Z.
  - It has 255 lines and 27,497 characters (27,507 bytes), and each of the nine new texts occurs once.
  - Undoing the nine changes in memory gives 253 lines and 26,553 characters, with each old clause once. The changes add 944 characters and two lines.
  - The twenty headings and the last line are unchanged.
  - `«V»` occurs twice, in lines 1 and 2.
  - `separate proof log` and each of GTWPE-D1's eight items occur once, and every absent phrase 0 times.
  - No character that Notion escapes appears outside inline code and the table tags.
  - Broad match: `merg` 7 (9 ignoring case), `Drive` 1, `Library` 1, `Notion` 11, `session` 19 (16 before the repair), `pfcanon` 6, `configuration` 1 and `settings` 1; `model`, `effort` and `strength` 0. The longest line is 734 characters.
  - The text rebuilt in memory reproduces the full reviewer's counts and all 33 of its line citations at `43150c6`.
- **The capture.** `PLAN-REVIEW.md` is 19,737 bytes with sha256 `1d154480…`: 19,680 characters of message and one final line feed. `PLAN-REVIEW-BRIEF.md` at `28f4037` has sha256 `d38a3ddf…`. Both are as the record states.
- **The twenty listed rows** were read one by one against `PLAN-REVIEW.md`.

METHOD AND DISCLOSURE
- **Commands:**
  - `git show`, `diff`, `log`, `grep`, `ls-tree`, `rev-parse` and `branch --show-current`;
  - `grep`, `sed`, `cat`, `wc`, `sha256sum`, `od`, `stat`, `ls`, `find` and `date`;
  - `python3 -I -c`, printing only counts and true-or-false results. One script rebuilt the draft as it was before the repair, in memory, from `draft-repairs.json`.

  I did not run `git status`, which can rewrite the index.
- **No other actions.** I made no fetch and no Notion, Drive, GitHub, session or agent action, and I wrote no file. No `.pyc` file under two hours old exists in the standard library or the repository.
- **`D22`.** I read the draft whole, in place, so my transcript holds it. I read no other prompt body, and I quote the draft here only by the clause at issue.
- **Side effects that were not mine:**
  - The repository's PostToolUse hook updates `.git/canon_relied_on_hook.json` after each shell command.
  - The harness saved one oversized output, the repair diff of the record and the handoff table (31.9 KB), as `tool-results/bjwjueirk.txt`. It holds repository text only, with no passage of the body beyond the clauses the record commits. I read it whole.
- **Not run:** the two record checks, which the brief does not list.
- **Not exercised:** any Notion write, the duplication, Notion's rendering of the body, and any live run.

## Canon relied on
- **`AGENTS.md`:**
  - the canon-first rule, and PF canon as read-only;
  - the truncation guardrail;
  - evidence attribution;
  - the code-review scope line, which does not apply to this D26-A check.

  The requirement for this block comes from ledger E-036 in `docs/ephemeral/gtwpe.rewrite/ERRORS.md`. I also read E-006, E-016 and E-022 there.
- **PF canon, from `docs/pfcanon/` on `main` at `601b330`**, the local `origin/main`, not fetched:
  - Change Process Guide (PF06): §3.5.2.8 in full, with its post-QA documentation drainage ordering; §0's drainage principles.
  - HDE Governance (PF04): the opening of §9.1, and §9.1.1 in full.
  - Technical Writing Best Practices (PF03): §3 in full.
  - HDE Build Notes (PF10): 2.29 PF10-CANON-001, through *In-flight change documents*; 2.38 PF10-AINEUTRAL-001, its source and rules 1 to 6.
  - The canon search: `git grep` over `docs/pfcanon/` for the held-back, selected-boundary and drain-ordering terms, and for redlines and drainage in PF03, PF06 and PF10.
- **Governing documents in `docs/prompt_ecosystem_management/` at `601b330`**, unchanged on the branch:
  - `gcfpe.decision-record.md`: D20 to D26, with D22's five conditions, its refinement and its status entries, and D26-A to D26-F.
  - `modification-template.md`: rules 1 to 8 and the template.
  - `ecosystem-change-management.md`: §1 to §7.
  - `gtwpe/gtwpe.decision-record.md`: GTWPE-D1.
- **In flight:**
  - the record at `ed964dc`: its front matter, §A's *The Flow Manager, settled* with ITEM-01 to ITEM-09, and §P whole;
  - its evidence: `draft-repairs.json`, `gtwpe.handoffs.md`, `PLAN-REVIEW-BRIEF.md` and `PLAN-REVIEW.md`;
  - the draft, whole, in place;
  - C1's §A: its rule table, R9 above all, and the E-016 and E-022 rows;
  - C2's Q-2, on how much of a body may enter the repository, and C3's DC-HIST rows;
  - design v1.2 §7.5 and §11.6, and implementation plan v1.2 §4;
  - this check's brief, `PLAN-DIFFCHECK-BRIEF.md`, at `3f32337`.

DECISION NEEDED: DC-R1 is open. Under D26-A rule 2 the plan now goes to Nathan with DC-R1, DC-L1 to DC-L16 and §P's twenty listed findings, and repairing any of them is his opt-in.
