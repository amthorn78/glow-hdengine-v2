---
artifact_type: ALPHA_FEEDBACK_FOR_DEEPER_ANALYSIS
artifact_version: "1.0"
created_date: 2026-09-20
status: FILED_FOR_ANALYSIS_ON_ALPHA_RESUMPTION
authority: Product Owner instruction, 2026-09-20
subject: TypeSafe Jev semantic screening — measured applicability to prompt-ecosystem maintenance
scope_note: Feedback record only. No Alpha work performed. Nothing in HDE-EPIC040 is in scope here.
---

# Alpha feedback — TypeSafe Jev semantic screening, measured

Filed for deeper analysis when Epic Alpha resumes. This is an observation record about
tooling. It performs no Alpha work, reaches no Alpha conclusion, and touches no
`HDE-EPIC040` artifact.

## What was measured

Three pre-registered runs against `jev-1.13.0`, thresholds fixed before each run.
Total spend across all three: **under $0.20**.

| Run | Purpose | Result |
|---|---|---|
| 1 | Pre-registered validation on recorded historical defeat wordings | `REJECT` — 0 of 5 positives caught |
| 2 | Blind recall, cases written by an independent party | `PASS` — 14/15 recall, 0/15 false positives, margin +0.526 |
| 3 | One-time screen of all 55 prompt bodies, 3,205 passages | 7 flagged, 155 uncertain, 3,043 clear; 8 of 9 embedded controls correct |

## The three findings worth analysing further

### 1. Complementary with regex, not superior to it

The screen catches **paraphrase**, which regex provably cannot — wordings such as
*"has drifted from the appendix ratified by the Product Owner"* scored above 0.90 while
containing none of the registry's `CTR-002` literals.

It **missed the terse literal form** that regex handles trivially: *"Compare the current
PF10 against the approved addendum and state the mismatch"* scored **0.507**.

Neither mechanism catches both. Any future design must run them together. A future
session reaching for a semantic screen as a *replacement* for a lexical check would lose
coverage, not gain it.

### 2. The failure mode is specification, not the model

Across three runs the model answered consistently — standard deviations around 0.01
against a published 0.0102 baseline. **Both failures were the question, not the answer.**
Run 1 asked whether a predicate "requires" an action; predicates require nothing. Run 3
asked for a consequent that terse imperative prose does not state.

This is the same error class that defeated the D8/D15 guard six times: each version was a
specification that claimed broader coverage than it had. **The tool converts a semantic
problem into a specification problem, and specification is where this ecosystem's failures
concentrate.** That is the finding most worth deeper analysis, because it is about the
authoring process rather than about any tool.

### 3. Two mechanics that carried the result

- **The uncertain band did work the flag threshold did not.** It caught the true case the
  threshold missed on both Run 2 (0.531) and Run 3 (0.507). A two-way threshold loses both.
- **Controls embedded inside the production run are what made the output interpretable.**
  Run 3 used an adapted question that had never been validated on prose. Without the nine
  controls it would have produced a confident-looking list with no evidence the instrument
  worked in that framing. The adaptation did partially fail, and only the controls revealed it.

## What this did not establish

- It moved no gate. §10 remains unconfirmed, §11 remains blocked, and `SF-05` remains open.
- It closed no finding and reached no conclusion about any prompt body. It produced a
  reading order of 162 passages out of 3,205.
- Its measured recall rests on 30 blind cases plus 9 in-run controls. That is evidence, not
  proof, and the cases were authored by a language model and judged by a language model —
  different families, overlapping training data.

## Questions left open for Alpha analysis

1. Does the complementary-coverage result hold on a corpus authored by humans rather than
   one whose adversarial cases were model-written?
2. Is there a class of ecosystem work where a semantic screen is load-bearing rather than
   advisory, and if so what would have to be true about its validation to allow that?
3. The specification-failure pattern in finding 2 spans guards and screen questions alike.
   Is there a review discipline that catches an over-claiming specification before it ships,
   short of an independent party attacking it? On current evidence, an attacking reviewer is
   the only control that has worked repeatedly.

## Standing constraint carried with this record

The screen is authorized for **one use case only** — triage of the one-time 55-body
baseline review — and that use is now spent. It is never a guard: it does not appear in a
validator, does not gate a release, and does not count as `D14` coverage. Full mechanism and
both validation runs are recorded on the plan's §12 and on the PoC page.
