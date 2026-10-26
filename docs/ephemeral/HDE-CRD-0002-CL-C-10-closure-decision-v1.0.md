---
artifact_type: CHANGE_CLOSURE_DECISION
artifact_title: CRD Retrospective and Closure Decision
artifact_version: "1.0"
logical_id: HDE-CRD-0002-CL-C-10-CHANGE-CLOSURE-DECISION
predecessor: none (the first closure decision for HDE-CRD-0002)
change_id: HDE-CRD-0002
change_class: CRD
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
producing_prompt: CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1
producing_prompt_url: https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022
prompt_page_state: 2026-10-12T02:29:13.994Z (read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decision_owner: Isis (Isis-53), continuing Lead Developer and terminal closure authority for HDE-CRD-0002
decision_session: https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (the continuing Isis session the QA-120 handoff names)
decision_time: 2026-10-26T01:15:16Z
decision: DO_NOT_CLOSE
state: CLOSURE_RETURNED_FOR_CLOSE_MUTATION_SET
return_work: §8 (HDE-CRD-0002's close mutation set, as approved Implementation Plan v1.1 §9 item 5 and §7 WU-PR-07 "Terminal-state reachability" define it)
next: terminal return to the Product Owner (§9). The close mutation set needs the Product Owner's authorization (Plan WU-PR-07 T0) and a vehicle, and release 100926.1 names no prompt that runs it. No continuation block is emitted
QA_REPORT_ID: HDE-CRD-0002-QA120-QA-REPORT v1.0, docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md (verdict PASS; blob d6cceaf3a019; SHA-256 f31e2e077300ead2a7b89a84dda31fc235f3c28ae2d90f8c9b886f4f0fb09973)
QA_RCA_ID: HDE-CRD-0002-QA120-QA-RCA v1.0, docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md (run_verdict PASS; blob bef1ca52b242; SHA-256 18eba71227cfe04a7f01011970303c8ebaba875e63c7a99fb2d2042796a55653)
specification: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (blob c4802a5a7fa3; INITIAL_APPROVE by Thoth), with delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE; S01 removed; HDE Build Notes 2.20)
implementation_plan: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd44; INITIAL_APPROVE by Isis), with delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (DELTA_APPROVE; HDE Build Notes 2.19)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.2.md (636,840 bytes; SHA-256 d1fcffecf95a4c236cb27f95b3056a2c660d3c99e2418ed89f359c312d0f5bca). v13.8 to v13.8.2 adds only addenda 2.29 and 2.30 and their index lines, read in full here; addenda 2.27 and 2.28 read in full earlier in this session
repository_head_read: origin/main 58a27859 ("PF10", after 34d132a0, #746)
PF10_ADDENDUM_OUTPUT: NONE (CL-C-10 is not a PF10_BUILD_NOTES_ADDENDUM producer)
canon_conflict_register: CR-1 to CR-8 and CR-10 to CR-12 carried as decided; CR-9 decided here, APPROVED, alternative (a) (§6.1); no new conflict
---

# HDE-CRD-0002 — CRD Retrospective and Closure Decision (CL-C-10), v1.0

## 0. Decision

| Field | Value |
| :- | :- |
| Decision | **`DO_NOT_CLOSE`** |
| State | `CLOSURE_RETURNED_FOR_CLOSE_MUTATION_SET` |
| Why | Every approved requirement is delivered or removed as approved, every work unit is accepted, the Ops task is accepted, documentation is complete and the final QA verdict is `PASS` (§2, §3). One required closure element is missing: **HDE-CRD-0002's own close mutation set** (close pack, ledgers, close-run evidence family and their Index and Mirror registration). The approved Implementation Plan names it as this change's Close Gate (§9 item 5). PF06 §1.0.6, §3.5.1 and §3.5.2, PF12 "Close-pack artifacts" and PF04 §2.0.19 require it for a CRD close. The Product Owner's own measure for WU-PR-07 is that this change "closes through the ordinary Close Gate with the new writer on the first attempt" (§4, B-1) |
| What is not wrong | Nothing failed. No approved objective failed and no QA finding is open, so this is not an ESC-30 matter (§4) |
| Return work | The close mutation set, T0 to T7 of Plan v1.1 §7 WU-PR-07 "Terminal-state reachability", with the bindings of §8 |
| Decided here | CR-9 `APPROVED`, alternative (a) (§6.1); the close representation of S01, G-1 (§6.2); a correction to the recorded state of D-1/LR6-O1 (§6.3) |
| Resume point | CL-C-10 again, in the continuing Isis session, after the Product Owner merges the close pull request, with that pull request's result record |
| Next | Terminal return to the Product Owner for the T0 authorization and the vehicle (§9). No continuation block |

This decision does not close the change. A future `CLOSE` will rest on the same evidence plus the close mutation set; nothing else in §2 to §5 needs to be redone.

## 1. Evidence read

| Input | How it was read |
| :- | :- |
| QA Report v1.0, QA RCA v1.0, QA-120 checkpoint v1.0 | In full, here |
| Specification v1.1-approved | Requirements, Exclusions, Constraints, Compatibility dependencies, Routed dependency and Closure result read in full here; review v1.1 and delta 01 with its review through worker extraction and HDE Build Notes 2.20 |
| Implementation Plan v1.1 | §1 to §7 and §9 to §15 read in full here; review v1.1, delta 01 and its review through worker extraction and HDE Build Notes 2.19 |
| Implementation Audit v1.0 | Worker extraction (read in full by the worker, 119,180 bytes) |
| PR-40 lineage reviews (11), Ops receipt, documentation completion | Decision lines and PR lineage read here (§3); bodies through worker extraction |
| QA-10 readiness, Reality Audit and Change Audit Triage v1.1; Live QA Guide v1.0; QA-70 reviews | This reviewer's own records; the FND-028 row and Guide §8 G-1 re-read here |
| QA Plan v1.3 | Read in full at review v1.4 in this session; §13 CR-9 and checks 14 and 15 re-read here |
| Remediation, rescope, postmortem and corrective-decision records; Product Owner dispositions and directions; the fourteen PF10 addendum records | Worker extraction (each file read in full, byte counts verified). The WU-PR-07 business-case disposition §2 and §3 and the WU-OPS-01 Ops task §13 (CR-9) re-read here |
| Precedent | `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md` (read in full) and v1.0 and v1.2 (front matter and close-pack passages); `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md` (read in full) |
| Repository state | `origin/main` `58a27859`: no `audit/HDE-CRD-0002_*`, no `audit/docdeltas/hde-crd-0002_*`, no `audit/qa/hde-crd-0002/close/` |

**Worker extraction.** Three read-only workers each read their files in full and returned quoted decision, scope and open-item extracts with byte counts. Their reports were checked against the files for every fact this decision relies on (decision lines, the WU-PR-07 measure, CR-9, G-1, FND-028, the addendum numbering). Extracts are aids; the files are the record.

## 2. Delivered-scope disposition

| Req. | Delivered by | Accepted at PR-40 | QA (Plan v1.3 checks) | Disposition |
| :- | :- | :- | :- | :- |
| S01 | — | — | 15 (removal evidence) | **Removed** by Specification delta 01 (DELTA_APPROVE; Product Owner OPTION 1; HDE Build Notes 2.20). Not delivered: a regular wheel install outside a source checkout still does not admit the release (delta 01 C-6) |
| S02 | WU-PR-03 (#643, #646) | ACCEPT | 17 `PASS` | Delivered |
| S03, S04, S05 | WU-PR-01 (#627, #630) | ACCEPT (v2.0) | 2 `PASS` | Delivered |
| S06 | WU-PR-02 (#634, #637) | ACCEPT (v2.0) | 3 `PASS`, with R-1's caveat | Delivered. Caveat: proven under Ubuntu 26.04's patched setuptools 78.1.1 as wired by a Moon Loop, not under the Plan's literal E-D construction |
| S07 | WU-PR-03 | ACCEPT | 4 `PASS` | Delivered |
| S08 | WU-PR-04 (#651) | ACCEPT | 5 `PASS` | Delivered |
| S09 | WU-PR-03 | ACCEPT | 6 `PASS` | Delivered (harness retired) |
| S10 | WU-PR-03 | ACCEPT | 7, 18 `PASS` | Delivered as an explicit-`dev` gate. The Specification text names "`dev`, `test` or `local`"; Plan v1.1 §15 (approved at IA-30) and corrective decision AD-2 (CR-8) read canon as requiring exactly `dev`, so `test` and `local` refuse. An approved reading, not a deviation found here |
| S11, S12, S13 | WU-PR-02 | ACCEPT (v2.0) | 8 `PASS` | Delivered |
| S14 | WU-PR-04 | ACCEPT | 9, 20 `PASS` | Delivered; one bounded live vendor call initiated by the Product Owner |
| S15 | WU-PR-03 | ACCEPT | 10 `PASS` | Delivered under AD-1 (CR-7): canon-retired routes excluded rather than removed |
| S16, S17 | WU-PR-08 (#687) | ACCEPT | 11 `PASS` | Delivered (reduced WU-PR-08; `1.4.0` cut dropped by delta 01) |
| S18 | WU-PR-03 | ACCEPT | 11 `PASS` | Delivered |
| S19 | WU-PR-05 (#656) | ACCEPT | 12, 18, 19, 20 `PASS` | Delivered: the review is recorded; F01 to F09 fixed; R01 to R07 routed to the Product Owner with reasons (FND-029, pending, non-gating) |
| S20 | WU-PR-06 (#660); remedy WU-REM-02 (#734) | ACCEPT; ACCEPT | 13 `PASS` (RV-1) | Delivered. QA110-F01 found, remedied and verified. In scope by the Product Owner's option A (§6.3) |
| S21 | WU-PR-07 (#668, companion #670) | ACCEPT | 14 `PASS` | Delivered as capability: writer, v2 schema, close-run family, ADR approved with changes (AQ-1; HDE Build Notes 2.15, 2.17). **Not yet used for HDE-CRD-0002's own close (B-1)** |
| S22 | WU-PR-02; remedy WU-REM-01 (#716) | ACCEPT; ACCEPT | 21 `PASS` | Delivered: the first real HDE-CRD-0002 publication validates |

**Other units.**
- WU-DOC-01 (#692, #695, #700): PR-40 ACCEPT (v3.0); DOC-20 `COMPLETE` (v1.1).
- WU-OPS-01: Ops task receipt `ACCEPT`; deployed `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` at `1.3.0` read by QA check 16.
- Routed out of the CRD at approval: RD-1 (GCFPE-MGMT-10), not a closure condition (Specification "Routed dependency").

**Release.** `1.3.0` with `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, refreshed in place, no version cut (delta 01).

## 3. Closure trace (PF06 §1.0.6)

PF06 §1.0.6: "A CRD may close only when its applicable implementation, Ops, QA, evidence, ADR, and drainage obligations have received the required decisions."

| Obligation | State | Holds |
| :- | :- | :- |
| Implementation | Eleven units, each with an ACCEPT lineage review on its final cycle; every requirement delivered or removed as approved (§2) | Yes |
| Ops | WU-OPS-01 receipt `ACCEPT`; CR-9's path-proof question decided here (§6.1) | Yes |
| QA | QA-120 verdict `PASS`; run complete, 21 of 21 checks accepted; one behavior defect (QA110-F01) remedied and verified | Yes |
| Evidence | QA evidence of record on `main`, indexed, validators green (Report §7). **The close mutation set does not exist** (§4 B-1) | **No** |
| ADR | The S21 ADR is approved with changes (AQ-1, HDE Build Notes 2.15) and defers to HDE Build Notes (2.17). No other ADR is required: S21's is the only canon change (Specification Exclusions) | Yes |
| Drainage | Each item has a decision and an owner: drained, explicitly deferred to its owner, or routed (§7). The close mutation set's drain-targets ledger records them (§8) | Yes, once recorded in the ledger |

## 4. Blocker determination

| # | Item | Acceptance-critical? | Basis | Disposition |
| :- | :- | :- | :- | :- |
| B-1 | No close mutation set: no `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` or their path proofs; no candidate source; no `audit/docdeltas/hde-crd-0002_doc_deltas.md` or `_drain_targets.md`; no `audit/qa/hde-crd-0002/close/` family | **Yes, closure prerequisite** | Plan v1.1 §9 item 5 ("Close Gate. HDE-CRD-0002's own close pack is produced by the S21 writer") and §7 WU-PR-07 T0 to T7; Implementation Audit S21 ("S21 completes before HDE-CRD-0002's ordinary Close Gate"; R-4: "the ordinary Close Gate waits or an exceptional closure is the Product Owner's decision"); PF06 §1.0.6, §3.5.1 ("Only the close mutation set is required to carry the full close pack"), §3.5.2.1; PF12 "Close-pack artifacts" ("This generic close-pack contract supports both Epic/PF09 and CRD/PF30 work"); PF04 §2.0.19 ("Close-pack presence is a baseline closure artifact requirement"); the WU-PR-07 business-case measure; FND-001 remedy measure (2) ("the close-pack pull request passes the evidence lane"); precedent HDE-EPIC040 CL-E-10 v1.1 | Return work (§8) |
| B-2 | G-1: the close representation of S01 | Would block the close pack's `SATISFIED` decision if left open | Live QA Guide §8 G-1; IR-11; the v2 schema allows only `MET` and `NOT_MET`, and `SATISFIED` needs every row `MET` | **Decided here** (§6.2); the close mutation set applies it |
| B-3 | CR-9 `PROPOSED`, unreviewed | An undecided obligation would fail PF06 §1.0.6's "received the required decisions" | Plan v1.3 §13; WU-OPS-01 Ops task §13 | **Decided here** (§6.1) |
| — | QA-120 verdict, QA110-F01, O-1, I-1, R-1 caveat, FND-028, FND-029, FND-012, O-A, OBS-1, OBS-2, OBS-12, PO-2, PO-5, D-1 (RCA), MB-021, the evidence-persistence general rule, CR-7/CR-10/CR-11 drainage, residual workstation state | No | Each is outside this CRD's requirements, an explicitly owned later-change candidate, a pending drainage, or a risk the Product Owner accepted; none is a failed approved objective (PF19 §3.1.3 separates drainage and administration from incomplete required work) | §7, with owners; the drain-targets ledger records them |

**Why this is not post-closure administration.** PF19 §3.1.3 and `AGENTS.md` "Operating routes and authority" make permanent drainage and board administration follow closure. They do not cover the close mutation set. HDE-EPIC040's CL-E-10 v1.0 read them as if they did, and v1.1 corrected it at the Product Owner's direction ("this is not really 'post closure' work, if a task needs to be done. This means we would need to run a fix for this, and then run CL-E-10"). This decision applies that correction from the start.

**Why not exceptional closure.** PF06 §3.5.1 reserves closure outside the ordinary Close Gate to an explicit Product Owner decision, and only after an ordinary lifecycle fails or is withdrawn. Nothing has failed: the writer exists and passed check 14. The Product Owner's WU-PR-07 measure asks for the ordinary Close Gate "on the first attempt" with "no exceptional-closure record".

## 5. Retrospective

### 5.1 Intended against delivered

- **Intended:** 22 acceptance intents across four phase blocks (Specification v1.1): carried defects (S01 to S18), one code security review (S19), a read-only pre-push check (S20), a close-pack writer for Epic and CRD identities (S21) and CRD evidence admission (S22).
- **Delivered:** S02 to S22 on `main` and verified by QA; S01 removed by Product Owner decision; release kept at `1.3.0` (§2).
- **Not delivered by design:** RD-1 (routed); S01; a close pack for HDE-EPIC040 (excluded).

### 5.2 Scope changes and their reasons

| Change | Reason | Record |
| :- | :- | :- |
| S01 removed; `1.4.0` cut dropped | S01 "has no real input"; the version label "has no reader" | WU-PR-08 scope disposition (OPTION 1); Specification delta 01; Plan delta 01 |
| S10 served for `dev` only | Canon requires explicit `dev` for the route | Plan v1.1 §15; AD-2 (CR-8) |
| S15 by exclusion of canon-retired routes | Canon precedence over the Specification's wording | AD-1 (CR-7) |
| Rescopes of WU-PR-01, WU-PR-03 (two), WU-PR-07 | Stale tools, start-helper default, purity roster, closeout-validation install | RS-20 reviews; HDE Build Notes 2.2, 2.6, 2.7, 2.13 |
| Two remediation units, WU-REM-01 and WU-REM-02 | FND-001 (evidence-lane tests assumed the CRD's root absent) and QA110-F01 (pre-push copies shared the source's objects) | ESC-40 reviews; HDE Build Notes 2.23, 2.24, 2.27 |
| No cost ceiling | Product Owner direction | HDE Build Notes 2.18 |

### 5.3 Implementation and integration quality

- Every unit landed through an ordinary pull request merged by the Product Owner, with exact-head CI and a PR-40 lineage review. Three units needed a second cycle (WU-PR-01, WU-PR-02: LR-1 corrections; WU-PR-03: corrective cycle after a merge with open review findings), and WU-DOC-01 needed three.
- Review load was heavy where designs reached outside the repository: WU-PR-06 took 24 Codex rounds and 51 findings (postmortem v1.1), which produced the business-case and real-input rules (HDE Build Notes 2.11) and the P1 rule (2.14).
- The release-identity spine held: member-changing units refreshed the manifest in place and the `release_id` stayed traceable throughout.

### 5.4 QA findings and causes

QA found one product defect, QA110-F01. Its cause is evidenced: `--shared` throwaway copies freshened the source checkout's pack, and the guard correctly saw it. Earlier validation venues used shallow sources, which disable `--shared`. The QA RCA §6 to §8 holds the full analysis, which this decision accepts without change. Two `TOOLING_BLOCKED` runs (checks 3 and 21) came from venue assumptions and from a guard narrower than the CI-exempt prefix list.

### 5.5 Decisions that shaped the change

AQ-1 (S21 ADR approved with changes), option A for WU-PR-06 (S20 kept), OPTION 1 for WU-PR-08 (S01 removed), the corrective decisions AD-1 to AD-6, no cost ceiling, the P1 rule, the Codex security review's deprecation, and the C-1 route direction D-1 to D-3 (CR-12).

### 5.6 What helped and what hindered

- **Helped:**
  - an exact Plan with a terminal-state design for the close (WU-PR-07);
  - QA's full-history environment, which found QA110-F01 as designed;
  - byte-for-byte prototype diffs in remediation;
  - preserved failure history.
- **Hindered:**
  - instructions read canon section by section rather than bullet by bullet (corrective decisions §6);
  - designs promised fidelity to external systems over open-ended inputs (WU-PR-06);
  - validation venues differed from the operating environment (shallow clones; container against workstation);
  - coupled constraints were missed in guards and redlines (FND-101, FND-202, FND-203, O-11);
  - prompt-route gaps: no author prompt for an approved-QA-Plan delta (MB-021), and, again, no prompt for the close mutation set (§10).

### 5.7 Residual risks

- S06 is proven only under the venue's patched setuptools, as wired (R-1 caveat).
- I-1: secret values printed into an executing session's transcript. The Product Owner accepted the risk without rotation (PO-QA100-4).
- O-1 and O-A remain as later-change candidates.
- The live Railway start command is unverified. If production ever started without the checkout, admission would refuse to start (`MISSING_FILE`).

### 5.8 Lessons

| ID | Lesson | Owner |
| :- | :- | :- |
| CL-L1 | The RCA's L-1 to L-7 stand as written | As the RCA names |
| CL-L2 | When the approved Plan names the change's own Close Gate, the closure-readiness route must schedule it before the closure decision. QA-120 here, as at HDE-EPIC040, listed the close-pack measure as a later point rather than a Close Gate prerequisite | GCFPE-MGMT-10 maintenance owner (QA-120 and CL-C-10 prompts) |
| CL-L3 | The second instance of the same flow gap (HDE-EPIC040, then HDE-CRD-0002) shows that a one-time task prompt does not fix it; a native close-mutation-set stage is needed | GCFPE-MGMT-10 maintenance owner; Product Owner |
| CL-L4 | A Product Owner decision that later records restate as open (D-1/LR6-O1) needs its outcome carried into each successor's open-items table, not only its question | Every record author; QA-10 and QA-120 in particular |

## 6. Decisions made in this record

### 6.1 CR-9 — path proofs under the WU-OPS-01 root: `APPROVED`, alternative (a)

| Field | Value |
| :- | :- |
| Reviewer and session | Isis (Isis-53), https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok |
| Reviewed artifact | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13, CR-9 as proposed (read in full here) |
| Decision time | 2026-10-26T01:15:16Z |
| Decision | `APPROVED`, alternative (a): the Ops evidence carries a SHA-256 ledger, and its path-proof coverage comes from the QA check that consumes it, published by the updater's existing HDE-CRD-0002 QA admission |
| Rationale | Canon places the path proof for consumed Ops evidence on the consuming QA check (PF19 v3.0.6 §11.1, "When QA consumes it, the QA check's governed `audit/qa/<change-id>/checks/<check_id>/primary.log` and required sibling path proof point to that evidence rather than re-homing it"), and only the canonical updater writes path proofs (PF12 v2.9.6 §8.3 and §8.6.3). Check 16 consumed the six WU-OPS-01 files by reference with verified SHA-256 values, and QA-110 v1.2 accepted it (FND-031). Alternative (b) would add code and a PR cycle for no proof gain; (c) gives less than (a) |
| Plan text | Plan delta 01 P-9's literal "with path proofs" is read through this decision. No Plan delta is made: the Ops unit is complete and accepted, so a delta would have no consumer |
| Drainage | None in permanent canon, which is consistent (as CR-9 proposed) |
| Boundary | CR-9 named "Isis, at the IA-30 boundary". No further IA-30 occurs for this change, and PF06 §1.0.6 requires the decision before close, so it is made at this change's last Isis decision boundary |

### 6.2 G-1 — the close representation of S01

- **Decision.** In the close candidate source, S01 is one acceptance row with result `MET` for its **amended** criterion: removal under Specification delta 01 (DELTA_APPROVE; HDE Build Notes 2.20) and its stated limit. It is bound to check 15's `PASS` primary, `audit/qa/hde-crd-0002/checks/qa-15-s01-removal/primary.log`, whose Plan v1.3 mapping names S01. Its `limitation` text states, in substance: "Removed by Specification delta 01 (Product Owner OPTION 1, 2026-10-21). Check 15 proves the removal and its stated limit, not delivery: a regular wheel install outside a source checkout still does not admit the release." S01 is also listed under the close report's superseded or rejected scope.
- **Why it is truthful.** The approved Specification is v1.1 plus delta 01. Its S01 criterion is the removal, and check 15 proves exactly that. `MET` with that limitation claims no delivery.
- **Authority.** G-1's owners are "the close mutation set and Isis at closure, with the Product Owner if a route beyond the writer's pinned forms is needed" (Live QA Guide §8). This representation stays within the writer's pinned forms (`MET` or `NOT_MET`; criterion text not copied), so no Product Owner route is needed.

### 6.3 Correction: D-1/LR6-O1 is decided

The QA Report §10, QA Plan v1.3 §14, my QA-70 review v1.4 §6, the WU-REM-02 lineage review and HDE Build Notes 2.27 and 2.28 carry "D-1/LR6-O1 (whether S20 is removed)" as an open Product Owner decision. It was decided on 2026-10-20: "S20 stays in scope as delivered by #660; no Specification delta is made" (WU-PR-07 business-case disposition §3, option A). Option A's stop rule was met at QA-10, so removing the `replay` report is a later change and the Product Owner's (FND-028; triage v1.1). What remains open is FND-028 only.

## 7. Open items and owners

None of these is a closure prerequisite. The close mutation set's drain-targets ledger records the drainage and deferral items (§8, R-1).

| Item | Owner | State |
| :- | :- | :- |
| HDE-CRD-0002 close mutation set (§8) | Product Owner (T0 authorization, vehicle, merge); the close session (T1 to T6) | **Return work** |
| PO-2 (do not pin tool versions); PO-5 (evidence persistence → PF19 §3.4.3) | Product Owner | `PENDING_DRAINAGE` |
| D-1 of the RCA (Plan Templates: guards take the classifier's full prefix list) | Product Owner | Proposed |
| Undrained HDE Build Notes 2.2 to 2.30 for this change, including CR-7, CR-10 and CR-11 drainage and the S21 ADR's affected canon homes | Product Owner, through canon maintenance | Pending; not a closure prerequisite (2.15) |
| FND-028 (remove `replay` in a later change) | Product Owner | Later change |
| FND-029 (S19-R01 to R07); FND-012; X-02; the legacy chart-loader defect (HDE-SEPA006) | Product Owner | Pending, non-gating |
| LR7-O1 / FND-020 (the S21 ADR's line 65 clause, superseded by HDE Build Notes 2.17 resolution A) | Product Owner (ADR revision on instruction) | Open documentation defect; the writer and 2.17 govern |
| Documentation and canon delta candidates FND-017 to FND-021 and FND-040; the HDE-CLI-API-Vendor-Ref §7.1.11 DD-04 paragraph | Product Owner | Candidates |
| Later-change candidates FND-022, FND-023 (LR8-F1), FND-024 (PR35-C1), FND-037, FND-038, X-01 to X-04, LR6-O4 | Product Owner | As the triage v1.1 records them |
| FND-004 of the Ops receipt (residual Railway login on the workstation) | Product Owner | Open |
| O-1 (OPS03 `EXDEV`) | Thoth; Product Owner if independent | Open, later-change candidate |
| O-A (owner-test fixtures re-time the developer's checkout) | Product Owner | Later-change candidate |
| OBS-1 (12 Epic acceptance maps already failing viability); OBS-2 (local failures of the contract-inventory test); OBS-12 (undeclared `ruby` dependency) | Product Owner | Later-change candidates |
| I-1 transcript handling | Product Owner | Risk accepted; transcript handling open |
| Residual workstation and service-host state (Report §12) | Product Owner | Open |
| MB-021 (approved-QA-Plan delta route); QA-100 evidence-commit default; the close-mutation-set route (§10) | GCFPE-MGMT-10 maintenance owner | Reported |
| Addendum numbering: the adr-defers record published as 2.17, the no-cost-ceiling record as 2.18, the Specification delta 01 record as 2.20 (each draft carries another number); addendum 2.11's misnumbered cross-references | Product Owner | Publication facts; CL-20 reconciles the inventory |
| Board update; closure memo | After a future `CLOSE` (§11) | Not due |

## 8. Exact return work

One close mutation set, as approved Plan v1.1 §7 WU-PR-07 "Terminal-state reachability" (a) to (e) and §9 item 5 define it. All steps run under closed rails in a local clean clone of the close branch; no close-run, close-pack or Index byte comes from a hosted workflow.

| # | Plan step | Required outcome |
| :- | :- | :- |
| R-0 | T0 | The Product Owner authorizes HDE-CRD-0002's close mutation set and names its vehicle: "a dedicated top-level close PR session acting under the Product Owner's authorization of that close PR", or the Product Owner (WU-PR-07 (c)). Its other preconditions hold: the final QA verdict and manifest are on `main`; AQ-1 is decided |
| R-1 | T1 | Author the causal inputs and commit them (C1): `audit/HDE-CRD-0002_close_candidate_source.json` (schema v2) and the two ledgers, `audit/docdeltas/hde-crd-0002_doc_deltas.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md`. The source must hold:<br>- an acceptance row for each of the 22 requirement IDs, each bound to the primaries of `PASS` checks whose Plan v1.3 mapping names it, with S01 as §6.2 decides;<br>- the deliverables (§2);<br>- deferrals from §7, each with its drain target or ADR status;<br>- the later-drain statements in the schema's vocabulary;<br>- `closure_decision` `SATISFIED` with posture `review_trace_only`, resting on the QA-120 Report's `verdict: PASS` (PO-35-20, HDE Build Notes 2.16 and 2.17);<br>- the follow-ups;<br>- the pointers, which name `audit/qa/hde-crd-0002/qa_step_logs_manifest.json`, the two ledgers and `audit/qa/hde-crd-0002/close/` as literal strings;<br>- the QA RCA placement (embedded summary, or `audit/HDE-CRD-0002_QA_RCA.md` by exact path; PF12 "Close-pack artifacts");<br>- the ADR block (2.15 C-1);<br>- `key_outputs` |
| R-2 | T2 | `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --write` on clean C1 |
| R-3 | T3 | `python tools/evidence/update_evidence_index.py`; commit C2 |
| R-4 | T4 | Same-run checks on clean C2, each captured with its command, exit status and output: the writer with `--check`; `update_evidence_index.py --check`; `orientation_demo.py --check`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `validate_evidence_paths.py`; `ci/checks/check_final_lf.sh` |
| R-5 | T5 | The close-run family under `audit/qa/hde-crd-0002/close/<check_id>/` through the updater's IF-4 entrypoint, inside its recovery transaction, never touching `qa_step_logs_manifest.json`; commit C3 |
| R-6 | T6 | Local re-validation on clean C3: the T4 set again, all exit 0; results go to the PR description only |
| R-7 | T7 | Hosted validation of the exact C3 head: the ordinary `test` job ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, and the Product Owner's `workflow_dispatch` of `.github/workflows/epic-closeout-validation.yml` with `git_ref` = C3 and the source path (its first hosted run, HDE Build Notes 2.13). Then the Product Owner merges |

**Also owned by the close work, not a closure prerequisite.** RF-12 (WU-DOC-01 documentation completion v1.1): update the nonclaim lines that state no close pack has been produced with the v2 writer (`README.md`, `AGENTS.md`, `CHANGELOG.md`) once HDE-CRD-0002's close pack exists. "Owner: whoever does that close work." Carrying it in the close pull request before T7 keeps the operative documents true at the merge. A later documentation pull request the Product Owner directs is the alternative.

**Not affected:** HDE-CRD-0002 cites no tracked issue (`TI-<id>`), so the v2 writer's ADR-status-only form for tracked issues (LR7-O9; HDE Build Notes 2.17 resolution B) does not limit this close.

**Measures this return observes:**
- WU-PR-07's: the ordinary Close Gate on the first attempt, every check mode passing, no exceptional-closure record;
- the FND-001 remedy's measure (2): the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes.

**Restart rules** are the Plan's: a change to any causal input restarts at T1; bringing `main` into the close branch restarts at T2. No step repairs a later step's output by hand.

**Return condition:**
- The close pull request is merged by the Product Owner.
- CL-C-10 is re-invoked in the continuing Isis session with the close session's result record.
- A close session that stops on a blocker returns that blocker to the Product Owner as its terminal result.

## 9. Product Owner decision needed

- **What the close mutation set is.** One pull request that writes HDE-CRD-0002's close report and manifest with the S21 writer, its two ledgers and its close-run evidence, registers them in the Index and Mirror, and validates them on the exact head. It is the last piece of this change's approved Plan, and the first real use of the writer this change built.
- **What breaks without it.** The change cannot close ordinarily. The WU-PR-07 measure and the FND-001 remedy's measure (2) stay unmet. The only other closure route is a Product Owner exceptional closure, which the WU-PR-07 measure says should not be needed.
- **What is needed.** Your T0 authorization of the close mutation set and its vehicle. Release 100926.1 names no prompt for it (§10). The Plan permits a dedicated top-level close PR session acting under your authorization, or you.
- **Options:**

| Option | Cost |
| :- | :- |
| (1) Authorize it; a dedicated top-level close session runs §8 from this record and Plan WU-PR-07 under a one-time task prompt, as HDE-EPIC040-CLOSE01 did | One task prompt to write, one close PR; your Proceed is the invocation, your merge ends it |
| (2) Authorize it; you run §8 yourself in a local clean clone | Your time; same PR |
| (3) Exceptional closure without the close pack (PF06 §3.5.1) | Fails the WU-PR-07 measure you set; leaves the writer unused on a real close |

- **Recommendation: (1).** It keeps author and executor separate, follows the approved Plan's actor rule, and matches the HDE-EPIC040 precedent you directed.

## 10. Prompt-ecosystem report (GCFPE-MGMT-10)

- **Prompts:** CL-C-10, QA-120 and the PR and Ops prompts of release GCFPE-20261009.1 / 100926.1.
- **Expected:** a native route for a CRD's close mutation set between QA-120 `PASS` and CL-C-10, as the alpha feedback brief requested for Epics on 2026-09-29.
- **Actual:**
  - CL-C-10's `DO_NOT_CLOSE` routes only to "the existing owner for already-authorized ordinary correction" or ESC-30;
  - its step 5 lists post-closure work but not the close mutation set;
  - QA-120 lists the close-pack measure as a later point;
  - no PR or Ops prompt consumes a closure finding, and the close mutation set has no `WORK_UNIT_ID` in the Plan's §7 list.
- **Evidence:** this record; `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md` (causes C-1 to C-4 recur unchanged).
- **Interim treatment:** §9.
- This session writes no Notion page; the report is carried by this record.

## 11. Post-closure administrative work (after a future `CLOSE`; not prerequisites)

1. CL-20: closure memo to Thoth and Master Scrum, the post-closure record and its addendum inventory.
2. Master Scrum's board update on the HDE development board, after memo delivery.
3. Conditional ADR maintenance (CL-30), only if a qualified condition arises; none is identified now (the S21 ADR's revision is the Product Owner's to direct, HDE Build Notes 2.17).
4. CL-40: the scan for PF09 gaps and CRD candidates.
5. No PF09 maintenance (CRD; Specification Exclusions) and no PF30 record (CR-1).
6. Permanent drainage of §7's items by their owners.

## 12. PF10 addendum inventory (already produced for this change)

All under `docs/ephemeral/`, each `HDE-CRD-0002-<name>.md`. Published numbers are those in PF10 v13.8.2.

| Record | Producer | Published as |
| :- | :- | :- |
| `WU-PR-01-PF10-build-notes-addendum-v1.0` | RS-20 | 2.2 |
| `PF10-build-notes-addendum-codex-security-review-deprecation-v1.0` | Product Owner direction | 2.3 |
| `WU-PR-03-PF10-build-notes-addendum-v1.0` | RS-20 | 2.6 |
| `WU-PR-03-corrective-PF10-build-notes-addendum-v1.0` | Product Owner direction | 2.7 |
| `WU-PR-07-PF10-build-notes-addendum-v1.0` | RS-20 | 2.13 |
| `PF10-build-notes-addendum-p1-findings-v1.0` | Product Owner direction | 2.14 |
| `PF10-build-notes-addendum-aq1-adr-v1.0` | Product Owner AQ-1 | 2.15 |
| `PF10-build-notes-addendum-adr-defers-v1.0` | Product Owner direction | 2.17 (record says 2.16) |
| `PF10-build-notes-addendum-no-cost-ceiling-v1.0` | Product Owner direction | 2.18 (record says 2.19) |
| `implementation-plan-delta-01-PF10-build-notes-addendum-v1.0` | IA-30 | 2.19 |
| `specification-delta-01-PF10-build-notes-addendum-v1.0` | CF-C-30 | 2.20 (record says 2.18) |
| `remediation-FND-001-PF10-build-notes-addendum-v1.0` | ESC-40 | 2.23 |
| `remediation-FND-001-PF10-build-notes-addendum-v1.1` | ESC-40 | 2.24 |
| `remediation-QA110-F01-PF10-build-notes-addendum-v1.0` | ESC-40 | 2.27 |

The other HDE-CRD-0002 entries in PF10 (2.4, 2.5, 2.8 to 2.12, 2.16, 2.21, 2.22, 2.25, 2.26, 2.28 to 2.30) record lineage reviews, receipts and QA stages, not qualifying approvals. Under CR-12, no addendum records the QA Plan v1.3 change.

## 13. CANON_CONFLICT_REGISTER

| ID | Status | Decision owner | Change here |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | `APPROVED_AS_CHANGED` | Thoth | — |
| CR-4 | `APPROVED` | Product Owner | — |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner | — |
| CR-6 | `APPROVED`, alternative (a) | IA through RS-20 | — |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner | — |
| CR-9 | **`APPROVED`, alternative (a)** | Isis | Decided here (§6.1); history: proposed by the IA in the WU-OPS-01 Ops task v1.0 §13, interim (a) applied by QA check 16 |
| CR-10 | `APPROVED`, alternative (a) | Isis (ESC-40) | — |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis (QA-70 review v1.0) | — |
| CR-12 | `APPROVED`, alternative (a) | Product Owner | — |

No new conflict. The close-mutation-set gap is a prompt-ecosystem gap (§10), not a canon conflict: canon is clear that the close mutation set is required.

## 14. TypeSafe reading for the return-work session (the close mutation set)

Action sent (v8.2): "In a dedicated session, produce one new close pull request for an already QA-passed change request of 22 requirements: author one close-candidate source file binding each requirement to its passing QA evidence plus two short ledgers, then run the existing governed close-pack writer, the evidence-index updater, about seven read-only validators and the close-run evidence publisher in a fixed, already approved seven-step sequence under closed rails, re-validate locally, and hand the exact head to hosted CI and one manual validation workflow. An approved step list exists; no product code changes and no live run against a provider occurs; the closure decision is re-run independently after the Product Owner merges."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.07 (confidence 0.35). Rung probabilities: low 0.02, medium 0.32, high 0.26, extra high 0.39, max 0.01, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.96, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.95).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.003, Fable 5.1 at high 0.003, Fable 5.1 at extra high 0.004, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.019, Opus 5.5 at medium 0.307, Opus 5.5 at high 0.250, Opus 5.5 at extra high 0.374, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.001, Sonnet 5.5 at medium 0.010, Sonnet 5.5 at high 0.008, Sonnet 5.5 at extra high 0.012, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - **Flags: boundary between medium and extra high.**
  - Sent 2026-10-26T01:12:24Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-26T01:12:24Z; HTTP 200 in 0.63 s; 5477 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "HDE-CRD-0002 close mutation set (return work of CL-C-10 v1.0 DO_NOT_CLOSE)", before this record was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - Close mutation set: Nathan's pick is not stated.
  - This CL-C-10 session: Nathan's pick is not stated. Its reading is in the QA Report §15 (Opus 5.5 at extra high, score 3.06).

**Surface advice.**
- **Session.** A dedicated top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, created by Nathan, acting under his authorization of the close PR. It is not a subagent of this session, and it is separate from the QA and Isis sessions.
- **Environment.** A local clean full-history clone of the close branch with CPython 3.12 and CI's full install (Flask is needed by the updater's `--check`), and `ruby`, `bash` and `curl` on `PATH`. Every step runs under closed rails through `env -i`.
- **Access.** GitHub write access for one branch and one pull request, and GitHub Actions dispatch rights for Nathan's T7 run of `epic-closeout-validation.yml`. No production, Railway, vendor or database access.
- **Reads:**
  - this record (§6.2, §7, §8);
  - Plan v1.1 §7 WU-PR-07 and §9;
  - `schemas/close_candidate_source.v2.json` and `tools/qa/generate_epic_close_pack.py`;
  - `docs/adr/hde/close_pack_writer_adr.md` with HDE Build Notes 2.15 and 2.17;
  - QA Plan v1.3 §10;
  - the QA Report and RCA.
- **Writes:**
  - only the close mutation set's paths (`audit/HDE-CRD-0002_*`, `audit/docdeltas/hde-crd-0002_*`, `audit/qa/hde-crd-0002/close/**`, the updater-owned graph files);
  - its result record under `docs/ephemeral/`.

## 15. Nonclaims

This decision does not:
- close HDE-CRD-0002 or establish acceptance of it;
- produce a close pack, or establish Close Gate completion or an exceptional closure;
- establish deployment, release activation, PF09 or PF30 movement, canon drainage or a board update;
- edit PF canon, PF10, code, tests or governed evidence;
- authorize the close mutation set, which is the Product Owner's (§9).

## Canon relied on

Read on `main` at `58a27859`; this branch edits no `docs/pfcanon/` file. Apart from PF10, `docs/pfcanon/` is unchanged since this session's earlier reads.

| Decision topic | Sources read (title, version, sections) | Applied in |
| :- | :- | :- |
| Task, decision states, routing, terminal return | CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1 (page state 2026-10-12T02:29:13.994Z), read in full: "Inputs", "Execute" 1 to 5, "Required result", "Next step and recovery", "Terminal operator return and receiver compatibility"; CL-20 — Prepare Closure Memo and Post-Closure Record — 100926.1 (page state 2026-10-12T02:29:16.766Z), read in full as the positive branch's receiver | §0, §9, §11 |
| CRD closure predicate | PF06-Canon-Change-Process-Guide v2.5.4 §1.0.6 "QA, closeout, and PF30 result update" (read in full); §1.0.4 (CRD follows the Epic process by substitution); line 28 ("They do not differ in applicable development, QA, evidence, operations, or closure rigor.") | §3, §4 |
| Close Gate and close mutation set | PF06 v2.5.4 §3.5.1 (including "Exceptional closure record"), §3.5.2.1, §4.1.1 applicability matrix (close report and manifest "Close-only"), read here | §4, §8, §9 |
| Close pack for a CRD | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 "Close-pack artifacts (deterministic path-of-record; baseline artifacts)" and "Change-container compatibility (normative)", read here; PF04-Canon-HDE-Governance v2.8.7 §2.0.19 close-pack baseline and "Close report minimal content", and Appendix D.0, read here | §4, §8 |
| Drainage and administration after closure | PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.3, read in full; "Close-pack truthfulness and same-run execution (normative)" (line read) | §4, §8, §11 |
| Ops evidence path proofs (CR-9) | PF19 v3.0.6 §11.1 (the consuming-check sentence, read here at its line) and PF12 v2.9.6 §8.3 and §8.6.3, as quoted in CR-9's proposal | §6.1 |
| Approved scope and its changes | Specification v1.1-approved; delta 01 (HDE Build Notes 2.20); Implementation Plan v1.1 §3, §7, §9, §13, §15; Plan delta 01 (2.19) | §2, §5 |
| Close design and S01 representation | Plan v1.1 §7 WU-PR-07 "Terminal-state reachability" (a) to (e); HDE Build Notes v13.8.2 2.13, 2.15 (C-1, C-2), 2.16 (the PO-35-1 to PO-35-21 table) and 2.17 (resolutions A and B); Live QA Guide v1.0 §8 G-1; `schemas/close_candidate_source.v2.json` (acceptance result enum `MET`/`NOT_MET`) and `tools/qa/generate_epic_close_pack.py` (the `MET` checks) | §6.2, §8 |
| Measures due at close | WU-PR-07 business-case disposition v1.0 §2 and §3 (read here); HDE Build Notes 2.24 (FND-001 measure (2)) | §4, §8 |
| QA verdict, causes, lessons | HDE Build Notes v13.8.2 2.27 to 2.30, read in full; the QA Report and RCA | §2, §5 |
| No cost ceiling; P1 rule; Codex security review | HDE Build Notes 2.18, 2.14, 2.3 | §5 |
| Precedent | `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md` (read in full) and v1.2 (the exceptional-closure record) | §4, §9 |
| Repository rules | `AGENTS.md`: "Operating routes and authority", "Evidence attribution, currentness and distinct decisions", HDE-EPIC039 workflow posture (the writer is capability only), closed rails | §4, §8 |
| TypeSafe reading | HDE Build Notes 2.1; the installed TypeSafe scoring skill | §14 |

**Searched and silent:** HDE Build Notes v13.8.2 holds no rule that moves a CRD's Close Gate after its closure decision or exempts a CRD from the close pack; its only rules on the subject (2.13, 2.15, 2.17, 2.23, 2.24) assume HDE-CRD-0002's close mutation set precedes its close.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-CL-C-10-20261026-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | Whole change: S01 (removed) to S22; WU-PR-01 to WU-PR-08, WU-DOC-01, WU-OPS-01, WU-REM-01, WU-REM-02 |
| prompt | CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1, page state of 2026-10-12T02:29:13.994Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, CL-C-10 (`DO_NOT_CLOSE`) |
| capture time | 2026-10-26T01:15:16Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, with three read-only worker subagents for input extraction |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-120-20261026-01 (Kronos) and the uses its Report lists |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
