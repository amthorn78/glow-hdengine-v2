---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20261006-gtwpe-tw-document-rules
status: PLANNING
targets: [prompt, notion_control]
gate_tier: 2
closure:
  upstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20]
  downstream: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20]
  state_sharers: [TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20]
readiness: NEEDS_RULING
override:
  by: Nathan
  overrides: [readiness]
  reason: "Nathan, 2026-10-06, approving the analysis (Q-1, option (a)): he waives HDE Governance §9.1.6's interacting-skill readiness for tw-flowmaster for this release as well, because C4 replaces the skill, C6 retires it, and a Flowmaster run against the new release stops loudly rather than producing a wrong result. The selection page and the three notes say that tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run it. The validator's vocabulary has no narrower gate, so `readiness` names it; the record's readiness field is ANALYZE's advice and is unchanged"
interaction_cost_predicted: 7
interaction_cost_actual:
estimate:
  plan: "about 4 h: §P for 31 passages and 10 identity lines in five members (anchors, new texts, phrase and absence checks), the selection page's three writes with a new Current operation, the three current-release notes and the catalog's checked-through commit; a dry run that reads the five bodies again, and one full review by a single reviewer. Time is the meter the session can read; tokens are not measured"
  execute: "about 3 h, not counting any wait for Nathan: five new versions (duplicate, title, edits), each read back whole by this session; the selection's three writes, the three notes and the catalog, each read back; the record. Time is the meter"
item_count_at_approval: 8
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-10-06
    required_open: 0
    outcome: "By this session, read-only: both record checks exit 0 on a scratch copy at ANALYZED; the front matter and every table parse, and the request is verbatim; A0 reproduces at b1bd769; the new titles and release label are free; a second, independent reading of a second fetch of the six bodies corrected two counts (version in TW-DRAIN-10, 23 to 24, and in TW-DRAIN-20, 24 to 25, both a kept exception) and confirmed every passage; the record tools need no change. No required defect. No full review"
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
    name: "The TW prompts' document rules: five new versions and the new TW-ALPHA release"
    items: [ITEM-01, ITEM-02, ITEM-03, ITEM-04, ITEM-05, ITEM-06, ITEM-07, ITEM-08]
    class: B
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
analyze_approved_by: "Nathan, 2026-10-06: \"Nathan approves the analysis of MODIFICATION-20261006-gtwpe-tw-document-rules at f8bbb6c (2026-10-06). PE39 checked it: main's modification_validate.py and gtwpe_record_check.py each pass all seven GTWPE records (7/7), the request in the front matter equals PE39's message, main is still b1bd769, and the branch changes only the record. Q-1: option (a). Nathan waives HDE Governance §9.1.6's interacting-skill readiness for tw-flowmaster for this release as well, because C4 replaces the skill, C6 retires it, and a Flowmaster run against the new release stops loudly rather than producing a wrong result. The selection page and the three notes say that tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run it, and the override block records the waiver. The Last Update Gate (ITEM-02 and risk 3): Nathan ruled on 2026-10-06, verbatim, \"the gate name for a non PF10 source should just be the filename of the source. that simple\", and \"I would never use a PF target as a source, that does not make sense.\" So a change's source is PF10 or a file that is not a PF document, never another PF. The gate is BN and the PF10 version used when the source is PF10, and the source's filename alone, with no BN, for any other source. PLAN builds the rule in this form, where the analysis says BN and the source filename, and risk 3 falls away. The ruling is recorded in the architecture record's update of 2026-10-06, \"the gate for a source other than PF10\", in amthorn78/glow-hdengine-v2#579. Continue to PLAN: one dry run and one full review by a single reviewer, and a second reviewer or a diff check only if that review finds a required defect. Stop at Nathan's plan approval, and report in at most five plain sentences ending with exactly what he must approve.\""
analyze_approved_date: 2026-10-06
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

This session ran the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
100526.2*, the version the catalog selects. The mode started at 2026-10-06T11:18:32Z, when PE39's request
arrived, with `main` at `b1bd769`. A context compaction came during the consult, before any step relied on
the body; the body was then fetched live, edited 2026-10-05T16:36:11.384Z. The request is in the front
matter, verbatim. The record is on `docs/20261006-modification-gtwpe-tw-document-rules`, its open pull
request amthorn78/glow-hdengine-v2#580.

### Consult

- **Repository**, on `main` at `b1bd769`.
  - C1's record, MODIFICATION-20261005-gtwpe-writing-side: §A A.1, A.4 (R2 to R8), A.5's C3 row, A.6
    (E-010), A.7 and A.8, and its `analyze_approved_by`.
  - C2's record, MODIFICATION-20261005-gtwpe-tw-repository-io, whole: its §A is this analysis's model, and
    its §E holds the readbacks of the six members and the four control pages.
  - The target architecture record, whole: §§4, 5, 8 and 9, and Nathan's answers 6 and 8.
  - The error ledger: E-010, E-033 and E-038.
  - amthorn78/glow-hdengine-v2#579, open and unmerged at head `3db2cf2`: its update to the architecture
    record ("no PF10 sentence for the Last Update Gate") and ledger row E-039.
  - In `docs/prompt_ecosystem_management/`: `modification-template.md` 2.1, `ecosystem-change-management.md`
    §2 and §4, `gtwpe/gtwpe.decision-record.md` (GTWPE-D1) and the header of `gtwpe/gtwpe_record_check.py`.
  - No other `docs/*-modification-gtwpe-*` branch carries this ID (`git ls-remote`).
- **Canon**, on `main` at `b1bd769`, unchanged since `31deec4`.
  - Searched with `git grep` for `Last Update Gate`, `Invocation tag`, `Draft`, `status`, `history`,
    `change log`, `volume`, `rollover` and the PF09 status values.
  - Read in full: Technical Writing Best Practices §3, §7, §14 and §15.1; HDE Governance §9.1.1, §9.1.6,
    §9.2 and §9.3; HDE Build Notes 2.29 PF10-CANON-001, 2.30 PF10-CITE-001 and 2.38 PF10-AINEUTRAL-001;
    HDE CRD Records §0 to §3.3, §4.2, §6 and §7; HDE Phased Epics' front matter and §0; HDE Build Checklist
    — Distillation §0.3 and §0.6.
- **Notion, read-only.** The GTWPE parent page and catalog; the selection page, *Alpha 1*, *HDE TW* and the
  Operations Hub; the six TW members (*The members, read live*); the lineage sources (A0).

### Drift check (A0)

`git fetch origin main`; the commit examined is `b1bd7699243395a708a1d49a82df7e0b61efcccb` (`b1bd769`),
#578's merge.

**(a) The lineage sources.** Searches with highlights off on `PE Metaprompt` and `GCFPE-MGMT-10` found no
page that the catalog does not record and that is newer than its record. The other PE Metaprompt hits are
archived predecessors dated 2026-09-12 and 2026-09-13 and pages that mention it. The other GCFPE-MGMT-10
hits are the archived `091326.1` and `091326.2` and control or tracking pages. Each recorded page was
fetched for its exact edit time. The PE Metaprompt's fetch and the register's were saved by the harness and
read by script (*Harness files*).

| Source | Recorded in the catalog | Found, by fetch | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1`, 2026-09-24T15:38 | 11:00:24.691Z; `091426.1` (`3db4590a05eb81d1bb64ebcb3ca8eb54`) at 15:38:34.295Z; the register selects it | None |
| PE Metaprompt | Pinned and selected: `091426.1`, 2026-09-23T17:17:22.217Z | 17:17:22.217Z; the register selects it (`3db4590a05eb8174be35d9e35acb3f77`) | None |

The register page was at 2026-09-23T17:43:39.489Z, the edit time the catalog records.

**(b) The watched paths.** `git log 1dec848..b1bd769` over *The watched sources* lists nothing. The range
holds two commits, amthorn78/glow-hdengine-v2#577 and amthorn78/glow-hdengine-v2#578. They change four
files, all under `docs/ephemeral/`, as PE39's request says.

No trigger finding. X4 re-pins nothing and moves the checked-through commit to the commit it examines.

### The members, read live

Each member was fetched whole into this session's context after the compaction and read whole. Each edit
time equals the readback time C2 recorded at X1.3, so no member has changed since its selection.

| Member | Version, page | Edited | Parent |
|---|---|---|---|
| TW-TRIAGE-10 — Identify PF10 Drain Targets | 100626.1, `3f14590a05eb81789e16d978795db77d` | 2026-10-06T03:18:14.556Z | *HDE TW* |
| TW-DRAIN-10 — Prepare PF Document Redlines | 100626.1, `3f14590a05eb81319ed0ebb00e14eedf` | 2026-10-06T03:19:43.487Z | *HDE TW* |
| TW-DRAIN-20 — Prepare PF09 Redlines | 100626.1, `3f14590a05eb81fa8c9bd34c9909c48d` | 2026-10-06T03:21:38.944Z | *HDE TW* |
| TW-RECORD-10 — Create Epic History Section | 100626.1, `3f14590a05eb8103babefccf8a92d748` | 2026-10-06T03:22:55.389Z | *HDE TW* |
| TW-RECORD-20 — Create CRD History Section | 100626.1, `3f14590a05eb81bc9127e36a85df1040` | 2026-10-06T03:23:58.670Z | *HDE TW* |
| TW-APPLY-10 — Apply Validated Redlines | 100626.1, `3f14590a05eb8156acaef4053b356625` | 2026-10-06T03:24:55.124Z | *HDE TW* |

### The C1 approval's check for a PF10 sentence (E-039)

- **What the C1 approval said.** Nathan's `analyze_approved_by` of MODIFICATION-20261005-gtwpe-writing-side
  (2026-10-05): "he will add one sentence to PF10 exempting the Last Update Gate from addendum 2.30 before C3
  starts; C3's ANALYZE confirms that sentence is on main."
- **What changed.** On 2026-10-06 Nathan ruled that the gate needs no PF10 change: it records the source an
  update used, and it is not a citation of HDE Build Notes (request, item 2). So that check no longer
  applies, and this analysis does not make it. The ruling is recorded in the architecture record's update
  "no PF10 sentence for the Last Update Gate", in amthorn78/glow-hdengine-v2#579. That pull request is open,
  and on `main` the update of 2026-10-06 still says C3 needs the sentence first.
- **Canon agrees.** HDE Build Notes 2.30 PF10-CITE-001's drain-target table names HDE Governance §0.2 and
  sections of the Build Checklist and the Mechanics Guide, but no document's front matter, though seventeen
  PF headers carry a gate of `BN` or `PF10` and a version, and three more a filename naming a PF10 version.
  Technical Writing Best Practices §15.1 treats the gate as a document-control value.
- **E-039.** This closes ledger row E-039, which #579 adds. The ledger is not this record's to edit, so
  closing the row is PE39's.

### The change, settled

The request's eight points, by item. C1's approved §A (A.1, A.4 to A.8) and the architecture record frame
them. `PLAN` writes the exact texts.

**ITEM-01. Document control (R4).**
- **TW-APPLY-10** derives every document-control field the revision changes, as architecture §5 lists them,
  where today its header contract covers three: the version, bumped once as today; the effective date and
  any other date the document's control fields carry; the Last Update Gate (ITEM-02); the change or revision
  history the document's own rules require, which arrives as a content redline and is applied like any
  other; internal references whose version-sensitive information must change, where today it synchronizes
  only a title's embedded version; and a check that all of them agree, a disagreement being a blocker.
- **The invocation tag stays.** Every PF header carries the same `INV-f2ac55d77ce9aacc`, so it does not
  depend on the revision.
- **The drains** draft, as a content redline, the change-history entry the target's own rules require. Canon
  examples: HDE Governance §9.3 requires a Doc-Delta entry in §9.3.1 for every normative change; HDE
  CLI-API-Vendor Ref §11.1 and HDE Schemas and Artifacts §9 hold change logs; an HDE CRD Records entry keeps
  its own material-change history (§4.2). They also supply, as today, the baseline's control-field schema.
- **Authority.** Technical Writing Best Practices §7 and §15.1 forbid changing a document-control value
  "unless the Product Owner or a governing source explicitly authorizes" it. Nathan's architecture §5 is
  that authorization, and TW-APPLY-10's header contract already carries it for three fields.

**ITEM-02. The Last Update Gate.**
- **The rule**, in TW-APPLY-10 and the drains, replacing "the exact deduplicated filenames of upstream
  sources": the gate names the source that justified the update, in Nathan's form (answer 6). That is `BN`
  and the version number of the PF file used when the source is a PF document, and `BN` and the source
  filename when it is not.
- **Several sources.** The present rule's handling stays: each source, deduplicated, in source order, now
  each in Nathan's form. Supporting reading is not a source of the update. A source whose identity cannot
  be resolved still blocks the metadata step.
- **The handoff.** The drains supply each source's identity (the PF file and its version, or the filename)
  in the package, and TW-APPLY-10 derives the gate from it.

**ITEM-03. No Draft (R5).**
- **TW-APPLY-10:** the revised PF carries no `Draft` or similar status language, no placeholder, TODO,
  unresolved drafting note, editorial comment or instruction to a future writer, and no stale status. A
  stale status field takes the value the document's own rules require (architecture §4: "Do not preserve an
  old document status merely because the source copy contained stale status information"); a value it
  cannot establish is a blocker.
- **The one exception** is what canon requires: a new PF30 volume's review copy carries Document status
  `Draft` and Volume status `Pending activation` (HDE CRD Records §6). Only TW-RECORD-20 writes one.
- **The drains** account for any such marker in their target as a hygiene redline. Nathan's architecture §4
  is the authorization TW-DRAIN-10's *General PF preparation* requires for hygiene.
- **TW-RECORD-10 and TW-RECORD-20** meet the same rule in their file (ITEM-05). TW-TRIAGE-10 writes no
  document.

**ITEM-04. PF09 row status (R6).** TW-DRAIN-20 judges every potentially affected row on all the evidence:
update it, leave it open, close it, or otherwise change it. It never leaves a row open because no
instruction says to close it, and never closes one only because related work shipped. The resulting PF09
shows the project's current state, not an accumulation of earlier row states. What stays: Done needs the
phase owner's completion and acceptance evidence, and unrelated rows are not touched. HDE Build Checklist —
Distillation agrees: "An existing PF09 status does not override contradictory current repository reality"
(§0.3), and Done requires every condition of §0.6.

**ITEM-05. PF20 and PF30 (R2, R3, R7, R8).**
- **Output.** Each record prompt writes the updated PF20 or PF30 Markdown file at the repository path the
  invocation names: the current canon file from `docs/pfcanon/` on `main`, with its one section inserted at
  the place the target's order requires, by an exact insertion. Every other byte is preserved and checked,
  as TW-APPLY-10 checks preservation. A report goes with it (ITEM-06). There is still no TW-APPLY-10 step
  (Nathan, 2026-09-29: PF20 and PF30 "don't need a redliner").
- **Control fields**, as ITEM-01 to ITEM-03.
- **Reconciliation (R7).** Each reads the original specification and every applicable PF10 change that
  modifies, clarifies, supersedes or extends it, never either alone (architecture §9). Today each reads only
  PF10's lifecycle controls.
- **PF30 as a volume family (R8), TW-RECORD-20.** It works in the volume the record belongs in: for a new
  CRD, the one volume whose Document status is `Canon` and Volume status `Active` (HDE CRD Records §6). It
  reports when that volume looks due for rollover, which is Nathan's determination. It opens a new volume
  only when the invocation carries his rollover decision, as §6 sets it: the next PF30.x; its review copy at
  Document status `Draft` and Volume status `Pending activation`; the reciprocal *Previous volume* and *Next
  volume* fields; and the prior volume's Volume status `Closed to new CRDs`. That writes two files, each
  with its own proof log. "Do not assume a second volume exists or open a new one" and "produce a full PF30
  artifact" go.
- **PF20 as one document (answer 8), TW-RECORD-10.** It keeps PF20's single structure and invents no volume.
- **Unchanged:** historical eligibility, approval evidence, nonduplication and identity rules, and "An
  existing record is not permission to create a duplicate or silently revise it through this creation
  role": an update to an existing record still goes through a drain.
- **E-010 stays as §A A.6 carries it.** HDE Governance §9.1.1 permits a PF20 or PF30 entry only as "a
  separately authorized historical drainage action". The invocation is that authorization, and the file is a
  copy in the pull request, never canon.

**ITEM-06. GTWPE-D1.** Each updated PF20 or PF30 file gets its own proof log beside it, named after it (the
file's name with `.proof-log` before `.md`), with all eight minimum items in Nathan's words and the link to
its file. As C2 did for the drains and the apply, the report is that proof log, so one file holds both
(`DERIV-001`). *GTWPE-D1, prompt by prompt* gives each prompt.

**ITEM-07. K-12.** TW-RECORD-20 takes its inputs as attached files or repository paths, never from Google
Drive or ChatGPT Library, in one sentence of its *Purpose*, as TW-RECORD-10's already says. It is an
absence, found by reading: TW-RECORD-20's *Purpose* names no input route.

**ITEM-08. A new TW-ALPHA release.** The five changed members, each at «V», with TW-TRIAGE-10 carried at
100626.1, by the three selection writes and the three current-release notes. C3 alters how the TW flow runs
(*How the TW flow changes*), so the new section carries a new *Current operation*. «V» follows the PE
Metaprompt's rule at execution: `100626.2` if `EXECUTE` runs on 2026-10-06, otherwise that date's `.1`; the
release label is `TW-ALPHA-<yyyymmdd>.N` on the same date.

### Per part: closure, tier, class and targets

One part, PART-01: the five new versions and the new release, which land together. The gate rule changes
both sides of the drain-to-apply handoff, and every rule here reaches several members, so splitting by rule
would split one member's new version across parts.

- **Targets.**
  - `prompt`: five new versions, of TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20 and TW-APPLY-10,
    each a new versioned sibling under *HDE TW*.
  - `notion_control`: the selection page's three writes; the current-release note on *Alpha 1*, *HDE TW* and
    the Operations Hub; and the catalog's checked-through commit at X4.
- **Closure**, from the relationships in the selected release's *Current operation*:
  - upstream, the producers of the handoffs the changed members consume (the drains' `READY` package and
    TW-APPLY-10's diagnostic): TW-APPLY-10, TW-DRAIN-10 and TW-DRAIN-20;
  - downstream, their consumers: the same three;
  - state sharers: TW-DRAIN-10 and TW-DRAIN-20, which share `READY`, `NO_CHANGE` and `BLOCKED`, and all
    five, which share `PARTIAL_PACKAGE` in their common save-recovery rules. C2 listed only the drains.

  TW-TRIAGE-10 and the record prompts have no recorded relationship with another member. Every member in
  the closure changes here.
- **Tier 2.**
  - The part changes a handoff: what a `READY` package carries for the gate (each source's identity) and for
    the change history (a content redline), and TW-APPLY-10's check of it. Both sides change here.
  - It changes a recorded relationship: the *Current operation* says the record prompts "still end with
    paste-ready sections only".
  - TW has no executable selftest, and no live trial has run since 2026-09-08. The gate is a static check of
    both sides of the handoff, with the whole-page readbacks, as C2's was.
- **Class B, rule application.** The part carries rulings already made into the prompts: Nathan's target
  architecture §§4, 5, 8 and 9 and his answers 6 and 8; his ruling of 2026-10-06 on the gate; GTWPE-D1; and
  his approved order (C1 §A A.5).
- **Authoring.** Through the selected PE Metaprompt's general rules, with GTWPE-MGMT-10's workarounds: only
  the approved edits and the two identity lines change, references stay versionless, and no model or effort
  text is added. Where a rule is already worded in a member, the new text converges on that wording
  (`ecosystem-change-management.md` §2, step 3): TW-RECORD-10's input sentence for ITEM-07, and the drains'
  and TW-APPLY-10's GTWPE-D1 passages for ITEM-06.

### Member dispositions (HDE Governance §9.1.6)

| Member or interface | Disposition | Reason |
|---|---|---|
| TW-DRAIN-10, TW-DRAIN-20, TW-APPLY-10 | Affected: a new version each | ITEM-01 to ITEM-03; and ITEM-04 for TW-DRAIN-20 |
| TW-RECORD-10, TW-RECORD-20 | Affected: a new version each | ITEM-01 to ITEM-03, ITEM-05 and ITEM-06; and ITEM-07 for TW-RECORD-20 |
| TW-TRIAGE-10 | Unaffected; carried into the new release at 100626.1 | It writes no document and sets no document-control field |
| TW-MGMT-10, TW-ASSESS-10 | Unaffected | Neither is selected |
| GTWPE-MGMT-10 100526.2 | Unaffected | Its route already repairs TW-ALPHA members and makes the selection writes, and its GTWPE-D1 guard applies to the five new versions. Its route text is worded for eight members (F-1). Its "until G5" stays for C6 (E-033) |
| The GTWPE catalog | Unaffected, but for X4's checked-through commit | The TW prompts join it at C6 |
| `tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Affected | Q-1 |
| `glow-write-boundary`, `glow-artifact-storage` | Unaffected | The record prompts' outputs stay under `docs/ephemeral/`, a path a session may write |
| The PE Metaprompt 091426.1; the GTWPE decision record | Unaffected | The authoring control, and the ruling applied |
| The GCFPE register and Flow Index | Unaffected | They list no TW member |

### GTWPE-D1, prompt by prompt

| Prompt | Writes before C3 | Writes after C3 | How the part leaves GTWPE-D1 whole |
|---|---|---|---|
| TW-DRAIN-10 | A redlines file, for `READY` and for `BLOCKED` work kept | The same | Unchanged: its processing report is the separate proof log beside the redlines file, named after it, with all eight items and the link. C3 does not edit that passage, and the readback checks it by phrase |
| TW-DRAIN-20 | As TW-DRAIN-10, for a PF09 phase file | The same | As TW-DRAIN-10 |
| TW-APPLY-10 | The final updated PF | The same | Unchanged: its application report is the separate proof log, stating the basis of each applied operation. C3 edits its header contract, not that passage |
| TW-RECORD-10 | A paste-ready section file, neither artifact type | The final updated PF20 file | Added: the report, a separate proof log beside the file, named after it, with all eight items in Nathan's words and the link (ITEM-06) |
| TW-RECORD-20 | As TW-RECORD-10 | The final updated PF30 file; on a rollover, the new volume and the prior volume's revised file | Added, as TW-RECORD-10: one proof log for each file it writes |
| TW-TRIAGE-10 | A list in its response | The same | Not bound |

No combined proof log is defined: no prompt writes both artifact types.

### Scope, and how it was measured (`SCOPE-001`)

**Method: broad match minus permitted exceptions, by reading.**
- Each body came back inline and whole, with no truncation flag, and was read in context.
- Each count below was made by reading one fetch, then checked by a second, independent reading of a
  second fetch at A6 (the request's standing direction; ledger E-035). The second reading corrected two
  counts (*Dry run (A6)*, D5). No command counted over a body.
- Matches are case-insensitive, at the start of a word: `version` not inside "conversion"; `date`, `gate`,
  `history` and `done` as words, so not "update", "validate", "gateway" or "historical".
- The broad terms, by rule, over the members each rule reaches:
  - ITEM-01 and ITEM-02: `version`, `date`, `history`, `header`, `gate`;
  - ITEM-03: `draft`, `status`, `placeholder`;
  - ITEM-04, TW-DRAIN-20 only: `clos`, `open`, `done`;
  - ITEM-05 and ITEM-06, the record prompts: `section`, `paste`, `insert`, `volume`, `PF10`, `report`,
    `proof`;
  - ITEM-07, TW-RECORD-20 only: `attach`, `reference`, `Drive`, `Library`.

**What is in scope.** A passage is a contiguous stretch of in-scope text. Each passage:
- sets or limits a document-control field, its authority, its check or its source provenance (ITEM-01,
  ITEM-02);
- governs status language, markers or hygiene in a produced document (ITEM-03);
- governs a PF09 row's status on the evidence (ITEM-04);
- defines a record prompt's output, its relationships, its volume handling or its reading of PF10 (ITEM-05,
  ITEM-06);
- or names TW-RECORD-20's input route (ITEM-07).

**The permitted exceptions, kept unchanged:**
- the identity lines, which the route changes as identity, not as rule text;
- a version that identifies a prompt, source, target, specification or output: in the preflight, output
  identity, intake, proof-log contents and handoffs;
- "gate" as a check: the page-count gate, a development or approval gate, launch gates, a violated gate, and
  TW-RECORD-20's ban on inferring a CRD number from "a Last Update Gate", which stays true;
- `status` in schema questions, in PF10's source-defined statuses, in save and validation status, in the
  record prompts' rules for the record's own content, and in TW-DRAIN-20's six dimensions and report
  classifications, which ITEM-04 leaves as they are;
- "history" as a source's material category in the drains' ledger, and the record prompts' historical
  content and titles;
- `placeholder` in the rules that keep placeholders out of a redline payload and a handoff, which agree with
  ITEM-03;
- TW-APPLY-10's version bullet, its header-location and conflict rules, its header before/after record, and
  the no-change report's "version bump", which already meet R4;
- in the record prompts: `report` in the shared save-recovery rules and the preflight; `insert` in the ban on
  inserting into an authoritative PF, which still holds because the file is a copy; `volume` naming the
  assigned target or its parts and in the duplicate check; `PF10` in the authority rule; and the generic
  locators (an attachment, a retrieval reference, evidence references), the Drive copy as no substitute, and
  the ban on writing to Drive or Library.

**Each member's broad hits, by term**, ITEM-01 to ITEM-04:

| Member | `version` | `date` | `history` | `header` | `gate` | `draft` | `status` | `placeholder` | `clos` | `open` | `done` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TW-TRIAGE-10 | 9 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | — | — | — |
| TW-DRAIN-10 | 24 | 2 | 1 | 6 | 3 | 0 | 5 | 2 | — | — | — |
| TW-DRAIN-20 | 25 | 3 | 1 | 6 | 3 | 0 | 19 | 2 | 7 | 3 | 3 |
| TW-RECORD-10 | 12 | 2 | 5 | 0 | 3 | 1 | 5 | 0 | — | — | — |
| TW-RECORD-20 | 13 | 1 | 3 | 0 | 4 | 1 | 9 | 0 | — | — | — |
| TW-APPLY-10 | 24 | 11 | 0 | 9 | 6 | 0 | 3 | 0 | — | — | — |

ITEM-05 to ITEM-07, in the record prompts:

| Member | `section` | `paste` | `insert` | `volume` | `PF10` | `report` | `proof` | `attach` | `reference` | `Drive` | `Library` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TW-RECORD-10 | 13 | 3 | 8 | 12 | 3 | 8 | 0 | — | — | — | — |
| TW-RECORD-20 | 13 | 4 | 8 | 13 | 3 | 8 | 0 | 1 | 5 | 2 | 1 |

**Each member's passages:**

| Member | Hits | In passages | Kept as exceptions | Passages in scope |
|---|---|---|---|---|
| TW-TRIAGE-10 | 11 | 0 | 11 | 0 |
| TW-DRAIN-10 | 43 | 12 | 31 | 4 |
| TW-DRAIN-20 | 72 | 21 | 51 | 5 |
| TW-RECORD-10 | 75 | 31 | 44 | 7 |
| TW-RECORD-20 | 89 | 36 | 53 | 8 |
| TW-APPLY-10 | 53 | 20 | 33 | 7 |

**The passages, by member and section.**
- **TW-APPLY-10 (7)**, all in *Deterministic final document-control header* but the last:
  - the opening two sentences: the standing authority for three fields, and what it does not authorize,
    "status or invocation-tag changes" among it (ITEM-01, ITEM-03);
  - the date bullet (ITEM-01);
  - the gate bullet (ITEM-02);
  - the sentence on a title's embedded version (ITEM-01, version-sensitive references);
  - "Report old/new values, source-file provenance and actual execution date" (ITEM-01, ITEM-02);
  - "Other header/title/status/invocation-tag changes need separately explicit authorization" (ITEM-01,
    ITEM-03);
  - in *Exact application and preservation*, the verification of the metadata plan (ITEM-01 to ITEM-03).
- **TW-DRAIN-10 (4).**
  - *Exact redline contract*: the paragraph on Apply's standing authority and the source filenames
    preparation supplies (ITEM-01, ITEM-02); the paragraph reserving "those three document-control fields"
    (ITEM-01, ITEM-03).
  - *General PF preparation*: "Any hygiene or deletion still needs exact selected-source or Nathan
    authorization" (ITEM-03), found by reading, with no broad hit.
  - *Completion, outputs and handoff*: the `READY` handoff's "source-file header provenance" (ITEM-02).
- **TW-DRAIN-20 (5).** TW-DRAIN-10's four, word for word, and in *PF09 coverage and native semantics* the
  paragraph on status meanings, Done and closing or reopening rows (ITEM-04).
- **TW-RECORD-10 (7).**
  - *Coded identity*: the relationship paragraph, "This role terminates with its paste-ready section" and no
    TW-APPLY-10 handoff (ITEM-05).
  - *Purpose*: its first sentence, "one complete historical Epic record section for the actual assigned
    PF20 document or existing volume" (ITEM-05).
  - *Destination*: the volume sentences (ITEM-05, PF20 as one document); the PF06, PF10 and PF27 reading
    sentences (ITEM-05, R7); the ban on choosing "final PF insertion/section numbering" (ITEM-05, placement).
  - *Section-only output and completion*: the whole section, its heading and four paragraphs (ITEM-01 to
    ITEM-03, ITEM-05, ITEM-06).
  - *PF20 schema*: "with current PF10 lifecycle overrides" (ITEM-05, R7).
- **TW-RECORD-20 (8).** TW-RECORD-10's seven, but in its *Purpose* the sentence on its inputs is in scope
  too (ITEM-07), and its *PF30 schema* holds two passages in place of PF20's one: the sentence on the volume
  family and PF10 overrides (ITEM-05, R7 and R8), and "produce a full PF30 artifact" (ITEM-05).

**Total: 31 passages in five members**, with each new version's two identity lines on top: 10.

**The rule-change search (`D26-E`).** The old texts are the gate as "filenames of upstream sources", the
record prompts' "paste-ready section" output, "Do not ... open a new one" and "a full PF30 artifact".
- In the members: only in the passages above.
- In GTWPE-MGMT-10 100526.2, by reading its fetch at the mode's start: none.
- In `docs/prompt_ecosystem_management/gtwpe/` at `b1bd769`, by `git grep`: `Last Update Gate` 0,
  `source filename` 0, `paste-ready` 0, `Section-only` 0, `full PF` 0, `rollover` 0; "proof log" 11, all in
  GTWPE-D1.
- On the control pages: the selection page's current *Current operation* says the record prompts "still end
  with paste-ready sections only" and that the Apply metadata and PF20/PF30 rules of TW-ALPHA-20260908.1
  "still apply"; that operation's own text sets the gate to "the deduplicated exact upstream source
  filenames". *Alpha 1*'s current rows call the record prompts "paste-ready section only". The route makes
  each of these historical, as a dated record, rather than rewriting it.

`PLAN` turns this into absence checks by phrase on the new pages.

### Pages that name TW's current release (A3)

**Method.** Searches with highlights off on `TW-ALPHA-20261006.1`, on `100626.1` and on a member title.
Each page found that could name the current release was fetched; a page last edited before 2026-10-06 cannot.
*Alpha 1* and the Operations Hub were saved by the harness and read by script.

| Page | Edited | Names TW's current release | Written by the route |
|---|---|---|---|
| *Glow Technical Writing Ecosystem*, the selection page, `3d44590a05eb8171ab6ff4dab33b00ef` | 2026-10-06T03:30:15.790Z | Yes: its status line and `## Selected release — TW-ALPHA-20261006.1`, with the page's one *Current operation* | Yes: the three selection writes |
| *Alpha 1 — Implementation and Validation*, `3d44590a05eb81fe991ff0114cb43029` | 2026-10-06T03:30:55.483Z | Yes: `## Selected release — TW-ALPHA-20261006.1`, with its six rows | Yes: the current-release note |
| *HDE TW*, `3c74590a05eb8176baf8cb59f1631f3c` | 2026-10-06T03:31:27.379Z | Yes: `## Current TW release — TW-ALPHA-20261006.1` | Yes: the current-release note |
| *Glow Operations Hub*, `3ce4590a05eb814f8892f88ff8539308` | 2026-10-06T03:31:55.832Z | Yes: `## Current Glow TW release — TW-ALPHA-20261006.1` | Yes: the current-release note |
| The GTWPE parent page and catalog, `3ea4590a05eb818c915bdfd3d150c44b` | 2026-10-06T03:29:32.421Z | No: it names TW-ALPHA, but no release | No: X4 writes only the checked-through commit |
| The two archived `100626.1` pages in *04 Archived Prompt Versions* | 2026-10-06 | No: unselected copies, named by version | No |
| Older pages, such as the architecture page, earlier member versions and GTWPE-MGMT-10's pages | Before 2026-10-06 | No | No |

**Coverage.** This is the set the record of TW's latest selection, C2's, wrote (X4.3 to X4.6). Each member's
own text names the selection page as holding its selection.

### How the TW flow changes (A3)

C3 alters how the TW flow runs, as the selection page's *Current operation* describes it:
- TW-RECORD-10 and TW-RECORD-20 end with an updated PF20 or PF30 file and its proof log at a repository
  path, not with a paste-ready section, and still with no Apply step;
- TW-APPLY-10 brings every document-control field forward, the gate in Nathan's form, and writes no Draft;
- the drains supply each source's identity and draft the change-history entry;
- TW-DRAIN-20 judges row status on all the evidence.

So the new release's section carries a new *Current operation*, and the present one becomes historical. It
also replaces the present one's statement that the Apply metadata and PF20/PF30 rules of TW-ALPHA-20260908.1
still apply.

### Contradictions and risks

1. **The TW Flowmaster skill (Q-1).** `tw-flowmaster` 1.3.0 and `flowmaster-validate` 3.3.2 do not run
   TW-ALPHA-20261006.1, and Nathan waived HDE Governance §9.1.6's interacting-skill readiness for that release
   only ("An edited subgroup is not ready while an affected counterpart remains incompatible"). C3's release
   keeps the gap. A Flowmaster run would hand the prompts no repository path, and each would stop at its
   missing-input rule, which `PLAN` keeps: a loud stop, not a wrong result.
2. **The Last Update Gate and HDE Phased Epics.** PF20's §0 says that when PF10 is referenced inside PF20,
   "avoid BN version strings". Nathan's ruling of 2026-10-06 settles it: the gate records the source an update
   used, and it is not a citation of HDE Build Notes. `PLAN` words the rule so that a TW-RECORD-10 run does not
   stop on that passage. Canon is not changed.
3. **The gate for a PF source other than PF10.** Nathan's form, `BN` and that PF's version, names the version
   but not the document. It is applied as Nathan worded it, and the proof log names the file. The TW flow's
   change sources are PF10, a specification or another non-PF source, so the case is rare.
4. **Document-control authority.** Technical Writing Best Practices §15.1 says "Do not invent, infer,
   normalize, or increment a document-control value", and §7 allows a change only on the Product Owner's or a
   governing source's explicit authorization. Nathan's architecture §§4 and 5 give it, as TW-APPLY-10's
   header contract already says for three fields. Not a conflict.
5. **E-010.** HDE Governance §9.1.1 against the Change Process Guide and Plan Templates on PF20 and PF30
   records stays Nathan's. The record prompts follow §9.1.1: one section, only when the invocation names it,
   only into a copy in the pull request.
6. **A PF30 rollover writes two files.** The new volume is a new document, written as HDE CRD Records §6
   sets it; the prior volume's revised file changes only its Volume status and *Next volume* fields. Each has
   its own proof log. Rollover is rare and always Nathan's decision.
7. **Placement of the inserted section.** PF30 orders records by CRD ID (§3.2). PF20 keeps its records last,
   under §2, numbered 2.2 to 2.25, and two of them, 2.23 and 2.24, carry the same HDE-EPIC038 record. The
   record prompts' existing rule decides placement: the target's established convention "only where uniquely
   supported", otherwise an exact input blocker; and "leave unrelated history intact".
8. **PF20's size.** PF20 is 952,515 bytes, about 317,000 tokens at ledger E-013's 3.0 bytes a token. The
   record prompts already require reading the whole target; C3 does not change that. A session that cannot
   hold it stops, and C4's capacity stop (S1) is the general answer.
9. **No executable check exists for TW.** The tier 2 gate is static, and no live TW trial has run since
   2026-09-08. C3's first live run is untried.
10. **One reader of the bodies.** The scope rests on this session's reading; workers do not fetch bodies
    (`D22`). The A6 dry run and `PLAN`'s dry run each read them again.
11. **The phrase check sees phrases, not meaning** (`D14`'s note). Carrying the rules close to Nathan's words
    lets the readback find each by phrase; the reviews read for behaviour.

### Defect classes matched (`ecosystem-change-management.md` §4)

- `SCOPE-001`: the scope above is measured by broad match minus exceptions, by reading, twice.
- `GUARD-001`: GTWPE-D1 lands in the two record prompts, with its guard: GTWPE-MGMT-10's prompt route checks it
  by phrase on each new page.
- `DERIV-001`: the document-control fields are derived from the actual change, not copied forward; the
  record prompts' report and proof log become one file; the four release pages restate the selection by hand.
- `FUNC-001`: `tw-flowmaster` would run TW the old way (Q-1).
- `NAME-001`: the record prompts become bound by GTWPE-D1 because of what they write, not their names.

### Findings against GTWPE-MGMT-10 100526.2

- **F-1:** its selection route is worded for eight members: write (1) "lists the eight members with only the
  changed rows new". The new release has six, five of them new. `PLAN` adapts the text, as C2 and the
  model-advice change did.

### Candidates for separate Modifications (recorded, not taken)

- **F-1**, in a later GTWPE-MGMT-10 repair, with E-033 for C6.
- **PF20 volumes**, if Nathan formally splits PF20 (answer 8). TW-RECORD-10 then needs a volume rule like
  TW-RECORD-20's.

### Open questions for the Product Owner

**Q-1. The TW Flowmaster skill, for this release (risk 1).**
- **(a) Waive HDE Governance §9.1.6's interacting-skill readiness for `tw-flowmaster` again, for this
  release.** The grounds are C2's: C4 replaces the skill, C6 retires it, and a Flowmaster run stops loudly
  rather than producing a wrong result. The selection page and the three notes say that `tw-flowmaster` 1.3.0
  and `flowmaster-validate` 3.3.2 do not run it, and the override block records the waiver.
- **(b) Update the skill first,** through the skill route: a skill part, a skill review cycle and an install,
  for a skill C6 retires.
- **Recommendation: (a).**

### Readiness and interaction cost

`NEEDS_RULING`, for Q-1. It is advice, not a refusal. No item waits on another item's execution, and every
item's scope is measured.

    interaction_cost = 1 open ruling + 2 + 3 review rounds + 0 skill review cycles + 0 installs + 1 merge = 7

- **Review rounds:** this mode's dry run; `PLAN`'s dry run; and one full review by a single reviewer. A second
  reviewer or a diff check comes only if that review finds a required defect, by the request's standing
  direction.
- **Q-1's option (b)** would add a skill review cycle and an install, making 9.
- **The merge** is the record's pull request, amthorn78/glow-hdengine-v2#580. It is not to be merged before the
  record is `COMPLETE`. No repository file other than the record and its evidence changes, so X2 waits for no
  merge.
- **Splitting saves nothing.** The five versions and the release land as one selection, and the gate rule
  spans both sides of a handoff.

The estimate is in the front matter. Time is the meter, and twice the estimate is where the session stops.

### Dry run (A6)

Every normal-path gate and readback of this mode, read-only, by this session. No full review ran.

| # | Gate or readback | Result |
|---|---|---|
| D1 | Both record checks on a scratch copy at `ANALYZED`: `modification_validate.py` and `gtwpe_record_check.py` | Both exit 0 |
| D2 | The front matter parses (PyYAML), its `request` equals PE39's message, and every table in the record has one column count in every row, by script | Parses; the request is verbatim; every table consistent |
| D3 | A0 reproduced: `git fetch origin main`; `origin/main`; `git log 1dec848..origin/main` over *The watched sources* | Still `b1bd769`; no commit |
| D4 | The new titles and the new release label are free | *HDE TW* (edited 2026-10-06T03:31:27.379Z) lists no member version after 100626.1, and the selection page (edited 03:30:15.790Z) names no release after TW-ALPHA-20261006.1 |
| D5 | The scope counts, by a second, independent reading of a second fetch of each of the six bodies, each at the edit time in *The members, read live* | Two counts corrected: `version` in TW-DRAIN-10, 23 to 24, and in TW-DRAIN-20, 24 to 25, both "versionless role name" in the handoff, a kept exception. Every other count, and every passage, confirmed |
| D6 | The record tools need no change for this Modification | By reading at `b1bd769`: `TARGETS` holds `prompt` and `notion_control`, and the record check needs only the subsections this record has |

No required defect.

### Harness files (`D22` condition 5)

- **Inline fetches, held only in this session's transcript**, which the harness keeps and leaves to its
  teardown:
  - GTWPE-MGMT-10 100526.2, once, after the compaction;
  - the six TW bodies at 100626.1, twice each: the scope's first reading and A6's second;
  - GCFPE-MGMT-10's proposed body and `091426.1`, fetched at A0 for their edit times;
  - the control pages: the GTWPE parent page, the selection page and *HDE TW*.
- **Harness saves, each read by a script that printed only what the check needed:**
  - the PE Metaprompt `091426.1` fetch, `mcp-Notion-notion-fetch-1791285895858.txt`: its title, edit time
    and path;
  - the register, `mcp-Notion-notion-fetch-1791285896481.txt`: its edit time and the two rows of *Current
    selection* that name GCFPE-MGMT-10 and the PE Metaprompt;
  - *Alpha 1*, `toolu_01Nr7BUZDpK3eaAjyoD9HJgW.json`, and the Operations Hub,
    `mcp-Notion-notion-fetch-1791286201813.txt`, both control pages: each one's edit time, headings, term
    counts and current TW release section.

  Earlier in this session the harness refused `rm` on its tool-results directory ("Session Transcript
  Tampering"), as `D22`'s refinement of 2026-09-23 foresees. So each save is left to its teardown and not read
  again. No save was hashed or compared as a body's identity.
- **The session transcript.** After the compaction, A1's verbatim copy of the request needed PE39's message,
  which only the transcript held. A script read it once and printed only the user's typed message that held
  "run C3", and its timestamp, never a tool result. The request was saved from it to `c3_request.txt` in the
  scratchpad.
- **Scratch files**, in this session's scratchpad: copies of canon from `main` (not prompt bodies); the
  scripts `user_request.py`, `save_meta.py` and `ctl_section.py`; the request; drafts of this section; and a
  scratch copy of this record for the dry run.

### Canon and rulings relied on

- **`AGENTS.md`:** the canon-first rule; canon is read-only; the CI-exempt paths; the pull request's headings.
- **Technical Writing Best Practices** §3, §7, §14 and §15.1.
- **HDE Governance** §9.1.1, §9.1.6, §9.2 and §9.3.
- **HDE Build Notes** 2.29 PF10-CANON-001, 2.30 PF10-CITE-001 and 2.38 PF10-AINEUTRAL-001.
- **HDE CRD Records** §0 to §3.3, §4.2, §6 and §7.
- **HDE Phased Epics:** its front matter and §0.
- **HDE Build Checklist — Distillation** §0.3 and §0.6.
- **HDE CLI-API-Vendor Ref** §11.1 and **HDE Schemas and Artifacts** §9, by their headings.
- **Rulings:** GTWPE-D1; `D21`, `D22` and `D26` (`gcfpe.decision-record.md`); Nathan's target architecture,
  §§4, 5, 8 and 9, his answers 6 and 8, and his directions of 2026-09-29; his ruling of 2026-10-06 on the
  gate; C1's approved §A (A.1, A.4 to A.8); and C2's override, for Q-1.

## §P — Plan

*Written by MODE = PLAN. Requires analyze_approved_by. Frozen once approved.*

This session runs the mode as a GTWPE-MGMT-10 session, following *GTWPE-MGMT-10 — Manage the GTWPE —
100526.2*, fetched live at the start of the mode, edited 2026-10-05T16:36:11.384Z, as at `ANALYZE`. The mode
started at 2026-10-06T12:30:32Z, when Nathan's approval of the analysis at `f8bbb6c` arrived; it is in the
front matter, verbatim. `main` is at `b1bd769`. The plan is being written; it follows below.
