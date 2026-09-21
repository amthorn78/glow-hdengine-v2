---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE34
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
subject: SF10-07 — scope three body obligations to the writers that owe them; and one fixture renamed
---

# Round 21 — `SF10-07`, and the last known defect

The end-to-end validator reported **10 errors on a healthy ecosystem**. All ten were the same thing:
four prompts checked for three things they do not owe. A check that fails when nothing is wrong gets
ignored, and then it is worthless when something real breaks. That is the whole reason for this round.

**After this change the end-to-end validator reports 4 errors, down from 10.** An earlier revision of
this round reached zero; independent review showed that one of the three exemptions was unevidenced,
and returning that obligation to all fourteen writers restores four of the errors. See *What
independent review found* below — the zero was wrong, not the four.

## What changed

`plan_writer_contract` carried seven obligations over 14 `evaluated_prompt_ids`, and the validator
applied **three body checks to all fourteen**. Membership was all-or-nothing, so there was no way to
say that an obligation applies to some writers and not others.

The contract now carries `body_obligation_ids`: one explicit roster per body obligation, naming the
**ten** writers that owe it. The four CF Specification authors — `CF-C-20`, `CF-C-40`, `CF-E-20`,
`CF-E-40` — are not on those rosters. A Specification states what a change **is**, so it neither
reads current PF10, nor consumes its active addenda, nor declares an authoring context; the contract
ledger already records that `artifact_type` distinguishes their modes, so an `AUTHORING_CONTEXT`
declaration would be a second encoding that can disagree with the first.

**Membership in `EXPECTED_WRITERS` stays at fourteen**, which is the point of doing it this way. The
four keep the four obligations that do apply to them — `approved_base_live_reauthoring_refused` above
all, the central rule of `CF-C-40`'s and `CF-E-40`'s approved-base mode. Shrinking the writer set to
ten would have taken that with it.

Rosters are **enumerated positively** — the ids that owe the obligation — rather than as an exemption
list, per this repository's own rule: enumerate what may exist rather than select what is forbidden.

## Measured, on the tree that is installed today

Baseline is the currently installed tree: **318 files**, digest `28f0aab951f35367…`.

| run | installed (base) | repaired (work) |
|---|---|---|
| end-to-end, 55 bodies | exit 1 — **10 errors** | exit 1 — **4 errors**, all `CURRENT_PF10_MARKDOWN` |
| contract fixture suite | exit 0 — 140 cases | exit 0 — **145 cases** |
| body fixture suite | exit 0 — 164 cases | exit 0 — **169 cases** |
| `change-flow` contract validator | exit 0 | exit 0 |
| `validate_flowmaster` suite | exit 0, `FLOWMASTER_SUITE_PASS` | exit 0, `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_artifact_timing` | exit 0 | exit 0 |

**The D8/D15 guard block is untouched** and byte-identical across all four copies — both skills, both
trees — at 7355 characters, md5 `46c69eaf8f00672e44f8502bbf43c721`.

Zero `.pyc` written into either tree. Every run used a scratch copy; the installed tree was never
written to.

## Five new fixtures, because a guard nobody has fired is not a guard

| injected | result |
|---|---|
| `body_obligation_ids` removed entirely | `PLAN_WRITER_BODY_OBLIGATION_SET` |
| a Specification author added back to a roster | `PLAN_WRITER_BODY_OBLIGATION:current_pf10_markdown_required` |
| a roster replaced by a string | `PLAN_WRITER_BODY_OBLIGATION:active_addenda_required` |
| an id outside the writer set added to a roster | `PLAN_WRITER_BODY_OBLIGATION:authoring_context_required` |

An unreadable roster fails closed. A body obligation whose scope cannot be read is **not** thereby
owed by nobody.

## What independent review found — `SKILL_REPAIR_REQUIRED`, and it was right

`SFR-01` reviewed the first version of this round and returned `SKILL_REPAIR_REQUIRED` with three
items. All three are confirmed by execution and all three are fixed here. Recorded as stated rather
than as softened versions.

### R1 — one exemption had no evidence, and my own measurement could not settle it

I exempted the four Specification authors from **three** obligations. Review found the contract
supports two and is **silent on the third**, and made the epistemic point that decides it:

> The 10 → 0 measurement can't settle it. The ten errors were `PROMPT_WRITER` errors on these prompts
> for these obligations; removing the obligations necessarily removes the errors. It confirms the
> scoping was applied, not that it was right.

That is correct, and it invalidates the headline claim I made. I then extracted the four bodies, which
review could not: **`CF-C-40` and `CF-E-40` carry "current PF10/overlay evidence only when that
correction relies on it"**, in three places each. They consume current PF10 conditionally — so the
exemption was not merely unevidenced, it was contradicted. `CF-C-20` and `CF-E-20` reference a
controlled PFCanon source conditionally, which is not positive evidence of exemption either.

**`current_pf10_markdown_required` is returned to all fourteen writers.** The other two exemptions
stand, on evidence verified against the contract before citing it: `exact_producer_set` is
`{CF-C-30, CF-E-30, ESC-40, IA-30, QA-70, RS-20}` and contains none of the four, and
`rescope_contract.decisions.SPECIFICATION_CHANGE_REQUIRED` routes a Specification change with "no
RS-20 addendum"; `member_registry.output_artifacts` is `["CRD_SPECIFICATION"]` for `CF-C-20` against
`["CRD_SPECIFICATION / SPECIFICATION_DELTA"]` for `CF-C-40`, with `native_function` saying the same.

**The four remaining errors are a prompt-body matter, not a skill matter**, and are out of this
round's scope. Three options, and the third is not available: state the canonical current-PF10 phrase
in the two bodies that demonstrably consume it; substantiate an exemption for the other two from their
input sections; or accept four known errors. Relaxing the check's accepted phrasing is **not** an
option — that is tuning a predicate until the bodies pass.

### R2 — a branch that could not fire, with a fixture named for it

`PLAN_WRITER_BODY_OBLIGATION_SCOPE` was unreachable: every expected roster is a subset of
`EXPECTED_WRITERS` by construction, and the branch ran only when the declared roster equalled its
expected set, so the subset test was always False. Proven by execution. The branch is removed — exact
equality already implies it — and the fixture named for it is renamed
**`reject-body-obligation-foreign-id`**, which is what it actually proves.

This is the "check that cannot fail" class, inside a change whose whole subject is that class.

### R3 — the rationale cited a field that does not carry the meaning

`artifact_type` occurs **once** in the contract, as `pf10_addendum_contract.artifact_type`. It is not
a per-prompt field and is absent from `member_registry` for all fourteen writers. The argument was
sound; the citation was wrong, inherited from loose wording in the contract ledger. Corrected to
`member_registry.native_function` / `output_artifacts` and the rescope contract — in the code comment,
in `SKILL.md`, and above.

### A fourth defect, found by a fixture rather than by review

Returning `current_pf10_markdown_required` to fourteen made the roster-drift fixture stop firing,
because it appended an id the roster now legitimately contained. That exposed a real gap: **set
equality alone accepted a duplicated id.** The check now compares length as well as membership, the
drift fixture points at a roster that genuinely excludes the four, and a separate
`reject-body-obligation-duplicate-id` case covers the duplicate. Five controls, all firing.

## Two things the suite caught that reading did not

**A hash-pin chain.** Changing the contract broke three pins in sequence — `CONTRACT_HASH`, then
`PROFILE_BUNDLED_CONTRACT_HASH`, then `PROFILE_CONTRACT_PIN` — because the contract's digest **and
byte count** are pinned in both the validator and the validation profile, and the profile's revision
map carried `change-flow: 3.2.6` where a plain digest grep did not find it. All four are updated to
the new contract identity, `37c6a41e7cf50ea1…`, 610587 bytes.

**A derived error reported as a root cause.** My first version of the scope check fired
`PLAN_WRITER_BODY_OBLIGATION_SCOPE` three times *in addition to* `PLAN_WRITER_SET` when a writer id
was removed, so the existing `reject-missing-pr10-writer` fixture failed. The fixture was right: a
broken roster should name itself once, not also accuse the rosters derived from it. The scope check is
now gated on the writer set being sound.

## The fixture rename

`reject-source-missing-crd-branch` substitutes `CL-Z-99` for `CL-C-10`, which retargets a destination
rather than removing a branch — it read as coverage that did not exist. Renamed
**`reject-source-retargeted-crd-destination`**. Raised by `SFR-01` in its §10 review; the behaviour
under test is unchanged.

## Revisions

`CHANGE_FLOW_SPECIALIZATION_REVISION` **3.2.6 → 3.2.7** at six sites across both skills, because
validation behaviour and the bundled contract both change. `FLOWMASTER_VALIDATE_REVISION`
**3.2.7 → 3.2.8**, one site. The `SKILL.md` sentence recording why 3.2.6 was incremented is **not
rewritten**; a successor sentence is added beside it, per `AUTH-001`.

**Both packages must be installed together.** The revision moves across both, so either alone leaves a
3.2.6 assertion pointed at a 3.2.7 declaration.

## Packages

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242115 | `45c339415f158602b75d8cb56af9463e0299c87e324c6f7e90f3031d2e645e2d` |
| `flowmaster-validate.skill` | 29 | 275155 | `094301f74a95b971e08280f015ec9979f6f5fe7f58446a37fb5d971ede324f1d` |

Each archive was extracted and compared path-by-path and digest-by-digest against the tested tree:
**identical, with no entries outside the skill root.**

## What this does not claim

No QA verdict, no acceptance, no closure. The independent §10 confirmation on the previous build is
scoped to that build's digests and **does not carry to these bytes** — this package needs its own
review. Ten files changed, all inside the two skills; the complete diff is `sf10-07.patch`, 363 lines.

Prompt bodies are untouched: no body, registry row, or Notion page changed. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` is untouched.
