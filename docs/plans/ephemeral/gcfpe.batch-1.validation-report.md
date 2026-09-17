# GCFPE Batch 1 Validation Report

```yaml
artifact_type: GCFPE_BATCH_1_VALIDATION_REPORT
artifact_version: "1.0"
report_date: 2026-09-17
validation_type: INDEPENDENT_FRESH_VALIDATION
authority: "Nathan / Product Owner, Batch 1 fresh validation authorization, 2026-09-17"
scope: BATCH_1_ONLY
repair_authority_granted: false
prompt_bodies_edited: 0
verdict: BATCH_1_DEFECTS_FOUND
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
selected_release_mutated: false
repository_writes: 0
pf10_edited_or_drained: false
criteria_met: 4
criteria_not_met: 2
defects_found: 8
open_items: 3
```

## 1. What this validation was and was not

This is a fresh, independent validation of the eleven Batch 1 prompt bodies as
they currently stand in Notion. It is not a repair. No prompt body was edited.
No repository write was made. The selected release, PF10, the release register,
Alpha state and PR/CI state were not touched.

The prior Batch 1 sign-off was not adopted. Findings below were formed from the
prompt bodies, the live candidate graph and the plan, and only then compared
against the historical artifacts. Where this validation reaches the same
conclusion as a prior artifact, that is stated as agreement, not as inheritance.

**Verdict: `BATCH_1_DEFECTS_FOUND`.** Eight defects and three open items. Two of
the six Batch 1 completion criteria are not met. The defects are concentrated in
the *governing record*, not in the prompt bodies: six of the eight are record,
vocabulary or copy defects, and only two are contract defects. No defect found
here blocks Batch 2 on a prompt-behavior ground.

## 2. Verdict summary per prompt

| # | Prompt | Disposition | Defects |
|---|---|---|---|
| 1.01 | GCFPE-MGMT-10 | PASS_WITH_OPEN_ITEMS | — (O1, O2) |
| 1.02 | MGR-10 | PASS | — |
| 1.03 | CF-PO-10 | PASS | — |
| 1.04 | CF-C-10 | DEFECT | D3, D6 |
| 1.05 | CF-C-20 | PASS | — |
| 1.06 | CF-C-30 | PASS | D5 (vocabulary, all 11) |
| 1.07 | CF-C-40 | DEFECT | D4, D7 |
| 1.08 | CF-E-10 | PASS | — |
| 1.09 | CF-E-20 | PASS | — |
| 1.10 | CF-E-30 | DEFECT | D8 |
| 1.11 | CF-E-40 | DEFECT | D4, D7, D8 |

D1, D2 and D5 are batch-wide and are not attributed to a single prompt.

## 3. Defects

### D1 — The Batch 1 completion record contradicts the prompts it certifies
**Severity: HIGH. Class: record. Owner: Nathan.**

The plan page names
[GCFPE-Batch-1-Repair-Report-v1.0-20260915.md](https://drive.google.com/file/d/1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-/view?usp=drivesdk)
as "the final Batch 1 report". Its per-prompt ledger row for CF-C-20 reads:

> "Isis authors the initial CRD Specification **or one bounded approved-base
> delta** … Distinguishes INITIAL_OR_PREAPPROVAL_AUTHORING from
> APPROVED_BASE_DELTA_AUTHORING; outputs CRD_SPECIFICATION **or
> SPECIFICATION_DELTA** in SPECIFICATION_PENDING"

The current CF-C-20 body states the opposite, twice:

> "This prompt does not approve its work, **author a delta against an approved
> base**, implement, plan, run QA, edit PF10, drain PF10, or create a PF10
> addendum."
> "**This prompt emits no SPECIFICATION_DELTA.**"

The same contradiction holds for CF-E-20. The report's "Specification
formation" layer row compounds it:

> "CF-C-20 and CF-E-20 accept either a valid class kickoff for
> initial/preapproval authoring **or an already approved immutable base plus
> authorized bounded material delta**."

against the body's "This prompt **never receives or rewrites an approved base**."

The report's supporting-control section is also false against the live artifact:

> "CF-C-20 and CF-E-20 **now explicitly list SPECIFICATION_DELTA** alongside
> their class Specification output."

Measured on the live graph: `CF-C-20.output_artifacts = ['CRD_SPECIFICATION']`,
`CF-E-20.output_artifacts = ['EPIC_SPECIFICATION']`. No `SPECIFICATION_DELTA`.

**Cause, established from timestamps.** The report was last modified
`2026-09-15T17:00:04Z`. All eleven prompt bodies were then re-edited between
`17:50:33Z` and `18:03:08Z` by a corrective pass that found three further
defects in the already-"complete" batch — recorded in
[the Pre-Edit Closure Ledger](https://drive.google.com/file/d/13K0F7S-eDTSYB54Bxo2dMDBQfm4dKC8h/view?usp=drivesdk)
(`17:47:45Z`) and
[the Corrective Repair and Author Self-Assessment](https://drive.google.com/file/d/1M7Ni7TGrZfIgHpCW1xlvPnKS9js0LazE/view?usp=drivesdk)
(`18:09Z`). Its Defect B is exactly this issue; its correction was to
"Restore sole kickoff authoring to CF-C-20/CF-E-20". The report was never
reissued.

**The prompts are right; the report is wrong.** No prompt repair is implied by
this defect.

### D2 — The plan page does not record the corrective pass at all
**Severity: HIGH. Class: record. Owner: Nathan.**

Searched the complete plan page for `corrective`, `self-assess`, the two Drive
IDs `1M7Ni7TGrZfIgHpCW1xlvPnKS9js0LazE` and `13K0F7S-eDTSYB54Bxo2dMDBQfm4dKC8h`,
and `targeted correction`. The only hit is an unrelated use of the phrase in
§3. Neither corrective artifact is referenced anywhere on the plan.

The plan's "Batch 1 completion record — 2026-09-15" still reads:

> "BATCH_1_COMPLETE. … The final Batch 1 report is
> GCFPE-Batch-1-Repair-Report-v1.0-20260915.md."

and the Execution line calls that same superseded report "the prior completion
record". A reader following the plan reaches only the stale document and has no
pointer to the correction that superseded it.

Note in fairness: the corrective report never claimed to re-establish
completion. Its own closing status is
`batch_1_completion_claim: SUPPORTED_ONLY_WITHIN_STATED_LIMITED_AUTHOR_SELF_REVIEW_SCOPE`
with `independent_verification: false`. The defect is that the plan never picked
it up, not that it overstated itself.

### D3 — CRD and Epic kickoff lanes differ on wrong-class recovery, with no stated reason
**Severity: MEDIUM. Class: contract. Prompts: CF-C-10 / CF-E-10.**

CF-E-10 carries a fourth routing branch:

> "A BLOCKED wrong-class result whose recorded selection is CRD goes directly to
> **CF-C-10** …"

CF-C-10 has no reciprocal branch. Confirmed on both sides: the live graph gives
CF-E-10 a `wrong_class_crd` edge to CF-C-10 and gives CF-C-10 no equivalent, so
graph and body agree — the asymmetry is in the contract itself, not a graph
error.

The asymmetry is not merely a longer path. For a CRD-lane arrival whose recorded
selection is EPIC, neither CF-PO-10 entry mode fits the facts:

- `UNRESOLVED_CLASSIFICATION_CASE` requires "an explicit statement that no
  choice has yet been made" — false; a choice exists.
- `EVIDENCED_SELECTION_RECORDING_OR_RECOVERY` applies when "an already evidenced
  decision has no valid record" — false; the record is valid, it simply routed
  to the wrong kickoff.

CF-C-10's remaining exit is therefore "A true source/authority stop without an
exact runnable receiver is terminal to Nathan." The Epic lane self-corrects the
same condition without involving Nathan; the CRD lane escalates. Nothing in
either body explains the difference.

This fails criterion 2, which requires the lanes to be "parallel where intended
and **explicitly different where required**." This difference is neither.

### D4 — SPECIFICATION_DELTA output is underspecified in CF-C-40 / CF-E-40
**Severity: MEDIUM. Class: contract. Prompts: CF-C-40 / CF-E-40.**

Within the same prompt, the preapproval mode declares a full output contract:

> "Return a complete revised pending **artifact_type: CRD_SPECIFICATION** with
> **state: SPECIFICATION_PENDING** and ASK OK?."

while the two delta modes declare content fields only:

> "author one complete pending SPECIFICATION_DELTA … State the immutable base,
> bounded proposed overlay, affected requirements/acceptance/dependencies,
> preserved exclusions, evidence, conflicts, unresolved items, and return phase."

No `artifact_type`, no `schema_version`, and no `state` token is declared for
`SPECIFICATION_DELTA` anywhere in Batch 1 — not in CF-C-40/CF-E-40 which produce
it, and not in CF-C-30/CF-E-30 which consume it ("one pending
SPECIFICATION_DELTA"). Its sibling artifacts both carry one
(`glow-specification/3.0`, `glow-kickoff/3.0`).

Consequence, measured: the live graph assigns
`CF-C-40.result_states = ['SPECIFICATION_PENDING']` covering all three branches
including the two delta branches. That value is not stated by any prompt body —
it rests on reading the adjective "pending" as the token `SPECIFICATION_PENDING`.
Contributing factor: CF-C-40 and CF-E-40 are the only two Batch 1 prompts with
no `## Required result` section; they go straight from `## Execute` to
`## Required result and routing`.

### D5 — `pf10_addendum_role` uses divergent tokens in graph and bodies, with no controlled vocabulary
**Severity: LOW. Class: vocabulary. Scope: all eleven.**

| | Graph token | Body token |
|---|---|---|
| CF-C-30, CF-E-30 | `QUALIFYING_PRODUCER` | `QUALIFYING_DELTA_APPROVAL_PRODUCER` |
| other nine | `NON_PRODUCER` | `NONPRODUCER` |

All eleven differ. `global.json` declares no controlled vocabulary for the field
(zero occurrences of `pf10_addendum_role` or any of the four tokens).

**Substance agrees.** The graph's `pf10_addendum_contract.exact_producer_set` is
`[CF-C-30, CF-E-30, ESC-40, IA-30, QA-70, RS-20]`, which matches the bodies
exactly for the Batch 1 members. This is a token-join defect, not a behavioral
one: no automated consumer can match the field across the two representations.

Which is right: neither is wrong on its own terms. The bodies' token is more
precise (it names *what* qualifies); the graph's spelling is consistent with its
own snake_case convention. The defect is the absent declaration, not either
choice.

### D6 — CF-C-10 dangling conjunction
**Severity: LOW. Class: copy. Prompt: CF-C-10.**

```
- SOURCE_REF, the complete primary requested-change or observed-problem source; and
Conditional:
```

The "and" introduces a third required item that does not exist. It is an
artifact of correctly removing the Epic-only PF09 bullet that CF-E-10 still
carries in that position.

### D7 — Doubled class token in the -40 preapproval inputs
**Severity: LOW. Class: copy. Prompts: CF-C-40 / CF-E-40.**

> CF-C-40: "the complete denied pending **CRD CRD_SPECIFICATION_REF**"
> CF-E-40: "the complete denied pending **Epic Epic_SPECIFICATION_REF**"

### D8 — Inconsistent identifier casing between lanes
**Severity: LOW. Class: copy. Prompts: CF-E-30 / CF-E-40.**

The Epic lane uses mixed-case `Epic_SPECIFICATION_REF` throughout where the CRD
lane uses all-caps `CRD_SPECIFICATION_REF`. Both lanes otherwise use SCREAMING
snake case for every identifier.

## 4. Batch 1 completion criteria, tested as claims that can fail

### Criterion 1 — All 11 prompts have complete review rows and final dispositions
**NOT MET.**

Two documents carry per-prompt rows, and neither satisfies the criterion against
the current bodies:

- **Repair Report v1.0** has an 11-row membership/disposition table (all
  `REPAIRED`) and an 11-row contract/copy ledger — but describes the
  pre-corrective bodies. Its CF-C-20 and CF-E-20 rows are materially false
  (D1). Six further prompts were also edited after it was written.
- **Corrective Repair report** has an 11-row changed-pages table and an 11-row
  regression table — but assigns dispositions to *defects* (A/B/C =
  `CONFIRMED_AND_CORRECTED`), not to prompts, and expressly declines to
  re-establish the completion claim.

No single current document carries complete review rows and a final disposition
per prompt against the bodies as they now stand.

### Criterion 2 — CRD and Epic branches parallel where intended, explicitly different where required
**NOT MET.** See D3. Verified parallel elsewhere: CF-PO-10 routes both classes
symmetrically; -20/-30/-40 are structurally identical across lanes; the Epic
lane's genuine extra requirement (PF09 phase and planned-work reference) is
stated explicitly in CF-E-10 and correctly absent from CF-C-10, which is an
example of the criterion being met. D3 is the one unexplained difference.

### Criterion 3 — Initial approvals are NOT misclassified as PF10 addendum events
**MET.** Reconciled on four independent surfaces:

- CF-C-30 / CF-E-30 step 2: "INITIAL_APPROVE approves the exact reviewed
  Specification and **emits no PF10 addendum**."
- The consumer agrees — IA-10: "**Initial Specification approval itself produces
  no PF10 addendum**", and it lists a PF10 addendum for the initial approval
  under "Not required because they do not yet exist".
- Live graph edges: `initial_approve` routes to IA-10; only `delta_approve`
  routes to `NATHAN_MANUAL_PF10_DRAIN`.
- `pf10_addendum_contract.native_outcome_normalization` maps `INITIAL_APPROVE →
  INITIAL_APPROVAL`, and `never_for` contains `INITIAL_APPROVAL`.

### Criterion 4 — A material in-flight approved-base change produces exactly one standalone addendum
**MET.**

- CF-C-30 / CF-E-30 step 5: "DELTA_APPROVE preserves that base and creates
  **exactly one standalone PF10_BUILD_NOTES_ADDENDUM**; editorial, unchanged,
  IN_SCOPE_REPAIR, denial, and revision-required outcomes create none."
- Idempotency is explicit: "Reuse the read-back matching addendum if the same
  valid approval was already handled; **never create a duplicate**", anchored on
  a stable `addendum_id` and a normalized approved-delta digest.
- `pf10_addendum_contract.exactly_one_per_qualifying_approval = true`.
- The bodies' 16 metadata fields plus 4 drain-verification anchor fields match
  the graph's 20 `required_fields` exactly, field for field.
- Exactly one graph edge carries `DELTA_APPROVE`, terminal, handoff count 0.
- The other nine Batch 1 prompts are non-producers and each states it does not
  create an addendum.

### Criterion 5 — Specification outputs give complete lawful intake to Batch 2
**MET.** Tested against the receiver rather than asserted. IA-10 `FIRST_ENTRY`
was read read-only and each required element matched to its supplier in the
CF-C-30 / CF-E-30 `INITIAL_APPROVE` package:

| IA-10 FIRST_ENTRY requires | Supplied by the -30 INITIAL_APPROVE package |
|---|---|
| exact approved Specification + exact Thoth decision, directly retrievable | "the exact approved Specification and Thoth decision by direct Drive link" |
| `CHANGE_CLASS`, `CHANGE_ID`, approval and predecessor lineage | "class/change and approval lineage"; artifact §1 is "Artifact Lineage and Approval State" |
| carried `CANON_CONFLICT_REGISTER` | "the carried conflict register" |
| actual source/repository/access facts | "actual existing source/repository/access facts" |
| truthful IA session binding state | "the required IA/session binding or its truthful unassigned state" |
| *must not* require a PF10 addendum for initial approval | -30 emits none on INITIAL_APPROVE |
| resolves its own PFCanon/PF10 | "IA-10 independently resolves its current controlled PFCanon/PF10 sources; this handoff does not fabricate them" |

Every required element has a named supplier. One wording gap, not a failure:
IA-10 says "approval and **predecessor** lineage" where -30 says "approval
lineage"; predecessor lineage is carried inside the Specification artifact's §1.

### Criterion 6 — Manager/coordinator prompts do not absorb other actors' authority
**MET.**

- GCFPE-MGMT-10: "does not execute product Change Flow, implementation,
  repository work, PR/CI activity, QA, PF10 drainage, release
  selection/promotion/archival … or Alpha work"; "General repair authority is
  never promotion approval." Its one nonterminal prompt handoff (to PR-10) is
  prepare-only: "It never executes PR-10 or resumes Alpha", matching
  `alpha_resumption_contract` (`prepare_only: true`, `execute_pr10: false`,
  `resume_alpha: false`).
- MGR-10: coordinates "without making a native Product Owner, author, reviewer,
  implementation, QA, Ops, closure, merge, abort, or PF10 decision"; "Nathan
  alone selects EPIC or CRD, provides PR Proceed, manually merges, and directly
  invokes PR-50"; "A coordinator result never authors, approves, implements,
  tests, accepts, closes, merges, aborts, drains, or promotes"; "Do not create,
  restart, configure, dispatch, inspect, or replace sessions."

## 5. No future artifacts (B4)

**PASS, all eleven.** This was the most common defect class in earlier batches
and was checked deliberately. Every prompt carries an explicit negative guard:

| Prompt | Guard |
|---|---|
| GCFPE-MGMT-10 | entry inputs are all present-state; no downstream artifact required |
| MGR-10 | "Do not require a future Specification, Audit, Plan, PR, QA Guide, QA Plan, PR reference, work unit, session identifier, or closure artifact merely because it appears later in the flow." |
| CF-PO-10 | "It must not require or invent a later Plan, PR, QA artifact, repository reference, work unit, or session ID." |
| CF-C-10, CF-E-10 | "No branch fills an omission from a future Plan, PR, QA artifact, or unverified session identity." |
| CF-C-20, CF-E-20 | "Do not demand raw intake, a Plan, a QA artifact, a PR artifact, a Product Owner approval ID, an already approved Specification, a pending delta, or a correction redline." |
| CF-C-30, CF-E-30 | "Do not require a Plan, QA artifact, PR artifact, or separate Product Owner approval object." |
| CF-C-40, CF-E-40 | "Do not supply a later-stage artifact or invent a correction." |

Optional and conditional inputs (B1) were separately checked: every one carries
an exact predicate and none can silently become mandatory. The strongest cases
are the anti-escalation clauses in -30 and -40 — "A Product Owner decision is
required only when the alleged correction needs an unresolved product-intent or
scope choice" and "it is not a universal prerequisite for a source-backed
factual correction." The weakest is CF-PO-10's "bounded additional Product Owner
context only when supplied and relevant", where "relevant" is a judgment term;
it cannot become mandatory because it is gated on "only when supplied".

## 6. Graph agreement (B3)

**Agreement: substantive. One vocabulary defect (D5). No contract disagreement
where the graph is at fault.**

Builder run, per the `glow-graph-contract` skill:

```
python3 graph_parts.py build data/graph-parts <out>
  WARNING  state_routes[RS-40]: declared route(s) with no backing edge: drain_verified
  build: 55 nodes, 235 edges, 55 state_routes
         embedded JSON 580047 bytes  sha256 d08f13ec…
         validation PASS
```

The single warning is the known Batch 3 orphan, already recorded in the plan and
the skill. It is not a Batch 1 finding.

Live-artifact verification, measured rather than inferred:

| Check | Result |
|---|---|
| Live Drive graph `1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp` | 569,990 bytes, whole-file sha256 `f98ae2b6c4b32661afda82f6fd7fd09ab5d82555e3bfa0cd91ff62e1091106a4` |
| Header `source_binding_revision` | `20260915.5-batch-1-targeted-correction` — the corrective pass's own recorded value |
| Header hash convention reproduced | embedded block 569,396 bytes, sha256 `6b5211f3ea51aa1e2ecfa178e243e9821ab15cad625de6424bcae603bf563ea6` — **exact match to header** |
| Shipped parts vs live graph, 11 Batch 1 prompts | **0 differences** in node, edges and `state_route` order |
| Batch 2 patch `section7_v2.json` touching Batch 1 | 0 occurrences of any of the 11 prompt IDs |
| `state_routes` ↔ `edges` parity, Batch 1 | 56 branches, 0 orphans, 0 edge-only |
| Node `candidate_url` bindings | 11/11 resolve to the plan-listed page at version `091426.1` |
| Destination URLs cited in the 11 bodies | 25/25 resolve to the named prompt at `091426.1` |

The live Drive graph is therefore the corrective-pass graph, it is intact, its
header hash is reproducible under the stated convention, and the shipped parts
represent it exactly for Batch 1.

**Where graph and prompt disagree, and which I believe:**

- **D5, `pf10_addendum_role` tokens.** Neither is authoritative; the field has no
  declared vocabulary. Substance agrees.
- **D4, `CF-C-40 / CF-E-40 result_states = ['SPECIFICATION_PENDING']`.** I
  believe the **graph's value is the intended one** and the **prompt is at
  fault** for not stating it. The graph's assignment is the only coherent
  reading, but it is not currently derivable from a stated token, which is
  precisely the "do not invent a field value no prompt body supports" condition.
  Recorded, not corrected.
- **D3, wrong-class asymmetry.** Graph and prompts agree. The defect is in the
  contract, so no graph change would fix it.

No graph edit was made. No part file was modified.

## 7. Open items — named, not filled

### O1 — GCFPE-MGMT-10 entry inputs lack producer, availability point and authority
The entry contract lists six required inputs ("exact Product Owner
authorization; exact repair or maintenance scope; affected candidate or
ecosystem identity; governing plan or other controlling source; complete current
sources required for the named case; and the relevant controls") with none of
the producer / native-availability-point / authority annotation that §5 of the
plan asks the review to establish. "The relevant controls" has no closed
definition at entry; it is only partially enumerated later, in Batch method
step 1 ("candidate, predecessor, plan, catalog, Flow Index, and directly
affected control identities"). Whether the entry list is intended to be closed
by that later enumeration cannot be determined from the body.

### O2 — The batch-mode completion result has no graph representation
GCFPE-MGMT-10 states that a repair-batch invocation returns a case-specific
completion result that "remains separate from these reusable maintenance
states", and that "A complete authorized batch may contain the plan-authorized
next-batch handoff". The live graph models only the four reusable states and has
no self-loop or batch-completion edge. I cannot determine from the body or the
graph whether the graph is deliberately silent on the governance mode or
incompletely models it. Both readings are defensible and the graph's own
`source_evidence` does not settle it. Not treated as a defect.

### O3 — Builder output differs by 4 bytes from the recorded Batch 2 Pass 3 file
The builder emits 580,646 whole-file / 580,047 embedded bytes; the Batch 2
MANIFEST and the plan record 580,650 / 580,051 for the synchronized graph. The
difference is 4 bytes in both measures, and `verify` reports semantic identity.
This is a Batch 2-lane observation surfaced by running the builder; it is not a
Batch 1 finding and was not pursued, since Batch 2 is out of scope for this
authorization. Flagged so it is not discovered later as a surprise.

## 8. Evidence — what was read

Notion, read completely: the eleven Batch 1 candidate bodies at their current
revisions; the plan page `3dc4590a05eb81a9adf1d8f800863937` (53,227 characters);
IA-10 `3db4590a05eb817aa191f1e822c30480`, read-only, as the Batch 2 consumer for
the criterion 5 test.

Drive, downloaded byte-exact via `download_file_content`: the live candidate
graph contract; the Batch 1 Repair Report v1.0; the Targeted Correction Pre-Edit
Closure Ledger; the Corrective Repair and Author Self-Assessment.

Skill: `glow-graph-contract` parts and builder; `global.json` contract sections.

Two Batch 1 Drive artifacts were found that the validation briefing did not
name — the Pre-Edit Closure Ledger and the Corrective Repair and Author
Self-Assessment. Finding them changed the outcome materially: they are the
evidence for D1 and D2. This is recorded because a briefing that omits them
would lead a later reader to the same stale conclusion.

The Batch 1 Contract Ledger `1Ej9MIKgejK69j-BorauRM14AE7mQffVX` and Copy/Repair
Ledger `1bzRCUEBgmw0j-TAer_72xAATZBTH1q9r` were located and their identities
confirmed but their bodies were not read in full; the two corrective artifacts
supersede them on every point this validation turned on. Stated rather than
implied.

## 9. What Nathan needs to decide

Repair authority was not granted for this run and is not assumed. The following
are returned for decision:

1. **D1 / D2, the record defects.** These are the reason the restart happened
   and they are still live. Reissuing the Batch 1 report against the current
   bodies, and pointing the plan at it, would close criterion 1. This is a
   record correction, not a prompt repair.
2. **D3, the wrong-class asymmetry.** Two lawful resolutions: add the reciprocal
   branch to CF-C-10, or state in both bodies why the lanes differ. Either
   closes criterion 2. The first is the smaller change.
3. **D4, the delta output contract.** Declaring `artifact_type`,
   `schema_version` and `state` for `SPECIFICATION_DELTA` in CF-C-40/CF-E-40
   would also remove the graph's only unsupported Batch 1 field value.
4. **D5 – D8**, vocabulary and copy. Low severity, no behavioral effect;
   worth folding into whichever pass touches these prompts next rather than
   opening one for them.
5. **O3**, the 4-byte builder delta, belongs to whoever reopens Batch 2.

**Batch 2 is not unblocked or blocked by this validation.** No defect found here
affects the CF-C-30 / CF-E-30 → IA-10 interface, which is the only Batch 1
surface Batch 2 consumes; criterion 5 passed on a run test.

## 10. Prohibited-action confirmation

No prompt body was edited. No repository write, commit, branch or PR occurred.
No graph file or part was edited. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not read for mutation and was not
mutated. PF10 was not read, edited or drained. The release register, Alpha
state, catalog and Flow Index were untouched. No ChatGPT Library artifact or
Library ID was used. Batches 2–6 were not executed; IA-10 was read read-only
solely to test criterion 5, as the plan's Batch method step 3 requires.
