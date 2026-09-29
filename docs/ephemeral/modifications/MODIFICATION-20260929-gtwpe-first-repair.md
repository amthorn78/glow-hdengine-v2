---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20260929-gtwpe-first-repair
status: ANALYZING
targets: [prompt, notion_control, tool]
gate_tier: 1
closure:
  upstream: []
  downstream: []
  state_sharers: []
readiness: NEEDS_RULING
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
    statement: "When GTWPE-MGMT-10 selects a new TW-ALPHA release, no other page goes on naming the superseded release unnoticed: ANALYZE finds every page that names TW's current release, the plan updates each one or lists it for Nathan as his ruling on Q1 sets, and `notion_control` names the pages the route writes."
    source: "Pilot findings PF-4, PF-1 and PF-D3 (MODIFICATION-20260929-gtwpe-pilot); Q1 below"
    disposition: ""
  - id: ITEM-02
    statement: "For any prompt change, ANALYZE finds every page that names the member's current version or links its page, and records whether the route writes each one."
    source: "Pilot finding PF-5"
    disposition: ""
  - id: ITEM-03
    statement: "The stop at twice the estimate has a meter the session can read: elapsed time, recorded when each mode starts and checked at every step boundary, with tokens recorded only where the session can read them without opening a file that holds a prompt body, and otherwise recorded as not measured."
    source: "Pilot finding PF-14; reproduced in this ANALYZE (Harness files)"
    disposition: ""
  - id: ITEM-04
    statement: "No Notion write is read back before it has landed: the session waits for each write to complete, polls any pending task until it reports success, and treats a failed task as a tool error."
    source: "Pilot finding PF-21 (the pilot's full review, RA-1 and PLB-1)"
    disposition: ""
  - id: ITEM-05
    statement: "A rollback never reverts other work and never fails for want of matching text: a page other sessions also write is rolled back only by reversing this Modification's own replacement, with the text taken from that write's readback, and is never restored from page history."
    source: "Pilot findings PF-22 and PF-27"
    disposition: ""
  - id: ITEM-06
    statement: "Exact facts come from fetched pages, never from Notion search: edit times, the register's selection and whether a title is already taken under a parent are read from fetches, and search is used only to discover pages."
    source: "Pilot findings PF-26 and PF-10; reproduced in this ANALYZE's drift check"
    disposition: ""
  - id: ITEM-07
    statement: "After a context compaction drops a prompt body read earlier in the mode, the session fetches it live again and never recovers it from a transcript; a count over a body says whether it was made by reading or by a command over the harness's save of a fetch; and before PLAN a quotation from a body is no longer than the defective clause."
    source: "Pilot findings PF-28, PF-2 and PF-17"
    disposition: ""
  - id: ITEM-08
    statement: "The body says where its Notion writes are made: from the managing session, on whatever surface it runs, because no AI product is a governance requirement (HDE Build Notes, PF10-AINEUTRAL-001), and the surface confers no permission."
    source: "Pilot findings PF-23 and PF-25; GTWPE ledger E-026"
    disposition: ""
  - id: ITEM-09
    statement: "A review in ANALYZE or PLAN follows one capture rule: its brief replaces the template's instruction to write a record with the write-nothing clause, and the reviewer's return is captured unedited, in whichever mode it ran, to a named evidence file under the Modification's evidence directory."
    source: "Pilot findings PF-12 and PF-20"
    disposition: ""
  - id: ITEM-10
    statement: "After every push, the Modification's branch has an open pull request, which gates nothing, so that the record, and any failure record, reach main when Nathan merges."
    source: "Pilot finding PF-24 (the pilot plan's K-13)"
    disposition: ""
  - id: ITEM-11
    statement: "The body's validation command runs the GTWPE record check of ITEM-17, which runs modification_validate.py and the GTWPE's own record rules."
    source: "Pilot finding PF-13"
    disposition: ""
  - id: ITEM-12
    statement: "ANALYZE branches from origin/main, commits and pushes the record at A1, and a restarted ANALYZE that finds its record already on a branch continues there instead of creating a second."
    source: "Pilot findings PF-8 and PF-9"
    disposition: ""
  - id: ITEM-13
    statement: "The drift check names its D26-E search: the terms of each change, searched in this prompt's body as fetched at the start of the mode and in docs/prompt_ecosystem_management/gtwpe/ at the commit examined."
    source: "Pilot finding PF-11"
    disposition: ""
  - id: ITEM-14
    statement: "A repaired TW-ALPHA member carries everything outside its approved edits unchanged, including its model-advice block, even where the PE Metaprompt's authoring exclusion would remove it (design D-17)."
    source: "Pilot finding PF-6"
    disposition: ""
  - id: ITEM-15
    statement: "The interaction cost counts every round in reviews, dry runs included, and every pull request Nathan merges, the record's included."
    source: "Pilot finding PF-15"
    disposition: ""
  - id: ITEM-16
    statement: "Each mode's dry run records its gates and results in a Dry run subsection of that mode's section."
    source: "Pilot finding PF-3"
    disposition: ""
  - id: ITEM-17
    statement: "A GTWPE record check, docs/prompt_ecosystem_management/gtwpe/gtwpe_record_check.py, runs modification_validate.py and adds the GTWPE's own record rules (the record is marked ecosystem GTWPE; each mode section it has reached carries a Harness files subsection; each mode that ran a dry run carries a Dry run subsection), with a selftest at 100% and a guard proof, and the pilot's record passes it."
    source: "Pilot findings PF-13, PF-3 and PF-D1; GTWPE ledger E-025"
    disposition: ""
parts:
  - id: PART-01
    name: "GTWPE-MGMT-10's next version, carrying the pilot's repairs"
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06, ITEM-07, ITEM-08, ITEM-09, ITEM-10, ITEM-11, ITEM-12, ITEM-13, ITEM-14, ITEM-15, ITEM-16]
    class: D
    after: [PART-02]
  - id: PART-02
    name: "The GTWPE record check and its selftest"
    items: [ITEM-17]
    class: C
    after: []
request: |
  PE37 accepted the pilot on 2026-09-29. The record passes main's validator at COMPLETE, the selftest passes 66/66, and PE37 re-read the new TW-MGMT-10 092926.1 page and the selection page live: both are correct.

  Next: run GTWPE-MGMT-10's first real repair, as a GTWPE-MGMT-10 Modification (ANALYZE, PLAN, EXECUTE), following the published body live and stopping at each of Nathan's approvals as in the pilot. It is design v1.2 §13.2's "After it" step.

  Scope:
  1. The pilot's findings against GTWPE-MGMT-10, PF-1 to PF-28, and the design findings PF-D1 to PF-D3. Fix first the ones that can give a wrong or unsafe result without anyone noticing: PF-4 and PF-5 (pages that name the current version), PF-14 (the stop rule has no meter), PF-21 (reading back before a Notion update lands), PF-22 and PF-27 (rollback), PF-26 (Notion search no longer exact), PF-28 (context compaction mid-mode), and PF-23 with PF-25 (where Notion writes are made). ANALYZE gives every finding a disposition; a low one may be deferred with its reason.
  2. One small repository tool part, so the change prompt's repository route gets its first real test: branch, pull request, merge detection at X3, and the tool's selftest. Take it from the pilot's own findings about the record template and validator (for example PF-13, the missing Harness files section). ANALYZE picks it and names it. This carries ledger error E-025: PE37's pilot request left out the design's tool part, so that route has never run.

  Not in scope: the input reader (the design's PART-01). It waits with the rest of the writing-side build, because Nathan's direction is that nothing on the writing side is implemented until the change management system is proven.

  Canon for PF-25: Nathan is adding a PF10 addendum, PF10-AINEUTRAL-001, that removes the requirement that Notion changes and prompt publishing be done in ChatGPT, and makes no AI product or model a governance requirement. If it is in PF10 on main when ANALYZE starts, the repaired body relies on it. If it is not, record it as a dependency and carry on; the Notion writes in this Modification then need Nathan's plan approval to say they are made from this Claude session, as in the pilot.

  Nathan's standing directions for this run:
  - Stop rather than produce substandard results. If the work will not fit at full quality, or cost reaches twice the estimate, stop at a clean point between steps and report what is done, what is not, and how to resume.
  - Effort: TypeSafe scores this step extra high, one session.

  Report to Nathan in at most five plain sentences, and end with exactly what he must approve, if anything.
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: MODIFICATION-20260929-gtwpe-pilot
shares_package_with: []
---

# MODIFICATION-20260929-gtwpe-first-repair

GTWPE-MGMT-10 gets its first real repair: a new version carrying the pilot's findings, and a GTWPE
record check that gives the change prompt's repository route its first run (design v1.2 §13.2,
*After it*; GTWPE ledger E-025).

## Intake

Not through triage. The request reached this session on 2026-09-29, pasted by Nathan and written by
PE37; it is copied verbatim into `request`. Its two numbered items are the pilot's findings and one
small tool part. The input reader, the design's PART-01, is out of scope by the request's own words.
`spawned_from` names the pilot, whose findings this Modification carries (design §13.2, *After it*).

## §A — Analysis

*Written by MODE = ANALYZE. Frozen once approved.*

In progress (A1). The analysis is written at A2 to A6.
