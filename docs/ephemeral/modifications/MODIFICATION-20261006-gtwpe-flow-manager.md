---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261006-gtwpe-flow-manager
status: PLANNING
targets: [prompt, rule, notion_control]
gate_tier: 1
closure:
  upstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20]
  downstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20]
  state_sharers: []
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 7
interaction_cost_actual:
estimate:
  plan: "about 5 h: the Flow Manager's complete body drafted through the PE Metaprompt from this analysis, as a temporary local draft, with the PE's PF03, PF06 and PF10 compatibility check; the handoff table; the catalog texts; §P's steps, readback phrases and the two-sided check of every pass invocation against the TW bodies; a dry run; and one full review by a single reviewer, who reads the draft. Time is the meter the session can read; tokens are not measured"
  execute: "about 2 h, not counting the wait for Nathan's merge: the new page (duplicate, title, the body) read back whole by this session; the handoff table committed and its merge detected on main (X2, X3); the catalog's row, note, design entry and checked-through commit, read back; the record. Time is the meter"
item_count_at_approval: 9
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-10-06
    required_open: 0
    outcome: "By this session, read-only: both record checks exit 0 on a scratch copy at ANALYZED; the front matter and every table parse, and the request is verbatim; A0 reproduces at ad1615d; the new title is free under the GTWPE parent page; a second, independent reading of a second fetch of GTWPE-MGMT-10 100526.2 and of the catalog confirmed every count; every quotation from a repository file or an installed skill found by grep; the record tools need no change. No required defect. No full review"
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-10-06
    required_open: 0
    outcome: "By this session, read-only, before any full review: both record checks exit 0 on a scratch copy at PLANNED; the front matter parses, and the approval and the request are verbatim; A0 reproduces at 601b330; every live edit time unchanged; the two-sided check of every pass invocation against the five TW bodies read live passes; the catalog's four old texts once each; the new title free; the draft's structure, phrases and absences as planned, by script; the handoff table's carried rows identical to design §6; the PF03, PF06 and PF10 check compatible. No required defect"
  - mode: PLAN
    kind: FULL
    date: 2026-10-06
    required_open: 4
    outcome: "One reviewer, GTWPE-FLOW-MANAGER-PLAN-A, as Nathan directed, on 43150c6 and the draft read in place: 2 required findings, R-1 (a PF10 change the run holds back can still reach a pass, unseen) and R-2 (a session that stops names no harness file that holds a prompt body), and 22 listed. The session confirmed both, and confirmed two listed findings as required under R1: L5 (a run with no draft returns RUN_REVIEW_READY) and L16 (X1.4's search matches nothing as written). All four repaired; a check of the repair's diff follows"
items:
  - id: ITEM-01
    statement: "The Flow Manager, a new prompt GTWPE-FLOW-10 — Run the Technical Writing Flow, that Nathan starts in a new standalone session with an execution prompt and its inputs, and that runs the whole writing flow, itself or through the subagents it judges useful: execution-time triage of the complete supplied context; the run's branch, its one pull request and working copies from docs/pfcanon/ on main; each affected document's passes through the selected TW prompts with Nathan's redlining discipline; the document-control check across the drafts; the cross-document consistency check, whose fixes are new redline-and-apply cycles; the completion standard; and a review-ready pull request. It never merges and never writes docs/pfcanon/."
    source: "Request item 1; MODIFICATION-20261005-gtwpe-writing-side §A A.2, A.4 (R1, R3, R4, R9, R12 to R15) and A.5's C4 row; target architecture §§1 to 3, 10 and 11, and Nathan's answers 2 and 3"
    disposition: ""
  - id: ITEM-02
    statement: "The run's layout: docs/ephemeral/gtwpe.runs/<run-id>/ with its drafts folder and RUN.md, on the run's own branch, settled against the proof log each TW prompt writes beside its artifact."
    source: "Request item 2; MODIFICATION-20261005-gtwpe-writing-side §A A.4; MODIFICATION-20261005-gtwpe-tw-repository-io §A risk 5 and §P K-8"
    disposition: ""
  - id: ITEM-03
    statement: "Stop and resume: the clean boundaries, the stop signals S1 to S6, RUN.md, and resume by RESUME <run-id>, with S1 sizing each pass, PF20 included, and with a run resumed on a later day never tripping TW-APPLY-10's check of a change-history entry its drain dated earlier."
    source: "Request item 3; MODIFICATION-20261005-gtwpe-writing-side §A R18 and *The stop, designed*; MODIFICATION-20261006-gtwpe-tw-document-rules §P K-4 and K-10; Nathan's direction of 2026-09-29 on stopping"
    disposition: ""
  - id: ITEM-04
    statement: "The Flow Manager's input: the execution prompt's contract, which Nathan writes by hand until C5's Change Manager produces it, and which no execution prompt can use to override GTWPE-D1, the stop rule or canon's read-only status."
    source: "Request item 4; MODIFICATION-20261005-gtwpe-writing-side §A A.5's C5 row, A.8 and R12; Nathan's answers 2 and 5"
    disposition: ""
  - id: ITEM-05
    statement: "Eligibility and routing: the canon PF documents and PF03, with PF09, PF20 and PF30 routed to their own prompts; PF10 a source only; PF27 changed only when a specification exists."
    source: "Request item 5; MODIFICATION-20261005-gtwpe-writing-side §A R10 and R11; Nathan's rulings of 2026-09-28 (design v1.2 §8.7) and his instruction of 2026-09-25 (plan v1.2 §1); ledger E-020"
    disposition: ""
  - id: ITEM-06
    statement: "GTWPE-D1 in a run: the Flow Manager writes neither artifact itself, every artifact in a run comes from a pass with its own proof log, and a run with an artifact and no proof log is not complete."
    source: "Request item 6; GTWPE-D1 (docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md); MODIFICATION-20261005-gtwpe-writing-side §A A.8 and S5"
    disposition: ""
  - id: ITEM-07
    statement: "The ledger items carried to C4: E-006, what a subagent may write, checked after each pass; E-016, harness files disclosed in the run report; and E-022, the Flow Manager's reads of TW prompt bodies, under D22."
    source: "Request item 7; MODIFICATION-20261005-gtwpe-writing-side §A A.6; ledger E-006, E-016 and E-022"
    disposition: ""
  - id: ITEM-08
    statement: "The Flow Manager's handoffs are recorded in docs/prompt_ecosystem_management/gtwpe/, as the GTWPE handoff table GTWPE-MGMT-10 reads for closure."
    source: "Request item 8, first half; MODIFICATION-20261005-gtwpe-writing-side §A A.5's C4 row; GTWPE-MGMT-10 100526.2, *Read these* and the record's closure row"
    disposition: ""
  - id: ITEM-09
    statement: "GTWPE-MGMT-10 can maintain the new prompt from the moment it lands, before C6 has the catalog select every member."
    source: "Request item 8, second half; MODIFICATION-20261005-gtwpe-writing-side §A A.5's C4 and C6 rows; the GTWPE catalog's members note"
    disposition: ""
parts:
  - id: PART-01
    name: "GTWPE-FLOW-10: its first page, its handoff table and its catalog row"
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06, ITEM-07, ITEM-08, ITEM-09]
    class: B
    after: []
request: |
  PE39 here, facilitator, on 2026-10-06.

  Where things stand, checked by PE39 today:
  - C3 is COMPLETE on main (amthorn78/glow-hdengine-v2#580, merged at `ad1615d`). TW-ALPHA-20261006.2 is selected: TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10 at 100626.2, and TW-TRIAGE-10 at 100626.1. They read PF canon from `docs/pfcanon/` on `main`, write at the repository path each invocation names under `docs/ephemeral/`, write a GTWPE-D1 proof log beside each artifact, bring every document-control field forward (the Last Update Gate in Nathan's form), and never merge. PE39 accepted C3 against main, both record checks (7/7), and the new pages and control pages, read live.
  - main is at `ad1615d`. Since the GTWPE catalog's checked-through commit `b1bd769`, main gained amthorn78/glow-hdengine-v2#579 (the error ledger and the target architecture record, under `docs/ephemeral/gtwpe.rewrite/`) and amthorn78/glow-hdengine-v2#580 (C3's record and evidence, under `docs/ephemeral/modifications/`). Nothing under `docs/pfcanon/` has changed since `31deec4`.

  Next: run C4, the fourth change in the order Nathan approved in MODIFICATION-20261005-gtwpe-writing-side (§A A.5), through GTWPE-MGMT-10 — Manage the GTWPE — 100526.2 (Notion page `3f04590a05eb8128b8c8ff3650ab2d5a`): ANALYZE, PLAN, EXECUTE. Follow the published body live and stop at each of Nathan's approvals.

  What C4 is (that record's §A A.2, A.4 with its drafts location, R1, R3, R4, R9 to R18 and *The stop, designed*, A.5's C4 and C5 rows, A.6 and A.8; the target architecture record, whole, with Nathan's answers 1 to 8 and his directions of 2026-09-29):
  1. The Flow Manager: a new prompt, proposed in §A A.2 as GTWPE-FLOW-10 — Run the Technical Writing Flow. Nathan starts it in a new standalone session with an execution prompt and its inputs, as attached files or repository paths (answer 2). It runs the whole flow in that session, itself or through the subagents it judges useful (answer 3): execution-time triage of the complete supplied context (architecture sections 2 and 7, R9); the run's branch, its one pull request and working copies from `docs/pfcanon/` on `main`; each affected document's passes through the selected TW prompts, with Nathan's redlining discipline (TW-DRAIN-10 or TW-DRAIN-20, then TW-APPLY-10; TW-RECORD-10 or TW-RECORD-20 for PF20 and PF30); the document-control check across the drafts (R4); the cross-document consistency check, whose fixes are new redline-and-apply cycles (R13); the completion standard (architecture section 10, R14); and a review-ready pull request. It never merges and never writes `docs/pfcanon/` (R12).
  2. The run's layout: `docs/ephemeral/gtwpe.runs/<run-id>/` with its drafts folder and `RUN.md`, on the run's own branch, as §A A.4 sketched it, settled against the proof log each TW prompt now writes beside its artifact (C2's risk 5; C3's K-8).
  3. Stop and resume (R18; §A *The stop, designed*): the clean boundaries, the stop signals S1 to S6, `RUN.md`, and resume by `RESUME <run-id>`. S1 sizes each pass, PF20 included (952,515 bytes; C3's K-10). A run resumed on a later day must not trip TW-APPLY-10's check of a change-history entry its drain dated earlier (C3's K-4).
  4. Its input: the execution prompt's contract, which Nathan writes by hand until C5's Change Manager produces it (A.5's C5 row). No execution prompt overrides GTWPE-D1, the stop rule or canon's read-only status (A.8; R12).
  5. Eligibility and routing (R10, R11): the canon PF documents and PF03, with PF09, PF20 and PF30 routed to their own prompts; PF10 a source only; PF27 changed only when a specification exists (ledger E-020, with C5).
  6. GTWPE-D1 (§A A.8): the Flow Manager writes neither artifact itself. Every artifact in a run comes from a pass with its own proof log, and a run with an artifact and no proof log is not complete (S5). GTWPE-MGMT-10 100526.2's GTWPE-D1 guard applies.
  7. The ledger items §A A.6 carries to C4: E-006 (what a subagent may write, checked after each pass), E-016 (harness files disclosed in the run report) and E-022 (the Flow Manager's reads of TW prompt bodies, under D22).
  8. Its handoffs recorded in `docs/prompt_ecosystem_management/gtwpe/` for GTWPE-MGMT-10's closure (A.5's C4 row), and, as the analysis finds, how GTWPE-MGMT-10 maintains the new prompt before C6 has the catalog select every member. After C4, Nathan can run a first live trial with a hand-written execution prompt (A.5).

  Not in C4: the Change Manager (C5); adoption (C6), including the retirement of tw-flowmaster, which stays as installed until then; E-033, which stays for C6; F-1 and E-035's count-by-script candidate, for a later GTWPE-MGMT-10 repair; E-010, which stays Nathan's; a PF20 volume rule, until Nathan splits PF20; and any change to the TW prompts. If the analysis finds a TW prompt must change for the Flow Manager to run it, raise that with Nathan rather than take it.

  Standing directions:
  - Nathan: "this flow can be simplified, let's not overcomplicate this".
  - Stop rather than produce substandard results.
  - Keep PLAN lean: one dry run and one full review by a single reviewer; a second reviewer or a diff check only if that review finds a required defect.
  - Counts over a prompt body: by script over a harness save where one exists (D22 lets a script print only a count), otherwise by two independent readings (ledger E-035).
  - No Modification branch is merged before its record is COMPLETE, except the pull requests the plan itself opens.
  - No GTWPE prompt carries model, effort or strength advice (R16).
  - No TypeSafe scoring in this work.
  - Report to Nathan in at most five plain sentences, in plain language, ending with exactly what he must approve or decide.
requested_by: Nathan
analyze_approved_by: "Nathan, 2026-10-06: \"Nathan approves the analysis of MODIFICATION-20261006-gtwpe-flow-manager at 772ccfb (2026-10-06). PE39 checked it: main's modification_validate.py and gtwpe_record_check.py each pass all eight GTWPE records (8/8), the request in the front matter equals PE39's message, main is still ad1615d, and the branch changes only the record. Nathan approves the three choices the analysis records: no document is copied ahead of its pass; GTWPE-FLOW-10's body is drafted and reviewed in the session that runs PLAN and is never stored in the repository, PLAN and EXECUTE run in that same session, and Nathan and PE39 read the published page live before the first trial; and the new page is created by duplicating a child page of the GTWPE parent page, retitling it and replacing its content (F-2). Risk 15 is PE39's citation error, logged as ledger E-040: the finding is C2's K-8, not C3's. Continue to PLAN: one dry run and one full review by a single reviewer, who reads the draft body, and a second reviewer or a diff check only if that review finds a required defect. Stop at Nathan's plan approval, and report in at most five plain sentences ending with exactly what he must approve.\""
analyze_approved_date: 2026-10-06
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20261006-gtwpe-flow-manager

C4 of the writing-side build: the Flow Manager, a new GTWPE prompt that runs the whole technical-writing
flow in one session Nathan starts and leaves a review-ready pull request of complete replacement PF
documents, each with its proof log; its handoffs recorded for GTWPE-MGMT-10; and its row in the GTWPE
catalog.

## Intake

Not through triage. The request came from PE39 on 2026-10-06 and is copied verbatim in the front matter.
It runs C4, the fourth change in the order Nathan approved in MODIFICATION-20261005-gtwpe-writing-side
(§A A.5), through GTWPE-MGMT-10 100526.2. Its eight numbered points, under "What C4 is", are ITEM-01 to
ITEM-09 in its order; its point 8 has two halves, ITEM-08 and ITEM-09. What it puts outside C4 is recorded
in §A, not taken here.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
100526.2*, fetched live at the start of the mode: edited 2026-10-05T16:36:11.384Z, the version the catalog
selects. The mode started at 2026-10-06T17:23:53Z, when PE39's request arrived, with `main` at `ad1615d`.
The request is in the front matter, verbatim. The record is on
`docs/20261006-modification-gtwpe-flow-manager`, the Modification's own branch, with its open pull request
amthorn78/glow-hdengine-v2#581. The session's harness had named another branch; nothing was pushed there,
since the next mode finds a record only on a `docs/*-modification-gtwpe-*` branch.

### Consult

- **Repository**, on `main` at `ad1615d`.
  - C1's record, MODIFICATION-20261005-gtwpe-writing-side: §A whole, above all A.1, A.2, A.4 with *The stop,
    designed*, A.5, A.6 and A.8, and its two approvals.
  - C2's record: §A *The change, settled* and *How the TW flow runs*, risk 5, and §P's K-8. C3's record: §A
    whole, and §P's open findings, K-4 and K-10 among them, and §E's readback times.
  - The target architecture record, whole: the architecture, Nathan's answers 1 to 8, his directions of
    2026-09-29 and 2026-10-05, and the updates of 2026-10-05 and 2026-10-06.
  - The error ledger, whole; the GTWPE decision record (GTWPE-D1); design v1.2 §§5, 6, 7, 8.4 to 8.7, 10, 11
    and 12; implementation plan v1.2 §1; `CHECKPOINT.md` §12.1 and §12.2, on how GTWPE-MGMT-10's own first
    page was published.
  - In `docs/prompt_ecosystem_management/`: `modification-template.md` 2.1, `ecosystem-change-management.md`,
    `execution-and-delegation-model.md`, `notion-write-boundary.md`, `prompt-body-content-policy.md` and
    `prompt-corpus-policy.md`, whole; in `gcfpe.decision-record.md`, `D21`, `D22`, `D23`'s clarification on
    subagents, `D24` and `D26`, whole; the header of `gtwpe/gtwpe_record_check.py`, and
    `modification_validate.py`'s target list.
  - `AGENTS.md` and `.github/pull_request_template.md`, and amthorn78/glow-hdengine-v2#580's description, for
    a pull request's form.
  - No `docs/*-modification-gtwpe-*` branch carries this ID (`git ls-remote`), so it is new.
- **Canon**, on `main` at `ad1615d`, unchanged since `31deec4` (`git log 31deec4..origin/main --
  docs/pfcanon/` is empty). Searched with `git grep` for the task's terms (`prompt ecosystem`,
  `downstream-session`, `subagent`, `pull request`, `drain`, `Last Update Gate`, `lowercase`) and read in
  full where it governs: *Canon and rulings relied on*, at the end of this section, says what each is used
  for.
- **Notion, read-only.** GTWPE-MGMT-10 100526.2; the GTWPE parent page and its catalog; the *Glow Technical
  Writing Ecosystem* page; *HDE TW*, *Alpha 1* and the Operations Hub; the architecture page; the six
  selected TW prompts (*The members, read live*); the PE Metaprompt 091426.1, for its general rules on
  creating a prompt; and the lineage sources (A0).
- **Installed skills**, read for this task: `glow-write-boundary`, `glow-workspace-currency` and
  `glow-artifact-storage`.

### Drift check (A0)

`git fetch origin main`; the commit examined is `ad1615d4a0ee8ab458084edf7aed7792932e5c68` (`ad1615d`),
#580's merge.

**(a) The lineage sources.** Searches with highlights off on `PE Metaprompt` and `GCFPE-MGMT-10` found no
page that the catalog does not record and that is newer than its record. The other PE Metaprompt hits are
archived predecessors dated 2026-09-12 and 2026-09-13; the other GCFPE-MGMT-10 hits are the archived
`091326.1` and `091326.2` and control or tracking pages. Each recorded page was fetched for its exact edit
time. The PE Metaprompt's fetch and the register's were saved by the harness and read by script (*Harness
files*).

| Source | Recorded in the catalog | Found, by fetch | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1`, 2026-09-24T15:38 | 11:00:24.691Z; `091426.1` (`3db4590a05eb81d1bb64ebcb3ca8eb54`) at 15:38:34.295Z; the register selects it | None |
| PE Metaprompt | Pinned and selected: `091426.1`, 2026-09-23T17:17:22.217Z | 17:17:22.217Z; the register selects it (`3db4590a05eb8174be35d9e35acb3f77`) | None |

The register page was at 2026-09-23T17:43:39.489Z, the edit time the catalog records.

**(b) The watched paths.** `git log b1bd769..ad1615d` over *The watched sources* lists nothing. The range
holds two commits, amthorn78/glow-hdengine-v2#579 and amthorn78/glow-hdengine-v2#580, which change twelve
files, all under `docs/ephemeral/`, as PE39's request says.

No trigger finding. X4 re-pins nothing and moves the checked-through commit to the commit it examines.

### The members, read live

Each TW member was fetched whole into this session's context and read whole. Each edit time equals the time
C3's or C2's `EXECUTE` recorded at its readback, so no member has changed since its selection. The selection
page (edited 2026-10-06T16:54:30.403Z) selects TW-ALPHA-20261006.2 with these six.

| Member | Version, page | Edited |
|---|---|---|
| TW-TRIAGE-10 — Identify PF10 Drain Targets | 100626.1, `3f14590a05eb81789e16d978795db77d` | 2026-10-06T03:18:14.556Z |
| TW-DRAIN-10 — Prepare PF Document Redlines | 100626.2, `3f14590a05eb819f8390f5b92fc4c8ab` | 2026-10-06T16:39:55.231Z |
| TW-DRAIN-20 — Prepare PF09 Redlines | 100626.2, `3f14590a05eb81a58043d304b7452801` | 2026-10-06T16:45:43.111Z |
| TW-RECORD-10 — Create Epic History Section | 100626.2, `3f14590a05eb81d399a7c3ab1fd6fb66` | 2026-10-06T16:47:37.162Z |
| TW-RECORD-20 — Create CRD History Section | 100626.2, `3f14590a05eb81eaaf0cedac0de274b9` | 2026-10-06T16:49:11.220Z |
| TW-APPLY-10 — Apply Validated Redlines | 100626.2, `3f14590a05eb81daa3cfee9956585cd5` | 2026-10-06T16:50:52.240Z |

The GTWPE parent page and catalog were at 2026-10-06T16:53:37.871Z, C3's X4: GTWPE-MGMT-10 100526.2 is the
catalog's one member, and its checked-through commit is `b1bd769`.

### The Flow Manager, settled

The request's eight points, as ITEM-01 to ITEM-09. Nathan's target architecture and C1's approved §A frame
them. Where this section changes a detail that C1's §A sketched, it says so and why. `PLAN` writes the body.

**What it is.** One new GTWPE prompt, *GTWPE-FLOW-10 — Run the Technical Writing Flow* (C1 §A A.2), a child
page of the GTWPE parent page, maintained by GTWPE-MGMT-10. Nathan starts it in a new standalone session with
an execution prompt and its inputs (answer 2). It runs the flow to a review-ready pull request in that
session, itself or through the subagents it judges useful (answer 3). It is a runtime role, never
GTWPE-MGMT-10's (C1 §A A.7), and it hands off to no prompt: every result returns to Nathan. It creates no
session, and it carries no model, surface or effort advice (R16).

#### ITEM-01. The flow

| Boundary | What is done (architecture §3, its steps) | By |
|---|---|---|
| **B1 Scope** | Read every input completely; reconfirm the requested change; decide which eligible documents it affects (1 to 3). Create the run's branch from `origin/main`; write `RUN.md`, and any input supplied as an attached file, in the run directory; commit, push and open the run's one pull request (4, 5) | The Flow Manager |
| **B2 Redlines** | For each document routed to a drain: its redlines file and proof log, the exact `no redlines`, or `BLOCKED` (7) | TW-DRAIN-10 or TW-DRAIN-20, as a pass |
| **B3 Drafts** | For each `READY` package: the complete revised document in the drafts folder with its proof log, or a diagnostic returned to its drain. For a PF20 or PF30 record: the updated document with its proof log (6 to 8) | TW-APPLY-10; TW-RECORD-10 or TW-RECORD-20 |
| **B4 Control** | Every draft's document-control fields checked across the run (9) | The Flow Manager |
| **B5 Consistency** | The cross-document consistency review; each fix a new redline-and-apply cycle (10) | A fresh reviewer subagent, then passes |
| **B6 Complete** | The completion standard for every document (architecture §10), and the pull request made review-ready (11) | The Flow Manager |

C1's §A sketched seven boundaries. B1 and B2 there, scope and then the branch with copied drafts, are one
boundary here: the scope can be recorded only on the branch, and the copies are made by the passes (below).

- **Triage (architecture §§2, 3 and 7; R9).** The Flow Manager reads the complete supplied context, every
  input in full, and makes its own execution-time triage rather than assume that every supplied document
  changes (architecture §2). For each eligible document it decides, by reading the document's ownership and
  the passages the change bears on, whether the change may affect it; a search hit or matching heading is not
  enough, as TW-TRIAGE-10 already words it. A document named in the execution prompt is checked, not
  assumed. When unsure, it routes the document: a drain's verified `no redlines` is the authoritative "not
  affected". Every decision and its reason go into `RUN.md`. For a PF10 source it applies the Change Process
  Guide §3.5.2.8 drain ordering, as design v1.2 §10.5 set it: a PF10 change whose epic's QA tasks PF10 does
  not record as complete is listed in `RUN.md` and the pull request, not drafted, unless the execution prompt
  carries Nathan's direction to draft it. It does not run TW-TRIAGE-10 (*Member dispositions*). When no
  eligible document is affected, the run ends at B1, with its record in the pull request.
- **The branch, the pull request and the working copies.** The run's branch is
  `docs/<yyyymmdd>-gtwpe-run-<slug>` from `origin/main` at intake, and its run ID `gtwpe-<yyyymmdd>-<slug>`
  (C1 §A A.4; design v1.2 §5.2). `RUN.md` records `origin/main`'s commit and each target's canon path and
  blob there. The pull request is opened at B1, so every pass after it finds it open, as the TW prompts
  require ("that branch then has one open pull request, opened if none is"). **No document is copied ahead
  of its pass.** TW-APPLY-10 writes "the entire revised PF" at the path its invocation names, applying exact
  original-bound operations to the canon original, and TW-RECORD-10 and TW-RECORD-20 write their file as the
  canon document "copied byte for byte" with one exact insertion. Both treat an existing file at their output
  path as a collision that blocks them ("do not overwrite it"). So the working copy of each document is made
  by the pass that changes it, from `docs/pfcanon/` on `main`, which meets architecture §3's steps 5 and 6
  and its rule that large documents are edited as copies, never regenerated (R3). A copy committed before the
  pass would stop it.
- **The passes.** Each pass follows the selected TW prompt's own body, read live from Notion when the pass
  starts (ITEM-07), as a pass inside the session Nathan started, which every TW prompt allows ("directly or
  through a session he started that runs this prompt as a pass"). The Flow Manager decides whether a pass runs
  in its own context or in a subagent (answer 3). The invocation it gives a pass carries what that prompt's
  intake asks for: the target's canon path, the run's sources by repository path, any selected boundary only
  where the execution prompt sets one, any supporting material, its output path and the run's branch. The
  output path is a pass directory for a drain, and the draft's exact path for TW-APPLY-10 or a record pass.
  A pass's terminal answer, `no redlines` included, is its return to the run, not the end of the run, and its
  handoff to the next prompt is made by the Flow Manager, never by the pass. **Only one pass writes at a
  time:** every pass commits and pushes its own outputs on the run's branch, and two writers in one working
  tree and branch can collide. Work that writes nothing, such as a review, may run in parallel. This is a
  constraint of one branch, not a decomposition (answer 3).
- **Document control (B4; R4).** TW-APPLY-10 and the record prompts already set and check each document's
  control fields (C3). The Flow Manager checks them across the run: each draft's version is its base version
  bumped once and equals the version in its file name; its dates are its own revision's; its Last Update Gate
  names the run's sources in Nathan's form, so drafts made from the same sources agree; its change-history
  entry is present where the document's rules require one; no document says Draft except where canon
  requires it (R5). It edits no draft. A failure sends that document back through its chain once with the
  finding, and then stops it (S5).
- **Consistency (B5; R13).** A fresh reviewer subagent, which writes nothing, reads every change in every
  draft, from the redlines files and proof logs that give each change and its place, and the passages of every
  other affected or canon document those changes bear on, completely, and returns its findings. The Flow
  Manager captures the return unedited into the run directory. A fix is a new redline-and-apply cycle that
  **starts again from canon**: the document's drain runs on the same sources with the finding as supporting
  material, then TW-APPLY-10. A second cycle on the draft itself would bump the version a second time and add
  a second change-history entry, which C3's rules reject. The superseded draft and its proof log are moved
  aside with `git mv`, kept, never edited. A finding in an eligible document outside the scope adds that
  document to the run, with the finding recorded as its reason. After the fixes, the documents they changed
  are reviewed once more; a finding left after that stops the run (S5).
- **Completion (B6; R14) and the pull request.** For each document, every point of architecture §10 is checked
  and recorded in `RUN.md`; a document that fails one goes back through its chain once, then stops (S5).
  The pull request's description keeps the template's headings (`AGENTS.md`): each document with its draft,
  its canon base path and blob, and its proof logs; the checks; what was not drained and why; and under
  *What merging does*, "Merging preserves the record and approves nothing (D21-C)". It may suggest how a draft
  is taken into canon, which answer 4 allows, and it claims no promotion, QA or acceptance.
- **What it never does (R12).** It never merges or closes a pull request, never writes `docs/pfcanon/`,
  Google Drive, ChatGPT Library or Notion, never edits a redlines file or a draft, and never creates or starts
  a session. An execution prompt that asks for any of these is a stop (S4), not an authorization.

#### ITEM-02. The run's layout

All under `docs/ephemeral/gtwpe.runs/<run-id>/`, on the run's branch, every directory name lowercase ASCII
(HDE Governance §0.4):

| Path | Holds | Written by |
|---|---|---|
| `RUN.md` | The run record: the execution prompt's path, `origin/main` at intake, the branch and pull request, each document's canon path and base blob, route and state at each boundary, every pass with its prompt and version, inputs, outputs, commit and checks, the stop and resume point, and the harness files | The Flow Manager |
| `inputs/` | Each input supplied as an attached file, so every pass and any resume reads it by repository path. A repository input is referenced by its path and blob, never copied | The Flow Manager |
| `pf-canon-drafts/` | Each complete replacement document, under its canon file name with the new version token, and **beside it its proof log**, `<name>.proof-log.md`, as C2 placed every proof log (C2 §A risk 5 and §P K-8). Taking a document into canon moves one file; its proof log stays as evidence | TW-APPLY-10; TW-RECORD-10 and TW-RECORD-20 |
| `passes/<key>/<attempt>/` | One directory per pass attempt: a drain's redlines file and its proof log, beside each other; an Apply diagnostic; and, on a redo, the superseded draft and proof log moved there | The passes; the Flow Manager moves superseded files |
| `review/` | Each consistency review's return, captured unedited | The Flow Manager |

`<key>` is the target's canon file name without its version and extension, lowercased. C1's §A put every
proof log under `passes/`; C2 put each one beside its artifact, so the drafts folder holds each document with
its proof log. A file holding a prompt body never enters the run directory.

#### ITEM-03. Stop and resume

The boundaries are B1 to B6 above. Each is clean when everything before it is committed and pushed and
`RUN.md` says so. Before each pass and at each boundary, the Flow Manager stops on any of C1's six signals,
settled here:

| Signal | Stops | When |
|---|---|---|
| **S1, capacity** | The run | The next pass cannot be finished at full quality in the context it would run in: its target, sources, PF03, its prompt and its checks, at about 3.0 bytes a token (ledger E-013), cannot all be read completely and held with room for its output. A fresh subagent has its own context, the Flow Manager what is left of its own. PF20 alone is 952,515 bytes, about 317,500 tokens, before the specification, the PF10 changes it reconciles and PF03 (C3's K-10). A pass is never started that cannot be finished, and never narrowed to fit |
| **S2, an unreadable input** | The run, for an execution-prompt input; the document, for a source only it uses | An input or source cannot be read completely (Technical Writing Best Practices §3) |
| **S3, a blocked pass** | The document | A pass returns `BLOCKED`, or the same failure persists after two materially different attempts, the TW prompts' own limit |
| **S4, a decision that is Nathan's** | The document; the run, when the execution prompt asks for anything ITEM-01's *What it never does* lists | A canon conflict; a PF30 rollover without his decision; a question a pass asks; an ineligible target the execution prompt names; a held-back PF10 change (*Triage*); a document that would need two pass chains in one run (*Eligibility and routing*) |
| **S5, a failed check** | The document | A proof log missing a required item; document-control fields that disagree; a consistency or completion finding left after its one fix |
| **S6, a write** | The run | A write that fails or lands uncertainly, or a pass that wrote anything but its named outputs (ITEM-07) |

A stop that concerns one document stops that document only: the Flow Manager finishes the other documents
through B3 and B4, then ends the run stopped, since B5 and B6 need every document (the PE Metaprompt:
"Continue independent authorized work"). On any stop it commits and pushes, writes in `RUN.md` what is done,
what is not, the signal and the exact resume point, says in the pull request's description where the run
stopped, and returns to Nathan with the resume line. A pass's partial output is never deleted to simulate a
rollback; the pass's own save-recovery rules resume it under its unchanged identity. That replaces C1's
"restoring the draft from its base blob": no draft is ever half applied, because TW-APPLY-10 validates the
whole package before it writes the file. It never finishes by lowering quality.

**Resume.** Nathan starts a new Flow Manager session with the same execution prompt, `RESUME <run-id>`, and
any decision he is giving. The Flow Manager checks out the run's branch, reads `RUN.md`, re-checks each
completed pass's outputs against the identities its proof log records, and re-checks each target's blob on
`origin/main` against `RUN.md`: a changed base restarts that document at B2. It then continues from the
recorded point, and nothing completed and verified is redone, except as the next paragraph says.

**A later day (C3's K-4).** A drain dates the change-history entry with its preparation date, and TW-APPLY-10
returns a package whose date disagrees with its own execution date. So **a document's drain and its apply run
on the same UTC date**: when an apply would run on a later date than its drain, because of a resume or
midnight, the Flow Manager runs the drain again before the apply. A document already applied keeps its date,
which is its revision's date; documents in one run may carry different dates.

#### ITEM-04. The execution prompt

Nathan writes it by hand until C5's Change Manager produces it, so it stays short. It names:

1. `RUN`, or `RESUME <run-id>`.
2. **The change:** what is requested.
3. **The sources:** each as an attached file or a repository path (answer 2): the source blob, which may be a
   PF10 set (answer 5).
4. **The governing specification**, a CRD or Epic Specification, by path, or `none`.
5. **Optionally:** the documents the change may affect; Nathan's authorizations, each of which the run never
   assumes: a PF20 or PF30 record (the separately authorized historical drainage of HDE Governance §9.1.1,
   ledger E-010), a PF30 rollover (HDE CRD Records §6), drafting a held-back PF10 change; any selected
   boundary; other context; a run name.

Everything else the Flow Manager recovers itself. A missing change or source is a stop at intake (S2). A PF
document, PF10 included, is read from `docs/pfcanon/` on `main`, never from an attachment. An input that is a
prompt body is refused (ledger E-022, option (i)). **No execution prompt overrides GTWPE-D1, the stop rule,
canon's read-only status, the ban on merging, or the route each document takes** (C1 §A A.8; R12; Nathan's
redlining discipline of 2026-09-29). Such an
instruction is a stop (S4), and every other instruction in it is read within those limits. Model or effort
lines in it are not instructions to the run (R16).

#### ITEM-05. Eligibility and routing

From Nathan's rulings of 2026-09-28 (design v1.2 §8.7) and his instruction of 2026-09-25 (plan v1.2 §1),
applied to the files on `main`:

| Class | Files on `main` | Route |
|---|---|---|
| General | PF03 and every file with "Canon" in its title outside PF09 and PF30: PF01, PF02, PF04, PF05, PF06, PF07, PF12, PF14, PF16, PF17, PF19, PF23, PF27, PF29 | TW-DRAIN-10, then TW-APPLY-10. **PF27 only when the run has a governing specification** that changes a template PF27 owns (ledger E-020) |
| PF09 | PF09.1 to PF09.7 | TW-DRAIN-20, then TW-APPLY-10 |
| PF20 | `PF20-Reference-HDE-Phased-Epics` | TW-RECORD-10, one section, only on the execution prompt's authorization |
| PF30 | `PF30.<n>-Canon-HDE-CRD-Records`, today PF30.1 | TW-RECORD-20 for a new CRD record, one section, only on that authorization; an update to an existing record goes through TW-DRAIN-10 and TW-APPLY-10, as the record prompts themselves say |
| Never a target | PF10, a source only; PF08, PF11, PF13, PF15, PF18, PF21, PF31; `PF-Invocation.md`; `PF-Reference-Glow Story.md` | None. A PF other than PF10 is never a source either (Nathan, 2026-10-06), though any PF may be read in support |

**One pass chain per document per run.** A document that would need two, such as a new record and a drained
update in the same PF30 volume, or two records in PF20, is a stop (S4): two chains would each start from canon
and produce two versions. Nathan's words fit it: PF20 and PF30 "only get one SECTION" (2026-09-29).

#### ITEM-06. GTWPE-D1 in a run

- The Flow Manager writes neither artifact. `RUN.md`, the inputs, the captured reviews and the pull
  request's description are none of GTWPE-D1's two artifact types. It never edits a redlines file or a
  draft, and every redlines file and final PF in a run comes from a pass that writes its own proof log
  beside it.
- A consistency or completion fix is a new cycle with its own proof logs (ITEM-01).
- At B6, every redlines file and every draft must have its proof log beside it, named after it, with all
  eight of GTWPE-D1's minimum items, checked by phrase. A run with an artifact and no complete proof log is
  not complete (S5).
- The body carries GTWPE-D1's requirement and its eight items in Nathan's words, so GTWPE-MGMT-10's guard can
  find them by phrase in this and every later version.

#### ITEM-07. E-006, E-016 and E-022

- **E-006, what a subagent may write.** A subagent that runs a pass writes only that pass's named outputs,
  in its named directory or path, and commits and pushes them on the run's branch, as the pass's prompt
  requires. It writes nothing else: no other path, branch or pull request, no merge, no Notion, Drive or
  Library write, no session and no skill. A subagent that runs a review writes nothing. **After each pass**
  the Flow Manager checks that `git status` is clean, that the files the pass's commits changed are exactly
  its named outputs, that only the run's branch moved on the remote, and that the run's pull request is still
  the branch's only one. A difference is S6. **Once, at B6**, it checks that the GTWPE parent page and
  *HDE TW* show no edit since intake. Its limit, as design v1.2 §7.5 recorded: a Notion write elsewhere, or one
  undone before the check, is not seen.
- **E-016, harness files.** At B6, `RUN.md` names every harness file that holds a prompt body: the session's
  transcript, each subagent's transcript, and each tool-results save. A save is deleted where the harness
  allows; otherwise it is left to the harness's teardown and never read again (`D22` condition 4).
- **E-022, reads of the TW prompt bodies.** Whoever runs a pass reads the selected TW prompt live from Notion,
  as the TW selection names it, and the next read goes back to Notion, after a compaction too. No body is kept
  as a file, copied into the repository, hashed or compared (`D22`). Each read is disclosed in `RUN.md`. An
  input that is a Notion prompt body is refused (ITEM-04).

#### ITEM-08. The handoff table

A new file, `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`, replaces design v1.2 §6 as the
GTWPE's handoff table, the one GTWPE-MGMT-10 reads for closure. GTWPE-MGMT-10's *Read these* says that table
lives in the design "until that table moves into `docs/prompt_ecosystem_management/gtwpe/`"; C4 moves it. The
new file holds:

- the common rules: files are UTF-8 Markdown with LF line endings, identities are repository paths and blobs
  or Notion page IDs and edit times, nothing passes by memory, and a consumer that cannot parse its input
  stops and never repairs it;
- the Flow Manager's handoffs: Nathan's execution prompt to it, and `RESUME`; its invocation of each TW pass;
  each pass's return to it (a `READY` or `BLOCKED` package, `no redlines`, a revised or updated document with
  its proof log, a diagnostic); its return of a diagnostic to the originating drain; and its return to Nathan;
- GTWPE-MGMT-10's own rows, H11 to H13, carried unchanged from design v1.2 §6. Rows H1 to H10, of the
  GTWPE-RUN-10 that is not built, are not carried;
- each member's result codes, so `state_sharers` can be read. The Flow Manager's are its own: proposed as
  `RUN_REVIEW_READY` (B6 passed), `RUN_STOPPED` (a stop, with its signal and resume point) and
  `RUN_NO_CHANGE` (no eligible document affected); `PLAN` fixes them;
- a small diagram of these handoffs, as the PE Metaprompt asks of a design;
- one sentence: the prompt bodies govern behaviour, the table indexes handoffs for closure, and a change to a
  handoff changes both its sides and this table in one Modification.

The catalog's *Approved design* entry is updated to name it.

#### ITEM-09. GTWPE-MGMT-10's maintenance before C6

The catalog already expects this member: "Further members are added as the approved build selects them: the
Flow Manager (a new prompt) and the TW prompts the build extends". So X4 adds GTWPE-FLOW-10's row to the
catalog's *Members* table, with its title, version and page, and the members note is rewritten to say so.
From then on GTWPE-MGMT-10's existing route for "A GTWPE prompt page" applies to it unchanged: a change is a
new versioned sibling under the GTWPE parent page, the catalog's row is moved at X4, and the page the row
names is never edited. No pre-C6 state or route is needed.

Until C6, the TW prompts stay selected on the *Glow Technical Writing Ecosystem* page, and the Flow Manager
resolves each pass's prompt and version there, as the TW prompts themselves do ("Resolve the next selected
version from the TW catalog"). C6, which moves every member into the GTWPE catalog, changes that locator in
the same change. Listing GTWPE-FLOW-10 adopts nothing: TW-ALPHA stays the TW selection, `tw-flowmaster` stays
installed until C6 retires it, and the page runs only when Nathan starts it. After C4, Nathan can run a first
live trial with a hand-written execution prompt (C1 §A A.5).

#### How the TW prompts fit, unchanged

No TW prompt needs to change for the Flow Manager to run it, so nothing goes to Nathan under the request's
last paragraph. Each of these was checked against the bodies read live:

| Point | What the TW prompts say | How the Flow Manager meets it |
|---|---|---|
| Who invokes them | "directly or through a session he started that runs this prompt as a pass" | Its session is the one Nathan started |
| Output path and branch | "An invocation that names no such path or branch is a missing input" | Every invocation names both |
| An existing file at an output path | "An unrelated collision is a blocker for that name; do not overwrite it" | No pre-copy; a redo moves the superseded draft aside first |
| `no redlines` "as the entire final response ... Stop" | The drain's own terminal answer | Read as the pass's return to the run |
| "For a complete READY package, Nathan invokes TW-APPLY-10"; the handoff is "Do not execute the invocation" | The pass hands on; it never invokes | The Flow Manager makes the next invocation, in the session Nathan started |
| An Apply diagnostic "only to the actual preparer" | Through Nathan or the session he started | It returns the diagnostic to that drain, in the same run |
| A record pass that must "ask Nathan" | A destination, approval or evidence it cannot resolve | A stop (S4) with the question |
| The canon commit each pass records | "Read current authoritative PF Markdown from `docs/pfcanon/` on `main`" | Base blobs pinned at B1 and re-checked before each pass |

#### The new page, through GTWPE-MGMT-10's route

- **Authoring.** `PLAN` drafts the complete body through the PE Metaprompt, which governs creating a prompt
  for an approved ecosystem addition, under this analysis once approved. That includes the PE's mandatory
  PF03, PF06 and PF10 compatibility check for a new Glow prompt; its two identity lines, the title line and
  `Prompt Version:`, at the execution date's `.1`, which the PE allows a net-new prompt; versionless
  references; and no runtime-selection or workload fields.
- **Where the draft lives before publication.** Not in the repository: Nathan's "writing prompts do not
  belong in repo" (C2's analysis approval), `prompt-corpus-policy.md` ("a committed or uploaded body") and
  GTWPE-MGMT-10's "No body enters it". The PE allows it as a temporary local draft ("Temporary local drafting
  is allowed"), and design v1.2 §12.2, still applying where not superseded, sets the practice: "Bodies are
  authored in the session. Any scratch draft is deleted after publication and disclosed (`D22`); no body
  enters the repository". So §P records the page's title, parent, identity lines, its headings in order and
  the phrases its readback checks, never the body. The single `PLAN` reviewer reads the draft from the path
  its committed brief names. Nathan approves on the record and that review, and he and PE39 read the page
  live once it is published, before the first trial. §12.2 had each body given "in the request itself for
  review"; for GTWPE-MGMT-10's own first page, which Nathan approved before the body existed, that review
  fell to the readback and the pilot's cold run (`CHECKPOINT.md` §12.1). Sending him the draft as a file
  would be "an uploaded body", which `prompt-corpus-policy.md` bars. `EXECUTE` publishes the reviewed draft
  unchanged, and the draft is deleted once the page is read back.
- **The Notion write.** GTWPE-MGMT-10's *Notion writes* allow it to "create child pages of the GTWPE parent
  page by duplication, then set their titles and apply approved edits to them". `EXECUTE` therefore duplicates
  an existing child page of the GTWPE parent, sets the new title, and replaces the whole content with the
  approved body, waiting for each write to land. The readback reads the page whole: title, parent, identity
  lines, every heading in order, every check phrase, no text of the duplicated page left, and the duplicated
  page's edit time unchanged. This is finding F-2.
- **Its gate, tier 1.** The member's own checks, and the consumers the handoff table names: a static check,
  made against the TW bodies read live, that each pass invocation the body defines supplies every input that
  prompt's intake requires, and that each of its returns is consumed. No executable check exists for TW.

#### What each rule becomes

C1's §A traced the architecture's rules, R1 to R18. Here is where each lands in the Flow Manager, with the
canon rules this analysis adds.

| Rule | Where it is met |
|---|---|
| R1 Redline creation, then redline apply, each with its report, for every document but PF20 and PF30 | ITEM-05's routing; B2 and B3 |
| R2 PF20 and PF30 add one section each, written directly, with a report | ITEM-05; the record passes at B3 |
| R3 Large PFs changed only by applying redlines to a copy, never regenerated | The working copies are made by the passes; the Flow Manager never writes a draft (ITEM-01) |
| R4 Version, dates, gate and change history set from the change and agreeing | The passes (C3), and B4 across the run |
| R5 No Draft, placeholders or stale status | The passes (C3), and B4 and B6 |
| R6 PF09 rows judged on all the evidence | TW-DRAIN-20, unchanged |
| R7 PF20 and PF30 reconcile the specification with every applicable PF10 change | The record passes, given the specification and the PF10 changes as sources |
| R8 PF30 a volume family; PF20 one document | TW-RECORD-20 and TW-RECORD-10; a rollover only on Nathan's decision in the execution prompt |
| R9 Every pass reads the whole supplied context | Triage, and every pass given the complete sources; a selection only where the execution prompt sets one |
| R10 Eligibility | ITEM-05 |
| R11 PF27 only when a specification exists | ITEM-05 |
| R12 Canon untouched; a review-ready pull request; promotion outside the flow | ITEM-01, *What it never does*; ITEM-04 |
| R13 Cross-document consistency | B5 |
| R14 The completion standard | B6 |
| R15 Subagents, as many as it judges useful | Its own decomposition, within ITEM-07's write bounds |
| R16 No model, effort or strength advice | None in the body; the readback checks its absence |
| R17 A proof log for every artifact | ITEM-06 |
| R18 Stop at a clean boundary rather than lower quality | ITEM-03 |
| Change Process Guide §3.5.2.8, drain ordering | Triage |
| HDE Governance §9.1.1: PF20 and PF30 entries only by authorized historical drainage; merges are Nathan's | ITEM-04 and ITEM-05; ITEM-01 |
| HDE Governance §0.4, lowercase directories | ITEM-02 |
| HDE Build Notes 2.29: canon from `docs/pfcanon/` on `main`; change-process documents in `docs/ephemeral/` | ITEM-01 and ITEM-02 |
| `AGENTS.md`: the pull request's headings and *What merging does* | ITEM-01, *Completion* |

### Per part: closure, tier, class and targets

One part, PART-01: the new page, its handoff table and its catalog row. Each describes the one new member and
is false without the others: a table of handoffs for a member that does not exist, or a row naming no page.

- **Targets.**
  - `prompt`: GTWPE-FLOW-10's first page, a new child of the GTWPE parent page.
  - `rule`: `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`, a commit on this branch, merged by
    Nathan at X2.
  - `notion_control`: the catalog's new row, its members note and its *Approved design* entry, with X4's
    checked-through commit.
- **Closure**, from the handoff table this part writes (ITEM-08), since design v1.2 §6 has no row for a member
  it never designed, and the GTWPE has no graph parts for `closure.py`:
  - upstream, the producers of the handoffs GTWPE-FLOW-10 consumes: TW-DRAIN-10 and TW-DRAIN-20 (a package or
    `no redlines`), TW-APPLY-10 (a revised PF or a diagnostic), TW-RECORD-10 and TW-RECORD-20 (an updated
    document), and Nathan, who is not a member;
  - downstream, the consumers of the handoffs it produces, its pass invocations: the same five, and Nathan;
  - state sharers: none. Its result codes are its own, and no member shares one.

  TW-TRIAGE-10 exchanges no handoff with it.
- **Tier 1.** A new member is at least 1 (GTWPE-MGMT-10's `gate_tier` row). No existing handoff's artifact,
  format, required fields or consumer check changes: the TW prompts already take an invocation from a pass
  inside a session Nathan started, their packages and returns are unchanged, and the selected release's
  *Current operation* already records such a run ("as a pass inside a session he started, or a handoff
  honored by a separately authorized controller"). The gate covers the member and the consumers the table
  names (*The new page*).
- **Class B, rule application.** It carries rulings already made into a new prompt and its records: the
  target architecture with Nathan's answers and directions, C1's approved §A, GTWPE-D1 and his eligibility
  rulings.
- **Authoring.** Through the PE Metaprompt's general rules, with GTWPE-MGMT-10's workarounds (*Relation to
  the PE Metaprompt*).

### Member dispositions (HDE Governance §9.1.6)

| Member or interface | Disposition | Reason |
|---|---|---|
| GTWPE-MGMT-10 100526.2 | Unaffected; not changed | Its route maintains the new member (ITEM-09). F-2 and F-3 go to a later repair |
| TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10, TW-RECORD-10, TW-RECORD-20 | Unaffected; not changed | The Flow Manager runs them as passes, and every fit point is met without a change (*How the TW prompts fit*) |
| TW-TRIAGE-10 | Unaffected; not run | It is PF10-only and list-only, and its "A title containing Canon is not an eligibility rule" contradicts Nathan's ruling of 2026-09-28 until C5. The Flow Manager's triage carries its reading rule instead |
| TW-MGMT-10, TW-ASSESS-10 | Unaffected | Neither is selected |
| The GTWPE catalog | Affected | ITEM-08 and ITEM-09; and X4's checked-through commit |
| Design v1.2 §6 | Replaced as the handoff table; not edited | ITEM-08. The design is a dated record |
| The GTWPE decision record; the PE Metaprompt 091426.1 | Unaffected | The ruling applied; the authoring control |
| `tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Unaffected | They do not run the current TW release, under Nathan's waivers for TW-ALPHA-20261006.1 and TW-ALPHA-20261006.2; they exchange no handoff with the Flow Manager; and they stay installed until C6 retires them. No TW-ALPHA release changes here, so no new waiver is needed |
| `glow-write-boundary`, `glow-artifact-storage`, `glow-workspace-currency` | Unaffected | A run writes only under `docs/ephemeral/`, on a `docs/` branch with one pull request, never merges or writes canon, and is read-only to Notion. Two wording points are risks 1 and 6 |
| The selection page, *Alpha 1*, *HDE TW*, the Operations Hub, the architecture page | Unaffected by the route | No write: GTWPE-MGMT-10 writes TW pages only with a new TW-ALPHA release (N-1) |
| The GCFPE register and Flow Index | Unaffected | They list no TW or GTWPE member |
| `modification_validate.py`, `gtwpe_record_check.py`, the template | Unaffected | `TARGETS` holds `prompt`, `rule` and `notion_control`; no new check is needed |

### GTWPE-D1, prompt by prompt (A2)

| Prompt | Writes before C4 | Writes after C4 | How the part leaves GTWPE-D1 whole |
|---|---|---|---|
| GTWPE-FLOW-10, added | — | Neither artifact type: `RUN.md`, inputs, captured reviews and the pull request's description | Not bound as a writer. Its body requires that every artifact in a run come from a pass with its own proof log, and checks each proof log's eight items at B6 (ITEM-06) |
| TW-DRAIN-10, TW-DRAIN-20 | A redlines file, with its separate proof log beside it | The same, in a run's `passes/` | Unchanged: the Flow Manager names the directory, so each proof log stays beside its file and named after it |
| TW-APPLY-10 | The revised PF, with its proof log beside it | The same, in `pf-canon-drafts/` | Unchanged |
| TW-RECORD-10, TW-RECORD-20 | The updated PF20 or PF30, with its proof log beside it | The same, in `pf-canon-drafts/` | Unchanged |
| TW-TRIAGE-10 | A list in its response | Not run | Not bound |

No combined proof log is defined: no prompt writes both types.

### Scope, and how it was measured (`SCOPE-001`)

**Method.**
- The new body has no text yet to measure. Its scope is *What each rule becomes*: every rule the approved
  design, this analysis and canon assign to it, each with the place it lands.
- The surfaces this part changes, and the text GTWPE-MGMT-10 reads for closure, were measured by broad match
  minus permitted exceptions, case-insensitive. GTWPE-MGMT-10 100526.2 and the GTWPE parent page came back
  inline, with no save to run a command over, so they were counted by reading, and each count is checked by a
  second, independent reading of a second fetch at A6 (the request's standing direction; ledger E-035). The
  repository was counted by `git grep`.

| Surface | Broad match | Hits | Permitted exceptions | Remainder: places to change |
|---|---|---|---|---|
| The catalog | `Flow Manager` | 1 | — | 1: the members note |
| | `GTWPE-FLOW-10`; `handoff`; `§6` | 0; 0; 0 | — | Additions: the *Members* table's new row, and the handoff table named in the *Approved design* entry |
| GTWPE-MGMT-10 100526.2 | `§6` | 2 | — | No edit, which is out of scope: *Read these* ("until that table moves") and the `closure` row both resolve to the new file (F-3) |
| | `handoff table` | 2 | The same two places | No edit |
| | `versioned sibling` | 4 | The TW-ALPHA member's row and the TW sentence of *Notion writes*: 2 | No edit: the GTWPE prompt-page row and the prompt route apply to the new member (F-2) |
| | `duplicat` | 3 | *Lineage*'s quotation of the PE: 1 | No edit: *Notion writes* and the prompt route are the duplication C4 uses (F-2) |
| | `new member` | 1 | — | No edit: the `gate_tier` rule that sets tier 1 |
| `gtwpe/` at `ad1615d`, by `git grep` | `handoff` | 3 | All in GTWPE-D1's own text | Addition: the new file |
| | `§6`; `Flow Manager`; `GTWPE-FLOW-10` | 0; 0; 0 | — | — |
| `docs/` at `ad1615d`, by `git grep` | `GTWPE-FLOW-10` | 2 | Both in C1's dated record | — |
| | `gtwpe.runs` | 7 files | Dated plans and designs, and C1's record; no run directory exists | — |

**The rule-change search (`D26-E`).** The rule that changes is where the GTWPE's handoff table lives. The old
text it contradicts: GTWPE-MGMT-10's two references, resolved as above; the catalog's *Approved design*
entry, which this part updates; and design v1.2 §6 itself, a dated record, replaced by the new file's own
statement and not edited. `PLAN` turns these into checks by phrase on the catalog and the new file.

**What the new page must not say** (`FUNC-001`; R12, R16): model, surface or effort advice; Google Drive or
ChatGPT Library as a source or destination; a merge; a canon write; a session created or started. `PLAN`
turns these into absence checks by phrase on the new page, beside a `D26-E` broad match by reading.

### Pages that name the Flow Manager (A3)

No page names a version of the new member or links its page, since neither exists. **Method:** Notion
searches with highlights off on `GTWPE-FLOW-10` and on "Flow Manager technical writing flow"; fetches of
each page found that could name it as current: the GTWPE parent page, the selection page, *HDE TW* and the
architecture page, read in context; *Alpha 1* and the Operations Hub, saved by the harness and counted by
script for `Flow Manager`.

| Page | Edited | Names the Flow Manager | Written by the route |
|---|---|---|---|
| The GTWPE parent page and catalog | 2026-10-06T16:53:37.871Z | Once, the members note: "the Flow Manager (a new prompt)" | Yes, at X4 (ITEM-09) |
| The selection page | 2026-10-06T16:54:30.403Z | Twice: TW-ALPHA-20261006.2's note and the historical TW-ALPHA-20261006.1 note, "until the Flow Manager (C4) replaces the Flowmaster, which C6 retires" | No |
| *HDE TW* | 2026-10-06T16:56:13.452Z | Twice: the current and the historical release notes, "until the Flow Manager (C4)" | No |
| *Alpha 1* | 2026-10-06T17:12:13.956Z | Twice, in the same two notes | No |
| The Operations Hub | 2026-10-06T16:56:55.793Z | Twice, in the same two notes | No |
| The architecture page | 2026-10-05T16:16:17.223Z | In its diagram and roles | No |

The four TW pages' current notes read as future once C4 lands. They are dated release notes, which
GTWPE-MGMT-10 writes only with a new TW-ALPHA release, and C6 rewrites them when it marks TW-ALPHA
superseded (N-1). **TW's current release** is not reached: no TW-ALPHA member changes. C4 adds a way to run
the flow without changing a TW member or the selection, and the selected release's *Current operation*
already admits a run "as a pass inside a session he started", so it stays true.

### Contradictions and risks

1. **The reviewed body lives only in this session before publication.** It cannot enter the repository, and
   no fingerprint binds it, since a body is never hashed. `PLAN` and `EXECUTE` must run in this session; a
   fresh session at `EXECUTE` has no draft and returns to `PLAN`. The readback checks the page by heading and
   phrase, and Nathan reads it live. `glow-artifact-storage` says "Do not author a prompt as a local file and
   attempt to transfer it"; the PE allows "Temporary local drafting", design v1.2 §12.2 sets it for new
   bodies, and the publication is one Notion write of the reviewed text, after which the draft is deleted, so
   no second home is kept.
2. **The route was written for a new version (F-2).** Duplicating a child page leaves, for seconds, a copy
   titled `… (1)` that holds that page's body, until its title and content are replaced. A failure in that
   window leaves a stray page: a loud stop under `D26-B`, and Nathan archives it. `PLAN` picks the page.
3. **One writer at a time.** Write passes run one after another, so a run with many documents takes longer
   and is likelier to meet S1 and resume. Parallel writers would need separate worktrees and branches merged
   back, against Nathan's "let's not overcomplicate this".
4. **A consistency fix redoes the document from canon**, a drain and an apply again, which for a large
   document may meet S1.
5. **S1 rests on the session's judgement of its capacity.** PF20's record pass needs room for about 317,500
   tokens of PF20 alone, before the specification, the PF10 changes and PF03 (C3's K-10).
6. **`glow-write-boundary` says "Open the PR when the session's work is done".** The architecture (§3, step 4)
   and the TW prompts open the run's pull request early, and a stopped run must resume from its branch. The
   run opens it at B1; only Nathan merges it.
7. **No executable check exists for TW**, and no live trial has run since 2026-09-08 (C3's K-7). The Flow
   Manager's first run is Nathan's trial after C4, so the gate is static.
8. **Advice for a downstream session.** HDE Governance §9.1.3 says "Every downstream-session prompt must
   receive task-specific human advice for execution surface, model and reasoning level". HDE Build Notes 2.38
   leaves its continuation to Nathan, and he confirmed on 2026-10-04 that his direction of 2026-09-29 is that
   determination for the TW prompts (MODIFICATION-20260930-gtwpe-tw-model-advice, E-F2). The Flow Manager is
   a TW prompt, so it carries none, and it sets no model for its subagents.
9. **E-010 stays Nathan's.** A record pass runs only on the execution prompt's authorization of historical
   drainage (HDE Governance §9.1.1).
10. **The handoff table restates the bodies' handoffs** (`DERIV-001`). The bodies govern behaviour; the table
    is GTWPE-MGMT-10's index for closure, and a handoff change changes both sides and the table in one
    Modification, at tier 2.
11. **The E-006 check has limits:** a Notion write outside the two watched pages, or a write undone before the
    check, is not seen (design v1.2 §7.5).
12. **Capturing a review's return** relies on the harness's transcript layout, which is not a documented
    interface; a change to it fails loudly (design v1.2 §7.4).
13. **One reader of the bodies.** The fit analysis rests on this session's reading of the six TW bodies, since
    workers do not fetch bodies (`D22`). `PLAN`'s dry run reads them again for the two-sided check.
14. **The phrase check sees phrases, not meaning** (`D14`'s note of 2026-09-23). The review reads for
    behaviour.
15. **The request's citation.** It cites "C3's K-8" for the proof log beside its artifact. That finding is
    C2's K-8; C3's K-8 is F-1. This analysis uses C2's (N-2).
16. **Drain ordering needs PF10's record of an epic's QA.** Where PF10 does not record it, the change is held
    back and listed (design v1.2 §10.5), never drafted on a guess.

### Defect classes matched (`ecosystem-change-management.md` §4)

- `GUARD-001`: GTWPE-D1's run rule ships with its check (B6, S5) and with GTWPE-MGMT-10's phrase readback.
- `FUNC-001`: the new page is checked for retired behaviours by what they make an agent do: model advice,
  Drive or Library, a merge, a canon write, a session.
- `DERIV-001`: the handoff table against the bodies (risk 10); `RUN.md` against the branch's files, which the
  resume re-checks against their proof logs.
- `NAME-001`: eligibility is by title because Nathan ruled it so on 2026-09-28 (design v1.2 §8.7); routing
  within it is by function.
- `STALE-001`: the drafts are the deliverable under review, not derived output (C1 §A risk 1).
- `SCOPE-001`: the scope above.

### Findings against GTWPE-MGMT-10 100526.2

- **F-2.** Its prompt route is written for a new version of an existing member: "Duplicate the current
  version's page", with headings "the same as the current version's". *What this prompt may change* names
  only "A new versioned sibling page". It has no step for a new member's first page. C4 applies the route as
  *Notion writes* allows: duplicate a child page of the GTWPE parent, retitle it, replace its content with the
  approved body, and check that the duplicated page is unchanged. Creating the page directly would be outside
  *Notion writes* and would need Nathan's explicit authorization.
- **F-3.** *Read these* and the record's `closure` row name design v1.2's "§6 handoff table". *Read these*
  already says "until that table moves into `docs/prompt_ecosystem_management/gtwpe/`", and the new file says
  it replaces §6, so both resolve to it; a later repair can name the file.

### Candidates for separate Modifications (recorded, not taken)

- **F-2 and F-3**, in a later GTWPE-MGMT-10 repair, with F-1 and E-035's count-by-script candidate.
- **C5**, the Change Manager, which writes the execution prompt in ITEM-04's contract and corrects
  TW-TRIAGE-10's eligibility sentence; **C6**, adoption, with E-033.
- **N-1**, for PE39 on Nathan's direction, outside the route. Once C4 lands, the four TW pages' current
  notes still say TW runs by Nathan's direct invocations "until the Flow Manager (C4)". The architecture page
  still shows a copy step before the passes, says the stop design is "still to be designed", and gives the
  Last Update Gate rule as it stood before Nathan's rulings of 2026-10-06, which the repository record
  carries. C6 rewrites the TW notes in any case.
- **N-2**, for PE39's ledger: risk 15.

### Open questions for the Product Owner

None. Canon and Nathan's rulings settle every point this change needs (*Canon and rulings relied on*). Two
choices are recorded here for his approval rather than asked: the route's duplication (F-2), and the body
reviewed in this session and read live by him after publication (*The new page*).

### Readiness and interaction cost

`READY`. No item waits on another item's execution, every surface's scope is measured, and no ruling is open.

    interaction_cost = 0 open rulings + 2 + 3 review rounds + 0 skill review cycles + 0 installs + 2 merges = 7

- **Review rounds:** this mode's dry run; `PLAN`'s dry run; and one full review by a single reviewer, who
  reads the draft body. A second reviewer or a diff check only if that review finds a required defect, by
  the request's standing direction.
- **Merges:** the branch's pull request, amthorn78/glow-hdengine-v2#581, at X2, because the handoff table is a
  repository file other than the record, which GTWPE-MGMT-10 allows ("the branch's pull request at X2"); then
  the record's pull request after X5. Neither is merged before its point.
- **Splitting saves nothing:** the page, its table and its row are one part.

The estimate is in the front matter. Time is the meter, and twice the estimate is where the session stops.

### Dry run (A6)

Every normal-path gate and readback of this mode, read-only, by this session. No full review ran: as in each
earlier GTWPE Modification, `ANALYZE` runs a dry run only, and `PLAN` carries the full review.

| # | Gate or readback | Result |
|---|---|---|
| D1 | Both record checks on a scratch copy of this record at `ANALYZED`, with this round in `reviews`: `modification_validate.py` and `gtwpe_record_check.py` | Both exit 0, 1/1 each |
| D2 | The front matter parses (PyYAML), its `request` equals PE39's message, and every table in the record has one column count in every row, by script | Parses; the request is verbatim; 13 tables, each with one column count in every row |
| D3 | A0 reproduced: `git fetch origin main`; `origin/main`; `git log b1bd769..origin/main` over *The watched sources* | Still `ad1615d`; the watched-path log is empty |
| D4 | The new title is free under the GTWPE parent page | The page, fetched again (edited 2026-10-06T16:53:37.871Z, unchanged), has five child pages: the four GTWPE-MGMT-10 versions and the architecture page. None is a GTWPE-FLOW-10 page |
| D5 | The scope counts, by a second, independent reading of a second fetch of GTWPE-MGMT-10 100526.2 and of the catalog | Both unchanged (2026-10-05T16:36:11.384Z; 2026-10-06T16:53:37.871Z). Every count confirmed, section by section: `§6` 2, `handoff table` 2, `versioned sibling` 4, `duplicat` 3, `new member` 1; in the catalog, `Flow Manager` 1, and `GTWPE-FLOW-10`, `handoff` and `§6` 0 |
| D6 | Each quotation from a repository file or an installed skill is found exactly in its source, by `grep -F` | 17 of 17 found: 14 in repository files on `main`, 2 in the installed skills, and 1 in the request |
| D7 | The fit table's and the route's quotations from the TW bodies, GTWPE-MGMT-10, the catalog, the selection page and the PE Metaprompt, checked against this session's fetches by reading | Each found as quoted. `PLAN`'s dry run reads the TW bodies again for the two-sided check |
| D8 | The record tools need no change for this Modification | By reading at `ad1615d`: `TARGETS` holds `prompt`, `rule` and `notion_control`, and the record check needs only the subsections this record has |

No required defect.

### Harness files (`D22` condition 5)

- **Inline fetches, held only in this session's transcript**, which the harness keeps and leaves to its
  teardown: GTWPE-MGMT-10 100526.2, twice (the mode's start and D5); the six TW bodies, once each, read for
  *How the TW prompts fit*; GCFPE-MGMT-10's proposed body and `091426.1`, fetched at A0 for their edit
  times; and the control pages: the GTWPE parent page (twice), the selection page, *HDE TW* and the
  architecture page.
- **Harness saves, each read by a script that printed only what the check needed:**
  - the PE Metaprompt `091426.1` fetch, `mcp-Notion-notion-fetch-1791308193076.txt`: its title, edit time and
    path for A0, then its headings and, in slices, the sections on modes, sources, standards, authoring,
    identity and publication, for *The new page*. One slice's output, 33.6 KB of PE text, was itself saved by
    the harness as `bwptg83jd.txt` and not read again. Both files were deleted with `rm` once the read was done
    (exit 0);
  - the register, `mcp-Notion-notion-fetch-1791308262714.txt`: its edit time and the two rows of *Current
    selection* that name GCFPE-MGMT-10 and the PE Metaprompt;
  - *Alpha 1*, `toolu_017vviMzMgXt2igzEW9Whjey.json`, and the Operations Hub,
    `mcp-Notion-notion-fetch-1791309137552.txt`, both control pages: each one's edit time, its `Flow Manager`
    count and the sentences that hold it, and its first headings.

  No save was hashed or compared as a body's identity.
- **A save that holds no prompt body:** `brgp5hj17.txt`, an oversized command output of HDE Governance §9.1.
- **The session transcript.** A1's verbatim copy of the request needed PE39's message, which only the
  transcript held. A script read it once and printed only the message's timestamp and length, never a tool
  result, and saved the message to `c4_request.txt` in the scratchpad.
- **Scratch files**, in this session's scratchpad: copies of PF03, PF04, PF06, PF10 and PF30.1 from `main`
  (canon, not prompt bodies); the request; the script that builds this record's front matter; drafts of this
  section; and a scratch copy of this record for the dry run.

### Canon and rulings relied on

- **`AGENTS.md`:** the canon-first rule; canon is read-only; the CI-exempt paths; the pull request's headings
  and "Merging preserves the record and approves nothing (D21-C)".
- **Technical Writing Best Practices** (PF03) §1, which authorizes no repository action; §3, complete reads
  (S1, S2); §7 and §15.1, document-control values; §11 and §14, the editorial checks (B6).
- **HDE Governance** (PF04): §0.4, lowercase directories (ITEM-02); §9.1.1, PF20 and PF30 entries only by a
  separately authorized historical drainage, merges as Nathan's, and a revision as a complete replacement
  that preserves the prior artifact; §9.1.2 and §9.1.3, as HDE Build Notes 2.29 and 2.38 supersede them, with
  §9.1.3's downstream-session advice (risk 8); §9.1.6, prompt ecosystem governance: the member dispositions,
  what a new member identifies, the readback of a complete changed body, and author, checker and acceptor.
- **HDE Build Notes** (PF10): 2.29 PF10-CANON-001, canon from `docs/pfcanon/` on `main`, change-process
  documents in `docs/ephemeral/`, and prompt bodies single-homed in Notion; 2.31 PF10-HDR-001; and 2.38
  PF10-AINEUTRAL-001, any surface, with the advice question left to Nathan.
- **Change Process Guide** (PF06) §3.5.2.8, the post-QA drain ordering (*Triage*).
- **HDE CRD Records** (PF30.1) §6, rollover as the Product Owner's determination (ITEM-04, ITEM-05).
- **Rulings:** GTWPE-D1; in `gcfpe.decision-record.md`, `D21`, `D22` with its refinement, `D23`'s
  clarification on subagents, which binds the GCFPE's main ecosystem only, `D24` and `D26` A to E; Nathan's
  target architecture with his answers 1 to 8, his directions of 2026-09-29 on redlining, stopping and model
  advice, and of 2026-10-05 on proof logs; his eligibility rulings of 2026-09-28 (design v1.2 §8.7); his
  instruction of 2026-09-25 on PF27 and PF30 (plan v1.2 §1); his "writing prompts do not belong in repo"
  (C2's analysis approval); his rulings of 2026-10-06 on the Last Update Gate; C1's approved §A; and design
  v1.2 §§5.2, 6, 7.4, 7.5, 10.5 and 12.2, where neither the architecture nor C1's §A supersedes them.
- **Controls:** `prompt-corpus-policy.md` with its `D22` amendment; `prompt-body-content-policy.md`;
  `notion-write-boundary.md`; the PE Metaprompt 091426.1's general rules; `glow-write-boundary`,
  `glow-artifact-storage` and `glow-workspace-currency`.
- **GTWPE-MGMT-10 100526.2**, as fetched at the start of this mode: *Entry contract*, *The spine*, `MODE =
  ANALYZE`, *How each kind of target changes* and *The watched sources*.

**This mode's own cost.** Time: from 2026-10-06T17:23:53Z to A7 at about 18:02Z, about 38 minutes by the
session's clock. Tokens: not measured by this session.

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

This session runs the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
100526.2*, fetched live at the start of the mode, edited 2026-10-05T16:36:11.384Z, as at `ANALYZE`.

- **Input:** §A as Nathan approved it at `772ccfb` on 2026-10-06. His words are in `analyze_approved_by`. The
  mode started at 2026-10-06T18:15:59Z, when his approval arrived.
- **The branch.** Nathan merged amthorn78/glow-hdengine-v2#581 with the record at `ANALYZED`, at
  2026-10-06T18:14:05Z (`7d05995`), and PE39's ledger change E-040 and E-041 followed (#582, `601b330`). The
  furthest copy of the record is therefore on `main`, byte-identical to `772ccfb`'s, and this mode works, as
  the *Entry contract* says for that case, on a new branch: `docs/20261006-modification-gtwpe-flow-manager`,
  restarted from `origin/main` at `601b330`, with a new pull request.
- **Authoring control:** the selected PE Metaprompt 091426.1, edited 2026-09-23T17:17:22.217Z, as A0 found
  it, fetched again at this mode's start. Its general rules apply with GTWPE-MGMT-10's workarounds
  (*Relation to the PE Metaprompt*): `Create` of an ecosystem addition whose design is approved, here §A as
  Nathan approved it; the two identity lines, at the execution date's `.1`, which the PE allows a net-new
  prompt; versionless references; no runtime-selection, configuration or workload text; and the mandatory
  PF03, PF06 and PF10 compatibility check for a new Glow prompt (*Dry run*, P10). Its GCFPE overlay, the
  section *GCFPE controlled release overlay*, does not apply and was not read.
- **`main`** is at `601b330`. Since `ad1615d`, which §A examined, it gained #581, this record at `ANALYZED`,
  and #582, ledger rows E-040 and E-041 in `docs/ephemeral/gtwpe.rewrite/ERRORS.md`. Neither touches a
  watched path (*Dry run*, P3).

### Nathan's directions, and how this plan applies them

- **The three choices he approved with the analysis.**
  - No document is copied ahead of its pass: the body says so, and routes every working copy through the pass
    that changes it (*The new page*).
  - The body is drafted and reviewed in this session and never stored in the repository. It is the local draft
    at `/tmp/claude-0/-home-user-glow-hdengine-v2/93ba4e61-b5cc-5c88-a70c-08c9d4d5eb79/scratchpad/c4/flow10/GTWPE-FLOW-10-draft.md`.
    This plan names it only by its headings, identity lines, last words and check phrases. `EXECUTE` runs in
    this session and publishes it unchanged, apart from the version in its first two lines. Nathan and PE39
    read the published page live before the first trial.
  - The new page is made by duplicating a child page of the GTWPE parent page, retitling it and replacing its
    content (F-2). The page duplicated is the architecture page, *GTWPE Target Architecture — Document-Writing
    Flow*, because it holds no prompt body: the duplication copies none, and a copy a failure leaves behind is
    plainly not a prompt.
- **One dry run and one full review by a single reviewer, who reads the draft body;** a second reviewer or a
  diff check only if that review finds a required defect. Nathan's approval names the reviewer's reading of
  the draft, the one body a worker reads here (`D22`). The reviewer fetches nothing from Notion.
- **"this flow can be simplified, let's not overcomplicate this".** One part, three targets, four Notion
  writes and one repository file. The body has twelve sections under its title, and three result codes. The
  plan builds no tool: the handoff table is one Markdown file, fixed in this plan and copied at `EXECUTE`.
- **Stop rather than produce substandard results.** A failed check stops `EXECUTE`, and nothing is repaired in
  flight (*How the plan runs*). The body carries the same rule for a run (S1 to S6).
- **No GTWPE prompt carries model, effort or strength advice (R16); no TypeSafe scoring.** The body has none,
  which *The new page's checks* tests by phrase and by reading. Nothing is scored.
- **The meter is time.** The estimate is about 5 h for `PLAN` and about 2 h for `EXECUTE`, not counting the
  wait for Nathan's merge. This mode stops at 10 h on the meter from 18:15:59Z, and `EXECUTE` at 4 h from
  X1.1.
- **GTWPE-MGMT-10 100526.2's GTWPE-D1 guard.** The body writes neither artifact type, and it carries GTWPE-D1's
  requirement and its eight minimum items in Nathan's words, which the readback checks by phrase.

### Findings on §A (recorded, not edited)

`PLAN` does not rewrite the analysis. Four of its statements are inexact for the body. None changes the scope,
the items or the members, and the body follows the sources §A cites.

- **P-1. PF30 changes only with a specification.** §A's routing table sets the specification condition for PF27
  only. The instruction it cites, Nathan's of 2026-09-25 (plan v1.2 §1: "PF27 and PF30 are updated only when a
  specification exists"), sets it for both. The body makes the PF30 family a target only when the run has a
  governing specification, for a new record and for a change to an existing one.
- **P-2. A held-back PF10 change.** §A's triage lists such a change and does not draft it; its signal table
  makes it a stop for Nathan's decision (S4). The body joins the two: the change is listed and not drafted, and
  each document it bears on stops until Nathan decides to draft the change or leave it out.
- **P-3. The check of the remote after a pass.** §A says the Flow Manager checks "that only the run's branch
  moved on the remote". During a run, Nathan and other sessions move other branches, `main` among them, so that
  check would stop runs that did nothing wrong. The body checks instead that no branch was created or deleted
  and that the run's branch is at the pass's last commit. A pass that pushes to another existing branch is not
  seen; that limit is listed (*Open findings*, K-1).
- **P-4. The pull request at X2.** §A names amthorn78/glow-hdengine-v2#581 as the pull request Nathan merges at
  X2. #581 was merged at `ANALYZED`, so X2's pull request is #583, this branch's. X5 counts #581's merge in
  `interaction_cost_actual`.

### What the plan settles

§A left these to `PLAN`.

- **The result codes:** `RUN_REVIEW_READY`, `RUN_STOPPED` and `RUN_NO_CHANGE`, as §A proposed.
- **The pass directory:** `passes/<key>/<NN>-<prompt>/`, one per pass, numbered per document, such as
  `passes/pf04-canon-hde-governance/01-tw-drain-10/`, where §A wrote `passes/<key>/<attempt>/`.
- **A draft's file name:** its canon file name with the version token replaced by the new version, so that
  taking it into canon moves one file and B4 can check the version against the name.
- **The pull request's state:** opened as a draft at B1, so every pass finds it open, and marked ready for review
  at B6 or on `RUN_NO_CHANGE`. A stopped run leaves it a draft.
- **A canon file that changes during a run:** checked before each pass. A changed target restarts its document
  at B2; a changed source, such as a new PF10 version, stops the run (S4).
- **A resume that changes the change, its sources or its governing specification:** a stop (S4), since that is a
  new run.
- **A capability the session lacks,** such as a reviewer with a fresh context for B5: a stop (S4).
- **The execution prompt** is kept as `inputs/execution-prompt.md`, so a resume can compare against it.

### How the plan runs

`EXECUTE` applies the steps below in order, and every step's check must pass before the next starts.

- **X1** makes the new page and reads it back (W1 to W3), then commits the handoff table.
- **X2** commits the record and pushes the branch. The handoff table is a repository file other than the record,
  so the mode returns `PRODUCT_OWNER_ACTION_PENDING` for Nathan's merge of #583.
- **X3**, after the merge, detects it by the file on `main` and re-runs the record checks from `main`.
- **X4** runs the drift check over the range since `ad1615d`, then updates the catalog in one write (W4): the new
  member's row, the members note, the *Approved design* entry and the checked-through commit.
- **X5** closes the record on the branch restarted from `origin/main`, with its own pull request.

**A stop.** A failed check or a tool error stops the run. Before W1, a failed precondition stops it with nothing
written, and it returns `IMPLEMENTATION_BLOCKED`. From W1 on, a failure takes `D26-B`'s path (*Failure path*),
and nothing more is written.

**Waiting for each write.** Every `notion-update-page` call is sent with `allow_async: false`. If a call still
returns an async task, the run polls it until it reports success, and only then makes the step's check. A task
that reports failure is a tool error, and the page is fetched again before anything else.

**Every text is sent exactly as written**, with the values substituted and nothing else changed. W3's text is
the draft with «V» in its first two lines, written by a script to a scratch file and sent whole. W4's texts are
printed from this section as committed, by script.

### Values

| Value | What it is, and when it is fixed |
|---|---|
| «D» | `EXECUTE`'s UTC date at X1.1, as `yyyy-mm-dd` |
| «V» | At X1.2: the new page's version, `MMDDYY` of «D» then `.1`, as the PE sets it for a net-new prompt. If «D» is 2026-10-06, «V» is `100626.1`. A child of the GTWPE parent page that already carries the new title is a collision and a stop (X1.0 (4)); the PE forbids incrementing to evade one |
| «T» | `GTWPE-FLOW-10 — Run the Technical Writing Flow — «V»`, the new page's title and first line |
| «ID» | At X1.3, the new page's ID as its duplication returns it, as 32 hex digits without dashes |
| «M», «m» | At X3: the commit on `origin/main` that brought `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`, in full and as its first seven characters |
| «S» | At X4.1: the UTC date, as `yyyy-mm-dd` |
| «HT» | Fixed in this plan: the sha256 of the handoff table as committed in the evidence directory (*Values fixed in this plan*) |

### Evidence files

In `docs/ephemeral/modifications/evidence/gtwpe-flow-manager/`, committed with this section:

| File | What it is |
|---|---|
| `gtwpe.handoffs.md` | The handoff table's exact text, which X1.4 copies byte for byte to `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md` |
| `PLAN-REVIEW-BRIEF.md` | PL3's review brief, committed before the reviewer is spawned |
| `PLAN-REVIEW.md` | The reviewer's return, captured unedited from its own transcript |
| `draft-repairs.json` | The repair round's nine changes to the draft, each as its old clause and new text exactly as applied, with the draft's line and character counts before and after. The draft itself is not in the repository |

### Values fixed in this plan

| Value | Fixed as |
|---|---|
| «HT» | `61aee2aeff2f351e9b51399bb5cb3bd9d019f998b120ad9f495fd1b52f4c2bef`, the sha256 of `gtwpe.handoffs.md`, 7,557 bytes, as *Repair round (PL3)* left it. The dry run's file was `d0d727c6…2315b`, 7,508 bytes |

### The new page

- **Title** «T». **Parent** the GTWPE parent page, *GTWPE — Glow Technical Writing Prompt Ecosystem*,
  `3ea4590a05eb818c915bdfd3d150c44b`, under *AI Prompts / HDE TW*. **Icon** none.
- **Duplicated page** *GTWPE Target Architecture — Document-Writing Flow*, `3ea4590a05eb81f7988bd032dfdccfb5`,
  edited 2026-10-05T16:16:17.223Z at this mode's fetch. It is never edited, and its edit time is checked
  unchanged after W1 and after W3.
- **Body** the reviewed draft, 255 lines, sent whole in W3 with «V» substituted in its first two lines and
  nothing else changed. Its first two lines are «T» and `Prompt Version: «V»`; its third begins `Operator note:`.
- **Headings, in order (20):** `# Run the Technical Writing Flow`; `## Purpose`; `## Authority and limits`;
  `## The execution prompt`; `## Sources and reading`; `## Eligibility and routing`;
  `## The run's branch, pull request and directory`; `## RUN.md`; `## Passes`; `## The flow`; `### B1 Scope`;
  `### B2 Redlines`; `### B3 Drafts`; `### B4 Document control`; `### B5 Consistency`; `### B6 Complete`;
  `### Redo from canon`; `## Proof logs (GTWPE-D1)`; `## Stop and resume`; `## Results`.
- **Last words:** "It names no other prompt to run."
- **Where each item lands in the body:**

| Item | Sections |
|---|---|
| ITEM-01, the flow | *Purpose*; *Authority and limits*; *Passes*; *The flow*, B1 to B6; *Redo from canon* |
| ITEM-02, the run's layout | *The run's branch, pull request and directory*; *RUN.md* |
| ITEM-03, stop and resume | *Stop and resume*; *Passes*, "One date for a drain and its apply"; S1's sizing |
| ITEM-04, the execution prompt | *The execution prompt*; *Authority and limits*, last bullet |
| ITEM-05, eligibility and routing | *Eligibility and routing* (with P-1) |
| ITEM-06, GTWPE-D1 in a run | *Proof logs (GTWPE-D1)*; *Passes*, check 5; B6 step 2 |
| ITEM-07, E-006, E-016, E-022 | *Passes*, "After each pass"; B1 step 3 and B6 step 3; B6 step 4; *Sources and reading*, third bullet |
| ITEM-08, the handoff table | Not in the body: `gtwpe.handoffs.md` (X1.4) |
| ITEM-09, maintenance before C6 | Not in the body: the catalog's row and note (W4). The body resolves the TW prompts from the TW selection page |

### The new page's checks

What X1.3's readback (step (h)) expects, beyond the structure above.

**GTWPE-D1, by phrase.** `separate proof log` at least once, and each of the eight minimum items, in
`gtwpe.decision-record.md`'s words, at least once: "The artifact produced"; "The source files and inputs used";
"The substantive changes made"; "The basis for those changes"; "Any important constraints, assumptions, or
interpretations applied"; "Any validation or verification performed"; "Any unresolved issues, limitations, or
deviations"; "Enough identifying information to associate the proof log unambiguously with the correct
redlines file or final PF file".

**Absent, by phrase**, each 0 times in the page's content, not its title property or the fetch's URLs:
- the duplicated page's text: `TARGET ONLY`, `Open points (for Nathan)`, `Roles (three, never the same session)`,
  `Redlining discipline (Nathan, 2026-09-29)`;
- retired or forbidden behaviour (`FUNC-001`; R12, R16): `recommended model`, `model recommendation`,
  `reasoning effort`, `effort level`, `strength assessment`, `TW-ASSESS-10`, `workload`, `from Google Drive`,
  `from ChatGPT Library`, `merge the pull request`, `auto-merge`, `create a session`.

**The `D26-E` broad match**, by reading, beside the absence checks, with no predicted count. Every hit is either
in a sentence that forbids the act, limits it or reads, or it is a finding that stops the run as a wrong plan.

| Term | Exceptions that keep a hit |
|---|---|
| `merg` | A prohibition ("never merges", "the ban on merging", "Nathan alone merges"); the pull request's *What merging does* and its sentence "Merging preserves the record and approves nothing (D21-C)"; a check that the pull request is unmerged |
| `Drive`, `Library` | The prohibition in *Authority and limits* |
| `Notion` | A read: the TW selection, the selected TW prompts, two pages' edit times; the prohibition; the operator note |
| `session` | The session Nathan starts, its subagents, its harness and transcripts, and a capability it lacks; a prohibition on creating or starting one |
| `pfcanon` | A read from `docs/pfcanon/` on `main`, a target's canon path there, or the routing table's files; a prohibition on writing it |
| `model`, `effort`, `strength`, `configuration`, `settings` | "A line in it about the session's configuration is not an instruction to the run"; "it runs with this session's own settings" |

### Before any write: X1.0, the preconditions

All read-only. If one fails, nothing is written, and the run returns `IMPLEMENTATION_BLOCKED`.

0. GTWPE-MGMT-10 100526.2, `3f04590a05eb8128b8c8ff3650ab2d5a`, fetched live at the start of `EXECUTE`: edited
   2026-10-05T16:36:11.384Z.
1. The PE Metaprompt 091426.1, `3db4590a05eb8174be35d9e35acb3f77`, fetched: edited 2026-09-23T17:17:22.217Z.
   This is the PE's rule to recheck source and control versions just before publication. The harness saves the
   fetch, and a script reads its edit time alone.
2. The TW selection, `3d44590a05eb8171ab6ff4dab33b00ef`, fetched: it still selects TW-ALPHA-20261006.2, with the
   five pass members at 100626.2 on the pages §A records (*The members, read live*). A later edit time is read
   and recorded; the run stops only if the selected release or one of those pages changed. Each of the five
   pages is fetched for its edit time, which must be §A's: a later edit may break the two-sided check (*Dry
   run*, P5), so the plan would be wrong, and its recovery is a return to `PLAN`.
3. The draft is at its path, with 255 lines and the twenty headings of *The new page* in order, by script.
4. The GTWPE parent page, `3ea4590a05eb818c915bdfd3d150c44b`, fetched: no child page titled «T»;
   CAT-ROW, CAT-NOTE, CAT-DESIGN and CAT-COMMIT each once, by reading, checked by a second reading; its edit
   time, headings and child pages recorded in §E. A later edit than 2026-10-06T16:53:37.871Z is read and
   recorded; the run stops only if an old text is gone or occurs twice.
5. The architecture page, `3ea4590a05eb81f7988bd032dfdccfb5`, fetched: its edit time, its first line of content,
   its last heading and its last words recorded in §E, for W1's check.
6. `git fetch origin main` succeeds, and `origin/main` is recorded in §E. A change to a watched path since
   `ad1615d` is not a stop here; X4.1 records it.
7. The evidence file `gtwpe.handoffs.md` has sha256 «HT».
8. The record checked out holds this plan with `plan_approved_by` set.

### The steps

Four Notion writes, W1 to W4. The plan makes no other.

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| X1.1 | — | the record | Set the status to `EXECUTING`. Fix «D», and record it in §E with the UTC time, which starts the clock | GTWPE-MGMT-10 X1 | The values are in §E before X1.2 | None needed |
| X1.2 | — | — | The preconditions X1.0 (0) to (8); fix «V» and «T» | This plan | Each as X1.0 states it | None needed |
| X1.3 | PART-01 | `prompt` | **(a)** Fetch the GTWPE parent page: no child page titled «T». **(b)** **W1**: `notion-duplicate-page` on the architecture page; «ID» is the returned ID. **(c)** Fetch «ID» until populated: at most six fetches, the second onwards after a wait of about 20 seconds, run as a background `sleep 20`, since the harness blocks a foreground sleep. Populated means: its first line of content, its last heading and its last words are the architecture page's, as X1.0 (5) recorded them; its parent is the GTWPE parent page; and the fetch reports no truncation or unknown block. **(d)** **W2**: `notion-update-page`, `update_properties`, `allow_async: false`: title «T», and `icon: "none"`. **(e)** A script writes the draft, with the value of «V» in place of the two placeholders `«V»` in its first two lines and nothing else changed, to `GTWPE-FLOW-10-send.md` beside it, and checks that the draft has exactly two `«V»`, both in those lines, and that the two files differ in those lines only. **(f)** **W3**: `notion-update-page`, `replace_content`, `allow_async: false`, `new_str` the send file's text, whole, as read from the file | The prompt-page route, as F-2 applies it to a new member; ITEM-01 to ITEM-07; this plan's approval (`notion-write-boundary.md`) | **(g)** W1 returns an ID other than the architecture page's, and the copy is populated by the sixth fetch; otherwise stop (`D26-B`). W2 and W3 return success, or a task polled to success. **(h)** Fetch «ID» whole, into this session's context, and check it, every check by reading and checked by a second reading: (1) the title is exactly «T»; (2) the parent is the GTWPE parent page; (3) the icon is none; (4) the first two lines are «T» and `Prompt Version: «V»`; (5) the headings, in order, are *The new page*'s twenty; (6) each section's text is the send file's, read against it section by section, allowing only Notion's documented reversible representation changes, such as stripped blank lines, Markdown escaping and a table's spacing; (7) the page ends with *The new page*'s last words; (8) GTWPE-D1's requirement and eight items occur by phrase (*The new page's checks*); (9) each absent phrase occurs 0 times; (10) the `D26-E` broad match, each hit recorded in §E with the exception that keeps it; (11) the fetch reports no truncation or unknown block. **(i)** Fetch the GTWPE parent page: exactly one child page carries «T», and it is «ID»; its other child pages are those X1.0 (4) recorded. Fetch the architecture page: its edit time is X1.0 (5)'s. **(j)** Delete the draft and the send file with `rm`, exit 0. A failed check stops the run (`D26-B`); a hit in (10) that says what the body must not say is a wrong plan (*If the plan is wrong*) | Before X4, Nathan archives the new page. The architecture page is never touched. Neither needs a copy of a body |
| X1.4 | PART-01 | `rule` | `cp` the evidence file `gtwpe.handoffs.md` to `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`; commit it with the record | The repository route for a procedure file; ITEM-08 | Its sha256 is «HT»; `git diff --name-only origin/main...HEAD` lists only the record, its evidence and this file; the `D26-E` search for old text the move contradicts, `git grep -n -i -e 'handoff table' -e 'design v1.2 §6' -- docs/prompt_ecosystem_management/` finds hits only in the new file (P9) | Before the merge, a commit on the branch removes the file. After it, a new Modification reverses it |
| X2 | — | the record | Commit the record with X1's values and dispositions. Run `gtwpe_record_check.py` and `modification_validate.py` on it at `EXECUTING`; push. Update #583's title and description. Return `PRODUCT_OWNER_ACTION_PENDING` for Nathan's merge of #583, ending `IN FLIGHT` | GTWPE-MGMT-10 X2 ("If a part changed a repository file other than the record and its evidence ... push the branch, open its pull request, and return") | Both checks exit 0; after the push, the branch's blob of each changed file equals the local file; #583 is the branch's one open pull request | Before the merge, as X1.4 |
| X3 | — | — | Only after Nathan's merge, in this session or a fresh one started from `main`: `git fetch origin main`; detect the merge by files on `main`, never by commit subjects (`D26-C`); fix «M» and «m»; run both record checks on the record as `main` holds it | GTWPE-MGMT-10 X3 | `git rev-parse origin/main:<path>` equals the branch's blob for the handoff table, the record and each evidence file; «M» is `git log -1 --format=%H origin/main -- docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`; both checks exit 0 | A new Modification reverses the file |
| X4.1 | — | — | Fix «S». `git log --format='%H %cI %s' ad1615d..«M»` over *The watched sources*, leaving out this Modification's own files. For each commit, a trigger finding in §E with its `D26-E` search: the change's own terms in 100526.2 as fetched at X1.2 and in `docs/prompt_ecosystem_management/gtwpe/` at «M», each with its count | GTWPE-MGMT-10 X4; §A *Drift check*, which examined through `ad1615d` | Every commit the log lists has a trigger finding in §E. A change that contradicts the GTWPE is recorded for Nathan and does not stop the run. A0 found no lineage trigger, so nothing is re-pinned | None needed |
| X4.2 | PART-01 | `notion_control` | **W4.** The GTWPE parent page. Pre-read: fetch it; CAT-ROW, CAT-NOTE, CAT-DESIGN and CAT-COMMIT each once, by reading; record its edit time, headings and child pages in §E. Then `update_content`, `allow_async: false`, four replacements in one call, in this order: CAT-ROW, CAT-NOTE, CAT-DESIGN, CAT-COMMIT, each to its new text (*The catalog texts*) | GTWPE-MGMT-10 X4 ("set the checked-through commit"; the catalog's row for a new member); ITEM-08 and ITEM-09 | Fetch it again, by reading, checked by a second reading: (1) the members table has two rows, GTWPE-MGMT-10's as the pre-read showed it, and below it GTWPE-FLOW-10's, its page cell in the rendered form *The catalog texts* gives; (2) CAT-NOTE-NEW, CAT-DESIGN-NEW and CAT-COMMIT-NEW present as sent, and CAT-NOTE, CAT-COMMIT and the first-row-only table absent; (3) by reading, `§6` and `handoff` occur only in CAT-DESIGN-NEW; (4) the page's opening paragraph, the catalog's own opening, the lineage pins, the *Recorded on 2026-09-29* paragraph, the five headings and the child pages as the pre-read showed them | The reverse replacements, with their texts taken from this readback, never from page history |
| X5 | — | the record | Record every step's and item's disposition. ITEM-01 to ITEM-07 are `VERIFIED` when X1.3 (h) passed; ITEM-08 when X1.4 and X3 passed; ITEM-09 when X4.2 passed. Record `interaction_cost_actual` against 7, with #581's merge at `ANALYZED`; the actual author, checker and acceptor of the part (HDE Governance §9.1.6); and the time on the clock. Set the status to `COMPLETE`. Restart the branch from `origin/main`, since X2 waited for a merge; commit the record and push; open its pull request. Return `ECOSYSTEM_CHANGE_COMPLETE` with X4.1's trigger findings | GTWPE-MGMT-10 X5 | Both checks exit 0 at `COMPLETE`; after the push, the branch's blob equals the local file; `git diff --stat origin/main...HEAD` lists only the record | — |

### The catalog texts

Catalog text, quoted in full. It is page state, not a prompt body. Each old text occurs once on the GTWPE parent
page (*Dry run*, P6). A mention is compared by its link, since Notion shows a linked page by its title.

**CAT-ROW**, the members table's last line and its close:

```
`3f04590a05eb8128b8c8ff3650ab2d5a`</td>
</tr>
</table>
```

**CAT-ROW-NEW** adds GTWPE-FLOW-10's row:

```
`3f04590a05eb8128b8c8ff3650ab2d5a`</td>
</tr>
<tr>
<td>GTWPE-FLOW-10</td>
<td>«T»</td>
<td>«V»</td>
<td><mention-page url="https://app.notion.com/p/«ID»"/> `«ID»`</td>
</tr>
</table>
```

Read back, Notion renders the new page cell with the page's title inside the mention, as C1's X4.2 found:

```
<td><mention-page url="https://app.notion.com/p/«ID»">«T»</mention-page> `«ID»`</td>
```

**CAT-NOTE**, the members note:

```
Further members are added as the approved build selects them: the Flow Manager (a new prompt) and the TW prompts the build extends (*Approved design*). Design v1.2's GTWPE-RUN-10, GTWPE-RECORD-10 and GTWPE-RECORD-20 are not built.
```

**CAT-NOTE-NEW:**

```
GTWPE-FLOW-10, the Flow Manager, joined on «S» (MODIFICATION-20261006-gtwpe-flow-manager). Listing it adopts nothing: it runs only when Nathan starts it, and it runs the TW prompts as the *Glow Technical Writing Ecosystem* page selects them. The TW prompts join as the approved build selects them (*Approved design*). Design v1.2's GTWPE-RUN-10, GTWPE-RECORD-10 and GTWPE-RECORD-20 are not built.
```

**CAT-DESIGN**, the end of the *Approved design* entry:

```
`docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.2.md`, approved by Nathan at G1 on 2026-09-29, still applies.
```

**CAT-DESIGN-NEW:**

```
`docs/ephemeral/gtwpe.rewrite/design/GTWPE-DESIGN-v1.2.md`, approved by Nathan at G1 on 2026-09-29, still applies. Its §6 handoff table is replaced by the GTWPE's handoff table, `docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md` (MODIFICATION-20261006-gtwpe-flow-manager).
```

**CAT-COMMIT**, the checked-through commit:

```
`b1bd7699243395a708a1d49a82df7e0b61efcccb` (`b1bd769`), examined by `EXECUTE` of MODIFICATION-20261006-gtwpe-tw-document-rules on 2026-10-06.
```

**CAT-COMMIT-NEW:**

```
`«M»` (`«m»`), examined by `EXECUTE` of MODIFICATION-20261006-gtwpe-flow-manager on «S». Before it, `b1bd769`, examined by `EXECUTE` of MODIFICATION-20261006-gtwpe-tw-document-rules.
```

The lineage pins do not change: A0 found no trigger, and X4.1 records any later one for Nathan.

### Failure path (`D26-B`)

From W1 on, a failed check or a tool error stops the run, and nothing more is built or written:

1. **A failure record** in §E. It holds every step's disposition and the failed step with its evidence, and marks
   the steps after it `NOT_RUN`, citing the stop. It is committed and pushed, and reaches `main` in #583 before
   X2's merge, or after it in a record-only pull request from the branch restarted at `origin/main`. Nathan
   merges it although the record is not `COMPLETE`: the failure-record exception of his merge rule.
2. **A read-only sweep** of what landed, after every pending task has been polled to its end: the GTWPE parent
   page with its child pages, «ID» if it exists, the architecture page and the branch with #583, each read once,
   and what each now says recorded in §E.
3. **The freeze kept:** no further Notion write. The part, having applied steps, is `BLOCKED` with its applied
   steps named, and the Modification stays `EXECUTING`.
4. **A return to Nathan**, `IMPLEMENTATION_BLOCKED`, ending `DECISION NEEDED`. Before X4, he archives the new
   page, or a copy titled with the architecture page's title that W1 left. W4 is reversed only when its own check
   failed, by its reverse replacements, with the texts taken from its readback, made by Nathan or at his
   direction. No page is restored from its history, and no rollback needs a copy of a prompt body.

### Open findings, accepted as risks

Approving this plan accepts each of these (`DISP-001`).

| # | Finding | Likelihood | Consequence | Why listed, not repaired |
|---|---|---|---|---|
| K-1 | P-3's check of the remote does not see a pass push to another existing branch, and B6's Notion check sees only two pages (§A risk 11) | Very low: every TW prompt pushes only to the branch its invocation names | An unauthorized write unseen by the run | §A's wording would stop runs that did nothing wrong whenever another branch moved; the limit is stated in the body |
| K-2 | B6's Notion check stops a run when another session edits *HDE TW* or the GTWPE parent page during it | Low | A loud stop; Nathan resumes | §A's check, kept as approved; a resume costs little |
| K-3 | W3 sends a 27,497-character body; a transcription or rendering fault is found only by the readback, which compares by reading | Low | A loud stop at X1.3 (h)(6); Nathan archives the page | `D22` forbids a byte comparison of a body; the readback is read twice, and Nathan and PE39 read the page live before the first trial |
| K-4 | CAT-ROW-NEW adds a row by replacing a table's closing lines; no earlier GTWPE write has added a table row | Low | A refused call writes nothing; a malformed table fails X4.2's check | A loud stop with its reverse replacement |
| K-5 | The reviewed draft's identity before W3 rests on this session alone: no fingerprint binds it, since a body is never hashed (§A risk 1) | Low | A changed draft would be published | Only this session writes the scratchpad; X1.0 (3) checks its structure; the readback and Nathan's live reading follow |
| K-6 | A run reads each TW prompt's selected version as each pass starts, so a run during a TW release change mixes versions | Low: a TW release changes only through GTWPE-MGMT-10 | `RUN.md` shows two versions of one prompt | Recorded per pass; design v1.2 §6's "a run started under one GTWPE version finishes under it" is not carried by §A |
| K-7 | No executable check exists for TW or for this prompt, and its first run is Nathan's trial (§A risk 7) | Medium | A runtime fault is found in use | The gate is static: P5's two-sided check; the trial is Nathan's, after C4 |
| K-8 | The phrase checks see phrases, not meaning (§A risk 14) | Low | A text that keeps a phrase while weakening its rule passes the readback | The review reads for behaviour; the readback also reads the page against the reviewed draft |
| K-9 | The gate's example, `BN 13.5` for PF10 v13.5, names today's PF10 version, as TW-APPLY-10's does | Certain | The example ages as PF10 moves | It shows the form; the rule is the PF10 version used |
| K-10 | §A's other risks: 2 (the copy's title in W1's window), 3 and 4 (one writer; a redo from canon), 5 (S1 rests on the session's judgement), 6 (`glow-write-boundary`'s "Open the PR when the session's work is done"), 8 (no advice for a downstream session), 9 (E-010), 10 (the table restates the bodies), 12 (capturing a review), 13 (one reader of the bodies) and 16 (drain ordering) | As §A states | As §A states | Approved with the analysis |
| K-11 | §A's findings P-1 to P-4, and this plan's going on past them where template rule 1 says to return to Nathan | Certain | Four inexact statements in the frozen analysis | None changes the scope, an item or a member; *Findings on §A* records each, and each goes to Nathan with this plan |
| L1 | *Resume* does not read the two Notion edit times again, so an edit made while a run is stopped, such as a GTWPE Modification's X4, stops it at B6 (S6) on every resume | Medium | A loud stop that no named decision clears | Listed by the reviewer: a loud stop. Nathan may opt in |
| L2 | A canon source that changes during a run stops it (S4), and every resume then fails the same check | Medium for runs over several sessions | A loud stop; the way on is a new run | A loud stop |
| L3 | B1 step 1 records the intake commit before step 2 sends `RESUME` to *Resume* | Low | Silent if a session re-bases; *Resume*'s check of each base blob against `RUN.md` still sees a changed canon file | Low, and *Resume* reads `RUN.md` |
| L4 | B6 does not check the base blobs again before marking the pull request ready | Low | A draft whose base changed during B5, its base blob shown in the description | Not one of the four required kinds |
| L6 | The diagnostic cycle has no count bound when each attempt fails differently | Low | Loud; only S1 ends it | A loud stop |
| L7 | Check 3 after a pass needs a list of the remote's branches taken before it, which *Before each pass* does not take, and it stops a clean run when another session creates or deletes a branch | Medium | A loud S6 | A loud stop. Nathan may opt in |
| L8 | §P goes on past P-1 to P-4 where template rule 1 says to return to Nathan (K-11) | Certain | Procedural; disclosed | Each goes to Nathan with this plan |
| L9 | A change to an existing PF30 record proceeds with no authorization in the execution prompt, as §A routes it | Medium | A PF30 update Nathan did not ask for, visible to him at review | §A settles the route; not silent |
| L10 | B4 check 4 omits the drains' rule that a PF30 material-change row's date keeps its decision-date meaning | Medium for PF30 updates | Loud: a stop (S5) after one redo | A loud stop. Nathan may opt in |
| L11 | B6 step 1 lacks B4 check 5's exception for language canon requires, as in a template or a record kept as history | Medium | A loud stop, or an inexact `RUN.md` record | A loud stop |
| L12 | A rollover's review copy of the next volume has no base version, so B4 check 1 cannot pass it | Likely on a rollover | A loud stop (S5) | Rollover only, on Nathan's decision |
| L13 | A draft's file name needs the new version before the pass derives it | Low | A loud stop (S5) | A loud stop |
| L14 | B5 step 2's "never retyping it" names no way to capture the return | Medium | A captured review that differs from the reviewer's return | Not one of the four required kinds: the run acts on the return it holds |
| L15 | The body omits GTWPE-D1's sentence that a proof log "should provide enough evidence for another session or reviewer"; B6 checks the eight items, as ITEM-06 asks | Low | A thin proof log passes | The passes carry that sentence, and write the proof logs |
| L17 | P13's `merg` count of 7 is case-sensitive; read case-insensitively it is 9, both extra hits within the exception for "Merging preserves the record and approves nothing (D21-C)" | Certain | None | A dated count |
| L18 | W3's text is sent by retyping, and once X1.3 (j) deletes the draft nothing can be compared with the reviewed text (K-3) | Low | A slip only (h)(6)'s readings would see | Accepted as K-3 |
| L19 | Untested until `EXECUTE`: W2's icon removal, what duplication does to the original, CAT-ROW's three-line old text, and how Notion renders a placeholder in a table cell | Low | A loud `D26-B` stop | A loud stop |
| L20 | F5's "any other failure" omits the body's retries for `PARTIAL_PACKAGE` and for `BLOCKED` with an input the run holds; its first half, F3's missing S4, is met by R-1's repair | Certain | Low; closure is unaffected | Not one of the four required kinds |
| L21 | The same-date rule drains again every document applied on a later date, though only a format that records a revision date needs it | Medium for runs over several days | The cost of a drain | The safe rule; not one of the four required kinds |
| L22 | The invocation does not state E-006's bound on what a pass may write; it rests on each TW prompt's output rule and the checks after the pass | Low | A stray write the run does not see | §A's design, with its limits stated (K-1) |

### Product Owner actions

| # | Action | How it is verified |
|---|---|---|
| PO-1 | Approve this plan. It authorizes W1 to W4 and nothing else in Notion (`notion-write-boundary.md`), made from the session that runs `EXECUTE` of this plan, which is this one (HDE Build Notes, PF10-AINEUTRAL-001) | His words go into `plan_approved_by` with the date; the validator refuses `EXECUTING` without them |
| PO-2 | Merge amthorn78/glow-hdengine-v2#583 at X2, with the handoff table and the record at `EXECUTING`: the exception of his merge rule for the pull request the plan opens | X3 detects it by files on `main` |
| PO-3 | With PE39, read the published page live before the first trial | Theirs; nothing in this Modification waits on it |
| PO-4 | Merge the record's pull request after X5 when he chooses | Nothing waits on that merge (`D21-C`) |
| PO-5 | Only after a failure: archive the new page, or W1's copy; merge the pull request carrying the failure record | The read-only sweep, after he acts |

### Explicitly not in scope

- C5, the Change Manager; C6, adoption, with E-033 and the retirement of `tw-flowmaster`; E-041, PE39's after C4.
- F-1, F-2 and F-3, and E-035's count-by-script candidate, for a later GTWPE-MGMT-10 repair; E-010, which stays
  Nathan's; a PF20 volume rule, until Nathan splits PF20.
- Any change to a TW prompt, to GTWPE-MGMT-10, to the selection page, *Alpha 1*, *HDE TW*, the Operations Hub or
  the architecture page.
- Any change to the catalog beyond W4's four texts.
- The first live trial, which is Nathan's after C4.
- Any change to canon.

### Dry run (PL3)

Every normal-path gate and readback of this plan that can run before `EXECUTE`, read-only, by this session,
before any full review. Counts over the draft were made by a script that printed only counts, positions and the
last words; the TW bodies, GTWPE-MGMT-10 and the catalog were read in this session's context.

| # | Gate or readback | Result |
|---|---|---|
| P1 | Both record checks on a scratch copy of this record at `PLANNED`, with this round in `reviews`: `modification_validate.py` and `gtwpe_record_check.py` | Both exit 0, 1/1 each |
| P2 | The front matter parses (PyYAML); `analyze_approved_by` quotes Nathan's message exactly, read by script from this session's transcript; the request is unchanged; every table in the record has one column count in every row, by script | Parses; the approval is verbatim, 1,177 characters; the request is verbatim; every table consistent |
| P3 | A0 reproduced at `601b330`: `git log ad1615d..origin/main` over *The watched sources* | Empty. The range's two commits, #581 and #582, change `docs/ephemeral/` only |
| P4 | The live reads at this mode's start: GTWPE-MGMT-10 100526.2, the five pass members, the TW selection, the GTWPE parent page, the architecture page and the PE Metaprompt | Each edit time unchanged: 100526.2 2026-10-05T16:36:11.384Z; TW-DRAIN-10 16:39:55.231Z, TW-DRAIN-20 16:45:43.111Z, TW-RECORD-10 16:47:37.162Z, TW-RECORD-20 16:49:11.220Z and TW-APPLY-10 16:50:52.240Z, all 2026-10-06, as §A recorded; the selection page 2026-10-06T16:54:30.403Z, still selecting TW-ALPHA-20261006.2; the GTWPE parent page 2026-10-06T16:53:37.871Z; the architecture page 2026-10-05T16:16:17.223Z; the PE Metaprompt 2026-09-23T17:17:22.217Z |
| P5 | The two-sided check: every input each pass's prompt requires is in the body's invocation, and every return it gives is consumed (*The two-sided check*, below) | Every requirement is met and every return consumed; no TW prompt needs to change |
| P6 | The catalog's old texts on the GTWPE parent page as fetched at P4, by reading, checked by a second reading | CAT-ROW, CAT-NOTE, CAT-DESIGN and CAT-COMMIT once each |
| P7 | The new title is free under the GTWPE parent page | Five child pages: the four GTWPE-MGMT-10 versions and the architecture page. None is a GTWPE-FLOW-10 page |
| P8 | The draft, by script | 253 lines, 26,553 characters; the twenty headings of *The new page*, in order; two `«V»`, both in lines 1 and 2, and no other `«…»` value; each absent phrase 0 times; `separate proof log` and each of the eight items once; no character Notion escapes outside inline code and the table tags; the last words as *The new page* gives them |
| P9 | The handoff table: its rows H11 to H13 against design v1.2 §6, by script; the `D26-E` search X1.4 repeats, on `main` | H11, H12 and H13 identical to the design's rows. `git grep -n -i -E 'handoff table\|design v1.2 §6'` over `docs/prompt_ecosystem_management/` at `601b330`: no hit, so no repository text names design §6 as the GTWPE's handoff table; after X1.4 the new file is the only hit |
| P10 | The PE's compatibility check of a new Glow prompt against PF03, PF06 and PF10 (*The PF03, PF06 and PF10 check*, below) | Compatible; no conflict |
| P11 | §A's *What each rule becomes*: each of R1 to R18 and the four canon rules found in the draft, by reading | Each found where §A places it, with P-1 and P-2 (*Findings on §A*) |
| P12 | The draft uses only Notion-flavored Markdown that the spec read at this mode's start supports: headings to level 3, paragraphs, bulleted and numbered lists with no nesting, bold, italics, inline code and `<table>` blocks with `header-row` | Yes |
| P13 | The broad match of *The new page's checks*, run on the draft by reading | Every hit is within its exceptions: `merg` 7, `Drive` 1, `Library` 1, `Notion` 11, `session` 16, `pfcanon` 6, `configuration` 1, `settings` 1, and `model`, `effort` and `strength` 0 |

No required defect. Before this dry run, the session's own review of the draft made fourteen repairs to the
draft's text, all before anything was committed; none changes what §A settles.

#### The two-sided check (P5)

Each requirement is quoted from the prompt's live body by its shortest clause.

| Prompt | It requires or returns | The body meets it in |
|---|---|---|
| All five | Runs "directly or through a session he started that runs this prompt as a pass" | *Authority and limits*; invocation item 2 |
| All five | "An invocation that names no such path or branch is a missing input" | Invocation items 6 and 7, in every invocation |
| All five | "that branch then has one open pull request, opened if none is" | B1 step 6 opens it before any pass; check 4 after each pass |
| All five | "Use the target/volume the invocation assigns" | Invocation item 4 |
| TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10 | "Confirm exact prompt/version, target baseline" | Invocation items 1 and 4 |
| All five | "establish distinguishable actual output filenames from the target/source version, exact selection and run identity" | Invocation item 3, the pass identity; one directory per pass |
| All five | "An unrelated collision is a blocker for that name; do not overwrite it" | No copy ahead of a pass; *Redo from canon* moves a superseded draft first |
| All five | "A filename or an attachment mentioned in another session does not prove access here" | Attached inputs are committed under `inputs/` at B1 and passed by repository path |
| All five | "each output's repository path, with the commit that holds it" | *Its return*; the checks after each pass |
| TW-DRAIN-10, TW-DRAIN-20 | "Minimal operator input is the assigned target PF and the incoming source" | Invocation items 4 and 5 |
| TW-DRAIN-10, TW-DRAIN-20 | "Nathan may optionally select agendas/sections and provide relevant supporting material" | Item 5: the boundary only where the execution prompt sets one; supporting material |
| TW-DRAIN-10, TW-DRAIN-20 | When the source is PF10, "resolve `PF10-HDE-Build-Notes` in `docs/pfcanon/` on `main`" | Item 5: PF10 by its path on `main` |
| TW-DRAIN-10, TW-DRAIN-20 | Return `READY`, exactly `no redlines`, or `BLOCKED`; `COMPLETE_PACKAGE` or `PARTIAL_PACKAGE` | *Its return*: each consumed |
| TW-DRAIN-10, TW-DRAIN-20 | For `READY`, carry "exact original, the completed redlines file and its proof log by repository path, selected scope, producer validation status and source-file header provenance" | TW-APPLY-10's invocation |
| TW-DRAIN-10, TW-DRAIN-20 | "On a returned Apply diagnostic, preserve original/package/originating-session lineage" | *Its return*: a new drain pass carrying the diagnostic, the package and the earlier pass's identity |
| TW-DRAIN-10, TW-DRAIN-20 | "Ask one focused question only when an essential choice, identity or selected boundary cannot be established" | *Its return*: a question is a stop (S4) |
| TW-APPLY-10 | "minimal inputs are the exact original PF, the earlier redlines and their proof log" | Item 4, the target's canon path and base blob; TW-APPLY-10's own line |
| TW-APPLY-10 | "If the original changed after preparation, require reconciliation by the preparer" | *Before each pass*: a changed target restarts at B2 |
| TW-APPLY-10 | Two files "at the repository path the invocation names"; a diagnostic "at the repository path the invocation names" | Item 6: `pf-canon-drafts/` with the file name; the pass directory for a diagnostic |
| TW-APPLY-10 | A package whose change-history entry disagrees with its execution date goes back to the preparer | *One date for a drain and its apply* |
| TW-APPLY-10 | "Only when Nathan explicitly requests a no-change report" | Never requested: `no redlines` is recorded |
| TW-RECORD-10 | "the approved Epic specification and the relevant additional material Nathan supplies" | TW-RECORD-10's line; *Eligibility and routing*, the run's Epic Specification |
| TW-RECORD-10 | "establish that actual completed/historical posture from supplied evidence"; otherwise "ask" | Its line carries the evidence; a question is a stop (S4) |
| TW-RECORD-10, TW-RECORD-20 | "every PF10 change that modifies, clarifies, supersedes or extends the approved specification" | Their lines: every applicable PF10 change; *Eligibility and routing*'s last bullet |
| TW-RECORD-10, TW-RECORD-20 | "Write the updated PF20" or "the updated PF30 volume at the repository path the invocation names", with its proof log beside it | Item 6 |
| TW-RECORD-20 | "the approved CRD specification, its actual specification-approval evidence" | TW-RECORD-20's line |
| TW-RECORD-20 | "Open a new volume only when the invocation carries his rollover decision", and the review copy "at the repository path the invocation names for it" | TW-RECORD-20's line: the decision and the path |
| TW-RECORD-10, TW-RECORD-20 | "If several real volumes leave placement ambiguous, ask Nathan"; a missing decisive input writes no updated file | A question or missing input is a stop (S4) |

Each line the body adds to an invocation is one a prompt's intake reads: the version and page (preflight), the
pass identity (output identity and the originating preparer), the branch's open pull request (the one-pull-request
rule), and the supporting material (the drains' optional material).

#### The PF03, PF06 and PF10 check (P10)

The PE requires "the mandatory complete PF03, PF06, and PF10 compatibility check" for a new Glow prompt. Design
v1.2 §1.1 recorded the complete check for the GTWPE's run prompt, at `0db3f0e`. Since then PF03 and PF06 have not
changed, and PF10 moved from v13.4.2 to v13.5. This mode read PF03 whole, PF06 §0.2, §0.6.10, §1.1.11 and
§3.5.2.8, and PF10's whole difference since `0db3f0e`, 185,681 bytes of diff: the version, "AI Agent sessions" in
its front matter, and addenda 2.32 to 2.38.

| Rule | Source | Where the body meets it |
|---|---|---|
| Read every relied-on source completely; a partial view is a retrieval failure; unknown stays unknown | Technical Writing Best Practices §3 | *Sources and reading*, first bullet; S2 |
| One canonical home; route by title; no condensed copy of owned canon | §3, §5 | The body routes to the TW prompts and names documents; it states only the workflow consequences it acts on |
| Claims of approval, application or merging only on direct evidence | §11, §12 | B6 step 5: the pull request claims no promotion, QA or acceptance |
| Document-control values change only on explicit authority | §7, §15.1 | The passes set them under their own standing authority; the Flow Manager edits no draft and checks them at B4 |
| Ask only when the answer changes the result | §12 | It recovers everything else; a question a pass asks goes to Nathan (S4) |
| The final editorial check | §14 | B6's completion standard, beside the passes' own checks |
| A canon edit is separate documentation work, and the Product Owner merges | Change Process Guide §0.2 | A run is its own pull request; Nathan alone merges |
| One-pass redline bundles | §0.6.10 | TW-DRAIN-10, TW-DRAIN-20 and TW-APPLY-10, unchanged |
| `ASK OK?` on an approval-submitted planning artifact | §1.1.11 | Not applicable: a run's pull request carries replacement documents, not a plan |
| Post-QA drain ordering | §3.5.2.8 | B1 step 5 |
| PF20 and PF30 entries only by separately authorized historical drainage | HDE Governance §9.1.1 | *Eligibility and routing*: only with Nathan's authorization |
| Canon is `docs/pfcanon/` on `main`; change-process documents in `docs/ephemeral/` | HDE Build Notes 2.29 | *Sources and reading*; the run directory |
| No HDE Build Notes locator in another PF | 2.30 | The passes; the Last Update Gate is not a citation (C3) |
| Header model-advice review retired | 2.31 | No such content |
| No required AI provider, product or model; the surface confers no permission | 2.38 | The body names none; a line about the session's configuration is not an instruction to the run |
| Specification format authority | 2.14 | PF27 only with a governing specification |
| Precedence; one logical base version; addenda scoped individually | §1 to §9 | The drains' own PF10 rules; the body passes PF10 by its path on `main` |

Addenda 2.32 and 2.35 to 2.37 record HDE-EPIC040's QA, and 2.33 and 2.34 govern QA plans and live vendor calls.
None sets a rule for a technical-writing run.

### Full review (PL3)

- **The reviewer.** One fresh general-purpose subagent, GTWPE-FLOW-MANAGER-PLAN-A, neither forked nor
  context-inheriting, as Nathan directed. Its only brief was `PLAN-REVIEW-BRIEF.md`, committed and pushed at
  `28f4037` before it was spawned, at about 18:50Z; it confirmed the brief's sha256 at that commit,
  `d38a3ddf9ff70067584116c3d93043872dba4e763913aae0bc05d8509b87bb9f`.
- **The run.** It reviewed §P at `43150c6` and read the draft whole, in place. It fetched nothing from Notion and
  wrote nothing. It reported two side effects that were not its acts: the repository's hook updating
  `.git/canon_relied_on_hook.json` after each shell command, and one harness save of canon text, HDE Governance
  §9.1, which holds no prompt body and which it did not read. It ran for about 38 minutes, and the harness
  reported 561,602 subagent tokens.
- **The capture.** Its return came back through the harness's `SubagentHandback` call. `capture.py` read the
  reviewer's own transcript, found by the path the harness gave for its agent ID, twice: first printing only the
  call's shape (one call, at transcript line 497, 19,680 characters), then writing its `message` to
  `PLAN-REVIEW.md`: 19,737 bytes, sha256 `1d1544809d2fd4ac146804ce391e334f0b4a9bdea8308935afe9b642fd3dd354`, the
  message and one final LF. Its first line, `2`, is its count of required findings, and it carries the
  `## Canon relied on` block the brief required.

**Result: 2 required findings, R-1 and R-2, and 22 listed, L1 to L22.** The session confirmed both, and confirmed
two of the listed findings as required under the fixed rubric's R1, so the round closes with four:

- **R-1** (R4 and R3), confirmed against the Change Process Guide §3.5.2.8 on `main`, the drains' "Read the
  entire incoming logical source by default" in the bodies read live, and the draft. A PF10 change the run holds
  back still reaches a pass inside the whole PF10 source: after Nathan's "leave it out", in a document triage did
  not link to the change, or in a document B5 adds. No check would see it.
- **R-2** (R3), confirmed against `D22` condition 5, "the session says in its report that it happened". A session
  that stops names no harness file that holds a prompt body, and only B6 names them.
- **L5**, confirmed by the session as R1, a defect on the normal success path that does not end in a loud stop.
  When every routed document returns `no redlines`, the run goes on through B5 and B6 and returns
  `RUN_REVIEW_READY` with no draft.
- **L16**, confirmed by the session as R1. X1.4's search, written in its table cell as
  `'handoff table\|design v1.2 §6'`, matches nothing when copied literally, so the step's check cannot tell a
  correct result from an incorrect one.

The other twenty listed findings stay listed (*Open findings, accepted as risks*).

### Repair round (PL3)

Each repair is the reviewer's smallest correction, or for L5 and L16 the session's smallest, and nothing else
changed. A script applied the draft's nine changes, each to a clause found once, and `draft-repairs.json`
records them: 26,553 characters before, plus 944, gives the 27,497 after. The repaired draft has 255 lines and 27,497 characters, with the same twenty headings and last words,
two `«V»` in its first two lines, each GTWPE-D1 phrase once and every absent phrase 0 times, by script.

| Finding | Where | Repair |
|---|---|---|
| R-1 | Draft, B1 step 5 | Adds: "His decision to leave it out is a selected boundary that excludes the change, and every invocation for those documents carries it" |
| R-1 | Draft, *Passes*, invocation item 5 | "the selected boundary only where the execution prompt or Nathan's decision sets one" |
| R-1 | Draft, *After each pass* | Check 6: "No redlines file, draft or proof log the pass wrote takes as a basis a PF10 change that `RUN.md` holds back, unless Nathan has directed that change drafted". A pass that took one stops its document (S4), as B1 step 5 does |
| R-1 | Draft, S4's row | "a held-back PF10 change, or a pass that took one as a basis" |
| R-1 | `gtwpe.handoffs.md`, F3 and F8 | Their returns name the new S4 stop, so that the table matches the body: F3 "(S3, S4 or S6)", which also meets L20's first half; F8 "A question, or a held-back PF10 change taken as a basis" |
| R-2 | Draft, *On any stop* | A stop records, as B6 step 4 does, "the harness files this session holds that carry a prompt body, and what became of each" |
| R-2 | Draft, B6 step 4; *RUN.md* | B6 names its files "beside those it records for the run's earlier sessions"; `RUN.md` holds those "of every session of the run (B6, and every stop)" |
| L5 | Draft, B3; *Results* | B3 ends: "If no routed document has a draft and none has stopped, the run ends as B1 step 7 does", returning `RUN_NO_CHANGE`; the result's row adds "by triage or by every drain's `no redlines`" |
| L16 | §P, X1.4 | The search is `git grep -n -i -e 'handoff table' -e 'design v1.2 §6' -- docs/prompt_ecosystem_management/`, with no pipe: no hit at `601b330`, and two in the new file's text. P9's row keeps the table-escaped form of the pattern the dry run ran as an alternation |

The repairs move three of §P's values: the draft's 255 lines, in *The new page* and X1.0 (3); its 27,497
characters, in K-3; and «HT», in *Values fixed in this plan*. A check of the repair's diff follows, as Nathan
directed for a review that finds a required defect.

### Harness files (`D22` condition 5), for `PLAN`

- **Inline fetches, held only in this session's transcript**, which the harness keeps and leaves to its teardown:
  GTWPE-MGMT-10 100526.2, once, at the mode's start; TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10, TW-RECORD-10 and
  TW-RECORD-20 at 100626.2, once each, for P4 and P5; the control pages: the GTWPE parent page, the TW selection
  and the architecture page; and Notion's Markdown specification, which is documentation.
- **A harness save:** the PE Metaprompt 091426.1's fetch, `mcp-Notion-notion-fetch-1791311000399.txt`, 76,839
  characters. Scripts printed its title, edit time and headings, then its sections outside the GCFPE overlay, in
  four slices, into this session's context for authoring. It was deleted with `rm` once that reading was done
  (exit 0). No save was hashed or compared as a body's identity.
- **The session transcript.** Nathan's approval needed his message, which only the transcript held. A script read
  it once and printed only the message's timestamp and length, never a tool result, and saved the message to
  `c4/c4_analyze_approval.txt` in the scratchpad.
- **The draft**, a prompt body authored in this session: `c4/flow10/GTWPE-FLOW-10-draft.md` in the scratchpad,
  never in the repository. Scripts over it printed only counts, positions and its last words (P8). X1.3 (j)
  deletes it once the page is read back.
- **The reviewer's transcript**, the output file the harness gave for its agent ID in this session's tasks
  directory. It holds the draft, which the reviewer read in place, as Nathan's approval named. `capture.py` read
  it twice for its one `SubagentHandback` call, at transcript line 497: first printing only the call's shape,
  then writing its message to `PLAN-REVIEW.md`. It is left to the harness's teardown.
- **Two side effects of the reviewer's run**, as it reported them, not its own acts: the repository's hook
  updated `.git/canon_relied_on_hook.json` after its shell commands, and the harness saved one oversized output
  of canon text, HDE Governance §9.1, as `bfywrv5le.txt`, which holds no prompt body.
- **Other scratch files**, in this session's scratchpad: PF10's difference since `0db3f0e` and a copy of PF06
  from `main` (canon, not prompt bodies); this section's drafts; `capture.py`; and the scripts that set the
  approval and read the transcript.

### Canon and rulings relied on, for `PLAN`

- **`AGENTS.md`:** the canon-first rule; canon is read-only; the CI-exempt paths; the pull request's headings and
  "Merging preserves the record and approves nothing (D21-C)".
- **Technical Writing Best Practices** (PF03), whole, for the compatibility check (P10).
- **Change Process Guide** (PF06) §0.2, §0.6.10, §1.1.11 and §3.5.2.8, the post-QA drain ordering.
- **HDE Governance** (PF04) §0.4, lowercase directories; §9.1.1, PF20 and PF30 entries only by separately authorized
  historical drainage, and merges as Nathan's; §9.1.6, prompt ecosystem governance, as §A applies it.
- **HDE Build Notes** (PF10), its whole difference since `0db3f0e`; 2.14, 2.29 PF10-CANON-001, 2.30 PF10-CITE-001,
  2.31 PF10-HDR-001 and 2.38 PF10-AINEUTRAL-001.
- **Rulings:** GTWPE-D1; in `gcfpe.decision-record.md`, `D21`, `D22` and `D26`; Nathan's target architecture with
  his answers 1 to 8 and his directions of 2026-09-29 and 2026-10-05; his eligibility rulings of 2026-09-28
  (design v1.2 §8.7); his instruction of 2026-09-25 (plan v1.2 §1), for P-1; his rulings of 2026-10-06 on the Last
  Update Gate; and his approval of this Modification's analysis, quoted in `analyze_approved_by`.
- **Controls:** `modification-template.md` 2.1; `reviewer-prompt-template.md`, its second template;
  `notion-write-boundary.md`; `prompt-body-content-policy.md`; the PE Metaprompt 091426.1's general rules; Notion's
  Markdown specification, for the body's form.
- **GTWPE-MGMT-10 100526.2**, as fetched at the start of this mode: *Entry contract*, *The spine*, `MODE = PLAN`,
  `MODE = EXECUTE`, *How each kind of target changes* and *The watched sources*.
