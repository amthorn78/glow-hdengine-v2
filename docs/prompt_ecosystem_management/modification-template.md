---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-22
status: BINDING
authority: Product Owner decision D20, 2026-09-22
validated_by: docs/prompt_ecosystem_management/modification_validate.py
---

# The Modification — template and format

One Modification per change. It is the unit of **approval and verification**, not the unit of
"one thing" — items batch into it when they share a rule, a verification, or a
package/review/install cycle (`D20`, and §3.2 of the redesign plan).

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
   `PLAN`; `plan_approved_by` empty blocks `EXECUTE`. That is what makes a Modification survive a
   session ending mid-change.
3. **Scope freezes at `ANALYZE` approval.** The `items` list may not grow afterwards. New scope is
   a new Modification with `spawned_from` set — never a wider one. This is what bounds the review
   loops.
4. **Every §P step carries a verification that could fail.** A step whose check is "read it and
   see" is not a step (`CHK-001`, `D11`).
5. **Every §E step and item carries a disposition.** A skipped step is a recorded disposition,
   never an omission. Silence is impossible by construction.
6. **Modifications that change the same skill share one package, one review and one install.**
   Product Owner decision, 2026-09-23. `PLAN` names the others in `shares_package_with`, and the
   shared package is built only once every sharing Modification's plan is approved. Each
   Modification keeps its own approval, coupling, steps and dispositions. The shared review,
   install and merge are counted once in `interaction_cost`, on the first Modification named,
   and as 0 on the rest. If the review rejects one Modification's edit, that Modification is
   blocked. By default the package is fixed and reviewed again; Nathan may instead ship the others
   without it.

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
modification_id: MODIFICATION-20260922-example-slug
status: INTAKE            # INTAKE ANALYZING ANALYZED PLANNING PLANNED EXECUTING COMPLETE BLOCKED ABANDONED
intake_record: ""         # INTAKE-<yyyymmdd>-<slug>.md beside this file, written by triage; empty if none
coupling:                 # ATOMIC = one act, a failure stops all. INDEPENDENT = per-item. No default: someone decides it
targets: []               # any of: prompt skill rule graph registry notion_control
gate_tier:                # 0 1 2 — computed from closure.py and the rebuilt part, never judged
closure:                  # computed; do not type these by hand
  upstream: []
  downstream: []
  state_sharers: []
readiness:                # READY | SPLIT_RECOMMENDED | NEEDS_RULING -- ADVISORY, never blocks
override:                 # optional; the Product Owner waiving a policy gate
  by: ""                  # overridable: scope_freeze readiness modification_class gate_tier deferral
  overrides: []
  reason: ""              # for a successor reading the record, not a justification owed to anyone
modification_class:       # A B C D E — ecosystem-change-management.md §2
interaction_cost_predicted:
interaction_cost_actual:  # filled in §E; this is what calibrates the prediction
items:
  - id: ITEM-01
    statement: "one sentence of requested outcome"
    source: ""            # the entry it came from, e.g. AF-008; empty for a new request
    disposition: ""       # filled in §E: APPLIED VERIFIED BLOCKED NOT_APPLICABLE
request: "the request, as received, verbatim -- never a copy of an entry's text; source names it"
requested_by: Nathan
analyze_approved_by: ""   # empty blocks PLAN
analyze_approved_date: ""
plan_approved_by: ""      # empty blocks EXECUTE
plan_approved_date: ""
supersedes: ""
spawned_from: ""          # the Modification that found this scope, if any
shares_package_with: []   # set by PLAN: other Modifications changing the same skill (rule 6)
---

# MODIFICATION-20260922-example-slug

One sentence: what this changes and why.

## Intake

*Written by triage at INTAKE: why these items belong together, and any link to another group — a
shared skill, an order, a tension. Absent when the Modification did not come through triage.*

## §A — Analysis

*Written by MODE = ANALYZE. Frozen once approved.*

### Closure and gate tier

Output of `closure.py`, pasted. Which tier, and why — including whether anything here changes
what a prompt *produces* rather than how it *routes*, which forces Tier 1 regardless of the
graph part.

### Targets and coupling

What this touches, and the gates each target implies. Why ATOMIC or INDEPENDENT.

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

State the number, its breakdown, and what a split would save. No threshold, no score.

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

Ordered steps. Each names its target, the exact edit, its authority, its verification and its
rollback. A plan is complete when it could be executed mechanically with no interpretation.

| # | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|
| 1 | | | | | |

### Product Owner actions

Merge, install, promote — named, with how each is verified.

### Explicitly not in scope

## §E — Execution

*Written by MODE = EXECUTE. Requires plan_approved_by.*

| step | disposition | evidence |
|---|---|---|
| 1 | | |

### Artifacts produced

Path, and how each was read back.

### Interaction cost, actual against predicted

Predicted N. Actual N. If they differ, why — this is the calibration data, and it is the reason
the estimate is a measurement rather than an opinion.

### Remaining Product Owner actions
```

## TEMPLATE ENDS

---

## The intake record — one per triage run

Triage writes one intake record per run, at
`docs/ephemeral/modifications/INTAKE-<yyyymmdd>-<slug>.md`, beside the drafts it creates, and
commits them together. **It is the only home for an item that does not become a Modification** —
a duplicate, an already-ruled item, an already-true one. Without it, those answers exist only in a
chat that ends. Each draft's `intake_record` names it, and the validator checks that the record
exists and lists that draft.

## INTAKE RECORD BEGINS

```markdown
---
artifact_type: GCFPE_INTAKE_RECORD
intake_id: INTAKE-20260922-example-slug
created_date: 2026-09-22
requested_by: Nathan
request: "what Nathan pasted, verbatim"
modifications: [MODIFICATION-20260922-example-slug]
---

# INTAKE-20260922-example-slug

## A. Items

Every item, whatever its disposition.

| # | source | statement | disposition | evidence | apparent surface (unmeasured) |
|---|---|---|---|---|---|
| 1 | AF-008 | one sentence of requested outcome | NEW | | |

Evidence is required for NOT_A_CHANGE (the file and line, or field, showing it is already true),
DUPLICATE_OF (the id) and ALREADY_RULED (the D-number).

## B. Grouping

| Modification | items | coupling | why these belong together |
|---|---|---|---|

Links between groups: a shared skill (rule 6), an order, a tension.

## Validator output

Pasted, not described.
```

## INTAKE RECORD ENDS

---

## Validate before claiming a mode is done

```
PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/modification_validate.py \
    docs/ephemeral/modifications/MODIFICATION-*.md
```

The validator is what makes the mode gates mechanical rather than advisory. This ecosystem's most
expensive lesson is that **narrating a rule is not applying it** — a rule was broken three times,
twice in the file that states it. A validator is the fix that documentation cannot be.
