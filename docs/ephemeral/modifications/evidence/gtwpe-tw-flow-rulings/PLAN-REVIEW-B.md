3

**GTWPE-TW-FLOW-RULINGS-PLAN-B: PLAN full review 1 of 2 of MODIFICATION-20261007-gtwpe-tw-flow-rulings, §P at `1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f`.**

I found three required defects. Each is a small text correction, and none changes what the first live run would draft.
1. The three new decision-record entries say Nathan accepted, when he approved the analysis, consequences that only this plan adds.
2. The selection page's new *Current operation* says every change of an unclosed epic or CRD waits. The prompts hold back only PF10 changes.
3. In a run without a specification, a PF10 change that bears on PF20 or PF30 and also on another document gets no account of its waiting part, so it can be counted as drained.

The rest checks out:
- `edits_check.py` passes, and each injected fault fails it.
- «H», «HD» and «HT» match the committed files.
- Both record checks exit 0.
- The anchors agree with every record of the bodies that the repository holds.
- The new handoff table matches both sides of every row.
- The control texts' order and the readback arguments are sound.

## Required findings

### RQ-B1 (R2). GTWPE-D2 to GTWPE-D4 credit Nathan's approval of the analysis with the plan's own readings

- **Text.** The evidence `gtwpe.decision-record.md`, which X1.4 copies byte for byte:
  - line 104: "Nathan accepted these consequences on 2026-10-07, when he approved the analysis of MODIFICATION-20261007-gtwpe-tw-flow-rulings (its S-1, S-2, S-3 and S-8, and ITEM-07); his words are in that record's `analyze_approved_by`";
  - line 158: the same sentence for GTWPE-D3 ("its S-4 and S-5");
  - line 210: the same for GTWPE-D4 ("its S-6 and S-7").
- **Evidence.** "These consequences" include text that §A does not hold. §P presents that text as its own answers, which Nathan accepts only with the plan: *Findings on §A* says "each goes to Nathan with this plan, and his approval of it accepts the plan's answer".
  - **GTWPE-D2, *What is not an input*.** It says "the mode of a prompt that has modes" (P-4) and "an output location given as a path on a branch" (P-3). §A's *Permitted exceptions* say only "GTWPE-MGMT-10's `MODE`" and "an output location given as a path, which is a filename".
  - **GTWPE-D3.** Three of its points come from the plan, not §A:
    - the account of "every change, each PF10 addendum among them", and `RUN_NO_CHANGE` when "the account holds no change" (DR-1);
    - a single triage file that "is neither of GTWPE-D1's two artifact types" (*What the plan settles*);
    - "a record pass's verified `no changes`" (P-2).
  - **GTWPE-D4, line 202.** "A record prompt's no-change result is exactly `no changes`" (P-2).
  - `analyze_approved_by` names none of these.
- **Path, likelihood, consequence.** Normal path. Certain: the file lands as written at X1.4, and on `main` with #590's merge. GTWPE-MGMT-10 reads this binding record first and does not relitigate it. It would present a session's readings as consequences Nathan accepted at the analysis, which is the E-048 failure class. A later check against `analyze_approved_by` would not find them. The substance is not wrong; the provenance is.
- **Smallest correction.** Name both approvals in each sentence. For GTWPE-D2: "...when he approved the analysis (its S-1, S-2, S-3 and S-8, and ITEM-07) and then the plan (its P-3 and P-4) of MODIFICATION-20261007-gtwpe-tw-flow-rulings; his words are in that record's `analyze_approved_by` and `plan_approved_by`."
  - GTWPE-D3 does the same, naming DR-1, P-2 and the triage-file settlement.
  - GTWPE-D4 does the same, naming P-2.
  - The plan approval needs no date in the file. Fix «HD» again afterwards.
- **In the last repair's text?** Partly.
  - The three sentences are not among DR-1 to DR-5.
  - GTWPE-D3's "every change" text is DR-1's. The record says GTWPE-D3's last bullet follows DR-1, and line 142 is left unwrapped where a sentence was inserted.
  - GTWPE-D2's and GTWPE-D4's items are P-3, P-4 and P-2.

### RQ-B2 (R2). The selection page would say every change of an unclosed epic or CRD waits; the prompts hold back only PF10 changes

- **Text.** In *SECTION* (SEL-2's new text, W26), *Current operation*, second paragraph (record line 1409): "A change that belongs to an epic or a CRD the run's files do not show closed waits for that closure, and the run lists it."
- **Evidence.** Every other text holds back only PF10 changes:
  - G-FLOW-10-E41: "Hold back each PF10 change that belongs to an epic or a CRD that the run's files do not show closed";
  - S-HOLD (DRAIN-10/20-E15) and RECORD-10/20-E10: "A PF10 change is held back when ...";
  - GTWPE-D3, *Canon sets the timing*: "A PF10 change ...";
  - *SECTION*'s own first paragraph (record line 1384): "A PF10 change ... is held back, and no pass drafts it".

  After DR-1 the triage file reports closure for every change (TRIAGE-10-E09, E14). Yet only PF10 changes and an Epic Specification's PF20 record wait (E41):
  - a CRD Specification's record is inserted or updated whatever the CRD's closure (RECORD-20-E10, E12);
  - any other change a source carries is routed and drafted ("route each document the triage file names for a change not held back").
- **Path, likelihood, consequence.**
  - The path is a normal run whose specification belongs to an unclosed CRD or epic. Canon supports it: HDE CRD Records registers a CRD at intake and updates it in flight (§3.2, §4.2).
  - Certain as text; a reader is plausibly misled.
  - Nathan reads this page for how TW runs, and §A read it for closure. It would state a hold-back the prompts do not perform.
  - Nothing catches it: X4.3 reads the page back against the text as sent.
- **Smallest correction.** "A PF10 change that belongs to an epic or a CRD the run's files do not show closed waits for that closure, and the run lists it."

  The other direction is to mean every change. The Change Process Guide's *Post-QA documentation drainage ordering (normative)* is not limited to PF10, and S-4 says "a change held back". In that case E41, S-HOLD and RECORD-10/20-E10 widen instead. That reaches CRD records registered in flight, ledger E-010's open conflict, so that choice is Nathan's. The one-word fix needs no decision from him.
- **In the last repair's text?** Probably.
  - DR-1 says the control texts follow its widening to every change.
  - The same section's first paragraph kept "A PF10 change".
  - The committed history cannot show the sentence's earlier form, since §P was first committed at `1f73053`.

### RQ-B3 (R1, with an R4 outcome). Without a specification, a change's PF20 or PF30 part gets no account, and the change can be counted as drained

- **Text.**
  - TRIAGE-10-E11: "PF20 and the PF30 family are eligible only when a specification is among the files given."
  - TRIAGE-10-E04: "For each, give the eligible documents it bears on, or why it cannot drain in this run."
  - TRIAGE-10-E14: "and either the eligible documents it bears on, by canon file name without its version, or the reason it cannot drain in this run: no eligible home, such as PF10 itself; or PF20 or the PF30 family with no specification among the files."
  - G-FLOW-10-E40 records in `RUN.md` "the account its triage file gives each change ...: the documents it bears on, or why it cannot drain in this run". F11 says the same.
- **Evidence.**
  - G-FLOW-10-E16 and GTWPE-D4 (line 190) require that, without a specification, "each change that bears on them is accounted for as waiting for one".
  - §A ITEM-03, approved as S-4, lists "a PF20 or PF30 part with no specification in the run" among the reasons a change cannot drain, "for each document the addendum bears on".
  - No new text speaks of a part of a change; no edit uses the word "part".
  - Without a specification the triage cannot name PF30: B1 step 5 stops on "names an ineligible document". Its either-or gives a change that has an eligible home only that home.
  - HDE Build Notes 2.14 is such a change today. It belongs to no epic or CRD, and its *Terminology* binds both PF27 and PF30 ("PF27 and PF30 adopt the same terms on their next revision").
- **Path, likelihood, consequence.**
  - Normal path: a run with PF10 and no specification, which the plan supports (E16, GTWPE-D4, *SECTION*'s third paragraph).
  - The omission is likely in any such run with today's PF10. `RUN.md` and the pull request would show 2.14 drained into PF27, with no record that its PF30 part waits.
  - If PF27's drain returns `no redlines`, B3 and *Results* (E43, E50) count 2.14 "shown already represented". That breaks S-4 and GTWPE-D3's own "for each document the change bears on".
  - A run can then end `RUN_NO_CHANGE` with that part undrained. This is unlikely today, while most addenda are held back.
  - Drained guidance leaves PF10 at its next revision (HDE Build Notes, *Precedence, versioning, and scope* §7), so the PF30 part can be lost silently.
- **Smallest correction.**
  - In TRIAGE-10-E14, "and either the eligible documents it bears on ... or the reason it cannot drain in this run:" becomes "the eligible documents it bears on, by canon file name without its version, and, for any part of it that cannot drain in this run, the reason:".
  - In TRIAGE-10-E04, G-FLOW-10-E40 and F11, "or why it cannot drain in this run" becomes "and why any part of it cannot drain in this run". E24, E44 and GTWPE-D3's first bullet take the same words.
  - The endings then hold as written, because a change with a waiting part is not "shown already represented".
- **In the last repair's text?** Partly.
  - TRIAGE-10-E04 is DR-5's rewording.
  - DR-1 names E14 among the edits it changed.
  - `edits.json` was first committed at `1f73053`, so whether the either-or predates them cannot be shown.

**Against D26-A rule 5:**
- Of the required findings, RQ-B2 probably sits in the last repair's text, and RQ-B1 and RQ-B3 partly do.
- Of the listed findings, only L27's citation is the repair's own text. L1 and L3 are older text left stale by DR-1.

## Listed findings

- **L1** (normal; certain as text; the approved narrative misdescribes the edits; text DR-1 left unchanged). *What the plan settles* still gives the triage file "for each PF10 change". It still says `RUN_NO_CHANGE` comes "only when every PF10 change is shown already represented, or the run has no PF10 source and changes no document". DR-1's edits use every change and are stricter, so C6's "exactly as *What the plan settles* says" fails for a non-PF10 change that cannot drain.
- **L2** (normal; certain; low; no). `gtwpe.handoffs.md` 1.1 keeps "Rows H11 to H13, GTWPE-MGMT-10's, are carried unchanged", although this version changes H11.
- **L3** (normal; certain; low; stale after DR-1). TW-TRIAGE-10 keeps the title "Identify PF10 Drain Targets", although it now accounts for every change in every source.
- **L4** (normal; low; a non-file authorization could still be asked for; no). TW-APPLY-10 keeps "Other header, title or invocation-tag changes need separately explicit authorization and exact validated edits" (C3's APPLY-10-08) with no "given as a file", unlike the drains' S-HEADER-AUTH. The `D26-E` exception "a source's authorization" can keep it.
- **L5** (normal; low; a non-incremental version can no longer be set; no). APPLY-10-E11 removes "an explicit authorized target version when supplied" instead of taking it as a file, as S-1 does with Nathan's other inputs.
- **L6** (normal; low to medium; loud S2 stop; no). G-FLOW-10-E06, E12 and E45 stop "an execution prompt that gives anything beyond `RUN` or `RESUME` and files". They do not except the prompt to run, which GTWPE-D2 and S-1 except. Separately, E07 makes `RUN` or `RESUME` item 1, and nothing says what happens to a message of filenames alone, which is what ruling 1 literally describes.
- **L7** (normal; low; loud; no). TRIAGE-10-E11 makes PF20 and PF30 eligible when "a specification is among the files given". GTWPE-FLOW-10 routes them only when "the run has a governing specification" (E14 to E16). A specification given only as a source makes the triage name PF30, and B1 step 5 then stops.
- **L8** (latent; low; loud; no). RECORD-20-E18 returns `no changes` only when "the sources require no change to any PF30 volume", while E41 gives each PF30 volume its own pass. With a second volume, a pass could neither return `no changes` nor write its assigned volume. PF30.1 is the only volume today.
- **L9** (normal where a closure decision is missing; medium; loud `RUN_STOPPED`; no). RECORD-10-E20 makes a waiting Epic record with no other change a missing-input stop. So a run with an unclosed Epic Specification whose routed PF20 changes need nothing ends `RUN_STOPPED`. K-10 says only that the run "drafts without that record, and lists it as waiting".
- **L10** (normal; low; visible inconsistency, or K-7's disagreement; no). *What the plan settles* says a new closure decision "starts a new run", but no edit says so. GTWPE-D2 counts a closure decision among Nathan's own decisions, and E48 and E49 let a resume add "a decision file". After such a resume, the triage file still reports the change unclosed.
- **L11** (direct use; medium; a direct drain skips every addendum of an epic not shown closed; no). S-HOLD and RECORD-10/20-E10 also bind direct invocations, where there is no triage file and the prompt judges closure itself. That carries S-4 past the run, and P-1 says only "in the members §A already changes".
- **L12** (direct use; low; as K-11; no). K-11's reason rests on DC-L1, which covers only the drains' `no redlines`. The record prompts' exact `no changes` is this plan's own choice (P-2).
- **L13** (normal; low; a surviving non-file passage would go unnoticed; no). The readback's `D26-E` table drops some of §A's measured ruling-1 terms: `decision`, `direction`, `statement`, `the change`, `supporting material`, `invocation` and `handoff`, and for GTWPE-FLOW-10 also `ask`, `request` and `supplied`. §A's *Scope* counts ruling 1 in GTWPE-FLOW-10's *B5* and *Redo from canon*, which have no edit and no row in *§A's passages, and how the plan meets each*. C4's §A puts B5's reach at "the finding as supporting material", which is a file.
- **L14** (normal; certain; low, bookkeeping; no). RECORD-10/20-E09 to E21 are tagged R4 and ITEM-05 only, although *The edits, by rule* says "(R4, R2)". X5 sets ITEM-03 by the edits tagged with it, so the record prompts' hold-back text falls outside ITEM-03's disposition.
- **L15** (normal; certain; low; no). X5 marks ITEM-06 `VERIFIED` when the PF09 row and TRIAGE-10's routing sentence "read back as *The new pages' checks* expects". That section sets no check for the PF09 row (template rule 4).
- **L16** (normal; low; a held-back change recorded as represented; no). E36 and F8 record `no redlines` or `no changes` as "each change the triage file routed to it is already represented". PF20 and PF30 are routed by the specification rule, not for a change. So a held-back change that the triage file names for PF30 could be read as routed (K-7's family).
- **L17** (normal; low; loud if a check finds no base blob; no). After the reorder, no B1 step says when a routed document's canon path and base blob enter `RUN.md`; the old step 6 wrote "`RUN.md` with the triage". No readback searches kept text for B1 step numbers. The two cross-references the repository records ("as B1 step 5 does", "ends as B1 step 7 does") are handled by E38 and E43.
- **L18** (normal; medium in a small context; loud S1 stop; no). S1 is not sized for the triage pass, which reads PF10 (489,946 bytes), every source and the target owners' content. K-9 sizes only the record passes.
- **L19** (failure path; low; loud D26-B return; no). Two failure windows leave mismatched selections:
  - A failure after X1.4's commit and before X3 lands the 1.1 table and decision record on `main` with #590's failure-record merge, while the old prompts stay selected. X1.4's restore is only a rollback column, not part of *Failure path*.
  - If W25 lands and W26 fails, the new Flow Manager is selected with the old TW prompts.
- **L20** (disclosure; low; no). K-24 names three members, but the PE Metaprompt's general rules were also read only before the compaction (lines 36 to 128, 173 to 207 and 291 to 353). After it, only its title, edit time and line 194 were read. This mode's saves, two of them the PE Metaprompt's body, were also left to teardown without an attempt to delete them (`D22` condition 4). Both facts appear in *Harness files*, not in K-24.
- **L21** (normal; certain; low; no). K-21 sets aside the PE Metaprompt's handoff rule. That is not among the workarounds recorded for *Relation to the PE Metaprompt* (the pilot's PF-6). §P rests it on *Read these* and GTWPE-D2, and the re-versioned GTWPE-MGMT-10 does not record it there for the next author.
- **L22** (procedure; certain; disclosed; no). Template rule 1 says a mode that finds an upstream section wrong "does not carry on past the finding". §P carries on past P-1 to P-5 (K-18), as C3 and C4 did with Nathan's acceptance. P-1 and P-2 are larger than theirs: hold-back text in four members, and F8.
- **L23** (normal; low; loud; no). Two GTWPE-MGMT-10 intake gaps:
  - E06's "Nathan's words in those files are the request" leaves no request text when the request is only a run's `RUN.md` (H11) or a drift-check record.
  - E03's "its subject, given only as files" reads against the Modification ID that `PLAN` and `EXECUTE` take.
- **L24** (normal; low; no). Non-file fields remain in handoffs:
  - F2's and the invocation's "that it runs as a pass inside the session Nathan started" is not among GTWPE-D2's exceptions.
  - The *Common rules*' "Every handoff passes the prompt to run and files" also reads onto the returns F3, F5, F8, F9 and F11.
  - *SECTION* gives a resume as "`RESUME` and the run's `RUN.md`", without E48's decision files.
- **L25** (normal; low; the backstop is X1.3 (g)(10); no). `edits_check.py` does what its docstring says, and each injected fault fails its own check, but its word lists are narrow:
  - EXCLUDED's `\bultra\b` passes the effort level "Ultracode", and the list names no model or product.
  - SELECT tests one stem, VALUES tests only «V», and BARE covers six extensions.
  - None of these gaps is used by the new texts.
- **L26** (record; certain; low; no). §P says that, apart from the anchors, it names each body only by its headings, first line and last words. *The two-sided check* quotes about ten kept clauses from the live bodies.
- **L27** (record; certain; low; partly DR-1's). Two citation slips:
  - DR-1 cites "answer 2" for "any other file or collection of source material that contains the change context", which is answer 5.
  - GTWPE-D2 cites E-045 for ruling 1's second sentence, which only PE40-INIT holds.
- **L28** (normal; low; no). G-FLOW-10-E18 gives a record pass "each PF10 change that bears on it" without "not held back", which DR-3 added to E14 and E15. The record prompts' E10 holds those changes back themselves.

## The claims, tested

- **C1 holds.**
  - Nothing is added beyond §A's items, members, targets or Notion writes: eight members with three writes each, W25 (the catalog's two rows and checked-through commit), and W26 to W29.
  - His approval is carried: ITEM-07 (G-MGMT-10-E03, E04, E06, E07, E15, E16); S-7 with DC-L2, quoted in GTWPE-D4; DC-L1, since no edit touches the drains' no-change exit and F3 keeps `no redlines`; Q-1 (a), on the selection page and all three notes.
  - The one reach it does not state is S-HOLD in direct invocations (L11).
- **C2 holds, with two exceptions.**
  - On the anchors' evidence it holds for R1, R3, R4, R6 and R7.
  - The exceptions are RQ-B3 (R2's account of a part) and RQ-B2 (a control text).
  - No new text adds model, effort, product or placeholder text, and PROOF holds every GTWPE-D1 phrase.
- **C3 holds row by row** for F1 to F11 and H11 against the edited sides. The exceptions are RQ-B3 (E16's waiting account has nothing in the triage file to consume), L7 and L8.
- **C4 is half true.** It is verbatim: all 14 quotations (11 block and 3 inline) are in the sources named, with one attribution nicety (L27). It fails "nothing more" (RQ-B1).
- **C5 holds.** P-1 to P-5 are each correct, and none adds an item, member, target or write. P-1 leaves its reach into direct invocations unstated (L11).
- **C6 fails in three places:** RQ-B2, RQ-B3 and L1.
- **C7 holds, with gaps L15 and L19.** Every Notion write has a readback that can fail, the failure path is D26-B's, and no rollback needs a prompt body.
- **C8 holds.**
  - SEL-1 before SEL-2 and CAT-FLOW before CAT-MGMT are safe for any «V», because each two-line old text holds a title cell.
  - No old text occurs in an earlier new text of its call.
  - The notes stay within the current TW sections.
  - Every `--has` and `--row` argument of X4.4 and X4.6 occurs in A1-NEW or HUB-NEW as `ctl_check.py` reads them.
- **C9 mostly holds.** K-10 understates its case (L9), K-11's reason is only half DC-L1's (L12), and K-18 is a disclosed departure from template rule 1 (L22). PO-1 to PO-5 and *Explicitly not in scope* are complete.

## What this review ran

- **The brief.** sha256 `e811945c7f0f7b0df6827416df367af8d003e2226b6bae11372781b47804f48c`, 13,242 bytes. `f77a77b` adds only the two briefs to `1f73053`. `origin/main` is `128836a`.
- **`edits_check.py`.** PASS: 8 members, 200 edits, 8 proof-log items, exit 0. Each of the 11 `--inject` faults exits 1 under its own code.
- **Hashes.** `edits.json`, the two evidence files and `ctl_check.py` have sha256 equal to «H», «HD», «HT» and the stated copy hash. Each equals its working-tree copy.
- **Record checks.** `modification_validate.py` and `gtwpe_record_check.py` run in check mode on the record as committed, at `PLANNING`: both exit 0, 1 of 1 passed.
- **X1.4's `D26-E` search.** No hit on the two new files or on `gtwpe_record_check.py`; 5 lines on `main`'s current handoff table.
- **Anchors.**
  - 63 of §A's 183 distinct quotations fall inside anchors once whitespace is collapsed, with no near miss.
  - 25 anchors match text that the C2, C3 and C4 records hold as current, and none matches only text an earlier edit replaced.
  - No two anchors of one member overlap so as to make a later replacement miss. Two shared prefix or suffix pairs (G-FLOW-10-E13 and E15; E50 and E51) sit in different cells.
- **Control texts.** No bare file name, and every placeholder is defined in *Values*.
- **First live run, traced.**
  - Its files are on `main`: PF10 v13.5 (489,946 bytes, 38 addenda), the HDE-EPIC040 Specification v1.1 (64,553), and its closure decision v1.2 (18,136, `decision: CLOSE`). PF20 holds no HDE-EPIC040 record.
  - The trace found no normal-path stop beyond S1 sizing (K-9, L18).
  - It ends `RUN_REVIEW_READY`, with every epic-bound addendum not shown closed listed as held back.
- **Side effects.**
  - I wrote no file, read no Notion page or prompt body, and changed no git state.
  - My early `python3 -I -c` reads ignore `PYTHONDONTWRITEBYTECODE`. I confirmed they wrote no bytecode: the repository is clean including ignored files, and no new stdlib `.pyc` exists. Later reads used `-B`.
  - The two record checks are beyond the brief's named tools; they write only under `--selftest`.
  - `PLAN-REVIEW-A.md` (25,303 bytes) appeared untracked at 14:23:27Z, written by the session, not by me. I did not open it.
  - The Canva and Railway connectors still need re-authorization in claude.ai's connector settings (known noise in PE40-INIT). This review used neither.

## Canon relied on

PF canon, read from `docs/pfcanon/` on `main` at `128836a` (unchanged since `fffadb5`), by title and section:
- **HDE Governance**: §2.0.19, the *Post-closure maintenance ordering* bullet; §9.1.1, with *Historical drainage*; §9.1.5; §9.1.6.
- **HDE Build Notes**: the front matter, and *Precedence, versioning, and scope* §1 to §8; 2.14 (*Binding*, *Reference posture*, *Terminology*); 2.38 (*Rule* 1 to 3).
- **Change Process Guide**: §1.1.2, §3.5.1, §6.3, and *Post-QA documentation drainage ordering (normative)*.
- **Plan Templates**: §2, *Historical-only posture (normative)*.
- **HDE Phased Epics**: §0, *Drain posture* and *Build Notes posture*.
- **HDE CRD Records**: §1, §3.2, §4.1, §4.2, §4.4 and §6.
- The file names in `docs/pfcanon/`, for eligibility: every PF09 phase file and PF30.1 carry `Canon` in their names.

Other governing documents, by file and section:
- **`AGENTS.md`**: the canon-first rule; PF canon is read-only; the truncation and retrieval guardrail; the CI-exempt review-scope note, which concerns automated code review, not this `D26-A` review.
- **`docs/prompt_ecosystem_management/gcfpe.decision-record.md`**: `D21` (A to E); `D22` (the ruling, conditions 1 to 5, and the refinement on deleting session files); `D26` (A to F).
- **`modification-template.md`**: *Rules the format exists to enforce* 1 to 8, and the §P template.
- **`ecosystem-change-management.md`**: §2, Step 1 (the classes).
- **`reviewer-prompt-template.md`**: the header and the second template, *ANALYZE and PLAN review brief*.
- **`notion-write-boundary.md`**: *The policy, as issued* and *The default is read-only*.
- **`gtwpe/gtwpe.decision-record.md`** (GTWPE-D1) and **`gtwpe/gtwpe.handoffs.md`** 1.0 on `main`, each diffed against its evidence copy.
- **The request, on `main` at `128836a`**: `PE40-INIT-20261007.md` (whole); `ERRORS.md` rows E-043 to E-054; `GTWPE-TARGET-ARCHITECTURE-20260929.md` (the target's §1 to §11, the answers 1 to 8, and the later directions); `CHECKPOINT.md` §8.
- **Earlier records**:
  - MODIFICATION-20261006-gtwpe-flow-manager: §A ITEM-01 to ITEM-03, §P *The new page*, its listed findings, and `evidence/gtwpe-flow-manager/draft-repairs.json`;
  - `evidence/gtwpe-tw-repository-io/edits-2.json` and `evidence/gtwpe-tw-document-rules/edits.json`;
  - MODIFICATION-20261005-gtwpe-writing-side, its authoring line;
  - MODIFICATION-20260929-gtwpe-pilot, PF-6;
  - MODIFICATION-20261006-gtwpe-tw-document-rules, *Findings on §A* and L14.

Not read: any Notion page or prompt body, including GTWPE-MGMT-10 100526.2 itself, which this record cites only through §P's quotations of it. No PF canon was read beyond the sections named.

IN FLIGHT
