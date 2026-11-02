# Proof log: PF27-Canon-Plan-Templates v2.0.6 redlines, run gtwpe-20261101-pf10-v14-0-5 (task T-07)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-07/prep-r1` (first preparation of T-07; no earlier T-07 output existed on the branch) |
| Originating preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step (page last edited 2026-10-09T11:05:22Z), run in the Claude Code cloud session https://claude.ai/code/session_01Q789tyeqMDbVqbUtqxA64b, which Nathan started for T-07 on 2026-11-02. No subagent, reviewer or other session took part. |
| Authorized step sequence | Nathan's handoff authorizes TW-DRAIN-10, then TW-APPLY-10 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) in this same session after a READY / COMPLETE_PACKAGE result, and a return to TW-DRAIN-10 if Apply returns a diagnostic. |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §12 after both files were read back. |
| Correction route | An Apply diagnostic returns to this preparer, in this session, under a distinguishable revision identity (`prep-r2` and later). |

## 2. Inputs and source roles

| Input | Identity | Role |
| :---- | :---- | :---- |
| Target (original) | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.6.md`; in-document title `PF27-Canon-Plan-Templates`; version v2.0.6; Status Canon; Effective date 2026-10-26; git blob `c21096d78b9865bf5aa0c531eee701e462d71a50`; SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00` over the whole blob; 323,765 bytes; 3,938 lines; LF endings | The one current PF27 Markdown under `docs/pfcanon/` on `main`. Baseline `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. On 2026-11-02 `origin/main` was `84d6d1cf`; its two later commits (amthorn78/glow-hdengine-v2#824 and amthorn78/glow-hdengine-v2#825) touch only `docs/ephemeral/HDE-M10V2-*` files and leave PF27 and PF10 byte-identical (same blobs). |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5, effective 2026.11.01; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines | The only substantive change source. One unlettered logical version. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`; blob `504712df548a02f3aa4e7b8c37027385e46a3878`; SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`; 633 lines | Read in full (lines 1–633). Applied to authored wording only; not a change source. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-07; rows C-02, C-08, C-09, C-26; supporting C-06; holds H-06 and H-07 | Routing and provenance only. Not a change source and not a Last Update Gate. The target and the selected units agree with the handoff. |
| Supporting canon (read, not drained) | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` (blob `0c3ce100f942`), §3.4 "Open rails (controlled)", lines 1171–1243, read in full; `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` (blob `53e6a9028dfa`), §7.1.10 "Endpoint policy (explicit version-gated dual lineage)", lines 3472–3504, read in full | Ownership checks for the routing sentences in RL-03 and RL-06. Neither is edited. |
| Handoff | Nathan's inline handoff of 2026-11-02 ("GTWPE document session — T-07 — Plan Templates (drain, then apply)") | Control instructions: target, selected units, holds, branch, outputs, the decision to drain 2.2 R-3 as written. |

## 3. Coverage

Target. Read completely, lines 1–3938, in twelve recorded windows (line range, bytes): 1–300 (28,897); 301–600 (22,102); 601–900 (33,849); 901–1060 (20,092); 1061–1200 (39,350); 1201–1385 (27,843); 1385–1599 (22,612); 1600–1899 (22,292); 1900–2269 (29,228); 2266–2705 (19,284); 2706–3225 (19,933); 3226–3938 (38,388). The windows overlap at lines 1385 and 2266–2269 and leave no gap. Every window ended at a complete line; the last ends at the file's final LF.

Selected source units, each read completely (PF10 lines, bytes):

| Unit | Lines | Row |
| :---- | :---- | :---- |
| 2.1 heading, timestamp, "Decision and approval status" | 205–224 | C-06 |
| 2.1 D-1 (read in passing; not selected) | 225–276 | none (C-01, not T-07) |
| 2.1 D-2 | 277–344 (with 205–224: 13,633 bytes for 205–344) | C-02 |
| 2.1 "Scope, exclusions and nonclaims", "Dependencies and unresolved obligations", "Evidence" | 491–516 | C-06 |
| 2.2 heading, "Decision and approval status", "The defect that prompted it", R-1, R-2 | 517–546 | C-08 (R-1 is C-07, see §5) |
| 2.2 R-3 | 547–551 (491–551: 7,237 bytes) | C-09 |
| 2.15 heading to R-6 | 1650–1804 (11,087 bytes) | C-26 |

Supporting reading, labeled as such and not drained: 2.2 lines 552–588 (6,048 bytes: changes delivered, nonconforming items, scope, dependencies; line 581 names the Plan Templates drainage targets); 2.5 lines 765–780 and line 856 (R-3 governs as written; CCR-5 and its alternatives); 2.9 lines 1150–1170 (line 1161: the CCR-5 ruling bounded to HDE-EPIC041); 2.15 lines 1805–1868 (4,159 bytes: HDE-EPIC041 disposition, nonconforming items, scope with the CRD exclusion at lines 1825 and 1835, and the drainage target list at lines 1845–1849); 2.16 R-3, lines 1936–1950. No unrelated addendum was read to rebuild triage.

Coverage state: complete for the target and for every selected unit.

## 4. Redlines prepared

Six `REPLACE` operations, each on one unique original line, in original order.

| Redline | Row | Target location (original line) | What it does | Source basis |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | C-08 | "Purpose & scope" > "Canon precedence for template use" (287) | Adds R-2's premise that PF versions and file names may change; keeps the title-only rule for HDE Build Notes and adds its reason; requires other PF references by current title, section where needed, never file name or version; applies the rules to an ADR a derived artifact carries; keeps the provenance sentence and states that a derived artifact that must remain valid pins no PF file name, version or digest. | 2.2 R-2 bullets 1, 2 and 4 (lines 542, 543, 545); target named at line 581 ("R-2 citations") |
| RL-02 | C-26 | §1 "Live QA Plan" > "Front matter" (326) | Adds the template field `Live test:` with the values RAN, WAIVED and MISSING after the Operators line, using allowed `<PLACEHOLDER>` markers for the evidence references and for the Product Owner's quoted words and date. | 2.15 R-4, lines 1763–1771 |
| RL-03 | C-26 | §1 "Live QA Plan" > "Open-Rails Live QA Requirement for production-affecting epics" (389, its last line) | Appends a new H3 "Live compat test for every Epic (required)": R-1's universal live compat test (live vendor compat and deployed-service check, pass predicates, findings, SYN-A and SYN-B, the own-surfaces step, what does not satisfy it), the CRD scope boundary, routing of execution controls to HDE Governance §3.4, R-4's live-test line for the plan and its review with the approval block and override rule, and R-3's naming rule. | 2.15 "Relation to other canon" (1666–1681), R-1 (1704–1739), R-3 (1755–1759), R-4 (1761–1784); supporting 1825, 1835; target at 1849 |
| RL-04 | C-26 | §1 "Live QA Plan" > "Close-out deliverables" > "What “QA RCA & Doc Delta summary” means" (973) | Adds a content bullet: the summary carries the live-test line and, with MISSING, gives no PASS verdict. | 2.15 R-4, line 1769 and table row line 1780 |
| RL-05 | C-09 | "Review guardrails" > "CI lane classification and automated budget-control discipline" (1312) | Adds R-3 as written as a new paragraph after the administrative-closeout paragraph. | 2.2 R-3, lines 549–550; target at line 581 |
| RL-06 | C-02 | §2 "HDE-EPIC-Specification" > "Epic Record Template (Normative)" > "Contract and Compatibility Posture (MUST)" (1459) | Keeps the four categories and adds that "explicit legacy fallback" reads as the terminal-v1 legacy selection, which is not a fallback, and routes route selection and the configured-base boundary to HDE CLI/API/Vendor Ref §7.1.10. | 2.1 D-2, line 316 (supersession), line 323 (drainage target); lines 288–289 |

Change-type classification (report labels only): RL-01 CANON_UPDATE with CONSISTENCY; RL-02, RL-03, RL-04 and RL-05 NEW_CANON; RL-06 CLARIFY. No DOC_HYGIENE or DELETION redline is prepared.

## 5. Change and disposition ledger

Every change in the selected units, with its disposition. "Not PF27" means the change belongs to another target or owner and is not repeated here.

**2.1 D-2 (C-02), lines 277–344**

| Element | Disposition |
| :---- | :---- |
| "What governs", "Selection", "The base", "No fallback" (281–289) | Owned by HDE CLI/API/Vendor Ref §7.1.10 (supporting reading confirms §7.1.10 already states the selection, the configured-base boundary and "retained legacy selection, not fallback"). Not PF27; RL-06 routes to the owner. |
| "The v1 path is retained legacy selection, not fallback" (288) | Represented in RL-06 ("It is not a fallback and makes no fallback claim"). |
| Fit with HDE Mechanics Guide §1.1 (290–297) | Not PF27 (T-05). PF27's "Exact technical facts and secret safety" rows (lines 110–113) were checked: they forbid `/v1` and `/v2` as route-construction inputs and auth selection by string inspection, consistent with D-2. No change. |
| Classification label `explicit_legacy_fallback` (298) | Not routed to PF27. RL-06 keeps the PF27 category name, matching D-2's choice to keep the label unchanged. |
| Basis (300–308) | Explanatory. No change. |
| Supersession of HDE Mechanics Guide, HDE Users Guide, HDE CLI/API/Vendor Ref (312–315) | Not PF27 (T-05, T-08, T-02). |
| Plan Templates "bg:resolve --source vendor route-policy posture" (316) | Actionable: RL-06. |
| Drainage targets (320–324) | PF27's target (323): RL-06. AGENTS.md (324): H-05, not a PF target. |
| Consequences for tests and evidence (328–339) | Not PF27. No change. |
| Left undecided: v1 retirement (343) | Unresolved by source; RL-06 says nothing about retirement. |

**2.1 context (C-06), lines 205–224 and 491–516**: supporting. D-2 takes effect as canon on publication (line 211), so RL-06 does not wait for Candidate CRD Items List item 9 (H-10). RL-06 states the category's meaning and routes to the owner; it makes no implementation-state claim, so the open implementing change does not block it. The scope, nonclaims and evidence are not drained.

**2.2 (C-08, C-09), lines 517–551**

| Element | Disposition |
| :---- | :---- |
| Heading, timestamp, decision (517–523) | Context. |
| "Status. Proposed." (524) | Not drained. v14.0.5 publishes the addendum, so its rules are active (ledger §2 status reading). |
| Relation to other canon (525) | Context. It names HDE Governance, HDE Schemas & Artifacts, Change Process Guide, Glow QA Guide and HDE Mechanics Guide; Plan Templates is not among them. |
| The defect that prompted it (527–531) | History. No change. |
| R-1 (533–538) | Row C-07, routed to T-01 (and, uncertain, T-03 to T-06), not to T-07. Line 525 does not list Plan Templates and line 581 names Plan Templates only for R-2 citations and R-3. No PF27 change. |
| R-2 bullet 1, versions may change (542) | RL-01. |
| R-2 bullet 2, no pin (543) | RL-01, as the consistency qualifier for the retained provenance sentence. |
| R-2 bullet 3, tool resolution at run time; validation does not re-read canon (544) | Tool behavior. Its drainage targets are HDE Governance §9.1.2 and §9.1.3 (line 581, T-01). Not PF27. |
| R-2 bullet 4, citations (545) | RL-01. Already represented in part at line 287 (title-only HDE Build Notes; current title and section); the reason, the never-by-file-name-or-version rule and the ADR scope are added. |
| R-3 (547–551) | RL-05, as written. Its own parenthetical citation of this PF27 section is not repeated inside that section. |

**2.15 (C-26), lines 1650–1804**

| Element | Disposition |
| :---- | :---- |
| Heading, timestamp, decision (1650–1664) | Context. The Product Owner's quoted direction is not drained. |
| "Status. Proposed." (1665) | Not drained (ledger §2 status reading). |
| Relation to other canon (1666–1681) | Applied in RL-03: the live compat test "does not depend on a finding that the Epic touches or can affect a production surface". The controls it preserves are routed to HDE Governance §3.4 in RL-03. |
| The failure that prompted it (1683–1702) | History of HDE-EPIC041. Not drained into PF27 (ledger C-27 and T-10 carry Epic history). |
| R-1 scope and why (1704–1707) | RL-03, first paragraph. |
| R-1 live vendor compat, pairs, pass predicates (1708–1716) | RL-03, first check bullet. |
| R-1 deployed-service check and findings (1717–1725) | RL-03, second check bullet. |
| R-1 own surfaces (1726) | RL-03. The existing Open-Rails subsection (lines 363–389) stays as the template's statement of HDE Governance §3.4 for those surfaces. |
| R-1 what does not satisfy it (1727–1734) | RL-03. |
| R-1 SYN-A and SYN-B (1735–1739) | RL-03, with UUIDs, derivations, birth data, the write path and authorization, and the TOOLING_BLOCKED rule. The Ops task that stores them (HDE-EPIC041-POSTCLOSE-OPS01 Part W) is history and is not named in the template. |
| R-2 (1741–1753) | Not PF27's share: 2.15's drainage list (1846) sends R-2 to HDE Governance §3.4 (T-01). RL-03 carries only R-4's override sentence ("only the Product Owner may waive this requirement, or any part of it") and R-3's reference to "a recorded Product Owner waiver". |
| R-3 (1755–1759) | RL-03, "Use of the name "Live QA"". |
| R-4 live-test line (1763–1771) | RL-02 (plan field), RL-03 (plan and review), RL-04 (QA RCA & Doc Delta summary). The other records R-4 names have PF27 homes outside §1 or none; see O-1. |
| R-4 table (1774–1782) | QA plan and plan review rows: RL-03. Final QA report row: RL-04. Other rows: O-1. |
| R-4 "Who may override" (1784) | RL-03. |
| R-4 prompts (1785) | Prompt instruction, not template text. Owner GCFPE management (H-11). Not drained. |
| R-5 (1787–1790) | Not PF27's share (1846: HDE Governance §3.4). RL-03 keeps only R-1's own sentence that a missing SYN person makes the deployed check TOOLING_BLOCKED. |
| R-6 (1792–1803) | Not PF27's share; a restatement of HDE Governance §3.4 controls. RL-03 routes execution and controls to HDE Governance §3.4, as 2.15's scope (1835) does. |

**Supporting units**: 2.9 line 1161 records the CCR-5 "(B) now, bounded" ruling for HDE-EPIC041 only; it is history and is not drained as a general rule. 2.16 R-3 (1940–1948) records that SYN-A and SYN-B are stored and registered; RL-03 states the requirement and the missing-fixture rule and makes no claim about current storage.

## 6. Held items, not drafted

| Hold | What is held | What it waits for |
| :---- | :---- | :---- |
| H-06, CCR-5 | Alternative (A) drain of §3B "Entries and exit (normative)" (target lines 2224–2228). §3B is unchanged. | The Product Owner's ruling between CCR-5 alternatives (A) and (B), which 2.5 line 856 offers. The correcting HDE Build Notes addendum is the Product Owner's (2.9 line 1161; 2.10 line 1298, item P-1). |
| H-07, CCR-1 / P-2 | Spec Preflight B "Close-pack baseline declared (planning gate)", which lists the acceptance map (target lines 1733–1749). Unchanged. | The Product Owner's decision whether a tokenless Epic needs an acceptance map (2.10 line 1299). No source text exists to drain. |

## 7. Outside dependencies

None blocks this package.

* The concurrent T-01 (HDE Governance), T-03 (Change Process Guide) and T-06 (Glow QA Guide) drains of 2.15 are not inputs. RL-03 cites HDE Governance §3.4 for the existing open-rails requirement and execution controls, which §3.4 already states in v2.8.8 (lines 1192–1206).
* Candidate CRD Items List item 9 (H-10) is open. RL-06 does not depend on its delivery (see §5, C-06).

## 8. Constraints, assumptions and interpretations

* Redline format. TW-DRAIN-10 requires literal fenced payloads; PF03 §8 says "When the operator supplies a redline format, follow it exactly", so its no-fence default does not apply to this redlines file. No fence enters PF27.
* New heading style. RL-03's heading has no outer bold, as PF03 §8 "Structure and presentation" requires. Most PF27 headings are bold-wrapped; §3B's are not. PF27's review guardrails treat heading styling as non-material.
* Placeholders. The existing Live QA Plan template placeholders are kept unchanged, as the handoff requires. RL-02 adds only allowed `<PLACEHOLDER>` markers ("Template-safe placeholders and omission syntax").
* RL-03 placement. The new H3 follows the last line of the Open-Rails subsection (line 389) and precedes its `---` rule, so no existing heading, title or order changes. Line 389 belongs logically to the empty H4 "PF10 overrides / conflicts (if any)" at line 361, which the Open-Rails H3 at line 363 separates from its content; that pre-existing structure is unchanged (O-7).
* RL-04 mapping. R-4 names "the final QA report and RCA". This template's QA RCA & Doc Delta summary is the closure-oriented summary that states what Live QA found and gives the readiness / closeout recommendation, so RL-04 places R-4's line and effect there. R-3's first-line rule is stated once, in RL-03, because the summary may live as a section of the close report.
* CRD boundary. 2.15 excludes CRDs (1835) and leaves to the Product Owner whether a runtime-changing CRD runs the R-1 test (1825). PF27's CRD profile reuses this template with CRD substituted for Epic, so RL-03 states that reuse for a CRD does not by itself apply these rules.
* RL-05 and §3B. R-3's first bullet places the close-pack write after the closure decision; §3B "Entries and exit" places the close mutation set before it. That is CCR-5. Under PF10's precedence rule R-3 governs as written (2.5 line 772), and the handoff directs draining it as written. After application PF27 states both rules until the Product Owner's CCR-5 ruling resolves H-06 (O-3).
* RL-06 wording. D-2 says the category "reads as" the terminal-v1 legacy selection and keeps the matching evidence label unchanged, so the category keeps its name and gains its reading. The other "fallback" phrases in §2 (lines 1458, 1462 and 1470) ask a plan to state what fallback remains; D-2 names only the route-policy bullet for Plan Templates, and those prompts stay valid (O-6).
* Citation form. New text names other PF documents by their in-document titles (`PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`) with a section, and HDE Build Notes is not cited by addendum, consistent with PF03 §3 "Canonical ownership" and with RL-01.
* Not a current-state claim. No redline states current repository, deployment or QA state.

## 9. Observations for Nathan (not drafted; outside the assigned selection)

* O-1. R-4 also names QA readiness, the QA task set, the QA execution result, the QA evidence review, the close mutation set result and the closure decision. PF27 templates that may carry some of these lie outside §1: §3B "Record fields (required)", §8 "QA Pass Review Record", §9 "Final QA Closeout Review + QA RCA" and §10 "Epic Closure Review + Retrospective". 2.15's drainage list (1849) names only §1 for Plan Templates, and HDE Build Notes governs those templates meanwhile.
* O-2. §2 "Contract and Compatibility Posture (MUST)" bullets "Open-rails QA declaration", "Implementation preservation" and "Review posture" (lines 1450, 1452, 1453) keep the touches-a-production-surface dependency that 2.15 supersedes for the scopes R-1 to R-4 address. They are not a named drainage target.
* O-3. RL-05 and §3B state different orderings of the close-pack write and the closure decision until CCR-5 is ruled (H-06).
* O-4. R-4 gives a plan the values RAN (with evidence references), WAIVED or MISSING. It does not say which value a plan carries for a live test it includes but has not yet run. RL-02 and RL-03 reproduce the rule as written.
* O-5. "Review guardrails" > "Explicit non-blockers" repeats one bullet at lines 1199 and 1200. Removing it needs a source or Nathan's authorization; it is not a placeholder or drafting marker. Unchanged.
* O-6. See §8, RL-06 wording.
* O-7. See §8, RL-03 placement.

## 10. Producer validation

Method: a script built every OLD block from the unchanged original by line number, built every NEW block from its OLD block, and checked the batch before the file was written. A second, independent parser then read the saved redlines file, extracted each fenced block, and repeated the checks against the original.

| Check | Result |
| :---- | :---- |
| Operation dialect | Six `REPLACE`; no `FIND_AND_REPLACE`, so the RL-045 count rule does not arise |
| OLD occurrence, expected / observed | 1 / 1 for each of RL-01 to RL-06 |
| OLD alignment | Each OLD starts at a line start and is followed by the original LF; each is the whole stated line |
| Stated line equals resolved line | 287, 326, 389, 973, 1312, 1459 |
| Spans (character offsets) | RL-01 27086–27420; RL-02 30064–30143; RL-03 35357–35434; RL-04 88968–89193; RL-05 161547–162110; RL-06 180321–180705 |
| Overlap, shared boundary, insertion in a replaced span, redline anchored on another's output | None |
| Payload hygiene | No U+2026, no three-period sequence, no fence, no CR in any NEW block |
| Saved-file round trip | Every fenced block in the saved file matches its stated SHA-256 and byte length, and re-resolves to count 1 in the original |
| One-pass simulation | Applying all six against the original, in descending offset order, gives 329,151 bytes and 3,970 lines (SHA-256 `37d404892bda68f5d5577f2d222c531a9e77ccd6580332d2f0bb06952d215596`). Each NEW block occurs exactly once in the result. This simulation changes no header field; TW-APPLY-10 derives the document-control fields. |

The validation scripts ran in the session scratchpad and are not committed.

## 11. Header provenance for TW-APPLY-10

* Baseline header schema (lines 1–15), in order: `# **0\) Document Control**`, `## **Header**`, then `**Title:**` PF27-Canon-Plan-Templates; `**Version:**` v2.0.6; `**Status:**` Canon; `**Effective date:**` 2026-10-26; `**Last Update Gate:**` BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-QA70-qa-plan-review-v1.0.md; `**Invocation tag:**` INV-f2ac55d77ce9aacc. Each field is its own paragraph.
* Sources that justify this update, in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5. It is the only source.
* Internal restatements of the document's own version or date outside the header: none (a search for `2.0.6` and `2026-10-26` finds only header lines 7 and 11).
* Change log or revision history: the target has none, and none is prepared.
* Status language and drafting markers: Status is Canon, not stale. A search for TODO, FIXME, `???`, TBD, draft-status wording and editorial notes found only template rules and template fields, which canon requires; no hygiene redline is needed.
* No redline touches the header.

## 12. Save verification receipt

Written after both files were saved in the working tree and read back from disk, on 2026-11-02.

| File | Verification |
| :---- | :---- |
| Redlines file | Read back from disk: 21,864 bytes, 226 lines, SHA-256 `0bb360b2fa126207207216a4b48f3fb42da211cd78ba487a243868a3b64ce15f`, ending with the line `END OF REDLINES` and a final LF. The independent parser re-validated the saved bytes: six redlines, each block matching its stated hash and length, each OLD at count 1, no overlap, and a one-pass result byte-identical to the simulation in §10. |
| This proof log | Read back in full (sections 1 to 11) before this receipt was added, then read back again after it was added. |

Save completeness: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. The package is ready for TW-APPLY-10 with the unchanged original, these two files, ledger rows C-02, C-08, C-09 and C-26, the selected source units in §3, branch `claude/gtwpe-triage-authoring-j94ewf`, final-output directory `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/` and diagnostic path `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`. The commit that holds the pair is given in the ledger row and the session's final response.
