---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261005-gtwpe-tw-repository-io
status: ANALYZED
targets: [prompt, notion_control]
gate_tier: 2
closure:
  upstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20]
  downstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20]
  state_sharers: [TW-DRAIN-10, TW-DRAIN-20]
readiness: NEEDS_RULING
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 8
interaction_cost_actual:
estimate:
  plan: "about 3.5 h: §P for 72 passages and 12 identity lines in six members (anchors, new texts, phrase and absence checks), the selection page's three writes with a new Current operation, the three current-release notes and the catalog's checked-through commit; a dry run, and one full review by a single reviewer. Time is the meter the session can read; tokens are not measured"
  execute: "about 3 h, not counting any wait for Nathan: six new versions (duplicate, title, edits), each read back whole by this session; the selection's three writes, the three notes and the catalog, each read back; the record. Time is the meter"
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-10-05
    required_open: 0
    outcome: "By this session, read-only: both record checks exit 0 on a scratch copy at ANALYZED; both selftests pass (17/17, 66/66); the front matter and every table parse, and the request is verbatim; A0 reproduces at 20d0dd8; the new titles and the release label are free; a second reading of the six bodies corrected one count (TW-DRAIN-20, reference, 14 to 15) and added PFCanon to the broad terms, both reflected in the scope; the record tools need no change. No required defect. No full review"
items:
  - id: ITEM-01
    statement: "The TW prompts stay single-homed in Notion: no TW prompt body, copy or excerpt enters the repository, and this change alters where they read and write, not where they live."
    source: "Request item 1; Nathan, 2026-10-05: \"writing prompts do not belong in repo.\""
    disposition: ""
  - id: ITEM-02
    statement: "TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10 take PF canon from docs/pfcanon/ on main, not from Google Drive, and take their other inputs as attached files or repository paths, never from Drive or ChatGPT Library."
    source: "Request item 2; HDE Build Notes 2.29 PF10-CANON-001; MODIFICATION-20261005-gtwpe-writing-side §A A.1, its row for the architecture's §2 (inputs), which the request cites"
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
parts:
  - id: PART-01
    name: "The six operational TW prompts on repository input and output, with proof logs, and the new TW-ALPHA release"
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06]
    class: B
    after: []
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

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
100526.2*, the version the catalog selects. It was fetched live at the start of the mode, and again after
a context compaction, as its *Reading prompt bodies* requires; both fetches show it edited
2026-10-05T16:36:11.384Z. The mode started at 2026-10-05T19:39:01Z, with `main` at `20d0dd8`. The request
is in the front matter, verbatim. The record is on `docs/20261005-modification-gtwpe-tw-repository-io`,
the Modification's own branch, as 100526.2 requires (*Entry contract*; *The record*, its *Branch* row). Its
open pull request is amthorn78/glow-hdengine-v2#575. The session's harness had named another branch, and
nothing was pushed there.

### Consult

- **Repository**, on `main` at `20d0dd8`.
  - C1's record, MODIFICATION-20261005-gtwpe-writing-side. Its approved §A sets C2's place in the order
    (A.5) and frames what C2 carries: A.1, A.4 and A.8.
  - The error ledger on `main`, among them E-029, E-032 and E-033.
  - The GTWPE decision record, whole: GTWPE-D1 and what follows from it.
  - The record of TW's latest selection, MODIFICATION-20260930-gtwpe-tw-model-advice: its dispositions,
    the pages it wrote, its Flowmaster question and its control texts.
  - `TW-MGMT-10-ANALYSIS-20260924.md`, findings F1 (the canon source is inverted) and F2 (output has no
    lawful destination).
  - In `docs/prompt_ecosystem_management/`: `modification-template.md` 2.1; `ecosystem-change-management.md`
    §1 and §2; the header of `gtwpe/gtwpe_record_check.py`; and `gcfpe.decision-record.md` `D22`.
  - No `docs/*-modification-gtwpe-*` branch was open (`git ls-remote`), so this ID is new.
- **Installed skills**, read as files: the *Technical Writing specialization* of `tw-flowmaster` 1.3.0's
  `SKILL.md`, through its *Selected-catalog TW profile*.
- **Canon**, on `main` at `20d0dd8`, unchanged since `31deec4`.
  - Searched with `git grep` for the task's terms: `PF10-CANON-001`, `ChatGPT Library`, `change-process
    documents`, `proof log`, `redlines file`, `downloadable`, `TW prompt`, `TW-ALPHA` and the member IDs.
  - Read in full: HDE Build Notes (PF10) 2.29 PF10-CANON-001 and 2.38 PF10-AINEUTRAL-001; HDE Governance
    (PF04) §9.1.3 to §9.1.6.
  - Canon names no TW prompt. It uses "proof log" only for evidence about the engine itself, as GTWPE-D1
    records.
- **Notion, read-only.**
  - The GTWPE parent page and its catalog, edited 2026-10-05T16:37:57.178Z: GTWPE-MGMT-10 at 100526.2,
    checked-through commit `31deec4`.
  - The selection page, *Glow Technical Writing Ecosystem*, edited 2026-10-05T00:30:29.861Z.
  - The six TW bodies that change, at 100426.1, each fetched live after the compaction and read whole
    (*The members, read live*).
  - *HDE TW*, *Alpha 1*, the Glow Operations Hub and the architecture page, for A3.
  - A search for "Glow HDE Living Prompt Flow Map" finds no page by that name, as on 2026-09-30.

### Drift check (A0)

`git fetch origin main`; the commit examined is `20d0dd84898b2d26ae7e7122eba16ac640350ba7` (`20d0dd8`),
#574's merge.

**(a) The lineage sources.** Searches with highlights off on `PE Metaprompt` and `GCFPE-MGMT-10` found no
page that the catalog does not record and that is newer than its record. The other PE Metaprompt hits are
archived predecessors dated 2026-09-12 and 2026-09-13. The other GCFPE-MGMT-10 hits are the archived
`091326.2` and control or tracking pages. Each recorded page was fetched for its exact edit time. The PE
Metaprompt's fetch and the register's were saved by the harness and read by script (*Harness files*).

| Source | Recorded in the catalog | Found, by fetch | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1`, 2026-09-24T15:38 | 11:00:24.691Z; `091426.1` (`3db4590a05eb81d1bb64ebcb3ca8eb54`) at 15:38:34.295Z; the register selects it | None |
| PE Metaprompt | Pinned and selected: `091426.1`, 2026-09-23T17:17:22.217Z | 17:17:22.217Z; the register selects it (`3db4590a05eb8174be35d9e35acb3f77`) | None |

The register page was at 2026-09-23T17:43:39.489Z, the edit time the catalog records.

**(b) The watched paths.** `git log 31deec4..20d0dd8` over *The watched sources* lists nothing. The range
holds two commits, #573 and #574. They change ten files, all under `docs/ephemeral/`, as PE39's request
expects.

No trigger finding. X4 re-pins nothing and moves the checked-through commit to the commit it examines.

### The members, read live

Each member that changes was fetched whole into this session's context after the compaction and read
whole. Each edit time equals the one C1 recorded, so no member has changed since its selection.

| Member | Version, page | Edited | Parent |
|---|---|---|---|
| TW-TRIAGE-10 — Identify PF10 Drain Targets | 100426.1, `3ef4590a05eb818e8295e1b9b2a09248` | 2026-10-04T13:43:27.279Z | *HDE TW* |
| TW-DRAIN-10 — Prepare PF Document Redlines | 100426.1, `3ef4590a05eb81d2a49fcf337bdfd831` | 2026-10-04T14:07:14.620Z | *HDE TW* |
| TW-DRAIN-20 — Prepare PF09 Redlines | 100426.1, `3ef4590a05eb81358170d58214cb1018` | 2026-10-04T14:08:48.149Z | *HDE TW* |
| TW-RECORD-10 — Create Epic History Section | 100426.1, `3ef4590a05eb81f28e25fb2cb7044eaa` | 2026-10-04T14:16:53.241Z | *HDE TW* |
| TW-RECORD-20 — Create CRD History Section | 100426.1, `3ef4590a05eb81cba424e4d3ec08871f` | 2026-10-04T14:20:11.935Z | *HDE TW* |
| TW-APPLY-10 — Apply Validated Redlines | 100426.1, `3ef4590a05eb8107a59bcc474348ca5e` | 2026-10-04T16:28:52.435Z | *HDE TW* |

TW-MGMT-10 100426.1 (`3ef4590a05eb81b5bc74f393bdf358b9`, under the selection page) does not change. It
leaves the selection, and its page stays as it is. It was read whole in this mode before the compaction and
not again, since no step here relies on its text. Its disposition rests on the selection page and on the
lines in the six members that name it.

### The change, settled

The request's six points, by item. C1's approved §A, which the request cites (A.1, A.5 and A.8), frames
them.

**ITEM-01. The prompts stay in Notion.**
- No TW prompt body or copy enters the repository: C2 changes where the prompts read and write, not where
  they live.
- Nathan's words make this a rule for TW. It matches HDE Governance §9.1.6, which keeps reusable GCFPE
  prompt bodies single-homed in Notion, and HDE Build Notes 2.29: "GCFPE prompt bodies remain single-homed
  in Notion".
- One point is open: whether an edit's shortest unique anchor counts as an excerpt (Q-2). Until Nathan
  answers, this record quotes no TW body beyond a short clause.
- Verified at `EXECUTE`: the branch changes only the record and its evidence, and no evidence file holds
  more of a body than Q-2's answer allows.

**ITEM-02. Reading.**
- **R1, canon.** Each of the six reads current authoritative PF Markdown from `docs/pfcanon/` on `main`,
  read-only, and records the commit it read. The PF10 build notes and PF09's phase files are resolved
  there too. A Drive copy, a native Google Doc, memory or reconstructed text is no substitute. HDE Build
  Notes 2.29: "PF-Canon is held in `docs/pfcanon/` on `main`", and "A native Google Doc, a Markdown export,
  a Google Drive folder or a Notion page confers no PF authority".
- **R2, other inputs.** The change source, a drain's package and a record's specification come as attached
  files or repository paths, never from Drive or ChatGPT Library. This is C1 §A A.1's row for the
  architecture's §2, which the request cites.

**ITEM-03. Writing.**
- **R3, outputs.** Each prompt that writes a file:
  - writes it at the repository path its invocation names, under `docs/ephemeral/`;
  - commits it and pushes it on the branch the invocation names, which then has one open pull request,
    opened if none is;
  - never merges, writes under `docs/pfcanon/`, or writes to Google Drive or ChatGPT Library (HDE Build
    Notes 2.29; HDE Governance §9.1.3, whose "prohibition on Drive persistence" stands);
  - stops on an invocation that names no such path, as a missing input, and invents none;
  - gives each output's repository path in its final response.

  TW-TRIAGE-10 still writes nothing: its list stays in the response.
- **R6, run mode.** Each prompt runs as Nathan's direct invocation, or as a pass inside a session he
  started. A pass needs no `TW-PFxx-x` document session of its own. No prompt creates or messages another
  session.

**ITEM-04. Proof logs.**
- **R4.** One file serves as each report and its artifact's proof log, so the two cannot drift apart
  (`DERIV-001`; C1 §A A.8):
  - TW-DRAIN-10's and TW-DRAIN-20's processing report becomes the proof log of the redlines file;
  - TW-APPLY-10's application report becomes the proof log of the revised PF.
- Each proof log is saved beside its artifact, in the same directory, and named after it.
- It carries GTWPE-D1's requirement and its eight minimum items in Nathan's words, so that GTWPE-MGMT-10's
  readback can find each by phrase. The report's present contents stay with them.
- TW-APPLY-10's proof log also states, for each applied operation, its redline ID and the basis the
  preparer's proof log gives for it, not only a pointer to it.

The `GTWPE-D1` record that A2 asks for:

| Prompt | Writes before the change | Writes after it | How the part leaves `GTWPE-D1` whole |
|---|---|---|---|
| TW-DRAIN-10 | A redlines Markdown file, for `READY` and for `BLOCKED` work kept as non-applicable redlines, and a processing report, to Library. Nothing for the exact `no redlines` exit | The redlines file and its proof log (the processing report), beside it and named after it, at the invocation's path. Nothing for `no redlines` | A separate proof log for the redlines file, with all eight minimum items in Nathan's words, linked by its name, its place and the identities it records (item 8). Today the report lacks item 5 and the deviations of item 7 (C1 §A A.8) |
| TW-DRAIN-20 | As TW-DRAIN-10, for a PF09 phase file | As TW-DRAIN-10 | As TW-DRAIN-10 |
| TW-APPLY-10 | The revised PF, a final updated PF Markdown file, and an application report, to Library. A diagnostic and no PF on failure | The revised PF and its proof log (the application report), beside it and named after it. A diagnostic and no PF on failure | A separate proof log for the revised PF, with all eight items, the basis of each applied operation stated, and the same link. Today the report gives item 4 only by pointer and lacks item 5 and deviations |
| TW-RECORD-10, TW-RECORD-20 | One paste-ready section file | The same file, at the invocation's path | Not bound: a section is neither artifact type. C3 binds them once each writes its section into a PF20 or PF30 drafts copy |
| TW-TRIAGE-10 | A list in the response | The same | Not bound |

No prompt writes both artifact types, so no combined proof log is defined. Neither a diagnostic nor
TW-APPLY-10's optional no-change report is an artifact: neither creates a revised PF.

**ITEM-05. The maintainer.**
- **R5.** Each of the six names GTWPE-MGMT-10 as its maintainer where it now names TW-MGMT-10, and keeps it
  no prerequisite on document turns.
- GTWPE-MGMT-10 100526.2 is already "the route by which a TW-ALPHA member is repaired" (*Native purpose*).
  Its "until G5" (E-033) stays for C6, as the request says.
- TW-MGMT-10 leaves the selection. Its page is not edited, since the route never edits an existing
  TW-ALPHA page.

**ITEM-06. The new release.**
- A new TW-ALPHA release, «R» (`TW-ALPHA-<yyyymmdd>.N`, dated by its selection), selects the six new
  versions. TW-MGMT-10 is not among them.
- The change alters how the TW flow runs (below), so the release carries a new *Current operation*, and the
  one it replaces becomes historical.
- The interacting skill `tw-flowmaster` is Q-1.

**Not in C2**, as the request says:
- C3's document rules, the Last Update Gate among them, which waits for Nathan's PF10 sentence;
- the Flow Manager (C4), the Change Manager (C5) and adoption (C6);
- E-033, which stays for C6.

### How the TW flow runs, after the change (A3)

The selected release's *Current operation* describes the flow:
- a drain, TW-DRAIN-10 or TW-DRAIN-20, ends at `no redlines` or with a `READY` package;
- TW-APPLY-10 validates and applies the package, or returns a diagnostic to the originating preparer;
- triage stays list-only, and the record prompts section-only.

Its text also keeps the rules of TW-ALPHA-20260908.1's historical operation, among them "Current Drive
PFCanon and repository mirrors stay read-only to TW workers".

C2 keeps the shape and changes how each step reads, writes and hands on:
- canon comes from `docs/pfcanon/` on `main`, and other inputs are attached files or repository paths;
- each output goes to the invocation's path under `docs/ephemeral/`, committed and pushed, its path named in
  the final response;
- a `READY` package is the redlines file and its proof log, by repository path, and a verified result is the
  revised PF and its proof log;
- a step runs as Nathan's direct invocation or as a pass inside a session he started;
- GTWPE-MGMT-10 maintains the prompts.

So the change alters how the flow runs. The new release carries its own *Current operation* stating this,
and the 2026-09-08 rules it keeps no longer include the Drive sentence. `PLAN` writes the text, and the
route's readback requires exactly one *Current operation* heading on the page.

### Per part: closure, tier, class and targets

One part, PART-01: the six new versions and the new release, which land together. A new version with no
selection has not landed. A selection that mixed repository and Library input and output would break the
drain-to-apply handoff, whose two sides change here.

- **Targets.**
  - `prompt`: the six new versions, each a new versioned sibling under *HDE TW*.
  - `notion_control`: the selection page's three writes; the current-release note on *Alpha 1*, *HDE TW*
    and the Operations Hub; and the catalog's checked-through commit at X4.
- **Closure**, from the relationships in the selected release's *Current operation*:
  - upstream, the producers of the handoffs the changed members consume (the drains' `READY` package and
    TW-APPLY-10's diagnostic): TW-APPLY-10, TW-DRAIN-10 and TW-DRAIN-20;
  - downstream, their consumers: the same three;
  - state sharers: TW-DRAIN-10 and TW-DRAIN-20, which share `READY`, `NO_CHANGE` and `BLOCKED`.

  TW-TRIAGE-10 and the record prompts have no recorded relationship with another member. Every member in
  the closure changes here.
- **Tier 2.**
  - The part changes a handoff: what a `READY` package holds (the report becomes the proof log), where it
    lives (a repository path, not Library), and TW-APPLY-10's intake check. Both sides change in this
    Modification.
  - TW has no executable selftest, and no live trial has run since 2026-09-08. So the gate is a static
    check of both sides of the handoff, with the whole-page readbacks, as the last TW change's was.
- **Class B, rule application.** The part carries rulings already made into the prompts:
  - HDE Build Notes 2.29 (`D7`), on where canon is read and where change-process documents are stored;
  - GTWPE-D1;
  - Nathan's approved order (C1 §A A.5), with his words that writing prompts do not belong in the
    repository.
- **Authoring.**
  - Through the selected PE Metaprompt's general rules, with GTWPE-MGMT-10's workarounds (*Relation to the
    PE Metaprompt*): only the approved edits and the two identity lines change, references stay versionless,
    and no model or effort text is added.
  - "Converge on existing wording" (`ecosystem-change-management.md` §2, step 3): the GCFPE's
    Drive-to-repository storage pass applied the same rule to 44 prompts. Its wording, such as the
    *Artifact and source boundaries* of GCFPE-MGMT-10 091426.1 (read live at A0), is the model for R1 and
    R3.

### Member dispositions (HDE Governance §9.1.6)

| Member or interface | Disposition | Reason |
|---|---|---|
| TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-APPLY-10 | Affected: a new version each | R1, R5 and R6 reach all six; R2 and R3 the five that take inputs or write files; R4 the drains and the apply |
| TW-MGMT-10 100426.1 | Affected: leaves the selection; page unchanged | Request item 5: GTWPE-MGMT-10 maintains the TW prompts |
| TW-ASSESS-10 | Unaffected | Retired and unselected since TW-ALPHA-20261004.1 |
| GTWPE-MGMT-10 100526.2 | Unaffected | It already repairs TW-ALPHA members and makes the selection writes. Its route text assumes eight members (F-1, below). Its "until G5" stays for C6 (E-033) |
| The GTWPE catalog | Unaffected, but for X4's checked-through commit | Its members note already says the TW prompts join the catalog when the build selects them, which is C6 |
| `tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Affected | Q-1 |
| `glow-write-boundary`, `glow-artifact-storage` | Unaffected | `docs/ephemeral/` is a path a session may write, and the new route stays inside it |
| The PE Metaprompt 091426.1; the GTWPE decision record | Unaffected | The authoring control, and the ruling applied |
| UTIL-10 (GCFPE) | Unaffected | GCFPE-owned; it overlaps TW-APPLY-10 in name only (TW-MGMT-10 analysis, F10) |
| The GCFPE register and Flow Index; the *Living Prompt Flow Map* | Unaffected | The first two list no TW member, and no page by the third's name exists |

### Scope, and how it was measured (`SCOPE-001`)

**Method: broad match minus permitted exceptions, by reading.**
- Each body came back inline and complete, with no truncation flag, and was read in context.
- Every count below was made by reading the fetch, then checked by a second reading of the same fetch. No
  command counted over a body.
- Matches are case-insensitive, on the stem.
- The broad terms, by rule:
  - R1: `Drive`, `PFCanon`, `mirror`;
  - R2 and R3: `Library`, `download`, `upload`, `reference`, `retriev`, `attach`;
  - R4: `report`;
  - R5: `TW-MGMT-10`;
  - R6: `session`, `initiat`.

**What is in scope.** A passage is a contiguous stretch of in-scope text. Each passage:
- reads or resolves PF canon or PF10 through Drive, names Drive as PF authority, or forbids the
  repository's canon as a "repository mirror" (R1);
- takes an input from Library, Drive or an unnamed "authorized" reference (R2);
- routes an output to a download, an "artifact route" or Library (R3);
- names the pair a drain or the apply writes, defines its report's contents, or hands the package on (R4);
- names TW-MGMT-10 as maintainer or as no prerequisite (R5);
- or requires a dedicated `TW-PFxx-x` document session, or Nathan's own launch in a way that excludes a pass
  (R6).

**The permitted exceptions, kept unchanged:**
- the bans on writing to Drive, which HDE Governance §9.1.3 keeps, though a sentence around one may change;
- a native Google Doc as no substitute for canon;
- "mirror" in the rule on current-repository claims, which concerns the repository's code, not canon;
- generic locators that a repository path satisfies: a "usable retrieval reference", a provider ID or
  usable retrieval reference, actual accessible references, attachments or usable references, evidence and
  source-ledger references, and "Reference" in PF titles;
- a "report" that means the same file once the pair is defined, or that names no artifact: the verb, the
  preflight's "existing report", the save-recovery rules, a legacy package's report, TW-APPLY-10's optional
  no-change report, and the record prompts' ban on producing a report, which is C3's to change;
- the drains' and TW-APPLY-10's *Purpose*, which name the report and stay true once the pair is defined;
- "session" in naming rules, in the bans on creating or messaging another session, in "originating
  preparer/session" lineage, and where Nathan owns or normally starts the session, none of which a pass
  inside a session he started contradicts;
- the relationship lines that say Nathan invokes the next prompt, read with R6's general rule;
- TW-TRIAGE-10's ban on creating files or changing repositories, since it writes nothing.

**Each member's broad hits, by term:**

| Member | `Drive` | `PFCanon` | `mirror` | `Library` | `download` | `upload` | `reference` | `retriev` | `attach` | `report` | `TW-MGMT-10` | `session` | `initiat` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TW-TRIAGE-10 | 2 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 1 | 5 | 1 |
| TW-DRAIN-10 | 6 | 1 | 3 | 1 | 3 | 1 | 14 | 8 | 2 | 20 | 2 | 10 | 3 |
| TW-DRAIN-20 | 6 | 2 | 3 | 1 | 3 | 1 | 15 | 8 | 2 | 23 | 2 | 11 | 2 |
| TW-RECORD-10 | 4 | 3 | 2 | 1 | 3 | 1 | 11 | 7 | 1 | 8 | 2 | 7 | 2 |
| TW-RECORD-20 | 4 | 2 | 2 | 1 | 3 | 1 | 7 | 7 | 1 | 8 | 2 | 6 | 2 |
| TW-APPLY-10 | 5 | 2 | 2 | 2 | 6 | 1 | 7 | 7 | 3 | 20 | 2 | 9 | 3 |

**Each member's passages:**

| Member | Hits | In passages | Kept as exceptions | Passages in scope |
|---|---|---|---|---|
| TW-TRIAGE-10 | 17 | 6 | 11 | 5 |
| TW-DRAIN-10 | 74 | 32 | 42 | 15 |
| TW-DRAIN-20 | 79 | 33 | 46 | 16 |
| TW-RECORD-10 | 52 | 22 | 30 | 12 |
| TW-RECORD-20 | 46 | 20 | 26 | 10 |
| TW-APPLY-10 | 69 | 36 | 33 | 14 |

**The passages, by member and section.**
- **TW-TRIAGE-10 (5).**
  - *Coded identity*: the line on who initiates invocations (R6); the maintainer line (R5).
  - *Purpose and authority*: the sentence that reads canon "through Google Drive" (R1); the sentence that
    makes Drive sources read-only (R1).
  - *Source identity and routing*, step 1: "repository mirror" among the forbidden substitutes (R1).
- **TW-DRAIN-10 (15).**
  - *Coded identity*: who initiates invocations (R6); the maintainer line (R5).
  - *Authority and sources*:
    - the session-identity sentences, with `TW-PFxx-x` (R6);
    - TW-MGMT-10 as no prerequisite (R5);
    - canon "through Google Drive in `Glow / Core Docs / PFCanon`" (R1);
    - "repository mirror" as a substitute (R1);
    - the read-only line, with the output route and its bans (R1, R3).
  - *Output identity and save recovery*: "a download" (R3).
  - *Intake and source scope*: the input route (R2); PF10 "in the authoritative Drive directory" (R1); "All
    PF authority still comes from current Drive Markdown" (R1).
  - *Completion, outputs and handoff*: the pair (R4); the report's contents (R4, R3); the references in the
    `READY` handoff (R4, R3); the download links and the Drive ban (R3).
- **TW-DRAIN-20 (16).** TW-DRAIN-10's fifteen, word for word, and *PF09 coverage*'s phase file resolved in
  `Glow / Core Docs / PFCanon` (R1).
- **TW-RECORD-10 (12).**
  - *Coded identity*: who initiates (R6); the maintainer line (R5).
  - *Purpose*: the specification taken "directly or through a usable authorized reference" (R2).
  - *Authority and sources*: the session identity (R6); TW-MGMT-10 as no prerequisite (R5); canon through
    Drive (R1); "repository mirror" (R1); the read-only line with the output route (R1, R3).
  - *Output identity*: "a download" (R3).
  - *Destination*: the target and its schema resolved "from Drive" (R1).
  - *Section-only output*: "one downloadable UTF-8 Markdown file" (R3).
  - *PF20 schema*: "in the PFCanon directory" (R1).
- **TW-RECORD-20 (10).** TW-RECORD-10's twelve, less two: its *Purpose* names no input route, and its PF30
  line names no directory.
- **TW-APPLY-10 (14).**
  - *Coded identity*: who initiates (R6); the maintainer line (R5).
  - *Authority and sources*: the session identity (R6); TW-MGMT-10 as no prerequisite (R5); canon through
    Drive (R1); "repository mirror" (R1); the read-only line with the output route (R1, R3).
  - *Output identity*: "a download" (R3).
  - *Intake*:
    - the inputs, "their preparation report" and how Nathan identifies them: attachments, Library or
      legacy ID fields (R2, R4);
    - current PF authority as "Drive" (R1).
  - *Deterministic final document-control header*: "the changed downloadable PF" (R3).
  - *Exact application and preservation*: the pair and the report's contents (R3, R4).
  - *Invalidity, failure and return*: "a downloadable Markdown diagnostic" (R3).
  - *Diagnostic handoff*: the diagnostic attached rather than named by its path (R3).

**Total: 72 passages in the six members**, with each new version's two identity lines on top: 12.

**The rule-change search (`D26-E`), for the plan.** After the edits, `PFCanon`, `upload`, `TW-MGMT-10`
and `TW-PFxx-x` survive nowhere in the new pages. `Drive` and `Library` survive only in the bans R3 keeps,
and `mirror` only in the repository-claims rule. `PLAN` turns this into absence checks by phrase.

### Pages that name TW's current release (A3)

**Method.** Searches with highlights off on:
- `TW-ALPHA-20261004.1`;
- `100426.1`;
- the six member IDs together;
- `TW-MGMT-10 Manage the Glow TW Ecosystem`;
- the six member titles;
- "current TW release selected TW-ALPHA".

Each page found that could name the current release was fetched (a page last edited before 2026-10-04
cannot). *Alpha 1* and the Hub were saved by the harness and read by script.

| Page | Edited | Names TW's current release | Written by the route |
|---|---|---|---|
| *Glow Technical Writing Ecosystem*, the selection page, `3d44590a05eb8171ab6ff4dab33b00ef` | 2026-10-05T00:30:29.861Z | Yes: its status line and `## Selected release — TW-ALPHA-20261004.1`, with the page's one *Current operation* | Yes: the three selection writes |
| *Alpha 1 — Implementation and Validation*, `3d44590a05eb81fe991ff0114cb43029` | 2026-10-04T17:10:29.105Z | Yes: `## Selected release — TW-ALPHA-20261004.1`, with its seven rows | Yes: the current-release note |
| *HDE TW*, `3c74590a05eb8176baf8cb59f1631f3c` | 2026-10-04T17:10:53.751Z | Yes: `## Current TW release — TW-ALPHA-20261004.1`, which names TW-MGMT-10 100426.1 as maintenance owner | Yes: the current-release note |
| *Glow Operations Hub*, `3ce4590a05eb814f8892f88ff8539308` | 2026-10-04T17:11:07.810Z | Yes: `## Current Glow TW release — TW-ALPHA-20261004.1`, on "the exact seven-member catalog" | Yes: the current-release note |
| *GTWPE Target Architecture — Document-Writing Flow* | 2026-10-05T16:16:17.223Z | No: its dated update of 2026-10-05 names TW-ALPHA-20261004.1 as what the model-advice change made | No (N-1) |
| The GTWPE parent page and catalog; GTWPE-MGMT-10's pages | 2026-10-05 | No: they name TW-ALPHA, but no release | No: X4 writes only the catalog's checked-through commit |
| The TypeSafe usage-log row *GTWPE W1 — first TW repair* | 2026-10-05 | Only as a dated log entry | No |
| Older pages, such as *Glow TW Alpha Implementation Handoff 090726.1*, earlier member versions and GCFPE pages | Before 2026-10-04 | No | No |

**Coverage.** This is the set the record of TW's latest selection wrote: in its *The control texts*, the
selection section on the selection page and *Alpha 1*, and a note on *HDE TW* and on the Hub. Each
member's own text names the selection page as holding its selection.

**Stale text.** C2 makes two notes stale:
- *HDE TW*'s names TW-MGMT-10 100426.1 as maintenance owner;
- the Hub's speaks of "the exact seven-member catalog".

The route replaces neither. It puts each new note above the old one and makes the old heading historical.

### Contradictions and risks

1. **The TW Flowmaster skill (Q-1).**
   - **What it does.** Installed `tw-flowmaster` 1.3.0 has a *Selected-catalog TW profile*. It applies when
     the selected drain and apply prompts carry the exact no-redlines contract, which the new versions still
     do. The profile drives each document through separate sessions, reads the Source Blob and results from
     Drive, and keeps its ledger there (*Source and action lanes*). It also checks a `READY` package and an
     Apply result as saved report pairs.
   - **What would happen.** Against the new release, a Flowmaster run would hand the prompts no output path
     and no repository inputs. Each would stop at its missing-input rule. That is a loud failure, not a
     silent one, provided `PLAN` keeps that rule.
   - **Canon.** HDE Governance §9.1.6: "An edited subgroup is not ready while an affected counterpart
     remains incompatible."
2. **The route assumes eight members (F-1).** *How each kind of target changes* has the new section list
   "the eight members with only the changed rows new". The new release has six members, all new. The plan
   adapts the text, as the last TW change did with seven.
3. **TW-MGMT-10's page stays runnable.** Unselected, its text still makes it the sole TW maintenance owner.
   The route never edits an existing TW-ALPHA page, as with TW-ASSESS-10. The selection page and the three
   notes say that GTWPE-MGMT-10 maintains the TW prompts.
4. **No executable check exists for TW.** The tier 2 gate is static, and no live TW trial has run since
   2026-09-08. The selection page already records runtime behaviour as unproven. C2 changes where every
   step reads and writes, so its first live run is untried.
5. **Where a proof log sits.**
   - The request puts each proof log beside its artifact.
   - C1 §A A.4 sketched the Flow Manager's drafts folder as holding only the replacement documents, with
     the proof logs under `passes/<target>/`.
   - C2 follows the request. C4 settles its own layout with it.
6. **The readbacks are heavy.** Six whole pages are read back by this session, and four control pages. A
   compaction during `EXECUTE` is likely. The body's rule covers it: fetch live again, and never recover a
   body from a transcript.
7. **One reader of the bodies.** The scope rests on this session's reading. No worker can check it, since
   workers do not fetch bodies (`D22`). `PLAN`'s dry run reads the bodies again.
8. **The phrase check sees phrases, not meaning** (`D14`'s note). Carrying GTWPE-D1's eight items in
   Nathan's own words lets the readback find each by phrase. The reviews read for behaviour.
9. **Excerpts (Q-2).** The plan's anchors are short passages of the bodies.

### Defect classes matched (`ecosystem-change-management.md` §4)

- `SCOPE-001`: the scope above is measured by broad match minus exceptions, by reading.
- `GUARD-001`: GTWPE-D1 lands in the three TW prompts that write its artifacts, with its guard:
  GTWPE-MGMT-10's prompt route checks it by phrase on each new page.
- `DERIV-001`: the report and the proof log become one file. The four release pages restate the selection
  by hand.
- `FUNC-001`: `tw-flowmaster` would run the old Drive route by function (Q-1).
- `NAME-001`: TW-APPLY-10's application report is bound by what it accompanies, a final PF, not by its name.

### Findings against GTWPE-MGMT-10 100526.2

- **F-1:** its selection route is worded for eight members (risk 2). It was first recorded by
  MODIFICATION-20260930-gtwpe-tw-model-advice, which adapted it the same way.

### Candidates for separate Modifications (recorded, not taken)

- **F-1**, in a later GTWPE-MGMT-10 repair. It could go with E-033, which the request keeps for C6.
- **N-1.** The architecture page's dated update of 2026-10-05 calls TW-ALPHA-20261004.1 the release the
  model-advice change made "now". It stays true as a dated note. A current wording is the facilitator's, as
  E-032's page fixes were.
- **N-2.** *Alpha 1* still carries a `### Current operation` heading under its historical TW-ALPHA-20260908.1
  release. E-029's fix renamed that heading only on the selection page. Outside the current TW section, it
  is not the route's to write: the facilitator's.
- **For C4:** the layout of the run directory against the request's proof log beside each artifact (risk 5).

### Open questions for the Product Owner

**Q-1. The TW Flowmaster skill (risk 1).**
- **(a) Select the new release in this Modification.** The selection page and the three notes say that
  `tw-flowmaster` 1.3.0 and `flowmaster-validate` 3.3.2 do not run it. TW runs by Nathan's direct
  invocations until the Flow Manager (C4), and C6 retires the skill, as the approved order has it. This
  waives HDE Governance §9.1.6's readiness rule for the skill, which is Nathan's to do.
- **(b) Update `tw-flowmaster`, with any `flowmaster-validate` assertion that pins its wording, in this
  Modification.** It goes through the skill route, and the new release is selected only after Nathan
  installs it, as the last TW change did. That adds a skill part, a skill review cycle and an install, for a
  skill C6 retires.
- **Recommendation: (a).**
  - The approved order already replaces the skill with the Flow Manager (C4) and retires it (C6), so
    updating it now is work C6 throws away.
  - The manual flow is how TW runs.
  - A Flowmaster run against the new release stops loudly; it does not produce a wrong result.

**Q-2. Excerpts in the repository (risk 9).**
- **The two texts.** The request's item 1: "No TW prompt body, copy or excerpt enters the repository."
  GTWPE-MGMT-10 100526.2, *Reading prompt bodies*: "No body enters it, and no passage longer than an edit's
  shortest unique anchor, or, before `PLAN` sets the anchors, than the clause at issue."
- **The practice.** `PLAN` gives each edit as its shortest unique anchor and its new text, in a committed
  `edits.json`, as every earlier TW change has. The last one, MODIFICATION-20260930-gtwpe-tw-model-advice,
  committed 69 edits: 51 located by an anchor and 18 by the two ends of a span. An anchor is a short excerpt
  of a body.
- **(a) Read item 1 as 100526.2 does:** no body, no copy, and no excerpt longer than an edit's shortest
  unique anchor (in `ANALYZE`, the clause at issue). `PLAN`'s checker holds each anchor to that limit.
- **(b) Read it literally:** no anchor is committed. The exact edits would then exist only in one session's
  context. No reviewer could check them, and no fresh session could resume from the record (`D26-C`). This
  analysis has designed no other way to give `PLAN` its edits.
- **Recommendation: (a).** It keeps every body in Notion, which Nathan's words ask for. It also keeps the
  plan reviewable and resumable.

### Readiness and interaction cost

`NEEDS_RULING`, for Q-1 and Q-2. It is advice, not a refusal. No item waits on another item's execution,
and every item's scope is measured.

    interaction_cost = 2 open rulings + 2 + 3 review rounds + 0 skill review cycles + 0 installs + 1 merge = 8

- **Review rounds:** this mode's dry run; `PLAN`'s dry run; and one full review by a single reviewer. A
  second reviewer or a diff check comes only if that review finds a required defect, by the request's
  standing direction.
- **Q-1's option (b)** would add a skill review cycle and an install, making 10.
- **The merge** is the record's pull request, amthorn78/glow-hdengine-v2#575. It is not to be merged before
  the record is `COMPLETE`. No repository file other than the record and its evidence changes, so X2 waits
  for no merge.
- **Splitting saves nothing.** The six versions and the release land as one selection. Splitting one rule
  across runs is what `ecosystem-change-management.md` §1 warns against.

The estimate is in the front matter. Time is the meter, and twice the estimate is where the session stops.

### Dry run (A6)

By this session, read-only, before any return to Nathan. No full review: as in each earlier GTWPE
Modification, `ANALYZE` runs a dry run only, and `PLAN` carries the full review.

| # | Gate | Result |
|---|---|---|
| D1 | `gtwpe_record_check.py` and `modification_validate.py` on a scratch copy of this record at `ANALYZED`, with this round in `reviews` | Both exit 0, 1/1 |
| D2 | Both selftests, from this branch at `20d0dd8`'s files | `gtwpe_record_check.py --selftest` 17/17; `modification_validate.py --selftest` 66/66 |
| D3 | The front matter parses (PyYAML), and its request equals PE39's message; every table in the record has one column count in every row, by script | Parses; the request is verbatim; 7 tables, each consistent |
| D4 | A0 reproduced: `git fetch origin main`; `origin/main`; `git log 31deec4..origin/main` over *The watched sources* | Still `20d0dd8`; no commit |
| D5 | The new versions' titles and the new release label are free | *HDE TW* (edited 2026-10-04T17:10:53.751Z) lists no TW member version after 100426.1, and the selection page names no release after TW-ALPHA-20261004.1 |
| D6 | The scope counts, by a second reading of the six fetches, made before this row | It corrected TW-DRAIN-20's `reference` count from 14 to 15 (its *PF09 coverage*, item 5). It also added `PFCanon` to the broad terms, which found two lines that say "PFCanon" but not "Drive": TW-DRAIN-20's PF09 phase file and TW-RECORD-10's PF20 line. Both are counted above. Every other count was confirmed. No command counted over a body |
| D7 | The record tools need no change for this Modification | By reading at `20d0dd8`: `TARGETS` holds `prompt` and `notion_control`, and the record check needs only the subsections this record has |

No required defect.

### Harness files (`D22` condition 5)

- **Inline fetches, held only in this session's transcript**, which the harness keeps and leaves to its
  teardown:
  - GTWPE-MGMT-10 100526.2, twice: at the mode's start and after the compaction.
  - The seven TW bodies at 100426.1 before the compaction, and the six that change again after it.
  - GCFPE-MGMT-10's proposed body and `091426.1`, fetched at A0 for their edit times.
  - The control pages: the GTWPE parent page, the selection page (twice), *HDE TW* and the architecture
    page.
- **Harness saves, each read by a script that printed only what the check needed:**
  - the PE Metaprompt `091426.1` fetch, `mcp-Notion-notion-fetch-1791229658527.txt`: its title, edit time
    and path;
  - the register, `mcp-Notion-notion-fetch-1791229659479.txt`: its edit time and the two rows of *Current
    selection* that name GCFPE-MGMT-10 and the PE Metaprompt;
  - *Alpha 1*, `toolu_01XJCM3rNWLKfzM1oF7aWKTG.json`, and the Operations Hub,
    `mcp-Notion-notion-fetch-1791229909775.txt`, both control pages: each one's edit time, headings, term
    counts and current TW release section.

  Earlier in this session the harness refused `rm` on its tool-results directory ("Session Transcript
  Tampering"), as `D22`'s refinement of 2026-09-23 foresees. So each save is left to its teardown and not
  read again. So is the PE Metaprompt save from C1's `EXECUTE`, `mcp-Notion-notion-fetch-1791218129501.txt`,
  which this mode did not read. No save was hashed or compared as a body's identity.
- **The session transcript.** After the compaction, `A1`'s verbatim copy of the request needed PE39's
  message, which only the transcript held. A script read it once and printed only the user's typed
  messages that held the request's opening words, never a tool result. The request was saved from it to
  `c2_request.txt` in the scratchpad.
- **Scratch files**, in this session's scratchpad: a copy of PF04 from `main` (canon, not a prompt body);
  the scripts `user_request.py`, `save_meta.py` and `ctl_section.py`; and a scratch copy of this record for
  the dry run.

### Canon and rulings relied on

- **`AGENTS.md`:** the canon-first rule; canon is read-only; the CI-exempt paths; the pull request's
  headings.
- **HDE Build Notes (PF10):**
  - 2.29 PF10-CANON-001: canon in `docs/pfcanon/` on `main`; change-process documents, redlines and
    reports among them, stored in `docs/ephemeral/`; ChatGPT Library and Drive neither destinations nor
    authorities; GCFPE prompt bodies single-homed in Notion. Used for ITEM-01 to ITEM-03.
  - 2.38 PF10-AINEUTRAL-001: no governance requirement for a provider, product, model or effort level;
    this session's Notion reads.
- **HDE Governance (PF04):**
  - §9.1.3: the prohibition on Drive persistence, which stands; final results identify the actual saved
    file. Its human-advice rule for a downstream session is left to Nathan by 2.38, and he settled it for
    the TW prompts (MODIFICATION-20260930-gtwpe-tw-model-advice, E-F2), so no TW prompt carries model
    advice.
  - §9.1.6: every other member's disposition; reconciling interacting skills (Q-1); readback; author,
    checker and acceptor at X5; reusable bodies single-homed in Notion.
- **Rulings:**
  - GTWPE-D1 (ITEM-04).
  - In `gcfpe.decision-record.md`: `D7`; `D14`'s note of 2026-09-23; `D22`, read in this mode, with its
    refinement; and `D21` and `D26` as GTWPE-MGMT-10 100526.2 states them.
  - Nathan's approved order, C1 §A A.5, approved 2026-10-05, and his words that writing prompts do not
    belong in the repository, as the request quotes them. His direction of 2026-09-29 that no TW prompt
    carries model advice. No TypeSafe scoring.
- **`ecosystem-change-management.md`:** §1, one rule applied wherever it reaches; §2, class B and
  converging on existing wording.
- **GTWPE-MGMT-10 100526.2**, as fetched at the start of this mode: *Entry contract*, *The spine*, `MODE =
  ANALYZE`, *How each kind of target changes*, *The watched sources* and *Relation to the PE Metaprompt*.

**This mode's own cost.** Time: from 2026-10-05T19:39:01Z to A7 at about 2026-10-05T20:09Z, about 30
minutes by the session's clock. Tokens: not measured by this session.
