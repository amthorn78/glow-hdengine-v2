2

GTWPE-TW-FLOW-RULINGS-PLAN-DC: the one check of the repair's diff (`D26-A` rule 2) for PLAN of MODIFICATION-20261007-gtwpe-tw-flow-rulings, on `1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f..9fefe96c1fd1bad898111bc35582619cc75d3c50`. The repair fixes RQ-1 to RQ-8 where *Repair round (PL3)* says. Two of its own changes, though, leave a contradiction beside them, so I find 2 required defects:
- **DC-R1.** RQ-2's repair makes the triage file name PF20 or the PF30 family in a reason when no specification is given, and narrows B1 step 5's stop to "an ineligible document to route". S4's own *When* cell, which the same repair rewrote, still stops a triage file that "names an ineligible document". So a run without a specification can stop on its normal path while HDE Build Notes 2.14 waits for PF30.
- **DC-R2.** RQ-1's repair widens what TW-RECORD-10 and TW-RECORD-20 make to "each other change, from PF10 or another source", and the decision record and the selection page say so. The same prompts' role line, output contract and Last Update Gate still allow only the record and PF10 changes.

Each needs a one-clause correction in `edits.json`. I list 12 more findings, most of them in the repair's own text. Required defects go from 8 to 2. That halves, but both sit in text the last repair added, which is `D26-A` rule 5's second signal. The cap is reached either way, so §P goes to Nathan.

REQUIRED

**DC-R1. R1, a defect on the normal success path (a loud stop).**
- **Text.** G-FLOW-10-E47's new text, S4's *When* cell: "a triage pass's error, or a triage file that leaves a change unaccounted for, omits a source it was given, or names an ineligible document;". It disagrees with three texts as this repair leaves them:
  - G-FLOW-10-E40, B1 step 5: "or names an ineligible document to route is a stop (S4)".
  - F11's check: "every document it names to route eligible".
  - TRIAGE-10-E11: "PF20 and the PF30 family are eligible only when a specification is among the files given; without one, the part of a change that bears on either cannot drain in this run, and the triage file names that document in its reason, not among the change's eligible documents". TRIAGE-10-E14 adds: "or PF20 or the PF30 family, named, with no specification among the files".
- **Evidence.**
  - "To route" was added to E40 so that a name in a reason would not stop the run. The repair round's RQ-2 row says so, and so does its new two-sided check: "its stop is for "an ineligible document to route"".
  - A script over `edits.json` finds "ineligible" in two new texts only, E40's and E47's.
  - S4's cell is a stop condition, not a summary. C4 sets the signal table as what the Flow Manager "stops on" before each pass and at each boundary (MODIFICATION-20261006-gtwpe-flow-manager §A ITEM-03).
  - This plan treats PF20 and PF30 without a specification as ineligible in the Flow Manager's check too. Dry run P5 checks B1 step 5 "against *Eligibility and routing*'s same set", where PF20 and PF30 count "only with a specification".
  - HDE Build Notes 2.14 belongs to no epic or CRD and binds PF30: "PF27 and PF30 adopt the same terms on their next revision". So in every run without a specification, the triage file names PF30 in 2.14's reason.
- **Path.** Normal: a run without a specification, such as PF10 alone. GTWPE-D4 and *SECTION* provide for it: "Without a specification, neither is updated".
- **Likelihood.** The condition holds in every such run while 2.14 waits. The stop follows whenever the Flow Manager applies S4's cell as written. Its two texts disagree and it may follow either, so medium.
- **Consequence.** The run ends `RUN_STOPPED` (S4) where it should end `RUN_REVIEW_READY`. No decision file Nathan gives removes the name from the triage file.
- **Why R1 although the stop is loud.** It stops the normal path, not a failure path. The session classed RQ-8 (B's L6) R1 on the same reading. If Nathan reads rule 3's loud-stop clause as covering it, it is listed instead, and the correction is the same.
- **Smallest correction.** In G-FLOW-10-E47's new text, change "or names an ineligible document;" to "or names an ineligible document to route;". Then re-run `edits_check.py` and fix «H» again.
- **In text the last repair added:** yes. RQ-2's repair makes the triage file name the document (TRIAGE-10-E11, E14) and narrows E40 and F11. It also rewrote E47 for RQ-1 but did not narrow that cell's triage clause.

**DC-R2. R2, a silent wrong edit to two prompt bodies, while the decision record and the selection page state the wider rule; also R4.**
- **Text: what the repair widened.** RQ-1's repair widens what a record pass makes in five places:
  - RECORD-10-E10: "Make every change the sources require in a copy of the actual assigned PF20 document, as *Output and completion* sets out: ...; and each other change, from PF10 or another source, that bears on PF20 in context and scope, except a held-back one". RECORD-20-E10 says the same for a PF30 volume.
  - G-FLOW-10-E14, E15 and E18: "each other change not held back".
  - GTWPE-D4: "and so does any other change a source carries that bears on it".
  - *SECTION*: "the specification's record and each other change not held back that bears on the document".
- **Text: what it left.** The same prompts' other new texts, unchanged since `1f73053`, still allow only the record and PF10 changes:
  - E09, in both prompts: "This role makes every change a run makes to PF20, an Epic's record and the PF10 changes that bear on PF20". TW-RECORD-20's reads the same for a PF30 volume and a CRD's record.
  - E14, in both, the output contract: "with each change made by an exact edit: the complete entry inserted once, ..., or the existing entry updated in place, and each applicable PF10 change at the passage it bears on. Never regenerate or rewrite the document: every other byte is preserved, and only those changes and the document-control fields below change."
  - E15, in both, the Last Update Gate: "the approved specification's filename when the update makes or changes a record, then, when the update carries or reconciles an applicable PF10 change,". It gives no form for any other source, though *SECTION* requires one: "or the source's filename alone for any other source".
- **Evidence.**
  - Comparing `edits.json` at both commits by script, the repair changed only E10 in each record prompt.
  - At `1f73053`, E10 also said "each PF10 change", so E09, E14 and E15 agreed with it. They no longer do.
  - *The edits, by rule* now says E09 to E21 make "each other change, from PF10 or another source, that bears on PF20". E09, E14 and E15 do not say it.
  - Nathan's S-6 and S-7 name only PF10 changes, so the widening is the plan's own. GTWPE-D4 credits it to RQ-1.
  - No check compares E10 with E09, E14 or E15. The readback finds each new text present, and the repair round read E10 only within its own passage.
- **Path.** Normal: a run whose files include a source other than PF10 carrying a change, not held back, that bears on PF20 or a PF30 volume beyond the specification's own record. One example is a closed CRD's Specification that changes PF30's own text. Another is "any other file or collection of source material that contains the change context" (Nathan's answer 5).
- **Likelihood.** Low as a path; the contradiction is certain as text.
- **Consequence.** The record pass either makes the change against E14, with a gate that names no source for it, or leaves it out, as E09 and E14 direct. If it leaves it out, `RUN.md` records the document as drained, or, on `no changes`, the change as already represented (E36, F8), and nothing reports the omission. Meanwhile GTWPE-D4 and the selection page say the record prompts make such a change.
- **Smallest correction.** Carry the widening into the same three texts of each record prompt, keeping their anchors:
  - E09: change "the PF10 changes that bear on PF20" to "each other change, from PF10 or another source, that bears on PF20" (in TW-RECORD-20, "on the volume").
  - E14: change "and each applicable PF10 change at the passage it bears on" to "and each other change the sources require, from PF10 or another source, at the passage it bears on".
  - E15: give another source's filename, in *SECTION*'s form.

  Then re-run `edits_check.py` and fix «H» again. The other way, narrowing back to PF10 changes, means changing RECORD-10-E10, RECORD-20-E10, G-FLOW-10-E14, E15, E18, GTWPE-D4 and *SECTION*. It would leave a non-PF10 change's PF20 or PF30 part with no pass to make it.
- **In text the last repair added:** yes, the widening (RECORD-10-E10, RECORD-20-E10, G-FLOW-10-E14, E15, E18, GTWPE-D4, *SECTION*). The texts it contradicts are older.

LISTED

Each line ends: [path; likelihood; consequence; in the last repair's text?]
- **DC-L1 (A5, RQ-6).** GTWPE-D3's provenance names the plan's DR-1, P-2, triage-file settlement, RQ-1 and RQ-2. Its last bullet's stop ("A run that drafts nothing while a change, or part of one, cannot drain in it ends stopped") comes from none of them: it is *What the plan settles*' endings, the settlement of B's L12. A's L3 named it. [normal; certain as text; low, provenance only, since the sentence names the plan approval too; yes]
- **DC-L2 (A7, B's L11).** Its listed reason says "the proof log names each change it holds back". The exact no-change exit writes no proof log (K-11), so in a direct invocation a held-back change is named nowhere. RQ-1 widens K-11 to a specification's changes. For HDE-EPIC040, PF10 records the QA verdict, not the closure decision (§A ITEM-05), so a direct drain given PF10 alone may hold back more than K-11's "Low" suggests. A fix touches the no-change exit that DC-L1 keeps, so it is Nathan's. [direct use; low to medium; a no-change result while a change waits, nothing lost from PF10; partly]
- **DC-L3 (A1).** A CRD's own record, made while that CRD's other changes are held back, records them as affected canon and intended drainage targets (HDE CRD Records §4.1). Check 6 (G-FLOW-10-E37) has no exception for the record, so a strict reading stops PF30 (S4). This is K-25's family. [normal, an in-flight CRD's Specification; low to medium; loud; yes]
- **DC-L4 (A1).** RECORD-20-E10's exception covers the record "made from the CRD's approval evidence". A PF10 change recording the same CRD's material decision bears on that record (§4.2) but belongs to the unclosed CRD, so it is held back. Nothing says whether a material update is part of "a CRD's own record". [normal, an in-flight CRD; low; the update waits, listed in `RUN.md`; partly]
- **DC-L5 (A1, E-010).** GTWPE-D3 and GTWPE-D4 rest the exception on HDE CRD Records §3.2, the side of E-010 that HDE Governance §9.1.1 contradicts ("The active workflow MUST NOT create, update or synchronize their entries"). Nothing is decided: the behaviour is §A's, and GTWPE-D4 keeps §9.1.1's framing and leaves E-010 to Nathan. §9.1.1's own *Historical drainage* would support the exception alone ("may add the approved planned baseline as planned state"). [—; certain as text; low; yes]
- **DC-L6 (A3, RQ-8).** "Files given alone mean `RUN`" (E07, F1). A resume given as the run's `RUN.md` and a decision file, without `RESUME`, starts a new run whose source is `RUN.md`. Its triage most likely finds no change, so it returns `RUN_NO_CHANGE` on a new pull request while the stopped run stays stopped. The resume line carries `RESUME` (E51). [resume; low; a wrong but visible result; yes]
- **DC-L7 (A2).** TRIAGE-10-E03 says the Flow Manager "routes each document the file names", and B1 step 6 routes "each document the triage file names for a change not held back". E11 now names PF20 or PF30 in a reason too. E16's "not routed" and E40's "to route" keep the two apart, but neither routing sentence says "among a change's documents". [normal, no specification; low; none, or a loud stop at the record pass; partly]
- **DC-L8 (A3, RQ-5).** *SECTION*'s second paragraph still says "a drain's verified `no redlines`, or a record pass's `no changes`, is the authoritative answer that a change is already represented there", without RQ-5's "not held back". Its next sentence says a held-back change waits. [—; certain as text; low, a control page's wording; no]
- **DC-L9 (A2).** Now that 2.14's PF30 part counts, every run without a specification that drafts nothing ends `RUN_STOPPED` (E42, E43, E50), and its resume cannot clear the stop (A's L20). That is S-4's rule as GTWPE-D3 states it, but K-8 records the effect only for a change whose home is PF10. [normal; certain with today's PF10; loud; yes]
- **DC-L10 (A6).** *Excerpts*' corrected list of where §P quotes a body ("about ten in *The two-sided check*, and a few in *Findings on §A* and *Repair round (PL3)*") leaves out *The new pages' checks*. Its `D26-E` exceptions quote about a dozen kept clauses ("the supplied change context", "request that fact", "section creation" ...), and it quotes GTWPE-MGMT-10's guard sentence. The 33 kept clauses that *Checks after the repair* counts bear this out. [record; certain; none; yes]
- **DC-L11 (A6).** *Harness files* converts two of the first save's ranges by one line at both ends (36–128 to 37–129, 173–207 to 174–208), but the third at its start only (291–353 to 292–353). Either that range ran to the save's end, or it should read 292 to 354. I cannot check: the save holds a prompt body. [record; certain as text; none; yes]
- **DC-L12 (A6).** *The stop rules* put RQ-5 in text older than the dry run's repair. But DR-1 names G-FLOW-10-E36 among the texts it changed, and A tagged its L1 so. Four of the eight then sit partly in DR-1's text, which is still not most, so the conclusion holds. [record; certain; none; no]

THE PRIOR ROUND'S REQUIRED FINDINGS, AND THE TREND
- **RQ-1: fixed with a new defect (DC-R2).**
  - The hold-back now covers a change from any source in every text the brief names: S-HOLD, both record prompts' E10, B1 step 6, check 6, S4, G-FLOW-10-E14, E15, E18 and E25, F3, F8, GTWPE-D3, *SECTION*, A1-NEW, P-1 and *What the plan settles*.
  - The CRD-record exception reads alike everywhere: RECORD-20-E10, E41, GTWPE-D3, GTWPE-D4, *SECTION*, A1-NEW, P-1 and *What the plan settles*.
- **RQ-2: fixed with a new defect (DC-R1).** The part that cannot drain is now accounted for in TRIAGE-10-E04, E11 and E14, B1 steps 5 and 7, B3, B6 step 5, `RUN.md` (E24), S4's scope (E46), *Results*, F11, GTWPE-D3, GTWPE-D4 and *SECTION*. No either/or form survives.
- **RQ-3: fixed.** APPLY-10-E19's anchor is C2's own sentence (APPLY-10-13 in `edits-2.json`, which C3 left alone). Its one exception, a no-change report, is the mode P-4 names and GTWPE-D2 excepts.
- **RQ-4: fixed.** Against `main`, version 1.1 changes H11 alone; H12 and H13 are identical to 1.0.
- **RQ-5: fixed** in E36 and F8. *SECTION*'s wording still lacks it (DC-L8).
- **RQ-6: fixed.** All three entries name both approvals and both fields, and GTWPE-D2's second quotation is attributed to PE40-INIT alone. One stop is still unlabelled (DC-L1).
- **RQ-7: fixed as written** (E52 to E55), on anchors the repository mostly does not hold (see below). Leaving *Proof logs (GTWPE-D1)* unedited is right: as C4 designed it, its list names what is not an artifact, not everything the Flow Manager writes.
- **RQ-8: fixed** (E06, E07, E45, F1). E12's "anything else" reads against item 1, which now excepts naming the prompt (see DC-L6).
- **Trend.** 8 distinct required defects become 2, which halves, so rule 5's first signal does not fire. Both sit in text the last repair added, as do ten of the twelve listed findings in whole or part, so its second signal fires. This was PLAN's one check of the repair's diff, so the cap (rule 2) sends §P to Nathan either way.

WHAT HOLDS, CLAIM BY CLAIM
- **C1** holds, except for DC-R1 and DC-R2.
- **C2** holds, except for DC-R1 and DC-R2.
  - The new texts quote their sources exactly. There are 11 block and 5 inline quotations, one of them inside Nathan's quoted approval. All are verbatim in PE40-INIT, the ledger, `analyze_approved_by`, HDE Governance, HDE Build Notes and `CHECKPOINT.md`.
  - HDE CRD Records §3.2's "the initial PF30 record is entered" is exact, and so is §9.1.1's "a Specification or Plan alone does not supersede canon".
  - The model-advice exception is the one MODIFICATION-20260930 records.
  - Canon supports the wider hold-back. HDE Governance §2.0.19 and §9.1.5 put the closure decision before PF10 drainage for the runtime flow, not only for epics, and PF10 is silent on this scope.
  - E37's widened anchor is check 6 exactly as C4's `draft-repairs.json` holds it. The published page is that draft except for two `RUN.md` links (C4 §E). The anchor is absent after its edit and clear of E38's on the next line.
  - `OVERLAP` passes.
- **C3** fails at DC-R2 (*The edits, by rule*) and at DC-R1 (the new two-sided check's triage row misses S4's cell). Everything else agrees:
  - 205 edits: 55, 17, 14, 28, 29, 21, 22 and 19, with 16 identity edits.
  - «H», «HD» and «HT», with their byte counts, and `ctl_check.py`'s copy hash.
  - 18 even tables in §P, and 14 handoff rows of six columns each.
  - X1.4's search: 5 lines on `main`, none on the new files.
- **C4** holds, with DC-L10 to DC-L12.
  - DR-1's words are answer 5's in the architecture record.
  - P9's rows have six columns.
  - P8's re-run counts follow from `ctl_check.py post` with the plan's own arguments: 5 + 3 + 6 = 14 checks on *Alpha 1*, 5 + 8 = 13 on the Hub.
  - The dated dry run's 89 lines are unchanged in place.
  - Each capture is the stated handback length plus one LF.
  - The two briefs hash as stated at `f77a77b`, which adds only them.
- **C5** holds for every row except B's L11, whose reason is half wrong (DC-L2). No other listed finding is required under §3: each ends loud, is cosmetic, is a record nit, or has no silent effect. A's L13 and B's L7 become a little likelier now that files given alone are a run, but the stop stays loud.

WHAT THE REPOSITORY DOES NOT HOLD, SO I DO NOT ASSUME IT
- **E52's clause** in *Authority and limits* ("writes `RUN.md`, the inputs, the captured"). C4 holds only §A ITEM-06's design sentence, "The Flow Manager writes neither artifact. `RUN.md`, the inputs, the captured reviews ...", which does not contain the anchor.
- **E53's cell.** C4 §A ITEM-02's layout row matches its anchor ("Each consistency review's return, captured unedited"). The repository holds neither what follows it in the body nor whether B5's capture step names the return `<NN>-consistency.md`, as E53's new text does.
- **E54's and E55's B5 steps**, the *Redo from canon* clause that refutes A's L9, and the sentence that refutes A's L8. No C4 record holds them.
- **The drains' kept `NO_CHANGE` condition**, on which K-11 and DC-L2 turn.

Each of these rests on the session's own reading of its fetches at 14:38Z and 14:57Z.

CHECKS I RAN, ALL READ-ONLY
- **The brief.** 12,631 bytes, sha256 `28b97bbd8e41b5442fb1b15104b15f3549301bd2f70775ec0d5538eeec8f1a96`. `c72afb6` adds only the brief to `9fefe96`. The working tree is clean and equal to `9fefe96` for every file reviewed.
- **The record.** At `9fefe96` it is 230,115 bytes and 2,032 lines. `origin/main` is `128836a`, the local ref; nothing was fetched. The branch changes nothing under `docs/pfcanon/` or `docs/prompt_ecosystem_management/`.
- **`edits_check.py`.** On `edits.json` it passes with exit 0: 8 members, 205 edits, 8 proof-log items. Each of the 11 `--inject` faults exits 1 with its own code among the failures. I took the exit codes by plain assignment, so they are the script's own.
- **The repair diff, by script over both commits.**
  - Changed: 18 GTWPE-FLOW-10 edits, one of them E37 with its anchor widened; TRIAGE-10-E04, E11 and E14; both S-HOLDs; both record prompts' E10.
  - Added: G-FLOW-10-E52 to E55 and APPLY-10-E19.
  - Nothing else changed.
- **The two `gtwpe/` files.** Each was diffed against `main` and against `1f73053`. GTWPE-D1 and the decision record's lines 4 to 64 are identical to `main`.
- **Also checked:** the quotations, tables, captures, hashes and X1.4's search, with the results above.
- **Not run:** the two record checks. The brief does not name them, and the check at `PLANNED` needs a scratch copy, which would be a file write.

METHOD AND DISCLOSURE
- **Commands.**
  - `git`: `show`, `diff`, `log`, `status`, `rev-parse`, `cat-file`, `ls-tree` and `grep`.
  - Shell: `grep`, `sed`, `awk`, `wc`, `sha256sum`, `stat`, `ls` and `cat`.
  - `python3 -I -B`, printing only.
  - `edits_check.py`, under `PYTHONDONTWRITEBYTECODE=1`.
- **No writes.** No file, no git command that changes state (fetch included), and no Notion, Drive, GitHub, session or agent action. The tree is clean, ignored files included, and `.git/index` is unchanged since 15:05:54Z.
- **Side effects that were not mine.**
  - The harness saved one oversized output of mine, about 30 KB of the record's repair diff (repository text, no prompt body), as `tool-results/b39rlqsa2.txt`. I did not open it, and read the diff again in narrower slices.
  - The repository's PostToolUse hook updated `.git/canon_relied_on_hook.json` at 15:43:13Z.
- **`D22`.** I read no prompt body. Every body clause quoted above is one the repository holds.
- **Connectors.** The Canva and Railway connectors still need re-authorization in claude.ai's connector settings (known noise in PE40-INIT). This check used neither.

## Canon relied on
- **`AGENTS.md`:**
  - the canon-first rule;
  - PF canon is read-only;
  - the truncation and retrieval guardrail, which is why the oversized output was re-read in narrower slices;
  - evidence attribution;
  - the CI-exempt review-scope note, which concerns automated code review, not this `D26-A` check that the brief commissions.
- **PF canon, from `docs/pfcanon/` on `origin/main` at `128836a`, by title and section:**
  - HDE Governance: §2.0.19, its *Post-closure maintenance ordering* bullet and the drainage bullets beside it; §9.1.1, whole, with *Historical drainage*; §9.1.5, whole; §9.1.2 to §9.1.6, by heading only.
  - Change Process Guide: §1.0.3 to §1.0.6; *Post-QA documentation drainage ordering (normative)*, whole; §3.5.1's historical-only sentence, found by search.
  - HDE CRD Records: §1, §2, §3.1, §3.2, §4.1 to §4.4, §5 and §6.
  - HDE Build Notes:
    - *Precedence, versioning, and scope* §1, §7 and §8;
    - 2.14, whole;
    - the headings of 2.1 to 2.38;
    - a search of the whole document for PF20, PF30, CRD Records, historical drainage and drain ordering, which finds no addendum on this scope, so under §8 permanent canon governs.
  - Not read, and nothing claimed of them: Plan Templates, HDE Phased Epics, the Change Process Guide's §1.1.2 and §6.3, and HDE Build Notes 2.38.
- **Governing documents, in `docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D20, D21, D22 with its refinement, and D26 A to F, read; D23 to D25 by heading only.
  - `modification-template.md`: *Rules the format exists to enforce*, 1 to 8, and the `reviews` ledger's comment.
  - `ecosystem-change-management.md`: its headings, and §4's catalogue by name.
  - `reviewer-prompt-template.md`: the second template, *ANALYZE and PLAN review brief*.
  - `notion-write-boundary.md`: *The policy, as issued*, and its headings.
  - `gtwpe/gtwpe.decision-record.md` and `gtwpe/gtwpe.handoffs.md` on `main`, each diffed against its evidence copy.
- **In flight:**
  - the record at `9fefe96`: §P whole; from §A, ITEM-02 to ITEM-05 and *What the analysis settles*; the front matter. Also its evidence and the two PLAN review records.
  - the request, on `main` at `128836a`:
    - `PE40-INIT-20261007.md`, whole;
    - `ERRORS.md`: E-010 in full, and the rows that GTWPE-D2 to GTWPE-D4 quote, by script;
    - `GTWPE-TARGET-ARCHITECTURE-20260929.md`: Nathan's answers 1 to 8;
    - `CHECKPOINT.md`, searched for one quotation.
  - C4's record (MODIFICATION-20261006-gtwpe-flow-manager): §A ITEM-01 to ITEM-06, §P *The new page*, and §E's resume; with `draft-repairs.json`.
  - C2's `edits-2.json` and C3's `edits.json`, for TW-APPLY-10's sentence.
  - MODIFICATION-20260930-gtwpe-tw-model-advice: its permitted exceptions.

DECISION NEEDED: this was PLAN's one check of the repair's diff, so §P goes to Nathan with DC-R1 and DC-R2 open, each a one-clause correction to new texts in `edits.json`, with the trend from 8 to 2 (both in the last repair's own text, D26-A rule 5's second signal) and DC-L1 to DC-L12 beside the 26 listed rows; repairing any of them is his to order.
