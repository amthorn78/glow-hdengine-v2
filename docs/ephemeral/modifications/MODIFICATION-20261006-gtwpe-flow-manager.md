---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261006-gtwpe-flow-manager
status: ANALYZING
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
  plan: ""
  execute: ""
reviews: []
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
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20261006-gtwpe-flow-manager

C4 of the writing-side build: the Flow Manager, a new GTWPE prompt that runs the whole technical-writing
flow in one session Nathan starts, and leaves a review-ready pull request of complete replacement PF
documents with their proof logs.

## Intake

Not through triage. The request came from PE39 on 2026-10-06 and is copied verbatim in the front matter.
It runs C4, the fourth change in the order Nathan approved in MODIFICATION-20261005-gtwpe-writing-side
(§A A.5), through GTWPE-MGMT-10 100526.2. Its eight numbered points, under "What C4 is", are ITEM-01 to
ITEM-09 in its order; its point 8 has two halves, ITEM-08 and ITEM-09. What it puts outside C4 is recorded
in §A, not taken here.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

In progress.
