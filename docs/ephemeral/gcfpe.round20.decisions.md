---
artifact_type: DEVELOPMENT_DECISION_RECORD
artifact_version: "1.0"
created_date: 2026-09-21
author: PE34
authority: Product Owner delegation, 2026-09-21 — development-level decisions to be taken by the development agent
status: DECIDED
subject: Closing round 20 so the prompt flow can be installed and development can continue
---

# Round 20 — decisions taken at development level

The Product Owner delegated these. Each is stated with its reason and its cost, so the record is
reviewable, but none of them is being escalated back.

## The fact that decides all of them

`SF10-07`, `SF-05`'s typed field, and the `reject-source-missing-crd-branch` fixture correction each
**change packaged skill bytes**. The independent §10 verdict `SKILL_FIT_CONFIRMED` is scoped to
`change-flow.skill` `07864f2b…` and `flowmaster-validate.skill` `43075084…`, and does not carry to
new bytes. Taking any of the three now costs a fresh §10 review round; taking them separately costs
three.

## D1 — Ship the confirmed package. Nothing further changes its bytes.

The package fixes `SF10-03`, `SF10-05`, `SF10-06` and `SF10-08`, and retires the
`flowmaster-propagate` pointer in the two skills it owns. It is independently confirmed at the two
digests above. **No further change is made to it in this round.**

Installation order is load-bearing and was established by execution: **update `flowmaster-validate`
first, then remove the `flowmaster-propagate` skill.** The reverse order gives `suite_ok: false`,
`missing=['flowmaster-propagate']`. The intermediate state is safe because `EXPECTED` is
required-presence only, with no unexpected-skill check.

## D2 — `SF-05`: take A′ plus the §3.6 enumeration as a recurring check. Do not build the typed field.

**Decided against Option A**, despite having just made it reachable.

Two independent methods now agree that the behaviour `D8` prohibits is **absent from the current
contract**: the §3.6 enumeration read all 101 terminal-or-blocking rows in full, and the 280-row
classification found no row that is both `COMPARISON` and terminal-or-blocking, with all **42** rows
in a blocking state classified `NONE`.

So the typed field would cost a field on 280 rows across the bundled contract copies, validator
support for the enum and the pin, an authoring rule, and a fresh §10 — to change the failure mode for
a risk that is not currently present. That is the wrong trade today.

**Revisit trigger, so this is a decision rather than a drift:** build the field if a condition ever
appears that pairs PF10 with comparison language on a terminal or blocking row, or if `CTR-002`'s
literals are found to have been evaded in a body.

## D3 — `pf10_dependency` placement: moot, and the reading task is withdrawn.

Under D2 no field lands, so the graph-versus-bodies choice does not arise and **the 19 rows outside
the `CLEAR` band need no Product Owner reading.** The classification remains landed as what it
actually is: a measurement showing the declared graph carries no prohibited comparison gate,
corroborating the enumeration by a method that catches paraphrase.

## D4 — `SF10-07`: per-obligation exemption, deferred to the next change that moves these skills.

The correct fix is to exempt `authoring_context_required` and `current_pf10_markdown_required` for the
four Specification authors only. Deleting the four from `evaluated_prompt_ids` would also strip
`approved_base_live_reauthoring_refused` from CF-C-40 and CF-E-40, which is not intended.

Deferred rather than done, because it moves bytes. It is not a defect in the prompt flow: the ten
remaining end-to-end errors are all `PROMPT_WRITER` and all this one issue.

## D5 — The fixture correction: deferred into the same change as D4.

`reject-source-missing-crd-branch` exercises a destination retarget rather than an absent branch, so
it reads as coverage that does not exist. `SFR-01` raised it and would take it before installation;
it is one line. **Recorded as a dated known defect instead**, because it moves bytes for a test-naming
error in a suite that is otherwise 164 cases with none failing.

**D4 and D5 are batched into one future change**, so there is exactly one more §10 review rather than
three.

## D6 — Stop building instruments.

The recorder, the bench, the claim inventory and the classifier are finished. Ten consecutive commits
changed no skill byte and reviewed only repository-side tooling. Scaffolding for future rounds stays
in the session scratchpad; only evidence artefacts land.

## What remains, and who holds it

Exactly one action, and it is not delegable: **only the Product Owner installs.** Install the two
skills in the D1 order. Everything else in round 20 is decided and recorded.
