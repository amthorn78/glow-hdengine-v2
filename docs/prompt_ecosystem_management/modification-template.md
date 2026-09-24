---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "2.0"
created_date: 2026-09-22
revised_date: 2026-09-23
status: BINDING
authority: Product Owner decisions D20 (2026-09-22) and D21 (2026-09-23)
validated_by: docs/prompt_ecosystem_management/modification_validate.py
---

# The Modification — template and format

**One run is one Modification** (`D21`). Everything handed in together goes through `ANALYZE`,
`PLAN` and `EXECUTE` together, with one approval per mode. A list of six unrelated changes is one
Modification, not six.

**Parts carry failure.** Inside a Modification, a part is the changes that must land together —
one rule across its surfaces, above all. A part lands whole or not at all. Parts land
independently of each other unless one is ordered `after` another. A Modification with no
`parts` is a single part.

**Not a "Change Record", never `CR`.** `CRD` appears 2,694 times in `docs/`, and `CHANGE_RECORD`
is already `GCFPE-MGMT-10`'s own declared output artifact at
`project-prompt-contract-registry.md:2310`.

Modifications live at `docs/ephemeral/modifications/MODIFICATION-<yyyymmdd>-<slug>.md`.

Copy everything between the markers. Delete the comments; keep the keys.

## Rules the format exists to enforce

1. **Each mode writes only its own section.** Triage writes `## Intake`; `PLAN` never rewrites §A;
   `EXECUTE` never rewrites §P. A mode that believes an upstream section is wrong records a finding
   and returns — it does not edit upstream (`AUTH-001` applied to this document's internal
   structure).
2. **Approval is a recorded field, not a remembered fact.** `analyze_approved_by` empty blocks
   `PLAN`; `plan_approved_by` empty blocks `EXECUTE`. That is what lets one session carry the
   whole process and a fresh one resume it. **A merge preserves the record; it approves nothing**
   (`D21-C`).
3. **Scope freezes at `ANALYZE` approval.** The `items` list may not grow afterwards. A part may
   still be dropped, with the reason recorded as its items' disposition. New scope is a new
   Modification with `spawned_from` set — never a wider one. This is what bounds the review loops.
   A finding outside the frozen scope is recorded on the GCFPE Modification Backlog (Notion,
   `3e54590a05eb81eb818fd0f42045167a`) with a severity, and a later run takes it as an item.
4. **Every §P step carries a verification that could fail.** A step whose check is "read it and
   see" is not a step (`CHK-001`, `D11`).
5. **Every §E step and item carries a disposition.** A skipped step is a recorded disposition,
   never an omission. Silence is impossible by construction.
6. **A part lands whole or not at all.** A part with some items applied and others blocked fails
   validation. Roll back what was applied, or unblock the rest.
7. **Every part that changes the same skill ships in one package, one review and one install.**
   Across separate runs, `PLAN` may share a package too: it names the other Modifications in
   `shares_package_with`, the shared package is built only once every sharing plan is approved,
   and its review, install and merge are counted once in `interaction_cost`. If the review
   rejects one part's edit, that part is blocked. By default the package is fixed and reviewed
   again; Nathan may instead ship the rest without it.

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
modification_id: MODIFICATION-20260923-example-slug
status: INTAKE            # INTAKE ANALYZING ANALYZED PLANNING PLANNED EXECUTING COMPLETE BLOCKED ABANDONED
targets: []               # union across parts: prompt skill rule graph registry notion_control
gate_tier:                # 0 1 2 -- the highest across parts, computed from closure.py, never judged
closure:                  # computed; do not type these by hand
  upstream: []
  downstream: []
  state_sharers: []
readiness:                # READY | SPLIT_RECOMMENDED | NEEDS_RULING -- ADVISORY, never blocks
override:                 # optional; the Product Owner waiving a policy gate
  by: ""                  # overridable: scope_freeze readiness modification_class gate_tier deferral
  overrides: []
  reason: ""              # for a successor reading the record, not a justification owed to anyone
interaction_cost_predicted:
interaction_cost_actual:  # filled in §E; this is what calibrates the prediction
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

    interaction_cost = open rulings + 2 + review cycles + installs + merges

State the number, its breakdown, and what moving a part to a separate run would save. No
threshold, no score.

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

Ordered steps, grouped by part. Each names its part, its target, the exact edit, its authority,
its verification and its rollback. A plan is complete when it could be executed mechanically with
no interpretation.

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

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
