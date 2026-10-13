---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-02-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: REJECT
predecessor: none (first lineage review of WU-PR-02)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5; Proceeded; spent by this REJECT), with its companion docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff (blob 242eff5f7c8e)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md (v1.0, PR_CANDIDATE_PUBLISHED; blob 5942994df870)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.4.md (v1.4, MERGE_PENDING; historical pre-merge evidence; blob 934b7f415bb2); PR-35 checkpoints v1.1 (blob 8c002e3e20bf), v1.2 (blob f722b4d3f1dd), v1.3 (blob 320fa002afa8)
PR_REFS: amthorn78/glow-hdengine-v2#634 (merged as 1d2c8345483dc1d143a3a4b32a57dcc34a6e2479)
entry_event: MERGE_OBSERVED for #634, delivered by the PR-35 session in the pasted handoff (no saved MERGE_OBSERVED artifact; NOT PRODUCED); merge verified independently (§3)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role (instruction v1.0 §12); session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
pr_sessions: PR-20 and PR-30 https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a; PR-35 https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain); addendum 2.1 governs §12's TypeSafe reading
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-13T21:38:18Z
repository_state_reviewed: origin/main 1d2c8345483dc1d143a3a4b32a57dcc34a6e2479 (tree b38adac61a49); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112d; unchanged since cc3dc33; addenda 2.1, 2.2, 2.3, 2.4)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); no new entry
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba), corrective plan for WU-PR-02
---

# HDE-CRD-0002 WU-PR-02 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**REJECT on LR-1.** #634 landed a test regression on `main`:
- `tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` passes at the PR base `0cd7b84` and fails at PR-30's head `c27c5e8` and at the merge commit `1d2c834`.
- The cause is the unit's own change to `tools/evidence/update_evidence_index.py`: `_load_human_index()` now always derives the release label, which requires a fully valid `catalog/manifest.json` under the updater's `ROOT`. The test points `ROOT` at a temporary directory that has no manifest, so the updater exits `CURRENT_RELEASE_LABEL_MANIFEST_INVALID`.
- No CI run of #634 selected that test: the classifier ties it to `adapter/factory.py`, `adapter/wsgi.py` and the two HDAPI v2 contract-inventory tools, not to the updater. WU-PR-03's first deliverable changes `adapter/factory.py`, so WU-PR-03's CI would run the test and fail on a defect that WU-PR-02 caused.

Everything else in the unit holds. S06, S11, S12, S13 and S22 are delivered as their acceptance items require, and this review re-established each from repository evidence (§5, §6). The four review findings were resolved: CX-1, CX-3 and CX-4 were corrected, and CX-2 is a residual accepted by the Product Owner. The merge is a clean squash of the reviewed head.

The landed #634 stays on `main`; nothing is reverted. The correction is bounded (§8) and goes through a new per-PR plan for the same work unit (PR-20), a new Proceed, PR-30, PR-35 and PR-40. The earlier Proceed is spent.

REJECT is this review's lineage result only. It is not QA, acceptance, Ops, PF09/PF30 movement, release activation, merge authority or closure.

## 2. Inputs read

Read in full: the PR-40 prompt; PR instruction v1.0; detailed plan v1.0 and its prototype diff header; results v1.0 to v1.4; Implementation Plan v1.1 §4, §7 (common paragraph, WU-PR-02 and WU-PR-03 blocks), §10, §11, §13; the Specification requirement rows S03, S06, S11, S12, S13, S22; Audit §5.6 and §6 S13; PF10 v13.5.5 addenda 2.3 and 2.4 (2.1 and 2.2 as cited); the canon sections in "Canon relied on". GitHub: #634 metadata, its 9 commits, its 7 formal reviews, 4 review threads, the Codex summary comment, the check runs on the final head and the post-merge push run.

## 3. Merge state and landed lineage

| Fact | Evidence |
| :- | :- |
| #634 merged | GitHub: `merged=true`, `merged_by amthorn78`, `merged_at 2026-10-13T20:57:34Z`, base `0cd7b843462df94273bb686def5e4a353d0b98ba`, head `d0c81aea9c18fafdaf51168661308d7ef537b689`, 9 commits, 20 files, +1,676 / −78 |
| Method | SQUASH. `1d2c834` has one parent, `0cd7b84`; `1d2c834^{tree}` = `d0c81ae^{tree}` = `b38adac61a49e61611ac8729390ca0e5c70ac3d5`; `0cd7b84` is an ancestor of `d0c81ae` |
| Commit order on the PR | `c27c5e8` (PR-30 implementation) → `4d11089` (result v1.0) → `c0ca923` (CX-1) → `b6fe37d` (v1.1) → `489bc17` (CX-3) → `e7ec65f` (v1.2) → `a028b0c` (CX-4) → `433c1a5` (v1.3) → `d0c81ae` (v1.4) |
| Later divergence | none: `origin/main` = `1d2c834` |
| Attributable landed delta | 20 paths: `tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/update_evidence_index.py`, `ci/checks/check_mirror_schema.sh`; `tests/evidence/test_release_attestation.py`, `test_engine_core_evidence.py`, `test_evidence_index_missing_state.py`; the eight governed Index/Mirror companions; results v1.0 to v1.4. Every path is one that instruction §6 and plan §6 bound. No release member, no `catalog/` file, no `docs/pfcanon/` file, no `orientation_demo.txt` change |

**Merged-change attribution** (skill `glow-merged-change-attribution-lock` 1.2.0, interface GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3, SHADOW_VALIDATION):
- Run: LOCAL_GIT on the repository checkout at `1d2c834`, comparison SHA `1d2c8345483dc1d143a3a4b32a57dcc34a6e2479`.
- Result: change `amthorn78/glow-hdengine-v2#634`, method SQUASH, reconciliation **EXACT** (direct and landed delta SHA-256 `5420e377…c6e8`).
- Divergence: no later committed divergence (`1d2c834..1d2c834` is empty) and no worktree divergence (staged, unstaged and untracked all empty).
- Validation: read-only invariant PASS. The validator returned `VALIDATED` (exit 0) for the in-flight artifact, whose evidence manifest SHA-256 is `81b23b35…d24d`.
- Shadow comparison: the native reading above matches; no discrepancy. The transient artifact is discarded after this review, as the skill directs.

## 4. Reviews, checks and corrected-change coverage

**Codex code review** (the chain under PF10 addendum 2.3; the Codex security review is not part of it and its absence is not a gap):

| ID | Head | Finding | Disposition | Thread |
| :- | :- | :- | :- | :- |
| CX-1 | `c27c5e8` | P1 "Verify captures before relabeling them as current" | corrected by `c0ca923`: a label moves only for a capture whose bytes differ from the Mirror's recorded `sha256`, or on first adoption; incoherent labels are refused | `PRRT_kwDOP103ks6sAH60` resolved |
| CX-2 | `b6fe37d` | P1 "Require producer proof before advancing capture labels" | accepted residual by the Product Owner's decision (result v1.2 §3.1); no code change; recorded for this review (§7 LR-O1) | `PRRT_kwDOP103ks6sA712` resolved |
| CX-3 | `b6fe37d` | P2 "Validate the manifest before minting a release label" | corrected by `489bc17`: `manifest_only_problems` runs before any label; else `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` | `PRRT_kwDOP103ks6sA719` resolved |
| CX-4 | `e7ec65f` | P2 "Detect setuptools using the wheel child's environment" | corrected by `a028b0c`: the layout probe runs with `sys.executable` in the wheel child's cleaned environment and directory | `PRRT_kwDOP103ks6sCFjw` resolved |
| — | `433c1a5`, `d0c81ae` | none | Codex summary (issue comment 6152304678) "Code Review Completed 2026-10-13T20:22:58Z" on `d0c81ae`, trigger "New commits"; the last Codex review with findings is 5509067586 on `e7ec65f` | 4 of 4 resolved |

Corrected-change coverage: each correction carries a test that fails against the head Codex reviewed and passes after (results v1.1 §4, v1.2 §5, v1.3 §3 and §4). This review read each correction's code in the landed diff (§6).

**Hosted CI:**

| Run / job | Head | Result |
| :- | :- | :- |
| 38446041858 / 115465311140 | `4d11089` | success; superseded (CX-1) |
| 38450463942 / 115479729750 | `b6fe37d` | success; superseded (CX-3) |
| 38456991751 / 115502168686 | `e7ec65f` | success; superseded (CX-4) |
| 38460145263 / 115512888315 | `433c1a5` | success; EVIDENCE and RELEASE lanes; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| **38462001207 / 115519275047** | **`d0c81ae` (final head; its tree is the merged tree)** | **success 20:20:15Z–20:30:46Z; the job log shows CHANGED_TESTS, EVIDENCE and RELEASE success, PRODUCT, COMPAT, DB, RAILS and QA skipped as classified, and prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK`** |
| 38466922360 / 115535985530 | `1d2c834` (push to `main`) | success 20:57:40Z–21:10:33Z |

No waiver exists or was needed. Green CI here does not cover LR-1: no classified lane ran the regressed test.

## 5. Independent verification by this review

All runs used closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), with vendor, geocode, database and `GH_TOKEN` variables unset. They ran in a scratch clone and its detached worktrees, never in the repository checkout. Two environments:
- **E-CI:** CPython 3.12.3 with CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <clone>`). Readiness: `pip install -r requirements-dev.txt` exit 0, then `python -m pytest --version` → `pytest 8.4.2`.
- **E-DEB:** `/usr/bin/python3 -m venv --system-site-packages`, CPython 3.13.16. setuptools 68.1.2 comes from `/usr/lib/python3/dist-packages` (Ubuntu `python3-setuptools` 68.1.2-2ubuntu1.2; `install_layout` appears in its `command/install_lib.py`). Repository requirements are installed, with no `-e .`. Neither `_distutils_system_mod` nor `engine` is importable.

Runs started at 2026-10-13T21:04:29Z.

| Check | Commit | Result |
| :- | :- | :- |
| Classifier, `pull_request` and `push`, base `0cd7b84` | `1d2c834` | exit 0 both; `lanes=evidence,release`; `changed_tests=true`; `path_count=20`; targets `tests/config/test_config_artifacts.py`, `tests/evidence/test_aux_preview_identity_parity.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_internal_version_manifest_captures.py` |
| `check_env_pins.sh`; `check_agents_md_citations.py` | `1d2c834` | 0; 0 |
| `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, `check_lf_endings.py`, `release_id_recompute.py --check-manifest-only` | `1d2c834` | all 0 |
| Updater written twice in a detached worktree | `1d2c834` | 0, 0; `git diff --exit-code` 0 after each; status empty (fixed point) |
| Changed-test step (detached worktree, `PYTHONPATH` = worktree) | `1d2c834` | **198 passed**; tree clean |
| Evidence lane test set (six `ci.yml` files) | `1d2c834` | **130 passed** (807.0 s) |
| `tests/config/test_config_artifacts.py`, `tests/evidence/test_engine_core_evidence.py` | `1d2c834` | **165 passed** (176.2 s); clone clean (`git diff` 0, status empty) |
| Release-lane tests (four files, detached worktree) | `1d2c834` | **79 passed**; tree clean |
| Release-lane build, E-CI, from the clone (`--output <external empty> --require-clean`, then `--verify --require-clean`) | `1d2c834` | build 0, verify 0; `build.log` has no `build_backend_compat` line (compat not applied: this interpreter resolves `_distutils_system_mod`); `attestation.json` 28,163 bytes, SHA-256 `b1f804658724509ba8e97d3e8caee3d27daa138459caa44605d069ce25b76c06`, `source_commit 1d2c834…`, `source_commit_exact true`, `pipeline_stop null`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| **S06 before**, E-DEB, clean clone, `env -i` with rails and `PATH` only | `0cd7b84` | build exit 1; stderr `RELEASE_ATTESTATION_FAILED:isolated_package_install_failed`; `failure.json` = `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}`; clone clean |
| **S06 after**, same method | `1d2c834` | build 0, `--verify --require-clean` 0; `build.log` carries `build_backend_compat=distribution_install_layout`; `attestation.json` 28,163 bytes, SHA-256 `88dd81d7703979bc14cdcbddf3e99faa8a07fd35c58f204ad61f1c8a7e5ef821`, `source_commit 1d2c834…`, `source_commit_exact true`, `pipeline_stop null`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| Index and Mirror against `0cd7b84` | `1d2c834` | 620 rows each, same keys. 28 rows on 23 paths carry exactly `current-release capture: release 1.3.0, release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`. After the label is stripped, every Index row is unchanged, and only the three self-describing Mirror rows (Index, Index checksum, Mirror) change their `sha256`/size. The 121 frozen-family Mirror rows (`artifacts/identity/`, `artifacts/math/`, `artifacts/cli/showcompat/`, `artifacts/vendor/`, `audit/ops/`) carry no label. No row carries `crd_id`; no `audit/qa/hde-crd-0002/` row |
| Release members | `1d2c834` | `catalog/manifest.json` byte-identical to `0cd7b84` (release `1.3.0`, 45 members); no changed path is a member |
| Updater-consuming test files outside #634's selected lanes (11 files: `tests/config/test_typed_bundles.py`, `tests/evidence/test_evidence_index_env.py`, `test_evidence_index_snapshot.py`, `test_evidence_index_token_sets.py`, `test_hdapi_v2_contract_inventory.py`, `test_hde_epic037_v2_adapter.py`, `tests/qa/test_epic024_bootstrap_status.py`, `tests/transport/test_internal_version_contract.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/unit/test_check_agents_md_citations.py`, `tests/qa/test_viability_generator_wrappers.py`) | `1d2c834` | **1 failed, 623 passed** (214.7 s). The failure is LR-1. Tree clean afterwards |
| `tests/qa/test_generate_epic_close_pack.py` (OBS-17 file) | `1d2c834` | 405 passed; tree clean |
| LR-1 test alone (detached worktrees) | `0cd7b84` / `c27c5e8` / `1d2c834` | **1 passed** (exit 0) / **1 failed** (exit 1) / **1 failed** (exit 1) |
| Every test file under `tests/` (`python -m pytest -q -rfE tests/`, detached worktree) | `1d2c834` | **1 failed, 4,528 passed, 3 skipped, 2 xfailed** (pytest exit 1; 1,469.9 s). The only failure is LR-1. Worktree clean afterwards (`git diff` 0, status empty) |

Exit codes above are cited only where the capture holds the producer's own status. For the two batch runs whose wrapper recorded another command's status, the result is cited from pytest's own summary line.

## 6. Requirement and obligation coverage

| Item | Plan v1.1 §7 acceptance / instruction | Status | Evidence |
| :- | :- | :- | :- |
| S06 | (1) O-10 fails before, builds and verifies after on a Debian interpreter; hosted release lane still builds and verifies | MET | §5 S06 rows (this review, on `1d2c834`); results v1.0 §4 and v1.3 §3; hosted RELEASE lane success on `d0c81ae` and `1d2c834`. Code read: the compat module is written by the builder from a constant, only for the wheel child, only when a probe in that child's own interpreter, cleaned environment and directory reports the patched backend; `_clean_child_env`, exact-source copies, `--no-index`/`--no-deps` and the failure receipts are unchanged |
| S13 | (2) the probe follows the isolated copy with no ambient `engine` | MET | `test_closure_probe_follows_the_isolated_copy_with_no_ambient_engine`, `test_closure_probe_ignores_a_different_ambient_engine` ×2, `test_closure_probe_fails_closed_when_engine_was_imported_from_elsewhere` (release-lane set, §5); the E-DEB full build passes the closure stages with no ambient `engine`. Code read: `ROOT` is inserted first when `engine` is not yet imported; every module of the import chain must resolve inside `ROOT`, or `IDENTITY_CLOSURE:ADMISSION_PROBE_NOT_ROOT_BOUND`; refusal is still true only for `INCOMPLETE_RELEASE_ROSTER` |
| S11 | (3) the engine-core test fails when the admitted `release_id` differs | MET | `test_core_evidence_binds_the_admitted_release_id` and `test_core_evidence_release_check_fails_when_the_admitted_release_id_differs` (changed-test and config/core sets, §5); `generate_engine_core_evidence.py` and the payloads unchanged |
| S12 | (4) every row for a regenerated current-release capture carries the IF-7 fields; frozen families unchanged; five validators exit 0 | MET | §5 Index/Mirror comparison (28 rows / 23 paths; frozen rows unlabelled); validators 0; encoding inside the PF12 §8.3 allowed keys (`notes`; ID-1); no new top-level key. Corrections CX-1 and CX-3 are in the landed code |
| S22 | (5) publication succeeds for a fixture HDE-CRD-0002 root and for HDE-CRD-0001, refuses HDE-CRD-0003 by name; the absent real root publishes nothing | MET | `test_crd_0002_fixture_root_publishes_beside_crd_0001`, `test_crd_publication_refuses_an_unadmitted_id_by_name`, `test_absent_admitted_crd_root_publishes_nothing`, `test_crd_index_admission_rejects_cross_crd_rows` ×2 (evidence lane); no HDE-CRD-0002 row on `main` |
| ID-2 / PD-7 | both allowed-key enforcers accept `crd_id` and refuse it together with `epic_id` (PF12 §8.3 "every serializer or validator") | MET | `check_mirror_schema.sh` diff (`OPTIONAL_KEYS` + `EPIC_CRD_EXCLUSIVE`); `_ALLOWED_INDEX_FIELDS` + `ValueError`; `test_mirror_schema_accepts_crd_id_and_refuses_epic_and_crd_together` ×3, `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together` |
| D-1 label model | labels derived from the admitted manifest; relabel through the updater alone | MET as landed, with a changed timing that later units must use (§7 LR-O3) | `_current_release_labels`: on a release change a label moves at the first updater run after the capture's owner regenerates it, not at the first updater run after the cut |
| D-2 to D-5 | admission table; validator conformance; attestation in the release lane; no member change | MET | §5; §3 |
| Exclusions (instruction §7) | — | MET | no member, manifest, canon, schema-in-canon, new key, evidence family, `crd_id` row, QA artifact, `AGENTS.md`/`README.md` edit; no skipped or `xfail` test added (diff searched) |
| Security (instruction §11; addendum 2.3 Rule 3) | — | MET | no network, no caller-environment input to any child; the probe adds no child-environment input; no secret in tests, logs, labels or records |
| Migration | none | MET | no data, schema, catalog or member change |
| Evidence obligations | PR result record; regenerated companions; no new evidence family | MET | results v1.0–v1.4; eight companions regenerated by the updater (fixed point, §5) |
| PR description | template headings, `AGENTS.md` content rules | MET | #634 body: Why, What changed, Checks run, Not in this PR, What merging does; nonclaims stated |
| Carried K-2 (PF10 addendum 2.4) | the closure keeps its test selections; the retired EPIC022 tests stay absent | MET | `test_release_closure_does_not_run_epic_closeout_assertions` unchanged (lines 617–622); the closure diff touches only the probe |
| **S03 outcome held across units** (Plan v1.1 §7 WU-PR-01, accepted; Specification S03 "recorded failures … are fixed") and WU-PR-02's own risk "Mirror consumers rejecting added fields" | every retained test passes | **NOT MET** | LR-1 (§7) |

**Plan deviations taken during PR-35, evaluated:**
- ID-35-1: CX-1 binds labels to regenerated captures.
- ID-35-2: PD-10 is superseded and the original manifest-only-cut invariant restored.
- ID-35-3: one test replaced.
- ID-35-4: CX-3, full manifest validation.
- ID-35-5: CX-4, the probe in the child's environment.
- The console-entrypoint test, listed "unchanged" in plan §8.1, gains one monkeypatch.

Each stays within instruction §6's files and the approved interfaces (IF-7's "captures the current release regenerates"; PF12 §6.2 "Do not compute an identity from a noncanonical or otherwise invalid manifest"; instruction §11). None is material in instruction §14's sense. PD-11 stands.

## 7. Findings

**LR-1 (defect; REJECT basis).**
- **Defect.** #634's updater change breaks an existing test that its CI never ran.
- **Where.** `tools/evidence/update_evidence_index.py`:
  - `_load_human_index()` (line 4145) calls `_current_release_labels(...)` → `_current_release_label()` (line 3826).
  - That runs `manifest_only_problems(ROOT / "catalog/manifest.json")` and raises `SystemExit("CURRENT_RELEASE_LABEL_MANIFEST_INVALID")` when the manifest is absent or invalid.
  - The label is needed on every run, because the updater's constant families include roster paths (for example the F07 writer artifacts).
- **Failing test.** `tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` (lines 1267–1279). It monkeypatches `indexer.ROOT` and `indexer.HUMAN_INDEX` to a temporary directory and calls `indexer._load_human_index()`.
- **Results.** 1 passed at `0cd7b84`; 1 failed at `c27c5e8` and at `1d2c834` (§5).
- **Why CI missed it.** `ci/checks/classify_ci_changes.py` registers this test file for `adapter/factory.py`, `adapter/wsgi.py`, `tools/evidence/generate_hdapi_v2_contract_inventory.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py` (lines 488–497, 645–647, 680–683), and not for `tools/evidence/update_evidence_index.py`, whose owners are `test_evidence_index_missing_state.py`, the ownership test and `tests/config/test_config_artifacts.py` (lines 727–731). Plan §11 ran the evidence, release, changed-test and qa sets, which do not include this file.
- **Affected obligations:**
  - The S03 outcome accepted with WU-PR-01: every retained test file passes in its lane.
  - WU-PR-02's own risk treatment in Plan v1.1 §7 ("Mirror consumers rejecting added fields").
  - WU-PR-03's dependency on a working base. WU-PR-03 changes `adapter/factory.py`, which selects this test.
- **Owner:** the WU-PR-02 PR engineering lineage, through a corrective per-PR plan (§8).
- **Not material.** It touches no acceptance intent, protected boundary, dependency or other unit's scope (instruction §14).

**LR-O1 (observation; CX-2 residual; reviewer independence; a correction of my advice).**
- **The residual.** After a release cut, a capture changed by something other than its owner (a stale restore, a truncated write, a forbidden hand edit) takes the new label at the next updater run.
- **Requirements unaffected.** No requirement or acceptance item is missed:
  - The S12 invariant concerns telling current from frozen captures.
  - PF12 §6.2 gives an Index/Mirror row "the owning capture's provenance; not another release-identity authority".
  - `AGENTS.md` says Index/Mirror facts never substitute for the substantive predicate.
- **The decision.** The Product Owner accepted the residual (result v1.2 §3.1).
- **Independence disclosure.** This reviewer, in this IA session, gave the recommendation the Product Owner adopted (option A). The decision is the Product Owner's; this review re-checked it against the requirements and canon above rather than relying on that advice.
- **Correction of my advice.** One supporting point in that advice was wrong as stated. I said the identity closure's currency check covers the reader_cli parity files, implying the release lane would catch a stale restore of them. It does not:
  - `build_release_attestation.py` (lines 740–780) lets the isolated closure regenerate outputs inside its copy and permits changes under the generated-evidence roots. The release lane therefore never compares tracked capture bytes with regenerated bytes.
  - The protection that exists for that family is the owner test `tests/evidence/test_determinism_gate_proofs.py::test_build_and_check_succeed_on_the_admitted_root` ("the live build reproduces the tracked outputs byte for byte"), which runs when the classifier selects it.
  - S11's binding of three engine-core payloads to the admitted `release_id` stands as stated.
  - The decision's two main reasons are unaffected: the label is not owner proof, and owner proof would change D-1.
- **Owner.** The IA carries the residual into the WU-PR-03, WU-PR-04, WU-PR-05 and WU-PR-08 instructions: Plan v1.1 §10 steps 7, 8 and 11 and the owners' `--check` modes remain the protection. It also goes to WU-DOC-01 with OBS-W2-1, so the label convention's documentation says the label is not proof that an owner ran.

**LR-O2 (observation; classifier coverage).**
- The updater has three registered owner tests, but at least 21 other test files import or run it (§5 lists those this review ran).
- An updater change therefore cannot rely on the classifier to run its consumers.
- Owner: the IA. Every later updater-changing instruction (the WU-PR-02 correction, WU-PR-07) requires a run of every test file that imports or runs the updater. A classifier owner registration is optional, and when used it is a stated finding (instruction §6).

**LR-O3 (observation for later units).** Two landed behaviors change how Plan v1.1 §10 runs for WU-PR-03, WU-PR-04, WU-PR-05 and WU-PR-08:
- **(a) Updater runs before the cut.** The updater refuses `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` whenever a member's bytes differ from the manifest (CX-3), in write and `--check` modes. The updater therefore cannot run between step 1 (member bytes final) and step 2 (cut).
- **(b) Label timing.** A roster capture takes the new release's label at the first updater run after its owner regenerates it (CX-1):
  - after step 4, for the canonical JSON gate (relabelled at step 5);
  - during step 6, for the config family;
  - at step 8, for the step-7 producers.
- **(c) Stale label.** A roster capture left byte-stable across a `release_id` change keeps its earlier label. D-1 already routes that to the IA as a finding.
- **Owner.** The IA states all three in the WU-PR-03 instruction.

**Carried observations (unchanged owners):**
- OBS-W2-1 and OBS-W2-2: doc-delta candidates, WU-DOC-01.
- OBS-W2-3: the other ambient probes. The Audit §6 S13 scopes S13 to the closure probe and calls the `ci.yml` inline probe "correct there". `run_sanity_pipeline.py` inserts its own `ROOT` first in `sys.path` when it is absent (lines 15–17). Observation only; the IA assigns no unit.
- OBS-17: `tests/qa/test_generate_epic_close_pack.py` passed locally, 405 (§5); hosted qa lane not selected. Owner: QA tool and test owner through the IA.
- O-6: not applicable here.
- AQ-1: gates WU-PR-07 only.
- PF10 addendum 2.2's downstream items: the WU-PR-03 and WU-PR-06 instructions.

## 8. Route and bounded correction

**REJECT → PR-20 — Create Detailed PR Implementation Plan — 100926.1**, for the same `WORK_UNIT_ID` WU-PR-02. It runs in a new dedicated top-level session that Nathan creates. That plan goes through its own Product Owner Proceed, then PR-30, PR-35 and PR-40. Plan v1.0's Proceed is spent and is never reused. #634's merge and review evidence are preserved and not reopened, and nothing is reverted.

**Bounded correction** (the whole corrective scope). The effective baseline stays the approved base, PR instruction v1.0 and PF10 addendum 2.3; this section extends instruction §6 by the loci it names, as a non-material correction under instruction §14:
1. **LR-1.** Make `tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` pass on `main` again, keeping its intent: superseded EPIC034 PR-04 rows are removed when their outputs are absent. Constraints:
   - Do not weaken the landed behavior. The updater still refuses an invalid or absent manifest (CX-3), and the label semantics (CX-1, IF-7) are unchanged.
   - Locus: the test file (test-only). That file is not among instruction §6's paths; this review binds it.
   - A change to `tools/evidence/update_evidence_index.py` is allowed only if the plan shows that a test-only correction cannot keep the test's intent.
2. **No further regression is in scope.** The full sweep in §5 found no failure at `1d2c834` other than LR-1. The corrective plan's own sweep confirms that at its head.
3. **A new PR result record** under `docs/ephemeral/`.

Validation the corrective plan must include:
- The corrected test fails at `1d2c834` and passes at the corrective head.
- Every test file that imports or runs `update_evidence_index.py` passes at the corrective head (LR-O2), or the full `tests/` sweep does.
- The evidence and release lane sets pass.
- The Index, Mirror and governed companions stay byte-identical (no updater output change is expected).

**Outside the correction:**
- The CX-2 residual (accepted by the Product Owner).
- The classifier, unless an owner registration is stated as a finding.
- LR-O1 and LR-O3, which go into later instructions.
- The carried observations.

**Merge order.** The correction lands before WU-PR-03 and before WU-PR-07.

**Next unit.** WU-PR-03's instruction is not issued by this review. PR-40 selects the next unit only after a complete accepted delivery, and instruction v1.0 §12 issues it "on ACCEPT". WU-PR-03 is otherwise dependency-ready: "Third; after WU-PR-01 … and WU-PR-02 (label model before rows are regenerated)", with WU-PR-01 accepted. It becomes the next stage (PR-10) when the corrected WU-PR-02 lineage is accepted.

## 9. CANON_CONFLICT_REGISTER

Carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |

No new entry. LR-1 is an implementation defect, not a canon conflict. ID-1 and ID-2 (instruction §4) apply PF12 §8.3 and §8.17 as written. The CX-1 and CX-3 corrections follow PF12 §6.2. The `CX-<n>` labels are review-finding identifiers, distinct from this register's `CR-<n>` (result v1.2 §2).

## 10. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:** a saved MERGE_OBSERVED artifact for #634; any QA, Ops, acceptance or closure artifact; a PF10 addendum; the WU-PR-03 instruction.
- **NOT EXECUTED by this review:**
  - the Codex security review (deprecated, addendum 2.3);
  - a hosted run of the regressed test;
  - the E-DEB rerun of CX-4's caller-`PYTHONPATH` case (result v1.3 §3 records it; this review re-ran S06 before/after without a caller path).
- **Pending:** the corrective plan (PR-20) and everything after it.
- **Prompt-use provenance:** the installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent, so usage is recorded here only (§13; pending, non-gating).

## 11. Recovery

No recovery is open. The resume point is PR-20 for the WU-PR-02 corrective plan. Before planning, it inspects `docs/ephemeral/HDE-CRD-0002-WU-PR-02-*`, open PRs and branches for existing corrective work.

## 12. TypeSafe reading for the receiving session (PR-20, WU-PR-02 corrective plan)

Action sent (v6): "Write, in a new dedicated session, a corrective detailed PR implementation plan for one work unit of an approved change whose first pull request merged and was then rejected at lineage review for one regression: an existing evidence test (one test in a 4,400-line test file) that the merged change to a 5,000-line evidence-index updater broke by requiring a valid release manifest on every run, to be restored without weakening that new refusal, with a reproduction before and after, a sweep of every test file that uses the updater, and a prototype in a throwaway copy. Planning only, no live run; a Product Owner Proceed, implementation, code review and a second lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.14 (confidence 0.87); rung probabilities low 0.00, medium 0.03, high 0.81, extra high 0.16, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.22, Opus 5.5 0.78 (confidence 0.56). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.63, Opus 5.5 at extra high 0.12, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.18, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T21:38:41Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T21:38:41Z; HTTP 200 in 0.76 s; 4253 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- **Notion row:** not written, as PR-40 directs. **Nathan's pick for PR-20:** not stated. **For this PR-40 session:** not stated (reading in result v1.4 §9).
- **Superseded reading with a factual error, not used.** The first text for this stage gave the test file as "a 1,300-line test file"; it has 4,424 lines. Only that phrase changed in the text above. The first reading (sent 2026-10-13T21:37:52Z; HTTP 200 in 0.78 s) was: **TypeSafe v6: Opus 5.5, high.** Effort score 2.13 (confidence 0.87); rung probabilities low 0.00, medium 0.03, high 0.81, extra high 0.16, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.23, Opus 5.5 0.77 (confidence 0.54). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.62, Opus 5.5 at extra high 0.12, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.19, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T21:37:52Z. Nathan picks the cell. Flags: none.
- **Superseded reading, not used.** Before LR-1 was found, this review scored the then-expected next stage, "PR-10 — HDE-CRD-0002 WU-PR-03 instruction" (sent 2026-10-13T21:09:42Z): **TypeSafe v6: Opus 5.5, high.** Effort score 2.35 (confidence 0.67); rung probabilities low 0.01, medium 0.06, high 0.53, extra high 0.38, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.10, Opus 5.5 0.90 (confidence 0.80). Twelve cells, computed from the two answers: Opus 5.5 at low 0.01, Opus 5.5 at medium 0.05, Opus 5.5 at high 0.48, Opus 5.5 at extra high 0.34, Opus 5.5 at max 0.02, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and high. Sent 2026-10-13T21:09:42Z. Nathan picks the cell. It is recorded for completeness only. A WU-PR-03 instruction is not the next stage, and a later PR-10 for WU-PR-03 takes its own reading.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt.
- The plan's reproduction and sweep need the E-CI environment of §5 (CPython 3.12 with CI's install), which needs package-index access for `pip install`.
- The whole `tests/` sweep took about 25 minutes here, and the evidence lane about 13.
- The Debian rehearsal environment is needed only if the plan changes `tools/evidence/build_release_attestation.py` or `tools/evidence/regenerate_identity_closure.py`, which this correction does not expect.
- No live vendor, production or database access is needed.
- This review's pull request should be merged first.

## Canon relied on

Read on `main` at `1d2c834` (`docs/pfcanon/` unchanged since `cc3dc33`):

| Decision topic | Sources and sections |
| :- | :- |
| Review authority, verdict and route | PR-40 — Review PR Work-Unit Lineage — 100926.1 (read in full: "Execute" steps 1–10, "Required result", "PRECISE IN-SCOPE DEFECT → re-plan", "Resolve the next approved Plan stage", "Accepted-final lineage protection"); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 "Change authority and exact-artifact lineage" (Proceed per detailed PR plan; PR merges remain Product Owner actions; revisions supply complete replacements) and §9.1.2 "Canon precedence and persistent sources" (canon on `main`; in-flight documents and Product Owner dispositions govern within their scope) |
| Review chain | PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 1–5 (only the Codex code review; security review absence is not a gap); addendum 2.4 (WU-PR-01 acceptance; K-2, OBS-17 and O-6 carried into WU-PR-02; addendum 2.2's items carried to WU-PR-03 and WU-PR-06) |
| S12, CX-1, CX-2, CX-3 | HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §6.2 "release_id computation" (steps 1–6; "Do not compute an identity from a noncanonical or otherwise invalid manifest"; the "Distinct source, capture, release, and evidence identities" table and the paragraph after it); §8.3 "Allowed top-level keys and unknown-key rejection" (metadata keys, `notes`, the `epic_id`/`crd_id` rule, "every serializer or validator") |
| S22 | HDE Schemas & Artifacts §8.17 "Change-container identity (normative)" |
| S03 (LR-1's affected outcome) and WU-PR-02/03 scope | Specification v1.1 rows S03, S06, S11, S12, S13, S22; Implementation Plan v1.1 §4 invariants, §7 (common paragraph; WU-PR-01, WU-PR-02 and WU-PR-03 blocks), §10, §11, §13; Audit v1.0 §5.6 and §6 S13; PR instruction v1.0 §4 (ID-1, ID-2), §6, §7, §8 (D-1 to D-5), §10, §11, §12, §14 |
| TypeSafe reading | PF10 addendum 2.1 (the reading informs Nathan's choice; no AI recommendation) |
| Operative documentation | `AGENTS.md` (canon-first rule; sole Index/Mirror writer; no hand edits; Index/Mirror facts never substitute for the substantive predicate; release identity; closed rails; pytest readiness; evidence attribution; PR descriptions) |

In-flight records read: the WU-PR-02 instruction v1.0, plan v1.0, results v1.0–v1.4; the WU-PR-01 Product Owner disposition of CR-4/CR-5 and lineage review v2.0 (format and carried items).

## 13. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38Z) |
| role/stage | continuing whole-change IA / PR-40 |
| capture time | 2026-10-13T21:38:18Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | PR-10 instruction 1; PR-20 plan 1; PR-30 implementation 1; PR-35 review resolution 1 (result v1.4 §10) |
| repository persistence | recorded here only (writer absent; pending, non-gating) |
