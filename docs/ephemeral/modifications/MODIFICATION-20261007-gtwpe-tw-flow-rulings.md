---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261007-gtwpe-tw-flow-rulings
status: ANALYZING
targets: [prompt, rule, notion_control]
gate_tier: 2
closure:
  upstream: [GTWPE-FLOW-10, TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-TRIAGE-10]
  downstream: [GTWPE-FLOW-10, GTWPE-MGMT-10, TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20, TW-TRIAGE-10]
  state_sharers: [TW-DRAIN-10, TW-DRAIN-20]
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 9
interaction_cost_actual:
estimate:
  plan: "about 9 h, not counting waits for Nathan: the edits to eight bodies, as anchors and new texts, authored through the PE Metaprompt from this analysis, with each passage counted twice; the decision record's three entries and the handoff table's rows; the selection page's three writes, the three current-release notes and the catalog rows; and PLAN's dry run, with its two-sided check of every invocation against the bodies it reaches, one full review and at most one diff check. Tokens are not measured"
  execute: "about 5 h, not counting the waits for Nathan's merges: eight new pages, each duplicated, titled, edited and read back whole; the decision record and the handoff table committed, and their merge detected on main (X2, X3); the selection writes and the three notes, read back; the catalog (X4); and the record at COMPLETE (X5). Tokens are not measured"
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-10-07
    required_open: 0
    outcome: "By this session, read-only, before any full review: both record checks exit 0 on a scratch copy at ANALYZED; the front matter and every table parse, and the request is verbatim; A0 reproduces at 128836a; every member and control page is unchanged. It found and corrected, before the review: two scope counts (GTWPE-FLOW-10 has 20 sections; TW-DRAIN-20's ruling 1 reach is 9), two unstated exceptions, four quotations (66 of 66 repository quotations now found, and every Notion quotation by a second reading), F9 missing from the tier 2 list, and the D26-E search not yet run over gtwpe/. None left open"
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
analyze_approved_by: ""
analyze_approved_date: ""
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

- **GTWPE-D2**, inputs: ruling 1, both sentences.
- **GTWPE-D3**, PF10 drainage: ruling 2's two sentences, and E-044's and E-052's "all pf docs should be updated
  based on context and scope, not whether or not the addenda specify a drain target."
- **GTWPE-D4**, PF20 and PF30: ruling 3's two sentences, E-046's and E-052's "If there is a spec involved, those
  docs are updated. if not, then not. its basic.", and E-053's "PF30 and PF20 DON't need the redliner. They
  should not need that step. They never have."

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
it rules out. The plan sets the exact forms.

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
  scope* §1), and removes drained guidance when it is formally revised (§7). The Change Process Guide's
  *Post-QA documentation drainage ordering (normative)* puts drainage "only after all QA tasks for the epic are
  complete", which is GTWPE-FLOW-10's B1 step 5 hold-back. Nathan's 2026-09-28 ruling "No, pF10 will NEVER be a
  merge target, EVER>" stands, as `CHECKPOINT.md` §8 records it.

What follows, for the plan: in a run with a PF10 source, every addendum is accounted for in `RUN.md` and the
pull request: the documents it drains into; where it is already represented, by the triage pass's reading or a
drain's verified `no redlines`; or why it cannot drain in this run (held back by canon's post-QA ordering, a PF20 or PF30 part with no specification, or a home that is no
eligible document, such as PF10 itself). No run ends `RUN_NO_CHANGE` or `RUN_REVIEW_READY` with an addendum
unaccounted for, and `RUN_NO_CHANGE` remains only for a run in which every addendum is shown already
represented, or which has no PF10 source and changes no document.

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
     return names, for each addendum, the documents it drains into, or why none in this run (ITEM-03).
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
  replaces it: with a specification in the run's inputs, the run updates PF20 for an Epic Specification
  (TW-RECORD-10) or PF30 for a CRD Specification (TW-RECORD-20); without one, neither. That Epic history is PF20's
  and CRD history PF30's is the documents' own scope (HDE Phased Epics §0; HDE CRD Records §1).
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
  since PF30 never goes to the redliner (E-053). So when a run revises a PF30 volume, TW-RECORD-20 also carries
  each applicable PF10 change that bears on that volume in context and scope (ITEM-03), beyond its one record.
  When no CRD Specification is in the run, PF30 is not revised, and the run accounts for such an addendum as
  waiting for one (ITEM-03).
- **Canon.** HDE Governance §9.1.1, *Historical drainage*, reserves PF20 and PF30 additions to "a separately
  authorized historical drainage action". Nathan rejected arguing his rule from it ("this is meaningless
  distinction", E-054), and his rule governs the GTWPE. Read for the canon-first rule only: it conflicts with no
  canon, since the run Nathan starts with a specification is such an action. E-010, canon's own conflict on PF20
  and PF30 records, stays his.
- **The first live run** (HDE Build Notes and the HDE-EPIC040 Specification, as PE40-INIT names them): an Epic
  Specification, so PF20 is updated through TW-RECORD-10, and HDE Phased Epics has no HDE-EPIC040 record yet
  (`git grep -c HDE-EPIC040` is 0), so the record is new; no CRD Specification, so PF30 is not revised.

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

### What the analysis settles, for Nathan's approval

Each follows from his words and the canon cited; none is his own words, so each is listed for his approval.

| # | Settled | From |
|---|---|---|
| S-1 | Ruling 1 covers Nathan's own inputs to a run. A resume, a decision at a stop and a rollover decision reach a run as files; a run or pass given anything beyond the prompt to run and its files stops at intake and names it | Ruling 1; GTWPE-FLOW-10's existing intake stop |
| S-2 | Attached files stay allowed beside repository paths | Answer 2 |
| S-3 | No selected boundary anywhere: every pass reads every source whole | Ruling 1; E-044 |
| S-4 | Every addendum accounted for; `RUN_NO_CHANGE` only as ITEM-03 states | Ruling 2; E-044's ruling; HDE Build Notes front matter §1 and §7; the Change Process Guide's post-QA ordering |
| S-5 | TW-TRIAGE-10 is the run's triage pass, evaluating every source; it stays optional for a direct invocation | Ruling 2; architecture §2 and §7 |
| S-6 | Epic Specification → PF20 through TW-RECORD-10; CRD Specification → PF30 through TW-RECORD-20 | Ruling 3; HDE Phased Epics §0; HDE CRD Records §1 |
| S-7 | The record prompts make every change to their document in a run: an existing record's update, and the PF10 changes that bear on the document in context and scope, such as 2.14's terms for PF30 | E-053's ruling; E-044's ruling; HDE Build Notes 2.14; HDE CRD Records §4.2 and §6; HDE Phased Epics *Drain posture* |
| S-8 | GTWPE-MGMT-10's own request is files only (ITEM-07) | Ruling 1; E-048 |

### What changes, by surface

| Surface | Route (*How each kind of target changes*) | Items |
|---|---|---|
| GTWPE-FLOW-10 | A new versioned sibling under the GTWPE parent page; the catalog selects it at X4 | 02, 03, 04, 05 |
| GTWPE-MGMT-10 | A new versioned sibling under the GTWPE parent page; the catalog selects it at X4 | 07 |
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
| GTWPE-MGMT-10 | Affected | ITEM-07 |
| GTWPE-FLOW-10 | Affected | ITEM-02 to ITEM-05 |
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
| `tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Unaffected | They do not run this release (the selection page), and C6 retires the Flowmaster |
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
| TW-RECORD-10 | The updated PF20 and its proof log, before; after, also for an existing record's update | The proof log and its eight items are kept; what it "also records" (where the entry went, the control fields before and after, that nothing else changed) is extended to an update |
| TW-RECORD-20 | The updated PF30 volume, and on a rollover the next volume's review copy, each with its proof log; after, also for an update | The same; one proof log per file, as now |

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
5. **Held-back addenda** wait for their epic's QA, by canon's post-QA ordering; the run accounts for them.
6. **TW-RECORD-20's role widens** from inserting one section to every change a run makes to its volume (S-7),
   beyond Nathan's "they only get one SECTION" of 2026-09-29. His "DON't need the redliner" of 2026-10-07 is the
   later word.
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
14. **Versioned filenames.** An execution prompt is a one-off run input and may name a PF document by its
    versioned path; the run resolves it on `main` and records its blob, and stops if that file is no longer there
    (S2). The durable bodies keep naming PF documents without a version, as HDE Build Notes 2.14's reference
    posture and HDE Governance §9.1.6's reference rule ask; `PLAN` sets each invocation's form within both.

### Defect classes matched (`ecosystem-change-management.md` §4)

- **DERIV-001,** nearest: the PF27 gate is a summary of Nathan's message restated as a rule (plan v1.2 §1), and
  the PF20 and PF30 authorization gate a canon reading set against his recorded architecture (E-046).
- **SCOPE-001:** the scope above is measured by broad match minus exceptions, with its method.
- **GUARD-001,** as a limit: the GTWPE has no registry, so a ruling's guard is each page's readback and `D26-E`'s
  search, as in C1 to C4.
- **SCOPE-002:** the selection writes and the notes touch only each page's current TW section (E-038's lesson).

### Candidates for separate Modifications (recorded, not taken)

- **E-042:** `RUN.md` as inline code on GTWPE-FLOW-10, and a check for bare file names. This Modification makes
  GTWPE-FLOW-10's next version, so Nathan may add it at approval.
- **E-033:** GTWPE-MGMT-10's "until G5", six places; **C3's F-1:** its route's "lists the eight members", where
  TW-ALPHA has six; and its two pointers to the design package's §6 handoff table, which moved in C4. GTWPE-MGMT-10 gets a new
  version here, so Nathan may add these at approval.
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

None. S-1 to S-8 are settled from his words and canon, and his approval accepts them.

### Readiness and interaction cost

`READY`. No item waits on another item's execution, every surface's scope is measured, and no ruling is open.

    interaction_cost = 0 open rulings + 2 + 5 review rounds + 0 skill review cycles + 0 installs + 2 merges = 9

- **Review rounds:** this mode's dry run and one full review by two reviewers; `PLAN`'s dry run, one full review
  and one check of a repair's diff, if needed.
- **Merges:** the branch's pull request at X2, which carries the decision record and the handoff table; then the
  record's pull request after X5.
- **Splitting saves nothing:** the items share GTWPE-FLOW-10, the handoff table and the selection. Moving ITEM-07
  to a run of its own would add two approvals, two review rounds and a merge.
- **Calibration:** C2 to C4 predicted 8, 7 and 7 and cost 14, 11 and 13.

**The estimate,** in the front matter: `PLAN` about 9 h and `EXECUTE` about 5 h, not counting waits for Nathan.
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
- **A save that holds no prompt body:** `bz21dfdmt.txt`, an oversized command output of HDE Governance §9.1.
- **The session transcript.** A1's verbatim copy of the request needed Nathan's message, which only the
  transcript held. A script read it once, for that message alone, and saved it to `request.txt` in the
  scratchpad.
- **Scratch files**, in this session's scratchpad, none holding a prompt body: `request.txt`; `build_a1.py`
  and `build_a.py`, which build this record; the drafts of its body; `dry/quotes_repo.py`, D6's check; and the
  scratch copies of this record for the dry run.

### Canon and rulings relied on

Canon read from `docs/pfcanon/` on `main` at `128836a`, cited by title and section.

| Source | Used for |
|---|---|
| **HDE Governance** §9.1.6 | Every other member given a disposition with a reason; affected producers and consumers reconciled in one coherent successor selection, an edited subgroup not ready while a counterpart is incompatible (the one part); author, checker and acceptor recorded at `EXECUTE`; management prompt bodies single-homed in Notion; external references by versionless document name (risk 14) |
| **HDE Governance** §9.1.1, *Historical drainage* | Read for ITEM-05 only, and not argued from (E-054) |
| **HDE Build Notes**, *Precedence, versioning, and scope* §1, §2 and §5 to §9 | An addendum governs until drained; drained guidance leaves at formal revision; every addendum is searched (ITEM-03) |
| **HDE Build Notes** 2.14 | PF27 and PF30 adopt the terms on their next revision (ITEM-05, S-7); the reference posture, by name and section, no pinned version (this record; risk 14) |
| **HDE Build Notes** 2.29 | Canon from `docs/pfcanon/` on `main`; change-process documents in `docs/ephemeral/`; the canon search before any analysis |
| **HDE Build Notes** 2.38 | No provider or product is required; the surface that writes Notion confers no permission (`EXECUTE`'s writes) |
| **Change Process Guide**, *Post-QA documentation drainage ordering (normative)* | A held-back addendum drains after its epic's QA (ITEM-03) |
| **HDE CRD Records** §1, §2, §4.2 and §6 | CRD history is PF30's; an existing record is updated in place with one appended row; a closed volume still takes updates; rollover is the Product Owner's (ITEM-05) |
| **HDE Phased Epics** §0, *Drain posture* | Epic history is PF20's; prior records are not mass-edited (ITEM-05) |
| Nathan's rulings of 2026-09-28, `CHECKPOINT.md` §8 | Eligibility: PF03 and the Canon-titled documents; PF20 and PF30 through their own prompts; PF10 never a target (ITEM-03, ITEM-04) |
| The architecture record, Nathan's words of 2026-09-29 and later | The target, answers 1 to 8, *Redlining discipline*, the stop rule, no model advice (ITEM-02 to ITEM-08) |
| GTWPE-D1 (`gtwpe.decision-record.md`) | Kept whole by every changed prompt (*GTWPE-D1, prompt by prompt*) |
| Nathan's rulings of 2026-10-07 (PE40-INIT rulings 1 to 5; the ledger's E-044, E-046, E-052 and E-053) | The request |
| `gcfpe.decision-record.md` `D21`, `D22`, `D23`'s clarification, `D24`, `D26` | One Modification in one part; reading bodies and harness files; workers within the task; fresh reviewers on a committed brief; the bounded review, `D26-E`'s old-text search and `D26-F`'s first trigger |
| `AGENTS.md` | The canon-first rule; PF canon read-only; the pull request's headings |

**Canon is silent** on how a technical-writing prompt's inputs and handoffs are given: no PF document governs the
GTWPE's flow, and a search for `execution prompt` finds nothing. On drainage it sets the timing (post-QA
ordering) and keeps an addendum authoritative until drained, without saying which run drains it. Nathan's
rulings govern there. This record uses PF03's omission marker, `[OMITTED]`, in quotations.
