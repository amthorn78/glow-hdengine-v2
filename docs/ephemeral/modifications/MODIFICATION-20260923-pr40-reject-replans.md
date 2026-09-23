---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-pr40-reject-replans
status: PLANNING
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
