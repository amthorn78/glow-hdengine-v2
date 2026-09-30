---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20260930-gtwpe-tw-model-advice
status: PLANNING
targets: [prompt, notion_control, skill]
gate_tier: 2
closure:
  upstream: [TW-ASSESS-10, TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10]
  downstream: [TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10]
  state_sharers: [TW-DRAIN-10, TW-DRAIN-20]
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 10
interaction_cost_actual:
estimate:
  plan: "about 4 h: §P for 63 passages across seven members (anchors, new texts and absence checks), the selection's three writes and three notes, and the skill part's 23 passages, validator edits, package build and D24 brief; a dry run, and one full review by two reviewers with its repair. Time is the meter the session can read"
  execute: "about 4 h, not counting any wait for Nathan: seven new versions (duplicate, title, edits), each read back whole by this session and by an isolated readback worker; the two skill packages built, validated on an isolated root and reviewed under D24 by two reviewer subagents; after Nathan's install, the digest comparison and the validator on the installed skills; then the selection's three writes and three notes, each read back. Time is the meter"
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-09-30
    required_open: 0
    outcome: "By this session, read-only: the validator and the GTWPE check exit 0 on the record at ANALYZED; A0 reproduces at f83c755; the front matter and every table parse; the seven new versions' titles and the new release label are free under their parents; the Flowmaster facts behind Q1 reproduce from the installed skill; the scope counts were checked by a second reading. No required defect. No full review"
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-09-30
    required_open: 0
    outcome: "Rerun by this session, read-only, on §A as revised at Nathan's direction of 2026-09-30: the validator and the GTWPE check exit 0 at ANALYZED; A0 reproduces at f83c755, and 092926.2 is unchanged; the front matter and every table parse; the validator passes on an isolated root of the installed skills and stops fatally on the installed tree (F-3); three scratch trials show the assertions that pin the old wording and the validator's self-identity; the guard candidates occur nowhere in tw-flowmaster's core; the skill scope table's 37 anchors are on their lines. No required defect. No full review"
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-30
    required_open: 0
    outcome: "By this session, read-only, before any full review: the validator and the GTWPE check exit 0 at PLANNED; main still f83c755, no watched-path change; the seven members and the control pages at the edit times the plan expects, every anchor found once by reading; the skill edits build, pass the suite strict and the guard proof 12/12, and package into archives that extract to the built trees; a three-site trial fails on PROFILE_IDENTITY, so the plan moves all four validator_revision sites (P-F2); edits.json consistent. No required defect"
item_count_at_approval: 4
items:
  - id: ITEM-01
    statement: "No selected TW-ALPHA prompt carries a model-guidance block, or any model, surface or effort recommendation, workload profile or strength rating."
    source: "Request item 1; Nathan's direction of 2026-09-29 (GTWPE-TARGET-ARCHITECTURE-20260929.md); candidate C7 of MODIFICATION-20260929-gtwpe-first-repair"
    disposition: ""
  - id: ITEM-02
    statement: "TW-ASSESS-10 is retired with no replacement, and no other selected TW-ALPHA prompt has a step, gate or handoff that requires it, so the flow works without it."
    source: "Request item 2; the same direction"
    disposition: ""
  - id: ITEM-03
    statement: "The release that carries these changes is selected only after Nathan has installed the updated TW Flowmaster skill and it validates as installed, and every page that names TW's current release is updated, as Nathan ruled on Q1 of MODIFICATION-20260929-gtwpe-first-repair."
    source: "Request, the paragraph after item 2; Nathan's direction of 2026-09-30, its item 2 (§A, Revision of 2026-09-30)"
    disposition: ""
  - id: ITEM-04
    statement: "The installed tw-flowmaster skill carries no TW-ASSESS-10 stage and no fixed model or effort policy, matching the new prompts, and flowmaster-validate asserts the new wording, not the old."
    source: "Nathan's direction of 2026-09-30, approving the analysis with Q1 (b): \"we should update the skill\"; its item 1 (§A, Revision of 2026-09-30)"
    disposition: ""
parts:
  - id: PART-01
    name: "The seven TW-ALPHA members without model advice, TW-ASSESS-10 retired, and the new release selected"
    items: [ITEM-01, ITEM-02, ITEM-03]
    class: B
    after: [PART-02]
  - id: PART-02
    name: "The TW Flowmaster skill packages: tw-flowmaster without TW-ASSESS-10's stages or its fixed model policy, and flowmaster-validate's assertions to match"
    items: [ITEM-04]
    class: B
    after: []
request: |
  PE37 accepted the first repair on 2026-09-30: the record is COMPLETE on main, main's validator passes it, and gtwpe_record_check.py passes 17/17 and the record, run from main. GTWPE-MGMT-10 092926.2 is now the change prompt.

  Next: run the first repair of the TW prompts through GTWPE-MGMT-10 092926.2 (ANALYZE, PLAN, EXECUTE), following the published body live and stopping at each of Nathan's approvals. It is candidate C7, from Nathan's direction of 2026-09-29 ("there should be no hard coded model recommendations or strength assessments at all" / "In the tw prompts I mean"; no canon addendum, per Nathan):
  1. Remove the model-guidance block, and any model, surface or effort recommendation, workload profile or strength rating, from every selected TW-ALPHA prompt that carries one.
  2. Retire TW-ASSESS-10 with no replacement, and remove every step, gate or handoff in the other prompts that requires it, so the flow still works without it.
  Nothing else in those prompts changes. Pages that name TW's current release are updated as Nathan ruled (Q1 of the first repair).

  Standing directions: stop rather than produce substandard results (the stop rule's meter is time); no Modification branch is merged before its record is COMPLETE, except the pull requests the plan itself opens. Report to Nathan in at most five plain sentences, ending with exactly what he must approve.
requested_by: Nathan
analyze_approved_by: "Nathan, 2026-09-30: \"Nathan approves the revised analysis at 119057f (2026-09-30), with two directions: \"the change manager needs a skill check layer like the gcfpe one has\" and \"this flow can be simplified, let's not overcomplicate this\". For this Modification: 1. Keep PLAN lean: one dry run and one full review by a single reviewer; no second reviewer or diff check unless the review finds a required defect. 2. Keep scope to removal: drop the new guard that makes tw-flowmaster refuse the old release (selection already waits for Nathan's install). Keep the validator guard against the removed wording returning. 3. Aim for about half the estimated time; the stop rule (time) still applies. Record as a candidate for GTWPE-MGMT-10's next repair: a skill route with a skill check layer modelled on the GCFPE one, so a skill part runs through the change prompt instead of around it. Continue to PLAN and stop at Nathan's plan approval.\""
analyze_approved_date: 2026-09-30
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: MODIFICATION-20260929-gtwpe-first-repair
shares_package_with: []
---

# MODIFICATION-20260930-gtwpe-tw-model-advice

The TW prompts lose every model recommendation and strength assessment, and TW-ASSESS-10 is retired,
as Nathan directed on 2026-09-29; the first TW prompt repair run through GTWPE-MGMT-10 092926.2.

## Intake

Not through triage. The request came from PE37 on 2026-09-30 and is copied verbatim in the front
matter. Its three numbered outcomes are ITEM-01 to ITEM-03; its sentence "Nothing else in those
prompts changes" bounds all three.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

*Revised on 2026-09-30 at Nathan's direction, before approval: see* Revision of 2026-09-30*, below,
which says what it supersedes.*

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
092926.2*, fetched live at the start of the mode: edited 2026-09-29T23:47:58.009Z, the version the
first repair selected. The request is in the front matter, verbatim. The mode's first timestamped
step was 2026-09-30T00:19:02Z; the canon search and the mode-start fetches came a few minutes before
it.

### Consult

- **Repository.** Nathan's direction is recorded in `GTWPE-TARGET-ARCHITECTURE-20260929.md`, *No model
  recommendations or strength assessments in the TW prompts* (on `main` since
  amthorn78/glow-hdengine-v2#564), read in full: no TW prompt carries a model, surface or effort
  recommendation, a workload profile, a strength rating or a session-strength assessment; the eight
  TW-ALPHA prompts lose their model-guidance blocks; TW-ASSESS-10 is retired with no replacement; and
  it is a repair, not a canon change. The first repair recorded it as candidate C7. Design v1.2 D-17
  carried TW-MGMT-10's block unchanged in the pilot and said removing it is a separate repair; this is
  that repair, and GTWPE-MGMT-10 092926.2 (E41) says only `ANALYZE` scopes it.
- **Canon.** HDE Governance §9.1.6 permits a prompt to carry "human model header" and asks for
  affected members, interacting skills and the flow to be reconciled together. HDE Build Notes (PF10)
  2.31 PF10-HDR-001 retired the header model-advice review and leaves the permission unchanged, and
  2.38 PF10-AINEUTRAL-001 makes no model or effort level a governance requirement. So canon permits the
  headers and requires none: removing them needs no addendum, as Nathan ruled. Canon names no TW
  prompt (a search for `TW-ASSESS`, `TW-ALPHA` and the member IDs finds none).
- **Notion.** The selection page, *Glow Technical Writing Ecosystem*, selects TW-ALPHA-20260929.1:
  eight members, TW-ASSESS-10 among them. Its current section says the *Current operation* of
  TW-ALPHA-20260908.1 still applies, and that operation runs TW-ASSESS-10 before redline creation and
  again before application.

### Drift check (A0)

`git fetch origin main`; the commit examined is `f83c7559fb51921e550aaa9ee2aaee82cf057449` (`f83c755`), #567's merge.

**(a) The lineage sources.** Searches with highlights off on `PE Metaprompt` and `GCFPE-MGMT-10`
found no page the catalog does not record that is newer than its record (the other hits are archived
predecessors, dated 2026-08-26 to 2026-09-13). Each recorded page was fetched for its exact edit
time, and the register's *Current selection* section was read from the harness's save by script:

| Source | Recorded in the catalog | Found, by fetch | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1`, 2026-09-24T15:38 | 11:00:24.691Z; `091426.1` at 15:38:34.295Z; the register selects `091426.1` | None |
| PE Metaprompt | Pinned and selected: `091426.1`, 2026-09-23T17:17:22.217Z | 17:17:22.217Z; the register selects it | None |

The register page was at 2026-09-23T17:43:39.489Z, the edit time the catalog records.

**(b) The watched paths.** `git log e000819..f83c755` over *The watched sources* lists nothing. The
one commit in the range, `f83c755` (#567), changes only the first repair's record.

No trigger finding. X4 re-pins nothing and moves the checked-through commit to the commit it examines.

### The members, read live

Each selected member was fetched whole into this session's context at this mode's start.

| Member | Version, page | Edited | Parent |
|---|---|---|---|
| TW-ASSESS-10 — Assess Session Strength | 090826.2, `3d54590a05eb81c395f4f2d92e9cccc5` | 2026-09-08T07:06:34.996Z | *HDE TW* |
| TW-TRIAGE-10 — Identify PF10 Drain Targets | 090726.2, `3d44590a05eb813283aefa68329609cc` | 2026-09-07T17:01:58.706Z | *HDE TW* |
| TW-DRAIN-10 — Prepare PF Document Redlines | 090826.1, `3d54590a05eb81489659dd250624a220` | 2026-09-08T06:57:45.615Z | *HDE TW* |
| TW-DRAIN-20 — Prepare PF09 Redlines | 090826.1, `3d54590a05eb81d0986be1200bfd4a3b` | 2026-09-08T06:58:40.452Z | *HDE TW* |
| TW-RECORD-10 — Create Epic History Section | 090726.2, `3d44590a05eb817fa047f69764b93396` | 2026-09-07T17:02:12.635Z | *HDE TW* |
| TW-RECORD-20 — Create CRD History Section | 090726.2, `3d44590a05eb819e8482d0a1650c5239` | 2026-09-07T17:02:17.512Z | *HDE TW* |
| TW-APPLY-10 — Apply Validated Redlines | 090826.1, `3d54590a05eb81f99ce6e7908a2a5a60` | 2026-09-08T06:59:20.213Z | *HDE TW* |
| TW-MGMT-10 — Manage the Glow TW Ecosystem | 092926.1, `3ea4590a05eb81d09391f5e87fcaebe0` | 2026-09-29T20:10:20.073Z | the selection page |

### Scope, and how it was measured (`SCOPE-001`)

**Method: broad match minus permitted exceptions, by reading.** The broad terms, searched in every
member's whole body: `assess` (any form), `analyzer`, `Strength`, `model`, `effort`, `reasoning`,
`surface`, `workload`, `profile`, `advice`, `recommend`, `appraisal`, `openai-docs`, `human guidance`,
`human header`, `Ultra`, `Max`, `Astra`, `Sol`, `GPT`. Every count was made by reading the fetch in
context and checked by a second reading of the same fetch; no command counted over a body.

**What is in scope, by this rule.** Removed: (1) each `<operator_model_guidance>` block, whole; (2)
every passage that recommends, requires, selects, appraises or maintains a model, surface, effort or
reasoning level, a workload profile or rating, or a session-strength assessment; (3) every step,
gate, handoff, relationship statement or membership count that requires, routes to, or names
TW-ASSESS-10 as a live member. A passage is a contiguous stretch of in-scope text.

**The permitted exceptions, kept unchanged:** prohibitions that stop a prompt producing or acting
on model advice (TW-TRIAGE-10's two bans on appending it and its "mandatory model-assessment stage"
ban; TW-RECORD-10's and TW-RECORD-20's rule to keep "model advice" out of the insertion text;
TW-MGMT-10's "follows from maintenance or model advice" and "model self-reconfiguration"); "workload"
and "assessment" meaning the document work itself (preflight step 4's "verification workload" in
five members; TW-TRIAGE-10's "complete supported assessment" of PF10); TW-MGMT-10's "capability/model
assumptions" in its impact record and "human headers belong solely in Notion", a location rule;
artifact and source routes, such as ChatGPT Library and Drive, which Nathan's direction does not
reach; and everything else ("Nothing else in those prompts changes").

| Member | Passages in scope, the block included | What they are | Exceptions kept |
|---|---|---|---|
| TW-ASSESS-10 | The whole prompt | Retired with no replacement: it leaves the selection, and its page stays intact, as TW keeps every old page | — |
| TW-TRIAGE-10 | 2 | The block; the sentence that says TW-ASSESS-10 supplies task assessment | 4 |
| TW-DRAIN-10 | 10 | The block; the two relationship sentences that put TW-ASSESS-10 before creation and before application; preflight step 4's clause on an "automatic Ultra requirement"; preflight step 5, the two mandatory assessment checkpoints; the sentence on "the two required assessment checkpoints"; the corrected package's route through "pre-Apply assessment"; the READY next step naming TW-ASSESS-10, and the sentence on "the analyzer"; the handoff's "human surface/model/reasoning recommendation" field, and "assessment" among its gates | 1 |
| TW-DRAIN-20 | 10 | The same ten, word for word | 1 |
| TW-RECORD-10 | 4 | The block; the clause "TW-ASSESS-10 supplies optional task advice"; the Ultra clause; preflight step 5, which chooses "an eligible surface, model and effort" | 2 |
| TW-RECORD-20 | 4 | The same four | 2 |
| TW-APPLY-10 | 12 | The block; intake "after TW-ASSESS-10 appraises" the package; the "Strength Analyzer checkpoint" clause; the Ultra clause; preflight step 5; three sentences of the paragraph after it that require pre-Apply TW-ASSESS-10; "assessment" in the no-change list and the sentence that exempts the report-only path from assessment; the diagnostic handoff's "model advice or limitation" and its "pre-Apply TW-ASSESS-10" for a corrected package | 1 |
| TW-MGMT-10 | 21 | The block; the "eight-member catalog" and TW-ASSESS-10's relationship; its membership as "the assessment-only TW-ASSESS-10", "the additional assessment role" and "one assessment prompt"; the workers' "Strength Analyzer checkpoints"; TW-ASSESS-10's mandate; the analyzer contract paragraph; the Ultra gate clause; the model research and workload sentences; the rule to "keep human guidance non-operative" after the identity lines; the account-picker clause; the alpha invariants' "mandatory assessment checkpoints", "task-bound recommendations" and "advisory research" clause; the analyzer's `openai-docs` sentences; the validation cases for the analyzer and advice; the publication rule that identity lines are "followed by its human guidance"; and "model evidence" in the checkpoint | 4 |

**Total:** 63 passages in the seven members that stay, 7 of them the blocks, and TW-ASSESS-10
retired. Every other member is affected, so each of the seven gets a new version.

**Rule-change search (`D26-E`), for the plan.** After the edits, none of the broad terms may survive
in the new pages outside the exceptions above; `PLAN` turns this into its absence checks.

### Per part: closure, tier, class and targets

One part, PART-01: the seven new member versions, the retirement and the new release, which must
land together. A new page with no selection has not landed, and a selection of pages that still
route to TW-ASSESS-10 would break the flow.

- **Targets:** `prompt` (the seven new versions) and `notion_control` (the selection page's three
  writes, and the current-release note on the three other pages that name TW's current release).
- **Closure,** from the relationships in the *Current operation* the selected release records:
  upstream, the producers of the handoffs the changed members consume (TW-ASSESS-10, TW-DRAIN-10,
  TW-DRAIN-20, TW-APPLY-10); downstream, their consumers (TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10);
  state sharers, TW-DRAIN-10 and TW-DRAIN-20, which share `READY`, `NO_CHANGE` and `BLOCKED`.
- **Tier 2.** The part changes recorded relationships and a handoff: a READY package now goes to
  TW-APPLY-10 directly, TW-APPLY-10 no longer requires an assessment, and the handoffs lose their
  recommendation field. Both sides change in this Modification. TW has no executable selftest and no
  live trial has run, so the gate is a static check of both sides of every changed relationship and
  the whole-page readbacks.
- **Class B, rule application:** Nathan's direction of 2026-09-29 is the ruling, and this carries it
  into the prompts (`ecosystem-change-management.md` §2 and §6: applying a ruling he has made,
  including its consequences, is the coordinator's).

### Member dispositions (HDE Governance §9.1.6)

| Member | Disposition | Reason |
|---|---|---|
| TW-ASSESS-10 | Affected: retired | Nathan's direction |
| TW-TRIAGE-10 | Affected | Carries the block, and names TW-ASSESS-10 |
| TW-DRAIN-10, TW-DRAIN-20 | Affected | The block; both assessment checkpoints; READY routes through TW-ASSESS-10; the handoff carries a recommendation |
| TW-RECORD-10, TW-RECORD-20 | Affected | The block; optional assessment; preflight step 5 chooses a surface, model and effort |
| TW-APPLY-10 | Affected | The block; intake requires pre-Apply assessment; the diagnostic carries model advice |
| TW-MGMT-10 | Affected | The block; it maintains TW-ASSESS-10 and model advice, and its publication rule would put the headers back |
| GTWPE-MGMT-10 092926.2 (the GTWPE) | Unaffected | It names no TW-ASSESS-10 and no model advice. Its selection route assumes eight members (finding F-1, below) |

**Interacting controls outside the members:** the TW Flowmaster skill (affected: Q1, below); the PE
Metaprompt (unaffected: it already bans workload ratings); the Drive guides the removed passages cite,
*General Prompt Flow and Creation Guidelines* and *Prompt Selection and Session Delegation Protocol*
(unaffected, and no longer cited by a TW prompt); *Model Routing and In-Flight Learning* under the
*Glow Operations Hub* (cited only by TW-ASSESS-10; unaffected). The GCFPE Flow Index and register list
no TW-ALPHA member, and no page by the name *Living Prompt Flow Map* exists (search, 2026-09-30).

### Pages that name TW's current release or link a member (A3)

Searches, highlights off, on `TW-ALPHA-20260929.1`, `TW-ASSESS-10 Assess Session Strength` and
`TW-DRAIN-10 TW-APPLY-10 TW-TRIAGE-10`, then a fetch of each page found that could name the current
release (a page last edited before 2026-09-29 cannot):

| Page | Edited | Names TW's current release | Written by the route |
|---|---|---|---|
| *Glow Technical Writing Ecosystem*, the selection page, `3d44590a05eb8171ab6ff4dab33b00ef` | 2026-09-29T20:14:15.580Z | Yes, its selected-release section | Yes: the three selection writes |
| *Alpha 1 — Implementation and Validation*, `3d44590a05eb81fe991ff0114cb43029` | 2026-09-29T20:15:21.232Z | Yes, `## Selected release — TW-ALPHA-20260929.1`, with its member rows | Yes: the current-release note (read by script from the harness's save) |
| *HDE TW*, `3c74590a05eb8176baf8cb59f1631f3c` | 2026-09-29T20:17:20.875Z | Yes, `## Current TW release — TW-ALPHA-20260929.1` | Yes: the current-release note |
| *Glow Operations Hub*, `3ce4590a05eb814f8892f88ff8539308` | 2026-09-29T20:18:21.747Z | Yes, `## Current Glow TW release — TW-ALPHA-20260929.1`, which says "the exact eight-member catalog" | Yes: the current-release note (read by script from the save) |
| *GCFPE Alpha Feedback — Deferred Items*, *TypeSafe effort scorer* use row, GTWPE pages, the GCFPE Flow Index | 2026-09-27 to 2026-09-30 | No (no TW-ALPHA member or release named; the TypeSafe row is PE37's scoring of this request) | No |
| Historical pages that link TW-ASSESS-10 or a member: *TW Strength Analyzer 090726.1*, earlier TW-ASSESS-10 and TW-MGMT-10 versions, *Glow TW Alpha Implementation Handoff 090726.1*, and the historical sections of the four pages above | 2026-09-07 to 2026-09-29 | No | No: historical records keep their links, as the pilot did |

This is the same set the pilot wrote (the record of TW's latest selection, MODIFICATION-20260929-gtwpe-pilot,
W5 to W8), and each member's own text names the selection page and *Alpha 1* as holding the selection.
All three current-release notes say that everything else in the 2026-09-08 follow-up still applies,
and that follow-up starts with TW-ASSESS-10; the new notes must say that part no longer applies.

### Contradictions and risks

1. **The TW Flowmaster skill requires TW-ASSESS-10** (Q1). Installed `tw-flowmaster`, revision
   1.2.0, has a selected-catalog TW profile that applies "only when" the selected drain and apply
   prompts "carry the mandatory pre-creation/pre-Apply assessment" contracts, and that adds
   `PRE_CREATION_ASSESSMENT` and `PRE_APPLY_ASSESSMENT` stages that run TW-ASSESS-10. Once the new
   release is selected, the profile no longer applies, and its legacy clauses, which carry fixed model
   and effort policies, would govern a Flowmaster run: a silent wrong path. GTWPE-MGMT-10 may not
   change this skill, and HDE Governance §9.1.6 says an edited subgroup "is not ready while an
   affected counterpart remains incompatible".
2. **The route assumes eight members** (finding F-1). *How each kind of target changes* has the new
   release section list "the eight members with only the changed rows new" and state that the prior
   release's *Current operation* "still apply". With a retirement there are seven, and the part of
   that operation that runs TW-ASSESS-10 no longer applies. The plan adapts the text of the three
   selection writes and the three notes to say so; the route's intent (one new section, prior
   heading historical, nothing else changed) holds.
3. **TW-ASSESS-10's page carries no retirement notice.** GTWPE-MGMT-10 never edits an existing TW-ALPHA
   page, and *HDE TW*'s child list still shows it. Someone who opens it directly can still run it.
   The selection page says it is retired.
4. **No executable check exists for TW.** The tier 2 gate is static, and no live TW trial has run
   since 2026-09-08. The selection page already records that runtime behaviour is unproven.
5. **The readbacks are heavy.** Seven whole pages, each read by this session and by an isolated
   readback worker, and four control pages. Compaction during `EXECUTE` is likely; 092926.2's rule
   (fetch live again, never recover from a transcript) covers it.
6. **Broad text edits at scale.** 56 passages besides the blocks; a wrong anchor fails loudly, and a
   wrong new text is caught only by the readback, so `PLAN`'s checks carry each edit's surviving-text
   absence as well as its new text.

### Defect classes matched (`ecosystem-change-management.md` §4)

- `SCOPE-001`: the scope above is measured by broad match minus exceptions, by reading.
- `GUARD-001`: a ruling applied without a guard; the plan's absence checks are the guard, and
  TW-MGMT-10's publication rule, which would restore the headers, is removed with the rest.
- `FUNC-001`: a retired behaviour reinstated by function; the Flowmaster profile (Q1) is that risk.
- `DERIV-001`: the four pages that name TW's current release restate the selection by hand.

### Findings against GTWPE-MGMT-10 092926.2

- **F-1:** its selection route (target *The GTWPE catalog, or TW-ALPHA's selection*) is written for a
  release with eight members and no retirement. See risk 2.

### Candidates for separate Modifications (recorded, not taken)

- **C1**: update the `tw-flowmaster` skill's selected-catalog TW profile, removing its assessment
  stages and its fixed model and effort policies, through that skill's own maintenance route.
- **C2**: F-1, the route's text for a release that retires a member.
- **C3**: carried from the first repair and still open: C8 (the find rule) and C9 (the merge rule in
  the body).

### Open questions for the Product Owner

**Q1. The TW Flowmaster skill.** It runs TW-ASSESS-10 twice per document when it drives a TW run,
and GTWPE-MGMT-10 cannot change it. Canon (§9.1.6) says the TW change is not ready while it stays
incompatible.

- **(a) Select the new release in this Modification,** and say on the selection page and in the
  three notes that the TW Flowmaster is not supported for this release until its profile is updated
  (C1). The manual flow works at once; a Flowmaster-driven run is unsupported until C1 lands. This
  waives §9.1.6's readiness rule for the skill, which is Nathan's to do.
- **(b) Publish the seven new versions but do not select them** until C1 is installed. This run ends
  `PROMOTION_CHECKPOINT_REQUIRED`, and a later Modification selects. It keeps canon's rule, and the
  model advice stays live until then.

**Recommendation: (a).** TW-MGMT-10 itself calls the Flowmaster optional and "not a worker
dependency"; the manual flow is how TW runs; and (b) keeps the advice Nathan ruled out in use for as
long as C1 takes.

### Readiness and interaction cost

`NEEDS_RULING`, for Q1. It is advice, not a refusal. No item waits on another item's execution, and
every item's scope is measured.

    interaction_cost = 1 open ruling + 2 + 3 review rounds + 0 skill reviews + 0 installs + 1 merge = 7

- The review rounds are this mode's dry run, and `PLAN`'s dry run and one full review. A check of the
  repair's diff makes 8.
- The merge is the record's pull request, amthorn78/glow-hdengine-v2#568, opened at A1 as 092926.2
  requires and not to be merged before the record is `COMPLETE`. No repository file other than the
  record and its evidence changes, so X2 waits for no merge.
- Splitting TW-MGMT-10 or the retirement into a separate run saves nothing: the members change as one
  selection.

The estimate is in the front matter; time is the meter. Twice it is where the session stops.

**This mode's own cost.** Time: from about 00:10Z to A7 at 2026-09-30T00:30:47Z, about 25 minutes. Tokens: not
measured by this session.

### Revision of 2026-09-30, at Nathan's direction

*Added by this mode on 2026-09-30, before `ANALYZE` approval. It supersedes the subsections it
names; the text above it stays as written, since a dated record is never corrected in place.*

**Nathan's direction, as PE37 relayed it on 2026-09-30:**

> Nathan approves the TW prompts repair's analysis (2026-09-30). Q1: option (b), plus the skill
> update — Nathan: "we should update the skill". Revise §A before PLAN (scope change; no new ruling
> needed beyond this): 1. Add a skill part: an updated tw-flowmaster package with TW-ASSESS-10's
> stages and its fixed model policy removed, matching the new prompts, and any flowmaster-validate
> assertions that pin the old wording updated to match. Nathan's direction is the explicit
> skill-update scope the body requires; Nathan alone installs. Prepare the package, run the
> validator against it, and hand Nathan the package with a change note. 2. Publish the seven new
> prompt versions, but select the new release only after Nathan has installed the updated skill and
> it validates as installed (X3-style wait). If GTWPE-MGMT-10 092926.2 has no route for a skill
> part, record that as a finding against the body and carry the part under Nathan's direction
> anyway. Set the record back to ANALYZED with a dry run, and stop for Nathan's approval before
> PLAN.

The direction widens the scope, so `analyze_approved_by` stays empty until Nathan approves this
revision, and the scope freezes then (*Scope freezes at analysis approval*).

**What it settles.** Q1 is answered: option (b), with the skill updated in this Modification. Risk 1
and candidate C1 become PART-02. This subsection supersedes *Per part*, Q1's recommendation and
*Readiness and interaction cost*; everything else in §A stands.

**Items and parts, as revised.**

- **ITEM-04** (new, from the direction's item 1): the installed `tw-flowmaster` carries no
  TW-ASSESS-10 stage and no fixed model or effort policy, matching the new prompts, and
  `flowmaster-validate` asserts the new wording, not the old. It comes from Nathan's direction, not
  from the request.
- **ITEM-03** (revised, from the direction's item 2): the new release is selected only after Nathan
  has installed the updated skill and it validates as installed.
- **PART-02** (new): the two skill packages, `tw-flowmaster` and `flowmaster-validate`, holding
  ITEM-04. Target `skill`. Class B: Nathan's direction is the ruling, and HDE Governance §9.1.6
  already requires an interacting skill to be reconciled with the members it serves. Tier 2, as the
  Modification's: the skill consumes the handoffs the members change (a READY package now goes to
  TW-APPLY-10 directly), and both sides change here. Closure adds nothing, since the skill is not a
  TW-ALPHA member.
- **PART-01** is ordered after PART-02: its selection writes and the three current-release notes
  wait until PART-02 has landed, which is when X3 has verified Nathan's install. Its seven new
  versions may be created before then and stay unselected, as the direction's item 2 allows. If
  PART-02 does not land, no selection is made, and the unselected pages take the route's rollback
  before X4: Nathan archives them.

**The skill part's scope, measured (`SCOPE-001`).** Method: the prompts' broad terms, plus
`rendered`, `page count` and `checkpoint`, searched by `grep` in the installed
`tw-flowmaster/SKILL.md` (a skill file, not a prompt body, so a command may count over it), and each
hit read in context. The installed file is revision 1.2.0: 499 lines, 58,355 bytes, sha256
`e0fad7be3bff06e229d54dd89e851b7b2d466bf7e986f857a67d9de0607e62a6`. Its embedded Primary core is
lines 12 to 228, and its TW specialization lines 229 to 499.

What is removed, from Nathan's words ("TW-ASSESS-10's stages and its fixed model policy removed,
matching the new prompts"): (1) every stage, input, check, route or report item that runs, requires
or names TW-ASSESS-10 or its assessments; (2) every fixed model, reasoning or effort policy, and
every input or rule that serves only such a policy, which is the rendered page count; (3) where the
profile names either, its text is rewritten to the new prompts' contract.

Kept unchanged:

- the embedded Primary core, lines 12 to 228, its three model or assessment mentions included: the
  validator requires it byte-identical to `flowmaster-primary`'s, and the skill's maintenance rule
  forbids editing it on its own;
- every clause that states the GCFPE's own contract: the GCFPE binding (lines 313, 315 and 317), the
  GCFPE sentences of lines 351, 352, 393 and 451, and line 355's `/model`, which GCFPE stages still
  use. Nathan's direction about the TW prompts does not reach them (candidate C4);
- records of the actual configuration: the composer checksum's "model/reasoning" (line 441), the
  report row's "application model/reasoning" (line 481), and line 339's rule to record the actual
  configuration only when directly verified;
- the prohibitions in the stall bullet, line 345: "Max did not prove the task should complete", "a
  hang does not prove model mismatch", and its ban on escalating effort because time elapsed;
- everything else.

| Line | Passage | Why it is in scope |
|---|---|---|
| 8 | `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0` | TW behaviour changes, so the skill's maintenance rule moves the revision, to 1.3.0 |
| 258 | The fixed policy `APPLICATION_REASONING_POLICY = ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN`, the whole line, with its notes on TW's assessment policy and the GCFPE's own, which qualify only this line | (2), and (1) |
| 266 | The accepted input `PF_RENDERED_PAGE_COUNTS` | (2): it feeds only the page-count rule |
| 268 | The accepted input `STRENGTH_ANALYZER_PROMPT_ID`, which resolves TW-ASSESS-10 | (1) |
| 331 | The profile's condition, that the prompts "carry the mandatory pre-creation/pre-Apply assessment and exact no-redlines contracts" | (3): rewritten to the new contract; see risk S-1 |
| 333 | "fixed-model/page-count, direct creation-to-application", in the list of legacy clauses the profile supersedes | (3): the first goes below, and without the pre-Apply stage the profile no longer departs from direct creation-to-application |
| 337, 338, 340 | Three bullets: TW-ASSESS-10's two assessment turns; the analyzer's documentation research; the `PRE_CREATION_ASSESSMENT` and `PRE_APPLY_ASSESSMENT` stages | (1), whole |
| 339 | The bullet on task-bound recommendations | (1), all but its rule on the actual configuration |
| 341 | "analyzer/"; "model/reasoning recommendation or qualified limit"; the sentence that sends READY output to pre-Apply TW-ASSESS-10, and the assessment to TW-APPLY-10 | (1), three passages: READY now points to TW-APPLY-10, as in the new prompts |
| 342 | "pre-Apply assessment/" | (1) |
| 343 | "and assessed", for a corrected package | (1) |
| 345 | "recommendation versus", before "observed configuration" | (1) |
| 347 | "assessments," among the report's counts | (1) |
| 351 | The sentence fixing GPT-5.6 Sol with Max reasoning for legacy runs; "for selected-catalog TW, apply its two-checkpoint policy" | (2) and (1), two passages |
| 352 | The legacy Ultra and Max sentences; the clause that TW uses its pre-Apply assessment | (2) and (1), two passages |
| 353 | "Never infer rendered pages from …" | (2): it serves only the page-count rule |
| 393 | ", or Sol Max for a non-GCFPE target" | (2) |
| 451 | Step 3's sentence selecting Sol Ultra or Sol Max for a non-GCFPE application | (2) |

**Total:** 23 passages on 19 lines, and the revision line. Nothing in the core changes.

**`flowmaster-validate`: the assertions that pin the old wording.** Measured by `grep` over the
whole installed `flowmaster-validate` tree for `tw-flowmaster`, `pre-Apply`, `pre-creation`,
`selected-catalog`, `1.2.0` and the removed identifiers, each hit read:

- `scripts/validate_flowmaster.py`, `CONTRACT_REQUIRED["tw-flowmaster"]`: four of its strings pin the
  old wording, `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`, `PRE_CREATION_ASSESSMENT`,
  `PRE_APPLY_ASSESSMENT` and `ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN`. The first moves to the new
  revision; the other three are removed.
- The same file's `CONTRACT_FORBIDDEN["tw-flowmaster"]` gains the guard (`GUARD-001`): the removed
  identifiers, so that none returns unnoticed. It is matched case-insensitively against the whole
  file, core included. The candidates, `TW-ASSESS-10`, `PRE_CREATION_ASSESSMENT`,
  `PRE_APPLY_ASSESSMENT`, `STRENGTH_ANALYZER_PROMPT_ID`, `APPLICATION_REASONING_POLICY` and
  `PF_RENDERED_PAGE_COUNTS`, occur nowhere in lines 1 to 228 (*Dry run, rerun*, R5). `PLAN` fixes
  the set, with a guard proof that each fires on the old file.
- `SKILL.md` line 184, the paragraph on the TW specialization, names revision 1.2.0 and
  "pre-creation and pre-Apply assessments". It is rewritten to the new revision and contract.
- The validator's own identity. Validation behaviour changes, so, by the skill's own convention,
  `FLOWMASTER_VALIDATE_REVISION` in `SKILL.md` and `validator_revision` at its three sites
  (`validate_flowmaster.py`, `validate_gcfpe_20260914.py` and `run_gcfpe_20260914_fixtures.py`) move
  from 3.3.1 to a new revision, and `SKILL_TREE_SHA256`, the skill's digest of itself, is
  recomputed: the validator refuses a tree whose digest differs from its declaration (R6).
- Nothing else. No fixture or reference names the TW contract, and no other skill's list, fixture
  or oracle changes, so the GCFPE's validation is unchanged.

**Finding against GTWPE-MGMT-10 092926.2.**

- **F-2: it has no route for this skill part.** *What this prompt may change* lists one skill, "The
  GTWPE wording of `glow-write-boundary`'s exception", and its `targets` vocabulary defines `skill`
  as that exception. Its *Native purpose* says it does not change "another ecosystem's controls",
  and `flowmaster-validate` validates the whole Flowmaster suite, GCFPE's `change-flow` among it. No
  overridable gate names a route (`OVERRIDABLE` in `modification_validate.py`), so no `override`
  block is recorded: Nathan's direction carries the part, as he said. It takes the route the body
  gives its one skill, by analogy: a `D24` package, two reviewer subagents on the first template of
  `reviewer-prompt-template.md`, Nathan's install, the post-install digest comparison, and, to roll
  back, Nathan's reinstall of the prior digest. X2 and X3 already provide for an install. The
  *Boundaries* let this prompt write only the record and its evidence here, so the packages' bytes
  and change note are evidence files of this Modification; `PLAN` sets their paths and how they
  reach Nathan.

**Finding outside the GTWPE.**

- **F-3: the installed skills cannot be validated as they are.** `flowmaster-validate` on the
  installed tree stops fatally (exit 2) on `canva-drive-facebook-workflow/SKILL.md`, whose quoted
  `name:` its front-matter check rejects, before it checks any Flowmaster skill (R4). Every
  validation in this Modification, the post-install one included, runs on an isolated root that
  copies every installed skill except that one, as the validator's documentation allows ("Use
  SKILLS_ROOT or --skills-root only for an exact fresh checkout or isolated test root"). The fix
  belongs to that skill's owner, outside this scope.

**Risks added.**

- **S-1: the interval between Nathan's install and the selection.** In that interval the installed
  skill has no assessment stage, while the selected release, TW-ALPHA-20260929.1, still requires
  TW-ASSESS-10. If the profile's new condition matched the old release, a Flowmaster run in that
  interval would skip assessments the selected prompts require, a silent wrong path; if it fell
  through to the legacy clauses, the run would resolve the wrong sources. So the rewritten condition
  must match only a release with no TW-ASSESS-10 dependency, and state that a selected release which
  still requires it is the profile's existing "scope/compatibility blocker", a loud stop. `PLAN`
  writes that text and checks it against both releases' contracts, and keeps the interval to X3's
  checks and the selection in one session.
- **S-2: the post-install validation needs the isolated root** (F-3). The root is rebuilt from the
  installed tree after Nathan's install, and the digest comparison runs on the installed files
  themselves.
- **S-3: this session may not see the install.** The synced skill directories date from
  2026-09-29T21:24Z; the directory's manifest was rewritten at 2026-09-30T01:07Z, but nothing shows
  that installed files refresh within a session. If they do not change after Nathan's install, X3
  resumes in a session Nathan starts after it, at the post-install checkpoint (`D26-C`).
- **S-4: `flowmaster-validate` is shared with the GCFPE.** Its new revision and digest are what every
  GCFPE session will see installed, though its GCFPE checks do not change. A search of
  `docs/prompt_ecosystem_management/` and `docs/graph/` on `main` for its declared digest
  `ed52208f…` and for its revision 3.3.1 as `validator_revision` or `FLOWMASTER_VALIDATE_REVISION`
  found no pin (`git grep`, no match).
- **S-5: a `D24` repair.** A `SKILL_REPAIR_REQUIRED` verdict means a repair and fresh reviewers on
  the new bytes: one more skill review cycle each time, under the stop rule by time.

**Candidates for separate Modifications, as revised.** C1 is taken, as PART-02. C2 and C3 stand. One
is added:

- **C4:** `tw-flowmaster`'s GCFPE binding (lines 315 and 317) still carries predecessor assessment
  and surface, model and reasoning advice for GCFPE stages: phrases that `session-relay-flowmaster`'s
  guard in `flowmaster-validate` forbids since MODIFICATION-20260923-closeout-residuals (ITEM-02,
  `D23-A` and `D23-B`). It is the GCFPE's contract, for GCFPE-MGMT-10, and outside Nathan's direction
  about the TW prompts.

**Readiness and interaction cost, as revised.** `READY`. Q1 is answered; PART-01's selection waits
on PART-02's install, which is an ordering, not sequential discovery; and every item's scope is
measured.

    interaction_cost = 1 ruling + 2 + 4 review rounds + 1 skill review cycle + 1 install + 1 merge = 10

- The ruling is Q1, answered in Nathan's approval of 2026-09-30; its round trip has happened.
- The review rounds are this mode's two dry runs, and `PLAN`'s dry run and one full review. A check
  of a repair's diff makes 11.
- The skill review cycle is `D24`'s two reviewers on the same bytes; each repair adds one (S-5).
- The install is one round trip for both packages, and X2 waits for it.
- The merge is still the record's pull request, #568. The packages are evidence files, so X2 waits
  for no merge.
- Moving PART-02 to a separate run saves nothing: PART-01 cannot land before it, and a second run
  adds its own approvals and merge.

The estimate in the front matter is revised: `PLAN` about 4 h, `EXECUTE` about 4 h without the
waits. Time is the meter, and twice it is where the session stops.

**This revision's own cost.** Time: from before 2026-09-30T01:09:02Z, when it wrote its first file,
to A7 at 2026-09-30T01:23:14Z. Tokens: not measured by this session.

### Dry run, rerun (A6)

On 2026-09-30, by this session, read-only, on §A as revised, before A7. No full review follows: the
skill part's scope is measured, no question is open, and `PLAN` reviews the exact texts.

| # | Gate | Result |
|---|---|---|
| R1 | `modification_validate.py` and `gtwpe_record_check.py` (on `main` at `f83c755`) on this record at `ANALYZED`, with this round in `reviews` | Both exit 0, 1/1 |
| R2 | A0 again: `git fetch --prune origin`; the watched-path log from `e000819`; GTWPE-MGMT-10 092926.2 fetched live again | `main` still `f83c755`; the log lists nothing; 092926.2 edited 2026-09-29T23:47:58.009Z, as at the mode's start |
| R3 | The front matter and tables, by script | They parse, and every table row has its table's column count |
| R4 | `validate_flowmaster.py` on the installed tree, then on a fresh isolated root: the 28 installed skills other than `canva-drive-facebook-workflow`, copied, with `tw-flowmaster` and `flowmaster-validate` equal to the installed (`diff -rq`, no output) | Installed tree: exit 2, `fatal_error` on the canva skill's front matter (F-3). Isolated root: `FLOWMASTER_SUITE_PASS`, exit 0, and exit 0 with `--strict-warnings`; `self_identity` OK; `validator_revision` 3.3.1; no skill error or warning |
| R5 | The guard candidates, counted case-insensitively by `grep` in `tw-flowmaster/SKILL.md` lines 1 to 228 (front matter, header and core) | 0 for each of `TW-ASSESS-10`, `PRE_CREATION_ASSESSMENT`, `PRE_APPLY_ASSESSMENT`, `STRENGTH_ANALYZER_PROMPT_ID`, `APPLICATION_REASONING_POLICY`, `PF_RENDERED_PAGE_COUNTS`, `ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN`, `two-checkpoint`, `Sol Max`, `Sol Ultra` and `GPT-5.6` |
| R6 | Three scratch trials, each on its own copy of the isolated root | `PRE_APPLY_ASSESSMENT` renamed in `tw-flowmaster`: exit 1, "missing specialization contract: PRE_APPLY_ASSESSMENT". The revision set to 1.3.0: exit 1, "missing specialization contract: TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0". `flowmaster-validate`'s `SKILL.md` line 184 changed: exit 1, `SKILL_SELF_IDENTITY:DECLARED_ed52208f4847_MEASURED_beb910eb3c98`. Apart from the error each names, which the third also reports under `change-flow`, each report's fixture results equal R4's |
| R7 | The skill scope table, by script: each row's anchor text on its line of the installed file | 37 of 38 on their lines; the revision line is line 8, not line 7, and the table was corrected before this row |
| R8 | 092926.2's *What this prompt may change*, its `targets` rule and *Native purpose*, read in the live fetch | As F-2 quotes them |

Not exercised: any Notion write, any package build, and any reviewer.

### Dry run (A6)

On 2026-09-30, by this session, read-only, before A7. No full review follows: the scope is measured,
the one open question is Nathan's, and `PLAN` reviews the exact texts.

| # | Gate | Result |
|---|---|---|
| D1 | `modification_validate.py` and `gtwpe_record_check.py` (on `main` at `f83c755`) on this record at `ANALYZED`, with this round in `reviews` | Both exit 0, 1/1 |
| D2 | A0 again: `git fetch origin main`, and the watched-path log from `e000819` | `main` still `f83c755`; the log lists nothing |
| D3 | The front matter and tables, by script | They parse, and every table row has its table's column count |
| D4 | The route's precondition for `EXECUTE` on 2026-09-30: the new versions' titles under their parents, from this mode's fetches of *HDE TW* and the selection page | No child page of either carries a `093026` version; the selection page names no `TW-ALPHA-20260930` release |
| D5 | Q1's facts, from the installed skill file | `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`; the profile's "only when" condition and its `PRE_CREATION_ASSESSMENT` and `PRE_APPLY_ASSESSMENT` stages are present |
| D6 | The scope table | Each member's passages and exceptions checked by a second reading of its fetch, in context |

Not exercised: any Notion write, and every readback, since `ANALYZE` writes nothing to Notion.

### Harness files (`D22` condition 5)

- **This session's transcript** holds, from this mode, the bodies of GTWPE-MGMT-10 092926.2, the eight
  TW-ALPHA members, and GCFPE-MGMT-10's proposed body and `091426.1` (A0's edit times, both returned
  inline), each fetched once into context; and control pages: the selection page, *HDE TW*, the
  GCFPE Flow Index and the *TypeSafe effort scorer* row. No script read the transcript, and every count
  over a body was made by reading, in context. It is left to teardown.
- **Five tool-results saves,** each read by script for only what its check needed, never hashed or
  compared, then deleted (exit 0): the PE Metaprompt 091426.1, a prompt body (its edit time and
  title); the GCFPE register (its edit time and *Current selection* rows); *Alpha 1* (its edit time,
  headings, first section and term counts); the *Glow Operations Hub* (its edit time, TW headings and
  current TW section); and *GCFPE Alpha Feedback — Deferred Items* (its edit time and TW term counts).
- **The skill file** `tw-flowmaster/SKILL.md`, read by `grep` and `sed` for its revision and its TW
  profile. It holds no prompt body.
- **Scratch:** `tw-notes.md` (short clauses and page identities, no body) and `sectionA.md` (this
  section's draft). No transient file holds a prompt body.
- **For the revision of 2026-09-30.** GTWPE-MGMT-10 092926.2 was fetched live again into this
  session's context, after a context compaction and before any step relied on it; it is left to
  teardown with the transcript, and nothing counted over it by script. The installed skill files
  `tw-flowmaster/SKILL.md` and `flowmaster-validate/`'s `SKILL.md` and scripts were read by `grep`,
  `sed` and a script; none holds a prompt body. Scratch: `fvroot/` and `fvroot2/`, the isolated
  roots; `tr-t1/` to `tr-t3/`, the trials' copies; `fv-*.json` and `dr-*.json`, the validator's
  reports; and `revise_a.py`, this revision's edit script. No transient file holds a prompt body.

### Canon and rulings relied on

- HDE Governance (PF04) §9.1.6, read in full on `main` at `f83c755`.
- HDE Build Notes (PF10) 2.31 PF10-HDR-001 (its rule and scope) and 2.38 PF10-AINEUTRAL-001 (its
  rule), read on `main` at `f83c755`.
- Nathan's direction of 2026-09-29, in `GTWPE-TARGET-ARCHITECTURE-20260929.md`, read in full; his
  Q1 ruling of the first repair (every page that names TW's current release is updated); his merge
  rule of 2026-09-29, recorded in MODIFICATION-20260929-gtwpe-first-repair §P.
- `ecosystem-change-management.md` §2, §4 and §6; `gcfpe.decision-record.md` `D21`, `D22` and `D26`;
  design v1.2 D-17; `modification-template.md` 2.1.
- The first repair's record, for C7, the route and its conventions; the pilot's record, for the four
  pages W5 to W8 wrote.
- For the revision: Nathan's direction of 2026-09-30, quoted in it; GTWPE-MGMT-10 092926.2 as fetched
  live again (*What this prompt may change*, the `targets` rule, *Boundaries*, *Reviews are bounded*,
  X2, X3 and *How each kind of target changes*); `gcfpe.decision-record.md` `D24`, read in full, and
  `D23-B`; `modification-template.md`'s `override` rules and `after`; HDE Governance §9.1.6 on
  interacting skills; and the installed `tw-flowmaster` (its maintenance rule) and
  `flowmaster-validate` (its entry points and self-identity), read as the harness files say.

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
092926.2*, fetched live in this session after a context compaction (edited
2026-09-29T23:47:58.009Z). The input is §A as Nathan approved it at `119057f` on 2026-09-30
(`analyze_approved_by`). The mode started at 2026-09-30T01:59Z, when the approval was recorded.

### Nathan's directions at approval, and how this plan applies them

- **"this flow can be simplified, let's not overcomplicate this".** The plan is lean: one dry run and
  one full review by a single reviewer, with no second reviewer or diff check unless that review
  finds a required defect (his item 1). `EXECUTE` drops the isolated readback worker the first
  repair used, since 092926.2's route asks only for this session's whole-page readback. `D24` still
  governs the skill packages: it is a standing ruling, which this plan does not relitigate, so two
  skill reviewers remain.
- **Scope is removal (his item 2).** The guard §A's risk S-1 asked for, making `tw-flowmaster` refuse
  the old release, is dropped: the profile's condition is only rewritten to the new contract, and
  the selection waits for Nathan's install. The validator's guard against the removed wording
  returning stays. S-1 is an accepted risk, K-1.
- **Half the estimated time (his item 3).** The aim is about 2 h for `PLAN` and about 2 h for
  `EXECUTE` without the waits. The stop rule is unchanged: twice the recorded estimate, by the clock.
- **"the change manager needs a skill check layer like the gcfpe one has".** Recorded as candidate
  C5 (*Explicitly not in scope*), for GTWPE-MGMT-10's next repair.

### Finding against §A (recorded, not repaired)

- **P-F1.** §A's *Interacting controls* says the two `Glow / Ops` guides "are no longer cited by a
  TW prompt". TW-MGMT-10's intake still cites *General Prompt Flow and Creation Guidelines* and
  *Prompt Selection and Session Delegation Protocol* as maintenance reading, a passage outside §A's
  21 for that member and kept by its rule ("everything else"). The edits are unaffected. §A stays as
  approved; Nathan sees this with the plan.
- **P-F2.** §A counts three `validator_revision` sites. There are four: the GCFPE validation profile
  in `flowmaster-validate/references/` carries the fourth, and `change-flow`'s GCFPE check compares
  it. The dry run's trial (R6) moved only the three and failed with `PROFILE_IDENTITY`; with the
  fourth moved, the suite passes. The plan moves all four, which is §A's own element ("move from
  3.3.1 to a new revision") correctly counted, not new scope; Nathan sees it with the plan.

### Values

| Value | Fixed |
|---|---|
| «D» | At X1.1: the UTC date the seven pages are created |
| «V» | At X1.1: `MMDDYY.1` for «D», the version of all seven new pages (PE's scheme; the pilot's precedent) |
| «ID:…» | At X1.5: each new page's ID, returned by its duplication |
| «S», «R» | At X4: the selection date, and `TW-ALPHA-<yyyymmdd of «S»>.1` |
| «PA» | Nathan's plan approval date, from `plan_approved_date` |
| «M» | At X4.1: `origin/main`'s commit then, full and short |
| Built `tw-flowmaster` | tree digest `0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c` (2 files, 55,131 bytes); `SKILL.md` sha256 `21c632e1b92a6096bb521d990fde1d7aee383af029e7f0e99fce68eac09b1575`, 54,711 bytes |
| Built `flowmaster-validate` | tree digest and `SKILL_TREE_SHA256` `284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733` (31 files, 1,915,296 bytes) |
| Installed, before | `tw-flowmaster` `fd6c344befd9ce9e89648e6e404dd39f02e50bfaef2ca13d4e56ab84f5576617` (2 files); `flowmaster-validate` `ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af` (31 files), its declared digest |

Tree digests are `validate_gcfpe_20260914.skill_tree_digest`, run with `PYTHONDONTWRITEBYTECODE=1`.

### Evidence files

In `docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/`:

| File | What it is | Written |
|---|---|---|
| `edits.json` | The 69 prompt edits: for each, its member, item, what it removes, and its `old` anchor, or its `start` and `end` anchors, and its new text; plus the phrases that must be absent after, and the kept terms' counts | `PLAN` |
| `skill_edits.py` | PART-02's 32 skill edits, as literal old and new strings, each required to match once; it copies the two installed skills to a new directory, edits them, and recomputes `SKILL_TREE_SHA256` | `PLAN` |
| `guard_proof.py` | The validator guard's proof: each of its six identifiers, injected, is reported; with its guard line removed, it is not | `PLAN` |
| `PLAN-REVIEW-BRIEF.md`, `PLAN-REVIEW.md` | PL3's brief, committed before the reviewer is spawned, and its record, captured unedited | `PLAN` |
| `D24-BRIEF.md`, `SECTION-10-REVIEW-tw1-1.md`, `SECTION-10-REVIEW-tw1-2.md` | X1.4's filled skill brief, committed before the reviewers are spawned, and their two records, captured unedited | `EXECUTE` |
| `packages.json`, `CHANGE-NOTE.md` | X1.3's archive names, sizes and sha256; the note that goes to Nathan with the archives | `EXECUTE` |

### Before any write: X1.0, the preconditions

All read-only. If any fails, stop and return `IMPLEMENTATION_BLOCKED`; nothing has been written.

0. GTWPE-MGMT-10 092926.2, fetched live at the start of `EXECUTE`: edited 2026-09-29T23:47:58.009Z.
1. Each of the seven current members, fetched live: its edit time is §A's (*The members, read live*).
2. `edits.json`: every anchor found once in its member's fetch, and every span's `start` before its
   `end`, by reading, checked by a second reading.
3. The installed skills: `tw-flowmaster` and `flowmaster-validate` tree digests equal *Installed,
   before*. The synced directory is only read.
4. *HDE TW* and the selection page: no child page title ends `— «V»`.
5. The four control pages carry their anchors once (*The control texts*), at the edit times the dry
   run found: the selection page 2026-09-29T20:14:15.580Z, *Alpha 1* 20:15:21.232Z, *HDE TW*
   20:17:20.875Z, the *Glow Operations Hub* 20:18:21.747Z, and the GTWPE parent page
   2026-09-30T00:00:57.785Z. A later edit is read and recorded; the step stops only if an anchor is
   gone.

### The steps

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| X1.1 | — | the record | Status `EXECUTING`; fix «D» and «V»; record the UTC start | GTWPE-MGMT-10 X1 | In §E before X1.2 | None needed |
| X1.2 | PART-02 | `skill` | Build: `PYTHONDONTWRITEBYTECODE=1 python3 skill_edits.py <synced skills root> <scratch>/built`. Make an isolated root: every installed skill except `canva-drive-facebook-workflow` (F-3), with the two built skills in place of the installed ones. Run `validate_flowmaster.py --skills-root <root> --strict-warnings` from the built validator, then `guard_proof.py <root> <scratch>/guard` | Nathan's direction of 2026-09-30 (F-2); `D24` | The script exits 0 and prints the built values in *Values*; the validator exits 0, `FLOWMASTER_SUITE_PASS`, `self_identity` OK, `validator_revision` 3.3.2, no skill error or warning; guard proof 12/12, exit 0; `diff -rq` of each built skill against the installed lists only the files `skill_edits.py` edits; the Primary core block of `tw-flowmaster` is byte-identical; in the built `tw-flowmaster`, the broad terms of §A's skill scope occur only in its kept exceptions (`D26-E`) | Delete the scratch directory |
| X1.3 | PART-02 | `skill` | Package each built skill with `skill-creator`'s `package_skill` into `tw-flowmaster.skill` and `flowmaster-validate.skill`; write `packages.json` | `D24` ("each `.skill` by its digest") | `package_skill` reports `Successfully packaged skill` for each; each archive extracted in a clean directory equals its built tree (`diff -r`, no output); `packages.json` holds each archive's name, size and sha256 | Delete the archives |
| X1.4 | PART-02 | `skill` | Fill `reviewer-prompt-template.md`'s first template as *The D24 brief* says; commit it as `D24-BRIEF.md` and push; spawn two fresh reviewer subagents, neither forked nor context-inheriting, with the brief as their only prompt; capture each final answer unedited to `SECTION-10-REVIEW-tw1-<n>.md` | `D24`; *Capturing a reviewer's or worker's return* | Both return `SKILL_FIT_CONFIRMED`, bound to `packages.json`'s digests. A `SKILL_REPAIR_REQUIRED` stops `EXECUTE` before X2, since its repair changes the plan | None needed; nothing is installed |
| X1.5 | PART-01 | `prompt` | For each member in the order TRIAGE, DRAIN-10, DRAIN-20, RECORD-10, RECORD-20, APPLY-10, MGMT-10, three writes. (a) Fetch its parent (*HDE TW*, or for TW-MGMT-10 the selection page): no child titled `<title> — «V»`. (b) **Write 1:** `notion-duplicate-page` on its current page; «ID» is the returned ID. (c) Fetch «ID» until populated: at most six fetches, about 20 seconds apart (`sleep 20` in the background); populated means its first line is the current identity line, its last heading is the current version's, and no truncation or unknown block is reported. (d) **Write 2:** `update_properties`, title `<title> — «V»`. (e) **Write 3:** `update_content`, `allow_async: false`, the member's edits from `edits.json` in one call, in file order, «V» substituted; a span's `old_str` is composed from (c)'s fetch as `edits.json`'s rule says. If the call fails for no match and the only unmatched edit is the block, it is sent once more with the block's tags written without backslashes; any other failure stops | The prompt-page route; ITEM-01 and ITEM-02 | Fetch «ID» whole, into this session's context: the title and parent; the first two lines `<title> — «V»` and `Prompt Version: «V»`; each edit's new text present; each phrase of `absent_after` absent; each term of `counts_after` at its count, case-sensitive; the headings those of the current version. Every count by reading, checked by a second reading. Then fetch the parent: exactly one child carries the new title, and it is «ID»; the current page's edit time unchanged | Before X4, Nathan archives «ID»; the current page is untouched |
| X2 | — | the record | Commit the record and the `EXECUTE` evidence; run both record checks at `EXECUTING`; push; send Nathan the two archives, then `CHANGE-NOTE.md`, by `SendUserFile`; return `PRODUCT_OWNER_ACTION_PENDING`, `IN FLIGHT`, for his install | GTWPE-MGMT-10 X2 ("needs an install") | Both checks exit 0; the branch's blob equals the local file; #568 is open | — |
| X3 | PART-02 | `skill` | After Nathan says he has installed: read the installed trees; rebuild an isolated root from the installed skills, less the canva skill; run the validator from the installed `flowmaster-validate`, strict | GTWPE-MGMT-10 X3 ("for a skill, compare the installed digest"); `D24` | The installed `tw-flowmaster` and `flowmaster-validate` tree digests equal the built values; the validator exits 0 with X1.2's results. If the synced directory still holds the old digests, stop and record it: X3 resumes in a session Nathan starts after the install (S-3, `D26-C`) | Nathan reinstalls the prior archives, whose digests are *Installed, before* |
| X4.1 | — | — | `git fetch origin main`; fix «M»; `git log e000819..«M»` over *The watched sources*, less this Modification's files | GTWPE-MGMT-10 X4 | Each commit listed is a trigger finding in §E with its `D26-E` search | — |
| X4.2 | — | `notion_control` | **The catalog.** The GTWPE parent page, `update_content`: *CAT-OLD* becomes *CAT-NEW* | X4 ("set the checked-through commit") | Readback: *CAT-NEW* present, *CAT-OLD* absent, the rest of the page as the pre-read showed it | The reverse replacement, from the readback's text |
| X4.3 | PART-01 | `notion_control` | **The selection.** The selection page, `update_content`, one replacement: *S-OLD* becomes *S-NEW* | The route for TW-ALPHA's selection; F-1 | Readback: the new status line; below it *SECTION*, whose seven rows link the seven «ID»s at «V»; below that `## Historical selected release — TW-ALPHA-20260929.1`; every other heading and child page as the pre-read showed them | The reverse replacement, from the readback's text; or a newer release selecting the prior versions by the same writes |
| X4.4 | PART-01 | `notion_control` | *Alpha 1*, one replacement: `## Selected release — TW-ALPHA-20260929.1` becomes *SECTION*, a newline, and `## Historical selected release — TW-ALPHA-20260929.1` | Nathan's Q1 ruling of the first repair | Readback, by a script over the harness's save: the page begins with *SECTION*'s heading, then the renamed heading; 32 headings, the old list with one added and one renamed | As X4.3 |
| X4.5 | PART-01 | `notion_control` | *HDE TW*, one replacement: *HDE-OLD* becomes *HDE-NEW* | As X4.4 | Readback: the page begins with *HDE-NEW*; every other heading and child page as the pre-read showed them | As X4.3 |
| X4.6 | PART-01 | `notion_control` | The *Glow Operations Hub*, one replacement: *HUB-OLD* becomes *HUB-NEW* | As X4.4 | Readback, by a script over the harness's save: *HUB-NEW*'s heading once, directly above `## Historical Glow TW release — TW-ALPHA-20260929.1`; 139 headings, the old list with one added and one renamed | As X4.3 |
| X5 | — | the record | Dispositions for every step and item; `interaction_cost_actual` against 10; author, checker and acceptor of each part; status `COMPLETE`; commit and push. The branch is kept, since X2 waited for an install, not a merge | GTWPE-MGMT-10 X5 | Both record checks exit 0 at `COMPLETE`; the branch's blob equals the local file | — |

**Waiting for each update.** Every `notion-update-page` call is sent with `allow_async: false`; a
returned async task is polled until it succeeds before the readback (*Read back every write*).

**Order.** X1.2 to X1.4 build and review the packages; while the reviewers run, X1.5 creates the
pages. X2 waits for both. X4.3 to X4.6 run only after X3 passes (PART-01 after PART-02).

### The prompt edits (`edits.json`)

| Member | Edits | What they remove |
|---|---|---|
| TW-TRIAGE-10 | 4 | Identity (2); the block; the sentence that TW-ASSESS-10 supplies task assessment |
| TW-DRAIN-10, TW-DRAIN-20 | 12 each | Identity (2); the block; the relationship sentences; the Ultra clause; preflight step 5, keeping its prompt, baseline and capability checks; the checkpoints sentence, keeping its no-manifest rule; the corrected package's pre-Apply route; the READY next step, now TW-APPLY-10; the analyzer sentence; the handoff's recommendation field; "assessment" among its gates |
| TW-RECORD-10, TW-RECORD-20 | 6 each | Identity (2); the block; the optional-advice clause; the Ultra clause; preflight step 5, keeping its capability blocker |
| TW-APPLY-10 | 12 | Identity (2); the block; intake after the appraisal; the Strength Analyzer clause; the Ultra clause; preflight step 5 as the drains'; the three sentences requiring pre-Apply assessment, keeping the no-manifest rule; "assessment" in the no-change list; the report-only exemption; the diagnostic's model advice; pre-Apply for a corrected package |
| TW-MGMT-10 | 17 | Identity (2); the block; the eight-member catalog, now seven, and TW-ASSESS-10's relationship; its three membership mentions; the workers' Strength Analyzer checkpoints; its mandate; the analyzer paragraph; the Ultra gate; the research, workload, human-guidance and account-picker sentences, keeping the header scheme and capability rule; the alpha invariants' checkpoints, recommendations and advisory research; the `openai-docs` sentences; the analyzer and advice validation cases; "followed by its human guidance"; "model evidence" |

**Total:** 69 edits, 14 of them identity lines, covering §A's 63 passages. Every kept term is one of
§A's exceptions. The guard (`GUARD-001`) is X1.5's absence check: `operator_model_guidance`,
`TW-ASSESS-10`, `Ultra`, `Strength Analyzer`, `pre-Apply`, `analyzer`, `recommendation`, `Astra`,
`GPT-`, `surface`, `effort`, `reasoning`, `openai-docs`, `human guidance`, `apprais` and
`eight-member` absent from every new page (`D26-E`).

### The skill edits (`skill_edits.py`)

`tw-flowmaster/SKILL.md`, 21 edits: §A's 23 passages as 20 edits (line 341's three as two, and
lines 351's and 352's two each as one), and the revision, 1.2.0 to 1.3.0. The profile's condition becomes "carry the exact no-redlines contract";
READY output points to TW-APPLY-10; line 339 keeps only "Record actual configuration only when
directly verified."; lines 351 and 352 keep only their GCFPE sentences.

`flowmaster-validate`, 11 edits: in `validate_flowmaster.py`, the TW revision required as 1.3.0, the
three old required terms removed, and six forbidden identifiers added for `tw-flowmaster`
(`TW-ASSESS-10`, `PRE_CREATION_ASSESSMENT`, `PRE_APPLY_ASSESSMENT`, `STRENGTH_ANALYZER_PROMPT_ID`,
`APPLICATION_REASONING_POLICY`, `PF_RENDERED_PAGE_COUNTS`); `validator_revision` 3.3.1 to 3.3.2 at
its four sites (three scripts and the GCFPE validation profile, P-F2); `FLOWMASTER_VALIDATE_REVISION` 3.3.1 to 3.3.2; `SKILL.md`'s TW paragraph;
and, after the edits, `SKILL_TREE_SHA256` recomputed.

### The control texts

In these, `«ID:X»` is member X's new page, and each row is one line.

**S-OLD**, the selection page's status line and the current release's heading, two lines:

```
**Status: TW-ALPHA-20260929.1 selected; TW-MGMT-10 repaired and verified. Live follow-up trial pending; PF04 cause unresolved.**
## Selected release — TW-ALPHA-20260929.1
```

**S-NEW:** the line below, a newline, *SECTION*, a newline, and
`## Historical selected release — TW-ALPHA-20260929.1`:

```
**Status: «R» selected; model advice removed and TW-ASSESS-10 retired. Live follow-up trial pending; PF04 cause unresolved.**
```

**SECTION**, on the selection page and on *Alpha 1*:

```
## Selected release — «R»
**Selected: «S».** Authority: MODIFICATION-20260930-gtwpe-tw-model-advice, run through GTWPE-MGMT-10 on Nathan's plan approval of «PA». As Nathan directed on 2026-09-29, no member carries a model, surface or effort recommendation, a workload profile or a strength rating, and TW-ASSESS-10 is retired with no replacement: no assessment runs before creation or application, and a READY package goes straight to TW-APPLY-10. Every row below is new. The *Current operation* and *Verification and runtime limits* of TW-ALPHA-20260908.1, below, still apply except where they run or name TW-ASSESS-10 or give model or effort advice; the next manual entry is the selected drain prompt. TW Flowmaster 1.3.0 and flowmaster-validate 3.3.2, installed by Nathan, match this release. All old prompt pages remain intact; TW-ASSESS-10 090826.2 is not selected.
- `TW-TRIAGE-10` — <mention-page url="https://app.notion.com/p/«ID:TRIAGE»"/> — PF10 target list only; «V».
- `TW-DRAIN-10` — <mention-page url="https://app.notion.com/p/«ID:DRAIN-10»"/> — General PF redlines/report or exact no redlines; «V».
- `TW-DRAIN-20` — <mention-page url="https://app.notion.com/p/«ID:DRAIN-20»"/> — PF09 redlines/report; board optional; «V».
- `TW-RECORD-10` — <mention-page url="https://app.notion.com/p/«ID:RECORD-10»"/> — PF20 paste-ready section only; «V».
- `TW-RECORD-20` — <mention-page url="https://app.notion.com/p/«ID:RECORD-20»"/> — PF30 paste-ready section only; «V».
- `TW-APPLY-10` — <mention-page url="https://app.notion.com/p/«ID:APPLY-10»"/> — Atomic validated application plus bounded header provenance; «V».
- `TW-MGMT-10` — <mention-page url="https://app.notion.com/p/«ID:MGMT-10»"/> — Sole TW prompt maintenance owner; «V».
```

**HDE-OLD** is `## Current TW release — TW-ALPHA-20260929.1`. **HDE-NEW:**

```
## Current TW release — «R»
<mention-page url="https://app.notion.com/p/3d44590a05eb8171ab6ff4dab33b00ef">Glow Technical Writing Ecosystem</mention-page> selects «R»: every member at «V», with no model, surface or effort recommendation, and TW-ASSESS-10 retired with no replacement, so a READY package goes straight to TW-APPLY-10. Entry: the selected drain prompt. Maintenance owner: <mention-page url="https://app.notion.com/p/«ID:MGMT-10»"/>. The 2026-09-08 follow-up below still applies except where it runs or names TW-ASSESS-10 or gives model advice. Exact rows: <mention-page url="https://app.notion.com/p/3d44590a05eb81fe991ff0114cb43029"/>. Changed by MODIFICATION-20260930-gtwpe-tw-model-advice, run through GTWPE-MGMT-10 on Nathan's plan approval of «PA».
## Historical TW release — TW-ALPHA-20260929.1
```

**HUB-OLD** is `## Current Glow TW release — TW-ALPHA-20260929.1`. **HUB-NEW:**

```
## Current Glow TW release — «R»
**«R» is selected.** <mention-page url="https://app.notion.com/p/3d44590a05eb8171ab6ff4dab33b00ef"/> and <mention-page url="https://app.notion.com/p/3d44590a05eb81fe991ff0114cb43029"/> hold the exact seven-member catalog. Every member is at «V», with no model, surface or effort recommendation, and TW-ASSESS-10 is retired with no replacement. Maintenance: <mention-page url="https://app.notion.com/p/«ID:MGMT-10»"/>. The 2026-09-08 follow-up below still applies except where it runs or names TW-ASSESS-10 or gives model advice. Changed by MODIFICATION-20260930-gtwpe-tw-model-advice, run through GTWPE-MGMT-10 on Nathan's plan approval of «PA».
## Historical Glow TW release — TW-ALPHA-20260929.1
```

**CAT-OLD**, in the GTWPE catalog's *Checked-through commit*:

```
`e0008199e4ba83ad04ffa576c34fc0785da99cf9` (`e000819`), examined by `EXECUTE` of MODIFICATION-20260929-gtwpe-first-repair on 2026-09-29.
```

**CAT-NEW:**

```
`«M, full»` (`«M»`), examined by `EXECUTE` of MODIFICATION-20260930-gtwpe-tw-model-advice on «the X4.1 date». Before it, `e000819`, examined by `EXECUTE` of MODIFICATION-20260929-gtwpe-first-repair.
```

A readback compares a mention by its link, since Notion shows a linked page by its title (the pilot's
PF-27).

### The `D24` brief (X1.4)

The first template of `reviewer-prompt-template.md`, every slot filled. §1: the two archives from
`packages.json`, installed together. §2: `NONE`, first review. §3: the installed trees' digests
(*Installed, before*) and the built ones, by `skill_tree_digest`. §4: this repository, branch
`docs/20260930-modification-gtwpe-tw-model-advice`, not merged, pull request #568; `AGENTS.md`;
`skill_edits.py`, `guard_proof.py` and this record. §5, the claims: C1, the built skills differ from
the installed only as `skill_edits.py` says; C2, the Primary core is byte-identical; C3, no stage,
input or rule of `tw-flowmaster` runs, requires or names TW-ASSESS-10, and no fixed model or effort
policy remains, outside §A's kept exceptions; C4, the suite passes strict, and each new guard fires;
C5, the authority is Nathan's direction of 2026-09-30, quoted from §A. §6, to attack: A1, the
rewritten profile condition and what now governs a selected-catalog run; A2, the kept GCFPE
clauses (C4 of §A) and line 339's kept rule; A3, the fourth `validator_revision` site (P-F2), in a
GCFPE reference; A4, whether any fixture or reference still expects the old terms. §7: the
canva skill's front matter (F-3); the isolated root. §8: X1.2's and X1.3's commands. §9: the
template's prohibitions, and no prompt body is fetched.

**`CHANGE-NOTE.md`**, to Nathan with the archives: the two archives' names and sha256; what changed
(this plan's two paragraphs above); the two reviewers' verdicts; that the selection waits for his
install; and that he installs both together, and rolls back by reinstalling the prior archives.

### Failure path (`D26-B`)

Before X1.5's first write, a failure stops `EXECUTE` with nothing written. After it: a failure record
in §E, a read-only sweep of the pages this run created and the control pages, the freeze kept, and a
return to Nathan. Pages already created stay unselected until he archives them; a landed control
write is undone by its reverse replacement, never from page history. A partial skill install is his
to reverse by reinstalling the prior archives.

### Open findings, accepted as risks

| # | Risk | Likelihood | Consequence |
|---|---|---|---|
| K-1 | §A's S-1, accepted by Nathan's direction: between the install and X4.3, the installed profile matches the old release and skips the assessments it requires | Low: the window is X3 to X4.3 in one session | A Flowmaster run started in that window would skip them |
| K-2 | 18 span edits, seven of them the blocks, compose `old_str` from the fetch; a wrong character fails the call | Low | Loud: the call fails, and the step stops before its readback |
| K-3 | A multi-edit `update_content` call may be applied in part | Low | Loud: X1.5's readback catches it; the page stays unselected (the first repair's K-15) |
| K-4 | X3's validation needs the isolated root (F-3), and this session may not see the install (S-3) | Certain for F-3; unknown for S-3 | Loud: X3 stops and resumes in a new session |
| K-5 | The reviewer checks the plan without prompt bodies (`D22`); only the dry run and X1.0 check anchors against them | Certain | A wrong anchor fails loudly at X1.5 |
| K-6 | TW has no executable check or live trial | Certain | The selection page says runtime is unproven |

### Product Owner actions

| # | Action | How it is verified |
|---|---|---|
| PO-1 | Approve this plan. It authorizes the 21 page writes of X1.5 and the five control writes of X4.2 to X4.6, and nothing else in Notion | `plan_approved_by` |
| PO-2 | Install the two archives X2 sends, together | X3's digest comparison and validation |
| PO-3 | Merge #568 when the record is `COMPLETE` | Not needed by this run (`D21-C`) |
| PO-4 | Only after a failure: archive unselected pages, or reinstall the prior archives | The failure record's sweep |

### Explicitly not in scope

- **C5, from Nathan's direction at approval:** a skill route in GTWPE-MGMT-10 with a skill check
  layer modelled on the GCFPE one, so a skill part runs through the change prompt instead of around
  it (with F-2). For GTWPE-MGMT-10's next repair.
- C2 (F-1), C3 and C4 of §A; the canva skill (F-3); the stale Flowmaster revisions on the selection
  page's historical limits; TW-ASSESS-10's page, which stays intact and unselected.

### Dry run (PL3)

On 2026-09-30, from about 02:05Z, by this session, read-only, before any full review.

| # | Gate | Result |
|---|---|---|
| P1 | `modification_validate.py` and `gtwpe_record_check.py` (on `main` at `f83c755`) on this record at `PLANNED`, with this round in `reviews` | Both exit 0, 1/1 |
| P2 | `git fetch --prune origin`; the watched-path log from `e000819` | `main` still `f83c755`; the log lists nothing |
| P3 | The seven members, fetched live at this mode's start | Each at §A's edit time |
| P4 | `edits.json`'s anchors in those fetches | Every `old`, `start` and `end` found once, and every `start` before its `end`, by reading, checked by a second reading |
| P5 | The control pages | The selection page 2026-09-29T20:14:15.580Z, *S-OLD* once, as its first two lines; *HDE TW* 20:17:20.875Z, *HDE-OLD* once, as its first line; *Alpha 1* 20:15:21.232Z and the *Glow Operations Hub* 20:18:21.747Z, each read by script from the harness's save: the anchor once, and 31 and 138 headings; the GTWPE parent page 2026-09-30T00:00:57.785Z, *CAT-OLD* once |
| P6 | X1.0 (4) for 2026-09-30 | No child page of *HDE TW* or of the selection page carries a `093026` version |
| P7 | X1.2 on the installed skills, in the scratchpad | `skill_edits.py` exits 0 and prints *Values*' built digests; the validator exits 0 with `--strict-warnings`: `FLOWMASTER_SUITE_PASS`, `self_identity` OK, `validator_revision` 3.3.2, no skill error or warning; the guard proof 12/12, exit 0 (each "guard disabled" case exits 1 on the validator's own digest, with no `tw-flowmaster` error, as expected); `diff -rq` lists exactly the six edited files; the core block identical; in the built `tw-flowmaster`'s specialization, the broad terms remain only on its kept exceptions: GCFPE lines, the stall prohibitions, `/model`, the checksum, the report row, and "checkpoint" meaning a ledger checkpoint |
| P8 | The same with `validator_revision` moved at three sites only | Exit 1: `change-flow` reports `FMV-GCF-CURRENT-001: PROFILE_IDENTITY` (P-F2) |
| P9 | `edits.json`, by script | 69 edits, 69 distinct IDs, 18 spans; no new text holds a phrase of `absent_after` |
| P10 | X1.3, trial packaging | Both archives written (19,193 and 322,860 bytes); 2 and 31 entries, none outside its root; each extracted tree equals the built one (`diff -r`, no output) |
| P11 | The front matter and tables, by script | They parse, and every table row has its table's column count |

Not exercised: any Notion write, X1.5's duplication and polling, X3's install, and the reviewers.

### Harness files (`D22` condition 5), for `PLAN`

- **This session's transcript** holds, from this mode, the bodies of the seven members and the control
  pages *Glow Technical Writing Ecosystem*, *HDE TW* and the GTWPE parent page, each fetched once into
  context. No script read the transcript; every anchor was found by reading. It is left to teardown.
- **Two tool-results saves**, both control pages: *Alpha 1* and the *Glow Operations Hub*, each read
  by script for its edit time, headings and anchor, then deleted (exit 0).
- **The skill files** were read by `grep`, `sed` and scripts, and copied into the scratchpad.
- **Scratch:** `gen_skill_edits.py` and `make_tw_edits.py`, which wrote the evidence files;
  `sectionP.md`, this section's draft; `ctl.py`; `pl-out/`, `pl-root/`, `pkg/` and `pkgx-*/`, the
  built skills, isolated root and trial archives; `pl-*.json` and `pl-*.txt`, gate output. No
  transient file holds a prompt body.

### Cost of this mode

Time: from 01:59Z, when Nathan's approval was recorded, to PL4. Tokens: not measured by this
session.

### Canon and rulings relied on

- Nathan's approval of 2026-09-30 and its three directions, quoted in `analyze_approved_by`.
- GTWPE-MGMT-10 092926.2, as fetched live: *PLAN*, *EXECUTE*, *How each kind of target changes*,
  *Reviews are bounded*, *Reading prompt bodies*, *Boundaries*.
- `gcfpe.decision-record.md` `D22`, `D24` and `D26`; `reviewer-prompt-template.md`, both templates;
  `modification-template.md` 2.1.
- HDE Governance (PF04) §9.1.6, as §A read it; HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001: no
  model or effort level is a requirement, which the removed texts no longer imply.
- The pilot's and the first repair's records, for the selection writes, the readback of mentions
  (PF-27) and the one-call edits.

## §E — Execution
