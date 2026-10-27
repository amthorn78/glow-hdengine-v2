---
artifact_type: IMPLEMENTATION_PLAN_REVIEW
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: INITIAL_PLAN_REVIEW
decision: INITIAL_DENY
reviewed_artifact: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md
reviewed_artifact_version: "1.0"
reviewed_artifact_blob: b0eefc0bd68eb67ee58d667602864c266db18458 (61,599 bytes; landed on main at 2fb81892, amthorn78/glow-hdengine-v2#619)
reviewed_artifact_state_after_review: PLAN_PENDING (unchanged; sentinel remains "ASK OK?")
audit_ref: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c; 119,180 bytes)
specification_ref: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
specification_reviewed_source: docs/ephemeral/HDE-CRD-0002-specification-v1.1.md (blob 8a3ef0a8930dcb6f610235ee84d68882bfaa80e1)
thoth_decision_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md (INITIAL_APPROVE, 2026-10-12T19:39:51Z)
reviewer: Isis, continuing Lead Developer and independent whole-change Implementation Plan reviewer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; the session that authored the Specification; reviewer binding assigned at this boundary as review v1.1 §6 provides)
ia_author: whole-change Implementation Agent for HDE-CRD-0002 (session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; author of the Audit and the Plan)
prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c)
prompt_release: GCFPE-20261009.1 / 100926.1
release_selection_check: GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", exactly 55 members, selected 2026-10-12 by Nathan / Product Owner; read 2026-10-12 (the current-selection section only)
created_at: 2026-10-12T20:44:49Z
repository_head_read: origin/main 2fb81892
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (unchanged since the Specification reads; addendum 2.1 only)
approved_base_plus_overlays: Specification v1.1 (approved) + PF10 overlays NONE
pf10_addendum: none (INITIAL_DENY produces no addendum)
next_prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
next_mode: PREAPPROVAL_PLAN_REVISION
next_actor: the same whole-change IA (session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah)
---

# HDE-CRD-0002 — Implementation Plan review v1.0 (IA-30)

## 1. Decision

**INITIAL_DENY.** Implementation Plan v1.0 is not approved. It stays `PLAN_PENDING` with `ASK OK?` and returns to its author, the same whole-change IA, through IA-40 in `PREAPPROVAL_PLAN_REVISION` mode. Four required redlines are given in §2 and §3.

The Plan is close to approvable. Its architecture, invariants, traceability, unit order, re-cut method, Ops unit and QA-readiness route are sound (§5). Each redline is a place where the Plan, as written, would:
- implement behavior that contradicts governing canon (R1, R4);
- let QA start on a requirement that cannot yet hold (R2); or
- leave the change's own closing path unproven (R3).

This decision creates no PF10 addendum. It authorizes no PR Instruction, implementation, Ops, QA, canon change, ADR approval, acceptance or closure.

**REVISE AND RESUBMIT**

## 2. Required redlines (summary)

| # | Plan v1.0 anchor | Defect | Consequence if unchanged |
| :- | :- | :- | :- |
| R1 | §5 IF-10 row; §5 IF-6 row (the `/reader` clause); §7 WU-PR-03 acceptance (2) | Dev `GET /reader` is gated on `APP_ENV` in `{dev, test, local}`, and the catalog row's `env_gate` is rewritten to match. Canon gates this route on explicit `APP_ENV=dev` | WU-PR-03 would serve the dev Reader for `test` and `local` and write a catalog row that contradicts normative canon. Both are execution behavior and governed-artifact meaning, not wording |
| R2 | §7 WU-PR-07 dependencies; §9 items 1, 4 and 5; §11 R-4; §13 AQ-1 | The S21 ADR decision (AQ-1) is due only before a Close Gate relies on S21, and is stated not to gate WU-PR-07's merge or QA entry | Two consequences. (a) WU-PR-07 merges an evidence family into the canonical updater that only an approved ADR may admit. (b) QA can start while S21's acceptance intent ("the accompanying ADR is approved") and the Distillation completion boundary cannot hold |
| R3 | §7 WU-PR-07 (no terminal-state statement); §9 item 5 | The Plan does not state the ordered path from the QA verdict to the final close-mutation-set bytes. Nor does it say whether the updater and the close-pack writer bind each other without a cycle | The reviewer cannot establish terminal-state reachability, which PF27 requires for Implementation Plan review. That path is the failure S21 exists to remove (CC-1, CC-2) |
| R4 | §4 invariant 6; §5 IF-3; §15 | The CRD close-pack filename prefix is `CRD-0002` (`CRD-NNNN`). Canon makes the CRD ID itself, `HDE-CRD-0002`, the prefix | The S21 writer would emit HDE-CRD-0002's close pack at a non-canonical filename, and the close-pack baseline check would fail |

## 3. Required redlines (detail)

Each item names the exact target in `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md`, the operation, the replacement or addition, the reason and the linked edits. Where a correction needs a design choice the Plan has not made, the item names the content the IA must supply and does not design it (Plan Templates, "Source-bound review authority and exact-fix limits").

### R1 — Gate dev `GET /reader` on explicit `APP_ENV=dev`

- **Defect.** IF-10 serves `GET /reader` "only for normalized `APP_ENV` in `{dev, test, local}` … (the `_dev_admin_gate` semantics)". IF-6 changes the `/reader` rows' `env_gate` to `APP_ENV in {dev,test,local}`. WU-PR-03 acceptance (2) tests that `test` and `local` are served.
- **Controlling source.**
  - HDE-CLI-API-Vendor-Ref §5.6, "Endpoint Catalog (JSON success)", transport-facts table, `/reader` row: "internal dev-harness; explicit `APP_ENV=dev`; production public enablement is a separate change".
  - HDE Schemas & Artifacts, Endpoint Catalog, "Reader surface routes and distinct contracts (normative)": "The existing development Reader v1 surface is `GET /reader` (with its defined HEAD behavior), explicitly gated by `APP_ENV=dev`."
  - HDE Governance §9.1.2: "For a real contradiction … Follow the governing PF position immediately."
  - The in-flight precedence rule (HDE Governance §9.1.2; Plan Templates, "Canon precedence for template use"): PF-Canon governs an in-flight document where they conflict. No PF10 addendum or Product Owner rescope applies here.
  - The `{dev, test, local}` set is canon for the other dev routes in the same §5.6 table (`/internal/dev/sampler`, `/dev/*/conjunction`), not for `/reader`.
- **Verified repository fact (main `2fb81892`).**
  - `docs/ENDPOINTS_CATALOG.json` rows `GET /reader` and `HEAD /reader` carry `env_gate: APP_ENV=dev` today.
  - `adapter/http_reader.py` line 603 serves when `APP_ENV` is unset or exactly `dev`.
  - `_dev_admin_gate` (lines 817–823) admits `{dev, test, local}` for the sampler and conjunction routes.
- **Why no Specification change is needed.** S10's acceptance intent reads: "The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses."
  - That is a necessary condition. A gate that serves only explicit `dev` satisfies it: every served request has `APP_ENV` in the named set, and unset refuses.
  - The "Dev route" constraint ("must not break dev, test or local use of `/reader`") is also met. The route refuses `test` and `local` today, so no existing use breaks.
  - The Plan therefore chose, within IA authority, the reading that contradicts canon. The canon-conforming reading is equally within that authority.
  - The wording that invited the wider reading is the Specification's, and Isis authored it.
- **Material consequence.** The serving behavior of a route mounted on the production factory, and the meaning of a governed catalog row, would contradict normative canon. QA and later reviews read both against canon.
- **Required correction.**
  1. §5, IF-10 row. Replace the third cell with: "`GET /reader` (and its defined HEAD behavior) served only when `APP_ENV` is explicitly `dev`; unset, empty and every other value, including `test` and `local`, refuse with `ERR_READER_FORBIDDEN` 403 (HDE-CLI-API-Vendor-Ref §5.6; HDE Schemas & Artifacts \"Reader surface routes and distinct contracts (normative)\"); `scripts/dev_start_reader.sh` defaults `APP_ENV=dev`."
  2. §5, IF-6 row. Replace "`/reader` rows' `env_gate` becomes `APP_ENV in {dev,test,local}`;" with "`/reader` rows' `env_gate` stays `APP_ENV=dev`;".
  3. §7, WU-PR-03, Acceptance and verification item (2). Replace "`GET /reader` is served for `dev`, `test`, `local` and refused (403, `ERR_READER_FORBIDDEN`) for unset, `prod`, `production`, `live` and arbitrary values;" with "`GET /reader` is served for `APP_ENV=dev` and refused (403, `ERR_READER_FORBIDDEN`) for unset, empty, `test`, `local`, `prod`, `production`, `live` and arbitrary values;". Keep the rest of item (2) unchanged.
  4. §15, append one sentence: "S10 is implemented as an explicit-`dev` gate: the Specification's acceptance intent states a necessary condition that this gate satisfies, and HDE-CLI-API-Vendor-Ref §5.6 and HDE Schemas & Artifacts \"Reader surface routes and distinct contracts (normative)\" require explicit `APP_ENV=dev` for this route (HDE Governance §9.1.2); serving `test` or `local` would need a canon change this CRD excludes, so no canon conflict is opened."
- **Linked edits.** None elsewhere in the Plan.
  - The Audit's S10 "Required behavior" sentence and EC-4 refer to `_dev_admin_gate` semantics. For the gate's value set, this review supersedes them within its scope (HDE Governance §9.1.2: reviews govern within their scope).
  - IA-40 revises the Plan only; no Audit revision is required.
  - EC-4's dev-runner default (`APP_ENV=dev`) stands.

### R2 — Decide the S21 ADR (AQ-1) before WU-PR-07 merges

- **Defect.** The Plan states the S21 ADR decision does not gate WU-PR-07's merge or QA entry, in four places:
  - §7 WU-PR-07 dependencies: "the ADR's approval gates reliance on the writer's output, not this unit's merge";
  - §9 item 4: "the S21 ADR's approval is a Close Gate prerequisite, not a QA-entry prerequisite";
  - §13 AQ-1: "does not gate this Plan, WU-PR-07's merge or QA entry", with the stage deadline "Before any Close Gate relies on S21's output";
  - §11 R-4: "S21 ADR unapproved when HDE-CRD-0002 reaches closure".
- **Controlling source.**
  - Specification Exclusions bullet 3: "No new evidence family, acceptance token or token matrix, except a home for close-workflow run evidence that S21's ADR admits (S21)."
  - S21 acceptance intent: "… the accompanying ADR is approved".
  - Distillation completion boundary: "… S19 to S22 hold on `main`, and S21's ADR is approved".
  - Change Process Guide §1.0.5: "A CRD that changes a canonical rule, contract, schema, process, interpretation, permanent policy, or governed-artifact meaning MUST have an accompanying approved ADR … A CRD Specification alone does not authorize canon supersession."
  - Change Process Guide §1.0.6: QA verifies the CRD's requirements; closeout needs the ADR decision.
- **Material consequence.**
  - (a) WU-PR-07 adds the IF-4 family to the canonical updater, the sole Index/Mirror writer. Merged with the ADR still `Proposed`, `main` would carry an evidence family that no approved ADR admits, which Exclusions bullet 3 forbids. If the Product Owner then chooses AQ-1 alternative (b) or another home, the merged code and its evidence model need reverting.
  - (b) QA-10 and the QA verdict would test S21 against an acceptance intent that cannot hold while the ADR is undecided. The result is a predictable S21 failure and a remediation loop with no code defect behind it.
- **Required correction.**
  1. §7, WU-PR-07, Dependencies and order. Replace the bullet's text with: "Seventh; after WU-PR-02 (updater model). The ADR draft is a deliverable of this unit; the Product Owner decides AQ-1 before merging it, because the IF-4 family admission creates the close-run evidence family that Exclusions bullet 3 permits only as S21's ADR admits it, and Change Process Guide §1.0.5 requires the accompanying approved ADR. If the decision differs from the draft, this unit is revised to the approved decision before merge (RS-10 where the decision changes the unit's bounded scope). S21 completes before HDE-CRD-0002's ordinary Close Gate."
  2. §9 item 1 (Entry). After "WU-OPS-01 is planned (OPS-10) or executed", insert ", and AQ-1 is decided".
  3. §9 item 4. Replace "the S21 ADR's approval is a Close Gate prerequisite, not a QA-entry prerequisite;" with "the S21 ADR's approval (AQ-1) is decided before WU-PR-07 merges, and so before QA-10, because S21's acceptance intent and the Distillation completion boundary include it;".
  4. §9 item 5. Replace "HDE-CRD-0002's own close pack is produced by the S21 writer after the ADR is approved (AQ-1); if the ADR is not approved by then, the ordinary Close Gate is not available and the Product Owner decides" with "HDE-CRD-0002's own close pack is produced by the S21 writer; AQ-1 is decided before WU-PR-07 merges. If the Product Owner declines the ADR, S21 does not hold, the ordinary Close Gate is not available, and the Product Owner decides". Keep the rest of the item.
  5. §11, R-4 row. Risk: "S21 ADR undecided when WU-PR-07 is otherwise ready to merge." Unit: "WU-PR-07". Treatment: "WU-PR-07 does not merge without the decision (§13 AQ-1); units ordered after it wait with it."
  6. §13, AQ-1 row. Effect: "Gates WU-PR-07's merge, and so QA verification of S21 and the Distillation completion boundary; does not gate this Plan or WU-PR-07's preparation and review." Stage deadline: "Before the Product Owner merges WU-PR-07."
- **Linked edits.**
  - The Audit's §7.2 and §8 AQ-1 deadline text is superseded by this review for the decision's timing. No Audit revision is required.
  - §16 `open_question` stays "AQ-1 (Product Owner; non-blocking for review)".

### R3 — State the S21 terminal-state reachability path

- **Defect.** WU-PR-07 proves pieces separately:
  - a dry-run close pack into `tmp_path`;
  - the retained feedback-dependency refusal;
  - a non-writing check mode;
  - an IF-4 publication under a fixture root.

  Neither WU-PR-07 nor §9 item 5 states the ordered path by which a real close mutation set reaches its final tracked bytes. The missing points are:
  - who produces the same-run close-workflow evidence, and in which venue (a local close session, or a hosted workflow whose output would have to be written back);
  - in which order the canonical updater and the writer run;
  - whether the Index indexes the close report and manifest, as it does for earlier close packs;
  - whether the manifest's `key_outputs` or evidence inputs bind the Index;
  - why those two bindings form no cycle.
- **Controlling source.**
  - Plan Templates, "Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review)": "Terminal-state reachability: identify the claimed terminal state and prove a feedback-free path from repository-local inputs to the tracked candidate bytes", with "Execution-surface feasibility", "Rails consistency" and "End-to-end proof".
  - Change Process Guide §3.5.1, "Feedback-free terminal lifecycle".
  - Change Process Guide §3.5.2.1 (close-pack files) and §3.5.2.3 (Index and Mirror trio in the same mutation set).
  - Glow QA Guide, "Close-pack truthfulness and same-run execution (normative)": same-run mechanical evidence under the QA root, and coherent refresh of the close-pack family, including the Human Index and Machine Mirror.
- **Verified repository fact (main `2fb81892`).** `tools/evidence/update_evidence_index.py` registers earlier close packs as Index rows (for example `epic022.close_report` → `audit/EPIC-022_close_report.md` and the matching `_MANIFEST.json`, lines 354–360). The updater/writer ordering question is therefore real.
- **Material consequence.**
  - S21's purpose and the Specification's Expected outcome are that "the ordinary Close Gate is available to HDE-CRD-0002 and later changes".
  - HDE-EPIC040 needed exceptional closure because no feedback-free path existed (CC-1, CC-2).
  - Without the stated path, this review cannot establish reachability, and WU-PR-07 could merge a writer whose real close sequence still needs a source → CI → source back-edge.
- **Required correction.** This adds content; the design choices are the IA's.
  1. §7, WU-PR-07. After the Deliverables bullet, add a bullet headed **Terminal-state reachability.** It states, from the IA's own design:
     - (a) the claimed terminal state: the close mutation set's tracked bytes (close report, manifest and its path proof at the canonical filenames, the close-run evidence family, and the Index trio), complete before hosted validation;
     - (b) the ordered transitions from the recorded QA verdict to those bytes, each with its producing tool, inputs, rails and authorization;
     - (c) the actor and venue that run the same-run close workflow whose evidence enters the close-run family;
     - (d) whether the Index indexes the close report and manifest, and whether the manifest binds the Index, with the reason the result has no cycle;
     - (e) that hosted CI validates those exact bytes in check modes and writes nothing the final state needs (Change Process Guide §3.5.1).
  2. §7, WU-PR-07, Acceptance and verification. Add item (7): "An end-to-end rehearsal of the stated transition sequence for a synthetic `HDE-CRD-0002` candidate in a throwaway copy of the repository ends with the writer's check mode, `tools/evidence/update_evidence_index.py --check`, `ci/checks/check_mirror_schema.sh` and `ci/checks/check_evidence_index_hash.sh` exiting 0; a second run of the sequence is byte-stable; no byte the final state needs is produced by hosted CI."
  3. §9 item 5. Append: "The path is the one WU-PR-07 states under Terminal-state reachability."
- **Linked edits.** If the stated design puts any close-run evidence or close-pack byte in hosted CI's output, the unit must change its design. The plan may not adopt such a path (Change Process Guide §3.5.1).

### R4 — Use the CRD ID as the close-pack filename prefix

- **Defect.**
  - Invariant 6: "close-pack prefix `CRD-0002`".
  - IF-3: "mapped to the filename prefix (`EPIC-NNN` / `CRD-NNNN`)".
  - §15: "close-pack prefix `CRD-0002`".

  The writer would emit `audit/CRD-0002_close_report.md` and `audit/CRD-0002_MANIFEST.json`.
- **Controlling source.**
  - HDE Schemas & Artifacts §1.2, "Change-container compatibility (normative)": "For a CRD, the stable CRD ID recorded in PF30 replaces `EPIC-###` as the filename prefix in the baseline suffix patterns below".
  - HDE CRD Records: "The canonical top-level CRD ID syntax is `HDE-CRD-<NNNN>`".
  - CR-3's interim treatment: the CRD ID is the Product Owner-assigned `HDE-CRD-0002`.
  - Change Process Guide §3.5.2.1: the close pack lives at its canonical filenames.

  The Epic prefix `EPIC-###` is a filename form distinct from the Epic ID. For a CRD, canon substitutes the ID itself. No repository precedent exists (`audit/` holds no CRD close pack).
- **Material consequence.** A canonical artifact identity would be wrong for the first CRD close pack. The close-pack baseline verification and the report's verification statement would bind the wrong filenames.
- **Required correction.**
  1. §4 invariant 6. Replace "close-pack prefix `CRD-0002`" with "close-pack filename prefix `HDE-CRD-0002` (`audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json`)".
  2. §5 IF-3. Replace "mapped to the filename prefix (`EPIC-NNN` / `CRD-NNNN`)" with "mapped to the filename prefix (`EPIC-NNN` for an Epic; the CRD ID itself, `HDE-CRD-NNNN`, for a CRD)".
  3. §15. Replace "close-pack prefix `CRD-0002`" with "close-pack filename prefix `HDE-CRD-0002`".
- **Linked edits.** None in the Plan. The Audit's §6 S21 "(`EPIC-NNN` / `CRD-NNNN`)" mapping is superseded by this review for the CRD prefix; no Audit revision is required.

## 4. Non-gating notes (no correction required)

- **N1 — Same-version manifest refreshes.** §3, §10 and R-8 refresh `catalog/manifest.json` at `1.3.0` in each member-changing unit before the single `1.4.0` cut. `main` will carry several distinct `release_id` values labelled `1.3.0`.
  - Precedent exists: `catalog/manifest.json` stayed `1.0.0` / `2025-12-26T00:00:00Z` across #403, #404 and #467, and PR06a re-cut in-PR at the same version.
  - OPS01's `1.3.0` verification refers to the pre-CRD `release_id`.
  - The Plan already requires each PR result record to name its refreshed `release_id`.
- **N2 — Retirement criterion in WU-PR-01.** S03 allows "fixed or retired with their files". Several failing uncovered files test surfaces this CRD changes:
  - `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py` and `tests/provider/test_vendor_and_prod_guard*.py` (S14's environment classification);
  - `tests/adapter/test_gate_auth.py` (S10).

  The PR-20 detailed plan should state when a failing file of current behavior is fixed rather than retired. The Plan's "never skip, disable or quarantine a test to get green" stands.
- **N3 — §9 item 3 parenthetical.** "S15 catalog-only after EC-8" sits inside the functional-feature list. §6 and Audit §7.4 classify S15 correctly ("catalog entries only"). One live vendor call satisfies the class either way.
- **N4 — Override actor principal and sink key.** IF-2 and EC-7 take the actor from the OS principal and defer the sink key's name to PR-20. That is consistent with CLI/API/Vendor Ref §7.1.11f ("authenticated OS/control-plane principal"). The PR-20 plan and the QA Plan establish that the Live QA venue yields a stable authenticated principal (§7.1.11e); R-3 already carries this.
- **N5 — `/aux/narrative` catalog row.** It follows the CLI/API/Vendor Ref §5.6 projected record ahead of HDE Schemas & Artifacts registration of `public_aux` and `aliases`. R-7 already records that no catalog conformance is claimed.
- **N6 — Board card.** The Notion card for HDE-CRD-0002 is still stale for its owner (Audit N-1). This session writes no Notion row.

## 5. Reviewed and found sound

| Area | Finding | Basis |
| :- | :- | :- |
| Lineage and authority | Same IA author and session as the Audit. Approved Specification, Thoth decision, PF10 v13.5.2 with no overlay, and CR-1 to CR-3 are carried. The Plan claims no authority it lacks | HDE Governance §9.1.1; IA-30 `INITIAL_PLAN_REVIEW` inputs |
| Requirement coverage | S01–S22, CD-1 to CD-3 and RD-1 each map to exactly one unit or to a stated non-delivery; no requirement is expanded | Specification v1.1 (approved); Plan §6 |
| Phase separation and order | Each unit sits in one Specification phase block, and no unit mixes DEV and OPS. The order honors every Specification phase-block dependency: S03–S05 together and first; S20 after them; S22 before QA; S21 before the Close Gate; member-changing work before the version bump. 8 PRs, within the 10-PR route | Change Process Guide §1.0.4 and §3.5.1; Plan Templates §2A "Alchemical phase separation" |
| Release identity | The re-cut method (§10) follows the admission byte binding and the observed PR06b order. Admission constants change once, in WU-PR-08 | `AGENTS.md` "Release identity" and HDE-EPIC040 admission addition; Audit §5.1, §7.3 |
| Vendor override interfaces | IF-1 and IF-2 match §7.1.11a–f, checked line by line: the flag regex; `APP_ENV`/`ENGINE_ENV` rules and both allow-lists; the eight-row matrix; the seven-step order; exit 64 versus exit 1; the audit fields and exclusions; `PROVIDER_AUDIT_UNAVAILABLE` | CLI/API/Vendor Ref §7.1.11 (read in full) |
| Ops unit | WU-OPS-01 carries Owner PO, Facilitator IA, Executor PO or delegated agent, PF07-derived facts with locators, a bounded PF07 gap (deployment trigger, build command), classification, secret posture, rollback intent and nonclaims, labelled "PO-only execution, IA-guided" | Plan Templates §3 "Ops Task Record" |
| Live QA | The classes match the Specification's table. The mandatory live vendor call and the §7.1.11e initiator are carried to the QA Plan, which designs them | Glow QA Guide §3.5.5; Change Process Guide §1.1.5A |
| Exclusions and conflicts | The Specification's exclusions are carried with none added. CR-1 to CR-3 interim treatments are applied. No PF update is made a deliverable | Plan §12, §15; HDE Governance §9.7 planning posture |
| Facts re-checked on main `2fb81892` | `update_evidence_index.py` lines 47–51 (single CRD admission); `qa_harness.py` line 23; `adapter/http_reader.py` line 603 and `_dev_admin_gate`; the catalog's `/reader` rows; the manifest's version history; the updater's close-pack Index rows | Repository read |

## 6. Next state and routing

- **Plan v1.0:** `PLAN_PENDING`, `ASK OK?`; not approved and not edited by this review.
- **Next:** IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1, `PREAPPROVAL_PLAN_REVISION`, by the same whole-change IA. It produces a complete successor pending Plan with an item-by-item application report for R1–R4, then returns to IA-30 `INITIAL_PLAN_REVIEW` with Isis as the same reviewer.
- **PF10 addendum:** none.

## 7. TypeSafe reading for the receiving session (IA-40)

Action sent (v6): "Revise a 62 KB initial change-wide Implementation Plan that an independent reviewer denied with four bounded required redlines, producing a complete successor pending Plan and an item-by-item application report: change a dev route's environment gate in two interface rows and one acceptance item to match canon; move a Product Owner ADR decision earlier in the unit order, QA-readiness route, risk and decision tables; add a terminal-state reachability statement and one end-to-end acceptance rehearsal for a close-pack writer unit, using the author's own design for the order of evidence-index and close-pack writes; and correct a canonical close-pack filename prefix in three places. No code is written and no live run occurs; the same reviewer re-reviews the revision."

- **TypeSafe v6: Opus 5.5, high.** Effort score 1.93 (confidence 0.85); rung probabilities low 0.00, medium 0.15, high 0.77, extra high 0.08, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.98 (confidence 0.96). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.15, Opus 5.5 at high 0.75, Opus 5.5 at extra high 0.08, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-12T20:44:45Z. Flags: none.
- **Detail:** v6 sent 2026-10-12T20:44:45Z; HTTP 200 in 0.69 s; 4260 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- **Nathan's pick for IA-40:** not stated.
- **Nathan's pick for this IA-30 session:** not stated (reading recorded in Plan v1.0 §17).

**Surface advice:** run IA-40 in the same whole-change IA lineage as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. It reads this review, Plan v1.0, the Audit and `docs/pfcanon/` on `main`. For R3 it re-reads `tools/evidence/update_evidence_index.py` (close-pack Index rows), `tools/qa/generate_epic_close_pack.py` and `.github/workflows/epic-closeout-validation.yml`. It writes only the successor Plan and its application report under `docs/ephemeral/`. It needs no live vendor, production or database access. This review's PR should be merged to `main` first.

## Canon relied on

Read on `main` at `2fb81892`. `docs/pfcanon/` is unchanged since `df23bbf` (#614). Sections were read in full unless marked otherwise. Each decision topic maps to its sections below.

- **Review authority, mode and outcomes:**
  - PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (the Plan's content; Isis reviews; the IA must not expand or reinterpret the Specification);
  - §9.1.2 "Canon precedence and persistent sources" (governing PF position on contradiction; in-flight documents and reviews govern within scope);
  - IA-30 and IA-40 at 100926.1 (modes, redline contract, routing).
- **Materiality and the reviewer's limits, for every finding:** PF27-Canon-Plan-Templates v2.0.5:
  - "Source-bound review authority and exact-fix limits";
  - "Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review)", including terminal-state reachability, execution-surface feasibility, rails consistency and end-to-end proof;
  - "Materiality-based blocker discipline for planning and review artifacts";
  - "Canon precedence for template use" (as quoted in the Plan's header).
- **R1:**
  - PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.6 "Endpoint Catalog (JSON success)" (read in full) and the dev `GET /reader` error-token passage (lines 2325–2329);
  - PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6, Endpoint Catalog, "Reader surface routes and distinct contracts (normative)" (lines 4680–4690);
  - canon search for `/reader` gating across `docs/pfcanon/` (the matching lines in PF02, PF04, PF05, PF07, PF09.4 and PF12 read);
  - the Specification's S10 and "Dev route" constraint.
- **R2:**
  - PF06-Canon-Change-Process-Guide v2.5.4 §1.0.4, §1.0.5, §1.0.6;
  - the Specification's Exclusions bullet 3, S21 acceptance intent and Distillation completion boundary.
- **R3:**
  - PF06 §3.5.1 "Requirement" (including "Feedback-free terminal lifecycle" and "Exceptional closure record"), §3.5.2.1 "Close-pack files", §3.5.2.3 "Index and mirror trio";
  - PF19-Canon-Glow-QA-Guide v3.0.6 "Close-pack truthfulness and same-run execution (normative)" and "Close report requirements" (lines 1115–1140);
  - PF27 terminal-state reachability (above).
- **R4:**
  - PF12 §1.2 "Change-container compatibility (normative)" and "Close-pack artifacts" (lines 583–660);
  - PF30.1-Canon-HDE-CRD-Records v0.9.1, CRD ID syntax (lines 56–60);
  - PF06 §3.5.2.1.
- **Vendor-override interfaces (found sound):** PF05 §7.1.11 and §7.1.11a–f, read in full.
- **Ops unit (found sound):** PF27 §3 "Ops Task Record (Template)": Definition, "Execution authority (normative)", "IA facilitation posture", "Not a PR", "Ops Task record fields".
- **Live QA classes (found sound):** PF19 §3.5.5 "Production-affecting Live QA minimum"; PF06 §1.1.5A (both read for the Specification revision on this date; canon unchanged since).
- **PF10:** PF10-HDE-Build-Notes v13.5.2. Addendum 2.1 governs only the TypeSafe reading in §7; PF10 is silent on the subject matter of R1–R4, so permanent canon governs.
- **Operative documentation:** `AGENTS.md` (canon-first and precedence rule; release identity; sole Index/Mirror writer; dev conjunction routes gated `dev|test|local`).

**Not read; no decision rests on them:** PF23-Canon-Reality-Audits; PF07-Canon-Glow-Infrastructure (WU-OPS-01's PF07 locators were taken from the Audit and Plan, not re-read); PF09 volumes (no PF09 mapping for this CRD, by the Specification's exclusion).

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md` (reviewed artifact);
- `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (compared by line diff with `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md`, which Isis authored and has read in full).

Consulted by search: `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md` (O-P07-04) and `docs/ephemeral/HDE-EPIC040-PR06a-pr35-checkpoint-v1.0.md` (same-version re-cut precedent).

**Prompts read:**
- IA-30 — Review Whole-Change Implementation Plan — 100926.1;
- IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (receiver contract);
- the GCFPE Membership and Release Register, current-selection section.

## 8. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-30 / initial plan review 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md`, v1.0 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | IA-30 — Review Whole-Change Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c |
| role/stage | Isis / IA-30 initial Implementation Plan review |
| capture time | 2026-10-12T20:44:49Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
