---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261006-gtwpe-tw-document-rules
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
    statement: "TW-APPLY-10 brings every document-control field of the revised PF forward from the actual change, and the fields agree with one another: the version, the dates, the Last Update Gate, the change or revision history the document's own rules require, and version-sensitive references; the drains draft that change-history entry as a content redline."
    source: "Request item 1; MODIFICATION-20261005-gtwpe-writing-side §A A.4 R4; target architecture §5"
    disposition: ""
  - id: ITEM-02
    statement: "TW-APPLY-10 and the drains derive the Last Update Gate from the actual source the update used, by Nathan's rule (answer 6), which replaces the current rule; it needs no PF10 change, and the analysis records that the C1 approval's check for a PF10 sentence no longer applies, which closes ledger E-039."
    source: "Request item 2; Nathan's answer 6 and his ruling of 2026-10-06, in the target architecture record; ledger E-039"
    disposition: ""
  - id: ITEM-03
    statement: "No document the TW prompts produce says Draft or carries placeholders, TODOs, editorial notes or a stale status, except where canon requires it: a new PF30 volume's review copy."
    source: "Request item 3; MODIFICATION-20261005-gtwpe-writing-side §A A.4 R5; target architecture §4; HDE CRD Records §6"
    disposition: ""
  - id: ITEM-04
    statement: "TW-DRAIN-20 judges every potentially affected PF09 row on all the evidence, never leaves a row open for lack of an instruction, never closes one only because related work shipped, and the resulting PF09 shows the project's current state."
    source: "Request item 4; MODIFICATION-20261005-gtwpe-writing-side §A A.4 R6; target architecture §8"
    disposition: ""
  - id: ITEM-05
    statement: "TW-RECORD-10 and TW-RECORD-20 write their one section into a copy of the PF at the repository path the invocation names, by an exact insertion, with a report, set that document's control fields as ITEM-01 does, and reconcile the original specification with every applicable PF10 change; TW-RECORD-20 treats PF30 as a volume family, and TW-RECORD-10 keeps PF20's single structure."
    source: "Request item 5; MODIFICATION-20261005-gtwpe-writing-side §A A.4 R2, R3, R7 and R8, and A.6 (E-010); target architecture §9; Nathan's answer 8; HDE CRD Records §6"
    disposition: ""
  - id: ITEM-06
    statement: "Once TW-RECORD-10 and TW-RECORD-20 write an updated PF20 or PF30 Markdown file, each writes a separate proof log beside that file, named after it, with all eight minimum items of GTWPE-D1."
    source: "Request item 6; GTWPE-D1 (docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md); MODIFICATION-20261005-gtwpe-writing-side §A A.8"
    disposition: ""
  - id: ITEM-07
    statement: "TW-RECORD-20 takes its inputs as attached files or repository paths, never from Google Drive or ChatGPT Library (K-12)."
    source: "Request item 7; MODIFICATION-20261005-gtwpe-tw-repository-io K-12; HDE Build Notes 2.29 PF10-CANON-001"
    disposition: ""
  - id: ITEM-08
    statement: "A new TW-ALPHA release selects the changed prompts, with its Current operation on the Glow Technical Writing Ecosystem page."
    source: "Request item 8"
    disposition: ""
parts:
  - id: PART-01
    name: "to be set by ANALYZE (A2)"
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06, ITEM-07, ITEM-08]
    class:
    after: []
request: |
  PE39 here, facilitator, on 2026-10-06.

  Where things stand, checked by PE39 today:
  - C2 of the writing-side build is COMPLETE on main (amthorn78/glow-hdengine-v2#577, merged at `7c18c26`). TW-ALPHA-20261006.1 is selected: TW-TRIAGE-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10 at 100626.1. They read PF canon from `docs/pfcanon/` on `main`, write at the repository path each invocation names under `docs/ephemeral/`, and never merge. TW-DRAIN-10, TW-DRAIN-20 and TW-APPLY-10 write a GTWPE-D1 proof log beside each artifact. PE39 accepted C2 against main, both record checks (6/6) and the Notion pages, read live.
  - main is at `b1bd769`. Since the GTWPE catalog's checked-through commit `1dec848`, main gained amthorn78/glow-hdengine-v2#577 (C2's record and its `edits-2.json`, under `docs/ephemeral/modifications/`) and amthorn78/glow-hdengine-v2#578 (the error ledger and the target architecture record, under `docs/ephemeral/gtwpe.rewrite/`). amthorn78/glow-hdengine-v2#579 changes the same two files, if Nathan has merged it. Nothing under `docs/pfcanon/` has changed since `31deec4`.

  Next: run C3, the third change in the order Nathan approved in MODIFICATION-20261005-gtwpe-writing-side (§A A.5), through GTWPE-MGMT-10 — Manage the GTWPE — 100526.2 (Notion page `3f04590a05eb8128b8c8ff3650ab2d5a`): ANALYZE, PLAN, EXECUTE. Follow the published body live and stop at each of Nathan's approvals.

  What C3 is (that record's §A A.1, A.4 rules R2 to R8, and A.5's C3 row; the target architecture record's sections 4, 5, 8 and 9, and Nathan's answers 6 and 8):
  1. Document control (R4). TW-APPLY-10 brings every document-control field of the revised PF forward from the actual change, and the fields agree with one another: the version, the dates, the Last Update Gate, the change or revision history the document's own rules require, and version-sensitive references (architecture section 5). The drains draft that change-history entry as a content redline.
  2. The Last Update Gate. Nathan's rule (answer 6), verbatim: "The Last Update Gate may use the following form: BN + the version number of the PF file used when the source is a PF document. If the source is not PF10 or another PF file, the Last Update Gate may instead use: BN + the source filename. The purpose is to identify the source revision or source artifact that justified the most recent update. The Flow Manager should therefore derive this field from the actual source used for the update rather than copying forward a stale value." It replaces the current rule (the upstream source filenames) in TW-APPLY-10 and the drains. Nathan ruled on 2026-10-06 that it needs no PF10 change: the gate records the source an update used and is not a citation of HDE Build Notes, and 2.30 PF10-CITE-001's own drain list names no document's gate. So the line in the C1 analysis approval, "C3's ANALYZE confirms that sentence is on main", no longer applies. Record that in the analysis; it closes ledger E-039. The architecture record's update of 2026-10-06 holds the ruling.
  3. No Draft (R5). No document produced says Draft or carries placeholders, TODOs, editorial notes or a stale status (architecture section 4), except where canon requires it: a new PF30 volume's review copy (HDE CRD Records §6).
  4. PF09 (R6). TW-DRAIN-20 judges every potentially affected row on all the evidence (updated, left open, closed or otherwise changed). It never leaves a row open for lack of an instruction, never closes one only because related work shipped, and the resulting PF09 shows the project's current state (architecture section 8).
  5. PF20 and PF30 (R2, R3, R7, R8). TW-RECORD-10 and TW-RECORD-20 write their one section into a copy of the PF at the repository path the invocation names, by an exact insertion, never by regenerating the document, with a report, and set that document's control fields as item 1 does. Each reconciles the original specification with every applicable PF10 change, never either alone (architecture section 9). TW-RECORD-20 treats PF30 as a volume family: it works in the right volume, reports when a split looks due, and opens a new volume only when the invocation carries Nathan's rollover decision (HDE CRD Records §6). TW-RECORD-10 keeps PF20's single structure (answer 8). Ledger E-010 stays as §A A.6 carries it (HDE Governance §9.1.1, historical drainage).
  6. GTWPE-D1. Once TW-RECORD-10 and TW-RECORD-20 write an updated PF20 or PF30 Markdown file, GTWPE-D1 binds them: each writes a separate proof log beside that file, named after it, with all eight minimum items. GTWPE-MGMT-10 100526.2's GTWPE-D1 guard applies to every prompt this change touches.
  7. K-12. TW-RECORD-20 takes its inputs as attached files or repository paths, never from Google Drive or ChatGPT Library, as the other five prompts have since C2. Nathan recorded K-12 as a candidate for a separate Modification; it is in C3 because item 5 rewrites the same input rule.
  8. A new TW-ALPHA release, with its Current operation on the Glow Technical Writing Ecosystem page.

  Not in C3: the Flow Manager (C4), including the drafts area's layout and the checks across documents; the Change Manager (C5); adoption (C6); and E-033 ("until G5" in GTWPE-MGMT-10), which stays for C6. E-038 (stale wording in older sections of Alpha 1 and the Operations Hub, with C2's N-2) is PE39's to fix after C3, outside the route; do not raise it again.

  Standing directions:
  - Nathan: "this flow can be simplified, let's not overcomplicate this".
  - Stop rather than produce substandard results.
  - Keep PLAN lean: one dry run and one full review by a single reviewer; a second reviewer or a diff check only if that review finds a required defect.
  - Counts over a prompt body: by script over a harness save where one exists (D22 lets a script print only a count), otherwise by two independent readings, as C2's successor plan did (ledger E-035).
  - TW Flowmaster 1.3.0 has not run the TW-ALPHA releases since C2. Nathan waived its readiness for C2's release only (C2's override); if C3's release needs the same, ask him at ANALYZE.
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

# MODIFICATION-20261006-gtwpe-tw-document-rules

C3 of the writing-side build, the writing flow's document rules: TW-APPLY-10 and the drains carry
every document-control field forward from the actual change, the Last Update Gate by Nathan's rule;
nothing they produce says Draft; TW-DRAIN-20 judges every PF09 row on the evidence; TW-RECORD-10 and
TW-RECORD-20 insert their section into a repository copy of PF20 or PF30, with a report and a proof
log; and a new TW-ALPHA release selects them. The prompts themselves stay in Notion.

## Intake

Not through triage. The request came from PE39 on 2026-10-06 and is copied verbatim in the front
matter. It runs C3, the third change in the order Nathan approved in
MODIFICATION-20261005-gtwpe-writing-side (§A A.5), through GTWPE-MGMT-10 100526.2. Its eight numbered
points, under "What C3 is", are ITEM-01 to ITEM-08, in its order. What it puts outside C3 is
recorded in §A, not taken here.

## §A — Analysis

*Written by MODE = ANALYZE. Requires nothing upstream. Frozen once approved.*

In progress (A1). The analysis follows at A2 to A7.
