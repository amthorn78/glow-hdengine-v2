2 distinct confirmed REQUIRED findings.

# PLAN review 1 — reviewer B

**Answer.** The 22 page operations and the graph repair are sound. On the live pages, every span is unique, sits on one line and carries no mention, link or escape markup. All eight pages were still at their pinned revisions when I read them at 12:12–12:16Z. No replacement drops a prohibition, return route or field list. The F03 continuation is resolvable and agrees with the graph. The committed dry run reproduces exactly: 10 of 10 gates; 237 edges, `ff296b1e…`; drift `[PR-40, RS-20]`; all four fixed EXECUTE digests.

Two required defects remain, both in text successor 2 added:

- **B-1 (R3).** X5's landing check byte-compares each landed prompt body with the pre-edit transient read, recovered from the harness records. D22 prohibits that comparison without exception, and the plan certifies D22 compliance.
- **B-2 (R1).** X6 writes the final §E and sets `COMPLETE` before X7 and X8 run. That §E includes X7's and X8's dispositions and readbacks. No later step updates the record.

Neither defect is an edit defect on the pages. B-2 is an author repair. B-1 is either an author repair (drop the comparison and list the residual risk) or an explicit D22 exception, which only Nathan can grant.

## Review identity and scope

- Reviewer B, fresh context: PLAN FULL review 1 of at most 2 (D26-A), from `BRIEF-PLAN-1-B.md` at `2c9ded0c`.
- Reviewed commit `cfa3a496`: the record's §P *DN-1 decision* and *Dated PLAN successor 2*, `PLAN-SUCCESSOR-2-20261011.md` and `plan-successor-2/*`. The working tree at `2c9ded0c` holds identical bytes for every reviewed file (checked by `diff`). I did not open reviewer A's record.
- Written: this file only, plus my scratch directory. Nothing was written to Notion, to a prompt body, to the record under review, to a skill, or elsewhere in the repository.

## REQUIRED findings

### B-1 — R3: X5's landing check is a body byte comparison that D22 forbids, presented as D22-compliant

**Text or step.**

- `body_check.py`, `check` mode, lines 354–365, takes the newest pre-edit read of the pinned revision: `expected, _ = apply_all(pre[-1][2], ops)`, then `row["rest_unchanged"] = expected == body`, plus a line-by-line `differing_lines` count.
- X5 passes only when every page has `pre_edit_read_found` and `rest_unchanged` true and `differing_lines` 0. The failure-path sweep runs the same check.
- The plan certifies compliance in PLAN-SUCCESSOR-2 §3, point 5 ("Landing is checked against the whole page, in memory … Nothing is stored or hashed (D22)"), and in §12 ("Nothing in the repository holds a body, a body hash or a body comparison"). Brief claim C7 repeats it.

**Evidence.**

- **What D22 requires.** The ruling is at decision record lines 1221–1239 and `prompt-corpus-policy.md` lines 93–112. A transient file is allowed only while it:
  - "serves only the read or check in hand, and is never a source for later work — the next read goes back to Notion" (condition 2);
  - "is never hashed, byte-compared or otherwise used as the body's identity" (condition 3);
  - where the session cannot delete it, is "never read again" (condition 4).

  "Body hashes or byte comparison" stay "prohibited, without exception".
- **What X5 does.** After X3 and X4, X5 reads each body's X2 harness record again, uses it as the baseline, and string-compares the whole landed body against it. That breaches conditions 2, 3 and 4 and the closing prohibition, on all eight pages, on the normal path.
- **The candidate's own rule.** The PE successor's GCFPE overlay (*Selected-release identity and source acquisition*) says: "A prompt body is read from Notion and never hashed, byte-compared or kept as a standing copy (`prompt-corpus-policy.md`, `D22`)".
- **Precedent.**
  - The GTWPE pilot declined exactly this new-against-old comparison and listed it as accepted risk K-6 ("No byte comparison of «NEW» with 090826.2 (`D22`)", `MODIFICATION-20260929-gtwpe-pilot.md:642`).
  - The GCFPE landing tool states "no body is compared" (`evidence/e6/land.py:175`).
  - The closeout record states "Nothing was hashed or byte-compared as a body's identity".
- **Refutation tried.**
  - "Nothing is stored" does not answer a rule that forbids the comparison itself.
  - `ecosystem-change-management.md` §5.2 ("compared by bytes") predates the corpus policy and D22, and the policy declares any conflicting procedure defective.
  - PF04 §9.1.6 asks for complete readback of changed bodies. A whole-page readback by reading meets that without a byte comparison.

**Path, likelihood and consequence.** Normal path (X5); certain. Nathan's approval would authorize, unflagged, a procedure his D22 ruling prohibits. The same dependency also makes a correct landing fail after the writes if X5 runs more than 240 minutes after X2, in another session, or after any renderer normalisation anywhere on the page (P2-5). That stop then routes into page restoration.

**Smallest correction.**

1. Drop `pre_edit_read_found`, `rest_unchanged` and `differing_lines` from `check` and from X5's criteria.
2. Keep `revision_moved`, every operation `LANDED`, every guard and the registry form.
3. Verify the rest of each landed page by a whole-page readback by reading, as PF04 §9.1.6 and earlier Modifications do.
4. List "a stray change outside the spans is caught only by that reading" as an accepted risk, as K-6 did.
5. Correct §3, point 5 and §12.

If Nathan wants the programmatic comparison instead, the plan asks him for an explicit, bounded D22 exception before EXECUTE approval, rather than asserting compliance.

**In text the last repair added:** yes. It is new in successor 2 (`body_check.py check`, §3 point 5, X5). No review repair has run yet.

### B-2 — R1: X6 closes the record before X7 and X8 run, and nothing records them afterwards

**Text or step.** X6 reads: "Write §E: step dispositions X0–X8, parts, artifacts with their readbacks, … Set `status: COMPLETE` … Commit and push." X7 (the W9–W10 tracking lines and their re-fetch) and X8 (PR #600's body, ready for review, head check) run after it. W9's text says "EXECUTE complete" and links "the X6 commit". No step after X8 writes §E.

**Evidence.** At X6 the executor must record X7's and X8's dispositions, and the W9/W10 readbacks, before any of them exist. It has two choices, and neither is truthful:

- **Claim them in advance.** That breaks `session-working-rules.md`, *Tracking is part of the work*, rules 4 and 5: "Never tick a box you cannot evidence"; "A write you have not read back is a claim, not a record".
- **Mark them pending.** The record is then set `COMPLETE`, pushed and never updated, so `main` keeps a stale disposition. That is the failure class the same document names: "The record caused the error".

The template (§P) counts a plan complete only when its normal path runs "with no interpretation".

**Path, likelihood and consequence.** Normal path; certain, on every EXECUTE. Consequence is low to moderate: a `COMPLETE` record whose X7/X8 entries are either unverified claims or stale.

**Smallest correction.**

1. X6 records X0–X6 and the item dispositions, without setting `COMPLETE`.
2. Add a final step after X8. It records X7–X8 with their readbacks, sets `COMPLETE` and `interaction_cost_actual`, runs the validator, commits and pushes, and then runs X8's head check. Alternatively, move X8's ready-for-review and head check after that commit.
3. W9 links the record by its branch path instead of "the X6 commit".

**In text the last repair added:** yes. It is new in successor 2 (§5, X6–X8).

## LISTED findings

Each line gives the path, likelihood, consequence, and whether the text is new in successor 2.

- **L-B1.** PE's *Standards and preservation* section still says "Preparing a standalone PF10 addendum does not authorize live PF10 inspection, numbering, insertion, canon adoption, or repository publication."
  - Every planned edit leaves it in place. It contradicts PF06 §0.1A for agent-authored addenda, G-F05-A cannot see it (it lacks "allocat"), and neither §8 nor MB-007's text records it.
  - Maintenance path; low. A PE run prepares an unnumbered addendum, or reads the producers' new rule as conflicting. Pre-existing text; recommend adding it to MB-007.
- **L-B2.** Some guard exceptions are wide enough to hide a regression. A regression placed on an excepted line or sentence passes.
  - G-F05-A's exception exempts any sentence that begins "Outside GCFPE", including PE-2's GCFPE half.
  - G-F02-A and G-F03-A exempt whole lines that carry an exception phrase: QA-50's latitude paragraph, and any line containing "nonterminal".
  - Maintenance; low. New (`guards.json`).
- **L-B3.** X4 carries no revision precondition. X3 (copy, builds, commit, push) separates X2's pin check from the writes, so an interleaved edit is found only after writing (X5). R-N's restore-to-pin would then also remove that other edit.
  - Failure path; low. Loud, with possible loss of another session's change. New.
  - Fix: re-run `plan --prompts <P>` on a fresh fetch immediately before each W-write, or run X3 before X2.
- **L-B4.** §6's "From X4 onward" branch does not distinguish steps. A failure at X6, X7 or X8, after X5 has verified the pages, records PART-01 `BLOCKED` and reverts X3, although PART-01 landed whole.
  - Failure path; low to medium (see L-B5 and L-B6). Leaves a false `BLOCKED` record and a reverted, verified copy. Loud. New.
- **L-B5.** X6 requires `grep -c 'typesafe-scoring request v6'` to print 1. A §E that names the TypeSafe row prints 2, and EXECUTE stops after all writes, into L-B4.
  - Normal path, avoidable trap; low. Loud. New.
- **L-B6.** X7's target line `**MODIFICATION-20261010 status:**` does not exist yet on the catalog (last edited 09:39:15Z) or on Alpha feedback (08:56:47Z).
  - X7 depends on the PLAN return writing exactly one such line on each page, and X7's check is a reading, not a committed command (D26-A rule 1).
  - Normal path; low. A loud stop at X7, into L-B4. New.
- **L-B7.** X0's "Record Nathan's approval verbatim in `plan_approved_by`" differs from this record's practice: the name goes in the field and his words are quoted in a section. Either reading passes the validator.
  - Normal path; low. Interpretation only. New.
- **L-B8.** QA50-1 tells Kronos, while authoring the Plan, to "Record the execution arrangement the Product Owner chooses". The Product Owner usually has not chosen yet.
  - Normal QA planning path; low. A literal reader may stop to ask, or record a placeholder. New (`edits.json`).
- **L-B9.** The F05 format text departs from canon wording in places:
  - It omits PF06 §0.1A's "unique metadata when needed".
  - It omits PF06 §0.1A's pointer that Technical Writing Best Practices owns the writing guidance. PF03 §9 holds the fullest output rule, and PLAN §13 does not cite it.
  - "Approval status" narrows PF06's and PF27's "status" and PF03's "status effects".
  - It drops PF27's "canonical subject matter", while IA-30 keeps "never … declares the addendum canonical".
  - It restates canon in seven bodies, which can drift from canon.

  I found no conflict a producer would act on. Normal path; low. New.
- **L-B10.** On CF-C-30, CF-E-30 and PE, "approval status" now sits beside the retained "It carries **no** status … field". The forbidden-fields scope note that tells the two apart by function lives only in the graph contract.
  - Normal path; low. A producer may omit the approval status or write a "Status:" line. New.
- **L-B11.** Producers resolve "the next continuous number" from PF10 on `main`, which changes only when Nathan transfers PF10. Two qualifying approvals before a transfer receive the same number. This follows from PF06 §0.1A combined with D8's no-paste-checkpoint rule.
  - Normal path when changes run in parallel; low to medium. Duplicate numbers that Nathan must renumber at paste. New text implements it.
- **L-B12.** The copied `global.json` keeps a stale self-description:
  - `_prologue`: "No assembled graph or shipped validation proof exists for these candidate parts. See ../README.md."
  - `status: FROZEN_FOR_CANDIDATE_AUTHORING` and `proofs: {}`.

  The new `execute/` directory has no README, and a shipped build now exists. `graph_repair.py check` forbids changing these keys. Low (STALE-001). New location.
- **L-B13.** Design point 3 says the new edge is placed "after the largest `global.json` index, here 125". The base's largest global index is 124. The edge's provisional index 125 ties with CF-C-10 → CF-E-10 and sorts after it, giving final position 126.
  - The outcome is deterministic and checked. No shipped consumer reads edge order: state routes use `state_route_order`, the deriver uses sets, and I found no order assumption in the validators. Wording only; new.
- **L-B14.** The plan never re-runs the seven rows' existing registry assertions before and after the edits.
  - My in-memory run found 0 findings before and 0 after on all seven rows: the selected registry (33–37 assertions per row) and the 2026-10-09 candidate proposals (35–39).
  - Verification gap only; low. New.
- **L-B15.** PE has no registry row, so its guards (G-F03-A, G-F04-A/B and G-F05-A/B/C on PE) have no standing home after this change, and nothing re-runs them (GUARD-001).
  - Maintenance path; low. §2 states it; §8 does not list it.
- **L-B16.** IA-30's graph branch `plan_delta_return` keeps `route_kind: TERMINAL_MANUAL_BOUNDARY`, the only such branch, while being nonterminal with one handoff. CF-C-30 and CF-E-30 use `NATIVE_RESULT`.
  - Pre-existing in both the selected and candidate parts, and F03's scope names the interfaces. Low; label inconsistency. Not new.
- **L-B17.** X1 neither refreshes `origin/main` nor re-checks PF06, PF27 or the registry at EXECUTE. A canon change between approval and EXECUTE goes unseen, and X3's digests then certify against the branch's copy.
  - Low. New.
- **L-B18.** `update_content` has no documented atomicity, so a call can land partially. X4 does not say to check page state before resending after compaction (D26-C).
  - Failure path; low. Loud: found at X5 or by the sweep. New.
- **L-B19.** DN-1 keeps "the derived registry". The plan delivers the deriver's drift report and leaves assembling a candidate registry to release qualification (§10). That is disclosed, but not flagged against DN-1's wording.
  - Low.

## Claims checked

- **C1.** Holds for all 22 operations. I read every selected span and replacement in session. Each span is unique and single-line, carries no markup, and is bounded so that the end anchor stops at a sentence end. Every replacement keeps the required prohibitions:
  - PF10 is never edited;
  - no claim of adoption;
  - IA-40 never reviews its own output or creates the addendum, and the delta returns to the same independent IA-30 reviewer;
  - QA-70's owner is the originating proposed-delta owner, never QA-80.

  B-1 concerns the landing check, not the edits.
- **C2.** Holds: 24 of 24 fixtures and 32 of 32 page rows agree; failing rows fall from 27 to 0. The five rows that already pass do so correctly: G-F05-B on IA-30, QA-70, RS-20 and ESC-40, which never carried the old format homes, and G-F03-A on PE, which carries no `DELTA_APPROVE` text. A broad search after the edits finds no surviving F02, F03 or F04 rule on the eight pages. For limits on breadth, see L-B1 and L-B2.
- **C3.** Holds.
  - **Reproduced:**

    | Output | Value |
    |---|---|
    | Build | 237 edges · 596,008 B · `ff296b1e…` |
    | Parts manifest | `b27c11ca…` (56 files) |
    | Derivation | 771 B · `27a2be82…` · deriver exit 1 |
    | Guards | 8,869 B · `8eb54659…` |
    | Drift | `[PR-40, RS-20]` |

  - **Branches.** The three branches match RS-20's live *Rescope authorship, independent review and return* and *Required inputs*, F09, and `plan-redlines.md`. They are disjoint from `rescope_non_pr` and from the PR-30, PR-35 and RS-40 branches by recorded origin. Each heads its group.
  - **`format_expectations`.** No shipped graph tool consumes or rejects it. `regenerate_contract.py` copies named keys only, and flowmaster-validate's closed key set applies to the bundled contract, which is the package Modification's concern (P2-4).
- **C4.** Fails on X6–X8 (B-2). Mechanical except L-B6 and L-B7. The failure path otherwise meets D26-B and the rule-6 carve-out: PR #600 is the record PR, and R-N is Nathan's restore.
- **C5.** Holds. Nothing moved is executed, and P2-1 is rightly outside scope. MB-007 and MB-008 each appear once on the Backlog (last edited 12:01:31Z). L-B1 is adjacent and not recorded anywhere.
- **C6.** Holds on behavior; see L-B9 and L-B10. No PF canon change.
- **C7.** Fails (B-1). The `edits.json` anchors, at most 15 words each, are minimal excerpts consistent with the corpus policy.
- **C8.** Holds. P2-1 to P2-6 are rightly listed:
  - P2-1 is outside scope;
  - P2-2 is a label only;
  - P2-3 is presence-only, with the exact count kept in `body_check.py`;
  - P2-4 is a validator mismatch on an unselected candidate;
  - P2-5 is a loud stop that cannot be dry-run;
  - P2-6 reuses ANALYZE's 55-member dispositions, as PF04 §9.1.6 allows.
- **A2.** The receiver is resolvable on every qualifying path:
  - CF-C-40 requires a return phase in every first and revised `SPECIFICATION_DELTA` (steps 3–4). CF-E-40 was not read; CF-E-30's step 4 reviews the affected return phase and its step 5 field list requires it.
  - IA-30's delta review requires the return point, and its addendum carries `return_point`.

  The rule agrees with:
  - the graph's nonterminal branches `crd_specification_delta_return`, `epic_specification_delta_return` and `plan_delta_return`;
  - the second diagram in `plan-flows.md`;
  - the idempotency rules (a stable `addendum_id`; reuse of a read-back match; IA-30 stops on a conflicting digest).

  The terminal clause maps to `review_terminal` and `plan_review_terminal`.
- **A4.** Batches are order-safe:
  - each start anchor is unique in the original and at each sequential step;
  - spans do not overlap;
  - no `new_str` re-creates a later `old_str`.

  A partial landing is caught loudly. Both windows are adequate only if X2 and X5 run in one session within 240 minutes; B-1's correction removes that dependency.
- **A8.** No Notion write was made. The async-task path, the deletion warning and W9–W10 cannot be exercised without a write. My reads found no moved page.

## What I ran and read (D22 disclosure)

- **Dry run.** `dry_run.py` re-run at 2026-10-11T12:23:35Z on my own reads (HEAD `2c9ded0c`, main `1ea6a262`): 10 of 10 gates pass. The receipt carries no body text and is kept in my scratch directory only.
- **Plan rehearsal.** `body_check.py plan --since-minutes 600` ran on my fetches. Its output was read in session only, never redirected, hashed or cached.
- **Scratch scripts.** Two scratch scripts, in my scratch directory, evaluated registry assertions and broad matches on the in-memory edited text. They printed only counts, assertion patterns and short windows, to my session.
- **Transient files.** I fetched QA-50, CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40 and CF-C-40, which are inline in my subagent transcript. The harness saved PE to `tool-results/mcp-Notion-notion-fetch-1791721008492.txt`, which I read in character slices through a JSON parse and with the tools above, within this review. I also read the operational pages: the candidate catalog and the Modification Backlog inline, and Alpha feedback from `…1791721859682.txt`, which I searched only for the tracking prefix and headings. No body was hashed, byte-compared or written to disk. The harness files stay in the session store for its teardown and are not read again.

## Canon relied on

| Source (`docs/pfcanon/` on `main` `1ea6a262`) | Sections read | Use |
|---|---|---|
| PF06-Canon-Change-Process-Guide v2.5.4 | §0.1A in full: the Specification-format paragraph (line 62) and the agent-authored addendum paragraph (line 64) | F05 format and numbering; runtime resolution of owning canon |
| PF27-Canon-Plan-Templates v2.0.5 | *Canon precedence for template use* (lines 280–294) in full | F05 format; canon precedence; `docs/ephemeral/` storage |
| PF03-Reference-Technical-Writing-Best-Practices v1.8.8 | §9 *Writing PF10-HDE-Build-Notes content* in full | The owner of addendum writing guidance (L-B9) |
| PF10-HDE-Build-Notes v13.5.1 | Complete (189 lines): precedence §§1–9, cross-references, template; "No current addenda" | No addendum overrides PF06, PF27 or PF03 on this topic |
| PF04-Canon-HDE-Governance v2.8.7 | §§9.1.2–9.1.6 in full | Canon-first reads; storage; complete readback of changed bodies; one coherent successor selection |

- **Search.** On `main`, I searched `docs/pfcanon/` for addendum allocation and numbering, "continuous addendum", "agent-authored", "page-ready", "numbered H2" and Build Notes addendum. The only governing hits are the sections above. The PF12, PF14, PF17, PF19 and PF20 hits concern other subject matter.
- **In-flight documents.** From the record at `cfa3a496`:
  - §A (including §A.10) and §P (dated plan, successor 1, DN-1, successor 2);
  - `PLAN-SUCCESSOR-2-20261011.md`, `edits.json`, `guards.json`, `body_check.py`, `graph_repair.py`, `dry_run.py` and `dry-run.json`;
  - `PLAN-SUCCESSOR-1-20261011.md`, `PLAN-20261011.md`, `plan-redlines.md`, `plan-flows.md`, `findings.md`, and `coverage.md` (F05 rows);
  - MODIFICATION-20261009's `execute/README.md`, candidate parts (`global.json`, CF-C-30, CF-E-30, IA-30, RS-20) and `candidate-registry-nonderived.json`.
- **Repository controls.**
  - `AGENTS.md`.
  - The decision record: D13, D14, D15, D20, D21 (including D21-C), D22 (with its refinement and status), D26 and D27.
  - `modification-template.md` and `modification_validate.py` (entry gates, `COMPLETE`, D26 checks).
  - In full: `ecosystem-change-management.md`, `notion-write-boundary.md` and `prompt-corpus-policy.md`.
  - `session-working-rules.md`, *Tracking is part of the work*.
  - `authoritative-surfaces.md`, Notion layer.
- **Precedent.** `MODIFICATION-20260929-gtwpe-pilot.md` K-6 and K-7; `evidence/e6/land.py`; closeout-residuals' harness-file disclosure.
- **Shipped tools.** glow-graph-contract `graph_parts.py` and `registry_deriver.py`; the governance audit's `_evaluate_assertions`; flowmaster-validate's PF10-contract checks.
- **Notion, read in memory.** The eight target pages at their pins, CF-C-40, the candidate catalog, the Modification Backlog, and the Alpha feedback page (searched only).

DECISION NEEDED. B-2 is an author repair. B-1 needs one of two things:

- the author repair above: drop the comparison and accept that a stray change outside the spans is caught only by reading; or
- Nathan's explicit, bounded D22 exception for the in-memory comparison.

One DIFF_CHECK follows a repair (D26-A).
