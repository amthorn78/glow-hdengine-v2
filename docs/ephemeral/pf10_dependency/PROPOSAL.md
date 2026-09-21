---
artifact_type: PF10_DEPENDENCY_PROPOSAL
artifact_version: "1.0"
created_date: 2026-09-21
authority: Product Owner authorization, 2026-09-21 — bounded second use of the TypeSafe Jev screen
status: PROPOSAL_FOR_PRODUCT_OWNER_REVIEW
subject: A typed `pf10_dependency` value proposed for each of the 280 state_routes rows
---

# `pf10_dependency` — proposed values for Product Owner review

**This is a proposal, not a landed field.** Nothing here is in a contract, gates anything, or counts
as `D14` coverage. The sequence is: classify (done) → **you review** → the approved enum lands as a
typed contract field → from then on the guard is a plain deterministic enum check, with no model and
no network. A probabilistic classifier could not be the guard and is not offered as one.

## Why this run happened

Review's `P1` on the decision briefs was that Option A cannot be called structural while the property
selecting which branches the rule governs — whether a condition compares PF10 against an
addendum-derived expectation — has no typed representation, because a paraphrase evades any
vocabulary selector. This run proposes that typed representation.

## What was run

<!-- generated: run -->
| | |
|---|---|
| model requested / served | `jev-latest` / `jev-1.13.0` |
| rows classified | **280**, every `state_routes` row |
| contract classified | `7f8d683e672dd4b14766fc2ec9c8ca7e5a964a11e4ddc4dea3fa4f8d7c9b5894` |
| blocking states, from the briefs | `AWAITING_PO_PROCEED`, `AWAITING_THOTH_REMEDIATION`, `BLOCKED`, `PLAN_PENDING_REVISED`, `RESCOPE_PROPOSAL_PENDING_REVIEW` |
| options | `COMPARISON`, `NONE`, `READ_ONLY`, `SOURCE_AVAILABILITY` |
| bands, fixed before the run | `CLEAR` ≥ 0.8 · `UNCERTAIN` 0.5–0.8 · `UNRESOLVED` < 0.5 |
| embedded controls | **28/28 correct**, 2 per batch, including both paraphrase controls |
| tokens | 136,198 in / 17,646 out |
<!-- /generated: run -->

**One revision to the question, made before the full run and recorded.** A 20-row validation batch
returned five `UNRESOLVED` on conditions reading *"missing source, authority, or review mode"*,
because my `SOURCE_AVAILABILITY` rubric never said it meant PF10 specifically while this contract
uses a bare "source" for the change's own artifact. That is an under-specified option of mine,
statable without reference to which answers I preferred. The validation batch is **void** and is not
carried into this proposal. No revision was made after seeing the full run.

## Result

<!-- generated: result -->
| label | rows |
|---|---|
| `NONE` | 270 |
| `READ_ONLY` | 7 |
| `COMPARISON` | 2 |
| `SOURCE_AVAILABILITY` | 1 |

**258 `CLEAR`, 20 `UNCERTAIN`, 2 `UNRESOLVED`.**
<!-- /generated: result -->

## The decisive finding: the briefs' conclusion survives a paraphrase-sensitive screen

The §3.6 enumeration concluded that no branch stops because a comparison between current PF10 and an
addendum-derived expectation found a difference. Review's objection was that its selector was
lexical, so a paraphrase could have escaped it.

**The result is stronger than that objection needed.** Every one of the **42** rows in a blocking
state — `BLOCKED`, `AWAITING_THOTH_REMEDIATION`, `RESCOPE_PROPOSAL_PENDING_REVIEW`,
`PLAN_PENDING_REVISED`, `AWAITING_PO_PROCEED` — is classified `NONE`: no PF10 dependency of any kind.
And both `COMPARISON` candidates are **non-terminal and in `DELTA_APPROVE`**, which is neither
terminal nor blocking. `D8` concerns a mandatory comparison *gate* — a stop. Nothing stops on a
comparison, and every row's `state` is now persisted in the JSON so that claim is auditable from the
artifact rather than from this sentence.

Read, both candidates are **`READ_ONLY` rather than `COMPARISON`**, and I recommend recording them
that way:

- `CF-E-30__epic_specification_delta_return` — 0.49, with `READ_ONLY` second at 0.36
- `IA-30__plan_delta_return` — 0.55, with `READ_ONLY` second at 0.29

Both read *"the exact … receiver recorded by the approved … delta **reads** current PF10; this is not
an RS-40 rescope route."* The receiver reads the current text. Nothing is compared and no difference
decides anything. The model hedged because "the approved delta" beside "current PF10" juxtaposes two
versions and *looks* like a comparison.

**The three sibling rows are the strongest evidence for that reading.** `CF-C-30`, `CF-E-30` and
`IA-30` carry near-identical wording, and the screen split them across the boundary — `READ_ONLY` at
0.72, `COMPARISON` at 0.49, `COMPARISON` at 0.55. Three identically-worded rows cannot belong to three
different classes. The split marks where the model is uncertain, not where the contract is, and all
three should carry the same value.

**Independent corroboration of the one row the briefs single out:** `RS-40__source_resolution_error`
came back `SOURCE_AVAILABILITY` at **0.98**, the highest-confidence non-`NONE` judgment in the run.
That is the row §3.6 names as the closest case, arrived at here without being told.

## Two runs: the conclusion reproduces, the individual confidences do not

The run was repeated in full after review asked for the served model, response completeness and each
row's `state` to be captured. **The labels and bands reproduced exactly** — 270 / 7 / 2 / 1 and
258 / 20 / 2, with the same two `COMPARISON` candidates, the same seven `READ_ONLY` and the same
`RS-40` at 0.98, on identical token counts.

**The individual confidences moved**, by up to 0.10: the `CF-C-30` sibling went 0.62 → 0.72, `CF-E-30`
0.51 → 0.49 and `IA-30` 0.57 → 0.55. One consequence worth naming: `CF-E-30` crossed below 0.50, so
it is now `UNRESOLVED` rather than `UNCERTAIN`, and the band totals held only because another row
crossed the other way.

So read the figures in this document as one run's reading and the **labels, bands and candidate set as
reproducible**. That is a property of the instrument, not a defect in it, and it is a further reason
the guard must be a deterministic check on an approved typed field rather than anything that consults
a model at runtime.

## Where the screen and the lexical selector disagree, honestly

The lexical selector found comparison language in **zero** rows. The screen proposed two, and reading
resolved both in the selector's favour. On this corpus the screen produced **two false-positive
`COMPARISON` candidates and no row the selector missed.**

That is not "the screen added nothing" — its `UNCERTAIN` band surfaced the three sibling rows whose
wording is genuinely ambiguous and which must carry one value, a grouping neither the selector nor the
enumeration produced. But it does mean the screen is **corroboration for a conclusion the enumeration
already reached**, not the thing that established it. The earlier measured record's finding holds:
neither mechanism covers both paraphrase and terse literal forms, so both run.

## The rows you would need to read

<!-- generated: reading -->
Of the **22** rows outside the `CLEAR` band, **2** are terminal: `GCFPE-MGMT-10__promotion_checkpoint_required` (NONE, 0.78), `RS-20__specification_change_required` (NONE, 0.70).

| row | proposed | conf | terminal | lexical | condition |
|---|---|---|---|---|---|
| `CF-C-30__approved_base_correction_redline` | NONE | 0.69 | no | NAMES_SOURCE | approved immutable CRD base plus a source-backed factual finding or actual authorized product/s… |
| `CF-C-30__crd_specification_delta_return` | READ_ONLY | 0.72 | no | NAMES_SOURCE | the exact affected native receiver recorded by the approved CRD Specification delta reads curre… |
| `CF-C-40__approved_base_delta_revision` | NONE | 0.66 | no | NO_MATCH | pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base… |
| `CF-C-40__preapproval_revision` | NONE | 0.67 | no | NO_MATCH | pending preapproval CRD Specification corrected under the exact redline… |
| `CF-E-30__approved_base_correction_redline` | NONE | 0.74 | no | NAMES_SOURCE | approved immutable Epic base plus a source-backed factual finding or actual authorized product/… |
| `CF-E-30__epic_specification_delta_return` | COMPARISON | 0.49 | no | NAMES_SOURCE | the exact affected native receiver recorded by the approved Epic Specification delta reads curr… |
| `CF-E-40__approved_base_delta_revision` | NONE | 0.54 | no | NO_MATCH | pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base… |
| `CF-E-40__approved_base_first_delta_authoring` | NONE | 0.69 | no | NO_MATCH | first standalone Epic Specification delta authored from the exact Thoth correction assessment/r… |
| `CF-E-40__preapproval_revision` | NONE | 0.68 | no | NO_MATCH | pending preapproval Epic Specification corrected under the exact redline… |
| `CL-20__adr_branch` | NONE | 0.79 | no | NO_MATCH | the conditional ADR predicate is satisfied and the ADR branch is explicitly selected… |
| `GCFPE-MGMT-10__maintenance_complete_native_return` | NONE | 0.70 | no | NO_MATCH | scoped maintenance complete and the exact case separately authorizes one ready native continuat… |
| `GCFPE-MGMT-10__promotion_checkpoint_required` | NONE | 0.78 | yes | NO_MATCH | exact-snapshot promotion approval or a required active control-layer checkpoint is outstanding;… |
| `IA-30__delta_deny` | NONE | 0.77 | no | NAMES_SOURCE | REVIEW_MODE=MATERIAL_PLAN_DELTA_REVIEW; exact delta redlines return to the same IA author throu… |
| `IA-30__initial_approve` | READ_ONLY | 0.51 | no | NAMES_SOURCE | REVIEW_MODE=INITIAL_PLAN_REVIEW and the pending whole-change Plan is approved; zero PF10 addend… |
| `IA-30__initial_deny` | NONE | 0.43 | no | NAMES_SOURCE | REVIEW_MODE=INITIAL_PLAN_REVIEW; exact itemized redlines return to the same IA author for AUTHO… |
| `IA-30__plan_delta_return` | COMPARISON | 0.55 | no | NAMES_SOURCE | REVIEW_MODE=MATERIAL_PLAN_DELTA_REVIEW; the exact return_point receiver recorded by the approve… |
| `QA-10__material_native_boundary` | NONE | 0.56 | no | NO_MATCH | a substantiated material scope, Canon, Specification, Plan, or authority boundary has an exact … |
| `QA-10__not_ready` | NONE | 0.70 | no | NO_MATCH | evidence proves failure of an applicable approved Plan objective… |
| `QA-110__escalation_required` | NONE | 0.79 | no | NO_MATCH | material QA evidence finding requires the native QA escalation report… |
| `RS-20__in_scope_pr35` | NONE | 0.78 | no | NAMES_SOURCE | existing repair owner/phase is PR-35 under the original Proceed; no addendum… |
| `RS-20__specification_change_required` | NONE | 0.70 | yes | NAMES_SOURCE | native Product Owner Specification-delta decision; no RS-20 addendum… |
| `UTIL-10__already_applied` | NONE | 0.73 | no | NO_MATCH | every item is already applied with matching target/redline lineage and resulting content, and t… |

The other 258 are `CLEAR`. Full per-row output, with every probability distribution, is in `pf10_dependency.proposal.json` beside this file.
<!-- /generated: reading -->

## Answers to review, 2026-09-21

Review held approval pending three questions and was right to: the gap it names is specification, not
rigour. Answering in its own order, and conceding where it is correct.

### 1. The rule the enum check enforces

Stated as a condition over field values:

> **Fail** any `state_routes` row where `pf10_dependency == "COMPARISON"` **and**
> (`terminal_for_invocation == true` **or** `state ∈ BLOCKING_STATES`).
>
> **Fail** any row whose `pf10_dependency` is absent, null, or not one of the four enumerated values.
>
> `SOURCE_AVAILABILITY` **may** be terminal — that is `RS-40 source_resolution_error`, which stops
> because PF10 cannot be read and explicitly forbids inferring from the failure. `READ_ONLY` and
> `NONE` are unconstrained by this rule.

That is the whole check. It is the `D8` prohibition stated over typed values: a comparison may inform
a continuation, and may never be the reason an invocation stops. It also follows v11's lesson —
enumerate what may exist rather than select what is forbidden — which is why the second clause fails
closed on an absent or unknown value rather than treating absence as compliance.

Against the current contract the check passes: both `COMPARISON` candidates are non-terminal and in
`DELTA_APPROVE`, and all 42 rows in a blocking state are `NONE`. The 22-row reading task now has a
criterion: a row's proposed value is wrong if reading its `condition` contradicts the rule above.

### 2. What makes a wrong label fail — and what does not

**The bare answer is that a deliberately false first declaration is undetectable, and no layer below
changes that.** Review has this exactly right, and "an authoring rule" was three words doing too much
work. Here is what can actually be enforced, in descending strength.

**(a) A lexical cross-check, deterministic.** Fail any row declaring `NONE` whose `condition` matches
the `CTR-002` comparison literals. This catches the literal false declaration outright. It does *not*
catch a paraphrased one — that is the same selector weakness the field exists because of, so it is a
floor, not a solution.

**(b) A declaration bound to the condition's text by hash.** Store `condition_sha256` beside
`pf10_dependency`; fail when a row's `condition` no longer hashes to the value its declaration was
made against. Editing a condition then **invalidates its declaration** and forces a fresh one. This
is the realistic failure — someone rewrites a condition and leaves the old label behind — and it is
deterministic. It is also a mechanism this round has already built and fired controls against, in the
claim inventory's allow-list, where keying an exemption to exact line text is what makes an edit
return the claim for accounting.

**(c) The screen as a review aid, never a gate.** Re-running the classification and reporting
*disagreements with the declarations* is detection without being a guard. It has no place in a
validator or in CI.

**The residual, stated rather than dressed:** an author who writes a paraphrased comparison and labels
the row `NONE` passes (a), passes (b), and is only surfaced by (c) as an item for a person to read.
What the field buys is not detection — it is that the claim becomes a **typed, dated, attributable
declaration in a governed artifact**, contradictable by reading the condition printed beside it, where
today there is no claim at all and therefore nothing to be wrong. That is a change in failure mode,
and review is entitled to weigh whether it earns its cost on that basis alone.

### 3. Relationship to `CTR-002` — supplement, and the placement is the weak point

**Review is right, and this is where the proposal is weakest.** The chain is prompt bodies in Notion →
graph parts (which hold edges and `state_route_order`) → `state_routes`, derived. The paraphrase risk
lives at the body. A typed field two derivations downstream does not close a gap in the source: the
paraphrase still enters where `CTR-002` already guards, and the declaration sits on a restatement.

So the honest framing is **supplement, not replacement**, with two coherent designs and a choice that
is the Product Owner's:

- **(i) Keep the field on the graph** and drop the claim that it addresses paraphrase at the source.
  It then buys graph-level consistency — a typed, checkable statement about every route, and the rule
  in §1 — and `CTR-002` remains the only defence at the body. Cost is what was already priced.
- **(ii) Put the declaration in the prompt bodies**, where the risk is, and derive the graph field from
  it like every other graph value. This is the coherent design. It costs a new per-branch declaration
  across 55 bodies authored in Notion in place, and the 280-row classification here becomes the
  derivation seed rather than the artefact.

The proposal as written implied (i) while arguing from the paraphrase objection, which belongs to (ii).
That is the specification gap review identified, and it is not closed by anything in this document.

## What this establishes, and what it does not

**Establishes:** a typed value is available for all 280 rows; the controls show the instrument
answered as specified on known labels, paraphrases included; no row is both `COMPARISON` and
terminal-or-blocking; the three ambiguous siblings are identified and grouped.

**Does not establish:** that the values are correct — 22 need your reading, and a false declaration on
any row is not detectable by this or any classifier. It moves no gate, closes no finding, and makes no
`QA`, acceptance, `PF09`, OPS, deployment or closure claim. It is not `D14` coverage: the guard is the
deterministic enum check that would follow your approval.

## If you approve the values

The remaining cost is what the briefs already priced: the field on 280 rows across the bundled
contract copies, validator support for the enum and the pin, and an authoring rule. One consequence
the claim inventory already flags: the briefs' *"remaining 60"* is derived from the contract's
terminal rows, so adding this field means that figure must be re-measured.
