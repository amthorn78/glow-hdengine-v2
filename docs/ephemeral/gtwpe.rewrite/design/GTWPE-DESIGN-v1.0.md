---
artifact_type: PE_ECOSYSTEM_DESIGN_PACKAGE
design_id: GTWPE-DESIGN
version: "1.0"
created_date: 2026-09-28
plan: GTWPE-IMPLEMENTATION-PLAN-v1.1.md (GTWPE-IMPL-PLAN v1.1), phase P1
author: W1, session_01UZ7d2wTQuWPE5Wk4ADwRET
facilitator: PE37, session_018teDumz2XyKdoXF9p3BKFM
canon_read_at: "main @ 8eb4ce0; docs/pfcanon/ and AGENTS.md are byte-identical at 53449c9"
result: AWAITING_APPROVAL
revised: 2026-09-28 — repair of the dry run's required findings DR-1 to DR-8 (design/DRY-RUN-P1.md)
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# GTWPE design package, v1.0

**The GTWPE turns an approved input into finished, merged PF documents in one managing session.**
It has four prompts, two repository tools and one shared procedure. Nathan approves each change
(G3) and merges each canon pull request (G4). This package fixes the membership, the contracts, the
resolutions of the open ledger items, the change plan and the test specification for plan phases
P2 to P5.

**Result: `AWAITING_APPROVAL` (G1).** Nothing in this package writes a page, a tool, a prompt, a
skill or a canon file (plan §6).

Approval sentinel: `ASK OK?`

## Contents

0. What G1 approves
1. Sources relied on
2. Membership
3. The ecosystem at a glance
4. Prompt contracts
5. A run, stage by stage
6. Producer and consumer contracts
7. Subagents: briefs, capture, post-check and cost
8. The change package and its validator
9. Resolutions: E-003, E-004, E-006, E-007, Q1 to Q3
10. Canon and rulings the plan predates
11. GTWPE-MGMT-10: scope, lineage and relation to the PE
12. Change plan
13. Test specification
14. Decisions for G1
15. Errors for the ledger
16. Open findings, listed as accepted risks
17. Reviews ledger
18. What this package does not claim

## 0. What G1 approves

G1 approves this version, pinned by its version number (plan §6), and only this version:

- the membership in §2, including the two dedicated record prompts Nathan ruled on 2026-09-28;
- the contracts in §4 to §8;
- the resolutions in §9;
- the change plan in §12 and the test specification in §13;
- each decision in §14, at the default or recommendation stated there, unless Nathan's approval says otherwise.

A later version needs its own approval. Approving G1 authorizes P2 to begin; it writes nothing.

## 1. Sources relied on

**PF canon, from `docs/pfcanon/` on `main`.** In this record PF10 is cited by addendum number and
title (PF03 §9; HDE Governance §0.2).

| Source | Read | Used for |
|---|---|---|
| PF03 — Technical Writing Best Practices | complete | §1 writing only; §3 complete reads, no ellipsis; §6 source precedence; §7 document control and finding accounting; §8 and §15.2 the redline format; §11 state language; §12 when to ask |
| PF06 — Change Process Guide | complete | §0.1A process ownership; §0.2 canon edits are separate documentation work, the PO squash-merges; §0.6.10 one-pass redline bundles; §1.0.3, §1.0.6, §1.1.2, §3.5.1, §6.3 PF30 and PF20 records; §1.1.11 `ASK OK?`; §3.5.2.8 post-QA drainage ordering |
| PF10 — HDE Build Notes | complete | §1 to §9 precedence, §7 drained guidance; 2.8 PF10-FORM-001; 2.14 Specification format authority; 2.29 PF10-CANON-001; 2.30 PF10-CITE-001; 2.31 PF10-HDR-001 |
| PF27 — Plan Templates | complete | *Review guardrails* (materiality, rendered escapes, redline bundles, review stability); §2 the Epic record and archive-on-close; §2A the CRD profile and compact PF30 contract |
| PF30.1 — HDE CRD Records | complete | §2 ownership; §3.1 CRD IDs; §3.2 record lifecycle; §3.3 vocabularies; §4 record contract; §6 volumes; §7 template |
| HDE Governance (PF04) | §0, §9.1 to §9.6, found by the canon-first search | §9.1.1 historical homes; §9.1.2 conflicts; §9.1.3 advice; §9.1.6 prompt ecosystems; §9.3.1 change log |
| HDE Phased Epics (PF20) | front matter, §0, Phase Exit Criteria, §1, and the §2 heading index, found by the canon-first search | its reference-ledger posture, drain posture and Build Notes posture; its record order |

**Repository, other.** `AGENTS.md` at sha256 `2a28ac5c15d348f8…` (changed after P0; §10). The plan
v1.1, `ERRORS.md`, `CHECKPOINT.md` (including §8's four rulings) and the three P0 input records. In
`docs/prompt_ecosystem_management/`: `README.md`, `gcfpe.decision-record.md` (D22, D24, D25-B, D26
and the `D23-G` successors), `session-working-rules.md`, `execution-and-delegation-model.md`,
`ecosystem-change-management.md`, `reviewer-prompt-template.md`, `modification-template.md`,
`prompt-body-content-policy.md`, `notion-write-boundary.md`, `skill-packaging-and-delivery.md`,
`authoritative-surfaces.md`, and `operating-procedures/carried-forward-operating-rules.md`.

**Notion, read-only under `D22`.** The eight selected TW bodies, the proposed GCFPE-MGMT-10 body
(`3e34590a05eb811b93d2da9b4ef8106d`) and, at P0, the PE Metaprompt 091426.1. Page IDs, edit times
and the rules kept are in `design/P1-SOURCE-NOTES.md`. No body is copied into this record.

### 1.1 The PF03, PF06 and PF10 check for new prompts

The PE Metaprompt requires a complete PF03, PF06 and PF10 check before a new Glow prompt is made.
All three were read in full (P1 source notes). The four GTWPE prompts must meet each rule below, and
this design meets it where stated.

| Rule | Source | Where the design meets it |
|---|---|---|
| Read every relied-on source completely; an unknown stays unknown | PF03 §3 | Drafters read the complete target (§7.3); `UNKNOWN` and `BLOCKED` are returns, never guesses |
| No ASCII three-period or Unicode ellipsis in a PF document | PF03 §3 | V8 |
| Source precedence: the operator, the complete target, the owning canon, then PF10 where an addendum speaks | PF03 §6 | The brief frame's settled rules (§7.2 item 4) |
| Document control changes only on explicit authority; every finding of an audit source is accounted for | PF03 §7, §15.1 | G3 approves each exact value (§8.4); B-DRAFT's change ledger accounts for every finding |
| The redline format and its placement rules | PF03 §8, §15.2 | §8.1; V1 to V7 |
| "applied", "committed" and "merged" only on direct evidence | PF03 §11 | The run report says "applied" after S6's diff check and "merged" only after S9 |
| Ask only when the answer changes the result | PF03 §12 | Subagents never ask; the manager asks at G3 or on a named blocker |
| A canon edit is separate documentation work; the PO squash-merges | PF06 §0.2 | A GTWPE run is separate canon maintenance, never part of an implementation PR; Nathan merges |
| One-pass redline bundles, original anchor space, no overlap | PF06 §0.6.10 | V4 to V7; a failing bundle returns to its drafter once |
| `ASK OK?` on approval-submitted artifacts | PF06 §1.1.11 | The G3 package and this design |
| Drainage only after the epic's QA is complete | PF06 §3.5.2.8 | §10.5; §14 D-3 |
| PF30 and PF20 records | PF06 §1.0.3, §1.0.6, §1.1.2, §3.5.1, §6.3 | The dedicated record prompts (§4.2, §4.3), within HDE Governance §9.1.1 (§10.3) |
| Precedence, the latest base version, addenda scoped individually | PF10 §1 to §9 | B-CLASSIFY-PF10 reads one logical base version through EOF; a later addendum governs only where scopes overlap |
| Agent-authored addendum form | PF10 2.8 | Not applicable: PF10 is never a GTWPE target |
| Specification format authority and terms | PF10 2.14 | PF27 through GTWPE-RUN-10, PF30 through GTWPE-RECORD-20; new text says "Specification" |
| Canon is `docs/pfcanon/` on `main`; a superseded version leaves it; agents write only under exact PO authority | PF10 2.29 | S6 replaces the versioned file; G3 is the exact authority |
| No PF10 locator in another PF | PF10 2.30 | V9 |
| No header model-advice review | PF10 2.31 | No model or effort content anywhere (`D7`, §9.4) |

## 2. Membership

### 2.1 Current members and their disposition

| Current | Disposition | What carries into the GTWPE, and where |
|---|---|---|
| TW-TRIAGE-10 090726.2 | Folded into S2 of GTWPE-RUN-10 | One logical PF10 base version, read through EOF; ownership established by reading the target; "a search hit or matching heading is not enough"; PF09 routed only to the actual phase file. Its "A title containing Canon is not an eligibility rule" is superseded by Nathan's ruling (§10.2) |
| TW-DRAIN-10 090826.1 | Subagent brief B-DRAFT inside GTWPE-RUN-10 | The change ledger (redline, already represented, out of ownership, blocking); exact redlines against the unchanged original; `READY`, `NO_CHANGE` (exactly `no redlines`), `BLOCKED`. Its `FIND_AND_REPLACE` is dropped: PF03 §8 has `INSERT`, `REPLACE` and `DELETE` only |
| TW-DRAIN-20 090826.1 | Subagent brief B-DRAFT-PF09 inside GTWPE-RUN-10 | The six dimensions: subtasks, tasks, phase statuses, new rows, evidence, Epic information. Board data is never a prerequisite |
| TW-APPLY-10 090826.1 | Replaced by `gtwpe_redline.py`, S6 and S7 | Whole-batch rejection; byte-exact application in descending offset order; untouched bytes verified; no metadata-only version bump. **Not carried:** its standing authority to derive version, date and Last Update Gate. G3 approves those values (PF03 §7, §15.1) |
| TW-ASSESS-10 090826.2 | Retired | Nothing. Nathan sets effort per turn and PE37 recommends it (plan §2.5); no GTWPE body carries model or effort content (`D7`, §9.4) |
| TW-RECORD-10 090726.2 | **GTWPE-RECORD-10**, the dedicated PF20 prompt | Completed Epics only; specification approval alone is insufficient; nonduplication; no identifiers allocated |
| TW-RECORD-20 090726.2 | **GTWPE-RECORD-20**, the dedicated PF30 prompt | The approved CRD Specification with its approval evidence; the PO allocates CRD IDs; nonduplication; exact PF30 vocabulary |
| TW-MGMT-10 090826.2 | Replaced by **GTWPE-MGMT-10** | Publication as a new versioned sibling, never overwrite, rename, move or delete; recheck and exact-title search before each create; readback; the catalog is updated only after the full set passes; both sides of every changed relationship |
| `tw-flowmaster` 1.2.0 (freeze digest `2 fd6c344b…`) | Retired through a `D24` skill package, installed by Nathan (P5) | Nothing. GTWPE-RUN-10's single session is the orchestrator |
| Glow Technical Writing Ecosystem page, selecting TW-ALPHA-20260908.1 | Kept intact; superseded banner at G5 | None of its pages is rewritten (plan §2.5) |
| The five unread neighbours, TW Strength Analyzer 090726.1, TW-Flowmaster-082626.8 and the predecessor versions under HDE TW | Not members of TW-ALPHA or of the GTWPE; untouched | *PF10 Condense — Work 090726.3* is PF10 work, which the GTWPE never does (§10.2) |
| UTIL-10, the GCFPE redline applier | Not a GTWPE member; unchanged | "other ecosystems do not become GCFPE members by proximity" (HDE Governance §9.1.6) |

### 2.2 Proposed membership

| Member | Kind | Home | Writes canon |
|---|---|---|---|
| **GTWPE-RUN-10 — Run the Glow Technical Writing Flow** | prompt | Notion, under the GTWPE parent page | the general targets (§8.7), through S4 to S9 |
| **GTWPE-RECORD-10 — Record an Epic in HDE Phased Epics** | prompt, dedicated | Notion | PF20 only, through S4 to S9 |
| **GTWPE-RECORD-20 — Record a CRD in HDE CRD Records** | prompt, dedicated | Notion | PF30.x only, through S4 to S9 |
| **GTWPE-MGMT-10 — Manage the GTWPE** | maintenance prompt | Notion | nothing in canon |
| `gtwpe_redline.py` and its selftest | tool | `docs/prompt_ecosystem_management/gtwpe/` | applies an approved package; never chooses one |
| `gtwpe_read.py` and `readers.lock` | tool | the same directory | nothing |
| `gtwpe-run-procedure.md` | shared procedure | the same directory | nothing |
| The GTWPE parent page and its catalog block | control | Notion, `AI Prompts / HDE TW` (ruling 3 of 2026-09-25) | nothing; it is GTWPE's selection authority from G5 |
| `glow-write-boundary`'s GTWPE exception | skill interface | the synced skills tree, through `D24` (P5) | permits the canon write in §8.7, nothing more |

**Why a shared procedure.** The three run prompts share S4 to S9. Written into three bodies, the
stages would drift apart, which is the failure the GCFPE-MGMT-10 redesign names ("One body means one
authority for the shared spine"). Each run prompt therefore cites `gtwpe-run-procedure.md` for S4 to
S9, the subagent brief frame and the post-check, and states only its own intake and drafting. Procedure lives in
`docs/prompt_ecosystem_management/` (kickoff workaround `D2`). The procedure carries no prompt body.

**Alternative, if Nathan meant briefs rather than prompts** (§14, D-1). The two record prompts could
instead be dedicated subagent briefs inside GTWPE-RUN-10, as TW-DRAIN-10 and TW-DRAIN-20 become.
This design reads "dedicated prompts" literally.

## 3. The ecosystem at a glance

```mermaid
flowchart LR
  N(["Nathan"]) -->|"invokes; approves G3; merges G4"| RUN["GTWPE-RUN-10<br/>general targets"]
  N -->|"invokes; approves G3; merges G4"| R10["GTWPE-RECORD-10<br/>PF20 only"]
  N -->|"invokes; approves G3; merges G4"| R20["GTWPE-RECORD-20<br/>PF30.x only"]
  N -->|"requests; approves each mode"| MG["GTWPE-MGMT-10<br/>maintenance"]
  RUN & R10 & R20 -->|"cite S4 to S9"| PROC["gtwpe-run-procedure.md"]
  RUN & R10 & R20 -->|"call"| TOOL["gtwpe_redline.py<br/>gtwpe_read.py"]
  RUN & R10 & R20 -->|"spawn; write nothing"| SUB["subagents<br/>classify, draft, verify"]
  RUN & R10 & R20 -->|"records branch"| REC[("docs/ephemeral/gtwpe.runs/run-id/")]
  RUN & R10 & R20 -->|"canon branch and PR"| PR[("canon PR<br/>target files only")]
  PR -->|"merge adopts"| CANON[("docs/pfcanon on main")]
  MG -->|"Modification record"| MOD[("docs/ephemeral/modifications/")]
  MG -->|"successor pages; catalog"| NP[("Notion GTWPE parent")]
  SK["glow-write-boundary<br/>GTWPE exception"] -.->|"permits"| PR
```

```mermaid
flowchart TD
  S0["S0 Intake: path, run ID, RUN.md"] -->|"inputs resolved"| S1["S1 Normalize: source records"]
  S0 -->|"input missing"| B1[["RUN_BLOCKED INPUT_MISSING"]]
  S1 -->|"reader unavailable"| B2[["RUN_BLOCKED UNSUPPORTED_INPUT"]]
  S1 --> S2["S2 Targets, or R2 destination for a record prompt"]
  S2 --> S3["S3 Draft: one subagent per target"]
  S3 -->|"READY"| S4["S4 Validate: gtwpe_redline.py validate"]
  S3 -->|"NO_CHANGE or BLOCKED"| PK["G3 package"]
  S4 -->|"exit 0"| PK
  S4 -->|"first rejection"| S3
  S4 -->|"second rejection"| B3[["REQUIRED error to Nathan"]]
  PK --> G3{{"S5 G3: Nathan approves files, edits, versions"}}
  G3 -->|"approved"| S6["S6 Apply on a local canon branch"]
  G3 -->|"declined"| C1[["CLOSED_NOT_APPROVED"]]
  S6 -->|"diff check fails"| B4[["stop: APPLY_DIFF_MISMATCH"]]
  S6 --> S7["S7 Verify: fresh subagent, isolated"]
  S7 -->|"difference"| B5[["stop: VERIFY_MISMATCH"]]
  S7 --> S8["S8 Publish: push canon branch, open PR"]
  S8 --> P1[["CANON_PR_OPEN, IN FLIGHT"]]
  P1 -.->|"Nathan merges; later RESUME"| S9["S9 Close: files on main equal S6 output"]
  S9 --> DONE[["RUN_COMPLETE"]]
```

## 4. Prompt contracts

Every GTWPE prompt shares these terms:

- **Identity.** The first two lines are `<PROMPT ID> — <title> — <MMDDYY.N>` and
  `Prompt Version: <MMDDYY.N>` (the PE Metaprompt's general rule; the TW ecosystem is outside `D23-G`,
  §14 D-5). There is no header of model, effort or workload advice (`D7`), and no selection state
  (`prompt-body-content-policy.md`).
- **Returns.** One result per return to Nathan, ending `DECISION NEEDED`, `NOTHING NEEDED` or
  `IN FLIGHT`. No prompt emits a `NEXT_PROMPT_HANDOFF` or hands off to another prompt (`D5`).
- **References.** External documents are cited by controlled directory, versionless name and section
  (HDE Governance §9.1.6; PF10 2.14). A body restates no rule it can cite.
- **Boundaries.** It never merges, installs, creates sessions, or writes to Notion, Drive or any
  repository path outside §5.2 and the approved canon files. `docs/pfcanon/PF10-*` is never written
  (Nathan, 2026-09-28).

### 4.1 GTWPE-RUN-10 — Run the Glow Technical Writing Flow

| Field | Contract |
|---|---|
| Purpose | Turn one Path A or Path B input (plan §2.1, §2.2) into approved, applied and merged changes to the general targets |
| Owner | Nathan invokes it and holds G3 and G4. The managing session runs it |
| Inputs | `START` with any of: **(a)** a document: a repository path, an upload, pasted text, a Notion page ID, or a Drive file Nathan names specifically (§9.4 `D10`); **(b)** a specification: the repository path of an approved Epic or CRD Specification under `docs/ephemeral/`; **(c)** `PF10`: the applicable PF10 file set (§9.5 Q2), whole or narrowed to named addenda. Optional: a slug, and a selection within (a). Or `RESUME <run-id>`. Or Nathan's G3 reply in the same session. §4.1.1 maps plan §2.2's rows to these inputs |
| Outputs | The run records (§5.2); the G3 package; one canon PR; the run report |
| Writes | The records branch and the run directory; the canon branch, holding only files Nathan approved at G3. After P5, `glow-write-boundary`'s exception permits the canon write; before P5 it is refused (E-002) |
| Reads | The inputs; `docs/pfcanon/` on `main`; the procedure; Notion and Drive only for a named input |
| Approval effects | Nathan's G3 approval, recorded verbatim, is `AGENTS.md`'s explicit direction for each named file (line 16). His merge adopts the change (plan ruling 1). A PR merge approves nothing else (D21-C) |
| Dependencies | `gtwpe_redline.py`, `gtwpe_read.py`, `readers.lock`, `gtwpe-run-procedure.md`; the PF canon cited in §1 |
| Exclusions | PF10, PF20 and PF30.x (§8.7); drafting any target itself, since each target has its own drafting subagent (plan §2.4); any action another prompt owns |
| Results | `AWAITING_APPROVAL` (the G3 package; `DECISION NEEDED`) · `CANON_PR_OPEN` (`IN FLIGHT`) · `RUN_COMPLETE` · `NO_CHANGE_COMPLETE` (every target `NO_CHANGE` and none unsure) · `RUN_BLOCKED: <code>` (`DECISION NEEDED`) · `CLOSED_NOT_APPROVED` · `CLOSED_NOT_ADOPTED` |
| Completion | `RUN_COMPLETE` when S9 finds every approved file on `main` equal to the S6 output. A due PF20 or PF30 record is named in the run report as information, never handed off |
| Resume | Only at the checkpoints in §5.3 (`D26-C`) |

#### 4.1.1 Plan §2.2's rows as invocations

| Plan §2.2 row | Inputs given | Targets | PF27; the PF20 or PF30 record |
|---|---|---|---|
| A document only | (a) | The eligible PFs the document bears on | Not touched. A missing specification never blocks Path A |
| A specification and PF10 | (b) and (c) | The PFs the PF10 set's addenda address | PF27 evaluated: `CHANGE` or `NO_CHANGE: <reason>`. The due record is named for GTWPE-RECORD-10 or GTWPE-RECORD-20 |
| A specification, a document, and PF10 | (a), (b) and (c) | The union of both rows | As the row above |
| A specification without PF10 | (b) | The specification's own targets | As above. PF10 is treated as absent, not as an error |
| PF10 only | (c) | The PFs its addenda address | Not touched |
| Nothing usable | None resolves | None | `RUN_BLOCKED: INPUT_MISSING`, listing the accepted inputs |

A document with PF10 and no specification, (a) and (c), takes the union of their targets and touches
neither PF27 nor a record.

### 4.2 GTWPE-RECORD-10 — Record an Epic in HDE Phased Epics

| Field | Contract |
|---|---|
| Purpose | Add one completed Epic's historical record to PF20, or make one bounded correction to an existing record, as a separately authorized historical drainage action (HDE Governance §9.1.1) |
| Owner | Nathan invokes; G3 and G4 are his |
| Inputs | The approved Epic Specification (repository path) with its approval evidence; the evidence that the Epic is closed (the closure decision and its source); supporting records Nathan names. Or `RESUME <run-id>` |
| Rules | PF20 takes completed Epics only and adds each "only once, at epic close" (PF27 §2; PF06 §1.1.2, §3.5.1, §6.3). Specification approval alone is insufficient. The record follows PF27 §2's Epic record template (PF10 2.14), using the "Specification" terms in new text (PF10 2.14). A prior record is updated only when the change "prevents future reader confusion" (PF20 §0, Drain posture). New text names HDE Build Notes by title only (PF10 2.30 governs over PF20's older "Prefer the relevant Addendum entry"). No Epic or issue ID is allocated |
| Destination | The single PF20 file on `main`. A new record goes after the last record as `### 2.<next> <Epic ID> …`, without the outer bold of the older headings (PF03 §8). Because PF20 has no end marker, the edit is a `REPLACE` of its last unique line that reproduces it (PF03 §8 widening) |
| Nonduplication | Search PF20 for the Epic ID first. PF20 already holds two records for HDE-EPIC038 (§2.23 and §2.24); the prompt reports such duplicates and never adds a third |
| Outputs, writes, results | As §4.1, for PF20 only |
| Dependencies, exclusions, completion | As §4.1, except that it writes only PF20, never another file, and is invoked by Nathan alone, never by another prompt. `RUN_COMPLETE` when S9 finds the new PF20 file on `main` equal to S6's output |
| Cost | PF20 is 952,515 B, about 318,000 tokens; its drafter reads all of it (§7.6) |

### 4.3 GTWPE-RECORD-20 — Record a CRD in HDE CRD Records

| Field | Contract |
|---|---|
| Purpose | Register a CRD, record a material change, or record its closure in PF30.x, as a separately authorized historical drainage action (HDE Governance §9.1.1) |
| Owner | Nathan invokes; G3 and G4 are his |
| Inputs | The approved CRD Specification with its approval evidence; for a material update or closure, the exact-source lineage (PR, commit, QA, closure decision). Or `RESUME <run-id>` |
| Rules | The CRD ID is the PO's to allocate and must already exist (PF30.1 §3.1); a missing ID is `RUN_BLOCKED: CRD_ID_MISSING`. One primary record per CRD, updated in place in its originating volume; the material-change history is append-only (§3.2, §4.2). Exact controlled vocabularies (§3.3). No inferred implementation, QA, acceptance, drainage or closure (§3.2, §5). Specification approval is a planned baseline only. "Specification approval" replaces "CRD Plan approval" in new text (PF10 2.14). New text names HDE Build Notes by title only (PF10 2.30), even where the §7 template asks for "exact references" |
| Destination | A new registration goes to the one `Active` volume, currently PF30.1 (§6); an update goes to the record's originating volume. The prompt never opens, closes or rolls over a volume |
| Outputs, writes, results | As §4.1, for PF30.x only. `RUN_BLOCKED: CRD_ID_MISSING` and `RUN_BLOCKED: APPROVAL_EVIDENCE_MISSING` are added |
| Dependencies, exclusions, completion | As §4.1, except that it writes only PF30.x, never another file, and is invoked by Nathan alone, never by another prompt. `RUN_COMPLETE` when S9 finds the PF30.x file on `main` equal to S6's output |

### 4.4 GTWPE-MGMT-10 — Manage the GTWPE

| Field | Contract |
|---|---|
| Purpose | Manage one GTWPE Modification, everything Nathan hands in together, from request to applied and verified result, through `ANALYZE`, `PLAN` and `EXECUTE` (§11) |
| Owner | Nathan requests the change and approves each mode. The managing session runs it |
| Inputs | `MODE` and the subject: the request for `ANALYZE`, or the Modification ID for `PLAN` and `EXECUTE` |
| Outputs | The Modification record and its evidence; successor prompt pages; the catalog update; a `D24` skill package when a skill is in scope |
| Writes | `docs/ephemeral/modifications/` and its evidence; `docs/prompt_ecosystem_management/gtwpe/`; the Notion GTWPE parent page and its catalog, under the destination rule G2 establishes. Never `docs/pfcanon/` |
| Approval effects | `analyze_approved_by` and `plan_approved_by` are written only on Nathan's approval, quoting his words; a merge approves nothing (D21-C). Merges and installs are his |
| Dependencies | The selected PE Metaprompt, with the kickoff's workarounds until its repair; `modification-template.md`, `modification_validate.py`, `reviewer-prompt-template.md`, `ecosystem-change-management.md`, `execution-and-delegation-model.md`, `gcfpe.decision-record.md` |
| Exclusions | PF canon; the GCFPE's register, catalog and PE Metaprompt; TW-ALPHA's pages before G5; running a GTWPE run |
| Results | `PRODUCT_OWNER_ACTION_PENDING`, `ECOSYSTEM_CHANGE_COMPLETE`, `IMPLEMENTATION_BLOCKED`, `PROMOTION_CHECKPOINT_REQUIRED`. It hands off to no prompt |
| Completion | `ECOSYSTEM_CHANGE_COMPLETE` once `EXECUTE` has verified what landed after Nathan's merges and installs |

## 5. A run, stage by stage

### 5.1 The stages

The three run prompts share S4 to S9 through the procedure. The record prompts replace S2 with R2 and
use their own drafting brief.

| Stage | What the manager does | Output | Check that can fail | On failure |
|---|---|---|---|---|
| S0 Intake | Determine the path (plan §2.2), the run ID, the branches; snapshot `origin/main` | `RUN.md` at `INTAKE` | Every input resolves to a readable identity | `RUN_BLOCKED: INPUT_MISSING` naming it, with the accepted inputs |
| S1 Normalize | Record each input. A repository input (the specification, PF10, an addendum file, a repository document) is recorded by path, blob SHA and unit index, with no copy of its bytes. An input from outside the repository (an upload, pasted text, a Notion page, a Drive file) is read into the record with `gtwpe_read.py`, or with the Notion or Drive connector. A Notion page that is a prompt body is recorded by identity only (page ID, title, `page_last_edited_at`), never its body (`D22`; plan §2.3); its drafter reads it live | `source/NN-<name>.json`, plus `source/NN-<name>.md` for an input from outside the repository | Each record carries origin, type, reader and version, byte count, sha256 (none for a prompt body), and a unit index covering the whole input or the stated selection | `RUN_BLOCKED: UNSUPPORTED_INPUT <type>`; never a guessed conversion. With §14 D-6's reader agents, which have no Notion tool, a prompt-body input is `UNSUPPORTED_INPUT notion-prompt-body` |
| S2 Targets (RUN-10) | Build the candidates: every eligible PF the source names by number or title (an exact search of the records), and every eligible PF whose purpose-and-scope sections the manager finds the source bears on, each with its reason (plan §2.2). For (c), add the PFs that B-CLASSIFY-PF10 maps from the PF10 set. Then classify each candidate (§7.3). Evaluate PF27 when a specification exists; name a due PF20 or PF30 record | `targets.md` | `gtwpe_redline.py targets-check`: every target cites a source unit that exists in a record, and passes the eligibility guard for this prompt (§8.7) | An unsure target is named for G3, never dropped or added silently |
| R2 Destination (RECORD-10, RECORD-20) | Resolve the volume, the insertion point and nonduplication by exact search | `targets.md` | The ID exists, is unique in the family, and the destination is unambiguous | `RUN_BLOCKED` naming the missing fact |
| S3 Draft | Spawn one drafting subagent per target (§7); capture each return programmatically (§7.4) | `drafts/<key>.return.md` and `.redlines.md` | The return parses and ends `END OF REDLINES`, or is exactly `no redlines`, or is `BLOCKED` with its reasons | A malformed return is re-dispatched once, then logged |
| S4 Validate | `gtwpe_redline.py validate` | `validate/<key>.json` | Exit 0 (§8.2) | The whole batch goes back to its drafter once with the diagnostic; a second failure is a `REQUIRED` error for Nathan (plan §8) |
| S5 / G3 | Assemble the G3 package; stop and return `AWAITING_APPROVAL` | `G3-PACKAGE.md` | Nathan's reply is recorded verbatim, and `gtwpe_redline.py approval-check` confirms it names the run and each file, or the package version whose file list is fixed | Declined: `CLOSED_NOT_APPROVED`. Changed by him: a new package version, S4 again, G3 again |
| S6 Apply | Fetch `main`; check each base blob is unchanged (§9.1); create the canon branch; `git mv` to the new filename; `gtwpe_redline.py apply`; commit locally | `apply/<key>.json`, `apply/<key>.diff` | The script's diff check: the output equals the one-pass simulation byte for byte, and every changed byte belongs to an approved operation | Stop, keep no file, log `REQUIRED` |
| S7 Verify | Spawn a fresh verifier that sees the approved package, the base and the local commit, never S6's report (§7.3) | `verify/<key>.md` | `gtwpe_redline.py verify-check`: the verifier reports every approved operation present exactly and no unexplained hunk, and its hunks match `apply/<key>.json`. The comparison runs centrally, never in the verifier | Stop; PE37 compares centrally (plan §8) |
| S8 Publish / G4 | Re-check the base blobs; push the canon branch; open the PR | The PR, and `RUN.md` at `CANON_PR_OPEN` | `gtwpe_redline.py pr-check`: `git diff --name-status origin/main...<canon branch>` lists exactly the approved files, and the branch's diff equals S6's | CI red or a conflict: diagnose; fix only within the approved edits, or back to G3 |
| S9 Close | Entered only at `RESUME`, from `main` | `REPORT.md`, `RUN.md` at `COMPLETE` | Each approved file on `origin/main` has the S6 output's blob; each old versioned filename is gone | `RUN_BLOCKED: MAIN_DIFFERS` with the difference |

### 5.2 Records, identities and branches

- **Run ID:** `gtwpe-<yyyymmdd>-<slug>`, lowercase ASCII, because every repository directory is
  lowercase (HDE Governance §0.4).
- **Run directory:** `docs/ephemeral/gtwpe.runs/<run-id>/` holding `RUN.md`, `source/`, `targets.md`,
  `drafts/`, `validate/`, `G3-PACKAGE.md`, `apply/`, `verify/`, `postcheck/` and `REPORT.md`. It never
  holds a whole PF copy, which would be a committed copy of derived output (`STALE-001`); `apply/`
  holds the diff and the identities.
- **Records branch:** `docs/<yyyymmdd>-gtwpe-run-<slug>`, holding only the run directory, pushed at each
  checkpoint. A records PR may be opened to preserve it: "Merging preserves the record and approves
  nothing (D21-C)". In P4, W1's trials record on `docs/20260925-gtwpe-w1` instead.
- **Canon branch:** `docs/<yyyymmdd>-gtwpe-canon-<slug>` from `origin/main` at S6, holding only the
  approved canon files. Its PR body follows the template headings, and its *What merging does* states
  which PF versions become current on `main` and that no QA, acceptance or closure follows (`AGENTS.md`
  line 74). Nathan squash-merges (PF06 §0.2).
- **`RUN.md` frontmatter:** `run_id`, `prompt` and its version, `path`, `status`, `inputs`, `main_at_s0`,
  `records_branch`, `canon_branch`, `canon_pr`, `targets` (key, path, base blob, outcome), `g3` (Nathan's
  words, date, package version), `cost` (time and tokens), `result`. Statuses: `INTAKE`, `NORMALIZED`,
  `TARGETED`, `DRAFTED`, `VALIDATED`, `AWAITING_APPROVAL`, `APPROVED`, `APPLIED`, `VERIFIED`,
  `CANON_PR_OPEN`, `COMPLETE`, `NO_CHANGE_COMPLETE`, `BLOCKED`, `CLOSED_NOT_APPROVED`,
  `CLOSED_NOT_ADOPTED`.

### 5.3 Checkpoints and failure after an external write

`RUN.md` is committed and pushed to the records branch after S1, after S4, when the G3 approval is
recorded, before S8 and after S8. Resume is only at those points (`D26-C`). **S8's push and PR are
the first external write.** After it, a failure takes `D26-B`'s path and nothing more: a failure
record in the run directory, a read-only sweep of what landed, the freeze kept, and a return to
Nathan. S9 detects the merge only by files on `main`, never by commit subjects (`D26-C`).

## 6. Producer and consumer contracts

Common to every handoff: files are UTF-8 with LF line endings; identities are repository paths plus
git blob SHAs, or Notion page IDs plus `page_last_edited_at`; nothing is passed by memory; a consumer
that cannot parse its input stops with the stage's blocked code and never repairs the input.

| # | Producer → consumer | Artifact and format | Required fields and provenance | Consumer's check | Invalid input → return to |
|---|---|---|---|---|---|
| H1 | Nathan → S0 | The invocation | Path A, Path B or both; each input's identity | Each input resolves | Nathan, `INPUT_MISSING` |
| H2 | S1 → S2 | Source record `.json`, plus a `.md` copy only for an input from outside the repository | origin (a repository path and blob SHA, or the outside identity), type, reader and version, bytes, sha256 (none for a prompt body), selection, units with stable anchors | Units cover the whole source or the stated selection | S1, once; then Nathan |
| H3 | S2 → S3 | Drafting brief (§7.2) | run ID, target path and base blob, eligibility class, the source units mapped to it with locations, the brief variant, a capture nonce | The target is eligible for this prompt; the units exist | Manager (a brief is never sent invalid) |
| H4 | Drafter → manager | Return: JSON envelope plus PF03 §15.2 redline blocks, between nonce markers (§7.4) | outcome, coverage rows, coupled edits, document-control proposal, blocked items, `wrote_anything: no` | Parses; set equality with the assigned units; every quoted anchor matches the base bytes | The drafter, once; then logged |
| H5 | S4 → S5 | `validate/<key>.json` and `G3-PACKAGE.md` | per-operation spans, counts, conflicts, simulation result; the package version | Exit 0, or the batch is rejected whole | S3 |
| H6 | Nathan → S6 | His G3 reply | run ID; each file or the package version | Recorded verbatim; names every file applied | Nathan, `DECISION NEEDED` |
| H7 | S6 → S7 | The local canon commit, `apply/<key>.json` | base and output blob SHAs, byte counts | Not shown to the verifier; kept for the central comparison | Stop |
| H8 | Verifier → manager | Return between nonce markers | per operation: present exactly, absent or altered; unmapped hunks | Parses; covers every approved operation | Stop; central comparison |
| H9 | S8 → Nathan | The canon PR | changed paths, PR body, run ID | Paths equal the approved files | Stop; fix within the approved edits |
| H10 | `main` → S9 | The merged files | blob SHAs on `origin/main` | Equal to S6's output | `MAIN_DIFFERS` to Nathan |
| H11 | A run → GTWPE-MGMT-10 | A defect in the run report, carried by Nathan | the failing stage, evidence, the run ID | ANALYZE classifies it (A to E) | Nathan |

**Size and tool assumptions.** The largest eligible targets are PF19 (657,008 B), PF14 (654,042 B),
PF12 (583,759 B) and PF04 (558,988 B), and for GTWPE-RECORD-10, PF20 (952,515 B). At the measured
3.0 bytes a token, a drafter's context at completion stays under about 450,000 tokens (§7.6). A
subagent's context limit is assumed to match the session's 1,000,000 (P0 §4.1). T4 and T2b test it.

**Version compatibility.** Each record names its producer: the prompt ID and version, and the tool
version constant. A consumer that finds another version's record re-validates it and never assumes
compatibility. A run started under one GTWPE version finishes under it; a new version applies from
the next run.

## 7. Subagents: briefs, capture, post-check and cost

### 7.1 When the manager delegates

By workload, never one agent per change for its own sake (proposed GCFPE-MGMT-10 spine). The manager
classifies S2 candidates itself when there are three or fewer and their relevant sections total under
about 60,000 tokens; otherwise it spawns one classifier per candidate. Every drafted target gets its
own drafter (plan §2.4). Every applied target gets its own verifier. Subagents cannot spawn subagents
(P0 §4.2), and they cannot ask Nathan anything (plan §2.4).

### 7.2 The brief frame (E-006)

Every brief is filled from a template in `gtwpe-run-procedure.md`. It carries, in order:

1. **Identity:** "You are a worker inside run `<run-id>`. You did not produce what you are given."
2. **The write-nothing clause, verbatim in every brief:** "You write nothing. Do not create, edit, move
   or delete any file, including under `/tmp`. Do not run a git command that changes any state. Do not
   create, edit or comment on a Notion page, a Drive file, a GitHub issue or pull request. Do not merge,
   push, install, create a session or spawn an agent. Reading is fine. Your answer is your return."
3. **Scope:** the exact target path and base blob, the source units by path and anchor, and the counts
   the manager precomputed, so coverage is arithmetic (`execution-and-delegation-model.md` §2).
4. **The settled rules**, as citations, never paraphrases: PF03 §3, §7, §8 and §15.2; PF06 §0.6.10;
   PF27 *Review guardrails* on rendered escapes; the variant's own rules (§7.3). "Apply them; do not revisit them. If a
   rule looks wrong, say so and stop."
5. **The escape hatch:** "Report any in-scope line your instructions do not cover"
   (`ecosystem-change-management.md` §2 Step 2).
6. **The return format** (§7.4), with the nonce.

### 7.3 The five briefs

| Brief | Stage | Reads | Returns |
|---|---|---|---|
| **B-CLASSIFY** | S2 | the candidate PF's scope and ownership sections, and the sections the source units point at, in full | per source unit: `TARGET` (with the PF section), `ALREADY_REPRESENTED` (with the location), `OUT_OF_OWNERSHIP` (with the owning PF), or `UNSURE` (with the question) |
| **B-CLASSIFY-PF10** | S2, Path B | the whole PF10 set: one logical base version through EOF, plus the named addendum files | per addendum: the permanent PFs it names or bears on, its QA state as recorded (PF06 §3.5.2.8), and whether it supersedes an older one |
| **B-DRAFT** | S3, general targets | the complete target; the assigned units; PF03 in full | the change ledger and redlines. It also lists the target's own maintenance edits (§8.5) and any PF10 next-revision duty naming this target |
| **B-DRAFT-PF09** | S3, a PF09.x phase file | as B-DRAFT | as B-DRAFT, plus the six dimensions, each changed, already represented, out of scope, no relevant change or blocked, with locations; development-board data is never required; no ID, phase, approval, completion or evidence is fabricated |
| **B-RECORD-PF20**, **B-RECORD-PF30** | S3 for the record prompts | the complete destination volume; the Specification; the evidence | the record as redlines, with every field sourced or marked `Unknown` with a reason where the schema allows it |
| **B-VERIFY** | S7 | the approved package, and a diff it computes itself with read-only git: `git diff -M origin/main <local-commit>` in a live run, or `git diff --no-index <base copy> <output copy>` on scratch copies in a trial. Neither writes a file | per operation: present exactly, absent or altered; every hunk not explained by an operation. It never reads S6's `apply/` files (`execution-and-delegation-model.md` §7) |

### 7.4 Capture: returns are extracted, never retyped

Subagents write nothing, so their returns reach the run records through the manager. Retyping them
would risk the defect `EVID-001` records (curly quotes flattened, a line dropped). **The manager
captures each return programmatically.** Each brief carries a fresh nonce, and the return begins
`GTWPE-RETURN <nonce>` and ends `END GTWPE-RETURN <nonce>`. Then `gtwpe_redline.py capture --nonce <n>`
reads the harness's own subagent transcripts under `~/.claude/projects/<project>/<session>/subagents/`,
finds the one assistant message holding both markers, and writes the text between them.

- **Proved in P1.** The P0 probe subagent's transcript is still on disk at
  `…/subagents/agent-acdc66a7d5db676cf.jsonl`, and a JSON parse extracted its final 1,111-character
  answer. P1's diff-check record is captured the same way (§17).
- **Failure is loud.** Zero matches, two different matches, or no transcript directory gives
  `RUN_BLOCKED: CAPTURE_UNAVAILABLE`. There is no manual fallback.
- **Limit.** The layout is the harness's, not a documented interface; a change to it fails loudly (§16).

### 7.5 The post-check: evidence that "writes nothing" held

A subagent's tools include Write, Edit, Bash, Notion writes, GitHub `merge_pull_request` and
`create_session` (P0 §4.2). The brief is the control, and the manager checks it afterwards.
`gtwpe_redline.py postcheck snapshot` runs before each spawn and `postcheck compare` after it:

| Surface | Snapshot | A difference means |
|---|---|---|
| The working tree | `git status --porcelain=v1 -uall`, `git rev-parse HEAD`, `git branch --list`, `git stash list` | a local write |
| The remote | `git ls-remote --heads origin` | a push or a new branch |
| Scratch | the file lists of `/tmp` and the session scratchpad | a file written outside the repository |
| GitHub | the open PRs and the PRs updated since the snapshot (MCP, read by the manager) | a PR created, changed or merged |
| Notion | `page_last_edited_at` of the GTWPE parent page and of `AI Prompts / HDE TW` (read by the manager) | a page created or edited under the GTWPE tree |
| Sessions | `list_sessions` (read by the manager) | a session created |

Any difference stops the run, and the post-check file records it. **Limits:** a Notion write outside
the two watched pages, and a write that is undone before the check, are not detected. §14 D-6 offers a
structural control.

### 7.6 Cost on the record (`D26-D`)

These figures are cost estimates. They are not model, effort or workload fields.

**Unit.** *Context at completion*: the total the Agent tool reports for a finished subagent, the same
measure as P0's probe: 97,191 tokens over 4 tool uses. Estimates use the probe as the base and add the
text each subagent reads, at the measured 3.0 bytes a token (§10.6), plus its output.
*Cumulative input* also counts every re-read of the context across the subagent's tool calls. For a
subagent that reads its target in 25,000-token slices, it is about calls × mean context, mostly cache
reads.

| Subagent | Reads | Context at completion | Cumulative input |
|---|---|---|---|
| B-CLASSIFY, one candidate | scope and relevant sections, 10k–60k | 110k–160k | 0.5M–1.0M |
| B-CLASSIFY-PF10, Path B | PF10 (316,408 B ≈ 105k) and named addenda | about 215k | about 1.5M |
| B-DRAFT, small target (PF03, PF23, PF29: 29–60 KB) | target 10k–20k, units, PF03 13k | 125k–140k | 0.7M–0.9M |
| B-DRAFT, PF09.x (71–195 KB) | target 24k–65k | 145k–190k | 1.0M–1.6M |
| B-DRAFT, PF06 (415 KB) | target 138k | about 265k | about 2.5M |
| B-DRAFT, PF04, PF12, PF14, PF19 (559–657 KB) | target 186k–219k | 310k–345k | 3M–4M |
| B-RECORD-PF30 (PF30.1, 40 KB) | volume 13k, Specification 5k–20k | 125k–145k | 0.7M–0.9M |
| B-RECORD-PF20 (PF20, 952 KB) | volume 318k, Specification | about 450k | about 6M |
| B-VERIFY, any target | package and the diff | 105k–125k | 0.4M–0.6M |

**Per run, subagents plus a fresh manager.** A Path A run on one small target is about 0.4M in
context at completion. Cumulative, it is about 4M–5M, most of it the manager re-reading its own
context over some thirty tool calls. A Path B run with five targets, one of them PF04, is about 2.5M,
or about 20M cumulative. A GTWPE-RECORD-20 run is about 0.4M, or about 4M. A GTWPE-RECORD-10 run is
about 0.7M, or about 10M. The P4 and P5 estimates in §12.5 use these figures.

## 8. The change package and its validator

### 8.1 Package format

One file per target, `drafts/<key>.redlines.md`: a header (run ID, prompt and version, target path,
base blob, drafter nonce, package version), the document-control proposal (§8.4), then PF03 §15.2
redline blocks, each labelled `CONTENT`, `COUPLED` (§8.5) or `NEXT_REVISION` (§8.5), then
`END OF REDLINES`. `G3-PACKAGE.md` lists every target with its outcome, its redlines, its
document-control changes (old and new values), its source citations, the S4 result, each unsure target
with its question, each `NO_CHANGE` and `BLOCKED` result, and a ready-to-send approval sentence naming
every file. It carries `ASK OK?` (PF06 §1.1.11; PF27 *Review guardrails*).

### 8.2 `gtwpe_redline.py validate`: what exit 0 means

| # | Check | Error code |
|---|---|---|
| V1 | The package parses; each block has every PF03 §15.2 field; the operation is `INSERT`, `REPLACE` or `DELETE` | `PARSE`, `OPERATION` |
| V2 | The target passes the eligibility guard for this prompt (§8.7) | `TARGET_INELIGIBLE` |
| V3 | The base file's blob on `origin/main` equals the package's base blob | `BASE_CHANGED` |
| V4 | The heading path matches exactly once, and each boundary line matches exactly once within its scope, against raw bytes (escapes included) | `ANCHOR_COUNT` |
| V5 | An `INSERT`'s two boundary lines are adjacent; a `REPLACE` or `DELETE` range is inclusive and ordered | `BOUNDARY` |
| V6 | No two operations overlap; no `INSERT` sits at or inside another operation's range; no two `INSERT`s share a gap | `OVERLAP` |
| V7 | A one-pass application in descending offset order succeeds, and each paste text lands where its boundaries say | `SIMULATION` |
| V8 | Paste text has no ASCII three-period or Unicode ellipsis (PF03 §3), is not wrapped whole in a code fence, and adds no outer-bold heading (PF03 §8) | `PASTE_FORM` |
| V9 | In a target other than PF10, paste text cites no PF10 locator: no section, addendum number, heading, paragraph or version (PF10 2.30; `AGENTS.md` line 20) | `CITE_PF10_LOCATOR` |
| V10 | Paste text pins no PF file version in a citation (PF10 2.14) | `CITE_VERSION_PINNED` |
| V11 | Document control changes only fields the target already has; the filename's version token equals the new `Version`; each date keeps the target's own format; the version increases | `DOC_CONTROL` |
| V12 | The package holds at least one `CONTENT` operation (no metadata-only bump) | `METADATA_ONLY` |
| V13 | LF only; the result still ends as the base did | `LINE_ENDING` |

V9 and V10 may be overridden per operation only by an entry in the package that Nathan's G3 approval
names; a historical citation kept verbatim is the expected case.

### 8.3 `apply` and its diff check

`gtwpe_redline.py apply` re-runs V1 to V13 on the current base, applies the operations once in
descending offset order, writes the new file and compares it with the S4 simulation byte for byte. It
also checks that every byte outside the operations' spans is unchanged. It records the base and output
blob SHAs, the sha256 values and the byte counts. The whole file is never regenerated (plan §2.4).

### 8.4 Document control

Field sets differ by PF: PF10 has `Name`, `Version`, `Effective Date`, `Status` and `Invocation tag`,
with no Last Update Gate. PF03 and PF04 have `Title`, `Version`, `Status`, `Effective date`,
`Last Update Gate` and `Invocation tag`. PF30.1 uses `Document status` and adds the volume fields.
PF20 writes `**Title**:`. PF16 has an H1 title with `Status`, `Version`, `Date`, `Last Update Gate` and
`Invocation tag` beneath it. **The drafter proposes values only
for fields the target already has, in its own format; Nathan approves each exact value at G3** (PF03
§7, §15.1). The new filename replaces only the version token in the old one. For a filename with no
version token, the file keeps its name and is updated in place. The superseded version leaves
`docs/pfcanon/`, and git history retains it (PF10 2.29).

### 8.5 Edits the target itself requires

A drafter finds and proposes, as labelled blocks in the same package:

- **`COUPLED`, the target's own maintenance rules.** HDE Governance §9.3.1: every normative PF04
  change adds a Change Log entry (`GOV-YYYYMMDD-<shortslug>`, class `NON_EPIC` with its §9.4 record) in
  the same change. Among the other eligible targets, HDE CLI-API-Vendor Ref §11.1 and HDE Schemas and
  Artifacts §9 carry the same kind of duty. HDE Math Spec states that it keeps no revision history.
- **`NEXT_REVISION`, PF10 duties that fall due when this PF is next revised.** For example, 2.31
  removes five sentences of HDE Governance §9.1.6 "When HDE Governance is next revised"; 2.30 names
  drain targets in PF04, PF09.x and PF14; 2.14 says "PF27 and PF30 adopt the same terms on their next
  revision". Each such block is shown at G3, where Nathan keeps or strikes it.

### 8.6 Raw bytes

Anchors and quotes are judged against raw bytes (PF03 §8; PF27 *Review guardrails*). PF files carry escapes from the
Google Docs export, such as `\[`, `\_` and `\<eof\>`, and an anchor reproduces them exactly. No
redline removes a display-layer escape on its own (PF27 *Review guardrails*). An addition at the end of a file with no
end marker, such as PF20, is a `REPLACE` of the last unique line that reproduces it.

### 8.7 Merge targets: Nathan's rulings, and the guard

| Class | Files on `main` today | Written only by |
|---|---|---|
| General | PF03, and every PF file with "canon" in its title except the PF30 family: PF01, PF02, PF04, PF05, PF06, PF07, PF09.1 to PF09.7, PF12, PF14, PF16, PF17, PF19, PF23, PF27, PF29 | GTWPE-RUN-10 |
| PF20 | `PF20-Reference-HDE-Phased-Epics-*` | GTWPE-RECORD-10 |
| PF30 | `PF30.<n>-Canon-HDE-CRD-Records-*`; today PF30.1 | GTWPE-RECORD-20 |
| Never | PF10; the other Reference files (PF08, PF11, PF13, PF15, PF18, PF21, PF31); `PF-Invocation.md`; `PF-Reference-Glow Story.md` | no GTWPE prompt |

Sources: Nathan, 2026-09-28: "No, pF10 will NEVER be a merge target, EVER>"; "with the exception of
PF03 only files with "canon" in their title are valid merge targets"; "PF20 and PF30 are special
targets with dedicated prompts" (`CHECKPOINT.md` §8).

**Guard (`GUARD-001`: a ruling ships with a guard).** `gtwpe_redline.py` holds the class rule. `validate`
and `apply` refuse a path outside the invoking prompt's class (V2), and S8 refuses a PR whose changed
paths leave it. A title check compares the filename with the in-document title (the `Title`, `Name` or
H1 line) and refuses a mismatch as `TARGET_TITLE_MISMATCH` for Nathan. Today all 34 files agree. The P5
skill exception is worded to the same classes and names PF10 as excluded. Selftest cases must fail on a
PF10 target, a Reference target, a PF30 target through GTWPE-RUN-10, and a general target through a
record prompt (§13.2).

## 9. Resolutions: E-003, E-004, E-006, E-007, Q1 to Q3

### 9.1 E-003: the canon PR's branch, and how S9 sees the merge without waiting

- **Branch.** One canon branch per run, `docs/<yyyymmdd>-gtwpe-canon-<slug>`, cut from `origin/main`
  at S6, holding only the approved files; the run records live on the separate records branch (§5.2).
- **No waiting.** At S8 the run returns `CANON_PR_OPEN` with `IN FLIGHT` and the session may end. No
  stage, run or relay waits on the PR (Nathan, 2026-09-28: PRs "cannot gate"). S9 runs only when
  Nathan invokes `RESUME <run-id>`.
- **Detection by files on `main`** (`D26-C`), never by commit subjects or PR state:
  `git fetch origin main`; for each approved file, `git rev-parse origin/main:<new path>` must equal
  the S6 output blob, and `git cat-file -e origin/main:<old path>` must fail when the filename changed.
  All equal: `RUN_COMPLETE`. None present, PR still open: `CANON_PR_OPEN` again, nothing done. PR closed
  unmerged: `CLOSED_NOT_ADOPTED`. Present with other bytes (for example, an edit in GitHub before the
  merge): `RUN_BLOCKED: MAIN_DIFFERS`, with the diff. Squash merges keep blob SHAs, so detection holds.
- **The base moving.** Before S6 and again at S8, each target's blob on `origin/main` is compared with
  the base blob drafted against. **Equal: proceed.** Other commits on `main` do not matter ("A
  changed/different/unavailable SHA alone does not revoke approval", `AGENTS.md` line 92). **Changed:**
  the package is re-validated against the new base. If every anchor resolves to the same text and the
  approved version still follows the new base's version, the approval stands. Otherwise G3 is repeated
  for that file only. "An approval of the old text never carries over" (plan §8).

### 9.2 E-004: pinned readers, or `BLOCKED` per type

- **The set**, in `docs/prompt_ecosystem_management/gtwpe/readers.lock`, as a pip requirements file with
  exact versions and `--hash` pins, resolved and recorded in P2: `pypdf` (`.pdf`; P0 resolved 6.19.0),
  `openpyxl` (`.xlsx`), `mammoth` (`.docx` to HTML), `markdownify` and `beautifulsoup4` (HTML to
  Markdown, also used after `mammoth`). `.csv` uses the standard library; Markdown and text are read
  as they are. The skills named in plan §2.3 (`docx`, `pdf`, `xlsx`) remain the reading guidance. Where a
  skill names a tool that pip cannot provide (`pandoc`, `pdftotext`), the lock's library is used.
- **The lock lists the full dependency closure,** because `--no-deps` installs nothing unlisted: for
  example `cobble` under `mammoth`, `soupsieve` under `beautifulsoup4`, `et-xmlfile` under `openpyxl`.
- **Provisioning**, once per run and outside the repository:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m pip install --require-hashes --no-deps --target "$SCRATCH/gtwpe-readers" -r readers.lock`.
  The source record names the reader, its version and the lock's sha256.
- **`BLOCKED` per type.** An install failure, a hash mismatch, an import error, a conversion error, or
  empty text from a non-empty file (a scanned PDF, for example; there is no OCR) gives
  `RUN_BLOCKED: UNSUPPORTED_INPUT <type>` for that input. Nothing is guessed, and a run whose required
  input is blocked does not continue (plan §2.3).
- **P2 builds and tests it** with a synthetic file of each type, and proves the blocked path by
  pointing the install at an unreachable index.

### 9.3 E-006: the subagent brief and the post-check

The brief is §7.2, with the write-nothing clause verbatim in every brief. The post-check is §7.5, run by
the manager around every spawn, and in P1 around the diff-check reviewer (§17). A structural control is
offered at §14 D-6.

### 9.4 E-007: PE defects D5, D7, D8 and D10

| Defect | Handling in the GTWPE | Where the PE repair goes |
|---|---|---|
| **D5**, two handoff rules | Every GTWPE prompt returns to Nathan and hands off to no prompt, with no `NEXT_PROMPT_HANDOFF` (§4). A due PF20 or PF30 record is named as information in the run report | The MGMT-10 promotion Modification (E-007) |
| **D7**, the model-advice ban forbids evaluating effort | No model, effort or workload content in any GTWPE body, contract or brief. Subagents inherit the session's model: the Agent call passes no `model`. HDE Governance §9.1.3's advice duty is for "downstream-session" prompts, and the GTWPE hands none off. §9.1.6 permits, and does not require, a human model header (PF10 2.31). A definition-level setting is evaluated only when Nathan asks (the PE test's proposed ruling) | The same |
| **D8**, a PE refactor misses non-GCFPE consumers | GTWPE-MGMT-10 lists a PE Metaprompt change among its triggers. Its `ANALYZE` runs the `D26-E` search, broad match minus permitted exceptions, over every GTWPE body, brief, procedure and tool, for text the new PE rule contradicts | The same: the PE's own change process should reach non-GCFPE consumers |
| **D10**, Drive against `D7` | A Drive file is a Path A input **only when Nathan names that specific file** in the invocation, by ID or link. It is read once at S1 through the Drive connector, and the record holds its ID, name, `modifiedTime`, MIME type and reader. It is never PF authority, never searched for, and never written ("A file lives there only where Nathan directs that specific file", `authoritative-surfaces.md`). §14 D-4 | The same |

### 9.5 Q1 to Q3

| Question | Plan default | Status in this design |
|---|---|---|
| Q1: does an Epic specification update PF20? | No | **Superseded by Nathan's ruling of 2026-09-28**: PF20 is a special target with a dedicated prompt, GTWPE-RECORD-10 (§4.2). The record is added only for a completed Epic, at close (PF27 §2) |
| Q2: what is "the applicable PF10 file set"? | The current `docs/pfcanon/PF10-*.md`, plus the `PF10_BUILD_NOTES_ADDENDUM` files the specification names | **Default kept.** The current PF10 is one logical base version: the unlettered file, or the complete verified contiguous lettered set (PF10 §3, §4). A named addendum file is an approved decision text not yet inserted into PF10. **The whole set is source only: the GTWPE never inserts, adds or removes a PF10 addendum** (Nathan, 2026-09-28) |
| Q3: is §2.3 the complete list of types? | Yes; others are `UNSUPPORTED_INPUT` until added through GTWPE-MGMT-10 | **Default kept** |

## 10. Canon and rulings the plan predates

### 10.1 `AGENTS.md` changed after P0

Five commits on 2026-09-27 changed it from sha256 `94c38926…` (50,015 B) to `2a28ac5c…` (55,079 B).

- **Line 16 replaced the exception plan §1 and §2.4 S5 quote.** It now reads: "Agents must not modify
  any PF canon document, PF10 included, unless the current prompt explicitly directs the agent to modify
  that particular file." The design meets it at G3: Nathan's reply is in the running prompt, and it
  names each file, or a package version whose file list is fixed (§5.1 S5).
- **Lines 11 and 12:** "Existing PF canon documents are not rewritten merely to incorporate those later
  changes. Further canonical changes are normally introduced through a new PF10 addendum". The GTWPE's
  purpose is to revise permanent PFs, from a document (Path A) or from PF10 (Path B). The design treats
  each G3 approval as the explicit exception, never as routine. §14 D-2 asks Nathan to confirm that
  posture.
- **Line 29:** "The historical Epic and CRD records documents are reference-only, not planning,
  registration or approval gates". The record prompts write records; no run waits on one.
- **Line 74** sets the canon PR's *What merging does*. **Line 92** sets how a moved base is judged (§9.1).

### 10.2 Nathan's rulings of 2026-09-28

Three rulings in P1, recorded verbatim in `CHECKPOINT.md` §8: PF10 is never a merge target; only PF03
and files with "canon" in their title are valid merge targets; PF20 and PF30 are special targets with
dedicated prompts. §8.7 applies them, §2 changes the membership to match, and Q1 is superseded.

### 10.3 HDE Governance §9.1.1: the historical homes

"**HDE Phased Epics** and **HDE CRD Records** are historical/reference homes only… The active workflow
MUST NOT create, update or synchronize their entries", and "Only a separately authorized historical
drainage action may add the approved planned baseline as planned state and actual implementation, PR,
Ops, QA, evidence, variances and disposition as distinct actual state." That conflicts with PF06 §1.0.3
and §1.0.6 and PF27 §2A, which put a PF30 record before implementation and at closure. HDE Governance
owns "the authority, approval, permission and claim boundaries". The record prompts fit §9.1.1 as it
stands: each run is invoked separately and approved at G3, and no workflow step waits on one. The
conflict between the three documents is Nathan's to settle. The GTWPE does not settle it.

### 10.4 PF30 records only CRDs

Plan §2.2 says "PF30.1 gets the change's record" whenever a specification exists. An Epic Specification
has no PF30 record (PF30.1 §1, §2); its history goes to PF20, at close. GTWPE-RUN-10's Path B names the
due record prompt accordingly.

### 10.5 Drainage ordering and next-revision duties

PF06 §3.5.2.8: drainage into canon "occurs only after all QA tasks for the epic are complete". Path B
therefore records each addendum's QA state (B-CLASSIFY-PF10). An addendum whose QA is incomplete or
unknown is not drafted; it is listed at G3, and drafting it needs Nathan's direction there. The
`NEXT_REVISION` blocks (§8.5) carry PF10's duties that fall due when a PF is next revised.

### 10.6 Measurements

PF text through the Read tool runs at about **3.0 bytes a token**: lines 1000 to 1459 of PF27 are
85,734 B and returned 28,668 tokens. P0 and the analysis assumed 4. Ten PF files are now 300 KB or
more; PF10 crossed the line since P0.

## 11. GTWPE-MGMT-10: scope, lineage and relation to the PE

**Lineage.** Derived from *GCFPE-MGMT-10 — Manage an Ecosystem Change — PROPOSED BODY (D20 redesign)*,
Notion `3e34590a05eb811b93d2da9b4ef8106d`, last edited 2026-09-24T11:00:24.691Z, status
`APPROVED_FOR_TESTING`, not promoted. The PE Metaprompt's rule: "duplicate and customize the prompt for
each ecosystem as requested, record lineage, and approve updates separately". A later GCFPE promotion
does not change GTWPE-MGMT-10. A change to it is a GTWPE-MGMT-10 Modification of its own.

**Kept from the source.** Three modes over one spine; two inputs (`MODE` and the subject); one
Modification per run, in parts, each landing whole or not at all; scope frozen at analysis approval;
approval as a recorded field quoting Nathan's words, never inferred from a merge; `D26`'s bounded reviews,
with the *ANALYZE and PLAN review brief*; resume only at checkpoints, with merges detected by files on
`main`; workers by workload; results `PRODUCT_OWNER_ACTION_PENDING`, `ECOSYSTEM_CHANGE_COMPLETE`,
`IMPLEMENTATION_BLOCKED`, `PROMOTION_CHECKPOINT_REQUIRED`; "This prompt hands off to no other prompt."

**Customized.**

| Point | GCFPE-MGMT-10 proposed body | GTWPE-MGMT-10 |
|---|---|---|
| Scope | GCFPE members, graph parts, the registry | The four GTWPE prompts, `gtwpe-run-procedure.md`, the tools, the lock, the selftest, the GTWPE parent page and catalog, and the GTWPE wording of `glow-write-boundary`'s exception |
| Dependency closure | `closure.py` over graph parts | The GTWPE has no graph parts. Its closure is §6's producer-consumer table, updated in the Modification record |
| Member comparison | — | For any member change, every other member gets an affected or unaffected disposition with a reason (HDE Governance §9.1.6) |
| Triggers | A request | A request; a run defect (H11); a change to the PE Metaprompt (`D8`); a change to a cited rule: PF03 §8, §15.2; PF06 §0.6.10; PF10 2.8, 2.14, 2.29, 2.30; PF27 *Review guardrails*; PF30.1 §3 to §7; HDE Governance §9.1.1, §9.3.1; `AGENTS.md`; `glow-write-boundary`; the decision record |
| Records | `docs/ephemeral/modifications/`, format 2.1 | The same directory, slug prefix `gtwpe-`; P2 checks that `modification_validate.py` accepts a record whose `closure` is not `closure.py` output (§16) |
| Notion writes | GCFPE maintenance surfaces | The GTWPE parent page and its catalog only, under the destination rule G2 establishes (`notion-write-boundary.md`). A finding outside the frozen scope goes back to Nathan in the record. There is no GTWPE backlog page unless he makes one |
| May not change | — | PF canon; the GCFPE register, catalog or PE Metaprompt (HDE Governance §9.1.6: its scope "does not extend automatically to another ecosystem"); TW-ALPHA pages before G5 |

**Relation to the PE.** GTWPE-MGMT-10 authors prompt changes through the selected PE Metaprompt, under
the kickoff's workarounds, until the PE repair lands. The PE's GCFPE overlay does not apply to the
GTWPE. Its general rules do (decision record, successor of 2026-09-23).

## 12. Change plan

### 12.1 Order

| Phase | Deliverable | Validation | Gate |
|---|---|---|---|
| **P2 Tools** | In `docs/prompt_ecosystem_management/gtwpe/`: `gtwpe_redline.py` with subcommands `targets-check`, `validate`, `approval-check`, `apply`, `capture`, `verify-check`, `pr-check`, `postcheck`, `detect-merge`; `gtwpe_read.py`; `readers.lock`; `gtwpe-run-procedure.md` (S4 to S9, the brief frame and templates, the post-check); `selftest.py` with at least 30 cases (§13.2); `guard_proof.py` | V2: selftest 100%; every check shown to fail when disabled | — |
| **P3 Publish** | The Notion writes in §12.2, each read back | V3: title, parent, identity lines and complete body verified; no page outside the list | **G2** before the first write |
| **P4 Trials** | T1 to T5 on scratch copies (§13.1) | V4: each expected result matched; each mismatch in `ERRORS.md` | — |
| **P5 Adoption** | (1) The `D24` skill package: `glow-write-boundary`'s GTWPE exception, `tw-flowmaster` retired, `flowmaster-validate` updated. Two reviewer subagents, Nathan's install, then the post-install digest comparison. (2) Only then T6, live through S5 to S9. (3) Superseded banners on TW-ALPHA's pages and a decision-record entry | V5: T6's files on `main` equal the approved edits; the skills installed and read back | **G3 and G4** in T6; **G5** |

### 12.2 The Notion writes for G2

In this order, each read back completely before the next: (1) create *GTWPE — Glow Technical Writing
Prompt Ecosystem* under `AI Prompts / HDE TW` (`3c74590a05eb8176baf8cb59f1631f3c`); (2) to (5) create
GTWPE-RUN-10, GTWPE-RECORD-10, GTWPE-RECORD-20 and GTWPE-MGMT-10 under it; (6) update the parent's
catalog block with the four versions and page IDs. Bodies are authored in the session. Any scratch
draft is deleted after publication and disclosed (`D22`); no body enters the repository (plan §4). The
G2 request lists each write with its title, parent and identity lines, and gives each body in the
request itself for review.

### 12.3 Compatibility and selection

TW-ALPHA-20260908.1 stays selected on its page until G5. The GTWPE runs alongside it from P5. A run
touches no TW page. At G5 the GTWPE catalog becomes the selection and the TW pages get banners; no page
is moved, rewritten or deleted.

### 12.4 Rollback, compensation and in-flight work

| Change | Before it lands | After it lands |
|---|---|---|
| A tool or procedure in the repository | Discard the branch | A GTWPE-MGMT-10 Modification |
| A Notion page | Not written until G2 | `D26-B`: a failure record, a read-only sweep, the freeze kept, a return. Nathan archives or restores from page history |
| A canon PR | Close it unmerged: `CLOSED_NOT_ADOPTED` | Compensation, never rollback: a new run whose package reverses the edits, approved at G3 |
| A skill | Nathan does not install | Nathan reinstalls the prior digest (`CHECKPOINT.md` §4.4) |

A TW session already in flight finishes under TW-ALPHA. The GTWPE starts no run on its behalf.

### 12.5 Estimates (`D26-D`)

| Phase | Plan | This design's estimate |
|---|---|---|
| P2 | about 2 h, 1M tokens | about 3 h, 1M context tokens. Nine subcommands, two tools and the procedure exceed the plan's scope |
| P3 | about 1 h, 0.5M | about 1.5 h, 0.6M. Four prompts, not two |
| P4 | about 3 h, 2M | about 4 h. The trials' subagents total about 2.5M in context at completion, or about 20M cumulative (§7.6), plus W1's own session. T2b reads PF20 in full |
| P5 | about 2 h, 1M | about 2 h, 1M, plus Nathan's installs; T6's cost follows §7.6 |

These exceed the plan's figures but stay under twice them, except P4's cumulative measure. **Which
measure the plan's "tokens" means is for PE37 to say** (§14 D-11).

## 13. Test specification

### 13.1 Trials

Fixtures are synthetic Markdown or scratch copies. No prompt body is stored (`D22`). T1 to T5 write
only to scratch copies and to `docs/ephemeral/` (plan §11).

| Trial | Input | Expected result |
|---|---|---|
| T1 | Path A: a short synthetic Markdown document asking for one wording fix in a scratch copy of PF03 | One target, PF03; PF27 and PF30.1 untouched; a one-operation package passes S4; S6's output differs from the base only in that span; S7 finds zero differences; S8 and S9 run dry: the PR body is written, and `detect-merge` runs against a synthetic merged repository |
| T2a | GTWPE-RECORD-20: a synthetic CRD Specification with a synthetic approval, against a scratch copy of PF30.1 | A new record inserted in CRD-ID order, with exact vocabulary and "Specification approval"; no ID allocated; V9 passes. A second invocation for the same ID is refused as a duplicate |
| T2b | GTWPE-RECORD-10: a synthetic completed Epic, against a scratch copy of PF20 | A record appended by a `REPLACE` of the last unique line; an Epic without closure evidence is refused |
| T2c | Path B: a synthetic Specification and a synthetic PF10 file of two addenda (one naming PF23 as a drain target, one with its QA incomplete) | PF23 is drafted; the second addendum is listed at G3 and not drafted; PF27 gets `NO_CHANGE: <reason>`; the due PF30 record is named, not drafted |
| T3 | A PF09 phase target: synthetic evidence for one subtask, against a scratch copy of PF09.x | All six dimensions accounted for; nothing fabricated |
| T4 | A target of 300 KB or more: PF04, PF12, PF14 or PF19 (scratch copy), with a one-line change | The exact-edit path; the output equals the base outside one span; for PF04, the §9.3.1 `COUPLED` entry is proposed |
| T5 | Negative cases: a non-unique anchor; overlapping edits; `.pptx`; a missing input; the base changed after S4; a PF10 target; a Reference target; a PF30 target through GTWPE-RUN-10; a missing capture marker | Each fails loudly with its code: `ANCHOR_COUNT`, `OVERLAP`, `UNSUPPORTED_INPUT pptx`, `INPUT_MISSING`, `BASE_CHANGED`, `TARGET_INELIGIBLE` (three times), `CAPTURE_UNAVAILABLE` |
| T6 | One real change Nathan approves, run live through S5 to S9 | The whole flow end to end. Candidates, for Nathan at P5: the "Specification" terms in PF30.1 (PF10 2.14), or the five superseded sentences in HDE Governance §9.1.6 (PF10 2.31). Each is subject to §14 D-2 |

### 13.2 P2 selftest, at least 30 cases

Positive: one of each operation; two non-overlapping operations; an `INSERT` beside a `REPLACE` that
does not touch it; an escaped anchor matched on raw bytes; an end-of-file addition by `REPLACE`; a
document-control change in each of the four field sets; a filename without a version token; capture of
a well-formed return; `detect-merge` in each of its four outcomes; the post-check with no change.
Negative, each with its code: a missing field; an unknown operation; a boundary matching twice; a
heading path matching zero times; non-adjacent `INSERT` boundaries; an overlap; two `INSERT`s at one
gap; a simulation that misplaces text; an ellipsis; a whole-block fence; an outer-bold heading; a PF10
locator in PF04; a version-pinned citation; a metadata-only package; a changed base; CRLF; each of the
four eligibility refusals; a filename and title mismatch; a capture with no match and one with two; a
post-check with a new file under `/tmp`. One positive and one negative case each for `targets-check`,
`approval-check`, `verify-check` and `pr-check`. **Guard proof:** each check disabled in a scratch copy fails
its own cases.

## 14. Decisions for G1

Each has a default. G1's approval takes the default unless Nathan's words say otherwise.

| # | Decision | Default or recommendation | Why it is his |
|---|---|---|---|
| D-1 | Are GTWPE-RECORD-10 and GTWPE-RECORD-20 separate prompts, or dedicated briefs inside GTWPE-RUN-10? | **Separate prompts**, sharing S4 to S9 through `gtwpe-run-procedure.md` | His ruling's wording, "dedicated prompts", settles which |
| D-2 | `AGENTS.md` lines 11 and 12 make a new PF10 addendum the normal route, and PF10 is never a GTWPE target. Confirm that the GTWPE revises permanent PFs only on his per-file G3 direction, as the explicit exception | **Confirm** | A policy question under his rulings |
| D-3 | PF06 §3.5.2.8: in Path B, an addendum whose QA is incomplete or unknown is listed at G3, not drafted, unless he directs | **Confirm** | Canon states the order; exceptions are his |
| D-4 | `D10`: a Drive file is a Path A input only when he names that specific file | **Confirm** | E-007 routes this decision to him |
| D-5 | Identity lines: keep the PE's two lines, including `Prompt Version:`, since TW is outside `D23-G` and AF-012 is open for it. Or adopt `D23-G`'s no-release-line rule for the GTWPE | **Keep the PE's lines** | `D23-G`'s scope is his ruling |
| D-6 | Two project agent definitions under `.claude/agents/`: `gtwpe-reader` (`tools: Read, Grep, Glob`) for classifiers and drafters, and `gtwpe-verifier` (`tools: Read, Grep, Glob, Bash`) for S7's read-only `git diff`. They remove Write, Edit and every MCP tool (Notion writes, GitHub merges, session creation); a drafter could then write nothing at all | **Recommended.** They sit outside `glow-write-boundary`'s paths, so they need his instruction or the P5 exception. Without them, §7.5 stands alone. P2 must also confirm that a session picks up a definition added mid-session | A write outside the permitted paths |
| D-7 | Capture subagent returns from the harness transcripts (§7.4), with no manual fallback | **Adopt** | It relies on an undocumented harness layout |
| D-8 | GTWPE-MGMT-10 uses `docs/ephemeral/modifications/` and `modification_validate.py`, with `closure` recorded from §6 | **Adopt**, subject to P2's check | It reuses a GCFPE control |
| D-9 | Plan §1's other two controls, the PE Metaprompt's "read-only" line and the release register's PF rule, are GCFPE controls outside GTWPE-MGMT-10's scope. Route them to a GCFPE Modification under PE37 before T6, or rule that they do not govern GTWPE runs | **A GCFPE Modification, before T6** | Another ecosystem's controls |
| D-10 | The destination rule for GTWPE-MGMT-10's Notion writes: the GTWPE parent page and its catalog block only | **Establish it at G2** | Notion writes need an explicit rule |
| D-11 | Which token measure the plan's estimates use: context at completion, or cumulative input | **PE37 to state**; this design reports both | The twice-the-estimate stop depends on it |

## 15. Errors for the ledger

For PE37 to enter in `ERRORS.md`. W1 does not write the ledger.

| # | Class | Severity | Finding | Evidence | Proposed disposition |
|---|---|---|---|---|---|
| P1-1 | SOURCE | LISTED | `AGENTS.md` changed on `main` after P0. Plan §1 and §2.4 S5 quote an exception that no longer exists | §10.1; `git log -- AGENTS.md` | Design: G3 names every file. Plan wording: PE37 |
| P1-2 | SOURCE | LISTED | HDE Governance §9.1.1 conflicts with PF06 §1.0.3, §1.0.6 and PF27 §2A on PF30 and PF20 records | §10.3 | For Nathan; the record prompts fit §9.1.1 |
| P1-3 | PLAN_DEFECT | LISTED | Plan §2.2 gives every specification a PF30.1 record; Epics have none | §10.4 | Fixed in the design |
| P1-4 | PLAN_DEFECT | LISTED | Plan §2.5 and Q1 predate Nathan's three rulings of 2026-09-28 | §10.2 | Fixed in the design |
| P1-5 | SOURCE | LISTED | PF text runs about 3.0 bytes a token, not 4; ten PFs are now 300 KB or more | §10.6 | Pricing uses the measured rate |
| P1-6 | SOURCE | LISTED | P0's `D22` disclosure named the tool-results file but not the harness's session and subagent transcripts, which also hold what was fetched. They stay outside the repository, are never hashed or compared by W1, and are left to harness teardown | `CHECKPOINT.md` §5 | Disclosed here and in the P1 checkpoint |
| P1-7 | AUTHORITY | LISTED | Plan §1's PE Metaprompt line and register PF rule are GCFPE controls outside GTWPE-MGMT-10's reach | §14 D-9 | For Nathan through PE37 |

## 16. Open findings, listed as accepted risks

Listed, not repaired (`D26-A` rule 4). Each is a loud stop or outside the normal path.

| Finding | Path | Likelihood | Consequence | Why listed |
|---|---|---|---|---|
| Capture depends on the harness's transcript layout | normal | low per release | `CAPTURE_UNAVAILABLE` stops the run | Loud; no silent path. D-7 |
| The post-check misses a Notion write outside the two watched pages | failure | low | An unauthorized page could survive unseen | The brief forbids it; D-6 would remove the tool |
| A subagent's context limit is unverified above 450k | normal, for PF20 | low | A drafter fails to finish: a loud `BLOCKED` | T2b and T4 measure it |
| `modification_validate.py` may reject a GTWPE record's `closure` | normal, for GTWPE-MGMT-10 | medium | A validator error at the first GTWPE Modification | P2 checks; D-8 |
| PF20 holds two records for HDE-EPIC038 | — | — | A reader may be confused | Reported, not repaired: PF20's drain posture allows only a bounded correction on Nathan's direction |

## 17. Reviews ledger

`D26` shape: `{mode, kind, date, required_open, outcome}`. The mode is `PLAN`: this is P1's design,
reviewed as a plan. The plan fixes the budget at one dry run and at most one diff check (plan §5, P1;
the relay).

```yaml
reviews:
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-28
    required_open: 8
    outcome: "DR-1 to DR-8 (seven R1, one R3) and 4 listed, in design/DRY-RUN-P1.md; all 8 repaired in 42badb7"
  - mode: PLAN
    kind: DIFF_CHECK
    date: 2026-09-28
    required_open: 3
    outcome: "RQ-1 to RQ-3 (two R1, one R3) and 13 listed, in design/REVIEW-P1-DIFFCHECK-R1.md. 8 to 3 halves, but all three sit in text the repair added (D26-A rule 5), and P1's cap is spent: returned to Nathan, DECISION NEEDED, not repaired"
```

The diff check was one fresh `general-purpose` reviewer, GTWPE-P1-DC-R1, briefed only by the
committed `design/REVIEW-BRIEF-P1-DIFFCHECK.md` (commit `ec82849`). Its record was captured by script
from its own transcript, as its `SubagentHandback` message: 19,754 bytes, sha256 `a5835377…`. It was
written to the record file unedited, with a final newline added. The post-check (§7.5) found no write
attributable to the reviewer. The one exception is the harness's automatic save of one oversized tool
result, which the reviewer disclosed; it holds a copy of `P1-SOURCE-NOTES.md`.

## 18. What this package does not claim

It writes and approves nothing: no prompt, page, tool, skill or canon file exists because of it. It
claims no test result: T1 to T6 and the selftest are specified, not run. It does not settle the canon
conflict in §10.3 and edits no PF document. It does not change the GCFPE's controls, register or PE
Metaprompt. Merging the records branch preserves this record and approves nothing (D21-C).
