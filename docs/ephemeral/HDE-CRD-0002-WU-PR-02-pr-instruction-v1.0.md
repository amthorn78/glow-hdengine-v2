---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-02-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review); addendum 2.1 governs §19 only. Addenda 2.2 and 2.4 are scoped to WU-PR-01 and change nothing in this unit; their downstream items are carried in §15
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c) — lineage; §5 below re-verifies and in two places corrects its facts
predecessor_unit_acceptance: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v2.0.md (PR-40 ACCEPT of WU-PR-01; landed at 4fc9fea, #631); recorded in PF10 addendum 2.4
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5, effective 2026.10.13; blob c98831e8112d; 50,181 bytes; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full: v13.5.4 read in full earlier in this IA lineage plus the complete v13.5.4→v13.5.5 diff, which changes only the version line and the index and appends addendum 2.4)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md §2.3 (record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md); §2.1 for §19
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (the session of Plan v1.1 and of the WU-PR-01 lineage reviews)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1"; read 2026-10-13)
created_at: 2026-10-13T15:52:05Z
repository_baseline: origin/main cc3dc337b554a26dfbc59d2d1464bdb6e31d0f7b (Product Owner direct-main commit "PF10 update", adding PF10 v13.5.5 over #631 at 4fc9fea); every code fact in §5 measured there
receiver: dedicated HDE-CRD-0002 WU-PR-02 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); no new entry (§16)
---

# HDE-CRD-0002 WU-PR-02 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-02 of HDE-CRD-0002, issued by the whole-change IA from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- author the detailed per-file plan (PR-20's output);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-02 (Plan v1.1 §7 heading "WU-PR-02 — Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation)") |
| Requirements | S06, S11, S12, S13, S22; CD-3 (resolved by S22) |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above) |
| Overlays | PF10 addendum 2.3 (reviewer chain). Addendum 2.2 (WU-PR-01 rescope) and 2.4 (WU-PR-01 ACCEPT) are not overlays on this unit |
| Upstream unit | WU-PR-01, accepted (lineage review v2.0) |
| Phase | Distillation |
| Live QA class | not production-affecting (Specification table; Plan §6) |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1 §1), permitting PR instructions in the Plan's dependency order.
- **Unit type.** PR unit.
- **Dependency state: ready.** Plan v1.1 §7: "Second; no code dependency on WU-PR-01; lands before WU-PR-07 (which extends the same updater) and before any member-changing unit's convergence relabels rows." WU-PR-01 is accepted (lineage review v2.0 §10). AQ-1 gates only WU-PR-07's merge. No QA Guide, QA Plan or Ops receipt is a prerequisite.
- **Order.** WU-PR-01 → **WU-PR-02** → WU-PR-03 → WU-PR-04 → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7).
- **Downstream dependents** (contracts in §8): WU-PR-03, WU-PR-04, WU-PR-05 and WU-PR-08 (their manifest refreshes regenerate rows under this unit's label model); WU-PR-07 (extends the same updater with the close-run family); QA-10 readiness (S22 must hold before HDE-CRD-0002 enters QA).

## 4. Required behavior

Acceptance intents, verbatim from the approved Specification (Requirements table):

| ID | Scope | Acceptance intent |
| :- | :- | :- |
| S06 | Make the attestation builder's wheel stage work under Debian-patched setuptools | The release attestation builds under Debian-patched setuptools |
| S11 | Make the engine-core evidence currency test check release identity | The test fails when `release_id` drifts |
| S12 | Correct provenance labels on current-release captures in the Machine Mirror | Current-release captures carry current-release labels |
| S13 | Remove the closure admission probe's dependence on the ambient installed package | The probe's result depends only on the isolated closure's own sources |
| S22 | Extend the canonical evidence-index updater's CRD admission to HDE-CRD-0002's QA root | Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate |

Plan v1.1 §7 WU-PR-02 purpose (approved): "Repair the release-evidence tooling defects HDE-EPIC040 carried and admit HDE-CRD-0002's QA root to the canonical evidence graph before QA."

Approved interfaces this unit implements (Plan §5, verbatim):
- **IF-5 (S22).** "An explicit admitted-CRD table in `tools/evidence/update_evidence_index.py`: `HDE-CRD-0001 → audit/qa/hde-crd-0001, audit.qa.hde_crd_0001`; `HDE-CRD-0002 → audit/qa/hde-crd-0002, audit.qa.hde_crd_0002`; no directory discovery; publication refuses any other ID by name."
- **IF-7 (S12).** "Rows for captures the current release regenerates carry release-identifying fields (version and `release_id`, or an equivalent `release_binding`); frozen families unchanged (Audit EC-5)."

Approved engineering choice EC-5 (Audit §7.1): "Current-release capture rows carry release-identifying fields (version and `release_id`, or an equivalent `release_binding` field); origin keys stay; frozen families keep capture-time labels." The S12 invariant (Audit §6 S12): "a reader of the Mirror can tell a current-release capture from a frozen one without opening the file."

**Canon-conforming reading of IF-7 (binding; IA decision ID-1).** HDE Schemas & Artifacts §8.3 "Minimum record schema (reject unknown keys)" and "Allowed top-level keys and unknown-key rejection" close the Mirror's top-level key set: the seven core keys plus the optional metadata keys `epic_id`, `crd_id`, `record_type`, `schema_version`, `notes`, `tokens`; "all other keys are rejected" (CI-blocking). Plan §7's provision for "Mirror schema companions only if IF-7 needs a schema field" therefore has no lawful branch here: a new top-level key would contradict normative canon, and the Specification excludes canon changes outside S21's ADR. IF-7's "equivalent `release_binding`" is realized **inside the allowed key set**. PR-20 chooses the encoding (for example a `record_type` value, the `notes` text, or both), records why, and proves the invariant by test. No new top-level key, no Mirror schema change and no canon edit. If PR-20 finds the invariant cannot be met inside the allowed key set, that is a boundary finding for RS-10/RS-20 (§14), not a schema edit. This follows HDE Governance §9.1.2 (PF-Canon governs an in-flight document where they conflict); it opens no canon conflict, because the canon-conforming option is within IF-7's own wording.

**CRD identity in the Mirror (binding; IA decision ID-2).** HDE Schemas & Artifacts §8.3 requires that, "before the first affected CRD enters QA, the Machine Mirror schema and every serializer or validator enforcing this allowed-key set MUST accept `crd_id`, enforce the `epic_id`/`crd_id` mutual-exclusion rule, and preserve valid historical and active `epic_id` records". §8.17 requires every validator or helper "that accepts only epic identity or `EPIC_QA_ROOT`" to be updated before the first affected CRD enters QA. `ci/checks/check_mirror_schema.sh` (§5.5) enforces the allowed-key set but omits `crd_id`. S22 is the unit that admits HDE-CRD-0002's QA evidence before QA, so S22 includes bringing that validator into conformance: accept `crd_id`, refuse a record carrying both `epic_id` and `crd_id`, preserve every existing record. HDE-CRD-0002's QA rows keep the existing CRD row shape that `_crd_qa_entry` emits for HDE-CRD-0001 (core keys only); this unit does not add `crd_id` to any row and does not migrate HDE-CRD-0001 rows.

## 5. Current repository and reference baseline (verified at `cc3dc33`)

PR-20 re-verifies at its own head before planning edits; observed facts prove planning-time reality only (Plan Templates "Repository loci and file minting").

### 5.1 S06 — O-10 reproduced in this container

Method: an export of `cc3dc33` (`git archive`) and a clean clone detached at `cc3dc33`; closed rails via `env -i` (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, `PATH=/usr/bin:/bin`); the builder's own wheel command (`tools/evidence/build_release_attestation.py` lines 350–370: `sys.executable -m pip wheel --disable-pip-version-check --no-cache-dir --no-index --no-deps --no-build-isolation --wheel-dir <wh> <source>`).

| Interpreter | setuptools it imports | Wheel command | Full builder (`--output <external> --require-clean`) |
| :- | :- | :- | :- |
| `/usr/bin/python3` (CPython 3.13.16, not the distribution's interpreter) | 68.1.2 from `/usr/lib/python3/dist-packages` (Ubuntu `python3-setuptools` 68.1.2-2ubuntu1.2) | **exit 1**: `AttributeError: install_layout. Did you mean: 'install_platlib'?` from `self.set_undefined_options('install',('install_layout','install_layout'))` | **exit 1**, receipt `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}`; clone clean afterwards |
| `/usr/bin/python3.12` (CPython 3.12.3, the distribution's own interpreter) | the same 68.1.2 | exit 0; `glow_hdengine-0.0.0-py3-none-any.whl` | not run |
| a venv with CI's install (Python 3.12.3; `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`) | upstream setuptools in the venv | — | **exit 0**; `attestation.json`, `attestation.json.sha256`, `build.log`, `evidence/`; clone clean afterwards |

Correction to the Audit (§6 S06 "Not reproduced in this container"): O-10 is reproducible in the current cloud container. The failing condition is a non-distribution interpreter importing the distribution-patched setuptools; it is the same receipt PR05 recorded (`docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` §7.4, `/usr/local/bin/python`). The `/usr/bin/python3` above lacks the repository's runtime and test dependencies, so a full post-fix rehearsal needs an environment that keeps the patched setuptools as the build backend while making the other dependencies importable; PR-20 designs and records it (§10).

Other facts: `_clean_child_env` (lines 328–339) passes only `PATH`, `TMPDIR`, closed rails and `HDE_ISOLATED_RELEASE_BUILD=1`; the venv stage follows at lines 394–452; `pyproject.toml` `[build-system] requires = ["setuptools>=68", "wheel"]`, backend `setuptools.build_meta`. The design record `docs/adr/hde/release_attestation_scaling_adr.md` is unchanged by this unit.

### 5.2 S13 — closure probe

`tools/evidence/regenerate_identity_closure.py` (421 lines): `release_not_admitted_observed()` (lines 384–393) imports `engine.config.registry_loader` in-process and returns true only for `INCOMPLETE_RELEASE_ROSTER` (`RELEASE_NOT_ADMITTED_REFUSAL_CODE`, line 25). `_run` and `_is_current` (lines 330–350) run `sys.executable` with `cwd=ROOT`. Consumers kept by WU-PR-01 that this unit must not break: the closure selects `tests/evidence/test_internal_version_manifest_captures.py` (line 283) and `tests/evidence/test_aux_preview_identity_parity.py` (line 378); `tests/evidence/test_release_attestation.py::test_release_closure_does_not_run_epic_closeout_assertions` (lines 614–617) asserts the two retired EPIC022 tests stay absent from the closure source (lineage review v1.0 K-2; PF10 addendum 2.4).

### 5.3 S11 — engine-core currency

`tests/evidence/test_engine_core_evidence.py::test_current_proofs_bind_actual_sources_and_behavior` (lines 78–97) checks fixture kind, source digests, run equality, vectors and JSON-compare digests, and never reads `release_id`. `tools/evidence/generate_engine_core_evidence.py` builds the proofs from `synthetic_complete_release_root(..., source_root=ROOT)` and records `bundle.release_id` (line 143).

Correction to the Audit (§5.6 "writes `release_id` into all four payloads"): `release_id` appears **nested** in three payloads (`artifacts/core/two_run/identity.json` ×3, `abba/ab_ba_parity.json` ×4, `json_compare/core_result_json_compare.json` ×2); `artifacts/core/purity/purity_report.json` carries none. Every occurrence equals `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`, which is `identity_meta()["release_id"]` at `cc3dc33` (release `1.3.0`).

### 5.4 S12 — Mirror labels

- `artifacts/evidence_index.jsonl`: 620 rows; key set observed `artifact_key, discovered_physical_path, epic_id, notes, produced_at_utc, proof_anchor, record_type, role, schema_version, sha256, size_bytes, tokens`; **0 rows carry any release field**.
- Current-release captures are registered under origin families with origin labels, for example `epic038.pr02.endpoint_catalog*` (`"epic_id": "HDE-EPIC038"`, `record_type` `epic038_pr02_catalog_evidence`; updater lines ~2975–2990) and the CLI conformance rows (`CLI_CONFORMANCE_ARTIFACTS`, lines ~3331–3341, no metadata keys).
- The families a re-cut regenerates and the frozen families are listed in `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §6.3 (config family, canonical JSON gate, determinism family, open-rails fixture proof, A7 family, F07 writer artifacts, engine-core) and §6.4 (frozen: `artifacts/cli/showcompat/*`, `artifacts/cli/{ab,ba,summary}.json`, help/install captures, `artifacts/identity/*`, `artifacts/math/*`, `artifacts/parity/two_run_identity.log`, `artifacts/bodygraph/release_bindings.json`, `artifacts/runtime/env_matrix.snapshot.json`, `artifacts/vendor/*`, `audit/ops/*`, EPIC032 router captures, the §2.21 captures). Whole-change Plan §10 steps 4 to 9 name the same producers.

### 5.5 S22 — updater CRD admission and Mirror validator

- `tools/evidence/update_evidence_index.py` (4,981 lines): single-ID constants `CRD_QA_ID = "HDE-CRD-0001"`, `CRD_QA_ROOT_REL = "audit/qa/hde-crd-0001"`, `CRD_QA_KEY = "audit.qa.hde_crd_0001"` (lines 49–51, under "another CRD needs its own explicit admission"); `_crd_qa_entry` (3776; rows carry `artifact_key`, `discovered_physical_path`, `role` only); `_load_crd_qa_entries` (3789–3827; `HarnessConfig(crd_id=CRD_QA_ID)` at 3822); `publish_crd_check_family` (4897; refuses any other ID at 4911–4912, "governed CRD publication admits only HDE-CRD-0001").
- `tools/qa/qa_harness.py` line 23 `CRD_RE` already accepts any `HDE-CRD-[0-9]{4,}`.
- `audit/qa/hde-crd-0001/` exists; the Mirror has 11 HDE-CRD-0001 rows and the Human Index 1 match; `audit/qa/hde-crd-0002/` does not exist (QA creates it later).
- `ci/checks/check_mirror_schema.sh`: `REQUIRED_KEYS` = the seven core keys; `OPTIONAL_KEYS` = `epic_id`, `notes`, `record_type`, `schema_version`, `tokens` (**no `crd_id`**); extra keys fail with `KEYS_EXTRA` (lines 8–24, 96–102). No current Mirror row carries `crd_id`.
- Tests: `tests/evidence/test_evidence_index_missing_state.py` (`crd_repo` fixture and `test_crd_*` cases) and `tests/qa/test_generic_qa_harness.py` (`test_crd_*`).

### 5.6 Release membership, CI lanes and owners

- None of this unit's files is a release member: the 45-path `ADMITTED_RELEASE_ROSTER` (`engine/config/registry_loader.py`) contains no `tools/evidence/*`, `ci/checks/*` or `tests/*` path. No manifest refresh is needed (C-5).
- `ci/checks/classify_ci_changes.py`: `tools/evidence/build_release_attestation.py`, `regenerate_identity_closure.py`, `update_evidence_index.py` and `ci/checks/check_mirror_schema.sh` are in `_RELEASE_IMPLEMENTATION_PATHS` (lines 211–242), so the release lane runs. Registered owner tests (`_EVIDENCE_HELPER_TEST_OWNERS`, lines 652–733): builder → `tests/evidence/test_release_attestation.py` + ownership test; closure → `test_release_manifest_content_binding.py`, ownership test, `test_internal_version_manifest_captures.py`, `test_aux_preview_identity_parity.py`; updater → `test_evidence_index_missing_state.py`, ownership test, `tests/config/test_config_artifacts.py`.

## 6. Bounded files and components

Each locus is IP Approved by Plan v1.1 §7 WU-PR-02 "Deliverables", except `ci/checks/check_mirror_schema.sh`, which ID-2 (§4) binds under S22 on canon's direct requirement.

| Path | Bound |
| :- | :- |
| `tools/evidence/build_release_attestation.py` | S06: the wheel stage (`_install_packaged_console_entrypoint`, `_clean_child_env` as needed). Exact-source guarantees stay: `_require_exact_source_copy`, the clean child environment, `--no-index`/`--no-deps`, the fixed-point and output contracts |
| `tools/evidence/regenerate_identity_closure.py` | S13: a root-bound probe (for example a child `sys.executable -I` with the isolated copy as `cwd` and import root). Refusal semantics unchanged: true only for `INCOMPLETE_RELEASE_ROSTER` |
| `tests/evidence/test_release_attestation.py` | S06 and S13 tests |
| `tests/evidence/test_engine_core_evidence.py` | S11: every `release_id` in the payloads equals the admitted identity; a negative case |
| `tools/evidence/update_evidence_index.py` | S22 (IF-5 table; entry builder, reconciler and publisher parameterized by admitted ID) and S12 (IF-7 labels within the allowed key set, ID-1) |
| `tests/evidence/test_evidence_index_missing_state.py` | S22 cases for both CRD IDs, foreign-scope and forgery cases; S12 label cases (or another updater test home PR-20 names) |
| `ci/checks/check_mirror_schema.sh` | S22 / ID-2 only: accept `crd_id`; refuse `epic_id` with `crd_id`; preserve every existing record |
| Governed companions, regenerated by the updater only | `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, their `.path_proof.txt` companions, `audit/gates/topology/orientation_demo.txt` — as S12's relabel requires |
| `docs/ephemeral/` PR result record | evidence obligations (§10) |

Any other file the work needs is a finding: route it under §14 before changing it. In particular `tools/evidence/generate_engine_core_evidence.py`, `tools/qa/qa_harness.py` and `ci/checks/classify_ci_changes.py` are expected to stay unchanged; if one must change (for example an owner registration for a new test file), PR-20 states it in its plan as a finding with its reason.

## 7. Exclusions

- No release member change; no manifest refresh; no admission-constant change.
- No canon edit; no Mirror schema change in canon; no new top-level Mirror key (ID-1).
- No new evidence family, acceptance token or token matrix (Specification Exclusions bullet 3).
- No hand edit of any governed artifact; the updater is the sole Index/Mirror writer. Frozen capture-time families (§5.4) keep their labels and bytes.
- No `crd_id` added to any existing row; no migration of HDE-CRD-0001 rows; no creation of `audit/qa/hde-crd-0002/` or any QA artifact.
- No skipped, disabled, `xfail`-marked or quarantined test.
- No `AGENTS.md`, `README.md` or `docs/EVIDENCE_INDEX.md` edit (WU-DOC-01).
- Nothing from WU-PR-03 to WU-PR-08: no close-run family (WU-PR-07), no re-cut (WU-PR-03/04/05/08).
- No live vendor, production or database call; closed rails throughout.

## 8. Interface contracts with other units

| Contract | Consumer | Binding content |
| :- | :- | :- |
| D-1 Label model before re-cuts | WU-PR-03, WU-PR-04, WU-PR-05, WU-PR-08 | Every row for a §5.4 current-release capture carries the IF-7 label, derived at publication from the admitted manifest, so each later same-version refresh and the `1.4.0` cut relabel rows through the updater alone. The PR-20 plan names the derivation and the family list it uses |
| D-2 CRD admission table | WU-PR-07 (adds the IF-4 close-run family to the same updater); QA-10 | IF-5's explicit table; publication refuses unlisted IDs by name; an absent `audit/qa/hde-crd-0002/` publishes nothing. WU-PR-07 extends this model rather than adding a second admission mechanism |
| D-3 Validator conformance | QA-10 and later QA evidence | `check_mirror_schema.sh` accepts `crd_id` with mutual exclusion; HDE-CRD-0002 rows use the existing CRD row shape |
| D-4 Attestation in the release lane | every later unit | The release lane still builds and verifies the attestation on hosted CI; the closure keeps its test selections (§5.2) |
| D-5 No member change | WU-PR-03 to WU-PR-08 | `catalog/manifest.json` and `release_id` untouched by this unit |

## 9. Disposition rules PR-20 must apply and record

1. **S06 reproduce first.** The plan reproduces §5.1's failure at its own head before choosing a design, and states the environment it will use for the after-change rehearsal (§10). The design choice (for example seeding the isolated build with an upstream build backend captured from the invoking environment while keeping `--no-index`, or building the pure-Python wheel without the patched install-command path) is PR-20's; the acceptance is the Debian-patched build, with exact-source guarantees intact.
2. **S13 stays truthful.** The probe never widens acceptance; an absent ambient package is not a failure; it follows the isolated copy only.
3. **S11 covers every occurrence.** The assertion walks all nested `release_id` values in the payloads that carry them; the purity report's absence of the field is recorded, not "fixed" by a writer change.
4. **S12 encoding (ID-1).** The plan names the encoding inside the allowed key set, the exact family list (from §5.4's sources and the updater's registrations), and a test that a current-release row is distinguishable from a frozen one by Mirror fields alone. Origin `artifact_key` values stay stable.
5. **S22 table (IF-5) and validator (ID-2).** No directory discovery; refusal names the admitted set; existing HDE-CRD-0001 behavior and every Epic input preserved.
6. **Governed regeneration.** Index, Mirror and companions are regenerated only by the updater in the PR, then every read-only validator runs.
7. **Real defects.** A defect that needs a change outside §6 is routed (§14), not absorbed.

## 10. Acceptance, tests and evidence

**Acceptance (Plan v1.1 §7 WU-PR-02, verbatim, with this instruction's binding readings in brackets):**
1. "A recorded reproduction of O-10 on a Debian interpreter fails before the change and the attestation builds and verifies after it; hosted CI's release lane still builds and verifies." [Before: §5.1's receipt at the PR base. After: the full builder exits 0 with the distribution-patched setuptools as the build backend.]
2. "A test proves the closure probe follows the isolated copy with no ambient `engine` importable."
3. "`test_engine_core_evidence.py` fails when the admitted `release_id` is monkeypatched to differ from the payloads."
4. "Every Mirror row for a regenerated current-release capture carries the IF-7 fields; frozen families unchanged; `ci/checks/check_mirror_schema.sh`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh` exit 0." [IF-7 fields = the ID-1 encoding inside the allowed key set.]
5. "Publication through `publish_crd_check_family` succeeds for a fixture `HDE-CRD-0002` root and for `HDE-CRD-0001`, and refuses `HDE-CRD-0003` by name; the absent real root publishes nothing." [Plus ID-2: `check_mirror_schema.sh` accepts a `crd_id` record and refuses an `epic_id`+`crd_id` record, proven by test.]

**Evidence obligations (Plan, verbatim):** "PR result record; the regenerated governed companions in the PR; no new evidence family." The record names every check actually run with counts, the before/after O-10 reproduction with its environment, and the S12 family list and encoding.

| Requirement | Acceptance | Proof | Stage |
| :- | :- | :- | :- |
| S06 | (1) | before/after builder receipts; release-lane attestation on hosted CI | PR-30 local; PR-35 CI |
| S13 | (2) | test with no ambient `engine` and with a different ambient package | PR-30; CI release lane |
| S11 | (3) | positive and monkeypatched negative case | PR-30; CI evidence lane |
| S12 | (4) | label test; regenerated Index/Mirror; read-only validators | PR-30; CI evidence and release lanes |
| S22 | (5) | publication cases; validator cases | PR-30; CI evidence and release lanes |

**Validation shape.** Python 3.12 with CI's install; `AGENTS.md` pytest readiness (`python -m pip install -r requirements-dev.txt`, then `python -m pytest --version`); closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, vendor, geocode and database keys unset); every test run that can write tracked artifacts in a detached worktree or throwaway copy with `git diff --exit-code` and an empty status afterwards (expect OBS-4's 11 same-byte rewrites only); `ci/checks/check_env_pins.sh` and `python3 ci/checks/check_agents_md_citations.py` stay green; the attestation built into an external empty directory with `--require-clean`.

**Nonclaims (Plan):** "No QA evidence is produced for HDE-CRD-0002; admission readiness only." CI green is not QA; no PF09 mapping.

## 11. Migration and security constraints

- **Migration:** none. No data, schema, catalog or member change. Rollback is Nathan's revert of the squash commit, followed by the updater regenerating Index/Mirror from the reverted model; no manifest refresh.
- **Security:** the attestation keeps its exact-source binding, clean child environment, `--no-index` and `--require-clean` refusal; any build backend seeded into the isolated build comes only from the invoking environment, never the network; the closure probe never runs ambient code to decide admission; the Mirror validator only widens to the canon-allowed `crd_id` and adds the mutual-exclusion refusal; no secret, token or key value in tests, logs or records.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session): reads this instruction and its lineage, the §5 and §6 repository files and canon on `main`; writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/` (design per §9, requirement-to-change/test map, ordered steps, risks, recovery); returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan): recovers existing work first; implements only the authorized scope; tests locally under §10; one coherent commit; publishes `PR_CANDIDATE_PUBLISHED`; hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session): retrieves and resolves the Codex code review findings (PF10 addendum 2.3: the Codex security review is not part of the chain), retests, pushes coherent corrections, uses CI economically, verifies current-head CI and mergeability, and returns `MERGE_PENDING` without merging.
- **PR description:** `.github/pull_request_template.md` headings with the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage and, on ACCEPT, issues the next unit's instruction (WU-PR-03).
- **Attributable lineage:** the PR result records, the PR reference and the squash commit.

## 13. Recovery

- Interruption: resume in the same dedicated phase session from its last saved artifact; inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- An ordinary defect in this instruction returns to this IA through PR-10; a corrected instruction is a new version, never an edit of v1.0.
- Abort is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent, a protected architecture, security, data-model or external-contract boundary, several units' scope, an accepted dependency, or budget, schedule or risk needing Product Owner direction.
- Before Proceed, the PR-20 author owns any rescope proposal (RS-10, optional support; RS-30 for revisions) and this IA reviews it through RS-20; the decision returns to the PR-20 planning context. After Proceed, PR-30 or PR-35 records `PR_RETURN_PHASE`. `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- Expected triggers: S12's invariant not achievable inside the allowed key set (ID-1); an S06 design that needs network access, a non-test change outside §6 or a weaker exact-source guarantee; a change to `generate_engine_core_evidence.py`, `qa_harness.py` or the classifier beyond an owner registration.

## 15. Unresolved items, carried observations and owners

| Item | Owner | Deadline |
| :- | :- | :- |
| S06 design and the post-fix rehearsal environment (§5.1, §9.1) | PR-20 session | In the plan |
| S12 encoding and exact family list (ID-1, §9.4) | PR-20 session | In the plan |
| Whether new tests need classifier owner registrations | PR-20 session | In the plan (as a stated finding if a classifier change is needed) |
| OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` (qa lane); a proposed test-side patch is in #627's conversation | QA tool and test owner, through the IA; Product Owner to route | Not this unit's scope; a qa-lane failure of that test on this PR is recorded as OBS-17, never "fixed" here |
| O-6: hosted `ruby` version unprinted | IA | Not applicable unless this PR selects the contract-inventory file |
| OBS-4: 11 tracked files rewritten with identical bytes by the changed-test step | IA | Expected; any other rewrite is a finding |
| WU-PR-03 baseline currency of the contract-inventory generator; WU-PR-06 sweep `ruby` (PF10 addendum 2.2 "Downstream work") | IA | WU-PR-03 and WU-PR-06 instructions |
| AQ-1 (S21 ADR) | Nathan / Product Owner | Before WU-PR-07 merges; does not gate this unit |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged:
- **CR-1, CR-2, CR-3** (CANON_RECONCILIATION) — APPROVED_AS_CHANGED (Thoth; instruction WU-PR-01 v1.0 §16). Not touched by this unit.
- **CR-4** — APPROVED (Product Owner; `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2). WU-PR-01 only.
- **CR-5** — APPROVED_AS_CHANGED (Product Owner; same record §3): the Product Owner assigns the vehicle for any canon replacement case by case. No canon replacement is planned in this unit.

No new conflict: ID-1 and ID-2 apply HDE Schemas & Artifacts §8.3 and §8.17 as written, within the Plan's own wording (IF-7's "equivalent `release_binding`"; S22's purpose), and change no canon.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Owner | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S06 "builds under Debian-patched setuptools" | the builder completes when the build backend is the distribution-patched setuptools | §5.1 reproduction before; full builder exit 0 after; release lane on CI | WU-PR-02 | (1) | PR-30; PR-35 CI |
| S11 "fails when `release_id` drifts" | currency test binds admitted identity | every nested occurrence equals `identity_meta()["release_id"]`; monkeypatched negative | WU-PR-02 | (3) | PR-30; CI |
| S12 "carry current-release labels" | a reader can tell current from frozen without opening the file | ID-1 encoding inside PF12 §8.3's allowed keys; frozen families unchanged | WU-PR-02 | (4) | PR-30; CI |
| S13 "depends only on the isolated closure's own sources" | probe bound to the copy | root-bound child probe; refusal semantics unchanged | WU-PR-02 | (2) | PR-30; CI release lane |
| S22 intent | updater publishes and validates HDE-CRD-0002 QA rows before QA; Epic and HDE-CRD-0001 preserved | IF-5 table; ID-2 validator conformance; existing row shape | WU-PR-02 | (5) | PR-30; CI |
| Plan "lands before WU-PR-07 … and before any member-changing unit's convergence relabels rows" | label model and admission model precede re-cuts and the close-run family | D-1, D-2 | WU-PR-02 → WU-PR-03/04/05/07/08 | (4), (5) | PR-40 |
| Specification Exclusions bullet 3 "No new evidence family" | labels and admission are not a family | §7 | WU-PR-02 | (4), (5) | PR-30 |
| Plan nonclaim "admission readiness only" | no QA evidence | §7, §10 | WU-PR-02 | — | PR-30 |

Checks against the full PR-20 contract: its sole substantive input is `PR_INSTRUCTION_ID`; this instruction carries the Specification, Audit, Plan and review lineage, the PF10 path and overlay set, the baseline, loci, exclusions, interfaces, dependencies, acceptance, evidence, migration, security, recovery, rescope, merge ownership and the return owner. No decisive comparison fails. The numeric facts in §5 were measured at `cc3dc33` by this IA (commands in §5.1 and below), not carried unverified.

## 18. Return owner and next step

- **INSTRUCTION_READY → PR-20 — Create Detailed PR Implementation Plan — 100926.1** (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba), in the dedicated WU-PR-02 PR engineering session (`session_disposition: INITIAL_DEDICATED_ASSIGNMENT`; `role_session_ref: NOT_YET_ASSIGNED`, assigned by Nathan at launch). Sole substantive input: this instruction's repository path.
- **Return to the IA:** PR-40 lineage review after Nathan's merge; rescope review through RS-20; same-owner correction of this instruction through PR-10.
- **Prerequisite:** the pull request carrying this instruction is merged to `main` before PR-20 runs.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-02)

Action sent (v6): "Write, in a new dedicated session, the detailed PR implementation plan for one work unit of an approved change: repair four release-evidence tools and one test (make the release attestation builder's wheel stage work when the interpreter uses a distribution-patched setuptools, reproduced and failing today; make an isolated closure admission probe independent of the ambient installed package; make an evidence currency test assert release identity; label current-release captures in the machine evidence mirror within a closed canonical key set; extend the canonical evidence-index updater's change admission to a second change ID and its mirror validator to accept the change-identity key), across about five files of a 5,000-line updater and an 870-line builder, with governed evidence regenerated only by its owner tool. Planning only, with a reproduction in a throwaway copy; no live vendor or production run; a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.30 (confidence 0.77); rung probabilities low 0.00, medium 0.02, high 0.67, extra high 0.30, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.20, Opus 5.5 0.80 (confidence 0.60). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.54, Opus 5.5 at extra high 0.24, Opus 5.5 at max 0.01, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.13, Fable 5.1 at extra high 0.06, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T15:52:04Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T15:52:04Z; HTTP 200 in 0.61 s; 4301 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: none.
- **Notion row:** not written, as PR-10 directs.
- **Nathan's pick for PR-20:** not stated. **For this PR-10 session:** not stated (the reading for PR-10 is in lineage review v2.0 §11).

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. The cloud container reproduces O-10: its `/usr/bin/python3` (3.13.16) imports Ubuntu's patched setuptools 68.1.2 from `/usr/lib/python3/dist-packages`, and a Python 3.12 venv with CI's install builds the attestation (§5.1). It needs no live vendor, production or database access and writes only its plan under `docs/ephemeral/`. This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-10 / instruction 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a |
| role/stage | whole-change IA / PR-10 |
| capture time | 2026-10-13T15:52:05Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating) |

## Canon relied on

Read on `main` at `cc3dc33`. Each decision topic maps to its sections:
- **Instruction authority, content and readiness:** PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (the IA's decomposition; Product Owner Proceed per PR) and §9.1.2 (canon precedence: PF-Canon governs an in-flight document where they conflict; ID-1 and ID-2 rest on it); PF27-Canon-Plan-Templates v2.0.5 "Repository loci and file minting" (concrete loci; facts prove planning-time reality), "Source-bound review authority and exact-fix limits", "CI lane classification and automated budget-control discipline" (lanes in §5.6).
- **S12 (ID-1):** PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.3 "Machine Evidence Index — JSONL mirror (records-only)": "Single home and path", "Format (canonical JSONL)", "Minimum record schema (reject unknown keys)", "Bundle-aware extension … Allowed top-level keys and unknown-key rejection" (read in full, lines 2232–2335).
- **S22 (IF-5, ID-2):** PF12 §8.3 (the `crd_id` acceptance and mutual-exclusion duty) and §8.17 "Live QA evidence layout", "Change-container identity (normative)" (read in full to "Path provenance").
- **Review chain:** PF10-HDE-Build-Notes v13.5.5 addendum 2.3 (Rules 2 and 3). **PF10:** v13.5.5 read in full (as `pf10_ref` states); addendum 2.1 governs §19; addenda 2.2 and 2.4 are WU-PR-01 records whose downstream items are carried in §15; PF10 is otherwise silent on this unit's subject matter.
- **Change process:** PF06-Canon-Change-Process-Guide v2.5.4 §0.2 (PR route; Product Owner squash; no canon edit in implementation PR work) and §1.0.4 (phase separation).
- **Operative documentation:** `AGENTS.md` (canon-first rule; sole Index/Mirror writer; governed evidence never hand-edited; release identity; closed rails; pytest readiness; PR descriptions).

**In-flight documents read:** Specification v1.1 (Requirements rows S06, S11, S12, S13, S22; Exclusions); Plan v1.1 §5 (IF-5, IF-7), §7 (WU-PR-02, the common paragraph, the order), §10, §13; Plan review v1.1; Audit v1.0 §5.6, §6 S06, S11, S12, S13, S22, §7.1 (EC-5); WU-PR-01 instruction v1.0 (format and carried register); WU-PR-01 lineage reviews v1.0 and v2.0; the CR-4/CR-5 disposition; `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §6.3 and §6.4; `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` §7.4 row and O-10.
