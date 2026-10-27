2 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-1-A — PLAN of MODIFICATION-20261027-gcfpe-backlog-open-items, full review 1

Reviewer A, under the committed brief `BRIEF-PLAN-1-A.md` (branch head `6385dbf`). Reviewed commit `b0f2481e743548067f834222f943e0284436e8ac`, read through a scratch `git archive` of that commit, not the branch head. Branch head differs from the commit only by the two PLAN briefs. Canon on `main` `91925e9` equals canon at the commit (empty `git diff` over `docs/pfcanon/`). I did not author this plan. I did not edit the record, merge, install, write to Notion or edit a prompt body.

## Answer first

- **The plan's normal path is sound in most places.** C-1's cascade, the binding pass logic, C-15's normalizer, C-16's judgements, the CD-9 and CD-6 conditions, PE's general rules, PART-13 against CD-7 and PF06 §3.5.1, and the D17 order all hold on the committed text and on live reads.
- **Two required defects remain.**
  - **R-1 (R1, with R4).** X1's and X8's surviving-old-text checks name no committed command, and the dry run never ran them.
  - **R-2 (R3).** The plan repairs listed finding L-C1, which Nathan accepted as a risk, without his opt-in. It also writes that wider reading into D30 as his ruling, while §P says L-C1 is still accepted.
- **15 LISTED.**
- **Closing state: IN FLIGHT.** This is full review 1 of at most 2 (D26-A).

## REQUIRED findings

### R-1 — X1's and X8's surviving-old-text checks have no committed command, and the dry run skipped them (R1; also R4)

**Class:** R1, a defect on the normal success path. It is also R4: a plausible path with a silent outcome.

**The text.**
- §P X1 / PLAN §5 X1:
  - "a script applies, with their counts: W6-RE-19 …, W6-RE-20, W6-RE-21, W6-RE-28, and W1's PART-02 note anchored on D30's last line";
  - verification "counted with `body_check.py`'s guard functions over each file: G-W6-RE-19F … 0, G-W6-RE-19R 2, …".
- X8: "`activation_render_102726.py check --phase part17` …: all 24 operations LANDED; G-W6-HUB-F 0, G-W6-HUB-RH 4, G-W6-HUB-RN 2, G-W6-HUB-RP 2, G-W6-REG-F 2, G-W6-REG-RN 2".
- X26's R3 and R4 repository edits, whose verification is "each `old` string 0 and each `new` string 1", have the same gap.

**The evidence.**
- **No committed script applies X1's or X26's repository edits.**
  - The edits exist only as old/new pairs in `plan/work/W1.json`, `W6.json`, `W7.json` and `W8.json` (`repo_edits`).
  - `grep` finds no `.py` under `plan/` that reads W6's `repo_edits`. `contracts_102726.py` and `registry_assemble_102726.py` read only RE-W7-01, W5 RE-4 and W4's registry edit.
- **`body_check.py` cannot run these guards on a file or a fetched control page.**
  - `guards_for()` (line 368) keeps only `surface == "prompt-body"`.
  - The registry pass (line 499) skips other surfaces.
  - `assemble_guards.py` says so (lines 31–33): "body_check runs a guard only on a page entry of edits.json, and the fixture self-test runs every guard".
  - So G-W6-RE-* (surface `repository`) and G-W6-HUB-* / G-W6-REG-* (surface `notion-control`) run only on their synthetic fixtures.
- **`activation_render_102726.py` checks nothing for PART-17 except LANDED.** It maps `part17` to no control phase (`CONTROL_PHASE = {"part17": None, …}`, line 58), so `check --phase part17` evaluates landing only. The dry run confirms it: `dry-run.json` N10 `activation_render.chain.phases[0]` = `{"phase": "part17", "pages_judged": 0}`. The 13 → 0 and 4 → 2 counts in PLAN PART-17 are W6's design-time measurements, not dry-run results.
- **The stored PART-02 note contradicts X1.** In `W1.json` `repo_edits[0]`, the note is anchored on D29's closing text ("…X22's rebuild of the parts and check of the registry from `main`. Each is in\nthe Modification's evidence.\n"). That text still occurs exactly once, immediately before `## D30`. Applied as stored, the note lands between D29 and D30. X1's own check ("the note heading occurs once, after `## D30`") then fails. X1 says "anchored on D30's last line", but nothing committed carries that anchor (Q-W7-2 (a) and C-11 left the re-anchoring to EXECUTE).
- **The dry run (D26-A rule 1: "check that every step's verification names a committed command") covers N0–N10 only.** No gate rehearses X1, X8's guard counts or X26's repository edits, and PLAN §4's stand-in list does not say so (C8).
- **I checked the anchors myself.** In a scratch script on the commit's files, every W6-RE-19/20/21/28, RE-W7-03 to RE-W7-10b and RE-W8-01 to RE-W8-08 `old` string occurs at its stated count, and the seven W6-RE-19 edits apply to v5.0.0. So the edits are well formed. What fails is that they cannot be applied and checked mechanically.

**Path, likelihood, consequence.**
- **Path and likelihood.** Normal path; certain.
- **Consequence at X1.** EXECUTE must write an unreviewed script to apply edits to three governed documents and the decision record, and must re-anchor W1's note by interpretation. A plan that needs this is not "executable mechanically with no interpretation on its normal path" (template §P).
- **Consequence at X8.** The only committed command named, `check --phase part17`, returns `ok` when all 24 operations landed, even if a 091426.1-era policy line that G-W6-HUB-F forbids survives on the Hub or the register. That is a silent pass on the very rule PART-17 applies (template rule 4, D26-E). C3's claim ("each rule change's forbidden guards search every page for surviving old text") is untrue for the Hub, the register and the four repository controls.

**Smallest correction.**
- Commit one small tool (for example `plan/repo_edits_102726.py apply|check`) that:
  - applies the X1 and X26 repository edits from the `repo_edits` entries, with W1's note re-anchored on D30's closing line ("**Until those land,\n`D30` is ruled but not applied.**\n");
  - checks each `old` count before and each `new` count after;
  - evaluates the `repository` guards on the files.
- Give `body_check.py`, or `activation_render_102726.py check --phase part17`, a mode that runs the `notion-control` guards (G-W6-HUB-*, G-W6-REG-*) on the fresh Hub and register reads.
- Add both to the dry run, and name the commands in X1, X8 and X26.

**In text the last repair added?** No. `activation_render_102726.py` is unchanged since `334c51c` (assembly A4). The W1 and W6 returns predate C-15 to C-22.

### R-2 — L-C1, accepted as a risk, is repaired without Nathan's opt-in and written into D30 as his ruling (R3)

**Class:** R3, a silent breach of a Product Owner ruling.

**The text.**
- **IA-30's delta review, W2-IA-30-BC-2 (PART-03, ITEM-14).** The new text says: "For every work unit the delta adds or changes, **including a unit whose acceptance criterion or outcome the delta changes without editing the unit**, check its business case …".
- **D30-A in `gcfpe.decision-record.md`, on the branch.** It reads: "In `MATERIAL_PLAN_DELTA_REVIEW`, every acceptance criterion the delta adds or changes is checked, **whether or not the delta edits a work unit**". G-W2-EM-2 is cut by acceptance criterion to match, and its `guards.json` rule text says "(L-C1)".
- **PLAN PART-03.** It reads: "IA-30 checks each work unit's business case in its initial Plan review and in its material Plan-delta review (R-A1, L-C1)."

**The evidence.**
- **What L-C1 is.** In §A.13, L-C1 is "ITEM-14 and ITEM-15 cut the delta check by work unit; a delta can change a criterion or the outcome without editing a unit", consequence "one criterion or case escapes the delta review". It had no planned PLAN handling, unlike L-A03 or L-A11.
- **What Nathan approved.** §A.14 quotes his approval: "All other listed findings are accepted as risks." He opted in only L-A12 / L-B1, L-A13 / L-B2 and L-A14.
- **What D26-A rule 4 says.** "Non-blocking findings are listed, not repaired … Repairing one is Nathan's opt-in." The brief §5 says the same: "LISTED findings are not repaired unless Nathan opts in."
- **Where the repair came from.** `plan/work/W2.json`, line 1034, records that it was directed: "R-A1 and L-C1, as the brief directs ('also weigh L-C1')". Lines 196 and 207 give the reasons: "so the check reaches those units as well"; "Cut by acceptance criterion, not by work unit, so a criterion changed without editing a unit is caught (L-C1)".
- **What the record tells Nathan.** §P *Open findings* and PLAN §10 still state that the accepted risks include "those accepted at ANALYZE approval (§A.13, less the three opt-ins)", which includes L-C1. Nothing asks him to opt L-C1 in, as R-P1 and R-P2 are put to him.
- **What D30 attributes to him.** D30 is headed "**Product Owner, 2026-10-27**" and quotes only "option (b) for ITEM-15 and ITEM-17, recorded as a decision-record ruling". ITEM-15's frozen statement cuts by "every work unit a material Plan delta adds or changes". So D30 records, as Nathan's class A ruling, a scope he did not rule.
- **Refutation tried.**
  - For ITEM-14's business case, "a unit whose acceptance criterion the delta changes" is arguably a unit the delta changes. So BC-2 alone might fall inside ITEM-14's words.
  - D30-A's "whether or not the delta edits a work unit" is not inside ITEM-15's words. Under either reading, the record says the risk stands while the bodies, the guard and the ruling repair it.

**Path, likelihood, consequence.**
- **Path and likelihood.** Normal path; certain.
- **Consequence.** Nathan approves a plan he is told leaves L-C1 as an accepted risk. On that approval, IA-30 (both lanes) and a decision-record ruling attributed to him carry a wider rule than the frozen ITEM-15. The behavioural effect is a stricter check, which is benign in substance. But D26-A's opt-in control is bypassed, and D30 overstates his ruling.

**Smallest correction.** Choose one:
- **(a)** Put L-C1 to Nathan in the plan-approval request as an opt-in, as R-P1 and R-P2 are. Prepare the two widening clauses (BC-2's "including a unit whose …" clause, D30-A's "whether or not the delta edits a work unit" and G-W2-EM-2's cut) as a conditional set. Until then, D30-A's delta bullet reads by work unit.
- **(b)** Revert those clauses to the frozen ITEM-14 and ITEM-15 cut, and keep L-C1 listed.

**In text the last repair added?** No. W2 and D30 predate C-15 to C-22.

## LISTED findings

| ID | Finding | Path | Likelihood | Consequence | In repair text |
|---|---|---|---|---|---|
| L-1 | X2's check ("the body begins with the duplicated head", no child page) passes on a partial or truncated duplicate. Unlike the precedent's X1, nothing compares the duplicate with its source (A7) | failure | low | content missing outside every guarded passage survives. The profile, registry and post-flight catch only part of it | no |
| L-2 | X5's head-first page PR-50 has only head and bare-mention operations. `<code>`, `<b>` and `\_` spans in worker operations are first written in X6's 55-page batch. I confirmed every `new` text is in fetch form (0 unescaped `_`, 0 Markdown markers), so the risk is Notion's acceptance, not authoring | failure | low | a write-form mismatch is loud at X7, but 55 pages then need Nathan's page-history restoration (D26-B). Smallest fix: head-first a page whose operations carry code and escape spans | yes (C-22) |
| L-3 | A3: the normalizer ships in no skill. After promotion, the installed governance audit and the 102726.1 profile run on raw fetches. N9's raw diagnostic gives 176 findings on 55 rows; N7's raw diagnostic validates 46 of 56 bodies. P-L4 names only the selected registry's half | normal, after promotion | certain | every later audit reports false failures, which can hide a real reintroduction (CHK-001, PAIR-001). X23 itself is fine: `registry_assemble_102726.py` and `x12`/`x18` normalize | yes (C-15) |
| L-4 | X14's `ok` has never been observed true. N7 `after_probe_ids` exits 1 with 111 contract-level errors, accepted as expected probe-rebinding classes | normal | possible | a loud stop at X14 if any of the 111 is not a probe artefact | partly (C-15, C-19) |
| L-5 | The binding pass and the regenerated G-W8-NAME-1 match only the exact predecessor titles. The generic `guards.json` pattern is replaced, and no body guard forbids a bare `100926.1` outside MGMT-10. A citation by a variant name ("X — older name — 100926.1") survives | normal | low | after promotion, a body names a superseded version by title | no |
| L-6 | The controls pull request opens from the working branch at X1, and X3, X7, X10 and X16–X17 keep committing to that branch until X18. "Restarted from `main` after each merge" (§12) does not say how commits made after a mid-run squash merge are kept | normal | likely | the map, receipts and `r1-successor-source-20261027.md` may land on `main` before promotion. A reset onto `main` could drop post-merge commits (loud at the next tool that reads them) | no (C-12) |
| L-7 | `activation-ops.json` C-REG writes "Work record: … [pull request #768]" on the register. #768 merged the ANALYZE record only (PLAN §12 notes the stale Q-W8-4 design) | normal | certain | a stale pointer on a control page | no |
| L-8 | §P and PLAN §1 state the PLAN review as "one FULL round of two reviewers, then at most one diff check". D26-A rule 2 allows two FULL reviews, then one diff check, and rule 6 forbids tightening an exit rule. This brief says "full review 1 of at most 2" | normal | certain | the PLAN estimate in §13 omits a possible second FULL round | no |
| L-9 | A8: merges are #768, the controls PR, the promotion PR and the record PR. That is 4 against §A.8's 2, or +2 rather than §12's "+1". PLAN review rounds will be at least 3 against §A.8's 2 | normal | certain | `interaction_cost` understated by about 2 | no |
| L-10 | P-L6 says "the receipt records four exceptions on five rows". `c16-decisions.json` counts 5 named exceptions on 4 prompts | normal | certain | a count only | yes (C-16) |
| L-11 | D30's tested-guard paragraph says "The Modification's §P lists five guards". §P lists none; PLAN §3 PART-04 does | normal | certain | wording | no |
| L-12 | A4: C-16's DOC-10 G-HP-5 exception covers *Required inputs*, "Preserve exact … producer/acceptance/operator/session identities". These are inputs the handoff supplies, so reading them as recorded facts is a judgement call. The other four exceptions (CL-C-10 G-HP-1 and G-HP-4, CL-E-10 G-HP-4, QA-110 G-HP-2) and the seven operations meet PART-07's test on the live pages I read | normal | low | ITEM-08 arguably incomplete on DOC-10 (P-L6) | yes (C-16) |
| L-13 | GCF-24.CLOSE is partitioned `MATERIAL_BRANCH_LOOP_OR_UTILITY`, although PF06 §3.5.1 places the stage on every close path, between the final QA Report and the closure decision. C-9 follows W5's precedent, GCF-17.LINEAGE | normal | certain | a consumer that treats non-core rows as optional would misread a mandatory stage. The successor oracle's must-fail fixture GCF-24 → GCF-25 mitigates this | no |
| L-14 | DN-5 (a)'s "the route produces no PF10 addendum" is carried only by QA-70's existing contract (initial-mode approvals produce none, and W4-P10-QA70-5 sends the review to initial mode). No operation or guard states it | normal | low | a reviewer could treat approving the successor as approving a material delta to an approved base | no |
| L-15 | §P open findings and PLAN §10 restate C-15's raw-form failure as pre-existing (P-L4). No row records that the bodies' 845 normalized "before" errors and 786 raw errors are of different classes (7 against 9), so C4's "changes no verdict except the rendering-only ones" is not shown class by class in a receipt | normal | possible | C4 rests on counts rather than a per-class reconciliation | yes (C-15) |

## Claims, as tested

- **C1 holds.**
  - The plan lands the 36 frozen items in one successor release and adds none.
  - PART-15 and PART-22 close `NOT_APPLICABLE` (DN-8 (c)).
  - PART-16 (DN-7 (a)) and PART-18 (DN-10 (b)) make no edit.
  - PART-23 closes delivered, in Nathan's words. Separately, R-2 widens ITEM-15's statement.
- **C2 holds, on the A1 attack.**
  - The cascade applies D23-G and PF04 §9.1.6 as an implementation consequence of a ruling. That is the coordinator's (`ecosystem-change-management.md` §6). It is disclosed, re-priced, and matches 100926.1's own 54-successor precedent (D27).
  - GCFPE-MGMT-10's live page (read 2026-10-12T02:30:05Z state) cites no page but its own Notion URL. CL-05's operations and PE name GCFPE-MGMT-10 by name only.
  - On a live in-memory scan, PE cites only itself and the register.
  - The 100926.1 bodies predate both the 100926.1 catalog and the CL-05 candidate, so none can cite an archived page. The fixpoint is complete, and no unchanged body is left citing an archived page.
- **C3 fails** for the Hub, the register and the repository controls (R-1). It holds for the 57 prompt bodies.
- **C4 holds** as far as the committed code shows.
  - The normalizer maps exactly four forms and leaves mentions alone. It only strengthens forbidden guards (a raw `\_` no longer hides a match), and required guards match equivalent renderings.
  - I found no case where it makes a guard pass on text the page does not carry.
  - See L-3 and L-15 for the installed-tool consequence.
- **C5 holds.**
  - D30 is recorded before execution, on the branch, and X0(g) checks it.
  - Request 4 is a new sentence in QA-70's new *Coherence tests* subsection (W4-P11-QA70-2), guarded by G-W4-11-4, and recorded as new.
  - No step before X21 writes the register's procedure binding. W6-REG-1 to -3 sit under *Mandatory PR and PF-document authority boundaries* and *Current source-reference policy*, not *Current selection*. C-REG appends. W6-BIND-1 to -3 run at P2.
  - L-A12 / L-B1, L-A13 / L-B2 and L-A14 are inside PART-13 and PART-24.
  - PE's TypeSafe citation is W6-PE-26 (PART-26).
  - Every PE operation sits inside "# GCFPE controlled release overlay" (live PE read). The general rules that also govern TW are unchanged.
  - Exception: R-2.
- **C6 holds.**
  - The binding pass rewrites only predecessor ids and titles from the map. It skips covered spans and carries them in the replacement, and it never touches a KEPT member.
  - A swapped or mistyped map entry stops loudly, because the head anchors bind identity and `validate` checks distinctness against the TSV.
  - The probe pass applied 1,184 operations with `bind_after` and `name_after` 0 on every page.
  - The mention write form is covered by X5 for bare and titled mentions.
  - Residual: L-5.
- **C7 holds.**
  - The D17 order is kept: P1 bindings, P2 register last, P3 install, P4, P5 move, P6 sweep.
  - Before promotion approval, nothing touches *Current selection* or the procedure binding.
  - X8's register edits are policy text under DN-9.
- **C8 fails in part.** The repository edits of X1 and X26, and X8's guards, were not exercised, and §4 does not say so (R-1). L-1 and L-2 are also unexercised.
- **A6 holds.**
  - CL05-01 to CL05-26 cover every candidate defect the first runs reported:
    - CL-05 result v1.0 §15 items 1–4;
    - v1.1 §15 items 1–2;
    - CL-C-10 v1.1 §9 (CL-L7; intake 3 against entry (b));
    - v1.2 §11 (allowed change 3; the tooling-mode route, CL-L9);
    - O-7;
    - the two drain-stale passages, plus a third (CL05-06).
  - QA-120's PASS intake (HP-QA-120-01, C-18) matches PF06 §3.5.1: the stage "resolves its inputs from the change's records" given the change ID. CLC-04's standalone-session wording matches "it needs no handoff to start".
  - The R1 rows, the 47 / 26 / 21 split and the digests match the D23 successor of 2026-10-27. For the partition, see L-13.
- **A8, as a question.** PLAN spend (about 9M, ending at 10.5–11.5M) is under twice ANALYZE's estimate on either bound, so no re-price is due. The EXECUTE re-price to 16–26M is not above twice the original. The merge and round counts are low (L-9).

## Pages read (D22)

Read live in Notion, read-only, through `notion-fetch`:
- GCFPE-MGMT-10 100926.1 `3f74590a05eb81b69bd8c27106f7a59d`;
- UTIL-10 `3f44590a05eb81d997d1fd2b8d1b5042`;
- DOC-10 `3f44590a05eb81ce99b1d2ade30c572f`;
- QA-70 `3f44590a05eb81209128ea7c82938faf`;
- CL-C-10 `3f44590a05eb819b8022f2a4cdd3b022`;
- PE Metaprompt 100926.1 `3f44590a05eb81f98b76c83465dc1960`;
- the GCFPE Membership and Release Register `3d24590a05eb81ce942ad994cfca9fa1`.

Each fetch's `as of` equalled its `edits.json` pin.

The PE and register results were too large to return inline. The harness saved them in its own tool-results folder. I read them in memory only, for headings, the anchors' sections and a page-id count, and never re-read or copied them. They stay for the harness's teardown. No body text is written here beyond the short quotes above.

Scratch, outside the repository, held:
- the commit's tree (`git archive`);
- PF06 v2.5.5, taken from `main`;
- the v5.0.0 procedure.

No plan tool was run. My checks were inline Python over the scratch copies of JSON and repository files, importing no plan module, so no bytecode was written.

## Canon relied on

- **`AGENTS.md`:** the canon-first rule, and *Code review guidelines* on real inputs.
- **PF10-HDE-Build-Notes v13.9** (`main` `91925e9`):
  - front matter §8, *Silence rule*;
  - §1.1 *Addendum Index*;
  - addendum 2.1's headings (S19), silent on every topic here.

  No older PF10 base and no PF10 history was read.
- **PF06-Canon-Change-Process-Guide v2.5.5:**
  - §0.1A, the agent-authored addendum paragraph;
  - §1.1.4, *PR review finding disposition (every pull request; real inputs only)*, in full;
  - §3.5.1, in full, including *Close-mutation-set stage*.
- **Decision record:**
  - D23, the rulings and its successors through *2026-10-27 — the R1 oracle gains the close-mutation-set stage*;
  - D24;
  - D26-A to D26-F;
  - D27;
  - D28;
  - D29;
  - D30.
- **Repository controls:** `modification-template.md` (format 2.1, rules 1–8, §P) and `ecosystem-change-management.md` (§2, §4, §5, §6).
- **The change's records:**
  - HDE-CRD-0002 CL-05 results v1.0 (§8a, §11, §15) and v1.1 (§11, §12, §15);
  - CL-C-10 decisions v1.0 §10, v1.1 §9 and v1.2 §11.

IN FLIGHT
