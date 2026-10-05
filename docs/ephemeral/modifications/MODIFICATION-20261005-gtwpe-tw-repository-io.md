---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261005-gtwpe-tw-repository-io
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
    statement: "The TW prompts stay single-homed in Notion: no TW prompt body, copy or excerpt enters the repository, and this change alters where they read and write, not where they live."
    source: "Request item 1; Nathan, 2026-10-05: \"writing prompts do not belong in repo.\""
    disposition: ""
  - id: ITEM-02
    statement: "TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10 take PF canon from docs/pfcanon/ on main, not from Google Drive."
    source: "Request item 2; HDE Build Notes 2.29 PF10-CANON-001"
    disposition: ""
  - id: ITEM-03
    statement: "Their outputs go to the repository path their invocation names, under docs/ephemeral/, not to ChatGPT Library or a download, and each stays runnable by Nathan directly or as a pass inside one session."
    source: "Request item 3; HDE Build Notes 2.29 PF10-CANON-001"
    disposition: ""
  - id: ITEM-04
    statement: "TW-DRAIN-10, TW-DRAIN-20 and TW-APPLY-10 meet GTWPE-D1 in full: each redlines Markdown file and each final updated PF Markdown file gets its own proof log beside it, named after it, with all eight minimum items, and TW-APPLY-10's proof log states the basis of each applied operation, not only a pointer to it."
    source: "Request item 4; GTWPE-D1 (docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md); MODIFICATION-20261005-gtwpe-writing-side §A A.8"
    disposition: ""
  - id: ITEM-05
    statement: "TW-MGMT-10 leaves the TW-ALPHA selection, and GTWPE-MGMT-10 maintains the TW prompts."
    source: "Request item 5"
    disposition: ""
  - id: ITEM-06
    statement: "A new TW-ALPHA release selects the changed prompts, with its Current operation on the Glow Technical Writing Ecosystem page."
    source: "Request item 6"
    disposition: ""
parts: []
request: |
  PE39 here, facilitator, on 2026-10-05.

  Where things stand, checked by PE39 today:
  - C1 of the writing-side build is COMPLETE on main (#573, merged at `ef75b31`). The GTWPE catalog selects GTWPE-MGMT-10 100526.2, which keeps GTWPE-D1 whole through every later change. Both record checks pass all five GTWPE records. PE39 accepted it against main and the live pages.
  - main is at `20d0dd8`. Since the catalog's checked-through commit `31deec4`, main gained #573 and #574, and every file they change is under `docs/ephemeral/`: C1's record and evidence, the error ledger (E-018 and E-019 closed, E-032, E-033) and the target architecture record's status. No watched path changed.
  - The selected TW release is still TW-ALPHA-20261004.1: seven prompts at 100426.1.

  Next: run C2, the second change in the order Nathan approved in MODIFICATION-20261005-gtwpe-writing-side (§A A.5), through GTWPE-MGMT-10 100526.2 (ANALYZE, PLAN, EXECUTE). Follow the published body live and stop at each of Nathan's approvals.

  What C2 is (§A A.1, A.5 and A.8):
  1. The prompts stay in Notion. Nathan, 2026-10-05: "writing prompts do not belong in repo." No TW prompt body, copy or excerpt enters the repository. C2 changes where the TW prompts read and write, not where they live; §A's label "The TW prompts on the repository" means only that.
  2. Reading. The six operational TW prompts (TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-APPLY-10) take PF canon from `docs/pfcanon/` on `main`, not from Google Drive (HDE Build Notes 2.29 PF10-CANON-001).
  3. Writing. Their outputs go to the repository path their invocation names, under `docs/ephemeral/`, not to ChatGPT Library or a download: under 2.29, Library and Drive are neither destinations nor authorities, and redlines and reports are change-process documents stored in `docs/ephemeral/`. Each stays runnable by Nathan directly, or as a pass inside one session; the Flow Manager itself is C4.
  4. Proof logs. TW-DRAIN-10, TW-DRAIN-20 and TW-APPLY-10 meet GTWPE-D1 in full, as §A A.8 sets out: each redlines Markdown file and each final updated PF Markdown file gets its own proof log beside it, named after it, with all eight minimum items, and TW-APPLY-10's proof log states the basis of each applied operation, not only a pointer to it. GTWPE-MGMT-10 100526.2's own GTWPE-D1 guard applies to this change.
  5. TW-MGMT-10 leaves the TW-ALPHA selection, since GTWPE-MGMT-10 maintains the TW prompts.
  6. A new TW-ALPHA release, with its *Current operation* on the *Glow Technical Writing Ecosystem* page.

  Not in C2: C3's document rules (including the Last Update Gate, which waits for Nathan's PF10 sentence), the Flow Manager (C4), the Change Manager (C5), adoption (C6), and E-033 ("until G5" in GTWPE-MGMT-10), which stays for C6.

  Standing directions:
  - Nathan: "this flow can be simplified, let's not overcomplicate this".
  - Stop rather than produce substandard results.
  - Keep PLAN lean: one dry run and one full review by a single reviewer; a second reviewer or a diff check only if that review finds a required defect.
  - No Modification branch is merged before its record is COMPLETE, except the pull requests the plan itself opens.
  - No TW prompt carries model, effort or strength advice.
  - No TypeSafe scoring in this work.
  - Report to Nathan in at most five plain sentences, in plain language, ending with exactly what he must approve or decide.
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20261005-gtwpe-tw-repository-io

C2 of the writing-side build: the six operational TW prompts take PF canon from the repository and
write their outputs there, the drains and the apply write a proof log beside each artifact they make
(GTWPE-D1), GTWPE-MGMT-10 replaces TW-MGMT-10 as the TW prompts' maintainer, and a new TW-ALPHA
release selects them. The prompts themselves stay in Notion.

## Intake

Not through triage. The request came from PE39 on 2026-10-05 and is copied verbatim in the front
matter. It runs C2, the second change in the order Nathan approved in
MODIFICATION-20261005-gtwpe-writing-side (§A A.5), through GTWPE-MGMT-10 100526.2. Its six numbered
points, under "What C2 is", are ITEM-01 to ITEM-06, in its order. What it puts outside C2 is
recorded in §A, not taken here.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

In progress: A0 and A1 are done; A2 to A7 follow.
