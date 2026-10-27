2 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-1-B: PLAN of MODIFICATION-20261027-gcfpe-backlog-open-items, full review 1 of 2

- **Reviewer:** REVIEWER-PLAN-1-B. I did not author the plan.
- **Brief:** `BRIEF-PLAN-1-B.md` at `6385dbf`.
- **Reviewed:** commit `b0f2481e743548067f834222f943e0284436e8ac`. The record's §P and §A.14; `PLAN-20261027.md`; `plan/` (coordinator decisions, edits, guards, the tools, both dry-run receipts, the R1 receipts, `work/W5.json`, `W7.json`, `W8.json`). I checked that every reviewed path is byte-identical between `b0f2481` and the working tree: the only later change is the two briefs.
- **Mode:** read-only. The only file I wrote is this record. I made no Notion write and edited no prompt body. I ran no tool from the plan's directory: I only imported `binding_pass.py` in memory to apply its rewrite to stored replacement texts.

## REQUIRED

### R-B1 (R1): the post-flight at X17 does not use C-15's text form, so it reports errors on correct bodies

- **Text.**
  - §5 X17: "two fresh reviewers stream bodies lane by lane (D22) …; `PASS` or `PASS WITH WARNINGS`, no mandatory open finding".
  - `postflight-procedure.md` Method step 3: "pipe it to the shipped validator with `--bodies-stdin`, run that row's `audit_assertions`".
  - C-15 says every guard, registry assertion and profile body check runs on `normalize_fetch.normalize(read)`. Claim C4 relies on this.
- **Evidence.**
  - C-15 itself says that no validator's matching is widened. `x12_qualify_102726.py` and `x18_validate_102726.py` refuse a payload that has not been normalized, so the built 3.5.0 profile does not normalize its own input.
  - The second dry run measured what a raw read gives on the edited bodies (`dry-run.json`):
    - N7 `after_probe_ids__raw_fetch_form_diagnostic`: 46 of 56 bodies validated, with 13 body errors (`PROMPT_BODY_ID_MISMATCH`, `QA_PASS_BODY_INTAKE`, `QA_PASS_RECEIVER_BODY`).
    - N9 `raw_fetch_form_diagnostic`: 176 assertion findings on 55 rows.
  - Neither the plan nor its tools give the post-flight brief or its reviewers the normalizer. `grep` finds "normaliz" in PLAN only at N7 and P-L4.
  - Post-flight step 4 says to read the coverage fields, so "46 of 56 validated" is not a pass.
  - X17 is the only qualification gate that reads bodies without the plan's own wrappers, and the dry run did not exercise it.
- **Path:** normal. **Likelihood:** likely. The raw-form errors are certain; how the reviewers then classify them is not.
- **Consequence:** one of two outcomes:
  - X17 reports mandatory findings on correct bodies. That is a stop, or a repair round on a defect that does not exist.
  - The reviewers dismiss validator errors as "presentation differences", and a real body error is dismissed the same way.
- **Smallest correction.** X17's brief names `plan/normalize_fetch.py` as the form in which each body is piped to the shipped validator and to the row's `audit_assertions`, citing C-15. Equivalently, the reviewers run `x12_qualify_102726.py` and `registry_assemble_102726.py assertions` on their own reads. Add one line to X17's verification: the reviewers' runs report the normalized form.
- **In text the last repair added?** It is in C-15's scope (repair R1/R2). The repair stopped short of X17; X17's row predates it.

### R-B2 (R2): the register's candidate record cites PR #768, which the plan itself calls stale

- **Text.** `activation-ops.json`, register page `3d24590a…`, op `C-REG` (phase `candidate`, written at X9):
  > "Work record: `docs/ephemeral/modifications/MODIFICATION-20261027-gcfpe-backlog-open-items.md`, [pull request #768](https://github.com/amthorn78/glow-hdengine-v2/pull/768)."
- **Evidence.**
  - PLAN §12 says: "W8's Q-W8-4 names #768 as the record pull request that merges after P7. #768 merged the ANALYZE record. C-12's controls pull request replaces that design."
  - `C-REG` is W8's text carried verbatim (`work/W8.json` `notion_control_ops` `C-REG`), so the stale reference W8 introduced is written to a control page.
  - #768 holds the record as it stood at ANALYZE ("Nothing has been edited, packaged, installed or selected"). It is not the plan or the evidence that produced the candidate.
  - No check reads the PR number:
    - `control_check_102726.py` forbids only retired release values;
    - `activation_render_102726.py check` confirms that the text landed, not that it is true.
- **Path:** normal. **Likelihood:** certain. **Consequence:** low. A persistent provenance link on the selection authority's page points at the wrong pull request. A reader of the candidate record is sent to the ANALYZE state.
- **Smallest correction.**
  - Replace the link with a marker, `@CONTROLS_PR`, which X1 records when it opens the controls pull request and which X9 fills.
  - Or drop the pull-request link and keep the record path.
- **In text the last repair added?** No.

## LISTED

- **L-B1.**
  - **Finding.** X5's head-first check (C-22) covers only the mention write form. Under the stand-in map, PR-50's operations are 2 head operations plus 8 URL-only mention rewrites (`A1-plan-standin.json`). None writes the `<code>`, `<b>` or `\_` forms that 79 worker replacements carry. If update_content renders those forms differently on write, the first sign is X7, after X6 has written all 55 other pages.
  - **Path, likelihood, consequence:** normal; possible; loud. D26-B applies, and Nathan restores 55 candidate pages from history.
  - **Repair text:** yes (C-22).
  - **Suggestion:** pick a head-first page whose operations carry every markup form.
- **L-B2.**
  - **Finding.** After promotion, the installed governance-audit engine and the installed 3.5.0 profile cannot validate the selected 102726.1 bodies from today's raw fetch. N9 raw gives 176 findings; N7 raw gives 13 errors and 46 of 56 validated. Every standing audit and every future GCFPE-MGMT-10 dry run that pipes a raw read reports false failures. P-L4 names this only for the 100926.1 registry.
  - **Path, likelihood, consequence:** normal, after promotion; certain; loud. Repair text: C-15.
  - **Suggestion:** extend P-L4 to 102726.1, or put the normalizer in the profile's and the registry's own reading, recorded as a decision.
- **L-B3.**
  - **Finding.** The binding checks do not cover two pages in the P5 archive set:
    - What the checks cover: G-W7-BIND-1 and `binding_pass` cover only `app.notion.com/p/<32 hex>` for SUCCESSOR members and PE. The profile's `PROMPT_BINDING_SUPERSEDED` also covers the dashed form, but SUCCESSOR members only, not PE.
    - What they miss: the 100926.1 catalog (`3f74590a…`) and the CL-05 candidate (`4054590a…`). Neither is forbidden in a member body, and `control_check_102726.py` checks them only on control pages.
    - I found no instance in the four bodies I read. The other 52 are unmeasured.
  - **Path, likelihood, consequence:** normal; low; silent if real. A body would point to an archived page after P5.
  - **Suggestion:** add the archive-set ids to BIND-1's regenerated pattern.
- **L-B4.**
  - **Finding.** X2's verification (parent, title, head, no child) would pass on a duplicate that silently lacks a span no anchor, guard or profile marker reaches. So would X4, X7 and X14 after it. D22 rules out byte comparison, but a character count and a heading sequence of the read in hand are not copies.
  - **Path, likelihood, consequence:** normal; low (the precedent's 55 duplications held); silent.
- **L-B5.**
  - **Finding.** The controls pull request opens at X1 and stays open while X2 to X17 commit to the same branch (the map at X3, the landing report at X7, R1 files including `docs/prompt_ecosystem_management/r1-successor-source-20261027.md` at X10). What Nathan merges depends on when he merges. §12's "restarted from `main` after each merge" has no merge-detection step before X18.
  - **Path, likelihood, consequence:** normal; possible; loud (a conflict or a duplicate diff at X26).
- **L-B6.**
  - **Finding.** C-1 is ITEM-31's surface and the coordinator's call. It applies PF04 §9.1.6 ("one coherent successor selection"; "an edited subgroup is not ready while an affected counterpart remains incompatible"), and D27's publication did the same: 54 successors, with GCFPE-MGMT-10 reused.
  - **Fixpoint confirmed:**
    - GCFPE-MGMT-10's body cites no member page, and no page except its own and its parent.
    - PE cites only its own page, a hub, AI Prompts and the register.
    - Each of the 13 members that get only head operations has 4 to 18 stale binding lines.
  - **Structural cost:** because bodies bind by page URL, any member change copies 54 pages, so D23-G's "unchanged member keeps its page" is reachable for GCFPE-MGMT-10 alone. This is a backlog candidate, not a defect.
- **L-B7.**
  - **Finding.** The record's frontmatter and §P disagree:
    - `interaction_cost_predicted` stays 23 while §12 adds a merge.
    - `estimate.execute` keeps 24–40 h and 12–20M while §P re-prices to 18–30 h and 16–26M.
  - **Path, likelihood, consequence:** normal; certain; low. The validator does not compare them.
- **L-B8.**
  - **Finding.** `binding_pass` rewrites any "<title> — 100926.1" on a line, including a historical mention. No worker replacement text contains one: I applied `rewrite_replacement` under the probe map to all 336 non-head operations and none changed. Body lines were not measured beyond the four bodies I read.
  - **Path, likelihood, consequence:** normal; low; silent.
- **L-B9.**
  - **Finding.** W6-PE-14g deletes the lead clause "preserve exactly one operative Alpha baseline; historical entries are non-operative" together with the stale 20260914 baseline. CD-12's "keeps its general rule" is met only by the sentence that remains ("Later maintenance must freshly resolve the authoritative Alpha state …").
  - The passage is inside PE's *GCFPE controlled release overlay*, so DN-8 (c), PE's general rules unchanged, holds. All 15 of PE's operations sit in the overlay or the frontmatter.
  - **Path, likelihood, consequence:** normal; certain; low.
- **L-B10.**
  - **Finding.** P-L6's count reads "four exceptions on five rows". `c16-decisions.json` counts `named_exceptions: 5`, and PART-07 says "C-16's four".
  - **Path, likelihood, consequence:** normal; certain; none. All five decisions meet PART-07's stated test as I read them.

## What held under attack

- **A1.** The cascade is the coordinator's call, and its fixpoint holds (L-B6).
- **A2.**
  - A swapped or wrong map id fails loudly at X4: each op is anchored to its own page's text, and `FETCH_HEAD` checks the page id.
  - Head operations are excluded from the binding rewrite, so HEAD-PE's `predecessor:` line is not rewritten.
  - No worker replacement is rewritten.
- **A3.** X23 runs registry assertions through the plan's normalizing `registry_assemble_102726.py` with the installed audit root, not through the installed engine reading raw text. Standing audits are L-B2.
- **A5.**
  - **The register's procedure binding.** No `part17`, `candidate` or `review` operation on any of the 13 control pages names a procedure or v5.x. W6-REG-1 to -3 change only the PF10 reference-boundary paragraph. C-REG appends.
  - **D30.** It is on the branch, after D29, and X0(g) checks it.
  - **Request 4.** QA-70's W4-P11-QA70-2 states it as its own duty. PLAN §3 PART-11 records that it is new.
- **A6.**
  - **Canon citations in the CL-05 operations.** The citations I checked match canon:
    - CL05-14: PF06 §3.5.1 *Close-tooling repair*.
    - CL05-12: PF06 §3.5.2.1 and PF12 §8.17 say that no Epic close-run family is admitted.
  - **Partition.** Putting GCF-24.CLOSE in `MATERIAL_BRANCH_LOOP_OR_UTILITY` follows the oracle's convention: GCF-17.LINEAGE, also on the normal path, has that partition, and the 26 core rows are pinned.
  - **QA-120's PASS intake (C-18).** It names the change ID and the QA Report and RCA. That fits PF06 §3.5.1, where the stage "resolves its inputs from the change's records".
- **A8.**
  - **Counts.** Every count I checked reproduces:
    - 446 stored operations = 110 head + 109 + 98 + 41 + 31 + 24 + 14 + 12 + 7.
    - 110 head operations = 54 × 2 + 1 + 1.
    - 13 members get only head operations.
    - About 1,190 operations in all = 446 + 113 + 632.
  - **Spend.** PLAN's spend of 10.5–11.5M is under twice 10M, so D26-D needs no re-price.

## Notion pages read (read-only, transient, D22)

| Page | Page id | As of |
|---|---|---|
| PE Metaprompt 100926.1 | `3f44590a05eb81f98b76c83465dc1960` | 2026-10-12T13:32:38.514Z; read by slices, around the PART-13, -14, -26 and -27 anchors, the heading index and the page ids it cites |
| GCFPE-MGMT-10 100926.1 | `3f74590a05eb81b69bd8c27106f7a59d` | 2026-10-12T02:30:05.584Z; read in full |
| CL-05 candidate 102626.2 | `4054590a05eb8155b301e2cb6dec31d5` | 2026-10-26T11:45:19.630Z; read in full |
| MGR-10 100926.1 | `3f44590a05eb813ea53ac959e7a4e597` | 2026-10-12T02:29:57.710Z; read in full |

No body is kept on disk beyond the harness's own record of the fetch.

## Canon relied on

Read on `main` `91925e9`:
- **PF10-HDE-Build-Notes v13.9:** the heading index. Its only addendum, 2.1 (S19), has no hit for close-mutation, business case, emulation, handoff, prompt ecosystem or GCFPE, so the §8 silence rule returns authority to permanent canon.
- **PF06-Canon-Change-Process-Guide v2.5.5:**
  - §3.5.1 in full, including *Close-mutation-set stage* and *Close-tooling repair*;
  - §3.5.2's opening;
  - §3.5.2.1 (close-pack files; "No Epic close-run family is admitted").
- **PF04-Canon-HDE-Governance v2.8.8:** §9.1.3 *GCFPE model and reasoning-level guidance*; §9.1.6 in full.
- **PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7:** *Same-run close evidence for a CRD*; §8.17 *Close-run family exception*. Both were read by search hit only, and are relied on only for "No Epic close-run family is admitted".
- **Repository controls:**
  - `AGENTS.md` (*Code review guidelines*, the canon-first rule, *Evidence attribution*);
  - `gcfpe.decision-record.md` D23 with its successors, including that of 2026-10-27, and D26 to D30;
  - `postflight-procedure.md` *Method*.

IN FLIGHT
