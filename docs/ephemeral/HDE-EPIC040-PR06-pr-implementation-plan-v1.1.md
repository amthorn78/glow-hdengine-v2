---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC040-PR06-PR-IMPLEMENTATION-PLAN
artifact_version: "1.1"
artifact_state: AWAITING_PO_PROCEED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06
pr_instruction_id: HDE-EPIC040-PR06-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
planning_inspection_capture_utc: 2026-09-25T08:53:00Z to 2026-09-25T10:08:45Z (v1.0); 2026-09-25T14:05:00Z to 2026-09-25T14:20:13Z (v1.1)
next_stage: PR-30 (Product Owner Proceed required first)
---

# HDE-EPIC040-PR06 — PR Implementation Plan v1.1

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR06-PR-IMPLEMENTATION-PLAN` |
| version | `v1.1` — complete successor of v1.0 (`docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.0.md`, SHA-256 `583de879f619ccdb5f32e20d5447b69c1509f447d6fb4227dcb963caaaf2e7b7`, `BLOCKED`), issued as the review §7 asked; v1.0 is preserved unchanged |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the applicable PF10 overlays (§2.3), now including the approved `HDE-EPIC040-PR06-F01` delta (PF10 §2.21) planned in §5.11; no open boundary finding (§14); pending Nathan / Product Owner's exact PR-30 invocation against this version |
| finding_ref | `HDE-EPIC040-PR06-F01` — decided: `HDE-EPIC040-PR06-F01-RESCOPE-REVIEW` v1.0 `APPROVE` alternative A, drained as PF10 §2.21 (§14.1); no other finding raised |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.1.md` |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR06` — Complete release admission and evidence convergence |
| PR_INSTRUCTION_ID | `HDE-EPIC040-PR06-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR06-pr-instruction-v1.0.md`, SHA-256 `20517abce769c3d241f944f8bde252434c4c59c4dade2c246c68224af469a684` (landed on `main` by #497 at `190527cf105eadca355a949697b308d084ae70e4`; byte-identical to the handoff's stated digest, verified by reading the whole file) |
| IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1, immutable approved base, `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| SPECIFICATION_ID | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| IMPLEMENTATION_AUDIT_ID | `HDE-EPIC040-IMPLEMENTATION-AUDIT` v2.0, `AUDIT_COMPLETE`, `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` |
| PLAN_REVIEW_ID (original, preserved) | `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| Applicable overlay reviews | `HDE-EPIC040-PR04-F01-RESCOPE-REVIEW` v2.0 (RS-20 `RESCOPE_REVIEW`, `APPROVE`) with its one addendum, drained as PF10 §2.15; PR03-R02 as PF10 §2.12; `HDE-EPIC040-PR06-F01-RESCOPE-REVIEW` v1.0 (`RESCOPE_REVIEW`, `APPROVE`, alternative A, decided by the retained whole-change IA by Product Owner direction) with its one addendum `HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md`, drained as PF10 §2.21. No `REMEDIATION_REVIEW` applies |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR06 |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` for the v1.0 PR-20 run; `RETAIN_EXISTING` for this v1.1 re-entry (the review returned the decision to the finding's author); PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `NOT_YET_ASSIGNED` — the handoff named the operator as assignment owner at launch and the launch message assigned none; no platform ID is invented. Known runtime identity from the harness: `https://claude.ai/code/session_01S3w2LDoDhi5GKMfuLRKkdx` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR06` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| Authority boundary | This plan authorizes nothing. Implementation waits for the Product Owner's PR-30 Proceed for this exact version; merge is Nathan's alone; QA, Ops, acceptance, release activation, deployment, PF-Canon edits, PF09 movement and Epic closure are outside it (instruction §§4, 9, 10) |

## 2. Exact controlling lineage and source record

### 2.1 Approved and accepted change lineage

| Role | Artifact | Identity used here |
| --- | --- | --- |
| Approved bases | Specification v1.1; Implementation Audit v2.0; immutable Plan v2.1 (header `PLAN_PENDING_REVISED` is its authoring state; approval is the review); Plan Review v2.1 Isis-50 `APPROVE` | read completely; §§5.10, 6.6, 7.1–7.4, 8, 11 of the Plan govern this unit |
| Accepted predecessors | PR01 v1.1, PR02 v1.0, PR03 v1.0, PR04 v1.0, PR05 v1.0 lineage reviews under `docs/ephemeral/` | all `ACCEPTED_FINAL`; the PR05 review (SHA-256 `7265e9cf3035acea3aa190d478ebf50df7525acaf8f828837751a106f792b023`) names PR06 next and carries O-17/CR-06 |
| This unit's instruction | `HDE-EPIC040-PR06-pr-instruction-v1.0.md`, `INSTRUCTION_READY` | sole substantive input of v1.0; §§3–13 mapped into §§3–14 below |
| F01 decision (new in v1.1) | `HDE-EPIC040-PR06-F01-rescope-review-v1.0.md` (SHA-256 `7264ed3f661de42f9c2ad40449d77e8d2a31a2edc2775a10c915074d1b246d05`) and `HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md` (SHA-256 `c5154465a1bdebda8f217ca7d320c0ec75bc74b37521931cbca4417d1b0d2b03`), landed by #499 | `APPROVE`, alternative A, binding conditions §4; the one overlay; both read completely; drained as PF10 §2.21 |
| Predecessor plan | `HDE-EPIC040-PR06-pr-implementation-plan-v1.0.md` (SHA-256 `583de879…e7b7`), landed by #498 | `BLOCKED`; its §§5–13 stand as complete planning work (review §5) and are carried here with the v1.1 changes marked |
| Format precedent | `HDE-EPIC040-PR05-pr-implementation-plan-v1.0.md` | structure only; no content inherited |

**What changed from v1.0 (complete list).** Front matter and §1 (state, version, finding); §2.1, §2.3, §2.4 (F01 lineage, PF10 v13.3.2 §2.21, second PR-20 use); §3.1 (baseline re-verified at `bce4c269…`); §3.3 and §10.6 (alt. A rehearsal rows); §4.2 CC-6 (no longer blocked); §5.11 (new: the approved gate change); §6.1 (gate as overlay locus); §7 (row for §2.21); §8.7 (new: overlay tests); §9 C0 and C3 (F01 decided; gate change ordered before convergence); §11.1 (review items for the conditions); §12 (R-10 replaced, R-14 added); §13.2 (O-P06-13, O-P06-14); §14 (finding resolved; D-11 updated; D-12, D-13 added); §16 (second use entry); §17 (PR-30 package is the native next step; the RS-10 package is closed). Everything else is carried verbatim from v1.0.

Accepted-final PR01–PR05 are not reopened, rerun, revised or reaccepted by this plan.

### 2.2 Controlled subject-matter sources used

All read from `docs/pfcanon/` as unique controlled Markdown; cited by title and section only.

| Source | Sections used | What they settle for PR06 |
| --- | --- | --- |
| PF12 — Canon HDE Schemas and Artifacts v2.9.5 (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`) | §4.1 canonical JSON rules; §5.1 manifest file shape, "Magic-10 v1 promoted release inputs", "Manifest and member form"; §5.2 hash input; §5.3 validation; §6.1 manifest construction; §6.2 `release_id`, §6.2.1 external release attestation; §6.3 change ⇒ new `release_id`; §6.4 evidence and CI hooks; §8.14–8.15 config artifacts and bundles | one row per promoted path, ASCII order, refreshed or added, no self-listing; version `1.1.0` and `built_at_utc 2026-08-24T18:04:49Z`; the cutter recalculates every listed member; format validation precedes hashing and never manufactures hash input different from the bytes on disk; `release_id = sha256(canonical bytes of catalog/manifest.json)`; `hde.release_attestation.v1` and `PR06R_B_FINAL_PASS` unchanged |
| PF01 — Canon HDE Math Spec v1.3.7 (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`) | §5.4 manifests and freeze-pack coupling (§§5.4.3–5.4.6); §9.5 parity and two-run identity; §9.6 pack closure and release identity | golden collection semantics, change ⇒ new `release_id`, closure of the pack |
| PF10 — HDE Build Notes v13.3.2 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.3.2.md`) | front matter §§1–9 (precedence, current-version rule); §§2.2–2.5 (C040 decisions); §§2.6–2.11, 2.13, 2.19, 2.20 (accepted predecessors); §2.12 (admission owner); §2.15 (F01 interval); §§2.16–2.18 (F03/F05/F07 deferrals); §2.21 (PR06-F01 frozen-capture identity source) | §2.12 is exercised unchanged; §2.15's acceptance self-extinguishes on admission and owes no removal; F03/F05/F07 stay with PR07; §2.21 extends PR06's loci by exactly the gate and its test home under the review's conditions |
| PF02, PF05, PF14 §6.7 (C040-05), PF09.3, PF03 | consulted for boundaries only | no PR06 decision rests on them beyond the carried register |
| `AGENTS.md` (repository instructions, read completely) | evidence discipline; sole updater; canonical JSON gate boundary (26 targets, six set rules); release identity section; direct-only DB posture; QA output placement; PR description contract | every rule applies to PR06's evidence work |

Where PF10 addresses a point expressly it takes precedence; no conflict between PF10 and PF12/PF01 was found for PR06's points.

### 2.3 Current controlled PF10 and every applicable active addendum

- Current controlled PF10: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.2.md` (2,273 lines, SHA-256 `35fab8e9a8af9cb17b41298551ae48c3259f678a9bb0d57a86f37d996a03f5ce`), re-resolved by this session at v1.1 time (v1.0 was planned against v13.3.1, SHA-256 `66305b8f…9c14`, which v13.3.2 supersedes by adding §2.21 and its index line; the diff is exactly that). `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md` and `…-v13.3.1.md` are still present beside it (O-P06-14, Nathan's, non-gating); under PF10 §6 the latest active base version, v13.3.2, is current and the older ones are not read.
- Applicable active addenda, all in that one file: §2.2, §2.3, §2.4, §2.5, §2.6, §2.7, §2.8, §2.9, §2.10, §2.11, §2.12, §2.13, §2.14, §2.15, §2.16, §2.17, §2.18, §2.19, §2.20, §2.21. Their source records under `docs/ephemeral/` (for example `HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`, `HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md`) are lineage, not additional authority.
- No PF10 edit is planned or authorized; this plan emits no addendum (PR-20 is not a qualifying approval prompt).

### 2.4 GCFPE execution sources

- Prompt executed: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, read completely at the v1.0 run and re-entered for v1.1 (Notion read only; no Notion write). RS-10 — Create Bounded Work-Unit Rescope Proposal — 091426.1 was read at v1.0 time for the handoff; the review §1 records that no RS-10 session was created.
- Release: GCFPE-20260914.1 / 091426.1 / 55 members. Carried uses: `GCFPE-USE-HDE-EPIC040-PR-10-20260925-PR06-01` (instruction §13), `GCFPE-USE-HDE-EPIC040-PR-20-20260925-PR06-01` (plan v1.0 §16), `GCFPE-USE-HDE-EPIC040-RS-20-20260925-PR06-F01-01` (review §8).
- Provenance persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent from the repository; persistence stays `PENDING / NON_GATING` (§16).

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline re-verified at planning time

| Item | Verified value |
| --- | --- |
| Repository / default branch | `amthorn78/glow-hdengine-v2` / `main` |
| `origin/main` at planning time | v1.0: `190527cf105eadca355a949697b308d084ae70e4` (tree `c1b19d23691e75bcd5699220134a6d8b95294e3f`). v1.1: `bce4c269989257f3a8d977da2a4a75fdbd2e8a61`, title `docs: Update PF10 HDE Build Notes to v13.3.2 (#500)`, fetched at re-entry; the three later commits (#498 plan v1.0, #499 F01 review and addendum, #500 PF10 v13.3.2) are all under `docs/` |
| Since the PR05 landing `4d7ab9d0fba64dd9c275ad3a25e4bf3c6ac46dae` | `git diff --stat 4d7ab9d…bce4c26 -- . ':(exclude)docs/'` is empty: every later change is under `docs/` (#495–#500). The non-docs tree PR-30 starts from is therefore the one every fact in §3.2 and every rehearsal in §3.3 was established on |
| Planning session tree | clean at both runs; no repository file outside `docs/ephemeral/` was written by either planning operation. All inspection with side effects ran in scratch clones under the session scratchpad (§3.3). The designated working branch was restarted from `bce4c269…` for v1.1 because its v1.0 pull request had merged |
| Local interpreter | Python 3.11.15 with `requirements.txt`, `requirements-dev.txt` (pytest 8.4.2) and `pip install -e .`; CI uses Python 3.12 — a difference recorded as an inference limit, not a finding |

### 3.2 Verified baseline facts that shape this plan

Each row was established by reading the named source completely or by executing the named read-only command on the baseline tree.

| # | Fact | Source |
| --- | --- | --- |
| F-01 | `catalog/manifest.json`: 15 members, `version 1.0.0`, `built_at_utc 2025-12-26T00:00:00Z`, 1,981 bytes, SHA-256 `a5f06ae3fcc964c41bb80c3630f455d9c246d9f87fcad500a5b74bf79b96bc01`; every existing row matches disk (`scripts/release_id_recompute.py --check-manifest-only` exit 0; cutter `--check` exit 0) | file read; commands |
| F-02 | `ADMITTED_RELEASE_ROSTER` has 44 sorted paths; `ADMITTED_RELEASE_VERSION == "1.1.0"`; `ADMITTED_RELEASE_BUILT_AT_UTC == "2026-08-24T18:04:49Z"` (`engine/config/registry_loader.py`). 29 roster paths are absent from the manifest; all 44 exist on disk; the roster includes `engine/categories/registry.py`, `engine/stable/sercanon.py` and `schemas/gates_v1.schema.json` beyond Plan §5.10's 15 + 31 list (instruction §3 makes the roster authoritative) | file read |
| F-03 | The admission owner's member-format rule (`_parse_release_member_bytes`: `.json` must equal its canonical serialization; `.py`/`.sql` must be UTF-8, non-empty, single final LF, `.py` must parse) refuses exactly three roster members on the baseline tree, all `NONCANONICAL_JSON`: `adapter/schemas/error_v1.schema.json` (426 B, SHA-256 `b83a963a…9fa3`; canonical form 345 B, `a3c333c6…c930`), `errors/token_map/token_map.json` (3,919 B, `f536744a…ca61`; canonical 2,982 B, `a218f515…701a`), `schemas/reader.v1.schema.json` (2,156 B, `bd00c334…fff1`; canonical 1,563 B, `ecfc2054…7550`). Parsed content is identical in each case (`json.loads` equality). The synthetic fixture (`tests/config/helpers.py`, `_SYNTHETIC_FUTURE_CANONICAL_JSON`) canonicalizes exactly these three, which is why the fixture admits while the real root cannot | command over all 44 members |
| F-04 | `errors/token_map/token_map.json` is produced by `tools/errors/generate_error_artifacts.py::_write_json` as `json.dumps(indent=2, sort_keys=True) + "\n"` (non-canonical by construction); `tests/cli/test_errors_parity.py::test_token_map_snapshot_matches_canonical` compares parsed content, not bytes. `schemas/reader.v1.schema.json.sha256` is a `sha256sum`-format sidecar of the schema bytes with no generator (only copied by `scripts/make_cli_smoke_audit.sh`); it currently matches the schema. The three files have no path proofs except the token map (`errors/token_map/token_map.json.path_proof.txt`, Index/Mirror row `ERROR_TOKEN_MAP_V1`) | file reads |
| F-05 | `scripts/cut_release_manifest.py::cut_manifest(manifest_path, *, version, built_at_utc, check=False, _publish=None)` validates the manifest's own shape and canonicality, validates every existing row's path safety, refreshes each row's hash and size from disk, sorts, and renders canonical bytes. It constructs no membership (the cutter gap the instruction verifies) and validates no member format | file read |
| F-06 | `tools/evidence/run_canonical_json_gate.py` pins `_EXPECTED_RELEASE_MANIFEST_PATHS` to the 15 current members; `_validate_release_manifest_snapshot` copies each listed member into a temporary root, requires the path tuple to equal that constant, and runs `cut_manifest(check=True)` there. With a 44-member manifest the gate fails `release_manifest_input_roster_invalid` (rehearsed, §3.3). The 26-path `EXPECTED_TARGET_PATHS` and six `EXPECTED_SET_RULES` are separate constants and are not touched by this plan | file read; rehearsal |
| F-07 | `tools/config/generate_config_artifacts.py --publish-family` runs, in order: cutter `--check` (re-cut with the existing version and timestamp on drift), `check_manifest_only`, the three primaries, catalog logs, bundles, the arrays report, the canonical JSON gate in write mode (`CONFIG_CANONICAL_GATE_FAILED` on non-zero), then `update_evidence_index.publish_config_family`, whose `_config_logical_delta` guard refuses `CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT:<identity>` when any Index/Mirror record outside `CONFIG_PRIMARY_PATHS` and `_CONFIG_SKELETON_PATHS` would change. Publication therefore requires every non-config record to be already current in the Mirror (rehearsed: it failed on a stale gate-log row and succeeded after a full updater run) | file read; rehearsal |
| F-08 | The sanity pipeline's stage 11 is `update_evidence_index.py --check` only. On a canonical run with no earlier failure, the pipeline writes the prospective PASS log before stage 11 and, on success, re-renders byte-identical PASS bytes; on failure it writes `summary:FAIL` and calls the updater's `--rebind-sanity-log` (FAIL model only). `run_sanity_pipeline_gate.py` accepts exactly two log models (PASS, exit 0; NOT_ADMITTED, exit 3) after a silent fresh run. Consequence: a transition into the PASS model requires the Mirror to bind the PASS-model bytes before the canonical run, and only the sole updater can bind them (§5.7, rehearsed) | file reads; rehearsal |
| F-09 | `tools/evidence/regenerate_identity_closure.py` runs each of its 18 `CLOSURE_STEPS` as "check first; write only when the check fails; check again"; `_check_closure` also runs `generate_open_rails_abba_proof.py --live --check` and pytest on `tests/evidence/test_aux_preview_identity_parity.py` and `tests/evidence/test_release_manifest_content_binding.py`. The showcompat and CLI-conformance steps validate frozen digests, so their write mode is never reached while the frozen captures are intact | file read; rehearsal |
| F-10 | After admission the two capture generators' write modes refuse on the real root without writing (showcompat: identity-metadata mismatch, PR04 O-20; CLI conformance: birth-only inputs, O-21) while `--check` passes on the frozen digests (rehearsed: write exit 1, check exit 0, no file changed) | rehearsal |
| F-11 | `tools/evidence/build_release_attestation.py` copies tracked files only, installs the packaged console entrypoint (wheel via `pip wheel --no-build-isolation`, venv, `pip install --no-index`), snapshots every file except `.git` and caches, runs `closure_write_and_check`, `closure_fixed_point_check` and `release_sanity`, and refuses `isolated_write_outside_evidence_roots` when any changed or new path is not in `ATTESTATION_GENERATED_OUTPUTS`. `_FORBIDDEN_TRACKED_ROOTS` is `.tox`, `.venv`, `node_modules`, `venv` | file read |
| F-12 | Narrative pack mount (PR04 O-18): `engine/narratives/state.py::get_pack()` calls `load_pack()` whose default `mount_root` is CWD-relative `narratives/`; `_copy_files_atomic` writes `narratives/<pack_sha>/` (10 files: five pack JSON files and their `.sha256` sidecars, 86,626 bytes) unless a byte-exact mount already exists, in which case it verifies and writes nothing. The current pack SHA is `4cc79e0535d93acece861fff5e725a26b62ab22ee2c03c9bae2632a5570953a0`. The repository tracks a stale mount `narratives/64e17c9c4d608f4feceedc16e43bff44e7a34208b2f32ebe49c81a8ee6ddc462/` (9 of its 10 files differ from the current pack; added with the loader in `1180d94`) that the loader never reads. Every live evaluation after admission therefore creates untracked `narratives/4cc79e05…/` residue (rehearsed), which fails CI's clean-tree assertions, `tests/evidence/test_rails_ci_workflow_integration.py::test_open_rails_producer_check_mode_has_no_repo_residue`, and the attestation write boundary | file reads; `git ls-files`; rehearsal |
| F-13 | `ci/checks/classify_ci_changes.py` returns no lanes (fail-closed `CI_CHANGE_SURFACE_UNCLASSIFIED`) for `errors/token_map/token_map.json`, `tools/errors/generate_error_artifacts.py` and any `narratives/…` path; a change to the classifier itself selects full validation (all seven lanes plus `_FULL_VALIDATION_SUPPLEMENTAL_TESTS`) | `classify_paths` executed in-process |
| F-14 | The golden comparator (`tools/config/artifacts.py::compare_goldens`) admits the candidate root through `_load_active_mechanics_bundle_from_root` and then runs the cases through the executing installation's modules: kernel cases import `engine.core.core`, `engine.magic10.*`, `engine.bodygraph.gates`; application cases (`M10-G005/G007/G008`) also import `engine.bodygraph.resolver`, `engine.compat.compute`, `engine.compat.error_tokens` and `engine.narratives.constants`. §2.12's executable-equivalence owner covers exactly eight modules (`engine/config/registry_loader.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py`, `engine/categories/registry.py`, `engine/core/core.py`, `engine/magic10/composite.py`, `engine/magic10/signals.py`, `engine/magic10/calculators.py`); `engine/bodygraph/gates.py`, `engine/bodygraph/resolver.py`, `engine/compat/compute.py`, `engine/compat/error_tokens.py` are roster members executed by the goldens without any binding (O-17/CR-06) | file reads |
| F-15 | 22 tests in 13 files assert the F01 interval state on the real root and fail once the real root admits (full inventory in §8.6; established by running every CI lane's pytest set and the supplemental roster against the rehearsed admitted tree) | rehearsal |
| F-16 | `.github/workflows/ci.yml` and `ci/jobs/rails_open_conformance.yml` accept the `RELEASE_NOT_ADMITTED` outcome only when the probe observes `INCOMPLETE_RELEASE_ROSTER`; after admission those branches are never taken (PF10 §2.15 binding condition 3: no removal owed, none planned) | file reads |
| F-17 | `tools/evidence/generate_identity_provenance.py --check` and `generate_release_bindings.py --check` compare against the current expected `release_id`; `scripts/release_id_recompute.py` writes only under `HDE_ISOLATED_RELEASE_BUILD=1`. In-tree `artifacts/math/*`, `artifacts/identity/*`, `artifacts/bodygraph/release_bindings.json` are frozen capture-time records that only the isolated closure regenerates (`AGENTS.md`, Release identity) | file reads |

### 3.3 Planning rehearsal in scratch clones (inference support, not PR evidence)

To plan from execution rather than reading alone, this session rehearsed the unit in throwaway clones of `190527cf…` under the session scratchpad (`probe`, `probe2`), never in the repository checkout. What the rehearsal established is recorded here as **inference support**; it is not implementation, not QA, not CI, and none of its bytes enter the PR. Every step below is re-executed by PR-30 on the real branch (§§9–10).

| Step rehearsed | Outcome |
| --- | --- |
| Canonicalize the three F-03 members, cut the 44-member manifest with `cut_manifest(version="1.1.0", built_at_utc="2026-08-24T18:04:49Z")` after constructing the rows | manifest 5,752 bytes; `load_active_mechanics_bundle()` admits the real root with `release_id 988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e` (identical to the synthetic fixture's identity, as expected once the member bytes agree); `engine.runtime.identity` reports the same value; `check_manifest_only` and cutter `--check` exit 0 |
| `generate_config_artifacts.py --compare-goldens .` | exit 0; all eight goldens `match`; `ok: true` |
| Canonical JSON gate | fails `release_manifest_input_roster_invalid` until `_EXPECTED_RELEASE_MANIFEST_PATHS` is rebound to the roster; then write and `--check-only` exit 0; the 26 targets unchanged |
| `--publish-family` | `CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT` when the gate-log row was stale in the Mirror; exit 0 after a full updater run first (F-07) |
| Determinism proofs, open-rails fixture proof, A7 transport proofs (write) | all regenerate through their owners; `--check` modes pass |
| Sanity pipeline | stages 01–10 pass once the interval tests are out of the way (rehearsed by deselecting them in the clone only); stage 11 fails until the Mirror binds the PASS model; with the PASS model bound by the sole updater the canonical run ends `summary:PASS` (exit 0), a second run and `run_sanity_pipeline_gate.py` exit 0, and `update_evidence_index.py --check` exits 0 — a fixed point (F-08) |
| Narrative mount | every live evaluation created untracked `narratives/4cc79e05…/`; with that loader-produced mount tracked and the stale mount removed, no residue remains (F-12) |
| Capture generators | write modes refuse (F-10); frozen digests validate |
| CI lanes and supplemental roster (pytest) | all pass except the 22 interval-pinned tests of §8.6 |
| External attestation build (v1.0) | see §10.6 attempts 1–4 for the recorded outcome and its environment caveats (Debian's system `setuptools` breaks `pip wheel --no-build-isolation` with `AttributeError: install_layout` until a current `setuptools` is installed; scripts executed inside the isolated copy import `engine` from the installed location, so the local rehearsal needs the editable install to point at the tree being attested) |
| Approved alternative A (v1.1) | in a clone at the PASS fixed point the gate was changed exactly as §5.11 specifies (four digest-verified sources; `summary.json` a consumer). `run_canonical_json_gate.py --check-only` exit 0; with `service_identity.json` rewritten to a different `release_id` the five identity-carrying targets still validate; `build_release_attestation.py --output <external empty dir> --require-clean` exit 0 and `--verify` exit 0 (`validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, `release_id 988ed2a7…`, 174 evidence files bound, 14 recorded under `omitted_files` by the builder's existing secret-safety rule, §10.6 attempt 5); the tree stayed clean. A step-wise emulation of the isolated closure in a further clone: closure write exit 0 (22 files regenerated in the copy), closure fixed-point check exit 0, release-sanity gate exit 0 with `summary:PASS`. Caveat: the clone carried the probe-only deselection of the 22 interval tests; on the real branch their §8.6 rewrites must pass instead. The gate's existing tests there: 84 passed, 3 failed — the roster-copy test (§8.4) and the two conjunction on-disk forgery tests whose first refusal token moves (§8.7) |

## 4. Exact objective, completion conditions and exclusions

### 4.1 Objective (Plan §6.6; instruction §4)

Close the actual complete promoted release and its same-root, deterministic generated evidence: the real repository root admits through the unchanged §2.12 owner, the manifest is the complete 44-member roster at `1.1.0` / `2026-08-24T18:04:49Z`, every governed derivative that changes is regenerated by its owner, the F01 interval ends on the real root, and the external attestation builder can produce `PR06R_B_FINAL_PASS` from this candidate into an external empty directory.

### 4.2 Completion conditions

| # | Condition | Proof home |
| --- | --- | --- |
| CC-1 | `catalog/manifest.json` lists exactly the 44 roster paths in ASCII order, no self-listing, no extra, version `1.1.0`, `built_at_utc 2026-08-24T18:04:49Z`, every row's hash and size equal to the validated on-disk bytes; `scripts/release_id_recompute.py --check-manifest-only` and cutter `--check` exit 0 | §§5.1, 10.2 |
| CC-2 | `load_active_mechanics_bundle()` admits the real root (no `HDE_CONFIG_ROOT`, no fixture) and `engine.runtime.identity` reports the same `release_id`; the pre-PR06 refusal is proven by the same test on the baseline manifest fixture | §8.2 |
| CC-3 | `generate_config_artifacts.py --compare-goldens <real root>` exits 0 with all eight goldens equal and a report written outside the tree; the O-17/CR-06 bounded treatment refuses `ok: true` for a manifest-consistent candidate whose executed application member differs from the installation | §§5.5, 8.3 |
| CC-4 | Config family, canonical JSON gate outputs, determinism, open-rails, A7, Index/Mirror/path proofs/orientation and the sanity log converge through their owners; every read-only check of §10.4 exits 0; the sanity log is the PASS model and the gate wrapper exits 0 | §§5.6–5.7, 10 |
| CC-5 | The 22 interval-pinned tests express the admitted posture; no test is skipped, disabled or quarantined; all seven CI lanes and the supplemental roster pass on the exact candidate head; the final audit finds a clean tree | §§8.6, 10.4–10.5 |
| CC-6 | `build_release_attestation.py --output <external empty dir> --require-clean` succeeds on the clean candidate and `--verify` exits 0; the bundle carries `PR06R_B_FINAL_PASS` only because the real candidate admitted; achievable once §5.11 is in place (§10.6 records the rehearsal) | §§5.11, 10.6 |
| CC-7 | PR-session code review, security review of corrected code, and CI on the exact head; native findings resolved on the current substantive change; the PR description follows the template with the merge statement of §15 | §§11, 15 |

The in-CI attestation of CC-6 is **not** the final OPS01 attestation; that waits for PR07's documentation (instruction §4).

### 4.3 Hard exclusions

PR07 (DOC-10; F03/F05/F07 and their re-cut), OPS01, independent QA, Ops, deployment, release activation, live DB or vendor work, PF-Canon edits (including PF10, PF12, PF01), PF09 movement, Epic closure, any change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS`, widening of the §2.12 covered-module set, extension of the canonical JSON gate's 26-target roster or six set rules, any gate change beyond PF10 §2.21's delta, refreshing historical EPIC022/EPIC038 evidence in the tree, regenerating or re-identifying the frozen showcompat / CLI-conformance captures (alternative B stays with PR07 / the Product Owner), and any change to `engine/narratives/loader.py`, `engine/config/registry_loader.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py` or `.github/workflows/ci.yml`.

## 5. Designed interfaces, invariants and contracts

Every design item names its exact locus, the contract it must keep, the failure tokens it adds, and the owner it must not displace. Nothing here changes mathematics, taxonomy, schemas, result fields, identity formulas, public routes, payloads or transport.

### 5.1 Manifest cutter — `scripts/cut_release_manifest.py` (owned locus)

**Contract kept.** `cut_manifest(manifest_path, *, version, built_at_utc, check=False, _publish=None) -> int` keeps its signature, closed-rails guard, input validation, canonical-manifest requirement, path-safety rules, sort, canonical render, `check` fixed-point semantics and private publisher seam. `--check` never writes and never calls the publisher.

**Extension (Plan §6.6, instruction §5.1).**

1. New keyword-only parameter `roster: Sequence[str] | None = None` and CLI flag `--roster-from-admission`. When the flag is given, the CLI passes `roster=engine.config.registry_loader.ADMITTED_RELEASE_ROSTER` (imported by the CLI layer only; the library function takes any explicit sequence so tests can drive it). Without the flag, behaviour is exactly today's refresh of the existing rows.
2. With a roster: after loading and validating the existing manifest, the cutter builds the membership as `{existing rows} ∪ {roster paths}` where every roster path gets exactly one row (existing row refreshed, absent row added), then refuses `release_manifest_extra_member:<path>` for any existing row whose path is not in the roster (no non-input extras), refuses `release_manifest_roster_invalid` if the roster is empty, has duplicates, is not ASCII-sorted, contains an unsafe path or the manifest's own path (no self-listing), and refuses `release_manifest_source_missing` / `release_manifest_source_symlink` as today for absent or symlinked members.
3. Member format validation before hashing (PF12 §5.1 "Manifest and member form", §5.2): for every row, in both modes, validate the member's owning format with the admission owner's existing rule (`engine.config.registry_loader._parse_release_member_bytes(raw, relative_path)`: canonical JSON for `.json`; UTF-8, non-empty, single final LF and `ast.parse` for `.py`; UTF-8, non-empty, single final LF for `.sql`; `UNSUPPORTED_MEMBER_FORMAT` otherwise), and refuse `release_manifest_member_format_invalid:<path>:<code>` on failure. The hash and size are then taken over the exact validated bytes; the cutter never normalizes, re-serializes or rewrites a member (F-03 members are finalized as source before the cut, §5.2). Importing that private helper mirrors the canonical JSON gate's existing practice of importing private admission helpers; no new public API is added to the admission owner (D-04).
4. `version` and `built_at_utc` remain explicit inputs; PR06's cut passes `1.1.0` and `2026-08-24T18:04:49Z` (Canon-fixed source values, never the run's clock).
5. Error surface: the CLI keeps `RELEASE_MANIFEST_CUT_FAILED:<message>` on stderr and exit 1 for every `ValueError`, so the new tokens surface through the existing channel.

**Invariant.** With the real roster, the rendered manifest is exactly `{root: "catalog/", version, built_at_utc, files: [44 rows in ASCII order]}` in canonical bytes; `release_id = sha256(those bytes)`; `--check` after the cut returns 0 and any later member change makes it return 1.

### 5.2 Source finalization before the cut (Plan §6.6 inputs; instruction §5.3 step 1)

Three roster members fail the member-format rule today (F-03). They are finalized as source bytes, with parsed content unchanged, before any cut:

| Member | Owner and action | Verification |
| --- | --- | --- |
| `errors/token_map/token_map.json` | Its owner `tools/errors/generate_error_artifacts.py` regenerates it. The owner's token-map write changes from `json.dumps(indent=2, sort_keys=True) + "\n"` to canonical bytes (`engine.serializer.canon.sercanon(payload, sort_keys=True)`) for exactly this output — a new `_write_canonical_json` used by the token-map line of `write_parity_artifacts`; the parity JSON and CLI text outputs under `parity/` and `errors/schema_check/` keep their current writers and bytes | `json.loads(old) == json.loads(new)`; `tests/cli/test_errors_parity.py::test_token_map_snapshot_matches_canonical` still passes; new test §8.5 pins canonical bytes |
| `schemas/reader.v1.schema.json` | Hand-maintained schema; rewritten to its canonical serialization (`sercanon(json.loads(bytes), sort_keys=True)`) as a byte-form change only | parsed-equality check recorded in the result; the `.sha256` sidecar refreshed (next row) |
| `schemas/reader.v1.schema.json.sha256` | No generator owns it (F-04); refreshed to `<sha256 of the canonical schema>  schemas/reader.v1.schema.json\n` (`sha256sum` format, exactly as today) | `sha256sum -c` passes; `scripts/make_cli_smoke_audit.sh` reads it unchanged |
| `adapter/schemas/error_v1.schema.json` | Hand-maintained schema; canonical serialization, byte-form change only | parsed equality; `tests/adapter/test_jsonschema.py` and compat lane unchanged |

Rejected alternative: leaving the files non-canonical, which the admission owner refuses (`NONCANONICAL_JSON`) and PF12 §5.2 forbids repairing by normalized hash input. Boundary: `tools/errors/generate_error_artifacts.py` is outside §6's list but is the owner of a promoted member; touching only its token-map writer is the "canonical source files finalized before cutting" input of Plan §6.6 and alters no gate semantics (D-02, §14).

### 5.3 Canonical JSON gate — `tools/evidence/run_canonical_json_gate.py` (necessary dependent; no roster extension)

`_EXPECTED_RELEASE_MANIFEST_PATHS` becomes `tuple(ADMITTED_RELEASE_ROSTER)` (the gate already imports from `engine.config.registry_loader`; the import list gains `ADMITTED_RELEASE_ROSTER`). Nothing else in the gate changes: `EXPECTED_TARGET_PATHS` stays the same 26 paths, `EXPECTED_SET_RULES` the same six entries, `_validate_release_manifest_snapshot` keeps its temp-root reconstruction and `cut_manifest(check=True)` call, `GATE_CAPTURED_AT_UTC` stays fixed. The instruction's adverse row "the fixed canonical-JSON gate roster is not silently extended" is satisfied by an explicit test that the target count is 26 and that the manifest validator refuses a 45-member manifest (`release_manifest_input_roster_invalid`) and a 43-member one (§8.4). Boundary: this is a coherence rebind of a predicate to the governed roster, not a gate-semantics change (D-03, §14).

### 5.4 Admission — `engine/config/registry_loader.py` (integrate only)

No production change. PR06 exercises the unchanged owner on the real root: `load_active_mechanics_bundle()` must admit with `release_id == sha256(canonical manifest bytes)`, `manifest_sha256`, `config_sha256` and 44 `source_identities`; the eight-owner executable-equivalence check runs as today. The F01 probe helpers (`release_not_admitted_observed()` in the sanity pipeline, gate wrapper, closure, builder and generators) stay in place and return `False` on the real root; their `True` branch is still covered by tests through a synthetic non-admitted root or a patched provider, never by the real root (§8.6). `test_actual_partial_repository_cannot_return_an_active_handle` becomes the pre-PR06 refusal proof on a fixture carrying the baseline 15-member manifest (CC-2 "refuses before PR06 and succeeds after").

### 5.5 Golden comparator — O-17/CR-06 bounded treatment in `tools/config/artifacts.py` (owned locus)

**Gap (F-14).** After `_golden_admit` proves the candidate's bytes are manifest-consistent, the runners execute the installation's application modules. A candidate root whose `engine/compat/compute.py` (or another executed member outside the eight §2.12 owners) differs from the executing installation still reports `ok: true` if the installation's module matches the goldens.

**Treatment inside the admission owner's existing scope (no §2.12 widening).** `compare_goldens` gains one read-only predicate, evaluated after `_golden_admit` and again after the last case ran (runners import lazily):

- `GOLDEN_EXECUTED_MEMBER_MODULES`: the fixed mapping of every `.py` roster member to its module name (`engine/compat/compute.py → engine.compat.compute`, `tools/bodygraph/check_magic10_gate_readiness.py → tools.bodygraph.check_magic10_gate_readiness`, `presenter/reader_v1/emitter.py → presenter.reader_v1.emitter`, and so on for all 33 `.py` members), derived from `ADMITTED_RELEASE_ROSTER` at import time so it cannot drift from the roster.
- For each member whose module is present in `sys.modules`: require `module.__file__` to be a readable regular file (else refuse `CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE:<path>`), read its bytes, and require `sha256(bytes) == candidate identity for that path` from `bundle.source_identities` (else refuse `CANDIDATE_EXECUTING_SOURCE_MISMATCH:<path>`). Modules not loaded are not executed by the goldens and are not bound.
- A refusal is a `GoldenComparisonRefusal` (exit 5 through the CLI, never `ok: true`, never a mismatch row); `render_golden_report` is unchanged.

**Why this is bounded.** It compares the installation's on-disk source of an executed module with the candidate's manifest-bound bytes; it does not compile, reload, import, or compare code objects, so it neither widens the §2.12 owner nor moves any I/O into core. For the real root the installation and the candidate are the same tree, so the predicate holds; for the synthetic fixture (built from the same tree with the same member bytes) it holds; for a fixture with a deliberately altered application member it refuses (§8.3). Recorded limitation: executable equivalence for the non-covered members (a module replaced after import) remains unproven; widening §2.12 would be a §9 route and is not planned (D-05, §14).

### 5.6 Config family publication — `tools/config/generate_config_artifacts.py` (owned locus)

**Contract kept.** `generate_config_artifacts.py` (write) and `--check` keep working on partial roots and on local registry captures without any release (`tests/config/test_registry_catalog_contract.py` relies on that); `--compare-goldens` keeps its exit codes 0/1/5 and its aliases/goldens/report rules; `--publish-family` keeps its sequence, the cutter check, `check_manifest_only`, the gate, and the updater's `publish_config_family` transaction with all its refusals.

**Change (instruction §5.2).** `--publish-family` gates on real admission and on same-capture identity:

1. Before any production step it calls `engine.config.registry_loader.load_active_mechanics_bundle()` (the unchanged owner) and refuses `CONFIG_PUBLICATION_RELEASE_NOT_ADMITTED:<code>` on any `SchemaValidationError`/`RegistryConfigError`, so a partial or tampered root can never publish the config family.
2. After the primaries are produced from the local registry capture it requires that capture's identity to equal the admitted bundle's: `capture.config_sha256 == bundle.config_sha256` (the exact four-input source hash the owner computed), refusing `CONFIG_PUBLICATION_CAPTURE_MISMATCH` otherwise; the same equality is asserted in `_verify_checked_outputs` for `--check` runs on the real root only when admission succeeds (a non-admitted root keeps today's local semantics for `--check`).
3. The registry report stays bound only to registry catalog inputs (never to `release_id`), exactly as `AGENTS.md` requires; the manifest row in the config family remains handled by `MUTABLE_RELEASE_SOURCE_INDEX_KEYS`.

**Ordering invariant (F-07).** `--publish-family` is run only after the canonical JSON gate outputs and every other non-config record are current in the Mirror (a full updater run precedes it); the gate run inside publication is then byte-idempotent and the `_config_logical_delta` guard stays silent. `tools/config/generate_bundles.py` and `tools/generate_registry_report.py` need no code change; they are re-run through publication.

### 5.7 Evidence convergence order (instruction §5.3; Plan §6.6)

The order below is fixed by the owners' own preconditions (F-07, F-08, F-09). Every producer is an existing owner; nothing is hand-edited; every step is re-run on unchanged inputs to prove a fixed point before the next.

| Step | Owner command (closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`) | Produces / proves |
| --- | --- | --- |
| 1 Source bytes | §5.2 finalization (token-map owner run; canonical schema bytes; sidecar) | the 44 members pass the member-format rule |
| 2 Cut | `python scripts/cut_release_manifest.py --version 1.1.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; then `python scripts/release_id_recompute.py --check-manifest-only`; then the same cutter call with `--check` | complete canonical manifest; `release_id` fixed; fixed point |
| 3 Admission and comparison | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; print(l().release_id)"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | real-root admission; eight goldens equal; exit 0 |
| 4 Gate | §5.3 rebind; `python tools/evidence/run_canonical_json_gate.py`; `python tools/evidence/run_canonical_json_gate.py --check-only` | gate outputs for the 44-member manifest; 26 targets pass |
| 5 Updater | `python tools/evidence/update_evidence_index.py`; `python tools/evidence/update_evidence_index.py --check` | Index/Mirror/path proofs bind the gate outputs, the canonicalized members and the token map; required before step 6 (F-07) |
| 6 Config family | `python tools/config/generate_config_artifacts.py --publish-family` (§5.6) | primaries, catalog logs, bundles, registry report, arrays report; gate byte-idempotent; updater config-family transaction |
| 7 Live producers | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; `python tools/evidence/generate_determinism_gate_proofs.py`; `python tools/evidence/generate_open_rails_abba_proof.py`; then each owner's `--check` | A7 transport family, determinism family, fixture open-rails proof regenerated from the admitted root; `--live --check` of the open-rails proof still validates the retained PO-run live proof (no live vendor call) |
| 8 Updater | `python tools/evidence/update_evidence_index.py`; `--check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh` | all companions current |
| 9 Sanity transition | §5.8 | `audit/gates/sanity_pipeline/sanity_pipeline.log` in the PASS model, bound, fixed point; gate wrapper exit 0 |
| 10 Frozen families | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen digests intact; no write |
| 11 Interval tests | §8.6 | the 22 tests express the admitted posture |
| 12 Candidate-wide | §10.4–10.5; §10.6 attestation rehearsal | every lane green locally; clean tree |

Any change to a source byte after step 2 restarts at step 2 (a re-cut); any change to an evidence primary restarts at step 5. Steps 4–10 are re-runnable and must be byte-stable on the second run (the definition of convergence used here).

### 5.8 Sanity-log model transition NOT_ADMITTED → PASS (O-07; F-08)

Mechanics (verified by reading `run_sanity_pipeline.py` and by rehearsal): stage 11 is `update_evidence_index.py --check`; before it, a canonical run writes the prospective PASS log; the check passes only if the Mirror already binds the PASS-model bytes. The FAIL-only `--rebind-sanity-log` cannot bind PASS, and the full updater binds whatever bytes are on disk. Procedure, all through owners:

1. Prove every stage passes without touching the canonical log: `python tools/evidence/run_sanity_pipeline.py --log-path <outside the tree>/sanity.log` must exit 0 with `summary:PASS` (a non-canonical run writes no prospective log and rebinds nothing).
2. Render the PASS model with the owner's renderer to the canonical path: `python -c "from tools.evidence import run_sanity_pipeline as p; p.SANITY_LOG.write_bytes(p._render_log([(n, 'OK') for n in p.STAGE_NAMES], 'NONE', 'PASS'))"` — the same function and bytes the canonical run itself writes at its sealing index; not a hand edit, and validated in the next two steps.
3. `python tools/evidence/update_evidence_index.py` (binds the PASS model), then `--check`.
4. Canonical run `python tools/evidence/run_sanity_pipeline.py` → exit 0, byte-identical PASS; then `python tools/evidence/run_sanity_pipeline_gate.py` → exit 0; then `update_evidence_index.py --check` → 0. If the canonical run fails, the owner rewrites the FAIL log and rebinds it — no false PASS can persist.

Observation for the owner (non-gating, §13.2): O-07's recipe ("owner canonical run, then full updater") is sufficient for PASS → NOT_ADMITTED but not for the reverse; the reverse needs the pre-binding above.

### 5.9 Narrative pack mount (PR04 O-18; F-12) — settled within scope, production mode recorded with its owner

Decision D-08. The loader-produced mount for the current pack, `narratives/4cc79e0535d93acece861fff5e725a26b62ab22ee2c03c9bae2632a5570953a0/` (the 10 files `_copy_files_atomic` writes: `keys.json`, `manifest.json`, `palettes.json`, `suppression_map.json`, `templates.json` and their `.sha256` sidecars, byte-identical to `catalog/narratives/`), is produced by one live evaluation on the admitted root (its owner) and committed; the stale tracked mount `narratives/64e17c9c…/` (never read by the loader; 9 of 10 files differ from the current pack) is removed. Effects: the loader finds a byte-exact mount and writes nothing on every evaluation, so CI's clean-tree assertions, the residue test and the attestation write boundary hold; `engine/narratives/loader.py` and `state.py` are untouched (no product behaviour change; no gate semantics change). `ci/checks/classify_ci_changes.py` registers the `narratives/` prefix (§6.2). Not settled here and recorded with the narrative loader owner (§13.2): the request-path mount on a cold read-only production worker and concurrent cold workers racing on the shared mount; the tracked mount mitigates only a deployment from this tree with the working directory at the repository root. The alternative — a loader-side mount strategy (packaged read-only resources or an explicitly writable, process-safe mount root) — is a product change outside PR06's loci and would be a §9 route if the Product Owner prefers it; it is not required for PR06's completion.

### 5.10 Failure tokens added (all on existing channels; none is an acceptance token)

| Token | Owner | Meaning |
| --- | --- | --- |
| `release_manifest_extra_member:<path>` | cutter | a row not in the roster (non-input extra) |
| `release_manifest_roster_invalid` | cutter | roster empty, unsorted, duplicate, unsafe or self-listing |
| `release_manifest_member_format_invalid:<path>:<code>` | cutter | member fails its owning format rule before hashing |
| `CONFIG_PUBLICATION_RELEASE_NOT_ADMITTED:<code>` | config publication | `--publish-family` on a root the admission owner refuses |
| `CONFIG_PUBLICATION_CAPTURE_MISMATCH` | config publication | primaries' capture identity differs from the admitted bundle's `config_sha256` |
| `CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE:<path>` / `CANDIDATE_EXECUTING_SOURCE_MISMATCH:<path>` | comparator | executed member's installation source unreadable / differs from the candidate's manifest-bound bytes (refusal, exit 5) |

No error-token registry entry (`engine/compat/error_tokens.py`, `errors/token_map/token_map.json`) changes: these are tool refusals, not compat/reader error tokens. The §5.11 tokens `frozen_capture_identity_source_unverified:<path>`, `frozen_capture_identity_shape_invalid:<path>` and `frozen_capture_identity_disagreement` are gate refusals on the same channel.

### 5.11 Frozen-capture identity source for the canonical JSON gate — `tools/evidence/run_canonical_json_gate.py` (approved overlay locus, PF10 §2.21; review §4)

**Approved delta.** `_CAPTURE_IDENTITY_META` is no longer read from `artifacts/identity/service_identity.json` (which the isolated closure regenerates). The expected capture-time identity is derived from the frozen captures themselves, read only after each capture's frozen digest is verified.

**Design (exact, bound to the review's conditions 1–7).**

1. Remove the import-time constants `_CAPTURE_SERVICE_IDENTITY` and `_CAPTURE_IDENTITY_META`; the gate reads `service_identity.json` for no purpose afterwards (condition 2).
2. Add the fixed source roster `_CAPTURE_IDENTITY_SOURCES` — the four identity-carrying frozen captures that hold a digest in `_FROZEN_GENERATED_SHA256`, with the key path each records its identity under: `artifacts/cli/showcompat/args.json` → `identity.meta`; `artifacts/cli/showcompat/stdout.json` → `compat.meta`; `artifacts/cli/ab.json` and `artifacts/cli/ba.json` → `conjunction.compat.meta`. `artifacts/cli/summary.json` also carries an identity (`identity.meta`) but has no digest in the gate's table, so it is not a source: its identity is still compared against the agreed value through `_validate_cli_summary` → `_validate_runtime_identity` and refuses on disagreement (condition 3). No digest is added for it (the addendum excludes changing the captures' digests). Reader envelopes carry no `release_id` and stay validated by `_validate_reader_meta` as today.
3. Add `_capture_identity_meta() -> dict[str, str]`, evaluated at validation time (never at import): for each source, read and parse the file under `ROOT`, require a frozen digest to exist in `_FROZEN_GENERATED_SHA256` and `sha256(sercanon(obj)) == digest` **before** touching the identity (else refuse `frozen_capture_identity_source_unverified:<path>`); walk the key path (else `frozen_capture_identity_shape_invalid:<path>`); require exactly `{engine_tag, invocation_tag, release_id}` with the existing string/hex64 rules; then require all four source identities to be equal (else `frozen_capture_identity_disagreement`) and return the agreed identity (conditions 2 and 3).
4. `_validate_runtime_identity` compares the presented `meta` with `_capture_identity_meta()` and keeps its token `runtime_identity_source_mismatch`; every other check in the gate — canonical bytes, frozen digests, schema documents, set rules, the 26 `EXPECTED_TARGET_PATHS`, the six `EXPECTED_SET_RULES`, `GATE_CAPTURED_AT_UTC` — is untouched (condition 3).
5. `service_identity.json` and the identity family stay certified against the current release by their own owners (`generate_identity_provenance.py --check`, `release_id_recompute.py --check`, `generate_release_bindings.py --check`) inside the isolated closure; nothing about them changes (condition 4).
6. No capture, generator, digest, closure, builder, schema, wire value or Index/Mirror row changes beyond a legitimate owner run (condition 6). Alternative B (re-identifying the captures) stays with PR07 / the Product Owner.
7. Honest attestation content (condition 7): the builder's payload already records `nonclaims` (`builder_executes_no_ops`, `no_database_write`, `no_deployment_or_migration`, `no_qa_pass_or_acceptance`, `no_pf09_status_movement`) and binds every evidence file by digest without describing provenance; it makes no claim that the frozen captures were produced by the current release. The `PR_IMPLEMENTATION_RESULT` states, under its nonclaims, that the bundle carries current identity evidence alongside frozen capture-time captures (EPIC022 D2 and CLI conformance) with their existing nonclaims. The builder is not changed (it is outside the approved loci).

**Invariant.** With the four digest-bound captures intact and `summary.json` agreeing, the gate passes whatever `service_identity.json` or the identity family currently say; any tamper to a capture's bytes, any disagreement between capture identities, and any capture without a verified frozen digest refuses before the identity is compared.

## 6. Exact file and component plan

### 6.1 Owned loci (instruction §6)

| Path | Change | Why |
| --- | --- | --- |
| `scripts/cut_release_manifest.py` | roster-driven membership construction; member-format validation before hashing; new failure tokens; `--roster-from-admission` | §5.1 |
| `scripts/release_id_recompute.py` | no code change planned (its manifest-only predicate already validates the 44-member manifest; verified by rehearsal); tests only | §5.7 step 2 |
| `engine/config/registry_loader.py` | no change (integrate only) | §5.4 |
| `tools/config/artifacts.py` | O-17/CR-06 executed-member source binding in `compare_goldens`; two refusal tokens | §5.5 |
| `tools/config/generate_config_artifacts.py` | `--publish-family` admission gate and same-capture equality | §5.6 |
| `tools/config/generate_bundles.py`, `tools/generate_registry_report.py` | no code change; re-run through publication | §5.6 |
| `tools/evidence/update_evidence_index.py` | no code change planned; sole writer for Index/Mirror/path proofs/orientation in steps 5, 6, 8, 9 | §5.7 |
| `tools/evidence/build_release_attestation.py` | no change: the F01 gap was not in the validator and is resolved by the gate change (PF10 §2.21) | §§5.11, 14 |
| `tools/evidence/run_canonical_json_gate.py` (approved overlay locus, PF10 §2.21) | frozen-capture identity source per §5.11; plus the D-03 roster rebind of §5.3 | §§5.3, 5.11 |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` (approved overlay test home) | §8.7 overlay tests; §8.4 rebind tests | §8 |
| `catalog/manifest.json` | cut by the cutter only: 44 rows, `1.1.0`, `2026-08-24T18:04:49Z` | §5.1 |
| Existing manifest, config and evidence tests | §8 | |

### 6.2 Necessary dependents (coherence; no gate semantics)

| Path | Change | Class |
| --- | --- | --- |
| `tools/evidence/run_canonical_json_gate.py` | `_EXPECTED_RELEASE_MANIFEST_PATHS = tuple(ADMITTED_RELEASE_ROSTER)`; import added (the file is also an approved overlay locus, §6.1) | predicate rebind to the governed roster (§5.3, D-03) |
| `tools/errors/generate_error_artifacts.py` | canonical writer for the token-map output only | owner of a promoted member; source finalization (§5.2, D-02) |
| `errors/token_map/token_map.json` | regenerated by its owner (canonical bytes) | promoted member |
| `schemas/reader.v1.schema.json`, `adapter/schemas/error_v1.schema.json` | canonical bytes, identical content | promoted members (§5.2) |
| `schemas/reader.v1.schema.json.sha256` | refreshed digest, same format | companion of a promoted member |
| `narratives/4cc79e05…/` (10 files added), `narratives/64e17c9c…/` (10 files removed) | loader-produced mount tracked; stale mount removed | O-18 settlement (§5.9, D-08) |
| `ci/checks/classify_ci_changes.py` | register `errors/token_map/token_map.json` → `{compat, product, release}`; `tools/errors/generate_error_artifacts.py` → `{compat, release}`; `narratives/` prefix → `{compat, product}`; keep every existing table | coherence registration (instruction §6; PF10 §2.15 ownership limits) |
| Interval-pinned test homes outside the owned test homes | §8.6 | tests express the gate outcomes §5.4 of the instruction requires |

### 6.3 Governed evidence regenerated by owners (never hand-edited)

Config family (`artifacts/thresholds/magic10_config.json`, `artifacts/thresholds/band_edges.json`, `artifacts/registry/registry_report.json`, `artifacts/config_bundles/{fe,be}_bundle.json`, `artifacts/catalog/*.log`, `artifacts/canonical/arrays_as_sets_report.log`), canonical JSON gate outputs (`audit/gates/canonical_json/*`, `audit/gates/json_gate/canonical/*`), determinism family (`audit/gates/parity/reader_cli/{ab,ba,summary}.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256`, `artifacts/cards/a3/IDENTITY_OK.txt`), open-rails fixture proof (`audit/gates/determinism/open_rails_abba.json`), A7 transport family (`docs/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/audit/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/*` of that family), the sanity log, and every Index/Mirror/path-proof/orientation companion through the sole updater. Exactly which of these change is determined by the owners on the real branch; the rehearsal saw the config family, the gate outputs, the A7 family, the token-map proof, the sanity log and their companions change, and the determinism and open-rails outputs rewritten byte-identically.

### 6.4 Frozen families (stay frozen, with nonclaims)

`artifacts/cli/showcompat/*` and `artifacts/cli/{ab,ba,summary}.json` plus help/install captures (EPIC022 D2 and CLI conformance; O-09/O-20/O-21: write modes refuse on the real root with `ERR_M10_LEGACY_INPUT_UNSUPPORTED` and `DB_QUERY_FAILED`); `artifacts/identity/*`, `artifacts/math/*`, `artifacts/parity/two_run_identity.log`, `artifacts/bodygraph/release_bindings.json`, `artifacts/runtime/env_matrix.snapshot.json` (frozen capture-time identity evidence; regenerated only by the isolated closure per `AGENTS.md`); `artifacts/vendor/*`, `audit/ops/*`, EPIC032 router captures (frozen, refused for write). Their `--check` posture on the baseline is recorded in §3.2 F-17 and §14.

### 6.5 Consequence for CI lanes

The candidate changes `ci/checks/classify_ci_changes.py`, so full validation applies: all seven lanes plus `_FULL_VALIDATION_SUPPLEMENTAL_TESTS`. Independently, `catalog/manifest.json` selects `release`; the cutter, `registry_loader.py` tests and the config tools select `product`/`evidence`/`release`; the gate selects `evidence`/`release`; the schema files select `compat`/`product`/`release`. The rails and release lanes' `RELEASE_NOT_ADMITTED` branches are never taken on this candidate (F-16).

### 6.6 Explicitly unchanged paths

`engine/**` (including `engine/config/registry_loader.py`, `engine/narratives/loader.py`, `engine/narratives/state.py`, `engine/runtime/identity.py`), `.github/workflows/ci.yml`, `ci/jobs/*.yml`, `ci/checks/run_rails_job_definitions.py`, `tools/evidence/regenerate_identity_closure.py` (18 steps, 185 declared outputs including path proofs), `tools/evidence/build_release_attestation.py`, `tools/evidence/run_sanity_pipeline.py`, `tools/evidence/run_sanity_pipeline_gate.py`, `tools/cli/generate_showcompat_artifacts.py`, `tools/cli/generate_cli_conformance_artifacts.py`, the frozen captures and their digests, `artifacts/identity/*`, `schemas/hde_release_attestation*.json`, `pyproject.toml`, `docs/pfcanon/**`, every historical evidence family.

## 7. Requirement-to-change-and-test mapping

| Requirement / criterion (Spec v1.1; Plan §§7.2–7.4) | PR06 change | Proof |
| --- | --- | --- |
| `K040-REQ-006` single immutable manifest-bound active configuration; no partial release | 44-member cut (§5.1); real-root admission (§5.4); `--publish-family` gated on admission (§5.6) | §8.1, §8.2, §8.4 |
| `K040-REQ-009` distinct config, source, pair, manifest and repo identities with exact closure | `release_id` from canonical manifest bytes; `config_sha256` same-capture equality; source identities for 44 members | §8.2, §8.4 |
| `K040-REQ-010` actual-candidate comparison | `--compare-goldens <real root>` exit 0; executed-member source binding (§5.5) | §8.3 |
| `K040-REQ-012` convergence of primaries and companions | §5.7 order; sanity PASS model (§5.8); read-only checks; frozen-capture identity source so the isolated closure can run (§5.11, PF10 §2.21) | §8.5, §8.7, §10.4, §10.6 |
| Portions of `-001` (approved mechanics only, no change), `-004` (external loader/admission fails closed), `-008` (adverse admission and evidence tests), `-011` (evidence through owners) | no mechanics change; refusals; owners only | §8 |
| `AC040-05` distinct identities; `AC040-06` actual complete admitted candidate; `AC040-08` evidence coherence; `AC040-09` exact request/decision/source/commit/review/CI/release identities | as above; PR record; CC-1…CC-7 | §§10, 15 |

OPS01's external proof is not claimed (instruction §7).

## 8. Detailed test design

Fixture policy: every adverse case runs on a synthetic root built by `tests/config/helpers.py::synthetic_complete_release_root` (or a copy of the real root under `tmp_path`); the real root is used only for positive admission and comparison proofs. No test is skipped, disabled or quarantined; every interval test is rewritten to assert the admitted posture plus a synthetic non-admitted case where the F01 branch remains reachable.

### 8.1 `tests/scripts/test_cut_release_manifest.py` (existing home)

- `test_roster_cut_constructs_exactly_the_admitted_roster`: fixture with the baseline 15-member manifest and all 44 members present → cut with the roster → 44 rows in ASCII order, version/timestamp as given, canonical bytes, `--check` fixed point, `release_id == sha256(bytes)`.
- Adverse: each of the 44 members omitted in turn from the fixture → `release_manifest_source_missing`; an existing non-roster row → `release_manifest_extra_member`; roster with duplicate / unsorted / unsafe / self-listing entry → `release_manifest_roster_invalid`; non-canonical `.json` member, `.py` without final LF, CRLF `.sql`, BOM, non-UTF-8 → `release_manifest_member_format_invalid:<path>:<code>`; symlinked member → `release_manifest_source_symlink`; `check=True` never writes and never calls `_publish`; existing behaviour without a roster unchanged (existing tests kept).

### 8.2 `tests/config/test_production_admission.py`, `tests/config/test_execution_coherence.py`, `tests/config/test_manifest_schema.py`, `tests/runtime/test_identity.py` (existing homes)

- `test_actual_repository_root_admits`: `load_active_mechanics_bundle()` on the real root returns a bundle with 44 `source_identities`, `manifest.version == "1.1.0"`, `built_at_utc` as adopted, `release_id == engine.runtime.identity.identity_meta()["release_id"] == sha256(canonical manifest bytes)`.
- `test_baseline_partial_manifest_still_refuses` (replaces `test_actual_partial_repository_cannot_return_an_active_handle`): a fixture carrying the pre-PR06 15-member manifest refuses `INCOMPLETE_RELEASE_ROSTER` through the public API (CC-2 "before and after").
- `test_generic_manifest_shape_does_not_claim_full_release_admission` → asserts 44 rows, `1.1.0`, no self-listing, and that `load_manifest` still returns a generic manifest without admission authority.
- Existing 43-member / extra-member / tamper / mixed-root / symlink cases kept on the synthetic fixture (Plan §6.6 adverse rows).

### 8.3 `tests/config/test_config_artifacts.py` (existing home; PR05's comparator tests)

- `test_compare_goldens_admits_the_real_root`: `--compare-goldens ROOT` → exit 0, eight `match`, `ok: true`, `candidate_release_id` equals the real `release_id`; report written outside the tree and never inside it.
- `test_admission_refusals_are_never_equality` → the real-root row becomes the positive case above; the incomplete and tampered synthetic rows stay.
- `test_cli_refusals_and_usage` → the first assertion moves to a synthetic incomplete root; all other rows unchanged.
- O-17/CR-06: `test_executed_member_source_mismatch_refuses`: synthetic complete root with `engine/compat/compute.py` altered by a trailing comment and its manifest re-cut (manifest-consistent) → refusal `CANDIDATE_EXECUTING_SOURCE_MISMATCH:engine/compat/compute.py`, never `ok: true`; `test_executed_member_binding_is_read_only` (no write, no import of the candidate's file, `sys.modules` unchanged); `test_unloaded_members_are_not_bound`.
- §5.6: `test_publish_family_refuses_without_admission` (patched provider raising `INCOMPLETE_RELEASE_ROSTER` → `CONFIG_PUBLICATION_RELEASE_NOT_ADMITTED:INCOMPLETE_RELEASE_ROSTER`, nothing written); `test_publish_family_refuses_capture_mismatch`; `test_generate_and_check_keep_working_on_partial_roots` (existing behaviour pinned).

### 8.4 `tests/evidence/test_canonical_json_gate_check_outputs.py` (existing home)

- `test_manifest_validator_binds_the_admitted_roster`: `_EXPECTED_RELEASE_MANIFEST_PATHS == ADMITTED_RELEASE_ROSTER`; a 43-member and a 45-member manifest both fail `release_manifest_input_roster_invalid`; `len(EXPECTED_TARGET_PATHS) == 26` and `len(EXPECTED_SET_RULES) == 6` unchanged.
- `test_full_gate_outputs_remain_current_after_metadata_only_release_cut` → the temporary root copies every roster member (add `errors/`, `presenter/`, `tools/bodygraph/` to the copied set, or copy exactly `ADMITTED_RELEASE_ROSTER`).

### 8.5 `tests/cli/test_errors_parity.py` and evidence coherence

- `test_token_map_bytes_are_canonical`: `Path("errors/token_map/token_map.json").read_bytes() == sercanon(render_token_map(), sort_keys=True)`; the parsed-equality test stays.
- `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` unchanged (now over 44 rows).
- `tests/evidence/test_sanity_pipeline.py`: existing PASS-model and gate tests unchanged; add `test_pass_model_transition_requires_prebound_mirror` documenting §5.8 with a temporary root.

### 8.6 Interval-pinned tests rewritten to the admitted posture (22 tests, 13 files; F-15)

| File | Tests | Rewrite |
| --- | --- | --- |
| `tests/cli/test_cli_usage_and_errors.py` | `test_admission_refusal_is_a_single_stderr_token` | subprocess `hdctl showcompat --pair-file` on the real root now exits 0 with a canonical `magic10_compat_result.v1` document on stdout and empty stderr; the single-token refusal is asserted in-process through the existing `compute._BUNDLE_PROVIDER` seam (the public admission owner derives its root from execution provenance and honours neither `HDE_CONFIG_ROOT` nor the working directory, as `tests/config/test_production_admission.py` already pins) |
| `tests/cli/test_showcompat_sources.py` | `test_showcompat_refuses_without_an_admitted_release` | patched provider raising `INCOMPLETE_RELEASE_ROSTER` (existing `_BUNDLE_PROVIDER` seam) instead of the real owner |
| `tests/http/test_compat_endpoint_contract.py` | `test_compat_post_self_pair_returns_carrier_and_admission_refusal_is_503` | real owner → 200 with the evaluated payload; the 503 `ERR_M10_MANIFEST_MISMATCH` row uses a patched provider |
| `tests/cli/test_showcompat_parity_and_identity.py` | `test_governed_showcompat_capture_uses_immutable_identity` | write mode on the real root now refuses with the generator's own `showcompat failed (rc=1): ERR_M10_LEGACY_INPUT_UNSUPPORTED` (O-20) without writing; `--check` still validates the frozen digests; the `REQUIRES_ADMITTED_RELEASE` branch is asserted with a patched admission |
| `tests/config/test_config_artifacts.py` | `test_admission_refusals_are_never_equality`, `test_cli_refusals_and_usage` | §8.3 |
| `tests/config/test_manifest_schema.py` | `test_generic_manifest_shape_does_not_claim_full_release_admission` | §8.2 |
| `tests/config/test_production_admission.py` | `test_actual_partial_repository_cannot_return_an_active_handle` | §8.2 |
| `tests/config/test_registry_catalog_contract.py` | `test_source_capture_detects_later_change_and_base_needs_no_mechanics_release` | the fixture's `capture.config.manifest.version` becomes `1.1.0`; behaviour otherwise unchanged |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` | `test_full_gate_outputs_remain_current_after_metadata_only_release_cut` | §8.4 |
| `tests/evidence/test_determinism_gate_proofs.py` | `test_build_raises_typed_release_not_admitted_before_any_live_capture`, `test_main_check_prints_explicit_line_exits_distinct_code_and_writes_nothing`, `test_main_write_mode_writes_none_of_its_outputs_when_not_admitted` | keep the three under a patched provider raising `INCOMPLETE_RELEASE_ROSTER`; add `test_build_and_check_succeed_on_the_admitted_root` (write to `tmp_path`, byte-identical to the tracked outputs) |
| `tests/evidence/test_open_rails_abba_proof.py` | `test_not_admitted_fixture_proof_shape_without_live_capture`, `test_check_current_ends_not_admitted_with_distinct_code_and_frozen_primary_check`, `test_fixture_generation_and_check_refuse_without_writing_when_not_admitted` | patched provider for the three; add `--check-current` exit 0 and `top_level_pass is True` on the real root with no residue |
| `tests/evidence/test_rails_ci_workflow_integration.py` | `test_open_rails_producer_check_mode_has_no_repo_residue` | real root: `--check-current` exit 0, repo state unchanged (the tracked mount makes this hold), stdout the producer's existing JSON status line (`{"path": "audit/gates/determinism/open_rails_abba.json", "result": "pass", "status": "OK", "top_level_pass": true}`) |
| `tests/evidence/test_sanity_pipeline.py` | `test_probe_classifies_exactly_the_incomplete_roster_refusal`, `test_isolated_closure_refuses_with_the_distinct_code_before_any_producer` | real owner → `release_not_admitted_observed() is False` and `probe_release_admission()` returns a bundle; the `True` branches under a patched provider |
| `tests/transport/test_a7_transport_proofs.py` | `test_build_raises_typed_release_not_admitted_without_any_request`, `test_main_check_prints_explicit_line_exits_distinct_code_and_writes_nothing`, `test_main_write_mode_refuses_when_not_admitted` | patched provider for the three; add the admitted-root build and `--check` case |

The workflow-shape tests (`test_workflow_release_lane_accepts_only_the_release_not_admitted_receipt_with_probe`, runner exit-code tests) stay unchanged: the CI text they pin does not change (F-16).

### 8.7 `tests/evidence/test_canonical_json_gate_check_outputs.py` — overlay tests (review §4 condition 5)

All in the gate's existing test home; each uses a temporary copy of the relevant `artifacts/` files with `run_canonical_json_gate.ROOT` monkeypatched, as the file's existing tests do.

- `test_frozen_capture_identity_passes_when_service_identity_is_regenerated`: rewrite `artifacts/identity/service_identity.json` in the copy with a different `release_id` (the closure's effect), then `_validate_target` for each of the five identity-carrying targets (four sources plus `summary.json`) and `_run_gate(TARGETS, check_only=True)` → pass; `_capture_identity_meta()` still returns the frozen `12523fec…` identity.
- `test_frozen_capture_identity_refuses_tampered_capture`: change the `release_id` inside `artifacts/cli/showcompat/args.json` in the copy → refusal `frozen_capture_identity_source_unverified:artifacts/cli/showcompat/args.json` (digest verified before the identity is read); the target's own `frozen_generated_capture_mismatch` still fires on that file.
- `test_frozen_capture_identity_refuses_disagreement`: monkeypatch `_FROZEN_GENERATED_SHA256` with recomputed digests for a copy in which `ab.json`'s and `ba.json`'s identity differs from `showcompat/args.json`'s and `stdout.json`'s → `frozen_capture_identity_disagreement`, so a coherent forgery of one family cannot pass by re-freezing it alone; a second case leaves the four sources intact and changes only `summary.json`'s `identity.meta` → `runtime_identity_source_mismatch` from `_validate_cli_summary` (the consumer path).
- `test_frozen_capture_identity_refuses_unverified_digest`: monkeypatch `_FROZEN_GENERATED_SHA256` without the `artifacts/cli/ab.json` entry → `frozen_capture_identity_source_unverified:artifacts/cli/ab.json` before any comparison.
- `test_gate_never_reads_service_identity_for_capture_identity`: with `artifacts/identity/service_identity.json` removed from the copy, the five identity-carrying targets still validate; the gate module source contains no `service_identity` reference.
- `test_generated_compat_identity_binds_immutable_runtime_source` (existing, parametrized) is renamed `…binds_frozen_capture_identity`; its forged-`meta` assertion (`runtime_identity_source_mismatch`) is unchanged in substance.
- `test_conjunction_capture_rejects_coherent_forged_uids` and `test_conjunction_capture_rejects_coherent_same_band_score_forgery` (existing) build a temporary root holding only forged `ab.json`/`ba.json`; under §5.11 their first refusal becomes `frozen_capture_identity_source_unverified:<path>` (the temporary root lacks the showcompat sources, and the forged files fail their digests before any identity or uid check — rehearsed, §3.3). Rewrite them to keep their intent: copy the four unforged source captures into the temporary root and forge only the presented payload, so `person_uid_source_mismatch` is preserved for the uid case; for the coherent on-disk same-band forgery keep the forged files and assert the earlier, stronger refusal `frozen_capture_identity_source_unverified:artifacts/cli/ab.json`, adding a presented-payload variant that reaches the existing order's `conjunction_counterpart_mismatch`. No token is removed and every forgery still refuses.
- Unchanged: `test_all_26_current_target_bindings_execute`, `test_d1_inventory_is_complete_unique_sorted_and_bound`, the set-rule and schema tests — proving the roster and rules are untouched (condition 3).

## 9. Ordered implementation procedure (for PR-30, after the Product Owner's Proceed for this version)

One pull request, one coherent commit series in the order below (D-10). No split is planned: an intermediate state with a cut manifest but unconverged evidence or interval-pinned tests would be red on every lane and would not be a meaningful checkpoint. Each checkpoint ends with the listed proof; a failing proof stops the procedure at that checkpoint and never proceeds by hand-editing.

### C0 — Preconditions (not implementation)

- `HDE-EPIC040-PR06-F01` is decided (`APPROVE`, alternative A) and drained as PF10 §2.21; this v1.1 plans the delta in §5.11 under the review's seven conditions. No other decision is outstanding.
- Product Owner PR-30 Proceed for the exact plan version. PR-30 inspects existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06 before creating anything (none exist at planning time).
- Environment as §10.1; `origin/main` re-verified; any non-docs change since `190527cf…` re-evaluated against §3.2 before starting.

### C1 — Source finalization and cutter (§§5.1–5.2)

1. Implement the cutter extension and its tests (§8.1); run `python -m pytest -q tests/scripts/test_cut_release_manifest.py`.
2. Implement the token-map canonical writer; run `python tools/errors/generate_error_artifacts.py`'s token-map path through its existing entrypoint (the owner's normal invocation; if that entrypoint also rewrites the parity captures, verify by `git diff` that only `errors/token_map/token_map.json` changed bytes — parity artifacts must be byte-identical, otherwise stop and record).
3. Canonicalize the two schema files; refresh the sidecar; prove parsed equality for all three members (`python - <<'EOF' … json.loads(old) == json.loads(new) …`) and record the before/after sizes and digests of §3.2 F-03.
4. Cut: §5.7 step 2. Record `release_id`. Expected (inference from the rehearsal, to be confirmed on the branch): `988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e` with a 5,752-byte manifest, provided no other member byte changed.
5. Proof: cutter `--check` 0; `check_manifest_only` 0; `load_active_mechanics_bundle()` admits; `tests/config/test_production_admission.py`, `tests/config/test_execution_coherence.py`, `tests/config/test_manifest_schema.py`, `tests/runtime/test_identity.py` green after §8.2 rewrites.

### C2 — Comparator and config publication (§§5.5–5.6)

1. Implement the executed-member source binding and the publication gate with their tests (§8.3); `python -m pytest -q tests/config/test_config_artifacts.py`.
2. `--compare-goldens . --report <outside>/golden_report.json` → 0.
3. Proof: the adverse "altered application member" fixture refuses; the real root passes.

### C3 — Gate changes, evidence convergence and sanity transition (§§5.3, 5.11, 5.7, 5.8)

1. Implement §5.11 (frozen-capture identity source) and §5.3 (roster rebind) in the gate together with §8.7 and §8.4; `tests/evidence/test_canonical_json_gate_check_outputs.py` green; `python tools/evidence/run_canonical_json_gate.py --check-only` on the not-yet-converged tree already exercises the new identity path (the four sources agree at `12523fec…`).
2. Run §5.7 steps 4–10 in order; after each owner, its `--check`; after step 8 all read-only checks; after step 9 the gate wrapper.
3. Narrative mount (§5.9): after the first live evaluation of step 7 creates `narratives/4cc79e05…/`, `git add` it and `git rm -r narratives/64e17c9c…/`; confirm `python -c "from engine.narratives.loader import load_pack; print(load_pack().mount_path)"` writes nothing (`git status` unchanged).
4. Proof: `git status --short --untracked-files=all` shows only intended paths; a second run of steps 4–10 changes no byte.

### C4 — Interval tests and CI coherence (§§8.6, 6.2)

1. Rewrite the 22 tests; add the new positive cases; run each file.
2. Register the three classifier entries; run `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py` (classifier coherence tests) and the classifier dry-run of §10.3.
3. Proof: no `skip`, `xfail` or deselect was added; `grep -rn "not_admitted" tests` still covers every F01 branch through patched providers.

### C5 — Candidate-wide validation and attestation rehearsal (§§10.4–10.6)

1. Lane-equivalent commands of §10.4 in the order CI runs them; supplemental roster of §10.5.
2. Attestation rehearsal of §10.6 from a clean committed tree into an external empty directory, then `--verify`; expected to pass once §5.11 is in place (rehearsed, §10.6). A failure is a finding to record, never something to patch around.
3. Proof: every command exit 0; clean tree after every isolated run.

### C6 — Publication (PR-30's `PR_CANDIDATE_PUBLISHED`)

1. One meaningful commit series on the working branch; PR description per `.github/pull_request_template.md` and `AGENTS.md` with the §15 merge statement; the `PR_IMPLEMENTATION_RESULT` under `docs/ephemeral/` naming every command run and its exit code, the before/after digests, the `release_id`, the attestation outcome, and what was not executed.
2. Hand off to PR-35 in its own dedicated session. PR-35 owns review correction, current-head CI, coherent corrective pushes and `MERGE_PENDING`; Nathan merges.

Recovery at any checkpoint: revert the compatible set together (code, config, schema bytes, generated artifacts, manifest, tests) with `git checkout -- .` / `git restore` on the branch; re-run the owners on unchanged inputs; if a source byte changed, restart at C1 step 4.

## 10. Local validation and evidence commands

### 10.1 Environment (exactly as `.github/workflows/ci.yml` installs, plus what the rehearsal needed)

```
python --version                      # CI: 3.12 (actions/setup-python); local rehearsal used 3.11.15
python -m pip install -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version            # readiness proof (AGENTS.md)
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
```

Two environment facts from the rehearsal that PR-30 must check before the attestation rehearsal: (a) a Debian/Ubuntu system `setuptools` (68.1.2 under `/usr/lib/python3/dist-packages`) makes `pip wheel --no-build-isolation` fail with `AttributeError: install_layout`; `python -m pip install --ignore-installed "setuptools>=75" "wheel>=0.43"` (or a venv) fixes it and the wheel `glow_hdengine-0.0.0-py3-none-any.whl` then builds; (b) the scripts the attestation runs inside its isolated copy import `engine` from the *installed* location (the editable install), so the editable install must point at the tree being attested (`pip install -e <that tree>`); in CI that is the candidate checkout itself.

### 10.2 Focused behavioral and ownership suites

```
python -m pytest -q -p no:cacheprovider tests/scripts/test_cut_release_manifest.py tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/config/test_manifest_schema.py tests/config/test_config_artifacts.py tests/config/test_registry_catalog_contract.py tests/runtime/test_identity.py tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_open_rails_abba_proof.py tests/transport/test_a7_transport_proofs.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_showcompat_sources.py tests/cli/test_showcompat_parity_and_identity.py tests/http/test_compat_endpoint_contract.py tests/evidence/test_rails_ci_workflow_integration.py
```

### 10.3 Classifier dry-run and changed-test isolation (as `ci.yml` runs them)

```
python ci/checks/classify_ci_changes.py --base origin/main --head HEAD --event-name pull_request --github-output /tmp/gh_out.txt --changed-tests-output /tmp/changed_tests.txt
# expect every lane true (classifier change ⇒ full validation) and no CI_CHANGE_SURFACE_UNCLASSIFIED
git worktree add --detach /tmp/pr06-changed-tests HEAD && (cd /tmp/pr06-changed-tests && PYTHONPATH=$PWD python -m pytest -q -p no:cacheprovider -- $(cat /tmp/changed_tests.txt) && git diff --exit-code && test -z "$(git status --short --untracked-files=all)")
```

### 10.4 Lane-equivalent validation (commands verbatim from `.github/workflows/ci.yml`, in lane order)

product: `python tools/order/generate_ordering_artifacts.py --check`; `python -m pytest -q tests/order tests/mech/test_order_properties.py tests/evidence/test_architecture_snapshot.py`.
compat: `ci/checks/check_cli_help.sh`; `python tools/cli/serializer_grep_guard.py --output <tmp>/serializer_grep_guard.log`; `python tools/cli/emitter_symbol_proof.py --output <tmp>/emitter_symbol_proof.txt`; the compat pytest set of the workflow.
db: `python ci/checks/check_direct_db_contract.py`; the db pytest set.
rails: `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` (must exit 0, never 3); `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`.
evidence: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/refresh_step_logs_manifest.py --check`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh` (a Python script with a `.sh` name: execute it directly or via `python`, not `bash`); `ci/checks/check_final_lf.sh`; the evidence pytest set.
qa: the qa pytest set in a detached worktree with a clean-tree assertion.
release: `git diff --exit-code`; `python scripts/release_id_recompute.py --check-manifest-only`; the release pytest set in a detached worktree; then §10.6.

### 10.5 Candidate-wide roster

`_FULL_VALIDATION_SUPPLEMENTAL_TESTS` from `ci/checks/classify_ci_changes.py` (the 40-path list), plus the evidence-family suites `tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_release_bindings.py tests/scripts tests/core/test_engine_core_purity.py tests/unit/test_narratives_loader.py tests/unit/test_narratives_router.py tests/evidence/test_internal_version_manifest_captures.py tests/evidence/test_http_reader_ci_ownership.py`. Do not run bare `pytest tests`: it collects legacy `core.*`/`adapters.*` modules that fail at import (14 collection errors on the baseline) and proves nothing.

### 10.6 Attestation rehearsal and the recorded planning outcome

Command (from a clean committed tree, external empty destination):

```
python tools/evidence/build_release_attestation.py --output "$RUNNER_TEMP/hde-release-attestation" --require-clean
python tools/evidence/build_release_attestation.py --verify "$RUNNER_TEMP/hde-release-attestation" --require-clean
git diff --exit-code && test -z "$(git status --short --untracked-files=all)"
```

Planning rehearsal record (scratch clone; inference support only):

| Attempt | Outcome | Cause | Standing |
| --- | --- | --- | --- |
| 1 | `isolated_package_install_failed` at `build_package_wheel` | Debian system `setuptools` (`AttributeError: install_layout`) | environment; fixed by §10.1 (a) |
| 2 | `release_not_admitted` at `closure_write_and_check` | isolated scripts imported `engine` from the editable install pointing at the real (unadmitted) repository | environment; fixed by §10.1 (b) |
| 3 | `isolated_stage_failed` (exit 1) at `closure_write_and_check` (v1.0) | reproduced step by step in the isolated sequence: `release_id_recompute.py` regenerated `artifacts/math/*`; `identity_provenance` regenerated `artifacts/identity/service_identity.json`, `release_id.json`, `release_id_recompute.log`, `artifacts/parity/two_run_identity.log`; `release_bindings` regenerated; then `run_canonical_json_gate.py` (write) failed with `runtime_identity_source_mismatch` on `artifacts/cli/ab.json`, `ba.json`, `showcompat/args.json`, `showcompat/stdout.json`, `summary.json` — the gate binds those frozen captures to `service_identity.json`, which the closure had just rewritten | **material finding HDE-EPIC040-PR06-F01 (§14)** |
| 4 | same five failures on the untouched baseline `190527cf…` with the F01 guard bypassed in the scratch clone only (`service_identity.json` regenerated to `a5f06ae3…`) (v1.0) | the defect predates PR06: it exists on every tree whose manifest identity differs from the frozen `12523fec…`, and has been masked since PR04 by the `release_not_admitted` receipt | confirmed F01 as pre-existing and decisive; decided by the review |
| 5 (v1.1) | build exit 0; `--verify` exit 0; `attestation.json` SHA-256 `3a35ac09380655320548a6fd4bc89fe5ba5ee475d6c383ea3818578b06b87e2b`; `release_admission: PR06R_B_FINAL_PASS`; `validation_result: PASS`; `release_id 988ed2a7…`; stages `build_packaged_wheel`, `install_packaged_console_entrypoint`, `closure_write_and_check`, `closure_fixed_point_check`, `release_sanity` all exit 0 (26-line transcript); 174 files bound; 14 declared outputs recorded under `omitted_files` with the builder's existing secret-safety reason codes (`UNREDACTED_BIRTH_INPUT_VALUE` for the showcompat captures, `UNREDACTED_BEARER_VALUE` for Index/Mirror, `UNREDACTED_CREDENTIAL_VALUE` for the env-matrix snapshot, `PRIMARY_OMITTED_SECRET_SAFETY` for their companions) — the same validator flags the same files on the baseline, so this is pre-existing builder behaviour, not an effect of PR06 (O-P06-15) | scratch clone at the PASS fixed point plus the §5.11 gate change; §10.1 environment fixes applied; interval tests deselected in the clone only | CC-6 achievable; the real-branch run is PR-30's |
| 6 (v1.1) | step-wise emulation of the isolated closure in a fresh clone of that state: `regenerate_identity_closure.py --in-place-isolated` exit 0 (22 files regenerated in the copy: the identity family, `artifacts/math/*`, `release_bindings.json`, the gate outputs and their proofs, Index/Mirror), `--check` exit 0, `run_sanity_pipeline_gate.py` exit 0 with `summary:PASS` | same clone family | confirms the closure reaches a fixed point once the gate reads the capture-time identity |

Consequently CC-6 is no longer blocked at planning time: the approved delta lets the closure run and the attestation pass on an admitted candidate. The attestation on the real candidate remains `NOT EXECUTED` until PR-30 runs it (C5).

### 10.7 Result record

PR-30 writes `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-result-v1.0.md` with: every command of §§10.2–10.6 and its exit code; the F-03 before/after digests; the manifest bytes/`release_id`; the golden report digest; the sanity log model and its binding; the attestation bundle digest (or its failure receipt); the classifier outputs; not-executed items with reasons; and the same distinctions (verified / inferred / not produced / not executed) this plan uses.

## 11. Code review and security review checklist

### 11.1 Code review (PR-session, on the current substantive change)

- Cutter: roster path handled once each; extras refused; self-listing refused; member format validated before hashing over the exact bytes; no normalization; `check` writes nothing; CLI tokens on stderr; existing tests untouched in meaning.
- Source finalization: the three members are content-identical to before (parsed equality recorded); the token-map owner's other outputs are byte-identical; the sidecar format unchanged.
- Gate: the manifest-roster constant, one import and the §5.11 identity source changed; 26 targets and six set rules unchanged; the module no longer reads `artifacts/identity/service_identity.json`; the identity is read only after the frozen digest verifies; the four sources must agree; `summary.json` still compares against the agreed identity; nothing is evaluated at import time.
- Comparator: predicate is read-only; refuses before `ok: true`; fixture and real-root cases both covered; no `sys.modules` mutation; no import of candidate files.
- Config publication: admission gate precedes any write; `--check`/write on partial roots unchanged; registry report never binds `release_id`.
- Evidence: every changed governed artifact has an owner command in the result record; no hand edits (`git log -p` on evidence paths shows only owner-produced diffs); Index/Mirror/path proofs/orientation converge under `--check`.
- Tests: no skip/xfail/deselect; every F01 branch still exercised via patched providers; the 22 rewrites assert the admitted posture.
- Classifier: three registrations, no other table changed; classifier coherence tests green.
- Narrative mount: tracked mount byte-identical to `catalog/narratives/`; stale mount removed; loader untouched.
- Nothing under `docs/pfcanon/`, `engine/`, `.github/workflows/` changed; no schema or wire-value change.

### 11.2 Security review (corrected code)

- Path safety in the cutter (absolute, `..`, backslash, symlink, escaping roots) for roster-derived rows as for existing rows.
- The comparator reads only `module.__file__` of already-loaded modules; it never imports or executes candidate bytes; refusal messages carry paths only, never contents.
- `--publish-family` cannot be driven by `HDE_CONFIG_ROOT` or an alias to publish from a non-admitted root; the admission owner is called without parameters.
- No secrets, birth or Gate payloads in any regenerated evidence (`validate_retained_text_safety` runs inside the attestation; the sanity stage 06 keys-only redaction job runs in the rails lane).
- The tracked narrative mount contains only the catalog pack copies; no user data.
- Attestation output only to an external empty directory; nothing written inside the repository by the builder.

## 12. Risk register and recovery

| ID | Risk | Treatment |
| --- | --- | --- |
| R-01 | A source byte of a roster member changes after the cut (for example a review correction) | any member change ⇒ re-cut (C1 step 4) and restart convergence at §5.7 step 4; the cutter `--check` and `check_manifest_only` in the release lane catch a stale cut |
| R-02 | The gate rebind is read as extending the fixed 26-target roster | §8.4 pins 26 targets and 6 set rules and refuses 43/45-member manifests; §5.3 records the boundary |
| R-03 | `--publish-family` refuses `CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT` | ordering of §5.7 (full updater before publication); never bypass the guard |
| R-04 | Sanity transition does not converge | §5.8 procedure; the non-canonical run first; the owner rewrites FAIL on any failure |
| R-05 | Untracked residue from live evaluations | tracked mount (§5.9); `git status --untracked-files=all` after every producer |
| R-06 | CI Python 3.12 vs local 3.11 | lane-equivalent runs are evidence of behaviour, not of CI; CI on the exact head remains the record |
| R-07 | Local attestation rehearsal blocked by packaging environment | §10.1 (a)–(b); record the environment in the result |
| R-08 | Interval-test rewrites weaken coverage of the F01 branches | every `not_admitted` branch keeps a patched-provider test; review item |
| R-09 | Comparator binding false refusals (`__file__` missing, `.pyc`-only modules) | refuse `CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE` rather than pass; test with a module whose `__file__` is deleted |
| R-10 | §5.11 drifts from PF10 §2.21's conditions (identity read before the digest verifies, a regenerated file consulted, the check weakened) | §8.7 proves each condition; §11.1 review items; the addendum's exclusions are the review checklist's boundary |
| R-11 | A later narrative pack change makes the tracked mount stale | the loader verifies bytes per pack SHA and writes a new mount directory; the stale one is dead; recorded for the loader owner (§13.2) |
| R-12 | Wrong lane registration in the classifier | classifier coherence tests and the dry-run of §10.3; full validation on this candidate regardless |
| R-13 | PR07's F03/F05 fixes change `schemas/reader.v1.schema.json`, `adapter/http_reader.py`, `presenter/reader_v1/emitter.py` | PR07 re-cuts and re-converges (instruction §8); PR06 does not pre-empt it |
| R-14 | Gate tests that copy only part of the tree, or forge a source capture on disk, now refuse first with `frozen_capture_identity_source_unverified` (two existing conjunction forgery tests; rehearsed) | such tests copy or symlink the four unforged source captures (the existing metadata-only-cut test already symlinks `artifacts/`) and forge presented payloads; never widen the identity source or bypass the digest (§8.7) |

Recovery: roll back the compatible set together on the branch; re-run owners on unchanged inputs; re-cut on source change; on convergence failure claim nothing and hand-edit nothing (instruction §11).

## 13. Carried `CANON_CONFLICT_REGISTER` and observations

### 13.1 `CANON_CONFLICT_REGISTER` (carried unchanged from Plan v2.1 §11, Plan Review v2.1 §6, PF10 §§2.2–2.5, 2.19, 2.20 and the instruction §12; no entry reopened, relabeled, omitted or newly decided; PR06 opens none)

| Entry | Classification / status | Decision lineage | PR06 note |
| --- | --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z (PF10 §2.2) | carried |
| C040-02 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | current controlled PF12 is repository v2.9.5; used as such (§2.2) |
| C040-03 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-04 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-05 | `CANON_RECONCILIATION` / `APPROVED`, alternative A | Isis-49, 2026-09-09T03:57:16Z (PF10 §2.3) | one four-argument core; no legacy success path; PF14 §6.7 permanent correction pending, non-gating |
| C040-06 | `NEW_CANON` / `APPROVED`, alternative A | Isis-50, 2026-09-09T11:48:08Z (PF10 §2.5) | 36-row taxonomy conformance-only; PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |

Neither `HDE-EPIC040-PR04-F01` (PF10 §2.15) nor `HDE-EPIC040-PR06-F01` (§14) is a register entry. The O-01 token-naming tension remains with the PF01/PF05 maintainers.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner |
| --- | --- | --- |
| O-P06-01 | (v1.0) `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md` sat beside v13.3.1 (instruction O-P06-01); superseded by O-P06-14 now that v13.3.2 is current | Nathan |
| O-P06-02 | O-07's transition recipe covers PASS → NOT_ADMITTED; the reverse needs the Mirror to pre-bind the PASS model (§5.8, F-08) | sanity pipeline / updater owners |
| O-P06-03 | O-18 production failure mode (request-path mount on a read-only cold worker; concurrent cold workers) remains; the tracked mount mitigates only a working-directory deployment from this tree | narrative loader owner (Product Owner if a loader change is wanted; §9 route) |
| O-P06-04 | O-12: the admitted roster is not shipped in wheels; the attestation's packaged console runs only `--help`/`--version` | packaging owner / Product Owner |
| O-P06-05 | L-10-type limitation: no current-head security review for PR04 or PR05 | Product Owner |
| O-P06-06 | O-16 / O-01 token-naming tension | PF01 / PF05 maintainers |
| O-P06-07 | O-09/O-20/O-21: showcompat and CLI-conformance write modes refuse on the admitted root (`ERR_M10_LEGACY_INPUT_UNSUPPORTED`; `DB_QUERY_FAILED` — birth-only inputs need a stored BodyGraph source); `scripts/cli/canonical_harness.py` is referenced by no lane; the captures stay frozen; a regeneration is a capture-source/identity decision (folded into F01 alternative B) | Product Owner / capture-generator owner |
| O-P06-08 | On the baseline, `generate_identity_provenance.py --check` (`RELEASE_ID_STATE_INVALID:freeze_pack_manifest_not_equal,release_id_mismatch`), `release_id_recompute.py --check` (STALE, eight `artifacts/math/*` files) and `generate_release_bindings.py --check` (DRIFT) already fail: the frozen identity family carries `12523fec…` while the manifest identity is `a5f06ae3…`; not a sanity stage (stage 02 uses `--check-manifest-only`), but the reason the isolated closure regenerates them (F01) | release-identity evidence owners |
| O-P06-09 | The stale tracked mount `narratives/64e17c9c…/` entered with the loader in `1180d94` (#447) and was never read | narrative loader owner (removed by D-08) |
| O-P06-10 | Scripts executed inside the attestation's isolated copy import `engine` from the installed location, not from the copy (`regenerate_identity_closure.py` does not insert its own root into `sys.path`); the same "executing installation vs candidate bytes" theme as O-17/CR-06, at the attestation level | attestation owner |
| O-P06-11 | PR07's F03/F05 fixes will change manifest members and therefore `release_id`; PR07 must re-cut and re-converge (instruction §8) | PR07 |
| O-P06-12 | `ci/checks/check_mirror_schema.sh` and `ci/checks/check_release_identity.sh` are Python scripts with `.sh` names (python3 shebang); invoking them with `bash` fails spuriously | CI owner (cosmetic) |
| O-P06-13 | Condition 7 (honest attestation content) is met without a builder change: the payload binds files by digest and carries fixed `nonclaims`; it describes no capture provenance. A builder-level nonclaim naming the frozen capture families would make the bundle self-describing; outside the approved loci, so not planned | attestation owner |
| O-P06-14 | Three PF10 files are present (`v13.3`, `v13.3.1`, `v13.3.2`); the two older base versions are not read under PF10 §6 | Nathan |
| O-P06-15 | The builder's secret-safety validator omits 14 declared outputs from the external bundle, on the baseline and after PR06 alike (showcompat captures `UNREDACTED_BIRTH_INPUT_VALUE`; Index/Mirror `UNREDACTED_BEARER_VALUE`; env-matrix snapshot `UNREDACTED_CREDENTIAL_VALUE`; their companions `PRIMARY_OMITTED_SECRET_SAFETY`), recording them under `omitted_files` with reason codes; whether the Index/Mirror should be carried in the bundle is the attestation owner's question, not PR06's | attestation owner |

## 14. Boundary finding resolved, planning decisions and boundary classification

### 14.1 `FINDING_REF: HDE-EPIC040-PR06-F01` — decided; the approved overlay is planned in §5.11

Plan v1.0 §14.1 recorded the finding: inside the isolated closure the identity family is regenerated to the current `release_id` while `tools/evidence/run_canonical_json_gate.py` bound the frozen CLI captures to `artifacts/identity/service_identity.json`, so the attestation failed on every tree whose manifest identity had moved (reproduced on the rehearsed admitted tree and on the untouched baseline). The finding's substantiation, cause and alternatives stand as written there and are not repeated.

| Item | State |
| --- | --- |
| Decision | `HDE-EPIC040-PR06-F01-RESCOPE-REVIEW` v1.0, `APPROVE`, alternative A, a bounded implementation rescope with seven binding conditions (§4); decided by the retained whole-change IA by Product Owner direction of 2026-09-25 ("The rescoping analysis is yours. It must go back to the PR session that authored it, whether approved or denied."); `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md`, SHA-256 `7264ed3f661de42f9c2ad40449d77e8d2a31a2edc2775a10c915074d1b246d05` |
| Overlay | `docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md` (SHA-256 `c5154465a1bdebda8f217ca7d320c0ec75bc74b37521931cbca4417d1b0d2b03`), published by Nathan as PF10 §2.21 in `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.2.md` (#500); the drained body matches the addendum |
| Delta | PR06's loci extended by exactly `tools/evidence/run_canonical_json_gate.py` and its existing test home; `_CAPTURE_IDENTITY_META` derived from the frozen captures' own digest-verified capture-time identity, never from a regenerated file |
| Classification | bounded implementation rescope; not material in the PR-10 sense; not a Specification change; not a defect in PR01–PR05 |
| Alternative B | not chosen; remains available to PR07 / the Product Owner (re-identifying the captures is a capture-contract decision) |
| Alternative C | rejected (contradicts PF12 §6.2.1 and `AGENTS.md`) |
| Where planned | §5.11 (design bound to conditions 1–7), §6.1 (locus), §8.7 (tests for the pass case and every refusal case), §9 C3 (order), §10.6 (rehearsal record) |
| Route closed | no RS-10 proposal session was created (the finding record was the proposal of record); no `PR_RETURN_PHASE`; RS-40 does not apply; this v1.1 is the complete successor the review §7 asked for |

No further boundary finding is open. §3.3 and §10.6 record the rehearsal of the approved delta in a scratch clone; CC-6 is no longer blocked at planning time.

### 14.2 Planning decisions (D-xx) and their boundary classification

| ID | Decision | Classification |
| --- | --- | --- |
| D-01 | The 44-member `ADMITTED_RELEASE_ROSTER`, `1.1.0` and `2026-08-24T18:04:49Z` are the cut inputs; Plan §5.10's 15 + 31 description yields to the roster (instruction §3) | in scope |
| D-02 | Source finalization of the three non-canonical members through their owners/canonical form; the token-map owner's writer becomes canonical for that output only | coherence dependent (Plan §6.6 inputs); not material |
| D-03 | Gate manifest-roster constant rebound to the roster; 26 targets untouched | coherence dependent; not material |
| D-04 | `registry_loader.py` untouched; the cutter reuses the admission owner's private member-format helper as the gate already does | in scope |
| D-05 | O-17/CR-06 bounded treatment is the comparator-side executed-member source binding; no §2.12 widening | in scope; limitation recorded |
| D-06 | `--publish-family` gated on real admission and same-capture equality; partial-root local APIs unchanged | in scope |
| D-07 | The 22 interval-pinned tests, including those in CLI/HTTP/transport homes, are rewritten to the admitted posture with F01 branches kept under patched providers | coherence with instruction §5.4; not material (no gate semantics change) |
| D-08 | O-18 settled by tracking the loader-produced mount and removing the stale one; loader untouched; production mode recorded with its owner | coherence dependent; not material; loader-side alternative is a §9 route if wanted |
| D-09 | Sanity PASS transition through the owner's renderer, the sole updater and the canonical run (§5.8) | in scope; O-P06-02 recorded |
| D-10 | One PR, ordered commits C1–C6, no split; PR07 depends on PR06 landing | in scope |
| D-11 | `HDE-EPIC040-PR06-F01` was material to PR06's completion and was routed; the approved alternative A is now planned as §5.11 under PF10 §2.21, exactly within the two-item loci extension | approved overlay (RS-20 `APPROVE`); in scope for v1.1 |
| D-12 | The identity-source roster is the four captures that hold a digest in `_FROZEN_GENERATED_SHA256`; `summary.json` is a consumer, not a source, and no digest is added for it | in scope under §2.21 (no digest, capture or generator change) |
| D-13 | Condition 7 (honest attestation content) is met by the builder's existing digest-only file binding and `nonclaims` plus an explicit statement in the result artifact; the builder is not changed (outside the loci) | in scope; recorded as O-P06-13 for the attestation owner |

No decision here rewrites the Plan, mints a Proceed, reruns an accepted unit, edits PF-Canon or merges.

## 15. Manual merge and post-implementation boundary

- Merge is Nathan's alone. PR-30 ends at `PR_CANDIDATE_PUBLISHED`; PR-35 ends at `MERGE_PENDING — Ready to merge`; PR-40 runs after `MERGE_OBSERVED` (or Nathan's assertion where no such result exists) with the retained IA in its read-only role.
- Merging PR06 makes the complete admitted release, the converged evidence and the ended F01 interval current on `main`. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, deployment, activation, Epic closure. The PR description states this under "What merging does", following `.github/pull_request_template.md` and `AGENTS.md` (Why / What changed / Checks run / Not in this PR / What merging does).
- Merge-order dependency: none upstream (PR05 landed); PR07 must follow PR06.

## 16. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-20-20260925-PR06-02` (this v1.1 re-entry); prior entries carried: `GCFPE-USE-HDE-EPIC040-PR-20-20260925-PR06-01` (v1.0), `GCFPE-USE-HDE-EPIC040-PR-10-20260925-PR06-01` (instruction), `GCFPE-USE-HDE-EPIC040-RS-20-20260925-PR06-F01-01` (review).

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204` (body as read during the v1.0 invocation of this session; re-entered by handoff for v1.1; Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06; Specification v1.1; instruction v1.0.
- Role / stage: dedicated PR06 PR-development session / PR-20 (re-entry after the RS-20 decision).
- Captured: 2026-09-25T14:20:13Z (v1.0 entry captured 2026-09-25T10:08:45Z).
- Execution identity: harness session `https://claude.ai/code/session_01S3w2LDoDhi5GKMfuLRKkdx`.
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.
- The v1.0 entry's fields are carried unchanged in the v1.0 file.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

- Receiver: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`; the same dedicated PR06 session (`RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06 / PR-30`; `context_conflict: NONE`).
- Gate: Nathan / Product Owner's manual PR-30 Proceed for exactly `HDE-EPIC040-PR06-PR-IMPLEMENTATION-PLAN` v1.1 and `HDE-EPIC040-PR06-PR-INSTRUCTION` v1.0. `AWAITING_PO_PROCEED` is not implementation approval and authorizes no merge, publication, Ops or QA.
- Inputs by repository path: this plan (`docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.1.md`); `docs/ephemeral/HDE-EPIC040-PR06-pr-instruction-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md` (binding conditions §4); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.2.md` (§§2.12, 2.15, 2.21); the immutable bases of §2.1.
- PR-30 obligations carried: inspect authorized local roots, repository state, existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06 before creating anything (none exist at planning time; the PR-20 storage branch `claude/gallant-wright-2f83bd` holds only planning documents and is not a PR06 implementation vehicle); resume the most advanced consistent state; challenge assumptions and the boundary cases of §8; implement only §§5–6 in the order of §9; test locally per §10, including the attestation rehearsal; form one coherent meaningful checkpoint; deliberately publish the initial candidate; `PR_CANDIDATE_PUBLISHED`; hand off to PR-35 in its own dedicated session naming the `PR_IMPLEMENTATION_RESULT` and the PR reference.
- PR-35 obligations carried: review retrieval and correction, local retesting, coherent corrective pushes, CI economy, current-head identity, required checks or a valid waiver, mergeability, genuine merge readiness; no merge. Nathan merges; PR-40 follows `MERGE_OBSERVED`.

### 17.2 Closed route

The v1.0 RS-10 package is closed: the finding was decided under Product Owner direction by the retained whole-change IA without an RS-10 session (review §1), the overlay is drained as PF10 §2.21, and no `PR_RETURN_PHASE` or RS-40 applies.

### 17.3 State summary (truthful states)

| Item | State |
| --- | --- |
| This plan | `AWAITING_PO_PROCEED` — complete, executable within approved scope plus PF10 §2.21; pending the Product Owner's PR-30 invocation for v1.1 |
| `HDE-EPIC040-PR06-F01` | decided (`APPROVE`, alternative A); drained (PF10 §2.21); planned (§5.11) |
| PR06 implementation, PR, CI, merge | `NOT EXECUTED` |
| PR06 result artifact, PR07, OPS01, QA, Ops, activation, closure | `NOT PRODUCED` / `NOT EXECUTED` |
| Attestation on the real candidate | `NOT EXECUTED` (rehearsed in a scratch clone only, §10.6) |
| Provenance persistence | `PENDING / NON_GATING` |
