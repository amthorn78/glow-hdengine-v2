---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "2.1"
created_date: 2026-09-22
revised_date: 2026-09-24 — format 2.1, D26
status: BINDING
authority: Product Owner decisions D20 (2026-09-22), D21 (2026-09-23) and D26 (2026-09-24)
validated_by: docs/prompt_ecosystem_management/modification_validate.py
---

# The Modification — template and format

**One run is one Modification** (`D21`). Everything handed in together goes through `ANALYZE`,
`PLAN` and `EXECUTE` together, with one approval per mode. A list of six unrelated changes is one
Modification, not six.

**Parts carry failure.** Inside a Modification, a part is the changes that must land together —
one rule across its surfaces, above all. A part lands whole or not at all (rule 6 has the one
carve-out). Parts land independently of each other unless one is ordered `after` another. A
Modification with no `parts` is a single part.

**Format 2.1** (`D26`) adds `format`, `estimate` and the `reviews` ledger. A record with no
`format` is a legacy record and validates as it always did; a record begun before `D26` adopts
2.1 when it next changes mode: that mode sets `estimate` for the work still to come, starts the
ledger empty, and cites earlier review rounds from the RCA rather than entering them.

**Not a "Change Record", never `CR`.** `CRD` appears 2,694 times in `docs/`, and `CHANGE_RECORD`
is already `GCFPE-MGMT-10`'s own declared output artifact at
`project-prompt-contract-registry.md:2310`.

Modifications live at `docs/ephemeral/modifications/MODIFICATION-<yyyymmdd>-<slug>.md`.

Copy everything between the markers. Delete the comments; keep the keys.

## Rules the format exists to enforce

1. **Each mode writes only its own section.** Triage writes `## Intake`; `PLAN` never rewrites §A;
   `EXECUTE` never rewrites §P. A mode that believes an upstream section is wrong records a finding
   and returns to the Product Owner with a `DECISION NEEDED` — it does not edit upstream, and it
   does not carry on past the finding (`AUTH-001` applied to this document's internal structure).
2. **Approval is a recorded field, not a remembered fact.** `analyze_approved_by` empty blocks
   `PLAN`; `plan_approved_by` empty blocks `EXECUTE`. That is what lets one session carry the
   whole process and a fresh one resume it. **A merge preserves the record; it approves nothing**
   (`D21-C`).
3. **Scope freezes at `ANALYZE` approval.** The `items` list may not grow afterwards. A part may
   still be dropped, with the reason recorded as its items' disposition. New scope is a new
   Modification with `spawned_from` set — never a wider one. It bounds scope, not review rounds;
   rule 8 bounds those. A finding outside the frozen scope is recorded on the GCFPE Modification Backlog (Notion,
   `3e54590a05eb81eb818fd0f42045167a`) with a severity, and a later run takes it as an item.
4. **Every §P step carries a verification that could fail.** A step whose check is "read it and
   see" is not a step (`CHK-001`, `D11`). **A rule change's verification also searches for
   surviving old text** the new rule contradicts, by broad match minus permitted exceptions
   (`SCOPE-001`, `D26-E`) — not only for the new wording.
5. **Every §E step and item carries a disposition.** A skipped step is a recorded disposition,
   never an omission. Silence is impossible by construction. **A stop is a disposition too:** the
   steps after it are `NOT_RUN`, each citing the stop.
6. **A part lands whole or not at all.** A part with some items applied and others blocked fails
   validation. Roll back what was applied, or unblock the rest. **The one carve-out (`D26-B`):**
   where a rollback would need a copy of a Notion prompt body that `D22` forbids, the rollback is
   Nathan's restoration from Notion page history. The part is recorded `BLOCKED` with its applied
   steps named, the Modification stays `EXECUTING` until he has restored them, and nothing further
   is automated.
7. **Every part that changes the same skill ships in one package, one review and one install.**
   Across separate runs, `PLAN` may share a package too: it names the other Modifications in
   `shares_package_with`, the shared package is built only once every sharing plan is approved,
   and its review, install and merge are counted once in `interaction_cost`. If the review
   rejects one part's edit, that part is blocked. By default the package is fixed and reviewed
   again; Nathan may instead ship the rest without it.
8. **Reviews are bounded (`D26-A`).** For `ANALYZE`, `PLAN` and skill reviews alike: a dry run
   first; then at most two full reviews and one check of the repair's diff per mode; then the
   output goes to Nathan with every open finding listed by path, likelihood and consequence. Only
   the four required kinds are repaired — a normal-path defect, a silent wrong edit to a body,
   governed document or control page, a silent breach of a ruling, and a plausible path with a
   silent or destructive outcome. Everything else is listed in §P as an accepted risk. Stop early
   and return to Nathan when required defects do not at least halve, when most sit in text the last
   repair added, or at twice the estimate. Every round goes in the `reviews` ledger. A session never
   tightens an exit rule, and names who set any it states. A third full review, or a first `PLAN`
   review without a dry run, needs Nathan's `override` (`review_cap`, `dry_run`).

## The Product Owner is never blocked by any of this

**`readiness` is advisory.** It reports what `ANALYZE` concluded. It does not refuse, and
`NEEDS_RULING` means *this wants your decision*, not *you must wait*.

Every gate here exists to stop a **session** proceeding on its own judgement. None of them exists
to stop Nathan. Where a policy gate would otherwise fail — scope freeze above all — an `override`
block waives it:

```yaml
override:
  by: Nathan
  overrides: [scope_freeze]
  reason: "needed now"
```

The `reason` is so a successor session knows the waiver was deliberate. **It is not a
justification anyone is owed** — "I need it" is a complete reason.

An override waives a **policy** gate. It cannot make a malformed record well-formed: a missing
section or an absent disposition is the document failing to say what happened, and waiving that
would only make the record lie.

---

## TEMPLATE BEGINS

```markdown
---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"             # D26; a record with no format is a legacy record
modification_id: MODIFICATION-20260923-example-slug
status: INTAKE            # INTAKE ANALYZING ANALYZED PLANNING PLANNED EXECUTING COMPLETE BLOCKED ABANDONED
targets: []               # union across parts: prompt skill rule graph registry notion_control tool
gate_tier:                # 0 1 2 -- the highest across parts, computed from closure.py, never judged
closure:                  # computed; do not type these by hand
  upstream: []
  downstream: []
  state_sharers: []
readiness:                # READY | SPLIT_RECOMMENDED | NEEDS_RULING -- ADVISORY, never blocks
override:                 # optional; the Product Owner waiving a policy gate
  by: ""                  # overridable: scope_freeze readiness modification_class gate_tier deferral review_cap dry_run
  overrides: []
  reason: ""              # for a successor reading the record, not a justification owed to anyone
interaction_cost_predicted:
interaction_cost_actual:  # filled in §E; this is what calibrates the prediction
estimate:                 # set by ANALYZE, required from ANALYZED: time and tokens, e.g. "3 h, 1.5M tokens"
  plan: ""
  execute: ""
reviews: []               # every ANALYZE, PLAN and SKILL review round, in order (rule 8, D26-A):
#  - mode: PLAN           # ANALYZE PLAN SKILL
#    kind: DRY_RUN        # DRY_RUN FULL DIFF_CHECK -- at most 2 FULL and 1 DIFF_CHECK per mode
#    date: 2026-09-24
#    required_open: 0     # distinct confirmed required defects open after the round
#    outcome: "one line: what it found, and what happened next"
items:
  - id: ITEM-01           # numbered once across the run
    statement: "one sentence of requested outcome"
    source: ""            # the entry it came from, e.g. AF-008; empty for a new request
    disposition: ""       # filled in §E: APPLIED VERIFIED BLOCKED NOT_APPLICABLE
parts:                    # every item in exactly one part; a part lands whole or not at all
  - id: PART-01
    name: "what this part changes, in a few words"
    items: [ITEM-01]
    class:                # A B C D E -- set by ANALYZE; ecosystem-change-management.md §2
    after: []             # parts that must land before this one
request: "the request, as received, verbatim -- never a copy of an entry's text; source names it"
requested_by: Nathan
analyze_approved_by: ""   # empty blocks PLAN
analyze_approved_date: ""
plan_approved_by: ""      # empty blocks EXECUTE
plan_approved_date: ""
supersedes: ""
spawned_from: ""          # the Modification that found this scope, if any
shares_package_with: []   # set by PLAN, rarely: another run changing the same skill (rule 7)
---

# MODIFICATION-20260923-example-slug

One sentence: what this changes and why.

## Intake

*Written by triage at INTAKE. Every item handed in, whatever its disposition, with its evidence —
an item that does not become part of the work lives only here. Then the parts: why each part's
items must land together, and any order or tension between parts. Absent when the Modification
did not come through triage.*

## §A — Analysis

*Written by MODE = ANALYZE. Frozen once approved.*

### Per part: closure, tier, class and targets

For each part: the output of `closure.py` for every prompt it touches, pasted; its tier, and why —
anything that changes what a prompt *produces* rather than how it *routes* is Tier 1 regardless
of the graph part; its class A–E; and its targets, with the gates each implies. The
Modification's tier is the highest of its parts'.

### Scope, and how it was measured

Broad match minus permitted exceptions, never an enumeration of known phrasings (`SCOPE-001`).
State the method beside the number.

### Contradictions and risks

Including any defect class from `ecosystem-change-management.md` §4 this matches.

### Open questions for the Product Owner

Each one is a round trip and can invalidate planned work. If this list is non-empty, readiness
is `NEEDS_RULING` — which is advice, not a refusal.

### Readiness and interaction cost

    interaction_cost = open rulings + 2 + ANALYZE and PLAN review rounds + skill review cycles
                       + installs + merges

State the number, its breakdown, and what moving a part to a separate run would save. No
threshold, no score. Then set `estimate`: the time and tokens `PLAN` and `EXECUTE` will take,
review rounds included. At twice the estimate the session re-prices to Nathan (rule 8).

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

Ordered steps, grouped by part. Each names its part, its target, the exact edit, its authority,
its verification and its rollback. A plan is complete when it could be executed mechanically with
no interpretation **on its normal path**. A failure path ends with a record, a stop and a return
to Nathan (`D26-B`): a failure record committed to `main` in a record pull request, a read-only
sweep, the freeze kept. The plan builds no machinery beyond that, and resumes only at checkpoints
(`D26-C`).

A plan stopped before approval resumes as a successor section below the dated plan, never as a
rewrite of it.

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

### Open findings, accepted as risks

Every finding still open when the plan goes to Nathan, by path, likelihood and consequence, each
with the reason it is listed rather than repaired (rule 8). Approving the plan accepts them
(`DISP-001`). `NONE` if there are none.

### Product Owner actions

Merge, install, promote — named, with how each is verified.

### Explicitly not in scope

## §E — Execution

*Written by MODE = EXECUTE. Requires plan_approved_by.*

| step | part | disposition | evidence |
|---|---|---|---|
| 1 | | | |

### Parts

Each part's outcome: landed whole, or blocked with its applied steps rolled back.

### Artifacts produced

Path, and how each was read back.

### Interaction cost, actual against predicted

Predicted N. Actual N. If they differ, why — this is the calibration data, and it is the reason
the estimate is a measurement rather than an opinion.

### Remaining Product Owner actions
```

## TEMPLATE ENDS

---

## Validate before claiming a mode is done

```
PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/modification_validate.py \
    docs/ephemeral/modifications/MODIFICATION-*.md
```

The validator is what makes the mode gates mechanical rather than advisory. This ecosystem's most
expensive lesson is that **narrating a rule is not applying it** — a rule was broken three times,
twice in the file that states it. A validator is the fix that documentation cannot be.
