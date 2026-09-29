2 distinct confirmed REQUIRED findings

Review GTWPE-P1R-R1-A of `design/GTWPE-DESIGN-v1.1.md` at `a33647c`. The file is blob `fe992b4e…`, 107,613 B, 1,153 lines, sha256 `14365db0…`. This is full review 1 of 2 for PLAN (D26-A).

- **Both required findings are in GTWPE-MGMT-10's drift check (§11.4 A0).** That is the step meant to keep the change prompt in step with its sources. Both failures are silent, not loud stops.
- **The validator claim (C2) reproduces.** A pilot record written as §11.3 and §11.4 say passes `modification_validate.py` at ANALYZED, PLANNED, EXECUTING and COMPLETE once `tool` is in `TARGETS`.

## Required findings

### RF-1 · R4 · A0 cannot see the next version of either lineage source

- **Text.**
  - §11.4 A0: "Compare the PE Metaprompt page and the GCFPE-MGMT-10 source page with the catalog's pins, at the minute resolution of a Notion search that returns titles and edit times and fetches no body."
  - §11.7 pins each source by "page ID and … edit time".
  - No step ever re-pins them. X4 moves only the last-close commit and the prompt rows.
- **Evidence.**
  - **The PE Metaprompt's next change arrives as a new page.**
    - `PE-METAPROMPT-TEST-20260924.md`, *Where the fixes go*: "it follows C-VERSION, so a changed body gets a successor page, which the register then binds. Its repair is therefore a GCFPE-MGMT-10 Modification. The queued MGMT-10 promotion Modification can carry it."
    - The decision record's D23 successor, "`D23-G` reaches the PE Metaprompt", says the same: "The PE Metaprompt itself follows C-VERSION".
    - `prompt-body-content-policy.md` applies the successor-page rule "from the release after 091426.1".
    - The pinned page `3db4590a…3f77` is then never edited, so A0 finds nothing.
  - **The source's next change also lands off the pinned page.**
    - Open item 3 of `pe-succession/pe36-to-pe37.md` queues "Promotion of the MGMT-10 proposed body". It is due now: the follow-up it waited on is COMPLETE.
    - D20-B has the new body replace "the current GCFPE-MGMT-10 in place". C-VERSION gives a changed member a successor page. Later GCFPE-MGMT-10 fixes are made on one of those pages, not on `3e34590a…8106d`.
    - The dry run itself searched for "no later versioned GCFPE-MGMT-10 page" (DRY-RUN-P1r check 4). It also recorded the live 091426.1 page edited after the pin, at 2026-09-24T15:38. A0 carries no such search.
  - **GTWPE-MGMT-10 would switch PEs without a trigger.**
    - It authors "through the selected PE Metaprompt" (§11.10). §4.4 *Dependencies* adds "with the kickoff's workarounds until its repair".
    - Once the register binds a successor, the session silently uses it, or the superseded page if it reads the pin. A0 reports no drift either way.
    - §9.4's D8 handling ("its drift check finds one … Its ANALYZE runs the D26-E search") never fires, and neither does E-019's fix.
    - A0's check, "Each change found is recorded", passes when nothing is found.
- **Path, likelihood and consequence.**
  - Path: normal. It is every ANALYZE after the PE repair or the promotion.
  - Likelihood: medium to high. Both are queued GCFPE work, and E-007 routes the PE repair to the promotion Modification.
  - Consequence, all silent:
    - GTWPE bodies are never searched for text the repaired PE contradicts.
    - The kickoff workarounds are never retired.
    - GCFPE-MGMT-10's fixes never reach GTWPE-MGMT-10.
  - This is the D8 failure the design says A0 closes.
- **Smallest correction.**
  - For each source, A0 also runs a title search on its stable name (`PE Metaprompt`, `GCFPE-MGMT-10`) with highlights off, and reads the GCFPE register's current selection.
  - A page other than the pinned one that is selected, or edited after the pin, is a trigger finding.
  - X4 re-pins a source's page ID and edit time when the Modification adopted its change or Nathan declined it.
- **In text the last repair added?** No. A0 and the pins are unchanged since `d087e4d`.
- **Refutation tried.**
  - An in-place edit would be caught. But D23's successor makes the PE follow C-VERSION, and D20-B lands the promoted body on the live page.
  - A title search would show a later page. But A0 names no such search; only the dry run ran one.

### RF-2 · R1 · X4 moves the pin past commits no A0 examined

- **Text.**
  - A0: "Run `git log <the catalog's last-close commit>..origin/main` over the watched paths (§11.7)".
  - X4: "Update the catalog block. Its last-close commit becomes X3's merge commit."
- **Evidence.**
  - A0 runs when ANALYZE starts. The merge comes days later, after Nathan's two approvals, the reviews and his merge.
  - `git log M..origin/main` excludes every ancestor of M. No step re-scans the gap: X3 re-runs the gates, not the drift check.
  - So every watched-path commit that lands on `main` between A0 and the merge is never reported. How X3 identifies "the merge commit" is not stated either; taking `origin/main` at X3 would widen the gap.
  - **Reproduced on `origin/main`:**
    - `git log 3d81a7f..origin/main -- 'docs/pfcanon/PF10-*' AGENTS.md` lists seven commits of 2026-09-27.
    - The same command from `69cea25`, standing in for a merge commit, lists none.
    - The six commits in between include `b7b0dee`, PF10 addendum 2.30 (PF10-CITE-001). That is the rule behind the GTWPE's own V9.
  - **The watched paths move daily.** The §11.7 paths took 38 commits on `main` from 2026-09-20 to 2026-09-28. At least one landed every day from 09-21 to 09-27, and ten on 09-27 alone.
- **Path, likelihood and consequence.**
  - Path: normal. It is every Modification's X4, the pilot's included: the pilot's pin moves from P2(b)'s commit to its own merge commit.
  - Likelihood: high.
  - Consequence, silent: the watched-path trigger loses whatever lands while a Modification is open. That is exactly the canon and governing-document drift A0 exists to catch.
- **Smallest correction.**
  - A0 records in §A the `origin/main` commit it examined.
  - At X4, before moving the pin, run A0's `git log` over the watched paths from that commit to the merge commit's first parent.
  - Carry each change found to Nathan as a trigger finding in the X5 return.
- **In text the last repair added?** Yes. The sentence is DRr-4's repair. The gap predates it: v1.1 as authored set the pin "to `origin/main` once the record has merged", which skipped the same window and more.
- **Refutation tried.**
  - "The next A0 starts where the last close ended." It starts after the merge commit, whose ancestors `git log A..B` excludes.
  - "The window is short." It spans two approvals and a merge, and the watched paths changed on each of the last seven days.

## Listed findings

Each line gives the finding, its path and likelihood, its consequence, and whether it sits in text the last repair added.

- **L1.** §11.6 and §16 count capturing a worker's return from its body-holding transcript as "the check in hand". That is defensible under D22's purpose test and disclosed, but it strains condition 4 ("never read again"). RQ-3's own remedy avoided the worker's transcript, and the cold run's return already reaches W1 as the Agent result · normal (P3), certain · a disclosed second read · repair text: yes.
- **L2.** The D26-D token measure (§11.3; §12.5; plan v1.2 §16.3) exists only in the transcripts' per-call usage, which P1 summed by script (CHECKPOINT §9.5). In P3, W1's transcript and the cold run's hold the GTWPE-MGMT-10 body, which §11.6 says is "never read again"; neither §11.6 nor §16 names this read · normal, likely · an undeclared second read, or no measure for the twice-the-estimate stop · no.
- **L3.** The tier rule needs judgement ("provably changes neither"; "what a member produces or does"). By its letter the pilot is tier 2, since the reader fixes H2's record format and the `UNSUPPORTED_INPUT` codes ("changes a §6 handoff … or a result code"). §13.2 says tier 1, and tier 2 would demand H2's consumer side, which P4 builds · normal (P3), certain · a pilot finding, and tiers set by judgement · no.
- **L4.** "Read from §6" does not give the same closure twice. §6 is keyed by stage, not member, and H2 names only S2 although the record prompts' R2 and drafters also work from S1's records. The result codes that set `state_sharers` are not in §6 at all · normal, medium · a narrower gate, found at a later run · no.
- **L5.** GTWPE-MGMT-10's body must cite "§6's handoff table", "the method P1 used (§17)" and "until P4". §4 *References* and HDE Governance §9.1.6 let a body cite neither a version-named ephemeral record nor a build phase. P4 then gives the table a second home in `gtwpe-run-procedure.md`, and no step repoints the landed GTWPE-MGMT-10 (DERIV-001) · normal after P4, medium · closure and tier read from a frozen copy after the first handoff change · partly.
- **L6.** X5 opens no pull request for the COMPLETE record ("Nathan merges it when he chooses"), and X2's PR is already merged. The GCFPE's X7.6 opened a close-out PR · normal, certain · the COMPLETE record stays on the branch · yes.
- **L7.** PROMOTION_CHECKPOINT_REQUIRED has no route. X5 sets COMPLETE, and only EXECUTE's X4 may change the catalog (§11.7), so Nathan's later "select it" has no step to carry it out · normal when the plan does not name the selection, certain there · a loud DECISION NEEDED with no next action · yes.
- **L8.** Pilot findings have no home in the record. §13.2 records them "before it acts" and V3 lists them, but template rule 1 confines each mode to its own section, and the cold run's findings arrive after §A is written · normal (P3), certain · W1 improvises · no.
- **L9.** Nothing checks GTWPE-MGMT-10's workers before P4 builds `postcheck`. The cold-run worker reads a body telling it to commit and push (A1, A7) under a brief saying write nothing. Reviewers hold Write, Notion-write and merge tools (CHECKPOINT §4.2). P1 checked by hand; §13.2 names no such check · normal (P3), low · an unseen write · partly.
- **L10.** Notion duplication is asynchronous; the connector's description says "do not rely on the new page … to be populated immediately". §11.5 edits the duplicate at once and does not limit the method to one exact search-and-replace per anchor · normal (every prompt change), low to medium · an edit fails loudly; or a whole-page `replace_content` retypes unedited text (EVID-001) and passes a readback that checks only identity lines, each edit and the headings. That is §16's listed consequence, from a likelier cause · no.
- **L11.** §11.5 never retitles the duplicate, and its readback omits the title and parent, which §12.2's readback checks · normal, medium · a successor page carrying the old version's title · yes.
- **L12.** An edit is "its shortest unique anchor and its new text" (PL1). For a REPLACE or DELETE longer than the anchor, the extent is recorded nowhere, and "new text present, anchor absent" cannot see leftover or over-deleted text · normal, low (PF03 §8's smallest-unique-range reading avoids it) · a silent partial edit · no.
- **L13.** D-10 and §12.2 let GTWPE-MGMT-10 "create child pages … and write nothing else", while §11.5 also edits the duplicate after creating it · normal, certain · a strict session stops · no.
- **L14.** §11.6 lets no reviewer fetch a prompt body, so a PLAN review of a prompt change cannot check an anchor's uniqueness or its new text in place · normal (prompt changes), certain · weaker reviews of the changes Nathan most needs · no.
- **L15.** S1 refuses on "that result's … path", but no record shows a Notion search result carrying a path. DRY-RUN-P1 check 5 and DRY-RUN-P1r checks 4, 5 and 7 record titles, timestamps and IDs, and the connector documents `path` for fetch only. Without a path, S1 either fetches (RQ-3's unreported read again) or falls back to the title pattern. The pattern misses "PE Metaprompt 091426.1", the source page's title and seven other HDE TW titles (CHECKPOINT §4.6). A missed body is written to `source/NN-<name>.md` and pushed. One read-only search settles it, and a search scoped with `page_url` to `AI Prompts` tests ancestry without a path field · normal (Path A with a Notion page), low · a silent D22 breach (R3 class) if the premise fails; I could not test it without a Notion call · yes.
- **L16.** A Notion input named by URL alone, the usual form, now stops, because S1 needs its title to search · normal, medium · a loud `INPUT_MISSING` or `notion-page-unidentified` · yes.
- **L17.** The E-022 refusal has no named home. S1's tool lands at P3, but the refusal's cases sit in P4's selftest (§13.3), and none of `gtwpe_redline.py`'s nine subcommands classifies a page. Adding it to `gtwpe_read.py` at P4 would change a landed member outside GTWPE-MGMT-10 · normal (P4), certain · a build-time question · partly.
- **L18.** §12.2 has P4 update the catalog block under G2, while §11.7 lets only EXECUTE change it after P2(b). No Modification moves the pin at P4, so the first A0 after P4 reports P4's own commits under the watched `gtwpe/` path as drift · normal (P4), certain · a contradiction, then noise · partly.
- **L19.** The Notion lineage pins are never re-pinned. A source or PE change that one Modification adopted, or Nathan declined, is reported again by every later A0 · normal, certain after the first change · recurring noise · yes.
- **L20.** A0 does not fetch before `git log`, so a long-lived session's stale `origin/main` hides recent commits · normal, low · a silent miss · no.
- **L21.** The watched paths omit sources the design relies on that can change: `skill-packaging-and-delivery.md` (the skill route), `authoritative-surfaces.md` (D10) and `.github/pull_request_template.md` (the canon PR body, §5.2) · normal, low · unseen drift · no.
- **L22.** After P4, §7.4's `capture` needs nonce markers, and a miss is `RUN_BLOCKED: CAPTURE_UNAVAILABLE`. The second template's fixed §6 carries no nonce, and GTWPE-MGMT-10 has no `RUN_BLOCKED` result · normal after P4, certain · loud · yes.
- **L23.** H12 and H13 carry approvals only. No row covers the resume after a merge or install (H10's analogue) or Nathan's selection after PROMOTION_CHECKPOINT_REQUIRED · normal, certain · resume by judgement · no.
- **L24.** D-14 names the kickoff's "one branch" but not `glow-write-boundary`'s "One branch per session, one PR per branch", which W1's second branch also crosses. G1 would waive the installed skill's rule without naming it · normal (P3), certain · yes.
- **L25.** The pilot changes no prompt page (§16). §11.5's route (duplication, edits, readback, selection, PROMOTION_CHECKPOINT_REQUIRED) therefore first runs at GTWPE-MGMT-10's first repair of its own page, though Nathan's G0 words are "so I can repair the rest of the prompts" · normal, certain · the route he needs is unproven when repairs begin · no; the plan fixed the pilot.
- **L26.** §11.8 closes a prompt repair as ECOSYSTEM_CHANGE_COMPLETE, with its items VERIFIED, on publication readback alone. HDE Governance §9.1.6, in the sentences PF10 2.31 keeps, separates published selection from observed runtime correction. It keeps the failing case for focused retest and says publication readback is not runtime validation. The design follows §9.1.6 elsewhere · normal (prompt repairs), certain · a repair reported done before any run shows it · no.
- **L27.** A prompt-only Modification's selection (X4) and completion wait on Nathan merging a PR that holds only the record (X2, X3). D21-C and his ruling of 2026-09-28 ("they cannot gate") treat such a PR as storage, and `glow-write-boundary` says not to ask him to merge "as a matter of routine" · normal, certain for prompt-only changes · a repaired prompt stays unselected until a storage PR merges · no.
- **L28.** D26-B's failure record "reaches `main`, in a record pull request", and it keeps "the freeze". §5.3, §11.4 and §12.4 name neither the record's destination nor any GTWPE freeze · failure path, low · loud · no.
- **L29.** §12.2's readback for P2(b) and P4 checks the title, parent, identity lines and headings only. Text that Notion's Markdown conversion alters inside a section passes, although §9.1.6 asks to "read back complete changed published bodies" · normal, low · a silently altered rule on a path the pilot does not run · yes.
- **L30.** `targets-check` enforces only the "(b) given" half of the PF27 rule. "Only for a template PF27 owns that the specification changes" rests on the manager, so a run with (b) and (c) can draft PF27 for PF10 2.14's terms · normal (Path B), low · G3 shows it · no.
- **L31.** §1 places "one title-only search at 2026-09-28T14:42Z" in P1r, but P1r began at 20:19Z (CHECKPOINT §10.1); the search belongs to §9.7 · record accuracy, certain · no effect at run time · no.

## The attack list, answered

- **A1.**
  - The "check in hand" reading holds in purpose and is disclosed, so it is not silent. It strains condition 4, and RQ-3's reasoning preferred not re-reading the worker's transcript (L1).
  - The cold run's return needs no transcript read unless it must be committed.
  - Something else does re-read a body-holding file: the token measure (L2).
- **A2.**
  - A session cannot apply the tier rule without judgement (L3).
  - "Read from §6" does not give the same closure twice (L4).
  - At P4 the table gains a second home, and GTWPE-MGMT-10 keeps pointing at the first (L5).
- **A3.**
  - **The validator walk passes.** I built synthetic records in memory exactly as §11.3 and §11.4 say:
    - `format: "2.1"`, `ecosystem: GTWPE`, `targets: [tool]`, tier 1, and one class-B part;
    - a ledger holding an ANALYZE dry run, then a PLAN dry run and full review;
    - `item_count_at_approval` set from PLANNING on.
  - The real `check()` failed each one only on `tool`. With `tool` added to `TARGETS` in memory, all four statuses pass. No further field, state or approval is missing at the validator level.
  - **Around the two merges:** the pin (RF-2), the missing close-out PR (L6), the missing promotion route (L7), no home for pilot findings (L8) and no worker post-check (L9).
- **A4.**
  - No D22 breach found.
  - The rollback is real, but it takes a new Modification, because only EXECUTE's X4 writes the catalog.
  - The weak points are L10 to L14.
- **A5.**
  - Identifying the page by title and ID works.
  - The refusal's path half rests on an unverified field (L15).
  - The title pattern misses the PE Metaprompt's title and the source page's title. I could not check where D17's archive sits.
  - An input named by URL alone now stops (L16).
- **A6.**
  - No section still describes v1.0's order.
  - §2.2, §3, §12.1, §12.2, §12.5 and §13 agree with plan v1.2 §16.1, and §12.5's rows equal §16.3's.
  - The build plan has two seams: L17 and L18.
- **A7.**
  - A0 cannot detect its triggers reliably: RF-1 for the two Notion sources, RF-2 for the watched paths.
  - Minute resolution is enough for an in-place edit (DRY-RUN-P1 check 5).
  - Before the first Modification closes, the last-close commit is `origin/main` as P2(b) writes the block (§11.7). The pilot's X4 then skips its own window (RF-2).
  - See also L19 to L21.
- **A8.**
  - §4.4 agrees with §11 on writes, reads, exclusions and results.
  - H12 and H13 carry approvals only (L23).
  - D-13 and D-14 match §13.2, but D-14 misses the skill's branch rule (L24).
  - §7.4's nonce capture and §11.4's interim capture diverge after P4 (L22).

## Claims

| Claim | Holds? |
|---|---|
| C1 | Yes. E-019's trigger is placed, but it does not work (RF-1) |
| C2 | Yes for the validator, reproduced. Every step names a check, but A0's check passes when it finds nothing (RF-1, RF-2) |
| C3 | No. Tier and closure need judgement (L3, L4), and the drift check misses both Notion sources (RF-1) and in-flight commits (RF-2) |
| C4 | Partly. No body is copied. Rollback by re-selection needs a new Modification. §11.6 meets D22 in purpose but strains condition 4 (L1, L2) |
| C5 | Yes as written. S1's path half is unverified (L15), and PF27's template half rests on judgement (L30) |
| C6 | Yes, except that the destination rule's letter does not cover editing the duplicate (L13) |
| C7 | Partly. W1 follows the published body and the cold run tests it cold, but the prompt-page route is never exercised (L25) and pilot findings have no home (L8) |
| C8 | See below |

**C8, in detail.**
- The three rulings hold.
  - PF10 is in the Never class, guarded by V2, `apply` and `pr-check`, and in no GTWPE-MGMT-10 write.
  - The classes cover all 34 files on `main`: 22 general, PF20, PF30.1 and 10 never.
  - PF20 and PF30.x are reached only through their dedicated prompts.
- The G0 direction is followed in order but not yet in effect. The change prompt's drift check misses what it exists to catch (RF-1, RF-2), and its prompt-repair route is unproven (L25).

## The dry run's findings, and the trend

| Finding | Disposition |
|---|---|
| DRr-1 | Fixed, and reproduced in memory |
| DRr-2 | Fixed |
| DRr-3 | Fixed. The capture strains D22 (L1), and the workers have no post-check (L9) |
| DRr-4 | Fixed, with a new defect (RF-2). See also L6, L7 and L19 |
| DRr-5 | Fixed for the ID search. The path half is unverified (L15), and URL-only inputs stop (L16) |
| DRr-6 | Fixed. The readback omits the title and parent (L11) and cannot see an edit's extent (L10, L12) |

**Trend.**
- The count went from 6 to 2, so it halves.
- RF-2 sits in repair text and RF-1 does not.
- Of the 31 listed findings, 10 sit wholly and 4 partly in repair text.
- Neither exit signal fires from this record alone. W1 combines it with R1-B's.

## Canon relied on

- **`AGENTS.md`** on `origin/main` `0db3f0e` (sha256 `2a28ac5c…81758f1`, 55,079 B). Sections applied: the canon-first rule; PF canon read-only; the truncation guardrail; *PR descriptions* (line 74); *Evidence attribution* (line 92). I checked lines 11, 12, 16, 20, 29, 74 and 92 against the design's citations.
- **The canon-first search.** `git grep` over `docs/pfcanon/` on `origin/main` for prompt ecosystem, GCFPE, the flow map, prompt bodies and GTWPE. Governing sections found and read in full:
  - PF04 — HDE Governance §9.1.6;
  - PF10 — HDE Build Notes, addendum 2.29 PF10-CANON-001 and addendum 2.31 PF10-HDR-001. Addendum 2.30 was read by heading only.
- **The file list of `docs/pfcanon/` on `main`,** used to check §8.7's classes.
- **In-flight documents:**
  - `design/GTWPE-DESIGN-v1.1.md` at `a33647c`, whole, and the repair diff `4e3a3db..a33647c`;
  - `design/DRY-RUN-P1r.md`, whole;
  - `CHECKPOINT.md`, whole, including §8 and §10.1;
  - `design/P1-SOURCE-NOTES.md`, whole;
  - `design/REVIEW-P1-DIFFCHECK-R1.md`, whole;
  - `design/DRY-RUN-P1.md`, check 5 only;
  - `design/GTWPE-DESIGN-v1.0.md`, not read whole, only lines found by search;
  - plan v1.2 and `ERRORS.md` at `0ecb6a1`, whole;
  - `PE-METAPROMPT-TEST-20260924.md`, *Where the fixes go*.
- **Governing documents** in `docs/prompt_ecosystem_management/`, identical at `a33647c` and `origin/main`:
  - `gcfpe.decision-record.md`: D17 (archival), and D20 to D26 in full with D23's successors;
  - read whole: `modification-template.md`, `modification_validate.py`, `ecosystem-change-management.md`, `notion-write-boundary.md` and `reviewer-prompt-template.md`;
  - `prompt-body-content-policy.md`, lines 25 to 60;
  - `pe-succession/pe36-to-pe37.md`, lines 44 to 80.
- **GCFPE records:**
  - `docs/ephemeral/pe37.stage5/MGMT-10-REVISION.md`, whole;
  - `MODIFICATION-20260923-closeout-residuals.md`: frontmatter, §E, *Harness files* and cost sections.
- **The installed `glow-write-boundary` `SKILL.md`,** whole.

## What I ran, and writes

- **Git.** Only read-only commands, against `a33647c`, `0ecb6a1` and `origin/main` `0db3f0e`. I made no fetch. Blob checks show the working-tree copies of the files I read equal `a33647c`, and `git status` stayed clean.
- **The validator.** I imported `check()` in-process with `python3 -B` and fed it records from memory, so no file was written. I did not run its `--selftest`, because it writes to a temporary directory.
- **Notion.** ToolSearch loaded the connector's definitions for search, fetch, duplicate-page and update-page. I made no Notion call.
- **Writes.** None.
- **One harness save to disclose.** The harness saved one oversized grep output of mine to its tool-results store (`…/tool-results/bgdfkbfjj.txt`). The preview showed a fragment of candidate-era prompt-body text committed in a historical repository record, the text `pe36-to-pe37.md` item 6 notes. I did not open the file, and it is left to teardown.

**For W1:** repair RF-1 and RF-2. D26-A allows one more full review, or the diff check. Nothing is needed from Nathan until the round closes.

NOTHING NEEDED
