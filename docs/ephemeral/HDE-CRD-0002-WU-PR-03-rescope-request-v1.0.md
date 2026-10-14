---
artifact_type: RESCOPE_REQUEST
artifact_id: HDE-CRD-0002-WU-PR-03-RESCOPE-REQUEST
artifact_version: "1.0"
status: RESCOPE_REQUEST_PENDING_REVIEW
approval_sentinel: "ASK OK?"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
items: RP-1 (the dev Reader start helper's APP_ENV default required by EC-4, IF-10 and acceptance (2) conflicts with PF canon); RP-3 (the IF-7 release-label roster keeps a stale label on a byte-stable capture, which fails WU-PR-02's own tests at this unit's refresh; the fix is in the updater, outside instruction §6); RP-2 (convergence step 3b; in scope under the base, no delta requested)
originating_stage: PR-20 — Create Detailed PR Implementation Plan — 100926.1, pre-Proceed planning (no PR_RETURN_PHASE: no Proceed, workspace vehicle or pull request for code exists)
author: originating PR implementation author, the dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (PR-20); authoring session https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002 through RS-20 (the IA issued instruction v1.0 under PR-10 and did not author this request)
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, PENDING; complete except RP-1 and RP-3)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 74e8f158b48d)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, approved; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; blob b39ac9f276db; lineage)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md (v13.5.6; blob 9c5468fb69e4; sha256 8663ab94289adae036dbb07af8b302d1b7f3b1d2a1b57dfb7bbd664a5b98bec0); addenda 2.2, 2.3, 2.5 read in full; no addendum speaks to dev Reader start helpers or APP_ENV defaults (searched)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md §2.2 (WU-PR-03 downstream item), §2.3, §2.5
prior_rescope_proposal_or_review: none for WU-PR-03
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_baseline: origin/main 20f16d06e78e6a2b99ca4527cf92bc3088da9fb1
created_at: 2026-10-14T02:01:29Z
return_point: this PR-20 planning context for WU-PR-03, which writes plan v1.1 (complete successor applying the decision) and presents it at AWAITING_PO_PROCEED
canon_conflict_register: CR-1 to CR-5 carried unchanged; CR-6 PROPOSED by this request (§5)
---

# HDE-CRD-0002 WU-PR-03 — Rescope request v1.0

## 1. Request

The WU-PR-03 PR-20 author asks the whole-change IA for one RS-20 decision on three items. RP-1 and RP-3 each block a complete plan; RP-2 is recorded for the reviewer's confirmation only.

| Item | Approved-base text | Boundary | Requested decision |
| :- | :- | :- | :- |
| RP-1 | EC-4 (Audit §7.1, carried by Plan v1.1): "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev` when unset; `docs/server/reader_v1.md` states it." IF-10 (Plan v1.1 §5), last clause: "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev`." Acceptance (2) (Plan v1.1 §7 WU-PR-03), last clause: "`scripts/dev_start_reader.sh` without `APP_ENV` starts a serving runner." | Five controlled PF canon documents (six binding passages, §2.1) require that dev Reader start helpers propagate `APP_ENV` exactly as supplied and never default it (§2). No PF10 rule and no Product Owner disposition supersedes them. Under `AGENTS.md` and HDE Governance §9.1.2, canon governs the in-flight Plan. Implementing canon leaves acceptance (2)'s last clause unmet; implementing the clause breaks canon | APPROVE the bounded delta of §3, or classify `IN_SCOPE_REPAIR` if the IA reads canon precedence as already authorizing it |
| RP-3 | Instruction §5.7 (c): "A roster capture left byte-stable across the `release_id` change keeps its earlier label. That is a finding to the IA (WU-PR-02 instruction §8 D-1), not a roster edit." Instruction §6: `tools/evidence/update_evidence_index.py` "expected to stay unchanged"; §14 trigger "a change needed outside §6 (in particular to … the updater …)" | `artifacts/core/purity/purity_report.json` is on the updater's `CURRENT_RELEASE_CAPTURE_PATHS` roster but its bytes do not depend on the release (it binds engine-core source digests). This unit's refresh leaves it byte-stable, so its Mirror row keeps the superseded `release_id`, and three WU-PR-02 tests in `tests/evidence/test_evidence_index_missing_state.py` (an evidence-lane test file) fail. No owner run inside §6 can relabel it (§2A) | APPROVE the bounded delta of §3A: one roster line removed from the updater, published by the updater itself |
| RP-2 | Plan v1.1 §10 step order (updater at step 5, A7 owner at step 7) | With this unit's new catalog validator, every updater run refuses until the A7 owner has rewritten the catalog. The plan adds step 3b (the A7 owner write after admission and before the gate). Not material: same commands, same owners, no acceptance or boundary change | Confirm `IN_SCOPE_REPAIR` (no delta) |

**Basis for a request rather than a proposal.** PR-20 owns the rescope request during pre-Proceed planning (PR-20 "Rescope authorship"); RS-10 is optional support and was not used; RS-20 accepts "exactly one complete read-back `RESCOPE_REQUEST` from PR-20". Precedent: `docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md`.

**What this request does not do.** It approves nothing, authorizes no implementation, rewrites no approved base, requests no Proceed, edits no canon and creates no PF10 addendum.

## 2. RP-1 evidence

### 2.1 Canon (read in full on `main` at `20f16d0`)

| Source | Passage (verbatim) |
| :- | :- |
| HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.8.1 "Dev/QA Reader availability", "Repo-side start-helper posture (names-only)" | "Dev Reader start helpers are part of the adapter/dev-harness boundary and MUST propagate `APP_ENV` exactly as supplied by the calling environment. They do not silently default `APP_ENV`." |
| HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §5.6, "Dev Reader start helpers (APP_ENV propagation)" | Start helpers "MUST: propagate APP_ENV from the calling environment as-is, including when it is explicitly set to "dev", "test", "local", "prod", an empty string, or left unset; MUST NOT supply a default APP_ENV value (for example, forcing APP_ENV=dev when it is empty or unset)". "…it must not override the caller's choice of APP_ENV." "Live QA harnesses … rely on this behavior to exercise and verify the full set of APP_ENV modes … This clarification ensures infra start helpers do not silently mask gating bugs by forcing APP_ENV to an allowed value." |
| HDE Mechanics Guide §34 "Dev HTTP Harness (single home)" | Required start command: "`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`"; current posture: the script "propagates `APP_ENV` only when the caller supplies it." |
| Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1 "Shared keys", `APP_ENV` note | Start helpers "MUST: Propagate `APP_ENV` from the caller … and MUST NOT silently force a default when `APP_ENV` is empty or unset." |
| HDE Build Checklist — Conjunction (`docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md`) Subtask HDE-CONJ001.4 | `scripts/dev_start_reader.sh` "forwards `APP_ENV` from the caller without forcing a default, exporting `APP_ENV` only when it is present so that harnesses can exercise `APP_ENV=dev`, `APP_ENV=prod`, empty, and unset modes" and "logs `APP_ENV_DISPLAY`". |
| Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §13.9 | "For dev Reader start helpers, silent `APP_ENV` defaulting was non-conforming. The durable posture was to propagate `APP_ENV` exactly as supplied, including unset or empty states, and to make the effective state explicit in governed evidence." |
| HDE Math Spec (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.8.md`) §12, "Dev Reader harness" bullet (supporting) | "A default that treats an unset environment as development is not fail-closed." |

PF10 v13.5.6 was searched for `dev_start_reader`, "start helper", and `APP_ENV` defaults: no addendum speaks to them.

### 2.2 Lineage

- The Specification does not require the default. S10's acceptance intent is about the route ("The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses"), narrowed by Plan v1.1 R1.1 to explicit `dev`. The constraint "Dev route. S10 must not break dev, test or local use of `/reader`" is met by the canonical start command, which supplies `APP_ENV=dev` (HDE Mechanics Guide §34).
- EC-4 originates in the Audit (§7.1, rationale: "S10 must not break dev use; the runner would otherwise start a refusing `/reader`"). Plan v1.1 IF-10 and acceptance (2) carry it. The review v1.1, the instruction and PF10 addenda 2.2 to 2.5 record no canon conflict on it. A search of every `docs/ephemeral/HDE-CRD-0002-*` record (other than this unit's new records) for "start-helper", "start helper", "silently default" and "propagate `APP_ENV`" finds nothing.
- The current script already conforms: it exports `APP_ENV` only when set and displays `<UNSET>` otherwise (lines 13–18). EC-4 would make it non-conforming.

### 2.3 Prototype evidence (this session; scratch; never pushed)

- **Approved-base design** (EC-4's default; a scratch copy of the script run from the prototype with `APP_ENV` unset): the banner prints `[dev-start] APP_ENV=dev` and `GET /reader?v=1` answers 200. The unset refusal that canon says QA harnesses rely on can then no longer be observed through the runner.
- **Proposed design** (script unchanged; `VERIFY.sh` requires an explicit `dev`; final prototype, plan §4.3):
  - `tests/scripts/test_dev_start_reader.py`, 10 passed:
    - `APP_ENV=dev` serves 200;
    - unset prints `[dev-start] APP_ENV=<UNSET>` and the runner refuses 403 `ERR_READER_FORBIDDEN`;
    - `test`, `local`, `prod` and empty are kept and refused;
    - `VERIFY.sh` with `APP_ENV=dev` exits 0 with all 12 tokens `_OK`;
    - `VERIFY.sh` without an explicit `dev` (unset, empty, `test`) exits 2 with `VERIFY_APP_ENV_NOT_DEV` and no output.
  - The full `tests/` sweep: 4,747 passed, 3 skipped, 2 xfailed, 0 failed.

### 2A. RP-3 evidence

- **The roster and its rule.** `tools/evidence/update_evidence_index.py` lines 55–83:
  - the comment reads: "Mirror rows for primaries whose bytes the admitted release determines carry a release label … A capture takes the label of the release in catalog/manifest.json only when its owner has regenerated it (its bytes differ from those the Mirror last recorded); a release change alone never relabels a capture";
  - `CURRENT_RELEASE_CAPTURE_PATHS` lists 23 paths, including `artifacts/core/purity/purity_report.json`;
  - `_current_release_labels` keeps the prior label unless the bytes changed.
- **The capture.** `artifacts/core/purity/purity_report.json` (`engine_core_purity_report.v1`) records module purity results and the SHA-256 of `catalog/magic10_mechanics_v1.json`, `engine/bodygraph/gates.py`, `engine/config/registry_loader.py`, `engine/core/*` and `engine/magic10/*`. It carries no `release_id`, and its bytes do not depend on the release. Its last change on `main` predates WU-PR-02 (`e7265a0`). This unit changes none of those sources, so the engine-core owner regenerates it byte-identically.
- **Observed (rehearsal 2, after steps 3b to 10 on both passes).**
  - The purity row keeps `notes: "current-release capture: release 1.3.0, release_id 52be4558…"` (the superseded release); every other roster row carries the new label.
  - A full `tests/` sweep on that state: `tests/evidence/test_evidence_index_missing_state.py` fails three tests, all on this row:
    - `test_current_release_capture_rows_are_labeled_and_frozen_rows_are_not` (`'…release_id 52be4558…'.endswith('…release_id d041ee18…')` is False);
    - `test_release_labels_follow_regenerated_captures_through_the_updater_alone` (line 1167, the same assertion);
    - `test_unlabeled_capture_rows_take_the_admitted_release_on_adoption` (byte difference at the label).
  - That file runs in the evidence lane, so CI would be red.
- **Why not inside §6.**
  - The capture's owner (`tools/evidence/generate_engine_core_evidence.py`) cannot change its bytes without a schema change.
  - Relabeling by hand is forbidden.
  - The tests encode WU-PR-02's accepted contract.
  - The roster lives in the updater, which instruction §6 keeps unchanged and §14 routes.
- **The same defect recurs** at every later same-version refresh that leaves the engine-core sources unchanged (WU-PR-04, and WU-PR-05 if it changes a member). WU-PR-08 changes `engine/config/registry_loader.py`, so it regenerates the capture and is unaffected.
- **Proposed fix, prototyped.** With the single roster line removed, one updater run strips the purity row's label itself: the row's `notes` field is dropped, there is no hand edit, and no other row changes. Then:
  - `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh` and `check_final_lf.sh` all exit 0;
  - the five evidence-lane test files plus `tests/evidence/test_engine_core_evidence.py` and `tests/evidence/test_evidence_index_missing_state.py`: 142 passed;
  - the full sweep result on the final prototype is in plan §4.3.

## 3. RP-1 proposed delta (smallest bounded overlay)

For WU-PR-03 only:
1. **EC-4** is not implemented. `scripts/dev_start_reader.sh` stays byte-unchanged (it already propagates `APP_ENV` exactly and displays the effective value).
2. **IF-10**, last clause, reads: "`scripts/dev_start_reader.sh` propagates `APP_ENV` exactly as the caller supplies it, including unset and empty, and never defaults it (HDE Architecture §3.8.1; HDE Mechanics Guide §5.6); the canonical start command supplies `APP_ENV=dev`."
3. **Acceptance (2)**, last clause, reads: "`scripts/dev_start_reader.sh` with `APP_ENV=dev` starts a serving runner; with `APP_ENV` unset or empty it propagates that state and the runner refuses `GET /reader` (403 `ERR_READER_FORBIDDEN`)."
4. **Documents.** `docs/server/reader_v1.md` and `docs/acceptance/reader_a7_crib.md` state the start command `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV` (replaces EC-4's "`docs/server/reader_v1.md` states it").
5. **`VERIFY.sh`** (it launches the runner through the start helper, so the same rule applies): line 4 `export APP_ENV=${APP_ENV:-dev}` — the PF14 §5.6 example of a forbidden default — is replaced by a loud refusal unless the caller supplies `APP_ENV=dev` (`VERIFY_APP_ENV_NOT_DEV`, exit 2, printing the effective value), because every `VERIFY.sh` check verifies the dev success path. The checks are otherwise as instruction §9.5 and plan §6.4 state.
6. **ID-3** is unchanged: `tests/scripts/test_dev_start_reader.py` stays registered as the owner of `scripts/dev_start_reader.sh`. It tests the propagation contract above and runs `VERIFY.sh` with `APP_ENV=dev`, plus three cases proving the refusal without it. The registration does not depend on the script changing, and it gives the canonical runner its first registered owner test.

## 3A. RP-3 proposed delta (smallest bounded overlay)

For WU-PR-03 only, instruction §6 gains one bounded locus:
1. `tools/evidence/update_evidence_index.py`: remove exactly the line `"artifacts/core/purity/purity_report.json",` from `CURRENT_RELEASE_CAPTURE_PATHS`. No other line, rule, refusal code, write path or schema changes. The roster comment already states the criterion the change applies ("primaries whose bytes the admitted release determines").
2. The updater's own run in the convergence (step 5, and step 8 thereafter) removes the row's label. No governed artifact is hand-edited.
3. Because the updater changes, LR-O2 applies: every test file that imports or runs the updater runs (the full `tests/` sweep satisfies it). The classifier already registers the updater's owners.
4. The PR result record states the roster change, its reason and the row it unlabels, and carries the nonclaim that the purity report is not a release-bound capture.

Alternatives:
- (b) The engine-core owner adds release identity to the purity report, so that the report regenerates at every release change. This is larger: an `engine_core_purity_report.v1` schema change, test changes and a new evidence meaning.
- (c) The IA lands the roster fix in its own PR before WU-PR-03. This is equivalent in content, adds a PR and a merge dependency, and WU-PR-03 waits for it.
- (d) Accept red evidence-lane CI. Not acceptable: acceptance (7) requires all lanes green.

Recommended: the delta above, (a).

## 4. Impact

| Surface | Effect |
| :- | :- |
| Requirements | S10 intent and the "Dev route" constraint met unchanged; S09 unchanged; no other requirement touched |
| Acceptance | WU-PR-03 (2) last clause as §3 item 3; (1), (3) to (7) unchanged |
| Interfaces | IF-10 last clause as §3 item 2; IF-6, IF-11 unchanged; contract E-6 reads "`/reader` served only for `APP_ENV=dev`; the runner propagates `APP_ENV` and the caller supplies `dev`; `VERIFY.sh` uses the canonical runner and requires `APP_ENV=dev`" |
| Files | `scripts/dev_start_reader.sh` leaves the changed set; `VERIFY.sh`, the two documents and the owner test as §3 |
| Tests | the owner test asserts propagation instead of a default; nothing else changes |
| Release, evidence, CI | RP-1: none (the script and `VERIFY.sh` are not release members and bind no governed evidence). RP-3: the updater (not a member) changes by one line; one Mirror row and the Index lose a label through the updater; the evidence lane and the updater's consumer tests cover it; the change classifies through the updater's existing registration |
| Ops, QA | QA-10's S10 Live QA step and WU-OPS-01 use the canonical start command with an explicit `APP_ENV`; the unset-refusal mode stays observable through the runner (HDE Mechanics Guide §5.6) |
| Downstream | RP-1: WU-DOC-01 states the start command with `APP_ENV=dev`. RP-3: WU-PR-04 and WU-PR-05 refreshes no longer hit the stale purity label; nothing else changes |
| Canon | none changes; EC-4 would have made HDE Architecture §3.8.1, HDE Mechanics Guide §5.6 and §34, Glow Infrastructure §8.1, the Conjunction checklist HDE-CONJ001.4 and the QA Guide §13.9 stale or violated |

## 5. Canon-conflict register entry (proposed)

| Field | Value |
| :- | :- |
| ID | CR-6 |
| Classification | CANON_RECONCILIATION (an approved in-flight Plan item contradicts current canon) |
| Sources | Plan v1.1 §5 IF-10 and §7 WU-PR-03 acceptance (2); Audit v1.0 §7.1 EC-4; versus the six binding canon passages of §2.1 (five documents) at `20f16d0`, with HDE Math Spec §12 supporting |
| Statement | The approved Plan requires the dev Reader start helper to default `APP_ENV=dev`; canon requires it to propagate `APP_ENV` exactly and never default it |
| Affected requirements | S10 (runner clause of acceptance (2)); S09 (`VERIFY.sh` launches the runner) |
| Alternatives | (a) canon governs; bounded Plan delta §3 (recommended). (b) keep EC-4 under a formally approved bounded Product Owner decision superseding canon for this script, as CR-4 did for R-14, with canon drainage of the six binding passages. (c) as (a), but `VERIFY.sh` keeps its own default as the caller (not recommended: it is the forbidden example) |
| Recommended disposition | (a) |
| Interim treatment | the plan v1.0 runner item is BLOCKED; no implementation exists |
| Unresolved risk | none beyond the decision |
| Drainage | none under (a); under (b), the six binding passages, owned by the Product Owner |
| Status | PROPOSED |
| Reviewer / session / reviewed artifact / decision time / rationale | not yet reviewed |

## 6. RP-2 evidence (for confirmation)

`tools/evidence/update_evidence_index.py::_validate_epic038_pr02_semantics` calls `generate_a7_transport_proofs.validate_catalog` on the tracked catalog, and the config publisher runs the updater. In rehearsal 1 (Plan v1.1 §10 order, after the cut), steps 5 and 6 exit 1 with `ValueError: aux narrative catalog invalid`. In rehearsal 2, with step 3b inserted (the A7 owner write and `--check` after admission and before the gate), every step 3 to 10 exits 0 on both passes (64 of 64 runs), with identical outputs on the second pass. Step 7 keeps the A7 owner run, which is then byte-stable. The restart point for an evidence-primary change becomes 3b. The plan records it as PD-15 and as observation OBS-P3-7 for WU-PR-04, WU-PR-05 and WU-PR-08.

## 7. Completed valid work (preserved)

Plan v1.0 is complete for every item except RP-1, including:
- S02, S07, S09 (harness removal, documents, `VERIFY.sh` repair), S15 (13 rows, validator, enumeration), S18;
- ID-3, ID-4, the convergence and its rehearsal, the tests and the validation plan.

The prototype diff accompanies it. Nothing is implemented, committed to a code branch or published.

## 8. Risks, exclusions, unresolved facts

- **Risk:** under (b), QA could no longer exercise the unset mode through the runner. Under (a), an operator who omits `APP_ENV` gets a refusing runner, which the banner (`APP_ENV=<UNSET>`) and the documents make visible.
- **Exclusions:** no change to the `/reader` gate design, the catalog, any member, any canon or any other unit.
- **Unresolved:** only these decisions.

## 9. Return

- **On APPROVE or IN_SCOPE_REPAIR:** this PR-20 planning context writes plan v1.1 as a complete successor applying the decision, and presents it at `AWAITING_PO_PROCEED`.
- **On REJECT:** for RP-1, plan v1.1 implements EC-4 as approved, and CR-6 stays open for its owner. For RP-3, the refresh cannot reach green CI inside §6, so plan v1.1 stays BLOCKED on RP-3 and returns it to the IA as owner (instruction §5.7 (c)).
- **On REVISION_REQUIRED:** RS-30 in this author context.
- **On SPECIFICATION_CHANGE_REQUIRED:** Nathan.

## Canon precedence (Plan Templates, "Canon precedence for template use")

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

Applied here: no PF10 addendum addresses dev Reader start helpers, and no Product Owner rescope adjudicates EC-4, so PF-Canon is followed (HDE Governance §9.1.2: "Follow the governing PF position immediately … otherwise report the precise conflict and stop the affected work").

## Canon relied on

Read on `main` at `20f16d0`: HDE Architecture §3.8.1; HDE Mechanics Guide §5.6 (start-helper paragraph) and §34; Glow Infrastructure §8.1 (`APP_ENV` note); HDE Build Checklist — Conjunction HDE-CONJ001.4; Glow QA Guide §13.9; HDE Math Spec §12 dev-harness bullet; HDE-CLI-API-Vendor-Ref §5.4 and §5.6 (route gate); HDE Schemas & Artifacts §8.8 (explicit `APP_ENV=dev`); HDE Governance §9.1.1 and §9.1.2; Plan Templates "Canon precedence for template use"; PF10-HDE-Build-Notes v13.5.6 addenda 2.2, 2.3, 2.5 (no rule on start helpers); `AGENTS.md` canon-first rule ("Where an in-flight document conflicts with PF-Canon, PF-Canon governs unless an applicable PF10 rule supersedes it … or a formally approved bounded Product Owner rescope supersedes it"). In-flight: Specification v1.1 S10 row and "Dev route" constraint; Audit v1.0 §7.1 EC-4; Plan v1.1 §5 IF-10, §7 WU-PR-03, §10, §15; PR instruction v1.0 §4, §6, §9.5, §14; `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` (CR-4 precedent).

## Prompt-use provenance (GCFPE_PROMPT_USES)

HDE-CRD-0002 / WU-PR-03 / PR-20 / rescope request 1; Specification v1.1; release GCFPE-20261009.1 / 100926.1; prompt PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba, page state 2026-10-12T02:29:47Z); role dedicated WU-PR-03 PR engineering session; capture 2026-10-14T02:01:29Z; execution identity https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ; repository persistence pending (installed writer absent).
