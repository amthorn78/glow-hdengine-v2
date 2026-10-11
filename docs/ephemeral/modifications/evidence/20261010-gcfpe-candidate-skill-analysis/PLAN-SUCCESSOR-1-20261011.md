# PLAN successor 1 — resumed dry run — 2026-10-11

**The dated plan's source stop is cleared, and its dry run now finds two required normal-path defects in the dated plan. Completing PLAN needs one Product Owner decision (DN-1, §5).** The graph tooling, companions and packaging route the dated plan lacked are present in this environment at identities bound to completed, reviewed Modifications. Graph build, registry derivation, contract regeneration and the governed packaging route pass on baselines. The same evidence shows that the dated plan's package-contract edits cannot be executed as written, and that its install step would leave installed skills incompatible with the selected release. No FULL review was started. No prompt, skill, graph part, registry, canon or release selection changed.

This successor does not rewrite [the dated plan](PLAN-20261011.md), its evidence or §A. It restarts PLAN before the first external write (D26-C) and is the dated successor the template requires.

## 1. Resume basis

| Fact | Value |
|---|---|
| Invocation | GCFPE-MGMT-10 testing body (D20 redesign page, last edited 2026-09-24), `MODE = PLAN`, Nathan, 2026-10-11 |
| Record location | only on `docs/20261010-modification-gcfpe-candidate-skill-analysis` (draft PR #600) at `6ed14c81`; absent on main `1ea6a262` and on the two other open `docs/*-modification-*` branches |
| Approval | `analyze_approved_by: Nathan`, 2026-10-11 (§A.10); `plan_approved_by` empty |
| Scope | unchanged: F02, F03, F04, F05, F07, F09 are the repair scope; F01, F06, F08 and L01–L11 are listed and not opted in |

## 2. Source identities in this environment

Measured with `freeze.py`, and for flowmaster-validate also with the tw1 `skill_tree_digest` recipe. Installed skills were copied to scratch; the synced directory was not written. Receipts: [plan-successor-dry-run.json](plan-successor-dry-run.json), gate G1.

| Skill | Installed digest | Bound by | Role in this plan |
|---|---|---|---|
| change-flow | `22 9a551af3…` | supplied archive (equal); closeout-residuals `installed_freeze.txt` | repair-package baseline |
| flowmaster-validate | `31 90c15e98…`; tw1 recipe `284b3ac1…` | supplied archive (equal); tw1 package, two `SKILL_FIT_CONFIRMED` | repair-package baseline |
| glow-hde-pr-development | `4 265f9170…` | supplied archive (equal); closeout-residuals `installed_freeze.txt` | repair-package baseline |
| flowmaster-primary | `2 2d41da26…` | supplied archive (equal) | unchanged |
| typesafe-scoring | `3 088c77f3…` | supplied archive (equal) | unchanged |
| glow-graph-contract | `9 e241bb9a…` | closeout-residuals `installed_freeze.txt`; cr1, two `SKILL_FIT_CONFIRMED` | build, registry derivation, contract regeneration |
| session-relay-flowmaster | `5 c8a5b224…` | same as above | suite sibling |
| amthor-workspace-governance-audit | `15 c214e874…` | same as above | registry parser for the deriver |
| tw-flowmaster | `2 0581205b…` | tw1 package, two `SKILL_FIT_CONFIRMED` | suite sibling |
| session-branch-flowmaster | `2 17b5800b…` | **no repository verdict**; accepted only by flowmaster-validate 3.3.2's suite pins (revision `1.0.0` and its required/forbidden strings) | suite sibling |
| skill-creator | `18 e4fee9c9…` | governed packaging mechanism | packaging route |
| glow-merged-change-attribution-lock | installed `10 c518ccb0…` ≠ analysed `11 ee253cfa…` | both advertise `MERGED_CHANGE_ATTRIBUTION_SKILL_REVISION: 1.2.0` | **required sibling of the GCFPE validation profile; the analysed bytes are not available here and were not substituted** |
| flowmaster-propagate | not installed | supplied archive only | no gate needs it; no change planned |

## 3. Dry run (D26-A step 1)

Command, committed: [plan-successor-dry-run.py](plan-successor-dry-run.py). Receipts: [plan-successor-dry-run.json](plan-successor-dry-run.json), run 2026-10-11T07:47:26Z at HEAD `6ed14c81`, main `1ea6a262`. Native pages: [plan-successor-native-checks.json](plan-successor-native-checks.json).

| Gate | Dated-plan check | Result |
|---|---|---|
| G1 identities and copy fidelity | V04 | PASS: 11 bound skills reproduce; tw1 recipe reproduces `284b3ac1…` |
| G2 shipped build, selected parts | V05 | PASS: 55 nodes · 229 edges · 575,074 B · sha256 `ae2bd159…`, the recorded proof token |
| G3 shipped build, candidate parts | V05 | PASS: 55 nodes · 236 edges · 589,795 B · sha256 `3510b2bf…`. First shipped build of these parts |
| G4 registry derivation, selected parts | V05 | PASS: 55 rows, 55 parts, no drift |
| G5 registry derivation, candidate parts | V05 | drift `[PR-40]` only, the candidate's D27 PR-40 routing; `--derive` prints its values, so the candidate registry is derivable rather than hand-authored |
| G6 contract regeneration `--check` | V13 input | PASS: both bundled contracts (4.1.1 / 1.3.1, 613,326 B, `dbae180b…`) regenerate byte-equal from the **selected** build |
| G7 Flowmaster suite, strict | V12 | FAIL on the intended source set: one ERROR, `SKILL_MISSING:glow-merged-change-attribution-lock` (FMV-GCF-CURRENT-001). The three companions the dated plan lacked are no longer missing |
| G8a/G8b change-flow and PR-development validators | V06, V10 | PASS, structural, selected-release profile |
| G8c flowmaster-validate GCFPE profile | V09 | FAIL: `SKILL_MISSING:glow-merged-change-attribution-lock`; 0 prompt bodies |
| G9 governed packaging route, unchanged package | V13 | PASS: quick_validate, package_skill, 4 entries, no traversal, extracted digest equals baseline `265f9170…`, gate run from extracted bytes passes |
| G10 record validation; G11 `git diff --check` | V01 | PASS |
| X, informational: installed attribution lock as sibling | none | suite PASS and profile PASS, **not counted**: those are not the analysed bytes |
| Native pages | V03 | All nine targets unchanged since the dated plan's read: every recorded last-edited time and anchor count matches. Catalog and Alpha feedback unchanged since the last recorded readback; register still selects GCFPE-20260914.1 / 091426.1 |

## 4. Required defects in the dated plan

Both are R1, a defect on the normal success path, confirmed by execution. Neither can be repaired by this session: each fix either needs design not yet scoped or sets a listed finding against the approved scope, which D26-B and D26-A rule 4 return to Nathan.

**DR-1 — The dated plan's package-contract edits cannot be executed.** F05's redline sets `pf10_addendum_contract.producer_allocates_pf10_number` to true in the packages' "active skill contract copies" and flips the validator's assertion. F02's redline changes the contract's `member_registry.QA-100.receiving_role`. Both values are copied from the built graph: `regenerate_contract.py` lines 74–75 and 41–47. G6 shows the bundled contract regenerates byte-equal from the **selected** parts. `validate_gcfpe_20260914.py` lines 1348–1361 fail with `GRAPH_PF10_CONTRACT_MISMATCH` unless contract and graph agree, and line 1715 asserts `False`. Each way to make the edit collides with something:

| Route | Collision |
|---|---|
| Hand-edit the bundled contract | Forbidden: glow-graph-contract says never hand-edit the contract; D13 makes the graph the authority. The validator then fails |
| Change the selected `docs/graph/parts` | Excluded by the dated plan §3. It would also make the selected graph disagree with the selected prompt bodies |
| Regenerate the packages' contract from the repaired candidate parts | That is F06's contract and profile change, listed and not opted in (§A.10) |

Observed values: `producer_allocates_pf10_number` is false in selected parts, candidate parts and the bundled contract. QA-100's `receiving_role` is the old text in selected parts and the bundled contract, and the D27 text in the candidate parts.

**DR-2 — E8 installs the repaired skills while the register still selects 091426.1.** The repaired change-flow and flowmaster-validate would encode D27 behavior that the selected members forbid. For example, the selected QA-100 role is "not Kronos acting as the executor", and the repaired skills would allow Kronos to execute. PF04 §9.1.6 requires interacting skills to be reconciled "in one coherent successor selection" and states that "an edited subgroup is not ready while an affected counterpart remains incompatible." The dated plan's normal path ends with the live skills ahead of the live prompts.

## 5. DN-1 — where do the three package repairs belong?

| Option | What happens | Cost |
|---|---|---|
| **1. Split (recommended)** | This Modification keeps the native candidate-body repairs on the eight pages (F02 QA-50; F03 CF-C-30, CF-E-30, IA-30; F04 and F05 PE; F05 the six producers) and the candidate execution-copy graph and derived registry (F05 global flag; F09 RS-20 → PR-20 edge). All are unselected, with no live effect, no skill review and no install. The package side of F02, F04, F05 and F07, with F06's candidate contract and profile, moves to a new Modification opened with `spawned_from` set (this prompt does not create it), planned with the candidate's release qualification so the packages are built once against the final candidate and installed with promotion | Needs your scope-freeze override, because it narrows ITEM-01 and drops ITEM-02 after approval. This Modification's interaction forecast falls from 11 to about 8 (one ruling added; one skill review cycle and three installs removed). The package work is priced in its own Modification |
| 2. Keep the packages here and opt into F06 for them | Regenerate both packages' contract from the repaired candidate parts with a new contract revision and graph pin, move the validators to a 100926.1 profile, keep the 091426.1 fixtures as history, run one D24 cycle, and install only with promotion. EXECUTE then ends `PROMOTION_CHECKPOINT_REQUIRED` | F06's profile design is unmeasured and is designed only after you choose it (D26-B). It needs the analysed attribution-lock archive (11 files, `ee253cfa…`) or your acceptance of the installed copy as the validation sibling. Forecast about 12 interactions plus F06's work and any repeat skill cycle |
| Not viable: execute the dated plan as written | It needs a hand-edited derived contract | Fails `GRAPH_PF10_CONTRACT_MISMATCH` and breaches the graph-contract rule |

**Recommendation: Option 1.** The packages cannot be made coherent before the candidate contract exists, and under either option they cannot be installed before promotion. Building them once against the final candidate avoids a second build and D24 cycle if qualification changes the candidate again: F01, F06, F08 and the native-body gate are still open. Option 1's remaining work also needs no package gates, so the attribution-lock gap stops blocking it.

## 6. Review, cost and estimate

No reviewer was spawned. FULL (0 of 2) and DIFF_CHECK (0 of 1) remain unspent for PLAN. The `reviews` ledger records this dry run with `required_open: 2`.

**Re-price (D26-D; session working rules, *Loops* 4).** Time: the dated session ran about 1.5 h (commits 23:40–01:14 UTC). This session ran about 1 h (07:31 to about 08:30 UTC). Together that is roughly 2.5 h of the 2–4 h forecast. Tokens: the dated session was not measured. This session's counters show about 0.46 M for the coordinator (the counter reset once when the worker process restarted, so the two segments are summed) plus 0.34 M for the native-page worker: about 0.8 M. That passes twice the 180k–350k PLAN forecast in this session alone. The forecast was set by ANALYZE on 2026-10-10; the twice-estimate rule was set by Nathan in D26 (2026-09-24).

| Remaining work, forecast | Option 1 | Option 2 |
|---|---|---|
| Complete PLAN: bind the native-body check commands and anchors, rerun the dry run on the final scope, one FULL round of two reviewers, at most one DIFF_CHECK | 2–4 h, 1.1–1.7 M tokens | plus F06 design and a package dry run: 4–8 h, 2–4 M tokens |
| EXECUTE | 3–5 h, 0.5–1.0 M tokens (eight native edits with readback, graph and registry, record) | plus packages, D24 and delivery: 6–10 h, 1.5–3 M tokens; install waits for promotion |

These are forecasts, not measurements. The ANALYZE forecast was low by this session's measurement.

## 7. Outside the frozen scope, recorded on the Modification Backlog

- **MB-005:** two different glow-merged-change-attribution-lock trees advertise revision 1.2.0: installed, 10 files, `c518ccb0…`; analysed, 11 files, `ee253cfa…`. That is the spent-identity defect `skill-identity-and-freeze.md` names.
- **MB-006:** the ANALYZE and PLAN review brief in `reviewer-prompt-template.md` neither points reviewers at AGENTS.md nor asks for the *Canon relied on* block AGENTS.md requires of every artifact. This Modification's `REVIEW-ANALYZE-1-B.md` and `REVIEW-ANALYZE-DIFF.md` lack the block, and the repository hook reports them after every shell command. They are dated reviewer records and stay as written.

## 8. Canon relied on

| Source | Sections read in this session | Use |
|---|---|---|
| PF04-Canon-HDE-Governance v2.8.7, `main` | §9.1.2, §9.1.3, §9.1.6, in full | Canon-first resolution and recording; storage classes; skill/member reconciliation in one coherent successor selection (DR-2) |
| PF10-HDE-Build-Notes v13.5.1, `main` | complete: 189 lines, 10,570 B, blob `23bdc484…` | No current addenda; nothing overrides the PF04 sections above |
| In-flight: this Modification | §A (approved), §A.10, dated §P, PLAN-20261011.md, plan-redlines.md, plan-verification.md, plan-dry-run.json, plan-source-checks.json, source-identities.md | Scope, redlines and the prior stop |
| In-flight: related records | closeout-residuals `installed_freeze.txt` and frontmatter; gtwpe-tw-model-advice `packages-tw1.json` and verdict lines | Identity bindings |
| Repository controls | decision record D26 and D27 in full, D22's refinement; modification-template.md; session-working-rules.md; authoritative-surfaces.md; reviewer-prompt-template.md; skill-identity-and-freeze.md; skill-packaging-and-delivery.md; ecosystem-change-management.md; execution-and-delegation-model.md; glow-graph-contract SKILL.md | Process rules applied |

Not re-read in this session: PF06 §0.1A and PF27, which the dated plan relied on for F05's substance. This successor does not change F05's substance.

Merging preserves the record and approves nothing (D21-C).
