---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261005-gtwpe-second-repair
status: ANALYZING
targets: []
gate_tier:
closure:
  upstream: []
  downstream: []
  state_sharers: []
readiness:
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted:
interaction_cost_actual:
estimate:
  plan: ""
  execute: ""
reviews: []
items:
  - id: ITEM-01
    statement: "GTWPE-MGMT-10 has a route for a skill part, with a skill check layer modelled on the GCFPE skill review (D24): a reviewer brief committed before any reviewer is spawned; two fresh, independent reviewer subagents, each returning SKILL_FIT_CONFIRMED against the same package digests; Nathan's install; then a post-install digest comparison and validation."
    source: "Request outcome 1; candidate C5 with finding F-2 of MODIFICATION-20260930-gtwpe-tw-model-advice; Nathan, 2026-09-30: \"the change manager needs a skill check layer like the gcfpe one has\""
    disposition: ""
  - id: ITEM-02
    statement: "A check that removed text is gone matches the removed phrase, so kept text that only shares a word with it does not stop the run."
    source: "Request outcome 2; finding E-F1 of MODIFICATION-20260930-gtwpe-tw-model-advice (GTWPE error ledger E-028)"
    disposition: ""
  - id: ITEM-03
    statement: "GTWPE-MGMT-10's body states Nathan's merge rule, that no Modification branch is merged before its record is COMPLETE except the pull requests the plan itself opens, and says which pull request carries a failure record."
    source: "Request outcome 3; candidate C9 of MODIFICATION-20260929-gtwpe-first-repair (GTWPE error ledger E-027); Nathan's rule of 2026-09-29"
    disposition: ""
  - id: ITEM-04
    statement: "When a change alters how the TW flow runs, the same run updates the Current operation section of the Glow Technical Writing Ecosystem page, so it never lags the selected release."
    source: "Request outcome 4; GTWPE error ledger E-029"
    disposition: ""
parts: []
request: |
  PE38 here, PE37's successor as facilitator, on 2026-10-05.

  The TW prompts repair is accepted. MODIFICATION-20260930-gtwpe-tw-model-advice is COMPLETE on main (#568). Run from main, modification_validate.py and gtwpe_record_check.py each pass all three GTWPE records (3/3), and the record check's selftest passes 17/17. The selection page shows TW-ALPHA-20261004.1.

  One change since your run, so your drift check expects it: on Nathan's direction, PE38 edited the "Glow Technical Writing Ecosystem" page directly (edited 2026-10-05T00:30:29Z). It added a *Current operation* section for TW-ALPHA-20261004.1 under the selected release: no assessment step, no model advice, next manual entry the selected drain prompt. It also marked the TW-ALPHA-20260908.1 operation and runtime-limit sections historical. Treat the page as it now stands and do not redo that edit.

  Next: run GTWPE-MGMT-10's second repair through GTWPE-MGMT-10 092926.2 itself (ANALYZE, PLAN, EXECUTE). Follow the published body live and stop at each of Nathan's approvals. Keep it small. Four outcomes:

  1. A skill route with a skill check layer. GTWPE-MGMT-10 gains a route for a skill part, with a check layer modelled on the GCFPE skill review (D24 in gcfpe.decision-record.md):
     - a reviewer brief committed before any reviewer is spawned;
     - two fresh, independent reviewer subagents, each returning SKILL_FIT_CONFIRMED against the same package digests;
     - Nathan installs;
     - then a post-install digest comparison and validation.
     This way a skill part runs through the change prompt instead of around it, as the TW prompts repair had to do. This is candidate C5 (with F-2) of MODIFICATION-20260930-gtwpe-tw-model-advice. Nathan: "the change manager needs a skill check layer like the gcfpe one has".
  2. Absence checks match phrases, not single words. A check that removed text is gone matches the removed phrase, so kept text that only shares a word with it does not stop the run. This is E-F1 of the TW prompts repair, where "reasoning" matched a kept TW-TRIAGE-10 sentence.
  3. Nathan's merge rule in the body. No Modification branch is merged before its record is COMPLETE, except the pull requests the plan itself opens. The body also says which pull request carries a failure record. This is candidate C9 of MODIFICATION-20260929-gtwpe-first-repair.
  4. The selection page's *Current operation* stays current. When a change alters how the TW flow runs, the same run updates that section on the "Glow Technical Writing Ecosystem" page, so it never lags the selected release again. This gap is why PE38 had to fix the page by hand today.

  Nothing else in GTWPE-MGMT-10 changes. Candidate C8 (the find rule) and the other recorded candidates stay out.

  Standing directions:
  - Nathan: "this flow can be simplified, let's not overcomplicate this".
  - Keep PLAN lean: one dry run and one full review by a single reviewer. Add a second reviewer or a diff check only if that review finds a required defect.
  - Stop rather than produce substandard results. The stop rule's meter is time.
  - No Modification branch is merged before its record is COMPLETE, except the pull requests the plan itself opens.
  - Report to Nathan in at most five plain sentences, in plain language, ending with exactly what he must approve.
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: MODIFICATION-20260930-gtwpe-tw-model-advice
shares_package_with: []
---

# MODIFICATION-20261005-gtwpe-second-repair

GTWPE-MGMT-10's second repair: a route for skill parts with a skill check layer, absence checks
that match phrases, Nathan's merge rule in the body, and the TW selection page's *Current
operation* kept current by the run that changes the flow.

## Intake

Not through triage. The request came from PE38 on 2026-10-05 and is copied verbatim in the front
matter. Its four numbered outcomes are ITEM-01 to ITEM-04; its sentence "Nothing else in
GTWPE-MGMT-10 changes" bounds all four, and it keeps candidate C8 and the other recorded candidates
out.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

In progress.
