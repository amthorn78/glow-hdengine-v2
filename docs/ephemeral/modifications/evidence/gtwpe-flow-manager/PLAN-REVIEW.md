2

GTWPE-FLOW-MANAGER-PLAN-A: full PLAN review 1 of at most 2 (D26-A) of MODIFICATION-20261006-gtwpe-flow-manager. I reviewed §P at 43150c6dc24cd15b3aa64171d8d22f5f059a8df2 and read the draft body of GTWPE-FLOW-10 whole, in place. I found two required defects, both in the draft body:
- **R-1.** A PF10 change that the run holds back can still be drafted by a pass, and no check would see it.
- **R-2.** A session that stops never discloses the harness files that hold the TW prompt bodies it read.

EXECUTE's own steps hold on their normal path, apart from one escaped search pattern (L16). The handoff table and the catalog texts are right.

**Checks I ran, all read-only:**
- **The brief.** At 28f4037 it has sha256 `d38a3ddf9ff70067584116c3d93043872dba4e763913aae0bc05d8509b87bb9f`. 28f4037 adds only that file to 43150c6.
- **The record.** At 43150c6 it is 125,379 bytes, blob `566c967`. Its §A is unchanged from 601b330's copy; only the front matter changed and §P was appended. 43150c6 changes only the record and `gtwpe.handoffs.md`, and no canon.
- **The handoff table.** `gtwpe.handoffs.md` is 7,508 bytes with sha256 `d0d727c6…2315b`, which equals «HT». Its rows H11 to H13 are identical to design v1.2 §6, by `diff`.
- **The draft, by script.** The scripts printed counts only, and the draft was never hashed or copied:
  - 253 lines and 26,553 characters, with the twenty headings in §P's order.
  - `«V»` twice, both in lines 1 and 2.
  - `separate proof log` once, and each of GTWPE-D1's eight items once.
  - Every absent phrase 0 times.
  - No `<`, `>`, `[`, `]`, `|`, `\` or `~` outside inline code and the table tags. The longest line is 734 characters.
  - Broad match, case-insensitive: `merg` 9 (7 case-sensitive), `Drive` 1, `Library` 1, `Notion` 11, `session` 16, `pfcanon` 6, `configuration` 1, `settings` 1, and `model`, `effort` and `strength` 0.
- **X1.4's search, run both ways.** At 601b330 neither pattern hits. On the evidence file, the unescaped pattern finds 2 hits and the pattern as written in the table finds 0.

REQUIRED

**R-1: R4, a plausible path with a silent outcome. Also R3, a silent breach of a ruling.** The rulings are the Change Process Guide §3.5.2.8 post-QA drain ordering, design v1.2 D-3 as Nathan confirmed it at G1, and, on one route, his own decision in the run. It lies on the normal path and on the designed resume path.
- **Text, in the draft:**
  - *Passes*, item 5 (line 116): "the selected boundary only where the execution prompt sets one".
  - *B1 Scope*, step 5 (line 147): "do not draft it", and the choice it gives Nathan, "to draft the change, or to leave it out".
  - *B5 Consistency*, step 3 (line 165): a finding "adds that document to the run at B2".
  - *After each pass* (lines 133 to 139): five checks, none of them on what a pass drew from its source.
- **Evidence:**
  - **A drain takes the whole source unless Nathan selects part of it.** C1's approved §A, R9: "The drains read 'the entire incoming logical source by default'; the Flow Manager never narrows a pass to a selection". §P's two-sided check pairs the drains' "Nathan may optionally select agendas/sections" with item 5's boundary, which only the execution prompt can set. PF10 is passed "by its path on `main`". A record pass reads "every PF10 change that modifies, clarifies, supersedes or extends the approved specification" (C3's REC-PF10).
  - **No TW prompt applies the post-QA ordering.** §A gives it to triage alone: *What each rule becomes* reads "Change Process Guide §3.5.2.8, drain ordering | Triage". The C2 and C3 edit files add no such rule.
  - **So the body has one lever:** stopping the documents triage finds the change bears on. Three routes still hand a pass the whole of PF10, held-back change included, with nothing excluding it:
    - (a) Nathan resumes with "leave it out". The stopped documents go back to B2 with no boundary, because his decision is not the execution prompt.
    - (b) Triage judged the change not to bear on a routed document, and it does. The body itself makes a drain's reading the authority over triage's (line 146).
    - (c) B5 adds a document "at B2". That document never passes B1 step 5.
  - **Nothing later sees it.** B4, B5 and B6 never compare a draft's changes with RUN.md's held-back list. B6 step 5 (line 173) lists the change as held back while a draft carries it.
  - **Refutation tried, and it fails.** A careful session might relay "leave it out" as a selection, but the body does not give it that, and routes (b) and (c) do not depend on it.
- **Likelihood:** route (a) is likely whenever Nathan chooses "leave it out". Routes (b) and (c) are low to medium; PF10 carries addenda of epics at different QA stages.
- **Consequence:** silent.
  - A review-ready pull request carries a document that drains a change §3.5.2.8 allows "only after all QA tasks for the epic are complete". Design §10.5 keeps such a change "not drafted, unless he directs".
  - On route (a), Nathan has just told the run to leave that change out, and the description says it was held back.
  - Taken into canon, the document drains the change.
- **Smallest correction.** No TW prompt changes, and the boundary stays Nathan's:
  1. In B1 step 5, after "or to leave it out", add: "A decision to leave it out is a selected boundary that excludes the change, and every invocation for those documents carries it."
  2. In *Passes*, item 5, write "only where the execution prompt or Nathan's decision sets one".
  3. In *After each pass*, add a sixth check: "No redlines file, draft or proof log the pass wrote takes a PF10 change that `RUN.md` holds back as a basis." A difference is already a stop. Every proof log records "The basis for those changes", so the check is mechanical.
  4. Optionally, *The execution prompt* item 5 can let Nathan choose "leave it out" in advance, as it lets him choose "draft it".
- **In text the last repair added:** not determinable. The "leave it out" choice is P-2's text; the boundary rule is §A's.

**R-2: R3, a silent breach of `D22` condition 5 as the GTWPE applies it.** It lies on the designed stop path.
- **Text, in the draft:**
  - *Stop and resume*, "On any stop" (line 228): the session records what is done, what is not, "the signal and the exact resume point", and returns. It names no harness file.
  - *RUN.md* (line 107): "the harness files and the prompt-body reads (B6)".
  - *B6 Complete*, step 4 (line 172): it names "every file the session's harness keeps that holds a prompt body".
- **Evidence:**
  - `D22` condition 5: "the session says in its report that it happened". `prompt-corpus-policy.md` puts it as "Disclosed in the session's report: which bodies, and that the files were deleted".
  - C1's approved §A A.6 carries E-016 to C4 as "Harness files from reading prompt bodies are disclosed in the run report (`D22` condition 5)". Design v1.2 §7.5 names subagent transcripts under the same condition.
  - Stops are designed to happen: S1 for PF20-sized work, and S4 for every held-back PF10 change under P-2.
  - A session that stops after a pass leaves bodies on disk: its transcript and its pass subagents' transcripts hold the TW bodies read live, as does any harness save. Its `RUN.md` and its return name none of these files, or what became of them.
  - The resumed session's B6 names only its own files, and no record tells it the earlier session's.
  - `RUN.md`'s per-pass read record (line 26) says which bodies were read, but not which files hold them.
  - **Refutation tried, and it fails.** Read strictly, D22 covers transient saves, and the five TW bodies came back inline at P4. But the GTWPE's approved texts apply condition 5 to transcripts, and the body's own B6 step 4 does too.
- **Likelihood:** for transcripts, the omission is certain on every stop after a pass. A harness save of a TW body is unlikely at 100626.2.
- **Consequence:** silent. The practical harm is small, because the files are left to teardown, but no stopped session meets the ruling's disclosure, and no later session can supply it.
- **Smallest correction:**
  - In "On any stop", after "the exact resume point", add: "and, as B6 step 4 does, the harness files this session holds that carry a prompt body, and what became of each".
  - In B6 step 4, add: "and those that `RUN.md` records for the run's earlier sessions".
- **In text the last repair added:** not determinable. The omission follows §A ITEM-07's "At B6".

LISTED

Each line gives the attack item, where the finding sits, the finding, its path, its likelihood and its consequence. For every finding, here and above, whether it sits in text the last repair added is not determinable: this is the first full review, and §P does not identify its fourteen pre-commit repairs.

- **L1 (A1).** *Resume* (line 229) never re-reads the two Notion edit times (lines 101, 171). An edit made while the run was stopped therefore stops it at B6 (S6) on every resume. Any GTWPE Modification's X4 makes such an edit, and so will E-041's planned fixes. K-2's "Nathan resumes" does not clear the stop, and the body names no decision that does. Failure path; medium; loud, but the run cannot reach `RUN_REVIEW_READY`.
- **L2 (A1, A3).** A canon source that changes during a run, such as a new PF10, stops it (line 110). Every resume then fails the same base check, so the only way out is a new run. Six commits titled as PF10 changes touched `docs/pfcanon/` on 2026-09-29. Multi-session runs; medium; loud and costly.
- **L3 (A1).** B1 step 1 ("record `origin/main` as the intake commit", line 143) runs before step 2 sends RESUME to *Resume*. A literal resume can re-base and miss a canon change made while the run was stopped. Fix: make the RESUME redirect step 1. Failure path; low, since *Sources and reading* and *Resume* point to `RUN.md`; silent if it happens.
- **L4 (A1).** B6 (lines 169 to 174) does not re-check the targets' base blobs before marking the pull request ready, so a target changed on main during B5 is missed. Normal path; low; a stale draft whose base blob shows in the description.
- **L5 (A1).** When every routed document returns `no redlines` (line 124), the run still reaches B5. It then returns `RUN_REVIEW_READY` with no draft, although *Results* (lines 238 to 250) and B1 step 7 define that case as `RUN_NO_CHANGE`. Normal path, since triage routes a document when unsure; medium; a wrong result code and a needless review, or an S4 stop.
- **L6 (A1).** The Apply-diagnostic cycle (line 127) has no count bound when each attempt fails differently; S3 (line 209) counts only a repeated failure, so only S1 ends it. Failure path; low; loud.
- **L7 (A3, P-3).** Check 3 (line 136) needs a snapshot of the remote's branches taken before the pass, and *Before each pass* (line 110) takes none. The check still stops a clean run whenever another session creates or deletes a branch, which is the false stop P-3 set out to remove. Normal path; medium; a loud S6.
- **L8 (A3, K-11).** Going on past P-1 to P-4 departs from template rule 1 ("does not carry on past the finding"). The departure is disclosed. P-1 follows plan v1.2 §1 exactly, P-2 is §A's own S4 row, and P-4 is factual. Certain; no consequence beyond those four.
- **L9 (A4).** Line 49 lets a change to an existing PF30 record proceed with no authorization in the execution prompt. C1's approved A.6, on E-010, says a PF20 or PF30 section is written "only when the run's execution prompt names it", and HDE Governance §9.1.1 requires "a separately authorized historical drainage action". §A settles the route this way. Normal path; medium; a PF30 update Nathan did not ask for, visible to him at review.
- **L10 (A4).** B4 check 4 (line 159), "agrees with its version and its date", omits DC-HIST's rule that a PF30 material-change row's date keeps its decision-date meaning. Read strictly, it fails every PF30 record update, then stops it (S5) after one redo. Normal path for PF30; medium; loud.
- **L11 (A4).** B6 step 1 (line 169) lacks B4 check 5's canon exception. PF27's templates, PF30.1's §7 template and PF20's historical TBD can therefore fail B6, or be recorded as passing that point. Normal path; medium; a loud stop, or an inexact `RUN.md` record.
- **L12 (A2, A4).** A rollover's review copy of the next volume has no base version: HDE CRD Records §6 says its version "is established when that volume is created". B4 check 1 (line 156) cannot pass it, so it stops (S5) after one redo. Rollover path; likely when Nathan authorizes a rollover; loud.
- **L13 (A2).** The file name in item 6 (line 117) needs the new version before the pass derives it. If the run and the pass bump the version differently, B4 check 1 fails, then S5. Normal path; low; loud.
- **L14 (A5).** B5 step 2 (line 164), "never retyping it", names no way to capture the return. Writing the return through the session's own file write is retyping (EVID-001). Normal path; medium; a captured review that differs from the return.
- **L15 (A5).** The body omits GTWPE-D1's sentence that a proof log "should provide enough evidence for another session or reviewer" (lines 178 to 187). B6 checks only that the eight items are present, which is all ITEM-06 asked for. Normal path; low; a thin proof log passes.
- **L16 (A6).** X1.4's search is written `'handoff table\|design v1.2 §6'`, with the pipe escaped for the table. Copied literally, it matches nothing anywhere. The D26-E check then passes vacuously, or fails after W1 to W3 have run. Normal path; low; a blind check, or a stop that leaves a published page to archive.
- **L17 (A6).** P13's `merg` count of 7 is case-sensitive. The case-insensitive count is 9, and both extra hits fall within the exception for "Merging preserves the record and approves nothing (D21-C)". Certain; none.
- **L18 (A6, K-3).** W3's 26,553 characters are retyped into the call, and once X1.3 (j) deletes the draft, nothing can be compared with the reviewed text. Only (h)(6)'s readings guard against a slip. Normal path; low; already accepted as K-3.
- **L19 (A6, not exercised).** Four things are untested:
  - W2's `icon: "none"`;
  - what duplication does to the original's edit time and child blocks;
  - CAT-ROW's three-line `old_str`;
  - how Notion renders `<key>` inside a `<td>` (line 86).

  Each would fail loudly at X1.3 (g) to (i) or X4.2. Normal path; low; a D26-B stop.
- **L20 (A7).** In `gtwpe.handoffs.md`, F3 omits a drain's question (S4). F5's "any other failure, Nathan, `RUN_STOPPED`" omits the body's retries for `PARTIAL_PACKAGE` and for `BLOCKED` with an input the run holds. Closure is unaffected. Certain; low.
- **L21 (A1).** The same-date rule (line 132) re-drains every document that is applied on a later date than its drain. The rule is needed only where the target's format records a revision date (C3's K-4). Multi-day runs; medium; the cost of a whole extra drain.
- **L22 (A5).** The invocation is "the pass's whole brief" (lines 111 to 118), yet it does not state E-006's bound on what a subagent may write. The bound rests on each TW prompt's own output rule. Normal path; low; a stray write the run does not see.

**What holds, claim by claim:**
- **C1.** It holds on EXECUTE's normal path, apart from L16.
- **C2.** ITEM-01 to ITEM-07 are carried out as §A settles them, with P-1 to P-4. P-1 and P-2 are faithful to their sources, and P-3 narrows an approved check, as disclosed. The draft fails C2 at R-1, and L5 is a normal-path inconsistency.
- **A1, the stop and resume design.**
  - No path double-applies: every apply and record pass starts from canon.
  - No path collides with a superseded draft: superseded drafts are moved aside first, and each pass gets a new directory.
  - No run ends review-ready with a stopped document.
  - B4, B5 and B6 each allow one redo before S5, and B5 one further review.
- **C3.** It holds against the C2 and C3 edit texts: every invocation field is supplied and every return is consumed. No TW prompt needs to change, R-1's correction included.
- **C4.** It holds.
- **C5.** It fails on §3.5.2.8 (R-1) and on `D22` (R-2) and holds on every other ruling. I could not check the PE Metaprompt's authoring exclusion: I did not read it, but the draft has no model, effort, workload or runtime-selection text.
- **C6, C7 and C8.** They hold. W1 to W4 are the only Notion writes, and each is within *Notion writes* as F-2 applies them.

**Method and disclosure:**
- **Commands, all read-only:**
  - `git`: `show`, `log`, `rev-parse`, `diff --stat`, `ls-tree`, `grep` and `status`.
  - shell: `grep`, `sed`, `cut`, `wc`, `sha256sum`, `od`, `ls`, `find` and `date`.
  - `python3 -I -c`, printing counts only. No `.pyc` file is newer than this session.
- **No other actions.** I made no fetch and no Notion, Drive, GitHub, session or agent action, and I wrote no file. The working tree was clean at the end.
- **Harness side effects that were not mine:**
  - The repository's PostToolUse hook (`.claude/hooks/check_canon_relied_on.py`) updates `.git/canon_relied_on_hook.json` after each Bash call.
  - The harness saved one oversized output of canon text, PF04 §9.1, as `tool-results/bfywrv5le.txt`. It holds no prompt body, and I did not read it.
- **The draft.** I read it in place and quote it here only by the clause at issue. My transcript holds it; this is the `D22` disclosure.
- **What I did not read:** no TW body, no GTWPE-MGMT-10 body and no PE Metaprompt body. What I say about the TW prompts rests on the edit files, `P1-SOURCE-NOTES.md`, §A and §P.
- **Not run:** the two record checks, which the brief does not list.
- **Not exercised:** any Notion write, the duplication, Notion's rendering of the body, and any live run.

## Canon relied on
- **AGENTS.md:**
  - the canon-first rule, and PF canon as read-only;
  - the pull request description rules and D21-C;
  - evidence attribution;
  - the truncation guardrail;
  - the code-review scope line, which does not apply to this D26-A review.

  The requirement for this block comes from ledger E-036 in `docs/ephemeral/gtwpe.rewrite/ERRORS.md`. I also read E-006, E-010, E-013, E-016, E-020, E-022, E-033, E-035, E-040 and E-041.
- **PF canon, from `docs/pfcanon/` on main at 601b330:**
  - Technical Writing Best Practices (PF03): whole.
  - Change Process Guide (PF06): §0.2 and §3.5.2.8, in full.
  - HDE Governance (PF04): §0.4; §9.1.1 and §9.1.6, in full.
  - HDE Build Notes (PF10): 2.29 PF10-CANON-001; 2.38 PF10-AINEUTRAL-001, in full.
  - HDE CRD Records (PF30.1): §0; §4.2; §6, in full; §7's material-change template; §8's HDE-CRD-0001 material-change history.
- **Governing documents in `docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D20 to D26.
  - `modification-template.md`: rules 1 to 8 and the §P template.
  - `ecosystem-change-management.md`: §1 to §6.
  - `gtwpe/gtwpe.decision-record.md`: GTWPE-D1.
  - `reviewer-prompt-template.md`: the second template.
  - `notion-write-boundary.md` and `prompt-body-content-policy.md`, whole.
  - `prompt-corpus-policy.md`: its `D22` amendment.
- **In flight:**
  - the record's §A and §P at 43150c6, `gtwpe.handoffs.md`, the brief, and the draft;
  - the target architecture, whole;
  - C1's §A: A.2, A.4, A.6 and A.8, and its catalog texts;
  - C3's record on PF30 updates and DC-R1, and its PLAN review;
  - the edit files `gtwpe-tw-repository-io/edits-2.json`, `gtwpe-tw-document-rules/edits.json` and `gtwpe-writing-side/edits.json`;
  - design v1.2 §5 to §7, §8.7 and §10, and implementation plan v1.2 §1.

IN FLIGHT: R-1 and R-2 go to repair. Then, as Nathan directed, a second reviewer or a check of the repair's diff follows, and the plan goes to him with L1 to L22 listed.
