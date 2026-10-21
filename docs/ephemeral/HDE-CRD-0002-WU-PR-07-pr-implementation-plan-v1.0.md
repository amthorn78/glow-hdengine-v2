---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
work_unit_title: "Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation; S21)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; landed by #664 as 6f53552)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE)
REMEDIATION_REVIEW_ID: none (no remediation lineage)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1
effective_baseline: approved base + PF10 addenda 2.11 (read with 2.12's numbering), 2.12, 2.5, 2.3 and 2.1 §19, and the Product Owner disposition of 2026-10-20 (docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (271,926 bytes; sha256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35; addenda 2.11 and 2.12 read in full in this session)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md §2.11, §2.12, §2.5, §2.3, §2.1
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.0-prototype.diff (git diff 6f53552 → prototype head; 1,982 lines; 91,626 bytes; sha256 33ee8bef36df7c29b6931eed9c0c8ce87af885ed39aa996bb2469d6b2f1199bf)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF (the dedicated WU-PR-07 PR engineering session; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, fetched and read in full in this session)
repository_baseline: origin/main 6f53552 (#664). Outside docs/ephemeral/, every byte equals 731f03c, the instruction's measured baseline (git diff --name-only 731f03c 6f53552 lists only the instruction)
working_branch: claude/gallant-cerf-ysdde5 (this plan only)
created_at: 2026-10-20T15:08:33Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§19)
---

# HDE-CRD-0002 WU-PR-07 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED.** This is the complete plan for WU-PR-07 within the instruction's scope and ceiling. The whole change was prototyped in a throwaway clone and passes its tests, the T0 to T6 rehearsal and a full local CI replay (§12). PR-30 applies the companion diff, re-runs the checks in §11 and publishes one PR.

One finding is outside this unit's approved scope and is the Product Owner's to route before or alongside the Proceed (§16, F-1). The hosted `epic-closeout-validation` job cannot pass its evidence-check step for any candidate today: it installs only `jsonschema`, and `update_evidence_index.py --check` imports Flask. HDE-CRD-0002's close needs that job (Plan v1.1 T7). Nothing in this plan's acceptance depends on it.

This plan authorizes nothing. Only the Product Owner's `PR Implementation Proceed` (PR-30) for exactly v1.0 authorizes implementation; only the Product Owner merges; AQ-1 (the ADR) is the Product Owner's before merge.

## 2. Lineage and sources read in this session

- **Instruction** v1.0, read in full. Its §5 baseline was re-measured at 6f53552 (§4).
- **Plan v1.1** §7 WU-PR-07 block in full (Purpose to Nonclaims, T0 to T7, restart rules, acceptance (1) to (7)); §5 IF-3 and IF-4 through the instruction's verbatim quotation.
- **Product Owner disposition** of 2026-10-20, read in full (business case, ceiling and counting; option A).
- **Specification v1.1** requirement table (rows S01 to S22, read and re-measured against the v1 refusal).
- **Audit v1.0** §8 AQ-1 (alternatives (a) to (c)).
- **PF10 v13.6.3** addenda 2.11 and 2.12 in full. 2.5, 2.3 and 2.1 are taken as the instruction reads them; this session read the parts that carry the items named in §17.
- **Code read**: `tools/qa/generate_epic_close_pack.py` (constants, model, validation, rendering, manifest reader, write and check flows, CLI), `schemas/epic_close_candidate_source.v1.json` in full, the writer test's fixtures and the OBS-17 test, `tools/evidence/update_evidence_index.py` (admission table, transaction, staged view, path proofs, Mirror rendering, CRD reconciler, Index loading, `_run_once`, convergence, `publish_crd_check_family`, CLI), `tools/qa/qa_harness.py` (config, results, primary rendering and parsing, CRD path and family validation), the classifier's owner registry, the rails workflow test's closeout pins, `.github/workflows/epic-closeout-validation.yml` and `.github/workflows/ci.yml`'s install step.
- **Canon** as listed in "Canon relied on".

## 3. Cost ceiling (ID-1)

**Ceiling** (Product Owner, 2026-10-20): one PR, review rounds capped by addendum 2.11 rule 8, at most 4 sessions or 3 days from PR-10 to merge, excluding Product Owner waits (Proceed, AQ-1, merge).

**Spent so far** (counted as the disposition record states):

| Item | Sessions | Elapsed working time |
| :- | -: | :- |
| PR-10 (instruction) | 1 | from 13:14:32Z, by 13:42:00Z (instruction `created_at`) |
| PR-20 (this plan), session 2 of 4 | 1 | prototype measurements from 13:55:25Z; plan saved 15:08:33Z (the last 47 minutes were the replay and consumer runs) |
| **Total at this plan** | **2 of 4** | **about 2 hours of 3 days** |

**How the plan stays within it:**
- **Scope.** Acceptance (1) to (7) and nothing more (rule 3). The plan builds no capability the measure does not need: no Epic close-run family, no generic Epic close-pack registration, no CLI for the close-run entrypoint, no change to the validation workflow (F-1 is routed, not built).
- **PR-30 runs in this same session** (session 2), after the Proceed. Because the change is already prototyped and passes, PR-30 applies the diff, re-runs the checks in §11 once and publishes. Estimate: 1 to 2 hours.
- **PR-35 is session 3.** Estimate: one Codex round plus one CI run on the final head, under a day. Rule 8 and addendum 2.11 rule 7 bound the rounds.
- **Slack.** One session (session 4) remains for one repeat of a stage or one RS-20 review if the Product Owner routes F-1 into this unit (§16).
- **Checks run once vs re-run.** Run once in PR-30, on the published head: the full-validation replay and the T0 to T6 rehearsal. Re-run in PR-35 only when a corrective commit touches code: the writer test file, the updater tests and the replay. The rehearsal is re-run only if a writer or updater correction changes behaviour.
- **Checkpoints.** PR-30's result and each PR-35 result record sessions and elapsed working time. A projected pass of the ceiling is material (instruction §14) and returns to the Product Owner before work continues.

## 4. Baseline re-check at 6f53552 (§9.5)

- `git diff --name-only 731f03c 6f53552`: only `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md`.
- Every row of instruction §5.2 re-measured (lines, bytes, blob): identical.
- §5.3: the v1 refusal applied to the Specification's 22 rows hits S06 (`attestation` in scope and intent) and S11 (`release identity`; `` `release_id` ``). Identical.
- §5.4: CRD-0002 QA root absent; `ADMITTED_CRD_QA` holds HDE-CRD-0001 and HDE-CRD-0002. Identical.
- §5.5 Epic-only search (`git grep` over `tools ci schemas scripts engine`): the v1 schema's `epic_id` pattern and the writer's `EPIC_RE`, as stated. The search also finds `qa_harness.EPIC_RE`, which is not Epic-only: `HarnessConfig` takes a CRD through `crd_id`.
- §5.6: lanes for the prototype head reproduce §10's expectation (§12.4).
- **Two differences from the instruction**, both new facts, neither changing the plan's scope:
  - ID-10 states that the closeout job's other checks pass. With only `jsonschema` installed, `update_evidence_index.py --check` exits 1 (`ModuleNotFoundError: No module named 'flask'`) at 6f53552. That is F-1 (§16).
  - The workflow has never been dispatched: the Actions API lists 0 runs of `epic-closeout-validation.yml`.

## 5. Design decisions (instruction §9.1)

| ID | Choice | Decision | Reason |
| :- | :- | :- | :- |
| PD-1 | v2 field shapes (IF-3) | Closed schema, every property required, `additionalProperties: false` throughout: `schema_version`, `change_id`, `plan_path`, `evidence_inputs[]` (binding, path; 1 to 256), `requirements_binding`, `acceptance[]` (criterion_id, evidence_bindings[], result `MET`/`NOT_MET`, limitation), `deliverables[]`, `deferrals[]` (id + drain_target, or id + adr_status + rationale), `later_drain_statements[]` (canon_homes[], locators[], current_posture, action and readiness in PF12's fixed vocabularies, evidence_bindings[], close_expectation), `tracked_issues[]` (`TI-NNN` + pointer or adr_status), `closure_decision` (decision `SATISFIED`/`NOT SATISFIED`, posture), `follow_ups[]`, `superseded[]` (binding, evidence_change), `pointers[]`, `qa_rca` (binding, or summary_lines[]), `key_outputs` (map of path strings with five required keys), `nonclaims[]` (exactly four) | Each canon element of §4.1 C1 to C7 has one structured field (§7); all evidence is referenced by binding name, so every digest comes from a tracked input |
| PD-2 | S06/S11 (ID-3) | **Bind requirement text by reference.** Acceptance carries the criterion ID; the requirements document is a bound evidence input (path and digest). The writer checks that each ID occurs as a token in that document (`REQUIREMENT_ID_UNBOUND`). The v1 refusal (`FEEDBACK_DEPENDENCY_RE`, the HEAD check and the `catalog/manifest.json` prefix) applies unchanged at runtime to every v2 string except the four nonclaim codes; the schema applies the same pattern to every free-text, path, pointer and binding field | Keeps the invariant exactly as v1 proves it (its negative cases stay valid) while all 22 real rows are expressible. The narrower options (identity-shaped matching; a term allowlist) would promise fail-closed handling over open-ended text (rule 5). Proven: copying S06's intent into a field is refused; the reference form writes (tests in §8) |
| PD-3 | v2 nonclaims (ID-5) | Four, all mandatory: `no_canon_drainage_or_register_movement`, `no_execution_by_writer`, `no_hosted_feedback_inputs`, `no_unbound_claim` | Each is true of every close, including a `SATISFIED` one; v1's "No QA PASS … is claimed" is not carried |
| PD-4 | IF-4 entrypoint and reconciler (ID-8) | `publish_crd_close_run_family(config, results, *, captured_at_utc=None, coherence_verifier=None)`, a Python API like `publish_crd_check_family` (HDE Mechanics Guide §1.6.3 calls that one "a Python API, not a new CLI"). It refuses a non-admitted ID or foreign root, requires the CRD's recorded QA family (`validate_crd_check_family`), refuses existing incoherence (`_run_once(check=True)`), then in one `_WriteTransaction` removes stale members, writes the primaries, converges, re-validates the family and runs the verifier. The given results replace the whole family (Plan restart rule for T5). `_load_crd_qa_entries` accepts `…/close/<check_id>/primary.log` rows and adds current close rows. The family's members are the primaries on disk, in a closed shape: `close/<check_id>/primary.log` plus its path proof, anything else refused | The Index derives from files on disk, as for the catalog pair; no close-run manifest is added (IF-4 names only primaries and proofs) |
| PD-5 | Epic close-run family (ID-8) | Not admitted; a stated limit in the ADR | No Epic QA root is admitted, and the measure needs only HDE-CRD-0002's close |
| PD-6 | Registration form (ID-9, ID-11) | `_crd_close_pack_entries`, for every row of `ADMITTED_CRD_QA`: neither file present, no rows; both present, rows `hde_crd_nnnn.close_report` and `hde_crd_nnnn.manifest` with `crd_id`; one present → `CRD_CLOSE_PACK_INCOMPLETE:<id>`; a retained row whose file is gone → `CRD_CLOSE_PACK_INDEXED_BUT_ABSENT:<id>`; a colliding row → `CRD_CLOSE_PACK_REGISTRATION_COLLISION`. Classifier: one entry `schemas/close_candidate_source.v2.json` → `tests/qa/test_generate_epic_close_pack.py` beside v1's | Mirrors the Epic rows' key style and `epic_id` field with `crd_id` (allowed by PF12 §8.3 and `check_mirror_schema.sh`); no new admission table |
| PD-7 | ADR text (ID-12) | `docs/adr/hde/close_pack_writer_adr.md`, status `Proposed`, in the companion diff: problem, eight numbered decisions, dependency direction, HDE-EPIC039's rationale weighed, alternatives, stated limits, Epic-only inventory, affected canon with locators and drainage statements, nonclaims, rollback | The precedent's form (`release_attestation_scaling_adr.md`); not indexed, like the precedent |
| PD-8 | OBS-17 (ID-14) | Diagnosed in the prototype, not reproduced (§12.5); recorded with what was tried | Bounded as ID-14 requires |
| PD-9 | HDE-EPIC039's source pin | `test_source_commit_hash_and_feedback_dependencies_do_not_enter_outputs` forbids `orientation_demo`, `path_proof` and `audit/qa/` in the writer's source. The v2 block names them only to refuse them as inputs and to derive the canonical QA-manifest pointer. The test keeps every v1 assertion on the v1 text and asserts the v2 block contains none of the remaining forbidden names | This is the neutral-writer reversal S21 must weigh (Specification constraint "Close-pack writer"); the ADR records it |
| PD-10 | `qa_harness.py` (ID-8) | One keyword `family` ("checks" default, "close" only for a CRD) on `_primary_log_content`, `_parse_crd_primary` and `_require_v2_primary_self_binding`; a guard `_require_primary_family` (+12 lines net) | A close-run primary is the same PF27 v2 step-log header as a check primary, bound to its own path; no second format |
| PD-11 | Model selection | The writer peeks at the source's `schema_version` after building the tree. A readable v2 source takes the v2 loader; anything else takes the unchanged v1 path, which raises v1's own refusals in v1's order. The manifest reader selects the identity field by the manifest's `schema_version` | v1 output and error precedence stay byte-for-byte; the 405 v1 cases pass unchanged except the pin in PD-9 |
| PD-12 | Free-text structure | Every v2 string passes v1's `REPORT_BODY_PROHIBITED_RE` (no headings, fences, lists, link definitions, `<`/`>` or controls): `REPORT_SECTION_AMBIGUOUS` | Keeps the report's section topology unique (Audit §6 S21 "Risks") |

## 6. Real-input sets (ID-2; addendum 2.11 rules 4 to 6)

| Component | Real inputs | Outside the set: one refusal or stated limit |
| :- | :- | :- |
| v2 schema and writer | A v2 source tracked at a clean HEAD; the plan and evidence files it names. First real source: `audit/HDE-CRD-0002_close_candidate_source.json`, authored at T1 from the approved Specification (S01 to S22, bound by reference), the Plan, the QA family and the two ledgers. Environments: local clone under closed rails with CI's install; the hosted closeout job with `jsonschema==4.23.0` only (the writer's imports are stdlib plus `jsonschema`, proven in §12.3) | Other schema versions → v1 path → `SOURCE_SCHEMA_INVALID`; other identity forms → schema refusal; untracked, symlinked, changed or empty inputs → v1's existing refusals; prohibited causal inputs → `CAUSAL_INPUT_PROHIBITED`; feedback terms → `FEEDBACK_DEPENDENCY_PROHIBITED`; structural text → `REPORT_SECTION_AMBIGUOUS`; postures beyond the three PF12 names → schema refusal (stated limit) |
| v1 path | Any v1 source (none is tracked on `main`) | Unchanged |
| Close-run entrypoint | `CheckResult`s the close session builds from its own captured T2 to T4 runs, for an admitted CRD whose QA family exists | Non-admitted ID, foreign root, nested transaction, empty or duplicate family, missing QA family → `ValueError`/`RuntimeError` before any write; a verifier failure → rollback |
| Close-run reconciler | `audit/qa/<crd>/close/<check_id>/primary.log` and its path proof | Any other member, a symlink or an empty root → refusal |
| CRD close-pack rows | `audit/HDE-CRD-NNNN_close_report.md` and `_MANIFEST.json`, written by the writer at T2 | One file only, or an indexed row whose file is gone → refusal |
| No emulation (rule 6) | The writer's in-process git reader is HDE-EPIC039's, unchanged. New code reimplements no external system; the rehearsal uses the real git and the real tools | — |

## 7. Canon map (§9.6)

| Canon element | Source field | Renderer output | Test |
| :- | :- | :- | :- |
| C1 canonical filenames (PF06 §3.5.2.1) | `change_id` | `_derived_paths_v2`: `audit/EPIC-NNN_*` or `audit/HDE-CRD-NNNN_*` | CRD and Epic dry runs |
| C1 exact-source acceptance | `acceptance[]`, `requirements_binding`, `evidence_inputs[]` | "Exact-source acceptance": criterion, result, evidence bindings, limitation; the requirements document by digest under "Source bindings" | CRD dry run (22 real IDs); `REQUIREMENT_ID_UNBOUND`, `BINDING_UNRESOLVED`, `ACCEPTANCE_AMBIGUOUS` |
| C1 verification statement | — (derived) | "Close-pack verification" | CRD dry run |
| C1 TI mapping | `tracked_issues[]` | "Tracked-issue closeout mapping", or "No TI item is cited" | CRD dry run |
| C1 binary decision; follow-ups; superseded | `closure_decision`, `follow_ups[]`, `superseded[]` | QA Rails lines; "Follow-ups"; "Superseded artifacts" | dry runs; `DECISION_CONTRADICTION` (both directions) |
| C4 deliverables, deferrals, later-drain (PF12 §1.2) | `deliverables[]`, `deferrals[]`, `later_drain_statements[]` | "Delivered scope", "Deferrals", "Later-drain PF-canon update statements" plus the fixed support-record line | CRD dry run; `DEFERRAL_UNBOUND` |
| C4 decision posture | `closure_decision.posture` | "Decision posture: …" in PF12's words | CRD dry run |
| C4 QA RCA | `qa_rca` | "QA RCA and Doc Delta summary", embedded or by binding | CRD dry run; rehearsal (embedded) |
| C4 supporting ledgers | `key_outputs`, `pointers`, `evidence_inputs` | the doc-delta, drain-target and QA-manifest paths required in all three | `OUTPUT_BINDING_MISMATCH`, `POINTER_MISSING` |
| C5 `key_outputs` (PF12 §1.2; PF14 §37.3) | `key_outputs` | manifest `key_outputs`: a JSON object of path strings | CRD dry run asserts object and string values |
| C6 "Key outputs" section; manifest points to report; no drainage prerequisite (PF14 §37.2) | `key_outputs` | "Key outputs" section; manifest `outputs.close_report` with SHA-256 and size; later-drain statements stated as support records | dry runs |
| C7 verbatim heading and pointer list (PF19) | `pointers[]` | `## QA Rails — Open/Close (Final PR)`; "Acceptance and evidence pointers" as literal strings | dry runs assert the exact headings list |
| C7 same-run evidence under the QA root (PF19) | — | the close-run family (IF-4) | updater tests; rehearsal T5 |
| C2 feedback-free lifecycle (PF06 §3.5.1) | every causal string | — | feedback, HEAD and prohibited-input refusals; rehearsal ("no hosted byte") |

## 8. Files and requirement-to-change/test map

| Path | Change (prototype, lines) | Tests |
| :- | :- | :- |
| `schemas/close_candidate_source.v2.json` (new) | 500 lines, generated from v1's `$defs` so the feedback pattern is byte-identical | `test_v2_schema_is_closed_and_shares_the_v1_feedback_refusal` |
| `schemas/epic_close_candidate_source.v1.json` | unchanged | existing v1 cases |
| `tools/qa/generate_epic_close_pack.py` | +496/−6: v2 block (constants, `CandidateModelV2`, loader, semantics, renderer) and four seam edits (`_validate_schema` `schema_rel`, `_load_model` dispatch, `_render_candidate` dispatch, manifest-reader identity) | 10 new tests, 54 new cases; 405 v1 cases |
| `tests/qa/test_generate_epic_close_pack.py` | +396: `CRD_0002_REQUIREMENTS` (the 22 real rows, copied verbatim, so the test does not depend on `docs/ephemeral/`), fixtures, the tests below; PD-9's pin narrowing | 459 cases pass |
| `tools/evidence/update_evidence_index.py` | +168/−2: reconciler accepts close rows; `_crd_close_run_entry`, `_crd_close_run_check_ids`, `_crd_close_pack_entries`, `publish_crd_close_run_family`; two lines in `_load_human_index` | 4 new tests |
| `tests/evidence/test_evidence_index_missing_state.py` | +138 | 37 tests |
| `tools/qa/qa_harness.py` | +17/−5 (PD-10) | updater tests; QA harness tests |
| `ci/checks/classify_ci_changes.py` | +3 (one owner entry) | rails workflow test (unchanged pins hold) |
| `docs/adr/hde/close_pack_writer_adr.md` (new) | 71 lines | acceptance (5) by reading |

New writer tests: schema closed and shared refusal; CRD dry run (all 14 headings in order, pointers, decision, posture, the 22 IDs, deferral, later-drain vocabulary, manifest `key_outputs` object of strings, report digest, check leaves bytes and status unchanged); Epic dry run (`EPIC-041` prefix); real S06 text refused when copied; 30 feedback cases across five free-text fields (schema and runtime); HEAD refusal at v1 parity; 7 prohibited causal inputs; 10 semantic refusals writing nothing; check refuses an edited committed report (`REPORT_HASH_MISMATCH`); unknown version keeps v1's refusal.

New updater tests: CRD close-pack rows absent-tolerant (none: Index byte-unchanged after write; one: refused, nothing written; both: rows and proofs, all six read-only checks pass; removed after indexing: refused); close-run family publishes without touching the QA manifest or `checks/` primary (bytes and mtimes compared), rows and proofs exist, the six checks pass, and a smaller family replaces the larger; publication refused without a QA family and for HDE-CRD-0003, and a verifier failure restores the whole tree (metadata compared); an unexpected member is refused by `--check`.

| Requirement or note | Acceptance | Proof (this plan's prototype) |
| :- | :- | :- |
| S21 report and manifest for an Epic or a CRD, from tracked inputs | (1), (2), (3) | writer tests; rehearsal T2 and T4 |
| S21 close-run home that leaves the QA manifest closed | (4) | updater tests; rehearsal T5 (`git diff C2 C3` over the QA manifest and `checks/` empty) |
| S21 ADR approved | (5); AQ-1 | ADR draft; Product Owner |
| Plan "Terminal-state reachability" | (7) | rehearsal (§12.2) |
| M1 | (4), (7) | registration tests; rehearsal T3 |
| CD-1; PF12 §1.2 inventory | (1) | CRD dry run; ADR inventory |
| Lanes | (6) | hosted CI at PR-35 |

## 9. Implementation sequence for PR-30

1. **Recover before creating.** Inspect this session's checkout, branches, worktrees, open PRs and `docs/ephemeral/` for WU-PR-07 work. Expected: none beyond this plan.
2. **Branch.** From current `origin/main`, on the session's designated branch. If `main` moved past 6f53552 outside `docs/`, re-run §4's measurements first and record any difference.
3. **Apply** the companion diff (`git apply --check`, then `git apply`). Any hunk that fails is applied by hand to the same effect and recorded under ID-16.
4. **Local checks** (§11, items 1 to 5), in detached copies; each ends with `git diff --exit-code` and an empty untracked status.
5. **Rehearsal** (§11 item 6) from the PR-30 head, with the scratch driver recorded in the PR-30 result.
6. **Commit** once: `feat(close-pack): v2 close-pack writer for Epic and CRD identities, close-run family, ADR draft (HDE-CRD-0002 WU-PR-07 S21)`.
7. **Replay** `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit (option A line, ID-17).
8. **Publish** the PR. The description follows `.github/pull_request_template.md` with the `AGENTS.md` content rules and states AQ-1 as pending.
9. **Result record** `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.0.md`: `PR_CANDIDATE_PUBLISHED`, the H-1 close sequence (§13), checks with counts, rehearsal facts, replay line, spend, nonclaims. Hand off to PR-35 in its own session.

**Integration seams:** the writer's four seam edits (PD-11); the updater's `_load_human_index` (two lines) and `_load_crd_qa_entries` (the close branch); the harness's `family` keyword. **Dependency order inside the PR:** harness keyword → updater → writer → tests → classifier → ADR (one commit).

## 10. PR split and merge dependencies

- **One PR.** The ceiling allows one, and the unit is one coherent change.
- **Before merge:** AQ-1 decided by the Product Owner (a different decision revises this unit, through RS-10 where it changes the bounded scope); PR-35's `MERGE_PENDING`.
- **Order:** after WU-PR-06 (accepted); before WU-PR-08, which runs the updater after the `1.4.0` cut and relies on H-2.
- **No release member changes** (§12.4), so no refresh is owed (addenda 2.6 to 2.8).

## 11. Validation PR-30 runs (and PR-35 re-runs where §3 says)

Environment: CPython 3.12 with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`), `ruby`, `bash`, `curl`, git; closed rails; vendor, database and GitHub keys and `ENGINE_ENV` unset; `XDG_STATE_HOME` an empty scratch directory; tests with `PYTHONPATH` set to the copy under test (OBS-W5-5).

1. `python -m pytest -q -p no:cacheprovider tests/qa/test_generate_epic_close_pack.py` (459 cases expected), then the OBS-17 test alone 50 times.
2. The 24 updater consumers and `tests/qa/test_generic_qa_harness.py` in one run (ID-15).
3. `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py`.
4. On the candidate head: `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_final_lf.sh`, and `git diff --stat <base> HEAD -- docs/evidence artifacts audit` empty (Index trio byte-unchanged, ID-9).
5. `prepush_check.py --base <base> --head HEAD lanes membership` with every changed path.
6. The rehearsal: two fresh runs and an idempotent re-run on C3 (§12.2).
7. `prepush_check.py … --full replay` (item 7 of §9).

## 12. Prototype record (throwaway clones under the session scratchpad; the session checkout was not changed)

All runs: closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), CPython 3.12.3, git 2.43.0, a scratch venv with CI's install. The prototype was committed only inside its scratch clone (head c0240b6 over 6f53552). Every copy ended with an empty `git status --short`.

### 12.1 Tests

| Run | Result | Time |
| :- | :- | :- |
| Writer test file (prototype) | 459 passed, exit 0 | 77 s |
| Updater close tests (`-k close`) | 4 passed, exit 0 | 34 s |
| Lanes, prototype head vs 6f53552 | `reason=selected_lanes;paths=8;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets | 5.3 s |
| Membership (the 6 code and doc paths) | none is a member (release 1.3.0, 45 members, `release_id` 77204764…) | 3.5 s |
| Full-validation replay (`prepush_check.py --base 6f53552 --head HEAD --full replay`, detached copy of c0240b6) | exit 0; `ci.yml` sha256 d02021f3… (the pinned one); `hdctl` resolves to the copy's `engine/cli/main.py`; all 16 steps SUCCESS (1, 4, 5 excluded and substituted); changed tests 4,077 passed (full validation); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 with the attestation built and verified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "copy after replay: clean"; repository unchanged | 14:17:09Z to 14:49:49Z (step time 1,947 s) |
| The 24 test files that reference the updater, plus `tests/qa/test_generic_qa_harness.py` and `tests/evidence/test_http_reader_ci_ownership.py`, in one run (ID-15) in a detached copy of c0240b6 | 1,636 passed, exit 0; copy status and diff empty afterwards | 14:50:06Z to 15:08:02Z (1,074 s) |

### 12.2 T0 to T6 rehearsal (acceptance (7))

Driver: a scratch script that clones the prototype head into a fresh directory and runs, with the real tools and the real git:
- **T0** `publish_crd_check_family` for HDE-CRD-0002 with two real executed checks (`ci/checks/check_env_pins.sh`; `update_evidence_index.py --check`), committed as C0 (a stand-in for the recorded QA verdict).
- **T1** the candidate source (22 real criterion IDs bound by reference to the real Specification in the clone; the Plan v1.1 path; the QA manifest and both check primaries; the two ledgers) and the ledgers, committed as C1.
- **T2** writer `--write`; **T3** updater write; committed as C2.
- **T4** on clean C2: writer `--check`, updater `--check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_final_lf.sh`.
- **T5** `publish_crd_close_run_family` from the nine captured T2 to T4 runs, committed as C3.
- **T6** the T4 set again on clean C3, then the read-only set with a `jsonschema`-only interpreter.

| Fact | Run 1 (14:05:35Z to 14:06:47Z) | Run 2 (14:07:03Z to 14:08:05Z) |
| :- | :- | :- |
| Every T0 to T6 command | exit 0 (50 commands) | exit 0 (50 commands) |
| C3 contents (against C1) | close report, manifest and 9 close-run primaries, each with a path proof (11 new proofs); 11 new Index rows (623 → 634) | same |
| QA manifest and `checks/` between C2 and C3 | unchanged (`git diff` empty) | unchanged |
| Re-run T2, T3 and T5 on clean C3 with the same captures | no byte changed (`git status` empty) | no byte changed |
| Writer `--check` with `jsonschema` only (as the hosted job) | exit 0 | exit 0 |
| Updater `--check` with `jsonschema` only | exit 1, `ModuleNotFoundError: No module named 'flask'` (F-1) | same |
| `orientation_demo.py --check`, `validate_evidence_paths.py` with `jsonschema` only | exit 0 | exit 0 |
| Hosted CI | not used; no byte of C3 comes from it | same |

**Byte stability between the two fresh runs** (tree 8b48392a vs 540cd70b): the close report, the manifest, `docs/evidence/INDEX.json`, `INDEX.sha256`, the orientation output and every close-run primary are byte-identical. The only differing bytes are clock provenance: the `mtime_utc` and `produced_at_utc` lines of 17 path proofs and the Mirror lines that embed them (the self-record, its SHA-256 sentinel and the Mirror's own proof). `AGENTS.md` "Path-proof portability" makes `mtime_utc` capture-time provenance, not a correctness input. Within one checkout the sequence is a fixed point: re-running it changes nothing.

**F-1 fix substantiated, not applied:** with an interpreter that has only `-r requirements.txt` (no editable install), all seven of the closeout job's check steps exit 0 on run 1's C3, and the tree stays clean.

### 12.3 Writer imports

The v2 block adds no import. The writer's `--check` passed in an interpreter holding only `jsonschema==4.23.0` and its dependencies (`attrs`, `jsonschema-specifications`, `referencing`, `rpds-py`, `typing_extensions`).

### 12.4 Change set facts

8 paths, +1,789/−13. No path under `docs/evidence/`, `artifacts/`, `audit/`, `catalog/`, `.github/`, `requirements*`, `pyproject.toml` or `pytest.ini`. No release member.

### 12.5 OBS-17 diagnosis (ID-14)

- **The hosted failure, read whole** (run 39345008218, job 118375390428, on 7a3b7b2): during a 3,946-test changed-tests step, after the test's recovering `--write` (exit 0) and its `git add` and commit, the final `--check` failed with `EPIC_CLOSE_PACK_ERROR:MANIFEST_BINDING_MISMATCH` and then `CHECK_MODE_MUTATION`.
- **Tried:** 200 runs of the test alone, 4 in parallel (13:57:04Z to 13:58:39Z): 200 passed. 80 runs, 2 in parallel, while two full writer-test runs ran alongside (13:59:32Z to 14:00:49Z): 80 passed; both load runs 405 passed. No recurrence in 280 runs.
- **Reading:** `MANIFEST_BINDING_MISMATCH` in `_read_manifest_committed_pair` means the committed manifest bytes differ from a fresh render, or the report's mode or parent differs. The recovering `--write` had verified the pair before printing OK. The failure therefore points at what the test's `git add` staged, not at the writer's render. One difference is unexamined: the hosted runner had git 2.55.0, while local runs used git 2.43.0.
- **Disposition:** mechanism not established. The OBS-17 path is v1 and unchanged in behaviour by this unit. PD-11's manifest-reader edit only selects the identity field. The test is never skipped. A recurrence on this unit's PR is a red run that PR-35 root-causes. Owner otherwise: the QA tool and test owner, through the IA.

## 13. Interface contracts (instruction §8)

- **H-1 Close sequence** (for HDE-CRD-0002's close mutation set; PR-30's result restates it against the published code):
  - T1: author `audit/HDE-CRD-0002_close_candidate_source.json` (v2), `audit/docdeltas/hde-crd-0002_doc_deltas.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md`; commit C1.
  - T2: `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --write`.
  - T3: `python tools/evidence/update_evidence_index.py`; commit C2.
  - T4: the seven checks of §12.2, each captured (argv, exit code, output).
  - T5: in Python, `publish_crd_close_run_family(HarnessConfig(crd_id="HDE-CRD-0002", repo_root=ROOT), results, captured_at_utc=<T4 capture time>)`, with one `CheckResult` per T2 to T4 run; commit C3.
  - T6: the T4 set again.
- **H-2 Absent-tolerant registration**: as PD-6.
- **H-3 IF-4 family**: as PD-4; keys `audit.qa.hde_crd_0002.close.<check_id>.primary.log`, role `log`.
- **H-4 Writer usage and posture** (WU-DOC-01): v2 schema, both identities, the outputs, the four nonclaims, the stated limits of the ADR.
- **H-5 ADR**: §5 PD-7.
- **H-6 Validation workflow**: inputs unchanged; the writer stays runnable with `jsonschema==4.23.0` only (proven). The job's evidence-check step fails today (F-1).

## 14. Security and migration

- Closed rails for every run; `CLOSED_RAILS_REQUIRED` kept. Close-run primaries record command argv, exit code, output and the rails pins (`captured_env` admits only those keys); no secret, key value, birth input or user identifier.
- Source paths are validated tracked, regular and non-symlinked (v1 rules). The close-run entrypoint writes only under the admitted root's `close/` and the Index trio and companions, inside one recoverable transaction.
- The Codex code review is in the chain; the Codex security review is not (addendum 2.3).
- Migration: none. v1 stays; no close pack, Index row or QA record is rewritten. Rollback: the Product Owner's revert of the squash commit.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| AQ-1 decided differently from the draft | The unit is revised before merge; RS-10 where the bounded scope changes |
| OBS-17 recurs on the PR | PR-35 root-causes it from the hosted log; never skipped |
| A Codex finding on a constructed input | Rule 7: traced path and stated limit; rule 8 after two same-class rounds |
| `main` moves before PR-30 | §9 step 2 re-measures; outside `docs/`, any change to a unit path is reconciled before applying |
| The ceiling is projected to pass | Return to the Product Owner before continuing |
| Interruption | Resume in this session from the last saved artifact; prototypes and rehearsals run only in throwaway clones |

## 16. Findings for the Product Owner

**F-1. The hosted closeout-validation job cannot pass its evidence-check step for any candidate.**
- **What it is.** `.github/workflows/epic-closeout-validation.yml` is the manual, read-only `workflow_dispatch` that HDE-CRD-0002's close runs at T7 (Plan v1.1 (e)) on the exact close head, before the Product Owner merges the close PR.
- **What breaks.** The job installs only `jsonschema==4.23.0`. `update_evidence_index.py --check` imports `tools/evidence/generate_a7_transport_proofs.py`, which imports Flask at module level, so the step "Run retained read-only evidence checks" exits 1. Proven at 6f53552 and on the rehearsal's C3. The job has never been dispatched. Without a fix, HDE-CRD-0002's close fails its measure ("every check mode passes") at T7.
- **Not this unit's approved scope.** The instruction lists the workflow as expected unchanged (§6), and a needed change there is a rescope trigger (§14). Plan v1.1's deliverable names the workflow only "where they read the schema version".
- **Options:**
  - **A. Fold it into WU-PR-07 (recommended).** One line: the install step becomes `python -m pip install -r requirements.txt`. Proven: all seven job checks pass with that install on C3. Route: I write an RS-10 rescope proposal in this session; the IA reviews it through RS-20; this plan gets a v1.1 with the line, and the Proceed is given against v1.1. Cost: the RS-20 review is session 3 of 4, leaving no slack after PR-35.
  - **B. Proceed on v1.0 as it stands, and fix the workflow separately** before HDE-CRD-0002's T7. The ceiling keeps one session of slack, but the fix needs its own vehicle and route later.
  - **C. Change T7** (drop or replace the hosted dispatch): a change to the approved Plan's terminal-state design, through RS-10/RS-20 or the Plan's owner.
- **Recommendation: A.** It is the cheapest complete path to the measure, and the fix is one proven line in the same lanes this PR already runs.

## 17. Carried items (instruction §15)

| Item | Disposition |
| :- | :- |
| §9.1 choices | Made (§5) |
| AQ-1 | Pending; the Product Owner decides before merge |
| M1 | Built (PD-6), tested, rehearsed |
| "Unknown pending discovery" | Confirmed: neither the workflow nor a release-sanity stage reads the schema version. New fact F-1 |
| OBS-17 | Diagnosed, not reproduced (§12.5) |
| LR-O2 | §11 item 2; 12 of the 24 consumers are not changed-test targets, so they run explicitly |
| Option A line | PR-30 and PR-35 record each replay; PR-40 states it |
| Ceiling | §3 |
| LR6-O2 | Read by wording; no decision depends on it |
| LR6-O5 | This unit does not edit `ci.yml`; F-1 option A edits a different workflow, so the pin is unaffected |
| OBS-W5-5; OBS-4, OBS-14 | §11 environment; tests only in copies |
| HDE-EPIC040 close records | Not reopened; no retroactive close pack |
| WU-PR-08's S01 fact | Not this unit |
| `release_id` 77204764…, 45 members | Unchanged; no member touched |
| Other OBS and S19 items | Their owners, not this unit |

## 18. Documents this change makes stale (not changed here)

| Document | Owner |
| :- | :- |
| `AGENTS.md` "HDE-EPIC039 current workflow posture" (the generic writer's description) | WU-DOC-01 (Product Owner instruction needed to edit `AGENTS.md`) |
| `README.md` line 25 | WU-DOC-01 |
| HDE Mechanics Guide §1.6.3 (CRD publication interface) and §37.2; HDE Schemas & Artifacts §1.2; Change Process Guide §3.5.2.1; Glow QA Guide close-pack sections | PF drainage owners, after AQ-1 (the ADR lists them) |
| `docs/qa_harness_pattern.md` (names only `publish_crd_check_family`) | WU-DOC-01 |

## 19. Canon-conflict register

Carried unchanged: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (a) (IA through RS-20); CR-7, CR-8 APPROVED (a) each (Product Owner). No new conflict. The instruction's three non-conflicts stand: the `key_outputs` string-value reading, the ADR-covered S21 canon change, and PF14 §37.2's EPIC-025-only generator line. HDE Mechanics Guide §1.6.3's statement that updater CRD admission is limited to HDE-CRD-0001 is earlier canon already overtaken by S22 and addendum 2.5 for HDE-CRD-0002. The close-run family is the ADR-covered change.

## 20. PR-30 and PR-35 obligations

- **PR-30** (this session, after the Proceed for exactly v1.0, or v1.1 if F-1 is folded in):
  - recover existing work first;
  - implement only §8's files from the companion diff;
  - run §11;
  - commit once, publish the PR and record the replay;
  - write the result record with spend;
  - return `PR_CANDIDATE_PUBLISHED`, handing off to PR-35 in its own session.
  - It does not resolve reviews, wait for CI readiness or merge.
- **PR-35** (its own session):
  - retrieve the Codex code review findings and disposition them under rule 7 (rule 8 after two same-class rounds; declining a P1 or security finding goes to the Product Owner first);
  - push coherent corrections and re-run §3's re-run set, recording each replay;
  - verify current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
  - state AQ-1 in the PR description and record spend;
  - return `MERGE_PENDING` without merging.
- **Nonclaims every record keeps:**
  - the writer and the family are capability only;
  - no close pack of any change is produced;
  - no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure;
  - no canon edit;
  - the ADR is `Proposed` until the Product Owner decides.

## 21. TypeSafe reading for the receiving session (PR-30, WU-PR-07)

Action sent (v8.2): "Implement, in a dedicated session, one work unit from a new detailed PR plan that the Product Owner has proceeded: apply an already prototyped change of about 1,700 lines across five code files and two test files (a new candidate-source schema version, a second model inside an existing 3,900-line close-pack writer, a close-run evidence entrypoint and an absent-tolerant registration in an existing 5,200-line evidence updater, a small QA-harness keyword, one CI-classifier registration) plus one architecture decision record draft; a task list and a prototype diff exist; run the unit's tests, an end-to-end rehearsal in a throwaway copy and a full local CI replay, then commit and open the pull request; no live provider call occurs; an automated code review, a separate merge-readiness session and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.81 (confidence 0.72); rung probabilities low 0.00, medium 0.02, high 0.26, extra high 0.60, max 0.12, ultracode 0.00. Model probabilities Fable 5.1 0.05, Opus 5.5 0.94, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.92). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.013, Fable 5.1 at extra high 0.030, Fable 5.1 at max 0.006, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.244, Opus 5.5 at extra high 0.564, Opus 5.5 at max 0.113, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.003, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T14:23:47Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-20T14:23:47Z; HTTP 200 in 0.73 s; 5525 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Superseded reading.** A first reading at 2026-10-20T14:17:48Z used an action text that stated the change size wrongly ("about 1,300 lines"; the prototype is 1,718 added lines of code and tests). It read Opus 5.5 at extra high (score 2.79, confidence 0.74; rungs low 0.00, medium 0.02, high 0.26, extra high 0.63, max 0.09, ultracode 0.00; models Fable 5.1 0.04, Opus 5.5 0.95, Sonnet 5.5 0.01, Haiku 5.5 0.00). It is kept as history; the reading above, with only the size corrected, is the record.
- **Records.** Run with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `implementation`, before this plan was saved. The Notion row was not written (addendum 2.1). Nathan's pick for PR-30 is not stated; his pick for this PR-20 session is not stated.

**Surface advice:** PR-30 continues in this same top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with GitHub access for the PR. Its environment needs:
- CPython 3.12 with CI's install, which needs package-index access;
- `ruby`, `bash`, `curl` and git;
- closed rails, with the vendor, database and GitHub keys unset;
- throwaway clones outside the checkout for every write-mode run.

Observed times: the writer test file takes 77 s, a rehearsal run about 70 s, and a full replay about 25 minutes. No live vendor, production or database access is needed. This plan's pull request should be merged first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / PR-20 / plan 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-PR-07 PR engineering session / PR-20 |
| capture time | 2026-10-20T15:08:33Z |
| execution identity | https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF |
| inherited usage | instruction v1.0 (PR-10, session_01CCKsYD2yX5WgU3biWKb59j); the Product Owner disposition (session_012tPq26JWVhCYZmcqTidpV2) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at 6f53552 (`docs/pfcanon/` unchanged since 043fa91).

| Topic | Sources and sections |
| :- | :- |
| Plan authority and content | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); HDE Governance §9.1.1, §9.1.2 and §9.7.3, as the instruction cites them |
| Overlays | PF10-HDE-Build-Notes v13.6.3: addendum 2.11 in full (rules 1 to 8; scope; effects on WU-PR-07); 2.12 in full (the numbering of 2.11; decisions 1 to 5); 2.5, 2.3 and 2.1 through the instruction |
| Close-pack files, lifecycle, canon change | Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.4.md`) §1.0.5, §1.0.6, §3.5.1 "Requirement" ("Feedback-free terminal lifecycle", "Exceptional closure record"), §3.5.2.1, §3.5.2.3 |
| Close-pack artifacts and identities | HDE Schemas & Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §1.2 "Close-pack artifacts", "Change-container compatibility (normative)", the supporting-ledger and deferral rules, "Close-pack manifest key_outputs (named binding map; normative)" |
| Close-pack mechanics; CRD publication interface | HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §37.2 "Governance & homes" (close report, doc deltas, manifest, generator, drainage posture), §37.3 "Conventions" (`key_outputs`), §1.6.3 "Current-family validation and publication" |
| Close report and same-run evidence | Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.6.md`) "Close-pack truthfulness and same-run execution (normative)", "Close report requirements (validator-bound; mechanical)" |
| In-flight documents | the instruction v1.0 in full; Plan v1.1 §7 WU-PR-07 block in full; the Product Owner disposition in full; the Specification's requirement table; Audit §8 AQ-1 |
| Operative documentation | `AGENTS.md`: canon-first rule; "HDE-EPIC039 current workflow posture"; "Evidence harness" and "Governed evidence rules"; "Path-proof portability"; closed rails and redaction; "Code review guidelines" and "Code review scope"; "PR descriptions" |

Silence: canon has no rule for a close-run evidence family; the Specification and the ADR govern it.
