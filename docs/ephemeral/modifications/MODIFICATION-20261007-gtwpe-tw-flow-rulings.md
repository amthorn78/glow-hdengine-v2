---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261007-gtwpe-tw-flow-rulings
status: PLANNING
targets: [prompt, rule, notion_control]
gate_tier: 2
closure:
  upstream: [GTWPE-FLOW-10, TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-TRIAGE-10]
  downstream: [GTWPE-FLOW-10, GTWPE-MGMT-10, TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-TRIAGE-10]
  state_sharers: [TW-DRAIN-10, TW-DRAIN-20]
readiness: NEEDS_RULING
override:
  by: Nathan
  overrides: [readiness]
  reason: "Nathan, 2026-10-07, approving the analysis (Q-1, option (a)): he waives HDE Governance §9.1.6's interacting-skill readiness for tw-flowmaster for the new TW-ALPHA release. The grounds are those of §A's Q-1, option (a): GTWPE-FLOW-10 runs the TW prompts as passes, C6 retires the skill, and a Flowmaster run against the new release stops loudly rather than producing a wrong result. The selection page and the three notes say that tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run it. The validator's vocabulary has no narrower gate, so `readiness` names it; the record's readiness field is ANALYZE's advice and is unchanged."
interaction_cost_predicted: 11
interaction_cost_actual:
estimate:
  plan: "about 10 h, not counting waits for Nathan: the edits to eight bodies, as anchors and new texts, authored through the PE Metaprompt from this analysis, with each passage counted twice; the decision record's three entries and the handoff table's rows; the selection page's three writes, the three current-release notes and the catalog rows; and PLAN's dry run, with its two-sided check of every invocation against the bodies it reaches, one full review and at most one diff check. Tokens are not measured"
  execute: "about 5 h, not counting the waits for Nathan's merges: eight new pages, each duplicated, titled, edited and read back whole; the decision record and the handoff table committed, and their merge detected on main (X2, X3); the selection writes and the three notes, read back; the catalog (X4); and the record at COMPLETE (X5). Tokens are not measured"
item_count_at_approval: 8
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-10-07
    required_open: 0
    outcome: "By this session, read-only, before any full review: both record checks exit 0 on a scratch copy at ANALYZED; the front matter and every table parse, and the request is verbatim; A0 reproduces at 128836a; every member and control page is unchanged. It found and corrected, before the review: two scope counts (GTWPE-FLOW-10 has 20 sections; TW-DRAIN-20's ruling 1 reach is 9), two unstated exceptions, four quotations (66 of 66 repository quotations now found, and every Notion quotation by a second reading), F9 missing from the tier 2 list, and the D26-E search not yet run over gtwpe/. None left open"
  - mode: ANALYZE
    kind: FULL
    date: 2026-10-07
    required_open: 7
    outcome: "Two fresh reviewers, GTWPE-TW-FLOW-RULINGS-ANALYZE-A and -B, each handed only its committed brief's path, on cc6b923: A 1 required and 22 listed, B 3 required and 20 listed. The session confirmed all four required findings, and three listed ones as required under the fixed rubric's R1: 7 distinct required defects, RQ-1 to RQ-7 (S-6 narrowed his PF20 and PF30 rule; canon's closure timing; the Flowmaster waiver for the new release; triage closing an addendum; ITEM-01's sentence counts; pinned PF versions; known-wrong text left in two re-versioned members), each repaired in §A. The listed findings stay listed, each with its reason"
  - mode: ANALYZE
    kind: DIFF_CHECK
    date: 2026-10-07
    required_open: 0
    outcome: "One fresh checker, GTWPE-TW-FLOW-RULINGS-ANALYZE-DC, handed only its committed brief's path, on the repair diff cc6b923..a14fcf3: no required defect, RQ-1 to RQ-7 each fixed; 8 listed, DC-L1 to DC-L8, six of them in the repair's own text (D26-A rule 5's second signal), and DC-L4 refuted by the session. Required defects went from 7 to 0. The cap is reached, so §A goes to Nathan with every open finding listed"
items:
  - id: ITEM-01
    statement: "Nathan's rulings of 2026-10-07 on a run's inputs, on PF10 drainage and on PF20 and PF30 are explicitly documented, in his words, in the GTWPE decision record."
    source: "PE40-INIT-20261007.md, Nathan's rulings 1 to 3 (ruling 1: \"this needs to be explicitly documented\"); ERRORS.md E-044, E-045, E-046, E-052 and E-053, Nathan's words in each; ecosystem-change-management.md §2 step 1"
    disposition: ""
  - id: ITEM-02
    statement: "The only inputs to a GTWPE run, and to each of its handoffs, are files, attached or given by filename or repository path; no other context passes, at any phase, and this is clear in the Operations Hub."
    source: "PE40-INIT-20261007.md, Nathan's ruling 1; ERRORS.md E-045; GTWPE-TARGET-ARCHITECTURE-20260929.md, Nathan's answer 2"
    disposition: ""
  - id: ITEM-03
    statement: "Every PF10 addendum in a run's sources is drained, whether or not it states a drain target, and every PF document is updated on its context and scope."
    source: "PE40-INIT-20261007.md, Nathan's ruling 2; ERRORS.md E-044 and E-052, Nathan's rulings"
    disposition: ""
  - id: ITEM-04
    statement: "Part of the run is a prompt that evaluates the drain targets."
    source: "PE40-INIT-20261007.md, Nathan's ruling 2; ERRORS.md E-051"
    disposition: ""
  - id: ITEM-05
    statement: "PF20 and PF30 are updated as part of the run whenever a specification is involved, and not otherwise, each through its own special prompt and never through the redliner."
    source: "PE40-INIT-20261007.md, Nathan's ruling 3; ERRORS.md E-046, E-052 and E-053, Nathan's rulings; GTWPE-TARGET-ARCHITECTURE-20260929.md §6 and *Redlining discipline*"
    disposition: ""
  - id: ITEM-06
    statement: "The PF09 documents are assigned the right prompts."
    source: "PE40-INIT-20261007.md, Nathan's ruling 4; ERRORS.md E-047"
    disposition: ""
  - id: ITEM-07
    statement: "GTWPE-MGMT-10 takes its own request as the files that record it, with no other context in the handoff."
    source: "PE40-INIT-20261007.md, Nathan's ruling 1 (\"you may not pass arbitrary context in handoffs\"; \"this is very important at every phase\"); ERRORS.md E-048"
    disposition: ""
  - id: ITEM-08
    statement: "Every GTWPE member, including everything C1 to C4 published, is checked against Nathan's words and the live sources, and what is found wrong is fixed."
    source: "PE40-INIT-20261007.md, Nathan's ruling 5 and *Read this first*; ERRORS.md E-048"
    disposition: ""
parts:
  - id: PART-01
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06, ITEM-07, ITEM-08]
    class: B
    after: []
request: |-
  Run GTWPE-MGMT-10 — Manage the GTWPE — 100526.2 (Notion page 3f04590a05eb8128b8c8ff3650ab2d5a), MODE = ANALYZE.

  Request, on main:
  - docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md
  - docs/ephemeral/gtwpe.rewrite/ERRORS.md
  - docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md
requested_by: Nathan
analyze_approved_by: "Nathan, 2026-10-07: \"Nathan approves the analysis of MODIFICATION-20261007-gtwpe-tw-flow-rulings at b4219de (2026-10-07). ITEM-07 stays. S-1 to S-8 are accepted, including S-7 for PF10 changes to PF20 and PF30, which sets aside the architecture's §9 sentence \"The agent must not update PF20 or PF30 from PF10 alone\" for those changes (DC-L2). DC-L1: a drain's `no redlines` return stays exactly as it is, and the equivalence location stays inside the drain. Q-1: (a), waive HDE Governance §9.1.6's interacting-skill readiness for tw-flowmaster for the new TW-ALPHA release.\""
analyze_approved_date: 2026-10-07
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20261007-gtwpe-tw-flow-rulings

The GTWPE's technical-writing flow brought into line with Nathan's rulings of 2026-10-07: a run takes only
files as inputs, every PF10 addendum is drained through a triage prompt that is part of the run, and PF20 and
PF30 are updated through their own prompts whenever a specification is involved; with every member checked
again against his words.

## Intake

Not through triage. Nathan's request, copied verbatim in the front matter, gives three files on `main` and
nothing else. At `128836aef7d45ae9f8c8118d2c5ab025d5ec634a` (`128836a`), the commit this mode examines:

| File | Blob | Bytes |
|---|---|---|
| `docs/ephemeral/gtwpe.rewrite/PE40-INIT-20261007.md` | `d41c071617f10ff21f738ac5092a5bbcf6341e3c` | 9,306 |
| `docs/ephemeral/gtwpe.rewrite/ERRORS.md` | `515002cfa0d5d07d7c72bc7f674b583d0a7f702b` | 52,236 |
| `docs/ephemeral/gtwpe.rewrite/GTWPE-TARGET-ARCHITECTURE-20260929.md` | `be57ef3222ee7d4d533fabc66f1722670154d317` | 29,177 |

**What the request is.** Nathan's words, where these files record them. The files also carry text by PE37,
PE39 and PE40: PE39's handover around Nathan's quoted rulings, each ledger row's finding and disposition, and
the readings and status updates in the architecture record. This record uses that text only to find Nathan's
words and as claims to check against the live sources, never as the request (ruling 5; ledger E-048 and
E-054).

**The items.** ITEM-01 to ITEM-08 number the outcomes Nathan's words ask for, in the order of PE40-INIT's
rulings 1 to 5:

| Nathan's words, where recorded | Item |
|---|---|
| Ruling 1, "this needs to be explicitly documented"; rulings 2 and 3 are rulings of the same kind | ITEM-01 |
| Ruling 1: "the only inputs should be the filenames. Any other context will corrupt the run. this needs to be explicitly documented. you may not pass arbitrary context in handoffs", then "make sure this is clear in the operations hub. this is very important at every phase." (E-045) | ITEM-02, and ITEM-07 for GTWPE-MGMT-10's own request |
| Ruling 2: "Whether or not an addendum states an explicit drain target, it needs to be drained." E-044 and E-052: "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target." | ITEM-03 |
| Ruling 2: "part of this run is to have a prompt evaluate the drain targets." (E-051) | ITEM-04 |
| Ruling 3: "PF20 and PF30 must be updated as part of this. of course." E-046 and E-052: "If there is a spec involved, those docs are updated. if not, then not. its basic." E-053: "PF30 and PF20 DON't need the redliner. They should not need that step. They never have." | ITEM-05 |
| Ruling 4: "make sure the pF09 docs are assigned the right prompts too." (E-047) | ITEM-06 |
| Ruling 5: "I have to believe everything is wrong now." E-048: "So you did all of this wrong. Days wasted. Fix it" | ITEM-08 |

**Handed in, and not an item.**

| Row or text | Disposition |
|---|---|
| E-043, the TypeSafe ladder and the HD scoring script | Outside this prompt's route. Neither scoring skill runs or validates the TW flow or the GTWPE, so GTWPE-MGMT-10 may not change them (*What this prompt may change*). Returned to Nathan. PE40-INIT and E-043's own PE40 check both say it is redone only if he asks |
| E-049, E-050 | Fixed; PE40-INIT lists them for the record only |
| E-054 | Fixed. Its lesson binds this analysis: where Nathan's recorded words settle a question, a prompt's text or a canon reading that points elsewhere is a defect to fix, not an option to offer |
| The other rows marked `OPEN`: E-004, E-006, E-007, E-009, E-010, E-015, E-016, E-020, E-021, E-022 and E-033 | None carries a ruling of 2026-10-07, and each names its own route. §A records which of them this Modification's rulings bear on |

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE — 100526.2*,
fetched live at the start of the mode: edited 2026-10-05T16:36:11.384Z, the version the catalog selects. The
mode started at 2026-10-07T04:55:40Z, when Nathan's request arrived, with `main` at `128836a`. The record is on
`docs/20261007-modification-gtwpe-tw-flow-rulings`, the Modification's own branch, with its open pull request
amthorn78/glow-hdengine-v2#590. The session's harness had named another branch; nothing was pushed there, since
the next mode finds a record only on a `docs/*-modification-gtwpe-*` branch.

### Consult

- **Repository**, on `main` at `128836a`.
  - The three request files, whole (*Intake*).
  - C1 to C4's records: MODIFICATION-20261005-gtwpe-writing-side §A A.2, A.4, A.5 and A.6 and its approval;
    MODIFICATION-20261006-gtwpe-flow-manager's front matter, §A whole and §E's readback times. C2's and C3's
    records for their items, parts and estimates.
  - `CHECKPOINT.md` §8, Nathan's rulings of 2026-09-28; implementation plan v1.2 §1, the source of the PF27
    gate (ITEM-03).
  - In `docs/prompt_ecosystem_management/`: `modification-template.md` 2.1, `ecosystem-change-management.md`,
    `execution-and-delegation-model.md`, `notion-write-boundary.md`, `prompt-body-content-policy.md` and
    `reviewer-prompt-template.md`, whole; in `gcfpe.decision-record.md`, `D21`, `D22`, `D23`'s clarification on
    subagents, `D24` and `D26`, whole; `gtwpe/gtwpe.decision-record.md` and `gtwpe/gtwpe.handoffs.md`, whole;
    the headers of `gtwpe/gtwpe_record_check.py` and `modification_validate.py`, and the validator's `check()`.
  - `AGENTS.md` and `.github/pull_request_template.md`.
  - No `docs/*-modification-gtwpe-*` branch carries this ID (`git ls-remote`): the only such branch is C2's,
    `docs/20261005-modification-gtwpe-tw-repository-io`, whose record is `COMPLETE` on `main`. The ID is new.
- **Canon**, on `main` at `128836a`, unchanged since `fffadb5` (`git log` over `docs/pfcanon/`). Searched with
  `git grep` for the task's terms: `drain`, `addend`, `PF20`, `PF30`, `PF27`, `PF09`, `rollover`, `material
  update`, `historical drainage`, `prompt ecosystem`, `handoff`, `technical writing`, `redline`. Read in full
  where it governs; *Canon and rulings relied on*, at the end of this section, says what each is used for.
- **Notion, read-only.** GTWPE-MGMT-10 100526.2; GTWPE-FLOW-10 100726.1 and the six selected TW prompts
  (*The members, read live*); the GTWPE parent page and its catalog; the *Glow Technical Writing Ecosystem*
  page; *HDE TW*, *Alpha 1* and the Glow Operations Hub; the architecture page; the lineage sources and the
  register (A0); and searches on every member's ID, title and version and on TW's current release (A3).
- **Installed skills**, read for this task: `glow-write-boundary` and `glow-workspace-currency`.

### Drift check (A0)

`git fetch origin main`; the commit examined is `128836aef7d45ae9f8c8118d2c5ab025d5ec634a` (`128836a`),
amthorn78/glow-hdengine-v2#589's merge.

**(a) The lineage sources.** Searches with highlights off on `PE Metaprompt` and `GCFPE-MGMT-10` found no page
that the catalog does not record and that is newer than its record. The other PE Metaprompt hits are archived
predecessors dated 2026-09-12 and 2026-09-13; the other GCFPE-MGMT-10 hits are the archived `091326.1` and
`091326.2` and control or tracking pages. The selected `091426.1` page did not appear in the results (a search
can miss a page); it was fetched by its recorded ID. Each recorded page was fetched for its exact edit time. The
PE Metaprompt's fetch and the register's were saved by the harness and read by script (*Harness files*).

| Source | Recorded in the catalog | Found, by fetch | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1`, 2026-09-24T15:38 | 11:00:24.691Z; `091426.1` (`3db4590a05eb81d1bb64ebcb3ca8eb54`) at 15:38:34.295Z; the register selects it | None |
| PE Metaprompt | Pinned and selected: `091426.1`, 2026-09-23T17:17:22.217Z | 17:17:22.217Z; the register selects it (`3db4590a05eb8174be35d9e35acb3f77`) | None |

The register page was at 2026-09-23T17:43:39.489Z, the edit time the catalog records.

**(b) The watched paths.** `git log b65e918..origin/main` over *The watched sources* lists nothing. The range
holds five commits, amthorn78/glow-hdengine-v2#584 and #586 to #589, which change 22 files, all under
`docs/ephemeral/`.

No trigger finding. X4 re-pins nothing and moves the checked-through commit to the commit it examines.

### The members, read live

Each member was fetched whole into this session's context and read whole. Each edit time equals the one its
last recorded readback gives (C3's or C4's `EXECUTE`), so no member has changed since its selection. The
selection page selects TW-ALPHA-20261006.2 with the six TW prompts below.

| Member | Version, page | Edited |
|---|---|---|
| GTWPE-MGMT-10 — Manage the GTWPE | 100526.2, `3f04590a05eb8128b8c8ff3650ab2d5a` | 2026-10-05T16:36:11.384Z |
| GTWPE-FLOW-10 — Run the Technical Writing Flow | 100726.1, `3f24590a05eb81798286d600250655d6` | 2026-10-07T00:09:42.961Z |
| TW-TRIAGE-10 — Identify PF10 Drain Targets | 100626.1, `3f14590a05eb81789e16d978795db77d` | 2026-10-06T03:18:14.556Z |
| TW-DRAIN-10 — Prepare PF Document Redlines | 100626.2, `3f14590a05eb819f8390f5b92fc4c8ab` | 2026-10-06T16:39:55.231Z |
| TW-DRAIN-20 — Prepare PF09 Redlines | 100626.2, `3f14590a05eb81a58043d304b7452801` | 2026-10-06T16:45:43.111Z |
| TW-RECORD-10 — Create Epic History Section | 100626.2, `3f14590a05eb81d399a7c3ab1fd6fb66` | 2026-10-06T16:47:37.162Z |
| TW-RECORD-20 — Create CRD History Section | 100626.2, `3f14590a05eb81eaaf0cedac0de274b9` | 2026-10-06T16:49:11.220Z |
| TW-APPLY-10 — Apply Validated Redlines | 100626.2, `3f14590a05eb81daa3cfee9956585cd5` | 2026-10-06T16:50:52.240Z |

The control pages, by fetch:

| Page | Edited | Against its last recorded readback |
|---|---|---|
| GTWPE parent page, with the catalog | 2026-10-07T01:59:25.993Z | Equal to C4's X4 readback. Members: GTWPE-MGMT-10 100526.2 and GTWPE-FLOW-10 100726.1; checked-through commit `b65e918` |
| *Glow Technical Writing Ecosystem* (the selection page) | 2026-10-07T02:12:01.288Z | Equal to E-041's readback |
| *HDE TW* | 2026-10-07T02:12:11.957Z | Equal to E-041's readback; 38 child pages |
| *Alpha 1 — Implementation and Validation* | 2026-10-07T02:11:56.963Z | Equal to E-041's readback; 34 headings |
| Glow Operations Hub | 2026-10-07T04:23:05.337Z | Later than E-041's readback (02:11:59.113Z). Its top now holds the red callout PE40-INIT records; its *Current Glow TW release — TW-ALPHA-20261006.2* section reads as E-041 left it |
| *GTWPE Target Architecture — Document-Writing Flow* | 2026-10-07T02:13:39.342Z | Equal to E-041's readback |

### The check against Nathan's words (ITEM-08)

Every member, and every control the GTWPE reads, was checked against Nathan's words in the three request files
and against the live sources, rather than against C1 to C4's records or PE39's or PE40's statements. Where this
check reaches the same result as a ledger row's PE40 check, the row is cited; where it differs, it says so.
Quotations from prompt bodies are the clause at issue, from this session's live fetch, and the dry run checks
each against a second fetch.

#### ITEM-01. The rulings, recorded

`gtwpe.decision-record.md` holds one ruling, GTWPE-D1. None of Nathan's rulings of 2026-10-07 is recorded there
or in the architecture record (E-045 says the same for ruling 1). The GTWPE decision record is where a ruling
that governs the GTWPE across changes lives ("they outlive any one change or release"), GTWPE-MGMT-10 reads it
first, and a ruling is recorded before it is applied (`ecosystem-change-management.md` §2, step 1). So the
change adds, in his words, verbatim, with what follows from each, as GTWPE-D1 is written:

- **GTWPE-D2**, inputs: ruling 1, both of its quotations, whole.
- **GTWPE-D3**, PF10 drainage: ruling 2, both of its quotations, whole, the second being ITEM-04's "part of this
  run is to have a prompt evaluate the drain targets."; and E-044's and E-052's "all pf docs should be updated
  based on context and scope, not whether or not the addenda specify a drain target."
- **GTWPE-D4**, PF20 and PF30: ruling 3, both of its quotations, whole; E-046's and E-052's "If there is a spec
  involved, those docs are updated. if not, then not. its basic."; and E-053's "PF30 and PF20 DON't need the
  redliner. They should not need that step. They never have."

Recording them there binds C5 and C6 as well: the Change Manager writes the Flow Manager's execution prompt, so
GTWPE-D2 governs C5's output.

#### ITEM-02. Files only

Nathan's ruling 1 is about the run and its handoffs, and his answer 2 of 2026-09-29 gives the shape of a start:
he initiates the session "by instructing it to run the technical-writing flow prompt and provide the required
inputs", either "as attached files" or "as filenames or paths that already exist in the repository". The broad
match is every input contract and every handoff in the GTWPE (*Scope*). What reaches beyond files:

| Surface | What it takes or passes beyond files | PE40's check |
|---|---|---|
| GTWPE-FLOW-10, its operator note and *The execution prompt* | "names the change and its sources"; item 2, "The change: what is requested"; item 5, "the documents the change may affect; a selected boundary within the sources; other context; a run name; and Nathan's authorizations"; "A missing change or source stops the run at intake (S2)"; item 1's `RESUME <run-id>`; item 4's "or `none`" | E-045, confirmed |
| GTWPE-FLOW-10, *Authority and limits* | "A line in it about the session's configuration is not an instruction to the run": a line other than a file, tolerated | New |
| GTWPE-FLOW-10, *Eligibility and routing* | "only with Nathan's authorization of that record", twice; "only on Nathan's rollover decision in the execution prompt" | E-046 and E-045 |
| GTWPE-FLOW-10, *The run's branch, pull request and directory* | the slug "taken from the execution prompt's run name or else from the change"; "A run name already in use [OMITTED] is a stop (S4)" | New |
| GTWPE-FLOW-10, *Passes* | item 5, "the selected boundary only where the execution prompt or Nathan's decision sets one; and any supporting material"; item 7, "The run's branch, and its open pull request"; for TW-APPLY-10, "with the selected scope and the drain's producer validation status and source-file header provenance"; for the record prompts, "every applicable PF10 change, and Nathan's authorization of the record" and "his rollover decision"; after-pass check 6, "unless Nathan has directed that change drafted" | E-045 (in part) |
| GTWPE-FLOW-10, *B1* | step 4, "A document the execution prompt names is checked"; step 5, "unless the execution prompt carries Nathan's direction to draft it", and his decision as "a selected boundary that excludes the change, and every invocation for those documents carries it" | E-045, confirmed |
| GTWPE-FLOW-10, *Stop and resume* and *Results* | S2's "A missing change"; S4's "a run name is in use" and "a resume changes the change"; *Resume*, "with `RESUME <run-id>` in place of `RUN`, and any decision he is giving"; "the populated resume line" | E-045, confirmed |
| All six TW prompts, *Turn preflight* item 3 and *Output identity* | "Whole incoming source or Nathan's exact selected boundary"; an output identity "from the target/source version, exact selection and run identity" | New |
| TW-DRAIN-10 and TW-DRAIN-20, *Intake and source scope* | "Nathan may optionally select agendas/sections and provide relevant supporting material"; "Accept explicit selections"; "A supplied legacy `PF10_BUILD_NOTES_VERSION` is an explicit identity hint" | New |
| TW-DRAIN-10 and TW-DRAIN-20, *Exact redline contract* | "For genuinely fileless input, retain the actual supplied title and conversation/source reference" | New |
| TW-DRAIN-10 and TW-DRAIN-20, *Completion, outputs and handoff* and *Formatted final-response handoff* | the next invocation carries "selected scope, producer validation status and source-file header provenance"; the handoff holds "known risks/anomalies", gates and a "populated copyable invocation using the next prompt's native ordinary-language inputs", and asks for "usable references, not placeholders or filename-only claims" | New |
| TW-TRIAGE-10, *Source identity and routing* | step 1, "an explicitly supplied legacy `PF10_BUILD_NOTES_VERSION`"; step 3, "the selected current PF10 requirements" | New |
| TW-RECORD-10, *Purpose and minimal inputs* and *Destination* | "with an exact Epic identity and target when not uniquely resolvable"; "or an explicit attributable Nathan statement"; "Resolve any Nathan-selected supporting section"; "ask Nathan for the destination" | New |
| TW-RECORD-20, *Destination* and *PF30 schema* | "Resolve any Nathan-selected supporting section"; "ask Nathan for the destination"; "only when the invocation carries his rollover decision" | New |
| TW-APPLY-10, *Deterministic final document-control header*, the no-change report and *Diagnostic handoff* | "an explicit authorized target version when supplied"; "explicitly fileless sources"; "Only when Nathan explicitly requests a no-change report"; a "populated invocation returning to that preparer" that carries "task selection" | New |
| `gtwpe.handoffs.md` | F1: "the change", "or `none`", and the optional "selected boundary, other context, a run name, and Nathan's authorizations"; F1's check, "a resume keeps the change"; F2: "any selected boundary and supporting material" and "the run's branch and its open pull request"; F4: "the selected scope, the producer validation status and source-file header provenance"; F7: "every applicable PF10 change; Nathan's authorization of the record; any rollover decision"; H11: "the failing stage, evidence, the run ID"; lightly, F3's and F5's returns, F6's lineage and F9's resume line, which the files they name already hold | E-045 for F1, F2, F4 and F7; the rest new |
| The selection page, *Current operation* of TW-ALPHA-20261006.2 | "Next manual entry: [OMITTED] the exact selected scope" | E-045, confirmed |
| The Operations Hub, *Current Glow TW release* | States no rule on inputs. The red callout above it carries Nathan's words, but it is outside GTWPE-MGMT-10's route | — |

**Permitted exceptions** (not reached): naming the prompt to run, as answer 2 does, and GTWPE-MGMT-10's `MODE`;
the Modification ID that its `PLAN` and `EXECUTE` take, which names the record's file; an output location given
as a path, which is a filename; a prompt's own Notion reads of its selection and of
the prompt bodies it runs; text that describes behaviour without asking for an input; and Nathan's approvals to
GTWPE-MGMT-10 (H13), which `D21` requires quoted into the record.

**The "selected boundary" goes.** Under ruling 1 a boundary in words cannot be passed, and under ruling 2 no
addendum is left out of a run: "if there are addenda in PF10, that means they need to be drained, otherwise they
would not be in there" (Nathan, E-044). Every pass reads the whole of every source it is given.

**What a run needs beyond files reaches it as a file.** The analysis reads ruling 1 as covering Nathan's own
inputs to a run, since the execution prompt it was given about is his. So: a resume names the run by its
`RUN.md`, a file; a decision Nathan gives at a stop (a canon conflict, a pass's question, a held-back PF10
change, a PF30 rollover) is a file the resume names; and what a pass needs about the run itself, its branch and
pull request, it reads from `RUN.md`. A run or pass given anything beyond the prompt to run and its files stops
at intake and names what it was given, as GTWPE-FLOW-10 already stops on an execution prompt that asks for what
it rules out. A PF document is named by its directory and versionless name, which canon asks of every prompt
and which still names one file on `main` (risk 14). The plan sets the exact forms.

**"make sure this is clear in the operations hub."** The Hub's current TW section is on GTWPE-MGMT-10's route (the
current-release note on each page that names TW's current release), so the new note there states the rule and
cites GTWPE-D2. The callout at the Hub's top is outside the route, and its last sentence, "GTWPE-FLOW-10
100726.1 still asks for more than filenames; that fix is open", goes stale at X4 (*Pages outside the route*).

#### ITEM-03. Every addendum drained

- **GTWPE-FLOW-10 lets an addendum go undrained.** B1 step 4 decides, document by document, "whether the change
  may affect it"; nothing accounts for every addendum; and B1 step 7, B3 and *Results* end `RUN_NO_CHANGE` when
  no document is affected. Confirmed, as E-044's PE40 check found.
- **PF27 is gated on a specification.** *Eligibility and routing*: "PF27 only when the run has a governing
  specification that changes a template PF27 owns." The gate comes from implementation plan v1.2 §1, which
  lists "PF27 and PF30 are updated only when a specification exists" among things Nathan's message of 2026-09-25
  "also instructed": a summary, not his words (E-052). His ruling, "all pf docs should be updated based on
  context and scope", removes the gate for PF27, a general document. PF30 keeps its specification rule, by his
  separate rule for PF20 and PF30 (ITEM-05).
- **TW-TRIAGE-10 can return no target.** "Return only a simple list of actual target basenames, or one concise
  supported no-target/error result", and its *Output*'s sentence "that no PF target requires drain". Confirmed,
  as E-051's PE40 check found.
- **The drains already account for each change** they are given: "an actionable redline, already represented
  with an exact equivalence location, out of this target's documented ownership [OMITTED], or a blocking unresolved
  item". That fits the rule, per document.
- **Canon bears on timing, not on whether.** HDE Build Notes keeps an addendum authoritative "until the guidance
  is formally reviewed and drained into the relevant permanent PF document" (*Precedence, versioning, and
  scope* §1), and removes drained guidance when it is formally revised (§7). Drainage comes after the change's
  QA, by the Change Process Guide's *Post-QA documentation drainage ordering (normative)* ("only after all QA
  tasks for the epic are complete"), and after its closure decision: "The runtime flow completes required
  QA/reporting and the Isis closure decision before its manual PF10 drainage" (HDE Governance §2.0.19,
  *Post-closure maintenance ordering*; §9.1.5). GTWPE-FLOW-10's B1 step 5 holds a change back only until its
  epic's QA is recorded complete, which is short of canon: a PF10 change that belongs to an epic or a CRD is
  drafted only once the run's files show that change closed, and is otherwise held back and accounted for.
  Nathan's 2026-09-28 ruling "No, pF10 will NEVER be a merge target, EVER>" stands, as `CHECKPOINT.md` §8
  records it.

What follows, for the plan: in a run with a PF10 source, every addendum is accounted for in `RUN.md` and the
pull request: the documents it drains into; where it is already represented, as a pass that read the document
shows it, by a drain's verified `no redlines` with its exact equivalence location, or by the record pass for PF20
or PF30, for each document the addendum bears on; or why it cannot drain in this run (held back until its
change's closure, by canon's ordering; a PF20 or PF30 part with no specification in the run; or a home that is
no eligible document, such as PF10 itself). The triage pass's reading routes an addendum's documents to their
passes and never closes an addendum by itself, as B1 step 4 already says of triage: "When unsure, route it: a
drain's verified `no redlines` is the authoritative answer that it is not affected." No run ends `RUN_NO_CHANGE`
or `RUN_REVIEW_READY` with an addendum unaccounted for, and `RUN_NO_CHANGE` remains only for a run in which every
addendum is shown already represented, or which has no PF10 source and changes no document.

#### ITEM-04. A triage prompt in the run

- GTWPE-FLOW-10 runs no triage prompt: B1 step 4 is its own triage, and `gtwpe.handoffs.md` has no TW-TRIAGE-10
  row. Confirmed, as E-051's PE40 check found. C4's *Member dispositions* left TW-TRIAGE-10 "Unaffected; not
  run": "It is PF10-only and list-only", and its eligibility sentence "contradicts Nathan's ruling of 2026-09-28
  until C5". Nathan's direction is that "the discipline of the prompts is not glossed over" (architecture
  record, *Redlining discipline*).
- TW-TRIAGE-10 is the selected prompt for this job and already allows it: "Nathan initiates every invocation and
  return, directly or through a session he started that runs this prompt as a pass." So the run invokes it as
  its triage pass and takes its return, as it does the drains'.
- TW-TRIAGE-10 needs repair before the run can rely on it, each point from Nathan's words:
  1. **Eligibility.** "including Reference documents where relevant. A title containing Canon is not an
     eligibility rule." Against Nathan's 2026-09-28 rulings: "with the exception of PF03 only files with "canon"
     in their title are valid merge targets", "PF20 and PF30 are special targets with dedicated prompts", and
     PF10 never a target.
  2. **No target.** Its no-target result, against ITEM-03.
  3. **A bare list.** One bullet per target basename cannot show that every addendum is accounted for. Its
     return names, for each addendum, the documents it bears on, which the run routes to their passes, or why
     none in this run (ITEM-03). It never closes an addendum as already represented: only a pass that reads the
     document can show that.
  4. **PF10 only.** "The incoming source is `PF10-HDE-Build-Notes`; do not generalize this alpha to other source
     types." Against the architecture's execution-time triage "against these inputs" (§2) and its full-context
     rule (§7), and Nathan's "based on context and scope": it evaluates the drain targets against every source
     the run has, the specification included.
  5. **Optional.** "This prompt is optional routing help" stays true of a direct invocation, which Nathan's
     ruling does not address; in a run it is part of the run.
- **C5.** C1's §A A.5 proposed C5 as "TW-TRIAGE-10 extended" into the Change Manager. This Modification makes
  TW-TRIAGE-10 the run's triage pass instead; C5's own `ANALYZE` settles the Change Manager's prompt in that
  light. Recorded, not decided here.

#### ITEM-05. PF20 and PF30

- **The authorization gate.** GTWPE-FLOW-10's PF20 and PF30 rows run the record prompts "only with Nathan's
  authorization of that record", and F1 and F7 carry it. Confirmed, as E-046's PE40 check found. Nathan's rule
  replaces it: "If there is a spec involved, those docs are updated. if not, then not." With any specification
  among the run's inputs, PF20 and PF30 are both updated, each through its own prompt, TW-RECORD-10 and
  TW-RECORD-20, on the run's context and scope; without one, neither. What each takes is set by its own scope
  (HDE Phased Epics §0; HDE CRD Records §1): an Epic Specification's record goes in PF20 and a CRD
  Specification's in PF30, and each document takes the PF10 changes that bear on it (S-7). Canon sets when an
  epic's record may go in PF20 (*Canon*, below).
- **The redliner on PF30.** GTWPE-FLOW-10 sends "A change to an existing record: TW-DRAIN-10, then TW-APPLY-10".
  Against E-053's ruling. Confirmed.
- **The record prompts refuse updates.** Both: "An existing record is not permission to create a duplicate or
  silently revise it through this creation role", and "Nathan may invoke the appropriate drain for such work".
  Their output checks allow only "the inserted entry and its control fields". So the record prompts make every
  change a run makes to their document, an existing record's included:
  - TW-RECORD-20, as HDE CRD Records §4.2 requires: "The affected current-state fields MUST be updated in the
    existing CRD entry", with one appended material-change row, earlier rows never overwritten; in the volume that
    holds the record, since a volume `Closed to new CRDs` still takes "all required material, correction,
    continuation, and closure updates" (§6).
  - TW-RECORD-10, within HDE Phased Epics' *Drain posture*: "do not mass-edit historical epic records", and
    "Only update a prior epic record when the change prevents future reader confusion".
- **One pass chain per document.** "A document that would need two, such as a new record and a change to an
  existing record in one PF30 volume, or two records in PF20, is a stop". With the record prompt making every
  change to its document, one pass makes them all; the plan settles what of this stop remains.
- **Addendum changes to PF20 and PF30.** HDE Build Notes 2.14 says "PF27 and PF30 adopt the same terms on their
  next revision", and PF30.1 uses "CRD Plan" 15 times on 14 lines (`grep -o`, by command). A PF30 revision is TW-RECORD-20's,
  since PF30 never goes to the redliner (E-053). So TW-RECORD-20 carries each applicable PF10 change that bears on
  a PF30 volume in context and scope (ITEM-03), beside any record it adds, and TW-RECORD-10 does the same for
  PF20. When no specification is in the run, neither is revised, and the run accounts for such an addendum as
  waiting for one (ITEM-03).
- **Canon.** Nathan's rule is stated from his words, not argued from canon ("this is meaningless distinction",
  E-054). Read for the canon-first rule only: HDE Governance §9.1.1 makes PF20 and PF30 historical homes that
  "The active workflow MUST NOT create, update or synchronize", reserves additions to "a separately authorized
  historical drainage action", and asks to "Preserve existing PF20/PF30 content and original identities as dated
  history"; its table and §9.1.5 put PF10 drainage after closure, as maintenance an authorized manual operator
  does. A run Nathan starts is that maintenance, not the active workflow, and S-7's update of an existing CRD
  record keeps its earlier rows and its identity, as HDE CRD Records §4.2 asks. Canon also sets when: PF20 takes
  an epic's record "only once, at epic close", and "In-flight epics MUST NOT be added" (Plan Templates §2,
  *Historical-only posture (normative)*; Change Process Guide §1.1.2, §3.5.1 and §6.3). So PF20 takes an Epic
  Specification's record only when the run's files show the epic closed; otherwise that part waits, accounted
  for as ITEM-03 says, and TW-RECORD-10 keeps its rule that the epic's completed or historical posture is
  established from the evidence it is given, which is a file. E-010, canon's own conflict on PF20 and PF30
  records, stays open and his.
- **The first live run** (HDE Build Notes and the HDE-EPIC040 Specification, as PE40-INIT names them): a
  specification is involved, so PF20 and PF30 are both updated. PF20 takes HDE-EPIC040's record, which is new
  (`git grep -c HDE-EPIC040` over HDE Phased Epics is 0), and the PF10 changes that bear on PF20; PF30 takes the
  PF10 changes that bear on it, such as 2.14's terms, and no new record, since no CRD Specification is in the
  run. HDE-EPIC040 was closed on 2026-09-29 by `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`
  (`CLOSE`). HDE Build Notes records its QA verdict ("It is not closure") and not that decision, so the decision
  must be among the run's inputs; without it, HDE-EPIC040's PF20 record and its PF10 changes wait.

#### ITEM-06. PF09

No defect, and no change of its own. GTWPE-FLOW-10 sends each PF09 phase document to TW-DRAIN-20, then
TW-APPLY-10, and keeps PF09 out of the general route. That is architecture §6 ("PF09 uses its own specialized
prompt") and *Redlining discipline* (every document but PF20 and PF30 goes through redline creation and redline
apply, with a report for each phase). TW-DRAIN-20's scope lines agree: "PF09 preparation belongs here" and "For
a complete READY package, Nathan invokes TW-APPLY-10"; TW-APPLY-10 takes packages "from actual TW-DRAIN-10/20
preparer"; and TW-DRAIN-20 judges every potentially affected row "on all the available evidence", architecture
§8 nearly word for word. This agrees with E-047's PE40 check. Which phase files a run takes is the triage pass's
(ITEM-04). TW-DRAIN-20 changes for ITEM-02 and ITEM-05 only. Nathan's approval of this analysis accepts it, which
closes E-047.

#### ITEM-07. GTWPE-MGMT-10's own request

GTWPE-MGMT-10's entry contract takes "the request in whatever form it arrives: a defect in a GTWPE run's
report, a sentence, a finding, a policy instruction", and asks for "the subject, the expected result, the
actual or requested result, and an example". A relayed request therefore reaches the analysis whole, as
context, and A1 copies it verbatim as the request. That is the route by which PE39's interpretations entered C1
to C4 (E-048: "PE39 wrote long change requests to the C1 to C4 workers carrying its own interpretations"). Under
ruling 1, a request handed to it carries only the files that record it, as Nathan's request for this
Modification does. Its workers and reviewers are handed only filenames, their committed brief among them.

**This differs from PE40's check,** which found "no defect found against the rulings in GTWPE-MGMT-10, whose
request may arrive "in whatever form", filenames included" (E-048). PE40 asked whether the prompt requires more than filenames; this
analysis asks whether it lets more than filenames pass in a handoff. Nathan's approval settles it; dropping
ITEM-07 leaves the rest of the Modification unchanged.

#### Everything else the check covered

Found consistent with Nathan's words, with no change: the architecture's §§4, 5 and 10 (no Draft status;
document control; the completion standard), built in C3 and checked in GTWPE-FLOW-10's B4 and B6; §6's PF03
special case; §7, full-context reading, in every pass; §8, in TW-DRAIN-20; §9, in both record prompts; answers 3
to 8; the stop rule (S1 to S6); no model or strength advice in any TW prompt or in GTWPE-FLOW-10; and GTWPE-D1
in every writer. Answer 8's "divided into additional logically organized volumes" is, by HDE CRD Records §6, the
Product Owner's determination; GTWPE-FLOW-10 stops for it (S4), which stays, with his decision given as a file
(ITEM-02). One more defect, under ITEM-05: TW-DRAIN-10's and TW-DRAIN-20's *Exact redline contract* keep "such
as an HDE CRD Records material-change row's decision date", written for the PF30 drain route ITEM-05 removes;
it goes with that route.

Found wrong against the live sources in GTWPE-MGMT-10, which ITEM-07 gives a new version, and fixed there under
ITEM-08: "until G5", in the six places E-033 lists (*Native purpose*; two rows of *What this prompt may change*;
*Notion writes*; the `prompt` and `notion_control` entries of the `targets` row), where the approved order of
changes has no G5 and adoption is C6, so the bound becomes the adoption change, as E-033 proposes; the selection
route's "lists the eight members", where TW-ALPHA has six (C3's F-1); and its two pointers to the design
package's §6 handoff table (*Read these*; the `closure` row of *The record*), which C4 replaced with
`docs/prompt_ecosystem_management/gtwpe/gtwpe.handoffs.md`. Likewise in GTWPE-FLOW-10, which ITEM-02 to ITEM-05
give a new version: the two links to `http://RUN.md` that Notion made of plain `RUN.md` at its publication
(E-042), which the ledger keeps as "a candidate for the prompt's next version", written as inline code, with the
check for bare file names that its finding F-E1 proposes.

### What the analysis settles, for Nathan's approval

Each follows from his words and the canon cited; none is his own words, so each is listed for his approval.

| # | Settled | From |
|---|---|---|
| S-1 | Ruling 1 covers Nathan's own inputs to a run. A resume, a decision at a stop and a rollover decision reach a run as files; a run or pass given anything beyond the prompt to run and its files stops at intake and names it | Ruling 1; GTWPE-FLOW-10's existing intake stop |
| S-2 | Attached files stay allowed beside repository paths | Answer 2 |
| S-3 | No selected boundary anywhere: every pass reads every source whole | Ruling 1; E-044 |
| S-4 | Every addendum accounted for, and counted as already represented only on a pass's verified finding for each document it bears on; a change held back until its epic or CRD is shown closed; `RUN_NO_CHANGE` only as ITEM-03 states | Ruling 2; E-044's ruling; HDE Build Notes front matter §1 and §7; the Change Process Guide's post-QA ordering; HDE Governance §2.0.19 and §9.1.5; GTWPE-FLOW-10's B1 step 4 |
| S-5 | TW-TRIAGE-10 is the run's triage pass, evaluating every source; it stays optional for a direct invocation | Ruling 2; architecture §2 and §7 |
| S-6 | With any specification among the run's inputs, PF20 and PF30 are both updated, each through its own prompt, on the run's context and scope: the specification's record in the document whose scope it is, an epic's only once its closure is among the run's files, and each document's applicable PF10 changes. Without a specification, neither | Ruling 3; E-046's and E-052's ruling; HDE Phased Epics §0; HDE CRD Records §1; Plan Templates §2; Change Process Guide §1.1.2, §3.5.1 and §6.3 |
| S-7 | The record prompts make every change to their document in a run: an existing record's update, and the PF10 changes that bear on the document in context and scope, such as 2.14's terms for PF30 | E-053's ruling; E-044's ruling; HDE Build Notes 2.14; HDE CRD Records §4.2 and §6; HDE Phased Epics *Drain posture* |
| S-8 | GTWPE-MGMT-10's own request is files only (ITEM-07) | Ruling 1; E-048 |

### What changes, by surface

| Surface | Route (*How each kind of target changes*) | Items |
|---|---|---|
| GTWPE-FLOW-10 | A new versioned sibling under the GTWPE parent page; the catalog selects it at X4 | 02, 03, 04, 05, 08 |
| GTWPE-MGMT-10 | A new versioned sibling under the GTWPE parent page; the catalog selects it at X4 | 07, 08 |
| TW-TRIAGE-10 | A new versioned sibling under *HDE TW*, selected by a new TW-ALPHA release | 02, 03, 04 |
| TW-DRAIN-10, TW-DRAIN-20 | The same | 02, 05 |
| TW-RECORD-10, TW-RECORD-20 | The same | 02, 05 |
| TW-APPLY-10 | The same | 02 |
| `gtwpe/gtwpe.decision-record.md` | A commit on this branch; Nathan merges at X2 | 01 |
| `gtwpe/gtwpe.handoffs.md` | The same commit and merge: F1, F2, F4, F6, F7, F9 and H11, the triage pass's two new rows, and the diagram | 02, 04, 05 |
| The selection page | The three selection writes, with a new *Current operation*, since the change alters how the TW flow runs | 02, 04, 05 |
| *HDE TW*, *Alpha 1*, the Operations Hub | The current-release note in each page's current TW section; on the Hub, the note states the rule (ITEM-02) | 02 |
| The GTWPE catalog | X4: the two rows, and the checked-through commit | — |

All six TW prompts change, so the new TW-ALPHA release has no unchanged row.

### Per part: closure, tier, class and targets

**One part,** PART-01, all eight items. A part is "one rule across its surfaces, above all" (`D21-B`): ruling 1
reaches every member, and rulings 2 and 3 share GTWPE-FLOW-10, the handoff table and the TW selection with it,
so splitting them would split a rule (the `D12` error) and put one page's edits in two parts.

- **Class B**, rule application: Nathan has ruled, and the ruling is the authorization. ITEM-01 records his
  rulings before they are applied, as a rule change needs (`ecosystem-change-management.md` §2, step 1).
- **Targets:** `prompt` (two GTWPE pages; six TW-ALPHA members), `rule` (the decision record and the handoff
  table), `notion_control` (the catalog; the selection page and the three pages that name TW's current release).
  No `tool`: the record format and its checks are unchanged. No `skill`.
- **Closure,** read from `gtwpe.handoffs.md` and the TW-ALPHA *Current operation*, on the changed handoffs:
  GTWPE-FLOW-10 consumes from and produces to TW-TRIAGE-10 (new), TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10,
  TW-RECORD-10 and TW-RECORD-20, and to GTWPE-MGMT-10 through H11; GTWPE-MGMT-10 consumes H11, whose producer is
  a run. TW-DRAIN-10 and TW-DRAIN-20 share their outcomes (`READY`, `NO_CHANGE`, `BLOCKED`; `COMPLETE_PACKAGE`,
  `PARTIAL_PACKAGE`). Every member the closure names changes in this Modification.
- **Tier 2:** it changes handoffs (F1, F2, F4, F6, F7, F9, H11 and two new rows) and TW-ALPHA relationships (the
  triage pass joins the run; the record prompts become the only route to PF20 and PF30), on both sides, in this
  Modification. No selftest or trial exercises a prompt handoff today; the gate is `PLAN`'s two-sided check of
  every invocation against the bodies it reaches, as C4 made it, and each new page's readback.

### Member dispositions (HDE Governance §9.1.6)

| Member or interface | Disposition | Reason |
|---|---|---|
| GTWPE-MGMT-10 | Affected | ITEM-07; ITEM-08, its own wrong text (*Everything else the check covered*) |
| GTWPE-FLOW-10 | Affected | ITEM-02 to ITEM-05; ITEM-08, the two `RUN.md` links (E-042) |
| TW-TRIAGE-10 | Affected | ITEM-02 to ITEM-04 |
| TW-DRAIN-10, TW-DRAIN-20 | Affected | ITEM-02; ITEM-05's PF30 clause |
| TW-RECORD-10, TW-RECORD-20 | Affected | ITEM-02, ITEM-05 |
| TW-APPLY-10 | Affected | ITEM-02 |
| TW-MGMT-10 (not selected since TW-ALPHA-20261006.1), TW-ASSESS-10 (retired) | Unaffected | Not selected; nothing runs them |
| The GTWPE catalog | Affected | X4: two rows and the checked-through commit |
| `gtwpe.decision-record.md` | Affected | ITEM-01; GTWPE-D1 unchanged |
| `gtwpe.handoffs.md` | Affected | ITEM-02, ITEM-04, ITEM-05 |
| `gtwpe_record_check.py`; `modification_validate.py`, `modification-template.md`, `reviewer-prompt-template.md` | Unaffected | The record format and its checks are unchanged; the last three are shared GCFPE controls, outside this prompt's route |
| The selection page; *HDE TW*, *Alpha 1*, the Operations Hub | Affected | The selection writes and the current-release notes |
| The architecture page and record | Unaffected by the route; left stale | Outside the route (*Pages outside the route*) |
| `tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Affected | Skills that interact with the TW-ALPHA selection and have not run its releases since C2. HDE Governance §9.1.6 reconciles interacting skills in one coherent successor selection, and Nathan waived that for TW Flowmaster one release at a time (C2's and C3's `override`). The new release needs his decision again (Q-1) |
| `glow-write-boundary`, the GTWPE exception | Unaffected | No write boundary changes: a run still writes only under `docs/ephemeral/` |
| `typesafe-scoring`, `hd-typesafe-scoring` | Outside the GTWPE | E-043 (*Intake*) |
| The PE Metaprompt 091426.1 | Unaffected | Used by `PLAN` to author, under GTWPE-MGMT-10's workarounds |

### GTWPE-D1, prompt by prompt (A2)

| Prompt | Writes, before and after | How the part keeps GTWPE-D1 whole |
|---|---|---|
| GTWPE-FLOW-10 | Neither artifact, before and after | Its *Proof logs (GTWPE-D1)* section, with the requirement verbatim and the B6 check, is not edited |
| GTWPE-MGMT-10 | Neither | Its guard (*Boundaries*; the proof-log check by phrase on a new page) is not edited |
| TW-TRIAGE-10 | Neither, before and after: its triage is a return, not an artifact | Nothing to keep |
| TW-DRAIN-10, TW-DRAIN-20 | The redlines file and its separate proof log, before and after | The proof-log paragraph, its eight minimum items and "named after it" are not edited; ITEM-02's edits are in intake and handoff text |
| TW-APPLY-10 | The revised PF and its separate proof log, before and after | The same |
| TW-RECORD-10 | The updated PF20 and its proof log, before; after, also for an existing record's update and for the PF10 changes it carries | The proof log and its eight items are kept; what it "also records" (where the entry went, the control fields before and after, that nothing else changed) is extended to every change it makes |
| TW-RECORD-20 | The updated PF30 volume, and on a rollover the next volume's review copy, each with its proof log; after, also for an existing record's update and for the PF10 changes it carries, with or without a new record | The same; one proof log per file, as now |

### Scope, and how it was measured (`SCOPE-001`)

**Method:** broad match by reading. For each rule, its broad terms were matched across each member's whole live
body, section by section, the permitted exceptions subtracted, and every remaining passage read in context. Every
body was fetched inline, so no harness save exists to count over by script; by `D22`, each count was made by
reading, and the dry run checks it by a second reading of a second fetch. The repository files were counted by
`grep`. This is also A3's `D26-E` search for these rulings: the passages reached are the text they contradict.

- **Ruling 1's terms:** `select`, `boundary`, `the change`, `context`, `supporting material`, `authoriz`,
  `decision`, `direction`, `statement`, `ask`, `fileless`, `run name`, `RESUME`, `invocation`, `handoff`,
  `supplied`. Exceptions as ITEM-02 lists them.
- **Ruling 2's:** `drain` as drainage (not the TW-DRAIN prompts), `no-target`, `no PF target`, `not affected`,
  `RUN_NO_CHANGE`, `list`, `optional`, `PF10-only` and `generalize`, `PF27`, `only when the run has`.
  Excepted: another TW prompt's note that TW-TRIAGE-10 is optional routing help, which S-5 keeps true of a
  direct invocation; in a run, GTWPE-FLOW-10 runs it.
- **Ruling 3's:** `PF20`, `PF30`, `record`, `authoriz`, `existing`, `appropriate drain`, `creation`, `insert`,
  `HDE CRD Records`. Excepted: PF20 and PF30 named as eligible, or in a record prompt's own schema text.

**Sections reached**, of each body's sections (the identity block, with a title heading that has no text of
its own, counted as one):

| Body | Sections | Ruling 1 | Ruling 2 | Ruling 3 |
|---|---|---|---|---|
| GTWPE-FLOW-10 | 20 | 11: identity; *Authority and limits*; *The execution prompt*; *Eligibility and routing*; *The run's branch, pull request and directory*; *Passes*; *B1*; *B5*; *Redo from canon*; *Stop and resume*; *Results* | 6: *Eligibility and routing*; *RUN.md*; *Passes*; *B1*; *B3*; *Results* | 4: *The execution prompt*; *Eligibility and routing*; *Passes*; *Stop and resume* |
| TW-TRIAGE-10 | 5 | 1: *Source identity and routing* (step 1's supplied version; step 3's "selected") | 4: *Coded identity and relationships*; *Purpose and authority*; *Source identity and routing*; *Output* | 2: *Coded identity and relationships* (it names only the two drains as next prompts); *Source identity and routing* (PF20 and PF30 as targets) |
| TW-DRAIN-10 | 12 | 8, two of them light: *Authority and sources* (light: "the explicit current Nathan directive"); *Turn preflight*; *Output identity*; *Intake and source scope*; *General PF preparation* (light: "Nathan authorization"); *Exact redline contract*; *Completion, outputs and handoff*; *Formatted final-response handoff* | 0 | 1: *Exact redline contract* |
| TW-DRAIN-20 | 13 | 9, three of them light: as TW-DRAIN-10, with its two PF09 sections in place of *General PF preparation*, which it does not have: *Development-board independence* (light: "selected sources") and *PF09 coverage and native semantics* (light: "selected prompt/source") | 0 | 1: *Exact redline contract* |
| TW-RECORD-10 | 9 | 5, one light: *Authority and sources* (light); *Purpose and minimal inputs*; *Turn preflight*; *Output identity*; *Destination, source roles and record preparation* | 0 | 4: identity (its title); *Purpose and minimal inputs*; *Destination, source roles and record preparation*; *Output and completion* |
| TW-RECORD-20 | 9 | 5, one light: *Authority and sources* (light); *Turn preflight*; *Output identity*; *Destination, source roles and record preparation*; *PF30 schema and native detail* | 0 | 5, one light: identity (its title); *Purpose and minimal inputs*; *Destination, source roles and record preparation*; *Output and completion*; *PF30 schema and native detail* (light: an update's volume) |
| TW-APPLY-10 | 12 | 8, two of them light: *Authority and sources* (light); *Turn preflight*; *Output identity*; *Intake and preparation-state verification*; *Deterministic final document-control header*; *Exact application and preservation* (the no-change report); *Invalidity, failure and return* (light: "ask Nathan to identify it"); *Diagnostic handoff* | 0 | 0 |
| GTWPE-MGMT-10 | 24 | 3: *Entry contract*; *Reviews are bounded* (the brief a reviewer is handed); *One session, and workers by workload* | 0 | 0 |

**ITEM-08's fixes in GTWPE-MGMT-10,** by reading its fetch after this session's context was compacted, each count
equal to an earlier reading of the same version, edited 2026-10-05T16:36:11.384Z: "G5" six times, in *Native
purpose*, *What this prompt may change* and *The record* (E-033's six); "§6" twice, in *Read these* and *The
record* (C4's dry run, D5); "eight members" once, in *How each kind of target changes* (C3's F-1). Five sections,
none of them among ruling 1's three. In GTWPE-FLOW-10, by reading its third fetch: the two `RUN.md` links, in the
heading of *RUN.md* and in the table of *The run's branch, pull request and directory*, E-042's "exactly those two
links"; both sections are among ruling 1's or ruling 2's already.

The plan measures each passage's exact anchor and count, by two independent readings where no save exists (ledger
E-035's lesson), and runs `D26-E`'s search for surviving old text on each new page.

**In the repository,** by reading the file whole: `gtwpe.handoffs.md`, 9 of its 12 rows reached, F1, F2, F4, F7 and
H11 fully and F3, F5, F6 and F9 lightly (a pass's return is its outcome and the paths of what it wrote; what more
it says is in those files), with F8, H12 and H13 not reached; its *Common rules* gain the rule, and the triage
pass two new rows and a node in the diagram. `gtwpe.decision-record.md`: three new entries; `git grep` on
ruling 1's terms finds three lines, its `applies_to` and two in GTWPE-D1, each a "handoff" through which the
proof-log rule must survive, which stays. `gtwpe_record_check.py`: one
line, a selftest fixture's quoted heading; no change.

### Pages that name the members or TW's current release (A3)

Searched with highlights off on each member's ID, title and version, and on `TW-ALPHA-20261006.2`; each page
found fetched or read, with each page the members name as holding their selection and each page C3's record
(TW's latest selection) says it wrote.

| Page | Names | Written by the route |
|---|---|---|
| The GTWPE parent page, with the catalog | GTWPE-MGMT-10 100526.2; GTWPE-FLOW-10 100726.1 | Yes, at X4 |
| *Glow Technical Writing Ecosystem* | TW-ALPHA-20261006.2 and its six members, and its *Current operation* | Yes: the three selection writes |
| *HDE TW* | TW-ALPHA-20261006.2 in *Current TW release*; the members as child pages | Yes: the current-release note. The new pages become children |
| *Alpha 1 — Implementation and Validation* | TW-ALPHA-20261006.2's rows | Yes: the current-release note |
| Glow Operations Hub | TW-ALPHA-20261006.2 in *Current Glow TW release*; the callout names GTWPE-FLOW-10 100726.1 | The current TW section, yes; the callout, no |
| *GTWPE Target Architecture — Document-Writing Flow* | GTWPE-FLOW-10, by mention; C1 to C4's status | No |
| Usage-log pages under *TypeSafe effort scorer — uses* | Past scoring requests, by title | No: dated logs of past use, not current state |
| *04 Archived Prompt Versions* | The archived unselected copies of TW-TRIAGE-10 and TW-DRAIN-10 100626.1 | No |
| Earlier versions of each member | Their own titles | No |

The new TW-TRIAGE-10 and TW-DRAIN-10 titles must be unique among *HDE TW*'s children and also differ from the
archived copies' titles, which reuse 100626.1.

**Does the change alter how the TW flow runs?** Yes: the triage prompt becomes part of a run, the record prompts
take every change to PF20 and PF30, and the entry takes only files. The new release's section carries a new
*Current operation*, and the current one becomes historical.

### Contradictions and risks

1. **The architecture's "context".** §1 has the manager decide "what context must be passed", and §2 lists "any
   additional context identified during manager triage". Ruling 1 is later: "Any other context will corrupt the
   run." Under it that context is passed as files.
2. **Nathan loses the TW prompts' optional selections** in a direct invocation, a behaviour his ruling requires
   (S-3). Recorded so he sees it.
3. **A stop becomes heavier to resume.** A decision at a stop is a file the resume names (S-1).
4. **An addendum with no eligible home,** such as one whose only home is PF10 itself, cannot drain, since PF10 is
   never a target; the run reports it (S-4) rather than leave it silently.
5. **Held-back addenda** wait for their epic's or CRD's closure, by canon's ordering (ITEM-03), and the run
   accounts for them. A run's files must include each closure decision it relies on, as the first live run shows
   (ITEM-05).
6. **The record prompts' role widens** from inserting one section to every change a run makes to their document
   (S-7), beyond Nathan's "they only get one SECTION" of 2026-09-29. His words of 2026-10-07 require it: PF30
   "must be updated" in the first run, which has no CRD record to add, so its update there can only be the PF10
   changes that bear on it; and "They should not need that step" keeps the redliner out.
7. **The record prompts' titles** ("Create Epic History Section", "Create CRD History Section") no longer describe an update; the plan decides
   whether a title changes, and if it does, every page naming it takes the new title.
8. **TW-TRIAGE-10 stops being list-only:** its return carries each addendum's targets (ITEM-04). The selection page
   says "TW-TRIAGE-10 stays list-only", which the new release's text replaces.
9. **ITEM-07 differs from PE40's check** (E-048).
10. **Eight bodies change at once.** Under `D26-F`'s "about ten live bodies"; but its first trigger holds, since
    Nathan refuted C4's completion (E-045, E-046, E-051), so this mode's review is a full one by two fresh
    reviewers, the template's number.
11. **Counts by reading** over eight bodies can be wrong, as in E-035; the plan makes each count twice,
    independently.
12. **The record and ledger rows outside this prompt.** E-020's premise ("PF27 can change in a run with no
    specification" as a defect) is reversed by E-052's ruling once this lands; E-006, E-016 and E-022 still read
    `OPEN` though C4 carried them (C4 ITEM-07, `VERIFIED`); E-004, E-009, E-015 and E-021 still read `OPEN` though
    C1's §A A.6 found them moot. The ledger is PE40's to keep (*Pages outside the route*).
13. **This mode's own reviewers** are handed only their committed brief's filename (ruling 1). The brief's content
    is the template's, which GTWPE-MGMT-10 requires.
14. **Versioned filenames.** HDE Build Notes 2.14 says "Do not pin a PF file version in a prompt", and HDE
    Governance §9.1.6 asks a temporary handoff prompt, as well as a durable body, for "the controlled directory,
    versionless document name and appropriate section", while it keeps "exact source binding in run artifacts".
    So an execution prompt, and every invocation, names a PF document by its directory and versionless name, such
    as `PF10-HDE-Build-Notes` in `docs/pfcanon/`, which still names one file on `main`; the run resolves it there
    and records the file and its blob in `RUN.md`. Nathan asked for the first run "using the latest PF10". Every
    other file is named by its repository path.
15. **The TW Flowmaster skill (Q-1).** `tw-flowmaster` 1.3.0 and `flowmaster-validate` 3.3.2 have not run the
    TW-ALPHA releases since C2, and a Flowmaster run against the new release would stop loudly rather than
    produce a wrong result, as for C3's (its risk 1). Nathan's waivers covered C2's and C3's releases only.

### Defect classes matched (`ecosystem-change-management.md` §4)

- **DERIV-001,** nearest: the PF27 gate is a summary of Nathan's message restated as a rule (plan v1.2 §1), and
  the PF20 and PF30 authorization gate a canon reading set against his recorded architecture (E-046).
- **SCOPE-001:** the scope above is measured by broad match minus exceptions, with its method.
- **GUARD-001,** as a limit: the GTWPE has no registry, so a ruling's guard is each page's readback and `D26-E`'s
  search, as in C1 to C4.
- **SCOPE-002:** the selection writes and the notes touch only each page's current TW section (E-038's lesson).

### Candidates for separate Modifications (recorded, not taken)

- **E-035's candidate:** counts over a body by script where a save exists.
- **Ruling 1 in the GCFPE.** The Operations Hub's *Prompt ecosystem worker output standard* lets a GCFPE handoff
  carry "the minimum context it needs". If "at every phase" reaches the GCFPE, that is GCFPE-MGMT-10's to change.

### Pages outside the route that this change leaves stale

For Nathan to authorize, or PE40 to do, after X4, as E-041 was done:

- **N-1:** the Operations Hub's red callout, last sentence: "GTWPE-FLOW-10 100726.1 still asks for more than
  filenames; that fix is open".
- **N-2:** the architecture page's status line of 2026-10-07 and its "resume with `RESUME <run-id>`"; the
  repository architecture record's status updates.
- **N-3:** the ledger: E-044 to E-048, E-051 to E-053, and the stale rows in risk 12.

### Open questions for the Product Owner

**Q-1. The TW Flowmaster skill, for this release (risk 15).**
- **(a) Waive HDE Governance §9.1.6's interacting-skill readiness for `tw-flowmaster` again, for this
  release.** Recommended. The grounds are C2's and C3's: GTWPE-FLOW-10 now runs the TW prompts as passes, C6
  retires the skill, and a Flowmaster run stops loudly rather than producing a wrong result. The selection page
  and the three notes say that `tw-flowmaster` 1.3.0 and `flowmaster-validate` 3.3.2 do not run the new release,
  and the `override` block records the waiver.
- **(b) Update `tw-flowmaster`, with any `flowmaster-validate` assertion that pins its wording, in this
  Modification.** It adds the `skill` target, a skill review cycle and Nathan's install.

S-1 to S-8 are settled from his words and canon, and his approval accepts them.

### Readiness and interaction cost

`NEEDS_RULING`, for Q-1. It is advice, not a refusal. No item waits on another item's execution, and every
surface's scope is measured.

    interaction_cost = 1 open ruling + 2 + 6 review rounds + 0 skill review cycles + 0 installs + 2 merges = 11

- **Review rounds:** this mode's dry run, its full review by two reviewers, and one check of the repair's diff;
  `PLAN`'s dry run, one full review and one check of a repair's diff.
- **Q-1's option (b)** would add a skill review cycle and an install, making 13.
- **Merges:** the branch's pull request at X2, which carries the decision record and the handoff table; then the
  record's pull request after X5.
- **Splitting saves nothing:** the items share GTWPE-FLOW-10, the handoff table and the selection. Moving ITEM-07
  to a run of its own would add two approvals, two review rounds and a merge.
- **Calibration:** C2 to C4 predicted 8, 7 and 7 and cost 14, 11 and 13, each above its prediction by rulings,
  diff checks and extra merges; on that record this one may cost more than 11.

**The estimate,** in the front matter: `PLAN` about 10 h and `EXECUTE` about 5 h, not counting waits for Nathan.
Time is the meter the session can read; tokens are not measured. Twice the estimate is where the session stops.

### Dry run (A6)

Every normal-path gate and readback of this mode, read-only, by this session, before any full review. What it
found was corrected in this section before the review, and the table says what each correction was.

| # | Gate or readback | Result |
|---|---|---|
| D1 | Both record checks on a scratch copy of this record at `ANALYZED`, with this round in `reviews`: `modification_validate.py` and `gtwpe_record_check.py` | Both exit 0, 1/1 each |
| D2 | The front matter parses (PyYAML), its `request` equals Nathan's message, and every table in the record has one column count in every row, by script | Parses; the request is verbatim; 15 tables, each with one column count in every row |
| D3 | A0 reproduced: `git fetch origin main`; `origin/main`; `git log b65e918..origin/main` over *The watched sources* | Still `128836a` at 2026-10-07T05:46Z; the watched-path log is empty |
| D4 | Every member and control page fetched again, for its edit time | Each unchanged: the eight members as *The members, read live* gives them; on 2026-10-07, the GTWPE parent page 01:59:25.993Z, the selection page 02:12:01.288Z, *HDE TW* 02:12:11.957Z, *Alpha 1* 02:11:56.963Z with 34 headings, the Operations Hub 04:23:05.337Z and the architecture page 02:13:39.342Z |
| D5 | The scope counts, by a second, independent reading of a second fetch of each body | Two counts corrected and one exception stated. GTWPE-FLOW-10 has 20 sections, not 21: the first reading counted its title heading, which has no text of its own, as a section, where it counted GTWPE-MGMT-10's, the only other, within the identity block; the table's header now says how the identity block counts. TW-DRAIN-20's ruling 1 reach is 9 sections, three light, not 8: *Development-board independence* ("selected sources") was missed. Ruling 2's term `optional` matches the TW prompts' note that TW-TRIAGE-10 is optional routing help, and the counts of 0 stood on an exception the record did not state; *Scope* now states it. A third fetch of GTWPE-FLOW-10 and TW-DRAIN-20 settled the two counts. Every other count confirmed, section by section |
| D6 | Each quotation from a repository file is found in its source on `origin/main`, whitespace collapsed, by script | 66 of 66, after four corrections. Answer 2 had been quoted without its list markers; it is now quoted in parts. The phrase quoted from E-044 as a rule, "an execution prompt names the sources; it never narrows them", was PE39's lesson, cut before "on PE39's inference"; Nathan's own words in that row replace it. "to be settled at C5" was PE39's account of C4 (E-051); C4's own words replace it. A bold phrase in quotation marks was not Nathan's wording; it now quotes him. And by `grep -o` and `grep -c`, "CRD Plan" appears 15 times on 14 lines of PF30.1 |
| D7 | Each quotation from a Notion page, checked against this session's second fetch, by reading | Each found as quoted |
| D8 | A3's `D26-E` search over the GTWPE's repository files, and the record tools | The search had covered the handoff table only; `git grep` now covers `docs/prompt_ecosystem_management/gtwpe/` (*Scope*). `TARGETS` holds `prompt`, `rule` and `notion_control`, and the record check needs only the subsections this record has, so no tool changes |
| D9 | The record's lists, against each other and against the bodies | *Per part*'s tier 2 list of changed handoffs left out F9, which *What changes* names; added. The `PLAN` and `EXECUTE` input, a Modification ID, was matched by ruling 1's terms and not listed as an exception; it names the record's file, and the exceptions now say so |

No required defect is left open.

### Full review (A6)

- **The reviewers.** Two fresh general-purpose subagents, GTWPE-TW-FLOW-RULINGS-ANALYZE-A and -B, neither
  forked nor context-inheriting, as the template sets. Each was handed nothing but its brief's repository path
  (ruling 1; risk 13): `ANALYZE-REVIEW-A-BRIEF.md` and `ANALYZE-REVIEW-B-BRIEF.md` in
  `docs/ephemeral/modifications/evidence/gtwpe-tw-flow-rulings/`, committed and pushed at `024425c` before
  either was spawned, at 05:51Z. Each confirmed its brief's sha256 at that commit (A `15fb79b2…`, B `ae6a9c56…`),
  and that `024425c` adds only the two briefs to `cc6b923`.
- **The runs.** Each reviewed §A at `cc6b923`, read no Notion page and wrote nothing. A ran for about 39 minutes
  and B for about 37; the harness reported 605,411 and 558,319 subagent tokens. B reported one side effect that
  was not its act: the harness saved one oversized output of its, a grep of `ERRORS.md`, which holds no prompt
  body (*Harness files*).
- **The captures.** Each return came back through the harness's `SubagentHandback` call. `capture.py` read each
  reviewer's own transcript, found by the path the harness gave for its agent ID, twice: first printing only the
  call's shape (one call each: A's at transcript line 585, 20,623 characters; B's at line 596, 22,599 characters),
  then writing its message, with one final LF:
  - `ANALYZE-REVIEW-A.md`: 20,708 bytes, sha256 `416ad54b534b956746400e71e5d4f7d1f949d0abe802c25ef57e71b4d98ff5ea`;
    first line `1`.
  - `ANALYZE-REVIEW-B.md`: 22,653 bytes, sha256 `6b58d32138173e4b9459fb61d18b4c8d44eb514f0e3fb83d017c45c83156e65b`;
    first line `3`.

  Each carries the `## Canon relied on` block the brief required.

**Result: A, 1 required and 22 listed; B, 3 required and 20 listed.** The session tested each required finding
against its source and confirmed all four, and it confirmed three listed findings as required under the fixed
rubric's R1. The round closes with 7 distinct required defects, each repaired in this section:

- **RQ-1** (B's R-1, with A's L1). S-6 narrowed "If there is a spec involved, those docs are updated" by type of
  specification, so the first live run would have left PF30 untouched, against ruling 3's "PF20 and PF30 must be
  updated as part of this". Confirmed against PE40-INIT's ruling 3 and ledger E-046 and E-052. Repaired in
  ITEM-05 (*The authorization gate*, *Addendum changes*, *The first live run*), S-6, risk 6 and *GTWPE-D1, prompt
  by prompt*.
- **RQ-2** (A's R-1, with B's L5, which the session confirmed as required). Canon's timing was missing: PF20
  takes an epic's record "only once, at epic close" (Plan Templates §2; Change Process Guide §1.1.2, §3.5.1 and
  §6.3), and PF10 drainage follows the Isis closure decision (HDE Governance §2.0.19 and §9.1.5). §A said the PF20
  rule "conflicts with no canon" and gave the post-QA ordering alone. Confirmed by reading those sections on
  `main`. Repaired in ITEM-03 (the canon bullet and what follows from it), ITEM-05 (*Canon*, which now cites
  §9.1.1 in full, as B's L6 asked, and *The first live run*, which needs HDE-EPIC040's closure decision among its
  files), S-4, S-6, risk 5 and the canon table.
- **RQ-3** (B's R-2). The new TW-ALPHA release needs Nathan's decision on `tw-flowmaster`'s readiness, as C2's
  and C3's did. Confirmed against their `override` blocks and Q-1s, and C4's disposition. Repaired in *Member
  dispositions*, risk 15, Q-1, readiness (`NEEDS_RULING`) and the interaction cost.
- **RQ-4** (B's R-3, with A's L5). The triage pass's reading alone could count an addendum as already
  represented. Confirmed against E-044's ruling and GTWPE-FLOW-10's own B1 step 4. Repaired in ITEM-03's
  accounting, ITEM-04's repair 3 and S-4.
- **RQ-5** (B's L13 and A's L17, confirmed as required). ITEM-01's "both sentences" and "two sentences" would
  leave ruling 2's third sentence, the basis of ITEM-04, out of GTWPE-D3. Repaired in ITEM-01.
- **RQ-6** (B's L8 and A's L14, confirmed as required). Risk 14 let an execution prompt pin a PF version, but
  HDE Build Notes 2.14 and HDE Governance §9.1.6 cover temporary prompts too. Confirmed by reading both. Repaired
  in risk 14 and ITEM-02.
- **RQ-7** (A's L13, confirmed as required). ITEM-08 says what is found wrong is fixed, yet §A left E-033's
  "until G5" and C3's F-1 in GTWPE-MGMT-10, which this Modification re-versions, as candidates; the same held
  for E-042's two links in GTWPE-FLOW-10. Repaired in *Everything else the check covered*, *What changes*,
  *Member dispositions*, *Scope* and *Candidates*.

After the repair, the session ran D1, D2 and D6 again: both record checks exit 0, on the record at `ANALYZING` and
on a scratch copy at `ANALYZED`; the front matter parses, the request is verbatim and all 16 tables are even; and
83 of 83 repository quotations are found, the repair's own included.

### Diff check (A6)

- **The checker.** One fresh general-purpose subagent, GTWPE-TW-FLOW-RULINGS-ANALYZE-DC, neither forked nor
  context-inheriting, handed nothing but its brief's repository path, `ANALYZE-DIFFCHECK-BRIEF.md`, committed and
  pushed at `798b4c3` before it was spawned, at 06:45Z. It confirmed the brief's sha256,
  `6e8adccf0b4f1a5f05fccdc38e7254050021df83b7ce1d864f805809138d512d`, and that `798b4c3` adds only the brief to
  `a14fcf3`. This is the one check of the repair's diff that `D26-A` rule 2 allows.
- **The run.** It read the record at `a14fcf3` whole and the repair diff over `cc6b923..a14fcf3`, read no Notion
  page and wrote nothing. It ran for about 36 minutes, and the harness reported 513,405 subagent tokens. The
  harness saved one oversized output of its, a grep of `ERRORS.md`'s row headings, which holds no prompt body
  (*Harness files*).
- **The capture.** `capture.py` read its transcript, found by the path the harness gave for its agent ID, twice,
  as for the reviewers (one `SubagentHandback` call, at transcript line 607, 16,977 characters), and wrote
  `ANALYZE-DIFFCHECK.md`: 17,052 bytes, sha256 `99785e02d394c61badc4ea12120e87313b031e61d0aa1109b54b0e3b7d12260c`;
  first line `0`.

**Result: no required defect; RQ-1 to RQ-7 each fixed where *Full review (A6)* says; 8 listed, DC-L1 to DC-L8.**
The count of distinct confirmed required defects went from 7 to 0. Six of the eight listed findings sit in text
the repair added, which is `D26-A` rule 5's second stop signal; the cap is reached in any case, so §A goes to
Nathan with every open finding listed. The session refuted one: DC-L4 says ITEM-03's new quotation of GTWPE-FLOW-10's
B1 step 4 could not be checked, and the session found it verbatim in its third fetch of that body, read after the
repair.

### Listed findings, accepted as risks (A6)

Not repaired, by `D26-A` rule 4; each goes to Nathan with its reason, and repairing one is his opt-in. Where
two rounds found the same thing, it is listed once.

| Finding | Reason it stays listed |
|---|---|
| A's L2, B's L7: S-7 against "they only get one SECTION"; the record prompts' drift control | RQ-1's repair derives S-7 from his words of 2026-10-07 (risk 6), and the record prompts' check that nothing else changed now covers every change they make. `PLAN` makes that check exact |
| A's L3: ITEM-07 as an open question | §A states that ITEM-07 differs from PE40's check and that dropping it leaves the rest unchanged; his approval decides it |
| A's L4: files only do not stop a facilitator's interpretation arriving as a file | A failure path. `PLAN` can carry the Intake's rule, that the request is Nathan's words where the files record them, into the entry contract, within ITEM-07 |
| A's L6: no accounting reason for a superseded addendum | Low. `PLAN` sets the accounting list |
| A's L7, B's L11: the triage pass's return is inline | Loud: `PLAN` makes the return a file or names it as an exception |
| A's L8, B's L1: ITEM-02's table omits passages *Scope* counts | *Scope* is the complete measure, and `PLAN`'s anchors and `D26-E` search work from it |
| A's L9, B's L4: the handoff rows F3, F5, F6 and F9 and the *Common rules* | `PLAN` settles each row against both sides, as tier 2 requires |
| A's L10: TW-TRIAGE-10's ruling 3 sections against its items | Low; the dispositions at `EXECUTE` |
| A's L11: the catalog's *Approved design* entry names C1's §A and design v1.2, which these rulings reverse in part | Low to moderate. The decision record governs; X4 could add a pointer to GTWPE-D2 to GTWPE-D4 if Nathan opts in |
| A's L12, B's L15: the PF27 gate's and C5's reversals of C1's approved §A are not rows of the S table | §A states both (ITEM-03; ITEM-04's *C5*), and the return to Nathan names them |
| A's L15, B's L18: the predicted cost | Now 11, with Q-1 and this mode's diff check; the calibration bullet says it may cost more |
| A's L16, B's L14: the Intake's table maps not every word of his | Low; no item changes |
| A's L18: the H13 exception admits any text in an approval | Low; `D21` requires his approval quoted |
| A's L19: ruling 2's reach omits GTWPE-FLOW-10's B6 and its pull-request text | Low; `PLAN`'s counts |
| A's L20: a PF20 pass may not fit (PF20 and PF10 read whole) | Likelihood unknown, and S1 stops loudly; `PLAN` tests S1 for a record pass |
| A's L21, B's L19: *Member dispositions* omits `glow-artifact-storage`, `glow-workspace-currency`, the GCFPE register and the Flow Index | Low; none changes |
| A's L22: ITEM-02's "clear in the Operations Hub" and the stale callout N-1 | N-1 is outside the route; the return asks Nathan to authorize it with X4 |
| B's L2: "All six TW prompts" includes TW-TRIAGE-10, which has no *Turn preflight* | Loud at `PLAN`'s anchors |
| B's L3: `closure.state_sharers` leaves out the record prompts and TW-APPLY-10, which share `PARTIAL_PACKAGE` (C3) | No effect: every member the closure names changes here |
| B's L6: S-7 against E-010, which stays his | RQ-2's repair cites §9.1.1 whole; S-7's update keeps a record's earlier rows and identity. The canon conflict stays his |
| B's L9: S-3 reaches direct invocations | S-3 is listed for his approval as a reading |
| B's L10: without a selected boundary, "leave it out" needs a form | Loud; S-1's decision file carries it, and `PLAN` sets the form |
| B's L12: a run in which every addendum waits and nothing is drafted has no stated result | Low; `PLAN` states it |
| B's L16: *Scope*'s `git grep` count for the decision record and the checker used only some of ruling 1's terms | With all of them, by `git grep` again: five lines in the decision record and seven ignoring case, the extra ones its own name, "decision record", and a title, "the Change Process Guide"; and two lines in the checker, four ignoring case. None is text the rulings contradict |
| B's L17: PART-01 has no `name` | Neither validator checks it |
| B's L20: no FUNC-001 match | `PLAN`'s `D26-E` search states the functional test: does anything make a run or pass take, or a handoff carry, more than the prompt to run and files |
| DC-L1: ITEM-03 counts an addendum as already represented on "a drain's verified `no redlines` with its exact equivalence location", but a drain's no-change return is exactly `no redlines`, and F3 and F8 do not change | The location is the basis of the drain's own verified coverage, which its rules already require; a return that names it in a file would change F3 and F8, which §A did not measure. Certain to need settling at `PLAN`, which would stop and return loudly. A one-line repair, at Nathan's opt-in |
| DC-L2: S-6 and the first live run update PF30 from PF10 changes alone, against architecture §9's "The agent must not update PF20 or PF30 from PF10 alone", which §A does not name, and *Everything else* still lists §9 as unchanged | Nathan's ruling in E-052, given on 2.14's change to PF30 itself, supports the update, and risk 6 states it. Naming §9 beside risk 6 and taking it off the unchanged list is a one-line repair, at his opt-in |
| DC-L3: "A run Nathan starts is that maintenance" does not hold for a CRD Specification's record of an in-flight CRD | Low. Its canon timing is E-010's open conflict, which stays his |
| DC-L4: the new quotation of GTWPE-FLOW-10's B1 step 4 is unverified | Refuted by the session: verbatim in its third fetch of that body |
| DC-L5: N-3 omits E-033 and E-042, which ITEM-08 now fixes, and the Intake still files E-033 among the rows not taken | Outside the route; the return names both for N-3 |
| DC-L6: risk 14's versionless name departs from answer 2's letter; its 2.14 quotation stops before "artifact, plan, ledger, report, or addendum"; a lettered PF10 set is several files | Low; `PLAN` sets the forms, with a loud stop at intake at worst |
| DC-L7: the closure hold-back is presented as canon's requirement, though §2.0.19's bullet also says "preparation does not prove physical drainage" | The stricter reading errs toward waiting, visibly; low |
| DC-L8: the triage pass alone still decides which documents an addendum bears on | Nathan's design, triage at execution time (architecture §2), with B1 step 4's "route it" when unsure |

### Harness files (`D22` condition 5)

- **Inline fetches, held only in this session's transcript**, which the harness keeps and leaves to its
  teardown:
  - GTWPE-MGMT-10 100526.2, three times: at the mode's start, in the dry run, and after this session's context
    was compacted, before A6 relied on it again (*Reading prompt bodies*).
  - GTWPE-FLOW-10 100726.1 and TW-DRAIN-20 100626.2, three times each: for the analysis, in the dry run, and
    once more to settle D5's two counts.
  - TW-TRIAGE-10, TW-DRAIN-10, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10, twice each: for the analysis and in
    the dry run.
  - GCFPE-MGMT-10's proposed body and `091426.1`, at A0, for their edit times.
  - The control pages: the GTWPE parent page, with the catalog, the selection page, *HDE TW* and the
    architecture page, each for the analysis and again in the dry run, and the parent page once more for the
    architecture page's ID.
- **Harness saves**, each read by a script that printed only what its check needed:
  - `mcp-Notion-notion-fetch-1791349522422.txt`, the PE Metaprompt `091426.1`: its edit time, for A0;
  - `mcp-Notion-notion-fetch-1791349540466.txt`, the register: its edit time and the *Current selection*
    rows that name GCFPE-MGMT-10 and the PE Metaprompt;
  - `mcp-Notion-notion-fetch-1791349580299.txt` and `mcp-Notion-notion-fetch-1791351317984.txt`, the
    Operations Hub, a control page, for the analysis and the dry run: its edit time, its current TW section
    and the callout at its top;
  - `toolu_01GEHJZjduBWJSV7YUUCc4tt.json` and `toolu_01EybegVeomBnkjMKpc7qGE4.json`, *Alpha 1*, a control
    page, for the analysis and the dry run: its edit time and its headings.

  No save was hashed or compared as a body's identity. The harness refused this session's `rm` of the saves
  ("Session Transcript Tampering"), so they are left to its teardown and never read again (`D22` condition 4).
- **Saves that hold no prompt body:** `bz21dfdmt.txt`, an oversized command output of HDE Governance §9.1; and
  `b0hdnp35v.txt`, reviewer B's oversized grep of `ERRORS.md`, which the session did not open.
- **The reviewers' transcripts**, the output files the harness gave for their agent IDs in this session's tasks
  directory. They hold no prompt body: neither reviewer read a Notion page. `capture.py` read each twice for its
  one `SubagentHandback` call, first printing only the call's shape, then writing its message to
  `ANALYZE-REVIEW-A.md` or `ANALYZE-REVIEW-B.md`. They are left to the harness's teardown.
- **The checker's transcript**, the output file the harness gave for its agent ID in this session's tasks
  directory. It holds no prompt body. `capture.py` read it twice for its one `SubagentHandback` call and wrote
  `ANALYZE-DIFFCHECK.md`. Its run left one harness save, `bhytaqauy.txt`, a grep of `ERRORS.md`'s row headings,
  which holds no prompt body and which the session did not open. Both are left to the harness's teardown.
- **The session transcript.** A1's verbatim copy of the request needed Nathan's message, which only the
  transcript held. A script read it once, for that message alone, and saved it to `request.txt` in the
  scratchpad.
- **Scratch files**, in this session's scratchpad, none holding a prompt body: `request.txt`; `build_a1.py`
  and `build_a.py`, which build this record; the drafts of its body; `dry/quotes_repo.py`, D6's check, run again
  after the repair; `capture.py`; the briefs' source; and the scratch copies of this record for the dry run.

### Canon and rulings relied on

Canon read from `docs/pfcanon/` on `main` at `128836a`, cited by title and section.

| Source | Used for |
|---|---|
| **HDE Governance** §9.1.6 | Every other member given a disposition with a reason; affected producers, consumers and interacting skills reconciled in one coherent successor selection, an edited subgroup not ready while a counterpart is incompatible (the one part; Q-1); author, checker and acceptor recorded at `EXECUTE`; management prompt bodies single-homed in Notion; external references, in durable bodies and in temporary handoff prompts, by controlled directory and versionless document name, with exact source binding kept in run artifacts (risk 14) |
| **HDE Governance** §9.1.1, with *Historical drainage* | PF20 and PF30 are historical homes the active workflow does not update; only a separately authorized historical drainage action adds to them; existing content and identities are preserved as dated history; PF10 drainage after closure is an authorized manual operator's. Read for ITEM-05's canon check only, and not argued from (E-054) |
| **HDE Governance** §2.0.19, *Post-closure maintenance ordering*, and §9.1.5 | PF10 drainage follows the Isis closure decision (ITEM-03, S-4) |
| **HDE Build Notes**, *Precedence, versioning, and scope* §1, §2 and §5 to §9 | An addendum governs until drained; drained guidance leaves at formal revision; every addendum is searched (ITEM-03) |
| **HDE Build Notes** 2.14 | PF27 and PF30 adopt the terms on their next revision (ITEM-05, S-7); the reference posture, "Do not pin a PF file version in a prompt" (this record; risk 14) |
| **HDE Build Notes** 2.37 | HDE-EPIC040's QA verdict, which "is not closure" (ITEM-05, the first live run) |
| **HDE Build Notes** 2.29 | Canon from `docs/pfcanon/` on `main`; change-process documents in `docs/ephemeral/`; the canon search before any analysis |
| **HDE Build Notes** 2.38 | No provider or product is required; the surface that writes Notion confers no permission (`EXECUTE`'s writes) |
| **Change Process Guide**, *Post-QA documentation drainage ordering (normative)* | Drainage after the change's QA (ITEM-03) |
| **Change Process Guide** §1.1.2, §3.5.1 and §6.3; **Plan Templates** §2, *Historical-only posture (normative)* | PF20 takes an epic's record only once, at epic close, and never an in-flight epic's (ITEM-05, S-6) |
| **HDE CRD Records** §1, §2, §4.2 and §6 | CRD history is PF30's; an existing record is updated in place with one appended row; a closed volume still takes updates; rollover is the Product Owner's (ITEM-05) |
| **HDE Phased Epics** §0, *Drain posture* | Epic history is PF20's; prior records are not mass-edited (ITEM-05) |
| Nathan's rulings of 2026-09-28, `CHECKPOINT.md` §8 | Eligibility: PF03 and the Canon-titled documents; PF20 and PF30 through their own prompts; PF10 never a target (ITEM-03, ITEM-04) |
| The architecture record, Nathan's words of 2026-09-29 and later | The target, answers 1 to 8, *Redlining discipline*, the stop rule, no model advice (ITEM-02 to ITEM-08) |
| GTWPE-D1 (`gtwpe.decision-record.md`) | Kept whole by every changed prompt (*GTWPE-D1, prompt by prompt*) |
| Nathan's rulings of 2026-10-07 (PE40-INIT rulings 1 to 5; the ledger's E-044, E-046, E-052 and E-053) | The request |
| `gcfpe.decision-record.md` `D21`, `D22`, `D23`'s clarification, `D24`, `D26` | One Modification in one part; reading bodies and harness files; workers within the task; fresh reviewers on a committed brief; the bounded review, `D26-E`'s old-text search and `D26-F`'s first trigger |
| `AGENTS.md` | The canon-first rule; PF canon read-only; the pull request's headings |

**Canon is silent** on how a technical-writing prompt's inputs and handoffs are given: no PF document governs the
GTWPE's flow, and a search for `execution prompt` finds nothing. On drainage it sets the timing (after the change's QA
and its closure decision) and keeps an addendum authoritative until drained, without saying which run drains
it. Nathan's
rulings govern there. This record uses PF03's omission marker, `[OMITTED]`, in quotations.
