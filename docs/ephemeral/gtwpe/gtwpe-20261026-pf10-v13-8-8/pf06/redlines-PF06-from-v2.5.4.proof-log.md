# Proof log — redlines-PF06-from-v2.5.4.md (T-PF06 preparation)

This is the processing report for the redlines file beside it. It records what the redlines change, what they rest on, how they were built and what was checked. It establishes no canon adoption, QA, acceptance or closure, and it is not a revised PF.

## 1. Identity

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf06/redlines-PF06-from-v2.5.4.md` (17 operations, all `REPLACE`; ends `END OF REDLINES`) |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf06/redlines-PF06-from-v2.5.4.proof-log.md` |
| Run identity | `gtwpe-20261026-pf10-v13-8-8 / T-PF06 / TW-DRAIN-10 run 1` (first preparation run for this target and source set; no earlier T-PF06 output existed on the branch) |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff (page state 2026-10-09T11:05:22Z; fetched live and read in full on 2026-10-26) |
| Preparer | This Claude Code session, https://claude.ai/code/session_01H9YUsfAYvAB5rJUKsZrCxB, started by Nathan with the GTWPE 100926.1 T-PF06 handoff. One session, no subagents, no reviewers |
| Authorized sequence | The handoff authorizes TW-DRAIN-10 and then TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b) in this same session |
| Preparation outcome | `READY` |
| Save completeness | `COMPLETE_PACKAGE` (receipt in §14, recorded after read-back) |
| Preparation date | 2026-10-26 (UTC) |
| Branch and PR | `docs/20261026-gtwpe-pf10-v13-8-8-documents` (the ledger's predeclared continuation, created by the T-PF07 session from `origin/main` `0838ba0`), shared draft PR [#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761). The ledger PR [#760](https://github.com/amthorn78/glow-hdengine-v2/pull/760) merged at 2026-10-26T21:18:51Z |

## 2. Target and baseline

| Field | Value |
| :---- | :---- |
| Path | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md` (read only; never written) |
| Logical title and version | PF06-Canon-Change-Process-Guide, v2.5.4, Status Canon, one unlettered file, no volume or phase parts |
| Baseline commit | `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`. Read at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`; `git diff --name-only 9dda63dd 0838ba08` lists only the triage ledger, so the target bytes are those of the baseline |
| Git blob | `d2df157b4014224406a8a0c52b64e28c53395e99` (matches the handoff and ledger prefix `d2df157b4014`) |
| Bytes, lines, SHA-256 | 428,753 bytes; 4,651 LF-terminated lines; SHA-256 `6f47d808c58708e03e28a0c9ca106248054257755503681d3e60e36deed9fe46` over the raw bytes |
| Byte shape | UTF-8, no BOM, LF only (no CR), file ends with two LF (line 4651 is empty); longest line 1,843 characters (line 2610) |
| Newer version on `main` | None: `docs/pfcanon/` on `main` holds only `PF06-Canon-Change-Process-Guide-v2.5.4.md` for PF06 |
| Native document-control header | `**Title:** PF06-Canon-Change-Process-Guide` (line 3); `**Version:** v2.5.4` (line 5); `**Status:** Canon` (line 7); `**Effective date**: 2026-10-09` (line 9); `**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md` (line 11); `**Invocation tag:** INV-f2ac55d77ce9aacc` (line 13). Version scheme: `v` plus three dotted numeric components. Date format: `YYYY-MM-DD`. Gate form: `BN <PF10 version>; <source filename>` |
| Change history | PF06 has no change log, revision history or Doc-Delta entry section, and no internal restatement of its own version or date outside the header (searched for `2.5.4`, `v2.5`, "change log", "revision history"). No history redline is owed |

## 3. Coverage of the target

The whole target was read in eight bounded line windows with the Read tool, whose per-line limit (2,000 characters) exceeds the longest line (1,843), so no line was truncated.

| Window (lines) | Lines | Bytes |
| :---- | :---- | :---- |
| 1–454 | 454 | 54,877 |
| 455–1036 | 582 | 54,899 |
| 1037–1607 | 571 | 54,893 |
| 1608–2186 | 579 | 54,769 |
| 2187–2636 | 450 | 54,709 |
| 2637–3390 | 754 | 54,816 |
| 3391–4148 | 758 | 54,979 |
| 4149–4651 | 503 | 44,811 |
| Total | 4,651 | 428,753 |

The windows are contiguous and their totals equal `wc -l` (4,651) and `wc -c` (428,753) of the baseline and the blob above. Coverage: complete.

## 4. Sources, roles and selected scope

All repository sources were read at `origin/main` (`9dda63dd`, equal bytes at `0838ba08`).

| Ref | Role | Identity | Boundaries read |
| :---- | :---- | :---- | :---- |
| SR1 | Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, v13.8.8, effective 2026.10.26, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | Front matter lines 1–223 in full. Addenda in full, heading to next heading: 2.11 (1205–1318), 2.14 (1549–1619), 2.15 (1620–1690), 2.16 (1691–1825; long lines read in folded form, every source line label L1691 to L1825 present), 2.17 (1826–1955), 2.18 (1956–2081, context only), 2.31 (3361–3470). Each boundary was checked against the next H2 |
| SR2 | Change source (approved base Specification) | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1, SPECIFICATION_APPROVED, blob `c4802a5a7fa33db38d42d8a7f64679cd18b50480`, 43,151 bytes, SHA-256 `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df` | Lines 1–230, which contain S-APR (147–193) and S-CR1, CR-1 (199–208), plus their context (front matter, Format and register posture, requirements, CR-2, CR-3) |
| SR3 | Overlay (approved delta 01) | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb`, 21,046 bytes, SHA-256 `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636` | Lines 1–162 in full. C-8 to C-12 change the Conjunction, Fermentation and Coagulation phase-block cells, the ordering line and the Live QA table's S01 row; none changes the S21 canon-impact bullets that S-APR routes to PF06, and §4 of the delta preserves CR-1 to CR-3 as carried |
| X03 | Supporting cross-reference | `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a198168958bf8b32c5f8b5459ee13de5b`, 25,360 bytes | Whole file (98 lines, read in folded form): status and amendment lines, Decision (items 1 to 9, lines 18–34), Stated limits, and "Affected canon and drainage consequences" (lines 76–90; the rows for Change Process Guide §3.5.2, §3.5.2.1 and §3.5.4) |
| X10 | Approval evidence | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`, blob prefix `c48f77a0c220` | Front matter: `decision: INITIAL_APPROVE` |
| SR4 | Approval evidence | `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`, blob prefix `5a6cecc86f60` | Front matter: `decision: DELTA_APPROVE` |
| X11 | Closure evidence | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md`, blob prefix `2260eae17974` | Front matter: `decision: CLOSE`, `state: CHANGE_CLOSED`, `decision_time: 2026-10-26T16:40:00Z`, decision owner Isis |
| X12 | Closure evidence | `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md`, blob prefix `ac60f368f6d9` | Front matter and the M-0 row ("PF10 drainage of HDE Build Notes 2.2 to 2.32 for this change [OMITTED] into permanent canon — Pending") |
| X13 | Closure evidence | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md`, blob prefix `d6cceaf3a019` | Front matter: `artifact_type: QA_REPORT`, `verdict: PASS` |
| X14 | Closure evidence | `audit/HDE-CRD-0002_close_report.md`, blob prefix `0bbc8050d3c1` | `Closure decision: SATISFIED`, `Decision posture: review-trace-only`, and the deferral naming Change Process Guide §3.5.1, §3.5.2, §3.5.2.1 and §3.5.4 ("Close expectation: after a separate canon-only drain step") |
| L | Routing record | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, blob `74944b261c0ebb2f80a416fb004b9a913da592d1` at commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` and on `main` | Read in full, including "Precedence and closure controls" and "Held and deferred items"; task row T-PF06 |

Supporting reading, not drainage:

* HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`, blob prefix `86cf613ce7f9`), §9.1 "Single-home doctrine" (including "Ops tasks" and "Epic and CRD change lanes"), §9.1.1 "Change authority and exact-artifact lineage" (including "Historical drainage") and §9.1.2 "Canon precedence and persistent sources": lines 2351–2440, read in full. §9.1.1 is the owner CR-1 aligns PF06 to.
* Technical Writing Best Practices (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob prefix `504712df548a`), read in full as the editorial standard.
* Repository inspection at `origin/main` `0838ba08` for the current-repository facts the redlines state: `tools/qa/generate_epic_close_pack.py` (blob present; `SOURCE_SCHEMA_VERSION_V2 = "close_candidate_source.v2"`; renders HDE Governance's literal `ADR status line:` field); `schemas/close_candidate_source.v2.json` (present; `tracked_issues` items allow only `id` and `adr_status`, `additionalProperties: false`; `adr_block` and `closure_override` present); `tools/evidence/update_evidence_index.py` (`ADMITTED_CRD_QA` at line 51; `def publish_crd_close_run_family` at line 5222); `audit/qa/hde-crd-0002/close/` (18 tracked files: primaries and path proofs); `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json` (present).

Closure posture: HDE-CRD-0002 is closed (X11, after X13 PASS), so none of its changes is held back on closure grounds. The cross-cutting rules of 2.11, 2.14, 2.18 and 2.31 are Product Owner directions in force and wait on no closure. No selected change is held back.

## 5. Precedence and supersession applied

* PF10 front matter §1 (PF10 authority), §2 (addendum scope), §5 (individual-addendum supersession), §8 (silence) and §9 (operational rule) were applied to the selected addenda.
* 2.18 withdraws the cost ceiling: 2.11 rule 1's ceiling bullet, rule 2's "exceeds its ceiling", rule 3's ceiling clauses and its passing-the-ceiling bullet; 2.14 rule 5 in full; 2.15's projected-ceiling sentence; 2.16's ceiling passages (historical). No ceiling text is carried.
* 2.14 narrows 2.11 rules 7 and 8 for P1 findings: the P1 bullets of R-12 carry 2.14 rules 1 to 4; the below-P1 bullet carries 2.11 rule 7 as written for findings below P1 (2.14 rule 6), with its Product Owner-first rule for declining a security finding.
* 2.17 amends 2.15: C-3's pointer clause is superseded (R-16 carries form (b) only); C-1 is extended by PO-35-13's naming rule (R-17 carries resolution A).
* 2.11's misnumbered internal cross-references (ledger: a PF10 publication fact, LR6-O2) were read by the rule their text describes: the drainage row's "rule 5 disposition" is rule 7 (finding disposition); its "rule 6 trigger" is rule 8 (repeated finding class); rule 7's "(rule 3)" is rule 4 (real inputs); "stays a fix under rule 5" is rule 7. 2.14 cites 2.11 by its published numbers (rules 4, 5, 7, 8), which agree with this reading.
* 2.31 is applied by its published numbering (rules 1 to 10). Its closing reference to a repair narrowing "as rule 5 limits" is read as rule 8, whose text describes the narrowing.
* Inside the revised PF06 text, HDE Build Notes is cited by title only, without addendum, section or version (Change Process Guide §0.2 "Build Notes reference posture"; Technical Writing Best Practices §3 "Canonical ownership" and §9). Other PF documents are routed by title.

## 6. Change and disposition ledger

Dispositions: **REDLINE** (the redline that carries it); **EQUIVALENT** (already represented at the stated PF06 location); **OUT OF TARGET** (another owner, with the destination); **WITHDRAWN** (superseded); **HISTORY** (record, not a rule); **HELD** (none).

### S-CR1 — Specification CR-1 (lines 199–208)

| Item | Disposition |
| :---- | :---- |
| §0.1 "accountable to PF30" | REDLINE R-01 |
| §0.1A CRD lane "PF30 accountability" | REDLINE R-02 |
| §0.1A "controlling work register" (would assert a CRD register once PF30 accountability is removed) | REDLINE R-03 |
| §0.1A lifecycle item 14 "PF09 or PF30 record completion" | REDLINE R-04 |
| §0.1A "PF30 work mapping for PF09 work-item mapping" | REDLINE R-05 |
| §0.1A "HDE CRD Records controls PF30 CRD registration and result tracking" | REDLINE R-06 |
| §1.0 heading "intake, plan, and PF30 registration" | REDLINE R-07 |
| §1.0.3 "a concise initial record in PF30 before implementation begins"; its heading | REDLINE R-08 |
| §1.0.4 "PF30 work mapping"; "PF30 mapping for PF09 mapping" | REDLINE R-09 |
| §1.0.6 "update the existing PF30 CRD record"; its heading | REDLINE R-10, R-11 |
| §0.1A "Specification format authority" (CRD Specifications use HDE CRD Records' record contract and template) and §1.0.2's matching sentence (line 1459) | EQUIVALENT, unchanged: CR-1 does not list them, and the approved Specification uses that format with no PF30 entry ("Format and register posture") |
| §1.1.1 line 1503 ("No extra token, PF20/PF30 record [OMITTED] is added as a native handoff input") | EQUIVALENT: already consistent with HDE Governance §9.1.1 |
| Plan Templates §2A; HDE CRD Records "CRD Plan" wording (§1, §2, §3.2, §4.1, §7) | OUT OF TARGET: T-PF27 and T-PF30.1 |

### A11 — addendum 2.11

| Item | Disposition |
| :---- | :---- |
| Rule 4 (real inputs) and rule 5 (constructed inputs) | REDLINE R-12, "Real input" bullet. Carried because the rule 7 disposition depends on it and no permanent PF home defines it |
| Rule 7 (finding disposition), below P1 | REDLINE R-12, "Findings below P1" bullet |
| Rule 7, the P1 parts | WITHDRAWN for P1 on a real input by 2.14; the surviving P1 rule is R-12's P1 bullets |
| Rule 8 (repeated finding class) | REDLINE R-12, "Repeated finding class" bullet, with 2.14 rule 4's P1 narrowing |
| Scope paragraph: the rules leave Change Process Guide §0.2's CI-budget rules and "There is no five-update circuit breaker" unchanged | EQUIVALENT at §0.2 line 191 (unchanged); restated in R-12 |
| "The rules do not weaken the existing duty to fix a real defect" | REDLINE R-12, "Unchanged duty" |
| Rules 1 to 3 (business case, gates) | OUT OF TARGET: HDE Governance §9.7.7, Plan Templates "Business Case (MUST)" and HDE CRD Records §4.1 (T-PF04, T-PF27, T-PF30.1). Observation, not drafted: PF06 §1.1.11 "Mechanical blockers (planning artifacts)" (line 2399) states an Epic-only Business Case blocker; 2.11's drainage table does not name PF06 for it |
| Rule 1 cost-ceiling bullet; rule 3 ceiling clauses | WITHDRAWN by 2.18 |
| Rule 6 (no emulation of external systems) | OUT OF TARGET: 2.11's drainage table names no PF home; prompt wording belongs to GCFPE-MGMT-10 |
| AGENTS.md real-input reporting row | OUT OF TARGET: landed through #661 (2.12) |
| Prompt wording changes | OUT OF TARGET: GCFPE-MGMT-10 and the Product Owner |
| Findings, causes, cost, timeline, WU-PR-06 effects | HISTORY (T-PF30.1) |

### A14 — addendum 2.14

| Item | Disposition |
| :---- | :---- |
| Rule 1 (scope of a P1) | REDLINE R-12, "P1 findings" (with the nonclaim that the priority is the reviewer's label) |
| Rule 2 (addressed until resolved; what fixed means; typed refusal; thread open; not merge-ready) | REDLINE R-12, "P1 findings" |
| Rule 3 (the one exception; reply; Product Owner first) | REDLINE R-12, "The one P1 exception" |
| Rule 4 (repeated finding class for a P1) | REDLINE R-12, "Repeated finding class" |
| Rule 5 (budget) | WITHDRAWN by 2.18 |
| Rule 6 (unchanged: below-P1 rule 7, security below P1, AGENTS.md, duty to fix a real defect) | REDLINE R-12, "Findings below P1" and "Unchanged duty"; the AGENTS.md rule is OUT OF TARGET |
| PR-35 and PR-40 prompt rows; optional AGENTS.md note | OUT OF TARGET: GCFPE-MGMT-10 and the Product Owner |
| WU-PR-07 CX7-2 and CX7-3 effects | HISTORY |

### A31 — addendum 2.31

| Item | Disposition |
| :---- | :---- |
| Rules 1 to 3 (the gap) | HISTORY and rationale; reflected in R-13's existence |
| Rule 4 (the stage; entries; exit; what it owns; what it never does) | REDLINE R-13 |
| Rules 5 and 6 (Dev, not Ops; an Ops run only packages already-produced artifacts) | REDLINE R-14, with a pointer bullet in R-13. EQUIVALENT support already in §0.2 (Ops task definition; "Ops closeout packaging run (OPS-01)", lines 441–453) and §3.5.2.1 (OPS-02, lines 2997–3010), both unchanged |
| Rule 7 (authority and actor) | REDLINE R-13, "Authority and actor" |
| Rule 8 (close-tooling repair; narrowing a recorded rule; limits) | REDLINE R-13, "Close-tooling repair" |
| Rule 9 (interim operation until a GCFPE Modification installs the stage) | OUT OF TARGET: interim routing; installation is MB-030 with GCFPE-MGMT-10. Not named in 2.31's drainage items |
| Rule 10 (HDE-CRD-0002's first run; B-4) | HISTORY (T-PF30.1) |
| Glow QA Guide §3.1.3; Plan Templates close-mutation-set task template | OUT OF TARGET: T-PF19, T-PF27 |

### A15, A16, A17 with X03 and S-APR

| Item | Disposition |
| :---- | :---- |
| X03 row §3.5.2 and §3.5.2.1: the CRD filename prefix beside `EPIC-NNN` | REDLINE R-15 |
| X03 row §3.5.2 and §3.5.2.1: the v2 writer as the generic producer | REDLINE R-15 |
| X03 row §3.5.2 and §3.5.2.1: the close-run family as the same-run evidence home; 2.15 family path, post-verdict status, single writer, no Epic family | REDLINE R-15 (the family's membership exception to HDE Schemas & Artifacts §8.17 is OUT OF TARGET: T-PF12, T-PF19) |
| X03 row §3.5.4: the v2 report's ADR block from the source's decisions and optional closure override; 2.15 C-1 | REDLINE R-17 |
| 2.17 resolution A (a `TOOLING_BLOCKED` check under a closure override) into §3.5.4 | REDLINE R-17 |
| 2.17 resolution B (form (b) only) into §3.5.2.1; 2.16 LR7-O9; 2.15 C-3 as amended | REDLINE R-16 |
| The CRD close report as the ADR block's location (2.15 C-1 applies the block to a CRD close) | REDLINE R-17 |
| S-APR, S21 canon impact: Change Process Guide §3.5.2 (close pack) | REDLINE R-14, R-15, R-16 |
| S-APR, QA requirement (Change Process Guide §0.1A and §1.0.6) and production-affecting Live QA minimum (§1.1.5A) | EQUIVALENT: §1.0.6 first paragraph (line 1477, unchanged by R-10/R-11) and §1.1.5A (lines 1832–1881) |
| S-APR, S14 drainage; operative documentation (AGENTS.md) | OUT OF TARGET: T-PF05, T-PF29; the Product Owner |
| Delta 01 C-8 to C-12 | No PF06 effect (§4 SR3) |
| 2.15 approval, status line, C-2 (current approved Specification), C-4 (ADR text), validation; 2.16 lineage record; 2.17 rules 1 and 2 and its ADR-revision row | HISTORY or OUT OF TARGET (the ADR is the Product Owner's; HDE Schemas & Artifacts, HDE Governance and HDE Mechanics Guide rows go to T-PF12, T-PF04, T-PF14) |
| X03 rows for HDE Schemas & Artifacts, Glow QA Guide, HDE Mechanics Guide and HDE Governance | OUT OF TARGET: T-PF12, T-PF19, T-PF14, T-PF04 |

## 7. Redline summary

Offsets are byte offsets into the baseline, end exclusive; the OLD block of each is one or more complete lines.

| ID | Location | Lines | Offsets | OLD bytes | NEW bytes | Rows | Type |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| R-01 | §0.1 | 17 | 287–1109 | 822 | 933 | S-CR1 | CONSISTENCY |
| R-02 | §0.1A CRD lane bullet | 26 | 1554–1780 | 226 | 324 | S-CR1 | CONSISTENCY |
| R-03 | §0.1A lanes paragraph | 28 | 1782–2152 | 370 | 488 | S-CR1 | CONSISTENCY |
| R-04 | §0.1A lifecycle item 14 | 45 | 2682–2740 | 58 | 183 | S-CR1 | CONSISTENCY |
| R-05 | §0.1A reuse paragraph | 47 | 2742–3084 | 342 | 458 | S-CR1 | CONSISTENCY |
| R-06 | §0.1A authority routing | 57 | 3730–3805 | 75 | 280 | S-CR1 | CONSISTENCY |
| R-07 | §1.0 heading | 1429 | 150050–150105 | 55 | 55 | S-CR1 | CONSISTENCY |
| R-08 | §1.0.3 heading and paragraph | 1461–1463 | 151332–151714 | 382 | 655 | S-CR1 | CONSISTENCY |
| R-09 | §1.0.4 second paragraph | 1469 | 152149–152615 | 466 | 628 | S-CR1 | CONSISTENCY |
| R-10 | §1.0.6 heading | 1475 | 153052–153102 | 50 | 29 | S-CR1 | CONSISTENCY |
| R-11 | §1.0.6 third paragraph | 1481 | 153849–154101 | 252 | 577 | S-CR1 | CONSISTENCY |
| R-12 | §1.1.4 after the QoS stop-rule | 1684 | 172704–173035 | 331 | 3,972 | A11, A14 | NEW_CANON |
| R-13 | §3.5.1 after the close-mutation-set paragraph | 2943 | 290272–290425 | 153 | 2,725 | A31 | NEW_CANON |
| R-14 | §3.5.2 under its heading | 2967 | 292896–292927 | 31 | 568 | A31 | NEW_CANON |
| R-15 | §3.5.2.1 close-pack filenames | 2971–2976 | 292964–293164 | 200 | 1,233 | A15, A16, X03, S-APR | CANON_UPDATE |
| R-16 | §3.5.2.1 tracked-issue bullet | 2983 | 293865–294209 | 344 | 690 | A17, A16, A15 | CANON_UPDATE |
| R-17 | §3.5.4 before and at "Location." | 3318–3320 | 323443–323528 | 85 | 1,130 | A15, A17, A16, X03 | CANON_UPDATE |

Sizes are UTF-8 bytes (`§` is two bytes). Three redlines reproduce their OLD line unchanged at the start of the NEW block and add text after it (R-12, R-13, R-14); R-15 and R-17 reproduce their unchanged baseline lines inside the NEW block. This gives exact original-bound placement without an `INSERT` gap. No redline touches a document-control field.

## 8. Producer validation

The batch was validated twice against the unchanged baseline, by two separate scripts run in the session scratchpad under Python 3 (`-I`):

1. The generator built each OLD block from exact baseline lines and each NEW block from those exact bytes plus authored text, and asserted per redline: OLD occurs exactly once; OLD starts at a line start and ends before an LF; NEW differs from OLD; NEW adds no ellipsis; no five-backtick fence occurs inside a payload. It asserted that the 17 spans are pairwise disjoint and not adjacent (each gap is at least one byte).
2. An independent parser read only the saved redlines file. It required the `END OF REDLINES` sentinel, extracted each section's Operation, expected count and fenced OLD and NEW literals, and re-checked: operation `REPLACE`; expected 1 and observed 1 for every OLD block; complete-line spans; non-empty NEW different from OLD; pairwise disjoint, non-touching spans. It also checked that each stated byte offset pair slices the raw baseline bytes to exactly that redline's OLD block. It then simulated one-pass application in descending offset order, with no rematching on changed text, and proved preservation by rebuilding the expected stream from the untouched baseline intervals and the payloads, and by checking every untouched interval at its predicted output offset.

| Check | Result |
| :---- | :---- |
| Expected and observed occurrences | 1 and 1 for all 17 |
| Complete-line OLD blocks | 17 of 17 |
| Overlap, touching spans, shared gaps | None |
| Simulated content-only output | 439,439 bytes; 4,684 LF; SHA-256 `3d3f23e61f0ab4f52d454bf1260ba71f79a434ce06e763489cfe8f44d5f7a09d`; no CR; ends with two LF, as the baseline does |
| Untouched baseline bytes preserved | 424,511 of 428,753 (the 17 OLD spans total 4,242 bytes) |
| Ellipsis in the redlines file (three full stops or U+2026) | 0 and 0 |
| Draft, TODO, FIXME or editorial markers in PF06 needing hygiene | None found. "Draft" occurs only as a verb and in the template name "Asset Draft Pack"; "ISSUE-XXX" and the angle-bracket and backslash placeholders are template content that canon keeps |

The simulated output is a validation artifact in the scratchpad only. It omits the document-control derivation, which belongs to TW-APPLY-10.

Correction record (the preparer's own, before READY): after the first read-back of the saved file, three defects were corrected and the whole batch was regenerated and revalidated with both scripts. (1) R-14's source rows named A16, but its content rests on 2.31 alone. (2) R-15's source rows named 2.17's resolutions and ADR Decision item 9, which belong to R-16 and R-17. (3) R-13's first sentence was reworded for clarity ("produced by its own stage of the change flow"). No locator, span or other payload changed. A fourth defect was found while writing this log: the first two generated files gave character offsets under the label "byte offsets", which differ from byte offsets after line 57 because the baseline holds multi-byte characters. The generator now computes byte offsets, the parser checks that each stated pair slices the raw baseline to the OLD block, and the whole batch was regenerated and revalidated. Only the stated offsets of R-07 to R-17 changed; every OLD and NEW literal is byte-identical to the previous generation, as the unchanged SHA-256 of the simulated output (`3d3f23e61f0ab4f52d454bf1260ba71f79a434ce06e763489cfe8f44d5f7a09d`) shows.

## 9. Header provenance for TW-APPLY-10

* Sources that justified the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` (PF10 v13.8.8; gate token `BN 13.8.8`), for R-12 to R-17; `HDE-CRD-0002-specification-v1.1-approved.md`, for R-01 to R-11 (CR-1) and R-14 to R-16 (S-APR). Delta 01 was read as the overlay in force and justified no change. The ADR (X03), HDE Governance and Technical Writing Best Practices were supporting reading, not sources.
* Expected Last Update Gate: `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md`.
* Baseline control values: Version `v2.5.4`; Effective date `2026-10-09`; Last Update Gate `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md`; Status `Canon` (the target's classification; not stale); Title and Invocation tag protected.
* No change-history entry is owed (§2).

## 10. Constraints, assumptions and interpretations

* The new stage is named functionally ("the close-mutation-set stage"), and the closure decision, the final QA Report and the review chain are named by function, because PF06 names no GCFPE prompt codes and Technical Writing Best Practices §2 asks for functional terms. Canonical values are kept exactly: `PASS`, `DO_NOT_CLOSE`, `SATISFIED`, `TOOLING_BLOCKED`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `PARKED`, `ADR status line:`.
* 2.14 rule 1's "by the Codex code review or by a person" is written "from the automated code review in the review chain or from a person" (PF06 §0.3: a product label denotes a function, not a provider mandate).
* 2.11 rule 7's standing default "a breach of the read-only or no-secrets guarantees" (from WU-PR-06) is written in its general form, "a breach of a read-only or no-secrets guarantee"; the WU-PR-06 disposition IDs are not carried.
* The §1.0, §1.0.3 and §1.0.6 headings are retitled because CR-1 names those sections and their headings would otherwise state the PF30 registration and result update that the alignment removes. Section numbers are unchanged; no PF06 text cross-references those headings (searched for `§1.0`).
* R-06 keeps HDE CRD Records' role as the owner of the CRD record contract and template used as the CRD Specification format, because §0.1A "Specification format authority" (not in CR-1) and the approved Specification rely on it.
* PF06 now states the HDE Governance §9.1.1 historical-drainage permission (R-04, R-08, R-11). Whether a record is actually made is T-PF30.1's separate authorization.
* Current-repository statements (the writer path, the v2 schema name, the close-run family path, form (b) only, the single writer) were verified on `main` (§4). They state checked-in bytes only, not runtime behavior.

## 11. Outside dependencies, observations and unresolved items

* Blocking dependencies: none. Unresolved selected changes: none. Held items touched: none (H-01 to H-06 concern HDE Math Spec, PO-2, CLI/API/Vendor Ref, Glow Infrastructure and HDE Governance §9.1.1's review-chain entry; none is in PF06's assigned scope).
* Observations, not drafted because no assigned row authorizes them:
  * §1.1.11 line 2399 states an Epic-only Business Case blocker; 2.11 extends the business case to every requirement and work unit but routes it to HDE Governance and Plan Templates.
  * §1.1.2 line 1532 ("archived in PF20 only at epic close") and §3.5.1 line 2939 (HDE Phased Epics at epic close) concern the Epic lane's PF20 history, which CR-1 does not cover.
  * §0.5.1 "Close-pack filenames (canonical)" (lines 966–990) lists Epic filenames only; the ADR canon table does not name §0.5.1.
  * §3.5.4's heading reads "(all epics)" although R-17 now covers a CRD close; the heading is protected and no source names it.
  * The §0.4 heading reads "0.4 4 Execution posture and flow (route-aware)" (line 507).
  * Several baseline literals carry escaped, emptied placeholders, for example `audit/EPIC-\\\_close\_report.md`; they are preserved byte-exact.
  * ADR line 67 still carries the clause that 2.17 resolution A supersedes, and ADR line 7 cites "addendum 2.31 rule 5" for the narrowing that the published 2.31 numbers rule 8. The ADR is the Product Owner's (2.17 drainage row).

## 12. Next step

TW-APPLY-10 — Apply Validated Redlines — 100926.1, in this session as the handoff authorizes, with: the original baseline above; this redlines file and proof log; ledger rows S-CR1, A11, A14, A31, A15, A16, A17, X03 and S-APR (task T-PF06); the selected source boundaries in §4; branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`; outputs `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf06/PF06-from-v2.5.4.md` and `PF06-from-v2.5.4.proof-log.md`, or on failure `apply-diagnostic-PF06-from-v2.5.4.md`.

## 13. PF titles and sections relied on

HDE Build Notes (front matter §1, §2, §5, §8, §9; addenda 2.11, 2.14, 2.15, 2.16, 2.17, 2.18 and 2.31); Change Process Guide (the whole target; in particular §0.1, §0.1A, §0.2 "Build Notes reference posture" and the CI-budget and Ops rules, §0.3, §1.0 to §1.0.6, §1.1.4, §1.1.11, §3.5.1, §3.5.2, §3.5.2.1, §3.5.4); HDE Governance §9.1, §9.1.1 and §9.1.2; Technical Writing Best Practices §2, §3, §5, §7, §8, §9, §11 and §14.

## 14. Save-verification receipt

* `redlines-PF06-from-v2.5.4.md`: saved at the path in §1; read back completely (474 lines, 37,868 bytes, ending with `END OF REDLINES`); SHA-256 `27a3215d0f00e15cd9a8f2cb1c9ece204096a3c51ff6e3497b57f2e3b1e8ebd3`, equal to the generated file the independent parser validated (§8).
* This proof log: read back completely (253 lines, 30,058 bytes) before this receipt was added. The receipt and the §1 save-completeness value were then added, and the change was verified as exactly those two edits by a byte diff against the read-back copy. The log does not carry its own hash.
* Package state: `READY`, `COMPLETE_PACKAGE`.
