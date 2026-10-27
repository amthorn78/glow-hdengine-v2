---
artifact_type: IMPLEMENTATION_PLAN_REVIEW
artifact_version: "1.1"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: INITIAL_PLAN_REVIEW (re-review after IA-40 PREAPPROVAL_PLAN_REVISION)
decision: INITIAL_APPROVE
reviewed_artifact: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md
reviewed_artifact_version: "1.1"
reviewed_artifact_blob: abffa2ccbd447a7e13727fc5e53e83341d35f0f4 (75,920 bytes; sha256 9747f0ffc084d3467ae876f24fa1f1f7a9db8f4a4bf5f62821cf8eb2b6ab486f; landed on main at 0eb41879, amthorn78/glow-hdengine-v2#621)
approved_representation: the exact unchanged Plan v1.1 plus this review. The Plan's saved body keeps PLAN_PENDING_REVISED and "ASK OK?"; this decision supplies the approval without editing the Plan
application_report: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1-application-report.md (blob b64a300ae8e71105c015f51c0ed0014fc45fc895)
predecessor_plan: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md (blob b0eefc0bd68eb67ee58d667602864c266db18458; denied)
predecessor_review: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.0.md (INITIAL_DENY, R1–R4)
audit_ref: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c)
specification_ref: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
thoth_decision_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md (INITIAL_APPROVE)
reviewer: Isis, continuing Lead Developer and independent whole-change Implementation Plan reviewer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; same reviewer as review v1.0)
ia_author: whole-change Implementation Agent for HDE-CRD-0002 (Audit and Plan v1.0 in session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; Plan v1.1 in the same IA role and artifact lineage, execution session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j)
prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c)
prompt_release: GCFPE-20261009.1 / 100926.1
release_selection_check: GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", 55 members; read 2026-10-12 (current-selection section)
created_at: 2026-10-12T21:08:54Z
repository_head_read: origin/main 0eb41879
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (unchanged; addendum 2.1 only)
approved_base_plus_overlays: Specification v1.1 (approved) + PF10 overlays NONE
pf10_addendum: none (INITIAL_APPROVE produces no addendum)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a)
next_work_unit: WU-PR-01
next_actor: the same whole-change IA
---

# HDE-CRD-0002 — Implementation Plan review v1.1 (IA-30)

## 1. Decision

**INITIAL_APPROVE.** Isis approves HDE-CRD-0002 Implementation Plan v1.1 exactly as reviewed: `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, blob `abffa2cc…`, 75,920 bytes. This is the change-wide Implementation Plan for HDE-CRD-0002.

The approved representation is the unchanged Plan v1.1 plus this review. The Plan's saved body keeps `PLAN_PENDING_REVISED` and `ASK OK?`; this decision supplies the approval without editing it, as the HDE-EPIC040 Plan review v2.1 did.

This is a whole-change review of v1.1. It is not limited to the changed paragraphs and does not simply accept the author's application report:
- Every R1–R4 item was checked against the line diff.
- The unchanged content was approvable in review v1.0 apart from R1–R4 (review v1.0 §5).
- R3's new design was checked against the code it relies on (§3).

What this approval does and does not authorize:
- **Does.** It permits PR Instruction creation (PR-10) in the Plan's dependency order, starting with WU-PR-01.
- **Does not.** It authorizes no PR Proceed, implementation, Ops execution, deployment, QA, ADR approval (AQ-1 stays with the Product Owner), canon change, acceptance or closure.
- **No addendum.** It creates no PF10 addendum.

**ASK OK.**

## 2. Redline application (review v1.0 §3)

| # | Required | v1.1 (line diff against v1.0) | Finding |
| :- | :- | :- | :- |
| R1.1 | IF-10 explicit-`dev` gate | IF-10 third cell replaced verbatim | Applied |
| R1.2 | IF-6 `/reader` `env_gate` stays `APP_ENV=dev` | Replaced verbatim | Applied. Matches the catalog on `main` (`GET`/`HEAD /reader`: `APP_ENV=dev`) |
| R1.3 | WU-PR-03 acceptance (2) | First clause replaced verbatim; the rest of the item is unchanged | Applied |
| R1.4 | §15 explicit-`dev` sentence | Appended verbatim | Applied |
| R2.1–R2.6 | AQ-1 before WU-PR-07 merges: WU-PR-07 dependencies, §9 items 1, 4 and 5, R-4, AQ-1 | Each replaced or inserted verbatim. §16 `open_question` gains "; decided before WU-PR-07 merges" | Applied. The §16 addition agrees with §13 and is within the linked edits |
| R3.1 | Terminal-state reachability bullet, elements (a)–(e), in the IA's own design | New bullet between Deliverables and Dependencies | Applied. Assessed in §3 |
| R3.2 | WU-PR-07 acceptance (7) | Appended verbatim | Applied |
| R3.3 | §9 item 5 pointer sentence | Appended verbatim | Applied |
| R4.1–R4.3 | `HDE-CRD-0002` close-pack filename prefix: invariant 6, IF-3, §15 | Replaced verbatim | Applied. A residue search finds no bare `CRD-0002_` or `CRD-NNNN` prefix; every occurrence (six `HDE-CRD-0002_`, one `HDE-CRD-NNNN`) is the canonical form |

**No unannounced changes.** Outside the R1–R4 anchors, the line diff shows only the edits the application report lists in its §4:
- header and provenance fields;
- the revision note;
- the §1 state token;
- §16;
- §17's TypeSafe reading;
- the "IA-40 revision reads" canon paragraph;
- the closing state line.

No requirement, unit, interface, order, risk, exclusion or decision outside R1–R4 changed. Non-gating notes N1–N6 are dispositioned in the report's §3 as review v1.0 directed. Each disposition is accepted.

## 3. R3 assessment: terminal-state reachability

Plan Templates, "Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review)", requires the reviewer to establish five things for the claimed terminal state. Each is established from the Plan's statement and the code on `main` at `0eb41879`.

| Element | Finding | Verified against |
| :- | :- | :- |
| Terminal state | (a) names every tracked byte of the close mutation set: close report, manifest and path proofs at the canonical `HDE-CRD-0002` filenames; the IF-4 close-run family; the Index trio and companions; and the tracked causal inputs. All are committed before hosted validation. This matches Change Process Guide §3.5.2.1 and §3.5.2.3 | Plan v1.1 WU-PR-07 (a) |
| Feedback-free path | T0–T7 run locally in a clean clone under closed rails. No close-run, close-pack or Index byte comes from a hosted workflow (c, e). Hosted validation is check-mode only and records its results on the PR (Change Process Guide §3.5.1). This verifies three facts in the code: (i) The writer refuses non-closed rails (`CLOSED_RAILS_REQUIRED`). It requires a clean tree before and after. In check mode it requires both outputs tracked at HEAD with matching bytes (`OUTPUT_HEAD_MISMATCH`). It refuses any worktree, HEAD or Git-control mutation (`CHECK_MODE_MUTATION`). (ii) Its docstring states that "existing candidate outputs are not causal inputs". (iii) `epic-closeout-validation.yml` is `workflow_dispatch` only, with inputs `git_ref` and `candidate_source`, `contents: read` and `persist-credentials: false`. It asserts a clean tree at the exact SHA | `tools/qa/generate_epic_close_pack.py` (module docstring; `_require_clean`; check path at lines 3735–3786; `_require_closed_rails`); `.github/workflows/epic-closeout-validation.yml` lines 1–60 |
| No cycle | (d) makes every dependency point toward the Index. Causal inputs feed the close report and manifest, which feed the Index. Close-run primaries feed the Index. The manifest binds no Index byte; the v2 writer is to refuse the Index trio, path proofs, orientation output, `audit/qa/<change-id>/close/**`, the close-pack outputs and `catalog/manifest.json` as causal inputs, and `key_outputs` carries paths without digests. The close-run primaries record T2–T4 against C1 and C2, which are fixed before they are written. The updater already indexes earlier close packs this way | `tools/evidence/update_evidence_index.py` lines 352–362 (`epic022.close_report`, `epic022.manifest`) |
| Execution-surface feasibility and rails | Each transition names its tool. The writer, the updater with its new IF-4 entrypoint, and the read-only checks all exist today or are WU-PR-07 deliverables. Every transition runs under the writer's own closed-rails set. Restart rules are stated | Plan v1.1 WU-PR-07 (b) |
| End-to-end proof | Acceptance (7) rehearses the exact sequence for a synthetic `HDE-CRD-0002` candidate in a throwaway copy. It ends with the writer's check, the updater `--check`, the Mirror-schema check and the Index-hash check, with second-run byte stability and no hosted-CI-produced byte | Plan v1.1 WU-PR-07 acceptance (7) |

The two points the bullet bounds to the PR-20 plan are engineering details inside S21's bound and need no Plan-level decision:
- the candidate-source path, recorded in the ADR;
- any `tools/qa/qa_harness.py` touch for rendering close-run primaries.

R3 is satisfied.

## 4. Non-gating notes (no correction required)

- **M1 — CRD close-pack Index registration.** T3 relies on "the CRD close-pack registration this unit adds", absent-tolerant like the Epic rows. WU-PR-07's Deliverables line for `tools/evidence/update_evidence_index.py` names only "IF-4 family admission". The file is already a deliverable, and the reachability bullet states the registration, so the PR-20 plan carries both. Whether the existing Epic rows are absent-tolerant was not verified here; acceptance (7)'s rehearsal exercises it.
- **M2 — IA execution session.** Plan v1.1 was authored in a different execution session (`session_01CCKsYD2yX5WgU3biWKb59j`) from Audit and Plan v1.0 (`session_012nUipT8gpdYtjzA5UQk5ah`). Under IA-30 and IA-40 "Role and artifact continuity", this is the same IA role and artifact lineage. Both sessions are recorded as provenance, and none is invented.
- **Carried from review v1.0:** N1–N6 stand as dispositioned. N2 (fix-versus-retire criterion) and N4 (override actor principal and sink key) are carried to the WU-PR-01 and WU-PR-04 PR-20 plans respectively.

## 5. Next stage

| Field | Value |
| :- | :- |
| `IMPLEMENTATION_PLAN_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by this review) |
| `PLAN_REVIEW_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md`, v1.1 |
| `WORK_UNIT_ID` | `WU-PR-01`: CI coverage of every test file; Distillation; S03, S04, S05 (Plan v1.1 §7) |
| Dependency state | Ready. The Plan's §7 says "First. No upstream dependency." No unit has landed. WU-PR-02, WU-PR-06 and WU-PR-07 may be prepared in parallel but merge in the stated order |
| Source and PF10 lineage | Specification v1.1 (approved) → Audit v1.0 → Plan v1.1 (approved here); PF10 v13.5.2, overlays NONE; canon on `main` unchanged since `df23bbf` (#614) |
| IA session | The same whole-change IA role (sessions recorded in M2) |
| `EXECUTION_POSTURE` | `MANUAL_PROMPT_EXECUTION` |
| Open owner decision | AQ-1 (Product Owner), due before WU-PR-07 merges; it does not gate WU-PR-01 |

The approved Plan remains the governing source for its later Ops (WU-OPS-01), documentation (WU-DOC-01) and QA-readiness consumers. No PR, Proceed, QA Guide, QA Plan, Ops receipt or documentation result is required before PR-10.

## 6. TypeSafe reading for the receiving session (PR-10, WU-PR-01)

Action sent (v6): "Create, as the whole-change Implementation Agent, the PR work-unit instructions for the first planned unit of a newly approved ten-unit CRD Implementation Plan: bringing about 135 test files that run in no CI lane into lanes or retiring each with a recorded reason, fail-closed classification for unregistered tools/qa shell and SQL sources, and aligning the CI workflow's documentation skip list with the classifier's eight prefixes while keeping governed primaries under CI. It reads the approved Plan, its review, the Audit and the Specification from the repository, confirms the unit is dependency-ready, and writes one instruction artifact; no code is written and no live run occurs; a dedicated PR planning session and a Product Owner Proceed follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.48 (confidence 0.65); rung probabilities low 0.00, medium 0.03, high 0.53, extra high 0.38, max 0.06, ultracode 0.00. Model probabilities Fable 5.1 0.10, Opus 5.5 0.90 (confidence 0.80). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.48, Opus 5.5 at extra high 0.34, Opus 5.5 at max 0.05, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.01, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and high. Sent 2026-10-12T21:08:50Z.
- **Detail:** v6 sent 2026-10-12T21:08:50Z; HTTP 200 in 0.81 s; 4258 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- **Nathan's pick for PR-10:** not stated.
- **Nathan's pick for this IA-30 session:** not stated (reading recorded in Plan v1.1 §17).

**Surface advice:** run PR-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change IA role. It reads the approved Plan v1.1, this review, the Audit (§5.2, §5.3, §5.7, Appendix A for WU-PR-01), the approved Specification and `docs/pfcanon/` on `main`. It also reads `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml` and `pytest.ini` for the unit's facts. It writes only its instruction artifact under `docs/ephemeral/`, and needs no live vendor, production or database access. This review's PR should be merged to `main` first.

## Canon relied on

Read on `main` at `0eb41879`. `docs/pfcanon/` is unchanged since `df23bbf` (#614), so the sections review v1.0 read in full stand; its "Canon relied on" block lists them. Each decision topic maps to its sections below.

- **Approval authority, mode and exact-artifact approval:**
  - PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (Isis approves the change-wide Plan; the IA may not expand the Specification) and §9.1.2 (precedence; reviews govern within scope);
  - IA-30 — Review Whole-Change Implementation Plan — 100926.1 (`INITIAL_APPROVE`; routing to PR-10).
- **R1 application:** PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.6 (`/reader` row); PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6, "Reader surface routes and distinct contracts (normative)".
- **R2 application:** PF06-Canon-Change-Process-Guide v2.5.4 §1.0.5 and §1.0.6; the Specification's Exclusions bullet 3, S21 acceptance intent and Distillation completion boundary.
- **R3 assessment:**
  - PF27-Canon-Plan-Templates v2.0.5, "Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review)" and "Materiality-based blocker discipline for planning and review artifacts";
  - PF06 §3.5.1 (including "Feedback-free terminal lifecycle"), §3.5.2.1, §3.5.2.3;
  - PF19-Canon-Glow-QA-Guide v3.0.6, "Close-pack truthfulness and same-run execution (normative)" and "Close report requirements".
- **R4 application:** PF12 §1.2 "Change-container compatibility (normative)"; PF30.1-Canon-HDE-CRD-Records v0.9.1, CRD ID syntax.
- **Whole-Plan approvability (unchanged content):** as review v1.0 §5 and its "Canon relied on" block, including:
  - PF05 §7.1.11a–f;
  - PF27 §3 "Ops Task Record";
  - PF19 §3.5.5;
  - PF06 §1.0.4 and §1.1.5A.
- **PF10:** PF10-HDE-Build-Notes v13.5.2. Addendum 2.1 governs only §6's TypeSafe reading; PF10 is silent on the Plan's subject matter.
- **Operative documentation:** `AGENTS.md` (canon-first; sole Index/Mirror writer; HDE-EPIC039 close-pack workflow posture).

**Repository facts read on `main` `0eb41879`:**
- `tools/qa/generate_epic_close_pack.py`: module docstring, `CLOSED_RAILS` and `_require_closed_rails`, `_require_clean` use, the check path at lines 3735–3786, and the argument contract;
- `.github/workflows/epic-closeout-validation.yml` lines 1–60;
- `tools/evidence/update_evidence_index.py` lines 340–366;
- `docs/ENDPOINTS_CATALOG.json` `/reader` rows (read for review v1.0; unchanged).

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, through the line diff against v1.0 (read in full for review v1.0) plus every changed hunk;
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1-application-report.md`;
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.0.md` (this reviewer's predecessor decision).

Carried from review v1.0, with no change on `main` since: the Audit v1.0 and the approved Specification v1.1.

**Prompts read:**
- IA-30 — Review Whole-Change Implementation Plan — 100926.1;
- PR-10 — Create PR Work-Unit Instructions — 100926.1 ("Resolve the next approved Plan stage", "Inputs", "Managed entry, execution posture and continuing identity");
- the GCFPE Membership and Release Register, current-selection section.

**Precedent consulted:** `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1 (1).md` §1 (approved representation of a revised Plan).

## 7. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-30 / initial plan review 2 (re-review) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | IA-30 — Review Whole-Change Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c |
| role/stage | Isis / IA-30 initial Implementation Plan review, re-review |
| capture time | 2026-10-12T21:08:54Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
