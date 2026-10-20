---
artifact_type: ADR_DECISION_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-07-ADR-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
requirement: S21
decision_question: AQ-1 (Implementation Plan v1.1 §13; Implementation Audit v1.0 §8)
reviewed_proposal: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.0.md on pull request #668's branch claude/gallant-cerf-ysdde5 (added 9813970, revised 32ecc53; read in full at head 45e4cef)
reviewed_adr: docs/adr/hde/close_pack_writer_adr.md at #668 head 45e4cefb84e5fc8945502f9404f469b76dd4b20e (blob 544e1d3; status Proposed; 72 lines)
reviewed_code: tools/qa/generate_epic_close_pack.py, schemas/close_candidate_source.v2.json, tools/evidence/update_evidence_index.py, tools/qa/qa_harness.py and their tests at 45e4cef (the review workflow read 0d50b06; every finding was re-checked at 45e4cef, §3)
reviewer: the continuing whole-change Implementation Agent for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
review_method: one workflow (run wf_b59fcf78-0c1): five independent review dimensions, then two adversarial verifiers per finding (39 agents, none failed), followed by this reviewer's own re-check of every surviving finding at 45e4cef and against canon
recommendation_given: approve with changes (option B)
product_owner_decision: APPROVED WITH CHANGES (option B), chosen by Nathan / Product Owner on 2026-10-20 in this session, after this review's findings were put to him; recorded in docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-aq1-adr-v1.0.md (proposed PF10 addendum 2.15)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.5.md on #668's branch (addenda 2.11, 2.13, 2.14); main still carries v13.6.3
created_at: 2026-10-20T23:40:00Z
---

# HDE-CRD-0002 WU-PR-07 — AQ-1 ADR review v1.0

## 1. Result

**Recommendation: approve with changes (option B).** The ADR's design is sound and keeps every HDE-EPIC039 safeguard. But at #668's head `45e4cef`, two parts of the v2 writer still fall short of canon on real inputs:

- **The ADR block.** The v2 close report has no ADR block, which Change Process Guide §3.5.4 requires in every close report. HDE-CRD-0002's own close report needs one, for the S21 decision itself.
- **The Specification's identity.** The writer accepts any tracked document as the requirements source. HDE-CRD-0002's superseded Specification v1.0 is tracked on `main` with 21 `S` rows (no S22). Bound with 21 met rows, it would pass the coverage check and produce `SATISFIED`, against Change Process Guide §3.5.2.1's "each current governing requirement".

The proposal's §6 text delta also misstates three rules, and the ADR's canon table is missing five homes.

**The Product Owner's decision** (2026-10-20, in this session, on these findings): approve with changes. The decision, its conditions and the admission of the close-run evidence family are recorded in the proposed PF10 addendum 2.15, `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-aq1-adr-v1.0.md`.

## 2. What was reviewed

| Input | Identity |
| :- | :- |
| Proposal | `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.0.md` at `45e4cef` (the text the Product Owner pasted into this session matches the pushed `32ecc53` revision) |
| ADR | `docs/adr/hde/close_pack_writer_adr.md` at `45e4cef`, blob `544e1d3` |
| Code | the writer, the v2 schema, the updater, the QA harness and their tests at `45e4cef`; CX7-6's fix `5717008` is included |
| Approved base | Specification v1.1 (S21, constraint "Close-pack writer", Exclusions); Implementation Plan v1.1 §7 WU-PR-07 and §13; instruction v1.0; rescope review v1.0 §6; PF10 addenda 2.11, 2.13 and 2.14 |

**Head drift, disclosed.** The review workflow was given `0d50b06`. #668's head moved to `45e4cef` while it ran (proposal added in `9813970`, CX7-6 fixed in `5717008`, proposal revised in `32ecc53`, result record v1.5 in `45e4cef`). This reviewer re-checked every finding at `45e4cef`. One finding (the change kind did not select the pinned format) is resolved there by `5717008` and is dropped.

## 3. Findings and dispositions

All findings below survived both adversarial verifiers and this reviewer's re-check at `45e4cef`.

| ID | Kind | Finding | Evidence at `45e4cef` | Disposition |
| :- | :- | :- | :- | :- |
| A-1 | code gap | The v2 report renders no ADR block. Change Process Guide §3.5.4 requires a brief ADR block in every close report, each decision with a label, statement, decision point, options considered, bounding canon, final decision, whether it becomes canonical, and doc-delta targets by PF title. HDE Schemas & Artifacts §1.2 "Change-container compatibility" applies this to a CRD close | no ADR-block field in `schemas/close_candidate_source.v2.json` (closed schema) and no ADR-block section in the renderer; `adr` appears in the writer only as deferral and tracked-issue `adr_status` | **Fix in #668** (condition C-1) |
| A-2 | code gap | `requirements_binding` may name any tracked document. A real superseded Specification passes the coverage check | schema `requirements_binding` has no path constraint; the writer only resolves the binding; `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md` has 21 `| S<NN> |` rows, v1.1-approved has 22 | **Fix in #668** (condition C-2) |
| A-3 | code gap, smaller | HDE Governance §2.0.19 "Close report minimal content" requires literal canon-pointer fields when a close report closes a TI item: a `TI-<id> pointers:` line and an `ADR status line:` line (plus `PF09 pointers:` for an Epic). The v2 renderer writes its own tracked-issue format | writer lines 2610–2620 render "pointer …" or "ADR status …" | **Fix in #668** (condition C-3) |
| T-1 | text | §6's coverage clause says "the criterion IDs are read from that document". The writer reads requirement IDs from the document; criterion IDs come from the source and must each be one of them, for any decision. Item 4 also never introduces the binary decision and posture, and leaves out that `SATISFIED` needs every acceptance row met and no follow-ups, while `NOT SATISFIED` needs a follow-up | writer `_requirement_ids`, `REQUIREMENT_ID_UNBOUND`, `REQUIREMENT_COVERAGE_INCOMPLETE`, `DECISION_CONTRADICTION` | Redline R-1 |
| T-2 | text | §6 says "an ADR status whose ID the drain-targets ledger names". The writer checks the deferral's or tracked issue's own `id` against the ledger; the `adr_status` text is not checked | writer lines 2419–2426 | Redline R-2 |
| T-3 | text | The ADR says the v2 block names the QA step-logs manifest "only as a canonical pointer", and item 5 presents `key_outputs` as paths only. Every key output other than the close report and manifest must also be a bound, digest-checked evidence input (`OUTPUT_BINDING_MISMATCH`) | writer, `key_outputs` binding check | Redline R-3 |
| T-4 | canon table | Five canon homes are missing from "Affected canon and drainage consequences" (Change Process Guide §1.0.5 requires the ADR to name affected canon): HDE Governance §2.0.19 and Appendix D.0; Change Process Guide §3.5.4; HDE Schemas & Artifacts §8.17 ("New standardized evidence families", "Current-state evidence") and §8.17.1; Glow QA Guide §3.4.3; HDE Mechanics Guide §37.2's epic-scoped filename list and §37.3's `key_outputs` rule | canon read on `main` (§6) | Redline R-4 |
| P-1 | process | The close-run family is a new recurring QA evidence family. HDE Schemas & Artifacts §8.17 says such a family "MUST be introduced via Glow HD Engine Build Notes addendum (or the owning PF canon home)". The same section forbids tools to "infer run state by enumerating subdirectories under audit/qa/<id>/", which the updater does for `close/`. No PF10 addendum introduced the family | PF12 §8.17; updater close-run reconciler | **Introduced by addendum 2.15**, with a scoped exception for its own membership |
| P-2 | process | The proposal has the PR-35 agent write the ADR's approval status line. Instruction ID-12 says "no agent marks the ADR approved" | proposal §6; instruction ID-12 | Addendum 2.15 states the status text and directs the PR-35 session to apply it as a transcription of the Product Owner's decision |
| P-3 | proposal text | Option C pre-decides exceptional closure and a revert. Plan v1.1 §9 item 5 leaves exceptional closure to a separate Product Owner decision under Change Process Guide §3.5.1 | proposal §4 | Moot: option C was not chosen. Recorded for the record |
| P-4 | proposal text | The proposal cites "result records v1.2, v1.3 and v1.5"; v1.5 exists only from `45e4cef` | branch history | Noted; no change needed now |

**Not findings.** The two stated limits added in PR-35 (pinned formats only, with a refusal for anything else; the pointer check does not judge whether a section demonstrates closure) leave no P1 on a real input unfixed. They are pinned inputs with one refusal, as addendum 2.11 rules 5 and 6 allow and addendum 2.14 rule 3 permits. Every concrete claim of Decision items 1 to 8 checked out against the code. The HDE-EPIC039 posture holds: one writer; `--source` with exactly one of `--write` or `--check`; report first and manifest last; `manifest → report → manifest` reads; mixed-state refusal; no hosted feedback.

**This reviewer's own omission.** Instruction v1.0 §4.1 mapped canon elements C1 to C7, but it did not list Change Process Guide §3.5.4 or HDE Governance §2.0.19, so the plan and the code missed A-1 and A-3. A-1 to A-3 are corrections within S21's acceptance intent ("a canon-conforming close report"), in files already in the unit's bounded set. They need no rescope.

## 4. Conditions of the approval (applied in #668 by the PR-35 session)

- **C-1. ADR block.** The v2 schema gains a required, non-empty list of ADR-block entries. Each entry carries the fields Change Process Guide §3.5.4 lists: label, statement, decision point, options considered (when more than one), bounding PF titles, final decision, canonical or change-specific, and doc-delta targets by PF title. An optional closure-override entry enumerates accepted gaps, as §3.5.4's "Closure override" requires. The renderer writes them as an "ADR block" section of the close report, with titles-only canon references. Tests cover a rendered block, a missing block refused, and the feedback refusal on its text.
- **C-2. The current approved Specification.** `requirements_binding` must name the tracked file `docs/ephemeral/<change-id>-specification-v<N>.<N>-approved.md` of the source's own change, at the highest version tracked. Any other document is refused with one typed code. Both real approved Specifications on `main` follow this pattern (`HDE-CRD-0002-specification-v1.1-approved.md`, `HDE-EPIC040-specification-v1.1-approved.md`). Tests cover the real v1.0 refused and v1.1-approved accepted.
- **C-3. TI canon-pointer lines.** A tracked-issue item renders HDE Governance §2.0.19's literal fields: `TI-<id> pointers:` for a pointer item, and `ADR status line:` for an ADR-status item. Tests cover both forms.
- **C-4. ADR text.** Redlines R-1 to R-4 (§5) replace the proposal's §6 delta. The ADR also records C-1 to C-3 in its Decision section.
- **C-5. Status line.** After C-1 to C-4 are pushed, the PR-35 session sets the ADR's status line to the text addendum 2.15 gives, as a transcription of the Product Owner's decision.
- **C-6. Validation.** The negative controls, the writer test file, the updater consumers, and the evidence and qa lanes run locally before one push. Hosted CI and a fresh Codex review run on the resulting head. Every P1 finding on a real input is fixed (addendum 2.14).
- **C-7. Ceiling.** The work stays in the PR-35 session. A projected pass of the ceiling returns to the Product Owner first (addendum 2.11 rule 3; 2.14 rule 5).

## 5. Redlines to the ADR

These replace the proposal's §6 delta.

- **R-1 (Decision item 4, acceptance).** Replace "an exact-source acceptance section that binds each criterion ID to a tracked requirements document, to tracked evidence and to a result and limitation;" with: "the binary `SATISFIED` / `NOT SATISFIED` closure decision with its posture; an exact-source acceptance section that binds each criterion ID to the change's current approved Specification, to tracked evidence and to a result and limitation. The writer reads the requirement IDs from that Specification in the change kind's pinned format and refuses a document without it. Every criterion ID must be one of those IDs. `SATISFIED` needs an acceptance row for every ID read, every row met and no follow-up; `NOT SATISFIED` needs at least one follow-up;".
- **R-2 (Decision item 4, deferrals and tracked issues).** Replace "deferrals with a drain target or ADR status; … the tracked-issue mapping;" with: "deferrals, each with a drain target, or with an ADR status and rationale, in which case the deferral's ID occurs in the drain-targets ledger; … the tracked-issue mapping in HDE Governance's literal `TI-<id> pointers:` and `ADR status line:` fields, each item either a pointer to a Markdown heading in a bound tracked evidence input or an ADR status, in which case the item's ID occurs in the drain-targets ledger; the ADR block that Change Process Guide §3.5.4 requires;".
- **R-3 (Decision item 5; "HDE-EPIC039's neutral writer, weighed").** Add to item 5: "Every key output other than the close report and the close manifest is also a bound tracked evidence input, so its digest is recorded (`OUTPUT_BINDING_MISMATCH` otherwise)." In the weighed section, replace "names the QA step-logs manifest only as a canonical pointer" with "binds the QA step-logs manifest as a tracked input and names it as a canonical pointer".
- **R-4 (Affected canon table).** Add rows:
  - HDE Governance §2.0.19 ("Close-pack baseline artifacts", "Close report minimal content (normative)", "Close-pack manifest `key_outputs` shape (normative)") and Appendix D.0: the CRD prefix beside `EPIC-###`, the v2 producer, the TI fields;
  - Change Process Guide §3.5.4 "ADR block in the close-pack (all epics)": the v2 report's ADR block;
  - HDE Schemas & Artifacts §8.17 ("New standardized evidence families", "Current-state evidence") and §8.17.1: the close-run family as a post-verdict family whose membership is its validated primaries, introduced by Build Notes addendum 2.15;
  - Glow QA Guide §3.4.3 "Evidence layout: current-state first": the same family beside `checks/`;
  - HDE Mechanics Guide §37.2's epic-scoped filename list and §37.3's `key_outputs` rule: the CRD filename form and the v2 `key_outputs` minimum.

## Canon relied on

Read on `main` at `390bc99` (`docs/pfcanon/` unchanged there since `043fa91`), with PF10 read on #668's branch.

In-flight documents read: the AQ-1 proposal v1.0 (at `45e4cef`); Specification v1.1-approved (S21, constraint "Close-pack writer", Exclusions) and Specification v1.0 (its `S` rows, for A-2); Implementation Plan v1.1 §7 WU-PR-07, §9 item 5, §11 R-4 and §13; WU-PR-07 instruction v1.0 §4.1, ID-5, ID-8, ID-12; rescope review v1.0 §6; PR-35 result records v1.0 to v1.5.

| Topic | Sources |
| :- | :- |
| ADR required; affected canon and drainage | PF06-Canon-Change-Process-Guide v2.5.4 §1.0.5 |
| Close report content | PF06 §3.5.2.1 and §3.5.4 (read in full); PF04-Canon-HDE-Governance v2.8.7 §2.0.19 (close-pack baseline, close report minimal content, `key_outputs` shape; read in full) |
| CRD close-pack identity | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §1.2 "Change-container compatibility (normative)" |
| New evidence family; current-state rule | PF12 §8.17 ("New standardized evidence families (MUST)", "Current-state evidence (normative)", read in full) and §8.17.1; PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.3 (located; as the workflow's verifiers quoted it) |
| `key_outputs` | PF12 §1.2 "Close-pack manifest key_outputs"; PF14-Canon-HDE-Mechanics-Guide v3.5.8 §37.2 and §37.3 |
| Business case, real inputs, finding disposition, P1s | PF10-HDE-Build-Notes v13.6.5 addenda 2.11 (rules 3 to 8), 2.13 and 2.14 |
| Decision owner and timing | Implementation Plan v1.1 §13 AQ-1, §11 R-4, §9 item 5; instruction v1.0 ID-12; PF04 §9.7.3 (ADRs are Product Owner-owned; agents draft) |
| HDE-EPIC039 posture | `AGENTS.md` "HDE-EPIC039 current workflow posture"; PF20-Reference-HDE-Phased-Epics v1.9.6 HDE-EPIC039 D5 |

Silence: canon prescribes no ADR status vocabulary beyond "approved ADR" (PF06 §1.0.5). The status text in addendum 2.15 uses "Approved" to match it.
