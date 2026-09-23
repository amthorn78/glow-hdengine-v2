---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-pr40-reject-replans
status: PLANNED
targets: [prompt, skill, rule, graph, registry, notion_control]
gate_tier: 1
closure:
  upstream: [DOC-20, DOC-10, PR-10]
  downstream: [PR-10, PR-20, RS-10]
  state_sharers: "PR-40 radius 9 and PR-20 radius 21, pasted in §A"
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 2
item_count_at_approval: 1
interaction_cost_actual:
items:
  - id: ITEM-01
    statement: "When PR-40 rejects landed work for an in-scope implementation, corrected-code or PR-lineage defect, the finding routes back to PR-20 for a new plan in a new dedicated implementor session that Nathan seeds, and goes through a new Product Owner Proceed, PR-30, PR-35 and PR-40 again."
    source: "Product Owner, 2026-09-23, while reviewing MODIFICATION-20260923-alpha-feedback-open-entries PART-08"
    disposition: ""
parts:
  - id: PART-01
    name: "A PR-40 reject re-plans through PR-20 in a new session"
    items: [ITEM-01]
    class: A
    after: []
request: |
  Yes, if PR-40 finds a defect, then it must go to remediation and an new PR opened for withi the PR work unit (PR05 for example). That would be the responsibility in this case of a new version of the work unit implementor (PR05-HDE-EPIC040-2) or something, which I would manually seed. then yes it would go through a whole new PR implementation planning process, approval, and review/CI monitoring, then another review.
  I hate to do it, but I need to stick with my plan. if a whole PR cycle fails validation, then it means it was badly executed and yes, needs to route back to PR-20
requested_by: Nathan
analyze_approved_by: Nathan
analyze_approved_date: 2026-09-23
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: MODIFICATION-20260923-alpha-feedback-open-entries
shares_package_with: [MODIFICATION-20260923-alpha-feedback-open-entries]
---

# MODIFICATION-20260923-pr40-reject-replans

When PR-40 rejects landed work for an in-scope defect, the work goes back to PR-20 for a new plan
in a new dedicated session, rather than straight back to PR-30 under the original Proceed.

## Intake

Spawned from `MODIFICATION-20260923-alpha-feedback-open-entries` on 2026-09-23. Its scope froze at
ANALYZE approval, so this is a new run (`D20`). Nathan chose the follow-up over widening the
original.

| item | disposition | evidence | apparent surface |
|---|---|---|---|
| ITEM-01 | **NEW** | Today PR-40's `REJECT` branch `reject_existing_pr_owner` sends "a precise in-scope implementation/review/corrected-code/PR-lineage defect" to **PR-30** under the "original Proceed" (`docs/graph/parts/prompts/PR-40.json`; `contract:15734`). The PR-40 body says PR-30 continuation "requires the original Proceed and a suitable actual authorized implementation vehicle". No record asks for or rules on a re-plan. "Remediation" means a fresh PR-20 planning cycle, not the ESC lane (Nathan, 2026-09-23) | PR-40's route and body; PR-20's entry; PR-30's entry; the single-Proceed rule |

Deduplicated against: the parent Modification (PART-08 step 28 leaves the route alone and points
here), the decision record `D1`–`D22` (no ruling on it), and the Alpha Feedback page (no entry).

## §A — Analysis

**Scope, measured by an exact search for edges and text naming the route.**
- **Graph:** one edge branch, `PR-40.json` `reject_existing_pr_owner` → PR-30. It becomes
  `reject_replan` → PR-20. Only the parts move; `PR-30`'s upstream loses PR-40 and `PR-20`'s gains it.
- **Bodies:** `PR-40`'s *PRECISE IN-SCOPE DEFECT → existing PR owner* branch; `PR-20`'s entry, which
  accepts a PR-40 reject finding; `PR-30`'s entry, where it names a PR-40 return.
- **Registry:** `PR-20` inputs (today only `PR_INSTRUCTION_ID`) and `PR-40` consumers (derived from
  the graph, `D13`).
- **Skills:** the single-Proceed wording in `glow-hde-pr-development` and `change-flow`, and the
  bundled contract (regenerated).
- **The single-Proceed rule, three places:** `global.json:48` ("never a second Proceed"); the Flow
  Index ("It is not restarted or duplicated by … a new session"); and **R1 row GCF-15**, whose stop
  condition is `STOP_SECOND_APPROVAL_OBJECT_REQUESTED`.

**Closure.**
- `PR-40`: upstream `DOC-20`; downstream `PR-10`, `PR-30`, `RS-10`; radius 9.
- `PR-20`: upstream `DOC-10`, `PR-10`; downstream `PR-20`, `RS-10`; radius 21.
- After the change, PR-40 → PR-20 replaces PR-40 → PR-30. The union is a bounded gate, not
  corpus-wide.

**Tier 1. Class A:** it reverses the one-Proceed-per-work-unit rule for the re-plan case, and
re-pins R1 row GCF-15.

**Targets:** graph, prompt (`PR-40`, `PR-20`, `PR-30`), registry, skill (`glow-hde-pr-development`,
`change-flow`, `flowmaster-validate` for the R1 re-pin), rule (`D23`), Notion control (Flow Index
wording).

**Risks.**
- **The R1 re-pin.** GCF-15 joins GCF-17, re-pinned by the parent's PART-09. It is one oracle
  revision, not two.
- **Session identity.** The new session is hand-seeded by Nathan (e.g. `PR05-HDE-EPIC040-2`).
  PR-20's entry must accept a new dedicated session for an existing `WORK_UNIT_ID`, and the parent's
  C-SESSION continuity list is per session pair, so the two compose.
- **The accepted-final protection still holds.** A rejected unit is not accepted-final, so "never
  rerun an accepted-final PR" is untouched.

**Open questions:** none. Nathan settled the destination and the ownership.

**Readiness:** `READY`. **Interaction cost:** 0 rulings + 2 + review 0 + install 0 + merge 0 = **2**.
It shares the parent's package, review, install and execution PR (rule 7), so only the two approvals
are its own.

### Correction to this analysis, 2026-09-23

The EXECUTE preflight of the parent found a factual error above. The paragraph is left as written.
- **The stop condition is on GCF-16, not GCF-15.** `STOP_SECOND_APPROVAL_OBJECT_REQUESTED` belongs to
  GCF-16.
- **GCF-16 already allows the re-plan.** Its approval is "bounded to one Plan … does not authorize …
  another Plan", and its recovery owner is "replan/reinvoke". A new Proceed on a new plan is
  therefore lawful under it.
- **The row the re-plan does change is GCF-17.LINEAGE, PR-40's row.** Its `next` rows (GCF-19,
  GCF-20) give PR-40 no R1 transition back to planning, so its `next` gains GCF-14.
- **Where it is recorded:** in the decision record, as a successor note under `D23`.

The preflight also found three more surfaces the analysis missed:
- the Proceed condition exists in **two** copies in `global.json`, at `:48` (`_other_edges`) and at
  `:311` (`boundary_transitions`), and the builder does not reconcile them;
- `PR-20.json:56` says the plan "awaits the original Product Owner Proceed";
- `PR-40`'s `state_route_order` must be renamed together with the branch, or the builder silently
  moves the row to the end.

## §P — Plan

Written 2026-09-23 by `MODE = PLAN`, after the parent's EXECUTE preflight. This Modification shares
the parent's package, gate, review, delivery and cut-over (rule 7, parent Amendment 1). It has no
execution path of its own.

### Canonical wording

- **C-REPLAN** (the PR-40 `REJECT` branch, replacing *PRECISE IN-SCOPE DEFECT → existing PR owner*):
  > **PRECISE IN-SCOPE DEFECT → re-plan.** When the landed work has a precise in-scope
  > implementation, review, corrected-code or PR-lineage defect, return `REJECT` with the finding in
  > `PR_WORK_UNIT_LINEAGE_REVIEW`, and hand off to `PR-20` for a new per-PR plan for the same
  > `WORK_UNIT_ID`. PR-20 runs in a new dedicated top-level session that Nathan creates and seeds
  > with this handoff; no session is created automatically. That plan goes through
  > its own Product Owner Proceed, then PR-30, PR-35 and PR-40 again. The earlier Proceed is spent
  > and is never reused.
- **C-PROCEED** (the single-Proceed rule, restated):
  > One Proceed per approved per-PR plan. A continuation — PR-30 to PR-35, a rescope return, a
  > recovery — never requires or creates a second Proceed. Only a PR-40 `REJECT` re-plan creates a
  > new plan, and that plan receives its own Proceed.
- **C-PR20-ENTRY** (added to PR-20's entry):
  > **Re-plan entry.** This prompt also accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` whose result is
  > `REJECT` (`reject_replan`) for an existing `WORK_UNIT_ID`. It then runs in a new top-level session
  > that Nathan creates, plans that work unit again from the landed state and the finding, and ends at
  > a new `AWAITING_PO_PROCEED` for the new plan. A pull request merged under an earlier plan cycle is
  > landed history: never resume, reuse or push to it.
- **C-PR30-ENTRY** (replaces PR-30's PR-40 return context):
  > PR-30 starts only from the Proceed of its own plan. A PR-40 finding never returns here directly;
  > it re-plans through PR-20 (`D23-F`).
- **The graph conditions** are the last three rows of the parent's A1-7 table, verbatim.
- **R1** is the parent's A1-1: GCF-17.LINEAGE (`next` gains GCF-14) and GCF-14 (`consumes` gains
  `pr_work_unit_lineage_review`). GCF-14 and GCF-15's session wording is read per plan cycle and
  stays.

C-REPLAN and C-PROCEED avoid two strings that `glow-hde-pr-development`'s validator forbids,
because those strings still guard the rescope and PR-35 cases: "receives its own PO Proceed" and
"normal Plan/instruction path". The forbidden list is not narrowed.

### Steps

| # | target | edit | verification |
|---|---|---|---|
| C1 | graph: `PR-40.json` | Replace the `reject_existing_pr_owner` edge **in place**, keeping edge index 172. Set `to` to PR-20, the branch to `reject_replan`, and the condition per A1-7. Rename the entry in `state_route_order` | build passes; `closure.py PR-40` shows downstream `[PR-10, PR-20, RS-10]`; `closure.py PR-20` shows PR-40 upstream |
| C2 | graph: `PR-20.json:56`; `global.json` `_other_edges` **and** `boundary_transitions.NATHAN_PROCEED` | The conditions per A1-7. Both `global.json` copies must be identical | build passes; the two copies are byte-equal |
| C3 | R1 | GCF-17.LINEAGE and GCF-14 per the parent's A1-1, in the same successor oracle as GCF-17. Add an R1 path fixture, GCF-17.LINEAGE → GCF-14, to `flowmaster-validate/fixtures/change-flow/scenarios.json`. It must fail with `FMV-GCF-EDGE-003` against the historical oracle and pass against the successor | the parent's E4 |
| C4 | bodies (computed at E3, landed at cut-over) | **`PR-40`:** C-REPLAN replaces the existing-PR-owner branch, and the body names PR-20. It keeps "historical pre-merge", "independent" and `glow-merged-change-attribution-lock`. **`PR-20`:** C-PR20-ENTRY is added to its entry. It avoids "when a denial requires correction" (`validate_gcfpe_artifact_timing.py:76`). **`PR-30`:** C-PR30-ENTRY replaces its PR-40 return context, and C-PROCEED replaces the single-Proceed sentence in the bodies that carry it | `PROMPT_HANDOFF_RECEIVER` clean for PR-40 → PR-20; the parent's E4 item 7 |
| C5 | registry | `PR-40` consumers and required interfaces are derived as `[PR-10, PR-20, RS-10]` by the parent's registry deriver, never hand-edited. `PR-20` gains the input "`PR_WORK_UNIT_LINEAGE_REVIEW` with `REJECT` (`reject_replan`) and its in-scope finding, for a re-plan of the same `WORK_UNIT_ID` in a new dedicated session Nathan seeds", as a quoted string. **Guards (`D23-F`):** on `PR-40`, "original Proceed and a suitable actual authorized implementation vehicle" is forbidden (`CTR-001`); on `PR-20`, C-PR20-ENTRY's opening is required, by the pattern `accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT` (`CTR-002`). It first runs as a clean control on today's PR-20 body, so it cannot be vacuous | in-memory evaluation, with each guard fired by an injected regression that yields exactly its own finding |
| C6 | `glow-hde-pr-development` | C-PROCEED at `:10`, `:17-18` and `:27`. One branch and one PR **per plan cycle** at `:77`, `:82` and `:158`. **Recovery is limited to the current plan cycle** at `:41` (recovery steps 3 and 4) and `:77`: a PR merged under an earlier plan cycle is landed history, never resumed, reused or pushed to. A behaviour case `## PR-40 rejection re-plan`, added to `case_headings`, covers a merged prior PR, for which a new branch and PR are created. A new required literal from C-PROCEED. The forbidden entry "followed in the same session by PR-35" is added, and no existing entry is narrowed. Lines `:10`, `:27` and `:158` are also edited by the parent's step 35, so each gets one combined replacement | the skill's validator passes; the old `:27` sentence, injected, fails with exactly that finding |
| C7 | `change-flow` | `:313` and `:323` stay **verbatim**: they are rescope sentences whose rule C-PROCEED keeps, and they also carry the accepted-final and PR-50 prohibitions. C-PROCEED is appended as its own sentence after `:301`. `:455` (GCF-17.LINEAGE) follows the successor row | the parent's gate |
| C8 | `flowmaster-validate` | Fixtures. A positive case: PR-40 `REJECT` → PR-20 in a new session → a new Proceed on the new plan is accepted. Three negatives: a second Proceed on the same plan, a second Proceed between PR-30 and PR-35, and PR-40 `REJECT` routed to PR-30. A contract assertion that the PR-40 `REJECT` branch targets PR-20. `ROUTE_GRAPH_SHORTHAND` gains `pr40_reject_replan`: PR-40, PR-20, `NATHAN_PROCEED`, PR-30. `rescope_contract.new_proceed_required` stays `false`, because it concerns rescope | fixture suite passes; each negative fails for its own reason |
| C9 | contract (by the parent's regenerator) | `receiver_compatibility.PR-20` accepts a PR-40 `REJECT` finding and a new top-level session for an existing `WORK_UNIT_ID`, with a new Proceed. `receiver_compatibility.PR-30` is unchanged: it never had a PR-40 return context. The route shorthand is as in C8 | the parent's new v4 `receiver_compatibility` content check (A1-6). No entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` `REJECT`, and a regression that gives one to PR-30 must fail |
| C10 | `amthor-workspace-governance-audit` | `SKILL.md:44` becomes "one Proceed per plan cycle" under C-PROCEED. `:43` gains the plan-cycle recovery rule | its fixture suite passes |
| C11 | Notion: Flow Index | "It is not restarted or duplicated by … a new session" gains "except a PR-40 `REJECT` re-plan, which is a new plan with its own Proceed (`D23-F`)". Made at cut-over | readback |

**Order:** C1–C2 go with the parent's E1, C3 and C6–C10 with E2, C4 with E3, and C5 with E1. C11 is
made at the cut-over. Everything is gated by the parent's E4, reviewed in its E5 and delivered in its
E6.

### Product Owner actions

None of its own. Nathan approves this plan together with the parent's Amendment 1. The merge,
install and freeze are shared.

### Not in scope

- Rescope's single Proceed (`rescope_contract.new_proceed_required: false`), which is unchanged.
- The ESC remediation lane.
- The DOC lane's PR-40 entry.

### Interaction cost

Predicted 2: its analysis approval and its plan approval. The plan approval is taken together with
the parent's amendment.
